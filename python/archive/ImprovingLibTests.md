# ImprovingLibTests

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page documents all tests that should be added (or improved) to enhance the Python distribution\'s test suite for the standard library. Checking [Coverage](http://coverage.livinglogic.de/coverage/web/waf.do) to see if there are any tests that could be improved or are missing, would be a real help. Also if you just generally think that a unit test needs improving, please add it here with a list of what could be improved.

If you feel that you would like to work on a test, please write your name in the \'Volunteer\' column of the table below, alongside the name of the test you wish to work on.

Please try to get all tests in alphabetical order

### New Tests 

::: {}
  --------------------------------- ---------------
  Test Name                         Volunteer
  Lib/test/test_asyncore.py         
  Lib/test/test_audiodev.py         
  Lib/test/test_bdb.py              
  Lib/test/test_cgitb.py            
  Lib/test/test_chunk.py            
  Lib/test/test_cmd.py              
  Lib/test/test_compileall.py       
  Lib/test/test_dbhash.py           
  Lib/test/test_formatter.py        
  Lib/test/test_ftplib.py           
  Lib/test/test_getpass.py          
  Lib/test/test_gopherlib.py        
  Lib/test/test_htmlentitydefs.py   
  Lib/test/test_ihooks.py           
  Lib/test/test_imghdr.py           
  Lib/test/test_imputil.py          
  Lib/test/test_keyword.py          
  Lib/test/test_linecache.py        
  Lib/test/test_macurl2path.py      
  Lib/test/test_mailcap.py          
  Lib/test/test_markupbase.py       
  Lib/test/test_mimify.py           
  Lib/test/test_modulefinder.py     
  Lib/test/test_mutex.py            
  Lib/test/test_nntplib.py          
  Lib/test/test_opcode.py           
  Lib/test/test_os2emxpath.py       
  Lib/test/test_pdb.py              
  Lib/test/test_pipes.py            Alan Mcintyre
  Lib/test/test_pkgutil.py          Matt Fleming
  Lib/test/test_poplib.py           
  Lib/test/test_posixfile.py        
  Lib/test/test_pstats.py           
  Lib/test/test_py_compile.py       
  Lib/test/test_pydoc.py            
  Lib/test/test_rexec.py            
  Lib/test/test_rlcompleter.py      
  Lib/test/test_sched.py            
  Lib/test/test_smtpd.py            
  Lib/test/test_smtplib.py          
  Lib/test/test_sndhdr.py           
  Lib/test/test_sre.py              
  Lib/test/test_sre_compile.py      
  Lib/test/test_sre_constants.py    
  Lib/test/test_stat.py             
  Lib/test/test_statvfs.py          
  Lib/test/test_stringold.py        
  Lib/test/test_sunau.py            
  Lib/test/test_sunaudio.py         
  Lib/test/test_symbol.py           
  Lib/test/test_tabnanny.py         
  Lib/test/test_telnetlib.py        
  Lib/test/test_this.py             
  Lib/test/test_timeit.py           
  Lib/test/test_toaiff.py           
  Lib/test/test_token.py            
  Lib/test/test_tty.py              
  Lib/test/test_user.py             
  Lib/test/test_webbrowser.py       
  --------------------------------- ---------------
:::

## Improve Tests 

::: {}
  ------------------------ ----------------------------- -----------
  Test Name                Things to improve             Volunteer
  Lib/test/test_runpy.py   Test with zip modules \[1\]   
  ------------------------ ----------------------------- -----------
:::

\[1\] The current tests for the runpy module don\'t cover the case of running a module from inside a zip file because the normal tests should still run even if the zipfile module isn\'t available. For Python 2.5, testing that runpy works with modules in zip files was done manually instead. To avoid regressions, this should be covered by the unit tests in 2.6. Doing this as a separate test_runpy_zip.py module is probably the easiest way to avoid messing with the results of the tests for normal filesystem based imports.
