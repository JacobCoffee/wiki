# Log4jExample

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# log4j Example 

[OtherExamples](OtherExamples)

------------------------------------------------------------------------

This example require several things.

- log4j on the classpath
- log4j.properties (below) in the same directory as the example
- example.xml (below) in the same directory as the example
- the example below
- And of course Jyhton 2.2

This was tested with Jython 2.2 and Java JVM 1.5 and 1.4.2

#### log4j Example 

- This is a simple example to show how easy it is to use log4j in your own scripts. The source is well documented but if you have any questions or want to more info use your favorite search engine and type in log4j.

:::: 
::: 
``` 
   1 from org.apache.log4j import * 
   2 
   3 class logtest:
   4     def __init__(self):
   5 
   6   log.info("start of Logtest")
   7   log.debug('just before file read')
   8   try:
   9    log.warn('file read proceding to processing')
  10    xmlStringData = open('example.xml').read()
  11   except:       
  12    #yes, more could have been done here but this is just an example
  13    log.error('file read FAILURE')
  14   log.info('file read proceding to processing') 
  15   # since this is just an example processing would go here.
  16   #
  17   #you can also log variables
  18   log.warn('its just an example, OK?')
  19   pi = 3.141592681
  20   msg = 'do you like?' + str(pi)
  21   log.info(msg)
  22   log.debug('lets try to parse the string')
  23   if '[CDATA' in xmlStringData:
  24    log.warn('No CDATA section.')                        
  25   #say good bye and close the log file.
  26   log.info('That all. The End. Good Bye')
  27   log.shutdown()
  28 
  29 
  30 if __name__ == '__main__':
  31     # loggingTest is just a string that identifies this log.
  32     log = Logger.getLogger("loggingTest")
  33     #use the config data in the properties file
  34     PropertyConfigurator.configure('log4j.properties')
  35     log.info('This is the start of the log file')
  36     logit = logtest()
  37     print '\n\nif you change the log level in the properties'
  38     print "file you'll get varing amouts of log data."
```
:::
::::

#### log4j.properties

- This file is required by the code above. it need to be in the same directory as the example however It can be anywhere as log as you provide a full path to the file. it configures how log4j operates. If it is not found it defaults to a default logging level. Since this is for example purposes the file below is larger then really needed.

<!-- -->

    #define loging level and output
    log4j.rootLogger=debug, stdout, LOGFILE
    #log4j.rootLogger=info, LOGFILE
    # this 2 lines tie the apache logging into log4j
    #log4j.logger.org.apache.axis.SOAPPart=DEBUG
    #log4j.logger.httpclient.wire.header=info
    #log4j.logger.org.apache.commons.httpclient=DEBUG

    # where is the logging going. 
    # This is for std out and defines the log output format
    log4j.appender.stdout=org.apache.log4j.ConsoleAppender
    log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
    log4j.appender.stdout.layout.ConversionPattern=%d{HH:mm:ss,SSS} | %p | [%c] %m%n %t

    #log it to a file as well. and define a filename, max file size and number of backups
    log4j.appender.LOGFILE=org.apache.log4j.RollingFileAppender
    log4j.appender.LOGFILE.File=jythonTest.log
    log4j.appender.LOGFILE.MaxFileSize=100KB
    # Keep one backup file
    log4j.appender.LOGFILE.MaxBackupIndex=1

    log4j.appender.LOGFILE.layout=org.apache.log4j.PatternLayout
    # Pattern for logfile - only diff is that date is added
    log4j.appender.LOGFILE.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} | %p | [%c] %m%n
    # Other Examples: only time, loglog level, loggerName
    #log4j.appender.LOGFILE.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss},%p,%c %m%n
    #above plus filename, linenumber, Class Name, method name
    #log4j.appender.LOGFILE.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss},%p,%c,%F,%L,%C{1},%M %m%n

#### Example xml file 

- This is here for completeness. Any text file could be use with the example above by changing the \'open\' line

in the above line.

    <?xml version="1.0" encoding="utf-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" 
                       xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" 
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xmlns:xsd="http://www.w3.org/2001/XMLSchema">
      <SOAP-ENV:Body>
        <GetXmlReport xmlns="http://localhost/Services/GetXmlReport">
          <xmlrequest>
            <Inquiry>
              <Client>
                <Type>W</Type>
              </Client>
              <Report>I</Report>
              <Provider>
                <ProviderID>TU</ProviderID>
              </Provider>
              <ClientInfo>
                <Name>
                  <First>Cathrine</First>
                  <Middle />
                  <Surname>Knight</Surname>
                </Name>
                <Account>34-5424-77</Account>
                <DateOfBirth>10/12/1938</DateOfBirth>
                <Address>
                  <Line1>4780 Centerville</Line1>
                  <CityStPostal>Saint Paul, MN 55127</CityStPostal>
                </Address>
              </ClientInfo>
            </Inquiry>
          </xmlrequest>
        </GetXmlReport>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
