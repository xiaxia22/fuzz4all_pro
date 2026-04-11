# Class FileCacheImageInputStream

**Source:** `java.desktop\javax\imageio\stream\FileCacheImageInputStream.html`

### Class Description

```java
public class
FileCacheImageInputStream

extends
ImageInputStreamImpl
```

An implementation of

ImageInputStream

that gets its
input from a regular

InputStream

. A file is used to
cache previously read data.

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

#### public FileCacheImageInputStream​(
InputStream
stream,

File
cacheDir)
throws
IOException

Constructs a

FileCacheImageInputStream

that will read
from a given

InputStream

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

InputStream

to read from.
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

true

since this

ImageInputStream

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

ImageInputStream

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

FileCacheImageInputStream

, closing
and removing the cache file. The source

InputStream

is not closed.

**Throws:**
- IOException

- if an error occurs.

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

#### Class FileCacheImageInputStream

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl
- - javax.imageio.stream.FileCacheImageInputStream

javax.imageio.stream.ImageInputStreamImpl

- javax.imageio.stream.FileCacheImageInputStream

javax.imageio.stream.FileCacheImageInputStream

**All Implemented Interfaces:** Closeable

,

DataInput

,

AutoCloseable

,

ImageInputStream

```java
public class
FileCacheImageInputStream

extends
ImageInputStreamImpl
```

An implementation of

ImageInputStream

that gets its
input from a regular

InputStream

. A file is used to
cache previously read data.

public class

FileCacheImageInputStream

extends

ImageInputStreamImpl

An implementation of

ImageInputStream

that gets its
input from a regular

InputStream

. A file is used to
cache previously read data.

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

FileCacheImageInputStream

​(

InputStream

stream,

File

cacheDir)

Constructs a

FileCacheImageInputStream

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

FileCacheImageInputStream

, closing
and removing the cache file.

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

true

since this

ImageInputStream

maintains a file cache.

boolean

isCachedMemory

()

Returns

false

since this

ImageInputStream

does not maintain a main memory
cache.

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

FileCacheImageInputStream

​(

InputStream

stream,

File

cacheDir)

Constructs a

FileCacheImageInputStream

that will read
from a given

InputStream

.

---

#### Constructor Summary

Constructs a

FileCacheImageInputStream

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

FileCacheImageInputStream

, closing
and removing the cache file.

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

true

since this

ImageInputStream

maintains a file cache.

boolean

isCachedMemory

()

Returns

false

since this

ImageInputStream

does not maintain a main memory
cache.

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

FileCacheImageInputStream

, closing
and removing the cache file.

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

true

since this

ImageInputStream

maintains a file cache.

Returns

false

since this

ImageInputStream

does not maintain a main memory
cache.

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

- FileCacheImageInputStream

```java
public FileCacheImageInputStream​(
InputStream
stream,

File
cacheDir)
throws
IOException
```

Constructs a

FileCacheImageInputStream

that will read
from a given

InputStream

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

InputStream

to read from.
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

true

since this

ImageInputStream

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

ImageInputStream

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

FileCacheImageInputStream

, closing
and removing the cache file. The source

InputStream

is not closed.

**Throws:** IOException

- if an error occurs.

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

- FileCacheImageInputStream

```java
public FileCacheImageInputStream​(
InputStream
stream,

File
cacheDir)
throws
IOException
```

Constructs a

FileCacheImageInputStream

that will read
from a given

InputStream

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

InputStream

to read from.
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

FileCacheImageInputStream

```java
public FileCacheImageInputStream​(
InputStream
stream,

File
cacheDir)
throws
IOException
```

Constructs a

FileCacheImageInputStream

that will read
from a given

InputStream

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

InputStream

to read from.
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

#### FileCacheImageInputStream

public FileCacheImageInputStream​(

InputStream

stream,

File

cacheDir)
throws

IOException

Constructs a

FileCacheImageInputStream

that will read
from a given

InputStream

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

true

since this

ImageInputStream

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

ImageInputStream

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

FileCacheImageInputStream

, closing
and removing the cache file. The source

InputStream

is not closed.

**Throws:** IOException

- if an error occurs.

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

true

since this

ImageInputStream

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

ImageInputStream

maintains a file cache.

isCachedMemory

```java
public boolean isCachedMemory()
```

Returns

false

since this

ImageInputStream

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

ImageInputStream

does not maintain a main memory
cache.

close

```java
public void close()
throws
IOException
```

Closes this

FileCacheImageInputStream

, closing
and removing the cache file. The source

InputStream

is not closed.

**Throws:** IOException

- if an error occurs.

---

#### close

public void close()
throws

IOException

Closes this

FileCacheImageInputStream

, closing
and removing the cache file. The source

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

