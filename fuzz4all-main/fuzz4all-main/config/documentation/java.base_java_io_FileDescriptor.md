# Class FileDescriptor

**Source:** `java.base\java\io\FileDescriptor.html`

### Class Description

```java
public final class
FileDescriptor

extends
Object
```

Instances of the file descriptor class serve as an opaque handle
to the underlying machine-specific structure representing an open
file, an open socket, or another source or sink of bytes.
The main practical use for a file descriptor is to create a

FileInputStream

or

FileOutputStream

to contain it.

Applications should not create their own file descriptors.

**Since:** 1.0

---

### Field Details

#### public static final
FileDescriptor
in

A handle to the standard input stream. Usually, this file
descriptor is not used directly, but rather via the input stream
known as

System.in

.

**See Also:**
- System.in

---

#### public static final
FileDescriptor
out

A handle to the standard output stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.out

.

**See Also:**
- System.out

---

#### public static final
FileDescriptor
err

A handle to the standard error stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.err

.

**See Also:**
- System.err

---

### Constructor Details

#### public FileDescriptor()

Constructs an (invalid) FileDescriptor object.
The fd or handle is set later.

---

### Method Details

#### public boolean valid()

Tests if this file descriptor object is valid.

**Returns:**
- true

if the file descriptor object represents a
valid, open file, socket, or other active I/O connection;

false

otherwise.

---

#### public void sync()
throws
SyncFailedException

Force all system buffers to synchronize with the underlying
device. This method returns after all modified data and
attributes of this FileDescriptor have been written to the
relevant device(s). In particular, if this FileDescriptor
refers to a physical storage medium, such as a file in a file
system, sync will not return until all in-memory modified copies
of buffers associated with this FileDescriptor have been
written to the physical medium.

sync is meant to be used by code that requires physical
storage (such as a file) to be in a known state For
example, a class that provided a simple transaction facility
might use sync to ensure that all changes to a file caused
by a given transaction were recorded on a storage medium.

sync only affects buffers downstream of this FileDescriptor. If
any in-memory buffering is being done by the application (for
example, by a BufferedOutputStream object), those buffers must
be flushed into the FileDescriptor (for example, by invoking
OutputStream.flush) before that data will be affected by sync.

**Throws:**
- SyncFailedException

- Thrown when the buffers cannot be flushed,
or because the system cannot guarantee that all the
buffers have been synchronized with physical media.

**Since:**
- 1.1

---

### Additional Sections

#### Class FileDescriptor

java.lang.Object

- java.io.FileDescriptor

java.io.FileDescriptor

```java
public final class
FileDescriptor

extends
Object
```

Instances of the file descriptor class serve as an opaque handle
to the underlying machine-specific structure representing an open
file, an open socket, or another source or sink of bytes.
The main practical use for a file descriptor is to create a

FileInputStream

or

FileOutputStream

to contain it.

Applications should not create their own file descriptors.

**Since:** 1.0

public final class

FileDescriptor

extends

Object

Instances of the file descriptor class serve as an opaque handle
to the underlying machine-specific structure representing an open
file, an open socket, or another source or sink of bytes.
The main practical use for a file descriptor is to create a

FileInputStream

or

FileOutputStream

to contain it.

Applications should not create their own file descriptors.

Applications should not create their own file descriptors.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

FileDescriptor

err

A handle to the standard error stream.

static

FileDescriptor

in

A handle to the standard input stream.

static

FileDescriptor

out

A handle to the standard output stream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileDescriptor

()

Constructs an (invalid) FileDescriptor object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

sync

()

Force all system buffers to synchronize with the underlying
device.

boolean

valid

()

Tests if this file descriptor object is valid.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

FileDescriptor

err

A handle to the standard error stream.

static

FileDescriptor

in

A handle to the standard input stream.

static

FileDescriptor

out

A handle to the standard output stream.

---

#### Field Summary

A handle to the standard error stream.

A handle to the standard input stream.

A handle to the standard output stream.

Constructor Summary

Constructors

Constructor

Description

FileDescriptor

()

Constructs an (invalid) FileDescriptor object.

---

#### Constructor Summary

Constructs an (invalid) FileDescriptor object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

sync

()

Force all system buffers to synchronize with the underlying
device.

boolean

valid

()

Tests if this file descriptor object is valid.

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

Force all system buffers to synchronize with the underlying
device.

Tests if this file descriptor object is valid.

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

============ FIELD DETAIL ===========

- Field Detail

- in

```java
public static final
FileDescriptor
in
```

A handle to the standard input stream. Usually, this file
descriptor is not used directly, but rather via the input stream
known as

System.in

.

**See Also:** System.in

- out

```java
public static final
FileDescriptor
out
```

A handle to the standard output stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.out

.

**See Also:** System.out

- err

```java
public static final
FileDescriptor
err
```

A handle to the standard error stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.err

.

**See Also:** System.err

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FileDescriptor

```java
public FileDescriptor()
```

Constructs an (invalid) FileDescriptor object.
The fd or handle is set later.

============ METHOD DETAIL ==========

- Method Detail

- valid

```java
public boolean valid()
```

Tests if this file descriptor object is valid.

**Returns:** true

if the file descriptor object represents a
valid, open file, socket, or other active I/O connection;

false

otherwise.

- sync

```java
public void sync()
throws
SyncFailedException
```

Force all system buffers to synchronize with the underlying
device. This method returns after all modified data and
attributes of this FileDescriptor have been written to the
relevant device(s). In particular, if this FileDescriptor
refers to a physical storage medium, such as a file in a file
system, sync will not return until all in-memory modified copies
of buffers associated with this FileDescriptor have been
written to the physical medium.

sync is meant to be used by code that requires physical
storage (such as a file) to be in a known state For
example, a class that provided a simple transaction facility
might use sync to ensure that all changes to a file caused
by a given transaction were recorded on a storage medium.

sync only affects buffers downstream of this FileDescriptor. If
any in-memory buffering is being done by the application (for
example, by a BufferedOutputStream object), those buffers must
be flushed into the FileDescriptor (for example, by invoking
OutputStream.flush) before that data will be affected by sync.

**Throws:** SyncFailedException

- Thrown when the buffers cannot be flushed,
or because the system cannot guarantee that all the
buffers have been synchronized with physical media.
**Since:** 1.1

Field Detail

- in

```java
public static final
FileDescriptor
in
```

A handle to the standard input stream. Usually, this file
descriptor is not used directly, but rather via the input stream
known as

System.in

.

**See Also:** System.in

- out

```java
public static final
FileDescriptor
out
```

A handle to the standard output stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.out

.

**See Also:** System.out

- err

```java
public static final
FileDescriptor
err
```

A handle to the standard error stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.err

.

**See Also:** System.err

---

#### Field Detail

in

```java
public static final
FileDescriptor
in
```

A handle to the standard input stream. Usually, this file
descriptor is not used directly, but rather via the input stream
known as

System.in

.

**See Also:** System.in

---

#### in

public static final

FileDescriptor

in

A handle to the standard input stream. Usually, this file
descriptor is not used directly, but rather via the input stream
known as

System.in

.

out

```java
public static final
FileDescriptor
out
```

A handle to the standard output stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.out

.

**See Also:** System.out

---

#### out

public static final

FileDescriptor

out

A handle to the standard output stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.out

.

err

```java
public static final
FileDescriptor
err
```

A handle to the standard error stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.err

.

**See Also:** System.err

---

#### err

public static final

FileDescriptor

err

A handle to the standard error stream. Usually, this file
descriptor is not used directly, but rather via the output stream
known as

System.err

.

Constructor Detail

- FileDescriptor

```java
public FileDescriptor()
```

Constructs an (invalid) FileDescriptor object.
The fd or handle is set later.

---

#### Constructor Detail

FileDescriptor

```java
public FileDescriptor()
```

Constructs an (invalid) FileDescriptor object.
The fd or handle is set later.

---

#### FileDescriptor

public FileDescriptor()

Constructs an (invalid) FileDescriptor object.
The fd or handle is set later.

Method Detail

- valid

```java
public boolean valid()
```

Tests if this file descriptor object is valid.

**Returns:** true

if the file descriptor object represents a
valid, open file, socket, or other active I/O connection;

false

otherwise.

- sync

```java
public void sync()
throws
SyncFailedException
```

Force all system buffers to synchronize with the underlying
device. This method returns after all modified data and
attributes of this FileDescriptor have been written to the
relevant device(s). In particular, if this FileDescriptor
refers to a physical storage medium, such as a file in a file
system, sync will not return until all in-memory modified copies
of buffers associated with this FileDescriptor have been
written to the physical medium.

sync is meant to be used by code that requires physical
storage (such as a file) to be in a known state For
example, a class that provided a simple transaction facility
might use sync to ensure that all changes to a file caused
by a given transaction were recorded on a storage medium.

sync only affects buffers downstream of this FileDescriptor. If
any in-memory buffering is being done by the application (for
example, by a BufferedOutputStream object), those buffers must
be flushed into the FileDescriptor (for example, by invoking
OutputStream.flush) before that data will be affected by sync.

**Throws:** SyncFailedException

- Thrown when the buffers cannot be flushed,
or because the system cannot guarantee that all the
buffers have been synchronized with physical media.
**Since:** 1.1

---

#### Method Detail

valid

```java
public boolean valid()
```

Tests if this file descriptor object is valid.

**Returns:** true

if the file descriptor object represents a
valid, open file, socket, or other active I/O connection;

false

otherwise.

---

#### valid

public boolean valid()

Tests if this file descriptor object is valid.

sync

```java
public void sync()
throws
SyncFailedException
```

Force all system buffers to synchronize with the underlying
device. This method returns after all modified data and
attributes of this FileDescriptor have been written to the
relevant device(s). In particular, if this FileDescriptor
refers to a physical storage medium, such as a file in a file
system, sync will not return until all in-memory modified copies
of buffers associated with this FileDescriptor have been
written to the physical medium.

sync is meant to be used by code that requires physical
storage (such as a file) to be in a known state For
example, a class that provided a simple transaction facility
might use sync to ensure that all changes to a file caused
by a given transaction were recorded on a storage medium.

sync only affects buffers downstream of this FileDescriptor. If
any in-memory buffering is being done by the application (for
example, by a BufferedOutputStream object), those buffers must
be flushed into the FileDescriptor (for example, by invoking
OutputStream.flush) before that data will be affected by sync.

**Throws:** SyncFailedException

- Thrown when the buffers cannot be flushed,
or because the system cannot guarantee that all the
buffers have been synchronized with physical media.
**Since:** 1.1

---

#### sync

public void sync()
throws

SyncFailedException

Force all system buffers to synchronize with the underlying
device. This method returns after all modified data and
attributes of this FileDescriptor have been written to the
relevant device(s). In particular, if this FileDescriptor
refers to a physical storage medium, such as a file in a file
system, sync will not return until all in-memory modified copies
of buffers associated with this FileDescriptor have been
written to the physical medium.

sync is meant to be used by code that requires physical
storage (such as a file) to be in a known state For
example, a class that provided a simple transaction facility
might use sync to ensure that all changes to a file caused
by a given transaction were recorded on a storage medium.

sync only affects buffers downstream of this FileDescriptor. If
any in-memory buffering is being done by the application (for
example, by a BufferedOutputStream object), those buffers must
be flushed into the FileDescriptor (for example, by invoking
OutputStream.flush) before that data will be affected by sync.

---

