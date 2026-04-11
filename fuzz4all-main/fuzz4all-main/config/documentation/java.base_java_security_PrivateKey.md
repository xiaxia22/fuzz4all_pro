# Interface PrivateKey

**Source:** `java.base\java\security\PrivateKey.html`

### Class Description

```java
public interface
PrivateKey

extends
Key
,
Destroyable
```

A private key.
The purpose of this interface is to group (and provide type safety
for) all private key interfaces.

Note: The specialized private key interfaces extend this interface.
See, for example, the

DSAPrivateKey

interface in

java.security.interfaces

.

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

PrivateKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

**All Superinterfaces:** Destroyable

,

Key

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

#### Interface PrivateKey

**All Superinterfaces:** Destroyable

,

Key

,

Serializable

**All Known Subinterfaces:** DHPrivateKey

,

DSAPrivateKey

,

ECPrivateKey

,

RSAMultiPrimePrivateCrtKey

,

RSAPrivateCrtKey

,

RSAPrivateKey

,

XECPrivateKey

```java
public interface
PrivateKey

extends
Key
,
Destroyable
```

A private key.
The purpose of this interface is to group (and provide type safety
for) all private key interfaces.

Note: The specialized private key interfaces extend this interface.
See, for example, the

DSAPrivateKey

interface in

java.security.interfaces

.

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

PrivateKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

**Since:** 1.1
**See Also:** Key

,

PublicKey

,

Certificate

,

Signature.initVerify(java.security.PublicKey)

,

DSAPrivateKey

,

RSAPrivateKey

,

RSAPrivateCrtKey

public interface

PrivateKey

extends

Key

,

Destroyable

A private key.
The purpose of this interface is to group (and provide type safety
for) all private key interfaces.

Note: The specialized private key interfaces extend this interface.
See, for example, the

DSAPrivateKey

interface in

java.security.interfaces

.

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

PrivateKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

Note: The specialized private key interfaces extend this interface.
See, for example, the

DSAPrivateKey

interface in

java.security.interfaces

.

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

PrivateKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

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

PrivateKey

is

Serializable

, implementations
should also override

ObjectOutputStream.writeObject(java.lang.Object)

to prevent keys that have been destroyed from being serialized.

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
compatibility with a previous version of the class.

---

#### Field Summary

The class fingerprint that is set to indicate serialization
compatibility with a previous version of the class.

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

