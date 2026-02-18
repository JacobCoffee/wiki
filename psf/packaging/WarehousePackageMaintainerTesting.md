# WarehousePackageMaintainerTesting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Help us test PyPI\'s authentication improvements! 

Warehouse is the code behind the Python Package Repository ([PyPI](https://pypi.org/)). We are seeking maintainers of Projects on PyPI to test our new security improvements while they\'re in beta and send us bug reports. Please help us shake the bugs out!

Feedback on user experience, accessibility, and overall ease of use are welcome; we want to support your workflows for account management and package maintainership. Go to [your account settings](https://pypi.org/manage/account/#two-factor) and try it out!

### Guidelines for Particpation 

- By participating, you agree to abide by the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).

- You must verify your primary email address on your Test PyPI and PyPI accounts before setting up 2FA or an API token.

- You should sign up for the [PyPI Announcement Mailing List](https://mail.python.org/mm3/mailman3/lists/pypi-announce.python.org/) for updates.

### Changes we\'re making 

To increase the security of PyPI downloads, we\'re introducing a few improvements:

#### Two-factor authentication 

[two-factor authentication (2FA)](https://pypi.org/help/#twofa) is a new login security option.

You can use 2FA right now on [Test PyPI](http://test.pypi.org/) and on [official PyPI](https://pypi.org). PyPI currently supports two 2FA methods. One is generating a code through a Time-based One-time Password (TOTP) application. After you set up 2FA on your PyPI account, then you must provide a TOTP (along with your username and password) to log in. Therefore, to use 2FA on PyPI, you\'ll need to provision an application (usually a mobile phone app) in order to generate authentication codes; see below for suggestions and pointers. This feature is fully deployed and out of beta.

**In beta:** We support WebAuthn and thus \"security keys\". A security key (also known as a universal second factor, or U2F key) is hardware device that communicates via USB, NFC, or Bluetooth. Popular keys include Yubikey, Google Titan and Thetis. PyPI supports any [FIDO U2F compatible key](https://fidoalliance.org/specifications/download/) and follows the [!WebAuthn standard](https://www.w3.org/TR/webauthn/). Users who have set up this second factor will be prompted to use their key (usually by inserting it into a USB port and pressing a button) when logging in. The WebAuthn support is **in beta** so check the \"caution\" warning below.

Two-factor authentication currently only applies to the login step, not package uploads.

#### Upload API tokens 

We\'re adding scoped API tokens so you can upload a package using a token instead of a username and password.

**In beta:** You can create and use API tokens to upload packages. API tokens provide an alternative way (instead of username and password) to authenticate when uploading packages to PyPI or Test PyPI. You can create a token for an entire PyPI account, in which case, the token will work for all projects associated with that account. Alternatively, you can limit a token\'s scope to a specific project. And then, manually or in your configuration file, when you upload, use `@token`{.backtick} for the username and the token string for the password. API token support is **in beta** so check the \"caution\" warning below.

#### Audit log 

We\'re adding a display so you can look at things that have happened in your user account or project, and check for signs someone\'s stolen your credentials.

You can view a log of sensitive actions from the last two weeks that are relevant to your user account, and if you are an Owner at least one project on PyPI, you can view a log of sensitive actions (performed by ANY user) relevant to projects you\'re an Owner for. (And PyPI administrators are able to view the full audit log.)

**In beta:** We\'re still refining this, so check the \"caution\" warning below. And the sensitive event logging and display starting on 16 August 2019, so you won\'t see sensitive events from before that date.

### Things to test 

Most of these you can test [on pypi.org](https://pypi.org/manage/account/#two-factor). For testing destructive actions, like removing an owner or deleting a project, please use [test.pypi.org](https://test.pypi.org/manage/account/#two-factor).

#### Caution (before you test) 

During this beta testing period, if things go awry, there\'s a chance we will need to wipe WebAuthn and API tokens from users\' accounts, so if you choose to try it, please be forewarned. That\'s why you need a PyPI-verified email address on [your user account](https://pypi.org/manage/account/) before adding a second login auth factor, to make potential account recovery smoother.

We may also fail to log, or to properly display, events in the audit log.

Reminder! Sign up for the [PyPI Announcement Mailing List](https://mail.python.org/mm3/mailman3/lists/pypi-announce.python.org/) to be kept in the loop as we continue this process!

#### Workflows 

- Verify primary email address: check that the user log lists the event

- Add, disable, and remove 2FA token using TOTP: check that the user log lists the events

- Add, disable, and remove 2FA token using U2F (WebAuthn): check that the user log lists the events

- Login/Logout

- Set multiple 2FA tokens and login: check that the user log lists the events

- Add and remove project-scoped API token, and verify that you see this in the user log

- Add and remove user-scoped API token, and verify that you see this in the user log

- Upload a package using API token, and verify that you see this in the project log

- Remove a user from owner/maintainer status for a project, and verify that their API token for that project stops working and that the project log lists the event

- Delete a release from a project: verify that the project log lists the event

- Delete a project, and verify that an API token scoped for that project stops working

- User Registration and Confirmation

- Password Reset: check that the user log lists the event

#### Testers we need 

In particular, please help us test this if any of these apply to you:

- automate uploads using continuous integration

- save your PyPI credentials in [a \`.pypirc\` file](https://packaging.python.org/guides/distributing-packages-using-setuptools/#create-an-account)

- use Windows

- usually visit PyPI on a mobile device

- are an organization where users share an auth token within a group

- have 4+ maintainers or owners for one project

- use an unusual TOTP app or U2F token

- have a slow Internet connection

- usually block cookies and JavaScript (note that you can\'t set up a U2F key without JavaScript)

- maintain 20+ projects

- created your PyPI account 6+ years ago

#### Setting up a TOTP application 

See [our help docs](https://pypi.org/help/#totp) for guidance on choosing a TOTP app for desktop or mobile.

#### Setting up a U2F security key 

See [our help docs](https://pypi.org/help/#utfkey) for guidance on setting up your U2F security key. Please note that you cannot set up or use U2F for a second factor without turning on JavaScript, and that [right now we only support Chrome, Edge, and Firefox](https://github.com/pypa/warehouse/issues/6034).

#### Provisioning and using API Tokens 

See [our help docs](https://pypi.org/help/#apitoken) for guidance on provisioning and using API Tokens. You can create a token that allows uploads for all projects your user account has Maintainer or Owner access to, or scope it to a specific project.

### Security bugs 

If you find any potential security vulnerabilities, please [follow our published security policy](https://pypi.org/security/). Please don\'t report security issues in Warehouse via GitHub, IRC, or mailing lists. Instead, please directly email one or more of our maintainers.

### Our next steps 

Once we fix all the urgent bugs we find, we\'ll remove the \"beta\" badge for each feature. Then we expect to move on to working on further security, accessibility, and internationalization tasks per [the Warehouse roadmap](https://wiki.python.org/psf/WarehouseRoadmap)). Thanks to the Open Technology Fund for funding this work. More progress reports at [the Packaging Working Group\'s wiki page](https://wiki.python.org/psf/PackagingWG).

### Contact us 

Security issues: [email security @ python dot org](https://pypi.org/security/)

GitHub for all other bug reports & feature requests:[https://github.com/pypa/warehouse/issues/new](https://github.com/pypa/warehouse/issues/new)

IRC: [#pypa-dev on Freenode](https://webchat.freenode.net/?channels=#pypa-dev) (someone\'s usually there 10am-5pm Central Time on weekdays)

Email: [distutils-sig mailing list](https://mail.python.org/mailman3/lists/distutils-sig.python.org/)

Thank you for testing Warehouse! You\'re helping us secure this ecosystem, and future users of PyPI will appreciate it. ![:)](/wiki/europython/img/smile.png%20":)")
