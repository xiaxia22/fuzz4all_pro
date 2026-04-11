# Class KeyGenerator

**Source:** `java.base\javax\crypto\KeyGenerator.html`

### Class Description

```java
public class
KeyGenerator

extends
Object
```

This class provides the functionality of a secret (symmetric) key generator.

Key generators are constructed using one of the

getInstance

class methods of this class.

KeyGenerator objects are reusable, i.e., after a key has been
generated, the same KeyGenerator object can be re-used to generate further
keys.

There are two ways to generate a key: in an algorithm-independent
manner, and in an algorithm-specific manner.
The only difference between the two is the initialization of the object:

- Algorithm-Independent Initialization

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** SecretKey

---

### Field Details

*No entries found.*

### Constructor Details

#### protected KeyGenerator​(
KeyGeneratorSpi
keyGenSpi,

Provider
provider,

String
algorithm)

Creates a KeyGenerator object.

**Parameters:**
- keyGenSpi

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

KeyGenerator

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyGenerator

object.

**Returns:**
- the algorithm name of this

KeyGenerator

object.

---

#### public static final
KeyGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new

KeyGenerator

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

KeyGeneratorSpi

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
KeyGenerator
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

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

KeyGenerator

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

KeyGeneratorSpi

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
KeyGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the new

KeyGenerator

object

**Throws:**
- IllegalArgumentException

- if the

provider

is

null
- NoSuchAlgorithmException

- if a

KeyGeneratorSpi

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

KeyGenerator

object.

**Returns:**
- the provider of this

KeyGenerator

object

---

#### public final void init​(
SecureRandom
random)

Initializes this key generator.

**Parameters:**
- random

- the source of randomness for this generator

---

#### public final void init​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException

Initializes this key generator with the specified parameter set.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:**
- params

- the key generation parameters

**Throws:**
- InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key generator

---

#### public final void init​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:**
- params

- the key generation parameters
- random

- the source of randomness for this key generator

**Throws:**
- InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

---

#### public final void init​(int keysize)

Initializes this key generator for a certain keysize.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:**
- keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.

**Throws:**
- InvalidParameterException

- if the keysize is wrong or not
supported.

---

#### public final void init​(int keysize,

SecureRandom
random)

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

**Parameters:**
- keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
- random

- the source of randomness for this key generator

**Throws:**
- InvalidParameterException

- if the keysize is wrong or not
supported.

---

#### public final
SecretKey
generateKey()

Generates a secret key.

**Returns:**
- the new key

---

### Additional Sections

#### Class KeyGenerator

java.lang.Object

- javax.crypto.KeyGenerator

javax.crypto.KeyGenerator

```java
public class
KeyGenerator

extends
Object
```

This class provides the functionality of a secret (symmetric) key generator.

Key generators are constructed using one of the

getInstance

class methods of this class.

KeyGenerator objects are reusable, i.e., after a key has been
generated, the same KeyGenerator object can be re-used to generate further
keys.

There are two ways to generate a key: in an algorithm-independent
manner, and in an algorithm-specific manner.
The only difference between the two is the initialization of the object:

- Algorithm-Independent Initialization

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** SecretKey

public class

KeyGenerator

extends

Object

This class provides the functionality of a secret (symmetric) key generator.

Key generators are constructed using one of the

getInstance

class methods of this class.

KeyGenerator objects are reusable, i.e., after a key has been
generated, the same KeyGenerator object can be re-used to generate further
keys.

There are two ways to generate a key: in an algorithm-independent
manner, and in an algorithm-specific manner.
The only difference between the two is the initialization of the object:

- Algorithm-Independent Initialization

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Key generators are constructed using one of the

getInstance

class methods of this class.

KeyGenerator objects are reusable, i.e., after a key has been
generated, the same KeyGenerator object can be re-used to generate further
keys.

There are two ways to generate a key: in an algorithm-independent
manner, and in an algorithm-specific manner.
The only difference between the two is the initialization of the object:

- Algorithm-Independent Initialization

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

KeyGenerator objects are reusable, i.e., after a key has been
generated, the same KeyGenerator object can be re-used to generate further
keys.

There are two ways to generate a key: in an algorithm-independent
manner, and in an algorithm-specific manner.
The only difference between the two is the initialization of the object:

- Algorithm-Independent Initialization

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

There are two ways to generate a key: in an algorithm-independent
manner, and in an algorithm-specific manner.
The only difference between the two is the initialization of the object:

- Algorithm-Independent Initialization

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Algorithm-Independent Initialization

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

All key generators share the concepts of a

keysize

and a

source of randomness

.
There is an

init

method in this KeyGenerator class that takes these two universally
shared types of arguments. There is also one that takes just a

keysize

argument, and uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation), and one that takes just a
source of randomness.

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

Since no other parameters are specified when you call the above
algorithm-independent

init

methods, it is up to the
provider what to do about the algorithm-specific parameters (if any) to be
associated with each of the keys.

Algorithm-Specific Initialization

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

For situations where a set of algorithm-specific parameters already
exists, there are two

init

methods that have an

AlgorithmParameterSpec

argument. One also has a

SecureRandom

argument, while the
other uses the SecureRandom implementation
of the highest-priority installed provider as the source of randomness
(or a system-provided source of randomness if none of the installed
providers supply a SecureRandom implementation).

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support the
following standard

KeyGenerator

algorithms with the keysizes in
parentheses:

- AES

(128)
- DES

(56)
- DESede

(168)
- HmacSHA1
- HmacSHA256

These algorithms are described in the

KeyGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

AES

(128)

DES

(56)

DESede

(168)

HmacSHA1

HmacSHA256

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

KeyGenerator

​(

KeyGeneratorSpi

keyGenSpi,

Provider

provider,

String

algorithm)

Creates a KeyGenerator object.

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

generateKey

()

Generates a secret key.

String

getAlgorithm

()

Returns the algorithm name of this

KeyGenerator

object.

static

KeyGenerator

getInstance

​(

String

algorithm)

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

static

KeyGenerator

getInstance

​(

String

algorithm,

String

provider)

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

static

KeyGenerator

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

Provider

getProvider

()

Returns the provider of this

KeyGenerator

object.

void

init

​(int keysize)

Initializes this key generator for a certain keysize.

void

init

​(int keysize,

SecureRandom

random)

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

void

init

​(

SecureRandom

random)

Initializes this key generator.

void

init

​(

AlgorithmParameterSpec

params)

Initializes this key generator with the specified parameter set.

void

init

​(

AlgorithmParameterSpec

params,

SecureRandom

random)

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

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

KeyGenerator

​(

KeyGeneratorSpi

keyGenSpi,

Provider

provider,

String

algorithm)

Creates a KeyGenerator object.

---

#### Constructor Summary

Creates a KeyGenerator object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SecretKey

generateKey

()

Generates a secret key.

String

getAlgorithm

()

Returns the algorithm name of this

KeyGenerator

object.

static

KeyGenerator

getInstance

​(

String

algorithm)

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

static

KeyGenerator

getInstance

​(

String

algorithm,

String

provider)

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

static

KeyGenerator

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

Provider

getProvider

()

Returns the provider of this

KeyGenerator

object.

void

init

​(int keysize)

Initializes this key generator for a certain keysize.

void

init

​(int keysize,

SecureRandom

random)

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

void

init

​(

SecureRandom

random)

Initializes this key generator.

void

init

​(

AlgorithmParameterSpec

params)

Initializes this key generator with the specified parameter set.

void

init

​(

AlgorithmParameterSpec

params,

SecureRandom

random)

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

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

Generates a secret key.

Returns the algorithm name of this

KeyGenerator

object.

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

Returns the provider of this

KeyGenerator

object.

Initializes this key generator for a certain keysize.

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

Initializes this key generator.

Initializes this key generator with the specified parameter set.

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

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

- KeyGenerator

```java
protected KeyGenerator​(
KeyGeneratorSpi
keyGenSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyGenerator object.

**Parameters:** keyGenSpi

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

KeyGenerator

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyGenerator

object.

**Returns:** the algorithm name of this

KeyGenerator

object.

- getInstance

```java
public static final
KeyGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the first
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

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyGenerator

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyGeneratorSpi

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
KeyGenerator
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

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyGenerator

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyGeneratorSpi

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
KeyGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyGenerator

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyGeneratorSpi

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

KeyGenerator

object.

**Returns:** the provider of this

KeyGenerator

object

- init

```java
public final void init​(
SecureRandom
random)
```

Initializes this key generator.

**Parameters:** random

- the source of randomness for this generator

- init

```java
public final void init​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this key generator with the specified parameter set.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** params

- the key generation parameters
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key generator

- init

```java
public final void init​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:** params

- the key generation parameters
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

- init

```java
public final void init​(int keysize)
```

Initializes this key generator for a certain keysize.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

- init

```java
public final void init​(int keysize,

SecureRandom
random)
```

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

- generateKey

```java
public final
SecretKey
generateKey()
```

Generates a secret key.

**Returns:** the new key

Constructor Detail

- KeyGenerator

```java
protected KeyGenerator​(
KeyGeneratorSpi
keyGenSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyGenerator object.

**Parameters:** keyGenSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Constructor Detail

KeyGenerator

```java
protected KeyGenerator​(
KeyGeneratorSpi
keyGenSpi,

Provider
provider,

String
algorithm)
```

Creates a KeyGenerator object.

**Parameters:** keyGenSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### KeyGenerator

protected KeyGenerator​(

KeyGeneratorSpi

keyGenSpi,

Provider

provider,

String

algorithm)

Creates a KeyGenerator object.

Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyGenerator

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyGenerator

object.

**Returns:** the algorithm name of this

KeyGenerator

object.

- getInstance

```java
public static final
KeyGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the first
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

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyGenerator

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyGeneratorSpi

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
KeyGenerator
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

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyGenerator

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyGeneratorSpi

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
KeyGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyGenerator

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyGeneratorSpi

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

KeyGenerator

object.

**Returns:** the provider of this

KeyGenerator

object

- init

```java
public final void init​(
SecureRandom
random)
```

Initializes this key generator.

**Parameters:** random

- the source of randomness for this generator

- init

```java
public final void init​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this key generator with the specified parameter set.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** params

- the key generation parameters
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key generator

- init

```java
public final void init​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:** params

- the key generation parameters
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

- init

```java
public final void init​(int keysize)
```

Initializes this key generator for a certain keysize.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

- init

```java
public final void init​(int keysize,

SecureRandom
random)
```

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

- generateKey

```java
public final
SecretKey
generateKey()
```

Generates a secret key.

**Returns:** the new key

---

#### Method Detail

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyGenerator

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyGenerator

object.

**Returns:** the algorithm name of this

KeyGenerator

object.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the algorithm name of this

KeyGenerator

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyGenerator

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyGenerator

object.

getInstance

```java
public static final
KeyGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the first
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

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

KeyGenerator

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyGeneratorSpi

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

KeyGenerator

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the first
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
KeyGenerator
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

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyGenerator

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyGeneratorSpi

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

KeyGenerator

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

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified provider
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
KeyGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested key algorithm.
See the KeyGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

KeyGenerator

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

KeyGeneratorSpi

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

KeyGenerator

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

KeyGenerator

object that generates secret keys
for the specified algorithm.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new KeyGenerator object encapsulating the
KeyGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyGenerator

object.

**Returns:** the provider of this

KeyGenerator

object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

KeyGenerator

object.

init

```java
public final void init​(
SecureRandom
random)
```

Initializes this key generator.

**Parameters:** random

- the source of randomness for this generator

---

#### init

public final void init​(

SecureRandom

random)

Initializes this key generator.

init

```java
public final void init​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this key generator with the specified parameter set.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** params

- the key generation parameters
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this key generator

---

#### init

public final void init​(

AlgorithmParameterSpec

params)
throws

InvalidAlgorithmParameterException

Initializes this key generator with the specified parameter set.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

init

```java
public final void init​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:** params

- the key generation parameters
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

---

#### init

public final void init​(

AlgorithmParameterSpec

params,

SecureRandom

random)
throws

InvalidAlgorithmParameterException

Initializes this key generator with the specified parameter
set and a user-provided source of randomness.

init

```java
public final void init​(int keysize)
```

Initializes this key generator for a certain keysize.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

---

#### init

public final void init​(int keysize)

Initializes this key generator for a certain keysize.

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

If this key generator requires any random bytes, it will get them
using the

SecureRandom

implementation of the highest-priority installed
provider as the source of randomness.
(If none of the installed providers supply an implementation of
SecureRandom, a system-provided source of randomness will be used.)

init

```java
public final void init​(int keysize,

SecureRandom
random)
```

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

---

#### init

public final void init​(int keysize,

SecureRandom

random)

Initializes this key generator for a certain keysize, using a
user-provided source of randomness.

generateKey

```java
public final
SecretKey
generateKey()
```

Generates a secret key.

**Returns:** the new key

---

#### generateKey

public final

SecretKey

generateKey()

Generates a secret key.

---

