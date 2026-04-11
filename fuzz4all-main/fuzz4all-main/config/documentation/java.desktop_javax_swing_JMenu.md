# Class JMenu

**Source:** `java.desktop\javax\swing\JMenu.html`

### Class Description

```java
@JavaBean
(
description
="A popup window containing menu items displayed in a menu bar.")
public class
JMenu

extends
JMenuItem

implements
Accessible
,
MenuElement
```

An implementation of a menu -- a popup window containing

JMenuItem

s that
is displayed when the user selects an item on the

JMenuBar

.
In addition to

JMenuItem

s, a

JMenu

can
also contain

JSeparator

s.

In essence, a menu is a button with an associated

JPopupMenu

.
When the "button" is pressed, the

JPopupMenu

appears. If the
"button" is on the

JMenuBar

, the menu is a top-level window.
If the "button" is another menu item, then the

JPopupMenu

is
"pull-right" menu.

Menus can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu has many benefits beyond directly
configuring a menu. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For information and examples of using menus see

How to Use Menus

,
a section in

The Java Tutorial.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** ImageObserver

,

ItemSelectable

,

MenuContainer

,

Serializable

,

Accessible

,

MenuElement

,

SwingConstants

---

### Field Details

#### protected
JMenu.WinListener
popupListener

The window-closing listener for the popup.

**See Also:**
- JMenu.WinListener

---

### Constructor Details

#### public JMenu()

Constructs a new

JMenu

with no text.

---

#### public JMenu​(
String
s)

Constructs a new

JMenu

with the supplied string
as its text.

**Parameters:**
- s

- the text for the menu label

---

#### public JMenu​(
Action
a)

Constructs a menu whose properties are taken from the

Action

supplied.

**Parameters:**
- a

- an

Action

**Since:**
- 1.3

---

#### public JMenu​(
String
s,
boolean b)

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

**Parameters:**
- s

- the text for the menu label
- b

- can the menu be torn off (not yet implemented)

---

### Method Details

#### public void updateUI()

Resets the UI property with a value from the current look and feel.

**Overrides:**
- updateUI

in class

JMenuItem

**See Also:**
- JComponent.updateUI()

---

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Returns the name of the L&F class that renders this component.

**Overrides:**
- getUIClassID

in class

JMenuItem

**Returns:**
- the string "MenuUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public void setModel​(
ButtonModel
newModel)

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

**Overrides:**
- setModel

in class

AbstractButton

**Parameters:**
- newModel

- the

ButtonModel

**See Also:**
- AbstractButton.getModel()

---

#### public boolean isSelected()

Returns true if the menu is currently selected (highlighted).

**Overrides:**
- isSelected

in class

AbstractButton

**Returns:**
- true if the menu is selected, else false

---

#### @BeanProperty
(
expert
=true,

hidden
=true,

description
="When the menu is selected, its popup child is shown.")
public void setSelected​(boolean b)

Sets the selection status of the menu.

**Overrides:**
- setSelected

in class

AbstractButton

**Parameters:**
- b

- true to select (highlight) the menu; false to de-select
the menu

---

#### public boolean isPopupMenuVisible()

Returns true if the menu's popup window is visible.

**Returns:**
- true if the menu is visible, else false

---

#### @BeanProperty
(
bound
=false,

expert
=true,

hidden
=true,

description
="The popup menu\'s visibility")
public void setPopupMenuVisible​(boolean b)

Sets the visibility of the menu's popup. If the menu is
not enabled, this method will have no effect.

**Parameters:**
- b

- a boolean value -- true to make the menu visible,
false to hide it

---

#### protected
Point
getPopupMenuOrigin()

Computes the origin for the

JMenu

's popup menu.
This method uses Look and Feel properties named

Menu.menuPopupOffsetX

,

Menu.menuPopupOffsetY

,

Menu.submenuPopupOffsetX

, and

Menu.submenuPopupOffsetY

to adjust the exact location of popup.

**Returns:**
- a

Point

in the coordinate space of the
menu which should be used as the origin
of the

JMenu

's popup menu

**Since:**
- 1.3

---

#### public int getDelay()

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.
Each look and feel (L&F) may determine its own policy for
observing the

delay

property.
In most cases, the delay is not observed for top level menus
or while dragging. The default for

delay

is 0.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Returns:**
- the

delay

property

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The delay between menu selection and making the popup menu visible")
public void setDelay​(int d)

Sets the suggested delay before the menu's

PopupMenu

is popped up or down. Each look and feel (L&F) may determine
it's own policy for observing the delay property. In most cases,
the delay is not observed for top level menus or while dragging.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Parameters:**
- d

- the number of milliseconds to delay

**Throws:**
- IllegalArgumentException

- if

d

is less than 0

---

#### public void setMenuLocation​(int x,
int y)

Sets the location of the popup component.

**Parameters:**
- x

- the x coordinate of the popup's new position
- y

- the y coordinate of the popup's new position

---

#### public
JMenuItem
add​(
JMenuItem
menuItem)

Appends a menu item to the end of this menu.
Returns the menu item added.

**Parameters:**
- menuItem

- the

JMenuitem

to be added

**Returns:**
- the

JMenuItem

added

---

#### public
Component
add​(
Component
c)

Appends a component to the end of this menu.
Returns the component added.

**Overrides:**
- add

in class

Container

**Parameters:**
- c

- the

Component

to add

**Returns:**
- the

Component

added

**See Also:**
- Container.addImpl(java.awt.Component, java.lang.Object, int)

,

Container.invalidate()

,

Container.validate()

,

JComponent.revalidate()

---

#### public
Component
add​(
Component
c,
int index)

Adds the specified component to this container at the given
position. If

index

equals -1, the component will
be appended to the end.

**Overrides:**
- add

in class

Container

**Parameters:**
- c

- the

Component

to add
- index

- the position at which to insert the component

**Returns:**
- the

Component

added

**See Also:**
- remove(javax.swing.JMenuItem)

,

Container.add(Component, int)

---

#### public
JMenuItem
add​(
String
s)

Creates a new menu item with the specified text and appends
it to the end of this menu.

**Parameters:**
- s

- the string for the menu item to be added

**Returns:**
- the new

JMenuItem

---

#### public
JMenuItem
add​(
Action
a)

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

**Parameters:**
- a

- the

Action

for the menu item to be added

**Returns:**
- the new

JMenuItem

**See Also:**
- Action

---

#### protected
JMenuItem
createActionComponent​(
Action
a)

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

**Parameters:**
- a

- the

Action

for the menu item to be added

**Returns:**
- the new menu item

**See Also:**
- Action

**Since:**
- 1.3

---

#### protected
PropertyChangeListener
createActionChangeListener​(
JMenuItem
b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

**Parameters:**
- b

- a menu item for which to create a

PropertyChangeListener

**Returns:**
- a

PropertyChangeListener

for

b

---

#### public void addSeparator()

Appends a new separator to the end of the menu.

---

#### public void insert​(
String
s,
int pos)

Inserts a new menu item with the specified text at a
given position.

**Parameters:**
- s

- the text for the menu item to add
- pos

- an integer specifying the position at which to add the
new menu item

**Throws:**
- IllegalArgumentException

- when the value of

pos

< 0

---

#### public
JMenuItem
insert​(
JMenuItem
mi,
int pos)

Inserts the specified

JMenuitem

at a given position.

**Parameters:**
- mi

- the

JMenuitem

to add
- pos

- an integer specifying the position at which to add the
new

JMenuitem

**Returns:**
- the new menu item

**Throws:**
- IllegalArgumentException

- if the value of

pos

< 0

---

#### public
JMenuItem
insert​(
Action
a,
int pos)

Inserts a new menu item attached to the specified

Action

object at a given position.

**Parameters:**
- a

- the

Action

object for the menu item to add
- pos

- an integer specifying the position at which to add the
new menu item

**Returns:**
- the new menu item

**Throws:**
- IllegalArgumentException

- if the value of

pos

< 0

---

#### public void insertSeparator​(int index)

Inserts a separator at the specified position.

**Parameters:**
- index

- an integer specifying the position at which to
insert the menu separator

**Throws:**
- IllegalArgumentException

- if the value of

index

< 0

---

#### public
JMenuItem
getItem​(int pos)

Returns the

JMenuItem

at the specified position.
If the component at

pos

is not a menu item,

null

is returned.
This method is included for AWT compatibility.

**Parameters:**
- pos

- an integer specifying the position

**Returns:**
- the menu item at the specified position; or

null

if the item as the specified position is not a menu item

**Throws:**
- IllegalArgumentException

- if the value of

pos

< 0

---

#### @BeanProperty
(
bound
=false)
public int getItemCount()

Returns the number of items on the menu, including separators.
This method is included for AWT compatibility.

**Returns:**
- an integer equal to the number of items on the menu

**See Also:**
- getMenuComponentCount()

---

#### @BeanProperty
(
bound
=false)
public boolean isTearOff()

Returns true if the menu can be torn off. This method is not
yet implemented.

**Returns:**
- true if the menu can be torn off, else false

**Throws:**
- Error

- if invoked -- this method is not yet implemented

---

#### public void remove​(
JMenuItem
item)

Removes the specified menu item from this menu. If there is no
popup menu, this method will have no effect.

**Parameters:**
- item

- the

JMenuItem

to be removed from the menu

---

#### public void remove​(int pos)

Removes the menu item at the specified index from this menu.

**Overrides:**
- remove

in class

Container

**Parameters:**
- pos

- the position of the item to be removed

**Throws:**
- IllegalArgumentException

- if the value of

pos

< 0, or if

pos

is greater than the number of menu items

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

---

#### public void remove​(
Component
c)

Removes the component

c

from this menu.

**Overrides:**
- remove

in class

Container

**Parameters:**
- c

- the component to be removed

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

---

#### public void removeAll()

Removes all menu items from this menu.

**Overrides:**
- removeAll

in class

Container

**See Also:**
- Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

---

#### @BeanProperty
(
bound
=false)
public int getMenuComponentCount()

Returns the number of components on the menu.

**Returns:**
- an integer containing the number of components on the menu

---

#### public
Component
getMenuComponent​(int n)

Returns the component at position

n

.

**Parameters:**
- n

- the position of the component to be returned

**Returns:**
- the component requested, or

null

if there is no popup menu

---

#### @BeanProperty
(
bound
=false)
public
Component
[] getMenuComponents()

Returns an array of

Component

s of the menu's
subcomponents. Note that this returns all

Component

s
in the popup menu, including separators.

**Returns:**
- an array of

Component

s or an empty array
if there is no popup menu

---

#### @BeanProperty
(
bound
=false)
public boolean isTopLevelMenu()

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

**Returns:**
- true if the menu is activated from the menu bar;
false if the menu is activated from a menu item
on another menu

---

#### public boolean isMenuComponent​(
Component
c)

Returns true if the specified component exists in the
submenu hierarchy.

**Parameters:**
- c

- the

Component

to be tested

**Returns:**
- true if the

Component

exists, false otherwise

---

#### @BeanProperty
(
bound
=false)
public
JPopupMenu
getPopupMenu()

Returns the popupmenu associated with this menu. If there is
no popupmenu, it will create one.

**Returns:**
- the

JPopupMenu

associated with this menu

---

#### public void addMenuListener​(
MenuListener
l)

Adds a listener for menu events.

**Parameters:**
- l

- the listener to be added

---

#### public void removeMenuListener​(
MenuListener
l)

Removes a listener for menu events.

**Parameters:**
- l

- the listener to be removed

---

#### @BeanProperty
(
bound
=false)
public
MenuListener
[] getMenuListeners()

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

**Returns:**
- all of the

MenuListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireMenuSelected()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:**
- Error

- if there is a

null

listener

**See Also:**
- EventListenerList

---

#### protected void fireMenuDeselected()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:**
- Error

- if there is a

null

listener

**See Also:**
- EventListenerList

---

#### protected void fireMenuCanceled()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:**
- Error

- if there is a

null

listener

**See Also:**
- EventListenerList

---

#### protected
JMenu.WinListener
createWinListener​(
JPopupMenu
p)

Creates a window-closing listener for the popup.

**Parameters:**
- p

- the

JPopupMenu

**Returns:**
- the new window-closing listener

**See Also:**
- JMenu.WinListener

---

#### public void menuSelectionChanged​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu.
Overrides

JMenuItem.menuSelectionChanged

.

**Specified by:**
- menuSelectionChanged

in interface

MenuElement

**Overrides:**
- menuSelectionChanged

in class

JMenuItem

**Parameters:**
- isIncluded

- true if this menu is active, false if
it is not

**See Also:**
- MenuSelectionManager.setSelectedPath(MenuElement[])

---

#### @BeanProperty
(
bound
=false)
public
MenuElement
[] getSubElements()

Returns an array of

MenuElement

s containing the submenu
for this menu component. If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface. Note that since

JSeparator

s do not conform to the

MenuElement

interface, this array will only contain

JMenuItem

s.

**Specified by:**
- getSubElements

in interface

MenuElement

**Overrides:**
- getSubElements

in class

JMenuItem

**Returns:**
- an array of

MenuElement

objects

---

#### public
Component
getComponent()

Returns the

java.awt.Component

used to
paint this

MenuElement

.
The returned component is used to convert events and detect if
an event is inside a menu component.

**Specified by:**
- getComponent

in interface

MenuElement

**Overrides:**
- getComponent

in class

JMenuItem

**Returns:**
- the

Component

that paints this menu item

---

#### public void applyComponentOrientation​(
ComponentOrientation
o)

Sets the

ComponentOrientation

property of this menu
and all components contained within it. This includes all
components returned by

getMenuComponents

.

**Overrides:**
- applyComponentOrientation

in class

Container

**Parameters:**
- o

- the new component orientation of this menu and
the components contained within it.

**Throws:**
- NullPointerException

- if

orientation

is null.

**See Also:**
- Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

**Since:**
- 1.4

---

#### public void setAccelerator​(
KeyStroke
keyStroke)

setAccelerator

is not defined for

JMenu

.
Use

setMnemonic

instead.

**Overrides:**
- setAccelerator

in class

JMenuItem

**Parameters:**
- keyStroke

- the keystroke combination which will invoke
the

JMenuItem

's actionlisteners
without navigating the menu hierarchy

**Throws:**
- Error

- if invoked -- this method is not defined for JMenu.
Use

setMnemonic

instead

---

#### protected void processKeyEvent​(
KeyEvent
evt)

Processes key stroke events such as mnemonics and accelerators.

**Overrides:**
- processKeyEvent

in class

JComponent

**Parameters:**
- evt

- the key event to be processed

**See Also:**
- KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

---

#### public void doClick​(int pressTime)

Programmatically performs a "click". This overrides the method

AbstractButton.doClick

in order to make the menu pop up.

**Overrides:**
- doClick

in class

AbstractButton

**Parameters:**
- pressTime

- indicates the number of milliseconds the
button was pressed for

---

#### protected
String
paramString()

Returns a string representation of this

JMenu

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JMenuItem

**Returns:**
- a string representation of this JMenu.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JMenu.
For JMenus, the AccessibleContext takes the form of an
AccessibleJMenu.
A new AccessibleJMenu instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

JMenuItem

**Returns:**
- an AccessibleJMenu that serves as the
AccessibleContext of this JMenu

---

### Additional Sections

#### Class JMenu

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JMenu

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JMenu

java.awt.Container

- javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JMenu

javax.swing.JComponent

- javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JMenu

javax.swing.AbstractButton

- javax.swing.JMenuItem
- - javax.swing.JMenu

javax.swing.JMenuItem

- javax.swing.JMenu

javax.swing.JMenu

**All Implemented Interfaces:** ImageObserver

,

ItemSelectable

,

MenuContainer

,

Serializable

,

Accessible

,

MenuElement

,

SwingConstants

```java
@JavaBean
(
description
="A popup window containing menu items displayed in a menu bar.")
public class
JMenu

extends
JMenuItem

implements
Accessible
,
MenuElement
```

An implementation of a menu -- a popup window containing

JMenuItem

s that
is displayed when the user selects an item on the

JMenuBar

.
In addition to

JMenuItem

s, a

JMenu

can
also contain

JSeparator

s.

In essence, a menu is a button with an associated

JPopupMenu

.
When the "button" is pressed, the

JPopupMenu

appears. If the
"button" is on the

JMenuBar

, the menu is a top-level window.
If the "button" is another menu item, then the

JPopupMenu

is
"pull-right" menu.

Menus can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu has many benefits beyond directly
configuring a menu. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For information and examples of using menus see

How to Use Menus

,
a section in

The Java Tutorial.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.2
**See Also:** JMenuItem

,

JSeparator

,

JMenuBar

,

JPopupMenu

,

Serialized Form

@JavaBean

(

description

="A popup window containing menu items displayed in a menu bar.")
public class

JMenu

extends

JMenuItem

implements

Accessible

,

MenuElement

An implementation of a menu -- a popup window containing

JMenuItem

s that
is displayed when the user selects an item on the

JMenuBar

.
In addition to

JMenuItem

s, a

JMenu

can
also contain

JSeparator

s.

In essence, a menu is a button with an associated

JPopupMenu

.
When the "button" is pressed, the

JPopupMenu

appears. If the
"button" is on the

JMenuBar

, the menu is a top-level window.
If the "button" is another menu item, then the

JPopupMenu

is
"pull-right" menu.

Menus can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu has many benefits beyond directly
configuring a menu. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For information and examples of using menus see

How to Use Menus

,
a section in

The Java Tutorial.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

In essence, a menu is a button with an associated

JPopupMenu

.
When the "button" is pressed, the

JPopupMenu

appears. If the
"button" is on the

JMenuBar

, the menu is a top-level window.
If the "button" is another menu item, then the

JPopupMenu

is
"pull-right" menu.

Menus can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu has many benefits beyond directly
configuring a menu. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For information and examples of using menus see

How to Use Menus

,
a section in

The Java Tutorial.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Menus can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu has many benefits beyond directly
configuring a menu. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For information and examples of using menus see

How to Use Menus

,
a section in

The Java Tutorial.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

For information and examples of using menus see

How to Use Menus

,
a section in

The Java Tutorial.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JMenu.AccessibleJMenu

This class implements accessibility support for the

JMenu

class.

protected class

JMenu.WinListener

A listener class that watches for a popup window closing.

- Nested classes/interfaces declared in class javax.swing.

JMenuItem

JMenuItem.AccessibleJMenuItem

- Nested classes/interfaces declared in class javax.swing.

AbstractButton

AbstractButton.AccessibleAbstractButton

,

AbstractButton.ButtonChangeListener

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JMenu.WinListener

popupListener

The window-closing listener for the popup.

- Fields declared in class javax.swing.

AbstractButton

actionListener

,

BORDER_PAINTED_CHANGED_PROPERTY

,

changeEvent

,

changeListener

,

CONTENT_AREA_FILLED_CHANGED_PROPERTY

,

DISABLED_ICON_CHANGED_PROPERTY

,

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

,

FOCUS_PAINTED_CHANGED_PROPERTY

,

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

,

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

,

ICON_CHANGED_PROPERTY

,

itemListener

,

MARGIN_CHANGED_PROPERTY

,

MNEMONIC_CHANGED_PROPERTY

,

model

,

MODEL_CHANGED_PROPERTY

,

PRESSED_ICON_CHANGED_PROPERTY

,

ROLLOVER_ENABLED_CHANGED_PROPERTY

,

ROLLOVER_ICON_CHANGED_PROPERTY

,

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

,

SELECTED_ICON_CHANGED_PROPERTY

,

TEXT_CHANGED_PROPERTY

,

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

,

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JMenu

()

Constructs a new

JMenu

with no text.

JMenu

​(

String

s)

Constructs a new

JMenu

with the supplied string
as its text.

JMenu

​(

String

s,
boolean b)

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

JMenu

​(

Action

a)

Constructs a menu whose properties are taken from the

Action

supplied.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Component

add

​(

Component

c)

Appends a component to the end of this menu.

Component

add

​(

Component

c,
int index)

Adds the specified component to this container at the given
position.

JMenuItem

add

​(

String

s)

Creates a new menu item with the specified text and appends
it to the end of this menu.

JMenuItem

add

​(

Action

a)

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

JMenuItem

add

​(

JMenuItem

menuItem)

Appends a menu item to the end of this menu.

void

addMenuListener

​(

MenuListener

l)

Adds a listener for menu events.

void

addSeparator

()

Appends a new separator to the end of the menu.

void

applyComponentOrientation

​(

ComponentOrientation

o)

Sets the

ComponentOrientation

property of this menu
and all components contained within it.

protected

PropertyChangeListener

createActionChangeListener

​(

JMenuItem

b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

protected

JMenuItem

createActionComponent

​(

Action

a)

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

protected

JMenu.WinListener

createWinListener

​(

JPopupMenu

p)

Creates a window-closing listener for the popup.

void

doClick

​(int pressTime)

Programmatically performs a "click".

protected void

fireMenuCanceled

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireMenuDeselected

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireMenuSelected

()

Notifies all listeners that have registered interest for
notification on this event type.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JMenu.

Component

getComponent

()

Returns the

java.awt.Component

used to
paint this

MenuElement

.

int

getDelay

()

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.

JMenuItem

getItem

​(int pos)

Returns the

JMenuItem

at the specified position.

int

getItemCount

()

Returns the number of items on the menu, including separators.

Component

getMenuComponent

​(int n)

Returns the component at position

n

.

int

getMenuComponentCount

()

Returns the number of components on the menu.

Component

[]

getMenuComponents

()

Returns an array of

Component

s of the menu's
subcomponents.

MenuListener

[]

getMenuListeners

()

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

JPopupMenu

getPopupMenu

()

Returns the popupmenu associated with this menu.

protected

Point

getPopupMenuOrigin

()

Computes the origin for the

JMenu

's popup menu.

MenuElement

[]

getSubElements

()

Returns an array of

MenuElement

s containing the submenu
for this menu component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

insert

​(

String

s,
int pos)

Inserts a new menu item with the specified text at a
given position.

JMenuItem

insert

​(

Action

a,
int pos)

Inserts a new menu item attached to the specified

Action

object at a given position.

JMenuItem

insert

​(

JMenuItem

mi,
int pos)

Inserts the specified

JMenuitem

at a given position.

void

insertSeparator

​(int index)

Inserts a separator at the specified position.

boolean

isMenuComponent

​(

Component

c)

Returns true if the specified component exists in the
submenu hierarchy.

boolean

isPopupMenuVisible

()

Returns true if the menu's popup window is visible.

boolean

isSelected

()

Returns true if the menu is currently selected (highlighted).

boolean

isTearOff

()

Returns true if the menu can be torn off.

boolean

isTopLevelMenu

()

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

void

menuSelectionChanged

​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu.

protected

String

paramString

()

Returns a string representation of this

JMenu

.

protected void

processKeyEvent

​(

KeyEvent

evt)

Processes key stroke events such as mnemonics and accelerators.

void

remove

​(int pos)

Removes the menu item at the specified index from this menu.

void

remove

​(

Component

c)

Removes the component

c

from this menu.

void

remove

​(

JMenuItem

item)

Removes the specified menu item from this menu.

void

removeAll

()

Removes all menu items from this menu.

void

removeMenuListener

​(

MenuListener

l)

Removes a listener for menu events.

void

setAccelerator

​(

KeyStroke

keyStroke)

setAccelerator

is not defined for

JMenu

.

void

setDelay

​(int d)

Sets the suggested delay before the menu's

PopupMenu

is popped up or down.

void

setMenuLocation

​(int x,
int y)

Sets the location of the popup component.

void

setModel

​(

ButtonModel

newModel)

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

void

setPopupMenuVisible

​(boolean b)

Sets the visibility of the menu's popup.

void

setSelected

​(boolean b)

Sets the selection status of the menu.

void

updateUI

()

Resets the UI property with a value from the current look and feel.

- Methods declared in class javax.swing.

JMenuItem

actionPropertyChanged

,

addMenuDragMouseListener

,

addMenuKeyListener

,

configurePropertiesFromAction

,

fireMenuDragMouseDragged

,

fireMenuDragMouseEntered

,

fireMenuDragMouseExited

,

fireMenuDragMouseReleased

,

fireMenuKeyPressed

,

fireMenuKeyReleased

,

fireMenuKeyTyped

,

getAccelerator

,

getMenuDragMouseListeners

,

getMenuKeyListeners

,

init

,

isArmed

,

processKeyEvent

,

processMenuDragMouseEvent

,

processMenuKeyEvent

,

processMouseEvent

,

removeMenuDragMouseListener

,

removeMenuKeyListener

,

setArmed

,

setEnabled

,

setUI

- Methods declared in class javax.swing.

AbstractButton

addActionListener

,

addChangeListener

,

addImpl

,

addItemListener

,

checkHorizontalKey

,

checkVerticalKey

,

createActionListener

,

createActionPropertyChangeListener

,

createChangeListener

,

createItemListener

,

doClick

,

fireActionPerformed

,

fireItemStateChanged

,

fireStateChanged

,

getAction

,

getActionCommand

,

getActionListeners

,

getChangeListeners

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getDisplayedMnemonicIndex

,

getHideActionText

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getItemListeners

,

getLabel

,

getMargin

,

getMnemonic

,

getModel

,

getMultiClickThreshhold

,

getPressedIcon

,

getRolloverIcon

,

getRolloverSelectedIcon

,

getSelectedIcon

,

getSelectedObjects

,

getText

,

getUI

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

isBorderPainted

,

isContentAreaFilled

,

isFocusPainted

,

isRolloverEnabled

,

paintBorder

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

removeNotify

,

setAction

,

setActionCommand

,

setBorderPainted

,

setContentAreaFilled

,

setDisabledIcon

,

setDisabledSelectedIcon

,

setDisplayedMnemonicIndex

,

setFocusPainted

,

setHideActionText

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabel

,

setLayout

,

setMargin

,

setMnemonic

,

setMnemonic

,

setMultiClickThreshhold

,

setPressedIcon

,

setRolloverEnabled

,

setRolloverIcon

,

setRolloverSelectedIcon

,

setSelectedIcon

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

- Methods declared in interface javax.swing.

MenuElement

processKeyEvent

,

processMouseEvent

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JMenu.AccessibleJMenu

This class implements accessibility support for the

JMenu

class.

protected class

JMenu.WinListener

A listener class that watches for a popup window closing.

- Nested classes/interfaces declared in class javax.swing.

JMenuItem

JMenuItem.AccessibleJMenuItem

- Nested classes/interfaces declared in class javax.swing.

AbstractButton

AbstractButton.AccessibleAbstractButton

,

AbstractButton.ButtonChangeListener

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

This class implements accessibility support for the

JMenu

class.

A listener class that watches for a popup window closing.

Nested classes/interfaces declared in class javax.swing.

JMenuItem

JMenuItem.AccessibleJMenuItem

---

#### Nested classes/interfaces declared in class javax.swing. JMenuItem

Nested classes/interfaces declared in class javax.swing.

AbstractButton

AbstractButton.AccessibleAbstractButton

,

AbstractButton.ButtonChangeListener

---

#### Nested classes/interfaces declared in class javax.swing. AbstractButton

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

protected

JMenu.WinListener

popupListener

The window-closing listener for the popup.

- Fields declared in class javax.swing.

AbstractButton

actionListener

,

BORDER_PAINTED_CHANGED_PROPERTY

,

changeEvent

,

changeListener

,

CONTENT_AREA_FILLED_CHANGED_PROPERTY

,

DISABLED_ICON_CHANGED_PROPERTY

,

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

,

FOCUS_PAINTED_CHANGED_PROPERTY

,

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

,

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

,

ICON_CHANGED_PROPERTY

,

itemListener

,

MARGIN_CHANGED_PROPERTY

,

MNEMONIC_CHANGED_PROPERTY

,

model

,

MODEL_CHANGED_PROPERTY

,

PRESSED_ICON_CHANGED_PROPERTY

,

ROLLOVER_ENABLED_CHANGED_PROPERTY

,

ROLLOVER_ICON_CHANGED_PROPERTY

,

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

,

SELECTED_ICON_CHANGED_PROPERTY

,

TEXT_CHANGED_PROPERTY

,

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

,

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

The window-closing listener for the popup.

Fields declared in class javax.swing.

AbstractButton

actionListener

,

BORDER_PAINTED_CHANGED_PROPERTY

,

changeEvent

,

changeListener

,

CONTENT_AREA_FILLED_CHANGED_PROPERTY

,

DISABLED_ICON_CHANGED_PROPERTY

,

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

,

FOCUS_PAINTED_CHANGED_PROPERTY

,

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

,

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

,

ICON_CHANGED_PROPERTY

,

itemListener

,

MARGIN_CHANGED_PROPERTY

,

MNEMONIC_CHANGED_PROPERTY

,

model

,

MODEL_CHANGED_PROPERTY

,

PRESSED_ICON_CHANGED_PROPERTY

,

ROLLOVER_ENABLED_CHANGED_PROPERTY

,

ROLLOVER_ICON_CHANGED_PROPERTY

,

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

,

SELECTED_ICON_CHANGED_PROPERTY

,

TEXT_CHANGED_PROPERTY

,

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

,

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

---

#### Fields declared in class javax.swing. AbstractButton

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

JMenu

()

Constructs a new

JMenu

with no text.

JMenu

​(

String

s)

Constructs a new

JMenu

with the supplied string
as its text.

JMenu

​(

String

s,
boolean b)

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

JMenu

​(

Action

a)

Constructs a menu whose properties are taken from the

Action

supplied.

---

#### Constructor Summary

Constructs a new

JMenu

with no text.

Constructs a new

JMenu

with the supplied string
as its text.

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

Constructs a menu whose properties are taken from the

Action

supplied.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Component

add

​(

Component

c)

Appends a component to the end of this menu.

Component

add

​(

Component

c,
int index)

Adds the specified component to this container at the given
position.

JMenuItem

add

​(

String

s)

Creates a new menu item with the specified text and appends
it to the end of this menu.

JMenuItem

add

​(

Action

a)

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

JMenuItem

add

​(

JMenuItem

menuItem)

Appends a menu item to the end of this menu.

void

addMenuListener

​(

MenuListener

l)

Adds a listener for menu events.

void

addSeparator

()

Appends a new separator to the end of the menu.

void

applyComponentOrientation

​(

ComponentOrientation

o)

Sets the

ComponentOrientation

property of this menu
and all components contained within it.

protected

PropertyChangeListener

createActionChangeListener

​(

JMenuItem

b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

protected

JMenuItem

createActionComponent

​(

Action

a)

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

protected

JMenu.WinListener

createWinListener

​(

JPopupMenu

p)

Creates a window-closing listener for the popup.

void

doClick

​(int pressTime)

Programmatically performs a "click".

protected void

fireMenuCanceled

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireMenuDeselected

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireMenuSelected

()

Notifies all listeners that have registered interest for
notification on this event type.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JMenu.

Component

getComponent

()

Returns the

java.awt.Component

used to
paint this

MenuElement

.

int

getDelay

()

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.

JMenuItem

getItem

​(int pos)

Returns the

JMenuItem

at the specified position.

int

getItemCount

()

Returns the number of items on the menu, including separators.

Component

getMenuComponent

​(int n)

Returns the component at position

n

.

int

getMenuComponentCount

()

Returns the number of components on the menu.

Component

[]

getMenuComponents

()

Returns an array of

Component

s of the menu's
subcomponents.

MenuListener

[]

getMenuListeners

()

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

JPopupMenu

getPopupMenu

()

Returns the popupmenu associated with this menu.

protected

Point

getPopupMenuOrigin

()

Computes the origin for the

JMenu

's popup menu.

MenuElement

[]

getSubElements

()

Returns an array of

MenuElement

s containing the submenu
for this menu component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

insert

​(

String

s,
int pos)

Inserts a new menu item with the specified text at a
given position.

JMenuItem

insert

​(

Action

a,
int pos)

Inserts a new menu item attached to the specified

Action

object at a given position.

JMenuItem

insert

​(

JMenuItem

mi,
int pos)

Inserts the specified

JMenuitem

at a given position.

void

insertSeparator

​(int index)

Inserts a separator at the specified position.

boolean

isMenuComponent

​(

Component

c)

Returns true if the specified component exists in the
submenu hierarchy.

boolean

isPopupMenuVisible

()

Returns true if the menu's popup window is visible.

boolean

isSelected

()

Returns true if the menu is currently selected (highlighted).

boolean

isTearOff

()

Returns true if the menu can be torn off.

boolean

isTopLevelMenu

()

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

void

menuSelectionChanged

​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu.

protected

String

paramString

()

Returns a string representation of this

JMenu

.

protected void

processKeyEvent

​(

KeyEvent

evt)

Processes key stroke events such as mnemonics and accelerators.

void

remove

​(int pos)

Removes the menu item at the specified index from this menu.

void

remove

​(

Component

c)

Removes the component

c

from this menu.

void

remove

​(

JMenuItem

item)

Removes the specified menu item from this menu.

void

removeAll

()

Removes all menu items from this menu.

void

removeMenuListener

​(

MenuListener

l)

Removes a listener for menu events.

void

setAccelerator

​(

KeyStroke

keyStroke)

setAccelerator

is not defined for

JMenu

.

void

setDelay

​(int d)

Sets the suggested delay before the menu's

PopupMenu

is popped up or down.

void

setMenuLocation

​(int x,
int y)

Sets the location of the popup component.

void

setModel

​(

ButtonModel

newModel)

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

void

setPopupMenuVisible

​(boolean b)

Sets the visibility of the menu's popup.

void

setSelected

​(boolean b)

Sets the selection status of the menu.

void

updateUI

()

Resets the UI property with a value from the current look and feel.

- Methods declared in class javax.swing.

JMenuItem

actionPropertyChanged

,

addMenuDragMouseListener

,

addMenuKeyListener

,

configurePropertiesFromAction

,

fireMenuDragMouseDragged

,

fireMenuDragMouseEntered

,

fireMenuDragMouseExited

,

fireMenuDragMouseReleased

,

fireMenuKeyPressed

,

fireMenuKeyReleased

,

fireMenuKeyTyped

,

getAccelerator

,

getMenuDragMouseListeners

,

getMenuKeyListeners

,

init

,

isArmed

,

processKeyEvent

,

processMenuDragMouseEvent

,

processMenuKeyEvent

,

processMouseEvent

,

removeMenuDragMouseListener

,

removeMenuKeyListener

,

setArmed

,

setEnabled

,

setUI

- Methods declared in class javax.swing.

AbstractButton

addActionListener

,

addChangeListener

,

addImpl

,

addItemListener

,

checkHorizontalKey

,

checkVerticalKey

,

createActionListener

,

createActionPropertyChangeListener

,

createChangeListener

,

createItemListener

,

doClick

,

fireActionPerformed

,

fireItemStateChanged

,

fireStateChanged

,

getAction

,

getActionCommand

,

getActionListeners

,

getChangeListeners

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getDisplayedMnemonicIndex

,

getHideActionText

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getItemListeners

,

getLabel

,

getMargin

,

getMnemonic

,

getModel

,

getMultiClickThreshhold

,

getPressedIcon

,

getRolloverIcon

,

getRolloverSelectedIcon

,

getSelectedIcon

,

getSelectedObjects

,

getText

,

getUI

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

isBorderPainted

,

isContentAreaFilled

,

isFocusPainted

,

isRolloverEnabled

,

paintBorder

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

removeNotify

,

setAction

,

setActionCommand

,

setBorderPainted

,

setContentAreaFilled

,

setDisabledIcon

,

setDisabledSelectedIcon

,

setDisplayedMnemonicIndex

,

setFocusPainted

,

setHideActionText

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabel

,

setLayout

,

setMargin

,

setMnemonic

,

setMnemonic

,

setMultiClickThreshhold

,

setPressedIcon

,

setRolloverEnabled

,

setRolloverIcon

,

setRolloverSelectedIcon

,

setSelectedIcon

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

- Methods declared in interface javax.swing.

MenuElement

processKeyEvent

,

processMouseEvent

---

#### Method Summary

Appends a component to the end of this menu.

Adds the specified component to this container at the given
position.

Creates a new menu item with the specified text and appends
it to the end of this menu.

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

Appends a menu item to the end of this menu.

Adds a listener for menu events.

Appends a new separator to the end of the menu.

Sets the

ComponentOrientation

property of this menu
and all components contained within it.

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

Creates a window-closing listener for the popup.

Programmatically performs a "click".

Notifies all listeners that have registered interest for
notification on this event type.

Gets the AccessibleContext associated with this JMenu.

Returns the

java.awt.Component

used to
paint this

MenuElement

.

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.

Returns the

JMenuItem

at the specified position.

Returns the number of items on the menu, including separators.

Returns the component at position

n

.

Returns the number of components on the menu.

Returns an array of

Component

s of the menu's
subcomponents.

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

Returns the popupmenu associated with this menu.

Computes the origin for the

JMenu

's popup menu.

Returns an array of

MenuElement

s containing the submenu
for this menu component.

Returns the name of the L&F class that renders this component.

Inserts a new menu item with the specified text at a
given position.

Inserts a new menu item attached to the specified

Action

object at a given position.

Inserts the specified

JMenuitem

at a given position.

Inserts a separator at the specified position.

Returns true if the specified component exists in the
submenu hierarchy.

Returns true if the menu's popup window is visible.

Returns true if the menu is currently selected (highlighted).

Returns true if the menu can be torn off.

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

Messaged when the menubar selection changes to activate or
deactivate this menu.

Returns a string representation of this

JMenu

.

Processes key stroke events such as mnemonics and accelerators.

Removes the menu item at the specified index from this menu.

Removes the component

c

from this menu.

Removes the specified menu item from this menu.

Removes all menu items from this menu.

Removes a listener for menu events.

setAccelerator

is not defined for

JMenu

.

Sets the suggested delay before the menu's

PopupMenu

is popped up or down.

Sets the location of the popup component.

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

Sets the visibility of the menu's popup.

Sets the selection status of the menu.

Resets the UI property with a value from the current look and feel.

Methods declared in class javax.swing.

JMenuItem

actionPropertyChanged

,

addMenuDragMouseListener

,

addMenuKeyListener

,

configurePropertiesFromAction

,

fireMenuDragMouseDragged

,

fireMenuDragMouseEntered

,

fireMenuDragMouseExited

,

fireMenuDragMouseReleased

,

fireMenuKeyPressed

,

fireMenuKeyReleased

,

fireMenuKeyTyped

,

getAccelerator

,

getMenuDragMouseListeners

,

getMenuKeyListeners

,

init

,

isArmed

,

processKeyEvent

,

processMenuDragMouseEvent

,

processMenuKeyEvent

,

processMouseEvent

,

removeMenuDragMouseListener

,

removeMenuKeyListener

,

setArmed

,

setEnabled

,

setUI

---

#### Methods declared in class javax.swing. JMenuItem

Methods declared in class javax.swing.

AbstractButton

addActionListener

,

addChangeListener

,

addImpl

,

addItemListener

,

checkHorizontalKey

,

checkVerticalKey

,

createActionListener

,

createActionPropertyChangeListener

,

createChangeListener

,

createItemListener

,

doClick

,

fireActionPerformed

,

fireItemStateChanged

,

fireStateChanged

,

getAction

,

getActionCommand

,

getActionListeners

,

getChangeListeners

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getDisplayedMnemonicIndex

,

getHideActionText

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getItemListeners

,

getLabel

,

getMargin

,

getMnemonic

,

getModel

,

getMultiClickThreshhold

,

getPressedIcon

,

getRolloverIcon

,

getRolloverSelectedIcon

,

getSelectedIcon

,

getSelectedObjects

,

getText

,

getUI

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

isBorderPainted

,

isContentAreaFilled

,

isFocusPainted

,

isRolloverEnabled

,

paintBorder

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

removeNotify

,

setAction

,

setActionCommand

,

setBorderPainted

,

setContentAreaFilled

,

setDisabledIcon

,

setDisabledSelectedIcon

,

setDisplayedMnemonicIndex

,

setFocusPainted

,

setHideActionText

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabel

,

setLayout

,

setMargin

,

setMnemonic

,

setMnemonic

,

setMultiClickThreshhold

,

setPressedIcon

,

setRolloverEnabled

,

setRolloverIcon

,

setRolloverSelectedIcon

,

setSelectedIcon

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

---

#### Methods declared in class javax.swing. AbstractButton

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

Methods declared in interface javax.swing.

MenuElement

processKeyEvent

,

processMouseEvent

---

#### Methods declared in interface javax.swing. MenuElement

============ FIELD DETAIL ===========

- Field Detail

- popupListener

```java
protected
JMenu.WinListener
popupListener
```

The window-closing listener for the popup.

**See Also:** JMenu.WinListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JMenu

```java
public JMenu()
```

Constructs a new

JMenu

with no text.

- JMenu

```java
public JMenu​(
String
s)
```

Constructs a new

JMenu

with the supplied string
as its text.

**Parameters:** s

- the text for the menu label

- JMenu

```java
public JMenu​(
Action
a)
```

Constructs a menu whose properties are taken from the

Action

supplied.

**Parameters:** a

- an

Action
**Since:** 1.3

- JMenu

```java
public JMenu​(
String
s,
boolean b)
```

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

**Parameters:** s

- the text for the menu label
**Parameters:** b

- can the menu be torn off (not yet implemented)

============ METHOD DETAIL ==========

- Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property with a value from the current look and feel.

**Overrides:** updateUI

in class

JMenuItem
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JMenuItem
**Returns:** the string "MenuUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setModel

```java
public void setModel​(
ButtonModel
newModel)
```

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

**Overrides:** setModel

in class

AbstractButton
**Parameters:** newModel

- the

ButtonModel
**See Also:** AbstractButton.getModel()

- isSelected

```java
public boolean isSelected()
```

Returns true if the menu is currently selected (highlighted).

**Overrides:** isSelected

in class

AbstractButton
**Returns:** true if the menu is selected, else false

- setSelected

```java
@BeanProperty
(
expert
=true,

hidden
=true,

description
="When the menu is selected, its popup child is shown.")
public void setSelected​(boolean b)
```

Sets the selection status of the menu.

**Overrides:** setSelected

in class

AbstractButton
**Parameters:** b

- true to select (highlight) the menu; false to de-select
the menu

- isPopupMenuVisible

```java
public boolean isPopupMenuVisible()
```

Returns true if the menu's popup window is visible.

**Returns:** true if the menu is visible, else false

- setPopupMenuVisible

```java
@BeanProperty
(
bound
=false,

expert
=true,

hidden
=true,

description
="The popup menu\'s visibility")
public void setPopupMenuVisible​(boolean b)
```

Sets the visibility of the menu's popup. If the menu is
not enabled, this method will have no effect.

**Parameters:** b

- a boolean value -- true to make the menu visible,
false to hide it

- getPopupMenuOrigin

```java
protected
Point
getPopupMenuOrigin()
```

Computes the origin for the

JMenu

's popup menu.
This method uses Look and Feel properties named

Menu.menuPopupOffsetX

,

Menu.menuPopupOffsetY

,

Menu.submenuPopupOffsetX

, and

Menu.submenuPopupOffsetY

to adjust the exact location of popup.

**Returns:** a

Point

in the coordinate space of the
menu which should be used as the origin
of the

JMenu

's popup menu
**Since:** 1.3

- getDelay

```java
public int getDelay()
```

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.
Each look and feel (L&F) may determine its own policy for
observing the

delay

property.
In most cases, the delay is not observed for top level menus
or while dragging. The default for

delay

is 0.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Returns:** the

delay

property

- setDelay

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The delay between menu selection and making the popup menu visible")
public void setDelay​(int d)
```

Sets the suggested delay before the menu's

PopupMenu

is popped up or down. Each look and feel (L&F) may determine
it's own policy for observing the delay property. In most cases,
the delay is not observed for top level menus or while dragging.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Parameters:** d

- the number of milliseconds to delay
**Throws:** IllegalArgumentException

- if

d

is less than 0

- setMenuLocation

```java
public void setMenuLocation​(int x,
int y)
```

Sets the location of the popup component.

**Parameters:** x

- the x coordinate of the popup's new position
**Parameters:** y

- the y coordinate of the popup's new position

- add

```java
public
JMenuItem
add​(
JMenuItem
menuItem)
```

Appends a menu item to the end of this menu.
Returns the menu item added.

**Parameters:** menuItem

- the

JMenuitem

to be added
**Returns:** the

JMenuItem

added

- add

```java
public
Component
add​(
Component
c)
```

Appends a component to the end of this menu.
Returns the component added.

**Overrides:** add

in class

Container
**Parameters:** c

- the

Component

to add
**Returns:** the

Component

added
**See Also:** Container.addImpl(java.awt.Component, java.lang.Object, int)

,

Container.invalidate()

,

Container.validate()

,

JComponent.revalidate()

- add

```java
public
Component
add​(
Component
c,
int index)
```

Adds the specified component to this container at the given
position. If

index

equals -1, the component will
be appended to the end.

**Overrides:** add

in class

Container
**Parameters:** c

- the

Component

to add
**Parameters:** index

- the position at which to insert the component
**Returns:** the

Component

added
**See Also:** remove(javax.swing.JMenuItem)

,

Container.add(Component, int)

- add

```java
public
JMenuItem
add​(
String
s)
```

Creates a new menu item with the specified text and appends
it to the end of this menu.

**Parameters:** s

- the string for the menu item to be added
**Returns:** the new

JMenuItem

- add

```java
public
JMenuItem
add​(
Action
a)
```

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

**Parameters:** a

- the

Action

for the menu item to be added
**Returns:** the new

JMenuItem
**See Also:** Action

- createActionComponent

```java
protected
JMenuItem
createActionComponent​(
Action
a)
```

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

**Parameters:** a

- the

Action

for the menu item to be added
**Returns:** the new menu item
**Since:** 1.3
**See Also:** Action

- createActionChangeListener

```java
protected
PropertyChangeListener
createActionChangeListener​(
JMenuItem
b)
```

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

**Parameters:** b

- a menu item for which to create a

PropertyChangeListener
**Returns:** a

PropertyChangeListener

for

b

- addSeparator

```java
public void addSeparator()
```

Appends a new separator to the end of the menu.

- insert

```java
public void insert​(
String
s,
int pos)
```

Inserts a new menu item with the specified text at a
given position.

**Parameters:** s

- the text for the menu item to add
**Parameters:** pos

- an integer specifying the position at which to add the
new menu item
**Throws:** IllegalArgumentException

- when the value of

pos

< 0

- insert

```java
public
JMenuItem
insert​(
JMenuItem
mi,
int pos)
```

Inserts the specified

JMenuitem

at a given position.

**Parameters:** mi

- the

JMenuitem

to add
**Parameters:** pos

- an integer specifying the position at which to add the
new

JMenuitem
**Returns:** the new menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

- insert

```java
public
JMenuItem
insert​(
Action
a,
int pos)
```

Inserts a new menu item attached to the specified

Action

object at a given position.

**Parameters:** a

- the

Action

object for the menu item to add
**Parameters:** pos

- an integer specifying the position at which to add the
new menu item
**Returns:** the new menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

- insertSeparator

```java
public void insertSeparator​(int index)
```

Inserts a separator at the specified position.

**Parameters:** index

- an integer specifying the position at which to
insert the menu separator
**Throws:** IllegalArgumentException

- if the value of

index

< 0

- getItem

```java
public
JMenuItem
getItem​(int pos)
```

Returns the

JMenuItem

at the specified position.
If the component at

pos

is not a menu item,

null

is returned.
This method is included for AWT compatibility.

**Parameters:** pos

- an integer specifying the position
**Returns:** the menu item at the specified position; or

null

if the item as the specified position is not a menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

- getItemCount

```java
@BeanProperty
(
bound
=false)
public int getItemCount()
```

Returns the number of items on the menu, including separators.
This method is included for AWT compatibility.

**Returns:** an integer equal to the number of items on the menu
**See Also:** getMenuComponentCount()

- isTearOff

```java
@BeanProperty
(
bound
=false)
public boolean isTearOff()
```

Returns true if the menu can be torn off. This method is not
yet implemented.

**Returns:** true if the menu can be torn off, else false
**Throws:** Error

- if invoked -- this method is not yet implemented

- remove

```java
public void remove​(
JMenuItem
item)
```

Removes the specified menu item from this menu. If there is no
popup menu, this method will have no effect.

**Parameters:** item

- the

JMenuItem

to be removed from the menu

- remove

```java
public void remove​(int pos)
```

Removes the menu item at the specified index from this menu.

**Overrides:** remove

in class

Container
**Parameters:** pos

- the position of the item to be removed
**Throws:** IllegalArgumentException

- if the value of

pos

< 0, or if

pos

is greater than the number of menu items
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

- remove

```java
public void remove​(
Component
c)
```

Removes the component

c

from this menu.

**Overrides:** remove

in class

Container
**Parameters:** c

- the component to be removed
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

- removeAll

```java
public void removeAll()
```

Removes all menu items from this menu.

**Overrides:** removeAll

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

- getMenuComponentCount

```java
@BeanProperty
(
bound
=false)
public int getMenuComponentCount()
```

Returns the number of components on the menu.

**Returns:** an integer containing the number of components on the menu

- getMenuComponent

```java
public
Component
getMenuComponent​(int n)
```

Returns the component at position

n

.

**Parameters:** n

- the position of the component to be returned
**Returns:** the component requested, or

null

if there is no popup menu

- getMenuComponents

```java
@BeanProperty
(
bound
=false)
public
Component
[] getMenuComponents()
```

Returns an array of

Component

s of the menu's
subcomponents. Note that this returns all

Component

s
in the popup menu, including separators.

**Returns:** an array of

Component

s or an empty array
if there is no popup menu

- isTopLevelMenu

```java
@BeanProperty
(
bound
=false)
public boolean isTopLevelMenu()
```

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

**Returns:** true if the menu is activated from the menu bar;
false if the menu is activated from a menu item
on another menu

- isMenuComponent

```java
public boolean isMenuComponent​(
Component
c)
```

Returns true if the specified component exists in the
submenu hierarchy.

**Parameters:** c

- the

Component

to be tested
**Returns:** true if the

Component

exists, false otherwise

- getPopupMenu

```java
@BeanProperty
(
bound
=false)
public
JPopupMenu
getPopupMenu()
```

Returns the popupmenu associated with this menu. If there is
no popupmenu, it will create one.

**Returns:** the

JPopupMenu

associated with this menu

- addMenuListener

```java
public void addMenuListener​(
MenuListener
l)
```

Adds a listener for menu events.

**Parameters:** l

- the listener to be added

- removeMenuListener

```java
public void removeMenuListener​(
MenuListener
l)
```

Removes a listener for menu events.

**Parameters:** l

- the listener to be removed

- getMenuListeners

```java
@BeanProperty
(
bound
=false)
public
MenuListener
[] getMenuListeners()
```

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

**Returns:** all of the

MenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireMenuSelected

```java
protected void fireMenuSelected()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

- fireMenuDeselected

```java
protected void fireMenuDeselected()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

- fireMenuCanceled

```java
protected void fireMenuCanceled()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

- createWinListener

```java
protected
JMenu.WinListener
createWinListener​(
JPopupMenu
p)
```

Creates a window-closing listener for the popup.

**Parameters:** p

- the

JPopupMenu
**Returns:** the new window-closing listener
**See Also:** JMenu.WinListener

- menuSelectionChanged

```java
public void menuSelectionChanged​(boolean isIncluded)
```

Messaged when the menubar selection changes to activate or
deactivate this menu.
Overrides

JMenuItem.menuSelectionChanged

.

**Specified by:** menuSelectionChanged

in interface

MenuElement
**Overrides:** menuSelectionChanged

in class

JMenuItem
**Parameters:** isIncluded

- true if this menu is active, false if
it is not
**See Also:** MenuSelectionManager.setSelectedPath(MenuElement[])

- getSubElements

```java
@BeanProperty
(
bound
=false)
public
MenuElement
[] getSubElements()
```

Returns an array of

MenuElement

s containing the submenu
for this menu component. If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface. Note that since

JSeparator

s do not conform to the

MenuElement

interface, this array will only contain

JMenuItem

s.

**Specified by:** getSubElements

in interface

MenuElement
**Overrides:** getSubElements

in class

JMenuItem
**Returns:** an array of

MenuElement

objects

- getComponent

```java
public
Component
getComponent()
```

Returns the

java.awt.Component

used to
paint this

MenuElement

.
The returned component is used to convert events and detect if
an event is inside a menu component.

**Specified by:** getComponent

in interface

MenuElement
**Overrides:** getComponent

in class

JMenuItem
**Returns:** the

Component

that paints this menu item

- applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
o)
```

Sets the

ComponentOrientation

property of this menu
and all components contained within it. This includes all
components returned by

getMenuComponents

.

**Overrides:** applyComponentOrientation

in class

Container
**Parameters:** o

- the new component orientation of this menu and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

- setAccelerator

```java
public void setAccelerator​(
KeyStroke
keyStroke)
```

setAccelerator

is not defined for

JMenu

.
Use

setMnemonic

instead.

**Overrides:** setAccelerator

in class

JMenuItem
**Parameters:** keyStroke

- the keystroke combination which will invoke
the

JMenuItem

's actionlisteners
without navigating the menu hierarchy
**Throws:** Error

- if invoked -- this method is not defined for JMenu.
Use

setMnemonic

instead

- processKeyEvent

```java
protected void processKeyEvent​(
KeyEvent
evt)
```

Processes key stroke events such as mnemonics and accelerators.

**Overrides:** processKeyEvent

in class

JComponent
**Parameters:** evt

- the key event to be processed
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

- doClick

```java
public void doClick​(int pressTime)
```

Programmatically performs a "click". This overrides the method

AbstractButton.doClick

in order to make the menu pop up.

**Overrides:** doClick

in class

AbstractButton
**Parameters:** pressTime

- indicates the number of milliseconds the
button was pressed for

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JMenu

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JMenuItem
**Returns:** a string representation of this JMenu.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JMenu.
For JMenus, the AccessibleContext takes the form of an
AccessibleJMenu.
A new AccessibleJMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JMenuItem
**Returns:** an AccessibleJMenu that serves as the
AccessibleContext of this JMenu

Field Detail

- popupListener

```java
protected
JMenu.WinListener
popupListener
```

The window-closing listener for the popup.

**See Also:** JMenu.WinListener

---

#### Field Detail

popupListener

```java
protected
JMenu.WinListener
popupListener
```

The window-closing listener for the popup.

**See Also:** JMenu.WinListener

---

#### popupListener

protected

JMenu.WinListener

popupListener

The window-closing listener for the popup.

Constructor Detail

- JMenu

```java
public JMenu()
```

Constructs a new

JMenu

with no text.

- JMenu

```java
public JMenu​(
String
s)
```

Constructs a new

JMenu

with the supplied string
as its text.

**Parameters:** s

- the text for the menu label

- JMenu

```java
public JMenu​(
Action
a)
```

Constructs a menu whose properties are taken from the

Action

supplied.

**Parameters:** a

- an

Action
**Since:** 1.3

- JMenu

```java
public JMenu​(
String
s,
boolean b)
```

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

**Parameters:** s

- the text for the menu label
**Parameters:** b

- can the menu be torn off (not yet implemented)

---

#### Constructor Detail

JMenu

```java
public JMenu()
```

Constructs a new

JMenu

with no text.

---

#### JMenu

public JMenu()

Constructs a new

JMenu

with no text.

JMenu

```java
public JMenu​(
String
s)
```

Constructs a new

JMenu

with the supplied string
as its text.

**Parameters:** s

- the text for the menu label

---

#### JMenu

public JMenu​(

String

s)

Constructs a new

JMenu

with the supplied string
as its text.

JMenu

```java
public JMenu​(
Action
a)
```

Constructs a menu whose properties are taken from the

Action

supplied.

**Parameters:** a

- an

Action
**Since:** 1.3

---

#### JMenu

public JMenu​(

Action

a)

Constructs a menu whose properties are taken from the

Action

supplied.

JMenu

```java
public JMenu​(
String
s,
boolean b)
```

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

**Parameters:** s

- the text for the menu label
**Parameters:** b

- can the menu be torn off (not yet implemented)

---

#### JMenu

public JMenu​(

String

s,
boolean b)

Constructs a new

JMenu

with the supplied string as
its text and specified as a tear-off menu or not.

Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property with a value from the current look and feel.

**Overrides:** updateUI

in class

JMenuItem
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JMenuItem
**Returns:** the string "MenuUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setModel

```java
public void setModel​(
ButtonModel
newModel)
```

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

**Overrides:** setModel

in class

AbstractButton
**Parameters:** newModel

- the

ButtonModel
**See Also:** AbstractButton.getModel()

- isSelected

```java
public boolean isSelected()
```

Returns true if the menu is currently selected (highlighted).

**Overrides:** isSelected

in class

AbstractButton
**Returns:** true if the menu is selected, else false

- setSelected

```java
@BeanProperty
(
expert
=true,

hidden
=true,

description
="When the menu is selected, its popup child is shown.")
public void setSelected​(boolean b)
```

Sets the selection status of the menu.

**Overrides:** setSelected

in class

AbstractButton
**Parameters:** b

- true to select (highlight) the menu; false to de-select
the menu

- isPopupMenuVisible

```java
public boolean isPopupMenuVisible()
```

Returns true if the menu's popup window is visible.

**Returns:** true if the menu is visible, else false

- setPopupMenuVisible

```java
@BeanProperty
(
bound
=false,

expert
=true,

hidden
=true,

description
="The popup menu\'s visibility")
public void setPopupMenuVisible​(boolean b)
```

Sets the visibility of the menu's popup. If the menu is
not enabled, this method will have no effect.

**Parameters:** b

- a boolean value -- true to make the menu visible,
false to hide it

- getPopupMenuOrigin

```java
protected
Point
getPopupMenuOrigin()
```

Computes the origin for the

JMenu

's popup menu.
This method uses Look and Feel properties named

Menu.menuPopupOffsetX

,

Menu.menuPopupOffsetY

,

Menu.submenuPopupOffsetX

, and

Menu.submenuPopupOffsetY

to adjust the exact location of popup.

**Returns:** a

Point

in the coordinate space of the
menu which should be used as the origin
of the

JMenu

's popup menu
**Since:** 1.3

- getDelay

```java
public int getDelay()
```

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.
Each look and feel (L&F) may determine its own policy for
observing the

delay

property.
In most cases, the delay is not observed for top level menus
or while dragging. The default for

delay

is 0.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Returns:** the

delay

property

- setDelay

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The delay between menu selection and making the popup menu visible")
public void setDelay​(int d)
```

Sets the suggested delay before the menu's

PopupMenu

is popped up or down. Each look and feel (L&F) may determine
it's own policy for observing the delay property. In most cases,
the delay is not observed for top level menus or while dragging.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Parameters:** d

- the number of milliseconds to delay
**Throws:** IllegalArgumentException

- if

d

is less than 0

- setMenuLocation

```java
public void setMenuLocation​(int x,
int y)
```

Sets the location of the popup component.

**Parameters:** x

- the x coordinate of the popup's new position
**Parameters:** y

- the y coordinate of the popup's new position

- add

```java
public
JMenuItem
add​(
JMenuItem
menuItem)
```

Appends a menu item to the end of this menu.
Returns the menu item added.

**Parameters:** menuItem

- the

JMenuitem

to be added
**Returns:** the

JMenuItem

added

- add

```java
public
Component
add​(
Component
c)
```

Appends a component to the end of this menu.
Returns the component added.

**Overrides:** add

in class

Container
**Parameters:** c

- the

Component

to add
**Returns:** the

Component

added
**See Also:** Container.addImpl(java.awt.Component, java.lang.Object, int)

,

Container.invalidate()

,

Container.validate()

,

JComponent.revalidate()

- add

```java
public
Component
add​(
Component
c,
int index)
```

Adds the specified component to this container at the given
position. If

index

equals -1, the component will
be appended to the end.

**Overrides:** add

in class

Container
**Parameters:** c

- the

Component

to add
**Parameters:** index

- the position at which to insert the component
**Returns:** the

Component

added
**See Also:** remove(javax.swing.JMenuItem)

,

Container.add(Component, int)

- add

```java
public
JMenuItem
add​(
String
s)
```

Creates a new menu item with the specified text and appends
it to the end of this menu.

**Parameters:** s

- the string for the menu item to be added
**Returns:** the new

JMenuItem

- add

```java
public
JMenuItem
add​(
Action
a)
```

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

**Parameters:** a

- the

Action

for the menu item to be added
**Returns:** the new

JMenuItem
**See Also:** Action

- createActionComponent

```java
protected
JMenuItem
createActionComponent​(
Action
a)
```

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

**Parameters:** a

- the

Action

for the menu item to be added
**Returns:** the new menu item
**Since:** 1.3
**See Also:** Action

- createActionChangeListener

```java
protected
PropertyChangeListener
createActionChangeListener​(
JMenuItem
b)
```

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

**Parameters:** b

- a menu item for which to create a

PropertyChangeListener
**Returns:** a

PropertyChangeListener

for

b

- addSeparator

```java
public void addSeparator()
```

Appends a new separator to the end of the menu.

- insert

```java
public void insert​(
String
s,
int pos)
```

Inserts a new menu item with the specified text at a
given position.

**Parameters:** s

- the text for the menu item to add
**Parameters:** pos

- an integer specifying the position at which to add the
new menu item
**Throws:** IllegalArgumentException

- when the value of

pos

< 0

- insert

```java
public
JMenuItem
insert​(
JMenuItem
mi,
int pos)
```

Inserts the specified

JMenuitem

at a given position.

**Parameters:** mi

- the

JMenuitem

to add
**Parameters:** pos

- an integer specifying the position at which to add the
new

JMenuitem
**Returns:** the new menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

- insert

```java
public
JMenuItem
insert​(
Action
a,
int pos)
```

Inserts a new menu item attached to the specified

Action

object at a given position.

**Parameters:** a

- the

Action

object for the menu item to add
**Parameters:** pos

- an integer specifying the position at which to add the
new menu item
**Returns:** the new menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

- insertSeparator

```java
public void insertSeparator​(int index)
```

Inserts a separator at the specified position.

**Parameters:** index

- an integer specifying the position at which to
insert the menu separator
**Throws:** IllegalArgumentException

- if the value of

index

< 0

- getItem

```java
public
JMenuItem
getItem​(int pos)
```

Returns the

JMenuItem

at the specified position.
If the component at

pos

is not a menu item,

null

is returned.
This method is included for AWT compatibility.

**Parameters:** pos

- an integer specifying the position
**Returns:** the menu item at the specified position; or

null

if the item as the specified position is not a menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

- getItemCount

```java
@BeanProperty
(
bound
=false)
public int getItemCount()
```

Returns the number of items on the menu, including separators.
This method is included for AWT compatibility.

**Returns:** an integer equal to the number of items on the menu
**See Also:** getMenuComponentCount()

- isTearOff

```java
@BeanProperty
(
bound
=false)
public boolean isTearOff()
```

Returns true if the menu can be torn off. This method is not
yet implemented.

**Returns:** true if the menu can be torn off, else false
**Throws:** Error

- if invoked -- this method is not yet implemented

- remove

```java
public void remove​(
JMenuItem
item)
```

Removes the specified menu item from this menu. If there is no
popup menu, this method will have no effect.

**Parameters:** item

- the

JMenuItem

to be removed from the menu

- remove

```java
public void remove​(int pos)
```

Removes the menu item at the specified index from this menu.

**Overrides:** remove

in class

Container
**Parameters:** pos

- the position of the item to be removed
**Throws:** IllegalArgumentException

- if the value of

pos

< 0, or if

pos

is greater than the number of menu items
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

- remove

```java
public void remove​(
Component
c)
```

Removes the component

c

from this menu.

**Overrides:** remove

in class

Container
**Parameters:** c

- the component to be removed
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

- removeAll

```java
public void removeAll()
```

Removes all menu items from this menu.

**Overrides:** removeAll

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

- getMenuComponentCount

```java
@BeanProperty
(
bound
=false)
public int getMenuComponentCount()
```

Returns the number of components on the menu.

**Returns:** an integer containing the number of components on the menu

- getMenuComponent

```java
public
Component
getMenuComponent​(int n)
```

Returns the component at position

n

.

**Parameters:** n

- the position of the component to be returned
**Returns:** the component requested, or

null

if there is no popup menu

- getMenuComponents

```java
@BeanProperty
(
bound
=false)
public
Component
[] getMenuComponents()
```

Returns an array of

Component

s of the menu's
subcomponents. Note that this returns all

Component

s
in the popup menu, including separators.

**Returns:** an array of

Component

s or an empty array
if there is no popup menu

- isTopLevelMenu

```java
@BeanProperty
(
bound
=false)
public boolean isTopLevelMenu()
```

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

**Returns:** true if the menu is activated from the menu bar;
false if the menu is activated from a menu item
on another menu

- isMenuComponent

```java
public boolean isMenuComponent​(
Component
c)
```

Returns true if the specified component exists in the
submenu hierarchy.

**Parameters:** c

- the

Component

to be tested
**Returns:** true if the

Component

exists, false otherwise

- getPopupMenu

```java
@BeanProperty
(
bound
=false)
public
JPopupMenu
getPopupMenu()
```

Returns the popupmenu associated with this menu. If there is
no popupmenu, it will create one.

**Returns:** the

JPopupMenu

associated with this menu

- addMenuListener

```java
public void addMenuListener​(
MenuListener
l)
```

Adds a listener for menu events.

**Parameters:** l

- the listener to be added

- removeMenuListener

```java
public void removeMenuListener​(
MenuListener
l)
```

Removes a listener for menu events.

**Parameters:** l

- the listener to be removed

- getMenuListeners

```java
@BeanProperty
(
bound
=false)
public
MenuListener
[] getMenuListeners()
```

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

**Returns:** all of the

MenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireMenuSelected

```java
protected void fireMenuSelected()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

- fireMenuDeselected

```java
protected void fireMenuDeselected()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

- fireMenuCanceled

```java
protected void fireMenuCanceled()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

- createWinListener

```java
protected
JMenu.WinListener
createWinListener​(
JPopupMenu
p)
```

Creates a window-closing listener for the popup.

**Parameters:** p

- the

JPopupMenu
**Returns:** the new window-closing listener
**See Also:** JMenu.WinListener

- menuSelectionChanged

```java
public void menuSelectionChanged​(boolean isIncluded)
```

Messaged when the menubar selection changes to activate or
deactivate this menu.
Overrides

JMenuItem.menuSelectionChanged

.

**Specified by:** menuSelectionChanged

in interface

MenuElement
**Overrides:** menuSelectionChanged

in class

JMenuItem
**Parameters:** isIncluded

- true if this menu is active, false if
it is not
**See Also:** MenuSelectionManager.setSelectedPath(MenuElement[])

- getSubElements

```java
@BeanProperty
(
bound
=false)
public
MenuElement
[] getSubElements()
```

Returns an array of

MenuElement

s containing the submenu
for this menu component. If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface. Note that since

JSeparator

s do not conform to the

MenuElement

interface, this array will only contain

JMenuItem

s.

**Specified by:** getSubElements

in interface

MenuElement
**Overrides:** getSubElements

in class

JMenuItem
**Returns:** an array of

MenuElement

objects

- getComponent

```java
public
Component
getComponent()
```

Returns the

java.awt.Component

used to
paint this

MenuElement

.
The returned component is used to convert events and detect if
an event is inside a menu component.

**Specified by:** getComponent

in interface

MenuElement
**Overrides:** getComponent

in class

JMenuItem
**Returns:** the

Component

that paints this menu item

- applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
o)
```

Sets the

ComponentOrientation

property of this menu
and all components contained within it. This includes all
components returned by

getMenuComponents

.

**Overrides:** applyComponentOrientation

in class

Container
**Parameters:** o

- the new component orientation of this menu and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

- setAccelerator

```java
public void setAccelerator​(
KeyStroke
keyStroke)
```

setAccelerator

is not defined for

JMenu

.
Use

setMnemonic

instead.

**Overrides:** setAccelerator

in class

JMenuItem
**Parameters:** keyStroke

- the keystroke combination which will invoke
the

JMenuItem

's actionlisteners
without navigating the menu hierarchy
**Throws:** Error

- if invoked -- this method is not defined for JMenu.
Use

setMnemonic

instead

- processKeyEvent

```java
protected void processKeyEvent​(
KeyEvent
evt)
```

Processes key stroke events such as mnemonics and accelerators.

**Overrides:** processKeyEvent

in class

JComponent
**Parameters:** evt

- the key event to be processed
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

- doClick

```java
public void doClick​(int pressTime)
```

Programmatically performs a "click". This overrides the method

AbstractButton.doClick

in order to make the menu pop up.

**Overrides:** doClick

in class

AbstractButton
**Parameters:** pressTime

- indicates the number of milliseconds the
button was pressed for

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JMenu

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JMenuItem
**Returns:** a string representation of this JMenu.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JMenu.
For JMenus, the AccessibleContext takes the form of an
AccessibleJMenu.
A new AccessibleJMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JMenuItem
**Returns:** an AccessibleJMenu that serves as the
AccessibleContext of this JMenu

---

#### Method Detail

updateUI

```java
public void updateUI()
```

Resets the UI property with a value from the current look and feel.

**Overrides:** updateUI

in class

JMenuItem
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property with a value from the current look and feel.

getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JMenuItem
**Returns:** the string "MenuUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false)
public

String

getUIClassID()

Returns the name of the L&F class that renders this component.

setModel

```java
public void setModel​(
ButtonModel
newModel)
```

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

**Overrides:** setModel

in class

AbstractButton
**Parameters:** newModel

- the

ButtonModel
**See Also:** AbstractButton.getModel()

---

#### setModel

public void setModel​(

ButtonModel

newModel)

Sets the data model for the "menu button" -- the label
that the user clicks to open or close the menu.

isSelected

```java
public boolean isSelected()
```

Returns true if the menu is currently selected (highlighted).

**Overrides:** isSelected

in class

AbstractButton
**Returns:** true if the menu is selected, else false

---

#### isSelected

public boolean isSelected()

Returns true if the menu is currently selected (highlighted).

setSelected

```java
@BeanProperty
(
expert
=true,

hidden
=true,

description
="When the menu is selected, its popup child is shown.")
public void setSelected​(boolean b)
```

Sets the selection status of the menu.

**Overrides:** setSelected

in class

AbstractButton
**Parameters:** b

- true to select (highlight) the menu; false to de-select
the menu

---

#### setSelected

@BeanProperty

(

expert

=true,

hidden

=true,

description

="When the menu is selected, its popup child is shown.")
public void setSelected​(boolean b)

Sets the selection status of the menu.

isPopupMenuVisible

```java
public boolean isPopupMenuVisible()
```

Returns true if the menu's popup window is visible.

**Returns:** true if the menu is visible, else false

---

#### isPopupMenuVisible

public boolean isPopupMenuVisible()

Returns true if the menu's popup window is visible.

setPopupMenuVisible

```java
@BeanProperty
(
bound
=false,

expert
=true,

hidden
=true,

description
="The popup menu\'s visibility")
public void setPopupMenuVisible​(boolean b)
```

Sets the visibility of the menu's popup. If the menu is
not enabled, this method will have no effect.

**Parameters:** b

- a boolean value -- true to make the menu visible,
false to hide it

---

#### setPopupMenuVisible

@BeanProperty

(

bound

=false,

expert

=true,

hidden

=true,

description

="The popup menu\'s visibility")
public void setPopupMenuVisible​(boolean b)

Sets the visibility of the menu's popup. If the menu is
not enabled, this method will have no effect.

getPopupMenuOrigin

```java
protected
Point
getPopupMenuOrigin()
```

Computes the origin for the

JMenu

's popup menu.
This method uses Look and Feel properties named

Menu.menuPopupOffsetX

,

Menu.menuPopupOffsetY

,

Menu.submenuPopupOffsetX

, and

Menu.submenuPopupOffsetY

to adjust the exact location of popup.

**Returns:** a

Point

in the coordinate space of the
menu which should be used as the origin
of the

JMenu

's popup menu
**Since:** 1.3

---

#### getPopupMenuOrigin

protected

Point

getPopupMenuOrigin()

Computes the origin for the

JMenu

's popup menu.
This method uses Look and Feel properties named

Menu.menuPopupOffsetX

,

Menu.menuPopupOffsetY

,

Menu.submenuPopupOffsetX

, and

Menu.submenuPopupOffsetY

to adjust the exact location of popup.

getDelay

```java
public int getDelay()
```

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.
Each look and feel (L&F) may determine its own policy for
observing the

delay

property.
In most cases, the delay is not observed for top level menus
or while dragging. The default for

delay

is 0.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Returns:** the

delay

property

---

#### getDelay

public int getDelay()

Returns the suggested delay, in milliseconds, before submenus
are popped up or down.
Each look and feel (L&F) may determine its own policy for
observing the

delay

property.
In most cases, the delay is not observed for top level menus
or while dragging. The default for

delay

is 0.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

setDelay

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The delay between menu selection and making the popup menu visible")
public void setDelay​(int d)
```

Sets the suggested delay before the menu's

PopupMenu

is popped up or down. Each look and feel (L&F) may determine
it's own policy for observing the delay property. In most cases,
the delay is not observed for top level menus or while dragging.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

**Parameters:** d

- the number of milliseconds to delay
**Throws:** IllegalArgumentException

- if

d

is less than 0

---

#### setDelay

@BeanProperty

(

bound

=false,

expert

=true,

description

="The delay between menu selection and making the popup menu visible")
public void setDelay​(int d)

Sets the suggested delay before the menu's

PopupMenu

is popped up or down. Each look and feel (L&F) may determine
it's own policy for observing the delay property. In most cases,
the delay is not observed for top level menus or while dragging.
This method is a property of the look and feel code and is used
to manage the idiosyncrasies of the various UI implementations.

setMenuLocation

```java
public void setMenuLocation​(int x,
int y)
```

Sets the location of the popup component.

**Parameters:** x

- the x coordinate of the popup's new position
**Parameters:** y

- the y coordinate of the popup's new position

---

#### setMenuLocation

public void setMenuLocation​(int x,
int y)

Sets the location of the popup component.

add

```java
public
JMenuItem
add​(
JMenuItem
menuItem)
```

Appends a menu item to the end of this menu.
Returns the menu item added.

**Parameters:** menuItem

- the

JMenuitem

to be added
**Returns:** the

JMenuItem

added

---

#### add

public

JMenuItem

add​(

JMenuItem

menuItem)

Appends a menu item to the end of this menu.
Returns the menu item added.

add

```java
public
Component
add​(
Component
c)
```

Appends a component to the end of this menu.
Returns the component added.

**Overrides:** add

in class

Container
**Parameters:** c

- the

Component

to add
**Returns:** the

Component

added
**See Also:** Container.addImpl(java.awt.Component, java.lang.Object, int)

,

Container.invalidate()

,

Container.validate()

,

JComponent.revalidate()

---

#### add

public

Component

add​(

Component

c)

Appends a component to the end of this menu.
Returns the component added.

add

```java
public
Component
add​(
Component
c,
int index)
```

Adds the specified component to this container at the given
position. If

index

equals -1, the component will
be appended to the end.

**Overrides:** add

in class

Container
**Parameters:** c

- the

Component

to add
**Parameters:** index

- the position at which to insert the component
**Returns:** the

Component

added
**See Also:** remove(javax.swing.JMenuItem)

,

Container.add(Component, int)

---

#### add

public

Component

add​(

Component

c,
int index)

Adds the specified component to this container at the given
position. If

index

equals -1, the component will
be appended to the end.

add

```java
public
JMenuItem
add​(
String
s)
```

Creates a new menu item with the specified text and appends
it to the end of this menu.

**Parameters:** s

- the string for the menu item to be added
**Returns:** the new

JMenuItem

---

#### add

public

JMenuItem

add​(

String

s)

Creates a new menu item with the specified text and appends
it to the end of this menu.

add

```java
public
JMenuItem
add​(
Action
a)
```

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

**Parameters:** a

- the

Action

for the menu item to be added
**Returns:** the new

JMenuItem
**See Also:** Action

---

#### add

public

JMenuItem

add​(

Action

a)

Creates a new menu item attached to the specified

Action

object
and appends it to the end of this menu.

createActionComponent

```java
protected
JMenuItem
createActionComponent​(
Action
a)
```

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

**Parameters:** a

- the

Action

for the menu item to be added
**Returns:** the new menu item
**Since:** 1.3
**See Also:** Action

---

#### createActionComponent

protected

JMenuItem

createActionComponent​(

Action

a)

Factory method which creates the

JMenuItem

for

Action

s added to the

JMenu

.

createActionChangeListener

```java
protected
PropertyChangeListener
createActionChangeListener​(
JMenuItem
b)
```

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

**Parameters:** b

- a menu item for which to create a

PropertyChangeListener
**Returns:** a

PropertyChangeListener

for

b

---

#### createActionChangeListener

protected

PropertyChangeListener

createActionChangeListener​(

JMenuItem

b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

addSeparator

```java
public void addSeparator()
```

Appends a new separator to the end of the menu.

---

#### addSeparator

public void addSeparator()

Appends a new separator to the end of the menu.

insert

```java
public void insert​(
String
s,
int pos)
```

Inserts a new menu item with the specified text at a
given position.

**Parameters:** s

- the text for the menu item to add
**Parameters:** pos

- an integer specifying the position at which to add the
new menu item
**Throws:** IllegalArgumentException

- when the value of

pos

< 0

---

#### insert

public void insert​(

String

s,
int pos)

Inserts a new menu item with the specified text at a
given position.

insert

```java
public
JMenuItem
insert​(
JMenuItem
mi,
int pos)
```

Inserts the specified

JMenuitem

at a given position.

**Parameters:** mi

- the

JMenuitem

to add
**Parameters:** pos

- an integer specifying the position at which to add the
new

JMenuitem
**Returns:** the new menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

---

#### insert

public

JMenuItem

insert​(

JMenuItem

mi,
int pos)

Inserts the specified

JMenuitem

at a given position.

insert

```java
public
JMenuItem
insert​(
Action
a,
int pos)
```

Inserts a new menu item attached to the specified

Action

object at a given position.

**Parameters:** a

- the

Action

object for the menu item to add
**Parameters:** pos

- an integer specifying the position at which to add the
new menu item
**Returns:** the new menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

---

#### insert

public

JMenuItem

insert​(

Action

a,
int pos)

Inserts a new menu item attached to the specified

Action

object at a given position.

insertSeparator

```java
public void insertSeparator​(int index)
```

Inserts a separator at the specified position.

**Parameters:** index

- an integer specifying the position at which to
insert the menu separator
**Throws:** IllegalArgumentException

- if the value of

index

< 0

---

#### insertSeparator

public void insertSeparator​(int index)

Inserts a separator at the specified position.

getItem

```java
public
JMenuItem
getItem​(int pos)
```

Returns the

JMenuItem

at the specified position.
If the component at

pos

is not a menu item,

null

is returned.
This method is included for AWT compatibility.

**Parameters:** pos

- an integer specifying the position
**Returns:** the menu item at the specified position; or

null

if the item as the specified position is not a menu item
**Throws:** IllegalArgumentException

- if the value of

pos

< 0

---

#### getItem

public

JMenuItem

getItem​(int pos)

Returns the

JMenuItem

at the specified position.
If the component at

pos

is not a menu item,

null

is returned.
This method is included for AWT compatibility.

getItemCount

```java
@BeanProperty
(
bound
=false)
public int getItemCount()
```

Returns the number of items on the menu, including separators.
This method is included for AWT compatibility.

**Returns:** an integer equal to the number of items on the menu
**See Also:** getMenuComponentCount()

---

#### getItemCount

@BeanProperty

(

bound

=false)
public int getItemCount()

Returns the number of items on the menu, including separators.
This method is included for AWT compatibility.

isTearOff

```java
@BeanProperty
(
bound
=false)
public boolean isTearOff()
```

Returns true if the menu can be torn off. This method is not
yet implemented.

**Returns:** true if the menu can be torn off, else false
**Throws:** Error

- if invoked -- this method is not yet implemented

---

#### isTearOff

@BeanProperty

(

bound

=false)
public boolean isTearOff()

Returns true if the menu can be torn off. This method is not
yet implemented.

remove

```java
public void remove​(
JMenuItem
item)
```

Removes the specified menu item from this menu. If there is no
popup menu, this method will have no effect.

**Parameters:** item

- the

JMenuItem

to be removed from the menu

---

#### remove

public void remove​(

JMenuItem

item)

Removes the specified menu item from this menu. If there is no
popup menu, this method will have no effect.

remove

```java
public void remove​(int pos)
```

Removes the menu item at the specified index from this menu.

**Overrides:** remove

in class

Container
**Parameters:** pos

- the position of the item to be removed
**Throws:** IllegalArgumentException

- if the value of

pos

< 0, or if

pos

is greater than the number of menu items
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

---

#### remove

public void remove​(int pos)

Removes the menu item at the specified index from this menu.

remove

```java
public void remove​(
Component
c)
```

Removes the component

c

from this menu.

**Overrides:** remove

in class

Container
**Parameters:** c

- the component to be removed
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

---

#### remove

public void remove​(

Component

c)

Removes the component

c

from this menu.

removeAll

```java
public void removeAll()
```

Removes all menu items from this menu.

**Overrides:** removeAll

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

---

#### removeAll

public void removeAll()

Removes all menu items from this menu.

getMenuComponentCount

```java
@BeanProperty
(
bound
=false)
public int getMenuComponentCount()
```

Returns the number of components on the menu.

**Returns:** an integer containing the number of components on the menu

---

#### getMenuComponentCount

@BeanProperty

(

bound

=false)
public int getMenuComponentCount()

Returns the number of components on the menu.

getMenuComponent

```java
public
Component
getMenuComponent​(int n)
```

Returns the component at position

n

.

**Parameters:** n

- the position of the component to be returned
**Returns:** the component requested, or

null

if there is no popup menu

---

#### getMenuComponent

public

Component

getMenuComponent​(int n)

Returns the component at position

n

.

getMenuComponents

```java
@BeanProperty
(
bound
=false)
public
Component
[] getMenuComponents()
```

Returns an array of

Component

s of the menu's
subcomponents. Note that this returns all

Component

s
in the popup menu, including separators.

**Returns:** an array of

Component

s or an empty array
if there is no popup menu

---

#### getMenuComponents

@BeanProperty

(

bound

=false)
public

Component

[] getMenuComponents()

Returns an array of

Component

s of the menu's
subcomponents. Note that this returns all

Component

s
in the popup menu, including separators.

isTopLevelMenu

```java
@BeanProperty
(
bound
=false)
public boolean isTopLevelMenu()
```

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

**Returns:** true if the menu is activated from the menu bar;
false if the menu is activated from a menu item
on another menu

---

#### isTopLevelMenu

@BeanProperty

(

bound

=false)
public boolean isTopLevelMenu()

Returns true if the menu is a 'top-level menu', that is, if it is
the direct child of a menubar.

isMenuComponent

```java
public boolean isMenuComponent​(
Component
c)
```

Returns true if the specified component exists in the
submenu hierarchy.

**Parameters:** c

- the

Component

to be tested
**Returns:** true if the

Component

exists, false otherwise

---

#### isMenuComponent

public boolean isMenuComponent​(

Component

c)

Returns true if the specified component exists in the
submenu hierarchy.

getPopupMenu

```java
@BeanProperty
(
bound
=false)
public
JPopupMenu
getPopupMenu()
```

Returns the popupmenu associated with this menu. If there is
no popupmenu, it will create one.

**Returns:** the

JPopupMenu

associated with this menu

---

#### getPopupMenu

@BeanProperty

(

bound

=false)
public

JPopupMenu

getPopupMenu()

Returns the popupmenu associated with this menu. If there is
no popupmenu, it will create one.

addMenuListener

```java
public void addMenuListener​(
MenuListener
l)
```

Adds a listener for menu events.

**Parameters:** l

- the listener to be added

---

#### addMenuListener

public void addMenuListener​(

MenuListener

l)

Adds a listener for menu events.

removeMenuListener

```java
public void removeMenuListener​(
MenuListener
l)
```

Removes a listener for menu events.

**Parameters:** l

- the listener to be removed

---

#### removeMenuListener

public void removeMenuListener​(

MenuListener

l)

Removes a listener for menu events.

getMenuListeners

```java
@BeanProperty
(
bound
=false)
public
MenuListener
[] getMenuListeners()
```

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

**Returns:** all of the

MenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getMenuListeners

@BeanProperty

(

bound

=false)
public

MenuListener

[] getMenuListeners()

Returns an array of all the

MenuListener

s added
to this JMenu with addMenuListener().

fireMenuSelected

```java
protected void fireMenuSelected()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

---

#### fireMenuSelected

protected void fireMenuSelected()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

fireMenuDeselected

```java
protected void fireMenuDeselected()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

---

#### fireMenuDeselected

protected void fireMenuDeselected()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

fireMenuCanceled

```java
protected void fireMenuCanceled()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**Throws:** Error

- if there is a

null

listener
**See Also:** EventListenerList

---

#### fireMenuCanceled

protected void fireMenuCanceled()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

createWinListener

```java
protected
JMenu.WinListener
createWinListener​(
JPopupMenu
p)
```

Creates a window-closing listener for the popup.

**Parameters:** p

- the

JPopupMenu
**Returns:** the new window-closing listener
**See Also:** JMenu.WinListener

---

#### createWinListener

protected

JMenu.WinListener

createWinListener​(

JPopupMenu

p)

Creates a window-closing listener for the popup.

menuSelectionChanged

```java
public void menuSelectionChanged​(boolean isIncluded)
```

Messaged when the menubar selection changes to activate or
deactivate this menu.
Overrides

JMenuItem.menuSelectionChanged

.

**Specified by:** menuSelectionChanged

in interface

MenuElement
**Overrides:** menuSelectionChanged

in class

JMenuItem
**Parameters:** isIncluded

- true if this menu is active, false if
it is not
**See Also:** MenuSelectionManager.setSelectedPath(MenuElement[])

---

#### menuSelectionChanged

public void menuSelectionChanged​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu.
Overrides

JMenuItem.menuSelectionChanged

.

getSubElements

```java
@BeanProperty
(
bound
=false)
public
MenuElement
[] getSubElements()
```

Returns an array of

MenuElement

s containing the submenu
for this menu component. If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface. Note that since

JSeparator

s do not conform to the

MenuElement

interface, this array will only contain

JMenuItem

s.

**Specified by:** getSubElements

in interface

MenuElement
**Overrides:** getSubElements

in class

JMenuItem
**Returns:** an array of

MenuElement

objects

---

#### getSubElements

@BeanProperty

(

bound

=false)
public

MenuElement

[] getSubElements()

Returns an array of

MenuElement

s containing the submenu
for this menu component. If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface. Note that since

JSeparator

s do not conform to the

MenuElement

interface, this array will only contain

JMenuItem

s.

getComponent

```java
public
Component
getComponent()
```

Returns the

java.awt.Component

used to
paint this

MenuElement

.
The returned component is used to convert events and detect if
an event is inside a menu component.

**Specified by:** getComponent

in interface

MenuElement
**Overrides:** getComponent

in class

JMenuItem
**Returns:** the

Component

that paints this menu item

---

#### getComponent

public

Component

getComponent()

Returns the

java.awt.Component

used to
paint this

MenuElement

.
The returned component is used to convert events and detect if
an event is inside a menu component.

applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
o)
```

Sets the

ComponentOrientation

property of this menu
and all components contained within it. This includes all
components returned by

getMenuComponents

.

**Overrides:** applyComponentOrientation

in class

Container
**Parameters:** o

- the new component orientation of this menu and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

---

#### applyComponentOrientation

public void applyComponentOrientation​(

ComponentOrientation

o)

Sets the

ComponentOrientation

property of this menu
and all components contained within it. This includes all
components returned by

getMenuComponents

.

setAccelerator

```java
public void setAccelerator​(
KeyStroke
keyStroke)
```

setAccelerator

is not defined for

JMenu

.
Use

setMnemonic

instead.

**Overrides:** setAccelerator

in class

JMenuItem
**Parameters:** keyStroke

- the keystroke combination which will invoke
the

JMenuItem

's actionlisteners
without navigating the menu hierarchy
**Throws:** Error

- if invoked -- this method is not defined for JMenu.
Use

setMnemonic

instead

---

#### setAccelerator

public void setAccelerator​(

KeyStroke

keyStroke)

setAccelerator

is not defined for

JMenu

.
Use

setMnemonic

instead.

processKeyEvent

```java
protected void processKeyEvent​(
KeyEvent
evt)
```

Processes key stroke events such as mnemonics and accelerators.

**Overrides:** processKeyEvent

in class

JComponent
**Parameters:** evt

- the key event to be processed
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

---

#### processKeyEvent

protected void processKeyEvent​(

KeyEvent

evt)

Processes key stroke events such as mnemonics and accelerators.

doClick

```java
public void doClick​(int pressTime)
```

Programmatically performs a "click". This overrides the method

AbstractButton.doClick

in order to make the menu pop up.

**Overrides:** doClick

in class

AbstractButton
**Parameters:** pressTime

- indicates the number of milliseconds the
button was pressed for

---

#### doClick

public void doClick​(int pressTime)

Programmatically performs a "click". This overrides the method

AbstractButton.doClick

in order to make the menu pop up.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JMenu

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JMenuItem
**Returns:** a string representation of this JMenu.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JMenu

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JMenu.
For JMenus, the AccessibleContext takes the form of an
AccessibleJMenu.
A new AccessibleJMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JMenuItem
**Returns:** an AccessibleJMenu that serves as the
AccessibleContext of this JMenu

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JMenu.
For JMenus, the AccessibleContext takes the form of an
AccessibleJMenu.
A new AccessibleJMenu instance is created if necessary.

---

