# TwistedWebServerSampleOnWindows

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

It\'s a little tricky getting twisted to run as a service in twisted 1.3. A main service .exe must spawn a new python process, because twisted must initialize in the main thread, and services don\'t start in the main thread. Its easiest to write the service wrapper in python.

I also found its easiest to register the service, then change which account the service runs as.

You could probably choose the child python script to run as

    python.exe twistd.py -f web.tap

if you know how to set up the web.tap.

# Service Wrapper 

    #based on http://twistedmatrix.com/pipermail/twisted-python/2003-October/006081.html

    import sys, os
    import win32serviceutil, win32service
    import win32api
    from  webserver import WebServer
    from subprocess import Popen,call

    class TwistedWebService(win32serviceutil.ServiceFramework):
        """NT Service."""
        
        _svc_name_ = "TwistedWebServer"
        _svc_display_name_ = "TwistedWebServer"
        def SvcDoRun(self):
            self.childServer = Popen(["python","d:/doug/dev/play/twisted/webserver.py"])
            self.childServer.wait()
            
        def SvcStop(self):
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
            self.kill(self.childServer.pid)

        def kill(self,pid):
            """kill function for Win32"""
            handle = win32api.OpenProcess(1, 0, pid)
            return (0 != win32api.TerminateProcess(handle, 0))


    if __name__ == '__main__':
        win32serviceutil.HandleCommandLine(TwistedWebService)

# Web Server 

    from twisted.web import static, server, script,error
    from twisted.application import internet, service


    class WebServer:

        #This is hacked together and not necessarily a good example
        def WebServerConfig(self):
             """return a site object that can supplied to a reactor"""
             root = static.File("d:/doug/wwwroot")
             files = ["d:/doug/dev/play/twisted/mime.types"]
             static.loadMimeTypes(files)

             skiRoot = error.NoResource()


             ski = root.putChild("ski",skiRoot)



             powderTour2k2 = static.File("D:/ransom/photos/2002-PowderTour/PowderTour2k2-selected")
             skiRoot.putChild("powdertour2k2",powderTour2k2)

             scrape =static.File("d:/doug/documents/scraping/general")
             scrapeRoot=root.putChild("scrape",scrape)
             
             root.ignoreExt(".rpy")
             root.processors = {'.rpy': script.ResourceScript}
             application = service.Application('web')
             serviceCollection = service.IServiceCollection(application)
             site = server.Site(root)
             return (site,application,serviceCollection)

        def Run(self):
            logpath="d:/doug/dev/play/twisted/log.txt";
            f = open(logpath, 'a')
            
            from twisted.python.log import startLogging
            from twisted.application.app import startApplication
            from twisted.internet import reactor
            
            startLogging(f)
            (site,application,serviceCollection) = self.WebServerConfig()
            startApplication(application, 0)
            #         i = internet.TCPServer(8089, site)
            #         i.setServiceParent(serviceCollection)
            
            reactor.listenTCP(8080, site)
            reactor.run()
            
        def Stop(self):
            reactor.stop()

    if __name__ == '__main__':
        WebServer().Run()
