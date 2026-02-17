# Admin/NewUsers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Adding New User Accounts 

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

Only logins using SSH authentication are allowed; password-authenticated logins are not supported.

1.  Create the user account. The Debian tool for doing this is useradd:

        sudo useradd -G svnusers,webmaster -c "<full name>" -m <account-name>

2.  Create the user\'s SSH authorization keys.

        cd ~<account-name>
        mkdir .ssh
        chmod 700 .ssh/
        jed .ssh/authorized_keys2
        chmod 600 .ssh/authorized_keys2 
