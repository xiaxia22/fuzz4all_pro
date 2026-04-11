# Class InflaterOutputStream

**Source:** `java.base\java\util\zip\InflaterOutputStream.html`

### Class Description

```java
public class
InflaterOutputStream

extends
FilterOutputStream
```

Implements an output stream filter for uncompressing data stored in the
"deflate" compression format.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

#### protected final
Inflater
inf

Decompressor for this stream.

---

#### protected final byte[] buf

Output buffer for writing uncompressed data.

---

### Constructor Details

#### public InflaterOutputStream​(
OutputStream
out)

Creates a new output stream with a default decompressor and buffer
size.

**Parameters:**
- out

- output stream to write the uncompressed data to

**Throws:**
- NullPointerException

- if

out

is null

---

#### public InflaterOutputStream​(
OutputStream
out,

Inflater
infl)

Creates a new output stream with the specified decompressor and a
default buffer size.

**Parameters:**
- out

- output stream to write the uncompressed data to
- infl

- decompressor ("inflater") for this stream

**Throws:**
- NullPointerException

- if

out

or

infl

is null

---

#### public InflaterOutputStream​(
OutputStream
out,

Inflater
infl,
int bufLen)

Creates a new output stream with the specified decompressor and
buffer size.

**Parameters:**
- out

- output stream to write the uncompressed data to
- infl

- decompressor ("inflater") for this stream
- bufLen

- decompression buffer size

**Throws:**
- IllegalArgumentException

- if

bufLen <= 0
- NullPointerException

- if

out

or

infl

is null

---

### Method Details

#### public void close()
throws
IOException

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

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

- if an I/O error occurs

**See Also:**
- FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### public void flush()
throws
IOException

Flushes this output stream, forcing any pending buffered output bytes to be
written.

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

- if an I/O error occurs or this stream is already
closed

**See Also:**
- FilterOutputStream.out

---

#### public void finish()
throws
IOException

Finishes writing uncompressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters in
succession to the same output stream.

**Throws:**
- IOException

- if an I/O error occurs or this stream is already
closed

---

#### public void write​(int b)
throws
IOException

Writes a byte to the uncompressed output stream.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- a single byte of compressed data to decompress and write to
the output stream

**Throws:**
- IOException

- if an I/O error occurs or this stream is already
closed
- ZipException

- if a compression (ZIP) format error occurs

---

#### public void write​(byte[] b,
int off,
int len)
throws
IOException

Writes an array of bytes to the uncompressed output stream.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- buffer containing compressed data to decompress and write to
the output stream
- off

- starting offset of the compressed data within

b
- len

- number of bytes to decompress from

b

**Throws:**
- IndexOutOfBoundsException

- if

off < 0

, or if

len < 0

, or if

len > b.length - off
- IOException

- if an I/O error occurs or this stream is already
closed
- NullPointerException

- if

b

is null
- ZipException

- if a compression (ZIP) format error occurs

**See Also:**
- FilterOutputStream.write(int)

---

### Additional Sections

#### Class InflaterOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.util.zip.InflaterOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.util.zip.InflaterOutputStream

java.io.FilterOutputStream

- java.util.zip.InflaterOutputStream

java.util.zip.InflaterOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
InflaterOutputStream

extends
FilterOutputStream
```

Implements an output stream filter for uncompressing data stored in the
"deflate" compression format.

**Since:** 1.6
**See Also:** InflaterInputStream

,

DeflaterInputStream

,

DeflaterOutputStream

public class

InflaterOutputStream

extends

FilterOutputStream

Implements an output stream filter for uncompressing data stored in the
"deflate" compression format.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

buf

Output buffer for writing uncompressed data.

protected

Inflater

inf

Decompressor for this stream.

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InflaterOutputStream

​(

OutputStream

out)

Creates a new output stream with a default decompressor and buffer
size.

InflaterOutputStream

​(

OutputStream

out,

Inflater

infl)

Creates a new output stream with the specified decompressor and a
default buffer size.

InflaterOutputStream

​(

OutputStream

out,

Inflater

infl,
int bufLen)

Creates a new output stream with the specified decompressor and
buffer size.

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

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

void

finish

()

Finishes writing uncompressed data to the output stream without closing
the underlying stream.

void

flush

()

Flushes this output stream, forcing any pending buffered output bytes to be
written.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes to the uncompressed output stream.

void

write

​(int b)

Writes a byte to the uncompressed output stream.

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

Output buffer for writing uncompressed data.

protected

Inflater

inf

Decompressor for this stream.

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

Output buffer for writing uncompressed data.

Decompressor for this stream.

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

InflaterOutputStream

​(

OutputStream

out)

Creates a new output stream with a default decompressor and buffer
size.

InflaterOutputStream

​(

OutputStream

out,

Inflater

infl)

Creates a new output stream with the specified decompressor and a
default buffer size.

InflaterOutputStream

​(

OutputStream

out,

Inflater

infl,
int bufLen)

Creates a new output stream with the specified decompressor and
buffer size.

---

#### Constructor Summary

Creates a new output stream with a default decompressor and buffer
size.

Creates a new output stream with the specified decompressor and a
default buffer size.

Creates a new output stream with the specified decompressor and
buffer size.

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

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

void

finish

()

Finishes writing uncompressed data to the output stream without closing
the underlying stream.

void

flush

()

Flushes this output stream, forcing any pending buffered output bytes to be
written.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes to the uncompressed output stream.

void

write

​(int b)

Writes a byte to the uncompressed output stream.

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

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

Finishes writing uncompressed data to the output stream without closing
the underlying stream.

Flushes this output stream, forcing any pending buffered output bytes to be
written.

Writes an array of bytes to the uncompressed output stream.

Writes a byte to the uncompressed output stream.

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

- inf

```java
protected final
Inflater
inf
```

Decompressor for this stream.

- buf

```java
protected final byte[] buf
```

Output buffer for writing uncompressed data.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out)
```

Creates a new output stream with a default decompressor and buffer
size.

**Parameters:** out

- output stream to write the uncompressed data to
**Throws:** NullPointerException

- if

out

is null

- InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out,

Inflater
infl)
```

Creates a new output stream with the specified decompressor and a
default buffer size.

**Parameters:** out

- output stream to write the uncompressed data to
**Parameters:** infl

- decompressor ("inflater") for this stream
**Throws:** NullPointerException

- if

out

or

infl

is null

- InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out,

Inflater
infl,
int bufLen)
```

Creates a new output stream with the specified decompressor and
buffer size.

**Parameters:** out

- output stream to write the uncompressed data to
**Parameters:** infl

- decompressor ("inflater") for this stream
**Parameters:** bufLen

- decompression buffer size
**Throws:** IllegalArgumentException

- if

bufLen <= 0
**Throws:** NullPointerException

- if

out

or

infl

is null

============ METHOD DETAIL ==========

- Method Detail

- close

```java
public void close()
throws
IOException
```

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

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

- if an I/O error occurs
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream, forcing any pending buffered output bytes to be
written.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**See Also:** FilterOutputStream.out

- finish

```java
public void finish()
throws
IOException
```

Finishes writing uncompressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters in
succession to the same output stream.

**Throws:** IOException

- if an I/O error occurs or this stream is already
closed

- write

```java
public void write​(int b)
throws
IOException
```

Writes a byte to the uncompressed output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- a single byte of compressed data to decompress and write to
the output stream
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**Throws:** ZipException

- if a compression (ZIP) format error occurs

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the uncompressed output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- buffer containing compressed data to decompress and write to
the output stream
**Parameters:** off

- starting offset of the compressed data within

b
**Parameters:** len

- number of bytes to decompress from

b
**Throws:** IndexOutOfBoundsException

- if

off < 0

, or if

len < 0

, or if

len > b.length - off
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**Throws:** NullPointerException

- if

b

is null
**Throws:** ZipException

- if a compression (ZIP) format error occurs
**See Also:** FilterOutputStream.write(int)

Field Detail

- inf

```java
protected final
Inflater
inf
```

Decompressor for this stream.

- buf

```java
protected final byte[] buf
```

Output buffer for writing uncompressed data.

---

#### Field Detail

inf

```java
protected final
Inflater
inf
```

Decompressor for this stream.

---

#### inf

protected final

Inflater

inf

Decompressor for this stream.

buf

```java
protected final byte[] buf
```

Output buffer for writing uncompressed data.

---

#### buf

protected final byte[] buf

Output buffer for writing uncompressed data.

Constructor Detail

- InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out)
```

Creates a new output stream with a default decompressor and buffer
size.

**Parameters:** out

- output stream to write the uncompressed data to
**Throws:** NullPointerException

- if

out

is null

- InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out,

Inflater
infl)
```

Creates a new output stream with the specified decompressor and a
default buffer size.

**Parameters:** out

- output stream to write the uncompressed data to
**Parameters:** infl

- decompressor ("inflater") for this stream
**Throws:** NullPointerException

- if

out

or

infl

is null

- InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out,

Inflater
infl,
int bufLen)
```

Creates a new output stream with the specified decompressor and
buffer size.

**Parameters:** out

- output stream to write the uncompressed data to
**Parameters:** infl

- decompressor ("inflater") for this stream
**Parameters:** bufLen

- decompression buffer size
**Throws:** IllegalArgumentException

- if

bufLen <= 0
**Throws:** NullPointerException

- if

out

or

infl

is null

---

#### Constructor Detail

InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out)
```

Creates a new output stream with a default decompressor and buffer
size.

**Parameters:** out

- output stream to write the uncompressed data to
**Throws:** NullPointerException

- if

out

is null

---

#### InflaterOutputStream

public InflaterOutputStream​(

OutputStream

out)

Creates a new output stream with a default decompressor and buffer
size.

InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out,

Inflater
infl)
```

Creates a new output stream with the specified decompressor and a
default buffer size.

**Parameters:** out

- output stream to write the uncompressed data to
**Parameters:** infl

- decompressor ("inflater") for this stream
**Throws:** NullPointerException

- if

out

or

infl

is null

---

#### InflaterOutputStream

public InflaterOutputStream​(

OutputStream

out,

Inflater

infl)

Creates a new output stream with the specified decompressor and a
default buffer size.

InflaterOutputStream

```java
public InflaterOutputStream​(
OutputStream
out,

Inflater
infl,
int bufLen)
```

Creates a new output stream with the specified decompressor and
buffer size.

**Parameters:** out

- output stream to write the uncompressed data to
**Parameters:** infl

- decompressor ("inflater") for this stream
**Parameters:** bufLen

- decompression buffer size
**Throws:** IllegalArgumentException

- if

bufLen <= 0
**Throws:** NullPointerException

- if

out

or

infl

is null

---

#### InflaterOutputStream

public InflaterOutputStream​(

OutputStream

out,

Inflater

infl,
int bufLen)

Creates a new output stream with the specified decompressor and
buffer size.

Method Detail

- close

```java
public void close()
throws
IOException
```

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

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

- if an I/O error occurs
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream, forcing any pending buffered output bytes to be
written.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**See Also:** FilterOutputStream.out

- finish

```java
public void finish()
throws
IOException
```

Finishes writing uncompressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters in
succession to the same output stream.

**Throws:** IOException

- if an I/O error occurs or this stream is already
closed

- write

```java
public void write​(int b)
throws
IOException
```

Writes a byte to the uncompressed output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- a single byte of compressed data to decompress and write to
the output stream
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**Throws:** ZipException

- if a compression (ZIP) format error occurs

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the uncompressed output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- buffer containing compressed data to decompress and write to
the output stream
**Parameters:** off

- starting offset of the compressed data within

b
**Parameters:** len

- number of bytes to decompress from

b
**Throws:** IndexOutOfBoundsException

- if

off < 0

, or if

len < 0

, or if

len > b.length - off
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**Throws:** NullPointerException

- if

b

is null
**Throws:** ZipException

- if a compression (ZIP) format error occurs
**See Also:** FilterOutputStream.write(int)

---

#### Method Detail

close

```java
public void close()
throws
IOException
```

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

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

- if an I/O error occurs
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### close

public void close()
throws

IOException

Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.

flush

```java
public void flush()
throws
IOException
```

Flushes this output stream, forcing any pending buffered output bytes to be
written.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**See Also:** FilterOutputStream.out

---

#### flush

public void flush()
throws

IOException

Flushes this output stream, forcing any pending buffered output bytes to be
written.

finish

```java
public void finish()
throws
IOException
```

Finishes writing uncompressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters in
succession to the same output stream.

**Throws:** IOException

- if an I/O error occurs or this stream is already
closed

---

#### finish

public void finish()
throws

IOException

Finishes writing uncompressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters in
succession to the same output stream.

write

```java
public void write​(int b)
throws
IOException
```

Writes a byte to the uncompressed output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- a single byte of compressed data to decompress and write to
the output stream
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**Throws:** ZipException

- if a compression (ZIP) format error occurs

---

#### write

public void write​(int b)
throws

IOException

Writes a byte to the uncompressed output stream.

write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the uncompressed output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- buffer containing compressed data to decompress and write to
the output stream
**Parameters:** off

- starting offset of the compressed data within

b
**Parameters:** len

- number of bytes to decompress from

b
**Throws:** IndexOutOfBoundsException

- if

off < 0

, or if

len < 0

, or if

len > b.length - off
**Throws:** IOException

- if an I/O error occurs or this stream is already
closed
**Throws:** NullPointerException

- if

b

is null
**Throws:** ZipException

- if a compression (ZIP) format error occurs
**See Also:** FilterOutputStream.write(int)

---

#### write

public void write​(byte[] b,
int off,
int len)
throws

IOException

Writes an array of bytes to the uncompressed output stream.

---

