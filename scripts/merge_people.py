#!/usr/bin/env python3
"""Merge all people/ directories into a single top-level people/ directory.

Collects person pages from python/people/, psf/people/, and jython/people/
into a unified people/ directory. Non-person content that ended up in
python/people/ (MoinMoin user subpages) gets moved to python/archive/.

Usage:
    python scripts/merge_people.py [--dry-run]
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Person detection (borrowed from reorganize.py)
# ---------------------------------------------------------------------------

_CAMELCASE_PERSON = re.compile(r"^[A-Z][a-z]+[A-Z][a-z]+$")
_QUOTED_PERSON = re.compile(r"^[A-Z][a-z]+(?:[-'][A-Za-z]+)* [A-Z][a-z]+.*$")

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
    "Albatross", "Aquarium", "Django", "Flask", "Twisted",
    "Zope", "Plone", "Pylons", "Quixote", "Tornado",
    "PyGame", "PyOpenGL", "PyGTK", "PyQt",
    "NumPy", "SciPy", "Pyrex", "Cython",
    "DistUtils", "SetupTools", "Buildout",
    "BoostPython",
}

# Known non-person directories in python/people/
NON_PERSON_DIRS: set[str] = {
    "Admin", "Asking for Help", "Email SIG", "JAM",
    "Podcast", "PythonLibraryReference",
}

# Known non-person entries in jython/people/
JYTHON_NON_PERSON: dict[str, str] = {
    "SummerOfCode": "jython/community/",
}


def _looks_like_person(stem: str) -> bool:
    """Heuristic: does this filename look like a person's name?"""
    if _QUOTED_PERSON.match(stem):
        return True
    if _CAMELCASE_PERSON.match(stem):
        if stem in NON_PERSON_CAMELCASE:
            return False
        caps = re.findall(r"[A-Z]", stem)
        if len(caps) == 2:
            return True
        if len(caps) > 2:
            parts = re.findall(r"[A-Z][a-z]+", stem)
            if len(parts) >= 2 and all(len(p) >= 2 for p in parts):
                return True
        return False
    # Lowercase usernames (psf-style)
    if re.match(r"^[a-z][a-z0-9._]+$", stem) and len(stem) < 25:
        return True
    # Names with dots like "Casper.dcl"
    if "." in stem and not stem.startswith(("Example", "PSF")):
        return True
    return False


# ---------------------------------------------------------------------------
# Non-person patterns for python/people/ entries
# These are MoinMoin user subpages that are not person pages
# ---------------------------------------------------------------------------

# Prefixes that indicate non-person content
_NON_PERSON_PREFIXES = [
    "App", "Array", "Article", "Ask",
    "Beginners", "Bit", "Bitwise", "Black", "Boa", "Boston", "Boulder",
    "Box", "Brain", "Bug", "Build", "Bundle", "Bytes",
    "Can", "Catalog", "Cerca", "Cgi", "Chandler", "Cheese", "ChiPy",
    "Choosing", "Cleanup", "Clear", "Cmd", "Code",
    "Commandline", "Commercial", "Common", "Comparing",
    "Conceptual", "Config", "Continuous", "Convention",
    "Con", "Cool", "Core", "Crashing", "Creating", "Cubic",
    "Db", "Dbus", "Dead", "Decorator", "Default", "Desert",
    "Deutsche", "Development", "Diacritical", "Dictionary",
    "Distribution", "Doc", "Dr",
    "Dubious", "Dunder", "Dvcs",
    "Eff", "Element", "Email", "Embedded", "EmPy", "Enfold",
    "Engineering", "Enthought", "Enumeration", "Environment",
    "EpyDoc", "Escaping", "Executable", "Execution", "Extreme",
    "Find", "Fiscal", "For", "Format", "Form",
    "Free", "Front", "Functional", "Function", "FxPy",
    "General", "GmPy", "Gnome", "Gnu", "Google",
    "Graphics",
    "Grok", "Guido",
    "Harvest", "Health", "Helping", "Hidden", "High",
    "Hjemmeside", "Hyper",
    "Idea", "Image", "Imp", "Information", "Integration",
    "Intermediate", "Internet",
    "JAM", "JeXt", "Jira", "JoBase", "Jython",
    "Kategori", "Key", "Kirby",
    "Language", "Launchpad", "Learning", "Leo",
    "Lightning", "Localizing", "Logging", "Logic", "LoGix",
    "Magyar", "Martellibot", "Matplotlib", "Memento",
    "MetaKit", "Microsoft", "MiddleKit", "MidSummer",
    "MiniDom", "Modifiche", "ModPython", "MontaVista",
    "More Info", "Movable", "Mpl", "Multiple", "Myth",
    "Navigation", "Networked", "Networking", "NodeBox", "NumArray",
    "Open", "Operator", "Option", "OptParse", "Organizers",
    "Package", "Parallel", "Patch", "Path",
    "Pattern", "Pdb", "People", "Perl", "Persistence",
    "Php", "Podcast",
    "Polish", "Portable", "PostScript", "Presentation",
    "Previous Meeting", "Print", "Processo", "Proxy",
    "PsfMaterials", "PullDom",
    "Py ", "PyAmazon", "PyAnt", "PyAudio", "PyBison", "PyBrenda",
    "PyChart", "PyChecker", "PyChem", "PyCrust", "PyDev", "PyDoc",
    "PyFit", "PyFltk", "PyGeo", "PyGobject", "PyGtk",
    "PyInstaller", "PyInterpreter", "PyJaipur", "PyJamas",
    "PyLaunchy", "PyLint", "PyLog", "PyLucene", "PyMat", "PyMedia",
    "PyMeld", "PyMite", "PyObjectivec", "PyPerl",
    "PyScripter", "PySerial", "PySide", "PySoy",
    "PyTable", "PyTables", "PyTextile", "PyTrails", "PyUi",
    "PyUnit", "PyWeek", "PyWiew", "Pydotorg", "Pyed", "Pyjamas",
    "Pythag",
    "Question", "Range", "Rdf", "Recipe", "RedHat",
    "Registration", "Regular", "Render", "Representation",
    "Restricted", "Retrograde",
    "RoundUp", "Rss",
    "SageMath", "Salem", "SanFrancisco",
    "SchoolTool", "Scientific", "SciTe", "Scripting",
    "SeaPig", "SecureShell", "Semplici", "Seneste",
    "Session", "Shell", "Siac", "SimpleTodo", "SimPy",
    "Singleton", "SiteNavig", "SkunkWeb", "SourceForge",
    "Spam", "Special Interest", "Specta", "Sponsor", "Spycy",
    "SqlObject", "Stackless", "Starship",
    "State ", "State Machine", "Stream",
    "String", "Strukturerad", "Subclassing", "Submitting",
    "Sugar", "SymPy", "Syntax",
    "Tahoe", "Talk ", "Talk", "TcpCommunication",
    "TestOob", "TestSoftware", "Texas", "TheCircle",
    "Thread", "Tiny", "TkZinc", "Tokyo", "Topically",
    "TracTracker", "Trouve", "Tuple", "TypeError",
    "Ubuntu", "UdpCommunication", "Unicode", "Useful",
    "UserKit", "Using",
    "Venom", "Version",
    "Virtual", "Visual", "Voicent", "Volunteer",
    "WebAccessibility", "WebApplications", "WebComponents",
    "WebKit", "WebServers", "WebServices", "WebStack",
    "WebStandardisation", "WebWare", "Webizing", "Webware",
    "WegWeiser", "WikiGuidelines", "WikiSpam", "WikiUsers",
    "WxDesigner", "WxGlade",
    "XmlBooks", "XmlDatabases",
    "ZeroPrice", "ZodbSprint",
]

# Exact non-person stems in python/people/
_NON_PERSON_EXACT: set[str] = {
    "AnyGui", "AppEngine", "ApplicationFrameworks", "ApplicationInfrastructure",
    "AppLocalization", "AppLogging", "AprilFools",
    "ArithmoGraph", "ArlingtonSprint", "ArrayInterface", "ArticleIdeas",
    "AskApache", "Attendee Notes",
    "BeginnersWorkshop", "BeThon", "BinPy", "BitArrays", "BitManipulation",
    "BitwiseOperators", "BlackRose", "BlaisePascal", "BoaConstructor",
    "BostonPig", "BoulderJam", "BoulderSprint", "BoxModel", "BrainStorm",
    "BrugerIndstillinger", "BugTracking",
    "Building Python with the free MS C Toolkit",
    "BuildStatically", "BundleBuilder", "BytesStr",
    "CanDo", "CatalogSig", "CercaPagina", "CgiScripts",
    "ChandlerBof", "ChandlerSprint", "CheeseShop", "ChiPy",
    "ChoosingDatabase", "CleanupUrllib", "ClearSilver",
    "CmdModule", "CodeCoverage", "CodeTag", "CommandlineTools",
    "CommercialServices", "CommonIdeas", "ComparingTypes",
    "ConceptualRoadmap", "ConfigObj", "ConText", "ContinuousIntegration",
    "ConventionHowto", "CoolGoose", "Core Python",
    "CoreDevelopment", "CoreSprint", "CrashingPython", "CreatingBuzz",
    "CubicTemp",
    "DbObj", "DbusExamples", "DeadLink", "DeadLinks", "DecoratorPattern",
    "DefaultEncoding", "DesertPy",
    "DeutscheSchlangen", "DevelopmentTools",
    "DiacriticalEditor", "DictionaryKeys",
    "DistributionUtilities", "DocSig", "DocTools", "DocutilsBof",
    "DocutilsSprint", "DrPython", "DrScheme", "DubiousPython",
    "DunderAlias", "DvcsComparison",
    "EffBot", "ElementTree", "EmPy", "EmailSprint", "EmbeddedPython",
    "Enfold Systems", "EngineeringLibraries", "EnthoughtPython",
    "EnumerationProgramming", "EnvironmentVariables",
    "EpyDoc", "EscapingHtml", "EscapingXml",
    "ExecutableModules", "ExecutionScenarios", "ExtremeProgramming",
    "FindSide", "FiscalSponsorship", "ForLoop", "ForSide",
    "FormatReference", "FormEncode",
    "FreeHosts", "FreeMemory", "FreeSoftware", "FrontPage",
    "FunctionalProgramming", "FunctionWrappers", "FxPy",
    "GeneralLibraries", "GmPy", "GnomePython", "GnuEmacs",
    "GnuEnterprise", "GoogleSprint", "GoogleTips",
    "GraphicsBof", "GrokSprint", "GuidovanRobot",
    "HarvestMan", "HealthCare", "HelpingPython",
    "HiddenJewels", "HighScore", "HjemmesideSkabelon", "HyperToons",
    "IdeaRepository", "ImageMagick", "ImpModule",
    "InformationRetrieval", "IntegrationLab",
    "Intermediate Conundrums", "IntermediatesGuide",
    "InternetCafe", "InternetSupport",
    "JeXt", "JiraTracker", "JoBase",
    "JythonBooks", "JythonProjects", "JythonSprint", "JythonUses",
    "KategoriHjemmeside", "KategoriKategori", "KeyError",
    "KirbyBase",
    "LanguageComparisons", "LaunchpadTracker", "LearningRepertoire",
    "LeoEditor", "LightningTalks",
    "LocalizingChandler", "LoggingPackage", "LogicTools", "LoGix",
    "MagyarPython", "MartelliBot", "MatplotlibSprint",
    "MementoPattern", "MetaKit", "Microsoft Access",
    "MiddleKit", "MidSummer", "MiniDom",
    "ModificheRecenti", "ModPython", "MontaVista", "More Info",
    "MovablePython", "MplMentors", "MultipleDispatch", "MythDebunking",
    "NavigationSite", "NetworkedData", "NetworkingSupport",
    "NodeBox", "NumArray",
    "Open Space", "OpenEmbedded", "OpenKomodo", "OpenSource", "OpenSpace",
    "OperatorHook", "OptionParsing", "OptParse",
    "Organizers Meetings Connection Details",
    "PackagePopularity", "ParallelDistutils", "ParallelProcessing",
    "PatchTriage", "PathClass", "PathModule",
    "PatternProgramming", "PdbImprovments", "PeopleFilter",
    "PerlPhrasebook", "PersistenceTools",
    "PhpPhrasebook",
    "Polish Python Coders Group", "PortablePython", "PostScript",
    "PresentationSoftware", "Previous Meeting on October 11 2007",
    "PrintFails", "ProcessoProgramma", "ProxyProgramming",
    "PsfMaterials", "PullDom",
    "Py Swallow Mail",
    "PyAmazon", "PyAnt", "PyAudio", "PyBison", "PyBrenda",
    "PyChart", "PyChecker", "PyChem", "PyCrust", "PyDev", "PyDoc",
    "PydotorgRedesign", "PyedPyers",
    "PyFit", "PyFltk", "PyGeo", "PyGobject", "PyGtk",
    "PyInstaller", "PyInterpreter", "PyJaipur", "PyJamas",
    "PyjamasDesktop", "PyLaunchy", "PyLint", "PyLog", "PyLucene",
    "PyMat", "PyMedia", "PyMeld", "PyMite", "PyObjectivec",
    "PyPerl", "PyPerlish", "PyScripter", "PySerial", "PySide",
    "PySoy", "PyTable", "PyTables", "PyTextile", "PythagoreanTheorem",
    "PyTrails", "PyUi", "PyUnit", "PyWeek", "PyWiew",
    "QuestionStaticmethod", "QuestionType",
    "RangeGenerator", "RdfLib", "RdfLibraries", "RecipeTemplate",
    "RedHat", "Registrations Available", "RegularExpression",
    "RenderMan", "RepresentationError", "RestrictedExecution",
    "RetrogradeOrbit",
    "RoundUp", "RssLibraries",
    "SageMath", "Salem Snakes - Python Club", "SanFrancisco",
    "SchoolTool", "ScientificPython", "SciTe", "ScriptingJava",
    "SeaPig", "SecureShell",
    "Semplici Programmi versione Italiana", "SenesteRettelser",
    "SessionChair", "ShellRun", "SiacNyse",
    "SimpleTodo", "SimPy", "SingletonProgramming",
    "SiteNavigering", "SkunkWeb", "SourceForge",
    "SpamPrevention", "Special Interest Groups",
    "SpectaGen", "SpectaReg", "SponsorOffers", "SpycyRoll",
    "SqlObject", "StacklessPython", "StarshipPython", "StarshipTransfer",
    "State Machine via Decorators", "StateProgramming",
    "StreamReader", "StreamRecoder", "StreamWriter",
    "StringFormatting", "StruktureradText",
    "SubclassingDictionaries", "SubmittingBugs", "SugarUi",
    "SymPy", "SyntaxReference",
    "TahoeMentors", "Talk Subjects", "TalkMistakes",
    "TcpCommunication",
    "TestOob", "TestSoftware", "Texas Pythoneers!", "TexasPythoneers",
    "TheCircle", "ThreadProgramming", "Tiny Python",
    "TkZinc", "TokyoPythonistas",
    "Topically Organized PEP List",
    "TracTracker", "TrouvePage", "TupleSyntax", "TypeError",
    "UbuntuInstall", "UdpCommunication", "UnicodeEncoding",
    "UsefulModules", "UserKit", "UsingEnumerate", "UsingSlots",
    "VenomPackage", "VersionControl",
    "VirtualPython", "VisualWx",
    "Voicent Simple Telephone Call API",
    "Volunteer Signup 2008", "Volunteer Signup", "VolunteerOpportunities",
    "WebAccessibility", "WebApplications", "WebComponents",
    "WebizingPython", "WebKit", "WebServers", "WebServices",
    "WebStack", "WebStandardisation", "WebWare", "WebwareSprint",
    "WegWeiser", "WikiGuidelines", "WikiSpam", "WikiUsers",
    "WxDesigner", "WxGlade",
    "XmlBooks", "XmlDatabases",
    "ZeroPrice", "ZodbSprint",
}


def _is_non_person(stem: str) -> bool:
    """Check if a stem is known non-person content in python/people/."""
    if stem in _NON_PERSON_EXACT:
        return True
    # Check if it's a known non-person from reorganize.py
    if stem in NON_PERSON_CAMELCASE:
        return True
    return False


def _entry_size(path: Path) -> int:
    """Get total content size for a file or directory."""
    if path.is_dir():
        total = 0
        for f in path.rglob("*.md"):
            try:
                total += f.stat().st_size
            except OSError:
                pass
        return total
    try:
        return path.stat().st_size
    except OSError:
        return 0


def git_mv(src: Path, dst: Path) -> None:
    """Move a file/directory using git mv, falling back to shutil."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["git", "mv", str(src), str(dst)],
            cwd=REPO_ROOT, check=True, capture_output=True,
        )
    except subprocess.CalledProcessError:
        if src.is_dir():
            shutil.copytree(str(src), str(dst), dirs_exist_ok=True)
            shutil.rmtree(str(src))
        else:
            shutil.move(str(src), str(dst))


def git_rm(path: Path) -> None:
    """Remove a file using git rm, falling back to os.remove."""
    try:
        subprocess.run(
            ["git", "rm", "-rf", str(path)],
            cwd=REPO_ROOT, check=True, capture_output=True,
        )
    except subprocess.CalledProcessError:
        if path.is_dir():
            shutil.rmtree(str(path))
        elif path.exists():
            path.unlink()


def collect_people_entries(wiki: str) -> dict[str, list[Path]]:
    """Collect entries from a wiki's people/ dir, grouped by person stem.

    Returns {stem: [paths]} where paths may include both a .md and a directory.
    """
    people_dir = REPO_ROOT / wiki / "people"
    if not people_dir.exists():
        return {}

    entries: dict[str, list[Path]] = {}
    for item in sorted(people_dir.iterdir()):
        if item.name == "index.md":
            continue
        stem = item.stem if item.is_file() else item.name
        entries.setdefault(stem, []).append(item)
    return entries


def classify_python_people() -> tuple[dict[str, list[Path]], dict[str, list[Path]]]:
    """Classify python/people/ entries into persons and non-persons.

    Returns (persons, non_persons) where each is {stem: [paths]}.
    """
    entries = collect_people_entries("python")
    persons: dict[str, list[Path]] = {}
    non_persons: dict[str, list[Path]] = {}

    for stem, paths in entries.items():
        # Check if it's a known non-person directory
        if stem in NON_PERSON_DIRS:
            non_persons[stem] = paths
            continue

        # Check if it's a known non-person entry
        if _is_non_person(stem):
            non_persons[stem] = paths
            continue

        # Use the heuristic
        if _looks_like_person(stem):
            persons[stem] = paths
        else:
            non_persons[stem] = paths

    return persons, non_persons


def resolve_dir_file_dupes(paths: list[Path]) -> Path:
    """Given both a .md file and a directory for the same stem, pick the directory."""
    dirs = [p for p in paths if p.is_dir()]
    files = [p for p in paths if p.is_file()]
    if dirs:
        return dirs[0]
    return files[0]


def pick_richer(candidates: list[tuple[str, list[Path]]]) -> tuple[str, Path]:
    """Among cross-wiki duplicates, pick the richer version.

    Returns (winning_wiki, winning_path).
    Directory > file; then larger > smaller.
    """
    best_wiki = candidates[0][0]
    best_path = resolve_dir_file_dupes(candidates[0][1])
    best_is_dir = best_path.is_dir()
    best_size = _entry_size(best_path)

    for wiki, paths in candidates[1:]:
        path = resolve_dir_file_dupes(paths)
        is_dir = path.is_dir()
        size = _entry_size(path)

        # Directory beats file
        if is_dir and not best_is_dir:
            best_wiki, best_path, best_is_dir, best_size = wiki, path, is_dir, size
        elif not is_dir and best_is_dir:
            continue
        elif size > best_size:
            best_wiki, best_path, best_is_dir, best_size = wiki, path, is_dir, size

    return best_wiki, best_path


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("Merge People Directories")
    print("=" * 60)
    print(f"Repo root: {REPO_ROOT}")
    print(f"Dry run: {dry_run}")
    print()

    # -----------------------------------------------------------------------
    # Step 1: Classify python/people/ entries
    # -----------------------------------------------------------------------
    print("Step 1: Classify python/people/ entries")
    py_persons, py_non_persons = classify_python_people()
    print(f"  Persons: {len(py_persons)}")
    print(f"  Non-persons: {len(py_non_persons)}")

    # -----------------------------------------------------------------------
    # Step 2: Collect people from psf/ and jython/
    # -----------------------------------------------------------------------
    print("\nStep 2: Collect PSF and Jython people")
    psf_entries = collect_people_entries("psf")
    jython_entries = collect_people_entries("jython")

    # Filter out non-people from jython
    jython_non_people: dict[str, list[Path]] = {}
    for stem in list(jython_entries.keys()):
        if stem in JYTHON_NON_PERSON:
            jython_non_people[stem] = jython_entries.pop(stem)

    # Handle Annapoornima Koppad / AnnapoornimaKoppad dupe in psf
    # (different naming convention, same person — keep both, they'll merge by stem)

    print(f"  PSF people: {len(psf_entries)}")
    print(f"  Jython people: {len(jython_entries)}")
    print(f"  Jython non-people: {len(jython_non_people)}")

    # -----------------------------------------------------------------------
    # Step 3: Merge and deduplicate
    # -----------------------------------------------------------------------
    print("\nStep 3: Merge and deduplicate")

    # Collect all people by stem across wikis
    all_people: dict[str, list[tuple[str, list[Path]]]] = {}
    for stem, paths in py_persons.items():
        all_people.setdefault(stem, []).append(("python", paths))
    for stem, paths in psf_entries.items():
        all_people.setdefault(stem, []).append(("psf", paths))
    for stem, paths in jython_entries.items():
        all_people.setdefault(stem, []).append(("jython", paths))

    # Find cross-wiki duplicates
    dupes = {s: v for s, v in all_people.items() if len(v) > 1}
    print(f"  Total unique people: {len(all_people)}")
    print(f"  Cross-wiki duplicates: {len(dupes)}")

    if dupes:
        print("  Duplicates:")
        for stem, candidates in sorted(dupes.items()):
            wikis = [w for w, _ in candidates]
            print(f"    {stem}: {', '.join(wikis)}")

    # -----------------------------------------------------------------------
    # Step 4: Plan moves
    # -----------------------------------------------------------------------
    print("\nStep 4: Plan moves")

    target_dir = REPO_ROOT / "people"
    archive_dir = REPO_ROOT / "python" / "archive"
    redirects: dict[str, str] = {}

    # Track what to move
    moves: list[tuple[Path, Path, str]] = []  # (src, dst, description)
    removes: list[tuple[Path, str]] = []  # (path, reason)

    for stem, candidates in all_people.items():
        if len(candidates) == 1:
            # Single source — just move
            wiki, paths = candidates[0]
            winner = resolve_dir_file_dupes(paths)
            if winner.is_dir():
                dst = target_dir / stem
            else:
                dst = target_dir / winner.name
            moves.append((winner, dst, f"{wiki}/people/{stem} -> people/"))

            # Remove the "loser" (standalone .md when dir exists)
            for p in paths:
                if p != winner:
                    removes.append((p, f"dir+file dupe, keeping dir"))

            # Add redirects for all paths
            for p in paths:
                if p.is_dir():
                    # Redirect the directory index
                    old_docname = f"{wiki}/people/{stem}/index"
                    new_docname = f"people/{stem}/index"
                    redirects[old_docname] = new_docname
                    # Also add non-index redirect
                    old_base = f"{wiki}/people/{stem}"
                    redirects[old_base] = f"people/{stem}"
                    # Redirect all files inside the directory
                    for md in p.rglob("*.md"):
                        rel = md.relative_to(REPO_ROOT / wiki / "people")
                        old_doc = f"{wiki}/people/{rel}".removesuffix(".md")
                        new_doc = f"people/{rel}".removesuffix(".md")
                        redirects[old_doc] = new_doc
                else:
                    old_docname = f"{wiki}/people/{stem}"
                    new_docname = f"people/{stem}"
                    redirects[old_docname] = new_docname
        else:
            # Cross-wiki duplicate — pick the richer version
            winning_wiki, winning_path = pick_richer(candidates)
            if winning_path.is_dir():
                dst = target_dir / stem
            else:
                dst = target_dir / winning_path.name
            moves.append((winning_path, dst, f"dupe winner: {winning_wiki}/people/{stem}"))

            # Handle all sources
            for wiki, paths in candidates:
                winner_in_wiki = resolve_dir_file_dupes(paths)
                if winner_in_wiki != winning_path:
                    # This is a loser — remove it
                    for p in paths:
                        removes.append((p, f"cross-wiki dupe, keeping {winning_wiki} version"))
                else:
                    # This is the winner — remove any file+dir dupes
                    for p in paths:
                        if p != winning_path:
                            removes.append((p, f"dir+file dupe, keeping dir"))

                # Add redirects for all paths from this wiki
                for p in paths:
                    if p.is_dir():
                        old_docname = f"{wiki}/people/{stem}/index"
                        new_docname = f"people/{stem}/index" if dst.is_dir() or winning_path.is_dir() else f"people/{stem}"
                        redirects[old_docname] = new_docname
                        old_base = f"{wiki}/people/{stem}"
                        redirects[old_base] = f"people/{stem}"
                        for md in p.rglob("*.md"):
                            rel = md.relative_to(REPO_ROOT / wiki / "people")
                            old_doc = f"{wiki}/people/{rel}".removesuffix(".md")
                            new_doc = f"people/{rel}".removesuffix(".md")
                            redirects[old_doc] = new_doc
                    else:
                        old_docname = f"{wiki}/people/{stem}"
                        new_docname = f"people/{stem}"
                        redirects[old_docname] = new_docname

    # Non-persons from python/people/ → python/archive/
    for stem, paths in py_non_persons.items():
        for p in paths:
            if p.is_dir():
                dst = archive_dir / stem
            else:
                dst = archive_dir / p.name
            moves.append((p, dst, f"non-person: python/people/{p.name} -> python/archive/"))
            # Add redirect
            if p.is_dir():
                old_docname = f"python/people/{stem}/index"
                new_docname = f"python/archive/{stem}/index"
                redirects[old_docname] = new_docname
                old_base = f"python/people/{stem}"
                redirects[old_base] = f"python/archive/{stem}"
                for md in p.rglob("*.md"):
                    rel = md.relative_to(REPO_ROOT / "python" / "people")
                    old_doc = f"python/people/{rel}".removesuffix(".md")
                    new_doc = f"python/archive/{rel}".removesuffix(".md")
                    redirects[old_doc] = new_doc
            else:
                old_docname = f"python/people/{stem}"
                new_docname = f"python/archive/{stem}"
                redirects[old_docname] = new_docname

    # Jython non-people
    for stem, paths in jython_non_people.items():
        target = JYTHON_NON_PERSON[stem]
        for p in paths:
            if p.is_dir():
                dst = REPO_ROOT / target / stem
            else:
                dst = REPO_ROOT / target / p.name
            moves.append((p, dst, f"jython non-person: {stem} -> {target}"))
            if p.is_dir():
                old_docname = f"jython/people/{stem}/index"
                new_docname = f"{target}{stem}/index"
                redirects[old_docname] = new_docname
                for md in p.rglob("*.md"):
                    rel = md.relative_to(REPO_ROOT / "jython" / "people")
                    old_doc = f"jython/people/{rel}".removesuffix(".md")
                    new_doc = f"{target}{rel}".removesuffix(".md")
                    redirects[old_doc] = new_doc
            else:
                old_docname = f"jython/people/{stem}"
                new_docname = f"{target}{stem}"
                redirects[old_docname] = new_docname

    print(f"  Moves planned: {len(moves)}")
    print(f"  Removes planned: {len(removes)}")
    print(f"  Redirects: {len(redirects)}")

    if dry_run:
        print("\n--- Moves (sample) ---")
        for src, dst, desc in moves[:30]:
            print(f"  {desc}")
            print(f"    {src.relative_to(REPO_ROOT)} -> {dst.relative_to(REPO_ROOT)}")
        if len(moves) > 30:
            print(f"  ... and {len(moves) - 30} more")

        print("\n--- Removes ---")
        for path, reason in removes:
            print(f"  RM {path.relative_to(REPO_ROOT)}: {reason}")

        print("\n--- Non-persons moved to archive (sample) ---")
        archive_moves = [(s, d, desc) for s, d, desc in moves if "non-person" in desc]
        for src, dst, desc in archive_moves[:20]:
            print(f"  {src.relative_to(REPO_ROOT)} -> {dst.relative_to(REPO_ROOT)}")
        if len(archive_moves) > 20:
            print(f"  ... and {len(archive_moves) - 20} more")

        print(f"\n--- Redirect samples ---")
        for old, new in list(redirects.items())[:10]:
            print(f"  {old} -> {new}")
        return

    # -----------------------------------------------------------------------
    # Step 5: Execute moves
    # -----------------------------------------------------------------------
    print("\nStep 5: Execute moves")
    target_dir.mkdir(parents=True, exist_ok=True)

    for src, dst, desc in moves:
        if not src.exists():
            print(f"  SKIP (missing): {src.relative_to(REPO_ROOT)}")
            continue
        print(f"  MOVE: {src.relative_to(REPO_ROOT)} -> {dst.relative_to(REPO_ROOT)}")
        git_mv(src, dst)

    for path, reason in removes:
        if not path.exists():
            continue
        print(f"  RM: {path.relative_to(REPO_ROOT)} ({reason})")
        git_rm(path)

    # -----------------------------------------------------------------------
    # Step 6: Update _redirects.json
    # -----------------------------------------------------------------------
    print("\nStep 6: Update _redirects.json")
    redirects_file = REPO_ROOT / "_redirects.json"
    existing: dict[str, str] = {}
    if redirects_file.exists():
        existing = json.loads(redirects_file.read_text())

    # Merge new redirects, updating any existing chains
    for old, new in redirects.items():
        existing[old] = new

    # Also update any existing redirects that pointed to old people paths
    for old, new in list(existing.items()):
        if new in redirects:
            existing[old] = redirects[new]

    existing = dict(sorted(existing.items()))
    redirects_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n")
    print(f"  Wrote {len(existing)} total redirects")

    # -----------------------------------------------------------------------
    # Step 7: Generate people/index.md
    # -----------------------------------------------------------------------
    print("\nStep 7: Generate people/index.md")
    people_entries: list[str] = []
    for item in sorted((REPO_ROOT / "people").iterdir()):
        if item.name == "index.md":
            continue
        if item.is_dir():
            # Check if it has an index.md
            if (item / "index.md").exists():
                people_entries.append(f"{item.name}/index")
            else:
                # List individual files
                for md in sorted(item.glob("*.md")):
                    people_entries.append(f"{item.name}/{md.stem}")
        else:
            if item.suffix == ".md":
                people_entries.append(item.stem)

    index_content = "# People\n\n"
    index_content += f"This section contains {len(people_entries)} pages.\n\n"
    index_content += "```{toctree}\n"
    index_content += ":maxdepth: 1\n"
    index_content += ":hidden:\n"
    index_content += "\n"
    for entry in people_entries:
        index_content += f"{entry}\n"
    index_content += "```\n"

    (REPO_ROOT / "people" / "index.md").write_text(index_content)
    print(f"  Generated with {len(people_entries)} entries")

    # -----------------------------------------------------------------------
    # Step 8: Update wiki index files
    # -----------------------------------------------------------------------
    print("\nStep 8: Update index files")

    # Add people/index to root index.md toctree
    root_index = REPO_ROOT / "index.md"
    root_text = root_index.read_text()
    if "people/index" not in root_text:
        root_text = root_text.replace(
            "python/index\n",
            "people/index\npython/index\n",
        )
        root_index.write_text(root_text)
        print("  Added people/index to root index.md")

    # Remove people/index from wiki indexes
    for wiki in ("python", "psf", "jython"):
        wiki_index = REPO_ROOT / wiki / "index.md"
        text = wiki_index.read_text()
        if "people/index\n" in text:
            text = text.replace("people/index\n", "")
            wiki_index.write_text(text)
            print(f"  Removed people/index from {wiki}/index.md")

    # -----------------------------------------------------------------------
    # Step 9: Clean up empty people directories
    # -----------------------------------------------------------------------
    print("\nStep 9: Clean up empty people directories")
    for wiki in ("python", "psf", "jython"):
        people_dir = REPO_ROOT / wiki / "people"
        if people_dir.exists():
            # Check if only index.md remains
            remaining = list(people_dir.iterdir())
            remaining_names = [r.name for r in remaining]
            if remaining_names == ["index.md"] or not remaining:
                git_rm(people_dir)
                print(f"  Removed {wiki}/people/ (empty)")
            elif remaining:
                print(f"  {wiki}/people/ still has: {remaining_names[:5]}...")

    print("\nDone! Now run:")
    print("  python scripts/gen_redirect_pages.py")
    print("  uv run sphinx-build -b html . _build/html -j auto --keep-going")


if __name__ == "__main__":
    main()
