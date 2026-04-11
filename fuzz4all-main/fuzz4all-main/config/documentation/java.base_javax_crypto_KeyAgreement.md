# Class KeyAgreement

**Source:** `java.base\javax\crypto\KeyAgreement.html`

### Class Description

```java
public class
KeyAgreement

extends
Object
```

This class provides the functionality of a key agreement (or key
exchange) protocol.

The keys involved in establishing a shared secret are created by one of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol.

For each of the correspondents in the key exchange,

doPhase

needs to be called. For example, if this key exchange is with one other
party,

doPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If this key exchange is
with two other parties,

doPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

Every implementation of the Java platform is required to support the
following standard

KeyAgreement

algorithm:

- DiffieHellman

This algorithm is described in the

KeyAgreement section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** KeyGenerator

,

SecretKey

---

### Field Details

*No entries found.*

### Constructor Details

#### protected KeyAgreement​(
KeyAgreementSpi
keyAgreeSpi,

Provider
provider,

String
algorithm)

Creates a KeyAgreement object.

**Parameters:**
- keyAgreeSpi

- the delegate
- provider

- the provider
- algorithm

- the algorithm

---

### Method Details

#### public final
String
getAlgorithm()

Returns the algorithm name of this

KeyAgreement

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyAgreement

object.

**Returns:**
- the algorithm name of this

KeyAgreement

object.

---

#### public static final
KeyAgreement
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new

KeyAgreement

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

KeyAgreementSpi

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
KeyAgreement
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

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

KeyAgreement

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

KeyAgreementSpi

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
KeyAgreement
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the new

KeyAgreement

object

**Throws:**
- IllegalArgumentException

- if the

provider

is

null
- NoSuchAlgorithmException

- if a

KeyAgreementSpi

implementation for the specified algorithm is not available
from the specified Provider object
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

KeyAgreement

object.

**Returns:**
- the provider of this

KeyAgreement

object

---

#### public final void init​(
Key
key)
throws
InvalidKeyException

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:**
- key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.

**Throws:**
- InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

---

#### public final void init​(
Key
key,

SecureRandom
random)
throws
InvalidKeyException

Initializes this key agreement with the given key and source of
randomness. The given key is required to contain all the algorithm
parameters required for this key agreement.

If the key agreement algorithm requires random bytes, it gets them
from the given source of randomness,

random

.
However, if the underlying
algorithm implementation does not require any random bytes,

random

is ignored.

**Parameters:**
- key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
- random

- the source of randomness

**Throws:**
- InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

---

#### public final void init​(
Key
key,

AlgorithmParameterSpec
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException

Initializes this key agreement with the given key and set of
algorithm parameters.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:**
- key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
- params

- the key agreement parameters

**Throws:**
- InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
- InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

---

#### public final void init​(
Key
key,

AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

**Parameters:**
- key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
- params

- the key agreement parameters
- random

- the source of randomness

**Throws:**
- InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
- InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

---

#### public final
Key
doPhase​(
Key
key,
boolean lastPhase)
throws
InvalidKeyException
,

IllegalStateException

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

**Parameters:**
- key

- the key for this phase. For example, in the case of
Diffie-Hellman between 2 parties, this would be the other party's
Diffie-Hellman public key.
- lastPhase

- flag which indicates whether or not this is the last
phase of this key agreement.

**Returns:**
- the (intermediate) key resulting from this phase, or null
if this phase does not yield a key

**Throws:**
- InvalidKeyException

- if the given key is inappropriate for
this phase.
- IllegalStateException

- if this key agreement has not been
initialized.

---

#### public final byte[] generateSecret()
throws
IllegalStateException

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Returns:**
- the new buffer with the shared secret

**Throws:**
- IllegalStateException

- if this key agreement has not been
completed yet

---

#### public final int generateSecret​(byte[] sharedSecret,
int offset)
throws
IllegalStateException
,

ShortBufferException

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

If the

sharedSecret

buffer is too small to hold the
result, a

ShortBufferException

is thrown.
In this case, this call should be repeated with a larger output buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:**
- sharedSecret

- the buffer for the shared secret
- offset

- the offset in

sharedSecret

where the
shared secret will be stored

**Returns:**
- the number of bytes placed into

sharedSecret

**Throws:**
- IllegalStateException

- if this key agreement has not been
completed yet
- ShortBufferException

- if the given output buffer is too small
to hold the secret

---

#### public final
SecretKey
generateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:**
- algorithm

- the requested secret-key algorithm

**Returns:**
- the shared secret key

**Throws:**
- IllegalStateException

- if this key agreement has not been
completed yet
- NoSuchAlgorithmException

- if the specified secret-key
algorithm is not available
- InvalidKeyException

- if the shared secret-key material cannot
be used to generate a secret key of the specified algorithm (e.g.,
the key material is too short)

---

### Additional Sections

#### Class KeyAgreement

java.lang.Object

- javax.crypto.KeyAgreement

javax.crypto.KeyAgreement

```java
public class
KeyAgreement

extends
Object
```

This class provides the functionality of a key agreement (or key
exchange) protocol.

The keys involved in establishing a shared secret are created by one of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol.

For each of the correspondents in the key exchange,

doPhase

needs to be called. For example, if this key exchange is with one other
party,

doPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If this key exchange is
with two other parties,

doPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

Every implementation of the Java platform is required to support the
following standard

KeyAgreement

algorithm:

- DiffieHellman

This algorithm is described in the

KeyAgreement section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** KeyGenerator

,

SecretKey

public class

KeyAgreement

extends

Object

This class provides the functionality of a key agreement (or key
exchange) protocol.

The keys involved in establishing a shared secret are created by one of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol.

For each of the correspondents in the key exchange,

doPhase

needs to be called. For example, if this key exchange is with one other
party,

doPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If this key exchange is
with two other parties,

doPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

Every implementation of the Java platform is required to support the
following standard

KeyAgreement

algorithm:

- DiffieHellman

This algorithm is described in the

KeyAgreement section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

The keys involved in establishing a shared secret are created by one of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol.

For each of the correspondents in the key exchange,

doPhase

needs to be called. For example, if this key exchange is with one other
party,

doPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If this key exchange is
with two other parties,

doPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

Every implementation of the Java platform is required to support the
following standard

KeyAgreement

algorithm:

- DiffieHellman

This algorithm is described in the

KeyAgreement section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

For each of the correspondents in the key exchange,

doPhase

needs to be called. For example, if this key exchange is with one other
party,

doPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If this key exchange is
with two other parties,

doPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

Every implementation of the Java platform is required to support the
following standard

KeyAgreement

algorithm:

- DiffieHellman

This algorithm is described in the

KeyAgreement section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support the
following standard

KeyAgreement

algorithm:

- DiffieHellman

This algorithm is described in the

KeyAgreement section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

DiffieHellman

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

KeyAgreement

​(

KeyAgreementSpi

keyAgreeSpi,

Provider

provider,

String

algorithm)

Creates a KeyAgreement object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Key

doPhase

​(

Key

key,
boolean lastPhase)

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

byte[]

generateSecret

()

Generates the shared secret and returns it in a new buffer.

int

generateSecret

​(byte[] sharedSecret,
int offset)

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

SecretKey

generateSecret

​(

String

algorithm)

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

String

getAlgorithm

()

Returns the algorithm name of this

KeyAgreement

object.

static

KeyAgreement

getInstance

​(

String

algorithm)

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

static

KeyAgreement

getInstance

​(

String

algorithm,

String

provider)

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

static

KeyAgreement

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

Provider

getProvider

()

Returns the provider of this

KeyAgreement

object.

void

init

​(

Key

key)

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

void

init

​(

Key

key,

SecureRandom

random)

Initializes this key agreement with the given key and source of
randomness.

void

init

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this key agreement with the given key and set of
algorithm parameters.

void

init

​(

Key

key,

AlgorithmParameterSpec

params,

SecureRandom

random)

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

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

KeyAgreement

​(

KeyAgreementSpi

keyAgreeSpi,

Provider

provider,

String

algorithm)

Creates a KeyAgreement object.

---

#### Constructor Summary

Creates a KeyAgreement object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Key

doPhase

​(

Key

key,
boolean lastPhase)

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

byte[]

generateSecret

()

Generates the shared secret and returns it in a new buffer.

int

generateSecret

​(byte[] sharedSecret,
int offset)

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

SecretKey

generateSecret

​(

String

algorithm)

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

String

getAlgorithm

()

Returns the algorithm name of this

KeyAgreement

object.

static

KeyAgreement

getInstance

​(

String

algorithm)

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

static

KeyAgreement

getInstance

​(

String

algorithm,

String

provider)

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

static

KeyAgreement

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

Provider

getProvider

()

Returns the provider of this

KeyAgreement

object.

void

init

​(

Key

key)

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

void

init

​(

Key

key,

SecureRandom

random)

Initializes this key agreement with the given key and source of
randomness.

void

init

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this key agreement with the given key and set of
algorithm parameters.

void

init

​(

Key

key,

AlgorithmParameterSpec

params,

SecureRandom

random)

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

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

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

Generates the shared secret and returns it in a new buffer.

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

Returns the algorithm name of this

KeyAgreement

object.

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

Returns the provider of this

KeyAgreement

object.

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

Initializes this key agreement with the given key and source of
randomness.

Initializes this key agreement with the given key and set of
algorithm parameters.

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

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

- KeyAgreement

```java
protected KeyAgreement​(
KeyAgreementSpi
keyAgreeSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyAgreement object.

**Parameters:** keyAgreeSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

============ METHOD DETAIL ==========

- Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyAgreement

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyAgreement

object.

**Returns:** the algorithm name of this

KeyAgreement

object.

- getInstance

```java
public static final
KeyAgreement
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the first
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

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyAgreement

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyAgreementSpi

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
KeyAgreement
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

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyAgreement

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyAgreementSpi

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
KeyAgreement
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyAgreement

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyAgreementSpi

implementation for the specified algorithm is not available
from the specified Provider object
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

KeyAgreement

object.

**Returns:** the provider of this

KeyAgreement

object

- init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
```

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

- init

```java
public final void init​(
Key
key,

SecureRandom
random)
throws
InvalidKeyException
```

Initializes this key agreement with the given key and source of
randomness. The given key is required to contain all the algorithm
parameters required for this key agreement.

If the key agreement algorithm requires random bytes, it gets them
from the given source of randomness,

random

.
However, if the underlying
algorithm implementation does not require any random bytes,

random

is ignored.

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

- init

```java
public final void init​(
Key
key,

AlgorithmParameterSpec
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
```

Initializes this key agreement with the given key and set of
algorithm parameters.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** params

- the key agreement parameters
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

- init

```java
public final void init​(
Key
key,

AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
```

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** params

- the key agreement parameters
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

- doPhase

```java
public final
Key
doPhase​(
Key
key,
boolean lastPhase)
throws
InvalidKeyException
,

IllegalStateException
```

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

**Parameters:** key

- the key for this phase. For example, in the case of
Diffie-Hellman between 2 parties, this would be the other party's
Diffie-Hellman public key.
**Parameters:** lastPhase

- flag which indicates whether or not this is the last
phase of this key agreement.
**Returns:** the (intermediate) key resulting from this phase, or null
if this phase does not yield a key
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this phase.
**Throws:** IllegalStateException

- if this key agreement has not been
initialized.

- generateSecret

```java
public final byte[] generateSecret()
throws
IllegalStateException
```

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Returns:** the new buffer with the shared secret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet

- generateSecret

```java
public final int generateSecret​(byte[] sharedSecret,
int offset)
throws
IllegalStateException
,

ShortBufferException
```

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

If the

sharedSecret

buffer is too small to hold the
result, a

ShortBufferException

is thrown.
In this case, this call should be repeated with a larger output buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** sharedSecret

- the buffer for the shared secret
**Parameters:** offset

- the offset in

sharedSecret

where the
shared secret will be stored
**Returns:** the number of bytes placed into

sharedSecret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the secret

- generateSecret

```java
public final
SecretKey
generateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** algorithm

- the requested secret-key algorithm
**Returns:** the shared secret key
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** NoSuchAlgorithmException

- if the specified secret-key
algorithm is not available
**Throws:** InvalidKeyException

- if the shared secret-key material cannot
be used to generate a secret key of the specified algorithm (e.g.,
the key material is too short)

Constructor Detail

- KeyAgreement

```java
protected KeyAgreement​(
KeyAgreementSpi
keyAgreeSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyAgreement object.

**Parameters:** keyAgreeSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Constructor Detail

KeyAgreement

```java
protected KeyAgreement​(
KeyAgreementSpi
keyAgreeSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyAgreement object.

**Parameters:** keyAgreeSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### KeyAgreement

protected KeyAgreement​(

KeyAgreementSpi

keyAgreeSpi,

Provider

provider,

String

algorithm)

Creates a KeyAgreement object.

Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyAgreement

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyAgreement

object.

**Returns:** the algorithm name of this

KeyAgreement

object.

- getInstance

```java
public static final
KeyAgreement
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the first
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

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyAgreement

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyAgreementSpi

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
KeyAgreement
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

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyAgreement

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyAgreementSpi

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
KeyAgreement
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyAgreement

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyAgreementSpi

implementation for the specified algorithm is not available
from the specified Provider object
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

KeyAgreement

object.

**Returns:** the provider of this

KeyAgreement

object

- init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
```

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

- init

```java
public final void init​(
Key
key,

SecureRandom
random)
throws
InvalidKeyException
```

Initializes this key agreement with the given key and source of
randomness. The given key is required to contain all the algorithm
parameters required for this key agreement.

If the key agreement algorithm requires random bytes, it gets them
from the given source of randomness,

random

.
However, if the underlying
algorithm implementation does not require any random bytes,

random

is ignored.

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

- init

```java
public final void init​(
Key
key,

AlgorithmParameterSpec
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
```

Initializes this key agreement with the given key and set of
algorithm parameters.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** params

- the key agreement parameters
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

- init

```java
public final void init​(
Key
key,

AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
```

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** params

- the key agreement parameters
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

- doPhase

```java
public final
Key
doPhase​(
Key
key,
boolean lastPhase)
throws
InvalidKeyException
,

IllegalStateException
```

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

**Parameters:** key

- the key for this phase. For example, in the case of
Diffie-Hellman between 2 parties, this would be the other party's
Diffie-Hellman public key.
**Parameters:** lastPhase

- flag which indicates whether or not this is the last
phase of this key agreement.
**Returns:** the (intermediate) key resulting from this phase, or null
if this phase does not yield a key
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this phase.
**Throws:** IllegalStateException

- if this key agreement has not been
initialized.

- generateSecret

```java
public final byte[] generateSecret()
throws
IllegalStateException
```

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Returns:** the new buffer with the shared secret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet

- generateSecret

```java
public final int generateSecret​(byte[] sharedSecret,
int offset)
throws
IllegalStateException
,

ShortBufferException
```

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

If the

sharedSecret

buffer is too small to hold the
result, a

ShortBufferException

is thrown.
In this case, this call should be repeated with a larger output buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** sharedSecret

- the buffer for the shared secret
**Parameters:** offset

- the offset in

sharedSecret

where the
shared secret will be stored
**Returns:** the number of bytes placed into

sharedSecret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the secret

- generateSecret

```java
public final
SecretKey
generateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** algorithm

- the requested secret-key algorithm
**Returns:** the shared secret key
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** NoSuchAlgorithmException

- if the specified secret-key
algorithm is not available
**Throws:** InvalidKeyException

- if the shared secret-key material cannot
be used to generate a secret key of the specified algorithm (e.g.,
the key material is too short)

---

#### Method Detail

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyAgreement

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyAgreement

object.

**Returns:** the algorithm name of this

KeyAgreement

object.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the algorithm name of this

KeyAgreement

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyAgreement

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyAgreement

object.

getInstance

```java
public static final
KeyAgreement
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the first
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

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyAgreement

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyAgreementSpi

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

KeyAgreement

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the first
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
KeyAgreement
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

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyAgreement

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyAgreementSpi

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

KeyAgreement

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

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified provider
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
KeyAgreement
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested key agreement
algorithm.
See the KeyAgreement section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyAgreement

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyAgreementSpi

implementation for the specified algorithm is not available
from the specified Provider object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

KeyAgreement

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

KeyAgreement

object that implements the
specified key agreement algorithm.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new KeyAgreement object encapsulating the
KeyAgreementSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyAgreement

object.

**Returns:** the provider of this

KeyAgreement

object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

KeyAgreement

object.

init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
```

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

---

#### init

public final void init​(

Key

key)
throws

InvalidKeyException

Initializes this key agreement with the given key, which is required to
contain all the algorithm parameters required for this key agreement.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

init

```java
public final void init​(
Key
key,

SecureRandom
random)
throws
InvalidKeyException
```

Initializes this key agreement with the given key and source of
randomness. The given key is required to contain all the algorithm
parameters required for this key agreement.

If the key agreement algorithm requires random bytes, it gets them
from the given source of randomness,

random

.
However, if the underlying
algorithm implementation does not require any random bytes,

random

is ignored.

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.

---

#### init

public final void init​(

Key

key,

SecureRandom

random)
throws

InvalidKeyException

Initializes this key agreement with the given key and source of
randomness. The given key is required to contain all the algorithm
parameters required for this key agreement.

If the key agreement algorithm requires random bytes, it gets them
from the given source of randomness,

random

.
However, if the underlying
algorithm implementation does not require any random bytes,

random

is ignored.

If the key agreement algorithm requires random bytes, it gets them
from the given source of randomness,

random

.
However, if the underlying
algorithm implementation does not require any random bytes,

random

is ignored.

init

```java
public final void init​(
Key
key,

AlgorithmParameterSpec
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
```

Initializes this key agreement with the given key and set of
algorithm parameters.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** params

- the key agreement parameters
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

---

#### init

public final void init​(

Key

key,

AlgorithmParameterSpec

params)
throws

InvalidKeyException

,

InvalidAlgorithmParameterException

Initializes this key agreement with the given key and set of
algorithm parameters.

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

If this key agreement requires any random bytes, it will get
them using the

SecureRandom

implementation of the highest-priority
installed provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

init

```java
public final void init​(
Key
key,

AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
```

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

**Parameters:** key

- the party's private information. For example, in the case
of the Diffie-Hellman key agreement, this would be the party's own
Diffie-Hellman private key.
**Parameters:** params

- the key agreement parameters
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the given key is
inappropriate for this key agreement, e.g., is of the wrong type or
has an incompatible algorithm type.
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key agreement.

---

#### init

public final void init​(

Key

key,

AlgorithmParameterSpec

params,

SecureRandom

random)
throws

InvalidKeyException

,

InvalidAlgorithmParameterException

Initializes this key agreement with the given key, set of
algorithm parameters, and source of randomness.

doPhase

```java
public final
Key
doPhase​(
Key
key,
boolean lastPhase)
throws
InvalidKeyException
,

IllegalStateException
```

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

**Parameters:** key

- the key for this phase. For example, in the case of
Diffie-Hellman between 2 parties, this would be the other party's
Diffie-Hellman public key.
**Parameters:** lastPhase

- flag which indicates whether or not this is the last
phase of this key agreement.
**Returns:** the (intermediate) key resulting from this phase, or null
if this phase does not yield a key
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this phase.
**Throws:** IllegalStateException

- if this key agreement has not been
initialized.

---

#### doPhase

public final

Key

doPhase​(

Key

key,
boolean lastPhase)
throws

InvalidKeyException

,

IllegalStateException

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

generateSecret

```java
public final byte[] generateSecret()
throws
IllegalStateException
```

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Returns:** the new buffer with the shared secret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet

---

#### generateSecret

public final byte[] generateSecret()
throws

IllegalStateException

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

generateSecret

```java
public final int generateSecret​(byte[] sharedSecret,
int offset)
throws
IllegalStateException
,

ShortBufferException
```

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

If the

sharedSecret

buffer is too small to hold the
result, a

ShortBufferException

is thrown.
In this case, this call should be repeated with a larger output buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** sharedSecret

- the buffer for the shared secret
**Parameters:** offset

- the offset in

sharedSecret

where the
shared secret will be stored
**Returns:** the number of bytes placed into

sharedSecret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the secret

---

#### generateSecret

public final int generateSecret​(byte[] sharedSecret,
int offset)
throws

IllegalStateException

,

ShortBufferException

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

If the

sharedSecret

buffer is too small to hold the
result, a

ShortBufferException

is thrown.
In this case, this call should be repeated with a larger output buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

If the

sharedSecret

buffer is too small to hold the
result, a

ShortBufferException

is thrown.
In this case, this call should be repeated with a larger output buffer.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

generateSecret

```java
public final
SecretKey
generateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** algorithm

- the requested secret-key algorithm
**Returns:** the shared secret key
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** NoSuchAlgorithmException

- if the specified secret-key
algorithm is not available
**Throws:** InvalidKeyException

- if the shared secret-key material cannot
be used to generate a secret key of the specified algorithm (e.g.,
the key material is too short)

---

#### generateSecret

public final

SecretKey

generateSecret​(

String

algorithm)
throws

IllegalStateException

,

NoSuchAlgorithmException

,

InvalidKeyException

Creates the shared secret and returns it as a

SecretKey

object of the specified algorithm.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

This method resets this

KeyAgreement

object, so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

init

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

---

