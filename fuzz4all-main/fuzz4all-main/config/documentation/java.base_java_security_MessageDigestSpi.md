# Class MessageDigestSpi

**Source:** `java.base\java\security\MessageDigestSpi.html`

### Class Description

```java
public abstract class
MessageDigestSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

MessageDigest

class, which provides the functionality
of a message digest algorithm, such as MD5 or SHA. Message digests are
secure one-way hash functions that take arbitrary-sized data and output a
fixed-length hash value.

All the abstract methods in this class must be implemented by a
cryptographic service provider who wishes to supply the implementation
of a particular message digest algorithm.

Implementations are free to implement the Cloneable interface.

**Direct Known Subclasses:** MessageDigest

---

### Field Details

*No entries found.*

### Constructor Details

#### public MessageDigestSpi()

*No description found.*

---

### Method Details

#### protected int engineGetDigestLength()

Returns the digest length in bytes.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

The default behavior is to return 0.

This method may be overridden by a provider to return the digest
length.

**Returns:**
- the digest length in bytes.

**Since:**
- 1.2

---

#### protected abstract void engineUpdate​(byte input)

Updates the digest using the specified byte.

**Parameters:**
- input

- the byte to use for the update.

---

#### protected abstract void engineUpdate​(byte[] input,
int offset,
int len)

Updates the digest using the specified array of bytes,
starting at the specified offset.

**Parameters:**
- input

- the array of bytes to use for the update.
- offset

- the offset to start from in the array of bytes.
- len

- the number of bytes to use, starting at

offset

.

---

#### protected void engineUpdate​(
ByteBuffer
input)

Update the digest using the specified ByteBuffer. The digest is
updated using the

input.remaining()

bytes starting
at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:**
- input

- the ByteBuffer

**Since:**
- 1.5

---

#### protected abstract byte[] engineDigest()

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

**Returns:**
- the array of bytes for the resulting hash value.

---

#### protected int engineDigest​(byte[] buf,
int offset,
int len)
throws
DigestException

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

**Parameters:**
- buf

- the output buffer in which to store the digest
- offset

- offset to start from in the output buffer
- len

- number of bytes within buf allotted for the digest.
Both this default implementation and the SUN provider do not
return partial digests. The presence of this parameter is solely
for consistency in our API's. If the value of this parameter is less
than the actual digest length, the method will throw a DigestException.
This parameter is ignored if its value is greater than or equal to
the actual digest length.

**Returns:**
- the length of the digest stored in the output buffer.

**Throws:**
- DigestException

- if an error occurs.

**Since:**
- 1.2

---

#### protected abstract void engineReset()

Resets the digest for further use.

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

- if this is called on an
implementation that does not support

Cloneable

.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class MessageDigestSpi

java.lang.Object

- java.security.MessageDigestSpi

java.security.MessageDigestSpi

**Direct Known Subclasses:** MessageDigest

```java
public abstract class
MessageDigestSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

MessageDigest

class, which provides the functionality
of a message digest algorithm, such as MD5 or SHA. Message digests are
secure one-way hash functions that take arbitrary-sized data and output a
fixed-length hash value.

All the abstract methods in this class must be implemented by a
cryptographic service provider who wishes to supply the implementation
of a particular message digest algorithm.

Implementations are free to implement the Cloneable interface.

**Since:** 1.2
**See Also:** MessageDigest

public abstract class

MessageDigestSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

MessageDigest

class, which provides the functionality
of a message digest algorithm, such as MD5 or SHA. Message digests are
secure one-way hash functions that take arbitrary-sized data and output a
fixed-length hash value.

All the abstract methods in this class must be implemented by a
cryptographic service provider who wishes to supply the implementation
of a particular message digest algorithm.

Implementations are free to implement the Cloneable interface.

All the abstract methods in this class must be implemented by a
cryptographic service provider who wishes to supply the implementation
of a particular message digest algorithm.

Implementations are free to implement the Cloneable interface.

Implementations are free to implement the Cloneable interface.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MessageDigestSpi

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

engineDigest

()

Completes the hash computation by performing final
operations such as padding.

protected int

engineDigest

​(byte[] buf,
int offset,
int len)

Completes the hash computation by performing final
operations such as padding.

protected int

engineGetDigestLength

()

Returns the digest length in bytes.

protected abstract void

engineReset

()

Resets the digest for further use.

protected abstract void

engineUpdate

​(byte input)

Updates the digest using the specified byte.

protected abstract void

engineUpdate

​(byte[] input,
int offset,
int len)

Updates the digest using the specified array of bytes,
starting at the specified offset.

protected void

engineUpdate

​(

ByteBuffer

input)

Update the digest using the specified ByteBuffer.

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

MessageDigestSpi

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

engineDigest

()

Completes the hash computation by performing final
operations such as padding.

protected int

engineDigest

​(byte[] buf,
int offset,
int len)

Completes the hash computation by performing final
operations such as padding.

protected int

engineGetDigestLength

()

Returns the digest length in bytes.

protected abstract void

engineReset

()

Resets the digest for further use.

protected abstract void

engineUpdate

​(byte input)

Updates the digest using the specified byte.

protected abstract void

engineUpdate

​(byte[] input,
int offset,
int len)

Updates the digest using the specified array of bytes,
starting at the specified offset.

protected void

engineUpdate

​(

ByteBuffer

input)

Update the digest using the specified ByteBuffer.

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

Completes the hash computation by performing final
operations such as padding.

Returns the digest length in bytes.

Resets the digest for further use.

Updates the digest using the specified byte.

Updates the digest using the specified array of bytes,
starting at the specified offset.

Update the digest using the specified ByteBuffer.

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

- MessageDigestSpi

```java
public MessageDigestSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineGetDigestLength

```java
protected int engineGetDigestLength()
```

Returns the digest length in bytes.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

The default behavior is to return 0.

This method may be overridden by a provider to return the digest
length.

**Returns:** the digest length in bytes.
**Since:** 1.2

- engineUpdate

```java
protected abstract void engineUpdate​(byte input)
```

Updates the digest using the specified byte.

**Parameters:** input

- the byte to use for the update.

- engineUpdate

```java
protected abstract void engineUpdate​(byte[] input,
int offset,
int len)
```

Updates the digest using the specified array of bytes,
starting at the specified offset.

**Parameters:** input

- the array of bytes to use for the update.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** len

- the number of bytes to use, starting at

offset

.

- engineUpdate

```java
protected void engineUpdate​(
ByteBuffer
input)
```

Update the digest using the specified ByteBuffer. The digest is
updated using the

input.remaining()

bytes starting
at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

- engineDigest

```java
protected abstract byte[] engineDigest()
```

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

**Returns:** the array of bytes for the resulting hash value.

- engineDigest

```java
protected int engineDigest​(byte[] buf,
int offset,
int len)
throws
DigestException
```

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

**Parameters:** buf

- the output buffer in which to store the digest
**Parameters:** offset

- offset to start from in the output buffer
**Parameters:** len

- number of bytes within buf allotted for the digest.
Both this default implementation and the SUN provider do not
return partial digests. The presence of this parameter is solely
for consistency in our API's. If the value of this parameter is less
than the actual digest length, the method will throw a DigestException.
This parameter is ignored if its value is greater than or equal to
the actual digest length.
**Returns:** the length of the digest stored in the output buffer.
**Throws:** DigestException

- if an error occurs.
**Since:** 1.2

- engineReset

```java
protected abstract void engineReset()
```

Resets the digest for further use.

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

- if this is called on an
implementation that does not support

Cloneable

.
**See Also:** Cloneable

Constructor Detail

- MessageDigestSpi

```java
public MessageDigestSpi()
```

---

#### Constructor Detail

MessageDigestSpi

```java
public MessageDigestSpi()
```

---

#### MessageDigestSpi

public MessageDigestSpi()

Method Detail

- engineGetDigestLength

```java
protected int engineGetDigestLength()
```

Returns the digest length in bytes.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

The default behavior is to return 0.

This method may be overridden by a provider to return the digest
length.

**Returns:** the digest length in bytes.
**Since:** 1.2

- engineUpdate

```java
protected abstract void engineUpdate​(byte input)
```

Updates the digest using the specified byte.

**Parameters:** input

- the byte to use for the update.

- engineUpdate

```java
protected abstract void engineUpdate​(byte[] input,
int offset,
int len)
```

Updates the digest using the specified array of bytes,
starting at the specified offset.

**Parameters:** input

- the array of bytes to use for the update.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** len

- the number of bytes to use, starting at

offset

.

- engineUpdate

```java
protected void engineUpdate​(
ByteBuffer
input)
```

Update the digest using the specified ByteBuffer. The digest is
updated using the

input.remaining()

bytes starting
at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

**Parameters:** input

- the ByteBuffer
**Since:** 1.5

- engineDigest

```java
protected abstract byte[] engineDigest()
```

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

**Returns:** the array of bytes for the resulting hash value.

- engineDigest

```java
protected int engineDigest​(byte[] buf,
int offset,
int len)
throws
DigestException
```

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

**Parameters:** buf

- the output buffer in which to store the digest
**Parameters:** offset

- offset to start from in the output buffer
**Parameters:** len

- number of bytes within buf allotted for the digest.
Both this default implementation and the SUN provider do not
return partial digests. The presence of this parameter is solely
for consistency in our API's. If the value of this parameter is less
than the actual digest length, the method will throw a DigestException.
This parameter is ignored if its value is greater than or equal to
the actual digest length.
**Returns:** the length of the digest stored in the output buffer.
**Throws:** DigestException

- if an error occurs.
**Since:** 1.2

- engineReset

```java
protected abstract void engineReset()
```

Resets the digest for further use.

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

- if this is called on an
implementation that does not support

Cloneable

.
**See Also:** Cloneable

---

#### Method Detail

engineGetDigestLength

```java
protected int engineGetDigestLength()
```

Returns the digest length in bytes.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

The default behavior is to return 0.

This method may be overridden by a provider to return the digest
length.

**Returns:** the digest length in bytes.
**Since:** 1.2

---

#### engineGetDigestLength

protected int engineGetDigestLength()

Returns the digest length in bytes.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

The default behavior is to return 0.

This method may be overridden by a provider to return the digest
length.

This concrete method has been added to this previously-defined
abstract class. (For backwards compatibility, it cannot be abstract.)

The default behavior is to return 0.

This method may be overridden by a provider to return the digest
length.

The default behavior is to return 0.

This method may be overridden by a provider to return the digest
length.

This method may be overridden by a provider to return the digest
length.

engineUpdate

```java
protected abstract void engineUpdate​(byte input)
```

Updates the digest using the specified byte.

**Parameters:** input

- the byte to use for the update.

---

#### engineUpdate

protected abstract void engineUpdate​(byte input)

Updates the digest using the specified byte.

engineUpdate

```java
protected abstract void engineUpdate​(byte[] input,
int offset,
int len)
```

Updates the digest using the specified array of bytes,
starting at the specified offset.

**Parameters:** input

- the array of bytes to use for the update.
**Parameters:** offset

- the offset to start from in the array of bytes.
**Parameters:** len

- the number of bytes to use, starting at

offset

.

---

#### engineUpdate

protected abstract void engineUpdate​(byte[] input,
int offset,
int len)

Updates the digest using the specified array of bytes,
starting at the specified offset.

engineUpdate

```java
protected void engineUpdate​(
ByteBuffer
input)
```

Update the digest using the specified ByteBuffer. The digest is
updated using the

input.remaining()

bytes starting
at

input.position()

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

Update the digest using the specified ByteBuffer. The digest is
updated using the

input.remaining()

bytes starting
at

input.position()

.
Upon return, the buffer's position will be equal to its limit;
its limit will not have changed.

engineDigest

```java
protected abstract byte[] engineDigest()
```

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

**Returns:** the array of bytes for the resulting hash value.

---

#### engineDigest

protected abstract byte[] engineDigest()

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

engineDigest

```java
protected int engineDigest​(byte[] buf,
int offset,
int len)
throws
DigestException
```

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

**Parameters:** buf

- the output buffer in which to store the digest
**Parameters:** offset

- offset to start from in the output buffer
**Parameters:** len

- number of bytes within buf allotted for the digest.
Both this default implementation and the SUN provider do not
return partial digests. The presence of this parameter is solely
for consistency in our API's. If the value of this parameter is less
than the actual digest length, the method will throw a DigestException.
This parameter is ignored if its value is greater than or equal to
the actual digest length.
**Returns:** the length of the digest stored in the output buffer.
**Throws:** DigestException

- if an error occurs.
**Since:** 1.2

---

#### engineDigest

protected int engineDigest​(byte[] buf,
int offset,
int len)
throws

DigestException

Completes the hash computation by performing final
operations such as padding. Once

engineDigest

has
been called, the engine should be reset (see

engineReset

).
Resetting is the responsibility of the
engine implementor.

This method should be abstract, but we leave it concrete for
binary compatibility. Knowledgeable providers should override this
method.

engineReset

```java
protected abstract void engineReset()
```

Resets the digest for further use.

---

#### engineReset

protected abstract void engineReset()

Resets the digest for further use.

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

- if this is called on an
implementation that does not support

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

