#!/usr/bin/env python3
"""Reorganize PSF wiki files into a logical directory structure.

Classifies .md files in python/, psf/, jython/ and moves them
to a deep directory structure. Generates redirect maps for
sphinxext-rediraffe.

Usage:
    python scripts/reorganize.py [--dry-run]
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Root of the repo (worktree)
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Exclusion patterns — MoinMoin boilerplate, system pages, spam
# ---------------------------------------------------------------------------

# Exact basenames to exclude (case-sensitive)
EXCLUDE_EXACT: set[str] = {
    # MoinMoin system pages
    "MoinMoin.md",
    "WikiName.md",
    "FortuneCookies.md",
    "WikiTipOfTheDay.md",
    "WikiTippDesTages.md",
    "CamelCase.md",
    "EditedSystemPages.md",
    "LocalBadContent.md",
    "LocalSpellingWords.md",
    "RandomPage.md",
    "SyncJobTemplate.md",
    "SlideTemplate.md",
    "ProjectTemplate.md",
    "ProjectGroupsTemplate.md",
    "HelpSystem.md",
    "HelpContents.md",
    "HelpForBeginners.md",
    "HelpForUsers.md",
    "HelpIndex.md",
    "HelpTemplate.md",
    "DocutilsTestPage.md",
    "WikiHomePage.md",
    "WikiSandkasten.md",
    "WikiToDo.md",
    "WikiCourseHandOut.md",
    "WikiKursHandOut.md",
    "LanguageSetup.md",
    "PermissionDeniedPage.md",
    "MissingPage.md",
    "MissingHomePage.md",
    "BadContent.md",
    "StartSeite.md",
    "SeiteFinden.md",
    "FehlendeSeite.md",
    "FehlendePersönlicheSeite.md",
    "NonEnglish.md",
    "UserPreferences.md",
    "Settings.md",
    "BlockedUsersGroup.md",
    "EditorsGroup.md",
    "TrustedEditorsGroup.md",
    "Admin.md",
    "AdminGroup.md",
    "MoinPagesEditorGroup.md",
    "WikiWikiWeb.md",
    "WikiCourse.md",
    "WikiKurs.md",
    "DummyPage.md",
    "XsltVersion.md",
    "Wiki沙箱.md",
    "PageD'Accueil.md",
    "SystemAdmin.md",
    "RechercherUnePage.md",
    "SeitenZugriffe.md",
    "AufgegebeneSeiten.md",
    "GesuchteSeiten.md",
    "TitelIndex.md",
    "VerwaisteSeiten.md",
    "ZufallsSeite.md",
    "AktuelleÄnderungen.md",
    "HomepageImWiki.md",
    "WikiSandkasten.md",
    # Jython specific junk
    "CategoryAaaBogusBogusBogus.md",
    "Beauty_Advice_To_Improve_With_Your_Look.md",
    "Portable_Generators_Diesel_Generators_Portable_Diesel_Generators_And_Their_Specifications.md",
    "Straightforward_Methods_Of_hair_extensions_-_An_Analysis.md",
    "asas.md",
    "atckor.md",
    "dasdad.md",
    "jythonuser.md",
    "linrh.md",
    "test.md",
    "1.md",
    # Python wiki junk
    "DeleteTestAndWelcome.md",
    "blackhawk.md",
    # PSF-specific system pages
    "CommitteeStatusReportTemplate.md",
}

# Prefix patterns to exclude
EXCLUDE_PREFIXES: list[str] = [
    "HelpOn",
    "Hilfe",
    "WikiCourse/",
    "WikiKurs/",
    "Category",
    "Kategorie",
    "HomepageVorlage",
    "HomepageGroupsTemplate",
    "HomepagePrivatePageTemplate",
    "HomepageReadPageTemplate",
    "HomepageReadWritePageTemplate",
    "HomepageTemplate",
    "SlideShowHandOutTemplate",
    "SlideShowTemplate",
    "EventStats/",
    "EventStats",
    "HilfeZu",
    "AidesDiverses",
    "FehlendeSeite",
    "FehlendePers",
    "KategorieHomepage",
    "KategorieVorlage",
]

# Non-English MoinMoin locale pages
EXCLUDE_SUFFIXES: list[str] = [
    "Language.md",
]

# Non-English system page patterns
NON_ENGLISH_SYSTEM_PATTERNS: list[re.Pattern] = [
    re.compile(r"^(Använda|Plats|Senaste|Slump|Sök|Titel|Övergivna|Önskade)"),  # Swedish
    re.compile(r"^(Rechercher|Aide|Créer|Dernières|Accueil|Accès|Page)"),  # French
    re.compile(r"^(Seite|Aktuelle|Zufalls|Verwaiste|Hilfe)"),  # German
    re.compile(r"^(Справочник|初学者)"),  # Russian/Chinese system pages
    re.compile(r"^(AnvändarInställningar|PlatsNavigering)"),
]


def is_excluded(rel_path: Path) -> bool:
    """Check if a file should be excluded based on patterns."""
    name = rel_path.name
    # The relative path within the wiki (e.g., "HelpOnFoo/Bar.md")
    inner = str(rel_path)

    if name in EXCLUDE_EXACT:
        return True

    stem = name.removesuffix(".md") if name.endswith(".md") else name
    for prefix in EXCLUDE_PREFIXES:
        if stem.startswith(prefix) or inner.startswith(prefix):
            return True

    for suffix in EXCLUDE_SUFFIXES:
        if name.endswith(suffix) and len(stem) > 10:
            # Only exclude long *Language.md files (locale pages)
            # but not things like "ProgrammingLanguage.md"
            pass

    for pat in NON_ENGLISH_SYSTEM_PATTERNS:
        if pat.match(stem):
            return True

    # EventStats directory
    if "EventStats" in inner.split("/"):
        return True

    return False


# ---------------------------------------------------------------------------
# Classification rules for python/
# ---------------------------------------------------------------------------

# Person page detection: CamelCase FirstLast or "First Last.md"
_CAMELCASE_PERSON = re.compile(
    r"^[A-Z][a-z]+[A-Z][a-z]+\.md$"
)
_QUOTED_PERSON = re.compile(
    r"^[A-Z][a-z]+(?:[-'][A-Za-z]+)* [A-Z][a-z]+.*\.md$"
)

# Known non-person CamelCase pages (libraries, concepts, etc.)
NON_PERSON_CAMELCASE: set[str] = {
    "ActivePython", "ActiveState", "AdapterRegistry", "AbstractBaseClasses",
    "AlternateLambdaSyntax", "AlternativeDescriptionOfProperty",
    "AlternativePathClass", "AlternativePathDiscussion",
    "AlternativePathModule", "AlternativePathModuleTests",
    "AppsWithPythonScripting", "AutoHotkey",
    "BeginnersGuide", "BitPim", "BooLanguage", "BuildBot",
    "CherryPy", "CloudPyPI", "CodeIntelligence", "CodingProjectIdeas",
    "ComputedAttributesUsingPropertyObjects", "ConfigParser",
    "CorbaPython", "CreatePythonExtensions",
    "DatabaseInterfaces", "DatabaseProgramming", "DataRepresentation",
    "DesignByContract", "DesktopProgramming",
    "DistributedProgramming", "DjangoNotes",
    "EasyInstall", "ExtensionClass",
    "GameProgramming", "GuiProgramming", "GuiBooks",
    "HierConfig", "HandlingExceptions",
    "IntegratedDevelopmentEnvironments", "InternetProgramming",
    "LanguageParsing", "LibraryCatalog",
    "MacPython", "MapReduce", "MetaClasses",
    "MovingToPythonFromOtherLanguages",
    "NetBeans", "NetworkProgramming", "NumericAndScientific",
    "ObserverPattern", "OperatorsOverview",
    "PackagingTutorial", "PointsAndRectangles",
    "PoweredBy", "ProjectsForLearning",
    "PythonAdvocacy", "PythonBooks", "PythonConferences",
    "PythonConsulting", "PythonEditors", "PythonEvents",
    "PythonForArtificialIntelligence",
    "PythonForScientificComputing",
    "PythonGameLibraries", "PythonGraphics",
    "PythonHosting", "PythonImplementations",
    "PythonInMusic", "PythonPeriodicals",
    "PythonSpeed", "PythonTraining", "PythonWebsite",
    "ScriptableInPython", "ShowMeDo",
    "SimplePrograms", "SimpleXMLRPCServer",
    "SpeedUp", "StackOverflow",
    "StructureAnnotation", "StructuredText",
    "SummerOfCode", "SwitchStatement",
    "TestDrivenDevelopment", "TkInter",
    "TimeComplexity", "TurboGears",
    "UnicodeData", "UsingPickle",
    "VirtualEnv",
    "WebFrameworks", "WebProgramming",
    "WindowsCompilers", "WxPython",
    "XmlRpc", "XmlParsing",
    # Frameworks / tools
    "Albatross", "Aquarium", "Django", "Flask", "Twisted",
    "Zope", "Plone", "Pylons", "Quixote", "Tornado",
    "PyGame", "PyOpenGL", "PyGTK", "PyQt",
    "NumPy", "SciPy", "Pyrex", "Cython",
    "DistUtils", "SetupTools", "VirtualEnv", "Buildout",
    "BoostPython",
}


def _looks_like_person(stem: str) -> bool:
    """Heuristic: does this filename look like a person's name?"""
    fname = stem + ".md"
    # Quoted "First Last.md"
    if _QUOTED_PERSON.match(fname):
        return True
    # CamelCase but not a known concept/library
    if _CAMELCASE_PERSON.match(fname):
        if stem in NON_PERSON_CAMELCASE:
            return False
        # Additional heuristic: if it has more than 2 capital letters
        # in sequence (like "PyGame"), it's probably not a person
        caps = re.findall(r"[A-Z]", stem)
        if len(caps) == 2:
            # Two capitals = FirstLast pattern, likely a person
            return True
        if len(caps) > 2:
            # Could be multi-name or could be acronym-heavy concept
            # Check: does it look like FirstMiddleLast or FirstMcLast?
            parts = re.findall(r"[A-Z][a-z]+", stem)
            if len(parts) >= 2 and all(len(p) >= 2 for p in parts):
                # All parts are real words (2+ chars), likely a person
                # unless it's a known compound concept
                return True
        return False
    # lowercase or other patterns: not a person
    return False


# Classification prefix patterns for python/
# Order matters — first match wins
PYTHON_RULES: list[tuple[str, list[str]]] = [
    # Conferences
    ("python/conferences/pycon/", [
        "PyCon", "PyConDC", "PyConPlanning", "PyConAPAC",
        "PyConIndia", "PyCon ", "PyConBrett", "PyConPostMortem",
        "PyConChet",
    ]),
    ("python/conferences/europython/", [
        "EuroPython", "EuroPy",
    ]),
    ("python/conferences/regional/", [
        "PyOhio", "AfpyCamp", "EuroScipy", "PythonBarCamp",
        "PythonConferences", "PythonEvents",
    ]),

    # Getting started / beginners
    ("python/getting-started/", [
        "BeginnersGuide", "LearnPython", "SimplePrograms",
        "MovingToPythonFromOtherLanguages", "ForLoops",
        "WhileLoop", "ProjectsForLearning", "CodingProjectIdeas",
        "ProblemSets",
    ]),

    # Guides / HowTo
    ("python/guides/", [
        "HowTo", "How to", "How Tkinter",
        "HandlingExceptions", "Powerful Python One-Liners",
    ]),

    # Web
    ("python/web/", [
        "WebProgramming", "WebFrameworks", "Django", "Flask",
        "WSGI", "Zope", "Plone", "Twisted", "CherryPy",
        "TurboGears", "Pylons", "Quixote", "Tornado",
        "Albatross", "Aquarium", "PoundPythonWeb",
        "Dojo-NL", "DjangoMeeting", "DjangoNotes",
    ]),

    # Science
    ("python/science/", [
        "NumPy", "SciPy", "Numeric", "NumericAndScientific",
        "ScientificProgramming", "PythonForScientificComputing",
        "PythonForArtificialIntelligence", "MapReduce",
    ]),

    # GUI
    ("python/gui/", [
        "GuiProgramming", "GuiBooks", "TkInter", "WxPython",
        "PyQt", "PyGTK", "PyWebkitGtk", "DesktopProgramming",
    ]),

    # Database
    ("python/database/", [
        "Database", "MySQL", "PostgreSQL", "SQLite", "Oracle",
        "DbApi", "SQL", "ADO",
    ]),

    # Editors
    ("python/editors/", [
        "IDE", "IDLE", "Emacs", "Vim", "Eclipse", "Wing",
        "PyCharm", "IntegratedDevelopmentEnvironments",
        "PythonEditors", "NetBeans", "CodeIntelligence",
    ]),

    # Packaging
    ("python/packaging/", [
        "Pip", "PyPI", "Setuptools", "Distutils", "Packaging",
        "Virtualenv", "VirtualEnv", "Distribute", "EasyInstall",
        "SetupTools", "Buildout", "buildout", "CloudPyPI",
        "PackagingTutorial", "A new pypi module",
    ]),

    # Python 3 migration
    ("python/py3/", [
        "2to3", "3to2", "Porting", "Python3", "Py3k",
        "Py3Ext", "2and3", "Python2orPython3",
        "5YearsOfPython3", "PortingToPy3k",
        "Python3PortingStatus",
    ]),

    # Language / internals
    ("python/language/", [
        "Decorators", "Generators", "Iterator", "Concurrency",
        "GIL", "AST", "MetaClasses", "DesignByContract",
        "SwitchStatement", "AlternateLambdaSyntax",
        "AlternativeDescription", "AlternativePath",
        "AbstractBaseClasses", "ConfigParser", "TimeComplexity",
        "AdapterRegistry", "ExtensionClass", "ObserverPattern",
        "OperatorsOverview", "ComputedAttributes",
        "StructureAnnotation", "StructuredText",
        "DataRepresentation", "LanguageParsing",
        "UnicodeData", "ByteplayDoc",
    ]),

    # Books
    ("python/books/", [
        "Books", "IntroductoryBooks", "AdvancedBooks",
        "ReferenceBooks", "FreeBooks", "NonEnglishBooks",
        "ScientificProgrammingBooks", "NetworkProgrammingBooks",
        "SystemAdministrationBooks", "Any good Python",
        "PythonBooks", "PythonPeriodicals",
        "KoreanPythonBooks",
    ]),

    # Community / user groups
    ("python/community/", [
        "LocalUserGroups", "BayPiggies", "Advocacy",
        "AdvocacyAccomplishments", "AdvocacyWritingTasks",
        "PythonAdvocacy", "MarketingPython",
        "GetInvolved", "PythonIrcChannel",
        "AbqPython", "AthensPUG", "BangPypers",
        "FrontRangePythoneers", "OmahaPythonUserGroup",
        "PhoenixGeoPythonGroup", "PortlandPythonUserGroup",
        "PUB", "PUN", "VanPyZ",
        "Ncr-Python", "PythonDiscourseIdeas",
        "PythonWikiMaintainers",
    ]),

    # Testing
    ("python/testing/", [
        "Testing", "PyTest", "DocTest", "UnitTest",
        "TestDrivenDevelopment",
    ]),

    # Networking
    ("python/networking/", [
        "SSL", "TCP", "IRC", "DistributedProgramming",
        "NetworkProgramming", "InternetProgramming",
        "SimpleXMLRPCServer", "XmlRpc", "CorbaPython",
    ]),

    # Multimedia / games
    ("python/multimedia/", [
        "PyGame", "GameProgramming", "Audio", "OpenGL",
        "PIL", "PythonGraphics", "PythonGameLibraries",
        "PythonInMusic", "PyOpenGL", "ShowMeDo",
    ]),

    # Platforms
    ("python/platforms/", [
        "Windows", "Mac", "Linux", "Py2Exe", "MacPython",
        "Android", "ActivePython", "ActiveState",
        "WindowsCompilers", "Win32All",
    ]),

    # Security
    ("python/security/", [
        "Security", "Cryptography", "SandboxedPython",
    ]),

    # Sprints
    ("python/sprints/", [
        "Sprint",
    ]),

    # Education
    ("python/education/", [
        "Teaching", "Schools", "EduSig", "Education",
        "SchoolsUsingPython",
    ]),

    # Documentation
    ("python/documentation/", [
        "Sphinx", "DocUtils", "DocumentationTools",
        "Documentation", "DocsCoordination",
    ]),

    # Infrastructure
    ("python/infrastructure/", [
        "PythonWebsite", "Tracker", "BuildBot",
        "SiteImprovements", "CallForTrackers",
        "PyBots", "PloneOrgMigration",
        "PyDevSummaries",
    ]),

    # Implementations
    ("python/implementations/", [
        "CPython", "PyPy", "IronPython", "Embedding",
        "Extension", "ctypes", "CreatePythonExtensions",
        "BoostPython", "boost.python", "Pyrex", "Cython",
        "PythonImplementations", "Dabo", "BitPim",
        "BooLanguage",
    ]),

    # Performance
    ("python/performance/", [
        "NeedForSpeed", "PythonSpeed", "SpeedUp", "Profil",
    ]),

    # Summer of Code
    ("python/soc/", [
        "SummerOfCode", "GSoC", "GoogleCodeIn",
        "Outreachy", "OPW", "CodeIn",
    ]),

    # PSF-related pages in python wiki
    ("python/psf/", [
        "PythonSoftwareFoundation", "PythonCd",
        "PSF Python Job Board", "PSF ",
        "EducationalCd",
    ]),

    # Libraries (general)
    ("python/libraries/", [
        "AppsWithPythonScripting", "ScriptableInPython",
        "LibraryCatalog", "PoweredBy",
        "PythonHosting", "4Suite",
        "HierConfig", "ACC", "IPSS",
        "UsingPickle", "AutoHotkey",
    ]),

    # I18n
    ("python/i18n/", [
        "初学者入门", "СправочникПоСинтаксису",
    ]),
]


def classify_python(rel_path: Path) -> str:
    """Classify a python/ file into a target directory."""
    stem = rel_path.stem
    name = rel_path.name
    inner = str(rel_path)  # path within python/ (e.g. "Foo/Bar.md")

    # If it's already in a subdirectory, keep context
    parts = inner.split("/")

    # Check rules by prefix match
    for target_dir, prefixes in PYTHON_RULES:
        for prefix in prefixes:
            if stem.startswith(prefix) or name.startswith(prefix):
                return target_dir
            # Also check if the first directory component matches
            if len(parts) > 1 and parts[0].startswith(prefix):
                return target_dir

    # Person pages
    if _looks_like_person(stem):
        return "python/people/"

    # Quoted person names with hyphens/special chars
    if _QUOTED_PERSON.match(name):
        return "python/people/"

    # Catch-all
    return "python/archive/"


# ---------------------------------------------------------------------------
# Classification rules for psf/
# ---------------------------------------------------------------------------

PSF_ABOUT = {"FrontPage", "Contents", "StatementOfValues", "CodeOfConduct",
             "WikiInstructions", "reference"}
PSF_GOVERNANCE = {"NewMembershipModel", "NewMember", "MembershipModelTalks",
                  "MembershipModelVisualization", "ProposalsForDiscussion",
                  "Declined_Nominations", "Info for new PSF members",
                  "CiviCRMImport", "SurveyQuestions"}
PSF_MARKETING = {"Logo", "PSF Logo", "PSF Logos", "Python Logos",
                 "PSF Press Kit", "PSF Python Brochure",
                 "PSF Conference Kit", "Merchandise", "CallForLogos"}
PSF_COMMS = {"PSFBlog", "Communications", "CommunicationChairProcesses",
             "Community Conference Reports", "Staff Conference Reports",
             "Community Relations"}
PSF_PACKAGING = {"PackagingSprints", "WarehouseRoadmap",
                 "WarehousePackageMaintainerTesting",
                 "Pip2020DonorFundedRoadmap",
                 "Fundable Packaging Improvements"}


def classify_psf(rel_path: Path) -> str:
    """Classify a psf/ file into a target directory."""
    stem = rel_path.stem
    inner = str(rel_path)
    parts = inner.split("/")

    # Working groups (directories and pages)
    if "WG" in stem or (len(parts) > 1 and "WG" in parts[0]):
        return "psf/working-groups/"
    if stem.endswith("WGGroup"):
        return "psf/people/"

    # About
    if stem in PSF_ABOUT:
        return "psf/about/"

    # Governance
    if stem in PSF_GOVERNANCE or stem.startswith("Bylaws"):
        return "psf/governance/"

    # Marketing
    if stem in PSF_MARKETING:
        return "psf/marketing/"

    # Communications
    if stem in PSF_COMMS or (len(parts) > 1 and parts[0] == "Communications"):
        return "psf/communications/"

    # Packaging
    if stem in PSF_PACKAGING:
        return "psf/packaging/"

    # Howto
    if len(parts) > 1 and parts[0] == "howto":
        return "psf/governance/"

    # Reference
    if len(parts) > 1 and parts[0] == "reference":
        return "psf/governance/"

    # Education
    if stem.startswith("Education") or stem.startswith("PythonEdu"):
        return "psf/working-groups/"

    # Person pages
    if _looks_like_person(stem):
        return "psf/people/"
    # Quoted person names in psf
    if _QUOTED_PERSON.match(stem + ".md"):
        return "psf/people/"

    # Lowercase single-word filenames that look like usernames
    if re.match(r"^[a-z][a-z0-9._]+$", stem) and len(stem) < 25:
        return "psf/people/"

    # Names with dots like "Casper.dcl"
    if "." in stem and not stem.startswith(("Example", "PSF")):
        return "psf/people/"

    return "psf/about/"


# ---------------------------------------------------------------------------
# Classification rules for jython/
# ---------------------------------------------------------------------------

JYTHON_ABOUT = {"FrontPage", "WhyJython", "JythonLogo", "JythonNews",
                "IrcChannel", "JythonOrgRedesign"}
JYTHON_GETTING_STARTED = {"DownloadInstructions", "InstallationDetails",
                          "InstallationInstructions", "InstallationInstructions2",
                          "InstallingJython", "LearningJython",
                          "JythonBibliography", "DocumentationAndEducation"}
JYTHON_USER_GUIDE = {"UserGuide", "UserGuide11", "JythonUserGuide",
                     "Jython User Guide", "NewUsersGuide",
                     "ConsoleChoices", "ReadlineSetup", "SimpleApp",
                     "PyServlet", "WebSphere"}
JYTHON_FAQ_PREFIX = "JythonFaq"
JYTHON_DEV_GUIDE = {"JythonDeveloperGuide", "CodingStandards",
                    "HowToReleaseJython", "DeveloperFAQ",
                    "PatchGuidelines", "ReportingBugs",
                    "TestingJython", "TestFailures",
                    "WhosDoingWhat", "MovingJythonForward",
                    "RoadMap", "JythonReleaseNotes",
                    "Jython25BackwardsIncompatibilities",
                    "HowToGetInvolved", "SvnToHgMigration",
                    "WebsiteBuilderSetup", "SourceForge",
                    "MigrateBugtests", "VersionTransition",
                    "UpgradeTo25CPythonLib", "RelicensingJython"}
JYTHON_INTERNALS = {"ImplementNewType", "ImplementSequenceType",
                    "IntegerConversion", "NewStyleClasses",
                    "GeneratedDerivedClasses", "MethodDispatch",
                    "JythonCompiler", "ReplaceJythonc",
                    "BufferProtocol", "PythonTypesInJava",
                    "CodeSpeedupExperiments", "PyFileBenchmarks",
                    "PerformanceEnhancements", "CollectionsIntegration",
                    "JepIndex", "JepGuidelines", "NewProposal",
                    "PackageScanning", "SysPackageManager",
                    "ExposeAnnotations", "Jython3000",
                    "ThreadLocalVariables", "BiggerTasks",
                    "DateTimeModule", "ComparisonJavaJython"}
JYTHON_MODULES = {"ModulePorting", "ModulesOverview", "AbsentModules",
                  "NewSocketModule", "SelectModule", "SetsModule",
                  "SSLModule", "UnicodeData",
                  "DjangoOnJython", "PylonsOnJython", "PylonsOnJythonOld",
                  "TwistedOnJython", "MercurialOnJython",
                  "SetuptoolsOnJython", "SqlAlchemyOnJython",
                  "JavaLibraries", "JavaScript"}
JYTHON_EXAMPLES = {"SwingExamples", "SwingSampler", "SwingWorker",
                   "TabbedExample", "JtreeExample", "ADB SwingExamples",
                   "DatabaseExamples", "CoreJythonExamples",
                   "OtherExamples", "XmlRelatedExamples",
                   "ApacheDerby", "Log4jExample", "PoiExample",
                   "EasterJar", "RSMD.py", "JythonNutpad",
                   "JythonClassesInJava", "JythonModulesInJava",
                   "PyServlet"}
JYTHON_COMMUNITY = {"WhosWho", "JythonUsers", "JythonEditors",
                    "SummerOfCode", "JythonSprint", "BofTopics"}
JYTHON_NEWSLETTER = {"JythonMonthly"}


def classify_jython(rel_path: Path) -> str:
    """Classify a jython/ file into a target directory."""
    stem = rel_path.stem
    inner = str(rel_path)
    parts = inner.split("/")

    # Newsletter
    if stem.startswith("JythonMonthly") or (len(parts) > 1 and parts[0] == "JythonMonthly"):
        return "jython/newsletter/"

    # FAQ
    if stem.startswith(JYTHON_FAQ_PREFIX) or (len(parts) > 1 and parts[0].startswith(JYTHON_FAQ_PREFIX)):
        return "jython/faq/"

    # Developer guide (also check subdirectory)
    if stem in JYTHON_DEV_GUIDE or (len(parts) > 1 and parts[0] in JYTHON_DEV_GUIDE):
        return "jython/developer-guide/"
    if stem.startswith("JythonDeveloperGuide") or (len(parts) > 1 and parts[0].startswith("JythonDeveloperGuide")):
        return "jython/developer-guide/"

    # About
    if stem in JYTHON_ABOUT:
        return "jython/about/"

    # Getting started
    if stem in JYTHON_GETTING_STARTED:
        return "jython/getting-started/"

    # User guide
    if stem in JYTHON_USER_GUIDE:
        return "jython/user-guide/"

    # Internals
    if stem in JYTHON_INTERNALS:
        return "jython/internals/"
    if stem.startswith("CodeSpeedupExperiments") or (len(parts) > 1 and parts[0].startswith("CodeSpeedupExperiments")):
        return "jython/internals/"
    if stem.startswith("CollectionsIntegration") or (len(parts) > 1 and parts[0].startswith("CollectionsIntegration")):
        return "jython/internals/"
    if stem.startswith("ShashankBharadwaj") or (len(parts) > 1 and parts[0].startswith("ShashankBharadwaj")):
        return "jython/internals/"

    # Modules
    if stem in JYTHON_MODULES:
        return "jython/modules/"

    # Examples
    if stem in JYTHON_EXAMPLES:
        return "jython/examples/"

    # Community
    if stem in JYTHON_COMMUNITY:
        return "jython/community/"

    # Person pages
    if _looks_like_person(stem):
        return "jython/people/"
    if _QUOTED_PERSON.match(stem + ".md"):
        return "jython/people/"

    # Other user pages
    if stem == "OtherUser" or (len(parts) > 1 and parts[0] == "OtherUser"):
        return "jython/people/"

    return "jython/about/"


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def collect_files(wiki_dir: str) -> list[Path]:
    """Collect all .md files in a wiki directory (relative to it)."""
    base = REPO_ROOT / wiki_dir
    files = []
    for md in sorted(base.rglob("*.md")):
        rel = md.relative_to(base)
        if "_attachments" in str(rel):
            continue
        files.append(rel)
    return files


def compute_moves(dry_run: bool = False) -> dict[str, str]:
    """Compute all file moves and return the redirect map."""
    redirects: dict[str, str] = {}
    excluded: list[str] = []
    moves: list[tuple[str, str]] = []

    for wiki in ("python", "psf", "jython"):
        files = collect_files(wiki)
        for rel in files:
            old_path = f"{wiki}/{rel}"

            # Skip index files at top level
            if rel.name == "index.md" and len(rel.parts) == 1:
                continue

            # Check exclusion
            if is_excluded(rel):
                excluded.append(old_path)
                continue

            # Classify
            if wiki == "python":
                target_dir = classify_python(rel)
            elif wiki == "psf":
                target_dir = classify_psf(rel)
            else:
                target_dir = classify_jython(rel)

            # Compute new path
            if len(rel.parts) == 1:
                # Top-level file → move into category dir
                new_path = target_dir + str(rel)
            else:
                # File in subdirectory — preserve relative structure under target
                new_path = target_dir + str(rel)

            # Skip if already in the right place
            if old_path == new_path:
                continue

            # Skip if source doesn't exist
            src = REPO_ROOT / old_path
            if not src.exists():
                continue

            moves.append((old_path, new_path))
            # Redirect map uses paths without .md extension (Sphinx docnames)
            old_docname = old_path.removesuffix(".md")
            new_docname = new_path.removesuffix(".md")
            redirects[old_docname] = new_docname

    print(f"Files to exclude: {len(excluded)}")
    print(f"Files to move: {len(moves)}")
    print(f"Redirects: {len(redirects)}")

    if dry_run:
        print("\n--- Exclusions (sample) ---")
        for p in excluded[:20]:
            print(f"  EXCLUDE: {p}")
        print("\n--- Moves (sample) ---")
        for old, new in moves[:30]:
            print(f"  {old} -> {new}")
        return redirects

    # Execute moves
    for old_path, new_path in moves:
        src = REPO_ROOT / old_path
        dst = REPO_ROOT / new_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        # Use git mv for tracked files, shutil.move for untracked
        try:
            subprocess.run(
                ["git", "mv", str(src), str(dst)],
                cwd=REPO_ROOT, check=True, capture_output=True,
            )
        except subprocess.CalledProcessError:
            # Fallback to regular move
            shutil.move(str(src), str(dst))

    # Move excluded files to _exclude/
    exclude_dir = REPO_ROOT / "_exclude"
    for p in excluded:
        src = REPO_ROOT / p
        if not src.exists():
            continue
        dst = exclude_dir / p
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            subprocess.run(
                ["git", "mv", str(src), str(dst)],
                cwd=REPO_ROOT, check=True, capture_output=True,
            )
        except subprocess.CalledProcessError:
            shutil.move(str(src), str(dst))

    # Also move _attachments directories alongside their pages
    for old_path, new_path in moves:
        old_dir = Path(old_path).parent
        new_dir = Path(new_path).parent
        # Check for _attachments with MoinMoin-encoded name
        stem = Path(old_path).stem
        wiki = old_path.split("/")[0]
        attach_dir = REPO_ROOT / wiki / "_attachments"
        if attach_dir.exists():
            # MoinMoin encodes subdirectories as (2f) in attachment dirs
            for adir in attach_dir.iterdir():
                if adir.is_dir() and _decode_moin(adir.name) == stem:
                    new_attach = REPO_ROOT / new_dir / "_attachments" / adir.name
                    new_attach.parent.mkdir(parents=True, exist_ok=True)
                    # Skip attachment moves for now — too complex
                    break

    return redirects


def _decode_moin(name: str) -> str:
    """Decode MoinMoin URL encoding: (2f) -> /, (20) -> space, etc."""
    result = name
    result = re.sub(r"\(([0-9a-fA-F]{2})\)", lambda m: chr(int(m.group(1), 16)), result)
    return result


def generate_moin_redirects() -> dict[str, str]:
    """Generate MoinMoin URL -> flat path redirect mappings.

    MoinMoin encoded URLs like Page(2f)SubPage map to Page/SubPage.
    These get chained with the reorganization redirects.
    """
    moin_redirects: dict[str, str] = {}

    # Scan _attachments directories for MoinMoin-encoded names
    # to discover the encoding patterns used
    for wiki in ("python", "psf", "jython"):
        attach_dir = REPO_ROOT / wiki / "_attachments"
        if not attach_dir.exists():
            continue
        for adir in attach_dir.iterdir():
            if not adir.is_dir():
                continue
            decoded = _decode_moin(adir.name)
            if decoded != adir.name:
                # This was a MoinMoin-encoded path
                encoded_docname = f"moin/{adir.name}"
                decoded_docname = f"{wiki}/{decoded}"
                moin_redirects[encoded_docname] = decoded_docname

    return moin_redirects


def generate_index_files() -> None:
    """Generate index.md files for each new directory."""
    # Find all directories that contain .md files
    dirs_with_files: dict[str, list[str]] = {}

    for wiki in ("python", "psf", "jython"):
        base = REPO_ROOT / wiki
        for md in sorted(base.rglob("*.md")):
            if "_attachments" in str(md) or "_exclude" in str(md):
                continue
            rel = md.relative_to(REPO_ROOT)
            parent = str(rel.parent)
            name = rel.stem
            if name == "index":
                continue
            dirs_with_files.setdefault(parent, []).append(name)

    # Directory titles
    DIR_TITLES: dict[str, str] = {
        "python": "Python Wiki",
        "python/people": "People",
        "python/conferences": "Conferences",
        "python/conferences/pycon": "PyCon",
        "python/conferences/europython": "EuroPython",
        "python/conferences/regional": "Regional Conferences",
        "python/getting-started": "Getting Started",
        "python/guides": "Guides & How-Tos",
        "python/web": "Web Development",
        "python/science": "Scientific Computing",
        "python/gui": "GUI Programming",
        "python/database": "Database Programming",
        "python/editors": "Editors & IDEs",
        "python/packaging": "Packaging & Distribution",
        "python/py3": "Python 3 Migration",
        "python/language": "Language & Internals",
        "python/books": "Books & Publications",
        "python/community": "Community & User Groups",
        "python/testing": "Testing",
        "python/networking": "Networking",
        "python/multimedia": "Multimedia & Games",
        "python/platforms": "Platform-Specific",
        "python/security": "Security",
        "python/sprints": "Sprints",
        "python/education": "Education",
        "python/documentation": "Documentation Tools",
        "python/infrastructure": "Infrastructure",
        "python/implementations": "Python Implementations",
        "python/performance": "Performance",
        "python/soc": "Summer of Code",
        "python/psf": "Python Software Foundation",
        "python/libraries": "Libraries & Tools",
        "python/i18n": "International Content",
        "python/archive": "Archive",
        "psf": "PSF Wiki",
        "psf/about": "About the PSF",
        "psf/governance": "Governance",
        "psf/working-groups": "Working Groups",
        "psf/people": "People",
        "psf/communications": "Communications",
        "psf/marketing": "Marketing & Branding",
        "psf/packaging": "Packaging",
        "jython": "Jython Wiki",
        "jython/about": "About Jython",
        "jython/getting-started": "Getting Started",
        "jython/user-guide": "User Guide",
        "jython/faq": "FAQ",
        "jython/developer-guide": "Developer Guide",
        "jython/internals": "Internals",
        "jython/modules": "Modules & Compatibility",
        "jython/examples": "Examples",
        "jython/community": "Community",
        "jython/newsletter": "Jython Monthly",
        "jython/people": "People",
    }

    for dir_path, files in sorted(dirs_with_files.items()):
        index_path = REPO_ROOT / dir_path / "index.md"
        title = DIR_TITLES.get(dir_path, dir_path.split("/")[-1].replace("-", " ").title())

        # Check for subdirectories that also have indexes
        subdirs = []
        for other_dir in dirs_with_files:
            if other_dir.startswith(dir_path + "/") and other_dir.count("/") == dir_path.count("/") + 1:
                subdirs.append(other_dir.split("/")[-1] + "/index")

        # Build toctree
        entries = sorted(subdirs) + sorted(files)

        # Limit toctree for very large directories (people, archive)
        content = f"# {title}\n\n"

        if len(entries) > 200:
            content += f"This section contains {len(entries)} pages.\n\n"

        content += "```{toctree}\n"
        content += ":maxdepth: 1\n"
        if len(entries) > 50:
            content += ":hidden:\n"
        content += "\n"
        for entry in entries:
            content += f"{entry}\n"
        content += "```\n"

        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(content)


def fix_internal_links(redirects: dict[str, str]) -> None:
    """Rewrite internal links in .md files to use new paths."""
    if not redirects:
        return

    link_pattern = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

    for wiki in ("python", "psf", "jython"):
        base = REPO_ROOT / wiki
        for md in base.rglob("*.md"):
            if "_attachments" in str(md) or "_exclude" in str(md):
                continue
            try:
                text = md.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue

            def replace_link(m: re.Match) -> str:
                label = m.group(1)
                href = m.group(2)
                # Only fix internal links (not http/https)
                if href.startswith(("http://", "https://", "#", "mailto:")):
                    return m.group(0)
                # Normalize the href to a docname
                docname = href.removesuffix(".md").removesuffix("/")
                if docname in redirects:
                    new_href = redirects[docname]
                    if href.endswith(".md"):
                        new_href += ".md"
                    return f"[{label}]({new_href})"
                return m.group(0)

            new_text = link_pattern.sub(replace_link, text)
            if new_text != text:
                md.write_text(new_text, encoding="utf-8")


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("PSF Wiki Reorganization")
    print("=" * 60)
    print(f"Repo root: {REPO_ROOT}")
    print(f"Dry run: {dry_run}")
    print()

    # Step 1: Compute moves and generate redirect map
    redirects = compute_moves(dry_run=dry_run)

    # Step 2: Generate MoinMoin URL redirects
    moin_redirects = generate_moin_redirects()
    print(f"MoinMoin URL redirects: {len(moin_redirects)}")

    # Chain: if moin redirect points to an old path that was moved,
    # update to point to the new path
    for moin_url, flat_path in list(moin_redirects.items()):
        if flat_path in redirects:
            moin_redirects[moin_url] = redirects[flat_path]

    # Merge all redirects
    all_redirects = {**redirects, **moin_redirects}
    print(f"Total redirects: {len(all_redirects)}")

    if dry_run:
        print("\n--- MoinMoin redirects (sample) ---")
        for old, new in list(moin_redirects.items())[:10]:
            print(f"  {old} -> {new}")
        return

    # Write redirect maps
    redirects_path = REPO_ROOT / "_redirects.json"
    redirects_path.write_text(json.dumps(all_redirects, indent=2, ensure_ascii=False))
    print(f"Wrote {redirects_path}")

    moin_path = REPO_ROOT / "_redirects_moin.json"
    moin_path.write_text(json.dumps(moin_redirects, indent=2, ensure_ascii=False))
    print(f"Wrote {moin_path}")

    # Step 3: Generate index files
    print("\nGenerating index files...")
    generate_index_files()

    # Step 4: Fix internal links
    print("Fixing internal links...")
    fix_internal_links(all_redirects)

    print("\nDone!")


if __name__ == "__main__":
    main()
