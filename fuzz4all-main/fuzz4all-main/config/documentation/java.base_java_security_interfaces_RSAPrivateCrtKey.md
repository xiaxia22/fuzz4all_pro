# Interface RSAPrivateCrtKey

**Source:** `java.base\java\security\interfaces\RSAPrivateCrtKey.html`

### Class Description

```java
public interface
RSAPrivateCrtKey

extends
RSAPrivateKey
```

The interface to an RSA private key, as defined in the

PKCS#1 v2.2

standard,
using the

Chinese Remainder Theorem

(CRT) information values.

**All Superinterfaces:** Destroyable

,

Key

,

PrivateKey

,

RSAKey

,

RSAPrivateKey

,

Serializable

---

### Field Details

#### static final long serialVersionUID

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### BigInteger
getPublicExponent()

Returns the public exponent.

**Returns:**
- the public exponent

---

#### BigInteger
getPrimeP()

Returns the primeP.

**Returns:**
- the primeP

---

#### BigInteger
getPrimeQ()

Returns the primeQ.

**Returns:**
- the primeQ

---

#### BigInteger
getPrimeExponentP()

Returns the primeExponentP.

**Returns:**
- the primeExponentP

---

#### BigInteger
getPrimeExponentQ()

Returns the primeExponentQ.

**Returns:**
- the primeExponentQ

---

#### BigInteger
getCrtCoefficient()

Returns the crtCoefficient.

**Returns:**
- the crtCoefficient

---

### Additional Sections

#### Interface RSAPrivateCrtKey

**All Superinterfaces:** Destroyable

,

Key

,

PrivateKey

,

RSAKey

,

RSAPrivateKey

,

Serializable

```java
public interface
RSAPrivateCrtKey

extends
RSAPrivateKey
```

The interface to an RSA private key, as defined in the

PKCS#1 v2.2

standard,
using the

Chinese Remainder Theorem

(CRT) information values.

**Since:** 1.2
**See Also:** RSAPrivateKey

public interface

RSAPrivateCrtKey

extends

RSAPrivateKey

The interface to an RSA private key, as defined in the

PKCS#1 v2.2

standard,
using the

Chinese Remainder Theorem

(CRT) information values.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

- Methods declared in interface java.security.interfaces.

RSAKey

getModulus

,

getParams

- Methods declared in interface java.security.interfaces.

RSAPrivateKey

getPrivateExponent

Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

---

#### Field Summary

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

- Methods declared in interface java.security.interfaces.

RSAKey

getModulus

,

getParams

- Methods declared in interface java.security.interfaces.

RSAPrivateKey

getPrivateExponent

---

#### Method Summary

Returns the crtCoefficient.

Returns the primeExponentP.

Returns the primeExponentQ.

Returns the primeP.

Returns the primeQ.

Returns the public exponent.

Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

---

#### Methods declared in interface javax.security.auth. Destroyable

Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

---

#### Methods declared in interface java.security. Key

Methods declared in interface java.security.interfaces.

RSAKey

getModulus

,

getParams

---

#### Methods declared in interface java.security.interfaces. RSAKey

Methods declared in interface java.security.interfaces.

RSAPrivateKey

getPrivateExponent

---

#### Methods declared in interface java.security.interfaces. RSAPrivateKey

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getPublicExponent

```java
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

- getPrimeP

```java
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP

- getPrimeQ

```java
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ

- getPrimeExponentP

```java
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP

- getPrimeExponentQ

```java
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ

- getCrtCoefficient

```java
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The type fingerprint that is set to indicate
serialization compatibility with a previous
version of the type.

Method Detail

- getPublicExponent

```java
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

- getPrimeP

```java
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP

- getPrimeQ

```java
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ

- getPrimeExponentP

```java
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP

- getPrimeExponentQ

```java
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ

- getCrtCoefficient

```java
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient

---

#### Method Detail

getPublicExponent

```java
BigInteger
getPublicExponent()
```

Returns the public exponent.

**Returns:** the public exponent

---

#### getPublicExponent

BigInteger

getPublicExponent()

Returns the public exponent.

getPrimeP

```java
BigInteger
getPrimeP()
```

Returns the primeP.

**Returns:** the primeP

---

#### getPrimeP

BigInteger

getPrimeP()

Returns the primeP.

getPrimeQ

```java
BigInteger
getPrimeQ()
```

Returns the primeQ.

**Returns:** the primeQ

---

#### getPrimeQ

BigInteger

getPrimeQ()

Returns the primeQ.

getPrimeExponentP

```java
BigInteger
getPrimeExponentP()
```

Returns the primeExponentP.

**Returns:** the primeExponentP

---

#### getPrimeExponentP

BigInteger

getPrimeExponentP()

Returns the primeExponentP.

getPrimeExponentQ

```java
BigInteger
getPrimeExponentQ()
```

Returns the primeExponentQ.

**Returns:** the primeExponentQ

---

#### getPrimeExponentQ

BigInteger

getPrimeExponentQ()

Returns the primeExponentQ.

getCrtCoefficient

```java
BigInteger
getCrtCoefficient()
```

Returns the crtCoefficient.

**Returns:** the crtCoefficient

---

#### getCrtCoefficient

BigInteger

getCrtCoefficient()

Returns the crtCoefficient.

---

