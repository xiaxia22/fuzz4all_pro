# Class EllipticCurve

**Source:** `java.base\java\security\spec\EllipticCurve.html`

### Class Description

```java
public class
EllipticCurve

extends
Object
```

This immutable class holds the necessary values needed to represent
an elliptic curve.

**Since:** 1.5
**See Also:** ECField

,

ECFieldFp

,

ECFieldF2m

---

### Field Details

*No entries found.*

### Constructor Details

#### public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b)

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

**Parameters:**
- field

- the finite field that this elliptic curve is over.
- a

- the first coefficient of this elliptic curve.
- b

- the second coefficient of this elliptic curve.

**Throws:**
- NullPointerException

- if

field

,

a

, or

b

is null.
- IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

---

#### public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b,
byte[] seed)

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

**Parameters:**
- field

- the finite field that this elliptic curve is over.
- a

- the first coefficient of this elliptic curve.
- b

- the second coefficient of this elliptic curve.
- seed

- the bytes used during curve generation for later
validation. Contents of this array are copied to protect against
subsequent modification.

**Throws:**
- NullPointerException

- if

field

,

a

, or

b

is null.
- IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

---

### Method Details

#### public
ECField
getField()

Returns the finite field

field

that this
elliptic curve is over.

**Returns:**
- the field

field

that this curve
is over.

---

#### public
BigInteger
getA()

Returns the first coefficient

a

of the
elliptic curve.

**Returns:**
- the first coefficient

a

.

---

#### public
BigInteger
getB()

Returns the second coefficient

b

of the
elliptic curve.

**Returns:**
- the second coefficient

b

.

---

#### public byte[] getSeed()

Returns the seeding bytes

seed

used
during curve generation. May be null if not specified.

**Returns:**
- the seeding bytes

seed

. A new
array is returned each time this method is called.

---

#### public boolean equals​(
Object
obj)

Compares this elliptic curve for equality with the
specified object.

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
EllipticCurve and the field, A, and B match, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this elliptic curve.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value computed from the hash codes of the field, A,
and B, as follows:

```java
(field.hashCode() << 6) + (a.hashCode() << 4) + (b.hashCode() << 2)
```

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class EllipticCurve

java.lang.Object

- java.security.spec.EllipticCurve

java.security.spec.EllipticCurve

```java
public class
EllipticCurve

extends
Object
```

This immutable class holds the necessary values needed to represent
an elliptic curve.

**Since:** 1.5
**See Also:** ECField

,

ECFieldFp

,

ECFieldF2m

public class

EllipticCurve

extends

Object

This immutable class holds the necessary values needed to represent
an elliptic curve.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EllipticCurve

​(

ECField

field,

BigInteger

a,

BigInteger

b)

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

EllipticCurve

​(

ECField

field,

BigInteger

a,

BigInteger

b,
byte[] seed)

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

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

Compares this elliptic curve for equality with the
specified object.

BigInteger

getA

()

Returns the first coefficient

a

of the
elliptic curve.

BigInteger

getB

()

Returns the second coefficient

b

of the
elliptic curve.

ECField

getField

()

Returns the finite field

field

that this
elliptic curve is over.

byte[]

getSeed

()

Returns the seeding bytes

seed

used
during curve generation.

int

hashCode

()

Returns a hash code value for this elliptic curve.

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

Constructor Summary

Constructors

Constructor

Description

EllipticCurve

​(

ECField

field,

BigInteger

a,

BigInteger

b)

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

EllipticCurve

​(

ECField

field,

BigInteger

a,

BigInteger

b,
byte[] seed)

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

---

#### Constructor Summary

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

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

Compares this elliptic curve for equality with the
specified object.

BigInteger

getA

()

Returns the first coefficient

a

of the
elliptic curve.

BigInteger

getB

()

Returns the second coefficient

b

of the
elliptic curve.

ECField

getField

()

Returns the finite field

field

that this
elliptic curve is over.

byte[]

getSeed

()

Returns the seeding bytes

seed

used
during curve generation.

int

hashCode

()

Returns a hash code value for this elliptic curve.

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

Compares this elliptic curve for equality with the
specified object.

Returns the first coefficient

a

of the
elliptic curve.

Returns the second coefficient

b

of the
elliptic curve.

Returns the finite field

field

that this
elliptic curve is over.

Returns the seeding bytes

seed

used
during curve generation.

Returns a hash code value for this elliptic curve.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EllipticCurve

```java
public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b)
```

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

**Parameters:** field

- the finite field that this elliptic curve is over.
**Parameters:** a

- the first coefficient of this elliptic curve.
**Parameters:** b

- the second coefficient of this elliptic curve.
**Throws:** NullPointerException

- if

field

,

a

, or

b

is null.
**Throws:** IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

- EllipticCurve

```java
public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b,
byte[] seed)
```

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

**Parameters:** field

- the finite field that this elliptic curve is over.
**Parameters:** a

- the first coefficient of this elliptic curve.
**Parameters:** b

- the second coefficient of this elliptic curve.
**Parameters:** seed

- the bytes used during curve generation for later
validation. Contents of this array are copied to protect against
subsequent modification.
**Throws:** NullPointerException

- if

field

,

a

, or

b

is null.
**Throws:** IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

============ METHOD DETAIL ==========

- Method Detail

- getField

```java
public
ECField
getField()
```

Returns the finite field

field

that this
elliptic curve is over.

**Returns:** the field

field

that this curve
is over.

- getA

```java
public
BigInteger
getA()
```

Returns the first coefficient

a

of the
elliptic curve.

**Returns:** the first coefficient

a

.

- getB

```java
public
BigInteger
getB()
```

Returns the second coefficient

b

of the
elliptic curve.

**Returns:** the second coefficient

b

.

- getSeed

```java
public byte[] getSeed()
```

Returns the seeding bytes

seed

used
during curve generation. May be null if not specified.

**Returns:** the seeding bytes

seed

. A new
array is returned each time this method is called.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this elliptic curve for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance of
EllipticCurve and the field, A, and B match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this elliptic curve.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value computed from the hash codes of the field, A,
and B, as follows:

```java
(field.hashCode() << 6) + (a.hashCode() << 4) + (b.hashCode() << 2)
```
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- EllipticCurve

```java
public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b)
```

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

**Parameters:** field

- the finite field that this elliptic curve is over.
**Parameters:** a

- the first coefficient of this elliptic curve.
**Parameters:** b

- the second coefficient of this elliptic curve.
**Throws:** NullPointerException

- if

field

,

a

, or

b

is null.
**Throws:** IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

- EllipticCurve

```java
public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b,
byte[] seed)
```

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

**Parameters:** field

- the finite field that this elliptic curve is over.
**Parameters:** a

- the first coefficient of this elliptic curve.
**Parameters:** b

- the second coefficient of this elliptic curve.
**Parameters:** seed

- the bytes used during curve generation for later
validation. Contents of this array are copied to protect against
subsequent modification.
**Throws:** NullPointerException

- if

field

,

a

, or

b

is null.
**Throws:** IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

---

#### Constructor Detail

EllipticCurve

```java
public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b)
```

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

**Parameters:** field

- the finite field that this elliptic curve is over.
**Parameters:** a

- the first coefficient of this elliptic curve.
**Parameters:** b

- the second coefficient of this elliptic curve.
**Throws:** NullPointerException

- if

field

,

a

, or

b

is null.
**Throws:** IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

---

#### EllipticCurve

public EllipticCurve​(

ECField

field,

BigInteger

a,

BigInteger

b)

Creates an elliptic curve with the specified elliptic field

field

and the coefficients

a

and

b

.

EllipticCurve

```java
public EllipticCurve​(
ECField
field,

BigInteger
a,

BigInteger
b,
byte[] seed)
```

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

**Parameters:** field

- the finite field that this elliptic curve is over.
**Parameters:** a

- the first coefficient of this elliptic curve.
**Parameters:** b

- the second coefficient of this elliptic curve.
**Parameters:** seed

- the bytes used during curve generation for later
validation. Contents of this array are copied to protect against
subsequent modification.
**Throws:** NullPointerException

- if

field

,

a

, or

b

is null.
**Throws:** IllegalArgumentException

- if

a

or

b

is not null and not in

field

.

---

#### EllipticCurve

public EllipticCurve​(

ECField

field,

BigInteger

a,

BigInteger

b,
byte[] seed)

Creates an elliptic curve with the specified elliptic field

field

, the coefficients

a

and

b

, and the

seed

used for curve generation.

Method Detail

- getField

```java
public
ECField
getField()
```

Returns the finite field

field

that this
elliptic curve is over.

**Returns:** the field

field

that this curve
is over.

- getA

```java
public
BigInteger
getA()
```

Returns the first coefficient

a

of the
elliptic curve.

**Returns:** the first coefficient

a

.

- getB

```java
public
BigInteger
getB()
```

Returns the second coefficient

b

of the
elliptic curve.

**Returns:** the second coefficient

b

.

- getSeed

```java
public byte[] getSeed()
```

Returns the seeding bytes

seed

used
during curve generation. May be null if not specified.

**Returns:** the seeding bytes

seed

. A new
array is returned each time this method is called.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this elliptic curve for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance of
EllipticCurve and the field, A, and B match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this elliptic curve.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value computed from the hash codes of the field, A,
and B, as follows:

```java
(field.hashCode() << 6) + (a.hashCode() << 4) + (b.hashCode() << 2)
```
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getField

```java
public
ECField
getField()
```

Returns the finite field

field

that this
elliptic curve is over.

**Returns:** the field

field

that this curve
is over.

---

#### getField

public

ECField

getField()

Returns the finite field

field

that this
elliptic curve is over.

getA

```java
public
BigInteger
getA()
```

Returns the first coefficient

a

of the
elliptic curve.

**Returns:** the first coefficient

a

.

---

#### getA

public

BigInteger

getA()

Returns the first coefficient

a

of the
elliptic curve.

getB

```java
public
BigInteger
getB()
```

Returns the second coefficient

b

of the
elliptic curve.

**Returns:** the second coefficient

b

.

---

#### getB

public

BigInteger

getB()

Returns the second coefficient

b

of the
elliptic curve.

getSeed

```java
public byte[] getSeed()
```

Returns the seeding bytes

seed

used
during curve generation. May be null if not specified.

**Returns:** the seeding bytes

seed

. A new
array is returned each time this method is called.

---

#### getSeed

public byte[] getSeed()

Returns the seeding bytes

seed

used
during curve generation. May be null if not specified.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this elliptic curve for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance of
EllipticCurve and the field, A, and B match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this elliptic curve for equality with the
specified object.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this elliptic curve.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value computed from the hash codes of the field, A,
and B, as follows:

```java
(field.hashCode() << 6) + (a.hashCode() << 4) + (b.hashCode() << 2)
```
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this elliptic curve.

(field.hashCode() << 6) + (a.hashCode() << 4) + (b.hashCode() << 2)

---

