# Class PopupMenu

**Source:** `java.desktop\java\awt\PopupMenu.html`

### Class Description

```java
public class
PopupMenu

extends
Menu
```

A class that implements a menu which can be dynamically popped up
at a specified position within a component.

As the inheritance hierarchy implies, a

PopupMenu

can be used anywhere a

Menu

can be used.
However, if you use a

PopupMenu

like a

Menu

(e.g., you add it to a

MenuBar

), then you

cannot

call

show

on that

PopupMenu

.

**All Implemented Interfaces:** MenuContainer

,

Serializable

,

Accessible

---

### Field Details

*No entries found.*

### Constructor Details

#### public PopupMenu()
throws
HeadlessException

Creates a new popup menu with an empty name.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public PopupMenu​(
String
label)
throws
HeadlessException

Creates a new popup menu with the specified name.

**Parameters:**
- label

- a non-

null

string specifying
the popup menu's label

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

### Method Details

#### public void addNotify()

Creates the popup menu's peer.
The peer allows us to change the appearance of the popup menu without
changing any of the popup menu's functionality.

**Overrides:**
- addNotify

in class

Menu

---

#### public void show​(
Component
origin,
int x,
int y)

Shows the popup menu at the x, y position relative to an origin
component.
The origin component must be contained within the component
hierarchy of the popup menu's parent. Both the origin and the parent
must be showing on the screen for this method to be valid.

If this

PopupMenu

is being used as a

Menu

(i.e., it has a non-

Component

parent),
then you cannot call this method on the

PopupMenu

.

**Parameters:**
- origin

- the component which defines the coordinate space
- x

- the x coordinate position to popup the menu
- y

- the y coordinate position to popup the menu

**Throws:**
- NullPointerException

- if the parent is

null
- IllegalArgumentException

- if this

PopupMenu

has a non-

Component

parent
- IllegalArgumentException

- if the origin is not in the
parent's hierarchy
- RuntimeException

- if the parent is not showing on screen

---

#### public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with this

PopupMenu

.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Menu

**Returns:**
- the

AccessibleContext

of this

PopupMenu

**Since:**
- 1.3

---

### Additional Sections

#### Class PopupMenu

java.lang.Object

- java.awt.MenuComponent
- - java.awt.MenuItem
- - java.awt.Menu
- - java.awt.PopupMenu

java.awt.MenuComponent

- java.awt.MenuItem
- - java.awt.Menu
- - java.awt.PopupMenu

java.awt.MenuItem

- java.awt.Menu
- - java.awt.PopupMenu

java.awt.Menu

- java.awt.PopupMenu

java.awt.PopupMenu

**All Implemented Interfaces:** MenuContainer

,

Serializable

,

Accessible

```java
public class
PopupMenu

extends
Menu
```

A class that implements a menu which can be dynamically popped up
at a specified position within a component.

As the inheritance hierarchy implies, a

PopupMenu

can be used anywhere a

Menu

can be used.
However, if you use a

PopupMenu

like a

Menu

(e.g., you add it to a

MenuBar

), then you

cannot

call

show

on that

PopupMenu

.

**See Also:** Serialized Form

public class

PopupMenu

extends

Menu

A class that implements a menu which can be dynamically popped up
at a specified position within a component.

As the inheritance hierarchy implies, a

PopupMenu

can be used anywhere a

Menu

can be used.
However, if you use a

PopupMenu

like a

Menu

(e.g., you add it to a

MenuBar

), then you

cannot

call

show

on that

PopupMenu

.

As the inheritance hierarchy implies, a

PopupMenu

can be used anywhere a

Menu

can be used.
However, if you use a

PopupMenu

like a

Menu

(e.g., you add it to a

MenuBar

), then you

cannot

call

show

on that

PopupMenu

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

PopupMenu.AccessibleAWTPopupMenu

Inner class of PopupMenu used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

Menu

Menu.AccessibleAWTMenu

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

PopupMenu

()

Creates a new popup menu with an empty name.

PopupMenu

​(

String

label)

Creates a new popup menu with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addNotify

()

Creates the popup menu's peer.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

PopupMenu

.

void

show

​(

Component

origin,
int x,
int y)

Shows the popup menu at the x, y position relative to an origin
component.

- Methods declared in class java.awt.

Menu

add

,

add

,

addSeparator

,

countItems

,

getItem

,

getItemCount

,

insert

,

insert

,

insertSeparator

,

isTearOff

,

paramString

,

remove

,

remove

,

removeAll

,

removeNotify

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

PopupMenu.AccessibleAWTPopupMenu

Inner class of PopupMenu used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

Menu

Menu.AccessibleAWTMenu

- Nested classes/interfaces declared in class java.awt.

MenuItem

MenuItem.AccessibleAWTMenuItem

- Nested classes/interfaces declared in class java.awt.

MenuComponent

MenuComponent.AccessibleAWTMenuComponent

---

#### Nested Class Summary

Inner class of PopupMenu used to provide default support for
accessibility.

Nested classes/interfaces declared in class java.awt.

Menu

Menu.AccessibleAWTMenu

---

#### Nested classes/interfaces declared in class java.awt. Menu

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

PopupMenu

()

Creates a new popup menu with an empty name.

PopupMenu

​(

String

label)

Creates a new popup menu with the specified name.

---

#### Constructor Summary

Creates a new popup menu with an empty name.

Creates a new popup menu with the specified name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addNotify

()

Creates the popup menu's peer.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

PopupMenu

.

void

show

​(

Component

origin,
int x,
int y)

Shows the popup menu at the x, y position relative to an origin
component.

- Methods declared in class java.awt.

Menu

add

,

add

,

addSeparator

,

countItems

,

getItem

,

getItemCount

,

insert

,

insert

,

insertSeparator

,

isTearOff

,

paramString

,

remove

,

remove

,

removeAll

,

removeNotify

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

Creates the popup menu's peer.

Gets the

AccessibleContext

associated with this

PopupMenu

.

Shows the popup menu at the x, y position relative to an origin
component.

Methods declared in class java.awt.

Menu

add

,

add

,

addSeparator

,

countItems

,

getItem

,

getItemCount

,

insert

,

insert

,

insertSeparator

,

isTearOff

,

paramString

,

remove

,

remove

,

removeAll

,

removeNotify

---

#### Methods declared in class java.awt. Menu

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

- PopupMenu

```java
public PopupMenu()
throws
HeadlessException
```

Creates a new popup menu with an empty name.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- PopupMenu

```java
public PopupMenu​(
String
label)
throws
HeadlessException
```

Creates a new popup menu with the specified name.

**Parameters:** label

- a non-

null

string specifying
the popup menu's label
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

Creates the popup menu's peer.
The peer allows us to change the appearance of the popup menu without
changing any of the popup menu's functionality.

**Overrides:** addNotify

in class

Menu

- show

```java
public void show​(
Component
origin,
int x,
int y)
```

Shows the popup menu at the x, y position relative to an origin
component.
The origin component must be contained within the component
hierarchy of the popup menu's parent. Both the origin and the parent
must be showing on the screen for this method to be valid.

If this

PopupMenu

is being used as a

Menu

(i.e., it has a non-

Component

parent),
then you cannot call this method on the

PopupMenu

.

**Parameters:** origin

- the component which defines the coordinate space
**Parameters:** x

- the x coordinate position to popup the menu
**Parameters:** y

- the y coordinate position to popup the menu
**Throws:** NullPointerException

- if the parent is

null
**Throws:** IllegalArgumentException

- if this

PopupMenu

has a non-

Component

parent
**Throws:** IllegalArgumentException

- if the origin is not in the
parent's hierarchy
**Throws:** RuntimeException

- if the parent is not showing on screen

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

PopupMenu

.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Menu
**Returns:** the

AccessibleContext

of this

PopupMenu
**Since:** 1.3

Constructor Detail

- PopupMenu

```java
public PopupMenu()
throws
HeadlessException
```

Creates a new popup menu with an empty name.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- PopupMenu

```java
public PopupMenu​(
String
label)
throws
HeadlessException
```

Creates a new popup menu with the specified name.

**Parameters:** label

- a non-

null

string specifying
the popup menu's label
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

PopupMenu

```java
public PopupMenu()
throws
HeadlessException
```

Creates a new popup menu with an empty name.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### PopupMenu

public PopupMenu()
throws

HeadlessException

Creates a new popup menu with an empty name.

PopupMenu

```java
public PopupMenu​(
String
label)
throws
HeadlessException
```

Creates a new popup menu with the specified name.

**Parameters:** label

- a non-

null

string specifying
the popup menu's label
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### PopupMenu

public PopupMenu​(

String

label)
throws

HeadlessException

Creates a new popup menu with the specified name.

Method Detail

- addNotify

```java
public void addNotify()
```

Creates the popup menu's peer.
The peer allows us to change the appearance of the popup menu without
changing any of the popup menu's functionality.

**Overrides:** addNotify

in class

Menu

- show

```java
public void show​(
Component
origin,
int x,
int y)
```

Shows the popup menu at the x, y position relative to an origin
component.
The origin component must be contained within the component
hierarchy of the popup menu's parent. Both the origin and the parent
must be showing on the screen for this method to be valid.

If this

PopupMenu

is being used as a

Menu

(i.e., it has a non-

Component

parent),
then you cannot call this method on the

PopupMenu

.

**Parameters:** origin

- the component which defines the coordinate space
**Parameters:** x

- the x coordinate position to popup the menu
**Parameters:** y

- the y coordinate position to popup the menu
**Throws:** NullPointerException

- if the parent is

null
**Throws:** IllegalArgumentException

- if this

PopupMenu

has a non-

Component

parent
**Throws:** IllegalArgumentException

- if the origin is not in the
parent's hierarchy
**Throws:** RuntimeException

- if the parent is not showing on screen

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

PopupMenu

.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Menu
**Returns:** the

AccessibleContext

of this

PopupMenu
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Creates the popup menu's peer.
The peer allows us to change the appearance of the popup menu without
changing any of the popup menu's functionality.

**Overrides:** addNotify

in class

Menu

---

#### addNotify

public void addNotify()

Creates the popup menu's peer.
The peer allows us to change the appearance of the popup menu without
changing any of the popup menu's functionality.

show

```java
public void show​(
Component
origin,
int x,
int y)
```

Shows the popup menu at the x, y position relative to an origin
component.
The origin component must be contained within the component
hierarchy of the popup menu's parent. Both the origin and the parent
must be showing on the screen for this method to be valid.

If this

PopupMenu

is being used as a

Menu

(i.e., it has a non-

Component

parent),
then you cannot call this method on the

PopupMenu

.

**Parameters:** origin

- the component which defines the coordinate space
**Parameters:** x

- the x coordinate position to popup the menu
**Parameters:** y

- the y coordinate position to popup the menu
**Throws:** NullPointerException

- if the parent is

null
**Throws:** IllegalArgumentException

- if this

PopupMenu

has a non-

Component

parent
**Throws:** IllegalArgumentException

- if the origin is not in the
parent's hierarchy
**Throws:** RuntimeException

- if the parent is not showing on screen

---

#### show

public void show​(

Component

origin,
int x,
int y)

Shows the popup menu at the x, y position relative to an origin
component.
The origin component must be contained within the component
hierarchy of the popup menu's parent. Both the origin and the parent
must be showing on the screen for this method to be valid.

If this

PopupMenu

is being used as a

Menu

(i.e., it has a non-

Component

parent),
then you cannot call this method on the

PopupMenu

.

If this

PopupMenu

is being used as a

Menu

(i.e., it has a non-

Component

parent),
then you cannot call this method on the

PopupMenu

.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

PopupMenu

.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Menu
**Returns:** the

AccessibleContext

of this

PopupMenu
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with this

PopupMenu

.

---

