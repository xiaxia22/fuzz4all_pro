# Class GlyphView

**Source:** `java.desktop\javax\swing\text\GlyphView.html`

### Class Description

```java
public class
GlyphView

extends
View

implements
TabableView
,
Cloneable
```

A GlyphView is a styled chunk of text that represents a view
mapped over an element in the text model. This view is generally
responsible for displaying text glyphs using character level
attributes in some way.
An implementation of the GlyphPainter class is used to do the
actual rendering and model/view translations. This separates
rendering from layout and management of the association with
the model.

The view supports breaking for the purpose of formatting.
The fragments produced by breaking share the view that has
primary responsibility for the element (i.e. they are nested
classes and carry only a small amount of state of their own)
so they can share its resources.

Since this view
represents text that may have tabs embedded in it, it implements the

TabableView

interface. Tabs will only be
expanded if this view is embedded in a container that does
tab expansion. ParagraphView is an example of a container
that does tab expansion.

**All Implemented Interfaces:** Cloneable

,

SwingConstants

,

TabableView

---

### Field Details

*No entries found.*

### Constructor Details

#### public GlyphView​(
Element
elem)

Constructs a new view wrapped on an element.

**Parameters:**
- elem

- the element

---

### Method Details

#### protected final
Object
clone()

Creates a shallow copy. This is used by the
createFragment and breakView methods.

**Overrides:**
- clone

in class

Object

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### public
GlyphView.GlyphPainter
getGlyphPainter()

Fetch the currently installed glyph painter.
If a painter has not yet been installed, and
a default was not yet needed, null is returned.

**Returns:**
- the currently installed glyph painter

---

#### public void setGlyphPainter​(
GlyphView.GlyphPainter
p)

Sets the painter to use for rendering glyphs.

**Parameters:**
- p

- the painter to use for rendering glyphs

---

#### public
Segment
getText​(int p0,
int p1)

Fetch a reference to the text that occupies
the given range. This is normally used by
the GlyphPainter to determine what characters
it should render glyphs for.

**Parameters:**
- p0

- the starting document offset >= 0
- p1

- the ending document offset >= p0

**Returns:**
- the

Segment

containing the text

---

#### public
Color
getBackground()

Fetch the background color to use to render the
glyphs. If there is no background color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a styled document, otherwise it returns null.

**Returns:**
- the background color to use to render the glyphs

---

#### public
Color
getForeground()

Fetch the foreground color to use to render the
glyphs. If there is no foreground color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components foreground
color is used. If there is no associated component, null
is returned.

**Returns:**
- the foreground color to use to render the glyphs

---

#### public
Font
getFont()

Fetch the font that the glyphs should be based
upon. This is implemented to call

StyledDocument.getFont

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components font
is used. If there is no associated component, null
is returned.

**Returns:**
- the font that the glyphs should be based upon

---

#### public boolean isUnderline()

Determine if the glyphs should be underlined. If true,
an underline should be drawn through the baseline.

**Returns:**
- if the glyphs should be underlined

---

#### public boolean isStrikeThrough()

Determine if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs.

**Returns:**
- if the glyphs should have a strikethrough line

---

#### public boolean isSubscript()

Determine if the glyphs should be rendered as superscript.

**Returns:**
- if the glyphs should be rendered as superscript

---

#### public boolean isSuperscript()

Determine if the glyphs should be rendered as subscript.

**Returns:**
- if the glyphs should be rendered as subscript

---

#### public
TabExpander
getTabExpander()

Fetch the TabExpander to use if tabs are present in this view.

**Returns:**
- the TabExpander to use if tabs are present in this view

---

#### protected void checkPainter()

Check to see that a glyph painter exists. If a painter
doesn't exist, a default glyph painter will be installed.

---

#### public float getTabbedSpan​(float x,

TabExpander
e)

Determines the desired span when using the given
tab expansion implementation.

**Specified by:**
- getTabbedSpan

in interface

TabableView

**Parameters:**
- x

- the position the view would be located
at for the purpose of tab expansion >= 0.
- e

- how to expand the tabs when encountered.

**Returns:**
- the desired span >= 0

**See Also:**
- TabableView.getTabbedSpan(float, javax.swing.text.TabExpander)

---

#### public float getPartialSpan​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

This method can be called while servicing the
getTabbedSpan or getPreferredSize. It has to
arrange for its own text buffer to make the
measurements.

**Specified by:**
- getPartialSpan

in interface

TabableView

**Parameters:**
- p0

- the starting document offset >= 0
- p1

- the ending document offset >= p0

**Returns:**
- the span >= 0

---

#### public int getStartOffset()

Fetches the portion of the model that this view is responsible for.

**Overrides:**
- getStartOffset

in class

View

**Returns:**
- the starting offset into the model

**See Also:**
- View.getStartOffset()

---

#### public int getEndOffset()

Fetches the portion of the model that this view is responsible for.

**Overrides:**
- getEndOffset

in class

View

**Returns:**
- the ending offset into the model

**See Also:**
- View.getEndOffset()

---

#### public void paint​(
Graphics
g,

Shape
a)

Renders a portion of a text style run.

**Specified by:**
- paint

in class

View

**Parameters:**
- g

- the rendering surface to use
- a

- the allocated region to render into

---

#### public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an axis.

This implementation returns the longest non-breakable area within
the view as a minimum span for

View.X_AXIS

.

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
- the minimum span the view can be rendered into

**Throws:**
- IllegalArgumentException

- if the

axis

parameter is invalid

**See Also:**
- View.getMinimumSpan(int)

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

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. For the label, the alignment is along the font
baseline for the y axis, and the superclasses alignment
along the x axis.

**Overrides:**
- getAlignment

in class

View

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the desired alignment. This should be a value
between 0.0 and 1.0 inclusive, where 0 indicates alignment at the
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

- either

Position.Bias.Forward

or

Position.Bias.Backward

**Returns:**
- the bounding box of the given position

**Throws:**
- BadLocationException

- if the given position does not represent a
valid location in the associated document

**See Also:**
- View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] biasReturn)

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
- biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the
zero-th element of this array

**Returns:**
- the location within the model that best represents the
given point of view >= 0

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### public int getBreakWeight​(int axis,
float pos,
float len)

Determines how attractive a break opportunity in
this view is. This can be used for determining which
view is the most attractive to call

breakView

on in the process of formatting. The
higher the weight, the more attractive the break. A
value equal to or lower than

View.BadBreakWeight

should not be considered for a break. A value greater
than or equal to

View.ForcedBreakWeight

should
be broken.

This is implemented to forward to the superclass for
the Y_AXIS. Along the X_AXIS the following values
may be returned.

This will normally result in the behavior of breaking
on a whitespace location if one can be found, otherwise
breaking between characters.

---

#### public
View
breakView​(int axis,
int p0,
float pos,
float len)

Breaks this view on the given axis at the given length.
This is implemented to attempt to break on a whitespace
location, and returns a fragment with the whitespace at
the end. If a whitespace location can't be found, the
nearest character is used.

**Overrides:**
- breakView

in class

View

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS
- p0

- the location in the model where the
fragment should start it's representation >= 0.
- pos

- the position along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
- len

- specifies the distance along the axis
where a potential break is desired >= 0.

**Returns:**
- the fragment of the view that represents the
given span, if the view can be broken. If the view
doesn't support breaking behavior, the view itself is
returned.

**See Also:**
- View.breakView(int, int, float, float)

---

#### public
View
createFragment​(int p0,
int p1)

Creates a view that represents a portion of the element.
This is potentially useful during formatting operations
for taking measurements of fragments of the view. If
the view doesn't support fragmenting (the default), it
should return itself.

This view does support fragmenting. It is implemented
to return a nested class that shares state in this view
representing only a portion of the view.

**Overrides:**
- createFragment

in class

View

**Parameters:**
- p0

- the starting offset >= 0. This should be a value
greater or equal to the element starting offset and
less than the element ending offset.
- p1

- the ending offset > p0. This should be a value
less than or equal to the elements end offset and
greater than the elements starting offset.

**Returns:**
- the view fragment, or itself if the view doesn't
support breaking into fragments

**See Also:**
- LabelView

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
location that one might place a caret. Some views may not be
visible, they might not be in the same order found in the model, or
they just might not allow access to some of the locations in the
model.
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
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
- b

- the bias
- biasRet

- the returned bias

**Returns:**
- the location within the model that best represents the next
location visual position.

**Throws:**
- BadLocationException

- the given position is not a valid
position within the document
- IllegalArgumentException

- for an invalid direction

---

#### public void insertUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)

Gives notification that something was inserted into
the document in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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

Gives notification that something was removed from the document
in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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
This is implemented to call preferenceChanged along both the
horizontal and vertical axis.

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

#### Class GlyphView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.GlyphView

javax.swing.text.View

- javax.swing.text.GlyphView

javax.swing.text.GlyphView

**All Implemented Interfaces:** Cloneable

,

SwingConstants

,

TabableView

**Direct Known Subclasses:** LabelView

```java
public class
GlyphView

extends
View

implements
TabableView
,
Cloneable
```

A GlyphView is a styled chunk of text that represents a view
mapped over an element in the text model. This view is generally
responsible for displaying text glyphs using character level
attributes in some way.
An implementation of the GlyphPainter class is used to do the
actual rendering and model/view translations. This separates
rendering from layout and management of the association with
the model.

The view supports breaking for the purpose of formatting.
The fragments produced by breaking share the view that has
primary responsibility for the element (i.e. they are nested
classes and carry only a small amount of state of their own)
so they can share its resources.

Since this view
represents text that may have tabs embedded in it, it implements the

TabableView

interface. Tabs will only be
expanded if this view is embedded in a container that does
tab expansion. ParagraphView is an example of a container
that does tab expansion.

**Since:** 1.3

public class

GlyphView

extends

View

implements

TabableView

,

Cloneable

A GlyphView is a styled chunk of text that represents a view
mapped over an element in the text model. This view is generally
responsible for displaying text glyphs using character level
attributes in some way.
An implementation of the GlyphPainter class is used to do the
actual rendering and model/view translations. This separates
rendering from layout and management of the association with
the model.

The view supports breaking for the purpose of formatting.
The fragments produced by breaking share the view that has
primary responsibility for the element (i.e. they are nested
classes and carry only a small amount of state of their own)
so they can share its resources.

Since this view
represents text that may have tabs embedded in it, it implements the

TabableView

interface. Tabs will only be
expanded if this view is embedded in a container that does
tab expansion. ParagraphView is an example of a container
that does tab expansion.

The view supports breaking for the purpose of formatting.
The fragments produced by breaking share the view that has
primary responsibility for the element (i.e. they are nested
classes and carry only a small amount of state of their own)
so they can share its resources.

Since this view
represents text that may have tabs embedded in it, it implements the

TabableView

interface. Tabs will only be
expanded if this view is embedded in a container that does
tab expansion. ParagraphView is an example of a container
that does tab expansion.

Since this view
represents text that may have tabs embedded in it, it implements the

TabableView

interface. Tabs will only be
expanded if this view is embedded in a container that does
tab expansion. ParagraphView is an example of a container
that does tab expansion.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

GlyphView.GlyphPainter

A class to perform rendering of the glyphs.

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

GlyphView

​(

Element

elem)

Constructs a new view wrapped on an element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

View

breakView

​(int axis,
int p0,
float pos,
float len)

Breaks this view on the given axis at the given length.

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

checkPainter

()

Check to see that a glyph painter exists.

protected

Object

clone

()

Creates a shallow copy.

View

createFragment

​(int p0,
int p1)

Creates a view that represents a portion of the element.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

Color

getBackground

()

Fetch the background color to use to render the
glyphs.

int

getBreakWeight

​(int axis,
float pos,
float len)

Determines how attractive a break opportunity in
this view is.

int

getEndOffset

()

Fetches the portion of the model that this view is responsible for.

Font

getFont

()

Fetch the font that the glyphs should be based
upon.

Color

getForeground

()

Fetch the foreground color to use to render the
glyphs.

GlyphView.GlyphPainter

getGlyphPainter

()

Fetch the currently installed glyph painter.

float

getMinimumSpan

​(int axis)

Determines the minimum span for this view along an axis.

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

getPartialSpan

​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getStartOffset

()

Fetches the portion of the model that this view is responsible for.

float

getTabbedSpan

​(float x,

TabExpander

e)

Determines the desired span when using the given
tab expansion implementation.

TabExpander

getTabExpander

()

Fetch the TabExpander to use if tabs are present in this view.

Segment

getText

​(int p0,
int p1)

Fetch a reference to the text that occupies
the given range.

void

insertUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into
the document in a location that this view is responsible for.

boolean

isStrikeThrough

()

Determine if the glyphs should have a strikethrough
line.

boolean

isSubscript

()

Determine if the glyphs should be rendered as superscript.

boolean

isSuperscript

()

Determine if the glyphs should be rendered as subscript.

boolean

isUnderline

()

Determine if the glyphs should be underlined.

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

Renders a portion of a text style run.

void

removeUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the document
in a location that this view is responsible for.

void

setGlyphPainter

​(

GlyphView.GlyphPainter

p)

Sets the painter to use for rendering glyphs.

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

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getGraphics

,

getMaximumSpan

,

getParent

,

getResizeWeight

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

setSize

,

updateChildren

,

updateLayout

,

viewToModel

- Methods declared in class java.lang.

Object

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

GlyphView.GlyphPainter

A class to perform rendering of the glyphs.

---

#### Nested Class Summary

A class to perform rendering of the glyphs.

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

GlyphView

​(

Element

elem)

Constructs a new view wrapped on an element.

---

#### Constructor Summary

Constructs a new view wrapped on an element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

View

breakView

​(int axis,
int p0,
float pos,
float len)

Breaks this view on the given axis at the given length.

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

checkPainter

()

Check to see that a glyph painter exists.

protected

Object

clone

()

Creates a shallow copy.

View

createFragment

​(int p0,
int p1)

Creates a view that represents a portion of the element.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

Color

getBackground

()

Fetch the background color to use to render the
glyphs.

int

getBreakWeight

​(int axis,
float pos,
float len)

Determines how attractive a break opportunity in
this view is.

int

getEndOffset

()

Fetches the portion of the model that this view is responsible for.

Font

getFont

()

Fetch the font that the glyphs should be based
upon.

Color

getForeground

()

Fetch the foreground color to use to render the
glyphs.

GlyphView.GlyphPainter

getGlyphPainter

()

Fetch the currently installed glyph painter.

float

getMinimumSpan

​(int axis)

Determines the minimum span for this view along an axis.

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

getPartialSpan

​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

int

getStartOffset

()

Fetches the portion of the model that this view is responsible for.

float

getTabbedSpan

​(float x,

TabExpander

e)

Determines the desired span when using the given
tab expansion implementation.

TabExpander

getTabExpander

()

Fetch the TabExpander to use if tabs are present in this view.

Segment

getText

​(int p0,
int p1)

Fetch a reference to the text that occupies
the given range.

void

insertUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was inserted into
the document in a location that this view is responsible for.

boolean

isStrikeThrough

()

Determine if the glyphs should have a strikethrough
line.

boolean

isSubscript

()

Determine if the glyphs should be rendered as superscript.

boolean

isSuperscript

()

Determine if the glyphs should be rendered as subscript.

boolean

isUnderline

()

Determine if the glyphs should be underlined.

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

Renders a portion of a text style run.

void

removeUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Gives notification that something was removed from the document
in a location that this view is responsible for.

void

setGlyphPainter

​(

GlyphView.GlyphPainter

p)

Sets the painter to use for rendering glyphs.

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

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getGraphics

,

getMaximumSpan

,

getParent

,

getResizeWeight

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

setSize

,

updateChildren

,

updateLayout

,

viewToModel

- Methods declared in class java.lang.

Object

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

Breaks this view on the given axis at the given length.

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Check to see that a glyph painter exists.

Creates a shallow copy.

Creates a view that represents a portion of the element.

Determines the desired alignment for this view along an
axis.

Fetch the background color to use to render the
glyphs.

Determines how attractive a break opportunity in
this view is.

Fetches the portion of the model that this view is responsible for.

Fetch the font that the glyphs should be based
upon.

Fetch the foreground color to use to render the
glyphs.

Fetch the currently installed glyph painter.

Determines the minimum span for this view along an axis.

Provides a way to determine the next visually represented model
location that one might place a caret.

Determines the span along the same axis as tab
expansion for a portion of the view.

Determines the preferred span for this view along an
axis.

Determines the desired span when using the given
tab expansion implementation.

Fetch the TabExpander to use if tabs are present in this view.

Fetch a reference to the text that occupies
the given range.

Gives notification that something was inserted into
the document in a location that this view is responsible for.

Determine if the glyphs should have a strikethrough
line.

Determine if the glyphs should be rendered as superscript.

Determine if the glyphs should be rendered as subscript.

Determine if the glyphs should be underlined.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Renders a portion of a text style run.

Gives notification that something was removed from the document
in a location that this view is responsible for.

Sets the painter to use for rendering glyphs.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.text.

View

append

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getGraphics

,

getMaximumSpan

,

getParent

,

getResizeWeight

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

- GlyphView

```java
public GlyphView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
protected final
Object
clone()
```

Creates a shallow copy. This is used by the
createFragment and breakView methods.

**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- getGlyphPainter

```java
public
GlyphView.GlyphPainter
getGlyphPainter()
```

Fetch the currently installed glyph painter.
If a painter has not yet been installed, and
a default was not yet needed, null is returned.

**Returns:** the currently installed glyph painter

- setGlyphPainter

```java
public void setGlyphPainter​(
GlyphView.GlyphPainter
p)
```

Sets the painter to use for rendering glyphs.

**Parameters:** p

- the painter to use for rendering glyphs

- getText

```java
public
Segment
getText​(int p0,
int p1)
```

Fetch a reference to the text that occupies
the given range. This is normally used by
the GlyphPainter to determine what characters
it should render glyphs for.

**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** the

Segment

containing the text

- getBackground

```java
public
Color
getBackground()
```

Fetch the background color to use to render the
glyphs. If there is no background color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a styled document, otherwise it returns null.

**Returns:** the background color to use to render the glyphs

- getForeground

```java
public
Color
getForeground()
```

Fetch the foreground color to use to render the
glyphs. If there is no foreground color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components foreground
color is used. If there is no associated component, null
is returned.

**Returns:** the foreground color to use to render the glyphs

- getFont

```java
public
Font
getFont()
```

Fetch the font that the glyphs should be based
upon. This is implemented to call

StyledDocument.getFont

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components font
is used. If there is no associated component, null
is returned.

**Returns:** the font that the glyphs should be based upon

- isUnderline

```java
public boolean isUnderline()
```

Determine if the glyphs should be underlined. If true,
an underline should be drawn through the baseline.

**Returns:** if the glyphs should be underlined

- isStrikeThrough

```java
public boolean isStrikeThrough()
```

Determine if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs.

**Returns:** if the glyphs should have a strikethrough line

- isSubscript

```java
public boolean isSubscript()
```

Determine if the glyphs should be rendered as superscript.

**Returns:** if the glyphs should be rendered as superscript

- isSuperscript

```java
public boolean isSuperscript()
```

Determine if the glyphs should be rendered as subscript.

**Returns:** if the glyphs should be rendered as subscript

- getTabExpander

```java
public
TabExpander
getTabExpander()
```

Fetch the TabExpander to use if tabs are present in this view.

**Returns:** the TabExpander to use if tabs are present in this view

- checkPainter

```java
protected void checkPainter()
```

Check to see that a glyph painter exists. If a painter
doesn't exist, a default glyph painter will be installed.

- getTabbedSpan

```java
public float getTabbedSpan​(float x,

TabExpander
e)
```

Determines the desired span when using the given
tab expansion implementation.

**Specified by:** getTabbedSpan

in interface

TabableView
**Parameters:** x

- the position the view would be located
at for the purpose of tab expansion >= 0.
**Parameters:** e

- how to expand the tabs when encountered.
**Returns:** the desired span >= 0
**See Also:** TabableView.getTabbedSpan(float, javax.swing.text.TabExpander)

- getPartialSpan

```java
public float getPartialSpan​(int p0,
int p1)
```

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

This method can be called while servicing the
getTabbedSpan or getPreferredSize. It has to
arrange for its own text buffer to make the
measurements.

**Specified by:** getPartialSpan

in interface

TabableView
**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** the span >= 0

- getStartOffset

```java
public int getStartOffset()
```

Fetches the portion of the model that this view is responsible for.

**Overrides:** getStartOffset

in class

View
**Returns:** the starting offset into the model
**See Also:** View.getStartOffset()

- getEndOffset

```java
public int getEndOffset()
```

Fetches the portion of the model that this view is responsible for.

**Overrides:** getEndOffset

in class

View
**Returns:** the ending offset into the model
**See Also:** View.getEndOffset()

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders a portion of a text style run.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an axis.

This implementation returns the longest non-breakable area within
the view as a minimum span for

View.X_AXIS

.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the minimum span the view can be rendered into
**Throws:** IllegalArgumentException

- if the

axis

parameter is invalid
**See Also:** View.getMinimumSpan(int)

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
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. For the label, the alignment is along the font
baseline for the y axis, and the superclasses alignment
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment. This should be a value
between 0.0 and 1.0 inclusive, where 0 indicates alignment at the
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

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

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
**Parameters:** biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the
zero-th element of this array
**Returns:** the location within the model that best represents the
given point of view >= 0
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getBreakWeight

```java
public int getBreakWeight​(int axis,
float pos,
float len)
```

Determines how attractive a break opportunity in
this view is. This can be used for determining which
view is the most attractive to call

breakView

on in the process of formatting. The
higher the weight, the more attractive the break. A
value equal to or lower than

View.BadBreakWeight

should not be considered for a break. A value greater
than or equal to

View.ForcedBreakWeight

should
be broken.

This is implemented to forward to the superclass for
the Y_AXIS. Along the X_AXIS the following values
may be returned.

This will normally result in the behavior of breaking
on a whitespace location if one can be found, otherwise
breaking between characters.

**Overrides:** getBreakWeight

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Parameters:** pos

- the potential location of the start of the
broken view >= 0. This may be useful for calculating tab
positions.
**Parameters:** len

- specifies the relative length from

pos

where a potential break is desired >= 0.
**Returns:** the weight, which should be a value between
View.ForcedBreakWeight and View.BadBreakWeight.
**See Also:** LabelView

,

ParagraphView

,

View.BadBreakWeight

,

View.GoodBreakWeight

,

View.ExcellentBreakWeight

,

View.ForcedBreakWeight

- breakView

```java
public
View
breakView​(int axis,
int p0,
float pos,
float len)
```

Breaks this view on the given axis at the given length.
This is implemented to attempt to break on a whitespace
location, and returns a fragment with the whitespace at
the end. If a whitespace location can't be found, the
nearest character is used.

**Overrides:** breakView

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Parameters:** p0

- the location in the model where the
fragment should start it's representation >= 0.
**Parameters:** pos

- the position along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
**Parameters:** len

- specifies the distance along the axis
where a potential break is desired >= 0.
**Returns:** the fragment of the view that represents the
given span, if the view can be broken. If the view
doesn't support breaking behavior, the view itself is
returned.
**See Also:** View.breakView(int, int, float, float)

- createFragment

```java
public
View
createFragment​(int p0,
int p1)
```

Creates a view that represents a portion of the element.
This is potentially useful during formatting operations
for taking measurements of fragments of the view. If
the view doesn't support fragmenting (the default), it
should return itself.

This view does support fragmenting. It is implemented
to return a nested class that shares state in this view
representing only a portion of the view.

**Overrides:** createFragment

in class

View
**Parameters:** p0

- the starting offset >= 0. This should be a value
greater or equal to the element starting offset and
less than the element ending offset.
**Parameters:** p1

- the ending offset > p0. This should be a value
less than or equal to the elements end offset and
greater than the elements starting offset.
**Returns:** the view fragment, or itself if the view doesn't
support breaking into fragments
**See Also:** LabelView

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
location that one might place a caret. Some views may not be
visible, they might not be in the same order found in the model, or
they just might not allow access to some of the locations in the
model.
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
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
**Parameters:** b

- the bias
**Parameters:** biasRet

- the returned bias
**Returns:** the location within the model that best represents the next
location visual position.
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Throws:** IllegalArgumentException

- for an invalid direction

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

Gives notification that something was inserted into
the document in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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

Gives notification that something was removed from the document
in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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
This is implemented to call preferenceChanged along both the
horizontal and vertical axis.

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

- GlyphView

```java
public GlyphView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

---

#### Constructor Detail

GlyphView

```java
public GlyphView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

---

#### GlyphView

public GlyphView​(

Element

elem)

Constructs a new view wrapped on an element.

Method Detail

- clone

```java
protected final
Object
clone()
```

Creates a shallow copy. This is used by the
createFragment and breakView methods.

**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- getGlyphPainter

```java
public
GlyphView.GlyphPainter
getGlyphPainter()
```

Fetch the currently installed glyph painter.
If a painter has not yet been installed, and
a default was not yet needed, null is returned.

**Returns:** the currently installed glyph painter

- setGlyphPainter

```java
public void setGlyphPainter​(
GlyphView.GlyphPainter
p)
```

Sets the painter to use for rendering glyphs.

**Parameters:** p

- the painter to use for rendering glyphs

- getText

```java
public
Segment
getText​(int p0,
int p1)
```

Fetch a reference to the text that occupies
the given range. This is normally used by
the GlyphPainter to determine what characters
it should render glyphs for.

**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** the

Segment

containing the text

- getBackground

```java
public
Color
getBackground()
```

Fetch the background color to use to render the
glyphs. If there is no background color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a styled document, otherwise it returns null.

**Returns:** the background color to use to render the glyphs

- getForeground

```java
public
Color
getForeground()
```

Fetch the foreground color to use to render the
glyphs. If there is no foreground color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components foreground
color is used. If there is no associated component, null
is returned.

**Returns:** the foreground color to use to render the glyphs

- getFont

```java
public
Font
getFont()
```

Fetch the font that the glyphs should be based
upon. This is implemented to call

StyledDocument.getFont

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components font
is used. If there is no associated component, null
is returned.

**Returns:** the font that the glyphs should be based upon

- isUnderline

```java
public boolean isUnderline()
```

Determine if the glyphs should be underlined. If true,
an underline should be drawn through the baseline.

**Returns:** if the glyphs should be underlined

- isStrikeThrough

```java
public boolean isStrikeThrough()
```

Determine if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs.

**Returns:** if the glyphs should have a strikethrough line

- isSubscript

```java
public boolean isSubscript()
```

Determine if the glyphs should be rendered as superscript.

**Returns:** if the glyphs should be rendered as superscript

- isSuperscript

```java
public boolean isSuperscript()
```

Determine if the glyphs should be rendered as subscript.

**Returns:** if the glyphs should be rendered as subscript

- getTabExpander

```java
public
TabExpander
getTabExpander()
```

Fetch the TabExpander to use if tabs are present in this view.

**Returns:** the TabExpander to use if tabs are present in this view

- checkPainter

```java
protected void checkPainter()
```

Check to see that a glyph painter exists. If a painter
doesn't exist, a default glyph painter will be installed.

- getTabbedSpan

```java
public float getTabbedSpan​(float x,

TabExpander
e)
```

Determines the desired span when using the given
tab expansion implementation.

**Specified by:** getTabbedSpan

in interface

TabableView
**Parameters:** x

- the position the view would be located
at for the purpose of tab expansion >= 0.
**Parameters:** e

- how to expand the tabs when encountered.
**Returns:** the desired span >= 0
**See Also:** TabableView.getTabbedSpan(float, javax.swing.text.TabExpander)

- getPartialSpan

```java
public float getPartialSpan​(int p0,
int p1)
```

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

This method can be called while servicing the
getTabbedSpan or getPreferredSize. It has to
arrange for its own text buffer to make the
measurements.

**Specified by:** getPartialSpan

in interface

TabableView
**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** the span >= 0

- getStartOffset

```java
public int getStartOffset()
```

Fetches the portion of the model that this view is responsible for.

**Overrides:** getStartOffset

in class

View
**Returns:** the starting offset into the model
**See Also:** View.getStartOffset()

- getEndOffset

```java
public int getEndOffset()
```

Fetches the portion of the model that this view is responsible for.

**Overrides:** getEndOffset

in class

View
**Returns:** the ending offset into the model
**See Also:** View.getEndOffset()

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders a portion of a text style run.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an axis.

This implementation returns the longest non-breakable area within
the view as a minimum span for

View.X_AXIS

.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the minimum span the view can be rendered into
**Throws:** IllegalArgumentException

- if the

axis

parameter is invalid
**See Also:** View.getMinimumSpan(int)

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
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. For the label, the alignment is along the font
baseline for the y axis, and the superclasses alignment
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment. This should be a value
between 0.0 and 1.0 inclusive, where 0 indicates alignment at the
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

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

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
**Parameters:** biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the
zero-th element of this array
**Returns:** the location within the model that best represents the
given point of view >= 0
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getBreakWeight

```java
public int getBreakWeight​(int axis,
float pos,
float len)
```

Determines how attractive a break opportunity in
this view is. This can be used for determining which
view is the most attractive to call

breakView

on in the process of formatting. The
higher the weight, the more attractive the break. A
value equal to or lower than

View.BadBreakWeight

should not be considered for a break. A value greater
than or equal to

View.ForcedBreakWeight

should
be broken.

This is implemented to forward to the superclass for
the Y_AXIS. Along the X_AXIS the following values
may be returned.

This will normally result in the behavior of breaking
on a whitespace location if one can be found, otherwise
breaking between characters.

**Overrides:** getBreakWeight

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Parameters:** pos

- the potential location of the start of the
broken view >= 0. This may be useful for calculating tab
positions.
**Parameters:** len

- specifies the relative length from

pos

where a potential break is desired >= 0.
**Returns:** the weight, which should be a value between
View.ForcedBreakWeight and View.BadBreakWeight.
**See Also:** LabelView

,

ParagraphView

,

View.BadBreakWeight

,

View.GoodBreakWeight

,

View.ExcellentBreakWeight

,

View.ForcedBreakWeight

- breakView

```java
public
View
breakView​(int axis,
int p0,
float pos,
float len)
```

Breaks this view on the given axis at the given length.
This is implemented to attempt to break on a whitespace
location, and returns a fragment with the whitespace at
the end. If a whitespace location can't be found, the
nearest character is used.

**Overrides:** breakView

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Parameters:** p0

- the location in the model where the
fragment should start it's representation >= 0.
**Parameters:** pos

- the position along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
**Parameters:** len

- specifies the distance along the axis
where a potential break is desired >= 0.
**Returns:** the fragment of the view that represents the
given span, if the view can be broken. If the view
doesn't support breaking behavior, the view itself is
returned.
**See Also:** View.breakView(int, int, float, float)

- createFragment

```java
public
View
createFragment​(int p0,
int p1)
```

Creates a view that represents a portion of the element.
This is potentially useful during formatting operations
for taking measurements of fragments of the view. If
the view doesn't support fragmenting (the default), it
should return itself.

This view does support fragmenting. It is implemented
to return a nested class that shares state in this view
representing only a portion of the view.

**Overrides:** createFragment

in class

View
**Parameters:** p0

- the starting offset >= 0. This should be a value
greater or equal to the element starting offset and
less than the element ending offset.
**Parameters:** p1

- the ending offset > p0. This should be a value
less than or equal to the elements end offset and
greater than the elements starting offset.
**Returns:** the view fragment, or itself if the view doesn't
support breaking into fragments
**See Also:** LabelView

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
location that one might place a caret. Some views may not be
visible, they might not be in the same order found in the model, or
they just might not allow access to some of the locations in the
model.
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
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
**Parameters:** b

- the bias
**Parameters:** biasRet

- the returned bias
**Returns:** the location within the model that best represents the next
location visual position.
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Throws:** IllegalArgumentException

- for an invalid direction

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

Gives notification that something was inserted into
the document in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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

Gives notification that something was removed from the document
in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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
This is implemented to call preferenceChanged along both the
horizontal and vertical axis.

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

clone

```java
protected final
Object
clone()
```

Creates a shallow copy. This is used by the
createFragment and breakView methods.

**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

protected final

Object

clone()

Creates a shallow copy. This is used by the
createFragment and breakView methods.

getGlyphPainter

```java
public
GlyphView.GlyphPainter
getGlyphPainter()
```

Fetch the currently installed glyph painter.
If a painter has not yet been installed, and
a default was not yet needed, null is returned.

**Returns:** the currently installed glyph painter

---

#### getGlyphPainter

public

GlyphView.GlyphPainter

getGlyphPainter()

Fetch the currently installed glyph painter.
If a painter has not yet been installed, and
a default was not yet needed, null is returned.

setGlyphPainter

```java
public void setGlyphPainter​(
GlyphView.GlyphPainter
p)
```

Sets the painter to use for rendering glyphs.

**Parameters:** p

- the painter to use for rendering glyphs

---

#### setGlyphPainter

public void setGlyphPainter​(

GlyphView.GlyphPainter

p)

Sets the painter to use for rendering glyphs.

getText

```java
public
Segment
getText​(int p0,
int p1)
```

Fetch a reference to the text that occupies
the given range. This is normally used by
the GlyphPainter to determine what characters
it should render glyphs for.

**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** the

Segment

containing the text

---

#### getText

public

Segment

getText​(int p0,
int p1)

Fetch a reference to the text that occupies
the given range. This is normally used by
the GlyphPainter to determine what characters
it should render glyphs for.

getBackground

```java
public
Color
getBackground()
```

Fetch the background color to use to render the
glyphs. If there is no background color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a styled document, otherwise it returns null.

**Returns:** the background color to use to render the glyphs

---

#### getBackground

public

Color

getBackground()

Fetch the background color to use to render the
glyphs. If there is no background color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a styled document, otherwise it returns null.

getForeground

```java
public
Color
getForeground()
```

Fetch the foreground color to use to render the
glyphs. If there is no foreground color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components foreground
color is used. If there is no associated component, null
is returned.

**Returns:** the foreground color to use to render the glyphs

---

#### getForeground

public

Color

getForeground()

Fetch the foreground color to use to render the
glyphs. If there is no foreground color, null should
be returned. This is implemented to call

StyledDocument.getBackground

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components foreground
color is used. If there is no associated component, null
is returned.

getFont

```java
public
Font
getFont()
```

Fetch the font that the glyphs should be based
upon. This is implemented to call

StyledDocument.getFont

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components font
is used. If there is no associated component, null
is returned.

**Returns:** the font that the glyphs should be based upon

---

#### getFont

public

Font

getFont()

Fetch the font that the glyphs should be based
upon. This is implemented to call

StyledDocument.getFont

if the associated
document is a StyledDocument. If the associated document
is not a StyledDocument, the associated components font
is used. If there is no associated component, null
is returned.

isUnderline

```java
public boolean isUnderline()
```

Determine if the glyphs should be underlined. If true,
an underline should be drawn through the baseline.

**Returns:** if the glyphs should be underlined

---

#### isUnderline

public boolean isUnderline()

Determine if the glyphs should be underlined. If true,
an underline should be drawn through the baseline.

isStrikeThrough

```java
public boolean isStrikeThrough()
```

Determine if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs.

**Returns:** if the glyphs should have a strikethrough line

---

#### isStrikeThrough

public boolean isStrikeThrough()

Determine if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs.

isSubscript

```java
public boolean isSubscript()
```

Determine if the glyphs should be rendered as superscript.

**Returns:** if the glyphs should be rendered as superscript

---

#### isSubscript

public boolean isSubscript()

Determine if the glyphs should be rendered as superscript.

isSuperscript

```java
public boolean isSuperscript()
```

Determine if the glyphs should be rendered as subscript.

**Returns:** if the glyphs should be rendered as subscript

---

#### isSuperscript

public boolean isSuperscript()

Determine if the glyphs should be rendered as subscript.

getTabExpander

```java
public
TabExpander
getTabExpander()
```

Fetch the TabExpander to use if tabs are present in this view.

**Returns:** the TabExpander to use if tabs are present in this view

---

#### getTabExpander

public

TabExpander

getTabExpander()

Fetch the TabExpander to use if tabs are present in this view.

checkPainter

```java
protected void checkPainter()
```

Check to see that a glyph painter exists. If a painter
doesn't exist, a default glyph painter will be installed.

---

#### checkPainter

protected void checkPainter()

Check to see that a glyph painter exists. If a painter
doesn't exist, a default glyph painter will be installed.

getTabbedSpan

```java
public float getTabbedSpan​(float x,

TabExpander
e)
```

Determines the desired span when using the given
tab expansion implementation.

**Specified by:** getTabbedSpan

in interface

TabableView
**Parameters:** x

- the position the view would be located
at for the purpose of tab expansion >= 0.
**Parameters:** e

- how to expand the tabs when encountered.
**Returns:** the desired span >= 0
**See Also:** TabableView.getTabbedSpan(float, javax.swing.text.TabExpander)

---

#### getTabbedSpan

public float getTabbedSpan​(float x,

TabExpander

e)

Determines the desired span when using the given
tab expansion implementation.

getPartialSpan

```java
public float getPartialSpan​(int p0,
int p1)
```

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

This method can be called while servicing the
getTabbedSpan or getPreferredSize. It has to
arrange for its own text buffer to make the
measurements.

**Specified by:** getPartialSpan

in interface

TabableView
**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** the span >= 0

---

#### getPartialSpan

public float getPartialSpan​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

This method can be called while servicing the
getTabbedSpan or getPreferredSize. It has to
arrange for its own text buffer to make the
measurements.

This method can be called while servicing the
getTabbedSpan or getPreferredSize. It has to
arrange for its own text buffer to make the
measurements.

getStartOffset

```java
public int getStartOffset()
```

Fetches the portion of the model that this view is responsible for.

**Overrides:** getStartOffset

in class

View
**Returns:** the starting offset into the model
**See Also:** View.getStartOffset()

---

#### getStartOffset

public int getStartOffset()

Fetches the portion of the model that this view is responsible for.

getEndOffset

```java
public int getEndOffset()
```

Fetches the portion of the model that this view is responsible for.

**Overrides:** getEndOffset

in class

View
**Returns:** the ending offset into the model
**See Also:** View.getEndOffset()

---

#### getEndOffset

public int getEndOffset()

Fetches the portion of the model that this view is responsible for.

paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Renders a portion of a text style run.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into

---

#### paint

public void paint​(

Graphics

g,

Shape

a)

Renders a portion of a text style run.

getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an axis.

This implementation returns the longest non-breakable area within
the view as a minimum span for

View.X_AXIS

.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either

View.X_AXIS

or

View.Y_AXIS
**Returns:** the minimum span the view can be rendered into
**Throws:** IllegalArgumentException

- if the

axis

parameter is invalid
**See Also:** View.getMinimumSpan(int)

---

#### getMinimumSpan

public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an axis.

This implementation returns the longest non-breakable area within
the view as a minimum span for

View.X_AXIS

.

This implementation returns the longest non-breakable area within
the view as a minimum span for

View.X_AXIS

.

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
axis. For the label, the alignment is along the font
baseline for the y axis, and the superclasses alignment
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment. This should be a value
between 0.0 and 1.0 inclusive, where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

---

#### getAlignment

public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. For the label, the alignment is along the font
baseline for the y axis, and the superclasses alignment
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

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
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
**Parameters:** biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the
zero-th element of this array
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

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

getBreakWeight

```java
public int getBreakWeight​(int axis,
float pos,
float len)
```

Determines how attractive a break opportunity in
this view is. This can be used for determining which
view is the most attractive to call

breakView

on in the process of formatting. The
higher the weight, the more attractive the break. A
value equal to or lower than

View.BadBreakWeight

should not be considered for a break. A value greater
than or equal to

View.ForcedBreakWeight

should
be broken.

This is implemented to forward to the superclass for
the Y_AXIS. Along the X_AXIS the following values
may be returned.

This will normally result in the behavior of breaking
on a whitespace location if one can be found, otherwise
breaking between characters.

**Overrides:** getBreakWeight

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Parameters:** pos

- the potential location of the start of the
broken view >= 0. This may be useful for calculating tab
positions.
**Parameters:** len

- specifies the relative length from

pos

where a potential break is desired >= 0.
**Returns:** the weight, which should be a value between
View.ForcedBreakWeight and View.BadBreakWeight.
**See Also:** LabelView

,

ParagraphView

,

View.BadBreakWeight

,

View.GoodBreakWeight

,

View.ExcellentBreakWeight

,

View.ForcedBreakWeight

---

#### getBreakWeight

public int getBreakWeight​(int axis,
float pos,
float len)

Determines how attractive a break opportunity in
this view is. This can be used for determining which
view is the most attractive to call

breakView

on in the process of formatting. The
higher the weight, the more attractive the break. A
value equal to or lower than

View.BadBreakWeight

should not be considered for a break. A value greater
than or equal to

View.ForcedBreakWeight

should
be broken.

This is implemented to forward to the superclass for
the Y_AXIS. Along the X_AXIS the following values
may be returned.

This will normally result in the behavior of breaking
on a whitespace location if one can be found, otherwise
breaking between characters.

This is implemented to forward to the superclass for
the Y_AXIS. Along the X_AXIS the following values
may be returned.

This will normally result in the behavior of breaking
on a whitespace location if one can be found, otherwise
breaking between characters.

breakView

```java
public
View
breakView​(int axis,
int p0,
float pos,
float len)
```

Breaks this view on the given axis at the given length.
This is implemented to attempt to break on a whitespace
location, and returns a fragment with the whitespace at
the end. If a whitespace location can't be found, the
nearest character is used.

**Overrides:** breakView

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Parameters:** p0

- the location in the model where the
fragment should start it's representation >= 0.
**Parameters:** pos

- the position along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
**Parameters:** len

- specifies the distance along the axis
where a potential break is desired >= 0.
**Returns:** the fragment of the view that represents the
given span, if the view can be broken. If the view
doesn't support breaking behavior, the view itself is
returned.
**See Also:** View.breakView(int, int, float, float)

---

#### breakView

public

View

breakView​(int axis,
int p0,
float pos,
float len)

Breaks this view on the given axis at the given length.
This is implemented to attempt to break on a whitespace
location, and returns a fragment with the whitespace at
the end. If a whitespace location can't be found, the
nearest character is used.

createFragment

```java
public
View
createFragment​(int p0,
int p1)
```

Creates a view that represents a portion of the element.
This is potentially useful during formatting operations
for taking measurements of fragments of the view. If
the view doesn't support fragmenting (the default), it
should return itself.

This view does support fragmenting. It is implemented
to return a nested class that shares state in this view
representing only a portion of the view.

**Overrides:** createFragment

in class

View
**Parameters:** p0

- the starting offset >= 0. This should be a value
greater or equal to the element starting offset and
less than the element ending offset.
**Parameters:** p1

- the ending offset > p0. This should be a value
less than or equal to the elements end offset and
greater than the elements starting offset.
**Returns:** the view fragment, or itself if the view doesn't
support breaking into fragments
**See Also:** LabelView

---

#### createFragment

public

View

createFragment​(int p0,
int p1)

Creates a view that represents a portion of the element.
This is potentially useful during formatting operations
for taking measurements of fragments of the view. If
the view doesn't support fragmenting (the default), it
should return itself.

This view does support fragmenting. It is implemented
to return a nested class that shares state in this view
representing only a portion of the view.

This view does support fragmenting. It is implemented
to return a nested class that shares state in this view
representing only a portion of the view.

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
location that one might place a caret. Some views may not be
visible, they might not be in the same order found in the model, or
they just might not allow access to some of the locations in the
model.
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
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
**Parameters:** b

- the bias
**Parameters:** biasRet

- the returned bias
**Returns:** the location within the model that best represents the next
location visual position.
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Throws:** IllegalArgumentException

- for an invalid direction

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
location that one might place a caret. Some views may not be
visible, they might not be in the same order found in the model, or
they just might not allow access to some of the locations in the
model.
This method enables specifying a position to convert
within the range of >=0. If the value is -1, a position
will be calculated automatically. If the value < -1,
the

BadLocationException

will be thrown.

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

Gives notification that something was inserted into
the document in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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

Gives notification that something was inserted into
the document in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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

Gives notification that something was removed from the document
in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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

Gives notification that something was removed from the document
in a location that this view is responsible for.
This is implemented to call preferenceChanged along the
axis the glyphs are rendered.

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
This is implemented to call preferenceChanged along both the
horizontal and vertical axis.

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
This is implemented to call preferenceChanged along both the
horizontal and vertical axis.

---

