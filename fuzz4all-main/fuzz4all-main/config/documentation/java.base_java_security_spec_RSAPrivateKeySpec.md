# Class RSAPrivateKeySpec

**Source:** `java.base\java\security\spec\RSAPrivateKeySpec.html`

### Class Description

```java
public class
RSAPrivateKeySpec

extends
Object

implements
KeySpec
```

This class specifies an RSA private key.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent)

Creates a new RSAPrivateKeySpec.

**Parameters:**
- modulus

- the modulus
- privateExponent

- the private exponent

---

#### public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent,

AlgorithmParameterSpec
params)

Creates a new RSAPrivateKeySpec with additional key parameters.

**Parameters:**
- modulus

- the modulus
- privateExponent

- the private exponent
- params

- the parameters associated with this key, may be null

**Since:**
- 11

---

### Method Details

#### public
BigInteger
getModulus()

Returns the modulus.

**Returns:**
- the modulus

---

#### public
BigInteger
getPrivateExponent()

Returns the private exponent.

**Returns:**
- the private exponent

---

#### public
AlgorithmParameterSpec
getParams()

Returns the parameters associated with this key, may be null if not
present.

**Returns:**
- the parameters associated with this key

**Since:**
- 11

---

### Additional Sections

#### Class RSAPrivateKeySpec

java.lang.Object

- java.security.spec.RSAPrivateKeySpec

java.security.spec.RSAPrivateKeySpec

**All Implemented Interfaces:** KeySpec

**Direct Known Subclasses:** RSAMultiPrimePrivateCrtKeySpec

,

RSAPrivateCrtKeySpec

```java
public class
RSAPrivateKeySpec

extends
Object

implements
KeySpec
```

This class specifies an RSA private key.

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

KeySpec

,

PKCS8EncodedKeySpec

,

RSAPublicKeySpec

,

RSAPrivateCrtKeySpec

public class

RSAPrivateKeySpec

extends

Object

implements

KeySpec

This class specifies an RSA private key.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RSAPrivateKeySpec

​(

BigInteger

modulus,

BigInteger

privateExponent)

Creates a new RSAPrivateKeySpec.

RSAPrivateKeySpec

​(

BigInteger

modulus,

BigInteger

privateExponent,

AlgorithmParameterSpec

params)

Creates a new RSAPrivateKeySpec with additional key parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getModulus

()

Returns the modulus.

AlgorithmParameterSpec

getParams

()

Returns the parameters associated with this key, may be null if not
present.

BigInteger

getPrivateExponent

()

Returns the private exponent.

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

RSAPrivateKeySpec

​(

BigInteger

modulus,

BigInteger

privateExponent)

Creates a new RSAPrivateKeySpec.

RSAPrivateKeySpec

​(

BigInteger

modulus,

BigInteger

privateExponent,

AlgorithmParameterSpec

params)

Creates a new RSAPrivateKeySpec with additional key parameters.

---

#### Constructor Summary

Creates a new RSAPrivateKeySpec.

Creates a new RSAPrivateKeySpec with additional key parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getModulus

()

Returns the modulus.

AlgorithmParameterSpec

getParams

()

Returns the parameters associated with this key, may be null if not
present.

BigInteger

getPrivateExponent

()

Returns the private exponent.

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

Returns the modulus.

Returns the parameters associated with this key, may be null if not
present.

Returns the private exponent.

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

- RSAPrivateKeySpec

```java
public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent)
```

Creates a new RSAPrivateKeySpec.

**Parameters:** modulus

- the modulus
**Parameters:** privateExponent

- the private exponent

- RSAPrivateKeySpec

```java
public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent,

AlgorithmParameterSpec
params)
```

Creates a new RSAPrivateKeySpec with additional key parameters.

**Parameters:** modulus

- the modulus
**Parameters:** privateExponent

- the private exponent
**Parameters:** params

- the parameters associated with this key, may be null
**Since:** 11

============ METHOD DETAIL ==========

- Method Detail

- getModulus

```java
public
BigInteger
getModulus()
```

Returns the modulus.

**Returns:** the modulus

- getPrivateExponent

```java
public
BigInteger
getPrivateExponent()
```

Returns the private exponent.

**Returns:** the private exponent

- getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Returns the parameters associated with this key, may be null if not
present.

**Returns:** the parameters associated with this key
**Since:** 11

Constructor Detail

- RSAPrivateKeySpec

```java
public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent)
```

Creates a new RSAPrivateKeySpec.

**Parameters:** modulus

- the modulus
**Parameters:** privateExponent

- the private exponent

- RSAPrivateKeySpec

```java
public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent,

AlgorithmParameterSpec
params)
```

Creates a new RSAPrivateKeySpec with additional key parameters.

**Parameters:** modulus

- the modulus
**Parameters:** privateExponent

- the private exponent
**Parameters:** params

- the parameters associated with this key, may be null
**Since:** 11

---

#### Constructor Detail

RSAPrivateKeySpec

```java
public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent)
```

Creates a new RSAPrivateKeySpec.

**Parameters:** modulus

- the modulus
**Parameters:** privateExponent

- the private exponent

---

#### RSAPrivateKeySpec

public RSAPrivateKeySpec​(

BigInteger

modulus,

BigInteger

privateExponent)

Creates a new RSAPrivateKeySpec.

RSAPrivateKeySpec

```java
public RSAPrivateKeySpec​(
BigInteger
modulus,

BigInteger
privateExponent,

AlgorithmParameterSpec
params)
```

Creates a new RSAPrivateKeySpec with additional key parameters.

**Parameters:** modulus

- the modulus
**Parameters:** privateExponent

- the private exponent
**Parameters:** params

- the parameters associated with this key, may be null
**Since:** 11

---

#### RSAPrivateKeySpec

public RSAPrivateKeySpec​(

BigInteger

modulus,

BigInteger

privateExponent,

AlgorithmParameterSpec

params)

Creates a new RSAPrivateKeySpec with additional key parameters.

Method Detail

- getModulus

```java
public
BigInteger
getModulus()
```

Returns the modulus.

**Returns:** the modulus

- getPrivateExponent

```java
public
BigInteger
getPrivateExponent()
```

Returns the private exponent.

**Returns:** the private exponent

- getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Returns the parameters associated with this key, may be null if not
present.

**Returns:** the parameters associated with this key
**Since:** 11

---

#### Method Detail

getModulus

```java
public
BigInteger
getModulus()
```

Returns the modulus.

**Returns:** the modulus

---

#### getModulus

public

BigInteger

getModulus()

Returns the modulus.

getPrivateExponent

```java
public
BigInteger
getPrivateExponent()
```

Returns the private exponent.

**Returns:** the private exponent

---

#### getPrivateExponent

public

BigInteger

getPrivateExponent()

Returns the private exponent.

getParams

```java
public
AlgorithmParameterSpec
getParams()
```

Returns the parameters associated with this key, may be null if not
present.

**Returns:** the parameters associated with this key
**Since:** 11

---

#### getParams

public

AlgorithmParameterSpec

getParams()

Returns the parameters associated with this key, may be null if not
present.

---

