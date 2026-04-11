# Interface DHPrivateKey

**Source:** `java.base\javax\crypto\interfaces\DHPrivateKey.html`

### Class Description

```java
public interface
DHPrivateKey

extends
DHKey
,
PrivateKey
```

The interface to a Diffie-Hellman private key.

**All Superinterfaces:** Destroyable

,

DHKey

,

Key

,

PrivateKey

,

Serializable

---

### Field Details

#### static final long serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### BigInteger
getX()

Returns the private value,

x

.

**Returns:**
- the private value,

x

---

### Additional Sections

#### Interface DHPrivateKey

**All Superinterfaces:** Destroyable

,

DHKey

,

Key

,

PrivateKey

,

Serializable

```java
public interface
DHPrivateKey

extends
DHKey
,
PrivateKey
```

The interface to a Diffie-Hellman private key.

**Since:** 1.4
**See Also:** DHKey

,

DHPublicKey

public interface

DHPrivateKey

extends

DHKey

,

PrivateKey

The interface to a Diffie-Hellman private key.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

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

Returns the private value,

x

.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface javax.crypto.interfaces.

DHKey

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

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

---

#### Field Summary

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

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

Returns the private value,

x

.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface javax.crypto.interfaces.

DHKey

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

Returns the private value,

x

.

Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

---

#### Methods declared in interface javax.security.auth. Destroyable

Methods declared in interface javax.crypto.interfaces.

DHKey

getParams

---

#### Methods declared in interface javax.crypto.interfaces. DHKey

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

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getX

```java
BigInteger
getX()
```

Returns the private value,

x

.

**Returns:** the private value,

x

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

Method Detail

- getX

```java
BigInteger
getX()
```

Returns the private value,

x

.

**Returns:** the private value,

x

---

#### Method Detail

getX

```java
BigInteger
getX()
```

Returns the private value,

x

.

**Returns:** the private value,

x

---

#### getX

BigInteger

getX()

Returns the private value,

x

.

---

