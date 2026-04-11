# Class CheckedOutputStream

**Source:** `java.base\java\util\zip\CheckedOutputStream.html`

### Class Description

```java
public class
CheckedOutputStream

extends
FilterOutputStream
```

An output stream that also maintains a checksum of the data being
written. The checksum can then be used to verify the integrity of
the output data.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CheckedOutputStream​(
OutputStream
out,

Checksum
cksum)

Creates an output stream with the specified Checksum.

**Parameters:**
- out

- the output stream
- cksum

- the checksum

---

### Method Details

#### public void write​(int b)
throws
IOException

Writes a byte. Will block until the byte is actually written.

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

Writes an array of bytes. Will block until the bytes are
actually written.

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

- the number of bytes to be written

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterOutputStream.write(int)

---

#### public
Checksum
getChecksum()

Returns the Checksum for this output stream.

**Returns:**
- the Checksum

---

### Additional Sections

#### Class CheckedOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.util.zip.CheckedOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.util.zip.CheckedOutputStream

java.io.FilterOutputStream

- java.util.zip.CheckedOutputStream

java.util.zip.CheckedOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
CheckedOutputStream

extends
FilterOutputStream
```

An output stream that also maintains a checksum of the data being
written. The checksum can then be used to verify the integrity of
the output data.

**Since:** 1.1
**See Also:** Checksum

public class

CheckedOutputStream

extends

FilterOutputStream

An output stream that also maintains a checksum of the data being
written. The checksum can then be used to verify the integrity of
the output data.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CheckedOutputStream

​(

OutputStream

out,

Checksum

cksum)

Creates an output stream with the specified Checksum.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Checksum

getChecksum

()

Returns the Checksum for this output stream.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes.

void

write

​(int b)

Writes a byte.

- Methods declared in class java.io.

FilterOutputStream

close

,

flush

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

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

CheckedOutputStream

​(

OutputStream

out,

Checksum

cksum)

Creates an output stream with the specified Checksum.

---

#### Constructor Summary

Creates an output stream with the specified Checksum.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Checksum

getChecksum

()

Returns the Checksum for this output stream.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes.

void

write

​(int b)

Writes a byte.

- Methods declared in class java.io.

FilterOutputStream

close

,

flush

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

Returns the Checksum for this output stream.

Writes an array of bytes.

Writes a byte.

Methods declared in class java.io.

FilterOutputStream

close

,

flush

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CheckedOutputStream

```java
public CheckedOutputStream​(
OutputStream
out,

Checksum
cksum)
```

Creates an output stream with the specified Checksum.

**Parameters:** out

- the output stream
**Parameters:** cksum

- the checksum

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes a byte. Will block until the byte is actually written.

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

Writes an array of bytes. Will block until the bytes are
actually written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to be written
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

- getChecksum

```java
public
Checksum
getChecksum()
```

Returns the Checksum for this output stream.

**Returns:** the Checksum

Constructor Detail

- CheckedOutputStream

```java
public CheckedOutputStream​(
OutputStream
out,

Checksum
cksum)
```

Creates an output stream with the specified Checksum.

**Parameters:** out

- the output stream
**Parameters:** cksum

- the checksum

---

#### Constructor Detail

CheckedOutputStream

```java
public CheckedOutputStream​(
OutputStream
out,

Checksum
cksum)
```

Creates an output stream with the specified Checksum.

**Parameters:** out

- the output stream
**Parameters:** cksum

- the checksum

---

#### CheckedOutputStream

public CheckedOutputStream​(

OutputStream

out,

Checksum

cksum)

Creates an output stream with the specified Checksum.

Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes a byte. Will block until the byte is actually written.

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

Writes an array of bytes. Will block until the bytes are
actually written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to be written
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

- getChecksum

```java
public
Checksum
getChecksum()
```

Returns the Checksum for this output stream.

**Returns:** the Checksum

---

#### Method Detail

write

```java
public void write​(int b)
throws
IOException
```

Writes a byte. Will block until the byte is actually written.

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

Writes a byte. Will block until the byte is actually written.

write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes. Will block until the bytes are
actually written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to be written
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

Writes an array of bytes. Will block until the bytes are
actually written.

getChecksum

```java
public
Checksum
getChecksum()
```

Returns the Checksum for this output stream.

**Returns:** the Checksum

---

#### getChecksum

public

Checksum

getChecksum()

Returns the Checksum for this output stream.

---

