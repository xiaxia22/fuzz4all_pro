# Interface PublicKey

**Source:** `java.base\java\security\PublicKey.html`

### Class Description

```java
public interface
PublicKey

extends
Key
```

A public key. This interface contains no methods or constants.
It merely serves to group (and provide type safety for) all public key
interfaces.

Note: The specialized public key interfaces extend this interface.
See, for example, the DSAPublicKey interface in

java.security.interfaces

.

**All Superinterfaces:** Key

,

Serializable

---

### Field Details

#### static final long serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility with a previous version of the class.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface PublicKey

**All Superinterfaces:** Key

,

Serializable

**All Known Subinterfaces:** DHPublicKey

,

DSAPublicKey

,

ECPublicKey

,

RSAPublicKey

,

XECPublicKey

```java
public interface
PublicKey

extends
Key
```

A public key. This interface contains no methods or constants.
It merely serves to group (and provide type safety for) all public key
interfaces.

Note: The specialized public key interfaces extend this interface.
See, for example, the DSAPublicKey interface in

java.security.interfaces

.

**Since:** 1.1
**See Also:** Key

,

PrivateKey

,

Certificate

,

Signature.initVerify(java.security.PublicKey)

,

DSAPublicKey

,

RSAPublicKey

public interface

PublicKey

extends

Key

A public key. This interface contains no methods or constants.
It merely serves to group (and provide type safety for) all public key
interfaces.

Note: The specialized public key interfaces extend this interface.
See, for example, the DSAPublicKey interface in

java.security.interfaces

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility with a previous version of the class.

========== METHOD SUMMARY ===========

- Method Summary

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
compatibility with a previous version of the class.

---

#### Field Summary

The class fingerprint that is set to indicate serialization
compatibility with a previous version of the class.

Method Summary

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

---

#### Method Summary

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
compatibility with a previous version of the class.

**See Also:** Constant Field Values

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility with a previous version of the class.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility with a previous version of the class.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility with a previous version of the class.

---

