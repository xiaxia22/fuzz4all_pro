# Class TransformAttribute

**Source:** `java.desktop\java\awt\font\TransformAttribute.html`

### Class Description

```java
public final class
TransformAttribute

extends
Object

implements
Serializable
```

The

TransformAttribute

class provides an immutable
wrapper for a transform so that it is safe to use as an attribute.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
TransformAttribute
IDENTITY

A

TransformAttribute

representing the identity transform.

**Since:**
- 1.6

---

### Constructor Details

#### public TransformAttribute​(
AffineTransform
transform)

Wraps the specified transform. The transform is cloned and a
reference to the clone is kept. The original transform is unchanged.
If null is passed as the argument, this constructor behaves as though
it were the identity transform. (Note that it is preferable to use

IDENTITY

in this case.)

**Parameters:**
- transform

- the specified

AffineTransform

to be wrapped,
or null.

---

### Method Details

#### public
AffineTransform
getTransform()

Returns a copy of the wrapped transform.

**Returns:**
- an

AffineTransform

that is a copy of the wrapped
transform of this

TransformAttribute

.

---

#### public boolean isIdentity()

Returns

true

if the wrapped transform is
an identity transform.

**Returns:**
- true

if the wrapped transform is
an identity transform;

false

otherwise.

**Since:**
- 1.4

---

#### public int hashCode()

Description copied from class:

Object

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.6

---

#### public boolean equals​(
Object
rhs)

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

**Overrides:**
- equals

in class

Object

**Parameters:**
- rhs

- the object to compare to

**Returns:**
- true

if the argument is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.6

---

### Additional Sections

#### Class TransformAttribute

java.lang.Object

- java.awt.font.TransformAttribute

java.awt.font.TransformAttribute

**All Implemented Interfaces:** Serializable

```java
public final class
TransformAttribute

extends
Object

implements
Serializable
```

The

TransformAttribute

class provides an immutable
wrapper for a transform so that it is safe to use as an attribute.

**See Also:** Serialized Form

public final class

TransformAttribute

extends

Object

implements

Serializable

The

TransformAttribute

class provides an immutable
wrapper for a transform so that it is safe to use as an attribute.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

TransformAttribute

IDENTITY

A

TransformAttribute

representing the identity transform.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TransformAttribute

​(

AffineTransform

transform)

Wraps the specified transform.

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

rhs)

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

AffineTransform

getTransform

()

Returns a copy of the wrapped transform.

int

hashCode

()

Returns a hash code value for the object.

boolean

isIdentity

()

Returns

true

if the wrapped transform is
an identity transform.

- Methods declared in class java.lang.

Object

clone

,

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

Field Summary

Fields

Modifier and Type

Field

Description

static

TransformAttribute

IDENTITY

A

TransformAttribute

representing the identity transform.

---

#### Field Summary

A

TransformAttribute

representing the identity transform.

Constructor Summary

Constructors

Constructor

Description

TransformAttribute

​(

AffineTransform

transform)

Wraps the specified transform.

---

#### Constructor Summary

Wraps the specified transform.

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

rhs)

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

AffineTransform

getTransform

()

Returns a copy of the wrapped transform.

int

hashCode

()

Returns a hash code value for the object.

boolean

isIdentity

()

Returns

true

if the wrapped transform is
an identity transform.

- Methods declared in class java.lang.

Object

clone

,

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

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

Returns a copy of the wrapped transform.

Returns a hash code value for the object.

Returns

true

if the wrapped transform is
an identity transform.

Methods declared in class java.lang.

Object

clone

,

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

- IDENTITY

```java
public static final
TransformAttribute
IDENTITY
```

A

TransformAttribute

representing the identity transform.

**Since:** 1.6

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TransformAttribute

```java
public TransformAttribute​(
AffineTransform
transform)
```

Wraps the specified transform. The transform is cloned and a
reference to the clone is kept. The original transform is unchanged.
If null is passed as the argument, this constructor behaves as though
it were the identity transform. (Note that it is preferable to use

IDENTITY

in this case.)

**Parameters:** transform

- the specified

AffineTransform

to be wrapped,
or null.

============ METHOD DETAIL ==========

- Method Detail

- getTransform

```java
public
AffineTransform
getTransform()
```

Returns a copy of the wrapped transform.

**Returns:** an

AffineTransform

that is a copy of the wrapped
transform of this

TransformAttribute

.

- isIdentity

```java
public boolean isIdentity()
```

Returns

true

if the wrapped transform is
an identity transform.

**Returns:** true

if the wrapped transform is
an identity transform;

false

otherwise.
**Since:** 1.4

- hashCode

```java
public int hashCode()
```

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
rhs)
```

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

**Overrides:** equals

in class

Object
**Parameters:** rhs

- the object to compare to
**Returns:** true

if the argument is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

Field Detail

- IDENTITY

```java
public static final
TransformAttribute
IDENTITY
```

A

TransformAttribute

representing the identity transform.

**Since:** 1.6

---

#### Field Detail

IDENTITY

```java
public static final
TransformAttribute
IDENTITY
```

A

TransformAttribute

representing the identity transform.

**Since:** 1.6

---

#### IDENTITY

public static final

TransformAttribute

IDENTITY

A

TransformAttribute

representing the identity transform.

Constructor Detail

- TransformAttribute

```java
public TransformAttribute​(
AffineTransform
transform)
```

Wraps the specified transform. The transform is cloned and a
reference to the clone is kept. The original transform is unchanged.
If null is passed as the argument, this constructor behaves as though
it were the identity transform. (Note that it is preferable to use

IDENTITY

in this case.)

**Parameters:** transform

- the specified

AffineTransform

to be wrapped,
or null.

---

#### Constructor Detail

TransformAttribute

```java
public TransformAttribute​(
AffineTransform
transform)
```

Wraps the specified transform. The transform is cloned and a
reference to the clone is kept. The original transform is unchanged.
If null is passed as the argument, this constructor behaves as though
it were the identity transform. (Note that it is preferable to use

IDENTITY

in this case.)

**Parameters:** transform

- the specified

AffineTransform

to be wrapped,
or null.

---

#### TransformAttribute

public TransformAttribute​(

AffineTransform

transform)

Wraps the specified transform. The transform is cloned and a
reference to the clone is kept. The original transform is unchanged.
If null is passed as the argument, this constructor behaves as though
it were the identity transform. (Note that it is preferable to use

IDENTITY

in this case.)

Method Detail

- getTransform

```java
public
AffineTransform
getTransform()
```

Returns a copy of the wrapped transform.

**Returns:** an

AffineTransform

that is a copy of the wrapped
transform of this

TransformAttribute

.

- isIdentity

```java
public boolean isIdentity()
```

Returns

true

if the wrapped transform is
an identity transform.

**Returns:** true

if the wrapped transform is
an identity transform;

false

otherwise.
**Since:** 1.4

- hashCode

```java
public int hashCode()
```

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
rhs)
```

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

**Overrides:** equals

in class

Object
**Parameters:** rhs

- the object to compare to
**Returns:** true

if the argument is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getTransform

```java
public
AffineTransform
getTransform()
```

Returns a copy of the wrapped transform.

**Returns:** an

AffineTransform

that is a copy of the wrapped
transform of this

TransformAttribute

.

---

#### getTransform

public

AffineTransform

getTransform()

Returns a copy of the wrapped transform.

isIdentity

```java
public boolean isIdentity()
```

Returns

true

if the wrapped transform is
an identity transform.

**Returns:** true

if the wrapped transform is
an identity transform;

false

otherwise.
**Since:** 1.4

---

#### isIdentity

public boolean isIdentity()

Returns

true

if the wrapped transform is
an identity transform.

hashCode

```java
public int hashCode()
```

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Description copied from class:

Object

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by

HashMap

.

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

The general contract of

hashCode

is:

- Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

Whenever it is invoked on the same object more than once during
an execution of a Java application, the

hashCode

method
must consistently return the same integer, provided no information
used in

equals

comparisons on the object is modified.
This integer need not remain consistent from one execution of an
application to another execution of the same application.

If two objects are equal according to the

equals(Object)

method, then calling the

hashCode

method on each of
the two objects must produce the same integer result.

It is

not

required that if two objects are unequal
according to the

Object.equals(java.lang.Object)

method, then calling the

hashCode

method on each of the
two objects must produce distinct integer results. However, the
programmer should be aware that producing distinct integer results
for unequal objects may improve the performance of hash tables.

As much as is reasonably practical, the hashCode method defined
by class

Object

does return distinct integers for
distinct objects. (The hashCode may or may not be implemented
as some function of an object's memory address at some point
in time.)

equals

```java
public boolean equals​(
Object
rhs)
```

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

**Overrides:** equals

in class

Object
**Parameters:** rhs

- the object to compare to
**Returns:** true

if the argument is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

rhs)

Returns

true

if rhs is a

TransformAttribute

whose transform is equal to this

TransformAttribute

's
transform.

---

