# Class BufferedOutputStream

**Source:** `java.base\java\io\BufferedOutputStream.html`

### Class Description

```java
public class
BufferedOutputStream

extends
FilterOutputStream
```

The class implements a buffered output stream. By setting up such
an output stream, an application can write bytes to the underlying
output stream without necessarily causing a call to the underlying
system for each byte written.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

#### protected byte[] buf

The internal buffer where data is stored.

---

#### protected int count

The number of valid bytes in the buffer. This value is always
in the range

0

through

buf.length

; elements

buf[0]

through

buf[count-1]

contain valid
byte data.

---

### Constructor Details

#### public BufferedOutputStream​(
OutputStream
out)

Creates a new buffered output stream to write data to the
specified underlying output stream.

**Parameters:**
- out

- the underlying output stream.

---

#### public BufferedOutputStream​(
OutputStream
out,
int size)

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

**Parameters:**
- out

- the underlying output stream.
- size

- the buffer size.

**Throws:**
- IllegalArgumentException

- if size <= 0.

---

### Method Details

#### public void write​(int b)
throws
IOException

Writes the specified byte to this buffered output stream.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the byte to be written.

**Throws:**
- IOException

- if an I/O error occurs.

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

to this buffered output stream.

Ordinarily this method stores bytes from the given array into this
stream's buffer, flushing the buffer to the underlying output stream as
needed. If the requested length is at least as large as this stream's
buffer, however, then this method will flush the buffer and write the
bytes directly to the underlying output stream. Thus redundant

BufferedOutputStream

s will not copy data unnecessarily.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the data.
- off

- the start offset in the data.
- len

- the number of bytes to write.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.write(int)

---

#### public void flush()
throws
IOException

Flushes this buffered output stream. This forces any buffered
output bytes to be written out to the underlying output stream.

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

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

### Additional Sections

#### Class BufferedOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.io.BufferedOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.io.BufferedOutputStream

java.io.FilterOutputStream

- java.io.BufferedOutputStream

java.io.BufferedOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
BufferedOutputStream

extends
FilterOutputStream
```

The class implements a buffered output stream. By setting up such
an output stream, an application can write bytes to the underlying
output stream without necessarily causing a call to the underlying
system for each byte written.

**Since:** 1.0

public class

BufferedOutputStream

extends

FilterOutputStream

The class implements a buffered output stream. By setting up such
an output stream, an application can write bytes to the underlying
output stream without necessarily causing a call to the underlying
system for each byte written.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

buf

The internal buffer where data is stored.

protected int

count

The number of valid bytes in the buffer.

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BufferedOutputStream

​(

OutputStream

out)

Creates a new buffered output stream to write data to the
specified underlying output stream.

BufferedOutputStream

​(

OutputStream

out,
int size)

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes this buffered output stream.

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

to this buffered output stream.

void

write

​(int b)

Writes the specified byte to this buffered output stream.

- Methods declared in class java.io.

FilterOutputStream

close

,

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

The internal buffer where data is stored.

protected int

count

The number of valid bytes in the buffer.

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

The internal buffer where data is stored.

The number of valid bytes in the buffer.

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

BufferedOutputStream

​(

OutputStream

out)

Creates a new buffered output stream to write data to the
specified underlying output stream.

BufferedOutputStream

​(

OutputStream

out,
int size)

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

---

#### Constructor Summary

Creates a new buffered output stream to write data to the
specified underlying output stream.

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes this buffered output stream.

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

to this buffered output stream.

void

write

​(int b)

Writes the specified byte to this buffered output stream.

- Methods declared in class java.io.

FilterOutputStream

close

,

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

Flushes this buffered output stream.

Writes

len

bytes from the specified byte array
starting at offset

off

to this buffered output stream.

Writes the specified byte to this buffered output stream.

Methods declared in class java.io.

FilterOutputStream

close

,

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

- buf

```java
protected byte[] buf
```

The internal buffer where data is stored.

- count

```java
protected int count
```

The number of valid bytes in the buffer. This value is always
in the range

0

through

buf.length

; elements

buf[0]

through

buf[count-1]

contain valid
byte data.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BufferedOutputStream

```java
public BufferedOutputStream​(
OutputStream
out)
```

Creates a new buffered output stream to write data to the
specified underlying output stream.

**Parameters:** out

- the underlying output stream.

- BufferedOutputStream

```java
public BufferedOutputStream​(
OutputStream
out,
int size)
```

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

**Parameters:** out

- the underlying output stream.
**Parameters:** size

- the buffer size.
**Throws:** IllegalArgumentException

- if size <= 0.

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this buffered output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be written.
**Throws:** IOException

- if an I/O error occurs.

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

to this buffered output stream.

Ordinarily this method stores bytes from the given array into this
stream's buffer, flushing the buffer to the underlying output stream as
needed. If the requested length is at least as large as this stream's
buffer, however, then this method will flush the buffer and write the
bytes directly to the underlying output stream. Thus redundant

BufferedOutputStream

s will not copy data unnecessarily.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.write(int)

- flush

```java
public void flush()
throws
IOException
```

Flushes this buffered output stream. This forces any buffered
output bytes to be written out to the underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

Field Detail

- buf

```java
protected byte[] buf
```

The internal buffer where data is stored.

- count

```java
protected int count
```

The number of valid bytes in the buffer. This value is always
in the range

0

through

buf.length

; elements

buf[0]

through

buf[count-1]

contain valid
byte data.

---

#### Field Detail

buf

```java
protected byte[] buf
```

The internal buffer where data is stored.

---

#### buf

protected byte[] buf

The internal buffer where data is stored.

count

```java
protected int count
```

The number of valid bytes in the buffer. This value is always
in the range

0

through

buf.length

; elements

buf[0]

through

buf[count-1]

contain valid
byte data.

---

#### count

protected int count

The number of valid bytes in the buffer. This value is always
in the range

0

through

buf.length

; elements

buf[0]

through

buf[count-1]

contain valid
byte data.

Constructor Detail

- BufferedOutputStream

```java
public BufferedOutputStream​(
OutputStream
out)
```

Creates a new buffered output stream to write data to the
specified underlying output stream.

**Parameters:** out

- the underlying output stream.

- BufferedOutputStream

```java
public BufferedOutputStream​(
OutputStream
out,
int size)
```

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

**Parameters:** out

- the underlying output stream.
**Parameters:** size

- the buffer size.
**Throws:** IllegalArgumentException

- if size <= 0.

---

#### Constructor Detail

BufferedOutputStream

```java
public BufferedOutputStream​(
OutputStream
out)
```

Creates a new buffered output stream to write data to the
specified underlying output stream.

**Parameters:** out

- the underlying output stream.

---

#### BufferedOutputStream

public BufferedOutputStream​(

OutputStream

out)

Creates a new buffered output stream to write data to the
specified underlying output stream.

BufferedOutputStream

```java
public BufferedOutputStream​(
OutputStream
out,
int size)
```

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

**Parameters:** out

- the underlying output stream.
**Parameters:** size

- the buffer size.
**Throws:** IllegalArgumentException

- if size <= 0.

---

#### BufferedOutputStream

public BufferedOutputStream​(

OutputStream

out,
int size)

Creates a new buffered output stream to write data to the
specified underlying output stream with the specified buffer
size.

Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this buffered output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be written.
**Throws:** IOException

- if an I/O error occurs.

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

to this buffered output stream.

Ordinarily this method stores bytes from the given array into this
stream's buffer, flushing the buffer to the underlying output stream as
needed. If the requested length is at least as large as this stream's
buffer, however, then this method will flush the buffer and write the
bytes directly to the underlying output stream. Thus redundant

BufferedOutputStream

s will not copy data unnecessarily.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.write(int)

- flush

```java
public void flush()
throws
IOException
```

Flushes this buffered output stream. This forces any buffered
output bytes to be written out to the underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### Method Detail

write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this buffered output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be written.
**Throws:** IOException

- if an I/O error occurs.

---

#### write

public void write​(int b)
throws

IOException

Writes the specified byte to this buffered output stream.

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

to this buffered output stream.

Ordinarily this method stores bytes from the given array into this
stream's buffer, flushing the buffer to the underlying output stream as
needed. If the requested length is at least as large as this stream's
buffer, however, then this method will flush the buffer and write the
bytes directly to the underlying output stream. Thus redundant

BufferedOutputStream

s will not copy data unnecessarily.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.write(int)

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

to this buffered output stream.

Ordinarily this method stores bytes from the given array into this
stream's buffer, flushing the buffer to the underlying output stream as
needed. If the requested length is at least as large as this stream's
buffer, however, then this method will flush the buffer and write the
bytes directly to the underlying output stream. Thus redundant

BufferedOutputStream

s will not copy data unnecessarily.

Ordinarily this method stores bytes from the given array into this
stream's buffer, flushing the buffer to the underlying output stream as
needed. If the requested length is at least as large as this stream's
buffer, however, then this method will flush the buffer and write the
bytes directly to the underlying output stream. Thus redundant

BufferedOutputStream

s will not copy data unnecessarily.

flush

```java
public void flush()
throws
IOException
```

Flushes this buffered output stream. This forces any buffered
output bytes to be written out to the underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### flush

public void flush()
throws

IOException

Flushes this buffered output stream. This forces any buffered
output bytes to be written out to the underlying output stream.

---

