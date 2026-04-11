# Class Line2D.Float

**Source:** `java.desktop\java\awt\geom\Line2D.Float.html`

### Class Description

```java
public static class
Line2D.Float

extends
Line2D

implements
Serializable
```

A line segment specified with float coordinates.

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

---

### Field Details

#### public float x1

The X coordinate of the start point of the line segment.

**Since:**
- 1.2

---

#### public float y1

The Y coordinate of the start point of the line segment.

**Since:**
- 1.2

---

#### public float x2

The X coordinate of the end point of the line segment.

**Since:**
- 1.2

---

#### public float y2

The Y coordinate of the end point of the line segment.

**Since:**
- 1.2

---

### Constructor Details

#### public Float()

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

**Since:**
- 1.2

---

#### public Float​(float x1,
float y1,
float x2,
float y2)

Constructs and initializes a Line from the specified coordinates.

**Parameters:**
- x1

- the X coordinate of the start point
- y1

- the Y coordinate of the start point
- x2

- the X coordinate of the end point
- y2

- the Y coordinate of the end point

**Since:**
- 1.2

---

#### public Float​(
Point2D
p1,

Point2D
p2)

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

**Parameters:**
- p1

- the start

Point2D

of this line segment
- p2

- the end

Point2D

of this line segment

**Since:**
- 1.2

---

### Method Details

#### public double getX1()

Returns the X coordinate of the start point in double precision.

**Specified by:**
- getX1

in class

Line2D

**Returns:**
- the X coordinate of the start point of this

Line2D

object.

**Since:**
- 1.2

---

#### public double getY1()

Returns the Y coordinate of the start point in double precision.

**Specified by:**
- getY1

in class

Line2D

**Returns:**
- the Y coordinate of the start point of this

Line2D

object.

**Since:**
- 1.2

---

#### public
Point2D
getP1()

Returns the start

Point2D

of this

Line2D

.

**Specified by:**
- getP1

in class

Line2D

**Returns:**
- the start

Point2D

of this

Line2D

.

**Since:**
- 1.2

---

#### public double getX2()

Returns the X coordinate of the end point in double precision.

**Specified by:**
- getX2

in class

Line2D

**Returns:**
- the X coordinate of the end point of this

Line2D

object.

**Since:**
- 1.2

---

#### public double getY2()

Returns the Y coordinate of the end point in double precision.

**Specified by:**
- getY2

in class

Line2D

**Returns:**
- the Y coordinate of the end point of this

Line2D

object.

**Since:**
- 1.2

---

#### public
Point2D
getP2()

Returns the end

Point2D

of this

Line2D

.

**Specified by:**
- getP2

in class

Line2D

**Returns:**
- the end

Point2D

of this

Line2D

.

**Since:**
- 1.2

---

#### public void setLine​(double x1,
double y1,
double x2,
double y2)

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

**Specified by:**
- setLine

in class

Line2D

**Parameters:**
- x1

- the X coordinate of the start point
- y1

- the Y coordinate of the start point
- x2

- the X coordinate of the end point
- y2

- the Y coordinate of the end point

**Since:**
- 1.2

---

#### public void setLine​(float x1,
float y1,
float x2,
float y2)

Sets the location of the end points of this

Line2D

to the specified float coordinates.

**Parameters:**
- x1

- the X coordinate of the start point
- y1

- the Y coordinate of the start point
- x2

- the X coordinate of the end point
- y2

- the Y coordinate of the end point

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

### Additional Sections

#### Class Line2D.Float

java.lang.Object

- java.awt.geom.Line2D
- - java.awt.geom.Line2D.Float

java.awt.geom.Line2D

- java.awt.geom.Line2D.Float

java.awt.geom.Line2D.Float

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

**Enclosing class:** Line2D

```java
public static class
Line2D.Float

extends
Line2D

implements
Serializable
```

A line segment specified with float coordinates.

**Since:** 1.2
**See Also:** Serialized Form

public static class

Line2D.Float

extends

Line2D

implements

Serializable

A line segment specified with float coordinates.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Line2D

Line2D.Double

,

Line2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

float

x1

The X coordinate of the start point of the line segment.

float

x2

The X coordinate of the end point of the line segment.

float

y1

The Y coordinate of the start point of the line segment.

float

y2

The Y coordinate of the end point of the line segment.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Float

()

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

Float

​(float x1,
float y1,
float x2,
float y2)

Constructs and initializes a Line from the specified coordinates.

Float

​(

Point2D

p1,

Point2D

p2)

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle2D

getBounds2D

()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

Point2D

getP1

()

Returns the start

Point2D

of this

Line2D

.

Point2D

getP2

()

Returns the end

Point2D

of this

Line2D

.

double

getX1

()

Returns the X coordinate of the start point in double precision.

double

getX2

()

Returns the X coordinate of the end point in double precision.

double

getY1

()

Returns the Y coordinate of the start point in double precision.

double

getY2

()

Returns the Y coordinate of the end point in double precision.

void

setLine

​(double x1,
double y1,
double x2,
double y2)

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

void

setLine

​(float x1,
float y1,
float x2,
float y2)

Sets the location of the end points of this

Line2D

to the specified float coordinates.

- Methods declared in class java.awt.geom.

Line2D

clone

,

contains

,

contains

,

contains

,

contains

,

getBounds

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

,

intersectsLine

,

intersectsLine

,

linesIntersect

,

ptLineDist

,

ptLineDist

,

ptLineDist

,

ptLineDistSq

,

ptLineDistSq

,

ptLineDistSq

,

ptSegDist

,

ptSegDist

,

ptSegDist

,

ptSegDistSq

,

ptSegDistSq

,

ptSegDistSq

,

relativeCCW

,

relativeCCW

,

relativeCCW

,

setLine

,

setLine

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

- Nested classes/interfaces declared in class java.awt.geom.

Line2D

Line2D.Double

,

Line2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

Line2D

Line2D.Double

,

Line2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. Line2D

Field Summary

Fields

Modifier and Type

Field

Description

float

x1

The X coordinate of the start point of the line segment.

float

x2

The X coordinate of the end point of the line segment.

float

y1

The Y coordinate of the start point of the line segment.

float

y2

The Y coordinate of the end point of the line segment.

---

#### Field Summary

The X coordinate of the start point of the line segment.

The X coordinate of the end point of the line segment.

The Y coordinate of the start point of the line segment.

The Y coordinate of the end point of the line segment.

Constructor Summary

Constructors

Constructor

Description

Float

()

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

Float

​(float x1,
float y1,
float x2,
float y2)

Constructs and initializes a Line from the specified coordinates.

Float

​(

Point2D

p1,

Point2D

p2)

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

---

#### Constructor Summary

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

Constructs and initializes a Line from the specified coordinates.

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle2D

getBounds2D

()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

Point2D

getP1

()

Returns the start

Point2D

of this

Line2D

.

Point2D

getP2

()

Returns the end

Point2D

of this

Line2D

.

double

getX1

()

Returns the X coordinate of the start point in double precision.

double

getX2

()

Returns the X coordinate of the end point in double precision.

double

getY1

()

Returns the Y coordinate of the start point in double precision.

double

getY2

()

Returns the Y coordinate of the end point in double precision.

void

setLine

​(double x1,
double y1,
double x2,
double y2)

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

void

setLine

​(float x1,
float y1,
float x2,
float y2)

Sets the location of the end points of this

Line2D

to the specified float coordinates.

- Methods declared in class java.awt.geom.

Line2D

clone

,

contains

,

contains

,

contains

,

contains

,

getBounds

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

,

intersectsLine

,

intersectsLine

,

linesIntersect

,

ptLineDist

,

ptLineDist

,

ptLineDist

,

ptLineDistSq

,

ptLineDistSq

,

ptLineDistSq

,

ptSegDist

,

ptSegDist

,

ptSegDist

,

ptSegDistSq

,

ptSegDistSq

,

ptSegDistSq

,

relativeCCW

,

relativeCCW

,

relativeCCW

,

setLine

,

setLine

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

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

Returns the start

Point2D

of this

Line2D

.

Returns the end

Point2D

of this

Line2D

.

Returns the X coordinate of the start point in double precision.

Returns the X coordinate of the end point in double precision.

Returns the Y coordinate of the start point in double precision.

Returns the Y coordinate of the end point in double precision.

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

Sets the location of the end points of this

Line2D

to the specified float coordinates.

Methods declared in class java.awt.geom.

Line2D

clone

,

contains

,

contains

,

contains

,

contains

,

getBounds

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

,

intersectsLine

,

intersectsLine

,

linesIntersect

,

ptLineDist

,

ptLineDist

,

ptLineDist

,

ptLineDistSq

,

ptLineDistSq

,

ptLineDistSq

,

ptSegDist

,

ptSegDist

,

ptSegDist

,

ptSegDistSq

,

ptSegDistSq

,

ptSegDistSq

,

relativeCCW

,

relativeCCW

,

relativeCCW

,

setLine

,

setLine

---

#### Methods declared in class java.awt.geom. Line2D

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

============ FIELD DETAIL ===========

- Field Detail

- x1

```java
public float x1
```

The X coordinate of the start point of the line segment.

**Since:** 1.2

- y1

```java
public float y1
```

The Y coordinate of the start point of the line segment.

**Since:** 1.2

- x2

```java
public float x2
```

The X coordinate of the end point of the line segment.

**Since:** 1.2

- y2

```java
public float y2
```

The Y coordinate of the end point of the line segment.

**Since:** 1.2

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Float

```java
public Float()
```

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

**Since:** 1.2

- Float

```java
public Float​(float x1,
float y1,
float x2,
float y2)
```

Constructs and initializes a Line from the specified coordinates.

**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

- Float

```java
public Float​(
Point2D
p1,

Point2D
p2)
```

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

**Parameters:** p1

- the start

Point2D

of this line segment
**Parameters:** p2

- the end

Point2D

of this line segment
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getX1

```java
public double getX1()
```

Returns the X coordinate of the start point in double precision.

**Specified by:** getX1

in class

Line2D
**Returns:** the X coordinate of the start point of this

Line2D

object.
**Since:** 1.2

- getY1

```java
public double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Specified by:** getY1

in class

Line2D
**Returns:** the Y coordinate of the start point of this

Line2D

object.
**Since:** 1.2

- getP1

```java
public
Point2D
getP1()
```

Returns the start

Point2D

of this

Line2D

.

**Specified by:** getP1

in class

Line2D
**Returns:** the start

Point2D

of this

Line2D

.
**Since:** 1.2

- getX2

```java
public double getX2()
```

Returns the X coordinate of the end point in double precision.

**Specified by:** getX2

in class

Line2D
**Returns:** the X coordinate of the end point of this

Line2D

object.
**Since:** 1.2

- getY2

```java
public double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Specified by:** getY2

in class

Line2D
**Returns:** the Y coordinate of the end point of this

Line2D

object.
**Since:** 1.2

- getP2

```java
public
Point2D
getP2()
```

Returns the end

Point2D

of this

Line2D

.

**Specified by:** getP2

in class

Line2D
**Returns:** the end

Point2D

of this

Line2D

.
**Since:** 1.2

- setLine

```java
public void setLine​(double x1,
double y1,
double x2,
double y2)
```

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

**Specified by:** setLine

in class

Line2D
**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

- setLine

```java
public void setLine​(float x1,
float y1,
float x2,
float y2)
```

Sets the location of the end points of this

Line2D

to the specified float coordinates.

**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

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
**Returns:** an instance of

Rectangle2D

that is a
high-precision bounding box of the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds()

Field Detail

- x1

```java
public float x1
```

The X coordinate of the start point of the line segment.

**Since:** 1.2

- y1

```java
public float y1
```

The Y coordinate of the start point of the line segment.

**Since:** 1.2

- x2

```java
public float x2
```

The X coordinate of the end point of the line segment.

**Since:** 1.2

- y2

```java
public float y2
```

The Y coordinate of the end point of the line segment.

**Since:** 1.2

---

#### Field Detail

x1

```java
public float x1
```

The X coordinate of the start point of the line segment.

**Since:** 1.2

---

#### x1

public float x1

The X coordinate of the start point of the line segment.

y1

```java
public float y1
```

The Y coordinate of the start point of the line segment.

**Since:** 1.2

---

#### y1

public float y1

The Y coordinate of the start point of the line segment.

x2

```java
public float x2
```

The X coordinate of the end point of the line segment.

**Since:** 1.2

---

#### x2

public float x2

The X coordinate of the end point of the line segment.

y2

```java
public float y2
```

The Y coordinate of the end point of the line segment.

**Since:** 1.2

---

#### y2

public float y2

The Y coordinate of the end point of the line segment.

Constructor Detail

- Float

```java
public Float()
```

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

**Since:** 1.2

- Float

```java
public Float​(float x1,
float y1,
float x2,
float y2)
```

Constructs and initializes a Line from the specified coordinates.

**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

- Float

```java
public Float​(
Point2D
p1,

Point2D
p2)
```

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

**Parameters:** p1

- the start

Point2D

of this line segment
**Parameters:** p2

- the end

Point2D

of this line segment
**Since:** 1.2

---

#### Constructor Detail

Float

```java
public Float()
```

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

**Since:** 1.2

---

#### Float

public Float()

Constructs and initializes a Line with coordinates (0, 0) → (0, 0).

Float

```java
public Float​(float x1,
float y1,
float x2,
float y2)
```

Constructs and initializes a Line from the specified coordinates.

**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

---

#### Float

public Float​(float x1,
float y1,
float x2,
float y2)

Constructs and initializes a Line from the specified coordinates.

Float

```java
public Float​(
Point2D
p1,

Point2D
p2)
```

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

**Parameters:** p1

- the start

Point2D

of this line segment
**Parameters:** p2

- the end

Point2D

of this line segment
**Since:** 1.2

---

#### Float

public Float​(

Point2D

p1,

Point2D

p2)

Constructs and initializes a

Line2D

from the
specified

Point2D

objects.

Method Detail

- getX1

```java
public double getX1()
```

Returns the X coordinate of the start point in double precision.

**Specified by:** getX1

in class

Line2D
**Returns:** the X coordinate of the start point of this

Line2D

object.
**Since:** 1.2

- getY1

```java
public double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Specified by:** getY1

in class

Line2D
**Returns:** the Y coordinate of the start point of this

Line2D

object.
**Since:** 1.2

- getP1

```java
public
Point2D
getP1()
```

Returns the start

Point2D

of this

Line2D

.

**Specified by:** getP1

in class

Line2D
**Returns:** the start

Point2D

of this

Line2D

.
**Since:** 1.2

- getX2

```java
public double getX2()
```

Returns the X coordinate of the end point in double precision.

**Specified by:** getX2

in class

Line2D
**Returns:** the X coordinate of the end point of this

Line2D

object.
**Since:** 1.2

- getY2

```java
public double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Specified by:** getY2

in class

Line2D
**Returns:** the Y coordinate of the end point of this

Line2D

object.
**Since:** 1.2

- getP2

```java
public
Point2D
getP2()
```

Returns the end

Point2D

of this

Line2D

.

**Specified by:** getP2

in class

Line2D
**Returns:** the end

Point2D

of this

Line2D

.
**Since:** 1.2

- setLine

```java
public void setLine​(double x1,
double y1,
double x2,
double y2)
```

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

**Specified by:** setLine

in class

Line2D
**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

- setLine

```java
public void setLine​(float x1,
float y1,
float x2,
float y2)
```

Sets the location of the end points of this

Line2D

to the specified float coordinates.

**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

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
**Returns:** an instance of

Rectangle2D

that is a
high-precision bounding box of the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds()

---

#### Method Detail

getX1

```java
public double getX1()
```

Returns the X coordinate of the start point in double precision.

**Specified by:** getX1

in class

Line2D
**Returns:** the X coordinate of the start point of this

Line2D

object.
**Since:** 1.2

---

#### getX1

public double getX1()

Returns the X coordinate of the start point in double precision.

getY1

```java
public double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Specified by:** getY1

in class

Line2D
**Returns:** the Y coordinate of the start point of this

Line2D

object.
**Since:** 1.2

---

#### getY1

public double getY1()

Returns the Y coordinate of the start point in double precision.

getP1

```java
public
Point2D
getP1()
```

Returns the start

Point2D

of this

Line2D

.

**Specified by:** getP1

in class

Line2D
**Returns:** the start

Point2D

of this

Line2D

.
**Since:** 1.2

---

#### getP1

public

Point2D

getP1()

Returns the start

Point2D

of this

Line2D

.

getX2

```java
public double getX2()
```

Returns the X coordinate of the end point in double precision.

**Specified by:** getX2

in class

Line2D
**Returns:** the X coordinate of the end point of this

Line2D

object.
**Since:** 1.2

---

#### getX2

public double getX2()

Returns the X coordinate of the end point in double precision.

getY2

```java
public double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Specified by:** getY2

in class

Line2D
**Returns:** the Y coordinate of the end point of this

Line2D

object.
**Since:** 1.2

---

#### getY2

public double getY2()

Returns the Y coordinate of the end point in double precision.

getP2

```java
public
Point2D
getP2()
```

Returns the end

Point2D

of this

Line2D

.

**Specified by:** getP2

in class

Line2D
**Returns:** the end

Point2D

of this

Line2D

.
**Since:** 1.2

---

#### getP2

public

Point2D

getP2()

Returns the end

Point2D

of this

Line2D

.

setLine

```java
public void setLine​(double x1,
double y1,
double x2,
double y2)
```

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

**Specified by:** setLine

in class

Line2D
**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

---

#### setLine

public void setLine​(double x1,
double y1,
double x2,
double y2)

Sets the location of the end points of this

Line2D

to
the specified double coordinates.

setLine

```java
public void setLine​(float x1,
float y1,
float x2,
float y2)
```

Sets the location of the end points of this

Line2D

to the specified float coordinates.

**Parameters:** x1

- the X coordinate of the start point
**Parameters:** y1

- the Y coordinate of the start point
**Parameters:** x2

- the X coordinate of the end point
**Parameters:** y2

- the Y coordinate of the end point
**Since:** 1.2

---

#### setLine

public void setLine​(float x1,
float y1,
float x2,
float y2)

Sets the location of the end points of this

Line2D

to the specified float coordinates.

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

---

