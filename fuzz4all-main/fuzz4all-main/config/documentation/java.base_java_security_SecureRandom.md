# Class SecureRandom

**Source:** `java.base\java\security\SecureRandom.html`

### Class Description

```java
public class
SecureRandom

extends
Random
```

This class provides a cryptographically strong random number
generator (RNG).

A cryptographically strong random number minimally complies with the
statistical random number generator tests specified in

FIPS 140-2, Security Requirements for Cryptographic Modules

,
section 4.9.1.
Additionally,

SecureRandom

must produce non-deterministic output.
Therefore any seed material passed to a

SecureRandom

object must be
unpredictable, and all

SecureRandom

output sequences must be
cryptographically strong, as described in

RFC 4086: Randomness Requirements for Security

.

Many

SecureRandom

implementations are in the form of a
pseudo-random number generator (PRNG, also known as deterministic random
bits generator or DRBG), which means they use a deterministic algorithm
to produce a pseudo-random sequence from a random seed.
Other implementations may produce true random numbers,
and yet others may use a combination of both techniques.

A caller obtains a

SecureRandom

instance via the
no-argument constructor or one of the

getInstance

methods.
For example:

```java
SecureRandom r1 = new SecureRandom();
SecureRandom r2 = SecureRandom.getInstance("NativePRNG");
SecureRandom r3 = SecureRandom.getInstance("DRBG",
DrbgParameters.instantiation(128, RESEED_ONLY, null));
```

The third statement above returns a

SecureRandom

object of the
specific algorithm supporting the specific instantiate parameters. The
implementation's effective instantiated parameters must match this minimum
request but is not necessarily the same. For example, even if the request
does not require a certain feature, the actual instantiation can provide
the feature. An implementation may lazily instantiate a

SecureRandom

until it's actually used, but the effective instantiate parameters must be
determined right after it's created and

getParameters()

should
always return the same result unchanged.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SecureRandom()

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

---

#### public SecureRandom​(byte[] seed)

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.
The

SecureRandom

instance is seeded with the specified seed bytes.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

**Parameters:**
- seed

- the seed.

---

#### protected SecureRandom​(
SecureRandomSpi
secureRandomSpi,

Provider
provider)

Creates a

SecureRandom

object.

**Parameters:**
- secureRandomSpi

- the

SecureRandom

implementation.
- provider

- the provider.

---

### Method Details

#### public static
SecureRandom
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

**Returns:**
- the new

SecureRandom

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

SecureRandomSpi

implementation for the
specified algorithm
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

**Since:**
- 1.2

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
SecureRandom
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

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

SecureRandom

object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty
- NoSuchAlgorithmException

- if a

SecureRandomSpi

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

**Since:**
- 1.2

---

#### public static
SecureRandom
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
- provider

- the provider.

**Returns:**
- the new

SecureRandom

object

**Throws:**
- IllegalArgumentException

- if the specified provider is

null
- NoSuchAlgorithmException

- if a

SecureRandomSpi

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

#### public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params)
throws
NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm and the specified

SecureRandomParameters

is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
- params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.

**Returns:**
- the new

SecureRandom

object

**Throws:**
- IllegalArgumentException

- if the specified params is

null
- NoSuchAlgorithmException

- if no Provider supports a

SecureRandomSpi

implementation for the specified
algorithm and parameters
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

**Since:**
- 9

**Implementation Note:**
- The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.

---

#### public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
- params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
- provider

- the name of the provider.

**Returns:**
- the new

SecureRandom

object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty, or params is

null
- NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
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

**Since:**
- 9

---

#### public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:**
- algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
- params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
- provider

- the provider.

**Returns:**
- the new

SecureRandom

object

**Throws:**
- IllegalArgumentException

- if the specified provider or params
is

null
- NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

**Since:**
- 9

---

#### public final
Provider
getProvider()

Returns the provider of this

SecureRandom

object.

**Returns:**
- the provider of this

SecureRandom

object.

---

#### public
String
getAlgorithm()

Returns the name of the algorithm implemented by this

SecureRandom

object.

**Returns:**
- the name of the algorithm or

unknown

if the algorithm name cannot be determined.

**Since:**
- 1.5

---

#### public
String
toString()

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation

---

#### public
SecureRandomParameters
getParameters()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

The returned value can be different from the

SecureRandomParameters

object passed into a

getInstance

method, but it cannot change during the lifetime of this

SecureRandom

object.

A caller can use the returned value to find out what features this

SecureRandom

supports.

**Returns:**
- the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.

**See Also:**
- SecureRandomSpi

**Since:**
- 9

---

#### public void setSeed​(byte[] seed)

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls are
guaranteed never to reduce randomness.

A PRNG

SecureRandom

will not seed itself automatically if

setSeed

is called before any

nextBytes

or

reseed

calls. The caller should make sure that the

seed

argument
contains enough entropy for the security of this

SecureRandom

.

**Parameters:**
- seed

- the seed.

**See Also:**
- getSeed(int)

---

#### public void setSeed​(long seed)

Reseeds this random object, using the eight bytes contained
in the given

long seed

. The given seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

This method is defined for compatibility with

java.util.Random

.

**Overrides:**
- setSeed

in class

Random

**Parameters:**
- seed

- the seed.

**See Also:**
- getSeed(int)

---

#### public void nextBytes​(byte[] bytes)

Generates a user-specified number of random bytes.

**Overrides:**
- nextBytes

in class

Random

**Parameters:**
- bytes

- the array to be filled in with random bytes.

---

#### public void nextBytes​(byte[] bytes,

SecureRandomParameters
params)

Generates a user-specified number of random bytes with
additional parameters.

**Parameters:**
- bytes

- the array to be filled in with random bytes
- params

- additional parameters

**Throws:**
- NullPointerException

- if

bytes

is null
- UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method
- IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom

**Since:**
- 9

---

#### protected final int next​(int numBits)

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros). This
method overrides a

java.util.Random

method, and serves
to provide a source of random bits to all of the methods inherited
from that class (for example,

nextInt

,

nextLong

, and

nextFloat

).

**Overrides:**
- next

in class

Random

**Parameters:**
- numBits

- number of pseudo-random bits to be generated, where

0 <= numBits <= 32

.

**Returns:**
- an

int

containing the user-specified number
of pseudo-random bits (right justified, with leading zeros).

---

#### public static byte[] getSeed​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

This method is only included for backwards compatibility.
The caller is encouraged to use one of the alternative

getInstance

methods to obtain a

SecureRandom

object, and
then call the

generateSeed

method to obtain seed bytes
from that object.

**Parameters:**
- numBytes

- the number of seed bytes to generate.

**Returns:**
- the seed bytes.

**Throws:**
- IllegalArgumentException

- if

numBytes

is negative

**See Also:**
- setSeed(byte[])

---

#### public byte[] generateSeed​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

**Parameters:**
- numBytes

- the number of seed bytes to generate.

**Returns:**
- the seed bytes.

**Throws:**
- IllegalArgumentException

- if

numBytes

is negative

---

#### public static
SecureRandom
getInstanceStrong()
throws
NoSuchAlgorithmException

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

Some situations require strong random values, such as when
creating high-value/long-lived secrets like RSA public/private
keys. To help guide applications in selecting a suitable strong

SecureRandom

implementation, Java distributions
include a list of known strong

SecureRandom

implementations in the

securerandom.strongAlgorithms

Security property.

Every implementation of the Java platform is required to
support at least one strong

SecureRandom

implementation.

**Returns:**
- a strong

SecureRandom

implementation as indicated
by the

securerandom.strongAlgorithms

Security property

**Throws:**
- NoSuchAlgorithmException

- if no algorithm is available

**See Also:**
- Security.getProperty(String)

**Since:**
- 1.8

---

#### public void reseed()

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

**Throws:**
- UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.

**Since:**
- 9

---

#### public void reseed​(
SecureRandomParameters
params)

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

Note that entropy is obtained from an entropy source. While
some data in

params

may contain entropy, its main usage is to
provide diversity.

**Parameters:**
- params

- extra parameters

**Throws:**
- UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.
- IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom

**Since:**
- 9

---

### Additional Sections

#### Class SecureRandom

java.lang.Object

- java.util.Random
- - java.security.SecureRandom

java.util.Random

- java.security.SecureRandom

java.security.SecureRandom

**All Implemented Interfaces:** Serializable

```java
public class
SecureRandom

extends
Random
```

This class provides a cryptographically strong random number
generator (RNG).

A cryptographically strong random number minimally complies with the
statistical random number generator tests specified in

FIPS 140-2, Security Requirements for Cryptographic Modules

,
section 4.9.1.
Additionally,

SecureRandom

must produce non-deterministic output.
Therefore any seed material passed to a

SecureRandom

object must be
unpredictable, and all

SecureRandom

output sequences must be
cryptographically strong, as described in

RFC 4086: Randomness Requirements for Security

.

Many

SecureRandom

implementations are in the form of a
pseudo-random number generator (PRNG, also known as deterministic random
bits generator or DRBG), which means they use a deterministic algorithm
to produce a pseudo-random sequence from a random seed.
Other implementations may produce true random numbers,
and yet others may use a combination of both techniques.

A caller obtains a

SecureRandom

instance via the
no-argument constructor or one of the

getInstance

methods.
For example:

```java
SecureRandom r1 = new SecureRandom();
SecureRandom r2 = SecureRandom.getInstance("NativePRNG");
SecureRandom r3 = SecureRandom.getInstance("DRBG",
DrbgParameters.instantiation(128, RESEED_ONLY, null));
```

The third statement above returns a

SecureRandom

object of the
specific algorithm supporting the specific instantiate parameters. The
implementation's effective instantiated parameters must match this minimum
request but is not necessarily the same. For example, even if the request
does not require a certain feature, the actual instantiation can provide
the feature. An implementation may lazily instantiate a

SecureRandom

until it's actually used, but the effective instantiate parameters must be
determined right after it's created and

getParameters()

should
always return the same result unchanged.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

**Implementation Requirements:** A

SecureRandom

service provider can advertise that it is thread-safe
by setting the

service
provider attribute

"ThreadSafe" to "true" when registering the provider.
Otherwise, this class will instead synchronize access to the following
methods of the

SecureRandomSpi

implementation:

- SecureRandomSpi.engineSetSeed(byte[])

SecureRandomSpi.engineNextBytes(byte[])

SecureRandomSpi.engineNextBytes(byte[], SecureRandomParameters)

SecureRandomSpi.engineGenerateSeed(int)

SecureRandomSpi.engineReseed(SecureRandomParameters)
**Since:** 1.1
**See Also:** SecureRandomSpi

,

Random

,

Serialized Form

public class

SecureRandom

extends

Random

This class provides a cryptographically strong random number
generator (RNG).

A cryptographically strong random number minimally complies with the
statistical random number generator tests specified in

FIPS 140-2, Security Requirements for Cryptographic Modules

,
section 4.9.1.
Additionally,

SecureRandom

must produce non-deterministic output.
Therefore any seed material passed to a

SecureRandom

object must be
unpredictable, and all

SecureRandom

output sequences must be
cryptographically strong, as described in

RFC 4086: Randomness Requirements for Security

.

Many

SecureRandom

implementations are in the form of a
pseudo-random number generator (PRNG, also known as deterministic random
bits generator or DRBG), which means they use a deterministic algorithm
to produce a pseudo-random sequence from a random seed.
Other implementations may produce true random numbers,
and yet others may use a combination of both techniques.

A caller obtains a

SecureRandom

instance via the
no-argument constructor or one of the

getInstance

methods.
For example:

```java
SecureRandom r1 = new SecureRandom();
SecureRandom r2 = SecureRandom.getInstance("NativePRNG");
SecureRandom r3 = SecureRandom.getInstance("DRBG",
DrbgParameters.instantiation(128, RESEED_ONLY, null));
```

The third statement above returns a

SecureRandom

object of the
specific algorithm supporting the specific instantiate parameters. The
implementation's effective instantiated parameters must match this minimum
request but is not necessarily the same. For example, even if the request
does not require a certain feature, the actual instantiation can provide
the feature. An implementation may lazily instantiate a

SecureRandom

until it's actually used, but the effective instantiate parameters must be
determined right after it's created and

getParameters()

should
always return the same result unchanged.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

A cryptographically strong random number minimally complies with the
statistical random number generator tests specified in

FIPS 140-2, Security Requirements for Cryptographic Modules

,
section 4.9.1.
Additionally,

SecureRandom

must produce non-deterministic output.
Therefore any seed material passed to a

SecureRandom

object must be
unpredictable, and all

SecureRandom

output sequences must be
cryptographically strong, as described in

RFC 4086: Randomness Requirements for Security

.

Many

SecureRandom

implementations are in the form of a
pseudo-random number generator (PRNG, also known as deterministic random
bits generator or DRBG), which means they use a deterministic algorithm
to produce a pseudo-random sequence from a random seed.
Other implementations may produce true random numbers,
and yet others may use a combination of both techniques.

A caller obtains a

SecureRandom

instance via the
no-argument constructor or one of the

getInstance

methods.
For example:

```java
SecureRandom r1 = new SecureRandom();
SecureRandom r2 = SecureRandom.getInstance("NativePRNG");
SecureRandom r3 = SecureRandom.getInstance("DRBG",
DrbgParameters.instantiation(128, RESEED_ONLY, null));
```

The third statement above returns a

SecureRandom

object of the
specific algorithm supporting the specific instantiate parameters. The
implementation's effective instantiated parameters must match this minimum
request but is not necessarily the same. For example, even if the request
does not require a certain feature, the actual instantiation can provide
the feature. An implementation may lazily instantiate a

SecureRandom

until it's actually used, but the effective instantiate parameters must be
determined right after it's created and

getParameters()

should
always return the same result unchanged.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

Many

SecureRandom

implementations are in the form of a
pseudo-random number generator (PRNG, also known as deterministic random
bits generator or DRBG), which means they use a deterministic algorithm
to produce a pseudo-random sequence from a random seed.
Other implementations may produce true random numbers,
and yet others may use a combination of both techniques.

A caller obtains a

SecureRandom

instance via the
no-argument constructor or one of the

getInstance

methods.
For example:

```java
SecureRandom r1 = new SecureRandom();
SecureRandom r2 = SecureRandom.getInstance("NativePRNG");
SecureRandom r3 = SecureRandom.getInstance("DRBG",
DrbgParameters.instantiation(128, RESEED_ONLY, null));
```

The third statement above returns a

SecureRandom

object of the
specific algorithm supporting the specific instantiate parameters. The
implementation's effective instantiated parameters must match this minimum
request but is not necessarily the same. For example, even if the request
does not require a certain feature, the actual instantiation can provide
the feature. An implementation may lazily instantiate a

SecureRandom

until it's actually used, but the effective instantiate parameters must be
determined right after it's created and

getParameters()

should
always return the same result unchanged.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

A caller obtains a

SecureRandom

instance via the
no-argument constructor or one of the

getInstance

methods.
For example:

```java
SecureRandom r1 = new SecureRandom();
SecureRandom r2 = SecureRandom.getInstance("NativePRNG");
SecureRandom r3 = SecureRandom.getInstance("DRBG",
DrbgParameters.instantiation(128, RESEED_ONLY, null));
```

The third statement above returns a

SecureRandom

object of the
specific algorithm supporting the specific instantiate parameters. The
implementation's effective instantiated parameters must match this minimum
request but is not necessarily the same. For example, even if the request
does not require a certain feature, the actual instantiation can provide
the feature. An implementation may lazily instantiate a

SecureRandom

until it's actually used, but the effective instantiate parameters must be
determined right after it's created and

getParameters()

should
always return the same result unchanged.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

SecureRandom r1 = new SecureRandom();
SecureRandom r2 = SecureRandom.getInstance("NativePRNG");
SecureRandom r3 = SecureRandom.getInstance("DRBG",
DrbgParameters.instantiation(128, RESEED_ONLY, null));

The third statement above returns a

SecureRandom

object of the
specific algorithm supporting the specific instantiate parameters. The
implementation's effective instantiated parameters must match this minimum
request but is not necessarily the same. For example, even if the request
does not require a certain feature, the actual instantiation can provide
the feature. An implementation may lazily instantiate a

SecureRandom

until it's actually used, but the effective instantiate parameters must be
determined right after it's created and

getParameters()

should
always return the same result unchanged.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

Typical callers of

SecureRandom

invoke the following methods
to retrieve random bytes:

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);
```

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

SecureRandom random = new SecureRandom();
byte[] bytes = new byte[20];
random.nextBytes(bytes);

Callers may also invoke the

generateSeed(int)

method
to generate a given number of seed bytes (to seed other random number
generators, for example):

```java
byte[] seed = random.generateSeed(20);
```

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

byte[] seed = random.generateSeed(20);

A newly created PRNG

SecureRandom

object is not seeded (except
if it is created by

SecureRandom(byte[])

). The first call to

nextBytes

will force it to seed itself from an implementation-
specific entropy source. This self-seeding will not occur if

setSeed

was previously called.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

A

SecureRandom

can be reseeded at any time by calling the

reseed

or

setSeed

method. The

reseed

method
reads entropy input from its entropy source to reseed itself.
The

setSeed

method requires the caller to provide the seed.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

Please note that

reseed

may not be supported by all

SecureRandom

implementations.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

Some

SecureRandom

implementations may accept a

SecureRandomParameters

parameter in its

nextBytes(byte[], SecureRandomParameters)

and

reseed(SecureRandomParameters)

methods to further
control the behavior of the methods.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

Note: Depending on the implementation, the

generateSeed

,

reseed

and

nextBytes

methods may block as entropy is being
gathered, for example, if the entropy source is /dev/random on various
Unix-like operating systems.

Thread safety

SecureRandom

objects are safe for use by multiple concurrent threads.

---

#### Thread safety

SecureRandomSpi.engineSetSeed(byte[])

SecureRandomSpi.engineNextBytes(byte[])

SecureRandomSpi.engineNextBytes(byte[], SecureRandomParameters)

SecureRandomSpi.engineGenerateSeed(int)

SecureRandomSpi.engineReseed(SecureRandomParameters)

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

SecureRandom

()

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

SecureRandom

​(byte[] seed)

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

protected

SecureRandom

​(

SecureRandomSpi

secureRandomSpi,

Provider

provider)

Creates a

SecureRandom

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

generateSeed

​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself.

String

getAlgorithm

()

Returns the name of the algorithm implemented by this

SecureRandom

object.

static

SecureRandom

getInstance

​(

String

algorithm)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

static

SecureRandom

getInstance

​(

String

algorithm,

String

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

static

SecureRandom

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

static

SecureRandom

getInstance

​(

String

algorithm,

SecureRandomParameters

params)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

static

SecureRandom

getInstance

​(

String

algorithm,

SecureRandomParameters

params,

String

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

static

SecureRandom

getInstance

​(

String

algorithm,

SecureRandomParameters

params,

Provider

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

static

SecureRandom

getInstanceStrong

()

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

SecureRandomParameters

getParameters

()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

Provider

getProvider

()

Returns the provider of this

SecureRandom

object.

static byte[]

getSeed

​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself.

protected int

next

​(int numBits)

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros).

void

nextBytes

​(byte[] bytes)

Generates a user-specified number of random bytes.

void

nextBytes

​(byte[] bytes,

SecureRandomParameters

params)

Generates a user-specified number of random bytes with
additional parameters.

void

reseed

()

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

void

reseed

​(

SecureRandomParameters

params)

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

void

setSeed

​(byte[] seed)

Reseeds this random object with the given seed.

void

setSeed

​(long seed)

Reseeds this random object, using the eight bytes contained
in the given

long seed

.

String

toString

()

Returns a Human-readable string representation of this

SecureRandom

.

- Methods declared in class java.util.

Random

doubles

,

doubles

,

doubles

,

doubles

,

ints

,

ints

,

ints

,

ints

,

longs

,

longs

,

longs

,

longs

,

nextBoolean

,

nextDouble

,

nextFloat

,

nextGaussian

,

nextInt

,

nextInt

,

nextLong

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

SecureRandom

()

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

SecureRandom

​(byte[] seed)

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

protected

SecureRandom

​(

SecureRandomSpi

secureRandomSpi,

Provider

provider)

Creates a

SecureRandom

object.

---

#### Constructor Summary

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

Creates a

SecureRandom

object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

generateSeed

​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself.

String

getAlgorithm

()

Returns the name of the algorithm implemented by this

SecureRandom

object.

static

SecureRandom

getInstance

​(

String

algorithm)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

static

SecureRandom

getInstance

​(

String

algorithm,

String

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

static

SecureRandom

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

static

SecureRandom

getInstance

​(

String

algorithm,

SecureRandomParameters

params)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

static

SecureRandom

getInstance

​(

String

algorithm,

SecureRandomParameters

params,

String

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

static

SecureRandom

getInstance

​(

String

algorithm,

SecureRandomParameters

params,

Provider

provider)

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

static

SecureRandom

getInstanceStrong

()

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

SecureRandomParameters

getParameters

()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

Provider

getProvider

()

Returns the provider of this

SecureRandom

object.

static byte[]

getSeed

​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself.

protected int

next

​(int numBits)

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros).

void

nextBytes

​(byte[] bytes)

Generates a user-specified number of random bytes.

void

nextBytes

​(byte[] bytes,

SecureRandomParameters

params)

Generates a user-specified number of random bytes with
additional parameters.

void

reseed

()

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

void

reseed

​(

SecureRandomParameters

params)

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

void

setSeed

​(byte[] seed)

Reseeds this random object with the given seed.

void

setSeed

​(long seed)

Reseeds this random object, using the eight bytes contained
in the given

long seed

.

String

toString

()

Returns a Human-readable string representation of this

SecureRandom

.

- Methods declared in class java.util.

Random

doubles

,

doubles

,

doubles

,

doubles

,

ints

,

ints

,

ints

,

ints

,

longs

,

longs

,

longs

,

longs

,

nextBoolean

,

nextDouble

,

nextFloat

,

nextGaussian

,

nextInt

,

nextInt

,

nextLong

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself.

Returns the name of the algorithm implemented by this

SecureRandom

object.

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

Returns the provider of this

SecureRandom

object.

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros).

Generates a user-specified number of random bytes.

Generates a user-specified number of random bytes with
additional parameters.

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

Reseeds this random object with the given seed.

Reseeds this random object, using the eight bytes contained
in the given

long seed

.

Returns a Human-readable string representation of this

SecureRandom

.

Methods declared in class java.util.

Random

doubles

,

doubles

,

doubles

,

doubles

,

ints

,

ints

,

ints

,

ints

,

longs

,

longs

,

longs

,

longs

,

nextBoolean

,

nextDouble

,

nextFloat

,

nextGaussian

,

nextInt

,

nextInt

,

nextLong

---

#### Methods declared in class java.util. Random

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SecureRandom

```java
public SecureRandom()
```

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

- SecureRandom

```java
public SecureRandom​(byte[] seed)
```

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.
The

SecureRandom

instance is seeded with the specified seed bytes.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

**Parameters:** seed

- the seed.

- SecureRandom

```java
protected SecureRandom​(
SecureRandomSpi
secureRandomSpi,

Provider
provider)
```

Creates a

SecureRandom

object.

**Parameters:** secureRandomSpi

- the

SecureRandom

implementation.
**Parameters:** provider

- the provider.

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
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

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Returns:** the new

SecureRandom

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

SecureRandomSpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 1.2
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
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

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SecureRandomSpi

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
**Since:** 1.2
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if a

SecureRandomSpi

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

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm and the specified

SecureRandomParameters

is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified params is

null
**Throws:** NoSuchAlgorithmException

- if no Provider supports a

SecureRandomSpi

implementation for the specified
algorithm and parameters
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty, or params is

null
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Parameters:** provider

- the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified provider or params
is

null
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

SecureRandom

object.

**Returns:** the provider of this

SecureRandom

object.

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the name of the algorithm implemented by this

SecureRandom

object.

**Returns:** the name of the algorithm or

unknown

if the algorithm name cannot be determined.
**Since:** 1.5

- toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

- getParameters

```java
public
SecureRandomParameters
getParameters()
```

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

The returned value can be different from the

SecureRandomParameters

object passed into a

getInstance

method, but it cannot change during the lifetime of this

SecureRandom

object.

A caller can use the returned value to find out what features this

SecureRandom

supports.

**Returns:** the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.
**Since:** 9
**See Also:** SecureRandomSpi

- setSeed

```java
public void setSeed​(byte[] seed)
```

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls are
guaranteed never to reduce randomness.

A PRNG

SecureRandom

will not seed itself automatically if

setSeed

is called before any

nextBytes

or

reseed

calls. The caller should make sure that the

seed

argument
contains enough entropy for the security of this

SecureRandom

.

**Parameters:** seed

- the seed.
**See Also:** getSeed(int)

- setSeed

```java
public void setSeed​(long seed)
```

Reseeds this random object, using the eight bytes contained
in the given

long seed

. The given seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

This method is defined for compatibility with

java.util.Random

.

**Overrides:** setSeed

in class

Random
**Parameters:** seed

- the seed.
**See Also:** getSeed(int)

- nextBytes

```java
public void nextBytes​(byte[] bytes)
```

Generates a user-specified number of random bytes.

**Overrides:** nextBytes

in class

Random
**Parameters:** bytes

- the array to be filled in with random bytes.

- nextBytes

```java
public void nextBytes​(byte[] bytes,

SecureRandomParameters
params)
```

Generates a user-specified number of random bytes with
additional parameters.

**Parameters:** bytes

- the array to be filled in with random bytes
**Parameters:** params

- additional parameters
**Throws:** NullPointerException

- if

bytes

is null
**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

- next

```java
protected final int next​(int numBits)
```

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros). This
method overrides a

java.util.Random

method, and serves
to provide a source of random bits to all of the methods inherited
from that class (for example,

nextInt

,

nextLong

, and

nextFloat

).

**Overrides:** next

in class

Random
**Parameters:** numBits

- number of pseudo-random bits to be generated, where

0 <= numBits <= 32

.
**Returns:** an

int

containing the user-specified number
of pseudo-random bits (right justified, with leading zeros).

- getSeed

```java
public static byte[] getSeed​(int numBytes)
```

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

This method is only included for backwards compatibility.
The caller is encouraged to use one of the alternative

getInstance

methods to obtain a

SecureRandom

object, and
then call the

generateSeed

method to obtain seed bytes
from that object.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.
**Throws:** IllegalArgumentException

- if

numBytes

is negative
**See Also:** setSeed(byte[])

- generateSeed

```java
public byte[] generateSeed​(int numBytes)
```

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.
**Throws:** IllegalArgumentException

- if

numBytes

is negative

- getInstanceStrong

```java
public static
SecureRandom
getInstanceStrong()
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

Some situations require strong random values, such as when
creating high-value/long-lived secrets like RSA public/private
keys. To help guide applications in selecting a suitable strong

SecureRandom

implementation, Java distributions
include a list of known strong

SecureRandom

implementations in the

securerandom.strongAlgorithms

Security property.

Every implementation of the Java platform is required to
support at least one strong

SecureRandom

implementation.

**Returns:** a strong

SecureRandom

implementation as indicated
by the

securerandom.strongAlgorithms

Security property
**Throws:** NoSuchAlgorithmException

- if no algorithm is available
**Since:** 1.8
**See Also:** Security.getProperty(String)

- reseed

```java
public void reseed()
```

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.
**Since:** 9

- reseed

```java
public void reseed​(
SecureRandomParameters
params)
```

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

Note that entropy is obtained from an entropy source. While
some data in

params

may contain entropy, its main usage is to
provide diversity.

**Parameters:** params

- extra parameters
**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

Constructor Detail

- SecureRandom

```java
public SecureRandom()
```

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

- SecureRandom

```java
public SecureRandom​(byte[] seed)
```

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.
The

SecureRandom

instance is seeded with the specified seed bytes.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

**Parameters:** seed

- the seed.

- SecureRandom

```java
protected SecureRandom​(
SecureRandomSpi
secureRandomSpi,

Provider
provider)
```

Creates a

SecureRandom

object.

**Parameters:** secureRandomSpi

- the

SecureRandom

implementation.
**Parameters:** provider

- the provider.

---

#### Constructor Detail

SecureRandom

```java
public SecureRandom()
```

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

---

#### SecureRandom

public SecureRandom()

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

SecureRandom

```java
public SecureRandom​(byte[] seed)
```

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.
The

SecureRandom

instance is seeded with the specified seed bytes.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

**Parameters:** seed

- the seed.

---

#### SecureRandom

public SecureRandom​(byte[] seed)

Constructs a secure random number generator (RNG) implementing the
default random number algorithm.
The

SecureRandom

instance is seeded with the specified seed bytes.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

This constructor traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports a

SecureRandom

(RNG) algorithm is returned.
If none of the Providers support a RNG algorithm,
then an implementation-specific default is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.

SecureRandom

```java
protected SecureRandom​(
SecureRandomSpi
secureRandomSpi,

Provider
provider)
```

Creates a

SecureRandom

object.

**Parameters:** secureRandomSpi

- the

SecureRandom

implementation.
**Parameters:** provider

- the provider.

---

#### SecureRandom

protected SecureRandom​(

SecureRandomSpi

secureRandomSpi,

Provider

provider)

Creates a

SecureRandom

object.

Method Detail

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
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

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Returns:** the new

SecureRandom

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

SecureRandomSpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 1.2
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
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

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SecureRandomSpi

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
**Since:** 1.2
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if a

SecureRandomSpi

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

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm and the specified

SecureRandomParameters

is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified params is

null
**Throws:** NoSuchAlgorithmException

- if no Provider supports a

SecureRandomSpi

implementation for the specified
algorithm and parameters
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty, or params is

null
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

- getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Parameters:** provider

- the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified provider or params
is

null
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

SecureRandom

object.

**Returns:** the provider of this

SecureRandom

object.

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the name of the algorithm implemented by this

SecureRandom

object.

**Returns:** the name of the algorithm or

unknown

if the algorithm name cannot be determined.
**Since:** 1.5

- toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

- getParameters

```java
public
SecureRandomParameters
getParameters()
```

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

The returned value can be different from the

SecureRandomParameters

object passed into a

getInstance

method, but it cannot change during the lifetime of this

SecureRandom

object.

A caller can use the returned value to find out what features this

SecureRandom

supports.

**Returns:** the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.
**Since:** 9
**See Also:** SecureRandomSpi

- setSeed

```java
public void setSeed​(byte[] seed)
```

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls are
guaranteed never to reduce randomness.

A PRNG

SecureRandom

will not seed itself automatically if

setSeed

is called before any

nextBytes

or

reseed

calls. The caller should make sure that the

seed

argument
contains enough entropy for the security of this

SecureRandom

.

**Parameters:** seed

- the seed.
**See Also:** getSeed(int)

- setSeed

```java
public void setSeed​(long seed)
```

Reseeds this random object, using the eight bytes contained
in the given

long seed

. The given seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

This method is defined for compatibility with

java.util.Random

.

**Overrides:** setSeed

in class

Random
**Parameters:** seed

- the seed.
**See Also:** getSeed(int)

- nextBytes

```java
public void nextBytes​(byte[] bytes)
```

Generates a user-specified number of random bytes.

**Overrides:** nextBytes

in class

Random
**Parameters:** bytes

- the array to be filled in with random bytes.

- nextBytes

```java
public void nextBytes​(byte[] bytes,

SecureRandomParameters
params)
```

Generates a user-specified number of random bytes with
additional parameters.

**Parameters:** bytes

- the array to be filled in with random bytes
**Parameters:** params

- additional parameters
**Throws:** NullPointerException

- if

bytes

is null
**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

- next

```java
protected final int next​(int numBits)
```

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros). This
method overrides a

java.util.Random

method, and serves
to provide a source of random bits to all of the methods inherited
from that class (for example,

nextInt

,

nextLong

, and

nextFloat

).

**Overrides:** next

in class

Random
**Parameters:** numBits

- number of pseudo-random bits to be generated, where

0 <= numBits <= 32

.
**Returns:** an

int

containing the user-specified number
of pseudo-random bits (right justified, with leading zeros).

- getSeed

```java
public static byte[] getSeed​(int numBytes)
```

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

This method is only included for backwards compatibility.
The caller is encouraged to use one of the alternative

getInstance

methods to obtain a

SecureRandom

object, and
then call the

generateSeed

method to obtain seed bytes
from that object.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.
**Throws:** IllegalArgumentException

- if

numBytes

is negative
**See Also:** setSeed(byte[])

- generateSeed

```java
public byte[] generateSeed​(int numBytes)
```

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.
**Throws:** IllegalArgumentException

- if

numBytes

is negative

- getInstanceStrong

```java
public static
SecureRandom
getInstanceStrong()
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

Some situations require strong random values, such as when
creating high-value/long-lived secrets like RSA public/private
keys. To help guide applications in selecting a suitable strong

SecureRandom

implementation, Java distributions
include a list of known strong

SecureRandom

implementations in the

securerandom.strongAlgorithms

Security property.

Every implementation of the Java platform is required to
support at least one strong

SecureRandom

implementation.

**Returns:** a strong

SecureRandom

implementation as indicated
by the

securerandom.strongAlgorithms

Security property
**Throws:** NoSuchAlgorithmException

- if no algorithm is available
**Since:** 1.8
**See Also:** Security.getProperty(String)

- reseed

```java
public void reseed()
```

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.
**Since:** 9

- reseed

```java
public void reseed​(
SecureRandomParameters
params)
```

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

Note that entropy is obtained from an entropy source. While
some data in

params

may contain entropy, its main usage is to
provide diversity.

**Parameters:** params

- extra parameters
**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

---

#### Method Detail

getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
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

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Returns:** the new

SecureRandom

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

SecureRandomSpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 1.2
**See Also:** Provider

---

#### getInstance

public static

SecureRandom

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
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
SecureRandom
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

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SecureRandomSpi

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
**Since:** 1.2
**See Also:** Provider

---

#### getInstance

public static

SecureRandom

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

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
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
SecureRandom
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified provider is

null
**Throws:** NoSuchAlgorithmException

- if a

SecureRandomSpi

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

SecureRandom

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object
does not have to be registered in the provider list.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object
does not have to be registered in the provider list.

getInstance

```java
public static
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm and the specified

SecureRandomParameters

is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified params is

null
**Throws:** NoSuchAlgorithmException

- if no Provider supports a

SecureRandomSpi

implementation for the specified
algorithm and parameters
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

---

#### getInstance

public static

SecureRandom

getInstance​(

String

algorithm,

SecureRandomParameters

params)
throws

NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm and the specified

SecureRandomParameters

is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the first
Provider that supports the specified algorithm and the specified

SecureRandomParameters

is returned.

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
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty, or params is

null
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

---

#### getInstance

public static

SecureRandom

getInstance​(

String

algorithm,

SecureRandomParameters

params,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified provider
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
SecureRandom
getInstance​(
String
algorithm,

SecureRandomParameters
params,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** algorithm

- the name of the RNG algorithm.
See the

SecureRandom

section in the

Java Security Standard Algorithm Names Specification

for information about standard RNG algorithm names.
**Parameters:** params

- the

SecureRandomParameters

the newly created

SecureRandom

object must support.
**Parameters:** provider

- the provider.
**Returns:** the new

SecureRandom

object
**Throws:** IllegalArgumentException

- if the specified provider or params
is

null
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

SecureRandomSpi

implementation for the
specified algorithm and parameters
**Throws:** NullPointerException

- if

algorithm

is

null
**Since:** 9
**See Also:** Provider

---

#### getInstance

public static

SecureRandom

getInstance​(

String

algorithm,

SecureRandomParameters

params,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

SecureRandom

object that implements the specified
Random Number Generator (RNG) algorithm and supports the specified

SecureRandomParameters

request.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object does not have to be registered in the
provider list.

A new

SecureRandom

object encapsulating the

SecureRandomSpi

implementation from the specified

Provider

object is returned. Note that the specified

Provider

object does not have to be registered in the
provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

SecureRandom

object.

**Returns:** the provider of this

SecureRandom

object.

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

SecureRandom

object.

getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the name of the algorithm implemented by this

SecureRandom

object.

**Returns:** the name of the algorithm or

unknown

if the algorithm name cannot be determined.
**Since:** 1.5

---

#### getAlgorithm

public

String

getAlgorithm()

Returns the name of the algorithm implemented by this

SecureRandom

object.

toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

---

#### toString

public

String

toString()

Returns a Human-readable string representation of this

SecureRandom

.

getParameters

```java
public
SecureRandomParameters
getParameters()
```

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

The returned value can be different from the

SecureRandomParameters

object passed into a

getInstance

method, but it cannot change during the lifetime of this

SecureRandom

object.

A caller can use the returned value to find out what features this

SecureRandom

supports.

**Returns:** the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.
**Since:** 9
**See Also:** SecureRandomSpi

---

#### getParameters

public

SecureRandomParameters

getParameters()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

The returned value can be different from the

SecureRandomParameters

object passed into a

getInstance

method, but it cannot change during the lifetime of this

SecureRandom

object.

A caller can use the returned value to find out what features this

SecureRandom

supports.

The returned value can be different from the

SecureRandomParameters

object passed into a

getInstance

method, but it cannot change during the lifetime of this

SecureRandom

object.

A caller can use the returned value to find out what features this

SecureRandom

supports.

A caller can use the returned value to find out what features this

SecureRandom

supports.

setSeed

```java
public void setSeed​(byte[] seed)
```

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls are
guaranteed never to reduce randomness.

A PRNG

SecureRandom

will not seed itself automatically if

setSeed

is called before any

nextBytes

or

reseed

calls. The caller should make sure that the

seed

argument
contains enough entropy for the security of this

SecureRandom

.

**Parameters:** seed

- the seed.
**See Also:** getSeed(int)

---

#### setSeed

public void setSeed​(byte[] seed)

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls are
guaranteed never to reduce randomness.

A PRNG

SecureRandom

will not seed itself automatically if

setSeed

is called before any

nextBytes

or

reseed

calls. The caller should make sure that the

seed

argument
contains enough entropy for the security of this

SecureRandom

.

A PRNG

SecureRandom

will not seed itself automatically if

setSeed

is called before any

nextBytes

or

reseed

calls. The caller should make sure that the

seed

argument
contains enough entropy for the security of this

SecureRandom

.

setSeed

```java
public void setSeed​(long seed)
```

Reseeds this random object, using the eight bytes contained
in the given

long seed

. The given seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

This method is defined for compatibility with

java.util.Random

.

**Overrides:** setSeed

in class

Random
**Parameters:** seed

- the seed.
**See Also:** getSeed(int)

---

#### setSeed

public void setSeed​(long seed)

Reseeds this random object, using the eight bytes contained
in the given

long seed

. The given seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

This method is defined for compatibility with

java.util.Random

.

This method is defined for compatibility with

java.util.Random

.

nextBytes

```java
public void nextBytes​(byte[] bytes)
```

Generates a user-specified number of random bytes.

**Overrides:** nextBytes

in class

Random
**Parameters:** bytes

- the array to be filled in with random bytes.

---

#### nextBytes

public void nextBytes​(byte[] bytes)

Generates a user-specified number of random bytes.

nextBytes

```java
public void nextBytes​(byte[] bytes,

SecureRandomParameters
params)
```

Generates a user-specified number of random bytes with
additional parameters.

**Parameters:** bytes

- the array to be filled in with random bytes
**Parameters:** params

- additional parameters
**Throws:** NullPointerException

- if

bytes

is null
**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

---

#### nextBytes

public void nextBytes​(byte[] bytes,

SecureRandomParameters

params)

Generates a user-specified number of random bytes with
additional parameters.

next

```java
protected final int next​(int numBits)
```

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros). This
method overrides a

java.util.Random

method, and serves
to provide a source of random bits to all of the methods inherited
from that class (for example,

nextInt

,

nextLong

, and

nextFloat

).

**Overrides:** next

in class

Random
**Parameters:** numBits

- number of pseudo-random bits to be generated, where

0 <= numBits <= 32

.
**Returns:** an

int

containing the user-specified number
of pseudo-random bits (right justified, with leading zeros).

---

#### next

protected final int next​(int numBits)

Generates an integer containing the user-specified number of
pseudo-random bits (right justified, with leading zeros). This
method overrides a

java.util.Random

method, and serves
to provide a source of random bits to all of the methods inherited
from that class (for example,

nextInt

,

nextLong

, and

nextFloat

).

getSeed

```java
public static byte[] getSeed​(int numBytes)
```

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

This method is only included for backwards compatibility.
The caller is encouraged to use one of the alternative

getInstance

methods to obtain a

SecureRandom

object, and
then call the

generateSeed

method to obtain seed bytes
from that object.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.
**Throws:** IllegalArgumentException

- if

numBytes

is negative
**See Also:** setSeed(byte[])

---

#### getSeed

public static byte[] getSeed​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

This method is only included for backwards compatibility.
The caller is encouraged to use one of the alternative

getInstance

methods to obtain a

SecureRandom

object, and
then call the

generateSeed

method to obtain seed bytes
from that object.

This method is only included for backwards compatibility.
The caller is encouraged to use one of the alternative

getInstance

methods to obtain a

SecureRandom

object, and
then call the

generateSeed

method to obtain seed bytes
from that object.

generateSeed

```java
public byte[] generateSeed​(int numBytes)
```

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.
**Throws:** IllegalArgumentException

- if

numBytes

is negative

---

#### generateSeed

public byte[] generateSeed​(int numBytes)

Returns the given number of seed bytes, computed using the seed
generation algorithm that this class uses to seed itself. This
call may be used to seed other random number generators.

getInstanceStrong

```java
public static
SecureRandom
getInstanceStrong()
throws
NoSuchAlgorithmException
```

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

Some situations require strong random values, such as when
creating high-value/long-lived secrets like RSA public/private
keys. To help guide applications in selecting a suitable strong

SecureRandom

implementation, Java distributions
include a list of known strong

SecureRandom

implementations in the

securerandom.strongAlgorithms

Security property.

Every implementation of the Java platform is required to
support at least one strong

SecureRandom

implementation.

**Returns:** a strong

SecureRandom

implementation as indicated
by the

securerandom.strongAlgorithms

Security property
**Throws:** NoSuchAlgorithmException

- if no algorithm is available
**Since:** 1.8
**See Also:** Security.getProperty(String)

---

#### getInstanceStrong

public static

SecureRandom

getInstanceStrong()
throws

NoSuchAlgorithmException

Returns a

SecureRandom

object that was selected by using
the algorithms/providers specified in the

securerandom.strongAlgorithms

Security

property.

Some situations require strong random values, such as when
creating high-value/long-lived secrets like RSA public/private
keys. To help guide applications in selecting a suitable strong

SecureRandom

implementation, Java distributions
include a list of known strong

SecureRandom

implementations in the

securerandom.strongAlgorithms

Security property.

Every implementation of the Java platform is required to
support at least one strong

SecureRandom

implementation.

Some situations require strong random values, such as when
creating high-value/long-lived secrets like RSA public/private
keys. To help guide applications in selecting a suitable strong

SecureRandom

implementation, Java distributions
include a list of known strong

SecureRandom

implementations in the

securerandom.strongAlgorithms

Security property.

Every implementation of the Java platform is required to
support at least one strong

SecureRandom

implementation.

Every implementation of the Java platform is required to
support at least one strong

SecureRandom

implementation.

reseed

```java
public void reseed()
```

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.
**Since:** 9

---

#### reseed

public void reseed()

Reseeds this

SecureRandom

with entropy input read from its
entropy source.

reseed

```java
public void reseed​(
SecureRandomParameters
params)
```

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

Note that entropy is obtained from an entropy source. While
some data in

params

may contain entropy, its main usage is to
provide diversity.

**Parameters:** params

- extra parameters
**Throws:** UnsupportedOperationException

- if the underlying provider
implementation has not overridden this method.
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

---

#### reseed

public void reseed​(

SecureRandomParameters

params)

Reseeds this

SecureRandom

with entropy input read from its
entropy source with additional parameters.

Note that entropy is obtained from an entropy source. While
some data in

params

may contain entropy, its main usage is to
provide diversity.

Note that entropy is obtained from an entropy source. While
some data in

params

may contain entropy, its main usage is to
provide diversity.

---

