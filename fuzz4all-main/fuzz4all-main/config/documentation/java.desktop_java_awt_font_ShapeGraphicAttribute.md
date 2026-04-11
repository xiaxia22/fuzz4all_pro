# Class ShapeGraphicAttribute

**Source:** `java.desktop\java\awt\font\ShapeGraphicAttribute.html`

### Class Description

```java
public final class
ShapeGraphicAttribute

extends
GraphicAttribute
```

The

ShapeGraphicAttribute

class is an implementation of

GraphicAttribute

that draws shapes in a

TextLayout

.

**See Also:** GraphicAttribute

---

### Field Details

#### public static final boolean STROKE

A key indicating the shape should be stroked with a 1-pixel wide stroke.

**See Also:**
- Constant Field Values

---

#### public static final boolean FILL

A key indicating the shape should be filled.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ShapeGraphicAttribute​(
Shape
shape,
int alignment,
boolean stroke)

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

**Parameters:**
- shape

- the

Shape

to render. The

Shape

is rendered with its origin at the origin of
this

ShapeGraphicAttribute

in the
host

TextLayout

. This object maintains a reference to

shape

.
- alignment

- one of the alignments from this

ShapeGraphicAttribute

.
- stroke

-

true

if the

Shape

should be
stroked;

false

if the

Shape

should be
filled.

---

### Method Details

#### public float getAscent()

Returns the ascent of this

ShapeGraphicAttribute

. The
ascent of a

ShapeGraphicAttribute

is the positive
distance from the origin of its

Shape

to the top of
bounds of its

Shape

.

**Specified by:**
- getAscent

in class

GraphicAttribute

**Returns:**
- the ascent of this

ShapeGraphicAttribute

.

**See Also:**
- GraphicAttribute.getBounds()

---

#### public float getDescent()

Returns the descent of this

ShapeGraphicAttribute

.
The descent of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the bottom of the
bounds of its

Shape

.

**Specified by:**
- getDescent

in class

GraphicAttribute

**Returns:**
- the descent of this

ShapeGraphicAttribute

.

**See Also:**
- GraphicAttribute.getBounds()

---

#### public float getAdvance()

Returns the advance of this

ShapeGraphicAttribute

.
The advance of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the right side of the
bounds of its

Shape

.

**Specified by:**
- getAdvance

in class

GraphicAttribute

**Returns:**
- the advance of this

ShapeGraphicAttribute

.

**See Also:**
- GraphicAttribute.getBounds()

---

#### public
Rectangle2D
getBounds()

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

ShapeGraphicAttribute

relative to
the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it does, this method's
implementation should indicate where the graphic is rendered.

**Overrides:**
- getBounds

in class

GraphicAttribute

**Returns:**
- a

Rectangle2D

that encloses all of the bits
rendered by this

ShapeGraphicAttribute

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

ShapeGraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.

**Overrides:**
- getOutline

in class

GraphicAttribute

**Parameters:**
- tx

- an optional

AffineTransform

to apply to the
this

ShapeGraphicAttribute

. This can be null.

**Returns:**
- the

Shape

representing this graphic attribute,
suitable for stroking or filling.

**Since:**
- 1.6

---

#### public int hashCode()

Returns a hashcode for this

ShapeGraphicAttribute

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this

ShapeGraphicAttribute

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
rhs)

Compares this

ShapeGraphicAttribute

to the specified

Object

.

**Overrides:**
- equals

in class

Object

**Parameters:**
- rhs

- the

Object

to compare for equality

**Returns:**
- true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public boolean equals​(
ShapeGraphicAttribute
rhs)

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

**Parameters:**
- rhs

- the

ShapeGraphicAttribute

to compare for
equality

**Returns:**
- true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.

---

### Additional Sections

#### Class ShapeGraphicAttribute

java.lang.Object

- java.awt.font.GraphicAttribute
- - java.awt.font.ShapeGraphicAttribute

java.awt.font.GraphicAttribute

- java.awt.font.ShapeGraphicAttribute

java.awt.font.ShapeGraphicAttribute

```java
public final class
ShapeGraphicAttribute

extends
GraphicAttribute
```

The

ShapeGraphicAttribute

class is an implementation of

GraphicAttribute

that draws shapes in a

TextLayout

.

**See Also:** GraphicAttribute

public final class

ShapeGraphicAttribute

extends

GraphicAttribute

The

ShapeGraphicAttribute

class is an implementation of

GraphicAttribute

that draws shapes in a

TextLayout

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static boolean

FILL

A key indicating the shape should be filled.

static boolean

STROKE

A key indicating the shape should be stroked with a 1-pixel wide stroke.

- Fields declared in class java.awt.font.

GraphicAttribute

BOTTOM_ALIGNMENT

,

CENTER_BASELINE

,

HANGING_BASELINE

,

ROMAN_BASELINE

,

TOP_ALIGNMENT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ShapeGraphicAttribute

​(

Shape

shape,
int alignment,
boolean stroke)

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

ShapeGraphicAttribute

rhs)

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

boolean

equals

​(

Object

rhs)

Compares this

ShapeGraphicAttribute

to the specified

Object

.

float

getAdvance

()

Returns the advance of this

ShapeGraphicAttribute

.

float

getAscent

()

Returns the ascent of this

ShapeGraphicAttribute

.

Rectangle2D

getBounds

()

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

ShapeGraphicAttribute

relative to
the rendering position.

float

getDescent

()

Returns the descent of this

ShapeGraphicAttribute

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

ShapeGraphicAttribute

renders.

int

hashCode

()

Returns a hashcode for this

ShapeGraphicAttribute

.

- Methods declared in class java.awt.font.

GraphicAttribute

draw

,

getAlignment

,

getJustificationInfo

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

static boolean

FILL

A key indicating the shape should be filled.

static boolean

STROKE

A key indicating the shape should be stroked with a 1-pixel wide stroke.

- Fields declared in class java.awt.font.

GraphicAttribute

BOTTOM_ALIGNMENT

,

CENTER_BASELINE

,

HANGING_BASELINE

,

ROMAN_BASELINE

,

TOP_ALIGNMENT

---

#### Field Summary

A key indicating the shape should be filled.

A key indicating the shape should be stroked with a 1-pixel wide stroke.

Fields declared in class java.awt.font.

GraphicAttribute

BOTTOM_ALIGNMENT

,

CENTER_BASELINE

,

HANGING_BASELINE

,

ROMAN_BASELINE

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt.font. GraphicAttribute

Constructor Summary

Constructors

Constructor

Description

ShapeGraphicAttribute

​(

Shape

shape,
int alignment,
boolean stroke)

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

---

#### Constructor Summary

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

ShapeGraphicAttribute

rhs)

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

boolean

equals

​(

Object

rhs)

Compares this

ShapeGraphicAttribute

to the specified

Object

.

float

getAdvance

()

Returns the advance of this

ShapeGraphicAttribute

.

float

getAscent

()

Returns the ascent of this

ShapeGraphicAttribute

.

Rectangle2D

getBounds

()

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

ShapeGraphicAttribute

relative to
the rendering position.

float

getDescent

()

Returns the descent of this

ShapeGraphicAttribute

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

ShapeGraphicAttribute

renders.

int

hashCode

()

Returns a hashcode for this

ShapeGraphicAttribute

.

- Methods declared in class java.awt.font.

GraphicAttribute

draw

,

getAlignment

,

getJustificationInfo

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

Compares this

ShapeGraphicAttribute

to the specified

Object

.

Returns the advance of this

ShapeGraphicAttribute

.

Returns the ascent of this

ShapeGraphicAttribute

.

Returns a

Rectangle2D

that encloses all of the
bits drawn by this

ShapeGraphicAttribute

relative to
the rendering position.

Returns the descent of this

ShapeGraphicAttribute

.

Return a

Shape

that represents the region that
this

ShapeGraphicAttribute

renders.

Returns a hashcode for this

ShapeGraphicAttribute

.

Methods declared in class java.awt.font.

GraphicAttribute

draw

,

getAlignment

,

getJustificationInfo

---

#### Methods declared in class java.awt.font. GraphicAttribute

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- STROKE

```java
public static final boolean STROKE
```

A key indicating the shape should be stroked with a 1-pixel wide stroke.

**See Also:** Constant Field Values

- FILL

```java
public static final boolean FILL
```

A key indicating the shape should be filled.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ShapeGraphicAttribute

```java
public ShapeGraphicAttribute​(
Shape
shape,
int alignment,
boolean stroke)
```

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

**Parameters:** shape

- the

Shape

to render. The

Shape

is rendered with its origin at the origin of
this

ShapeGraphicAttribute

in the
host

TextLayout

. This object maintains a reference to

shape

.
**Parameters:** alignment

- one of the alignments from this

ShapeGraphicAttribute

.
**Parameters:** stroke

-

true

if the

Shape

should be
stroked;

false

if the

Shape

should be
filled.

============ METHOD DETAIL ==========

- Method Detail

- getAscent

```java
public float getAscent()
```

Returns the ascent of this

ShapeGraphicAttribute

. The
ascent of a

ShapeGraphicAttribute

is the positive
distance from the origin of its

Shape

to the top of
bounds of its

Shape

.

**Specified by:** getAscent

in class

GraphicAttribute
**Returns:** the ascent of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getDescent

```java
public float getDescent()
```

Returns the descent of this

ShapeGraphicAttribute

.
The descent of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the bottom of the
bounds of its

Shape

.

**Specified by:** getDescent

in class

GraphicAttribute
**Returns:** the descent of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getAdvance

```java
public float getAdvance()
```

Returns the advance of this

ShapeGraphicAttribute

.
The advance of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the right side of the
bounds of its

Shape

.

**Specified by:** getAdvance

in class

GraphicAttribute
**Returns:** the advance of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

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

ShapeGraphicAttribute

relative to
the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it does, this method's
implementation should indicate where the graphic is rendered.

**Overrides:** getBounds

in class

GraphicAttribute
**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

ShapeGraphicAttribute

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

ShapeGraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.

**Overrides:** getOutline

in class

GraphicAttribute
**Parameters:** tx

- an optional

AffineTransform

to apply to the
this

ShapeGraphicAttribute

. This can be null.
**Returns:** the

Shape

representing this graphic attribute,
suitable for stroking or filling.
**Since:** 1.6

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

ShapeGraphicAttribute

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

ShapeGraphicAttribute

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
rhs)
```

Compares this

ShapeGraphicAttribute

to the specified

Object

.

**Overrides:** equals

in class

Object
**Parameters:** rhs

- the

Object

to compare for equality
**Returns:** true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- equals

```java
public boolean equals​(
ShapeGraphicAttribute
rhs)
```

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

**Parameters:** rhs

- the

ShapeGraphicAttribute

to compare for
equality
**Returns:** true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.

Field Detail

- STROKE

```java
public static final boolean STROKE
```

A key indicating the shape should be stroked with a 1-pixel wide stroke.

**See Also:** Constant Field Values

- FILL

```java
public static final boolean FILL
```

A key indicating the shape should be filled.

**See Also:** Constant Field Values

---

#### Field Detail

STROKE

```java
public static final boolean STROKE
```

A key indicating the shape should be stroked with a 1-pixel wide stroke.

**See Also:** Constant Field Values

---

#### STROKE

public static final boolean STROKE

A key indicating the shape should be stroked with a 1-pixel wide stroke.

FILL

```java
public static final boolean FILL
```

A key indicating the shape should be filled.

**See Also:** Constant Field Values

---

#### FILL

public static final boolean FILL

A key indicating the shape should be filled.

Constructor Detail

- ShapeGraphicAttribute

```java
public ShapeGraphicAttribute​(
Shape
shape,
int alignment,
boolean stroke)
```

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

**Parameters:** shape

- the

Shape

to render. The

Shape

is rendered with its origin at the origin of
this

ShapeGraphicAttribute

in the
host

TextLayout

. This object maintains a reference to

shape

.
**Parameters:** alignment

- one of the alignments from this

ShapeGraphicAttribute

.
**Parameters:** stroke

-

true

if the

Shape

should be
stroked;

false

if the

Shape

should be
filled.

---

#### Constructor Detail

ShapeGraphicAttribute

```java
public ShapeGraphicAttribute​(
Shape
shape,
int alignment,
boolean stroke)
```

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

**Parameters:** shape

- the

Shape

to render. The

Shape

is rendered with its origin at the origin of
this

ShapeGraphicAttribute

in the
host

TextLayout

. This object maintains a reference to

shape

.
**Parameters:** alignment

- one of the alignments from this

ShapeGraphicAttribute

.
**Parameters:** stroke

-

true

if the

Shape

should be
stroked;

false

if the

Shape

should be
filled.

---

#### ShapeGraphicAttribute

public ShapeGraphicAttribute​(

Shape

shape,
int alignment,
boolean stroke)

Constructs a

ShapeGraphicAttribute

for the specified

Shape

.

Method Detail

- getAscent

```java
public float getAscent()
```

Returns the ascent of this

ShapeGraphicAttribute

. The
ascent of a

ShapeGraphicAttribute

is the positive
distance from the origin of its

Shape

to the top of
bounds of its

Shape

.

**Specified by:** getAscent

in class

GraphicAttribute
**Returns:** the ascent of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getDescent

```java
public float getDescent()
```

Returns the descent of this

ShapeGraphicAttribute

.
The descent of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the bottom of the
bounds of its

Shape

.

**Specified by:** getDescent

in class

GraphicAttribute
**Returns:** the descent of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getAdvance

```java
public float getAdvance()
```

Returns the advance of this

ShapeGraphicAttribute

.
The advance of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the right side of the
bounds of its

Shape

.

**Specified by:** getAdvance

in class

GraphicAttribute
**Returns:** the advance of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

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

ShapeGraphicAttribute

relative to
the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it does, this method's
implementation should indicate where the graphic is rendered.

**Overrides:** getBounds

in class

GraphicAttribute
**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

ShapeGraphicAttribute

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

ShapeGraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.

**Overrides:** getOutline

in class

GraphicAttribute
**Parameters:** tx

- an optional

AffineTransform

to apply to the
this

ShapeGraphicAttribute

. This can be null.
**Returns:** the

Shape

representing this graphic attribute,
suitable for stroking or filling.
**Since:** 1.6

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

ShapeGraphicAttribute

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

ShapeGraphicAttribute

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
rhs)
```

Compares this

ShapeGraphicAttribute

to the specified

Object

.

**Overrides:** equals

in class

Object
**Parameters:** rhs

- the

Object

to compare for equality
**Returns:** true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- equals

```java
public boolean equals​(
ShapeGraphicAttribute
rhs)
```

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

**Parameters:** rhs

- the

ShapeGraphicAttribute

to compare for
equality
**Returns:** true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.

---

#### Method Detail

getAscent

```java
public float getAscent()
```

Returns the ascent of this

ShapeGraphicAttribute

. The
ascent of a

ShapeGraphicAttribute

is the positive
distance from the origin of its

Shape

to the top of
bounds of its

Shape

.

**Specified by:** getAscent

in class

GraphicAttribute
**Returns:** the ascent of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

---

#### getAscent

public float getAscent()

Returns the ascent of this

ShapeGraphicAttribute

. The
ascent of a

ShapeGraphicAttribute

is the positive
distance from the origin of its

Shape

to the top of
bounds of its

Shape

.

getDescent

```java
public float getDescent()
```

Returns the descent of this

ShapeGraphicAttribute

.
The descent of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the bottom of the
bounds of its

Shape

.

**Specified by:** getDescent

in class

GraphicAttribute
**Returns:** the descent of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

---

#### getDescent

public float getDescent()

Returns the descent of this

ShapeGraphicAttribute

.
The descent of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the bottom of the
bounds of its

Shape

.

getAdvance

```java
public float getAdvance()
```

Returns the advance of this

ShapeGraphicAttribute

.
The advance of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the right side of the
bounds of its

Shape

.

**Specified by:** getAdvance

in class

GraphicAttribute
**Returns:** the advance of this

ShapeGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

---

#### getAdvance

public float getAdvance()

Returns the advance of this

ShapeGraphicAttribute

.
The advance of a

ShapeGraphicAttribute

is the distance
from the origin of its

Shape

to the right side of the
bounds of its

Shape

.

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

ShapeGraphicAttribute

relative to
the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it does, this method's
implementation should indicate where the graphic is rendered.

**Overrides:** getBounds

in class

GraphicAttribute
**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

ShapeGraphicAttribute

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

ShapeGraphicAttribute

relative to
the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it does, this method's
implementation should indicate where the graphic is rendered.

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

ShapeGraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.

**Overrides:** getOutline

in class

GraphicAttribute
**Parameters:** tx

- an optional

AffineTransform

to apply to the
this

ShapeGraphicAttribute

. This can be null.
**Returns:** the

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

ShapeGraphicAttribute

renders. This is used when a

TextLayout

is requested to return the outline of the text.
The (untransformed) shape must not extend outside the rectangular
bounds returned by

getBounds

.

hashCode

```java
public int hashCode()
```

Returns a hashcode for this

ShapeGraphicAttribute

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

ShapeGraphicAttribute

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this

ShapeGraphicAttribute

.

equals

```java
public boolean equals​(
Object
rhs)
```

Compares this

ShapeGraphicAttribute

to the specified

Object

.

**Overrides:** equals

in class

Object
**Parameters:** rhs

- the

Object

to compare for equality
**Returns:** true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

rhs)

Compares this

ShapeGraphicAttribute

to the specified

Object

.

equals

```java
public boolean equals​(
ShapeGraphicAttribute
rhs)
```

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

**Parameters:** rhs

- the

ShapeGraphicAttribute

to compare for
equality
**Returns:** true

if this

ShapeGraphicAttribute

equals

rhs

;

false

otherwise.

---

#### equals

public boolean equals​(

ShapeGraphicAttribute

rhs)

Compares this

ShapeGraphicAttribute

to the specified

ShapeGraphicAttribute

.

---

