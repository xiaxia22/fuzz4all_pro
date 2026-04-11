# Interface PathIterator

**Source:** `java.desktop\java\awt\geom\PathIterator.html`

### Class Description

```java
public interface
PathIterator
```

The

PathIterator

interface provides the mechanism
for objects that implement the

Shape

interface to return the geometry of their boundary by allowing
a caller to retrieve the path of that boundary a segment at a
time. This interface allows these objects to retrieve the path of
their boundary a segment at a time by using 1st through 3rd order
Bézier curves, which are lines and quadratic or cubic
Bézier splines.

Multiple subpaths can be expressed by using a "MOVETO" segment to
create a discontinuity in the geometry to move from the end of
one subpath to the beginning of the next.

Each subpath can be closed manually by ending the last segment in
the subpath on the same coordinate as the beginning "MOVETO" segment
for that subpath or by using a "CLOSE" segment to append a line
segment from the last point back to the first.
Be aware that manually closing an outline as opposed to using a
"CLOSE" segment to close the path might result in different line
style decorations being used at the end points of the subpath.
For example, the

BasicStroke

object
uses a line "JOIN" decoration to connect the first and last points
if a "CLOSE" segment is encountered, whereas simply ending the path
on the same coordinate as the beginning coordinate results in line
"CAP" decorations being used at the ends.

**All Known Implementing Classes:** FlatteningPathIterator

---

### Field Details

#### @Native

static final int WIND_EVEN_ODD

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.
The even-odd rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments an odd number of times.

**See Also:**
- Constant Field Values

---

#### @Native

static final int WIND_NON_ZERO

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.
The non-zero rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments a different number
of times in the counter-clockwise direction than the
clockwise direction.

**See Also:**
- Constant Field Values

---

#### @Native

static final int SEG_MOVETO

The segment type constant for a point that specifies the
starting location for a new subpath.

**See Also:**
- Constant Field Values

---

#### @Native

static final int SEG_LINETO

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

**See Also:**
- Constant Field Values

---

#### @Native

static final int SEG_QUADTO

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
and the final interpolated control point (P2).
The parametric control equation for this curve is:

```java
P(t) = B(2,0)*CP + B(2,1)*P1 + B(2,2)*P2
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

**See Also:**
- Constant Field Values

---

#### @Native

static final int SEG_CUBICTO

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
the second control point (P2),
and the final interpolated control point (P3).
The parametric control equation for this curve is:

```java
P(t) = B(3,0)*CP + B(3,1)*P1 + B(3,2)*P2 + B(3,3)*P3
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

This form of curve is commonly known as a Bézier curve.

**See Also:**
- Constant Field Values

---

#### @Native

static final int SEG_CLOSE

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getWindingRule()

Returns the winding rule for determining the interior of the
path.

**Returns:**
- the winding rule.

**See Also:**
- WIND_EVEN_ODD

,

WIND_NON_ZERO

---

#### boolean isDone()

Tests if the iteration is complete.

**Returns:**
- true

if all the segments have
been read;

false

otherwise.

---

#### void next()

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

---

#### int currentSegment​(float[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:**
- coords

- an array that holds the data returned from
this method

**Returns:**
- the path-segment type of the current path segment.

**See Also:**
- SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

---

#### int currentSegment​(double[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:**
- coords

- an array that holds the data returned from
this method

**Returns:**
- the path-segment type of the current path segment.

**See Also:**
- SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

---

### Additional Sections

#### Interface PathIterator

**All Known Implementing Classes:** FlatteningPathIterator

```java
public interface
PathIterator
```

The

PathIterator

interface provides the mechanism
for objects that implement the

Shape

interface to return the geometry of their boundary by allowing
a caller to retrieve the path of that boundary a segment at a
time. This interface allows these objects to retrieve the path of
their boundary a segment at a time by using 1st through 3rd order
Bézier curves, which are lines and quadratic or cubic
Bézier splines.

Multiple subpaths can be expressed by using a "MOVETO" segment to
create a discontinuity in the geometry to move from the end of
one subpath to the beginning of the next.

Each subpath can be closed manually by ending the last segment in
the subpath on the same coordinate as the beginning "MOVETO" segment
for that subpath or by using a "CLOSE" segment to append a line
segment from the last point back to the first.
Be aware that manually closing an outline as opposed to using a
"CLOSE" segment to close the path might result in different line
style decorations being used at the end points of the subpath.
For example, the

BasicStroke

object
uses a line "JOIN" decoration to connect the first and last points
if a "CLOSE" segment is encountered, whereas simply ending the path
on the same coordinate as the beginning coordinate results in line
"CAP" decorations being used at the ends.

**See Also:** Shape

,

BasicStroke

public interface

PathIterator

The

PathIterator

interface provides the mechanism
for objects that implement the

Shape

interface to return the geometry of their boundary by allowing
a caller to retrieve the path of that boundary a segment at a
time. This interface allows these objects to retrieve the path of
their boundary a segment at a time by using 1st through 3rd order
Bézier curves, which are lines and quadratic or cubic
Bézier splines.

Multiple subpaths can be expressed by using a "MOVETO" segment to
create a discontinuity in the geometry to move from the end of
one subpath to the beginning of the next.

Each subpath can be closed manually by ending the last segment in
the subpath on the same coordinate as the beginning "MOVETO" segment
for that subpath or by using a "CLOSE" segment to append a line
segment from the last point back to the first.
Be aware that manually closing an outline as opposed to using a
"CLOSE" segment to close the path might result in different line
style decorations being used at the end points of the subpath.
For example, the

BasicStroke

object
uses a line "JOIN" decoration to connect the first and last points
if a "CLOSE" segment is encountered, whereas simply ending the path
on the same coordinate as the beginning coordinate results in line
"CAP" decorations being used at the ends.

Multiple subpaths can be expressed by using a "MOVETO" segment to
create a discontinuity in the geometry to move from the end of
one subpath to the beginning of the next.

Each subpath can be closed manually by ending the last segment in
the subpath on the same coordinate as the beginning "MOVETO" segment
for that subpath or by using a "CLOSE" segment to append a line
segment from the last point back to the first.
Be aware that manually closing an outline as opposed to using a
"CLOSE" segment to close the path might result in different line
style decorations being used at the end points of the subpath.
For example, the

BasicStroke

object
uses a line "JOIN" decoration to connect the first and last points
if a "CLOSE" segment is encountered, whereas simply ending the path
on the same coordinate as the beginning coordinate results in line
"CAP" decorations being used at the ends.

Each subpath can be closed manually by ending the last segment in
the subpath on the same coordinate as the beginning "MOVETO" segment
for that subpath or by using a "CLOSE" segment to append a line
segment from the last point back to the first.
Be aware that manually closing an outline as opposed to using a
"CLOSE" segment to close the path might result in different line
style decorations being used at the end points of the subpath.
For example, the

BasicStroke

object
uses a line "JOIN" decoration to connect the first and last points
if a "CLOSE" segment is encountered, whereas simply ending the path
on the same coordinate as the beginning coordinate results in line
"CAP" decorations being used at the ends.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

SEG_CLOSE

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

static int

SEG_CUBICTO

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.

static int

SEG_LINETO

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

static int

SEG_MOVETO

The segment type constant for a point that specifies the
starting location for a new subpath.

static int

SEG_QUADTO

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.

static int

WIND_EVEN_ODD

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.

static int

WIND_NON_ZERO

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

currentSegment

​(double[] coords)

Returns the coordinates and type of the current path segment in
the iteration.

int

currentSegment

​(float[] coords)

Returns the coordinates and type of the current path segment in
the iteration.

int

getWindingRule

()

Returns the winding rule for determining the interior of the
path.

boolean

isDone

()

Tests if the iteration is complete.

void

next

()

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

Field Summary

Fields

Modifier and Type

Field

Description

static int

SEG_CLOSE

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

static int

SEG_CUBICTO

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.

static int

SEG_LINETO

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

static int

SEG_MOVETO

The segment type constant for a point that specifies the
starting location for a new subpath.

static int

SEG_QUADTO

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.

static int

WIND_EVEN_ODD

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.

static int

WIND_NON_ZERO

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.

---

#### Field Summary

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

The segment type constant for a point that specifies the
starting location for a new subpath.

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

currentSegment

​(double[] coords)

Returns the coordinates and type of the current path segment in
the iteration.

int

currentSegment

​(float[] coords)

Returns the coordinates and type of the current path segment in
the iteration.

int

getWindingRule

()

Returns the winding rule for determining the interior of the
path.

boolean

isDone

()

Tests if the iteration is complete.

void

next

()

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

---

#### Method Summary

Returns the coordinates and type of the current path segment in
the iteration.

Returns the winding rule for determining the interior of the
path.

Tests if the iteration is complete.

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

============ FIELD DETAIL ===========

- Field Detail

- WIND_EVEN_ODD

```java
@Native

static final int WIND_EVEN_ODD
```

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.
The even-odd rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments an odd number of times.

**See Also:** Constant Field Values

- WIND_NON_ZERO

```java
@Native

static final int WIND_NON_ZERO
```

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.
The non-zero rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments a different number
of times in the counter-clockwise direction than the
clockwise direction.

**See Also:** Constant Field Values

- SEG_MOVETO

```java
@Native

static final int SEG_MOVETO
```

The segment type constant for a point that specifies the
starting location for a new subpath.

**See Also:** Constant Field Values

- SEG_LINETO

```java
@Native

static final int SEG_LINETO
```

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

**See Also:** Constant Field Values

- SEG_QUADTO

```java
@Native

static final int SEG_QUADTO
```

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
and the final interpolated control point (P2).
The parametric control equation for this curve is:

```java
P(t) = B(2,0)*CP + B(2,1)*P1 + B(2,2)*P2
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

**See Also:** Constant Field Values

- SEG_CUBICTO

```java
@Native

static final int SEG_CUBICTO
```

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
the second control point (P2),
and the final interpolated control point (P3).
The parametric control equation for this curve is:

```java
P(t) = B(3,0)*CP + B(3,1)*P1 + B(3,2)*P2 + B(3,3)*P3
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

This form of curve is commonly known as a Bézier curve.

**See Also:** Constant Field Values

- SEG_CLOSE

```java
@Native

static final int SEG_CLOSE
```

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getWindingRule

```java
int getWindingRule()
```

Returns the winding rule for determining the interior of the
path.

**Returns:** the winding rule.
**See Also:** WIND_EVEN_ODD

,

WIND_NON_ZERO

- isDone

```java
boolean isDone()
```

Tests if the iteration is complete.

**Returns:** true

if all the segments have
been read;

false

otherwise.

- next

```java
void next()
```

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

- currentSegment

```java
int currentSegment​(float[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path-segment type of the current path segment.
**See Also:** SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

- currentSegment

```java
int currentSegment​(double[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path-segment type of the current path segment.
**See Also:** SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

Field Detail

- WIND_EVEN_ODD

```java
@Native

static final int WIND_EVEN_ODD
```

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.
The even-odd rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments an odd number of times.

**See Also:** Constant Field Values

- WIND_NON_ZERO

```java
@Native

static final int WIND_NON_ZERO
```

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.
The non-zero rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments a different number
of times in the counter-clockwise direction than the
clockwise direction.

**See Also:** Constant Field Values

- SEG_MOVETO

```java
@Native

static final int SEG_MOVETO
```

The segment type constant for a point that specifies the
starting location for a new subpath.

**See Also:** Constant Field Values

- SEG_LINETO

```java
@Native

static final int SEG_LINETO
```

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

**See Also:** Constant Field Values

- SEG_QUADTO

```java
@Native

static final int SEG_QUADTO
```

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
and the final interpolated control point (P2).
The parametric control equation for this curve is:

```java
P(t) = B(2,0)*CP + B(2,1)*P1 + B(2,2)*P2
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

**See Also:** Constant Field Values

- SEG_CUBICTO

```java
@Native

static final int SEG_CUBICTO
```

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
the second control point (P2),
and the final interpolated control point (P3).
The parametric control equation for this curve is:

```java
P(t) = B(3,0)*CP + B(3,1)*P1 + B(3,2)*P2 + B(3,3)*P3
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

This form of curve is commonly known as a Bézier curve.

**See Also:** Constant Field Values

- SEG_CLOSE

```java
@Native

static final int SEG_CLOSE
```

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

**See Also:** Constant Field Values

---

#### Field Detail

WIND_EVEN_ODD

```java
@Native

static final int WIND_EVEN_ODD
```

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.
The even-odd rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments an odd number of times.

**See Also:** Constant Field Values

---

#### WIND_EVEN_ODD

@Native

static final int WIND_EVEN_ODD

The winding rule constant for specifying an even-odd rule
for determining the interior of a path.
The even-odd rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments an odd number of times.

WIND_NON_ZERO

```java
@Native

static final int WIND_NON_ZERO
```

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.
The non-zero rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments a different number
of times in the counter-clockwise direction than the
clockwise direction.

**See Also:** Constant Field Values

---

#### WIND_NON_ZERO

@Native

static final int WIND_NON_ZERO

The winding rule constant for specifying a non-zero rule
for determining the interior of a path.
The non-zero rule specifies that a point lies inside the
path if a ray drawn in any direction from that point to
infinity is crossed by path segments a different number
of times in the counter-clockwise direction than the
clockwise direction.

SEG_MOVETO

```java
@Native

static final int SEG_MOVETO
```

The segment type constant for a point that specifies the
starting location for a new subpath.

**See Also:** Constant Field Values

---

#### SEG_MOVETO

@Native

static final int SEG_MOVETO

The segment type constant for a point that specifies the
starting location for a new subpath.

SEG_LINETO

```java
@Native

static final int SEG_LINETO
```

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

**See Also:** Constant Field Values

---

#### SEG_LINETO

@Native

static final int SEG_LINETO

The segment type constant for a point that specifies the
end point of a line to be drawn from the most recently
specified point.

SEG_QUADTO

```java
@Native

static final int SEG_QUADTO
```

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
and the final interpolated control point (P2).
The parametric control equation for this curve is:

```java
P(t) = B(2,0)*CP + B(2,1)*P1 + B(2,2)*P2
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

**See Also:** Constant Field Values

---

#### SEG_QUADTO

@Native

static final int SEG_QUADTO

The segment type constant for the pair of points that specify
a quadratic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
and the final interpolated control point (P2).
The parametric control equation for this curve is:

```java
P(t) = B(2,0)*CP + B(2,1)*P1 + B(2,2)*P2
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

P(t) = B(2,0)*CP + B(2,1)*P1 + B(2,2)*P2
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)

SEG_CUBICTO

```java
@Native

static final int SEG_CUBICTO
```

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
the second control point (P2),
and the final interpolated control point (P3).
The parametric control equation for this curve is:

```java
P(t) = B(3,0)*CP + B(3,1)*P1 + B(3,2)*P2 + B(3,3)*P3
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

This form of curve is commonly known as a Bézier curve.

**See Also:** Constant Field Values

---

#### SEG_CUBICTO

@Native

static final int SEG_CUBICTO

The segment type constant for the set of 3 points that specify
a cubic parametric curve to be drawn from the most recently
specified point.
The curve is interpolated by solving the parametric control
equation in the range

(t=[0..1])

using
the most recently specified (current) point (CP),
the first control point (P1),
the second control point (P2),
and the final interpolated control point (P3).
The parametric control equation for this curve is:

```java
P(t) = B(3,0)*CP + B(3,1)*P1 + B(3,2)*P2 + B(3,3)*P3
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)
```

This form of curve is commonly known as a Bézier curve.

P(t) = B(3,0)*CP + B(3,1)*P1 + B(3,2)*P2 + B(3,3)*P3
0 <= t <= 1

B(n,m) = mth coefficient of nth degree Bernstein polynomial
= C(n,m) * t^(m) * (1 - t)^(n-m)
C(n,m) = Combinations of n things, taken m at a time
= n! / (m! * (n-m)!)

SEG_CLOSE

```java
@Native

static final int SEG_CLOSE
```

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

**See Also:** Constant Field Values

---

#### SEG_CLOSE

@Native

static final int SEG_CLOSE

The segment type constant that specifies that
the preceding subpath should be closed by appending a line segment
back to the point corresponding to the most recent SEG_MOVETO.

Method Detail

- getWindingRule

```java
int getWindingRule()
```

Returns the winding rule for determining the interior of the
path.

**Returns:** the winding rule.
**See Also:** WIND_EVEN_ODD

,

WIND_NON_ZERO

- isDone

```java
boolean isDone()
```

Tests if the iteration is complete.

**Returns:** true

if all the segments have
been read;

false

otherwise.

- next

```java
void next()
```

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

- currentSegment

```java
int currentSegment​(float[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path-segment type of the current path segment.
**See Also:** SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

- currentSegment

```java
int currentSegment​(double[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path-segment type of the current path segment.
**See Also:** SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

---

#### Method Detail

getWindingRule

```java
int getWindingRule()
```

Returns the winding rule for determining the interior of the
path.

**Returns:** the winding rule.
**See Also:** WIND_EVEN_ODD

,

WIND_NON_ZERO

---

#### getWindingRule

int getWindingRule()

Returns the winding rule for determining the interior of the
path.

isDone

```java
boolean isDone()
```

Tests if the iteration is complete.

**Returns:** true

if all the segments have
been read;

false

otherwise.

---

#### isDone

boolean isDone()

Tests if the iteration is complete.

next

```java
void next()
```

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

---

#### next

void next()

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

currentSegment

```java
int currentSegment​(float[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path-segment type of the current path segment.
**See Also:** SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

---

#### currentSegment

int currentSegment​(float[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

currentSegment

```java
int currentSegment​(double[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path-segment type of the current path segment.
**See Also:** SEG_MOVETO

,

SEG_LINETO

,

SEG_QUADTO

,

SEG_CUBICTO

,

SEG_CLOSE

---

#### currentSegment

int currentSegment​(double[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path-segment type:
SEG_MOVETO, SEG_LINETO, SEG_QUADTO, SEG_CUBICTO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types returns one point,
SEG_QUADTO returns two points,
SEG_CUBICTO returns 3 points
and SEG_CLOSE does not return any points.

---

