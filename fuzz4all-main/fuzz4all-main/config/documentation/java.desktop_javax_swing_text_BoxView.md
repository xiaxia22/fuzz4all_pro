# Class BoxView

**Source:** `java.desktop\javax\swing\text\BoxView.html`

### Class Description

```java
public class
BoxView

extends
CompositeView
```

A view that arranges its children into a box shape by tiling
its children along an axis. The box is somewhat like that
found in TeX where there is alignment of the
children, flexibility of the children is considered, etc.
This is a building block that might be useful to represent
things like a collection of lines, paragraphs,
lists, columns, pages, etc. The axis along which the children are tiled is
considered the major axis. The orthogonal axis is the minor axis.

Layout for each axis is handled separately by the methods

layoutMajorAxis

and

layoutMinorAxis

.
Subclasses can change the layout algorithm by
reimplementing these methods. These methods will be called
as necessary depending upon whether or not there is cached
layout information and the cache is considered
valid. These methods are typically called if the given size
along the axis changes, or if

layoutChanged

is
called to force an updated layout. The

layoutChanged

method invalidates cached layout information, if there is any.
The requirements published to the parent view are calculated by
the methods

calculateMajorAxisRequirements

and

calculateMinorAxisRequirements

.
If the layout algorithm is changed, these methods will
likely need to be reimplemented.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public BoxView​(
Element
elem,
int axis)

Constructs a

BoxView

.

**Parameters:**
- elem

- the element this view is responsible for
- axis

- either

View.X_AXIS

or

View.Y_AXIS

---

### Method Details

#### public int getAxis()

Fetches the tile axis property. This is the axis along which
the child views are tiled.

**Returns:**
- the major axis of the box, either

View.X_AXIS

or

View.Y_AXIS

**Since:**
- 1.3

---

#### public void setAxis​(int axis)

Sets the tile axis property. This is the axis along which
the child views are tiled.

**Parameters:**
- axis

- either

View.X_AXIS

or

View.Y_AXIS

**Since:**
- 1.3

---

#### public void layoutChanged​(int axis)

Invalidates the layout along an axis. This happens
automatically if the preferences have changed for
any of the child views. In some cases the layout
may need to be recalculated when the preferences
have not changed. The layout can be marked as
invalid by calling this method. The layout will
be updated the next time the

setSize

method
is called on this view (typically in paint).

**Parameters:**
- axis

- either

View.X_AXIS

or

View.Y_AXIS

**Since:**
- 1.3

---

#### protected boolean isLayoutValid​(int axis)

Determines if the layout is valid along the given axis.

**Parameters:**
- axis

- either

View.X_AXIS

or

View.Y_AXIS

**Returns:**
- if the layout is valid along the given axis

**Since:**
- 1.4

---

#### protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)

Paints a child. By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Parameters:**
- g

- the graphics context
- alloc

- the allocated region to paint into
- index

- the child index, >= 0 && < getViewCount()

---

#### public void replace​(int index,
int length,

View
[] elems)

Invalidates the layout and resizes the cache of
requests/allocations. The child allocations can still
be accessed for the old layout, but the new children
will have an offset and span of 0.

**Overrides:**
- replace

in class

CompositeView

**Parameters:**
- index

- the starting index into the child views to insert
the new views; this should be a value >= 0 and <= getViewCount
- length

- the number of existing child views to remove;
This should be a value >= 0 and <= (getViewCount() - offset)
- elems

- the child views to add; this value can be

null

to indicate no children are being added
(useful to remove)

---

#### protected void forwardUpdate​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a,

ViewFactory
f)

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.
If a child changed its requirements and the allocation
was valid prior to forwarding the portion of the box
from the starting child to the end of the box will
be repainted.

**Overrides:**
- forwardUpdate

in class

View

**Parameters:**
- ec

- changes to the element this view is responsible
for (may be

null

if there were no changes)
- e

- the change information from the associated document
- a

- the current allocation of the view
- f

- the factory to use to rebuild if the view has children

**See Also:**
- View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

**Since:**
- 1.3

---

#### public void preferenceChanged​(
View
child,
boolean width,
boolean height)

This is called by a child to indicate its
preferred span has changed. This is implemented to
throw away cached layout information so that new
calculations will be done the next time the children
need an allocation.

**Overrides:**
- preferenceChanged

in class

View

**Parameters:**
- child

- the child view
- width

- true if the width preference should change
- height

- true if the height preference should change

**See Also:**
- JComponent.revalidate()

---

#### public int getResizeWeight​(int axis)

Gets the resize weight. A value of 0 or less is not resizable.

**Overrides:**
- getResizeWeight

in class

View

**Parameters:**
- axis

- may be either

View.X_AXIS

or

View.Y_AXIS

**Returns:**
- the weight

**Throws:**
- IllegalArgumentException

- for an invalid axis

---

#### public void setSize​(float width,
float height)

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information. This is implemented to call the
layout method with the sizes inside of the insets.

**Overrides:**
- setSize

in class

View

**Parameters:**
- width

- the width >= 0
- height

- the height >= 0

---

#### public void paint​(
Graphics
g,

Shape
allocation)

Renders the

BoxView

using the given
rendering surface and area
on that surface. Only the children that intersect
the clip bounds of the given

Graphics

will be rendered.

**Specified by:**
- paint

in class

View

**Parameters:**
- g

- the rendering surface to use
- allocation

- the allocated region to render into

**See Also:**
- View.paint(java.awt.Graphics, java.awt.Shape)

---

#### public
Shape
getChildAllocation​(int index,

Shape
a)

Fetches the allocation for the given child view.
This enables finding out where various views
are located. This is implemented to return

null

if the layout is invalid,
otherwise the superclass behavior is executed.

**Overrides:**
- getChildAllocation

in class

CompositeView

**Parameters:**
- index

- the index of the child, >= 0 && > getViewCount()
- a

- the allocation to this view

**Returns:**
- the allocation to the child; or

null

if

a

is

null

;
or

null

if the layout is invalid

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
to the coordinate space of the view mapped to it. This makes
sure the allocation is valid before calling the superclass.

**Overrides:**
- modelToView

in class

CompositeView

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

#### public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:**
- viewToModel

in class

CompositeView

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

#### public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the total alignment
needed to position the children with the alignment points
lined up along the axis orthogonal to the axis that is
being tiled. The axis being tiled will request to be
centered (i.e. 0.5f).

**Overrides:**
- getAlignment

in class

View

**Parameters:**
- axis

- may be either

View.X_AXIS

or

View.Y_AXIS

**Returns:**
- the desired alignment >= 0.0f && <= 1.0f; this should
be a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view

**Throws:**
- IllegalArgumentException

- for an invalid axis

---

#### public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

**Specified by:**
- getPreferredSpan

in class

View

**Parameters:**
- axis

- may be either

View.X_AXIS

or

View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view

**Throws:**
- IllegalArgumentException

- for an invalid axis type

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an
axis.

**Overrides:**
- getMinimumSpan

in class

View

**Parameters:**
- axis

- may be either

View.X_AXIS

or

View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view

**Throws:**
- IllegalArgumentException

- for an invalid axis type

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis.

**Overrides:**
- getMaximumSpan

in class

View

**Parameters:**
- axis

- may be either

View.X_AXIS

or

View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view

**Throws:**
- IllegalArgumentException

- for an invalid axis type

**See Also:**
- View.getPreferredSpan(int)

---

#### protected boolean isAllocationValid()

Are the allocations for the children still
valid?

**Returns:**
- true if allocations still valid

---

#### protected boolean isBefore​(int x,
int y,

Rectangle
innerAlloc)

Determines if a point falls before an allocated region.

**Specified by:**
- isBefore

in class

CompositeView

**Parameters:**
- x

- the X coordinate >= 0
- y

- the Y coordinate >= 0
- innerAlloc

- the allocated region; this is the area
inside of the insets

**Returns:**
- true if the point lies before the region else false

---

#### protected boolean isAfter​(int x,
int y,

Rectangle
innerAlloc)

Determines if a point falls after an allocated region.

**Specified by:**
- isAfter

in class

CompositeView

**Parameters:**
- x

- the X coordinate >= 0
- y

- the Y coordinate >= 0
- innerAlloc

- the allocated region; this is the area
inside of the insets

**Returns:**
- true if the point lies after the region else false

---

#### protected
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)

Fetches the child view at the given coordinates.

**Specified by:**
- getViewAtPoint

in class

CompositeView

**Parameters:**
- x

- the X coordinate >= 0
- y

- the Y coordinate >= 0
- alloc

- the parents inner allocation on entry, which should
be changed to the child's allocation on exit

**Returns:**
- the view

---

#### protected void childAllocation​(int index,

Rectangle
alloc)

Allocates a region for a child view.

**Specified by:**
- childAllocation

in class

CompositeView

**Parameters:**
- index

- the index of the child view to
allocate, >= 0 && < getViewCount()
- alloc

- the allocated region

---

#### protected void layout​(int width,
int height)

Perform layout on the box

**Parameters:**
- width

- the width (inside of the insets) >= 0
- height

- the height (inside of the insets) >= 0

---

#### public int getWidth()

Returns the current width of the box. This is the width that
it was last allocated.

**Returns:**
- the current width of the box

---

#### public int getHeight()

Returns the current height of the box. This is the height that
it was last allocated.

**Returns:**
- the current height of the box

---

#### protected void layoutMajorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the major axis of the box (i.e. the
axis that it represents). The results of the layout (the
offset and span for each children) are placed in the given
arrays which represent the allocations to the children
along the major axis.

**Parameters:**
- targetSpan

- the total span given to the view, which
would be used to layout the children
- axis

- the axis being layed out
- offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
- spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

---

#### protected void layoutMinorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents). The results
of the layout (the offset and span for each children) are
placed in the given arrays which represent the allocations to
the children along the minor axis.

**Parameters:**
- targetSpan

- the total span given to the view, which
would be used to layout the children
- axis

- the axis being layed out
- offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
- spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

---

#### protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)

Calculates the size requirements for the major axis

axis

.

**Parameters:**
- axis

- the axis being studied
- r

- the

SizeRequirements

object;
if

null

one will be created

**Returns:**
- the newly initialized

SizeRequirements

object

**See Also:**
- SizeRequirements

---

#### protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)

Calculates the size requirements for the minor axis

axis

.

**Parameters:**
- axis

- the axis being studied
- r

- the

SizeRequirements

object;
if

null

one will be created

**Returns:**
- the newly initialized

SizeRequirements

object

**See Also:**
- SizeRequirements

---

#### protected void baselineLayout​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

**Parameters:**
- targetSpan

- the total span given to the view, which
would be used to layout the children
- axis

- the axis being studied, either

View.X_AXIS

or

View.Y_AXIS
- offsets

- an empty array filled by this method with
values specifying the location of each child view
- spans

- an empty array filled by this method with
values specifying the extent of each child view

---

#### protected
SizeRequirements
baselineRequirements​(int axis,

SizeRequirements
r)

Calculates the size requirements for this

BoxView

by examining the size of each child view.

**Parameters:**
- axis

- the axis being studied
- r

- the

SizeRequirements

object;
if

null

one will be created

**Returns:**
- the newly initialized

SizeRequirements

object

---

#### protected int getOffset​(int axis,
int childIndex)

Fetches the offset of a particular child's current layout.

**Parameters:**
- axis

- the axis being studied
- childIndex

- the index of the requested child

**Returns:**
- the offset (location) for the specified child

---

#### protected int getSpan​(int axis,
int childIndex)

Fetches the span of a particular child's current layout.

**Parameters:**
- axis

- the axis being studied
- childIndex

- the index of the requested child

**Returns:**
- the span (width or height) of the specified child

---

#### protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)

Determines in which direction the next view lays.
Consider the View at index n. Typically the

View

s
are layed out from left to right, so that the

View

to the EAST will be at index n + 1, and the

View

to the WEST will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true,
indicating the

View

s are layed out in
descending order. Otherwise the method would return false
indicating the

View

s are layed out in ascending order.

If the receiver is laying its

View

s along the

Y_AXIS

, this will return the value from
invoking the same method on the

View

responsible for rendering

position

and

bias

. Otherwise this will return false.

**Overrides:**
- flipEastAndWestAtEnds

in class

CompositeView

**Parameters:**
- position

- position into the model
- bias

- either

Position.Bias.Forward

or

Position.Bias.Backward

**Returns:**
- true if the

View

s surrounding the

View

responding for rendering

position

and

bias

are layed out in descending order; otherwise false

---

### Additional Sections

#### Class BoxView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.CompositeView
- - javax.swing.text.BoxView

javax.swing.text.View

- javax.swing.text.CompositeView
- - javax.swing.text.BoxView

javax.swing.text.CompositeView

- javax.swing.text.BoxView

javax.swing.text.BoxView

**All Implemented Interfaces:** SwingConstants

**Direct Known Subclasses:** BlockView

,

FlowView

,

TableView

,

TableView.TableCell

,

TableView.TableRow

,

WrappedPlainView

,

ZoneView

```java
public class
BoxView

extends
CompositeView
```

A view that arranges its children into a box shape by tiling
its children along an axis. The box is somewhat like that
found in TeX where there is alignment of the
children, flexibility of the children is considered, etc.
This is a building block that might be useful to represent
things like a collection of lines, paragraphs,
lists, columns, pages, etc. The axis along which the children are tiled is
considered the major axis. The orthogonal axis is the minor axis.

Layout for each axis is handled separately by the methods

layoutMajorAxis

and

layoutMinorAxis

.
Subclasses can change the layout algorithm by
reimplementing these methods. These methods will be called
as necessary depending upon whether or not there is cached
layout information and the cache is considered
valid. These methods are typically called if the given size
along the axis changes, or if

layoutChanged

is
called to force an updated layout. The

layoutChanged

method invalidates cached layout information, if there is any.
The requirements published to the parent view are calculated by
the methods

calculateMajorAxisRequirements

and

calculateMinorAxisRequirements

.
If the layout algorithm is changed, these methods will
likely need to be reimplemented.

public class

BoxView

extends

CompositeView

A view that arranges its children into a box shape by tiling
its children along an axis. The box is somewhat like that
found in TeX where there is alignment of the
children, flexibility of the children is considered, etc.
This is a building block that might be useful to represent
things like a collection of lines, paragraphs,
lists, columns, pages, etc. The axis along which the children are tiled is
considered the major axis. The orthogonal axis is the minor axis.

Layout for each axis is handled separately by the methods

layoutMajorAxis

and

layoutMinorAxis

.
Subclasses can change the layout algorithm by
reimplementing these methods. These methods will be called
as necessary depending upon whether or not there is cached
layout information and the cache is considered
valid. These methods are typically called if the given size
along the axis changes, or if

layoutChanged

is
called to force an updated layout. The

layoutChanged

method invalidates cached layout information, if there is any.
The requirements published to the parent view are calculated by
the methods

calculateMajorAxisRequirements

and

calculateMinorAxisRequirements

.
If the layout algorithm is changed, these methods will
likely need to be reimplemented.

Layout for each axis is handled separately by the methods

layoutMajorAxis

and

layoutMinorAxis

.
Subclasses can change the layout algorithm by
reimplementing these methods. These methods will be called
as necessary depending upon whether or not there is cached
layout information and the cache is considered
valid. These methods are typically called if the given size
along the axis changes, or if

layoutChanged

is
called to force an updated layout. The

layoutChanged

method invalidates cached layout information, if there is any.
The requirements published to the parent view are calculated by
the methods

calculateMajorAxisRequirements

and

calculateMinorAxisRequirements

.
If the layout algorithm is changed, these methods will
likely need to be reimplemented.

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

BoxView

​(

Element

elem,
int axis)

Constructs a

BoxView

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

baselineLayout

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

protected

SizeRequirements

baselineRequirements

​(int axis,

SizeRequirements

r)

Calculates the size requirements for this

BoxView

by examining the size of each child view.

protected

SizeRequirements

calculateMajorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculates the size requirements for the major axis

axis

.

protected

SizeRequirements

calculateMinorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculates the size requirements for the minor axis

axis

.

protected void

childAllocation

​(int index,

Rectangle

alloc)

Allocates a region for a child view.

protected boolean

flipEastAndWestAtEnds

​(int position,

Position.Bias

bias)

Determines in which direction the next view lays.

protected void

forwardUpdate

​(

DocumentEvent.ElementChange

ec,

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

int

getAxis

()

Fetches the tile axis property.

Shape

getChildAllocation

​(int index,

Shape

a)

Fetches the allocation for the given child view.

int

getHeight

()

Returns the current height of the box.

float

getMaximumSpan

​(int axis)

Determines the maximum span for this view along an
axis.

float

getMinimumSpan

​(int axis)

Determines the minimum span for this view along an
axis.

protected int

getOffset

​(int axis,
int childIndex)

Fetches the offset of a particular child's current layout.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getResizeWeight

​(int axis)

Gets the resize weight.

protected int

getSpan

​(int axis,
int childIndex)

Fetches the span of a particular child's current layout.

protected

View

getViewAtPoint

​(int x,
int y,

Rectangle

alloc)

Fetches the child view at the given coordinates.

int

getWidth

()

Returns the current width of the box.

protected boolean

isAfter

​(int x,
int y,

Rectangle

innerAlloc)

Determines if a point falls after an allocated region.

protected boolean

isAllocationValid

()

Are the allocations for the children still
valid?

protected boolean

isBefore

​(int x,
int y,

Rectangle

innerAlloc)

Determines if a point falls before an allocated region.

protected boolean

isLayoutValid

​(int axis)

Determines if the layout is valid along the given axis.

protected void

layout

​(int width,
int height)

Perform layout on the box

void

layoutChanged

​(int axis)

Invalidates the layout along an axis.

protected void

layoutMajorAxis

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the major axis of the box (i.e. the
axis that it represents).

protected void

layoutMinorAxis

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents).

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

void

paint

​(

Graphics

g,

Shape

allocation)

Renders the

BoxView

using the given
rendering surface and area
on that surface.

protected void

paintChild

​(

Graphics

g,

Rectangle

alloc,
int index)

Paints a child.

void

preferenceChanged

​(

View

child,
boolean width,
boolean height)

This is called by a child to indicate its
preferred span has changed.

void

replace

​(int index,
int length,

View

[] elems)

Invalidates the layout and resizes the cache of
requests/allocations.

void

setAxis

​(int axis)

Sets the tile axis property.

void

setSize

​(float width,
float height)

Sets the size of the view.

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

CompositeView

getBottomInset

,

getInsideAllocation

,

getLeftInset

,

getNextEastWestVisualPositionFrom

,

getNextNorthSouthVisualPositionFrom

,

getNextVisualPositionFrom

,

getRightInset

,

getTopInset

,

getView

,

getViewAtPosition

,

getViewCount

,

getViewIndex

,

getViewIndexAtPosition

,

loadChildren

,

modelToView

,

setInsets

,

setParagraphInsets

,

setParent

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

forwardUpdateToView

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

getParent

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

remove

,

removeAll

,

removeUpdate

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

BoxView

​(

Element

elem,
int axis)

Constructs a

BoxView

.

---

#### Constructor Summary

Constructs a

BoxView

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

baselineLayout

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

protected

SizeRequirements

baselineRequirements

​(int axis,

SizeRequirements

r)

Calculates the size requirements for this

BoxView

by examining the size of each child view.

protected

SizeRequirements

calculateMajorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculates the size requirements for the major axis

axis

.

protected

SizeRequirements

calculateMinorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculates the size requirements for the minor axis

axis

.

protected void

childAllocation

​(int index,

Rectangle

alloc)

Allocates a region for a child view.

protected boolean

flipEastAndWestAtEnds

​(int position,

Position.Bias

bias)

Determines in which direction the next view lays.

protected void

forwardUpdate

​(

DocumentEvent.ElementChange

ec,

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

int

getAxis

()

Fetches the tile axis property.

Shape

getChildAllocation

​(int index,

Shape

a)

Fetches the allocation for the given child view.

int

getHeight

()

Returns the current height of the box.

float

getMaximumSpan

​(int axis)

Determines the maximum span for this view along an
axis.

float

getMinimumSpan

​(int axis)

Determines the minimum span for this view along an
axis.

protected int

getOffset

​(int axis,
int childIndex)

Fetches the offset of a particular child's current layout.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getResizeWeight

​(int axis)

Gets the resize weight.

protected int

getSpan

​(int axis,
int childIndex)

Fetches the span of a particular child's current layout.

protected

View

getViewAtPoint

​(int x,
int y,

Rectangle

alloc)

Fetches the child view at the given coordinates.

int

getWidth

()

Returns the current width of the box.

protected boolean

isAfter

​(int x,
int y,

Rectangle

innerAlloc)

Determines if a point falls after an allocated region.

protected boolean

isAllocationValid

()

Are the allocations for the children still
valid?

protected boolean

isBefore

​(int x,
int y,

Rectangle

innerAlloc)

Determines if a point falls before an allocated region.

protected boolean

isLayoutValid

​(int axis)

Determines if the layout is valid along the given axis.

protected void

layout

​(int width,
int height)

Perform layout on the box

void

layoutChanged

​(int axis)

Invalidates the layout along an axis.

protected void

layoutMajorAxis

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the major axis of the box (i.e. the
axis that it represents).

protected void

layoutMinorAxis

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents).

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

void

paint

​(

Graphics

g,

Shape

allocation)

Renders the

BoxView

using the given
rendering surface and area
on that surface.

protected void

paintChild

​(

Graphics

g,

Rectangle

alloc,
int index)

Paints a child.

void

preferenceChanged

​(

View

child,
boolean width,
boolean height)

This is called by a child to indicate its
preferred span has changed.

void

replace

​(int index,
int length,

View

[] elems)

Invalidates the layout and resizes the cache of
requests/allocations.

void

setAxis

​(int axis)

Sets the tile axis property.

void

setSize

​(float width,
float height)

Sets the size of the view.

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

CompositeView

getBottomInset

,

getInsideAllocation

,

getLeftInset

,

getNextEastWestVisualPositionFrom

,

getNextNorthSouthVisualPositionFrom

,

getNextVisualPositionFrom

,

getRightInset

,

getTopInset

,

getView

,

getViewAtPosition

,

getViewCount

,

getViewIndex

,

getViewIndexAtPosition

,

loadChildren

,

modelToView

,

setInsets

,

setParagraphInsets

,

setParent

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

forwardUpdateToView

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

getParent

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

remove

,

removeAll

,

removeUpdate

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

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

Calculates the size requirements for this

BoxView

by examining the size of each child view.

Calculates the size requirements for the major axis

axis

.

Calculates the size requirements for the minor axis

axis

.

Allocates a region for a child view.

Determines in which direction the next view lays.

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.

Determines the desired alignment for this view along an
axis.

Fetches the tile axis property.

Fetches the allocation for the given child view.

Returns the current height of the box.

Determines the maximum span for this view along an
axis.

Determines the minimum span for this view along an
axis.

Fetches the offset of a particular child's current layout.

Determines the preferred span for this view along an
axis.

Gets the resize weight.

Fetches the span of a particular child's current layout.

Fetches the child view at the given coordinates.

Returns the current width of the box.

Determines if a point falls after an allocated region.

Are the allocations for the children still
valid?

Determines if a point falls before an allocated region.

Determines if the layout is valid along the given axis.

Perform layout on the box

Invalidates the layout along an axis.

Performs layout for the major axis of the box (i.e. the
axis that it represents).

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents).

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Renders the

BoxView

using the given
rendering surface and area
on that surface.

Paints a child.

This is called by a child to indicate its
preferred span has changed.

Invalidates the layout and resizes the cache of
requests/allocations.

Sets the tile axis property.

Sets the size of the view.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.text.

CompositeView

getBottomInset

,

getInsideAllocation

,

getLeftInset

,

getNextEastWestVisualPositionFrom

,

getNextNorthSouthVisualPositionFrom

,

getNextVisualPositionFrom

,

getRightInset

,

getTopInset

,

getView

,

getViewAtPosition

,

getViewCount

,

getViewIndex

,

getViewIndexAtPosition

,

loadChildren

,

modelToView

,

setInsets

,

setParagraphInsets

,

setParent

---

#### Methods declared in class javax.swing.text. CompositeView

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

forwardUpdateToView

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

getParent

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

remove

,

removeAll

,

removeUpdate

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

- BoxView

```java
public BoxView​(
Element
elem,
int axis)
```

Constructs a

BoxView

.

**Parameters:** elem

- the element this view is responsible for
**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS

============ METHOD DETAIL ==========

- Method Detail

- getAxis

```java
public int getAxis()
```

Fetches the tile axis property. This is the axis along which
the child views are tiled.

**Returns:** the major axis of the box, either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

- setAxis

```java
public void setAxis​(int axis)
```

Sets the tile axis property. This is the axis along which
the child views are tiled.

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

- layoutChanged

```java
public void layoutChanged​(int axis)
```

Invalidates the layout along an axis. This happens
automatically if the preferences have changed for
any of the child views. In some cases the layout
may need to be recalculated when the preferences
have not changed. The layout can be marked as
invalid by calling this method. The layout will
be updated the next time the

setSize

method
is called on this view (typically in paint).

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

- isLayoutValid

```java
protected boolean isLayoutValid​(int axis)
```

Determines if the layout is valid along the given axis.

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Returns:** if the layout is valid along the given axis
**Since:** 1.4

- paintChild

```java
protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)
```

Paints a child. By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Parameters:** g

- the graphics context
**Parameters:** alloc

- the allocated region to paint into
**Parameters:** index

- the child index, >= 0 && < getViewCount()

- replace

```java
public void replace​(int index,
int length,

View
[] elems)
```

Invalidates the layout and resizes the cache of
requests/allocations. The child allocations can still
be accessed for the old layout, but the new children
will have an offset and span of 0.

**Overrides:** replace

in class

CompositeView
**Parameters:** index

- the starting index into the child views to insert
the new views; this should be a value >= 0 and <= getViewCount
**Parameters:** length

- the number of existing child views to remove;
This should be a value >= 0 and <= (getViewCount() - offset)
**Parameters:** elems

- the child views to add; this value can be

null

to indicate no children are being added
(useful to remove)

- forwardUpdate

```java
protected void forwardUpdate​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.
If a child changed its requirements and the allocation
was valid prior to forwarding the portion of the box
from the starting child to the end of the box will
be repainted.

**Overrides:** forwardUpdate

in class

View
**Parameters:** ec

- changes to the element this view is responsible
for (may be

null

if there were no changes)
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**Since:** 1.3
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- preferenceChanged

```java
public void preferenceChanged​(
View
child,
boolean width,
boolean height)
```

This is called by a child to indicate its
preferred span has changed. This is implemented to
throw away cached layout information so that new
calculations will be done the next time the children
need an allocation.

**Overrides:** preferenceChanged

in class

View
**Parameters:** child

- the child view
**Parameters:** width

- true if the width preference should change
**Parameters:** height

- true if the height preference should change
**See Also:** JComponent.revalidate()

- getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Gets the resize weight. A value of 0 or less is not resizable.

**Overrides:** getResizeWeight

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the weight
**Throws:** IllegalArgumentException

- for an invalid axis

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information. This is implemented to call the
layout method with the sizes inside of the insets.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

- paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders the

BoxView

using the given
rendering surface and area
on that surface. Only the children that intersect
the clip bounds of the given

Graphics

will be rendered.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** allocation

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getChildAllocation

```java
public
Shape
getChildAllocation​(int index,

Shape
a)
```

Fetches the allocation for the given child view.
This enables finding out where various views
are located. This is implemented to return

null

if the layout is invalid,
otherwise the superclass behavior is executed.

**Overrides:** getChildAllocation

in class

CompositeView
**Parameters:** index

- the index of the child, >= 0 && > getViewCount()
**Parameters:** a

- the allocation to this view
**Returns:** the allocation to the child; or

null

if

a

is

null

;
or

null

if the layout is invalid

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
to the coordinate space of the view mapped to it. This makes
sure the allocation is valid before calling the superclass.

**Overrides:** modelToView

in class

CompositeView
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

**Overrides:** viewToModel

in class

CompositeView
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

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the total alignment
needed to position the children with the alignment points
lined up along the axis orthogonal to the axis that is
being tiled. The axis being tiled will request to be
centered (i.e. 0.5f).

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the desired alignment >= 0.0f && <= 1.0f; this should
be a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view
**Throws:** IllegalArgumentException

- for an invalid axis

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis.

**Overrides:** getMaximumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- isAllocationValid

```java
protected boolean isAllocationValid()
```

Are the allocations for the children still
valid?

**Returns:** true if allocations still valid

- isBefore

```java
protected boolean isBefore​(int x,
int y,

Rectangle
innerAlloc)
```

Determines if a point falls before an allocated region.

**Specified by:** isBefore

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** innerAlloc

- the allocated region; this is the area
inside of the insets
**Returns:** true if the point lies before the region else false

- isAfter

```java
protected boolean isAfter​(int x,
int y,

Rectangle
innerAlloc)
```

Determines if a point falls after an allocated region.

**Specified by:** isAfter

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** innerAlloc

- the allocated region; this is the area
inside of the insets
**Returns:** true if the point lies after the region else false

- getViewAtPoint

```java
protected
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)
```

Fetches the child view at the given coordinates.

**Specified by:** getViewAtPoint

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the parents inner allocation on entry, which should
be changed to the child's allocation on exit
**Returns:** the view

- childAllocation

```java
protected void childAllocation​(int index,

Rectangle
alloc)
```

Allocates a region for a child view.

**Specified by:** childAllocation

in class

CompositeView
**Parameters:** index

- the index of the child view to
allocate, >= 0 && < getViewCount()
**Parameters:** alloc

- the allocated region

- layout

```java
protected void layout​(int width,
int height)
```

Perform layout on the box

**Parameters:** width

- the width (inside of the insets) >= 0
**Parameters:** height

- the height (inside of the insets) >= 0

- getWidth

```java
public int getWidth()
```

Returns the current width of the box. This is the width that
it was last allocated.

**Returns:** the current width of the box

- getHeight

```java
public int getHeight()
```

Returns the current height of the box. This is the height that
it was last allocated.

**Returns:** the current height of the box

- layoutMajorAxis

```java
protected void layoutMajorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Performs layout for the major axis of the box (i.e. the
axis that it represents). The results of the layout (the
offset and span for each children) are placed in the given
arrays which represent the allocations to the children
along the major axis.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

- layoutMinorAxis

```java
protected void layoutMinorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents). The results
of the layout (the offset and span for each children) are
placed in the given arrays which represent the allocations to
the children along the minor axis.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

- calculateMajorAxisRequirements

```java
protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for the major axis

axis

.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object
**See Also:** SizeRequirements

- calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for the minor axis

axis

.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object
**See Also:** SizeRequirements

- baselineLayout

```java
protected void baselineLayout​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being studied, either

View.X_AXIS

or

View.Y_AXIS
**Parameters:** offsets

- an empty array filled by this method with
values specifying the location of each child view
**Parameters:** spans

- an empty array filled by this method with
values specifying the extent of each child view

- baselineRequirements

```java
protected
SizeRequirements
baselineRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for this

BoxView

by examining the size of each child view.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object

- getOffset

```java
protected int getOffset​(int axis,
int childIndex)
```

Fetches the offset of a particular child's current layout.

**Parameters:** axis

- the axis being studied
**Parameters:** childIndex

- the index of the requested child
**Returns:** the offset (location) for the specified child

- getSpan

```java
protected int getSpan​(int axis,
int childIndex)
```

Fetches the span of a particular child's current layout.

**Parameters:** axis

- the axis being studied
**Parameters:** childIndex

- the index of the requested child
**Returns:** the span (width or height) of the specified child

- flipEastAndWestAtEnds

```java
protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)
```

Determines in which direction the next view lays.
Consider the View at index n. Typically the

View

s
are layed out from left to right, so that the

View

to the EAST will be at index n + 1, and the

View

to the WEST will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true,
indicating the

View

s are layed out in
descending order. Otherwise the method would return false
indicating the

View

s are layed out in ascending order.

If the receiver is laying its

View

s along the

Y_AXIS

, this will return the value from
invoking the same method on the

View

responsible for rendering

position

and

bias

. Otherwise this will return false.

**Overrides:** flipEastAndWestAtEnds

in class

CompositeView
**Parameters:** position

- position into the model
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** true if the

View

s surrounding the

View

responding for rendering

position

and

bias

are layed out in descending order; otherwise false

Constructor Detail

- BoxView

```java
public BoxView​(
Element
elem,
int axis)
```

Constructs a

BoxView

.

**Parameters:** elem

- the element this view is responsible for
**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS

---

#### Constructor Detail

BoxView

```java
public BoxView​(
Element
elem,
int axis)
```

Constructs a

BoxView

.

**Parameters:** elem

- the element this view is responsible for
**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS

---

#### BoxView

public BoxView​(

Element

elem,
int axis)

Constructs a

BoxView

.

Method Detail

- getAxis

```java
public int getAxis()
```

Fetches the tile axis property. This is the axis along which
the child views are tiled.

**Returns:** the major axis of the box, either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

- setAxis

```java
public void setAxis​(int axis)
```

Sets the tile axis property. This is the axis along which
the child views are tiled.

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

- layoutChanged

```java
public void layoutChanged​(int axis)
```

Invalidates the layout along an axis. This happens
automatically if the preferences have changed for
any of the child views. In some cases the layout
may need to be recalculated when the preferences
have not changed. The layout can be marked as
invalid by calling this method. The layout will
be updated the next time the

setSize

method
is called on this view (typically in paint).

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

- isLayoutValid

```java
protected boolean isLayoutValid​(int axis)
```

Determines if the layout is valid along the given axis.

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Returns:** if the layout is valid along the given axis
**Since:** 1.4

- paintChild

```java
protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)
```

Paints a child. By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Parameters:** g

- the graphics context
**Parameters:** alloc

- the allocated region to paint into
**Parameters:** index

- the child index, >= 0 && < getViewCount()

- replace

```java
public void replace​(int index,
int length,

View
[] elems)
```

Invalidates the layout and resizes the cache of
requests/allocations. The child allocations can still
be accessed for the old layout, but the new children
will have an offset and span of 0.

**Overrides:** replace

in class

CompositeView
**Parameters:** index

- the starting index into the child views to insert
the new views; this should be a value >= 0 and <= getViewCount
**Parameters:** length

- the number of existing child views to remove;
This should be a value >= 0 and <= (getViewCount() - offset)
**Parameters:** elems

- the child views to add; this value can be

null

to indicate no children are being added
(useful to remove)

- forwardUpdate

```java
protected void forwardUpdate​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.
If a child changed its requirements and the allocation
was valid prior to forwarding the portion of the box
from the starting child to the end of the box will
be repainted.

**Overrides:** forwardUpdate

in class

View
**Parameters:** ec

- changes to the element this view is responsible
for (may be

null

if there were no changes)
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**Since:** 1.3
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- preferenceChanged

```java
public void preferenceChanged​(
View
child,
boolean width,
boolean height)
```

This is called by a child to indicate its
preferred span has changed. This is implemented to
throw away cached layout information so that new
calculations will be done the next time the children
need an allocation.

**Overrides:** preferenceChanged

in class

View
**Parameters:** child

- the child view
**Parameters:** width

- true if the width preference should change
**Parameters:** height

- true if the height preference should change
**See Also:** JComponent.revalidate()

- getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Gets the resize weight. A value of 0 or less is not resizable.

**Overrides:** getResizeWeight

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the weight
**Throws:** IllegalArgumentException

- for an invalid axis

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information. This is implemented to call the
layout method with the sizes inside of the insets.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

- paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders the

BoxView

using the given
rendering surface and area
on that surface. Only the children that intersect
the clip bounds of the given

Graphics

will be rendered.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** allocation

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getChildAllocation

```java
public
Shape
getChildAllocation​(int index,

Shape
a)
```

Fetches the allocation for the given child view.
This enables finding out where various views
are located. This is implemented to return

null

if the layout is invalid,
otherwise the superclass behavior is executed.

**Overrides:** getChildAllocation

in class

CompositeView
**Parameters:** index

- the index of the child, >= 0 && > getViewCount()
**Parameters:** a

- the allocation to this view
**Returns:** the allocation to the child; or

null

if

a

is

null

;
or

null

if the layout is invalid

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
to the coordinate space of the view mapped to it. This makes
sure the allocation is valid before calling the superclass.

**Overrides:** modelToView

in class

CompositeView
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

**Overrides:** viewToModel

in class

CompositeView
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

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the total alignment
needed to position the children with the alignment points
lined up along the axis orthogonal to the axis that is
being tiled. The axis being tiled will request to be
centered (i.e. 0.5f).

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the desired alignment >= 0.0f && <= 1.0f; this should
be a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view
**Throws:** IllegalArgumentException

- for an invalid axis

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis.

**Overrides:** getMaximumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- isAllocationValid

```java
protected boolean isAllocationValid()
```

Are the allocations for the children still
valid?

**Returns:** true if allocations still valid

- isBefore

```java
protected boolean isBefore​(int x,
int y,

Rectangle
innerAlloc)
```

Determines if a point falls before an allocated region.

**Specified by:** isBefore

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** innerAlloc

- the allocated region; this is the area
inside of the insets
**Returns:** true if the point lies before the region else false

- isAfter

```java
protected boolean isAfter​(int x,
int y,

Rectangle
innerAlloc)
```

Determines if a point falls after an allocated region.

**Specified by:** isAfter

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** innerAlloc

- the allocated region; this is the area
inside of the insets
**Returns:** true if the point lies after the region else false

- getViewAtPoint

```java
protected
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)
```

Fetches the child view at the given coordinates.

**Specified by:** getViewAtPoint

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the parents inner allocation on entry, which should
be changed to the child's allocation on exit
**Returns:** the view

- childAllocation

```java
protected void childAllocation​(int index,

Rectangle
alloc)
```

Allocates a region for a child view.

**Specified by:** childAllocation

in class

CompositeView
**Parameters:** index

- the index of the child view to
allocate, >= 0 && < getViewCount()
**Parameters:** alloc

- the allocated region

- layout

```java
protected void layout​(int width,
int height)
```

Perform layout on the box

**Parameters:** width

- the width (inside of the insets) >= 0
**Parameters:** height

- the height (inside of the insets) >= 0

- getWidth

```java
public int getWidth()
```

Returns the current width of the box. This is the width that
it was last allocated.

**Returns:** the current width of the box

- getHeight

```java
public int getHeight()
```

Returns the current height of the box. This is the height that
it was last allocated.

**Returns:** the current height of the box

- layoutMajorAxis

```java
protected void layoutMajorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Performs layout for the major axis of the box (i.e. the
axis that it represents). The results of the layout (the
offset and span for each children) are placed in the given
arrays which represent the allocations to the children
along the major axis.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

- layoutMinorAxis

```java
protected void layoutMinorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents). The results
of the layout (the offset and span for each children) are
placed in the given arrays which represent the allocations to
the children along the minor axis.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

- calculateMajorAxisRequirements

```java
protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for the major axis

axis

.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object
**See Also:** SizeRequirements

- calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for the minor axis

axis

.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object
**See Also:** SizeRequirements

- baselineLayout

```java
protected void baselineLayout​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being studied, either

View.X_AXIS

or

View.Y_AXIS
**Parameters:** offsets

- an empty array filled by this method with
values specifying the location of each child view
**Parameters:** spans

- an empty array filled by this method with
values specifying the extent of each child view

- baselineRequirements

```java
protected
SizeRequirements
baselineRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for this

BoxView

by examining the size of each child view.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object

- getOffset

```java
protected int getOffset​(int axis,
int childIndex)
```

Fetches the offset of a particular child's current layout.

**Parameters:** axis

- the axis being studied
**Parameters:** childIndex

- the index of the requested child
**Returns:** the offset (location) for the specified child

- getSpan

```java
protected int getSpan​(int axis,
int childIndex)
```

Fetches the span of a particular child's current layout.

**Parameters:** axis

- the axis being studied
**Parameters:** childIndex

- the index of the requested child
**Returns:** the span (width or height) of the specified child

- flipEastAndWestAtEnds

```java
protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)
```

Determines in which direction the next view lays.
Consider the View at index n. Typically the

View

s
are layed out from left to right, so that the

View

to the EAST will be at index n + 1, and the

View

to the WEST will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true,
indicating the

View

s are layed out in
descending order. Otherwise the method would return false
indicating the

View

s are layed out in ascending order.

If the receiver is laying its

View

s along the

Y_AXIS

, this will return the value from
invoking the same method on the

View

responsible for rendering

position

and

bias

. Otherwise this will return false.

**Overrides:** flipEastAndWestAtEnds

in class

CompositeView
**Parameters:** position

- position into the model
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** true if the

View

s surrounding the

View

responding for rendering

position

and

bias

are layed out in descending order; otherwise false

---

#### Method Detail

getAxis

```java
public int getAxis()
```

Fetches the tile axis property. This is the axis along which
the child views are tiled.

**Returns:** the major axis of the box, either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

---

#### getAxis

public int getAxis()

Fetches the tile axis property. This is the axis along which
the child views are tiled.

setAxis

```java
public void setAxis​(int axis)
```

Sets the tile axis property. This is the axis along which
the child views are tiled.

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

---

#### setAxis

public void setAxis​(int axis)

Sets the tile axis property. This is the axis along which
the child views are tiled.

layoutChanged

```java
public void layoutChanged​(int axis)
```

Invalidates the layout along an axis. This happens
automatically if the preferences have changed for
any of the child views. In some cases the layout
may need to be recalculated when the preferences
have not changed. The layout can be marked as
invalid by calling this method. The layout will
be updated the next time the

setSize

method
is called on this view (typically in paint).

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Since:** 1.3

---

#### layoutChanged

public void layoutChanged​(int axis)

Invalidates the layout along an axis. This happens
automatically if the preferences have changed for
any of the child views. In some cases the layout
may need to be recalculated when the preferences
have not changed. The layout can be marked as
invalid by calling this method. The layout will
be updated the next time the

setSize

method
is called on this view (typically in paint).

isLayoutValid

```java
protected boolean isLayoutValid​(int axis)
```

Determines if the layout is valid along the given axis.

**Parameters:** axis

- either

View.X_AXIS

or

View.Y_AXIS
**Returns:** if the layout is valid along the given axis
**Since:** 1.4

---

#### isLayoutValid

protected boolean isLayoutValid​(int axis)

Determines if the layout is valid along the given axis.

paintChild

```java
protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)
```

Paints a child. By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Parameters:** g

- the graphics context
**Parameters:** alloc

- the allocated region to paint into
**Parameters:** index

- the child index, >= 0 && < getViewCount()

---

#### paintChild

protected void paintChild​(

Graphics

g,

Rectangle

alloc,
int index)

Paints a child. By default
that is all it does, but a subclass can use this to paint
things relative to the child.

replace

```java
public void replace​(int index,
int length,

View
[] elems)
```

Invalidates the layout and resizes the cache of
requests/allocations. The child allocations can still
be accessed for the old layout, but the new children
will have an offset and span of 0.

**Overrides:** replace

in class

CompositeView
**Parameters:** index

- the starting index into the child views to insert
the new views; this should be a value >= 0 and <= getViewCount
**Parameters:** length

- the number of existing child views to remove;
This should be a value >= 0 and <= (getViewCount() - offset)
**Parameters:** elems

- the child views to add; this value can be

null

to indicate no children are being added
(useful to remove)

---

#### replace

public void replace​(int index,
int length,

View

[] elems)

Invalidates the layout and resizes the cache of
requests/allocations. The child allocations can still
be accessed for the old layout, but the new children
will have an offset and span of 0.

forwardUpdate

```java
protected void forwardUpdate​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.
If a child changed its requirements and the allocation
was valid prior to forwarding the portion of the box
from the starting child to the end of the box will
be repainted.

**Overrides:** forwardUpdate

in class

View
**Parameters:** ec

- changes to the element this view is responsible
for (may be

null

if there were no changes)
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**Since:** 1.3
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### forwardUpdate

protected void forwardUpdate​(

DocumentEvent.ElementChange

ec,

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Forwards the given

DocumentEvent

to the child views
that need to be notified of the change to the model.
If a child changed its requirements and the allocation
was valid prior to forwarding the portion of the box
from the starting child to the end of the box will
be repainted.

preferenceChanged

```java
public void preferenceChanged​(
View
child,
boolean width,
boolean height)
```

This is called by a child to indicate its
preferred span has changed. This is implemented to
throw away cached layout information so that new
calculations will be done the next time the children
need an allocation.

**Overrides:** preferenceChanged

in class

View
**Parameters:** child

- the child view
**Parameters:** width

- true if the width preference should change
**Parameters:** height

- true if the height preference should change
**See Also:** JComponent.revalidate()

---

#### preferenceChanged

public void preferenceChanged​(

View

child,
boolean width,
boolean height)

This is called by a child to indicate its
preferred span has changed. This is implemented to
throw away cached layout information so that new
calculations will be done the next time the children
need an allocation.

getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Gets the resize weight. A value of 0 or less is not resizable.

**Overrides:** getResizeWeight

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the weight
**Throws:** IllegalArgumentException

- for an invalid axis

---

#### getResizeWeight

public int getResizeWeight​(int axis)

Gets the resize weight. A value of 0 or less is not resizable.

setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information. This is implemented to call the
layout method with the sizes inside of the insets.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

---

#### setSize

public void setSize​(float width,
float height)

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information. This is implemented to call the
layout method with the sizes inside of the insets.

paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders the

BoxView

using the given
rendering surface and area
on that surface. Only the children that intersect
the clip bounds of the given

Graphics

will be rendered.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** allocation

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

---

#### paint

public void paint​(

Graphics

g,

Shape

allocation)

Renders the

BoxView

using the given
rendering surface and area
on that surface. Only the children that intersect
the clip bounds of the given

Graphics

will be rendered.

getChildAllocation

```java
public
Shape
getChildAllocation​(int index,

Shape
a)
```

Fetches the allocation for the given child view.
This enables finding out where various views
are located. This is implemented to return

null

if the layout is invalid,
otherwise the superclass behavior is executed.

**Overrides:** getChildAllocation

in class

CompositeView
**Parameters:** index

- the index of the child, >= 0 && > getViewCount()
**Parameters:** a

- the allocation to this view
**Returns:** the allocation to the child; or

null

if

a

is

null

;
or

null

if the layout is invalid

---

#### getChildAllocation

public

Shape

getChildAllocation​(int index,

Shape

a)

Fetches the allocation for the given child view.
This enables finding out where various views
are located. This is implemented to return

null

if the layout is invalid,
otherwise the superclass behavior is executed.

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
to the coordinate space of the view mapped to it. This makes
sure the allocation is valid before calling the superclass.

**Overrides:** modelToView

in class

CompositeView
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
to the coordinate space of the view mapped to it. This makes
sure the allocation is valid before calling the superclass.

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

**Overrides:** viewToModel

in class

CompositeView
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

getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the total alignment
needed to position the children with the alignment points
lined up along the axis orthogonal to the axis that is
being tiled. The axis being tiled will request to be
centered (i.e. 0.5f).

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the desired alignment >= 0.0f && <= 1.0f; this should
be a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view
**Throws:** IllegalArgumentException

- for an invalid axis

---

#### getAlignment

public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the total alignment
needed to position the children with the alignment points
lined up along the axis orthogonal to the axis that is
being tiled. The axis being tiled will request to be
centered (i.e. 0.5f).

getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

---

#### getMinimumSpan

public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an
axis.

getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis.

**Overrides:** getMaximumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

---

#### getMaximumSpan

public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis.

isAllocationValid

```java
protected boolean isAllocationValid()
```

Are the allocations for the children still
valid?

**Returns:** true if allocations still valid

---

#### isAllocationValid

protected boolean isAllocationValid()

Are the allocations for the children still
valid?

isBefore

```java
protected boolean isBefore​(int x,
int y,

Rectangle
innerAlloc)
```

Determines if a point falls before an allocated region.

**Specified by:** isBefore

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** innerAlloc

- the allocated region; this is the area
inside of the insets
**Returns:** true if the point lies before the region else false

---

#### isBefore

protected boolean isBefore​(int x,
int y,

Rectangle

innerAlloc)

Determines if a point falls before an allocated region.

isAfter

```java
protected boolean isAfter​(int x,
int y,

Rectangle
innerAlloc)
```

Determines if a point falls after an allocated region.

**Specified by:** isAfter

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** innerAlloc

- the allocated region; this is the area
inside of the insets
**Returns:** true if the point lies after the region else false

---

#### isAfter

protected boolean isAfter​(int x,
int y,

Rectangle

innerAlloc)

Determines if a point falls after an allocated region.

getViewAtPoint

```java
protected
View
getViewAtPoint​(int x,
int y,

Rectangle
alloc)
```

Fetches the child view at the given coordinates.

**Specified by:** getViewAtPoint

in class

CompositeView
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** alloc

- the parents inner allocation on entry, which should
be changed to the child's allocation on exit
**Returns:** the view

---

#### getViewAtPoint

protected

View

getViewAtPoint​(int x,
int y,

Rectangle

alloc)

Fetches the child view at the given coordinates.

childAllocation

```java
protected void childAllocation​(int index,

Rectangle
alloc)
```

Allocates a region for a child view.

**Specified by:** childAllocation

in class

CompositeView
**Parameters:** index

- the index of the child view to
allocate, >= 0 && < getViewCount()
**Parameters:** alloc

- the allocated region

---

#### childAllocation

protected void childAllocation​(int index,

Rectangle

alloc)

Allocates a region for a child view.

layout

```java
protected void layout​(int width,
int height)
```

Perform layout on the box

**Parameters:** width

- the width (inside of the insets) >= 0
**Parameters:** height

- the height (inside of the insets) >= 0

---

#### layout

protected void layout​(int width,
int height)

Perform layout on the box

getWidth

```java
public int getWidth()
```

Returns the current width of the box. This is the width that
it was last allocated.

**Returns:** the current width of the box

---

#### getWidth

public int getWidth()

Returns the current width of the box. This is the width that
it was last allocated.

getHeight

```java
public int getHeight()
```

Returns the current height of the box. This is the height that
it was last allocated.

**Returns:** the current height of the box

---

#### getHeight

public int getHeight()

Returns the current height of the box. This is the height that
it was last allocated.

layoutMajorAxis

```java
protected void layoutMajorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Performs layout for the major axis of the box (i.e. the
axis that it represents). The results of the layout (the
offset and span for each children) are placed in the given
arrays which represent the allocations to the children
along the major axis.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

---

#### layoutMajorAxis

protected void layoutMajorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the major axis of the box (i.e. the
axis that it represents). The results of the layout (the
offset and span for each children) are placed in the given
arrays which represent the allocations to the children
along the major axis.

layoutMinorAxis

```java
protected void layoutMinorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents). The results
of the layout (the offset and span for each children) are
placed in the given arrays which represent the allocations to
the children along the minor axis.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

---

#### layoutMinorAxis

protected void layoutMinorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents). The results
of the layout (the offset and span for each children) are
placed in the given arrays which represent the allocations to
the children along the minor axis.

calculateMajorAxisRequirements

```java
protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for the major axis

axis

.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object
**See Also:** SizeRequirements

---

#### calculateMajorAxisRequirements

protected

SizeRequirements

calculateMajorAxisRequirements​(int axis,

SizeRequirements

r)

Calculates the size requirements for the major axis

axis

.

calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for the minor axis

axis

.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object
**See Also:** SizeRequirements

---

#### calculateMinorAxisRequirements

protected

SizeRequirements

calculateMinorAxisRequirements​(int axis,

SizeRequirements

r)

Calculates the size requirements for the minor axis

axis

.

baselineLayout

```java
protected void baselineLayout​(int targetSpan,
int axis,
int[] offsets,
int[] spans)
```

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children
**Parameters:** axis

- the axis being studied, either

View.X_AXIS

or

View.Y_AXIS
**Parameters:** offsets

- an empty array filled by this method with
values specifying the location of each child view
**Parameters:** spans

- an empty array filled by this method with
values specifying the extent of each child view

---

#### baselineLayout

protected void baselineLayout​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Computes the location and extent of each child view
in this

BoxView

given the

targetSpan

,
which is the width (or height) of the region we have to
work with.

baselineRequirements

```java
protected
SizeRequirements
baselineRequirements​(int axis,

SizeRequirements
r)
```

Calculates the size requirements for this

BoxView

by examining the size of each child view.

**Parameters:** axis

- the axis being studied
**Parameters:** r

- the

SizeRequirements

object;
if

null

one will be created
**Returns:** the newly initialized

SizeRequirements

object

---

#### baselineRequirements

protected

SizeRequirements

baselineRequirements​(int axis,

SizeRequirements

r)

Calculates the size requirements for this

BoxView

by examining the size of each child view.

getOffset

```java
protected int getOffset​(int axis,
int childIndex)
```

Fetches the offset of a particular child's current layout.

**Parameters:** axis

- the axis being studied
**Parameters:** childIndex

- the index of the requested child
**Returns:** the offset (location) for the specified child

---

#### getOffset

protected int getOffset​(int axis,
int childIndex)

Fetches the offset of a particular child's current layout.

getSpan

```java
protected int getSpan​(int axis,
int childIndex)
```

Fetches the span of a particular child's current layout.

**Parameters:** axis

- the axis being studied
**Parameters:** childIndex

- the index of the requested child
**Returns:** the span (width or height) of the specified child

---

#### getSpan

protected int getSpan​(int axis,
int childIndex)

Fetches the span of a particular child's current layout.

flipEastAndWestAtEnds

```java
protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias
bias)
```

Determines in which direction the next view lays.
Consider the View at index n. Typically the

View

s
are layed out from left to right, so that the

View

to the EAST will be at index n + 1, and the

View

to the WEST will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true,
indicating the

View

s are layed out in
descending order. Otherwise the method would return false
indicating the

View

s are layed out in ascending order.

If the receiver is laying its

View

s along the

Y_AXIS

, this will return the value from
invoking the same method on the

View

responsible for rendering

position

and

bias

. Otherwise this will return false.

**Overrides:** flipEastAndWestAtEnds

in class

CompositeView
**Parameters:** position

- position into the model
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** true if the

View

s surrounding the

View

responding for rendering

position

and

bias

are layed out in descending order; otherwise false

---

#### flipEastAndWestAtEnds

protected boolean flipEastAndWestAtEnds​(int position,

Position.Bias

bias)

Determines in which direction the next view lays.
Consider the View at index n. Typically the

View

s
are layed out from left to right, so that the

View

to the EAST will be at index n + 1, and the

View

to the WEST will be at index n - 1. In certain situations,
such as with bidirectional text, it is possible
that the

View

to EAST is not at index n + 1,
but rather at index n - 1, or that the

View

to the WEST is not at index n - 1, but index n + 1.
In this case this method would return true,
indicating the

View

s are layed out in
descending order. Otherwise the method would return false
indicating the

View

s are layed out in ascending order.

If the receiver is laying its

View

s along the

Y_AXIS

, this will return the value from
invoking the same method on the

View

responsible for rendering

position

and

bias

. Otherwise this will return false.

If the receiver is laying its

View

s along the

Y_AXIS

, this will return the value from
invoking the same method on the

View

responsible for rendering

position

and

bias

. Otherwise this will return false.

---

