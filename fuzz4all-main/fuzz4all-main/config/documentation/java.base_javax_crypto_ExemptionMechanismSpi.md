# Class ExemptionMechanismSpi

**Source:** `java.base\javax\crypto\ExemptionMechanismSpi.html`

### Class Description

```java
public abstract class
ExemptionMechanismSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

ExemptionMechanism

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular exemption mechanism.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public ExemptionMechanismSpi()

*No description found.*

---

### Method Details

#### protected abstract int engineGetOutputSize​(int inputLen)

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

engineGenExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:**
- inputLen

- the input length (in bytes)

**Returns:**
- the required output buffer size (in bytes)

---

#### protected abstract void engineInit​(
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

, the underlying
exemption mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

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

#### protected abstract void engineInit​(
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

If this exemption mechanism requires any algorithm parameters and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

#### protected abstract void engineInit​(
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
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

#### protected abstract byte[] engineGenExemptionBlob()
throws
ExemptionMechanismException

Generates the exemption mechanism key blob.

**Returns:**
- the new buffer with the result key blob.

**Throws:**
- ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### protected abstract int engineGenExemptionBlob​(byte[] output,
int outputOffset)
throws
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

engineGetOutputSize

to determine
how big the output buffer should be.

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
- ShortBufferException

- if the given output buffer is too small
to hold the result.
- ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

### Additional Sections

#### Class ExemptionMechanismSpi

java.lang.Object

- javax.crypto.ExemptionMechanismSpi

javax.crypto.ExemptionMechanismSpi

```java
public abstract class
ExemptionMechanismSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

ExemptionMechanism

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular exemption mechanism.

**Since:** 1.4

public abstract class

ExemptionMechanismSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

ExemptionMechanism

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular exemption mechanism.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ExemptionMechanismSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract byte[]

engineGenExemptionBlob

()

Generates the exemption mechanism key blob.

protected abstract int

engineGenExemptionBlob

​(byte[] output,
int outputOffset)

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

protected abstract int

engineGetOutputSize

​(int inputLen)

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

protected abstract void

engineInit

​(

Key

key)

Initializes this exemption mechanism with a key.

protected abstract void

engineInit

​(

Key

key,

AlgorithmParameters

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

protected abstract void

engineInit

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

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

ExemptionMechanismSpi

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

protected abstract byte[]

engineGenExemptionBlob

()

Generates the exemption mechanism key blob.

protected abstract int

engineGenExemptionBlob

​(byte[] output,
int outputOffset)

Generates the exemption mechanism key blob, and stores the result in
the

output

buffer, starting at

outputOffset

inclusive.

protected abstract int

engineGetOutputSize

​(int inputLen)

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

protected abstract void

engineInit

​(

Key

key)

Initializes this exemption mechanism with a key.

protected abstract void

engineInit

​(

Key

key,

AlgorithmParameters

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

protected abstract void

engineInit

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

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

buffer, starting at

outputOffset

inclusive.

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

Initializes this exemption mechanism with a key.

Initializes this exemption mechanism with a key and a set of algorithm
parameters.

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

- ExemptionMechanismSpi

```java
public ExemptionMechanismSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineGetOutputSize

```java
protected abstract int engineGetOutputSize​(int inputLen)
```

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

engineGenExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:** inputLen

- the input length (in bytes)
**Returns:** the required output buffer size (in bytes)

- engineInit

```java
protected abstract void engineInit​(
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

, the underlying
exemption mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

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

- engineInit

```java
protected abstract void engineInit​(
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

If this exemption mechanism requires any algorithm parameters and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

- engineInit

```java
protected abstract void engineInit​(
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
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

- engineGenExemptionBlob

```java
protected abstract byte[] engineGenExemptionBlob()
throws
ExemptionMechanismException
```

Generates the exemption mechanism key blob.

**Returns:** the new buffer with the result key blob.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

- engineGenExemptionBlob

```java
protected abstract int engineGenExemptionBlob​(byte[] output,
int outputOffset)
throws
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

engineGetOutputSize

to determine
how big the output buffer should be.

**Parameters:** output

- the buffer for the result
**Parameters:** outputOffset

- the offset in

output

where the result
is stored
**Returns:** the number of bytes stored in

output
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

Constructor Detail

- ExemptionMechanismSpi

```java
public ExemptionMechanismSpi()
```

---

#### Constructor Detail

ExemptionMechanismSpi

```java
public ExemptionMechanismSpi()
```

---

#### ExemptionMechanismSpi

public ExemptionMechanismSpi()

Method Detail

- engineGetOutputSize

```java
protected abstract int engineGetOutputSize​(int inputLen)
```

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

engineGenExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:** inputLen

- the input length (in bytes)
**Returns:** the required output buffer size (in bytes)

- engineInit

```java
protected abstract void engineInit​(
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

, the underlying
exemption mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

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

- engineInit

```java
protected abstract void engineInit​(
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

If this exemption mechanism requires any algorithm parameters and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

- engineInit

```java
protected abstract void engineInit​(
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
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

- engineGenExemptionBlob

```java
protected abstract byte[] engineGenExemptionBlob()
throws
ExemptionMechanismException
```

Generates the exemption mechanism key blob.

**Returns:** the new buffer with the result key blob.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

- engineGenExemptionBlob

```java
protected abstract int engineGenExemptionBlob​(byte[] output,
int outputOffset)
throws
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

engineGetOutputSize

to determine
how big the output buffer should be.

**Parameters:** output

- the buffer for the result
**Parameters:** outputOffset

- the offset in

output

where the result
is stored
**Returns:** the number of bytes stored in

output
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### Method Detail

engineGetOutputSize

```java
protected abstract int engineGetOutputSize​(int inputLen)
```

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

engineGenExemptionBlob

call may be smaller than the length returned by this method.

**Parameters:** inputLen

- the input length (in bytes)
**Returns:** the required output buffer size (in bytes)

---

#### engineGetOutputSize

protected abstract int engineGetOutputSize​(int inputLen)

Returns the length in bytes that an output buffer would need to be in
order to hold the result of the next

engineGenExemptionBlob

operation, given the input length

inputLen

(in bytes).

The actual output length of the next

engineGenExemptionBlob

call may be smaller than the length returned by this method.

The actual output length of the next

engineGenExemptionBlob

call may be smaller than the length returned by this method.

engineInit

```java
protected abstract void engineInit​(
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

, the underlying
exemption mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

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

#### engineInit

protected abstract void engineInit​(

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

, the underlying
exemption mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidKeyException

is raised.

If this exemption mechanism requires any algorithm parameters
that cannot be derived from the given

key

, the underlying
exemption mechanism implementation is supposed to generate the required
parameters itself (using provider-specific default values); in the case
that algorithm parameters must be specified by the caller, an

InvalidKeyException

is raised.

engineInit

```java
protected abstract void engineInit​(
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

If this exemption mechanism requires any algorithm parameters and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

#### engineInit

protected abstract void engineInit​(

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

If this exemption mechanism requires any algorithm parameters and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

If this exemption mechanism requires any algorithm parameters and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

engineInit

```java
protected abstract void engineInit​(
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
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

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

#### engineInit

protected abstract void engineInit​(

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
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

If this exemption mechanism requires any algorithm parameters
and

params

is null, the underlying exemption mechanism
implementation is supposed to generate the required parameters
itself (using provider-specific default values); in the case that
algorithm parameters must be specified by the caller, an

InvalidAlgorithmParameterException

is raised.

engineGenExemptionBlob

```java
protected abstract byte[] engineGenExemptionBlob()
throws
ExemptionMechanismException
```

Generates the exemption mechanism key blob.

**Returns:** the new buffer with the result key blob.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### engineGenExemptionBlob

protected abstract byte[] engineGenExemptionBlob()
throws

ExemptionMechanismException

Generates the exemption mechanism key blob.

engineGenExemptionBlob

```java
protected abstract int engineGenExemptionBlob​(byte[] output,
int outputOffset)
throws
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

engineGetOutputSize

to determine
how big the output buffer should be.

**Parameters:** output

- the buffer for the result
**Parameters:** outputOffset

- the offset in

output

where the result
is stored
**Returns:** the number of bytes stored in

output
**Throws:** ShortBufferException

- if the given output buffer is too small
to hold the result.
**Throws:** ExemptionMechanismException

- if problem(s) encountered in the
process of generating.

---

#### engineGenExemptionBlob

protected abstract int engineGenExemptionBlob​(byte[] output,
int outputOffset)
throws

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

engineGetOutputSize

to determine
how big the output buffer should be.

If the

output

buffer is too small to hold the result,
a

ShortBufferException

is thrown. In this case, repeat this
call with a larger output buffer. Use

engineGetOutputSize

to determine
how big the output buffer should be.

---

