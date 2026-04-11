# Class CubicCurve2D

**Source:** `java.desktop\java\awt\geom\CubicCurve2D.html`

### Class Description

```java
public abstract class
CubicCurve2D

extends
Object

implements
Shape
,
Cloneable
```

The

CubicCurve2D

class defines a cubic parametric curve
segment in

(x,y)

coordinate space.

This class is only the abstract superclass for all objects which
store a 2D cubic curve segment.
The actual storage representation of the coordinates is left to
the subclass.

**All Implemented Interfaces:** Shape

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CubicCurve2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**See Also:**
- CubicCurve2D.Float

,

CubicCurve2D.Double

**Since:**
- 1.2

---

### Method Details

#### public abstract double getX1()

Returns the X coordinate of the start point in double precision.

**Returns:**
- the X coordinate of the start point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract double getY1()

Returns the Y coordinate of the start point in double precision.

**Returns:**
- the Y coordinate of the start point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract
Point2D
getP1()

Returns the start point.

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

#### public abstract double getCtrlX1()

Returns the X coordinate of the first control point in double precision.

**Returns:**
- the X coordinate of the first control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract double getCtrlY1()

Returns the Y coordinate of the first control point in double precision.

**Returns:**
- the Y coordinate of the first control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract
Point2D
getCtrlP1()

Returns the first control point.

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

#### public abstract double getCtrlX2()

Returns the X coordinate of the second control point
in double precision.

**Returns:**
- the X coordinate of the second control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract double getCtrlY2()

Returns the Y coordinate of the second control point
in double precision.

**Returns:**
- the Y coordinate of the second control point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract
Point2D
getCtrlP2()

Returns the second control point.

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

#### public abstract double getX2()

Returns the X coordinate of the end point in double precision.

**Returns:**
- the X coordinate of the end point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract double getY2()

Returns the Y coordinate of the end point in double precision.

**Returns:**
- the Y coordinate of the end point of the

CubicCurve2D

.

**Since:**
- 1.2

---

#### public abstract
Point2D
getP2()

Returns the end point.

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

#### public abstract void setCurve​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Sets the location of the end points and control points of this curve
to the specified double coordinates.

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

#### public void setCurve​(double[] coords,
int offset)

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

**Parameters:**
- coords

- a double array containing coordinates
- offset

- the index of

coords

from which to begin
setting the end points and control points of this curve
to the coordinates contained in

coords

**Since:**
- 1.2

---

#### public void setCurve​(
Point2D
p1,

Point2D
cp1,

Point2D
cp2,

Point2D
p2)

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

**Parameters:**
- p1

- the first specified

Point2D

used to set the
start point of this curve
- cp1

- the second specified

Point2D

used to set the
first control point of this curve
- cp2

- the third specified

Point2D

used to set the
second control point of this curve
- p2

- the fourth specified

Point2D

used to set the
end point of this curve

**Since:**
- 1.2

---

#### public void setCurve​(
Point2D
[] pts,
int offset)

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

**Parameters:**
- pts

- an array of

Point2D

objects
- offset

- the index of

pts

from which to begin setting
the end points and control points of this curve to the
points contained in

pts

**Since:**
- 1.2

---

#### public void setCurve​(
CubicCurve2D
c)

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

**Parameters:**
- c

- the specified

CubicCurve2D

**Since:**
- 1.2

---

#### public static double getFlatnessSq​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the square of the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:**
- x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
- y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
- ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
- ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
- ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
- ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
- x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
- y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D

**Returns:**
- the square of the flatness of the

CubicCurve2D

represented by the specified coordinates.

**Since:**
- 1.2

---

#### public static double getFlatness​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:**
- x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
- y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
- ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
- ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
- ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
- ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
- x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
- y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D

**Returns:**
- the flatness of the

CubicCurve2D

represented by the specified coordinates.

**Since:**
- 1.2

---

#### public static double getFlatnessSq​(double[] coords,
int offset)

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:**
- coords

- an array containing coordinates
- offset

- the index of

coords

from which to begin
getting the end points and control points of the curve

**Returns:**
- the square of the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.

**Since:**
- 1.2

---

#### public static double getFlatness​(double[] coords,
int offset)

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:**
- coords

- an array containing coordinates
- offset

- the index of

coords

from which to begin
getting the end points and control points of the curve

**Returns:**
- the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.

**Since:**
- 1.2

---

#### public double getFlatnessSq()

Returns the square of the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:**
- the square of the flatness of this curve.

**Since:**
- 1.2

---

#### public double getFlatness()

Returns the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:**
- the flatness of this curve.

**Since:**
- 1.2

---

#### public void subdivide​(
CubicCurve2D
left,

CubicCurve2D
right)

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.
Either or both of the left and right objects may be the same
as this object or null.

**Parameters:**
- left

- the cubic curve object for storing for the left or
first half of the subdivided curve
- right

- the cubic curve object for storing for the right or
second half of the subdivided curve

**Since:**
- 1.2

---

#### public static void subdivide​(
CubicCurve2D
src,

CubicCurve2D
left,

CubicCurve2D
right)

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.
Either or both of the

left

and

right

objects
may be the same as the

src

object or

null

.

**Parameters:**
- src

- the cubic curve to be subdivided
- left

- the cubic curve object for storing the left or
first half of the subdivided curve
- right

- the cubic curve object for storing the right or
second half of the subdivided curve

**Since:**
- 1.2

---

#### public static void subdivide​(double[] src,
int srcoff,
double[] left,
int leftoff,
double[] right,
int rightoff)

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.
Either or both of the

left

and

right

arrays may be

null

or a reference to the same array
as the

src

array.
Note that the last point in the first subdivided curve is the
same as the first point in the second subdivided curve. Thus,
it is possible to pass the same array for

left

and

right

and to use offsets, such as

rightoff

equals (

leftoff

+ 6), in order
to avoid allocating extra storage for this common point.

**Parameters:**
- src

- the array holding the coordinates for the source curve
- srcoff

- the offset into the array of the beginning of the
the 6 source coordinates
- left

- the array for storing the coordinates for the first
half of the subdivided curve
- leftoff

- the offset into the array of the beginning of the
the 6 left coordinates
- right

- the array for storing the coordinates for the second
half of the subdivided curve
- rightoff

- the offset into the array of the beginning of the
the 6 right coordinates

**Since:**
- 1.2

---

#### public static int solveCubic​(double[] eqn)

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots. The solved cubic is represented
by the equation:

```java
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
```

A return value of -1 is used to distinguish a constant equation
that might be always 0 or never 0 from an equation that has no
zeroes.

**Parameters:**
- eqn

- an array containing coefficients for a cubic

**Returns:**
- the number of roots, or -1 if the equation is a constant.

**Since:**
- 1.2

---

#### public static int solveCubic​(double[] eqn,
double[] res)

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.
The cubic solved is represented by the equation:
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
A return value of -1 is used to distinguish a constant equation,
which may be always 0 or never 0, from an equation which has no
zeroes.

**Parameters:**
- eqn

- the specified array of coefficients to use to solve
the cubic equation
- res

- the array that contains the non-complex roots
resulting from the solution of the cubic equation

**Returns:**
- the number of roots, or -1 if the equation is a constant

**Since:**
- 1.3

---

#### public boolean contains​(double x,
double y)

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

**Specified by:**
- contains

in interface

Shape

**Parameters:**
- x

- the specified X coordinate to be tested
- y

- the specified Y coordinate to be tested

**Returns:**
- true

if the specified coordinates are inside
the

Shape

boundary;

false

otherwise.

**Since:**
- 1.2

---

#### public boolean contains​(
Point2D
p)

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

**Specified by:**
- contains

in interface

Shape

**Parameters:**
- p

- the specified

Point2D

to be tested

**Returns:**
- true

if the specified

Point2D

is
inside the boundary of the

Shape

;

false

otherwise.

**Since:**
- 1.2

---

#### public boolean intersects​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.
The rectangular area is considered to intersect the

Shape

if any point is contained in both the interior of the

Shape

and the specified rectangular area.

The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the rectangular area and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the rectangular area does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:**
- intersects

in interface

Shape

**Parameters:**
- x

- the X coordinate of the upper-left corner
of the specified rectangular area
- y

- the Y coordinate of the upper-left corner
of the specified rectangular area
- w

- the width of the specified rectangular area
- h

- the height of the specified rectangular area

**Returns:**
- true

if the interior of the

Shape

and
the interior of the rectangular area intersect, or are
both highly likely to intersect and intersection calculations
would be too expensive to perform;

false

otherwise.

**See Also:**
- Area

**Since:**
- 1.2

---

#### public boolean intersects​(
Rectangle2D
r)

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.
The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the

Rectangle2D

and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the

Rectangle2D

does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:**
- intersects

in interface

Shape

**Parameters:**
- r

- the specified

Rectangle2D

**Returns:**
- true

if the interior of the

Shape

and
the interior of the specified

Rectangle2D

intersect, or are both highly likely to intersect and intersection
calculations would be too expensive to perform;

false

otherwise.

**See Also:**
- Shape.intersects(double, double, double, double)

**Since:**
- 1.2

---

#### public boolean contains​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

entirely contains
the specified rectangular area. All coordinates that lie inside
the rectangular area must lie within the

Shape

for the
entire rectangular area to be considered contained within the

Shape

.

The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the rectangular area are
prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the rectangular area.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:**
- contains

in interface

Shape

**Parameters:**
- x

- the X coordinate of the upper-left corner
of the specified rectangular area
- y

- the Y coordinate of the upper-left corner
of the specified rectangular area
- w

- the width of the specified rectangular area
- h

- the height of the specified rectangular area

**Returns:**
- true

if the interior of the

Shape

entirely contains the specified rectangular area;

false

otherwise or, if the

Shape

contains the rectangular area and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.

**See Also:**
- Area

,

Shape.intersects(double, double, double, double)

**Since:**
- 1.2

---

#### public boolean contains​(
Rectangle2D
r)

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.
The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the

Rectangle2D

are prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the

Rectangle2D

.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:**
- contains

in interface

Shape

**Parameters:**
- r

- The specified

Rectangle2D

**Returns:**
- true

if the interior of the

Shape

entirely contains the

Rectangle2D

;

false

otherwise or, if the

Shape

contains the

Rectangle2D

and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.

**See Also:**
- Shape.contains(double, double, double, double)

**Since:**
- 1.2

---

#### public
Rectangle
getBounds()

Returns an integer

Rectangle

that completely encloses the

Shape

. Note that there is no guarantee that the
returned

Rectangle

is the smallest bounding box that
encloses the

Shape

, only that the

Shape

lies entirely within the indicated

Rectangle

. The
returned

Rectangle

might also fail to completely
enclose the

Shape

if the

Shape

overflows
the limited range of the integer data type. The

getBounds2D

method generally returns a
tighter bounding box due to its greater flexibility in
representation.

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

method, then
it must be inside the returned

Rectangle

bounds object
according to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(x,y)

requires

bounds.contains(x,y)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(x,y)

does not imply

shape.contains(x,y)

**Specified by:**
- getBounds

in interface

Shape

**Returns:**
- an integer

Rectangle

that completely encloses
the

Shape

.

**See Also:**
- Shape.getBounds2D()

**Since:**
- 1.2

---

#### public
PathIterator
getPathIterator​(
AffineTransform
at)

Returns an iteration object that defines the boundary of the
shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:**
- getPathIterator

in interface

Shape

**Parameters:**
- at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired

**Returns:**
- the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

, one
segment at a time.

**Since:**
- 1.2

---

#### public
PathIterator
getPathIterator​(
AffineTransform
at,
double flatness)

Return an iteration object that defines the boundary of the
flattened shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:**
- getPathIterator

in interface

Shape

**Parameters:**
- at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
- flatness

- the maximum amount that the control points
for a given curve can vary from colinear before a subdivided
curve is replaced by a straight line connecting the end points

**Returns:**
- the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

,
one segment at a time.

**Since:**
- 1.2

---

#### public
Object
clone()

Creates a new object of the same class as this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- OutOfMemoryError

- if there is not enough memory.

**See Also:**
- Cloneable

**Since:**
- 1.2

---

### Additional Sections

#### Class CubicCurve2D

java.lang.Object

- java.awt.geom.CubicCurve2D

java.awt.geom.CubicCurve2D

**All Implemented Interfaces:** Shape

,

Cloneable

**Direct Known Subclasses:** CubicCurve2D.Double

,

CubicCurve2D.Float

```java
public abstract class
CubicCurve2D

extends
Object

implements
Shape
,
Cloneable
```

The

CubicCurve2D

class defines a cubic parametric curve
segment in

(x,y)

coordinate space.

This class is only the abstract superclass for all objects which
store a 2D cubic curve segment.
The actual storage representation of the coordinates is left to
the subclass.

**Since:** 1.2

public abstract class

CubicCurve2D

extends

Object

implements

Shape

,

Cloneable

The

CubicCurve2D

class defines a cubic parametric curve
segment in

(x,y)

coordinate space.

This class is only the abstract superclass for all objects which
store a 2D cubic curve segment.
The actual storage representation of the coordinates is left to
the subclass.

This class is only the abstract superclass for all objects which
store a 2D cubic curve segment.
The actual storage representation of the coordinates is left to
the subclass.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CubicCurve2D.Double

A cubic parametric curve segment specified with

double

coordinates.

static class

CubicCurve2D.Float

A cubic parametric curve segment specified with

float

coordinates.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CubicCurve2D

()

This is an abstract class that cannot be instantiated directly.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a new object of the same class as this object.

boolean

contains

​(double x,
double y)

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

boolean

contains

​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

entirely contains
the specified rectangular area.

boolean

contains

​(

Point2D

p)

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

boolean

contains

​(

Rectangle2D

r)

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.

Rectangle

getBounds

()

Returns an integer

Rectangle

that completely encloses the

Shape

.

abstract

Point2D

getCtrlP1

()

Returns the first control point.

abstract

Point2D

getCtrlP2

()

Returns the second control point.

abstract double

getCtrlX1

()

Returns the X coordinate of the first control point in double precision.

abstract double

getCtrlX2

()

Returns the X coordinate of the second control point
in double precision.

abstract double

getCtrlY1

()

Returns the Y coordinate of the first control point in double precision.

abstract double

getCtrlY2

()

Returns the Y coordinate of the second control point
in double precision.

double

getFlatness

()

Returns the flatness of this curve.

static double

getFlatness

​(double[] coords,
int offset)

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index.

static double

getFlatness

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the flatness of the cubic curve specified
by the indicated control points.

double

getFlatnessSq

()

Returns the square of the flatness of this curve.

static double

getFlatnessSq

​(double[] coords,
int offset)

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index.

static double

getFlatnessSq

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the square of the flatness of the cubic curve specified
by the indicated control points.

abstract

Point2D

getP1

()

Returns the start point.

abstract

Point2D

getP2

()

Returns the end point.

PathIterator

getPathIterator

​(

AffineTransform

at)

Returns an iteration object that defines the boundary of the
shape.

PathIterator

getPathIterator

​(

AffineTransform

at,
double flatness)

Return an iteration object that defines the boundary of the
flattened shape.

abstract double

getX1

()

Returns the X coordinate of the start point in double precision.

abstract double

getX2

()

Returns the X coordinate of the end point in double precision.

abstract double

getY1

()

Returns the Y coordinate of the start point in double precision.

abstract double

getY2

()

Returns the Y coordinate of the end point in double precision.

boolean

intersects

​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.

boolean

intersects

​(

Rectangle2D

r)

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.

void

setCurve

​(double[] coords,
int offset)

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

abstract void

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

void

setCurve

​(

CubicCurve2D

c)

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

void

setCurve

​(

Point2D

[] pts,
int offset)

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

void

setCurve

​(

Point2D

p1,

Point2D

cp1,

Point2D

cp2,

Point2D

p2)

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

static int

solveCubic

​(double[] eqn)

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots.

static int

solveCubic

​(double[] eqn,
double[] res)

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.

static void

subdivide

​(double[] src,
int srcoff,
double[] left,
int leftoff,
double[] right,
int rightoff)

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.

void

subdivide

​(

CubicCurve2D

left,

CubicCurve2D

right)

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.

static void

subdivide

​(

CubicCurve2D

src,

CubicCurve2D

left,

CubicCurve2D

right)

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.

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

- Methods declared in interface java.awt.

Shape

getBounds2D

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CubicCurve2D.Double

A cubic parametric curve segment specified with

double

coordinates.

static class

CubicCurve2D.Float

A cubic parametric curve segment specified with

float

coordinates.

---

#### Nested Class Summary

A cubic parametric curve segment specified with

double

coordinates.

A cubic parametric curve segment specified with

float

coordinates.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CubicCurve2D

()

This is an abstract class that cannot be instantiated directly.

---

#### Constructor Summary

This is an abstract class that cannot be instantiated directly.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a new object of the same class as this object.

boolean

contains

​(double x,
double y)

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

boolean

contains

​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

entirely contains
the specified rectangular area.

boolean

contains

​(

Point2D

p)

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

boolean

contains

​(

Rectangle2D

r)

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.

Rectangle

getBounds

()

Returns an integer

Rectangle

that completely encloses the

Shape

.

abstract

Point2D

getCtrlP1

()

Returns the first control point.

abstract

Point2D

getCtrlP2

()

Returns the second control point.

abstract double

getCtrlX1

()

Returns the X coordinate of the first control point in double precision.

abstract double

getCtrlX2

()

Returns the X coordinate of the second control point
in double precision.

abstract double

getCtrlY1

()

Returns the Y coordinate of the first control point in double precision.

abstract double

getCtrlY2

()

Returns the Y coordinate of the second control point
in double precision.

double

getFlatness

()

Returns the flatness of this curve.

static double

getFlatness

​(double[] coords,
int offset)

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index.

static double

getFlatness

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the flatness of the cubic curve specified
by the indicated control points.

double

getFlatnessSq

()

Returns the square of the flatness of this curve.

static double

getFlatnessSq

​(double[] coords,
int offset)

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index.

static double

getFlatnessSq

​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the square of the flatness of the cubic curve specified
by the indicated control points.

abstract

Point2D

getP1

()

Returns the start point.

abstract

Point2D

getP2

()

Returns the end point.

PathIterator

getPathIterator

​(

AffineTransform

at)

Returns an iteration object that defines the boundary of the
shape.

PathIterator

getPathIterator

​(

AffineTransform

at,
double flatness)

Return an iteration object that defines the boundary of the
flattened shape.

abstract double

getX1

()

Returns the X coordinate of the start point in double precision.

abstract double

getX2

()

Returns the X coordinate of the end point in double precision.

abstract double

getY1

()

Returns the Y coordinate of the start point in double precision.

abstract double

getY2

()

Returns the Y coordinate of the end point in double precision.

boolean

intersects

​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.

boolean

intersects

​(

Rectangle2D

r)

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.

void

setCurve

​(double[] coords,
int offset)

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

abstract void

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

void

setCurve

​(

CubicCurve2D

c)

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

void

setCurve

​(

Point2D

[] pts,
int offset)

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

void

setCurve

​(

Point2D

p1,

Point2D

cp1,

Point2D

cp2,

Point2D

p2)

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

static int

solveCubic

​(double[] eqn)

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots.

static int

solveCubic

​(double[] eqn,
double[] res)

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.

static void

subdivide

​(double[] src,
int srcoff,
double[] left,
int leftoff,
double[] right,
int rightoff)

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.

void

subdivide

​(

CubicCurve2D

left,

CubicCurve2D

right)

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.

static void

subdivide

​(

CubicCurve2D

src,

CubicCurve2D

left,

CubicCurve2D

right)

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.

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

- Methods declared in interface java.awt.

Shape

getBounds2D

---

#### Method Summary

Creates a new object of the same class as this object.

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

Tests if the interior of the

Shape

entirely contains
the specified rectangular area.

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.

Returns an integer

Rectangle

that completely encloses the

Shape

.

Returns the first control point.

Returns the second control point.

Returns the X coordinate of the first control point in double precision.

Returns the X coordinate of the second control point
in double precision.

Returns the Y coordinate of the first control point in double precision.

Returns the Y coordinate of the second control point
in double precision.

Returns the flatness of this curve.

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index.

Returns the flatness of the cubic curve specified
by the indicated control points.

Returns the square of the flatness of this curve.

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index.

Returns the square of the flatness of the cubic curve specified
by the indicated control points.

Returns the start point.

Returns the end point.

Returns an iteration object that defines the boundary of the
shape.

Return an iteration object that defines the boundary of the
flattened shape.

Returns the X coordinate of the start point in double precision.

Returns the X coordinate of the end point in double precision.

Returns the Y coordinate of the start point in double precision.

Returns the Y coordinate of the end point in double precision.

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

Sets the location of the end points and control points of this curve
to the specified double coordinates.

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots.

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.

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

Methods declared in interface java.awt.

Shape

getBounds2D

---

#### Methods declared in interface java.awt. Shape

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CubicCurve2D

```java
protected CubicCurve2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** CubicCurve2D.Float

,

CubicCurve2D.Double

============ METHOD DETAIL ==========

- Method Detail

- getX1

```java
public abstract double getX1()
```

Returns the X coordinate of the start point in double precision.

**Returns:** the X coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getY1

```java
public abstract double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Returns:** the Y coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getP1

```java
public abstract
Point2D
getP1()
```

Returns the start point.

**Returns:** a

Point2D

that is the start point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX1

```java
public abstract double getCtrlX1()
```

Returns the X coordinate of the first control point in double precision.

**Returns:** the X coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY1

```java
public abstract double getCtrlY1()
```

Returns the Y coordinate of the first control point in double precision.

**Returns:** the Y coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP1

```java
public abstract
Point2D
getCtrlP1()
```

Returns the first control point.

**Returns:** a

Point2D

that is the first control point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX2

```java
public abstract double getCtrlX2()
```

Returns the X coordinate of the second control point
in double precision.

**Returns:** the X coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY2

```java
public abstract double getCtrlY2()
```

Returns the Y coordinate of the second control point
in double precision.

**Returns:** the Y coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP2

```java
public abstract
Point2D
getCtrlP2()
```

Returns the second control point.

**Returns:** a

Point2D

that is the second control point of
the

CubicCurve2D

.
**Since:** 1.2

- getX2

```java
public abstract double getX2()
```

Returns the X coordinate of the end point in double precision.

**Returns:** the X coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getY2

```java
public abstract double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Returns:** the Y coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getP2

```java
public abstract
Point2D
getP2()
```

Returns the end point.

**Returns:** a

Point2D

that is the end point of
the

CubicCurve2D

.
**Since:** 1.2

- setCurve

```java
public abstract void setCurve​(double x1,
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

- setCurve

```java
public void setCurve​(double[] coords,
int offset)
```

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

**Parameters:** coords

- a double array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
setting the end points and control points of this curve
to the coordinates contained in

coords
**Since:** 1.2

- setCurve

```java
public void setCurve​(
Point2D
p1,

Point2D
cp1,

Point2D
cp2,

Point2D
p2)
```

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

**Parameters:** p1

- the first specified

Point2D

used to set the
start point of this curve
**Parameters:** cp1

- the second specified

Point2D

used to set the
first control point of this curve
**Parameters:** cp2

- the third specified

Point2D

used to set the
second control point of this curve
**Parameters:** p2

- the fourth specified

Point2D

used to set the
end point of this curve
**Since:** 1.2

- setCurve

```java
public void setCurve​(
Point2D
[] pts,
int offset)
```

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

**Parameters:** pts

- an array of

Point2D

objects
**Parameters:** offset

- the index of

pts

from which to begin setting
the end points and control points of this curve to the
points contained in

pts
**Since:** 1.2

- setCurve

```java
public void setCurve​(
CubicCurve2D
c)
```

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

**Parameters:** c

- the specified

CubicCurve2D
**Since:** 1.2

- getFlatnessSq

```java
public static double getFlatnessSq​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Returns the square of the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
**Parameters:** y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D
**Returns:** the square of the flatness of the

CubicCurve2D

represented by the specified coordinates.
**Since:** 1.2

- getFlatness

```java
public static double getFlatness​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Returns the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
**Parameters:** y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D
**Returns:** the flatness of the

CubicCurve2D

represented by the specified coordinates.
**Since:** 1.2

- getFlatnessSq

```java
public static double getFlatnessSq​(double[] coords,
int offset)
```

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** coords

- an array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
getting the end points and control points of the curve
**Returns:** the square of the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.
**Since:** 1.2

- getFlatness

```java
public static double getFlatness​(double[] coords,
int offset)
```

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** coords

- an array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
getting the end points and control points of the curve
**Returns:** the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.
**Since:** 1.2

- getFlatnessSq

```java
public double getFlatnessSq()
```

Returns the square of the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:** the square of the flatness of this curve.
**Since:** 1.2

- getFlatness

```java
public double getFlatness()
```

Returns the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:** the flatness of this curve.
**Since:** 1.2

- subdivide

```java
public void subdivide​(
CubicCurve2D
left,

CubicCurve2D
right)
```

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.
Either or both of the left and right objects may be the same
as this object or null.

**Parameters:** left

- the cubic curve object for storing for the left or
first half of the subdivided curve
**Parameters:** right

- the cubic curve object for storing for the right or
second half of the subdivided curve
**Since:** 1.2

- subdivide

```java
public static void subdivide​(
CubicCurve2D
src,

CubicCurve2D
left,

CubicCurve2D
right)
```

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.
Either or both of the

left

and

right

objects
may be the same as the

src

object or

null

.

**Parameters:** src

- the cubic curve to be subdivided
**Parameters:** left

- the cubic curve object for storing the left or
first half of the subdivided curve
**Parameters:** right

- the cubic curve object for storing the right or
second half of the subdivided curve
**Since:** 1.2

- subdivide

```java
public static void subdivide​(double[] src,
int srcoff,
double[] left,
int leftoff,
double[] right,
int rightoff)
```

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.
Either or both of the

left

and

right

arrays may be

null

or a reference to the same array
as the

src

array.
Note that the last point in the first subdivided curve is the
same as the first point in the second subdivided curve. Thus,
it is possible to pass the same array for

left

and

right

and to use offsets, such as

rightoff

equals (

leftoff

+ 6), in order
to avoid allocating extra storage for this common point.

**Parameters:** src

- the array holding the coordinates for the source curve
**Parameters:** srcoff

- the offset into the array of the beginning of the
the 6 source coordinates
**Parameters:** left

- the array for storing the coordinates for the first
half of the subdivided curve
**Parameters:** leftoff

- the offset into the array of the beginning of the
the 6 left coordinates
**Parameters:** right

- the array for storing the coordinates for the second
half of the subdivided curve
**Parameters:** rightoff

- the offset into the array of the beginning of the
the 6 right coordinates
**Since:** 1.2

- solveCubic

```java
public static int solveCubic​(double[] eqn)
```

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots. The solved cubic is represented
by the equation:

```java
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
```

A return value of -1 is used to distinguish a constant equation
that might be always 0 or never 0 from an equation that has no
zeroes.

**Parameters:** eqn

- an array containing coefficients for a cubic
**Returns:** the number of roots, or -1 if the equation is a constant.
**Since:** 1.2

- solveCubic

```java
public static int solveCubic​(double[] eqn,
double[] res)
```

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.
The cubic solved is represented by the equation:
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
A return value of -1 is used to distinguish a constant equation,
which may be always 0 or never 0, from an equation which has no
zeroes.

**Parameters:** eqn

- the specified array of coefficients to use to solve
the cubic equation
**Parameters:** res

- the array that contains the non-complex roots
resulting from the solution of the cubic equation
**Returns:** the number of roots, or -1 if the equation is a constant
**Since:** 1.3

- contains

```java
public boolean contains​(double x,
double y)
```

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

**Specified by:** contains

in interface

Shape
**Parameters:** x

- the specified X coordinate to be tested
**Parameters:** y

- the specified Y coordinate to be tested
**Returns:** true

if the specified coordinates are inside
the

Shape

boundary;

false

otherwise.
**Since:** 1.2

- contains

```java
public boolean contains​(
Point2D
p)
```

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

**Specified by:** contains

in interface

Shape
**Parameters:** p

- the specified

Point2D

to be tested
**Returns:** true

if the specified

Point2D

is
inside the boundary of the

Shape

;

false

otherwise.
**Since:** 1.2

- intersects

```java
public boolean intersects​(double x,
double y,
double w,
double h)
```

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.
The rectangular area is considered to intersect the

Shape

if any point is contained in both the interior of the

Shape

and the specified rectangular area.

The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the rectangular area and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the rectangular area does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** intersects

in interface

Shape
**Parameters:** x

- the X coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** y

- the Y coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** w

- the width of the specified rectangular area
**Parameters:** h

- the height of the specified rectangular area
**Returns:** true

if the interior of the

Shape

and
the interior of the rectangular area intersect, or are
both highly likely to intersect and intersection calculations
would be too expensive to perform;

false

otherwise.
**Since:** 1.2
**See Also:** Area

- intersects

```java
public boolean intersects​(
Rectangle2D
r)
```

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.
The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the

Rectangle2D

and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the

Rectangle2D

does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** intersects

in interface

Shape
**Parameters:** r

- the specified

Rectangle2D
**Returns:** true

if the interior of the

Shape

and
the interior of the specified

Rectangle2D

intersect, or are both highly likely to intersect and intersection
calculations would be too expensive to perform;

false

otherwise.
**Since:** 1.2
**See Also:** Shape.intersects(double, double, double, double)

- contains

```java
public boolean contains​(double x,
double y,
double w,
double h)
```

Tests if the interior of the

Shape

entirely contains
the specified rectangular area. All coordinates that lie inside
the rectangular area must lie within the

Shape

for the
entire rectangular area to be considered contained within the

Shape

.

The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the rectangular area are
prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the rectangular area.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** contains

in interface

Shape
**Parameters:** x

- the X coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** y

- the Y coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** w

- the width of the specified rectangular area
**Parameters:** h

- the height of the specified rectangular area
**Returns:** true

if the interior of the

Shape

entirely contains the specified rectangular area;

false

otherwise or, if the

Shape

contains the rectangular area and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.
**Since:** 1.2
**See Also:** Area

,

Shape.intersects(double, double, double, double)

- contains

```java
public boolean contains​(
Rectangle2D
r)
```

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.
The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the

Rectangle2D

are prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the

Rectangle2D

.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** contains

in interface

Shape
**Parameters:** r

- The specified

Rectangle2D
**Returns:** true

if the interior of the

Shape

entirely contains the

Rectangle2D

;

false

otherwise or, if the

Shape

contains the

Rectangle2D

and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.
**Since:** 1.2
**See Also:** Shape.contains(double, double, double, double)

- getBounds

```java
public
Rectangle
getBounds()
```

Returns an integer

Rectangle

that completely encloses the

Shape

. Note that there is no guarantee that the
returned

Rectangle

is the smallest bounding box that
encloses the

Shape

, only that the

Shape

lies entirely within the indicated

Rectangle

. The
returned

Rectangle

might also fail to completely
enclose the

Shape

if the

Shape

overflows
the limited range of the integer data type. The

getBounds2D

method generally returns a
tighter bounding box due to its greater flexibility in
representation.

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

method, then
it must be inside the returned

Rectangle

bounds object
according to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(x,y)

requires

bounds.contains(x,y)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(x,y)

does not imply

shape.contains(x,y)

**Specified by:** getBounds

in interface

Shape
**Returns:** an integer

Rectangle

that completely encloses
the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds2D()

- getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at)
```

Returns an iteration object that defines the boundary of the
shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:** getPathIterator

in interface

Shape
**Parameters:** at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

, one
segment at a time.
**Since:** 1.2

- getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at,
double flatness)
```

Return an iteration object that defines the boundary of the
flattened shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:** getPathIterator

in interface

Shape
**Parameters:** at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Parameters:** flatness

- the maximum amount that the control points
for a given curve can vary from colinear before a subdivided
curve is replaced by a straight line connecting the end points
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

,
one segment at a time.
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Creates a new object of the same class as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

Constructor Detail

- CubicCurve2D

```java
protected CubicCurve2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** CubicCurve2D.Float

,

CubicCurve2D.Double

---

#### Constructor Detail

CubicCurve2D

```java
protected CubicCurve2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** CubicCurve2D.Float

,

CubicCurve2D.Double

---

#### CubicCurve2D

protected CubicCurve2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

Method Detail

- getX1

```java
public abstract double getX1()
```

Returns the X coordinate of the start point in double precision.

**Returns:** the X coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getY1

```java
public abstract double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Returns:** the Y coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

- getP1

```java
public abstract
Point2D
getP1()
```

Returns the start point.

**Returns:** a

Point2D

that is the start point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX1

```java
public abstract double getCtrlX1()
```

Returns the X coordinate of the first control point in double precision.

**Returns:** the X coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY1

```java
public abstract double getCtrlY1()
```

Returns the Y coordinate of the first control point in double precision.

**Returns:** the Y coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP1

```java
public abstract
Point2D
getCtrlP1()
```

Returns the first control point.

**Returns:** a

Point2D

that is the first control point of
the

CubicCurve2D

.
**Since:** 1.2

- getCtrlX2

```java
public abstract double getCtrlX2()
```

Returns the X coordinate of the second control point
in double precision.

**Returns:** the X coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlY2

```java
public abstract double getCtrlY2()
```

Returns the Y coordinate of the second control point
in double precision.

**Returns:** the Y coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

- getCtrlP2

```java
public abstract
Point2D
getCtrlP2()
```

Returns the second control point.

**Returns:** a

Point2D

that is the second control point of
the

CubicCurve2D

.
**Since:** 1.2

- getX2

```java
public abstract double getX2()
```

Returns the X coordinate of the end point in double precision.

**Returns:** the X coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getY2

```java
public abstract double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Returns:** the Y coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

- getP2

```java
public abstract
Point2D
getP2()
```

Returns the end point.

**Returns:** a

Point2D

that is the end point of
the

CubicCurve2D

.
**Since:** 1.2

- setCurve

```java
public abstract void setCurve​(double x1,
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

- setCurve

```java
public void setCurve​(double[] coords,
int offset)
```

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

**Parameters:** coords

- a double array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
setting the end points and control points of this curve
to the coordinates contained in

coords
**Since:** 1.2

- setCurve

```java
public void setCurve​(
Point2D
p1,

Point2D
cp1,

Point2D
cp2,

Point2D
p2)
```

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

**Parameters:** p1

- the first specified

Point2D

used to set the
start point of this curve
**Parameters:** cp1

- the second specified

Point2D

used to set the
first control point of this curve
**Parameters:** cp2

- the third specified

Point2D

used to set the
second control point of this curve
**Parameters:** p2

- the fourth specified

Point2D

used to set the
end point of this curve
**Since:** 1.2

- setCurve

```java
public void setCurve​(
Point2D
[] pts,
int offset)
```

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

**Parameters:** pts

- an array of

Point2D

objects
**Parameters:** offset

- the index of

pts

from which to begin setting
the end points and control points of this curve to the
points contained in

pts
**Since:** 1.2

- setCurve

```java
public void setCurve​(
CubicCurve2D
c)
```

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

**Parameters:** c

- the specified

CubicCurve2D
**Since:** 1.2

- getFlatnessSq

```java
public static double getFlatnessSq​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Returns the square of the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
**Parameters:** y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D
**Returns:** the square of the flatness of the

CubicCurve2D

represented by the specified coordinates.
**Since:** 1.2

- getFlatness

```java
public static double getFlatness​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Returns the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
**Parameters:** y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D
**Returns:** the flatness of the

CubicCurve2D

represented by the specified coordinates.
**Since:** 1.2

- getFlatnessSq

```java
public static double getFlatnessSq​(double[] coords,
int offset)
```

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** coords

- an array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
getting the end points and control points of the curve
**Returns:** the square of the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.
**Since:** 1.2

- getFlatness

```java
public static double getFlatness​(double[] coords,
int offset)
```

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** coords

- an array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
getting the end points and control points of the curve
**Returns:** the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.
**Since:** 1.2

- getFlatnessSq

```java
public double getFlatnessSq()
```

Returns the square of the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:** the square of the flatness of this curve.
**Since:** 1.2

- getFlatness

```java
public double getFlatness()
```

Returns the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:** the flatness of this curve.
**Since:** 1.2

- subdivide

```java
public void subdivide​(
CubicCurve2D
left,

CubicCurve2D
right)
```

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.
Either or both of the left and right objects may be the same
as this object or null.

**Parameters:** left

- the cubic curve object for storing for the left or
first half of the subdivided curve
**Parameters:** right

- the cubic curve object for storing for the right or
second half of the subdivided curve
**Since:** 1.2

- subdivide

```java
public static void subdivide​(
CubicCurve2D
src,

CubicCurve2D
left,

CubicCurve2D
right)
```

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.
Either or both of the

left

and

right

objects
may be the same as the

src

object or

null

.

**Parameters:** src

- the cubic curve to be subdivided
**Parameters:** left

- the cubic curve object for storing the left or
first half of the subdivided curve
**Parameters:** right

- the cubic curve object for storing the right or
second half of the subdivided curve
**Since:** 1.2

- subdivide

```java
public static void subdivide​(double[] src,
int srcoff,
double[] left,
int leftoff,
double[] right,
int rightoff)
```

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.
Either or both of the

left

and

right

arrays may be

null

or a reference to the same array
as the

src

array.
Note that the last point in the first subdivided curve is the
same as the first point in the second subdivided curve. Thus,
it is possible to pass the same array for

left

and

right

and to use offsets, such as

rightoff

equals (

leftoff

+ 6), in order
to avoid allocating extra storage for this common point.

**Parameters:** src

- the array holding the coordinates for the source curve
**Parameters:** srcoff

- the offset into the array of the beginning of the
the 6 source coordinates
**Parameters:** left

- the array for storing the coordinates for the first
half of the subdivided curve
**Parameters:** leftoff

- the offset into the array of the beginning of the
the 6 left coordinates
**Parameters:** right

- the array for storing the coordinates for the second
half of the subdivided curve
**Parameters:** rightoff

- the offset into the array of the beginning of the
the 6 right coordinates
**Since:** 1.2

- solveCubic

```java
public static int solveCubic​(double[] eqn)
```

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots. The solved cubic is represented
by the equation:

```java
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
```

A return value of -1 is used to distinguish a constant equation
that might be always 0 or never 0 from an equation that has no
zeroes.

**Parameters:** eqn

- an array containing coefficients for a cubic
**Returns:** the number of roots, or -1 if the equation is a constant.
**Since:** 1.2

- solveCubic

```java
public static int solveCubic​(double[] eqn,
double[] res)
```

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.
The cubic solved is represented by the equation:
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
A return value of -1 is used to distinguish a constant equation,
which may be always 0 or never 0, from an equation which has no
zeroes.

**Parameters:** eqn

- the specified array of coefficients to use to solve
the cubic equation
**Parameters:** res

- the array that contains the non-complex roots
resulting from the solution of the cubic equation
**Returns:** the number of roots, or -1 if the equation is a constant
**Since:** 1.3

- contains

```java
public boolean contains​(double x,
double y)
```

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

**Specified by:** contains

in interface

Shape
**Parameters:** x

- the specified X coordinate to be tested
**Parameters:** y

- the specified Y coordinate to be tested
**Returns:** true

if the specified coordinates are inside
the

Shape

boundary;

false

otherwise.
**Since:** 1.2

- contains

```java
public boolean contains​(
Point2D
p)
```

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

**Specified by:** contains

in interface

Shape
**Parameters:** p

- the specified

Point2D

to be tested
**Returns:** true

if the specified

Point2D

is
inside the boundary of the

Shape

;

false

otherwise.
**Since:** 1.2

- intersects

```java
public boolean intersects​(double x,
double y,
double w,
double h)
```

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.
The rectangular area is considered to intersect the

Shape

if any point is contained in both the interior of the

Shape

and the specified rectangular area.

The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the rectangular area and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the rectangular area does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** intersects

in interface

Shape
**Parameters:** x

- the X coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** y

- the Y coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** w

- the width of the specified rectangular area
**Parameters:** h

- the height of the specified rectangular area
**Returns:** true

if the interior of the

Shape

and
the interior of the rectangular area intersect, or are
both highly likely to intersect and intersection calculations
would be too expensive to perform;

false

otherwise.
**Since:** 1.2
**See Also:** Area

- intersects

```java
public boolean intersects​(
Rectangle2D
r)
```

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.
The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the

Rectangle2D

and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the

Rectangle2D

does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** intersects

in interface

Shape
**Parameters:** r

- the specified

Rectangle2D
**Returns:** true

if the interior of the

Shape

and
the interior of the specified

Rectangle2D

intersect, or are both highly likely to intersect and intersection
calculations would be too expensive to perform;

false

otherwise.
**Since:** 1.2
**See Also:** Shape.intersects(double, double, double, double)

- contains

```java
public boolean contains​(double x,
double y,
double w,
double h)
```

Tests if the interior of the

Shape

entirely contains
the specified rectangular area. All coordinates that lie inside
the rectangular area must lie within the

Shape

for the
entire rectangular area to be considered contained within the

Shape

.

The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the rectangular area are
prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the rectangular area.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** contains

in interface

Shape
**Parameters:** x

- the X coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** y

- the Y coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** w

- the width of the specified rectangular area
**Parameters:** h

- the height of the specified rectangular area
**Returns:** true

if the interior of the

Shape

entirely contains the specified rectangular area;

false

otherwise or, if the

Shape

contains the rectangular area and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.
**Since:** 1.2
**See Also:** Area

,

Shape.intersects(double, double, double, double)

- contains

```java
public boolean contains​(
Rectangle2D
r)
```

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.
The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the

Rectangle2D

are prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the

Rectangle2D

.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** contains

in interface

Shape
**Parameters:** r

- The specified

Rectangle2D
**Returns:** true

if the interior of the

Shape

entirely contains the

Rectangle2D

;

false

otherwise or, if the

Shape

contains the

Rectangle2D

and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.
**Since:** 1.2
**See Also:** Shape.contains(double, double, double, double)

- getBounds

```java
public
Rectangle
getBounds()
```

Returns an integer

Rectangle

that completely encloses the

Shape

. Note that there is no guarantee that the
returned

Rectangle

is the smallest bounding box that
encloses the

Shape

, only that the

Shape

lies entirely within the indicated

Rectangle

. The
returned

Rectangle

might also fail to completely
enclose the

Shape

if the

Shape

overflows
the limited range of the integer data type. The

getBounds2D

method generally returns a
tighter bounding box due to its greater flexibility in
representation.

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

method, then
it must be inside the returned

Rectangle

bounds object
according to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(x,y)

requires

bounds.contains(x,y)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(x,y)

does not imply

shape.contains(x,y)

**Specified by:** getBounds

in interface

Shape
**Returns:** an integer

Rectangle

that completely encloses
the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds2D()

- getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at)
```

Returns an iteration object that defines the boundary of the
shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:** getPathIterator

in interface

Shape
**Parameters:** at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

, one
segment at a time.
**Since:** 1.2

- getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at,
double flatness)
```

Return an iteration object that defines the boundary of the
flattened shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:** getPathIterator

in interface

Shape
**Parameters:** at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Parameters:** flatness

- the maximum amount that the control points
for a given curve can vary from colinear before a subdivided
curve is replaced by a straight line connecting the end points
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

,
one segment at a time.
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Creates a new object of the same class as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

---

#### Method Detail

getX1

```java
public abstract double getX1()
```

Returns the X coordinate of the start point in double precision.

**Returns:** the X coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getX1

public abstract double getX1()

Returns the X coordinate of the start point in double precision.

getY1

```java
public abstract double getY1()
```

Returns the Y coordinate of the start point in double precision.

**Returns:** the Y coordinate of the start point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getY1

public abstract double getY1()

Returns the Y coordinate of the start point in double precision.

getP1

```java
public abstract
Point2D
getP1()
```

Returns the start point.

**Returns:** a

Point2D

that is the start point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getP1

public abstract

Point2D

getP1()

Returns the start point.

getCtrlX1

```java
public abstract double getCtrlX1()
```

Returns the X coordinate of the first control point in double precision.

**Returns:** the X coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlX1

public abstract double getCtrlX1()

Returns the X coordinate of the first control point in double precision.

getCtrlY1

```java
public abstract double getCtrlY1()
```

Returns the Y coordinate of the first control point in double precision.

**Returns:** the Y coordinate of the first control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlY1

public abstract double getCtrlY1()

Returns the Y coordinate of the first control point in double precision.

getCtrlP1

```java
public abstract
Point2D
getCtrlP1()
```

Returns the first control point.

**Returns:** a

Point2D

that is the first control point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlP1

public abstract

Point2D

getCtrlP1()

Returns the first control point.

getCtrlX2

```java
public abstract double getCtrlX2()
```

Returns the X coordinate of the second control point
in double precision.

**Returns:** the X coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlX2

public abstract double getCtrlX2()

Returns the X coordinate of the second control point
in double precision.

getCtrlY2

```java
public abstract double getCtrlY2()
```

Returns the Y coordinate of the second control point
in double precision.

**Returns:** the Y coordinate of the second control point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlY2

public abstract double getCtrlY2()

Returns the Y coordinate of the second control point
in double precision.

getCtrlP2

```java
public abstract
Point2D
getCtrlP2()
```

Returns the second control point.

**Returns:** a

Point2D

that is the second control point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getCtrlP2

public abstract

Point2D

getCtrlP2()

Returns the second control point.

getX2

```java
public abstract double getX2()
```

Returns the X coordinate of the end point in double precision.

**Returns:** the X coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getX2

public abstract double getX2()

Returns the X coordinate of the end point in double precision.

getY2

```java
public abstract double getY2()
```

Returns the Y coordinate of the end point in double precision.

**Returns:** the Y coordinate of the end point of the

CubicCurve2D

.
**Since:** 1.2

---

#### getY2

public abstract double getY2()

Returns the Y coordinate of the end point in double precision.

getP2

```java
public abstract
Point2D
getP2()
```

Returns the end point.

**Returns:** a

Point2D

that is the end point of
the

CubicCurve2D

.
**Since:** 1.2

---

#### getP2

public abstract

Point2D

getP2()

Returns the end point.

setCurve

```java
public abstract void setCurve​(double x1,
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

public abstract void setCurve​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Sets the location of the end points and control points of this curve
to the specified double coordinates.

setCurve

```java
public void setCurve​(double[] coords,
int offset)
```

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

**Parameters:** coords

- a double array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
setting the end points and control points of this curve
to the coordinates contained in

coords
**Since:** 1.2

---

#### setCurve

public void setCurve​(double[] coords,
int offset)

Sets the location of the end points and control points of this curve
to the double coordinates at the specified offset in the specified
array.

setCurve

```java
public void setCurve​(
Point2D
p1,

Point2D
cp1,

Point2D
cp2,

Point2D
p2)
```

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

**Parameters:** p1

- the first specified

Point2D

used to set the
start point of this curve
**Parameters:** cp1

- the second specified

Point2D

used to set the
first control point of this curve
**Parameters:** cp2

- the third specified

Point2D

used to set the
second control point of this curve
**Parameters:** p2

- the fourth specified

Point2D

used to set the
end point of this curve
**Since:** 1.2

---

#### setCurve

public void setCurve​(

Point2D

p1,

Point2D

cp1,

Point2D

cp2,

Point2D

p2)

Sets the location of the end points and control points of this curve
to the specified

Point2D

coordinates.

setCurve

```java
public void setCurve​(
Point2D
[] pts,
int offset)
```

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

**Parameters:** pts

- an array of

Point2D

objects
**Parameters:** offset

- the index of

pts

from which to begin setting
the end points and control points of this curve to the
points contained in

pts
**Since:** 1.2

---

#### setCurve

public void setCurve​(

Point2D

[] pts,
int offset)

Sets the location of the end points and control points of this curve
to the coordinates of the

Point2D

objects at the specified
offset in the specified array.

setCurve

```java
public void setCurve​(
CubicCurve2D
c)
```

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

**Parameters:** c

- the specified

CubicCurve2D
**Since:** 1.2

---

#### setCurve

public void setCurve​(

CubicCurve2D

c)

Sets the location of the end points and control points of this curve
to the same as those in the specified

CubicCurve2D

.

getFlatnessSq

```java
public static double getFlatnessSq​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Returns the square of the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
**Parameters:** y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D
**Returns:** the square of the flatness of the

CubicCurve2D

represented by the specified coordinates.
**Since:** 1.2

---

#### getFlatnessSq

public static double getFlatnessSq​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the square of the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

getFlatness

```java
public static double getFlatness​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)
```

Returns the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** x1

- the X coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** y1

- the Y coordinate that specifies the start point
of a

CubicCurve2D
**Parameters:** ctrlx1

- the X coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrly1

- the Y coordinate that specifies the first control point
of a

CubicCurve2D
**Parameters:** ctrlx2

- the X coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** ctrly2

- the Y coordinate that specifies the second control point
of a

CubicCurve2D
**Parameters:** x2

- the X coordinate that specifies the end point
of a

CubicCurve2D
**Parameters:** y2

- the Y coordinate that specifies the end point
of a

CubicCurve2D
**Returns:** the flatness of the

CubicCurve2D

represented by the specified coordinates.
**Since:** 1.2

---

#### getFlatness

public static double getFlatness​(double x1,
double y1,
double ctrlx1,
double ctrly1,
double ctrlx2,
double ctrly2,
double x2,
double y2)

Returns the flatness of the cubic curve specified
by the indicated control points. The flatness is the maximum distance
of a control point from the line connecting the end points.

getFlatnessSq

```java
public static double getFlatnessSq​(double[] coords,
int offset)
```

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** coords

- an array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
getting the end points and control points of the curve
**Returns:** the square of the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.
**Since:** 1.2

---

#### getFlatnessSq

public static double getFlatnessSq​(double[] coords,
int offset)

Returns the square of the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

getFlatness

```java
public static double getFlatness​(double[] coords,
int offset)
```

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

**Parameters:** coords

- an array containing coordinates
**Parameters:** offset

- the index of

coords

from which to begin
getting the end points and control points of the curve
**Returns:** the flatness of the

CubicCurve2D

specified by the coordinates in

coords

at
the specified offset.
**Since:** 1.2

---

#### getFlatness

public static double getFlatness​(double[] coords,
int offset)

Returns the flatness of the cubic curve specified
by the control points stored in the indicated array at the
indicated index. The flatness is the maximum distance
of a control point from the line connecting the end points.

getFlatnessSq

```java
public double getFlatnessSq()
```

Returns the square of the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:** the square of the flatness of this curve.
**Since:** 1.2

---

#### getFlatnessSq

public double getFlatnessSq()

Returns the square of the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

getFlatness

```java
public double getFlatness()
```

Returns the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

**Returns:** the flatness of this curve.
**Since:** 1.2

---

#### getFlatness

public double getFlatness()

Returns the flatness of this curve. The flatness is the
maximum distance of a control point from the line connecting the
end points.

subdivide

```java
public void subdivide​(
CubicCurve2D
left,

CubicCurve2D
right)
```

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.
Either or both of the left and right objects may be the same
as this object or null.

**Parameters:** left

- the cubic curve object for storing for the left or
first half of the subdivided curve
**Parameters:** right

- the cubic curve object for storing for the right or
second half of the subdivided curve
**Since:** 1.2

---

#### subdivide

public void subdivide​(

CubicCurve2D

left,

CubicCurve2D

right)

Subdivides this cubic curve and stores the resulting two
subdivided curves into the left and right curve parameters.
Either or both of the left and right objects may be the same
as this object or null.

subdivide

```java
public static void subdivide​(
CubicCurve2D
src,

CubicCurve2D
left,

CubicCurve2D
right)
```

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.
Either or both of the

left

and

right

objects
may be the same as the

src

object or

null

.

**Parameters:** src

- the cubic curve to be subdivided
**Parameters:** left

- the cubic curve object for storing the left or
first half of the subdivided curve
**Parameters:** right

- the cubic curve object for storing the right or
second half of the subdivided curve
**Since:** 1.2

---

#### subdivide

public static void subdivide​(

CubicCurve2D

src,

CubicCurve2D

left,

CubicCurve2D

right)

Subdivides the cubic curve specified by the

src

parameter
and stores the resulting two subdivided curves into the

left

and

right

curve parameters.
Either or both of the

left

and

right

objects
may be the same as the

src

object or

null

.

subdivide

```java
public static void subdivide​(double[] src,
int srcoff,
double[] left,
int leftoff,
double[] right,
int rightoff)
```

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.
Either or both of the

left

and

right

arrays may be

null

or a reference to the same array
as the

src

array.
Note that the last point in the first subdivided curve is the
same as the first point in the second subdivided curve. Thus,
it is possible to pass the same array for

left

and

right

and to use offsets, such as

rightoff

equals (

leftoff

+ 6), in order
to avoid allocating extra storage for this common point.

**Parameters:** src

- the array holding the coordinates for the source curve
**Parameters:** srcoff

- the offset into the array of the beginning of the
the 6 source coordinates
**Parameters:** left

- the array for storing the coordinates for the first
half of the subdivided curve
**Parameters:** leftoff

- the offset into the array of the beginning of the
the 6 left coordinates
**Parameters:** right

- the array for storing the coordinates for the second
half of the subdivided curve
**Parameters:** rightoff

- the offset into the array of the beginning of the
the 6 right coordinates
**Since:** 1.2

---

#### subdivide

public static void subdivide​(double[] src,
int srcoff,
double[] left,
int leftoff,
double[] right,
int rightoff)

Subdivides the cubic curve specified by the coordinates
stored in the

src

array at indices

srcoff

through (

srcoff

+ 7) and stores the
resulting two subdivided curves into the two result arrays at the
corresponding indices.
Either or both of the

left

and

right

arrays may be

null

or a reference to the same array
as the

src

array.
Note that the last point in the first subdivided curve is the
same as the first point in the second subdivided curve. Thus,
it is possible to pass the same array for

left

and

right

and to use offsets, such as

rightoff

equals (

leftoff

+ 6), in order
to avoid allocating extra storage for this common point.

solveCubic

```java
public static int solveCubic​(double[] eqn)
```

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots. The solved cubic is represented
by the equation:

```java
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
```

A return value of -1 is used to distinguish a constant equation
that might be always 0 or never 0 from an equation that has no
zeroes.

**Parameters:** eqn

- an array containing coefficients for a cubic
**Returns:** the number of roots, or -1 if the equation is a constant.
**Since:** 1.2

---

#### solveCubic

public static int solveCubic​(double[] eqn)

Solves the cubic whose coefficients are in the

eqn

array and places the non-complex roots back into the same array,
returning the number of roots. The solved cubic is represented
by the equation:

```java
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
```

A return value of -1 is used to distinguish a constant equation
that might be always 0 or never 0 from an equation that has no
zeroes.

eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0

solveCubic

```java
public static int solveCubic​(double[] eqn,
double[] res)
```

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.
The cubic solved is represented by the equation:
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
A return value of -1 is used to distinguish a constant equation,
which may be always 0 or never 0, from an equation which has no
zeroes.

**Parameters:** eqn

- the specified array of coefficients to use to solve
the cubic equation
**Parameters:** res

- the array that contains the non-complex roots
resulting from the solution of the cubic equation
**Returns:** the number of roots, or -1 if the equation is a constant
**Since:** 1.3

---

#### solveCubic

public static int solveCubic​(double[] eqn,
double[] res)

Solve the cubic whose coefficients are in the

eqn

array and place the non-complex roots into the

res

array, returning the number of roots.
The cubic solved is represented by the equation:
eqn = {c, b, a, d}
dx^3 + ax^2 + bx + c = 0
A return value of -1 is used to distinguish a constant equation,
which may be always 0 or never 0, from an equation which has no
zeroes.

contains

```java
public boolean contains​(double x,
double y)
```

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

**Specified by:** contains

in interface

Shape
**Parameters:** x

- the specified X coordinate to be tested
**Parameters:** y

- the specified Y coordinate to be tested
**Returns:** true

if the specified coordinates are inside
the

Shape

boundary;

false

otherwise.
**Since:** 1.2

---

#### contains

public boolean contains​(double x,
double y)

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

contains

```java
public boolean contains​(
Point2D
p)
```

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

**Specified by:** contains

in interface

Shape
**Parameters:** p

- the specified

Point2D

to be tested
**Returns:** true

if the specified

Point2D

is
inside the boundary of the

Shape

;

false

otherwise.
**Since:** 1.2

---

#### contains

public boolean contains​(

Point2D

p)

Tests if a specified

Point2D

is inside the boundary
of the

Shape

, as described by the

definition of insideness

.

intersects

```java
public boolean intersects​(double x,
double y,
double w,
double h)
```

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.
The rectangular area is considered to intersect the

Shape

if any point is contained in both the interior of the

Shape

and the specified rectangular area.

The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the rectangular area and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the rectangular area does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** intersects

in interface

Shape
**Parameters:** x

- the X coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** y

- the Y coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** w

- the width of the specified rectangular area
**Parameters:** h

- the height of the specified rectangular area
**Returns:** true

if the interior of the

Shape

and
the interior of the rectangular area intersect, or are
both highly likely to intersect and intersection calculations
would be too expensive to perform;

false

otherwise.
**Since:** 1.2
**See Also:** Area

---

#### intersects

public boolean intersects​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.
The rectangular area is considered to intersect the

Shape

if any point is contained in both the interior of the

Shape

and the specified rectangular area.

The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the rectangular area and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the rectangular area does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the rectangular area and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the rectangular area does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

there is a high probability that the rectangular area and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

intersects

```java
public boolean intersects​(
Rectangle2D
r)
```

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.
The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the

Rectangle2D

and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the

Rectangle2D

does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** intersects

in interface

Shape
**Parameters:** r

- the specified

Rectangle2D
**Returns:** true

if the interior of the

Shape

and
the interior of the specified

Rectangle2D

intersect, or are both highly likely to intersect and intersection
calculations would be too expensive to perform;

false

otherwise.
**Since:** 1.2
**See Also:** Shape.intersects(double, double, double, double)

---

#### intersects

public boolean intersects​(

Rectangle2D

r)

Tests if the interior of the

Shape

intersects the
interior of a specified

Rectangle2D

.
The

Shape.intersects()

method allows a

Shape

implementation to conservatively return

true

when:

- there is a high probability that the

Rectangle2D

and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

This means that for some

Shapes

this method might
return

true

even though the

Rectangle2D

does not
intersect the

Shape

.
The

Area

class performs
more accurate computations of geometric intersection than most

Shape

objects and therefore can be used if a more precise
answer is required.

there is a high probability that the

Rectangle2D

and the

Shape

intersect, but

the calculations to accurately determine this intersection
are prohibitively expensive.

contains

```java
public boolean contains​(double x,
double y,
double w,
double h)
```

Tests if the interior of the

Shape

entirely contains
the specified rectangular area. All coordinates that lie inside
the rectangular area must lie within the

Shape

for the
entire rectangular area to be considered contained within the

Shape

.

The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the rectangular area are
prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the rectangular area.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** contains

in interface

Shape
**Parameters:** x

- the X coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** y

- the Y coordinate of the upper-left corner
of the specified rectangular area
**Parameters:** w

- the width of the specified rectangular area
**Parameters:** h

- the height of the specified rectangular area
**Returns:** true

if the interior of the

Shape

entirely contains the specified rectangular area;

false

otherwise or, if the

Shape

contains the rectangular area and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.
**Since:** 1.2
**See Also:** Area

,

Shape.intersects(double, double, double, double)

---

#### contains

public boolean contains​(double x,
double y,
double w,
double h)

Tests if the interior of the

Shape

entirely contains
the specified rectangular area. All coordinates that lie inside
the rectangular area must lie within the

Shape

for the
entire rectangular area to be considered contained within the

Shape

.

The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the rectangular area are
prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the rectangular area.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the rectangular area are
prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the rectangular area.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the rectangular area are
prohibitively expensive.

contains

```java
public boolean contains​(
Rectangle2D
r)
```

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.
The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the

Rectangle2D

are prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the

Rectangle2D

.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

**Specified by:** contains

in interface

Shape
**Parameters:** r

- The specified

Rectangle2D
**Returns:** true

if the interior of the

Shape

entirely contains the

Rectangle2D

;

false

otherwise or, if the

Shape

contains the

Rectangle2D

and the

intersects

method returns

true

and the containment calculations would be too expensive to
perform.
**Since:** 1.2
**See Also:** Shape.contains(double, double, double, double)

---

#### contains

public boolean contains​(

Rectangle2D

r)

Tests if the interior of the

Shape

entirely contains the
specified

Rectangle2D

.
The

Shape.contains()

method allows a

Shape

implementation to conservatively return

false

when:

- the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the

Rectangle2D

are prohibitively expensive.

This means that for some

Shapes

this method might
return

false

even though the

Shape

contains
the

Rectangle2D

.
The

Area

class performs
more accurate geometric computations than most

Shape

objects and therefore can be used if a more precise
answer is required.

the

intersect

method returns

true

and

the calculations to determine whether or not the

Shape

entirely contains the

Rectangle2D

are prohibitively expensive.

getBounds

```java
public
Rectangle
getBounds()
```

Returns an integer

Rectangle

that completely encloses the

Shape

. Note that there is no guarantee that the
returned

Rectangle

is the smallest bounding box that
encloses the

Shape

, only that the

Shape

lies entirely within the indicated

Rectangle

. The
returned

Rectangle

might also fail to completely
enclose the

Shape

if the

Shape

overflows
the limited range of the integer data type. The

getBounds2D

method generally returns a
tighter bounding box due to its greater flexibility in
representation.

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

method, then
it must be inside the returned

Rectangle

bounds object
according to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(x,y)

requires

bounds.contains(x,y)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(x,y)

does not imply

shape.contains(x,y)

**Specified by:** getBounds

in interface

Shape
**Returns:** an integer

Rectangle

that completely encloses
the

Shape

.
**Since:** 1.2
**See Also:** Shape.getBounds2D()

---

#### getBounds

public

Rectangle

getBounds()

Returns an integer

Rectangle

that completely encloses the

Shape

. Note that there is no guarantee that the
returned

Rectangle

is the smallest bounding box that
encloses the

Shape

, only that the

Shape

lies entirely within the indicated

Rectangle

. The
returned

Rectangle

might also fail to completely
enclose the

Shape

if the

Shape

overflows
the limited range of the integer data type. The

getBounds2D

method generally returns a
tighter bounding box due to its greater flexibility in
representation.

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

method, then
it must be inside the returned

Rectangle

bounds object
according to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(x,y)

requires

bounds.contains(x,y)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(x,y)

does not imply

shape.contains(x,y)

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

method, then
it must be inside the returned

Rectangle

bounds object
according to the

contains(point)

method of the

bounds

. Specifically:

shape.contains(x,y)

requires

bounds.contains(x,y)

If a

point

is not inside the

shape

, then it might
still be contained in the

bounds

object:

bounds.contains(x,y)

does not imply

shape.contains(x,y)

getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at)
```

Returns an iteration object that defines the boundary of the
shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:** getPathIterator

in interface

Shape
**Parameters:** at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

, one
segment at a time.
**Since:** 1.2

---

#### getPathIterator

public

PathIterator

getPathIterator​(

AffineTransform

at)

Returns an iteration object that defines the boundary of the
shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at,
double flatness)
```

Return an iteration object that defines the boundary of the
flattened shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

**Specified by:** getPathIterator

in interface

Shape
**Parameters:** at

- an optional

AffineTransform

to be applied to the
coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Parameters:** flatness

- the maximum amount that the control points
for a given curve can vary from colinear before a subdivided
curve is replaced by a straight line connecting the end points
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

CubicCurve2D

,
one segment at a time.
**Since:** 1.2

---

#### getPathIterator

public

PathIterator

getPathIterator​(

AffineTransform

at,
double flatness)

Return an iteration object that defines the boundary of the
flattened shape.
The iterator for this class is not multi-threaded safe,
which means that this

CubicCurve2D

class does not
guarantee that modifications to the geometry of this

CubicCurve2D

object do not affect any iterations of
that geometry that are already in process.

clone

```java
public
Object
clone()
```

Creates a new object of the same class as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a new object of the same class as this object.

---

