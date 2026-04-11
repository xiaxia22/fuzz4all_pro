# Class KeyAgreementSpi

**Source:** `java.base\javax\crypto\KeyAgreementSpi.html`

### Class Description

```java
public abstract class
KeyAgreementSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyAgreement

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular key agreement algorithm.

The keys involved in establishing a shared secret are created by one
of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol
(

engineDoPhase

).

For each of the correspondents in the key exchange,

engineDoPhase

needs to be called. For example, if the key exchange is with one other
party,

engineDoPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If the key exchange is
with two other parties,

engineDoPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

**Since:** 1.4
**See Also:** KeyGenerator

,

SecretKey

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyAgreementSpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInit​(
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

#### protected abstract void engineInit​(
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

#### protected abstract
Key
engineDoPhase​(
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
- the (intermediate) key resulting from this phase, or null if
this phase does not yield a key

**Throws:**
- InvalidKeyException

- if the given key is inappropriate for
this phase.
- IllegalStateException

- if this key agreement has not been
initialized.

---

#### protected abstract byte[] engineGenerateSecret()
throws
IllegalStateException

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

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

#### protected abstract int engineGenerateSecret​(byte[] sharedSecret,
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

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

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

#### protected abstract
SecretKey
engineGenerateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:**
- algorithm

- the requested secret key algorithm

**Returns:**
- the shared secret key

**Throws:**
- IllegalStateException

- if this key agreement has not been
completed yet
- NoSuchAlgorithmException

- if the requested secret key
algorithm is not available
- InvalidKeyException

- if the shared secret key material cannot
be used to generate a secret key of the requested algorithm type (e.g.,
the key material is too short)

---

### Additional Sections

#### Class KeyAgreementSpi

java.lang.Object

- javax.crypto.KeyAgreementSpi

javax.crypto.KeyAgreementSpi

```java
public abstract class
KeyAgreementSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyAgreement

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular key agreement algorithm.

The keys involved in establishing a shared secret are created by one
of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol
(

engineDoPhase

).

For each of the correspondents in the key exchange,

engineDoPhase

needs to be called. For example, if the key exchange is with one other
party,

engineDoPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If the key exchange is
with two other parties,

engineDoPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

**Since:** 1.4
**See Also:** KeyGenerator

,

SecretKey

public abstract class

KeyAgreementSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyAgreement

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular key agreement algorithm.

The keys involved in establishing a shared secret are created by one
of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol
(

engineDoPhase

).

For each of the correspondents in the key exchange,

engineDoPhase

needs to be called. For example, if the key exchange is with one other
party,

engineDoPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If the key exchange is
with two other parties,

engineDoPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

The keys involved in establishing a shared secret are created by one
of the
key generators (

KeyPairGenerator

or

KeyGenerator

), a

KeyFactory

, or as a result from
an intermediate phase of the key agreement protocol
(

engineDoPhase

).

For each of the correspondents in the key exchange,

engineDoPhase

needs to be called. For example, if the key exchange is with one other
party,

engineDoPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If the key exchange is
with two other parties,

engineDoPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

For each of the correspondents in the key exchange,

engineDoPhase

needs to be called. For example, if the key exchange is with one other
party,

engineDoPhase

needs to be called once, with the

lastPhase

flag set to

true

.
If the key exchange is
with two other parties,

engineDoPhase

needs to be called twice,
the first time setting the

lastPhase

flag to

false

, and the second time setting it to

true

.
There may be any number of parties involved in a key exchange.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyAgreementSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

Key

engineDoPhase

​(

Key

key,
boolean lastPhase)

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

protected abstract byte[]

engineGenerateSecret

()

Generates the shared secret and returns it in a new buffer.

protected abstract int

engineGenerateSecret

​(byte[] sharedSecret,
int offset)

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

protected abstract

SecretKey

engineGenerateSecret

​(

String

algorithm)

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

protected abstract void

engineInit

​(

Key

key,

SecureRandom

random)

Initializes this key agreement with the given key and source of
randomness.

protected abstract void

engineInit

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

Constructor

Description

KeyAgreementSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

Key

engineDoPhase

​(

Key

key,
boolean lastPhase)

Executes the next phase of this key agreement with the given
key that was received from one of the other parties involved in this key
agreement.

protected abstract byte[]

engineGenerateSecret

()

Generates the shared secret and returns it in a new buffer.

protected abstract int

engineGenerateSecret

​(byte[] sharedSecret,
int offset)

Generates the shared secret, and places it into the buffer

sharedSecret

, beginning at

offset

inclusive.

protected abstract

SecretKey

engineGenerateSecret

​(

String

algorithm)

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

protected abstract void

engineInit

​(

Key

key,

SecureRandom

random)

Initializes this key agreement with the given key and source of
randomness.

protected abstract void

engineInit

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

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

Initializes this key agreement with the given key and source of
randomness.

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

- KeyAgreementSpi

```java
public KeyAgreementSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInit

```java
protected abstract void engineInit​(
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

- engineInit

```java
protected abstract void engineInit​(
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

- engineDoPhase

```java
protected abstract
Key
engineDoPhase​(
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
**Returns:** the (intermediate) key resulting from this phase, or null if
this phase does not yield a key
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this phase.
**Throws:** IllegalStateException

- if this key agreement has not been
initialized.

- engineGenerateSecret

```java
protected abstract byte[] engineGenerateSecret()
throws
IllegalStateException
```

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Returns:** the new buffer with the shared secret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet

- engineGenerateSecret

```java
protected abstract int engineGenerateSecret​(byte[] sharedSecret,
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

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

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

- engineGenerateSecret

```java
protected abstract
SecretKey
engineGenerateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** algorithm

- the requested secret key algorithm
**Returns:** the shared secret key
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** NoSuchAlgorithmException

- if the requested secret key
algorithm is not available
**Throws:** InvalidKeyException

- if the shared secret key material cannot
be used to generate a secret key of the requested algorithm type (e.g.,
the key material is too short)

Constructor Detail

- KeyAgreementSpi

```java
public KeyAgreementSpi()
```

---

#### Constructor Detail

KeyAgreementSpi

```java
public KeyAgreementSpi()
```

---

#### KeyAgreementSpi

public KeyAgreementSpi()

Method Detail

- engineInit

```java
protected abstract void engineInit​(
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

- engineInit

```java
protected abstract void engineInit​(
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

- engineDoPhase

```java
protected abstract
Key
engineDoPhase​(
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
**Returns:** the (intermediate) key resulting from this phase, or null if
this phase does not yield a key
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this phase.
**Throws:** IllegalStateException

- if this key agreement has not been
initialized.

- engineGenerateSecret

```java
protected abstract byte[] engineGenerateSecret()
throws
IllegalStateException
```

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Returns:** the new buffer with the shared secret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet

- engineGenerateSecret

```java
protected abstract int engineGenerateSecret​(byte[] sharedSecret,
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

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

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

- engineGenerateSecret

```java
protected abstract
SecretKey
engineGenerateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** algorithm

- the requested secret key algorithm
**Returns:** the shared secret key
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** NoSuchAlgorithmException

- if the requested secret key
algorithm is not available
**Throws:** InvalidKeyException

- if the shared secret key material cannot
be used to generate a secret key of the requested algorithm type (e.g.,
the key material is too short)

---

#### Method Detail

engineInit

```java
protected abstract void engineInit​(
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

#### engineInit

protected abstract void engineInit​(

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

engineInit

```java
protected abstract void engineInit​(
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

#### engineInit

protected abstract void engineInit​(

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

engineDoPhase

```java
protected abstract
Key
engineDoPhase​(
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
**Returns:** the (intermediate) key resulting from this phase, or null if
this phase does not yield a key
**Throws:** InvalidKeyException

- if the given key is inappropriate for
this phase.
**Throws:** IllegalStateException

- if this key agreement has not been
initialized.

---

#### engineDoPhase

protected abstract

Key

engineDoPhase​(

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

engineGenerateSecret

```java
protected abstract byte[] engineGenerateSecret()
throws
IllegalStateException
```

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Returns:** the new buffer with the shared secret
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet

---

#### engineGenerateSecret

protected abstract byte[] engineGenerateSecret()
throws

IllegalStateException

Generates the shared secret and returns it in a new buffer.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

engineGenerateSecret

```java
protected abstract int engineGenerateSecret​(byte[] sharedSecret,
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

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

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

#### engineGenerateSecret

protected abstract int engineGenerateSecret​(byte[] sharedSecret,
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

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

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

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

engineGenerateSecret

```java
protected abstract
SecretKey
engineGenerateSecret​(
String
algorithm)
throws
IllegalStateException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

**Parameters:** algorithm

- the requested secret key algorithm
**Returns:** the shared secret key
**Throws:** IllegalStateException

- if this key agreement has not been
completed yet
**Throws:** NoSuchAlgorithmException

- if the requested secret key
algorithm is not available
**Throws:** InvalidKeyException

- if the shared secret key material cannot
be used to generate a secret key of the requested algorithm type (e.g.,
the key material is too short)

---

#### engineGenerateSecret

protected abstract

SecretKey

engineGenerateSecret​(

String

algorithm)
throws

IllegalStateException

,

NoSuchAlgorithmException

,

InvalidKeyException

Creates the shared secret and returns it as a secret key object
of the requested algorithm type.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

This method resets this

KeyAgreementSpi

object,
so that it
can be reused for further key agreements. Unless this key agreement is
reinitialized with one of the

engineInit

methods, the same
private information and algorithm parameters will be used for
subsequent key agreements.

---

