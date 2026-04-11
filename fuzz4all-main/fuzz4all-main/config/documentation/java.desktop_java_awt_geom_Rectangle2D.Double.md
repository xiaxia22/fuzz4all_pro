# Class Rectangle2D.Double

**Source:** `java.desktop\java\awt\geom\Rectangle2D.Double.html`

### Class Description

```java
public static class
Rectangle2D.Double

extends
Rectangle2D

implements
Serializable
```

The

Double

class defines a rectangle specified in
double coordinates.

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

---

### Field Details

#### public double x

The X coordinate of this

Rectangle2D

.

**Since:**
- 1.2

---

#### public double y

The Y coordinate of this

Rectangle2D

.

**Since:**
- 1.2

---

#### public double width

The width of this

Rectangle2D

.

**Since:**
- 1.2

---

#### public double height

The height of this

Rectangle2D

.

**Since:**
- 1.2

---

### Constructor Details

#### public Double()

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

**Since:**
- 1.2

---

#### public Double​(double x,
double y,
double w,
double h)

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

**Parameters:**
- x

- the X coordinate of the upper-left corner
of the newly constructed

Rectangle2D
- y

- the Y coordinate of the upper-left corner
of the newly constructed

Rectangle2D
- w

- the width of the newly constructed

Rectangle2D
- h

- the height of the newly constructed

Rectangle2D

**Since:**
- 1.2

---

### Method Details

#### public double getX()

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:**
- getX

in class

RectangularShape

**Returns:**
- the X coordinate of the upper-left corner of
the framing rectangle.

**Since:**
- 1.2

---

#### public double getY()

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:**
- getY

in class

RectangularShape

**Returns:**
- the Y coordinate of the upper-left corner of
the framing rectangle.

**Since:**
- 1.2

---

#### public double getWidth()

Returns the width of the framing rectangle in

double

precision.

**Specified by:**
- getWidth

in class

RectangularShape

**Returns:**
- the width of the framing rectangle.

**Since:**
- 1.2

---

#### public double getHeight()

Returns the height of the framing rectangle
in

double

precision.

**Specified by:**
- getHeight

in class

RectangularShape

**Returns:**
- the height of the framing rectangle.

**Since:**
- 1.2

---

#### public boolean isEmpty()

Determines whether the

RectangularShape

is empty.
When the

RectangularShape

is empty, it encloses no
area.

**Specified by:**
- isEmpty

in class

RectangularShape

**Returns:**
- true

if the

RectangularShape

is empty;

false

otherwise.

**Since:**
- 1.2

---

#### public void setRect​(double x,
double y,
double w,
double h)

Sets the location and size of this

Rectangle2D

to the specified

double

values.

**Specified by:**
- setRect

in class

Rectangle2D

**Parameters:**
- x

- the X coordinate of the upper-left corner
of this

Rectangle2D
- y

- the Y coordinate of the upper-left corner
of this

Rectangle2D
- w

- the width of this

Rectangle2D
- h

- the height of this

Rectangle2D

**Since:**
- 1.2

---

#### public void setRect​(
Rectangle2D
r)

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

**Overrides:**
- setRect

in class

Rectangle2D

**Parameters:**
- r

- the specified

Rectangle2D

**Since:**
- 1.2

---

#### public int outcode​(double x,
double y)

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.
This method computes a binary OR of the appropriate mask values
indicating, for each side of this

Rectangle2D

,
whether or not the specified coordinates are on the same side
of the edge as the rest of this

Rectangle2D

.

**Specified by:**
- outcode

in class

Rectangle2D

**Parameters:**
- x

- the specified X coordinate
- y

- the specified Y coordinate

**Returns:**
- the logical OR of all appropriate out codes.

**See Also:**
- Rectangle2D.OUT_LEFT

,

Rectangle2D.OUT_TOP

,

Rectangle2D.OUT_RIGHT

,

Rectangle2D.OUT_BOTTOM

**Since:**
- 1.2

---

#### public
Rectangle2D
getBounds2D()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.
Note that there is no guarantee that the returned

Rectangle2D

is the smallest bounding box that encloses
the

Shape

, only that the

Shape

lies
entirely within the indicated

Rectangle2D

. The
bounding box returned by this method is usually tighter than that
returned by the

getBounds

method and never fails due
to overflow problems since the return value can be an instance of
the

Rectangle2D

that uses double precision values to
store the dimensions.

Note that the

definition of insideness

can lead to situations where points
on the defining outline of the

shape

may not be considered
contained in the returned

bounds

object, but only in cases
where those points are also not considered contained in the original

shape

.

If a

point

is inside the

shape

according to the

contains(point)

method, then it must
be inside the returned

Rectangle2D

bounds object according
to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(p)

requires

bounds.contains(p)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(p)

does not imply

shape.contains(p)

**Specified by:**
- getBounds2D

in interface

Shape

**Overrides:**
- getBounds2D

in class

Rectangle2D

**Returns:**
- an instance of

Rectangle2D

that is a
high-precision bounding box of the

Shape

.

**See Also:**
- Shape.getBounds()

**Since:**
- 1.2

---

#### public
Rectangle2D
createIntersection​(
Rectangle2D
r)

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:**
- createIntersection

in class

Rectangle2D

**Parameters:**
- r

- the

Rectangle2D

to be intersected with
this

Rectangle2D

**Returns:**
- the largest

Rectangle2D

contained in both
the specified

Rectangle2D

and in this

Rectangle2D

.

**Since:**
- 1.2

---

#### public
Rectangle2D
createUnion​(
Rectangle2D
r)

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:**
- createUnion

in class

Rectangle2D

**Parameters:**
- r

- the

Rectangle2D

to be combined with
this

Rectangle2D

**Returns:**
- the smallest

Rectangle2D

containing both
the specified

Rectangle2D

and this

Rectangle2D

.

**Since:**
- 1.2

---

#### public
String
toString()

Returns the

String

representation of this

Rectangle2D

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

representing this

Rectangle2D

.

**Since:**
- 1.2

---

### Additional Sections

#### Class Rectangle2D.Double

java.lang.Object

- java.awt.geom.RectangularShape
- - java.awt.geom.Rectangle2D
- - java.awt.geom.Rectangle2D.Double

java.awt.geom.RectangularShape

- java.awt.geom.Rectangle2D
- - java.awt.geom.Rectangle2D.Double

java.awt.geom.Rectangle2D

- java.awt.geom.Rectangle2D.Double

java.awt.geom.Rectangle2D.Double

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

**Enclosing class:** Rectangle2D

```java
public static class
Rectangle2D.Double

extends
Rectangle2D

implements
Serializable
```

The

Double

class defines a rectangle specified in
double coordinates.

**Since:** 1.2
**See Also:** Serialized Form

public static class

Rectangle2D.Double

extends

Rectangle2D

implements

Serializable

The

Double

class defines a rectangle specified in
double coordinates.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Rectangle2D

Rectangle2D.Double

,

Rectangle2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

double

height

The height of this

Rectangle2D

.

double

width

The width of this

Rectangle2D

.

double

x

The X coordinate of this

Rectangle2D

.

double

y

The Y coordinate of this

Rectangle2D

.

- Fields declared in class java.awt.geom.

Rectangle2D

OUT_BOTTOM

,

OUT_LEFT

,

OUT_RIGHT

,

OUT_TOP

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Double

()

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

Double

​(double x,
double y,
double w,
double h)

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle2D

createIntersection

​(

Rectangle2D

r)

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

Rectangle2D

createUnion

​(

Rectangle2D

r)

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

Rectangle2D

getBounds2D

()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

double

getHeight

()

Returns the height of the framing rectangle
in

double

precision.

double

getWidth

()

Returns the width of the framing rectangle in

double

precision.

double

getX

()

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

double

getY

()

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

boolean

isEmpty

()

Determines whether the

RectangularShape

is empty.

int

outcode

​(double x,
double y)

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.

void

setRect

​(double x,
double y,
double w,
double h)

Sets the location and size of this

Rectangle2D

to the specified

double

values.

void

setRect

​(

Rectangle2D

r)

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

String

toString

()

Returns the

String

representation of this

Rectangle2D

.

- Methods declared in class java.awt.geom.

Rectangle2D

add

,

add

,

add

,

contains

,

contains

,

equals

,

getPathIterator

,

getPathIterator

,

hashCode

,

intersect

,

intersects

,

intersectsLine

,

intersectsLine

,

outcode

,

setFrame

,

union

- Methods declared in class java.awt.geom.

RectangularShape

clone

,

contains

,

contains

,

getBounds

,

getCenterX

,

getCenterY

,

getFrame

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

intersects

,

setFrame

,

setFrame

,

setFrameFromCenter

,

setFrameFromCenter

,

setFrameFromDiagonal

,

setFrameFromDiagonal

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Rectangle2D

Rectangle2D.Double

,

Rectangle2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

Rectangle2D

Rectangle2D.Double

,

Rectangle2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. Rectangle2D

Field Summary

Fields

Modifier and Type

Field

Description

double

height

The height of this

Rectangle2D

.

double

width

The width of this

Rectangle2D

.

double

x

The X coordinate of this

Rectangle2D

.

double

y

The Y coordinate of this

Rectangle2D

.

- Fields declared in class java.awt.geom.

Rectangle2D

OUT_BOTTOM

,

OUT_LEFT

,

OUT_RIGHT

,

OUT_TOP

---

#### Field Summary

The height of this

Rectangle2D

.

The width of this

Rectangle2D

.

The X coordinate of this

Rectangle2D

.

The Y coordinate of this

Rectangle2D

.

Fields declared in class java.awt.geom.

Rectangle2D

OUT_BOTTOM

,

OUT_LEFT

,

OUT_RIGHT

,

OUT_TOP

---

#### Fields declared in class java.awt.geom. Rectangle2D

Constructor Summary

Constructors

Constructor

Description

Double

()

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

Double

​(double x,
double y,
double w,
double h)

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

---

#### Constructor Summary

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle2D

createIntersection

​(

Rectangle2D

r)

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

Rectangle2D

createUnion

​(

Rectangle2D

r)

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

Rectangle2D

getBounds2D

()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

double

getHeight

()

Returns the height of the framing rectangle
in

double

precision.

double

getWidth

()

Returns the width of the framing rectangle in

double

precision.

double

getX

()

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

double

getY

()

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

boolean

isEmpty

()

Determines whether the

RectangularShape

is empty.

int

outcode

​(double x,
double y)

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.

void

setRect

​(double x,
double y,
double w,
double h)

Sets the location and size of this

Rectangle2D

to the specified

double

values.

void

setRect

​(

Rectangle2D

r)

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

String

toString

()

Returns the

String

representation of this

Rectangle2D

.

- Methods declared in class java.awt.geom.

Rectangle2D

add

,

add

,

add

,

contains

,

contains

,

equals

,

getPathIterator

,

getPathIterator

,

hashCode

,

intersect

,

intersects

,

intersectsLine

,

intersectsLine

,

outcode

,

setFrame

,

union

- Methods declared in class java.awt.geom.

RectangularShape

clone

,

contains

,

contains

,

getBounds

,

getCenterX

,

getCenterY

,

getFrame

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

intersects

,

setFrame

,

setFrame

,

setFrameFromCenter

,

setFrameFromCenter

,

setFrameFromDiagonal

,

setFrameFromDiagonal

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

Returns the height of the framing rectangle
in

double

precision.

Returns the width of the framing rectangle in

double

precision.

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

Determines whether the

RectangularShape

is empty.

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.

Sets the location and size of this

Rectangle2D

to the specified

double

values.

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

Returns the

String

representation of this

Rectangle2D

.

Methods declared in class java.awt.geom.

Rectangle2D

add

,

add

,

add

,

contains

,

contains

,

equals

,

getPathIterator

,

getPathIterator

,

hashCode

,

intersect

,

intersects

,

intersectsLine

,

intersectsLine

,

outcode

,

setFrame

,

union

---

#### Methods declared in class java.awt.geom. Rectangle2D

Methods declared in class java.awt.geom.

RectangularShape

clone

,

contains

,

contains

,

getBounds

,

getCenterX

,

getCenterY

,

getFrame

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

intersects

,

setFrame

,

setFrame

,

setFrameFromCenter

,

setFrameFromCenter

,

setFrameFromDiagonal

,

setFrameFromDiagonal

---

#### Methods declared in class java.awt.geom. RectangularShape

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

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

- x

```java
public double x
```

The X coordinate of this

Rectangle2D

.

**Since:** 1.2

- y

```java
public double y
```

The Y coordinate of this

Rectangle2D

.

**Since:** 1.2

- width

```java
public double width
```

The width of this

Rectangle2D

.

**Since:** 1.2

- height

```java
public double height
```

The height of this

Rectangle2D

.

**Since:** 1.2

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Double

```java
public Double()
```

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

**Since:** 1.2

- Double

```java
public Double​(double x,
double y,
double w,
double h)
```

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

**Parameters:** x

- the X coordinate of the upper-left corner
of the newly constructed

Rectangle2D
**Parameters:** y

- the Y coordinate of the upper-left corner
of the newly constructed

Rectangle2D
**Parameters:** w

- the width of the newly constructed

Rectangle2D
**Parameters:** h

- the height of the newly constructed

Rectangle2D
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getX

```java
public double getX()
```

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:** getX

in class

RectangularShape
**Returns:** the X coordinate of the upper-left corner of
the framing rectangle.
**Since:** 1.2

- getY

```java
public double getY()
```

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:** getY

in class

RectangularShape
**Returns:** the Y coordinate of the upper-left corner of
the framing rectangle.
**Since:** 1.2

- getWidth

```java
public double getWidth()
```

Returns the width of the framing rectangle in

double

precision.

**Specified by:** getWidth

in class

RectangularShape
**Returns:** the width of the framing rectangle.
**Since:** 1.2

- getHeight

```java
public double getHeight()
```

Returns the height of the framing rectangle
in

double

precision.

**Specified by:** getHeight

in class

RectangularShape
**Returns:** the height of the framing rectangle.
**Since:** 1.2

- isEmpty

```java
public boolean isEmpty()
```

Determines whether the

RectangularShape

is empty.
When the

RectangularShape

is empty, it encloses no
area.

**Specified by:** isEmpty

in class

RectangularShape
**Returns:** true

if the

RectangularShape

is empty;

false

otherwise.
**Since:** 1.2

- setRect

```java
public void setRect​(double x,
double y,
double w,
double h)
```

Sets the location and size of this

Rectangle2D

to the specified

double

values.

**Specified by:** setRect

in class

Rectangle2D
**Parameters:** x

- the X coordinate of the upper-left corner
of this

Rectangle2D
**Parameters:** y

- the Y coordinate of the upper-left corner
of this

Rectangle2D
**Parameters:** w

- the width of this

Rectangle2D
**Parameters:** h

- the height of this

Rectangle2D
**Since:** 1.2

- setRect

```java
public void setRect​(
Rectangle2D
r)
```

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

**Overrides:** setRect

in class

Rectangle2D
**Parameters:** r

- the specified

Rectangle2D
**Since:** 1.2

- outcode

```java
public int outcode​(double x,
double y)
```

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.
This method computes a binary OR of the appropriate mask values
indicating, for each side of this

Rectangle2D

,
whether or not the specified coordinates are on the same side
of the edge as the rest of this

Rectangle2D

.

**Specified by:** outcode

in class

Rectangle2D
**Parameters:** x

- the specified X coordinate
**Parameters:** y

- the specified Y coordinate
**Returns:** the logical OR of all appropriate out codes.
**Since:** 1.2
**See Also:** Rectangle2D.OUT_LEFT

,

Rectangle2D.OUT_TOP

,

Rectangle2D.OUT_RIGHT

,

Rectangle2D.OUT_BOTTOM

- getBounds2D

```java
public
Rectangle2D
getBounds2D()
```

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.
Note that there is no guarantee that the returned

Rectangle2D

is the smallest bounding box that encloses
the

Shape

, only that the

Shape

lies
entirely within the indicated

Rectangle2D

. The
bounding box returned by this method is usually tighter than that
returned by the

getBounds

method and never fails due
to overflow problems since the return value can be an instance of
the

Rectangle2D

that uses double precision values to
store the dimensions.

Note that the

definition of insideness

can lead to situations where points
on the defining outline of the

shape

may not be considered
contained in the returned

bounds

object, but only in cases
where those points are also not considered contained in the original

shape

.

If a

point

is inside the

shape

according to the

contains(point)

method, then it must
be inside the returned

Rectangle2D

bounds object according
to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(p)

requires

bounds.contains(p)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(p)

does not imply

shape.contains(p)

**Specified by:** getBounds2D

in interface

Shape
**Overrides:** getBounds2D

in class

Rectangle2D
**Returns:** an instance of

Rectangle2D

that is a
high-precision bounding box of the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds()

- createIntersection

```java
public
Rectangle2D
createIntersection​(
Rectangle2D
r)
```

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:** createIntersection

in class

Rectangle2D
**Parameters:** r

- the

Rectangle2D

to be intersected with
this

Rectangle2D
**Returns:** the largest

Rectangle2D

contained in both
the specified

Rectangle2D

and in this

Rectangle2D

.
**Since:** 1.2

- createUnion

```java
public
Rectangle2D
createUnion​(
Rectangle2D
r)
```

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:** createUnion

in class

Rectangle2D
**Parameters:** r

- the

Rectangle2D

to be combined with
this

Rectangle2D
**Returns:** the smallest

Rectangle2D

containing both
the specified

Rectangle2D

and this

Rectangle2D

.
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns the

String

representation of this

Rectangle2D

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing this

Rectangle2D

.
**Since:** 1.2

Field Detail

- x

```java
public double x
```

The X coordinate of this

Rectangle2D

.

**Since:** 1.2

- y

```java
public double y
```

The Y coordinate of this

Rectangle2D

.

**Since:** 1.2

- width

```java
public double width
```

The width of this

Rectangle2D

.

**Since:** 1.2

- height

```java
public double height
```

The height of this

Rectangle2D

.

**Since:** 1.2

---

#### Field Detail

x

```java
public double x
```

The X coordinate of this

Rectangle2D

.

**Since:** 1.2

---

#### x

public double x

The X coordinate of this

Rectangle2D

.

y

```java
public double y
```

The Y coordinate of this

Rectangle2D

.

**Since:** 1.2

---

#### y

public double y

The Y coordinate of this

Rectangle2D

.

width

```java
public double width
```

The width of this

Rectangle2D

.

**Since:** 1.2

---

#### width

public double width

The width of this

Rectangle2D

.

height

```java
public double height
```

The height of this

Rectangle2D

.

**Since:** 1.2

---

#### height

public double height

The height of this

Rectangle2D

.

Constructor Detail

- Double

```java
public Double()
```

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

**Since:** 1.2

- Double

```java
public Double​(double x,
double y,
double w,
double h)
```

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

**Parameters:** x

- the X coordinate of the upper-left corner
of the newly constructed

Rectangle2D
**Parameters:** y

- the Y coordinate of the upper-left corner
of the newly constructed

Rectangle2D
**Parameters:** w

- the width of the newly constructed

Rectangle2D
**Parameters:** h

- the height of the newly constructed

Rectangle2D
**Since:** 1.2

---

#### Constructor Detail

Double

```java
public Double()
```

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

**Since:** 1.2

---

#### Double

public Double()

Constructs a new

Rectangle2D

, initialized to
location (0, 0) and size (0, 0).

Double

```java
public Double​(double x,
double y,
double w,
double h)
```

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

**Parameters:** x

- the X coordinate of the upper-left corner
of the newly constructed

Rectangle2D
**Parameters:** y

- the Y coordinate of the upper-left corner
of the newly constructed

Rectangle2D
**Parameters:** w

- the width of the newly constructed

Rectangle2D
**Parameters:** h

- the height of the newly constructed

Rectangle2D
**Since:** 1.2

---

#### Double

public Double​(double x,
double y,
double w,
double h)

Constructs and initializes a

Rectangle2D

from the specified

double

coordinates.

Method Detail

- getX

```java
public double getX()
```

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:** getX

in class

RectangularShape
**Returns:** the X coordinate of the upper-left corner of
the framing rectangle.
**Since:** 1.2

- getY

```java
public double getY()
```

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:** getY

in class

RectangularShape
**Returns:** the Y coordinate of the upper-left corner of
the framing rectangle.
**Since:** 1.2

- getWidth

```java
public double getWidth()
```

Returns the width of the framing rectangle in

double

precision.

**Specified by:** getWidth

in class

RectangularShape
**Returns:** the width of the framing rectangle.
**Since:** 1.2

- getHeight

```java
public double getHeight()
```

Returns the height of the framing rectangle
in

double

precision.

**Specified by:** getHeight

in class

RectangularShape
**Returns:** the height of the framing rectangle.
**Since:** 1.2

- isEmpty

```java
public boolean isEmpty()
```

Determines whether the

RectangularShape

is empty.
When the

RectangularShape

is empty, it encloses no
area.

**Specified by:** isEmpty

in class

RectangularShape
**Returns:** true

if the

RectangularShape

is empty;

false

otherwise.
**Since:** 1.2

- setRect

```java
public void setRect​(double x,
double y,
double w,
double h)
```

Sets the location and size of this

Rectangle2D

to the specified

double

values.

**Specified by:** setRect

in class

Rectangle2D
**Parameters:** x

- the X coordinate of the upper-left corner
of this

Rectangle2D
**Parameters:** y

- the Y coordinate of the upper-left corner
of this

Rectangle2D
**Parameters:** w

- the width of this

Rectangle2D
**Parameters:** h

- the height of this

Rectangle2D
**Since:** 1.2

- setRect

```java
public void setRect​(
Rectangle2D
r)
```

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

**Overrides:** setRect

in class

Rectangle2D
**Parameters:** r

- the specified

Rectangle2D
**Since:** 1.2

- outcode

```java
public int outcode​(double x,
double y)
```

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.
This method computes a binary OR of the appropriate mask values
indicating, for each side of this

Rectangle2D

,
whether or not the specified coordinates are on the same side
of the edge as the rest of this

Rectangle2D

.

**Specified by:** outcode

in class

Rectangle2D
**Parameters:** x

- the specified X coordinate
**Parameters:** y

- the specified Y coordinate
**Returns:** the logical OR of all appropriate out codes.
**Since:** 1.2
**See Also:** Rectangle2D.OUT_LEFT

,

Rectangle2D.OUT_TOP

,

Rectangle2D.OUT_RIGHT

,

Rectangle2D.OUT_BOTTOM

- getBounds2D

```java
public
Rectangle2D
getBounds2D()
```

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.
Note that there is no guarantee that the returned

Rectangle2D

is the smallest bounding box that encloses
the

Shape

, only that the

Shape

lies
entirely within the indicated

Rectangle2D

. The
bounding box returned by this method is usually tighter than that
returned by the

getBounds

method and never fails due
to overflow problems since the return value can be an instance of
the

Rectangle2D

that uses double precision values to
store the dimensions.

Note that the

definition of insideness

can lead to situations where points
on the defining outline of the

shape

may not be considered
contained in the returned

bounds

object, but only in cases
where those points are also not considered contained in the original

shape

.

If a

point

is inside the

shape

according to the

contains(point)

method, then it must
be inside the returned

Rectangle2D

bounds object according
to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(p)

requires

bounds.contains(p)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(p)

does not imply

shape.contains(p)

**Specified by:** getBounds2D

in interface

Shape
**Overrides:** getBounds2D

in class

Rectangle2D
**Returns:** an instance of

Rectangle2D

that is a
high-precision bounding box of the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds()

- createIntersection

```java
public
Rectangle2D
createIntersection​(
Rectangle2D
r)
```

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:** createIntersection

in class

Rectangle2D
**Parameters:** r

- the

Rectangle2D

to be intersected with
this

Rectangle2D
**Returns:** the largest

Rectangle2D

contained in both
the specified

Rectangle2D

and in this

Rectangle2D

.
**Since:** 1.2

- createUnion

```java
public
Rectangle2D
createUnion​(
Rectangle2D
r)
```

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:** createUnion

in class

Rectangle2D
**Parameters:** r

- the

Rectangle2D

to be combined with
this

Rectangle2D
**Returns:** the smallest

Rectangle2D

containing both
the specified

Rectangle2D

and this

Rectangle2D

.
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns the

String

representation of this

Rectangle2D

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing this

Rectangle2D

.
**Since:** 1.2

---

#### Method Detail

getX

```java
public double getX()
```

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:** getX

in class

RectangularShape
**Returns:** the X coordinate of the upper-left corner of
the framing rectangle.
**Since:** 1.2

---

#### getX

public double getX()

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.

getY

```java
public double getY()
```

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

**Specified by:** getY

in class

RectangularShape
**Returns:** the Y coordinate of the upper-left corner of
the framing rectangle.
**Since:** 1.2

---

#### getY

public double getY()

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.

getWidth

```java
public double getWidth()
```

Returns the width of the framing rectangle in

double

precision.

**Specified by:** getWidth

in class

RectangularShape
**Returns:** the width of the framing rectangle.
**Since:** 1.2

---

#### getWidth

public double getWidth()

Returns the width of the framing rectangle in

double

precision.

getHeight

```java
public double getHeight()
```

Returns the height of the framing rectangle
in

double

precision.

**Specified by:** getHeight

in class

RectangularShape
**Returns:** the height of the framing rectangle.
**Since:** 1.2

---

#### getHeight

public double getHeight()

Returns the height of the framing rectangle
in

double

precision.

isEmpty

```java
public boolean isEmpty()
```

Determines whether the

RectangularShape

is empty.
When the

RectangularShape

is empty, it encloses no
area.

**Specified by:** isEmpty

in class

RectangularShape
**Returns:** true

if the

RectangularShape

is empty;

false

otherwise.
**Since:** 1.2

---

#### isEmpty

public boolean isEmpty()

Determines whether the

RectangularShape

is empty.
When the

RectangularShape

is empty, it encloses no
area.

setRect

```java
public void setRect​(double x,
double y,
double w,
double h)
```

Sets the location and size of this

Rectangle2D

to the specified

double

values.

**Specified by:** setRect

in class

Rectangle2D
**Parameters:** x

- the X coordinate of the upper-left corner
of this

Rectangle2D
**Parameters:** y

- the Y coordinate of the upper-left corner
of this

Rectangle2D
**Parameters:** w

- the width of this

Rectangle2D
**Parameters:** h

- the height of this

Rectangle2D
**Since:** 1.2

---

#### setRect

public void setRect​(double x,
double y,
double w,
double h)

Sets the location and size of this

Rectangle2D

to the specified

double

values.

setRect

```java
public void setRect​(
Rectangle2D
r)
```

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

**Overrides:** setRect

in class

Rectangle2D
**Parameters:** r

- the specified

Rectangle2D
**Since:** 1.2

---

#### setRect

public void setRect​(

Rectangle2D

r)

Sets this

Rectangle2D

to be the same as the specified

Rectangle2D

.

outcode

```java
public int outcode​(double x,
double y)
```

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.
This method computes a binary OR of the appropriate mask values
indicating, for each side of this

Rectangle2D

,
whether or not the specified coordinates are on the same side
of the edge as the rest of this

Rectangle2D

.

**Specified by:** outcode

in class

Rectangle2D
**Parameters:** x

- the specified X coordinate
**Parameters:** y

- the specified Y coordinate
**Returns:** the logical OR of all appropriate out codes.
**Since:** 1.2
**See Also:** Rectangle2D.OUT_LEFT

,

Rectangle2D.OUT_TOP

,

Rectangle2D.OUT_RIGHT

,

Rectangle2D.OUT_BOTTOM

---

#### outcode

public int outcode​(double x,
double y)

Determines where the specified coordinates lie with respect
to this

Rectangle2D

.
This method computes a binary OR of the appropriate mask values
indicating, for each side of this

Rectangle2D

,
whether or not the specified coordinates are on the same side
of the edge as the rest of this

Rectangle2D

.

getBounds2D

```java
public
Rectangle2D
getBounds2D()
```

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.
Note that there is no guarantee that the returned

Rectangle2D

is the smallest bounding box that encloses
the

Shape

, only that the

Shape

lies
entirely within the indicated

Rectangle2D

. The
bounding box returned by this method is usually tighter than that
returned by the

getBounds

method and never fails due
to overflow problems since the return value can be an instance of
the

Rectangle2D

that uses double precision values to
store the dimensions.

Note that the

definition of insideness

can lead to situations where points
on the defining outline of the

shape

may not be considered
contained in the returned

bounds

object, but only in cases
where those points are also not considered contained in the original

shape

.

If a

point

is inside the

shape

according to the

contains(point)

method, then it must
be inside the returned

Rectangle2D

bounds object according
to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(p)

requires

bounds.contains(p)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(p)

does not imply

shape.contains(p)

**Specified by:** getBounds2D

in interface

Shape
**Overrides:** getBounds2D

in class

Rectangle2D
**Returns:** an instance of

Rectangle2D

that is a
high-precision bounding box of the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds()

---

#### getBounds2D

public

Rectangle2D

getBounds2D()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.
Note that there is no guarantee that the returned

Rectangle2D

is the smallest bounding box that encloses
the

Shape

, only that the

Shape

lies
entirely within the indicated

Rectangle2D

. The
bounding box returned by this method is usually tighter than that
returned by the

getBounds

method and never fails due
to overflow problems since the return value can be an instance of
the

Rectangle2D

that uses double precision values to
store the dimensions.

Note that the

definition of insideness

can lead to situations where points
on the defining outline of the

shape

may not be considered
contained in the returned

bounds

object, but only in cases
where those points are also not considered contained in the original

shape

.

If a

point

is inside the

shape

according to the

contains(point)

method, then it must
be inside the returned

Rectangle2D

bounds object according
to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(p)

requires

bounds.contains(p)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(p)

does not imply

shape.contains(p)

Note that the

definition of insideness

can lead to situations where points
on the defining outline of the

shape

may not be considered
contained in the returned

bounds

object, but only in cases
where those points are also not considered contained in the original

shape

.

If a

point

is inside the

shape

according to the

contains(point)

method, then it must
be inside the returned

Rectangle2D

bounds object according
to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(p)

requires

bounds.contains(p)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(p)

does not imply

shape.contains(p)

createIntersection

```java
public
Rectangle2D
createIntersection​(
Rectangle2D
r)
```

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:** createIntersection

in class

Rectangle2D
**Parameters:** r

- the

Rectangle2D

to be intersected with
this

Rectangle2D
**Returns:** the largest

Rectangle2D

contained in both
the specified

Rectangle2D

and in this

Rectangle2D

.
**Since:** 1.2

---

#### createIntersection

public

Rectangle2D

createIntersection​(

Rectangle2D

r)

Returns a new

Rectangle2D

object representing the
intersection of this

Rectangle2D

with the specified

Rectangle2D

.

createUnion

```java
public
Rectangle2D
createUnion​(
Rectangle2D
r)
```

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

**Specified by:** createUnion

in class

Rectangle2D
**Parameters:** r

- the

Rectangle2D

to be combined with
this

Rectangle2D
**Returns:** the smallest

Rectangle2D

containing both
the specified

Rectangle2D

and this

Rectangle2D

.
**Since:** 1.2

---

#### createUnion

public

Rectangle2D

createUnion​(

Rectangle2D

r)

Returns a new

Rectangle2D

object representing the
union of this

Rectangle2D

with the specified

Rectangle2D

.

toString

```java
public
String
toString()
```

Returns the

String

representation of this

Rectangle2D

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing this

Rectangle2D

.
**Since:** 1.2

---

#### toString

public

String

toString()

Returns the

String

representation of this

Rectangle2D

.

---

