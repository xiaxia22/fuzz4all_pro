# Class MemoryCacheImageInputStream

**Source:** `java.desktop\javax\imageio\stream\MemoryCacheImageInputStream.html`

### Class Description

```java
public class
MemoryCacheImageInputStream

extends
ImageInputStreamImpl
```

An implementation of

ImageInputStream

that gets its
input from a regular

InputStream

. A memory buffer is
used to cache at least the data between the discard position and
the current read position.

In general, it is preferable to use a

FileCacheImageInputStream

when reading from a regular

InputStream

. This class is provided for cases where
it is not possible to create a writable temporary file.

**All Implemented Interfaces:** Closeable

,

DataInput

,

AutoCloseable

,

ImageInputStream

---

### Field Details

*No entries found.*

### Constructor Details

#### public MemoryCacheImageInputStream​(
InputStream
stream)

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

.

**Parameters:**
- stream

- an

InputStream

to read from.

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

ImageInputStream

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

ImageInputStream

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

ImageInputStream

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

MemoryCacheImageInputStream

, freeing
the cache. The source

InputStream

is not closed.

**Throws:**
- IOException

- if an I/O error occurs.

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

#### Class MemoryCacheImageInputStream

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl
- - javax.imageio.stream.MemoryCacheImageInputStream

javax.imageio.stream.ImageInputStreamImpl

- javax.imageio.stream.MemoryCacheImageInputStream

javax.imageio.stream.MemoryCacheImageInputStream

**All Implemented Interfaces:** Closeable

,

DataInput

,

AutoCloseable

,

ImageInputStream

```java
public class
MemoryCacheImageInputStream

extends
ImageInputStreamImpl
```

An implementation of

ImageInputStream

that gets its
input from a regular

InputStream

. A memory buffer is
used to cache at least the data between the discard position and
the current read position.

In general, it is preferable to use a

FileCacheImageInputStream

when reading from a regular

InputStream

. This class is provided for cases where
it is not possible to create a writable temporary file.

public class

MemoryCacheImageInputStream

extends

ImageInputStreamImpl

An implementation of

ImageInputStream

that gets its
input from a regular

InputStream

. A memory buffer is
used to cache at least the data between the discard position and
the current read position.

In general, it is preferable to use a

FileCacheImageInputStream

when reading from a regular

InputStream

. This class is provided for cases where
it is not possible to create a writable temporary file.

In general, it is preferable to use a

FileCacheImageInputStream

when reading from a regular

InputStream

. This class is provided for cases where
it is not possible to create a writable temporary file.

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

MemoryCacheImageInputStream

​(

InputStream

stream)

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

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

void

close

()

Closes this

MemoryCacheImageInputStream

, freeing
the cache.

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

Returns

true

since this

ImageInputStream

caches data in order to allow
seeking backwards.

boolean

isCachedFile

()

Returns

false

since this

ImageInputStream

does not maintain a file cache.

boolean

isCachedMemory

()

Returns

true

since this

ImageInputStream

maintains a main memory cache.

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

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

MemoryCacheImageInputStream

​(

InputStream

stream)

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

.

---

#### Constructor Summary

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

close

()

Closes this

MemoryCacheImageInputStream

, freeing
the cache.

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

Returns

true

since this

ImageInputStream

caches data in order to allow
seeking backwards.

boolean

isCachedFile

()

Returns

false

since this

ImageInputStream

does not maintain a file cache.

boolean

isCachedMemory

()

Returns

true

since this

ImageInputStream

maintains a main memory cache.

- Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

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

Closes this

MemoryCacheImageInputStream

, freeing
the cache.

Deprecated.

The

finalize

method has been deprecated.

Returns

true

since this

ImageInputStream

caches data in order to allow
seeking backwards.

Returns

false

since this

ImageInputStream

does not maintain a file cache.

Returns

true

since this

ImageInputStream

maintains a main memory cache.

Methods declared in class javax.imageio.stream.

ImageInputStreamImpl

checkClosed

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MemoryCacheImageInputStream

```java
public MemoryCacheImageInputStream​(
InputStream
stream)
```

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

.

**Parameters:** stream

- an

InputStream

to read from.
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

ImageInputStream

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

ImageInputStream

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

ImageInputStream

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

MemoryCacheImageInputStream

, freeing
the cache. The source

InputStream

is not closed.

**Throws:** IOException

- if an I/O error occurs.

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

- MemoryCacheImageInputStream

```java
public MemoryCacheImageInputStream​(
InputStream
stream)
```

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

.

**Parameters:** stream

- an

InputStream

to read from.
**Throws:** IllegalArgumentException

- if

stream

is

null

.

---

#### Constructor Detail

MemoryCacheImageInputStream

```java
public MemoryCacheImageInputStream​(
InputStream
stream)
```

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

.

**Parameters:** stream

- an

InputStream

to read from.
**Throws:** IllegalArgumentException

- if

stream

is

null

.

---

#### MemoryCacheImageInputStream

public MemoryCacheImageInputStream​(

InputStream

stream)

Constructs a

MemoryCacheImageInputStream

that will read
from a given

InputStream

.

Method Detail

- isCached

```java
public boolean isCached()
```

Returns

true

since this

ImageInputStream

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

ImageInputStream

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

ImageInputStream

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

MemoryCacheImageInputStream

, freeing
the cache. The source

InputStream

is not closed.

**Throws:** IOException

- if an I/O error occurs.

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

isCached

```java
public boolean isCached()
```

Returns

true

since this

ImageInputStream

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

ImageInputStream

caches data in order to allow
seeking backwards.

isCachedFile

```java
public boolean isCachedFile()
```

Returns

false

since this

ImageInputStream

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

ImageInputStream

does not maintain a file cache.

isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

true

since this

ImageInputStream

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

ImageInputStream

maintains a main memory cache.

close

```java
public void close()
throws
IOException
```

Closes this

MemoryCacheImageInputStream

, freeing
the cache. The source

InputStream

is not closed.

**Throws:** IOException

- if an I/O error occurs.

---

#### close

public void close()
throws

IOException

Closes this

MemoryCacheImageInputStream

, freeing
the cache. The source

InputStream

is not closed.

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

