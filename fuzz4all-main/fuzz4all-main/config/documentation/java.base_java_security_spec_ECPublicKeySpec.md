# Class ECPublicKeySpec

**Source:** `java.base\java\security\spec\ECPublicKeySpec.html`

### Class Description

```java
public class
ECPublicKeySpec

extends
Object

implements
KeySpec
```

This immutable class specifies an elliptic curve public key with
its associated parameters.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public ECPublicKeySpec​(
ECPoint
w,

ECParameterSpec
params)

Creates a new ECPublicKeySpec with the specified
parameter values.

**Parameters:**
- w

- the public point.
- params

- the associated elliptic curve domain
parameters.

**Throws:**
- NullPointerException

- if

w

or

params

is null.
- IllegalArgumentException

- if

w

is point at infinity, i.e. ECPoint.POINT_INFINITY

---

### Method Details

#### public
ECPoint
getW()

Returns the public point W.

**Returns:**
- the public point W.

---

#### public
ECParameterSpec
getParams()

Returns the associated elliptic curve domain
parameters.

**Returns:**
- the EC domain parameters.

---

### Additional Sections

#### Class ECPublicKeySpec

java.lang.Object

- java.security.spec.ECPublicKeySpec

java.security.spec.ECPublicKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
ECPublicKeySpec

extends
Object

implements
KeySpec
```

This immutable class specifies an elliptic curve public key with
its associated parameters.

**Since:** 1.5
**See Also:** KeySpec

,

ECPoint

,

ECParameterSpec

public class

ECPublicKeySpec

extends

Object

implements

KeySpec

This immutable class specifies an elliptic curve public key with
its associated parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ECPublicKeySpec

​(

ECPoint

w,

ECParameterSpec

params)

Creates a new ECPublicKeySpec with the specified
parameter values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ECParameterSpec

getParams

()

Returns the associated elliptic curve domain
parameters.

ECPoint

getW

()

Returns the public point W.

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

ECPublicKeySpec

​(

ECPoint

w,

ECParameterSpec

params)

Creates a new ECPublicKeySpec with the specified
parameter values.

---

#### Constructor Summary

Creates a new ECPublicKeySpec with the specified
parameter values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ECParameterSpec

getParams

()

Returns the associated elliptic curve domain
parameters.

ECPoint

getW

()

Returns the public point W.

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

Returns the associated elliptic curve domain
parameters.

Returns the public point W.

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

- ECPublicKeySpec

```java
public ECPublicKeySpec​(
ECPoint
w,

ECParameterSpec
params)
```

Creates a new ECPublicKeySpec with the specified
parameter values.

**Parameters:** w

- the public point.
**Parameters:** params

- the associated elliptic curve domain
parameters.
**Throws:** NullPointerException

- if

w

or

params

is null.
**Throws:** IllegalArgumentException

- if

w

is point at infinity, i.e. ECPoint.POINT_INFINITY

============ METHOD DETAIL ==========

- Method Detail

- getW

```java
public
ECPoint
getW()
```

Returns the public point W.

**Returns:** the public point W.

- getParams

```java
public
ECParameterSpec
getParams()
```

Returns the associated elliptic curve domain
parameters.

**Returns:** the EC domain parameters.

Constructor Detail

- ECPublicKeySpec

```java
public ECPublicKeySpec​(
ECPoint
w,

ECParameterSpec
params)
```

Creates a new ECPublicKeySpec with the specified
parameter values.

**Parameters:** w

- the public point.
**Parameters:** params

- the associated elliptic curve domain
parameters.
**Throws:** NullPointerException

- if

w

or

params

is null.
**Throws:** IllegalArgumentException

- if

w

is point at infinity, i.e. ECPoint.POINT_INFINITY

---

#### Constructor Detail

ECPublicKeySpec

```java
public ECPublicKeySpec​(
ECPoint
w,

ECParameterSpec
params)
```

Creates a new ECPublicKeySpec with the specified
parameter values.

**Parameters:** w

- the public point.
**Parameters:** params

- the associated elliptic curve domain
parameters.
**Throws:** NullPointerException

- if

w

or

params

is null.
**Throws:** IllegalArgumentException

- if

w

is point at infinity, i.e. ECPoint.POINT_INFINITY

---

#### ECPublicKeySpec

public ECPublicKeySpec​(

ECPoint

w,

ECParameterSpec

params)

Creates a new ECPublicKeySpec with the specified
parameter values.

Method Detail

- getW

```java
public
ECPoint
getW()
```

Returns the public point W.

**Returns:** the public point W.

- getParams

```java
public
ECParameterSpec
getParams()
```

Returns the associated elliptic curve domain
parameters.

**Returns:** the EC domain parameters.

---

#### Method Detail

getW

```java
public
ECPoint
getW()
```

Returns the public point W.

**Returns:** the public point W.

---

#### getW

public

ECPoint

getW()

Returns the public point W.

getParams

```java
public
ECParameterSpec
getParams()
```

Returns the associated elliptic curve domain
parameters.

**Returns:** the EC domain parameters.

---

#### getParams

public

ECParameterSpec

getParams()

Returns the associated elliptic curve domain
parameters.

---

