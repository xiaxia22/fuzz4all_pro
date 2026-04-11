# Interface RSAKey

**Source:** `java.base\java\security\interfaces\RSAKey.html`

### Class Description

```java
public interface
RSAKey
```

The interface to a public or private key in

PKCS#1 v2.2

standard,
such as those for RSA, or RSASSA-PSS algorithms.

**All Known Subinterfaces:** RSAMultiPrimePrivateCrtKey

,

RSAPrivateCrtKey

,

RSAPrivateKey

,

RSAPublicKey

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### BigInteger
getModulus()

Returns the modulus.

**Returns:**
- the modulus

---

#### default
AlgorithmParameterSpec
getParams()

Returns the parameters associated with this key.
The parameters are optional and may be either
explicitly specified or implicitly created during
key pair generation.

**Returns:**
- the associated parameters, may be null

**Since:**
- 11

**Implementation Requirements:**
- The default implementation returns

null

.

---

### Additional Sections

#### Interface RSAKey

**All Known Subinterfaces:** RSAMultiPrimePrivateCrtKey

,

RSAPrivateCrtKey

,

RSAPrivateKey

,

RSAPublicKey

```java
public interface
RSAKey
```

The interface to a public or private key in

PKCS#1 v2.2

standard,
such as those for RSA, or RSASSA-PSS algorithms.

**Since:** 1.3
**See Also:** RSAPublicKey

,

RSAPrivateKey

public interface

RSAKey

The interface to a public or private key in

PKCS#1 v2.2

standard,
such as those for RSA, or RSASSA-PSS algorithms.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

BigInteger

getModulus

()

Returns the modulus.

default

AlgorithmParameterSpec

getParams

()

Returns the parameters associated with this key.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

BigInteger

getModulus

()

Returns the modulus.

default

AlgorithmParameterSpec

getParams

()

Returns the parameters associated with this key.

---

#### Method Summary

Returns the modulus.

Returns the parameters associated with this key.

============ METHOD DETAIL ==========

- Method Detail

- getModulus

```java
BigInteger
getModulus()
```

Returns the modulus.

**Returns:** the modulus

- getParams

```java
default
AlgorithmParameterSpec
getParams()
```

Returns the parameters associated with this key.
The parameters are optional and may be either
explicitly specified or implicitly created during
key pair generation.

**Implementation Requirements:** The default implementation returns

null

.
**Returns:** the associated parameters, may be null
**Since:** 11

Method Detail

- getModulus

```java
BigInteger
getModulus()
```

Returns the modulus.

**Returns:** the modulus

- getParams

```java
default
AlgorithmParameterSpec
getParams()
```

Returns the parameters associated with this key.
The parameters are optional and may be either
explicitly specified or implicitly created during
key pair generation.

**Implementation Requirements:** The default implementation returns

null

.
**Returns:** the associated parameters, may be null
**Since:** 11

---

#### Method Detail

getModulus

```java
BigInteger
getModulus()
```

Returns the modulus.

**Returns:** the modulus

---

#### getModulus

BigInteger

getModulus()

Returns the modulus.

getParams

```java
default
AlgorithmParameterSpec
getParams()
```

Returns the parameters associated with this key.
The parameters are optional and may be either
explicitly specified or implicitly created during
key pair generation.

**Implementation Requirements:** The default implementation returns

null

.
**Returns:** the associated parameters, may be null
**Since:** 11

---

#### getParams

default

AlgorithmParameterSpec

getParams()

Returns the parameters associated with this key.
The parameters are optional and may be either
explicitly specified or implicitly created during
key pair generation.

---

