# Class FieldView

**Source:** `java.desktop\javax\swing\text\FieldView.html`

### Class Description

```java
public class
FieldView

extends
PlainView
```

Extends the multi-line plain text view to be suitable
for a single-line editor view. If the view is
allocated extra space, the field must adjust for it.
If the hosting component is a JTextField, this view
will manage the ranges of the associated BoundedRangeModel
and will adjust the horizontal allocation to match the
current visibility settings of the JTextField.

**All Implemented Interfaces:** SwingConstants

,

TabExpander

---

### Field Details

*No entries found.*

### Constructor Details

#### public FieldView​(
Element
elem)

Constructs a new FieldView wrapped on an element.

**Parameters:**
- elem

- the element

---

### Method Details

#### protected
FontMetrics
getFontMetrics()

Fetches the font metrics associated with the component hosting
this view.

**Returns:**
- the metrics

---

#### protected
Shape
adjustAllocation​(
Shape
a)

Adjusts the allocation given to the view
to be a suitable allocation for a text field.
If the view has been allocated more than the
preferred span vertically, the allocation is
changed to be centered vertically. Horizontally
the view is adjusted according to the horizontal
alignment property set on the associated JTextField
(if that is the type of the hosting component).

**Parameters:**
- a

- the allocation given to the view, which may need
to be adjusted.

**Returns:**
- the allocation that the superclass should use.

---

#### public void paint​(
Graphics
g,

Shape
a)

Renders using the given rendering surface and area on that surface.
The view may need to do layout and create child views to enable
itself to render into the given allocation.

**Overrides:**
- paint

in class

PlainView

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

**Overrides:**
- getPreferredSpan

in class

PlainView

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**See Also:**
- View.getPreferredSpan(int)

---

#### public int getResizeWeight​(int axis)

Determines the resizability of the view along the
given axis. A value of 0 or less is not resizable.

**Overrides:**
- getResizeWeight

in class

View

**Parameters:**
- axis

- View.X_AXIS or View.Y_AXIS

**Returns:**
- the weight -> 1 for View.X_AXIS, else 0

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

**Overrides:**
- modelToView

in class

PlainView

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

#### public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:**
- viewToModel

in class

PlainView

**Parameters:**
- fx

- the X coordinate >= 0.0f
- fy

- the Y coordinate >= 0.0f
- a

- the allocated region to render into
- bias

- the returned bias

**Returns:**
- the location within the model that best represents the
given point in the view

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

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

PlainView

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

PlainView

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

### Additional Sections

#### Class FieldView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.PlainView
- - javax.swing.text.FieldView

javax.swing.text.View

- javax.swing.text.PlainView
- - javax.swing.text.FieldView

javax.swing.text.PlainView

- javax.swing.text.FieldView

javax.swing.text.FieldView

**All Implemented Interfaces:** SwingConstants

,

TabExpander

**Direct Known Subclasses:** PasswordView

```java
public class
FieldView

extends
PlainView
```

Extends the multi-line plain text view to be suitable
for a single-line editor view. If the view is
allocated extra space, the field must adjust for it.
If the hosting component is a JTextField, this view
will manage the ranges of the associated BoundedRangeModel
and will adjust the horizontal allocation to match the
current visibility settings of the JTextField.

**See Also:** View

public class

FieldView

extends

PlainView

Extends the multi-line plain text view to be suitable
for a single-line editor view. If the view is
allocated extra space, the field must adjust for it.
If the hosting component is a JTextField, this view
will manage the ranges of the associated BoundedRangeModel
and will adjust the horizontal allocation to match the
current visibility settings of the JTextField.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

PlainView

metrics

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

FieldView

​(

Element

elem)

Constructs a new FieldView wrapped on an element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Shape

adjustAllocation

​(

Shape

a)

Adjusts the allocation given to the view
to be a suitable allocation for a text field.

protected

FontMetrics

getFontMetrics

()

Fetches the font metrics associated with the component hosting
this view.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getResizeWeight

​(int axis)

Determines the resizability of the view along the
given axis.

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

Renders using the given rendering surface and area on that surface.

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

int

viewToModel

​(float fx,
float fy,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

PlainView

changedUpdate

,

damageLineRange

,

drawLine

,

drawLine

,

drawSelectedText

,

drawSelectedText

,

drawUnselectedText

,

drawUnselectedText

,

getLineBuffer

,

getTabSize

,

lineToRect

,

nextTabStop

,

setSize

,

updateDamage

,

updateMetrics

- Methods declared in class javax.swing.text.

View

append

,

breakView

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

replace

,

setParent

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

PlainView

metrics

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

PlainView

metrics

---

#### Fields declared in class javax.swing.text. PlainView

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

FieldView

​(

Element

elem)

Constructs a new FieldView wrapped on an element.

---

#### Constructor Summary

Constructs a new FieldView wrapped on an element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Shape

adjustAllocation

​(

Shape

a)

Adjusts the allocation given to the view
to be a suitable allocation for a text field.

protected

FontMetrics

getFontMetrics

()

Fetches the font metrics associated with the component hosting
this view.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getResizeWeight

​(int axis)

Determines the resizability of the view along the
given axis.

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

Renders using the given rendering surface and area on that surface.

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

int

viewToModel

​(float fx,
float fy,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

PlainView

changedUpdate

,

damageLineRange

,

drawLine

,

drawLine

,

drawSelectedText

,

drawSelectedText

,

drawUnselectedText

,

drawUnselectedText

,

getLineBuffer

,

getTabSize

,

lineToRect

,

nextTabStop

,

setSize

,

updateDamage

,

updateMetrics

- Methods declared in class javax.swing.text.

View

append

,

breakView

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

replace

,

setParent

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

Adjusts the allocation given to the view
to be a suitable allocation for a text field.

Fetches the font metrics associated with the component hosting
this view.

Determines the preferred span for this view along an
axis.

Determines the resizability of the view along the
given axis.

Gives notification that something was inserted into the document
in a location that this view is responsible for.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Renders using the given rendering surface and area on that surface.

Gives notification that something was removed from the document
in a location that this view is responsible for.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.text.

PlainView

changedUpdate

,

damageLineRange

,

drawLine

,

drawLine

,

drawSelectedText

,

drawSelectedText

,

drawUnselectedText

,

drawUnselectedText

,

getLineBuffer

,

getTabSize

,

lineToRect

,

nextTabStop

,

setSize

,

updateDamage

,

updateMetrics

---

#### Methods declared in class javax.swing.text. PlainView

Methods declared in class javax.swing.text.

View

append

,

breakView

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

replace

,

setParent

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

- FieldView

```java
public FieldView​(
Element
elem)
```

Constructs a new FieldView wrapped on an element.

**Parameters:** elem

- the element

============ METHOD DETAIL ==========

- Method Detail

- getFontMetrics

```java
protected
FontMetrics
getFontMetrics()
```

Fetches the font metrics associated with the component hosting
this view.

**Returns:** the metrics

- adjustAllocation

```java
protected
Shape
adjustAllocation​(
Shape
a)
```

Adjusts the allocation given to the view
to be a suitable allocation for a text field.
If the view has been allocated more than the
preferred span vertically, the allocation is
changed to be centered vertically. Horizontally
the view is adjusted according to the horizontal
alignment property set on the associated JTextField
(if that is the type of the hosting component).

**Parameters:** a

- the allocation given to the view, which may need
to be adjusted.
**Returns:** the allocation that the superclass should use.

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders using the given rendering surface and area on that surface.
The view may need to do layout and create child views to enable
itself to render into the given allocation.

**Overrides:** paint

in class

PlainView
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

**Overrides:** getPreferredSpan

in class

PlainView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

- getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Determines the resizability of the view along the
given axis. A value of 0 or less is not resizable.

**Overrides:** getResizeWeight

in class

View
**Parameters:** axis

- View.X_AXIS or View.Y_AXIS
**Returns:** the weight -> 1 for View.X_AXIS, else 0

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

**Overrides:** modelToView

in class

PlainView
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
public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:** viewToModel

in class

PlainView
**Parameters:** fx

- the X coordinate >= 0.0f
**Parameters:** fy

- the Y coordinate >= 0.0f
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

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

PlainView
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

PlainView
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

Constructor Detail

- FieldView

```java
public FieldView​(
Element
elem)
```

Constructs a new FieldView wrapped on an element.

**Parameters:** elem

- the element

---

#### Constructor Detail

FieldView

```java
public FieldView​(
Element
elem)
```

Constructs a new FieldView wrapped on an element.

**Parameters:** elem

- the element

---

#### FieldView

public FieldView​(

Element

elem)

Constructs a new FieldView wrapped on an element.

Method Detail

- getFontMetrics

```java
protected
FontMetrics
getFontMetrics()
```

Fetches the font metrics associated with the component hosting
this view.

**Returns:** the metrics

- adjustAllocation

```java
protected
Shape
adjustAllocation​(
Shape
a)
```

Adjusts the allocation given to the view
to be a suitable allocation for a text field.
If the view has been allocated more than the
preferred span vertically, the allocation is
changed to be centered vertically. Horizontally
the view is adjusted according to the horizontal
alignment property set on the associated JTextField
(if that is the type of the hosting component).

**Parameters:** a

- the allocation given to the view, which may need
to be adjusted.
**Returns:** the allocation that the superclass should use.

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders using the given rendering surface and area on that surface.
The view may need to do layout and create child views to enable
itself to render into the given allocation.

**Overrides:** paint

in class

PlainView
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

**Overrides:** getPreferredSpan

in class

PlainView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

- getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Determines the resizability of the view along the
given axis. A value of 0 or less is not resizable.

**Overrides:** getResizeWeight

in class

View
**Parameters:** axis

- View.X_AXIS or View.Y_AXIS
**Returns:** the weight -> 1 for View.X_AXIS, else 0

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

**Overrides:** modelToView

in class

PlainView
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
public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:** viewToModel

in class

PlainView
**Parameters:** fx

- the X coordinate >= 0.0f
**Parameters:** fy

- the Y coordinate >= 0.0f
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

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

PlainView
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

PlainView
**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### Method Detail

getFontMetrics

```java
protected
FontMetrics
getFontMetrics()
```

Fetches the font metrics associated with the component hosting
this view.

**Returns:** the metrics

---

#### getFontMetrics

protected

FontMetrics

getFontMetrics()

Fetches the font metrics associated with the component hosting
this view.

adjustAllocation

```java
protected
Shape
adjustAllocation​(
Shape
a)
```

Adjusts the allocation given to the view
to be a suitable allocation for a text field.
If the view has been allocated more than the
preferred span vertically, the allocation is
changed to be centered vertically. Horizontally
the view is adjusted according to the horizontal
alignment property set on the associated JTextField
(if that is the type of the hosting component).

**Parameters:** a

- the allocation given to the view, which may need
to be adjusted.
**Returns:** the allocation that the superclass should use.

---

#### adjustAllocation

protected

Shape

adjustAllocation​(

Shape

a)

Adjusts the allocation given to the view
to be a suitable allocation for a text field.
If the view has been allocated more than the
preferred span vertically, the allocation is
changed to be centered vertically. Horizontally
the view is adjusted according to the horizontal
alignment property set on the associated JTextField
(if that is the type of the hosting component).

paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders using the given rendering surface and area on that surface.
The view may need to do layout and create child views to enable
itself to render into the given allocation.

**Overrides:** paint

in class

PlainView
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

Renders using the given rendering surface and area on that surface.
The view may need to do layout and create child views to enable
itself to render into the given allocation.

getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Overrides:** getPreferredSpan

in class

PlainView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

getResizeWeight

```java
public int getResizeWeight​(int axis)
```

Determines the resizability of the view along the
given axis. A value of 0 or less is not resizable.

**Overrides:** getResizeWeight

in class

View
**Parameters:** axis

- View.X_AXIS or View.Y_AXIS
**Returns:** the weight -> 1 for View.X_AXIS, else 0

---

#### getResizeWeight

public int getResizeWeight​(int axis)

Determines the resizability of the view along the
given axis. A value of 0 or less is not resizable.

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

**Overrides:** modelToView

in class

PlainView
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
public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:** viewToModel

in class

PlainView
**Parameters:** fx

- the X coordinate >= 0.0f
**Parameters:** fy

- the Y coordinate >= 0.0f
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### viewToModel

public int viewToModel​(float fx,
float fy,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

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

PlainView
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

PlainView
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

---

