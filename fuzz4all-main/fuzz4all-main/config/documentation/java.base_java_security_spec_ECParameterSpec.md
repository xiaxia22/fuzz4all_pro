# Class ECParameterSpec

**Source:** `java.base\java\security\spec\ECParameterSpec.html`

### Class Description

```java
public class
ECParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This immutable class specifies the set of domain parameters
used with elliptic curve cryptography (ECC).

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public ECParameterSpec​(
EllipticCurve
curve,

ECPoint
g,

BigInteger
n,
int h)

Creates elliptic curve domain parameters based on the
specified values.

**Parameters:**
- curve

- the elliptic curve which this parameter
defines.
- g

- the generator which is also known as the base point.
- n

- the order of the generator

g

.
- h

- the cofactor.

**Throws:**
- NullPointerException

- if

curve

,

g

, or

n

is null.
- IllegalArgumentException

- if

n

or

h

is not positive.

---

### Method Details

#### public
EllipticCurve
getCurve()

Returns the elliptic curve that this parameter defines.

**Returns:**
- the elliptic curve that this parameter defines.

---

#### public
ECPoint
getGenerator()

Returns the generator which is also known as the base point.

**Returns:**
- the generator which is also known as the base point.

---

#### public
BigInteger
getOrder()

Returns the order of the generator.

**Returns:**
- the order of the generator.

---

#### public int getCofactor()

Returns the cofactor.

**Returns:**
- the cofactor.

---

### Additional Sections

#### Class ECParameterSpec

java.lang.Object

- java.security.spec.ECParameterSpec

java.security.spec.ECParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
ECParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This immutable class specifies the set of domain parameters
used with elliptic curve cryptography (ECC).

**Since:** 1.5
**See Also:** AlgorithmParameterSpec

public class

ECParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This immutable class specifies the set of domain parameters
used with elliptic curve cryptography (ECC).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ECParameterSpec

​(

EllipticCurve

curve,

ECPoint

g,

BigInteger

n,
int h)

Creates elliptic curve domain parameters based on the
specified values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getCofactor

()

Returns the cofactor.

EllipticCurve

getCurve

()

Returns the elliptic curve that this parameter defines.

ECPoint

getGenerator

()

Returns the generator which is also known as the base point.

BigInteger

getOrder

()

Returns the order of the generator.

- Methods declared in class java.lang.

Object

clone

,

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

Constructor Summary

Constructors

Constructor

Description

ECParameterSpec

​(

EllipticCurve

curve,

ECPoint

g,

BigInteger

n,
int h)

Creates elliptic curve domain parameters based on the
specified values.

---

#### Constructor Summary

Creates elliptic curve domain parameters based on the
specified values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getCofactor

()

Returns the cofactor.

EllipticCurve

getCurve

()

Returns the elliptic curve that this parameter defines.

ECPoint

getGenerator

()

Returns the generator which is also known as the base point.

BigInteger

getOrder

()

Returns the order of the generator.

- Methods declared in class java.lang.

Object

clone

,

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

Returns the cofactor.

Returns the elliptic curve that this parameter defines.

Returns the generator which is also known as the base point.

Returns the order of the generator.

Methods declared in class java.lang.

Object

clone

,

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

- ECParameterSpec

```java
public ECParameterSpec​(
EllipticCurve
curve,

ECPoint
g,

BigInteger
n,
int h)
```

Creates elliptic curve domain parameters based on the
specified values.

**Parameters:** curve

- the elliptic curve which this parameter
defines.
**Parameters:** g

- the generator which is also known as the base point.
**Parameters:** n

- the order of the generator

g

.
**Parameters:** h

- the cofactor.
**Throws:** NullPointerException

- if

curve

,

g

, or

n

is null.
**Throws:** IllegalArgumentException

- if

n

or

h

is not positive.

============ METHOD DETAIL ==========

- Method Detail

- getCurve

```java
public
EllipticCurve
getCurve()
```

Returns the elliptic curve that this parameter defines.

**Returns:** the elliptic curve that this parameter defines.

- getGenerator

```java
public
ECPoint
getGenerator()
```

Returns the generator which is also known as the base point.

**Returns:** the generator which is also known as the base point.

- getOrder

```java
public
BigInteger
getOrder()
```

Returns the order of the generator.

**Returns:** the order of the generator.

- getCofactor

```java
public int getCofactor()
```

Returns the cofactor.

**Returns:** the cofactor.

Constructor Detail

- ECParameterSpec

```java
public ECParameterSpec​(
EllipticCurve
curve,

ECPoint
g,

BigInteger
n,
int h)
```

Creates elliptic curve domain parameters based on the
specified values.

**Parameters:** curve

- the elliptic curve which this parameter
defines.
**Parameters:** g

- the generator which is also known as the base point.
**Parameters:** n

- the order of the generator

g

.
**Parameters:** h

- the cofactor.
**Throws:** NullPointerException

- if

curve

,

g

, or

n

is null.
**Throws:** IllegalArgumentException

- if

n

or

h

is not positive.

---

#### Constructor Detail

ECParameterSpec

```java
public ECParameterSpec​(
EllipticCurve
curve,

ECPoint
g,

BigInteger
n,
int h)
```

Creates elliptic curve domain parameters based on the
specified values.

**Parameters:** curve

- the elliptic curve which this parameter
defines.
**Parameters:** g

- the generator which is also known as the base point.
**Parameters:** n

- the order of the generator

g

.
**Parameters:** h

- the cofactor.
**Throws:** NullPointerException

- if

curve

,

g

, or

n

is null.
**Throws:** IllegalArgumentException

- if

n

or

h

is not positive.

---

#### ECParameterSpec

public ECParameterSpec​(

EllipticCurve

curve,

ECPoint

g,

BigInteger

n,
int h)

Creates elliptic curve domain parameters based on the
specified values.

Method Detail

- getCurve

```java
public
EllipticCurve
getCurve()
```

Returns the elliptic curve that this parameter defines.

**Returns:** the elliptic curve that this parameter defines.

- getGenerator

```java
public
ECPoint
getGenerator()
```

Returns the generator which is also known as the base point.

**Returns:** the generator which is also known as the base point.

- getOrder

```java
public
BigInteger
getOrder()
```

Returns the order of the generator.

**Returns:** the order of the generator.

- getCofactor

```java
public int getCofactor()
```

Returns the cofactor.

**Returns:** the cofactor.

---

#### Method Detail

getCurve

```java
public
EllipticCurve
getCurve()
```

Returns the elliptic curve that this parameter defines.

**Returns:** the elliptic curve that this parameter defines.

---

#### getCurve

public

EllipticCurve

getCurve()

Returns the elliptic curve that this parameter defines.

getGenerator

```java
public
ECPoint
getGenerator()
```

Returns the generator which is also known as the base point.

**Returns:** the generator which is also known as the base point.

---

#### getGenerator

public

ECPoint

getGenerator()

Returns the generator which is also known as the base point.

getOrder

```java
public
BigInteger
getOrder()
```

Returns the order of the generator.

**Returns:** the order of the generator.

---

#### getOrder

public

BigInteger

getOrder()

Returns the order of the generator.

getCofactor

```java
public int getCofactor()
```

Returns the cofactor.

**Returns:** the cofactor.

---

#### getCofactor

public int getCofactor()

Returns the cofactor.

---

