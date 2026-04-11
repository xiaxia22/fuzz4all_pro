# Class Ellipse2D.Float

**Source:** `java.desktop\java\awt\geom\Ellipse2D.Float.html`

### Class Description

```java
public static class
Ellipse2D.Float

extends
Ellipse2D

implements
Serializable
```

The

Float

class defines an ellipse specified
in

float

precision.

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

---

### Field Details

#### public float x

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:**
- 1.2

---

#### public float y

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:**
- 1.2

---

#### public float width

The overall width of this

Ellipse2D

.

**Since:**
- 1.2

---

#### public float height

The overall height of this

Ellipse2D

.

**Since:**
- 1.2

---

### Constructor Details

#### public Float()

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

**Since:**
- 1.2

---

#### public Float​(float x,
float y,
float w,
float h)

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

**Parameters:**
- x

- the X coordinate of the upper-left corner
of the framing rectangle
- y

- the Y coordinate of the upper-left corner
of the framing rectangle
- w

- the width of the framing rectangle
- h

- the height of the framing rectangle

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

#### public void setFrame​(float x,
float y,
float w,
float h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Parameters:**
- x

- the X coordinate of the upper-left corner of the
specified rectangular shape
- y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
- w

- the width of the specified rectangular shape
- h

- the height of the specified rectangular shape

**Since:**
- 1.2

---

#### public void setFrame​(double x,
double y,
double w,
double h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Specified by:**
- setFrame

in class

RectangularShape

**Parameters:**
- x

- the X coordinate of the upper-left corner of the
specified rectangular shape
- y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
- w

- the width of the specified rectangular shape
- h

- the height of the specified rectangular shape

**See Also:**
- RectangularShape.getFrame()

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

#### Class Ellipse2D.Float

java.lang.Object

- java.awt.geom.RectangularShape
- - java.awt.geom.Ellipse2D
- - java.awt.geom.Ellipse2D.Float

java.awt.geom.RectangularShape

- java.awt.geom.Ellipse2D
- - java.awt.geom.Ellipse2D.Float

java.awt.geom.Ellipse2D

- java.awt.geom.Ellipse2D.Float

java.awt.geom.Ellipse2D.Float

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

**Enclosing class:** Ellipse2D

```java
public static class
Ellipse2D.Float

extends
Ellipse2D

implements
Serializable
```

The

Float

class defines an ellipse specified
in

float

precision.

**Since:** 1.2
**See Also:** Serialized Form

public static class

Ellipse2D.Float

extends

Ellipse2D

implements

Serializable

The

Float

class defines an ellipse specified
in

float

precision.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Ellipse2D

Ellipse2D.Double

,

Ellipse2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

float

height

The overall height of this

Ellipse2D

.

float

width

The overall width of this

Ellipse2D

.

float

x

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

float

y

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Float

()

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

Float

​(float x,
float y,
float w,
float h)

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

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

void

setFrame

​(double x,
double y,
double w,
double h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

void

setFrame

​(float x,
float y,
float w,
float h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

- Methods declared in class java.awt.geom.

Ellipse2D

contains

,

contains

,

equals

,

getPathIterator

,

hashCode

,

intersects

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

Ellipse2D

Ellipse2D.Double

,

Ellipse2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

Ellipse2D

Ellipse2D.Double

,

Ellipse2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. Ellipse2D

Field Summary

Fields

Modifier and Type

Field

Description

float

height

The overall height of this

Ellipse2D

.

float

width

The overall width of this

Ellipse2D

.

float

x

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

float

y

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

---

#### Field Summary

The overall height of this

Ellipse2D

.

The overall width of this

Ellipse2D

.

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

Constructor Summary

Constructors

Constructor

Description

Float

()

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

Float

​(float x,
float y,
float w,
float h)

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

---

#### Constructor Summary

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

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

void

setFrame

​(double x,
double y,
double w,
double h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

void

setFrame

​(float x,
float y,
float w,
float h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

- Methods declared in class java.awt.geom.

Ellipse2D

contains

,

contains

,

equals

,

getPathIterator

,

hashCode

,

intersects

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

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

Methods declared in class java.awt.geom.

Ellipse2D

contains

,

contains

,

equals

,

getPathIterator

,

hashCode

,

intersects

---

#### Methods declared in class java.awt.geom. Ellipse2D

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
public float x
```

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:** 1.2

- y

```java
public float y
```

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:** 1.2

- width

```java
public float width
```

The overall width of this

Ellipse2D

.

**Since:** 1.2

- height

```java
public float height
```

The overall height of this

Ellipse2D

.

**Since:** 1.2

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Float

```java
public Float()
```

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

**Since:** 1.2

- Float

```java
public Float​(float x,
float y,
float w,
float h)
```

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

**Parameters:** x

- the X coordinate of the upper-left corner
of the framing rectangle
**Parameters:** y

- the Y coordinate of the upper-left corner
of the framing rectangle
**Parameters:** w

- the width of the framing rectangle
**Parameters:** h

- the height of the framing rectangle
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

- setFrame

```java
public void setFrame​(float x,
float y,
float w,
float h)
```

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Parameters:** x

- the X coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** w

- the width of the specified rectangular shape
**Parameters:** h

- the height of the specified rectangular shape
**Since:** 1.2

- setFrame

```java
public void setFrame​(double x,
double y,
double w,
double h)
```

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Specified by:** setFrame

in class

RectangularShape
**Parameters:** x

- the X coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** w

- the width of the specified rectangular shape
**Parameters:** h

- the height of the specified rectangular shape
**Since:** 1.2
**See Also:** RectangularShape.getFrame()

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

- x

```java
public float x
```

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:** 1.2

- y

```java
public float y
```

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:** 1.2

- width

```java
public float width
```

The overall width of this

Ellipse2D

.

**Since:** 1.2

- height

```java
public float height
```

The overall height of this

Ellipse2D

.

**Since:** 1.2

---

#### Field Detail

x

```java
public float x
```

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:** 1.2

---

#### x

public float x

The X coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

y

```java
public float y
```

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

**Since:** 1.2

---

#### y

public float y

The Y coordinate of the upper-left corner of the
framing rectangle of this

Ellipse2D

.

width

```java
public float width
```

The overall width of this

Ellipse2D

.

**Since:** 1.2

---

#### width

public float width

The overall width of this

Ellipse2D

.

height

```java
public float height
```

The overall height of this

Ellipse2D

.

**Since:** 1.2

---

#### height

public float height

The overall height of this

Ellipse2D

.

Constructor Detail

- Float

```java
public Float()
```

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

**Since:** 1.2

- Float

```java
public Float​(float x,
float y,
float w,
float h)
```

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

**Parameters:** x

- the X coordinate of the upper-left corner
of the framing rectangle
**Parameters:** y

- the Y coordinate of the upper-left corner
of the framing rectangle
**Parameters:** w

- the width of the framing rectangle
**Parameters:** h

- the height of the framing rectangle
**Since:** 1.2

---

#### Constructor Detail

Float

```java
public Float()
```

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

**Since:** 1.2

---

#### Float

public Float()

Constructs a new

Ellipse2D

, initialized to
location (0, 0) and size (0, 0).

Float

```java
public Float​(float x,
float y,
float w,
float h)
```

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

**Parameters:** x

- the X coordinate of the upper-left corner
of the framing rectangle
**Parameters:** y

- the Y coordinate of the upper-left corner
of the framing rectangle
**Parameters:** w

- the width of the framing rectangle
**Parameters:** h

- the height of the framing rectangle
**Since:** 1.2

---

#### Float

public Float​(float x,
float y,
float w,
float h)

Constructs and initializes an

Ellipse2D

from the
specified coordinates.

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

- setFrame

```java
public void setFrame​(float x,
float y,
float w,
float h)
```

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Parameters:** x

- the X coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** w

- the width of the specified rectangular shape
**Parameters:** h

- the height of the specified rectangular shape
**Since:** 1.2

- setFrame

```java
public void setFrame​(double x,
double y,
double w,
double h)
```

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Specified by:** setFrame

in class

RectangularShape
**Parameters:** x

- the X coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** w

- the width of the specified rectangular shape
**Parameters:** h

- the height of the specified rectangular shape
**Since:** 1.2
**See Also:** RectangularShape.getFrame()

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

setFrame

```java
public void setFrame​(float x,
float y,
float w,
float h)
```

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Parameters:** x

- the X coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** w

- the width of the specified rectangular shape
**Parameters:** h

- the height of the specified rectangular shape
**Since:** 1.2

---

#### setFrame

public void setFrame​(float x,
float y,
float w,
float h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

setFrame

```java
public void setFrame​(double x,
double y,
double w,
double h)
```

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

**Specified by:** setFrame

in class

RectangularShape
**Parameters:** x

- the X coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** y

- the Y coordinate of the upper-left corner of the
specified rectangular shape
**Parameters:** w

- the width of the specified rectangular shape
**Parameters:** h

- the height of the specified rectangular shape
**Since:** 1.2
**See Also:** RectangularShape.getFrame()

---

#### setFrame

public void setFrame​(double x,
double y,
double w,
double h)

Sets the location and size of the framing rectangle of this

Shape

to the specified rectangular values.

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

