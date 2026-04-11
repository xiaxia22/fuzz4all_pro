# Interface RSAPrivateKey

**Source:** `java.base\java\security\interfaces\RSAPrivateKey.html`

### Class Description

```java
public interface
RSAPrivateKey

extends
PrivateKey
,
RSAKey
```

The interface to an RSA private key.

**All Superinterfaces:** Destroyable

,

Key

,

PrivateKey

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
getPrivateExponent()

Returns the private exponent.

**Returns:**
- the private exponent

---

### Additional Sections

#### Interface RSAPrivateKey

**All Superinterfaces:** Destroyable

,

Key

,

PrivateKey

,

RSAKey

,

Serializable

**All Known Subinterfaces:** RSAMultiPrimePrivateCrtKey

,

RSAPrivateCrtKey

```java
public interface
RSAPrivateKey

extends
PrivateKey
,
RSAKey
```

The interface to an RSA private key.

**Since:** 1.2
**See Also:** RSAPrivateCrtKey

public interface

RSAPrivateKey

extends

PrivateKey

,

RSAKey

The interface to an RSA private key.

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

getPrivateExponent

()

Returns the private exponent.

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

getPrivateExponent

()

Returns the private exponent.

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

---

#### Method Summary

Returns the private exponent.

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

- getPrivateExponent

```java
BigInteger
getPrivateExponent()
```

Returns the private exponent.

**Returns:** the private exponent

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

- getPrivateExponent

```java
BigInteger
getPrivateExponent()
```

Returns the private exponent.

**Returns:** the private exponent

---

#### Method Detail

getPrivateExponent

```java
BigInteger
getPrivateExponent()
```

Returns the private exponent.

**Returns:** the private exponent

---

#### getPrivateExponent

BigInteger

getPrivateExponent()

Returns the private exponent.

---

