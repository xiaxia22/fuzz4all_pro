# Class ListView

**Source:** `java.desktop\javax\swing\text\html\ListView.html`

### Class Description

```java
public class
ListView

extends
BlockView
```

A view implementation to display an html list

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public ListView​(
Element
elem)

Creates a new view that represents a list element.

**Parameters:**
- elem

- the element to create a view for

---

### Method Details

#### public float getAlignment​(int axis)

Calculates the desired shape of the list.

**Overrides:**
- getAlignment

in class

BlockView

**Parameters:**
- axis

- may be either X_AXIS or Y_AXIS

**Returns:**
- the desired span

**See Also:**
- View.getPreferredSpan(int)

---

#### public void paint​(
Graphics
g,

Shape
allocation)

Renders using the given rendering surface and area on that
surface.

**Overrides:**
- paint

in class

BlockView

**Parameters:**
- g

- the rendering surface to use
- allocation

- the allocated region to render into

**See Also:**
- View.paint(java.awt.Graphics, java.awt.Shape)

---

#### protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)

Paints one of the children; called by paint(). By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Overrides:**
- paintChild

in class

BoxView

**Parameters:**
- g

- the graphics context
- alloc

- the allocated region to render the child into
- index

- the index of the child

---

### Additional Sections

#### Class ListView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.html.BlockView
- - javax.swing.text.html.ListView

javax.swing.text.View

- javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.html.BlockView
- - javax.swing.text.html.ListView

javax.swing.text.CompositeView

- javax.swing.text.BoxView
- - javax.swing.text.html.BlockView
- - javax.swing.text.html.ListView

javax.swing.text.BoxView

- javax.swing.text.html.BlockView
- - javax.swing.text.html.ListView

javax.swing.text.html.BlockView

- javax.swing.text.html.ListView

javax.swing.text.html.ListView

**All Implemented Interfaces:** SwingConstants

```java
public class
ListView

extends
BlockView
```

A view implementation to display an html list

public class

ListView

extends

BlockView

A view implementation to display an html list

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

ListView

​(

Element

elem)

Creates a new view that represents a list element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getAlignment

​(int axis)

Calculates the desired shape of the list.

void

paint

​(

Graphics

g,

Shape

allocation)

Renders using the given rendering surface and area on that
surface.

protected void

paintChild

​(

Graphics

g,

Rectangle

alloc,
int index)

Paints one of the children; called by paint().

- Methods declared in class javax.swing.text.html.

BlockView

calculateMajorAxisRequirements

,

calculateMinorAxisRequirements

,

getAttributes

,

getMaximumSpan

,

getMinimumSpan

,

getPreferredSpan

,

getResizeWeight

,

getStyleSheet

,

layoutMinorAxis

,

setParent

,

setPropertiesFromAttributes

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

ListView

​(

Element

elem)

Creates a new view that represents a list element.

---

#### Constructor Summary

Creates a new view that represents a list element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getAlignment

​(int axis)

Calculates the desired shape of the list.

void

paint

​(

Graphics

g,

Shape

allocation)

Renders using the given rendering surface and area on that
surface.

protected void

paintChild

​(

Graphics

g,

Rectangle

alloc,
int index)

Paints one of the children; called by paint().

- Methods declared in class javax.swing.text.html.

BlockView

calculateMajorAxisRequirements

,

calculateMinorAxisRequirements

,

getAttributes

,

getMaximumSpan

,

getMinimumSpan

,

getPreferredSpan

,

getResizeWeight

,

getStyleSheet

,

layoutMinorAxis

,

setParent

,

setPropertiesFromAttributes

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

Calculates the desired shape of the list.

Renders using the given rendering surface and area on that
surface.

Paints one of the children; called by paint().

Methods declared in class javax.swing.text.html.

BlockView

calculateMajorAxisRequirements

,

calculateMinorAxisRequirements

,

getAttributes

,

getMaximumSpan

,

getMinimumSpan

,

getPreferredSpan

,

getResizeWeight

,

getStyleSheet

,

layoutMinorAxis

,

setParent

,

setPropertiesFromAttributes

---

#### Methods declared in class javax.swing.text.html. BlockView

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

- ListView

```java
public ListView​(
Element
elem)
```

Creates a new view that represents a list element.

**Parameters:** elem

- the element to create a view for

============ METHOD DETAIL ==========

- Method Detail

- getAlignment

```java
public float getAlignment​(int axis)
```

Calculates the desired shape of the list.

**Overrides:** getAlignment

in class

BlockView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the desired span
**See Also:** View.getPreferredSpan(int)

- paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders using the given rendering surface and area on that
surface.

**Overrides:** paint

in class

BlockView
**Parameters:** g

- the rendering surface to use
**Parameters:** allocation

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- paintChild

```java
protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)
```

Paints one of the children; called by paint(). By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Overrides:** paintChild

in class

BoxView
**Parameters:** g

- the graphics context
**Parameters:** alloc

- the allocated region to render the child into
**Parameters:** index

- the index of the child

Constructor Detail

- ListView

```java
public ListView​(
Element
elem)
```

Creates a new view that represents a list element.

**Parameters:** elem

- the element to create a view for

---

#### Constructor Detail

ListView

```java
public ListView​(
Element
elem)
```

Creates a new view that represents a list element.

**Parameters:** elem

- the element to create a view for

---

#### ListView

public ListView​(

Element

elem)

Creates a new view that represents a list element.

Method Detail

- getAlignment

```java
public float getAlignment​(int axis)
```

Calculates the desired shape of the list.

**Overrides:** getAlignment

in class

BlockView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the desired span
**See Also:** View.getPreferredSpan(int)

- paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders using the given rendering surface and area on that
surface.

**Overrides:** paint

in class

BlockView
**Parameters:** g

- the rendering surface to use
**Parameters:** allocation

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- paintChild

```java
protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)
```

Paints one of the children; called by paint(). By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Overrides:** paintChild

in class

BoxView
**Parameters:** g

- the graphics context
**Parameters:** alloc

- the allocated region to render the child into
**Parameters:** index

- the index of the child

---

#### Method Detail

getAlignment

```java
public float getAlignment​(int axis)
```

Calculates the desired shape of the list.

**Overrides:** getAlignment

in class

BlockView
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the desired span
**See Also:** View.getPreferredSpan(int)

---

#### getAlignment

public float getAlignment​(int axis)

Calculates the desired shape of the list.

paint

```java
public void paint​(
Graphics
g,

Shape
allocation)
```

Renders using the given rendering surface and area on that
surface.

**Overrides:** paint

in class

BlockView
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
surface.

paintChild

```java
protected void paintChild​(
Graphics
g,

Rectangle
alloc,
int index)
```

Paints one of the children; called by paint(). By default
that is all it does, but a subclass can use this to paint
things relative to the child.

**Overrides:** paintChild

in class

BoxView
**Parameters:** g

- the graphics context
**Parameters:** alloc

- the allocated region to render the child into
**Parameters:** index

- the index of the child

---

#### paintChild

protected void paintChild​(

Graphics

g,

Rectangle

alloc,
int index)

Paints one of the children; called by paint(). By default
that is all it does, but a subclass can use this to paint
things relative to the child.

---

