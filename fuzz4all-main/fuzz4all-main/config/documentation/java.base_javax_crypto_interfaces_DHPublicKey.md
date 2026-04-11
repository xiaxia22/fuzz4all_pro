# Interface DHPublicKey

**Source:** `java.base\javax\crypto\interfaces\DHPublicKey.html`

### Class Description

```java
public interface
DHPublicKey

extends
DHKey
,
PublicKey
```

The interface to a Diffie-Hellman public key.

**All Superinterfaces:** DHKey

,

Key

,

PublicKey

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
getY()

Returns the public value,

y

.

**Returns:**
- the public value,

y

---

### Additional Sections

#### Interface DHPublicKey

**All Superinterfaces:** DHKey

,

Key

,

PublicKey

,

Serializable

```java
public interface
DHPublicKey

extends
DHKey
,
PublicKey
```

The interface to a Diffie-Hellman public key.

**Since:** 1.4
**See Also:** DHKey

,

DHPrivateKey

public interface

DHPublicKey

extends

DHKey

,

PublicKey

The interface to a Diffie-Hellman public key.

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

getY

()

Returns the public value,

y

.

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

getY

()

Returns the public value,

y

.

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

Returns the public value,

y

.

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

- getY

```java
BigInteger
getY()
```

Returns the public value,

y

.

**Returns:** the public value,

y

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

- getY

```java
BigInteger
getY()
```

Returns the public value,

y

.

**Returns:** the public value,

y

---

#### Method Detail

getY

```java
BigInteger
getY()
```

Returns the public value,

y

.

**Returns:** the public value,

y

---

#### getY

BigInteger

getY()

Returns the public value,

y

.

---

