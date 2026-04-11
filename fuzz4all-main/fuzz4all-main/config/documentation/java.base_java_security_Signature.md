# Class Signature

**Source:** `java.base\java\security\Signature.html`

### Class Description

```java
public abstract class
Signature

extends
SignatureSpi
```

The Signature class is used to provide applications the functionality
of a digital signature algorithm. Digital signatures are used for
authentication and integrity assurance of digital data.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The DSA algorithm using the
SHA-256 message digest algorithm can be specified as

SHA256withDSA

.
In the case of RSA the signing algorithm could be specified as, for example,

SHA256withRSA

.
The algorithm name must be specified, as there is no default.

A Signature object can be used to generate and verify digital
signatures.

There are three phases to the use of a Signature object for
either signing data or verifying a signature:

- Initialization, with either

- a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Updating

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

Note that this class is abstract and extends from

SignatureSpi

for historical reasons.
Application developers should only take notice of the methods defined in
this

Signature

class; all the methods in
the superclass are intended for cryptographic service providers who wish to
supply their own implementations of digital signature algorithms.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.1

---

### Field Details

#### protected static final int UNINITIALIZED

Possible

state

value, signifying that
this signature object has not yet been initialized.

**See Also:**
- Constant Field Values

---

#### protected static final int SIGN

Possible

state

value, signifying that
this signature object has been initialized for signing.

**See Also:**
- Constant Field Values

---

#### protected static final int VERIFY

Possible

state

value, signifying that
this signature object has been initialized for verification.

**See Also:**
- Constant Field Values

---

#### protected int state

Current state of this signature object.

---

### Constructor Details

#### protected Signature​(
String
algorithm)

Creates a Signature object for the specified algorithm.

**Parameters:**
- algorithm

- the standard string name of the algorithm.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

---

### Method Details

#### public static
Signature
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a Signature object that implements the specified signature
algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Signature object encapsulating the
SignatureSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Returns:**
- the new

Signature

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

Signature

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
Signature
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns a Signature object that implements the specified signature
algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

Signature

object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty
- NoSuchAlgorithmException

- if a

SignatureSpi

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
Signature
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a Signature object that implements the specified
signature algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the new

Signature

object

**Throws:**
- IllegalArgumentException

- if the provider is

null
- NoSuchAlgorithmException

- if a

SignatureSpi

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

Returns the provider of this signature object.

**Returns:**
- the provider of this signature object

---

#### public final void initVerify​(
PublicKey
publicKey)
throws
InvalidKeyException

Initializes this object for verification. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:**
- publicKey

- the public key of the identity whose signature is
going to be verified.

**Throws:**
- InvalidKeyException

- if the key is invalid.

---

#### public final void initVerify​(
Certificate
certificate)
throws
InvalidKeyException

Initializes this object for verification, using the public key from
the given certificate.

If the certificate is of type X.509 and has a

key usage

extension field marked as critical, and the value of the

key usage

extension field implies that the public key in
the certificate and its corresponding private key are not
supposed to be used for digital signatures, an

InvalidKeyException

is thrown.

**Parameters:**
- certificate

- the certificate of the identity whose signature is
going to be verified.

**Throws:**
- InvalidKeyException

- if the public key in the certificate
is not encoded properly or does not include required parameter
information or cannot be used for digital signature purposes.

**Since:**
- 1.3

---

#### public final void initSign​(
PrivateKey
privateKey)
throws
InvalidKeyException

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:**
- privateKey

- the private key of the identity whose signature
is going to be generated.

**Throws:**
- InvalidKeyException

- if the key is invalid.

---

#### public final void initSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:**
- privateKey

- the private key of the identity whose signature
is going to be generated.
- random

- the source of randomness for this signature.

**Throws:**
- InvalidKeyException

- if the key is invalid.

---

#### public final byte[] sign()
throws
SignatureException

Returns the signature bytes of all the data updated.
The format of the signature depends on the underlying
signature scheme.

A call to this method resets this signature object to the state
it was in when previously initialized for signing via a
call to

initSign(PrivateKey)

. That is, the object is
reset and available to generate another signature from the same
signer, if desired, via new calls to

update

and

sign

.

**Returns:**
- the signature bytes of the signing operation's result.

**Throws:**
- SignatureException

- if this signature object is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

---

#### public final int sign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

This signature object is reset to its initial state (the state it
was in after a call to one of the

initSign

methods) and
can be reused to generate further signatures with the same private key.

**Parameters:**
- outbuf

- buffer for the signature result.
- offset

- offset into

outbuf

where the signature is
stored.
- len

- number of bytes within

outbuf

allotted for the
signature.

**Returns:**
- the number of bytes placed into

outbuf

.

**Throws:**
- SignatureException

- if this signature object is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.
- IllegalArgumentException

- if

outbuf

is

null

,
or

offset

or

len

is less than 0, or the sum of

offset

and

len

is greater than the length of

outbuf

.

**Since:**
- 1.2

---

#### public final boolean verify​(byte[] signature)
throws
SignatureException

Verifies the passed-in signature.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:**
- signature

- the signature bytes to be verified.

**Returns:**
- true if the signature was verified, false if not.

**Throws:**
- SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

---

#### public final boolean verify​(byte[] signature,
int offset,
int length)
throws
SignatureException

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:**
- signature

- the signature bytes to be verified.
- offset

- the offset to start from in the array of bytes.
- length

- the number of bytes to use, starting at offset.

**Returns:**
- true if the signature was verified, false if not.

**Throws:**
- SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.
- IllegalArgumentException

- if the

signature

byte array is

null

, or the

offset

or

length

is less than 0, or the sum of the

offset

and

length

is greater than the length of the

signature

byte array.

**Since:**
- 1.4

---

#### public final void update​(byte b)
throws
SignatureException

Updates the data to be signed or verified by a byte.

**Parameters:**
- b

- the byte to use for the update.

**Throws:**
- SignatureException

- if this signature object is not
initialized properly.

---

#### public final void update​(byte[] data)
throws
SignatureException

Updates the data to be signed or verified, using the specified
array of bytes.

**Parameters:**
- data

- the byte array to use for the update.

**Throws:**
- SignatureException

- if this signature object is not
initialized properly.

---

#### public final void update​(byte[] data,
int off,
int len)
throws
SignatureException

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

**Parameters:**
- data

- the array of bytes.
- off

- the offset to start from in the array of bytes.
- len

- the number of bytes to use, starting at offset.

**Throws:**
- SignatureException

- if this signature object is not
initialized properly.
- IllegalArgumentException

- if

data

is

null

,
or

off

or

len

is less than 0, or the sum of

off

and

len

is greater than the length of

data

.

---

#### public final void update​(
ByteBuffer
data)
throws
SignatureException

Updates the data to be signed or verified using the specified
ByteBuffer. Processes the

data.remaining()

bytes
starting at

data.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:**
- data

- the ByteBuffer

**Throws:**
- SignatureException

- if this signature object is not
initialized properly.

**Since:**
- 1.5

---

#### public final
String
getAlgorithm()

Returns the name of the algorithm for this signature object.

**Returns:**
- the name of the algorithm for this signature object.

---

#### public
String
toString()

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this signature object.

---

#### @Deprecated

public final void setParameter​(
String
param,

Object
value)
throws
InvalidParameterException

Sets the specified algorithm parameter to the specified value.
This method supplies a general-purpose mechanism through
which it is possible to set the various parameters of this object.
A parameter may be any settable parameter for the algorithm, such as
a parameter size, or a source of random bits for signature generation
(if appropriate), or an indication of whether or not to perform
a specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

**Parameters:**
- param

- the string identifier of the parameter.
- value

- the parameter value.

**Throws:**
- InvalidParameterException

- if

param

is an
invalid parameter for this signature algorithm engine,
the parameter is already set
and cannot be set again, a security exception occurs, and so on.

**See Also:**
- getParameter(java.lang.String)

---

#### public final void setParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException

Initializes this signature engine with the specified parameter set.

**Parameters:**
- params

- the parameters

**Throws:**
- InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this signature engine

**See Also:**
- getParameters()

---

#### public final
AlgorithmParameters
getParameters()

Returns the parameters used with this signature object.

If this signature has been previously initialized with parameters
(by calling the

setParameter

method), this method returns
the same parameters. If this signature has not been initialized with
parameters, this method may return a combination of default and
randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:**
- the parameters used with this signature, or

null

**See Also:**
- setParameter(AlgorithmParameterSpec)

**Since:**
- 1.4

---

#### @Deprecated

public final
Object
getParameter​(
String
param)
throws
InvalidParameterException

Gets the value of the specified algorithm parameter. This method
supplies a general-purpose mechanism through which it is possible to
get the various parameters of this object. A parameter may be any
settable parameter for the algorithm, such as a parameter size, or
a source of random bits for signature generation (if appropriate),
or an indication of whether or not to perform a specific but optional
computation. A uniform algorithm-specific naming scheme for each
parameter is desirable but left unspecified at this time.

**Parameters:**
- param

- the string name of the parameter.

**Returns:**
- the object that represents the parameter value, or

null

if
there is none.

**Throws:**
- InvalidParameterException

- if

param

is an invalid
parameter for this engine, or another exception occurs while
trying to get this parameter.

**See Also:**
- setParameter(String, Object)

---

#### public
Object
clone()
throws
CloneNotSupportedException

Returns a clone if the implementation is cloneable.

**Overrides:**
- clone

in class

SignatureSpi

**Returns:**
- a clone if the implementation is cloneable.

**Throws:**
- CloneNotSupportedException

- if this is called
on an implementation that does not support

Cloneable

.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Signature

java.lang.Object

- java.security.SignatureSpi
- - java.security.Signature

java.security.SignatureSpi

- java.security.Signature

java.security.Signature

```java
public abstract class
Signature

extends
SignatureSpi
```

The Signature class is used to provide applications the functionality
of a digital signature algorithm. Digital signatures are used for
authentication and integrity assurance of digital data.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The DSA algorithm using the
SHA-256 message digest algorithm can be specified as

SHA256withDSA

.
In the case of RSA the signing algorithm could be specified as, for example,

SHA256withRSA

.
The algorithm name must be specified, as there is no default.

A Signature object can be used to generate and verify digital
signatures.

There are three phases to the use of a Signature object for
either signing data or verifying a signature:

- Initialization, with either

- a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Updating

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

Note that this class is abstract and extends from

SignatureSpi

for historical reasons.
Application developers should only take notice of the methods defined in
this

Signature

class; all the methods in
the superclass are intended for cryptographic service providers who wish to
supply their own implementations of digital signature algorithms.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.1

public abstract class

Signature

extends

SignatureSpi

The Signature class is used to provide applications the functionality
of a digital signature algorithm. Digital signatures are used for
authentication and integrity assurance of digital data.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The DSA algorithm using the
SHA-256 message digest algorithm can be specified as

SHA256withDSA

.
In the case of RSA the signing algorithm could be specified as, for example,

SHA256withRSA

.
The algorithm name must be specified, as there is no default.

A Signature object can be used to generate and verify digital
signatures.

There are three phases to the use of a Signature object for
either signing data or verifying a signature:

- Initialization, with either

- a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Updating

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

Note that this class is abstract and extends from

SignatureSpi

for historical reasons.
Application developers should only take notice of the methods defined in
this

Signature

class; all the methods in
the superclass are intended for cryptographic service providers who wish to
supply their own implementations of digital signature algorithms.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The DSA algorithm using the
SHA-256 message digest algorithm can be specified as

SHA256withDSA

.
In the case of RSA the signing algorithm could be specified as, for example,

SHA256withRSA

.
The algorithm name must be specified, as there is no default.

A Signature object can be used to generate and verify digital
signatures.

There are three phases to the use of a Signature object for
either signing data or verifying a signature:

- Initialization, with either

- a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Updating

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

Note that this class is abstract and extends from

SignatureSpi

for historical reasons.
Application developers should only take notice of the methods defined in
this

Signature

class; all the methods in
the superclass are intended for cryptographic service providers who wish to
supply their own implementations of digital signature algorithms.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

A Signature object can be used to generate and verify digital
signatures.

There are three phases to the use of a Signature object for
either signing data or verifying a signature:

- Initialization, with either

- a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Updating

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

Note that this class is abstract and extends from

SignatureSpi

for historical reasons.
Application developers should only take notice of the methods defined in
this

Signature

class; all the methods in
the superclass are intended for cryptographic service providers who wish to
supply their own implementations of digital signature algorithms.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

There are three phases to the use of a Signature object for
either signing data or verifying a signature:

- Initialization, with either

- a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Updating

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

Note that this class is abstract and extends from

SignatureSpi

for historical reasons.
Application developers should only take notice of the methods defined in
this

Signature

class; all the methods in
the superclass are intended for cryptographic service providers who wish to
supply their own implementations of digital signature algorithms.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Initialization, with either

- a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Updating

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

a public key, which initializes the signature for
verification (see

initVerify

), or

a private key (and optionally a Secure Random Number Generator),
which initializes the signature for signing
(see

initSign(PrivateKey)

and

initSign(PrivateKey, SecureRandom)

).

Depending on the type of initialization, this will update the
bytes to be signed or verified. See the

update

methods.

Signing or Verifying a signature on all updated bytes. See the

sign

methods and the

verify

method.

Note that this class is abstract and extends from

SignatureSpi

for historical reasons.
Application developers should only take notice of the methods defined in
this

Signature

class; all the methods in
the superclass are intended for cryptographic service providers who wish to
supply their own implementations of digital signature algorithms.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support the
following standard

Signature

algorithms:

- SHA1withDSA
- SHA256withDSA
- SHA1withRSA
- SHA256withRSA

These algorithms are described in the

Signature section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

SHA1withDSA

SHA256withDSA

SHA1withRSA

SHA256withRSA

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static int

SIGN

Possible

state

value, signifying that
this signature object has been initialized for signing.

protected int

state

Current state of this signature object.

protected static int

UNINITIALIZED

Possible

state

value, signifying that
this signature object has not yet been initialized.

protected static int

VERIFY

Possible

state

value, signifying that
this signature object has been initialized for verification.

- Fields declared in class java.security.

SignatureSpi

appRandom

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Signature

​(

String

algorithm)

Creates a Signature object for the specified algorithm.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the implementation is cloneable.

String

getAlgorithm

()

Returns the name of the algorithm for this signature object.

static

Signature

getInstance

​(

String

algorithm)

Returns a Signature object that implements the specified signature
algorithm.

static

Signature

getInstance

​(

String

algorithm,

String

provider)

Returns a Signature object that implements the specified signature
algorithm.

static

Signature

getInstance

​(

String

algorithm,

Provider

provider)

Returns a Signature object that implements the specified
signature algorithm.

Object

getParameter

​(

String

param)

Deprecated.

AlgorithmParameters

getParameters

()

Returns the parameters used with this signature object.

Provider

getProvider

()

Returns the provider of this signature object.

void

initSign

​(

PrivateKey

privateKey)

Initialize this object for signing.

void

initSign

​(

PrivateKey

privateKey,

SecureRandom

random)

Initialize this object for signing.

void

initVerify

​(

Certificate

certificate)

Initializes this object for verification, using the public key from
the given certificate.

void

initVerify

​(

PublicKey

publicKey)

Initializes this object for verification.

void

setParameter

​(

String

param,

Object

value)

Deprecated.

Use

setParameter

.

void

setParameter

​(

AlgorithmParameterSpec

params)

Initializes this signature engine with the specified parameter set.

byte[]

sign

()

Returns the signature bytes of all the data updated.

int

sign

​(byte[] outbuf,
int offset,
int len)

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.

String

toString

()

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

void

update

​(byte b)

Updates the data to be signed or verified by a byte.

void

update

​(byte[] data)

Updates the data to be signed or verified, using the specified
array of bytes.

void

update

​(byte[] data,
int off,
int len)

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

void

update

​(

ByteBuffer

data)

Updates the data to be signed or verified using the specified
ByteBuffer.

boolean

verify

​(byte[] signature)

Verifies the passed-in signature.

boolean

verify

​(byte[] signature,
int offset,
int length)

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

- Methods declared in class java.security.

SignatureSpi

engineGetParameter

,

engineGetParameters

,

engineInitSign

,

engineInitSign

,

engineInitVerify

,

engineSetParameter

,

engineSetParameter

,

engineSign

,

engineSign

,

engineUpdate

,

engineUpdate

,

engineUpdate

,

engineVerify

,

engineVerify

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

protected static int

SIGN

Possible

state

value, signifying that
this signature object has been initialized for signing.

protected int

state

Current state of this signature object.

protected static int

UNINITIALIZED

Possible

state

value, signifying that
this signature object has not yet been initialized.

protected static int

VERIFY

Possible

state

value, signifying that
this signature object has been initialized for verification.

- Fields declared in class java.security.

SignatureSpi

appRandom

---

#### Field Summary

Possible

state

value, signifying that
this signature object has been initialized for signing.

Current state of this signature object.

Possible

state

value, signifying that
this signature object has not yet been initialized.

Possible

state

value, signifying that
this signature object has been initialized for verification.

Fields declared in class java.security.

SignatureSpi

appRandom

---

#### Fields declared in class java.security. SignatureSpi

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Signature

​(

String

algorithm)

Creates a Signature object for the specified algorithm.

---

#### Constructor Summary

Creates a Signature object for the specified algorithm.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the implementation is cloneable.

String

getAlgorithm

()

Returns the name of the algorithm for this signature object.

static

Signature

getInstance

​(

String

algorithm)

Returns a Signature object that implements the specified signature
algorithm.

static

Signature

getInstance

​(

String

algorithm,

String

provider)

Returns a Signature object that implements the specified signature
algorithm.

static

Signature

getInstance

​(

String

algorithm,

Provider

provider)

Returns a Signature object that implements the specified
signature algorithm.

Object

getParameter

​(

String

param)

Deprecated.

AlgorithmParameters

getParameters

()

Returns the parameters used with this signature object.

Provider

getProvider

()

Returns the provider of this signature object.

void

initSign

​(

PrivateKey

privateKey)

Initialize this object for signing.

void

initSign

​(

PrivateKey

privateKey,

SecureRandom

random)

Initialize this object for signing.

void

initVerify

​(

Certificate

certificate)

Initializes this object for verification, using the public key from
the given certificate.

void

initVerify

​(

PublicKey

publicKey)

Initializes this object for verification.

void

setParameter

​(

String

param,

Object

value)

Deprecated.

Use

setParameter

.

void

setParameter

​(

AlgorithmParameterSpec

params)

Initializes this signature engine with the specified parameter set.

byte[]

sign

()

Returns the signature bytes of all the data updated.

int

sign

​(byte[] outbuf,
int offset,
int len)

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.

String

toString

()

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

void

update

​(byte b)

Updates the data to be signed or verified by a byte.

void

update

​(byte[] data)

Updates the data to be signed or verified, using the specified
array of bytes.

void

update

​(byte[] data,
int off,
int len)

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

void

update

​(

ByteBuffer

data)

Updates the data to be signed or verified using the specified
ByteBuffer.

boolean

verify

​(byte[] signature)

Verifies the passed-in signature.

boolean

verify

​(byte[] signature,
int offset,
int length)

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

- Methods declared in class java.security.

SignatureSpi

engineGetParameter

,

engineGetParameters

,

engineInitSign

,

engineInitSign

,

engineInitVerify

,

engineSetParameter

,

engineSetParameter

,

engineSign

,

engineSign

,

engineUpdate

,

engineUpdate

,

engineUpdate

,

engineVerify

,

engineVerify

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

wait

,

wait

,

wait

---

#### Method Summary

Returns a clone if the implementation is cloneable.

Returns the name of the algorithm for this signature object.

Returns a Signature object that implements the specified signature
algorithm.

Returns a Signature object that implements the specified
signature algorithm.

Deprecated.

Returns the parameters used with this signature object.

Returns the provider of this signature object.

Initialize this object for signing.

Initializes this object for verification, using the public key from
the given certificate.

Initializes this object for verification.

Deprecated.

Use

setParameter

.

Initializes this signature engine with the specified parameter set.

Returns the signature bytes of all the data updated.

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

Updates the data to be signed or verified by a byte.

Updates the data to be signed or verified, using the specified
array of bytes.

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

Updates the data to be signed or verified using the specified
ByteBuffer.

Verifies the passed-in signature.

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

Methods declared in class java.security.

SignatureSpi

engineGetParameter

,

engineGetParameters

,

engineInitSign

,

engineInitSign

,

engineInitVerify

,

engineSetParameter

,

engineSetParameter

,

engineSign

,

engineSign

,

engineUpdate

,

engineUpdate

,

engineUpdate

,

engineVerify

,

engineVerify

---

#### Methods declared in class java.security. SignatureSpi

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- UNINITIALIZED

```java
protected static final int UNINITIALIZED
```

Possible

state

value, signifying that
this signature object has not yet been initialized.

**See Also:** Constant Field Values

- SIGN

```java
protected static final int SIGN
```

Possible

state

value, signifying that
this signature object has been initialized for signing.

**See Also:** Constant Field Values

- VERIFY

```java
protected static final int VERIFY
```

Possible

state

value, signifying that
this signature object has been initialized for verification.

**See Also:** Constant Field Values

- state

```java
protected int state
```

Current state of this signature object.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Signature

```java
protected Signature​(
String
algorithm)
```

Creates a Signature object for the specified algorithm.

**Parameters:** algorithm

- the standard string name of the algorithm.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
Signature
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a Signature object that implements the specified signature
algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Signature object encapsulating the
SignatureSpi implementation from the first
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

- the standard name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

Signature

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

Signature

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
Signature
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

Returns a Signature object that implements the specified signature
algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

Signature

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SignatureSpi

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
Signature
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a Signature object that implements the specified
signature algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

Signature

object
**Throws:** IllegalArgumentException

- if the provider is

null
**Throws:** NoSuchAlgorithmException

- if a

SignatureSpi

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

Returns the provider of this signature object.

**Returns:** the provider of this signature object

- initVerify

```java
public final void initVerify​(
PublicKey
publicKey)
throws
InvalidKeyException
```

Initializes this object for verification. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** publicKey

- the public key of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the key is invalid.

- initVerify

```java
public final void initVerify​(
Certificate
certificate)
throws
InvalidKeyException
```

Initializes this object for verification, using the public key from
the given certificate.

If the certificate is of type X.509 and has a

key usage

extension field marked as critical, and the value of the

key usage

extension field implies that the public key in
the certificate and its corresponding private key are not
supposed to be used for digital signatures, an

InvalidKeyException

is thrown.

**Parameters:** certificate

- the certificate of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the public key in the certificate
is not encoded properly or does not include required parameter
information or cannot be used for digital signature purposes.
**Since:** 1.3

- initSign

```java
public final void initSign​(
PrivateKey
privateKey)
throws
InvalidKeyException
```

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** privateKey

- the private key of the identity whose signature
is going to be generated.
**Throws:** InvalidKeyException

- if the key is invalid.

- initSign

```java
public final void initSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException
```

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** privateKey

- the private key of the identity whose signature
is going to be generated.
**Parameters:** random

- the source of randomness for this signature.
**Throws:** InvalidKeyException

- if the key is invalid.

- sign

```java
public final byte[] sign()
throws
SignatureException
```

Returns the signature bytes of all the data updated.
The format of the signature depends on the underlying
signature scheme.

A call to this method resets this signature object to the state
it was in when previously initialized for signing via a
call to

initSign(PrivateKey)

. That is, the object is
reset and available to generate another signature from the same
signer, if desired, via new calls to

update

and

sign

.

**Returns:** the signature bytes of the signing operation's result.
**Throws:** SignatureException

- if this signature object is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

- sign

```java
public final int sign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException
```

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

This signature object is reset to its initial state (the state it
was in after a call to one of the

initSign

methods) and
can be reused to generate further signatures with the same private key.

**Parameters:** outbuf

- buffer for the signature result.
**Parameters:** offset

- offset into

outbuf

where the signature is
stored.
**Parameters:** len

- number of bytes within

outbuf

allotted for the
signature.
**Returns:** the number of bytes placed into

outbuf

.
**Throws:** SignatureException

- if this signature object is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.
**Throws:** IllegalArgumentException

- if

outbuf

is

null

,
or

offset

or

len

is less than 0, or the sum of

offset

and

len

is greater than the length of

outbuf

.
**Since:** 1.2

- verify

```java
public final boolean verify​(byte[] signature)
throws
SignatureException
```

Verifies the passed-in signature.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:** signature

- the signature bytes to be verified.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

- verify

```java
public final boolean verify​(byte[] signature,
int offset,
int length)
throws
SignatureException
```

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:** signature

- the signature bytes to be verified.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** length

- the number of bytes to use, starting at offset.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.
**Throws:** IllegalArgumentException

- if the

signature

byte array is

null

, or the

offset

or

length

is less than 0, or the sum of the

offset

and

length

is greater than the length of the

signature

byte array.
**Since:** 1.4

- update

```java
public final void update​(byte b)
throws
SignatureException
```

Updates the data to be signed or verified by a byte.

**Parameters:** b

- the byte to use for the update.
**Throws:** SignatureException

- if this signature object is not
initialized properly.

- update

```java
public final void update​(byte[] data)
throws
SignatureException
```

Updates the data to be signed or verified, using the specified
array of bytes.

**Parameters:** data

- the byte array to use for the update.
**Throws:** SignatureException

- if this signature object is not
initialized properly.

- update

```java
public final void update​(byte[] data,
int off,
int len)
throws
SignatureException
```

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

**Parameters:** data

- the array of bytes.
**Parameters:** off

- the offset to start from in the array of bytes.
**Parameters:** len

- the number of bytes to use, starting at offset.
**Throws:** SignatureException

- if this signature object is not
initialized properly.
**Throws:** IllegalArgumentException

- if

data

is

null

,
or

off

or

len

is less than 0, or the sum of

off

and

len

is greater than the length of

data

.

- update

```java
public final void update​(
ByteBuffer
data)
throws
SignatureException
```

Updates the data to be signed or verified using the specified
ByteBuffer. Processes the

data.remaining()

bytes
starting at

data.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** data

- the ByteBuffer
**Throws:** SignatureException

- if this signature object is not
initialized properly.
**Since:** 1.5

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the name of the algorithm for this signature object.

**Returns:** the name of the algorithm for this signature object.

- toString

```java
public
String
toString()
```

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this signature object.

- setParameter

```java
@Deprecated

public final void setParameter​(
String
param,

Object
value)
throws
InvalidParameterException
```

Deprecated.

Use

setParameter

.

Sets the specified algorithm parameter to the specified value.
This method supplies a general-purpose mechanism through
which it is possible to set the various parameters of this object.
A parameter may be any settable parameter for the algorithm, such as
a parameter size, or a source of random bits for signature generation
(if appropriate), or an indication of whether or not to perform
a specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

**Parameters:** param

- the string identifier of the parameter.
**Parameters:** value

- the parameter value.
**Throws:** InvalidParameterException

- if

param

is an
invalid parameter for this signature algorithm engine,
the parameter is already set
and cannot be set again, a security exception occurs, and so on.
**See Also:** getParameter(java.lang.String)

- setParameter

```java
public final void setParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this signature engine with the specified parameter set.

**Parameters:** params

- the parameters
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this signature engine
**See Also:** getParameters()

- getParameters

```java
public final
AlgorithmParameters
getParameters()
```

Returns the parameters used with this signature object.

If this signature has been previously initialized with parameters
(by calling the

setParameter

method), this method returns
the same parameters. If this signature has not been initialized with
parameters, this method may return a combination of default and
randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:** the parameters used with this signature, or

null
**Since:** 1.4
**See Also:** setParameter(AlgorithmParameterSpec)

- getParameter

```java
@Deprecated

public final
Object
getParameter​(
String
param)
throws
InvalidParameterException
```

Deprecated.

Gets the value of the specified algorithm parameter. This method
supplies a general-purpose mechanism through which it is possible to
get the various parameters of this object. A parameter may be any
settable parameter for the algorithm, such as a parameter size, or
a source of random bits for signature generation (if appropriate),
or an indication of whether or not to perform a specific but optional
computation. A uniform algorithm-specific naming scheme for each
parameter is desirable but left unspecified at this time.

**Parameters:** param

- the string name of the parameter.
**Returns:** the object that represents the parameter value, or

null

if
there is none.
**Throws:** InvalidParameterException

- if

param

is an invalid
parameter for this engine, or another exception occurs while
trying to get this parameter.
**See Also:** setParameter(String, Object)

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone if the implementation is cloneable.

**Overrides:** clone

in class

SignatureSpi
**Returns:** a clone if the implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called
on an implementation that does not support

Cloneable

.
**See Also:** Cloneable

Field Detail

- UNINITIALIZED

```java
protected static final int UNINITIALIZED
```

Possible

state

value, signifying that
this signature object has not yet been initialized.

**See Also:** Constant Field Values

- SIGN

```java
protected static final int SIGN
```

Possible

state

value, signifying that
this signature object has been initialized for signing.

**See Also:** Constant Field Values

- VERIFY

```java
protected static final int VERIFY
```

Possible

state

value, signifying that
this signature object has been initialized for verification.

**See Also:** Constant Field Values

- state

```java
protected int state
```

Current state of this signature object.

---

#### Field Detail

UNINITIALIZED

```java
protected static final int UNINITIALIZED
```

Possible

state

value, signifying that
this signature object has not yet been initialized.

**See Also:** Constant Field Values

---

#### UNINITIALIZED

protected static final int UNINITIALIZED

Possible

state

value, signifying that
this signature object has not yet been initialized.

SIGN

```java
protected static final int SIGN
```

Possible

state

value, signifying that
this signature object has been initialized for signing.

**See Also:** Constant Field Values

---

#### SIGN

protected static final int SIGN

Possible

state

value, signifying that
this signature object has been initialized for signing.

VERIFY

```java
protected static final int VERIFY
```

Possible

state

value, signifying that
this signature object has been initialized for verification.

**See Also:** Constant Field Values

---

#### VERIFY

protected static final int VERIFY

Possible

state

value, signifying that
this signature object has been initialized for verification.

state

```java
protected int state
```

Current state of this signature object.

---

#### state

protected int state

Current state of this signature object.

Constructor Detail

- Signature

```java
protected Signature​(
String
algorithm)
```

Creates a Signature object for the specified algorithm.

**Parameters:** algorithm

- the standard string name of the algorithm.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

---

#### Constructor Detail

Signature

```java
protected Signature​(
String
algorithm)
```

Creates a Signature object for the specified algorithm.

**Parameters:** algorithm

- the standard string name of the algorithm.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

---

#### Signature

protected Signature​(

String

algorithm)

Creates a Signature object for the specified algorithm.

Method Detail

- getInstance

```java
public static
Signature
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a Signature object that implements the specified signature
algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Signature object encapsulating the
SignatureSpi implementation from the first
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

- the standard name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

Signature

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

Signature

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
Signature
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

Returns a Signature object that implements the specified signature
algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

Signature

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SignatureSpi

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
Signature
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a Signature object that implements the specified
signature algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

Signature

object
**Throws:** IllegalArgumentException

- if the provider is

null
**Throws:** NoSuchAlgorithmException

- if a

SignatureSpi

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

Returns the provider of this signature object.

**Returns:** the provider of this signature object

- initVerify

```java
public final void initVerify​(
PublicKey
publicKey)
throws
InvalidKeyException
```

Initializes this object for verification. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** publicKey

- the public key of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the key is invalid.

- initVerify

```java
public final void initVerify​(
Certificate
certificate)
throws
InvalidKeyException
```

Initializes this object for verification, using the public key from
the given certificate.

If the certificate is of type X.509 and has a

key usage

extension field marked as critical, and the value of the

key usage

extension field implies that the public key in
the certificate and its corresponding private key are not
supposed to be used for digital signatures, an

InvalidKeyException

is thrown.

**Parameters:** certificate

- the certificate of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the public key in the certificate
is not encoded properly or does not include required parameter
information or cannot be used for digital signature purposes.
**Since:** 1.3

- initSign

```java
public final void initSign​(
PrivateKey
privateKey)
throws
InvalidKeyException
```

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** privateKey

- the private key of the identity whose signature
is going to be generated.
**Throws:** InvalidKeyException

- if the key is invalid.

- initSign

```java
public final void initSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException
```

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** privateKey

- the private key of the identity whose signature
is going to be generated.
**Parameters:** random

- the source of randomness for this signature.
**Throws:** InvalidKeyException

- if the key is invalid.

- sign

```java
public final byte[] sign()
throws
SignatureException
```

Returns the signature bytes of all the data updated.
The format of the signature depends on the underlying
signature scheme.

A call to this method resets this signature object to the state
it was in when previously initialized for signing via a
call to

initSign(PrivateKey)

. That is, the object is
reset and available to generate another signature from the same
signer, if desired, via new calls to

update

and

sign

.

**Returns:** the signature bytes of the signing operation's result.
**Throws:** SignatureException

- if this signature object is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

- sign

```java
public final int sign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException
```

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

This signature object is reset to its initial state (the state it
was in after a call to one of the

initSign

methods) and
can be reused to generate further signatures with the same private key.

**Parameters:** outbuf

- buffer for the signature result.
**Parameters:** offset

- offset into

outbuf

where the signature is
stored.
**Parameters:** len

- number of bytes within

outbuf

allotted for the
signature.
**Returns:** the number of bytes placed into

outbuf

.
**Throws:** SignatureException

- if this signature object is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.
**Throws:** IllegalArgumentException

- if

outbuf

is

null

,
or

offset

or

len

is less than 0, or the sum of

offset

and

len

is greater than the length of

outbuf

.
**Since:** 1.2

- verify

```java
public final boolean verify​(byte[] signature)
throws
SignatureException
```

Verifies the passed-in signature.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:** signature

- the signature bytes to be verified.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

- verify

```java
public final boolean verify​(byte[] signature,
int offset,
int length)
throws
SignatureException
```

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:** signature

- the signature bytes to be verified.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** length

- the number of bytes to use, starting at offset.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.
**Throws:** IllegalArgumentException

- if the

signature

byte array is

null

, or the

offset

or

length

is less than 0, or the sum of the

offset

and

length

is greater than the length of the

signature

byte array.
**Since:** 1.4

- update

```java
public final void update​(byte b)
throws
SignatureException
```

Updates the data to be signed or verified by a byte.

**Parameters:** b

- the byte to use for the update.
**Throws:** SignatureException

- if this signature object is not
initialized properly.

- update

```java
public final void update​(byte[] data)
throws
SignatureException
```

Updates the data to be signed or verified, using the specified
array of bytes.

**Parameters:** data

- the byte array to use for the update.
**Throws:** SignatureException

- if this signature object is not
initialized properly.

- update

```java
public final void update​(byte[] data,
int off,
int len)
throws
SignatureException
```

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

**Parameters:** data

- the array of bytes.
**Parameters:** off

- the offset to start from in the array of bytes.
**Parameters:** len

- the number of bytes to use, starting at offset.
**Throws:** SignatureException

- if this signature object is not
initialized properly.
**Throws:** IllegalArgumentException

- if

data

is

null

,
or

off

or

len

is less than 0, or the sum of

off

and

len

is greater than the length of

data

.

- update

```java
public final void update​(
ByteBuffer
data)
throws
SignatureException
```

Updates the data to be signed or verified using the specified
ByteBuffer. Processes the

data.remaining()

bytes
starting at

data.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** data

- the ByteBuffer
**Throws:** SignatureException

- if this signature object is not
initialized properly.
**Since:** 1.5

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the name of the algorithm for this signature object.

**Returns:** the name of the algorithm for this signature object.

- toString

```java
public
String
toString()
```

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this signature object.

- setParameter

```java
@Deprecated

public final void setParameter​(
String
param,

Object
value)
throws
InvalidParameterException
```

Deprecated.

Use

setParameter

.

Sets the specified algorithm parameter to the specified value.
This method supplies a general-purpose mechanism through
which it is possible to set the various parameters of this object.
A parameter may be any settable parameter for the algorithm, such as
a parameter size, or a source of random bits for signature generation
(if appropriate), or an indication of whether or not to perform
a specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

**Parameters:** param

- the string identifier of the parameter.
**Parameters:** value

- the parameter value.
**Throws:** InvalidParameterException

- if

param

is an
invalid parameter for this signature algorithm engine,
the parameter is already set
and cannot be set again, a security exception occurs, and so on.
**See Also:** getParameter(java.lang.String)

- setParameter

```java
public final void setParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this signature engine with the specified parameter set.

**Parameters:** params

- the parameters
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this signature engine
**See Also:** getParameters()

- getParameters

```java
public final
AlgorithmParameters
getParameters()
```

Returns the parameters used with this signature object.

If this signature has been previously initialized with parameters
(by calling the

setParameter

method), this method returns
the same parameters. If this signature has not been initialized with
parameters, this method may return a combination of default and
randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:** the parameters used with this signature, or

null
**Since:** 1.4
**See Also:** setParameter(AlgorithmParameterSpec)

- getParameter

```java
@Deprecated

public final
Object
getParameter​(
String
param)
throws
InvalidParameterException
```

Deprecated.

Gets the value of the specified algorithm parameter. This method
supplies a general-purpose mechanism through which it is possible to
get the various parameters of this object. A parameter may be any
settable parameter for the algorithm, such as a parameter size, or
a source of random bits for signature generation (if appropriate),
or an indication of whether or not to perform a specific but optional
computation. A uniform algorithm-specific naming scheme for each
parameter is desirable but left unspecified at this time.

**Parameters:** param

- the string name of the parameter.
**Returns:** the object that represents the parameter value, or

null

if
there is none.
**Throws:** InvalidParameterException

- if

param

is an invalid
parameter for this engine, or another exception occurs while
trying to get this parameter.
**See Also:** setParameter(String, Object)

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone if the implementation is cloneable.

**Overrides:** clone

in class

SignatureSpi
**Returns:** a clone if the implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called
on an implementation that does not support

Cloneable

.
**See Also:** Cloneable

---

#### Method Detail

getInstance

```java
public static
Signature
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a Signature object that implements the specified signature
algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Signature object encapsulating the
SignatureSpi implementation from the first
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

- the standard name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Returns:** the new

Signature

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

Signature

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

Signature

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a Signature object that implements the specified signature
algorithm.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Signature object encapsulating the
SignatureSpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new Signature object encapsulating the
SignatureSpi implementation from the first
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
Signature
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

Returns a Signature object that implements the specified signature
algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

Signature

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

SignatureSpi

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

Signature

getInstance​(

String

algorithm,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns a Signature object that implements the specified signature
algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new Signature object encapsulating the
SignatureSpi implementation from the specified provider
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
Signature
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a Signature object that implements the specified
signature algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the name of the algorithm requested.
See the Signature section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the new

Signature

object
**Throws:** IllegalArgumentException

- if the provider is

null
**Throws:** NoSuchAlgorithmException

- if a

SignatureSpi

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

Signature

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a Signature object that implements the specified
signature algorithm.

A new Signature object encapsulating the
SignatureSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new Signature object encapsulating the
SignatureSpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this signature object.

**Returns:** the provider of this signature object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this signature object.

initVerify

```java
public final void initVerify​(
PublicKey
publicKey)
throws
InvalidKeyException
```

Initializes this object for verification. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** publicKey

- the public key of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the key is invalid.

---

#### initVerify

public final void initVerify​(

PublicKey

publicKey)
throws

InvalidKeyException

Initializes this object for verification. If this method is called
again with a different argument, it negates the effect
of this call.

initVerify

```java
public final void initVerify​(
Certificate
certificate)
throws
InvalidKeyException
```

Initializes this object for verification, using the public key from
the given certificate.

If the certificate is of type X.509 and has a

key usage

extension field marked as critical, and the value of the

key usage

extension field implies that the public key in
the certificate and its corresponding private key are not
supposed to be used for digital signatures, an

InvalidKeyException

is thrown.

**Parameters:** certificate

- the certificate of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the public key in the certificate
is not encoded properly or does not include required parameter
information or cannot be used for digital signature purposes.
**Since:** 1.3

---

#### initVerify

public final void initVerify​(

Certificate

certificate)
throws

InvalidKeyException

Initializes this object for verification, using the public key from
the given certificate.

If the certificate is of type X.509 and has a

key usage

extension field marked as critical, and the value of the

key usage

extension field implies that the public key in
the certificate and its corresponding private key are not
supposed to be used for digital signatures, an

InvalidKeyException

is thrown.

If the certificate is of type X.509 and has a

key usage

extension field marked as critical, and the value of the

key usage

extension field implies that the public key in
the certificate and its corresponding private key are not
supposed to be used for digital signatures, an

InvalidKeyException

is thrown.

initSign

```java
public final void initSign​(
PrivateKey
privateKey)
throws
InvalidKeyException
```

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** privateKey

- the private key of the identity whose signature
is going to be generated.
**Throws:** InvalidKeyException

- if the key is invalid.

---

#### initSign

public final void initSign​(

PrivateKey

privateKey)
throws

InvalidKeyException

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

initSign

```java
public final void initSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException
```

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

**Parameters:** privateKey

- the private key of the identity whose signature
is going to be generated.
**Parameters:** random

- the source of randomness for this signature.
**Throws:** InvalidKeyException

- if the key is invalid.

---

#### initSign

public final void initSign​(

PrivateKey

privateKey,

SecureRandom

random)
throws

InvalidKeyException

Initialize this object for signing. If this method is called
again with a different argument, it negates the effect
of this call.

sign

```java
public final byte[] sign()
throws
SignatureException
```

Returns the signature bytes of all the data updated.
The format of the signature depends on the underlying
signature scheme.

A call to this method resets this signature object to the state
it was in when previously initialized for signing via a
call to

initSign(PrivateKey)

. That is, the object is
reset and available to generate another signature from the same
signer, if desired, via new calls to

update

and

sign

.

**Returns:** the signature bytes of the signing operation's result.
**Throws:** SignatureException

- if this signature object is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

---

#### sign

public final byte[] sign()
throws

SignatureException

Returns the signature bytes of all the data updated.
The format of the signature depends on the underlying
signature scheme.

A call to this method resets this signature object to the state
it was in when previously initialized for signing via a
call to

initSign(PrivateKey)

. That is, the object is
reset and available to generate another signature from the same
signer, if desired, via new calls to

update

and

sign

.

A call to this method resets this signature object to the state
it was in when previously initialized for signing via a
call to

initSign(PrivateKey)

. That is, the object is
reset and available to generate another signature from the same
signer, if desired, via new calls to

update

and

sign

.

sign

```java
public final int sign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException
```

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

This signature object is reset to its initial state (the state it
was in after a call to one of the

initSign

methods) and
can be reused to generate further signatures with the same private key.

**Parameters:** outbuf

- buffer for the signature result.
**Parameters:** offset

- offset into

outbuf

where the signature is
stored.
**Parameters:** len

- number of bytes within

outbuf

allotted for the
signature.
**Returns:** the number of bytes placed into

outbuf

.
**Throws:** SignatureException

- if this signature object is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.
**Throws:** IllegalArgumentException

- if

outbuf

is

null

,
or

offset

or

len

is less than 0, or the sum of

offset

and

len

is greater than the length of

outbuf

.
**Since:** 1.2

---

#### sign

public final int sign​(byte[] outbuf,
int offset,
int len)
throws

SignatureException

Finishes the signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

This signature object is reset to its initial state (the state it
was in after a call to one of the

initSign

methods) and
can be reused to generate further signatures with the same private key.

This signature object is reset to its initial state (the state it
was in after a call to one of the

initSign

methods) and
can be reused to generate further signatures with the same private key.

verify

```java
public final boolean verify​(byte[] signature)
throws
SignatureException
```

Verifies the passed-in signature.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:** signature

- the signature bytes to be verified.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

---

#### verify

public final boolean verify​(byte[] signature)
throws

SignatureException

Verifies the passed-in signature.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

verify

```java
public final boolean verify​(byte[] signature,
int offset,
int length)
throws
SignatureException
```

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

**Parameters:** signature

- the signature bytes to be verified.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** length

- the number of bytes to use, starting at offset.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if this signature object is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.
**Throws:** IllegalArgumentException

- if the

signature

byte array is

null

, or the

offset

or

length

is less than 0, or the sum of the

offset

and

length

is greater than the length of the

signature

byte array.
**Since:** 1.4

---

#### verify

public final boolean verify​(byte[] signature,
int offset,
int length)
throws

SignatureException

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

A call to this method resets this signature object to the state
it was in when previously initialized for verification via a
call to

initVerify(PublicKey)

. That is, the object is
reset and available to verify another signature from the identity
whose public key was specified in the call to

initVerify

.

update

```java
public final void update​(byte b)
throws
SignatureException
```

Updates the data to be signed or verified by a byte.

**Parameters:** b

- the byte to use for the update.
**Throws:** SignatureException

- if this signature object is not
initialized properly.

---

#### update

public final void update​(byte b)
throws

SignatureException

Updates the data to be signed or verified by a byte.

update

```java
public final void update​(byte[] data)
throws
SignatureException
```

Updates the data to be signed or verified, using the specified
array of bytes.

**Parameters:** data

- the byte array to use for the update.
**Throws:** SignatureException

- if this signature object is not
initialized properly.

---

#### update

public final void update​(byte[] data)
throws

SignatureException

Updates the data to be signed or verified, using the specified
array of bytes.

update

```java
public final void update​(byte[] data,
int off,
int len)
throws
SignatureException
```

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

**Parameters:** data

- the array of bytes.
**Parameters:** off

- the offset to start from in the array of bytes.
**Parameters:** len

- the number of bytes to use, starting at offset.
**Throws:** SignatureException

- if this signature object is not
initialized properly.
**Throws:** IllegalArgumentException

- if

data

is

null

,
or

off

or

len

is less than 0, or the sum of

off

and

len

is greater than the length of

data

.

---

#### update

public final void update​(byte[] data,
int off,
int len)
throws

SignatureException

Updates the data to be signed or verified, using the specified
array of bytes, starting at the specified offset.

update

```java
public final void update​(
ByteBuffer
data)
throws
SignatureException
```

Updates the data to be signed or verified using the specified
ByteBuffer. Processes the

data.remaining()

bytes
starting at

data.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** data

- the ByteBuffer
**Throws:** SignatureException

- if this signature object is not
initialized properly.
**Since:** 1.5

---

#### update

public final void update​(

ByteBuffer

data)
throws

SignatureException

Updates the data to be signed or verified using the specified
ByteBuffer. Processes the

data.remaining()

bytes
starting at

data.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the name of the algorithm for this signature object.

**Returns:** the name of the algorithm for this signature object.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the name of the algorithm for this signature object.

toString

```java
public
String
toString()
```

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this signature object.

---

#### toString

public

String

toString()

Returns a string representation of this signature object,
providing information that includes the state of the object
and the name of the algorithm used.

setParameter

```java
@Deprecated

public final void setParameter​(
String
param,

Object
value)
throws
InvalidParameterException
```

Deprecated.

Use

setParameter

.

Sets the specified algorithm parameter to the specified value.
This method supplies a general-purpose mechanism through
which it is possible to set the various parameters of this object.
A parameter may be any settable parameter for the algorithm, such as
a parameter size, or a source of random bits for signature generation
(if appropriate), or an indication of whether or not to perform
a specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

**Parameters:** param

- the string identifier of the parameter.
**Parameters:** value

- the parameter value.
**Throws:** InvalidParameterException

- if

param

is an
invalid parameter for this signature algorithm engine,
the parameter is already set
and cannot be set again, a security exception occurs, and so on.
**See Also:** getParameter(java.lang.String)

---

#### setParameter

@Deprecated

public final void setParameter​(

String

param,

Object

value)
throws

InvalidParameterException

Sets the specified algorithm parameter to the specified value.
This method supplies a general-purpose mechanism through
which it is possible to set the various parameters of this object.
A parameter may be any settable parameter for the algorithm, such as
a parameter size, or a source of random bits for signature generation
(if appropriate), or an indication of whether or not to perform
a specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

setParameter

```java
public final void setParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this signature engine with the specified parameter set.

**Parameters:** params

- the parameters
**Throws:** InvalidAlgorithmParameterException

- if the given parameters
are inappropriate for this signature engine
**See Also:** getParameters()

---

#### setParameter

public final void setParameter​(

AlgorithmParameterSpec

params)
throws

InvalidAlgorithmParameterException

Initializes this signature engine with the specified parameter set.

getParameters

```java
public final
AlgorithmParameters
getParameters()
```

Returns the parameters used with this signature object.

If this signature has been previously initialized with parameters
(by calling the

setParameter

method), this method returns
the same parameters. If this signature has not been initialized with
parameters, this method may return a combination of default and
randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:** the parameters used with this signature, or

null
**Since:** 1.4
**See Also:** setParameter(AlgorithmParameterSpec)

---

#### getParameters

public final

AlgorithmParameters

getParameters()

Returns the parameters used with this signature object.

If this signature has been previously initialized with parameters
(by calling the

setParameter

method), this method returns
the same parameters. If this signature has not been initialized with
parameters, this method may return a combination of default and
randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

If this signature has been previously initialized with parameters
(by calling the

setParameter

method), this method returns
the same parameters. If this signature has not been initialized with
parameters, this method may return a combination of default and
randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

getParameter

```java
@Deprecated

public final
Object
getParameter​(
String
param)
throws
InvalidParameterException
```

Deprecated.

Gets the value of the specified algorithm parameter. This method
supplies a general-purpose mechanism through which it is possible to
get the various parameters of this object. A parameter may be any
settable parameter for the algorithm, such as a parameter size, or
a source of random bits for signature generation (if appropriate),
or an indication of whether or not to perform a specific but optional
computation. A uniform algorithm-specific naming scheme for each
parameter is desirable but left unspecified at this time.

**Parameters:** param

- the string name of the parameter.
**Returns:** the object that represents the parameter value, or

null

if
there is none.
**Throws:** InvalidParameterException

- if

param

is an invalid
parameter for this engine, or another exception occurs while
trying to get this parameter.
**See Also:** setParameter(String, Object)

---

#### getParameter

@Deprecated

public final

Object

getParameter​(

String

param)
throws

InvalidParameterException

Gets the value of the specified algorithm parameter. This method
supplies a general-purpose mechanism through which it is possible to
get the various parameters of this object. A parameter may be any
settable parameter for the algorithm, such as a parameter size, or
a source of random bits for signature generation (if appropriate),
or an indication of whether or not to perform a specific but optional
computation. A uniform algorithm-specific naming scheme for each
parameter is desirable but left unspecified at this time.

clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone if the implementation is cloneable.

**Overrides:** clone

in class

SignatureSpi
**Returns:** a clone if the implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called
on an implementation that does not support

Cloneable

.
**See Also:** Cloneable

---

#### clone

public

Object

clone()
throws

CloneNotSupportedException

Returns a clone if the implementation is cloneable.

---

