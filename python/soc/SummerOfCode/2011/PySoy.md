# SummerOfCode/2011/PySoy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PySoy Ideas for GSoC 2011 

The best way to get started is to join \#[PySoy](PySoy) on irc.freenode.net. [ArcRiley](ArcRiley) is also available via email to answer questions directly.

These ideas are starting points only, one of the team members can help you get the current code installed and walk you through how a specific component works so you can draft a more complete proposal (or think of a completely different one).

Remember that applicants are required to commit code to be eligible for acceptance, though this may be after their application is submitted. The contributed code need not be in the same area as their proposal would have them working in.

## Texture Manipulation 

We plan to use GEGL (GIMP\'s backend) with a Pythonic frontend to allow for real-time texture manipulation. This should allow adding visible damage in response to collisions, allow players to edit skins and icons within games, and modifying bump maps.

This involves working primarily with GEGL.

## Enhanced Scenes 

Write a collection of enhanced scene types which allow for different play styles without excessive setup. For example, a 2.5D scene akin to \"\"Little Big Planet\"\" or tiled land scene as would be used for open gaming environments. Each of these new scenes would be a subclass of soy.scenes.Scene.

This may involve working with Orc assembly to write new collision routines.

## Volume and Surface 

Extend our current collision shapes for calculating displacement and surface so that bodies can be made to float or tumble in the wind.

These calculations do not need to be physically accurate, or even realistic, only a rough simulation for game design purposes. Game designers will adjust liquid density, wind speed, the size and shape of objects, etc to get the effect they desire, none of these parameters are based on real world measurements.

This may involve working with Orc assembly language.

## Interactive Widgets 

Build a complete set of themeable interactive widgets for various types of menus, lists, trees, form boxes, chat windows, and selection tools that game designers can use with little additional code.

This involves the introduction of a theme system, which we haven\'t added yet, so a game developer can design a border/color scheme for a game\'s UI and have it work everywhere.

This would involve a good deal of OpenGL, Cairo, and Pango.

## Gyro Controller Input 

Write one or more new controller classes that take input from various gyro controllers, from [WiiMotes](./WiiMotes.html) to Android phones. Most of these devices require working with bluetooth.

The resulting API should allow a game developer to add basic 3d axis support for gyro controllers with only a few lines of code.

This would involve working with the Genie language and potentially Java for a small Android app to turn a phone into a game controller.
