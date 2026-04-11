# Class PlainView

**Source:** `java.desktop\javax\swing\text\PlainView.html`

### Class Description

```java
public class
PlainView

extends
View

implements
TabExpander
```

Implements View interface for a simple multi-line text view
that has text in one font and color. The view represents each
child element as a line of text.

**All Implemented Interfaces:** SwingConstants

,

TabExpander

---

### Field Details

#### protected
FontMetrics
metrics

Font metrics for the current font.

---

### Constructor Details

#### public PlainView​(
Element
elem)

Constructs a new PlainView wrapped on an element.

**Parameters:**
- elem

- the element

---

### Method Details

#### protected int getTabSize()

Returns the tab size set for the document, defaulting to 8.

**Returns:**
- the tab size

---

#### @Deprecated
(
since
="9")
protected void drawLine​(int lineIndex,

Graphics
g,
int x,
int y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:**
- lineIndex

- the line to draw >= 0
- g

- the

Graphics

context
- x

- the starting X position >= 0
- y

- the starting Y position >= 0

**See Also:**
- drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

---

#### protected void drawLine​(int lineIndex,

Graphics2D
g,
float x,
float y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:**
- lineIndex

- the line to draw

>= 0
- g

- the

Graphics

context
- x

- the starting X position

>= 0
- y

- the starting Y position

>= 0

**See Also:**
- drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

**Since:**
- 9

---

#### @Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate >= 0
- y

- the starting Y coordinate >= 0
- p0

- the beginning position in the model >= 0
- p1

- the ending position in the model >= 0

**Returns:**
- the X location of the end of the range >= 0

**Throws:**
- BadLocationException

- if the range is invalid

---

#### protected float drawUnselectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate

>= 0
- y

- the starting Y coordinate

>= 0
- p0

- the beginning position in the model

>= 0
- p1

- the ending position in the model

>= 0

**Returns:**
- the X location of the end of the range

>= 0

**Throws:**
- BadLocationException

- if the range is invalid

**Since:**
- 9

---

#### @Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate >= 0
- y

- the starting Y coordinate >= 0
- p0

- the beginning position in the model >= 0
- p1

- the ending position in the model >= 0

**Returns:**
- the location of the end of the range

**Throws:**
- BadLocationException

- if the range is invalid

---

#### protected float drawSelectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate

>= 0
- y

- the starting Y coordinate

>= 0
- p0

- the beginning position in the model

>= 0
- p1

- the ending position in the model

>= 0

**Returns:**
- the location of the end of the range

**Throws:**
- BadLocationException

- if the range is invalid

**Since:**
- 9

---

#### protected final
Segment
getLineBuffer()

Gives access to a buffer that can be used to fetch
text from the associated document.

**Returns:**
- the buffer

---

#### protected void updateMetrics()

Checks to see if the font metrics and longest line
are up-to-date.

**Since:**
- 1.4

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

- for an invalid axis

**See Also:**
- View.getPreferredSpan(int)

---

#### public void paint​(
Graphics
g,

Shape
a)

Renders using the given rendering surface and area on that surface.
The view may need to do layout and create child views to enable
itself to render into the given allocation.

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
given point in the view >= 0

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

#### public void setSize​(float width,
float height)

Sets the size of the view. This should cause
layout of the view along the given axis, if it
has any layout duties.

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

#### public float nextTabStop​(float x,
int tabOffset)

Returns the next tab stop position after a given reference position.
This implementation does not support things like centering so it
ignores the tabOffset argument.

**Specified by:**
- nextTabStop

in interface

TabExpander

**Parameters:**
- x

- the current position >= 0
- tabOffset

- the position within the text stream
that the tab occurred at >= 0.

**Returns:**
- the tab stop, measured in points >= 0

---

#### protected void updateDamage​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)

Repaint the region of change covered by the given document
event. Damages the line that begins the range to cover
the case when the insert/remove is only on one line.
If lines are added or removed, damages the whole
view. The longest line is checked to see if it has
changed.

**Parameters:**
- changes

- the change information from the associated document
- a

- the current allocation of the view
- f

- the factory to use to rebuild if the view has children

**Since:**
- 1.4

---

#### protected void damageLineRange​(int line0,
int line1,

Shape
a,

Component
host)

Repaint the given line range.

**Parameters:**
- host

- the component hosting the view (used to call repaint)
- a

- the region allocated for the view to render into
- line0

- the starting line number to repaint. This must
be a valid line number in the model.
- line1

- the ending line number to repaint. This must
be a valid line number in the model.

**Since:**
- 1.4

---

#### protected
Rectangle
lineToRect​(
Shape
a,
int line)

Determine the rectangle that represents the given line.

**Parameters:**
- a

- the region allocated for the view to render into
- line

- the line number to find the region of. This must
be a valid line number in the model.

**Returns:**
- the rectangle that represents the given line

**Since:**
- 1.4

---

### Additional Sections

#### Class PlainView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.PlainView

javax.swing.text.View

- javax.swing.text.PlainView

javax.swing.text.PlainView

**All Implemented Interfaces:** SwingConstants

,

TabExpander

**Direct Known Subclasses:** FieldView

```java
public class
PlainView

extends
View

implements
TabExpander
```

Implements View interface for a simple multi-line text view
that has text in one font and color. The view represents each
child element as a line of text.

**See Also:** View

public class

PlainView

extends

View

implements

TabExpander

Implements View interface for a simple multi-line text view
that has text in one font and color. The view represents each
child element as a line of text.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

FontMetrics

metrics

Font metrics for the current font.

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

PlainView

​(

Element

elem)

Constructs a new PlainView wrapped on an element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

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

protected void

damageLineRange

​(int line0,
int line1,

Shape

a,

Component

host)

Repaint the given line range.

protected void

drawLine

​(int lineIndex,

Graphics2D

g,
float x,
float y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs.

protected void

drawLine

​(int lineIndex,

Graphics

g,
int x,
int y)

Deprecated.

replaced by

drawLine(int, Graphics2D, float, float)

protected float

drawSelectedText

​(

Graphics2D

g,
float x,
float y,
int p0,
int p1)

Renders the given range in the model as selected text.

protected int

drawSelectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

drawSelectedText(Graphics2D, float, float, int, int)

protected float

drawUnselectedText

​(

Graphics2D

g,
float x,
float y,
int p0,
int p1)

Renders the given range in the model as normal unselected
text.

protected int

drawUnselectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

drawUnselectedText(Graphics2D, float, float, int, int)

protected

Segment

getLineBuffer

()

Gives access to a buffer that can be used to fetch
text from the associated document.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

protected int

getTabSize

()

Returns the tab size set for the document, defaulting to 8.

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

protected

Rectangle

lineToRect

​(

Shape

a,
int line)

Determine the rectangle that represents the given line.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

float

nextTabStop

​(float x,
int tabOffset)

Returns the next tab stop position after a given reference position.

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

void

setSize

​(float width,
float height)

Sets the size of the view.

protected void

updateDamage

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Repaint the region of change covered by the given document
event.

protected void

updateMetrics

()

Checks to see if the font metrics and longest line
are up-to-date.

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

Fields

Modifier and Type

Field

Description

protected

FontMetrics

metrics

Font metrics for the current font.

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

Font metrics for the current font.

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

PlainView

​(

Element

elem)

Constructs a new PlainView wrapped on an element.

---

#### Constructor Summary

Constructs a new PlainView wrapped on an element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

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

protected void

damageLineRange

​(int line0,
int line1,

Shape

a,

Component

host)

Repaint the given line range.

protected void

drawLine

​(int lineIndex,

Graphics2D

g,
float x,
float y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs.

protected void

drawLine

​(int lineIndex,

Graphics

g,
int x,
int y)

Deprecated.

replaced by

drawLine(int, Graphics2D, float, float)

protected float

drawSelectedText

​(

Graphics2D

g,
float x,
float y,
int p0,
int p1)

Renders the given range in the model as selected text.

protected int

drawSelectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

drawSelectedText(Graphics2D, float, float, int, int)

protected float

drawUnselectedText

​(

Graphics2D

g,
float x,
float y,
int p0,
int p1)

Renders the given range in the model as normal unselected
text.

protected int

drawUnselectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

drawUnselectedText(Graphics2D, float, float, int, int)

protected

Segment

getLineBuffer

()

Gives access to a buffer that can be used to fetch
text from the associated document.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

protected int

getTabSize

()

Returns the tab size set for the document, defaulting to 8.

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

protected

Rectangle

lineToRect

​(

Shape

a,
int line)

Determine the rectangle that represents the given line.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

float

nextTabStop

​(float x,
int tabOffset)

Returns the next tab stop position after a given reference position.

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

void

setSize

​(float width,
float height)

Sets the size of the view.

protected void

updateDamage

​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Repaint the region of change covered by the given document
event.

protected void

updateMetrics

()

Checks to see if the font metrics and longest line
are up-to-date.

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

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Repaint the given line range.

Renders a line of text, suppressing whitespace at the end
and expanding any tabs.

Deprecated.

replaced by

drawLine(int, Graphics2D, float, float)

Renders the given range in the model as selected text.

Deprecated.

replaced by

drawSelectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as normal unselected
text.

Deprecated.

replaced by

drawUnselectedText(Graphics2D, float, float, int, int)

Gives access to a buffer that can be used to fetch
text from the associated document.

Determines the preferred span for this view along an
axis.

Returns the tab size set for the document, defaulting to 8.

Gives notification that something was inserted into the document
in a location that this view is responsible for.

Determine the rectangle that represents the given line.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Returns the next tab stop position after a given reference position.

Renders using the given rendering surface and area on that surface.

Gives notification that something was removed from the document
in a location that this view is responsible for.

Sets the size of the view.

Repaint the region of change covered by the given document
event.

Checks to see if the font metrics and longest line
are up-to-date.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

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

============ FIELD DETAIL ===========

- Field Detail

- metrics

```java
protected
FontMetrics
metrics
```

Font metrics for the current font.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PlainView

```java
public PlainView​(
Element
elem)
```

Constructs a new PlainView wrapped on an element.

**Parameters:** elem

- the element

============ METHOD DETAIL ==========

- Method Detail

- getTabSize

```java
protected int getTabSize()
```

Returns the tab size set for the document, defaulting to 8.

**Returns:** the tab size

- drawLine

```java
@Deprecated
(
since
="9")
protected void drawLine​(int lineIndex,

Graphics
g,
int x,
int y)
```

Deprecated.

replaced by

drawLine(int, Graphics2D, float, float)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** lineIndex

- the line to draw >= 0
**Parameters:** g

- the

Graphics

context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

- drawLine

```java
protected void drawLine​(int lineIndex,

Graphics2D
g,
float x,
float y)
```

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** lineIndex

- the line to draw

>= 0
**Parameters:** g

- the

Graphics

context
**Parameters:** x

- the starting X position

>= 0
**Parameters:** y

- the starting Y position

>= 0
**Since:** 9
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

- drawUnselectedText

```java
@Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

drawUnselectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= 0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if the range is invalid

- drawUnselectedText

```java
protected float drawUnselectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException
```

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** p0

- the beginning position in the model

>= 0
**Parameters:** p1

- the ending position in the model

>= 0
**Returns:** the X location of the end of the range

>= 0
**Throws:** BadLocationException

- if the range is invalid
**Since:** 9

- drawSelectedText

```java
@Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

drawSelectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= 0
**Returns:** the location of the end of the range
**Throws:** BadLocationException

- if the range is invalid

- drawSelectedText

```java
protected float drawSelectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException
```

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** p0

- the beginning position in the model

>= 0
**Parameters:** p1

- the ending position in the model

>= 0
**Returns:** the location of the end of the range
**Throws:** BadLocationException

- if the range is invalid
**Since:** 9

- getLineBuffer

```java
protected final
Segment
getLineBuffer()
```

Gives access to a buffer that can be used to fetch
text from the associated document.

**Returns:** the buffer

- updateMetrics

```java
protected void updateMetrics()
```

Checks to see if the font metrics and longest line
are up-to-date.

**Since:** 1.4

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

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

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

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

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
given point in the view >= 0
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

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view along the given axis, if it
has any layout duties.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

- nextTabStop

```java
public float nextTabStop​(float x,
int tabOffset)
```

Returns the next tab stop position after a given reference position.
This implementation does not support things like centering so it
ignores the tabOffset argument.

**Specified by:** nextTabStop

in interface

TabExpander
**Parameters:** x

- the current position >= 0
**Parameters:** tabOffset

- the position within the text stream
that the tab occurred at >= 0.
**Returns:** the tab stop, measured in points >= 0

- updateDamage

```java
protected void updateDamage​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Repaint the region of change covered by the given document
event. Damages the line that begins the range to cover
the case when the insert/remove is only on one line.
If lines are added or removed, damages the whole
view. The longest line is checked to see if it has
changed.

**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**Since:** 1.4

- damageLineRange

```java
protected void damageLineRange​(int line0,
int line1,

Shape
a,

Component
host)
```

Repaint the given line range.

**Parameters:** host

- the component hosting the view (used to call repaint)
**Parameters:** a

- the region allocated for the view to render into
**Parameters:** line0

- the starting line number to repaint. This must
be a valid line number in the model.
**Parameters:** line1

- the ending line number to repaint. This must
be a valid line number in the model.
**Since:** 1.4

- lineToRect

```java
protected
Rectangle
lineToRect​(
Shape
a,
int line)
```

Determine the rectangle that represents the given line.

**Parameters:** a

- the region allocated for the view to render into
**Parameters:** line

- the line number to find the region of. This must
be a valid line number in the model.
**Returns:** the rectangle that represents the given line
**Since:** 1.4

Field Detail

- metrics

```java
protected
FontMetrics
metrics
```

Font metrics for the current font.

---

#### Field Detail

metrics

```java
protected
FontMetrics
metrics
```

Font metrics for the current font.

---

#### metrics

protected

FontMetrics

metrics

Font metrics for the current font.

Constructor Detail

- PlainView

```java
public PlainView​(
Element
elem)
```

Constructs a new PlainView wrapped on an element.

**Parameters:** elem

- the element

---

#### Constructor Detail

PlainView

```java
public PlainView​(
Element
elem)
```

Constructs a new PlainView wrapped on an element.

**Parameters:** elem

- the element

---

#### PlainView

public PlainView​(

Element

elem)

Constructs a new PlainView wrapped on an element.

Method Detail

- getTabSize

```java
protected int getTabSize()
```

Returns the tab size set for the document, defaulting to 8.

**Returns:** the tab size

- drawLine

```java
@Deprecated
(
since
="9")
protected void drawLine​(int lineIndex,

Graphics
g,
int x,
int y)
```

Deprecated.

replaced by

drawLine(int, Graphics2D, float, float)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** lineIndex

- the line to draw >= 0
**Parameters:** g

- the

Graphics

context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

- drawLine

```java
protected void drawLine​(int lineIndex,

Graphics2D
g,
float x,
float y)
```

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** lineIndex

- the line to draw

>= 0
**Parameters:** g

- the

Graphics

context
**Parameters:** x

- the starting X position

>= 0
**Parameters:** y

- the starting Y position

>= 0
**Since:** 9
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

- drawUnselectedText

```java
@Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

drawUnselectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= 0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if the range is invalid

- drawUnselectedText

```java
protected float drawUnselectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException
```

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** p0

- the beginning position in the model

>= 0
**Parameters:** p1

- the ending position in the model

>= 0
**Returns:** the X location of the end of the range

>= 0
**Throws:** BadLocationException

- if the range is invalid
**Since:** 9

- drawSelectedText

```java
@Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

drawSelectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= 0
**Returns:** the location of the end of the range
**Throws:** BadLocationException

- if the range is invalid

- drawSelectedText

```java
protected float drawSelectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException
```

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** p0

- the beginning position in the model

>= 0
**Parameters:** p1

- the ending position in the model

>= 0
**Returns:** the location of the end of the range
**Throws:** BadLocationException

- if the range is invalid
**Since:** 9

- getLineBuffer

```java
protected final
Segment
getLineBuffer()
```

Gives access to a buffer that can be used to fetch
text from the associated document.

**Returns:** the buffer

- updateMetrics

```java
protected void updateMetrics()
```

Checks to see if the font metrics and longest line
are up-to-date.

**Since:** 1.4

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

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

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

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

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
given point in the view >= 0
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

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view along the given axis, if it
has any layout duties.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

- nextTabStop

```java
public float nextTabStop​(float x,
int tabOffset)
```

Returns the next tab stop position after a given reference position.
This implementation does not support things like centering so it
ignores the tabOffset argument.

**Specified by:** nextTabStop

in interface

TabExpander
**Parameters:** x

- the current position >= 0
**Parameters:** tabOffset

- the position within the text stream
that the tab occurred at >= 0.
**Returns:** the tab stop, measured in points >= 0

- updateDamage

```java
protected void updateDamage​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Repaint the region of change covered by the given document
event. Damages the line that begins the range to cover
the case when the insert/remove is only on one line.
If lines are added or removed, damages the whole
view. The longest line is checked to see if it has
changed.

**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**Since:** 1.4

- damageLineRange

```java
protected void damageLineRange​(int line0,
int line1,

Shape
a,

Component
host)
```

Repaint the given line range.

**Parameters:** host

- the component hosting the view (used to call repaint)
**Parameters:** a

- the region allocated for the view to render into
**Parameters:** line0

- the starting line number to repaint. This must
be a valid line number in the model.
**Parameters:** line1

- the ending line number to repaint. This must
be a valid line number in the model.
**Since:** 1.4

- lineToRect

```java
protected
Rectangle
lineToRect​(
Shape
a,
int line)
```

Determine the rectangle that represents the given line.

**Parameters:** a

- the region allocated for the view to render into
**Parameters:** line

- the line number to find the region of. This must
be a valid line number in the model.
**Returns:** the rectangle that represents the given line
**Since:** 1.4

---

#### Method Detail

getTabSize

```java
protected int getTabSize()
```

Returns the tab size set for the document, defaulting to 8.

**Returns:** the tab size

---

#### getTabSize

protected int getTabSize()

Returns the tab size set for the document, defaulting to 8.

drawLine

```java
@Deprecated
(
since
="9")
protected void drawLine​(int lineIndex,

Graphics
g,
int x,
int y)
```

Deprecated.

replaced by

drawLine(int, Graphics2D, float, float)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** lineIndex

- the line to draw >= 0
**Parameters:** g

- the

Graphics

context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

---

#### drawLine

@Deprecated

(

since

="9")
protected void drawLine​(int lineIndex,

Graphics

g,
int x,
int y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

drawLine

```java
protected void drawLine​(int lineIndex,

Graphics2D
g,
float x,
float y)
```

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** lineIndex

- the line to draw

>= 0
**Parameters:** g

- the

Graphics

context
**Parameters:** x

- the starting X position

>= 0
**Parameters:** y

- the starting Y position

>= 0
**Since:** 9
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

---

#### drawLine

protected void drawLine​(int lineIndex,

Graphics2D

g,
float x,
float y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

drawUnselectedText

```java
@Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

drawUnselectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= 0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if the range is invalid

---

#### drawUnselectedText

@Deprecated

(

since

="9")
protected int drawUnselectedText​(

Graphics

g,
int x,
int y,
int p0,
int p1)
throws

BadLocationException

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

drawUnselectedText

```java
protected float drawUnselectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException
```

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** p0

- the beginning position in the model

>= 0
**Parameters:** p1

- the ending position in the model

>= 0
**Returns:** the X location of the end of the range

>= 0
**Throws:** BadLocationException

- if the range is invalid
**Since:** 9

---

#### drawUnselectedText

protected float drawUnselectedText​(

Graphics2D

g,
float x,
float y,
int p0,
int p1)
throws

BadLocationException

Renders the given range in the model as normal unselected
text. Uses the foreground or disabled color to render the text.

drawSelectedText

```java
@Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

drawSelectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= 0
**Returns:** the location of the end of the range
**Throws:** BadLocationException

- if the range is invalid

---

#### drawSelectedText

@Deprecated

(

since

="9")
protected int drawSelectedText​(

Graphics

g,
int x,
int y,
int p0,
int p1)
throws

BadLocationException

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

drawSelectedText

```java
protected float drawSelectedText​(
Graphics2D
g,
float x,
float y,
int p0,
int p1)
throws
BadLocationException
```

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** p0

- the beginning position in the model

>= 0
**Parameters:** p1

- the ending position in the model

>= 0
**Returns:** the location of the end of the range
**Throws:** BadLocationException

- if the range is invalid
**Since:** 9

---

#### drawSelectedText

protected float drawSelectedText​(

Graphics2D

g,
float x,
float y,
int p0,
int p1)
throws

BadLocationException

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background.

getLineBuffer

```java
protected final
Segment
getLineBuffer()
```

Gives access to a buffer that can be used to fetch
text from the associated document.

**Returns:** the buffer

---

#### getLineBuffer

protected final

Segment

getLineBuffer()

Gives access to a buffer that can be used to fetch
text from the associated document.

updateMetrics

```java
protected void updateMetrics()
```

Checks to see if the font metrics and longest line
are up-to-date.

**Since:** 1.4

---

#### updateMetrics

protected void updateMetrics()

Checks to see if the font metrics and longest line
are up-to-date.

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

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

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

Renders using the given rendering surface and area on that surface.
The view may need to do layout and create child views to enable
itself to render into the given allocation.

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

setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view along the given axis, if it
has any layout duties.

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
layout of the view along the given axis, if it
has any layout duties.

nextTabStop

```java
public float nextTabStop​(float x,
int tabOffset)
```

Returns the next tab stop position after a given reference position.
This implementation does not support things like centering so it
ignores the tabOffset argument.

**Specified by:** nextTabStop

in interface

TabExpander
**Parameters:** x

- the current position >= 0
**Parameters:** tabOffset

- the position within the text stream
that the tab occurred at >= 0.
**Returns:** the tab stop, measured in points >= 0

---

#### nextTabStop

public float nextTabStop​(float x,
int tabOffset)

Returns the next tab stop position after a given reference position.
This implementation does not support things like centering so it
ignores the tabOffset argument.

updateDamage

```java
protected void updateDamage​(
DocumentEvent
changes,

Shape
a,

ViewFactory
f)
```

Repaint the region of change covered by the given document
event. Damages the line that begins the range to cover
the case when the insert/remove is only on one line.
If lines are added or removed, damages the whole
view. The longest line is checked to see if it has
changed.

**Parameters:** changes

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**Since:** 1.4

---

#### updateDamage

protected void updateDamage​(

DocumentEvent

changes,

Shape

a,

ViewFactory

f)

Repaint the region of change covered by the given document
event. Damages the line that begins the range to cover
the case when the insert/remove is only on one line.
If lines are added or removed, damages the whole
view. The longest line is checked to see if it has
changed.

damageLineRange

```java
protected void damageLineRange​(int line0,
int line1,

Shape
a,

Component
host)
```

Repaint the given line range.

**Parameters:** host

- the component hosting the view (used to call repaint)
**Parameters:** a

- the region allocated for the view to render into
**Parameters:** line0

- the starting line number to repaint. This must
be a valid line number in the model.
**Parameters:** line1

- the ending line number to repaint. This must
be a valid line number in the model.
**Since:** 1.4

---

#### damageLineRange

protected void damageLineRange​(int line0,
int line1,

Shape

a,

Component

host)

Repaint the given line range.

lineToRect

```java
protected
Rectangle
lineToRect​(
Shape
a,
int line)
```

Determine the rectangle that represents the given line.

**Parameters:** a

- the region allocated for the view to render into
**Parameters:** line

- the line number to find the region of. This must
be a valid line number in the model.
**Returns:** the rectangle that represents the given line
**Since:** 1.4

---

#### lineToRect

protected

Rectangle

lineToRect​(

Shape

a,
int line)

Determine the rectangle that represents the given line.

---

