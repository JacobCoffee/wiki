# Asking for Help/with newton force calculator

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: with newton force calculator 

## Verables: 

:::: 
::: 
``` 
N = newton force,
M = Mass,
X = X axis,
Z = Z axis,
Y = Y axis,
YR = Yaw,
PR = Pitch,
RR = Roll,
XA = X axis acceleration,
ZA = Z axis acceleration,
YA = Y axis acceleration,
YRA = Yaw acceleration,
PRA = Pitch acceleration,
RRA = Roll acceleration,
obj = 3D object
```
:::
::::

## get values from main app: 

:::: 
::: 
``` 
obj_Main.M = 3000 MTons,
obj_thruster is parented to obj_main,
obj_thruster.X = 10,
obj_thruster.Z = 20,
obj_thruster.Y = 30, 
obj_thruster.YR = 90,
obj_thruster.PR = 180,
obj_thruster.RR = 270,
Obj_thruster.N.X = 400 MTons
```
:::
::::

## calculate acceleration: 

### Need help finding code to go here 

the calculator gives me

## out put to main app: 

:::: 
::: 
``` 
obj_main.XA,
obj_main.ZA,
obj_main.YA,
obj_main.YRA, 
obj_main.PRA,
obj_main.RRA
```
:::
::::

I will run the calculator once for every thruster on the obj. Add them together and get haw the object moves in space. then do it again and add both to see how fast the obj is moving now. And where it has moved to. this way I can set the obj to travel though space in a realistic way not this unrealistic follow the path key framed fashion.

I have tried to find to find the formulas need to due this for days. I\'m new to python but the program i\'m trying to right this plugin for just started using python and it is simple enough for me to work with. Please please help.

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help]() page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
