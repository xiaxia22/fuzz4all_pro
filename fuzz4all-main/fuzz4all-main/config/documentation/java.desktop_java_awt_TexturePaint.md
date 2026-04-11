# Class TexturePaint

**Source:** `java.desktop\java\awt\TexturePaint.html`

### Class Description

```java
public class
TexturePaint

extends
Object

implements
Paint
```

The

TexturePaint

class provides a way to fill a

Shape

with a texture that is specified as
a

BufferedImage

. The size of the

BufferedImage

object should be small because the

BufferedImage

data
is copied by the

TexturePaint

object.
At construction time, the texture is anchored to the upper
left corner of a

Rectangle2D

that is
specified in user space. Texture is computed for
locations in the device space by conceptually replicating the
specified

Rectangle2D

infinitely in all directions
in user space and mapping the

BufferedImage

to each
replicated

Rectangle2D

.

**All Implemented Interfaces:** Paint

,

Transparency

---

### Field Details

*No entries found.*

### Constructor Details

#### public TexturePaint​(
BufferedImage
txtr,

Rectangle2D
anchor)

Constructs a

TexturePaint

object.

**Parameters:**
- txtr

- the

BufferedImage

object with the texture
used for painting
- anchor

- the

Rectangle2D

in user space used to
anchor and replicate the texture

---

### Method Details

#### public
BufferedImage
getImage()

Returns the

BufferedImage

texture used to
fill the shapes.

**Returns:**
- a

BufferedImage

.

---

#### public
Rectangle2D
getAnchorRect()

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

**Returns:**
- the

Rectangle2D

used to anchor and
size this

TexturePaint

.

---

#### public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
xform,

RenderingHints
hints)

Creates and returns a

PaintContext

used to
generate a tiled image pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:**
- createContext

in interface

Paint

**Parameters:**
- cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
- deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
- userBounds

- the user space bounding box
of the graphics primitive being rendered.
- xform

- the

AffineTransform

from user
space into device space.
- hints

- the set of hints that the context object can use to
choose between rendering alternatives.

**Returns:**
- the

PaintContext

for
generating color patterns.

**See Also:**
- Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

---

#### public int getTransparency()

Returns the transparency mode for this

TexturePaint

.

**Specified by:**
- getTransparency

in interface

Transparency

**Returns:**
- the transparency mode for this

TexturePaint

as an integer value.

**See Also:**
- Transparency

---

### Additional Sections

#### Class TexturePaint

java.lang.Object

- java.awt.TexturePaint

java.awt.TexturePaint

**All Implemented Interfaces:** Paint

,

Transparency

```java
public class
TexturePaint

extends
Object

implements
Paint
```

The

TexturePaint

class provides a way to fill a

Shape

with a texture that is specified as
a

BufferedImage

. The size of the

BufferedImage

object should be small because the

BufferedImage

data
is copied by the

TexturePaint

object.
At construction time, the texture is anchored to the upper
left corner of a

Rectangle2D

that is
specified in user space. Texture is computed for
locations in the device space by conceptually replicating the
specified

Rectangle2D

infinitely in all directions
in user space and mapping the

BufferedImage

to each
replicated

Rectangle2D

.

**See Also:** Paint

,

Graphics2D.setPaint(java.awt.Paint)

public class

TexturePaint

extends

Object

implements

Paint

The

TexturePaint

class provides a way to fill a

Shape

with a texture that is specified as
a

BufferedImage

. The size of the

BufferedImage

object should be small because the

BufferedImage

data
is copied by the

TexturePaint

object.
At construction time, the texture is anchored to the upper
left corner of a

Rectangle2D

that is
specified in user space. Texture is computed for
locations in the device space by conceptually replicating the
specified

Rectangle2D

infinitely in all directions
in user space and mapping the

BufferedImage

to each
replicated

Rectangle2D

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TexturePaint

​(

BufferedImage

txtr,

Rectangle2D

anchor)

Constructs a

TexturePaint

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PaintContext

createContext

​(

ColorModel

cm,

Rectangle

deviceBounds,

Rectangle2D

userBounds,

AffineTransform

xform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a tiled image pattern.

Rectangle2D

getAnchorRect

()

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

BufferedImage

getImage

()

Returns the

BufferedImage

texture used to
fill the shapes.

int

getTransparency

()

Returns the transparency mode for this

TexturePaint

.

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

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Field Summary

Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Fields declared in interface java.awt. Transparency

Constructor Summary

Constructors

Constructor

Description

TexturePaint

​(

BufferedImage

txtr,

Rectangle2D

anchor)

Constructs a

TexturePaint

object.

---

#### Constructor Summary

Constructs a

TexturePaint

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PaintContext

createContext

​(

ColorModel

cm,

Rectangle

deviceBounds,

Rectangle2D

userBounds,

AffineTransform

xform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a tiled image pattern.

Rectangle2D

getAnchorRect

()

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

BufferedImage

getImage

()

Returns the

BufferedImage

texture used to
fill the shapes.

int

getTransparency

()

Returns the transparency mode for this

TexturePaint

.

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

Creates and returns a

PaintContext

used to
generate a tiled image pattern.

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

Returns the

BufferedImage

texture used to
fill the shapes.

Returns the transparency mode for this

TexturePaint

.

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

- TexturePaint

```java
public TexturePaint​(
BufferedImage
txtr,

Rectangle2D
anchor)
```

Constructs a

TexturePaint

object.

**Parameters:** txtr

- the

BufferedImage

object with the texture
used for painting
**Parameters:** anchor

- the

Rectangle2D

in user space used to
anchor and replicate the texture

============ METHOD DETAIL ==========

- Method Detail

- getImage

```java
public
BufferedImage
getImage()
```

Returns the

BufferedImage

texture used to
fill the shapes.

**Returns:** a

BufferedImage

.

- getAnchorRect

```java
public
Rectangle2D
getAnchorRect()
```

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

**Returns:** the

Rectangle2D

used to anchor and
size this

TexturePaint

.

- createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
xform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a tiled image pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:** createContext

in interface

Paint
**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** userBounds

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** xform

- the

AffineTransform

from user
space into device space.
**Parameters:** hints

- the set of hints that the context object can use to
choose between rendering alternatives.
**Returns:** the

PaintContext

for
generating color patterns.
**See Also:** Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

- getTransparency

```java
public int getTransparency()
```

Returns the transparency mode for this

TexturePaint

.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** the transparency mode for this

TexturePaint

as an integer value.
**See Also:** Transparency

Constructor Detail

- TexturePaint

```java
public TexturePaint​(
BufferedImage
txtr,

Rectangle2D
anchor)
```

Constructs a

TexturePaint

object.

**Parameters:** txtr

- the

BufferedImage

object with the texture
used for painting
**Parameters:** anchor

- the

Rectangle2D

in user space used to
anchor and replicate the texture

---

#### Constructor Detail

TexturePaint

```java
public TexturePaint​(
BufferedImage
txtr,

Rectangle2D
anchor)
```

Constructs a

TexturePaint

object.

**Parameters:** txtr

- the

BufferedImage

object with the texture
used for painting
**Parameters:** anchor

- the

Rectangle2D

in user space used to
anchor and replicate the texture

---

#### TexturePaint

public TexturePaint​(

BufferedImage

txtr,

Rectangle2D

anchor)

Constructs a

TexturePaint

object.

Method Detail

- getImage

```java
public
BufferedImage
getImage()
```

Returns the

BufferedImage

texture used to
fill the shapes.

**Returns:** a

BufferedImage

.

- getAnchorRect

```java
public
Rectangle2D
getAnchorRect()
```

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

**Returns:** the

Rectangle2D

used to anchor and
size this

TexturePaint

.

- createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
xform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a tiled image pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:** createContext

in interface

Paint
**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** userBounds

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** xform

- the

AffineTransform

from user
space into device space.
**Parameters:** hints

- the set of hints that the context object can use to
choose between rendering alternatives.
**Returns:** the

PaintContext

for
generating color patterns.
**See Also:** Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

- getTransparency

```java
public int getTransparency()
```

Returns the transparency mode for this

TexturePaint

.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** the transparency mode for this

TexturePaint

as an integer value.
**See Also:** Transparency

---

#### Method Detail

getImage

```java
public
BufferedImage
getImage()
```

Returns the

BufferedImage

texture used to
fill the shapes.

**Returns:** a

BufferedImage

.

---

#### getImage

public

BufferedImage

getImage()

Returns the

BufferedImage

texture used to
fill the shapes.

getAnchorRect

```java
public
Rectangle2D
getAnchorRect()
```

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

**Returns:** the

Rectangle2D

used to anchor and
size this

TexturePaint

.

---

#### getAnchorRect

public

Rectangle2D

getAnchorRect()

Returns a copy of the anchor rectangle which positions and
sizes the textured image.

createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
xform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a tiled image pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:** createContext

in interface

Paint
**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** userBounds

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** xform

- the

AffineTransform

from user
space into device space.
**Parameters:** hints

- the set of hints that the context object can use to
choose between rendering alternatives.
**Returns:** the

PaintContext

for
generating color patterns.
**See Also:** Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

---

#### createContext

public

PaintContext

createContext​(

ColorModel

cm,

Rectangle

deviceBounds,

Rectangle2D

userBounds,

AffineTransform

xform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a tiled image pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

getTransparency

```java
public int getTransparency()
```

Returns the transparency mode for this

TexturePaint

.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** the transparency mode for this

TexturePaint

as an integer value.
**See Also:** Transparency

---

#### getTransparency

public int getTransparency()

Returns the transparency mode for this

TexturePaint

.

---

