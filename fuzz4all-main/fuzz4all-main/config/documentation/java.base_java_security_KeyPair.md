# Class KeyPair

**Source:** `java.base\java\security\KeyPair.html`

### Class Description

```java
public final class
KeyPair

extends
Object

implements
Serializable
```

This class is a simple holder for a key pair (a public key and a
private key). It does not enforce any security, and, when initialized,
should be treated like a PrivateKey.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyPair​(
PublicKey
publicKey,

PrivateKey
privateKey)

Constructs a key pair from the given public key and private key.

Note that this constructor only stores references to the public
and private key components in the generated key pair. This is safe,
because

Key

objects are immutable.

**Parameters:**
- publicKey

- the public key.
- privateKey

- the private key.

---

### Method Details

#### public
PublicKey
getPublic()

Returns a reference to the public key component of this key pair.

**Returns:**
- a reference to the public key.

---

#### public
PrivateKey
getPrivate()

Returns a reference to the private key component of this key pair.

**Returns:**
- a reference to the private key.

---

### Additional Sections

#### Class KeyPair

java.lang.Object

- java.security.KeyPair

java.security.KeyPair

**All Implemented Interfaces:** Serializable

```java
public final class
KeyPair

extends
Object

implements
Serializable
```

This class is a simple holder for a key pair (a public key and a
private key). It does not enforce any security, and, when initialized,
should be treated like a PrivateKey.

**Since:** 1.1
**See Also:** PublicKey

,

PrivateKey

,

Serialized Form

public final class

KeyPair

extends

Object

implements

Serializable

This class is a simple holder for a key pair (a public key and a
private key). It does not enforce any security, and, when initialized,
should be treated like a PrivateKey.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyPair

​(

PublicKey

publicKey,

PrivateKey

privateKey)

Constructs a key pair from the given public key and private key.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrivateKey

getPrivate

()

Returns a reference to the private key component of this key pair.

PublicKey

getPublic

()

Returns a reference to the public key component of this key pair.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

KeyPair

​(

PublicKey

publicKey,

PrivateKey

privateKey)

Constructs a key pair from the given public key and private key.

---

#### Constructor Summary

Constructs a key pair from the given public key and private key.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrivateKey

getPrivate

()

Returns a reference to the private key component of this key pair.

PublicKey

getPublic

()

Returns a reference to the public key component of this key pair.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a reference to the private key component of this key pair.

Returns a reference to the public key component of this key pair.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- KeyPair

```java
public KeyPair​(
PublicKey
publicKey,

PrivateKey
privateKey)
```

Constructs a key pair from the given public key and private key.

Note that this constructor only stores references to the public
and private key components in the generated key pair. This is safe,
because

Key

objects are immutable.

**Parameters:** publicKey

- the public key.
**Parameters:** privateKey

- the private key.

============ METHOD DETAIL ==========

- Method Detail

- getPublic

```java
public
PublicKey
getPublic()
```

Returns a reference to the public key component of this key pair.

**Returns:** a reference to the public key.

- getPrivate

```java
public
PrivateKey
getPrivate()
```

Returns a reference to the private key component of this key pair.

**Returns:** a reference to the private key.

Constructor Detail

- KeyPair

```java
public KeyPair​(
PublicKey
publicKey,

PrivateKey
privateKey)
```

Constructs a key pair from the given public key and private key.

Note that this constructor only stores references to the public
and private key components in the generated key pair. This is safe,
because

Key

objects are immutable.

**Parameters:** publicKey

- the public key.
**Parameters:** privateKey

- the private key.

---

#### Constructor Detail

KeyPair

```java
public KeyPair​(
PublicKey
publicKey,

PrivateKey
privateKey)
```

Constructs a key pair from the given public key and private key.

Note that this constructor only stores references to the public
and private key components in the generated key pair. This is safe,
because

Key

objects are immutable.

**Parameters:** publicKey

- the public key.
**Parameters:** privateKey

- the private key.

---

#### KeyPair

public KeyPair​(

PublicKey

publicKey,

PrivateKey

privateKey)

Constructs a key pair from the given public key and private key.

Note that this constructor only stores references to the public
and private key components in the generated key pair. This is safe,
because

Key

objects are immutable.

Note that this constructor only stores references to the public
and private key components in the generated key pair. This is safe,
because

Key

objects are immutable.

Method Detail

- getPublic

```java
public
PublicKey
getPublic()
```

Returns a reference to the public key component of this key pair.

**Returns:** a reference to the public key.

- getPrivate

```java
public
PrivateKey
getPrivate()
```

Returns a reference to the private key component of this key pair.

**Returns:** a reference to the private key.

---

#### Method Detail

getPublic

```java
public
PublicKey
getPublic()
```

Returns a reference to the public key component of this key pair.

**Returns:** a reference to the public key.

---

#### getPublic

public

PublicKey

getPublic()

Returns a reference to the public key component of this key pair.

getPrivate

```java
public
PrivateKey
getPrivate()
```

Returns a reference to the private key component of this key pair.

**Returns:** a reference to the private key.

---

#### getPrivate

public

PrivateKey

getPrivate()

Returns a reference to the private key component of this key pair.

---

