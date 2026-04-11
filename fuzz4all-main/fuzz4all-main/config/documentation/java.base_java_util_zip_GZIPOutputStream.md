# Class GZIPOutputStream

**Source:** `java.base\java\util\zip\GZIPOutputStream.html`

### Class Description

```java
public class
GZIPOutputStream

extends
DeflaterOutputStream
```

This class implements a stream filter for writing compressed data in
the GZIP file format.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

#### protected
CRC32
crc

CRC-32 of uncompressed data.

---

### Constructor Details

#### public GZIPOutputStream​(
OutputStream
out,
int size)
throws
IOException

Creates a new output stream with the specified buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor GZIPOutputStream(out, size, false).

**Parameters:**
- out

- the output stream
- size

- the output buffer size

**Throws:**
- IOException

- If an I/O error has occurred.
- IllegalArgumentException

- if

size <= 0

---

#### public GZIPOutputStream​(
OutputStream
out,
int size,
boolean syncFlush)
throws
IOException

Creates a new output stream with the specified buffer size and
flush mode.

**Parameters:**
- out

- the output stream
- size

- the output buffer size
- syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream

**Throws:**
- IOException

- If an I/O error has occurred.
- IllegalArgumentException

- if

size <= 0

**Since:**
- 1.7

---

#### public GZIPOutputStream​(
OutputStream
out)
throws
IOException

Creates a new output stream with a default buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor GZIPOutputStream(out, false).

**Parameters:**
- out

- the output stream

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### public GZIPOutputStream​(
OutputStream
out,
boolean syncFlush)
throws
IOException

Creates a new output stream with a default buffer size and
the specified flush mode.

**Parameters:**
- out

- the output stream
- syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream

**Throws:**
- IOException

- If an I/O error has occurred.

**Since:**
- 1.7

---

### Method Details

#### public void write​(byte[] buf,
int off,
int len)
throws
IOException

Writes array of bytes to the compressed output stream. This method
will block until all the bytes are written.

**Overrides:**
- write

in class

DeflaterOutputStream

**Parameters:**
- buf

- the data to be written
- off

- the start offset of the data
- len

- the length of the data

**Throws:**
- IOException

- If an I/O error has occurred.

**See Also:**
- FilterOutputStream.write(int)

---

#### public void finish()
throws
IOException

Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Overrides:**
- finish

in class

DeflaterOutputStream

**Throws:**
- IOException

- if an I/O error has occurred

---

### Additional Sections

#### Class GZIPOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream
- - java.util.zip.GZIPOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream
- - java.util.zip.GZIPOutputStream

java.io.FilterOutputStream

- java.util.zip.DeflaterOutputStream
- - java.util.zip.GZIPOutputStream

java.util.zip.DeflaterOutputStream

- java.util.zip.GZIPOutputStream

java.util.zip.GZIPOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
GZIPOutputStream

extends
DeflaterOutputStream
```

This class implements a stream filter for writing compressed data in
the GZIP file format.

**Since:** 1.1

public class

GZIPOutputStream

extends

DeflaterOutputStream

This class implements a stream filter for writing compressed data in
the GZIP file format.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

CRC32

crc

CRC-32 of uncompressed data.

- Fields declared in class java.util.zip.

DeflaterOutputStream

buf

,

def

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GZIPOutputStream

​(

OutputStream

out)

Creates a new output stream with a default buffer size.

GZIPOutputStream

​(

OutputStream

out,
boolean syncFlush)

Creates a new output stream with a default buffer size and
the specified flush mode.

GZIPOutputStream

​(

OutputStream

out,
int size)

Creates a new output stream with the specified buffer size.

GZIPOutputStream

​(

OutputStream

out,
int size,
boolean syncFlush)

Creates a new output stream with the specified buffer size and
flush mode.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

finish

()

Finishes writing compressed data to the output stream without closing
the underlying stream.

void

write

​(byte[] buf,
int off,
int len)

Writes array of bytes to the compressed output stream.

- Methods declared in class java.util.zip.

DeflaterOutputStream

close

,

deflate

,

flush

,

write

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

protected

CRC32

crc

CRC-32 of uncompressed data.

- Fields declared in class java.util.zip.

DeflaterOutputStream

buf

,

def

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

CRC-32 of uncompressed data.

Fields declared in class java.util.zip.

DeflaterOutputStream

buf

,

def

---

#### Fields declared in class java.util.zip. DeflaterOutputStream

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

GZIPOutputStream

​(

OutputStream

out)

Creates a new output stream with a default buffer size.

GZIPOutputStream

​(

OutputStream

out,
boolean syncFlush)

Creates a new output stream with a default buffer size and
the specified flush mode.

GZIPOutputStream

​(

OutputStream

out,
int size)

Creates a new output stream with the specified buffer size.

GZIPOutputStream

​(

OutputStream

out,
int size,
boolean syncFlush)

Creates a new output stream with the specified buffer size and
flush mode.

---

#### Constructor Summary

Creates a new output stream with a default buffer size.

Creates a new output stream with a default buffer size and
the specified flush mode.

Creates a new output stream with the specified buffer size.

Creates a new output stream with the specified buffer size and
flush mode.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

finish

()

Finishes writing compressed data to the output stream without closing
the underlying stream.

void

write

​(byte[] buf,
int off,
int len)

Writes array of bytes to the compressed output stream.

- Methods declared in class java.util.zip.

DeflaterOutputStream

close

,

deflate

,

flush

,

write

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

Finishes writing compressed data to the output stream without closing
the underlying stream.

Writes array of bytes to the compressed output stream.

Methods declared in class java.util.zip.

DeflaterOutputStream

close

,

deflate

,

flush

,

write

---

#### Methods declared in class java.util.zip. DeflaterOutputStream

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

- crc

```java
protected
CRC32
crc
```

CRC-32 of uncompressed data.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
int size)
throws
IOException
```

Creates a new output stream with the specified buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor GZIPOutputStream(out, size, false).

**Parameters:** out

- the output stream
**Parameters:** size

- the output buffer size
**Throws:** IOException

- If an I/O error has occurred.
**Throws:** IllegalArgumentException

- if

size <= 0

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
int size,
boolean syncFlush)
throws
IOException
```

Creates a new output stream with the specified buffer size and
flush mode.

**Parameters:** out

- the output stream
**Parameters:** size

- the output buffer size
**Parameters:** syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IOException

- If an I/O error has occurred.
**Throws:** IllegalArgumentException

- if

size <= 0
**Since:** 1.7

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out)
throws
IOException
```

Creates a new output stream with a default buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor GZIPOutputStream(out, false).

**Parameters:** out

- the output stream
**Throws:** IOException

- If an I/O error has occurred.

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
boolean syncFlush)
throws
IOException
```

Creates a new output stream with a default buffer size and
the specified flush mode.

**Parameters:** out

- the output stream
**Parameters:** syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IOException

- If an I/O error has occurred.
**Since:** 1.7

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(byte[] buf,
int off,
int len)
throws
IOException
```

Writes array of bytes to the compressed output stream. This method
will block until all the bytes are written.

**Overrides:** write

in class

DeflaterOutputStream
**Parameters:** buf

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**Throws:** IOException

- If an I/O error has occurred.
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

**Overrides:** finish

in class

DeflaterOutputStream
**Throws:** IOException

- if an I/O error has occurred

Field Detail

- crc

```java
protected
CRC32
crc
```

CRC-32 of uncompressed data.

---

#### Field Detail

crc

```java
protected
CRC32
crc
```

CRC-32 of uncompressed data.

---

#### crc

protected

CRC32

crc

CRC-32 of uncompressed data.

Constructor Detail

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
int size)
throws
IOException
```

Creates a new output stream with the specified buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor GZIPOutputStream(out, size, false).

**Parameters:** out

- the output stream
**Parameters:** size

- the output buffer size
**Throws:** IOException

- If an I/O error has occurred.
**Throws:** IllegalArgumentException

- if

size <= 0

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
int size,
boolean syncFlush)
throws
IOException
```

Creates a new output stream with the specified buffer size and
flush mode.

**Parameters:** out

- the output stream
**Parameters:** size

- the output buffer size
**Parameters:** syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IOException

- If an I/O error has occurred.
**Throws:** IllegalArgumentException

- if

size <= 0
**Since:** 1.7

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out)
throws
IOException
```

Creates a new output stream with a default buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor GZIPOutputStream(out, false).

**Parameters:** out

- the output stream
**Throws:** IOException

- If an I/O error has occurred.

- GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
boolean syncFlush)
throws
IOException
```

Creates a new output stream with a default buffer size and
the specified flush mode.

**Parameters:** out

- the output stream
**Parameters:** syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IOException

- If an I/O error has occurred.
**Since:** 1.7

---

#### Constructor Detail

GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
int size)
throws
IOException
```

Creates a new output stream with the specified buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor GZIPOutputStream(out, size, false).

**Parameters:** out

- the output stream
**Parameters:** size

- the output buffer size
**Throws:** IOException

- If an I/O error has occurred.
**Throws:** IllegalArgumentException

- if

size <= 0

---

#### GZIPOutputStream

public GZIPOutputStream​(

OutputStream

out,
int size)
throws

IOException

Creates a new output stream with the specified buffer size.

The new output stream instance is created as if by invoking
the 3-argument constructor GZIPOutputStream(out, size, false).

The new output stream instance is created as if by invoking
the 3-argument constructor GZIPOutputStream(out, size, false).

GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
int size,
boolean syncFlush)
throws
IOException
```

Creates a new output stream with the specified buffer size and
flush mode.

**Parameters:** out

- the output stream
**Parameters:** size

- the output buffer size
**Parameters:** syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IOException

- If an I/O error has occurred.
**Throws:** IllegalArgumentException

- if

size <= 0
**Since:** 1.7

---

#### GZIPOutputStream

public GZIPOutputStream​(

OutputStream

out,
int size,
boolean syncFlush)
throws

IOException

Creates a new output stream with the specified buffer size and
flush mode.

GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out)
throws
IOException
```

Creates a new output stream with a default buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor GZIPOutputStream(out, false).

**Parameters:** out

- the output stream
**Throws:** IOException

- If an I/O error has occurred.

---

#### GZIPOutputStream

public GZIPOutputStream​(

OutputStream

out)
throws

IOException

Creates a new output stream with a default buffer size.

The new output stream instance is created as if by invoking
the 2-argument constructor GZIPOutputStream(out, false).

The new output stream instance is created as if by invoking
the 2-argument constructor GZIPOutputStream(out, false).

GZIPOutputStream

```java
public GZIPOutputStream​(
OutputStream
out,
boolean syncFlush)
throws
IOException
```

Creates a new output stream with a default buffer size and
the specified flush mode.

**Parameters:** out

- the output stream
**Parameters:** syncFlush

- if

true

invocation of the inherited

flush()

method of
this instance flushes the compressor with flush mode

Deflater.SYNC_FLUSH

before flushing the output
stream, otherwise only flushes the output stream
**Throws:** IOException

- If an I/O error has occurred.
**Since:** 1.7

---

#### GZIPOutputStream

public GZIPOutputStream​(

OutputStream

out,
boolean syncFlush)
throws

IOException

Creates a new output stream with a default buffer size and
the specified flush mode.

Method Detail

- write

```java
public void write​(byte[] buf,
int off,
int len)
throws
IOException
```

Writes array of bytes to the compressed output stream. This method
will block until all the bytes are written.

**Overrides:** write

in class

DeflaterOutputStream
**Parameters:** buf

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**Throws:** IOException

- If an I/O error has occurred.
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

**Overrides:** finish

in class

DeflaterOutputStream
**Throws:** IOException

- if an I/O error has occurred

---

#### Method Detail

write

```java
public void write​(byte[] buf,
int off,
int len)
throws
IOException
```

Writes array of bytes to the compressed output stream. This method
will block until all the bytes are written.

**Overrides:** write

in class

DeflaterOutputStream
**Parameters:** buf

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**Throws:** IOException

- If an I/O error has occurred.
**See Also:** FilterOutputStream.write(int)

---

#### write

public void write​(byte[] buf,
int off,
int len)
throws

IOException

Writes array of bytes to the compressed output stream. This method
will block until all the bytes are written.

finish

```java
public void finish()
throws
IOException
```

Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Overrides:** finish

in class

DeflaterOutputStream
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

---

