# Interface SecretKey

**Source:** `java.base\javax\crypto\SecretKey.html`

### Class Description

```java
public interface
SecretKey

extends
Key
,
Destroyable
```

A secret (symmetric) key.
The purpose of this interface is to group (and provide type safety
for) all secret key interfaces.

Provider implementations of this interface must overwrite the

equals

and

hashCode

methods inherited from

Object

, so that secret keys are compared based on
their underlying key material and not based on reference.
Implementations should override the default

destroy

and

isDestroyed

methods from the

Destroyable

interface to enable
sensitive key information to be destroyed, cleared, or in the case
where such information is immutable, unreferenced.
Finally, since

SecretKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

Keys that implement this interface return the string

RAW

as their encoding format (see

getFormat

), and return the
raw key bytes as the result of a

getEncoded

method call. (The

getFormat

and

getEncoded

methods are inherited
from the

Key

parent interface.)

**All Superinterfaces:** Destroyable

,

Key

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

*No entries found.*

### Additional Sections

#### Interface SecretKey

**All Superinterfaces:** Destroyable

,

Key

,

Serializable

**All Known Subinterfaces:** PBEKey

**All Known Implementing Classes:** EncryptionKey

,

KerberosKey

,

SecretKeySpec

```java
public interface
SecretKey

extends
Key
,
Destroyable
```

A secret (symmetric) key.
The purpose of this interface is to group (and provide type safety
for) all secret key interfaces.

Provider implementations of this interface must overwrite the

equals

and

hashCode

methods inherited from

Object

, so that secret keys are compared based on
their underlying key material and not based on reference.
Implementations should override the default

destroy

and

isDestroyed

methods from the

Destroyable

interface to enable
sensitive key information to be destroyed, cleared, or in the case
where such information is immutable, unreferenced.
Finally, since

SecretKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

Keys that implement this interface return the string

RAW

as their encoding format (see

getFormat

), and return the
raw key bytes as the result of a

getEncoded

method call. (The

getFormat

and

getEncoded

methods are inherited
from the

Key

parent interface.)

**Since:** 1.4
**See Also:** SecretKeyFactory

,

Cipher

public interface

SecretKey

extends

Key

,

Destroyable

A secret (symmetric) key.
The purpose of this interface is to group (and provide type safety
for) all secret key interfaces.

Provider implementations of this interface must overwrite the

equals

and

hashCode

methods inherited from

Object

, so that secret keys are compared based on
their underlying key material and not based on reference.
Implementations should override the default

destroy

and

isDestroyed

methods from the

Destroyable

interface to enable
sensitive key information to be destroyed, cleared, or in the case
where such information is immutable, unreferenced.
Finally, since

SecretKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

Keys that implement this interface return the string

RAW

as their encoding format (see

getFormat

), and return the
raw key bytes as the result of a

getEncoded

method call. (The

getFormat

and

getEncoded

methods are inherited
from the

Key

parent interface.)

Provider implementations of this interface must overwrite the

equals

and

hashCode

methods inherited from

Object

, so that secret keys are compared based on
their underlying key material and not based on reference.
Implementations should override the default

destroy

and

isDestroyed

methods from the

Destroyable

interface to enable
sensitive key information to be destroyed, cleared, or in the case
where such information is immutable, unreferenced.
Finally, since

SecretKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

Keys that implement this interface return the string

RAW

as their encoding format (see

getFormat

), and return the
raw key bytes as the result of a

getEncoded

method call. (The

getFormat

and

getEncoded

methods are inherited
from the

Key

parent interface.)

Keys that implement this interface return the string

RAW

as their encoding format (see

getFormat

), and return the
raw key bytes as the result of a

getEncoded

method call. (The

getFormat

and

getEncoded

methods are inherited
from the

Key

parent interface.)

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

---

#### Method Summary

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

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:** Constant Field Values

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

---

