# Class AlgorithmParameterGenerator

**Source:** `java.base\java\security\AlgorithmParameterGenerator.html`

### Class Description

```java
public class
AlgorithmParameterGenerator

extends
Object
```

The

AlgorithmParameterGenerator

class is used to generate a
set of
parameters to be used with a certain algorithm. Parameter generators
are constructed using the

getInstance

factory methods
(static methods that return instances of a given class).

The object that will generate the parameters can be initialized
in two different ways: in an algorithm-independent manner, or in an
algorithm-specific manner:

- The algorithm-independent approach uses the fact that all parameter
generators share the concept of a "size" and a
source of randomness. The measure of size is universally shared
by all algorithm parameters, though it is interpreted differently
for different algorithms. For example, in the case of parameters for
the

DSA

algorithm, "size" corresponds to the size
of the prime modulus (in bits).
When using this approach, algorithm-specific parameter generation
values - if any - default to some standard values, unless they can be
derived from the specified size.

The other approach initializes a parameter generator object
using algorithm-specific semantics, which are represented by a set of
algorithm-specific parameter generation values. To generate
Diffie-Hellman system parameters, for example, the parameter generation
values usually
consist of the size of the prime modulus and the size of the
random exponent, both specified in number of bits.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

init

method),
each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameterGenerator

algorithms and
keysizes in parentheses:

- DiffieHellman

(1024, 2048)
- DSA

(1024, 2048)

These algorithms are described in the

AlgorithmParameterGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.2
**See Also:** AlgorithmParameters

,

AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AlgorithmParameterGenerator​(
AlgorithmParameterGeneratorSpi
paramGenSpi,

Provider
provider,

String
algorithm)

Creates an AlgorithmParameterGenerator object.

**Parameters:**
- paramGenSpi

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

Returns the standard name of the algorithm this parameter
generator is associated with.

**Returns:**
- the string name of the algorithm.

---

#### public static
AlgorithmParameterGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new

AlgorithmParameterGenerator

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParameterGeneratorSpi

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
AlgorithmParameterGenerator
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the string name of the Provider.

**Returns:**
- the new

AlgorithmParameterGenerator

object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty
- NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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
AlgorithmParameterGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the string name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the

Provider

object.

**Returns:**
- the new

AlgorithmParameterGenerator

object

**Throws:**
- IllegalArgumentException

- if the specified provider is

null
- NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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

Returns the provider of this algorithm parameter generator object.

**Returns:**
- the provider of this algorithm parameter generator object

---

#### public final void init​(int size)

Initializes this parameter generator for a certain size.
To create the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:**
- size

- the size (number of bits).

---

#### public final void init​(int size,

SecureRandom
random)

Initializes this parameter generator for a certain size and source
of randomness.

**Parameters:**
- size

- the size (number of bits).
- random

- the source of randomness.

---

#### public final void init​(
AlgorithmParameterSpec
genParamSpec)
throws
InvalidAlgorithmParameterException

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.
To generate the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:**
- genParamSpec

- the set of algorithm-specific parameter generation values.

**Throws:**
- InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

---

#### public final void init​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

**Parameters:**
- genParamSpec

- the set of algorithm-specific parameter generation values.
- random

- the source of randomness.

**Throws:**
- InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

---

#### public final
AlgorithmParameters
generateParameters()

Generates the parameters.

**Returns:**
- the new AlgorithmParameters object.

---

### Additional Sections

#### Class AlgorithmParameterGenerator

java.lang.Object

- java.security.AlgorithmParameterGenerator

java.security.AlgorithmParameterGenerator

```java
public class
AlgorithmParameterGenerator

extends
Object
```

The

AlgorithmParameterGenerator

class is used to generate a
set of
parameters to be used with a certain algorithm. Parameter generators
are constructed using the

getInstance

factory methods
(static methods that return instances of a given class).

The object that will generate the parameters can be initialized
in two different ways: in an algorithm-independent manner, or in an
algorithm-specific manner:

- The algorithm-independent approach uses the fact that all parameter
generators share the concept of a "size" and a
source of randomness. The measure of size is universally shared
by all algorithm parameters, though it is interpreted differently
for different algorithms. For example, in the case of parameters for
the

DSA

algorithm, "size" corresponds to the size
of the prime modulus (in bits).
When using this approach, algorithm-specific parameter generation
values - if any - default to some standard values, unless they can be
derived from the specified size.

The other approach initializes a parameter generator object
using algorithm-specific semantics, which are represented by a set of
algorithm-specific parameter generation values. To generate
Diffie-Hellman system parameters, for example, the parameter generation
values usually
consist of the size of the prime modulus and the size of the
random exponent, both specified in number of bits.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

init

method),
each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameterGenerator

algorithms and
keysizes in parentheses:

- DiffieHellman

(1024, 2048)
- DSA

(1024, 2048)

These algorithms are described in the

AlgorithmParameterGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.2
**See Also:** AlgorithmParameters

,

AlgorithmParameterSpec

public class

AlgorithmParameterGenerator

extends

Object

The

AlgorithmParameterGenerator

class is used to generate a
set of
parameters to be used with a certain algorithm. Parameter generators
are constructed using the

getInstance

factory methods
(static methods that return instances of a given class).

The object that will generate the parameters can be initialized
in two different ways: in an algorithm-independent manner, or in an
algorithm-specific manner:

- The algorithm-independent approach uses the fact that all parameter
generators share the concept of a "size" and a
source of randomness. The measure of size is universally shared
by all algorithm parameters, though it is interpreted differently
for different algorithms. For example, in the case of parameters for
the

DSA

algorithm, "size" corresponds to the size
of the prime modulus (in bits).
When using this approach, algorithm-specific parameter generation
values - if any - default to some standard values, unless they can be
derived from the specified size.

The other approach initializes a parameter generator object
using algorithm-specific semantics, which are represented by a set of
algorithm-specific parameter generation values. To generate
Diffie-Hellman system parameters, for example, the parameter generation
values usually
consist of the size of the prime modulus and the size of the
random exponent, both specified in number of bits.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

init

method),
each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameterGenerator

algorithms and
keysizes in parentheses:

- DiffieHellman

(1024, 2048)
- DSA

(1024, 2048)

These algorithms are described in the

AlgorithmParameterGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

The object that will generate the parameters can be initialized
in two different ways: in an algorithm-independent manner, or in an
algorithm-specific manner:

- The algorithm-independent approach uses the fact that all parameter
generators share the concept of a "size" and a
source of randomness. The measure of size is universally shared
by all algorithm parameters, though it is interpreted differently
for different algorithms. For example, in the case of parameters for
the

DSA

algorithm, "size" corresponds to the size
of the prime modulus (in bits).
When using this approach, algorithm-specific parameter generation
values - if any - default to some standard values, unless they can be
derived from the specified size.

The other approach initializes a parameter generator object
using algorithm-specific semantics, which are represented by a set of
algorithm-specific parameter generation values. To generate
Diffie-Hellman system parameters, for example, the parameter generation
values usually
consist of the size of the prime modulus and the size of the
random exponent, both specified in number of bits.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

init

method),
each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameterGenerator

algorithms and
keysizes in parentheses:

- DiffieHellman

(1024, 2048)
- DSA

(1024, 2048)

These algorithms are described in the

AlgorithmParameterGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

The algorithm-independent approach uses the fact that all parameter
generators share the concept of a "size" and a
source of randomness. The measure of size is universally shared
by all algorithm parameters, though it is interpreted differently
for different algorithms. For example, in the case of parameters for
the

DSA

algorithm, "size" corresponds to the size
of the prime modulus (in bits).
When using this approach, algorithm-specific parameter generation
values - if any - default to some standard values, unless they can be
derived from the specified size.

The other approach initializes a parameter generator object
using algorithm-specific semantics, which are represented by a set of
algorithm-specific parameter generation values. To generate
Diffie-Hellman system parameters, for example, the parameter generation
values usually
consist of the size of the prime modulus and the size of the
random exponent, both specified in number of bits.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

init

method),
each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameterGenerator

algorithms and
keysizes in parentheses:

- DiffieHellman

(1024, 2048)
- DSA

(1024, 2048)

These algorithms are described in the

AlgorithmParameterGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameterGenerator

algorithms and
keysizes in parentheses:

- DiffieHellman

(1024, 2048)
- DSA

(1024, 2048)

These algorithms are described in the

AlgorithmParameterGenerator section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

DiffieHellman

(1024, 2048)

DSA

(1024, 2048)

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AlgorithmParameterGenerator

​(

AlgorithmParameterGeneratorSpi

paramGenSpi,

Provider

provider,

String

algorithm)

Creates an AlgorithmParameterGenerator object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmParameters

generateParameters

()

Generates the parameters.

String

getAlgorithm

()

Returns the standard name of the algorithm this parameter
generator is associated with.

static

AlgorithmParameterGenerator

getInstance

​(

String

algorithm)

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

static

AlgorithmParameterGenerator

getInstance

​(

String

algorithm,

String

provider)

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

static

AlgorithmParameterGenerator

getInstance

​(

String

algorithm,

Provider

provider)

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

Provider

getProvider

()

Returns the provider of this algorithm parameter generator object.

void

init

​(int size)

Initializes this parameter generator for a certain size.

void

init

​(int size,

SecureRandom

random)

Initializes this parameter generator for a certain size and source
of randomness.

void

init

​(

AlgorithmParameterSpec

genParamSpec)

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

void

init

​(

AlgorithmParameterSpec

genParamSpec,

SecureRandom

random)

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

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

AlgorithmParameterGenerator

​(

AlgorithmParameterGeneratorSpi

paramGenSpi,

Provider

provider,

String

algorithm)

Creates an AlgorithmParameterGenerator object.

---

#### Constructor Summary

Creates an AlgorithmParameterGenerator object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmParameters

generateParameters

()

Generates the parameters.

String

getAlgorithm

()

Returns the standard name of the algorithm this parameter
generator is associated with.

static

AlgorithmParameterGenerator

getInstance

​(

String

algorithm)

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

static

AlgorithmParameterGenerator

getInstance

​(

String

algorithm,

String

provider)

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

static

AlgorithmParameterGenerator

getInstance

​(

String

algorithm,

Provider

provider)

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

Provider

getProvider

()

Returns the provider of this algorithm parameter generator object.

void

init

​(int size)

Initializes this parameter generator for a certain size.

void

init

​(int size,

SecureRandom

random)

Initializes this parameter generator for a certain size and source
of randomness.

void

init

​(

AlgorithmParameterSpec

genParamSpec)

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

void

init

​(

AlgorithmParameterSpec

genParamSpec,

SecureRandom

random)

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

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

Generates the parameters.

Returns the standard name of the algorithm this parameter
generator is associated with.

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

Returns the provider of this algorithm parameter generator object.

Initializes this parameter generator for a certain size.

Initializes this parameter generator for a certain size and source
of randomness.

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

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

- AlgorithmParameterGenerator

```java
protected AlgorithmParameterGenerator​(
AlgorithmParameterGeneratorSpi
paramGenSpi,

Provider
provider,

String
algorithm)
```

Creates an AlgorithmParameterGenerator object.

**Parameters:** paramGenSpi

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

Returns the standard name of the algorithm this parameter
generator is associated with.

**Returns:** the string name of the algorithm.

- getInstance

```java
public static
AlgorithmParameterGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the first
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

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParameterGeneratorSpi

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
AlgorithmParameterGenerator
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

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the string name of the Provider.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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
AlgorithmParameterGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the string name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the

Provider

object.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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

Returns the provider of this algorithm parameter generator object.

**Returns:** the provider of this algorithm parameter generator object

- init

```java
public final void init​(int size)
```

Initializes this parameter generator for a certain size.
To create the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:** size

- the size (number of bits).

- init

```java
public final void init​(int size,

SecureRandom
random)
```

Initializes this parameter generator for a certain size and source
of randomness.

**Parameters:** size

- the size (number of bits).
**Parameters:** random

- the source of randomness.

- init

```java
public final void init​(
AlgorithmParameterSpec
genParamSpec)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.
To generate the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

- init

```java
public final void init​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Parameters:** random

- the source of randomness.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

- generateParameters

```java
public final
AlgorithmParameters
generateParameters()
```

Generates the parameters.

**Returns:** the new AlgorithmParameters object.

Constructor Detail

- AlgorithmParameterGenerator

```java
protected AlgorithmParameterGenerator​(
AlgorithmParameterGeneratorSpi
paramGenSpi,

Provider
provider,

String
algorithm)
```

Creates an AlgorithmParameterGenerator object.

**Parameters:** paramGenSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Constructor Detail

AlgorithmParameterGenerator

```java
protected AlgorithmParameterGenerator​(
AlgorithmParameterGeneratorSpi
paramGenSpi,

Provider
provider,

String
algorithm)
```

Creates an AlgorithmParameterGenerator object.

**Parameters:** paramGenSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### AlgorithmParameterGenerator

protected AlgorithmParameterGenerator​(

AlgorithmParameterGeneratorSpi

paramGenSpi,

Provider

provider,

String

algorithm)

Creates an AlgorithmParameterGenerator object.

Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the standard name of the algorithm this parameter
generator is associated with.

**Returns:** the string name of the algorithm.

- getInstance

```java
public static
AlgorithmParameterGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the first
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

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParameterGeneratorSpi

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
AlgorithmParameterGenerator
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

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the string name of the Provider.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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
AlgorithmParameterGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the string name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the

Provider

object.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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

Returns the provider of this algorithm parameter generator object.

**Returns:** the provider of this algorithm parameter generator object

- init

```java
public final void init​(int size)
```

Initializes this parameter generator for a certain size.
To create the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:** size

- the size (number of bits).

- init

```java
public final void init​(int size,

SecureRandom
random)
```

Initializes this parameter generator for a certain size and source
of randomness.

**Parameters:** size

- the size (number of bits).
**Parameters:** random

- the source of randomness.

- init

```java
public final void init​(
AlgorithmParameterSpec
genParamSpec)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.
To generate the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

- init

```java
public final void init​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Parameters:** random

- the source of randomness.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

- generateParameters

```java
public final
AlgorithmParameters
generateParameters()
```

Generates the parameters.

**Returns:** the new AlgorithmParameters object.

---

#### Method Detail

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the standard name of the algorithm this parameter
generator is associated with.

**Returns:** the string name of the algorithm.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the standard name of the algorithm this parameter
generator is associated with.

getInstance

```java
public static
AlgorithmParameterGenerator
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the first
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

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParameterGeneratorSpi

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

AlgorithmParameterGenerator

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the first
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
AlgorithmParameterGenerator
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

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the string name of the Provider.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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

AlgorithmParameterGenerator

getInstance​(

String

algorithm,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified provider
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
AlgorithmParameterGenerator
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the string name of the algorithm this
parameter generator is associated with.
See the AlgorithmParameterGenerator section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the

Provider

object.
**Returns:** the new

AlgorithmParameterGenerator

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParameterGeneratorSpi

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

AlgorithmParameterGenerator

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns an AlgorithmParameterGenerator object for generating
a set of parameters to be used with the specified algorithm.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new AlgorithmParameterGenerator object encapsulating the
AlgorithmParameterGeneratorSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this algorithm parameter generator object.

**Returns:** the provider of this algorithm parameter generator object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this algorithm parameter generator object.

init

```java
public final void init​(int size)
```

Initializes this parameter generator for a certain size.
To create the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:** size

- the size (number of bits).

---

#### init

public final void init​(int size)

Initializes this parameter generator for a certain size.
To create the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

init

```java
public final void init​(int size,

SecureRandom
random)
```

Initializes this parameter generator for a certain size and source
of randomness.

**Parameters:** size

- the size (number of bits).
**Parameters:** random

- the source of randomness.

---

#### init

public final void init​(int size,

SecureRandom

random)

Initializes this parameter generator for a certain size and source
of randomness.

init

```java
public final void init​(
AlgorithmParameterSpec
genParamSpec)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.
To generate the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

---

#### init

public final void init​(

AlgorithmParameterSpec

genParamSpec)
throws

InvalidAlgorithmParameterException

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.
To generate the parameters, the

SecureRandom

implementation of the highest-priority installed provider is used as
the source of randomness.
(If none of the installed providers supply an implementation of

SecureRandom

, a system-provided source of randomness is
used.)

init

```java
public final void init​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Parameters:** random

- the source of randomness.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

---

#### init

public final void init​(

AlgorithmParameterSpec

genParamSpec,

SecureRandom

random)
throws

InvalidAlgorithmParameterException

Initializes this parameter generator with a set of algorithm-specific
parameter generation values.

generateParameters

```java
public final
AlgorithmParameters
generateParameters()
```

Generates the parameters.

**Returns:** the new AlgorithmParameters object.

---

#### generateParameters

public final

AlgorithmParameters

generateParameters()

Generates the parameters.

---

