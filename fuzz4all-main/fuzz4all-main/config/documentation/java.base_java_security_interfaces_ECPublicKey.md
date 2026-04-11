# Interface ECPublicKey

**Source:** `java.base\java\security\interfaces\ECPublicKey.html`

### Class Description

```java
public interface
ECPublicKey

extends
PublicKey
,
ECKey
```

The interface to an elliptic curve (EC) public key.

**All Superinterfaces:** ECKey

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
serialization compatibility.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### ECPoint
getW()

Returns the public point W.

**Returns:**
- the public point W.

---

### Additional Sections

#### Interface ECPublicKey

**All Superinterfaces:** ECKey

,

Key

,

PublicKey

,

Serializable

```java
public interface
ECPublicKey

extends
PublicKey
,
ECKey
```

The interface to an elliptic curve (EC) public key.

**Since:** 1.5
**See Also:** PublicKey

,

ECKey

,

ECPoint

public interface

ECPublicKey

extends

PublicKey

,

ECKey

The interface to an elliptic curve (EC) public key.

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

ECPoint

getW

()

Returns the public point W.

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

ECPoint

getW

()

Returns the public point W.

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

Returns the public point W.

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

- getW

```java
ECPoint
getW()
```

Returns the public point W.

**Returns:** the public point W.

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

- getW

```java
ECPoint
getW()
```

Returns the public point W.

**Returns:** the public point W.

---

#### Method Detail

getW

```java
ECPoint
getW()
```

Returns the public point W.

**Returns:** the public point W.

---

#### getW

ECPoint

getW()

Returns the public point W.

---

