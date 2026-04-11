# Interface ECPrivateKey

**Source:** `java.base\java\security\interfaces\ECPrivateKey.html`

### Class Description

```java
public interface
ECPrivateKey

extends
PrivateKey
,
ECKey
```

The interface to an elliptic curve (EC) private key.

**All Superinterfaces:** Destroyable

,

ECKey

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
serialization compatibility.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### BigInteger
getS()

Returns the private value S.

**Returns:**
- the private value S.

---

### Additional Sections

#### Interface ECPrivateKey

**All Superinterfaces:** Destroyable

,

ECKey

,

Key

,

PrivateKey

,

Serializable

```java
public interface
ECPrivateKey

extends
PrivateKey
,
ECKey
```

The interface to an elliptic curve (EC) private key.

**Since:** 1.5
**See Also:** PrivateKey

,

ECKey

public interface

ECPrivateKey

extends

PrivateKey

,

ECKey

The interface to an elliptic curve (EC) private key.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getS

()

Returns the private value S.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface java.security.interfaces.

ECKey

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
serialization compatibility.

---

#### Field Summary

The class fingerprint that is set to indicate
serialization compatibility.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getS

()

Returns the private value S.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface java.security.interfaces.

ECKey

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

Returns the private value S.

Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

---

#### Methods declared in interface javax.security.auth. Destroyable

Methods declared in interface java.security.interfaces.

ECKey

getParams

---

#### Methods declared in interface java.security.interfaces. ECKey

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
serialization compatibility.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getS

```java
BigInteger
getS()
```

Returns the private value S.

**Returns:** the private value S.

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility.

Method Detail

- getS

```java
BigInteger
getS()
```

Returns the private value S.

**Returns:** the private value S.

---

#### Method Detail

getS

```java
BigInteger
getS()
```

Returns the private value S.

**Returns:** the private value S.

---

#### getS

BigInteger

getS()

Returns the private value S.

---

