# Class Point2D

**Source:** `java.desktop\java\awt\geom\Point2D.html`

### Class Description

```java
public abstract class
Point2D

extends
Object

implements
Cloneable
```

The

Point2D

class defines a point representing a location
in

(x,y)

coordinate space.

This class is only the abstract superclass for all objects that
store a 2D coordinate.
The actual storage representation of the coordinates is left to
the subclass.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Point2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**See Also:**
- Point2D.Float

,

Point2D.Double

,

Point

**Since:**
- 1.2

---

### Method Details

#### public abstract double getX()

Returns the X coordinate of this

Point2D

in

double

precision.

**Returns:**
- the X coordinate of this

Point2D

.

**Since:**
- 1.2

---

#### public abstract double getY()

Returns the Y coordinate of this

Point2D

in

double

precision.

**Returns:**
- the Y coordinate of this

Point2D

.

**Since:**
- 1.2

---

#### public abstract void setLocation​(double x,
double y)

Sets the location of this

Point2D

to the
specified

double

coordinates.

**Parameters:**
- x

- the new X coordinate of this

Point2D
- y

- the new Y coordinate of this

Point2D

**Since:**
- 1.2

---

#### public void setLocation​(
Point2D
p)

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

**Parameters:**
- p

- the specified

Point2D

to which to set
this

Point2D

**Since:**
- 1.2

---

#### public static double distanceSq​(double x1,
double y1,
double x2,
double y2)

Returns the square of the distance between two points.

**Parameters:**
- x1

- the X coordinate of the first specified point
- y1

- the Y coordinate of the first specified point
- x2

- the X coordinate of the second specified point
- y2

- the Y coordinate of the second specified point

**Returns:**
- the square of the distance between the two
sets of specified coordinates.

**Since:**
- 1.2

---

#### public static double distance​(double x1,
double y1,
double x2,
double y2)

Returns the distance between two points.

**Parameters:**
- x1

- the X coordinate of the first specified point
- y1

- the Y coordinate of the first specified point
- x2

- the X coordinate of the second specified point
- y2

- the Y coordinate of the second specified point

**Returns:**
- the distance between the two sets of specified
coordinates.

**Since:**
- 1.2

---

#### public double distanceSq​(double px,
double py)

Returns the square of the distance from this

Point2D

to a specified point.

**Parameters:**
- px

- the X coordinate of the specified point to be measured
against this

Point2D
- py

- the Y coordinate of the specified point to be measured
against this

Point2D

**Returns:**
- the square of the distance between this

Point2D

and the specified point.

**Since:**
- 1.2

---

#### public double distanceSq​(
Point2D
pt)

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

**Parameters:**
- pt

- the specified point to be measured
against this

Point2D

**Returns:**
- the square of the distance between this

Point2D

to a specified

Point2D

.

**Since:**
- 1.2

---

#### public double distance​(double px,
double py)

Returns the distance from this

Point2D

to
a specified point.

**Parameters:**
- px

- the X coordinate of the specified point to be measured
against this

Point2D
- py

- the Y coordinate of the specified point to be measured
against this

Point2D

**Returns:**
- the distance between this

Point2D

and a specified point.

**Since:**
- 1.2

---

#### public double distance​(
Point2D
pt)

Returns the distance from this

Point2D

to a
specified

Point2D

.

**Parameters:**
- pt

- the specified point to be measured
against this

Point2D

**Returns:**
- the distance between this

Point2D

and
the specified

Point2D

.

**Since:**
- 1.2

---

#### public
Object
clone()

Creates a new object of the same class and with the
same contents as this object.

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

#### public int hashCode()

Returns the hashcode for this

Point2D

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

Point2D

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

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

Object

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

**Since:**
- 1.2

---

### Additional Sections

#### Class Point2D

java.lang.Object

- java.awt.geom.Point2D

java.awt.geom.Point2D

**All Implemented Interfaces:** Cloneable

**Direct Known Subclasses:** Point

,

Point2D.Double

,

Point2D.Float

```java
public abstract class
Point2D

extends
Object

implements
Cloneable
```

The

Point2D

class defines a point representing a location
in

(x,y)

coordinate space.

This class is only the abstract superclass for all objects that
store a 2D coordinate.
The actual storage representation of the coordinates is left to
the subclass.

**Since:** 1.2

public abstract class

Point2D

extends

Object

implements

Cloneable

The

Point2D

class defines a point representing a location
in

(x,y)

coordinate space.

This class is only the abstract superclass for all objects that
store a 2D coordinate.
The actual storage representation of the coordinates is left to
the subclass.

This class is only the abstract superclass for all objects that
store a 2D coordinate.
The actual storage representation of the coordinates is left to
the subclass.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Point2D.Double

The

Double

class defines a point specified in

double

precision.

static class

Point2D.Float

The

Float

class defines a point specified in float
precision.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Point2D

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

Creates a new object of the same class and with the
same contents as this object.

double

distance

​(double px,
double py)

Returns the distance from this

Point2D

to
a specified point.

static double

distance

​(double x1,
double y1,
double x2,
double y2)

Returns the distance between two points.

double

distance

​(

Point2D

pt)

Returns the distance from this

Point2D

to a
specified

Point2D

.

double

distanceSq

​(double px,
double py)

Returns the square of the distance from this

Point2D

to a specified point.

static double

distanceSq

​(double x1,
double y1,
double x2,
double y2)

Returns the square of the distance between two points.

double

distanceSq

​(

Point2D

pt)

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

boolean

equals

​(

Object

obj)

Determines whether or not two points are equal.

abstract double

getX

()

Returns the X coordinate of this

Point2D

in

double

precision.

abstract double

getY

()

Returns the Y coordinate of this

Point2D

in

double

precision.

int

hashCode

()

Returns the hashcode for this

Point2D

.

abstract void

setLocation

​(double x,
double y)

Sets the location of this

Point2D

to the
specified

double

coordinates.

void

setLocation

​(

Point2D

p)

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

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

Nested Classes

Modifier and Type

Class

Description

static class

Point2D.Double

The

Double

class defines a point specified in

double

precision.

static class

Point2D.Float

The

Float

class defines a point specified in float
precision.

---

#### Nested Class Summary

The

Double

class defines a point specified in

double

precision.

The

Float

class defines a point specified in float
precision.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Point2D

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

Creates a new object of the same class and with the
same contents as this object.

double

distance

​(double px,
double py)

Returns the distance from this

Point2D

to
a specified point.

static double

distance

​(double x1,
double y1,
double x2,
double y2)

Returns the distance between two points.

double

distance

​(

Point2D

pt)

Returns the distance from this

Point2D

to a
specified

Point2D

.

double

distanceSq

​(double px,
double py)

Returns the square of the distance from this

Point2D

to a specified point.

static double

distanceSq

​(double x1,
double y1,
double x2,
double y2)

Returns the square of the distance between two points.

double

distanceSq

​(

Point2D

pt)

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

boolean

equals

​(

Object

obj)

Determines whether or not two points are equal.

abstract double

getX

()

Returns the X coordinate of this

Point2D

in

double

precision.

abstract double

getY

()

Returns the Y coordinate of this

Point2D

in

double

precision.

int

hashCode

()

Returns the hashcode for this

Point2D

.

abstract void

setLocation

​(double x,
double y)

Sets the location of this

Point2D

to the
specified

double

coordinates.

void

setLocation

​(

Point2D

p)

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

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

Creates a new object of the same class and with the
same contents as this object.

Returns the distance from this

Point2D

to
a specified point.

Returns the distance between two points.

Returns the distance from this

Point2D

to a
specified

Point2D

.

Returns the square of the distance from this

Point2D

to a specified point.

Returns the square of the distance between two points.

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

Determines whether or not two points are equal.

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

Returns the hashcode for this

Point2D

.

Sets the location of this

Point2D

to the
specified

double

coordinates.

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Point2D

```java
protected Point2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Point2D.Float

,

Point2D.Double

,

Point

============ METHOD DETAIL ==========

- Method Detail

- getX

```java
public abstract double getX()
```

Returns the X coordinate of this

Point2D

in

double

precision.

**Returns:** the X coordinate of this

Point2D

.
**Since:** 1.2

- getY

```java
public abstract double getY()
```

Returns the Y coordinate of this

Point2D

in

double

precision.

**Returns:** the Y coordinate of this

Point2D

.
**Since:** 1.2

- setLocation

```java
public abstract void setLocation​(double x,
double y)
```

Sets the location of this

Point2D

to the
specified

double

coordinates.

**Parameters:** x

- the new X coordinate of this

Point2D
**Parameters:** y

- the new Y coordinate of this

Point2D
**Since:** 1.2

- setLocation

```java
public void setLocation​(
Point2D
p)
```

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

**Parameters:** p

- the specified

Point2D

to which to set
this

Point2D
**Since:** 1.2

- distanceSq

```java
public static double distanceSq​(double x1,
double y1,
double x2,
double y2)
```

Returns the square of the distance between two points.

**Parameters:** x1

- the X coordinate of the first specified point
**Parameters:** y1

- the Y coordinate of the first specified point
**Parameters:** x2

- the X coordinate of the second specified point
**Parameters:** y2

- the Y coordinate of the second specified point
**Returns:** the square of the distance between the two
sets of specified coordinates.
**Since:** 1.2

- distance

```java
public static double distance​(double x1,
double y1,
double x2,
double y2)
```

Returns the distance between two points.

**Parameters:** x1

- the X coordinate of the first specified point
**Parameters:** y1

- the Y coordinate of the first specified point
**Parameters:** x2

- the X coordinate of the second specified point
**Parameters:** y2

- the Y coordinate of the second specified point
**Returns:** the distance between the two sets of specified
coordinates.
**Since:** 1.2

- distanceSq

```java
public double distanceSq​(double px,
double py)
```

Returns the square of the distance from this

Point2D

to a specified point.

**Parameters:** px

- the X coordinate of the specified point to be measured
against this

Point2D
**Parameters:** py

- the Y coordinate of the specified point to be measured
against this

Point2D
**Returns:** the square of the distance between this

Point2D

and the specified point.
**Since:** 1.2

- distanceSq

```java
public double distanceSq​(
Point2D
pt)
```

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

**Parameters:** pt

- the specified point to be measured
against this

Point2D
**Returns:** the square of the distance between this

Point2D

to a specified

Point2D

.
**Since:** 1.2

- distance

```java
public double distance​(double px,
double py)
```

Returns the distance from this

Point2D

to
a specified point.

**Parameters:** px

- the X coordinate of the specified point to be measured
against this

Point2D
**Parameters:** py

- the Y coordinate of the specified point to be measured
against this

Point2D
**Returns:** the distance between this

Point2D

and a specified point.
**Since:** 1.2

- distance

```java
public double distance​(
Point2D
pt)
```

Returns the distance from this

Point2D

to a
specified

Point2D

.

**Parameters:** pt

- the specified point to be measured
against this

Point2D
**Returns:** the distance between this

Point2D

and
the specified

Point2D

.
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Creates a new object of the same class and with the
same contents as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this

Point2D

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

Point2D

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

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

Object
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
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- Point2D

```java
protected Point2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Point2D.Float

,

Point2D.Double

,

Point

---

#### Constructor Detail

Point2D

```java
protected Point2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Point2D.Float

,

Point2D.Double

,

Point

---

#### Point2D

protected Point2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

Method Detail

- getX

```java
public abstract double getX()
```

Returns the X coordinate of this

Point2D

in

double

precision.

**Returns:** the X coordinate of this

Point2D

.
**Since:** 1.2

- getY

```java
public abstract double getY()
```

Returns the Y coordinate of this

Point2D

in

double

precision.

**Returns:** the Y coordinate of this

Point2D

.
**Since:** 1.2

- setLocation

```java
public abstract void setLocation​(double x,
double y)
```

Sets the location of this

Point2D

to the
specified

double

coordinates.

**Parameters:** x

- the new X coordinate of this

Point2D
**Parameters:** y

- the new Y coordinate of this

Point2D
**Since:** 1.2

- setLocation

```java
public void setLocation​(
Point2D
p)
```

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

**Parameters:** p

- the specified

Point2D

to which to set
this

Point2D
**Since:** 1.2

- distanceSq

```java
public static double distanceSq​(double x1,
double y1,
double x2,
double y2)
```

Returns the square of the distance between two points.

**Parameters:** x1

- the X coordinate of the first specified point
**Parameters:** y1

- the Y coordinate of the first specified point
**Parameters:** x2

- the X coordinate of the second specified point
**Parameters:** y2

- the Y coordinate of the second specified point
**Returns:** the square of the distance between the two
sets of specified coordinates.
**Since:** 1.2

- distance

```java
public static double distance​(double x1,
double y1,
double x2,
double y2)
```

Returns the distance between two points.

**Parameters:** x1

- the X coordinate of the first specified point
**Parameters:** y1

- the Y coordinate of the first specified point
**Parameters:** x2

- the X coordinate of the second specified point
**Parameters:** y2

- the Y coordinate of the second specified point
**Returns:** the distance between the two sets of specified
coordinates.
**Since:** 1.2

- distanceSq

```java
public double distanceSq​(double px,
double py)
```

Returns the square of the distance from this

Point2D

to a specified point.

**Parameters:** px

- the X coordinate of the specified point to be measured
against this

Point2D
**Parameters:** py

- the Y coordinate of the specified point to be measured
against this

Point2D
**Returns:** the square of the distance between this

Point2D

and the specified point.
**Since:** 1.2

- distanceSq

```java
public double distanceSq​(
Point2D
pt)
```

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

**Parameters:** pt

- the specified point to be measured
against this

Point2D
**Returns:** the square of the distance between this

Point2D

to a specified

Point2D

.
**Since:** 1.2

- distance

```java
public double distance​(double px,
double py)
```

Returns the distance from this

Point2D

to
a specified point.

**Parameters:** px

- the X coordinate of the specified point to be measured
against this

Point2D
**Parameters:** py

- the Y coordinate of the specified point to be measured
against this

Point2D
**Returns:** the distance between this

Point2D

and a specified point.
**Since:** 1.2

- distance

```java
public double distance​(
Point2D
pt)
```

Returns the distance from this

Point2D

to a
specified

Point2D

.

**Parameters:** pt

- the specified point to be measured
against this

Point2D
**Returns:** the distance between this

Point2D

and
the specified

Point2D

.
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Creates a new object of the same class and with the
same contents as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this

Point2D

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

Point2D

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

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

Object
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
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getX

```java
public abstract double getX()
```

Returns the X coordinate of this

Point2D

in

double

precision.

**Returns:** the X coordinate of this

Point2D

.
**Since:** 1.2

---

#### getX

public abstract double getX()

Returns the X coordinate of this

Point2D

in

double

precision.

getY

```java
public abstract double getY()
```

Returns the Y coordinate of this

Point2D

in

double

precision.

**Returns:** the Y coordinate of this

Point2D

.
**Since:** 1.2

---

#### getY

public abstract double getY()

Returns the Y coordinate of this

Point2D

in

double

precision.

setLocation

```java
public abstract void setLocation​(double x,
double y)
```

Sets the location of this

Point2D

to the
specified

double

coordinates.

**Parameters:** x

- the new X coordinate of this

Point2D
**Parameters:** y

- the new Y coordinate of this

Point2D
**Since:** 1.2

---

#### setLocation

public abstract void setLocation​(double x,
double y)

Sets the location of this

Point2D

to the
specified

double

coordinates.

setLocation

```java
public void setLocation​(
Point2D
p)
```

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

**Parameters:** p

- the specified

Point2D

to which to set
this

Point2D
**Since:** 1.2

---

#### setLocation

public void setLocation​(

Point2D

p)

Sets the location of this

Point2D

to the same
coordinates as the specified

Point2D

object.

distanceSq

```java
public static double distanceSq​(double x1,
double y1,
double x2,
double y2)
```

Returns the square of the distance between two points.

**Parameters:** x1

- the X coordinate of the first specified point
**Parameters:** y1

- the Y coordinate of the first specified point
**Parameters:** x2

- the X coordinate of the second specified point
**Parameters:** y2

- the Y coordinate of the second specified point
**Returns:** the square of the distance between the two
sets of specified coordinates.
**Since:** 1.2

---

#### distanceSq

public static double distanceSq​(double x1,
double y1,
double x2,
double y2)

Returns the square of the distance between two points.

distance

```java
public static double distance​(double x1,
double y1,
double x2,
double y2)
```

Returns the distance between two points.

**Parameters:** x1

- the X coordinate of the first specified point
**Parameters:** y1

- the Y coordinate of the first specified point
**Parameters:** x2

- the X coordinate of the second specified point
**Parameters:** y2

- the Y coordinate of the second specified point
**Returns:** the distance between the two sets of specified
coordinates.
**Since:** 1.2

---

#### distance

public static double distance​(double x1,
double y1,
double x2,
double y2)

Returns the distance between two points.

distanceSq

```java
public double distanceSq​(double px,
double py)
```

Returns the square of the distance from this

Point2D

to a specified point.

**Parameters:** px

- the X coordinate of the specified point to be measured
against this

Point2D
**Parameters:** py

- the Y coordinate of the specified point to be measured
against this

Point2D
**Returns:** the square of the distance between this

Point2D

and the specified point.
**Since:** 1.2

---

#### distanceSq

public double distanceSq​(double px,
double py)

Returns the square of the distance from this

Point2D

to a specified point.

distanceSq

```java
public double distanceSq​(
Point2D
pt)
```

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

**Parameters:** pt

- the specified point to be measured
against this

Point2D
**Returns:** the square of the distance between this

Point2D

to a specified

Point2D

.
**Since:** 1.2

---

#### distanceSq

public double distanceSq​(

Point2D

pt)

Returns the square of the distance from this

Point2D

to a specified

Point2D

.

distance

```java
public double distance​(double px,
double py)
```

Returns the distance from this

Point2D

to
a specified point.

**Parameters:** px

- the X coordinate of the specified point to be measured
against this

Point2D
**Parameters:** py

- the Y coordinate of the specified point to be measured
against this

Point2D
**Returns:** the distance between this

Point2D

and a specified point.
**Since:** 1.2

---

#### distance

public double distance​(double px,
double py)

Returns the distance from this

Point2D

to
a specified point.

distance

```java
public double distance​(
Point2D
pt)
```

Returns the distance from this

Point2D

to a
specified

Point2D

.

**Parameters:** pt

- the specified point to be measured
against this

Point2D
**Returns:** the distance between this

Point2D

and
the specified

Point2D

.
**Since:** 1.2

---

#### distance

public double distance​(

Point2D

pt)

Returns the distance from this

Point2D

to a
specified

Point2D

.

clone

```java
public
Object
clone()
```

Creates a new object of the same class and with the
same contents as this object.

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

Creates a new object of the same class and with the
same contents as this object.

hashCode

```java
public int hashCode()
```

Returns the hashcode for this

Point2D

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

Point2D

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashcode for this

Point2D

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

Object
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
**Since:** 1.2
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

---

