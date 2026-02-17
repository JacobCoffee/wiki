# SimpleApp

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Apache Sampleapp.java 

back to [ApacheDerby](ApacheDerby) Example

\--

:::: 
::: 
``` 
   1 /*
   2    Derby - Class SimpleApp
   3  */
   4 
   5 import java.sql.Connection;
   6 import java.sql.DriverManager;
   7 import java.sql.ResultSet;
   8 import java.sql.SQLException;
   9 import java.sql.Statement;
  10 
  11 import java.util.Properties;
  12 
  13 
  14 /**
  15  * This sample program is a minimal JDBC application showing
  16  * JDBC access to Derby.
  17  *
  18  * Instructions for how to run this program are
  19  * given in <A HREF=example.html>example.html</A>.
  20  *
  21  * Derby applications can run against Derby running in an embedded
  22  * or a client/server framework. When Derby runs in an embedded framework,
  23  * the Derby application and Derby run in the same JVM. The application
  24  * starts up the Derby engine. When Derby runs in a client/server framework,
  25  * the application runs in a different JVM from Derby. The application only needs
  26  * to start the client driver, and the connectivity framework provides network connections.
  27  * (The server must already be running.)
  28  *
  29  * <p>When you run this application, give one of the following arguments:
  30  *    * embedded (default, if none specified)
  31  *    * derbyclient (will use the Net client driver to access Network Server)
  32  *    * jccjdbcclient (if Derby is running embedded in the JCC Server framework)
  33  *
  34  */
  35 public class SimpleApp
  36 {
  37     /* the default framework is embedded*/
  38     public String framework = "embedded";
  39     public String driver = "org.apache.derby.jdbc.EmbeddedDriver";
  40     public String protocol = "jdbc:derby:";
  41     
  42     public String username = "user1";
  43     public String password = "user1";
  44 
  45     public static void main(String[] args)
  46     {
  47         new SimpleApp().go(args);
  48     }
  49 
  50     void go(String[] args)
  51     {
  52         /* parse the arguments to determine which framework is desired*/
  53         parseArguments(args);
  54 
  55         /* check for J2ME specification - J2ME must use a DataSource further on */
  56         String javaspec = System.getProperty( "java.specification.name" );
  57         boolean java2me = false;
  58         if( javaspec.indexOf( "J2ME" ) > -1 )
  59         {
  60             java2me = true;
  61         }
  62         System.out.println(java2me);
  63         System.out.println("SimpleApp starting in " + framework + " mode.");
  64 
  65         try
  66         {
  67             /*
  68                The driver is installed by loading its class.
  69                In an embedded environment, this will start up Derby, since it is not already running.
  70              */
  71             org.apache.derby.jdbc.EmbeddedSimpleDataSource ds = null;
  72             Connection conn = null;
  73             Properties props = new Properties();
  74             props.put("user", username);
  75             props.put("password", password);
  76 
  77             /* If we are using a J2ME jvm, we need to use a DataSource, otherwise
  78              * we can use java.sql.DriverManager to get the connection, or
  79              * a Datasource. This example program uses a DataSource with J2ME
  80              * but uses DriverManager otherwise.
  81              * If we were to use a DataSource for J2SE, we could use
  82              * the org.apache.derby.jdbc.EmbeddedDataSource, rather than the
  83              * org.apache.derby.jdbc.EmbeddedSimpleDataSource we need to use for J2ME.
  84              */
  85          
  86             if( java2me )
  87             {
  88                 /*
  89                    The connection specifies create in the DataSource settings for
  90                    the database to be created. To remove the database,
  91                    remove the directory derbyDB and its contents.
  92                    The directory derbyDB will be created under
  93                    the directory that the system property
  94                    derby.system.home points to, or the current
  95                    directory if derby.system.home is not set.
  96                  */
  97        
  98                 ds = new org.apache.derby.jdbc.EmbeddedSimpleDataSource();
  99                 ds.setDatabaseName("derbyDB");
 100                 ds.setCreateDatabase("create");
 101                 conn = ds.getConnection(username, password);
 102                 
 103                 System.out.println("this is Java2Me");
 104             }
 105             else
 106             {
 107                 System.out.println("this is NOT Java2Me");
 108                 /*
 109                    The connection specifies create=true in the url to cause
 110                    the database to be created. To remove the database,
 111                    remove the directory derbyDB and its contents.
 112                    The directory derbyDB will be created under
 113                    the directory that the system property
 114                    derby.system.home points to, or the current
 115                    directory if derby.system.home is not set.
 116                  */
 117           
 118                 Class.forName(driver).newInstance();
 119                 System.out.println("Loaded the appropriate driver.");
 120             
 121                 conn = DriverManager.getConnection(protocol +
 122                     "derbyDB;create=true", props);
 123             }
 124             System.out.println("Connected to and created database derbyDB");
 125 
 126             conn.setAutoCommit(false);
 127 
 128             /*
 129                Creating a statement lets us issue commands against
 130                the connection.
 131              */
 132             Statement s = conn.createStatement();
 133 
 134             /*
 135                We create a table, add a few rows, and update one.
 136              */
 137             s.execute("create table derbyDB(num int, addr varchar(40))");
 138             System.out.println("Created table derbyDB");
 139             s.execute("insert into derbyDB values (1956,'Webster St.')");
 140             System.out.println("Inserted 1956 Webster");
 141             s.execute("insert into derbyDB values (1910,'Union St.')");
 142             System.out.println("Inserted 1910 Union");
 143             s.execute(
 144                 "update derbyDB set num=180, addr='Grand Ave.' where num=1956");
 145             System.out.println("Updated 1956 Webster to 180 Grand");
 146 
 147             s.execute(
 148                 "update derbyDB set num=300, addr='Lakeshore Ave.' where num=180");
 149             System.out.println("Updated 180 Grand to 300 Lakeshore");
 150 
 151             /*
 152                We select the rows and verify the results.
 153              */
 154             ResultSet rs = s.executeQuery(
 155                     "SELECT num, addr FROM derbyDB ORDER BY num");
 156 
 157             if (!rs.next())
 158             {
 159                 throw new Exception("Wrong number of rows");
 160             }
 161 
 162             if (rs.getInt(1) != 300)
 163             {
 164                 throw new Exception("Wrong row returned");
 165             }
 166 
 167             if (!rs.next())
 168             {
 169                 throw new Exception("Wrong number of rows");
 170             }
 171 
 172             if (rs.getInt(1) != 1910)
 173             {
 174                 throw new Exception("Wrong row returned");
 175             }
 176 
 177             if (rs.next())
 178             {
 179                 throw new Exception("Wrong number of rows");
 180             }
 181 
 182             System.out.println("Verified the rows");
 183 
 184             s.execute("drop table derbyDB");
 185             System.out.println("Dropped table derbyDB");
 186 
 187             /*
 188                We release the result and statement resources.
 189              */
 190             rs.close();
 191             s.close();
 192             System.out.println("Closed result set and statement");
 193 
 194             /*
 195                We end the transaction and the connection.
 196              */
 197             conn.commit();
 198             conn.close();
 199             System.out.println("Committed transaction and closed connection");
 200 
 201             /*
 202                In embedded mode, an application should shut down Derby.
 203                If the application fails to shut down Derby explicitly,
 204                the Derby does not perform a checkpoint when the JVM shuts down, which means
 205                that the next connection will be slower.
 206                Explicitly shutting down Derby with the URL is preferred.
 207                This style of shutdown will always throw an "exception".
 208              */
 209             boolean gotSQLExc = false;
 210 
 211             if (framework.equals("embedded"))
 212             {
 213                 /* again, with J2ME, we need to use a datasource to get the connection */
 214                 if( java2me )
 215                 {
 216                     try
 217                     {
 218                         ds.setShutdownDatabase( "shutdown" );
 219                         conn = ds.getConnection(username, password);
 220                     }
 221                     catch (SQLException se)
 222                     {
 223                         if( se.getErrorCode() == 45000 )
 224                         {
 225                             gotSQLExc = true;
 226                         }
 227                     }
 228                 }
 229                 else                  
 230                 {   
 231                     try
 232                     {
 233                         DriverManager.getConnection("jdbc:derby:;shutdown=true");
 234                     }
 235                     catch (SQLException se)
 236                     {
 237                         gotSQLExc = true;
 238                     }
 239                 }
 240 
 241                 if (!gotSQLExc)
 242                 {
 243                     System.out.println("Database did not shut down normally");
 244                 }
 245                 else
 246                 {
 247                     System.out.println("Database shut down normally");
 248                 }
 249             }
 250         }
 251         catch (Throwable e)
 252         {
 253             System.out.println("exception thrown:");
 254 
 255             if (e instanceof SQLException)
 256             {
 257                 printSQLError((SQLException) e);
 258             }
 259             else
 260             {
 261                 e.printStackTrace();
 262             }
 263         }
 264 
 265         System.out.println("SimpleApp finished");
 266     }
 267 
 268     static void printSQLError(SQLException e)
 269     {
 270         while (e != null)
 271         {
 272             System.out.println(e.toString());
 273             e = e.getNextException();
 274         }
 275     }
 276 
 277     private void parseArguments(String[] args)
 278     {
 279         int length = args.length;
 280 
 281         for (int index = 0; index < length; index++)
 282         {
 283             if (args[index].equalsIgnoreCase("jccjdbcclient"))
 284             {
 285                 framework = "jccjdbc";
 286                 driver = "com.ibm.db2.jcc.DB2Driver";
 287                 protocol = "jdbc:derby:net://localhost:1527/";
 288             }
 289             if (args[index].equalsIgnoreCase("derbyclient"))
 290             {
 291                 framework = "derbyclient";
 292                 driver = "org.apache.derby.jdbc.ClientDriver";
 293                 protocol = "jdbc:derby://localhost:1527/";
 294             }
 295         }
 296     }
 297 }
```
:::
::::

back to [ApacheDerby](ApacheDerby) Example
