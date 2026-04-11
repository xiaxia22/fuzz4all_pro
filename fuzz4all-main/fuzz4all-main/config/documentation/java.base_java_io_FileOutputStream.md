# Class FileOutputStream

**Source:** `java.base\java\io\FileOutputStream.html`

### Class Description

```java
public class
FileOutputStream

extends
OutputStream
```

A file output stream is an output stream for writing data to a

File

or to a

FileDescriptor

. Whether or not
a file is available or may be created depends upon the underlying
platform. Some platforms, in particular, allow a file to be opened
for writing by only one

FileOutputStream

(or other
file-writing object) at a time. In such situations the constructors in
this class will fail if the file involved is already open.

FileOutputStream

is meant for writing streams of raw bytes
such as image data. For writing streams of characters, consider using

FileWriter

.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileOutputStream​(
String
name)
throws
FileNotFoundException

Creates a file output stream to write to the file with the
specified name. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:**
- name

- the system-dependent filename

**Throws:**
- FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
- SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.

**See Also:**
- SecurityManager.checkWrite(java.lang.String)

**Implementation Requirements:**
- Invoking this constructor with the parameter

name

is
equivalent to invoking

new FileOutputStream(name, false)

.

---

#### public FileOutputStream​(
String
name,
boolean append)
throws
FileNotFoundException

Creates a file output stream to write to the file with the specified
name. If the second argument is

true

, then
bytes will be written to the end of the file rather than the beginning.
A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:**
- name

- the system-dependent file name
- append

- if

true

, then bytes will be written
to the end of the file rather than the beginning

**Throws:**
- FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason.
- SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.

**See Also:**
- SecurityManager.checkWrite(java.lang.String)

**Since:**
- 1.1

---

#### public FileOutputStream​(
File
file)
throws
FileNotFoundException

Creates a file output stream to write to the file represented by
the specified

File

object. A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:**
- file

- the file to be opened for writing.

**Throws:**
- FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
- SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.

**See Also:**
- File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

---

#### public FileOutputStream​(
File
file,
boolean append)
throws
FileNotFoundException

Creates a file output stream to write to the file represented by
the specified

File

object. If the second argument is

true

, then bytes will be written to the end of the file
rather than the beginning. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:**
- file

- the file to be opened for writing.
- append

- if

true

, then bytes will be written
to the end of the file rather than the beginning

**Throws:**
- FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
- SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.

**See Also:**
- File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

**Since:**
- 1.4

---

#### public FileOutputStream​(
FileDescriptor
fdObj)

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

First, if there is a security manager, its

checkWrite

method is called with the file descriptor

fdObj

argument as its argument.

If

fdObj

is null then a

NullPointerException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

**Parameters:**
- fdObj

- the file descriptor to be opened for writing

**Throws:**
- SecurityException

- if a security manager exists and its

checkWrite

method denies
write access to the file descriptor

**See Also:**
- SecurityManager.checkWrite(java.io.FileDescriptor)

---

### Method Details

#### public void write​(int b)
throws
IOException

Writes the specified byte to this file output stream. Implements
the

write

method of

OutputStream

.

**Specified by:**
- write

in class

OutputStream

**Parameters:**
- b

- the byte to be written.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public void write​(byte[] b)
throws
IOException

Writes

b.length

bytes from the specified byte array
to this file output stream.

**Overrides:**
- write

in class

OutputStream

**Parameters:**
- b

- the data.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- OutputStream.write(byte[], int, int)

---

#### public void write​(byte[] b,
int off,
int len)
throws
IOException

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

**Overrides:**
- write

in class

OutputStream

**Parameters:**
- b

- the data.
- off

- the start offset in the data.
- len

- the number of bytes to write.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public void close()
throws
IOException

Closes this file output stream and releases any system resources
associated with this stream. This file output stream may no longer
be used for writing bytes.

If this stream has an associated channel then the channel is closed
as well.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Overrides:**
- close

in class

OutputStream

**Throws:**
- IOException

- if an I/O error occurs.

**API Note:**
- Overriding

close()

to perform cleanup actions is reliable
only when called directly or when called by try-with-resources.
Do not depend on finalization to invoke

close

;
finalization is not reliable and is deprecated.
If cleanup of native resources is needed, other mechanisms such as

Cleaner

should be used.

---

#### public final
FileDescriptor
getFD()
throws
IOException

Returns the file descriptor associated with this stream.

**Returns:**
- the

FileDescriptor

object that represents
the connection to the file in the file system being used
by this

FileOutputStream

object.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FileDescriptor

---

#### public
FileChannel
getChannel()

Returns the unique

FileChannel

object associated with this file output stream.

The initial

position

of the returned channel will be equal to the
number of bytes written to the file so far unless this stream is in
append mode, in which case it will be equal to the size of the file.
Writing bytes to this stream will increment the channel's position
accordingly. Changing the channel's position, either explicitly or by
writing, will change this stream's file position.

**Returns:**
- the file channel associated with this file output stream

**Since:**
- 1.4

---

#### @Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException

Cleans up the connection to the file, and ensures that the

close()

method of this file output stream is
called when there are no more references to this stream.
The

finalize()

method does not call

close()

directly.

**Overrides:**
- finalize

in class

Object

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FileInputStream.close()

**API Note:**
- To release resources used by this stream

close()

should be called
directly or by try-with-resources.

**Implementation Requirements:**
- If this FileOutputStream has been subclassed and the

close()

method has been overridden, the

close()

method will be
called when the FileOutputStream is unreachable.
Otherwise, it is implementation specific how the resource cleanup described in

close()

is performed.

---

### Additional Sections

#### Class FileOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FileOutputStream

java.io.OutputStream

- java.io.FileOutputStream

java.io.FileOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
FileOutputStream

extends
OutputStream
```

A file output stream is an output stream for writing data to a

File

or to a

FileDescriptor

. Whether or not
a file is available or may be created depends upon the underlying
platform. Some platforms, in particular, allow a file to be opened
for writing by only one

FileOutputStream

(or other
file-writing object) at a time. In such situations the constructors in
this class will fail if the file involved is already open.

FileOutputStream

is meant for writing streams of raw bytes
such as image data. For writing streams of characters, consider using

FileWriter

.

**API Note:** To release resources used by this stream

close()

should be called
directly or by try-with-resources. Subclasses are responsible for the cleanup
of resources acquired by the subclass.
Subclasses that override

finalize()

in order to perform cleanup
should be modified to use alternative cleanup mechanisms such as

Cleaner

and remove the overriding

finalize

method.
**Implementation Requirements:** If this FileOutputStream has been subclassed and the

close()

method has been overridden, the

close()

method will be
called when the FileInputStream is unreachable.
Otherwise, it is implementation specific how the resource cleanup described in

close()

is performed.
**Since:** 1.0
**See Also:** File

,

FileDescriptor

,

FileInputStream

,

Files.newOutputStream(java.nio.file.Path, java.nio.file.OpenOption...)

public class

FileOutputStream

extends

OutputStream

A file output stream is an output stream for writing data to a

File

or to a

FileDescriptor

. Whether or not
a file is available or may be created depends upon the underlying
platform. Some platforms, in particular, allow a file to be opened
for writing by only one

FileOutputStream

(or other
file-writing object) at a time. In such situations the constructors in
this class will fail if the file involved is already open.

FileOutputStream

is meant for writing streams of raw bytes
such as image data. For writing streams of characters, consider using

FileWriter

.

FileOutputStream

is meant for writing streams of raw bytes
such as image data. For writing streams of characters, consider using

FileWriter

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileOutputStream

​(

File

file)

Creates a file output stream to write to the file represented by
the specified

File

object.

FileOutputStream

​(

FileDescriptor

fdObj)

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

FileOutputStream

​(

File

file,
boolean append)

Creates a file output stream to write to the file represented by
the specified

File

object.

FileOutputStream

​(

String

name)

Creates a file output stream to write to the file with the
specified name.

FileOutputStream

​(

String

name,
boolean append)

Creates a file output stream to write to the file with the specified
name.

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

Closes this file output stream and releases any system resources
associated with this stream.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be removed.

FileChannel

getChannel

()

Returns the unique

FileChannel

object associated with this file output stream.

FileDescriptor

getFD

()

Returns the file descriptor associated with this stream.

void

write

​(byte[] b)

Writes

b.length

bytes from the specified byte array
to this file output stream.

void

write

​(byte[] b,
int off,
int len)

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

void

write

​(int b)

Writes the specified byte to this file output stream.

- Methods declared in class java.io.

OutputStream

flush

,

nullOutputStream

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

Constructor Summary

Constructors

Constructor

Description

FileOutputStream

​(

File

file)

Creates a file output stream to write to the file represented by
the specified

File

object.

FileOutputStream

​(

FileDescriptor

fdObj)

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

FileOutputStream

​(

File

file,
boolean append)

Creates a file output stream to write to the file represented by
the specified

File

object.

FileOutputStream

​(

String

name)

Creates a file output stream to write to the file with the
specified name.

FileOutputStream

​(

String

name,
boolean append)

Creates a file output stream to write to the file with the specified
name.

---

#### Constructor Summary

Creates a file output stream to write to the file represented by
the specified

File

object.

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

Creates a file output stream to write to the file with the
specified name.

Creates a file output stream to write to the file with the specified
name.

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

Closes this file output stream and releases any system resources
associated with this stream.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be removed.

FileChannel

getChannel

()

Returns the unique

FileChannel

object associated with this file output stream.

FileDescriptor

getFD

()

Returns the file descriptor associated with this stream.

void

write

​(byte[] b)

Writes

b.length

bytes from the specified byte array
to this file output stream.

void

write

​(byte[] b,
int off,
int len)

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

void

write

​(int b)

Writes the specified byte to this file output stream.

- Methods declared in class java.io.

OutputStream

flush

,

nullOutputStream

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

---

#### Method Summary

Closes this file output stream and releases any system resources
associated with this stream.

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be removed.

Returns the unique

FileChannel

object associated with this file output stream.

Returns the file descriptor associated with this stream.

Writes

b.length

bytes from the specified byte array
to this file output stream.

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

Writes the specified byte to this file output stream.

Methods declared in class java.io.

OutputStream

flush

,

nullOutputStream

---

#### Methods declared in class java.io. OutputStream

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FileOutputStream

```java
public FileOutputStream​(
String
name)
throws
FileNotFoundException
```

Creates a file output stream to write to the file with the
specified name. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Implementation Requirements:** Invoking this constructor with the parameter

name

is
equivalent to invoking

new FileOutputStream(name, false)

.
**Parameters:** name

- the system-dependent filename
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**See Also:** SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
String
name,
boolean append)
throws
FileNotFoundException
```

Creates a file output stream to write to the file with the specified
name. If the second argument is

true

, then
bytes will be written to the end of the file rather than the beginning.
A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** name

- the system-dependent file name
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason.
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**Since:** 1.1
**See Also:** SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
File
file)
throws
FileNotFoundException
```

Creates a file output stream to write to the file represented by
the specified

File

object. A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** file

- the file to be opened for writing.
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**See Also:** File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
File
file,
boolean append)
throws
FileNotFoundException
```

Creates a file output stream to write to the file represented by
the specified

File

object. If the second argument is

true

, then bytes will be written to the end of the file
rather than the beginning. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** file

- the file to be opened for writing.
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**Since:** 1.4
**See Also:** File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
FileDescriptor
fdObj)
```

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

First, if there is a security manager, its

checkWrite

method is called with the file descriptor

fdObj

argument as its argument.

If

fdObj

is null then a

NullPointerException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

**Parameters:** fdObj

- the file descriptor to be opened for writing
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies
write access to the file descriptor
**See Also:** SecurityManager.checkWrite(java.io.FileDescriptor)

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this file output stream. Implements
the

write

method of

OutputStream

.

**Specified by:** write

in class

OutputStream
**Parameters:** b

- the byte to be written.
**Throws:** IOException

- if an I/O error occurs.

- write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this file output stream.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** OutputStream.write(byte[], int, int)

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this file output stream and releases any system resources
associated with this stream. This file output stream may no longer
be used for writing bytes.

If this stream has an associated channel then the channel is closed
as well.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

OutputStream
**API Note:** Overriding

close()

to perform cleanup actions is reliable
only when called directly or when called by try-with-resources.
Do not depend on finalization to invoke

close

;
finalization is not reliable and is deprecated.
If cleanup of native resources is needed, other mechanisms such as

Cleaner

should be used.
**Throws:** IOException

- if an I/O error occurs.

- getFD

```java
public final
FileDescriptor
getFD()
throws
IOException
```

Returns the file descriptor associated with this stream.

**Returns:** the

FileDescriptor

object that represents
the connection to the file in the file system being used
by this

FileOutputStream

object.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FileDescriptor

- getChannel

```java
public
FileChannel
getChannel()
```

Returns the unique

FileChannel

object associated with this file output stream.

The initial

position

of the returned channel will be equal to the
number of bytes written to the file so far unless this stream is in
append mode, in which case it will be equal to the size of the file.
Writing bytes to this stream will increment the channel's position
accordingly. Changing the channel's position, either explicitly or by
writing, will change this stream's file position.

**Returns:** the file channel associated with this file output stream
**Since:** 1.4

- finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be removed.
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

Cleans up the connection to the file, and ensures that the

close()

method of this file output stream is
called when there are no more references to this stream.
The

finalize()

method does not call

close()

directly.

**Overrides:** finalize

in class

Object
**API Note:** To release resources used by this stream

close()

should be called
directly or by try-with-resources.
**Implementation Requirements:** If this FileOutputStream has been subclassed and the

close()

method has been overridden, the

close()

method will be
called when the FileOutputStream is unreachable.
Otherwise, it is implementation specific how the resource cleanup described in

close()

is performed.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FileInputStream.close()

Constructor Detail

- FileOutputStream

```java
public FileOutputStream​(
String
name)
throws
FileNotFoundException
```

Creates a file output stream to write to the file with the
specified name. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Implementation Requirements:** Invoking this constructor with the parameter

name

is
equivalent to invoking

new FileOutputStream(name, false)

.
**Parameters:** name

- the system-dependent filename
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**See Also:** SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
String
name,
boolean append)
throws
FileNotFoundException
```

Creates a file output stream to write to the file with the specified
name. If the second argument is

true

, then
bytes will be written to the end of the file rather than the beginning.
A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** name

- the system-dependent file name
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason.
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**Since:** 1.1
**See Also:** SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
File
file)
throws
FileNotFoundException
```

Creates a file output stream to write to the file represented by
the specified

File

object. A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** file

- the file to be opened for writing.
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**See Also:** File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
File
file,
boolean append)
throws
FileNotFoundException
```

Creates a file output stream to write to the file represented by
the specified

File

object. If the second argument is

true

, then bytes will be written to the end of the file
rather than the beginning. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** file

- the file to be opened for writing.
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**Since:** 1.4
**See Also:** File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

- FileOutputStream

```java
public FileOutputStream​(
FileDescriptor
fdObj)
```

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

First, if there is a security manager, its

checkWrite

method is called with the file descriptor

fdObj

argument as its argument.

If

fdObj

is null then a

NullPointerException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

**Parameters:** fdObj

- the file descriptor to be opened for writing
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies
write access to the file descriptor
**See Also:** SecurityManager.checkWrite(java.io.FileDescriptor)

---

#### Constructor Detail

FileOutputStream

```java
public FileOutputStream​(
String
name)
throws
FileNotFoundException
```

Creates a file output stream to write to the file with the
specified name. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Implementation Requirements:** Invoking this constructor with the parameter

name

is
equivalent to invoking

new FileOutputStream(name, false)

.
**Parameters:** name

- the system-dependent filename
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**See Also:** SecurityManager.checkWrite(java.lang.String)

---

#### FileOutputStream

public FileOutputStream​(

String

name)
throws

FileNotFoundException

Creates a file output stream to write to the file with the
specified name. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

FileOutputStream

```java
public FileOutputStream​(
String
name,
boolean append)
throws
FileNotFoundException
```

Creates a file output stream to write to the file with the specified
name. If the second argument is

true

, then
bytes will be written to the end of the file rather than the beginning.
A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** name

- the system-dependent file name
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason.
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**Since:** 1.1
**See Also:** SecurityManager.checkWrite(java.lang.String)

---

#### FileOutputStream

public FileOutputStream​(

String

name,
boolean append)
throws

FileNotFoundException

Creates a file output stream to write to the file with the specified
name. If the second argument is

true

, then
bytes will be written to the end of the file rather than the beginning.
A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

First, if there is a security manager, its

checkWrite

method is called with

name

as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

FileOutputStream

```java
public FileOutputStream​(
File
file)
throws
FileNotFoundException
```

Creates a file output stream to write to the file represented by
the specified

File

object. A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** file

- the file to be opened for writing.
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**See Also:** File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

---

#### FileOutputStream

public FileOutputStream​(

File

file)
throws

FileNotFoundException

Creates a file output stream to write to the file represented by
the specified

File

object. A new

FileDescriptor

object is created to represent this
file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

FileOutputStream

```java
public FileOutputStream​(
File
file,
boolean append)
throws
FileNotFoundException
```

Creates a file output stream to write to the file represented by
the specified

File

object. If the second argument is

true

, then bytes will be written to the end of the file
rather than the beginning. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

**Parameters:** file

- the file to be opened for writing.
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** FileNotFoundException

- if the file exists but is a directory
rather than a regular file, does not exist but cannot
be created, or cannot be opened for any other reason
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies write access
to the file.
**Since:** 1.4
**See Also:** File.getPath()

,

SecurityException

,

SecurityManager.checkWrite(java.lang.String)

---

#### FileOutputStream

public FileOutputStream​(

File

file,
boolean append)
throws

FileNotFoundException

Creates a file output stream to write to the file represented by
the specified

File

object. If the second argument is

true

, then bytes will be written to the end of the file
rather than the beginning. A new

FileDescriptor

object is
created to represent this file connection.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

First, if there is a security manager, its

checkWrite

method is called with the path represented by the

file

argument as its argument.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

If the file exists but is a directory rather than a regular file, does
not exist but cannot be created, or cannot be opened for any other
reason then a

FileNotFoundException

is thrown.

FileOutputStream

```java
public FileOutputStream​(
FileDescriptor
fdObj)
```

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

First, if there is a security manager, its

checkWrite

method is called with the file descriptor

fdObj

argument as its argument.

If

fdObj

is null then a

NullPointerException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

**Parameters:** fdObj

- the file descriptor to be opened for writing
**Throws:** SecurityException

- if a security manager exists and its

checkWrite

method denies
write access to the file descriptor
**See Also:** SecurityManager.checkWrite(java.io.FileDescriptor)

---

#### FileOutputStream

public FileOutputStream​(

FileDescriptor

fdObj)

Creates a file output stream to write to the specified file
descriptor, which represents an existing connection to an actual
file in the file system.

First, if there is a security manager, its

checkWrite

method is called with the file descriptor

fdObj

argument as its argument.

If

fdObj

is null then a

NullPointerException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

First, if there is a security manager, its

checkWrite

method is called with the file descriptor

fdObj

argument as its argument.

If

fdObj

is null then a

NullPointerException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

If

fdObj

is null then a

NullPointerException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

This constructor does not throw an exception if

fdObj

is

invalid

.
However, if the methods are invoked on the resulting stream to attempt
I/O on the stream, an

IOException

is thrown.

Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this file output stream. Implements
the

write

method of

OutputStream

.

**Specified by:** write

in class

OutputStream
**Parameters:** b

- the byte to be written.
**Throws:** IOException

- if an I/O error occurs.

- write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this file output stream.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** OutputStream.write(byte[], int, int)

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this file output stream and releases any system resources
associated with this stream. This file output stream may no longer
be used for writing bytes.

If this stream has an associated channel then the channel is closed
as well.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

OutputStream
**API Note:** Overriding

close()

to perform cleanup actions is reliable
only when called directly or when called by try-with-resources.
Do not depend on finalization to invoke

close

;
finalization is not reliable and is deprecated.
If cleanup of native resources is needed, other mechanisms such as

Cleaner

should be used.
**Throws:** IOException

- if an I/O error occurs.

- getFD

```java
public final
FileDescriptor
getFD()
throws
IOException
```

Returns the file descriptor associated with this stream.

**Returns:** the

FileDescriptor

object that represents
the connection to the file in the file system being used
by this

FileOutputStream

object.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FileDescriptor

- getChannel

```java
public
FileChannel
getChannel()
```

Returns the unique

FileChannel

object associated with this file output stream.

The initial

position

of the returned channel will be equal to the
number of bytes written to the file so far unless this stream is in
append mode, in which case it will be equal to the size of the file.
Writing bytes to this stream will increment the channel's position
accordingly. Changing the channel's position, either explicitly or by
writing, will change this stream's file position.

**Returns:** the file channel associated with this file output stream
**Since:** 1.4

- finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be removed.
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

Cleans up the connection to the file, and ensures that the

close()

method of this file output stream is
called when there are no more references to this stream.
The

finalize()

method does not call

close()

directly.

**Overrides:** finalize

in class

Object
**API Note:** To release resources used by this stream

close()

should be called
directly or by try-with-resources.
**Implementation Requirements:** If this FileOutputStream has been subclassed and the

close()

method has been overridden, the

close()

method will be
called when the FileOutputStream is unreachable.
Otherwise, it is implementation specific how the resource cleanup described in

close()

is performed.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FileInputStream.close()

---

#### Method Detail

write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this file output stream. Implements
the

write

method of

OutputStream

.

**Specified by:** write

in class

OutputStream
**Parameters:** b

- the byte to be written.
**Throws:** IOException

- if an I/O error occurs.

---

#### write

public void write​(int b)
throws

IOException

Writes the specified byte to this file output stream. Implements
the

write

method of

OutputStream

.

write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this file output stream.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** OutputStream.write(byte[], int, int)

---

#### write

public void write​(byte[] b)
throws

IOException

Writes

b.length

bytes from the specified byte array
to this file output stream.

write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.

---

#### write

public void write​(byte[] b,
int off,
int len)
throws

IOException

Writes

len

bytes from the specified byte array
starting at offset

off

to this file output stream.

close

```java
public void close()
throws
IOException
```

Closes this file output stream and releases any system resources
associated with this stream. This file output stream may no longer
be used for writing bytes.

If this stream has an associated channel then the channel is closed
as well.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

OutputStream
**API Note:** Overriding

close()

to perform cleanup actions is reliable
only when called directly or when called by try-with-resources.
Do not depend on finalization to invoke

close

;
finalization is not reliable and is deprecated.
If cleanup of native resources is needed, other mechanisms such as

Cleaner

should be used.
**Throws:** IOException

- if an I/O error occurs.

---

#### close

public void close()
throws

IOException

Closes this file output stream and releases any system resources
associated with this stream. This file output stream may no longer
be used for writing bytes.

If this stream has an associated channel then the channel is closed
as well.

If this stream has an associated channel then the channel is closed
as well.

getFD

```java
public final
FileDescriptor
getFD()
throws
IOException
```

Returns the file descriptor associated with this stream.

**Returns:** the

FileDescriptor

object that represents
the connection to the file in the file system being used
by this

FileOutputStream

object.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FileDescriptor

---

#### getFD

public final

FileDescriptor

getFD()
throws

IOException

Returns the file descriptor associated with this stream.

getChannel

```java
public
FileChannel
getChannel()
```

Returns the unique

FileChannel

object associated with this file output stream.

The initial

position

of the returned channel will be equal to the
number of bytes written to the file so far unless this stream is in
append mode, in which case it will be equal to the size of the file.
Writing bytes to this stream will increment the channel's position
accordingly. Changing the channel's position, either explicitly or by
writing, will change this stream's file position.

**Returns:** the file channel associated with this file output stream
**Since:** 1.4

---

#### getChannel

public

FileChannel

getChannel()

Returns the unique

FileChannel

object associated with this file output stream.

The initial

position

of the returned channel will be equal to the
number of bytes written to the file so far unless this stream is in
append mode, in which case it will be equal to the size of the file.
Writing bytes to this stream will increment the channel's position
accordingly. Changing the channel's position, either explicitly or by
writing, will change this stream's file position.

The initial

position

of the returned channel will be equal to the
number of bytes written to the file so far unless this stream is in
append mode, in which case it will be equal to the size of the file.
Writing bytes to this stream will increment the channel's position
accordingly. Changing the channel's position, either explicitly or by
writing, will change this stream's file position.

finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be removed.
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

Cleans up the connection to the file, and ensures that the

close()

method of this file output stream is
called when there are no more references to this stream.
The

finalize()

method does not call

close()

directly.

**Overrides:** finalize

in class

Object
**API Note:** To release resources used by this stream

close()

should be called
directly or by try-with-resources.
**Implementation Requirements:** If this FileOutputStream has been subclassed and the

close()

method has been overridden, the

close()

method will be
called when the FileOutputStream is unreachable.
Otherwise, it is implementation specific how the resource cleanup described in

close()

is performed.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FileInputStream.close()

---

#### finalize

@Deprecated

(

since

="9",

forRemoval

=true)
protected void finalize()
throws

IOException

Cleans up the connection to the file, and ensures that the

close()

method of this file output stream is
called when there are no more references to this stream.
The

finalize()

method does not call

close()

directly.

---

