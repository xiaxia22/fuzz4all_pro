# Class MenuBar

**Source:** `java.desktop\java\awt\MenuBar.html`

### Class Description

```java
public class
MenuBar

extends
MenuComponent

implements
MenuContainer
,
Accessible
```

The

MenuBar

class encapsulates the platform's
concept of a menu bar bound to a frame. In order to associate
the menu bar with a

Frame

object, call the
frame's

setMenuBar

method.

target for cross references

This is what a menu bar might look like:

A menu bar handles keyboard shortcuts for menu items, passing them
along to its child menus.
(Keyboard shortcuts, which are optional, provide the user with
an alternative to the mouse for invoking a menu item and the
action that is associated with it.)
Each menu item can maintain an instance of

MenuShortcut

.
The

MenuBar

class defines several methods,

shortcuts()

and

getShortcutMenuItem(java.awt.MenuShortcut)

that retrieve information about the shortcuts a given
menu bar is managing.

**All Implemented Interfaces:** MenuContainer

,

Serializable

,

Accessible

---

### Field Details

*No entries found.*

### Constructor Details

#### public MenuBar()
throws
HeadlessException

Creates a new menu bar.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

### Method Details

#### public void addNotify()

Creates the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

---

#### public void removeNotify()

Removes the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

**Overrides:**
- removeNotify

in class

MenuComponent

---

#### public
Menu
getHelpMenu()

Gets the help menu on the menu bar.

**Returns:**
- the help menu on this menu bar.

---

#### public void setHelpMenu​(
Menu
m)

Sets the specified menu to be this menu bar's help menu.
If this menu bar has an existing help menu, the old help menu is
removed from the menu bar, and replaced with the specified menu.

**Parameters:**
- m

- the menu to be set as the help menu

---

#### public
Menu
add​(
Menu
m)

Adds the specified menu to the menu bar.
If the menu has been part of another menu bar,
removes it from that menu bar.

**Parameters:**
- m

- the menu to be added

**Returns:**
- the menu added

**See Also:**
- remove(int)

,

remove(java.awt.MenuComponent)

---

#### public void remove​(int index)

Removes the menu located at the specified
index from this menu bar.

**Parameters:**
- index

- the position of the menu to be removed.

**See Also:**
- add(java.awt.Menu)

---

#### public void remove​(
MenuComponent
m)

Removes the specified menu component from this menu bar.

**Specified by:**
- remove

in interface

MenuContainer

**Parameters:**
- m

- the menu component to be removed.

**See Also:**
- add(java.awt.Menu)

---

#### public int getMenuCount()

Gets the number of menus on the menu bar.

**Returns:**
- the number of menus on the menu bar.

**Since:**
- 1.1

---

#### @Deprecated

public int countMenus()

Gets the number of menus on the menu bar.

**Returns:**
- the number of menus on the menu bar.

---

#### public
Menu
getMenu​(int i)

Gets the specified menu.

**Parameters:**
- i

- the index position of the menu to be returned.

**Returns:**
- the menu at the specified index of this menu bar.

---

#### public
Enumeration
<
MenuShortcut
> shortcuts()

Gets an enumeration of all menu shortcuts this menu bar
is managing.

**Returns:**
- an enumeration of menu shortcuts that this
menu bar is managing.

**See Also:**
- MenuShortcut

**Since:**
- 1.1

---

#### public
MenuItem
getShortcutMenuItem​(
MenuShortcut
s)

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

**Parameters:**
- s

- the specified menu shortcut.

**Returns:**
- the menu item for the specified shortcut.

**See Also:**
- MenuItem

,

MenuShortcut

**Since:**
- 1.1

---

#### public void deleteShortcut​(
MenuShortcut
s)

Deletes the specified menu shortcut.

**Parameters:**
- s

- the menu shortcut to delete.

**Since:**
- 1.1

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this MenuBar.
For menu bars, the AccessibleContext takes the form of an
AccessibleAWTMenuBar.
A new AccessibleAWTMenuBar instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

MenuComponent

**Returns:**
- an AccessibleAWTMenuBar that serves as the
AccessibleContext of this MenuBar

**Since:**
- 1.3

---

### Additional Sections

#### Class MenuBar

java.lang.Object

- java.awt.MenuComponent
- - java.awt.MenuBar

java.awt.MenuComponent

- java.awt.MenuBar

java.awt.MenuBar

**All Implemented Interfaces:** MenuContainer

,

Serializable

,

Accessible

```java
public class
MenuBar

extends
MenuComponent

implements
MenuContainer
,
Accessible
```

The

MenuBar

class encapsulates the platform's
concept of a menu bar bound to a frame. In order to associate
the menu bar with a

Frame

object, call the
frame's

setMenuBar

method.

target for cross references

This is what a menu bar might look like:

A menu bar handles keyboard shortcuts for menu items, passing them
along to its child menus.
(Keyboard shortcuts, which are optional, provide the user with
an alternative to the mouse for invoking a menu item and the
action that is associated with it.)
Each menu item can maintain an instance of

MenuShortcut

.
The

MenuBar

class defines several methods,

shortcuts()

and

getShortcutMenuItem(java.awt.MenuShortcut)

that retrieve information about the shortcuts a given
menu bar is managing.

**Since:** 1.0
**See Also:** Frame

,

Frame.setMenuBar(java.awt.MenuBar)

,

Menu

,

MenuItem

,

MenuShortcut

,

Serialized Form

public class

MenuBar

extends

MenuComponent

implements

MenuContainer

,

Accessible

The

MenuBar

class encapsulates the platform's
concept of a menu bar bound to a frame. In order to associate
the menu bar with a

Frame

object, call the
frame's

setMenuBar

method.

target for cross references

This is what a menu bar might look like:

A menu bar handles keyboard shortcuts for menu items, passing them
along to its child menus.
(Keyboard shortcuts, which are optional, provide the user with
an alternative to the mouse for invoking a menu item and the
action that is associated with it.)
Each menu item can maintain an instance of

MenuShortcut

.
The

MenuBar

class defines several methods,

shortcuts()

and

getShortcutMenuItem(java.awt.MenuShortcut)

that retrieve information about the shortcuts a given
menu bar is managing.

target for cross references

This is what a menu bar might look like:

A menu bar handles keyboard shortcuts for menu items, passing them
along to its child menus.
(Keyboard shortcuts, which are optional, provide the user with
an alternative to the mouse for invoking a menu item and the
action that is associated with it.)
Each menu item can maintain an instance of

MenuShortcut

.
The

MenuBar

class defines several methods,

shortcuts()

and

getShortcutMenuItem(java.awt.MenuShortcut)

that retrieve information about the shortcuts a given
menu bar is managing.

A menu bar handles keyboard shortcuts for menu items, passing them
along to its child menus.
(Keyboard shortcuts, which are optional, provide the user with
an alternative to the mouse for invoking a menu item and the
action that is associated with it.)
Each menu item can maintain an instance of

MenuShortcut

.
The

MenuBar

class defines several methods,

shortcuts()

and

getShortcutMenuItem(java.awt.MenuShortcut)

that retrieve information about the shortcuts a given
menu bar is managing.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

MenuBar.AccessibleAWTMenuBar

Inner class of MenuBar used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

MenuComponent

MenuComponent.AccessibleAWTMenuComponent

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MenuBar

()

Creates a new menu bar.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Menu

add

​(

Menu

m)

Adds the specified menu to the menu bar.

void

addNotify

()

Creates the menu bar's peer.

int

countMenus

()

Deprecated.

As of JDK version 1.1,
replaced by

getMenuCount()

.

void

deleteShortcut

​(

MenuShortcut

s)

Deletes the specified menu shortcut.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this MenuBar.

Menu

getHelpMenu

()

Gets the help menu on the menu bar.

Menu

getMenu

​(int i)

Gets the specified menu.

int

getMenuCount

()

Gets the number of menus on the menu bar.

MenuItem

getShortcutMenuItem

​(

MenuShortcut

s)

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

void

remove

​(int index)

Removes the menu located at the specified
index from this menu bar.

void

remove

​(

MenuComponent

m)

Removes the specified menu component from this menu bar.

void

removeNotify

()

Removes the menu bar's peer.

void

setHelpMenu

​(

Menu

m)

Sets the specified menu to be this menu bar's help menu.

Enumeration

<

MenuShortcut

>

shortcuts

()

Gets an enumeration of all menu shortcuts this menu bar
is managing.

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

paramString

,

postEvent

,

processEvent

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

MenuBar.AccessibleAWTMenuBar

Inner class of MenuBar used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

MenuComponent

MenuComponent.AccessibleAWTMenuComponent

---

#### Nested Class Summary

Inner class of MenuBar used to provide default support for
accessibility.

Nested classes/interfaces declared in class java.awt.

MenuComponent

MenuComponent.AccessibleAWTMenuComponent

---

#### Nested classes/interfaces declared in class java.awt. MenuComponent

Constructor Summary

Constructors

Constructor

Description

MenuBar

()

Creates a new menu bar.

---

#### Constructor Summary

Creates a new menu bar.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Menu

add

​(

Menu

m)

Adds the specified menu to the menu bar.

void

addNotify

()

Creates the menu bar's peer.

int

countMenus

()

Deprecated.

As of JDK version 1.1,
replaced by

getMenuCount()

.

void

deleteShortcut

​(

MenuShortcut

s)

Deletes the specified menu shortcut.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this MenuBar.

Menu

getHelpMenu

()

Gets the help menu on the menu bar.

Menu

getMenu

​(int i)

Gets the specified menu.

int

getMenuCount

()

Gets the number of menus on the menu bar.

MenuItem

getShortcutMenuItem

​(

MenuShortcut

s)

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

void

remove

​(int index)

Removes the menu located at the specified
index from this menu bar.

void

remove

​(

MenuComponent

m)

Removes the specified menu component from this menu bar.

void

removeNotify

()

Removes the menu bar's peer.

void

setHelpMenu

​(

Menu

m)

Sets the specified menu to be this menu bar's help menu.

Enumeration

<

MenuShortcut

>

shortcuts

()

Gets an enumeration of all menu shortcuts this menu bar
is managing.

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

paramString

,

postEvent

,

processEvent

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

Adds the specified menu to the menu bar.

Creates the menu bar's peer.

Deprecated.

As of JDK version 1.1,
replaced by

getMenuCount()

.

Deletes the specified menu shortcut.

Gets the AccessibleContext associated with this MenuBar.

Gets the help menu on the menu bar.

Gets the specified menu.

Gets the number of menus on the menu bar.

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

Removes the menu located at the specified
index from this menu bar.

Removes the specified menu component from this menu bar.

Removes the menu bar's peer.

Sets the specified menu to be this menu bar's help menu.

Gets an enumeration of all menu shortcuts this menu bar
is managing.

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

paramString

,

postEvent

,

processEvent

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

- MenuBar

```java
public MenuBar()
throws
HeadlessException
```

Creates a new menu bar.

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

Creates the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

- removeNotify

```java
public void removeNotify()
```

Removes the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

**Overrides:** removeNotify

in class

MenuComponent

- getHelpMenu

```java
public
Menu
getHelpMenu()
```

Gets the help menu on the menu bar.

**Returns:** the help menu on this menu bar.

- setHelpMenu

```java
public void setHelpMenu​(
Menu
m)
```

Sets the specified menu to be this menu bar's help menu.
If this menu bar has an existing help menu, the old help menu is
removed from the menu bar, and replaced with the specified menu.

**Parameters:** m

- the menu to be set as the help menu

- add

```java
public
Menu
add​(
Menu
m)
```

Adds the specified menu to the menu bar.
If the menu has been part of another menu bar,
removes it from that menu bar.

**Parameters:** m

- the menu to be added
**Returns:** the menu added
**See Also:** remove(int)

,

remove(java.awt.MenuComponent)

- remove

```java
public void remove​(int index)
```

Removes the menu located at the specified
index from this menu bar.

**Parameters:** index

- the position of the menu to be removed.
**See Also:** add(java.awt.Menu)

- remove

```java
public void remove​(
MenuComponent
m)
```

Removes the specified menu component from this menu bar.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** m

- the menu component to be removed.
**See Also:** add(java.awt.Menu)

- getMenuCount

```java
public int getMenuCount()
```

Gets the number of menus on the menu bar.

**Returns:** the number of menus on the menu bar.
**Since:** 1.1

- countMenus

```java
@Deprecated

public int countMenus()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMenuCount()

.

Gets the number of menus on the menu bar.

**Returns:** the number of menus on the menu bar.

- getMenu

```java
public
Menu
getMenu​(int i)
```

Gets the specified menu.

**Parameters:** i

- the index position of the menu to be returned.
**Returns:** the menu at the specified index of this menu bar.

- shortcuts

```java
public
Enumeration
<
MenuShortcut
> shortcuts()
```

Gets an enumeration of all menu shortcuts this menu bar
is managing.

**Returns:** an enumeration of menu shortcuts that this
menu bar is managing.
**Since:** 1.1
**See Also:** MenuShortcut

- getShortcutMenuItem

```java
public
MenuItem
getShortcutMenuItem​(
MenuShortcut
s)
```

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

**Parameters:** s

- the specified menu shortcut.
**Returns:** the menu item for the specified shortcut.
**Since:** 1.1
**See Also:** MenuItem

,

MenuShortcut

- deleteShortcut

```java
public void deleteShortcut​(
MenuShortcut
s)
```

Deletes the specified menu shortcut.

**Parameters:** s

- the menu shortcut to delete.
**Since:** 1.1

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this MenuBar.
For menu bars, the AccessibleContext takes the form of an
AccessibleAWTMenuBar.
A new AccessibleAWTMenuBar instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

MenuComponent
**Returns:** an AccessibleAWTMenuBar that serves as the
AccessibleContext of this MenuBar
**Since:** 1.3

Constructor Detail

- MenuBar

```java
public MenuBar()
throws
HeadlessException
```

Creates a new menu bar.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

MenuBar

```java
public MenuBar()
throws
HeadlessException
```

Creates a new menu bar.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### MenuBar

public MenuBar()
throws

HeadlessException

Creates a new menu bar.

Method Detail

- addNotify

```java
public void addNotify()
```

Creates the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

- removeNotify

```java
public void removeNotify()
```

Removes the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

**Overrides:** removeNotify

in class

MenuComponent

- getHelpMenu

```java
public
Menu
getHelpMenu()
```

Gets the help menu on the menu bar.

**Returns:** the help menu on this menu bar.

- setHelpMenu

```java
public void setHelpMenu​(
Menu
m)
```

Sets the specified menu to be this menu bar's help menu.
If this menu bar has an existing help menu, the old help menu is
removed from the menu bar, and replaced with the specified menu.

**Parameters:** m

- the menu to be set as the help menu

- add

```java
public
Menu
add​(
Menu
m)
```

Adds the specified menu to the menu bar.
If the menu has been part of another menu bar,
removes it from that menu bar.

**Parameters:** m

- the menu to be added
**Returns:** the menu added
**See Also:** remove(int)

,

remove(java.awt.MenuComponent)

- remove

```java
public void remove​(int index)
```

Removes the menu located at the specified
index from this menu bar.

**Parameters:** index

- the position of the menu to be removed.
**See Also:** add(java.awt.Menu)

- remove

```java
public void remove​(
MenuComponent
m)
```

Removes the specified menu component from this menu bar.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** m

- the menu component to be removed.
**See Also:** add(java.awt.Menu)

- getMenuCount

```java
public int getMenuCount()
```

Gets the number of menus on the menu bar.

**Returns:** the number of menus on the menu bar.
**Since:** 1.1

- countMenus

```java
@Deprecated

public int countMenus()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMenuCount()

.

Gets the number of menus on the menu bar.

**Returns:** the number of menus on the menu bar.

- getMenu

```java
public
Menu
getMenu​(int i)
```

Gets the specified menu.

**Parameters:** i

- the index position of the menu to be returned.
**Returns:** the menu at the specified index of this menu bar.

- shortcuts

```java
public
Enumeration
<
MenuShortcut
> shortcuts()
```

Gets an enumeration of all menu shortcuts this menu bar
is managing.

**Returns:** an enumeration of menu shortcuts that this
menu bar is managing.
**Since:** 1.1
**See Also:** MenuShortcut

- getShortcutMenuItem

```java
public
MenuItem
getShortcutMenuItem​(
MenuShortcut
s)
```

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

**Parameters:** s

- the specified menu shortcut.
**Returns:** the menu item for the specified shortcut.
**Since:** 1.1
**See Also:** MenuItem

,

MenuShortcut

- deleteShortcut

```java
public void deleteShortcut​(
MenuShortcut
s)
```

Deletes the specified menu shortcut.

**Parameters:** s

- the menu shortcut to delete.
**Since:** 1.1

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this MenuBar.
For menu bars, the AccessibleContext takes the form of an
AccessibleAWTMenuBar.
A new AccessibleAWTMenuBar instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

MenuComponent
**Returns:** an AccessibleAWTMenuBar that serves as the
AccessibleContext of this MenuBar
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Creates the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

---

#### addNotify

public void addNotify()

Creates the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

removeNotify

```java
public void removeNotify()
```

Removes the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

**Overrides:** removeNotify

in class

MenuComponent

---

#### removeNotify

public void removeNotify()

Removes the menu bar's peer. The peer allows us to change the
appearance of the menu bar without changing any of the menu bar's
functionality.

getHelpMenu

```java
public
Menu
getHelpMenu()
```

Gets the help menu on the menu bar.

**Returns:** the help menu on this menu bar.

---

#### getHelpMenu

public

Menu

getHelpMenu()

Gets the help menu on the menu bar.

setHelpMenu

```java
public void setHelpMenu​(
Menu
m)
```

Sets the specified menu to be this menu bar's help menu.
If this menu bar has an existing help menu, the old help menu is
removed from the menu bar, and replaced with the specified menu.

**Parameters:** m

- the menu to be set as the help menu

---

#### setHelpMenu

public void setHelpMenu​(

Menu

m)

Sets the specified menu to be this menu bar's help menu.
If this menu bar has an existing help menu, the old help menu is
removed from the menu bar, and replaced with the specified menu.

add

```java
public
Menu
add​(
Menu
m)
```

Adds the specified menu to the menu bar.
If the menu has been part of another menu bar,
removes it from that menu bar.

**Parameters:** m

- the menu to be added
**Returns:** the menu added
**See Also:** remove(int)

,

remove(java.awt.MenuComponent)

---

#### add

public

Menu

add​(

Menu

m)

Adds the specified menu to the menu bar.
If the menu has been part of another menu bar,
removes it from that menu bar.

remove

```java
public void remove​(int index)
```

Removes the menu located at the specified
index from this menu bar.

**Parameters:** index

- the position of the menu to be removed.
**See Also:** add(java.awt.Menu)

---

#### remove

public void remove​(int index)

Removes the menu located at the specified
index from this menu bar.

remove

```java
public void remove​(
MenuComponent
m)
```

Removes the specified menu component from this menu bar.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** m

- the menu component to be removed.
**See Also:** add(java.awt.Menu)

---

#### remove

public void remove​(

MenuComponent

m)

Removes the specified menu component from this menu bar.

getMenuCount

```java
public int getMenuCount()
```

Gets the number of menus on the menu bar.

**Returns:** the number of menus on the menu bar.
**Since:** 1.1

---

#### getMenuCount

public int getMenuCount()

Gets the number of menus on the menu bar.

countMenus

```java
@Deprecated

public int countMenus()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMenuCount()

.

Gets the number of menus on the menu bar.

**Returns:** the number of menus on the menu bar.

---

#### countMenus

@Deprecated

public int countMenus()

Gets the number of menus on the menu bar.

getMenu

```java
public
Menu
getMenu​(int i)
```

Gets the specified menu.

**Parameters:** i

- the index position of the menu to be returned.
**Returns:** the menu at the specified index of this menu bar.

---

#### getMenu

public

Menu

getMenu​(int i)

Gets the specified menu.

shortcuts

```java
public
Enumeration
<
MenuShortcut
> shortcuts()
```

Gets an enumeration of all menu shortcuts this menu bar
is managing.

**Returns:** an enumeration of menu shortcuts that this
menu bar is managing.
**Since:** 1.1
**See Also:** MenuShortcut

---

#### shortcuts

public

Enumeration

<

MenuShortcut

> shortcuts()

Gets an enumeration of all menu shortcuts this menu bar
is managing.

getShortcutMenuItem

```java
public
MenuItem
getShortcutMenuItem​(
MenuShortcut
s)
```

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

**Parameters:** s

- the specified menu shortcut.
**Returns:** the menu item for the specified shortcut.
**Since:** 1.1
**See Also:** MenuItem

,

MenuShortcut

---

#### getShortcutMenuItem

public

MenuItem

getShortcutMenuItem​(

MenuShortcut

s)

Gets the instance of

MenuItem

associated
with the specified

MenuShortcut

object,
or

null

if none of the menu items being managed
by this menu bar is associated with the specified menu
shortcut.

deleteShortcut

```java
public void deleteShortcut​(
MenuShortcut
s)
```

Deletes the specified menu shortcut.

**Parameters:** s

- the menu shortcut to delete.
**Since:** 1.1

---

#### deleteShortcut

public void deleteShortcut​(

MenuShortcut

s)

Deletes the specified menu shortcut.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this MenuBar.
For menu bars, the AccessibleContext takes the form of an
AccessibleAWTMenuBar.
A new AccessibleAWTMenuBar instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

MenuComponent
**Returns:** an AccessibleAWTMenuBar that serves as the
AccessibleContext of this MenuBar
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this MenuBar.
For menu bars, the AccessibleContext takes the form of an
AccessibleAWTMenuBar.
A new AccessibleAWTMenuBar instance is created if necessary.

---

