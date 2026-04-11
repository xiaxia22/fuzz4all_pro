# Class FileImageInputStream

**Source:** `java.desktop\javax\imageio\stream\FileImageInputStream.html`

### Class Description

```java
public class
FileImageInputStream

extends
ImageInputStreamImpl
```

An implementation of

ImageInputStream

that gets its
input from a

File

or

RandomAccessFile

.
The file contents are assumed to be stable during the lifetime of
the object.

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

#### public FileImageInputStream​(
File
f)
throws
FileNotFoundException
,

IOException

Constructs a

FileImageInputStream

that will read
from a given

File

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:**
- f

- a

File

to read from.

**Throws:**
- IllegalArgumentException

- if

f

is

null

.
- SecurityException

- if a security manager exists
and does not allow read access to the file.
- FileNotFoundException

- if

f

is a
directory or cannot be opened for reading for any other reason.
- IOException

- if an I/O error occurs.

---

#### public FileImageInputStream​(
RandomAccessFile
raf)

Constructs a

FileImageInputStream

that will read
from a given

RandomAccessFile

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:**
- raf

- a

RandomAccessFile

to read from.

**Throws:**
- IllegalArgumentException

- if

raf

is

null

.

---

### Method Details

#### public long length()

Returns the length of the underlying file, or

-1

if it is unknown.

**Specified by:**
- length

in interface

ImageInputStream

**Overrides:**
- length

in class

ImageInputStreamImpl

**Returns:**
- the file length as a

long

, or

-1

.

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

#### Class FileImageInputStream

java.lang.Object

- javax.imageio.stream.ImageInputStreamImpl
- - javax.imageio.stream.FileImageInputStream

javax.imageio.stream.ImageInputStreamImpl

- javax.imageio.stream.FileImageInputStream

javax.imageio.stream.FileImageInputStream

**All Implemented Interfaces:** Closeable

,

DataInput

,

AutoCloseable

,

ImageInputStream

```java
public class
FileImageInputStream

extends
ImageInputStreamImpl
```

An implementation of

ImageInputStream

that gets its
input from a

File

or

RandomAccessFile

.
The file contents are assumed to be stable during the lifetime of
the object.

public class

FileImageInputStream

extends

ImageInputStreamImpl

An implementation of

ImageInputStream

that gets its
input from a

File

or

RandomAccessFile

.
The file contents are assumed to be stable during the lifetime of
the object.

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

FileImageInputStream

​(

File

f)

Constructs a

FileImageInputStream

that will read
from a given

File

.

FileImageInputStream

​(

RandomAccessFile

raf)

Constructs a

FileImageInputStream

that will read
from a given

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

long

length

()

Returns the length of the underlying file, or

-1

if it is unknown.

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

FileImageInputStream

​(

File

f)

Constructs a

FileImageInputStream

that will read
from a given

File

.

FileImageInputStream

​(

RandomAccessFile

raf)

Constructs a

FileImageInputStream

that will read
from a given

RandomAccessFile

.

---

#### Constructor Summary

Constructs a

FileImageInputStream

that will read
from a given

File

.

Constructs a

FileImageInputStream

that will read
from a given

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

long

length

()

Returns the length of the underlying file, or

-1

if it is unknown.

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

Deprecated.

The

finalize

method has been deprecated.

Returns the length of the underlying file, or

-1

if it is unknown.

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

- FileImageInputStream

```java
public FileImageInputStream​(
File
f)
throws
FileNotFoundException
,

IOException
```

Constructs a

FileImageInputStream

that will read
from a given

File

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:** f

- a

File

to read from.
**Throws:** IllegalArgumentException

- if

f

is

null

.
**Throws:** SecurityException

- if a security manager exists
and does not allow read access to the file.
**Throws:** FileNotFoundException

- if

f

is a
directory or cannot be opened for reading for any other reason.
**Throws:** IOException

- if an I/O error occurs.

- FileImageInputStream

```java
public FileImageInputStream​(
RandomAccessFile
raf)
```

Constructs a

FileImageInputStream

that will read
from a given

RandomAccessFile

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:** raf

- a

RandomAccessFile

to read from.
**Throws:** IllegalArgumentException

- if

raf

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- length

```java
public long length()
```

Returns the length of the underlying file, or

-1

if it is unknown.

**Specified by:** length

in interface

ImageInputStream
**Overrides:** length

in class

ImageInputStreamImpl
**Returns:** the file length as a

long

, or

-1

.

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

- FileImageInputStream

```java
public FileImageInputStream​(
File
f)
throws
FileNotFoundException
,

IOException
```

Constructs a

FileImageInputStream

that will read
from a given

File

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:** f

- a

File

to read from.
**Throws:** IllegalArgumentException

- if

f

is

null

.
**Throws:** SecurityException

- if a security manager exists
and does not allow read access to the file.
**Throws:** FileNotFoundException

- if

f

is a
directory or cannot be opened for reading for any other reason.
**Throws:** IOException

- if an I/O error occurs.

- FileImageInputStream

```java
public FileImageInputStream​(
RandomAccessFile
raf)
```

Constructs a

FileImageInputStream

that will read
from a given

RandomAccessFile

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:** raf

- a

RandomAccessFile

to read from.
**Throws:** IllegalArgumentException

- if

raf

is

null

.

---

#### Constructor Detail

FileImageInputStream

```java
public FileImageInputStream​(
File
f)
throws
FileNotFoundException
,

IOException
```

Constructs a

FileImageInputStream

that will read
from a given

File

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:** f

- a

File

to read from.
**Throws:** IllegalArgumentException

- if

f

is

null

.
**Throws:** SecurityException

- if a security manager exists
and does not allow read access to the file.
**Throws:** FileNotFoundException

- if

f

is a
directory or cannot be opened for reading for any other reason.
**Throws:** IOException

- if an I/O error occurs.

---

#### FileImageInputStream

public FileImageInputStream​(

File

f)
throws

FileNotFoundException

,

IOException

Constructs a

FileImageInputStream

that will read
from a given

File

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

FileImageInputStream

```java
public FileImageInputStream​(
RandomAccessFile
raf)
```

Constructs a

FileImageInputStream

that will read
from a given

RandomAccessFile

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

**Parameters:** raf

- a

RandomAccessFile

to read from.
**Throws:** IllegalArgumentException

- if

raf

is

null

.

---

#### FileImageInputStream

public FileImageInputStream​(

RandomAccessFile

raf)

Constructs a

FileImageInputStream

that will read
from a given

RandomAccessFile

.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

The file contents must not change between the time this
object is constructed and the time of the last call to a read
method.

Method Detail

- length

```java
public long length()
```

Returns the length of the underlying file, or

-1

if it is unknown.

**Specified by:** length

in interface

ImageInputStream
**Overrides:** length

in class

ImageInputStreamImpl
**Returns:** the file length as a

long

, or

-1

.

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

length

```java
public long length()
```

Returns the length of the underlying file, or

-1

if it is unknown.

**Specified by:** length

in interface

ImageInputStream
**Overrides:** length

in class

ImageInputStreamImpl
**Returns:** the file length as a

long

, or

-1

.

---

#### length

public long length()

Returns the length of the underlying file, or

-1

if it is unknown.

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

