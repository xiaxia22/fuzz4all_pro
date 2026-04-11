# Class KeyFactory

**Source:** `java.base\java\security\KeyFactory.html`

### Class Description

```java
public class
KeyFactory

extends
Object
```

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

The following is an example of how to use a key factory in order to
instantiate a DSA public key from its encoding.
Assume Alice has received a digital signature from Bob.
Bob also sent her his public key (in encoded format) to verify
his signature. Alice then performs the following actions:

```java
X509EncodedKeySpec bobPubKeySpec = new X509EncodedKeySpec(bobEncodedPubKey);
KeyFactory keyFactory = KeyFactory.getInstance("DSA");
PublicKey bobPubKey = keyFactory.generatePublic(bobPubKeySpec);
Signature sig = Signature.getInstance("DSA");
sig.initVerify(bobPubKey);
sig.update(data);
sig.verify(signature);
```

Every implementation of the Java platform is required to support the
following standard

KeyFactory

algorithms:

- DiffieHellman
- DSA
- RSA

These algorithms are described in the

KeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.2
**See Also:** Key

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

#### protected KeyFactory​(
KeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)

Creates a KeyFactory object.

**Parameters:**
- keyFacSpi

- the delegate
- provider

- the provider
- algorithm

- the name of the algorithm
to associate with this

KeyFactory

---

### Method Details

#### public static
KeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new

KeyFactory

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

KeyFactorySpi

implementation for the
specified algorithm
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

**Implementation Note:**
- The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.

---

#### public static
KeyFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

KeyFactory

object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty
- NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not
available from the specified provider
- NoSuchProviderException

- if the specified provider is not
registered in the security provider list
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

---

#### public static
KeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the new

KeyFactory

object

**Throws:**
- IllegalArgumentException

- if the specified provider is

null
- NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

**Since:**
- 1.4

---

#### public final
Provider
getProvider()

Returns the provider of this key factory object.

**Returns:**
- the provider of this key factory object

---

#### public final
String
getAlgorithm()

Gets the name of the algorithm
associated with this

KeyFactory

.

**Returns:**
- the name of the algorithm associated with this

KeyFactory

---

#### public final
PublicKey
generatePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException

Generates a public key object from the provided key specification
(key material).

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

#### public final
PrivateKey
generatePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException

Generates a private key object from the provided key specification
(key material).

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

#### public final <T extends
KeySpec
> T getKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException

Returns a specification (key material) of the given key object.

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
inappropriate for the given key, or the given key cannot be processed
(e.g., the given key has an unrecognized algorithm or format).

**Type Parameters:**
- T

- the type of the key specification to be returned

---

#### public final
Key
translateKey​(
Key
key)
throws
InvalidKeyException

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

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

#### Class KeyFactory

java.lang.Object

- java.security.KeyFactory

java.security.KeyFactory

```java
public class
KeyFactory

extends
Object
```

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

The following is an example of how to use a key factory in order to
instantiate a DSA public key from its encoding.
Assume Alice has received a digital signature from Bob.
Bob also sent her his public key (in encoded format) to verify
his signature. Alice then performs the following actions:

```java
X509EncodedKeySpec bobPubKeySpec = new X509EncodedKeySpec(bobEncodedPubKey);
KeyFactory keyFactory = KeyFactory.getInstance("DSA");
PublicKey bobPubKey = keyFactory.generatePublic(bobPubKeySpec);
Signature sig = Signature.getInstance("DSA");
sig.initVerify(bobPubKey);
sig.update(data);
sig.verify(signature);
```

Every implementation of the Java platform is required to support the
following standard

KeyFactory

algorithms:

- DiffieHellman
- DSA
- RSA

These algorithms are described in the

KeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.2
**See Also:** Key

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

public class

KeyFactory

extends

Object

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

The following is an example of how to use a key factory in order to
instantiate a DSA public key from its encoding.
Assume Alice has received a digital signature from Bob.
Bob also sent her his public key (in encoded format) to verify
his signature. Alice then performs the following actions:

```java
X509EncodedKeySpec bobPubKeySpec = new X509EncodedKeySpec(bobEncodedPubKey);
KeyFactory keyFactory = KeyFactory.getInstance("DSA");
PublicKey bobPubKey = keyFactory.generatePublic(bobPubKeySpec);
Signature sig = Signature.getInstance("DSA");
sig.initVerify(bobPubKey);
sig.update(data);
sig.verify(signature);
```

Every implementation of the Java platform is required to support the
following standard

KeyFactory

algorithms:

- DiffieHellman
- DSA
- RSA

These algorithms are described in the

KeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

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

The following is an example of how to use a key factory in order to
instantiate a DSA public key from its encoding.
Assume Alice has received a digital signature from Bob.
Bob also sent her his public key (in encoded format) to verify
his signature. Alice then performs the following actions:

```java
X509EncodedKeySpec bobPubKeySpec = new X509EncodedKeySpec(bobEncodedPubKey);
KeyFactory keyFactory = KeyFactory.getInstance("DSA");
PublicKey bobPubKey = keyFactory.generatePublic(bobPubKeySpec);
Signature sig = Signature.getInstance("DSA");
sig.initVerify(bobPubKey);
sig.update(data);
sig.verify(signature);
```

Every implementation of the Java platform is required to support the
following standard

KeyFactory

algorithms:

- DiffieHellman
- DSA
- RSA

These algorithms are described in the

KeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Multiple compatible key specifications may exist for the same key.
For example, a DSA public key may be specified using

DSAPublicKeySpec

or

X509EncodedKeySpec

. A key factory can be used to translate
between compatible key specifications.

The following is an example of how to use a key factory in order to
instantiate a DSA public key from its encoding.
Assume Alice has received a digital signature from Bob.
Bob also sent her his public key (in encoded format) to verify
his signature. Alice then performs the following actions:

```java
X509EncodedKeySpec bobPubKeySpec = new X509EncodedKeySpec(bobEncodedPubKey);
KeyFactory keyFactory = KeyFactory.getInstance("DSA");
PublicKey bobPubKey = keyFactory.generatePublic(bobPubKeySpec);
Signature sig = Signature.getInstance("DSA");
sig.initVerify(bobPubKey);
sig.update(data);
sig.verify(signature);
```

Every implementation of the Java platform is required to support the
following standard

KeyFactory

algorithms:

- DiffieHellman
- DSA
- RSA

These algorithms are described in the

KeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

The following is an example of how to use a key factory in order to
instantiate a DSA public key from its encoding.
Assume Alice has received a digital signature from Bob.
Bob also sent her his public key (in encoded format) to verify
his signature. Alice then performs the following actions:

```java
X509EncodedKeySpec bobPubKeySpec = new X509EncodedKeySpec(bobEncodedPubKey);
KeyFactory keyFactory = KeyFactory.getInstance("DSA");
PublicKey bobPubKey = keyFactory.generatePublic(bobPubKeySpec);
Signature sig = Signature.getInstance("DSA");
sig.initVerify(bobPubKey);
sig.update(data);
sig.verify(signature);
```

Every implementation of the Java platform is required to support the
following standard

KeyFactory

algorithms:

- DiffieHellman
- DSA
- RSA

These algorithms are described in the

KeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

X509EncodedKeySpec bobPubKeySpec = new X509EncodedKeySpec(bobEncodedPubKey);
KeyFactory keyFactory = KeyFactory.getInstance("DSA");
PublicKey bobPubKey = keyFactory.generatePublic(bobPubKeySpec);
Signature sig = Signature.getInstance("DSA");
sig.initVerify(bobPubKey);
sig.update(data);
sig.verify(signature);

Every implementation of the Java platform is required to support the
following standard

KeyFactory

algorithms:

- DiffieHellman
- DSA
- RSA

These algorithms are described in the

KeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

DiffieHellman

DSA

RSA

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

KeyFactory

​(

KeyFactorySpi

keyFacSpi,

Provider

provider,

String

algorithm)

Creates a KeyFactory object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrivateKey

generatePrivate

​(

KeySpec

keySpec)

Generates a private key object from the provided key specification
(key material).

PublicKey

generatePublic

​(

KeySpec

keySpec)

Generates a public key object from the provided key specification
(key material).

String

getAlgorithm

()

Gets the name of the algorithm
associated with this

KeyFactory

.

static

KeyFactory

getInstance

​(

String

algorithm)

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

static

KeyFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

static

KeyFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

<T extends

KeySpec

>

T

getKeySpec

​(

Key

key,

Class

<T> keySpec)

Returns a specification (key material) of the given key object.

Provider

getProvider

()

Returns the provider of this key factory object.

Key

translateKey

​(

Key

key)

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

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

Modifier

Constructor

Description

protected

KeyFactory

​(

KeyFactorySpi

keyFacSpi,

Provider

provider,

String

algorithm)

Creates a KeyFactory object.

---

#### Constructor Summary

Creates a KeyFactory object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrivateKey

generatePrivate

​(

KeySpec

keySpec)

Generates a private key object from the provided key specification
(key material).

PublicKey

generatePublic

​(

KeySpec

keySpec)

Generates a public key object from the provided key specification
(key material).

String

getAlgorithm

()

Gets the name of the algorithm
associated with this

KeyFactory

.

static

KeyFactory

getInstance

​(

String

algorithm)

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

static

KeyFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

static

KeyFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

<T extends

KeySpec

>

T

getKeySpec

​(

Key

key,

Class

<T> keySpec)

Returns a specification (key material) of the given key object.

Provider

getProvider

()

Returns the provider of this key factory object.

Key

translateKey

​(

Key

key)

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

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

Generates a private key object from the provided key specification
(key material).

Generates a public key object from the provided key specification
(key material).

Gets the name of the algorithm
associated with this

KeyFactory

.

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

Returns a specification (key material) of the given key object.

Returns the provider of this key factory object.

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

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

- KeyFactory

```java
protected KeyFactory​(
KeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyFactory object.

**Parameters:** keyFacSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the name of the algorithm
to associate with this

KeyFactory

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyFactorySpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not
available from the specified provider
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyFactory

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 1.4
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this key factory object.

**Returns:** the provider of this key factory object

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Gets the name of the algorithm
associated with this

KeyFactory

.

**Returns:** the name of the algorithm associated with this

KeyFactory

- generatePublic

```java
public final
PublicKey
generatePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a public key object from the provided key specification
(key material).

**Parameters:** keySpec

- the specification (key material) of the public key.
**Returns:** the public key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a public key.

- generatePrivate

```java
public final
PrivateKey
generatePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a private key object from the provided key specification
(key material).

**Parameters:** keySpec

- the specification (key material) of the private key.
**Returns:** the private key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a private key.

- getKeySpec

```java
public final <T extends
KeySpec
> T getKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key object.

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
inappropriate for the given key, or the given key cannot be processed
(e.g., the given key has an unrecognized algorithm or format).

- translateKey

```java
public final
Key
translateKey​(
Key
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted.
**Returns:** the translated key.
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this key factory.

Constructor Detail

- KeyFactory

```java
protected KeyFactory​(
KeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyFactory object.

**Parameters:** keyFacSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the name of the algorithm
to associate with this

KeyFactory

---

#### Constructor Detail

KeyFactory

```java
protected KeyFactory​(
KeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyFactory object.

**Parameters:** keyFacSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the name of the algorithm
to associate with this

KeyFactory

---

#### KeyFactory

protected KeyFactory​(

KeyFactorySpi

keyFacSpi,

Provider

provider,

String

algorithm)

Creates a KeyFactory object.

Method Detail

- getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyFactorySpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not
available from the specified provider
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyFactory

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 1.4
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this key factory object.

**Returns:** the provider of this key factory object

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Gets the name of the algorithm
associated with this

KeyFactory

.

**Returns:** the name of the algorithm associated with this

KeyFactory

- generatePublic

```java
public final
PublicKey
generatePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a public key object from the provided key specification
(key material).

**Parameters:** keySpec

- the specification (key material) of the public key.
**Returns:** the public key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a public key.

- generatePrivate

```java
public final
PrivateKey
generatePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a private key object from the provided key specification
(key material).

**Parameters:** keySpec

- the specification (key material) of the private key.
**Returns:** the private key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a private key.

- getKeySpec

```java
public final <T extends
KeySpec
> T getKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key object.

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
inappropriate for the given key, or the given key cannot be processed
(e.g., the given key has an unrecognized algorithm or format).

- translateKey

```java
public final
Key
translateKey​(
Key
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted.
**Returns:** the translated key.
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this key factory.

---

#### Method Detail

getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyFactorySpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static

KeyFactory

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not
available from the specified provider
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static

KeyFactory

getInstance​(

String

algorithm,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

getInstance

```java
public static
KeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the requested key algorithm.
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyFactory

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 1.4
**See Also:** Provider

---

#### getInstance

public static

KeyFactory

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a KeyFactory object that converts
public/private keys of the specified algorithm.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new KeyFactory object encapsulating the
KeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this key factory object.

**Returns:** the provider of this key factory object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this key factory object.

getAlgorithm

```java
public final
String
getAlgorithm()
```

Gets the name of the algorithm
associated with this

KeyFactory

.

**Returns:** the name of the algorithm associated with this

KeyFactory

---

#### getAlgorithm

public final

String

getAlgorithm()

Gets the name of the algorithm
associated with this

KeyFactory

.

generatePublic

```java
public final
PublicKey
generatePublic​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a public key object from the provided key specification
(key material).

**Parameters:** keySpec

- the specification (key material) of the public key.
**Returns:** the public key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a public key.

---

#### generatePublic

public final

PublicKey

generatePublic​(

KeySpec

keySpec)
throws

InvalidKeySpecException

Generates a public key object from the provided key specification
(key material).

generatePrivate

```java
public final
PrivateKey
generatePrivate​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a private key object from the provided key specification
(key material).

**Parameters:** keySpec

- the specification (key material) of the private key.
**Returns:** the private key.
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this key factory to produce a private key.

---

#### generatePrivate

public final

PrivateKey

generatePrivate​(

KeySpec

keySpec)
throws

InvalidKeySpecException

Generates a private key object from the provided key specification
(key material).

getKeySpec

```java
public final <T extends
KeySpec
> T getKeySpec​(
Key
key,

Class
<T> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key object.

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
inappropriate for the given key, or the given key cannot be processed
(e.g., the given key has an unrecognized algorithm or format).

---

#### getKeySpec

public final <T extends

KeySpec

> T getKeySpec​(

Key

key,

Class

<T> keySpec)
throws

InvalidKeySpecException

Returns a specification (key material) of the given key object.

keySpec

identifies the specification class in which
the key material should be returned. It could, for example, be

DSAPublicKeySpec.class

, to indicate that the
key material should be returned in an instance of the

DSAPublicKeySpec

class.

translateKey

```java
public final
Key
translateKey​(
Key
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted.
**Returns:** the translated key.
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this key factory.

---

#### translateKey

public final

Key

translateKey​(

Key

key)
throws

InvalidKeyException

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this key factory.

---

