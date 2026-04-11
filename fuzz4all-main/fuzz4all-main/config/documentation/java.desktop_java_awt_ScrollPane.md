# Class ScrollPane

**Source:** `java.desktop\java\awt\ScrollPane.html`

### Class Description

```java
public class
ScrollPane

extends
Container

implements
Accessible
```

A container class which implements automatic horizontal and/or
vertical scrolling for a single child component. The display
policy for the scrollbars can be set to:

- as needed: scrollbars created and shown only when needed by scrollpane

always: scrollbars created and always shown by the scrollpane

never: scrollbars never created or shown by the scrollpane

The state of the horizontal and vertical scrollbars is represented
by two

ScrollPaneAdjustable

objects (one for each
dimension) which implement the

Adjustable

interface.
The API provides methods to access those objects such that the
attributes on the Adjustable object (such as unitIncrement, value,
etc.) can be manipulated.

Certain adjustable properties (minimum, maximum, blockIncrement,
and visibleAmount) are set internally by the scrollpane in accordance
with the geometry of the scrollpane and its child and these should
not be set by programs using the scrollpane.

If the scrollbar display policy is defined as "never", then the
scrollpane can still be programmatically scrolled using the
setScrollPosition() method and the scrollpane will move and clip
the child's contents appropriately. This policy is useful if the
program needs to create and manage its own adjustable controls.

The placement of the scrollbars is controlled by platform-specific
properties set by the user outside of the program.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final int SCROLLBARS_AS_NEEDED

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLLBARS_ALWAYS

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLLBARS_NEVER

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ScrollPane()
throws
HeadlessException

Create a new scrollpane container with a scrollbar display
policy of "as needed".

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### @ConstructorProperties
("scrollbarDisplayPolicy")
public ScrollPane​(int scrollbarDisplayPolicy)
throws
HeadlessException

Create a new scrollpane container.

**Parameters:**
- scrollbarDisplayPolicy

- policy for when scrollbars should be shown

**Throws:**
- IllegalArgumentException

- if the specified scrollbar
display policy is invalid
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

### Method Details

#### protected final void addImpl​(
Component
comp,

Object
constraints,
int index)

Adds the specified component to this scroll pane container.
If the scroll pane has an existing child component, that
component is removed and the new one is added.

**Overrides:**
- addImpl

in class

Container

**Parameters:**
- comp

- the component to be added
- constraints

- not applicable
- index

- position of child component (must be <= 0)

**See Also:**
- Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

---

#### public int getScrollbarDisplayPolicy()

Returns the display policy for the scrollbars.

**Returns:**
- the display policy for the scrollbars

---

#### public
Dimension
getViewportSize()

Returns the current size of the scroll pane's view port.

**Returns:**
- the size of the view port in pixels

---

#### public int getHScrollbarHeight()

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:**
- the height of a horizontal scrollbar in pixels

---

#### public int getVScrollbarWidth()

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:**
- the width of a vertical scrollbar in pixels

---

#### public
Adjustable
getVAdjustable()

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:**
- the vertical scrollbar state

**See Also:**
- ScrollPaneAdjustable

---

#### public
Adjustable
getHAdjustable()

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:**
- the horizontal scrollbar state

**See Also:**
- ScrollPaneAdjustable

---

#### public void setScrollPosition​(int x,
int y)

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child. Specifying a position outside of the legal scrolling bounds
of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:**
- x

- the x position to scroll to
- y

- the y position to scroll to

**Throws:**
- NullPointerException

- if the scrollpane does not contain
a child

---

#### public void setScrollPosition​(
Point
p)

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child and the specified position is within legal scrolling bounds
of the child. Specifying a position outside of the legal scrolling
bounds of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:**
- p

- the Point representing the position to scroll to

**Throws:**
- NullPointerException

- if

p

is

null

---

#### public
Point
getScrollPosition()

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.
This is a convenience method which interfaces with the adjustable
objects which represent the state of the scrollbars.

**Returns:**
- the coordinate position for the current scroll position

**Throws:**
- NullPointerException

- if the scrollpane does not contain
a child

---

#### public final void setLayout​(
LayoutManager
mgr)

Sets the layout manager for this container. This method is
overridden to prevent the layout mgr from being set.

**Overrides:**
- setLayout

in class

Container

**Parameters:**
- mgr

- the specified layout manager

**See Also:**
- Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

---

#### public void doLayout()

Lays out this container by resizing its child to its preferred size.
If the new preferred size of the child causes the current scroll
position to be invalid, the scroll position is set to the closest
valid position.

**Overrides:**
- doLayout

in class

Container

**See Also:**
- Component.validate()

---

#### @Deprecated

public void layout()

**Overrides:**
- layout

in class

Container

---

#### public void printComponents​(
Graphics
g)

Prints the component in this scroll pane.

**Overrides:**
- printComponents

in class

Container

**Parameters:**
- g

- the specified Graphics window

**See Also:**
- Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

---

#### public void addNotify()

Creates the scroll pane's peer.

**Overrides:**
- addNotify

in class

Container

**See Also:**
- Component.isDisplayable()

,

Container.removeNotify()

---

#### public
String
paramString()

Returns a string representing the state of this

ScrollPane

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

Container

**Returns:**
- the parameter string of this scroll pane

---

#### protected void processMouseWheelEvent​(
MouseWheelEvent
e)

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:**
- processMouseWheelEvent

in class

Component

**Parameters:**
- e

- the mouse wheel event

**See Also:**
- MouseWheelEvent

,

MouseWheelListener

,

Component.addMouseWheelListener(java.awt.event.MouseWheelListener)

,

Component.enableEvents(long)

**Since:**
- 1.4

---

#### protected boolean eventTypeEnabled​(int type)

If wheel scrolling is enabled, we return true for MouseWheelEvents

**Since:**
- 1.4

---

#### public void setWheelScrollingEnabled​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:**
- handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.

**See Also:**
- isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

**Since:**
- 1.4

---

#### public boolean isWheelScrollingEnabled()

Indicates whether or not scrolling will take place in response to
the mouse wheel. Wheel scrolling is enabled by default.

**Returns:**
- true

if the wheel scrolling enabled;
otherwise

false

**See Also:**
- setWheelScrollingEnabled(boolean)

**Since:**
- 1.4

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this ScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleAWTScrollPane.
A new AccessibleAWTScrollPane instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleAWTScrollPane that serves as the
AccessibleContext of this ScrollPane

**Since:**
- 1.3

---

### Additional Sections

#### Class ScrollPane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.ScrollPane

java.awt.Component

- java.awt.Container
- - java.awt.ScrollPane

java.awt.Container

- java.awt.ScrollPane

java.awt.ScrollPane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
public class
ScrollPane

extends
Container

implements
Accessible
```

A container class which implements automatic horizontal and/or
vertical scrolling for a single child component. The display
policy for the scrollbars can be set to:

- as needed: scrollbars created and shown only when needed by scrollpane

always: scrollbars created and always shown by the scrollpane

never: scrollbars never created or shown by the scrollpane

The state of the horizontal and vertical scrollbars is represented
by two

ScrollPaneAdjustable

objects (one for each
dimension) which implement the

Adjustable

interface.
The API provides methods to access those objects such that the
attributes on the Adjustable object (such as unitIncrement, value,
etc.) can be manipulated.

Certain adjustable properties (minimum, maximum, blockIncrement,
and visibleAmount) are set internally by the scrollpane in accordance
with the geometry of the scrollpane and its child and these should
not be set by programs using the scrollpane.

If the scrollbar display policy is defined as "never", then the
scrollpane can still be programmatically scrolled using the
setScrollPosition() method and the scrollpane will move and clip
the child's contents appropriately. This policy is useful if the
program needs to create and manage its own adjustable controls.

The placement of the scrollbars is controlled by platform-specific
properties set by the user outside of the program.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

**See Also:** Serialized Form

public class

ScrollPane

extends

Container

implements

Accessible

A container class which implements automatic horizontal and/or
vertical scrolling for a single child component. The display
policy for the scrollbars can be set to:

- as needed: scrollbars created and shown only when needed by scrollpane

always: scrollbars created and always shown by the scrollpane

never: scrollbars never created or shown by the scrollpane

The state of the horizontal and vertical scrollbars is represented
by two

ScrollPaneAdjustable

objects (one for each
dimension) which implement the

Adjustable

interface.
The API provides methods to access those objects such that the
attributes on the Adjustable object (such as unitIncrement, value,
etc.) can be manipulated.

Certain adjustable properties (minimum, maximum, blockIncrement,
and visibleAmount) are set internally by the scrollpane in accordance
with the geometry of the scrollpane and its child and these should
not be set by programs using the scrollpane.

If the scrollbar display policy is defined as "never", then the
scrollpane can still be programmatically scrolled using the
setScrollPosition() method and the scrollpane will move and clip
the child's contents appropriately. This policy is useful if the
program needs to create and manage its own adjustable controls.

The placement of the scrollbars is controlled by platform-specific
properties set by the user outside of the program.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

as needed: scrollbars created and shown only when needed by scrollpane

always: scrollbars created and always shown by the scrollpane

never: scrollbars never created or shown by the scrollpane

The state of the horizontal and vertical scrollbars is represented
by two

ScrollPaneAdjustable

objects (one for each
dimension) which implement the

Adjustable

interface.
The API provides methods to access those objects such that the
attributes on the Adjustable object (such as unitIncrement, value,
etc.) can be manipulated.

Certain adjustable properties (minimum, maximum, blockIncrement,
and visibleAmount) are set internally by the scrollpane in accordance
with the geometry of the scrollpane and its child and these should
not be set by programs using the scrollpane.

If the scrollbar display policy is defined as "never", then the
scrollpane can still be programmatically scrolled using the
setScrollPosition() method and the scrollpane will move and clip
the child's contents appropriately. This policy is useful if the
program needs to create and manage its own adjustable controls.

The placement of the scrollbars is controlled by platform-specific
properties set by the user outside of the program.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

Certain adjustable properties (minimum, maximum, blockIncrement,
and visibleAmount) are set internally by the scrollpane in accordance
with the geometry of the scrollpane and its child and these should
not be set by programs using the scrollpane.

If the scrollbar display policy is defined as "never", then the
scrollpane can still be programmatically scrolled using the
setScrollPosition() method and the scrollpane will move and clip
the child's contents appropriately. This policy is useful if the
program needs to create and manage its own adjustable controls.

The placement of the scrollbars is controlled by platform-specific
properties set by the user outside of the program.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

If the scrollbar display policy is defined as "never", then the
scrollpane can still be programmatically scrolled using the
setScrollPosition() method and the scrollpane will move and clip
the child's contents appropriately. This policy is useful if the
program needs to create and manage its own adjustable controls.

The placement of the scrollbars is controlled by platform-specific
properties set by the user outside of the program.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

The placement of the scrollbars is controlled by platform-specific
properties set by the user outside of the program.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

The initial size of this container is set to 100x100, but can
be reset using setSize().

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

Scrolling with the wheel on a wheel-equipped mouse is enabled by default.
This can be disabled using

setWheelScrollingEnabled

.
Wheel scrolling can be customized by setting the block and
unit increment of the horizontal and vertical Adjustables.
For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

Insets are used to define any space used by scrollbars and any
borders created by the scroll pane. getInsets() can be used
to get the current value for the insets. If the value of
scrollbarsAlwaysVisible is false, then the value of the insets
will change dynamically depending on whether the scrollbars are
currently visible or not.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

ScrollPane.AccessibleAWTScrollPane

This class implements accessibility support for the

ScrollPane

class.

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

static int

SCROLLBARS_ALWAYS

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

static int

SCROLLBARS_AS_NEEDED

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

static int

SCROLLBARS_NEVER

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

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

ScrollPane

()

Create a new scrollpane container with a scrollbar display
policy of "as needed".

ScrollPane

​(int scrollbarDisplayPolicy)

Create a new scrollpane container.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this scroll pane container.

void

addNotify

()

Creates the scroll pane's peer.

void

doLayout

()

Lays out this container by resizing its child to its preferred size.

protected boolean

eventTypeEnabled

​(int type)

If wheel scrolling is enabled, we return true for MouseWheelEvents

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this ScrollPane.

Adjustable

getHAdjustable

()

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.

int

getHScrollbarHeight

()

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

int

getScrollbarDisplayPolicy

()

Returns the display policy for the scrollbars.

Point

getScrollPosition

()

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.

Adjustable

getVAdjustable

()

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.

Dimension

getViewportSize

()

Returns the current size of the scroll pane's view port.

int

getVScrollbarWidth

()

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

boolean

isWheelScrollingEnabled

()

Indicates whether or not scrolling will take place in response to
the mouse wheel.

void

layout

()

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

String

paramString

()

Returns a string representing the state of this

ScrollPane

.

void

printComponents

​(

Graphics

g)

Prints the component in this scroll pane.

protected void

processMouseWheelEvent

​(

MouseWheelEvent

e)

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container.

void

setScrollPosition

​(int x,
int y)

Scrolls to the specified position within the child component.

void

setScrollPosition

​(

Point

p)

Scrolls to the specified position within the child component.

void

setWheelScrollingEnabled

​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.

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

findComponentAt

,

findComponentAt

,

getAlignmentX

,

getAlignmentY

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

getInsets

,

getLayout

,

getListeners

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

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

isValidateRoot

,

list

,

list

,

locate

,

minimumSize

,

paint

,

paintComponents

,

preferredSize

,

print

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

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

setFocusTraversalKeysEnabled

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

ScrollPane.AccessibleAWTScrollPane

This class implements accessibility support for the

ScrollPane

class.

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

ScrollPane

class.

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

static int

SCROLLBARS_ALWAYS

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

static int

SCROLLBARS_AS_NEEDED

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

static int

SCROLLBARS_NEVER

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

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

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

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

ScrollPane

()

Create a new scrollpane container with a scrollbar display
policy of "as needed".

ScrollPane

​(int scrollbarDisplayPolicy)

Create a new scrollpane container.

---

#### Constructor Summary

Create a new scrollpane container with a scrollbar display
policy of "as needed".

Create a new scrollpane container.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this scroll pane container.

void

addNotify

()

Creates the scroll pane's peer.

void

doLayout

()

Lays out this container by resizing its child to its preferred size.

protected boolean

eventTypeEnabled

​(int type)

If wheel scrolling is enabled, we return true for MouseWheelEvents

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this ScrollPane.

Adjustable

getHAdjustable

()

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.

int

getHScrollbarHeight

()

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

int

getScrollbarDisplayPolicy

()

Returns the display policy for the scrollbars.

Point

getScrollPosition

()

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.

Adjustable

getVAdjustable

()

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.

Dimension

getViewportSize

()

Returns the current size of the scroll pane's view port.

int

getVScrollbarWidth

()

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

boolean

isWheelScrollingEnabled

()

Indicates whether or not scrolling will take place in response to
the mouse wheel.

void

layout

()

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

String

paramString

()

Returns a string representing the state of this

ScrollPane

.

void

printComponents

​(

Graphics

g)

Prints the component in this scroll pane.

protected void

processMouseWheelEvent

​(

MouseWheelEvent

e)

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container.

void

setScrollPosition

​(int x,
int y)

Scrolls to the specified position within the child component.

void

setScrollPosition

​(

Point

p)

Scrolls to the specified position within the child component.

void

setWheelScrollingEnabled

​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.

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

findComponentAt

,

findComponentAt

,

getAlignmentX

,

getAlignmentY

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

getInsets

,

getLayout

,

getListeners

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

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

isValidateRoot

,

list

,

list

,

locate

,

minimumSize

,

paint

,

paintComponents

,

preferredSize

,

print

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

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

setFocusTraversalKeysEnabled

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

Adds the specified component to this scroll pane container.

Creates the scroll pane's peer.

Lays out this container by resizing its child to its preferred size.

If wheel scrolling is enabled, we return true for MouseWheelEvents

Gets the AccessibleContext associated with this ScrollPane.

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

Returns the display policy for the scrollbars.

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.

Returns the current size of the scroll pane's view port.

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

Indicates whether or not scrolling will take place in response to
the mouse wheel.

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

Returns a string representing the state of this

ScrollPane

.

Prints the component in this scroll pane.

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

Sets the layout manager for this container.

Scrolls to the specified position within the child component.

Enables/disables scrolling in response to movement of the mouse wheel.

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

findComponentAt

,

findComponentAt

,

getAlignmentX

,

getAlignmentY

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

getInsets

,

getLayout

,

getListeners

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

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

isValidateRoot

,

list

,

list

,

locate

,

minimumSize

,

paint

,

paintComponents

,

preferredSize

,

print

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

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

setFocusTraversalKeysEnabled

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

============ FIELD DETAIL ===========

- Field Detail

- SCROLLBARS_AS_NEEDED

```java
public static final int SCROLLBARS_AS_NEEDED
```

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

**See Also:** Constant Field Values

- SCROLLBARS_ALWAYS

```java
public static final int SCROLLBARS_ALWAYS
```

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

**See Also:** Constant Field Values

- SCROLLBARS_NEVER

```java
public static final int SCROLLBARS_NEVER
```

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ScrollPane

```java
public ScrollPane()
throws
HeadlessException
```

Create a new scrollpane container with a scrollbar display
policy of "as needed".

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- ScrollPane

```java
@ConstructorProperties
("scrollbarDisplayPolicy")
public ScrollPane​(int scrollbarDisplayPolicy)
throws
HeadlessException
```

Create a new scrollpane container.

**Parameters:** scrollbarDisplayPolicy

- policy for when scrollbars should be shown
**Throws:** IllegalArgumentException

- if the specified scrollbar
display policy is invalid
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- addImpl

```java
protected final void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this scroll pane container.
If the scroll pane has an existing child component, that
component is removed and the new one is added.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- not applicable
**Parameters:** index

- position of child component (must be <= 0)
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

- getScrollbarDisplayPolicy

```java
public int getScrollbarDisplayPolicy()
```

Returns the display policy for the scrollbars.

**Returns:** the display policy for the scrollbars

- getViewportSize

```java
public
Dimension
getViewportSize()
```

Returns the current size of the scroll pane's view port.

**Returns:** the size of the view port in pixels

- getHScrollbarHeight

```java
public int getHScrollbarHeight()
```

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:** the height of a horizontal scrollbar in pixels

- getVScrollbarWidth

```java
public int getVScrollbarWidth()
```

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:** the width of a vertical scrollbar in pixels

- getVAdjustable

```java
public
Adjustable
getVAdjustable()
```

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:** the vertical scrollbar state
**See Also:** ScrollPaneAdjustable

- getHAdjustable

```java
public
Adjustable
getHAdjustable()
```

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:** the horizontal scrollbar state
**See Also:** ScrollPaneAdjustable

- setScrollPosition

```java
public void setScrollPosition​(int x,
int y)
```

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child. Specifying a position outside of the legal scrolling bounds
of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:** x

- the x position to scroll to
**Parameters:** y

- the y position to scroll to
**Throws:** NullPointerException

- if the scrollpane does not contain
a child

- setScrollPosition

```java
public void setScrollPosition​(
Point
p)
```

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child and the specified position is within legal scrolling bounds
of the child. Specifying a position outside of the legal scrolling
bounds of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:** p

- the Point representing the position to scroll to
**Throws:** NullPointerException

- if

p

is

null

- getScrollPosition

```java
public
Point
getScrollPosition()
```

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.
This is a convenience method which interfaces with the adjustable
objects which represent the state of the scrollbars.

**Returns:** the coordinate position for the current scroll position
**Throws:** NullPointerException

- if the scrollpane does not contain
a child

- setLayout

```java
public final void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container. This method is
overridden to prevent the layout mgr from being set.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- doLayout

```java
public void doLayout()
```

Lays out this container by resizing its child to its preferred size.
If the new preferred size of the child causes the current scroll
position to be invalid, the scroll position is set to the closest
valid position.

**Overrides:** doLayout

in class

Container
**See Also:** Component.validate()

- layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

**Overrides:** layout

in class

Container

- printComponents

```java
public void printComponents​(
Graphics
g)
```

Prints the component in this scroll pane.

**Overrides:** printComponents

in class

Container
**Parameters:** g

- the specified Graphics window
**See Also:** Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

- addNotify

```java
public void addNotify()
```

Creates the scroll pane's peer.

**Overrides:** addNotify

in class

Container
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- paramString

```java
public
String
paramString()
```

Returns a string representing the state of this

ScrollPane

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this scroll pane

- processMouseWheelEvent

```java
protected void processMouseWheelEvent​(
MouseWheelEvent
e)
```

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processMouseWheelEvent

in class

Component
**Parameters:** e

- the mouse wheel event
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

Component.addMouseWheelListener(java.awt.event.MouseWheelListener)

,

Component.enableEvents(long)

- eventTypeEnabled

```java
protected boolean eventTypeEnabled​(int type)
```

If wheel scrolling is enabled, we return true for MouseWheelEvents

**Since:** 1.4

- setWheelScrollingEnabled

```java
public void setWheelScrollingEnabled​(boolean handleWheel)
```

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:** handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.
**Since:** 1.4
**See Also:** isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

- isWheelScrollingEnabled

```java
public boolean isWheelScrollingEnabled()
```

Indicates whether or not scrolling will take place in response to
the mouse wheel. Wheel scrolling is enabled by default.

**Returns:** true

if the wheel scrolling enabled;
otherwise

false
**Since:** 1.4
**See Also:** setWheelScrollingEnabled(boolean)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this ScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleAWTScrollPane.
A new AccessibleAWTScrollPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleAWTScrollPane that serves as the
AccessibleContext of this ScrollPane
**Since:** 1.3

Field Detail

- SCROLLBARS_AS_NEEDED

```java
public static final int SCROLLBARS_AS_NEEDED
```

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

**See Also:** Constant Field Values

- SCROLLBARS_ALWAYS

```java
public static final int SCROLLBARS_ALWAYS
```

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

**See Also:** Constant Field Values

- SCROLLBARS_NEVER

```java
public static final int SCROLLBARS_NEVER
```

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

**See Also:** Constant Field Values

---

#### Field Detail

SCROLLBARS_AS_NEEDED

```java
public static final int SCROLLBARS_AS_NEEDED
```

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

**See Also:** Constant Field Values

---

#### SCROLLBARS_AS_NEEDED

public static final int SCROLLBARS_AS_NEEDED

Specifies that horizontal/vertical scrollbar should be shown
only when the size of the child exceeds the size of the scrollpane
in the horizontal/vertical dimension.

SCROLLBARS_ALWAYS

```java
public static final int SCROLLBARS_ALWAYS
```

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

**See Also:** Constant Field Values

---

#### SCROLLBARS_ALWAYS

public static final int SCROLLBARS_ALWAYS

Specifies that horizontal/vertical scrollbars should always be
shown regardless of the respective sizes of the scrollpane and child.

SCROLLBARS_NEVER

```java
public static final int SCROLLBARS_NEVER
```

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

**See Also:** Constant Field Values

---

#### SCROLLBARS_NEVER

public static final int SCROLLBARS_NEVER

Specifies that horizontal/vertical scrollbars should never be shown
regardless of the respective sizes of the scrollpane and child.

Constructor Detail

- ScrollPane

```java
public ScrollPane()
throws
HeadlessException
```

Create a new scrollpane container with a scrollbar display
policy of "as needed".

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- ScrollPane

```java
@ConstructorProperties
("scrollbarDisplayPolicy")
public ScrollPane​(int scrollbarDisplayPolicy)
throws
HeadlessException
```

Create a new scrollpane container.

**Parameters:** scrollbarDisplayPolicy

- policy for when scrollbars should be shown
**Throws:** IllegalArgumentException

- if the specified scrollbar
display policy is invalid
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

ScrollPane

```java
public ScrollPane()
throws
HeadlessException
```

Create a new scrollpane container with a scrollbar display
policy of "as needed".

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### ScrollPane

public ScrollPane()
throws

HeadlessException

Create a new scrollpane container with a scrollbar display
policy of "as needed".

ScrollPane

```java
@ConstructorProperties
("scrollbarDisplayPolicy")
public ScrollPane​(int scrollbarDisplayPolicy)
throws
HeadlessException
```

Create a new scrollpane container.

**Parameters:** scrollbarDisplayPolicy

- policy for when scrollbars should be shown
**Throws:** IllegalArgumentException

- if the specified scrollbar
display policy is invalid
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### ScrollPane

@ConstructorProperties

("scrollbarDisplayPolicy")
public ScrollPane​(int scrollbarDisplayPolicy)
throws

HeadlessException

Create a new scrollpane container.

Method Detail

- addImpl

```java
protected final void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this scroll pane container.
If the scroll pane has an existing child component, that
component is removed and the new one is added.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- not applicable
**Parameters:** index

- position of child component (must be <= 0)
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

- getScrollbarDisplayPolicy

```java
public int getScrollbarDisplayPolicy()
```

Returns the display policy for the scrollbars.

**Returns:** the display policy for the scrollbars

- getViewportSize

```java
public
Dimension
getViewportSize()
```

Returns the current size of the scroll pane's view port.

**Returns:** the size of the view port in pixels

- getHScrollbarHeight

```java
public int getHScrollbarHeight()
```

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:** the height of a horizontal scrollbar in pixels

- getVScrollbarWidth

```java
public int getVScrollbarWidth()
```

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:** the width of a vertical scrollbar in pixels

- getVAdjustable

```java
public
Adjustable
getVAdjustable()
```

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:** the vertical scrollbar state
**See Also:** ScrollPaneAdjustable

- getHAdjustable

```java
public
Adjustable
getHAdjustable()
```

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:** the horizontal scrollbar state
**See Also:** ScrollPaneAdjustable

- setScrollPosition

```java
public void setScrollPosition​(int x,
int y)
```

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child. Specifying a position outside of the legal scrolling bounds
of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:** x

- the x position to scroll to
**Parameters:** y

- the y position to scroll to
**Throws:** NullPointerException

- if the scrollpane does not contain
a child

- setScrollPosition

```java
public void setScrollPosition​(
Point
p)
```

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child and the specified position is within legal scrolling bounds
of the child. Specifying a position outside of the legal scrolling
bounds of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:** p

- the Point representing the position to scroll to
**Throws:** NullPointerException

- if

p

is

null

- getScrollPosition

```java
public
Point
getScrollPosition()
```

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.
This is a convenience method which interfaces with the adjustable
objects which represent the state of the scrollbars.

**Returns:** the coordinate position for the current scroll position
**Throws:** NullPointerException

- if the scrollpane does not contain
a child

- setLayout

```java
public final void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container. This method is
overridden to prevent the layout mgr from being set.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- doLayout

```java
public void doLayout()
```

Lays out this container by resizing its child to its preferred size.
If the new preferred size of the child causes the current scroll
position to be invalid, the scroll position is set to the closest
valid position.

**Overrides:** doLayout

in class

Container
**See Also:** Component.validate()

- layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

**Overrides:** layout

in class

Container

- printComponents

```java
public void printComponents​(
Graphics
g)
```

Prints the component in this scroll pane.

**Overrides:** printComponents

in class

Container
**Parameters:** g

- the specified Graphics window
**See Also:** Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

- addNotify

```java
public void addNotify()
```

Creates the scroll pane's peer.

**Overrides:** addNotify

in class

Container
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- paramString

```java
public
String
paramString()
```

Returns a string representing the state of this

ScrollPane

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this scroll pane

- processMouseWheelEvent

```java
protected void processMouseWheelEvent​(
MouseWheelEvent
e)
```

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processMouseWheelEvent

in class

Component
**Parameters:** e

- the mouse wheel event
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

Component.addMouseWheelListener(java.awt.event.MouseWheelListener)

,

Component.enableEvents(long)

- eventTypeEnabled

```java
protected boolean eventTypeEnabled​(int type)
```

If wheel scrolling is enabled, we return true for MouseWheelEvents

**Since:** 1.4

- setWheelScrollingEnabled

```java
public void setWheelScrollingEnabled​(boolean handleWheel)
```

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:** handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.
**Since:** 1.4
**See Also:** isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

- isWheelScrollingEnabled

```java
public boolean isWheelScrollingEnabled()
```

Indicates whether or not scrolling will take place in response to
the mouse wheel. Wheel scrolling is enabled by default.

**Returns:** true

if the wheel scrolling enabled;
otherwise

false
**Since:** 1.4
**See Also:** setWheelScrollingEnabled(boolean)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this ScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleAWTScrollPane.
A new AccessibleAWTScrollPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleAWTScrollPane that serves as the
AccessibleContext of this ScrollPane
**Since:** 1.3

---

#### Method Detail

addImpl

```java
protected final void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this scroll pane container.
If the scroll pane has an existing child component, that
component is removed and the new one is added.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- not applicable
**Parameters:** index

- position of child component (must be <= 0)
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

---

#### addImpl

protected final void addImpl​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this scroll pane container.
If the scroll pane has an existing child component, that
component is removed and the new one is added.

getScrollbarDisplayPolicy

```java
public int getScrollbarDisplayPolicy()
```

Returns the display policy for the scrollbars.

**Returns:** the display policy for the scrollbars

---

#### getScrollbarDisplayPolicy

public int getScrollbarDisplayPolicy()

Returns the display policy for the scrollbars.

getViewportSize

```java
public
Dimension
getViewportSize()
```

Returns the current size of the scroll pane's view port.

**Returns:** the size of the view port in pixels

---

#### getViewportSize

public

Dimension

getViewportSize()

Returns the current size of the scroll pane's view port.

getHScrollbarHeight

```java
public int getHScrollbarHeight()
```

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:** the height of a horizontal scrollbar in pixels

---

#### getHScrollbarHeight

public int getHScrollbarHeight()

Returns the height that would be occupied by a horizontal
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

getVScrollbarWidth

```java
public int getVScrollbarWidth()
```

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

**Returns:** the width of a vertical scrollbar in pixels

---

#### getVScrollbarWidth

public int getVScrollbarWidth()

Returns the width that would be occupied by a vertical
scrollbar, which is independent of whether it is currently
displayed by the scroll pane or not.

getVAdjustable

```java
public
Adjustable
getVAdjustable()
```

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:** the vertical scrollbar state
**See Also:** ScrollPaneAdjustable

---

#### getVAdjustable

public

Adjustable

getVAdjustable()

Returns the

ScrollPaneAdjustable

object which
represents the state of the vertical scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

getHAdjustable

```java
public
Adjustable
getHAdjustable()
```

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

**Returns:** the horizontal scrollbar state
**See Also:** ScrollPaneAdjustable

---

#### getHAdjustable

public

Adjustable

getHAdjustable()

Returns the

ScrollPaneAdjustable

object which
represents the state of the horizontal scrollbar.
The declared return type of this method is

Adjustable

to maintain backward compatibility.

setScrollPosition

```java
public void setScrollPosition​(int x,
int y)
```

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child. Specifying a position outside of the legal scrolling bounds
of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:** x

- the x position to scroll to
**Parameters:** y

- the y position to scroll to
**Throws:** NullPointerException

- if the scrollpane does not contain
a child

---

#### setScrollPosition

public void setScrollPosition​(int x,
int y)

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child. Specifying a position outside of the legal scrolling bounds
of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

setScrollPosition

```java
public void setScrollPosition​(
Point
p)
```

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child and the specified position is within legal scrolling bounds
of the child. Specifying a position outside of the legal scrolling
bounds of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

**Parameters:** p

- the Point representing the position to scroll to
**Throws:** NullPointerException

- if

p

is

null

---

#### setScrollPosition

public void setScrollPosition​(

Point

p)

Scrolls to the specified position within the child component.
A call to this method is only valid if the scroll pane contains
a child and the specified position is within legal scrolling bounds
of the child. Specifying a position outside of the legal scrolling
bounds of the child will scroll to the closest legal position.
Legal bounds are defined to be the rectangle:
x = 0, y = 0, width = (child width - view port width),
height = (child height - view port height).
This is a convenience method which interfaces with the Adjustable
objects which represent the state of the scrollbars.

getScrollPosition

```java
public
Point
getScrollPosition()
```

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.
This is a convenience method which interfaces with the adjustable
objects which represent the state of the scrollbars.

**Returns:** the coordinate position for the current scroll position
**Throws:** NullPointerException

- if the scrollpane does not contain
a child

---

#### getScrollPosition

public

Point

getScrollPosition()

Returns the current x,y position within the child which is displayed
at the 0,0 location of the scrolled panel's view port.
This is a convenience method which interfaces with the adjustable
objects which represent the state of the scrollbars.

setLayout

```java
public final void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container. This method is
overridden to prevent the layout mgr from being set.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

---

#### setLayout

public final void setLayout​(

LayoutManager

mgr)

Sets the layout manager for this container. This method is
overridden to prevent the layout mgr from being set.

doLayout

```java
public void doLayout()
```

Lays out this container by resizing its child to its preferred size.
If the new preferred size of the child causes the current scroll
position to be invalid, the scroll position is set to the closest
valid position.

**Overrides:** doLayout

in class

Container
**See Also:** Component.validate()

---

#### doLayout

public void doLayout()

Lays out this container by resizing its child to its preferred size.
If the new preferred size of the child causes the current scroll
position to be invalid, the scroll position is set to the closest
valid position.

layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

**Overrides:** layout

in class

Container

---

#### layout

@Deprecated

public void layout()

printComponents

```java
public void printComponents​(
Graphics
g)
```

Prints the component in this scroll pane.

**Overrides:** printComponents

in class

Container
**Parameters:** g

- the specified Graphics window
**See Also:** Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

---

#### printComponents

public void printComponents​(

Graphics

g)

Prints the component in this scroll pane.

addNotify

```java
public void addNotify()
```

Creates the scroll pane's peer.

**Overrides:** addNotify

in class

Container
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

---

#### addNotify

public void addNotify()

Creates the scroll pane's peer.

paramString

```java
public
String
paramString()
```

Returns a string representing the state of this

ScrollPane

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this scroll pane

---

#### paramString

public

String

paramString()

Returns a string representing the state of this

ScrollPane

. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

processMouseWheelEvent

```java
protected void processMouseWheelEvent​(
MouseWheelEvent
e)
```

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processMouseWheelEvent

in class

Component
**Parameters:** e

- the mouse wheel event
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

Component.addMouseWheelListener(java.awt.event.MouseWheelListener)

,

Component.enableEvents(long)

---

#### processMouseWheelEvent

protected void processMouseWheelEvent​(

MouseWheelEvent

e)

Process mouse wheel events that are delivered to this

ScrollPane

by scrolling an appropriate amount.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

eventTypeEnabled

```java
protected boolean eventTypeEnabled​(int type)
```

If wheel scrolling is enabled, we return true for MouseWheelEvents

**Since:** 1.4

---

#### eventTypeEnabled

protected boolean eventTypeEnabled​(int type)

If wheel scrolling is enabled, we return true for MouseWheelEvents

setWheelScrollingEnabled

```java
public void setWheelScrollingEnabled​(boolean handleWheel)
```

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:** handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.
**Since:** 1.4
**See Also:** isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

---

#### setWheelScrollingEnabled

public void setWheelScrollingEnabled​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

isWheelScrollingEnabled

```java
public boolean isWheelScrollingEnabled()
```

Indicates whether or not scrolling will take place in response to
the mouse wheel. Wheel scrolling is enabled by default.

**Returns:** true

if the wheel scrolling enabled;
otherwise

false
**Since:** 1.4
**See Also:** setWheelScrollingEnabled(boolean)

---

#### isWheelScrollingEnabled

public boolean isWheelScrollingEnabled()

Indicates whether or not scrolling will take place in response to
the mouse wheel. Wheel scrolling is enabled by default.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this ScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleAWTScrollPane.
A new AccessibleAWTScrollPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleAWTScrollPane that serves as the
AccessibleContext of this ScrollPane
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this ScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleAWTScrollPane.
A new AccessibleAWTScrollPane instance is created if necessary.

---

