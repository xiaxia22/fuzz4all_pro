# Class RSAPublicKeySpec

**Source:** `java.base\java\security\spec\RSAPublicKeySpec.html`

### Class Description

```java
public class
RSAPublicKeySpec

extends
Object

implements
KeySpec
```

This class specifies an RSA public key.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent)

Creates a new RSAPublicKeySpec.

**Parameters:**
- modulus

- the modulus
- publicExponent

- the public exponent

---

#### public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

AlgorithmParameterSpec
params)

Creates a new RSAPublicKeySpec with additional key parameters.

**Parameters:**
- modulus

- the modulus
- publicExponent

- the public exponent
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
getPublicExponent()

Returns the public exponent.

**Returns:**
- the public exponent

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

#### Class RSAPublicKeySpec

java.lang.Object

- java.security.spec.RSAPublicKeySpec

java.security.spec.RSAPublicKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
RSAPublicKeySpec

extends
Object

implements
KeySpec
```

This class specifies an RSA public key.

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

KeySpec

,

X509EncodedKeySpec

,

RSAPrivateKeySpec

,

RSAPrivateCrtKeySpec

public class

RSAPublicKeySpec

extends

Object

implements

KeySpec

This class specifies an RSA public key.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RSAPublicKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent)

Creates a new RSAPublicKeySpec.

RSAPublicKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent,

AlgorithmParameterSpec

params)

Creates a new RSAPublicKeySpec with additional key parameters.

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

getPublicExponent

()

Returns the public exponent.

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

RSAPublicKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent)

Creates a new RSAPublicKeySpec.

RSAPublicKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent,

AlgorithmParameterSpec

params)

Creates a new RSAPublicKeySpec with additional key parameters.

---

#### Constructor Summary

Creates a new RSAPublicKeySpec.

Creates a new RSAPublicKeySpec with additional key parameters.

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

getPublicExponent

()

Returns the public exponent.

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

Returns the public exponent.

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

- RSAPublicKeySpec

```java
public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent)
```

Creates a new RSAPublicKeySpec.

**Parameters:** modulus

- the modulus
**Parameters:** publicExponent

- the public exponent

- RSAPublicKeySpec

```java
public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

AlgorithmParameterSpec
params)
```

Creates a new RSAPublicKeySpec with additional key parameters.

**Parameters:** modulus

- the modulus
**Parameters:** publicExponent

- the public exponent
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

- getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

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

- RSAPublicKeySpec

```java
public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent)
```

Creates a new RSAPublicKeySpec.

**Parameters:** modulus

- the modulus
**Parameters:** publicExponent

- the public exponent

- RSAPublicKeySpec

```java
public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

AlgorithmParameterSpec
params)
```

Creates a new RSAPublicKeySpec with additional key parameters.

**Parameters:** modulus

- the modulus
**Parameters:** publicExponent

- the public exponent
**Parameters:** params

- the parameters associated with this key, may be null
**Since:** 11

---

#### Constructor Detail

RSAPublicKeySpec

```java
public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent)
```

Creates a new RSAPublicKeySpec.

**Parameters:** modulus

- the modulus
**Parameters:** publicExponent

- the public exponent

---

#### RSAPublicKeySpec

public RSAPublicKeySpec​(

BigInteger

modulus,

BigInteger

publicExponent)

Creates a new RSAPublicKeySpec.

RSAPublicKeySpec

```java
public RSAPublicKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

AlgorithmParameterSpec
params)
```

Creates a new RSAPublicKeySpec with additional key parameters.

**Parameters:** modulus

- the modulus
**Parameters:** publicExponent

- the public exponent
**Parameters:** params

- the parameters associated with this key, may be null
**Since:** 11

---

#### RSAPublicKeySpec

public RSAPublicKeySpec​(

BigInteger

modulus,

BigInteger

publicExponent,

AlgorithmParameterSpec

params)

Creates a new RSAPublicKeySpec with additional key parameters.

Method Detail

- getModulus

```java
public
BigInteger
getModulus()
```

Returns the modulus.

**Returns:** the modulus

- getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

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

getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

---

#### getPublicExponent

public

BigInteger

getPublicExponent()

Returns the public exponent.

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

