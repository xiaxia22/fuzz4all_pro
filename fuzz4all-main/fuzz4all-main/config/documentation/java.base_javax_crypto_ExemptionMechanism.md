# Class ExemptionMechanism

**Source:** `java.base\javax\crypto\ExemptionMechanism.html`

### Class Description

```java
public class
ExemptionMechanism

extends
Object
```

This class provides the functionality of an exemption mechanism, examples
of which are

key recovery

,

key weakening

, and

key escrow

.

Applications or applets that use an exemption mechanism may be granted
stronger encryption capabilities than those which don't.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ExemptionMechanism​(
ExemptionMechanismSpi
exmechSpi,

Provider
provider,

String
mechanism)

Creates a ExemptionMechanism object.

**Parameters:**
- exmechSpi

- the delegate
- provider

- the provider
- mechanism

- the exemption mechanism

---

### Method Details

#### public final
String
getName()

Returns the exemption mechanism name of this

ExemptionMechanism

object.

This is the same name that was specified in one of the

getInstance

calls that created this

ExemptionMechanism

object.

**Returns:**
- the exemption mechanism name of this

ExemptionMechanism

object.

---

#### public static final
ExemptionMechanism
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested exemption
mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.

**Returns:**
- the new

ExemptionMechanism

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports an

ExemptionMechanismSpi

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
ExemptionMechanism
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
- provider

- the name of the provider.

**Returns:**
- the new

ExemptionMechanism

object

**Throws:**
- IllegalArgumentException

- if the

provider

is

null

or empty
- NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

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
ExemptionMechanism
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
- provider

- the provider.

**Returns:**
- the new

ExemptionMechanism

object

**Throws:**
- IllegalArgumentException

- if the

provider

is null
- NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

implementation for the specified algorithm is not available
from the specified

Provider object
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

ExemptionMechanism

object.

**Returns:**
- the provider of this

ExemptionMechanism

object.

---

#### public final boolean isCryptoAllowed​(
Key
key)
throws
ExemptionMechanismException

Returns whether the result blob has been generated successfully by this
exemption mechanism.

The method also makes sure that the key passed in is the same as
the one this exemption mechanism used in initializing and generating
phases.

**Parameters:**
- key

- the key the crypto is going to use.

**Returns:**
- whether the result blob of the same key has been generated
successfully by this exemption mechanism; false if

key

is null.

**Throws:**
- ExemptionMechanismException

- if problem(s) encountered
while determining whether the result blob has been generated successfully
by this exemption mechanism object.

---

#### public final int getOutputSize​(int inputLen)
throws
IllegalStateException

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

genExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:**
- inputLen

- the input length (in bytes)

**Returns:**
- the required output buffer size (in bytes)

**Throws:**
- IllegalStateException

- if this exemption mechanism is in a
wrong state (e.g., has not yet been initialized)

---

#### public final void init​(
Key
key)
throws
InvalidKeyException
,

ExemptionMechanismException

Initializes this exemption mechanism with a key.

If this exemption mechanism requires any algorithm parameters
that cannot be derived from the given

key

, the
underlying exemption mechanism implementation is supposed to
generate the required parameters itself (using provider-specific
default values); in the case that algorithm parameters must be
specified by the caller, an

InvalidKeyException

is raised.

**Parameters:**
- key

- the key for this exemption mechanism

**Throws:**
- InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
- ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

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
,

ExemptionMechanismException

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption
mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:**
- key

- the key for this exemption mechanism
- params

- the algorithm parameters

**Throws:**
- InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
- InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
- ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

---

#### public final void init​(
Key
key,

AlgorithmParameters
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
,

ExemptionMechanismException

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters itself
(using provider-specific default values); in the case that algorithm
parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:**
- key

- the key for this exemption mechanism
- params

- the algorithm parameters

**Throws:**
- InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
- InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
- ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

---

#### public final byte[] genExemptionBlob()
throws
IllegalStateException
,

ExemptionMechanismException

Generates the exemption mechanism key blob.

**Returns:**
- the new buffer with the result key blob.

**Throws:**
- IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
- ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### public final int genExemptionBlob​(byte[] output)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:**
- output

- the buffer for the result

**Returns:**
- the number of bytes stored in

output

**Throws:**
- IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
- ShortBufferException

- if the given output buffer is too small
to hold the result.
- ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### public final int genExemptionBlob​(byte[] output,
int outputOffset)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:**
- output

- the buffer for the result
- outputOffset

- the offset in

output

where the result
is stored

**Returns:**
- the number of bytes stored in

output

**Throws:**
- IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
- ShortBufferException

- if the given output buffer is too small
to hold the result.
- ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

### Additional Sections

#### Class ExemptionMechanism

java.lang.Object

- javax.crypto.ExemptionMechanism

javax.crypto.ExemptionMechanism

```java
public class
ExemptionMechanism

extends
Object
```

This class provides the functionality of an exemption mechanism, examples
of which are

key recovery

,

key weakening

, and

key escrow

.

Applications or applets that use an exemption mechanism may be granted
stronger encryption capabilities than those which don't.

**Since:** 1.4

public class

ExemptionMechanism

extends

Object

This class provides the functionality of an exemption mechanism, examples
of which are

key recovery

,

key weakening

, and

key escrow

.

Applications or applets that use an exemption mechanism may be granted
stronger encryption capabilities than those which don't.

Applications or applets that use an exemption mechanism may be granted
stronger encryption capabilities than those which don't.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ExemptionMechanism

​(

ExemptionMechanismSpi

exmechSpi,

Provider

provider,

String

mechanism)

Creates a ExemptionMechanism object.

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

genExemptionBlob

()

Generates the exemption mechanism key blob.

int

genExemptionBlob

​(byte[] output)

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

int

genExemptionBlob

​(byte[] output,
int outputOffset)

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

static

ExemptionMechanism

getInstance

​(

String

algorithm)

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

static

ExemptionMechanism

getInstance

​(

String

algorithm,

String

provider)

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

static

ExemptionMechanism

getInstance

​(

String

algorithm,

Provider

provider)

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

String

getName

()

Returns the exemption mechanism name of this

ExemptionMechanism

object.

int

getOutputSize

​(int inputLen)

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

Provider

getProvider

()

Returns the provider of this

ExemptionMechanism

object.

void

init

​(

Key

key)

Initializes this exemption mechanism with a key.

void

init

​(

Key

key,

AlgorithmParameters

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

void

init

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

boolean

isCryptoAllowed

​(

Key

key)

Returns whether the result blob has been generated successfully by this
exemption mechanism.

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

ExemptionMechanism

​(

ExemptionMechanismSpi

exmechSpi,

Provider

provider,

String

mechanism)

Creates a ExemptionMechanism object.

---

#### Constructor Summary

Creates a ExemptionMechanism object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

genExemptionBlob

()

Generates the exemption mechanism key blob.

int

genExemptionBlob

​(byte[] output)

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

int

genExemptionBlob

​(byte[] output,
int outputOffset)

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

static

ExemptionMechanism

getInstance

​(

String

algorithm)

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

static

ExemptionMechanism

getInstance

​(

String

algorithm,

String

provider)

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

static

ExemptionMechanism

getInstance

​(

String

algorithm,

Provider

provider)

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

String

getName

()

Returns the exemption mechanism name of this

ExemptionMechanism

object.

int

getOutputSize

​(int inputLen)

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

Provider

getProvider

()

Returns the provider of this

ExemptionMechanism

object.

void

init

​(

Key

key)

Initializes this exemption mechanism with a key.

void

init

​(

Key

key,

AlgorithmParameters

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

void

init

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

boolean

isCryptoAllowed

​(

Key

key)

Returns whether the result blob has been generated successfully by this
exemption mechanism.

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

Generates the exemption mechanism key blob.

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

Returns the exemption mechanism name of this

ExemptionMechanism

object.

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

Returns the provider of this

ExemptionMechanism

object.

Initializes this exemption mechanism with a key.

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

Returns whether the result blob has been generated successfully by this
exemption mechanism.

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

- ExemptionMechanism

```java
protected ExemptionMechanism​(
ExemptionMechanismSpi
exmechSpi,

Provider
provider,

String
mechanism)
```

Creates a ExemptionMechanism object.

**Parameters:** exmechSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** mechanism

- the exemption mechanism

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public final
String
getName()
```

Returns the exemption mechanism name of this

ExemptionMechanism

object.

This is the same name that was specified in one of the

getInstance

calls that created this

ExemptionMechanism

object.

**Returns:** the exemption mechanism name of this

ExemptionMechanism

object.

- getInstance

```java
public static final
ExemptionMechanism
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the first
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

- the standard name of the requested exemption
mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Returns:** the new

ExemptionMechanism

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

ExemptionMechanismSpi

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
ExemptionMechanism
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

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

ExemptionMechanism

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

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
ExemptionMechanism
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Parameters:** provider

- the provider.
**Returns:** the new

ExemptionMechanism

object
**Throws:** IllegalArgumentException

- if the

provider

is null
**Throws:** NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

implementation for the specified algorithm is not available
from the specified

Provider object
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

ExemptionMechanism

object.

**Returns:** the provider of this

ExemptionMechanism

object.

- isCryptoAllowed

```java
public final boolean isCryptoAllowed​(
Key
key)
throws
ExemptionMechanismException
```

Returns whether the result blob has been generated successfully by this
exemption mechanism.

The method also makes sure that the key passed in is the same as
the one this exemption mechanism used in initializing and generating
phases.

**Parameters:** key

- the key the crypto is going to use.
**Returns:** whether the result blob of the same key has been generated
successfully by this exemption mechanism; false if

key

is null.
**Throws:** ExemptionMechanismException

- if problem(s) encountered
while determining whether the result blob has been generated successfully
by this exemption mechanism object.

- getOutputSize

```java
public final int getOutputSize​(int inputLen)
throws
IllegalStateException
```

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

genExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:** inputLen

- the input length (in bytes)
**Returns:** the required output buffer size (in bytes)
**Throws:** IllegalStateException

- if this exemption mechanism is in a
wrong state (e.g., has not yet been initialized)

- init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key.

If this exemption mechanism requires any algorithm parameters
that cannot be derived from the given

key

, the
underlying exemption mechanism implementation is supposed to
generate the required parameters itself (using provider-specific
default values); in the case that algorithm parameters must be
specified by the caller, an

InvalidKeyException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

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
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption
mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Parameters:** params

- the algorithm parameters
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

- init

```java
public final void init​(
Key
key,

AlgorithmParameters
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters itself
(using provider-specific default values); in the case that algorithm
parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Parameters:** params

- the algorithm parameters
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

- genExemptionBlob

```java
public final byte[] genExemptionBlob()
throws
IllegalStateException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob.

**Returns:** the new buffer with the result key blob.
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

- genExemptionBlob

```java
public final int genExemptionBlob​(byte[] output)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:** output

- the buffer for the result
**Returns:** the number of bytes stored in

output
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

- genExemptionBlob

```java
public final int genExemptionBlob​(byte[] output,
int outputOffset)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:** output

- the buffer for the result
**Parameters:** outputOffset

- the offset in

output

where the result
is stored
**Returns:** the number of bytes stored in

output
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

Constructor Detail

- ExemptionMechanism

```java
protected ExemptionMechanism​(
ExemptionMechanismSpi
exmechSpi,

Provider
provider,

String
mechanism)
```

Creates a ExemptionMechanism object.

**Parameters:** exmechSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** mechanism

- the exemption mechanism

---

#### Constructor Detail

ExemptionMechanism

```java
protected ExemptionMechanism​(
ExemptionMechanismSpi
exmechSpi,

Provider
provider,

String
mechanism)
```

Creates a ExemptionMechanism object.

**Parameters:** exmechSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** mechanism

- the exemption mechanism

---

#### ExemptionMechanism

protected ExemptionMechanism​(

ExemptionMechanismSpi

exmechSpi,

Provider

provider,

String

mechanism)

Creates a ExemptionMechanism object.

Method Detail

- getName

```java
public final
String
getName()
```

Returns the exemption mechanism name of this

ExemptionMechanism

object.

This is the same name that was specified in one of the

getInstance

calls that created this

ExemptionMechanism

object.

**Returns:** the exemption mechanism name of this

ExemptionMechanism

object.

- getInstance

```java
public static final
ExemptionMechanism
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the first
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

- the standard name of the requested exemption
mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Returns:** the new

ExemptionMechanism

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

ExemptionMechanismSpi

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
ExemptionMechanism
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

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

ExemptionMechanism

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

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
ExemptionMechanism
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Parameters:** provider

- the provider.
**Returns:** the new

ExemptionMechanism

object
**Throws:** IllegalArgumentException

- if the

provider

is null
**Throws:** NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

implementation for the specified algorithm is not available
from the specified

Provider object
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

ExemptionMechanism

object.

**Returns:** the provider of this

ExemptionMechanism

object.

- isCryptoAllowed

```java
public final boolean isCryptoAllowed​(
Key
key)
throws
ExemptionMechanismException
```

Returns whether the result blob has been generated successfully by this
exemption mechanism.

The method also makes sure that the key passed in is the same as
the one this exemption mechanism used in initializing and generating
phases.

**Parameters:** key

- the key the crypto is going to use.
**Returns:** whether the result blob of the same key has been generated
successfully by this exemption mechanism; false if

key

is null.
**Throws:** ExemptionMechanismException

- if problem(s) encountered
while determining whether the result blob has been generated successfully
by this exemption mechanism object.

- getOutputSize

```java
public final int getOutputSize​(int inputLen)
throws
IllegalStateException
```

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

genExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:** inputLen

- the input length (in bytes)
**Returns:** the required output buffer size (in bytes)
**Throws:** IllegalStateException

- if this exemption mechanism is in a
wrong state (e.g., has not yet been initialized)

- init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key.

If this exemption mechanism requires any algorithm parameters
that cannot be derived from the given

key

, the
underlying exemption mechanism implementation is supposed to
generate the required parameters itself (using provider-specific
default values); in the case that algorithm parameters must be
specified by the caller, an

InvalidKeyException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

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
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption
mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Parameters:** params

- the algorithm parameters
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

- init

```java
public final void init​(
Key
key,

AlgorithmParameters
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters itself
(using provider-specific default values); in the case that algorithm
parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Parameters:** params

- the algorithm parameters
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

- genExemptionBlob

```java
public final byte[] genExemptionBlob()
throws
IllegalStateException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob.

**Returns:** the new buffer with the result key blob.
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

- genExemptionBlob

```java
public final int genExemptionBlob​(byte[] output)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:** output

- the buffer for the result
**Returns:** the number of bytes stored in

output
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

- genExemptionBlob

```java
public final int genExemptionBlob​(byte[] output,
int outputOffset)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:** output

- the buffer for the result
**Parameters:** outputOffset

- the offset in

output

where the result
is stored
**Returns:** the number of bytes stored in

output
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### Method Detail

getName

```java
public final
String
getName()
```

Returns the exemption mechanism name of this

ExemptionMechanism

object.

This is the same name that was specified in one of the

getInstance

calls that created this

ExemptionMechanism

object.

**Returns:** the exemption mechanism name of this

ExemptionMechanism

object.

---

#### getName

public final

String

getName()

Returns the exemption mechanism name of this

ExemptionMechanism

object.

This is the same name that was specified in one of the

getInstance

calls that created this

ExemptionMechanism

object.

This is the same name that was specified in one of the

getInstance

calls that created this

ExemptionMechanism

object.

getInstance

```java
public static final
ExemptionMechanism
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the first
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

- the standard name of the requested exemption
mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Returns:** the new

ExemptionMechanism

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports an

ExemptionMechanismSpi

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

ExemptionMechanism

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the first
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
ExemptionMechanism
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

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

ExemptionMechanism

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

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

ExemptionMechanism

getInstance​(

String

algorithm,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified provider
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
ExemptionMechanism
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested exemption mechanism.
See the ExemptionMechanism section in the

Java Security Standard Algorithm Names Specification

for information about standard exemption mechanism names.
**Parameters:** provider

- the provider.
**Returns:** the new

ExemptionMechanism

object
**Throws:** IllegalArgumentException

- if the

provider

is null
**Throws:** NoSuchAlgorithmException

- if an

ExemptionMechanismSpi

implementation for the specified algorithm is not available
from the specified

Provider object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

ExemptionMechanism

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns an

ExemptionMechanism

object that implements the
specified exemption mechanism algorithm.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new ExemptionMechanism object encapsulating the
ExemptionMechanismSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

ExemptionMechanism

object.

**Returns:** the provider of this

ExemptionMechanism

object.

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

ExemptionMechanism

object.

isCryptoAllowed

```java
public final boolean isCryptoAllowed​(
Key
key)
throws
ExemptionMechanismException
```

Returns whether the result blob has been generated successfully by this
exemption mechanism.

The method also makes sure that the key passed in is the same as
the one this exemption mechanism used in initializing and generating
phases.

**Parameters:** key

- the key the crypto is going to use.
**Returns:** whether the result blob of the same key has been generated
successfully by this exemption mechanism; false if

key

is null.
**Throws:** ExemptionMechanismException

- if problem(s) encountered
while determining whether the result blob has been generated successfully
by this exemption mechanism object.

---

#### isCryptoAllowed

public final boolean isCryptoAllowed​(

Key

key)
throws

ExemptionMechanismException

Returns whether the result blob has been generated successfully by this
exemption mechanism.

The method also makes sure that the key passed in is the same as
the one this exemption mechanism used in initializing and generating
phases.

The method also makes sure that the key passed in is the same as
the one this exemption mechanism used in initializing and generating
phases.

getOutputSize

```java
public final int getOutputSize​(int inputLen)
throws
IllegalStateException
```

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

genExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:** inputLen

- the input length (in bytes)
**Returns:** the required output buffer size (in bytes)
**Throws:** IllegalStateException

- if this exemption mechanism is in a
wrong state (e.g., has not yet been initialized)

---

#### getOutputSize

public final int getOutputSize​(int inputLen)
throws

IllegalStateException

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

genExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

genExemptionBlob

call may be smaller than the length returned by this method.

The actual output length of the next

genExemptionBlob

call may be smaller than the length returned by this method.

init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key.

If this exemption mechanism requires any algorithm parameters
that cannot be derived from the given

key

, the
underlying exemption mechanism implementation is supposed to
generate the required parameters itself (using provider-specific
default values); in the case that algorithm parameters must be
specified by the caller, an

InvalidKeyException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

---

#### init

public final void init​(

Key

key)
throws

InvalidKeyException

,

ExemptionMechanismException

Initializes this exemption mechanism with a key.

If this exemption mechanism requires any algorithm parameters
that cannot be derived from the given

key

, the
underlying exemption mechanism implementation is supposed to
generate the required parameters itself (using provider-specific
default values); in the case that algorithm parameters must be
specified by the caller, an

InvalidKeyException

is raised.

If this exemption mechanism requires any algorithm parameters
that cannot be derived from the given

key

, the
underlying exemption mechanism implementation is supposed to
generate the required parameters itself (using provider-specific
default values); in the case that algorithm parameters must be
specified by the caller, an

InvalidKeyException

is raised.

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
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption
mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Parameters:** params

- the algorithm parameters
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

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

,

ExemptionMechanismException

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption
mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption
mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

init

```java
public final void init​(
Key
key,

AlgorithmParameters
params)
throws
InvalidKeyException
,

InvalidAlgorithmParameterException
,

ExemptionMechanismException
```

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters itself
(using provider-specific default values); in the case that algorithm
parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

**Parameters:** key

- the key for this exemption mechanism
**Parameters:** params

- the algorithm parameters
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this exemption mechanism.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this exemption mechanism.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of initializing.

---

#### init

public final void init​(

Key

key,

AlgorithmParameters

params)
throws

InvalidKeyException

,

InvalidAlgorithmParameterException

,

ExemptionMechanismException

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters itself
(using provider-specific default values); in the case that algorithm
parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters itself
(using provider-specific default values); in the case that algorithm
parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

genExemptionBlob

```java
public final byte[] genExemptionBlob()
throws
IllegalStateException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob.

**Returns:** the new buffer with the result key blob.
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### genExemptionBlob

public final byte[] genExemptionBlob()
throws

IllegalStateException

,

ExemptionMechanismException

Generates the exemption mechanism key blob.

genExemptionBlob

```java
public final int genExemptionBlob​(byte[] output)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:** output

- the buffer for the result
**Returns:** the number of bytes stored in

output
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### genExemptionBlob

public final int genExemptionBlob​(byte[] output)
throws

IllegalStateException

,

ShortBufferException

,

ExemptionMechanismException

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

genExemptionBlob

```java
public final int genExemptionBlob​(byte[] output,
int outputOffset)
throws
IllegalStateException
,

ShortBufferException
,

ExemptionMechanismException
```

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

**Parameters:** output

- the buffer for the result
**Parameters:** outputOffset

- the offset in

output

where the result
is stored
**Returns:** the number of bytes stored in

output
**Throws:** IllegalStateException

- if this exemption mechanism is in
a wrong state (e.g., has not been initialized).
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### genExemptionBlob

public final int genExemptionBlob​(byte[] output,
int outputOffset)
throws

IllegalStateException

,

ShortBufferException

,

ExemptionMechanismException

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

getOutputSize

to determine how big
the output buffer should be.

---

