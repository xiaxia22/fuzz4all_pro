# Interface RSAPublicKey

**Source:** `java.base\java\security\interfaces\RSAPublicKey.html`

### Class Description

```java
public interface
RSAPublicKey

extends
PublicKey
,
RSAKey
```

The interface to an RSA public key.

**All Superinterfaces:** Key

,

PublicKey

,

RSAKey

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

### Additional Sections

#### Interface RSAPublicKey

**All Superinterfaces:** Key

,

PublicKey

,

RSAKey

,

Serializable

```java
public interface
RSAPublicKey

extends
PublicKey
,
RSAKey
```

The interface to an RSA public key.

**Since:** 1.2

public interface

RSAPublicKey

extends

PublicKey

,

RSAKey

The interface to an RSA public key.

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

getPublicExponent

()

Returns the public exponent.

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

getPublicExponent

()

Returns the public exponent.

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

---

#### Method Summary

Returns the public exponent.

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

---

