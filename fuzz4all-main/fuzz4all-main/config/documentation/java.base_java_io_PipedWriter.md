# Class PipedWriter

**Source:** `java.base\java\io\PipedWriter.html`

### Class Description

```java
public class
PipedWriter

extends
Writer
```

Piped character-output streams.

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PipedWriter​(
PipedReader
snk)
throws
IOException

Creates a piped writer connected to the specified piped
reader. Data characters written to this stream will then be
available as input from

snk

.

**Parameters:**
- snk

- The piped reader to connect to.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public PipedWriter()

Creates a piped writer that is not yet connected to a
piped reader. It must be connected to a piped reader,
either by the receiver or the sender, before being used.

**See Also:**
- PipedReader.connect(java.io.PipedWriter)

,

connect(java.io.PipedReader)

---

### Method Details

#### public void connect​(
PipedReader
snk)
throws
IOException

Connects this piped writer to a receiver. If this object
is already connected to some other piped reader, an

IOException

is thrown.

If

snk

is an unconnected piped reader and

src

is an unconnected piped writer, they may
be connected by either the call:

```java
src.connect(snk)
```

or the call:

```java
snk.connect(src)
```

The two calls have the same effect.

**Parameters:**
- snk

- the piped reader to connect to.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public void write​(int c)
throws
IOException

Writes the specified

char

to the piped output stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

Implements the

write

method of

Writer

.

**Overrides:**
- write

in class

Writer

**Parameters:**
- c

- the

char

to be written.

**Throws:**
- IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

---

#### public void write​(char[] cbuf,
int off,
int len)
throws
IOException

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.
This method blocks until all the characters are written to the output
stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

**Specified by:**
- write

in class

Writer

**Parameters:**
- cbuf

- the data.
- off

- the start offset in the data.
- len

- the number of characters to write.

**Throws:**
- IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
- IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

---

#### public void flush()
throws
IOException

Flushes this output stream and forces any buffered output characters
to be written out.
This will notify any readers that characters are waiting in the pipe.

**Specified by:**
- flush

in interface

Flushable
- flush

in class

Writer

**Throws:**
- IOException

- if the pipe is closed, or an I/O error occurs.

---

#### public void close()
throws
IOException

Closes this piped output stream and releases any system resources
associated with this stream. This stream may no longer be used for
writing characters.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable
- close

in class

Writer

**Throws:**
- IOException

- if an I/O error occurs.

---

### Additional Sections

#### Class PipedWriter

java.lang.Object

- java.io.Writer
- - java.io.PipedWriter

java.io.Writer

- java.io.PipedWriter

java.io.PipedWriter

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

```java
public class
PipedWriter

extends
Writer
```

Piped character-output streams.

**Since:** 1.1

public class

PipedWriter

extends

Writer

Piped character-output streams.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

Writer

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PipedWriter

()

Creates a piped writer that is not yet connected to a
piped reader.

PipedWriter

​(

PipedReader

snk)

Creates a piped writer connected to the specified piped
reader.

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

Closes this piped output stream and releases any system resources
associated with this stream.

void

connect

​(

PipedReader

snk)

Connects this piped writer to a receiver.

void

flush

()

Flushes this output stream and forces any buffered output characters
to be written out.

void

write

​(char[] cbuf,
int off,
int len)

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.

void

write

​(int c)

Writes the specified

char

to the piped output stream.

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

nullWriter

,

write

,

write

,

write

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

- Fields declared in class java.io.

Writer

lock

---

#### Field Summary

Fields declared in class java.io.

Writer

lock

---

#### Fields declared in class java.io. Writer

Constructor Summary

Constructors

Constructor

Description

PipedWriter

()

Creates a piped writer that is not yet connected to a
piped reader.

PipedWriter

​(

PipedReader

snk)

Creates a piped writer connected to the specified piped
reader.

---

#### Constructor Summary

Creates a piped writer that is not yet connected to a
piped reader.

Creates a piped writer connected to the specified piped
reader.

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

Closes this piped output stream and releases any system resources
associated with this stream.

void

connect

​(

PipedReader

snk)

Connects this piped writer to a receiver.

void

flush

()

Flushes this output stream and forces any buffered output characters
to be written out.

void

write

​(char[] cbuf,
int off,
int len)

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.

void

write

​(int c)

Writes the specified

char

to the piped output stream.

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

nullWriter

,

write

,

write

,

write

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

Closes this piped output stream and releases any system resources
associated with this stream.

Connects this piped writer to a receiver.

Flushes this output stream and forces any buffered output characters
to be written out.

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.

Writes the specified

char

to the piped output stream.

Methods declared in class java.io.

Writer

append

,

append

,

append

,

nullWriter

,

write

,

write

,

write

---

#### Methods declared in class java.io. Writer

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

- PipedWriter

```java
public PipedWriter​(
PipedReader
snk)
throws
IOException
```

Creates a piped writer connected to the specified piped
reader. Data characters written to this stream will then be
available as input from

snk

.

**Parameters:** snk

- The piped reader to connect to.
**Throws:** IOException

- if an I/O error occurs.

- PipedWriter

```java
public PipedWriter()
```

Creates a piped writer that is not yet connected to a
piped reader. It must be connected to a piped reader,
either by the receiver or the sender, before being used.

**See Also:** PipedReader.connect(java.io.PipedWriter)

,

connect(java.io.PipedReader)

============ METHOD DETAIL ==========

- Method Detail

- connect

```java
public void connect​(
PipedReader
snk)
throws
IOException
```

Connects this piped writer to a receiver. If this object
is already connected to some other piped reader, an

IOException

is thrown.

If

snk

is an unconnected piped reader and

src

is an unconnected piped writer, they may
be connected by either the call:

```java
src.connect(snk)
```

or the call:

```java
snk.connect(src)
```

The two calls have the same effect.

**Parameters:** snk

- the piped reader to connect to.
**Throws:** IOException

- if an I/O error occurs.

- write

```java
public void write​(int c)
throws
IOException
```

Writes the specified

char

to the piped output stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

Implements the

write

method of

Writer

.

**Overrides:** write

in class

Writer
**Parameters:** c

- the

char

to be written.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

- write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.
This method blocks until all the characters are written to the output
stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of characters to write.
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output characters
to be written out.
This will notify any readers that characters are waiting in the pipe.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- if the pipe is closed, or an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this piped output stream and releases any system resources
associated with this stream. This stream may no longer be used for
writing characters.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer
**Throws:** IOException

- if an I/O error occurs.

Constructor Detail

- PipedWriter

```java
public PipedWriter​(
PipedReader
snk)
throws
IOException
```

Creates a piped writer connected to the specified piped
reader. Data characters written to this stream will then be
available as input from

snk

.

**Parameters:** snk

- The piped reader to connect to.
**Throws:** IOException

- if an I/O error occurs.

- PipedWriter

```java
public PipedWriter()
```

Creates a piped writer that is not yet connected to a
piped reader. It must be connected to a piped reader,
either by the receiver or the sender, before being used.

**See Also:** PipedReader.connect(java.io.PipedWriter)

,

connect(java.io.PipedReader)

---

#### Constructor Detail

PipedWriter

```java
public PipedWriter​(
PipedReader
snk)
throws
IOException
```

Creates a piped writer connected to the specified piped
reader. Data characters written to this stream will then be
available as input from

snk

.

**Parameters:** snk

- The piped reader to connect to.
**Throws:** IOException

- if an I/O error occurs.

---

#### PipedWriter

public PipedWriter​(

PipedReader

snk)
throws

IOException

Creates a piped writer connected to the specified piped
reader. Data characters written to this stream will then be
available as input from

snk

.

PipedWriter

```java
public PipedWriter()
```

Creates a piped writer that is not yet connected to a
piped reader. It must be connected to a piped reader,
either by the receiver or the sender, before being used.

**See Also:** PipedReader.connect(java.io.PipedWriter)

,

connect(java.io.PipedReader)

---

#### PipedWriter

public PipedWriter()

Creates a piped writer that is not yet connected to a
piped reader. It must be connected to a piped reader,
either by the receiver or the sender, before being used.

Method Detail

- connect

```java
public void connect​(
PipedReader
snk)
throws
IOException
```

Connects this piped writer to a receiver. If this object
is already connected to some other piped reader, an

IOException

is thrown.

If

snk

is an unconnected piped reader and

src

is an unconnected piped writer, they may
be connected by either the call:

```java
src.connect(snk)
```

or the call:

```java
snk.connect(src)
```

The two calls have the same effect.

**Parameters:** snk

- the piped reader to connect to.
**Throws:** IOException

- if an I/O error occurs.

- write

```java
public void write​(int c)
throws
IOException
```

Writes the specified

char

to the piped output stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

Implements the

write

method of

Writer

.

**Overrides:** write

in class

Writer
**Parameters:** c

- the

char

to be written.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

- write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.
This method blocks until all the characters are written to the output
stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of characters to write.
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output characters
to be written out.
This will notify any readers that characters are waiting in the pipe.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- if the pipe is closed, or an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this piped output stream and releases any system resources
associated with this stream. This stream may no longer be used for
writing characters.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer
**Throws:** IOException

- if an I/O error occurs.

---

#### Method Detail

connect

```java
public void connect​(
PipedReader
snk)
throws
IOException
```

Connects this piped writer to a receiver. If this object
is already connected to some other piped reader, an

IOException

is thrown.

If

snk

is an unconnected piped reader and

src

is an unconnected piped writer, they may
be connected by either the call:

```java
src.connect(snk)
```

or the call:

```java
snk.connect(src)
```

The two calls have the same effect.

**Parameters:** snk

- the piped reader to connect to.
**Throws:** IOException

- if an I/O error occurs.

---

#### connect

public void connect​(

PipedReader

snk)
throws

IOException

Connects this piped writer to a receiver. If this object
is already connected to some other piped reader, an

IOException

is thrown.

If

snk

is an unconnected piped reader and

src

is an unconnected piped writer, they may
be connected by either the call:

```java
src.connect(snk)
```

or the call:

```java
snk.connect(src)
```

The two calls have the same effect.

If

snk

is an unconnected piped reader and

src

is an unconnected piped writer, they may
be connected by either the call:

```java
src.connect(snk)
```

or the call:

```java
snk.connect(src)
```

The two calls have the same effect.

src.connect(snk)

snk.connect(src)

write

```java
public void write​(int c)
throws
IOException
```

Writes the specified

char

to the piped output stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

Implements the

write

method of

Writer

.

**Overrides:** write

in class

Writer
**Parameters:** c

- the

char

to be written.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

---

#### write

public void write​(int c)
throws

IOException

Writes the specified

char

to the piped output stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

Implements the

write

method of

Writer

.

Implements the

write

method of

Writer

.

write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.
This method blocks until all the characters are written to the output
stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of characters to write.
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed
or an I/O error occurs.

---

#### write

public void write​(char[] cbuf,
int off,
int len)
throws

IOException

Writes

len

characters from the specified character array
starting at offset

off

to this piped output stream.
This method blocks until all the characters are written to the output
stream.
If a thread was reading data characters from the connected piped input
stream, but the thread is no longer alive, then an

IOException

is thrown.

flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output characters
to be written out.
This will notify any readers that characters are waiting in the pipe.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- if the pipe is closed, or an I/O error occurs.

---

#### flush

public void flush()
throws

IOException

Flushes this output stream and forces any buffered output characters
to be written out.
This will notify any readers that characters are waiting in the pipe.

close

```java
public void close()
throws
IOException
```

Closes this piped output stream and releases any system resources
associated with this stream. This stream may no longer be used for
writing characters.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer
**Throws:** IOException

- if an I/O error occurs.

---

#### close

public void close()
throws

IOException

Closes this piped output stream and releases any system resources
associated with this stream. This stream may no longer be used for
writing characters.

---

