# Pip2020DonorFundedRoadmap

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Roadmap for pip resolver and UX work in 2020 

Thanks to [the Chan Zuckerberg Initiative](https://chanzuckerberg.com/eoss/proposals/improving-user-experience-and-debuggability-of-pip-for-all-python-users/) and [Mozilla\'s Open Source Support program](https://pyfound.blogspot.com/2019/12/moss-czi-support-pip.html), the [PackagingWG](PackagingWG) is receiving funding to [finish pip\'s dependency resolver](https://wiki.python.org/psf/Fundable%20Packaging%20Improvements#Finish_dependency_resolver_for_pip) and [improve pip\'s user experience](https://wiki.python.org/psf/Fundable%20Packaging%20Improvements#Improve_pip_user_experience).

## Key people 

Contractors working on this project will be

- [Python developers hired via Python Software Foundation RfP](https://pyfound.blogspot.com/2019/11/seeking-developers-for-paid-contract.html): Pradyun Gedam, Tzu-ping Chung, Paul F. Moore of Atos, and Ilan Schnell

- [User experience research and design consultancy Simply Secure](https://simplysecure.org/)

- [Project manager: Sumana Harihareswara of Changeset Consulting](https://changeset.nyc/)

## Work summary 

We\'ve finished a next-generation rewrite of the dependency resolver within pip, Python\'s package download and installation tool. The project ran into massive technical debt, but the refactoring is nearly finished and functionality is in pip 20.3 now. [Many improvements and installation and dependency issues for Python users, conda/Anaconda, and other platforms are blocked awaiting this feature.](https://wiki.python.org/psf/Fundable%20Packaging%20Improvements#Finish_dependency_resolver_for_pip)

Also, pip\'s user experience has become more consistent across features, to fit the user\'s mental model better, reduce unintended data loss, and provide better error messages and prompts, logs, output, and reporting.

Multiple developers, a UX design/research consultancy, and a project manager are executing a three-phase plan to support user experience, communications/publicity, and testing work (including developing robust testing and continuous integration infrastructure) on the resolver, as well as core feature development and review.

Initially, as developers came up to speed on pip and work on finishing refactoring the build logic within pip, UX experts studied the command line packaging/distribution environment, ran user tests, and developed robust user journeys/concept maps.

Second, the contractors worked together on implementing the resolver. The developers wrote tests, improved CI, built test infrastructure, introduced new abstractions and fixed bugs found in alpha testing, collaborated with downstreams and users about config flags and transition schedules, and so on. The UX experts improved command-line UX (such as in-CLI help and error messages, and specific commands and names of flags), and improved the [pip user guide](https://pip.pypa.io/en/stable/user_guide/).

Finally, one contract developer is maintaining the pip repository by triaging bugs and reviewing pull requests (releasing bottlenecks), and the UX experts will train maintainers in CLI UX design principles and write UX guidelines for the project.

Throughout, a project manager is finding and communicating with stakeholders and testers, and with the funders.

## Detailed work plan 

*Exists in other documents, such as [https://pyfound.blogspot.com/2019/11/seeking-developers-for-paid-contract.html](https://pyfound.blogspot.com/2019/11/seeking-developers-for-paid-contract.html) and [https://github.com/pypa/pip/milestone/38](https://github.com/pypa/pip/milestone/38) .*

### Phase I (Foundational work, early 2020) 

#### Developers\' onboarding and initial work 

See [RFP](https://github.com/python/request-for/blob/master/2020-pip/RFP.md).

#### UX onboarding and initial work 

- Read, view, and process the voluminous existing information on pip user confusion (such as the \"Improve UX\" milestone [https://github.com/pypa/pip/milestone/10](https://github.com/pypa/pip/milestone/10), \"Print Better Error Messages\" milestone [https://github.com/pypa/pip/milestone/25](https://github.com/pypa/pip/milestone/25), Stack Overflow questions about pip, and unofficial blog posts and articles such as \"The Python Packaging Ecosystem\" [https://www.curiousefficiency.org/posts/2016/09/python-packaging-ecosystem.html](https://www.curiousefficiency.org/posts/2016/09/python-packaging-ecosystem.html))

- Perform user interviews and testing, and writeups (covering pip). These will be organized similarly to how the grant-funded PyPI team\'s UX researcher/designer organized user interviews and user tests (see [https://whoisnicoleharris.com/2018/03/13/user-testing-warehouse.html](https://whoisnicoleharris.com/2018/03/13/user-testing-warehouse.html), [https://whoisnicoleharris.com/2018/07/22/pypi-user-research.html](https://whoisnicoleharris.com/2018/07/22/pypi-user-research.html), and [https://github.com/pypa/warehouse/issues/6173](https://github.com/pypa/warehouse/issues/6173)). We will recruit diverse users who have different skill levels, come from industry, academia, and more, are diverse across gender, ethnicity, and age, and have different computing environments. Outcomes: greater systematic understandings of users\' workflows, mental models, and current priorities for fixing issues, to feed into developer documentation.

- Develop user journey maps & workflows

### Phase II (Resolver work, \~March-June 2020) 

#### Developers 

See [RFP](https://github.com/python/request-for/blob/master/2020-pip/RFP.md).

#### UX 

- Working with maintainers to write documentation and help messages, and to design resolver user experience

### Phase III (Maintenance and Sustainability work, June-December 2020) 

#### Developer 

- Keep up with the pip code and issue review queue for 10 hours per week, thus releasing a key bottleneck and enabling existing maintainers to make progress on key architectural features
- Help new contributors develop into continuing contributors
- Help existing contributors grow into co-maintainers

#### UX 

- Interview users, run tests, and writeup (covering resolver and expanding research scope). These will be organized similarly to the research in the first phase, but will measure user experience improvements from the new resolver, and will allow the researcher to expand their research. Scope to, for instance, issues involving conda, virtualenvs, and other package managers. Outcomes: greater user understandings, as above, and assessment of the UX improvements in the new resolver.

- Update workflows, expand user journeys, and develop checklist for developing new features

- Develop templates for UI bugs, commands, error messages, output, documentation, and configuration files

- Teach other pip developers UX practices per [https://simplysecure.org/what-we-do/user-research/](https://simplysecure.org/what-we-do/user-research/)

- Develop list of people/organizations who can participate in UX testing
