# Developer Guide

For people who want to work on Jython itself -- fixing bugs, porting modules, cutting releases, or just understanding how the project is organized. This section has the coding standards, tooling guides, and process documentation you need to contribute effectively.

## Getting Involved

- [JythonDeveloperGuide](JythonDeveloperGuide/index) -- The main developer guide with IDE setup instructions (Eclipse, IntelliJ, NetBeans), porting guides, and regression test notes
- [JythonDeveloperGuide (summary)](JythonDeveloperGuide) -- A condensed version of the developer guide
- [HowToGetInvolved](HowToGetInvolved) -- Where to start if you want to contribute to Jython
- [WhosDoingWhat](WhosDoingWhat) -- Who is working on which parts of the project

## Standards & Process

- [CodingStandards](CodingStandards) -- Code style conventions for the Jython codebase
- [PatchGuidelines](PatchGuidelines) -- How to prepare and submit patches
- [ReportingBugs](ReportingBugs) -- How and where to file bug reports

## Testing

- [TestingJython](TestingJython) -- How to run the Jython test suite
- [TestFailures](TestFailures) -- Known test failures and their status
- [MigrateBugtests](MigrateBugtests) -- Moving legacy bug tests into the modern test framework

## Releases & Planning

- [HowToReleaseJython](HowToReleaseJython) -- The release process, step by step
- [JythonReleaseNotes](JythonReleaseNotes) -- Release notes across Jython versions
- [RoadMap](RoadMap) -- Planned features and milestones
- [MovingJythonForward](MovingJythonForward) -- Discussion about the project's direction and priorities

## Compatibility & Migration

- [Jython25BackwardsIncompatibilities](Jython25BackwardsIncompatibilities) -- Breaking changes introduced in Jython 2.5
- [UpgradeTo25CPythonLib](UpgradeTo25CPythonLib) -- Upgrading the bundled CPython standard library to match 2.5
- [VersionTransition](VersionTransition) -- Notes on transitioning between major Jython versions
- [RelicensingJython](RelicensingJython) -- The effort to relicense Jython

## Infrastructure

- [DeveloperFAQ](DeveloperFAQ) -- Common developer questions and answers
- [SourceForge](SourceForge) -- Jython's historical SourceForge project page
- [SvnToHgMigration](SvnToHgMigration) -- Migrating the repository from Subversion to Mercurial
- [WebsiteBuilderSetup](WebsiteBuilderSetup) -- How the jython.org website build system works

```{toctree}
:hidden:
:maxdepth: 1

JythonDeveloperGuide/index
CodingStandards
DeveloperFAQ
HowToGetInvolved
HowToReleaseJython
Jython25BackwardsIncompatibilities
JythonDeveloperGuide
JythonReleaseNotes
MigrateBugtests
MovingJythonForward
PatchGuidelines
RelicensingJython
ReportingBugs
RoadMap
SourceForge
SvnToHgMigration
TestFailures
TestingJython
UpgradeTo25CPythonLib
VersionTransition
WebsiteBuilderSetup
WhosDoingWhat
```
