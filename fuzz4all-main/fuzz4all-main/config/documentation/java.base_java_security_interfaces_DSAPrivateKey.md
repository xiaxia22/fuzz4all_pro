# Interface DSAPrivateKey

**Source:** `java.base\java\security\interfaces\DSAPrivateKey.html`

### Class Description

```java
public interface
DSAPrivateKey

extends
DSAKey
,
PrivateKey
```

The standard interface to a DSA private key. DSA (Digital Signature
Algorithm) is defined in NIST's FIPS-186.

**All Superinterfaces:** Destroyable

,

DSAKey

,

Key

,

PrivateKey

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
getX()

Returns the value of the private key,

x

.

**Returns:**
- the value of the private key,

x

.

---

### Additional Sections

#### Interface DSAPrivateKey

**All Superinterfaces:** Destroyable

,

DSAKey

,

Key

,

PrivateKey

,

Serializable

```java
public interface
DSAPrivateKey

extends
DSAKey
,
PrivateKey
```

The standard interface to a DSA private key. DSA (Digital Signature
Algorithm) is defined in NIST's FIPS-186.

**Since:** 1.1
**See Also:** Key

,

Signature

,

DSAKey

,

DSAPublicKey

public interface

DSAPrivateKey

extends

DSAKey

,

PrivateKey

The standard interface to a DSA private key. DSA (Digital Signature
Algorithm) is defined in NIST's FIPS-186.

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

getX

()

Returns the value of the private key,

x

.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

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

getX

()

Returns the value of the private key,

x

.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

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

Returns the value of the private key,

x

.

Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

---

#### Methods declared in interface javax.security.auth. Destroyable

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

- getX

```java
BigInteger
getX()
```

Returns the value of the private key,

x

.

**Returns:** the value of the private key,

x

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

- getX

```java
BigInteger
getX()
```

Returns the value of the private key,

x

.

**Returns:** the value of the private key,

x

.

---

#### Method Detail

getX

```java
BigInteger
getX()
```

Returns the value of the private key,

x

.

**Returns:** the value of the private key,

x

.

---

#### getX

BigInteger

getX()

Returns the value of the private key,

x

.

---

