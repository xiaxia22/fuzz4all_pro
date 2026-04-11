# Class CompositeView

**Source:** `java.desktop\javax\swing\text\CompositeView.html`

### Class Description

```java
public abstract class
CompositeView

extends
View
```

CompositeView

is an abstract

View

implementation which manages one or more child views.
(Note that

CompositeView

is intended
for managing relatively small numbers of child views.)

CompositeView

is intended to be used as
a starting point for

View

implementations,
such as

BoxView

, that will contain child

View

s. Subclasses that wish to manage the
collection of child

View

s should use the

replace(int, int, javax.swing.text.View[])

method. As

View

invokes

replace

during

DocumentListener

notification, you normally won't need to directly
invoke

replace

.

While

CompositeView

does not impose a layout policy on its child

View

s,
it does allow for inseting the child

View

s
it will contain. The insets can be set by either

setInsets(short, short, short, short)

or

setParagraphInsets(javax.swing.text.AttributeSet)

.

In addition to the abstract methods of

View

,
subclasses of

CompositeView

will need to
override:

- isBefore(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is before the visual space
of the

CompositeView

.

isAfter(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is after the visual space
of the

CompositeView

.

getViewAtPoint(int, int, java.awt.Rectangle)

- Returns the view at
a given visual location.

childAllocation(int, java.awt.Rectangle)

- Returns the bounds of
a particular child

View

.

getChildAllocation

will invoke

childAllocation

after offseting
the bounds by the

Inset

s of the

CompositeView

.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompositeView​(
Element
elem)

Constructs a

CompositeView

for the given element.

**Parameters:**
- elem

- the element this view is responsible for

---

### Method Details

#### protected void loadChildren​(
ViewFactory
f)

Loads all of the children to initialize the view.
This is called by the

setParent(javax.swing.text.View)

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

**Parameters:**
- f

- the view factory

**See Also:**
- setParent(javax.swing.text.View)

---

#### public void setParent​(
View
parent)

Sets the parent of the view.
This is reimplemented to provide the superclass
behavior as well as calling the

loadChildren

method if this view does not already have children.
The children should not be loaded in the
constructor because the act of setting the parent
may cause them to try to search up the hierarchy
(to get the hosting

Container

for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

**Overrides:**
- setParent

in class

View

**Parameters:**
- parent

- the parent of the view,

null

if none

---

#### public int getViewCount()

Returns the number of child views of this view.

**Overrides:**
- getViewCount

in class

View

**Returns:**
- the number of views >= 0

**See Also:**
- getView(int)

---

#### public
View
getView​(int n)

Returns the n-th view in this container.

**Overrides:**
- getView

in class

View

**Parameters:**
- n

- the number of the desired view, >= 0 && < getViewCount()

**Returns:**
- the view at index

n

---

#### public void replace​(int offset,
int length,

View
[] views)

Replaces child views. If there are no views to remove
this acts as an insert. If there are no views to
add this acts as a remove. Views being removed will
have the parent set to

null

,
and the internal reference to them removed so that they
may be garbage collected.

**Overrides:**
- replace

in class

View

**Parameters:**
- offset

- the starting index into the child views to insert
the new views; >= 0 and <= getViewCount
- length

- the number of existing child views to remove;
this should be a value >= 0 and <= (getViewCount() - offset)
- views

- the child views to add; this value can be

null

to indicate no children are being added (useful to remove)

---

#### public
Shape
getChildAllocation​(int index,

Shape
a)

Fetches the allocation for the given child view to
render into. This enables finding out where various views
are located.

**Overrides:**
- getChildAllocation

in class

View

**Parameters:**
- index

- the index of the child, >= 0 && < getViewCount()
- a

- the allocation to this view

**Returns:**
- the allocation to the child

---

#### public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:**
- modelToView

in class

View

**Parameters:**
- pos

- the position to convert >= 0
- a

- the allocated region to render into
- b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward

**Returns:**
- the bounding box of the given position

**Throws:**
- BadLocationException

- if the given position does
not represent a valid location in the associated document

**See Also:**
- View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### public
Shape
modelToView​(int p0,

Position.Bias
b0,
int p1,

Position.Bias
b1,

Shape
a)
throws
BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:**
- modelToView

in class

View

**Parameters:**
- p0

- the position to convert >= 0
- b0

- the bias toward the previous character or the
next character represented by p0, in case the
position is a boundary of two views; either

Position.Bias.Forward

or

Position.Bias.Backward
- p1

- the position to convert >= 0
- b1

- the bias toward the previous character or the
next character represented by p1, in case the
position is a boundary of two views
- a

- the allocated region to render into

**Returns:**
- the bounding box of the given position is returned

**Throws:**
- BadLocationException

- if the given position does
not represent a valid location in the associated document
- IllegalArgumentException

- for an invalid bias argument

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:**
- viewToModel

in class

View

**Parameters:**
- x

- x coordinate of the view location to convert >= 0
- y

- y coordinate of the view location to convert >= 0
- a

- the allocated region to render into
- bias

- either

Position.Bias.Forward

or

Position.Bias.Backward

**Returns:**
- the location within the model that best represents the
given point in the view >= 0

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### public int getNextVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.
This is a convenience method for

getNextNorthSouthVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

and

getNextEastWestVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

.
This method enables specifying a position to convert
within the range of >=0. If the value is -1, a position
will be calculated automatically. If the value < -1,
the

BadLocationException

will be thrown.

**Overrides:**
- getNextVisualPositionFrom

in class

View

**Parameters:**
- pos

- the position to convert
- b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
- a

- the allocated region to render into
- direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
- biasRet

- an array containing the bias that was checked

**Returns:**
- the location within the model that best represents the next
location visual position

**Throws:**
- BadLocationException

- the given position is not a valid
position within the document
- IllegalArgumentException

- if

direction

is invalid

---

#### public int getViewIndex​(int pos,

Position.Bias
b)

Returns the child view index representing the given
position in the model. This is implemented to call the

getViewIndexByPosition

method for backward compatibility.

**Overrides:**
- getViewIndex

in class

View

**Parameters:**
- pos

- the position >= 0
- b

- the bias

**Returns:**
- index of the view representing the given position, or
-1 if no view represents that position

**Since:**
- 1.3

---

#### protected abstract boolean isBefore​(int x,
int y,

Rectangle
alloc)

Tests whether a point lies before the rectangle range.

**Parameters:**
- x

- the X coordinate >= 0
- y

- the Y coordinate >= 0
- alloc

- the rectangle

**Returns:**
- true if the point is before the specified range

---

#### protected abstract boolean isAfter​(int x,
int y,

Rectangle
alloc)

Tests whether a point lies after the rectangle range.

**Parameters:**
- x

- the X coordinate >= 0
- y

- the Y coordinate >= 0
- alloc

- the rectangle

**Returns:**
- true if the point is after the specified range

---

#### protected abstract
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)

Fetches the child view at the given coordinates.

**Parameters:**
- x

- the X coordinate >= 0
- y

- the Y coordinate >= 0
- alloc

- the parent's allocation on entry, which should
be changed to the child's allocation on exit

**Returns:**
- the child view

---

#### protected abstract void childAllocation​(int index,

Rectangle
a)

Returns the allocation for a given child.

**Parameters:**
- index

- the index of the child, >= 0 && < getViewCount()
- a

- the allocation to the interior of the box on entry,
and the allocation of the child view at the index on exit.

---

#### protected
View
getViewAtPosition​(int pos,

Rectangle
a)

Fetches the child view that represents the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:**
- pos

- the position >= 0
- a

- the allocation to the interior of the box on entry,
and the allocation of the view containing the position on exit

**Returns:**
- the view representing the given position, or

null

if there isn't one

---

#### protected int getViewIndexAtPosition​(int pos)

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:**
- pos

- the position >= 0

**Returns:**
- index of the view representing the given position, or
-1 if no view represents that position

---

#### protected
Rectangle
getInsideAllocation​(
Shape
a)

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.
It is expected that the returned value would be further
mutated to represent an allocation to a child view.
This is implemented to reuse an instance variable so
it avoids creating excessive Rectangles. Typically
the result of calling this method would be fed to
the

childAllocation

method.

**Parameters:**
- a

- the allocation given to the view

**Returns:**
- the allocation that represents the inside of the
view after the margins have all been removed; if the
given allocation was

null

,
the return value is

null

---

#### protected void setParagraphInsets​(
AttributeSet
attr)

Sets the insets from the paragraph attributes specified in
the given attributes.

**Parameters:**
- attr

- the attributes

---

#### protected void setInsets​(short top,
short left,
short bottom,
short right)

Sets the insets for the view.

**Parameters:**
- top

- the top inset >= 0
- left

- the left inset >= 0
- bottom

- the bottom inset >= 0
- right

- the right inset >= 0

---

#### protected short getLeftInset()

Gets the left inset.

**Returns:**
- the inset >= 0

---

#### protected short getRightInset()

Gets the right inset.

**Returns:**
- the inset >= 0

---

#### protected short getTopInset()

Gets the top inset.

**Returns:**
- the inset >= 0

---

#### protected short getBottomInset()

Gets the bottom inset.

**Returns:**
- the inset >= 0

---

#### protected int getNextNorthSouthVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException

Returns the next visual position for the cursor, in either the
north or south direction.

**Parameters:**
- pos

- the position to convert >= 0
- b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
- a

- the allocated region to render into
- direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.NORTH

SwingConstants.SOUTH
- biasRet

- an array containing the bias that was checked

**Returns:**
- the location within the model that best represents the next
north or south location

**Throws:**
- BadLocationException

- for a bad location within a document model
- IllegalArgumentException

- if

direction

is invalid

**See Also:**
- getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

---

#### protected int getNextEastWestVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException

Returns the next visual position for the cursor, in either the
east or west direction.

**Parameters:**
- pos

- the position to convert >= 0
- b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
- a

- the allocated region to render into
- direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST
- biasRet

- an array containing the bias that was checked

**Returns:**
- the location within the model that best represents the next
west or east location

**Throws:**
- BadLocationException

- for a bad location within a document model
- IllegalArgumentException

- if

direction

is invalid

**See Also:**
- getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

---

#### protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)

Determines in which direction the next view lays.
Consider the

View

at index n. Typically the

View

s are layed out from left to right,
so that the

View

to the EAST will be
at index n + 1, and the

View

to the WEST
will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true, indicating the

View

s are layed out in descending order.

This unconditionally returns false, subclasses should override this
method if there is the possibility for laying

View

s in
descending order.

**Parameters:**
- position

- position into the model
- bias

- either

Position.Bias.Forward

or

Position.Bias.Backward

**Returns:**
- false

---

### Additional Sections

#### Class CompositeView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.CompositeView

javax.swing.text.View

- javax.swing.text.CompositeView

javax.swing.text.CompositeView

**All Implemented Interfaces:** SwingConstants

**Direct Known Subclasses:** BoxView

```java
public abstract class
CompositeView

extends
View
```

CompositeView

is an abstract

View

implementation which manages one or more child views.
(Note that

CompositeView

is intended
for managing relatively small numbers of child views.)

CompositeView

is intended to be used as
a starting point for

View

implementations,
such as

BoxView

, that will contain child

View

s. Subclasses that wish to manage the
collection of child

View

s should use the

replace(int, int, javax.swing.text.View[])

method. As

View

invokes

replace

during

DocumentListener

notification, you normally won't need to directly
invoke

replace

.

While

CompositeView

does not impose a layout policy on its child

View

s,
it does allow for inseting the child

View

s
it will contain. The insets can be set by either

setInsets(short, short, short, short)

or

setParagraphInsets(javax.swing.text.AttributeSet)

.

In addition to the abstract methods of

View

,
subclasses of

CompositeView

will need to
override:

- isBefore(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is before the visual space
of the

CompositeView

.

isAfter(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is after the visual space
of the

CompositeView

.

getViewAtPoint(int, int, java.awt.Rectangle)

- Returns the view at
a given visual location.

childAllocation(int, java.awt.Rectangle)

- Returns the bounds of
a particular child

View

.

getChildAllocation

will invoke

childAllocation

after offseting
the bounds by the

Inset

s of the

CompositeView

.

public abstract class

CompositeView

extends

View

CompositeView

is an abstract

View

implementation which manages one or more child views.
(Note that

CompositeView

is intended
for managing relatively small numbers of child views.)

CompositeView

is intended to be used as
a starting point for

View

implementations,
such as

BoxView

, that will contain child

View

s. Subclasses that wish to manage the
collection of child

View

s should use the

replace(int, int, javax.swing.text.View[])

method. As

View

invokes

replace

during

DocumentListener

notification, you normally won't need to directly
invoke

replace

.

While

CompositeView

does not impose a layout policy on its child

View

s,
it does allow for inseting the child

View

s
it will contain. The insets can be set by either

setInsets(short, short, short, short)

or

setParagraphInsets(javax.swing.text.AttributeSet)

.

In addition to the abstract methods of

View

,
subclasses of

CompositeView

will need to
override:

- isBefore(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is before the visual space
of the

CompositeView

.

isAfter(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is after the visual space
of the

CompositeView

.

getViewAtPoint(int, int, java.awt.Rectangle)

- Returns the view at
a given visual location.

childAllocation(int, java.awt.Rectangle)

- Returns the bounds of
a particular child

View

.

getChildAllocation

will invoke

childAllocation

after offseting
the bounds by the

Inset

s of the

CompositeView

.

While

CompositeView

does not impose a layout policy on its child

View

s,
it does allow for inseting the child

View

s
it will contain. The insets can be set by either

setInsets(short, short, short, short)

or

setParagraphInsets(javax.swing.text.AttributeSet)

.

In addition to the abstract methods of

View

,
subclasses of

CompositeView

will need to
override:

- isBefore(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is before the visual space
of the

CompositeView

.

isAfter(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is after the visual space
of the

CompositeView

.

getViewAtPoint(int, int, java.awt.Rectangle)

- Returns the view at
a given visual location.

childAllocation(int, java.awt.Rectangle)

- Returns the bounds of
a particular child

View

.

getChildAllocation

will invoke

childAllocation

after offseting
the bounds by the

Inset

s of the

CompositeView

.

In addition to the abstract methods of

View

,
subclasses of

CompositeView

will need to
override:

- isBefore(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is before the visual space
of the

CompositeView

.

isAfter(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is after the visual space
of the

CompositeView

.

getViewAtPoint(int, int, java.awt.Rectangle)

- Returns the view at
a given visual location.

childAllocation(int, java.awt.Rectangle)

- Returns the bounds of
a particular child

View

.

getChildAllocation

will invoke

childAllocation

after offseting
the bounds by the

Inset

s of the

CompositeView

.

isBefore(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is before the visual space
of the

CompositeView

.

isAfter(int, int, java.awt.Rectangle)

- Used to test if a given

View

location is after the visual space
of the

CompositeView

.

getViewAtPoint(int, int, java.awt.Rectangle)

- Returns the view at
a given visual location.

childAllocation(int, java.awt.Rectangle)

- Returns the bounds of
a particular child

View

.

getChildAllocation

will invoke

childAllocation

after offseting
the bounds by the

Inset

s of the

CompositeView

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

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

CompositeView

​(

Element

elem)

Constructs a

CompositeView

for the given element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract void

childAllocation

​(int index,

Rectangle

a)

Returns the allocation for a given child.

protected boolean

flipEastAndWestAtEnds

​(int position,

Position.Bias

bias)

Determines in which direction the next view lays.

protected short

getBottomInset

()

Gets the bottom inset.

Shape

getChildAllocation

​(int index,

Shape

a)

Fetches the allocation for the given child view to
render into.

protected

Rectangle

getInsideAllocation

​(

Shape

a)

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.

protected short

getLeftInset

()

Gets the left inset.

protected int

getNextEastWestVisualPositionFrom

​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Returns the next visual position for the cursor, in either the
east or west direction.

protected int

getNextNorthSouthVisualPositionFrom

​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Returns the next visual position for the cursor, in either the
north or south direction.

int

getNextVisualPositionFrom

​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Provides a way to determine the next visually represented model
location that one might place a caret.

protected short

getRightInset

()

Gets the right inset.

protected short

getTopInset

()

Gets the top inset.

View

getView

​(int n)

Returns the n-th view in this container.

protected abstract

View

getViewAtPoint

​(int x,
int y,

Rectangle

alloc)

Fetches the child view at the given coordinates.

protected

View

getViewAtPosition

​(int pos,

Rectangle

a)

Fetches the child view that represents the given position in
the model.

int

getViewCount

()

Returns the number of child views of this view.

int

getViewIndex

​(int pos,

Position.Bias

b)

Returns the child view index representing the given
position in the model.

protected int

getViewIndexAtPosition

​(int pos)

Fetches the child view index representing the given position in
the model.

protected abstract boolean

isAfter

​(int x,
int y,

Rectangle

alloc)

Tests whether a point lies after the rectangle range.

protected abstract boolean

isBefore

​(int x,
int y,

Rectangle

alloc)

Tests whether a point lies before the rectangle range.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Shape

modelToView

​(int p0,

Position.Bias

b0,
int p1,

Position.Bias

b1,

Shape

a)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

void

replace

​(int offset,
int length,

View

[] views)

Replaces child views.

protected void

setInsets

​(short top,
short left,
short bottom,
short right)

Sets the insets for the view.

protected void

setParagraphInsets

​(

AttributeSet

attr)

Sets the insets from the paragraph attributes specified in
the given attributes.

void

setParent

​(

View

parent)

Sets the parent of the view.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAlignment

,

getAttributes

,

getBreakWeight

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getParent

,

getPreferredSpan

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getViewFactory

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

paint

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

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

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

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

Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

---

#### Fields declared in class javax.swing.text. View

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

CompositeView

​(

Element

elem)

Constructs a

CompositeView

for the given element.

---

#### Constructor Summary

Constructs a

CompositeView

for the given element.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract void

childAllocation

​(int index,

Rectangle

a)

Returns the allocation for a given child.

protected boolean

flipEastAndWestAtEnds

​(int position,

Position.Bias

bias)

Determines in which direction the next view lays.

protected short

getBottomInset

()

Gets the bottom inset.

Shape

getChildAllocation

​(int index,

Shape

a)

Fetches the allocation for the given child view to
render into.

protected

Rectangle

getInsideAllocation

​(

Shape

a)

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.

protected short

getLeftInset

()

Gets the left inset.

protected int

getNextEastWestVisualPositionFrom

​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Returns the next visual position for the cursor, in either the
east or west direction.

protected int

getNextNorthSouthVisualPositionFrom

​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Returns the next visual position for the cursor, in either the
north or south direction.

int

getNextVisualPositionFrom

​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Provides a way to determine the next visually represented model
location that one might place a caret.

protected short

getRightInset

()

Gets the right inset.

protected short

getTopInset

()

Gets the top inset.

View

getView

​(int n)

Returns the n-th view in this container.

protected abstract

View

getViewAtPoint

​(int x,
int y,

Rectangle

alloc)

Fetches the child view at the given coordinates.

protected

View

getViewAtPosition

​(int pos,

Rectangle

a)

Fetches the child view that represents the given position in
the model.

int

getViewCount

()

Returns the number of child views of this view.

int

getViewIndex

​(int pos,

Position.Bias

b)

Returns the child view index representing the given
position in the model.

protected int

getViewIndexAtPosition

​(int pos)

Fetches the child view index representing the given position in
the model.

protected abstract boolean

isAfter

​(int x,
int y,

Rectangle

alloc)

Tests whether a point lies after the rectangle range.

protected abstract boolean

isBefore

​(int x,
int y,

Rectangle

alloc)

Tests whether a point lies before the rectangle range.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Shape

modelToView

​(int p0,

Position.Bias

b0,
int p1,

Position.Bias

b1,

Shape

a)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

void

replace

​(int offset,
int length,

View

[] views)

Replaces child views.

protected void

setInsets

​(short top,
short left,
short bottom,
short right)

Sets the insets for the view.

protected void

setParagraphInsets

​(

AttributeSet

attr)

Sets the insets from the paragraph attributes specified in
the given attributes.

void

setParent

​(

View

parent)

Sets the parent of the view.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAlignment

,

getAttributes

,

getBreakWeight

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getParent

,

getPreferredSpan

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getViewFactory

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

paint

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

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

Returns the allocation for a given child.

Determines in which direction the next view lays.

Gets the bottom inset.

Fetches the allocation for the given child view to
render into.

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.

Gets the left inset.

Returns the next visual position for the cursor, in either the
east or west direction.

Returns the next visual position for the cursor, in either the
north or south direction.

Provides a way to determine the next visually represented model
location that one might place a caret.

Gets the right inset.

Gets the top inset.

Returns the n-th view in this container.

Fetches the child view at the given coordinates.

Fetches the child view that represents the given position in
the model.

Returns the number of child views of this view.

Returns the child view index representing the given
position in the model.

Fetches the child view index representing the given position in
the model.

Tests whether a point lies after the rectangle range.

Tests whether a point lies before the rectangle range.

Loads all of the children to initialize the view.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Replaces child views.

Sets the insets for the view.

Sets the insets from the paragraph attributes specified in
the given attributes.

Sets the parent of the view.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAlignment

,

getAttributes

,

getBreakWeight

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getParent

,

getPreferredSpan

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getViewFactory

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

paint

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

---

#### Methods declared in class javax.swing.text. View

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompositeView

```java
public CompositeView​(
Element
elem)
```

Constructs a

CompositeView

for the given element.

**Parameters:** elem

- the element this view is responsible for

============ METHOD DETAIL ==========

- Method Detail

- loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent(javax.swing.text.View)

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

**Parameters:** f

- the view factory
**See Also:** setParent(javax.swing.text.View)

- setParent

```java
public void setParent​(
View
parent)
```

Sets the parent of the view.
This is reimplemented to provide the superclass
behavior as well as calling the

loadChildren

method if this view does not already have children.
The children should not be loaded in the
constructor because the act of setting the parent
may cause them to try to search up the hierarchy
(to get the hosting

Container

for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the parent of the view,

null

if none

- getViewCount

```java
public int getViewCount()
```

Returns the number of child views of this view.

**Overrides:** getViewCount

in class

View
**Returns:** the number of views >= 0
**See Also:** getView(int)

- getView

```java
public
View
getView​(int n)
```

Returns the n-th view in this container.

**Overrides:** getView

in class

View
**Parameters:** n

- the number of the desired view, >= 0 && < getViewCount()
**Returns:** the view at index

n

- replace

```java
public void replace​(int offset,
int length,

View
[] views)
```

Replaces child views. If there are no views to remove
this acts as an insert. If there are no views to
add this acts as a remove. Views being removed will
have the parent set to

null

,
and the internal reference to them removed so that they
may be garbage collected.

**Overrides:** replace

in class

View
**Parameters:** offset

- the starting index into the child views to insert
the new views; >= 0 and <= getViewCount
**Parameters:** length

- the number of existing child views to remove;
this should be a value >= 0 and <= (getViewCount() - offset)
**Parameters:** views

- the child views to add; this value can be

null

to indicate no children are being added (useful to remove)

- getChildAllocation

```java
public
Shape
getChildAllocation​(int index,

Shape
a)
```

Fetches the allocation for the given child view to
render into. This enables finding out where various views
are located.

**Overrides:** getChildAllocation

in class

View
**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to this view
**Returns:** the allocation to the child

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does
not represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- modelToView

```java
public
Shape
modelToView​(int p0,

Position.Bias
b0,
int p1,

Position.Bias
b1,

Shape
a)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:** modelToView

in class

View
**Parameters:** p0

- the position to convert >= 0
**Parameters:** b0

- the bias toward the previous character or the
next character represented by p0, in case the
position is a boundary of two views; either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** p1

- the position to convert >= 0
**Parameters:** b1

- the bias toward the previous character or the
next character represented by p1, in case the
position is a boundary of two views
**Parameters:** a

- the allocated region to render into
**Returns:** the bounding box of the given position is returned
**Throws:** BadLocationException

- if the given position does
not represent a valid location in the associated document
**Throws:** IllegalArgumentException

- for an invalid bias argument
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- x coordinate of the view location to convert >= 0
**Parameters:** y

- y coordinate of the view location to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the location within the model that best represents the
given point in the view >= 0
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.
This is a convenience method for

getNextNorthSouthVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

and

getNextEastWestVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

.
This method enables specifying a position to convert
within the range of >=0. If the value is -1, a position
will be calculated automatically. If the value < -1,
the

BadLocationException

will be thrown.

**Overrides:** getNextVisualPositionFrom

in class

View
**Parameters:** pos

- the position to convert
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Throws:** IllegalArgumentException

- if

direction

is invalid

- getViewIndex

```java
public int getViewIndex​(int pos,

Position.Bias
b)
```

Returns the child view index representing the given
position in the model. This is implemented to call the

getViewIndexByPosition

method for backward compatibility.

**Overrides:** getViewIndex

in class

View
**Parameters:** pos

- the position >= 0
**Parameters:** b

- the bias
**Returns:** index of the view representing the given position, or
-1 if no view represents that position
**Since:** 1.3

- isBefore

```java
protected abstract boolean isBefore​(int x,
int y,

Rectangle
alloc)
```

Tests whether a point lies before the rectangle range.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the rectangle
**Returns:** true if the point is before the specified range

- isAfter

```java
protected abstract boolean isAfter​(int x,
int y,

Rectangle
alloc)
```

Tests whether a point lies after the rectangle range.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the rectangle
**Returns:** true if the point is after the specified range

- getViewAtPoint

```java
protected abstract
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)
```

Fetches the child view at the given coordinates.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the parent's allocation on entry, which should
be changed to the child's allocation on exit
**Returns:** the child view

- childAllocation

```java
protected abstract void childAllocation​(int index,

Rectangle
a)
```

Returns the allocation for a given child.

**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to the interior of the box on entry,
and the allocation of the child view at the index on exit.

- getViewAtPosition

```java
protected
View
getViewAtPosition​(int pos,

Rectangle
a)
```

Fetches the child view that represents the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Parameters:** a

- the allocation to the interior of the box on entry,
and the allocation of the view containing the position on exit
**Returns:** the view representing the given position, or

null

if there isn't one

- getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos)
```

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

- getInsideAllocation

```java
protected
Rectangle
getInsideAllocation​(
Shape
a)
```

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.
It is expected that the returned value would be further
mutated to represent an allocation to a child view.
This is implemented to reuse an instance variable so
it avoids creating excessive Rectangles. Typically
the result of calling this method would be fed to
the

childAllocation

method.

**Parameters:** a

- the allocation given to the view
**Returns:** the allocation that represents the inside of the
view after the margins have all been removed; if the
given allocation was

null

,
the return value is

null

- setParagraphInsets

```java
protected void setParagraphInsets​(
AttributeSet
attr)
```

Sets the insets from the paragraph attributes specified in
the given attributes.

**Parameters:** attr

- the attributes

- setInsets

```java
protected void setInsets​(short top,
short left,
short bottom,
short right)
```

Sets the insets for the view.

**Parameters:** top

- the top inset >= 0
**Parameters:** left

- the left inset >= 0
**Parameters:** bottom

- the bottom inset >= 0
**Parameters:** right

- the right inset >= 0

- getLeftInset

```java
protected short getLeftInset()
```

Gets the left inset.

**Returns:** the inset >= 0

- getRightInset

```java
protected short getRightInset()
```

Gets the right inset.

**Returns:** the inset >= 0

- getTopInset

```java
protected short getTopInset()
```

Gets the top inset.

**Returns:** the inset >= 0

- getBottomInset

```java
protected short getBottomInset()
```

Gets the bottom inset.

**Returns:** the inset >= 0

- getNextNorthSouthVisualPositionFrom

```java
protected int getNextNorthSouthVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position for the cursor, in either the
north or south direction.

**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
north or south location
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

is invalid
**See Also:** getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

- getNextEastWestVisualPositionFrom

```java
protected int getNextEastWestVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position for the cursor, in either the
east or west direction.

**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
west or east location
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

is invalid
**See Also:** getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

- flipEastAndWestAtEnds

```java
protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)
```

Determines in which direction the next view lays.
Consider the

View

at index n. Typically the

View

s are layed out from left to right,
so that the

View

to the EAST will be
at index n + 1, and the

View

to the WEST
will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true, indicating the

View

s are layed out in descending order.

This unconditionally returns false, subclasses should override this
method if there is the possibility for laying

View

s in
descending order.

**Parameters:** position

- position into the model
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** false

Constructor Detail

- CompositeView

```java
public CompositeView​(
Element
elem)
```

Constructs a

CompositeView

for the given element.

**Parameters:** elem

- the element this view is responsible for

---

#### Constructor Detail

CompositeView

```java
public CompositeView​(
Element
elem)
```

Constructs a

CompositeView

for the given element.

**Parameters:** elem

- the element this view is responsible for

---

#### CompositeView

public CompositeView​(

Element

elem)

Constructs a

CompositeView

for the given element.

Method Detail

- loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent(javax.swing.text.View)

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

**Parameters:** f

- the view factory
**See Also:** setParent(javax.swing.text.View)

- setParent

```java
public void setParent​(
View
parent)
```

Sets the parent of the view.
This is reimplemented to provide the superclass
behavior as well as calling the

loadChildren

method if this view does not already have children.
The children should not be loaded in the
constructor because the act of setting the parent
may cause them to try to search up the hierarchy
(to get the hosting

Container

for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the parent of the view,

null

if none

- getViewCount

```java
public int getViewCount()
```

Returns the number of child views of this view.

**Overrides:** getViewCount

in class

View
**Returns:** the number of views >= 0
**See Also:** getView(int)

- getView

```java
public
View
getView​(int n)
```

Returns the n-th view in this container.

**Overrides:** getView

in class

View
**Parameters:** n

- the number of the desired view, >= 0 && < getViewCount()
**Returns:** the view at index

n

- replace

```java
public void replace​(int offset,
int length,

View
[] views)
```

Replaces child views. If there are no views to remove
this acts as an insert. If there are no views to
add this acts as a remove. Views being removed will
have the parent set to

null

,
and the internal reference to them removed so that they
may be garbage collected.

**Overrides:** replace

in class

View
**Parameters:** offset

- the starting index into the child views to insert
the new views; >= 0 and <= getViewCount
**Parameters:** length

- the number of existing child views to remove;
this should be a value >= 0 and <= (getViewCount() - offset)
**Parameters:** views

- the child views to add; this value can be

null

to indicate no children are being added (useful to remove)

- getChildAllocation

```java
public
Shape
getChildAllocation​(int index,

Shape
a)
```

Fetches the allocation for the given child view to
render into. This enables finding out where various views
are located.

**Overrides:** getChildAllocation

in class

View
**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to this view
**Returns:** the allocation to the child

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does
not represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- modelToView

```java
public
Shape
modelToView​(int p0,

Position.Bias
b0,
int p1,

Position.Bias
b1,

Shape
a)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:** modelToView

in class

View
**Parameters:** p0

- the position to convert >= 0
**Parameters:** b0

- the bias toward the previous character or the
next character represented by p0, in case the
position is a boundary of two views; either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** p1

- the position to convert >= 0
**Parameters:** b1

- the bias toward the previous character or the
next character represented by p1, in case the
position is a boundary of two views
**Parameters:** a

- the allocated region to render into
**Returns:** the bounding box of the given position is returned
**Throws:** BadLocationException

- if the given position does
not represent a valid location in the associated document
**Throws:** IllegalArgumentException

- for an invalid bias argument
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- x coordinate of the view location to convert >= 0
**Parameters:** y

- y coordinate of the view location to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the location within the model that best represents the
given point in the view >= 0
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.
This is a convenience method for

getNextNorthSouthVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

and

getNextEastWestVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

.
This method enables specifying a position to convert
within the range of >=0. If the value is -1, a position
will be calculated automatically. If the value < -1,
the

BadLocationException

will be thrown.

**Overrides:** getNextVisualPositionFrom

in class

View
**Parameters:** pos

- the position to convert
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Throws:** IllegalArgumentException

- if

direction

is invalid

- getViewIndex

```java
public int getViewIndex​(int pos,

Position.Bias
b)
```

Returns the child view index representing the given
position in the model. This is implemented to call the

getViewIndexByPosition

method for backward compatibility.

**Overrides:** getViewIndex

in class

View
**Parameters:** pos

- the position >= 0
**Parameters:** b

- the bias
**Returns:** index of the view representing the given position, or
-1 if no view represents that position
**Since:** 1.3

- isBefore

```java
protected abstract boolean isBefore​(int x,
int y,

Rectangle
alloc)
```

Tests whether a point lies before the rectangle range.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the rectangle
**Returns:** true if the point is before the specified range

- isAfter

```java
protected abstract boolean isAfter​(int x,
int y,

Rectangle
alloc)
```

Tests whether a point lies after the rectangle range.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the rectangle
**Returns:** true if the point is after the specified range

- getViewAtPoint

```java
protected abstract
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)
```

Fetches the child view at the given coordinates.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the parent's allocation on entry, which should
be changed to the child's allocation on exit
**Returns:** the child view

- childAllocation

```java
protected abstract void childAllocation​(int index,

Rectangle
a)
```

Returns the allocation for a given child.

**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to the interior of the box on entry,
and the allocation of the child view at the index on exit.

- getViewAtPosition

```java
protected
View
getViewAtPosition​(int pos,

Rectangle
a)
```

Fetches the child view that represents the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Parameters:** a

- the allocation to the interior of the box on entry,
and the allocation of the view containing the position on exit
**Returns:** the view representing the given position, or

null

if there isn't one

- getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos)
```

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

- getInsideAllocation

```java
protected
Rectangle
getInsideAllocation​(
Shape
a)
```

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.
It is expected that the returned value would be further
mutated to represent an allocation to a child view.
This is implemented to reuse an instance variable so
it avoids creating excessive Rectangles. Typically
the result of calling this method would be fed to
the

childAllocation

method.

**Parameters:** a

- the allocation given to the view
**Returns:** the allocation that represents the inside of the
view after the margins have all been removed; if the
given allocation was

null

,
the return value is

null

- setParagraphInsets

```java
protected void setParagraphInsets​(
AttributeSet
attr)
```

Sets the insets from the paragraph attributes specified in
the given attributes.

**Parameters:** attr

- the attributes

- setInsets

```java
protected void setInsets​(short top,
short left,
short bottom,
short right)
```

Sets the insets for the view.

**Parameters:** top

- the top inset >= 0
**Parameters:** left

- the left inset >= 0
**Parameters:** bottom

- the bottom inset >= 0
**Parameters:** right

- the right inset >= 0

- getLeftInset

```java
protected short getLeftInset()
```

Gets the left inset.

**Returns:** the inset >= 0

- getRightInset

```java
protected short getRightInset()
```

Gets the right inset.

**Returns:** the inset >= 0

- getTopInset

```java
protected short getTopInset()
```

Gets the top inset.

**Returns:** the inset >= 0

- getBottomInset

```java
protected short getBottomInset()
```

Gets the bottom inset.

**Returns:** the inset >= 0

- getNextNorthSouthVisualPositionFrom

```java
protected int getNextNorthSouthVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position for the cursor, in either the
north or south direction.

**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
north or south location
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

is invalid
**See Also:** getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

- getNextEastWestVisualPositionFrom

```java
protected int getNextEastWestVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position for the cursor, in either the
east or west direction.

**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
west or east location
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

is invalid
**See Also:** getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

- flipEastAndWestAtEnds

```java
protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)
```

Determines in which direction the next view lays.
Consider the

View

at index n. Typically the

View

s are layed out from left to right,
so that the

View

to the EAST will be
at index n + 1, and the

View

to the WEST
will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true, indicating the

View

s are layed out in descending order.

This unconditionally returns false, subclasses should override this
method if there is the possibility for laying

View

s in
descending order.

**Parameters:** position

- position into the model
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** false

---

#### Method Detail

loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent(javax.swing.text.View)

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

**Parameters:** f

- the view factory
**See Also:** setParent(javax.swing.text.View)

---

#### loadChildren

protected void loadChildren​(

ViewFactory

f)

Loads all of the children to initialize the view.
This is called by the

setParent(javax.swing.text.View)

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

setParent

```java
public void setParent​(
View
parent)
```

Sets the parent of the view.
This is reimplemented to provide the superclass
behavior as well as calling the

loadChildren

method if this view does not already have children.
The children should not be loaded in the
constructor because the act of setting the parent
may cause them to try to search up the hierarchy
(to get the hosting

Container

for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the parent of the view,

null

if none

---

#### setParent

public void setParent​(

View

parent)

Sets the parent of the view.
This is reimplemented to provide the superclass
behavior as well as calling the

loadChildren

method if this view does not already have children.
The children should not be loaded in the
constructor because the act of setting the parent
may cause them to try to search up the hierarchy
(to get the hosting

Container

for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

getViewCount

```java
public int getViewCount()
```

Returns the number of child views of this view.

**Overrides:** getViewCount

in class

View
**Returns:** the number of views >= 0
**See Also:** getView(int)

---

#### getViewCount

public int getViewCount()

Returns the number of child views of this view.

getView

```java
public
View
getView​(int n)
```

Returns the n-th view in this container.

**Overrides:** getView

in class

View
**Parameters:** n

- the number of the desired view, >= 0 && < getViewCount()
**Returns:** the view at index

n

---

#### getView

public

View

getView​(int n)

Returns the n-th view in this container.

replace

```java
public void replace​(int offset,
int length,

View
[] views)
```

Replaces child views. If there are no views to remove
this acts as an insert. If there are no views to
add this acts as a remove. Views being removed will
have the parent set to

null

,
and the internal reference to them removed so that they
may be garbage collected.

**Overrides:** replace

in class

View
**Parameters:** offset

- the starting index into the child views to insert
the new views; >= 0 and <= getViewCount
**Parameters:** length

- the number of existing child views to remove;
this should be a value >= 0 and <= (getViewCount() - offset)
**Parameters:** views

- the child views to add; this value can be

null

to indicate no children are being added (useful to remove)

---

#### replace

public void replace​(int offset,
int length,

View

[] views)

Replaces child views. If there are no views to remove
this acts as an insert. If there are no views to
add this acts as a remove. Views being removed will
have the parent set to

null

,
and the internal reference to them removed so that they
may be garbage collected.

getChildAllocation

```java
public
Shape
getChildAllocation​(int index,

Shape
a)
```

Fetches the allocation for the given child view to
render into. This enables finding out where various views
are located.

**Overrides:** getChildAllocation

in class

View
**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to this view
**Returns:** the allocation to the child

---

#### getChildAllocation

public

Shape

getChildAllocation​(int index,

Shape

a)

Fetches the allocation for the given child view to
render into. This enables finding out where various views
are located.

modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does
not represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### modelToView

public

Shape

modelToView​(int pos,

Shape

a,

Position.Bias

b)
throws

BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

modelToView

```java
public
Shape
modelToView​(int p0,

Position.Bias
b0,
int p1,

Position.Bias
b1,

Shape
a)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:** modelToView

in class

View
**Parameters:** p0

- the position to convert >= 0
**Parameters:** b0

- the bias toward the previous character or the
next character represented by p0, in case the
position is a boundary of two views; either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** p1

- the position to convert >= 0
**Parameters:** b1

- the bias toward the previous character or the
next character represented by p1, in case the
position is a boundary of two views
**Parameters:** a

- the allocated region to render into
**Returns:** the bounding box of the given position is returned
**Throws:** BadLocationException

- if the given position does
not represent a valid location in the associated document
**Throws:** IllegalArgumentException

- for an invalid bias argument
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### modelToView

public

Shape

modelToView​(int p0,

Position.Bias

b0,
int p1,

Position.Bias

b1,

Shape

a)
throws

BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- x coordinate of the view location to convert >= 0
**Parameters:** y

- y coordinate of the view location to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the location within the model that best represents the
given point in the view >= 0
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### viewToModel

public int viewToModel​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.
This is a convenience method for

getNextNorthSouthVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

and

getNextEastWestVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

.
This method enables specifying a position to convert
within the range of >=0. If the value is -1, a position
will be calculated automatically. If the value < -1,
the

BadLocationException

will be thrown.

**Overrides:** getNextVisualPositionFrom

in class

View
**Parameters:** pos

- the position to convert
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Throws:** IllegalArgumentException

- if

direction

is invalid

---

#### getNextVisualPositionFrom

public int getNextVisualPositionFrom​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)
throws

BadLocationException

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.
This is a convenience method for

getNextNorthSouthVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

and

getNextEastWestVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

.
This method enables specifying a position to convert
within the range of >=0. If the value is -1, a position
will be calculated automatically. If the value < -1,
the

BadLocationException

will be thrown.

SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH

getViewIndex

```java
public int getViewIndex​(int pos,

Position.Bias
b)
```

Returns the child view index representing the given
position in the model. This is implemented to call the

getViewIndexByPosition

method for backward compatibility.

**Overrides:** getViewIndex

in class

View
**Parameters:** pos

- the position >= 0
**Parameters:** b

- the bias
**Returns:** index of the view representing the given position, or
-1 if no view represents that position
**Since:** 1.3

---

#### getViewIndex

public int getViewIndex​(int pos,

Position.Bias

b)

Returns the child view index representing the given
position in the model. This is implemented to call the

getViewIndexByPosition

method for backward compatibility.

isBefore

```java
protected abstract boolean isBefore​(int x,
int y,

Rectangle
alloc)
```

Tests whether a point lies before the rectangle range.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the rectangle
**Returns:** true if the point is before the specified range

---

#### isBefore

protected abstract boolean isBefore​(int x,
int y,

Rectangle

alloc)

Tests whether a point lies before the rectangle range.

isAfter

```java
protected abstract boolean isAfter​(int x,
int y,

Rectangle
alloc)
```

Tests whether a point lies after the rectangle range.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the rectangle
**Returns:** true if the point is after the specified range

---

#### isAfter

protected abstract boolean isAfter​(int x,
int y,

Rectangle

alloc)

Tests whether a point lies after the rectangle range.

getViewAtPoint

```java
protected abstract
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)
```

Fetches the child view at the given coordinates.

**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the parent's allocation on entry, which should
be changed to the child's allocation on exit
**Returns:** the child view

---

#### getViewAtPoint

protected abstract

View

getViewAtPoint​(int x,
int y,

Rectangle

alloc)

Fetches the child view at the given coordinates.

childAllocation

```java
protected abstract void childAllocation​(int index,

Rectangle
a)
```

Returns the allocation for a given child.

**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to the interior of the box on entry,
and the allocation of the child view at the index on exit.

---

#### childAllocation

protected abstract void childAllocation​(int index,

Rectangle

a)

Returns the allocation for a given child.

getViewAtPosition

```java
protected
View
getViewAtPosition​(int pos,

Rectangle
a)
```

Fetches the child view that represents the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Parameters:** a

- the allocation to the interior of the box on entry,
and the allocation of the view containing the position on exit
**Returns:** the view representing the given position, or

null

if there isn't one

---

#### getViewAtPosition

protected

View

getViewAtPosition​(int pos,

Rectangle

a)

Fetches the child view that represents the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos)
```

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

---

#### getViewIndexAtPosition

protected int getViewIndexAtPosition​(int pos)

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

getInsideAllocation

```java
protected
Rectangle
getInsideAllocation​(
Shape
a)
```

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.
It is expected that the returned value would be further
mutated to represent an allocation to a child view.
This is implemented to reuse an instance variable so
it avoids creating excessive Rectangles. Typically
the result of calling this method would be fed to
the

childAllocation

method.

**Parameters:** a

- the allocation given to the view
**Returns:** the allocation that represents the inside of the
view after the margins have all been removed; if the
given allocation was

null

,
the return value is

null

---

#### getInsideAllocation

protected

Rectangle

getInsideAllocation​(

Shape

a)

Translates the immutable allocation given to the view
to a mutable allocation that represents the interior
allocation (i.e. the bounds of the given allocation
with the top, left, bottom, and right insets removed.
It is expected that the returned value would be further
mutated to represent an allocation to a child view.
This is implemented to reuse an instance variable so
it avoids creating excessive Rectangles. Typically
the result of calling this method would be fed to
the

childAllocation

method.

setParagraphInsets

```java
protected void setParagraphInsets​(
AttributeSet
attr)
```

Sets the insets from the paragraph attributes specified in
the given attributes.

**Parameters:** attr

- the attributes

---

#### setParagraphInsets

protected void setParagraphInsets​(

AttributeSet

attr)

Sets the insets from the paragraph attributes specified in
the given attributes.

setInsets

```java
protected void setInsets​(short top,
short left,
short bottom,
short right)
```

Sets the insets for the view.

**Parameters:** top

- the top inset >= 0
**Parameters:** left

- the left inset >= 0
**Parameters:** bottom

- the bottom inset >= 0
**Parameters:** right

- the right inset >= 0

---

#### setInsets

protected void setInsets​(short top,
short left,
short bottom,
short right)

Sets the insets for the view.

getLeftInset

```java
protected short getLeftInset()
```

Gets the left inset.

**Returns:** the inset >= 0

---

#### getLeftInset

protected short getLeftInset()

Gets the left inset.

getRightInset

```java
protected short getRightInset()
```

Gets the right inset.

**Returns:** the inset >= 0

---

#### getRightInset

protected short getRightInset()

Gets the right inset.

getTopInset

```java
protected short getTopInset()
```

Gets the top inset.

**Returns:** the inset >= 0

---

#### getTopInset

protected short getTopInset()

Gets the top inset.

getBottomInset

```java
protected short getBottomInset()
```

Gets the bottom inset.

**Returns:** the inset >= 0

---

#### getBottomInset

protected short getBottomInset()

Gets the bottom inset.

getNextNorthSouthVisualPositionFrom

```java
protected int getNextNorthSouthVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position for the cursor, in either the
north or south direction.

**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
north or south location
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

is invalid
**See Also:** getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

---

#### getNextNorthSouthVisualPositionFrom

protected int getNextNorthSouthVisualPositionFrom​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)
throws

BadLocationException

Returns the next visual position for the cursor, in either the
north or south direction.

SwingConstants.NORTH

SwingConstants.SOUTH

getNextEastWestVisualPositionFrom

```java
protected int getNextEastWestVisualPositionFrom​(int pos,

Position.Bias
b,

Shape
a,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position for the cursor, in either the
east or west direction.

**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- a bias value of either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST

SwingConstants.EAST
**Parameters:** biasRet

- an array containing the bias that was checked
**Returns:** the location within the model that best represents the next
west or east location
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

is invalid
**See Also:** getNextVisualPositionFrom(int, javax.swing.text.Position.Bias, java.awt.Shape, int, javax.swing.text.Position.Bias[])

---

#### getNextEastWestVisualPositionFrom

protected int getNextEastWestVisualPositionFrom​(int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)
throws

BadLocationException

Returns the next visual position for the cursor, in either the
east or west direction.

SwingConstants.WEST

SwingConstants.EAST

flipEastAndWestAtEnds

```java
protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)
```

Determines in which direction the next view lays.
Consider the

View

at index n. Typically the

View

s are layed out from left to right,
so that the

View

to the EAST will be
at index n + 1, and the

View

to the WEST
will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true, indicating the

View

s are layed out in descending order.

This unconditionally returns false, subclasses should override this
method if there is the possibility for laying

View

s in
descending order.

**Parameters:** position

- position into the model
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** false

---

#### flipEastAndWestAtEnds

protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias

bias)

Determines in which direction the next view lays.
Consider the

View

at index n. Typically the

View

s are layed out from left to right,
so that the

View

to the EAST will be
at index n + 1, and the

View

to the WEST
will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true, indicating the

View

s are layed out in descending order.

This unconditionally returns false, subclasses should override this
method if there is the possibility for laying

View

s in
descending order.

This unconditionally returns false, subclasses should override this
method if there is the possibility for laying

View

s in
descending order.

---

