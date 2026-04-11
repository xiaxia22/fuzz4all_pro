# Class FileStore

**Source:** `java.base\java\nio\file\FileStore.html`

### Class Description

```java
public abstract class
FileStore

extends
Object
```

Storage for files. A

FileStore

represents a storage pool, device,
partition, volume, concrete file system or other implementation specific means
of file storage. The

FileStore

for where a file is stored is obtained
by invoking the

getFileStore

method, or all file
stores can be enumerated by invoking the

getFileStores

method.

In addition to the methods defined by this class, a file store may support
one or more

FileStoreAttributeView

classes
that provide a read-only or updatable view of a set of file store attributes.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

#### protected FileStore()

Initializes a new instance of this class.

---

### Method Details

#### public abstract
String
name()

Returns the name of this file store. The format of the name is highly
implementation specific. It will typically be the name of the storage
pool or volume.

The string returned by this method may differ from the string
returned by the

toString

method.

**Returns:**
- the name of this file store

---

#### public abstract
String
type()

Returns the

type

of this file store. The format of the string
returned by this method is highly implementation specific. It may
indicate, for example, the format used or if the file store is local
or remote.

**Returns:**
- a string representing the type of this file store

---

#### public abstract boolean isReadOnly()

Tells whether this file store is read-only. A file store is read-only if
it does not support write operations or other changes to files. Any
attempt to create a file, open an existing file for writing etc. causes
an

IOException

to be thrown.

**Returns:**
- true

if, and only if, this file store is read-only

---

#### public abstract long getTotalSpace()
throws
IOException

Returns the size, in bytes, of the file store.

**Returns:**
- the size of the file store, in bytes

**Throws:**
- IOException

- if an I/O error occurs

---

#### public abstract long getUsableSpace()
throws
IOException

Returns the number of bytes available to this Java virtual machine on the
file store.

The returned number of available bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of usable bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be made inaccurate
by any external I/O operations including those made on the system outside
of this Java virtual machine.

**Returns:**
- the number of bytes available

**Throws:**
- IOException

- if an I/O error occurs

---

#### public long getBlockSize()
throws
IOException

Returns the number of bytes per block in this file store.

File storage is typically organized into discrete sequences of bytes
called

blocks

. A block is the smallest storage unit of a file store.
Every read and write operation is performed on a multiple of blocks.

**Returns:**
- a positive value representing the block size of this file store,
in bytes

**Throws:**
- IOException

- if an I/O error occurs
- UnsupportedOperationException

- if the operation is not supported

**Since:**
- 10

**Implementation Requirements:**
- The implementation in this class throws an

UnsupportedOperationException

.

---

#### public abstract long getUnallocatedSpace()
throws
IOException

Returns the number of unallocated bytes in the file store.

The returned number of unallocated bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of unallocated bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be
made inaccurate by any external I/O operations including those made on
the system outside of this virtual machine.

**Returns:**
- the number of unallocated bytes

**Throws:**
- IOException

- if an I/O error occurs

---

#### public abstract boolean supportsFileAttributeView​(
Class
<? extends
FileAttributeView
> type)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

will always return

true

. In the case of
the default provider, this method cannot guarantee to give the correct
result when the file store is not a local storage device. The reasons for
this are implementation specific and therefore unspecified.

**Parameters:**
- type

- the file attribute view type

**Returns:**
- true

if, and only if, the file attribute view is
supported

---

#### public abstract boolean supportsFileAttributeView​(
String
name)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

, identified by the name "

basic

" will
always return

true

. In the case of the default provider, this
method cannot guarantee to give the correct result when the file store is
not a local storage device. The reasons for this are implementation
specific and therefore unspecified.

**Parameters:**
- name

- the

name

of file attribute view

**Returns:**
- true

if, and only if, the file attribute view is
supported

---

#### public abstract <V extends
FileStoreAttributeView
> V getFileStoreAttributeView​(
Class
<V> type)

Returns a

FileStoreAttributeView

of the given type.

This method is intended to be used where the file store attribute
view defines type-safe methods to read or update the file store attributes.
The

type

parameter is the type of the attribute view required and
the method returns an instance of that type if supported.

**Parameters:**
- type

- the

Class

object corresponding to the attribute view

**Returns:**
- a file store attribute view of the specified type or

null

if the attribute view is not available

**Type Parameters:**
- V

- The

FileStoreAttributeView

type

---

#### public abstract
Object
getAttribute​(
String
attribute)
throws
IOException

Reads the value of a file store attribute.

The

attribute

parameter identifies the attribute to be read
and takes the form:

view-name

:

attribute-name

where the character

':'

stands for itself.

view-name

is the

name

of
a

AttributeView

that identifies a set of file attributes.

attribute-name

is the name of the attribute.

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

**Parameters:**
- attribute

- the attribute to read

**Returns:**
- the attribute value;

null

may be valid for some
attributes

**Throws:**
- UnsupportedOperationException

- if the attribute view is not available or it does not support
reading the attribute
- IOException

- if an I/O error occurs

---

### Additional Sections

#### Class FileStore

java.lang.Object

- java.nio.file.FileStore

java.nio.file.FileStore

```java
public abstract class
FileStore

extends
Object
```

Storage for files. A

FileStore

represents a storage pool, device,
partition, volume, concrete file system or other implementation specific means
of file storage. The

FileStore

for where a file is stored is obtained
by invoking the

getFileStore

method, or all file
stores can be enumerated by invoking the

getFileStores

method.

In addition to the methods defined by this class, a file store may support
one or more

FileStoreAttributeView

classes
that provide a read-only or updatable view of a set of file store attributes.

**Since:** 1.7

public abstract class

FileStore

extends

Object

Storage for files. A

FileStore

represents a storage pool, device,
partition, volume, concrete file system or other implementation specific means
of file storage. The

FileStore

for where a file is stored is obtained
by invoking the

getFileStore

method, or all file
stores can be enumerated by invoking the

getFileStores

method.

In addition to the methods defined by this class, a file store may support
one or more

FileStoreAttributeView

classes
that provide a read-only or updatable view of a set of file store attributes.

In addition to the methods defined by this class, a file store may support
one or more

FileStoreAttributeView

classes
that provide a read-only or updatable view of a set of file store attributes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FileStore

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Object

getAttribute

​(

String

attribute)

Reads the value of a file store attribute.

long

getBlockSize

()

Returns the number of bytes per block in this file store.

abstract <V extends

FileStoreAttributeView

>

V

getFileStoreAttributeView

​(

Class

<V> type)

Returns a

FileStoreAttributeView

of the given type.

abstract long

getTotalSpace

()

Returns the size, in bytes, of the file store.

abstract long

getUnallocatedSpace

()

Returns the number of unallocated bytes in the file store.

abstract long

getUsableSpace

()

Returns the number of bytes available to this Java virtual machine on the
file store.

abstract boolean

isReadOnly

()

Tells whether this file store is read-only.

abstract

String

name

()

Returns the name of this file store.

abstract boolean

supportsFileAttributeView

​(

Class

<? extends

FileAttributeView

> type)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

abstract boolean

supportsFileAttributeView

​(

String

name)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

abstract

String

type

()

Returns the

type

of this file store.

- Methods declared in class java.lang.

Object

clone

,

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

Modifier

Constructor

Description

protected

FileStore

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Object

getAttribute

​(

String

attribute)

Reads the value of a file store attribute.

long

getBlockSize

()

Returns the number of bytes per block in this file store.

abstract <V extends

FileStoreAttributeView

>

V

getFileStoreAttributeView

​(

Class

<V> type)

Returns a

FileStoreAttributeView

of the given type.

abstract long

getTotalSpace

()

Returns the size, in bytes, of the file store.

abstract long

getUnallocatedSpace

()

Returns the number of unallocated bytes in the file store.

abstract long

getUsableSpace

()

Returns the number of bytes available to this Java virtual machine on the
file store.

abstract boolean

isReadOnly

()

Tells whether this file store is read-only.

abstract

String

name

()

Returns the name of this file store.

abstract boolean

supportsFileAttributeView

​(

Class

<? extends

FileAttributeView

> type)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

abstract boolean

supportsFileAttributeView

​(

String

name)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

abstract

String

type

()

Returns the

type

of this file store.

- Methods declared in class java.lang.

Object

clone

,

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

Reads the value of a file store attribute.

Returns the number of bytes per block in this file store.

Returns a

FileStoreAttributeView

of the given type.

Returns the size, in bytes, of the file store.

Returns the number of unallocated bytes in the file store.

Returns the number of bytes available to this Java virtual machine on the
file store.

Tells whether this file store is read-only.

Returns the name of this file store.

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Returns the

type

of this file store.

Methods declared in class java.lang.

Object

clone

,

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

- FileStore

```java
protected FileStore()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
public abstract
String
name()
```

Returns the name of this file store. The format of the name is highly
implementation specific. It will typically be the name of the storage
pool or volume.

The string returned by this method may differ from the string
returned by the

toString

method.

**Returns:** the name of this file store

- type

```java
public abstract
String
type()
```

Returns the

type

of this file store. The format of the string
returned by this method is highly implementation specific. It may
indicate, for example, the format used or if the file store is local
or remote.

**Returns:** a string representing the type of this file store

- isReadOnly

```java
public abstract boolean isReadOnly()
```

Tells whether this file store is read-only. A file store is read-only if
it does not support write operations or other changes to files. Any
attempt to create a file, open an existing file for writing etc. causes
an

IOException

to be thrown.

**Returns:** true

if, and only if, this file store is read-only

- getTotalSpace

```java
public abstract long getTotalSpace()
throws
IOException
```

Returns the size, in bytes, of the file store.

**Returns:** the size of the file store, in bytes
**Throws:** IOException

- if an I/O error occurs

- getUsableSpace

```java
public abstract long getUsableSpace()
throws
IOException
```

Returns the number of bytes available to this Java virtual machine on the
file store.

The returned number of available bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of usable bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be made inaccurate
by any external I/O operations including those made on the system outside
of this Java virtual machine.

**Returns:** the number of bytes available
**Throws:** IOException

- if an I/O error occurs

- getBlockSize

```java
public long getBlockSize()
throws
IOException
```

Returns the number of bytes per block in this file store.

File storage is typically organized into discrete sequences of bytes
called

blocks

. A block is the smallest storage unit of a file store.
Every read and write operation is performed on a multiple of blocks.

**Implementation Requirements:** The implementation in this class throws an

UnsupportedOperationException

.
**Returns:** a positive value representing the block size of this file store,
in bytes
**Throws:** IOException

- if an I/O error occurs
**Throws:** UnsupportedOperationException

- if the operation is not supported
**Since:** 10

- getUnallocatedSpace

```java
public abstract long getUnallocatedSpace()
throws
IOException
```

Returns the number of unallocated bytes in the file store.

The returned number of unallocated bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of unallocated bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be
made inaccurate by any external I/O operations including those made on
the system outside of this virtual machine.

**Returns:** the number of unallocated bytes
**Throws:** IOException

- if an I/O error occurs

- supportsFileAttributeView

```java
public abstract boolean supportsFileAttributeView​(
Class
<? extends
FileAttributeView
> type)
```

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

will always return

true

. In the case of
the default provider, this method cannot guarantee to give the correct
result when the file store is not a local storage device. The reasons for
this are implementation specific and therefore unspecified.

**Parameters:** type

- the file attribute view type
**Returns:** true

if, and only if, the file attribute view is
supported

- supportsFileAttributeView

```java
public abstract boolean supportsFileAttributeView​(
String
name)
```

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

, identified by the name "

basic

" will
always return

true

. In the case of the default provider, this
method cannot guarantee to give the correct result when the file store is
not a local storage device. The reasons for this are implementation
specific and therefore unspecified.

**Parameters:** name

- the

name

of file attribute view
**Returns:** true

if, and only if, the file attribute view is
supported

- getFileStoreAttributeView

```java
public abstract <V extends
FileStoreAttributeView
> V getFileStoreAttributeView​(
Class
<V> type)
```

Returns a

FileStoreAttributeView

of the given type.

This method is intended to be used where the file store attribute
view defines type-safe methods to read or update the file store attributes.
The

type

parameter is the type of the attribute view required and
the method returns an instance of that type if supported.

**Type Parameters:** V

- The

FileStoreAttributeView

type
**Parameters:** type

- the

Class

object corresponding to the attribute view
**Returns:** a file store attribute view of the specified type or

null

if the attribute view is not available

- getAttribute

```java
public abstract
Object
getAttribute​(
String
attribute)
throws
IOException
```

Reads the value of a file store attribute.

The

attribute

parameter identifies the attribute to be read
and takes the form:

view-name

:

attribute-name

where the character

':'

stands for itself.

view-name

is the

name

of
a

AttributeView

that identifies a set of file attributes.

attribute-name

is the name of the attribute.

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

**Parameters:** attribute

- the attribute to read
**Returns:** the attribute value;

null

may be valid for some
attributes
**Throws:** UnsupportedOperationException

- if the attribute view is not available or it does not support
reading the attribute
**Throws:** IOException

- if an I/O error occurs

Constructor Detail

- FileStore

```java
protected FileStore()
```

Initializes a new instance of this class.

---

#### Constructor Detail

FileStore

```java
protected FileStore()
```

Initializes a new instance of this class.

---

#### FileStore

protected FileStore()

Initializes a new instance of this class.

Method Detail

- name

```java
public abstract
String
name()
```

Returns the name of this file store. The format of the name is highly
implementation specific. It will typically be the name of the storage
pool or volume.

The string returned by this method may differ from the string
returned by the

toString

method.

**Returns:** the name of this file store

- type

```java
public abstract
String
type()
```

Returns the

type

of this file store. The format of the string
returned by this method is highly implementation specific. It may
indicate, for example, the format used or if the file store is local
or remote.

**Returns:** a string representing the type of this file store

- isReadOnly

```java
public abstract boolean isReadOnly()
```

Tells whether this file store is read-only. A file store is read-only if
it does not support write operations or other changes to files. Any
attempt to create a file, open an existing file for writing etc. causes
an

IOException

to be thrown.

**Returns:** true

if, and only if, this file store is read-only

- getTotalSpace

```java
public abstract long getTotalSpace()
throws
IOException
```

Returns the size, in bytes, of the file store.

**Returns:** the size of the file store, in bytes
**Throws:** IOException

- if an I/O error occurs

- getUsableSpace

```java
public abstract long getUsableSpace()
throws
IOException
```

Returns the number of bytes available to this Java virtual machine on the
file store.

The returned number of available bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of usable bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be made inaccurate
by any external I/O operations including those made on the system outside
of this Java virtual machine.

**Returns:** the number of bytes available
**Throws:** IOException

- if an I/O error occurs

- getBlockSize

```java
public long getBlockSize()
throws
IOException
```

Returns the number of bytes per block in this file store.

File storage is typically organized into discrete sequences of bytes
called

blocks

. A block is the smallest storage unit of a file store.
Every read and write operation is performed on a multiple of blocks.

**Implementation Requirements:** The implementation in this class throws an

UnsupportedOperationException

.
**Returns:** a positive value representing the block size of this file store,
in bytes
**Throws:** IOException

- if an I/O error occurs
**Throws:** UnsupportedOperationException

- if the operation is not supported
**Since:** 10

- getUnallocatedSpace

```java
public abstract long getUnallocatedSpace()
throws
IOException
```

Returns the number of unallocated bytes in the file store.

The returned number of unallocated bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of unallocated bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be
made inaccurate by any external I/O operations including those made on
the system outside of this virtual machine.

**Returns:** the number of unallocated bytes
**Throws:** IOException

- if an I/O error occurs

- supportsFileAttributeView

```java
public abstract boolean supportsFileAttributeView​(
Class
<? extends
FileAttributeView
> type)
```

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

will always return

true

. In the case of
the default provider, this method cannot guarantee to give the correct
result when the file store is not a local storage device. The reasons for
this are implementation specific and therefore unspecified.

**Parameters:** type

- the file attribute view type
**Returns:** true

if, and only if, the file attribute view is
supported

- supportsFileAttributeView

```java
public abstract boolean supportsFileAttributeView​(
String
name)
```

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

, identified by the name "

basic

" will
always return

true

. In the case of the default provider, this
method cannot guarantee to give the correct result when the file store is
not a local storage device. The reasons for this are implementation
specific and therefore unspecified.

**Parameters:** name

- the

name

of file attribute view
**Returns:** true

if, and only if, the file attribute view is
supported

- getFileStoreAttributeView

```java
public abstract <V extends
FileStoreAttributeView
> V getFileStoreAttributeView​(
Class
<V> type)
```

Returns a

FileStoreAttributeView

of the given type.

This method is intended to be used where the file store attribute
view defines type-safe methods to read or update the file store attributes.
The

type

parameter is the type of the attribute view required and
the method returns an instance of that type if supported.

**Type Parameters:** V

- The

FileStoreAttributeView

type
**Parameters:** type

- the

Class

object corresponding to the attribute view
**Returns:** a file store attribute view of the specified type or

null

if the attribute view is not available

- getAttribute

```java
public abstract
Object
getAttribute​(
String
attribute)
throws
IOException
```

Reads the value of a file store attribute.

The

attribute

parameter identifies the attribute to be read
and takes the form:

view-name

:

attribute-name

where the character

':'

stands for itself.

view-name

is the

name

of
a

AttributeView

that identifies a set of file attributes.

attribute-name

is the name of the attribute.

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

**Parameters:** attribute

- the attribute to read
**Returns:** the attribute value;

null

may be valid for some
attributes
**Throws:** UnsupportedOperationException

- if the attribute view is not available or it does not support
reading the attribute
**Throws:** IOException

- if an I/O error occurs

---

#### Method Detail

name

```java
public abstract
String
name()
```

Returns the name of this file store. The format of the name is highly
implementation specific. It will typically be the name of the storage
pool or volume.

The string returned by this method may differ from the string
returned by the

toString

method.

**Returns:** the name of this file store

---

#### name

public abstract

String

name()

Returns the name of this file store. The format of the name is highly
implementation specific. It will typically be the name of the storage
pool or volume.

The string returned by this method may differ from the string
returned by the

toString

method.

The string returned by this method may differ from the string
returned by the

toString

method.

type

```java
public abstract
String
type()
```

Returns the

type

of this file store. The format of the string
returned by this method is highly implementation specific. It may
indicate, for example, the format used or if the file store is local
or remote.

**Returns:** a string representing the type of this file store

---

#### type

public abstract

String

type()

Returns the

type

of this file store. The format of the string
returned by this method is highly implementation specific. It may
indicate, for example, the format used or if the file store is local
or remote.

isReadOnly

```java
public abstract boolean isReadOnly()
```

Tells whether this file store is read-only. A file store is read-only if
it does not support write operations or other changes to files. Any
attempt to create a file, open an existing file for writing etc. causes
an

IOException

to be thrown.

**Returns:** true

if, and only if, this file store is read-only

---

#### isReadOnly

public abstract boolean isReadOnly()

Tells whether this file store is read-only. A file store is read-only if
it does not support write operations or other changes to files. Any
attempt to create a file, open an existing file for writing etc. causes
an

IOException

to be thrown.

getTotalSpace

```java
public abstract long getTotalSpace()
throws
IOException
```

Returns the size, in bytes, of the file store.

**Returns:** the size of the file store, in bytes
**Throws:** IOException

- if an I/O error occurs

---

#### getTotalSpace

public abstract long getTotalSpace()
throws

IOException

Returns the size, in bytes, of the file store.

getUsableSpace

```java
public abstract long getUsableSpace()
throws
IOException
```

Returns the number of bytes available to this Java virtual machine on the
file store.

The returned number of available bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of usable bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be made inaccurate
by any external I/O operations including those made on the system outside
of this Java virtual machine.

**Returns:** the number of bytes available
**Throws:** IOException

- if an I/O error occurs

---

#### getUsableSpace

public abstract long getUsableSpace()
throws

IOException

Returns the number of bytes available to this Java virtual machine on the
file store.

The returned number of available bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of usable bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be made inaccurate
by any external I/O operations including those made on the system outside
of this Java virtual machine.

The returned number of available bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of usable bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be made inaccurate
by any external I/O operations including those made on the system outside
of this Java virtual machine.

getBlockSize

```java
public long getBlockSize()
throws
IOException
```

Returns the number of bytes per block in this file store.

File storage is typically organized into discrete sequences of bytes
called

blocks

. A block is the smallest storage unit of a file store.
Every read and write operation is performed on a multiple of blocks.

**Implementation Requirements:** The implementation in this class throws an

UnsupportedOperationException

.
**Returns:** a positive value representing the block size of this file store,
in bytes
**Throws:** IOException

- if an I/O error occurs
**Throws:** UnsupportedOperationException

- if the operation is not supported
**Since:** 10

---

#### getBlockSize

public long getBlockSize()
throws

IOException

Returns the number of bytes per block in this file store.

File storage is typically organized into discrete sequences of bytes
called

blocks

. A block is the smallest storage unit of a file store.
Every read and write operation is performed on a multiple of blocks.

File storage is typically organized into discrete sequences of bytes
called

blocks

. A block is the smallest storage unit of a file store.
Every read and write operation is performed on a multiple of blocks.

getUnallocatedSpace

```java
public abstract long getUnallocatedSpace()
throws
IOException
```

Returns the number of unallocated bytes in the file store.

The returned number of unallocated bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of unallocated bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be
made inaccurate by any external I/O operations including those made on
the system outside of this virtual machine.

**Returns:** the number of unallocated bytes
**Throws:** IOException

- if an I/O error occurs

---

#### getUnallocatedSpace

public abstract long getUnallocatedSpace()
throws

IOException

Returns the number of unallocated bytes in the file store.

The returned number of unallocated bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of unallocated bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be
made inaccurate by any external I/O operations including those made on
the system outside of this virtual machine.

The returned number of unallocated bytes is a hint, but not a
guarantee, that it is possible to use most or any of these bytes. The
number of unallocated bytes is most likely to be accurate immediately
after the space attributes are obtained. It is likely to be
made inaccurate by any external I/O operations including those made on
the system outside of this virtual machine.

supportsFileAttributeView

```java
public abstract boolean supportsFileAttributeView​(
Class
<? extends
FileAttributeView
> type)
```

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

will always return

true

. In the case of
the default provider, this method cannot guarantee to give the correct
result when the file store is not a local storage device. The reasons for
this are implementation specific and therefore unspecified.

**Parameters:** type

- the file attribute view type
**Returns:** true

if, and only if, the file attribute view is
supported

---

#### supportsFileAttributeView

public abstract boolean supportsFileAttributeView​(

Class

<? extends

FileAttributeView

> type)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

will always return

true

. In the case of
the default provider, this method cannot guarantee to give the correct
result when the file store is not a local storage device. The reasons for
this are implementation specific and therefore unspecified.

Invoking this method to test if the file store supports

BasicFileAttributeView

will always return

true

. In the case of
the default provider, this method cannot guarantee to give the correct
result when the file store is not a local storage device. The reasons for
this are implementation specific and therefore unspecified.

supportsFileAttributeView

```java
public abstract boolean supportsFileAttributeView​(
String
name)
```

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

, identified by the name "

basic

" will
always return

true

. In the case of the default provider, this
method cannot guarantee to give the correct result when the file store is
not a local storage device. The reasons for this are implementation
specific and therefore unspecified.

**Parameters:** name

- the

name

of file attribute view
**Returns:** true

if, and only if, the file attribute view is
supported

---

#### supportsFileAttributeView

public abstract boolean supportsFileAttributeView​(

String

name)

Tells whether or not this file store supports the file attributes
identified by the given file attribute view.

Invoking this method to test if the file store supports

BasicFileAttributeView

, identified by the name "

basic

" will
always return

true

. In the case of the default provider, this
method cannot guarantee to give the correct result when the file store is
not a local storage device. The reasons for this are implementation
specific and therefore unspecified.

Invoking this method to test if the file store supports

BasicFileAttributeView

, identified by the name "

basic

" will
always return

true

. In the case of the default provider, this
method cannot guarantee to give the correct result when the file store is
not a local storage device. The reasons for this are implementation
specific and therefore unspecified.

getFileStoreAttributeView

```java
public abstract <V extends
FileStoreAttributeView
> V getFileStoreAttributeView​(
Class
<V> type)
```

Returns a

FileStoreAttributeView

of the given type.

This method is intended to be used where the file store attribute
view defines type-safe methods to read or update the file store attributes.
The

type

parameter is the type of the attribute view required and
the method returns an instance of that type if supported.

**Type Parameters:** V

- The

FileStoreAttributeView

type
**Parameters:** type

- the

Class

object corresponding to the attribute view
**Returns:** a file store attribute view of the specified type or

null

if the attribute view is not available

---

#### getFileStoreAttributeView

public abstract <V extends

FileStoreAttributeView

> V getFileStoreAttributeView​(

Class

<V> type)

Returns a

FileStoreAttributeView

of the given type.

This method is intended to be used where the file store attribute
view defines type-safe methods to read or update the file store attributes.
The

type

parameter is the type of the attribute view required and
the method returns an instance of that type if supported.

This method is intended to be used where the file store attribute
view defines type-safe methods to read or update the file store attributes.
The

type

parameter is the type of the attribute view required and
the method returns an instance of that type if supported.

getAttribute

```java
public abstract
Object
getAttribute​(
String
attribute)
throws
IOException
```

Reads the value of a file store attribute.

The

attribute

parameter identifies the attribute to be read
and takes the form:

view-name

:

attribute-name

where the character

':'

stands for itself.

view-name

is the

name

of
a

AttributeView

that identifies a set of file attributes.

attribute-name

is the name of the attribute.

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

**Parameters:** attribute

- the attribute to read
**Returns:** the attribute value;

null

may be valid for some
attributes
**Throws:** UnsupportedOperationException

- if the attribute view is not available or it does not support
reading the attribute
**Throws:** IOException

- if an I/O error occurs

---

#### getAttribute

public abstract

Object

getAttribute​(

String

attribute)
throws

IOException

Reads the value of a file store attribute.

The

attribute

parameter identifies the attribute to be read
and takes the form:

view-name

:

attribute-name

where the character

':'

stands for itself.

view-name

is the

name

of
a

AttributeView

that identifies a set of file attributes.

attribute-name

is the name of the attribute.

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

The

attribute

parameter identifies the attribute to be read
and takes the form:

view-name

:

attribute-name

where the character

':'

stands for itself.

view-name

is the

name

of
a

AttributeView

that identifies a set of file attributes.

attribute-name

is the name of the attribute.

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

view-name

is the

name

of
a

AttributeView

that identifies a set of file attributes.

attribute-name

is the name of the attribute.

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

Usage Example:

Suppose we want to know if ZFS compression is enabled (assuming the "zfs"
view is supported):

```java
boolean compression = (Boolean)fs.getAttribute("zfs:compression");
```

boolean compression = (Boolean)fs.getAttribute("zfs:compression");

---

