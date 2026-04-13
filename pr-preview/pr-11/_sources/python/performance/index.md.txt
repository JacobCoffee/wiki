# Performance

These pages cover Python performance -- both practical tips for writing faster code and historical efforts to speed up the CPython interpreter itself. Some of this content dates back to specific sprints and projects from the mid-2000s, so treat the historical pages as context rather than current advice. The general performance tips, though, hold up well.

## Performance Tips and Techniques

- [Python Speed](PythonSpeed/index) -- collected resources on making Python code run faster
- [Python Speed](PythonSpeed) -- overview of Python performance characteristics and optimization strategies

## Profiling

- [Profile Replacement Project](ProfileReplacementProject) -- a proposal to replace the profile and pstats modules with something more Pythonic

## Interpreter Optimization Projects

- [Need for Speed](NeedForSpeed/index) -- results from the 2006 NeedForSpeed sprint in Reykjavik
- [Need for Speed](NeedForSpeed) -- the sprint that targeted CPython interpreter performance improvements
- [Speed Up Interpreter Startup](SpeedUpInterpreterStartup) -- analysis of what makes the Python interpreter slow to start, from PyCon 2004
- [Speed Up 2to3 Pattern Matching](SpeedUp2to3PatternMatching) -- replacing the naive backtracking in 2to3 with finite state machines

```{toctree}
:hidden:
:maxdepth: 1

NeedForSpeed/index
PythonSpeed/index
NeedForSpeed
ProfileReplacementProject
PythonSpeed
SpeedUp2to3PatternMatching
SpeedUpInterpreterStartup
```
