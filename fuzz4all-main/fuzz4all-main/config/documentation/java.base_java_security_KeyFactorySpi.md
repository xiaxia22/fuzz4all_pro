# Class KeyFactorySpi

**Source:** `java.base\java\security\KeyFactorySpi.html`

### Class Description

```java
public abstract class
KeyFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyFactory

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a key factory for a particular algorithm.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.

Key factories are bi-directional. That is, they allow you to build an
opaque key object from a given key specification (key material), or to
retrieve the underlying key material of a key object in a suitable format.

Multiple compatible key specifications may exist for the same key.
For example, a DSA public key may be specified using

DSAPublicKeySpec

or

X509EncodedKeySpec

. A key factory can be used to translate
between compatible key specifications.

A provider should document all the key specifications supported by its
key factory.

**Since:** 1.2
**See Also:** KeyFactory

,

Key

,

PublicKey

,

PrivateKey

,

KeySpec

,

DSAPublicKeySpec

,

X509EncodedKeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyFactorySpi()

*No description found.*

---

### Method Details

#### protected abstract
PublicKey
engineGeneratePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException

Generates a public key object from the provided key
specification (key material).

**Parameters:**
- keySpec

- the specification (key material) of the public key.

**Returns:**
- the public key.

**Throws:**
- InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a public key.

---

#### protected abstract
PrivateKey
engineGeneratePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException

Generates a private key object from the provided key
specification (key material).

**Parameters:**
- keySpec

- the specification (key material) of the private key.

**Returns:**
- the private key.

**Throws:**
- InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a private key.

---

#### protected abstract <T extends
KeySpec
> T engineGetKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException

Returns a specification (key material) of the given key
object.

keySpec

identifies the specification class in which
the key material should be returned. It could, for example, be

DSAPublicKeySpec.class

, to indicate that the
key material should be returned in an instance of the

DSAPublicKeySpec

class.

**Parameters:**
- key

- the key.
- keySpec

- the specification class in which
the key material should be returned.

**Returns:**
- the underlying key specification (key material) in an instance
of the requested specification class.

**Throws:**
- InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key, or the given key cannot be dealt with
(e.g., the given key has an unrecognized format).

**Type Parameters:**
- T

- the type of the key specification to be returned

---

#### protected abstract
Key
engineTranslateKey​(
Key
key)
throws
InvalidKeyException

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

**Parameters:**
- key

- the key whose provider is unknown or untrusted.

**Returns:**
- the translated key.

**Throws:**
- InvalidKeyException

- if the given key cannot be processed
by this key factory.

---

### Additional Sections

#### Class KeyFactorySpi

java.lang.Object

- java.security.KeyFactorySpi

java.security.KeyFactorySpi

```java
public abstract class
KeyFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyFactory

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a key factory for a particular algorithm.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.

Key factories are bi-directional. That is, they allow you to build an
opaque key object from a given key specification (key material), or to
retrieve the underlying key material of a key object in a suitable format.

Multiple compatible key specifications may exist for the same key.
For example, a DSA public key may be specified using

DSAPublicKeySpec

or

X509EncodedKeySpec

. A key factory can be used to translate
between compatible key specifications.

A provider should document all the key specifications supported by its
key factory.

**Since:** 1.2
**See Also:** KeyFactory

,

Key

,

PublicKey

,

PrivateKey

,

KeySpec

,

DSAPublicKeySpec

,

X509EncodedKeySpec

public abstract class

KeyFactorySpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyFactory

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a key factory for a particular algorithm.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.

Key factories are bi-directional. That is, they allow you to build an
opaque key object from a given key specification (key material), or to
retrieve the underlying key material of a key object in a suitable format.

Multiple compatible key specifications may exist for the same key.
For example, a DSA public key may be specified using

DSAPublicKeySpec

or

X509EncodedKeySpec

. A key factory can be used to translate
between compatible key specifications.

A provider should document all the key specifications supported by its
key factory.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.

Key factories are bi-directional. That is, they allow you to build an
opaque key object from a given key specification (key material), or to
retrieve the underlying key material of a key object in a suitable format.

Multiple compatible key specifications may exist for the same key.
For example, a DSA public key may be specified using

DSAPublicKeySpec

or

X509EncodedKeySpec

. A key factory can be used to translate
between compatible key specifications.

A provider should document all the key specifications supported by its
key factory.

Key factories are bi-directional. That is, they allow you to build an
opaque key object from a given key specification (key material), or to
retrieve the underlying key material of a key object in a suitable format.

Multiple compatible key specifications may exist for the same key.
For example, a DSA public key may be specified using

DSAPublicKeySpec

or

X509EncodedKeySpec

. A key factory can be used to translate
between compatible key specifications.

A provider should document all the key specifications supported by its
key factory.

Multiple compatible key specifications may exist for the same key.
For example, a DSA public key may be specified using

DSAPublicKeySpec

or

X509EncodedKeySpec

. A key factory can be used to translate
between compatible key specifications.

A provider should document all the key specifications supported by its
key factory.

A provider should document all the key specifications supported by its
key factory.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyFactorySpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

PrivateKey

engineGeneratePrivate

​(

KeySpec

keySpec)

Generates a private key object from the provided key
specification (key material).

protected abstract

PublicKey

engineGeneratePublic

​(

KeySpec

keySpec)

Generates a public key object from the provided key
specification (key material).

protected abstract <T extends

KeySpec

>

T

engineGetKeySpec

​(

Key

key,

Class

<T> keySpec)

Returns a specification (key material) of the given key
object.

protected abstract

Key

engineTranslateKey

​(

Key

key)

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

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

KeyFactorySpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

PrivateKey

engineGeneratePrivate

​(

KeySpec

keySpec)

Generates a private key object from the provided key
specification (key material).

protected abstract

PublicKey

engineGeneratePublic

​(

KeySpec

keySpec)

Generates a public key object from the provided key
specification (key material).

protected abstract <T extends

KeySpec

>

T

engineGetKeySpec

​(

Key

key,

Class

<T> keySpec)

Returns a specification (key material) of the given key
object.

protected abstract

Key

engineTranslateKey

​(

Key

key)

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

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

Generates a private key object from the provided key
specification (key material).

Generates a public key object from the provided key
specification (key material).

Returns a specification (key material) of the given key
object.

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

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

- KeyFactorySpi

```java
public KeyFactorySpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineGeneratePublic

```java
protected abstract
PublicKey
engineGeneratePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a public key object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the public key.
**Returns:** the public key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a public key.

- engineGeneratePrivate

```java
protected abstract
PrivateKey
engineGeneratePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a private key object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the private key.
**Returns:** the private key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a private key.

- engineGetKeySpec

```java
protected abstract <T extends
KeySpec
> T engineGetKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key
object.

keySpec

identifies the specification class in which
the key material should be returned. It could, for example, be

DSAPublicKeySpec.class

, to indicate that the
key material should be returned in an instance of the

DSAPublicKeySpec

class.

**Type Parameters:** T

- the type of the key specification to be returned
**Parameters:** key

- the key.
**Parameters:** keySpec

- the specification class in which
the key material should be returned.
**Returns:** the underlying key specification (key material) in an instance
of the requested specification class.
**Throws:** InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key, or the given key cannot be dealt with
(e.g., the given key has an unrecognized format).

- engineTranslateKey

```java
protected abstract
Key
engineTranslateKey​(
Key
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

**Parameters:** key

- the key whose provider is unknown or untrusted.
**Returns:** the translated key.
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this key factory.

Constructor Detail

- KeyFactorySpi

```java
public KeyFactorySpi()
```

---

#### Constructor Detail

KeyFactorySpi

```java
public KeyFactorySpi()
```

---

#### KeyFactorySpi

public KeyFactorySpi()

Method Detail

- engineGeneratePublic

```java
protected abstract
PublicKey
engineGeneratePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a public key object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the public key.
**Returns:** the public key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a public key.

- engineGeneratePrivate

```java
protected abstract
PrivateKey
engineGeneratePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a private key object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the private key.
**Returns:** the private key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a private key.

- engineGetKeySpec

```java
protected abstract <T extends
KeySpec
> T engineGetKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key
object.

keySpec

identifies the specification class in which
the key material should be returned. It could, for example, be

DSAPublicKeySpec.class

, to indicate that the
key material should be returned in an instance of the

DSAPublicKeySpec

class.

**Type Parameters:** T

- the type of the key specification to be returned
**Parameters:** key

- the key.
**Parameters:** keySpec

- the specification class in which
the key material should be returned.
**Returns:** the underlying key specification (key material) in an instance
of the requested specification class.
**Throws:** InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key, or the given key cannot be dealt with
(e.g., the given key has an unrecognized format).

- engineTranslateKey

```java
protected abstract
Key
engineTranslateKey​(
Key
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

**Parameters:** key

- the key whose provider is unknown or untrusted.
**Returns:** the translated key.
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this key factory.

---

#### Method Detail

engineGeneratePublic

```java
protected abstract
PublicKey
engineGeneratePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a public key object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the public key.
**Returns:** the public key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a public key.

---

#### engineGeneratePublic

protected abstract

PublicKey

engineGeneratePublic​(

KeySpec

keySpec)
throws

InvalidKeySpecException

Generates a public key object from the provided key
specification (key material).

engineGeneratePrivate

```java
protected abstract
PrivateKey
engineGeneratePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a private key object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the private key.
**Returns:** the private key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a private key.

---

#### engineGeneratePrivate

protected abstract

PrivateKey

engineGeneratePrivate​(

KeySpec

keySpec)
throws

InvalidKeySpecException

Generates a private key object from the provided key
specification (key material).

engineGetKeySpec

```java
protected abstract <T extends
KeySpec
> T engineGetKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key
object.

keySpec

identifies the specification class in which
the key material should be returned. It could, for example, be

DSAPublicKeySpec.class

, to indicate that the
key material should be returned in an instance of the

DSAPublicKeySpec

class.

**Type Parameters:** T

- the type of the key specification to be returned
**Parameters:** key

- the key.
**Parameters:** keySpec

- the specification class in which
the key material should be returned.
**Returns:** the underlying key specification (key material) in an instance
of the requested specification class.
**Throws:** InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key, or the given key cannot be dealt with
(e.g., the given key has an unrecognized format).

---

#### engineGetKeySpec

protected abstract <T extends

KeySpec

> T engineGetKeySpec​(

Key

key,

Class

<T> keySpec)
throws

InvalidKeySpecException

Returns a specification (key material) of the given key
object.

keySpec

identifies the specification class in which
the key material should be returned. It could, for example, be

DSAPublicKeySpec.class

, to indicate that the
key material should be returned in an instance of the

DSAPublicKeySpec

class.

engineTranslateKey

```java
protected abstract
Key
engineTranslateKey​(
Key
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

**Parameters:** key

- the key whose provider is unknown or untrusted.
**Returns:** the translated key.
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this key factory.

---

#### engineTranslateKey

protected abstract

Key

engineTranslateKey​(

Key

key)
throws

InvalidKeyException

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this key
factory.

---

