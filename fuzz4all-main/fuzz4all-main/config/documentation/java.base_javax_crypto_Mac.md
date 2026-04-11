# Class Mac

**Source:** `java.base\javax\crypto\Mac.html`

### Class Description

```java
public class
Mac

extends
Object

implements
Cloneable
```

This class provides the functionality of a "Message Authentication Code"
(MAC) algorithm.

A MAC provides a way to check
the integrity of information transmitted over or stored in an unreliable
medium, based on a secret key. Typically, message
authentication codes are used between two parties that share a secret
key in order to validate information transmitted between these
parties.

A MAC mechanism that is based on cryptographic hash functions is
referred to as HMAC. HMAC can be used with any cryptographic hash function,
e.g., SHA256 or SHA384, in combination with a secret shared key. HMAC is
specified in RFC 2104.

Every implementation of the Java platform is required to support
the following standard

Mac

algorithms:

- HmacMD5
- HmacSHA1
- HmacSHA256

These algorithms are described in the

Mac section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Mac​(
MacSpi
macSpi,

Provider
provider,

String
algorithm)

Creates a MAC object.

**Parameters:**
- macSpi

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

Mac

object.

This is the same name that was specified in one of the

getInstance

calls that created this

Mac

object.

**Returns:**
- the algorithm name of this

Mac

object.

---

#### public static final
Mac
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a

Mac

object that implements the
specified MAC algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Mac object encapsulating the
MacSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new

Mac

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

MacSpi

implementation for the specified algorithm
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
Mac
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

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

Mac

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

MacSpi

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
Mac
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the new

Mac

object

**Throws:**
- IllegalArgumentException

- if the

provider

is

null
- NoSuchAlgorithmException

- if a

MacSpi

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

Mac

object.

**Returns:**
- the provider of this

Mac

object.

---

#### public final int getMacLength()

Returns the length of the MAC in bytes.

**Returns:**
- the MAC length in bytes.

---

#### public final void init​(
Key
key)
throws
InvalidKeyException

Initializes this

Mac

object with the given key.

**Parameters:**
- key

- the key.

**Throws:**
- InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.

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

Initializes this

Mac

object with the given key and
algorithm parameters.

**Parameters:**
- key

- the key.
- params

- the algorithm parameters.

**Throws:**
- InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.
- InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this MAC.

---

#### public final void update​(byte input)
throws
IllegalStateException

Processes the given byte.

**Parameters:**
- input

- the input byte to be processed.

**Throws:**
- IllegalStateException

- if this

Mac

has not been
initialized.

---

#### public final void update​(byte[] input)
throws
IllegalStateException

Processes the given array of bytes.

**Parameters:**
- input

- the array of bytes to be processed.

**Throws:**
- IllegalStateException

- if this

Mac

has not been
initialized.

---

#### public final void update​(byte[] input,
int offset,
int len)
throws
IllegalStateException

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

**Parameters:**
- input

- the input buffer.
- offset

- the offset in

input

where the input starts.
- len

- the number of bytes to process.

**Throws:**
- IllegalStateException

- if this

Mac

has not been
initialized.

---

#### public final void update​(
ByteBuffer
input)

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:**
- input

- the ByteBuffer

**Throws:**
- IllegalStateException

- if this

Mac

has not been
initialized.

**Since:**
- 1.5

---

#### public final byte[] doFinal()
throws
IllegalStateException

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Returns:**
- the MAC result.

**Throws:**
- IllegalStateException

- if this

Mac

has not been
initialized.

---

#### public final void doFinal​(byte[] output,
int outOffset)
throws
ShortBufferException
,

IllegalStateException

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

The MAC result is stored in

output

, starting at

outOffset

inclusive.

**Parameters:**
- output

- the buffer where the MAC result is stored
- outOffset

- the offset in

output

where the MAC is
stored

**Throws:**
- ShortBufferException

- if the given output buffer is too small
to hold the result
- IllegalStateException

- if this

Mac

has not been
initialized.

---

#### public final byte[] doFinal​(byte[] input)
throws
IllegalStateException

Processes the given array of bytes and finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Parameters:**
- input

- data in bytes

**Returns:**
- the MAC result.

**Throws:**
- IllegalStateException

- if this

Mac

has not been
initialized.

---

#### public final void reset()

Resets this

Mac

object.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

---

#### public final
Object
clone()
throws
CloneNotSupportedException

Returns a clone if the provider implementation is cloneable.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone if the provider implementation is cloneable.

**Throws:**
- CloneNotSupportedException

- if this is called on a
delegate that does not support

Cloneable

.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Mac

java.lang.Object

- javax.crypto.Mac

javax.crypto.Mac

**All Implemented Interfaces:** Cloneable

```java
public class
Mac

extends
Object

implements
Cloneable
```

This class provides the functionality of a "Message Authentication Code"
(MAC) algorithm.

A MAC provides a way to check
the integrity of information transmitted over or stored in an unreliable
medium, based on a secret key. Typically, message
authentication codes are used between two parties that share a secret
key in order to validate information transmitted between these
parties.

A MAC mechanism that is based on cryptographic hash functions is
referred to as HMAC. HMAC can be used with any cryptographic hash function,
e.g., SHA256 or SHA384, in combination with a secret shared key. HMAC is
specified in RFC 2104.

Every implementation of the Java platform is required to support
the following standard

Mac

algorithms:

- HmacMD5
- HmacSHA1
- HmacSHA256

These algorithms are described in the

Mac section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4

public class

Mac

extends

Object

implements

Cloneable

This class provides the functionality of a "Message Authentication Code"
(MAC) algorithm.

A MAC provides a way to check
the integrity of information transmitted over or stored in an unreliable
medium, based on a secret key. Typically, message
authentication codes are used between two parties that share a secret
key in order to validate information transmitted between these
parties.

A MAC mechanism that is based on cryptographic hash functions is
referred to as HMAC. HMAC can be used with any cryptographic hash function,
e.g., SHA256 or SHA384, in combination with a secret shared key. HMAC is
specified in RFC 2104.

Every implementation of the Java platform is required to support
the following standard

Mac

algorithms:

- HmacMD5
- HmacSHA1
- HmacSHA256

These algorithms are described in the

Mac section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

A MAC provides a way to check
the integrity of information transmitted over or stored in an unreliable
medium, based on a secret key. Typically, message
authentication codes are used between two parties that share a secret
key in order to validate information transmitted between these
parties.

A MAC mechanism that is based on cryptographic hash functions is
referred to as HMAC. HMAC can be used with any cryptographic hash function,
e.g., SHA256 or SHA384, in combination with a secret shared key. HMAC is
specified in RFC 2104.

Every implementation of the Java platform is required to support
the following standard

Mac

algorithms:

- HmacMD5
- HmacSHA1
- HmacSHA256

These algorithms are described in the

Mac section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

A MAC mechanism that is based on cryptographic hash functions is
referred to as HMAC. HMAC can be used with any cryptographic hash function,
e.g., SHA256 or SHA384, in combination with a secret shared key. HMAC is
specified in RFC 2104.

Every implementation of the Java platform is required to support
the following standard

Mac

algorithms:

- HmacMD5
- HmacSHA1
- HmacSHA256

These algorithms are described in the

Mac section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support
the following standard

Mac

algorithms:

- HmacMD5
- HmacSHA1
- HmacSHA256

These algorithms are described in the

Mac section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

HmacMD5

HmacSHA1

HmacSHA256

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Mac

​(

MacSpi

macSpi,

Provider

provider,

String

algorithm)

Creates a MAC object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the provider implementation is cloneable.

byte[]

doFinal

()

Finishes the MAC operation.

byte[]

doFinal

​(byte[] input)

Processes the given array of bytes and finishes the MAC operation.

void

doFinal

​(byte[] output,
int outOffset)

Finishes the MAC operation.

String

getAlgorithm

()

Returns the algorithm name of this

Mac

object.

static

Mac

getInstance

​(

String

algorithm)

Returns a

Mac

object that implements the
specified MAC algorithm.

static

Mac

getInstance

​(

String

algorithm,

String

provider)

Returns a

Mac

object that implements the
specified MAC algorithm.

static

Mac

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

Mac

object that implements the
specified MAC algorithm.

int

getMacLength

()

Returns the length of the MAC in bytes.

Provider

getProvider

()

Returns the provider of this

Mac

object.

void

init

​(

Key

key)

Initializes this

Mac

object with the given key.

void

init

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this

Mac

object with the given key and
algorithm parameters.

void

reset

()

Resets this

Mac

object.

void

update

​(byte input)

Processes the given byte.

void

update

​(byte[] input)

Processes the given array of bytes.

void

update

​(byte[] input,
int offset,
int len)

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

void

update

​(

ByteBuffer

input)

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.

- Methods declared in class java.lang.

Object

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

Mac

​(

MacSpi

macSpi,

Provider

provider,

String

algorithm)

Creates a MAC object.

---

#### Constructor Summary

Creates a MAC object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the provider implementation is cloneable.

byte[]

doFinal

()

Finishes the MAC operation.

byte[]

doFinal

​(byte[] input)

Processes the given array of bytes and finishes the MAC operation.

void

doFinal

​(byte[] output,
int outOffset)

Finishes the MAC operation.

String

getAlgorithm

()

Returns the algorithm name of this

Mac

object.

static

Mac

getInstance

​(

String

algorithm)

Returns a

Mac

object that implements the
specified MAC algorithm.

static

Mac

getInstance

​(

String

algorithm,

String

provider)

Returns a

Mac

object that implements the
specified MAC algorithm.

static

Mac

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

Mac

object that implements the
specified MAC algorithm.

int

getMacLength

()

Returns the length of the MAC in bytes.

Provider

getProvider

()

Returns the provider of this

Mac

object.

void

init

​(

Key

key)

Initializes this

Mac

object with the given key.

void

init

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this

Mac

object with the given key and
algorithm parameters.

void

reset

()

Resets this

Mac

object.

void

update

​(byte input)

Processes the given byte.

void

update

​(byte[] input)

Processes the given array of bytes.

void

update

​(byte[] input,
int offset,
int len)

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

void

update

​(

ByteBuffer

input)

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.

- Methods declared in class java.lang.

Object

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

Returns a clone if the provider implementation is cloneable.

Finishes the MAC operation.

Processes the given array of bytes and finishes the MAC operation.

Returns the algorithm name of this

Mac

object.

Returns a

Mac

object that implements the
specified MAC algorithm.

Returns the length of the MAC in bytes.

Returns the provider of this

Mac

object.

Initializes this

Mac

object with the given key.

Initializes this

Mac

object with the given key and
algorithm parameters.

Resets this

Mac

object.

Processes the given byte.

Processes the given array of bytes.

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.

Methods declared in class java.lang.

Object

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

- Mac

```java
protected Mac​(
MacSpi
macSpi,

Provider
provider,

String
algorithm)
```

Creates a MAC object.

**Parameters:** macSpi

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

Mac

object.

This is the same name that was specified in one of the

getInstance

calls that created this

Mac

object.

**Returns:** the algorithm name of this

Mac

object.

- getInstance

```java
public static final
Mac
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

Mac

object that implements the
specified MAC algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Mac object encapsulating the
MacSpi implementation from the first
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

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

Mac

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

MacSpi

implementation for the specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static final
Mac
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

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

Mac

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

MacSpi

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
Mac
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

Mac

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

MacSpi

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

Mac

object.

**Returns:** the provider of this

Mac

object.

- getMacLength

```java
public final int getMacLength()
```

Returns the length of the MAC in bytes.

**Returns:** the MAC length in bytes.

- init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
```

Initializes this

Mac

object with the given key.

**Parameters:** key

- the key.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.

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

Initializes this

Mac

object with the given key and
algorithm parameters.

**Parameters:** key

- the key.
**Parameters:** params

- the algorithm parameters.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this MAC.

- update

```java
public final void update​(byte input)
throws
IllegalStateException
```

Processes the given byte.

**Parameters:** input

- the input byte to be processed.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- update

```java
public final void update​(byte[] input)
throws
IllegalStateException
```

Processes the given array of bytes.

**Parameters:** input

- the array of bytes to be processed.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- update

```java
public final void update​(byte[] input,
int offset,
int len)
throws
IllegalStateException
```

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

**Parameters:** input

- the input buffer.
**Parameters:** offset

- the offset in

input

where the input starts.
**Parameters:** len

- the number of bytes to process.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- update

```java
public final void update​(
ByteBuffer
input)
```

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** input

- the ByteBuffer
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.
**Since:** 1.5

- doFinal

```java
public final byte[] doFinal()
throws
IllegalStateException
```

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Returns:** the MAC result.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- doFinal

```java
public final void doFinal​(byte[] output,
int outOffset)
throws
ShortBufferException
,

IllegalStateException
```

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

The MAC result is stored in

output

, starting at

outOffset

inclusive.

**Parameters:** output

- the buffer where the MAC result is stored
**Parameters:** outOffset

- the offset in

output

where the MAC is
stored
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- doFinal

```java
public final byte[] doFinal​(byte[] input)
throws
IllegalStateException
```

Processes the given array of bytes and finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Parameters:** input

- data in bytes
**Returns:** the MAC result.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- reset

```java
public final void reset()
```

Resets this

Mac

object.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

- clone

```java
public final
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone if the provider implementation is cloneable.

**Overrides:** clone

in class

Object
**Returns:** a clone if the provider implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called on a
delegate that does not support

Cloneable

.
**See Also:** Cloneable

Constructor Detail

- Mac

```java
protected Mac​(
MacSpi
macSpi,

Provider
provider,

String
algorithm)
```

Creates a MAC object.

**Parameters:** macSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Constructor Detail

Mac

```java
protected Mac​(
MacSpi
macSpi,

Provider
provider,

String
algorithm)
```

Creates a MAC object.

**Parameters:** macSpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Mac

protected Mac​(

MacSpi

macSpi,

Provider

provider,

String

algorithm)

Creates a MAC object.

Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

Mac

object.

This is the same name that was specified in one of the

getInstance

calls that created this

Mac

object.

**Returns:** the algorithm name of this

Mac

object.

- getInstance

```java
public static final
Mac
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

Mac

object that implements the
specified MAC algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Mac object encapsulating the
MacSpi implementation from the first
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

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

Mac

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

MacSpi

implementation for the specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static final
Mac
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

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

Mac

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

MacSpi

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
Mac
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

Mac

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

MacSpi

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

Mac

object.

**Returns:** the provider of this

Mac

object.

- getMacLength

```java
public final int getMacLength()
```

Returns the length of the MAC in bytes.

**Returns:** the MAC length in bytes.

- init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
```

Initializes this

Mac

object with the given key.

**Parameters:** key

- the key.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.

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

Initializes this

Mac

object with the given key and
algorithm parameters.

**Parameters:** key

- the key.
**Parameters:** params

- the algorithm parameters.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this MAC.

- update

```java
public final void update​(byte input)
throws
IllegalStateException
```

Processes the given byte.

**Parameters:** input

- the input byte to be processed.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- update

```java
public final void update​(byte[] input)
throws
IllegalStateException
```

Processes the given array of bytes.

**Parameters:** input

- the array of bytes to be processed.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- update

```java
public final void update​(byte[] input,
int offset,
int len)
throws
IllegalStateException
```

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

**Parameters:** input

- the input buffer.
**Parameters:** offset

- the offset in

input

where the input starts.
**Parameters:** len

- the number of bytes to process.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- update

```java
public final void update​(
ByteBuffer
input)
```

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** input

- the ByteBuffer
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.
**Since:** 1.5

- doFinal

```java
public final byte[] doFinal()
throws
IllegalStateException
```

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Returns:** the MAC result.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- doFinal

```java
public final void doFinal​(byte[] output,
int outOffset)
throws
ShortBufferException
,

IllegalStateException
```

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

The MAC result is stored in

output

, starting at

outOffset

inclusive.

**Parameters:** output

- the buffer where the MAC result is stored
**Parameters:** outOffset

- the offset in

output

where the MAC is
stored
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- doFinal

```java
public final byte[] doFinal​(byte[] input)
throws
IllegalStateException
```

Processes the given array of bytes and finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Parameters:** input

- data in bytes
**Returns:** the MAC result.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

- reset

```java
public final void reset()
```

Resets this

Mac

object.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

- clone

```java
public final
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone if the provider implementation is cloneable.

**Overrides:** clone

in class

Object
**Returns:** a clone if the provider implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called on a
delegate that does not support

Cloneable

.
**See Also:** Cloneable

---

#### Method Detail

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

Mac

object.

This is the same name that was specified in one of the

getInstance

calls that created this

Mac

object.

**Returns:** the algorithm name of this

Mac

object.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the algorithm name of this

Mac

object.

This is the same name that was specified in one of the

getInstance

calls that created this

Mac

object.

This is the same name that was specified in one of the

getInstance

calls that created this

Mac

object.

getInstance

```java
public static final
Mac
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

Mac

object that implements the
specified MAC algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Mac object encapsulating the
MacSpi implementation from the first
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

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

Mac

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

MacSpi

implementation for the specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

Mac

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a

Mac

object that implements the
specified MAC algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Mac object encapsulating the
MacSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Mac object encapsulating the
MacSpi implementation from the first
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
Mac
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

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

Mac

object
**Throws:** IllegalArgumentException

- if the

provider

is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

MacSpi

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

Mac

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

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new Mac object encapsulating the
MacSpi implementation from the specified provider
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
Mac
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested MAC algorithm.
See the Mac section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

Mac

object
**Throws:** IllegalArgumentException

- if the

provider

is

null
**Throws:** NoSuchAlgorithmException

- if a

MacSpi

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

Mac

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

Mac

object that implements the
specified MAC algorithm.

A new Mac object encapsulating the
MacSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new Mac object encapsulating the
MacSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

Mac

object.

**Returns:** the provider of this

Mac

object.

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

Mac

object.

getMacLength

```java
public final int getMacLength()
```

Returns the length of the MAC in bytes.

**Returns:** the MAC length in bytes.

---

#### getMacLength

public final int getMacLength()

Returns the length of the MAC in bytes.

init

```java
public final void init​(
Key
key)
throws
InvalidKeyException
```

Initializes this

Mac

object with the given key.

**Parameters:** key

- the key.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.

---

#### init

public final void init​(

Key

key)
throws

InvalidKeyException

Initializes this

Mac

object with the given key.

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

Initializes this

Mac

object with the given key and
algorithm parameters.

**Parameters:** key

- the key.
**Parameters:** params

- the algorithm parameters.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this MAC.

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

Initializes this

Mac

object with the given key and
algorithm parameters.

update

```java
public final void update​(byte input)
throws
IllegalStateException
```

Processes the given byte.

**Parameters:** input

- the input byte to be processed.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

---

#### update

public final void update​(byte input)
throws

IllegalStateException

Processes the given byte.

update

```java
public final void update​(byte[] input)
throws
IllegalStateException
```

Processes the given array of bytes.

**Parameters:** input

- the array of bytes to be processed.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

---

#### update

public final void update​(byte[] input)
throws

IllegalStateException

Processes the given array of bytes.

update

```java
public final void update​(byte[] input,
int offset,
int len)
throws
IllegalStateException
```

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

**Parameters:** input

- the input buffer.
**Parameters:** offset

- the offset in

input

where the input starts.
**Parameters:** len

- the number of bytes to process.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

---

#### update

public final void update​(byte[] input,
int offset,
int len)
throws

IllegalStateException

Processes the first

len

bytes in

input

,
starting at

offset

inclusive.

update

```java
public final void update​(
ByteBuffer
input)
```

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** input

- the ByteBuffer
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.
**Since:** 1.5

---

#### update

public final void update​(

ByteBuffer

input)

Processes

input.remaining()

bytes in the ByteBuffer

input

, starting at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

doFinal

```java
public final byte[] doFinal()
throws
IllegalStateException
```

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Returns:** the MAC result.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

---

#### doFinal

public final byte[] doFinal()
throws

IllegalStateException

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

doFinal

```java
public final void doFinal​(byte[] output,
int outOffset)
throws
ShortBufferException
,

IllegalStateException
```

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

The MAC result is stored in

output

, starting at

outOffset

inclusive.

**Parameters:** output

- the buffer where the MAC result is stored
**Parameters:** outOffset

- the offset in

output

where the MAC is
stored
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

---

#### doFinal

public final void doFinal​(byte[] output,
int outOffset)
throws

ShortBufferException

,

IllegalStateException

Finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

The MAC result is stored in

output

, starting at

outOffset

inclusive.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

The MAC result is stored in

output

, starting at

outOffset

inclusive.

The MAC result is stored in

output

, starting at

outOffset

inclusive.

doFinal

```java
public final byte[] doFinal​(byte[] input)
throws
IllegalStateException
```

Processes the given array of bytes and finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

**Parameters:** input

- data in bytes
**Returns:** the MAC result.
**Throws:** IllegalStateException

- if this

Mac

has not been
initialized.

---

#### doFinal

public final byte[] doFinal​(byte[] input)
throws

IllegalStateException

Processes the given array of bytes and finishes the MAC operation.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

reset

```java
public final void reset()
```

Resets this

Mac

object.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

---

#### reset

public final void reset()

Resets this

Mac

object.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

A call to this method resets this

Mac

object to the
state it was in when previously initialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.
That is, the object is reset and available to generate another MAC from
the same key, if desired, via new calls to

update

and

doFinal

.
(In order to reuse this

Mac

object with a different key,
it must be reinitialized via a call to

init(Key)

or

init(Key, AlgorithmParameterSpec)

.

clone

```java
public final
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone if the provider implementation is cloneable.

**Overrides:** clone

in class

Object
**Returns:** a clone if the provider implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called on a
delegate that does not support

Cloneable

.
**See Also:** Cloneable

---

#### clone

public final

Object

clone()
throws

CloneNotSupportedException

Returns a clone if the provider implementation is cloneable.

---

