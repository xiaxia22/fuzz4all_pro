# Class GeneralPath

**Source:** `java.desktop\java\awt\geom\GeneralPath.html`

### Class Description

```java
public final class
GeneralPath

extends
Path2D.Float
```

The

GeneralPath

class represents a geometric path
constructed from straight lines, and quadratic and cubic
(Bézier) curves. It can contain multiple subpaths.

GeneralPath

is a legacy final class which exactly
implements the behavior of its superclass

Path2D.Float

.
Together with

Path2D.Double

, the

Path2D

classes
provide full implementations of a general geometric path that
support all of the functionality of the

Shape

and

PathIterator

interfaces with the ability to explicitly
select different levels of internal coordinate precision.

Use

Path2D.Float

(or this legacy

GeneralPath

subclass) when dealing with data that can be represented
and used with floating point precision. Use

Path2D.Double

for data that requires the accuracy or range of double precision.

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public GeneralPath()

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

**Since:**
- 1.2

---

#### public GeneralPath​(int rule)

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

**Parameters:**
- rule

- the winding rule

**See Also:**
- Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

**Since:**
- 1.2

---

#### public GeneralPath​(int rule,
int initialCapacity)

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.
This number is an initial guess as to how many path segments
will be added to the path, but the storage is expanded as
needed to store whatever path segments are added.

**Parameters:**
- rule

- the winding rule
- initialCapacity

- the estimate for the number of path segments
in the path

**See Also:**
- Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

**Since:**
- 1.2

---

#### public GeneralPath​(
Shape
s)

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.
All of the initial geometry and the winding rule for this path are
taken from the specified

Shape

object.

**Parameters:**
- s

- the specified

Shape

object

**Since:**
- 1.2

---

### Method Details

*No entries found.*

### Additional Sections

#### Class GeneralPath

java.lang.Object

- java.awt.geom.Path2D
- - java.awt.geom.Path2D.Float
- - java.awt.geom.GeneralPath

java.awt.geom.Path2D

- java.awt.geom.Path2D.Float
- - java.awt.geom.GeneralPath

java.awt.geom.Path2D.Float

- java.awt.geom.GeneralPath

java.awt.geom.GeneralPath

**All Implemented Interfaces:** Shape

,

Serializable

,

Cloneable

```java
public final class
GeneralPath

extends
Path2D.Float
```

The

GeneralPath

class represents a geometric path
constructed from straight lines, and quadratic and cubic
(Bézier) curves. It can contain multiple subpaths.

GeneralPath

is a legacy final class which exactly
implements the behavior of its superclass

Path2D.Float

.
Together with

Path2D.Double

, the

Path2D

classes
provide full implementations of a general geometric path that
support all of the functionality of the

Shape

and

PathIterator

interfaces with the ability to explicitly
select different levels of internal coordinate precision.

Use

Path2D.Float

(or this legacy

GeneralPath

subclass) when dealing with data that can be represented
and used with floating point precision. Use

Path2D.Double

for data that requires the accuracy or range of double precision.

**Since:** 1.2
**See Also:** Serialized Form

public final class

GeneralPath

extends

Path2D.Float

The

GeneralPath

class represents a geometric path
constructed from straight lines, and quadratic and cubic
(Bézier) curves. It can contain multiple subpaths.

GeneralPath

is a legacy final class which exactly
implements the behavior of its superclass

Path2D.Float

.
Together with

Path2D.Double

, the

Path2D

classes
provide full implementations of a general geometric path that
support all of the functionality of the

Shape

and

PathIterator

interfaces with the ability to explicitly
select different levels of internal coordinate precision.

Use

Path2D.Float

(or this legacy

GeneralPath

subclass) when dealing with data that can be represented
and used with floating point precision. Use

Path2D.Double

for data that requires the accuracy or range of double precision.

GeneralPath

is a legacy final class which exactly
implements the behavior of its superclass

Path2D.Float

.
Together with

Path2D.Double

, the

Path2D

classes
provide full implementations of a general geometric path that
support all of the functionality of the

Shape

and

PathIterator

interfaces with the ability to explicitly
select different levels of internal coordinate precision.

Use

Path2D.Float

(or this legacy

GeneralPath

subclass) when dealing with data that can be represented
and used with floating point precision. Use

Path2D.Double

for data that requires the accuracy or range of double precision.

Use

Path2D.Float

(or this legacy

GeneralPath

subclass) when dealing with data that can be represented
and used with floating point precision. Use

Path2D.Double

for data that requires the accuracy or range of double precision.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Path2D

Path2D.Double

,

Path2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.geom.

Path2D

WIND_EVEN_ODD

,

WIND_NON_ZERO

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GeneralPath

()

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

GeneralPath

​(int rule)

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

GeneralPath

​(int rule,
int initialCapacity)

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.

GeneralPath

​(

Shape

s)

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.awt.geom.

Path2D.Float

append

,

clone

,

curveTo

,

curveTo

,

getBounds2D

,

getPathIterator

,

lineTo

,

lineTo

,

moveTo

,

moveTo

,

quadTo

,

quadTo

,

transform

- Methods declared in class java.awt.geom.

Path2D

append

,

closePath

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

createTransformedShape

,

getBounds

,

getCurrentPoint

,

getPathIterator

,

getWindingRule

,

intersects

,

intersects

,

intersects

,

intersects

,

reset

,

setWindingRule

,

trimToSize

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

Path2D

Path2D.Double

,

Path2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

Path2D

Path2D.Double

,

Path2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. Path2D

Field Summary

- Fields declared in class java.awt.geom.

Path2D

WIND_EVEN_ODD

,

WIND_NON_ZERO

---

#### Field Summary

Fields declared in class java.awt.geom.

Path2D

WIND_EVEN_ODD

,

WIND_NON_ZERO

---

#### Fields declared in class java.awt.geom. Path2D

Constructor Summary

Constructors

Constructor

Description

GeneralPath

()

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

GeneralPath

​(int rule)

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

GeneralPath

​(int rule,
int initialCapacity)

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.

GeneralPath

​(

Shape

s)

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.

---

#### Constructor Summary

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.

Method Summary

- Methods declared in class java.awt.geom.

Path2D.Float

append

,

clone

,

curveTo

,

curveTo

,

getBounds2D

,

getPathIterator

,

lineTo

,

lineTo

,

moveTo

,

moveTo

,

quadTo

,

quadTo

,

transform

- Methods declared in class java.awt.geom.

Path2D

append

,

closePath

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

createTransformedShape

,

getBounds

,

getCurrentPoint

,

getPathIterator

,

getWindingRule

,

intersects

,

intersects

,

intersects

,

intersects

,

reset

,

setWindingRule

,

trimToSize

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

Methods declared in class java.awt.geom.

Path2D.Float

append

,

clone

,

curveTo

,

curveTo

,

getBounds2D

,

getPathIterator

,

lineTo

,

lineTo

,

moveTo

,

moveTo

,

quadTo

,

quadTo

,

transform

---

#### Methods declared in class java.awt.geom. Path2D.Float

Methods declared in class java.awt.geom.

Path2D

append

,

closePath

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

contains

,

createTransformedShape

,

getBounds

,

getCurrentPoint

,

getPathIterator

,

getWindingRule

,

intersects

,

intersects

,

intersects

,

intersects

,

reset

,

setWindingRule

,

trimToSize

---

#### Methods declared in class java.awt.geom. Path2D

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GeneralPath

```java
public GeneralPath()
```

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

**Since:** 1.2

- GeneralPath

```java
public GeneralPath​(int rule)
```

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

**Parameters:** rule

- the winding rule
**Since:** 1.2
**See Also:** Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

- GeneralPath

```java
public GeneralPath​(int rule,
int initialCapacity)
```

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.
This number is an initial guess as to how many path segments
will be added to the path, but the storage is expanded as
needed to store whatever path segments are added.

**Parameters:** rule

- the winding rule
**Parameters:** initialCapacity

- the estimate for the number of path segments
in the path
**Since:** 1.2
**See Also:** Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

- GeneralPath

```java
public GeneralPath​(
Shape
s)
```

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.
All of the initial geometry and the winding rule for this path are
taken from the specified

Shape

object.

**Parameters:** s

- the specified

Shape

object
**Since:** 1.2

Constructor Detail

- GeneralPath

```java
public GeneralPath()
```

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

**Since:** 1.2

- GeneralPath

```java
public GeneralPath​(int rule)
```

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

**Parameters:** rule

- the winding rule
**Since:** 1.2
**See Also:** Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

- GeneralPath

```java
public GeneralPath​(int rule,
int initialCapacity)
```

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.
This number is an initial guess as to how many path segments
will be added to the path, but the storage is expanded as
needed to store whatever path segments are added.

**Parameters:** rule

- the winding rule
**Parameters:** initialCapacity

- the estimate for the number of path segments
in the path
**Since:** 1.2
**See Also:** Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

- GeneralPath

```java
public GeneralPath​(
Shape
s)
```

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.
All of the initial geometry and the winding rule for this path are
taken from the specified

Shape

object.

**Parameters:** s

- the specified

Shape

object
**Since:** 1.2

---

#### Constructor Detail

GeneralPath

```java
public GeneralPath()
```

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

**Since:** 1.2

---

#### GeneralPath

public GeneralPath()

Constructs a new empty single precision

GeneralPath

object
with a default winding rule of

Path2D.WIND_NON_ZERO

.

GeneralPath

```java
public GeneralPath​(int rule)
```

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

**Parameters:** rule

- the winding rule
**Since:** 1.2
**See Also:** Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

---

#### GeneralPath

public GeneralPath​(int rule)

Constructs a new

GeneralPath

object with the specified
winding rule to control operations that require the interior of the
path to be defined.

GeneralPath

```java
public GeneralPath​(int rule,
int initialCapacity)
```

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.
This number is an initial guess as to how many path segments
will be added to the path, but the storage is expanded as
needed to store whatever path segments are added.

**Parameters:** rule

- the winding rule
**Parameters:** initialCapacity

- the estimate for the number of path segments
in the path
**Since:** 1.2
**See Also:** Path2D.WIND_EVEN_ODD

,

Path2D.WIND_NON_ZERO

---

#### GeneralPath

public GeneralPath​(int rule,
int initialCapacity)

Constructs a new

GeneralPath

object with the specified
winding rule and the specified initial capacity to store path
coordinates.
This number is an initial guess as to how many path segments
will be added to the path, but the storage is expanded as
needed to store whatever path segments are added.

GeneralPath

```java
public GeneralPath​(
Shape
s)
```

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.
All of the initial geometry and the winding rule for this path are
taken from the specified

Shape

object.

**Parameters:** s

- the specified

Shape

object
**Since:** 1.2

---

#### GeneralPath

public GeneralPath​(

Shape

s)

Constructs a new

GeneralPath

object from an arbitrary

Shape

object.
All of the initial geometry and the winding rule for this path are
taken from the specified

Shape

object.

---

