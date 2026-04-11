# Class ImageInputStreamImpl

**Source:** `java.desktop\javax\imageio\stream\ImageInputStreamImpl.html`

### Class Description

```java
public abstract class
ImageInputStreamImpl

extends
Object

implements
ImageInputStream
```

An abstract class implementing the

ImageInputStream

interface.
This class is designed to reduce the number of methods that must
be implemented by subclasses.

In particular, this class handles most or all of the details of
byte order interpretation, buffering, mark/reset, discarding,
closing, and disposing.

**All Implemented Interfaces:** Closeable

,

DataInput

,

AutoCloseable

,

ImageInputStream

---

### Field Details

#### protected
ByteOrder
byteOrder

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order. By default, the value is

ByteOrder.BIG_ENDIAN

.

---

#### protected long streamPos

The current read position within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the read position.

---

#### protected int bitOffset

The current bit offset within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the bit offset.

---

#### protected long flushedPos

The position prior to which data may be discarded. Seeking
to a smaller position is not allowed.

flushedPos

will always be >= 0.

---

### Constructor Details

#### public ImageInputStreamImpl()

Constructs an

ImageInputStreamImpl

.

---

### Method Details

#### protected final void checkClosed()
throws
IOException

Throws an

IOException

if the stream has been closed.
Subclasses may call this method from any of their methods that
require the stream not to be closed.

**Throws:**
- IOException

- if the stream is closed.

---

#### public abstract int read()
throws
IOException

Reads a single byte from the stream and returns it as an

int

between 0 and 255. If EOF is reached,

-1

is returned.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

The bit offset within the stream must be reset to zero before
the read occurs.

**Specified by:**
- read

in interface

ImageInputStream

**Returns:**
- the value of the next byte in the stream, or

-1

if EOF is reached.

**Throws:**
- IOException

- if the stream has been closed.

---

#### public int read​(byte[] b)
throws
IOException

A convenience method that calls

read(b, 0, b.length)

.

The bit offset within the stream is reset to zero before
the read occurs.

**Specified by:**
- read

in interface

ImageInputStream

**Parameters:**
- b

- an array of bytes to be written to.

**Returns:**
- the number of bytes actually read, or

-1

to indicate EOF.

**Throws:**
- NullPointerException

- if

b

is

null

.
- IOException

- if an I/O error occurs.

---

#### public abstract int read​(byte[] b,
int off,
int len)
throws
IOException

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.
If no bytes can be read because the end of the stream has been
reached,

-1

is returned.

The bit offset within the stream must be reset to zero before
the read occurs.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

**Specified by:**
- read

in interface

ImageInputStream

**Parameters:**
- b

- an array of bytes to be written to.
- off

- the starting position within

b

to write to.
- len

- the maximum number of bytes to read.

**Returns:**
- the number of bytes actually read, or

-1

to indicate EOF.

**Throws:**
- IndexOutOfBoundsException

- if

off

is
negative,

len

is negative, or

off + len

is greater than

b.length

.
- NullPointerException

- if

b

is

null

.
- IOException

- if an I/O error occurs.

---

#### public long length()

Returns

-1L

to indicate that the stream has unknown
length. Subclasses must override this method to provide actual
length information.

**Specified by:**
- length

in interface

ImageInputStream

**Returns:**
- -1L to indicate unknown length.

---

#### public int skipBytes​(int n)
throws
IOException

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:**
- skipBytes

in interface

DataInput
- skipBytes

in interface

ImageInputStream

**Parameters:**
- n

- the number of bytes to seek forward.

**Returns:**
- an

int

representing the number of bytes
skipped.

**Throws:**
- IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

---

#### public long skipBytes​(long n)
throws
IOException

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:**
- skipBytes

in interface

ImageInputStream

**Parameters:**
- n

- the number of bytes to seek forward.

**Returns:**
- a

long

representing the number of bytes
skipped.

**Throws:**
- IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

---

#### public void mark()

Pushes the current stream position onto a stack of marked
positions.

**Specified by:**
- mark

in interface

ImageInputStream

---

#### public void reset()
throws
IOException

Resets the current stream byte and bit positions from the stack
of marked positions.

An

IOException

will be thrown if the previous
marked position lies in the discarded portion of the stream.

**Specified by:**
- reset

in interface

ImageInputStream

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public boolean isCached()

Default implementation returns false. Subclasses should
override this if they cache data.

**Specified by:**
- isCached

in interface

ImageInputStream

**Returns:**
- true

if this

ImageInputStream

caches data.

**See Also:**
- ImageInputStream.isCachedMemory()

,

ImageInputStream.isCachedFile()

---

#### public boolean isCachedMemory()

Default implementation returns false. Subclasses should
override this if they cache data in main memory.

**Specified by:**
- isCachedMemory

in interface

ImageInputStream

**Returns:**
- true

if this

ImageInputStream

caches data in main memory.

**See Also:**
- ImageInputStream.isCached()

,

ImageInputStream.isCachedFile()

---

#### public boolean isCachedFile()

Default implementation returns false. Subclasses should
override this if they cache data in a temporary file.

**Specified by:**
- isCachedFile

in interface

ImageInputStream

**Returns:**
- true

if this

ImageInputStream

caches data in a temporary file.

**See Also:**
- ImageInputStream.isCached()

,

ImageInputStream.isCachedMemory()

---

#### @Deprecated
(
since
="9")
protected void finalize()
throws
Throwable

Finalizes this object prior to garbage collection. The

close

method is called to close any open input
source. This method should not be called from application
code.

**Overrides:**
- finalize

in class

Object

**Throws:**
- Throwable

- if an error occurs during superclass
finalization.

**See Also:**
- WeakReference

,

PhantomReference

---

### Additional Sections

#### Class ImageInputStreamImpl

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl

javax.imageio.stream.ImageInputStreamImpl

**All Implemented Interfaces:** Closeable

,

DataInput

,

AutoCloseable

,

ImageInputStream

**Direct Known Subclasses:** FileCacheImageInputStream

,

FileImageInputStream

,

ImageOutputStreamImpl

,

MemoryCacheImageInputStream

```java
public abstract class
ImageInputStreamImpl

extends
Object

implements
ImageInputStream
```

An abstract class implementing the

ImageInputStream

interface.
This class is designed to reduce the number of methods that must
be implemented by subclasses.

In particular, this class handles most or all of the details of
byte order interpretation, buffering, mark/reset, discarding,
closing, and disposing.

public abstract class

ImageInputStreamImpl

extends

Object

implements

ImageInputStream

An abstract class implementing the

ImageInputStream

interface.
This class is designed to reduce the number of methods that must
be implemented by subclasses.

In particular, this class handles most or all of the details of
byte order interpretation, buffering, mark/reset, discarding,
closing, and disposing.

In particular, this class handles most or all of the details of
byte order interpretation, buffering, mark/reset, discarding,
closing, and disposing.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

bitOffset

The current bit offset within the stream.

protected

ByteOrder

byteOrder

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order.

protected long

flushedPos

The position prior to which data may be discarded.

protected long

streamPos

The current read position within the stream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ImageInputStreamImpl

()

Constructs an

ImageInputStreamImpl

.

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

protected void

checkClosed

()

Throws an

IOException

if the stream has been closed.

protected void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

boolean

isCached

()

Default implementation returns false.

boolean

isCachedFile

()

Default implementation returns false.

boolean

isCachedMemory

()

Default implementation returns false.

long

length

()

Returns

-1L

to indicate that the stream has unknown
length.

void

mark

()

Pushes the current stream position onto a stack of marked
positions.

abstract int

read

()

Reads a single byte from the stream and returns it as an

int

between 0 and 255.

int

read

​(byte[] b)

A convenience method that calls

read(b, 0, b.length)

.

abstract int

read

​(byte[] b,
int off,
int len)

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.

void

reset

()

Resets the current stream byte and bit positions from the stack
of marked positions.

int

skipBytes

​(int n)

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

long

skipBytes

​(long n)

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

- Methods declared in class java.lang.

Object

clone

,

equals

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

- Methods declared in interface javax.imageio.stream.

ImageInputStream

close

,

flush

,

flushBefore

,

getBitOffset

,

getByteOrder

,

getFlushedPosition

,

getStreamPosition

,

readBit

,

readBits

,

readBoolean

,

readByte

,

readBytes

,

readChar

,

readDouble

,

readFloat

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readInt

,

readLine

,

readLong

,

readShort

,

readUnsignedByte

,

readUnsignedInt

,

readUnsignedShort

,

readUTF

,

seek

,

setBitOffset

,

setByteOrder

Field Summary

Fields

Modifier and Type

Field

Description

protected int

bitOffset

The current bit offset within the stream.

protected

ByteOrder

byteOrder

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order.

protected long

flushedPos

The position prior to which data may be discarded.

protected long

streamPos

The current read position within the stream.

---

#### Field Summary

The current bit offset within the stream.

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order.

The position prior to which data may be discarded.

The current read position within the stream.

Constructor Summary

Constructors

Constructor

Description

ImageInputStreamImpl

()

Constructs an

ImageInputStreamImpl

.

---

#### Constructor Summary

Constructs an

ImageInputStreamImpl

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected void

checkClosed

()

Throws an

IOException

if the stream has been closed.

protected void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

boolean

isCached

()

Default implementation returns false.

boolean

isCachedFile

()

Default implementation returns false.

boolean

isCachedMemory

()

Default implementation returns false.

long

length

()

Returns

-1L

to indicate that the stream has unknown
length.

void

mark

()

Pushes the current stream position onto a stack of marked
positions.

abstract int

read

()

Reads a single byte from the stream and returns it as an

int

between 0 and 255.

int

read

​(byte[] b)

A convenience method that calls

read(b, 0, b.length)

.

abstract int

read

​(byte[] b,
int off,
int len)

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.

void

reset

()

Resets the current stream byte and bit positions from the stack
of marked positions.

int

skipBytes

​(int n)

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

long

skipBytes

​(long n)

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

- Methods declared in class java.lang.

Object

clone

,

equals

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

- Methods declared in interface javax.imageio.stream.

ImageInputStream

close

,

flush

,

flushBefore

,

getBitOffset

,

getByteOrder

,

getFlushedPosition

,

getStreamPosition

,

readBit

,

readBits

,

readBoolean

,

readByte

,

readBytes

,

readChar

,

readDouble

,

readFloat

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readInt

,

readLine

,

readLong

,

readShort

,

readUnsignedByte

,

readUnsignedInt

,

readUnsignedShort

,

readUTF

,

seek

,

setBitOffset

,

setByteOrder

---

#### Method Summary

Throws an

IOException

if the stream has been closed.

Deprecated.

The

finalize

method has been deprecated.

Default implementation returns false.

Returns

-1L

to indicate that the stream has unknown
length.

Pushes the current stream position onto a stack of marked
positions.

Reads a single byte from the stream and returns it as an

int

between 0 and 255.

A convenience method that calls

read(b, 0, b.length)

.

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.

Resets the current stream byte and bit positions from the stack
of marked positions.

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

Methods declared in class java.lang.

Object

clone

,

equals

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

Methods declared in interface javax.imageio.stream.

ImageInputStream

close

,

flush

,

flushBefore

,

getBitOffset

,

getByteOrder

,

getFlushedPosition

,

getStreamPosition

,

readBit

,

readBits

,

readBoolean

,

readByte

,

readBytes

,

readChar

,

readDouble

,

readFloat

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readFully

,

readInt

,

readLine

,

readLong

,

readShort

,

readUnsignedByte

,

readUnsignedInt

,

readUnsignedShort

,

readUTF

,

seek

,

setBitOffset

,

setByteOrder

---

#### Methods declared in interface javax.imageio.stream. ImageInputStream

============ FIELD DETAIL ===========

- Field Detail

- byteOrder

```java
protected
ByteOrder
byteOrder
```

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order. By default, the value is

ByteOrder.BIG_ENDIAN

.

- streamPos

```java
protected long streamPos
```

The current read position within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the read position.

- bitOffset

```java
protected int bitOffset
```

The current bit offset within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the bit offset.

- flushedPos

```java
protected long flushedPos
```

The position prior to which data may be discarded. Seeking
to a smaller position is not allowed.

flushedPos

will always be >= 0.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageInputStreamImpl

```java
public ImageInputStreamImpl()
```

Constructs an

ImageInputStreamImpl

.

============ METHOD DETAIL ==========

- Method Detail

- checkClosed

```java
protected final void checkClosed()
throws
IOException
```

Throws an

IOException

if the stream has been closed.
Subclasses may call this method from any of their methods that
require the stream not to be closed.

**Throws:** IOException

- if the stream is closed.

- read

```java
public abstract int read()
throws
IOException
```

Reads a single byte from the stream and returns it as an

int

between 0 and 255. If EOF is reached,

-1

is returned.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

The bit offset within the stream must be reset to zero before
the read occurs.

**Specified by:** read

in interface

ImageInputStream
**Returns:** the value of the next byte in the stream, or

-1

if EOF is reached.
**Throws:** IOException

- if the stream has been closed.

- read

```java
public int read​(byte[] b)
throws
IOException
```

A convenience method that calls

read(b, 0, b.length)

.

The bit offset within the stream is reset to zero before
the read occurs.

**Specified by:** read

in interface

ImageInputStream
**Parameters:** b

- an array of bytes to be written to.
**Returns:** the number of bytes actually read, or

-1

to indicate EOF.
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IOException

- if an I/O error occurs.

- read

```java
public abstract int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.
If no bytes can be read because the end of the stream has been
reached,

-1

is returned.

The bit offset within the stream must be reset to zero before
the read occurs.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

**Specified by:** read

in interface

ImageInputStream
**Parameters:** b

- an array of bytes to be written to.
**Parameters:** off

- the starting position within

b

to write to.
**Parameters:** len

- the maximum number of bytes to read.
**Returns:** the number of bytes actually read, or

-1

to indicate EOF.
**Throws:** IndexOutOfBoundsException

- if

off

is
negative,

len

is negative, or

off + len

is greater than

b.length

.
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IOException

- if an I/O error occurs.

- length

```java
public long length()
```

Returns

-1L

to indicate that the stream has unknown
length. Subclasses must override this method to provide actual
length information.

**Specified by:** length

in interface

ImageInputStream
**Returns:** -1L to indicate unknown length.

- skipBytes

```java
public int skipBytes​(int n)
throws
IOException
```

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:** skipBytes

in interface

DataInput
**Specified by:** skipBytes

in interface

ImageInputStream
**Parameters:** n

- the number of bytes to seek forward.
**Returns:** an

int

representing the number of bytes
skipped.
**Throws:** IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

- skipBytes

```java
public long skipBytes​(long n)
throws
IOException
```

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:** skipBytes

in interface

ImageInputStream
**Parameters:** n

- the number of bytes to seek forward.
**Returns:** a

long

representing the number of bytes
skipped.
**Throws:** IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

- mark

```java
public void mark()
```

Pushes the current stream position onto a stack of marked
positions.

**Specified by:** mark

in interface

ImageInputStream

- reset

```java
public void reset()
throws
IOException
```

Resets the current stream byte and bit positions from the stack
of marked positions.

An

IOException

will be thrown if the previous
marked position lies in the discarded portion of the stream.

**Specified by:** reset

in interface

ImageInputStream
**Throws:** IOException

- if an I/O error occurs.

- isCached

```java
public boolean isCached()
```

Default implementation returns false. Subclasses should
override this if they cache data.

**Specified by:** isCached

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data.
**See Also:** ImageInputStream.isCachedMemory()

,

ImageInputStream.isCachedFile()

- isCachedMemory

```java
public boolean isCachedMemory()
```

Default implementation returns false. Subclasses should
override this if they cache data in main memory.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data in main memory.
**See Also:** ImageInputStream.isCached()

,

ImageInputStream.isCachedFile()

- isCachedFile

```java
public boolean isCachedFile()
```

Default implementation returns false. Subclasses should
override this if they cache data in a temporary file.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data in a temporary file.
**See Also:** ImageInputStream.isCached()

,

ImageInputStream.isCachedMemory()

- finalize

```java
@Deprecated
(
since
="9")
protected void finalize()
throws
Throwable
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Finalizes this object prior to garbage collection. The

close

method is called to close any open input
source. This method should not be called from application
code.

**Overrides:** finalize

in class

Object
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

Field Detail

- byteOrder

```java
protected
ByteOrder
byteOrder
```

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order. By default, the value is

ByteOrder.BIG_ENDIAN

.

- streamPos

```java
protected long streamPos
```

The current read position within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the read position.

- bitOffset

```java
protected int bitOffset
```

The current bit offset within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the bit offset.

- flushedPos

```java
protected long flushedPos
```

The position prior to which data may be discarded. Seeking
to a smaller position is not allowed.

flushedPos

will always be >= 0.

---

#### Field Detail

byteOrder

```java
protected
ByteOrder
byteOrder
```

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order. By default, the value is

ByteOrder.BIG_ENDIAN

.

---

#### byteOrder

protected

ByteOrder

byteOrder

The byte order of the stream as an instance of the enumeration
class

java.nio.ByteOrder

, where

ByteOrder.BIG_ENDIAN

indicates network byte order
and

ByteOrder.LITTLE_ENDIAN

indicates the reverse
order. By default, the value is

ByteOrder.BIG_ENDIAN

.

streamPos

```java
protected long streamPos
```

The current read position within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the read position.

---

#### streamPos

protected long streamPos

The current read position within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the read position.

bitOffset

```java
protected int bitOffset
```

The current bit offset within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the bit offset.

---

#### bitOffset

protected int bitOffset

The current bit offset within the stream. Subclasses are
responsible for keeping this value current from any method they
override that alters the bit offset.

flushedPos

```java
protected long flushedPos
```

The position prior to which data may be discarded. Seeking
to a smaller position is not allowed.

flushedPos

will always be >= 0.

---

#### flushedPos

protected long flushedPos

The position prior to which data may be discarded. Seeking
to a smaller position is not allowed.

flushedPos

will always be >= 0.

Constructor Detail

- ImageInputStreamImpl

```java
public ImageInputStreamImpl()
```

Constructs an

ImageInputStreamImpl

.

---

#### Constructor Detail

ImageInputStreamImpl

```java
public ImageInputStreamImpl()
```

Constructs an

ImageInputStreamImpl

.

---

#### ImageInputStreamImpl

public ImageInputStreamImpl()

Constructs an

ImageInputStreamImpl

.

Method Detail

- checkClosed

```java
protected final void checkClosed()
throws
IOException
```

Throws an

IOException

if the stream has been closed.
Subclasses may call this method from any of their methods that
require the stream not to be closed.

**Throws:** IOException

- if the stream is closed.

- read

```java
public abstract int read()
throws
IOException
```

Reads a single byte from the stream and returns it as an

int

between 0 and 255. If EOF is reached,

-1

is returned.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

The bit offset within the stream must be reset to zero before
the read occurs.

**Specified by:** read

in interface

ImageInputStream
**Returns:** the value of the next byte in the stream, or

-1

if EOF is reached.
**Throws:** IOException

- if the stream has been closed.

- read

```java
public int read​(byte[] b)
throws
IOException
```

A convenience method that calls

read(b, 0, b.length)

.

The bit offset within the stream is reset to zero before
the read occurs.

**Specified by:** read

in interface

ImageInputStream
**Parameters:** b

- an array of bytes to be written to.
**Returns:** the number of bytes actually read, or

-1

to indicate EOF.
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IOException

- if an I/O error occurs.

- read

```java
public abstract int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.
If no bytes can be read because the end of the stream has been
reached,

-1

is returned.

The bit offset within the stream must be reset to zero before
the read occurs.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

**Specified by:** read

in interface

ImageInputStream
**Parameters:** b

- an array of bytes to be written to.
**Parameters:** off

- the starting position within

b

to write to.
**Parameters:** len

- the maximum number of bytes to read.
**Returns:** the number of bytes actually read, or

-1

to indicate EOF.
**Throws:** IndexOutOfBoundsException

- if

off

is
negative,

len

is negative, or

off + len

is greater than

b.length

.
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IOException

- if an I/O error occurs.

- length

```java
public long length()
```

Returns

-1L

to indicate that the stream has unknown
length. Subclasses must override this method to provide actual
length information.

**Specified by:** length

in interface

ImageInputStream
**Returns:** -1L to indicate unknown length.

- skipBytes

```java
public int skipBytes​(int n)
throws
IOException
```

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:** skipBytes

in interface

DataInput
**Specified by:** skipBytes

in interface

ImageInputStream
**Parameters:** n

- the number of bytes to seek forward.
**Returns:** an

int

representing the number of bytes
skipped.
**Throws:** IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

- skipBytes

```java
public long skipBytes​(long n)
throws
IOException
```

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:** skipBytes

in interface

ImageInputStream
**Parameters:** n

- the number of bytes to seek forward.
**Returns:** a

long

representing the number of bytes
skipped.
**Throws:** IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

- mark

```java
public void mark()
```

Pushes the current stream position onto a stack of marked
positions.

**Specified by:** mark

in interface

ImageInputStream

- reset

```java
public void reset()
throws
IOException
```

Resets the current stream byte and bit positions from the stack
of marked positions.

An

IOException

will be thrown if the previous
marked position lies in the discarded portion of the stream.

**Specified by:** reset

in interface

ImageInputStream
**Throws:** IOException

- if an I/O error occurs.

- isCached

```java
public boolean isCached()
```

Default implementation returns false. Subclasses should
override this if they cache data.

**Specified by:** isCached

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data.
**See Also:** ImageInputStream.isCachedMemory()

,

ImageInputStream.isCachedFile()

- isCachedMemory

```java
public boolean isCachedMemory()
```

Default implementation returns false. Subclasses should
override this if they cache data in main memory.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data in main memory.
**See Also:** ImageInputStream.isCached()

,

ImageInputStream.isCachedFile()

- isCachedFile

```java
public boolean isCachedFile()
```

Default implementation returns false. Subclasses should
override this if they cache data in a temporary file.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data in a temporary file.
**See Also:** ImageInputStream.isCached()

,

ImageInputStream.isCachedMemory()

- finalize

```java
@Deprecated
(
since
="9")
protected void finalize()
throws
Throwable
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Finalizes this object prior to garbage collection. The

close

method is called to close any open input
source. This method should not be called from application
code.

**Overrides:** finalize

in class

Object
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

---

#### Method Detail

checkClosed

```java
protected final void checkClosed()
throws
IOException
```

Throws an

IOException

if the stream has been closed.
Subclasses may call this method from any of their methods that
require the stream not to be closed.

**Throws:** IOException

- if the stream is closed.

---

#### checkClosed

protected final void checkClosed()
throws

IOException

Throws an

IOException

if the stream has been closed.
Subclasses may call this method from any of their methods that
require the stream not to be closed.

read

```java
public abstract int read()
throws
IOException
```

Reads a single byte from the stream and returns it as an

int

between 0 and 255. If EOF is reached,

-1

is returned.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

The bit offset within the stream must be reset to zero before
the read occurs.

**Specified by:** read

in interface

ImageInputStream
**Returns:** the value of the next byte in the stream, or

-1

if EOF is reached.
**Throws:** IOException

- if the stream has been closed.

---

#### read

public abstract int read()
throws

IOException

Reads a single byte from the stream and returns it as an

int

between 0 and 255. If EOF is reached,

-1

is returned.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

The bit offset within the stream must be reset to zero before
the read occurs.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

The bit offset within the stream must be reset to zero before
the read occurs.

The bit offset within the stream must be reset to zero before
the read occurs.

read

```java
public int read​(byte[] b)
throws
IOException
```

A convenience method that calls

read(b, 0, b.length)

.

The bit offset within the stream is reset to zero before
the read occurs.

**Specified by:** read

in interface

ImageInputStream
**Parameters:** b

- an array of bytes to be written to.
**Returns:** the number of bytes actually read, or

-1

to indicate EOF.
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IOException

- if an I/O error occurs.

---

#### read

public int read​(byte[] b)
throws

IOException

A convenience method that calls

read(b, 0, b.length)

.

The bit offset within the stream is reset to zero before
the read occurs.

The bit offset within the stream is reset to zero before
the read occurs.

read

```java
public abstract int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.
If no bytes can be read because the end of the stream has been
reached,

-1

is returned.

The bit offset within the stream must be reset to zero before
the read occurs.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

**Specified by:** read

in interface

ImageInputStream
**Parameters:** b

- an array of bytes to be written to.
**Parameters:** off

- the starting position within

b

to write to.
**Parameters:** len

- the maximum number of bytes to read.
**Returns:** the number of bytes actually read, or

-1

to indicate EOF.
**Throws:** IndexOutOfBoundsException

- if

off

is
negative,

len

is negative, or

off + len

is greater than

b.length

.
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IOException

- if an I/O error occurs.

---

#### read

public abstract int read​(byte[] b,
int off,
int len)
throws

IOException

Reads up to

len

bytes from the stream, and stores
them into

b

starting at index

off

.
If no bytes can be read because the end of the stream has been
reached,

-1

is returned.

The bit offset within the stream must be reset to zero before
the read occurs.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

The bit offset within the stream must be reset to zero before
the read occurs.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

Subclasses must provide an implementation for this method.
The subclass implementation should update the stream position
before exiting.

length

```java
public long length()
```

Returns

-1L

to indicate that the stream has unknown
length. Subclasses must override this method to provide actual
length information.

**Specified by:** length

in interface

ImageInputStream
**Returns:** -1L to indicate unknown length.

---

#### length

public long length()

Returns

-1L

to indicate that the stream has unknown
length. Subclasses must override this method to provide actual
length information.

skipBytes

```java
public int skipBytes​(int n)
throws
IOException
```

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:** skipBytes

in interface

DataInput
**Specified by:** skipBytes

in interface

ImageInputStream
**Parameters:** n

- the number of bytes to seek forward.
**Returns:** an

int

representing the number of bytes
skipped.
**Throws:** IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

---

#### skipBytes

public int skipBytes​(int n)
throws

IOException

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

The bit offset is reset to zero.

skipBytes

```java
public long skipBytes​(long n)
throws
IOException
```

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

**Specified by:** skipBytes

in interface

ImageInputStream
**Parameters:** n

- the number of bytes to seek forward.
**Returns:** a

long

representing the number of bytes
skipped.
**Throws:** IOException

- if

getStreamPosition

throws an

IOException

when computing either
the starting or ending position.

---

#### skipBytes

public long skipBytes​(long n)
throws

IOException

Advances the current stream position by calling

seek(getStreamPosition() + n)

.

The bit offset is reset to zero.

The bit offset is reset to zero.

mark

```java
public void mark()
```

Pushes the current stream position onto a stack of marked
positions.

**Specified by:** mark

in interface

ImageInputStream

---

#### mark

public void mark()

Pushes the current stream position onto a stack of marked
positions.

reset

```java
public void reset()
throws
IOException
```

Resets the current stream byte and bit positions from the stack
of marked positions.

An

IOException

will be thrown if the previous
marked position lies in the discarded portion of the stream.

**Specified by:** reset

in interface

ImageInputStream
**Throws:** IOException

- if an I/O error occurs.

---

#### reset

public void reset()
throws

IOException

Resets the current stream byte and bit positions from the stack
of marked positions.

An

IOException

will be thrown if the previous
marked position lies in the discarded portion of the stream.

An

IOException

will be thrown if the previous
marked position lies in the discarded portion of the stream.

isCached

```java
public boolean isCached()
```

Default implementation returns false. Subclasses should
override this if they cache data.

**Specified by:** isCached

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data.
**See Also:** ImageInputStream.isCachedMemory()

,

ImageInputStream.isCachedFile()

---

#### isCached

public boolean isCached()

Default implementation returns false. Subclasses should
override this if they cache data.

isCachedMemory

```java
public boolean isCachedMemory()
```

Default implementation returns false. Subclasses should
override this if they cache data in main memory.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data in main memory.
**See Also:** ImageInputStream.isCached()

,

ImageInputStream.isCachedFile()

---

#### isCachedMemory

public boolean isCachedMemory()

Default implementation returns false. Subclasses should
override this if they cache data in main memory.

isCachedFile

```java
public boolean isCachedFile()
```

Default implementation returns false. Subclasses should
override this if they cache data in a temporary file.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Returns:** true

if this

ImageInputStream

caches data in a temporary file.
**See Also:** ImageInputStream.isCached()

,

ImageInputStream.isCachedMemory()

---

#### isCachedFile

public boolean isCachedFile()

Default implementation returns false. Subclasses should
override this if they cache data in a temporary file.

finalize

```java
@Deprecated
(
since
="9")
protected void finalize()
throws
Throwable
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Finalizes this object prior to garbage collection. The

close

method is called to close any open input
source. This method should not be called from application
code.

**Overrides:** finalize

in class

Object
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

---

#### finalize

@Deprecated

(

since

="9")
protected void finalize()
throws

Throwable

Finalizes this object prior to garbage collection. The

close

method is called to close any open input
source. This method should not be called from application
code.

---

