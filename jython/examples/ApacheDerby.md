# ApacheDerby

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Apache Derby Example(s) 

back to [OtherExamples](OtherExamples)

\-- Posted on the Jython-users mailing list by Alfonso Reyes, September 2007

This Derby example doesn\'t need the use of zxJDBC. I was looking to complete the exercises in the book \"Python programming with Java libraries\" but couldn\'t find anywhere a site to download InstantDB. Trying Apache Derby was quite a pleasant experience. I am attaching files here.

[RSMD.py](./RSMD(2e)py.html) is a database utility I found in IBM.\
[SimpleApp](SimpleApp).java the original Java demo

If you follow the instructions in this tutorial everything will go smooth. [Derby Tutorial](http://db.apache.org/derby/papers/DerbyTut/install_software.html). (note: there is also a lot of info on their wiki)

:::: 
::: 
``` 
   1 """ Derby Class SimpleApp.py
   2     Add derby.jar to your CLASSPATH
   3     Ported by: Alfonso Reyes, September 2007
   4 
   5 """
   6 from RSMD import printRSMD, RSMD    # nice methods I downloaded from IBM site
   7 from java.sql import Connection, DriverManager, ResultSet, SQLException, Statement
   8 
   9 from java.util import Properties
  10 from java.lang import Class
  11 
  12 class SimpleApp:
  13     def __init__(self):
  14         # the default framework is embedded
  15         self.framework = "embedded"
  16         self.driver = "org.apache.derby.jdbc.EmbeddedDriver"
  17         self.protocol = "jdbc:derby:"
  18         self.username = "user1"
  19         self.password = "user1"
  20 
  21     def go(self):
  22         # parse the arguments to determine which framework is desired
  23         #parseArguments(args)
  24         """   The driver is installed by loading its class.
  25         In an embedded environment, this will start up Derby, since it is not already running.
  26 
  27         """
  28         ds = None
  29         conn = None
  30         props = Properties()
  31         props.put("user", self.username)
  32         props.put("password", self.password)
  33         print props
  34 
  35         # check for J2ME specification - J2ME must use a DataSource further on */
  36         javaspec = props.getProperty( "java.specification.name" )
  37 
  38         """
  39            The connection specifies create=true in the url to cause
  40            the database to be created. To remove the database,
  41            remove the directory derbyDB and its contents.
  42            The directory derbyDB will be created under
  43            the directory that the system property
  44            derby.system.home points to, or the current
  45            directory if derby.system.home is not set.
  46 
  47          """
  48         Class.forName(self.driver).newInstance()
  49         print "Loaded the appropriate driver."
  50 
  51         database = "derbyDB5"   # put here the name for your database
  52         dbStr = self.protocol + database + ";create=true"
  53         print dbStr
  54         conn = DriverManager.getConnection(dbStr, props)
  55         print "Connected to and created database derbyDB"
  56 
  57         conn.setAutoCommit(False)
  58 
  59         """    Creating a statement lets us issue commands against
  60         the connection.
  61 
  62         """
  63         s = conn.createStatement()
  64 
  65         #   We create a table, add a few rows, and update one.
  66         s.execute("create table derbyDB(num int, addr varchar(40))")
  67         print "Created table derbyDB"
  68         s.execute("insert into derbyDB values (1956,'Webster St.')")
  69         print "Inserted 1956 Webster"
  70         s.execute("insert into derbyDB values (1910,'Union St.')")
  71         print "Inserted 1910 Union"
  72         s.execute("insert into derbyDB values (1,'Wandering Oak')")
  73         print "Inserted 1 Wandering Oak"
  74 
  75         s.execute(
  76             "update derbyDB set num=180, addr='Grand Ave.' where num=1956")
  77         print "Updated 1956 Webster to 180 Grand"
  78 
  79         s.execute(
  80             "update derbyDB set num=300, addr='Lakeshore Ave.' where num=180")
  81         print "Updated 180 Grand to 300 Lakeshore"
  82 
  83         #  We select the rows and verify the results.
  84         rs = s.executeQuery("SELECT num, addr FROM derbyDB ORDER BY num")
  85 
  86         print "Verified the rows"
  87         stmt   = conn.createStatement()
  88         Query  = 'SELECT * FROM derbyDB'
  89         rs     = stmt.executeQuery( Query )
  90         rsmd   = RSMD( rs )
  91         printRSMD( rsmd, Query )
  92 
  93         rowCount = 0
  94         while ( rs.next() ) :
  95             rowCount += 1
  96             row = ( rs.getInt( 1 ), rs.getString( 2 ) )
  97             print row
  98 
  99         stmt.close()        # close stmt connection
 100         s.execute("drop table derbyDB")
 101         print"Dropped table derbyDB"
 102 
 103         # We release the result and statement resources.
 104         rs.close()
 105         s.close()
 106         print "Closed result set and statements"
 107 
 108         #  We end the transaction and the connection.
 109         conn.commit()
 110         conn.close()
 111         print "Committed transaction and closed connection"
 112 
 113         """   In embedded mode, an application should shut down Derby.
 114            If the application fails to shut down Derby explicitly,
 115            the Derby does not perform a checkpoint when the JVM shuts down, which means
 116            that the next connection will be slower.
 117            Explicitly shutting down Derby with the URL is preferred.
 118            This style of shutdown will always throw an "exception".
 119 
 120         """
 121         gotSQLExc = False
 122         try:
 123             DriverManager.getConnection("jdbc:derby:;shutdown=true")
 124         except SQLException:
 125             print "Catching exceptions"
 126             gotSQLExc = True
 127 
 128         if (not gotSQLExc):
 129             print "Database did not shut down normally"
 130         else:
 131             print "Database shut down normally"
 132         print("SimpleApp finished")
 133 
 134 if __name__ == '__main__':
 135     SimpleApp().go()
```
:::
::::
