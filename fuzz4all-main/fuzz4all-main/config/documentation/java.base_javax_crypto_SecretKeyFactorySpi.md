# Class SecretKeyFactorySpi

**Source:** `java.base\javax\crypto\SecretKeyFactorySpi.html`

### Class Description

```java
public abstract class
SecretKeyFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

SecretKeyFactory

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a secret-key factory for a particular algorithm.

A provider should document all the key specifications supported by its
secret key factory.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

**Since:** 1.4
**See Also:** SecretKey

,

DESKeySpec

,

DESedeKeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public SecretKeyFactorySpi()

*No description found.*

---

### Method Details

#### protected abstract
SecretKey
engineGenerateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException

Generates a

SecretKey

object from the
provided key specification (key material).

**Parameters:**
- keySpec

- the specification (key material) of the secret key

**Returns:**
- the secret key

**Throws:**
- InvalidKeySpecException

- if the given key specification
is inappropriate for this secret-key factory to produce a secret key.

---

#### protected abstract
KeySpec
engineGetKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException

Returns a specification (key material) of the given key
object in the requested format.

**Parameters:**
- key

- the key
- keySpec

- the requested format in which the key material shall be
returned

**Returns:**
- the underlying key specification (key material) in the
requested format

**Throws:**
- InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key (e.g., the algorithms associated with

key

and

keySpec

do not match, or

key

references a key on a cryptographic hardware device
whereas

keySpec

is the specification of a software-based
key), or the given key cannot be dealt with
(e.g., the given key has an algorithm or format not supported by this
secret-key factory).

---

#### protected abstract
SecretKey
engineTranslateKey​(
SecretKey
key)
throws
InvalidKeyException

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

**Parameters:**
- key

- the key whose provider is unknown or untrusted

**Returns:**
- the translated key

**Throws:**
- InvalidKeyException

- if the given key cannot be processed
by this secret-key factory.

---

### Additional Sections

#### Class SecretKeyFactorySpi

java.lang.Object

- javax.crypto.SecretKeyFactorySpi

javax.crypto.SecretKeyFactorySpi

```java
public abstract class
SecretKeyFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

SecretKeyFactory

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a secret-key factory for a particular algorithm.

A provider should document all the key specifications supported by its
secret key factory.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

**Since:** 1.4
**See Also:** SecretKey

,

DESKeySpec

,

DESedeKeySpec

public abstract class

SecretKeyFactorySpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

SecretKeyFactory

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a secret-key factory for a particular algorithm.

A provider should document all the key specifications supported by its
secret key factory.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

A provider should document all the key specifications supported by its
secret key factory.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SecretKeyFactorySpi

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

SecretKey

engineGenerateSecret

​(

KeySpec

keySpec)

Generates a

SecretKey

object from the
provided key specification (key material).

protected abstract

KeySpec

engineGetKeySpec

​(

SecretKey

key,

Class

<?> keySpec)

Returns a specification (key material) of the given key
object in the requested format.

protected abstract

SecretKey

engineTranslateKey

​(

SecretKey

key)

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

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

SecretKeyFactorySpi

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

SecretKey

engineGenerateSecret

​(

KeySpec

keySpec)

Generates a

SecretKey

object from the
provided key specification (key material).

protected abstract

KeySpec

engineGetKeySpec

​(

SecretKey

key,

Class

<?> keySpec)

Returns a specification (key material) of the given key
object in the requested format.

protected abstract

SecretKey

engineTranslateKey

​(

SecretKey

key)

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

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

Generates a

SecretKey

object from the
provided key specification (key material).

Returns a specification (key material) of the given key
object in the requested format.

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

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

- SecretKeyFactorySpi

```java
public SecretKeyFactorySpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineGenerateSecret

```java
protected abstract
SecretKey
engineGenerateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a

SecretKey

object from the
provided key specification (key material).

**Parameters:** keySpec

- the specification (key material) of the secret key
**Returns:** the secret key
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this secret-key factory to produce a secret key.

- engineGetKeySpec

```java
protected abstract
KeySpec
engineGetKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key
object in the requested format.

**Parameters:** key

- the key
**Parameters:** keySpec

- the requested format in which the key material shall be
returned
**Returns:** the underlying key specification (key material) in the
requested format
**Throws:** InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key (e.g., the algorithms associated with

key

and

keySpec

do not match, or

key

references a key on a cryptographic hardware device
whereas

keySpec

is the specification of a software-based
key), or the given key cannot be dealt with
(e.g., the given key has an algorithm or format not supported by this
secret-key factory).

- engineTranslateKey

```java
protected abstract
SecretKey
engineTranslateKey​(
SecretKey
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted
**Returns:** the translated key
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this secret-key factory.

Constructor Detail

- SecretKeyFactorySpi

```java
public SecretKeyFactorySpi()
```

---

#### Constructor Detail

SecretKeyFactorySpi

```java
public SecretKeyFactorySpi()
```

---

#### SecretKeyFactorySpi

public SecretKeyFactorySpi()

Method Detail

- engineGenerateSecret

```java
protected abstract
SecretKey
engineGenerateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a

SecretKey

object from the
provided key specification (key material).

**Parameters:** keySpec

- the specification (key material) of the secret key
**Returns:** the secret key
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this secret-key factory to produce a secret key.

- engineGetKeySpec

```java
protected abstract
KeySpec
engineGetKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key
object in the requested format.

**Parameters:** key

- the key
**Parameters:** keySpec

- the requested format in which the key material shall be
returned
**Returns:** the underlying key specification (key material) in the
requested format
**Throws:** InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key (e.g., the algorithms associated with

key

and

keySpec

do not match, or

key

references a key on a cryptographic hardware device
whereas

keySpec

is the specification of a software-based
key), or the given key cannot be dealt with
(e.g., the given key has an algorithm or format not supported by this
secret-key factory).

- engineTranslateKey

```java
protected abstract
SecretKey
engineTranslateKey​(
SecretKey
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted
**Returns:** the translated key
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this secret-key factory.

---

#### Method Detail

engineGenerateSecret

```java
protected abstract
SecretKey
engineGenerateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a

SecretKey

object from the
provided key specification (key material).

**Parameters:** keySpec

- the specification (key material) of the secret key
**Returns:** the secret key
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this secret-key factory to produce a secret key.

---

#### engineGenerateSecret

protected abstract

SecretKey

engineGenerateSecret​(

KeySpec

keySpec)
throws

InvalidKeySpecException

Generates a

SecretKey

object from the
provided key specification (key material).

engineGetKeySpec

```java
protected abstract
KeySpec
engineGetKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key
object in the requested format.

**Parameters:** key

- the key
**Parameters:** keySpec

- the requested format in which the key material shall be
returned
**Returns:** the underlying key specification (key material) in the
requested format
**Throws:** InvalidKeySpecException

- if the requested key specification is
inappropriate for the given key (e.g., the algorithms associated with

key

and

keySpec

do not match, or

key

references a key on a cryptographic hardware device
whereas

keySpec

is the specification of a software-based
key), or the given key cannot be dealt with
(e.g., the given key has an algorithm or format not supported by this
secret-key factory).

---

#### engineGetKeySpec

protected abstract

KeySpec

engineGetKeySpec​(

SecretKey

key,

Class

<?> keySpec)
throws

InvalidKeySpecException

Returns a specification (key material) of the given key
object in the requested format.

engineTranslateKey

```java
protected abstract
SecretKey
engineTranslateKey​(
SecretKey
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted
**Returns:** the translated key
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this secret-key factory.

---

#### engineTranslateKey

protected abstract

SecretKey

engineTranslateKey​(

SecretKey

key)
throws

InvalidKeyException

Translates a key object, whose provider may be unknown or
potentially untrusted, into a corresponding key object of this
secret-key factory.

---

