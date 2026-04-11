# Class ECFieldFp

**Source:** `java.base\java\security\spec\ECFieldFp.html`

### Class Description

```java
public class
ECFieldFp

extends
Object

implements
ECField
```

This immutable class defines an elliptic curve (EC) prime
finite field.

**All Implemented Interfaces:** ECField

---

### Field Details

*No entries found.*

### Constructor Details

#### public ECFieldFp​(
BigInteger
p)

Creates an elliptic curve prime finite field
with the specified prime

p

.

**Parameters:**
- p

- the prime.

**Throws:**
- NullPointerException

- if

p

is null.
- IllegalArgumentException

- if

p

is not positive.

---

### Method Details

#### public int getFieldSize()

Returns the field size in bits which is size of prime p
for this prime finite field.

**Specified by:**
- getFieldSize

in interface

ECField

**Returns:**
- the field size in bits.

---

#### public
BigInteger
getP()

Returns the prime

p

of this prime finite field.

**Returns:**
- the prime.

---

#### public boolean equals​(
Object
obj)

Compares this prime finite field for equality with the
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

is an instance
of ECFieldFp and the prime value match, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this prime finite field.

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

#### Class ECFieldFp

java.lang.Object

- java.security.spec.ECFieldFp

java.security.spec.ECFieldFp

**All Implemented Interfaces:** ECField

```java
public class
ECFieldFp

extends
Object

implements
ECField
```

This immutable class defines an elliptic curve (EC) prime
finite field.

**Since:** 1.5
**See Also:** ECField

public class

ECFieldFp

extends

Object

implements

ECField

This immutable class defines an elliptic curve (EC) prime
finite field.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ECFieldFp

​(

BigInteger

p)

Creates an elliptic curve prime finite field
with the specified prime

p

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

Compares this prime finite field for equality with the
specified object.

int

getFieldSize

()

Returns the field size in bits which is size of prime p
for this prime finite field.

BigInteger

getP

()

Returns the prime

p

of this prime finite field.

int

hashCode

()

Returns a hash code value for this prime finite field.

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

ECFieldFp

​(

BigInteger

p)

Creates an elliptic curve prime finite field
with the specified prime

p

.

---

#### Constructor Summary

Creates an elliptic curve prime finite field
with the specified prime

p

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

Compares this prime finite field for equality with the
specified object.

int

getFieldSize

()

Returns the field size in bits which is size of prime p
for this prime finite field.

BigInteger

getP

()

Returns the prime

p

of this prime finite field.

int

hashCode

()

Returns a hash code value for this prime finite field.

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

Compares this prime finite field for equality with the
specified object.

Returns the field size in bits which is size of prime p
for this prime finite field.

Returns the prime

p

of this prime finite field.

Returns a hash code value for this prime finite field.

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

- ECFieldFp

```java
public ECFieldFp​(
BigInteger
p)
```

Creates an elliptic curve prime finite field
with the specified prime

p

.

**Parameters:** p

- the prime.
**Throws:** NullPointerException

- if

p

is null.
**Throws:** IllegalArgumentException

- if

p

is not positive.

============ METHOD DETAIL ==========

- Method Detail

- getFieldSize

```java
public int getFieldSize()
```

Returns the field size in bits which is size of prime p
for this prime finite field.

**Specified by:** getFieldSize

in interface

ECField
**Returns:** the field size in bits.

- getP

```java
public
BigInteger
getP()
```

Returns the prime

p

of this prime finite field.

**Returns:** the prime.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this prime finite field for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance
of ECFieldFp and the prime value match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this prime finite field.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- ECFieldFp

```java
public ECFieldFp​(
BigInteger
p)
```

Creates an elliptic curve prime finite field
with the specified prime

p

.

**Parameters:** p

- the prime.
**Throws:** NullPointerException

- if

p

is null.
**Throws:** IllegalArgumentException

- if

p

is not positive.

---

#### Constructor Detail

ECFieldFp

```java
public ECFieldFp​(
BigInteger
p)
```

Creates an elliptic curve prime finite field
with the specified prime

p

.

**Parameters:** p

- the prime.
**Throws:** NullPointerException

- if

p

is null.
**Throws:** IllegalArgumentException

- if

p

is not positive.

---

#### ECFieldFp

public ECFieldFp​(

BigInteger

p)

Creates an elliptic curve prime finite field
with the specified prime

p

.

Method Detail

- getFieldSize

```java
public int getFieldSize()
```

Returns the field size in bits which is size of prime p
for this prime finite field.

**Specified by:** getFieldSize

in interface

ECField
**Returns:** the field size in bits.

- getP

```java
public
BigInteger
getP()
```

Returns the prime

p

of this prime finite field.

**Returns:** the prime.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this prime finite field for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance
of ECFieldFp and the prime value match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this prime finite field.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getFieldSize

```java
public int getFieldSize()
```

Returns the field size in bits which is size of prime p
for this prime finite field.

**Specified by:** getFieldSize

in interface

ECField
**Returns:** the field size in bits.

---

#### getFieldSize

public int getFieldSize()

Returns the field size in bits which is size of prime p
for this prime finite field.

getP

```java
public
BigInteger
getP()
```

Returns the prime

p

of this prime finite field.

**Returns:** the prime.

---

#### getP

public

BigInteger

getP()

Returns the prime

p

of this prime finite field.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this prime finite field for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance
of ECFieldFp and the prime value match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this prime finite field for equality with the
specified object.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this prime finite field.

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

Returns a hash code value for this prime finite field.

---

