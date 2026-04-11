# Class InflaterInputStream

**Source:** `java.base\java\util\zip\InflaterInputStream.html`

### Class Description

```java
public class
InflaterInputStream

extends
FilterInputStream
```

This class implements a stream filter for uncompressing data in the
"deflate" compression format. It is also used as the basis for other
decompression filters, such as GZIPInputStream.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

#### protected
Inflater
inf

Decompressor for this stream.

---

#### protected byte[] buf

Input buffer for decompression.

---

#### protected int len

Length of input buffer.

---

### Constructor Details

#### public InflaterInputStream​(
InputStream
in,

Inflater
inf,
int size)

Creates a new input stream with the specified decompressor and
buffer size.

**Parameters:**
- in

- the input stream
- inf

- the decompressor ("inflater")
- size

- the input buffer size

**Throws:**
- IllegalArgumentException

- if

size <= 0

---

#### public InflaterInputStream​(
InputStream
in,

Inflater
inf)

Creates a new input stream with the specified decompressor and a
default buffer size.

**Parameters:**
- in

- the input stream
- inf

- the decompressor ("inflater")

---

#### public InflaterInputStream​(
InputStream
in)

Creates a new input stream with a default decompressor and buffer size.

**Parameters:**
- in

- the input stream

---

### Method Details

#### public int read()
throws
IOException

Reads a byte of uncompressed data. This method will block until
enough input is available for decompression.

**Overrides:**
- read

in class

FilterInputStream

**Returns:**
- the byte read, or -1 if end of compressed input is reached

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

#### public int read​(byte[] b,
int off,
int len)
throws
IOException

Reads uncompressed data into an array of bytes. If

len

is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and

0

is returned.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- b

- the buffer into which the data is read
- off

- the start offset in the destination array

b
- len

- the maximum number of bytes read

**Returns:**
- the actual number of bytes read, or -1 if the end of the
compressed input is reached or a preset dictionary is needed

**Throws:**
- NullPointerException

- If

b

is

null

.
- IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

#### public int available()
throws
IOException

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:**
- available

in class

FilterInputStream

**Returns:**
- 1 before EOF and 0 after EOF.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public long skip​(long n)
throws
IOException

Skips specified number of bytes of uncompressed data.

**Overrides:**
- skip

in class

FilterInputStream

**Parameters:**
- n

- the number of bytes to skip

**Returns:**
- the actual number of bytes skipped.

**Throws:**
- IOException

- if an I/O error has occurred
- IllegalArgumentException

- if

n < 0

---

#### public void close()
throws
IOException

Closes this input stream and releases any system resources associated
with the stream.

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

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

#### protected void fill()
throws
IOException

Fills input buffer with more data to decompress.

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public boolean markSupported()

Tests if this input stream supports the

mark

and

reset

methods. The

markSupported

method of

InflaterInputStream

returns

false

.

**Overrides:**
- markSupported

in class

FilterInputStream

**Returns:**
- a

boolean

indicating if this stream type supports
the

mark

and

reset

methods.

**See Also:**
- InputStream.mark(int)

,

InputStream.reset()

---

#### public void mark​(int readlimit)

Marks the current position in this input stream.

The

mark

method of

InflaterInputStream

does nothing.

**Overrides:**
- mark

in class

FilterInputStream

**Parameters:**
- readlimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.

**See Also:**
- InputStream.reset()

---

#### public void reset()
throws
IOException

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

The method

reset

for class

InflaterInputStream

does nothing except throw an

IOException

.

**Overrides:**
- reset

in class

FilterInputStream

**Throws:**
- IOException

- if this method is invoked.

**See Also:**
- InputStream.mark(int)

,

IOException

---

### Additional Sections

#### Class InflaterInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - java.util.zip.InflaterInputStream

java.io.InputStream

- java.io.FilterInputStream
- - java.util.zip.InflaterInputStream

java.io.FilterInputStream

- java.util.zip.InflaterInputStream

java.util.zip.InflaterInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

**Direct Known Subclasses:** GZIPInputStream

,

ZipInputStream

```java
public class
InflaterInputStream

extends
FilterInputStream
```

This class implements a stream filter for uncompressing data in the
"deflate" compression format. It is also used as the basis for other
decompression filters, such as GZIPInputStream.

**Since:** 1.1
**See Also:** Inflater

public class

InflaterInputStream

extends

FilterInputStream

This class implements a stream filter for uncompressing data in the
"deflate" compression format. It is also used as the basis for other
decompression filters, such as GZIPInputStream.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

buf

Input buffer for decompression.

protected

Inflater

inf

Decompressor for this stream.

protected int

len

Length of input buffer.

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InflaterInputStream

​(

InputStream

in)

Creates a new input stream with a default decompressor and buffer size.

InflaterInputStream

​(

InputStream

in,

Inflater

inf)

Creates a new input stream with the specified decompressor and a
default buffer size.

InflaterInputStream

​(

InputStream

in,

Inflater

inf,
int size)

Creates a new input stream with the specified decompressor and
buffer size.

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

Closes this input stream and releases any system resources associated
with the stream.

protected void

fill

()

Fills input buffer with more data to decompress.

void

mark

​(int readlimit)

Marks the current position in this input stream.

boolean

markSupported

()

Tests if this input stream supports the

mark

and

reset

methods.

int

read

()

Reads a byte of uncompressed data.

int

read

​(byte[] b,
int off,
int len)

Reads uncompressed data into an array of bytes.

void

reset

()

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

long

skip

​(long n)

Skips specified number of bytes of uncompressed data.

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

Input buffer for decompression.

protected

Inflater

inf

Decompressor for this stream.

protected int

len

Length of input buffer.

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

Input buffer for decompression.

Decompressor for this stream.

Length of input buffer.

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Constructor

Description

InflaterInputStream

​(

InputStream

in)

Creates a new input stream with a default decompressor and buffer size.

InflaterInputStream

​(

InputStream

in,

Inflater

inf)

Creates a new input stream with the specified decompressor and a
default buffer size.

InflaterInputStream

​(

InputStream

in,

Inflater

inf,
int size)

Creates a new input stream with the specified decompressor and
buffer size.

---

#### Constructor Summary

Creates a new input stream with a default decompressor and buffer size.

Creates a new input stream with the specified decompressor and a
default buffer size.

Creates a new input stream with the specified decompressor and
buffer size.

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

Closes this input stream and releases any system resources associated
with the stream.

protected void

fill

()

Fills input buffer with more data to decompress.

void

mark

​(int readlimit)

Marks the current position in this input stream.

boolean

markSupported

()

Tests if this input stream supports the

mark

and

reset

methods.

int

read

()

Reads a byte of uncompressed data.

int

read

​(byte[] b,
int off,
int len)

Reads uncompressed data into an array of bytes.

void

reset

()

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

long

skip

​(long n)

Skips specified number of bytes of uncompressed data.

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

Closes this input stream and releases any system resources associated
with the stream.

Fills input buffer with more data to decompress.

Marks the current position in this input stream.

Tests if this input stream supports the

mark

and

reset

methods.

Reads a byte of uncompressed data.

Reads uncompressed data into an array of bytes.

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

Skips specified number of bytes of uncompressed data.

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

- inf

```java
protected
Inflater
inf
```

Decompressor for this stream.

- buf

```java
protected byte[] buf
```

Input buffer for decompression.

- len

```java
protected int len
```

Length of input buffer.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in,

Inflater
inf,
int size)
```

Creates a new input stream with the specified decompressor and
buffer size.

**Parameters:** in

- the input stream
**Parameters:** inf

- the decompressor ("inflater")
**Parameters:** size

- the input buffer size
**Throws:** IllegalArgumentException

- if

size <= 0

- InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in,

Inflater
inf)
```

Creates a new input stream with the specified decompressor and a
default buffer size.

**Parameters:** in

- the input stream
**Parameters:** inf

- the decompressor ("inflater")

- InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in)
```

Creates a new input stream with a default decompressor and buffer size.

**Parameters:** in

- the input stream

============ METHOD DETAIL ==========

- Method Detail

- read

```java
public int read()
throws
IOException
```

Reads a byte of uncompressed data. This method will block until
enough input is available for decompression.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read, or -1 if end of compressed input is reached
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads uncompressed data into an array of bytes. If

len

is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and

0

is returned.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
compressed input is reached or a preset dictionary is needed
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:** available

in class

FilterInputStream
**Returns:** 1 before EOF and 0 after EOF.
**Throws:** IOException

- if an I/O error occurs.

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes of uncompressed data.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

n < 0

- close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources associated
with the stream.

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

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- fill

```java
protected void fill()
throws
IOException
```

Fills input buffer with more data to decompress.

**Throws:** IOException

- if an I/O error has occurred

- markSupported

```java
public boolean markSupported()
```

Tests if this input stream supports the

mark

and

reset

methods. The

markSupported

method of

InflaterInputStream

returns

false

.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** a

boolean

indicating if this stream type supports
the

mark

and

reset

methods.
**See Also:** InputStream.mark(int)

,

InputStream.reset()

- mark

```java
public void mark​(int readlimit)
```

Marks the current position in this input stream.

The

mark

method of

InflaterInputStream

does nothing.

**Overrides:** mark

in class

FilterInputStream
**Parameters:** readlimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.
**See Also:** InputStream.reset()

- reset

```java
public void reset()
throws
IOException
```

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

The method

reset

for class

InflaterInputStream

does nothing except throw an

IOException

.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- if this method is invoked.
**See Also:** InputStream.mark(int)

,

IOException

Field Detail

- inf

```java
protected
Inflater
inf
```

Decompressor for this stream.

- buf

```java
protected byte[] buf
```

Input buffer for decompression.

- len

```java
protected int len
```

Length of input buffer.

---

#### Field Detail

inf

```java
protected
Inflater
inf
```

Decompressor for this stream.

---

#### inf

protected

Inflater

inf

Decompressor for this stream.

buf

```java
protected byte[] buf
```

Input buffer for decompression.

---

#### buf

protected byte[] buf

Input buffer for decompression.

len

```java
protected int len
```

Length of input buffer.

---

#### len

protected int len

Length of input buffer.

Constructor Detail

- InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in,

Inflater
inf,
int size)
```

Creates a new input stream with the specified decompressor and
buffer size.

**Parameters:** in

- the input stream
**Parameters:** inf

- the decompressor ("inflater")
**Parameters:** size

- the input buffer size
**Throws:** IllegalArgumentException

- if

size <= 0

- InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in,

Inflater
inf)
```

Creates a new input stream with the specified decompressor and a
default buffer size.

**Parameters:** in

- the input stream
**Parameters:** inf

- the decompressor ("inflater")

- InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in)
```

Creates a new input stream with a default decompressor and buffer size.

**Parameters:** in

- the input stream

---

#### Constructor Detail

InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in,

Inflater
inf,
int size)
```

Creates a new input stream with the specified decompressor and
buffer size.

**Parameters:** in

- the input stream
**Parameters:** inf

- the decompressor ("inflater")
**Parameters:** size

- the input buffer size
**Throws:** IllegalArgumentException

- if

size <= 0

---

#### InflaterInputStream

public InflaterInputStream​(

InputStream

in,

Inflater

inf,
int size)

Creates a new input stream with the specified decompressor and
buffer size.

InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in,

Inflater
inf)
```

Creates a new input stream with the specified decompressor and a
default buffer size.

**Parameters:** in

- the input stream
**Parameters:** inf

- the decompressor ("inflater")

---

#### InflaterInputStream

public InflaterInputStream​(

InputStream

in,

Inflater

inf)

Creates a new input stream with the specified decompressor and a
default buffer size.

InflaterInputStream

```java
public InflaterInputStream​(
InputStream
in)
```

Creates a new input stream with a default decompressor and buffer size.

**Parameters:** in

- the input stream

---

#### InflaterInputStream

public InflaterInputStream​(

InputStream

in)

Creates a new input stream with a default decompressor and buffer size.

Method Detail

- read

```java
public int read()
throws
IOException
```

Reads a byte of uncompressed data. This method will block until
enough input is available for decompression.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read, or -1 if end of compressed input is reached
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads uncompressed data into an array of bytes. If

len

is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and

0

is returned.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
compressed input is reached or a preset dictionary is needed
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:** available

in class

FilterInputStream
**Returns:** 1 before EOF and 0 after EOF.
**Throws:** IOException

- if an I/O error occurs.

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes of uncompressed data.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

n < 0

- close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources associated
with the stream.

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

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- fill

```java
protected void fill()
throws
IOException
```

Fills input buffer with more data to decompress.

**Throws:** IOException

- if an I/O error has occurred

- markSupported

```java
public boolean markSupported()
```

Tests if this input stream supports the

mark

and

reset

methods. The

markSupported

method of

InflaterInputStream

returns

false

.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** a

boolean

indicating if this stream type supports
the

mark

and

reset

methods.
**See Also:** InputStream.mark(int)

,

InputStream.reset()

- mark

```java
public void mark​(int readlimit)
```

Marks the current position in this input stream.

The

mark

method of

InflaterInputStream

does nothing.

**Overrides:** mark

in class

FilterInputStream
**Parameters:** readlimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.
**See Also:** InputStream.reset()

- reset

```java
public void reset()
throws
IOException
```

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

The method

reset

for class

InflaterInputStream

does nothing except throw an

IOException

.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- if this method is invoked.
**See Also:** InputStream.mark(int)

,

IOException

---

#### Method Detail

read

```java
public int read()
throws
IOException
```

Reads a byte of uncompressed data. This method will block until
enough input is available for decompression.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read, or -1 if end of compressed input is reached
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### read

public int read()
throws

IOException

Reads a byte of uncompressed data. This method will block until
enough input is available for decompression.

read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads uncompressed data into an array of bytes. If

len

is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and

0

is returned.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
compressed input is reached or a preset dictionary is needed
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### read

public int read​(byte[] b,
int off,
int len)
throws

IOException

Reads uncompressed data into an array of bytes. If

len

is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and

0

is returned.

available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:** available

in class

FilterInputStream
**Returns:** 1 before EOF and 0 after EOF.
**Throws:** IOException

- if an I/O error occurs.

---

#### available

public int available()
throws

IOException

Returns 0 after EOF has been reached, otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes of uncompressed data.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

n < 0

---

#### skip

public long skip​(long n)
throws

IOException

Skips specified number of bytes of uncompressed data.

close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources associated
with the stream.

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

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### close

public void close()
throws

IOException

Closes this input stream and releases any system resources associated
with the stream.

fill

```java
protected void fill()
throws
IOException
```

Fills input buffer with more data to decompress.

**Throws:** IOException

- if an I/O error has occurred

---

#### fill

protected void fill()
throws

IOException

Fills input buffer with more data to decompress.

markSupported

```java
public boolean markSupported()
```

Tests if this input stream supports the

mark

and

reset

methods. The

markSupported

method of

InflaterInputStream

returns

false

.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** a

boolean

indicating if this stream type supports
the

mark

and

reset

methods.
**See Also:** InputStream.mark(int)

,

InputStream.reset()

---

#### markSupported

public boolean markSupported()

Tests if this input stream supports the

mark

and

reset

methods. The

markSupported

method of

InflaterInputStream

returns

false

.

mark

```java
public void mark​(int readlimit)
```

Marks the current position in this input stream.

The

mark

method of

InflaterInputStream

does nothing.

**Overrides:** mark

in class

FilterInputStream
**Parameters:** readlimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.
**See Also:** InputStream.reset()

---

#### mark

public void mark​(int readlimit)

Marks the current position in this input stream.

The

mark

method of

InflaterInputStream

does nothing.

The

mark

method of

InflaterInputStream

does nothing.

reset

```java
public void reset()
throws
IOException
```

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

The method

reset

for class

InflaterInputStream

does nothing except throw an

IOException

.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- if this method is invoked.
**See Also:** InputStream.mark(int)

,

IOException

---

#### reset

public void reset()
throws

IOException

Repositions this stream to the position at the time the

mark

method was last called on this input stream.

The method

reset

for class

InflaterInputStream

does nothing except throw an

IOException

.

The method

reset

for class

InflaterInputStream

does nothing except throw an

IOException

.

---

