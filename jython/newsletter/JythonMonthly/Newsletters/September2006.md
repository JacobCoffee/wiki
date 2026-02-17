# JythonMonthly/Newsletters/September2006

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  --------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***               ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **September 2006 \-- Issue #3**   
  --------------------------------- ---------------------------------------------------------------------------------------------------
:::

Welcome to the September 2006 issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge. I want to encourage the readers of Jython Monthly to send any articles, tips, tricks, or any other Jython related material to me if you think it should be distributed with this newsletter.

\- Josh Juneau

Questions, comments, or suggestions?

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com) or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net) for discussion.

# Articles 

## Accessing Jython from Java Without Using Jythonc 

[http://wiki.python.org/jython/JythonMonthly/Articles/September2006/1](http://wiki.python.org/jython/JythonMonthly/Articles/September2006/1)

*Submitted By: Josh Juneau*

You may or may not know that it is possible to access Jython code from Java without compiling it using the jythonc utility. This technique is possible using a mixture of Java interfaces and usage of the [PythonInterpreter](./PythonInterpreter.html). As a matter of fact, I believe that using this technique correctly is more effective than using jythonc.

To put it simply, to use this technique you must create a \"factory\" method which uses the [PythonInterpreter](./PythonInterpreter.html) class to interpret a .py module for use within Java code. Any Java code that uses the Jython code should be coded against an interface which is implemented by the Jython code.

In order to provide a fully functional example, I\'ve created a simple application with hard-coded data. This application shows the potential for using this technique within your Java applications to have the ability for use of dynamic Jython objects.

The application is simply called \"jyinterface\" and it contains four pieces of code:

- -Main.java

  \-[JythonFactory](./JythonFactory.html).java - Uses the [PythonInterpreter](./PythonInterpreter.html) to return a Java object

  \-[EmployeeType](./EmployeeType.html).java - An interface which will be implemented by a Jython bean -Employee.py - Jython bean representing an employee

We\'ll start by coding the \"[EmployeeType](./EmployeeType.html).java\" interface which is what our Java code will use in order to interact with the Jython object:

    package jyinterface.interfaces;

    public interface EmployeeType {
        
        public String getEmployeeFirst();
        public String getEmployeeLast();
        public String getEmployeeId();
        
    }

The Jython bean \"Employee.py\" is just a simple Jython object which implements the Java interface \"[EmployeeType](./EmployeeType.html).java\":

    # Jython source file
    from jyinterface.interfaces import EmployeeType

    class Employee(EmployeeType):
       def __init__(self):
          self.first = "Josh"
          self.last  = "Juneau"
          self.id = "myempid"

       def getEmployeeFirst(self):
          return self.first

       def getEmployeeLast(self):
          return self.last

       def getEmployeeId(self):
          return self.id

Next, the most powerful code for this technique is the \"[JythonFactory](./JythonFactory.html).java\" class. This code defines a method which interprets a Jython module into Java and returns for use within Java code. The best part about creating a factory class such as this one is *reuse*! The factory can be coded in many different ways, but this way allows for reuse because you can essentially pass any Java interface/Jython module to it.

    package jyinterface.factory;

    import org.python.util.PythonInterpreter;

    public class JythonFactory {
       private static JythonFactory instance = null;
        
       public static JythonFactory getInstance(){
            if(instance == null){
                instance = new JythonFactory();
            }
            
            return instance;
                  
        }
        
       public static Object getJythonObject(String interfaceName,
                                            String pathToJythonModule){
                  
           Object javaInt = null;
           PythonInterpreter interpreter = new PythonInterpreter();
           interpreter.execfile(pathToJythonModule);
           String tempName = pathToJythonModule.substring(pathToJythonModule.lastIndexOf("/")+1);
           tempName = tempName.substring(0, tempName.indexOf("."));
           System.out.println(tempName);
           String instanceName = tempName.toLowerCase();
           String javaClassName = tempName.substring(0,1).toUpperCase() +
                               tempName.substring(1);
           String objectDef = "=" + javaClassName + "()";
           interpreter.exec(instanceName + objectDef);
            try {
               Class JavaInterface = Class.forName(interfaceName);
               javaInt = 
                    interpreter.get(instanceName).__tojava__(JavaInterface);
            } catch (ClassNotFoundException ex) {
                ex.printStackTrace();  // Add logging here
            }

           return javaInt;
       }
    }

As we stated previously, a Java interface/Jython module combo needs to be passed to the **getJythonObject** method in order to return the resulting code. In the following piece of code, you can see how this is done. Simply pass in two strings:

1.  Fully qualified name of the Java Interface
2.  Full path to the Jython code module

Here is the \"Main.java\" code:

    package jyinterface;

    import jyinterface.interfaces.EmployeeType;
    import jyinterface.factory.JythonFactory;
    import org.python.util.PythonInterpreter;


    public class Main {
        
        EmployeeType et;
        
        /** Creates a new instance of Main */
        public Main() {
        }
        
        /**
         * @param args the command line arguments
         */
        public static void main(String[] args) {
            JythonFactory jf = JythonFactory.getInstance();
            EmployeeType eType = (EmployeeType) jf.getJythonObject(
                                   "jyinterface.interfaces.EmployeeType", "<<path to module>>/Employee.py");
            System.out.println("Employee Name: " + eType.getEmployeeFirst() + " " + 
                        eType.getEmployeeLast());
            System.out.println("Employee ID: " + eType.getEmployeeId());
            
        }
    }

This technique is powerful because it allows an application to use code which can be interchanged or dynamically updated without re-deployment or re-compile. It also follows a great Java practice which is *code against Java interfaces*!! One downfall to this approach is that the code is interpreted every time it is invoked, so the performance may not be as good as using a jythonc compiled piece of code. It obviously depends upon the requirements of the application, but the usefulness of this technique may outweigh the performance factor in many cases.

Next time you plan to create a Java application that contains some Jython code, give this technique a try\...

## Closures in Jython - Simple Example 

[http://wiki.python.org/jython/JythonMonthly/Articles/September2006/2](http://wiki.python.org/jython/JythonMonthly/Articles/September2006/2)

*Submitted By: Josh Juneau*

There has been a lot of discussion regarding closures recently. The topic of closures being added to the a future JDK is hot, but many of you know that this methodology already exists in Jython and Python\...and it is quite easy to use.

In case you are unfamiliar with the topic, please read more about closures and their usage [here](http://en.wikipedia.org/wiki/Closure_(computer_science)).

This brief article was written to show a simple example of how to use closures in Jython. There are various different ways to write a closure in Jython and I will show you two such methods.

This foundation for this example is based around the age old restaurant tip calculator. Many people suggest that a good waitor or waitress shall receive upwards to 20%, and others say that 15% is sufficient. This closure function would prove useful for porting into applications which may require such variations for tip calculation.

Lets place our tip calculator into a module appropriately named calcTip.py and defined as follows:

    def calcTip(x):
       def multiplyTip(y):
          return y + (x * y)
       return multiplyTip

As you can see, the closure is simply a function within a function. Using the popular lambda syntax, this closure can also be written as follows:

    def calcTip(x):
       return lambda y: y + (x * y)

Obviously, using lambda cuts out some typing and it is the preferred method. Now, why would something like this be useful? If we look within the realm of our restaurant tip calculator mentioned above, we will see that this can be extremely useful. So lets say we wish to create an application which will print out a total restaurant bill including tip for three different categories: *Poor Service*, *Mediocre Service*, and *Excellent Service*. Completely defining this application is outside of the context of this brief article, but I can show you the idea with the following lines of code.

Let\'s say we have defined our tip calculator using either of the two closure definitions listed above. We can use it in our example as follows:

    # Calculate tip for bill total of $30.95
    poor = calcTip(.15)             # tip 15 percent
    mediocre = calcTip(.18)        # tip 18 percent
    excellent = calcTip(.20)        # tip 20 percent
    print 'Poor: %s, Mediocre: %s, Excellent %s' % (poor(30.95),mediocre(30.95), excellent(30.95))

Result:

    Poor: 35.5925, Mediocre: 36.521, Excellent 37.14

Of course, you can format the output to suit the needs of your application. As ou can see, this simply spits out the unformatted bill + tip total. If we wanted to, we could pass these functions around just like a regular variable. The possibilities are endless..

Now, hopefully you can appreciate the beauty of closures a bit more!

# Off The Lists 

**Charlie Groves on the Possible Future of Jythonc:**

Speaking of jythonc on the branches, in my dev list spelunking for PyXML info last night I noticed a couple comments that made it sound like jythonc might be unable to support generators. A lack of generator support is definitely causing every jythonc test to fail on the 2.3 branch since they\'ve made their way into the std Python library there. What\'s the plan for jythonc in the future?

One of the things I saw mentioned was that rather than having a full blown .py -\> .java translator like jythonc, we could just have a static proxy bytecode creator. Since having the proxy bytecode in the classpath would allow the interpreter to function in a restricted classloader enviroment, this would allow jython to run everywhere. It would just remove the ability to have Jython code declare a Java calling mechanism with all of the \'@sig\' business. I personally prefer to declare an interface or class in java and have my jython code extend that if I want to call it from java. It removes the complication of having to run jythonc and doesn\'t force a user to learn the new \'@sig\' declaration. Do people really like the \'@sig\' feature of jythonc? Does it allow anything beyond what\'s possible with declaring interfaces in Java? Not that it matters if jythonc can\'t do generators\....

Well, it\'s got enough life in it to last through the 2.2 release at least. I wrote a long spiel about a way to handle all of the jythonc use cases without the bother of compiling to Java like jythonc does, but it looks like Randy Brown already came up with my plan in the bullet points at the bottom of [http://thread.gmane.org/gmane.comp.lang.jython.devel/1429/focus=1430](http://thread.gmane.org/gmane.comp.lang.jython.devel/1429/focus=1430) You should all be thankful that Alan pointed to that thread since my explanation was definitely longer, less clear and more tedious.

**Abhay Posted the Following Question:**

I was wondering if there was a way I could inspect the arguments of a member function of a Java Class in Jython.

*Response by Jeff Emanuel :*

     for a in obj.methodName.argslist:
        print a.data

# Interested in Developing Jython? 

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867) and submit patches for items which you can repair.

# Who\'s Using Jython? 

[Open-source reunion organizer Gather uses a Jython installer](http://gather.sourceforge.net)

[Open Jump - An open source GIS software written in Java](http://openjump.org/wiki/show/HomePage)

# Jython Blogs 

Jython Operator Overloading - [http://pauloherrera.wordpress.com/2006/08/24/operator-overloading-in-java-using-jython/](http://pauloherrera.wordpress.com/2006/08/24/operator-overloading-in-java-using-jython/)

Java isn\'t just Python without the cool language features - [http://rollerweblogger.org/roller/entry/java_isn_t_just_python](http://rollerweblogger.org/roller/entry/java_isn_t_just_python)

# Interesting Facts 

New Benchmark Suite Offering Jython Benchmarks (inteprets a the pybench Python benchmark) - [http://www.dacapobench.org/](http://www.dacapobench.org/)

Jython - Average Job Salary & Stats in UK [http://www.itjobswatch.co.uk/jobs/uk/jython.do](http://www.itjobswatch.co.uk/jobs/uk/jython.do)

# Useful Links 

::: {}
  ----------------------------------------------------------------
  **Links**
  [Jython Home](http://www.jython.org)
  [Python Home](http://www.python.org)
  [Jython WikiPedia](http://en.wikipedia.org/wiki/Jython)
  [Freshmeat.net](http://freshmeat.net/projects/jython/)
  [Python Daily News](http://www.pythonware.com/daily/)
  ----------------------------------------------------------------
:::
