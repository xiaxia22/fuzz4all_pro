# Class DeflaterOutputStream

**Source:** `java.base\java\util\zip\DeflaterOutputStream.html`

### Class Description

```java
public class
DeflaterOutputStream

extends
FilterOutputStream
```

This class implements an output stream filter for compressing data in
the "deflate" compression format. It is also used as the basis for other
types of compression filters, such as GZIPOutputStream.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

#### protected
Deflater
def

Compressor for this stream.

---

#### protected byte[] buf

Output buffer for writing compressed data.

---

### Constructor Details

#### public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size,
boolean syncFlush)

Creates a new output stream with the specified compressor,
buffer size and flush mode.

**Parameters:**
- out

- the output stream
- def

- the compressor ("deflater")
- size

- the output buffer size
- syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream

**Throws:**
- IllegalArgumentException

- if

size <= 0

**Since:**
- 1.7

---

#### public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size)

Creates a new output stream with the specified compressor and
buffer size.

The new output stream instance is created as if by invoking
the 4-argument constructor DeflaterOutputStream(out, def, size, false).

**Parameters:**
- out

- the output stream
- def

- the compressor ("deflater")
- size

- the output buffer size

**Throws:**
- IllegalArgumentException

- if

size <= 0

---

#### public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
boolean syncFlush)

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

**Parameters:**
- out

- the output stream
- def

- the compressor ("deflater")
- syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream

**Since:**
- 1.7

---

#### public DeflaterOutputStream​(
OutputStream
out,

Deflater
def)

Creates a new output stream with the specified compressor and
a default buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor DeflaterOutputStream(out, def, false).

**Parameters:**
- out

- the output stream
- def

- the compressor ("deflater")

---

#### public DeflaterOutputStream​(
OutputStream
out,
boolean syncFlush)

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

**Parameters:**
- out

- the output stream
- syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream

**Since:**
- 1.7

---

#### public DeflaterOutputStream​(
OutputStream
out)

Creates a new output stream with a default compressor and buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor DeflaterOutputStream(out, false).

**Parameters:**
- out

- the output stream

---

### Method Details

#### public void write​(int b)
throws
IOException

Writes a byte to the compressed output stream. This method will
block until the byte can be written.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the byte to be written

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public void write​(byte[] b,
int off,
int len)
throws
IOException

Writes an array of bytes to the compressed output stream. This
method will block until all the bytes are written.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the data to be written
- off

- the start offset of the data
- len

- the length of the data

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterOutputStream.write(int)

---

#### public void finish()
throws
IOException

Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public void close()
throws
IOException

Writes remaining compressed data to the output stream and closes the
underlying stream.

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

FilterOutputStream

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### protected void deflate()
throws
IOException

Writes next block of compressed data to the output stream.

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public void flush()
throws
IOException

Flushes the compressed output stream.

If

syncFlush

is

true

when this compressed output stream is
constructed, this method first flushes the underlying

compressor

with the flush mode

Deflater.SYNC_FLUSH

to force
all pending data to be flushed out to the output stream and then
flushes the output stream. Otherwise this method only flushes the
output stream without flushing the

compressor

.

**Specified by:**
- flush

in interface

Flushable

**Overrides:**
- flush

in class

FilterOutputStream

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterOutputStream.out

**Since:**
- 1.7

---

### Additional Sections

#### Class DeflaterOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream

java.io.FilterOutputStream

- java.util.zip.DeflaterOutputStream

java.util.zip.DeflaterOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

**Direct Known Subclasses:** GZIPOutputStream

,

ZipOutputStream

```java
public class
DeflaterOutputStream

extends
FilterOutputStream
```

This class implements an output stream filter for compressing data in
the "deflate" compression format. It is also used as the basis for other
types of compression filters, such as GZIPOutputStream.

**Since:** 1.1
**See Also:** Deflater

public class

DeflaterOutputStream

extends

FilterOutputStream

This class implements an output stream filter for compressing data in
the "deflate" compression format. It is also used as the basis for other
types of compression filters, such as GZIPOutputStream.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

buf

Output buffer for writing compressed data.

protected

Deflater

def

Compressor for this stream.

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DeflaterOutputStream

​(

OutputStream

out)

Creates a new output stream with a default compressor and buffer size.

DeflaterOutputStream

​(

OutputStream

out,
boolean syncFlush)

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def)

Creates a new output stream with the specified compressor and
a default buffer size.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def,
boolean syncFlush)

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def,
int size)

Creates a new output stream with the specified compressor and
buffer size.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def,
int size,
boolean syncFlush)

Creates a new output stream with the specified compressor,
buffer size and flush mode.

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

Writes remaining compressed data to the output stream and closes the
underlying stream.

protected void

deflate

()

Writes next block of compressed data to the output stream.

void

finish

()

Finishes writing compressed data to the output stream without closing
the underlying stream.

void

flush

()

Flushes the compressed output stream.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes to the compressed output stream.

void

write

​(int b)

Writes a byte to the compressed output stream.

- Methods declared in class java.io.

FilterOutputStream

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

Output buffer for writing compressed data.

protected

Deflater

def

Compressor for this stream.

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

Output buffer for writing compressed data.

Compressor for this stream.

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

DeflaterOutputStream

​(

OutputStream

out)

Creates a new output stream with a default compressor and buffer size.

DeflaterOutputStream

​(

OutputStream

out,
boolean syncFlush)

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def)

Creates a new output stream with the specified compressor and
a default buffer size.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def,
boolean syncFlush)

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def,
int size)

Creates a new output stream with the specified compressor and
buffer size.

DeflaterOutputStream

​(

OutputStream

out,

Deflater

def,
int size,
boolean syncFlush)

Creates a new output stream with the specified compressor,
buffer size and flush mode.

---

#### Constructor Summary

Creates a new output stream with a default compressor and buffer size.

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

Creates a new output stream with the specified compressor and
a default buffer size.

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

Creates a new output stream with the specified compressor and
buffer size.

Creates a new output stream with the specified compressor,
buffer size and flush mode.

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

Writes remaining compressed data to the output stream and closes the
underlying stream.

protected void

deflate

()

Writes next block of compressed data to the output stream.

void

finish

()

Finishes writing compressed data to the output stream without closing
the underlying stream.

void

flush

()

Flushes the compressed output stream.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes to the compressed output stream.

void

write

​(int b)

Writes a byte to the compressed output stream.

- Methods declared in class java.io.

FilterOutputStream

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

Writes remaining compressed data to the output stream and closes the
underlying stream.

Writes next block of compressed data to the output stream.

Finishes writing compressed data to the output stream without closing
the underlying stream.

Flushes the compressed output stream.

Writes an array of bytes to the compressed output stream.

Writes a byte to the compressed output stream.

Methods declared in class java.io.

FilterOutputStream

write

---

#### Methods declared in class java.io. FilterOutputStream

Methods declared in class java.io.

OutputStream

nullOutputStream

---

#### Methods declared in class java.io. OutputStream

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
protected
Deflater
def
```

Compressor for this stream.

- buf

```java
protected byte[] buf
```

Output buffer for writing compressed data.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size,
boolean syncFlush)
```

Creates a new output stream with the specified compressor,
buffer size and flush mode.

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** size

- the output buffer size
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IllegalArgumentException

- if

size <= 0
**Since:** 1.7

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size)
```

Creates a new output stream with the specified compressor and
buffer size.

The new output stream instance is created as if by invoking
the 4-argument constructor DeflaterOutputStream(out, def, size, false).

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** size

- the output buffer size
**Throws:** IllegalArgumentException

- if

size <= 0

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
boolean syncFlush)
```

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Since:** 1.7

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def)
```

Creates a new output stream with the specified compressor and
a default buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor DeflaterOutputStream(out, def, false).

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,
boolean syncFlush)
```

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

**Parameters:** out

- the output stream
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Since:** 1.7

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out)
```

Creates a new output stream with a default compressor and buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor DeflaterOutputStream(out, false).

**Parameters:** out

- the output stream

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes a byte to the compressed output stream. This method will
block until the byte can be written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be written
**Throws:** IOException

- if an I/O error has occurred

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the compressed output stream. This
method will block until all the bytes are written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

- finish

```java
public void finish()
throws
IOException
```

Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Throws:** IOException

- if an I/O error has occurred

- close

```java
public void close()
throws
IOException
```

Writes remaining compressed data to the output stream and closes the
underlying stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

- deflate

```java
protected void deflate()
throws
IOException
```

Writes next block of compressed data to the output stream.

**Throws:** IOException

- if an I/O error has occurred

- flush

```java
public void flush()
throws
IOException
```

Flushes the compressed output stream.

If

syncFlush

is

true

when this compressed output stream is
constructed, this method first flushes the underlying

compressor

with the flush mode

Deflater.SYNC_FLUSH

to force
all pending data to be flushed out to the output stream and then
flushes the output stream. Otherwise this method only flushes the
output stream without flushing the

compressor

.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error has occurred
**Since:** 1.7
**See Also:** FilterOutputStream.out

Field Detail

- def

```java
protected
Deflater
def
```

Compressor for this stream.

- buf

```java
protected byte[] buf
```

Output buffer for writing compressed data.

---

#### Field Detail

def

```java
protected
Deflater
def
```

Compressor for this stream.

---

#### def

protected

Deflater

def

Compressor for this stream.

buf

```java
protected byte[] buf
```

Output buffer for writing compressed data.

---

#### buf

protected byte[] buf

Output buffer for writing compressed data.

Constructor Detail

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size,
boolean syncFlush)
```

Creates a new output stream with the specified compressor,
buffer size and flush mode.

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** size

- the output buffer size
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IllegalArgumentException

- if

size <= 0
**Since:** 1.7

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size)
```

Creates a new output stream with the specified compressor and
buffer size.

The new output stream instance is created as if by invoking
the 4-argument constructor DeflaterOutputStream(out, def, size, false).

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** size

- the output buffer size
**Throws:** IllegalArgumentException

- if

size <= 0

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
boolean syncFlush)
```

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Since:** 1.7

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def)
```

Creates a new output stream with the specified compressor and
a default buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor DeflaterOutputStream(out, def, false).

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,
boolean syncFlush)
```

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

**Parameters:** out

- the output stream
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Since:** 1.7

- DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out)
```

Creates a new output stream with a default compressor and buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor DeflaterOutputStream(out, false).

**Parameters:** out

- the output stream

---

#### Constructor Detail

DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size,
boolean syncFlush)
```

Creates a new output stream with the specified compressor,
buffer size and flush mode.

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** size

- the output buffer size
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IllegalArgumentException

- if

size <= 0
**Since:** 1.7

---

#### DeflaterOutputStream

public DeflaterOutputStream​(

OutputStream

out,

Deflater

def,
int size,
boolean syncFlush)

Creates a new output stream with the specified compressor,
buffer size and flush mode.

DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
int size)
```

Creates a new output stream with the specified compressor and
buffer size.

The new output stream instance is created as if by invoking
the 4-argument constructor DeflaterOutputStream(out, def, size, false).

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** size

- the output buffer size
**Throws:** IllegalArgumentException

- if

size <= 0

---

#### DeflaterOutputStream

public DeflaterOutputStream​(

OutputStream

out,

Deflater

def,
int size)

Creates a new output stream with the specified compressor and
buffer size.

The new output stream instance is created as if by invoking
the 4-argument constructor DeflaterOutputStream(out, def, size, false).

The new output stream instance is created as if by invoking
the 4-argument constructor DeflaterOutputStream(out, def, size, false).

DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def,
boolean syncFlush)
```

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Since:** 1.7

---

#### DeflaterOutputStream

public DeflaterOutputStream​(

OutputStream

out,

Deflater

def,
boolean syncFlush)

Creates a new output stream with the specified compressor, flush
mode and a default buffer size.

DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,

Deflater
def)
```

Creates a new output stream with the specified compressor and
a default buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor DeflaterOutputStream(out, def, false).

**Parameters:** out

- the output stream
**Parameters:** def

- the compressor ("deflater")

---

#### DeflaterOutputStream

public DeflaterOutputStream​(

OutputStream

out,

Deflater

def)

Creates a new output stream with the specified compressor and
a default buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor DeflaterOutputStream(out, def, false).

The new output stream instance is created as if by invoking
the 3-argument constructor DeflaterOutputStream(out, def, false).

DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out,
boolean syncFlush)
```

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

**Parameters:** out

- the output stream
**Parameters:** syncFlush

- if

true

the

flush()

method of this
instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Since:** 1.7

---

#### DeflaterOutputStream

public DeflaterOutputStream​(

OutputStream

out,
boolean syncFlush)

Creates a new output stream with a default compressor, a default
buffer size and the specified flush mode.

DeflaterOutputStream

```java
public DeflaterOutputStream​(
OutputStream
out)
```

Creates a new output stream with a default compressor and buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor DeflaterOutputStream(out, false).

**Parameters:** out

- the output stream

---

#### DeflaterOutputStream

public DeflaterOutputStream​(

OutputStream

out)

Creates a new output stream with a default compressor and buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor DeflaterOutputStream(out, false).

The new output stream instance is created as if by invoking
the 2-argument constructor DeflaterOutputStream(out, false).

Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes a byte to the compressed output stream. This method will
block until the byte can be written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be written
**Throws:** IOException

- if an I/O error has occurred

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the compressed output stream. This
method will block until all the bytes are written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

- finish

```java
public void finish()
throws
IOException
```

Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Throws:** IOException

- if an I/O error has occurred

- close

```java
public void close()
throws
IOException
```

Writes remaining compressed data to the output stream and closes the
underlying stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

- deflate

```java
protected void deflate()
throws
IOException
```

Writes next block of compressed data to the output stream.

**Throws:** IOException

- if an I/O error has occurred

- flush

```java
public void flush()
throws
IOException
```

Flushes the compressed output stream.

If

syncFlush

is

true

when this compressed output stream is
constructed, this method first flushes the underlying

compressor

with the flush mode

Deflater.SYNC_FLUSH

to force
all pending data to be flushed out to the output stream and then
flushes the output stream. Otherwise this method only flushes the
output stream without flushing the

compressor

.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error has occurred
**Since:** 1.7
**See Also:** FilterOutputStream.out

---

#### Method Detail

write

```java
public void write​(int b)
throws
IOException
```

Writes a byte to the compressed output stream. This method will
block until the byte can be written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be written
**Throws:** IOException

- if an I/O error has occurred

---

#### write

public void write​(int b)
throws

IOException

Writes a byte to the compressed output stream. This method will
block until the byte can be written.

write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the compressed output stream. This
method will block until all the bytes are written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

---

#### write

public void write​(byte[] b,
int off,
int len)
throws

IOException

Writes an array of bytes to the compressed output stream. This
method will block until all the bytes are written.

finish

```java
public void finish()
throws
IOException
```

Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Throws:** IOException

- if an I/O error has occurred

---

#### finish

public void finish()
throws

IOException

Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

close

```java
public void close()
throws
IOException
```

Writes remaining compressed data to the output stream and closes the
underlying stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### close

public void close()
throws

IOException

Writes remaining compressed data to the output stream and closes the
underlying stream.

deflate

```java
protected void deflate()
throws
IOException
```

Writes next block of compressed data to the output stream.

**Throws:** IOException

- if an I/O error has occurred

---

#### deflate

protected void deflate()
throws

IOException

Writes next block of compressed data to the output stream.

flush

```java
public void flush()
throws
IOException
```

Flushes the compressed output stream.

If

syncFlush

is

true

when this compressed output stream is
constructed, this method first flushes the underlying

compressor

with the flush mode

Deflater.SYNC_FLUSH

to force
all pending data to be flushed out to the output stream and then
flushes the output stream. Otherwise this method only flushes the
output stream without flushing the

compressor

.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error has occurred
**Since:** 1.7
**See Also:** FilterOutputStream.out

---

#### flush

public void flush()
throws

IOException

Flushes the compressed output stream.

If

syncFlush

is

true

when this compressed output stream is
constructed, this method first flushes the underlying

compressor

with the flush mode

Deflater.SYNC_FLUSH

to force
all pending data to be flushed out to the output stream and then
flushes the output stream. Otherwise this method only flushes the
output stream without flushing the

compressor

.

---

