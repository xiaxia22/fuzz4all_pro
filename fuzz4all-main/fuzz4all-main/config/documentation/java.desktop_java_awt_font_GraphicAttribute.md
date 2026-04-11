# Class GraphicAttribute

**Source:** `java.desktop\java\awt\font\GraphicAttribute.html`

### Class Description

```java
public abstract class
GraphicAttribute

extends
Object
```

This class is used with the CHAR_REPLACEMENT attribute.

The

GraphicAttribute

class represents a graphic embedded
in text. Clients subclass this class to implement their own char
replacement graphics. Clients wishing to embed shapes and images in
text need not subclass this class. Instead, clients can use the

ShapeGraphicAttribute

and

ImageGraphicAttribute

classes.

Subclasses must ensure that their objects are immutable once they
are constructed. Mutating a

GraphicAttribute

that
is used in a

TextLayout

results in undefined behavior from the

TextLayout

.

**Direct Known Subclasses:** ImageGraphicAttribute

,

ShapeGraphicAttribute

---

### Field Details

#### public static final int TOP_ALIGNMENT

Aligns top of graphic to top of line.

**See Also:**
- Constant Field Values

---

#### public static final int BOTTOM_ALIGNMENT

Aligns bottom of graphic to bottom of line.

**See Also:**
- Constant Field Values

---

#### public static final int ROMAN_BASELINE

Aligns origin of graphic to roman baseline of line.

**See Also:**
- Constant Field Values

---

#### public static final int CENTER_BASELINE

Aligns origin of graphic to center baseline of line.

**See Also:**
- Constant Field Values

---

#### public static final int HANGING_BASELINE

Aligns origin of graphic to hanging baseline of line.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected GraphicAttribute​(int alignment)

Constructs a

GraphicAttribute

.
Subclasses use this to define the alignment of the graphic.

**Parameters:**
- alignment

- an int representing one of the

GraphicAttribute

alignment fields

**Throws:**
- IllegalArgumentException

- if alignment is not one of the
five defined values.

---

### Method Details

#### public abstract float getAscent()

Returns the ascent of this

GraphicAttribute

. A
graphic can be rendered above its ascent.

**Returns:**
- the ascent of this

GraphicAttribute

.

**See Also:**
- getBounds()

---

#### public abstract float getDescent()

Returns the descent of this

GraphicAttribute

. A
graphic can be rendered below its descent.

**Returns:**
- the descent of this

GraphicAttribute

.

**See Also:**
- getBounds()

---

#### public abstract float getAdvance()

Returns the advance of this

GraphicAttribute

. The

GraphicAttribute

object's advance is the distance
from the point at which the graphic is rendered and the point where
the next character or graphic is rendered. A graphic can be
rendered beyond its advance

**Returns:**
- the advance of this

GraphicAttribute

.

**See Also:**
- getBounds()

---

#### public
Rectangle2D
getBounds()

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.
A graphic may be rendered beyond its origin, ascent, descent,
or advance; but if it is, this method's implementation must
indicate where the graphic is rendered.
Default bounds is the rectangle (0, -ascent, advance, ascent+descent).

**Returns:**
- a

Rectangle2D

that encloses all of the bits
rendered by this

GraphicAttribute

.

---

#### public
Shape
getOutline​(
AffineTransform
tx)

Return a

Shape

that represents the region that
this

GraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.
The default implementation returns the rectangle returned by

getBounds()

, transformed by the provided

AffineTransform

if present.

**Parameters:**
- tx

- an optional

AffineTransform

to apply to the
outline of this

GraphicAttribute

. This can be null.

**Returns:**
- a

Shape

representing this graphic attribute,
suitable for stroking or filling.

**Since:**
- 1.6

---

#### public abstract void draw​(
Graphics2D
graphics,
float x,
float y)

Renders this

GraphicAttribute

at the specified
location.

**Parameters:**
- graphics

- the

Graphics2D

into which to render the
graphic
- x

- the user-space X coordinate where the graphic is rendered
- y

- the user-space Y coordinate where the graphic is rendered

---

#### public final int getAlignment()

Returns the alignment of this

GraphicAttribute

.
Alignment can be to a particular baseline, or to the absolute top
or bottom of a line.

**Returns:**
- the alignment of this

GraphicAttribute

.

---

#### public
GlyphJustificationInfo
getJustificationInfo()

Returns the justification information for this

GraphicAttribute

. Subclasses
can override this method to provide different justification
information.

**Returns:**
- a

GlyphJustificationInfo

object that contains the
justification information for this

GraphicAttribute

.

---

### Additional Sections

#### Class GraphicAttribute

java.lang.Object

- java.awt.font.GraphicAttribute

java.awt.font.GraphicAttribute

**Direct Known Subclasses:** ImageGraphicAttribute

,

ShapeGraphicAttribute

```java
public abstract class
GraphicAttribute

extends
Object
```

This class is used with the CHAR_REPLACEMENT attribute.

The

GraphicAttribute

class represents a graphic embedded
in text. Clients subclass this class to implement their own char
replacement graphics. Clients wishing to embed shapes and images in
text need not subclass this class. Instead, clients can use the

ShapeGraphicAttribute

and

ImageGraphicAttribute

classes.

Subclasses must ensure that their objects are immutable once they
are constructed. Mutating a

GraphicAttribute

that
is used in a

TextLayout

results in undefined behavior from the

TextLayout

.

public abstract class

GraphicAttribute

extends

Object

This class is used with the CHAR_REPLACEMENT attribute.

The

GraphicAttribute

class represents a graphic embedded
in text. Clients subclass this class to implement their own char
replacement graphics. Clients wishing to embed shapes and images in
text need not subclass this class. Instead, clients can use the

ShapeGraphicAttribute

and

ImageGraphicAttribute

classes.

Subclasses must ensure that their objects are immutable once they
are constructed. Mutating a

GraphicAttribute

that
is used in a

TextLayout

results in undefined behavior from the

TextLayout

.

The

GraphicAttribute

class represents a graphic embedded
in text. Clients subclass this class to implement their own char
replacement graphics. Clients wishing to embed shapes and images in
text need not subclass this class. Instead, clients can use the

ShapeGraphicAttribute

and

ImageGraphicAttribute

classes.

Subclasses must ensure that their objects are immutable once they
are constructed. Mutating a

GraphicAttribute

that
is used in a

TextLayout

results in undefined behavior from the

TextLayout

.

Subclasses must ensure that their objects are immutable once they
are constructed. Mutating a

GraphicAttribute

that
is used in a

TextLayout

results in undefined behavior from the

TextLayout

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BOTTOM_ALIGNMENT

Aligns bottom of graphic to bottom of line.

static int

CENTER_BASELINE

Aligns origin of graphic to center baseline of line.

static int

HANGING_BASELINE

Aligns origin of graphic to hanging baseline of line.

static int

ROMAN_BASELINE

Aligns origin of graphic to roman baseline of line.

static int

TOP_ALIGNMENT

Aligns top of graphic to top of line.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

GraphicAttribute

​(int alignment)

Constructs a

GraphicAttribute

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

draw

​(

Graphics2D

graphics,
float x,
float y)

Renders this

GraphicAttribute

at the specified
location.

abstract float

getAdvance

()

Returns the advance of this

GraphicAttribute

.

int

getAlignment

()

Returns the alignment of this

GraphicAttribute

.

abstract float

getAscent

()

Returns the ascent of this

GraphicAttribute

.

Rectangle2D

getBounds

()

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.

abstract float

getDescent

()

Returns the descent of this

GraphicAttribute

.

GlyphJustificationInfo

getJustificationInfo

()

Returns the justification information for this

GraphicAttribute

.

Shape

getOutline

​(

AffineTransform

tx)

Return a

Shape

that represents the region that
this

GraphicAttribute

renders.

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

static int

BOTTOM_ALIGNMENT

Aligns bottom of graphic to bottom of line.

static int

CENTER_BASELINE

Aligns origin of graphic to center baseline of line.

static int

HANGING_BASELINE

Aligns origin of graphic to hanging baseline of line.

static int

ROMAN_BASELINE

Aligns origin of graphic to roman baseline of line.

static int

TOP_ALIGNMENT

Aligns top of graphic to top of line.

---

#### Field Summary

Aligns bottom of graphic to bottom of line.

Aligns origin of graphic to center baseline of line.

Aligns origin of graphic to hanging baseline of line.

Aligns origin of graphic to roman baseline of line.

Aligns top of graphic to top of line.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

GraphicAttribute

​(int alignment)

Constructs a

GraphicAttribute

.

---

#### Constructor Summary

Constructs a

GraphicAttribute

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

draw

​(

Graphics2D

graphics,
float x,
float y)

Renders this

GraphicAttribute

at the specified
location.

abstract float

getAdvance

()

Returns the advance of this

GraphicAttribute

.

int

getAlignment

()

Returns the alignment of this

GraphicAttribute

.

abstract float

getAscent

()

Returns the ascent of this

GraphicAttribute

.

Rectangle2D

getBounds

()

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.

abstract float

getDescent

()

Returns the descent of this

GraphicAttribute

.

GlyphJustificationInfo

getJustificationInfo

()

Returns the justification information for this

GraphicAttribute

.

Shape

getOutline

​(

AffineTransform

tx)

Return a

Shape

that represents the region that
this

GraphicAttribute

renders.

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

Renders this

GraphicAttribute

at the specified
location.

Returns the advance of this

GraphicAttribute

.

Returns the alignment of this

GraphicAttribute

.

Returns the ascent of this

GraphicAttribute

.

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.

Returns the descent of this

GraphicAttribute

.

Returns the justification information for this

GraphicAttribute

.

Return a

Shape

that represents the region that
this

GraphicAttribute

renders.

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

- TOP_ALIGNMENT

```java
public static final int TOP_ALIGNMENT
```

Aligns top of graphic to top of line.

**See Also:** Constant Field Values

- BOTTOM_ALIGNMENT

```java
public static final int BOTTOM_ALIGNMENT
```

Aligns bottom of graphic to bottom of line.

**See Also:** Constant Field Values

- ROMAN_BASELINE

```java
public static final int ROMAN_BASELINE
```

Aligns origin of graphic to roman baseline of line.

**See Also:** Constant Field Values

- CENTER_BASELINE

```java
public static final int CENTER_BASELINE
```

Aligns origin of graphic to center baseline of line.

**See Also:** Constant Field Values

- HANGING_BASELINE

```java
public static final int HANGING_BASELINE
```

Aligns origin of graphic to hanging baseline of line.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GraphicAttribute

```java
protected GraphicAttribute​(int alignment)
```

Constructs a

GraphicAttribute

.
Subclasses use this to define the alignment of the graphic.

**Parameters:** alignment

- an int representing one of the

GraphicAttribute

alignment fields
**Throws:** IllegalArgumentException

- if alignment is not one of the
five defined values.

============ METHOD DETAIL ==========

- Method Detail

- getAscent

```java
public abstract float getAscent()
```

Returns the ascent of this

GraphicAttribute

. A
graphic can be rendered above its ascent.

**Returns:** the ascent of this

GraphicAttribute

.
**See Also:** getBounds()

- getDescent

```java
public abstract float getDescent()
```

Returns the descent of this

GraphicAttribute

. A
graphic can be rendered below its descent.

**Returns:** the descent of this

GraphicAttribute

.
**See Also:** getBounds()

- getAdvance

```java
public abstract float getAdvance()
```

Returns the advance of this

GraphicAttribute

. The

GraphicAttribute

object's advance is the distance
from the point at which the graphic is rendered and the point where
the next character or graphic is rendered. A graphic can be
rendered beyond its advance

**Returns:** the advance of this

GraphicAttribute

.
**See Also:** getBounds()

- getBounds

```java
public
Rectangle2D
getBounds()
```

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.
A graphic may be rendered beyond its origin, ascent, descent,
or advance; but if it is, this method's implementation must
indicate where the graphic is rendered.
Default bounds is the rectangle (0, -ascent, advance, ascent+descent).

**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

GraphicAttribute

.

- getOutline

```java
public
Shape
getOutline​(
AffineTransform
tx)
```

Return a

Shape

that represents the region that
this

GraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.
The default implementation returns the rectangle returned by

getBounds()

, transformed by the provided

AffineTransform

if present.

**Parameters:** tx

- an optional

AffineTransform

to apply to the
outline of this

GraphicAttribute

. This can be null.
**Returns:** a

Shape

representing this graphic attribute,
suitable for stroking or filling.
**Since:** 1.6

- draw

```java
public abstract void draw​(
Graphics2D
graphics,
float x,
float y)
```

Renders this

GraphicAttribute

at the specified
location.

**Parameters:** graphics

- the

Graphics2D

into which to render the
graphic
**Parameters:** x

- the user-space X coordinate where the graphic is rendered
**Parameters:** y

- the user-space Y coordinate where the graphic is rendered

- getAlignment

```java
public final int getAlignment()
```

Returns the alignment of this

GraphicAttribute

.
Alignment can be to a particular baseline, or to the absolute top
or bottom of a line.

**Returns:** the alignment of this

GraphicAttribute

.

- getJustificationInfo

```java
public
GlyphJustificationInfo
getJustificationInfo()
```

Returns the justification information for this

GraphicAttribute

. Subclasses
can override this method to provide different justification
information.

**Returns:** a

GlyphJustificationInfo

object that contains the
justification information for this

GraphicAttribute

.

Field Detail

- TOP_ALIGNMENT

```java
public static final int TOP_ALIGNMENT
```

Aligns top of graphic to top of line.

**See Also:** Constant Field Values

- BOTTOM_ALIGNMENT

```java
public static final int BOTTOM_ALIGNMENT
```

Aligns bottom of graphic to bottom of line.

**See Also:** Constant Field Values

- ROMAN_BASELINE

```java
public static final int ROMAN_BASELINE
```

Aligns origin of graphic to roman baseline of line.

**See Also:** Constant Field Values

- CENTER_BASELINE

```java
public static final int CENTER_BASELINE
```

Aligns origin of graphic to center baseline of line.

**See Also:** Constant Field Values

- HANGING_BASELINE

```java
public static final int HANGING_BASELINE
```

Aligns origin of graphic to hanging baseline of line.

**See Also:** Constant Field Values

---

#### Field Detail

TOP_ALIGNMENT

```java
public static final int TOP_ALIGNMENT
```

Aligns top of graphic to top of line.

**See Also:** Constant Field Values

---

#### TOP_ALIGNMENT

public static final int TOP_ALIGNMENT

Aligns top of graphic to top of line.

BOTTOM_ALIGNMENT

```java
public static final int BOTTOM_ALIGNMENT
```

Aligns bottom of graphic to bottom of line.

**See Also:** Constant Field Values

---

#### BOTTOM_ALIGNMENT

public static final int BOTTOM_ALIGNMENT

Aligns bottom of graphic to bottom of line.

ROMAN_BASELINE

```java
public static final int ROMAN_BASELINE
```

Aligns origin of graphic to roman baseline of line.

**See Also:** Constant Field Values

---

#### ROMAN_BASELINE

public static final int ROMAN_BASELINE

Aligns origin of graphic to roman baseline of line.

CENTER_BASELINE

```java
public static final int CENTER_BASELINE
```

Aligns origin of graphic to center baseline of line.

**See Also:** Constant Field Values

---

#### CENTER_BASELINE

public static final int CENTER_BASELINE

Aligns origin of graphic to center baseline of line.

HANGING_BASELINE

```java
public static final int HANGING_BASELINE
```

Aligns origin of graphic to hanging baseline of line.

**See Also:** Constant Field Values

---

#### HANGING_BASELINE

public static final int HANGING_BASELINE

Aligns origin of graphic to hanging baseline of line.

Constructor Detail

- GraphicAttribute

```java
protected GraphicAttribute​(int alignment)
```

Constructs a

GraphicAttribute

.
Subclasses use this to define the alignment of the graphic.

**Parameters:** alignment

- an int representing one of the

GraphicAttribute

alignment fields
**Throws:** IllegalArgumentException

- if alignment is not one of the
five defined values.

---

#### Constructor Detail

GraphicAttribute

```java
protected GraphicAttribute​(int alignment)
```

Constructs a

GraphicAttribute

.
Subclasses use this to define the alignment of the graphic.

**Parameters:** alignment

- an int representing one of the

GraphicAttribute

alignment fields
**Throws:** IllegalArgumentException

- if alignment is not one of the
five defined values.

---

#### GraphicAttribute

protected GraphicAttribute​(int alignment)

Constructs a

GraphicAttribute

.
Subclasses use this to define the alignment of the graphic.

Method Detail

- getAscent

```java
public abstract float getAscent()
```

Returns the ascent of this

GraphicAttribute

. A
graphic can be rendered above its ascent.

**Returns:** the ascent of this

GraphicAttribute

.
**See Also:** getBounds()

- getDescent

```java
public abstract float getDescent()
```

Returns the descent of this

GraphicAttribute

. A
graphic can be rendered below its descent.

**Returns:** the descent of this

GraphicAttribute

.
**See Also:** getBounds()

- getAdvance

```java
public abstract float getAdvance()
```

Returns the advance of this

GraphicAttribute

. The

GraphicAttribute

object's advance is the distance
from the point at which the graphic is rendered and the point where
the next character or graphic is rendered. A graphic can be
rendered beyond its advance

**Returns:** the advance of this

GraphicAttribute

.
**See Also:** getBounds()

- getBounds

```java
public
Rectangle2D
getBounds()
```

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.
A graphic may be rendered beyond its origin, ascent, descent,
or advance; but if it is, this method's implementation must
indicate where the graphic is rendered.
Default bounds is the rectangle (0, -ascent, advance, ascent+descent).

**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

GraphicAttribute

.

- getOutline

```java
public
Shape
getOutline​(
AffineTransform
tx)
```

Return a

Shape

that represents the region that
this

GraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.
The default implementation returns the rectangle returned by

getBounds()

, transformed by the provided

AffineTransform

if present.

**Parameters:** tx

- an optional

AffineTransform

to apply to the
outline of this

GraphicAttribute

. This can be null.
**Returns:** a

Shape

representing this graphic attribute,
suitable for stroking or filling.
**Since:** 1.6

- draw

```java
public abstract void draw​(
Graphics2D
graphics,
float x,
float y)
```

Renders this

GraphicAttribute

at the specified
location.

**Parameters:** graphics

- the

Graphics2D

into which to render the
graphic
**Parameters:** x

- the user-space X coordinate where the graphic is rendered
**Parameters:** y

- the user-space Y coordinate where the graphic is rendered

- getAlignment

```java
public final int getAlignment()
```

Returns the alignment of this

GraphicAttribute

.
Alignment can be to a particular baseline, or to the absolute top
or bottom of a line.

**Returns:** the alignment of this

GraphicAttribute

.

- getJustificationInfo

```java
public
GlyphJustificationInfo
getJustificationInfo()
```

Returns the justification information for this

GraphicAttribute

. Subclasses
can override this method to provide different justification
information.

**Returns:** a

GlyphJustificationInfo

object that contains the
justification information for this

GraphicAttribute

.

---

#### Method Detail

getAscent

```java
public abstract float getAscent()
```

Returns the ascent of this

GraphicAttribute

. A
graphic can be rendered above its ascent.

**Returns:** the ascent of this

GraphicAttribute

.
**See Also:** getBounds()

---

#### getAscent

public abstract float getAscent()

Returns the ascent of this

GraphicAttribute

. A
graphic can be rendered above its ascent.

getDescent

```java
public abstract float getDescent()
```

Returns the descent of this

GraphicAttribute

. A
graphic can be rendered below its descent.

**Returns:** the descent of this

GraphicAttribute

.
**See Also:** getBounds()

---

#### getDescent

public abstract float getDescent()

Returns the descent of this

GraphicAttribute

. A
graphic can be rendered below its descent.

getAdvance

```java
public abstract float getAdvance()
```

Returns the advance of this

GraphicAttribute

. The

GraphicAttribute

object's advance is the distance
from the point at which the graphic is rendered and the point where
the next character or graphic is rendered. A graphic can be
rendered beyond its advance

**Returns:** the advance of this

GraphicAttribute

.
**See Also:** getBounds()

---

#### getAdvance

public abstract float getAdvance()

Returns the advance of this

GraphicAttribute

. The

GraphicAttribute

object's advance is the distance
from the point at which the graphic is rendered and the point where
the next character or graphic is rendered. A graphic can be
rendered beyond its advance

getBounds

```java
public
Rectangle2D
getBounds()
```

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.
A graphic may be rendered beyond its origin, ascent, descent,
or advance; but if it is, this method's implementation must
indicate where the graphic is rendered.
Default bounds is the rectangle (0, -ascent, advance, ascent+descent).

**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

GraphicAttribute

.

---

#### getBounds

public

Rectangle2D

getBounds()

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

GraphicAttribute

relative to the
rendering position.
A graphic may be rendered beyond its origin, ascent, descent,
or advance; but if it is, this method's implementation must
indicate where the graphic is rendered.
Default bounds is the rectangle (0, -ascent, advance, ascent+descent).

getOutline

```java
public
Shape
getOutline​(
AffineTransform
tx)
```

Return a

Shape

that represents the region that
this

GraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.
The default implementation returns the rectangle returned by

getBounds()

, transformed by the provided

AffineTransform

if present.

**Parameters:** tx

- an optional

AffineTransform

to apply to the
outline of this

GraphicAttribute

. This can be null.
**Returns:** a

Shape

representing this graphic attribute,
suitable for stroking or filling.
**Since:** 1.6

---

#### getOutline

public

Shape

getOutline​(

AffineTransform

tx)

Return a

Shape

that represents the region that
this

GraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.
The default implementation returns the rectangle returned by

getBounds()

, transformed by the provided

AffineTransform

if present.

draw

```java
public abstract void draw​(
Graphics2D
graphics,
float x,
float y)
```

Renders this

GraphicAttribute

at the specified
location.

**Parameters:** graphics

- the

Graphics2D

into which to render the
graphic
**Parameters:** x

- the user-space X coordinate where the graphic is rendered
**Parameters:** y

- the user-space Y coordinate where the graphic is rendered

---

#### draw

public abstract void draw​(

Graphics2D

graphics,
float x,
float y)

Renders this

GraphicAttribute

at the specified
location.

getAlignment

```java
public final int getAlignment()
```

Returns the alignment of this

GraphicAttribute

.
Alignment can be to a particular baseline, or to the absolute top
or bottom of a line.

**Returns:** the alignment of this

GraphicAttribute

.

---

#### getAlignment

public final int getAlignment()

Returns the alignment of this

GraphicAttribute

.
Alignment can be to a particular baseline, or to the absolute top
or bottom of a line.

getJustificationInfo

```java
public
GlyphJustificationInfo
getJustificationInfo()
```

Returns the justification information for this

GraphicAttribute

. Subclasses
can override this method to provide different justification
information.

**Returns:** a

GlyphJustificationInfo

object that contains the
justification information for this

GraphicAttribute

.

---

#### getJustificationInfo

public

GlyphJustificationInfo

getJustificationInfo()

Returns the justification information for this

GraphicAttribute

. Subclasses
can override this method to provide different justification
information.

---

