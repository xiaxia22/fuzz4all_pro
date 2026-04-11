# Class Menu

**Source:** `java.desktop\java\awt\Menu.html`

### Class Description

```java
public class
Menu

extends
MenuItem

implements
MenuContainer
,
Accessible
```

A

Menu

object is a pull-down menu component
that is deployed from a menu bar.

A menu can optionally be a

tear-off

menu. A tear-off menu
can be opened and dragged away from its parent menu bar or menu.
It remains on the screen after the mouse button has been released.
The mechanism for tearing off a menu is platform dependent, since
the look and feel of the tear-off menu is determined by its peer.
On platforms that do not support tear-off menus, the tear-off
property is ignored.

Each item in a menu must belong to the

MenuItem

class. It can be an instance of

MenuItem

, a submenu
(an instance of

Menu

), or a check box (an instance of

CheckboxMenuItem

).

**All Implemented Interfaces:** MenuContainer

,

Serializable

,

Accessible

---

### Field Details

*No entries found.*

### Constructor Details

#### public Menu()
throws
HeadlessException

Constructs a new menu with an empty label. This menu is not
a tear-off menu.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.1

---

#### public Menu​(
String
label)
throws
HeadlessException

Constructs a new menu with the specified label. This menu is not
a tear-off menu.

**Parameters:**
- label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public Menu​(
String
label,
boolean tearOff)
throws
HeadlessException

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Parameters:**
- label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.
- tearOff

- if

true

, the menu
is a tear-off menu.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

### Method Details

#### public void addNotify()

Creates the menu's peer. The peer allows us to modify the
appearance of the menu without changing its functionality.

**Overrides:**
- addNotify

in class

MenuItem

---

#### public void removeNotify()

Removes the menu's peer. The peer allows us to modify the appearance
of the menu without changing its functionality.

**Overrides:**
- removeNotify

in class

MenuComponent

---

#### public boolean isTearOff()

Indicates whether this menu is a tear-off menu.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Returns:**
- true

if this is a tear-off menu;

false

otherwise.

---

#### public int getItemCount()

Get the number of items in this menu.

**Returns:**
- the number of items in this menu

**Since:**
- 1.1

---

#### @Deprecated

public int countItems()

Returns the number of items in this menu.

**Returns:**
- the number of items in this menu

---

#### public
MenuItem
getItem​(int index)

Gets the item located at the specified index of this menu.

**Parameters:**
- index

- the position of the item to be returned.

**Returns:**
- the item located at the specified index.

---

#### public
MenuItem
add​(
MenuItem
mi)

Adds the specified menu item to this menu. If the
menu item has been part of another menu, removes it
from that menu.

**Parameters:**
- mi

- the menu item to be added

**Returns:**
- the menu item added

**See Also:**
- insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

---

#### public void add​(
String
label)

Adds an item with the specified label to this menu.

**Parameters:**
- label

- the text on the item

**See Also:**
- insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

---

#### public void insert​(
MenuItem
menuitem,
int index)

Inserts a menu item into this menu
at the specified position.

**Parameters:**
- menuitem

- the menu item to be inserted.
- index

- the position at which the menu
item should be inserted.

**Throws:**
- IllegalArgumentException

- if the value of

index

is less than zero

**See Also:**
- add(java.lang.String)

,

add(java.awt.MenuItem)

**Since:**
- 1.1

---

#### public void insert​(
String
label,
int index)

Inserts a menu item with the specified label into this menu
at the specified position. This is a convenience method for

insert(menuItem, index)

.

**Parameters:**
- label

- the text on the item
- index

- the position at which the menu item
should be inserted

**Throws:**
- IllegalArgumentException

- if the value of

index

is less than zero

**See Also:**
- add(java.lang.String)

,

add(java.awt.MenuItem)

**Since:**
- 1.1

---

#### public void addSeparator()

Adds a separator line, or a hypen, to the menu at the current position.

**See Also:**
- insertSeparator(int)

---

#### public void insertSeparator​(int index)

Inserts a separator at the specified position.

**Parameters:**
- index

- the position at which the
menu separator should be inserted.

**Throws:**
- IllegalArgumentException

- if the value of

index

is less than 0.

**See Also:**
- addSeparator()

**Since:**
- 1.1

---

#### public void remove​(int index)

Removes the menu item at the specified index from this menu.

**Parameters:**
- index

- the position of the item to be removed.

---

#### public void remove​(
MenuComponent
item)

Removes the specified menu item from this menu.

**Specified by:**
- remove

in interface

MenuContainer

**Parameters:**
- item

- the item to be removed from the menu.
If

item

is

null

or is not in this menu, this method does
nothing.

---

#### public void removeAll()

Removes all items from this menu.

**Since:**
- 1.1

---

#### public
String
paramString()

Returns a string representing the state of this

Menu

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

MenuItem

**Returns:**
- the parameter string of this menu

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this Menu.
For menus, the AccessibleContext takes the form of an
AccessibleAWTMenu.
A new AccessibleAWTMenu instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

MenuItem

**Returns:**
- an AccessibleAWTMenu that serves as the
AccessibleContext of this Menu

**Since:**
- 1.3

---

### Additional Sections

#### Class Menu

java.lang.Object

- java.awt.MenuComponent
- - java.awt.MenuItem
- - java.awt.Menu

java.awt.MenuComponent

- java.awt.MenuItem
- - java.awt.Menu

java.awt.MenuItem

- java.awt.Menu

java.awt.Menu

**All Implemented Interfaces:** MenuContainer

,

Serializable

,

Accessible

**Direct Known Subclasses:** PopupMenu

```java
public class
Menu

extends
MenuItem

implements
MenuContainer
,
Accessible
```

A

Menu

object is a pull-down menu component
that is deployed from a menu bar.

A menu can optionally be a

tear-off

menu. A tear-off menu
can be opened and dragged away from its parent menu bar or menu.
It remains on the screen after the mouse button has been released.
The mechanism for tearing off a menu is platform dependent, since
the look and feel of the tear-off menu is determined by its peer.
On platforms that do not support tear-off menus, the tear-off
property is ignored.

Each item in a menu must belong to the

MenuItem

class. It can be an instance of

MenuItem

, a submenu
(an instance of

Menu

), or a check box (an instance of

CheckboxMenuItem

).

**Since:** 1.0
**See Also:** MenuItem

,

CheckboxMenuItem

,

Serialized Form

public class

Menu

extends

MenuItem

implements

MenuContainer

,

Accessible

A

Menu

object is a pull-down menu component
that is deployed from a menu bar.

A menu can optionally be a

tear-off

menu. A tear-off menu
can be opened and dragged away from its parent menu bar or menu.
It remains on the screen after the mouse button has been released.
The mechanism for tearing off a menu is platform dependent, since
the look and feel of the tear-off menu is determined by its peer.
On platforms that do not support tear-off menus, the tear-off
property is ignored.

Each item in a menu must belong to the

MenuItem

class. It can be an instance of

MenuItem

, a submenu
(an instance of

Menu

), or a check box (an instance of

CheckboxMenuItem

).

A menu can optionally be a

tear-off

menu. A tear-off menu
can be opened and dragged away from its parent menu bar or menu.
It remains on the screen after the mouse button has been released.
The mechanism for tearing off a menu is platform dependent, since
the look and feel of the tear-off menu is determined by its peer.
On platforms that do not support tear-off menus, the tear-off
property is ignored.

Each item in a menu must belong to the

MenuItem

class. It can be an instance of

MenuItem

, a submenu
(an instance of

Menu

), or a check box (an instance of

CheckboxMenuItem

).

Each item in a menu must belong to the

MenuItem

class. It can be an instance of

MenuItem

, a submenu
(an instance of

Menu

), or a check box (an instance of

CheckboxMenuItem

).

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Menu.AccessibleAWTMenu

Inner class of Menu used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

MenuItem

MenuItem.AccessibleAWTMenuItem

- Nested classes/interfaces declared in class java.awt.

MenuComponent

MenuComponent.AccessibleAWTMenuComponent

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Menu

()

Constructs a new menu with an empty label.

Menu

​(

String

label)

Constructs a new menu with the specified label.

Menu

​(

String

label,
boolean tearOff)

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

MenuItem

add

​(

MenuItem

mi)

Adds the specified menu item to this menu.

void

add

​(

String

label)

Adds an item with the specified label to this menu.

void

addNotify

()

Creates the menu's peer.

void

addSeparator

()

Adds a separator line, or a hypen, to the menu at the current position.

int

countItems

()

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Menu.

MenuItem

getItem

​(int index)

Gets the item located at the specified index of this menu.

int

getItemCount

()

Get the number of items in this menu.

void

insert

​(

MenuItem

menuitem,
int index)

Inserts a menu item into this menu
at the specified position.

void

insert

​(

String

label,
int index)

Inserts a menu item with the specified label into this menu
at the specified position.

void

insertSeparator

​(int index)

Inserts a separator at the specified position.

boolean

isTearOff

()

Indicates whether this menu is a tear-off menu.

String

paramString

()

Returns a string representing the state of this

Menu

.

void

remove

​(int index)

Removes the menu item at the specified index from this menu.

void

remove

​(

MenuComponent

item)

Removes the specified menu item from this menu.

void

removeAll

()

Removes all items from this menu.

void

removeNotify

()

Removes the menu's peer.

- Methods declared in class java.awt.

MenuItem

addActionListener

,

deleteShortcut

,

disable

,

disableEvents

,

enable

,

enable

,

enableEvents

,

getActionCommand

,

getActionListeners

,

getLabel

,

getListeners

,

getShortcut

,

isEnabled

,

processActionEvent

,

processEvent

,

removeActionListener

,

setActionCommand

,

setEnabled

,

setLabel

,

setShortcut

- Methods declared in class java.awt.

MenuComponent

dispatchEvent

,

getFont

,

getName

,

getParent

,

getTreeLock

,

postEvent

,

setFont

,

setName

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.awt.

MenuContainer

getFont

,

postEvent

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Menu.AccessibleAWTMenu

Inner class of Menu used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

MenuItem

MenuItem.AccessibleAWTMenuItem

- Nested classes/interfaces declared in class java.awt.

MenuComponent

MenuComponent.AccessibleAWTMenuComponent

---

#### Nested Class Summary

Inner class of Menu used to provide default support for
accessibility.

Nested classes/interfaces declared in class java.awt.

MenuItem

MenuItem.AccessibleAWTMenuItem

---

#### Nested classes/interfaces declared in class java.awt. MenuItem

Nested classes/interfaces declared in class java.awt.

MenuComponent

MenuComponent.AccessibleAWTMenuComponent

---

#### Nested classes/interfaces declared in class java.awt. MenuComponent

Constructor Summary

Constructors

Constructor

Description

Menu

()

Constructs a new menu with an empty label.

Menu

​(

String

label)

Constructs a new menu with the specified label.

Menu

​(

String

label,
boolean tearOff)

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

---

#### Constructor Summary

Constructs a new menu with an empty label.

Constructs a new menu with the specified label.

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

MenuItem

add

​(

MenuItem

mi)

Adds the specified menu item to this menu.

void

add

​(

String

label)

Adds an item with the specified label to this menu.

void

addNotify

()

Creates the menu's peer.

void

addSeparator

()

Adds a separator line, or a hypen, to the menu at the current position.

int

countItems

()

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Menu.

MenuItem

getItem

​(int index)

Gets the item located at the specified index of this menu.

int

getItemCount

()

Get the number of items in this menu.

void

insert

​(

MenuItem

menuitem,
int index)

Inserts a menu item into this menu
at the specified position.

void

insert

​(

String

label,
int index)

Inserts a menu item with the specified label into this menu
at the specified position.

void

insertSeparator

​(int index)

Inserts a separator at the specified position.

boolean

isTearOff

()

Indicates whether this menu is a tear-off menu.

String

paramString

()

Returns a string representing the state of this

Menu

.

void

remove

​(int index)

Removes the menu item at the specified index from this menu.

void

remove

​(

MenuComponent

item)

Removes the specified menu item from this menu.

void

removeAll

()

Removes all items from this menu.

void

removeNotify

()

Removes the menu's peer.

- Methods declared in class java.awt.

MenuItem

addActionListener

,

deleteShortcut

,

disable

,

disableEvents

,

enable

,

enable

,

enableEvents

,

getActionCommand

,

getActionListeners

,

getLabel

,

getListeners

,

getShortcut

,

isEnabled

,

processActionEvent

,

processEvent

,

removeActionListener

,

setActionCommand

,

setEnabled

,

setLabel

,

setShortcut

- Methods declared in class java.awt.

MenuComponent

dispatchEvent

,

getFont

,

getName

,

getParent

,

getTreeLock

,

postEvent

,

setFont

,

setName

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.awt.

MenuContainer

getFont

,

postEvent

---

#### Method Summary

Adds the specified menu item to this menu.

Adds an item with the specified label to this menu.

Creates the menu's peer.

Adds a separator line, or a hypen, to the menu at the current position.

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Gets the AccessibleContext associated with this Menu.

Gets the item located at the specified index of this menu.

Get the number of items in this menu.

Inserts a menu item into this menu
at the specified position.

Inserts a menu item with the specified label into this menu
at the specified position.

Inserts a separator at the specified position.

Indicates whether this menu is a tear-off menu.

Returns a string representing the state of this

Menu

.

Removes the menu item at the specified index from this menu.

Removes the specified menu item from this menu.

Removes all items from this menu.

Removes the menu's peer.

Methods declared in class java.awt.

MenuItem

addActionListener

,

deleteShortcut

,

disable

,

disableEvents

,

enable

,

enable

,

enableEvents

,

getActionCommand

,

getActionListeners

,

getLabel

,

getListeners

,

getShortcut

,

isEnabled

,

processActionEvent

,

processEvent

,

removeActionListener

,

setActionCommand

,

setEnabled

,

setLabel

,

setShortcut

---

#### Methods declared in class java.awt. MenuItem

Methods declared in class java.awt.

MenuComponent

dispatchEvent

,

getFont

,

getName

,

getParent

,

getTreeLock

,

postEvent

,

setFont

,

setName

,

toString

---

#### Methods declared in class java.awt. MenuComponent

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.awt.

MenuContainer

getFont

,

postEvent

---

#### Methods declared in interface java.awt. MenuContainer

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Menu

```java
public Menu()
throws
HeadlessException
```

Constructs a new menu with an empty label. This menu is not
a tear-off menu.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

- Menu

```java
public Menu​(
String
label)
throws
HeadlessException
```

Constructs a new menu with the specified label. This menu is not
a tear-off menu.

**Parameters:** label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- Menu

```java
public Menu​(
String
label,
boolean tearOff)
throws
HeadlessException
```

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Parameters:** label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.
**Parameters:** tearOff

- if

true

, the menu
is a tear-off menu.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- addNotify

```java
public void addNotify()
```

Creates the menu's peer. The peer allows us to modify the
appearance of the menu without changing its functionality.

**Overrides:** addNotify

in class

MenuItem

- removeNotify

```java
public void removeNotify()
```

Removes the menu's peer. The peer allows us to modify the appearance
of the menu without changing its functionality.

**Overrides:** removeNotify

in class

MenuComponent

- isTearOff

```java
public boolean isTearOff()
```

Indicates whether this menu is a tear-off menu.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Returns:** true

if this is a tear-off menu;

false

otherwise.

- getItemCount

```java
public int getItemCount()
```

Get the number of items in this menu.

**Returns:** the number of items in this menu
**Since:** 1.1

- countItems

```java
@Deprecated

public int countItems()
```

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Returns the number of items in this menu.

**Returns:** the number of items in this menu

- getItem

```java
public
MenuItem
getItem​(int index)
```

Gets the item located at the specified index of this menu.

**Parameters:** index

- the position of the item to be returned.
**Returns:** the item located at the specified index.

- add

```java
public
MenuItem
add​(
MenuItem
mi)
```

Adds the specified menu item to this menu. If the
menu item has been part of another menu, removes it
from that menu.

**Parameters:** mi

- the menu item to be added
**Returns:** the menu item added
**See Also:** insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

- add

```java
public void add​(
String
label)
```

Adds an item with the specified label to this menu.

**Parameters:** label

- the text on the item
**See Also:** insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

- insert

```java
public void insert​(
MenuItem
menuitem,
int index)
```

Inserts a menu item into this menu
at the specified position.

**Parameters:** menuitem

- the menu item to be inserted.
**Parameters:** index

- the position at which the menu
item should be inserted.
**Throws:** IllegalArgumentException

- if the value of

index

is less than zero
**Since:** 1.1
**See Also:** add(java.lang.String)

,

add(java.awt.MenuItem)

- insert

```java
public void insert​(
String
label,
int index)
```

Inserts a menu item with the specified label into this menu
at the specified position. This is a convenience method for

insert(menuItem, index)

.

**Parameters:** label

- the text on the item
**Parameters:** index

- the position at which the menu item
should be inserted
**Throws:** IllegalArgumentException

- if the value of

index

is less than zero
**Since:** 1.1
**See Also:** add(java.lang.String)

,

add(java.awt.MenuItem)

- addSeparator

```java
public void addSeparator()
```

Adds a separator line, or a hypen, to the menu at the current position.

**See Also:** insertSeparator(int)

- insertSeparator

```java
public void insertSeparator​(int index)
```

Inserts a separator at the specified position.

**Parameters:** index

- the position at which the
menu separator should be inserted.
**Throws:** IllegalArgumentException

- if the value of

index

is less than 0.
**Since:** 1.1
**See Also:** addSeparator()

- remove

```java
public void remove​(int index)
```

Removes the menu item at the specified index from this menu.

**Parameters:** index

- the position of the item to be removed.

- remove

```java
public void remove​(
MenuComponent
item)
```

Removes the specified menu item from this menu.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** item

- the item to be removed from the menu.
If

item

is

null

or is not in this menu, this method does
nothing.

- removeAll

```java
public void removeAll()
```

Removes all items from this menu.

**Since:** 1.1

- paramString

```java
public
String
paramString()
```

Returns a string representing the state of this

Menu

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

MenuItem
**Returns:** the parameter string of this menu

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Menu.
For menus, the AccessibleContext takes the form of an
AccessibleAWTMenu.
A new AccessibleAWTMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

MenuItem
**Returns:** an AccessibleAWTMenu that serves as the
AccessibleContext of this Menu
**Since:** 1.3

Constructor Detail

- Menu

```java
public Menu()
throws
HeadlessException
```

Constructs a new menu with an empty label. This menu is not
a tear-off menu.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

- Menu

```java
public Menu​(
String
label)
throws
HeadlessException
```

Constructs a new menu with the specified label. This menu is not
a tear-off menu.

**Parameters:** label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- Menu

```java
public Menu​(
String
label,
boolean tearOff)
throws
HeadlessException
```

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Parameters:** label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.
**Parameters:** tearOff

- if

true

, the menu
is a tear-off menu.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

Menu

```java
public Menu()
throws
HeadlessException
```

Constructs a new menu with an empty label. This menu is not
a tear-off menu.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Menu

public Menu()
throws

HeadlessException

Constructs a new menu with an empty label. This menu is not
a tear-off menu.

Menu

```java
public Menu​(
String
label)
throws
HeadlessException
```

Constructs a new menu with the specified label. This menu is not
a tear-off menu.

**Parameters:** label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Menu

public Menu​(

String

label)
throws

HeadlessException

Constructs a new menu with the specified label. This menu is not
a tear-off menu.

Menu

```java
public Menu​(
String
label,
boolean tearOff)
throws
HeadlessException
```

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Parameters:** label

- the menu's label in the menu bar, or in
another menu of which this menu is a submenu.
**Parameters:** tearOff

- if

true

, the menu
is a tear-off menu.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Menu

public Menu​(

String

label,
boolean tearOff)
throws

HeadlessException

Constructs a new menu with the specified label,
indicating whether the menu can be torn off.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

Method Detail

- addNotify

```java
public void addNotify()
```

Creates the menu's peer. The peer allows us to modify the
appearance of the menu without changing its functionality.

**Overrides:** addNotify

in class

MenuItem

- removeNotify

```java
public void removeNotify()
```

Removes the menu's peer. The peer allows us to modify the appearance
of the menu without changing its functionality.

**Overrides:** removeNotify

in class

MenuComponent

- isTearOff

```java
public boolean isTearOff()
```

Indicates whether this menu is a tear-off menu.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Returns:** true

if this is a tear-off menu;

false

otherwise.

- getItemCount

```java
public int getItemCount()
```

Get the number of items in this menu.

**Returns:** the number of items in this menu
**Since:** 1.1

- countItems

```java
@Deprecated

public int countItems()
```

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Returns the number of items in this menu.

**Returns:** the number of items in this menu

- getItem

```java
public
MenuItem
getItem​(int index)
```

Gets the item located at the specified index of this menu.

**Parameters:** index

- the position of the item to be returned.
**Returns:** the item located at the specified index.

- add

```java
public
MenuItem
add​(
MenuItem
mi)
```

Adds the specified menu item to this menu. If the
menu item has been part of another menu, removes it
from that menu.

**Parameters:** mi

- the menu item to be added
**Returns:** the menu item added
**See Also:** insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

- add

```java
public void add​(
String
label)
```

Adds an item with the specified label to this menu.

**Parameters:** label

- the text on the item
**See Also:** insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

- insert

```java
public void insert​(
MenuItem
menuitem,
int index)
```

Inserts a menu item into this menu
at the specified position.

**Parameters:** menuitem

- the menu item to be inserted.
**Parameters:** index

- the position at which the menu
item should be inserted.
**Throws:** IllegalArgumentException

- if the value of

index

is less than zero
**Since:** 1.1
**See Also:** add(java.lang.String)

,

add(java.awt.MenuItem)

- insert

```java
public void insert​(
String
label,
int index)
```

Inserts a menu item with the specified label into this menu
at the specified position. This is a convenience method for

insert(menuItem, index)

.

**Parameters:** label

- the text on the item
**Parameters:** index

- the position at which the menu item
should be inserted
**Throws:** IllegalArgumentException

- if the value of

index

is less than zero
**Since:** 1.1
**See Also:** add(java.lang.String)

,

add(java.awt.MenuItem)

- addSeparator

```java
public void addSeparator()
```

Adds a separator line, or a hypen, to the menu at the current position.

**See Also:** insertSeparator(int)

- insertSeparator

```java
public void insertSeparator​(int index)
```

Inserts a separator at the specified position.

**Parameters:** index

- the position at which the
menu separator should be inserted.
**Throws:** IllegalArgumentException

- if the value of

index

is less than 0.
**Since:** 1.1
**See Also:** addSeparator()

- remove

```java
public void remove​(int index)
```

Removes the menu item at the specified index from this menu.

**Parameters:** index

- the position of the item to be removed.

- remove

```java
public void remove​(
MenuComponent
item)
```

Removes the specified menu item from this menu.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** item

- the item to be removed from the menu.
If

item

is

null

or is not in this menu, this method does
nothing.

- removeAll

```java
public void removeAll()
```

Removes all items from this menu.

**Since:** 1.1

- paramString

```java
public
String
paramString()
```

Returns a string representing the state of this

Menu

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

MenuItem
**Returns:** the parameter string of this menu

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Menu.
For menus, the AccessibleContext takes the form of an
AccessibleAWTMenu.
A new AccessibleAWTMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

MenuItem
**Returns:** an AccessibleAWTMenu that serves as the
AccessibleContext of this Menu
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Creates the menu's peer. The peer allows us to modify the
appearance of the menu without changing its functionality.

**Overrides:** addNotify

in class

MenuItem

---

#### addNotify

public void addNotify()

Creates the menu's peer. The peer allows us to modify the
appearance of the menu without changing its functionality.

removeNotify

```java
public void removeNotify()
```

Removes the menu's peer. The peer allows us to modify the appearance
of the menu without changing its functionality.

**Overrides:** removeNotify

in class

MenuComponent

---

#### removeNotify

public void removeNotify()

Removes the menu's peer. The peer allows us to modify the appearance
of the menu without changing its functionality.

isTearOff

```java
public boolean isTearOff()
```

Indicates whether this menu is a tear-off menu.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

**Returns:** true

if this is a tear-off menu;

false

otherwise.

---

#### isTearOff

public boolean isTearOff()

Indicates whether this menu is a tear-off menu.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

Tear-off functionality may not be supported by all
implementations of AWT. If a particular implementation doesn't
support tear-off menus, this value is silently ignored.

getItemCount

```java
public int getItemCount()
```

Get the number of items in this menu.

**Returns:** the number of items in this menu
**Since:** 1.1

---

#### getItemCount

public int getItemCount()

Get the number of items in this menu.

countItems

```java
@Deprecated

public int countItems()
```

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Returns the number of items in this menu.

**Returns:** the number of items in this menu

---

#### countItems

@Deprecated

public int countItems()

Returns the number of items in this menu.

getItem

```java
public
MenuItem
getItem​(int index)
```

Gets the item located at the specified index of this menu.

**Parameters:** index

- the position of the item to be returned.
**Returns:** the item located at the specified index.

---

#### getItem

public

MenuItem

getItem​(int index)

Gets the item located at the specified index of this menu.

add

```java
public
MenuItem
add​(
MenuItem
mi)
```

Adds the specified menu item to this menu. If the
menu item has been part of another menu, removes it
from that menu.

**Parameters:** mi

- the menu item to be added
**Returns:** the menu item added
**See Also:** insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

---

#### add

public

MenuItem

add​(

MenuItem

mi)

Adds the specified menu item to this menu. If the
menu item has been part of another menu, removes it
from that menu.

add

```java
public void add​(
String
label)
```

Adds an item with the specified label to this menu.

**Parameters:** label

- the text on the item
**See Also:** insert(java.lang.String, int)

,

insert(java.awt.MenuItem, int)

---

#### add

public void add​(

String

label)

Adds an item with the specified label to this menu.

insert

```java
public void insert​(
MenuItem
menuitem,
int index)
```

Inserts a menu item into this menu
at the specified position.

**Parameters:** menuitem

- the menu item to be inserted.
**Parameters:** index

- the position at which the menu
item should be inserted.
**Throws:** IllegalArgumentException

- if the value of

index

is less than zero
**Since:** 1.1
**See Also:** add(java.lang.String)

,

add(java.awt.MenuItem)

---

#### insert

public void insert​(

MenuItem

menuitem,
int index)

Inserts a menu item into this menu
at the specified position.

insert

```java
public void insert​(
String
label,
int index)
```

Inserts a menu item with the specified label into this menu
at the specified position. This is a convenience method for

insert(menuItem, index)

.

**Parameters:** label

- the text on the item
**Parameters:** index

- the position at which the menu item
should be inserted
**Throws:** IllegalArgumentException

- if the value of

index

is less than zero
**Since:** 1.1
**See Also:** add(java.lang.String)

,

add(java.awt.MenuItem)

---

#### insert

public void insert​(

String

label,
int index)

Inserts a menu item with the specified label into this menu
at the specified position. This is a convenience method for

insert(menuItem, index)

.

addSeparator

```java
public void addSeparator()
```

Adds a separator line, or a hypen, to the menu at the current position.

**See Also:** insertSeparator(int)

---

#### addSeparator

public void addSeparator()

Adds a separator line, or a hypen, to the menu at the current position.

insertSeparator

```java
public void insertSeparator​(int index)
```

Inserts a separator at the specified position.

**Parameters:** index

- the position at which the
menu separator should be inserted.
**Throws:** IllegalArgumentException

- if the value of

index

is less than 0.
**Since:** 1.1
**See Also:** addSeparator()

---

#### insertSeparator

public void insertSeparator​(int index)

Inserts a separator at the specified position.

remove

```java
public void remove​(int index)
```

Removes the menu item at the specified index from this menu.

**Parameters:** index

- the position of the item to be removed.

---

#### remove

public void remove​(int index)

Removes the menu item at the specified index from this menu.

remove

```java
public void remove​(
MenuComponent
item)
```

Removes the specified menu item from this menu.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** item

- the item to be removed from the menu.
If

item

is

null

or is not in this menu, this method does
nothing.

---

#### remove

public void remove​(

MenuComponent

item)

Removes the specified menu item from this menu.

removeAll

```java
public void removeAll()
```

Removes all items from this menu.

**Since:** 1.1

---

#### removeAll

public void removeAll()

Removes all items from this menu.

paramString

```java
public
String
paramString()
```

Returns a string representing the state of this

Menu

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

MenuItem
**Returns:** the parameter string of this menu

---

#### paramString

public

String

paramString()

Returns a string representing the state of this

Menu

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Menu.
For menus, the AccessibleContext takes the form of an
AccessibleAWTMenu.
A new AccessibleAWTMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

MenuItem
**Returns:** an AccessibleAWTMenu that serves as the
AccessibleContext of this Menu
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this Menu.
For menus, the AccessibleContext takes the form of an
AccessibleAWTMenu.
A new AccessibleAWTMenu instance is created if necessary.

---

