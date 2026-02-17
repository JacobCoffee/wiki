# OromoLanguage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Oromo** ( Oromo: *Afaan Oromoo*) is an Afroasiatic language belonging to the *Cushitic branch*. It is native to the Ethiopian state of Oromia and spoken predominantly by the Oromo people and neighbouring ethnic groups in the Horn of Africa ;[https://www.ethnologue.com/browse/families](./HornofAfrica.html).

**Afaan Oromoo**

:::: 
::: 
``` 
   1 # Python 3.0/3.1
   2 
   3 # English
   4 
   5 """ E.g., let us create a class called student, which attributes such as I.D. number, name, number of items and cost. """
   6 
   7 class Student:
   8     id = "test id"
   9     name = "name"
  10     numberofitems = 0
  11     cost = 0.00
  12     
  13     def __init__(self,id, name, age):
  14         self.id = id
  15         self.name=name
  16         self.age = age
  17     
  18     def getName(self):
  19         return self.name
  20     
  21     def printStudent(self):
  22         print self.id, "$$$$$ ", self.name
  23         
  24     def total(self,items, cost):
  25         self.numberofitems = items
  26         self.cost = cost
  27         return self.numberofitems * self.cost
  28     
  29     
  30 
  31 student = Student("123","sisaz",23)
  32 
  33 student.printStudent()
  34 
  35 
  36 
  37 # Afaan Oromoo
  38 
  39 """ Akka fakkeenyatti, kutaa Barataa jedhu haa fudhannu. Kutaa kana keessatti, lakkoofsi galmee, maqaan, baay'inni fi kaffaltiin hammatamanii argamu."""
  40 
  41 class Barataa:
  42     id = "Lakk. galmee"
  43     maqaa = "Maqaa"
  44     baayina = 0
  45     kaffaltii = 0.00
  46     
  47     def __init__(self,id, maqaa, umurii):
  48         self.id = id
  49         self.maqaa=maqaa
  50         self.umurii = umurii
  51     
  52     def getName(self):
  53         return self.maqaa
  54     
  55     def printBarataa(self):
  56         print self.id, "$$$$$ ", self.maqaa
  57         
  58     def Walii_gala(self, baayina, kaffaltii):
  59         self.numberofitems = baayina
  60         self.kaffaltii = kaffaltii
  61         return self.baayina * self.kaffaltii
  62     
  63     
  64 
  65 barataa = Barataa("123","Boona",23)
  66 
  67 student.printBarataa()
```
:::
::::

------------------------------------------------------------------------

[CategoryLanguage](CategoryLanguage)
