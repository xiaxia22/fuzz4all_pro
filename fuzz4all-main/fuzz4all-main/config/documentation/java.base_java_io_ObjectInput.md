# Interface ObjectInput

**Source:** `java.base\java\io\ObjectInput.html`

### Class Description

```java
public interface
ObjectInput

extends
DataInput
,
AutoCloseable
```

ObjectInput extends the DataInput interface to include the reading of
objects. DataInput includes methods for the input of primitive types,
ObjectInput extends that interface to include objects, arrays, and Strings.

**All Superinterfaces:** AutoCloseable

,

DataInput

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
readObject()
throws
ClassNotFoundException
,

IOException

Read and return an object. The class that implements this interface
defines where the object is "read" from.

**Returns:**
- the object read from the stream

**Throws:**
- ClassNotFoundException

- If the class of a serialized
object cannot be found.
- IOException

- If any of the usual Input/Output
related exceptions occur.

---

#### int read()
throws
IOException

Reads a byte of data. This method will block if no input is
available.

**Returns:**
- the byte read, or -1 if the end of the
stream is reached.

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### int read​(byte[] b)
throws
IOException

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:**
- b

- the buffer into which the data is read

**Returns:**
- the actual number of bytes read, -1 is
returned when the end of the stream is reached.

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### int read​(byte[] b,
int off,
int len)
throws
IOException

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:**
- b

- the buffer into which the data is read
- off

- the start offset of the data
- len

- the maximum number of bytes read

**Returns:**
- the actual number of bytes read, -1 is
returned when the end of the stream is reached.

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### long skip​(long n)
throws
IOException

Skips n bytes of input.

**Parameters:**
- n

- the number of bytes to be skipped

**Returns:**
- the actual number of bytes skipped.

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### int available()
throws
IOException

Returns the number of bytes that can be read
without blocking.

**Returns:**
- the number of available bytes.

**Throws:**
- IOException

- If an I/O error has occurred.

---

#### void close()
throws
IOException

Closes the input stream. Must be called
to release any resources associated with
the stream.

**Specified by:**
- close

in interface

AutoCloseable

**Throws:**
- IOException

- If an I/O error has occurred.

---

### Additional Sections

#### Interface ObjectInput

**All Superinterfaces:** AutoCloseable

,

DataInput

**All Known Implementing Classes:** ObjectInputStream

```java
public interface
ObjectInput

extends
DataInput
,
AutoCloseable
```

ObjectInput extends the DataInput interface to include the reading of
objects. DataInput includes methods for the input of primitive types,
ObjectInput extends that interface to include objects, arrays, and Strings.

**Since:** 1.1
**See Also:** InputStream

,

ObjectOutputStream

,

ObjectInputStream

public interface

ObjectInput

extends

DataInput

,

AutoCloseable

ObjectInput extends the DataInput interface to include the reading of
objects. DataInput includes methods for the input of primitive types,
ObjectInput extends that interface to include objects, arrays, and Strings.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

available

()

Returns the number of bytes that can be read
without blocking.

void

close

()

Closes the input stream.

int

read

()

Reads a byte of data.

int

read

​(byte[] b)

Reads into an array of bytes.

int

read

​(byte[] b,
int off,
int len)

Reads into an array of bytes.

Object

readObject

()

Read and return an object.

long

skip

​(long n)

Skips n bytes of input.

- Methods declared in interface java.io.

DataInput

readBoolean

,

readByte

,

readChar

,

readDouble

,

readFloat

,

readFully

,

readFully

,

readInt

,

readLine

,

readLong

,

readShort

,

readUnsignedByte

,

readUnsignedShort

,

readUTF

,

skipBytes

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

available

()

Returns the number of bytes that can be read
without blocking.

void

close

()

Closes the input stream.

int

read

()

Reads a byte of data.

int

read

​(byte[] b)

Reads into an array of bytes.

int

read

​(byte[] b,
int off,
int len)

Reads into an array of bytes.

Object

readObject

()

Read and return an object.

long

skip

​(long n)

Skips n bytes of input.

- Methods declared in interface java.io.

DataInput

readBoolean

,

readByte

,

readChar

,

readDouble

,

readFloat

,

readFully

,

readFully

,

readInt

,

readLine

,

readLong

,

readShort

,

readUnsignedByte

,

readUnsignedShort

,

readUTF

,

skipBytes

---

#### Method Summary

Returns the number of bytes that can be read
without blocking.

Closes the input stream.

Reads a byte of data.

Reads into an array of bytes.

Read and return an object.

Skips n bytes of input.

Methods declared in interface java.io.

DataInput

readBoolean

,

readByte

,

readChar

,

readDouble

,

readFloat

,

readFully

,

readFully

,

readInt

,

readLine

,

readLong

,

readShort

,

readUnsignedByte

,

readUnsignedShort

,

readUTF

,

skipBytes

---

#### Methods declared in interface java.io. DataInput

============ METHOD DETAIL ==========

- Method Detail

- readObject

```java
Object
readObject()
throws
ClassNotFoundException
,

IOException
```

Read and return an object. The class that implements this interface
defines where the object is "read" from.

**Returns:** the object read from the stream
**Throws:** ClassNotFoundException

- If the class of a serialized
object cannot be found.
**Throws:** IOException

- If any of the usual Input/Output
related exceptions occur.

- read

```java
int read()
throws
IOException
```

Reads a byte of data. This method will block if no input is
available.

**Returns:** the byte read, or -1 if the end of the
stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

- read

```java
int read​(byte[] b)
throws
IOException
```

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:** b

- the buffer into which the data is read
**Returns:** the actual number of bytes read, -1 is
returned when the end of the stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

- read

```java
int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, -1 is
returned when the end of the stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

- skip

```java
long skip​(long n)
throws
IOException
```

Skips n bytes of input.

**Parameters:** n

- the number of bytes to be skipped
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- If an I/O error has occurred.

- available

```java
int available()
throws
IOException
```

Returns the number of bytes that can be read
without blocking.

**Returns:** the number of available bytes.
**Throws:** IOException

- If an I/O error has occurred.

- close

```java
void close()
throws
IOException
```

Closes the input stream. Must be called
to release any resources associated with
the stream.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- If an I/O error has occurred.

Method Detail

- readObject

```java
Object
readObject()
throws
ClassNotFoundException
,

IOException
```

Read and return an object. The class that implements this interface
defines where the object is "read" from.

**Returns:** the object read from the stream
**Throws:** ClassNotFoundException

- If the class of a serialized
object cannot be found.
**Throws:** IOException

- If any of the usual Input/Output
related exceptions occur.

- read

```java
int read()
throws
IOException
```

Reads a byte of data. This method will block if no input is
available.

**Returns:** the byte read, or -1 if the end of the
stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

- read

```java
int read​(byte[] b)
throws
IOException
```

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:** b

- the buffer into which the data is read
**Returns:** the actual number of bytes read, -1 is
returned when the end of the stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

- read

```java
int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, -1 is
returned when the end of the stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

- skip

```java
long skip​(long n)
throws
IOException
```

Skips n bytes of input.

**Parameters:** n

- the number of bytes to be skipped
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- If an I/O error has occurred.

- available

```java
int available()
throws
IOException
```

Returns the number of bytes that can be read
without blocking.

**Returns:** the number of available bytes.
**Throws:** IOException

- If an I/O error has occurred.

- close

```java
void close()
throws
IOException
```

Closes the input stream. Must be called
to release any resources associated with
the stream.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- If an I/O error has occurred.

---

#### Method Detail

readObject

```java
Object
readObject()
throws
ClassNotFoundException
,

IOException
```

Read and return an object. The class that implements this interface
defines where the object is "read" from.

**Returns:** the object read from the stream
**Throws:** ClassNotFoundException

- If the class of a serialized
object cannot be found.
**Throws:** IOException

- If any of the usual Input/Output
related exceptions occur.

---

#### readObject

Object

readObject()
throws

ClassNotFoundException

,

IOException

Read and return an object. The class that implements this interface
defines where the object is "read" from.

read

```java
int read()
throws
IOException
```

Reads a byte of data. This method will block if no input is
available.

**Returns:** the byte read, or -1 if the end of the
stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

---

#### read

int read()
throws

IOException

Reads a byte of data. This method will block if no input is
available.

read

```java
int read​(byte[] b)
throws
IOException
```

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:** b

- the buffer into which the data is read
**Returns:** the actual number of bytes read, -1 is
returned when the end of the stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

---

#### read

int read​(byte[] b)
throws

IOException

Reads into an array of bytes. This method will
block until some input is available.

read

```java
int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads into an array of bytes. This method will
block until some input is available.

**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, -1 is
returned when the end of the stream is reached.
**Throws:** IOException

- If an I/O error has occurred.

---

#### read

int read​(byte[] b,
int off,
int len)
throws

IOException

Reads into an array of bytes. This method will
block until some input is available.

skip

```java
long skip​(long n)
throws
IOException
```

Skips n bytes of input.

**Parameters:** n

- the number of bytes to be skipped
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- If an I/O error has occurred.

---

#### skip

long skip​(long n)
throws

IOException

Skips n bytes of input.

available

```java
int available()
throws
IOException
```

Returns the number of bytes that can be read
without blocking.

**Returns:** the number of available bytes.
**Throws:** IOException

- If an I/O error has occurred.

---

#### available

int available()
throws

IOException

Returns the number of bytes that can be read
without blocking.

close

```java
void close()
throws
IOException
```

Closes the input stream. Must be called
to release any resources associated with
the stream.

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

Closes the input stream. Must be called
to release any resources associated with
the stream.

---

