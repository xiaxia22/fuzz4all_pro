# Class RSAMultiPrimePrivateCrtKeySpec

**Source:** `java.base\java\security\spec\RSAMultiPrimePrivateCrtKeySpec.html`

### Class Description

```java
public class
RSAMultiPrimePrivateCrtKeySpec

extends
RSAPrivateKeySpec
```

This class specifies an RSA multi-prime private key, as defined in the

PKCS#1 v2.2

standard
using the Chinese Remainder Theorem (CRT) information values
for efficiency.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

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

- the prime factor q of q
- primeExponentP

- this is d mod (p-1)
- primeExponentQ

- this is d mod (q-1)
- crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
- otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)

**Throws:**
- NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

is null
- IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified

---

#### public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo,

AlgorithmParameterSpec
keyParams)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

with additional
key parameters.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

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

- the Chinese Remainder Theorem coefficient
q-1 mod p
- otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)
- keyParams

- the parameters associated with key

**Throws:**
- NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

and

keyParams

is null
- IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified

**Since:**
- 11

---

### Method Details

#### public
BigInteger
getPublicExponent()

Returns the public exponent.

**Returns:**
- the public exponent.

---

#### public
BigInteger
getPrimeP()

Returns the primeP.

**Returns:**
- the primeP.

---

#### public
BigInteger
getPrimeQ()

Returns the primeQ.

**Returns:**
- the primeQ.

---

#### public
BigInteger
getPrimeExponentP()

Returns the primeExponentP.

**Returns:**
- the primeExponentP.

---

#### public
BigInteger
getPrimeExponentQ()

Returns the primeExponentQ.

**Returns:**
- the primeExponentQ.

---

#### public
BigInteger
getCrtCoefficient()

Returns the crtCoefficient.

**Returns:**
- the crtCoefficient.

---

#### public
RSAOtherPrimeInfo
[] getOtherPrimeInfo()

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

**Returns:**
- the otherPrimeInfo. Returns a new array each time this method
is called.

---

### Additional Sections

#### Class RSAMultiPrimePrivateCrtKeySpec

java.lang.Object

- java.security.spec.RSAPrivateKeySpec
- - java.security.spec.RSAMultiPrimePrivateCrtKeySpec

java.security.spec.RSAPrivateKeySpec

- java.security.spec.RSAMultiPrimePrivateCrtKeySpec

java.security.spec.RSAMultiPrimePrivateCrtKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
RSAMultiPrimePrivateCrtKeySpec

extends
RSAPrivateKeySpec
```

This class specifies an RSA multi-prime private key, as defined in the

PKCS#1 v2.2

standard
using the Chinese Remainder Theorem (CRT) information values
for efficiency.

**Since:** 1.4
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

,

RSAOtherPrimeInfo

public class

RSAMultiPrimePrivateCrtKeySpec

extends

RSAPrivateKeySpec

This class specifies an RSA multi-prime private key, as defined in the

PKCS#1 v2.2

standard
using the Chinese Remainder Theorem (CRT) information values
for efficiency.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RSAMultiPrimePrivateCrtKeySpec

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

RSAOtherPrimeInfo

[] otherPrimeInfo)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

RSAMultiPrimePrivateCrtKeySpec

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

RSAOtherPrimeInfo

[] otherPrimeInfo,

AlgorithmParameterSpec

keyParams)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

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

RSAOtherPrimeInfo

[]

getOtherPrimeInfo

()

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

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

RSAMultiPrimePrivateCrtKeySpec

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

RSAOtherPrimeInfo

[] otherPrimeInfo)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

RSAMultiPrimePrivateCrtKeySpec

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

RSAOtherPrimeInfo

[] otherPrimeInfo,

AlgorithmParameterSpec

keyParams)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

with additional
key parameters.

---

#### Constructor Summary

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

Creates a new

RSAMultiPrimePrivateCrtKeySpec

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

RSAOtherPrimeInfo

[]

getOtherPrimeInfo

()

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

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

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

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

- RSAMultiPrimePrivateCrtKeySpec

```java
public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo)
```

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of q
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
**Parameters:** otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)
**Throws:** NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

is null
**Throws:** IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified

- RSAMultiPrimePrivateCrtKeySpec

```java
public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo,

AlgorithmParameterSpec
keyParams)
```

Creates a new

RSAMultiPrimePrivateCrtKeySpec

with additional
key parameters.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

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

- the Chinese Remainder Theorem coefficient
q-1 mod p
**Parameters:** otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)
**Parameters:** keyParams

- the parameters associated with key
**Throws:** NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

and

keyParams

is null
**Throws:** IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified
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

**Returns:** the public exponent.

- getPrimeP

```java
public
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP.

- getPrimeQ

```java
public
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ.

- getPrimeExponentP

```java
public
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP.

- getPrimeExponentQ

```java
public
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ.

- getCrtCoefficient

```java
public
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient.

- getOtherPrimeInfo

```java
public
RSAOtherPrimeInfo
[] getOtherPrimeInfo()
```

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

**Returns:** the otherPrimeInfo. Returns a new array each time this method
is called.

Constructor Detail

- RSAMultiPrimePrivateCrtKeySpec

```java
public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo)
```

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of q
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
**Parameters:** otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)
**Throws:** NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

is null
**Throws:** IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified

- RSAMultiPrimePrivateCrtKeySpec

```java
public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo,

AlgorithmParameterSpec
keyParams)
```

Creates a new

RSAMultiPrimePrivateCrtKeySpec

with additional
key parameters.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

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

- the Chinese Remainder Theorem coefficient
q-1 mod p
**Parameters:** otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)
**Parameters:** keyParams

- the parameters associated with key
**Throws:** NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

and

keyParams

is null
**Throws:** IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified
**Since:** 11

---

#### Constructor Detail

RSAMultiPrimePrivateCrtKeySpec

```java
public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo)
```

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

**Parameters:** modulus

- the modulus n
**Parameters:** publicExponent

- the public exponent e
**Parameters:** privateExponent

- the private exponent d
**Parameters:** primeP

- the prime factor p of n
**Parameters:** primeQ

- the prime factor q of q
**Parameters:** primeExponentP

- this is d mod (p-1)
**Parameters:** primeExponentQ

- this is d mod (q-1)
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient q-1 mod p
**Parameters:** otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)
**Throws:** NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

is null
**Throws:** IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified

---

#### RSAMultiPrimePrivateCrtKeySpec

public RSAMultiPrimePrivateCrtKeySpec​(

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

RSAOtherPrimeInfo

[] otherPrimeInfo)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

RSAMultiPrimePrivateCrtKeySpec

```java
public RSAMultiPrimePrivateCrtKeySpec​(
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

RSAOtherPrimeInfo
[] otherPrimeInfo,

AlgorithmParameterSpec
keyParams)
```

Creates a new

RSAMultiPrimePrivateCrtKeySpec

with additional
key parameters.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

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

- the Chinese Remainder Theorem coefficient
q-1 mod p
**Parameters:** otherPrimeInfo

- triplets of the rest of primes, null can be
specified if there are only two prime factors
(p and q)
**Parameters:** keyParams

- the parameters associated with key
**Throws:** NullPointerException

- if any of the specified parameters
with the exception of

otherPrimeInfo

and

keyParams

is null
**Throws:** IllegalArgumentException

- if an empty, i.e. 0-length,

otherPrimeInfo

is specified
**Since:** 11

---

#### RSAMultiPrimePrivateCrtKeySpec

public RSAMultiPrimePrivateCrtKeySpec​(

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

RSAOtherPrimeInfo

[] otherPrimeInfo,

AlgorithmParameterSpec

keyParams)

Creates a new

RSAMultiPrimePrivateCrtKeySpec

with additional
key parameters.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

Note that the contents of

otherPrimeInfo

are copied to protect against subsequent modification when
constructing this object.

Method Detail

- getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent.

- getPrimeP

```java
public
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP.

- getPrimeQ

```java
public
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ.

- getPrimeExponentP

```java
public
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP.

- getPrimeExponentQ

```java
public
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ.

- getCrtCoefficient

```java
public
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient.

- getOtherPrimeInfo

```java
public
RSAOtherPrimeInfo
[] getOtherPrimeInfo()
```

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

**Returns:** the otherPrimeInfo. Returns a new array each time this method
is called.

---

#### Method Detail

getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent.

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

**Returns:** the primeP.

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

**Returns:** the primeQ.

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

**Returns:** the primeExponentP.

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

**Returns:** the primeExponentQ.

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

**Returns:** the crtCoefficient.

---

#### getCrtCoefficient

public

BigInteger

getCrtCoefficient()

Returns the crtCoefficient.

getOtherPrimeInfo

```java
public
RSAOtherPrimeInfo
[] getOtherPrimeInfo()
```

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

**Returns:** the otherPrimeInfo. Returns a new array each time this method
is called.

---

#### getOtherPrimeInfo

public

RSAOtherPrimeInfo

[] getOtherPrimeInfo()

Returns a copy of the otherPrimeInfo or null if there are
only two prime factors (p and q).

---

