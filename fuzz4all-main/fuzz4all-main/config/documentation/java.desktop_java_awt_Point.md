# Class Point

**Source:** `java.desktop\java\awt\Point.html`

### Class Description

```java
public class
Point

extends
Point2D

implements
Serializable
```

A point representing a location in

(x,y)

coordinate space,
specified in integer precision.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public int x

The X coordinate of this

Point

.
If no X coordinate is set it will default to 0.

**See Also:**
- getLocation()

,

move(int, int)

**Since:**
- 1.0

---

#### public int y

The Y coordinate of this

Point

.
If no Y coordinate is set it will default to 0.

**See Also:**
- getLocation()

,

move(int, int)

**Since:**
- 1.0

---

### Constructor Details

#### public Point()

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

**Since:**
- 1.1

---

#### public Point​(
Point
p)

Constructs and initializes a point with the same location as
the specified

Point

object.

**Parameters:**
- p

- a point

**Since:**
- 1.1

---

#### public Point​(int x,
int y)

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

**Parameters:**
- x

- the X coordinate of the newly constructed

Point
- y

- the Y coordinate of the newly constructed

Point

**Since:**
- 1.0

---

### Method Details

#### public double getX()

Returns the X coordinate of this

Point2D

in

double

precision.

**Specified by:**
- getX

in class

Point2D

**Returns:**
- the X coordinate of this

Point2D

.

**Since:**
- 1.2

---

#### public double getY()

Returns the Y coordinate of this

Point2D

in

double

precision.

**Specified by:**
- getY

in class

Point2D

**Returns:**
- the Y coordinate of this

Point2D

.

**Since:**
- 1.2

---

#### public
Point
getLocation()

Returns the location of this point.
This method is included for completeness, to parallel the

getLocation

method of

Component

.

**Returns:**
- a copy of this point, at the same location

**See Also:**
- Component.getLocation()

,

setLocation(java.awt.Point)

,

setLocation(int, int)

**Since:**
- 1.1

---

#### public void setLocation​(
Point
p)

Sets the location of the point to the specified location.
This method is included for completeness, to parallel the

setLocation

method of

Component

.

**Parameters:**
- p

- a point, the new location for this point

**See Also:**
- Component.setLocation(java.awt.Point)

,

getLocation()

**Since:**
- 1.1

---

#### public void setLocation​(int x,
int y)

Changes the point to have the specified location.

This method is included for completeness, to parallel the

setLocation

method of

Component

.
Its behavior is identical with

move(int, int)

.

**Parameters:**
- x

- the X coordinate of the new location
- y

- the Y coordinate of the new location

**See Also:**
- Component.setLocation(int, int)

,

getLocation()

,

move(int, int)

**Since:**
- 1.1

---

#### public void setLocation​(double x,
double y)

Sets the location of this point to the specified double coordinates.
The double values will be rounded to integer values.
Any number smaller than

Integer.MIN_VALUE

will be reset to

MIN_VALUE

, and any number
larger than

Integer.MAX_VALUE

will be
reset to

MAX_VALUE

.

**Specified by:**
- setLocation

in class

Point2D

**Parameters:**
- x

- the X coordinate of the new location
- y

- the Y coordinate of the new location

**See Also:**
- getLocation()

---

#### public void move​(int x,
int y)

Moves this point to the specified location in the

(x,y)

coordinate plane. This method
is identical with

setLocation(int, int)

.

**Parameters:**
- x

- the X coordinate of the new location
- y

- the Y coordinate of the new location

**See Also:**
- Component.setLocation(int, int)

---

#### public void translate​(int dx,
int dy)

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

**Parameters:**
- dx

- the distance to move this point
along the X axis
- dy

- the distance to move this point
along the Y axis

---

#### public boolean equals​(
Object
obj)

Determines whether or not two points are equal. Two instances of

Point2D

are equal if the values of their

x

and

y

member fields, representing
their position in the coordinate space, are the same.

**Overrides:**
- equals

in class

Point2D

**Parameters:**
- obj

- an object to be compared with this

Point2D

**Returns:**
- true

if the object to be compared is
an instance of

Point2D

and has
the same values;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string representation of this point and its location
in the

(x,y)

coordinate space. This method is
intended to be used only for debugging purposes, and the content
and format of the returned string may vary between implementations.
The returned string may be empty but may not be

null

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this point

---

### Additional Sections

#### Class Point

java.lang.Object

- java.awt.geom.Point2D
- - java.awt.Point

java.awt.geom.Point2D

- java.awt.Point

java.awt.Point

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
Point

extends
Point2D

implements
Serializable
```

A point representing a location in

(x,y)

coordinate space,
specified in integer precision.

**Since:** 1.0
**See Also:** Serialized Form

public class

Point

extends

Point2D

implements

Serializable

A point representing a location in

(x,y)

coordinate space,
specified in integer precision.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Point2D

Point2D.Double

,

Point2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

int

x

The X coordinate of this

Point

.

int

y

The Y coordinate of this

Point

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Point

()

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

Point

​(int x,
int y)

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

Point

​(

Point

p)

Constructs and initializes a point with the same location as
the specified

Point

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether or not two points are equal.

Point

getLocation

()

Returns the location of this point.

double

getX

()

Returns the X coordinate of this

Point2D

in

double

precision.

double

getY

()

Returns the Y coordinate of this

Point2D

in

double

precision.

void

move

​(int x,
int y)

Moves this point to the specified location in the

(x,y)

coordinate plane.

void

setLocation

​(double x,
double y)

Sets the location of this point to the specified double coordinates.

void

setLocation

​(int x,
int y)

Changes the point to have the specified location.

void

setLocation

​(

Point

p)

Sets the location of the point to the specified location.

String

toString

()

Returns a string representation of this point and its location
in the

(x,y)

coordinate space.

void

translate

​(int dx,
int dy)

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

- Methods declared in class java.awt.geom.

Point2D

clone

,

distance

,

distance

,

distance

,

distanceSq

,

distanceSq

,

distanceSq

,

hashCode

,

setLocation

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

Point2D

Point2D.Double

,

Point2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

Point2D

Point2D.Double

,

Point2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. Point2D

Field Summary

Fields

Modifier and Type

Field

Description

int

x

The X coordinate of this

Point

.

int

y

The Y coordinate of this

Point

.

---

#### Field Summary

The X coordinate of this

Point

.

The Y coordinate of this

Point

.

Constructor Summary

Constructors

Constructor

Description

Point

()

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

Point

​(int x,
int y)

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

Point

​(

Point

p)

Constructs and initializes a point with the same location as
the specified

Point

object.

---

#### Constructor Summary

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

Constructs and initializes a point with the same location as
the specified

Point

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether or not two points are equal.

Point

getLocation

()

Returns the location of this point.

double

getX

()

Returns the X coordinate of this

Point2D

in

double

precision.

double

getY

()

Returns the Y coordinate of this

Point2D

in

double

precision.

void

move

​(int x,
int y)

Moves this point to the specified location in the

(x,y)

coordinate plane.

void

setLocation

​(double x,
double y)

Sets the location of this point to the specified double coordinates.

void

setLocation

​(int x,
int y)

Changes the point to have the specified location.

void

setLocation

​(

Point

p)

Sets the location of the point to the specified location.

String

toString

()

Returns a string representation of this point and its location
in the

(x,y)

coordinate space.

void

translate

​(int dx,
int dy)

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

- Methods declared in class java.awt.geom.

Point2D

clone

,

distance

,

distance

,

distance

,

distanceSq

,

distanceSq

,

distanceSq

,

hashCode

,

setLocation

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

Determines whether or not two points are equal.

Returns the location of this point.

Returns the X coordinate of this

Point2D

in

double

precision.

Returns the Y coordinate of this

Point2D

in

double

precision.

Moves this point to the specified location in the

(x,y)

coordinate plane.

Sets the location of this point to the specified double coordinates.

Changes the point to have the specified location.

Sets the location of the point to the specified location.

Returns a string representation of this point and its location
in the

(x,y)

coordinate space.

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

Methods declared in class java.awt.geom.

Point2D

clone

,

distance

,

distance

,

distance

,

distanceSq

,

distanceSq

,

distanceSq

,

hashCode

,

setLocation

---

#### Methods declared in class java.awt.geom. Point2D

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
public int x
```

The X coordinate of this

Point

.
If no X coordinate is set it will default to 0.

**Since:** 1.0
**See Also:** getLocation()

,

move(int, int)

- y

```java
public int y
```

The Y coordinate of this

Point

.
If no Y coordinate is set it will default to 0.

**Since:** 1.0
**See Also:** getLocation()

,

move(int, int)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Point

```java
public Point()
```

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

**Since:** 1.1

- Point

```java
public Point​(
Point
p)
```

Constructs and initializes a point with the same location as
the specified

Point

object.

**Parameters:** p

- a point
**Since:** 1.1

- Point

```java
public Point​(int x,
int y)
```

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

**Parameters:** x

- the X coordinate of the newly constructed

Point
**Parameters:** y

- the Y coordinate of the newly constructed

Point
**Since:** 1.0

============ METHOD DETAIL ==========

- Method Detail

- getX

```java
public double getX()
```

Returns the X coordinate of this

Point2D

in

double

precision.

**Specified by:** getX

in class

Point2D
**Returns:** the X coordinate of this

Point2D

.
**Since:** 1.2

- getY

```java
public double getY()
```

Returns the Y coordinate of this

Point2D

in

double

precision.

**Specified by:** getY

in class

Point2D
**Returns:** the Y coordinate of this

Point2D

.
**Since:** 1.2

- getLocation

```java
public
Point
getLocation()
```

Returns the location of this point.
This method is included for completeness, to parallel the

getLocation

method of

Component

.

**Returns:** a copy of this point, at the same location
**Since:** 1.1
**See Also:** Component.getLocation()

,

setLocation(java.awt.Point)

,

setLocation(int, int)

- setLocation

```java
public void setLocation​(
Point
p)
```

Sets the location of the point to the specified location.
This method is included for completeness, to parallel the

setLocation

method of

Component

.

**Parameters:** p

- a point, the new location for this point
**Since:** 1.1
**See Also:** Component.setLocation(java.awt.Point)

,

getLocation()

- setLocation

```java
public void setLocation​(int x,
int y)
```

Changes the point to have the specified location.

This method is included for completeness, to parallel the

setLocation

method of

Component

.
Its behavior is identical with

move(int, int)

.

**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**Since:** 1.1
**See Also:** Component.setLocation(int, int)

,

getLocation()

,

move(int, int)

- setLocation

```java
public void setLocation​(double x,
double y)
```

Sets the location of this point to the specified double coordinates.
The double values will be rounded to integer values.
Any number smaller than

Integer.MIN_VALUE

will be reset to

MIN_VALUE

, and any number
larger than

Integer.MAX_VALUE

will be
reset to

MAX_VALUE

.

**Specified by:** setLocation

in class

Point2D
**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**See Also:** getLocation()

- move

```java
public void move​(int x,
int y)
```

Moves this point to the specified location in the

(x,y)

coordinate plane. This method
is identical with

setLocation(int, int)

.

**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**See Also:** Component.setLocation(int, int)

- translate

```java
public void translate​(int dx,
int dy)
```

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

**Parameters:** dx

- the distance to move this point
along the X axis
**Parameters:** dy

- the distance to move this point
along the Y axis

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether or not two points are equal. Two instances of

Point2D

are equal if the values of their

x

and

y

member fields, representing
their position in the coordinate space, are the same.

**Overrides:** equals

in class

Point2D
**Parameters:** obj

- an object to be compared with this

Point2D
**Returns:** true

if the object to be compared is
an instance of

Point2D

and has
the same values;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string representation of this point and its location
in the

(x,y)

coordinate space. This method is
intended to be used only for debugging purposes, and the content
and format of the returned string may vary between implementations.
The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this point

Field Detail

- x

```java
public int x
```

The X coordinate of this

Point

.
If no X coordinate is set it will default to 0.

**Since:** 1.0
**See Also:** getLocation()

,

move(int, int)

- y

```java
public int y
```

The Y coordinate of this

Point

.
If no Y coordinate is set it will default to 0.

**Since:** 1.0
**See Also:** getLocation()

,

move(int, int)

---

#### Field Detail

x

```java
public int x
```

The X coordinate of this

Point

.
If no X coordinate is set it will default to 0.

**Since:** 1.0
**See Also:** getLocation()

,

move(int, int)

---

#### x

public int x

The X coordinate of this

Point

.
If no X coordinate is set it will default to 0.

y

```java
public int y
```

The Y coordinate of this

Point

.
If no Y coordinate is set it will default to 0.

**Since:** 1.0
**See Also:** getLocation()

,

move(int, int)

---

#### y

public int y

The Y coordinate of this

Point

.
If no Y coordinate is set it will default to 0.

Constructor Detail

- Point

```java
public Point()
```

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

**Since:** 1.1

- Point

```java
public Point​(
Point
p)
```

Constructs and initializes a point with the same location as
the specified

Point

object.

**Parameters:** p

- a point
**Since:** 1.1

- Point

```java
public Point​(int x,
int y)
```

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

**Parameters:** x

- the X coordinate of the newly constructed

Point
**Parameters:** y

- the Y coordinate of the newly constructed

Point
**Since:** 1.0

---

#### Constructor Detail

Point

```java
public Point()
```

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

**Since:** 1.1

---

#### Point

public Point()

Constructs and initializes a point at the origin
(0, 0) of the coordinate space.

Point

```java
public Point​(
Point
p)
```

Constructs and initializes a point with the same location as
the specified

Point

object.

**Parameters:** p

- a point
**Since:** 1.1

---

#### Point

public Point​(

Point

p)

Constructs and initializes a point with the same location as
the specified

Point

object.

Point

```java
public Point​(int x,
int y)
```

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

**Parameters:** x

- the X coordinate of the newly constructed

Point
**Parameters:** y

- the Y coordinate of the newly constructed

Point
**Since:** 1.0

---

#### Point

public Point​(int x,
int y)

Constructs and initializes a point at the specified

(x,y)

location in the coordinate space.

Method Detail

- getX

```java
public double getX()
```

Returns the X coordinate of this

Point2D

in

double

precision.

**Specified by:** getX

in class

Point2D
**Returns:** the X coordinate of this

Point2D

.
**Since:** 1.2

- getY

```java
public double getY()
```

Returns the Y coordinate of this

Point2D

in

double

precision.

**Specified by:** getY

in class

Point2D
**Returns:** the Y coordinate of this

Point2D

.
**Since:** 1.2

- getLocation

```java
public
Point
getLocation()
```

Returns the location of this point.
This method is included for completeness, to parallel the

getLocation

method of

Component

.

**Returns:** a copy of this point, at the same location
**Since:** 1.1
**See Also:** Component.getLocation()

,

setLocation(java.awt.Point)

,

setLocation(int, int)

- setLocation

```java
public void setLocation​(
Point
p)
```

Sets the location of the point to the specified location.
This method is included for completeness, to parallel the

setLocation

method of

Component

.

**Parameters:** p

- a point, the new location for this point
**Since:** 1.1
**See Also:** Component.setLocation(java.awt.Point)

,

getLocation()

- setLocation

```java
public void setLocation​(int x,
int y)
```

Changes the point to have the specified location.

This method is included for completeness, to parallel the

setLocation

method of

Component

.
Its behavior is identical with

move(int, int)

.

**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**Since:** 1.1
**See Also:** Component.setLocation(int, int)

,

getLocation()

,

move(int, int)

- setLocation

```java
public void setLocation​(double x,
double y)
```

Sets the location of this point to the specified double coordinates.
The double values will be rounded to integer values.
Any number smaller than

Integer.MIN_VALUE

will be reset to

MIN_VALUE

, and any number
larger than

Integer.MAX_VALUE

will be
reset to

MAX_VALUE

.

**Specified by:** setLocation

in class

Point2D
**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**See Also:** getLocation()

- move

```java
public void move​(int x,
int y)
```

Moves this point to the specified location in the

(x,y)

coordinate plane. This method
is identical with

setLocation(int, int)

.

**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**See Also:** Component.setLocation(int, int)

- translate

```java
public void translate​(int dx,
int dy)
```

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

**Parameters:** dx

- the distance to move this point
along the X axis
**Parameters:** dy

- the distance to move this point
along the Y axis

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether or not two points are equal. Two instances of

Point2D

are equal if the values of their

x

and

y

member fields, representing
their position in the coordinate space, are the same.

**Overrides:** equals

in class

Point2D
**Parameters:** obj

- an object to be compared with this

Point2D
**Returns:** true

if the object to be compared is
an instance of

Point2D

and has
the same values;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string representation of this point and its location
in the

(x,y)

coordinate space. This method is
intended to be used only for debugging purposes, and the content
and format of the returned string may vary between implementations.
The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this point

---

#### Method Detail

getX

```java
public double getX()
```

Returns the X coordinate of this

Point2D

in

double

precision.

**Specified by:** getX

in class

Point2D
**Returns:** the X coordinate of this

Point2D

.
**Since:** 1.2

---

#### getX

public double getX()

Returns the X coordinate of this

Point2D

in

double

precision.

getY

```java
public double getY()
```

Returns the Y coordinate of this

Point2D

in

double

precision.

**Specified by:** getY

in class

Point2D
**Returns:** the Y coordinate of this

Point2D

.
**Since:** 1.2

---

#### getY

public double getY()

Returns the Y coordinate of this

Point2D

in

double

precision.

getLocation

```java
public
Point
getLocation()
```

Returns the location of this point.
This method is included for completeness, to parallel the

getLocation

method of

Component

.

**Returns:** a copy of this point, at the same location
**Since:** 1.1
**See Also:** Component.getLocation()

,

setLocation(java.awt.Point)

,

setLocation(int, int)

---

#### getLocation

public

Point

getLocation()

Returns the location of this point.
This method is included for completeness, to parallel the

getLocation

method of

Component

.

setLocation

```java
public void setLocation​(
Point
p)
```

Sets the location of the point to the specified location.
This method is included for completeness, to parallel the

setLocation

method of

Component

.

**Parameters:** p

- a point, the new location for this point
**Since:** 1.1
**See Also:** Component.setLocation(java.awt.Point)

,

getLocation()

---

#### setLocation

public void setLocation​(

Point

p)

Sets the location of the point to the specified location.
This method is included for completeness, to parallel the

setLocation

method of

Component

.

setLocation

```java
public void setLocation​(int x,
int y)
```

Changes the point to have the specified location.

This method is included for completeness, to parallel the

setLocation

method of

Component

.
Its behavior is identical with

move(int, int)

.

**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**Since:** 1.1
**See Also:** Component.setLocation(int, int)

,

getLocation()

,

move(int, int)

---

#### setLocation

public void setLocation​(int x,
int y)

Changes the point to have the specified location.

This method is included for completeness, to parallel the

setLocation

method of

Component

.
Its behavior is identical with

move(int, int)

.

This method is included for completeness, to parallel the

setLocation

method of

Component

.
Its behavior is identical with

move(int, int)

.

setLocation

```java
public void setLocation​(double x,
double y)
```

Sets the location of this point to the specified double coordinates.
The double values will be rounded to integer values.
Any number smaller than

Integer.MIN_VALUE

will be reset to

MIN_VALUE

, and any number
larger than

Integer.MAX_VALUE

will be
reset to

MAX_VALUE

.

**Specified by:** setLocation

in class

Point2D
**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**See Also:** getLocation()

---

#### setLocation

public void setLocation​(double x,
double y)

Sets the location of this point to the specified double coordinates.
The double values will be rounded to integer values.
Any number smaller than

Integer.MIN_VALUE

will be reset to

MIN_VALUE

, and any number
larger than

Integer.MAX_VALUE

will be
reset to

MAX_VALUE

.

move

```java
public void move​(int x,
int y)
```

Moves this point to the specified location in the

(x,y)

coordinate plane. This method
is identical with

setLocation(int, int)

.

**Parameters:** x

- the X coordinate of the new location
**Parameters:** y

- the Y coordinate of the new location
**See Also:** Component.setLocation(int, int)

---

#### move

public void move​(int x,
int y)

Moves this point to the specified location in the

(x,y)

coordinate plane. This method
is identical with

setLocation(int, int)

.

translate

```java
public void translate​(int dx,
int dy)
```

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

**Parameters:** dx

- the distance to move this point
along the X axis
**Parameters:** dy

- the distance to move this point
along the Y axis

---

#### translate

public void translate​(int dx,
int dy)

Translates this point, at location

(x,y)

,
by

dx

along the

x

axis and

dy

along the

y

axis so that it now represents the point

(x+dx,y+dy)

.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether or not two points are equal. Two instances of

Point2D

are equal if the values of their

x

and

y

member fields, representing
their position in the coordinate space, are the same.

**Overrides:** equals

in class

Point2D
**Parameters:** obj

- an object to be compared with this

Point2D
**Returns:** true

if the object to be compared is
an instance of

Point2D

and has
the same values;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Determines whether or not two points are equal. Two instances of

Point2D

are equal if the values of their

x

and

y

member fields, representing
their position in the coordinate space, are the same.

toString

```java
public
String
toString()
```

Returns a string representation of this point and its location
in the

(x,y)

coordinate space. This method is
intended to be used only for debugging purposes, and the content
and format of the returned string may vary between implementations.
The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this point

---

#### toString

public

String

toString()

Returns a string representation of this point and its location
in the

(x,y)

coordinate space. This method is
intended to be used only for debugging purposes, and the content
and format of the returned string may vary between implementations.
The returned string may be empty but may not be

null

.

---

