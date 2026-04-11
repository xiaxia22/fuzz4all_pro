# Class SecretKeyFactory

**Source:** `java.base\javax\crypto\SecretKeyFactory.html`

### Class Description

```java
public class
SecretKeyFactory

extends
Object
```

This class represents a factory for secret keys.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.
Secret key factories operate only on secret (symmetric) keys.

Key factories are bi-directional, i.e., they allow to build an opaque
key object from a given key specification (key material), or to retrieve
the underlying key material of a key object in a suitable format.

Application developers should refer to their provider's documentation
to find out which key specifications are supported by the

generateSecret

and

getKeySpec

methods.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

Every implementation of the Java platform is required to support the
following standard

SecretKeyFactory

algorithms:

- DES
- DESede

These algorithms are described in the

SecretKeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** SecretKey

,

DESKeySpec

,

DESedeKeySpec

,

PBEKeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SecretKeyFactory​(
SecretKeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)

Creates a SecretKeyFactory object.

**Parameters:**
- keyFacSpi

- the delegate
- provider

- the provider
- algorithm

- the secret-key algorithm

---

### Method Details

#### public static final
SecretKeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new

SecretKeyFactory

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

SecretKeyFactorySpi

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

#### public static final
SecretKeyFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

SecretKeyFactory

object

**Throws:**
- IllegalArgumentException

- if the

provider

is

null

or empty
- NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

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

#### public static final
SecretKeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the new

SecretKeyFactory

object

**Throws:**
- IllegalArgumentException

- if the

provider

is

null
- NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

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

---

#### public final
Provider
getProvider()

Returns the provider of this

SecretKeyFactory

object.

**Returns:**
- the provider of this

SecretKeyFactory

object

---

#### public final
String
getAlgorithm()

Returns the algorithm name of this

SecretKeyFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

SecretKeyFactory

object.

**Returns:**
- the algorithm name of this

SecretKeyFactory

object.

---

#### public final
SecretKey
generateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException

Generates a

SecretKey

object from the provided key
specification (key material).

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

#### public final
KeySpec
getKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException

Returns a specification (key material) of the given key object
in the requested format.

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

#### public final
SecretKey
translateKey​(
SecretKey
key)
throws
InvalidKeyException

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

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

#### Class SecretKeyFactory

java.lang.Object

- javax.crypto.SecretKeyFactory

javax.crypto.SecretKeyFactory

```java
public class
SecretKeyFactory

extends
Object
```

This class represents a factory for secret keys.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.
Secret key factories operate only on secret (symmetric) keys.

Key factories are bi-directional, i.e., they allow to build an opaque
key object from a given key specification (key material), or to retrieve
the underlying key material of a key object in a suitable format.

Application developers should refer to their provider's documentation
to find out which key specifications are supported by the

generateSecret

and

getKeySpec

methods.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

Every implementation of the Java platform is required to support the
following standard

SecretKeyFactory

algorithms:

- DES
- DESede

These algorithms are described in the

SecretKeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** SecretKey

,

DESKeySpec

,

DESedeKeySpec

,

PBEKeySpec

public class

SecretKeyFactory

extends

Object

This class represents a factory for secret keys.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.
Secret key factories operate only on secret (symmetric) keys.

Key factories are bi-directional, i.e., they allow to build an opaque
key object from a given key specification (key material), or to retrieve
the underlying key material of a key object in a suitable format.

Application developers should refer to their provider's documentation
to find out which key specifications are supported by the

generateSecret

and

getKeySpec

methods.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

Every implementation of the Java platform is required to support the
following standard

SecretKeyFactory

algorithms:

- DES
- DESede

These algorithms are described in the

SecretKeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Key factories are used to convert

keys

(opaque
cryptographic keys of type

Key

) into

key specifications

(transparent representations of the underlying key material), and vice
versa.
Secret key factories operate only on secret (symmetric) keys.

Key factories are bi-directional, i.e., they allow to build an opaque
key object from a given key specification (key material), or to retrieve
the underlying key material of a key object in a suitable format.

Application developers should refer to their provider's documentation
to find out which key specifications are supported by the

generateSecret

and

getKeySpec

methods.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

Every implementation of the Java platform is required to support the
following standard

SecretKeyFactory

algorithms:

- DES
- DESede

These algorithms are described in the

SecretKeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Key factories are bi-directional, i.e., they allow to build an opaque
key object from a given key specification (key material), or to retrieve
the underlying key material of a key object in a suitable format.

Application developers should refer to their provider's documentation
to find out which key specifications are supported by the

generateSecret

and

getKeySpec

methods.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

Every implementation of the Java platform is required to support the
following standard

SecretKeyFactory

algorithms:

- DES
- DESede

These algorithms are described in the

SecretKeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Application developers should refer to their provider's documentation
to find out which key specifications are supported by the

generateSecret

and

getKeySpec

methods.
For example, the DES secret-key factory supplied by the "SunJCE" provider
supports

DESKeySpec

as a transparent representation of DES
keys, and that provider's secret-key factory for Triple DES keys supports

DESedeKeySpec

as a transparent representation of Triple DES
keys.

Every implementation of the Java platform is required to support the
following standard

SecretKeyFactory

algorithms:

- DES
- DESede

These algorithms are described in the

SecretKeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support the
following standard

SecretKeyFactory

algorithms:

- DES
- DESede

These algorithms are described in the

SecretKeyFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

DES

DESede

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SecretKeyFactory

​(

SecretKeyFactorySpi

keyFacSpi,

Provider

provider,

String

algorithm)

Creates a SecretKeyFactory object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SecretKey

generateSecret

​(

KeySpec

keySpec)

Generates a

SecretKey

object from the provided key
specification (key material).

String

getAlgorithm

()

Returns the algorithm name of this

SecretKeyFactory

object.

static

SecretKeyFactory

getInstance

​(

String

algorithm)

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

static

SecretKeyFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

static

SecretKeyFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

KeySpec

getKeySpec

​(

SecretKey

key,

Class

<?> keySpec)

Returns a specification (key material) of the given key object
in the requested format.

Provider

getProvider

()

Returns the provider of this

SecretKeyFactory

object.

SecretKey

translateKey

​(

SecretKey

key)

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

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

SecretKeyFactory

​(

SecretKeyFactorySpi

keyFacSpi,

Provider

provider,

String

algorithm)

Creates a SecretKeyFactory object.

---

#### Constructor Summary

Creates a SecretKeyFactory object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SecretKey

generateSecret

​(

KeySpec

keySpec)

Generates a

SecretKey

object from the provided key
specification (key material).

String

getAlgorithm

()

Returns the algorithm name of this

SecretKeyFactory

object.

static

SecretKeyFactory

getInstance

​(

String

algorithm)

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

static

SecretKeyFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

static

SecretKeyFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

KeySpec

getKeySpec

​(

SecretKey

key,

Class

<?> keySpec)

Returns a specification (key material) of the given key object
in the requested format.

Provider

getProvider

()

Returns the provider of this

SecretKeyFactory

object.

SecretKey

translateKey

​(

SecretKey

key)

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

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

object from the provided key
specification (key material).

Returns the algorithm name of this

SecretKeyFactory

object.

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

Returns a specification (key material) of the given key object
in the requested format.

Returns the provider of this

SecretKeyFactory

object.

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

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

- SecretKeyFactory

```java
protected SecretKeyFactory​(
SecretKeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)
```

Creates a SecretKeyFactory object.

**Parameters:** keyFacSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the secret-key algorithm

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static final
SecretKeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the first
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

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

SecretKeyFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

SecretKeyFactorySpi

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
public static final
SecretKeyFactory
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

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecretKeyFactory

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

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
public static final
SecretKeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

SecretKeyFactory

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

SecretKeyFactory

object.

**Returns:** the provider of this

SecretKeyFactory

object

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

SecretKeyFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

SecretKeyFactory

object.

**Returns:** the algorithm name of this

SecretKeyFactory

object.

- generateSecret

```java
public final
SecretKey
generateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a

SecretKey

object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the secret key
**Returns:** the secret key
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this secret-key factory to produce a secret key.

- getKeySpec

```java
public final
KeySpec
getKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key object
in the requested format.

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

- translateKey

```java
public final
SecretKey
translateKey​(
SecretKey
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted
**Returns:** the translated key
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this secret-key factory.

Constructor Detail

- SecretKeyFactory

```java
protected SecretKeyFactory​(
SecretKeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)
```

Creates a SecretKeyFactory object.

**Parameters:** keyFacSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the secret-key algorithm

---

#### Constructor Detail

SecretKeyFactory

```java
protected SecretKeyFactory​(
SecretKeyFactorySpi
keyFacSpi,

Provider
provider,

String
algorithm)
```

Creates a SecretKeyFactory object.

**Parameters:** keyFacSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the secret-key algorithm

---

#### SecretKeyFactory

protected SecretKeyFactory​(

SecretKeyFactorySpi

keyFacSpi,

Provider

provider,

String

algorithm)

Creates a SecretKeyFactory object.

Method Detail

- getInstance

```java
public static final
SecretKeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the first
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

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

SecretKeyFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

SecretKeyFactorySpi

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
public static final
SecretKeyFactory
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

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecretKeyFactory

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

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
public static final
SecretKeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

SecretKeyFactory

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

SecretKeyFactory

object.

**Returns:** the provider of this

SecretKeyFactory

object

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

SecretKeyFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

SecretKeyFactory

object.

**Returns:** the algorithm name of this

SecretKeyFactory

object.

- generateSecret

```java
public final
SecretKey
generateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a

SecretKey

object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the secret key
**Returns:** the secret key
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this secret-key factory to produce a secret key.

- getKeySpec

```java
public final
KeySpec
getKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key object
in the requested format.

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

- translateKey

```java
public final
SecretKey
translateKey​(
SecretKey
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted
**Returns:** the translated key
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this secret-key factory.

---

#### Method Detail

getInstance

```java
public static final
SecretKeyFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the first
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

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

SecretKeyFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

SecretKeyFactorySpi

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

public static final

SecretKeyFactory

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the first
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
public static final
SecretKeyFactory
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

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecretKeyFactory

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

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

public static final

SecretKeyFactory

getInstance​(

String

algorithm,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified provider
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
public static final
SecretKeyFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested secret-key
algorithm.
See the SecretKeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

SecretKeyFactory

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

SecretKeyFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

SecretKeyFactory

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

SecretKeyFactory

object that converts
secret keys of the specified algorithm.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new SecretKeyFactory object encapsulating the
SecretKeyFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

SecretKeyFactory

object.

**Returns:** the provider of this

SecretKeyFactory

object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

SecretKeyFactory

object.

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

SecretKeyFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

SecretKeyFactory

object.

**Returns:** the algorithm name of this

SecretKeyFactory

object.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the algorithm name of this

SecretKeyFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

SecretKeyFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

SecretKeyFactory

object.

generateSecret

```java
public final
SecretKey
generateSecret​(
KeySpec
keySpec)
throws
InvalidKeySpecException
```

Generates a

SecretKey

object from the provided key
specification (key material).

**Parameters:** keySpec

- the specification (key material) of the secret key
**Returns:** the secret key
**Throws:** InvalidKeySpecException

- if the given key specification
is inappropriate for this secret-key factory to produce a secret key.

---

#### generateSecret

public final

SecretKey

generateSecret​(

KeySpec

keySpec)
throws

InvalidKeySpecException

Generates a

SecretKey

object from the provided key
specification (key material).

getKeySpec

```java
public final
KeySpec
getKeySpec​(
SecretKey
key,

Class
<?> keySpec)
throws
InvalidKeySpecException
```

Returns a specification (key material) of the given key object
in the requested format.

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

#### getKeySpec

public final

KeySpec

getKeySpec​(

SecretKey

key,

Class

<?> keySpec)
throws

InvalidKeySpecException

Returns a specification (key material) of the given key object
in the requested format.

translateKey

```java
public final
SecretKey
translateKey​(
SecretKey
key)
throws
InvalidKeyException
```

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

**Parameters:** key

- the key whose provider is unknown or untrusted
**Returns:** the translated key
**Throws:** InvalidKeyException

- if the given key cannot be processed
by this secret-key factory.

---

#### translateKey

public final

SecretKey

translateKey​(

SecretKey

key)
throws

InvalidKeyException

Translates a key object, whose provider may be unknown or potentially
untrusted, into a corresponding key object of this secret-key factory.

---

