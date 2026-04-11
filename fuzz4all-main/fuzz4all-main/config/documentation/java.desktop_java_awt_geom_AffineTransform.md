# Class AffineTransform

**Source:** `java.desktop\java\awt\geom\AffineTransform.html`

### Class Description

```java
public class
AffineTransform

extends
Object

implements
Cloneable
,
Serializable
```

The

AffineTransform

class represents a 2D affine transform
that performs a linear mapping from 2D coordinates to other 2D
coordinates that preserves the "straightness" and
"parallelness" of lines. Affine transformations can be constructed
using sequences of translations, scales, flips, rotations, and shears.

Such a coordinate transformation can be represented by a 3 row by
3 column matrix with an implied last row of [ 0 0 1 ]. This matrix
transforms source coordinates

(x,y)

into
destination coordinates

(x',y')

by considering
them to be a column vector and multiplying the coordinate vector
by the matrix according to the following process:

```java
[ x'] [ m00 m01 m02 ] [ x ] [ m00x + m01y + m02 ]
[ y'] = [ m10 m11 m12 ] [ y ] = [ m10x + m11y + m12 ]
[ 1 ] [ 0 0 1 ] [ 1 ] [ 1 ]
```

Handling 90-Degree Rotations

In some variations of the

rotate

methods in the

AffineTransform

class, a double-precision argument
specifies the angle of rotation in radians.
These methods have special handling for rotations of approximately
90 degrees (including multiples such as 180, 270, and 360 degrees),
so that the common case of quadrant rotation is handled more
efficiently.
This special handling can cause angles very close to multiples of
90 degrees to be treated as if they were exact multiples of
90 degrees.
For small multiples of 90 degrees the range of angles treated
as a quadrant rotation is approximately 0.00000121 degrees wide.
This section explains why such special care is needed and how
it is implemented.

Since 90 degrees is represented as

PI/2

in radians,
and since PI is a transcendental (and therefore irrational) number,
it is not possible to exactly represent a multiple of 90 degrees as
an exact double precision value measured in radians.
As a result it is theoretically impossible to describe quadrant
rotations (90, 180, 270 or 360 degrees) using these values.
Double precision floating point values can get very close to
non-zero multiples of

PI/2

but never close enough
for the sine or cosine to be exactly 0.0, 1.0 or -1.0.
The implementations of

Math.sin()

and

Math.cos()

correspondingly never return 0.0
for any case other than

Math.sin(0.0)

.
These same implementations do, however, return exactly 1.0 and
-1.0 for some range of numbers around each multiple of 90
degrees since the correct answer is so close to 1.0 or -1.0 that
the double precision significand cannot represent the difference
as accurately as it can for numbers that are near 0.0.

The net result of these issues is that if the

Math.sin()

and

Math.cos()

methods
are used to directly generate the values for the matrix modifications
during these radian-based rotation operations then the resulting
transform is never strictly classifiable as a quadrant rotation
even for a simple case like

rotate(Math.PI/2.0)

,
due to minor variations in the matrix caused by the non-0.0 values
obtained for the sine and cosine.
If these transforms are not classified as quadrant rotations then
subsequent code which attempts to optimize further operations based
upon the type of the transform will be relegated to its most general
implementation.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final int TYPE_IDENTITY

This constant indicates that the transform defined by this object
is an identity transform.
An identity transform is one in which the output coordinates are
always the same as the input coordinates.
If this transform is anything other than the identity transform,
the type will either be the constant GENERAL_TRANSFORM or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**See Also:**
- TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_TRANSLATION

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.
A translation moves the coordinates by a constant amount in x
and y without changing the length or angle of vectors.

**See Also:**
- TYPE_IDENTITY

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_UNIFORM_SCALE

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.
A uniform scale multiplies the length of vectors by the same amount
in both the x and y directions without changing the angle between
vectors.
This flag bit is mutually exclusive with the TYPE_GENERAL_SCALE flag.

**See Also:**
- TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_GENERAL_SCALE

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.
A general scale multiplies the length of vectors by different
amounts in the x and y directions without changing the angle
between perpendicular vectors.
This flag bit is mutually exclusive with the TYPE_UNIFORM_SCALE flag.

**See Also:**
- TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_MASK_SCALE

This constant is a bit mask for any of the scale flag bits.

**See Also:**
- TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_FLIP

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.
A right handed coordinate system is one where the positive X
axis rotates counterclockwise to overlay the positive Y axis
similar to the direction that the fingers on your right hand
curl when you stare end on at your thumb.
A left handed coordinate system is one where the positive X
axis rotates clockwise to overlay the positive Y axis similar
to the direction that the fingers on your left hand curl.
There is no mathematical way to determine the angle of the
original flipping or mirroring transformation since all angles
of flip are identical given an appropriate adjusting rotation.

**See Also:**
- TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_QUADRANT_ROTATION

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the TYPE_GENERAL_ROTATION flag.

**See Also:**
- TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_GENERAL_ROTATION

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the
TYPE_QUADRANT_ROTATION flag.

**See Also:**
- TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_MASK_ROTATION

This constant is a bit mask for any of the rotation flag bits.

**See Also:**
- TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TYPE_GENERAL_TRANSFORM

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.
If this transform can be classified by any of the above constants,
the type will either be the constant TYPE_IDENTITY or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**See Also:**
- TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

getType()

,

Constant Field Values

**Since:**
- 1.2

---

### Constructor Details

#### public AffineTransform()

Constructs a new

AffineTransform

representing the
Identity transformation.

**Since:**
- 1.2

---

#### public AffineTransform​(
AffineTransform
Tx)

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

**Parameters:**
- Tx

- the

AffineTransform

object to copy

**Since:**
- 1.2

---

#### @ConstructorProperties
({"scaleX","shearY","shearX","scaleY","translateX","translateY"})
public AffineTransform​(float m00,
float m10,
float m01,
float m11,
float m02,
float m12)

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:**
- m00

- the X coordinate scaling element of the 3x3 matrix
- m10

- the Y coordinate shearing element of the 3x3 matrix
- m01

- the X coordinate shearing element of the 3x3 matrix
- m11

- the Y coordinate scaling element of the 3x3 matrix
- m02

- the X coordinate translation element of the 3x3 matrix
- m12

- the Y coordinate translation element of the 3x3 matrix

**Since:**
- 1.2

---

#### public AffineTransform​(float[] flatmatrix)

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:**
- flatmatrix

- the float array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.

**Since:**
- 1.2

---

#### public AffineTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:**
- m00

- the X coordinate scaling element of the 3x3 matrix
- m10

- the Y coordinate shearing element of the 3x3 matrix
- m01

- the X coordinate shearing element of the 3x3 matrix
- m11

- the Y coordinate scaling element of the 3x3 matrix
- m02

- the X coordinate translation element of the 3x3 matrix
- m12

- the Y coordinate translation element of the 3x3 matrix

**Since:**
- 1.2

---

#### public AffineTransform​(double[] flatmatrix)

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:**
- flatmatrix

- the double array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.

**Since:**
- 1.2

---

### Method Details

#### public static
AffineTransform
getTranslateInstance​(double tx,
double ty)

Returns a transform representing a translation transformation.
The matrix representing the returned transform is:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:**
- tx

- the distance by which coordinates are translated in the
X axis direction
- ty

- the distance by which coordinates are translated in the
Y axis direction

**Returns:**
- an

AffineTransform

object that represents a
translation transformation, created with the specified vector.

**Since:**
- 1.2

---

#### public static
AffineTransform
getRotateInstance​(double theta)

Returns a transform representing a rotation transformation.
The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:**
- theta

- the angle of rotation measured in radians

**Returns:**
- an

AffineTransform

object that is a rotation
transformation, created with the specified angle of rotation.

**Since:**
- 1.2

---

#### public static
AffineTransform
getRotateInstance​(double theta,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
AffineTransform Tx = new AffineTransform();
Tx.translate(anchorx, anchory); // S3: final translation
Tx.rotate(theta); // S2: rotate around anchor
Tx.translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:**
- theta

- the angle of rotation measured in radians
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Returns:**
- an

AffineTransform

object that rotates
coordinates around the specified point by the specified angle of
rotation.

**Since:**
- 1.2

---

#### public static
AffineTransform
getRotateInstance​(double vecx,
double vecy)

Returns a transform that rotates coordinates according to
a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx));
```

**Parameters:**
- vecx

- the X coordinate of the rotation vector
- vecy

- the Y coordinate of the rotation vector

**Returns:**
- an

AffineTransform

object that rotates
coordinates according to the specified rotation vector.

**Since:**
- 1.6

---

#### public static
AffineTransform
getRotateInstance​(double vecx,
double vecy,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx),
anchorx, anchory);
```

**Parameters:**
- vecx

- the X coordinate of the rotation vector
- vecy

- the Y coordinate of the rotation vector
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Returns:**
- an

AffineTransform

object that rotates
coordinates around the specified point according to the
specified rotation vector.

**Since:**
- 1.6

---

#### public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants)

Returns a transform that rotates coordinates by the specified
number of quadrants.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:**
- numquadrants

- the number of 90 degree arcs to rotate by

**Returns:**
- an

AffineTransform

object that rotates
coordinates by the specified number of quadrants.

**Since:**
- 1.6

---

#### public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants,
double anchorx,
double anchory)

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0,
anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:**
- numquadrants

- the number of 90 degree arcs to rotate by
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Returns:**
- an

AffineTransform

object that rotates
coordinates by the specified number of quadrants around the
specified anchor point.

**Since:**
- 1.6

---

#### public static
AffineTransform
getScaleInstance​(double sx,
double sy)

Returns a transform representing a scaling transformation.
The matrix representing the returned transform is:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:**
- sx

- the factor by which coordinates are scaled along the
X axis direction
- sy

- the factor by which coordinates are scaled along the
Y axis direction

**Returns:**
- an

AffineTransform

object that scales
coordinates by the specified factors.

**Since:**
- 1.2

---

#### public static
AffineTransform
getShearInstance​(double shx,
double shy)

Returns a transform representing a shearing transformation.
The matrix representing the returned transform is:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:**
- shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
- shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate

**Returns:**
- an

AffineTransform

object that shears
coordinates by the specified multipliers.

**Since:**
- 1.2

---

#### public int getType()

Retrieves the flag bits describing the conversion properties of
this transform.
The return value is either one of the constants TYPE_IDENTITY
or TYPE_GENERAL_TRANSFORM, or a combination of the
appropriate flag bits.
A valid combination of flag bits is an exclusive OR operation
that can combine
the TYPE_TRANSLATION flag bit
in addition to either of the
TYPE_UNIFORM_SCALE or TYPE_GENERAL_SCALE flag bits
as well as either of the
TYPE_QUADRANT_ROTATION or TYPE_GENERAL_ROTATION flag bits.

**Returns:**
- the OR combination of any of the indicated flags that
apply to this transform

**See Also:**
- TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

**Since:**
- 1.2

---

#### public double getDeterminant()

Returns the determinant of the matrix representation of the transform.
The determinant is useful both to determine if the transform can
be inverted and to get a single value representing the
combined X and Y scaling of the transform.

If the determinant is non-zero, then this transform is
invertible and the various methods that depend on the inverse
transform do not need to throw a

NoninvertibleTransformException

.
If the determinant is zero then this transform can not be
inverted since the transform maps all input coordinates onto
a line or a point.
If the determinant is near enough to zero then inverse transform
operations might not carry enough precision to produce meaningful
results.

If this transform represents a uniform scale, as indicated by
the

getType

method then the determinant also
represents the square of the uniform scale factor by which all of
the points are expanded from or contracted towards the origin.
If this transform represents a non-uniform scale or more general
transform then the determinant is not likely to represent a
value useful for any purpose other than determining if inverse
transforms are possible.

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

**Returns:**
- the determinant of the matrix used to transform the
coordinates.

**See Also:**
- getType()

,

createInverse()

,

inverseTransform(java.awt.geom.Point2D, java.awt.geom.Point2D)

,

TYPE_UNIFORM_SCALE

**Since:**
- 1.2

---

#### public void getMatrix​(double[] flatmatrix)

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.
The values are stored in the array as
{ m00 m10 m01 m11 m02 m12 }.
An array of 4 doubles can also be specified, in which case only the
first four elements representing the non-transform
parts of the array are retrieved and the values are stored into
the array as { m00 m10 m01 m11 }

**Parameters:**
- flatmatrix

- the double array used to store the returned
values.

**See Also:**
- getScaleX()

,

getScaleY()

,

getShearX()

,

getShearY()

,

getTranslateX()

,

getTranslateY()

**Since:**
- 1.2

---

#### public double getScaleX()

Returns the

m00

element of the 3x3 affine transformation matrix.
This matrix factor determines how input X coordinates will affect output
X coordinates and is one element of the scale of the transform.
To measure the full amount by which X coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(1, 0);
p = tx.deltaTransform(p, p);
double scaleX = p.distance(0, 0);
```

**Returns:**
- a double value that is

m00

element of the
3x3 affine transformation matrix.

**See Also:**
- getMatrix(double[])

**Since:**
- 1.2

---

#### public double getScaleY()

Returns the

m11

element of the 3x3 affine transformation matrix.
This matrix factor determines how input Y coordinates will affect output
Y coordinates and is one element of the scale of the transform.
To measure the full amount by which Y coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(0, 1);
p = tx.deltaTransform(p, p);
double scaleY = p.distance(0, 0);
```

**Returns:**
- a double value that is

m11

element of the
3x3 affine transformation matrix.

**See Also:**
- getMatrix(double[])

**Since:**
- 1.2

---

#### public double getShearX()

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

**Returns:**
- a double value that is the X coordinate of the shearing
element of the affine transformation matrix.

**See Also:**
- getMatrix(double[])

**Since:**
- 1.2

---

#### public double getShearY()

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

**Returns:**
- a double value that is the Y coordinate of the shearing
element of the affine transformation matrix.

**See Also:**
- getMatrix(double[])

**Since:**
- 1.2

---

#### public double getTranslateX()

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

**Returns:**
- a double value that is the X coordinate of the translation
element of the affine transformation matrix.

**See Also:**
- getMatrix(double[])

**Since:**
- 1.2

---

#### public double getTranslateY()

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

**Returns:**
- a double value that is the Y coordinate of the translation
element of the affine transformation matrix.

**See Also:**
- getMatrix(double[])

**Since:**
- 1.2

---

#### public void translate​(double tx,
double ty)

Concatenates this transform with a translation transformation.
This is equivalent to calling concatenate(T), where T is an

AffineTransform

represented by the following matrix:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:**
- tx

- the distance by which coordinates are translated in the
X axis direction
- ty

- the distance by which coordinates are translated in the
Y axis direction

**Since:**
- 1.2

---

#### public void rotate​(double theta)

Concatenates this transform with a rotation transformation.
This is equivalent to calling concatenate(R), where R is an

AffineTransform

represented by the following matrix:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:**
- theta

- the angle of rotation measured in radians

**Since:**
- 1.2

---

#### public void rotate​(double theta,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
translate(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:**
- theta

- the angle of rotation measured in radians
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Since:**
- 1.2

---

#### public void rotate​(double vecx,
double vecy)

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
no additional rotation is added to this transform.
This operation is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx));
```

**Parameters:**
- vecx

- the X coordinate of the rotation vector
- vecy

- the Y coordinate of the rotation vector

**Since:**
- 1.6

---

#### public void rotate​(double vecx,
double vecy,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is not modified in any way.
This method is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:**
- vecx

- the X coordinate of the rotation vector
- vecy

- the Y coordinate of the rotation vector
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Since:**
- 1.6

---

#### public void quadrantRotate​(int numquadrants)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.
This is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:**
- numquadrants

- the number of 90 degree arcs to rotate by

**Since:**
- 1.6

---

#### public void quadrantRotate​(int numquadrants,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.
This method is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:**
- numquadrants

- the number of 90 degree arcs to rotate by
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Since:**
- 1.6

---

#### public void scale​(double sx,
double sy)

Concatenates this transform with a scaling transformation.
This is equivalent to calling concatenate(S), where S is an

AffineTransform

represented by the following matrix:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:**
- sx

- the factor by which coordinates are scaled along the
X axis direction
- sy

- the factor by which coordinates are scaled along the
Y axis direction

**Since:**
- 1.2

---

#### public void shear​(double shx,
double shy)

Concatenates this transform with a shearing transformation.
This is equivalent to calling concatenate(SH), where SH is an

AffineTransform

represented by the following matrix:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:**
- shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
- shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate

**Since:**
- 1.2

---

#### public void setToIdentity()

Resets this transform to the Identity transform.

**Since:**
- 1.2

---

#### public void setToTranslation​(double tx,
double ty)

Sets this transform to a translation transformation.
The matrix representing this transform becomes:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:**
- tx

- the distance by which coordinates are translated in the
X axis direction
- ty

- the distance by which coordinates are translated in the
Y axis direction

**Since:**
- 1.2

---

#### public void setToRotation​(double theta)

Sets this transform to a rotation transformation.
The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:**
- theta

- the angle of rotation measured in radians

**Since:**
- 1.2

---

#### public void setToRotation​(double theta,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
setToTranslation(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:**
- theta

- the angle of rotation measured in radians
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Since:**
- 1.2

---

#### public void setToRotation​(double vecx,
double vecy)

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToRotation(Math.atan2(vecy, vecx));
```

**Parameters:**
- vecx

- the X coordinate of the rotation vector
- vecy

- the Y coordinate of the rotation vector

**Since:**
- 1.6

---

#### public void setToRotation​(double vecx,
double vecy,
double anchorx,
double anchory)

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToTranslation(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:**
- vecx

- the X coordinate of the rotation vector
- vecy

- the Y coordinate of the rotation vector
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Since:**
- 1.6

---

#### public void setToQuadrantRotation​(int numquadrants)

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:**
- numquadrants

- the number of 90 degree arcs to rotate by

**Since:**
- 1.6

---

#### public void setToQuadrantRotation​(int numquadrants,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:**
- numquadrants

- the number of 90 degree arcs to rotate by
- anchorx

- the X coordinate of the rotation anchor point
- anchory

- the Y coordinate of the rotation anchor point

**Since:**
- 1.6

---

#### public void setToScale​(double sx,
double sy)

Sets this transform to a scaling transformation.
The matrix representing this transform becomes:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:**
- sx

- the factor by which coordinates are scaled along the
X axis direction
- sy

- the factor by which coordinates are scaled along the
Y axis direction

**Since:**
- 1.2

---

#### public void setToShear​(double shx,
double shy)

Sets this transform to a shearing transformation.
The matrix representing this transform becomes:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:**
- shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
- shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate

**Since:**
- 1.2

---

#### public void setTransform​(
AffineTransform
Tx)

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

**Parameters:**
- Tx

- the

AffineTransform

object from which to
copy the transform

**Since:**
- 1.2

---

#### public void setTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Sets this transform to the matrix specified by the 6
double precision values.

**Parameters:**
- m00

- the X coordinate scaling element of the 3x3 matrix
- m10

- the Y coordinate shearing element of the 3x3 matrix
- m01

- the X coordinate shearing element of the 3x3 matrix
- m11

- the Y coordinate scaling element of the 3x3 matrix
- m02

- the X coordinate translation element of the 3x3 matrix
- m12

- the Y coordinate translation element of the 3x3 matrix

**Since:**
- 1.2

---

#### public void concatenate​(
AffineTransform
Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by

Tx

and then
transforming the result by the original transform Cx like this:
Cx'(p) = Cx(Tx(p))
In matrix notation, if this transform Cx is
represented by the matrix [this] and

Tx

is represented
by the matrix [Tx] then this method does the following:

```java
[this] = [this] x [Tx]
```

**Parameters:**
- Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.

**See Also:**
- preConcatenate(java.awt.geom.AffineTransform)

**Since:**
- 1.2

---

#### public void preConcatenate​(
AffineTransform
Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by the original transform
Cx and then transforming the result by

Tx

like this:
Cx'(p) = Tx(Cx(p))
In matrix notation, if this transform Cx
is represented by the matrix [this] and

Tx

is
represented by the matrix [Tx] then this method does the
following:

```java
[this] = [Tx] x [this]
```

**Parameters:**
- Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.

**See Also:**
- concatenate(java.awt.geom.AffineTransform)

**Since:**
- 1.2

---

#### public
AffineTransform
createInverse()
throws
NoninvertibleTransformException

Returns an

AffineTransform

object representing the
inverse transformation.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

createInverse

method is called.

**Returns:**
- a new

AffineTransform

object representing the
inverse transformation.

**Throws:**
- NoninvertibleTransformException

- if the matrix cannot be inverted.

**See Also:**
- getDeterminant()

**Since:**
- 1.2

---

#### public void invert()
throws
NoninvertibleTransformException

Sets this transform to the inverse of itself.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

invert

method is called.

**Throws:**
- NoninvertibleTransformException

- if the matrix cannot be inverted.

**See Also:**
- getDeterminant()

**Since:**
- 1.6

---

#### public
Point2D
transform​(
Point2D
ptSrc,

Point2D
ptDst)

Transforms the specified

ptSrc

and stores the result
in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the transformation is
stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with
the transformed point.

**Parameters:**
- ptSrc

- the specified

Point2D

to be transformed
- ptDst

- the specified

Point2D

that stores the
result of transforming

ptSrc

**Returns:**
- the

ptDst

after transforming

ptSrc

and storing the result in

ptDst

.

**Since:**
- 1.2

---

#### public void transform​(
Point2D
[] ptSrc,
int srcOff,

Point2D
[] ptDst,
int dstOff,
int numPts)

Transforms an array of point objects by this transform.
If any element of the

ptDst

array is

null

, a new

Point2D

object is allocated
and stored into that element before storing the results of the
transformation.

Note that this method does not take any precautions to
avoid problems caused by storing results into

Point2D

objects that will be used as the source for calculations
further down the source array.
This method does guarantee that if a specified

Point2D

object is both the source and destination for the same single point
transform operation then the results will not be stored until
the calculations are complete to avoid storing the results on
top of the operands.
If, however, the destination

Point2D

object for one
operation is the same object as the source

Point2D

object for another operation further down the source array then
the original coordinates in that point are overwritten before
they can be converted.

**Parameters:**
- ptSrc

- the array containing the source point objects
- ptDst

- the array into which the transform point objects are
returned
- srcOff

- the offset to the first point object to be
transformed in the source array
- dstOff

- the offset to the location of the first
transformed point object that is stored in the destination array
- numPts

- the number of point objects to be transformed

**Since:**
- 1.2

---

#### public void transform​(float[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are overwritten by a
previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:**
- srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
- dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
- srcOff

- the offset to the first point to be transformed
in the source array
- dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
- numPts

- the number of points to be transformed

**Since:**
- 1.2

---

#### public void transform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:**
- srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
- dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
- srcOff

- the offset to the first point to be transformed
in the source array
- dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
- numPts

- the number of point objects to be transformed

**Since:**
- 1.2

---

#### public void transform​(float[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:**
- srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
- dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
- srcOff

- the offset to the first point to be transformed
in the source array
- dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
- numPts

- the number of points to be transformed

**Since:**
- 1.2

---

#### public void transform​(double[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:**
- srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
- dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
- srcOff

- the offset to the first point to be transformed
in the source array
- dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
- numPts

- the number of point objects to be transformed

**Since:**
- 1.2

---

#### public
Point2D
inverseTransform​(
Point2D
ptSrc,

Point2D
ptDst)
throws
NoninvertibleTransformException

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the transformed
point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with the
transformed point.

**Parameters:**
- ptSrc

- the point to be inverse transformed
- ptDst

- the resulting transformed point

**Returns:**
- ptDst

, which contains the result of the
inverse transform.

**Throws:**
- NoninvertibleTransformException

- if the matrix cannot be
inverted.

**Since:**
- 1.2

---

#### public void inverseTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
throws
NoninvertibleTransformException

Inverse transforms an array of double precision coordinates by
this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:**
- srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
- dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
- srcOff

- the offset to the first point to be transformed
in the source array
- dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
- numPts

- the number of point objects to be transformed

**Throws:**
- NoninvertibleTransformException

- if the matrix cannot be
inverted.

**Since:**
- 1.2

---

#### public
Point2D
deltaTransform​(
Point2D
ptSrc,

Point2D
ptDst)

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same object,
the input point is correctly overwritten with the transformed
point.

**Parameters:**
- ptSrc

- the distance vector to be delta transformed
- ptDst

- the resulting transformed distance vector

**Returns:**
- ptDst

, which contains the result of the
transformation.

**Since:**
- 1.2

---

#### public void deltaTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of relative distance vectors by this
transform.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:**
- srcPts

- the array containing the source distance vectors.
Each vector is stored as a pair of relative x, y coordinates.
- dstPts

- the array into which the transformed distance vectors
are returned. Each vector is stored as a pair of relative
x, y coordinates.
- srcOff

- the offset to the first vector to be transformed
in the source array
- dstOff

- the offset to the location of the first
transformed vector that is stored in the destination array
- numPts

- the number of vector coordinate pairs to be
transformed

**Since:**
- 1.2

---

#### public
Shape
createTransformedShape​(
Shape
pSrc)

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

**Parameters:**
- pSrc

- the specified

Shape

object to be
transformed by this transform.

**Returns:**
- a new

Shape

object that defines the geometry
of the transformed

Shape

, or null if

pSrc

is null.

**Since:**
- 1.2

---

#### public
String
toString()

Returns a

String

that represents the value of this

Object

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

representing the value of this

Object

.

**Since:**
- 1.2

---

#### public boolean isIdentity()

Returns

true

if this

AffineTransform

is
an identity transform.

**Returns:**
- true

if this

AffineTransform

is
an identity transform;

false

otherwise.

**Since:**
- 1.2

---

#### public
Object
clone()

Returns a copy of this

AffineTransform

object.

**Overrides:**
- clone

in class

Object

**Returns:**
- an

Object

that is a copy of this

AffineTransform

object.

**See Also:**
- Cloneable

**Since:**
- 1.2

---

#### public int hashCode()

Returns the hashcode for this transform.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this transform.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.2

---

#### public boolean equals​(
Object
obj)

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the

Object

to test for equality with this

AffineTransform

**Returns:**
- true

if

obj

equals this

AffineTransform

object;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.2

---

### Additional Sections

#### Class AffineTransform

java.lang.Object

- java.awt.geom.AffineTransform

java.awt.geom.AffineTransform

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
AffineTransform

extends
Object

implements
Cloneable
,
Serializable
```

The

AffineTransform

class represents a 2D affine transform
that performs a linear mapping from 2D coordinates to other 2D
coordinates that preserves the "straightness" and
"parallelness" of lines. Affine transformations can be constructed
using sequences of translations, scales, flips, rotations, and shears.

Such a coordinate transformation can be represented by a 3 row by
3 column matrix with an implied last row of [ 0 0 1 ]. This matrix
transforms source coordinates

(x,y)

into
destination coordinates

(x',y')

by considering
them to be a column vector and multiplying the coordinate vector
by the matrix according to the following process:

```java
[ x'] [ m00 m01 m02 ] [ x ] [ m00x + m01y + m02 ]
[ y'] = [ m10 m11 m12 ] [ y ] = [ m10x + m11y + m12 ]
[ 1 ] [ 0 0 1 ] [ 1 ] [ 1 ]
```

Handling 90-Degree Rotations

In some variations of the

rotate

methods in the

AffineTransform

class, a double-precision argument
specifies the angle of rotation in radians.
These methods have special handling for rotations of approximately
90 degrees (including multiples such as 180, 270, and 360 degrees),
so that the common case of quadrant rotation is handled more
efficiently.
This special handling can cause angles very close to multiples of
90 degrees to be treated as if they were exact multiples of
90 degrees.
For small multiples of 90 degrees the range of angles treated
as a quadrant rotation is approximately 0.00000121 degrees wide.
This section explains why such special care is needed and how
it is implemented.

Since 90 degrees is represented as

PI/2

in radians,
and since PI is a transcendental (and therefore irrational) number,
it is not possible to exactly represent a multiple of 90 degrees as
an exact double precision value measured in radians.
As a result it is theoretically impossible to describe quadrant
rotations (90, 180, 270 or 360 degrees) using these values.
Double precision floating point values can get very close to
non-zero multiples of

PI/2

but never close enough
for the sine or cosine to be exactly 0.0, 1.0 or -1.0.
The implementations of

Math.sin()

and

Math.cos()

correspondingly never return 0.0
for any case other than

Math.sin(0.0)

.
These same implementations do, however, return exactly 1.0 and
-1.0 for some range of numbers around each multiple of 90
degrees since the correct answer is so close to 1.0 or -1.0 that
the double precision significand cannot represent the difference
as accurately as it can for numbers that are near 0.0.

The net result of these issues is that if the

Math.sin()

and

Math.cos()

methods
are used to directly generate the values for the matrix modifications
during these radian-based rotation operations then the resulting
transform is never strictly classifiable as a quadrant rotation
even for a simple case like

rotate(Math.PI/2.0)

,
due to minor variations in the matrix caused by the non-0.0 values
obtained for the sine and cosine.
If these transforms are not classified as quadrant rotations then
subsequent code which attempts to optimize further operations based
upon the type of the transform will be relegated to its most general
implementation.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

**Since:** 1.2
**See Also:** Serialized Form

public class

AffineTransform

extends

Object

implements

Cloneable

,

Serializable

The

AffineTransform

class represents a 2D affine transform
that performs a linear mapping from 2D coordinates to other 2D
coordinates that preserves the "straightness" and
"parallelness" of lines. Affine transformations can be constructed
using sequences of translations, scales, flips, rotations, and shears.

Such a coordinate transformation can be represented by a 3 row by
3 column matrix with an implied last row of [ 0 0 1 ]. This matrix
transforms source coordinates

(x,y)

into
destination coordinates

(x',y')

by considering
them to be a column vector and multiplying the coordinate vector
by the matrix according to the following process:

```java
[ x'] [ m00 m01 m02 ] [ x ] [ m00x + m01y + m02 ]
[ y'] = [ m10 m11 m12 ] [ y ] = [ m10x + m11y + m12 ]
[ 1 ] [ 0 0 1 ] [ 1 ] [ 1 ]
```

Handling 90-Degree Rotations

In some variations of the

rotate

methods in the

AffineTransform

class, a double-precision argument
specifies the angle of rotation in radians.
These methods have special handling for rotations of approximately
90 degrees (including multiples such as 180, 270, and 360 degrees),
so that the common case of quadrant rotation is handled more
efficiently.
This special handling can cause angles very close to multiples of
90 degrees to be treated as if they were exact multiples of
90 degrees.
For small multiples of 90 degrees the range of angles treated
as a quadrant rotation is approximately 0.00000121 degrees wide.
This section explains why such special care is needed and how
it is implemented.

Since 90 degrees is represented as

PI/2

in radians,
and since PI is a transcendental (and therefore irrational) number,
it is not possible to exactly represent a multiple of 90 degrees as
an exact double precision value measured in radians.
As a result it is theoretically impossible to describe quadrant
rotations (90, 180, 270 or 360 degrees) using these values.
Double precision floating point values can get very close to
non-zero multiples of

PI/2

but never close enough
for the sine or cosine to be exactly 0.0, 1.0 or -1.0.
The implementations of

Math.sin()

and

Math.cos()

correspondingly never return 0.0
for any case other than

Math.sin(0.0)

.
These same implementations do, however, return exactly 1.0 and
-1.0 for some range of numbers around each multiple of 90
degrees since the correct answer is so close to 1.0 or -1.0 that
the double precision significand cannot represent the difference
as accurately as it can for numbers that are near 0.0.

The net result of these issues is that if the

Math.sin()

and

Math.cos()

methods
are used to directly generate the values for the matrix modifications
during these radian-based rotation operations then the resulting
transform is never strictly classifiable as a quadrant rotation
even for a simple case like

rotate(Math.PI/2.0)

,
due to minor variations in the matrix caused by the non-0.0 values
obtained for the sine and cosine.
If these transforms are not classified as quadrant rotations then
subsequent code which attempts to optimize further operations based
upon the type of the transform will be relegated to its most general
implementation.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

Such a coordinate transformation can be represented by a 3 row by
3 column matrix with an implied last row of [ 0 0 1 ]. This matrix
transforms source coordinates

(x,y)

into
destination coordinates

(x',y')

by considering
them to be a column vector and multiplying the coordinate vector
by the matrix according to the following process:

```java
[ x'] [ m00 m01 m02 ] [ x ] [ m00x + m01y + m02 ]
[ y'] = [ m10 m11 m12 ] [ y ] = [ m10x + m11y + m12 ]
[ 1 ] [ 0 0 1 ] [ 1 ] [ 1 ]
```

Handling 90-Degree Rotations

In some variations of the

rotate

methods in the

AffineTransform

class, a double-precision argument
specifies the angle of rotation in radians.
These methods have special handling for rotations of approximately
90 degrees (including multiples such as 180, 270, and 360 degrees),
so that the common case of quadrant rotation is handled more
efficiently.
This special handling can cause angles very close to multiples of
90 degrees to be treated as if they were exact multiples of
90 degrees.
For small multiples of 90 degrees the range of angles treated
as a quadrant rotation is approximately 0.00000121 degrees wide.
This section explains why such special care is needed and how
it is implemented.

Since 90 degrees is represented as

PI/2

in radians,
and since PI is a transcendental (and therefore irrational) number,
it is not possible to exactly represent a multiple of 90 degrees as
an exact double precision value measured in radians.
As a result it is theoretically impossible to describe quadrant
rotations (90, 180, 270 or 360 degrees) using these values.
Double precision floating point values can get very close to
non-zero multiples of

PI/2

but never close enough
for the sine or cosine to be exactly 0.0, 1.0 or -1.0.
The implementations of

Math.sin()

and

Math.cos()

correspondingly never return 0.0
for any case other than

Math.sin(0.0)

.
These same implementations do, however, return exactly 1.0 and
-1.0 for some range of numbers around each multiple of 90
degrees since the correct answer is so close to 1.0 or -1.0 that
the double precision significand cannot represent the difference
as accurately as it can for numbers that are near 0.0.

The net result of these issues is that if the

Math.sin()

and

Math.cos()

methods
are used to directly generate the values for the matrix modifications
during these radian-based rotation operations then the resulting
transform is never strictly classifiable as a quadrant rotation
even for a simple case like

rotate(Math.PI/2.0)

,
due to minor variations in the matrix caused by the non-0.0 values
obtained for the sine and cosine.
If these transforms are not classified as quadrant rotations then
subsequent code which attempts to optimize further operations based
upon the type of the transform will be relegated to its most general
implementation.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

[ x'] [ m00 m01 m02 ] [ x ] [ m00x + m01y + m02 ]
[ y'] = [ m10 m11 m12 ] [ y ] = [ m10x + m11y + m12 ]
[ 1 ] [ 0 0 1 ] [ 1 ] [ 1 ]

---

#### Handling 90-Degree Rotations

In some variations of the

rotate

methods in the

AffineTransform

class, a double-precision argument
specifies the angle of rotation in radians.
These methods have special handling for rotations of approximately
90 degrees (including multiples such as 180, 270, and 360 degrees),
so that the common case of quadrant rotation is handled more
efficiently.
This special handling can cause angles very close to multiples of
90 degrees to be treated as if they were exact multiples of
90 degrees.
For small multiples of 90 degrees the range of angles treated
as a quadrant rotation is approximately 0.00000121 degrees wide.
This section explains why such special care is needed and how
it is implemented.

Since 90 degrees is represented as

PI/2

in radians,
and since PI is a transcendental (and therefore irrational) number,
it is not possible to exactly represent a multiple of 90 degrees as
an exact double precision value measured in radians.
As a result it is theoretically impossible to describe quadrant
rotations (90, 180, 270 or 360 degrees) using these values.
Double precision floating point values can get very close to
non-zero multiples of

PI/2

but never close enough
for the sine or cosine to be exactly 0.0, 1.0 or -1.0.
The implementations of

Math.sin()

and

Math.cos()

correspondingly never return 0.0
for any case other than

Math.sin(0.0)

.
These same implementations do, however, return exactly 1.0 and
-1.0 for some range of numbers around each multiple of 90
degrees since the correct answer is so close to 1.0 or -1.0 that
the double precision significand cannot represent the difference
as accurately as it can for numbers that are near 0.0.

The net result of these issues is that if the

Math.sin()

and

Math.cos()

methods
are used to directly generate the values for the matrix modifications
during these radian-based rotation operations then the resulting
transform is never strictly classifiable as a quadrant rotation
even for a simple case like

rotate(Math.PI/2.0)

,
due to minor variations in the matrix caused by the non-0.0 values
obtained for the sine and cosine.
If these transforms are not classified as quadrant rotations then
subsequent code which attempts to optimize further operations based
upon the type of the transform will be relegated to its most general
implementation.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

Since 90 degrees is represented as

PI/2

in radians,
and since PI is a transcendental (and therefore irrational) number,
it is not possible to exactly represent a multiple of 90 degrees as
an exact double precision value measured in radians.
As a result it is theoretically impossible to describe quadrant
rotations (90, 180, 270 or 360 degrees) using these values.
Double precision floating point values can get very close to
non-zero multiples of

PI/2

but never close enough
for the sine or cosine to be exactly 0.0, 1.0 or -1.0.
The implementations of

Math.sin()

and

Math.cos()

correspondingly never return 0.0
for any case other than

Math.sin(0.0)

.
These same implementations do, however, return exactly 1.0 and
-1.0 for some range of numbers around each multiple of 90
degrees since the correct answer is so close to 1.0 or -1.0 that
the double precision significand cannot represent the difference
as accurately as it can for numbers that are near 0.0.

The net result of these issues is that if the

Math.sin()

and

Math.cos()

methods
are used to directly generate the values for the matrix modifications
during these radian-based rotation operations then the resulting
transform is never strictly classifiable as a quadrant rotation
even for a simple case like

rotate(Math.PI/2.0)

,
due to minor variations in the matrix caused by the non-0.0 values
obtained for the sine and cosine.
If these transforms are not classified as quadrant rotations then
subsequent code which attempts to optimize further operations based
upon the type of the transform will be relegated to its most general
implementation.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

The net result of these issues is that if the

Math.sin()

and

Math.cos()

methods
are used to directly generate the values for the matrix modifications
during these radian-based rotation operations then the resulting
transform is never strictly classifiable as a quadrant rotation
even for a simple case like

rotate(Math.PI/2.0)

,
due to minor variations in the matrix caused by the non-0.0 values
obtained for the sine and cosine.
If these transforms are not classified as quadrant rotations then
subsequent code which attempts to optimize further operations based
upon the type of the transform will be relegated to its most general
implementation.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

Because quadrant rotations are fairly common,
this class should handle these cases reasonably quickly, both in
applying the rotations to the transform and in applying the resulting
transform to the coordinates.
To facilitate this optimal handling, the methods which take an angle
of rotation measured in radians attempt to detect angles that are
intended to be quadrant rotations and treat them as such.
These methods therefore treat an angle

theta

as a quadrant
rotation if either

Math.sin(

theta

)

or

Math.cos(

theta

)

returns exactly 1.0 or -1.0.
As a rule of thumb, this property holds true for a range of
approximately 0.0000000211 radians (or 0.00000121 degrees) around
small multiples of

Math.PI/2.0

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

TYPE_FLIP

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.

static int

TYPE_GENERAL_ROTATION

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.

static int

TYPE_GENERAL_SCALE

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.

static int

TYPE_GENERAL_TRANSFORM

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.

static int

TYPE_IDENTITY

This constant indicates that the transform defined by this object
is an identity transform.

static int

TYPE_MASK_ROTATION

This constant is a bit mask for any of the rotation flag bits.

static int

TYPE_MASK_SCALE

This constant is a bit mask for any of the scale flag bits.

static int

TYPE_QUADRANT_ROTATION

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.

static int

TYPE_TRANSLATION

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.

static int

TYPE_UNIFORM_SCALE

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AffineTransform

()

Constructs a new

AffineTransform

representing the
Identity transformation.

AffineTransform

​(double[] flatmatrix)

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix.

AffineTransform

​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

AffineTransform

​(float[] flatmatrix)

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix.

AffineTransform

​(float m00,
float m10,
float m01,
float m11,
float m02,
float m12)

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

AffineTransform

​(

AffineTransform

Tx)

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this

AffineTransform

object.

void

concatenate

​(

AffineTransform

Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.

AffineTransform

createInverse

()

Returns an

AffineTransform

object representing the
inverse transformation.

Shape

createTransformedShape

​(

Shape

pSrc)

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

void

deltaTransform

​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of relative distance vectors by this
transform.

Point2D

deltaTransform

​(

Point2D

ptSrc,

Point2D

ptDst)

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.

boolean

equals

​(

Object

obj)

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

double

getDeterminant

()

Returns the determinant of the matrix representation of the transform.

void

getMatrix

​(double[] flatmatrix)

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.

static

AffineTransform

getQuadrantRotateInstance

​(int numquadrants)

Returns a transform that rotates coordinates by the specified
number of quadrants.

static

AffineTransform

getQuadrantRotateInstance

​(int numquadrants,
double anchorx,
double anchory)

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.

static

AffineTransform

getRotateInstance

​(double theta)

Returns a transform representing a rotation transformation.

static

AffineTransform

getRotateInstance

​(double vecx,
double vecy)

Returns a transform that rotates coordinates according to
a rotation vector.

static

AffineTransform

getRotateInstance

​(double theta,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor point.

static

AffineTransform

getRotateInstance

​(double vecx,
double vecy,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.

static

AffineTransform

getScaleInstance

​(double sx,
double sy)

Returns a transform representing a scaling transformation.

double

getScaleX

()

Returns the

m00

element of the 3x3 affine transformation matrix.

double

getScaleY

()

Returns the

m11

element of the 3x3 affine transformation matrix.

static

AffineTransform

getShearInstance

​(double shx,
double shy)

Returns a transform representing a shearing transformation.

double

getShearX

()

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

double

getShearY

()

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

static

AffineTransform

getTranslateInstance

​(double tx,
double ty)

Returns a transform representing a translation transformation.

double

getTranslateX

()

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

double

getTranslateY

()

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

int

getType

()

Retrieves the flag bits describing the conversion properties of
this transform.

int

hashCode

()

Returns the hashcode for this transform.

void

inverseTransform

​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Inverse transforms an array of double precision coordinates by
this transform.

Point2D

inverseTransform

​(

Point2D

ptSrc,

Point2D

ptDst)

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.

void

invert

()

Sets this transform to the inverse of itself.

boolean

isIdentity

()

Returns

true

if this

AffineTransform

is
an identity transform.

void

preConcatenate

​(

AffineTransform

Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.

void

quadrantRotate

​(int numquadrants)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.

void

quadrantRotate

​(int numquadrants,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.

void

rotate

​(double theta)

Concatenates this transform with a rotation transformation.

void

rotate

​(double vecx,
double vecy)

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.

void

rotate

​(double theta,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point.

void

rotate

​(double vecx,
double vecy,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.

void

scale

​(double sx,
double sy)

Concatenates this transform with a scaling transformation.

void

setToIdentity

()

Resets this transform to the Identity transform.

void

setToQuadrantRotation

​(int numquadrants)

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.

void

setToQuadrantRotation

​(int numquadrants,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.

void

setToRotation

​(double theta)

Sets this transform to a rotation transformation.

void

setToRotation

​(double vecx,
double vecy)

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.

void

setToRotation

​(double theta,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation.

void

setToRotation

​(double vecx,
double vecy,
double anchorx,
double anchory)

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.

void

setToScale

​(double sx,
double sy)

Sets this transform to a scaling transformation.

void

setToShear

​(double shx,
double shy)

Sets this transform to a shearing transformation.

void

setToTranslation

​(double tx,
double ty)

Sets this transform to a translation transformation.

void

setTransform

​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Sets this transform to the matrix specified by the 6
double precision values.

void

setTransform

​(

AffineTransform

Tx)

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

void

shear

​(double shx,
double shy)

Concatenates this transform with a shearing transformation.

String

toString

()

Returns a

String

that represents the value of this

Object

.

void

transform

​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform.

void

transform

​(double[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.

void

transform

​(float[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.

void

transform

​(float[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform.

void

transform

​(

Point2D

[] ptSrc,
int srcOff,

Point2D

[] ptDst,
int dstOff,
int numPts)

Transforms an array of point objects by this transform.

Point2D

transform

​(

Point2D

ptSrc,

Point2D

ptDst)

Transforms the specified

ptSrc

and stores the result
in

ptDst

.

void

translate

​(double tx,
double ty)

Concatenates this transform with a translation transformation.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

TYPE_FLIP

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.

static int

TYPE_GENERAL_ROTATION

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.

static int

TYPE_GENERAL_SCALE

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.

static int

TYPE_GENERAL_TRANSFORM

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.

static int

TYPE_IDENTITY

This constant indicates that the transform defined by this object
is an identity transform.

static int

TYPE_MASK_ROTATION

This constant is a bit mask for any of the rotation flag bits.

static int

TYPE_MASK_SCALE

This constant is a bit mask for any of the scale flag bits.

static int

TYPE_QUADRANT_ROTATION

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.

static int

TYPE_TRANSLATION

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.

static int

TYPE_UNIFORM_SCALE

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.

---

#### Field Summary

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.

This constant indicates that the transform defined by this object
is an identity transform.

This constant is a bit mask for any of the rotation flag bits.

This constant is a bit mask for any of the scale flag bits.

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.

Constructor Summary

Constructors

Constructor

Description

AffineTransform

()

Constructs a new

AffineTransform

representing the
Identity transformation.

AffineTransform

​(double[] flatmatrix)

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix.

AffineTransform

​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

AffineTransform

​(float[] flatmatrix)

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix.

AffineTransform

​(float m00,
float m10,
float m01,
float m11,
float m02,
float m12)

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

AffineTransform

​(

AffineTransform

Tx)

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

---

#### Constructor Summary

Constructs a new

AffineTransform

representing the
Identity transformation.

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix.

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix.

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this

AffineTransform

object.

void

concatenate

​(

AffineTransform

Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.

AffineTransform

createInverse

()

Returns an

AffineTransform

object representing the
inverse transformation.

Shape

createTransformedShape

​(

Shape

pSrc)

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

void

deltaTransform

​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of relative distance vectors by this
transform.

Point2D

deltaTransform

​(

Point2D

ptSrc,

Point2D

ptDst)

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.

boolean

equals

​(

Object

obj)

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

double

getDeterminant

()

Returns the determinant of the matrix representation of the transform.

void

getMatrix

​(double[] flatmatrix)

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.

static

AffineTransform

getQuadrantRotateInstance

​(int numquadrants)

Returns a transform that rotates coordinates by the specified
number of quadrants.

static

AffineTransform

getQuadrantRotateInstance

​(int numquadrants,
double anchorx,
double anchory)

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.

static

AffineTransform

getRotateInstance

​(double theta)

Returns a transform representing a rotation transformation.

static

AffineTransform

getRotateInstance

​(double vecx,
double vecy)

Returns a transform that rotates coordinates according to
a rotation vector.

static

AffineTransform

getRotateInstance

​(double theta,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor point.

static

AffineTransform

getRotateInstance

​(double vecx,
double vecy,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.

static

AffineTransform

getScaleInstance

​(double sx,
double sy)

Returns a transform representing a scaling transformation.

double

getScaleX

()

Returns the

m00

element of the 3x3 affine transformation matrix.

double

getScaleY

()

Returns the

m11

element of the 3x3 affine transformation matrix.

static

AffineTransform

getShearInstance

​(double shx,
double shy)

Returns a transform representing a shearing transformation.

double

getShearX

()

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

double

getShearY

()

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

static

AffineTransform

getTranslateInstance

​(double tx,
double ty)

Returns a transform representing a translation transformation.

double

getTranslateX

()

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

double

getTranslateY

()

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

int

getType

()

Retrieves the flag bits describing the conversion properties of
this transform.

int

hashCode

()

Returns the hashcode for this transform.

void

inverseTransform

​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Inverse transforms an array of double precision coordinates by
this transform.

Point2D

inverseTransform

​(

Point2D

ptSrc,

Point2D

ptDst)

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.

void

invert

()

Sets this transform to the inverse of itself.

boolean

isIdentity

()

Returns

true

if this

AffineTransform

is
an identity transform.

void

preConcatenate

​(

AffineTransform

Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.

void

quadrantRotate

​(int numquadrants)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.

void

quadrantRotate

​(int numquadrants,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.

void

rotate

​(double theta)

Concatenates this transform with a rotation transformation.

void

rotate

​(double vecx,
double vecy)

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.

void

rotate

​(double theta,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point.

void

rotate

​(double vecx,
double vecy,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.

void

scale

​(double sx,
double sy)

Concatenates this transform with a scaling transformation.

void

setToIdentity

()

Resets this transform to the Identity transform.

void

setToQuadrantRotation

​(int numquadrants)

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.

void

setToQuadrantRotation

​(int numquadrants,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.

void

setToRotation

​(double theta)

Sets this transform to a rotation transformation.

void

setToRotation

​(double vecx,
double vecy)

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.

void

setToRotation

​(double theta,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation.

void

setToRotation

​(double vecx,
double vecy,
double anchorx,
double anchory)

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.

void

setToScale

​(double sx,
double sy)

Sets this transform to a scaling transformation.

void

setToShear

​(double shx,
double shy)

Sets this transform to a shearing transformation.

void

setToTranslation

​(double tx,
double ty)

Sets this transform to a translation transformation.

void

setTransform

​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Sets this transform to the matrix specified by the 6
double precision values.

void

setTransform

​(

AffineTransform

Tx)

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

void

shear

​(double shx,
double shy)

Concatenates this transform with a shearing transformation.

String

toString

()

Returns a

String

that represents the value of this

Object

.

void

transform

​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform.

void

transform

​(double[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.

void

transform

​(float[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.

void

transform

​(float[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform.

void

transform

​(

Point2D

[] ptSrc,
int srcOff,

Point2D

[] ptDst,
int dstOff,
int numPts)

Transforms an array of point objects by this transform.

Point2D

transform

​(

Point2D

ptSrc,

Point2D

ptDst)

Transforms the specified

ptSrc

and stores the result
in

ptDst

.

void

translate

​(double tx,
double ty)

Concatenates this transform with a translation transformation.

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

Returns a copy of this

AffineTransform

object.

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.

Returns an

AffineTransform

object representing the
inverse transformation.

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

Transforms an array of relative distance vectors by this
transform.

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

Returns the determinant of the matrix representation of the transform.

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.

Returns a transform that rotates coordinates by the specified
number of quadrants.

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.

Returns a transform representing a rotation transformation.

Returns a transform that rotates coordinates according to
a rotation vector.

Returns a transform that rotates coordinates around an anchor point.

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.

Returns a transform representing a scaling transformation.

Returns the

m00

element of the 3x3 affine transformation matrix.

Returns the

m11

element of the 3x3 affine transformation matrix.

Returns a transform representing a shearing transformation.

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

Returns a transform representing a translation transformation.

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

Retrieves the flag bits describing the conversion properties of
this transform.

Returns the hashcode for this transform.

Inverse transforms an array of double precision coordinates by
this transform.

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.

Sets this transform to the inverse of itself.

Returns

true

if this

AffineTransform

is
an identity transform.

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.

Concatenates this transform with a rotation transformation.

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.

Concatenates this transform with a transform that rotates
coordinates around an anchor point.

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.

Concatenates this transform with a scaling transformation.

Resets this transform to the Identity transform.

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.

Sets this transform to a rotation transformation.

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.

Sets this transform to a translated rotation transformation.

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.

Sets this transform to a scaling transformation.

Sets this transform to a shearing transformation.

Sets this transform to a translation transformation.

Sets this transform to the matrix specified by the 6
double precision values.

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

Concatenates this transform with a shearing transformation.

Returns a

String

that represents the value of this

Object

.

Transforms an array of double precision coordinates by this transform.

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.

Transforms an array of floating point coordinates by this transform.

Transforms an array of point objects by this transform.

Transforms the specified

ptSrc

and stores the result
in

ptDst

.

Concatenates this transform with a translation transformation.

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

- TYPE_IDENTITY

```java
public static final int TYPE_IDENTITY
```

This constant indicates that the transform defined by this object
is an identity transform.
An identity transform is one in which the output coordinates are
always the same as the input coordinates.
If this transform is anything other than the identity transform,
the type will either be the constant GENERAL_TRANSFORM or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**Since:** 1.2
**See Also:** TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_TRANSLATION

```java
public static final int TYPE_TRANSLATION
```

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.
A translation moves the coordinates by a constant amount in x
and y without changing the length or angle of vectors.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_UNIFORM_SCALE

```java
public static final int TYPE_UNIFORM_SCALE
```

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.
A uniform scale multiplies the length of vectors by the same amount
in both the x and y directions without changing the angle between
vectors.
This flag bit is mutually exclusive with the TYPE_GENERAL_SCALE flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_GENERAL_SCALE

```java
public static final int TYPE_GENERAL_SCALE
```

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.
A general scale multiplies the length of vectors by different
amounts in the x and y directions without changing the angle
between perpendicular vectors.
This flag bit is mutually exclusive with the TYPE_UNIFORM_SCALE flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_MASK_SCALE

```java
public static final int TYPE_MASK_SCALE
```

This constant is a bit mask for any of the scale flag bits.

**Since:** 1.2
**See Also:** TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

Constant Field Values

- TYPE_FLIP

```java
public static final int TYPE_FLIP
```

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.
A right handed coordinate system is one where the positive X
axis rotates counterclockwise to overlay the positive Y axis
similar to the direction that the fingers on your right hand
curl when you stare end on at your thumb.
A left handed coordinate system is one where the positive X
axis rotates clockwise to overlay the positive Y axis similar
to the direction that the fingers on your left hand curl.
There is no mathematical way to determine the angle of the
original flipping or mirroring transformation since all angles
of flip are identical given an appropriate adjusting rotation.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_QUADRANT_ROTATION

```java
public static final int TYPE_QUADRANT_ROTATION
```

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the TYPE_GENERAL_ROTATION flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_GENERAL_ROTATION

```java
public static final int TYPE_GENERAL_ROTATION
```

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the
TYPE_QUADRANT_ROTATION flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_MASK_ROTATION

```java
public static final int TYPE_MASK_ROTATION
```

This constant is a bit mask for any of the rotation flag bits.

**Since:** 1.2
**See Also:** TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

Constant Field Values

- TYPE_GENERAL_TRANSFORM

```java
public static final int TYPE_GENERAL_TRANSFORM
```

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.
If this transform can be classified by any of the above constants,
the type will either be the constant TYPE_IDENTITY or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

getType()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AffineTransform

```java
public AffineTransform()
```

Constructs a new

AffineTransform

representing the
Identity transformation.

**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(
AffineTransform
Tx)
```

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

**Parameters:** Tx

- the

AffineTransform

object to copy
**Since:** 1.2

- AffineTransform

```java
@ConstructorProperties
({"scaleX","shearY","shearX","scaleY","translateX","translateY"})
public AffineTransform​(float m00,
float m10,
float m01,
float m11,
float m02,
float m12)
```

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(float[] flatmatrix)
```

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:** flatmatrix

- the float array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.
**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)
```

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(double[] flatmatrix)
```

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:** flatmatrix

- the double array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getTranslateInstance

```java
public static
AffineTransform
getTranslateInstance​(double tx,
double ty)
```

Returns a transform representing a translation transformation.
The matrix representing the returned transform is:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Returns:** an

AffineTransform

object that represents a
translation transformation, created with the specified vector.
**Since:** 1.2

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double theta)
```

Returns a transform representing a rotation transformation.
The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Returns:** an

AffineTransform

object that is a rotation
transformation, created with the specified angle of rotation.
**Since:** 1.2

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double theta,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
AffineTransform Tx = new AffineTransform();
Tx.translate(anchorx, anchory); // S3: final translation
Tx.rotate(theta); // S2: rotate around anchor
Tx.translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates around the specified point by the specified angle of
rotation.
**Since:** 1.2

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double vecx,
double vecy)
```

Returns a transform that rotates coordinates according to
a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Returns:** an

AffineTransform

object that rotates
coordinates according to the specified rotation vector.
**Since:** 1.6

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx),
anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates around the specified point according to the
specified rotation vector.
**Since:** 1.6

- getQuadrantRotateInstance

```java
public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants)
```

Returns a transform that rotates coordinates by the specified
number of quadrants.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Returns:** an

AffineTransform

object that rotates
coordinates by the specified number of quadrants.
**Since:** 1.6

- getQuadrantRotateInstance

```java
public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0,
anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates by the specified number of quadrants around the
specified anchor point.
**Since:** 1.6

- getScaleInstance

```java
public static
AffineTransform
getScaleInstance​(double sx,
double sy)
```

Returns a transform representing a scaling transformation.
The matrix representing the returned transform is:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Returns:** an

AffineTransform

object that scales
coordinates by the specified factors.
**Since:** 1.2

- getShearInstance

```java
public static
AffineTransform
getShearInstance​(double shx,
double shy)
```

Returns a transform representing a shearing transformation.
The matrix representing the returned transform is:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Returns:** an

AffineTransform

object that shears
coordinates by the specified multipliers.
**Since:** 1.2

- getType

```java
public int getType()
```

Retrieves the flag bits describing the conversion properties of
this transform.
The return value is either one of the constants TYPE_IDENTITY
or TYPE_GENERAL_TRANSFORM, or a combination of the
appropriate flag bits.
A valid combination of flag bits is an exclusive OR operation
that can combine
the TYPE_TRANSLATION flag bit
in addition to either of the
TYPE_UNIFORM_SCALE or TYPE_GENERAL_SCALE flag bits
as well as either of the
TYPE_QUADRANT_ROTATION or TYPE_GENERAL_ROTATION flag bits.

**Returns:** the OR combination of any of the indicated flags that
apply to this transform
**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

- getDeterminant

```java
public double getDeterminant()
```

Returns the determinant of the matrix representation of the transform.
The determinant is useful both to determine if the transform can
be inverted and to get a single value representing the
combined X and Y scaling of the transform.

If the determinant is non-zero, then this transform is
invertible and the various methods that depend on the inverse
transform do not need to throw a

NoninvertibleTransformException

.
If the determinant is zero then this transform can not be
inverted since the transform maps all input coordinates onto
a line or a point.
If the determinant is near enough to zero then inverse transform
operations might not carry enough precision to produce meaningful
results.

If this transform represents a uniform scale, as indicated by
the

getType

method then the determinant also
represents the square of the uniform scale factor by which all of
the points are expanded from or contracted towards the origin.
If this transform represents a non-uniform scale or more general
transform then the determinant is not likely to represent a
value useful for any purpose other than determining if inverse
transforms are possible.

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

**Returns:** the determinant of the matrix used to transform the
coordinates.
**Since:** 1.2
**See Also:** getType()

,

createInverse()

,

inverseTransform(java.awt.geom.Point2D, java.awt.geom.Point2D)

,

TYPE_UNIFORM_SCALE

- getMatrix

```java
public void getMatrix​(double[] flatmatrix)
```

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.
The values are stored in the array as
{ m00 m10 m01 m11 m02 m12 }.
An array of 4 doubles can also be specified, in which case only the
first four elements representing the non-transform
parts of the array are retrieved and the values are stored into
the array as { m00 m10 m01 m11 }

**Parameters:** flatmatrix

- the double array used to store the returned
values.
**Since:** 1.2
**See Also:** getScaleX()

,

getScaleY()

,

getShearX()

,

getShearY()

,

getTranslateX()

,

getTranslateY()

- getScaleX

```java
public double getScaleX()
```

Returns the

m00

element of the 3x3 affine transformation matrix.
This matrix factor determines how input X coordinates will affect output
X coordinates and is one element of the scale of the transform.
To measure the full amount by which X coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(1, 0);
p = tx.deltaTransform(p, p);
double scaleX = p.distance(0, 0);
```

**Returns:** a double value that is

m00

element of the
3x3 affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getScaleY

```java
public double getScaleY()
```

Returns the

m11

element of the 3x3 affine transformation matrix.
This matrix factor determines how input Y coordinates will affect output
Y coordinates and is one element of the scale of the transform.
To measure the full amount by which Y coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(0, 1);
p = tx.deltaTransform(p, p);
double scaleY = p.distance(0, 0);
```

**Returns:** a double value that is

m11

element of the
3x3 affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getShearX

```java
public double getShearX()
```

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

**Returns:** a double value that is the X coordinate of the shearing
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getShearY

```java
public double getShearY()
```

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

**Returns:** a double value that is the Y coordinate of the shearing
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getTranslateX

```java
public double getTranslateX()
```

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

**Returns:** a double value that is the X coordinate of the translation
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getTranslateY

```java
public double getTranslateY()
```

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

**Returns:** a double value that is the Y coordinate of the translation
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- translate

```java
public void translate​(double tx,
double ty)
```

Concatenates this transform with a translation transformation.
This is equivalent to calling concatenate(T), where T is an

AffineTransform

represented by the following matrix:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Since:** 1.2

- rotate

```java
public void rotate​(double theta)
```

Concatenates this transform with a rotation transformation.
This is equivalent to calling concatenate(R), where R is an

AffineTransform

represented by the following matrix:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Since:** 1.2

- rotate

```java
public void rotate​(double theta,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
translate(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.2

- rotate

```java
public void rotate​(double vecx,
double vecy)
```

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
no additional rotation is added to this transform.
This operation is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Since:** 1.6

- rotate

```java
public void rotate​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is not modified in any way.
This method is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- quadrantRotate

```java
public void quadrantRotate​(int numquadrants)
```

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.
This is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Since:** 1.6

- quadrantRotate

```java
public void quadrantRotate​(int numquadrants,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.
This method is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- scale

```java
public void scale​(double sx,
double sy)
```

Concatenates this transform with a scaling transformation.
This is equivalent to calling concatenate(S), where S is an

AffineTransform

represented by the following matrix:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Since:** 1.2

- shear

```java
public void shear​(double shx,
double shy)
```

Concatenates this transform with a shearing transformation.
This is equivalent to calling concatenate(SH), where SH is an

AffineTransform

represented by the following matrix:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Since:** 1.2

- setToIdentity

```java
public void setToIdentity()
```

Resets this transform to the Identity transform.

**Since:** 1.2

- setToTranslation

```java
public void setToTranslation​(double tx,
double ty)
```

Sets this transform to a translation transformation.
The matrix representing this transform becomes:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Since:** 1.2

- setToRotation

```java
public void setToRotation​(double theta)
```

Sets this transform to a rotation transformation.
The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Since:** 1.2

- setToRotation

```java
public void setToRotation​(double theta,
double anchorx,
double anchory)
```

Sets this transform to a translated rotation transformation.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
setToTranslation(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.2

- setToRotation

```java
public void setToRotation​(double vecx,
double vecy)
```

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToRotation(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Since:** 1.6

- setToRotation

```java
public void setToRotation​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToTranslation(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- setToQuadrantRotation

```java
public void setToQuadrantRotation​(int numquadrants)
```

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Since:** 1.6

- setToQuadrantRotation

```java
public void setToQuadrantRotation​(int numquadrants,
double anchorx,
double anchory)
```

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- setToScale

```java
public void setToScale​(double sx,
double sy)
```

Sets this transform to a scaling transformation.
The matrix representing this transform becomes:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Since:** 1.2

- setToShear

```java
public void setToShear​(double shx,
double shy)
```

Sets this transform to a shearing transformation.
The matrix representing this transform becomes:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Since:** 1.2

- setTransform

```java
public void setTransform​(
AffineTransform
Tx)
```

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

**Parameters:** Tx

- the

AffineTransform

object from which to
copy the transform
**Since:** 1.2

- setTransform

```java
public void setTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)
```

Sets this transform to the matrix specified by the 6
double precision values.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

- concatenate

```java
public void concatenate​(
AffineTransform
Tx)
```

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by

Tx

and then
transforming the result by the original transform Cx like this:
Cx'(p) = Cx(Tx(p))
In matrix notation, if this transform Cx is
represented by the matrix [this] and

Tx

is represented
by the matrix [Tx] then this method does the following:

```java
[this] = [this] x [Tx]
```

**Parameters:** Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.
**Since:** 1.2
**See Also:** preConcatenate(java.awt.geom.AffineTransform)

- preConcatenate

```java
public void preConcatenate​(
AffineTransform
Tx)
```

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by the original transform
Cx and then transforming the result by

Tx

like this:
Cx'(p) = Tx(Cx(p))
In matrix notation, if this transform Cx
is represented by the matrix [this] and

Tx

is
represented by the matrix [Tx] then this method does the
following:

```java
[this] = [Tx] x [this]
```

**Parameters:** Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.
**Since:** 1.2
**See Also:** concatenate(java.awt.geom.AffineTransform)

- createInverse

```java
public
AffineTransform
createInverse()
throws
NoninvertibleTransformException
```

Returns an

AffineTransform

object representing the
inverse transformation.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

createInverse

method is called.

**Returns:** a new

AffineTransform

object representing the
inverse transformation.
**Throws:** NoninvertibleTransformException

- if the matrix cannot be inverted.
**Since:** 1.2
**See Also:** getDeterminant()

- invert

```java
public void invert()
throws
NoninvertibleTransformException
```

Sets this transform to the inverse of itself.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

invert

method is called.

**Throws:** NoninvertibleTransformException

- if the matrix cannot be inverted.
**Since:** 1.6
**See Also:** getDeterminant()

- transform

```java
public
Point2D
transform​(
Point2D
ptSrc,

Point2D
ptDst)
```

Transforms the specified

ptSrc

and stores the result
in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the transformation is
stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with
the transformed point.

**Parameters:** ptSrc

- the specified

Point2D

to be transformed
**Parameters:** ptDst

- the specified

Point2D

that stores the
result of transforming

ptSrc
**Returns:** the

ptDst

after transforming

ptSrc

and storing the result in

ptDst

.
**Since:** 1.2

- transform

```java
public void transform​(
Point2D
[] ptSrc,
int srcOff,

Point2D
[] ptDst,
int dstOff,
int numPts)
```

Transforms an array of point objects by this transform.
If any element of the

ptDst

array is

null

, a new

Point2D

object is allocated
and stored into that element before storing the results of the
transformation.

Note that this method does not take any precautions to
avoid problems caused by storing results into

Point2D

objects that will be used as the source for calculations
further down the source array.
This method does guarantee that if a specified

Point2D

object is both the source and destination for the same single point
transform operation then the results will not be stored until
the calculations are complete to avoid storing the results on
top of the operands.
If, however, the destination

Point2D

object for one
operation is the same object as the source

Point2D

object for another operation further down the source array then
the original coordinates in that point are overwritten before
they can be converted.

**Parameters:** ptSrc

- the array containing the source point objects
**Parameters:** ptDst

- the array into which the transform point objects are
returned
**Parameters:** srcOff

- the offset to the first point object to be
transformed in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point object that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

- transform

```java
public void transform​(float[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of floating point coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are overwritten by a
previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of points to be transformed
**Since:** 1.2

- transform

```java
public void transform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of double precision coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

- transform

```java
public void transform​(float[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of points to be transformed
**Since:** 1.2

- transform

```java
public void transform​(double[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

- inverseTransform

```java
public
Point2D
inverseTransform​(
Point2D
ptSrc,

Point2D
ptDst)
throws
NoninvertibleTransformException
```

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the transformed
point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with the
transformed point.

**Parameters:** ptSrc

- the point to be inverse transformed
**Parameters:** ptDst

- the resulting transformed point
**Returns:** ptDst

, which contains the result of the
inverse transform.
**Throws:** NoninvertibleTransformException

- if the matrix cannot be
inverted.
**Since:** 1.2

- inverseTransform

```java
public void inverseTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
throws
NoninvertibleTransformException
```

Inverse transforms an array of double precision coordinates by
this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Throws:** NoninvertibleTransformException

- if the matrix cannot be
inverted.
**Since:** 1.2

- deltaTransform

```java
public
Point2D
deltaTransform​(
Point2D
ptSrc,

Point2D
ptDst)
```

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same object,
the input point is correctly overwritten with the transformed
point.

**Parameters:** ptSrc

- the distance vector to be delta transformed
**Parameters:** ptDst

- the resulting transformed distance vector
**Returns:** ptDst

, which contains the result of the
transformation.
**Since:** 1.2

- deltaTransform

```java
public void deltaTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of relative distance vectors by this
transform.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source distance vectors.
Each vector is stored as a pair of relative x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed distance vectors
are returned. Each vector is stored as a pair of relative
x, y coordinates.
**Parameters:** srcOff

- the offset to the first vector to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed vector that is stored in the destination array
**Parameters:** numPts

- the number of vector coordinate pairs to be
transformed
**Since:** 1.2

- createTransformedShape

```java
public
Shape
createTransformedShape​(
Shape
pSrc)
```

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

**Parameters:** pSrc

- the specified

Shape

object to be
transformed by this transform.
**Returns:** a new

Shape

object that defines the geometry
of the transformed

Shape

, or null if

pSrc

is null.
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns a

String

that represents the value of this

Object

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing the value of this

Object

.
**Since:** 1.2

- isIdentity

```java
public boolean isIdentity()
```

Returns

true

if this

AffineTransform

is
an identity transform.

**Returns:** true

if this

AffineTransform

is
an identity transform;

false

otherwise.
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Returns a copy of this

AffineTransform

object.

**Overrides:** clone

in class

Object
**Returns:** an

Object

that is a copy of this

AffineTransform

object.
**Since:** 1.2
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this transform.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this transform.
**Since:** 1.2
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the

Object

to test for equality with this

AffineTransform
**Returns:** true

if

obj

equals this

AffineTransform

object;

false

otherwise.
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

Field Detail

- TYPE_IDENTITY

```java
public static final int TYPE_IDENTITY
```

This constant indicates that the transform defined by this object
is an identity transform.
An identity transform is one in which the output coordinates are
always the same as the input coordinates.
If this transform is anything other than the identity transform,
the type will either be the constant GENERAL_TRANSFORM or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**Since:** 1.2
**See Also:** TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_TRANSLATION

```java
public static final int TYPE_TRANSLATION
```

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.
A translation moves the coordinates by a constant amount in x
and y without changing the length or angle of vectors.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_UNIFORM_SCALE

```java
public static final int TYPE_UNIFORM_SCALE
```

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.
A uniform scale multiplies the length of vectors by the same amount
in both the x and y directions without changing the angle between
vectors.
This flag bit is mutually exclusive with the TYPE_GENERAL_SCALE flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_GENERAL_SCALE

```java
public static final int TYPE_GENERAL_SCALE
```

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.
A general scale multiplies the length of vectors by different
amounts in the x and y directions without changing the angle
between perpendicular vectors.
This flag bit is mutually exclusive with the TYPE_UNIFORM_SCALE flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_MASK_SCALE

```java
public static final int TYPE_MASK_SCALE
```

This constant is a bit mask for any of the scale flag bits.

**Since:** 1.2
**See Also:** TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

Constant Field Values

- TYPE_FLIP

```java
public static final int TYPE_FLIP
```

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.
A right handed coordinate system is one where the positive X
axis rotates counterclockwise to overlay the positive Y axis
similar to the direction that the fingers on your right hand
curl when you stare end on at your thumb.
A left handed coordinate system is one where the positive X
axis rotates clockwise to overlay the positive Y axis similar
to the direction that the fingers on your left hand curl.
There is no mathematical way to determine the angle of the
original flipping or mirroring transformation since all angles
of flip are identical given an appropriate adjusting rotation.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_QUADRANT_ROTATION

```java
public static final int TYPE_QUADRANT_ROTATION
```

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the TYPE_GENERAL_ROTATION flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_GENERAL_ROTATION

```java
public static final int TYPE_GENERAL_ROTATION
```

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the
TYPE_QUADRANT_ROTATION flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

- TYPE_MASK_ROTATION

```java
public static final int TYPE_MASK_ROTATION
```

This constant is a bit mask for any of the rotation flag bits.

**Since:** 1.2
**See Also:** TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

Constant Field Values

- TYPE_GENERAL_TRANSFORM

```java
public static final int TYPE_GENERAL_TRANSFORM
```

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.
If this transform can be classified by any of the above constants,
the type will either be the constant TYPE_IDENTITY or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

getType()

,

Constant Field Values

---

#### Field Detail

TYPE_IDENTITY

```java
public static final int TYPE_IDENTITY
```

This constant indicates that the transform defined by this object
is an identity transform.
An identity transform is one in which the output coordinates are
always the same as the input coordinates.
If this transform is anything other than the identity transform,
the type will either be the constant GENERAL_TRANSFORM or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**Since:** 1.2
**See Also:** TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

---

#### TYPE_IDENTITY

public static final int TYPE_IDENTITY

This constant indicates that the transform defined by this object
is an identity transform.
An identity transform is one in which the output coordinates are
always the same as the input coordinates.
If this transform is anything other than the identity transform,
the type will either be the constant GENERAL_TRANSFORM or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

TYPE_TRANSLATION

```java
public static final int TYPE_TRANSLATION
```

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.
A translation moves the coordinates by a constant amount in x
and y without changing the length or angle of vectors.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

---

#### TYPE_TRANSLATION

public static final int TYPE_TRANSLATION

This flag bit indicates that the transform defined by this object
performs a translation in addition to the conversions indicated
by other flag bits.
A translation moves the coordinates by a constant amount in x
and y without changing the length or angle of vectors.

TYPE_UNIFORM_SCALE

```java
public static final int TYPE_UNIFORM_SCALE
```

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.
A uniform scale multiplies the length of vectors by the same amount
in both the x and y directions without changing the angle between
vectors.
This flag bit is mutually exclusive with the TYPE_GENERAL_SCALE flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

---

#### TYPE_UNIFORM_SCALE

public static final int TYPE_UNIFORM_SCALE

This flag bit indicates that the transform defined by this object
performs a uniform scale in addition to the conversions indicated
by other flag bits.
A uniform scale multiplies the length of vectors by the same amount
in both the x and y directions without changing the angle between
vectors.
This flag bit is mutually exclusive with the TYPE_GENERAL_SCALE flag.

TYPE_GENERAL_SCALE

```java
public static final int TYPE_GENERAL_SCALE
```

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.
A general scale multiplies the length of vectors by different
amounts in the x and y directions without changing the angle
between perpendicular vectors.
This flag bit is mutually exclusive with the TYPE_UNIFORM_SCALE flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

---

#### TYPE_GENERAL_SCALE

public static final int TYPE_GENERAL_SCALE

This flag bit indicates that the transform defined by this object
performs a general scale in addition to the conversions indicated
by other flag bits.
A general scale multiplies the length of vectors by different
amounts in the x and y directions without changing the angle
between perpendicular vectors.
This flag bit is mutually exclusive with the TYPE_UNIFORM_SCALE flag.

TYPE_MASK_SCALE

```java
public static final int TYPE_MASK_SCALE
```

This constant is a bit mask for any of the scale flag bits.

**Since:** 1.2
**See Also:** TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

Constant Field Values

---

#### TYPE_MASK_SCALE

public static final int TYPE_MASK_SCALE

This constant is a bit mask for any of the scale flag bits.

TYPE_FLIP

```java
public static final int TYPE_FLIP
```

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.
A right handed coordinate system is one where the positive X
axis rotates counterclockwise to overlay the positive Y axis
similar to the direction that the fingers on your right hand
curl when you stare end on at your thumb.
A left handed coordinate system is one where the positive X
axis rotates clockwise to overlay the positive Y axis similar
to the direction that the fingers on your left hand curl.
There is no mathematical way to determine the angle of the
original flipping or mirroring transformation since all angles
of flip are identical given an appropriate adjusting rotation.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

---

#### TYPE_FLIP

public static final int TYPE_FLIP

This flag bit indicates that the transform defined by this object
performs a mirror image flip about some axis which changes the
normally right handed coordinate system into a left handed
system in addition to the conversions indicated by other flag bits.
A right handed coordinate system is one where the positive X
axis rotates counterclockwise to overlay the positive Y axis
similar to the direction that the fingers on your right hand
curl when you stare end on at your thumb.
A left handed coordinate system is one where the positive X
axis rotates clockwise to overlay the positive Y axis similar
to the direction that the fingers on your left hand curl.
There is no mathematical way to determine the angle of the
original flipping or mirroring transformation since all angles
of flip are identical given an appropriate adjusting rotation.

TYPE_QUADRANT_ROTATION

```java
public static final int TYPE_QUADRANT_ROTATION
```

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the TYPE_GENERAL_ROTATION flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

---

#### TYPE_QUADRANT_ROTATION

public static final int TYPE_QUADRANT_ROTATION

This flag bit indicates that the transform defined by this object
performs a quadrant rotation by some multiple of 90 degrees in
addition to the conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the TYPE_GENERAL_ROTATION flag.

TYPE_GENERAL_ROTATION

```java
public static final int TYPE_GENERAL_ROTATION
```

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the
TYPE_QUADRANT_ROTATION flag.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_TRANSFORM

,

getType()

,

Constant Field Values

---

#### TYPE_GENERAL_ROTATION

public static final int TYPE_GENERAL_ROTATION

This flag bit indicates that the transform defined by this object
performs a rotation by an arbitrary angle in addition to the
conversions indicated by other flag bits.
A rotation changes the angles of vectors by the same amount
regardless of the original direction of the vector and without
changing the length of the vector.
This flag bit is mutually exclusive with the
TYPE_QUADRANT_ROTATION flag.

TYPE_MASK_ROTATION

```java
public static final int TYPE_MASK_ROTATION
```

This constant is a bit mask for any of the rotation flag bits.

**Since:** 1.2
**See Also:** TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

Constant Field Values

---

#### TYPE_MASK_ROTATION

public static final int TYPE_MASK_ROTATION

This constant is a bit mask for any of the rotation flag bits.

TYPE_GENERAL_TRANSFORM

```java
public static final int TYPE_GENERAL_TRANSFORM
```

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.
If this transform can be classified by any of the above constants,
the type will either be the constant TYPE_IDENTITY or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_FLIP

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

getType()

,

Constant Field Values

---

#### TYPE_GENERAL_TRANSFORM

public static final int TYPE_GENERAL_TRANSFORM

This constant indicates that the transform defined by this object
performs an arbitrary conversion of the input coordinates.
If this transform can be classified by any of the above constants,
the type will either be the constant TYPE_IDENTITY or a
combination of the appropriate flag bits for the various coordinate
conversions that this transform performs.

Constructor Detail

- AffineTransform

```java
public AffineTransform()
```

Constructs a new

AffineTransform

representing the
Identity transformation.

**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(
AffineTransform
Tx)
```

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

**Parameters:** Tx

- the

AffineTransform

object to copy
**Since:** 1.2

- AffineTransform

```java
@ConstructorProperties
({"scaleX","shearY","shearX","scaleY","translateX","translateY"})
public AffineTransform​(float m00,
float m10,
float m01,
float m11,
float m02,
float m12)
```

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(float[] flatmatrix)
```

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:** flatmatrix

- the float array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.
**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)
```

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

- AffineTransform

```java
public AffineTransform​(double[] flatmatrix)
```

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:** flatmatrix

- the double array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.
**Since:** 1.2

---

#### Constructor Detail

AffineTransform

```java
public AffineTransform()
```

Constructs a new

AffineTransform

representing the
Identity transformation.

**Since:** 1.2

---

#### AffineTransform

public AffineTransform()

Constructs a new

AffineTransform

representing the
Identity transformation.

AffineTransform

```java
public AffineTransform​(
AffineTransform
Tx)
```

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

**Parameters:** Tx

- the

AffineTransform

object to copy
**Since:** 1.2

---

#### AffineTransform

public AffineTransform​(

AffineTransform

Tx)

Constructs a new

AffineTransform

that is a copy of
the specified

AffineTransform

object.

AffineTransform

```java
@ConstructorProperties
({"scaleX","shearY","shearX","scaleY","translateX","translateY"})
public AffineTransform​(float m00,
float m10,
float m01,
float m11,
float m02,
float m12)
```

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

---

#### AffineTransform

@ConstructorProperties

({"scaleX","shearY","shearX","scaleY","translateX","translateY"})
public AffineTransform​(float m00,
float m10,
float m01,
float m11,
float m02,
float m12)

Constructs a new

AffineTransform

from 6 floating point
values representing the 6 specifiable entries of the 3x3
transformation matrix.

AffineTransform

```java
public AffineTransform​(float[] flatmatrix)
```

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:** flatmatrix

- the float array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.
**Since:** 1.2

---

#### AffineTransform

public AffineTransform​(float[] flatmatrix)

Constructs a new

AffineTransform

from an array of
floating point values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

AffineTransform

```java
public AffineTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)
```

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

---

#### AffineTransform

public AffineTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Constructs a new

AffineTransform

from 6 double
precision values representing the 6 specifiable entries of the 3x3
transformation matrix.

AffineTransform

```java
public AffineTransform​(double[] flatmatrix)
```

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

**Parameters:** flatmatrix

- the double array containing the values to be set
in the new

AffineTransform

object. The length of the
array is assumed to be at least 4. If the length of the array is
less than 6, only the first 4 values are taken. If the length of
the array is greater than 6, the first 6 values are taken.
**Since:** 1.2

---

#### AffineTransform

public AffineTransform​(double[] flatmatrix)

Constructs a new

AffineTransform

from an array of
double precision values representing either the 4 non-translation
entries or the 6 specifiable entries of the 3x3 transformation
matrix. The values are retrieved from the array as
{ m00 m10 m01 m11 [m02 m12]}.

Method Detail

- getTranslateInstance

```java
public static
AffineTransform
getTranslateInstance​(double tx,
double ty)
```

Returns a transform representing a translation transformation.
The matrix representing the returned transform is:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Returns:** an

AffineTransform

object that represents a
translation transformation, created with the specified vector.
**Since:** 1.2

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double theta)
```

Returns a transform representing a rotation transformation.
The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Returns:** an

AffineTransform

object that is a rotation
transformation, created with the specified angle of rotation.
**Since:** 1.2

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double theta,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
AffineTransform Tx = new AffineTransform();
Tx.translate(anchorx, anchory); // S3: final translation
Tx.rotate(theta); // S2: rotate around anchor
Tx.translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates around the specified point by the specified angle of
rotation.
**Since:** 1.2

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double vecx,
double vecy)
```

Returns a transform that rotates coordinates according to
a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Returns:** an

AffineTransform

object that rotates
coordinates according to the specified rotation vector.
**Since:** 1.6

- getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx),
anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates around the specified point according to the
specified rotation vector.
**Since:** 1.6

- getQuadrantRotateInstance

```java
public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants)
```

Returns a transform that rotates coordinates by the specified
number of quadrants.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Returns:** an

AffineTransform

object that rotates
coordinates by the specified number of quadrants.
**Since:** 1.6

- getQuadrantRotateInstance

```java
public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0,
anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates by the specified number of quadrants around the
specified anchor point.
**Since:** 1.6

- getScaleInstance

```java
public static
AffineTransform
getScaleInstance​(double sx,
double sy)
```

Returns a transform representing a scaling transformation.
The matrix representing the returned transform is:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Returns:** an

AffineTransform

object that scales
coordinates by the specified factors.
**Since:** 1.2

- getShearInstance

```java
public static
AffineTransform
getShearInstance​(double shx,
double shy)
```

Returns a transform representing a shearing transformation.
The matrix representing the returned transform is:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Returns:** an

AffineTransform

object that shears
coordinates by the specified multipliers.
**Since:** 1.2

- getType

```java
public int getType()
```

Retrieves the flag bits describing the conversion properties of
this transform.
The return value is either one of the constants TYPE_IDENTITY
or TYPE_GENERAL_TRANSFORM, or a combination of the
appropriate flag bits.
A valid combination of flag bits is an exclusive OR operation
that can combine
the TYPE_TRANSLATION flag bit
in addition to either of the
TYPE_UNIFORM_SCALE or TYPE_GENERAL_SCALE flag bits
as well as either of the
TYPE_QUADRANT_ROTATION or TYPE_GENERAL_ROTATION flag bits.

**Returns:** the OR combination of any of the indicated flags that
apply to this transform
**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

- getDeterminant

```java
public double getDeterminant()
```

Returns the determinant of the matrix representation of the transform.
The determinant is useful both to determine if the transform can
be inverted and to get a single value representing the
combined X and Y scaling of the transform.

If the determinant is non-zero, then this transform is
invertible and the various methods that depend on the inverse
transform do not need to throw a

NoninvertibleTransformException

.
If the determinant is zero then this transform can not be
inverted since the transform maps all input coordinates onto
a line or a point.
If the determinant is near enough to zero then inverse transform
operations might not carry enough precision to produce meaningful
results.

If this transform represents a uniform scale, as indicated by
the

getType

method then the determinant also
represents the square of the uniform scale factor by which all of
the points are expanded from or contracted towards the origin.
If this transform represents a non-uniform scale or more general
transform then the determinant is not likely to represent a
value useful for any purpose other than determining if inverse
transforms are possible.

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

**Returns:** the determinant of the matrix used to transform the
coordinates.
**Since:** 1.2
**See Also:** getType()

,

createInverse()

,

inverseTransform(java.awt.geom.Point2D, java.awt.geom.Point2D)

,

TYPE_UNIFORM_SCALE

- getMatrix

```java
public void getMatrix​(double[] flatmatrix)
```

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.
The values are stored in the array as
{ m00 m10 m01 m11 m02 m12 }.
An array of 4 doubles can also be specified, in which case only the
first four elements representing the non-transform
parts of the array are retrieved and the values are stored into
the array as { m00 m10 m01 m11 }

**Parameters:** flatmatrix

- the double array used to store the returned
values.
**Since:** 1.2
**See Also:** getScaleX()

,

getScaleY()

,

getShearX()

,

getShearY()

,

getTranslateX()

,

getTranslateY()

- getScaleX

```java
public double getScaleX()
```

Returns the

m00

element of the 3x3 affine transformation matrix.
This matrix factor determines how input X coordinates will affect output
X coordinates and is one element of the scale of the transform.
To measure the full amount by which X coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(1, 0);
p = tx.deltaTransform(p, p);
double scaleX = p.distance(0, 0);
```

**Returns:** a double value that is

m00

element of the
3x3 affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getScaleY

```java
public double getScaleY()
```

Returns the

m11

element of the 3x3 affine transformation matrix.
This matrix factor determines how input Y coordinates will affect output
Y coordinates and is one element of the scale of the transform.
To measure the full amount by which Y coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(0, 1);
p = tx.deltaTransform(p, p);
double scaleY = p.distance(0, 0);
```

**Returns:** a double value that is

m11

element of the
3x3 affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getShearX

```java
public double getShearX()
```

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

**Returns:** a double value that is the X coordinate of the shearing
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getShearY

```java
public double getShearY()
```

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

**Returns:** a double value that is the Y coordinate of the shearing
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getTranslateX

```java
public double getTranslateX()
```

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

**Returns:** a double value that is the X coordinate of the translation
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- getTranslateY

```java
public double getTranslateY()
```

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

**Returns:** a double value that is the Y coordinate of the translation
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

- translate

```java
public void translate​(double tx,
double ty)
```

Concatenates this transform with a translation transformation.
This is equivalent to calling concatenate(T), where T is an

AffineTransform

represented by the following matrix:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Since:** 1.2

- rotate

```java
public void rotate​(double theta)
```

Concatenates this transform with a rotation transformation.
This is equivalent to calling concatenate(R), where R is an

AffineTransform

represented by the following matrix:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Since:** 1.2

- rotate

```java
public void rotate​(double theta,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
translate(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.2

- rotate

```java
public void rotate​(double vecx,
double vecy)
```

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
no additional rotation is added to this transform.
This operation is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Since:** 1.6

- rotate

```java
public void rotate​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is not modified in any way.
This method is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- quadrantRotate

```java
public void quadrantRotate​(int numquadrants)
```

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.
This is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Since:** 1.6

- quadrantRotate

```java
public void quadrantRotate​(int numquadrants,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.
This method is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- scale

```java
public void scale​(double sx,
double sy)
```

Concatenates this transform with a scaling transformation.
This is equivalent to calling concatenate(S), where S is an

AffineTransform

represented by the following matrix:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Since:** 1.2

- shear

```java
public void shear​(double shx,
double shy)
```

Concatenates this transform with a shearing transformation.
This is equivalent to calling concatenate(SH), where SH is an

AffineTransform

represented by the following matrix:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Since:** 1.2

- setToIdentity

```java
public void setToIdentity()
```

Resets this transform to the Identity transform.

**Since:** 1.2

- setToTranslation

```java
public void setToTranslation​(double tx,
double ty)
```

Sets this transform to a translation transformation.
The matrix representing this transform becomes:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Since:** 1.2

- setToRotation

```java
public void setToRotation​(double theta)
```

Sets this transform to a rotation transformation.
The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Since:** 1.2

- setToRotation

```java
public void setToRotation​(double theta,
double anchorx,
double anchory)
```

Sets this transform to a translated rotation transformation.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
setToTranslation(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.2

- setToRotation

```java
public void setToRotation​(double vecx,
double vecy)
```

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToRotation(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Since:** 1.6

- setToRotation

```java
public void setToRotation​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToTranslation(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- setToQuadrantRotation

```java
public void setToQuadrantRotation​(int numquadrants)
```

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Since:** 1.6

- setToQuadrantRotation

```java
public void setToQuadrantRotation​(int numquadrants,
double anchorx,
double anchory)
```

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

- setToScale

```java
public void setToScale​(double sx,
double sy)
```

Sets this transform to a scaling transformation.
The matrix representing this transform becomes:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Since:** 1.2

- setToShear

```java
public void setToShear​(double shx,
double shy)
```

Sets this transform to a shearing transformation.
The matrix representing this transform becomes:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Since:** 1.2

- setTransform

```java
public void setTransform​(
AffineTransform
Tx)
```

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

**Parameters:** Tx

- the

AffineTransform

object from which to
copy the transform
**Since:** 1.2

- setTransform

```java
public void setTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)
```

Sets this transform to the matrix specified by the 6
double precision values.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

- concatenate

```java
public void concatenate​(
AffineTransform
Tx)
```

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by

Tx

and then
transforming the result by the original transform Cx like this:
Cx'(p) = Cx(Tx(p))
In matrix notation, if this transform Cx is
represented by the matrix [this] and

Tx

is represented
by the matrix [Tx] then this method does the following:

```java
[this] = [this] x [Tx]
```

**Parameters:** Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.
**Since:** 1.2
**See Also:** preConcatenate(java.awt.geom.AffineTransform)

- preConcatenate

```java
public void preConcatenate​(
AffineTransform
Tx)
```

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by the original transform
Cx and then transforming the result by

Tx

like this:
Cx'(p) = Tx(Cx(p))
In matrix notation, if this transform Cx
is represented by the matrix [this] and

Tx

is
represented by the matrix [Tx] then this method does the
following:

```java
[this] = [Tx] x [this]
```

**Parameters:** Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.
**Since:** 1.2
**See Also:** concatenate(java.awt.geom.AffineTransform)

- createInverse

```java
public
AffineTransform
createInverse()
throws
NoninvertibleTransformException
```

Returns an

AffineTransform

object representing the
inverse transformation.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

createInverse

method is called.

**Returns:** a new

AffineTransform

object representing the
inverse transformation.
**Throws:** NoninvertibleTransformException

- if the matrix cannot be inverted.
**Since:** 1.2
**See Also:** getDeterminant()

- invert

```java
public void invert()
throws
NoninvertibleTransformException
```

Sets this transform to the inverse of itself.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

invert

method is called.

**Throws:** NoninvertibleTransformException

- if the matrix cannot be inverted.
**Since:** 1.6
**See Also:** getDeterminant()

- transform

```java
public
Point2D
transform​(
Point2D
ptSrc,

Point2D
ptDst)
```

Transforms the specified

ptSrc

and stores the result
in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the transformation is
stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with
the transformed point.

**Parameters:** ptSrc

- the specified

Point2D

to be transformed
**Parameters:** ptDst

- the specified

Point2D

that stores the
result of transforming

ptSrc
**Returns:** the

ptDst

after transforming

ptSrc

and storing the result in

ptDst

.
**Since:** 1.2

- transform

```java
public void transform​(
Point2D
[] ptSrc,
int srcOff,

Point2D
[] ptDst,
int dstOff,
int numPts)
```

Transforms an array of point objects by this transform.
If any element of the

ptDst

array is

null

, a new

Point2D

object is allocated
and stored into that element before storing the results of the
transformation.

Note that this method does not take any precautions to
avoid problems caused by storing results into

Point2D

objects that will be used as the source for calculations
further down the source array.
This method does guarantee that if a specified

Point2D

object is both the source and destination for the same single point
transform operation then the results will not be stored until
the calculations are complete to avoid storing the results on
top of the operands.
If, however, the destination

Point2D

object for one
operation is the same object as the source

Point2D

object for another operation further down the source array then
the original coordinates in that point are overwritten before
they can be converted.

**Parameters:** ptSrc

- the array containing the source point objects
**Parameters:** ptDst

- the array into which the transform point objects are
returned
**Parameters:** srcOff

- the offset to the first point object to be
transformed in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point object that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

- transform

```java
public void transform​(float[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of floating point coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are overwritten by a
previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of points to be transformed
**Since:** 1.2

- transform

```java
public void transform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of double precision coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

- transform

```java
public void transform​(float[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of points to be transformed
**Since:** 1.2

- transform

```java
public void transform​(double[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

- inverseTransform

```java
public
Point2D
inverseTransform​(
Point2D
ptSrc,

Point2D
ptDst)
throws
NoninvertibleTransformException
```

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the transformed
point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with the
transformed point.

**Parameters:** ptSrc

- the point to be inverse transformed
**Parameters:** ptDst

- the resulting transformed point
**Returns:** ptDst

, which contains the result of the
inverse transform.
**Throws:** NoninvertibleTransformException

- if the matrix cannot be
inverted.
**Since:** 1.2

- inverseTransform

```java
public void inverseTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
throws
NoninvertibleTransformException
```

Inverse transforms an array of double precision coordinates by
this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Throws:** NoninvertibleTransformException

- if the matrix cannot be
inverted.
**Since:** 1.2

- deltaTransform

```java
public
Point2D
deltaTransform​(
Point2D
ptSrc,

Point2D
ptDst)
```

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same object,
the input point is correctly overwritten with the transformed
point.

**Parameters:** ptSrc

- the distance vector to be delta transformed
**Parameters:** ptDst

- the resulting transformed distance vector
**Returns:** ptDst

, which contains the result of the
transformation.
**Since:** 1.2

- deltaTransform

```java
public void deltaTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of relative distance vectors by this
transform.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source distance vectors.
Each vector is stored as a pair of relative x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed distance vectors
are returned. Each vector is stored as a pair of relative
x, y coordinates.
**Parameters:** srcOff

- the offset to the first vector to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed vector that is stored in the destination array
**Parameters:** numPts

- the number of vector coordinate pairs to be
transformed
**Since:** 1.2

- createTransformedShape

```java
public
Shape
createTransformedShape​(
Shape
pSrc)
```

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

**Parameters:** pSrc

- the specified

Shape

object to be
transformed by this transform.
**Returns:** a new

Shape

object that defines the geometry
of the transformed

Shape

, or null if

pSrc

is null.
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns a

String

that represents the value of this

Object

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing the value of this

Object

.
**Since:** 1.2

- isIdentity

```java
public boolean isIdentity()
```

Returns

true

if this

AffineTransform

is
an identity transform.

**Returns:** true

if this

AffineTransform

is
an identity transform;

false

otherwise.
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Returns a copy of this

AffineTransform

object.

**Overrides:** clone

in class

Object
**Returns:** an

Object

that is a copy of this

AffineTransform

object.
**Since:** 1.2
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this transform.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this transform.
**Since:** 1.2
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the

Object

to test for equality with this

AffineTransform
**Returns:** true

if

obj

equals this

AffineTransform

object;

false

otherwise.
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getTranslateInstance

```java
public static
AffineTransform
getTranslateInstance​(double tx,
double ty)
```

Returns a transform representing a translation transformation.
The matrix representing the returned transform is:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Returns:** an

AffineTransform

object that represents a
translation transformation, created with the specified vector.
**Since:** 1.2

---

#### getTranslateInstance

public static

AffineTransform

getTranslateInstance​(double tx,
double ty)

Returns a transform representing a translation transformation.
The matrix representing the returned transform is:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]

getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double theta)
```

Returns a transform representing a rotation transformation.
The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Returns:** an

AffineTransform

object that is a rotation
transformation, created with the specified angle of rotation.
**Since:** 1.2

---

#### getRotateInstance

public static

AffineTransform

getRotateInstance​(double theta)

Returns a transform representing a rotation transformation.
The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]

getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double theta,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
AffineTransform Tx = new AffineTransform();
Tx.translate(anchorx, anchory); // S3: final translation
Tx.rotate(theta); // S2: rotate around anchor
Tx.translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates around the specified point by the specified angle of
rotation.
**Since:** 1.2

---

#### getRotateInstance

public static

AffineTransform

getRotateInstance​(double theta,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
AffineTransform Tx = new AffineTransform();
Tx.translate(anchorx, anchory); // S3: final translation
Tx.rotate(theta); // S2: rotate around anchor
Tx.translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

This operation is equivalent to the following sequence of calls:

```java
AffineTransform Tx = new AffineTransform();
Tx.translate(anchorx, anchory); // S3: final translation
Tx.rotate(theta); // S2: rotate around anchor
Tx.translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing the returned transform is:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

AffineTransform Tx = new AffineTransform();
Tx.translate(anchorx, anchory); // S3: final translation
Tx.rotate(theta); // S2: rotate around anchor
Tx.translate(-anchorx, -anchory); // S1: translate anchor to origin

[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]

getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double vecx,
double vecy)
```

Returns a transform that rotates coordinates according to
a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Returns:** an

AffineTransform

object that rotates
coordinates according to the specified rotation vector.
**Since:** 1.6

---

#### getRotateInstance

public static

AffineTransform

getRotateInstance​(double vecx,
double vecy)

Returns a transform that rotates coordinates according to
a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx));
```

AffineTransform.getRotateInstance(Math.atan2(vecy, vecx));

getRotateInstance

```java
public static
AffineTransform
getRotateInstance​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx),
anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates around the specified point according to the
specified rotation vector.
**Since:** 1.6

---

#### getRotateInstance

public static

AffineTransform

getRotateInstance​(double vecx,
double vecy,
double anchorx,
double anchory)

Returns a transform that rotates coordinates around an anchor
point according to a rotation vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
an identity transform is returned.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(Math.atan2(vecy, vecx),
anchorx, anchory);
```

AffineTransform.getRotateInstance(Math.atan2(vecy, vecx),
anchorx, anchory);

getQuadrantRotateInstance

```java
public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants)
```

Returns a transform that rotates coordinates by the specified
number of quadrants.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Returns:** an

AffineTransform

object that rotates
coordinates by the specified number of quadrants.
**Since:** 1.6

---

#### getQuadrantRotateInstance

public static

AffineTransform

getQuadrantRotateInstance​(int numquadrants)

Returns a transform that rotates coordinates by the specified
number of quadrants.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0);

getQuadrantRotateInstance

```java
public static
AffineTransform
getQuadrantRotateInstance​(int numquadrants,
double anchorx,
double anchory)
```

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0,
anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Returns:** an

AffineTransform

object that rotates
coordinates by the specified number of quadrants around the
specified anchor point.
**Since:** 1.6

---

#### getQuadrantRotateInstance

public static

AffineTransform

getQuadrantRotateInstance​(int numquadrants,
double anchorx,
double anchory)

Returns a transform that rotates coordinates by the specified
number of quadrants around the specified anchor point.
This operation is equivalent to calling:

```java
AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0,
anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

AffineTransform.getRotateInstance(numquadrants * Math.PI / 2.0,
anchorx, anchory);

getScaleInstance

```java
public static
AffineTransform
getScaleInstance​(double sx,
double sy)
```

Returns a transform representing a scaling transformation.
The matrix representing the returned transform is:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Returns:** an

AffineTransform

object that scales
coordinates by the specified factors.
**Since:** 1.2

---

#### getScaleInstance

public static

AffineTransform

getScaleInstance​(double sx,
double sy)

Returns a transform representing a scaling transformation.
The matrix representing the returned transform is:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]

getShearInstance

```java
public static
AffineTransform
getShearInstance​(double shx,
double shy)
```

Returns a transform representing a shearing transformation.
The matrix representing the returned transform is:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Returns:** an

AffineTransform

object that shears
coordinates by the specified multipliers.
**Since:** 1.2

---

#### getShearInstance

public static

AffineTransform

getShearInstance​(double shx,
double shy)

Returns a transform representing a shearing transformation.
The matrix representing the returned transform is:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]

getType

```java
public int getType()
```

Retrieves the flag bits describing the conversion properties of
this transform.
The return value is either one of the constants TYPE_IDENTITY
or TYPE_GENERAL_TRANSFORM, or a combination of the
appropriate flag bits.
A valid combination of flag bits is an exclusive OR operation
that can combine
the TYPE_TRANSLATION flag bit
in addition to either of the
TYPE_UNIFORM_SCALE or TYPE_GENERAL_SCALE flag bits
as well as either of the
TYPE_QUADRANT_ROTATION or TYPE_GENERAL_ROTATION flag bits.

**Returns:** the OR combination of any of the indicated flags that
apply to this transform
**Since:** 1.2
**See Also:** TYPE_IDENTITY

,

TYPE_TRANSLATION

,

TYPE_UNIFORM_SCALE

,

TYPE_GENERAL_SCALE

,

TYPE_QUADRANT_ROTATION

,

TYPE_GENERAL_ROTATION

,

TYPE_GENERAL_TRANSFORM

---

#### getType

public int getType()

Retrieves the flag bits describing the conversion properties of
this transform.
The return value is either one of the constants TYPE_IDENTITY
or TYPE_GENERAL_TRANSFORM, or a combination of the
appropriate flag bits.
A valid combination of flag bits is an exclusive OR operation
that can combine
the TYPE_TRANSLATION flag bit
in addition to either of the
TYPE_UNIFORM_SCALE or TYPE_GENERAL_SCALE flag bits
as well as either of the
TYPE_QUADRANT_ROTATION or TYPE_GENERAL_ROTATION flag bits.

getDeterminant

```java
public double getDeterminant()
```

Returns the determinant of the matrix representation of the transform.
The determinant is useful both to determine if the transform can
be inverted and to get a single value representing the
combined X and Y scaling of the transform.

If the determinant is non-zero, then this transform is
invertible and the various methods that depend on the inverse
transform do not need to throw a

NoninvertibleTransformException

.
If the determinant is zero then this transform can not be
inverted since the transform maps all input coordinates onto
a line or a point.
If the determinant is near enough to zero then inverse transform
operations might not carry enough precision to produce meaningful
results.

If this transform represents a uniform scale, as indicated by
the

getType

method then the determinant also
represents the square of the uniform scale factor by which all of
the points are expanded from or contracted towards the origin.
If this transform represents a non-uniform scale or more general
transform then the determinant is not likely to represent a
value useful for any purpose other than determining if inverse
transforms are possible.

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

**Returns:** the determinant of the matrix used to transform the
coordinates.
**Since:** 1.2
**See Also:** getType()

,

createInverse()

,

inverseTransform(java.awt.geom.Point2D, java.awt.geom.Point2D)

,

TYPE_UNIFORM_SCALE

---

#### getDeterminant

public double getDeterminant()

Returns the determinant of the matrix representation of the transform.
The determinant is useful both to determine if the transform can
be inverted and to get a single value representing the
combined X and Y scaling of the transform.

If the determinant is non-zero, then this transform is
invertible and the various methods that depend on the inverse
transform do not need to throw a

NoninvertibleTransformException

.
If the determinant is zero then this transform can not be
inverted since the transform maps all input coordinates onto
a line or a point.
If the determinant is near enough to zero then inverse transform
operations might not carry enough precision to produce meaningful
results.

If this transform represents a uniform scale, as indicated by
the

getType

method then the determinant also
represents the square of the uniform scale factor by which all of
the points are expanded from or contracted towards the origin.
If this transform represents a non-uniform scale or more general
transform then the determinant is not likely to represent a
value useful for any purpose other than determining if inverse
transforms are possible.

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

If the determinant is non-zero, then this transform is
invertible and the various methods that depend on the inverse
transform do not need to throw a

NoninvertibleTransformException

.
If the determinant is zero then this transform can not be
inverted since the transform maps all input coordinates onto
a line or a point.
If the determinant is near enough to zero then inverse transform
operations might not carry enough precision to produce meaningful
results.

If this transform represents a uniform scale, as indicated by
the

getType

method then the determinant also
represents the square of the uniform scale factor by which all of
the points are expanded from or contracted towards the origin.
If this transform represents a non-uniform scale or more general
transform then the determinant is not likely to represent a
value useful for any purpose other than determining if inverse
transforms are possible.

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

If this transform represents a uniform scale, as indicated by
the

getType

method then the determinant also
represents the square of the uniform scale factor by which all of
the points are expanded from or contracted towards the origin.
If this transform represents a non-uniform scale or more general
transform then the determinant is not likely to represent a
value useful for any purpose other than determining if inverse
transforms are possible.

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

Mathematically, the determinant is calculated using the formula:

```java
| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |
```

| m00 m01 m02 |
| m10 m11 m12 | = m00 * m11 - m01 * m10
| 0 0 1 |

getMatrix

```java
public void getMatrix​(double[] flatmatrix)
```

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.
The values are stored in the array as
{ m00 m10 m01 m11 m02 m12 }.
An array of 4 doubles can also be specified, in which case only the
first four elements representing the non-transform
parts of the array are retrieved and the values are stored into
the array as { m00 m10 m01 m11 }

**Parameters:** flatmatrix

- the double array used to store the returned
values.
**Since:** 1.2
**See Also:** getScaleX()

,

getScaleY()

,

getShearX()

,

getShearY()

,

getTranslateX()

,

getTranslateY()

---

#### getMatrix

public void getMatrix​(double[] flatmatrix)

Retrieves the 6 specifiable values in the 3x3 affine transformation
matrix and places them into an array of double precisions values.
The values are stored in the array as
{ m00 m10 m01 m11 m02 m12 }.
An array of 4 doubles can also be specified, in which case only the
first four elements representing the non-transform
parts of the array are retrieved and the values are stored into
the array as { m00 m10 m01 m11 }

getScaleX

```java
public double getScaleX()
```

Returns the

m00

element of the 3x3 affine transformation matrix.
This matrix factor determines how input X coordinates will affect output
X coordinates and is one element of the scale of the transform.
To measure the full amount by which X coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(1, 0);
p = tx.deltaTransform(p, p);
double scaleX = p.distance(0, 0);
```

**Returns:** a double value that is

m00

element of the
3x3 affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

---

#### getScaleX

public double getScaleX()

Returns the

m00

element of the 3x3 affine transformation matrix.
This matrix factor determines how input X coordinates will affect output
X coordinates and is one element of the scale of the transform.
To measure the full amount by which X coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(1, 0);
p = tx.deltaTransform(p, p);
double scaleX = p.distance(0, 0);
```

Point2D p = new Point2D.Double(1, 0);
p = tx.deltaTransform(p, p);
double scaleX = p.distance(0, 0);

getScaleY

```java
public double getScaleY()
```

Returns the

m11

element of the 3x3 affine transformation matrix.
This matrix factor determines how input Y coordinates will affect output
Y coordinates and is one element of the scale of the transform.
To measure the full amount by which Y coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(0, 1);
p = tx.deltaTransform(p, p);
double scaleY = p.distance(0, 0);
```

**Returns:** a double value that is

m11

element of the
3x3 affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

---

#### getScaleY

public double getScaleY()

Returns the

m11

element of the 3x3 affine transformation matrix.
This matrix factor determines how input Y coordinates will affect output
Y coordinates and is one element of the scale of the transform.
To measure the full amount by which Y coordinates are stretched or
contracted by this transform, use the following code:

```java
Point2D p = new Point2D.Double(0, 1);
p = tx.deltaTransform(p, p);
double scaleY = p.distance(0, 0);
```

Point2D p = new Point2D.Double(0, 1);
p = tx.deltaTransform(p, p);
double scaleY = p.distance(0, 0);

getShearX

```java
public double getShearX()
```

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

**Returns:** a double value that is the X coordinate of the shearing
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

---

#### getShearX

public double getShearX()

Returns the X coordinate shearing element (m01) of the 3x3
affine transformation matrix.

getShearY

```java
public double getShearY()
```

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

**Returns:** a double value that is the Y coordinate of the shearing
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

---

#### getShearY

public double getShearY()

Returns the Y coordinate shearing element (m10) of the 3x3
affine transformation matrix.

getTranslateX

```java
public double getTranslateX()
```

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

**Returns:** a double value that is the X coordinate of the translation
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

---

#### getTranslateX

public double getTranslateX()

Returns the X coordinate of the translation element (m02) of the
3x3 affine transformation matrix.

getTranslateY

```java
public double getTranslateY()
```

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

**Returns:** a double value that is the Y coordinate of the translation
element of the affine transformation matrix.
**Since:** 1.2
**See Also:** getMatrix(double[])

---

#### getTranslateY

public double getTranslateY()

Returns the Y coordinate of the translation element (m12) of the
3x3 affine transformation matrix.

translate

```java
public void translate​(double tx,
double ty)
```

Concatenates this transform with a translation transformation.
This is equivalent to calling concatenate(T), where T is an

AffineTransform

represented by the following matrix:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Since:** 1.2

---

#### translate

public void translate​(double tx,
double ty)

Concatenates this transform with a translation transformation.
This is equivalent to calling concatenate(T), where T is an

AffineTransform

represented by the following matrix:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]

rotate

```java
public void rotate​(double theta)
```

Concatenates this transform with a rotation transformation.
This is equivalent to calling concatenate(R), where R is an

AffineTransform

represented by the following matrix:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Since:** 1.2

---

#### rotate

public void rotate​(double theta)

Concatenates this transform with a rotation transformation.
This is equivalent to calling concatenate(R), where R is an

AffineTransform

represented by the following matrix:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]

rotate

```java
public void rotate​(double theta,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
translate(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.2

---

#### rotate

public void rotate​(double theta,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
translate(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

This operation is equivalent to the following sequence of calls:

```java
translate(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

translate(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin

rotate

```java
public void rotate​(double vecx,
double vecy)
```

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
no additional rotation is added to this transform.
This operation is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Since:** 1.6

---

#### rotate

public void rotate​(double vecx,
double vecy)

Concatenates this transform with a transform that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
no additional rotation is added to this transform.
This operation is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx));
```

rotate(Math.atan2(vecy, vecx));

rotate

```java
public void rotate​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is not modified in any way.
This method is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

---

#### rotate

public void rotate​(double vecx,
double vecy,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is not modified in any way.
This method is equivalent to calling:

```java
rotate(Math.atan2(vecy, vecx), anchorx, anchory);
```

rotate(Math.atan2(vecy, vecx), anchorx, anchory);

quadrantRotate

```java
public void quadrantRotate​(int numquadrants)
```

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.
This is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Since:** 1.6

---

#### quadrantRotate

public void quadrantRotate​(int numquadrants)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants.
This is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

rotate(numquadrants * Math.PI / 2.0);

quadrantRotate

```java
public void quadrantRotate​(int numquadrants,
double anchorx,
double anchory)
```

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.
This method is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

---

#### quadrantRotate

public void quadrantRotate​(int numquadrants,
double anchorx,
double anchory)

Concatenates this transform with a transform that rotates
coordinates by the specified number of quadrants around
the specified anchor point.
This method is equivalent to calling:

```java
rotate(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

rotate(numquadrants * Math.PI / 2.0, anchorx, anchory);

scale

```java
public void scale​(double sx,
double sy)
```

Concatenates this transform with a scaling transformation.
This is equivalent to calling concatenate(S), where S is an

AffineTransform

represented by the following matrix:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Since:** 1.2

---

#### scale

public void scale​(double sx,
double sy)

Concatenates this transform with a scaling transformation.
This is equivalent to calling concatenate(S), where S is an

AffineTransform

represented by the following matrix:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]

shear

```java
public void shear​(double shx,
double shy)
```

Concatenates this transform with a shearing transformation.
This is equivalent to calling concatenate(SH), where SH is an

AffineTransform

represented by the following matrix:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Since:** 1.2

---

#### shear

public void shear​(double shx,
double shy)

Concatenates this transform with a shearing transformation.
This is equivalent to calling concatenate(SH), where SH is an

AffineTransform

represented by the following matrix:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]

setToIdentity

```java
public void setToIdentity()
```

Resets this transform to the Identity transform.

**Since:** 1.2

---

#### setToIdentity

public void setToIdentity()

Resets this transform to the Identity transform.

setToTranslation

```java
public void setToTranslation​(double tx,
double ty)
```

Sets this transform to a translation transformation.
The matrix representing this transform becomes:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

**Parameters:** tx

- the distance by which coordinates are translated in the
X axis direction
**Parameters:** ty

- the distance by which coordinates are translated in the
Y axis direction
**Since:** 1.2

---

#### setToTranslation

public void setToTranslation​(double tx,
double ty)

Sets this transform to a translation transformation.
The matrix representing this transform becomes:

```java
[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]
```

[ 1 0 tx ]
[ 0 1 ty ]
[ 0 0 1 ]

setToRotation

```java
public void setToRotation​(double theta)
```

Sets this transform to a rotation transformation.
The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Since:** 1.2

---

#### setToRotation

public void setToRotation​(double theta)

Sets this transform to a rotation transformation.
The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

[ cos(theta) -sin(theta) 0 ]
[ sin(theta) cos(theta) 0 ]
[ 0 0 1 ]

setToRotation

```java
public void setToRotation​(double theta,
double anchorx,
double anchory)
```

Sets this transform to a translated rotation transformation.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
setToTranslation(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

**Parameters:** theta

- the angle of rotation measured in radians
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.2

---

#### setToRotation

public void setToRotation​(double theta,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation.
This operation is equivalent to translating the coordinates so
that the anchor point is at the origin (S1), then rotating them
about the new origin (S2), and finally translating so that the
intermediate origin is restored to the coordinates of the original
anchor point (S3).

This operation is equivalent to the following sequence of calls:

```java
setToTranslation(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

This operation is equivalent to the following sequence of calls:

```java
setToTranslation(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin
```

The matrix representing this transform becomes:

```java
[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]
```

Rotating by a positive angle theta rotates points on the positive
X axis toward the positive Y axis.
Note also the discussion of

Handling 90-Degree Rotations

above.

setToTranslation(anchorx, anchory); // S3: final translation
rotate(theta); // S2: rotate around anchor
translate(-anchorx, -anchory); // S1: translate anchor to origin

[ cos(theta) -sin(theta) x-x*cos+y*sin ]
[ sin(theta) cos(theta) y-x*sin-y*cos ]
[ 0 0 1 ]

setToRotation

```java
public void setToRotation​(double vecx,
double vecy)
```

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToRotation(Math.atan2(vecy, vecx));
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Since:** 1.6

---

#### setToRotation

public void setToRotation​(double vecx,
double vecy)

Sets this transform to a rotation transformation that rotates
coordinates according to a rotation vector.
All coordinates rotate about the origin by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToRotation(Math.atan2(vecy, vecx));
```

setToRotation(Math.atan2(vecy, vecx));

setToRotation

```java
public void setToRotation​(double vecx,
double vecy,
double anchorx,
double anchory)
```

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToTranslation(Math.atan2(vecy, vecx), anchorx, anchory);
```

**Parameters:** vecx

- the X coordinate of the rotation vector
**Parameters:** vecy

- the Y coordinate of the rotation vector
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

---

#### setToRotation

public void setToRotation​(double vecx,
double vecy,
double anchorx,
double anchory)

Sets this transform to a rotation transformation that rotates
coordinates around an anchor point according to a rotation
vector.
All coordinates rotate about the specified anchor coordinates
by the same amount.
The amount of rotation is such that coordinates along the former
positive X axis will subsequently align with the vector pointing
from the origin to the specified vector coordinates.
If both

vecx

and

vecy

are 0.0,
the transform is set to an identity transform.
This operation is equivalent to calling:

```java
setToTranslation(Math.atan2(vecy, vecx), anchorx, anchory);
```

setToTranslation(Math.atan2(vecy, vecx), anchorx, anchory);

setToQuadrantRotation

```java
public void setToQuadrantRotation​(int numquadrants)
```

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Since:** 1.6

---

#### setToQuadrantRotation

public void setToQuadrantRotation​(int numquadrants)

Sets this transform to a rotation transformation that rotates
coordinates by the specified number of quadrants.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

setToRotation(numquadrants * Math.PI / 2.0);

setToQuadrantRotation

```java
public void setToQuadrantRotation​(int numquadrants,
double anchorx,
double anchory)
```

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

**Parameters:** numquadrants

- the number of 90 degree arcs to rotate by
**Parameters:** anchorx

- the X coordinate of the rotation anchor point
**Parameters:** anchory

- the Y coordinate of the rotation anchor point
**Since:** 1.6

---

#### setToQuadrantRotation

public void setToQuadrantRotation​(int numquadrants,
double anchorx,
double anchory)

Sets this transform to a translated rotation transformation
that rotates coordinates by the specified number of quadrants
around the specified anchor point.
This operation is equivalent to calling:

```java
setToRotation(numquadrants * Math.PI / 2.0, anchorx, anchory);
```

Rotating by a positive number of quadrants rotates points on
the positive X axis toward the positive Y axis.

setToRotation(numquadrants * Math.PI / 2.0, anchorx, anchory);

setToScale

```java
public void setToScale​(double sx,
double sy)
```

Sets this transform to a scaling transformation.
The matrix representing this transform becomes:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

**Parameters:** sx

- the factor by which coordinates are scaled along the
X axis direction
**Parameters:** sy

- the factor by which coordinates are scaled along the
Y axis direction
**Since:** 1.2

---

#### setToScale

public void setToScale​(double sx,
double sy)

Sets this transform to a scaling transformation.
The matrix representing this transform becomes:

```java
[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]
```

[ sx 0 0 ]
[ 0 sy 0 ]
[ 0 0 1 ]

setToShear

```java
public void setToShear​(double shx,
double shy)
```

Sets this transform to a shearing transformation.
The matrix representing this transform becomes:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

**Parameters:** shx

- the multiplier by which coordinates are shifted in the
direction of the positive X axis as a factor of their Y coordinate
**Parameters:** shy

- the multiplier by which coordinates are shifted in the
direction of the positive Y axis as a factor of their X coordinate
**Since:** 1.2

---

#### setToShear

public void setToShear​(double shx,
double shy)

Sets this transform to a shearing transformation.
The matrix representing this transform becomes:

```java
[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]
```

[ 1 shx 0 ]
[ shy 1 0 ]
[ 0 0 1 ]

setTransform

```java
public void setTransform​(
AffineTransform
Tx)
```

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

**Parameters:** Tx

- the

AffineTransform

object from which to
copy the transform
**Since:** 1.2

---

#### setTransform

public void setTransform​(

AffineTransform

Tx)

Sets this transform to a copy of the transform in the specified

AffineTransform

object.

setTransform

```java
public void setTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)
```

Sets this transform to the matrix specified by the 6
double precision values.

**Parameters:** m00

- the X coordinate scaling element of the 3x3 matrix
**Parameters:** m10

- the Y coordinate shearing element of the 3x3 matrix
**Parameters:** m01

- the X coordinate shearing element of the 3x3 matrix
**Parameters:** m11

- the Y coordinate scaling element of the 3x3 matrix
**Parameters:** m02

- the X coordinate translation element of the 3x3 matrix
**Parameters:** m12

- the Y coordinate translation element of the 3x3 matrix
**Since:** 1.2

---

#### setTransform

public void setTransform​(double m00,
double m10,
double m01,
double m11,
double m02,
double m12)

Sets this transform to the matrix specified by the 6
double precision values.

concatenate

```java
public void concatenate​(
AffineTransform
Tx)
```

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by

Tx

and then
transforming the result by the original transform Cx like this:
Cx'(p) = Cx(Tx(p))
In matrix notation, if this transform Cx is
represented by the matrix [this] and

Tx

is represented
by the matrix [Tx] then this method does the following:

```java
[this] = [this] x [Tx]
```

**Parameters:** Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.
**Since:** 1.2
**See Also:** preConcatenate(java.awt.geom.AffineTransform)

---

#### concatenate

public void concatenate​(

AffineTransform

Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx in the most commonly useful
way to provide a new user space
that is mapped to the former user space by

Tx

.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by

Tx

and then
transforming the result by the original transform Cx like this:
Cx'(p) = Cx(Tx(p))
In matrix notation, if this transform Cx is
represented by the matrix [this] and

Tx

is represented
by the matrix [Tx] then this method does the following:

```java
[this] = [this] x [Tx]
```

[this] = [this] x [Tx]

preConcatenate

```java
public void preConcatenate​(
AffineTransform
Tx)
```

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by the original transform
Cx and then transforming the result by

Tx

like this:
Cx'(p) = Tx(Cx(p))
In matrix notation, if this transform Cx
is represented by the matrix [this] and

Tx

is
represented by the matrix [Tx] then this method does the
following:

```java
[this] = [Tx] x [this]
```

**Parameters:** Tx

- the

AffineTransform

object to be
concatenated with this

AffineTransform

object.
**Since:** 1.2
**See Also:** concatenate(java.awt.geom.AffineTransform)

---

#### preConcatenate

public void preConcatenate​(

AffineTransform

Tx)

Concatenates an

AffineTransform Tx

to
this

AffineTransform

Cx
in a less commonly used way such that

Tx

modifies the
coordinate transformation relative to the absolute pixel
space rather than relative to the existing user space.
Cx is updated to perform the combined transformation.
Transforming a point p by the updated transform Cx' is
equivalent to first transforming p by the original transform
Cx and then transforming the result by

Tx

like this:
Cx'(p) = Tx(Cx(p))
In matrix notation, if this transform Cx
is represented by the matrix [this] and

Tx

is
represented by the matrix [Tx] then this method does the
following:

```java
[this] = [Tx] x [this]
```

[this] = [Tx] x [this]

createInverse

```java
public
AffineTransform
createInverse()
throws
NoninvertibleTransformException
```

Returns an

AffineTransform

object representing the
inverse transformation.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

createInverse

method is called.

**Returns:** a new

AffineTransform

object representing the
inverse transformation.
**Throws:** NoninvertibleTransformException

- if the matrix cannot be inverted.
**Since:** 1.2
**See Also:** getDeterminant()

---

#### createInverse

public

AffineTransform

createInverse()
throws

NoninvertibleTransformException

Returns an

AffineTransform

object representing the
inverse transformation.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

createInverse

method is called.

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

createInverse

method is called.

invert

```java
public void invert()
throws
NoninvertibleTransformException
```

Sets this transform to the inverse of itself.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

invert

method is called.

**Throws:** NoninvertibleTransformException

- if the matrix cannot be inverted.
**Since:** 1.6
**See Also:** getDeterminant()

---

#### invert

public void invert()
throws

NoninvertibleTransformException

Sets this transform to the inverse of itself.
The inverse transform Tx' of this transform Tx
maps coordinates transformed by Tx back
to their original coordinates.
In other words, Tx'(Tx(p)) = p = Tx(Tx'(p)).

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

invert

method is called.

If this transform maps all coordinates onto a point or a line
then it will not have an inverse, since coordinates that do
not lie on the destination point or line will not have an inverse
mapping.
The

getDeterminant

method can be used to determine if this
transform has no inverse, in which case an exception will be
thrown if the

invert

method is called.

transform

```java
public
Point2D
transform​(
Point2D
ptSrc,

Point2D
ptDst)
```

Transforms the specified

ptSrc

and stores the result
in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the transformation is
stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with
the transformed point.

**Parameters:** ptSrc

- the specified

Point2D

to be transformed
**Parameters:** ptDst

- the specified

Point2D

that stores the
result of transforming

ptSrc
**Returns:** the

ptDst

after transforming

ptSrc

and storing the result in

ptDst

.
**Since:** 1.2

---

#### transform

public

Point2D

transform​(

Point2D

ptSrc,

Point2D

ptDst)

Transforms the specified

ptSrc

and stores the result
in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the transformation is
stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with
the transformed point.

transform

```java
public void transform​(
Point2D
[] ptSrc,
int srcOff,

Point2D
[] ptDst,
int dstOff,
int numPts)
```

Transforms an array of point objects by this transform.
If any element of the

ptDst

array is

null

, a new

Point2D

object is allocated
and stored into that element before storing the results of the
transformation.

Note that this method does not take any precautions to
avoid problems caused by storing results into

Point2D

objects that will be used as the source for calculations
further down the source array.
This method does guarantee that if a specified

Point2D

object is both the source and destination for the same single point
transform operation then the results will not be stored until
the calculations are complete to avoid storing the results on
top of the operands.
If, however, the destination

Point2D

object for one
operation is the same object as the source

Point2D

object for another operation further down the source array then
the original coordinates in that point are overwritten before
they can be converted.

**Parameters:** ptSrc

- the array containing the source point objects
**Parameters:** ptDst

- the array into which the transform point objects are
returned
**Parameters:** srcOff

- the offset to the first point object to be
transformed in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point object that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

---

#### transform

public void transform​(

Point2D

[] ptSrc,
int srcOff,

Point2D

[] ptDst,
int dstOff,
int numPts)

Transforms an array of point objects by this transform.
If any element of the

ptDst

array is

null

, a new

Point2D

object is allocated
and stored into that element before storing the results of the
transformation.

Note that this method does not take any precautions to
avoid problems caused by storing results into

Point2D

objects that will be used as the source for calculations
further down the source array.
This method does guarantee that if a specified

Point2D

object is both the source and destination for the same single point
transform operation then the results will not be stored until
the calculations are complete to avoid storing the results on
top of the operands.
If, however, the destination

Point2D

object for one
operation is the same object as the source

Point2D

object for another operation further down the source array then
the original coordinates in that point are overwritten before
they can be converted.

Note that this method does not take any precautions to
avoid problems caused by storing results into

Point2D

objects that will be used as the source for calculations
further down the source array.
This method does guarantee that if a specified

Point2D

object is both the source and destination for the same single point
transform operation then the results will not be stored until
the calculations are complete to avoid storing the results on
top of the operands.
If, however, the destination

Point2D

object for one
operation is the same object as the source

Point2D

object for another operation further down the source array then
the original coordinates in that point are overwritten before
they can be converted.

transform

```java
public void transform​(float[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of floating point coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are overwritten by a
previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of points to be transformed
**Since:** 1.2

---

#### transform

public void transform​(float[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are overwritten by a
previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

transform

```java
public void transform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of double precision coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

---

#### transform

public void transform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

transform

```java
public void transform​(float[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point coordinates
are returned. Each point is stored as a pair of x, y
coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of points to be transformed
**Since:** 1.2

---

#### transform

public void transform​(float[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of floating point coordinates by this transform
and stores the results into an array of doubles.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

transform

```java
public void transform​(double[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Since:** 1.2

---

#### transform

public void transform​(double[] srcPts,
int srcOff,
float[] dstPts,
int dstOff,
int numPts)

Transforms an array of double precision coordinates by this transform
and stores the results into an array of floats.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

inverseTransform

```java
public
Point2D
inverseTransform​(
Point2D
ptSrc,

Point2D
ptDst)
throws
NoninvertibleTransformException
```

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the transformed
point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with the
transformed point.

**Parameters:** ptSrc

- the point to be inverse transformed
**Parameters:** ptDst

- the resulting transformed point
**Returns:** ptDst

, which contains the result of the
inverse transform.
**Throws:** NoninvertibleTransformException

- if the matrix cannot be
inverted.
**Since:** 1.2

---

#### inverseTransform

public

Point2D

inverseTransform​(

Point2D

ptSrc,

Point2D

ptDst)
throws

NoninvertibleTransformException

Inverse transforms the specified

ptSrc

and stores the
result in

ptDst

.
If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the transformed
point, is returned for convenience.
If

ptSrc

and

ptDst

are the same
object, the input point is correctly overwritten with the
transformed point.

inverseTransform

```java
public void inverseTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
throws
NoninvertibleTransformException
```

Inverse transforms an array of double precision coordinates by
this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source point coordinates.
Each point is stored as a pair of x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed point
coordinates are returned. Each point is stored as a pair of
x, y coordinates.
**Parameters:** srcOff

- the offset to the first point to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed point that is stored in the destination array
**Parameters:** numPts

- the number of point objects to be transformed
**Throws:** NoninvertibleTransformException

- if the matrix cannot be
inverted.
**Since:** 1.2

---

#### inverseTransform

public void inverseTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
throws

NoninvertibleTransformException

Inverse transforms an array of double precision coordinates by
this transform.
The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the specified
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

deltaTransform

```java
public
Point2D
deltaTransform​(
Point2D
ptSrc,

Point2D
ptDst)
```

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same object,
the input point is correctly overwritten with the transformed
point.

**Parameters:** ptSrc

- the distance vector to be delta transformed
**Parameters:** ptDst

- the resulting transformed distance vector
**Returns:** ptDst

, which contains the result of the
transformation.
**Since:** 1.2

---

#### deltaTransform

public

Point2D

deltaTransform​(

Point2D

ptSrc,

Point2D

ptDst)

Transforms the relative distance vector specified by

ptSrc

and stores the result in

ptDst

.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

If

ptDst

is

null

, a new

Point2D

object is allocated and then the result of the
transform is stored in this object.
In either case,

ptDst

, which contains the
transformed point, is returned for convenience.
If

ptSrc

and

ptDst

are the same object,
the input point is correctly overwritten with the transformed
point.

[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]

deltaTransform

```java
public void deltaTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)
```

Transforms an array of relative distance vectors by this
transform.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

**Parameters:** srcPts

- the array containing the source distance vectors.
Each vector is stored as a pair of relative x, y coordinates.
**Parameters:** dstPts

- the array into which the transformed distance vectors
are returned. Each vector is stored as a pair of relative
x, y coordinates.
**Parameters:** srcOff

- the offset to the first vector to be transformed
in the source array
**Parameters:** dstOff

- the offset to the location of the first
transformed vector that is stored in the destination array
**Parameters:** numPts

- the number of vector coordinate pairs to be
transformed
**Since:** 1.2

---

#### deltaTransform

public void deltaTransform​(double[] srcPts,
int srcOff,
double[] dstPts,
int dstOff,
int numPts)

Transforms an array of relative distance vectors by this
transform.
A relative distance vector is transformed without applying the
translation components of the affine transformation matrix
using the following equations:

```java
[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]
```

The two coordinate array sections can be exactly the same or
can be overlapping sections of the same array without affecting the
validity of the results.
This method ensures that no source coordinates are
overwritten by a previous operation before they can be transformed.
The coordinates are stored in the arrays starting at the indicated
offset in the order

[x0, y0, x1, y1, ..., xn, yn]

.

[ x' ] [ m00 m01 (m02) ] [ x ] [ m00x + m01y ]
[ y' ] = [ m10 m11 (m12) ] [ y ] = [ m10x + m11y ]
[ (1) ] [ (0) (0) ( 1 ) ] [ (1) ] [ (1) ]

createTransformedShape

```java
public
Shape
createTransformedShape​(
Shape
pSrc)
```

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

**Parameters:** pSrc

- the specified

Shape

object to be
transformed by this transform.
**Returns:** a new

Shape

object that defines the geometry
of the transformed

Shape

, or null if

pSrc

is null.
**Since:** 1.2

---

#### createTransformedShape

public

Shape

createTransformedShape​(

Shape

pSrc)

Returns a new

Shape

object defined by the geometry of the
specified

Shape

after it has been transformed by
this transform.

toString

```java
public
String
toString()
```

Returns a

String

that represents the value of this

Object

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing the value of this

Object

.
**Since:** 1.2

---

#### toString

public

String

toString()

Returns a

String

that represents the value of this

Object

.

isIdentity

```java
public boolean isIdentity()
```

Returns

true

if this

AffineTransform

is
an identity transform.

**Returns:** true

if this

AffineTransform

is
an identity transform;

false

otherwise.
**Since:** 1.2

---

#### isIdentity

public boolean isIdentity()

Returns

true

if this

AffineTransform

is
an identity transform.

clone

```java
public
Object
clone()
```

Returns a copy of this

AffineTransform

object.

**Overrides:** clone

in class

Object
**Returns:** an

Object

that is a copy of this

AffineTransform

object.
**Since:** 1.2
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a copy of this

AffineTransform

object.

hashCode

```java
public int hashCode()
```

Returns the hashcode for this transform.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this transform.
**Since:** 1.2
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashcode for this transform.

equals

```java
public boolean equals​(
Object
obj)
```

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the

Object

to test for equality with this

AffineTransform
**Returns:** true

if

obj

equals this

AffineTransform

object;

false

otherwise.
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Returns

true

if this

AffineTransform

represents the same affine coordinate transform as the specified
argument.

---

