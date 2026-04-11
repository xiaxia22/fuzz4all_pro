# Class AlgorithmParameters

**Source:** `java.base\java\security\AlgorithmParameters.html`

### Class Description

```java
public class
AlgorithmParameters

extends
Object
```

This class is used as an opaque representation of cryptographic parameters.

An

AlgorithmParameters

object for managing the parameters
for a particular algorithm can be obtained by
calling one of the

getInstance

factory methods
(static methods that return instances of a given class).

Once an

AlgorithmParameters

object is obtained, it must be
initialized via a call to

init

, using an appropriate parameter
specification or parameter encoding.

A transparent parameter specification is obtained from an

AlgorithmParameters

object via a call to

getParameterSpec

, and a byte encoding of the parameters is
obtained via a call to

getEncoded

.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameters

algorithms:

- AES
- DES
- DESede
- DiffieHellman
- DSA

These algorithms are described in the

AlgorithmParameters section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.2
**See Also:** AlgorithmParameterSpec

,

DSAParameterSpec

,

KeyPairGenerator

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AlgorithmParameters​(
AlgorithmParametersSpi
paramSpi,

Provider
provider,

String
algorithm)

Creates an AlgorithmParameters object.

**Parameters:**
- paramSpi

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

Returns the name of the algorithm associated with this parameter object.

**Returns:**
- the algorithm name.

---

#### public static
AlgorithmParameters
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a parameter object for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:**
- algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new parameter object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParametersSpi

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
AlgorithmParameters
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:**
- algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new parameter object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty
- NoSuchAlgorithmException

- if an

AlgorithmParametersSpi

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
AlgorithmParameters
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:**
- algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new parameter object

**Throws:**
- IllegalArgumentException

- if the provider is

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

Returns the provider of this parameter object.

**Returns:**
- the provider of this parameter object

---

#### public final void init​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException

Initializes this parameter object using the parameters
specified in

paramSpec

.

**Parameters:**
- paramSpec

- the parameter specification.

**Throws:**
- InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object, or if this parameter object has already been initialized.

---

#### public final void init​(byte[] params)
throws
IOException

Imports the specified parameters and decodes them according to the
primary decoding format for parameters. The primary decoding
format for parameters is ASN.1, if an ASN.1 specification for this type
of parameters exists.

**Parameters:**
- params

- the encoded parameters.

**Throws:**
- IOException

- on decoding errors, or if this parameter object
has already been initialized.

---

#### public final void init​(byte[] params,

String
format)
throws
IOException

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:**
- params

- the encoded parameters.
- format

- the name of the decoding scheme.

**Throws:**
- IOException

- on decoding errors, or if this parameter object
has already been initialized.

---

#### public final <T extends
AlgorithmParameterSpec
> T getParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException

Returns a (transparent) specification of this parameter object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Parameters:**
- paramSpec

- the specification class in which
the parameters should be returned.

**Returns:**
- the parameter specification.

**Throws:**
- InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object, or if this
parameter object has not been initialized.

**Type Parameters:**
- T

- the type of the parameter specification to be returrned

---

#### public final byte[] getEncoded()
throws
IOException

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:**
- the parameters encoded using their primary encoding format.

**Throws:**
- IOException

- on encoding errors, or if this parameter object
has not been initialized.

---

#### public final byte[] getEncoded​(
String
format)
throws
IOException

Returns the parameters encoded in the specified scheme.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:**
- format

- the name of the encoding format.

**Returns:**
- the parameters encoded using the specified encoding scheme.

**Throws:**
- IOException

- on encoding errors, or if this parameter object
has not been initialized.

---

#### public final
String
toString()

Returns a formatted string describing the parameters.

**Overrides:**
- toString

in class

Object

**Returns:**
- a formatted string describing the parameters, or null if this
parameter object has not been initialized.

---

### Additional Sections

#### Class AlgorithmParameters

java.lang.Object

- java.security.AlgorithmParameters

java.security.AlgorithmParameters

```java
public class
AlgorithmParameters

extends
Object
```

This class is used as an opaque representation of cryptographic parameters.

An

AlgorithmParameters

object for managing the parameters
for a particular algorithm can be obtained by
calling one of the

getInstance

factory methods
(static methods that return instances of a given class).

Once an

AlgorithmParameters

object is obtained, it must be
initialized via a call to

init

, using an appropriate parameter
specification or parameter encoding.

A transparent parameter specification is obtained from an

AlgorithmParameters

object via a call to

getParameterSpec

, and a byte encoding of the parameters is
obtained via a call to

getEncoded

.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameters

algorithms:

- AES
- DES
- DESede
- DiffieHellman
- DSA

These algorithms are described in the

AlgorithmParameters section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.2
**See Also:** AlgorithmParameterSpec

,

DSAParameterSpec

,

KeyPairGenerator

public class

AlgorithmParameters

extends

Object

This class is used as an opaque representation of cryptographic parameters.

An

AlgorithmParameters

object for managing the parameters
for a particular algorithm can be obtained by
calling one of the

getInstance

factory methods
(static methods that return instances of a given class).

Once an

AlgorithmParameters

object is obtained, it must be
initialized via a call to

init

, using an appropriate parameter
specification or parameter encoding.

A transparent parameter specification is obtained from an

AlgorithmParameters

object via a call to

getParameterSpec

, and a byte encoding of the parameters is
obtained via a call to

getEncoded

.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameters

algorithms:

- AES
- DES
- DESede
- DiffieHellman
- DSA

These algorithms are described in the

AlgorithmParameters section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

An

AlgorithmParameters

object for managing the parameters
for a particular algorithm can be obtained by
calling one of the

getInstance

factory methods
(static methods that return instances of a given class).

Once an

AlgorithmParameters

object is obtained, it must be
initialized via a call to

init

, using an appropriate parameter
specification or parameter encoding.

A transparent parameter specification is obtained from an

AlgorithmParameters

object via a call to

getParameterSpec

, and a byte encoding of the parameters is
obtained via a call to

getEncoded

.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameters

algorithms:

- AES
- DES
- DESede
- DiffieHellman
- DSA

These algorithms are described in the

AlgorithmParameters section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Once an

AlgorithmParameters

object is obtained, it must be
initialized via a call to

init

, using an appropriate parameter
specification or parameter encoding.

A transparent parameter specification is obtained from an

AlgorithmParameters

object via a call to

getParameterSpec

, and a byte encoding of the parameters is
obtained via a call to

getEncoded

.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameters

algorithms:

- AES
- DES
- DESede
- DiffieHellman
- DSA

These algorithms are described in the

AlgorithmParameters section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

A transparent parameter specification is obtained from an

AlgorithmParameters

object via a call to

getParameterSpec

, and a byte encoding of the parameters is
obtained via a call to

getEncoded

.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameters

algorithms:

- AES
- DES
- DESede
- DiffieHellman
- DSA

These algorithms are described in the

AlgorithmParameters section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support the
following standard

AlgorithmParameters

algorithms:

- AES
- DES
- DESede
- DiffieHellman
- DSA

These algorithms are described in the

AlgorithmParameters section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

AES

DES

DESede

DiffieHellman

DSA

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AlgorithmParameters

​(

AlgorithmParametersSpi

paramSpi,

Provider

provider,

String

algorithm)

Creates an AlgorithmParameters object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the name of the algorithm associated with this parameter object.

byte[]

getEncoded

()

Returns the parameters in their primary encoding format.

byte[]

getEncoded

​(

String

format)

Returns the parameters encoded in the specified scheme.

static

AlgorithmParameters

getInstance

​(

String

algorithm)

Returns a parameter object for the specified algorithm.

static

AlgorithmParameters

getInstance

​(

String

algorithm,

String

provider)

Returns a parameter object for the specified algorithm.

static

AlgorithmParameters

getInstance

​(

String

algorithm,

Provider

provider)

Returns a parameter object for the specified algorithm.

<T extends

AlgorithmParameterSpec

>

T

getParameterSpec

​(

Class

<T> paramSpec)

Returns a (transparent) specification of this parameter object.

Provider

getProvider

()

Returns the provider of this parameter object.

void

init

​(byte[] params)

Imports the specified parameters and decodes them according to the
primary decoding format for parameters.

void

init

​(byte[] params,

String

format)

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.

void

init

​(

AlgorithmParameterSpec

paramSpec)

Initializes this parameter object using the parameters
specified in

paramSpec

.

String

toString

()

Returns a formatted string describing the parameters.

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

protected

AlgorithmParameters

​(

AlgorithmParametersSpi

paramSpi,

Provider

provider,

String

algorithm)

Creates an AlgorithmParameters object.

---

#### Constructor Summary

Creates an AlgorithmParameters object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the name of the algorithm associated with this parameter object.

byte[]

getEncoded

()

Returns the parameters in their primary encoding format.

byte[]

getEncoded

​(

String

format)

Returns the parameters encoded in the specified scheme.

static

AlgorithmParameters

getInstance

​(

String

algorithm)

Returns a parameter object for the specified algorithm.

static

AlgorithmParameters

getInstance

​(

String

algorithm,

String

provider)

Returns a parameter object for the specified algorithm.

static

AlgorithmParameters

getInstance

​(

String

algorithm,

Provider

provider)

Returns a parameter object for the specified algorithm.

<T extends

AlgorithmParameterSpec

>

T

getParameterSpec

​(

Class

<T> paramSpec)

Returns a (transparent) specification of this parameter object.

Provider

getProvider

()

Returns the provider of this parameter object.

void

init

​(byte[] params)

Imports the specified parameters and decodes them according to the
primary decoding format for parameters.

void

init

​(byte[] params,

String

format)

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.

void

init

​(

AlgorithmParameterSpec

paramSpec)

Initializes this parameter object using the parameters
specified in

paramSpec

.

String

toString

()

Returns a formatted string describing the parameters.

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

Returns the name of the algorithm associated with this parameter object.

Returns the parameters in their primary encoding format.

Returns the parameters encoded in the specified scheme.

Returns a parameter object for the specified algorithm.

Returns a (transparent) specification of this parameter object.

Returns the provider of this parameter object.

Imports the specified parameters and decodes them according to the
primary decoding format for parameters.

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.

Initializes this parameter object using the parameters
specified in

paramSpec

.

Returns a formatted string describing the parameters.

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

- AlgorithmParameters

```java
protected AlgorithmParameters​(
AlgorithmParametersSpi
paramSpi,

Provider
provider,

String
algorithm)
```

Creates an AlgorithmParameters object.

**Parameters:** paramSpi

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

Returns the name of the algorithm associated with this parameter object.

**Returns:** the algorithm name.

- getInstance

```java
public static
AlgorithmParameters
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a parameter object for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new parameter object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParametersSpi

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
AlgorithmParameters
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

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new parameter object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParametersSpi

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
AlgorithmParameters
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new parameter object
**Throws:** IllegalArgumentException

- if the provider is

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

Returns the provider of this parameter object.

**Returns:** the provider of this parameter object

- init

```java
public final void init​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException
```

Initializes this parameter object using the parameters
specified in

paramSpec

.

**Parameters:** paramSpec

- the parameter specification.
**Throws:** InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object, or if this parameter object has already been initialized.

- init

```java
public final void init​(byte[] params)
throws
IOException
```

Imports the specified parameters and decodes them according to the
primary decoding format for parameters. The primary decoding
format for parameters is ASN.1, if an ASN.1 specification for this type
of parameters exists.

**Parameters:** params

- the encoded parameters.
**Throws:** IOException

- on decoding errors, or if this parameter object
has already been initialized.

- init

```java
public final void init​(byte[] params,

String
format)
throws
IOException
```

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** params

- the encoded parameters.
**Parameters:** format

- the name of the decoding scheme.
**Throws:** IOException

- on decoding errors, or if this parameter object
has already been initialized.

- getParameterSpec

```java
public final <T extends
AlgorithmParameterSpec
> T getParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException
```

Returns a (transparent) specification of this parameter object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Type Parameters:** T

- the type of the parameter specification to be returrned
**Parameters:** paramSpec

- the specification class in which
the parameters should be returned.
**Returns:** the parameter specification.
**Throws:** InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object, or if this
parameter object has not been initialized.

- getEncoded

```java
public final byte[] getEncoded()
throws
IOException
```

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:** the parameters encoded using their primary encoding format.
**Throws:** IOException

- on encoding errors, or if this parameter object
has not been initialized.

- getEncoded

```java
public final byte[] getEncoded​(
String
format)
throws
IOException
```

Returns the parameters encoded in the specified scheme.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** format

- the name of the encoding format.
**Returns:** the parameters encoded using the specified encoding scheme.
**Throws:** IOException

- on encoding errors, or if this parameter object
has not been initialized.

- toString

```java
public final
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters, or null if this
parameter object has not been initialized.

Constructor Detail

- AlgorithmParameters

```java
protected AlgorithmParameters​(
AlgorithmParametersSpi
paramSpi,

Provider
provider,

String
algorithm)
```

Creates an AlgorithmParameters object.

**Parameters:** paramSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Constructor Detail

AlgorithmParameters

```java
protected AlgorithmParameters​(
AlgorithmParametersSpi
paramSpi,

Provider
provider,

String
algorithm)
```

Creates an AlgorithmParameters object.

**Parameters:** paramSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### AlgorithmParameters

protected AlgorithmParameters​(

AlgorithmParametersSpi

paramSpi,

Provider

provider,

String

algorithm)

Creates an AlgorithmParameters object.

Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the name of the algorithm associated with this parameter object.

**Returns:** the algorithm name.

- getInstance

```java
public static
AlgorithmParameters
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a parameter object for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new parameter object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParametersSpi

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
AlgorithmParameters
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

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new parameter object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParametersSpi

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
AlgorithmParameters
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new parameter object
**Throws:** IllegalArgumentException

- if the provider is

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

Returns the provider of this parameter object.

**Returns:** the provider of this parameter object

- init

```java
public final void init​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException
```

Initializes this parameter object using the parameters
specified in

paramSpec

.

**Parameters:** paramSpec

- the parameter specification.
**Throws:** InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object, or if this parameter object has already been initialized.

- init

```java
public final void init​(byte[] params)
throws
IOException
```

Imports the specified parameters and decodes them according to the
primary decoding format for parameters. The primary decoding
format for parameters is ASN.1, if an ASN.1 specification for this type
of parameters exists.

**Parameters:** params

- the encoded parameters.
**Throws:** IOException

- on decoding errors, or if this parameter object
has already been initialized.

- init

```java
public final void init​(byte[] params,

String
format)
throws
IOException
```

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** params

- the encoded parameters.
**Parameters:** format

- the name of the decoding scheme.
**Throws:** IOException

- on decoding errors, or if this parameter object
has already been initialized.

- getParameterSpec

```java
public final <T extends
AlgorithmParameterSpec
> T getParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException
```

Returns a (transparent) specification of this parameter object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Type Parameters:** T

- the type of the parameter specification to be returrned
**Parameters:** paramSpec

- the specification class in which
the parameters should be returned.
**Returns:** the parameter specification.
**Throws:** InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object, or if this
parameter object has not been initialized.

- getEncoded

```java
public final byte[] getEncoded()
throws
IOException
```

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:** the parameters encoded using their primary encoding format.
**Throws:** IOException

- on encoding errors, or if this parameter object
has not been initialized.

- getEncoded

```java
public final byte[] getEncoded​(
String
format)
throws
IOException
```

Returns the parameters encoded in the specified scheme.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** format

- the name of the encoding format.
**Returns:** the parameters encoded using the specified encoding scheme.
**Throws:** IOException

- on encoding errors, or if this parameter object
has not been initialized.

- toString

```java
public final
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters, or null if this
parameter object has not been initialized.

---

#### Method Detail

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the name of the algorithm associated with this parameter object.

**Returns:** the algorithm name.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the name of the algorithm associated with this parameter object.

getInstance

```java
public static
AlgorithmParameters
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a parameter object for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new parameter object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

AlgorithmParametersSpi

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

AlgorithmParameters

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a parameter object for the specified algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

getInstance

```java
public static
AlgorithmParameters
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

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new parameter object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

AlgorithmParametersSpi

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

AlgorithmParameters

getInstance​(

String

algorithm,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

getInstance

```java
public static
AlgorithmParameters
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

**Parameters:** algorithm

- the name of the algorithm requested.
See the AlgorithmParameters section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new parameter object
**Throws:** IllegalArgumentException

- if the provider is

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

AlgorithmParameters

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a parameter object for the specified algorithm.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

A new AlgorithmParameters object encapsulating the
AlgorithmParametersSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

The returned parameter object must be initialized via a call to

init

, using an appropriate parameter specification or
parameter encoding.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this parameter object.

**Returns:** the provider of this parameter object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this parameter object.

init

```java
public final void init​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException
```

Initializes this parameter object using the parameters
specified in

paramSpec

.

**Parameters:** paramSpec

- the parameter specification.
**Throws:** InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object, or if this parameter object has already been initialized.

---

#### init

public final void init​(

AlgorithmParameterSpec

paramSpec)
throws

InvalidParameterSpecException

Initializes this parameter object using the parameters
specified in

paramSpec

.

init

```java
public final void init​(byte[] params)
throws
IOException
```

Imports the specified parameters and decodes them according to the
primary decoding format for parameters. The primary decoding
format for parameters is ASN.1, if an ASN.1 specification for this type
of parameters exists.

**Parameters:** params

- the encoded parameters.
**Throws:** IOException

- on decoding errors, or if this parameter object
has already been initialized.

---

#### init

public final void init​(byte[] params)
throws

IOException

Imports the specified parameters and decodes them according to the
primary decoding format for parameters. The primary decoding
format for parameters is ASN.1, if an ASN.1 specification for this type
of parameters exists.

init

```java
public final void init​(byte[] params,

String
format)
throws
IOException
```

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** params

- the encoded parameters.
**Parameters:** format

- the name of the decoding scheme.
**Throws:** IOException

- on decoding errors, or if this parameter object
has already been initialized.

---

#### init

public final void init​(byte[] params,

String

format)
throws

IOException

Imports the parameters from

params

and decodes them
according to the specified decoding scheme.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

getParameterSpec

```java
public final <T extends
AlgorithmParameterSpec
> T getParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException
```

Returns a (transparent) specification of this parameter object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Type Parameters:** T

- the type of the parameter specification to be returrned
**Parameters:** paramSpec

- the specification class in which
the parameters should be returned.
**Returns:** the parameter specification.
**Throws:** InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object, or if this
parameter object has not been initialized.

---

#### getParameterSpec

public final <T extends

AlgorithmParameterSpec

> T getParameterSpec​(

Class

<T> paramSpec)
throws

InvalidParameterSpecException

Returns a (transparent) specification of this parameter object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

getEncoded

```java
public final byte[] getEncoded()
throws
IOException
```

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:** the parameters encoded using their primary encoding format.
**Throws:** IOException

- on encoding errors, or if this parameter object
has not been initialized.

---

#### getEncoded

public final byte[] getEncoded()
throws

IOException

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

getEncoded

```java
public final byte[] getEncoded​(
String
format)
throws
IOException
```

Returns the parameters encoded in the specified scheme.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** format

- the name of the encoding format.
**Returns:** the parameters encoded using the specified encoding scheme.
**Throws:** IOException

- on encoding errors, or if this parameter object
has not been initialized.

---

#### getEncoded

public final byte[] getEncoded​(

String

format)
throws

IOException

Returns the parameters encoded in the specified scheme.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

toString

```java
public final
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters, or null if this
parameter object has not been initialized.

---

#### toString

public final

String

toString()

Returns a formatted string describing the parameters.

---

