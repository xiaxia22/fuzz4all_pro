# Class Ellipse2D

**Source:** `java.desktop\java\awt\geom\Ellipse2D.html`

### Class Description

```java
public abstract class
Ellipse2D

extends
RectangularShape
```

The

Ellipse2D

class describes an ellipse that is defined
by a framing rectangle.

This class is only the abstract superclass for all objects which
store a 2D ellipse.
The actual storage representation of the coordinates is left to
the subclass.

**All Implemented Interfaces:** Shape

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Ellipse2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**See Also:**
- Ellipse2D.Float

,

Ellipse2D.Double

**Since:**
- 1.2

---

### Method Details

#### public boolean contains​(double x,
double y)

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

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

#### public
PathIterator
getPathIterator​(
AffineTransform
at)

Returns an iteration object that defines the boundary of this

Ellipse2D

.
The iterator for this class is multi-threaded safe, which means
that this

Ellipse2D

class guarantees that
modifications to the geometry of this

Ellipse2D

object do not affect any iterations of that geometry that
are already in process.

**Parameters:**
- at

- an optional

AffineTransform

to be applied to
the coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired

**Returns:**
- the

PathIterator

object that returns the
geometry of the outline of this

Ellipse2D

,
one segment at a time.

**Since:**
- 1.2

---

#### public int hashCode()

Returns the hashcode for this

Ellipse2D

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hashcode for this

Ellipse2D

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.6

---

#### public boolean equals​(
Object
obj)

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

. The specified

Object

is equal to this

Ellipse2D

if it is an instance of

Ellipse2D

and if its
location and size are the same as this

Ellipse2D

.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- an

Object

to be compared with this

Ellipse2D

.

**Returns:**
- true

if

obj

is an instance
of

Ellipse2D

and has the same values;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.6

---

### Additional Sections

#### Class Ellipse2D

java.lang.Object

- java.awt.geom.RectangularShape
- - java.awt.geom.Ellipse2D

java.awt.geom.RectangularShape

- java.awt.geom.Ellipse2D

java.awt.geom.Ellipse2D

**All Implemented Interfaces:** Shape

,

Cloneable

**Direct Known Subclasses:** Ellipse2D.Double

,

Ellipse2D.Float

```java
public abstract class
Ellipse2D

extends
RectangularShape
```

The

Ellipse2D

class describes an ellipse that is defined
by a framing rectangle.

This class is only the abstract superclass for all objects which
store a 2D ellipse.
The actual storage representation of the coordinates is left to
the subclass.

**Since:** 1.2

public abstract class

Ellipse2D

extends

RectangularShape

The

Ellipse2D

class describes an ellipse that is defined
by a framing rectangle.

This class is only the abstract superclass for all objects which
store a 2D ellipse.
The actual storage representation of the coordinates is left to
the subclass.

This class is only the abstract superclass for all objects which
store a 2D ellipse.
The actual storage representation of the coordinates is left to
the subclass.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Ellipse2D.Double

The

Double

class defines an ellipse specified
in

double

precision.

static class

Ellipse2D.Float

The

Float

class defines an ellipse specified
in

float

precision.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Ellipse2D

()

This is an abstract class that cannot be instantiated directly.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

equals

​(

Object

obj)

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

.

PathIterator

getPathIterator

​(

AffineTransform

at)

Returns an iteration object that defines the boundary of this

Ellipse2D

.

int

hashCode

()

Returns the hashcode for this

Ellipse2D

.

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

getHeight

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

getPathIterator

,

getWidth

,

getX

,

getY

,

intersects

,

isEmpty

,

setFrame

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

Ellipse2D.Double

The

Double

class defines an ellipse specified
in

double

precision.

static class

Ellipse2D.Float

The

Float

class defines an ellipse specified
in

float

precision.

---

#### Nested Class Summary

The

Double

class defines an ellipse specified
in

double

precision.

The

Float

class defines an ellipse specified
in

float

precision.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Ellipse2D

()

This is an abstract class that cannot be instantiated directly.

---

#### Constructor Summary

This is an abstract class that cannot be instantiated directly.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

equals

​(

Object

obj)

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

.

PathIterator

getPathIterator

​(

AffineTransform

at)

Returns an iteration object that defines the boundary of this

Ellipse2D

.

int

hashCode

()

Returns the hashcode for this

Ellipse2D

.

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

getHeight

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

getPathIterator

,

getWidth

,

getX

,

getY

,

intersects

,

isEmpty

,

setFrame

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

Tests if the specified coordinates are inside the boundary of the

Shape

, as described by the

definition of insideness

.

Tests if the interior of the

Shape

entirely contains
the specified rectangular area.

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

.

Returns an iteration object that defines the boundary of this

Ellipse2D

.

Returns the hashcode for this

Ellipse2D

.

Tests if the interior of the

Shape

intersects the
interior of a specified rectangular area.

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

getHeight

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

getPathIterator

,

getWidth

,

getX

,

getY

,

intersects

,

isEmpty

,

setFrame

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

- Ellipse2D

```java
protected Ellipse2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Ellipse2D.Float

,

Ellipse2D.Double

============ METHOD DETAIL ==========

- Method Detail

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

- getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at)
```

Returns an iteration object that defines the boundary of this

Ellipse2D

.
The iterator for this class is multi-threaded safe, which means
that this

Ellipse2D

class guarantees that
modifications to the geometry of this

Ellipse2D

object do not affect any iterations of that geometry that
are already in process.

**Parameters:** at

- an optional

AffineTransform

to be applied to
the coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

Ellipse2D

,
one segment at a time.
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this

Ellipse2D

.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode for this

Ellipse2D

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

. The specified

Object

is equal to this

Ellipse2D

if it is an instance of

Ellipse2D

and if its
location and size are the same as this

Ellipse2D

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- an

Object

to be compared with this

Ellipse2D

.
**Returns:** true

if

obj

is an instance
of

Ellipse2D

and has the same values;

false

otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- Ellipse2D

```java
protected Ellipse2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Ellipse2D.Float

,

Ellipse2D.Double

---

#### Constructor Detail

Ellipse2D

```java
protected Ellipse2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Ellipse2D.Float

,

Ellipse2D.Double

---

#### Ellipse2D

protected Ellipse2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

Method Detail

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

- getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at)
```

Returns an iteration object that defines the boundary of this

Ellipse2D

.
The iterator for this class is multi-threaded safe, which means
that this

Ellipse2D

class guarantees that
modifications to the geometry of this

Ellipse2D

object do not affect any iterations of that geometry that
are already in process.

**Parameters:** at

- an optional

AffineTransform

to be applied to
the coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

Ellipse2D

,
one segment at a time.
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this

Ellipse2D

.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode for this

Ellipse2D

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

. The specified

Object

is equal to this

Ellipse2D

if it is an instance of

Ellipse2D

and if its
location and size are the same as this

Ellipse2D

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- an

Object

to be compared with this

Ellipse2D

.
**Returns:** true

if

obj

is an instance
of

Ellipse2D

and has the same values;

false

otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

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

getPathIterator

```java
public
PathIterator
getPathIterator​(
AffineTransform
at)
```

Returns an iteration object that defines the boundary of this

Ellipse2D

.
The iterator for this class is multi-threaded safe, which means
that this

Ellipse2D

class guarantees that
modifications to the geometry of this

Ellipse2D

object do not affect any iterations of that geometry that
are already in process.

**Parameters:** at

- an optional

AffineTransform

to be applied to
the coordinates as they are returned in the iteration, or

null

if untransformed coordinates are desired
**Returns:** the

PathIterator

object that returns the
geometry of the outline of this

Ellipse2D

,
one segment at a time.
**Since:** 1.2

---

#### getPathIterator

public

PathIterator

getPathIterator​(

AffineTransform

at)

Returns an iteration object that defines the boundary of this

Ellipse2D

.
The iterator for this class is multi-threaded safe, which means
that this

Ellipse2D

class guarantees that
modifications to the geometry of this

Ellipse2D

object do not affect any iterations of that geometry that
are already in process.

hashCode

```java
public int hashCode()
```

Returns the hashcode for this

Ellipse2D

.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode for this

Ellipse2D

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashcode for this

Ellipse2D

.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

. The specified

Object

is equal to this

Ellipse2D

if it is an instance of

Ellipse2D

and if its
location and size are the same as this

Ellipse2D

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- an

Object

to be compared with this

Ellipse2D

.
**Returns:** true

if

obj

is an instance
of

Ellipse2D

and has the same values;

false

otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Determines whether or not the specified

Object

is
equal to this

Ellipse2D

. The specified

Object

is equal to this

Ellipse2D

if it is an instance of

Ellipse2D

and if its
location and size are the same as this

Ellipse2D

.

---

