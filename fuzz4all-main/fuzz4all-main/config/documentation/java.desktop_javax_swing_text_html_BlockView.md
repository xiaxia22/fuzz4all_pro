# Class BlockView

**Source:** `java.desktop\javax\swing\text\html\BlockView.html`

### Class Description

```java
public class
BlockView

extends
BoxView
```

A view implementation to display a block (as a box)
with CSS specifications.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public BlockView​(
Element
elem,
int axis)

Creates a new view that represents an
html box. This can be used for a number
of elements.

**Parameters:**
- elem

- the element to create a view for
- axis

- either View.X_AXIS or View.Y_AXIS

---

### Method Details

#### public void setParent​(
View
parent)

Establishes the parent view for this view. This is
guaranteed to be called before any other methods if the
parent view is functioning properly.

This is implemented
to forward to the superclass as well as call the

setPropertiesFromAttributes()

method to set the paragraph properties from the css
attributes. The call is made at this time to ensure
the ability to resolve upward through the parents
view attributes.

**Overrides:**
- setParent

in class

CompositeView

**Parameters:**
- parent

- the new parent, or null if the view is
being removed from a parent it was previously added
to

---

#### protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles). This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

**Overrides:**
- calculateMajorAxisRequirements

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

#### protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).
This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

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

#### protected void layoutMinorAxis​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents). The results
of the layout (the offset and span for each children) are
placed in the given arrays which represent the allocations to
the children along the minor axis.

**Overrides:**
- layoutMinorAxis

in class

BoxView

**Parameters:**
- targetSpan

- the total span given to the view, which
would be used to layout the children.
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

#### public void paint​(
Graphics
g,

Shape
allocation)

Renders using the given rendering surface and area on that
surface. This is implemented to delegate to the css box
painter to paint the border and background prior to the
interior.

**Overrides:**
- paint

in class

BoxView

**Parameters:**
- g

- the rendering surface to use
- allocation

- the allocated region to render into

**See Also:**
- View.paint(java.awt.Graphics, java.awt.Shape)

---

#### public
AttributeSet
getAttributes()

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:**
- getAttributes

in class

View

**Returns:**
- the attributes to use when rendering

---

#### public int getResizeWeight​(int axis)

Gets the resize weight.

**Overrides:**
- getResizeWeight

in class

BoxView

**Parameters:**
- axis

- may be either X_AXIS or Y_AXIS

**Returns:**
- the weight

**Throws:**
- IllegalArgumentException

- for an invalid axis

---

#### public float getAlignment​(int axis)

Gets the alignment.

**Overrides:**
- getAlignment

in class

BoxView

**Parameters:**
- axis

- may be either X_AXIS or Y_AXIS

**Returns:**
- the alignment

---

#### public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

**Overrides:**
- getPreferredSpan

in class

BoxView

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

BoxView

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

BoxView

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

#### protected void setPropertiesFromAttributes()

Update any cached values that come from attributes.

---

#### protected
StyleSheet
getStyleSheet()

Convenient method to get the StyleSheet.

**Returns:**
- the StyleSheet

---

### Additional Sections

#### Class BlockView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.html.BlockView

javax.swing.text.View

- javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.html.BlockView

javax.swing.text.CompositeView

- javax.swing.text.BoxView
- - javax.swing.text.html.BlockView

javax.swing.text.BoxView

- javax.swing.text.html.BlockView

javax.swing.text.html.BlockView

**All Implemented Interfaces:** SwingConstants

**Direct Known Subclasses:** ListView

```java
public class
BlockView

extends
BoxView
```

A view implementation to display a block (as a box)
with CSS specifications.

public class

BlockView

extends

BoxView

A view implementation to display a block (as a box)
with CSS specifications.

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

BlockView

​(

Element

elem,
int axis)

Creates a new view that represents an
html box.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

SizeRequirements

calculateMajorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles).

protected

SizeRequirements

calculateMinorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).

float

getAlignment

​(int axis)

Gets the alignment.

AttributeSet

getAttributes

()

Fetches the attributes to use when rendering.

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

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getResizeWeight

​(int axis)

Gets the resize weight.

protected

StyleSheet

getStyleSheet

()

Convenient method to get the StyleSheet.

protected void

layoutMinorAxis

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents).

void

paint

​(

Graphics

g,

Shape

allocation)

Renders using the given rendering surface and area on that
surface.

void

setParent

​(

View

parent)

Establishes the parent view for this view.

protected void

setPropertiesFromAttributes

()

Update any cached values that come from attributes.

- Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

childAllocation

,

flipEastAndWestAtEnds

,

forwardUpdate

,

getAxis

,

getChildAllocation

,

getHeight

,

getOffset

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

layout

,

layoutChanged

,

layoutMajorAxis

,

modelToView

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

getViewIndexAtPosition

,

loadChildren

,

modelToView

,

setInsets

,

setParagraphInsets

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

BlockView

​(

Element

elem,
int axis)

Creates a new view that represents an
html box.

---

#### Constructor Summary

Creates a new view that represents an
html box.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

SizeRequirements

calculateMajorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles).

protected

SizeRequirements

calculateMinorAxisRequirements

​(int axis,

SizeRequirements

r)

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).

float

getAlignment

​(int axis)

Gets the alignment.

AttributeSet

getAttributes

()

Fetches the attributes to use when rendering.

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

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getResizeWeight

​(int axis)

Gets the resize weight.

protected

StyleSheet

getStyleSheet

()

Convenient method to get the StyleSheet.

protected void

layoutMinorAxis

​(int targetSpan,
int axis,
int[] offsets,
int[] spans)

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents).

void

paint

​(

Graphics

g,

Shape

allocation)

Renders using the given rendering surface and area on that
surface.

void

setParent

​(

View

parent)

Establishes the parent view for this view.

protected void

setPropertiesFromAttributes

()

Update any cached values that come from attributes.

- Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

childAllocation

,

flipEastAndWestAtEnds

,

forwardUpdate

,

getAxis

,

getChildAllocation

,

getHeight

,

getOffset

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

layout

,

layoutChanged

,

layoutMajorAxis

,

modelToView

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

getViewIndexAtPosition

,

loadChildren

,

modelToView

,

setInsets

,

setParagraphInsets

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

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles).

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).

Gets the alignment.

Fetches the attributes to use when rendering.

Determines the maximum span for this view along an
axis.

Determines the minimum span for this view along an
axis.

Determines the preferred span for this view along an
axis.

Gets the resize weight.

Convenient method to get the StyleSheet.

Performs layout for the minor axis of the box (i.e. the
axis orthogonal to the axis that it represents).

Renders using the given rendering surface and area on that
surface.

Establishes the parent view for this view.

Update any cached values that come from attributes.

Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

childAllocation

,

flipEastAndWestAtEnds

,

forwardUpdate

,

getAxis

,

getChildAllocation

,

getHeight

,

getOffset

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

layout

,

layoutChanged

,

layoutMajorAxis

,

modelToView

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

getViewIndexAtPosition

,

loadChildren

,

modelToView

,

setInsets

,

setParagraphInsets

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

- BlockView

```java
public BlockView​(
Element
elem,
int axis)
```

Creates a new view that represents an
html box. This can be used for a number
of elements.

**Parameters:** elem

- the element to create a view for
**Parameters:** axis

- either View.X_AXIS or View.Y_AXIS

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
View
parent)
```

Establishes the parent view for this view. This is
guaranteed to be called before any other methods if the
parent view is functioning properly.

This is implemented
to forward to the superclass as well as call the

setPropertiesFromAttributes()

method to set the paragraph properties from the css
attributes. The call is made at this time to ensure
the ability to resolve upward through the parents
view attributes.

**Overrides:** setParent

in class

CompositeView
**Parameters:** parent

- the new parent, or null if the view is
being removed from a parent it was previously added
to

- calculateMajorAxisRequirements

```java
protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles). This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

**Overrides:** calculateMajorAxisRequirements

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

- calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).
This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

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

**Overrides:** layoutMinorAxis

in class

BoxView
**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children.
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

- paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders using the given rendering surface and area on that
surface. This is implemented to delegate to the css box
painter to paint the border and background prior to the
interior.

**Overrides:** paint

in class

BoxView
**Parameters:** g

- the rendering surface to use
**Parameters:** allocation

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:** getAttributes

in class

View
**Returns:** the attributes to use when rendering

- getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Gets the resize weight.

**Overrides:** getResizeWeight

in class

BoxView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the weight
**Throws:** IllegalArgumentException

- for an invalid axis

- getAlignment

```java
public float getAlignment​(int axis)
```

Gets the alignment.

**Overrides:** getAlignment

in class

BoxView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the alignment

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Overrides:** getPreferredSpan

in class

BoxView
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

BoxView
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

BoxView
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

- setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Update any cached values that come from attributes.

- getStyleSheet

```java
protected
StyleSheet
getStyleSheet()
```

Convenient method to get the StyleSheet.

**Returns:** the StyleSheet

Constructor Detail

- BlockView

```java
public BlockView​(
Element
elem,
int axis)
```

Creates a new view that represents an
html box. This can be used for a number
of elements.

**Parameters:** elem

- the element to create a view for
**Parameters:** axis

- either View.X_AXIS or View.Y_AXIS

---

#### Constructor Detail

BlockView

```java
public BlockView​(
Element
elem,
int axis)
```

Creates a new view that represents an
html box. This can be used for a number
of elements.

**Parameters:** elem

- the element to create a view for
**Parameters:** axis

- either View.X_AXIS or View.Y_AXIS

---

#### BlockView

public BlockView​(

Element

elem,
int axis)

Creates a new view that represents an
html box. This can be used for a number
of elements.

Method Detail

- setParent

```java
public void setParent​(
View
parent)
```

Establishes the parent view for this view. This is
guaranteed to be called before any other methods if the
parent view is functioning properly.

This is implemented
to forward to the superclass as well as call the

setPropertiesFromAttributes()

method to set the paragraph properties from the css
attributes. The call is made at this time to ensure
the ability to resolve upward through the parents
view attributes.

**Overrides:** setParent

in class

CompositeView
**Parameters:** parent

- the new parent, or null if the view is
being removed from a parent it was previously added
to

- calculateMajorAxisRequirements

```java
protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles). This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

**Overrides:** calculateMajorAxisRequirements

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

- calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).
This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

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

**Overrides:** layoutMinorAxis

in class

BoxView
**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children.
**Parameters:** axis

- the axis being layed out
**Parameters:** offsets

- the offsets from the origin of the view for
each of the child views; this is a return value and is
filled in by the implementation of this method
**Parameters:** spans

- the span of each child view; this is a return
value and is filled in by the implementation of this method

- paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders using the given rendering surface and area on that
surface. This is implemented to delegate to the css box
painter to paint the border and background prior to the
interior.

**Overrides:** paint

in class

BoxView
**Parameters:** g

- the rendering surface to use
**Parameters:** allocation

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:** getAttributes

in class

View
**Returns:** the attributes to use when rendering

- getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Gets the resize weight.

**Overrides:** getResizeWeight

in class

BoxView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the weight
**Throws:** IllegalArgumentException

- for an invalid axis

- getAlignment

```java
public float getAlignment​(int axis)
```

Gets the alignment.

**Overrides:** getAlignment

in class

BoxView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the alignment

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Overrides:** getPreferredSpan

in class

BoxView
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

BoxView
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

BoxView
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

- setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Update any cached values that come from attributes.

- getStyleSheet

```java
protected
StyleSheet
getStyleSheet()
```

Convenient method to get the StyleSheet.

**Returns:** the StyleSheet

---

#### Method Detail

setParent

```java
public void setParent​(
View
parent)
```

Establishes the parent view for this view. This is
guaranteed to be called before any other methods if the
parent view is functioning properly.

This is implemented
to forward to the superclass as well as call the

setPropertiesFromAttributes()

method to set the paragraph properties from the css
attributes. The call is made at this time to ensure
the ability to resolve upward through the parents
view attributes.

**Overrides:** setParent

in class

CompositeView
**Parameters:** parent

- the new parent, or null if the view is
being removed from a parent it was previously added
to

---

#### setParent

public void setParent​(

View

parent)

Establishes the parent view for this view. This is
guaranteed to be called before any other methods if the
parent view is functioning properly.

This is implemented
to forward to the superclass as well as call the

setPropertiesFromAttributes()

method to set the paragraph properties from the css
attributes. The call is made at this time to ensure
the ability to resolve upward through the parents
view attributes.

This is implemented
to forward to the superclass as well as call the

setPropertiesFromAttributes()

method to set the paragraph properties from the css
attributes. The call is made at this time to ensure
the ability to resolve upward through the parents
view attributes.

calculateMajorAxisRequirements

```java
protected
SizeRequirements
calculateMajorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles). This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

**Overrides:** calculateMajorAxisRequirements

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

#### calculateMajorAxisRequirements

protected

SizeRequirements

calculateMajorAxisRequirements​(int axis,

SizeRequirements

r)

Calculate the requirements of the block along the major
axis (i.e. the axis along with it tiles). This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

calculateMinorAxisRequirements

```java
protected
SizeRequirements
calculateMinorAxisRequirements​(int axis,

SizeRequirements
r)
```

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).
This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

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

Calculate the requirements of the block along the minor
axis (i.e. the axis orthogonal to the axis along with it tiles).
This is implemented
to provide the superclass behavior and then adjust it if the
CSS width or height attribute is specified and applicable to
the axis.

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

**Overrides:** layoutMinorAxis

in class

BoxView
**Parameters:** targetSpan

- the total span given to the view, which
would be used to layout the children.
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

paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders using the given rendering surface and area on that
surface. This is implemented to delegate to the css box
painter to paint the border and background prior to the
interior.

**Overrides:** paint

in class

BoxView
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

Renders using the given rendering surface and area on that
surface. This is implemented to delegate to the css box
painter to paint the border and background prior to the
interior.

getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:** getAttributes

in class

View
**Returns:** the attributes to use when rendering

---

#### getAttributes

public

AttributeSet

getAttributes()

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Gets the resize weight.

**Overrides:** getResizeWeight

in class

BoxView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the weight
**Throws:** IllegalArgumentException

- for an invalid axis

---

#### getResizeWeight

public int getResizeWeight​(int axis)

Gets the resize weight.

getAlignment

```java
public float getAlignment​(int axis)
```

Gets the alignment.

**Overrides:** getAlignment

in class

BoxView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the alignment

---

#### getAlignment

public float getAlignment​(int axis)

Gets the alignment.

getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Overrides:** getPreferredSpan

in class

BoxView
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

BoxView
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

BoxView
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

setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Update any cached values that come from attributes.

---

#### setPropertiesFromAttributes

protected void setPropertiesFromAttributes()

Update any cached values that come from attributes.

getStyleSheet

```java
protected
StyleSheet
getStyleSheet()
```

Convenient method to get the StyleSheet.

**Returns:** the StyleSheet

---

#### getStyleSheet

protected

StyleSheet

getStyleSheet()

Convenient method to get the StyleSheet.

---

