# TrackerAccessControl

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The permissions in the table are as follows:

- R: View
- r: View if it is not classified as spam (full read to fields creation, creator, actor, activity, name, spambayes_score, spambayes_misclassified, author, recipients, date, files, messageid, inreplyto, type, description; no access if spam to content, summary)
- C: Create
- E: Edit
- e: Edit one\'s own data
- v: view one\'s own data

The classes can be roughly divided into enumerations (issue_type, severity, component, version, priority, status, resolution, keyword), content (issue, msg, file), and administration (user, query).

::: {}
  -------------------------- ----------- ------ ----------- -------------
  Class.Field                Anonymous   User   Developer   Coordinator
  issue_type                 R           R      R           RCE
  severity                   R           R      R           RCE
  component                  R           R      R           RCE
  version                    R           R      R           RCE
  priority                   R           R      R           RCE
  status                     R           R      R           RCE
  resolution                 R           R      R           RCE
  keyword                    R           R      RCE         RCE
  issue                      R           RC     RCE         RCE
  file                       r           RC     RCE         RCE
  msg                        r           RC     RCE         RCE
  user                       C           Rv     Rv          RE
  query                                  vCe    vCe         vCe
  public query                           RC     RC          RC
  issue.title                            E                  
  issue.type                             E                  
  issue.components                       E                  
  issue.versions                         E                  
  issue.severity                         E                  
  issue.messages                         E                  
  issue.files                            E                  
  issue.nosy                             E                  
  user.username                          e      e           
  user.password                          e      e           
  user.address                           e      e           
  user.realname                          e      e           
  user.phone                             e      e           
  user.organization                      e      e           
  user.alternate_addresses               e      e           
  user.queries                           e      e           
  user.timezone                          e      e           
  -------------------------- ----------- ------ ----------- -------------
:::

In addition, the following permissions are granted:

- Anonymous: Web access
- User, Developer, Coordinator: Web and Email access, May Report Misclassified
- Coordinator: May Classify
