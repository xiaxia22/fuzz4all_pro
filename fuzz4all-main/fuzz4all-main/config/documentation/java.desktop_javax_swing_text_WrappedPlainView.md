# Class WrappedPlainView

**Source:** `java.desktop\javax\swing\text\WrappedPlainView.html`

### Class Description

```java
public class
WrappedPlainView

extends
BoxView

implements
TabExpander
```

View of plain text (text with only one font and color)
that does line-wrapping. This view expects that its
associated element has child elements that represent
the lines it should be wrapping. It is implemented
as a vertical box that contains logical line views.
The logical line views are nested classes that render
the logical line as multiple physical line if the logical
line is too wide to fit within the allocation. The
line views draw upon the outer class for its state
to reduce their memory requirements.

The line views do all of their rendering through the

drawLine

method which in turn does all of
its rendering through the

drawSelectedText

and

drawUnselectedText

methods. This
enables subclasses to easily specialize the rendering
without concern for the layout aspects.

**All Implemented Interfaces:** SwingConstants

,

TabExpander

---

### Field Details

*No entries found.*

### Constructor Details

#### public WrappedPlainView​(
Element
elem)

Creates a new WrappedPlainView. Lines will be wrapped
on character boundaries.

**Parameters:**
- elem

- the element underlying the view

---

#### public WrappedPlainView​(
Element
elem,
boolean wordWrap)

Creates a new WrappedPlainView. Lines can be wrapped on
either character or word boundaries depending upon the
setting of the wordWrap parameter.

**Parameters:**
- elem

- the element underlying the view
- wordWrap

- should lines be wrapped on word boundaries?

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
protected void drawLine​(int p0,
int p1,

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
- p0

- the starting document location to use >= 0
- p1

- the ending document location to use >= p1
- g

- the graphics context
- x

- the starting X position >= 0
- y

- the starting Y position >= 0

**See Also:**
- drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

---

#### protected void drawLine​(int p0,
int p1,

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
- p0

- the starting document location to use >= 0
- p1

- the ending document location to use >= p1
- g

- the graphics context
- x

- the starting X position >= 0
- y

- the starting Y position >= 0

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
text.

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

- the ending position in the model >= p0

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
text.

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

- the ending position in the model >= p0

**Returns:**
- the X location of the end of the range >= 0

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

- the ending position in the model >= p0

**Returns:**
- the location of the end of the range.

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

- the starting X coordinate >= 0
- y

- the starting Y coordinate >= 0
- p0

- the beginning position in the model >= 0
- p1

- the ending position in the model >= p0

**Returns:**
- the location of the end of the range.

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

#### protected int calculateBreakPosition​(int p0,
int p1)

This is called by the nested wrapped line
views to determine the break location. This can
be reimplemented to alter the breaking behavior.
It will either break at word or character boundaries
depending upon the break argument given at
construction.

**Parameters:**
- p0

- the starting document location
- p1

- the ending document location to use

**Returns:**
- the break position

---

#### protected void loadChildren​(
ViewFactory
f)

Loads all of the children to initialize the view.
This is called by the

setParent

method.
Subclasses can reimplement this to initialize their
child views in a different manner. The default
implementation creates a child view for each
child element.

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

#### public void paint​(
Graphics
g,

Shape
a)

Renders using the given rendering surface and area
on that surface. This is implemented to stash the
selection positions, selection colors, and font
metrics for the nested lines to use.

**Overrides:**
- paint

in class

BoxView

**Parameters:**
- g

- the rendering surface to use
- a

- the allocated region to render into

**See Also:**
- View.paint(java.awt.Graphics, java.awt.Shape)

---

#### public void setSize​(float width,
float height)

Sets the size of the view. This should cause
layout of the view along the given axis, if it
has any layout duties.

**Overrides:**
- setSize

in class

BoxView

**Parameters:**
- width

- the width >= 0
- height

- the height >= 0

---

#### public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:**
- getPreferredSpan

in class

BoxView

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:**
- getMinimumSpan

in class

BoxView

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**See Also:**
- View.getMinimumSpan(int)

---

#### public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:**
- getMaximumSpan

in class

BoxView

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**See Also:**
- View.getMaximumSpan(int)

---

#### public void insertUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)

Gives notification that something was inserted into the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:**
- insertUpdate

in class

View

**Parameters:**
- e

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
e,

Shape
a,

ViewFactory
f)

Gives notification that something was removed from the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:**
- removeUpdate

in class

View

**Parameters:**
- e

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
e,

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
- e

- the change information from the associated document
- a

- the current allocation of the view
- f

- the factory to use to rebuild if the view has children

**See Also:**
- View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

### Additional Sections

#### Class WrappedPlainView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.WrappedPlainView

javax.swing.text.View

- javax.swing.text.CompositeView
- - javax.swing.text.BoxView
- - javax.swing.text.WrappedPlainView

javax.swing.text.CompositeView

- javax.swing.text.BoxView
- - javax.swing.text.WrappedPlainView

javax.swing.text.BoxView

- javax.swing.text.WrappedPlainView

javax.swing.text.WrappedPlainView

**All Implemented Interfaces:** SwingConstants

,

TabExpander

```java
public class
WrappedPlainView

extends
BoxView

implements
TabExpander
```

View of plain text (text with only one font and color)
that does line-wrapping. This view expects that its
associated element has child elements that represent
the lines it should be wrapping. It is implemented
as a vertical box that contains logical line views.
The logical line views are nested classes that render
the logical line as multiple physical line if the logical
line is too wide to fit within the allocation. The
line views draw upon the outer class for its state
to reduce their memory requirements.

The line views do all of their rendering through the

drawLine

method which in turn does all of
its rendering through the

drawSelectedText

and

drawUnselectedText

methods. This
enables subclasses to easily specialize the rendering
without concern for the layout aspects.

**See Also:** View

public class

WrappedPlainView

extends

BoxView

implements

TabExpander

View of plain text (text with only one font and color)
that does line-wrapping. This view expects that its
associated element has child elements that represent
the lines it should be wrapping. It is implemented
as a vertical box that contains logical line views.
The logical line views are nested classes that render
the logical line as multiple physical line if the logical
line is too wide to fit within the allocation. The
line views draw upon the outer class for its state
to reduce their memory requirements.

The line views do all of their rendering through the

drawLine

method which in turn does all of
its rendering through the

drawSelectedText

and

drawUnselectedText

methods. This
enables subclasses to easily specialize the rendering
without concern for the layout aspects.

The line views do all of their rendering through the

drawLine

method which in turn does all of
its rendering through the

drawSelectedText

and

drawUnselectedText

methods. This
enables subclasses to easily specialize the rendering
without concern for the layout aspects.

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

WrappedPlainView

​(

Element

elem)

Creates a new WrappedPlainView.

WrappedPlainView

​(

Element

elem,
boolean wordWrap)

Creates a new WrappedPlainView.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected int

calculateBreakPosition

​(int p0,
int p1)

This is called by the nested wrapped line
views to determine the break location.

void

changedUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

protected void

drawLine

​(int p0,
int p1,

Graphics2D

g,
float x,
float y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs.

protected void

drawLine

​(int p0,
int p1,

Graphics

g,
int x,
int y)

Deprecated.

replaced by

drawLine(int, int, Graphics2D, float, float)

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

protected int

getTabSize

()

Returns the tab size set for the document, defaulting to 8.

void

insertUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into the
document in a location that this view is responsible for.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

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

Renders using the given rendering surface and area
on that surface.

void

removeUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the
document in a location that this view is responsible for.

void

setSize

​(float width,
float height)

Sets the size of the view.

- Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

calculateMajorAxisRequirements

,

calculateMinorAxisRequirements

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

getOffset

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

layout

,

layoutChanged

,

layoutMajorAxis

,

layoutMinorAxis

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

WrappedPlainView

​(

Element

elem)

Creates a new WrappedPlainView.

WrappedPlainView

​(

Element

elem,
boolean wordWrap)

Creates a new WrappedPlainView.

---

#### Constructor Summary

Creates a new WrappedPlainView.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected int

calculateBreakPosition

​(int p0,
int p1)

This is called by the nested wrapped line
views to determine the break location.

void

changedUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

protected void

drawLine

​(int p0,
int p1,

Graphics2D

g,
float x,
float y)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs.

protected void

drawLine

​(int p0,
int p1,

Graphics

g,
int x,
int y)

Deprecated.

replaced by

drawLine(int, int, Graphics2D, float, float)

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

protected int

getTabSize

()

Returns the tab size set for the document, defaulting to 8.

void

insertUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into the
document in a location that this view is responsible for.

protected void

loadChildren

​(

ViewFactory

f)

Loads all of the children to initialize the view.

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

Renders using the given rendering surface and area
on that surface.

void

removeUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the
document in a location that this view is responsible for.

void

setSize

​(float width,
float height)

Sets the size of the view.

- Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

calculateMajorAxisRequirements

,

calculateMinorAxisRequirements

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

getOffset

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

layout

,

layoutChanged

,

layoutMajorAxis

,

layoutMinorAxis

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

This is called by the nested wrapped line
views to determine the break location.

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Renders a line of text, suppressing whitespace at the end
and expanding any tabs.

Deprecated.

replaced by

drawLine(int, int, Graphics2D, float, float)

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

Determines the maximum span for this view along an
axis.

Determines the minimum span for this view along an
axis.

Determines the preferred span for this view along an
axis.

Returns the tab size set for the document, defaulting to 8.

Gives notification that something was inserted into the
document in a location that this view is responsible for.

Loads all of the children to initialize the view.

Returns the next tab stop position after a given reference position.

Renders using the given rendering surface and area
on that surface.

Gives notification that something was removed from the
document in a location that this view is responsible for.

Sets the size of the view.

Methods declared in class javax.swing.text.

BoxView

baselineLayout

,

baselineRequirements

,

calculateMajorAxisRequirements

,

calculateMinorAxisRequirements

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

getOffset

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

layout

,

layoutChanged

,

layoutMajorAxis

,

layoutMinorAxis

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- WrappedPlainView

```java
public WrappedPlainView​(
Element
elem)
```

Creates a new WrappedPlainView. Lines will be wrapped
on character boundaries.

**Parameters:** elem

- the element underlying the view

- WrappedPlainView

```java
public WrappedPlainView​(
Element
elem,
boolean wordWrap)
```

Creates a new WrappedPlainView. Lines can be wrapped on
either character or word boundaries depending upon the
setting of the wordWrap parameter.

**Parameters:** elem

- the element underlying the view
**Parameters:** wordWrap

- should lines be wrapped on word boundaries?

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
protected void drawLine​(int p0,
int p1,

Graphics
g,
int x,
int y)
```

Deprecated.

replaced by

drawLine(int, int, Graphics2D, float, float)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** p0

- the starting document location to use >= 0
**Parameters:** p1

- the ending document location to use >= p1
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

- drawLine

```java
protected void drawLine​(int p0,
int p1,

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

**Parameters:** p0

- the starting document location to use >= 0
**Parameters:** p1

- the ending document location to use >= p1
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
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
text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
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
text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
**Returns:** the X location of the end of the range >= 0
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

- the ending position in the model >= p0
**Returns:** the location of the end of the range.
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

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
**Returns:** the location of the end of the range.
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

- calculateBreakPosition

```java
protected int calculateBreakPosition​(int p0,
int p1)
```

This is called by the nested wrapped line
views to determine the break location. This can
be reimplemented to alter the breaking behavior.
It will either break at word or character boundaries
depending upon the break argument given at
construction.

**Parameters:** p0

- the starting document location
**Parameters:** p1

- the ending document location to use
**Returns:** the break position

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
Subclasses can reimplement this to initialize their
child views in a different manner. The default
implementation creates a child view for each
child element.

**Overrides:** loadChildren

in class

CompositeView
**Parameters:** f

- the view factory
**See Also:** CompositeView.setParent(javax.swing.text.View)

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

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders using the given rendering surface and area
on that surface. This is implemented to stash the
selection positions, selection colors, and font
metrics for the nested lines to use.

**Overrides:** paint

in class

BoxView
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

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

BoxView
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getPreferredSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getMinimumSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getMinimumSpan(int)

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getMaximumSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getMaximumSpan(int)

- insertUpdate

```java
public void insertUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Gives notification that something was inserted into the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:** insertUpdate

in class

View
**Parameters:** e

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
e,

Shape
a,

ViewFactory
f)
```

Gives notification that something was removed from the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:** removeUpdate

in class

View
**Parameters:** e

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
e,

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
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

Constructor Detail

- WrappedPlainView

```java
public WrappedPlainView​(
Element
elem)
```

Creates a new WrappedPlainView. Lines will be wrapped
on character boundaries.

**Parameters:** elem

- the element underlying the view

- WrappedPlainView

```java
public WrappedPlainView​(
Element
elem,
boolean wordWrap)
```

Creates a new WrappedPlainView. Lines can be wrapped on
either character or word boundaries depending upon the
setting of the wordWrap parameter.

**Parameters:** elem

- the element underlying the view
**Parameters:** wordWrap

- should lines be wrapped on word boundaries?

---

#### Constructor Detail

WrappedPlainView

```java
public WrappedPlainView​(
Element
elem)
```

Creates a new WrappedPlainView. Lines will be wrapped
on character boundaries.

**Parameters:** elem

- the element underlying the view

---

#### WrappedPlainView

public WrappedPlainView​(

Element

elem)

Creates a new WrappedPlainView. Lines will be wrapped
on character boundaries.

WrappedPlainView

```java
public WrappedPlainView​(
Element
elem,
boolean wordWrap)
```

Creates a new WrappedPlainView. Lines can be wrapped on
either character or word boundaries depending upon the
setting of the wordWrap parameter.

**Parameters:** elem

- the element underlying the view
**Parameters:** wordWrap

- should lines be wrapped on word boundaries?

---

#### WrappedPlainView

public WrappedPlainView​(

Element

elem,
boolean wordWrap)

Creates a new WrappedPlainView. Lines can be wrapped on
either character or word boundaries depending upon the
setting of the wordWrap parameter.

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
protected void drawLine​(int p0,
int p1,

Graphics
g,
int x,
int y)
```

Deprecated.

replaced by

drawLine(int, int, Graphics2D, float, float)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** p0

- the starting document location to use >= 0
**Parameters:** p1

- the ending document location to use >= p1
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

- drawLine

```java
protected void drawLine​(int p0,
int p1,

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

**Parameters:** p0

- the starting document location to use >= 0
**Parameters:** p1

- the ending document location to use >= p1
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
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
text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
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
text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
**Returns:** the X location of the end of the range >= 0
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

- the ending position in the model >= p0
**Returns:** the location of the end of the range.
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

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
**Returns:** the location of the end of the range.
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

- calculateBreakPosition

```java
protected int calculateBreakPosition​(int p0,
int p1)
```

This is called by the nested wrapped line
views to determine the break location. This can
be reimplemented to alter the breaking behavior.
It will either break at word or character boundaries
depending upon the break argument given at
construction.

**Parameters:** p0

- the starting document location
**Parameters:** p1

- the ending document location to use
**Returns:** the break position

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
Subclasses can reimplement this to initialize their
child views in a different manner. The default
implementation creates a child view for each
child element.

**Overrides:** loadChildren

in class

CompositeView
**Parameters:** f

- the view factory
**See Also:** CompositeView.setParent(javax.swing.text.View)

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

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders using the given rendering surface and area
on that surface. This is implemented to stash the
selection positions, selection colors, and font
metrics for the nested lines to use.

**Overrides:** paint

in class

BoxView
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

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

BoxView
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getPreferredSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getMinimumSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getMinimumSpan(int)

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getMaximumSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getMaximumSpan(int)

- insertUpdate

```java
public void insertUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Gives notification that something was inserted into the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:** insertUpdate

in class

View
**Parameters:** e

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
e,

Shape
a,

ViewFactory
f)
```

Gives notification that something was removed from the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:** removeUpdate

in class

View
**Parameters:** e

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
e,

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
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

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
protected void drawLine​(int p0,
int p1,

Graphics
g,
int x,
int y)
```

Deprecated.

replaced by

drawLine(int, int, Graphics2D, float, float)

Renders a line of text, suppressing whitespace at the end
and expanding any tabs. This is implemented to make calls
to the methods

drawUnselectedText

and

drawSelectedText

so that the way selected and
unselected text are rendered can be customized.

**Parameters:** p0

- the starting document location to use >= 0
**Parameters:** p1

- the ending document location to use >= p1
**Parameters:** g

- the graphics context
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
protected void drawLine​(int p0,
int p1,

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
protected void drawLine​(int p0,
int p1,

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

**Parameters:** p0

- the starting document location to use >= 0
**Parameters:** p1

- the ending document location to use >= p1
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X position >= 0
**Parameters:** y

- the starting Y position >= 0
**Since:** 9
**See Also:** drawUnselectedText(java.awt.Graphics, int, int, int, int)

,

drawSelectedText(java.awt.Graphics, int, int, int, int)

---

#### drawLine

protected void drawLine​(int p0,
int p1,

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
text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
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
text.

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
text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
**Returns:** the X location of the end of the range >= 0
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
text.

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

- the ending position in the model >= p0
**Returns:** the location of the end of the range.
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

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the beginning position in the model >= 0
**Parameters:** p1

- the ending position in the model >= p0
**Returns:** the location of the end of the range.
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

calculateBreakPosition

```java
protected int calculateBreakPosition​(int p0,
int p1)
```

This is called by the nested wrapped line
views to determine the break location. This can
be reimplemented to alter the breaking behavior.
It will either break at word or character boundaries
depending upon the break argument given at
construction.

**Parameters:** p0

- the starting document location
**Parameters:** p1

- the ending document location to use
**Returns:** the break position

---

#### calculateBreakPosition

protected int calculateBreakPosition​(int p0,
int p1)

This is called by the nested wrapped line
views to determine the break location. This can
be reimplemented to alter the breaking behavior.
It will either break at word or character boundaries
depending upon the break argument given at
construction.

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
Subclasses can reimplement this to initialize their
child views in a different manner. The default
implementation creates a child view for each
child element.

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
Subclasses can reimplement this to initialize their
child views in a different manner. The default
implementation creates a child view for each
child element.

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

paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders using the given rendering surface and area
on that surface. This is implemented to stash the
selection positions, selection colors, and font
metrics for the nested lines to use.

**Overrides:** paint

in class

BoxView
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

Renders using the given rendering surface and area
on that surface. This is implemented to stash the
selection positions, selection colors, and font
metrics for the nested lines to use.

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

BoxView
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

getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getPreferredSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getMinimumSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getMinimumSpan(int)

---

#### getMinimumSpan

public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

**Overrides:** getMaximumSpan

in class

BoxView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getMaximumSpan(int)

---

#### getMaximumSpan

public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis. This is implemented to provide the superclass
behavior after first making sure that the current font
metrics are cached (for the nested lines which use
the metrics to determine the height of the potentially
wrapped lines).

insertUpdate

```java
public void insertUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Gives notification that something was inserted into the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:** insertUpdate

in class

View
**Parameters:** e

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

e,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into the
document in a location that this view is responsible for.
This is implemented to simply update the children.

removeUpdate

```java
public void removeUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Gives notification that something was removed from the
document in a location that this view is responsible for.
This is implemented to simply update the children.

**Overrides:** removeUpdate

in class

View
**Parameters:** e

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

e,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the
document in a location that this view is responsible for.
This is implemented to simply update the children.

changedUpdate

```java
public void changedUpdate​(
DocumentEvent
e,

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
**Parameters:** e

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

e,

Shape

a,

ViewFactory

f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

---

