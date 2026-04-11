# Class FlatteningPathIterator

**Source:** `java.desktop\java\awt\geom\FlatteningPathIterator.html`

### Class Description

```java
public class
FlatteningPathIterator

extends
Object

implements
PathIterator
```

The

FlatteningPathIterator

class returns a flattened view of
another

PathIterator

object. Other

Shape

classes can use this class to provide flattening behavior for their paths
without having to perform the interpolation calculations themselves.

**All Implemented Interfaces:** PathIterator

---

### Field Details

*No entries found.*

### Constructor Details

#### public FlatteningPathIterator​(
PathIterator
src,
double flatness)

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it. The iterator does not
subdivide any curve read from the source iterator to more than
10 levels of subdivision which yields a maximum of 1024 line
segments per curve.

**Parameters:**
- src

- the original unflattened path being iterated over
- flatness

- the maximum allowable distance between the
control points and the flattened curve

---

#### public FlatteningPathIterator​(
PathIterator
src,
double flatness,
int limit)

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.
The

limit

parameter allows you to control the
maximum number of recursive subdivisions that the iterator
can make before it assumes that the curve is flat enough
without measuring against the

flatness

parameter.
The flattened iteration therefore never generates more than
a maximum of

(2^limit)

line segments per curve.

**Parameters:**
- src

- the original unflattened path being iterated over
- flatness

- the maximum allowable distance between the
control points and the flattened curve
- limit

- the maximum number of recursive subdivisions
allowed for any curved segment

**Throws:**
- IllegalArgumentException

- if

flatness

or

limit

is less than zero

---

### Method Details

#### public double getFlatness()

Returns the flatness of this iterator.

**Returns:**
- the flatness of this

FlatteningPathIterator

.

---

#### public int getRecursionLimit()

Returns the recursion limit of this iterator.

**Returns:**
- the recursion limit of this

FlatteningPathIterator

.

---

#### public int getWindingRule()

Returns the winding rule for determining the interior of the
path.

**Specified by:**
- getWindingRule

in interface

PathIterator

**Returns:**
- the winding rule of the original unflattened path being
iterated over.

**See Also:**
- PathIterator.WIND_EVEN_ODD

,

PathIterator.WIND_NON_ZERO

---

#### public boolean isDone()

Tests if the iteration is complete.

**Specified by:**
- isDone

in interface

PathIterator

**Returns:**
- true

if all the segments have
been read;

false

otherwise.

---

#### public void next()

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

**Specified by:**
- next

in interface

PathIterator

---

#### public int currentSegment​(float[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:**
- currentSegment

in interface

PathIterator

**Parameters:**
- coords

- an array that holds the data returned from
this method

**Returns:**
- the path segment type of the current path segment.

**Throws:**
- NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.

**See Also:**
- PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

---

#### public int currentSegment​(double[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:**
- currentSegment

in interface

PathIterator

**Parameters:**
- coords

- an array that holds the data returned from
this method

**Returns:**
- the path segment type of the current path segment.

**Throws:**
- NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.

**See Also:**
- PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

---

### Additional Sections

#### Class FlatteningPathIterator

java.lang.Object

- java.awt.geom.FlatteningPathIterator

java.awt.geom.FlatteningPathIterator

**All Implemented Interfaces:** PathIterator

```java
public class
FlatteningPathIterator

extends
Object

implements
PathIterator
```

The

FlatteningPathIterator

class returns a flattened view of
another

PathIterator

object. Other

Shape

classes can use this class to provide flattening behavior for their paths
without having to perform the interpolation calculations themselves.

public class

FlatteningPathIterator

extends

Object

implements

PathIterator

The

FlatteningPathIterator

class returns a flattened view of
another

PathIterator

object. Other

Shape

classes can use this class to provide flattening behavior for their paths
without having to perform the interpolation calculations themselves.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.awt.geom.

PathIterator

SEG_CLOSE

,

SEG_CUBICTO

,

SEG_LINETO

,

SEG_MOVETO

,

SEG_QUADTO

,

WIND_EVEN_ODD

,

WIND_NON_ZERO

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FlatteningPathIterator

​(

PathIterator

src,
double flatness)

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it.

FlatteningPathIterator

​(

PathIterator

src,
double flatness,
int limit)

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

double

getFlatness

()

Returns the flatness of this iterator.

int

getRecursionLimit

()

Returns the recursion limit of this iterator.

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

- Fields declared in interface java.awt.geom.

PathIterator

SEG_CLOSE

,

SEG_CUBICTO

,

SEG_LINETO

,

SEG_MOVETO

,

SEG_QUADTO

,

WIND_EVEN_ODD

,

WIND_NON_ZERO

---

#### Field Summary

Fields declared in interface java.awt.geom.

PathIterator

SEG_CLOSE

,

SEG_CUBICTO

,

SEG_LINETO

,

SEG_MOVETO

,

SEG_QUADTO

,

WIND_EVEN_ODD

,

WIND_NON_ZERO

---

#### Fields declared in interface java.awt.geom. PathIterator

Constructor Summary

Constructors

Constructor

Description

FlatteningPathIterator

​(

PathIterator

src,
double flatness)

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it.

FlatteningPathIterator

​(

PathIterator

src,
double flatness,
int limit)

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.

---

#### Constructor Summary

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it.

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.

Method Summary

All Methods

Instance Methods

Concrete Methods

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

double

getFlatness

()

Returns the flatness of this iterator.

int

getRecursionLimit

()

Returns the recursion limit of this iterator.

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

Returns the coordinates and type of the current path segment in
the iteration.

Returns the flatness of this iterator.

Returns the recursion limit of this iterator.

Returns the winding rule for determining the interior of the
path.

Tests if the iteration is complete.

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

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

- FlatteningPathIterator

```java
public FlatteningPathIterator​(
PathIterator
src,
double flatness)
```

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it. The iterator does not
subdivide any curve read from the source iterator to more than
10 levels of subdivision which yields a maximum of 1024 line
segments per curve.

**Parameters:** src

- the original unflattened path being iterated over
**Parameters:** flatness

- the maximum allowable distance between the
control points and the flattened curve

- FlatteningPathIterator

```java
public FlatteningPathIterator​(
PathIterator
src,
double flatness,
int limit)
```

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.
The

limit

parameter allows you to control the
maximum number of recursive subdivisions that the iterator
can make before it assumes that the curve is flat enough
without measuring against the

flatness

parameter.
The flattened iteration therefore never generates more than
a maximum of

(2^limit)

line segments per curve.

**Parameters:** src

- the original unflattened path being iterated over
**Parameters:** flatness

- the maximum allowable distance between the
control points and the flattened curve
**Parameters:** limit

- the maximum number of recursive subdivisions
allowed for any curved segment
**Throws:** IllegalArgumentException

- if

flatness

or

limit

is less than zero

============ METHOD DETAIL ==========

- Method Detail

- getFlatness

```java
public double getFlatness()
```

Returns the flatness of this iterator.

**Returns:** the flatness of this

FlatteningPathIterator

.

- getRecursionLimit

```java
public int getRecursionLimit()
```

Returns the recursion limit of this iterator.

**Returns:** the recursion limit of this

FlatteningPathIterator

.

- getWindingRule

```java
public int getWindingRule()
```

Returns the winding rule for determining the interior of the
path.

**Specified by:** getWindingRule

in interface

PathIterator
**Returns:** the winding rule of the original unflattened path being
iterated over.
**See Also:** PathIterator.WIND_EVEN_ODD

,

PathIterator.WIND_NON_ZERO

- isDone

```java
public boolean isDone()
```

Tests if the iteration is complete.

**Specified by:** isDone

in interface

PathIterator
**Returns:** true

if all the segments have
been read;

false

otherwise.

- next

```java
public void next()
```

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

**Specified by:** next

in interface

PathIterator

- currentSegment

```java
public int currentSegment​(float[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:** currentSegment

in interface

PathIterator
**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path segment type of the current path segment.
**Throws:** NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.
**See Also:** PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

- currentSegment

```java
public int currentSegment​(double[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:** currentSegment

in interface

PathIterator
**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path segment type of the current path segment.
**Throws:** NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.
**See Also:** PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

Constructor Detail

- FlatteningPathIterator

```java
public FlatteningPathIterator​(
PathIterator
src,
double flatness)
```

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it. The iterator does not
subdivide any curve read from the source iterator to more than
10 levels of subdivision which yields a maximum of 1024 line
segments per curve.

**Parameters:** src

- the original unflattened path being iterated over
**Parameters:** flatness

- the maximum allowable distance between the
control points and the flattened curve

- FlatteningPathIterator

```java
public FlatteningPathIterator​(
PathIterator
src,
double flatness,
int limit)
```

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.
The

limit

parameter allows you to control the
maximum number of recursive subdivisions that the iterator
can make before it assumes that the curve is flat enough
without measuring against the

flatness

parameter.
The flattened iteration therefore never generates more than
a maximum of

(2^limit)

line segments per curve.

**Parameters:** src

- the original unflattened path being iterated over
**Parameters:** flatness

- the maximum allowable distance between the
control points and the flattened curve
**Parameters:** limit

- the maximum number of recursive subdivisions
allowed for any curved segment
**Throws:** IllegalArgumentException

- if

flatness

or

limit

is less than zero

---

#### Constructor Detail

FlatteningPathIterator

```java
public FlatteningPathIterator​(
PathIterator
src,
double flatness)
```

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it. The iterator does not
subdivide any curve read from the source iterator to more than
10 levels of subdivision which yields a maximum of 1024 line
segments per curve.

**Parameters:** src

- the original unflattened path being iterated over
**Parameters:** flatness

- the maximum allowable distance between the
control points and the flattened curve

---

#### FlatteningPathIterator

public FlatteningPathIterator​(

PathIterator

src,
double flatness)

Constructs a new

FlatteningPathIterator

object that
flattens a path as it iterates over it. The iterator does not
subdivide any curve read from the source iterator to more than
10 levels of subdivision which yields a maximum of 1024 line
segments per curve.

FlatteningPathIterator

```java
public FlatteningPathIterator​(
PathIterator
src,
double flatness,
int limit)
```

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.
The

limit

parameter allows you to control the
maximum number of recursive subdivisions that the iterator
can make before it assumes that the curve is flat enough
without measuring against the

flatness

parameter.
The flattened iteration therefore never generates more than
a maximum of

(2^limit)

line segments per curve.

**Parameters:** src

- the original unflattened path being iterated over
**Parameters:** flatness

- the maximum allowable distance between the
control points and the flattened curve
**Parameters:** limit

- the maximum number of recursive subdivisions
allowed for any curved segment
**Throws:** IllegalArgumentException

- if

flatness

or

limit

is less than zero

---

#### FlatteningPathIterator

public FlatteningPathIterator​(

PathIterator

src,
double flatness,
int limit)

Constructs a new

FlatteningPathIterator

object
that flattens a path as it iterates over it.
The

limit

parameter allows you to control the
maximum number of recursive subdivisions that the iterator
can make before it assumes that the curve is flat enough
without measuring against the

flatness

parameter.
The flattened iteration therefore never generates more than
a maximum of

(2^limit)

line segments per curve.

Method Detail

- getFlatness

```java
public double getFlatness()
```

Returns the flatness of this iterator.

**Returns:** the flatness of this

FlatteningPathIterator

.

- getRecursionLimit

```java
public int getRecursionLimit()
```

Returns the recursion limit of this iterator.

**Returns:** the recursion limit of this

FlatteningPathIterator

.

- getWindingRule

```java
public int getWindingRule()
```

Returns the winding rule for determining the interior of the
path.

**Specified by:** getWindingRule

in interface

PathIterator
**Returns:** the winding rule of the original unflattened path being
iterated over.
**See Also:** PathIterator.WIND_EVEN_ODD

,

PathIterator.WIND_NON_ZERO

- isDone

```java
public boolean isDone()
```

Tests if the iteration is complete.

**Specified by:** isDone

in interface

PathIterator
**Returns:** true

if all the segments have
been read;

false

otherwise.

- next

```java
public void next()
```

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

**Specified by:** next

in interface

PathIterator

- currentSegment

```java
public int currentSegment​(float[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:** currentSegment

in interface

PathIterator
**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path segment type of the current path segment.
**Throws:** NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.
**See Also:** PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

- currentSegment

```java
public int currentSegment​(double[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:** currentSegment

in interface

PathIterator
**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path segment type of the current path segment.
**Throws:** NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.
**See Also:** PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

---

#### Method Detail

getFlatness

```java
public double getFlatness()
```

Returns the flatness of this iterator.

**Returns:** the flatness of this

FlatteningPathIterator

.

---

#### getFlatness

public double getFlatness()

Returns the flatness of this iterator.

getRecursionLimit

```java
public int getRecursionLimit()
```

Returns the recursion limit of this iterator.

**Returns:** the recursion limit of this

FlatteningPathIterator

.

---

#### getRecursionLimit

public int getRecursionLimit()

Returns the recursion limit of this iterator.

getWindingRule

```java
public int getWindingRule()
```

Returns the winding rule for determining the interior of the
path.

**Specified by:** getWindingRule

in interface

PathIterator
**Returns:** the winding rule of the original unflattened path being
iterated over.
**See Also:** PathIterator.WIND_EVEN_ODD

,

PathIterator.WIND_NON_ZERO

---

#### getWindingRule

public int getWindingRule()

Returns the winding rule for determining the interior of the
path.

isDone

```java
public boolean isDone()
```

Tests if the iteration is complete.

**Specified by:** isDone

in interface

PathIterator
**Returns:** true

if all the segments have
been read;

false

otherwise.

---

#### isDone

public boolean isDone()

Tests if the iteration is complete.

next

```java
public void next()
```

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

**Specified by:** next

in interface

PathIterator

---

#### next

public void next()

Moves the iterator to the next segment of the path forwards
along the primary direction of traversal as long as there are
more points in that direction.

currentSegment

```java
public int currentSegment​(float[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:** currentSegment

in interface

PathIterator
**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path segment type of the current path segment.
**Throws:** NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.
**See Also:** PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

---

#### currentSegment

public int currentSegment​(float[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A float array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of float x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

currentSegment

```java
public int currentSegment​(double[] coords)
```

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

**Specified by:** currentSegment

in interface

PathIterator
**Parameters:** coords

- an array that holds the data returned from
this method
**Returns:** the path segment type of the current path segment.
**Throws:** NoSuchElementException

- if there
are no more elements in the flattening path to be
returned.
**See Also:** PathIterator.SEG_MOVETO

,

PathIterator.SEG_LINETO

,

PathIterator.SEG_CLOSE

---

#### currentSegment

public int currentSegment​(double[] coords)

Returns the coordinates and type of the current path segment in
the iteration.
The return value is the path segment type:
SEG_MOVETO, SEG_LINETO, or SEG_CLOSE.
A double array of length 6 must be passed in and can be used to
store the coordinates of the point(s).
Each point is stored as a pair of double x,y coordinates.
SEG_MOVETO and SEG_LINETO types return one point,
and SEG_CLOSE does not return any points.

---

