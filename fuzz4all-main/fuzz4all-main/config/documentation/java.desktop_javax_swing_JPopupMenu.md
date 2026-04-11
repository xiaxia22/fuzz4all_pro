# Class JPopupMenu

**Source:** `java.desktop\javax\swing\JPopupMenu.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A small window that pops up and displays a series of choices.")
public class
JPopupMenu

extends
JComponent

implements
Accessible
,
MenuElement
```

An implementation of a popup menu -- a small window that pops up
and displays a series of choices. A

JPopupMenu

is used for the
menu that appears when the user selects an item on the menu bar.
It is also used for "pull-right" menu that appears when the
selects a menu item that activates it. Finally, a

JPopupMenu

can also be used anywhere else you want a menu to appear. For
example, when the user right-clicks in a specified area.

For information and examples of using popup menus, see

How to Use Menus

in

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

MenuContainer

,

Serializable

,

Accessible

,

MenuElement

---

### Field Details

*No entries found.*

### Constructor Details

#### public JPopupMenu()

Constructs a

JPopupMenu

without an "invoker".

---

#### public JPopupMenu​(
String
label)

Constructs a

JPopupMenu

with the specified title.

**Parameters:**
- label

- the string that a UI may use to display as a title
for the popup menu.

---

### Method Details

#### public static void setDefaultLightWeightPopupEnabled​(boolean aFlag)

Sets the default value of the

lightWeightPopupEnabled

property.

**Parameters:**
- aFlag

-

true

if popups can be lightweight,
otherwise

false

**See Also:**
- getDefaultLightWeightPopupEnabled()

,

setLightWeightPopupEnabled(boolean)

---

#### public static boolean getDefaultLightWeightPopupEnabled()

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

**Returns:**
- the value of the

defaultLightWeightPopupEnabled

property

**See Also:**
- setDefaultLightWeightPopupEnabled(boolean)

---

#### public
PopupMenuUI
getUI()

Returns the look and feel (L&F) object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

PopupMenuUI

object that renders this component

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
PopupMenuUI
ui)

Sets the L&F object that renders this component.

**Parameters:**
- ui

- the new

PopupMenuUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Resets the UI property to a value from the current look and feel.

**Overrides:**
- updateUI

in class

JComponent

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

JComponent

**Returns:**
- the string "PopupMenuUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

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

#### public
SingleSelectionModel
getSelectionModel()

Returns the model object that handles single selections.

**Returns:**
- the

selectionModel

property

**See Also:**
- SingleSelectionModel

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The selection model for the popup menu")
public void setSelectionModel​(
SingleSelectionModel
model)

Sets the model object to handle single selections.

**Parameters:**
- model

- the new

SingleSelectionModel

**See Also:**
- SingleSelectionModel

---

#### public
JMenuItem
add​(
JMenuItem
menuItem)

Appends the specified menu item to the end of this menu.

**Parameters:**
- menuItem

- the

JMenuItem

to add

**Returns:**
- the

JMenuItem

added

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
- a new

JMenuItem

created using

s

---

#### public
JMenuItem
add​(
Action
a)

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

**Parameters:**
- a

- the

Action

to add to the menu

**Returns:**
- the new menu item

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

Actions

added to the

JPopupMenu

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

- the menu item for which to create a listener

**Returns:**
- a properly configured

PropertyChangeListener

---

#### public void remove​(int pos)

Removes the component at the specified index from this popup menu.

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

< 0, or if the value of

pos

is greater than the
number of items

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="Determines whether lightweight popups are used when possible")
public void setLightWeightPopupEnabled​(boolean aFlag)

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.
By default, when a look and feel displays a popup,
it can choose to
use a lightweight (all-Java) popup.
Lightweight popup windows are more efficient than heavyweight
(native peer) windows,
but lightweight and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight components,
you should disable lightweight popups.
Some look and feels might always use heavyweight popups,
no matter what the value of this property.

**Parameters:**
- aFlag

-

false

to disable lightweight popups

**See Also:**
- isLightWeightPopupEnabled()

---

#### public boolean isLightWeightPopupEnabled()

Gets the

lightWeightPopupEnabled

property.

**Returns:**
- the value of the

lightWeightPopupEnabled

property

**See Also:**
- setLightWeightPopupEnabled(boolean)

---

#### public
String
getLabel()

Returns the popup menu's label

**Returns:**
- a string containing the popup menu's label

**See Also:**
- setLabel(java.lang.String)

---

#### @BeanProperty
(
description
="The label for the popup menu.")
public void setLabel​(
String
label)

Sets the popup menu's label. Different look and feels may choose
to display or not display this.

**Parameters:**
- label

- a string specifying the label for the popup menu

**See Also:**
- setLabel(java.lang.String)

---

#### public void addSeparator()

Appends a new separator at the end of the menu.

---

#### public void insert​(
Action
a,
int index)

Inserts a menu item for the specified

Action

object at
a given position.

**Parameters:**
- a

- the

Action

object to insert
- index

- specifies the position at which to insert the

Action

, where 0 is the first

**Throws:**
- IllegalArgumentException

- if

index

< 0

**See Also:**
- Action

---

#### public void insert​(
Component
component,
int index)

Inserts the specified component into the menu at a given
position.

**Parameters:**
- component

- the

Component

to insert
- index

- specifies the position at which
to insert the component, where 0 is the first

**Throws:**
- IllegalArgumentException

- if

index

< 0

---

#### public void addPopupMenuListener​(
PopupMenuListener
l)

Adds a

PopupMenu

listener.

**Parameters:**
- l

- the

PopupMenuListener

to add

---

#### public void removePopupMenuListener​(
PopupMenuListener
l)

Removes a

PopupMenu

listener.

**Parameters:**
- l

- the

PopupMenuListener

to remove

---

#### @BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

**Returns:**
- all of the

PopupMenuListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void addMenuKeyListener​(
MenuKeyListener
l)

Adds a

MenuKeyListener

to the popup menu.

**Parameters:**
- l

- the

MenuKeyListener

to be added

**Since:**
- 1.5

---

#### public void removeMenuKeyListener​(
MenuKeyListener
l)

Removes a

MenuKeyListener

from the popup menu.

**Parameters:**
- l

- the

MenuKeyListener

to be removed

**Since:**
- 1.5

---

#### @BeanProperty
(
bound
=false)
public
MenuKeyListener
[] getMenuKeyListeners()

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

**Returns:**
- all of the

MenuKeyListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.5

---

#### protected void firePopupMenuWillBecomeVisible()

Notifies

PopupMenuListener

s that this popup menu will
become visible.

---

#### protected void firePopupMenuWillBecomeInvisible()

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

---

#### protected void firePopupMenuCanceled()

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

---

#### public void pack()

Lays out the container so that it uses the minimum space
needed to display its contents.

---

#### @BeanProperty
(
description
="Makes the popup visible")
public void setVisible​(boolean b)

Sets the visibility of the popup menu.

**Overrides:**
- setVisible

in class

JComponent

**Parameters:**
- b

- true to make the popup visible, or false to
hide it

**See Also:**
- Component.isVisible()

,

Component.invalidate()

---

#### public boolean isVisible()

Returns true if the popup menu is visible (currently
being displayed).

**Overrides:**
- isVisible

in class

Component

**Returns:**
- true

if the component is visible,

false

otherwise

**See Also:**
- Component.setVisible(boolean)

---

#### @BeanProperty
(
description
="The location of the popup menu.")
public void setLocation​(int x,
int y)

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

JPopupMenu

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:**
- setLocation

in class

Component

**Parameters:**
- x

- the x coordinate of the popup's new position
in the screen's coordinate space
- y

- the y coordinate of the popup's new position
in the screen's coordinate space

**See Also:**
- Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

---

#### public
Component
getInvoker()

Returns the component which is the 'invoker' of this
popup menu.

**Returns:**
- the

Component

in which the popup menu is displayed

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The invoking component for the popup menu")
public void setInvoker​(
Component
invoker)

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

**Parameters:**
- invoker

- the

Component

in which the popup
menu is displayed

---

#### public void show​(
Component
invoker,
int x,
int y)

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

**Parameters:**
- invoker

- the component in whose space the popup menu is to appear
- x

- the x coordinate in invoker's coordinate space at which
the popup menu is to be displayed
- y

- the y coordinate in invoker's coordinate space at which
the popup menu is to be displayed

---

#### @Deprecated

public
Component
getComponentAtIndex​(int i)

Returns the component at the specified index.

**Parameters:**
- i

- the index of the component, where 0 is the first

**Returns:**
- the

Component

at that index

---

#### public int getComponentIndex​(
Component
c)

Returns the index of the specified component.

**Parameters:**
- c

- the

Component

to find

**Returns:**
- the index of the component, where 0 is the first;
or -1 if the component is not found

---

#### @BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(
Dimension
d)

Sets the size of the Popup window using a

Dimension

object.
This is equivalent to

setPreferredSize(d)

.

**Parameters:**
- d

- the

Dimension

specifying the new size
of this component.

---

#### @BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(int width,
int height)

Sets the size of the Popup window to the specified width and
height. This is equivalent to

setPreferredSize(new Dimension(width, height))

.

**Parameters:**
- width

- the new width of the Popup in pixels
- height

- the new height of the Popup in pixels

---

#### @BeanProperty
(
expert
=true,

hidden
=true,

description
="The selected component on the popup menu")
public void setSelected​(
Component
sel)

Sets the currently selected component, This will result
in a change to the selection model.

**Parameters:**
- sel

- the

Component

to select

---

#### public boolean isBorderPainted()

Checks whether the border should be painted.

**Returns:**
- true if the border is painted, false otherwise

**See Also:**
- setBorderPainted(boolean)

---

#### @BeanProperty
(
bound
=false,

description
="Is the border of the popup menu painted")
public void setBorderPainted​(boolean b)

Sets whether the border should be painted.

**Parameters:**
- b

- if true, the border is painted.

**See Also:**
- isBorderPainted()

---

#### protected void paintBorder​(
Graphics
g)

Paints the popup menu's border if the

borderPainted

property is

true

.

**Overrides:**
- paintBorder

in class

JComponent

**Parameters:**
- g

- the

Graphics

object

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

---

#### @BeanProperty
(
bound
=false)
public
Insets
getMargin()

Returns the margin, in pixels, between the popup menu's border and
its containers.

**Returns:**
- an

Insets

object containing the margin values.

---

#### protected
String
paramString()

Returns a string representation of this

JPopupMenu

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this

JPopupMenu

.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JPopupMenu.
For JPopupMenus, the AccessibleContext takes the form of an
AccessibleJPopupMenu.
A new AccessibleJPopupMenu instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJPopupMenu that serves as the
AccessibleContext of this JPopupMenu

---

#### public void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)

This method is required to conform to the

MenuElement

interface, but it not implemented.

**Specified by:**
- processMouseEvent

in interface

MenuElement

**Parameters:**
- event

- a

MouseEvent

to be processed
- path

- the path of the receiving element in the menu hierarchy
- manager

- the

MenuSelectionManager

for the menu hierarchy

**See Also:**
- MenuElement.processMouseEvent(MouseEvent, MenuElement[], MenuSelectionManager)

---

#### public void processKeyEvent​(
KeyEvent
e,

MenuElement
[] path,

MenuSelectionManager
manager)

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

Note: you do not have to forward the event to sub-components.
This is done automatically by the

MenuSelectionManager

.

**Specified by:**
- processKeyEvent

in interface

MenuElement

**Parameters:**
- e

- a

KeyEvent
- path

- the

MenuElement

path array
- manager

- the

MenuSelectionManager

---

#### public void menuSelectionChanged​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu. This implements the

javax.swing.MenuElement

interface.
Overrides

MenuElement.menuSelectionChanged

.

**Specified by:**
- menuSelectionChanged

in interface

MenuElement

**Parameters:**
- isIncluded

- true if this menu is active, false if
it is not

**See Also:**
- MenuElement.menuSelectionChanged(boolean)

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
for this menu component. It will only return items conforming to
the

JMenuElement

interface.
If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface.

**Specified by:**
- getSubElements

in interface

MenuElement

**Returns:**
- an array of

MenuElement

objects

**See Also:**
- MenuElement.getSubElements()

---

#### public
Component
getComponent()

Returns this

JPopupMenu

component.

**Specified by:**
- getComponent

in interface

MenuElement

**Returns:**
- this

JPopupMenu

object

**See Also:**
- MenuElement.getComponent()

---

#### public boolean isPopupTrigger​(
MouseEvent
e)

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

**Parameters:**
- e

- a

MouseEvent

**Returns:**
- true if the mouse event is a popup trigger

**Since:**
- 1.3

---

### Additional Sections

#### Class JPopupMenu

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPopupMenu

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPopupMenu

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JPopupMenu

javax.swing.JComponent

- javax.swing.JPopupMenu

javax.swing.JPopupMenu

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

MenuElement

**Direct Known Subclasses:** BasicComboPopup

```java
@JavaBean
(
defaultProperty
="UI",

description
="A small window that pops up and displays a series of choices.")
public class
JPopupMenu

extends
JComponent

implements
Accessible
,
MenuElement
```

An implementation of a popup menu -- a small window that pops up
and displays a series of choices. A

JPopupMenu

is used for the
menu that appears when the user selects an item on the menu bar.
It is also used for "pull-right" menu that appears when the
selects a menu item that activates it. Finally, a

JPopupMenu

can also be used anywhere else you want a menu to appear. For
example, when the user right-clicks in a specified area.

For information and examples of using popup menus, see

How to Use Menus

in

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
**See Also:** Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A small window that pops up and displays a series of choices.")
public class

JPopupMenu

extends

JComponent

implements

Accessible

,

MenuElement

An implementation of a popup menu -- a small window that pops up
and displays a series of choices. A

JPopupMenu

is used for the
menu that appears when the user selects an item on the menu bar.
It is also used for "pull-right" menu that appears when the
selects a menu item that activates it. Finally, a

JPopupMenu

can also be used anywhere else you want a menu to appear. For
example, when the user right-clicks in a specified area.

For information and examples of using popup menus, see

How to Use Menus

in

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

For information and examples of using popup menus, see

How to Use Menus

in

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

JPopupMenu.AccessibleJPopupMenu

This class implements accessibility support for the

JPopupMenu

class.

static class

JPopupMenu.Separator

A popup menu-specific separator.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JPopupMenu

()

Constructs a

JPopupMenu

without an "invoker".

JPopupMenu

​(

String

label)

Constructs a

JPopupMenu

with the specified title.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

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

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

JMenuItem

add

​(

JMenuItem

menuItem)

Appends the specified menu item to the end of this menu.

void

addMenuKeyListener

​(

MenuKeyListener

l)

Adds a

MenuKeyListener

to the popup menu.

void

addPopupMenuListener

​(

PopupMenuListener

l)

Adds a

PopupMenu

listener.

void

addSeparator

()

Appends a new separator at the end of the menu.

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

Actions

added to the

JPopupMenu

.

protected void

firePopupMenuCanceled

()

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

protected void

firePopupMenuWillBecomeInvisible

()

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

protected void

firePopupMenuWillBecomeVisible

()

Notifies

PopupMenuListener

s that this popup menu will
become visible.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JPopupMenu.

Component

getComponent

()

Returns this

JPopupMenu

component.

Component

getComponentAtIndex

​(int i)

Deprecated.

replaced by

Container.getComponent(int)

int

getComponentIndex

​(

Component

c)

Returns the index of the specified component.

static boolean

getDefaultLightWeightPopupEnabled

()

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

Component

getInvoker

()

Returns the component which is the 'invoker' of this
popup menu.

String

getLabel

()

Returns the popup menu's label

Insets

getMargin

()

Returns the margin, in pixels, between the popup menu's border and
its containers.

MenuKeyListener

[]

getMenuKeyListeners

()

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

PopupMenuListener

[]

getPopupMenuListeners

()

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

SingleSelectionModel

getSelectionModel

()

Returns the model object that handles single selections.

MenuElement

[]

getSubElements

()

Returns an array of

MenuElement

s containing the submenu
for this menu component.

PopupMenuUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

insert

​(

Component

component,
int index)

Inserts the specified component into the menu at a given
position.

void

insert

​(

Action

a,
int index)

Inserts a menu item for the specified

Action

object at
a given position.

boolean

isBorderPainted

()

Checks whether the border should be painted.

boolean

isLightWeightPopupEnabled

()

Gets the

lightWeightPopupEnabled

property.

boolean

isPopupTrigger

​(

MouseEvent

e)

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

boolean

isVisible

()

Returns true if the popup menu is visible (currently
being displayed).

void

menuSelectionChanged

​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu.

void

pack

()

Lays out the container so that it uses the minimum space
needed to display its contents.

protected void

paintBorder

​(

Graphics

g)

Paints the popup menu's border if the

borderPainted

property is

true

.

protected

String

paramString

()

Returns a string representation of this

JPopupMenu

.

protected void

processKeyEvent

​(

KeyEvent

evt)

Processes key stroke events such as mnemonics and accelerators.

void

processKeyEvent

​(

KeyEvent

e,

MenuElement

[] path,

MenuSelectionManager

manager)

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

void

processMouseEvent

​(

MouseEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

This method is required to conform to the

MenuElement

interface, but it not implemented.

void

remove

​(int pos)

Removes the component at the specified index from this popup menu.

void

removeMenuKeyListener

​(

MenuKeyListener

l)

Removes a

MenuKeyListener

from the popup menu.

void

removePopupMenuListener

​(

PopupMenuListener

l)

Removes a

PopupMenu

listener.

void

setBorderPainted

​(boolean b)

Sets whether the border should be painted.

static void

setDefaultLightWeightPopupEnabled

​(boolean aFlag)

Sets the default value of the

lightWeightPopupEnabled

property.

void

setInvoker

​(

Component

invoker)

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

void

setLabel

​(

String

label)

Sets the popup menu's label.

void

setLightWeightPopupEnabled

​(boolean aFlag)

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.

void

setLocation

​(int x,
int y)

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

void

setPopupSize

​(int width,
int height)

Sets the size of the Popup window to the specified width and
height.

void

setPopupSize

​(

Dimension

d)

Sets the size of the Popup window using a

Dimension

object.

void

setSelected

​(

Component

sel)

Sets the currently selected component, This will result
in a change to the selection model.

void

setSelectionModel

​(

SingleSelectionModel

model)

Sets the model object to handle single selections.

void

setUI

​(

PopupMenuUI

ui)

Sets the L&F object that renders this component.

void

setVisible

​(boolean b)

Sets the visibility of the popup menu.

void

show

​(

Component

invoker,
int x,
int y)

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

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

removeNotify

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

setEnabled

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

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

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

remove

,

removeAll

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

setLayout

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

imageUpdate

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JPopupMenu.AccessibleJPopupMenu

This class implements accessibility support for the

JPopupMenu

class.

static class

JPopupMenu.Separator

A popup menu-specific separator.

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

JPopupMenu

class.

A popup menu-specific separator.

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

---

#### Field Summary

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

Constructor Summary

Constructors

Constructor

Description

JPopupMenu

()

Constructs a

JPopupMenu

without an "invoker".

JPopupMenu

​(

String

label)

Constructs a

JPopupMenu

with the specified title.

---

#### Constructor Summary

Constructs a

JPopupMenu

without an "invoker".

Constructs a

JPopupMenu

with the specified title.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

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

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

JMenuItem

add

​(

JMenuItem

menuItem)

Appends the specified menu item to the end of this menu.

void

addMenuKeyListener

​(

MenuKeyListener

l)

Adds a

MenuKeyListener

to the popup menu.

void

addPopupMenuListener

​(

PopupMenuListener

l)

Adds a

PopupMenu

listener.

void

addSeparator

()

Appends a new separator at the end of the menu.

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

Actions

added to the

JPopupMenu

.

protected void

firePopupMenuCanceled

()

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

protected void

firePopupMenuWillBecomeInvisible

()

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

protected void

firePopupMenuWillBecomeVisible

()

Notifies

PopupMenuListener

s that this popup menu will
become visible.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JPopupMenu.

Component

getComponent

()

Returns this

JPopupMenu

component.

Component

getComponentAtIndex

​(int i)

Deprecated.

replaced by

Container.getComponent(int)

int

getComponentIndex

​(

Component

c)

Returns the index of the specified component.

static boolean

getDefaultLightWeightPopupEnabled

()

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

Component

getInvoker

()

Returns the component which is the 'invoker' of this
popup menu.

String

getLabel

()

Returns the popup menu's label

Insets

getMargin

()

Returns the margin, in pixels, between the popup menu's border and
its containers.

MenuKeyListener

[]

getMenuKeyListeners

()

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

PopupMenuListener

[]

getPopupMenuListeners

()

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

SingleSelectionModel

getSelectionModel

()

Returns the model object that handles single selections.

MenuElement

[]

getSubElements

()

Returns an array of

MenuElement

s containing the submenu
for this menu component.

PopupMenuUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

insert

​(

Component

component,
int index)

Inserts the specified component into the menu at a given
position.

void

insert

​(

Action

a,
int index)

Inserts a menu item for the specified

Action

object at
a given position.

boolean

isBorderPainted

()

Checks whether the border should be painted.

boolean

isLightWeightPopupEnabled

()

Gets the

lightWeightPopupEnabled

property.

boolean

isPopupTrigger

​(

MouseEvent

e)

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

boolean

isVisible

()

Returns true if the popup menu is visible (currently
being displayed).

void

menuSelectionChanged

​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu.

void

pack

()

Lays out the container so that it uses the minimum space
needed to display its contents.

protected void

paintBorder

​(

Graphics

g)

Paints the popup menu's border if the

borderPainted

property is

true

.

protected

String

paramString

()

Returns a string representation of this

JPopupMenu

.

protected void

processKeyEvent

​(

KeyEvent

evt)

Processes key stroke events such as mnemonics and accelerators.

void

processKeyEvent

​(

KeyEvent

e,

MenuElement

[] path,

MenuSelectionManager

manager)

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

void

processMouseEvent

​(

MouseEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

This method is required to conform to the

MenuElement

interface, but it not implemented.

void

remove

​(int pos)

Removes the component at the specified index from this popup menu.

void

removeMenuKeyListener

​(

MenuKeyListener

l)

Removes a

MenuKeyListener

from the popup menu.

void

removePopupMenuListener

​(

PopupMenuListener

l)

Removes a

PopupMenu

listener.

void

setBorderPainted

​(boolean b)

Sets whether the border should be painted.

static void

setDefaultLightWeightPopupEnabled

​(boolean aFlag)

Sets the default value of the

lightWeightPopupEnabled

property.

void

setInvoker

​(

Component

invoker)

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

void

setLabel

​(

String

label)

Sets the popup menu's label.

void

setLightWeightPopupEnabled

​(boolean aFlag)

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.

void

setLocation

​(int x,
int y)

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

void

setPopupSize

​(int width,
int height)

Sets the size of the Popup window to the specified width and
height.

void

setPopupSize

​(

Dimension

d)

Sets the size of the Popup window using a

Dimension

object.

void

setSelected

​(

Component

sel)

Sets the currently selected component, This will result
in a change to the selection model.

void

setSelectionModel

​(

SingleSelectionModel

model)

Sets the model object to handle single selections.

void

setUI

​(

PopupMenuUI

ui)

Sets the L&F object that renders this component.

void

setVisible

​(boolean b)

Sets the visibility of the popup menu.

void

show

​(

Component

invoker,
int x,
int y)

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

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

removeNotify

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

setEnabled

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

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

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

remove

,

removeAll

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

setLayout

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

imageUpdate

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

---

#### Method Summary

Creates a new menu item with the specified text and appends
it to the end of this menu.

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

Appends the specified menu item to the end of this menu.

Adds a

MenuKeyListener

to the popup menu.

Adds a

PopupMenu

listener.

Appends a new separator at the end of the menu.

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur.

Factory method which creates the

JMenuItem

for

Actions

added to the

JPopupMenu

.

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

Notifies

PopupMenuListener

s that this popup menu will
become visible.

Gets the AccessibleContext associated with this JPopupMenu.

Returns this

JPopupMenu

component.

Deprecated.

replaced by

Container.getComponent(int)

Returns the index of the specified component.

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

Returns the component which is the 'invoker' of this
popup menu.

Returns the popup menu's label

Returns the margin, in pixels, between the popup menu's border and
its containers.

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

Returns the model object that handles single selections.

Returns an array of

MenuElement

s containing the submenu
for this menu component.

Returns the look and feel (L&F) object that renders this component.

Returns the name of the L&F class that renders this component.

Inserts the specified component into the menu at a given
position.

Inserts a menu item for the specified

Action

object at
a given position.

Checks whether the border should be painted.

Gets the

lightWeightPopupEnabled

property.

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

Returns true if the popup menu is visible (currently
being displayed).

Messaged when the menubar selection changes to activate or
deactivate this menu.

Lays out the container so that it uses the minimum space
needed to display its contents.

Paints the popup menu's border if the

borderPainted

property is

true

.

Returns a string representation of this

JPopupMenu

.

Processes key stroke events such as mnemonics and accelerators.

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

This method is required to conform to the

MenuElement

interface, but it not implemented.

Removes the component at the specified index from this popup menu.

Removes a

MenuKeyListener

from the popup menu.

Removes a

PopupMenu

listener.

Sets whether the border should be painted.

Sets the default value of the

lightWeightPopupEnabled

property.

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

Sets the popup menu's label.

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

Sets the size of the Popup window to the specified width and
height.

Sets the size of the Popup window using a

Dimension

object.

Sets the currently selected component, This will result
in a change to the selection model.

Sets the model object to handle single selections.

Sets the L&F object that renders this component.

Sets the visibility of the popup menu.

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

Resets the UI property to a value from the current look and feel.

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

removeNotify

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

setEnabled

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

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

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

remove

,

removeAll

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

setLayout

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

imageUpdate

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JPopupMenu

```java
public JPopupMenu()
```

Constructs a

JPopupMenu

without an "invoker".

- JPopupMenu

```java
public JPopupMenu​(
String
label)
```

Constructs a

JPopupMenu

with the specified title.

**Parameters:** label

- the string that a UI may use to display as a title
for the popup menu.

============ METHOD DETAIL ==========

- Method Detail

- setDefaultLightWeightPopupEnabled

```java
public static void setDefaultLightWeightPopupEnabled​(boolean aFlag)
```

Sets the default value of the

lightWeightPopupEnabled

property.

**Parameters:** aFlag

-

true

if popups can be lightweight,
otherwise

false
**See Also:** getDefaultLightWeightPopupEnabled()

,

setLightWeightPopupEnabled(boolean)

- getDefaultLightWeightPopupEnabled

```java
public static boolean getDefaultLightWeightPopupEnabled()
```

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

**Returns:** the value of the

defaultLightWeightPopupEnabled

property
**See Also:** setDefaultLightWeightPopupEnabled(boolean)

- getUI

```java
public
PopupMenuUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

PopupMenuUI

object that renders this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
PopupMenuUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the new

PopupMenuUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
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

JComponent
**Returns:** the string "PopupMenuUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

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

- getSelectionModel

```java
public
SingleSelectionModel
getSelectionModel()
```

Returns the model object that handles single selections.

**Returns:** the

selectionModel

property
**See Also:** SingleSelectionModel

- setSelectionModel

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The selection model for the popup menu")
public void setSelectionModel​(
SingleSelectionModel
model)
```

Sets the model object to handle single selections.

**Parameters:** model

- the new

SingleSelectionModel
**See Also:** SingleSelectionModel

- add

```java
public
JMenuItem
add​(
JMenuItem
menuItem)
```

Appends the specified menu item to the end of this menu.

**Parameters:** menuItem

- the

JMenuItem

to add
**Returns:** the

JMenuItem

added

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
**Returns:** a new

JMenuItem

created using

s

- add

```java
public
JMenuItem
add​(
Action
a)
```

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

**Parameters:** a

- the

Action

to add to the menu
**Returns:** the new menu item
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

Actions

added to the

JPopupMenu

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

- the menu item for which to create a listener
**Returns:** a properly configured

PropertyChangeListener

- remove

```java
public void remove​(int pos)
```

Removes the component at the specified index from this popup menu.

**Overrides:** remove

in class

Container
**Parameters:** pos

- the position of the item to be removed
**Throws:** IllegalArgumentException

- if the value of

pos

< 0, or if the value of

pos

is greater than the
number of items
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

- setLightWeightPopupEnabled

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Determines whether lightweight popups are used when possible")
public void setLightWeightPopupEnabled​(boolean aFlag)
```

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.
By default, when a look and feel displays a popup,
it can choose to
use a lightweight (all-Java) popup.
Lightweight popup windows are more efficient than heavyweight
(native peer) windows,
but lightweight and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight components,
you should disable lightweight popups.
Some look and feels might always use heavyweight popups,
no matter what the value of this property.

**Parameters:** aFlag

-

false

to disable lightweight popups
**See Also:** isLightWeightPopupEnabled()

- isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Gets the

lightWeightPopupEnabled

property.

**Returns:** the value of the

lightWeightPopupEnabled

property
**See Also:** setLightWeightPopupEnabled(boolean)

- getLabel

```java
public
String
getLabel()
```

Returns the popup menu's label

**Returns:** a string containing the popup menu's label
**See Also:** setLabel(java.lang.String)

- setLabel

```java
@BeanProperty
(
description
="The label for the popup menu.")
public void setLabel​(
String
label)
```

Sets the popup menu's label. Different look and feels may choose
to display or not display this.

**Parameters:** label

- a string specifying the label for the popup menu
**See Also:** setLabel(java.lang.String)

- addSeparator

```java
public void addSeparator()
```

Appends a new separator at the end of the menu.

- insert

```java
public void insert​(
Action
a,
int index)
```

Inserts a menu item for the specified

Action

object at
a given position.

**Parameters:** a

- the

Action

object to insert
**Parameters:** index

- specifies the position at which to insert the

Action

, where 0 is the first
**Throws:** IllegalArgumentException

- if

index

< 0
**See Also:** Action

- insert

```java
public void insert​(
Component
component,
int index)
```

Inserts the specified component into the menu at a given
position.

**Parameters:** component

- the

Component

to insert
**Parameters:** index

- specifies the position at which
to insert the component, where 0 is the first
**Throws:** IllegalArgumentException

- if

index

< 0

- addPopupMenuListener

```java
public void addPopupMenuListener​(
PopupMenuListener
l)
```

Adds a

PopupMenu

listener.

**Parameters:** l

- the

PopupMenuListener

to add

- removePopupMenuListener

```java
public void removePopupMenuListener​(
PopupMenuListener
l)
```

Removes a

PopupMenu

listener.

**Parameters:** l

- the

PopupMenuListener

to remove

- getPopupMenuListeners

```java
@BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()
```

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

**Returns:** all of the

PopupMenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addMenuKeyListener

```java
public void addMenuKeyListener​(
MenuKeyListener
l)
```

Adds a

MenuKeyListener

to the popup menu.

**Parameters:** l

- the

MenuKeyListener

to be added
**Since:** 1.5

- removeMenuKeyListener

```java
public void removeMenuKeyListener​(
MenuKeyListener
l)
```

Removes a

MenuKeyListener

from the popup menu.

**Parameters:** l

- the

MenuKeyListener

to be removed
**Since:** 1.5

- getMenuKeyListeners

```java
@BeanProperty
(
bound
=false)
public
MenuKeyListener
[] getMenuKeyListeners()
```

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

**Returns:** all of the

MenuKeyListener

s added or an empty
array if no listeners have been added
**Since:** 1.5

- firePopupMenuWillBecomeVisible

```java
protected void firePopupMenuWillBecomeVisible()
```

Notifies

PopupMenuListener

s that this popup menu will
become visible.

- firePopupMenuWillBecomeInvisible

```java
protected void firePopupMenuWillBecomeInvisible()
```

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

- firePopupMenuCanceled

```java
protected void firePopupMenuCanceled()
```

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

- pack

```java
public void pack()
```

Lays out the container so that it uses the minimum space
needed to display its contents.

- setVisible

```java
@BeanProperty
(
description
="Makes the popup visible")
public void setVisible​(boolean b)
```

Sets the visibility of the popup menu.

**Overrides:** setVisible

in class

JComponent
**Parameters:** b

- true to make the popup visible, or false to
hide it
**See Also:** Component.isVisible()

,

Component.invalidate()

- isVisible

```java
public boolean isVisible()
```

Returns true if the popup menu is visible (currently
being displayed).

**Overrides:** isVisible

in class

Component
**Returns:** true

if the component is visible,

false

otherwise
**See Also:** Component.setVisible(boolean)

- setLocation

```java
@BeanProperty
(
description
="The location of the popup menu.")
public void setLocation​(int x,
int y)
```

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

JPopupMenu

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** x

- the x coordinate of the popup's new position
in the screen's coordinate space
**Parameters:** y

- the y coordinate of the popup's new position
in the screen's coordinate space
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

- getInvoker

```java
public
Component
getInvoker()
```

Returns the component which is the 'invoker' of this
popup menu.

**Returns:** the

Component

in which the popup menu is displayed

- setInvoker

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The invoking component for the popup menu")
public void setInvoker​(
Component
invoker)
```

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

**Parameters:** invoker

- the

Component

in which the popup
menu is displayed

- show

```java
public void show​(
Component
invoker,
int x,
int y)
```

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

**Parameters:** invoker

- the component in whose space the popup menu is to appear
**Parameters:** x

- the x coordinate in invoker's coordinate space at which
the popup menu is to be displayed
**Parameters:** y

- the y coordinate in invoker's coordinate space at which
the popup menu is to be displayed

- getComponentAtIndex

```java
@Deprecated

public
Component
getComponentAtIndex​(int i)
```

Deprecated.

replaced by

Container.getComponent(int)

Returns the component at the specified index.

**Parameters:** i

- the index of the component, where 0 is the first
**Returns:** the

Component

at that index

- getComponentIndex

```java
public int getComponentIndex​(
Component
c)
```

Returns the index of the specified component.

**Parameters:** c

- the

Component

to find
**Returns:** the index of the component, where 0 is the first;
or -1 if the component is not found

- setPopupSize

```java
@BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(
Dimension
d)
```

Sets the size of the Popup window using a

Dimension

object.
This is equivalent to

setPreferredSize(d)

.

**Parameters:** d

- the

Dimension

specifying the new size
of this component.

- setPopupSize

```java
@BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(int width,
int height)
```

Sets the size of the Popup window to the specified width and
height. This is equivalent to

setPreferredSize(new Dimension(width, height))

.

**Parameters:** width

- the new width of the Popup in pixels
**Parameters:** height

- the new height of the Popup in pixels

- setSelected

```java
@BeanProperty
(
expert
=true,

hidden
=true,

description
="The selected component on the popup menu")
public void setSelected​(
Component
sel)
```

Sets the currently selected component, This will result
in a change to the selection model.

**Parameters:** sel

- the

Component

to select

- isBorderPainted

```java
public boolean isBorderPainted()
```

Checks whether the border should be painted.

**Returns:** true if the border is painted, false otherwise
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
bound
=false,

description
="Is the border of the popup menu painted")
public void setBorderPainted​(boolean b)
```

Sets whether the border should be painted.

**Parameters:** b

- if true, the border is painted.
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the popup menu's border if the

borderPainted

property is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

object
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

- getMargin

```java
@BeanProperty
(
bound
=false)
public
Insets
getMargin()
```

Returns the margin, in pixels, between the popup menu's border and
its containers.

**Returns:** an

Insets

object containing the margin values.

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JPopupMenu

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JPopupMenu

.

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

Gets the AccessibleContext associated with this JPopupMenu.
For JPopupMenus, the AccessibleContext takes the form of an
AccessibleJPopupMenu.
A new AccessibleJPopupMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJPopupMenu that serves as the
AccessibleContext of this JPopupMenu

- processMouseEvent

```java
public void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

This method is required to conform to the

MenuElement

interface, but it not implemented.

**Specified by:** processMouseEvent

in interface

MenuElement
**Parameters:** event

- a

MouseEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy
**See Also:** MenuElement.processMouseEvent(MouseEvent, MenuElement[], MenuSelectionManager)

- processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

Note: you do not have to forward the event to sub-components.
This is done automatically by the

MenuSelectionManager

.

**Specified by:** processKeyEvent

in interface

MenuElement
**Parameters:** e

- a

KeyEvent
**Parameters:** path

- the

MenuElement

path array
**Parameters:** manager

- the

MenuSelectionManager

- menuSelectionChanged

```java
public void menuSelectionChanged​(boolean isIncluded)
```

Messaged when the menubar selection changes to activate or
deactivate this menu. This implements the

javax.swing.MenuElement

interface.
Overrides

MenuElement.menuSelectionChanged

.

**Specified by:** menuSelectionChanged

in interface

MenuElement
**Parameters:** isIncluded

- true if this menu is active, false if
it is not
**See Also:** MenuElement.menuSelectionChanged(boolean)

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
for this menu component. It will only return items conforming to
the

JMenuElement

interface.
If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface.

**Specified by:** getSubElements

in interface

MenuElement
**Returns:** an array of

MenuElement

objects
**See Also:** MenuElement.getSubElements()

- getComponent

```java
public
Component
getComponent()
```

Returns this

JPopupMenu

component.

**Specified by:** getComponent

in interface

MenuElement
**Returns:** this

JPopupMenu

object
**See Also:** MenuElement.getComponent()

- isPopupTrigger

```java
public boolean isPopupTrigger​(
MouseEvent
e)
```

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

**Parameters:** e

- a

MouseEvent
**Returns:** true if the mouse event is a popup trigger
**Since:** 1.3

Constructor Detail

- JPopupMenu

```java
public JPopupMenu()
```

Constructs a

JPopupMenu

without an "invoker".

- JPopupMenu

```java
public JPopupMenu​(
String
label)
```

Constructs a

JPopupMenu

with the specified title.

**Parameters:** label

- the string that a UI may use to display as a title
for the popup menu.

---

#### Constructor Detail

JPopupMenu

```java
public JPopupMenu()
```

Constructs a

JPopupMenu

without an "invoker".

---

#### JPopupMenu

public JPopupMenu()

Constructs a

JPopupMenu

without an "invoker".

JPopupMenu

```java
public JPopupMenu​(
String
label)
```

Constructs a

JPopupMenu

with the specified title.

**Parameters:** label

- the string that a UI may use to display as a title
for the popup menu.

---

#### JPopupMenu

public JPopupMenu​(

String

label)

Constructs a

JPopupMenu

with the specified title.

Method Detail

- setDefaultLightWeightPopupEnabled

```java
public static void setDefaultLightWeightPopupEnabled​(boolean aFlag)
```

Sets the default value of the

lightWeightPopupEnabled

property.

**Parameters:** aFlag

-

true

if popups can be lightweight,
otherwise

false
**See Also:** getDefaultLightWeightPopupEnabled()

,

setLightWeightPopupEnabled(boolean)

- getDefaultLightWeightPopupEnabled

```java
public static boolean getDefaultLightWeightPopupEnabled()
```

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

**Returns:** the value of the

defaultLightWeightPopupEnabled

property
**See Also:** setDefaultLightWeightPopupEnabled(boolean)

- getUI

```java
public
PopupMenuUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

PopupMenuUI

object that renders this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
PopupMenuUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the new

PopupMenuUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
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

JComponent
**Returns:** the string "PopupMenuUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

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

- getSelectionModel

```java
public
SingleSelectionModel
getSelectionModel()
```

Returns the model object that handles single selections.

**Returns:** the

selectionModel

property
**See Also:** SingleSelectionModel

- setSelectionModel

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The selection model for the popup menu")
public void setSelectionModel​(
SingleSelectionModel
model)
```

Sets the model object to handle single selections.

**Parameters:** model

- the new

SingleSelectionModel
**See Also:** SingleSelectionModel

- add

```java
public
JMenuItem
add​(
JMenuItem
menuItem)
```

Appends the specified menu item to the end of this menu.

**Parameters:** menuItem

- the

JMenuItem

to add
**Returns:** the

JMenuItem

added

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
**Returns:** a new

JMenuItem

created using

s

- add

```java
public
JMenuItem
add​(
Action
a)
```

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

**Parameters:** a

- the

Action

to add to the menu
**Returns:** the new menu item
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

Actions

added to the

JPopupMenu

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

- the menu item for which to create a listener
**Returns:** a properly configured

PropertyChangeListener

- remove

```java
public void remove​(int pos)
```

Removes the component at the specified index from this popup menu.

**Overrides:** remove

in class

Container
**Parameters:** pos

- the position of the item to be removed
**Throws:** IllegalArgumentException

- if the value of

pos

< 0, or if the value of

pos

is greater than the
number of items
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

- setLightWeightPopupEnabled

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Determines whether lightweight popups are used when possible")
public void setLightWeightPopupEnabled​(boolean aFlag)
```

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.
By default, when a look and feel displays a popup,
it can choose to
use a lightweight (all-Java) popup.
Lightweight popup windows are more efficient than heavyweight
(native peer) windows,
but lightweight and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight components,
you should disable lightweight popups.
Some look and feels might always use heavyweight popups,
no matter what the value of this property.

**Parameters:** aFlag

-

false

to disable lightweight popups
**See Also:** isLightWeightPopupEnabled()

- isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Gets the

lightWeightPopupEnabled

property.

**Returns:** the value of the

lightWeightPopupEnabled

property
**See Also:** setLightWeightPopupEnabled(boolean)

- getLabel

```java
public
String
getLabel()
```

Returns the popup menu's label

**Returns:** a string containing the popup menu's label
**See Also:** setLabel(java.lang.String)

- setLabel

```java
@BeanProperty
(
description
="The label for the popup menu.")
public void setLabel​(
String
label)
```

Sets the popup menu's label. Different look and feels may choose
to display or not display this.

**Parameters:** label

- a string specifying the label for the popup menu
**See Also:** setLabel(java.lang.String)

- addSeparator

```java
public void addSeparator()
```

Appends a new separator at the end of the menu.

- insert

```java
public void insert​(
Action
a,
int index)
```

Inserts a menu item for the specified

Action

object at
a given position.

**Parameters:** a

- the

Action

object to insert
**Parameters:** index

- specifies the position at which to insert the

Action

, where 0 is the first
**Throws:** IllegalArgumentException

- if

index

< 0
**See Also:** Action

- insert

```java
public void insert​(
Component
component,
int index)
```

Inserts the specified component into the menu at a given
position.

**Parameters:** component

- the

Component

to insert
**Parameters:** index

- specifies the position at which
to insert the component, where 0 is the first
**Throws:** IllegalArgumentException

- if

index

< 0

- addPopupMenuListener

```java
public void addPopupMenuListener​(
PopupMenuListener
l)
```

Adds a

PopupMenu

listener.

**Parameters:** l

- the

PopupMenuListener

to add

- removePopupMenuListener

```java
public void removePopupMenuListener​(
PopupMenuListener
l)
```

Removes a

PopupMenu

listener.

**Parameters:** l

- the

PopupMenuListener

to remove

- getPopupMenuListeners

```java
@BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()
```

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

**Returns:** all of the

PopupMenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addMenuKeyListener

```java
public void addMenuKeyListener​(
MenuKeyListener
l)
```

Adds a

MenuKeyListener

to the popup menu.

**Parameters:** l

- the

MenuKeyListener

to be added
**Since:** 1.5

- removeMenuKeyListener

```java
public void removeMenuKeyListener​(
MenuKeyListener
l)
```

Removes a

MenuKeyListener

from the popup menu.

**Parameters:** l

- the

MenuKeyListener

to be removed
**Since:** 1.5

- getMenuKeyListeners

```java
@BeanProperty
(
bound
=false)
public
MenuKeyListener
[] getMenuKeyListeners()
```

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

**Returns:** all of the

MenuKeyListener

s added or an empty
array if no listeners have been added
**Since:** 1.5

- firePopupMenuWillBecomeVisible

```java
protected void firePopupMenuWillBecomeVisible()
```

Notifies

PopupMenuListener

s that this popup menu will
become visible.

- firePopupMenuWillBecomeInvisible

```java
protected void firePopupMenuWillBecomeInvisible()
```

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

- firePopupMenuCanceled

```java
protected void firePopupMenuCanceled()
```

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

- pack

```java
public void pack()
```

Lays out the container so that it uses the minimum space
needed to display its contents.

- setVisible

```java
@BeanProperty
(
description
="Makes the popup visible")
public void setVisible​(boolean b)
```

Sets the visibility of the popup menu.

**Overrides:** setVisible

in class

JComponent
**Parameters:** b

- true to make the popup visible, or false to
hide it
**See Also:** Component.isVisible()

,

Component.invalidate()

- isVisible

```java
public boolean isVisible()
```

Returns true if the popup menu is visible (currently
being displayed).

**Overrides:** isVisible

in class

Component
**Returns:** true

if the component is visible,

false

otherwise
**See Also:** Component.setVisible(boolean)

- setLocation

```java
@BeanProperty
(
description
="The location of the popup menu.")
public void setLocation​(int x,
int y)
```

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

JPopupMenu

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** x

- the x coordinate of the popup's new position
in the screen's coordinate space
**Parameters:** y

- the y coordinate of the popup's new position
in the screen's coordinate space
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

- getInvoker

```java
public
Component
getInvoker()
```

Returns the component which is the 'invoker' of this
popup menu.

**Returns:** the

Component

in which the popup menu is displayed

- setInvoker

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The invoking component for the popup menu")
public void setInvoker​(
Component
invoker)
```

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

**Parameters:** invoker

- the

Component

in which the popup
menu is displayed

- show

```java
public void show​(
Component
invoker,
int x,
int y)
```

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

**Parameters:** invoker

- the component in whose space the popup menu is to appear
**Parameters:** x

- the x coordinate in invoker's coordinate space at which
the popup menu is to be displayed
**Parameters:** y

- the y coordinate in invoker's coordinate space at which
the popup menu is to be displayed

- getComponentAtIndex

```java
@Deprecated

public
Component
getComponentAtIndex​(int i)
```

Deprecated.

replaced by

Container.getComponent(int)

Returns the component at the specified index.

**Parameters:** i

- the index of the component, where 0 is the first
**Returns:** the

Component

at that index

- getComponentIndex

```java
public int getComponentIndex​(
Component
c)
```

Returns the index of the specified component.

**Parameters:** c

- the

Component

to find
**Returns:** the index of the component, where 0 is the first;
or -1 if the component is not found

- setPopupSize

```java
@BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(
Dimension
d)
```

Sets the size of the Popup window using a

Dimension

object.
This is equivalent to

setPreferredSize(d)

.

**Parameters:** d

- the

Dimension

specifying the new size
of this component.

- setPopupSize

```java
@BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(int width,
int height)
```

Sets the size of the Popup window to the specified width and
height. This is equivalent to

setPreferredSize(new Dimension(width, height))

.

**Parameters:** width

- the new width of the Popup in pixels
**Parameters:** height

- the new height of the Popup in pixels

- setSelected

```java
@BeanProperty
(
expert
=true,

hidden
=true,

description
="The selected component on the popup menu")
public void setSelected​(
Component
sel)
```

Sets the currently selected component, This will result
in a change to the selection model.

**Parameters:** sel

- the

Component

to select

- isBorderPainted

```java
public boolean isBorderPainted()
```

Checks whether the border should be painted.

**Returns:** true if the border is painted, false otherwise
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
bound
=false,

description
="Is the border of the popup menu painted")
public void setBorderPainted​(boolean b)
```

Sets whether the border should be painted.

**Parameters:** b

- if true, the border is painted.
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the popup menu's border if the

borderPainted

property is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

object
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

- getMargin

```java
@BeanProperty
(
bound
=false)
public
Insets
getMargin()
```

Returns the margin, in pixels, between the popup menu's border and
its containers.

**Returns:** an

Insets

object containing the margin values.

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JPopupMenu

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JPopupMenu

.

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

Gets the AccessibleContext associated with this JPopupMenu.
For JPopupMenus, the AccessibleContext takes the form of an
AccessibleJPopupMenu.
A new AccessibleJPopupMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJPopupMenu that serves as the
AccessibleContext of this JPopupMenu

- processMouseEvent

```java
public void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

This method is required to conform to the

MenuElement

interface, but it not implemented.

**Specified by:** processMouseEvent

in interface

MenuElement
**Parameters:** event

- a

MouseEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy
**See Also:** MenuElement.processMouseEvent(MouseEvent, MenuElement[], MenuSelectionManager)

- processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

Note: you do not have to forward the event to sub-components.
This is done automatically by the

MenuSelectionManager

.

**Specified by:** processKeyEvent

in interface

MenuElement
**Parameters:** e

- a

KeyEvent
**Parameters:** path

- the

MenuElement

path array
**Parameters:** manager

- the

MenuSelectionManager

- menuSelectionChanged

```java
public void menuSelectionChanged​(boolean isIncluded)
```

Messaged when the menubar selection changes to activate or
deactivate this menu. This implements the

javax.swing.MenuElement

interface.
Overrides

MenuElement.menuSelectionChanged

.

**Specified by:** menuSelectionChanged

in interface

MenuElement
**Parameters:** isIncluded

- true if this menu is active, false if
it is not
**See Also:** MenuElement.menuSelectionChanged(boolean)

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
for this menu component. It will only return items conforming to
the

JMenuElement

interface.
If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface.

**Specified by:** getSubElements

in interface

MenuElement
**Returns:** an array of

MenuElement

objects
**See Also:** MenuElement.getSubElements()

- getComponent

```java
public
Component
getComponent()
```

Returns this

JPopupMenu

component.

**Specified by:** getComponent

in interface

MenuElement
**Returns:** this

JPopupMenu

object
**See Also:** MenuElement.getComponent()

- isPopupTrigger

```java
public boolean isPopupTrigger​(
MouseEvent
e)
```

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

**Parameters:** e

- a

MouseEvent
**Returns:** true if the mouse event is a popup trigger
**Since:** 1.3

---

#### Method Detail

setDefaultLightWeightPopupEnabled

```java
public static void setDefaultLightWeightPopupEnabled​(boolean aFlag)
```

Sets the default value of the

lightWeightPopupEnabled

property.

**Parameters:** aFlag

-

true

if popups can be lightweight,
otherwise

false
**See Also:** getDefaultLightWeightPopupEnabled()

,

setLightWeightPopupEnabled(boolean)

---

#### setDefaultLightWeightPopupEnabled

public static void setDefaultLightWeightPopupEnabled​(boolean aFlag)

Sets the default value of the

lightWeightPopupEnabled

property.

getDefaultLightWeightPopupEnabled

```java
public static boolean getDefaultLightWeightPopupEnabled()
```

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

**Returns:** the value of the

defaultLightWeightPopupEnabled

property
**See Also:** setDefaultLightWeightPopupEnabled(boolean)

---

#### getDefaultLightWeightPopupEnabled

public static boolean getDefaultLightWeightPopupEnabled()

Gets the

defaultLightWeightPopupEnabled

property,
which by default is

true

.

getUI

```java
public
PopupMenuUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

PopupMenuUI

object that renders this component

---

#### getUI

public

PopupMenuUI

getUI()

Returns the look and feel (L&F) object that renders this component.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
PopupMenuUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the new

PopupMenuUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(

PopupMenuUI

ui)

Sets the L&F object that renders this component.

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look and feel.

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

JComponent
**Returns:** the string "PopupMenuUI"
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

getSelectionModel

```java
public
SingleSelectionModel
getSelectionModel()
```

Returns the model object that handles single selections.

**Returns:** the

selectionModel

property
**See Also:** SingleSelectionModel

---

#### getSelectionModel

public

SingleSelectionModel

getSelectionModel()

Returns the model object that handles single selections.

setSelectionModel

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The selection model for the popup menu")
public void setSelectionModel​(
SingleSelectionModel
model)
```

Sets the model object to handle single selections.

**Parameters:** model

- the new

SingleSelectionModel
**See Also:** SingleSelectionModel

---

#### setSelectionModel

@BeanProperty

(

bound

=false,

expert

=true,

description

="The selection model for the popup menu")
public void setSelectionModel​(

SingleSelectionModel

model)

Sets the model object to handle single selections.

add

```java
public
JMenuItem
add​(
JMenuItem
menuItem)
```

Appends the specified menu item to the end of this menu.

**Parameters:** menuItem

- the

JMenuItem

to add
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

Appends the specified menu item to the end of this menu.

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
**Returns:** a new

JMenuItem

created using

s

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

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

**Parameters:** a

- the

Action

to add to the menu
**Returns:** the new menu item
**See Also:** Action

---

#### add

public

JMenuItem

add​(

Action

a)

Appends a new menu item to the end of the menu which
dispatches the specified

Action

object.

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

Actions

added to the

JPopupMenu

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

Actions

added to the

JPopupMenu

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

- the menu item for which to create a listener
**Returns:** a properly configured

PropertyChangeListener

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

remove

```java
public void remove​(int pos)
```

Removes the component at the specified index from this popup menu.

**Overrides:** remove

in class

Container
**Parameters:** pos

- the position of the item to be removed
**Throws:** IllegalArgumentException

- if the value of

pos

< 0, or if the value of

pos

is greater than the
number of items
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

Removes the component at the specified index from this popup menu.

setLightWeightPopupEnabled

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Determines whether lightweight popups are used when possible")
public void setLightWeightPopupEnabled​(boolean aFlag)
```

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.
By default, when a look and feel displays a popup,
it can choose to
use a lightweight (all-Java) popup.
Lightweight popup windows are more efficient than heavyweight
(native peer) windows,
but lightweight and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight components,
you should disable lightweight popups.
Some look and feels might always use heavyweight popups,
no matter what the value of this property.

**Parameters:** aFlag

-

false

to disable lightweight popups
**See Also:** isLightWeightPopupEnabled()

---

#### setLightWeightPopupEnabled

@BeanProperty

(

bound

=false,

expert

=true,

description

="Determines whether lightweight popups are used when possible")
public void setLightWeightPopupEnabled​(boolean aFlag)

Sets the value of the

lightWeightPopupEnabled

property,
which by default is

true

.
By default, when a look and feel displays a popup,
it can choose to
use a lightweight (all-Java) popup.
Lightweight popup windows are more efficient than heavyweight
(native peer) windows,
but lightweight and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight components,
you should disable lightweight popups.
Some look and feels might always use heavyweight popups,
no matter what the value of this property.

isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Gets the

lightWeightPopupEnabled

property.

**Returns:** the value of the

lightWeightPopupEnabled

property
**See Also:** setLightWeightPopupEnabled(boolean)

---

#### isLightWeightPopupEnabled

public boolean isLightWeightPopupEnabled()

Gets the

lightWeightPopupEnabled

property.

getLabel

```java
public
String
getLabel()
```

Returns the popup menu's label

**Returns:** a string containing the popup menu's label
**See Also:** setLabel(java.lang.String)

---

#### getLabel

public

String

getLabel()

Returns the popup menu's label

setLabel

```java
@BeanProperty
(
description
="The label for the popup menu.")
public void setLabel​(
String
label)
```

Sets the popup menu's label. Different look and feels may choose
to display or not display this.

**Parameters:** label

- a string specifying the label for the popup menu
**See Also:** setLabel(java.lang.String)

---

#### setLabel

@BeanProperty

(

description

="The label for the popup menu.")
public void setLabel​(

String

label)

Sets the popup menu's label. Different look and feels may choose
to display or not display this.

addSeparator

```java
public void addSeparator()
```

Appends a new separator at the end of the menu.

---

#### addSeparator

public void addSeparator()

Appends a new separator at the end of the menu.

insert

```java
public void insert​(
Action
a,
int index)
```

Inserts a menu item for the specified

Action

object at
a given position.

**Parameters:** a

- the

Action

object to insert
**Parameters:** index

- specifies the position at which to insert the

Action

, where 0 is the first
**Throws:** IllegalArgumentException

- if

index

< 0
**See Also:** Action

---

#### insert

public void insert​(

Action

a,
int index)

Inserts a menu item for the specified

Action

object at
a given position.

insert

```java
public void insert​(
Component
component,
int index)
```

Inserts the specified component into the menu at a given
position.

**Parameters:** component

- the

Component

to insert
**Parameters:** index

- specifies the position at which
to insert the component, where 0 is the first
**Throws:** IllegalArgumentException

- if

index

< 0

---

#### insert

public void insert​(

Component

component,
int index)

Inserts the specified component into the menu at a given
position.

addPopupMenuListener

```java
public void addPopupMenuListener​(
PopupMenuListener
l)
```

Adds a

PopupMenu

listener.

**Parameters:** l

- the

PopupMenuListener

to add

---

#### addPopupMenuListener

public void addPopupMenuListener​(

PopupMenuListener

l)

Adds a

PopupMenu

listener.

removePopupMenuListener

```java
public void removePopupMenuListener​(
PopupMenuListener
l)
```

Removes a

PopupMenu

listener.

**Parameters:** l

- the

PopupMenuListener

to remove

---

#### removePopupMenuListener

public void removePopupMenuListener​(

PopupMenuListener

l)

Removes a

PopupMenu

listener.

getPopupMenuListeners

```java
@BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()
```

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

**Returns:** all of the

PopupMenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getPopupMenuListeners

@BeanProperty

(

bound

=false)
public

PopupMenuListener

[] getPopupMenuListeners()

Returns an array of all the

PopupMenuListener

s added
to this JMenuItem with addPopupMenuListener().

addMenuKeyListener

```java
public void addMenuKeyListener​(
MenuKeyListener
l)
```

Adds a

MenuKeyListener

to the popup menu.

**Parameters:** l

- the

MenuKeyListener

to be added
**Since:** 1.5

---

#### addMenuKeyListener

public void addMenuKeyListener​(

MenuKeyListener

l)

Adds a

MenuKeyListener

to the popup menu.

removeMenuKeyListener

```java
public void removeMenuKeyListener​(
MenuKeyListener
l)
```

Removes a

MenuKeyListener

from the popup menu.

**Parameters:** l

- the

MenuKeyListener

to be removed
**Since:** 1.5

---

#### removeMenuKeyListener

public void removeMenuKeyListener​(

MenuKeyListener

l)

Removes a

MenuKeyListener

from the popup menu.

getMenuKeyListeners

```java
@BeanProperty
(
bound
=false)
public
MenuKeyListener
[] getMenuKeyListeners()
```

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

**Returns:** all of the

MenuKeyListener

s added or an empty
array if no listeners have been added
**Since:** 1.5

---

#### getMenuKeyListeners

@BeanProperty

(

bound

=false)
public

MenuKeyListener

[] getMenuKeyListeners()

Returns an array of all the

MenuKeyListener

s added
to this JPopupMenu with addMenuKeyListener().

firePopupMenuWillBecomeVisible

```java
protected void firePopupMenuWillBecomeVisible()
```

Notifies

PopupMenuListener

s that this popup menu will
become visible.

---

#### firePopupMenuWillBecomeVisible

protected void firePopupMenuWillBecomeVisible()

Notifies

PopupMenuListener

s that this popup menu will
become visible.

firePopupMenuWillBecomeInvisible

```java
protected void firePopupMenuWillBecomeInvisible()
```

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

---

#### firePopupMenuWillBecomeInvisible

protected void firePopupMenuWillBecomeInvisible()

Notifies

PopupMenuListener

s that this popup menu will
become invisible.

firePopupMenuCanceled

```java
protected void firePopupMenuCanceled()
```

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

---

#### firePopupMenuCanceled

protected void firePopupMenuCanceled()

Notifies

PopupMenuListeners

that this popup menu is
cancelled.

pack

```java
public void pack()
```

Lays out the container so that it uses the minimum space
needed to display its contents.

---

#### pack

public void pack()

Lays out the container so that it uses the minimum space
needed to display its contents.

setVisible

```java
@BeanProperty
(
description
="Makes the popup visible")
public void setVisible​(boolean b)
```

Sets the visibility of the popup menu.

**Overrides:** setVisible

in class

JComponent
**Parameters:** b

- true to make the popup visible, or false to
hide it
**See Also:** Component.isVisible()

,

Component.invalidate()

---

#### setVisible

@BeanProperty

(

description

="Makes the popup visible")
public void setVisible​(boolean b)

Sets the visibility of the popup menu.

isVisible

```java
public boolean isVisible()
```

Returns true if the popup menu is visible (currently
being displayed).

**Overrides:** isVisible

in class

Component
**Returns:** true

if the component is visible,

false

otherwise
**See Also:** Component.setVisible(boolean)

---

#### isVisible

public boolean isVisible()

Returns true if the popup menu is visible (currently
being displayed).

setLocation

```java
@BeanProperty
(
description
="The location of the popup menu.")
public void setLocation​(int x,
int y)
```

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

JPopupMenu

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** x

- the x coordinate of the popup's new position
in the screen's coordinate space
**Parameters:** y

- the y coordinate of the popup's new position
in the screen's coordinate space
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

---

#### setLocation

@BeanProperty

(

description

="The location of the popup menu.")
public void setLocation​(int x,
int y)

Sets the location of the upper left corner of the
popup menu using x, y coordinates.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

JPopupMenu

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

JPopupMenu

object is placed and sized
in a way that corresponds closely to the desktop settings.

getInvoker

```java
public
Component
getInvoker()
```

Returns the component which is the 'invoker' of this
popup menu.

**Returns:** the

Component

in which the popup menu is displayed

---

#### getInvoker

public

Component

getInvoker()

Returns the component which is the 'invoker' of this
popup menu.

setInvoker

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The invoking component for the popup menu")
public void setInvoker​(
Component
invoker)
```

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

**Parameters:** invoker

- the

Component

in which the popup
menu is displayed

---

#### setInvoker

@BeanProperty

(

bound

=false,

expert

=true,

description

="The invoking component for the popup menu")
public void setInvoker​(

Component

invoker)

Sets the invoker of this popup menu -- the component in which
the popup menu menu is to be displayed.

show

```java
public void show​(
Component
invoker,
int x,
int y)
```

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

**Parameters:** invoker

- the component in whose space the popup menu is to appear
**Parameters:** x

- the x coordinate in invoker's coordinate space at which
the popup menu is to be displayed
**Parameters:** y

- the y coordinate in invoker's coordinate space at which
the popup menu is to be displayed

---

#### show

public void show​(

Component

invoker,
int x,
int y)

Displays the popup menu at the position x,y in the coordinate
space of the component invoker.

getComponentAtIndex

```java
@Deprecated

public
Component
getComponentAtIndex​(int i)
```

Deprecated.

replaced by

Container.getComponent(int)

Returns the component at the specified index.

**Parameters:** i

- the index of the component, where 0 is the first
**Returns:** the

Component

at that index

---

#### getComponentAtIndex

@Deprecated

public

Component

getComponentAtIndex​(int i)

Returns the component at the specified index.

getComponentIndex

```java
public int getComponentIndex​(
Component
c)
```

Returns the index of the specified component.

**Parameters:** c

- the

Component

to find
**Returns:** the index of the component, where 0 is the first;
or -1 if the component is not found

---

#### getComponentIndex

public int getComponentIndex​(

Component

c)

Returns the index of the specified component.

setPopupSize

```java
@BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(
Dimension
d)
```

Sets the size of the Popup window using a

Dimension

object.
This is equivalent to

setPreferredSize(d)

.

**Parameters:** d

- the

Dimension

specifying the new size
of this component.

---

#### setPopupSize

@BeanProperty

(

description

="The size of the popup menu")
public void setPopupSize​(

Dimension

d)

Sets the size of the Popup window using a

Dimension

object.
This is equivalent to

setPreferredSize(d)

.

setPopupSize

```java
@BeanProperty
(
description
="The size of the popup menu")
public void setPopupSize​(int width,
int height)
```

Sets the size of the Popup window to the specified width and
height. This is equivalent to

setPreferredSize(new Dimension(width, height))

.

**Parameters:** width

- the new width of the Popup in pixels
**Parameters:** height

- the new height of the Popup in pixels

---

#### setPopupSize

@BeanProperty

(

description

="The size of the popup menu")
public void setPopupSize​(int width,
int height)

Sets the size of the Popup window to the specified width and
height. This is equivalent to

setPreferredSize(new Dimension(width, height))

.

setSelected

```java
@BeanProperty
(
expert
=true,

hidden
=true,

description
="The selected component on the popup menu")
public void setSelected​(
Component
sel)
```

Sets the currently selected component, This will result
in a change to the selection model.

**Parameters:** sel

- the

Component

to select

---

#### setSelected

@BeanProperty

(

expert

=true,

hidden

=true,

description

="The selected component on the popup menu")
public void setSelected​(

Component

sel)

Sets the currently selected component, This will result
in a change to the selection model.

isBorderPainted

```java
public boolean isBorderPainted()
```

Checks whether the border should be painted.

**Returns:** true if the border is painted, false otherwise
**See Also:** setBorderPainted(boolean)

---

#### isBorderPainted

public boolean isBorderPainted()

Checks whether the border should be painted.

setBorderPainted

```java
@BeanProperty
(
bound
=false,

description
="Is the border of the popup menu painted")
public void setBorderPainted​(boolean b)
```

Sets whether the border should be painted.

**Parameters:** b

- if true, the border is painted.
**See Also:** isBorderPainted()

---

#### setBorderPainted

@BeanProperty

(

bound

=false,

description

="Is the border of the popup menu painted")
public void setBorderPainted​(boolean b)

Sets whether the border should be painted.

paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the popup menu's border if the

borderPainted

property is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

object
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

---

#### paintBorder

protected void paintBorder​(

Graphics

g)

Paints the popup menu's border if the

borderPainted

property is

true

.

getMargin

```java
@BeanProperty
(
bound
=false)
public
Insets
getMargin()
```

Returns the margin, in pixels, between the popup menu's border and
its containers.

**Returns:** an

Insets

object containing the margin values.

---

#### getMargin

@BeanProperty

(

bound

=false)
public

Insets

getMargin()

Returns the margin, in pixels, between the popup menu's border and
its containers.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JPopupMenu

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JPopupMenu

.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JPopupMenu

.
This method
is intended to be used only for debugging purposes, and the
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

Gets the AccessibleContext associated with this JPopupMenu.
For JPopupMenus, the AccessibleContext takes the form of an
AccessibleJPopupMenu.
A new AccessibleJPopupMenu instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJPopupMenu that serves as the
AccessibleContext of this JPopupMenu

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JPopupMenu.
For JPopupMenus, the AccessibleContext takes the form of an
AccessibleJPopupMenu.
A new AccessibleJPopupMenu instance is created if necessary.

processMouseEvent

```java
public void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

This method is required to conform to the

MenuElement

interface, but it not implemented.

**Specified by:** processMouseEvent

in interface

MenuElement
**Parameters:** event

- a

MouseEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy
**See Also:** MenuElement.processMouseEvent(MouseEvent, MenuElement[], MenuSelectionManager)

---

#### processMouseEvent

public void processMouseEvent​(

MouseEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

This method is required to conform to the

MenuElement

interface, but it not implemented.

processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

Note: you do not have to forward the event to sub-components.
This is done automatically by the

MenuSelectionManager

.

**Specified by:** processKeyEvent

in interface

MenuElement
**Parameters:** e

- a

KeyEvent
**Parameters:** path

- the

MenuElement

path array
**Parameters:** manager

- the

MenuSelectionManager

---

#### processKeyEvent

public void processKeyEvent​(

KeyEvent

e,

MenuElement

[] path,

MenuSelectionManager

manager)

Processes a key event forwarded from the

MenuSelectionManager

and changes the menu selection,
if necessary, by using

MenuSelectionManager

's API.

Note: you do not have to forward the event to sub-components.
This is done automatically by the

MenuSelectionManager

.

Note: you do not have to forward the event to sub-components.
This is done automatically by the

MenuSelectionManager

.

menuSelectionChanged

```java
public void menuSelectionChanged​(boolean isIncluded)
```

Messaged when the menubar selection changes to activate or
deactivate this menu. This implements the

javax.swing.MenuElement

interface.
Overrides

MenuElement.menuSelectionChanged

.

**Specified by:** menuSelectionChanged

in interface

MenuElement
**Parameters:** isIncluded

- true if this menu is active, false if
it is not
**See Also:** MenuElement.menuSelectionChanged(boolean)

---

#### menuSelectionChanged

public void menuSelectionChanged​(boolean isIncluded)

Messaged when the menubar selection changes to activate or
deactivate this menu. This implements the

javax.swing.MenuElement

interface.
Overrides

MenuElement.menuSelectionChanged

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
for this menu component. It will only return items conforming to
the

JMenuElement

interface.
If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface.

**Specified by:** getSubElements

in interface

MenuElement
**Returns:** an array of

MenuElement

objects
**See Also:** MenuElement.getSubElements()

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
for this menu component. It will only return items conforming to
the

JMenuElement

interface.
If popup menu is

null

returns
an empty array. This method is required to conform to the

MenuElement

interface.

getComponent

```java
public
Component
getComponent()
```

Returns this

JPopupMenu

component.

**Specified by:** getComponent

in interface

MenuElement
**Returns:** this

JPopupMenu

object
**See Also:** MenuElement.getComponent()

---

#### getComponent

public

Component

getComponent()

Returns this

JPopupMenu

component.

isPopupTrigger

```java
public boolean isPopupTrigger​(
MouseEvent
e)
```

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

**Parameters:** e

- a

MouseEvent
**Returns:** true if the mouse event is a popup trigger
**Since:** 1.3

---

#### isPopupTrigger

public boolean isPopupTrigger​(

MouseEvent

e)

Returns true if the

MouseEvent

is considered a popup trigger
by the

JPopupMenu

's currently installed UI.

---

