# MacPython/VoodooPad/Terminology

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

*([FileMaker](./FileMaker.html) Pro.app terminology, generated from /Applications/Development/FileMaker Pro 6/FileMaker Pro.app)*

::: {}
  -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Suites**     [URL Suite](./MacPython(2f)VoodooPad(2f)Terminology.html#suite_URL_Suite) [Subset of the Core, Table, and Database suites](./MacPython(2f)VoodooPad(2f)Terminology.html#suite_Subset_of_the_Core_Table_and_Database_suites) [FileMaker Suite](./MacPython(2f)VoodooPad(2f)Terminology.html#suite_FileMaker_Suite)
  **Commands**   [begin_transaction](./MacPython(2f)VoodooPad(2f)Terminology.html#command_begin_transaction) [class_info](./MacPython(2f)VoodooPad(2f)Terminology.html#command_class_info) [close](./MacPython(2f)VoodooPad(2f)Terminology.html#command_close) [copy](./MacPython(2f)VoodooPad(2f)Terminology.html#command_copy) [count](./MacPython(2f)VoodooPad(2f)Terminology.html#command_count) [create](./MacPython(2f)VoodooPad(2f)Terminology.html#command_create) [cut](./MacPython(2f)VoodooPad(2f)Terminology.html#command_cut) [data_size](./MacPython(2f)VoodooPad(2f)Terminology.html#command_data_size) [delete](./MacPython(2f)VoodooPad(2f)Terminology.html#command_delete) [do_menu](./MacPython(2f)VoodooPad(2f)Terminology.html#command_do_menu) [do_script](./MacPython(2f)VoodooPad(2f)Terminology.html#command_do_script) [duplicate](./MacPython(2f)VoodooPad(2f)Terminology.html#command_duplicate) [end_transaction](./MacPython(2f)VoodooPad(2f)Terminology.html#command_end_transaction) [event_info](./MacPython(2f)VoodooPad(2f)Terminology.html#command_event_info) [exists](./MacPython(2f)VoodooPad(2f)Terminology.html#command_exists) [find](./MacPython(2f)VoodooPad(2f)Terminology.html#command_find) [get_data](./MacPython(2f)VoodooPad(2f)Terminology.html#command_get_data) [get_remote_URL](./MacPython(2f)VoodooPad(2f)Terminology.html#command_get_remote_URL) [getURL](./MacPython(2f)VoodooPad(2f)Terminology.html#command_getURL) [go_to](./MacPython(2f)VoodooPad(2f)Terminology.html#command_go_to) [open](./MacPython(2f)VoodooPad(2f)Terminology.html#command_open) [paste](./MacPython(2f)VoodooPad(2f)Terminology.html#command_paste) [print\_](./MacPython(2f)VoodooPad(2f)Terminology.html#command_print_) [quit](./MacPython(2f)VoodooPad(2f)Terminology.html#command_quit) [redo](./MacPython(2f)VoodooPad(2f)Terminology.html#command_redo) [save](./MacPython(2f)VoodooPad(2f)Terminology.html#command_save) [set_data](./MacPython(2f)VoodooPad(2f)Terminology.html#command_set_data) [show](./MacPython(2f)VoodooPad(2f)Terminology.html#command_show) [sort](./MacPython(2f)VoodooPad(2f)Terminology.html#command_sort) [undo](./MacPython(2f)VoodooPad(2f)Terminology.html#command_undo)
  **Classes**    [application](./MacPython(2f)VoodooPad(2f)Terminology.html#class_application) [cell](./MacPython(2f)VoodooPad(2f)Terminology.html#class_cell) [database](./MacPython(2f)VoodooPad(2f)Terminology.html#class_database) [document](./MacPython(2f)VoodooPad(2f)Terminology.html#class_document) [field](./MacPython(2f)VoodooPad(2f)Terminology.html#class_field) [FileMaker_script](./MacPython(2f)VoodooPad(2f)Terminology.html#class_FileMaker_script) [layout](./MacPython(2f)VoodooPad(2f)Terminology.html#class_layout) [menu](./MacPython(2f)VoodooPad(2f)Terminology.html#class_menu) [menu_item](./MacPython(2f)VoodooPad(2f)Terminology.html#class_menu_item) [record](./MacPython(2f)VoodooPad(2f)Terminology.html#class_record) [request](./MacPython(2f)VoodooPad(2f)Terminology.html#class_request) [window](./MacPython(2f)VoodooPad(2f)Terminology.html#class_window)
  -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

## URL Suite 

Standard Suite for Uniform Resource Locators

### Commands 

- **application.getURL(\...)** \-- Open a [FileMaker](./FileMaker.html) Pro database using a URL specification\

  - *Text* \-- The URL specification for the [FileMaker](./FileMaker.html) Pro database in the form \"FMP5://\[host\]/filename\"\
    Result: *None*

## Subset of the Core, Table, and Database suites 

Subset of Events supported by other Applications

### Commands 

- **application.begin_transaction()** \-- Begin a transaction\

  - Result: *SInt32* \-- The transaction ID

  **application.class_info(\...)** \-- Get information about an object class\

  - \[*Type*\] \-- The object class about which information is requested\
    \[**in\_**=*[IntlWritingCode](./IntlWritingCode.html)*\] \-- The human language and script system in which to return information\
    Result: *[ClassInfo](./ClassInfo.html)* \-- A record containing the object&#8217;s properties and elements

  **reference.close()** \-- Close an object\

  - Result: *None*

  **application.copy()** \-- Copy an object to the clipboard\

  - Result: *None*

  **reference.count(\...)** \-- Return the number of elements of a particular class within an object\

  - **class\_**=*Type* \-- The class of the elements to be counted\
    Result: *SInt32* \-- The number of elements

  **application.create(\...)** \-- Create a new element\

  - **new**=*Type* \-- The class of the new element\
    \[**at**=*[InsertionLoc](./InsertionLoc.html)*\] \-- The location at which to insert the element\
    \[**with_data**=*Anything*\] \-- The initial data for the element\
    \[**with_properties**=*AERecord*\] \-- The initial data for the properties of the element\
    Result: *[ObjectSpecifier](./ObjectSpecifier.html)* \-- To the new object(s)

  **application.cut()** \-- Cut an object to the clipboard\

  - Result: *None*

  **reference.data_size(\...)** \-- Return the size in bytes of an object\

  - \[**as**=*Type*\] \-- The data type for which the size is calculated\
    Result: *SInt32* \-- The size of the object in bytes

  **reference.delete()** \-- Delete an element from an object\

  - Result: *None*

  **application.do_menu(\...)** \-- Execute a menu command\

  - *Anything* \-- This denotes both the menu ID and the menu item\
    \[**menu_named**=*Text*\] \-- The name of the menu item\
    Result: *Anything* \-- Result of menu selection

  **application.do_script(\...)** \-- Execute a script\

  - *Text* \-- The name or specifier of the [FileMaker](./FileMaker.html) script to be executed\
    Result: *Anything* \-- The result of the Script

  **reference.duplicate(\...)** \-- Duplicate an object\

  - \[**to**=*[InsertionLoc](./InsertionLoc.html)*\] \-- The new location for the object\
    Result: *[ObjectSpecifier](./ObjectSpecifier.html)* \-- To the duplicated object(s)

  **application.end_transaction()** \-- End a transaction\

  - Result: *None*

  **application.event_info(\...)** \-- Get information about the Apple events in a suite\

  - *Type* \-- The event class of the Apple events for which to return information\
    \[**in\_**=*[IntlWritingCode](./IntlWritingCode.html)*\] \-- The human language and script system in which to return information\
    Result: *list of [EventInfo](./EventInfo.html)* \-- A record containing the events and their parameters

  **reference.exists()** \-- Tell if an object exists\

  - Result: *Boolean* \-- True if it exists, false if not

  **reference.get_data(\...)** \-- Get the data for an object\

  - \[**as**=*list of Type*\] \-- The desired types for the data, in order of preference\
    Result: *Anything*

  **reference.open(\...)** \-- Open an object\

  - \[**with_password**=*Text*\] \-- The password to use\
    Result: *None*

  **application.paste()** \-- Paste an object from the clipboard\

  - Result: *None*

  **reference.print\_()** \-- Print an object\

  - Result: *None*

  **application.quit()** \-- Perform tasks before termination, then terminate\

  - Result: *None*

  **application.redo()** \-- Reverse the action of the immediately preceding undo\

  - Result: *None*

  **reference.save()** \-- Save an object\

  - Result: *None*

  **reference.set_data(\...)** \-- Set an object\'s data\

  - **to**=*Anything* \-- The new value\
    Result: *None*

  **reference.show()** \-- Bring an object into view\

  - Result: *None*

  **reference.sort(\...)** \-- Sort the records in a layout\

  - \[**by**=*[ObjectSpecifier](./ObjectSpecifier.html)*\] \-- The fields to sort by\
    \[**in_order**=*k.ascending \| k.descending \| k.custom*\] \-- The sort type\
    Result: *None*

  **application.undo()** \-- Undo the action of the previous event or user interaction\

  - Result: *None*

### Classes 

- **application** \-- The application

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **frontmost** (r/o) *Boolean* \-- Is this the frontmost application?\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the application\
      **version** (r/o) *Version* \-- The version of the application\

    Elements:
    - **[documents](./MacPython(2f)VoodooPad(2f)Terminology.html#class_document)** \-- *index \| name*\
      **[windows](./MacPython(2f)VoodooPad(2f)Terminology.html#class_window)** \-- *index \| name*\
      **[menus](./MacPython(2f)VoodooPad(2f)Terminology.html#class_menu)** \-- *name \| index*\

  **window** \-- A [FileMaker](./FileMaker.html) Pro document window

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the window\
      **bounds** *QDRectangle* \-- The bounding rectangle of the window\
      **visible** *Boolean* \-- Is the window visible?\
      **index** (r/o) *SInt32* \-- The number of the window\
      **floating** (r/o) *Boolean* \-- Does the window float?\
      **zoomable** (r/o) *Boolean* \-- Is the window zoomable?\
      **zoomed** *Boolean* \-- Is the window zoomed?\
      **modal** (r/o) *Boolean* \-- Is the window modal?\
      **resizable** (r/o) *Boolean* \-- Is the window resizable?\
      **has_close_box** (r/o) *Boolean* \-- Does the window have a close box?\
      **has_title_bar** (r/o) *Boolean* \-- Does the window have a title bar?\

    Elements:
    - **[documents](./MacPython(2f)VoodooPad(2f)Terminology.html#class_document)** \-- *name \| index*\
      **[FileMaker_scripts](./MacPython(2f)VoodooPad(2f)Terminology.html#class_FileMaker_script)** \-- *name \| index \| relative \| range \| test \| id*\
      **[databases](./MacPython(2f)VoodooPad(2f)Terminology.html#class_database)** \-- *name \| index*\

  **document** \-- A [FileMaker](./FileMaker.html) Pro document

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the document\
      **modified** (r/o) *Boolean* \-- True if the document has been modified\

    Elements:
    - **[windows](./MacPython(2f)VoodooPad(2f)Terminology.html#class_window)** \-- *index \| name*\
      **[databases](./MacPython(2f)VoodooPad(2f)Terminology.html#class_database)** \-- *name \| index*\
      **[FileMaker_scripts](./MacPython(2f)VoodooPad(2f)Terminology.html#class_FileMaker_script)** \-- *name \| index \| relative \| range \| test \| id*\

  **database** \-- A [FileMaker](./FileMaker.html) Pro database

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the database\
      **lock** (r/o) *k.unlocked \| k.shared_lock \| k.exclusive_lock* \-- The current session\'s lock on the database\
      **current_layout** *[ObjectSpecifier](./ObjectSpecifier.html)* \-- The current layout\
      **current_record** *[ObjectSpecifier](./ObjectSpecifier.html)* \-- The current record\
      **access** (r/o) *k.no_access \| k.read \| k.write \| k.update \| k.create \| k.delete \| k.read_write \| k.read_update \| k.read_create \| k.read_delete \| k.write_update \| k.write_create \| k.write_delete \| k.update_create \| k.update_delete \| k.write_delete \| k.read_write_update \| k.read_write_create \| k.read_write_delete \| k.write_update_create \| k.write_update_delete \| k.update_create_delete \| k.read_create_delete \| k.read_update_delete \| k.write_create_delete \| k.read_update_create \| k.no_delete \| k.no_create \| k.no_update \| k.no_read \| k.no_write \| k.full* \-- The access privileges\
      **multiuser** *Boolean* \-- If true, users have access to the database over the network\

    Elements:
    - **[layouts](./MacPython(2f)VoodooPad(2f)Terminology.html#class_layout)** \-- *name \| index \| relative \| range \| test \| id*\
      **[FileMaker_scripts](./MacPython(2f)VoodooPad(2f)Terminology.html#class_FileMaker_script)** \-- *name \| index \| relative \| range \| test \| id*\

  **[FileMaker](./FileMaker.html)\_script** \-- A [FileMaker](./FileMaker.html) script

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the [FileMaker](./FileMaker.html) Script\
      **ID** (r/o) *[LongFloat](./LongFloat.html)* \-- The unique ID of the [FileMaker](./FileMaker.html) Script\

  **layout** \-- A [FileMaker](./FileMaker.html) Pro layout

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the layout\
      **ID** (r/o) *[LongFloat](./LongFloat.html)* \-- The unique ID of the layout\
      **access** (r/o) *k.no_access \| k.read \| k.write \| k.update \| k.create \| k.delete \| k.read_write \| k.read_update \| k.read_create \| k.read_delete \| k.write_update \| k.write_create \| k.write_delete \| k.update_create \| k.update_delete \| k.write_delete \| k.read_write_update \| k.read_write_create \| k.read_write_delete \| k.write_update_create \| k.write_update_delete \| k.update_create_delete \| k.read_create_delete \| k.read_update_delete \| k.write_create_delete \| k.read_update_create \| k.no_delete \| k.no_create \| k.no_update \| k.no_read \| k.no_write \| k.full* \-- The access privileges of the layout\
      **protection** (r/o) *k.read_only \| k.formulas_protected \| k.read_write* \-- Indicates whether the formulas of the cells in the layout can be changed\
      **lock** (r/o) *k.unlocked \| k.shared_lock \| k.exclusive_lock* \-- The lock on the layout\
      **kind** (r/o) *k.table \| k.view* \-- The kind of layout (View = [FileMaker](./FileMaker.html) Pro layout, table = all fields i.e. layout 0)\
      **visible** (r/o) *Boolean* \-- Is the layout visible in the layouts menu?\

    Elements:
    - **[fields](./MacPython(2f)VoodooPad(2f)Terminology.html#class_field)** \-- *name \| index \| relative \| range \| test \| id*\
      **[records](./MacPython(2f)VoodooPad(2f)Terminology.html#class_record)** \-- *name \| index \| relative \| range \| test \| id*\
      **[cells](./MacPython(2f)VoodooPad(2f)Terminology.html#class_cell)** \-- *name \| index \| relative \| range \| test \| id*\
      **[requests](./MacPython(2f)VoodooPad(2f)Terminology.html#class_request)** \-- *name \| index \| relative \| range \| test \| id*\

  **field** \-- A [FileMaker](./FileMaker.html) Pro field

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **choices** (r/o) *AEList* \-- The value list for the field\
      **access** (r/o) *k.no_access \| k.read \| k.write \| k.update \| k.create \| k.delete \| k.read_write \| k.read_update \| k.read_create \| k.read_delete \| k.write_update \| k.write_create \| k.write_delete \| k.update_create \| k.update_delete \| k.write_delete \| k.read_write_update \| k.read_write_create \| k.read_write_delete \| k.write_update_create \| k.write_update_delete \| k.update_create_delete \| k.read_create_delete \| k.read_update_delete \| k.write_create_delete \| k.read_update_create \| k.no_delete \| k.no_create \| k.no_update \| k.no_read \| k.no_write \| k.full* \-- The access privileges for the field\
      **formula** (r/o) *Text* \-- The field\'s calculation formula\
      **ID** (r/o) *[LongFloat](./LongFloat.html)* \-- The unique ID of the field\
      **lock** (r/o) *k.unlocked \| k.shared_lock \| k.exclusive_lock* \-- The lock status of the field\
      **name** (r/o) *Text* \-- The name of the field\
      **nulls_OK** (r/o) *Boolean* \-- Is this field allowed to be empty?\
      **protection** (r/o) *k.read_only \| k.formulas_protected \| k.read_write* \-- The protection of this field\
      **repeats** (r/o) *Enumeration* \-- Is this a repeating field?\
      **repeat_size** (r/o) *SInt32* \-- Maximum number of repetitions of the field\
      **unique_value** (r/o) *Boolean* \-- Must this field contain unique values?\
      **globalValue** (r/o) *Boolean* \-- Is this field a global field?\

    Elements:
    - **[cells](./MacPython(2f)VoodooPad(2f)Terminology.html#class_cell)** \-- *name \| index \| relative \| range \| test \| id*\

  **record** \-- A [FileMaker](./FileMaker.html) Pro record

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the record\
      **ID** (r/o) *[LongFloat](./LongFloat.html)* \-- The unique ID of the record\
      **lock** (r/o) *k.unlocked \| k.shared_lock \| k.exclusive_lock* \-- The lock for the record\
      **protection** (r/o) *k.read_only \| k.formulas_protected \| k.read_write* \-- Indicates whether the formulas of the cells in the record can be changed\
      **access** (r/o) *k.no_access \| k.read \| k.write \| k.update \| k.create \| k.delete \| k.read_write \| k.read_update \| k.read_create \| k.read_delete \| k.write_update \| k.write_create \| k.write_delete \| k.update_create \| k.update_delete \| k.write_delete \| k.read_write_update \| k.read_write_create \| k.read_write_delete \| k.write_update_create \| k.write_update_delete \| k.update_create_delete \| k.read_create_delete \| k.read_update_delete \| k.write_create_delete \| k.read_update_create \| k.no_delete \| k.no_create \| k.no_update \| k.no_read \| k.no_write \| k.full* \-- Indicates the access privileges for the record\

    Elements:
    - **[cells](./MacPython(2f)VoodooPad(2f)Terminology.html#class_cell)** \-- *name \| index \| relative \| range \| test \| id*\

  **cell** \-- A field value in a record or request

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **choices** (r/o) *AEList* \-- The value list for the cell\
      **formula** (r/o) *Text* \-- The cell\'s calculation formula\
      **lock** (r/o) *k.unlocked \| k.shared_lock \| k.exclusive_lock* \-- The lock status of the cell\
      **name** (r/o) *Text* \-- The cell\'s name\
      **protection** (r/o) *k.read_only \| k.formulas_protected \| k.read_write* \-- The protection of this cell\
      **cellValue** *Text* \-- The cell value\
      **ID** (r/o) *AEList* \-- The unique ID of the cell (the first element is the record ID, the second element is the cell ID)\
      **repeat_size** (r/o) *SInt32* \-- Number of repetitions of the cell\
      **globalValue** (r/o) *Boolean* \-- Is this cell a global cell?\

## FileMaker Suite 

[FileMaker](./FileMaker.html) Pro-specific events and objects

### Commands 

- **reference.go_to()** \-- Go to an object\

  - Result: *None*

  **reference.find()** \-- Perform a [FileMaker](./FileMaker.html) Pro Find given current requests\

  - Result: *None*

  **application.get_remote_URL()** \-- Opens a hosted [FileMaker](./FileMaker.html) Pro database\

  - Result: *Text* \-- The URL specification for the opened database in the form \"FMP5://\[host\]/filename\"

### Classes 

- **request** \-- A [FileMaker](./FileMaker.html) Pro find request

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** (r/o) *[IntlText](./IntlText.html)* \-- The name of the find request\
      **ID** (r/o) *[LongFloat](./LongFloat.html)* \-- The unique ID of the find request\
      **omitted** *Boolean* \-- True if the request is to be omitted\

    Elements:
    - **[cells](./MacPython(2f)VoodooPad(2f)Terminology.html#class_cell)** \-- *name \| index \| relative \| range \| test \| id*\

  **menu_item** \-- A menu item

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** *[IntlText](./IntlText.html)* \-- The name of the menu item\
      **ID** *SInt32* \-- The unique ID of the menu item\
      **enabled** *Boolean* \-- Is the menu item enabled?\
      **item_number** (r/o) *[ShortInteger](./ShortInteger.html)* \-- The menu item number\
      **checked** *Boolean* \-- Is the menu item checked?\
      **notify_address** *TargetID* \-- The target ID\

  **menu** \-- A menu

  - Properties:
    - **best_type** (r/o) *Type* \-- The best descriptor type\
      **class\_** (r/o) *Type* \-- The class\
      **default_type** (r/o) *Type* \-- The default descriptor type\
      **name** *[IntlText](./IntlText.html)* \-- The name of the menu\
      **ID** (r/o) *[ShortInteger](./ShortInteger.html)* \-- The resource ID of the menu\
      **enabled** *Boolean* \-- Is the menu enabled?\

    Elements:
    - **[menu_items](./MacPython(2f)VoodooPad(2f)Terminology.html#class_menu_item)** \-- *index \| name*\
      **[menus](./MacPython(2f)VoodooPad(2f)Terminology.html#class_menu)** \-- *index \| name*\
