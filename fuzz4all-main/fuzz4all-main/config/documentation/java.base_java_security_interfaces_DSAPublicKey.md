# Interface DSAPublicKey

**Source:** `java.base\java\security\interfaces\DSAPublicKey.html`

### Class Description

```java
public interface
DSAPublicKey

extends
DSAKey
,
PublicKey
```

The interface to a DSA public key. DSA (Digital Signature Algorithm)
is defined in NIST's FIPS-186.

**All Superinterfaces:** DSAKey

,

Key

,

PublicKey

,

Serializable

---

### Field Details

#### static final long serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### BigInteger
getY()

Returns the value of the public key,

y

.

**Returns:**
- the value of the public key,

y

.

---

### Additional Sections

#### Interface DSAPublicKey

**All Superinterfaces:** DSAKey

,

Key

,

PublicKey

,

Serializable

```java
public interface
DSAPublicKey

extends
DSAKey
,
PublicKey
```

The interface to a DSA public key. DSA (Digital Signature Algorithm)
is defined in NIST's FIPS-186.

**Since:** 1.1
**See Also:** Key

,

Signature

,

DSAKey

,

DSAPrivateKey

public interface

DSAPublicKey

extends

DSAKey

,

PublicKey

The interface to a DSA public key. DSA (Digital Signature Algorithm)
is defined in NIST's FIPS-186.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getY

()

Returns the value of the public key,

y

.

- Methods declared in interface java.security.interfaces.

DSAKey

getParams

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

---

#### Field Summary

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getY

()

Returns the value of the public key,

y

.

- Methods declared in interface java.security.interfaces.

DSAKey

getParams

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

---

#### Method Summary

Returns the value of the public key,

y

.

Methods declared in interface java.security.interfaces.

DSAKey

getParams

---

#### Methods declared in interface java.security.interfaces. DSAKey

Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

---

#### Methods declared in interface java.security. Key

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getY

```java
BigInteger
getY()
```

Returns the value of the public key,

y

.

**Returns:** the value of the public key,

y

.

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

Method Detail

- getY

```java
BigInteger
getY()
```

Returns the value of the public key,

y

.

**Returns:** the value of the public key,

y

.

---

#### Method Detail

getY

```java
BigInteger
getY()
```

Returns the value of the public key,

y

.

**Returns:** the value of the public key,

y

.

---

#### getY

BigInteger

getY()

Returns the value of the public key,

y

.

---

