# Class MacSpi

**Source:** `java.base\javax\crypto\MacSpi.html`

### Class Description

```java
public abstract class
MacSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Mac

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular MAC algorithm.

Implementations are free to implement the Cloneable interface.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public MacSpi()

*No description found.*

---

### Method Details

#### protected abstract int engineGetMacLength()

Returns the length of the MAC in bytes.

**Returns:**
- the MAC length in bytes.

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

Initializes the MAC with the given (secret) key and algorithm
parameters.

**Parameters:**
- key

- the (secret) key.
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

#### protected abstract void engineUpdate​(byte input)

Processes the given byte.

**Parameters:**
- input

- the input byte to be processed.

---

#### protected abstract void engineUpdate​(byte[] input,
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

**Parameters:**
- input

- the input buffer.
- offset

- the offset in

input

where the input starts.
- len

- the number of bytes to process.

---

#### protected void engineUpdate​(
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

Subclasses should consider overriding this method if they can
process ByteBuffers more efficiently than byte arrays.

**Parameters:**
- input

- the ByteBuffer

**Since:**
- 1.5

---

#### protected abstract byte[] engineDoFinal()

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

**Returns:**
- the MAC result.

---

#### protected abstract void engineReset()

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

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

#### Class MacSpi

java.lang.Object

- javax.crypto.MacSpi

javax.crypto.MacSpi

```java
public abstract class
MacSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Mac

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular MAC algorithm.

Implementations are free to implement the Cloneable interface.

**Since:** 1.4

public abstract class

MacSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

Mac

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular MAC algorithm.

Implementations are free to implement the Cloneable interface.

Implementations are free to implement the Cloneable interface.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MacSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the implementation is cloneable.

protected abstract byte[]

engineDoFinal

()

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

protected abstract int

engineGetMacLength

()

Returns the length of the MAC in bytes.

protected abstract void

engineInit

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes the MAC with the given (secret) key and algorithm
parameters.

protected abstract void

engineReset

()

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

protected abstract void

engineUpdate

​(byte input)

Processes the given byte.

protected abstract void

engineUpdate

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

protected void

engineUpdate

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

Constructor

Description

MacSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone if the implementation is cloneable.

protected abstract byte[]

engineDoFinal

()

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

protected abstract int

engineGetMacLength

()

Returns the length of the MAC in bytes.

protected abstract void

engineInit

​(

Key

key,

AlgorithmParameterSpec

params)

Initializes the MAC with the given (secret) key and algorithm
parameters.

protected abstract void

engineReset

()

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

protected abstract void

engineUpdate

​(byte input)

Processes the given byte.

protected abstract void

engineUpdate

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

protected void

engineUpdate

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

Returns a clone if the implementation is cloneable.

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

Returns the length of the MAC in bytes.

Initializes the MAC with the given (secret) key and algorithm
parameters.

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

Processes the given byte.

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

- MacSpi

```java
public MacSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineGetMacLength

```java
protected abstract int engineGetMacLength()
```

Returns the length of the MAC in bytes.

**Returns:** the MAC length in bytes.

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
```

Initializes the MAC with the given (secret) key and algorithm
parameters.

**Parameters:** key

- the (secret) key.
**Parameters:** params

- the algorithm parameters.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this MAC.

- engineUpdate

```java
protected abstract void engineUpdate​(byte input)
```

Processes the given byte.

**Parameters:** input

- the input byte to be processed.

- engineUpdate

```java
protected abstract void engineUpdate​(byte[] input,
int offset,
int len)
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

- engineUpdate

```java
protected void engineUpdate​(
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

Subclasses should consider overriding this method if they can
process ByteBuffers more efficiently than byte arrays.

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

- engineDoFinal

```java
protected abstract byte[] engineDoFinal()
```

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

**Returns:** the MAC result.

- engineReset

```java
protected abstract void engineReset()
```

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

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

Constructor Detail

- MacSpi

```java
public MacSpi()
```

---

#### Constructor Detail

MacSpi

```java
public MacSpi()
```

---

#### MacSpi

public MacSpi()

Method Detail

- engineGetMacLength

```java
protected abstract int engineGetMacLength()
```

Returns the length of the MAC in bytes.

**Returns:** the MAC length in bytes.

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
```

Initializes the MAC with the given (secret) key and algorithm
parameters.

**Parameters:** key

- the (secret) key.
**Parameters:** params

- the algorithm parameters.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this MAC.

- engineUpdate

```java
protected abstract void engineUpdate​(byte input)
```

Processes the given byte.

**Parameters:** input

- the input byte to be processed.

- engineUpdate

```java
protected abstract void engineUpdate​(byte[] input,
int offset,
int len)
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

- engineUpdate

```java
protected void engineUpdate​(
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

Subclasses should consider overriding this method if they can
process ByteBuffers more efficiently than byte arrays.

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

- engineDoFinal

```java
protected abstract byte[] engineDoFinal()
```

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

**Returns:** the MAC result.

- engineReset

```java
protected abstract void engineReset()
```

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

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

engineGetMacLength

```java
protected abstract int engineGetMacLength()
```

Returns the length of the MAC in bytes.

**Returns:** the MAC length in bytes.

---

#### engineGetMacLength

protected abstract int engineGetMacLength()

Returns the length of the MAC in bytes.

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
```

Initializes the MAC with the given (secret) key and algorithm
parameters.

**Parameters:** key

- the (secret) key.
**Parameters:** params

- the algorithm parameters.
**Throws:** InvalidKeyException

- if the given key is inappropriate for
initializing this MAC.
**Throws:** InvalidAlgorithmParameterException

- if the given algorithm
parameters are inappropriate for this MAC.

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

Initializes the MAC with the given (secret) key and algorithm
parameters.

engineUpdate

```java
protected abstract void engineUpdate​(byte input)
```

Processes the given byte.

**Parameters:** input

- the input byte to be processed.

---

#### engineUpdate

protected abstract void engineUpdate​(byte input)

Processes the given byte.

engineUpdate

```java
protected abstract void engineUpdate​(byte[] input,
int offset,
int len)
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

---

#### engineUpdate

protected abstract void engineUpdate​(byte[] input,
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

engineUpdate

```java
protected void engineUpdate​(
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

Subclasses should consider overriding this method if they can
process ByteBuffers more efficiently than byte arrays.

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

---

#### engineUpdate

protected void engineUpdate​(

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

Subclasses should consider overriding this method if they can
process ByteBuffers more efficiently than byte arrays.

Subclasses should consider overriding this method if they can
process ByteBuffers more efficiently than byte arrays.

engineDoFinal

```java
protected abstract byte[] engineDoFinal()
```

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

**Returns:** the MAC result.

---

#### engineDoFinal

protected abstract byte[] engineDoFinal()

Completes the MAC computation and resets the MAC for further use,
maintaining the secret key that the MAC was initialized with.

engineReset

```java
protected abstract void engineReset()
```

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

---

#### engineReset

protected abstract void engineReset()

Resets the MAC for further use, maintaining the secret key that the
MAC was initialized with.

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

