# Class Arc2D.Double

**Source:** `java.desktop\java\awt\geom\Arc2D.Double.html`

### Class Description

```java
public static class
Arc2D.Double

extends
Arc2D

implements
Serializable
```

This class defines an arc specified in

double

precision.

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

---

### Field Details

#### public double x

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:**
- 1.2

---

#### public double y

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:**
- 1.2

---

#### public double width

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:**
- 1.2

---

#### public double height

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:**
- 1.2

---

#### public double start

The starting angle of the arc in degrees.

**Since:**
- 1.2

---

#### public double extent

The angular extent of the arc in degrees.

**Since:**
- 1.2

---

### Constructor Details

#### public Double()

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

**Since:**
- 1.2

---

#### public Double​(int type)

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

**Parameters:**
- type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.

**Since:**
- 1.2

---

#### public Double​(double x,
double y,
double w,
double h,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:**
- x

- The X coordinate of the upper-left corner
of the arc's framing rectangle.
- y

- The Y coordinate of the upper-left corner
of the arc's framing rectangle.
- w

- The overall width of the full ellipse of which this
arc is a partial section.
- h

- The overall height of the full ellipse of which this
arc is a partial section.
- start

- The starting angle of the arc in degrees.
- extent

- The angular extent of the arc in degrees.
- type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.

**Since:**
- 1.2

---

#### public Double​(
Rectangle2D
ellipseBounds,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:**
- ellipseBounds

- The framing rectangle that defines the
outer boundary of the full ellipse of which this arc is a
partial section.
- start

- The starting angle of the arc in degrees.
- extent

- The angular extent of the arc in degrees.
- type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.

**Since:**
- 1.2

---

### Method Details

#### public double getX()

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

**Specified by:**
- getHeight

in class

RectangularShape

**Returns:**
- the height of the framing rectangle.

**Since:**
- 1.2

---

#### public double getAngleStart()

Returns the starting angle of the arc.

**Specified by:**
- getAngleStart

in class

Arc2D

**Returns:**
- A double value that represents the starting angle
of the arc in degrees.

**See Also:**
- Arc2D.setAngleStart(double)

**Since:**
- 1.2

---

#### public double getAngleExtent()

Returns the angular extent of the arc.

**Specified by:**
- getAngleExtent

in class

Arc2D

**Returns:**
- A double value that represents the angular extent
of the arc in degrees.

**See Also:**
- Arc2D.setAngleExtent(double)

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

#### public void setArc​(double x,
double y,
double w,
double h,
double angSt,
double angExt,
int closure)

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

**Specified by:**
- setArc

in class

Arc2D

**Parameters:**
- x

- The X coordinate of the upper-left corner of the arc.
- y

- The Y coordinate of the upper-left corner of the arc.
- w

- The overall width of the full ellipse of which
this arc is a partial section.
- h

- The overall height of the full ellipse of which
this arc is a partial section.
- angSt

- The starting angle of the arc in degrees.
- angExt

- The angular extent of the arc in degrees.
- closure

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.

**Since:**
- 1.2

---

#### public void setAngleStart​(double angSt)

Sets the starting angle of this arc to the specified double
value.

**Specified by:**
- setAngleStart

in class

Arc2D

**Parameters:**
- angSt

- The starting angle of the arc in degrees.

**See Also:**
- Arc2D.getAngleStart()

**Since:**
- 1.2

---

#### public void setAngleExtent​(double angExt)

Sets the angular extent of this arc to the specified double
value.

**Specified by:**
- setAngleExtent

in class

Arc2D

**Parameters:**
- angExt

- The angular extent of the arc in degrees.

**See Also:**
- Arc2D.getAngleExtent()

**Since:**
- 1.2

---

#### protected
Rectangle2D
makeBounds​(double x,
double y,
double w,
double h)

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

**Specified by:**
- makeBounds

in class

Arc2D

**Parameters:**
- x

- The X coordinate of the upper-left corner of the
framing rectangle.
- y

- The Y coordinate of the upper-left corner of the
framing rectangle.
- w

- The width of the framing rectangle.
- h

- The height of the framing rectangle.

**Returns:**
- a

Rectangle2D

that is the framing rectangle
of this arc.

**Since:**
- 1.2

---

### Additional Sections

#### Class Arc2D.Double

java.lang.Object

- java.awt.geom.RectangularShape
- - java.awt.geom.Arc2D
- - java.awt.geom.Arc2D.Double

java.awt.geom.RectangularShape

- java.awt.geom.Arc2D
- - java.awt.geom.Arc2D.Double

java.awt.geom.Arc2D

- java.awt.geom.Arc2D.Double

java.awt.geom.Arc2D.Double

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

**Enclosing class:** Arc2D

```java
public static class
Arc2D.Double

extends
Arc2D

implements
Serializable
```

This class defines an arc specified in

double

precision.

**Since:** 1.2
**See Also:** Serialized Form

public static class

Arc2D.Double

extends

Arc2D

implements

Serializable

This class defines an arc specified in

double

precision.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Arc2D

Arc2D.Double

,

Arc2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

double

extent

The angular extent of the arc in degrees.

double

height

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

double

start

The starting angle of the arc in degrees.

double

width

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

double

x

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

double

y

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

- Fields declared in class java.awt.geom.

Arc2D

CHORD

,

OPEN

,

PIE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Double

()

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

Double

​(double x,
double y,
double w,
double h,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

Double

​(int type)

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

Double

​(

Rectangle2D

ellipseBounds,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

double

getAngleExtent

()

Returns the angular extent of the arc.

double

getAngleStart

()

Returns the starting angle of the arc.

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

protected

Rectangle2D

makeBounds

​(double x,
double y,
double w,
double h)

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

void

setAngleExtent

​(double angExt)

Sets the angular extent of this arc to the specified double
value.

void

setAngleStart

​(double angSt)

Sets the starting angle of this arc to the specified double
value.

void

setArc

​(double x,
double y,
double w,
double h,
double angSt,
double angExt,
int closure)

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

- Methods declared in class java.awt.geom.

Arc2D

contains

,

contains

,

contains

,

containsAngle

,

equals

,

getArcType

,

getBounds2D

,

getEndPoint

,

getPathIterator

,

getStartPoint

,

hashCode

,

intersects

,

setAngles

,

setAngles

,

setAngleStart

,

setArc

,

setArc

,

setArc

,

setArcByCenter

,

setArcByTangent

,

setArcType

,

setFrame

- Methods declared in class java.awt.geom.

RectangularShape

clone

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

getPathIterator

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

toString

,

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Arc2D

Arc2D.Double

,

Arc2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

Arc2D

Arc2D.Double

,

Arc2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. Arc2D

Field Summary

Fields

Modifier and Type

Field

Description

double

extent

The angular extent of the arc in degrees.

double

height

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

double

start

The starting angle of the arc in degrees.

double

width

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

double

x

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

double

y

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

- Fields declared in class java.awt.geom.

Arc2D

CHORD

,

OPEN

,

PIE

---

#### Field Summary

The angular extent of the arc in degrees.

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

The starting angle of the arc in degrees.

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

Fields declared in class java.awt.geom.

Arc2D

CHORD

,

OPEN

,

PIE

---

#### Fields declared in class java.awt.geom. Arc2D

Constructor Summary

Constructors

Constructor

Description

Double

()

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

Double

​(double x,
double y,
double w,
double h,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

Double

​(int type)

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

Double

​(

Rectangle2D

ellipseBounds,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

---

#### Constructor Summary

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

double

getAngleExtent

()

Returns the angular extent of the arc.

double

getAngleStart

()

Returns the starting angle of the arc.

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

protected

Rectangle2D

makeBounds

​(double x,
double y,
double w,
double h)

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

void

setAngleExtent

​(double angExt)

Sets the angular extent of this arc to the specified double
value.

void

setAngleStart

​(double angSt)

Sets the starting angle of this arc to the specified double
value.

void

setArc

​(double x,
double y,
double w,
double h,
double angSt,
double angExt,
int closure)

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

- Methods declared in class java.awt.geom.

Arc2D

contains

,

contains

,

contains

,

containsAngle

,

equals

,

getArcType

,

getBounds2D

,

getEndPoint

,

getPathIterator

,

getStartPoint

,

hashCode

,

intersects

,

setAngles

,

setAngles

,

setAngleStart

,

setArc

,

setArc

,

setArc

,

setArcByCenter

,

setArcByTangent

,

setArcType

,

setFrame

- Methods declared in class java.awt.geom.

RectangularShape

clone

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

getPathIterator

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the angular extent of the arc.

Returns the starting angle of the arc.

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

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

Sets the angular extent of this arc to the specified double
value.

Sets the starting angle of this arc to the specified double
value.

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

Methods declared in class java.awt.geom.

Arc2D

contains

,

contains

,

contains

,

containsAngle

,

equals

,

getArcType

,

getBounds2D

,

getEndPoint

,

getPathIterator

,

getStartPoint

,

hashCode

,

intersects

,

setAngles

,

setAngles

,

setAngleStart

,

setArc

,

setArc

,

setArc

,

setArcByCenter

,

setArcByTangent

,

setArcType

,

setFrame

---

#### Methods declared in class java.awt.geom. Arc2D

Methods declared in class java.awt.geom.

RectangularShape

clone

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

getPathIterator

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

- x

```java
public double x
```

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:** 1.2

- y

```java
public double y
```

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:** 1.2

- width

```java
public double width
```

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:** 1.2

- height

```java
public double height
```

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:** 1.2

- start

```java
public double start
```

The starting angle of the arc in degrees.

**Since:** 1.2

- extent

```java
public double extent
```

The angular extent of the arc in degrees.

**Since:** 1.2

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Double

```java
public Double()
```

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

**Since:** 1.2

- Double

```java
public Double​(int type)
```

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

- Double

```java
public Double​(double x,
double y,
double w,
double h,
double start,
double extent,
int type)
```

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:** x

- The X coordinate of the upper-left corner
of the arc's framing rectangle.
**Parameters:** y

- The Y coordinate of the upper-left corner
of the arc's framing rectangle.
**Parameters:** w

- The overall width of the full ellipse of which this
arc is a partial section.
**Parameters:** h

- The overall height of the full ellipse of which this
arc is a partial section.
**Parameters:** start

- The starting angle of the arc in degrees.
**Parameters:** extent

- The angular extent of the arc in degrees.
**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

- Double

```java
public Double​(
Rectangle2D
ellipseBounds,
double start,
double extent,
int type)
```

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:** ellipseBounds

- The framing rectangle that defines the
outer boundary of the full ellipse of which this arc is a
partial section.
**Parameters:** start

- The starting angle of the arc in degrees.
**Parameters:** extent

- The angular extent of the arc in degrees.
**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

**Specified by:** getHeight

in class

RectangularShape
**Returns:** the height of the framing rectangle.
**Since:** 1.2

- getAngleStart

```java
public double getAngleStart()
```

Returns the starting angle of the arc.

**Specified by:** getAngleStart

in class

Arc2D
**Returns:** A double value that represents the starting angle
of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.setAngleStart(double)

- getAngleExtent

```java
public double getAngleExtent()
```

Returns the angular extent of the arc.

**Specified by:** getAngleExtent

in class

Arc2D
**Returns:** A double value that represents the angular extent
of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.setAngleExtent(double)

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

- setArc

```java
public void setArc​(double x,
double y,
double w,
double h,
double angSt,
double angExt,
int closure)
```

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

**Specified by:** setArc

in class

Arc2D
**Parameters:** x

- The X coordinate of the upper-left corner of the arc.
**Parameters:** y

- The Y coordinate of the upper-left corner of the arc.
**Parameters:** w

- The overall width of the full ellipse of which
this arc is a partial section.
**Parameters:** h

- The overall height of the full ellipse of which
this arc is a partial section.
**Parameters:** angSt

- The starting angle of the arc in degrees.
**Parameters:** angExt

- The angular extent of the arc in degrees.
**Parameters:** closure

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

- setAngleStart

```java
public void setAngleStart​(double angSt)
```

Sets the starting angle of this arc to the specified double
value.

**Specified by:** setAngleStart

in class

Arc2D
**Parameters:** angSt

- The starting angle of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.getAngleStart()

- setAngleExtent

```java
public void setAngleExtent​(double angExt)
```

Sets the angular extent of this arc to the specified double
value.

**Specified by:** setAngleExtent

in class

Arc2D
**Parameters:** angExt

- The angular extent of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.getAngleExtent()

- makeBounds

```java
protected
Rectangle2D
makeBounds​(double x,
double y,
double w,
double h)
```

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

**Specified by:** makeBounds

in class

Arc2D
**Parameters:** x

- The X coordinate of the upper-left corner of the
framing rectangle.
**Parameters:** y

- The Y coordinate of the upper-left corner of the
framing rectangle.
**Parameters:** w

- The width of the framing rectangle.
**Parameters:** h

- The height of the framing rectangle.
**Returns:** a

Rectangle2D

that is the framing rectangle
of this arc.
**Since:** 1.2

Field Detail

- x

```java
public double x
```

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:** 1.2

- y

```java
public double y
```

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:** 1.2

- width

```java
public double width
```

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:** 1.2

- height

```java
public double height
```

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:** 1.2

- start

```java
public double start
```

The starting angle of the arc in degrees.

**Since:** 1.2

- extent

```java
public double extent
```

The angular extent of the arc in degrees.

**Since:** 1.2

---

#### Field Detail

x

```java
public double x
```

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:** 1.2

---

#### x

public double x

The X coordinate of the upper-left corner of the framing
rectangle of the arc.

y

```java
public double y
```

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

**Since:** 1.2

---

#### y

public double y

The Y coordinate of the upper-left corner of the framing
rectangle of the arc.

width

```java
public double width
```

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:** 1.2

---

#### width

public double width

The overall width of the full ellipse of which this arc is
a partial section (not considering the angular extents).

height

```java
public double height
```

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

**Since:** 1.2

---

#### height

public double height

The overall height of the full ellipse of which this arc is
a partial section (not considering the angular extents).

start

```java
public double start
```

The starting angle of the arc in degrees.

**Since:** 1.2

---

#### start

public double start

The starting angle of the arc in degrees.

extent

```java
public double extent
```

The angular extent of the arc in degrees.

**Since:** 1.2

---

#### extent

public double extent

The angular extent of the arc in degrees.

Constructor Detail

- Double

```java
public Double()
```

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

**Since:** 1.2

- Double

```java
public Double​(int type)
```

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

- Double

```java
public Double​(double x,
double y,
double w,
double h,
double start,
double extent,
int type)
```

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:** x

- The X coordinate of the upper-left corner
of the arc's framing rectangle.
**Parameters:** y

- The Y coordinate of the upper-left corner
of the arc's framing rectangle.
**Parameters:** w

- The overall width of the full ellipse of which this
arc is a partial section.
**Parameters:** h

- The overall height of the full ellipse of which this
arc is a partial section.
**Parameters:** start

- The starting angle of the arc in degrees.
**Parameters:** extent

- The angular extent of the arc in degrees.
**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

- Double

```java
public Double​(
Rectangle2D
ellipseBounds,
double start,
double extent,
int type)
```

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:** ellipseBounds

- The framing rectangle that defines the
outer boundary of the full ellipse of which this arc is a
partial section.
**Parameters:** start

- The starting angle of the arc in degrees.
**Parameters:** extent

- The angular extent of the arc in degrees.
**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

---

#### Constructor Detail

Double

```java
public Double()
```

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

**Since:** 1.2

---

#### Double

public Double()

Constructs a new OPEN arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0).

Double

```java
public Double​(int type)
```

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

---

#### Double

public Double​(int type)

Constructs a new arc, initialized to location (0, 0),
size (0, 0), angular extents (start = 0, extent = 0), and
the specified closure type.

Double

```java
public Double​(double x,
double y,
double w,
double h,
double start,
double extent,
int type)
```

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:** x

- The X coordinate of the upper-left corner
of the arc's framing rectangle.
**Parameters:** y

- The Y coordinate of the upper-left corner
of the arc's framing rectangle.
**Parameters:** w

- The overall width of the full ellipse of which this
arc is a partial section.
**Parameters:** h

- The overall height of the full ellipse of which this
arc is a partial section.
**Parameters:** start

- The starting angle of the arc in degrees.
**Parameters:** extent

- The angular extent of the arc in degrees.
**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

---

#### Double

public Double​(double x,
double y,
double w,
double h,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

Double

```java
public Double​(
Rectangle2D
ellipseBounds,
double start,
double extent,
int type)
```

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

**Parameters:** ellipseBounds

- The framing rectangle that defines the
outer boundary of the full ellipse of which this arc is a
partial section.
**Parameters:** start

- The starting angle of the arc in degrees.
**Parameters:** extent

- The angular extent of the arc in degrees.
**Parameters:** type

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

---

#### Double

public Double​(

Rectangle2D

ellipseBounds,
double start,
double extent,
int type)

Constructs a new arc, initialized to the specified location,
size, angular extents, and closure type.

Method Detail

- getX

```java
public double getX()
```

Returns the X coordinate of the upper-left corner of
the framing rectangle in

double

precision.
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

**Specified by:** getHeight

in class

RectangularShape
**Returns:** the height of the framing rectangle.
**Since:** 1.2

- getAngleStart

```java
public double getAngleStart()
```

Returns the starting angle of the arc.

**Specified by:** getAngleStart

in class

Arc2D
**Returns:** A double value that represents the starting angle
of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.setAngleStart(double)

- getAngleExtent

```java
public double getAngleExtent()
```

Returns the angular extent of the arc.

**Specified by:** getAngleExtent

in class

Arc2D
**Returns:** A double value that represents the angular extent
of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.setAngleExtent(double)

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

- setArc

```java
public void setArc​(double x,
double y,
double w,
double h,
double angSt,
double angExt,
int closure)
```

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

**Specified by:** setArc

in class

Arc2D
**Parameters:** x

- The X coordinate of the upper-left corner of the arc.
**Parameters:** y

- The Y coordinate of the upper-left corner of the arc.
**Parameters:** w

- The overall width of the full ellipse of which
this arc is a partial section.
**Parameters:** h

- The overall height of the full ellipse of which
this arc is a partial section.
**Parameters:** angSt

- The starting angle of the arc in degrees.
**Parameters:** angExt

- The angular extent of the arc in degrees.
**Parameters:** closure

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

- setAngleStart

```java
public void setAngleStart​(double angSt)
```

Sets the starting angle of this arc to the specified double
value.

**Specified by:** setAngleStart

in class

Arc2D
**Parameters:** angSt

- The starting angle of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.getAngleStart()

- setAngleExtent

```java
public void setAngleExtent​(double angExt)
```

Sets the angular extent of this arc to the specified double
value.

**Specified by:** setAngleExtent

in class

Arc2D
**Parameters:** angExt

- The angular extent of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.getAngleExtent()

- makeBounds

```java
protected
Rectangle2D
makeBounds​(double x,
double y,
double w,
double h)
```

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

**Specified by:** makeBounds

in class

Arc2D
**Parameters:** x

- The X coordinate of the upper-left corner of the
framing rectangle.
**Parameters:** y

- The Y coordinate of the upper-left corner of the
framing rectangle.
**Parameters:** w

- The width of the framing rectangle.
**Parameters:** h

- The height of the framing rectangle.
**Returns:** a

Rectangle2D

that is the framing rectangle
of this arc.
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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

getY

```java
public double getY()
```

Returns the Y coordinate of the upper-left corner of
the framing rectangle in

double

precision.
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

getWidth

```java
public double getWidth()
```

Returns the width of the framing rectangle in

double

precision.
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

getHeight

```java
public double getHeight()
```

Returns the height of the framing rectangle
in

double

precision.
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

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
Note that the arc

partially inscribes

the framing rectangle of this

RectangularShape

.

getAngleStart

```java
public double getAngleStart()
```

Returns the starting angle of the arc.

**Specified by:** getAngleStart

in class

Arc2D
**Returns:** A double value that represents the starting angle
of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.setAngleStart(double)

---

#### getAngleStart

public double getAngleStart()

Returns the starting angle of the arc.

getAngleExtent

```java
public double getAngleExtent()
```

Returns the angular extent of the arc.

**Specified by:** getAngleExtent

in class

Arc2D
**Returns:** A double value that represents the angular extent
of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.setAngleExtent(double)

---

#### getAngleExtent

public double getAngleExtent()

Returns the angular extent of the arc.

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

setArc

```java
public void setArc​(double x,
double y,
double w,
double h,
double angSt,
double angExt,
int closure)
```

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

**Specified by:** setArc

in class

Arc2D
**Parameters:** x

- The X coordinate of the upper-left corner of the arc.
**Parameters:** y

- The Y coordinate of the upper-left corner of the arc.
**Parameters:** w

- The overall width of the full ellipse of which
this arc is a partial section.
**Parameters:** h

- The overall height of the full ellipse of which
this arc is a partial section.
**Parameters:** angSt

- The starting angle of the arc in degrees.
**Parameters:** angExt

- The angular extent of the arc in degrees.
**Parameters:** closure

- The closure type for the arc:

Arc2D.OPEN

,

Arc2D.CHORD

, or

Arc2D.PIE

.
**Since:** 1.2

---

#### setArc

public void setArc​(double x,
double y,
double w,
double h,
double angSt,
double angExt,
int closure)

Sets the location, size, angular extents, and closure type of
this arc to the specified double values.

setAngleStart

```java
public void setAngleStart​(double angSt)
```

Sets the starting angle of this arc to the specified double
value.

**Specified by:** setAngleStart

in class

Arc2D
**Parameters:** angSt

- The starting angle of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.getAngleStart()

---

#### setAngleStart

public void setAngleStart​(double angSt)

Sets the starting angle of this arc to the specified double
value.

setAngleExtent

```java
public void setAngleExtent​(double angExt)
```

Sets the angular extent of this arc to the specified double
value.

**Specified by:** setAngleExtent

in class

Arc2D
**Parameters:** angExt

- The angular extent of the arc in degrees.
**Since:** 1.2
**See Also:** Arc2D.getAngleExtent()

---

#### setAngleExtent

public void setAngleExtent​(double angExt)

Sets the angular extent of this arc to the specified double
value.

makeBounds

```java
protected
Rectangle2D
makeBounds​(double x,
double y,
double w,
double h)
```

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

**Specified by:** makeBounds

in class

Arc2D
**Parameters:** x

- The X coordinate of the upper-left corner of the
framing rectangle.
**Parameters:** y

- The Y coordinate of the upper-left corner of the
framing rectangle.
**Parameters:** w

- The width of the framing rectangle.
**Parameters:** h

- The height of the framing rectangle.
**Returns:** a

Rectangle2D

that is the framing rectangle
of this arc.
**Since:** 1.2

---

#### makeBounds

protected

Rectangle2D

makeBounds​(double x,
double y,
double w,
double h)

Constructs a

Rectangle2D

of the appropriate precision
to hold the parameters calculated to be the framing rectangle
of this arc.

---

