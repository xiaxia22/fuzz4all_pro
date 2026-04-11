# Class XECPublicKeySpec

**Source:** `java.base\java\security\spec\XECPublicKeySpec.html`

### Class Description

```java
public class
XECPublicKeySpec

extends
Object

implements
KeySpec
```

A class representing elliptic curve public keys as defined in RFC 7748,
including the curve and other algorithm parameters. The public key is a
particular point on the curve, which is represented using only its
u-coordinate. A u-coordinate is an element of the field of integers modulo
some value that is determined by the algorithm parameters. This field
element is represented by a BigInteger which may hold any value. That is,
the BigInteger is not restricted to the range of canonical field elements.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public XECPublicKeySpec​(
AlgorithmParameterSpec
params,

BigInteger
u)

Construct a public key spec using the supplied parameters and
u coordinate.

**Parameters:**
- params

- the algorithm parameters
- u

- the u-coordinate of the point, represented using a BigInteger
which may hold any value

**Throws:**
- NullPointerException

- if

params

or

u

is null.

---

### Method Details

#### public
AlgorithmParameterSpec
getParams()

Get the algorithm parameters that define the curve and other settings.

**Returns:**
- the parameters

---

#### public
BigInteger
getU()

Get the u coordinate of the point.

**Returns:**
- the u-coordinate, represented using a BigInteger which may hold
any value

---

### Additional Sections

#### Class XECPublicKeySpec

java.lang.Object

- java.security.spec.XECPublicKeySpec

java.security.spec.XECPublicKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
XECPublicKeySpec

extends
Object

implements
KeySpec
```

A class representing elliptic curve public keys as defined in RFC 7748,
including the curve and other algorithm parameters. The public key is a
particular point on the curve, which is represented using only its
u-coordinate. A u-coordinate is an element of the field of integers modulo
some value that is determined by the algorithm parameters. This field
element is represented by a BigInteger which may hold any value. That is,
the BigInteger is not restricted to the range of canonical field elements.

**Since:** 11

public class

XECPublicKeySpec

extends

Object

implements

KeySpec

A class representing elliptic curve public keys as defined in RFC 7748,
including the curve and other algorithm parameters. The public key is a
particular point on the curve, which is represented using only its
u-coordinate. A u-coordinate is an element of the field of integers modulo
some value that is determined by the algorithm parameters. This field
element is represented by a BigInteger which may hold any value. That is,
the BigInteger is not restricted to the range of canonical field elements.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XECPublicKeySpec

​(

AlgorithmParameterSpec

params,

BigInteger

u)

Construct a public key spec using the supplied parameters and
u coordinate.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getParams

()

Get the algorithm parameters that define the curve and other settings.

BigInteger

getU

()

Get the u coordinate of the point.

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

XECPublicKeySpec

​(

AlgorithmParameterSpec

params,

BigInteger

u)

Construct a public key spec using the supplied parameters and
u coordinate.

---

#### Constructor Summary

Construct a public key spec using the supplied parameters and
u coordinate.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getParams

()

Get the algorithm parameters that define the curve and other settings.

BigInteger

getU

()

Get the u coordinate of the point.

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

Get the algorithm parameters that define the curve and other settings.

Get the u coordinate of the point.

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

- XECPublicKeySpec

```java
public XECPublicKeySpec​(
AlgorithmParameterSpec
params,

BigInteger
u)
```

Construct a public key spec using the supplied parameters and
u coordinate.

**Parameters:** params

- the algorithm parameters
**Parameters:** u

- the u-coordinate of the point, represented using a BigInteger
which may hold any value
**Throws:** NullPointerException

- if

params

or

u

is null.

============ METHOD DETAIL ==========

- Method Detail

- getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Get the algorithm parameters that define the curve and other settings.

**Returns:** the parameters

- getU

```java
public
BigInteger
getU()
```

Get the u coordinate of the point.

**Returns:** the u-coordinate, represented using a BigInteger which may hold
any value

Constructor Detail

- XECPublicKeySpec

```java
public XECPublicKeySpec​(
AlgorithmParameterSpec
params,

BigInteger
u)
```

Construct a public key spec using the supplied parameters and
u coordinate.

**Parameters:** params

- the algorithm parameters
**Parameters:** u

- the u-coordinate of the point, represented using a BigInteger
which may hold any value
**Throws:** NullPointerException

- if

params

or

u

is null.

---

#### Constructor Detail

XECPublicKeySpec

```java
public XECPublicKeySpec​(
AlgorithmParameterSpec
params,

BigInteger
u)
```

Construct a public key spec using the supplied parameters and
u coordinate.

**Parameters:** params

- the algorithm parameters
**Parameters:** u

- the u-coordinate of the point, represented using a BigInteger
which may hold any value
**Throws:** NullPointerException

- if

params

or

u

is null.

---

#### XECPublicKeySpec

public XECPublicKeySpec​(

AlgorithmParameterSpec

params,

BigInteger

u)

Construct a public key spec using the supplied parameters and
u coordinate.

Method Detail

- getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Get the algorithm parameters that define the curve and other settings.

**Returns:** the parameters

- getU

```java
public
BigInteger
getU()
```

Get the u coordinate of the point.

**Returns:** the u-coordinate, represented using a BigInteger which may hold
any value

---

#### Method Detail

getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Get the algorithm parameters that define the curve and other settings.

**Returns:** the parameters

---

#### getParams

public

AlgorithmParameterSpec

getParams()

Get the algorithm parameters that define the curve and other settings.

getU

```java
public
BigInteger
getU()
```

Get the u coordinate of the point.

**Returns:** the u-coordinate, represented using a BigInteger which may hold
any value

---

#### getU

public

BigInteger

getU()

Get the u coordinate of the point.

---

