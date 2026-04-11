# Interface Destroyable

**Source:** `java.base\javax\security\auth\Destroyable.html`

### Class Description

```java
public interface
Destroyable
```

Objects such as credentials may optionally implement this interface
to provide the capability to destroy its contents.

**All Known Subinterfaces:** DHPrivateKey

,

DSAPrivateKey

,

ECPrivateKey

,

PBEKey

,

PrivateKey

,

RSAMultiPrimePrivateCrtKey

,

RSAPrivateCrtKey

,

RSAPrivateKey

,

SecretKey

,

XECPrivateKey

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default void destroy()
throws
DestroyFailedException

Destroy this

Object

.

Sensitive information associated with this

Object

is destroyed or cleared. Subsequent calls to certain methods
on this

Object

will result in an

IllegalStateException

being thrown.

**Throws:**
- DestroyFailedException

- if the destroy operation fails.
- SecurityException

- if the caller does not have permission
to destroy this

Object

.

**Implementation Requirements:**
- The default implementation throws

DestroyFailedException

.

---

#### default boolean isDestroyed()

Determine if this

Object

has been destroyed.

**Returns:**
- true if this

Object

has been destroyed,
false otherwise.

**Implementation Requirements:**
- The default implementation returns false.

---

### Additional Sections

#### Interface Destroyable

**All Known Subinterfaces:** DHPrivateKey

,

DSAPrivateKey

,

ECPrivateKey

,

PBEKey

,

PrivateKey

,

RSAMultiPrimePrivateCrtKey

,

RSAPrivateCrtKey

,

RSAPrivateKey

,

SecretKey

,

XECPrivateKey

**All Known Implementing Classes:** EncryptionKey

,

KerberosCredMessage

,

KerberosKey

,

KerberosTicket

,

KeyStore.PasswordProtection

,

SecretKeySpec

,

X500PrivateCredential

```java
public interface
Destroyable
```

Objects such as credentials may optionally implement this interface
to provide the capability to destroy its contents.

**Since:** 1.4
**See Also:** Subject

public interface

Destroyable

Objects such as credentials may optionally implement this interface
to provide the capability to destroy its contents.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default void

destroy

()

Destroy this

Object

.

default boolean

isDestroyed

()

Determine if this

Object

has been destroyed.

Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default void

destroy

()

Destroy this

Object

.

default boolean

isDestroyed

()

Determine if this

Object

has been destroyed.

---

#### Method Summary

Destroy this

Object

.

Determine if this

Object

has been destroyed.

============ METHOD DETAIL ==========

- Method Detail

- destroy

```java
default void destroy()
throws
DestroyFailedException
```

Destroy this

Object

.

Sensitive information associated with this

Object

is destroyed or cleared. Subsequent calls to certain methods
on this

Object

will result in an

IllegalStateException

being thrown.

**Implementation Requirements:** The default implementation throws

DestroyFailedException

.
**Throws:** DestroyFailedException

- if the destroy operation fails.
**Throws:** SecurityException

- if the caller does not have permission
to destroy this

Object

.

- isDestroyed

```java
default boolean isDestroyed()
```

Determine if this

Object

has been destroyed.

**Implementation Requirements:** The default implementation returns false.
**Returns:** true if this

Object

has been destroyed,
false otherwise.

Method Detail

- destroy

```java
default void destroy()
throws
DestroyFailedException
```

Destroy this

Object

.

Sensitive information associated with this

Object

is destroyed or cleared. Subsequent calls to certain methods
on this

Object

will result in an

IllegalStateException

being thrown.

**Implementation Requirements:** The default implementation throws

DestroyFailedException

.
**Throws:** DestroyFailedException

- if the destroy operation fails.
**Throws:** SecurityException

- if the caller does not have permission
to destroy this

Object

.

- isDestroyed

```java
default boolean isDestroyed()
```

Determine if this

Object

has been destroyed.

**Implementation Requirements:** The default implementation returns false.
**Returns:** true if this

Object

has been destroyed,
false otherwise.

---

#### Method Detail

destroy

```java
default void destroy()
throws
DestroyFailedException
```

Destroy this

Object

.

Sensitive information associated with this

Object

is destroyed or cleared. Subsequent calls to certain methods
on this

Object

will result in an

IllegalStateException

being thrown.

**Implementation Requirements:** The default implementation throws

DestroyFailedException

.
**Throws:** DestroyFailedException

- if the destroy operation fails.
**Throws:** SecurityException

- if the caller does not have permission
to destroy this

Object

.

---

#### destroy

default void destroy()
throws

DestroyFailedException

Destroy this

Object

.

Sensitive information associated with this

Object

is destroyed or cleared. Subsequent calls to certain methods
on this

Object

will result in an

IllegalStateException

being thrown.

Sensitive information associated with this

Object

is destroyed or cleared. Subsequent calls to certain methods
on this

Object

will result in an

IllegalStateException

being thrown.

isDestroyed

```java
default boolean isDestroyed()
```

Determine if this

Object

has been destroyed.

**Implementation Requirements:** The default implementation returns false.
**Returns:** true if this

Object

has been destroyed,
false otherwise.

---

#### isDestroyed

default boolean isDestroyed()

Determine if this

Object

has been destroyed.

---

