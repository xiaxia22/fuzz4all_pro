# Interface ObjectOutput

**Source:** `java.base\java\io\ObjectOutput.html`

### Class Description

```java
public interface
ObjectOutput

extends
DataOutput
,
AutoCloseable
```

ObjectOutput extends the DataOutput interface to include writing of objects.
DataOutput includes methods for output of primitive types, ObjectOutput
extends that interface to include objects, arrays, and Strings.

**All Superinterfaces:** AutoCloseable

,

DataOutput

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void writeObject​(
Object
obj)
throws
IOException

Write an object to the underlying storage or stream. The
class that implements this interface defines how the object is
written.

**Parameters:**
- obj

- the object to be written

**Throws:**
- IOException

- Any of the usual Input/Output related exceptions.

---

#### void write​(int b)
throws
IOException

Writes a byte. This method will block until the byte is actually
written.

**Specified by:**
- write

in interface

DataOutput

**Parameters:**
- b

- the byte

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### void write​(byte[] b)
throws
IOException

Writes an array of bytes. This method will block until the bytes
are actually written.

**Specified by:**
- write

in interface

DataOutput

**Parameters:**
- b

- the data to be written

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### void write​(byte[] b,
int off,
int len)
throws
IOException

Writes a sub array of bytes.

**Specified by:**
- write

in interface

DataOutput

**Parameters:**
- b

- the data to be written
- off

- the start offset in the data
- len

- the number of bytes that are written

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### void flush()
throws
IOException

Flushes the stream. This will write any buffered
output bytes.

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### void close()
throws
IOException

Closes the stream. This method must be called
to release any resources associated with the
stream.

**Specified by:**
- close

in interface

AutoCloseable

**Throws:**
- IOException

- If an I/O error has occurred.

---

### Additional Sections

#### Interface ObjectOutput

**All Superinterfaces:** AutoCloseable

,

DataOutput

**All Known Implementing Classes:** ObjectOutputStream

```java
public interface
ObjectOutput

extends
DataOutput
,
AutoCloseable
```

ObjectOutput extends the DataOutput interface to include writing of objects.
DataOutput includes methods for output of primitive types, ObjectOutput
extends that interface to include objects, arrays, and Strings.

**Since:** 1.1
**See Also:** InputStream

,

ObjectOutputStream

,

ObjectInputStream

public interface

ObjectOutput

extends

DataOutput

,

AutoCloseable

ObjectOutput extends the DataOutput interface to include writing of objects.
DataOutput includes methods for output of primitive types, ObjectOutput
extends that interface to include objects, arrays, and Strings.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes the stream.

void

flush

()

Flushes the stream.

void

write

​(byte[] b)

Writes an array of bytes.

void

write

​(byte[] b,
int off,
int len)

Writes a sub array of bytes.

void

write

​(int b)

Writes a byte.

void

writeObject

​(

Object

obj)

Write an object to the underlying storage or stream.

- Methods declared in interface java.io.

DataOutput

writeBoolean

,

writeByte

,

writeBytes

,

writeChar

,

writeChars

,

writeDouble

,

writeFloat

,

writeInt

,

writeLong

,

writeShort

,

writeUTF

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes the stream.

void

flush

()

Flushes the stream.

void

write

​(byte[] b)

Writes an array of bytes.

void

write

​(byte[] b,
int off,
int len)

Writes a sub array of bytes.

void

write

​(int b)

Writes a byte.

void

writeObject

​(

Object

obj)

Write an object to the underlying storage or stream.

- Methods declared in interface java.io.

DataOutput

writeBoolean

,

writeByte

,

writeBytes

,

writeChar

,

writeChars

,

writeDouble

,

writeFloat

,

writeInt

,

writeLong

,

writeShort

,

writeUTF

---

#### Method Summary

Closes the stream.

Flushes the stream.

Writes an array of bytes.

Writes a sub array of bytes.

Writes a byte.

Write an object to the underlying storage or stream.

Methods declared in interface java.io.

DataOutput

writeBoolean

,

writeByte

,

writeBytes

,

writeChar

,

writeChars

,

writeDouble

,

writeFloat

,

writeInt

,

writeLong

,

writeShort

,

writeUTF

---

#### Methods declared in interface java.io. DataOutput

============ METHOD DETAIL ==========

- Method Detail

- writeObject

```java
void writeObject​(
Object
obj)
throws
IOException
```

Write an object to the underlying storage or stream. The
class that implements this interface defines how the object is
written.

**Parameters:** obj

- the object to be written
**Throws:** IOException

- Any of the usual Input/Output related exceptions.

- write

```java
void write​(int b)
throws
IOException
```

Writes a byte. This method will block until the byte is actually
written.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the byte
**Throws:** IOException

- If an I/O error has occurred.

- write

```java
void write​(byte[] b)
throws
IOException
```

Writes an array of bytes. This method will block until the bytes
are actually written.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the data to be written
**Throws:** IOException

- If an I/O error has occurred.

- write

```java
void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes a sub array of bytes.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of bytes that are written
**Throws:** IOException

- If an I/O error has occurred.

- flush

```java
void flush()
throws
IOException
```

Flushes the stream. This will write any buffered
output bytes.

**Throws:** IOException

- If an I/O error has occurred.

- close

```java
void close()
throws
IOException
```

Closes the stream. This method must be called
to release any resources associated with the
stream.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- If an I/O error has occurred.

Method Detail

- writeObject

```java
void writeObject​(
Object
obj)
throws
IOException
```

Write an object to the underlying storage or stream. The
class that implements this interface defines how the object is
written.

**Parameters:** obj

- the object to be written
**Throws:** IOException

- Any of the usual Input/Output related exceptions.

- write

```java
void write​(int b)
throws
IOException
```

Writes a byte. This method will block until the byte is actually
written.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the byte
**Throws:** IOException

- If an I/O error has occurred.

- write

```java
void write​(byte[] b)
throws
IOException
```

Writes an array of bytes. This method will block until the bytes
are actually written.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the data to be written
**Throws:** IOException

- If an I/O error has occurred.

- write

```java
void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes a sub array of bytes.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of bytes that are written
**Throws:** IOException

- If an I/O error has occurred.

- flush

```java
void flush()
throws
IOException
```

Flushes the stream. This will write any buffered
output bytes.

**Throws:** IOException

- If an I/O error has occurred.

- close

```java
void close()
throws
IOException
```

Closes the stream. This method must be called
to release any resources associated with the
stream.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- If an I/O error has occurred.

---

#### Method Detail

writeObject

```java
void writeObject​(
Object
obj)
throws
IOException
```

Write an object to the underlying storage or stream. The
class that implements this interface defines how the object is
written.

**Parameters:** obj

- the object to be written
**Throws:** IOException

- Any of the usual Input/Output related exceptions.

---

#### writeObject

void writeObject​(

Object

obj)
throws

IOException

Write an object to the underlying storage or stream. The
class that implements this interface defines how the object is
written.

write

```java
void write​(int b)
throws
IOException
```

Writes a byte. This method will block until the byte is actually
written.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the byte
**Throws:** IOException

- If an I/O error has occurred.

---

#### write

void write​(int b)
throws

IOException

Writes a byte. This method will block until the byte is actually
written.

write

```java
void write​(byte[] b)
throws
IOException
```

Writes an array of bytes. This method will block until the bytes
are actually written.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the data to be written
**Throws:** IOException

- If an I/O error has occurred.

---

#### write

void write​(byte[] b)
throws

IOException

Writes an array of bytes. This method will block until the bytes
are actually written.

write

```java
void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes a sub array of bytes.

**Specified by:** write

in interface

DataOutput
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of bytes that are written
**Throws:** IOException

- If an I/O error has occurred.

---

#### write

void write​(byte[] b,
int off,
int len)
throws

IOException

Writes a sub array of bytes.

flush

```java
void flush()
throws
IOException
```

Flushes the stream. This will write any buffered
output bytes.

**Throws:** IOException

- If an I/O error has occurred.

---

#### flush

void flush()
throws

IOException

Flushes the stream. This will write any buffered
output bytes.

close

```java
void close()
throws
IOException
```

Closes the stream. This method must be called
to release any resources associated with the
stream.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- If an I/O error has occurred.

---

#### close

void close()
throws

IOException

Closes the stream. This method must be called
to release any resources associated with the
stream.

---

