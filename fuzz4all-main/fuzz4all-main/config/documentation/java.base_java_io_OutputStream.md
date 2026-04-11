# Class OutputStream

**Source:** `java.base\java\io\OutputStream.html`

### Class Description

```java
public abstract class
OutputStream

extends
Object

implements
Closeable
,
Flushable
```

This abstract class is the superclass of all classes representing
an output stream of bytes. An output stream accepts output bytes
and sends them to some sink.

Applications that need to define a subclass of

OutputStream

must always provide at least a method
that writes one byte of output.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public OutputStream()

*No description found.*

---

### Method Details

#### public static
OutputStream
nullOutputStream()

Returns a new

OutputStream

which discards all bytes. The
returned stream is initially open. The stream is closed by calling
the

close()

method. Subsequent calls to

close()

have
no effect.

While the stream is open, the

write(int)

,

write(byte[])

, and

write(byte[], int, int)

methods do nothing.
After the stream has been closed, these methods all throw

IOException

.

The

flush()

method does nothing.

**Returns:**
- an

OutputStream

which discards all bytes

**Since:**
- 11

---

#### public abstract void write​(int b)
throws
IOException

Writes the specified byte to this output stream. The general
contract for

write

is that one byte is written
to the output stream. The byte to be written is the eight
low-order bits of the argument

b

. The 24
high-order bits of

b

are ignored.

Subclasses of

OutputStream

must provide an
implementation for this method.

**Parameters:**
- b

- the

byte

.

**Throws:**
- IOException

- if an I/O error occurs. In particular,
an

IOException

may be thrown if the
output stream has been closed.

---

#### public void write​(byte[] b)
throws
IOException

Writes

b.length

bytes from the specified byte array
to this output stream. The general contract for

write(b)

is that it should have exactly the same effect as the call

write(b, 0, b.length)

.

**Parameters:**
- b

- the data.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- write(byte[], int, int)

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

to this output stream.
The general contract for

write(b, off, len)

is that
some of the bytes in the array

b

are written to the
output stream in order; element

b[off]

is the first
byte written and

b[off+len-1]

is the last byte written
by this operation.

The

write

method of

OutputStream

calls
the write method of one argument on each of the bytes to be
written out. Subclasses are encouraged to override this method and
provide a more efficient implementation.

If

b

is

null

, a

NullPointerException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

**Parameters:**
- b

- the data.
- off

- the start offset in the data.
- len

- the number of bytes to write.

**Throws:**
- IOException

- if an I/O error occurs. In particular,
an

IOException

is thrown if the output
stream is closed.

---

#### public void flush()
throws
IOException

Flushes this output stream and forces any buffered output bytes
to be written out. The general contract of

flush

is
that calling it is an indication that, if any bytes previously
written have been buffered by the implementation of the output
stream, such bytes should immediately be written to their
intended destination.

If the intended destination of this stream is an abstraction provided by
the underlying operating system, for example a file, then flushing the
stream guarantees only that bytes previously written to the stream are
passed to the operating system for writing; it does not guarantee that
they are actually written to a physical device such as a disk drive.

The

flush

method of

OutputStream

does nothing.

**Specified by:**
- flush

in interface

Flushable

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public void close()
throws
IOException

Closes this output stream and releases any system resources
associated with this stream. The general contract of

close

is that it closes the output stream. A closed stream cannot perform
output operations and cannot be reopened.

The

close

method of

OutputStream

does nothing.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Throws:**
- IOException

- if an I/O error occurs.

---

### Additional Sections

#### Class OutputStream

java.lang.Object

- java.io.OutputStream

java.io.OutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

**Direct Known Subclasses:** ByteArrayOutputStream

,

FileOutputStream

,

FilterOutputStream

,

ObjectOutputStream

,

PipedOutputStream

```java
public abstract class
OutputStream

extends
Object

implements
Closeable
,
Flushable
```

This abstract class is the superclass of all classes representing
an output stream of bytes. An output stream accepts output bytes
and sends them to some sink.

Applications that need to define a subclass of

OutputStream

must always provide at least a method
that writes one byte of output.

**Since:** 1.0
**See Also:** BufferedOutputStream

,

ByteArrayOutputStream

,

DataOutputStream

,

FilterOutputStream

,

InputStream

,

write(int)

public abstract class

OutputStream

extends

Object

implements

Closeable

,

Flushable

This abstract class is the superclass of all classes representing
an output stream of bytes. An output stream accepts output bytes
and sends them to some sink.

Applications that need to define a subclass of

OutputStream

must always provide at least a method
that writes one byte of output.

Applications that need to define a subclass of

OutputStream

must always provide at least a method
that writes one byte of output.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OutputStream

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this output stream and releases any system resources
associated with this stream.

void

flush

()

Flushes this output stream and forces any buffered output bytes
to be written out.

static

OutputStream

nullOutputStream

()

Returns a new

OutputStream

which discards all bytes.

void

write

​(byte[] b)

Writes

b.length

bytes from the specified byte array
to this output stream.

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

to this output stream.

abstract void

write

​(int b)

Writes the specified byte to this output stream.

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

Constructor

Description

OutputStream

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this output stream and releases any system resources
associated with this stream.

void

flush

()

Flushes this output stream and forces any buffered output bytes
to be written out.

static

OutputStream

nullOutputStream

()

Returns a new

OutputStream

which discards all bytes.

void

write

​(byte[] b)

Writes

b.length

bytes from the specified byte array
to this output stream.

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

to this output stream.

abstract void

write

​(int b)

Writes the specified byte to this output stream.

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

Closes this output stream and releases any system resources
associated with this stream.

Flushes this output stream and forces any buffered output bytes
to be written out.

Returns a new

OutputStream

which discards all bytes.

Writes

b.length

bytes from the specified byte array
to this output stream.

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

Writes the specified byte to this output stream.

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

- OutputStream

```java
public OutputStream()
```

============ METHOD DETAIL ==========

- Method Detail

- nullOutputStream

```java
public static
OutputStream
nullOutputStream()
```

Returns a new

OutputStream

which discards all bytes. The
returned stream is initially open. The stream is closed by calling
the

close()

method. Subsequent calls to

close()

have
no effect.

While the stream is open, the

write(int)

,

write(byte[])

, and

write(byte[], int, int)

methods do nothing.
After the stream has been closed, these methods all throw

IOException

.

The

flush()

method does nothing.

**Returns:** an

OutputStream

which discards all bytes
**Since:** 11

- write

```java
public abstract void write​(int b)
throws
IOException
```

Writes the specified byte to this output stream. The general
contract for

write

is that one byte is written
to the output stream. The byte to be written is the eight
low-order bits of the argument

b

. The 24
high-order bits of

b

are ignored.

Subclasses of

OutputStream

must provide an
implementation for this method.

**Parameters:** b

- the

byte

.
**Throws:** IOException

- if an I/O error occurs. In particular,
an

IOException

may be thrown if the
output stream has been closed.

- write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this output stream. The general contract for

write(b)

is that it should have exactly the same effect as the call

write(b, 0, b.length)

.

**Parameters:** b

- the data.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(byte[], int, int)

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

to this output stream.
The general contract for

write(b, off, len)

is that
some of the bytes in the array

b

are written to the
output stream in order; element

b[off]

is the first
byte written and

b[off+len-1]

is the last byte written
by this operation.

The

write

method of

OutputStream

calls
the write method of one argument on each of the bytes to be
written out. Subclasses are encouraged to override this method and
provide a more efficient implementation.

If

b

is

null

, a

NullPointerException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs. In particular,
an

IOException

is thrown if the output
stream is closed.

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output bytes
to be written out. The general contract of

flush

is
that calling it is an indication that, if any bytes previously
written have been buffered by the implementation of the output
stream, such bytes should immediately be written to their
intended destination.

If the intended destination of this stream is an abstraction provided by
the underlying operating system, for example a file, then flushing the
stream guarantees only that bytes previously written to the stream are
passed to the operating system for writing; it does not guarantee that
they are actually written to a physical device such as a disk drive.

The

flush

method of

OutputStream

does nothing.

**Specified by:** flush

in interface

Flushable
**Throws:** IOException

- if an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with this stream. The general contract of

close

is that it closes the output stream. A closed stream cannot perform
output operations and cannot be reopened.

The

close

method of

OutputStream

does nothing.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error occurs.

Constructor Detail

- OutputStream

```java
public OutputStream()
```

---

#### Constructor Detail

OutputStream

```java
public OutputStream()
```

---

#### OutputStream

public OutputStream()

Method Detail

- nullOutputStream

```java
public static
OutputStream
nullOutputStream()
```

Returns a new

OutputStream

which discards all bytes. The
returned stream is initially open. The stream is closed by calling
the

close()

method. Subsequent calls to

close()

have
no effect.

While the stream is open, the

write(int)

,

write(byte[])

, and

write(byte[], int, int)

methods do nothing.
After the stream has been closed, these methods all throw

IOException

.

The

flush()

method does nothing.

**Returns:** an

OutputStream

which discards all bytes
**Since:** 11

- write

```java
public abstract void write​(int b)
throws
IOException
```

Writes the specified byte to this output stream. The general
contract for

write

is that one byte is written
to the output stream. The byte to be written is the eight
low-order bits of the argument

b

. The 24
high-order bits of

b

are ignored.

Subclasses of

OutputStream

must provide an
implementation for this method.

**Parameters:** b

- the

byte

.
**Throws:** IOException

- if an I/O error occurs. In particular,
an

IOException

may be thrown if the
output stream has been closed.

- write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this output stream. The general contract for

write(b)

is that it should have exactly the same effect as the call

write(b, 0, b.length)

.

**Parameters:** b

- the data.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(byte[], int, int)

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

to this output stream.
The general contract for

write(b, off, len)

is that
some of the bytes in the array

b

are written to the
output stream in order; element

b[off]

is the first
byte written and

b[off+len-1]

is the last byte written
by this operation.

The

write

method of

OutputStream

calls
the write method of one argument on each of the bytes to be
written out. Subclasses are encouraged to override this method and
provide a more efficient implementation.

If

b

is

null

, a

NullPointerException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs. In particular,
an

IOException

is thrown if the output
stream is closed.

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output bytes
to be written out. The general contract of

flush

is
that calling it is an indication that, if any bytes previously
written have been buffered by the implementation of the output
stream, such bytes should immediately be written to their
intended destination.

If the intended destination of this stream is an abstraction provided by
the underlying operating system, for example a file, then flushing the
stream guarantees only that bytes previously written to the stream are
passed to the operating system for writing; it does not guarantee that
they are actually written to a physical device such as a disk drive.

The

flush

method of

OutputStream

does nothing.

**Specified by:** flush

in interface

Flushable
**Throws:** IOException

- if an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with this stream. The general contract of

close

is that it closes the output stream. A closed stream cannot perform
output operations and cannot be reopened.

The

close

method of

OutputStream

does nothing.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error occurs.

---

#### Method Detail

nullOutputStream

```java
public static
OutputStream
nullOutputStream()
```

Returns a new

OutputStream

which discards all bytes. The
returned stream is initially open. The stream is closed by calling
the

close()

method. Subsequent calls to

close()

have
no effect.

While the stream is open, the

write(int)

,

write(byte[])

, and

write(byte[], int, int)

methods do nothing.
After the stream has been closed, these methods all throw

IOException

.

The

flush()

method does nothing.

**Returns:** an

OutputStream

which discards all bytes
**Since:** 11

---

#### nullOutputStream

public static

OutputStream

nullOutputStream()

Returns a new

OutputStream

which discards all bytes. The
returned stream is initially open. The stream is closed by calling
the

close()

method. Subsequent calls to

close()

have
no effect.

While the stream is open, the

write(int)

,

write(byte[])

, and

write(byte[], int, int)

methods do nothing.
After the stream has been closed, these methods all throw

IOException

.

The

flush()

method does nothing.

While the stream is open, the

write(int)

,

write(byte[])

, and

write(byte[], int, int)

methods do nothing.
After the stream has been closed, these methods all throw

IOException

.

The

flush()

method does nothing.

The

flush()

method does nothing.

write

```java
public abstract void write​(int b)
throws
IOException
```

Writes the specified byte to this output stream. The general
contract for

write

is that one byte is written
to the output stream. The byte to be written is the eight
low-order bits of the argument

b

. The 24
high-order bits of

b

are ignored.

Subclasses of

OutputStream

must provide an
implementation for this method.

**Parameters:** b

- the

byte

.
**Throws:** IOException

- if an I/O error occurs. In particular,
an

IOException

may be thrown if the
output stream has been closed.

---

#### write

public abstract void write​(int b)
throws

IOException

Writes the specified byte to this output stream. The general
contract for

write

is that one byte is written
to the output stream. The byte to be written is the eight
low-order bits of the argument

b

. The 24
high-order bits of

b

are ignored.

Subclasses of

OutputStream

must provide an
implementation for this method.

Subclasses of

OutputStream

must provide an
implementation for this method.

write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this output stream. The general contract for

write(b)

is that it should have exactly the same effect as the call

write(b, 0, b.length)

.

**Parameters:** b

- the data.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(byte[], int, int)

---

#### write

public void write​(byte[] b)
throws

IOException

Writes

b.length

bytes from the specified byte array
to this output stream. The general contract for

write(b)

is that it should have exactly the same effect as the call

write(b, 0, b.length)

.

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

to this output stream.
The general contract for

write(b, off, len)

is that
some of the bytes in the array

b

are written to the
output stream in order; element

b[off]

is the first
byte written and

b[off+len-1]

is the last byte written
by this operation.

The

write

method of

OutputStream

calls
the write method of one argument on each of the bytes to be
written out. Subclasses are encouraged to override this method and
provide a more efficient implementation.

If

b

is

null

, a

NullPointerException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs. In particular,
an

IOException

is thrown if the output
stream is closed.

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

to this output stream.
The general contract for

write(b, off, len)

is that
some of the bytes in the array

b

are written to the
output stream in order; element

b[off]

is the first
byte written and

b[off+len-1]

is the last byte written
by this operation.

The

write

method of

OutputStream

calls
the write method of one argument on each of the bytes to be
written out. Subclasses are encouraged to override this method and
provide a more efficient implementation.

If

b

is

null

, a

NullPointerException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

The

write

method of

OutputStream

calls
the write method of one argument on each of the bytes to be
written out. Subclasses are encouraged to override this method and
provide a more efficient implementation.

If

b

is

null

, a

NullPointerException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

If

b

is

null

, a

NullPointerException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

If

off

is negative, or

len

is negative, or

off+len

is greater than the length of the array

b

, then an

IndexOutOfBoundsException

is thrown.

flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output bytes
to be written out. The general contract of

flush

is
that calling it is an indication that, if any bytes previously
written have been buffered by the implementation of the output
stream, such bytes should immediately be written to their
intended destination.

If the intended destination of this stream is an abstraction provided by
the underlying operating system, for example a file, then flushing the
stream guarantees only that bytes previously written to the stream are
passed to the operating system for writing; it does not guarantee that
they are actually written to a physical device such as a disk drive.

The

flush

method of

OutputStream

does nothing.

**Specified by:** flush

in interface

Flushable
**Throws:** IOException

- if an I/O error occurs.

---

#### flush

public void flush()
throws

IOException

Flushes this output stream and forces any buffered output bytes
to be written out. The general contract of

flush

is
that calling it is an indication that, if any bytes previously
written have been buffered by the implementation of the output
stream, such bytes should immediately be written to their
intended destination.

If the intended destination of this stream is an abstraction provided by
the underlying operating system, for example a file, then flushing the
stream guarantees only that bytes previously written to the stream are
passed to the operating system for writing; it does not guarantee that
they are actually written to a physical device such as a disk drive.

The

flush

method of

OutputStream

does nothing.

If the intended destination of this stream is an abstraction provided by
the underlying operating system, for example a file, then flushing the
stream guarantees only that bytes previously written to the stream are
passed to the operating system for writing; it does not guarantee that
they are actually written to a physical device such as a disk drive.

The

flush

method of

OutputStream

does nothing.

The

flush

method of

OutputStream

does nothing.

close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with this stream. The general contract of

close

is that it closes the output stream. A closed stream cannot perform
output operations and cannot be reopened.

The

close

method of

OutputStream

does nothing.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error occurs.

---

#### close

public void close()
throws

IOException

Closes this output stream and releases any system resources
associated with this stream. The general contract of

close

is that it closes the output stream. A closed stream cannot perform
output operations and cannot be reopened.

The

close

method of

OutputStream

does nothing.

The

close

method of

OutputStream

does nothing.

---

