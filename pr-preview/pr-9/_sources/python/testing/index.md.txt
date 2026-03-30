# Testing

Everything here is about testing Python code -- the frameworks available, the philosophies behind them, and practical advice for specific situations. Python has a strong culture around testing, and these pages reflect the community's collected wisdom on the subject, from the standard library's unittest and doctest modules to third-party tools like pytest.

## Concepts and Approaches

- [Testing](Testing) -- a general overview of testing in Python and what it means to verify your code
- [Test-Driven Development](TestDrivenDevelopment) -- the TDD workflow: write the test first, then write the code

## Frameworks and Tools

- [Unit Tests](UnitTests) -- survey of Python testing frameworks, including unittest and alternatives
- [pytest](PyTest) -- the popular third-party test runner with minimal boilerplate
- [doctest](DocTest) -- testing by embedding examples in docstrings

## Specialized Topics

- [Testing Infrastructure](Testing%20Infrastructure) -- what testing infrastructure is and how it supports your workflow
- [Testing CGI Scripts](TestingCgiScripts) -- approaches to testing CGI scripts outside of a web server

```{toctree}
:hidden:
:maxdepth: 1

DocTest
PyTest
TestDrivenDevelopment
Testing
Testing Infrastructure
TestingCgiScripts
UnitTests
```
