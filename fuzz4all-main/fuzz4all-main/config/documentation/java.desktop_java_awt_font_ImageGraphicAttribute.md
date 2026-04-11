# Class ImageGraphicAttribute

**Source:** `java.desktop\java\awt\font\ImageGraphicAttribute.html`

### Class Description

```java
public final class
ImageGraphicAttribute

extends
GraphicAttribute
```

The

ImageGraphicAttribute

class is an implementation of

GraphicAttribute

which draws images in
a

TextLayout

.

**See Also:** GraphicAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public ImageGraphicAttribute​(
Image
image,
int alignment)

Constructs an

ImageGraphicAttribute

from the specified

Image

. The origin is at (0, 0).

**Parameters:**
- image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
- alignment

- one of the alignments from this

ImageGraphicAttribute

---

#### public ImageGraphicAttribute​(
Image
image,
int alignment,
float originX,
float originY)

Constructs an

ImageGraphicAttribute

from the specified

Image

. The point
(

originX

,

originY

) in the

Image

appears at the origin of the

ImageGraphicAttribute

within the text.

**Parameters:**
- image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
- alignment

- one of the alignments from this

ImageGraphicAttribute
- originX

- the X coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.
- originY

- the Y coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.

---

### Method Details

#### public float getAscent()

Returns the ascent of this

ImageGraphicAttribute

. The
ascent of an

ImageGraphicAttribute

is the distance
from the top of the image to the origin.

**Specified by:**
- getAscent

in class

GraphicAttribute

**Returns:**
- the ascent of this

ImageGraphicAttribute

.

**See Also:**
- GraphicAttribute.getBounds()

---

#### public float getDescent()

Returns the descent of this

ImageGraphicAttribute

.
The descent of an

ImageGraphicAttribute

is the
distance from the origin to the bottom of the image.

**Specified by:**
- getDescent

in class

GraphicAttribute

**Returns:**
- the descent of this

ImageGraphicAttribute

.

**See Also:**
- GraphicAttribute.getBounds()

---

#### public float getAdvance()

Returns the advance of this

ImageGraphicAttribute

.
The advance of an

ImageGraphicAttribute

is the
distance from the origin to the right edge of the image.

**Specified by:**
- getAdvance

in class

GraphicAttribute

**Returns:**
- the advance of this

ImageGraphicAttribute

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
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it is, this
method's implementation must indicate where the graphic is rendered.

**Overrides:**
- getBounds

in class

GraphicAttribute

**Returns:**
- a

Rectangle2D

that encloses all of the bits
rendered by this

ImageGraphicAttribute

.

---

#### public int hashCode()

Returns a hashcode for this

ImageGraphicAttribute

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
rhs)

Compares this

ImageGraphicAttribute

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

ImageGraphicAttribute

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
ImageGraphicAttribute
rhs)

Compares this

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

**Parameters:**
- rhs

- the

ImageGraphicAttribute

to compare for
equality

**Returns:**
- true

if this

ImageGraphicAttribute

equals

rhs

;

false

otherwise.

---

### Additional Sections

#### Class ImageGraphicAttribute

java.lang.Object

- java.awt.font.GraphicAttribute
- - java.awt.font.ImageGraphicAttribute

java.awt.font.GraphicAttribute

- java.awt.font.ImageGraphicAttribute

java.awt.font.ImageGraphicAttribute

```java
public final class
ImageGraphicAttribute

extends
GraphicAttribute
```

The

ImageGraphicAttribute

class is an implementation of

GraphicAttribute

which draws images in
a

TextLayout

.

**See Also:** GraphicAttribute

public final class

ImageGraphicAttribute

extends

GraphicAttribute

The

ImageGraphicAttribute

class is an implementation of

GraphicAttribute

which draws images in
a

TextLayout

.

=========== FIELD SUMMARY ===========

- Field Summary

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

ImageGraphicAttribute

​(

Image

image,
int alignment)

Constructs an

ImageGraphicAttribute

from the specified

Image

.

ImageGraphicAttribute

​(

Image

image,
int alignment,
float originX,
float originY)

Constructs an

ImageGraphicAttribute

from the specified

Image

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

ImageGraphicAttribute

rhs)

Compares this

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

boolean

equals

​(

Object

rhs)

Compares this

ImageGraphicAttribute

to the specified

Object

.

float

getAdvance

()

Returns the advance of this

ImageGraphicAttribute

.

float

getAscent

()

Returns the ascent of this

ImageGraphicAttribute

.

Rectangle2D

getBounds

()

Returns a

Rectangle2D

that encloses all of the
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position.

float

getDescent

()

Returns the descent of this

ImageGraphicAttribute

.

int

hashCode

()

Returns a hashcode for this

ImageGraphicAttribute

.

- Methods declared in class java.awt.font.

GraphicAttribute

draw

,

getAlignment

,

getJustificationInfo

,

getOutline

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

ImageGraphicAttribute

​(

Image

image,
int alignment)

Constructs an

ImageGraphicAttribute

from the specified

Image

.

ImageGraphicAttribute

​(

Image

image,
int alignment,
float originX,
float originY)

Constructs an

ImageGraphicAttribute

from the specified

Image

.

---

#### Constructor Summary

Constructs an

ImageGraphicAttribute

from the specified

Image

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

ImageGraphicAttribute

rhs)

Compares this

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

boolean

equals

​(

Object

rhs)

Compares this

ImageGraphicAttribute

to the specified

Object

.

float

getAdvance

()

Returns the advance of this

ImageGraphicAttribute

.

float

getAscent

()

Returns the ascent of this

ImageGraphicAttribute

.

Rectangle2D

getBounds

()

Returns a

Rectangle2D

that encloses all of the
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position.

float

getDescent

()

Returns the descent of this

ImageGraphicAttribute

.

int

hashCode

()

Returns a hashcode for this

ImageGraphicAttribute

.

- Methods declared in class java.awt.font.

GraphicAttribute

draw

,

getAlignment

,

getJustificationInfo

,

getOutline

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

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

Compares this

ImageGraphicAttribute

to the specified

Object

.

Returns the advance of this

ImageGraphicAttribute

.

Returns the ascent of this

ImageGraphicAttribute

.

Returns a

Rectangle2D

that encloses all of the
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position.

Returns the descent of this

ImageGraphicAttribute

.

Returns a hashcode for this

ImageGraphicAttribute

.

Methods declared in class java.awt.font.

GraphicAttribute

draw

,

getAlignment

,

getJustificationInfo

,

getOutline

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageGraphicAttribute

```java
public ImageGraphicAttribute​(
Image
image,
int alignment)
```

Constructs an

ImageGraphicAttribute

from the specified

Image

. The origin is at (0, 0).

**Parameters:** image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
**Parameters:** alignment

- one of the alignments from this

ImageGraphicAttribute

- ImageGraphicAttribute

```java
public ImageGraphicAttribute​(
Image
image,
int alignment,
float originX,
float originY)
```

Constructs an

ImageGraphicAttribute

from the specified

Image

. The point
(

originX

,

originY

) in the

Image

appears at the origin of the

ImageGraphicAttribute

within the text.

**Parameters:** image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
**Parameters:** alignment

- one of the alignments from this

ImageGraphicAttribute
**Parameters:** originX

- the X coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.
**Parameters:** originY

- the Y coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.

============ METHOD DETAIL ==========

- Method Detail

- getAscent

```java
public float getAscent()
```

Returns the ascent of this

ImageGraphicAttribute

. The
ascent of an

ImageGraphicAttribute

is the distance
from the top of the image to the origin.

**Specified by:** getAscent

in class

GraphicAttribute
**Returns:** the ascent of this

ImageGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getDescent

```java
public float getDescent()
```

Returns the descent of this

ImageGraphicAttribute

.
The descent of an

ImageGraphicAttribute

is the
distance from the origin to the bottom of the image.

**Specified by:** getDescent

in class

GraphicAttribute
**Returns:** the descent of this

ImageGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getAdvance

```java
public float getAdvance()
```

Returns the advance of this

ImageGraphicAttribute

.
The advance of an

ImageGraphicAttribute

is the
distance from the origin to the right edge of the image.

**Specified by:** getAdvance

in class

GraphicAttribute
**Returns:** the advance of this

ImageGraphicAttribute

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
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it is, this
method's implementation must indicate where the graphic is rendered.

**Overrides:** getBounds

in class

GraphicAttribute
**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

ImageGraphicAttribute

.

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

ImageGraphicAttribute

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
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

ImageGraphicAttribute

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

ImageGraphicAttribute

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
ImageGraphicAttribute
rhs)
```

Compares this

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

**Parameters:** rhs

- the

ImageGraphicAttribute

to compare for
equality
**Returns:** true

if this

ImageGraphicAttribute

equals

rhs

;

false

otherwise.

Constructor Detail

- ImageGraphicAttribute

```java
public ImageGraphicAttribute​(
Image
image,
int alignment)
```

Constructs an

ImageGraphicAttribute

from the specified

Image

. The origin is at (0, 0).

**Parameters:** image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
**Parameters:** alignment

- one of the alignments from this

ImageGraphicAttribute

- ImageGraphicAttribute

```java
public ImageGraphicAttribute​(
Image
image,
int alignment,
float originX,
float originY)
```

Constructs an

ImageGraphicAttribute

from the specified

Image

. The point
(

originX

,

originY

) in the

Image

appears at the origin of the

ImageGraphicAttribute

within the text.

**Parameters:** image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
**Parameters:** alignment

- one of the alignments from this

ImageGraphicAttribute
**Parameters:** originX

- the X coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.
**Parameters:** originY

- the Y coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.

---

#### Constructor Detail

ImageGraphicAttribute

```java
public ImageGraphicAttribute​(
Image
image,
int alignment)
```

Constructs an

ImageGraphicAttribute

from the specified

Image

. The origin is at (0, 0).

**Parameters:** image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
**Parameters:** alignment

- one of the alignments from this

ImageGraphicAttribute

---

#### ImageGraphicAttribute

public ImageGraphicAttribute​(

Image

image,
int alignment)

Constructs an

ImageGraphicAttribute

from the specified

Image

. The origin is at (0, 0).

ImageGraphicAttribute

```java
public ImageGraphicAttribute​(
Image
image,
int alignment,
float originX,
float originY)
```

Constructs an

ImageGraphicAttribute

from the specified

Image

. The point
(

originX

,

originY

) in the

Image

appears at the origin of the

ImageGraphicAttribute

within the text.

**Parameters:** image

- the

Image

rendered by this

ImageGraphicAttribute

.
This object keeps a reference to

image

.
**Parameters:** alignment

- one of the alignments from this

ImageGraphicAttribute
**Parameters:** originX

- the X coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.
**Parameters:** originY

- the Y coordinate of the point within
the

Image

that appears at the origin of the

ImageGraphicAttribute

in the text line.

---

#### ImageGraphicAttribute

public ImageGraphicAttribute​(

Image

image,
int alignment,
float originX,
float originY)

Constructs an

ImageGraphicAttribute

from the specified

Image

. The point
(

originX

,

originY

) in the

Image

appears at the origin of the

ImageGraphicAttribute

within the text.

Method Detail

- getAscent

```java
public float getAscent()
```

Returns the ascent of this

ImageGraphicAttribute

. The
ascent of an

ImageGraphicAttribute

is the distance
from the top of the image to the origin.

**Specified by:** getAscent

in class

GraphicAttribute
**Returns:** the ascent of this

ImageGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getDescent

```java
public float getDescent()
```

Returns the descent of this

ImageGraphicAttribute

.
The descent of an

ImageGraphicAttribute

is the
distance from the origin to the bottom of the image.

**Specified by:** getDescent

in class

GraphicAttribute
**Returns:** the descent of this

ImageGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

- getAdvance

```java
public float getAdvance()
```

Returns the advance of this

ImageGraphicAttribute

.
The advance of an

ImageGraphicAttribute

is the
distance from the origin to the right edge of the image.

**Specified by:** getAdvance

in class

GraphicAttribute
**Returns:** the advance of this

ImageGraphicAttribute

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
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it is, this
method's implementation must indicate where the graphic is rendered.

**Overrides:** getBounds

in class

GraphicAttribute
**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

ImageGraphicAttribute

.

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

ImageGraphicAttribute

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
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

ImageGraphicAttribute

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

ImageGraphicAttribute

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
ImageGraphicAttribute
rhs)
```

Compares this

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

**Parameters:** rhs

- the

ImageGraphicAttribute

to compare for
equality
**Returns:** true

if this

ImageGraphicAttribute

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

ImageGraphicAttribute

. The
ascent of an

ImageGraphicAttribute

is the distance
from the top of the image to the origin.

**Specified by:** getAscent

in class

GraphicAttribute
**Returns:** the ascent of this

ImageGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

---

#### getAscent

public float getAscent()

Returns the ascent of this

ImageGraphicAttribute

. The
ascent of an

ImageGraphicAttribute

is the distance
from the top of the image to the origin.

getDescent

```java
public float getDescent()
```

Returns the descent of this

ImageGraphicAttribute

.
The descent of an

ImageGraphicAttribute

is the
distance from the origin to the bottom of the image.

**Specified by:** getDescent

in class

GraphicAttribute
**Returns:** the descent of this

ImageGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

---

#### getDescent

public float getDescent()

Returns the descent of this

ImageGraphicAttribute

.
The descent of an

ImageGraphicAttribute

is the
distance from the origin to the bottom of the image.

getAdvance

```java
public float getAdvance()
```

Returns the advance of this

ImageGraphicAttribute

.
The advance of an

ImageGraphicAttribute

is the
distance from the origin to the right edge of the image.

**Specified by:** getAdvance

in class

GraphicAttribute
**Returns:** the advance of this

ImageGraphicAttribute

.
**See Also:** GraphicAttribute.getBounds()

---

#### getAdvance

public float getAdvance()

Returns the advance of this

ImageGraphicAttribute

.
The advance of an

ImageGraphicAttribute

is the
distance from the origin to the right edge of the image.

getBounds

```java
public
Rectangle2D
getBounds()
```

Returns a

Rectangle2D

that encloses all of the
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it is, this
method's implementation must indicate where the graphic is rendered.

**Overrides:** getBounds

in class

GraphicAttribute
**Returns:** a

Rectangle2D

that encloses all of the bits
rendered by this

ImageGraphicAttribute

.

---

#### getBounds

public

Rectangle2D

getBounds()

Returns a

Rectangle2D

that encloses all of the
bits rendered by this

ImageGraphicAttribute

, relative
to the rendering position. A graphic can be rendered beyond its
origin, ascent, descent, or advance; but if it is, this
method's implementation must indicate where the graphic is rendered.

hashCode

```java
public int hashCode()
```

Returns a hashcode for this

ImageGraphicAttribute

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this

ImageGraphicAttribute

.

equals

```java
public boolean equals​(
Object
rhs)
```

Compares this

ImageGraphicAttribute

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

ImageGraphicAttribute

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

ImageGraphicAttribute

to the specified

Object

.

equals

```java
public boolean equals​(
ImageGraphicAttribute
rhs)
```

Compares this

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

**Parameters:** rhs

- the

ImageGraphicAttribute

to compare for
equality
**Returns:** true

if this

ImageGraphicAttribute

equals

rhs

;

false

otherwise.

---

#### equals

public boolean equals​(

ImageGraphicAttribute

rhs)

Compares this

ImageGraphicAttribute

to the specified

ImageGraphicAttribute

.

---

