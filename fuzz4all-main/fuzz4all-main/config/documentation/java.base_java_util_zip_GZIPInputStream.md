# Class GZIPInputStream

**Source:** `java.base\java\util\zip\GZIPInputStream.html`

### Class Description

```java
public class
GZIPInputStream

extends
InflaterInputStream
```

This class implements a stream filter for reading compressed data in
the GZIP file format.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

#### protected
CRC32
crc

CRC-32 for uncompressed data.

---

#### protected boolean eos

Indicates end of input stream.

---

#### public static final int GZIP_MAGIC

GZIP header magic number.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public GZIPInputStream​(
InputStream
in,
int size)
throws
IOException

Creates a new input stream with the specified buffer size.

**Parameters:**
- in

- the input stream
- size

- the input buffer size

**Throws:**
- ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
- IOException

- if an I/O error has occurred
- IllegalArgumentException

- if

size <= 0

---

#### public GZIPInputStream​(
InputStream
in)
throws
IOException

Creates a new input stream with a default buffer size.

**Parameters:**
- in

- the input stream

**Throws:**
- ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
- IOException

- if an I/O error has occurred

---

### Method Details

#### public int read​(byte[] buf,
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

InflaterInputStream

**Parameters:**
- buf

- the buffer into which the data is read
- off

- the start offset in the destination array

b
- len

- the maximum number of bytes read

**Returns:**
- the actual number of bytes read, or -1 if the end of the
compressed input stream is reached

**Throws:**
- NullPointerException

- If

buf

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

buf.length - off
- ZipException

- if the compressed input data is corrupt.
- IOException

- if an I/O error has occurred.

**See Also:**
- FilterInputStream.in

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

InflaterInputStream

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

### Additional Sections

#### Class GZIPInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - java.util.zip.InflaterInputStream
- - java.util.zip.GZIPInputStream

java.io.InputStream

- java.io.FilterInputStream
- - java.util.zip.InflaterInputStream
- - java.util.zip.GZIPInputStream

java.io.FilterInputStream

- java.util.zip.InflaterInputStream
- - java.util.zip.GZIPInputStream

java.util.zip.InflaterInputStream

- java.util.zip.GZIPInputStream

java.util.zip.GZIPInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
GZIPInputStream

extends
InflaterInputStream
```

This class implements a stream filter for reading compressed data in
the GZIP file format.

**Since:** 1.1
**See Also:** InflaterInputStream

public class

GZIPInputStream

extends

InflaterInputStream

This class implements a stream filter for reading compressed data in
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

CRC-32 for uncompressed data.

protected boolean

eos

Indicates end of input stream.

static int

GZIP_MAGIC

GZIP header magic number.

- Fields declared in class java.util.zip.

InflaterInputStream

buf

,

inf

,

len

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GZIPInputStream

​(

InputStream

in)

Creates a new input stream with a default buffer size.

GZIPInputStream

​(

InputStream

in,
int size)

Creates a new input stream with the specified buffer size.

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

Closes this input stream and releases any system resources associated
with the stream.

int

read

​(byte[] buf,
int off,
int len)

Reads uncompressed data into an array of bytes.

- Methods declared in class java.util.zip.

InflaterInputStream

available

,

fill

,

mark

,

markSupported

,

read

,

reset

,

skip

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

protected

CRC32

crc

CRC-32 for uncompressed data.

protected boolean

eos

Indicates end of input stream.

static int

GZIP_MAGIC

GZIP header magic number.

- Fields declared in class java.util.zip.

InflaterInputStream

buf

,

inf

,

len

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

CRC-32 for uncompressed data.

Indicates end of input stream.

GZIP header magic number.

Fields declared in class java.util.zip.

InflaterInputStream

buf

,

inf

,

len

---

#### Fields declared in class java.util.zip. InflaterInputStream

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Constructor

Description

GZIPInputStream

​(

InputStream

in)

Creates a new input stream with a default buffer size.

GZIPInputStream

​(

InputStream

in,
int size)

Creates a new input stream with the specified buffer size.

---

#### Constructor Summary

Creates a new input stream with a default buffer size.

Creates a new input stream with the specified buffer size.

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

Closes this input stream and releases any system resources associated
with the stream.

int

read

​(byte[] buf,
int off,
int len)

Reads uncompressed data into an array of bytes.

- Methods declared in class java.util.zip.

InflaterInputStream

available

,

fill

,

mark

,

markSupported

,

read

,

reset

,

skip

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

Closes this input stream and releases any system resources associated
with the stream.

Reads uncompressed data into an array of bytes.

Methods declared in class java.util.zip.

InflaterInputStream

available

,

fill

,

mark

,

markSupported

,

read

,

reset

,

skip

---

#### Methods declared in class java.util.zip. InflaterInputStream

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

- crc

```java
protected
CRC32
crc
```

CRC-32 for uncompressed data.

- eos

```java
protected boolean eos
```

Indicates end of input stream.

- GZIP_MAGIC

```java
public static final int GZIP_MAGIC
```

GZIP header magic number.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GZIPInputStream

```java
public GZIPInputStream​(
InputStream
in,
int size)
throws
IOException
```

Creates a new input stream with the specified buffer size.

**Parameters:** in

- the input stream
**Parameters:** size

- the input buffer size
**Throws:** ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

size <= 0

- GZIPInputStream

```java
public GZIPInputStream​(
InputStream
in)
throws
IOException
```

Creates a new input stream with a default buffer size.

**Parameters:** in

- the input stream
**Throws:** ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
**Throws:** IOException

- if an I/O error has occurred

============ METHOD DETAIL ==========

- Method Detail

- read

```java
public int read​(byte[] buf,
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

InflaterInputStream
**Parameters:** buf

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
compressed input stream is reached
**Throws:** NullPointerException

- If

buf

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

buf.length - off
**Throws:** ZipException

- if the compressed input data is corrupt.
**Throws:** IOException

- if an I/O error has occurred.
**See Also:** FilterInputStream.in

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

InflaterInputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

Field Detail

- crc

```java
protected
CRC32
crc
```

CRC-32 for uncompressed data.

- eos

```java
protected boolean eos
```

Indicates end of input stream.

- GZIP_MAGIC

```java
public static final int GZIP_MAGIC
```

GZIP header magic number.

**See Also:** Constant Field Values

---

#### Field Detail

crc

```java
protected
CRC32
crc
```

CRC-32 for uncompressed data.

---

#### crc

protected

CRC32

crc

CRC-32 for uncompressed data.

eos

```java
protected boolean eos
```

Indicates end of input stream.

---

#### eos

protected boolean eos

Indicates end of input stream.

GZIP_MAGIC

```java
public static final int GZIP_MAGIC
```

GZIP header magic number.

**See Also:** Constant Field Values

---

#### GZIP_MAGIC

public static final int GZIP_MAGIC

GZIP header magic number.

Constructor Detail

- GZIPInputStream

```java
public GZIPInputStream​(
InputStream
in,
int size)
throws
IOException
```

Creates a new input stream with the specified buffer size.

**Parameters:** in

- the input stream
**Parameters:** size

- the input buffer size
**Throws:** ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

size <= 0

- GZIPInputStream

```java
public GZIPInputStream​(
InputStream
in)
throws
IOException
```

Creates a new input stream with a default buffer size.

**Parameters:** in

- the input stream
**Throws:** ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
**Throws:** IOException

- if an I/O error has occurred

---

#### Constructor Detail

GZIPInputStream

```java
public GZIPInputStream​(
InputStream
in,
int size)
throws
IOException
```

Creates a new input stream with the specified buffer size.

**Parameters:** in

- the input stream
**Parameters:** size

- the input buffer size
**Throws:** ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

size <= 0

---

#### GZIPInputStream

public GZIPInputStream​(

InputStream

in,
int size)
throws

IOException

Creates a new input stream with the specified buffer size.

GZIPInputStream

```java
public GZIPInputStream​(
InputStream
in)
throws
IOException
```

Creates a new input stream with a default buffer size.

**Parameters:** in

- the input stream
**Throws:** ZipException

- if a GZIP format error has occurred or the
compression method used is unsupported
**Throws:** IOException

- if an I/O error has occurred

---

#### GZIPInputStream

public GZIPInputStream​(

InputStream

in)
throws

IOException

Creates a new input stream with a default buffer size.

Method Detail

- read

```java
public int read​(byte[] buf,
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

InflaterInputStream
**Parameters:** buf

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
compressed input stream is reached
**Throws:** NullPointerException

- If

buf

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

buf.length - off
**Throws:** ZipException

- if the compressed input data is corrupt.
**Throws:** IOException

- if an I/O error has occurred.
**See Also:** FilterInputStream.in

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

InflaterInputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### Method Detail

read

```java
public int read​(byte[] buf,
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

InflaterInputStream
**Parameters:** buf

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
compressed input stream is reached
**Throws:** NullPointerException

- If

buf

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

buf.length - off
**Throws:** ZipException

- if the compressed input data is corrupt.
**Throws:** IOException

- if an I/O error has occurred.
**See Also:** FilterInputStream.in

---

#### read

public int read​(byte[] buf,
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

InflaterInputStream
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

---

