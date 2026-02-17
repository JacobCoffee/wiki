# PythonSoftwareFoundationLicenseFaq

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Software Foundation License FAQ 

This FAQ answers commonly asked questions about Python\'s license -- what the license allows and requires, what license to use for new code, how code gets contributed to Python, and related topics.

## Using the Python Software Foundation License 

### Can I bundle Python with my non-open-source application? 

Yes. Unlike some open source licenses, the PSF License allows Python to be included in non-open applications, either in unmodified or modified form. See also this [more detailed overview](http://python.org/psf/license).

### If I bundle Python with my application, what do I need to include in my software and/or printed documentation? 

You must retain all copyright notices found in the code you are redistributing and include a copy of the PSF License and all of the other licenses in the Python \"license stack\" with the software distribution. The \"license stack\" is a result of the history of Python\'s development as [described here](https://opensource.org/steward/python-software-foundation/) (this page also lists all licenses in the stack).

Separate from the issue of copyright, the name "Python" is also a trademark. You should include the notice "\"Python\" is a registered trademark of the Python Software Foundation" in the appropriate part of your documentation or About box and place the "®" symbol after the first mention of "Python" in your documentation. (For example: "Python® is used as the scripting language for\...")

### What about using third party Python modules that aren\'t part of the Python distribution? 

Many of the third party modules for Python are released under similarly non-restrictive open source licenses. However, you should read the license and contact the respective authors for any clarification on allowed uses and requirements. The PSF has no legal authority over third party modules for Python.

### Is Python subject to export laws? 

- **Please note that this section is most probably no longer up to date:** The US export rules have changed a lot, since the text was written. For up to date information, please consult the [Bureau of Industry and Security (BIS)](http://www.bis.doc.gov/) website.

Python is subject to US export control laws and may be subject to export control laws of other countries. The US Department of Commerce\'s Bureau of Export Administration (BXA), also referred to as the Bureau of Industry and Security, classifies Python as \"mass market encryption software\" under the export control number (ECCN) 5D002.

Python is defined as \"publicly available\" under §734.3(b)(3) of US export control regulations. As such, its source code can be exported and reexported without restrictions. As far as the PSF is aware, we have fulfilled the notification requirements for such export and reexport, described here:

[http://www.bis.doc.gov/Encryption/PubAvailEncSourceCodeNofify.html](http://www.bis.doc.gov/Encryption/PubAvailEncSourceCodeNofify.html)

If you are exporting Python from the USA, it is your responsibility to comply with all export control laws. This may include registering your product with the BXA and checking the Denied Persons and other lists kept by the BXA.

Exporting from some other countries may also entail restrictions or requirements, but this is beyond the scope of this FAQ. Be sure to consult your local authorities.

*Details of our filings with the BXA follow:*

The PSF filed a TSU NOTIFICATION with the BXA twice, but never received a response.

The first filing was for Python 2.2 which contained the rotor module. This module contained weak encryption, but still required filing with the BXA, as far as we understood it, because the key length could be adjusted by the user of the rotor module. The rotor module was since removed from Python. It is not present in Python 2.4 and later.

The second filing with the BXA was for Python 2.4. In Python 2.4 and later, there is no encryption software in the source code. There is, however, wrapper code for openssl. This wrapper in and of itself is not encryption software, but when Python is distributed in binary form, as in the Windows installer, it may contain a copy of the binary of openssl in unmodified form.

### Which open source license should I use? 

This is a tough question to answer. In general, you should use one of the [OSI approved licenses](http://opensource.org/licenses/) . If you think your code may eventually make it into Python or its standard libraries, you could already use one of the acceptable initial licenses for contribution of code to the PSF (these are [listed below](PythonSoftwareFoundationLicenseFaq#WhatifIwanttocontributemycodetothePSF.3F)). This is not a requirement since you\'ll be able to re-license your code later, as long as all copyright holders in the work at the time agree. But using a license compatible with the contribution process *may* make life easier in the long run if it avoids extra work for your company\'s legal department when it comes time to contribute the code.

Note that OSI approved open source licenses vary quite a bit in how strongly they grant rights to the user. For example, some licenses explicitly grant rights to patents held now or in the future by the licensor. Many others do not. At the same time, some licenses like the [GPL](http://opensource.org/licenses/gpl-license.php) place restrictions on redistribution and usage that may not be acceptable either to you or to your potential users.

One thing is for sure: Slapping a license willy nilly on your code is a bad idea. You should be informed about what licensing is and whether your chosen license is going to do what you want it to.

When in doubt, buy a book on open source licensing.

### How do I use the PSF License? 

The PSF license was developed specifically and only for Python and its standard libraries. If you want to license your code for contribution to the PSF, do not use the PSF license; instead [see below](PythonSoftwareFoundationLicenseFaq#WhatifIwanttocontributemycodetothePSF.3F).

Many projects on Source Forge and elsewhere have adopted the PSF license, but not always in an appropriate way. If you feel the PSF License is the one to use with your code, you must change the following parts of the license:

- Replace all occurrences of \"Python Software Foundation\" and \"PSF\" with your name or organization.
- Replace \"Python\" with the name of your project.

This includes altering the copyright notice in paragraph 2. The author of the work holds the copyright, not the PSF. While you could transfer copyright to the PSF, that requires a legal process and in most cases the PSF has no interest or reason to accept the copyrights of works outside of Python and its standard libraries.

Consulting an attorney may be a good idea to make sure your changes to the license are appropriate and correct.

Note that the PSF license consists only of the top license in the \"license stack\" that is included in Python. The current (as of this writing) version of the PSF license is [PythonSoftwareFoundationLicenseV2Easy](PythonSoftwareFoundationLicenseV2Easy). When using the PSF License with your project, you should never include the other parts of the Python license stack, such as the CNRI license or Guido\'s biography. Python has that history, but your code does not!

## Contributing Code to Python 

### What if I want to contribute my code to the PSF? 

The PSF does not want contributions of any code other than that which will end up in Python or its standard libraries, or in Jython.

If your code is going to end up in Python or the standard library, the PSF will require you to:

- License your code under an acceptable open source license. These currently include only the [Academic Free License 2.1](http://www.samurajdata.se/opensource/mirror/licenses/afl-2.1.php) ([local copy](PythonSoftwareFoundationLicenseFaq/AFL-2.1)) and the [Apache License 2.0](http://www.opensource.org/licenses/apache2.0.php) ([local copy](PythonSoftwareFoundationLicenseFaq/Apache-License-2.0)), although this list may be expanded in the future. (No, the PSF License is not acceptable; see below)

- Fill out and submit a [contributor agreement](http://www.python.org/psf/contrib/contrib-form/).

For details, see [Contributing to the PSF](http://www.python.org/psf/contrib/).

### Why can\'t I contribute code under the PSF License? 

The initial open source license under which the contribution is released to the PSF is the legal agreement that grants most of the rights the PSF will have to that code. The contribution agreement itself just gives the PSF the right to redistribute the work under a different license.

For this reason, and in order to protect contributions from future claims, the PSF requires that the initial open source license contain a clause that specifically grants the right to use patents held now or in the future by the contributor.

While it seems somewhat ironic that the PSF license cannot be used as the initial license on contributions, the approach does make sound legal sense.

### Who signs the contributor agreement? 

If the contributor is an employee, then the company should sign the contributor agreement unless (1) the company authorized the employee to make the contribution under his/her own name, or (2) the employee\'s contribution was independently created outside the scope of his employment. If the contributor is a contractor rather than an employee, then he/she may make the contribution unless his/her contract with the company says otherwise.

When in doubt, a potential contributor should ask their attorney or manager. Ordinarily it is up to the company to train its employees and contractors and to enforce its own policies and contracts; anything else may be their own \"negligent supervision.\"

### What do I put on the \"title\" line of the contributor agreement? 

The \"title\" line is only important for companies signing the agreement. For individuals that are contributing code written in their spare time, the line can be left blank.

For companies, only company authorized personnel may sign the agreement and this authorization has to be made clear by including the title of the undersigning person within the company.

Please note that agreements signing by unauthorized employees of a company are void and can create potential problems for the PSF.

Typical titles are \"CEO\", \"Chairman\", \"Owner\", etc.

### How do I define the Contribution mentioned in the contributor agreement 

After you have signed the PSF contributor agreement, please include the following lines in all contributed files or patches:

    Copyright (c) <year>, <your name>
    Licensed to PSF under a Contributor Agreement.

If in doubt, please raise the question on the tracker. A core developer will then guide you.
