# Class DeflaterInputStream

**Source:** `java.base\java\util\zip\DeflaterInputStream.html`

### Class Description

```java
public class
DeflaterInputStream

extends
FilterInputStream
```

Implements an input stream filter for compressing data in the "deflate"
compression format.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

#### protected final
Deflater
def

Compressor for this stream.

---

#### protected final byte[] buf

Input buffer for reading compressed data.

---

### Constructor Details

#### public DeflaterInputStream​(
InputStream
in)

Creates a new input stream with a default compressor and buffer
size.

**Parameters:**
- in

- input stream to read the uncompressed data to

**Throws:**
- NullPointerException

- if

in

is null

---

#### public DeflaterInputStream​(
InputStream
in,

Deflater
defl)

Creates a new input stream with the specified compressor and a
default buffer size.

**Parameters:**
- in

- input stream to read the uncompressed data to
- defl

- compressor ("deflater") for this stream

**Throws:**
- NullPointerException

- if

in

or

defl

is null

---

#### public DeflaterInputStream​(
InputStream
in,

Deflater
defl,
int bufLen)

Creates a new input stream with the specified compressor and buffer
size.

**Parameters:**
- in

- input stream to read the uncompressed data to
- defl

- compressor ("deflater") for this stream
- bufLen

- compression buffer size

**Throws:**
- IllegalArgumentException

- if

bufLen <= 0
- NullPointerException

- if

in

or

defl

is null

---

### Method Details

#### public void close()
throws
IOException

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

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

FilterInputStream

**Throws:**
- IOException

- if an I/O error occurs

**See Also:**
- FilterInputStream.in

---

#### public int read()
throws
IOException

Reads a single byte of compressed data from the input stream.
This method will block until some input can be read and compressed.

**Overrides:**
- read

in class

FilterInputStream

**Returns:**
- a single byte of compressed data, or -1 if the end of the
uncompressed input stream is reached

**Throws:**
- IOException

- if an I/O error occurs or if this stream is
already closed

**See Also:**
- FilterInputStream.in

---

#### public int read​(byte[] b,
int off,
int len)
throws
IOException

Reads compressed data into a byte array.
This method will block until some input can be read and compressed.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- b

- buffer into which the data is read
- off

- starting offset of the data within

b
- len

- maximum number of compressed bytes to read into

b

**Returns:**
- the actual number of bytes read, or -1 if the end of the
uncompressed input stream is reached

**Throws:**
- IndexOutOfBoundsException

- if

len > b.length - off
- IOException

- if an I/O error occurs or if this input stream is
already closed

**See Also:**
- FilterInputStream.in

---

#### public long skip​(long n)
throws
IOException

Skips over and discards data from the input stream.
This method may block until the specified number of bytes are read and
skipped.

Note:

While

n

is given as a

long

,
the maximum number of bytes which can be skipped is

Integer.MAX_VALUE

.

**Overrides:**
- skip

in class

FilterInputStream

**Parameters:**
- n

- number of bytes to be skipped

**Returns:**
- the actual number of bytes skipped

**Throws:**
- IOException

- if an I/O error occurs or if this stream is
already closed

---

#### public int available()
throws
IOException

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking

**Overrides:**
- available

in class

FilterInputStream

**Returns:**
- zero after the end of the underlying input stream has been
reached, otherwise always returns 1

**Throws:**
- IOException

- if an I/O error occurs or if this stream is
already closed

---

#### public boolean markSupported()

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

**Overrides:**
- markSupported

in class

FilterInputStream

**Returns:**
- false, always

**See Also:**
- FilterInputStream.in

,

InputStream.mark(int)

,

InputStream.reset()

---

#### public void mark​(int limit)

This operation is not supported

.

**Overrides:**
- mark

in class

FilterInputStream

**Parameters:**
- limit

- maximum bytes that can be read before invalidating the position marker

**See Also:**
- FilterInputStream.in

,

FilterInputStream.reset()

---

#### public void reset()
throws
IOException

This operation is not supported

.

**Overrides:**
- reset

in class

FilterInputStream

**Throws:**
- IOException

- always thrown

**See Also:**
- FilterInputStream.in

,

FilterInputStream.mark(int)

---

### Additional Sections

#### Class DeflaterInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - java.util.zip.DeflaterInputStream

java.io.InputStream

- java.io.FilterInputStream
- - java.util.zip.DeflaterInputStream

java.io.FilterInputStream

- java.util.zip.DeflaterInputStream

java.util.zip.DeflaterInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
DeflaterInputStream

extends
FilterInputStream
```

Implements an input stream filter for compressing data in the "deflate"
compression format.

**Since:** 1.6
**See Also:** DeflaterOutputStream

,

InflaterOutputStream

,

InflaterInputStream

public class

DeflaterInputStream

extends

FilterInputStream

Implements an input stream filter for compressing data in the "deflate"
compression format.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

buf

Input buffer for reading compressed data.

protected

Deflater

def

Compressor for this stream.

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DeflaterInputStream

​(

InputStream

in)

Creates a new input stream with a default compressor and buffer
size.

DeflaterInputStream

​(

InputStream

in,

Deflater

defl)

Creates a new input stream with the specified compressor and a
default buffer size.

DeflaterInputStream

​(

InputStream

in,

Deflater

defl,
int bufLen)

Creates a new input stream with the specified compressor and buffer
size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

available

()

Returns 0 after EOF has been reached, otherwise always return 1.

void

close

()

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

void

mark

​(int limit)

This operation is not supported

.

boolean

markSupported

()

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

int

read

()

Reads a single byte of compressed data from the input stream.

int

read

​(byte[] b,
int off,
int len)

Reads compressed data into a byte array.

void

reset

()

This operation is not supported

.

long

skip

​(long n)

Skips over and discards data from the input stream.

- Methods declared in class java.io.

FilterInputStream

read

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

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

Fields

Modifier and Type

Field

Description

protected byte[]

buf

Input buffer for reading compressed data.

protected

Deflater

def

Compressor for this stream.

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

Input buffer for reading compressed data.

Compressor for this stream.

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Constructor

Description

DeflaterInputStream

​(

InputStream

in)

Creates a new input stream with a default compressor and buffer
size.

DeflaterInputStream

​(

InputStream

in,

Deflater

defl)

Creates a new input stream with the specified compressor and a
default buffer size.

DeflaterInputStream

​(

InputStream

in,

Deflater

defl,
int bufLen)

Creates a new input stream with the specified compressor and buffer
size.

---

#### Constructor Summary

Creates a new input stream with a default compressor and buffer
size.

Creates a new input stream with the specified compressor and a
default buffer size.

Creates a new input stream with the specified compressor and buffer
size.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

available

()

Returns 0 after EOF has been reached, otherwise always return 1.

void

close

()

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

void

mark

​(int limit)

This operation is not supported

.

boolean

markSupported

()

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

int

read

()

Reads a single byte of compressed data from the input stream.

int

read

​(byte[] b,
int off,
int len)

Reads compressed data into a byte array.

void

reset

()

This operation is not supported

.

long

skip

​(long n)

Skips over and discards data from the input stream.

- Methods declared in class java.io.

FilterInputStream

read

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

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

Returns 0 after EOF has been reached, otherwise always return 1.

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

This operation is not supported

.

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

Reads a single byte of compressed data from the input stream.

Reads compressed data into a byte array.

Skips over and discards data from the input stream.

Methods declared in class java.io.

FilterInputStream

read

---

#### Methods declared in class java.io. FilterInputStream

Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

---

#### Methods declared in class java.io. InputStream

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

- def

```java
protected final
Deflater
def
```

Compressor for this stream.

- buf

```java
protected final byte[] buf
```

Input buffer for reading compressed data.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in)
```

Creates a new input stream with a default compressor and buffer
size.

**Parameters:** in

- input stream to read the uncompressed data to
**Throws:** NullPointerException

- if

in

is null

- DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in,

Deflater
defl)
```

Creates a new input stream with the specified compressor and a
default buffer size.

**Parameters:** in

- input stream to read the uncompressed data to
**Parameters:** defl

- compressor ("deflater") for this stream
**Throws:** NullPointerException

- if

in

or

defl

is null

- DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in,

Deflater
defl,
int bufLen)
```

Creates a new input stream with the specified compressor and buffer
size.

**Parameters:** in

- input stream to read the uncompressed data to
**Parameters:** defl

- compressor ("deflater") for this stream
**Parameters:** bufLen

- compression buffer size
**Throws:** IllegalArgumentException

- if

bufLen <= 0
**Throws:** NullPointerException

- if

in

or

defl

is null

============ METHOD DETAIL ==========

- Method Detail

- close

```java
public void close()
throws
IOException
```

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs
**See Also:** FilterInputStream.in

- read

```java
public int read()
throws
IOException
```

Reads a single byte of compressed data from the input stream.
This method will block until some input can be read and compressed.

**Overrides:** read

in class

FilterInputStream
**Returns:** a single byte of compressed data, or -1 if the end of the
uncompressed input stream is reached
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads compressed data into a byte array.
This method will block until some input can be read and compressed.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- buffer into which the data is read
**Parameters:** off

- starting offset of the data within

b
**Parameters:** len

- maximum number of compressed bytes to read into

b
**Returns:** the actual number of bytes read, or -1 if the end of the
uncompressed input stream is reached
**Throws:** IndexOutOfBoundsException

- if

len > b.length - off
**Throws:** IOException

- if an I/O error occurs or if this input stream is
already closed
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips over and discards data from the input stream.
This method may block until the specified number of bytes are read and
skipped.

Note:

While

n

is given as a

long

,
the maximum number of bytes which can be skipped is

Integer.MAX_VALUE

.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- number of bytes to be skipped
**Returns:** the actual number of bytes skipped
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed

- available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking

**Overrides:** available

in class

FilterInputStream
**Returns:** zero after the end of the underlying input stream has been
reached, otherwise always returns 1
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed

- markSupported

```java
public boolean markSupported()
```

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** false, always
**See Also:** FilterInputStream.in

,

InputStream.mark(int)

,

InputStream.reset()

- mark

```java
public void mark​(int limit)
```

This operation is not supported

.

**Overrides:** mark

in class

FilterInputStream
**Parameters:** limit

- maximum bytes that can be read before invalidating the position marker
**See Also:** FilterInputStream.in

,

FilterInputStream.reset()

- reset

```java
public void reset()
throws
IOException
```

This operation is not supported

.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- always thrown
**See Also:** FilterInputStream.in

,

FilterInputStream.mark(int)

Field Detail

- def

```java
protected final
Deflater
def
```

Compressor for this stream.

- buf

```java
protected final byte[] buf
```

Input buffer for reading compressed data.

---

#### Field Detail

def

```java
protected final
Deflater
def
```

Compressor for this stream.

---

#### def

protected final

Deflater

def

Compressor for this stream.

buf

```java
protected final byte[] buf
```

Input buffer for reading compressed data.

---

#### buf

protected final byte[] buf

Input buffer for reading compressed data.

Constructor Detail

- DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in)
```

Creates a new input stream with a default compressor and buffer
size.

**Parameters:** in

- input stream to read the uncompressed data to
**Throws:** NullPointerException

- if

in

is null

- DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in,

Deflater
defl)
```

Creates a new input stream with the specified compressor and a
default buffer size.

**Parameters:** in

- input stream to read the uncompressed data to
**Parameters:** defl

- compressor ("deflater") for this stream
**Throws:** NullPointerException

- if

in

or

defl

is null

- DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in,

Deflater
defl,
int bufLen)
```

Creates a new input stream with the specified compressor and buffer
size.

**Parameters:** in

- input stream to read the uncompressed data to
**Parameters:** defl

- compressor ("deflater") for this stream
**Parameters:** bufLen

- compression buffer size
**Throws:** IllegalArgumentException

- if

bufLen <= 0
**Throws:** NullPointerException

- if

in

or

defl

is null

---

#### Constructor Detail

DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in)
```

Creates a new input stream with a default compressor and buffer
size.

**Parameters:** in

- input stream to read the uncompressed data to
**Throws:** NullPointerException

- if

in

is null

---

#### DeflaterInputStream

public DeflaterInputStream​(

InputStream

in)

Creates a new input stream with a default compressor and buffer
size.

DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in,

Deflater
defl)
```

Creates a new input stream with the specified compressor and a
default buffer size.

**Parameters:** in

- input stream to read the uncompressed data to
**Parameters:** defl

- compressor ("deflater") for this stream
**Throws:** NullPointerException

- if

in

or

defl

is null

---

#### DeflaterInputStream

public DeflaterInputStream​(

InputStream

in,

Deflater

defl)

Creates a new input stream with the specified compressor and a
default buffer size.

DeflaterInputStream

```java
public DeflaterInputStream​(
InputStream
in,

Deflater
defl,
int bufLen)
```

Creates a new input stream with the specified compressor and buffer
size.

**Parameters:** in

- input stream to read the uncompressed data to
**Parameters:** defl

- compressor ("deflater") for this stream
**Parameters:** bufLen

- compression buffer size
**Throws:** IllegalArgumentException

- if

bufLen <= 0
**Throws:** NullPointerException

- if

in

or

defl

is null

---

#### DeflaterInputStream

public DeflaterInputStream​(

InputStream

in,

Deflater

defl,
int bufLen)

Creates a new input stream with the specified compressor and buffer
size.

Method Detail

- close

```java
public void close()
throws
IOException
```

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs
**See Also:** FilterInputStream.in

- read

```java
public int read()
throws
IOException
```

Reads a single byte of compressed data from the input stream.
This method will block until some input can be read and compressed.

**Overrides:** read

in class

FilterInputStream
**Returns:** a single byte of compressed data, or -1 if the end of the
uncompressed input stream is reached
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads compressed data into a byte array.
This method will block until some input can be read and compressed.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- buffer into which the data is read
**Parameters:** off

- starting offset of the data within

b
**Parameters:** len

- maximum number of compressed bytes to read into

b
**Returns:** the actual number of bytes read, or -1 if the end of the
uncompressed input stream is reached
**Throws:** IndexOutOfBoundsException

- if

len > b.length - off
**Throws:** IOException

- if an I/O error occurs or if this input stream is
already closed
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips over and discards data from the input stream.
This method may block until the specified number of bytes are read and
skipped.

Note:

While

n

is given as a

long

,
the maximum number of bytes which can be skipped is

Integer.MAX_VALUE

.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- number of bytes to be skipped
**Returns:** the actual number of bytes skipped
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed

- available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking

**Overrides:** available

in class

FilterInputStream
**Returns:** zero after the end of the underlying input stream has been
reached, otherwise always returns 1
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed

- markSupported

```java
public boolean markSupported()
```

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** false, always
**See Also:** FilterInputStream.in

,

InputStream.mark(int)

,

InputStream.reset()

- mark

```java
public void mark​(int limit)
```

This operation is not supported

.

**Overrides:** mark

in class

FilterInputStream
**Parameters:** limit

- maximum bytes that can be read before invalidating the position marker
**See Also:** FilterInputStream.in

,

FilterInputStream.reset()

- reset

```java
public void reset()
throws
IOException
```

This operation is not supported

.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- always thrown
**See Also:** FilterInputStream.in

,

FilterInputStream.mark(int)

---

#### Method Detail

close

```java
public void close()
throws
IOException
```

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs
**See Also:** FilterInputStream.in

---

#### close

public void close()
throws

IOException

Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.

read

```java
public int read()
throws
IOException
```

Reads a single byte of compressed data from the input stream.
This method will block until some input can be read and compressed.

**Overrides:** read

in class

FilterInputStream
**Returns:** a single byte of compressed data, or -1 if the end of the
uncompressed input stream is reached
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed
**See Also:** FilterInputStream.in

---

#### read

public int read()
throws

IOException

Reads a single byte of compressed data from the input stream.
This method will block until some input can be read and compressed.

read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads compressed data into a byte array.
This method will block until some input can be read and compressed.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- buffer into which the data is read
**Parameters:** off

- starting offset of the data within

b
**Parameters:** len

- maximum number of compressed bytes to read into

b
**Returns:** the actual number of bytes read, or -1 if the end of the
uncompressed input stream is reached
**Throws:** IndexOutOfBoundsException

- if

len > b.length - off
**Throws:** IOException

- if an I/O error occurs or if this input stream is
already closed
**See Also:** FilterInputStream.in

---

#### read

public int read​(byte[] b,
int off,
int len)
throws

IOException

Reads compressed data into a byte array.
This method will block until some input can be read and compressed.

skip

```java
public long skip​(long n)
throws
IOException
```

Skips over and discards data from the input stream.
This method may block until the specified number of bytes are read and
skipped.

Note:

While

n

is given as a

long

,
the maximum number of bytes which can be skipped is

Integer.MAX_VALUE

.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- number of bytes to be skipped
**Returns:** the actual number of bytes skipped
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed

---

#### skip

public long skip​(long n)
throws

IOException

Skips over and discards data from the input stream.
This method may block until the specified number of bytes are read and
skipped.

Note:

While

n

is given as a

long

,
the maximum number of bytes which can be skipped is

Integer.MAX_VALUE

.

available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking

**Overrides:** available

in class

FilterInputStream
**Returns:** zero after the end of the underlying input stream has been
reached, otherwise always returns 1
**Throws:** IOException

- if an I/O error occurs or if this stream is
already closed

---

#### available

public int available()
throws

IOException

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking

Programs should not count on this method to return the actual number
of bytes that could be read without blocking

markSupported

```java
public boolean markSupported()
```

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** false, always
**See Also:** FilterInputStream.in

,

InputStream.mark(int)

,

InputStream.reset()

---

#### markSupported

public boolean markSupported()

Always returns

false

because this input stream does not support
the

mark()

and

reset()

methods.

mark

```java
public void mark​(int limit)
```

This operation is not supported

.

**Overrides:** mark

in class

FilterInputStream
**Parameters:** limit

- maximum bytes that can be read before invalidating the position marker
**See Also:** FilterInputStream.in

,

FilterInputStream.reset()

---

#### mark

public void mark​(int limit)

This operation is not supported

.

reset

```java
public void reset()
throws
IOException
```

This operation is not supported

.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- always thrown
**See Also:** FilterInputStream.in

,

FilterInputStream.mark(int)

---

#### reset

public void reset()
throws

IOException

This operation is not supported

.

---

