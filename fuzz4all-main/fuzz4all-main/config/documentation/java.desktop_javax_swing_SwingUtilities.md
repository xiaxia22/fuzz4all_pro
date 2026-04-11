# Class SwingUtilities

**Source:** `java.desktop\javax\swing\SwingUtilities.html`

### Class Description

```java
public class
SwingUtilities

extends
Object

implements
SwingConstants
```

A collection of utility methods for Swing.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static final boolean isRectangleContainingRectangle​(
Rectangle
a,

Rectangle
b)

Return

true

if @{code a} contains

b

**Parameters:**
- a

- the first rectangle
- b

- the second rectangle

**Returns:**
- true

if @{code a} contains

b

---

#### public static
Rectangle
getLocalBounds​(
Component
aComponent)

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

**Parameters:**
- aComponent

- a component

**Returns:**
- the local bounds for the component

aComponent

---

#### public static
Window
getWindowAncestor​(
Component
c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

**Parameters:**
- c

-

Component

to get

Window

ancestor
of.

**Returns:**
- the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

**Since:**
- 1.3

---

#### public static
Point
convertPoint​(
Component
source,

Point
aPoint,

Component
destination)

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aPoint

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aPoint

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aPoint

without any conversion.

**Parameters:**
- source

- the source component
- aPoint

- the point
- destination

- the destination component

**Returns:**
- the converted coordinate

---

#### public static
Point
convertPoint​(
Component
source,
int x,
int y,

Component
destination)

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

(x,y)

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

(x,y)

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

(x,y)

without any conversion.

**Parameters:**
- source

- the source component
- x

- the x-coordinate of the point
- y

- the y-coordinate of the point
- destination

- the destination component

**Returns:**
- the converted coordinate

---

#### public static
Rectangle
convertRectangle​(
Component
source,

Rectangle
aRectangle,

Component
destination)

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aRectangle

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aRectangle

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aRectangle

without any conversion.

**Parameters:**
- source

- the source component
- aRectangle

- a rectangle
- destination

- the destination component

**Returns:**
- the converted rectangle

---

#### public static
Container
getAncestorOfClass​(
Class
<?> c,

Component
comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds. Can return

null

, if a class

c

cannot be found.

**Parameters:**
- c

- the class of a component
- comp

- the component

**Returns:**
- the ancestor of the

comp

,
or

null

if

c

cannot be found.

---

#### public static
Container
getAncestorNamed​(
String
name,

Component
comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds. Can return

null

, if

name

cannot be found.

**Parameters:**
- name

- the name of a component
- comp

- the component

**Returns:**
- the ancestor of the

comp

,
or

null

if

name

cannot be found.

---

#### public static
Component
getDeepestComponentAt​(
Component
parent,
int x,
int y)

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.
If

parent

does not contain the specified location,
then

null

is returned. If

parent

is not a
container, or none of

parent

's visible descendents
contain the specified location,

parent

is returned.

**Parameters:**
- parent

- the root component to begin the search
- x

- the x target location
- y

- the y target location

**Returns:**
- the deepest component

---

#### public static
MouseEvent
convertMouseEvent​(
Component
source,

MouseEvent
sourceEvent,

Component
destination)

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system. If

source

is

null

,

sourceEvent

x and y members
are assumed to be into

destination

's root component coordinate system.
If

destination

is

null

, the
returned MouseEvent will be in

source

's coordinate system.

sourceEvent

will not be changed. A new event is returned.
the

source

field of the returned event will be set
to

destination

if destination is non-

null

use the translateMouseEvent() method to translate a mouse event from
one component to another without changing the source.

**Parameters:**
- source

- the source component
- sourceEvent

- the source mouse event
- destination

- the destination component

**Returns:**
- the new mouse event

---

#### public static void convertPointToScreen​(
Point
p,

Component
c)

Convert a point from a component's coordinate system to
screen coordinates.

**Parameters:**
- p

- a Point object (converted to the new coordinate system)
- c

- a Component object

---

#### public static void convertPointFromScreen​(
Point
p,

Component
c)

Convert a point from a screen coordinates to a component's
coordinate system

**Parameters:**
- p

- a Point object (converted to the new coordinate system)
- c

- a Component object

---

#### public static
Window
windowForComponent​(
Component
c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

Note: This method provides the same functionality as

getWindowAncestor

.

**Parameters:**
- c

-

Component

to get

Window

ancestor
of.

**Returns:**
- the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

---

#### public static boolean isDescendingFrom​(
Component
a,

Component
b)

Return

true

if a component

a

descends from a component

b

**Parameters:**
- a

- the first component
- b

- the second component

**Returns:**
- true

if a component

a

descends from a component

b

---

#### public static
Rectangle
computeIntersection​(int x,
int y,
int width,
int height,

Rectangle
dest)

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.
If the two rectangles don't intersect,
then the returned rectangle begins at (0,0)
and has zero width and height.

**Parameters:**
- x

- the X coordinate of the first rectangle's top-left point
- y

- the Y coordinate of the first rectangle's top-left point
- width

- the width of the first rectangle
- height

- the height of the first rectangle
- dest

- the second rectangle

**Returns:**
- dest

, modified to specify the intersection

---

#### public static
Rectangle
computeUnion​(int x,
int y,
int width,
int height,

Rectangle
dest)

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

**Parameters:**
- x

- the x-coordinate of the first rectangle
- y

- the y-coordinate of the first rectangle
- width

- the width of the first rectangle
- height

- the height of the first rectangle
- dest

- the coordinates of the second rectangle; the union
of the two rectangles is returned in this rectangle

**Returns:**
- the

dest

Rectangle

---

#### public static
Rectangle
[] computeDifference​(
Rectangle
rectA,

Rectangle
rectB)

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

. If the
two Rects do not overlap, returns an empty array

**Parameters:**
- rectA

- the first rectangle
- rectB

- the second rectangle

**Returns:**
- an array of rectangles representing the regions within

rectA

that do not overlap with

rectB

.

---

#### public static boolean isLeftMouseButton​(
MouseEvent
anEvent)

Returns true if the mouse event specifies the left mouse button.

**Parameters:**
- anEvent

- a MouseEvent object

**Returns:**
- true if the left mouse button was active

---

#### public static boolean isMiddleMouseButton​(
MouseEvent
anEvent)

Returns true if the mouse event specifies the middle mouse button.

**Parameters:**
- anEvent

- a MouseEvent object

**Returns:**
- true if the middle mouse button was active

---

#### public static boolean isRightMouseButton​(
MouseEvent
anEvent)

Returns true if the mouse event specifies the right mouse button.

**Parameters:**
- anEvent

- a MouseEvent object

**Returns:**
- true if the right mouse button was active

---

#### public static int computeStringWidth​(
FontMetrics
fm,

String
str)

Compute the width of the string using a font with the specified
"metrics" (sizes).

**Parameters:**
- fm

- a FontMetrics object to compute with
- str

- the String to compute

**Returns:**
- an int containing the string width

---

#### public static
String
layoutCompoundLabel​(
JComponent
c,

FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
The JComponents orientation (LEADING/TRAILING) will also be taken
into account and translated into LEFT/RIGHT values accordingly.

**Parameters:**
- c

- the component
- fm

- the instance of

FontMetrics
- text

- the text
- icon

- the icon
- verticalAlignment

- the vertical alignment
- horizontalAlignment

- the horizontal alignment
- verticalTextPosition

- the vertical text position
- horizontalTextPosition

- the horizontal text position
- viewR

- the available rectangle
- iconR

- the rectangle for the icon
- textR

- the rectangle for the text
- textIconGap

- the gap between text and icon

**Returns:**
- the possibly clipped version of the compound labels string

---

#### public static
String
layoutCompoundLabel​(
FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
This layoutCompoundLabel() does not know how to handle LEADING/TRAILING
values in horizontalTextPosition (they will default to RIGHT) and in
horizontalAlignment (they will default to CENTER).
Use the other version of layoutCompoundLabel() instead.

**Parameters:**
- fm

- the instance of

FontMetrics
- text

- the text
- icon

- the icon
- verticalAlignment

- the vertical alignment
- horizontalAlignment

- the horizontal alignment
- verticalTextPosition

- the vertical text position
- horizontalTextPosition

- the horizontal text position
- viewR

- the available rectangle
- iconR

- the rectangle for the icon
- textR

- the rectangle for the text
- textIconGap

- the gap between text and icon

**Returns:**
- the possibly clipped version of the compound labels string

---

#### public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,
int x,
int y,
int w,
int h)

Paints a component to the specified

Graphics

.
This method is primarily useful to render

Component

s that don't exist as part of the visible
containment hierarchy, but are used for rendering. For
example, if you are doing your own rendering and want to render
some text (or even HTML), you could make use of

JLabel

's text rendering support and have it paint
directly by way of this method, without adding the label to the
visible containment hierarchy.

This method makes use of

CellRendererPane

to handle
the actual painting, and is only recommended if you use one
component for rendering. If you make use of multiple components
to handle the rendering, as

JTable

does, use

CellRendererPane

directly. Otherwise, as described
below, you could end up with a

CellRendererPane

per

Component

.

If

c

's parent is not a

CellRendererPane

,
a new

CellRendererPane

is created,

c

is
added to it, and the

CellRendererPane

is added to

p

. If

c

's parent is a

CellRendererPane

and the

CellRendererPane

s
parent is not

p

, it is added to

p

.

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

**Parameters:**
- g

- the

Graphics

object to draw on
- c

- the

Component

to draw
- p

- the intermediate

Container
- x

- an int specifying the left side of the area draw in, in pixels,
measured from the left edge of the graphics context
- y

- an int specifying the top of the area to draw in, in pixels
measured down from the top edge of the graphics context
- w

- an int specifying the width of the area draw in, in pixels
- h

- an int specifying the height of the area draw in, in pixels

**See Also:**
- CellRendererPane

,

Component.isLightweight()

---

#### public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,

Rectangle
r)

Paints a component to the specified

Graphics

. This
is a cover method for

paintComponent(Graphics,Component,Container,int,int,int,int)

.
Refer to it for more information.

**Parameters:**
- g

- the

Graphics

object to draw on
- c

- the

Component

to draw
- p

- the intermediate

Container
- r

- the

Rectangle

to draw in

**See Also:**
- paintComponent(Graphics,Component,Container,int,int,int,int)

,

CellRendererPane

---

#### public static void updateComponentTreeUI​(
Component
c)

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

**Parameters:**
- c

- the component

---

#### public static void invokeLater​(
Runnable
doRun)

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread. This will happen after all
pending AWT events have been processed. This method should
be used when an application thread needs to update the GUI.
In the following example the

invokeLater

call queues
the

Runnable

object

doHelloWorld

on the event dispatching thread and
then prints a message.

```java
Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

SwingUtilities.invokeLater(doHelloWorld);
System.out.println("This might well be displayed before the other message.");
```

If invokeLater is called from the event dispatching thread --
for example, from a JButton's ActionListener -- the

doRun.run()

will
still be deferred until all pending events have been processed.
Note that if the

doRun.run()

throws an uncaught exception
the event dispatching thread will unwind (not the current thread).

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeLater()

.

Unlike the rest of Swing, this method can be invoked from any thread.

**Parameters:**
- doRun

- the instance of

Runnable

**See Also:**
- invokeAndWait(java.lang.Runnable)

---

#### public static void invokeAndWait​(
Runnable
doRun)
throws
InterruptedException
,

InvocationTargetException

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread. This call blocks until
all pending AWT events have been processed and (then)

doRun.run()

returns. This method should
be used when an application thread needs to update the GUI.
It shouldn't be called from the event dispatching thread.
Here's an example that creates a new application thread
that uses

invokeAndWait

to print a string from the event
dispatching thread and then, when that's finished, print
a string from the application thread.

```java
final Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

Thread appThread = new Thread() {
public void run() {
try {
SwingUtilities.invokeAndWait(doHelloWorld);
}
catch (Exception e) {
e.printStackTrace();
}
System.out.println("Finished on " + Thread.currentThread());
}
};
appThread.start();
```

Note that if the

Runnable.run

method throws an
uncaught exception
(on the event dispatching thread) it's caught and rethrown, as
an

InvocationTargetException

, on the caller's thread.

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeAndWait()

.

**Parameters:**
- doRun

- the instance of

Runnable

**Throws:**
- InterruptedException

- if we're interrupted while waiting for
the event dispatching thread to finish executing

doRun.run()
- InvocationTargetException

- if an exception is thrown
while running

doRun

**See Also:**
- invokeLater(java.lang.Runnable)

---

#### public static boolean isEventDispatchThread()

Returns true if the current thread is an AWT event dispatching thread.

As of 1.3 this method is just a cover for

java.awt.EventQueue.isDispatchThread()

.

**Returns:**
- true if the current thread is an AWT event dispatching thread

---

#### public static int getAccessibleIndexInParent​(
Component
c)

Get the index of this object in its accessible parent.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:**
- c

- the component

**Returns:**
- -1 of this object does not have an accessible parent.
Otherwise, the index of the child in its accessible parent.

---

#### public static
Accessible
getAccessibleAt​(
Component
c,

Point
p)

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.
Otherwise returns

null

.

**Parameters:**
- c

- the component
- p

- the local coordinate

**Returns:**
- the

Accessible

at the specified location,
if it exists; otherwise

null

---

#### public static
AccessibleStateSet
getAccessibleStateSet​(
Component
c)

Get the state of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:**
- c

- the component

**Returns:**
- an instance of AccessibleStateSet containing the current state
set of the object

**See Also:**
- AccessibleState

---

#### public static int getAccessibleChildrenCount​(
Component
c)

Returns the number of accessible children in the object. If all
of the children of this object implement Accessible, than this
method should return the number of children of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:**
- c

- the component

**Returns:**
- the number of accessible children in the object.

---

#### public static
Accessible
getAccessibleChild​(
Component
c,
int i)

Return the nth Accessible child of the object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:**
- c

- the component
- i

- zero-based index of child

**Returns:**
- the nth Accessible child of the object

---

#### @Deprecated

public static
Component
findFocusOwner​(
Component
c)

Return the child

Component

of the specified

Component

that is the focus owner, if any.

**Parameters:**
- c

- the root of the

Component

hierarchy to
search for the focus owner

**Returns:**
- the focus owner, or

null

if there is no focus
owner, or if the focus owner is not

comp

, or a
descendant of

comp

**See Also:**
- KeyboardFocusManager.getFocusOwner()

---

#### public static
JRootPane
getRootPane​(
Component
c)

If c is a JRootPane descendant return its JRootPane ancestor.
If c is a RootPaneContainer then return its JRootPane.

**Parameters:**
- c

- the component

**Returns:**
- the JRootPane for Component c or

null

.

---

#### public static
Component
getRoot​(
Component
c)

Returns the root component for the current component tree.

**Parameters:**
- c

- the component

**Returns:**
- the first ancestor of c that's a Window or the last Applet ancestor

---

#### public static boolean processKeyBindings​(
KeyEvent
event)

Process the key bindings for the

Component

associated with

event

. This method is only useful if

event.getComponent()

does not descend from

JComponent

, or your are not invoking

super.processKeyEvent

from within your

JComponent

subclass.

JComponent

automatically processes bindings from within its

processKeyEvent

method, hence you rarely need
to directly invoke this method.

**Parameters:**
- event

- KeyEvent used to identify which bindings to process, as
well as which Component has focus.

**Returns:**
- true if a binding has found and processed

**Since:**
- 1.4

---

#### public static boolean notifyAction​(
Action
action,

KeyStroke
ks,

KeyEvent
event,

Object
sender,
int modifiers)

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.
The command for the ActionEvent is determined by:

- If the action was registered via

registerKeyboardAction

, then the command string
passed in (

null

will be used if

null

was passed in).

Action value with name Action.ACTION_COMMAND_KEY, unless

null

.

String value of the KeyEvent, unless

getKeyChar

returns KeyEvent.CHAR_UNDEFINED..

This will return true if

action

is non-

null

and
actionPerformed is invoked on it.

**Parameters:**
- action

- an action
- ks

- a key stroke
- event

- a key event
- sender

- a sender
- modifiers

- action modifiers

**Returns:**
- true

if

action

is non-

null

and
actionPerformed is invoked on it.

**See Also:**
- Action.accept(java.lang.Object)

**Since:**
- 1.3

---

#### public static void replaceUIInputMap​(
JComponent
component,
int type,

InputMap
uiInputMap)

Convenience method to change the UI InputMap for

component

to

uiInputMap

. If

uiInputMap

is

null

,
this removes any previously installed UI InputMap.

**Parameters:**
- component

- a component
- type

- a type
- uiInputMap

- an

InputMap

**Since:**
- 1.3

---

#### public static void replaceUIActionMap​(
JComponent
component,

ActionMap
uiActionMap)

Convenience method to change the UI ActionMap for

component

to

uiActionMap

. If

uiActionMap

is

null

,
this removes any previously installed UI ActionMap.

**Parameters:**
- component

- a component
- uiActionMap

- an

ActionMap

**Since:**
- 1.3

---

#### public static
InputMap
getUIInputMap​(
JComponent
component,
int condition)

Returns the InputMap provided by the UI for condition

condition

in component

component

.

This will return

null

if the UI has not installed an InputMap
of the specified type.

**Parameters:**
- component

- a component
- condition

- a condition

**Returns:**
- the

ActionMap

provided by the UI for

condition

in the component, or

null

if the UI has not installed
an InputMap of the specified type.

**Since:**
- 1.3

---

#### public static
ActionMap
getUIActionMap​(
JComponent
component)

Returns the ActionMap provided by the UI
in component

component

.

This will return

null

if the UI has not installed an ActionMap.

**Parameters:**
- component

- a component

**Returns:**
- the

ActionMap

provided by the UI in the component,
or

null

if the UI has not installed an ActionMap.

**Since:**
- 1.3

---

#### public static
Rectangle
calculateInnerArea​(
JComponent
c,

Rectangle
r)

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.
The position and size specify the bounds of the component,
adjusted so as not to include the border area (the insets).
This method is useful for classes
that implement painting code.

**Parameters:**
- c

- the JComponent in question; if

null

, this method returns

null
- r

- the Rectangle instance to be modified;
may be

null

**Returns:**
- null

if the Component is

null

;
otherwise, returns the passed-in rectangle (if non-

null

)
or a new rectangle specifying position and size information

**Since:**
- 1.4

---

#### public static
Container
getUnwrappedParent​(
Component
component)

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

**Parameters:**
- component

-

Component

to get
the first ancestor of, which is not a

JLayer

instance.

**Returns:**
- the first ancestor of the

component

which is not an instance of

JLayer

.
If such an ancestor can not be found,

null

is returned.

**Throws:**
- NullPointerException

- if

component

is

null

**See Also:**
- JLayer

**Since:**
- 1.7

---

#### public static
Component
getUnwrappedView​(
JViewport
viewport)

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.

If the

viewport

's view component is not a

JLayer

,
this method is equivalent to

JViewport.getView()

otherwise

JLayer.getView()

will be recursively
called on all descending

JLayer

s.

**Parameters:**
- viewport

-

JViewport

to get the first descendant of,
which in not a

JLayer

instance.

**Returns:**
- the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.

**Throws:**
- NullPointerException

- if

viewport

is

null

**See Also:**
- JViewport.getView()

,

JLayer

**Since:**
- 1.7

---

### Additional Sections

#### Class SwingUtilities

java.lang.Object

- javax.swing.SwingUtilities

javax.swing.SwingUtilities

**All Implemented Interfaces:** SwingConstants

```java
public class
SwingUtilities

extends
Object

implements
SwingConstants
```

A collection of utility methods for Swing.

**Since:** 1.2

public class

SwingUtilities

extends

Object

implements

SwingConstants

A collection of utility methods for Swing.

=========== FIELD SUMMARY ===========

- Field Summary

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

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Rectangle

calculateInnerArea

​(

JComponent

c,

Rectangle

r)

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.

static

Rectangle

[]

computeDifference

​(

Rectangle

rectA,

Rectangle

rectB)

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

.

static

Rectangle

computeIntersection

​(int x,
int y,
int width,
int height,

Rectangle

dest)

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.

static int

computeStringWidth

​(

FontMetrics

fm,

String

str)

Compute the width of the string using a font with the specified
"metrics" (sizes).

static

Rectangle

computeUnion

​(int x,
int y,
int width,
int height,

Rectangle

dest)

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

static

MouseEvent

convertMouseEvent

​(

Component

source,

MouseEvent

sourceEvent,

Component

destination)

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system.

static

Point

convertPoint

​(

Component

source,
int x,
int y,

Component

destination)

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.

static

Point

convertPoint

​(

Component

source,

Point

aPoint,

Component

destination)

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.

static void

convertPointFromScreen

​(

Point

p,

Component

c)

Convert a point from a screen coordinates to a component's
coordinate system

static void

convertPointToScreen

​(

Point

p,

Component

c)

Convert a point from a component's coordinate system to
screen coordinates.

static

Rectangle

convertRectangle

​(

Component

source,

Rectangle

aRectangle,

Component

destination)

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.

static

Component

findFocusOwner

​(

Component

c)

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getFocusOwner()

.

static

Accessible

getAccessibleAt

​(

Component

c,

Point

p)

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.

static

Accessible

getAccessibleChild

​(

Component

c,
int i)

Return the nth Accessible child of the object.

static int

getAccessibleChildrenCount

​(

Component

c)

Returns the number of accessible children in the object.

static int

getAccessibleIndexInParent

​(

Component

c)

Get the index of this object in its accessible parent.

static

AccessibleStateSet

getAccessibleStateSet

​(

Component

c)

Get the state of this object.

static

Container

getAncestorNamed

​(

String

name,

Component

comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds.

static

Container

getAncestorOfClass

​(

Class

<?> c,

Component

comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds.

static

Component

getDeepestComponentAt

​(

Component

parent,
int x,
int y)

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.

static

Rectangle

getLocalBounds

​(

Component

aComponent)

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

static

Component

getRoot

​(

Component

c)

Returns the root component for the current component tree.

static

JRootPane

getRootPane

​(

Component

c)

If c is a JRootPane descendant return its JRootPane ancestor.

static

ActionMap

getUIActionMap

​(

JComponent

component)

Returns the ActionMap provided by the UI
in component

component

.

static

InputMap

getUIInputMap

​(

JComponent

component,
int condition)

Returns the InputMap provided by the UI for condition

condition

in component

component

.

static

Container

getUnwrappedParent

​(

Component

component)

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

static

Component

getUnwrappedView

​(

JViewport

viewport)

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.

static

Window

getWindowAncestor

​(

Component

c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

static void

invokeAndWait

​(

Runnable

doRun)

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread.

static void

invokeLater

​(

Runnable

doRun)

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread.

static boolean

isDescendingFrom

​(

Component

a,

Component

b)

Return

true

if a component

a

descends from a component

b

static boolean

isEventDispatchThread

()

Returns true if the current thread is an AWT event dispatching thread.

static boolean

isLeftMouseButton

​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the left mouse button.

static boolean

isMiddleMouseButton

​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the middle mouse button.

static boolean

isRectangleContainingRectangle

​(

Rectangle

a,

Rectangle

b)

Return

true

if @{code a} contains

b

static boolean

isRightMouseButton

​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the right mouse button.

static

String

layoutCompoundLabel

​(

FontMetrics

fm,

String

text,

Icon

icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string.

static

String

layoutCompoundLabel

​(

JComponent

c,

FontMetrics

fm,

String

text,

Icon

icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string.

static boolean

notifyAction

​(

Action

action,

KeyStroke

ks,

KeyEvent

event,

Object

sender,
int modifiers)

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.

static void

paintComponent

​(

Graphics

g,

Component

c,

Container

p,
int x,
int y,
int w,
int h)

Paints a component to the specified

Graphics

.

static void

paintComponent

​(

Graphics

g,

Component

c,

Container

p,

Rectangle

r)

Paints a component to the specified

Graphics

.

static boolean

processKeyBindings

​(

KeyEvent

event)

Process the key bindings for the

Component

associated with

event

.

static void

replaceUIActionMap

​(

JComponent

component,

ActionMap

uiActionMap)

Convenience method to change the UI ActionMap for

component

to

uiActionMap

.

static void

replaceUIInputMap

​(

JComponent

component,
int type,

InputMap

uiInputMap)

Convenience method to change the UI InputMap for

component

to

uiInputMap

.

static void

updateComponentTreeUI

​(

Component

c)

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

static

Window

windowForComponent

​(

Component

c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

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

toString

,

wait

,

wait

,

wait

Field Summary

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Rectangle

calculateInnerArea

​(

JComponent

c,

Rectangle

r)

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.

static

Rectangle

[]

computeDifference

​(

Rectangle

rectA,

Rectangle

rectB)

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

.

static

Rectangle

computeIntersection

​(int x,
int y,
int width,
int height,

Rectangle

dest)

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.

static int

computeStringWidth

​(

FontMetrics

fm,

String

str)

Compute the width of the string using a font with the specified
"metrics" (sizes).

static

Rectangle

computeUnion

​(int x,
int y,
int width,
int height,

Rectangle

dest)

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

static

MouseEvent

convertMouseEvent

​(

Component

source,

MouseEvent

sourceEvent,

Component

destination)

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system.

static

Point

convertPoint

​(

Component

source,
int x,
int y,

Component

destination)

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.

static

Point

convertPoint

​(

Component

source,

Point

aPoint,

Component

destination)

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.

static void

convertPointFromScreen

​(

Point

p,

Component

c)

Convert a point from a screen coordinates to a component's
coordinate system

static void

convertPointToScreen

​(

Point

p,

Component

c)

Convert a point from a component's coordinate system to
screen coordinates.

static

Rectangle

convertRectangle

​(

Component

source,

Rectangle

aRectangle,

Component

destination)

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.

static

Component

findFocusOwner

​(

Component

c)

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getFocusOwner()

.

static

Accessible

getAccessibleAt

​(

Component

c,

Point

p)

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.

static

Accessible

getAccessibleChild

​(

Component

c,
int i)

Return the nth Accessible child of the object.

static int

getAccessibleChildrenCount

​(

Component

c)

Returns the number of accessible children in the object.

static int

getAccessibleIndexInParent

​(

Component

c)

Get the index of this object in its accessible parent.

static

AccessibleStateSet

getAccessibleStateSet

​(

Component

c)

Get the state of this object.

static

Container

getAncestorNamed

​(

String

name,

Component

comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds.

static

Container

getAncestorOfClass

​(

Class

<?> c,

Component

comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds.

static

Component

getDeepestComponentAt

​(

Component

parent,
int x,
int y)

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.

static

Rectangle

getLocalBounds

​(

Component

aComponent)

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

static

Component

getRoot

​(

Component

c)

Returns the root component for the current component tree.

static

JRootPane

getRootPane

​(

Component

c)

If c is a JRootPane descendant return its JRootPane ancestor.

static

ActionMap

getUIActionMap

​(

JComponent

component)

Returns the ActionMap provided by the UI
in component

component

.

static

InputMap

getUIInputMap

​(

JComponent

component,
int condition)

Returns the InputMap provided by the UI for condition

condition

in component

component

.

static

Container

getUnwrappedParent

​(

Component

component)

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

static

Component

getUnwrappedView

​(

JViewport

viewport)

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.

static

Window

getWindowAncestor

​(

Component

c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

static void

invokeAndWait

​(

Runnable

doRun)

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread.

static void

invokeLater

​(

Runnable

doRun)

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread.

static boolean

isDescendingFrom

​(

Component

a,

Component

b)

Return

true

if a component

a

descends from a component

b

static boolean

isEventDispatchThread

()

Returns true if the current thread is an AWT event dispatching thread.

static boolean

isLeftMouseButton

​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the left mouse button.

static boolean

isMiddleMouseButton

​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the middle mouse button.

static boolean

isRectangleContainingRectangle

​(

Rectangle

a,

Rectangle

b)

Return

true

if @{code a} contains

b

static boolean

isRightMouseButton

​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the right mouse button.

static

String

layoutCompoundLabel

​(

FontMetrics

fm,

String

text,

Icon

icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string.

static

String

layoutCompoundLabel

​(

JComponent

c,

FontMetrics

fm,

String

text,

Icon

icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string.

static boolean

notifyAction

​(

Action

action,

KeyStroke

ks,

KeyEvent

event,

Object

sender,
int modifiers)

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.

static void

paintComponent

​(

Graphics

g,

Component

c,

Container

p,
int x,
int y,
int w,
int h)

Paints a component to the specified

Graphics

.

static void

paintComponent

​(

Graphics

g,

Component

c,

Container

p,

Rectangle

r)

Paints a component to the specified

Graphics

.

static boolean

processKeyBindings

​(

KeyEvent

event)

Process the key bindings for the

Component

associated with

event

.

static void

replaceUIActionMap

​(

JComponent

component,

ActionMap

uiActionMap)

Convenience method to change the UI ActionMap for

component

to

uiActionMap

.

static void

replaceUIInputMap

​(

JComponent

component,
int type,

InputMap

uiInputMap)

Convenience method to change the UI InputMap for

component

to

uiInputMap

.

static void

updateComponentTreeUI

​(

Component

c)

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

static

Window

windowForComponent

​(

Component

c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

.

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.

Compute the width of the string using a font with the specified
"metrics" (sizes).

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system.

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.

Convert a point from a screen coordinates to a component's
coordinate system

Convert a point from a component's coordinate system to
screen coordinates.

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getFocusOwner()

.

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.

Return the nth Accessible child of the object.

Returns the number of accessible children in the object.

Get the index of this object in its accessible parent.

Get the state of this object.

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds.

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds.

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

Returns the root component for the current component tree.

If c is a JRootPane descendant return its JRootPane ancestor.

Returns the ActionMap provided by the UI
in component

component

.

Returns the InputMap provided by the UI for condition

condition

in component

component

.

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread.

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread.

Return

true

if a component

a

descends from a component

b

Returns true if the current thread is an AWT event dispatching thread.

Returns true if the mouse event specifies the left mouse button.

Returns true if the mouse event specifies the middle mouse button.

Return

true

if @{code a} contains

b

Returns true if the mouse event specifies the right mouse button.

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string.

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.

Paints a component to the specified

Graphics

.

Process the key bindings for the

Component

associated with

event

.

Convenience method to change the UI ActionMap for

component

to

uiActionMap

.

Convenience method to change the UI InputMap for

component

to

uiInputMap

.

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- isRectangleContainingRectangle

```java
public static final boolean isRectangleContainingRectangle​(
Rectangle
a,

Rectangle
b)
```

Return

true

if @{code a} contains

b

**Parameters:** a

- the first rectangle
**Parameters:** b

- the second rectangle
**Returns:** true

if @{code a} contains

b

- getLocalBounds

```java
public static
Rectangle
getLocalBounds​(
Component
aComponent)
```

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

**Parameters:** aComponent

- a component
**Returns:** the local bounds for the component

aComponent

- getWindowAncestor

```java
public static
Window
getWindowAncestor​(
Component
c)
```

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

**Parameters:** c

-

Component

to get

Window

ancestor
of.
**Returns:** the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.
**Since:** 1.3

- convertPoint

```java
public static
Point
convertPoint​(
Component
source,

Point
aPoint,

Component
destination)
```

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aPoint

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aPoint

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aPoint

without any conversion.

**Parameters:** source

- the source component
**Parameters:** aPoint

- the point
**Parameters:** destination

- the destination component
**Returns:** the converted coordinate

- convertPoint

```java
public static
Point
convertPoint​(
Component
source,
int x,
int y,

Component
destination)
```

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

(x,y)

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

(x,y)

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

(x,y)

without any conversion.

**Parameters:** source

- the source component
**Parameters:** x

- the x-coordinate of the point
**Parameters:** y

- the y-coordinate of the point
**Parameters:** destination

- the destination component
**Returns:** the converted coordinate

- convertRectangle

```java
public static
Rectangle
convertRectangle​(
Component
source,

Rectangle
aRectangle,

Component
destination)
```

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aRectangle

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aRectangle

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aRectangle

without any conversion.

**Parameters:** source

- the source component
**Parameters:** aRectangle

- a rectangle
**Parameters:** destination

- the destination component
**Returns:** the converted rectangle

- getAncestorOfClass

```java
public static
Container
getAncestorOfClass​(
Class
<?> c,

Component
comp)
```

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds. Can return

null

, if a class

c

cannot be found.

**Parameters:** c

- the class of a component
**Parameters:** comp

- the component
**Returns:** the ancestor of the

comp

,
or

null

if

c

cannot be found.

- getAncestorNamed

```java
public static
Container
getAncestorNamed​(
String
name,

Component
comp)
```

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds. Can return

null

, if

name

cannot be found.

**Parameters:** name

- the name of a component
**Parameters:** comp

- the component
**Returns:** the ancestor of the

comp

,
or

null

if

name

cannot be found.

- getDeepestComponentAt

```java
public static
Component
getDeepestComponentAt​(
Component
parent,
int x,
int y)
```

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.
If

parent

does not contain the specified location,
then

null

is returned. If

parent

is not a
container, or none of

parent

's visible descendents
contain the specified location,

parent

is returned.

**Parameters:** parent

- the root component to begin the search
**Parameters:** x

- the x target location
**Parameters:** y

- the y target location
**Returns:** the deepest component

- convertMouseEvent

```java
public static
MouseEvent
convertMouseEvent​(
Component
source,

MouseEvent
sourceEvent,

Component
destination)
```

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system. If

source

is

null

,

sourceEvent

x and y members
are assumed to be into

destination

's root component coordinate system.
If

destination

is

null

, the
returned MouseEvent will be in

source

's coordinate system.

sourceEvent

will not be changed. A new event is returned.
the

source

field of the returned event will be set
to

destination

if destination is non-

null

use the translateMouseEvent() method to translate a mouse event from
one component to another without changing the source.

**Parameters:** source

- the source component
**Parameters:** sourceEvent

- the source mouse event
**Parameters:** destination

- the destination component
**Returns:** the new mouse event

- convertPointToScreen

```java
public static void convertPointToScreen​(
Point
p,

Component
c)
```

Convert a point from a component's coordinate system to
screen coordinates.

**Parameters:** p

- a Point object (converted to the new coordinate system)
**Parameters:** c

- a Component object

- convertPointFromScreen

```java
public static void convertPointFromScreen​(
Point
p,

Component
c)
```

Convert a point from a screen coordinates to a component's
coordinate system

**Parameters:** p

- a Point object (converted to the new coordinate system)
**Parameters:** c

- a Component object

- windowForComponent

```java
public static
Window
windowForComponent​(
Component
c)
```

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

Note: This method provides the same functionality as

getWindowAncestor

.

**Parameters:** c

-

Component

to get

Window

ancestor
of.
**Returns:** the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

- isDescendingFrom

```java
public static boolean isDescendingFrom​(
Component
a,

Component
b)
```

Return

true

if a component

a

descends from a component

b

**Parameters:** a

- the first component
**Parameters:** b

- the second component
**Returns:** true

if a component

a

descends from a component

b

- computeIntersection

```java
public static
Rectangle
computeIntersection​(int x,
int y,
int width,
int height,

Rectangle
dest)
```

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.
If the two rectangles don't intersect,
then the returned rectangle begins at (0,0)
and has zero width and height.

**Parameters:** x

- the X coordinate of the first rectangle's top-left point
**Parameters:** y

- the Y coordinate of the first rectangle's top-left point
**Parameters:** width

- the width of the first rectangle
**Parameters:** height

- the height of the first rectangle
**Parameters:** dest

- the second rectangle
**Returns:** dest

, modified to specify the intersection

- computeUnion

```java
public static
Rectangle
computeUnion​(int x,
int y,
int width,
int height,

Rectangle
dest)
```

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

**Parameters:** x

- the x-coordinate of the first rectangle
**Parameters:** y

- the y-coordinate of the first rectangle
**Parameters:** width

- the width of the first rectangle
**Parameters:** height

- the height of the first rectangle
**Parameters:** dest

- the coordinates of the second rectangle; the union
of the two rectangles is returned in this rectangle
**Returns:** the

dest

Rectangle

- computeDifference

```java
public static
Rectangle
[] computeDifference​(
Rectangle
rectA,

Rectangle
rectB)
```

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

. If the
two Rects do not overlap, returns an empty array

**Parameters:** rectA

- the first rectangle
**Parameters:** rectB

- the second rectangle
**Returns:** an array of rectangles representing the regions within

rectA

that do not overlap with

rectB

.

- isLeftMouseButton

```java
public static boolean isLeftMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the left mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the left mouse button was active

- isMiddleMouseButton

```java
public static boolean isMiddleMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the middle mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the middle mouse button was active

- isRightMouseButton

```java
public static boolean isRightMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the right mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the right mouse button was active

- computeStringWidth

```java
public static int computeStringWidth​(
FontMetrics
fm,

String
str)
```

Compute the width of the string using a font with the specified
"metrics" (sizes).

**Parameters:** fm

- a FontMetrics object to compute with
**Parameters:** str

- the String to compute
**Returns:** an int containing the string width

- layoutCompoundLabel

```java
public static
String
layoutCompoundLabel​(
JComponent
c,

FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)
```

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
The JComponents orientation (LEADING/TRAILING) will also be taken
into account and translated into LEFT/RIGHT values accordingly.

**Parameters:** c

- the component
**Parameters:** fm

- the instance of

FontMetrics
**Parameters:** text

- the text
**Parameters:** icon

- the icon
**Parameters:** verticalAlignment

- the vertical alignment
**Parameters:** horizontalAlignment

- the horizontal alignment
**Parameters:** verticalTextPosition

- the vertical text position
**Parameters:** horizontalTextPosition

- the horizontal text position
**Parameters:** viewR

- the available rectangle
**Parameters:** iconR

- the rectangle for the icon
**Parameters:** textR

- the rectangle for the text
**Parameters:** textIconGap

- the gap between text and icon
**Returns:** the possibly clipped version of the compound labels string

- layoutCompoundLabel

```java
public static
String
layoutCompoundLabel​(
FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)
```

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
This layoutCompoundLabel() does not know how to handle LEADING/TRAILING
values in horizontalTextPosition (they will default to RIGHT) and in
horizontalAlignment (they will default to CENTER).
Use the other version of layoutCompoundLabel() instead.

**Parameters:** fm

- the instance of

FontMetrics
**Parameters:** text

- the text
**Parameters:** icon

- the icon
**Parameters:** verticalAlignment

- the vertical alignment
**Parameters:** horizontalAlignment

- the horizontal alignment
**Parameters:** verticalTextPosition

- the vertical text position
**Parameters:** horizontalTextPosition

- the horizontal text position
**Parameters:** viewR

- the available rectangle
**Parameters:** iconR

- the rectangle for the icon
**Parameters:** textR

- the rectangle for the text
**Parameters:** textIconGap

- the gap between text and icon
**Returns:** the possibly clipped version of the compound labels string

- paintComponent

```java
public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,
int x,
int y,
int w,
int h)
```

Paints a component to the specified

Graphics

.
This method is primarily useful to render

Component

s that don't exist as part of the visible
containment hierarchy, but are used for rendering. For
example, if you are doing your own rendering and want to render
some text (or even HTML), you could make use of

JLabel

's text rendering support and have it paint
directly by way of this method, without adding the label to the
visible containment hierarchy.

This method makes use of

CellRendererPane

to handle
the actual painting, and is only recommended if you use one
component for rendering. If you make use of multiple components
to handle the rendering, as

JTable

does, use

CellRendererPane

directly. Otherwise, as described
below, you could end up with a

CellRendererPane

per

Component

.

If

c

's parent is not a

CellRendererPane

,
a new

CellRendererPane

is created,

c

is
added to it, and the

CellRendererPane

is added to

p

. If

c

's parent is a

CellRendererPane

and the

CellRendererPane

s
parent is not

p

, it is added to

p

.

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

**Parameters:** g

- the

Graphics

object to draw on
**Parameters:** c

- the

Component

to draw
**Parameters:** p

- the intermediate

Container
**Parameters:** x

- an int specifying the left side of the area draw in, in pixels,
measured from the left edge of the graphics context
**Parameters:** y

- an int specifying the top of the area to draw in, in pixels
measured down from the top edge of the graphics context
**Parameters:** w

- an int specifying the width of the area draw in, in pixels
**Parameters:** h

- an int specifying the height of the area draw in, in pixels
**See Also:** CellRendererPane

,

Component.isLightweight()

- paintComponent

```java
public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,

Rectangle
r)
```

Paints a component to the specified

Graphics

. This
is a cover method for

paintComponent(Graphics,Component,Container,int,int,int,int)

.
Refer to it for more information.

**Parameters:** g

- the

Graphics

object to draw on
**Parameters:** c

- the

Component

to draw
**Parameters:** p

- the intermediate

Container
**Parameters:** r

- the

Rectangle

to draw in
**See Also:** paintComponent(Graphics,Component,Container,int,int,int,int)

,

CellRendererPane

- updateComponentTreeUI

```java
public static void updateComponentTreeUI​(
Component
c)
```

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

**Parameters:** c

- the component

- invokeLater

```java
public static void invokeLater​(
Runnable
doRun)
```

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread. This will happen after all
pending AWT events have been processed. This method should
be used when an application thread needs to update the GUI.
In the following example the

invokeLater

call queues
the

Runnable

object

doHelloWorld

on the event dispatching thread and
then prints a message.

```java
Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

SwingUtilities.invokeLater(doHelloWorld);
System.out.println("This might well be displayed before the other message.");
```

If invokeLater is called from the event dispatching thread --
for example, from a JButton's ActionListener -- the

doRun.run()

will
still be deferred until all pending events have been processed.
Note that if the

doRun.run()

throws an uncaught exception
the event dispatching thread will unwind (not the current thread).

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeLater()

.

Unlike the rest of Swing, this method can be invoked from any thread.

**Parameters:** doRun

- the instance of

Runnable
**See Also:** invokeAndWait(java.lang.Runnable)

- invokeAndWait

```java
public static void invokeAndWait​(
Runnable
doRun)
throws
InterruptedException
,

InvocationTargetException
```

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread. This call blocks until
all pending AWT events have been processed and (then)

doRun.run()

returns. This method should
be used when an application thread needs to update the GUI.
It shouldn't be called from the event dispatching thread.
Here's an example that creates a new application thread
that uses

invokeAndWait

to print a string from the event
dispatching thread and then, when that's finished, print
a string from the application thread.

```java
final Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

Thread appThread = new Thread() {
public void run() {
try {
SwingUtilities.invokeAndWait(doHelloWorld);
}
catch (Exception e) {
e.printStackTrace();
}
System.out.println("Finished on " + Thread.currentThread());
}
};
appThread.start();
```

Note that if the

Runnable.run

method throws an
uncaught exception
(on the event dispatching thread) it's caught and rethrown, as
an

InvocationTargetException

, on the caller's thread.

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeAndWait()

.

**Parameters:** doRun

- the instance of

Runnable
**Throws:** InterruptedException

- if we're interrupted while waiting for
the event dispatching thread to finish executing

doRun.run()
**Throws:** InvocationTargetException

- if an exception is thrown
while running

doRun
**See Also:** invokeLater(java.lang.Runnable)

- isEventDispatchThread

```java
public static boolean isEventDispatchThread()
```

Returns true if the current thread is an AWT event dispatching thread.

As of 1.3 this method is just a cover for

java.awt.EventQueue.isDispatchThread()

.

**Returns:** true if the current thread is an AWT event dispatching thread

- getAccessibleIndexInParent

```java
public static int getAccessibleIndexInParent​(
Component
c)
```

Get the index of this object in its accessible parent.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** -1 of this object does not have an accessible parent.
Otherwise, the index of the child in its accessible parent.

- getAccessibleAt

```java
public static
Accessible
getAccessibleAt​(
Component
c,

Point
p)
```

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.
Otherwise returns

null

.

**Parameters:** c

- the component
**Parameters:** p

- the local coordinate
**Returns:** the

Accessible

at the specified location,
if it exists; otherwise

null

- getAccessibleStateSet

```java
public static
AccessibleStateSet
getAccessibleStateSet​(
Component
c)
```

Get the state of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** an instance of AccessibleStateSet containing the current state
set of the object
**See Also:** AccessibleState

- getAccessibleChildrenCount

```java
public static int getAccessibleChildrenCount​(
Component
c)
```

Returns the number of accessible children in the object. If all
of the children of this object implement Accessible, than this
method should return the number of children of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** the number of accessible children in the object.

- getAccessibleChild

```java
public static
Accessible
getAccessibleChild​(
Component
c,
int i)
```

Return the nth Accessible child of the object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Parameters:** i

- zero-based index of child
**Returns:** the nth Accessible child of the object

- findFocusOwner

```java
@Deprecated

public static
Component
findFocusOwner​(
Component
c)
```

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getFocusOwner()

.

Return the child

Component

of the specified

Component

that is the focus owner, if any.

**Parameters:** c

- the root of the

Component

hierarchy to
search for the focus owner
**Returns:** the focus owner, or

null

if there is no focus
owner, or if the focus owner is not

comp

, or a
descendant of

comp
**See Also:** KeyboardFocusManager.getFocusOwner()

- getRootPane

```java
public static
JRootPane
getRootPane​(
Component
c)
```

If c is a JRootPane descendant return its JRootPane ancestor.
If c is a RootPaneContainer then return its JRootPane.

**Parameters:** c

- the component
**Returns:** the JRootPane for Component c or

null

.

- getRoot

```java
public static
Component
getRoot​(
Component
c)
```

Returns the root component for the current component tree.

**Parameters:** c

- the component
**Returns:** the first ancestor of c that's a Window or the last Applet ancestor

- processKeyBindings

```java
public static boolean processKeyBindings​(
KeyEvent
event)
```

Process the key bindings for the

Component

associated with

event

. This method is only useful if

event.getComponent()

does not descend from

JComponent

, or your are not invoking

super.processKeyEvent

from within your

JComponent

subclass.

JComponent

automatically processes bindings from within its

processKeyEvent

method, hence you rarely need
to directly invoke this method.

**Parameters:** event

- KeyEvent used to identify which bindings to process, as
well as which Component has focus.
**Returns:** true if a binding has found and processed
**Since:** 1.4

- notifyAction

```java
public static boolean notifyAction​(
Action
action,

KeyStroke
ks,

KeyEvent
event,

Object
sender,
int modifiers)
```

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.
The command for the ActionEvent is determined by:

- If the action was registered via

registerKeyboardAction

, then the command string
passed in (

null

will be used if

null

was passed in).

Action value with name Action.ACTION_COMMAND_KEY, unless

null

.

String value of the KeyEvent, unless

getKeyChar

returns KeyEvent.CHAR_UNDEFINED..

This will return true if

action

is non-

null

and
actionPerformed is invoked on it.

**Parameters:** action

- an action
**Parameters:** ks

- a key stroke
**Parameters:** event

- a key event
**Parameters:** sender

- a sender
**Parameters:** modifiers

- action modifiers
**Returns:** true

if

action

is non-

null

and
actionPerformed is invoked on it.
**Since:** 1.3
**See Also:** Action.accept(java.lang.Object)

- replaceUIInputMap

```java
public static void replaceUIInputMap​(
JComponent
component,
int type,

InputMap
uiInputMap)
```

Convenience method to change the UI InputMap for

component

to

uiInputMap

. If

uiInputMap

is

null

,
this removes any previously installed UI InputMap.

**Parameters:** component

- a component
**Parameters:** type

- a type
**Parameters:** uiInputMap

- an

InputMap
**Since:** 1.3

- replaceUIActionMap

```java
public static void replaceUIActionMap​(
JComponent
component,

ActionMap
uiActionMap)
```

Convenience method to change the UI ActionMap for

component

to

uiActionMap

. If

uiActionMap

is

null

,
this removes any previously installed UI ActionMap.

**Parameters:** component

- a component
**Parameters:** uiActionMap

- an

ActionMap
**Since:** 1.3

- getUIInputMap

```java
public static
InputMap
getUIInputMap​(
JComponent
component,
int condition)
```

Returns the InputMap provided by the UI for condition

condition

in component

component

.

This will return

null

if the UI has not installed an InputMap
of the specified type.

**Parameters:** component

- a component
**Parameters:** condition

- a condition
**Returns:** the

ActionMap

provided by the UI for

condition

in the component, or

null

if the UI has not installed
an InputMap of the specified type.
**Since:** 1.3

- getUIActionMap

```java
public static
ActionMap
getUIActionMap​(
JComponent
component)
```

Returns the ActionMap provided by the UI
in component

component

.

This will return

null

if the UI has not installed an ActionMap.

**Parameters:** component

- a component
**Returns:** the

ActionMap

provided by the UI in the component,
or

null

if the UI has not installed an ActionMap.
**Since:** 1.3

- calculateInnerArea

```java
public static
Rectangle
calculateInnerArea​(
JComponent
c,

Rectangle
r)
```

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.
The position and size specify the bounds of the component,
adjusted so as not to include the border area (the insets).
This method is useful for classes
that implement painting code.

**Parameters:** c

- the JComponent in question; if

null

, this method returns

null
**Parameters:** r

- the Rectangle instance to be modified;
may be

null
**Returns:** null

if the Component is

null

;
otherwise, returns the passed-in rectangle (if non-

null

)
or a new rectangle specifying position and size information
**Since:** 1.4

- getUnwrappedParent

```java
public static
Container
getUnwrappedParent​(
Component
component)
```

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

**Parameters:** component

-

Component

to get
the first ancestor of, which is not a

JLayer

instance.
**Returns:** the first ancestor of the

component

which is not an instance of

JLayer

.
If such an ancestor can not be found,

null

is returned.
**Throws:** NullPointerException

- if

component

is

null
**Since:** 1.7
**See Also:** JLayer

- getUnwrappedView

```java
public static
Component
getUnwrappedView​(
JViewport
viewport)
```

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.

If the

viewport

's view component is not a

JLayer

,
this method is equivalent to

JViewport.getView()

otherwise

JLayer.getView()

will be recursively
called on all descending

JLayer

s.

**Parameters:** viewport

-

JViewport

to get the first descendant of,
which in not a

JLayer

instance.
**Returns:** the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.
**Throws:** NullPointerException

- if

viewport

is

null
**Since:** 1.7
**See Also:** JViewport.getView()

,

JLayer

Method Detail

- isRectangleContainingRectangle

```java
public static final boolean isRectangleContainingRectangle​(
Rectangle
a,

Rectangle
b)
```

Return

true

if @{code a} contains

b

**Parameters:** a

- the first rectangle
**Parameters:** b

- the second rectangle
**Returns:** true

if @{code a} contains

b

- getLocalBounds

```java
public static
Rectangle
getLocalBounds​(
Component
aComponent)
```

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

**Parameters:** aComponent

- a component
**Returns:** the local bounds for the component

aComponent

- getWindowAncestor

```java
public static
Window
getWindowAncestor​(
Component
c)
```

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

**Parameters:** c

-

Component

to get

Window

ancestor
of.
**Returns:** the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.
**Since:** 1.3

- convertPoint

```java
public static
Point
convertPoint​(
Component
source,

Point
aPoint,

Component
destination)
```

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aPoint

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aPoint

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aPoint

without any conversion.

**Parameters:** source

- the source component
**Parameters:** aPoint

- the point
**Parameters:** destination

- the destination component
**Returns:** the converted coordinate

- convertPoint

```java
public static
Point
convertPoint​(
Component
source,
int x,
int y,

Component
destination)
```

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

(x,y)

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

(x,y)

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

(x,y)

without any conversion.

**Parameters:** source

- the source component
**Parameters:** x

- the x-coordinate of the point
**Parameters:** y

- the y-coordinate of the point
**Parameters:** destination

- the destination component
**Returns:** the converted coordinate

- convertRectangle

```java
public static
Rectangle
convertRectangle​(
Component
source,

Rectangle
aRectangle,

Component
destination)
```

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aRectangle

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aRectangle

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aRectangle

without any conversion.

**Parameters:** source

- the source component
**Parameters:** aRectangle

- a rectangle
**Parameters:** destination

- the destination component
**Returns:** the converted rectangle

- getAncestorOfClass

```java
public static
Container
getAncestorOfClass​(
Class
<?> c,

Component
comp)
```

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds. Can return

null

, if a class

c

cannot be found.

**Parameters:** c

- the class of a component
**Parameters:** comp

- the component
**Returns:** the ancestor of the

comp

,
or

null

if

c

cannot be found.

- getAncestorNamed

```java
public static
Container
getAncestorNamed​(
String
name,

Component
comp)
```

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds. Can return

null

, if

name

cannot be found.

**Parameters:** name

- the name of a component
**Parameters:** comp

- the component
**Returns:** the ancestor of the

comp

,
or

null

if

name

cannot be found.

- getDeepestComponentAt

```java
public static
Component
getDeepestComponentAt​(
Component
parent,
int x,
int y)
```

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.
If

parent

does not contain the specified location,
then

null

is returned. If

parent

is not a
container, or none of

parent

's visible descendents
contain the specified location,

parent

is returned.

**Parameters:** parent

- the root component to begin the search
**Parameters:** x

- the x target location
**Parameters:** y

- the y target location
**Returns:** the deepest component

- convertMouseEvent

```java
public static
MouseEvent
convertMouseEvent​(
Component
source,

MouseEvent
sourceEvent,

Component
destination)
```

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system. If

source

is

null

,

sourceEvent

x and y members
are assumed to be into

destination

's root component coordinate system.
If

destination

is

null

, the
returned MouseEvent will be in

source

's coordinate system.

sourceEvent

will not be changed. A new event is returned.
the

source

field of the returned event will be set
to

destination

if destination is non-

null

use the translateMouseEvent() method to translate a mouse event from
one component to another without changing the source.

**Parameters:** source

- the source component
**Parameters:** sourceEvent

- the source mouse event
**Parameters:** destination

- the destination component
**Returns:** the new mouse event

- convertPointToScreen

```java
public static void convertPointToScreen​(
Point
p,

Component
c)
```

Convert a point from a component's coordinate system to
screen coordinates.

**Parameters:** p

- a Point object (converted to the new coordinate system)
**Parameters:** c

- a Component object

- convertPointFromScreen

```java
public static void convertPointFromScreen​(
Point
p,

Component
c)
```

Convert a point from a screen coordinates to a component's
coordinate system

**Parameters:** p

- a Point object (converted to the new coordinate system)
**Parameters:** c

- a Component object

- windowForComponent

```java
public static
Window
windowForComponent​(
Component
c)
```

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

Note: This method provides the same functionality as

getWindowAncestor

.

**Parameters:** c

-

Component

to get

Window

ancestor
of.
**Returns:** the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

- isDescendingFrom

```java
public static boolean isDescendingFrom​(
Component
a,

Component
b)
```

Return

true

if a component

a

descends from a component

b

**Parameters:** a

- the first component
**Parameters:** b

- the second component
**Returns:** true

if a component

a

descends from a component

b

- computeIntersection

```java
public static
Rectangle
computeIntersection​(int x,
int y,
int width,
int height,

Rectangle
dest)
```

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.
If the two rectangles don't intersect,
then the returned rectangle begins at (0,0)
and has zero width and height.

**Parameters:** x

- the X coordinate of the first rectangle's top-left point
**Parameters:** y

- the Y coordinate of the first rectangle's top-left point
**Parameters:** width

- the width of the first rectangle
**Parameters:** height

- the height of the first rectangle
**Parameters:** dest

- the second rectangle
**Returns:** dest

, modified to specify the intersection

- computeUnion

```java
public static
Rectangle
computeUnion​(int x,
int y,
int width,
int height,

Rectangle
dest)
```

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

**Parameters:** x

- the x-coordinate of the first rectangle
**Parameters:** y

- the y-coordinate of the first rectangle
**Parameters:** width

- the width of the first rectangle
**Parameters:** height

- the height of the first rectangle
**Parameters:** dest

- the coordinates of the second rectangle; the union
of the two rectangles is returned in this rectangle
**Returns:** the

dest

Rectangle

- computeDifference

```java
public static
Rectangle
[] computeDifference​(
Rectangle
rectA,

Rectangle
rectB)
```

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

. If the
two Rects do not overlap, returns an empty array

**Parameters:** rectA

- the first rectangle
**Parameters:** rectB

- the second rectangle
**Returns:** an array of rectangles representing the regions within

rectA

that do not overlap with

rectB

.

- isLeftMouseButton

```java
public static boolean isLeftMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the left mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the left mouse button was active

- isMiddleMouseButton

```java
public static boolean isMiddleMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the middle mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the middle mouse button was active

- isRightMouseButton

```java
public static boolean isRightMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the right mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the right mouse button was active

- computeStringWidth

```java
public static int computeStringWidth​(
FontMetrics
fm,

String
str)
```

Compute the width of the string using a font with the specified
"metrics" (sizes).

**Parameters:** fm

- a FontMetrics object to compute with
**Parameters:** str

- the String to compute
**Returns:** an int containing the string width

- layoutCompoundLabel

```java
public static
String
layoutCompoundLabel​(
JComponent
c,

FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)
```

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
The JComponents orientation (LEADING/TRAILING) will also be taken
into account and translated into LEFT/RIGHT values accordingly.

**Parameters:** c

- the component
**Parameters:** fm

- the instance of

FontMetrics
**Parameters:** text

- the text
**Parameters:** icon

- the icon
**Parameters:** verticalAlignment

- the vertical alignment
**Parameters:** horizontalAlignment

- the horizontal alignment
**Parameters:** verticalTextPosition

- the vertical text position
**Parameters:** horizontalTextPosition

- the horizontal text position
**Parameters:** viewR

- the available rectangle
**Parameters:** iconR

- the rectangle for the icon
**Parameters:** textR

- the rectangle for the text
**Parameters:** textIconGap

- the gap between text and icon
**Returns:** the possibly clipped version of the compound labels string

- layoutCompoundLabel

```java
public static
String
layoutCompoundLabel​(
FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)
```

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
This layoutCompoundLabel() does not know how to handle LEADING/TRAILING
values in horizontalTextPosition (they will default to RIGHT) and in
horizontalAlignment (they will default to CENTER).
Use the other version of layoutCompoundLabel() instead.

**Parameters:** fm

- the instance of

FontMetrics
**Parameters:** text

- the text
**Parameters:** icon

- the icon
**Parameters:** verticalAlignment

- the vertical alignment
**Parameters:** horizontalAlignment

- the horizontal alignment
**Parameters:** verticalTextPosition

- the vertical text position
**Parameters:** horizontalTextPosition

- the horizontal text position
**Parameters:** viewR

- the available rectangle
**Parameters:** iconR

- the rectangle for the icon
**Parameters:** textR

- the rectangle for the text
**Parameters:** textIconGap

- the gap between text and icon
**Returns:** the possibly clipped version of the compound labels string

- paintComponent

```java
public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,
int x,
int y,
int w,
int h)
```

Paints a component to the specified

Graphics

.
This method is primarily useful to render

Component

s that don't exist as part of the visible
containment hierarchy, but are used for rendering. For
example, if you are doing your own rendering and want to render
some text (or even HTML), you could make use of

JLabel

's text rendering support and have it paint
directly by way of this method, without adding the label to the
visible containment hierarchy.

This method makes use of

CellRendererPane

to handle
the actual painting, and is only recommended if you use one
component for rendering. If you make use of multiple components
to handle the rendering, as

JTable

does, use

CellRendererPane

directly. Otherwise, as described
below, you could end up with a

CellRendererPane

per

Component

.

If

c

's parent is not a

CellRendererPane

,
a new

CellRendererPane

is created,

c

is
added to it, and the

CellRendererPane

is added to

p

. If

c

's parent is a

CellRendererPane

and the

CellRendererPane

s
parent is not

p

, it is added to

p

.

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

**Parameters:** g

- the

Graphics

object to draw on
**Parameters:** c

- the

Component

to draw
**Parameters:** p

- the intermediate

Container
**Parameters:** x

- an int specifying the left side of the area draw in, in pixels,
measured from the left edge of the graphics context
**Parameters:** y

- an int specifying the top of the area to draw in, in pixels
measured down from the top edge of the graphics context
**Parameters:** w

- an int specifying the width of the area draw in, in pixels
**Parameters:** h

- an int specifying the height of the area draw in, in pixels
**See Also:** CellRendererPane

,

Component.isLightweight()

- paintComponent

```java
public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,

Rectangle
r)
```

Paints a component to the specified

Graphics

. This
is a cover method for

paintComponent(Graphics,Component,Container,int,int,int,int)

.
Refer to it for more information.

**Parameters:** g

- the

Graphics

object to draw on
**Parameters:** c

- the

Component

to draw
**Parameters:** p

- the intermediate

Container
**Parameters:** r

- the

Rectangle

to draw in
**See Also:** paintComponent(Graphics,Component,Container,int,int,int,int)

,

CellRendererPane

- updateComponentTreeUI

```java
public static void updateComponentTreeUI​(
Component
c)
```

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

**Parameters:** c

- the component

- invokeLater

```java
public static void invokeLater​(
Runnable
doRun)
```

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread. This will happen after all
pending AWT events have been processed. This method should
be used when an application thread needs to update the GUI.
In the following example the

invokeLater

call queues
the

Runnable

object

doHelloWorld

on the event dispatching thread and
then prints a message.

```java
Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

SwingUtilities.invokeLater(doHelloWorld);
System.out.println("This might well be displayed before the other message.");
```

If invokeLater is called from the event dispatching thread --
for example, from a JButton's ActionListener -- the

doRun.run()

will
still be deferred until all pending events have been processed.
Note that if the

doRun.run()

throws an uncaught exception
the event dispatching thread will unwind (not the current thread).

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeLater()

.

Unlike the rest of Swing, this method can be invoked from any thread.

**Parameters:** doRun

- the instance of

Runnable
**See Also:** invokeAndWait(java.lang.Runnable)

- invokeAndWait

```java
public static void invokeAndWait​(
Runnable
doRun)
throws
InterruptedException
,

InvocationTargetException
```

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread. This call blocks until
all pending AWT events have been processed and (then)

doRun.run()

returns. This method should
be used when an application thread needs to update the GUI.
It shouldn't be called from the event dispatching thread.
Here's an example that creates a new application thread
that uses

invokeAndWait

to print a string from the event
dispatching thread and then, when that's finished, print
a string from the application thread.

```java
final Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

Thread appThread = new Thread() {
public void run() {
try {
SwingUtilities.invokeAndWait(doHelloWorld);
}
catch (Exception e) {
e.printStackTrace();
}
System.out.println("Finished on " + Thread.currentThread());
}
};
appThread.start();
```

Note that if the

Runnable.run

method throws an
uncaught exception
(on the event dispatching thread) it's caught and rethrown, as
an

InvocationTargetException

, on the caller's thread.

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeAndWait()

.

**Parameters:** doRun

- the instance of

Runnable
**Throws:** InterruptedException

- if we're interrupted while waiting for
the event dispatching thread to finish executing

doRun.run()
**Throws:** InvocationTargetException

- if an exception is thrown
while running

doRun
**See Also:** invokeLater(java.lang.Runnable)

- isEventDispatchThread

```java
public static boolean isEventDispatchThread()
```

Returns true if the current thread is an AWT event dispatching thread.

As of 1.3 this method is just a cover for

java.awt.EventQueue.isDispatchThread()

.

**Returns:** true if the current thread is an AWT event dispatching thread

- getAccessibleIndexInParent

```java
public static int getAccessibleIndexInParent​(
Component
c)
```

Get the index of this object in its accessible parent.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** -1 of this object does not have an accessible parent.
Otherwise, the index of the child in its accessible parent.

- getAccessibleAt

```java
public static
Accessible
getAccessibleAt​(
Component
c,

Point
p)
```

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.
Otherwise returns

null

.

**Parameters:** c

- the component
**Parameters:** p

- the local coordinate
**Returns:** the

Accessible

at the specified location,
if it exists; otherwise

null

- getAccessibleStateSet

```java
public static
AccessibleStateSet
getAccessibleStateSet​(
Component
c)
```

Get the state of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** an instance of AccessibleStateSet containing the current state
set of the object
**See Also:** AccessibleState

- getAccessibleChildrenCount

```java
public static int getAccessibleChildrenCount​(
Component
c)
```

Returns the number of accessible children in the object. If all
of the children of this object implement Accessible, than this
method should return the number of children of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** the number of accessible children in the object.

- getAccessibleChild

```java
public static
Accessible
getAccessibleChild​(
Component
c,
int i)
```

Return the nth Accessible child of the object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Parameters:** i

- zero-based index of child
**Returns:** the nth Accessible child of the object

- findFocusOwner

```java
@Deprecated

public static
Component
findFocusOwner​(
Component
c)
```

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getFocusOwner()

.

Return the child

Component

of the specified

Component

that is the focus owner, if any.

**Parameters:** c

- the root of the

Component

hierarchy to
search for the focus owner
**Returns:** the focus owner, or

null

if there is no focus
owner, or if the focus owner is not

comp

, or a
descendant of

comp
**See Also:** KeyboardFocusManager.getFocusOwner()

- getRootPane

```java
public static
JRootPane
getRootPane​(
Component
c)
```

If c is a JRootPane descendant return its JRootPane ancestor.
If c is a RootPaneContainer then return its JRootPane.

**Parameters:** c

- the component
**Returns:** the JRootPane for Component c or

null

.

- getRoot

```java
public static
Component
getRoot​(
Component
c)
```

Returns the root component for the current component tree.

**Parameters:** c

- the component
**Returns:** the first ancestor of c that's a Window or the last Applet ancestor

- processKeyBindings

```java
public static boolean processKeyBindings​(
KeyEvent
event)
```

Process the key bindings for the

Component

associated with

event

. This method is only useful if

event.getComponent()

does not descend from

JComponent

, or your are not invoking

super.processKeyEvent

from within your

JComponent

subclass.

JComponent

automatically processes bindings from within its

processKeyEvent

method, hence you rarely need
to directly invoke this method.

**Parameters:** event

- KeyEvent used to identify which bindings to process, as
well as which Component has focus.
**Returns:** true if a binding has found and processed
**Since:** 1.4

- notifyAction

```java
public static boolean notifyAction​(
Action
action,

KeyStroke
ks,

KeyEvent
event,

Object
sender,
int modifiers)
```

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.
The command for the ActionEvent is determined by:

- If the action was registered via

registerKeyboardAction

, then the command string
passed in (

null

will be used if

null

was passed in).

Action value with name Action.ACTION_COMMAND_KEY, unless

null

.

String value of the KeyEvent, unless

getKeyChar

returns KeyEvent.CHAR_UNDEFINED..

This will return true if

action

is non-

null

and
actionPerformed is invoked on it.

**Parameters:** action

- an action
**Parameters:** ks

- a key stroke
**Parameters:** event

- a key event
**Parameters:** sender

- a sender
**Parameters:** modifiers

- action modifiers
**Returns:** true

if

action

is non-

null

and
actionPerformed is invoked on it.
**Since:** 1.3
**See Also:** Action.accept(java.lang.Object)

- replaceUIInputMap

```java
public static void replaceUIInputMap​(
JComponent
component,
int type,

InputMap
uiInputMap)
```

Convenience method to change the UI InputMap for

component

to

uiInputMap

. If

uiInputMap

is

null

,
this removes any previously installed UI InputMap.

**Parameters:** component

- a component
**Parameters:** type

- a type
**Parameters:** uiInputMap

- an

InputMap
**Since:** 1.3

- replaceUIActionMap

```java
public static void replaceUIActionMap​(
JComponent
component,

ActionMap
uiActionMap)
```

Convenience method to change the UI ActionMap for

component

to

uiActionMap

. If

uiActionMap

is

null

,
this removes any previously installed UI ActionMap.

**Parameters:** component

- a component
**Parameters:** uiActionMap

- an

ActionMap
**Since:** 1.3

- getUIInputMap

```java
public static
InputMap
getUIInputMap​(
JComponent
component,
int condition)
```

Returns the InputMap provided by the UI for condition

condition

in component

component

.

This will return

null

if the UI has not installed an InputMap
of the specified type.

**Parameters:** component

- a component
**Parameters:** condition

- a condition
**Returns:** the

ActionMap

provided by the UI for

condition

in the component, or

null

if the UI has not installed
an InputMap of the specified type.
**Since:** 1.3

- getUIActionMap

```java
public static
ActionMap
getUIActionMap​(
JComponent
component)
```

Returns the ActionMap provided by the UI
in component

component

.

This will return

null

if the UI has not installed an ActionMap.

**Parameters:** component

- a component
**Returns:** the

ActionMap

provided by the UI in the component,
or

null

if the UI has not installed an ActionMap.
**Since:** 1.3

- calculateInnerArea

```java
public static
Rectangle
calculateInnerArea​(
JComponent
c,

Rectangle
r)
```

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.
The position and size specify the bounds of the component,
adjusted so as not to include the border area (the insets).
This method is useful for classes
that implement painting code.

**Parameters:** c

- the JComponent in question; if

null

, this method returns

null
**Parameters:** r

- the Rectangle instance to be modified;
may be

null
**Returns:** null

if the Component is

null

;
otherwise, returns the passed-in rectangle (if non-

null

)
or a new rectangle specifying position and size information
**Since:** 1.4

- getUnwrappedParent

```java
public static
Container
getUnwrappedParent​(
Component
component)
```

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

**Parameters:** component

-

Component

to get
the first ancestor of, which is not a

JLayer

instance.
**Returns:** the first ancestor of the

component

which is not an instance of

JLayer

.
If such an ancestor can not be found,

null

is returned.
**Throws:** NullPointerException

- if

component

is

null
**Since:** 1.7
**See Also:** JLayer

- getUnwrappedView

```java
public static
Component
getUnwrappedView​(
JViewport
viewport)
```

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.

If the

viewport

's view component is not a

JLayer

,
this method is equivalent to

JViewport.getView()

otherwise

JLayer.getView()

will be recursively
called on all descending

JLayer

s.

**Parameters:** viewport

-

JViewport

to get the first descendant of,
which in not a

JLayer

instance.
**Returns:** the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.
**Throws:** NullPointerException

- if

viewport

is

null
**Since:** 1.7
**See Also:** JViewport.getView()

,

JLayer

---

#### Method Detail

isRectangleContainingRectangle

```java
public static final boolean isRectangleContainingRectangle​(
Rectangle
a,

Rectangle
b)
```

Return

true

if @{code a} contains

b

**Parameters:** a

- the first rectangle
**Parameters:** b

- the second rectangle
**Returns:** true

if @{code a} contains

b

---

#### isRectangleContainingRectangle

public static final boolean isRectangleContainingRectangle​(

Rectangle

a,

Rectangle

b)

Return

true

if @{code a} contains

b

getLocalBounds

```java
public static
Rectangle
getLocalBounds​(
Component
aComponent)
```

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

**Parameters:** aComponent

- a component
**Returns:** the local bounds for the component

aComponent

---

#### getLocalBounds

public static

Rectangle

getLocalBounds​(

Component

aComponent)

Return the rectangle (0,0,bounds.width,bounds.height) for the component

aComponent

getWindowAncestor

```java
public static
Window
getWindowAncestor​(
Component
c)
```

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

**Parameters:** c

-

Component

to get

Window

ancestor
of.
**Returns:** the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.
**Since:** 1.3

---

#### getWindowAncestor

public static

Window

getWindowAncestor​(

Component

c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

convertPoint

```java
public static
Point
convertPoint​(
Component
source,

Point
aPoint,

Component
destination)
```

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aPoint

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aPoint

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aPoint

without any conversion.

**Parameters:** source

- the source component
**Parameters:** aPoint

- the point
**Parameters:** destination

- the destination component
**Returns:** the converted coordinate

---

#### convertPoint

public static

Point

convertPoint​(

Component

source,

Point

aPoint,

Component

destination)

Convert a

aPoint

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aPoint

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aPoint

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aPoint

without any conversion.

convertPoint

```java
public static
Point
convertPoint​(
Component
source,
int x,
int y,

Component
destination)
```

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

(x,y)

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

(x,y)

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

(x,y)

without any conversion.

**Parameters:** source

- the source component
**Parameters:** x

- the x-coordinate of the point
**Parameters:** y

- the y-coordinate of the point
**Parameters:** destination

- the destination component
**Returns:** the converted coordinate

---

#### convertPoint

public static

Point

convertPoint​(

Component

source,
int x,
int y,

Component

destination)

Convert the point

(x,y)

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

(x,y)

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

(x,y)

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

(x,y)

without any conversion.

convertRectangle

```java
public static
Rectangle
convertRectangle​(
Component
source,

Rectangle
aRectangle,

Component
destination)
```

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aRectangle

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aRectangle

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aRectangle

without any conversion.

**Parameters:** source

- the source component
**Parameters:** aRectangle

- a rectangle
**Parameters:** destination

- the destination component
**Returns:** the converted rectangle

---

#### convertRectangle

public static

Rectangle

convertRectangle​(

Component

source,

Rectangle

aRectangle,

Component

destination)

Convert the rectangle

aRectangle

in

source

coordinate system to

destination

coordinate system.
If

source

is

null

,

aRectangle

is assumed to be in

destination

's
root component coordinate system.
If

destination

is

null

,

aRectangle

will be converted to

source

's
root component coordinate system.
If both

source

and

destination

are

null

, return

aRectangle

without any conversion.

getAncestorOfClass

```java
public static
Container
getAncestorOfClass​(
Class
<?> c,

Component
comp)
```

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds. Can return

null

, if a class

c

cannot be found.

**Parameters:** c

- the class of a component
**Parameters:** comp

- the component
**Returns:** the ancestor of the

comp

,
or

null

if

c

cannot be found.

---

#### getAncestorOfClass

public static

Container

getAncestorOfClass​(

Class

<?> c,

Component

comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of class

c

it
finds. Can return

null

, if a class

c

cannot be found.

getAncestorNamed

```java
public static
Container
getAncestorNamed​(
String
name,

Component
comp)
```

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds. Can return

null

, if

name

cannot be found.

**Parameters:** name

- the name of a component
**Parameters:** comp

- the component
**Returns:** the ancestor of the

comp

,
or

null

if

name

cannot be found.

---

#### getAncestorNamed

public static

Container

getAncestorNamed​(

String

name,

Component

comp)

Convenience method for searching above

comp

in the
component hierarchy and returns the first object of

name

it
finds. Can return

null

, if

name

cannot be found.

getDeepestComponentAt

```java
public static
Component
getDeepestComponentAt​(
Component
parent,
int x,
int y)
```

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.
If

parent

does not contain the specified location,
then

null

is returned. If

parent

is not a
container, or none of

parent

's visible descendents
contain the specified location,

parent

is returned.

**Parameters:** parent

- the root component to begin the search
**Parameters:** x

- the x target location
**Parameters:** y

- the y target location
**Returns:** the deepest component

---

#### getDeepestComponentAt

public static

Component

getDeepestComponentAt​(

Component

parent,
int x,
int y)

Returns the deepest visible descendent Component of

parent

that contains the location

x

,

y

.
If

parent

does not contain the specified location,
then

null

is returned. If

parent

is not a
container, or none of

parent

's visible descendents
contain the specified location,

parent

is returned.

convertMouseEvent

```java
public static
MouseEvent
convertMouseEvent​(
Component
source,

MouseEvent
sourceEvent,

Component
destination)
```

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system. If

source

is

null

,

sourceEvent

x and y members
are assumed to be into

destination

's root component coordinate system.
If

destination

is

null

, the
returned MouseEvent will be in

source

's coordinate system.

sourceEvent

will not be changed. A new event is returned.
the

source

field of the returned event will be set
to

destination

if destination is non-

null

use the translateMouseEvent() method to translate a mouse event from
one component to another without changing the source.

**Parameters:** source

- the source component
**Parameters:** sourceEvent

- the source mouse event
**Parameters:** destination

- the destination component
**Returns:** the new mouse event

---

#### convertMouseEvent

public static

MouseEvent

convertMouseEvent​(

Component

source,

MouseEvent

sourceEvent,

Component

destination)

Returns a MouseEvent similar to

sourceEvent

except that its x
and y members have been converted to

destination

's coordinate
system. If

source

is

null

,

sourceEvent

x and y members
are assumed to be into

destination

's root component coordinate system.
If

destination

is

null

, the
returned MouseEvent will be in

source

's coordinate system.

sourceEvent

will not be changed. A new event is returned.
the

source

field of the returned event will be set
to

destination

if destination is non-

null

use the translateMouseEvent() method to translate a mouse event from
one component to another without changing the source.

convertPointToScreen

```java
public static void convertPointToScreen​(
Point
p,

Component
c)
```

Convert a point from a component's coordinate system to
screen coordinates.

**Parameters:** p

- a Point object (converted to the new coordinate system)
**Parameters:** c

- a Component object

---

#### convertPointToScreen

public static void convertPointToScreen​(

Point

p,

Component

c)

Convert a point from a component's coordinate system to
screen coordinates.

convertPointFromScreen

```java
public static void convertPointFromScreen​(
Point
p,

Component
c)
```

Convert a point from a screen coordinates to a component's
coordinate system

**Parameters:** p

- a Point object (converted to the new coordinate system)
**Parameters:** c

- a Component object

---

#### convertPointFromScreen

public static void convertPointFromScreen​(

Point

p,

Component

c)

Convert a point from a screen coordinates to a component's
coordinate system

windowForComponent

```java
public static
Window
windowForComponent​(
Component
c)
```

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

Note: This method provides the same functionality as

getWindowAncestor

.

**Parameters:** c

-

Component

to get

Window

ancestor
of.
**Returns:** the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

---

#### windowForComponent

public static

Window

windowForComponent​(

Component

c)

Returns the first

Window

ancestor of

c

, or

null

if

c

is not contained inside a

Window

.

Note: This method provides the same functionality as

getWindowAncestor

.

Note: This method provides the same functionality as

getWindowAncestor

.

isDescendingFrom

```java
public static boolean isDescendingFrom​(
Component
a,

Component
b)
```

Return

true

if a component

a

descends from a component

b

**Parameters:** a

- the first component
**Parameters:** b

- the second component
**Returns:** true

if a component

a

descends from a component

b

---

#### isDescendingFrom

public static boolean isDescendingFrom​(

Component

a,

Component

b)

Return

true

if a component

a

descends from a component

b

computeIntersection

```java
public static
Rectangle
computeIntersection​(int x,
int y,
int width,
int height,

Rectangle
dest)
```

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.
If the two rectangles don't intersect,
then the returned rectangle begins at (0,0)
and has zero width and height.

**Parameters:** x

- the X coordinate of the first rectangle's top-left point
**Parameters:** y

- the Y coordinate of the first rectangle's top-left point
**Parameters:** width

- the width of the first rectangle
**Parameters:** height

- the height of the first rectangle
**Parameters:** dest

- the second rectangle
**Returns:** dest

, modified to specify the intersection

---

#### computeIntersection

public static

Rectangle

computeIntersection​(int x,
int y,
int width,
int height,

Rectangle

dest)

Convenience to calculate the intersection of two rectangles
without allocating a new rectangle.
If the two rectangles don't intersect,
then the returned rectangle begins at (0,0)
and has zero width and height.

computeUnion

```java
public static
Rectangle
computeUnion​(int x,
int y,
int width,
int height,

Rectangle
dest)
```

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

**Parameters:** x

- the x-coordinate of the first rectangle
**Parameters:** y

- the y-coordinate of the first rectangle
**Parameters:** width

- the width of the first rectangle
**Parameters:** height

- the height of the first rectangle
**Parameters:** dest

- the coordinates of the second rectangle; the union
of the two rectangles is returned in this rectangle
**Returns:** the

dest

Rectangle

---

#### computeUnion

public static

Rectangle

computeUnion​(int x,
int y,
int width,
int height,

Rectangle

dest)

Convenience method that calculates the union of two rectangles
without allocating a new rectangle.

computeDifference

```java
public static
Rectangle
[] computeDifference​(
Rectangle
rectA,

Rectangle
rectB)
```

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

. If the
two Rects do not overlap, returns an empty array

**Parameters:** rectA

- the first rectangle
**Parameters:** rectB

- the second rectangle
**Returns:** an array of rectangles representing the regions within

rectA

that do not overlap with

rectB

.

---

#### computeDifference

public static

Rectangle

[] computeDifference​(

Rectangle

rectA,

Rectangle

rectB)

Convenience returning an array of rect representing the regions within

rectA

that do not overlap with

rectB

. If the
two Rects do not overlap, returns an empty array

isLeftMouseButton

```java
public static boolean isLeftMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the left mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the left mouse button was active

---

#### isLeftMouseButton

public static boolean isLeftMouseButton​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the left mouse button.

isMiddleMouseButton

```java
public static boolean isMiddleMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the middle mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the middle mouse button was active

---

#### isMiddleMouseButton

public static boolean isMiddleMouseButton​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the middle mouse button.

isRightMouseButton

```java
public static boolean isRightMouseButton​(
MouseEvent
anEvent)
```

Returns true if the mouse event specifies the right mouse button.

**Parameters:** anEvent

- a MouseEvent object
**Returns:** true if the right mouse button was active

---

#### isRightMouseButton

public static boolean isRightMouseButton​(

MouseEvent

anEvent)

Returns true if the mouse event specifies the right mouse button.

computeStringWidth

```java
public static int computeStringWidth​(
FontMetrics
fm,

String
str)
```

Compute the width of the string using a font with the specified
"metrics" (sizes).

**Parameters:** fm

- a FontMetrics object to compute with
**Parameters:** str

- the String to compute
**Returns:** an int containing the string width

---

#### computeStringWidth

public static int computeStringWidth​(

FontMetrics

fm,

String

str)

Compute the width of the string using a font with the specified
"metrics" (sizes).

layoutCompoundLabel

```java
public static
String
layoutCompoundLabel​(
JComponent
c,

FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)
```

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
The JComponents orientation (LEADING/TRAILING) will also be taken
into account and translated into LEFT/RIGHT values accordingly.

**Parameters:** c

- the component
**Parameters:** fm

- the instance of

FontMetrics
**Parameters:** text

- the text
**Parameters:** icon

- the icon
**Parameters:** verticalAlignment

- the vertical alignment
**Parameters:** horizontalAlignment

- the horizontal alignment
**Parameters:** verticalTextPosition

- the vertical text position
**Parameters:** horizontalTextPosition

- the horizontal text position
**Parameters:** viewR

- the available rectangle
**Parameters:** iconR

- the rectangle for the icon
**Parameters:** textR

- the rectangle for the text
**Parameters:** textIconGap

- the gap between text and icon
**Returns:** the possibly clipped version of the compound labels string

---

#### layoutCompoundLabel

public static

String

layoutCompoundLabel​(

JComponent

c,

FontMetrics

fm,

String

text,

Icon

icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
The JComponents orientation (LEADING/TRAILING) will also be taken
into account and translated into LEFT/RIGHT values accordingly.

layoutCompoundLabel

```java
public static
String
layoutCompoundLabel​(
FontMetrics
fm,

String
text,

Icon
icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int textIconGap)
```

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
This layoutCompoundLabel() does not know how to handle LEADING/TRAILING
values in horizontalTextPosition (they will default to RIGHT) and in
horizontalAlignment (they will default to CENTER).
Use the other version of layoutCompoundLabel() instead.

**Parameters:** fm

- the instance of

FontMetrics
**Parameters:** text

- the text
**Parameters:** icon

- the icon
**Parameters:** verticalAlignment

- the vertical alignment
**Parameters:** horizontalAlignment

- the horizontal alignment
**Parameters:** verticalTextPosition

- the vertical text position
**Parameters:** horizontalTextPosition

- the horizontal text position
**Parameters:** viewR

- the available rectangle
**Parameters:** iconR

- the rectangle for the icon
**Parameters:** textR

- the rectangle for the text
**Parameters:** textIconGap

- the gap between text and icon
**Returns:** the possibly clipped version of the compound labels string

---

#### layoutCompoundLabel

public static

String

layoutCompoundLabel​(

FontMetrics

fm,

String

text,

Icon

icon,
int verticalAlignment,
int horizontalAlignment,
int verticalTextPosition,
int horizontalTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int textIconGap)

Compute and return the location of the icons origin, the
location of origin of the text baseline, and a possibly clipped
version of the compound labels string. Locations are computed
relative to the viewR rectangle.
This layoutCompoundLabel() does not know how to handle LEADING/TRAILING
values in horizontalTextPosition (they will default to RIGHT) and in
horizontalAlignment (they will default to CENTER).
Use the other version of layoutCompoundLabel() instead.

paintComponent

```java
public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,
int x,
int y,
int w,
int h)
```

Paints a component to the specified

Graphics

.
This method is primarily useful to render

Component

s that don't exist as part of the visible
containment hierarchy, but are used for rendering. For
example, if you are doing your own rendering and want to render
some text (or even HTML), you could make use of

JLabel

's text rendering support and have it paint
directly by way of this method, without adding the label to the
visible containment hierarchy.

This method makes use of

CellRendererPane

to handle
the actual painting, and is only recommended if you use one
component for rendering. If you make use of multiple components
to handle the rendering, as

JTable

does, use

CellRendererPane

directly. Otherwise, as described
below, you could end up with a

CellRendererPane

per

Component

.

If

c

's parent is not a

CellRendererPane

,
a new

CellRendererPane

is created,

c

is
added to it, and the

CellRendererPane

is added to

p

. If

c

's parent is a

CellRendererPane

and the

CellRendererPane

s
parent is not

p

, it is added to

p

.

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

**Parameters:** g

- the

Graphics

object to draw on
**Parameters:** c

- the

Component

to draw
**Parameters:** p

- the intermediate

Container
**Parameters:** x

- an int specifying the left side of the area draw in, in pixels,
measured from the left edge of the graphics context
**Parameters:** y

- an int specifying the top of the area to draw in, in pixels
measured down from the top edge of the graphics context
**Parameters:** w

- an int specifying the width of the area draw in, in pixels
**Parameters:** h

- an int specifying the height of the area draw in, in pixels
**See Also:** CellRendererPane

,

Component.isLightweight()

---

#### paintComponent

public static void paintComponent​(

Graphics

g,

Component

c,

Container

p,
int x,
int y,
int w,
int h)

Paints a component to the specified

Graphics

.
This method is primarily useful to render

Component

s that don't exist as part of the visible
containment hierarchy, but are used for rendering. For
example, if you are doing your own rendering and want to render
some text (or even HTML), you could make use of

JLabel

's text rendering support and have it paint
directly by way of this method, without adding the label to the
visible containment hierarchy.

This method makes use of

CellRendererPane

to handle
the actual painting, and is only recommended if you use one
component for rendering. If you make use of multiple components
to handle the rendering, as

JTable

does, use

CellRendererPane

directly. Otherwise, as described
below, you could end up with a

CellRendererPane

per

Component

.

If

c

's parent is not a

CellRendererPane

,
a new

CellRendererPane

is created,

c

is
added to it, and the

CellRendererPane

is added to

p

. If

c

's parent is a

CellRendererPane

and the

CellRendererPane

s
parent is not

p

, it is added to

p

.

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

This method makes use of

CellRendererPane

to handle
the actual painting, and is only recommended if you use one
component for rendering. If you make use of multiple components
to handle the rendering, as

JTable

does, use

CellRendererPane

directly. Otherwise, as described
below, you could end up with a

CellRendererPane

per

Component

.

If

c

's parent is not a

CellRendererPane

,
a new

CellRendererPane

is created,

c

is
added to it, and the

CellRendererPane

is added to

p

. If

c

's parent is a

CellRendererPane

and the

CellRendererPane

s
parent is not

p

, it is added to

p

.

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

If

c

's parent is not a

CellRendererPane

,
a new

CellRendererPane

is created,

c

is
added to it, and the

CellRendererPane

is added to

p

. If

c

's parent is a

CellRendererPane

and the

CellRendererPane

s
parent is not

p

, it is added to

p

.

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

The component should either descend from

JComponent

or be another kind of lightweight component.
A lightweight component is one whose "lightweight" property
(returned by the

Component

isLightweight

method)
is true. If the Component is not lightweight, bad things map happen:
crashes, exceptions, painting problems...

paintComponent

```java
public static void paintComponent​(
Graphics
g,

Component
c,

Container
p,

Rectangle
r)
```

Paints a component to the specified

Graphics

. This
is a cover method for

paintComponent(Graphics,Component,Container,int,int,int,int)

.
Refer to it for more information.

**Parameters:** g

- the

Graphics

object to draw on
**Parameters:** c

- the

Component

to draw
**Parameters:** p

- the intermediate

Container
**Parameters:** r

- the

Rectangle

to draw in
**See Also:** paintComponent(Graphics,Component,Container,int,int,int,int)

,

CellRendererPane

---

#### paintComponent

public static void paintComponent​(

Graphics

g,

Component

c,

Container

p,

Rectangle

r)

Paints a component to the specified

Graphics

. This
is a cover method for

paintComponent(Graphics,Component,Container,int,int,int,int)

.
Refer to it for more information.

updateComponentTreeUI

```java
public static void updateComponentTreeUI​(
Component
c)
```

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

**Parameters:** c

- the component

---

#### updateComponentTreeUI

public static void updateComponentTreeUI​(

Component

c)

A simple minded look and feel change: ask each node in the tree
to

updateUI()

-- that is, to initialize its UI property
with the current look and feel.

invokeLater

```java
public static void invokeLater​(
Runnable
doRun)
```

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread. This will happen after all
pending AWT events have been processed. This method should
be used when an application thread needs to update the GUI.
In the following example the

invokeLater

call queues
the

Runnable

object

doHelloWorld

on the event dispatching thread and
then prints a message.

```java
Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

SwingUtilities.invokeLater(doHelloWorld);
System.out.println("This might well be displayed before the other message.");
```

If invokeLater is called from the event dispatching thread --
for example, from a JButton's ActionListener -- the

doRun.run()

will
still be deferred until all pending events have been processed.
Note that if the

doRun.run()

throws an uncaught exception
the event dispatching thread will unwind (not the current thread).

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeLater()

.

Unlike the rest of Swing, this method can be invoked from any thread.

**Parameters:** doRun

- the instance of

Runnable
**See Also:** invokeAndWait(java.lang.Runnable)

---

#### invokeLater

public static void invokeLater​(

Runnable

doRun)

Causes

doRun.run()

to be executed asynchronously on the
AWT event dispatching thread. This will happen after all
pending AWT events have been processed. This method should
be used when an application thread needs to update the GUI.
In the following example the

invokeLater

call queues
the

Runnable

object

doHelloWorld

on the event dispatching thread and
then prints a message.

```java
Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

SwingUtilities.invokeLater(doHelloWorld);
System.out.println("This might well be displayed before the other message.");
```

If invokeLater is called from the event dispatching thread --
for example, from a JButton's ActionListener -- the

doRun.run()

will
still be deferred until all pending events have been processed.
Note that if the

doRun.run()

throws an uncaught exception
the event dispatching thread will unwind (not the current thread).

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeLater()

.

Unlike the rest of Swing, this method can be invoked from any thread.

Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

SwingUtilities.invokeLater(doHelloWorld);
System.out.println("This might well be displayed before the other message.");

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeLater()

.

Unlike the rest of Swing, this method can be invoked from any thread.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeLater()

.

Unlike the rest of Swing, this method can be invoked from any thread.

Unlike the rest of Swing, this method can be invoked from any thread.

invokeAndWait

```java
public static void invokeAndWait​(
Runnable
doRun)
throws
InterruptedException
,

InvocationTargetException
```

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread. This call blocks until
all pending AWT events have been processed and (then)

doRun.run()

returns. This method should
be used when an application thread needs to update the GUI.
It shouldn't be called from the event dispatching thread.
Here's an example that creates a new application thread
that uses

invokeAndWait

to print a string from the event
dispatching thread and then, when that's finished, print
a string from the application thread.

```java
final Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

Thread appThread = new Thread() {
public void run() {
try {
SwingUtilities.invokeAndWait(doHelloWorld);
}
catch (Exception e) {
e.printStackTrace();
}
System.out.println("Finished on " + Thread.currentThread());
}
};
appThread.start();
```

Note that if the

Runnable.run

method throws an
uncaught exception
(on the event dispatching thread) it's caught and rethrown, as
an

InvocationTargetException

, on the caller's thread.

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeAndWait()

.

**Parameters:** doRun

- the instance of

Runnable
**Throws:** InterruptedException

- if we're interrupted while waiting for
the event dispatching thread to finish executing

doRun.run()
**Throws:** InvocationTargetException

- if an exception is thrown
while running

doRun
**See Also:** invokeLater(java.lang.Runnable)

---

#### invokeAndWait

public static void invokeAndWait​(

Runnable

doRun)
throws

InterruptedException

,

InvocationTargetException

Causes

doRun.run()

to be executed synchronously on the
AWT event dispatching thread. This call blocks until
all pending AWT events have been processed and (then)

doRun.run()

returns. This method should
be used when an application thread needs to update the GUI.
It shouldn't be called from the event dispatching thread.
Here's an example that creates a new application thread
that uses

invokeAndWait

to print a string from the event
dispatching thread and then, when that's finished, print
a string from the application thread.

```java
final Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

Thread appThread = new Thread() {
public void run() {
try {
SwingUtilities.invokeAndWait(doHelloWorld);
}
catch (Exception e) {
e.printStackTrace();
}
System.out.println("Finished on " + Thread.currentThread());
}
};
appThread.start();
```

Note that if the

Runnable.run

method throws an
uncaught exception
(on the event dispatching thread) it's caught and rethrown, as
an

InvocationTargetException

, on the caller's thread.

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeAndWait()

.

final Runnable doHelloWorld = new Runnable() {
public void run() {
System.out.println("Hello World on " + Thread.currentThread());
}
};

Thread appThread = new Thread() {
public void run() {
try {
SwingUtilities.invokeAndWait(doHelloWorld);
}
catch (Exception e) {
e.printStackTrace();
}
System.out.println("Finished on " + Thread.currentThread());
}
};
appThread.start();

Additional documentation and examples for this method can be
found in

Concurrency in Swing

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeAndWait()

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.invokeAndWait()

.

isEventDispatchThread

```java
public static boolean isEventDispatchThread()
```

Returns true if the current thread is an AWT event dispatching thread.

As of 1.3 this method is just a cover for

java.awt.EventQueue.isDispatchThread()

.

**Returns:** true if the current thread is an AWT event dispatching thread

---

#### isEventDispatchThread

public static boolean isEventDispatchThread()

Returns true if the current thread is an AWT event dispatching thread.

As of 1.3 this method is just a cover for

java.awt.EventQueue.isDispatchThread()

.

As of 1.3 this method is just a cover for

java.awt.EventQueue.isDispatchThread()

.

getAccessibleIndexInParent

```java
public static int getAccessibleIndexInParent​(
Component
c)
```

Get the index of this object in its accessible parent.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** -1 of this object does not have an accessible parent.
Otherwise, the index of the child in its accessible parent.

---

#### getAccessibleIndexInParent

public static int getAccessibleIndexInParent​(

Component

c)

Get the index of this object in its accessible parent.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

getAccessibleAt

```java
public static
Accessible
getAccessibleAt​(
Component
c,

Point
p)
```

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.
Otherwise returns

null

.

**Parameters:** c

- the component
**Parameters:** p

- the local coordinate
**Returns:** the

Accessible

at the specified location,
if it exists; otherwise

null

---

#### getAccessibleAt

public static

Accessible

getAccessibleAt​(

Component

c,

Point

p)

Returns the

Accessible

child contained at the
local coordinate

Point

, if one exists.
Otherwise returns

null

.

getAccessibleStateSet

```java
public static
AccessibleStateSet
getAccessibleStateSet​(
Component
c)
```

Get the state of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** an instance of AccessibleStateSet containing the current state
set of the object
**See Also:** AccessibleState

---

#### getAccessibleStateSet

public static

AccessibleStateSet

getAccessibleStateSet​(

Component

c)

Get the state of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

getAccessibleChildrenCount

```java
public static int getAccessibleChildrenCount​(
Component
c)
```

Returns the number of accessible children in the object. If all
of the children of this object implement Accessible, than this
method should return the number of children of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Returns:** the number of accessible children in the object.

---

#### getAccessibleChildrenCount

public static int getAccessibleChildrenCount​(

Component

c)

Returns the number of accessible children in the object. If all
of the children of this object implement Accessible, than this
method should return the number of children of this object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

getAccessibleChild

```java
public static
Accessible
getAccessibleChild​(
Component
c,
int i)
```

Return the nth Accessible child of the object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

**Parameters:** c

- the component
**Parameters:** i

- zero-based index of child
**Returns:** the nth Accessible child of the object

---

#### getAccessibleChild

public static

Accessible

getAccessibleChild​(

Component

c,
int i)

Return the nth Accessible child of the object.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

Note: as of the Java 2 platform v1.3, it is recommended that developers call
Component.AccessibleAWTComponent.getAccessibleIndexInParent() instead
of using this method.

findFocusOwner

```java
@Deprecated

public static
Component
findFocusOwner​(
Component
c)
```

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getFocusOwner()

.

Return the child

Component

of the specified

Component

that is the focus owner, if any.

**Parameters:** c

- the root of the

Component

hierarchy to
search for the focus owner
**Returns:** the focus owner, or

null

if there is no focus
owner, or if the focus owner is not

comp

, or a
descendant of

comp
**See Also:** KeyboardFocusManager.getFocusOwner()

---

#### findFocusOwner

@Deprecated

public static

Component

findFocusOwner​(

Component

c)

Return the child

Component

of the specified

Component

that is the focus owner, if any.

getRootPane

```java
public static
JRootPane
getRootPane​(
Component
c)
```

If c is a JRootPane descendant return its JRootPane ancestor.
If c is a RootPaneContainer then return its JRootPane.

**Parameters:** c

- the component
**Returns:** the JRootPane for Component c or

null

.

---

#### getRootPane

public static

JRootPane

getRootPane​(

Component

c)

If c is a JRootPane descendant return its JRootPane ancestor.
If c is a RootPaneContainer then return its JRootPane.

getRoot

```java
public static
Component
getRoot​(
Component
c)
```

Returns the root component for the current component tree.

**Parameters:** c

- the component
**Returns:** the first ancestor of c that's a Window or the last Applet ancestor

---

#### getRoot

public static

Component

getRoot​(

Component

c)

Returns the root component for the current component tree.

processKeyBindings

```java
public static boolean processKeyBindings​(
KeyEvent
event)
```

Process the key bindings for the

Component

associated with

event

. This method is only useful if

event.getComponent()

does not descend from

JComponent

, or your are not invoking

super.processKeyEvent

from within your

JComponent

subclass.

JComponent

automatically processes bindings from within its

processKeyEvent

method, hence you rarely need
to directly invoke this method.

**Parameters:** event

- KeyEvent used to identify which bindings to process, as
well as which Component has focus.
**Returns:** true if a binding has found and processed
**Since:** 1.4

---

#### processKeyBindings

public static boolean processKeyBindings​(

KeyEvent

event)

Process the key bindings for the

Component

associated with

event

. This method is only useful if

event.getComponent()

does not descend from

JComponent

, or your are not invoking

super.processKeyEvent

from within your

JComponent

subclass.

JComponent

automatically processes bindings from within its

processKeyEvent

method, hence you rarely need
to directly invoke this method.

notifyAction

```java
public static boolean notifyAction​(
Action
action,

KeyStroke
ks,

KeyEvent
event,

Object
sender,
int modifiers)
```

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.
The command for the ActionEvent is determined by:

- If the action was registered via

registerKeyboardAction

, then the command string
passed in (

null

will be used if

null

was passed in).

Action value with name Action.ACTION_COMMAND_KEY, unless

null

.

String value of the KeyEvent, unless

getKeyChar

returns KeyEvent.CHAR_UNDEFINED..

This will return true if

action

is non-

null

and
actionPerformed is invoked on it.

**Parameters:** action

- an action
**Parameters:** ks

- a key stroke
**Parameters:** event

- a key event
**Parameters:** sender

- a sender
**Parameters:** modifiers

- action modifiers
**Returns:** true

if

action

is non-

null

and
actionPerformed is invoked on it.
**Since:** 1.3
**See Also:** Action.accept(java.lang.Object)

---

#### notifyAction

public static boolean notifyAction​(

Action

action,

KeyStroke

ks,

KeyEvent

event,

Object

sender,
int modifiers)

Invokes

actionPerformed

on

action

if

action

is non-

null

and accepts the sender object.
The command for the ActionEvent is determined by:

- If the action was registered via

registerKeyboardAction

, then the command string
passed in (

null

will be used if

null

was passed in).

Action value with name Action.ACTION_COMMAND_KEY, unless

null

.

String value of the KeyEvent, unless

getKeyChar

returns KeyEvent.CHAR_UNDEFINED..

This will return true if

action

is non-

null

and
actionPerformed is invoked on it.

If the action was registered via

registerKeyboardAction

, then the command string
passed in (

null

will be used if

null

was passed in).

Action value with name Action.ACTION_COMMAND_KEY, unless

null

.

String value of the KeyEvent, unless

getKeyChar

returns KeyEvent.CHAR_UNDEFINED..

replaceUIInputMap

```java
public static void replaceUIInputMap​(
JComponent
component,
int type,

InputMap
uiInputMap)
```

Convenience method to change the UI InputMap for

component

to

uiInputMap

. If

uiInputMap

is

null

,
this removes any previously installed UI InputMap.

**Parameters:** component

- a component
**Parameters:** type

- a type
**Parameters:** uiInputMap

- an

InputMap
**Since:** 1.3

---

#### replaceUIInputMap

public static void replaceUIInputMap​(

JComponent

component,
int type,

InputMap

uiInputMap)

Convenience method to change the UI InputMap for

component

to

uiInputMap

. If

uiInputMap

is

null

,
this removes any previously installed UI InputMap.

replaceUIActionMap

```java
public static void replaceUIActionMap​(
JComponent
component,

ActionMap
uiActionMap)
```

Convenience method to change the UI ActionMap for

component

to

uiActionMap

. If

uiActionMap

is

null

,
this removes any previously installed UI ActionMap.

**Parameters:** component

- a component
**Parameters:** uiActionMap

- an

ActionMap
**Since:** 1.3

---

#### replaceUIActionMap

public static void replaceUIActionMap​(

JComponent

component,

ActionMap

uiActionMap)

Convenience method to change the UI ActionMap for

component

to

uiActionMap

. If

uiActionMap

is

null

,
this removes any previously installed UI ActionMap.

getUIInputMap

```java
public static
InputMap
getUIInputMap​(
JComponent
component,
int condition)
```

Returns the InputMap provided by the UI for condition

condition

in component

component

.

This will return

null

if the UI has not installed an InputMap
of the specified type.

**Parameters:** component

- a component
**Parameters:** condition

- a condition
**Returns:** the

ActionMap

provided by the UI for

condition

in the component, or

null

if the UI has not installed
an InputMap of the specified type.
**Since:** 1.3

---

#### getUIInputMap

public static

InputMap

getUIInputMap​(

JComponent

component,
int condition)

Returns the InputMap provided by the UI for condition

condition

in component

component

.

This will return

null

if the UI has not installed an InputMap
of the specified type.

This will return

null

if the UI has not installed an InputMap
of the specified type.

getUIActionMap

```java
public static
ActionMap
getUIActionMap​(
JComponent
component)
```

Returns the ActionMap provided by the UI
in component

component

.

This will return

null

if the UI has not installed an ActionMap.

**Parameters:** component

- a component
**Returns:** the

ActionMap

provided by the UI in the component,
or

null

if the UI has not installed an ActionMap.
**Since:** 1.3

---

#### getUIActionMap

public static

ActionMap

getUIActionMap​(

JComponent

component)

Returns the ActionMap provided by the UI
in component

component

.

This will return

null

if the UI has not installed an ActionMap.

This will return

null

if the UI has not installed an ActionMap.

calculateInnerArea

```java
public static
Rectangle
calculateInnerArea​(
JComponent
c,

Rectangle
r)
```

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.
The position and size specify the bounds of the component,
adjusted so as not to include the border area (the insets).
This method is useful for classes
that implement painting code.

**Parameters:** c

- the JComponent in question; if

null

, this method returns

null
**Parameters:** r

- the Rectangle instance to be modified;
may be

null
**Returns:** null

if the Component is

null

;
otherwise, returns the passed-in rectangle (if non-

null

)
or a new rectangle specifying position and size information
**Since:** 1.4

---

#### calculateInnerArea

public static

Rectangle

calculateInnerArea​(

JComponent

c,

Rectangle

r)

Stores the position and size of
the inner painting area of the specified component
in

r

and returns

r

.
The position and size specify the bounds of the component,
adjusted so as not to include the border area (the insets).
This method is useful for classes
that implement painting code.

getUnwrappedParent

```java
public static
Container
getUnwrappedParent​(
Component
component)
```

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

**Parameters:** component

-

Component

to get
the first ancestor of, which is not a

JLayer

instance.
**Returns:** the first ancestor of the

component

which is not an instance of

JLayer

.
If such an ancestor can not be found,

null

is returned.
**Throws:** NullPointerException

- if

component

is

null
**Since:** 1.7
**See Also:** JLayer

---

#### getUnwrappedParent

public static

Container

getUnwrappedParent​(

Component

component)

Returns the first ancestor of the

component

which is not an instance of

JLayer

.

getUnwrappedView

```java
public static
Component
getUnwrappedView​(
JViewport
viewport)
```

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.

If the

viewport

's view component is not a

JLayer

,
this method is equivalent to

JViewport.getView()

otherwise

JLayer.getView()

will be recursively
called on all descending

JLayer

s.

**Parameters:** viewport

-

JViewport

to get the first descendant of,
which in not a

JLayer

instance.
**Returns:** the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.
**Throws:** NullPointerException

- if

viewport

is

null
**Since:** 1.7
**See Also:** JViewport.getView()

,

JLayer

---

#### getUnwrappedView

public static

Component

getUnwrappedView​(

JViewport

viewport)

Returns the first

JViewport

's descendant
which is not an instance of

JLayer

.
If such a descendant can not be found,

null

is returned.

If the

viewport

's view component is not a

JLayer

,
this method is equivalent to

JViewport.getView()

otherwise

JLayer.getView()

will be recursively
called on all descending

JLayer

s.

---

