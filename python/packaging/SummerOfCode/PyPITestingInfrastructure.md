# SummerOfCode/PyPITestingInfrastructure

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page describes a possible Summer of Code project for a testing infrastructure for PyPI.

**Contact: Tarek Ziadé \<[tarek@ziade.org](mailto:tarek@ziade.org)\> or Alexis Métaireau \<[alexis@notmyidea.org](mailto:alexis@notmyidea.org)\>**

PyPI has recently gained a [PubSubHubBub](./PubSubHubBub.html) interface we can use to trigger events when a new package is uploaded.

The student work to be done is :

- compare and chose the best virtual environment for the testing infrastructure we need

- create a initial collections of clean VMs

- study tools like systemtap to be able to report what happens on a box

- create a set of scripts to drive the Virtual Machines (Linux only is acceptable) :
  - start the VM
  - set up the VM for the tests (firewall, probes, etc.)
  - upload content and run commands over the VM
  - get back the reports
  - perform rollback

- create a [PubSubHubBub](./PubSubHubBub.html) daemon

  - trigger the tests for each upload events
  - store the report

- create a website
  - display the reports
  - create a registry system for people to get reports by emails

The final piece of software should be extensible by a plugin system (adding test-cases to PyPI testing infrastructure).
