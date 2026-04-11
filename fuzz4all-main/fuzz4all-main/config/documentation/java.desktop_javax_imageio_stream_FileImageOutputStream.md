# Class FileImageOutputStream

**Source:** `java.desktop\javax\imageio\stream\FileImageOutputStream.html`

### Class Description

```java
public class
FileImageOutputStream

extends
ImageOutputStreamImpl
```

An implementation of

ImageOutputStream

that writes its
output directly to a

File

or

RandomAccessFile

.

**All Implemented Interfaces:** Closeable

,

DataInput

,

DataOutput

,

AutoCloseable

,

ImageInputStream

,

ImageOutputStream

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileImageOutputStream​(
File
f)
throws
FileNotFoundException
,

IOException

Constructs a

FileImageOutputStream

that will write
to a given

File

.

**Parameters:**
- f

- a

File

to write to.

**Throws:**
- IllegalArgumentException

- if

f

is

null

.
- SecurityException

- if a security manager exists
and does not allow write access to the file.
- FileNotFoundException

- if

f

does not denote
a regular file or it cannot be opened for reading and writing for any
other reason.
- IOException

- if an I/O error occurs.

---

#### public FileImageOutputStream​(
RandomAccessFile
raf)

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

**Parameters:**
- raf

- a

RandomAccessFile

to write to.

**Throws:**
- IllegalArgumentException

- if

raf

is

null

.

---

### Method Details

#### public void seek​(long pos)
throws
IOException

Sets the current stream position and resets the bit offset to
0. It is legal to seeking past the end of the file; an

EOFException

will be thrown only if a read is
performed. The file length will not be increased until a write
is performed.

**Parameters:**
- pos

- a

long

containing the desired file
pointer position.

**Throws:**
- IndexOutOfBoundsException

- if

pos

is smaller
than the flushed position.
- IOException

- if any other I/O error occurs.

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

ImageInputStreamImpl

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

#### Class FileImageOutputStream

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl
- - javax.imageio.stream.ImageOutputStreamImpl
- - javax.imageio.stream.FileImageOutputStream

javax.imageio.stream.ImageInputStreamImpl

- javax.imageio.stream.ImageOutputStreamImpl
- - javax.imageio.stream.FileImageOutputStream

javax.imageio.stream.ImageOutputStreamImpl

- javax.imageio.stream.FileImageOutputStream

javax.imageio.stream.FileImageOutputStream

**All Implemented Interfaces:** Closeable

,

DataInput

,

DataOutput

,

AutoCloseable

,

ImageInputStream

,

ImageOutputStream

```java
public class
FileImageOutputStream

extends
ImageOutputStreamImpl
```

An implementation of

ImageOutputStream

that writes its
output directly to a

File

or

RandomAccessFile

.

public class

FileImageOutputStream

extends

ImageOutputStreamImpl

An implementation of

ImageOutputStream

that writes its
output directly to a

File

or

RandomAccessFile

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.imageio.stream.

ImageInputStreamImpl

bitOffset

,

byteOrder

,

flushedPos

,

streamPos

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileImageOutputStream

​(

File

f)

Constructs a

FileImageOutputStream

that will write
to a given

File

.

FileImageOutputStream

​(

RandomAccessFile

raf)

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

void

seek

​(long pos)

Sets the current stream position and resets the bit offset to
0.

- Methods declared in class javax.imageio.stream.

ImageOutputStreamImpl

flushBits

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

isCached

,

isCachedFile

,

isCachedMemory

,

length

,

mark

,

read

,

read

,

read

,

reset

,

skipBytes

,

skipBytes

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

getBitOffset

,

getByteOrder

,

getFlushedPosition

,

getStreamPosition

,

isCached

,

isCachedFile

,

isCachedMemory

,

length

,

mark

,

read

,

read

,

read

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

reset

,

setBitOffset

,

setByteOrder

,

skipBytes

,

skipBytes

- Methods declared in interface javax.imageio.stream.

ImageOutputStream

flushBefore

,

write

,

write

,

write

,

writeBit

,

writeBits

,

writeBoolean

,

writeByte

,

writeBytes

,

writeChar

,

writeChars

,

writeChars

,

writeDouble

,

writeDoubles

,

writeFloat

,

writeFloats

,

writeInt

,

writeInts

,

writeLong

,

writeLongs

,

writeShort

,

writeShorts

,

writeUTF

Field Summary

- Fields declared in class javax.imageio.stream.

ImageInputStreamImpl

bitOffset

,

byteOrder

,

flushedPos

,

streamPos

---

#### Field Summary

Fields declared in class javax.imageio.stream.

ImageInputStreamImpl

bitOffset

,

byteOrder

,

flushedPos

,

streamPos

---

#### Fields declared in class javax.imageio.stream. ImageInputStreamImpl

Constructor Summary

Constructors

Constructor

Description

FileImageOutputStream

​(

File

f)

Constructs a

FileImageOutputStream

that will write
to a given

File

.

FileImageOutputStream

​(

RandomAccessFile

raf)

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

---

#### Constructor Summary

Constructs a

FileImageOutputStream

that will write
to a given

File

.

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

void

seek

​(long pos)

Sets the current stream position and resets the bit offset to
0.

- Methods declared in class javax.imageio.stream.

ImageOutputStreamImpl

flushBits

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

isCached

,

isCachedFile

,

isCachedMemory

,

length

,

mark

,

read

,

read

,

read

,

reset

,

skipBytes

,

skipBytes

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

getBitOffset

,

getByteOrder

,

getFlushedPosition

,

getStreamPosition

,

isCached

,

isCachedFile

,

isCachedMemory

,

length

,

mark

,

read

,

read

,

read

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

reset

,

setBitOffset

,

setByteOrder

,

skipBytes

,

skipBytes

- Methods declared in interface javax.imageio.stream.

ImageOutputStream

flushBefore

,

write

,

write

,

write

,

writeBit

,

writeBits

,

writeBoolean

,

writeByte

,

writeBytes

,

writeChar

,

writeChars

,

writeChars

,

writeDouble

,

writeDoubles

,

writeFloat

,

writeFloats

,

writeInt

,

writeInts

,

writeLong

,

writeLongs

,

writeShort

,

writeShorts

,

writeUTF

---

#### Method Summary

Deprecated.

The

finalize

method has been deprecated.

Sets the current stream position and resets the bit offset to
0.

Methods declared in class javax.imageio.stream.

ImageOutputStreamImpl

flushBits

---

#### Methods declared in class javax.imageio.stream. ImageOutputStreamImpl

Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

isCached

,

isCachedFile

,

isCachedMemory

,

length

,

mark

,

read

,

read

,

read

,

reset

,

skipBytes

,

skipBytes

---

#### Methods declared in class javax.imageio.stream. ImageInputStreamImpl

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

getBitOffset

,

getByteOrder

,

getFlushedPosition

,

getStreamPosition

,

isCached

,

isCachedFile

,

isCachedMemory

,

length

,

mark

,

read

,

read

,

read

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

reset

,

setBitOffset

,

setByteOrder

,

skipBytes

,

skipBytes

---

#### Methods declared in interface javax.imageio.stream. ImageInputStream

Methods declared in interface javax.imageio.stream.

ImageOutputStream

flushBefore

,

write

,

write

,

write

,

writeBit

,

writeBits

,

writeBoolean

,

writeByte

,

writeBytes

,

writeChar

,

writeChars

,

writeChars

,

writeDouble

,

writeDoubles

,

writeFloat

,

writeFloats

,

writeInt

,

writeInts

,

writeLong

,

writeLongs

,

writeShort

,

writeShorts

,

writeUTF

---

#### Methods declared in interface javax.imageio.stream. ImageOutputStream

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FileImageOutputStream

```java
public FileImageOutputStream​(
File
f)
throws
FileNotFoundException
,

IOException
```

Constructs a

FileImageOutputStream

that will write
to a given

File

.

**Parameters:** f

- a

File

to write to.
**Throws:** IllegalArgumentException

- if

f

is

null

.
**Throws:** SecurityException

- if a security manager exists
and does not allow write access to the file.
**Throws:** FileNotFoundException

- if

f

does not denote
a regular file or it cannot be opened for reading and writing for any
other reason.
**Throws:** IOException

- if an I/O error occurs.

- FileImageOutputStream

```java
public FileImageOutputStream​(
RandomAccessFile
raf)
```

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

**Parameters:** raf

- a

RandomAccessFile

to write to.
**Throws:** IllegalArgumentException

- if

raf

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- seek

```java
public void seek​(long pos)
throws
IOException
```

Sets the current stream position and resets the bit offset to
0. It is legal to seeking past the end of the file; an

EOFException

will be thrown only if a read is
performed. The file length will not be increased until a write
is performed.

**Parameters:** pos

- a

long

containing the desired file
pointer position.
**Throws:** IndexOutOfBoundsException

- if

pos

is smaller
than the flushed position.
**Throws:** IOException

- if any other I/O error occurs.

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

ImageInputStreamImpl
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

Constructor Detail

- FileImageOutputStream

```java
public FileImageOutputStream​(
File
f)
throws
FileNotFoundException
,

IOException
```

Constructs a

FileImageOutputStream

that will write
to a given

File

.

**Parameters:** f

- a

File

to write to.
**Throws:** IllegalArgumentException

- if

f

is

null

.
**Throws:** SecurityException

- if a security manager exists
and does not allow write access to the file.
**Throws:** FileNotFoundException

- if

f

does not denote
a regular file or it cannot be opened for reading and writing for any
other reason.
**Throws:** IOException

- if an I/O error occurs.

- FileImageOutputStream

```java
public FileImageOutputStream​(
RandomAccessFile
raf)
```

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

**Parameters:** raf

- a

RandomAccessFile

to write to.
**Throws:** IllegalArgumentException

- if

raf

is

null

.

---

#### Constructor Detail

FileImageOutputStream

```java
public FileImageOutputStream​(
File
f)
throws
FileNotFoundException
,

IOException
```

Constructs a

FileImageOutputStream

that will write
to a given

File

.

**Parameters:** f

- a

File

to write to.
**Throws:** IllegalArgumentException

- if

f

is

null

.
**Throws:** SecurityException

- if a security manager exists
and does not allow write access to the file.
**Throws:** FileNotFoundException

- if

f

does not denote
a regular file or it cannot be opened for reading and writing for any
other reason.
**Throws:** IOException

- if an I/O error occurs.

---

#### FileImageOutputStream

public FileImageOutputStream​(

File

f)
throws

FileNotFoundException

,

IOException

Constructs a

FileImageOutputStream

that will write
to a given

File

.

FileImageOutputStream

```java
public FileImageOutputStream​(
RandomAccessFile
raf)
```

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

**Parameters:** raf

- a

RandomAccessFile

to write to.
**Throws:** IllegalArgumentException

- if

raf

is

null

.

---

#### FileImageOutputStream

public FileImageOutputStream​(

RandomAccessFile

raf)

Constructs a

FileImageOutputStream

that will write
to a given

RandomAccessFile

.

Method Detail

- seek

```java
public void seek​(long pos)
throws
IOException
```

Sets the current stream position and resets the bit offset to
0. It is legal to seeking past the end of the file; an

EOFException

will be thrown only if a read is
performed. The file length will not be increased until a write
is performed.

**Parameters:** pos

- a

long

containing the desired file
pointer position.
**Throws:** IndexOutOfBoundsException

- if

pos

is smaller
than the flushed position.
**Throws:** IOException

- if any other I/O error occurs.

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

ImageInputStreamImpl
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

---

#### Method Detail

seek

```java
public void seek​(long pos)
throws
IOException
```

Sets the current stream position and resets the bit offset to
0. It is legal to seeking past the end of the file; an

EOFException

will be thrown only if a read is
performed. The file length will not be increased until a write
is performed.

**Parameters:** pos

- a

long

containing the desired file
pointer position.
**Throws:** IndexOutOfBoundsException

- if

pos

is smaller
than the flushed position.
**Throws:** IOException

- if any other I/O error occurs.

---

#### seek

public void seek​(long pos)
throws

IOException

Sets the current stream position and resets the bit offset to
0. It is legal to seeking past the end of the file; an

EOFException

will be thrown only if a read is
performed. The file length will not be increased until a write
is performed.

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

ImageInputStreamImpl
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

