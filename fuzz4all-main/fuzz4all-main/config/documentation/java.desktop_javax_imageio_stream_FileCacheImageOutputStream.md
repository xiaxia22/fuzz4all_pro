# Class FileCacheImageOutputStream

**Source:** `java.desktop\javax\imageio\stream\FileCacheImageOutputStream.html`

### Class Description

```java
public class
FileCacheImageOutputStream

extends
ImageOutputStreamImpl
```

An implementation of

ImageOutputStream

that writes its
output to a regular

OutputStream

. A file is used to
cache data until it is flushed to the output stream.

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

#### public FileCacheImageOutputStream​(
OutputStream
stream,

File
cacheDir)
throws
IOException

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

.

A temporary file is used as a cache. If

cacheDir

is non-

null

and is a
directory, the file will be created there. If it is

null

, the system-dependent default temporary-file
directory will be used (see the documentation for

File.createTempFile

for details).

**Parameters:**
- stream

- an

OutputStream

to write to.
- cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.

**Throws:**
- IllegalArgumentException

- if

stream

is

null

.
- IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.
- IOException

- if a cache file cannot be created.

---

### Method Details

#### public void seek​(long pos)
throws
IOException

Sets the current stream position and resets the bit offset to
0. It is legal to seek past the end of the file; an

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

true

since this

ImageOutputStream

maintains a file cache.

**Specified by:**
- isCachedFile

in interface

ImageInputStream

**Overrides:**
- isCachedFile

in class

ImageInputStreamImpl

**Returns:**
- true

.

**See Also:**
- isCached()

,

isCachedMemory()

---

#### public boolean isCachedMemory()

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

**Specified by:**
- isCachedMemory

in interface

ImageInputStream

**Overrides:**
- isCachedMemory

in class

ImageInputStreamImpl

**Returns:**
- false

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

FileCacheImageOutputStream

. All
pending data is flushed to the output, and the cache file
is closed and removed. The destination

OutputStream

is not closed.

**Throws:**
- IOException

- if an error occurs.

---

### Additional Sections

#### Class FileCacheImageOutputStream

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl
- - javax.imageio.stream.ImageOutputStreamImpl
- - javax.imageio.stream.FileCacheImageOutputStream

javax.imageio.stream.ImageInputStreamImpl

- javax.imageio.stream.ImageOutputStreamImpl
- - javax.imageio.stream.FileCacheImageOutputStream

javax.imageio.stream.ImageOutputStreamImpl

- javax.imageio.stream.FileCacheImageOutputStream

javax.imageio.stream.FileCacheImageOutputStream

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
FileCacheImageOutputStream

extends
ImageOutputStreamImpl
```

An implementation of

ImageOutputStream

that writes its
output to a regular

OutputStream

. A file is used to
cache data until it is flushed to the output stream.

public class

FileCacheImageOutputStream

extends

ImageOutputStreamImpl

An implementation of

ImageOutputStream

that writes its
output to a regular

OutputStream

. A file is used to
cache data until it is flushed to the output stream.

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

FileCacheImageOutputStream

​(

OutputStream

stream,

File

cacheDir)

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

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

FileCacheImageOutputStream

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

true

since this

ImageOutputStream

maintains a file cache.

boolean

isCachedMemory

()

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

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

FileCacheImageOutputStream

​(

OutputStream

stream,

File

cacheDir)

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

.

---

#### Constructor Summary

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

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

FileCacheImageOutputStream

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

true

since this

ImageOutputStream

maintains a file cache.

boolean

isCachedMemory

()

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

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

FileCacheImageOutputStream

.

Returns

true

since this

ImageOutputStream

caches data in order to allow
seeking backwards.

Returns

true

since this

ImageOutputStream

maintains a file cache.

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

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

- FileCacheImageOutputStream

```java
public FileCacheImageOutputStream​(
OutputStream
stream,

File
cacheDir)
throws
IOException
```

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

.

A temporary file is used as a cache. If

cacheDir

is non-

null

and is a
directory, the file will be created there. If it is

null

, the system-dependent default temporary-file
directory will be used (see the documentation for

File.createTempFile

for details).

**Parameters:** stream

- an

OutputStream

to write to.
**Parameters:** cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.
**Throws:** IllegalArgumentException

- if

stream

is

null

.
**Throws:** IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.
**Throws:** IOException

- if a cache file cannot be created.

============ METHOD DETAIL ==========

- Method Detail

- seek

```java
public void seek​(long pos)
throws
IOException
```

Sets the current stream position and resets the bit offset to
0. It is legal to seek past the end of the file; an

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

true

since this

ImageOutputStream

maintains a file cache.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Overrides:** isCachedFile

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCached()

,

isCachedMemory()

- isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Overrides:** isCachedMemory

in class

ImageInputStreamImpl
**Returns:** false

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

FileCacheImageOutputStream

. All
pending data is flushed to the output, and the cache file
is closed and removed. The destination

OutputStream

is not closed.

**Throws:** IOException

- if an error occurs.

Constructor Detail

- FileCacheImageOutputStream

```java
public FileCacheImageOutputStream​(
OutputStream
stream,

File
cacheDir)
throws
IOException
```

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

.

A temporary file is used as a cache. If

cacheDir

is non-

null

and is a
directory, the file will be created there. If it is

null

, the system-dependent default temporary-file
directory will be used (see the documentation for

File.createTempFile

for details).

**Parameters:** stream

- an

OutputStream

to write to.
**Parameters:** cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.
**Throws:** IllegalArgumentException

- if

stream

is

null

.
**Throws:** IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.
**Throws:** IOException

- if a cache file cannot be created.

---

#### Constructor Detail

FileCacheImageOutputStream

```java
public FileCacheImageOutputStream​(
OutputStream
stream,

File
cacheDir)
throws
IOException
```

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

.

A temporary file is used as a cache. If

cacheDir

is non-

null

and is a
directory, the file will be created there. If it is

null

, the system-dependent default temporary-file
directory will be used (see the documentation for

File.createTempFile

for details).

**Parameters:** stream

- an

OutputStream

to write to.
**Parameters:** cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.
**Throws:** IllegalArgumentException

- if

stream

is

null

.
**Throws:** IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.
**Throws:** IOException

- if a cache file cannot be created.

---

#### FileCacheImageOutputStream

public FileCacheImageOutputStream​(

OutputStream

stream,

File

cacheDir)
throws

IOException

Constructs a

FileCacheImageOutputStream

that will write
to a given

outputStream

.

A temporary file is used as a cache. If

cacheDir

is non-

null

and is a
directory, the file will be created there. If it is

null

, the system-dependent default temporary-file
directory will be used (see the documentation for

File.createTempFile

for details).

A temporary file is used as a cache. If

cacheDir

is non-

null

and is a
directory, the file will be created there. If it is

null

, the system-dependent default temporary-file
directory will be used (see the documentation for

File.createTempFile

for details).

Method Detail

- seek

```java
public void seek​(long pos)
throws
IOException
```

Sets the current stream position and resets the bit offset to
0. It is legal to seek past the end of the file; an

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

true

since this

ImageOutputStream

maintains a file cache.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Overrides:** isCachedFile

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCached()

,

isCachedMemory()

- isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Overrides:** isCachedMemory

in class

ImageInputStreamImpl
**Returns:** false

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

FileCacheImageOutputStream

. All
pending data is flushed to the output, and the cache file
is closed and removed. The destination

OutputStream

is not closed.

**Throws:** IOException

- if an error occurs.

---

#### Method Detail

seek

```java
public void seek​(long pos)
throws
IOException
```

Sets the current stream position and resets the bit offset to
0. It is legal to seek past the end of the file; an

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
0. It is legal to seek past the end of the file; an

EOFException

will be thrown only if a read is
performed. The file length will not be increased until a write
is performed.

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

true

since this

ImageOutputStream

maintains a file cache.

**Specified by:** isCachedFile

in interface

ImageInputStream
**Overrides:** isCachedFile

in class

ImageInputStreamImpl
**Returns:** true

.
**See Also:** isCached()

,

isCachedMemory()

---

#### isCachedFile

public boolean isCachedFile()

Returns

true

since this

ImageOutputStream

maintains a file cache.

isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

**Specified by:** isCachedMemory

in interface

ImageInputStream
**Overrides:** isCachedMemory

in class

ImageInputStreamImpl
**Returns:** false

.
**See Also:** isCached()

,

isCachedFile()

---

#### isCachedMemory

public boolean isCachedMemory()

Returns

false

since this

ImageOutputStream

does not maintain a main memory
cache.

close

```java
public void close()
throws
IOException
```

Closes this

FileCacheImageOutputStream

. All
pending data is flushed to the output, and the cache file
is closed and removed. The destination

OutputStream

is not closed.

**Throws:** IOException

- if an error occurs.

---

#### close

public void close()
throws

IOException

Closes this

FileCacheImageOutputStream

. All
pending data is flushed to the output, and the cache file
is closed and removed. The destination

OutputStream

is not closed.

---

