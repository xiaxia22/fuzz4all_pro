# Class CubicCurve2D.Double

**Source:** `java.desktop\java\awt\geom\CubicCurve2D.Double.html`

### Class Description

```java
public static class
CubicCurve2D.Double

extends
CubicCurve2D

implements
Serializable
```

A cubic parametric curve segment specified with

double

coordinates.

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

---

### Field Details

#### public double x1

The X coordinate of the start point
of the cubic curve segment.

**Since:**
- 1.2

---

#### public double y1

The Y coordinate of the start point
of the cubic curve segment.

**Since:**
- 1.2

---

#### public double ctrlx1

The X coordinate of the first control point
of the cubic curve segment.

**Since:**
- 1.2

---

#### public double ctrly1

The Y coordinate of the first control point
of the cubic curve segment.

**Since:**
- 1.2

---

#### public double ctrlx2

The X coordinate of the second control point
of the cubic curve segment.

**Since:**
- 1.2

---

#### public double ctrly2

The Y coordinate of the second control point
of the cubic curve segment.

**Since:**
- 1.2

---

#### public double x2

The X coordinate of the end point
of the cubic curve segment.

**Since:**
- 1.2

---

#### public double y2

The Y coordinate of the end point
of the cubic curve segment.

**Since:**
- 1.2

---

### Constructor Details

#### public Double()

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

**Since:**
- 1.2

---

#### public Double​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Constructs and initializes a

CubicCurve2D

from
the specified

double

coordinates.

**Parameters:**
- x1

- the X coordinate for the start point
of the resulting

CubicCurve2D
- y1

- the Y coordinate for the start point
of the resulting

CubicCurve2D
- ctrlx1

- the X coordinate for the first control point
of the resulting

CubicCurve2D
- ctrly1

- the Y coordinate for the first control point
of the resulting

CubicCurve2D
- ctrlx2

- the X coordinate for the second control point
of the resulting

CubicCurve2D
- ctrly2

- the Y coordinate for the second control point
of the resulting

CubicCurve2D
- x2

- the X coordinate for the end point
of the resulting

CubicCurve2D
- y2

- the Y coordinate for the end point
of the resulting

CubicCurve2D

**Since:**
- 1.2

---

### Method Details

#### public double getX1()

Returns the X coordinate of the start point in double precision.

**Specified by:**
- getX1

in class

CubicCurve2D

**Returns:**
- the X coordinate of the start point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public double getY1()

Returns the Y coordinate of the start point in double precision.

**Specified by:**
- getY1

in class

CubicCurve2D

**Returns:**
- the Y coordinate of the start point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public
Point2D
getP1()

Returns the start point.

**Specified by:**
- getP1

in class

CubicCurve2D

**Returns:**
- a

Point2D

that is the start point of
the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public double getCtrlX1()

Returns the X coordinate of the first control point in double precision.

**Specified by:**
- getCtrlX1

in class

CubicCurve2D

**Returns:**
- the X coordinate of the first control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public double getCtrlY1()

Returns the Y coordinate of the first control point in double precision.

**Specified by:**
- getCtrlY1

in class

CubicCurve2D

**Returns:**
- the Y coordinate of the first control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public
Point2D
getCtrlP1()

Returns the first control point.

**Specified by:**
- getCtrlP1

in class

CubicCurve2D

**Returns:**
- a

Point2D

that is the first control point of
the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public double getCtrlX2()

Returns the X coordinate of the second control point
in double precision.

**Specified by:**
- getCtrlX2

in class

CubicCurve2D

**Returns:**
- the X coordinate of the second control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public double getCtrlY2()

Returns the Y coordinate of the second control point
in double precision.

**Specified by:**
- getCtrlY2

in class

CubicCurve2D

**Returns:**
- the Y coordinate of the second control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public
Point2D
getCtrlP2()

Returns the second control point.

**Specified by:**
- getCtrlP2

in class

CubicCurve2D

**Returns:**
- a

Point2D

that is the second control point of
the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public double getX2()

Returns the X coordinate of the end point in double precision.

**Specified by:**
- getX2

in class

CubicCurve2D

**Returns:**
- the X coordinate of the end point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public double getY2()

Returns the Y coordinate of the end point in double precision.

**Specified by:**
- getY2

in class

CubicCurve2D

**Returns:**
- the Y coordinate of the end point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public
Point2D
getP2()

Returns the end point.

**Specified by:**
- getP2

in class

CubicCurve2D

**Returns:**
- a

Point2D

that is the end point of
the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public void setCurve​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Sets the location of the end points and control points of this curve
to the specified double coordinates.

**Specified by:**
- setCurve

in class

CubicCurve2D

**Parameters:**
- x1

- the X coordinate used to set the start point
of this

CubicCurve2D
- y1

- the Y coordinate used to set the start point
of this

CubicCurve2D
- ctrlx1

- the X coordinate used to set the first control point
of this

CubicCurve2D
- ctrly1

- the Y coordinate used to set the first control point
of this

CubicCurve2D
- ctrlx2

- the X coordinate used to set the second control point
of this

CubicCurve2D
- ctrly2

- the Y coordinate used to set the second control point
of this

CubicCurve2D
- x2

- the X coordinate used to set the end point
of this

CubicCurve2D
- y2

- the Y coordinate used to set the end point
of this

CubicCurve2D

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

#### Class CubicCurve2D.Double

java.lang.Object

- java.awt.geom.CubicCurve2D
- - java.awt.geom.CubicCurve2D.Double

java.awt.geom.CubicCurve2D

- java.awt.geom.CubicCurve2D.Double

java.awt.geom.CubicCurve2D.Double

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

**Enclosing class:** CubicCurve2D

```java
public static class
CubicCurve2D.Double

extends
CubicCurve2D

implements
Serializable
```

A cubic parametric curve segment specified with

double

coordinates.

**Since:** 1.2
**See Also:** Serialized Form

public static class

CubicCurve2D.Double

extends

CubicCurve2D

implements

Serializable

A cubic parametric curve segment specified with

double

coordinates.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

CubicCurve2D

CubicCurve2D.Double

,

CubicCurve2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

double

ctrlx1

The X coordinate of the first control point
of the cubic curve segment.

double

ctrlx2

The X coordinate of the second control point
of the cubic curve segment.

double

ctrly1

The Y coordinate of the first control point
of the cubic curve segment.

double

ctrly2

The Y coordinate of the second control point
of the cubic curve segment.

double

x1

The X coordinate of the start point
of the cubic curve segment.

double

x2

The X coordinate of the end point
of the cubic curve segment.

double

y1

The Y coordinate of the start point
of the cubic curve segment.

double

y2

The Y coordinate of the end point
of the cubic curve segment.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Double

()

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

Double

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Constructs and initializes a

CubicCurve2D

from
the specified

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

getBounds2D

()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

Point2D

getCtrlP1

()

Returns the first control point.

Point2D

getCtrlP2

()

Returns the second control point.

double

getCtrlX1

()

Returns the X coordinate of the first control point in double precision.

double

getCtrlX2

()

Returns the X coordinate of the second control point
in double precision.

double

getCtrlY1

()

Returns the Y coordinate of the first control point in double precision.

double

getCtrlY2

()

Returns the Y coordinate of the second control point
in double precision.

Point2D

getP1

()

Returns the start point.

Point2D

getP2

()

Returns the end point.

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

setCurve

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Sets the location of the end points and control points of this curve
to the specified double coordinates.

- Methods declared in class java.awt.geom.

CubicCurve2D

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

getFlatness

,

getFlatness

,

getFlatness

,

getFlatnessSq

,

getFlatnessSq

,

getFlatnessSq

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

,

setCurve

,

setCurve

,

setCurve

,

setCurve

,

solveCubic

,

solveCubic

,

subdivide

,

subdivide

,

subdivide

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

CubicCurve2D

CubicCurve2D.Double

,

CubicCurve2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

CubicCurve2D

CubicCurve2D.Double

,

CubicCurve2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. CubicCurve2D

Field Summary

Fields

Modifier and Type

Field

Description

double

ctrlx1

The X coordinate of the first control point
of the cubic curve segment.

double

ctrlx2

The X coordinate of the second control point
of the cubic curve segment.

double

ctrly1

The Y coordinate of the first control point
of the cubic curve segment.

double

ctrly2

The Y coordinate of the second control point
of the cubic curve segment.

double

x1

The X coordinate of the start point
of the cubic curve segment.

double

x2

The X coordinate of the end point
of the cubic curve segment.

double

y1

The Y coordinate of the start point
of the cubic curve segment.

double

y2

The Y coordinate of the end point
of the cubic curve segment.

---

#### Field Summary

The X coordinate of the first control point
of the cubic curve segment.

The X coordinate of the second control point
of the cubic curve segment.

The Y coordinate of the first control point
of the cubic curve segment.

The Y coordinate of the second control point
of the cubic curve segment.

The X coordinate of the start point
of the cubic curve segment.

The X coordinate of the end point
of the cubic curve segment.

The Y coordinate of the start point
of the cubic curve segment.

The Y coordinate of the end point
of the cubic curve segment.

Constructor Summary

Constructors

Constructor

Description

Double

()

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

Double

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Constructs and initializes a

CubicCurve2D

from
the specified

double

coordinates.

---

#### Constructor Summary

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

Constructs and initializes a

CubicCurve2D

from
the specified

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

getBounds2D

()

Returns a high precision and more accurate bounding box of
the

Shape

than the

getBounds

method.

Point2D

getCtrlP1

()

Returns the first control point.

Point2D

getCtrlP2

()

Returns the second control point.

double

getCtrlX1

()

Returns the X coordinate of the first control point in double precision.

double

getCtrlX2

()

Returns the X coordinate of the second control point
in double precision.

double

getCtrlY1

()

Returns the Y coordinate of the first control point in double precision.

double

getCtrlY2

()

Returns the Y coordinate of the second control point
in double precision.

Point2D

getP1

()

Returns the start point.

Point2D

getP2

()

Returns the end point.

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

setCurve

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Sets the location of the end points and control points of this curve
to the specified double coordinates.

- Methods declared in class java.awt.geom.

CubicCurve2D

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

getFlatness

,

getFlatness

,

getFlatness

,

getFlatnessSq

,

getFlatnessSq

,

getFlatnessSq

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

,

setCurve

,

setCurve

,

setCurve

,

setCurve

,

solveCubic

,

solveCubic

,

subdivide

,

subdivide

,

subdivide

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

Returns the first control point.

Returns the second control point.

Returns the X coordinate of the first control point in double precision.

Returns the X coordinate of the second control point
in double precision.

Returns the Y coordinate of the first control point in double precision.

Returns the Y coordinate of the second control point
in double precision.

Returns the start point.

Returns the end point.

Returns the X coordinate of the start point in double precision.

Returns the X coordinate of the end point in double precision.

Returns the Y coordinate of the start point in double precision.

Returns the Y coordinate of the end point in double precision.

Sets the location of the end points and control points of this curve
to the specified double coordinates.

Methods declared in class java.awt.geom.

CubicCurve2D

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

getFlatness

,

getFlatness

,

getFlatness

,

getFlatnessSq

,

getFlatnessSq

,

getFlatnessSq

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

,

setCurve

,

setCurve

,

setCurve

,

setCurve

,

solveCubic

,

solveCubic

,

subdivide

,

subdivide

,

subdivide

---

#### Methods declared in class java.awt.geom. CubicCurve2D

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
public double x1
```

The X coordinate of the start point
of the cubic curve segment.

**Since:** 1.2

- y1

```java
public double y1
```

The Y coordinate of the start point
of the cubic curve segment.

**Since:** 1.2

- ctrlx1

```java
public double ctrlx1
```

The X coordinate of the first control point
of the cubic curve segment.

**Since:** 1.2

- ctrly1

```java
public double ctrly1
```

The Y coordinate of the first control point
of the cubic curve segment.

**Since:** 1.2

- ctrlx2

```java
public double ctrlx2
```

The X coordinate of the second control point
of the cubic curve segment.

**Since:** 1.2

- ctrly2

```java
public double ctrly2
```

The Y coordinate of the second control point
of the cubic curve segment.

**Since:** 1.2

- x2

```java
public double x2
```

The X coordinate of the end point
of the cubic curve segment.

**Since:** 1.2

- y2

```java
public double y2
```

The Y coordinate of the end point
of the cubic curve segment.

**Since:** 1.2

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Double

```java
public Double()
```

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

**Since:** 1.2

- Double

```java
public Double​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Constructs and initializes a

CubicCurve2D

from
the specified

double

coordinates.

**Parameters:** x1

- the X coordinate for the start point
of the resulting

CubicCurve2D
**Parameters:** y1

- the Y coordinate for the start point
of the resulting

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate for the first control point
of the resulting

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate for the first control point
of the resulting

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate for the second control point
of the resulting

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate for the second control point
of the resulting

CubicCurve2D
**Parameters:** x2

- the X coordinate for the end point
of the resulting

CubicCurve2D
**Parameters:** y2

- the Y coordinate for the end point
of the resulting

CubicCurve2D
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

CubicCurve2D
**Returns:** the X coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getY1

```java
public double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Specified by:** getY1

in class

CubicCurve2D
**Returns:** the Y coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getP1

```java
public
Point2D
getP1()
```

Returns the start point.

**Specified by:** getP1

in class

CubicCurve2D
**Returns:** a

Point2D

that is the start point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX1

```java
public double getCtrlX1()
```

Returns the X coordinate of the first control point in double precision.

**Specified by:** getCtrlX1

in class

CubicCurve2D
**Returns:** the X coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY1

```java
public double getCtrlY1()
```

Returns the Y coordinate of the first control point in double precision.

**Specified by:** getCtrlY1

in class

CubicCurve2D
**Returns:** the Y coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP1

```java
public
Point2D
getCtrlP1()
```

Returns the first control point.

**Specified by:** getCtrlP1

in class

CubicCurve2D
**Returns:** a

Point2D

that is the first control point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX2

```java
public double getCtrlX2()
```

Returns the X coordinate of the second control point
in double precision.

**Specified by:** getCtrlX2

in class

CubicCurve2D
**Returns:** the X coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY2

```java
public double getCtrlY2()
```

Returns the Y coordinate of the second control point
in double precision.

**Specified by:** getCtrlY2

in class

CubicCurve2D
**Returns:** the Y coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP2

```java
public
Point2D
getCtrlP2()
```

Returns the second control point.

**Specified by:** getCtrlP2

in class

CubicCurve2D
**Returns:** a

Point2D

that is the second control point of
the

CubicCurve2D

.
**Since:** 1.2

- getX2

```java
public double getX2()
```

Returns the X coordinate of the end point in double precision.

**Specified by:** getX2

in class

CubicCurve2D
**Returns:** the X coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getY2

```java
public double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Specified by:** getY2

in class

CubicCurve2D
**Returns:** the Y coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getP2

```java
public
Point2D
getP2()
```

Returns the end point.

**Specified by:** getP2

in class

CubicCurve2D
**Returns:** a

Point2D

that is the end point of
the

CubicCurve2D

.
**Since:** 1.2

- setCurve

```java
public void setCurve​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Sets the location of the end points and control points of this curve
to the specified double coordinates.

**Specified by:** setCurve

in class

CubicCurve2D
**Parameters:** x1

- the X coordinate used to set the start point
of this

CubicCurve2D
**Parameters:** y1

- the Y coordinate used to set the start point
of this

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate used to set the first control point
of this

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate used to set the first control point
of this

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate used to set the second control point
of this

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate used to set the second control point
of this

CubicCurve2D
**Parameters:** x2

- the X coordinate used to set the end point
of this

CubicCurve2D
**Parameters:** y2

- the Y coordinate used to set the end point
of this

CubicCurve2D
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
public double x1
```

The X coordinate of the start point
of the cubic curve segment.

**Since:** 1.2

- y1

```java
public double y1
```

The Y coordinate of the start point
of the cubic curve segment.

**Since:** 1.2

- ctrlx1

```java
public double ctrlx1
```

The X coordinate of the first control point
of the cubic curve segment.

**Since:** 1.2

- ctrly1

```java
public double ctrly1
```

The Y coordinate of the first control point
of the cubic curve segment.

**Since:** 1.2

- ctrlx2

```java
public double ctrlx2
```

The X coordinate of the second control point
of the cubic curve segment.

**Since:** 1.2

- ctrly2

```java
public double ctrly2
```

The Y coordinate of the second control point
of the cubic curve segment.

**Since:** 1.2

- x2

```java
public double x2
```

The X coordinate of the end point
of the cubic curve segment.

**Since:** 1.2

- y2

```java
public double y2
```

The Y coordinate of the end point
of the cubic curve segment.

**Since:** 1.2

---

#### Field Detail

x1

```java
public double x1
```

The X coordinate of the start point
of the cubic curve segment.

**Since:** 1.2

---

#### x1

public double x1

The X coordinate of the start point
of the cubic curve segment.

y1

```java
public double y1
```

The Y coordinate of the start point
of the cubic curve segment.

**Since:** 1.2

---

#### y1

public double y1

The Y coordinate of the start point
of the cubic curve segment.

ctrlx1

```java
public double ctrlx1
```

The X coordinate of the first control point
of the cubic curve segment.

**Since:** 1.2

---

#### ctrlx1

public double ctrlx1

The X coordinate of the first control point
of the cubic curve segment.

ctrly1

```java
public double ctrly1
```

The Y coordinate of the first control point
of the cubic curve segment.

**Since:** 1.2

---

#### ctrly1

public double ctrly1

The Y coordinate of the first control point
of the cubic curve segment.

ctrlx2

```java
public double ctrlx2
```

The X coordinate of the second control point
of the cubic curve segment.

**Since:** 1.2

---

#### ctrlx2

public double ctrlx2

The X coordinate of the second control point
of the cubic curve segment.

ctrly2

```java
public double ctrly2
```

The Y coordinate of the second control point
of the cubic curve segment.

**Since:** 1.2

---

#### ctrly2

public double ctrly2

The Y coordinate of the second control point
of the cubic curve segment.

x2

```java
public double x2
```

The X coordinate of the end point
of the cubic curve segment.

**Since:** 1.2

---

#### x2

public double x2

The X coordinate of the end point
of the cubic curve segment.

y2

```java
public double y2
```

The Y coordinate of the end point
of the cubic curve segment.

**Since:** 1.2

---

#### y2

public double y2

The Y coordinate of the end point
of the cubic curve segment.

Constructor Detail

- Double

```java
public Double()
```

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

**Since:** 1.2

- Double

```java
public Double​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Constructs and initializes a

CubicCurve2D

from
the specified

double

coordinates.

**Parameters:** x1

- the X coordinate for the start point
of the resulting

CubicCurve2D
**Parameters:** y1

- the Y coordinate for the start point
of the resulting

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate for the first control point
of the resulting

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate for the first control point
of the resulting

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate for the second control point
of the resulting

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate for the second control point
of the resulting

CubicCurve2D
**Parameters:** x2

- the X coordinate for the end point
of the resulting

CubicCurve2D
**Parameters:** y2

- the Y coordinate for the end point
of the resulting

CubicCurve2D
**Since:** 1.2

---

#### Constructor Detail

Double

```java
public Double()
```

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

**Since:** 1.2

---

#### Double

public Double()

Constructs and initializes a CubicCurve with coordinates
(0, 0, 0, 0, 0, 0, 0, 0).

Double

```java
public Double​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Constructs and initializes a

CubicCurve2D

from
the specified

double

coordinates.

**Parameters:** x1

- the X coordinate for the start point
of the resulting

CubicCurve2D
**Parameters:** y1

- the Y coordinate for the start point
of the resulting

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate for the first control point
of the resulting

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate for the first control point
of the resulting

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate for the second control point
of the resulting

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate for the second control point
of the resulting

CubicCurve2D
**Parameters:** x2

- the X coordinate for the end point
of the resulting

CubicCurve2D
**Parameters:** y2

- the Y coordinate for the end point
of the resulting

CubicCurve2D
**Since:** 1.2

---

#### Double

public Double​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Constructs and initializes a

CubicCurve2D

from
the specified

double

coordinates.

Method Detail

- getX1

```java
public double getX1()
```

Returns the X coordinate of the start point in double precision.

**Specified by:** getX1

in class

CubicCurve2D
**Returns:** the X coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getY1

```java
public double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Specified by:** getY1

in class

CubicCurve2D
**Returns:** the Y coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getP1

```java
public
Point2D
getP1()
```

Returns the start point.

**Specified by:** getP1

in class

CubicCurve2D
**Returns:** a

Point2D

that is the start point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX1

```java
public double getCtrlX1()
```

Returns the X coordinate of the first control point in double precision.

**Specified by:** getCtrlX1

in class

CubicCurve2D
**Returns:** the X coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY1

```java
public double getCtrlY1()
```

Returns the Y coordinate of the first control point in double precision.

**Specified by:** getCtrlY1

in class

CubicCurve2D
**Returns:** the Y coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP1

```java
public
Point2D
getCtrlP1()
```

Returns the first control point.

**Specified by:** getCtrlP1

in class

CubicCurve2D
**Returns:** a

Point2D

that is the first control point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX2

```java
public double getCtrlX2()
```

Returns the X coordinate of the second control point
in double precision.

**Specified by:** getCtrlX2

in class

CubicCurve2D
**Returns:** the X coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY2

```java
public double getCtrlY2()
```

Returns the Y coordinate of the second control point
in double precision.

**Specified by:** getCtrlY2

in class

CubicCurve2D
**Returns:** the Y coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP2

```java
public
Point2D
getCtrlP2()
```

Returns the second control point.

**Specified by:** getCtrlP2

in class

CubicCurve2D
**Returns:** a

Point2D

that is the second control point of
the

CubicCurve2D

.
**Since:** 1.2

- getX2

```java
public double getX2()
```

Returns the X coordinate of the end point in double precision.

**Specified by:** getX2

in class

CubicCurve2D
**Returns:** the X coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getY2

```java
public double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Specified by:** getY2

in class

CubicCurve2D
**Returns:** the Y coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getP2

```java
public
Point2D
getP2()
```

Returns the end point.

**Specified by:** getP2

in class

CubicCurve2D
**Returns:** a

Point2D

that is the end point of
the

CubicCurve2D

.
**Since:** 1.2

- setCurve

```java
public void setCurve​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Sets the location of the end points and control points of this curve
to the specified double coordinates.

**Specified by:** setCurve

in class

CubicCurve2D
**Parameters:** x1

- the X coordinate used to set the start point
of this

CubicCurve2D
**Parameters:** y1

- the Y coordinate used to set the start point
of this

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate used to set the first control point
of this

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate used to set the first control point
of this

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate used to set the second control point
of this

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate used to set the second control point
of this

CubicCurve2D
**Parameters:** x2

- the X coordinate used to set the end point
of this

CubicCurve2D
**Parameters:** y2

- the Y coordinate used to set the end point
of this

CubicCurve2D
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

CubicCurve2D
**Returns:** the X coordinate of the start point of the

CubicCurve2D

.
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

CubicCurve2D
**Returns:** the Y coordinate of the start point of the

CubicCurve2D

.
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

Returns the start point.

**Specified by:** getP1

in class

CubicCurve2D
**Returns:** a

Point2D

that is the start point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getP1

public

Point2D

getP1()

Returns the start point.

getCtrlX1

```java
public double getCtrlX1()
```

Returns the X coordinate of the first control point in double precision.

**Specified by:** getCtrlX1

in class

CubicCurve2D
**Returns:** the X coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlX1

public double getCtrlX1()

Returns the X coordinate of the first control point in double precision.

getCtrlY1

```java
public double getCtrlY1()
```

Returns the Y coordinate of the first control point in double precision.

**Specified by:** getCtrlY1

in class

CubicCurve2D
**Returns:** the Y coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlY1

public double getCtrlY1()

Returns the Y coordinate of the first control point in double precision.

getCtrlP1

```java
public
Point2D
getCtrlP1()
```

Returns the first control point.

**Specified by:** getCtrlP1

in class

CubicCurve2D
**Returns:** a

Point2D

that is the first control point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlP1

public

Point2D

getCtrlP1()

Returns the first control point.

getCtrlX2

```java
public double getCtrlX2()
```

Returns the X coordinate of the second control point
in double precision.

**Specified by:** getCtrlX2

in class

CubicCurve2D
**Returns:** the X coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlX2

public double getCtrlX2()

Returns the X coordinate of the second control point
in double precision.

getCtrlY2

```java
public double getCtrlY2()
```

Returns the Y coordinate of the second control point
in double precision.

**Specified by:** getCtrlY2

in class

CubicCurve2D
**Returns:** the Y coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlY2

public double getCtrlY2()

Returns the Y coordinate of the second control point
in double precision.

getCtrlP2

```java
public
Point2D
getCtrlP2()
```

Returns the second control point.

**Specified by:** getCtrlP2

in class

CubicCurve2D
**Returns:** a

Point2D

that is the second control point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlP2

public

Point2D

getCtrlP2()

Returns the second control point.

getX2

```java
public double getX2()
```

Returns the X coordinate of the end point in double precision.

**Specified by:** getX2

in class

CubicCurve2D
**Returns:** the X coordinate of the end point of the

CubicCurve2D

.
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

CubicCurve2D
**Returns:** the Y coordinate of the end point of the

CubicCurve2D

.
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

Returns the end point.

**Specified by:** getP2

in class

CubicCurve2D
**Returns:** a

Point2D

that is the end point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getP2

public

Point2D

getP2()

Returns the end point.

setCurve

```java
public void setCurve​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Sets the location of the end points and control points of this curve
to the specified double coordinates.

**Specified by:** setCurve

in class

CubicCurve2D
**Parameters:** x1

- the X coordinate used to set the start point
of this

CubicCurve2D
**Parameters:** y1

- the Y coordinate used to set the start point
of this

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate used to set the first control point
of this

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate used to set the first control point
of this

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate used to set the second control point
of this

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate used to set the second control point
of this

CubicCurve2D
**Parameters:** x2

- the X coordinate used to set the end point
of this

CubicCurve2D
**Parameters:** y2

- the Y coordinate used to set the end point
of this

CubicCurve2D
**Since:** 1.2

---

#### setCurve

public void setCurve​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Sets the location of the end points and control points of this curve
to the specified double coordinates.

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

