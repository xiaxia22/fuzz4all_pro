# Class RSAPrivateCrtKeySpec

**Source:** `java.base\java\security\spec\RSAPrivateCrtKeySpec.html`

### Class Description

```java
public class
RSAPrivateCrtKeySpec

extends
RSAPrivateKeySpec
```

This class specifies an RSA private key, as defined in the

PKCS#1 v2.2

standard,
using the Chinese Remainder Theorem (CRT) information values for efficiency.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient)

Creates a new

RSAPrivateCrtKeySpec

.

**Parameters:**
- modulus

- the modulus n
- publicExponent

- the public exponent e
- privateExponent

- the private exponent d
- primeP

- the prime factor p of n
- primeQ

- the prime factor q of n
- primeExponentP

- this is d mod (p-1)
- primeExponentQ

- this is d mod (q-1)
- crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p

---

#### public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient,

AlgorithmParameterSpec
keyParams)

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

**Parameters:**
- modulus

- the modulus n
- publicExponent

- the public exponent e
- privateExponent

- the private exponent d
- primeP

- the prime factor p of n
- primeQ

- the prime factor q of n
- primeExponentP

- this is d mod (p-1)
- primeExponentQ

- this is d mod (q-1)
- crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
- keyParams

- the parameters associated with key

**Since:**
- 11

---

### Method Details

#### public
BigInteger
getPublicExponent()

Returns the public exponent.

**Returns:**
- the public exponent

---

#### public
BigInteger
getPrimeP()

Returns the primeP.

**Returns:**
- the primeP

---

#### public
BigInteger
getPrimeQ()

Returns the primeQ.

**Returns:**
- the primeQ

---

#### public
BigInteger
getPrimeExponentP()

Returns the primeExponentP.

**Returns:**
- the primeExponentP

---

#### public
BigInteger
getPrimeExponentQ()

Returns the primeExponentQ.

**Returns:**
- the primeExponentQ

---

#### public
BigInteger
getCrtCoefficient()

Returns the crtCoefficient.

**Returns:**
- the crtCoefficient

---

### Additional Sections

#### Class RSAPrivateCrtKeySpec

java.lang.Object

- java.security.spec.RSAPrivateKeySpec
- - java.security.spec.RSAPrivateCrtKeySpec

java.security.spec.RSAPrivateKeySpec

- java.security.spec.RSAPrivateCrtKeySpec

java.security.spec.RSAPrivateCrtKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
RSAPrivateCrtKeySpec

extends
RSAPrivateKeySpec
```

This class specifies an RSA private key, as defined in the

PKCS#1 v2.2

standard,
using the Chinese Remainder Theorem (CRT) information values for efficiency.

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

KeySpec

,

PKCS8EncodedKeySpec

,

RSAPrivateKeySpec

,

RSAPublicKeySpec

public class

RSAPrivateCrtKeySpec

extends

RSAPrivateKeySpec

This class specifies an RSA private key, as defined in the

PKCS#1 v2.2

standard,
using the Chinese Remainder Theorem (CRT) information values for efficiency.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RSAPrivateCrtKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent,

BigInteger

privateExponent,

BigInteger

primeP,

BigInteger

primeQ,

BigInteger

primeExponentP,

BigInteger

primeExponentQ,

BigInteger

crtCoefficient)

Creates a new

RSAPrivateCrtKeySpec

.

RSAPrivateCrtKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent,

BigInteger

privateExponent,

BigInteger

primeP,

BigInteger

primeQ,

BigInteger

primeExponentP,

BigInteger

primeExponentQ,

BigInteger

crtCoefficient,

AlgorithmParameterSpec

keyParams)

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getCrtCoefficient

()

Returns the crtCoefficient.

BigInteger

getPrimeExponentP

()

Returns the primeExponentP.

BigInteger

getPrimeExponentQ

()

Returns the primeExponentQ.

BigInteger

getPrimeP

()

Returns the primeP.

BigInteger

getPrimeQ

()

Returns the primeQ.

BigInteger

getPublicExponent

()

Returns the public exponent.

- Methods declared in class java.security.spec.

RSAPrivateKeySpec

getModulus

,

getParams

,

getPrivateExponent

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

RSAPrivateCrtKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent,

BigInteger

privateExponent,

BigInteger

primeP,

BigInteger

primeQ,

BigInteger

primeExponentP,

BigInteger

primeExponentQ,

BigInteger

crtCoefficient)

Creates a new

RSAPrivateCrtKeySpec

.

RSAPrivateCrtKeySpec

​(

BigInteger

modulus,

BigInteger

publicExponent,

BigInteger

privateExponent,

BigInteger

primeP,

BigInteger

primeQ,

BigInteger

primeExponentP,

BigInteger

primeExponentQ,

BigInteger

crtCoefficient,

AlgorithmParameterSpec

keyParams)

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

---

#### Constructor Summary

Creates a new

RSAPrivateCrtKeySpec

.

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getCrtCoefficient

()

Returns the crtCoefficient.

BigInteger

getPrimeExponentP

()

Returns the primeExponentP.

BigInteger

getPrimeExponentQ

()

Returns the primeExponentQ.

BigInteger

getPrimeP

()

Returns the primeP.

BigInteger

getPrimeQ

()

Returns the primeQ.

BigInteger

getPublicExponent

()

Returns the public exponent.

- Methods declared in class java.security.spec.

RSAPrivateKeySpec

getModulus

,

getParams

,

getPrivateExponent

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

Returns the crtCoefficient.

Returns the primeExponentP.

Returns the primeExponentQ.

Returns the primeP.

Returns the primeQ.

Returns the public exponent.

Methods declared in class java.security.spec.

RSAPrivateKeySpec

getModulus

,

getParams

,

getPrivateExponent

---

#### Methods declared in class java.security.spec. RSAPrivateKeySpec

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

- RSAPrivateCrtKeySpec

```java
public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient)
```

Creates a new

RSAPrivateCrtKeySpec

.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of n
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p

- RSAPrivateCrtKeySpec

```java
public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient,

AlgorithmParameterSpec
keyParams)
```

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of n
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
**Parameters:** keyParams

- the parameters associated with key
**Since:** 11

============ METHOD DETAIL ==========

- Method Detail

- getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

- getPrimeP

```java
public
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP

- getPrimeQ

```java
public
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ

- getPrimeExponentP

```java
public
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP

- getPrimeExponentQ

```java
public
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ

- getCrtCoefficient

```java
public
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient

Constructor Detail

- RSAPrivateCrtKeySpec

```java
public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient)
```

Creates a new

RSAPrivateCrtKeySpec

.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of n
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p

- RSAPrivateCrtKeySpec

```java
public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient,

AlgorithmParameterSpec
keyParams)
```

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of n
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
**Parameters:** keyParams

- the parameters associated with key
**Since:** 11

---

#### Constructor Detail

RSAPrivateCrtKeySpec

```java
public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient)
```

Creates a new

RSAPrivateCrtKeySpec

.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of n
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p

---

#### RSAPrivateCrtKeySpec

public RSAPrivateCrtKeySpec​(

BigInteger

modulus,

BigInteger

publicExponent,

BigInteger

privateExponent,

BigInteger

primeP,

BigInteger

primeQ,

BigInteger

primeExponentP,

BigInteger

primeExponentQ,

BigInteger

crtCoefficient)

Creates a new

RSAPrivateCrtKeySpec

.

RSAPrivateCrtKeySpec

```java
public RSAPrivateCrtKeySpec​(
BigInteger
modulus,

BigInteger
publicExponent,

BigInteger
privateExponent,

BigInteger
primeP,

BigInteger
primeQ,

BigInteger
primeExponentP,

BigInteger
primeExponentQ,

BigInteger
crtCoefficient,

AlgorithmParameterSpec
keyParams)
```

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of n
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
**Parameters:** keyParams

- the parameters associated with key
**Since:** 11

---

#### RSAPrivateCrtKeySpec

public RSAPrivateCrtKeySpec​(

BigInteger

modulus,

BigInteger

publicExponent,

BigInteger

privateExponent,

BigInteger

primeP,

BigInteger

primeQ,

BigInteger

primeExponentP,

BigInteger

primeExponentQ,

BigInteger

crtCoefficient,

AlgorithmParameterSpec

keyParams)

Creates a new

RSAPrivateCrtKeySpec

with additional
key parameters.

Method Detail

- getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

- getPrimeP

```java
public
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP

- getPrimeQ

```java
public
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ

- getPrimeExponentP

```java
public
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP

- getPrimeExponentQ

```java
public
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ

- getCrtCoefficient

```java
public
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient

---

#### Method Detail

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

getPrimeP

```java
public
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP

---

#### getPrimeP

public

BigInteger

getPrimeP()

Returns the primeP.

getPrimeQ

```java
public
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ

---

#### getPrimeQ

public

BigInteger

getPrimeQ()

Returns the primeQ.

getPrimeExponentP

```java
public
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP

---

#### getPrimeExponentP

public

BigInteger

getPrimeExponentP()

Returns the primeExponentP.

getPrimeExponentQ

```java
public
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ

---

#### getPrimeExponentQ

public

BigInteger

getPrimeExponentQ()

Returns the primeExponentQ.

getCrtCoefficient

```java
public
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient

---

#### getCrtCoefficient

public

BigInteger

getCrtCoefficient()

Returns the crtCoefficient.

---

