# Class CheckedInputStream

**Source:** `java.base\java\util\zip\CheckedInputStream.html`

### Class Description

```java
public class
CheckedInputStream

extends
FilterInputStream
```

An input stream that also maintains a checksum of the data being read.
The checksum can then be used to verify the integrity of the input data.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CheckedInputStream​(
InputStream
in,

Checksum
cksum)

Creates an input stream using the specified Checksum.

**Parameters:**
- in

- the input stream
- cksum

- the Checksum

---

### Method Details

#### public int read()
throws
IOException

Reads a byte. Will block if no input is available.

**Overrides:**
- read

in class

FilterInputStream

**Returns:**
- the byte read, or -1 if the end of the stream is reached.

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

#### public int read​(byte[] buf,
int off,
int len)
throws
IOException

Reads into an array of bytes. If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- buf

- the buffer into which the data is read
- off

- the start offset in the destination array

b
- len

- the maximum number of bytes read

**Returns:**
- the actual number of bytes read, or -1 if the end
of the stream is reached.

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
- IOException

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

#### public long skip​(long n)
throws
IOException

Skips specified number of bytes of input.

**Overrides:**
- skip

in class

FilterInputStream

**Parameters:**
- n

- the number of bytes to skip

**Returns:**
- the actual number of bytes skipped

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public
Checksum
getChecksum()

Returns the Checksum for this input stream.

**Returns:**
- the Checksum value

---

### Additional Sections

#### Class CheckedInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - java.util.zip.CheckedInputStream

java.io.InputStream

- java.io.FilterInputStream
- - java.util.zip.CheckedInputStream

java.io.FilterInputStream

- java.util.zip.CheckedInputStream

java.util.zip.CheckedInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
CheckedInputStream

extends
FilterInputStream
```

An input stream that also maintains a checksum of the data being read.
The checksum can then be used to verify the integrity of the input data.

**Since:** 1.1
**See Also:** Checksum

public class

CheckedInputStream

extends

FilterInputStream

An input stream that also maintains a checksum of the data being read.
The checksum can then be used to verify the integrity of the input data.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CheckedInputStream

​(

InputStream

in,

Checksum

cksum)

Creates an input stream using the specified Checksum.

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

Returns the Checksum for this input stream.

int

read

()

Reads a byte.

int

read

​(byte[] buf,
int off,
int len)

Reads into an array of bytes.

long

skip

​(long n)

Skips specified number of bytes of input.

- Methods declared in class java.io.

FilterInputStream

available

,

close

,

mark

,

markSupported

,

read

,

reset

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

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Constructor

Description

CheckedInputStream

​(

InputStream

in,

Checksum

cksum)

Creates an input stream using the specified Checksum.

---

#### Constructor Summary

Creates an input stream using the specified Checksum.

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

Returns the Checksum for this input stream.

int

read

()

Reads a byte.

int

read

​(byte[] buf,
int off,
int len)

Reads into an array of bytes.

long

skip

​(long n)

Skips specified number of bytes of input.

- Methods declared in class java.io.

FilterInputStream

available

,

close

,

mark

,

markSupported

,

read

,

reset

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

Returns the Checksum for this input stream.

Reads a byte.

Reads into an array of bytes.

Skips specified number of bytes of input.

Methods declared in class java.io.

FilterInputStream

available

,

close

,

mark

,

markSupported

,

read

,

reset

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CheckedInputStream

```java
public CheckedInputStream​(
InputStream
in,

Checksum
cksum)
```

Creates an input stream using the specified Checksum.

**Parameters:** in

- the input stream
**Parameters:** cksum

- the Checksum

============ METHOD DETAIL ==========

- Method Detail

- read

```java
public int read()
throws
IOException
```

Reads a byte. Will block if no input is available.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read, or -1 if the end of the stream is reached.
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] buf,
int off,
int len)
throws
IOException
```

Reads into an array of bytes. If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:** read

in class

FilterInputStream
**Parameters:** buf

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end
of the stream is reached.
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
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes of input.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped
**Throws:** IOException

- if an I/O error has occurred

- getChecksum

```java
public
Checksum
getChecksum()
```

Returns the Checksum for this input stream.

**Returns:** the Checksum value

Constructor Detail

- CheckedInputStream

```java
public CheckedInputStream​(
InputStream
in,

Checksum
cksum)
```

Creates an input stream using the specified Checksum.

**Parameters:** in

- the input stream
**Parameters:** cksum

- the Checksum

---

#### Constructor Detail

CheckedInputStream

```java
public CheckedInputStream​(
InputStream
in,

Checksum
cksum)
```

Creates an input stream using the specified Checksum.

**Parameters:** in

- the input stream
**Parameters:** cksum

- the Checksum

---

#### CheckedInputStream

public CheckedInputStream​(

InputStream

in,

Checksum

cksum)

Creates an input stream using the specified Checksum.

Method Detail

- read

```java
public int read()
throws
IOException
```

Reads a byte. Will block if no input is available.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read, or -1 if the end of the stream is reached.
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] buf,
int off,
int len)
throws
IOException
```

Reads into an array of bytes. If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:** read

in class

FilterInputStream
**Parameters:** buf

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end
of the stream is reached.
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
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes of input.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped
**Throws:** IOException

- if an I/O error has occurred

- getChecksum

```java
public
Checksum
getChecksum()
```

Returns the Checksum for this input stream.

**Returns:** the Checksum value

---

#### Method Detail

read

```java
public int read()
throws
IOException
```

Reads a byte. Will block if no input is available.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read, or -1 if the end of the stream is reached.
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### read

public int read()
throws

IOException

Reads a byte. Will block if no input is available.

read

```java
public int read​(byte[] buf,
int off,
int len)
throws
IOException
```

Reads into an array of bytes. If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:** read

in class

FilterInputStream
**Parameters:** buf

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end
of the stream is reached.
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
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### read

public int read​(byte[] buf,
int off,
int len)
throws

IOException

Reads into an array of bytes. If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes of input.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped
**Throws:** IOException

- if an I/O error has occurred

---

#### skip

public long skip​(long n)
throws

IOException

Skips specified number of bytes of input.

getChecksum

```java
public
Checksum
getChecksum()
```

Returns the Checksum for this input stream.

**Returns:** the Checksum value

---

#### getChecksum

public

Checksum

getChecksum()

Returns the Checksum for this input stream.

---

