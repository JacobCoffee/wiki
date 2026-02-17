# WebsiteRedesignProposal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Development of python.org Website to promote and inform about python 

**Note:** This proposal was funded and completed. See [PythonWebsite](PythonWebsite) for information on ongoing content and tool development for the python.org website.

The python website development started approximately a year ago. Over the period of the last year there has been significant input from Python users, advocates and board members which has resulted in the following deliverables

         1. Logo
            
         2. Website design
            
         3. Website Template Build
            
         4. An initial information architecture
            
         5. An implementation plan

The site has been built as XHTML 1.0 Transitional using CSS Positioning techniques. This is widely accepted best practise for reasons of usability, accessibility and forward compatibility. It also ensures that pages are small and hence the site is quick. A final advantage is that, if desired, the site can be re-skinned without replacing the HTML and hence without rebuilding the templating system. The site design can be seen as built and tested HTML at www.pythonworld.com (there have been some changes since it was tested across browsers so compatibility may be lacking, full cross browser testing of this template will take place and any problems fixed).

The current state of the project has been inspected and given verbal approval by Steve Holden and has no outstanding issues held against it. The next stage of the project is to develop the following components

           1. The templating system (prototype nearly complete)
            
           2. Final information architecture
            
           3. A set of conversion modules that will allow changes made to the
               current content to be kept largely in sync until such time as
               the site is deemed ready to launch.

This step needs some intensive effort which we (myself and Matt Goodall) will undertake. Unfortunately we estimate that it would take approximately three weeks for two people to complete and we think this would take more than four months to do in our spare time (even that presumes that our company doesn\'t place too many demands on us).

We are proposing to contribute one month of work and we ask the Python grant fund to provide the other one month at Pollenation\'s cost rate.

This would work out as 4,000 GBP. If this is possible we would look to complete the work during February/March

Our company\'s payment terms are typically 50% initial payment. 50% on delivery. Our deliverables would be

         1. Final testing of the website HTML/CSS to ensure cross browser
             compatibility and accessibility
            
         2. a completed templating system - a nevow/yaml/rest command line
             driven system of generating a html website. (initial template
             data - http://pythonworld.com/resources).
            
         3. set of modules that implements over 90% of the current Python
             website - It is desired that the website content be dynamically
             converted from existing ht files. This will ensure that any
             revisions that take place between the start of the project and
             the site launch will be included. A framework will be built that
             reads the ht files and generated YAML content in a format
             suitable for the templating system. For ht content that is not
             in a 'typical' format, custom modules will be added to the
             framework.

Because the templating system is driven from plain text files, which contain a combination of YAML data and ReST blocks, the site will be simple to edit with command line tools. It is expected that a standalone webserver be included with the svn repository such that editors may run the website on their own computers before committing any changes.

The modules will also provides a simple to use framework under which existing content which doesn\'t currently integrate into the existing site framework, may be repurposed. We will also provide templates under which dynamically generated content (pypi, python wiki) can be included in the new design.

It goes without saying that just as our current work has been made without expected recompense, once the project is complete we would continue to work at the framework and commit ourselves to supporting an administration server that would host the templating and content system. It is expected that the flat html files that the systems generated will remain hosted at it\'s current location.

Although the work will be completed as a collaboration between our developers, each developer will have a main responsibility. Matt Goodall (one of the two main Nevow developers) will be creating the templating system. Tim Parkin will be working on the content storage framework and any modifications needed on the [PyYaml](./PyYaml.html) module (which is currently maintained by Pollenation Internet). Certain pages will require additional templates building in order to accommodate their different layouts; these templates will be provided by Pollenation.

Pollenation would like to have a small credit in the footer (which would help enormously - the text \'web design\' in a small font in the footer with a link to our website would be more than adequate. It could appear alongside the hosting credits - a small icon would be sufficient if text is unacceptable). This credit would help use continue in business and enable our business to continue offering web support for the Python site.

Yours sincerely

Tim Parkin

Managing Director

------------------------------------------------------------------------

# APPENDIX - Details of YAML page generation 

The following is a draft example of how the YAML template data files would look. The example is based on the home page of the site and is consequently more complex than typical pages would be. This does demonstrate the flexibility of the proposed system however.

    ---
    # Type of template to use
    template: standard

    # Page components
    contents:  { meta: +meta.yml, topnav: +topnav.yml, nav: +nav.yml, main: _homepage }

    # variables references above
    vars:
      homepage:   { content: [ _title, _photos, _sidebars, _intro, _news ] }
      title:     'The Official Home of the Python Programmming Language'
      photos:     +photos.yml
      sidebars: [ +sidebar_using-python-for.yml, +sidebar_python-projects.yml ]
      intro:      +intro.rst
      news:       +news.rst

The standard template contains \'holes\' labelled \'meta\',\'topnav\',\'nav\' and \'main\'. Where a yaml file appears, it is used to file the \'hole\'. For example, the \'nav\' yml file looks like this

    ---
    # Type of template to use
    template: navigation

    # Contents of the template
    contents: 
      # Main Navigation
      main-navigation :
      - [ABOUT, about]
      - [NEWS, news]
      - [DOCUMENTATION, docs]
      - [DOWNLOAD, download]
      - [COMMUNITY, community]
      - [DEVELOPERS, dev]
      - [LINKS, links]
     
      # Additional to make certain sections default open
      open-navigation: [about]

      # Quick links for navigation
      quick-links:
        documentation:
          - [languages, docs/lang]
          - [libraries, docs/libraries]
          - [modules, docs/modules]
          - [more, docs]
        downloads:
          - [python-2.3.tar.bz2, ftp/python/2.3/python-2.3.tar.bz2]
          - [python-2.3.exe, ftp/python/2.3/python-2.3.exe]
          - [more, downloads]

It can be seen that it is simple to add a new top level navigation item or quick link. The template has to have some knowledge of how it is to be rendered (to understand a list of links or a group of lists of links, as in the quick links case: or that \'open-navigation\' refers to the \'main-navigation\' and what it means.

A typical page would not have to include the navigation section as it can be inherited from it\'s parent; This is also true for the meta and topnav elements. The only important items are the contents (which can be just a ReST file) and optionally the sidebar (which may be a table of contents, possibly auto generated from the document itself).

From this it can be seen that to generate a new page is as simple as generating a new directory, copying an index.yml, changing the contents mapping to include a \'main: +main.rst\' and adding a ReST document named \'main.rst\'.

    -- 
    Tim Parkin, Pollenation Internet Ltd
    e: tim at pollenation dot net   w: http://www.pollenation.net 
    t: +44 (0)113 2252500    m: +44 (0)7980 594768
    f: +44 (0)845 2802368
