# Class Insets

**Source:** `java.desktop\java\awt\Insets.html`

### Class Description

```java
public class
Insets

extends
Object

implements
Cloneable
,
Serializable
```

An

Insets

object is a representation of the borders
of a container. It specifies the space that a container must leave
at each of its edges. The space can be a border, a blank space, or
a title.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public int top

The inset from the top.
This value is added to the Top of the rectangle
to yield a new location for the Top.

**See Also:**
- clone()

---

#### public int left

The inset from the left.
This value is added to the Left of the rectangle
to yield a new location for the Left edge.

**See Also:**
- clone()

---

#### public int bottom

The inset from the bottom.
This value is subtracted from the Bottom of the rectangle
to yield a new location for the Bottom.

**See Also:**
- clone()

---

#### public int right

The inset from the right.
This value is subtracted from the Right of the rectangle
to yield a new location for the Right edge.

**See Also:**
- clone()

---

### Constructor Details

#### public Insets​(int top,
int left,
int bottom,
int right)

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

**Parameters:**
- top

- the inset from the top.
- left

- the inset from the left.
- bottom

- the inset from the bottom.
- right

- the inset from the right.

---

### Method Details

#### public void set​(int top,
int left,
int bottom,
int right)

Set top, left, bottom, and right to the specified values

**Parameters:**
- top

- the inset from the top.
- left

- the inset from the left.
- bottom

- the inset from the bottom.
- right

- the inset from the right.

**Since:**
- 1.5

---

#### public boolean equals​(
Object
obj)

Checks whether two insets objects are equal. Two instances
of

Insets

are equal if the four integer values
of the fields

top

,

left

,

bottom

, and

right

are all equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if the two insets are equal;
otherwise

false

.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.1

---

#### public int hashCode()

Returns the hash code for this Insets.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this Insets.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this

Insets

object.
This method is intended to be used only for debugging purposes, and
the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

Insets

object.

---

#### public
Object
clone()

Create a copy of this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a copy of this

Insets

object.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Insets

java.lang.Object

- java.awt.Insets

java.awt.Insets

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** InsetsUIResource

```java
public class
Insets

extends
Object

implements
Cloneable
,
Serializable
```

An

Insets

object is a representation of the borders
of a container. It specifies the space that a container must leave
at each of its edges. The space can be a border, a blank space, or
a title.

**Since:** 1.0
**See Also:** LayoutManager

,

Container

,

Serialized Form

public class

Insets

extends

Object

implements

Cloneable

,

Serializable

An

Insets

object is a representation of the borders
of a container. It specifies the space that a container must leave
at each of its edges. The space can be a border, a blank space, or
a title.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

int

bottom

The inset from the bottom.

int

left

The inset from the left.

int

right

The inset from the right.

int

top

The inset from the top.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Insets

​(int top,
int left,
int bottom,
int right)

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Create a copy of this object.

boolean

equals

​(

Object

obj)

Checks whether two insets objects are equal.

int

hashCode

()

Returns the hash code for this Insets.

void

set

​(int top,
int left,
int bottom,
int right)

Set top, left, bottom, and right to the specified values

String

toString

()

Returns a string representation of this

Insets

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

bottom

The inset from the bottom.

int

left

The inset from the left.

int

right

The inset from the right.

int

top

The inset from the top.

---

#### Field Summary

The inset from the bottom.

The inset from the left.

The inset from the right.

The inset from the top.

Constructor Summary

Constructors

Constructor

Description

Insets

​(int top,
int left,
int bottom,
int right)

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

---

#### Constructor Summary

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Create a copy of this object.

boolean

equals

​(

Object

obj)

Checks whether two insets objects are equal.

int

hashCode

()

Returns the hash code for this Insets.

void

set

​(int top,
int left,
int bottom,
int right)

Set top, left, bottom, and right to the specified values

String

toString

()

Returns a string representation of this

Insets

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

wait

,

wait

,

wait

---

#### Method Summary

Create a copy of this object.

Checks whether two insets objects are equal.

Returns the hash code for this Insets.

Set top, left, bottom, and right to the specified values

Returns a string representation of this

Insets

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- top

```java
public int top
```

The inset from the top.
This value is added to the Top of the rectangle
to yield a new location for the Top.

**See Also:** clone()

- left

```java
public int left
```

The inset from the left.
This value is added to the Left of the rectangle
to yield a new location for the Left edge.

**See Also:** clone()

- bottom

```java
public int bottom
```

The inset from the bottom.
This value is subtracted from the Bottom of the rectangle
to yield a new location for the Bottom.

**See Also:** clone()

- right

```java
public int right
```

The inset from the right.
This value is subtracted from the Right of the rectangle
to yield a new location for the Right edge.

**See Also:** clone()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Insets

```java
public Insets​(int top,
int left,
int bottom,
int right)
```

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

**Parameters:** top

- the inset from the top.
**Parameters:** left

- the inset from the left.
**Parameters:** bottom

- the inset from the bottom.
**Parameters:** right

- the inset from the right.

============ METHOD DETAIL ==========

- Method Detail

- set

```java
public void set​(int top,
int left,
int bottom,
int right)
```

Set top, left, bottom, and right to the specified values

**Parameters:** top

- the inset from the top.
**Parameters:** left

- the inset from the left.
**Parameters:** bottom

- the inset from the bottom.
**Parameters:** right

- the inset from the right.
**Since:** 1.5

- equals

```java
public boolean equals​(
Object
obj)
```

Checks whether two insets objects are equal. Two instances
of

Insets

are equal if the four integer values
of the fields

top

,

left

,

bottom

, and

right

are all equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if the two insets are equal;
otherwise

false

.
**Since:** 1.1
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this Insets.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this Insets.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

Insets

object.
This method is intended to be used only for debugging purposes, and
the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Insets

object.

- clone

```java
public
Object
clone()
```

Create a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

Insets

object.
**See Also:** Cloneable

Field Detail

- top

```java
public int top
```

The inset from the top.
This value is added to the Top of the rectangle
to yield a new location for the Top.

**See Also:** clone()

- left

```java
public int left
```

The inset from the left.
This value is added to the Left of the rectangle
to yield a new location for the Left edge.

**See Also:** clone()

- bottom

```java
public int bottom
```

The inset from the bottom.
This value is subtracted from the Bottom of the rectangle
to yield a new location for the Bottom.

**See Also:** clone()

- right

```java
public int right
```

The inset from the right.
This value is subtracted from the Right of the rectangle
to yield a new location for the Right edge.

**See Also:** clone()

---

#### Field Detail

top

```java
public int top
```

The inset from the top.
This value is added to the Top of the rectangle
to yield a new location for the Top.

**See Also:** clone()

---

#### top

public int top

The inset from the top.
This value is added to the Top of the rectangle
to yield a new location for the Top.

left

```java
public int left
```

The inset from the left.
This value is added to the Left of the rectangle
to yield a new location for the Left edge.

**See Also:** clone()

---

#### left

public int left

The inset from the left.
This value is added to the Left of the rectangle
to yield a new location for the Left edge.

bottom

```java
public int bottom
```

The inset from the bottom.
This value is subtracted from the Bottom of the rectangle
to yield a new location for the Bottom.

**See Also:** clone()

---

#### bottom

public int bottom

The inset from the bottom.
This value is subtracted from the Bottom of the rectangle
to yield a new location for the Bottom.

right

```java
public int right
```

The inset from the right.
This value is subtracted from the Right of the rectangle
to yield a new location for the Right edge.

**See Also:** clone()

---

#### right

public int right

The inset from the right.
This value is subtracted from the Right of the rectangle
to yield a new location for the Right edge.

Constructor Detail

- Insets

```java
public Insets​(int top,
int left,
int bottom,
int right)
```

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

**Parameters:** top

- the inset from the top.
**Parameters:** left

- the inset from the left.
**Parameters:** bottom

- the inset from the bottom.
**Parameters:** right

- the inset from the right.

---

#### Constructor Detail

Insets

```java
public Insets​(int top,
int left,
int bottom,
int right)
```

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

**Parameters:** top

- the inset from the top.
**Parameters:** left

- the inset from the left.
**Parameters:** bottom

- the inset from the bottom.
**Parameters:** right

- the inset from the right.

---

#### Insets

public Insets​(int top,
int left,
int bottom,
int right)

Creates and initializes a new

Insets

object with the
specified top, left, bottom, and right insets.

Method Detail

- set

```java
public void set​(int top,
int left,
int bottom,
int right)
```

Set top, left, bottom, and right to the specified values

**Parameters:** top

- the inset from the top.
**Parameters:** left

- the inset from the left.
**Parameters:** bottom

- the inset from the bottom.
**Parameters:** right

- the inset from the right.
**Since:** 1.5

- equals

```java
public boolean equals​(
Object
obj)
```

Checks whether two insets objects are equal. Two instances
of

Insets

are equal if the four integer values
of the fields

top

,

left

,

bottom

, and

right

are all equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if the two insets are equal;
otherwise

false

.
**Since:** 1.1
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this Insets.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this Insets.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

Insets

object.
This method is intended to be used only for debugging purposes, and
the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Insets

object.

- clone

```java
public
Object
clone()
```

Create a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

Insets

object.
**See Also:** Cloneable

---

#### Method Detail

set

```java
public void set​(int top,
int left,
int bottom,
int right)
```

Set top, left, bottom, and right to the specified values

**Parameters:** top

- the inset from the top.
**Parameters:** left

- the inset from the left.
**Parameters:** bottom

- the inset from the bottom.
**Parameters:** right

- the inset from the right.
**Since:** 1.5

---

#### set

public void set​(int top,
int left,
int bottom,
int right)

Set top, left, bottom, and right to the specified values

equals

```java
public boolean equals​(
Object
obj)
```

Checks whether two insets objects are equal. Two instances
of

Insets

are equal if the four integer values
of the fields

top

,

left

,

bottom

, and

right

are all equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if the two insets are equal;
otherwise

false

.
**Since:** 1.1
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks whether two insets objects are equal. Two instances
of

Insets

are equal if the four integer values
of the fields

top

,

left

,

bottom

, and

right

are all equal.

hashCode

```java
public int hashCode()
```

Returns the hash code for this Insets.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this Insets.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code for this Insets.

toString

```java
public
String
toString()
```

Returns a string representation of this

Insets

object.
This method is intended to be used only for debugging purposes, and
the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Insets

object.

---

#### toString

public

String

toString()

Returns a string representation of this

Insets

object.
This method is intended to be used only for debugging purposes, and
the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

clone

```java
public
Object
clone()
```

Create a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

Insets

object.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Create a copy of this object.

---

