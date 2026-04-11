# Class ECPrivateKeySpec

**Source:** `java.base\java\security\spec\ECPrivateKeySpec.html`

### Class Description

```java
public class
ECPrivateKeySpec

extends
Object

implements
KeySpec
```

This immutable class specifies an elliptic curve private key with
its associated parameters.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public ECPrivateKeySpec​(
BigInteger
s,

ECParameterSpec
params)

Creates a new ECPrivateKeySpec with the specified
parameter values.

**Parameters:**
- s

- the private value.
- params

- the associated elliptic curve domain
parameters.

**Throws:**
- NullPointerException

- if

s

or

params

is null.

---

### Method Details

#### public
BigInteger
getS()

Returns the private value S.

**Returns:**
- the private value S.

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

#### Class ECPrivateKeySpec

java.lang.Object

- java.security.spec.ECPrivateKeySpec

java.security.spec.ECPrivateKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
ECPrivateKeySpec

extends
Object

implements
KeySpec
```

This immutable class specifies an elliptic curve private key with
its associated parameters.

**Since:** 1.5
**See Also:** KeySpec

,

ECParameterSpec

public class

ECPrivateKeySpec

extends

Object

implements

KeySpec

This immutable class specifies an elliptic curve private key with
its associated parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ECPrivateKeySpec

​(

BigInteger

s,

ECParameterSpec

params)

Creates a new ECPrivateKeySpec with the specified
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

BigInteger

getS

()

Returns the private value S.

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

ECPrivateKeySpec

​(

BigInteger

s,

ECParameterSpec

params)

Creates a new ECPrivateKeySpec with the specified
parameter values.

---

#### Constructor Summary

Creates a new ECPrivateKeySpec with the specified
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

BigInteger

getS

()

Returns the private value S.

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

Returns the private value S.

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

- ECPrivateKeySpec

```java
public ECPrivateKeySpec​(
BigInteger
s,

ECParameterSpec
params)
```

Creates a new ECPrivateKeySpec with the specified
parameter values.

**Parameters:** s

- the private value.
**Parameters:** params

- the associated elliptic curve domain
parameters.
**Throws:** NullPointerException

- if

s

or

params

is null.

============ METHOD DETAIL ==========

- Method Detail

- getS

```java
public
BigInteger
getS()
```

Returns the private value S.

**Returns:** the private value S.

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

- ECPrivateKeySpec

```java
public ECPrivateKeySpec​(
BigInteger
s,

ECParameterSpec
params)
```

Creates a new ECPrivateKeySpec with the specified
parameter values.

**Parameters:** s

- the private value.
**Parameters:** params

- the associated elliptic curve domain
parameters.
**Throws:** NullPointerException

- if

s

or

params

is null.

---

#### Constructor Detail

ECPrivateKeySpec

```java
public ECPrivateKeySpec​(
BigInteger
s,

ECParameterSpec
params)
```

Creates a new ECPrivateKeySpec with the specified
parameter values.

**Parameters:** s

- the private value.
**Parameters:** params

- the associated elliptic curve domain
parameters.
**Throws:** NullPointerException

- if

s

or

params

is null.

---

#### ECPrivateKeySpec

public ECPrivateKeySpec​(

BigInteger

s,

ECParameterSpec

params)

Creates a new ECPrivateKeySpec with the specified
parameter values.

Method Detail

- getS

```java
public
BigInteger
getS()
```

Returns the private value S.

**Returns:** the private value S.

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

getS

```java
public
BigInteger
getS()
```

Returns the private value S.

**Returns:** the private value S.

---

#### getS

public

BigInteger

getS()

Returns the private value S.

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

