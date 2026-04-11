# Class IconView

**Source:** `java.desktop\javax\swing\text\IconView.html`

### Class Description

```java
public class
IconView

extends
View
```

Icon decorator that implements the view interface. The
entire element is used to represent the icon. This acts
as a gateway from the display-only View implementations to
interactive lightweight icons (that is, it allows icons
to be embedded into the View hierarchy. The parent of the icon
is the container that is handed out by the associated view
factory.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public IconView​(
Element
elem)

Creates a new icon view that represents an element.

**Parameters:**
- elem

- the element to create a view for

---

### Method Details

#### public void paint​(
Graphics
g,

Shape
a)

Paints the icon.
The real paint behavior occurs naturally from the association
that the icon has with its parent container (the same
container hosting this view), so this simply allows us to
position the icon properly relative to the view. Since
the coordinate system for the view is simply the parent
containers, positioning the child icon is easy.

**Specified by:**
- paint

in class

View

**Parameters:**
- g

- the rendering surface to use
- a

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
- the span the view would like to be rendered into
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**Throws:**
- IllegalArgumentException

- for an invalid axis

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:**
- getAlignment

in class

View

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the desired alignment >= 0.0f && <= 1.0f. This should be
a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

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
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward

**Returns:**
- the bounding box of the given position

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

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
- bias

- the returned bias

**Returns:**
- the location within the model that best represents the
given point of view >= 0

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

### Additional Sections

#### Class IconView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.IconView

javax.swing.text.View

- javax.swing.text.IconView

javax.swing.text.IconView

**All Implemented Interfaces:** SwingConstants

```java
public class
IconView

extends
View
```

Icon decorator that implements the view interface. The
entire element is used to represent the icon. This acts
as a gateway from the display-only View implementations to
interactive lightweight icons (that is, it allows icons
to be embedded into the View hierarchy. The parent of the icon
is the container that is handed out by the associated view
factory.

public class

IconView

extends

View

Icon decorator that implements the view interface. The
entire element is used to represent the icon. This acts
as a gateway from the display-only View implementations to
interactive lightweight icons (that is, it allows icons
to be embedded into the View hierarchy. The parent of the icon
is the container that is handed out by the associated view
factory.

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

IconView

​(

Element

elem)

Creates a new icon view that represents an element.

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

Determines the desired alignment for this view along an
axis.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

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

a)

Paints the icon.

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

getAttributes

,

getBreakWeight

,

getChildAllocation

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

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

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

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setParent

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

IconView

​(

Element

elem)

Creates a new icon view that represents an element.

---

#### Constructor Summary

Creates a new icon view that represents an element.

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

Determines the desired alignment for this view along an
axis.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

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

a)

Paints the icon.

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

getAttributes

,

getBreakWeight

,

getChildAllocation

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

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

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

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setParent

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

Determines the desired alignment for this view along an
axis.

Determines the preferred span for this view along an
axis.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Paints the icon.

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

getAttributes

,

getBreakWeight

,

getChildAllocation

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

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

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

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setParent

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

- IconView

```java
public IconView​(
Element
elem)
```

Creates a new icon view that represents an element.

**Parameters:** elem

- the element to create a view for

============ METHOD DETAIL ==========

- Method Detail

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Paints the icon.
The real paint behavior occurs naturally from the association
that the icon has with its parent container (the same
container hosting this view), so this simply allows us to
position the icon properly relative to the view. Since
the coordinate system for the view is simply the parent
containers, positioning the child icon is easy.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

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
**Returns:** the span the view would like to be rendered into
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment >= 0.0f && <= 1.0f. This should be
a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

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
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
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

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point of view >= 0
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

Constructor Detail

- IconView

```java
public IconView​(
Element
elem)
```

Creates a new icon view that represents an element.

**Parameters:** elem

- the element to create a view for

---

#### Constructor Detail

IconView

```java
public IconView​(
Element
elem)
```

Creates a new icon view that represents an element.

**Parameters:** elem

- the element to create a view for

---

#### IconView

public IconView​(

Element

elem)

Creates a new icon view that represents an element.

Method Detail

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Paints the icon.
The real paint behavior occurs naturally from the association
that the icon has with its parent container (the same
container hosting this view), so this simply allows us to
position the icon properly relative to the view. Since
the coordinate system for the view is simply the parent
containers, positioning the child icon is easy.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

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
**Returns:** the span the view would like to be rendered into
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment >= 0.0f && <= 1.0f. This should be
a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

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
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
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

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point of view >= 0
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### Method Detail

paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Paints the icon.
The real paint behavior occurs naturally from the association
that the icon has with its parent container (the same
container hosting this view), so this simply allows us to
position the icon properly relative to the view. Since
the coordinate system for the view is simply the parent
containers, positioning the child icon is easy.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

---

#### paint

public void paint​(

Graphics

g,

Shape

a)

Paints the icon.
The real paint behavior occurs naturally from the association
that the icon has with its parent container (the same
container hosting this view), so this simply allows us to
position the icon properly relative to the view. Since
the coordinate system for the view is simply the parent
containers, positioning the child icon is easy.

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
**Returns:** the span the view would like to be rendered into
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment >= 0.0f && <= 1.0f. This should be
a value between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

---

#### getAlignment

public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

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
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
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

Position.Bias.Forward

Position.Bias.Backward

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

- the X coordinate >= 0
**Parameters:** y

- the Y coordinate >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point of view >= 0
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

---

