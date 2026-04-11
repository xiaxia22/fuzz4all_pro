# Class GlyphView.GlyphPainter

**Source:** `java.desktop\javax\swing\text\GlyphView.GlyphPainter.html`

### Class Description

```java
public abstract static class
GlyphView.GlyphPainter

extends
Object
```

A class to perform rendering of the glyphs.
This can be implemented to be stateless, or
to hold some information as a cache to
facilitate faster rendering and model/view
translation. At a minimum, the GlyphPainter
allows a View implementation to perform its
duties independent of a particular version
of JVM and selection of capabilities (i.e.
shaping for i18n, etc).

**Enclosing class:** GlyphView

---

### Field Details

*No entries found.*

### Constructor Details

#### public GlyphPainter()

*No description found.*

---

### Method Details

#### public abstract float getSpan​(
GlyphView
v,
int p0,
int p1,

TabExpander
e,
float x)

Determine the span the glyphs given a start location
(for tab expansion).

**Parameters:**
- v

- the

GlyphView
- p0

- the beginning position
- p1

- the ending position
- e

- how to expand the tabs when encountered
- x

- the X coordinate

**Returns:**
- the span the glyphs given a start location

---

#### public abstract float getHeight​(
GlyphView
v)

Returns of the height.

**Parameters:**
- v

- the

GlyphView

**Returns:**
- of the height

---

#### public abstract float getAscent​(
GlyphView
v)

Returns of the ascent.

**Parameters:**
- v

- the

GlyphView

**Returns:**
- of the ascent

---

#### public abstract float getDescent​(
GlyphView
v)

Returns of the descent.

**Parameters:**
- v

- the

GlyphView

**Returns:**
- of the descent

---

#### public abstract void paint​(
GlyphView
v,

Graphics
g,

Shape
a,
int p0,
int p1)

Paint the glyphs representing the given range.

**Parameters:**
- v

- the

GlyphView
- g

- the graphics context
- a

- the current allocation of the view
- p0

- the beginning position
- p1

- the ending position

---

#### public abstract
Shape
modelToView​(
GlyphView
v,
int pos,

Position.Bias
bias,

Shape
a)
throws
BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.
This is shared by the broken views.

**Parameters:**
- v

- the

GlyphView

containing the
destination coordinate space
- pos

- the position to convert
- bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
- a

- Bounds of the View

**Returns:**
- the bounding box of the given position

**Throws:**
- BadLocationException

- if the given position does not represent a
valid location in the associated document

**See Also:**
- View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### public abstract int viewToModel​(
GlyphView
v,
float x,
float y,

Shape
a,

Position.Bias
[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:**
- v

- the

GlyphView

to provide a mapping for
- x

- the X coordinate
- y

- the Y coordinate
- a

- the allocated region to render into
- biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array

**Returns:**
- the location within the model that best represents the
given point of view

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### public abstract int getBoundedPosition​(
GlyphView
v,
int p0,
float x,
float len)

Determines the model location that represents the
maximum advance that fits within the given span.
This could be used to break the given view. The result
should be a location just shy of the given advance. This
differs from viewToModel which returns the closest
position which might be proud of the maximum advance.

**Parameters:**
- v

- the view to find the model location to break at.
- p0

- the location in the model where the
fragment should start it's representation >= 0.
- x

- the graphic location along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
- len

- specifies the distance into the view
where a potential break is desired >= 0.

**Returns:**
- the maximum model location possible for a break.

**See Also:**
- View.breakView(int, int, float, float)

---

#### public
GlyphView.GlyphPainter
getPainter​(
GlyphView
v,
int p0,
int p1)

Create a painter to use for the given GlyphView. If
the painter carries state it can create another painter
to represent a new GlyphView that is being created. If
the painter doesn't hold any significant state, it can
return itself. The default behavior is to return itself.

**Parameters:**
- v

- the

GlyphView

to provide a painter for
- p0

- the starting document offset >= 0
- p1

- the ending document offset >= p0

**Returns:**
- a painter to use for the given GlyphView

---

#### public int getNextVisualPositionFrom​(
GlyphView
v,
int pos,

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

**Parameters:**
- v

- the view to use
- pos

- the position to convert >= 0
- b

- either

Position.Bias.Forward

or

Position.Bias.Backward
- a

- the allocated region to render into
- direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
- biasRet

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array

**Returns:**
- the location within the model that best represents the next
location visual position.

**Throws:**
- BadLocationException

- for a bad location within a document model
- IllegalArgumentException

- for an invalid direction

---

### Additional Sections

#### Class GlyphView.GlyphPainter

java.lang.Object

- javax.swing.text.GlyphView.GlyphPainter

javax.swing.text.GlyphView.GlyphPainter

**Enclosing class:** GlyphView

```java
public abstract static class
GlyphView.GlyphPainter

extends
Object
```

A class to perform rendering of the glyphs.
This can be implemented to be stateless, or
to hold some information as a cache to
facilitate faster rendering and model/view
translation. At a minimum, the GlyphPainter
allows a View implementation to perform its
duties independent of a particular version
of JVM and selection of capabilities (i.e.
shaping for i18n, etc).

**Since:** 1.3

public abstract static class

GlyphView.GlyphPainter

extends

Object

A class to perform rendering of the glyphs.
This can be implemented to be stateless, or
to hold some information as a cache to
facilitate faster rendering and model/view
translation. At a minimum, the GlyphPainter
allows a View implementation to perform its
duties independent of a particular version
of JVM and selection of capabilities (i.e.
shaping for i18n, etc).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GlyphPainter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract float

getAscent

​(

GlyphView

v)

Returns of the ascent.

abstract int

getBoundedPosition

​(

GlyphView

v,
int p0,
float x,
float len)

Determines the model location that represents the
maximum advance that fits within the given span.

abstract float

getDescent

​(

GlyphView

v)

Returns of the descent.

abstract float

getHeight

​(

GlyphView

v)

Returns of the height.

int

getNextVisualPositionFrom

​(

GlyphView

v,
int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Provides a way to determine the next visually represented model
location that one might place a caret.

GlyphView.GlyphPainter

getPainter

​(

GlyphView

v,
int p0,
int p1)

Create a painter to use for the given GlyphView.

abstract float

getSpan

​(

GlyphView

v,
int p0,
int p1,

TabExpander

e,
float x)

Determine the span the glyphs given a start location
(for tab expansion).

abstract

Shape

modelToView

​(

GlyphView

v,
int pos,

Position.Bias

bias,

Shape

a)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

abstract void

paint

​(

GlyphView

v,

Graphics

g,

Shape

a,
int p0,
int p1)

Paint the glyphs representing the given range.

abstract int

viewToModel

​(

GlyphView

v,
float x,
float y,

Shape

a,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

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

Constructor Summary

Constructors

Constructor

Description

GlyphPainter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract float

getAscent

​(

GlyphView

v)

Returns of the ascent.

abstract int

getBoundedPosition

​(

GlyphView

v,
int p0,
float x,
float len)

Determines the model location that represents the
maximum advance that fits within the given span.

abstract float

getDescent

​(

GlyphView

v)

Returns of the descent.

abstract float

getHeight

​(

GlyphView

v)

Returns of the height.

int

getNextVisualPositionFrom

​(

GlyphView

v,
int pos,

Position.Bias

b,

Shape

a,
int direction,

Position.Bias

[] biasRet)

Provides a way to determine the next visually represented model
location that one might place a caret.

GlyphView.GlyphPainter

getPainter

​(

GlyphView

v,
int p0,
int p1)

Create a painter to use for the given GlyphView.

abstract float

getSpan

​(

GlyphView

v,
int p0,
int p1,

TabExpander

e,
float x)

Determine the span the glyphs given a start location
(for tab expansion).

abstract

Shape

modelToView

​(

GlyphView

v,
int pos,

Position.Bias

bias,

Shape

a)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

abstract void

paint

​(

GlyphView

v,

Graphics

g,

Shape

a,
int p0,
int p1)

Paint the glyphs representing the given range.

abstract int

viewToModel

​(

GlyphView

v,
float x,
float y,

Shape

a,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

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

Returns of the ascent.

Determines the model location that represents the
maximum advance that fits within the given span.

Returns of the descent.

Returns of the height.

Provides a way to determine the next visually represented model
location that one might place a caret.

Create a painter to use for the given GlyphView.

Determine the span the glyphs given a start location
(for tab expansion).

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Paint the glyphs representing the given range.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

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

- GlyphPainter

```java
public GlyphPainter()
```

============ METHOD DETAIL ==========

- Method Detail

- getSpan

```java
public abstract float getSpan​(
GlyphView
v,
int p0,
int p1,

TabExpander
e,
float x)
```

Determine the span the glyphs given a start location
(for tab expansion).

**Parameters:** v

- the

GlyphView
**Parameters:** p0

- the beginning position
**Parameters:** p1

- the ending position
**Parameters:** e

- how to expand the tabs when encountered
**Parameters:** x

- the X coordinate
**Returns:** the span the glyphs given a start location

- getHeight

```java
public abstract float getHeight​(
GlyphView
v)
```

Returns of the height.

**Parameters:** v

- the

GlyphView
**Returns:** of the height

- getAscent

```java
public abstract float getAscent​(
GlyphView
v)
```

Returns of the ascent.

**Parameters:** v

- the

GlyphView
**Returns:** of the ascent

- getDescent

```java
public abstract float getDescent​(
GlyphView
v)
```

Returns of the descent.

**Parameters:** v

- the

GlyphView
**Returns:** of the descent

- paint

```java
public abstract void paint​(
GlyphView
v,

Graphics
g,

Shape
a,
int p0,
int p1)
```

Paint the glyphs representing the given range.

**Parameters:** v

- the

GlyphView
**Parameters:** g

- the graphics context
**Parameters:** a

- the current allocation of the view
**Parameters:** p0

- the beginning position
**Parameters:** p1

- the ending position

- modelToView

```java
public abstract
Shape
modelToView​(
GlyphView
v,
int pos,

Position.Bias
bias,

Shape
a)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.
This is shared by the broken views.

**Parameters:** v

- the

GlyphView

containing the
destination coordinate space
**Parameters:** pos

- the position to convert
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- Bounds of the View
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public abstract int viewToModel​(
GlyphView
v,
float x,
float y,

Shape
a,

Position.Bias
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:** v

- the

GlyphView

to provide a mapping for
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** a

- the allocated region to render into
**Parameters:** biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array
**Returns:** the location within the model that best represents the
given point of view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getBoundedPosition

```java
public abstract int getBoundedPosition​(
GlyphView
v,
int p0,
float x,
float len)
```

Determines the model location that represents the
maximum advance that fits within the given span.
This could be used to break the given view. The result
should be a location just shy of the given advance. This
differs from viewToModel which returns the closest
position which might be proud of the maximum advance.

**Parameters:** v

- the view to find the model location to break at.
**Parameters:** p0

- the location in the model where the
fragment should start it's representation >= 0.
**Parameters:** x

- the graphic location along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
**Parameters:** len

- specifies the distance into the view
where a potential break is desired >= 0.
**Returns:** the maximum model location possible for a break.
**See Also:** View.breakView(int, int, float, float)

- getPainter

```java
public
GlyphView.GlyphPainter
getPainter​(
GlyphView
v,
int p0,
int p1)
```

Create a painter to use for the given GlyphView. If
the painter carries state it can create another painter
to represent a new GlyphView that is being created. If
the painter doesn't hold any significant state, it can
return itself. The default behavior is to return itself.

**Parameters:** v

- the

GlyphView

to provide a painter for
**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** a painter to use for the given GlyphView

- getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(
GlyphView
v,
int pos,

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

**Parameters:** v

- the view to use
**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
**Parameters:** biasRet

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array
**Returns:** the location within the model that best represents the next
location visual position.
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- for an invalid direction

Constructor Detail

- GlyphPainter

```java
public GlyphPainter()
```

---

#### Constructor Detail

GlyphPainter

```java
public GlyphPainter()
```

---

#### GlyphPainter

public GlyphPainter()

Method Detail

- getSpan

```java
public abstract float getSpan​(
GlyphView
v,
int p0,
int p1,

TabExpander
e,
float x)
```

Determine the span the glyphs given a start location
(for tab expansion).

**Parameters:** v

- the

GlyphView
**Parameters:** p0

- the beginning position
**Parameters:** p1

- the ending position
**Parameters:** e

- how to expand the tabs when encountered
**Parameters:** x

- the X coordinate
**Returns:** the span the glyphs given a start location

- getHeight

```java
public abstract float getHeight​(
GlyphView
v)
```

Returns of the height.

**Parameters:** v

- the

GlyphView
**Returns:** of the height

- getAscent

```java
public abstract float getAscent​(
GlyphView
v)
```

Returns of the ascent.

**Parameters:** v

- the

GlyphView
**Returns:** of the ascent

- getDescent

```java
public abstract float getDescent​(
GlyphView
v)
```

Returns of the descent.

**Parameters:** v

- the

GlyphView
**Returns:** of the descent

- paint

```java
public abstract void paint​(
GlyphView
v,

Graphics
g,

Shape
a,
int p0,
int p1)
```

Paint the glyphs representing the given range.

**Parameters:** v

- the

GlyphView
**Parameters:** g

- the graphics context
**Parameters:** a

- the current allocation of the view
**Parameters:** p0

- the beginning position
**Parameters:** p1

- the ending position

- modelToView

```java
public abstract
Shape
modelToView​(
GlyphView
v,
int pos,

Position.Bias
bias,

Shape
a)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.
This is shared by the broken views.

**Parameters:** v

- the

GlyphView

containing the
destination coordinate space
**Parameters:** pos

- the position to convert
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- Bounds of the View
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public abstract int viewToModel​(
GlyphView
v,
float x,
float y,

Shape
a,

Position.Bias
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:** v

- the

GlyphView

to provide a mapping for
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** a

- the allocated region to render into
**Parameters:** biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array
**Returns:** the location within the model that best represents the
given point of view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getBoundedPosition

```java
public abstract int getBoundedPosition​(
GlyphView
v,
int p0,
float x,
float len)
```

Determines the model location that represents the
maximum advance that fits within the given span.
This could be used to break the given view. The result
should be a location just shy of the given advance. This
differs from viewToModel which returns the closest
position which might be proud of the maximum advance.

**Parameters:** v

- the view to find the model location to break at.
**Parameters:** p0

- the location in the model where the
fragment should start it's representation >= 0.
**Parameters:** x

- the graphic location along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
**Parameters:** len

- specifies the distance into the view
where a potential break is desired >= 0.
**Returns:** the maximum model location possible for a break.
**See Also:** View.breakView(int, int, float, float)

- getPainter

```java
public
GlyphView.GlyphPainter
getPainter​(
GlyphView
v,
int p0,
int p1)
```

Create a painter to use for the given GlyphView. If
the painter carries state it can create another painter
to represent a new GlyphView that is being created. If
the painter doesn't hold any significant state, it can
return itself. The default behavior is to return itself.

**Parameters:** v

- the

GlyphView

to provide a painter for
**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** a painter to use for the given GlyphView

- getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(
GlyphView
v,
int pos,

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

**Parameters:** v

- the view to use
**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
**Parameters:** biasRet

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array
**Returns:** the location within the model that best represents the next
location visual position.
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- for an invalid direction

---

#### Method Detail

getSpan

```java
public abstract float getSpan​(
GlyphView
v,
int p0,
int p1,

TabExpander
e,
float x)
```

Determine the span the glyphs given a start location
(for tab expansion).

**Parameters:** v

- the

GlyphView
**Parameters:** p0

- the beginning position
**Parameters:** p1

- the ending position
**Parameters:** e

- how to expand the tabs when encountered
**Parameters:** x

- the X coordinate
**Returns:** the span the glyphs given a start location

---

#### getSpan

public abstract float getSpan​(

GlyphView

v,
int p0,
int p1,

TabExpander

e,
float x)

Determine the span the glyphs given a start location
(for tab expansion).

getHeight

```java
public abstract float getHeight​(
GlyphView
v)
```

Returns of the height.

**Parameters:** v

- the

GlyphView
**Returns:** of the height

---

#### getHeight

public abstract float getHeight​(

GlyphView

v)

Returns of the height.

getAscent

```java
public abstract float getAscent​(
GlyphView
v)
```

Returns of the ascent.

**Parameters:** v

- the

GlyphView
**Returns:** of the ascent

---

#### getAscent

public abstract float getAscent​(

GlyphView

v)

Returns of the ascent.

getDescent

```java
public abstract float getDescent​(
GlyphView
v)
```

Returns of the descent.

**Parameters:** v

- the

GlyphView
**Returns:** of the descent

---

#### getDescent

public abstract float getDescent​(

GlyphView

v)

Returns of the descent.

paint

```java
public abstract void paint​(
GlyphView
v,

Graphics
g,

Shape
a,
int p0,
int p1)
```

Paint the glyphs representing the given range.

**Parameters:** v

- the

GlyphView
**Parameters:** g

- the graphics context
**Parameters:** a

- the current allocation of the view
**Parameters:** p0

- the beginning position
**Parameters:** p1

- the ending position

---

#### paint

public abstract void paint​(

GlyphView

v,

Graphics

g,

Shape

a,
int p0,
int p1)

Paint the glyphs representing the given range.

modelToView

```java
public abstract
Shape
modelToView​(
GlyphView
v,
int pos,

Position.Bias
bias,

Shape
a)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.
This is shared by the broken views.

**Parameters:** v

- the

GlyphView

containing the
destination coordinate space
**Parameters:** pos

- the position to convert
**Parameters:** bias

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- Bounds of the View
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### modelToView

public abstract

Shape

modelToView​(

GlyphView

v,
int pos,

Position.Bias

bias,

Shape

a)
throws

BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.
This is shared by the broken views.

viewToModel

```java
public abstract int viewToModel​(
GlyphView
v,
float x,
float y,

Shape
a,

Position.Bias
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:** v

- the

GlyphView

to provide a mapping for
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** a

- the allocated region to render into
**Parameters:** biasReturn

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array
**Returns:** the location within the model that best represents the
given point of view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### viewToModel

public abstract int viewToModel​(

GlyphView

v,
float x,
float y,

Shape

a,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

getBoundedPosition

```java
public abstract int getBoundedPosition​(
GlyphView
v,
int p0,
float x,
float len)
```

Determines the model location that represents the
maximum advance that fits within the given span.
This could be used to break the given view. The result
should be a location just shy of the given advance. This
differs from viewToModel which returns the closest
position which might be proud of the maximum advance.

**Parameters:** v

- the view to find the model location to break at.
**Parameters:** p0

- the location in the model where the
fragment should start it's representation >= 0.
**Parameters:** x

- the graphic location along the axis that the
broken view would occupy >= 0. This may be useful for
things like tab calculations.
**Parameters:** len

- specifies the distance into the view
where a potential break is desired >= 0.
**Returns:** the maximum model location possible for a break.
**See Also:** View.breakView(int, int, float, float)

---

#### getBoundedPosition

public abstract int getBoundedPosition​(

GlyphView

v,
int p0,
float x,
float len)

Determines the model location that represents the
maximum advance that fits within the given span.
This could be used to break the given view. The result
should be a location just shy of the given advance. This
differs from viewToModel which returns the closest
position which might be proud of the maximum advance.

getPainter

```java
public
GlyphView.GlyphPainter
getPainter​(
GlyphView
v,
int p0,
int p1)
```

Create a painter to use for the given GlyphView. If
the painter carries state it can create another painter
to represent a new GlyphView that is being created. If
the painter doesn't hold any significant state, it can
return itself. The default behavior is to return itself.

**Parameters:** v

- the

GlyphView

to provide a painter for
**Parameters:** p0

- the starting document offset >= 0
**Parameters:** p1

- the ending document offset >= p0
**Returns:** a painter to use for the given GlyphView

---

#### getPainter

public

GlyphView.GlyphPainter

getPainter​(

GlyphView

v,
int p0,
int p1)

Create a painter to use for the given GlyphView. If
the painter carries state it can create another painter
to represent a new GlyphView that is being created. If
the painter doesn't hold any significant state, it can
return itself. The default behavior is to return itself.

getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(
GlyphView
v,
int pos,

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

**Parameters:** v

- the view to use
**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- either

Position.Bias.Forward

or

Position.Bias.Backward
**Parameters:** a

- the allocated region to render into
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH.
**Parameters:** biasRet

- either

Position.Bias.Forward

or

Position.Bias.Backward

is returned as the zero-th element of this array
**Returns:** the location within the model that best represents the next
location visual position.
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- for an invalid direction

---

#### getNextVisualPositionFrom

public int getNextVisualPositionFrom​(

GlyphView

v,
int pos,

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

---

