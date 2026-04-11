# Class PipedReader

**Source:** `java.base\java\io\PipedReader.html`

### Class Description

```java
public class
PipedReader

extends
Reader
```

Piped character-input streams.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PipedReader​(
PipedWriter
src)
throws
IOException

Creates a

PipedReader

so
that it is connected to the piped writer

src

. Data written to

src

will then be available as input from this stream.

**Parameters:**
- src

- the stream to connect to.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public PipedReader​(
PipedWriter
src,
int pipeSize)
throws
IOException

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer. Data written to

src

will then be available as input from this stream.

**Parameters:**
- src

- the stream to connect to.
- pipeSize

- the size of the pipe's buffer.

**Throws:**
- IOException

- if an I/O error occurs.
- IllegalArgumentException

- if

pipeSize <= 0

.

**Since:**
- 1.6

---

#### public PipedReader()

Creates a

PipedReader

so
that it is not yet

connected

. It must be

connected

to a

PipedWriter

before being used.

---

#### public PipedReader​(int pipeSize)

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.
It must be

connected

to a

PipedWriter

before being used.

**Parameters:**
- pipeSize

- the size of the pipe's buffer.

**Throws:**
- IllegalArgumentException

- if

pipeSize <= 0

.

**Since:**
- 1.6

---

### Method Details

#### public void connect​(
PipedWriter
src)
throws
IOException

Causes this piped reader to be connected
to the piped writer

src

.
If this object is already connected to some
other piped writer, an

IOException

is thrown.

If

src

is an
unconnected piped writer and

snk

is an unconnected piped reader, they
may be connected by either the call:

```java
snk.connect(src)
```

or the call:

```java
src.connect(snk)
```

The two calls have the same effect.

**Parameters:**
- src

- The piped writer to connect to.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public int read()
throws
IOException

Reads the next character of data from this piped stream.
If no character is available because the end of the stream
has been reached, the value

-1

is returned.
This method blocks until input data is available, the end of
the stream is detected, or an exception is thrown.

**Overrides:**
- read

in class

Reader

**Returns:**
- the next character of data, or

-1

if the end of the
stream is reached.

**Throws:**
- IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.

---

#### public int read​(char[] cbuf,
int off,
int len)
throws
IOException

Reads up to

len

characters of data from this piped
stream into an array of characters. Less than

len

characters
will be read if the end of the data stream is reached or if

len

exceeds the pipe's buffer size. This method
blocks until at least one character of input is available.

**Specified by:**
- read

in class

Reader

**Parameters:**
- cbuf

- the buffer into which the data is read.
- off

- the start offset of the data.
- len

- the maximum number of characters read.

**Returns:**
- the total number of characters read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.

**Throws:**
- IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.
- IndexOutOfBoundsException

- If an I/O error occurs

---

#### public boolean ready()
throws
IOException

Tell whether this stream is ready to be read. A piped character
stream is ready if the circular buffer is not empty.

**Overrides:**
- ready

in class

Reader

**Returns:**
- True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.

**Throws:**
- IOException

- if the pipe is

broken

,

unconnected

, or closed.

---

#### public void close()
throws
IOException

Closes this piped stream and releases any system resources
associated with the stream.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable
- close

in class

Reader

**Throws:**
- IOException

- if an I/O error occurs.

---

### Additional Sections

#### Class PipedReader

java.lang.Object

- java.io.Reader
- - java.io.PipedReader

java.io.Reader

- java.io.PipedReader

java.io.PipedReader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

```java
public class
PipedReader

extends
Reader
```

Piped character-input streams.

**Since:** 1.1

public class

PipedReader

extends

Reader

Piped character-input streams.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

Reader

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PipedReader

()

Creates a

PipedReader

so
that it is not yet

connected

.

PipedReader

​(int pipeSize)

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.

PipedReader

​(

PipedWriter

src)

Creates a

PipedReader

so
that it is connected to the piped writer

src

.

PipedReader

​(

PipedWriter

src,
int pipeSize)

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer.

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

Closes this piped stream and releases any system resources
associated with the stream.

void

connect

​(

PipedWriter

src)

Causes this piped reader to be connected
to the piped writer

src

.

int

read

()

Reads the next character of data from this piped stream.

int

read

​(char[] cbuf,
int off,
int len)

Reads up to

len

characters of data from this piped
stream into an array of characters.

boolean

ready

()

Tell whether this stream is ready to be read.

- Methods declared in class java.io.

Reader

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

,

transferTo

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

Reader

lock

---

#### Field Summary

Fields declared in class java.io.

Reader

lock

---

#### Fields declared in class java.io. Reader

Constructor Summary

Constructors

Constructor

Description

PipedReader

()

Creates a

PipedReader

so
that it is not yet

connected

.

PipedReader

​(int pipeSize)

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.

PipedReader

​(

PipedWriter

src)

Creates a

PipedReader

so
that it is connected to the piped writer

src

.

PipedReader

​(

PipedWriter

src,
int pipeSize)

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer.

---

#### Constructor Summary

Creates a

PipedReader

so
that it is not yet

connected

.

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.

Creates a

PipedReader

so
that it is connected to the piped writer

src

.

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer.

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

Closes this piped stream and releases any system resources
associated with the stream.

void

connect

​(

PipedWriter

src)

Causes this piped reader to be connected
to the piped writer

src

.

int

read

()

Reads the next character of data from this piped stream.

int

read

​(char[] cbuf,
int off,
int len)

Reads up to

len

characters of data from this piped
stream into an array of characters.

boolean

ready

()

Tell whether this stream is ready to be read.

- Methods declared in class java.io.

Reader

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

,

transferTo

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

Closes this piped stream and releases any system resources
associated with the stream.

Causes this piped reader to be connected
to the piped writer

src

.

Reads the next character of data from this piped stream.

Reads up to

len

characters of data from this piped
stream into an array of characters.

Tell whether this stream is ready to be read.

Methods declared in class java.io.

Reader

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

,

transferTo

---

#### Methods declared in class java.io. Reader

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

- PipedReader

```java
public PipedReader​(
PipedWriter
src)
throws
IOException
```

Creates a

PipedReader

so
that it is connected to the piped writer

src

. Data written to

src

will then be available as input from this stream.

**Parameters:** src

- the stream to connect to.
**Throws:** IOException

- if an I/O error occurs.

- PipedReader

```java
public PipedReader​(
PipedWriter
src,
int pipeSize)
throws
IOException
```

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer. Data written to

src

will then be available as input from this stream.

**Parameters:** src

- the stream to connect to.
**Parameters:** pipeSize

- the size of the pipe's buffer.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** IllegalArgumentException

- if

pipeSize <= 0

.
**Since:** 1.6

- PipedReader

```java
public PipedReader()
```

Creates a

PipedReader

so
that it is not yet

connected

. It must be

connected

to a

PipedWriter

before being used.

- PipedReader

```java
public PipedReader​(int pipeSize)
```

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.
It must be

connected

to a

PipedWriter

before being used.

**Parameters:** pipeSize

- the size of the pipe's buffer.
**Throws:** IllegalArgumentException

- if

pipeSize <= 0

.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- connect

```java
public void connect​(
PipedWriter
src)
throws
IOException
```

Causes this piped reader to be connected
to the piped writer

src

.
If this object is already connected to some
other piped writer, an

IOException

is thrown.

If

src

is an
unconnected piped writer and

snk

is an unconnected piped reader, they
may be connected by either the call:

```java
snk.connect(src)
```

or the call:

```java
src.connect(snk)
```

The two calls have the same effect.

**Parameters:** src

- The piped writer to connect to.
**Throws:** IOException

- if an I/O error occurs.

- read

```java
public int read()
throws
IOException
```

Reads the next character of data from this piped stream.
If no character is available because the end of the stream
has been reached, the value

-1

is returned.
This method blocks until input data is available, the end of
the stream is detected, or an exception is thrown.

**Overrides:** read

in class

Reader
**Returns:** the next character of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.

- read

```java
public int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads up to

len

characters of data from this piped
stream into an array of characters. Less than

len

characters
will be read if the end of the data stream is reached or if

len

exceeds the pipe's buffer size. This method
blocks until at least one character of input is available.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- the buffer into which the data is read.
**Parameters:** off

- the start offset of the data.
**Parameters:** len

- the maximum number of characters read.
**Returns:** the total number of characters read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tell whether this stream is ready to be read. A piped character
stream is ready if the circular buffer is not empty.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, or closed.

- close

```java
public void close()
throws
IOException
```

Closes this piped stream and releases any system resources
associated with the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Reader
**Throws:** IOException

- if an I/O error occurs.

Constructor Detail

- PipedReader

```java
public PipedReader​(
PipedWriter
src)
throws
IOException
```

Creates a

PipedReader

so
that it is connected to the piped writer

src

. Data written to

src

will then be available as input from this stream.

**Parameters:** src

- the stream to connect to.
**Throws:** IOException

- if an I/O error occurs.

- PipedReader

```java
public PipedReader​(
PipedWriter
src,
int pipeSize)
throws
IOException
```

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer. Data written to

src

will then be available as input from this stream.

**Parameters:** src

- the stream to connect to.
**Parameters:** pipeSize

- the size of the pipe's buffer.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** IllegalArgumentException

- if

pipeSize <= 0

.
**Since:** 1.6

- PipedReader

```java
public PipedReader()
```

Creates a

PipedReader

so
that it is not yet

connected

. It must be

connected

to a

PipedWriter

before being used.

- PipedReader

```java
public PipedReader​(int pipeSize)
```

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.
It must be

connected

to a

PipedWriter

before being used.

**Parameters:** pipeSize

- the size of the pipe's buffer.
**Throws:** IllegalArgumentException

- if

pipeSize <= 0

.
**Since:** 1.6

---

#### Constructor Detail

PipedReader

```java
public PipedReader​(
PipedWriter
src)
throws
IOException
```

Creates a

PipedReader

so
that it is connected to the piped writer

src

. Data written to

src

will then be available as input from this stream.

**Parameters:** src

- the stream to connect to.
**Throws:** IOException

- if an I/O error occurs.

---

#### PipedReader

public PipedReader​(

PipedWriter

src)
throws

IOException

Creates a

PipedReader

so
that it is connected to the piped writer

src

. Data written to

src

will then be available as input from this stream.

PipedReader

```java
public PipedReader​(
PipedWriter
src,
int pipeSize)
throws
IOException
```

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer. Data written to

src

will then be available as input from this stream.

**Parameters:** src

- the stream to connect to.
**Parameters:** pipeSize

- the size of the pipe's buffer.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** IllegalArgumentException

- if

pipeSize <= 0

.
**Since:** 1.6

---

#### PipedReader

public PipedReader​(

PipedWriter

src,
int pipeSize)
throws

IOException

Creates a

PipedReader

so that it is connected
to the piped writer

src

and uses the specified
pipe size for the pipe's buffer. Data written to

src

will then be available as input from this stream.

PipedReader

```java
public PipedReader()
```

Creates a

PipedReader

so
that it is not yet

connected

. It must be

connected

to a

PipedWriter

before being used.

---

#### PipedReader

public PipedReader()

Creates a

PipedReader

so
that it is not yet

connected

. It must be

connected

to a

PipedWriter

before being used.

PipedReader

```java
public PipedReader​(int pipeSize)
```

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.
It must be

connected

to a

PipedWriter

before being used.

**Parameters:** pipeSize

- the size of the pipe's buffer.
**Throws:** IllegalArgumentException

- if

pipeSize <= 0

.
**Since:** 1.6

---

#### PipedReader

public PipedReader​(int pipeSize)

Creates a

PipedReader

so that it is not yet

connected

and uses
the specified pipe size for the pipe's buffer.
It must be

connected

to a

PipedWriter

before being used.

Method Detail

- connect

```java
public void connect​(
PipedWriter
src)
throws
IOException
```

Causes this piped reader to be connected
to the piped writer

src

.
If this object is already connected to some
other piped writer, an

IOException

is thrown.

If

src

is an
unconnected piped writer and

snk

is an unconnected piped reader, they
may be connected by either the call:

```java
snk.connect(src)
```

or the call:

```java
src.connect(snk)
```

The two calls have the same effect.

**Parameters:** src

- The piped writer to connect to.
**Throws:** IOException

- if an I/O error occurs.

- read

```java
public int read()
throws
IOException
```

Reads the next character of data from this piped stream.
If no character is available because the end of the stream
has been reached, the value

-1

is returned.
This method blocks until input data is available, the end of
the stream is detected, or an exception is thrown.

**Overrides:** read

in class

Reader
**Returns:** the next character of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.

- read

```java
public int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads up to

len

characters of data from this piped
stream into an array of characters. Less than

len

characters
will be read if the end of the data stream is reached or if

len

exceeds the pipe's buffer size. This method
blocks until at least one character of input is available.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- the buffer into which the data is read.
**Parameters:** off

- the start offset of the data.
**Parameters:** len

- the maximum number of characters read.
**Returns:** the total number of characters read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tell whether this stream is ready to be read. A piped character
stream is ready if the circular buffer is not empty.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, or closed.

- close

```java
public void close()
throws
IOException
```

Closes this piped stream and releases any system resources
associated with the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Reader
**Throws:** IOException

- if an I/O error occurs.

---

#### Method Detail

connect

```java
public void connect​(
PipedWriter
src)
throws
IOException
```

Causes this piped reader to be connected
to the piped writer

src

.
If this object is already connected to some
other piped writer, an

IOException

is thrown.

If

src

is an
unconnected piped writer and

snk

is an unconnected piped reader, they
may be connected by either the call:

```java
snk.connect(src)
```

or the call:

```java
src.connect(snk)
```

The two calls have the same effect.

**Parameters:** src

- The piped writer to connect to.
**Throws:** IOException

- if an I/O error occurs.

---

#### connect

public void connect​(

PipedWriter

src)
throws

IOException

Causes this piped reader to be connected
to the piped writer

src

.
If this object is already connected to some
other piped writer, an

IOException

is thrown.

If

src

is an
unconnected piped writer and

snk

is an unconnected piped reader, they
may be connected by either the call:

```java
snk.connect(src)
```

or the call:

```java
src.connect(snk)
```

The two calls have the same effect.

If

src

is an
unconnected piped writer and

snk

is an unconnected piped reader, they
may be connected by either the call:

```java
snk.connect(src)
```

or the call:

```java
src.connect(snk)
```

The two calls have the same effect.

snk.connect(src)

or the call:

```java
src.connect(snk)
```

The two calls have the same effect.

src.connect(snk)

The two calls have the same effect.

read

```java
public int read()
throws
IOException
```

Reads the next character of data from this piped stream.
If no character is available because the end of the stream
has been reached, the value

-1

is returned.
This method blocks until input data is available, the end of
the stream is detected, or an exception is thrown.

**Overrides:** read

in class

Reader
**Returns:** the next character of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.

---

#### read

public int read()
throws

IOException

Reads the next character of data from this piped stream.
If no character is available because the end of the stream
has been reached, the value

-1

is returned.
This method blocks until input data is available, the end of
the stream is detected, or an exception is thrown.

read

```java
public int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads up to

len

characters of data from this piped
stream into an array of characters. Less than

len

characters
will be read if the end of the data stream is reached or if

len

exceeds the pipe's buffer size. This method
blocks until at least one character of input is available.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- the buffer into which the data is read.
**Parameters:** off

- the start offset of the data.
**Parameters:** len

- the maximum number of characters read.
**Returns:** the total number of characters read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, closed,
or an I/O error occurs.
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

---

#### read

public int read​(char[] cbuf,
int off,
int len)
throws

IOException

Reads up to

len

characters of data from this piped
stream into an array of characters. Less than

len

characters
will be read if the end of the data stream is reached or if

len

exceeds the pipe's buffer size. This method
blocks until at least one character of input is available.

ready

```java
public boolean ready()
throws
IOException
```

Tell whether this stream is ready to be read. A piped character
stream is ready if the circular buffer is not empty.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- if the pipe is

broken

,

unconnected

, or closed.

---

#### ready

public boolean ready()
throws

IOException

Tell whether this stream is ready to be read. A piped character
stream is ready if the circular buffer is not empty.

close

```java
public void close()
throws
IOException
```

Closes this piped stream and releases any system resources
associated with the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Reader
**Throws:** IOException

- if an I/O error occurs.

---

#### close

public void close()
throws

IOException

Closes this piped stream and releases any system resources
associated with the stream.

---

