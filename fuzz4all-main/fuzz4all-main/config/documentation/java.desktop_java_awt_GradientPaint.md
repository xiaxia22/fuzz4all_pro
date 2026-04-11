# Class GradientPaint

**Source:** `java.desktop\java\awt\GradientPaint.html`

### Class Description

```java
public class
GradientPaint

extends
Object

implements
Paint
```

The

GradientPaint

class provides a way to fill
a

Shape

with a linear color gradient pattern.
If

Point

P1 with

Color

C1 and

Point

P2 with

Color

C2 are specified in user space, the

Color

on the P1, P2 connecting line is proportionally
changed from C1 to C2. Any point P not on the extended P1, P2
connecting line has the color of the point P' that is the perpendicular
projection of P on the extended P1, P2 connecting line.
Points on the extended line outside of the P1, P2 segment can be colored
in one of two ways.

- If the gradient is cyclic then the points on the extended P1, P2
connecting line cycle back and forth between the colors C1 and C2.

If the gradient is acyclic then points on the P1 side of the segment
have the constant

Color

C1 while points on the P2 side
have the constant

Color

C2.

**All Implemented Interfaces:** Paint

,

Transparency

---

### Field Details

*No entries found.*

### Constructor Details

#### public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2)

Constructs a simple acyclic

GradientPaint

object.

**Parameters:**
- x1

- x coordinate of the first specified

Point

in user space
- y1

- y coordinate of the first specified

Point

in user space
- color1

-

Color

at the first specified

Point
- x2

- x coordinate of the second specified

Point

in user space
- y2

- y coordinate of the second specified

Point

in user space
- color2

-

Color

at the second specified

Point

**Throws:**
- NullPointerException

- if either one of colors is null

---

#### public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2)

Constructs a simple acyclic

GradientPaint

object.

**Parameters:**
- pt1

- the first specified

Point

in user space
- color1

-

Color

at the first specified

Point
- pt2

- the second specified

Point

in user space
- color2

-

Color

at the second specified

Point

**Throws:**
- NullPointerException

- if either one of colors or points
is null

---

#### public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:**
- x1

- x coordinate of the first specified

Point

in user space
- y1

- y coordinate of the first specified

Point

in user space
- color1

-

Color

at the first specified

Point
- x2

- x coordinate of the second specified

Point

in user space
- y2

- y coordinate of the second specified

Point

in user space
- color2

-

Color

at the second specified

Point
- cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise

---

#### @ConstructorProperties
({"point1","color1","point2","color2","cyclic"})
public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:**
- pt1

- the first specified

Point

in user space
- color1

-

Color

at the first specified

Point
- pt2

- the second specified

Point

in user space
- color2

-

Color

at the second specified

Point
- cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise

**Throws:**
- NullPointerException

- if either one of colors or points
is null

---

### Method Details

#### public
Point2D
getPoint1()

Returns a copy of the point P1 that anchors the first color.

**Returns:**
- a

Point2D

object that is a copy of the point
that anchors the first color of this

GradientPaint

.

---

#### public
Color
getColor1()

Returns the color C1 anchored by the point P1.

**Returns:**
- a

Color

object that is the color
anchored by P1.

---

#### public
Point2D
getPoint2()

Returns a copy of the point P2 which anchors the second color.

**Returns:**
- a

Point2D

object that is a copy of the point
that anchors the second color of this

GradientPaint

.

---

#### public
Color
getColor2()

Returns the color C2 anchored by the point P2.

**Returns:**
- a

Color

object that is the color
anchored by P2.

---

#### public boolean isCyclic()

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

**Returns:**
- true

if the gradient cycles repeatedly
between the two colors;

false

otherwise.

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
generate a linear color gradient pattern.
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

GradientPaint

.

**Specified by:**
- getTransparency

in interface

Transparency

**Returns:**
- an integer value representing this

GradientPaint

object's transparency mode.

**See Also:**
- Transparency

---

### Additional Sections

#### Class GradientPaint

java.lang.Object

- java.awt.GradientPaint

java.awt.GradientPaint

**All Implemented Interfaces:** Paint

,

Transparency

```java
public class
GradientPaint

extends
Object

implements
Paint
```

The

GradientPaint

class provides a way to fill
a

Shape

with a linear color gradient pattern.
If

Point

P1 with

Color

C1 and

Point

P2 with

Color

C2 are specified in user space, the

Color

on the P1, P2 connecting line is proportionally
changed from C1 to C2. Any point P not on the extended P1, P2
connecting line has the color of the point P' that is the perpendicular
projection of P on the extended P1, P2 connecting line.
Points on the extended line outside of the P1, P2 segment can be colored
in one of two ways.

- If the gradient is cyclic then the points on the extended P1, P2
connecting line cycle back and forth between the colors C1 and C2.

If the gradient is acyclic then points on the P1 side of the segment
have the constant

Color

C1 while points on the P2 side
have the constant

Color

C2.

**See Also:** Paint

,

Graphics2D.setPaint(java.awt.Paint)

public class

GradientPaint

extends

Object

implements

Paint

The

GradientPaint

class provides a way to fill
a

Shape

with a linear color gradient pattern.
If

Point

P1 with

Color

C1 and

Point

P2 with

Color

C2 are specified in user space, the

Color

on the P1, P2 connecting line is proportionally
changed from C1 to C2. Any point P not on the extended P1, P2
connecting line has the color of the point P' that is the perpendicular
projection of P on the extended P1, P2 connecting line.
Points on the extended line outside of the P1, P2 segment can be colored
in one of two ways.

- If the gradient is cyclic then the points on the extended P1, P2
connecting line cycle back and forth between the colors C1 and C2.

If the gradient is acyclic then points on the P1 side of the segment
have the constant

Color

C1 while points on the P2 side
have the constant

Color

C2.

If the gradient is cyclic then the points on the extended P1, P2
connecting line cycle back and forth between the colors C1 and C2.

If the gradient is acyclic then points on the P1 side of the segment
have the constant

Color

C1 while points on the P2 side
have the constant

Color

C2.

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

GradientPaint

​(float x1,
float y1,

Color

color1,
float x2,
float y2,

Color

color2)

Constructs a simple acyclic

GradientPaint

object.

GradientPaint

​(float x1,
float y1,

Color

color1,
float x2,
float y2,

Color

color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

GradientPaint

​(

Point2D

pt1,

Color

color1,

Point2D

pt2,

Color

color2)

Constructs a simple acyclic

GradientPaint

object.

GradientPaint

​(

Point2D

pt1,

Color

color1,

Point2D

pt2,

Color

color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

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
generate a linear color gradient pattern.

Color

getColor1

()

Returns the color C1 anchored by the point P1.

Color

getColor2

()

Returns the color C2 anchored by the point P2.

Point2D

getPoint1

()

Returns a copy of the point P1 that anchors the first color.

Point2D

getPoint2

()

Returns a copy of the point P2 which anchors the second color.

int

getTransparency

()

Returns the transparency mode for this

GradientPaint

.

boolean

isCyclic

()

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

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

GradientPaint

​(float x1,
float y1,

Color

color1,
float x2,
float y2,

Color

color2)

Constructs a simple acyclic

GradientPaint

object.

GradientPaint

​(float x1,
float y1,

Color

color1,
float x2,
float y2,

Color

color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

GradientPaint

​(

Point2D

pt1,

Color

color1,

Point2D

pt2,

Color

color2)

Constructs a simple acyclic

GradientPaint

object.

GradientPaint

​(

Point2D

pt1,

Color

color1,

Point2D

pt2,

Color

color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

---

#### Constructor Summary

Constructs a simple acyclic

GradientPaint

object.

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

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
generate a linear color gradient pattern.

Color

getColor1

()

Returns the color C1 anchored by the point P1.

Color

getColor2

()

Returns the color C2 anchored by the point P2.

Point2D

getPoint1

()

Returns a copy of the point P1 that anchors the first color.

Point2D

getPoint2

()

Returns a copy of the point P2 which anchors the second color.

int

getTransparency

()

Returns the transparency mode for this

GradientPaint

.

boolean

isCyclic

()

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

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
generate a linear color gradient pattern.

Returns the color C1 anchored by the point P1.

Returns the color C2 anchored by the point P2.

Returns a copy of the point P1 that anchors the first color.

Returns a copy of the point P2 which anchors the second color.

Returns the transparency mode for this

GradientPaint

.

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

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

- GradientPaint

```java
public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2)
```

Constructs a simple acyclic

GradientPaint

object.

**Parameters:** x1

- x coordinate of the first specified

Point

in user space
**Parameters:** y1

- y coordinate of the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** x2

- x coordinate of the second specified

Point

in user space
**Parameters:** y2

- y coordinate of the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Throws:** NullPointerException

- if either one of colors is null

- GradientPaint

```java
public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2)
```

Constructs a simple acyclic

GradientPaint

object.

**Parameters:** pt1

- the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** pt2

- the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Throws:** NullPointerException

- if either one of colors or points
is null

- GradientPaint

```java
public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2,
boolean cyclic)
```

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:** x1

- x coordinate of the first specified

Point

in user space
**Parameters:** y1

- y coordinate of the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** x2

- x coordinate of the second specified

Point

in user space
**Parameters:** y2

- y coordinate of the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Parameters:** cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise

- GradientPaint

```java
@ConstructorProperties
({"point1","color1","point2","color2","cyclic"})
public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2,
boolean cyclic)
```

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:** pt1

- the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** pt2

- the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Parameters:** cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise
**Throws:** NullPointerException

- if either one of colors or points
is null

============ METHOD DETAIL ==========

- Method Detail

- getPoint1

```java
public
Point2D
getPoint1()
```

Returns a copy of the point P1 that anchors the first color.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the first color of this

GradientPaint

.

- getColor1

```java
public
Color
getColor1()
```

Returns the color C1 anchored by the point P1.

**Returns:** a

Color

object that is the color
anchored by P1.

- getPoint2

```java
public
Point2D
getPoint2()
```

Returns a copy of the point P2 which anchors the second color.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the second color of this

GradientPaint

.

- getColor2

```java
public
Color
getColor2()
```

Returns the color C2 anchored by the point P2.

**Returns:** a

Color

object that is the color
anchored by P2.

- isCyclic

```java
public boolean isCyclic()
```

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

**Returns:** true

if the gradient cycles repeatedly
between the two colors;

false

otherwise.

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
generate a linear color gradient pattern.
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

GradientPaint

.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** an integer value representing this

GradientPaint

object's transparency mode.
**See Also:** Transparency

Constructor Detail

- GradientPaint

```java
public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2)
```

Constructs a simple acyclic

GradientPaint

object.

**Parameters:** x1

- x coordinate of the first specified

Point

in user space
**Parameters:** y1

- y coordinate of the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** x2

- x coordinate of the second specified

Point

in user space
**Parameters:** y2

- y coordinate of the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Throws:** NullPointerException

- if either one of colors is null

- GradientPaint

```java
public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2)
```

Constructs a simple acyclic

GradientPaint

object.

**Parameters:** pt1

- the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** pt2

- the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Throws:** NullPointerException

- if either one of colors or points
is null

- GradientPaint

```java
public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2,
boolean cyclic)
```

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:** x1

- x coordinate of the first specified

Point

in user space
**Parameters:** y1

- y coordinate of the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** x2

- x coordinate of the second specified

Point

in user space
**Parameters:** y2

- y coordinate of the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Parameters:** cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise

- GradientPaint

```java
@ConstructorProperties
({"point1","color1","point2","color2","cyclic"})
public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2,
boolean cyclic)
```

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:** pt1

- the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** pt2

- the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Parameters:** cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise
**Throws:** NullPointerException

- if either one of colors or points
is null

---

#### Constructor Detail

GradientPaint

```java
public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2)
```

Constructs a simple acyclic

GradientPaint

object.

**Parameters:** x1

- x coordinate of the first specified

Point

in user space
**Parameters:** y1

- y coordinate of the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** x2

- x coordinate of the second specified

Point

in user space
**Parameters:** y2

- y coordinate of the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Throws:** NullPointerException

- if either one of colors is null

---

#### GradientPaint

public GradientPaint​(float x1,
float y1,

Color

color1,
float x2,
float y2,

Color

color2)

Constructs a simple acyclic

GradientPaint

object.

GradientPaint

```java
public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2)
```

Constructs a simple acyclic

GradientPaint

object.

**Parameters:** pt1

- the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** pt2

- the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Throws:** NullPointerException

- if either one of colors or points
is null

---

#### GradientPaint

public GradientPaint​(

Point2D

pt1,

Color

color1,

Point2D

pt2,

Color

color2)

Constructs a simple acyclic

GradientPaint

object.

GradientPaint

```java
public GradientPaint​(float x1,
float y1,

Color
color1,
float x2,
float y2,

Color
color2,
boolean cyclic)
```

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:** x1

- x coordinate of the first specified

Point

in user space
**Parameters:** y1

- y coordinate of the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** x2

- x coordinate of the second specified

Point

in user space
**Parameters:** y2

- y coordinate of the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Parameters:** cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise

---

#### GradientPaint

public GradientPaint​(float x1,
float y1,

Color

color1,
float x2,
float y2,

Color

color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

GradientPaint

```java
@ConstructorProperties
({"point1","color1","point2","color2","cyclic"})
public GradientPaint​(
Point2D
pt1,

Color
color1,

Point2D
pt2,

Color
color2,
boolean cyclic)
```

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

**Parameters:** pt1

- the first specified

Point

in user space
**Parameters:** color1

-

Color

at the first specified

Point
**Parameters:** pt2

- the second specified

Point

in user space
**Parameters:** color2

-

Color

at the second specified

Point
**Parameters:** cyclic

-

true

if the gradient pattern should cycle
repeatedly between the two colors;

false

otherwise
**Throws:** NullPointerException

- if either one of colors or points
is null

---

#### GradientPaint

@ConstructorProperties

({"point1","color1","point2","color2","cyclic"})
public GradientPaint​(

Point2D

pt1,

Color

color1,

Point2D

pt2,

Color

color2,
boolean cyclic)

Constructs either a cyclic or acyclic

GradientPaint

object depending on the

boolean

parameter.

Method Detail

- getPoint1

```java
public
Point2D
getPoint1()
```

Returns a copy of the point P1 that anchors the first color.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the first color of this

GradientPaint

.

- getColor1

```java
public
Color
getColor1()
```

Returns the color C1 anchored by the point P1.

**Returns:** a

Color

object that is the color
anchored by P1.

- getPoint2

```java
public
Point2D
getPoint2()
```

Returns a copy of the point P2 which anchors the second color.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the second color of this

GradientPaint

.

- getColor2

```java
public
Color
getColor2()
```

Returns the color C2 anchored by the point P2.

**Returns:** a

Color

object that is the color
anchored by P2.

- isCyclic

```java
public boolean isCyclic()
```

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

**Returns:** true

if the gradient cycles repeatedly
between the two colors;

false

otherwise.

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
generate a linear color gradient pattern.
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

GradientPaint

.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** an integer value representing this

GradientPaint

object's transparency mode.
**See Also:** Transparency

---

#### Method Detail

getPoint1

```java
public
Point2D
getPoint1()
```

Returns a copy of the point P1 that anchors the first color.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the first color of this

GradientPaint

.

---

#### getPoint1

public

Point2D

getPoint1()

Returns a copy of the point P1 that anchors the first color.

getColor1

```java
public
Color
getColor1()
```

Returns the color C1 anchored by the point P1.

**Returns:** a

Color

object that is the color
anchored by P1.

---

#### getColor1

public

Color

getColor1()

Returns the color C1 anchored by the point P1.

getPoint2

```java
public
Point2D
getPoint2()
```

Returns a copy of the point P2 which anchors the second color.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the second color of this

GradientPaint

.

---

#### getPoint2

public

Point2D

getPoint2()

Returns a copy of the point P2 which anchors the second color.

getColor2

```java
public
Color
getColor2()
```

Returns the color C2 anchored by the point P2.

**Returns:** a

Color

object that is the color
anchored by P2.

---

#### getColor2

public

Color

getColor2()

Returns the color C2 anchored by the point P2.

isCyclic

```java
public boolean isCyclic()
```

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

**Returns:** true

if the gradient cycles repeatedly
between the two colors;

false

otherwise.

---

#### isCyclic

public boolean isCyclic()

Returns

true

if the gradient cycles repeatedly
between the two colors C1 and C2.

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
generate a linear color gradient pattern.
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
generate a linear color gradient pattern.
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

GradientPaint

.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** an integer value representing this

GradientPaint

object's transparency mode.
**See Also:** Transparency

---

#### getTransparency

public int getTransparency()

Returns the transparency mode for this

GradientPaint

.

---

