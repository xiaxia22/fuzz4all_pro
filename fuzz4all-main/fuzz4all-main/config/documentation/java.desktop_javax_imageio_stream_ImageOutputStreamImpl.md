# Class ImageOutputStreamImpl

**Source:** `java.desktop\javax\imageio\stream\ImageOutputStreamImpl.html`

### Class Description

```java
public abstract class
ImageOutputStreamImpl

extends
ImageInputStreamImpl

implements
ImageOutputStream
```

An abstract class implementing the

ImageOutputStream

interface.
This class is designed to reduce the number of methods that must
be implemented by subclasses.

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

#### public ImageOutputStreamImpl()

Constructs an

ImageOutputStreamImpl

.

---

### Method Details

#### protected final void flushBits()
throws
IOException

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one. This method should be called by subclasses at the
beginning of the

write(int)

and

write(byte[], int, int)

methods.

**Throws:**
- IOException

- if an I/O error occurs.

---

### Additional Sections

#### Class ImageOutputStreamImpl

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl
- - javax.imageio.stream.ImageOutputStreamImpl

javax.imageio.stream.ImageInputStreamImpl

- javax.imageio.stream.ImageOutputStreamImpl

javax.imageio.stream.ImageOutputStreamImpl

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

**Direct Known Subclasses:** FileCacheImageOutputStream

,

FileImageOutputStream

,

MemoryCacheImageOutputStream

```java
public abstract class
ImageOutputStreamImpl

extends
ImageInputStreamImpl

implements
ImageOutputStream
```

An abstract class implementing the

ImageOutputStream

interface.
This class is designed to reduce the number of methods that must
be implemented by subclasses.

public abstract class

ImageOutputStreamImpl

extends

ImageInputStreamImpl

implements

ImageOutputStream

An abstract class implementing the

ImageOutputStream

interface.
This class is designed to reduce the number of methods that must
be implemented by subclasses.

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

ImageOutputStreamImpl

()

Constructs an

ImageOutputStreamImpl

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

flushBits

()

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one.

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

finalize

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

seek

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

ImageOutputStreamImpl

()

Constructs an

ImageOutputStreamImpl

.

---

#### Constructor Summary

Constructs an

ImageOutputStreamImpl

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

flushBits

()

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one.

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

finalize

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

seek

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

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one.

Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

finalize

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

seek

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

- ImageOutputStreamImpl

```java
public ImageOutputStreamImpl()
```

Constructs an

ImageOutputStreamImpl

.

============ METHOD DETAIL ==========

- Method Detail

- flushBits

```java
protected final void flushBits()
throws
IOException
```

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one. This method should be called by subclasses at the
beginning of the

write(int)

and

write(byte[], int, int)

methods.

**Throws:** IOException

- if an I/O error occurs.

Constructor Detail

- ImageOutputStreamImpl

```java
public ImageOutputStreamImpl()
```

Constructs an

ImageOutputStreamImpl

.

---

#### Constructor Detail

ImageOutputStreamImpl

```java
public ImageOutputStreamImpl()
```

Constructs an

ImageOutputStreamImpl

.

---

#### ImageOutputStreamImpl

public ImageOutputStreamImpl()

Constructs an

ImageOutputStreamImpl

.

Method Detail

- flushBits

```java
protected final void flushBits()
throws
IOException
```

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one. This method should be called by subclasses at the
beginning of the

write(int)

and

write(byte[], int, int)

methods.

**Throws:** IOException

- if an I/O error occurs.

---

#### Method Detail

flushBits

```java
protected final void flushBits()
throws
IOException
```

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one. This method should be called by subclasses at the
beginning of the

write(int)

and

write(byte[], int, int)

methods.

**Throws:** IOException

- if an I/O error occurs.

---

#### flushBits

protected final void flushBits()
throws

IOException

If the bit offset is non-zero, forces the remaining bits
in the current byte to 0 and advances the stream position
by one. This method should be called by subclasses at the
beginning of the

write(int)

and

write(byte[], int, int)

methods.

---

