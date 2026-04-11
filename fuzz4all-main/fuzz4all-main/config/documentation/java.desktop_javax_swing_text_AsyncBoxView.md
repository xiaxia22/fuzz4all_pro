# Class AsyncBoxView

**Source:** `java.desktop\javax\swing\text\AsyncBoxView.html`

### Class Description

```java
public class
AsyncBoxView

extends
View
```

A box that does layout asynchronously. This
is useful to keep the GUI event thread moving by
not doing any layout on it. The layout is done
on a granularity of operations on the child views.
After each child view is accessed for some part
of layout (a potentially time consuming operation)
the remaining tasks can be abandoned or a new higher
priority task (i.e. to service a synchronous request
or a visible area) can be taken on.

While the child view is being accessed
a read lock is acquired on the associated document
so that the model is stable while being accessed.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

#### protected
AsyncBoxView.ChildLocator
locator

Object that manages the offsets of the
children. All locking for management of
child locations is on this object.

---

### Constructor Details

#### public AsyncBoxView​(
Element
elem,
int axis)

Construct a box view that does asynchronous layout.

**Parameters:**
- elem

- the element of the model to represent
- axis

- the axis to tile along. This can be
either X_AXIS or Y_AXIS.

---

### Method Details

#### public int getMajorAxis()

Fetch the major axis (the axis the children
are tiled along). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:**
- the major axis

---

#### public int getMinorAxis()

Fetch the minor axis (the axis orthogonal
to the tiled axis). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:**
- the minor axis

---

#### public float getTopInset()

Get the top part of the margin around the view.

**Returns:**
- the top part of the margin around the view

---

#### public void setTopInset​(float i)

Set the top part of the margin around the view.

**Parameters:**
- i

- the value of the inset

---

#### public float getBottomInset()

Get the bottom part of the margin around the view.

**Returns:**
- the bottom part of the margin around the view

---

#### public void setBottomInset​(float i)

Set the bottom part of the margin around the view.

**Parameters:**
- i

- the value of the inset

---

#### public float getLeftInset()

Get the left part of the margin around the view.

**Returns:**
- the left part of the margin around the view

---

#### public void setLeftInset​(float i)

Set the left part of the margin around the view.

**Parameters:**
- i

- the value of the inset

---

#### public float getRightInset()

Get the right part of the margin around the view.

**Returns:**
- the right part of the margin around the view

---

#### public void setRightInset​(float i)

Set the right part of the margin around the view.

**Parameters:**
- i

- the value of the inset

---

#### protected float getInsetSpan​(int axis)

Fetch the span along an axis that is taken up by the insets.

**Parameters:**
- axis

- the axis to determine the total insets along,
either X_AXIS or Y_AXIS.

**Returns:**
- the span along an axis that is taken up by the insets

**Since:**
- 1.4

---

#### protected void setEstimatedMajorSpan​(boolean isEstimated)

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated. If this
property is true, the value of setSize along the major axis
will change the requirements along the major axis and incremental
changes will be ignored until all of the children have been updated
(which will cause the property to automatically be set to false).
If the property is false the value of the majorSpan will be
considered to be accurate and incremental changes will be
added into the total as they are calculated.

**Parameters:**
- isEstimated

- new value for the estimatedMajorSpan property

**Since:**
- 1.4

---

#### protected boolean getEstimatedMajorSpan()

Is the major span currently estimated?

**Returns:**
- whether or not the major span currently estimated

**Since:**
- 1.4

---

#### protected
AsyncBoxView.ChildState
getChildState​(int index)

Fetch the object representing the layout state of
of the child at the given index.

**Parameters:**
- index

- the child index. This should be a
value >= 0 and < getViewCount().

**Returns:**
- the object representing the layout state of
of the child at the given index

---

#### protected
LayoutQueue
getLayoutQueue()

Fetch the queue to use for layout.

**Returns:**
- the queue to use for layout

---

#### protected
AsyncBoxView.ChildState
createChildState​(
View
v)

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

**Parameters:**
- v

- the view

**Returns:**
- new child state

---

#### protected void majorRequirementChange​(
AsyncBoxView.ChildState
cs,
float delta)

Requirements changed along the major axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the event thread if it is trying to update
something immediately (such as to perform a
model/view translation).

This is implemented to mark the major axis as having
changed so that a future check to see if the requirements
need to be published to the parent view will consider
the major axis. If the span along the major axis is
not estimated, it is updated by the given delta to reflect
the incremental change. The delta is ignored if the
major span is estimated.

**Parameters:**
- cs

- the child state
- delta

- the delta

---

#### protected void minorRequirementChange​(
AsyncBoxView.ChildState
cs)

Requirements changed along the minor axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the GUI thread if it is trying to update
something immediately (such as to perform a
model/view translation).

**Parameters:**
- cs

- the child state

---

#### protected void flushRequirementChanges()

Publish the changes in preferences upward to the parent
view. This is normally called by the layout thread.

---

#### public void replace​(int offset,
int length,

View
[] views)

Calls the superclass to update the child views, and
updates the status records for the children. This
is expected to be called while a write lock is held
on the model so that interaction with the layout
thread will not happen (i.e. the layout thread
acquires a read lock before doing anything).

**Overrides:**
- replace

in class

View

**Parameters:**
- offset

- the starting offset into the child views >= 0
- length

- the number of existing views to replace >= 0
- views

- the child views to insert

---

#### protected void loadChildren​(
ViewFactory
f)

Loads all of the children to initialize the view.
This is called by the

setParent

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

Normally a write-lock is held on the Document while
the children are being changed, which keeps the rendering
and layout threads safe. The exception to this is when
the view is initialized to represent an existing element
(via this method), so it is synchronized to exclude
preferenceChanged while we are initializing.

**Parameters:**
- f

- the view factory

**See Also:**
- setParent(javax.swing.text.View)

---

#### protected int getViewIndexAtPosition​(int pos,

Position.Bias
b)

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:**
- pos

- the position >= 0
- b

- the position bias

**Returns:**
- index of the view representing the given position, or
-1 if no view represents that position

---

#### protected void updateLayout​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a)

Update the layout in response to receiving notification of
change from the model. This is implemented to note the
change on the ChildLocator so that offsets of the children
will be correctly computed.

**Overrides:**
- updateLayout

in class

View

**Parameters:**
- ec

- changes to the element this view is responsible
for (may be null if there were no changes).
- e

- the change information from the associated document
- a

- the current allocation of the view

**See Also:**
- View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

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
(to get the hosting Container for example).
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

- the parent of the view, null if none

---

#### public void preferenceChanged​(
View
child,
boolean width,
boolean height)

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout. This is reimplemented to queue new work
on the layout thread. This method gets messaged from
multiple threads via the children.

**Overrides:**
- preferenceChanged

in class

View

**Parameters:**
- child

- the child view
- width

- true if the width preference has changed
- height

- true if the height preference has changed

**See Also:**
- JComponent.revalidate()

---

#### public void setSize​(float width,
float height)

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information.

Since the major axis is updated asynchronously and should be
the sum of the tiled children the call is ignored for the major
axis. Since the minor axis is flexible, work is queued to resize
the children if the minor span changes.

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
alloc)

Render the view using the given allocation and
rendering surface.

This is implemented to determine whether or not the
desired region to be rendered (i.e. the unclipped
area) is up to date or not. If up-to-date the children
are rendered. If not up-to-date, a task to build
the desired area is placed on the layout queue as
a high priority task. This keeps by event thread
moving by rendering if ready, and postponing until
a later time if not ready (since paint requests
can be rescheduled).

**Specified by:**
- paint

in class

View

**Parameters:**
- g

- the rendering surface to use
- alloc

- the allocated region to render into

**See Also:**
- View.paint(java.awt.Graphics, java.awt.Shape)

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

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

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

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

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

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**Throws:**
- IllegalArgumentException

- for an invalid axis type

**See Also:**
- View.getPreferredSpan(int)

---

#### public int getViewCount()

Returns the number of views in this view. Since
the default is to not be a composite view this
returns 0.

**Overrides:**
- getViewCount

in class

View

**Returns:**
- the number of views >= 0

**See Also:**
- View.getViewCount()

---

#### public
View
getView​(int n)

Gets the nth child view. Since there are no
children by default, this returns null.

**Overrides:**
- getView

in class

View

**Parameters:**
- n

- the number of the view to get, >= 0 && < getViewCount()

**Returns:**
- the view

---

#### public
Shape
getChildAllocation​(int index,

Shape
a)

Fetches the allocation for the given child view.
This enables finding out where various views
are located, without assuming the views store
their location. This returns null since the
default is to not have any child views.

**Overrides:**
- getChildAllocation

in class

View

**Parameters:**
- index

- the index of the child, >= 0 && < getViewCount()
- a

- the allocation to this view.

**Returns:**
- the allocation to the child

---

#### public int getViewIndex​(int pos,

Position.Bias
b)

Returns the child view index representing the given position in
the model. By default a view has no children so this is implemented
to return -1 to indicate there is no valid child index for any
position.

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

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views.

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
[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

This is expected to be called by the GUI thread, holding a
read-lock on the associated model. It is implemented to
locate the child view and determine it's allocation with a
lock on the ChildLocator object, and to call viewToModel
on the child view with a lock on the ChildState object
to avoid interaction with the layout thread.

**Specified by:**
- viewToModel

in class

View

**Parameters:**
- x

- the X coordinate >= 0
- y

- the Y coordinate >= 0
- a

- the allocated region to render into
- biasReturn

- the returned bias

**Returns:**
- the location within the model that best represents the
given point in the view >= 0. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

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
- a

- the allocated region to render into
- direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST
- SwingConstants.EAST
- SwingConstants.NORTH
- SwingConstants.SOUTH
- biasRet

- an array contain the bias that was checked
- b

- the bias

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

### Additional Sections

#### Class AsyncBoxView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.AsyncBoxView

javax.swing.text.View

- javax.swing.text.AsyncBoxView

javax.swing.text.AsyncBoxView

**All Implemented Interfaces:** SwingConstants

```java
public class
AsyncBoxView

extends
View
```

A box that does layout asynchronously. This
is useful to keep the GUI event thread moving by
not doing any layout on it. The layout is done
on a granularity of operations on the child views.
After each child view is accessed for some part
of layout (a potentially time consuming operation)
the remaining tasks can be abandoned or a new higher
priority task (i.e. to service a synchronous request
or a visible area) can be taken on.

While the child view is being accessed
a read lock is acquired on the associated document
so that the model is stable while being accessed.

**Since:** 1.3

public class

AsyncBoxView

extends

View

A box that does layout asynchronously. This
is useful to keep the GUI event thread moving by
not doing any layout on it. The layout is done
on a granularity of operations on the child views.
After each child view is accessed for some part
of layout (a potentially time consuming operation)
the remaining tasks can be abandoned or a new higher
priority task (i.e. to service a synchronous request
or a visible area) can be taken on.

While the child view is being accessed
a read lock is acquired on the associated document
so that the model is stable while being accessed.

While the child view is being accessed
a read lock is acquired on the associated document
so that the model is stable while being accessed.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

AsyncBoxView.ChildLocator

A class to manage the effective position of the
child views in a localized area while changes are
being made around the localized area.

class

AsyncBoxView.ChildState

A record representing the layout state of a
child view.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

AsyncBoxView.ChildLocator

locator

Object that manages the offsets of the
children.

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

AsyncBoxView

​(

Element

elem,
int axis)

Construct a box view that does asynchronous layout.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AsyncBoxView.ChildState

createChildState

​(

View

v)

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

protected void

flushRequirementChanges

()

Publish the changes in preferences upward to the parent
view.

float

getBottomInset

()

Get the bottom part of the margin around the view.

Shape

getChildAllocation

​(int index,

Shape

a)

Fetches the allocation for the given child view.

protected

AsyncBoxView.ChildState

getChildState

​(int index)

Fetch the object representing the layout state of
of the child at the given index.

protected boolean

getEstimatedMajorSpan

()

Is the major span currently estimated?

protected float

getInsetSpan

​(int axis)

Fetch the span along an axis that is taken up by the insets.

protected

LayoutQueue

getLayoutQueue

()

Fetch the queue to use for layout.

float

getLeftInset

()

Get the left part of the margin around the view.

int

getMajorAxis

()

Fetch the major axis (the axis the children
are tiled along).

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

int

getMinorAxis

()

Fetch the minor axis (the axis orthogonal
to the tiled axis).

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

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

float

getRightInset

()

Get the right part of the margin around the view.

float

getTopInset

()

Get the top part of the margin around the view.

View

getView

​(int n)

Gets the nth child view.

int

getViewCount

()

Returns the number of views in this view.

int

getViewIndex

​(int pos,

Position.Bias

b)

Returns the child view index representing the given position in
the model.

protected int

getViewIndexAtPosition

​(int pos,

Position.Bias

b)

Fetches the child view index representing the given position in
the model.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

protected void

majorRequirementChange

​(

AsyncBoxView.ChildState

cs,
float delta)

Requirements changed along the major axis.

protected void

minorRequirementChange

​(

AsyncBoxView.ChildState

cs)

Requirements changed along the minor axis.

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

alloc)

Render the view using the given allocation and
rendering surface.

void

preferenceChanged

​(

View

child,
boolean width,
boolean height)

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout.

void

replace

​(int offset,
int length,

View

[] views)

Calls the superclass to update the child views, and
updates the status records for the children.

void

setBottomInset

​(float i)

Set the bottom part of the margin around the view.

protected void

setEstimatedMajorSpan

​(boolean isEstimated)

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated.

void

setLeftInset

​(float i)

Set the left part of the margin around the view.

void

setParent

​(

View

parent)

Sets the parent of the view.

void

setRightInset

​(float i)

Set the right part of the margin around the view.

void

setSize

​(float width,
float height)

Sets the size of the view.

void

setTopInset

​(float i)

Set the top part of the margin around the view.

protected void

updateLayout

​(

DocumentEvent.ElementChange

ec,

DocumentEvent

e,

Shape

a)

Update the layout in response to receiving notification of
change from the model.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] biasReturn)

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

getParent

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

AsyncBoxView.ChildLocator

A class to manage the effective position of the
child views in a localized area while changes are
being made around the localized area.

class

AsyncBoxView.ChildState

A record representing the layout state of a
child view.

---

#### Nested Class Summary

A class to manage the effective position of the
child views in a localized area while changes are
being made around the localized area.

A record representing the layout state of a
child view.

Field Summary

Fields

Modifier and Type

Field

Description

protected

AsyncBoxView.ChildLocator

locator

Object that manages the offsets of the
children.

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

Object that manages the offsets of the
children.

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

AsyncBoxView

​(

Element

elem,
int axis)

Construct a box view that does asynchronous layout.

---

#### Constructor Summary

Construct a box view that does asynchronous layout.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AsyncBoxView.ChildState

createChildState

​(

View

v)

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

protected void

flushRequirementChanges

()

Publish the changes in preferences upward to the parent
view.

float

getBottomInset

()

Get the bottom part of the margin around the view.

Shape

getChildAllocation

​(int index,

Shape

a)

Fetches the allocation for the given child view.

protected

AsyncBoxView.ChildState

getChildState

​(int index)

Fetch the object representing the layout state of
of the child at the given index.

protected boolean

getEstimatedMajorSpan

()

Is the major span currently estimated?

protected float

getInsetSpan

​(int axis)

Fetch the span along an axis that is taken up by the insets.

protected

LayoutQueue

getLayoutQueue

()

Fetch the queue to use for layout.

float

getLeftInset

()

Get the left part of the margin around the view.

int

getMajorAxis

()

Fetch the major axis (the axis the children
are tiled along).

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

int

getMinorAxis

()

Fetch the minor axis (the axis orthogonal
to the tiled axis).

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

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

float

getRightInset

()

Get the right part of the margin around the view.

float

getTopInset

()

Get the top part of the margin around the view.

View

getView

​(int n)

Gets the nth child view.

int

getViewCount

()

Returns the number of views in this view.

int

getViewIndex

​(int pos,

Position.Bias

b)

Returns the child view index representing the given position in
the model.

protected int

getViewIndexAtPosition

​(int pos,

Position.Bias

b)

Fetches the child view index representing the given position in
the model.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

protected void

majorRequirementChange

​(

AsyncBoxView.ChildState

cs,
float delta)

Requirements changed along the major axis.

protected void

minorRequirementChange

​(

AsyncBoxView.ChildState

cs)

Requirements changed along the minor axis.

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

alloc)

Render the view using the given allocation and
rendering surface.

void

preferenceChanged

​(

View

child,
boolean width,
boolean height)

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout.

void

replace

​(int offset,
int length,

View

[] views)

Calls the superclass to update the child views, and
updates the status records for the children.

void

setBottomInset

​(float i)

Set the bottom part of the margin around the view.

protected void

setEstimatedMajorSpan

​(boolean isEstimated)

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated.

void

setLeftInset

​(float i)

Set the left part of the margin around the view.

void

setParent

​(

View

parent)

Sets the parent of the view.

void

setRightInset

​(float i)

Set the right part of the margin around the view.

void

setSize

​(float width,
float height)

Sets the size of the view.

void

setTopInset

​(float i)

Set the top part of the margin around the view.

protected void

updateLayout

​(

DocumentEvent.ElementChange

ec,

DocumentEvent

e,

Shape

a)

Update the layout in response to receiving notification of
change from the model.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] biasReturn)

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

getParent

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

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

Publish the changes in preferences upward to the parent
view.

Get the bottom part of the margin around the view.

Fetches the allocation for the given child view.

Fetch the object representing the layout state of
of the child at the given index.

Is the major span currently estimated?

Fetch the span along an axis that is taken up by the insets.

Fetch the queue to use for layout.

Get the left part of the margin around the view.

Fetch the major axis (the axis the children
are tiled along).

Determines the maximum span for this view along an
axis.

Determines the minimum span for this view along an
axis.

Fetch the minor axis (the axis orthogonal
to the tiled axis).

Provides a way to determine the next visually represented model
location that one might place a caret.

Determines the preferred span for this view along an
axis.

Get the right part of the margin around the view.

Get the top part of the margin around the view.

Gets the nth child view.

Returns the number of views in this view.

Returns the child view index representing the given position in
the model.

Fetches the child view index representing the given position in
the model.

Loads all of the children to initialize the view.

Requirements changed along the major axis.

Requirements changed along the minor axis.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Render the view using the given allocation and
rendering surface.

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout.

Calls the superclass to update the child views, and
updates the status records for the children.

Set the bottom part of the margin around the view.

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated.

Set the left part of the margin around the view.

Sets the parent of the view.

Set the right part of the margin around the view.

Sets the size of the view.

Set the top part of the margin around the view.

Update the layout in response to receiving notification of
change from the model.

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

getParent

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

============ FIELD DETAIL ===========

- Field Detail

- locator

```java
protected
AsyncBoxView.ChildLocator
locator
```

Object that manages the offsets of the
children. All locking for management of
child locations is on this object.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AsyncBoxView

```java
public AsyncBoxView​(
Element
elem,
int axis)
```

Construct a box view that does asynchronous layout.

**Parameters:** elem

- the element of the model to represent
**Parameters:** axis

- the axis to tile along. This can be
either X_AXIS or Y_AXIS.

============ METHOD DETAIL ==========

- Method Detail

- getMajorAxis

```java
public int getMajorAxis()
```

Fetch the major axis (the axis the children
are tiled along). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:** the major axis

- getMinorAxis

```java
public int getMinorAxis()
```

Fetch the minor axis (the axis orthogonal
to the tiled axis). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:** the minor axis

- getTopInset

```java
public float getTopInset()
```

Get the top part of the margin around the view.

**Returns:** the top part of the margin around the view

- setTopInset

```java
public void setTopInset​(float i)
```

Set the top part of the margin around the view.

**Parameters:** i

- the value of the inset

- getBottomInset

```java
public float getBottomInset()
```

Get the bottom part of the margin around the view.

**Returns:** the bottom part of the margin around the view

- setBottomInset

```java
public void setBottomInset​(float i)
```

Set the bottom part of the margin around the view.

**Parameters:** i

- the value of the inset

- getLeftInset

```java
public float getLeftInset()
```

Get the left part of the margin around the view.

**Returns:** the left part of the margin around the view

- setLeftInset

```java
public void setLeftInset​(float i)
```

Set the left part of the margin around the view.

**Parameters:** i

- the value of the inset

- getRightInset

```java
public float getRightInset()
```

Get the right part of the margin around the view.

**Returns:** the right part of the margin around the view

- setRightInset

```java
public void setRightInset​(float i)
```

Set the right part of the margin around the view.

**Parameters:** i

- the value of the inset

- getInsetSpan

```java
protected float getInsetSpan​(int axis)
```

Fetch the span along an axis that is taken up by the insets.

**Parameters:** axis

- the axis to determine the total insets along,
either X_AXIS or Y_AXIS.
**Returns:** the span along an axis that is taken up by the insets
**Since:** 1.4

- setEstimatedMajorSpan

```java
protected void setEstimatedMajorSpan​(boolean isEstimated)
```

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated. If this
property is true, the value of setSize along the major axis
will change the requirements along the major axis and incremental
changes will be ignored until all of the children have been updated
(which will cause the property to automatically be set to false).
If the property is false the value of the majorSpan will be
considered to be accurate and incremental changes will be
added into the total as they are calculated.

**Parameters:** isEstimated

- new value for the estimatedMajorSpan property
**Since:** 1.4

- getEstimatedMajorSpan

```java
protected boolean getEstimatedMajorSpan()
```

Is the major span currently estimated?

**Returns:** whether or not the major span currently estimated
**Since:** 1.4

- getChildState

```java
protected
AsyncBoxView.ChildState
getChildState​(int index)
```

Fetch the object representing the layout state of
of the child at the given index.

**Parameters:** index

- the child index. This should be a
value >= 0 and < getViewCount().
**Returns:** the object representing the layout state of
of the child at the given index

- getLayoutQueue

```java
protected
LayoutQueue
getLayoutQueue()
```

Fetch the queue to use for layout.

**Returns:** the queue to use for layout

- createChildState

```java
protected
AsyncBoxView.ChildState
createChildState​(
View
v)
```

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

**Parameters:** v

- the view
**Returns:** new child state

- majorRequirementChange

```java
protected void majorRequirementChange​(
AsyncBoxView.ChildState
cs,
float delta)
```

Requirements changed along the major axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the event thread if it is trying to update
something immediately (such as to perform a
model/view translation).

This is implemented to mark the major axis as having
changed so that a future check to see if the requirements
need to be published to the parent view will consider
the major axis. If the span along the major axis is
not estimated, it is updated by the given delta to reflect
the incremental change. The delta is ignored if the
major span is estimated.

**Parameters:** cs

- the child state
**Parameters:** delta

- the delta

- minorRequirementChange

```java
protected void minorRequirementChange​(
AsyncBoxView.ChildState
cs)
```

Requirements changed along the minor axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the GUI thread if it is trying to update
something immediately (such as to perform a
model/view translation).

**Parameters:** cs

- the child state

- flushRequirementChanges

```java
protected void flushRequirementChanges()
```

Publish the changes in preferences upward to the parent
view. This is normally called by the layout thread.

- replace

```java
public void replace​(int offset,
int length,

View
[] views)
```

Calls the superclass to update the child views, and
updates the status records for the children. This
is expected to be called while a write lock is held
on the model so that interaction with the layout
thread will not happen (i.e. the layout thread
acquires a read lock before doing anything).

**Overrides:** replace

in class

View
**Parameters:** offset

- the starting offset into the child views >= 0
**Parameters:** length

- the number of existing views to replace >= 0
**Parameters:** views

- the child views to insert

- loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

Normally a write-lock is held on the Document while
the children are being changed, which keeps the rendering
and layout threads safe. The exception to this is when
the view is initialized to represent an existing element
(via this method), so it is synchronized to exclude
preferenceChanged while we are initializing.

**Parameters:** f

- the view factory
**See Also:** setParent(javax.swing.text.View)

- getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos,

Position.Bias
b)
```

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Parameters:** b

- the position bias
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

- updateLayout

```java
protected void updateLayout​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a)
```

Update the layout in response to receiving notification of
change from the model. This is implemented to note the
change on the ChildLocator so that offsets of the children
will be correctly computed.

**Overrides:** updateLayout

in class

View
**Parameters:** ec

- changes to the element this view is responsible
for (may be null if there were no changes).
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

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
(to get the hosting Container for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the parent of the view, null if none

- preferenceChanged

```java
public void preferenceChanged​(
View
child,
boolean width,
boolean height)
```

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout. This is reimplemented to queue new work
on the layout thread. This method gets messaged from
multiple threads via the children.

**Overrides:** preferenceChanged

in class

View
**Parameters:** child

- the child view
**Parameters:** width

- true if the width preference has changed
**Parameters:** height

- true if the height preference has changed
**See Also:** JComponent.revalidate()

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information.

Since the major axis is updated asynchronously and should be
the sum of the tiled children the call is ignored for the major
axis. Since the minor axis is flexible, work is queued to resize
the children if the minor span changes.

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
alloc)
```

Render the view using the given allocation and
rendering surface.

This is implemented to determine whether or not the
desired region to be rendered (i.e. the unclipped
area) is up to date or not. If up-to-date the children
are rendered. If not up-to-date, a task to build
the desired area is placed on the layout queue as
a high priority task. This keeps by event thread
moving by rendering if ready, and postponing until
a later time if not ready (since paint requests
can be rescheduled).

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** alloc

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- getViewCount

```java
public int getViewCount()
```

Returns the number of views in this view. Since
the default is to not be a composite view this
returns 0.

**Overrides:** getViewCount

in class

View
**Returns:** the number of views >= 0
**See Also:** View.getViewCount()

- getView

```java
public
View
getView​(int n)
```

Gets the nth child view. Since there are no
children by default, this returns null.

**Overrides:** getView

in class

View
**Parameters:** n

- the number of the view to get, >= 0 && < getViewCount()
**Returns:** the view

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
are located, without assuming the views store
their location. This returns null since the
default is to not have any child views.

**Overrides:** getChildAllocation

in class

View
**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to this view.
**Returns:** the allocation to the child

- getViewIndex

```java
public int getViewIndex​(int pos,

Position.Bias
b)
```

Returns the child view index representing the given position in
the model. By default a view has no children so this is implemented
to return -1 to indicate there is no valid child index for any
position.

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

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views.
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
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

This is expected to be called by the GUI thread, holding a
read-lock on the associated model. It is implemented to
locate the child view and determine it's allocation with a
lock on the ChildLocator object, and to call viewToModel
on the child view with a lock on the ChildState object
to avoid interaction with the layout thread.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** biasReturn

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view >= 0. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

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
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST
- SwingConstants.EAST
- SwingConstants.NORTH
- SwingConstants.SOUTH
**Parameters:** biasRet

- an array contain the bias that was checked
**Parameters:** b

- the bias
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Throws:** IllegalArgumentException

- if

direction

is invalid

Field Detail

- locator

```java
protected
AsyncBoxView.ChildLocator
locator
```

Object that manages the offsets of the
children. All locking for management of
child locations is on this object.

---

#### Field Detail

locator

```java
protected
AsyncBoxView.ChildLocator
locator
```

Object that manages the offsets of the
children. All locking for management of
child locations is on this object.

---

#### locator

protected

AsyncBoxView.ChildLocator

locator

Object that manages the offsets of the
children. All locking for management of
child locations is on this object.

Constructor Detail

- AsyncBoxView

```java
public AsyncBoxView​(
Element
elem,
int axis)
```

Construct a box view that does asynchronous layout.

**Parameters:** elem

- the element of the model to represent
**Parameters:** axis

- the axis to tile along. This can be
either X_AXIS or Y_AXIS.

---

#### Constructor Detail

AsyncBoxView

```java
public AsyncBoxView​(
Element
elem,
int axis)
```

Construct a box view that does asynchronous layout.

**Parameters:** elem

- the element of the model to represent
**Parameters:** axis

- the axis to tile along. This can be
either X_AXIS or Y_AXIS.

---

#### AsyncBoxView

public AsyncBoxView​(

Element

elem,
int axis)

Construct a box view that does asynchronous layout.

Method Detail

- getMajorAxis

```java
public int getMajorAxis()
```

Fetch the major axis (the axis the children
are tiled along). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:** the major axis

- getMinorAxis

```java
public int getMinorAxis()
```

Fetch the minor axis (the axis orthogonal
to the tiled axis). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:** the minor axis

- getTopInset

```java
public float getTopInset()
```

Get the top part of the margin around the view.

**Returns:** the top part of the margin around the view

- setTopInset

```java
public void setTopInset​(float i)
```

Set the top part of the margin around the view.

**Parameters:** i

- the value of the inset

- getBottomInset

```java
public float getBottomInset()
```

Get the bottom part of the margin around the view.

**Returns:** the bottom part of the margin around the view

- setBottomInset

```java
public void setBottomInset​(float i)
```

Set the bottom part of the margin around the view.

**Parameters:** i

- the value of the inset

- getLeftInset

```java
public float getLeftInset()
```

Get the left part of the margin around the view.

**Returns:** the left part of the margin around the view

- setLeftInset

```java
public void setLeftInset​(float i)
```

Set the left part of the margin around the view.

**Parameters:** i

- the value of the inset

- getRightInset

```java
public float getRightInset()
```

Get the right part of the margin around the view.

**Returns:** the right part of the margin around the view

- setRightInset

```java
public void setRightInset​(float i)
```

Set the right part of the margin around the view.

**Parameters:** i

- the value of the inset

- getInsetSpan

```java
protected float getInsetSpan​(int axis)
```

Fetch the span along an axis that is taken up by the insets.

**Parameters:** axis

- the axis to determine the total insets along,
either X_AXIS or Y_AXIS.
**Returns:** the span along an axis that is taken up by the insets
**Since:** 1.4

- setEstimatedMajorSpan

```java
protected void setEstimatedMajorSpan​(boolean isEstimated)
```

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated. If this
property is true, the value of setSize along the major axis
will change the requirements along the major axis and incremental
changes will be ignored until all of the children have been updated
(which will cause the property to automatically be set to false).
If the property is false the value of the majorSpan will be
considered to be accurate and incremental changes will be
added into the total as they are calculated.

**Parameters:** isEstimated

- new value for the estimatedMajorSpan property
**Since:** 1.4

- getEstimatedMajorSpan

```java
protected boolean getEstimatedMajorSpan()
```

Is the major span currently estimated?

**Returns:** whether or not the major span currently estimated
**Since:** 1.4

- getChildState

```java
protected
AsyncBoxView.ChildState
getChildState​(int index)
```

Fetch the object representing the layout state of
of the child at the given index.

**Parameters:** index

- the child index. This should be a
value >= 0 and < getViewCount().
**Returns:** the object representing the layout state of
of the child at the given index

- getLayoutQueue

```java
protected
LayoutQueue
getLayoutQueue()
```

Fetch the queue to use for layout.

**Returns:** the queue to use for layout

- createChildState

```java
protected
AsyncBoxView.ChildState
createChildState​(
View
v)
```

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

**Parameters:** v

- the view
**Returns:** new child state

- majorRequirementChange

```java
protected void majorRequirementChange​(
AsyncBoxView.ChildState
cs,
float delta)
```

Requirements changed along the major axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the event thread if it is trying to update
something immediately (such as to perform a
model/view translation).

This is implemented to mark the major axis as having
changed so that a future check to see if the requirements
need to be published to the parent view will consider
the major axis. If the span along the major axis is
not estimated, it is updated by the given delta to reflect
the incremental change. The delta is ignored if the
major span is estimated.

**Parameters:** cs

- the child state
**Parameters:** delta

- the delta

- minorRequirementChange

```java
protected void minorRequirementChange​(
AsyncBoxView.ChildState
cs)
```

Requirements changed along the minor axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the GUI thread if it is trying to update
something immediately (such as to perform a
model/view translation).

**Parameters:** cs

- the child state

- flushRequirementChanges

```java
protected void flushRequirementChanges()
```

Publish the changes in preferences upward to the parent
view. This is normally called by the layout thread.

- replace

```java
public void replace​(int offset,
int length,

View
[] views)
```

Calls the superclass to update the child views, and
updates the status records for the children. This
is expected to be called while a write lock is held
on the model so that interaction with the layout
thread will not happen (i.e. the layout thread
acquires a read lock before doing anything).

**Overrides:** replace

in class

View
**Parameters:** offset

- the starting offset into the child views >= 0
**Parameters:** length

- the number of existing views to replace >= 0
**Parameters:** views

- the child views to insert

- loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

Normally a write-lock is held on the Document while
the children are being changed, which keeps the rendering
and layout threads safe. The exception to this is when
the view is initialized to represent an existing element
(via this method), so it is synchronized to exclude
preferenceChanged while we are initializing.

**Parameters:** f

- the view factory
**See Also:** setParent(javax.swing.text.View)

- getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos,

Position.Bias
b)
```

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Parameters:** b

- the position bias
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

- updateLayout

```java
protected void updateLayout​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a)
```

Update the layout in response to receiving notification of
change from the model. This is implemented to note the
change on the ChildLocator so that offsets of the children
will be correctly computed.

**Overrides:** updateLayout

in class

View
**Parameters:** ec

- changes to the element this view is responsible
for (may be null if there were no changes).
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

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
(to get the hosting Container for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the parent of the view, null if none

- preferenceChanged

```java
public void preferenceChanged​(
View
child,
boolean width,
boolean height)
```

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout. This is reimplemented to queue new work
on the layout thread. This method gets messaged from
multiple threads via the children.

**Overrides:** preferenceChanged

in class

View
**Parameters:** child

- the child view
**Parameters:** width

- true if the width preference has changed
**Parameters:** height

- true if the height preference has changed
**See Also:** JComponent.revalidate()

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information.

Since the major axis is updated asynchronously and should be
the sum of the tiled children the call is ignored for the major
axis. Since the minor axis is flexible, work is queued to resize
the children if the minor span changes.

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
alloc)
```

Render the view using the given allocation and
rendering surface.

This is implemented to determine whether or not the
desired region to be rendered (i.e. the unclipped
area) is up to date or not. If up-to-date the children
are rendered. If not up-to-date, a task to build
the desired area is placed on the layout queue as
a high priority task. This keeps by event thread
moving by rendering if ready, and postponing until
a later time if not ready (since paint requests
can be rescheduled).

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** alloc

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

- getViewCount

```java
public int getViewCount()
```

Returns the number of views in this view. Since
the default is to not be a composite view this
returns 0.

**Overrides:** getViewCount

in class

View
**Returns:** the number of views >= 0
**See Also:** View.getViewCount()

- getView

```java
public
View
getView​(int n)
```

Gets the nth child view. Since there are no
children by default, this returns null.

**Overrides:** getView

in class

View
**Parameters:** n

- the number of the view to get, >= 0 && < getViewCount()
**Returns:** the view

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
are located, without assuming the views store
their location. This returns null since the
default is to not have any child views.

**Overrides:** getChildAllocation

in class

View
**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to this view.
**Returns:** the allocation to the child

- getViewIndex

```java
public int getViewIndex​(int pos,

Position.Bias
b)
```

Returns the child view index representing the given position in
the model. By default a view has no children so this is implemented
to return -1 to indicate there is no valid child index for any
position.

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

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views.
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
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

This is expected to be called by the GUI thread, holding a
read-lock on the associated model. It is implemented to
locate the child view and determine it's allocation with a
lock on the ChildLocator object, and to call viewToModel
on the child view with a lock on the ChildState object
to avoid interaction with the layout thread.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** biasReturn

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view >= 0. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

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
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST
- SwingConstants.EAST
- SwingConstants.NORTH
- SwingConstants.SOUTH
**Parameters:** biasRet

- an array contain the bias that was checked
**Parameters:** b

- the bias
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

#### Method Detail

getMajorAxis

```java
public int getMajorAxis()
```

Fetch the major axis (the axis the children
are tiled along). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:** the major axis

---

#### getMajorAxis

public int getMajorAxis()

Fetch the major axis (the axis the children
are tiled along). This will have a value of
either X_AXIS or Y_AXIS.

getMinorAxis

```java
public int getMinorAxis()
```

Fetch the minor axis (the axis orthogonal
to the tiled axis). This will have a value of
either X_AXIS or Y_AXIS.

**Returns:** the minor axis

---

#### getMinorAxis

public int getMinorAxis()

Fetch the minor axis (the axis orthogonal
to the tiled axis). This will have a value of
either X_AXIS or Y_AXIS.

getTopInset

```java
public float getTopInset()
```

Get the top part of the margin around the view.

**Returns:** the top part of the margin around the view

---

#### getTopInset

public float getTopInset()

Get the top part of the margin around the view.

setTopInset

```java
public void setTopInset​(float i)
```

Set the top part of the margin around the view.

**Parameters:** i

- the value of the inset

---

#### setTopInset

public void setTopInset​(float i)

Set the top part of the margin around the view.

getBottomInset

```java
public float getBottomInset()
```

Get the bottom part of the margin around the view.

**Returns:** the bottom part of the margin around the view

---

#### getBottomInset

public float getBottomInset()

Get the bottom part of the margin around the view.

setBottomInset

```java
public void setBottomInset​(float i)
```

Set the bottom part of the margin around the view.

**Parameters:** i

- the value of the inset

---

#### setBottomInset

public void setBottomInset​(float i)

Set the bottom part of the margin around the view.

getLeftInset

```java
public float getLeftInset()
```

Get the left part of the margin around the view.

**Returns:** the left part of the margin around the view

---

#### getLeftInset

public float getLeftInset()

Get the left part of the margin around the view.

setLeftInset

```java
public void setLeftInset​(float i)
```

Set the left part of the margin around the view.

**Parameters:** i

- the value of the inset

---

#### setLeftInset

public void setLeftInset​(float i)

Set the left part of the margin around the view.

getRightInset

```java
public float getRightInset()
```

Get the right part of the margin around the view.

**Returns:** the right part of the margin around the view

---

#### getRightInset

public float getRightInset()

Get the right part of the margin around the view.

setRightInset

```java
public void setRightInset​(float i)
```

Set the right part of the margin around the view.

**Parameters:** i

- the value of the inset

---

#### setRightInset

public void setRightInset​(float i)

Set the right part of the margin around the view.

getInsetSpan

```java
protected float getInsetSpan​(int axis)
```

Fetch the span along an axis that is taken up by the insets.

**Parameters:** axis

- the axis to determine the total insets along,
either X_AXIS or Y_AXIS.
**Returns:** the span along an axis that is taken up by the insets
**Since:** 1.4

---

#### getInsetSpan

protected float getInsetSpan​(int axis)

Fetch the span along an axis that is taken up by the insets.

setEstimatedMajorSpan

```java
protected void setEstimatedMajorSpan​(boolean isEstimated)
```

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated. If this
property is true, the value of setSize along the major axis
will change the requirements along the major axis and incremental
changes will be ignored until all of the children have been updated
(which will cause the property to automatically be set to false).
If the property is false the value of the majorSpan will be
considered to be accurate and incremental changes will be
added into the total as they are calculated.

**Parameters:** isEstimated

- new value for the estimatedMajorSpan property
**Since:** 1.4

---

#### setEstimatedMajorSpan

protected void setEstimatedMajorSpan​(boolean isEstimated)

Set the estimatedMajorSpan property that determines if the
major span should be treated as being estimated. If this
property is true, the value of setSize along the major axis
will change the requirements along the major axis and incremental
changes will be ignored until all of the children have been updated
(which will cause the property to automatically be set to false).
If the property is false the value of the majorSpan will be
considered to be accurate and incremental changes will be
added into the total as they are calculated.

getEstimatedMajorSpan

```java
protected boolean getEstimatedMajorSpan()
```

Is the major span currently estimated?

**Returns:** whether or not the major span currently estimated
**Since:** 1.4

---

#### getEstimatedMajorSpan

protected boolean getEstimatedMajorSpan()

Is the major span currently estimated?

getChildState

```java
protected
AsyncBoxView.ChildState
getChildState​(int index)
```

Fetch the object representing the layout state of
of the child at the given index.

**Parameters:** index

- the child index. This should be a
value >= 0 and < getViewCount().
**Returns:** the object representing the layout state of
of the child at the given index

---

#### getChildState

protected

AsyncBoxView.ChildState

getChildState​(int index)

Fetch the object representing the layout state of
of the child at the given index.

getLayoutQueue

```java
protected
LayoutQueue
getLayoutQueue()
```

Fetch the queue to use for layout.

**Returns:** the queue to use for layout

---

#### getLayoutQueue

protected

LayoutQueue

getLayoutQueue()

Fetch the queue to use for layout.

createChildState

```java
protected
AsyncBoxView.ChildState
createChildState​(
View
v)
```

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

**Parameters:** v

- the view
**Returns:** new child state

---

#### createChildState

protected

AsyncBoxView.ChildState

createChildState​(

View

v)

New ChildState records are created through
this method to allow subclasses the extend
the ChildState records to do/hold more.

majorRequirementChange

```java
protected void majorRequirementChange​(
AsyncBoxView.ChildState
cs,
float delta)
```

Requirements changed along the major axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the event thread if it is trying to update
something immediately (such as to perform a
model/view translation).

This is implemented to mark the major axis as having
changed so that a future check to see if the requirements
need to be published to the parent view will consider
the major axis. If the span along the major axis is
not estimated, it is updated by the given delta to reflect
the incremental change. The delta is ignored if the
major span is estimated.

**Parameters:** cs

- the child state
**Parameters:** delta

- the delta

---

#### majorRequirementChange

protected void majorRequirementChange​(

AsyncBoxView.ChildState

cs,
float delta)

Requirements changed along the major axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the event thread if it is trying to update
something immediately (such as to perform a
model/view translation).

This is implemented to mark the major axis as having
changed so that a future check to see if the requirements
need to be published to the parent view will consider
the major axis. If the span along the major axis is
not estimated, it is updated by the given delta to reflect
the incremental change. The delta is ignored if the
major span is estimated.

This is implemented to mark the major axis as having
changed so that a future check to see if the requirements
need to be published to the parent view will consider
the major axis. If the span along the major axis is
not estimated, it is updated by the given delta to reflect
the incremental change. The delta is ignored if the
major span is estimated.

minorRequirementChange

```java
protected void minorRequirementChange​(
AsyncBoxView.ChildState
cs)
```

Requirements changed along the minor axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the GUI thread if it is trying to update
something immediately (such as to perform a
model/view translation).

**Parameters:** cs

- the child state

---

#### minorRequirementChange

protected void minorRequirementChange​(

AsyncBoxView.ChildState

cs)

Requirements changed along the minor axis.
This is called by the thread doing layout for
the given ChildState object when it has completed
fetching the child views new preferences.
Typically this would be the layout thread, but
might be the GUI thread if it is trying to update
something immediately (such as to perform a
model/view translation).

flushRequirementChanges

```java
protected void flushRequirementChanges()
```

Publish the changes in preferences upward to the parent
view. This is normally called by the layout thread.

---

#### flushRequirementChanges

protected void flushRequirementChanges()

Publish the changes in preferences upward to the parent
view. This is normally called by the layout thread.

replace

```java
public void replace​(int offset,
int length,

View
[] views)
```

Calls the superclass to update the child views, and
updates the status records for the children. This
is expected to be called while a write lock is held
on the model so that interaction with the layout
thread will not happen (i.e. the layout thread
acquires a read lock before doing anything).

**Overrides:** replace

in class

View
**Parameters:** offset

- the starting offset into the child views >= 0
**Parameters:** length

- the number of existing views to replace >= 0
**Parameters:** views

- the child views to insert

---

#### replace

public void replace​(int offset,
int length,

View

[] views)

Calls the superclass to update the child views, and
updates the status records for the children. This
is expected to be called while a write lock is held
on the model so that interaction with the layout
thread will not happen (i.e. the layout thread
acquires a read lock before doing anything).

loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

Normally a write-lock is held on the Document while
the children are being changed, which keeps the rendering
and layout threads safe. The exception to this is when
the view is initialized to represent an existing element
(via this method), so it is synchronized to exclude
preferenceChanged while we are initializing.

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

setParent

method. Subclasses can reimplement this to initialize
their child views in a different manner. The default
implementation creates a child view for each
child element.

Normally a write-lock is held on the Document while
the children are being changed, which keeps the rendering
and layout threads safe. The exception to this is when
the view is initialized to represent an existing element
(via this method), so it is synchronized to exclude
preferenceChanged while we are initializing.

Normally a write-lock is held on the Document while
the children are being changed, which keeps the rendering
and layout threads safe. The exception to this is when
the view is initialized to represent an existing element
(via this method), so it is synchronized to exclude
preferenceChanged while we are initializing.

getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos,

Position.Bias
b)
```

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

**Parameters:** pos

- the position >= 0
**Parameters:** b

- the position bias
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

---

#### getViewIndexAtPosition

protected int getViewIndexAtPosition​(int pos,

Position.Bias

b)

Fetches the child view index representing the given position in
the model. This is implemented to fetch the view in the case
where there is a child view for each child element.

updateLayout

```java
protected void updateLayout​(
DocumentEvent.ElementChange
ec,

DocumentEvent
e,

Shape
a)
```

Update the layout in response to receiving notification of
change from the model. This is implemented to note the
change on the ChildLocator so that offsets of the children
will be correctly computed.

**Overrides:** updateLayout

in class

View
**Parameters:** ec

- changes to the element this view is responsible
for (may be null if there were no changes).
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

,

View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### updateLayout

protected void updateLayout​(

DocumentEvent.ElementChange

ec,

DocumentEvent

e,

Shape

a)

Update the layout in response to receiving notification of
change from the model. This is implemented to note the
change on the ChildLocator so that offsets of the children
will be correctly computed.

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
(to get the hosting Container for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the parent of the view, null if none

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
(to get the hosting Container for example).
If this view has children (the view is being moved
from one place in the view hierarchy to another),
the

loadChildren

method will not be called.

preferenceChanged

```java
public void preferenceChanged​(
View
child,
boolean width,
boolean height)
```

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout. This is reimplemented to queue new work
on the layout thread. This method gets messaged from
multiple threads via the children.

**Overrides:** preferenceChanged

in class

View
**Parameters:** child

- the child view
**Parameters:** width

- true if the width preference has changed
**Parameters:** height

- true if the height preference has changed
**See Also:** JComponent.revalidate()

---

#### preferenceChanged

public void preferenceChanged​(

View

child,
boolean width,
boolean height)

Child views can call this on the parent to indicate that
the preference has changed and should be reconsidered
for layout. This is reimplemented to queue new work
on the layout thread. This method gets messaged from
multiple threads via the children.

setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if the view caches any layout
information.

Since the major axis is updated asynchronously and should be
the sum of the tiled children the call is ignored for the major
axis. Since the minor axis is flexible, work is queued to resize
the children if the minor span changes.

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
information.

Since the major axis is updated asynchronously and should be
the sum of the tiled children the call is ignored for the major
axis. Since the minor axis is flexible, work is queued to resize
the children if the minor span changes.

Since the major axis is updated asynchronously and should be
the sum of the tiled children the call is ignored for the major
axis. Since the minor axis is flexible, work is queued to resize
the children if the minor span changes.

paint

```java
public void paint​(
Graphics
g,

Shape
alloc)
```

Render the view using the given allocation and
rendering surface.

This is implemented to determine whether or not the
desired region to be rendered (i.e. the unclipped
area) is up to date or not. If up-to-date the children
are rendered. If not up-to-date, a task to build
the desired area is placed on the layout queue as
a high priority task. This keeps by event thread
moving by rendering if ready, and postponing until
a later time if not ready (since paint requests
can be rescheduled).

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** alloc

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

---

#### paint

public void paint​(

Graphics

g,

Shape

alloc)

Render the view using the given allocation and
rendering surface.

This is implemented to determine whether or not the
desired region to be rendered (i.e. the unclipped
area) is up to date or not. If up-to-date the children
are rendered. If not up-to-date, a task to build
the desired area is placed on the layout queue as
a high priority task. This keeps by event thread
moving by rendering if ready, and postponing until
a later time if not ready (since paint requests
can be rescheduled).

This is implemented to determine whether or not the
desired region to be rendered (i.e. the unclipped
area) is up to date or not. If up-to-date the children
are rendered. If not up-to-date, a task to build
the desired area is placed on the layout queue as
a high priority task. This keeps by event thread
moving by rendering if ready, and postponing until
a later time if not ready (since paint requests
can be rescheduled).

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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
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

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis type
**See Also:** View.getPreferredSpan(int)

---

#### getMaximumSpan

public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis.

getViewCount

```java
public int getViewCount()
```

Returns the number of views in this view. Since
the default is to not be a composite view this
returns 0.

**Overrides:** getViewCount

in class

View
**Returns:** the number of views >= 0
**See Also:** View.getViewCount()

---

#### getViewCount

public int getViewCount()

Returns the number of views in this view. Since
the default is to not be a composite view this
returns 0.

getView

```java
public
View
getView​(int n)
```

Gets the nth child view. Since there are no
children by default, this returns null.

**Overrides:** getView

in class

View
**Parameters:** n

- the number of the view to get, >= 0 && < getViewCount()
**Returns:** the view

---

#### getView

public

View

getView​(int n)

Gets the nth child view. Since there are no
children by default, this returns null.

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
are located, without assuming the views store
their location. This returns null since the
default is to not have any child views.

**Overrides:** getChildAllocation

in class

View
**Parameters:** index

- the index of the child, >= 0 && < getViewCount()
**Parameters:** a

- the allocation to this view.
**Returns:** the allocation to the child

---

#### getChildAllocation

public

Shape

getChildAllocation​(int index,

Shape

a)

Fetches the allocation for the given child view.
This enables finding out where various views
are located, without assuming the views store
their location. This returns null since the
default is to not have any child views.

getViewIndex

```java
public int getViewIndex​(int pos,

Position.Bias
b)
```

Returns the child view index representing the given position in
the model. By default a view has no children so this is implemented
to return -1 to indicate there is no valid child index for any
position.

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

Returns the child view index representing the given position in
the model. By default a view has no children so this is implemented
to return -1 to indicate there is no valid child index for any
position.

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

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views.
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

modelToView​(int pos,

Shape

a,

Position.Bias

b)
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
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

This is expected to be called by the GUI thread, holding a
read-lock on the associated model. It is implemented to
locate the child view and determine it's allocation with a
lock on the ChildLocator object, and to call viewToModel
on the child view with a lock on the ChildState object
to avoid interaction with the layout thread.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** biasReturn

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view >= 0. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

---

#### viewToModel

public int viewToModel​(float x,
float y,

Shape

a,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model. The biasReturn argument will be
filled in to indicate that the point given is closer to the next
character in the model or the previous character in the model.

This is expected to be called by the GUI thread, holding a
read-lock on the associated model. It is implemented to
locate the child view and determine it's allocation with a
lock on the ChildLocator object, and to call viewToModel
on the child view with a lock on the ChildState object
to avoid interaction with the layout thread.

This is expected to be called by the GUI thread, holding a
read-lock on the associated model. It is implemented to
locate the child view and determine it's allocation with a
lock on the ChildLocator object, and to call viewToModel
on the child view with a lock on the ChildState object
to avoid interaction with the layout thread.

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
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard;
this may be one of the following:

- SwingConstants.WEST
- SwingConstants.EAST
- SwingConstants.NORTH
- SwingConstants.SOUTH
**Parameters:** biasRet

- an array contain the bias that was checked
**Parameters:** b

- the bias
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

---

