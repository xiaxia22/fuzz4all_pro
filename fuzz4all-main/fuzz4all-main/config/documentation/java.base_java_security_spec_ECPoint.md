# Class ECPoint

**Source:** `java.base\java\security\spec\ECPoint.html`

### Class Description

```java
public class
ECPoint

extends
Object
```

This immutable class represents a point on an elliptic curve (EC)
in affine coordinates. Other coordinate systems can
extend this class to represent this point in other
coordinates.

**Since:** 1.5

---

### Field Details

#### public static final
ECPoint
POINT_INFINITY

This defines the point at infinity.

---

### Constructor Details

#### public ECPoint​(
BigInteger
x,

BigInteger
y)

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

**Parameters:**
- x

- the affine x-coordinate.
- y

- the affine y-coordinate.

**Throws:**
- NullPointerException

- if

x

or

y

is null.

---

### Method Details

#### public
BigInteger
getAffineX()

Returns the affine x-coordinate

x

.
Note: POINT_INFINITY has a null affine x-coordinate.

**Returns:**
- the affine x-coordinate.

---

#### public
BigInteger
getAffineY()

Returns the affine y-coordinate

y

.
Note: POINT_INFINITY has a null affine y-coordinate.

**Returns:**
- the affine y-coordinate.

---

#### public boolean equals​(
Object
obj)

Compares this elliptic curve point for equality with
the specified object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared.

**Returns:**
- true if

obj

is an instance of
ECPoint and the affine coordinates match, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this elliptic curve point.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class ECPoint

java.lang.Object

- java.security.spec.ECPoint

java.security.spec.ECPoint

```java
public class
ECPoint

extends
Object
```

This immutable class represents a point on an elliptic curve (EC)
in affine coordinates. Other coordinate systems can
extend this class to represent this point in other
coordinates.

**Since:** 1.5

public class

ECPoint

extends

Object

This immutable class represents a point on an elliptic curve (EC)
in affine coordinates. Other coordinate systems can
extend this class to represent this point in other
coordinates.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ECPoint

POINT_INFINITY

This defines the point at infinity.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ECPoint

​(

BigInteger

x,

BigInteger

y)

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

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

Compares this elliptic curve point for equality with
the specified object.

BigInteger

getAffineX

()

Returns the affine x-coordinate

x

.

BigInteger

getAffineY

()

Returns the affine y-coordinate

y

.

int

hashCode

()

Returns a hash code value for this elliptic curve point.

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

ECPoint

POINT_INFINITY

This defines the point at infinity.

---

#### Field Summary

This defines the point at infinity.

Constructor Summary

Constructors

Constructor

Description

ECPoint

​(

BigInteger

x,

BigInteger

y)

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

---

#### Constructor Summary

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

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

Compares this elliptic curve point for equality with
the specified object.

BigInteger

getAffineX

()

Returns the affine x-coordinate

x

.

BigInteger

getAffineY

()

Returns the affine y-coordinate

y

.

int

hashCode

()

Returns a hash code value for this elliptic curve point.

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

Compares this elliptic curve point for equality with
the specified object.

Returns the affine x-coordinate

x

.

Returns the affine y-coordinate

y

.

Returns a hash code value for this elliptic curve point.

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

- POINT_INFINITY

```java
public static final
ECPoint
POINT_INFINITY
```

This defines the point at infinity.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ECPoint

```java
public ECPoint​(
BigInteger
x,

BigInteger
y)
```

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

**Parameters:** x

- the affine x-coordinate.
**Parameters:** y

- the affine y-coordinate.
**Throws:** NullPointerException

- if

x

or

y

is null.

============ METHOD DETAIL ==========

- Method Detail

- getAffineX

```java
public
BigInteger
getAffineX()
```

Returns the affine x-coordinate

x

.
Note: POINT_INFINITY has a null affine x-coordinate.

**Returns:** the affine x-coordinate.

- getAffineY

```java
public
BigInteger
getAffineY()
```

Returns the affine y-coordinate

y

.
Note: POINT_INFINITY has a null affine y-coordinate.

**Returns:** the affine y-coordinate.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this elliptic curve point for equality with
the specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance of
ECPoint and the affine coordinates match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this elliptic curve point.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Field Detail

- POINT_INFINITY

```java
public static final
ECPoint
POINT_INFINITY
```

This defines the point at infinity.

---

#### Field Detail

POINT_INFINITY

```java
public static final
ECPoint
POINT_INFINITY
```

This defines the point at infinity.

---

#### POINT_INFINITY

public static final

ECPoint

POINT_INFINITY

This defines the point at infinity.

Constructor Detail

- ECPoint

```java
public ECPoint​(
BigInteger
x,

BigInteger
y)
```

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

**Parameters:** x

- the affine x-coordinate.
**Parameters:** y

- the affine y-coordinate.
**Throws:** NullPointerException

- if

x

or

y

is null.

---

#### Constructor Detail

ECPoint

```java
public ECPoint​(
BigInteger
x,

BigInteger
y)
```

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

**Parameters:** x

- the affine x-coordinate.
**Parameters:** y

- the affine y-coordinate.
**Throws:** NullPointerException

- if

x

or

y

is null.

---

#### ECPoint

public ECPoint​(

BigInteger

x,

BigInteger

y)

Creates an ECPoint from the specified affine x-coordinate

x

and affine y-coordinate

y

.

Method Detail

- getAffineX

```java
public
BigInteger
getAffineX()
```

Returns the affine x-coordinate

x

.
Note: POINT_INFINITY has a null affine x-coordinate.

**Returns:** the affine x-coordinate.

- getAffineY

```java
public
BigInteger
getAffineY()
```

Returns the affine y-coordinate

y

.
Note: POINT_INFINITY has a null affine y-coordinate.

**Returns:** the affine y-coordinate.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this elliptic curve point for equality with
the specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance of
ECPoint and the affine coordinates match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this elliptic curve point.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getAffineX

```java
public
BigInteger
getAffineX()
```

Returns the affine x-coordinate

x

.
Note: POINT_INFINITY has a null affine x-coordinate.

**Returns:** the affine x-coordinate.

---

#### getAffineX

public

BigInteger

getAffineX()

Returns the affine x-coordinate

x

.
Note: POINT_INFINITY has a null affine x-coordinate.

getAffineY

```java
public
BigInteger
getAffineY()
```

Returns the affine y-coordinate

y

.
Note: POINT_INFINITY has a null affine y-coordinate.

**Returns:** the affine y-coordinate.

---

#### getAffineY

public

BigInteger

getAffineY()

Returns the affine y-coordinate

y

.
Note: POINT_INFINITY has a null affine y-coordinate.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this elliptic curve point for equality with
the specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance of
ECPoint and the affine coordinates match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this elliptic curve point for equality with
the specified object.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this elliptic curve point.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this elliptic curve point.

---

