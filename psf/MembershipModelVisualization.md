# MembershipModelVisualization

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Membership Model Visualization 

The newly proposed PSF membership model is a great idea and the echo from the PSF members is overwhelmingly positive.

There are quite a few details. A picture may help to make these easier to understand. This is an attempt to visualize this. Instead of using a graphics drawing application, I generated the diagram below with a Python program. The source is also attached.

- So, just where does \"the diagram below\" appear? - SH

This is by no means complete but can serve as a basis for coming up with further details. The advantage is that all these familiar tools and procedures such as version control, pull request and tests can be applied.

So far there is no code in methods. It should be possible to add algorithms and make the membership rules executable. Since code is primarily a means of communication between humans and only in the second place instructions for the computer, this little program may help to better understand what we want to express.

- [![\[ATTACH\]](/wiki/europython/img/attach.png "[ATTACH]")]( "Upload new attachment "classes_membership_model.png"")

:::: 
::: 
``` 
   1 #! /usr/bin/env python3
   2 
   3 """The new PSF membership model in code.
   4 """
   5 
   6 import abc
   7 
   8 
   9 class Member(metaclass=abc.ABCMeta):
  10     """A member of the PSF. An abstract concept.
  11     """
  12 
  13 
  14 class IndividualMember(Member):
  15     """A personal member.
  16 
  17     Anyone how would to be associated with the PSF can sign up.
  18     """
  19     order_of_magnitude_range = 1e4, 1e5
  20 
  21 
  22 class InstitutionalMember(Member, metaclass=abc.ABCMeta):
  23     """An institutional member of the PSF. An abstract concept.
  24     """
  25 
  26     def vote(self):
  27         """Elect board members.
  28         """
  29 
  30 
  31 class SponsorMember(InstitutionalMember):
  32     """Organization that pays to be a member.
  33 
  34     These can be companies or other institutions.
  35     """
  36     order_of_magnitude_range = 1e1, 1e3
  37 
  38 
  39 class OrganizationMember(InstitutionalMember):
  40     """National organizations that are somewhat equivalent to
  41     the PSF, but operate in other countries.
  42 
  43     These organizations should have or work comparable to having a non-profit
  44     status.
  45     """
  46     order_of_magnitude_range = 1e1, 1e2
  47 
  48 
  49 class VotingMember(IndividualMember, metaclass=abc.ABCMeta):
  50     """An individual member with voting rights.
  51     """
  52 
  53     def vote(self):
  54         """Elect board members.
  55         """
  56 
  57 
  58 class SupportingMember(VotingMember):
  59     """A member who gives money.
  60     """
  61     order_of_magnitude_range = 1e1, 1e3
  62 
  63 
  64 class ManagingMember(VotingMember):
  65     """A member who gives time.
  66     """
  67     order_of_magnitude_range = 1e1, 1e2
  68 
  69 
  70 class ContributingMember(VotingMember):
  71     """A member who gives code, documentation etc.
  72     """
  73     order_of_magnitude_range = 1e1, 1e2
  74 
  75 
  76 class Fellow(ManagingMember, ContributingMember):
  77     # No sequence of parents intended but need to specify one.
  78     """Elected from among the members.
  79     """
  80     order_of_magnitude_range = 1e1, 1e2
  81 
  82 
  83 class BoardMember(Fellow):
  84     # No sequence of parents intended but need to specify one.
  85     """Elected from among the fellows.
  86     """
  87     order_of_magnitude_range = 1e0, 1e1
  88 
  89 
  90 class WorkingGroup:
  91     """A working group.
  92     """
  93     """
  94 
```
:::
::::
