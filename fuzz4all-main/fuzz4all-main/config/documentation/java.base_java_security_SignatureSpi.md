# Class SignatureSpi

**Source:** `java.base\java\security\SignatureSpi.html`

### Class Description

```java
public abstract class
SignatureSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Signature

class, which is used to provide the
functionality of a digital signature algorithm. Digital signatures are used
for authentication and integrity assurance of digital data.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular signature algorithm.

**Direct Known Subclasses:** Signature

---

### Field Details

#### protected
SecureRandom
appRandom

Application-specified source of randomness.

---

### Constructor Details

#### public SignatureSpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInitVerify​(
PublicKey
publicKey)
throws
InvalidKeyException

Initializes this signature object with the specified
public key for verification operations.

**Parameters:**
- publicKey

- the public key of the identity whose signature is
going to be verified.

**Throws:**
- InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

---

#### protected abstract void engineInitSign​(
PrivateKey
privateKey)
throws
InvalidKeyException

Initializes this signature object with the specified
private key for signing operations.

**Parameters:**
- privateKey

- the private key of the identity whose signature
will be generated.

**Throws:**
- InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

---

#### protected void engineInitSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException

Initializes this signature object with the specified
private key and source of randomness for signing operations.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

**Parameters:**
- privateKey

- the private key of the identity whose signature
will be generated.
- random

- the source of randomness

**Throws:**
- InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

---

#### protected abstract void engineUpdate​(byte b)
throws
SignatureException

Updates the data to be signed or verified
using the specified byte.

**Parameters:**
- b

- the byte to use for the update.

**Throws:**
- SignatureException

- if the engine is not initialized
properly.

---

#### protected abstract void engineUpdate​(byte[] b,
int off,
int len)
throws
SignatureException

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

**Parameters:**
- b

- the array of bytes
- off

- the offset to start from in the array of bytes
- len

- the number of bytes to use, starting at offset

**Throws:**
- SignatureException

- if the engine is not initialized
properly

---

#### protected void engineUpdate​(
ByteBuffer
input)

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
- input

- the ByteBuffer

**Since:**
- 1.5

---

#### protected abstract byte[] engineSign()
throws
SignatureException

Returns the signature bytes of all the data
updated so far.
The format of the signature depends on the underlying
signature scheme.

**Returns:**
- the signature bytes of the signing operation's result.

**Throws:**
- SignatureException

- if the engine is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

---

#### protected int engineSign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

The signature implementation is reset to its initial state
(the state it was in after a call to one of the

engineInitSign

methods)
and can be reused to generate further signatures with the same private
key.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

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
Both this default implementation and the SUN provider do not
return partial digests. If the value of this parameter is less
than the actual signature length, this method will throw a
SignatureException.
This parameter is ignored if its value is greater than or equal to
the actual signature length.

**Returns:**
- the number of bytes placed into

outbuf

**Throws:**
- SignatureException

- if the engine is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.

**Since:**
- 1.2

---

#### protected abstract boolean engineVerify​(byte[] sigBytes)
throws
SignatureException

Verifies the passed-in signature.

**Parameters:**
- sigBytes

- the signature bytes to be verified.

**Returns:**
- true if the signature was verified, false if not.

**Throws:**
- SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

---

#### protected boolean engineVerify​(byte[] sigBytes,
int offset,
int length)
throws
SignatureException

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

Note: Subclasses should overwrite the default implementation.

**Parameters:**
- sigBytes

- the signature bytes to be verified.
- offset

- the offset to start from in the array of bytes.
- length

- the number of bytes to use, starting at offset.

**Returns:**
- true if the signature was verified, false if not.

**Throws:**
- SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

**Since:**
- 1.4

---

#### @Deprecated

protected abstract void engineSetParameter​(
String
param,

Object
value)
throws
InvalidParameterException

Sets the specified algorithm parameter to the specified
value. This method supplies a general-purpose mechanism through
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

---

#### protected void engineSetParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

**Parameters:**
- params

- the parameters

**Throws:**
- UnsupportedOperationException

- if this method is not
overridden by a provider
- InvalidAlgorithmParameterException

- if this method is
overridden by a provider and the given parameters
are inappropriate for this signature engine

---

#### protected
AlgorithmParameters
engineGetParameters()

This method is overridden by providers to return the parameters
used with this signature engine.

If this signature engine has been previously initialized with
parameters (by calling the

engineSetParameter

method), this
method returns the same parameters. If this signature engine has not been
initialized with parameters, this method may return a combination of
default and randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:**
- the parameters used with this signature engine, or

null

**Throws:**
- UnsupportedOperationException

- if this method is
not overridden by a provider

**Since:**
- 1.4

---

#### @Deprecated

protected abstract
Object
engineGetParameter​(
String
param)
throws
InvalidParameterException

Gets the value of the specified algorithm parameter.
This method supplies a general-purpose mechanism through which it
is possible to get the various parameters of this object. A parameter
may be any settable parameter for the algorithm, such as a parameter
size, or a source of random bits for signature generation (if
appropriate), or an indication of whether or not to perform a
specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

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

is an
invalid parameter for this engine, or another exception occurs while
trying to get this parameter.

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

Object

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

#### Class SignatureSpi

java.lang.Object

- java.security.SignatureSpi

java.security.SignatureSpi

**Direct Known Subclasses:** Signature

```java
public abstract class
SignatureSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Signature

class, which is used to provide the
functionality of a digital signature algorithm. Digital signatures are used
for authentication and integrity assurance of digital data.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular signature algorithm.

**Since:** 1.2
**See Also:** Signature

public abstract class

SignatureSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

Signature

class, which is used to provide the
functionality of a digital signature algorithm. Digital signatures are used
for authentication and integrity assurance of digital data.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular signature algorithm.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular signature algorithm.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

SecureRandom

appRandom

Application-specified source of randomness.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SignatureSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the implementation is cloneable.

protected abstract

Object

engineGetParameter

​(

String

param)

Deprecated.

protected

AlgorithmParameters

engineGetParameters

()

This method is overridden by providers to return the parameters
used with this signature engine.

protected abstract void

engineInitSign

​(

PrivateKey

privateKey)

Initializes this signature object with the specified
private key for signing operations.

protected void

engineInitSign

​(

PrivateKey

privateKey,

SecureRandom

random)

Initializes this signature object with the specified
private key and source of randomness for signing operations.

protected abstract void

engineInitVerify

​(

PublicKey

publicKey)

Initializes this signature object with the specified
public key for verification operations.

protected abstract void

engineSetParameter

​(

String

param,

Object

value)

Deprecated.

Replaced by

engineSetParameter

.

protected void

engineSetParameter

​(

AlgorithmParameterSpec

params)

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

protected abstract byte[]

engineSign

()

Returns the signature bytes of all the data
updated so far.

protected int

engineSign

​(byte[] outbuf,
int offset,
int len)

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.

protected abstract void

engineUpdate

​(byte b)

Updates the data to be signed or verified
using the specified byte.

protected abstract void

engineUpdate

​(byte[] b,
int off,
int len)

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

protected void

engineUpdate

​(

ByteBuffer

input)

Updates the data to be signed or verified using the specified
ByteBuffer.

protected abstract boolean

engineVerify

​(byte[] sigBytes)

Verifies the passed-in signature.

protected boolean

engineVerify

​(byte[] sigBytes,
int offset,
int length)

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

SecureRandom

appRandom

Application-specified source of randomness.

---

#### Field Summary

Application-specified source of randomness.

Constructor Summary

Constructors

Constructor

Description

SignatureSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the implementation is cloneable.

protected abstract

Object

engineGetParameter

​(

String

param)

Deprecated.

protected

AlgorithmParameters

engineGetParameters

()

This method is overridden by providers to return the parameters
used with this signature engine.

protected abstract void

engineInitSign

​(

PrivateKey

privateKey)

Initializes this signature object with the specified
private key for signing operations.

protected void

engineInitSign

​(

PrivateKey

privateKey,

SecureRandom

random)

Initializes this signature object with the specified
private key and source of randomness for signing operations.

protected abstract void

engineInitVerify

​(

PublicKey

publicKey)

Initializes this signature object with the specified
public key for verification operations.

protected abstract void

engineSetParameter

​(

String

param,

Object

value)

Deprecated.

Replaced by

engineSetParameter

.

protected void

engineSetParameter

​(

AlgorithmParameterSpec

params)

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

protected abstract byte[]

engineSign

()

Returns the signature bytes of all the data
updated so far.

protected int

engineSign

​(byte[] outbuf,
int offset,
int len)

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.

protected abstract void

engineUpdate

​(byte b)

Updates the data to be signed or verified
using the specified byte.

protected abstract void

engineUpdate

​(byte[] b,
int off,
int len)

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

protected void

engineUpdate

​(

ByteBuffer

input)

Updates the data to be signed or verified using the specified
ByteBuffer.

protected abstract boolean

engineVerify

​(byte[] sigBytes)

Verifies the passed-in signature.

protected boolean

engineVerify

​(byte[] sigBytes,
int offset,
int length)

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

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

Returns a clone if the implementation is cloneable.

Deprecated.

This method is overridden by providers to return the parameters
used with this signature engine.

Initializes this signature object with the specified
private key for signing operations.

Initializes this signature object with the specified
private key and source of randomness for signing operations.

Initializes this signature object with the specified
public key for verification operations.

Deprecated.

Replaced by

engineSetParameter

.

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

Returns the signature bytes of all the data
updated so far.

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.

Updates the data to be signed or verified
using the specified byte.

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

Updates the data to be signed or verified using the specified
ByteBuffer.

Verifies the passed-in signature.

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

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

============ FIELD DETAIL ===========

- Field Detail

- appRandom

```java
protected
SecureRandom
appRandom
```

Application-specified source of randomness.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SignatureSpi

```java
public SignatureSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInitVerify

```java
protected abstract void engineInitVerify​(
PublicKey
publicKey)
throws
InvalidKeyException
```

Initializes this signature object with the specified
public key for verification operations.

**Parameters:** publicKey

- the public key of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

- engineInitSign

```java
protected abstract void engineInitSign​(
PrivateKey
privateKey)
throws
InvalidKeyException
```

Initializes this signature object with the specified
private key for signing operations.

**Parameters:** privateKey

- the private key of the identity whose signature
will be generated.
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

- engineInitSign

```java
protected void engineInitSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException
```

Initializes this signature object with the specified
private key and source of randomness for signing operations.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

**Parameters:** privateKey

- the private key of the identity whose signature
will be generated.
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

- engineUpdate

```java
protected abstract void engineUpdate​(byte b)
throws
SignatureException
```

Updates the data to be signed or verified
using the specified byte.

**Parameters:** b

- the byte to use for the update.
**Throws:** SignatureException

- if the engine is not initialized
properly.

- engineUpdate

```java
protected abstract void engineUpdate​(byte[] b,
int off,
int len)
throws
SignatureException
```

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

**Parameters:** b

- the array of bytes
**Parameters:** off

- the offset to start from in the array of bytes
**Parameters:** len

- the number of bytes to use, starting at offset
**Throws:** SignatureException

- if the engine is not initialized
properly

- engineUpdate

```java
protected void engineUpdate​(
ByteBuffer
input)
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

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

- engineSign

```java
protected abstract byte[] engineSign()
throws
SignatureException
```

Returns the signature bytes of all the data
updated so far.
The format of the signature depends on the underlying
signature scheme.

**Returns:** the signature bytes of the signing operation's result.
**Throws:** SignatureException

- if the engine is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

- engineSign

```java
protected int engineSign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException
```

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

The signature implementation is reset to its initial state
(the state it was in after a call to one of the

engineInitSign

methods)
and can be reused to generate further signatures with the same private
key.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

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
Both this default implementation and the SUN provider do not
return partial digests. If the value of this parameter is less
than the actual signature length, this method will throw a
SignatureException.
This parameter is ignored if its value is greater than or equal to
the actual signature length.
**Returns:** the number of bytes placed into

outbuf
**Throws:** SignatureException

- if the engine is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.
**Since:** 1.2

- engineVerify

```java
protected abstract boolean engineVerify​(byte[] sigBytes)
throws
SignatureException
```

Verifies the passed-in signature.

**Parameters:** sigBytes

- the signature bytes to be verified.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

- engineVerify

```java
protected boolean engineVerify​(byte[] sigBytes,
int offset,
int length)
throws
SignatureException
```

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

Note: Subclasses should overwrite the default implementation.

**Parameters:** sigBytes

- the signature bytes to be verified.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** length

- the number of bytes to use, starting at offset.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.
**Since:** 1.4

- engineSetParameter

```java
@Deprecated

protected abstract void engineSetParameter​(
String
param,

Object
value)
throws
InvalidParameterException
```

Deprecated.

Replaced by

engineSetParameter

.

Sets the specified algorithm parameter to the specified
value. This method supplies a general-purpose mechanism through
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

- engineSetParameter

```java
protected void engineSetParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

**Parameters:** params

- the parameters
**Throws:** UnsupportedOperationException

- if this method is not
overridden by a provider
**Throws:** InvalidAlgorithmParameterException

- if this method is
overridden by a provider and the given parameters
are inappropriate for this signature engine

- engineGetParameters

```java
protected
AlgorithmParameters
engineGetParameters()
```

This method is overridden by providers to return the parameters
used with this signature engine.

If this signature engine has been previously initialized with
parameters (by calling the

engineSetParameter

method), this
method returns the same parameters. If this signature engine has not been
initialized with parameters, this method may return a combination of
default and randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:** the parameters used with this signature engine, or

null
**Throws:** UnsupportedOperationException

- if this method is
not overridden by a provider
**Since:** 1.4

- engineGetParameter

```java
@Deprecated

protected abstract
Object
engineGetParameter​(
String
param)
throws
InvalidParameterException
```

Deprecated.

Gets the value of the specified algorithm parameter.
This method supplies a general-purpose mechanism through which it
is possible to get the various parameters of this object. A parameter
may be any settable parameter for the algorithm, such as a parameter
size, or a source of random bits for signature generation (if
appropriate), or an indication of whether or not to perform a
specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

**Parameters:** param

- the string name of the parameter.
**Returns:** the object that represents the parameter value, or

null

if
there is none.
**Throws:** InvalidParameterException

- if

param

is an
invalid parameter for this engine, or another exception occurs while
trying to get this parameter.

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

Object
**Returns:** a clone if the implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called
on an implementation that does not support

Cloneable

.
**See Also:** Cloneable

Field Detail

- appRandom

```java
protected
SecureRandom
appRandom
```

Application-specified source of randomness.

---

#### Field Detail

appRandom

```java
protected
SecureRandom
appRandom
```

Application-specified source of randomness.

---

#### appRandom

protected

SecureRandom

appRandom

Application-specified source of randomness.

Constructor Detail

- SignatureSpi

```java
public SignatureSpi()
```

---

#### Constructor Detail

SignatureSpi

```java
public SignatureSpi()
```

---

#### SignatureSpi

public SignatureSpi()

Method Detail

- engineInitVerify

```java
protected abstract void engineInitVerify​(
PublicKey
publicKey)
throws
InvalidKeyException
```

Initializes this signature object with the specified
public key for verification operations.

**Parameters:** publicKey

- the public key of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

- engineInitSign

```java
protected abstract void engineInitSign​(
PrivateKey
privateKey)
throws
InvalidKeyException
```

Initializes this signature object with the specified
private key for signing operations.

**Parameters:** privateKey

- the private key of the identity whose signature
will be generated.
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

- engineInitSign

```java
protected void engineInitSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException
```

Initializes this signature object with the specified
private key and source of randomness for signing operations.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

**Parameters:** privateKey

- the private key of the identity whose signature
will be generated.
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

- engineUpdate

```java
protected abstract void engineUpdate​(byte b)
throws
SignatureException
```

Updates the data to be signed or verified
using the specified byte.

**Parameters:** b

- the byte to use for the update.
**Throws:** SignatureException

- if the engine is not initialized
properly.

- engineUpdate

```java
protected abstract void engineUpdate​(byte[] b,
int off,
int len)
throws
SignatureException
```

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

**Parameters:** b

- the array of bytes
**Parameters:** off

- the offset to start from in the array of bytes
**Parameters:** len

- the number of bytes to use, starting at offset
**Throws:** SignatureException

- if the engine is not initialized
properly

- engineUpdate

```java
protected void engineUpdate​(
ByteBuffer
input)
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

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

- engineSign

```java
protected abstract byte[] engineSign()
throws
SignatureException
```

Returns the signature bytes of all the data
updated so far.
The format of the signature depends on the underlying
signature scheme.

**Returns:** the signature bytes of the signing operation's result.
**Throws:** SignatureException

- if the engine is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

- engineSign

```java
protected int engineSign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException
```

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

The signature implementation is reset to its initial state
(the state it was in after a call to one of the

engineInitSign

methods)
and can be reused to generate further signatures with the same private
key.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

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
Both this default implementation and the SUN provider do not
return partial digests. If the value of this parameter is less
than the actual signature length, this method will throw a
SignatureException.
This parameter is ignored if its value is greater than or equal to
the actual signature length.
**Returns:** the number of bytes placed into

outbuf
**Throws:** SignatureException

- if the engine is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.
**Since:** 1.2

- engineVerify

```java
protected abstract boolean engineVerify​(byte[] sigBytes)
throws
SignatureException
```

Verifies the passed-in signature.

**Parameters:** sigBytes

- the signature bytes to be verified.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

- engineVerify

```java
protected boolean engineVerify​(byte[] sigBytes,
int offset,
int length)
throws
SignatureException
```

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

Note: Subclasses should overwrite the default implementation.

**Parameters:** sigBytes

- the signature bytes to be verified.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** length

- the number of bytes to use, starting at offset.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.
**Since:** 1.4

- engineSetParameter

```java
@Deprecated

protected abstract void engineSetParameter​(
String
param,

Object
value)
throws
InvalidParameterException
```

Deprecated.

Replaced by

engineSetParameter

.

Sets the specified algorithm parameter to the specified
value. This method supplies a general-purpose mechanism through
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

- engineSetParameter

```java
protected void engineSetParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

**Parameters:** params

- the parameters
**Throws:** UnsupportedOperationException

- if this method is not
overridden by a provider
**Throws:** InvalidAlgorithmParameterException

- if this method is
overridden by a provider and the given parameters
are inappropriate for this signature engine

- engineGetParameters

```java
protected
AlgorithmParameters
engineGetParameters()
```

This method is overridden by providers to return the parameters
used with this signature engine.

If this signature engine has been previously initialized with
parameters (by calling the

engineSetParameter

method), this
method returns the same parameters. If this signature engine has not been
initialized with parameters, this method may return a combination of
default and randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:** the parameters used with this signature engine, or

null
**Throws:** UnsupportedOperationException

- if this method is
not overridden by a provider
**Since:** 1.4

- engineGetParameter

```java
@Deprecated

protected abstract
Object
engineGetParameter​(
String
param)
throws
InvalidParameterException
```

Deprecated.

Gets the value of the specified algorithm parameter.
This method supplies a general-purpose mechanism through which it
is possible to get the various parameters of this object. A parameter
may be any settable parameter for the algorithm, such as a parameter
size, or a source of random bits for signature generation (if
appropriate), or an indication of whether or not to perform a
specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

**Parameters:** param

- the string name of the parameter.
**Returns:** the object that represents the parameter value, or

null

if
there is none.
**Throws:** InvalidParameterException

- if

param

is an
invalid parameter for this engine, or another exception occurs while
trying to get this parameter.

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

Object
**Returns:** a clone if the implementation is cloneable.
**Throws:** CloneNotSupportedException

- if this is called
on an implementation that does not support

Cloneable

.
**See Also:** Cloneable

---

#### Method Detail

engineInitVerify

```java
protected abstract void engineInitVerify​(
PublicKey
publicKey)
throws
InvalidKeyException
```

Initializes this signature object with the specified
public key for verification operations.

**Parameters:** publicKey

- the public key of the identity whose signature is
going to be verified.
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

---

#### engineInitVerify

protected abstract void engineInitVerify​(

PublicKey

publicKey)
throws

InvalidKeyException

Initializes this signature object with the specified
public key for verification operations.

engineInitSign

```java
protected abstract void engineInitSign​(
PrivateKey
privateKey)
throws
InvalidKeyException
```

Initializes this signature object with the specified
private key for signing operations.

**Parameters:** privateKey

- the private key of the identity whose signature
will be generated.
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

---

#### engineInitSign

protected abstract void engineInitSign​(

PrivateKey

privateKey)
throws

InvalidKeyException

Initializes this signature object with the specified
private key for signing operations.

engineInitSign

```java
protected void engineInitSign​(
PrivateKey
privateKey,

SecureRandom
random)
throws
InvalidKeyException
```

Initializes this signature object with the specified
private key and source of randomness for signing operations.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

**Parameters:** privateKey

- the private key of the identity whose signature
will be generated.
**Parameters:** random

- the source of randomness
**Throws:** InvalidKeyException

- if the key is improperly
encoded, parameters are missing, and so on.

---

#### engineInitSign

protected void engineInitSign​(

PrivateKey

privateKey,

SecureRandom

random)
throws

InvalidKeyException

Initializes this signature object with the specified
private key and source of randomness for signing operations.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

engineUpdate

```java
protected abstract void engineUpdate​(byte b)
throws
SignatureException
```

Updates the data to be signed or verified
using the specified byte.

**Parameters:** b

- the byte to use for the update.
**Throws:** SignatureException

- if the engine is not initialized
properly.

---

#### engineUpdate

protected abstract void engineUpdate​(byte b)
throws

SignatureException

Updates the data to be signed or verified
using the specified byte.

engineUpdate

```java
protected abstract void engineUpdate​(byte[] b,
int off,
int len)
throws
SignatureException
```

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

**Parameters:** b

- the array of bytes
**Parameters:** off

- the offset to start from in the array of bytes
**Parameters:** len

- the number of bytes to use, starting at offset
**Throws:** SignatureException

- if the engine is not initialized
properly

---

#### engineUpdate

protected abstract void engineUpdate​(byte[] b,
int off,
int len)
throws

SignatureException

Updates the data to be signed or verified, using the
specified array of bytes, starting at the specified offset.

engineUpdate

```java
protected void engineUpdate​(
ByteBuffer
input)
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

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

---

#### engineUpdate

protected void engineUpdate​(

ByteBuffer

input)

Updates the data to be signed or verified using the specified
ByteBuffer. Processes the

data.remaining()

bytes
starting at

data.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

engineSign

```java
protected abstract byte[] engineSign()
throws
SignatureException
```

Returns the signature bytes of all the data
updated so far.
The format of the signature depends on the underlying
signature scheme.

**Returns:** the signature bytes of the signing operation's result.
**Throws:** SignatureException

- if the engine is not
initialized properly or if this signature algorithm is unable to
process the input data provided.

---

#### engineSign

protected abstract byte[] engineSign()
throws

SignatureException

Returns the signature bytes of all the data
updated so far.
The format of the signature depends on the underlying
signature scheme.

engineSign

```java
protected int engineSign​(byte[] outbuf,
int offset,
int len)
throws
SignatureException
```

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

The signature implementation is reset to its initial state
(the state it was in after a call to one of the

engineInitSign

methods)
and can be reused to generate further signatures with the same private
key.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

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
Both this default implementation and the SUN provider do not
return partial digests. If the value of this parameter is less
than the actual signature length, this method will throw a
SignatureException.
This parameter is ignored if its value is greater than or equal to
the actual signature length.
**Returns:** the number of bytes placed into

outbuf
**Throws:** SignatureException

- if the engine is not
initialized properly, if this signature algorithm is unable to
process the input data provided, or if

len

is less
than the actual signature length.
**Since:** 1.2

---

#### engineSign

protected int engineSign​(byte[] outbuf,
int offset,
int len)
throws

SignatureException

Finishes this signature operation and stores the resulting signature
bytes in the provided buffer

outbuf

, starting at

offset

.
The format of the signature depends on the underlying
signature scheme.

The signature implementation is reset to its initial state
(the state it was in after a call to one of the

engineInitSign

methods)
and can be reused to generate further signatures with the same private
key.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

The signature implementation is reset to its initial state
(the state it was in after a call to one of the

engineInitSign

methods)
and can be reused to generate further signatures with the same private
key.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

engineVerify

```java
protected abstract boolean engineVerify​(byte[] sigBytes)
throws
SignatureException
```

Verifies the passed-in signature.

**Parameters:** sigBytes

- the signature bytes to be verified.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.

---

#### engineVerify

protected abstract boolean engineVerify​(byte[] sigBytes)
throws

SignatureException

Verifies the passed-in signature.

engineVerify

```java
protected boolean engineVerify​(byte[] sigBytes,
int offset,
int length)
throws
SignatureException
```

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

Note: Subclasses should overwrite the default implementation.

**Parameters:** sigBytes

- the signature bytes to be verified.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** length

- the number of bytes to use, starting at offset.
**Returns:** true if the signature was verified, false if not.
**Throws:** SignatureException

- if the engine is not
initialized properly, the passed-in signature is improperly
encoded or of the wrong type, if this signature algorithm is unable to
process the input data provided, etc.
**Since:** 1.4

---

#### engineVerify

protected boolean engineVerify​(byte[] sigBytes,
int offset,
int length)
throws

SignatureException

Verifies the passed-in signature in the specified array
of bytes, starting at the specified offset.

Note: Subclasses should overwrite the default implementation.

Note: Subclasses should overwrite the default implementation.

engineSetParameter

```java
@Deprecated

protected abstract void engineSetParameter​(
String
param,

Object
value)
throws
InvalidParameterException
```

Deprecated.

Replaced by

engineSetParameter

.

Sets the specified algorithm parameter to the specified
value. This method supplies a general-purpose mechanism through
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

---

#### engineSetParameter

@Deprecated

protected abstract void engineSetParameter​(

String

param,

Object

value)
throws

InvalidParameterException

Sets the specified algorithm parameter to the specified
value. This method supplies a general-purpose mechanism through
which it is possible to set the various parameters of this object.
A parameter may be any settable parameter for the algorithm, such as
a parameter size, or a source of random bits for signature generation
(if appropriate), or an indication of whether or not to perform
a specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

engineSetParameter

```java
protected void engineSetParameter​(
AlgorithmParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

**Parameters:** params

- the parameters
**Throws:** UnsupportedOperationException

- if this method is not
overridden by a provider
**Throws:** InvalidAlgorithmParameterException

- if this method is
overridden by a provider and the given parameters
are inappropriate for this signature engine

---

#### engineSetParameter

protected void engineSetParameter​(

AlgorithmParameterSpec

params)
throws

InvalidAlgorithmParameterException

This method is overridden by providers to initialize
this signature engine with the specified parameter set.

engineGetParameters

```java
protected
AlgorithmParameters
engineGetParameters()
```

This method is overridden by providers to return the parameters
used with this signature engine.

If this signature engine has been previously initialized with
parameters (by calling the

engineSetParameter

method), this
method returns the same parameters. If this signature engine has not been
initialized with parameters, this method may return a combination of
default and randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

**Returns:** the parameters used with this signature engine, or

null
**Throws:** UnsupportedOperationException

- if this method is
not overridden by a provider
**Since:** 1.4

---

#### engineGetParameters

protected

AlgorithmParameters

engineGetParameters()

This method is overridden by providers to return the parameters
used with this signature engine.

If this signature engine has been previously initialized with
parameters (by calling the

engineSetParameter

method), this
method returns the same parameters. If this signature engine has not been
initialized with parameters, this method may return a combination of
default and randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

If this signature engine has been previously initialized with
parameters (by calling the

engineSetParameter

method), this
method returns the same parameters. If this signature engine has not been
initialized with parameters, this method may return a combination of
default and randomly generated parameter values if the underlying
signature implementation supports it and can successfully generate
them. Otherwise,

null

is returned.

engineGetParameter

```java
@Deprecated

protected abstract
Object
engineGetParameter​(
String
param)
throws
InvalidParameterException
```

Deprecated.

Gets the value of the specified algorithm parameter.
This method supplies a general-purpose mechanism through which it
is possible to get the various parameters of this object. A parameter
may be any settable parameter for the algorithm, such as a parameter
size, or a source of random bits for signature generation (if
appropriate), or an indication of whether or not to perform a
specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

**Parameters:** param

- the string name of the parameter.
**Returns:** the object that represents the parameter value, or

null

if
there is none.
**Throws:** InvalidParameterException

- if

param

is an
invalid parameter for this engine, or another exception occurs while
trying to get this parameter.

---

#### engineGetParameter

@Deprecated

protected abstract

Object

engineGetParameter​(

String

param)
throws

InvalidParameterException

Gets the value of the specified algorithm parameter.
This method supplies a general-purpose mechanism through which it
is possible to get the various parameters of this object. A parameter
may be any settable parameter for the algorithm, such as a parameter
size, or a source of random bits for signature generation (if
appropriate), or an indication of whether or not to perform a
specific but optional computation. A uniform algorithm-specific
naming scheme for each parameter is desirable but left unspecified
at this time.

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

Object
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

