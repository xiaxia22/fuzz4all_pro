# Class XECPrivateKeySpec

**Source:** `java.base\java\security\spec\XECPrivateKeySpec.html`

### Class Description

```java
public class
XECPrivateKeySpec

extends
Object

implements
KeySpec
```

A class representing elliptic curve private keys as defined in RFC 7748,
including the curve and other algorithm parameters. The private key is
represented as an encoded scalar value. The decoding procedure defined in
the RFC includes an operation that forces certain bits of the key to either
1 or 0. This operation is known as "pruning" or "clamping" the private key.
All arrays in this spec are unpruned, and implementations will need to prune
the array before using it in any numerical operations.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public XECPrivateKeySpec​(
AlgorithmParameterSpec
params,
byte[] scalar)

Construct a private key spec using the supplied parameters and
encoded scalar value.

**Parameters:**
- params

- the algorithm parameters
- scalar

- the unpruned encoded scalar value. This array is copied
to protect against subsequent modification.

**Throws:**
- NullPointerException

- if

params

or

scalar

is null.

---

### Method Details

#### public
AlgorithmParameterSpec
getParams()

Get the algorithm parameters that define the curve and other settings.

**Returns:**
- the algorithm parameters

---

#### public byte[] getScalar()

Get the scalar value encoded as an unpruned byte array. A new copy of
the array is returned each time this method is called.

**Returns:**
- the unpruned encoded scalar value

---

### Additional Sections

#### Class XECPrivateKeySpec

java.lang.Object

- java.security.spec.XECPrivateKeySpec

java.security.spec.XECPrivateKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
XECPrivateKeySpec

extends
Object

implements
KeySpec
```

A class representing elliptic curve private keys as defined in RFC 7748,
including the curve and other algorithm parameters. The private key is
represented as an encoded scalar value. The decoding procedure defined in
the RFC includes an operation that forces certain bits of the key to either
1 or 0. This operation is known as "pruning" or "clamping" the private key.
All arrays in this spec are unpruned, and implementations will need to prune
the array before using it in any numerical operations.

**Since:** 11

public class

XECPrivateKeySpec

extends

Object

implements

KeySpec

A class representing elliptic curve private keys as defined in RFC 7748,
including the curve and other algorithm parameters. The private key is
represented as an encoded scalar value. The decoding procedure defined in
the RFC includes an operation that forces certain bits of the key to either
1 or 0. This operation is known as "pruning" or "clamping" the private key.
All arrays in this spec are unpruned, and implementations will need to prune
the array before using it in any numerical operations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XECPrivateKeySpec

​(

AlgorithmParameterSpec

params,
byte[] scalar)

Construct a private key spec using the supplied parameters and
encoded scalar value.

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

byte[]

getScalar

()

Get the scalar value encoded as an unpruned byte array.

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

XECPrivateKeySpec

​(

AlgorithmParameterSpec

params,
byte[] scalar)

Construct a private key spec using the supplied parameters and
encoded scalar value.

---

#### Constructor Summary

Construct a private key spec using the supplied parameters and
encoded scalar value.

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

byte[]

getScalar

()

Get the scalar value encoded as an unpruned byte array.

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

Get the scalar value encoded as an unpruned byte array.

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

- XECPrivateKeySpec

```java
public XECPrivateKeySpec​(
AlgorithmParameterSpec
params,
byte[] scalar)
```

Construct a private key spec using the supplied parameters and
encoded scalar value.

**Parameters:** params

- the algorithm parameters
**Parameters:** scalar

- the unpruned encoded scalar value. This array is copied
to protect against subsequent modification.
**Throws:** NullPointerException

- if

params

or

scalar

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

**Returns:** the algorithm parameters

- getScalar

```java
public byte[] getScalar()
```

Get the scalar value encoded as an unpruned byte array. A new copy of
the array is returned each time this method is called.

**Returns:** the unpruned encoded scalar value

Constructor Detail

- XECPrivateKeySpec

```java
public XECPrivateKeySpec​(
AlgorithmParameterSpec
params,
byte[] scalar)
```

Construct a private key spec using the supplied parameters and
encoded scalar value.

**Parameters:** params

- the algorithm parameters
**Parameters:** scalar

- the unpruned encoded scalar value. This array is copied
to protect against subsequent modification.
**Throws:** NullPointerException

- if

params

or

scalar

is null.

---

#### Constructor Detail

XECPrivateKeySpec

```java
public XECPrivateKeySpec​(
AlgorithmParameterSpec
params,
byte[] scalar)
```

Construct a private key spec using the supplied parameters and
encoded scalar value.

**Parameters:** params

- the algorithm parameters
**Parameters:** scalar

- the unpruned encoded scalar value. This array is copied
to protect against subsequent modification.
**Throws:** NullPointerException

- if

params

or

scalar

is null.

---

#### XECPrivateKeySpec

public XECPrivateKeySpec​(

AlgorithmParameterSpec

params,
byte[] scalar)

Construct a private key spec using the supplied parameters and
encoded scalar value.

Method Detail

- getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Get the algorithm parameters that define the curve and other settings.

**Returns:** the algorithm parameters

- getScalar

```java
public byte[] getScalar()
```

Get the scalar value encoded as an unpruned byte array. A new copy of
the array is returned each time this method is called.

**Returns:** the unpruned encoded scalar value

---

#### Method Detail

getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Get the algorithm parameters that define the curve and other settings.

**Returns:** the algorithm parameters

---

#### getParams

public

AlgorithmParameterSpec

getParams()

Get the algorithm parameters that define the curve and other settings.

getScalar

```java
public byte[] getScalar()
```

Get the scalar value encoded as an unpruned byte array. A new copy of
the array is returned each time this method is called.

**Returns:** the unpruned encoded scalar value

---

#### getScalar

public byte[] getScalar()

Get the scalar value encoded as an unpruned byte array. A new copy of
the array is returned each time this method is called.

---

