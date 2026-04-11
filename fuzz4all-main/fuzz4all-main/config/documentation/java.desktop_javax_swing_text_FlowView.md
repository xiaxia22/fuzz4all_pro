# Class FlowView

**Source:** `java.desktop\javax\swing\text\FlowView.html`

### Class Description

```java
public abstract class
FlowView

extends
BoxView
```

A View that tries to flow it's children into some
partially constrained space. This can be used to
build things like paragraphs, pages, etc. The
flow is made up of the following pieces of functionality.

- A logical set of child views, which as used as a
layout pool from which a physical view is formed.

A strategy for translating the logical view to
a physical (flowed) view.

Constraints for the strategy to work against.

A physical structure, that represents the flow.
The children of this view are where the pieces of
of the logical views are placed to create the flow.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

#### protected int layoutSpan

Default constraint against which the flow is
created against.

---

#### protected
View
layoutPool

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view). These are not
directly children of this view. These are either
placed into the rows directly or used for the purpose
of breaking into smaller chunks, to form the physical
view.

---

#### protected
FlowView.FlowStrategy
strategy

The behavior for keeping the flow updated. By
default this is a singleton shared by all instances
of FlowView (FlowStrategy is stateless). Subclasses
can create an alternative strategy, which might keep
state.

---

### Constructor Details

#### public FlowView​(
Element
elem,
int axis)

Constructs a FlowView for the given element.

**Parameters:**
- elem

- the element that this view is responsible for
- axis

- may be either View.X_AXIS or View.Y_AXIS

---

### Method Details

#### public int getFlowAxis()

Fetches the axis along which views should be
flowed. By default, this will be the axis
orthogonal to the axis along which the flow
rows are tiled (the axis of the default flow
rows themselves). This is typically used
by the

FlowStrategy

.

**Returns:**
- the axis along which views should be
flowed

---

#### public int getFlowSpan​(int index)

Fetch the constraining span to flow against for
the given child index. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints. By default, the entire
span inside of the insets along the flow axis
is returned.

**Parameters:**
- index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().

**Returns:**
- the constraining span to flow against for
the given child index

**See Also:**
- getFlowStart(int)

---

#### public int getFlowStart​(int index)

Fetch the location along the flow axis that the
flow span will start at. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints.

**Parameters:**
- index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().

**Returns:**
- the location along the flow axis that the
flow span will start at

**See Also:**
- getFlowSpan(int)

---

#### protected abstract
View
createRow()

Create a View that should be used to hold a
a rows worth of children in a flow. This is
called by the FlowStrategy when new children
are added or removed (i.e. rows are added or
removed) in the process of updating the flow.

**Returns:**
- a View that should be used to hold a
a rows worth of children in a flow

---

#### protected void loadChildren​(
ViewFactory
f)

Loads all of the children to initialize the view.
This is called by the

setParent

method.
This is reimplemented to not load any children directly
(as they are created in the process of formatting).
If the layoutPool variable is null, an instance of
LogicalView is created to represent the logical view
that is used in the process of formatting.

**Overrides:**
- loadChildren

in class

CompositeView

**Parameters:**
- f

- the view factory

**See Also:**
- CompositeView.setParent(javax.swing.text.View)

---

#### protected int getViewIndexAtPosition​(int pos)

Fetches the child view index representing the given position in
the model.

**Overrides:**
- getViewIndexAtPosition

in class

CompositeView

**Parameters:**
- pos

- the position >= 0

**Returns:**
- index of the view representing the given position, or
-1 if no view represents that position

---

#### protected void layout​(int width,
int height)

Lays out the children. If the span along the flow
axis has changed, layout is marked as invalid which
which will cause the superclass behavior to recalculate
the layout along the box axis. The FlowStrategy.layout
method will be called to rebuild the flow rows as
appropriate. If the height of this view changes
(determined by the preferred size along the box axis),
a preferenceChanged is called. Following all of that,
the normal box layout of the superclass is performed.

**Overrides:**
- layout

in class

BoxView

**Parameters:**
- width

- the width to lay out against >= 0. This is
the width inside of the inset area.
- height

- the height to lay out against >= 0 This
is the height inside of the inset area.

---

#### protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)

Calculate requirements along the minor axis. This
is implemented to forward the request to the logical
view by calling getMinimumSpan, getPreferredSpan, and
getMaximumSpan on it.

**Overrides:**
- calculateMinorAxisRequirements

in class

BoxView

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

#### public void insertUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)

Gives notification that something was inserted into the document
in a location that this view is responsible for.

**Overrides:**
- insertUpdate

in class

View

**Parameters:**
- changes

- the change information from the associated document
- a

- the current allocation of the view
- f

- the factory to use to rebuild if the view has children

**See Also:**
- View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### public void removeUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)

Gives notification that something was removed from the document
in a location that this view is responsible for.

**Overrides:**
- removeUpdate

in class

View

**Parameters:**
- changes

- the change information from the associated document
- a

- the current allocation of the view
- f

- the factory to use to rebuild if the view has children

**See Also:**
- View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### public void changedUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:**
- changedUpdate

in class

View

**Parameters:**
- changes

- the change information from the associated document
- a

- the current allocation of the view
- f

- the factory to use to rebuild if the view has children

**See Also:**
- View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

### Additional Sections

#### Class FlowView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.FlowView

javax.swing.text.View

- javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.FlowView

javax.swing.text.CompositeView

- javax.swing.text.BoxView
- - javax.swing.text.FlowView

javax.swing.text.BoxView

- javax.swing.text.FlowView

javax.swing.text.FlowView

**All Implemented Interfaces:** SwingConstants

**Direct Known Subclasses:** ParagraphView

```java
public abstract class
FlowView

extends
BoxView
```

A View that tries to flow it's children into some
partially constrained space. This can be used to
build things like paragraphs, pages, etc. The
flow is made up of the following pieces of functionality.

- A logical set of child views, which as used as a
layout pool from which a physical view is formed.

A strategy for translating the logical view to
a physical (flowed) view.

Constraints for the strategy to work against.

A physical structure, that represents the flow.
The children of this view are where the pieces of
of the logical views are placed to create the flow.

**Since:** 1.3
**See Also:** View

public abstract class

FlowView

extends

BoxView

A View that tries to flow it's children into some
partially constrained space. This can be used to
build things like paragraphs, pages, etc. The
flow is made up of the following pieces of functionality.

- A logical set of child views, which as used as a
layout pool from which a physical view is formed.

A strategy for translating the logical view to
a physical (flowed) view.

Constraints for the strategy to work against.

A physical structure, that represents the flow.
The children of this view are where the pieces of
of the logical views are placed to create the flow.

A logical set of child views, which as used as a
layout pool from which a physical view is formed.

A strategy for translating the logical view to
a physical (flowed) view.

Constraints for the strategy to work against.

A physical structure, that represents the flow.
The children of this view are where the pieces of
of the logical views are placed to create the flow.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

FlowView.FlowStrategy

Strategy for maintaining the physical form
of the flow.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

View

layoutPool

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view).

protected int

layoutSpan

Default constraint against which the flow is
created against.

protected

FlowView.FlowStrategy

strategy

The behavior for keeping the flow updated.

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

FlowView

​(

Element

elem,
int axis)

Constructs a FlowView for the given element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected

SizeRequirements

calculateMinorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculate requirements along the minor axis.

void

changedUpdate

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

protected abstract

View

createRow

()

Create a View that should be used to hold a
a rows worth of children in a flow.

int

getFlowAxis

()

Fetches the axis along which views should be
flowed.

int

getFlowSpan

​(int index)

Fetch the constraining span to flow against for
the given child index.

int

getFlowStart

​(int index)

Fetch the location along the flow axis that the
flow span will start at.

protected int

getViewIndexAtPosition

​(int pos)

Fetches the child view index representing the given position in
the model.

void

insertUpdate

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into the document
in a location that this view is responsible for.

protected void

layout

​(int width,
int height)

Lays out the children.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

void

removeUpdate

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the document
in a location that this view is responsible for.

- Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

calculateMajorAxisRequirements

,

childAllocation

,

flipEastAndWestAtEnds

,

forwardUpdate

,

getAlignment

,

getAxis

,

getChildAllocation

,

getHeight

,

getMaximumSpan

,

getMinimumSpan

,

getOffset

,

getPreferredSpan

,

getResizeWeight

,

getSpan

,

getViewAtPoint

,

getWidth

,

isAfter

,

isAllocationValid

,

isBefore

,

isLayoutValid

,

layoutChanged

,

layoutMajorAxis

,

layoutMinorAxis

,

modelToView

,

paint

,

paintChild

,

preferenceChanged

,

replace

,

setAxis

,

setSize

,

viewToModel

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

isVisible

,

modelToView

,

remove

,

removeAll

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

FlowView.FlowStrategy

Strategy for maintaining the physical form
of the flow.

---

#### Nested Class Summary

Strategy for maintaining the physical form
of the flow.

Field Summary

Fields

Modifier and Type

Field

Description

protected

View

layoutPool

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view).

protected int

layoutSpan

Default constraint against which the flow is
created against.

protected

FlowView.FlowStrategy

strategy

The behavior for keeping the flow updated.

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

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view).

Default constraint against which the flow is
created against.

The behavior for keeping the flow updated.

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

FlowView

​(

Element

elem,
int axis)

Constructs a FlowView for the given element.

---

#### Constructor Summary

Constructs a FlowView for the given element.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected

SizeRequirements

calculateMinorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculate requirements along the minor axis.

void

changedUpdate

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

protected abstract

View

createRow

()

Create a View that should be used to hold a
a rows worth of children in a flow.

int

getFlowAxis

()

Fetches the axis along which views should be
flowed.

int

getFlowSpan

​(int index)

Fetch the constraining span to flow against for
the given child index.

int

getFlowStart

​(int index)

Fetch the location along the flow axis that the
flow span will start at.

protected int

getViewIndexAtPosition

​(int pos)

Fetches the child view index representing the given position in
the model.

void

insertUpdate

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into the document
in a location that this view is responsible for.

protected void

layout

​(int width,
int height)

Lays out the children.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

void

removeUpdate

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the document
in a location that this view is responsible for.

- Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

calculateMajorAxisRequirements

,

childAllocation

,

flipEastAndWestAtEnds

,

forwardUpdate

,

getAlignment

,

getAxis

,

getChildAllocation

,

getHeight

,

getMaximumSpan

,

getMinimumSpan

,

getOffset

,

getPreferredSpan

,

getResizeWeight

,

getSpan

,

getViewAtPoint

,

getWidth

,

isAfter

,

isAllocationValid

,

isBefore

,

isLayoutValid

,

layoutChanged

,

layoutMajorAxis

,

layoutMinorAxis

,

modelToView

,

paint

,

paintChild

,

preferenceChanged

,

replace

,

setAxis

,

setSize

,

viewToModel

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

isVisible

,

modelToView

,

remove

,

removeAll

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

Calculate requirements along the minor axis.

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Create a View that should be used to hold a
a rows worth of children in a flow.

Fetches the axis along which views should be
flowed.

Fetch the constraining span to flow against for
the given child index.

Fetch the location along the flow axis that the
flow span will start at.

Fetches the child view index representing the given position in
the model.

Gives notification that something was inserted into the document
in a location that this view is responsible for.

Lays out the children.

Loads all of the children to initialize the view.

Gives notification that something was removed from the document
in a location that this view is responsible for.

Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

calculateMajorAxisRequirements

,

childAllocation

,

flipEastAndWestAtEnds

,

forwardUpdate

,

getAlignment

,

getAxis

,

getChildAllocation

,

getHeight

,

getMaximumSpan

,

getMinimumSpan

,

getOffset

,

getPreferredSpan

,

getResizeWeight

,

getSpan

,

getViewAtPoint

,

getWidth

,

isAfter

,

isAllocationValid

,

isBefore

,

isLayoutValid

,

layoutChanged

,

layoutMajorAxis

,

layoutMinorAxis

,

modelToView

,

paint

,

paintChild

,

preferenceChanged

,

replace

,

setAxis

,

setSize

,

viewToModel

---

#### Methods declared in class javax.swing.text. BoxView

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

isVisible

,

modelToView

,

remove

,

removeAll

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

============ FIELD DETAIL ===========

- Field Detail

- layoutSpan

```java
protected int layoutSpan
```

Default constraint against which the flow is
created against.

- layoutPool

```java
protected
View
layoutPool
```

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view). These are not
directly children of this view. These are either
placed into the rows directly or used for the purpose
of breaking into smaller chunks, to form the physical
view.

- strategy

```java
protected
FlowView.FlowStrategy
strategy
```

The behavior for keeping the flow updated. By
default this is a singleton shared by all instances
of FlowView (FlowStrategy is stateless). Subclasses
can create an alternative strategy, which might keep
state.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FlowView

```java
public FlowView​(
Element
elem,
int axis)
```

Constructs a FlowView for the given element.

**Parameters:** elem

- the element that this view is responsible for
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS

============ METHOD DETAIL ==========

- Method Detail

- getFlowAxis

```java
public int getFlowAxis()
```

Fetches the axis along which views should be
flowed. By default, this will be the axis
orthogonal to the axis along which the flow
rows are tiled (the axis of the default flow
rows themselves). This is typically used
by the

FlowStrategy

.

**Returns:** the axis along which views should be
flowed

- getFlowSpan

```java
public int getFlowSpan​(int index)
```

Fetch the constraining span to flow against for
the given child index. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints. By default, the entire
span inside of the insets along the flow axis
is returned.

**Parameters:** index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().
**Returns:** the constraining span to flow against for
the given child index
**See Also:** getFlowStart(int)

- getFlowStart

```java
public int getFlowStart​(int index)
```

Fetch the location along the flow axis that the
flow span will start at. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints.

**Parameters:** index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().
**Returns:** the location along the flow axis that the
flow span will start at
**See Also:** getFlowSpan(int)

- createRow

```java
protected abstract
View
createRow()
```

Create a View that should be used to hold a
a rows worth of children in a flow. This is
called by the FlowStrategy when new children
are added or removed (i.e. rows are added or
removed) in the process of updating the flow.

**Returns:** a View that should be used to hold a
a rows worth of children in a flow

- loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent

method.
This is reimplemented to not load any children directly
(as they are created in the process of formatting).
If the layoutPool variable is null, an instance of
LogicalView is created to represent the logical view
that is used in the process of formatting.

**Overrides:** loadChildren

in class

CompositeView
**Parameters:** f

- the view factory
**See Also:** CompositeView.setParent(javax.swing.text.View)

- getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos)
```

Fetches the child view index representing the given position in
the model.

**Overrides:** getViewIndexAtPosition

in class

CompositeView
**Parameters:** pos

- the position >= 0
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

- layout

```java
protected void layout​(int width,
int height)
```

Lays out the children. If the span along the flow
axis has changed, layout is marked as invalid which
which will cause the superclass behavior to recalculate
the layout along the box axis. The FlowStrategy.layout
method will be called to rebuild the flow rows as
appropriate. If the height of this view changes
(determined by the preferred size along the box axis),
a preferenceChanged is called. Following all of that,
the normal box layout of the superclass is performed.

**Overrides:** layout

in class

BoxView
**Parameters:** width

- the width to lay out against >= 0. This is
the width inside of the inset area.
**Parameters:** height

- the height to lay out against >= 0 This
is the height inside of the inset area.

- calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate requirements along the minor axis. This
is implemented to forward the request to the logical
view by calling getMinimumSpan, getPreferredSpan, and
getMaximumSpan on it.

**Overrides:** calculateMinorAxisRequirements

in class

BoxView
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

- insertUpdate

```java
public void insertUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification that something was inserted into the document
in a location that this view is responsible for.

**Overrides:** insertUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- removeUpdate

```java
public void removeUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification that something was removed from the document
in a location that this view is responsible for.

**Overrides:** removeUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- changedUpdate

```java
public void changedUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:** changedUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

Field Detail

- layoutSpan

```java
protected int layoutSpan
```

Default constraint against which the flow is
created against.

- layoutPool

```java
protected
View
layoutPool
```

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view). These are not
directly children of this view. These are either
placed into the rows directly or used for the purpose
of breaking into smaller chunks, to form the physical
view.

- strategy

```java
protected
FlowView.FlowStrategy
strategy
```

The behavior for keeping the flow updated. By
default this is a singleton shared by all instances
of FlowView (FlowStrategy is stateless). Subclasses
can create an alternative strategy, which might keep
state.

---

#### Field Detail

layoutSpan

```java
protected int layoutSpan
```

Default constraint against which the flow is
created against.

---

#### layoutSpan

protected int layoutSpan

Default constraint against which the flow is
created against.

layoutPool

```java
protected
View
layoutPool
```

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view). These are not
directly children of this view. These are either
placed into the rows directly or used for the purpose
of breaking into smaller chunks, to form the physical
view.

---

#### layoutPool

protected

View

layoutPool

These are the views that represent the child elements
of the element this view represents (The logical view
to translate to a physical view). These are not
directly children of this view. These are either
placed into the rows directly or used for the purpose
of breaking into smaller chunks, to form the physical
view.

strategy

```java
protected
FlowView.FlowStrategy
strategy
```

The behavior for keeping the flow updated. By
default this is a singleton shared by all instances
of FlowView (FlowStrategy is stateless). Subclasses
can create an alternative strategy, which might keep
state.

---

#### strategy

protected

FlowView.FlowStrategy

strategy

The behavior for keeping the flow updated. By
default this is a singleton shared by all instances
of FlowView (FlowStrategy is stateless). Subclasses
can create an alternative strategy, which might keep
state.

Constructor Detail

- FlowView

```java
public FlowView​(
Element
elem,
int axis)
```

Constructs a FlowView for the given element.

**Parameters:** elem

- the element that this view is responsible for
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS

---

#### Constructor Detail

FlowView

```java
public FlowView​(
Element
elem,
int axis)
```

Constructs a FlowView for the given element.

**Parameters:** elem

- the element that this view is responsible for
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS

---

#### FlowView

public FlowView​(

Element

elem,
int axis)

Constructs a FlowView for the given element.

Method Detail

- getFlowAxis

```java
public int getFlowAxis()
```

Fetches the axis along which views should be
flowed. By default, this will be the axis
orthogonal to the axis along which the flow
rows are tiled (the axis of the default flow
rows themselves). This is typically used
by the

FlowStrategy

.

**Returns:** the axis along which views should be
flowed

- getFlowSpan

```java
public int getFlowSpan​(int index)
```

Fetch the constraining span to flow against for
the given child index. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints. By default, the entire
span inside of the insets along the flow axis
is returned.

**Parameters:** index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().
**Returns:** the constraining span to flow against for
the given child index
**See Also:** getFlowStart(int)

- getFlowStart

```java
public int getFlowStart​(int index)
```

Fetch the location along the flow axis that the
flow span will start at. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints.

**Parameters:** index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().
**Returns:** the location along the flow axis that the
flow span will start at
**See Also:** getFlowSpan(int)

- createRow

```java
protected abstract
View
createRow()
```

Create a View that should be used to hold a
a rows worth of children in a flow. This is
called by the FlowStrategy when new children
are added or removed (i.e. rows are added or
removed) in the process of updating the flow.

**Returns:** a View that should be used to hold a
a rows worth of children in a flow

- loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent

method.
This is reimplemented to not load any children directly
(as they are created in the process of formatting).
If the layoutPool variable is null, an instance of
LogicalView is created to represent the logical view
that is used in the process of formatting.

**Overrides:** loadChildren

in class

CompositeView
**Parameters:** f

- the view factory
**See Also:** CompositeView.setParent(javax.swing.text.View)

- getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos)
```

Fetches the child view index representing the given position in
the model.

**Overrides:** getViewIndexAtPosition

in class

CompositeView
**Parameters:** pos

- the position >= 0
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

- layout

```java
protected void layout​(int width,
int height)
```

Lays out the children. If the span along the flow
axis has changed, layout is marked as invalid which
which will cause the superclass behavior to recalculate
the layout along the box axis. The FlowStrategy.layout
method will be called to rebuild the flow rows as
appropriate. If the height of this view changes
(determined by the preferred size along the box axis),
a preferenceChanged is called. Following all of that,
the normal box layout of the superclass is performed.

**Overrides:** layout

in class

BoxView
**Parameters:** width

- the width to lay out against >= 0. This is
the width inside of the inset area.
**Parameters:** height

- the height to lay out against >= 0 This
is the height inside of the inset area.

- calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate requirements along the minor axis. This
is implemented to forward the request to the logical
view by calling getMinimumSpan, getPreferredSpan, and
getMaximumSpan on it.

**Overrides:** calculateMinorAxisRequirements

in class

BoxView
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

- insertUpdate

```java
public void insertUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification that something was inserted into the document
in a location that this view is responsible for.

**Overrides:** insertUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- removeUpdate

```java
public void removeUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification that something was removed from the document
in a location that this view is responsible for.

**Overrides:** removeUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- changedUpdate

```java
public void changedUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:** changedUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### Method Detail

getFlowAxis

```java
public int getFlowAxis()
```

Fetches the axis along which views should be
flowed. By default, this will be the axis
orthogonal to the axis along which the flow
rows are tiled (the axis of the default flow
rows themselves). This is typically used
by the

FlowStrategy

.

**Returns:** the axis along which views should be
flowed

---

#### getFlowAxis

public int getFlowAxis()

Fetches the axis along which views should be
flowed. By default, this will be the axis
orthogonal to the axis along which the flow
rows are tiled (the axis of the default flow
rows themselves). This is typically used
by the

FlowStrategy

.

getFlowSpan

```java
public int getFlowSpan​(int index)
```

Fetch the constraining span to flow against for
the given child index. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints. By default, the entire
span inside of the insets along the flow axis
is returned.

**Parameters:** index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().
**Returns:** the constraining span to flow against for
the given child index
**See Also:** getFlowStart(int)

---

#### getFlowSpan

public int getFlowSpan​(int index)

Fetch the constraining span to flow against for
the given child index. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints. By default, the entire
span inside of the insets along the flow axis
is returned.

getFlowStart

```java
public int getFlowStart​(int index)
```

Fetch the location along the flow axis that the
flow span will start at. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints.

**Parameters:** index

- the index of the row being updated.
This should be a value >= 0 and < getViewCount().
**Returns:** the location along the flow axis that the
flow span will start at
**See Also:** getFlowSpan(int)

---

#### getFlowStart

public int getFlowStart​(int index)

Fetch the location along the flow axis that the
flow span will start at. This is called by the
FlowStrategy while it is updating the flow.
A flow can be shaped by providing different values
for the row constraints.

createRow

```java
protected abstract
View
createRow()
```

Create a View that should be used to hold a
a rows worth of children in a flow. This is
called by the FlowStrategy when new children
are added or removed (i.e. rows are added or
removed) in the process of updating the flow.

**Returns:** a View that should be used to hold a
a rows worth of children in a flow

---

#### createRow

protected abstract

View

createRow()

Create a View that should be used to hold a
a rows worth of children in a flow. This is
called by the FlowStrategy when new children
are added or removed (i.e. rows are added or
removed) in the process of updating the flow.

loadChildren

```java
protected void loadChildren​(
ViewFactory
f)
```

Loads all of the children to initialize the view.
This is called by the

setParent

method.
This is reimplemented to not load any children directly
(as they are created in the process of formatting).
If the layoutPool variable is null, an instance of
LogicalView is created to represent the logical view
that is used in the process of formatting.

**Overrides:** loadChildren

in class

CompositeView
**Parameters:** f

- the view factory
**See Also:** CompositeView.setParent(javax.swing.text.View)

---

#### loadChildren

protected void loadChildren​(

ViewFactory

f)

Loads all of the children to initialize the view.
This is called by the

setParent

method.
This is reimplemented to not load any children directly
(as they are created in the process of formatting).
If the layoutPool variable is null, an instance of
LogicalView is created to represent the logical view
that is used in the process of formatting.

getViewIndexAtPosition

```java
protected int getViewIndexAtPosition​(int pos)
```

Fetches the child view index representing the given position in
the model.

**Overrides:** getViewIndexAtPosition

in class

CompositeView
**Parameters:** pos

- the position >= 0
**Returns:** index of the view representing the given position, or
-1 if no view represents that position

---

#### getViewIndexAtPosition

protected int getViewIndexAtPosition​(int pos)

Fetches the child view index representing the given position in
the model.

layout

```java
protected void layout​(int width,
int height)
```

Lays out the children. If the span along the flow
axis has changed, layout is marked as invalid which
which will cause the superclass behavior to recalculate
the layout along the box axis. The FlowStrategy.layout
method will be called to rebuild the flow rows as
appropriate. If the height of this view changes
(determined by the preferred size along the box axis),
a preferenceChanged is called. Following all of that,
the normal box layout of the superclass is performed.

**Overrides:** layout

in class

BoxView
**Parameters:** width

- the width to lay out against >= 0. This is
the width inside of the inset area.
**Parameters:** height

- the height to lay out against >= 0 This
is the height inside of the inset area.

---

#### layout

protected void layout​(int width,
int height)

Lays out the children. If the span along the flow
axis has changed, layout is marked as invalid which
which will cause the superclass behavior to recalculate
the layout along the box axis. The FlowStrategy.layout
method will be called to rebuild the flow rows as
appropriate. If the height of this view changes
(determined by the preferred size along the box axis),
a preferenceChanged is called. Following all of that,
the normal box layout of the superclass is performed.

calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate requirements along the minor axis. This
is implemented to forward the request to the logical
view by calling getMinimumSpan, getPreferredSpan, and
getMaximumSpan on it.

**Overrides:** calculateMinorAxisRequirements

in class

BoxView
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

Calculate requirements along the minor axis. This
is implemented to forward the request to the logical
view by calling getMinimumSpan, getPreferredSpan, and
getMaximumSpan on it.

insertUpdate

```java
public void insertUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification that something was inserted into the document
in a location that this view is responsible for.

**Overrides:** insertUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### insertUpdate

public void insertUpdate​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into the document
in a location that this view is responsible for.

removeUpdate

```java
public void removeUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification that something was removed from the document
in a location that this view is responsible for.

**Overrides:** removeUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### removeUpdate

public void removeUpdate​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the document
in a location that this view is responsible for.

changedUpdate

```java
public void changedUpdate​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:** changedUpdate

in class

View
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### changedUpdate

public void changedUpdate​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

---

