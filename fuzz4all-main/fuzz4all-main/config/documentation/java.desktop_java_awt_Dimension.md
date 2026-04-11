# Class Dimension

**Source:** `java.desktop\java\awt\Dimension.html`

### Class Description

```java
public class
Dimension

extends
Dimension2D

implements
Serializable
```

The

Dimension

class encapsulates the width and
height of a component (in integer precision) in a single object.
The class is
associated with certain properties of components. Several methods
defined by the

Component

class and the

LayoutManager

interface return a

Dimension

object.

Normally the values of

width

and

height

are non-negative integers.
The constructors that allow you to create a dimension do
not prevent you from setting a negative value for these properties.
If the value of

width

or

height

is
negative, the behavior of some methods defined by other objects is
undefined.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public int width

The width dimension; negative values can be used.

**See Also:**
- getSize()

,

setSize(double, double)

**Since:**
- 1.0

---

#### public int height

The height dimension; negative values can be used.

**See Also:**
- getSize()

,

setSize(double, double)

**Since:**
- 1.0

---

### Constructor Details

#### public Dimension()

Creates an instance of

Dimension

with a width
of zero and a height of zero.

---

#### public Dimension​(
Dimension
d)

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

**Parameters:**
- d

- the specified dimension for the

width

and

height

values

---

#### public Dimension​(int width,
int height)

Constructs a

Dimension

and initializes
it to the specified width and specified height.

**Parameters:**
- width

- the specified width
- height

- the specified height

---

### Method Details

#### public double getWidth()

Returns the width of this

Dimension

in double
precision.

**Specified by:**
- getWidth

in class

Dimension2D

**Returns:**
- the width of this

Dimension

.

**Since:**
- 1.2

---

#### public double getHeight()

Returns the height of this

Dimension

in double
precision.

**Specified by:**
- getHeight

in class

Dimension2D

**Returns:**
- the height of this

Dimension

.

**Since:**
- 1.2

---

#### public void setSize​(double width,
double height)

Sets the size of this

Dimension

object to
the specified width and height in double precision.
Note that if

width

or

height

are larger than

Integer.MAX_VALUE

, they will
be reset to

Integer.MAX_VALUE

.

**Specified by:**
- setSize

in class

Dimension2D

**Parameters:**
- width

- the new width for the

Dimension

object
- height

- the new height for the

Dimension

object

**Since:**
- 1.2

---

#### public
Dimension
getSize()

Gets the size of this

Dimension

object.
This method is included for completeness, to parallel the

getSize

method defined by

Component

.

**Returns:**
- the size of this dimension, a new instance of

Dimension

with the same width and height

**See Also:**
- setSize(double, double)

,

Component.getSize()

**Since:**
- 1.1

---

#### public void setSize​(
Dimension
d)

Sets the size of this

Dimension

object to the specified size.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:**
- d

- the new size for this

Dimension

object

**See Also:**
- getSize()

,

Component.setSize(int, int)

**Since:**
- 1.1

---

#### public void setSize​(int width,
int height)

Sets the size of this

Dimension

object
to the specified width and height.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:**
- width

- the new width for this

Dimension

object
- height

- the new height for this

Dimension

object

**See Also:**
- getSize()

,

Component.setSize(int, int)

**Since:**
- 1.1

---

#### public boolean equals​(
Object
obj)

Checks whether two dimension objects have equal values.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code for this

Dimension

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

Dimension

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields. This method is intended to be used only
for debugging purposes, and the content and format of the returned
string may vary between implementations. The returned string may be
empty but may not be

null

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

Dimension

object

---

### Additional Sections

#### Class Dimension

java.lang.Object

- java.awt.geom.Dimension2D
- - java.awt.Dimension

java.awt.geom.Dimension2D

- java.awt.Dimension

java.awt.Dimension

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** DimensionUIResource

```java
public class
Dimension

extends
Dimension2D

implements
Serializable
```

The

Dimension

class encapsulates the width and
height of a component (in integer precision) in a single object.
The class is
associated with certain properties of components. Several methods
defined by the

Component

class and the

LayoutManager

interface return a

Dimension

object.

Normally the values of

width

and

height

are non-negative integers.
The constructors that allow you to create a dimension do
not prevent you from setting a negative value for these properties.
If the value of

width

or

height

is
negative, the behavior of some methods defined by other objects is
undefined.

**Since:** 1.0
**See Also:** Component

,

LayoutManager

,

Serialized Form

public class

Dimension

extends

Dimension2D

implements

Serializable

The

Dimension

class encapsulates the width and
height of a component (in integer precision) in a single object.
The class is
associated with certain properties of components. Several methods
defined by the

Component

class and the

LayoutManager

interface return a

Dimension

object.

Normally the values of

width

and

height

are non-negative integers.
The constructors that allow you to create a dimension do
not prevent you from setting a negative value for these properties.
If the value of

width

or

height

is
negative, the behavior of some methods defined by other objects is
undefined.

Normally the values of

width

and

height

are non-negative integers.
The constructors that allow you to create a dimension do
not prevent you from setting a negative value for these properties.
If the value of

width

or

height

is
negative, the behavior of some methods defined by other objects is
undefined.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

int

height

The height dimension; negative values can be used.

int

width

The width dimension; negative values can be used.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Dimension

()

Creates an instance of

Dimension

with a width
of zero and a height of zero.

Dimension

​(int width,
int height)

Constructs a

Dimension

and initializes
it to the specified width and specified height.

Dimension

​(

Dimension

d)

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

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

Checks whether two dimension objects have equal values.

double

getHeight

()

Returns the height of this

Dimension

in double
precision.

Dimension

getSize

()

Gets the size of this

Dimension

object.

double

getWidth

()

Returns the width of this

Dimension

in double
precision.

int

hashCode

()

Returns the hash code for this

Dimension

.

void

setSize

​(double width,
double height)

Sets the size of this

Dimension

object to
the specified width and height in double precision.

void

setSize

​(int width,
int height)

Sets the size of this

Dimension

object
to the specified width and height.

void

setSize

​(

Dimension

d)

Sets the size of this

Dimension

object to the specified size.

String

toString

()

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields.

- Methods declared in class java.awt.geom.

Dimension2D

clone

,

setSize

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

int

height

The height dimension; negative values can be used.

int

width

The width dimension; negative values can be used.

---

#### Field Summary

The height dimension; negative values can be used.

The width dimension; negative values can be used.

Constructor Summary

Constructors

Constructor

Description

Dimension

()

Creates an instance of

Dimension

with a width
of zero and a height of zero.

Dimension

​(int width,
int height)

Constructs a

Dimension

and initializes
it to the specified width and specified height.

Dimension

​(

Dimension

d)

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

---

#### Constructor Summary

Creates an instance of

Dimension

with a width
of zero and a height of zero.

Constructs a

Dimension

and initializes
it to the specified width and specified height.

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

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

Checks whether two dimension objects have equal values.

double

getHeight

()

Returns the height of this

Dimension

in double
precision.

Dimension

getSize

()

Gets the size of this

Dimension

object.

double

getWidth

()

Returns the width of this

Dimension

in double
precision.

int

hashCode

()

Returns the hash code for this

Dimension

.

void

setSize

​(double width,
double height)

Sets the size of this

Dimension

object to
the specified width and height in double precision.

void

setSize

​(int width,
int height)

Sets the size of this

Dimension

object
to the specified width and height.

void

setSize

​(

Dimension

d)

Sets the size of this

Dimension

object to the specified size.

String

toString

()

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields.

- Methods declared in class java.awt.geom.

Dimension2D

clone

,

setSize

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

Checks whether two dimension objects have equal values.

Returns the height of this

Dimension

in double
precision.

Gets the size of this

Dimension

object.

Returns the width of this

Dimension

in double
precision.

Returns the hash code for this

Dimension

.

Sets the size of this

Dimension

object to
the specified width and height in double precision.

Sets the size of this

Dimension

object
to the specified width and height.

Sets the size of this

Dimension

object to the specified size.

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields.

Methods declared in class java.awt.geom.

Dimension2D

clone

,

setSize

---

#### Methods declared in class java.awt.geom. Dimension2D

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

- width

```java
public int width
```

The width dimension; negative values can be used.

**Since:** 1.0
**See Also:** getSize()

,

setSize(double, double)

- height

```java
public int height
```

The height dimension; negative values can be used.

**Since:** 1.0
**See Also:** getSize()

,

setSize(double, double)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Dimension

```java
public Dimension()
```

Creates an instance of

Dimension

with a width
of zero and a height of zero.

- Dimension

```java
public Dimension​(
Dimension
d)
```

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

**Parameters:** d

- the specified dimension for the

width

and

height

values

- Dimension

```java
public Dimension​(int width,
int height)
```

Constructs a

Dimension

and initializes
it to the specified width and specified height.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height

============ METHOD DETAIL ==========

- Method Detail

- getWidth

```java
public double getWidth()
```

Returns the width of this

Dimension

in double
precision.

**Specified by:** getWidth

in class

Dimension2D
**Returns:** the width of this

Dimension

.
**Since:** 1.2

- getHeight

```java
public double getHeight()
```

Returns the height of this

Dimension

in double
precision.

**Specified by:** getHeight

in class

Dimension2D
**Returns:** the height of this

Dimension

.
**Since:** 1.2

- setSize

```java
public void setSize​(double width,
double height)
```

Sets the size of this

Dimension

object to
the specified width and height in double precision.
Note that if

width

or

height

are larger than

Integer.MAX_VALUE

, they will
be reset to

Integer.MAX_VALUE

.

**Specified by:** setSize

in class

Dimension2D
**Parameters:** width

- the new width for the

Dimension

object
**Parameters:** height

- the new height for the

Dimension

object
**Since:** 1.2

- getSize

```java
public
Dimension
getSize()
```

Gets the size of this

Dimension

object.
This method is included for completeness, to parallel the

getSize

method defined by

Component

.

**Returns:** the size of this dimension, a new instance of

Dimension

with the same width and height
**Since:** 1.1
**See Also:** setSize(double, double)

,

Component.getSize()

- setSize

```java
public void setSize​(
Dimension
d)
```

Sets the size of this

Dimension

object to the specified size.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:** d

- the new size for this

Dimension

object
**Since:** 1.1
**See Also:** getSize()

,

Component.setSize(int, int)

- setSize

```java
public void setSize​(int width,
int height)
```

Sets the size of this

Dimension

object
to the specified width and height.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:** width

- the new width for this

Dimension

object
**Parameters:** height

- the new height for this

Dimension

object
**Since:** 1.1
**See Also:** getSize()

,

Component.setSize(int, int)

- equals

```java
public boolean equals​(
Object
obj)
```

Checks whether two dimension objects have equal values.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this

Dimension

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

Dimension
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields. This method is intended to be used only
for debugging purposes, and the content and format of the returned
string may vary between implementations. The returned string may be
empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Dimension

object

Field Detail

- width

```java
public int width
```

The width dimension; negative values can be used.

**Since:** 1.0
**See Also:** getSize()

,

setSize(double, double)

- height

```java
public int height
```

The height dimension; negative values can be used.

**Since:** 1.0
**See Also:** getSize()

,

setSize(double, double)

---

#### Field Detail

width

```java
public int width
```

The width dimension; negative values can be used.

**Since:** 1.0
**See Also:** getSize()

,

setSize(double, double)

---

#### width

public int width

The width dimension; negative values can be used.

height

```java
public int height
```

The height dimension; negative values can be used.

**Since:** 1.0
**See Also:** getSize()

,

setSize(double, double)

---

#### height

public int height

The height dimension; negative values can be used.

Constructor Detail

- Dimension

```java
public Dimension()
```

Creates an instance of

Dimension

with a width
of zero and a height of zero.

- Dimension

```java
public Dimension​(
Dimension
d)
```

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

**Parameters:** d

- the specified dimension for the

width

and

height

values

- Dimension

```java
public Dimension​(int width,
int height)
```

Constructs a

Dimension

and initializes
it to the specified width and specified height.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height

---

#### Constructor Detail

Dimension

```java
public Dimension()
```

Creates an instance of

Dimension

with a width
of zero and a height of zero.

---

#### Dimension

public Dimension()

Creates an instance of

Dimension

with a width
of zero and a height of zero.

Dimension

```java
public Dimension​(
Dimension
d)
```

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

**Parameters:** d

- the specified dimension for the

width

and

height

values

---

#### Dimension

public Dimension​(

Dimension

d)

Creates an instance of

Dimension

whose width
and height are the same as for the specified dimension.

Dimension

```java
public Dimension​(int width,
int height)
```

Constructs a

Dimension

and initializes
it to the specified width and specified height.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height

---

#### Dimension

public Dimension​(int width,
int height)

Constructs a

Dimension

and initializes
it to the specified width and specified height.

Method Detail

- getWidth

```java
public double getWidth()
```

Returns the width of this

Dimension

in double
precision.

**Specified by:** getWidth

in class

Dimension2D
**Returns:** the width of this

Dimension

.
**Since:** 1.2

- getHeight

```java
public double getHeight()
```

Returns the height of this

Dimension

in double
precision.

**Specified by:** getHeight

in class

Dimension2D
**Returns:** the height of this

Dimension

.
**Since:** 1.2

- setSize

```java
public void setSize​(double width,
double height)
```

Sets the size of this

Dimension

object to
the specified width and height in double precision.
Note that if

width

or

height

are larger than

Integer.MAX_VALUE

, they will
be reset to

Integer.MAX_VALUE

.

**Specified by:** setSize

in class

Dimension2D
**Parameters:** width

- the new width for the

Dimension

object
**Parameters:** height

- the new height for the

Dimension

object
**Since:** 1.2

- getSize

```java
public
Dimension
getSize()
```

Gets the size of this

Dimension

object.
This method is included for completeness, to parallel the

getSize

method defined by

Component

.

**Returns:** the size of this dimension, a new instance of

Dimension

with the same width and height
**Since:** 1.1
**See Also:** setSize(double, double)

,

Component.getSize()

- setSize

```java
public void setSize​(
Dimension
d)
```

Sets the size of this

Dimension

object to the specified size.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:** d

- the new size for this

Dimension

object
**Since:** 1.1
**See Also:** getSize()

,

Component.setSize(int, int)

- setSize

```java
public void setSize​(int width,
int height)
```

Sets the size of this

Dimension

object
to the specified width and height.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:** width

- the new width for this

Dimension

object
**Parameters:** height

- the new height for this

Dimension

object
**Since:** 1.1
**See Also:** getSize()

,

Component.setSize(int, int)

- equals

```java
public boolean equals​(
Object
obj)
```

Checks whether two dimension objects have equal values.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this

Dimension

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

Dimension
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields. This method is intended to be used only
for debugging purposes, and the content and format of the returned
string may vary between implementations. The returned string may be
empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Dimension

object

---

#### Method Detail

getWidth

```java
public double getWidth()
```

Returns the width of this

Dimension

in double
precision.

**Specified by:** getWidth

in class

Dimension2D
**Returns:** the width of this

Dimension

.
**Since:** 1.2

---

#### getWidth

public double getWidth()

Returns the width of this

Dimension

in double
precision.

getHeight

```java
public double getHeight()
```

Returns the height of this

Dimension

in double
precision.

**Specified by:** getHeight

in class

Dimension2D
**Returns:** the height of this

Dimension

.
**Since:** 1.2

---

#### getHeight

public double getHeight()

Returns the height of this

Dimension

in double
precision.

setSize

```java
public void setSize​(double width,
double height)
```

Sets the size of this

Dimension

object to
the specified width and height in double precision.
Note that if

width

or

height

are larger than

Integer.MAX_VALUE

, they will
be reset to

Integer.MAX_VALUE

.

**Specified by:** setSize

in class

Dimension2D
**Parameters:** width

- the new width for the

Dimension

object
**Parameters:** height

- the new height for the

Dimension

object
**Since:** 1.2

---

#### setSize

public void setSize​(double width,
double height)

Sets the size of this

Dimension

object to
the specified width and height in double precision.
Note that if

width

or

height

are larger than

Integer.MAX_VALUE

, they will
be reset to

Integer.MAX_VALUE

.

getSize

```java
public
Dimension
getSize()
```

Gets the size of this

Dimension

object.
This method is included for completeness, to parallel the

getSize

method defined by

Component

.

**Returns:** the size of this dimension, a new instance of

Dimension

with the same width and height
**Since:** 1.1
**See Also:** setSize(double, double)

,

Component.getSize()

---

#### getSize

public

Dimension

getSize()

Gets the size of this

Dimension

object.
This method is included for completeness, to parallel the

getSize

method defined by

Component

.

setSize

```java
public void setSize​(
Dimension
d)
```

Sets the size of this

Dimension

object to the specified size.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:** d

- the new size for this

Dimension

object
**Since:** 1.1
**See Also:** getSize()

,

Component.setSize(int, int)

---

#### setSize

public void setSize​(

Dimension

d)

Sets the size of this

Dimension

object to the specified size.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

setSize

```java
public void setSize​(int width,
int height)
```

Sets the size of this

Dimension

object
to the specified width and height.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

**Parameters:** width

- the new width for this

Dimension

object
**Parameters:** height

- the new height for this

Dimension

object
**Since:** 1.1
**See Also:** getSize()

,

Component.setSize(int, int)

---

#### setSize

public void setSize​(int width,
int height)

Sets the size of this

Dimension

object
to the specified width and height.
This method is included for completeness, to parallel the

setSize

method defined by

Component

.

equals

```java
public boolean equals​(
Object
obj)
```

Checks whether two dimension objects have equal values.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

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

Checks whether two dimension objects have equal values.

hashCode

```java
public int hashCode()
```

Returns the hash code for this

Dimension

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

Dimension
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code for this

Dimension

.

toString

```java
public
String
toString()
```

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields. This method is intended to be used only
for debugging purposes, and the content and format of the returned
string may vary between implementations. The returned string may be
empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Dimension

object

---

#### toString

public

String

toString()

Returns a string representation of the values of this

Dimension

object's

height

and

width

fields. This method is intended to be used only
for debugging purposes, and the content and format of the returned
string may vary between implementations. The returned string may be
empty but may not be

null

.

---

