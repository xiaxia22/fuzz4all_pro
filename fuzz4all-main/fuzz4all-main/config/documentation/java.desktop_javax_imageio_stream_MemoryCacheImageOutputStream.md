# Class MemoryCacheImageOutputStream

**Source:** `java.desktop\javax\imageio\stream\MemoryCacheImageOutputStream.html`

### Class Description

```java
public class
MemoryCacheImageOutputStream

extends
ImageOutputStreamImpl
```

An implementation of

ImageOutputStream

that writes its
output to a regular

OutputStream

. A memory buffer is
used to cache at least the data between the discard position and
the current write position. The only constructor takes an

OutputStream

, so this class may not be used for
read/modify/write operations. Reading can occur only on parts of
the stream that have already been written to the cache and not
yet flushed.

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

#### public MemoryCacheImageOutputStream​(
OutputStream
stream)

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

**Parameters:**
- stream

- an

OutputStream

to write to.

**Throws:**
- IllegalArgumentException

- if

stream

is

null

.

---

### Method Details

#### public boolean isCached()

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

**Specified by:**
- isCached

in interface

ImageInputStream

**Overrides:**
- isCached

in class

ImageInputStreamImpl

**Returns:**
- true

.

**See Also:**
- isCachedMemory()

,

isCachedFile()

---

#### public boolean isCachedFile()

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

**Specified by:**
- isCachedFile

in interface

ImageInputStream

**Overrides:**
- isCachedFile

in class

ImageInputStreamImpl

**Returns:**
- false

.

**See Also:**
- isCached()

,

isCachedMemory()

---

#### public boolean isCachedMemory()

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

**Specified by:**
- isCachedMemory

in interface

ImageInputStream

**Overrides:**
- isCachedMemory

in class

ImageInputStreamImpl

**Returns:**
- true

.

**See Also:**
- isCached()

,

isCachedFile()

---

#### public void close()
throws
IOException

Closes this

MemoryCacheImageOutputStream

. All
pending data is flushed to the output, and the cache
is released. The destination

OutputStream

is not closed.

**Throws:**
- IOException

- if an I/O error occurs.

---

### Additional Sections

#### Class MemoryCacheImageOutputStream

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl
- - javax.imageio.stream.ImageOutputStreamImpl
- - javax.imageio.stream.MemoryCacheImageOutputStream

javax.imageio.stream.ImageInputStreamImpl

- javax.imageio.stream.ImageOutputStreamImpl
- - javax.imageio.stream.MemoryCacheImageOutputStream

javax.imageio.stream.ImageOutputStreamImpl

- javax.imageio.stream.MemoryCacheImageOutputStream

javax.imageio.stream.MemoryCacheImageOutputStream

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
MemoryCacheImageOutputStream

extends
ImageOutputStreamImpl
```

An implementation of

ImageOutputStream

that writes its
output to a regular

OutputStream

. A memory buffer is
used to cache at least the data between the discard position and
the current write position. The only constructor takes an

OutputStream

, so this class may not be used for
read/modify/write operations. Reading can occur only on parts of
the stream that have already been written to the cache and not
yet flushed.

public class

MemoryCacheImageOutputStream

extends

ImageOutputStreamImpl

An implementation of

ImageOutputStream

that writes its
output to a regular

OutputStream

. A memory buffer is
used to cache at least the data between the discard position and
the current write position. The only constructor takes an

OutputStream

, so this class may not be used for
read/modify/write operations. Reading can occur only on parts of
the stream that have already been written to the cache and not
yet flushed.

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

MemoryCacheImageOutputStream

​(

OutputStream

stream)

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this

MemoryCacheImageOutputStream

.

boolean

isCached

()

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

boolean

isCachedFile

()

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

boolean

isCachedMemory

()

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

- Methods declared in class javax.imageio.stream.

ImageOutputStreamImpl

flushBits

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

finalize

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

MemoryCacheImageOutputStream

​(

OutputStream

stream)

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

---

#### Constructor Summary

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this

MemoryCacheImageOutputStream

.

boolean

isCached

()

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

boolean

isCachedFile

()

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

boolean

isCachedMemory

()

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

- Methods declared in class javax.imageio.stream.

ImageOutputStreamImpl

flushBits

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

finalize

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

Closes this

MemoryCacheImageOutputStream

.

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

Methods declared in class javax.imageio.stream.

ImageOutputStreamImpl

flushBits

---

#### Methods declared in class javax.imageio.stream. ImageOutputStreamImpl

Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

,

finalize

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

- MemoryCacheImageOutputStream

```java
public MemoryCacheImageOutputStream​(
OutputStream
stream)
```

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

**Parameters:** stream

- an

OutputStream

to write to.
**Throws:** IllegalArgumentException

- if

stream

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- isCached

```java
public boolean isCached()
```

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

**Specified by:** isCached

in interface

ImageInputStream
**Overrides:** isCached

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCachedMemory()

,

isCachedFile()

- isCachedFile

```java
public boolean isCachedFile()
```

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Overrides:** isCachedFile

in class

ImageInputStreamImpl
**Returns:** false

.
**See Also:** isCached()

,

isCachedMemory()

- isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Overrides:** isCachedMemory

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCached()

,

isCachedFile()

- close

```java
public void close()
throws
IOException
```

Closes this

MemoryCacheImageOutputStream

. All
pending data is flushed to the output, and the cache
is released. The destination

OutputStream

is not closed.

**Throws:** IOException

- if an I/O error occurs.

Constructor Detail

- MemoryCacheImageOutputStream

```java
public MemoryCacheImageOutputStream​(
OutputStream
stream)
```

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

**Parameters:** stream

- an

OutputStream

to write to.
**Throws:** IllegalArgumentException

- if

stream

is

null

.

---

#### Constructor Detail

MemoryCacheImageOutputStream

```java
public MemoryCacheImageOutputStream​(
OutputStream
stream)
```

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

**Parameters:** stream

- an

OutputStream

to write to.
**Throws:** IllegalArgumentException

- if

stream

is

null

.

---

#### MemoryCacheImageOutputStream

public MemoryCacheImageOutputStream​(

OutputStream

stream)

Constructs a

MemoryCacheImageOutputStream

that will write
to a given

OutputStream

.

Method Detail

- isCached

```java
public boolean isCached()
```

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

**Specified by:** isCached

in interface

ImageInputStream
**Overrides:** isCached

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCachedMemory()

,

isCachedFile()

- isCachedFile

```java
public boolean isCachedFile()
```

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Overrides:** isCachedFile

in class

ImageInputStreamImpl
**Returns:** false

.
**See Also:** isCached()

,

isCachedMemory()

- isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Overrides:** isCachedMemory

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCached()

,

isCachedFile()

- close

```java
public void close()
throws
IOException
```

Closes this

MemoryCacheImageOutputStream

. All
pending data is flushed to the output, and the cache
is released. The destination

OutputStream

is not closed.

**Throws:** IOException

- if an I/O error occurs.

---

#### Method Detail

isCached

```java
public boolean isCached()
```

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

**Specified by:** isCached

in interface

ImageInputStream
**Overrides:** isCached

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCachedMemory()

,

isCachedFile()

---

#### isCached

public boolean isCached()

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

isCachedFile

```java
public boolean isCachedFile()
```

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Overrides:** isCachedFile

in class

ImageInputStreamImpl
**Returns:** false

.
**See Also:** isCached()

,

isCachedMemory()

---

#### isCachedFile

public boolean isCachedFile()

Returns

false

since this

ImageOutputStream

does not maintain a file cache.

isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Overrides:** isCachedMemory

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCached()

,

isCachedFile()

---

#### isCachedMemory

public boolean isCachedMemory()

Returns

true

since this

ImageOutputStream

maintains a main memory cache.

close

```java
public void close()
throws
IOException
```

Closes this

MemoryCacheImageOutputStream

. All
pending data is flushed to the output, and the cache
is released. The destination

OutputStream

is not closed.

**Throws:** IOException

- if an I/O error occurs.

---

#### close

public void close()
throws

IOException

Closes this

MemoryCacheImageOutputStream

. All
pending data is flushed to the output, and the cache
is released. The destination

OutputStream

is not closed.

---

