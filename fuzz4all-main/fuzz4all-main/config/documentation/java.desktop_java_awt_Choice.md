# Class Choice

**Source:** `java.desktop\java\awt\Choice.html`

### Class Description

```java
public class
Choice

extends
Component

implements
ItemSelectable
,
Accessible
```

The

Choice

class presents a pop-up menu of choices.
The current choice is displayed as the title of the menu.

The following code example produces a pop-up menu:

```java
Choice ColorChooser = new Choice();
ColorChooser.add("Green");
ColorChooser.add("Red");
ColorChooser.add("Blue");
```

After this choice menu has been added to a panel,
it appears as follows in its normal state:

In the picture,

"Green"

is the current choice.
Pushing the mouse button down on the object causes a menu to
appear with the current choice highlighted.

Some native platforms do not support arbitrary resizing of

Choice

components and the behavior of

setSize()/getSize()

is bound by
such limitations.
Native GUI

Choice

components' size are often bound by such
attributes as font size and length of items contained within
the

Choice

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

---

### Field Details

*No entries found.*

### Constructor Details

#### public Choice()
throws
HeadlessException

Creates a new choice menu. The menu initially has no items in it.

By default, the first item added to the choice menu becomes the
selected item, until a different selection is made by the user
by calling one of the

select

methods.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

select(int)

,

select(java.lang.String)

---

### Method Details

#### public void addNotify()

Creates the

Choice

's peer. This peer allows us
to change the look
of the

Choice

without changing its functionality.

**Overrides:**
- addNotify

in class

Component

**See Also:**
- Component.getToolkit()

---

#### public int getItemCount()

Returns the number of items in this

Choice

menu.

**Returns:**
- the number of items in this

Choice

menu

**See Also:**
- getItem(int)

**Since:**
- 1.1

---

#### @Deprecated

public int countItems()

Returns the number of items in this

Choice

menu.

**Returns:**
- the number of items in this

Choice

menu

---

#### public
String
getItem​(int index)

Gets the string at the specified index in this

Choice

menu.

**Parameters:**
- index

- the index at which to begin

**Returns:**
- the item at the specified index

**See Also:**
- getItemCount()

---

#### public void add​(
String
item)

Adds an item to this

Choice

menu.

**Parameters:**
- item

- the item to be added

**Throws:**
- NullPointerException

- if the item's value is

null

**Since:**
- 1.1

---

#### public void addItem​(
String
item)

Obsolete as of Java 2 platform v1.1. Please use the

add

method instead.

Adds an item to this

Choice

menu.

**Parameters:**
- item

- the item to be added

**Throws:**
- NullPointerException

- if the item's value is equal to

null

---

#### public void insert​(
String
item,
int index)

Inserts the item into this choice at the specified position.
Existing items at an index greater than or equal to

index

are shifted up by one to accommodate
the new item. If

index

is greater than or
equal to the number of items in this choice,

item

is added to the end of this choice.

If the item is the first one being added to the choice,
then the item becomes selected. Otherwise, if the
selected item was one of the items shifted, the first
item in the choice becomes the selected item. If the
selected item was no among those shifted, it remains
the selected item.

**Parameters:**
- item

- the non-

null

item to be inserted
- index

- the position at which the item should be inserted

**Throws:**
- IllegalArgumentException

- if index is less than 0

---

#### public void remove​(
String
item)

Removes the first occurrence of

item

from the

Choice

menu. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:**
- item

- the item to remove from this

Choice

menu

**Throws:**
- IllegalArgumentException

- if the item doesn't
exist in the choice menu

**Since:**
- 1.1

---

#### public void remove​(int position)

Removes an item from the choice menu
at the specified position. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:**
- position

- the position of the item

**Throws:**
- IndexOutOfBoundsException

- if the specified
position is out of bounds

**Since:**
- 1.1

---

#### public void removeAll()

Removes all items from the choice menu.

**See Also:**
- remove(java.lang.String)

**Since:**
- 1.1

---

#### public
String
getSelectedItem()

Gets a representation of the current choice as a string.

**Returns:**
- a string representation of the currently
selected item in this choice menu

**See Also:**
- getSelectedIndex()

---

#### public
Object
[] getSelectedObjects()

Returns an array (length 1) containing the currently selected
item. If this choice has no items, returns

null

.

**Specified by:**
- getSelectedObjects

in interface

ItemSelectable

**Returns:**
- the list of selected objects, or

null

**See Also:**
- ItemSelectable

---

#### public int getSelectedIndex()

Returns the index of the currently selected item.
If nothing is selected, returns -1.

**Returns:**
- the index of the currently selected item, or -1 if nothing
is currently selected

**See Also:**
- getSelectedItem()

---

#### public void select​(int pos)

Sets the selected item in this

Choice

menu to be the
item at the specified position.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:**
- pos

- the position of the selected item

**Throws:**
- IllegalArgumentException

- if the specified
position is greater than the
number of items or less than zero

**See Also:**
- getSelectedItem()

,

getSelectedIndex()

---

#### public void select​(
String
str)

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.
If more than one item matches (is equal to) the specified string,
the one with the smallest index is selected.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:**
- str

- the specified string

**See Also:**
- getSelectedItem()

,

getSelectedIndex()

---

#### public void addItemListener​(
ItemListener
l)

Adds the specified item listener to receive item events from
this

Choice

menu. Item events are sent in response
to user input, but not in response to calls to

select

.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- addItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the item listener

**See Also:**
- removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

ItemEvent

,

ItemListener

**Since:**
- 1.1

---

#### public void removeItemListener​(
ItemListener
l)

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- removeItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the item listener

**See Also:**
- addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

**Since:**
- 1.1

---

#### public
ItemListener
[] getItemListeners()

Returns an array of all the item listeners
registered on this choice.

**Returns:**
- all of this choice's

ItemListener

s
or an empty array if no item
listeners are currently registered

**See Also:**
- addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

**Since:**
- 1.4

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Choice c

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(c.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:**
- getListeners

in class

Component

**Parameters:**
- listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this choice,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- getItemListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of the listeners

---

#### protected void processEvent​(
AWTEvent
e)

Processes events on this choice. If the event is an
instance of

ItemEvent

, it invokes the

processItemEvent

method. Otherwise, it calls its
superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:**
- processEvent

in class

Component

**Parameters:**
- e

- the event

**See Also:**
- ItemEvent

,

processItemEvent(java.awt.event.ItemEvent)

**Since:**
- 1.1

---

#### protected void processItemEvent​(
ItemEvent
e)

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the item event

**See Also:**
- ItemEvent

,

ItemListener

,

addItemListener(ItemListener)

,

Component.enableEvents(long)

**Since:**
- 1.1

---

#### protected
String
paramString()

Returns a string representing the state of this

Choice

menu. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

Component

**Returns:**
- the parameter string of this

Choice

menu

---

#### public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with this

Choice

. For

Choice

components,
the

AccessibleContext

takes the form of an

AccessibleAWTChoice

. A new

AccessibleAWTChoice

instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an

AccessibleAWTChoice

that serves as the

AccessibleContext

of this

Choice

**Since:**
- 1.3

---

### Additional Sections

#### Class Choice

java.lang.Object

- java.awt.Component
- - java.awt.Choice

java.awt.Component

- java.awt.Choice

java.awt.Choice

**All Implemented Interfaces:** ImageObserver

,

ItemSelectable

,

MenuContainer

,

Serializable

,

Accessible

```java
public class
Choice

extends
Component

implements
ItemSelectable
,
Accessible
```

The

Choice

class presents a pop-up menu of choices.
The current choice is displayed as the title of the menu.

The following code example produces a pop-up menu:

```java
Choice ColorChooser = new Choice();
ColorChooser.add("Green");
ColorChooser.add("Red");
ColorChooser.add("Blue");
```

After this choice menu has been added to a panel,
it appears as follows in its normal state:

In the picture,

"Green"

is the current choice.
Pushing the mouse button down on the object causes a menu to
appear with the current choice highlighted.

Some native platforms do not support arbitrary resizing of

Choice

components and the behavior of

setSize()/getSize()

is bound by
such limitations.
Native GUI

Choice

components' size are often bound by such
attributes as font size and length of items contained within
the

Choice

.

**Since:** 1.0
**See Also:** Serialized Form

public class

Choice

extends

Component

implements

ItemSelectable

,

Accessible

The

Choice

class presents a pop-up menu of choices.
The current choice is displayed as the title of the menu.

The following code example produces a pop-up menu:

```java
Choice ColorChooser = new Choice();
ColorChooser.add("Green");
ColorChooser.add("Red");
ColorChooser.add("Blue");
```

After this choice menu has been added to a panel,
it appears as follows in its normal state:

In the picture,

"Green"

is the current choice.
Pushing the mouse button down on the object causes a menu to
appear with the current choice highlighted.

Some native platforms do not support arbitrary resizing of

Choice

components and the behavior of

setSize()/getSize()

is bound by
such limitations.
Native GUI

Choice

components' size are often bound by such
attributes as font size and length of items contained within
the

Choice

.

The following code example produces a pop-up menu:

```java
Choice ColorChooser = new Choice();
ColorChooser.add("Green");
ColorChooser.add("Red");
ColorChooser.add("Blue");
```

After this choice menu has been added to a panel,
it appears as follows in its normal state:

In the picture,

"Green"

is the current choice.
Pushing the mouse button down on the object causes a menu to
appear with the current choice highlighted.

Some native platforms do not support arbitrary resizing of

Choice

components and the behavior of

setSize()/getSize()

is bound by
such limitations.
Native GUI

Choice

components' size are often bound by such
attributes as font size and length of items contained within
the

Choice

.

Choice ColorChooser = new Choice();
ColorChooser.add("Green");
ColorChooser.add("Red");
ColorChooser.add("Blue");

After this choice menu has been added to a panel,
it appears as follows in its normal state:

In the picture,

"Green"

is the current choice.
Pushing the mouse button down on the object causes a menu to
appear with the current choice highlighted.

Some native platforms do not support arbitrary resizing of

Choice

components and the behavior of

setSize()/getSize()

is bound by
such limitations.
Native GUI

Choice

components' size are often bound by such
attributes as font size and length of items contained within
the

Choice

.

In the picture,

"Green"

is the current choice.
Pushing the mouse button down on the object causes a menu to
appear with the current choice highlighted.

Some native platforms do not support arbitrary resizing of

Choice

components and the behavior of

setSize()/getSize()

is bound by
such limitations.
Native GUI

Choice

components' size are often bound by such
attributes as font size and length of items contained within
the

Choice

.

Some native platforms do not support arbitrary resizing of

Choice

components and the behavior of

setSize()/getSize()

is bound by
such limitations.
Native GUI

Choice

components' size are often bound by such
attributes as font size and length of items contained within
the

Choice

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Choice.AccessibleAWTChoice

This class implements accessibility support for the

Choice

class.

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

Choice

()

Creates a new choice menu.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

add

​(

String

item)

Adds an item to this

Choice

menu.

void

addItem

​(

String

item)

Obsolete as of Java 2 platform v1.1.

void

addItemListener

​(

ItemListener

l)

Adds the specified item listener to receive item events from
this

Choice

menu.

void

addNotify

()

Creates the

Choice

's peer.

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

Gets the

AccessibleContext

associated with this

Choice

.

String

getItem

​(int index)

Gets the string at the specified index in this

Choice

menu.

int

getItemCount

()

Returns the number of items in this

Choice

menu.

ItemListener

[]

getItemListeners

()

Returns an array of all the item listeners
registered on this choice.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

int

getSelectedIndex

()

Returns the index of the currently selected item.

String

getSelectedItem

()

Gets a representation of the current choice as a string.

Object

[]

getSelectedObjects

()

Returns an array (length 1) containing the currently selected
item.

void

insert

​(

String

item,
int index)

Inserts the item into this choice at the specified position.

protected

String

paramString

()

Returns a string representing the state of this

Choice

menu.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this choice.

protected void

processItemEvent

​(

ItemEvent

e)

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

void

remove

​(int position)

Removes an item from the choice menu
at the specified position.

void

remove

​(

String

item)

Removes the first occurrence of

item

from the

Choice

menu.

void

removeAll

()

Removes all items from the choice menu.

void

removeItemListener

​(

ItemListener

l)

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.

void

select

​(int pos)

Sets the selected item in this

Choice

menu to be the
item at the specified position.

void

select

​(

String

str)

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

,

getMinimumSize

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

getPreferredSize

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

,

location

,

lostFocus

,

minimumSize

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

paint

,

paintAll

,

postEvent

,

preferredSize

,

prepareImage

,

prepareImage

,

print

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

removeNotify

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

Choice.AccessibleAWTChoice

This class implements accessibility support for the

Choice

class.

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

Choice

class.

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

Choice

()

Creates a new choice menu.

---

#### Constructor Summary

Creates a new choice menu.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

add

​(

String

item)

Adds an item to this

Choice

menu.

void

addItem

​(

String

item)

Obsolete as of Java 2 platform v1.1.

void

addItemListener

​(

ItemListener

l)

Adds the specified item listener to receive item events from
this

Choice

menu.

void

addNotify

()

Creates the

Choice

's peer.

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

Gets the

AccessibleContext

associated with this

Choice

.

String

getItem

​(int index)

Gets the string at the specified index in this

Choice

menu.

int

getItemCount

()

Returns the number of items in this

Choice

menu.

ItemListener

[]

getItemListeners

()

Returns an array of all the item listeners
registered on this choice.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

int

getSelectedIndex

()

Returns the index of the currently selected item.

String

getSelectedItem

()

Gets a representation of the current choice as a string.

Object

[]

getSelectedObjects

()

Returns an array (length 1) containing the currently selected
item.

void

insert

​(

String

item,
int index)

Inserts the item into this choice at the specified position.

protected

String

paramString

()

Returns a string representing the state of this

Choice

menu.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this choice.

protected void

processItemEvent

​(

ItemEvent

e)

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

void

remove

​(int position)

Removes an item from the choice menu
at the specified position.

void

remove

​(

String

item)

Removes the first occurrence of

item

from the

Choice

menu.

void

removeAll

()

Removes all items from the choice menu.

void

removeItemListener

​(

ItemListener

l)

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.

void

select

​(int pos)

Sets the selected item in this

Choice

menu to be the
item at the specified position.

void

select

​(

String

str)

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

,

getMinimumSize

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

getPreferredSize

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

,

location

,

lostFocus

,

minimumSize

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

paint

,

paintAll

,

postEvent

,

preferredSize

,

prepareImage

,

prepareImage

,

print

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

removeNotify

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

Adds an item to this

Choice

menu.

Obsolete as of Java 2 platform v1.1.

Adds the specified item listener to receive item events from
this

Choice

menu.

Creates the

Choice

's peer.

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Gets the

AccessibleContext

associated with this

Choice

.

Gets the string at the specified index in this

Choice

menu.

Returns the number of items in this

Choice

menu.

Returns an array of all the item listeners
registered on this choice.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

Returns the index of the currently selected item.

Gets a representation of the current choice as a string.

Returns an array (length 1) containing the currently selected
item.

Inserts the item into this choice at the specified position.

Returns a string representing the state of this

Choice

menu.

Processes events on this choice.

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

Removes an item from the choice menu
at the specified position.

Removes the first occurrence of

item

from the

Choice

menu.

Removes all items from the choice menu.

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.

Sets the selected item in this

Choice

menu to be the
item at the specified position.

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

,

getMinimumSize

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

getPreferredSize

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

,

location

,

lostFocus

,

minimumSize

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

paint

,

paintAll

,

postEvent

,

preferredSize

,

prepareImage

,

prepareImage

,

print

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

removeNotify

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

- Choice

```java
public Choice()
throws
HeadlessException
```

Creates a new choice menu. The menu initially has no items in it.

By default, the first item added to the choice menu becomes the
selected item, until a different selection is made by the user
by calling one of the

select

methods.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

,

select(int)

,

select(java.lang.String)

============ METHOD DETAIL ==========

- Method Detail

- addNotify

```java
public void addNotify()
```

Creates the

Choice

's peer. This peer allows us
to change the look
of the

Choice

without changing its functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.getToolkit()

- getItemCount

```java
public int getItemCount()
```

Returns the number of items in this

Choice

menu.

**Returns:** the number of items in this

Choice

menu
**Since:** 1.1
**See Also:** getItem(int)

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

Returns the number of items in this

Choice

menu.

**Returns:** the number of items in this

Choice

menu

- getItem

```java
public
String
getItem​(int index)
```

Gets the string at the specified index in this

Choice

menu.

**Parameters:** index

- the index at which to begin
**Returns:** the item at the specified index
**See Also:** getItemCount()

- add

```java
public void add​(
String
item)
```

Adds an item to this

Choice

menu.

**Parameters:** item

- the item to be added
**Throws:** NullPointerException

- if the item's value is

null
**Since:** 1.1

- addItem

```java
public void addItem​(
String
item)
```

Obsolete as of Java 2 platform v1.1. Please use the

add

method instead.

Adds an item to this

Choice

menu.

**Parameters:** item

- the item to be added
**Throws:** NullPointerException

- if the item's value is equal to

null

- insert

```java
public void insert​(
String
item,
int index)
```

Inserts the item into this choice at the specified position.
Existing items at an index greater than or equal to

index

are shifted up by one to accommodate
the new item. If

index

is greater than or
equal to the number of items in this choice,

item

is added to the end of this choice.

If the item is the first one being added to the choice,
then the item becomes selected. Otherwise, if the
selected item was one of the items shifted, the first
item in the choice becomes the selected item. If the
selected item was no among those shifted, it remains
the selected item.

**Parameters:** item

- the non-

null

item to be inserted
**Parameters:** index

- the position at which the item should be inserted
**Throws:** IllegalArgumentException

- if index is less than 0

- remove

```java
public void remove​(
String
item)
```

Removes the first occurrence of

item

from the

Choice

menu. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:** item

- the item to remove from this

Choice

menu
**Throws:** IllegalArgumentException

- if the item doesn't
exist in the choice menu
**Since:** 1.1

- remove

```java
public void remove​(int position)
```

Removes an item from the choice menu
at the specified position. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:** position

- the position of the item
**Throws:** IndexOutOfBoundsException

- if the specified
position is out of bounds
**Since:** 1.1

- removeAll

```java
public void removeAll()
```

Removes all items from the choice menu.

**Since:** 1.1
**See Also:** remove(java.lang.String)

- getSelectedItem

```java
public
String
getSelectedItem()
```

Gets a representation of the current choice as a string.

**Returns:** a string representation of the currently
selected item in this choice menu
**See Also:** getSelectedIndex()

- getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Returns an array (length 1) containing the currently selected
item. If this choice has no items, returns

null

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** the list of selected objects, or

null
**See Also:** ItemSelectable

- getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the index of the currently selected item.
If nothing is selected, returns -1.

**Returns:** the index of the currently selected item, or -1 if nothing
is currently selected
**See Also:** getSelectedItem()

- select

```java
public void select​(int pos)
```

Sets the selected item in this

Choice

menu to be the
item at the specified position.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** pos

- the position of the selected item
**Throws:** IllegalArgumentException

- if the specified
position is greater than the
number of items or less than zero
**See Also:** getSelectedItem()

,

getSelectedIndex()

- select

```java
public void select​(
String
str)
```

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.
If more than one item matches (is equal to) the specified string,
the one with the smallest index is selected.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** str

- the specified string
**See Also:** getSelectedItem()

,

getSelectedIndex()

- addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds the specified item listener to receive item events from
this

Choice

menu. Item events are sent in response
to user input, but not in response to calls to

select

.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

ItemEvent

,

ItemListener

- removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

- getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this choice.

**Returns:** all of this choice's

ItemListener

s
or an empty array if no item
listeners are currently registered
**Since:** 1.4
**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Choice c

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(c.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this choice,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getItemListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this choice. If the event is an
instance of

ItemEvent

, it invokes the

processItemEvent

method. Otherwise, it calls its
superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** ItemEvent

,

processItemEvent(java.awt.event.ItemEvent)

- processItemEvent

```java
protected void processItemEvent​(
ItemEvent
e)
```

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the item event
**Since:** 1.1
**See Also:** ItemEvent

,

ItemListener

,

addItemListener(ItemListener)

,

Component.enableEvents(long)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Choice

menu. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this

Choice

menu

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

Choice

. For

Choice

components,
the

AccessibleContext

takes the form of an

AccessibleAWTChoice

. A new

AccessibleAWTChoice

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTChoice

that serves as the

AccessibleContext

of this

Choice
**Since:** 1.3

Constructor Detail

- Choice

```java
public Choice()
throws
HeadlessException
```

Creates a new choice menu. The menu initially has no items in it.

By default, the first item added to the choice menu becomes the
selected item, until a different selection is made by the user
by calling one of the

select

methods.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

,

select(int)

,

select(java.lang.String)

---

#### Constructor Detail

Choice

```java
public Choice()
throws
HeadlessException
```

Creates a new choice menu. The menu initially has no items in it.

By default, the first item added to the choice menu becomes the
selected item, until a different selection is made by the user
by calling one of the

select

methods.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

,

select(int)

,

select(java.lang.String)

---

#### Choice

public Choice()
throws

HeadlessException

Creates a new choice menu. The menu initially has no items in it.

By default, the first item added to the choice menu becomes the
selected item, until a different selection is made by the user
by calling one of the

select

methods.

By default, the first item added to the choice menu becomes the
selected item, until a different selection is made by the user
by calling one of the

select

methods.

Method Detail

- addNotify

```java
public void addNotify()
```

Creates the

Choice

's peer. This peer allows us
to change the look
of the

Choice

without changing its functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.getToolkit()

- getItemCount

```java
public int getItemCount()
```

Returns the number of items in this

Choice

menu.

**Returns:** the number of items in this

Choice

menu
**Since:** 1.1
**See Also:** getItem(int)

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

Returns the number of items in this

Choice

menu.

**Returns:** the number of items in this

Choice

menu

- getItem

```java
public
String
getItem​(int index)
```

Gets the string at the specified index in this

Choice

menu.

**Parameters:** index

- the index at which to begin
**Returns:** the item at the specified index
**See Also:** getItemCount()

- add

```java
public void add​(
String
item)
```

Adds an item to this

Choice

menu.

**Parameters:** item

- the item to be added
**Throws:** NullPointerException

- if the item's value is

null
**Since:** 1.1

- addItem

```java
public void addItem​(
String
item)
```

Obsolete as of Java 2 platform v1.1. Please use the

add

method instead.

Adds an item to this

Choice

menu.

**Parameters:** item

- the item to be added
**Throws:** NullPointerException

- if the item's value is equal to

null

- insert

```java
public void insert​(
String
item,
int index)
```

Inserts the item into this choice at the specified position.
Existing items at an index greater than or equal to

index

are shifted up by one to accommodate
the new item. If

index

is greater than or
equal to the number of items in this choice,

item

is added to the end of this choice.

If the item is the first one being added to the choice,
then the item becomes selected. Otherwise, if the
selected item was one of the items shifted, the first
item in the choice becomes the selected item. If the
selected item was no among those shifted, it remains
the selected item.

**Parameters:** item

- the non-

null

item to be inserted
**Parameters:** index

- the position at which the item should be inserted
**Throws:** IllegalArgumentException

- if index is less than 0

- remove

```java
public void remove​(
String
item)
```

Removes the first occurrence of

item

from the

Choice

menu. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:** item

- the item to remove from this

Choice

menu
**Throws:** IllegalArgumentException

- if the item doesn't
exist in the choice menu
**Since:** 1.1

- remove

```java
public void remove​(int position)
```

Removes an item from the choice menu
at the specified position. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:** position

- the position of the item
**Throws:** IndexOutOfBoundsException

- if the specified
position is out of bounds
**Since:** 1.1

- removeAll

```java
public void removeAll()
```

Removes all items from the choice menu.

**Since:** 1.1
**See Also:** remove(java.lang.String)

- getSelectedItem

```java
public
String
getSelectedItem()
```

Gets a representation of the current choice as a string.

**Returns:** a string representation of the currently
selected item in this choice menu
**See Also:** getSelectedIndex()

- getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Returns an array (length 1) containing the currently selected
item. If this choice has no items, returns

null

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** the list of selected objects, or

null
**See Also:** ItemSelectable

- getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the index of the currently selected item.
If nothing is selected, returns -1.

**Returns:** the index of the currently selected item, or -1 if nothing
is currently selected
**See Also:** getSelectedItem()

- select

```java
public void select​(int pos)
```

Sets the selected item in this

Choice

menu to be the
item at the specified position.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** pos

- the position of the selected item
**Throws:** IllegalArgumentException

- if the specified
position is greater than the
number of items or less than zero
**See Also:** getSelectedItem()

,

getSelectedIndex()

- select

```java
public void select​(
String
str)
```

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.
If more than one item matches (is equal to) the specified string,
the one with the smallest index is selected.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** str

- the specified string
**See Also:** getSelectedItem()

,

getSelectedIndex()

- addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds the specified item listener to receive item events from
this

Choice

menu. Item events are sent in response
to user input, but not in response to calls to

select

.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

ItemEvent

,

ItemListener

- removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

- getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this choice.

**Returns:** all of this choice's

ItemListener

s
or an empty array if no item
listeners are currently registered
**Since:** 1.4
**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Choice c

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(c.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this choice,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getItemListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this choice. If the event is an
instance of

ItemEvent

, it invokes the

processItemEvent

method. Otherwise, it calls its
superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** ItemEvent

,

processItemEvent(java.awt.event.ItemEvent)

- processItemEvent

```java
protected void processItemEvent​(
ItemEvent
e)
```

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the item event
**Since:** 1.1
**See Also:** ItemEvent

,

ItemListener

,

addItemListener(ItemListener)

,

Component.enableEvents(long)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Choice

menu. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this

Choice

menu

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

Choice

. For

Choice

components,
the

AccessibleContext

takes the form of an

AccessibleAWTChoice

. A new

AccessibleAWTChoice

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTChoice

that serves as the

AccessibleContext

of this

Choice
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Creates the

Choice

's peer. This peer allows us
to change the look
of the

Choice

without changing its functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.getToolkit()

---

#### addNotify

public void addNotify()

Creates the

Choice

's peer. This peer allows us
to change the look
of the

Choice

without changing its functionality.

getItemCount

```java
public int getItemCount()
```

Returns the number of items in this

Choice

menu.

**Returns:** the number of items in this

Choice

menu
**Since:** 1.1
**See Also:** getItem(int)

---

#### getItemCount

public int getItemCount()

Returns the number of items in this

Choice

menu.

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

Returns the number of items in this

Choice

menu.

**Returns:** the number of items in this

Choice

menu

---

#### countItems

@Deprecated

public int countItems()

Returns the number of items in this

Choice

menu.

getItem

```java
public
String
getItem​(int index)
```

Gets the string at the specified index in this

Choice

menu.

**Parameters:** index

- the index at which to begin
**Returns:** the item at the specified index
**See Also:** getItemCount()

---

#### getItem

public

String

getItem​(int index)

Gets the string at the specified index in this

Choice

menu.

add

```java
public void add​(
String
item)
```

Adds an item to this

Choice

menu.

**Parameters:** item

- the item to be added
**Throws:** NullPointerException

- if the item's value is

null
**Since:** 1.1

---

#### add

public void add​(

String

item)

Adds an item to this

Choice

menu.

addItem

```java
public void addItem​(
String
item)
```

Obsolete as of Java 2 platform v1.1. Please use the

add

method instead.

Adds an item to this

Choice

menu.

**Parameters:** item

- the item to be added
**Throws:** NullPointerException

- if the item's value is equal to

null

---

#### addItem

public void addItem​(

String

item)

Obsolete as of Java 2 platform v1.1. Please use the

add

method instead.

Adds an item to this

Choice

menu.

Adds an item to this

Choice

menu.

insert

```java
public void insert​(
String
item,
int index)
```

Inserts the item into this choice at the specified position.
Existing items at an index greater than or equal to

index

are shifted up by one to accommodate
the new item. If

index

is greater than or
equal to the number of items in this choice,

item

is added to the end of this choice.

If the item is the first one being added to the choice,
then the item becomes selected. Otherwise, if the
selected item was one of the items shifted, the first
item in the choice becomes the selected item. If the
selected item was no among those shifted, it remains
the selected item.

**Parameters:** item

- the non-

null

item to be inserted
**Parameters:** index

- the position at which the item should be inserted
**Throws:** IllegalArgumentException

- if index is less than 0

---

#### insert

public void insert​(

String

item,
int index)

Inserts the item into this choice at the specified position.
Existing items at an index greater than or equal to

index

are shifted up by one to accommodate
the new item. If

index

is greater than or
equal to the number of items in this choice,

item

is added to the end of this choice.

If the item is the first one being added to the choice,
then the item becomes selected. Otherwise, if the
selected item was one of the items shifted, the first
item in the choice becomes the selected item. If the
selected item was no among those shifted, it remains
the selected item.

If the item is the first one being added to the choice,
then the item becomes selected. Otherwise, if the
selected item was one of the items shifted, the first
item in the choice becomes the selected item. If the
selected item was no among those shifted, it remains
the selected item.

remove

```java
public void remove​(
String
item)
```

Removes the first occurrence of

item

from the

Choice

menu. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:** item

- the item to remove from this

Choice

menu
**Throws:** IllegalArgumentException

- if the item doesn't
exist in the choice menu
**Since:** 1.1

---

#### remove

public void remove​(

String

item)

Removes the first occurrence of

item

from the

Choice

menu. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

remove

```java
public void remove​(int position)
```

Removes an item from the choice menu
at the specified position. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

**Parameters:** position

- the position of the item
**Throws:** IndexOutOfBoundsException

- if the specified
position is out of bounds
**Since:** 1.1

---

#### remove

public void remove​(int position)

Removes an item from the choice menu
at the specified position. If the item
being removed is the currently selected item,
then the first item in the choice becomes the
selected item. Otherwise, the currently selected
item remains selected (and the selected index is
updated accordingly).

removeAll

```java
public void removeAll()
```

Removes all items from the choice menu.

**Since:** 1.1
**See Also:** remove(java.lang.String)

---

#### removeAll

public void removeAll()

Removes all items from the choice menu.

getSelectedItem

```java
public
String
getSelectedItem()
```

Gets a representation of the current choice as a string.

**Returns:** a string representation of the currently
selected item in this choice menu
**See Also:** getSelectedIndex()

---

#### getSelectedItem

public

String

getSelectedItem()

Gets a representation of the current choice as a string.

getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Returns an array (length 1) containing the currently selected
item. If this choice has no items, returns

null

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** the list of selected objects, or

null
**See Also:** ItemSelectable

---

#### getSelectedObjects

public

Object

[] getSelectedObjects()

Returns an array (length 1) containing the currently selected
item. If this choice has no items, returns

null

.

getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the index of the currently selected item.
If nothing is selected, returns -1.

**Returns:** the index of the currently selected item, or -1 if nothing
is currently selected
**See Also:** getSelectedItem()

---

#### getSelectedIndex

public int getSelectedIndex()

Returns the index of the currently selected item.
If nothing is selected, returns -1.

select

```java
public void select​(int pos)
```

Sets the selected item in this

Choice

menu to be the
item at the specified position.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** pos

- the position of the selected item
**Throws:** IllegalArgumentException

- if the specified
position is greater than the
number of items or less than zero
**See Also:** getSelectedItem()

,

getSelectedIndex()

---

#### select

public void select​(int pos)

Sets the selected item in this

Choice

menu to be the
item at the specified position.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

select

```java
public void select​(
String
str)
```

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.
If more than one item matches (is equal to) the specified string,
the one with the smallest index is selected.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** str

- the specified string
**See Also:** getSelectedItem()

,

getSelectedIndex()

---

#### select

public void select​(

String

str)

Sets the selected item in this

Choice

menu
to be the item whose name is equal to the specified string.
If more than one item matches (is equal to) the specified string,
the one with the smallest index is selected.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds the specified item listener to receive item events from
this

Choice

menu. Item events are sent in response
to user input, but not in response to calls to

select

.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

ItemEvent

,

ItemListener

---

#### addItemListener

public void addItemListener​(

ItemListener

l)

Adds the specified item listener to receive item events from
this

Choice

menu. Item events are sent in response
to user input, but not in response to calls to

select

.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

---

#### removeItemListener

public void removeItemListener​(

ItemListener

l)

Removes the specified item listener so that it no longer receives
item events from this

Choice

menu.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this choice.

**Returns:** all of this choice's

ItemListener

s
or an empty array if no item
listeners are currently registered
**Since:** 1.4
**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

---

#### getItemListeners

public

ItemListener

[] getItemListeners()

Returns an array of all the item listeners
registered on this choice.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Choice c

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(c.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this choice,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getItemListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Choice

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Choice c

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(c.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Choice c

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(c.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

ItemListener[] ils = (ItemListener[])(c.getListeners(ItemListener.class));

processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this choice. If the event is an
instance of

ItemEvent

, it invokes the

processItemEvent

method. Otherwise, it calls its
superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** ItemEvent

,

processItemEvent(java.awt.event.ItemEvent)

---

#### processEvent

protected void processEvent​(

AWTEvent

e)

Processes events on this choice. If the event is an
instance of

ItemEvent

, it invokes the

processItemEvent

method. Otherwise, it calls its
superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processItemEvent

```java
protected void processItemEvent​(
ItemEvent
e)
```

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the item event
**Since:** 1.1
**See Also:** ItemEvent

,

ItemListener

,

addItemListener(ItemListener)

,

Component.enableEvents(long)

---

#### processItemEvent

protected void processItemEvent​(

ItemEvent

e)

Processes item events occurring on this

Choice

menu by dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Choice

menu. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this

Choice

menu

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this

Choice

menu. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

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

Choice

. For

Choice

components,
the

AccessibleContext

takes the form of an

AccessibleAWTChoice

. A new

AccessibleAWTChoice

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTChoice

that serves as the

AccessibleContext

of this

Choice
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with this

Choice

. For

Choice

components,
the

AccessibleContext

takes the form of an

AccessibleAWTChoice

. A new

AccessibleAWTChoice

instance is created if necessary.

---

