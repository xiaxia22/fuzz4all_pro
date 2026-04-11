# Class FilterReader

**Source:** `java.base\java\io\FilterReader.html`

### Class Description

```java
public abstract class
FilterReader

extends
Reader
```

Abstract class for reading filtered character streams.
The abstract class

FilterReader

itself
provides default methods that pass all requests to
the contained stream. Subclasses of

FilterReader

should override some of these methods and may also provide
additional methods and fields.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

#### protected
Reader
in

The underlying character-input stream.

---

### Constructor Details

#### protected FilterReader​(
Reader
in)

Creates a new filtered reader.

**Parameters:**
- in

- a Reader object providing the underlying stream.

**Throws:**
- NullPointerException

- if

in

is

null

---

### Method Details

#### public int read()
throws
IOException

Reads a single character.

**Overrides:**
- read

in class

Reader

**Returns:**
- The character read, as an integer in the range 0 to 65535
(

0x00-0xffff

), or -1 if the end of the stream has
been reached

**Throws:**
- IOException

- If an I/O error occurs

---

#### public int read​(char[] cbuf,
int off,
int len)
throws
IOException

Reads characters into a portion of an array.

**Specified by:**
- read

in class

Reader

**Parameters:**
- cbuf

- Destination buffer
- off

- Offset at which to start storing characters
- len

- Maximum number of characters to read

**Returns:**
- The number of characters read, or -1 if the end of the
stream has been reached

**Throws:**
- IOException

- If an I/O error occurs
- IndexOutOfBoundsException

- If an I/O error occurs

---

#### public long skip​(long n)
throws
IOException

Skips characters.

**Overrides:**
- skip

in class

Reader

**Parameters:**
- n

- The number of characters to skip

**Returns:**
- The number of characters actually skipped

**Throws:**
- IOException

- If an I/O error occurs

---

#### public boolean ready()
throws
IOException

Tells whether this stream is ready to be read.

**Overrides:**
- ready

in class

Reader

**Returns:**
- True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.

**Throws:**
- IOException

- If an I/O error occurs

---

#### public boolean markSupported()

Tells whether this stream supports the mark() operation.

**Overrides:**
- markSupported

in class

Reader

**Returns:**
- true if and only if this stream supports the mark operation.

---

#### public void mark​(int readAheadLimit)
throws
IOException

Marks the present position in the stream.

**Overrides:**
- mark

in class

Reader

**Parameters:**
- readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.

**Throws:**
- IOException

- If an I/O error occurs

---

#### public void reset()
throws
IOException

Resets the stream.

**Overrides:**
- reset

in class

Reader

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class FilterReader

java.lang.Object

- java.io.Reader
- - java.io.FilterReader

java.io.Reader

- java.io.FilterReader

java.io.FilterReader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

**Direct Known Subclasses:** PushbackReader

```java
public abstract class
FilterReader

extends
Reader
```

Abstract class for reading filtered character streams.
The abstract class

FilterReader

itself
provides default methods that pass all requests to
the contained stream. Subclasses of

FilterReader

should override some of these methods and may also provide
additional methods and fields.

**Since:** 1.1

public abstract class

FilterReader

extends

Reader

Abstract class for reading filtered character streams.
The abstract class

FilterReader

itself
provides default methods that pass all requests to
the contained stream. Subclasses of

FilterReader

should override some of these methods and may also provide
additional methods and fields.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Reader

in

The underlying character-input stream.

- Fields declared in class java.io.

Reader

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FilterReader

​(

Reader

in)

Creates a new filtered reader.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

mark

​(int readAheadLimit)

Marks the present position in the stream.

boolean

markSupported

()

Tells whether this stream supports the mark() operation.

int

read

()

Reads a single character.

int

read

​(char[] cbuf,
int off,
int len)

Reads characters into a portion of an array.

boolean

ready

()

Tells whether this stream is ready to be read.

void

reset

()

Resets the stream.

long

skip

​(long n)

Skips characters.

- Methods declared in class java.io.

Reader

close

,

nullReader

,

read

,

read

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

Reader

in

The underlying character-input stream.

- Fields declared in class java.io.

Reader

lock

---

#### Field Summary

The underlying character-input stream.

Fields declared in class java.io.

Reader

lock

---

#### Fields declared in class java.io. Reader

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FilterReader

​(

Reader

in)

Creates a new filtered reader.

---

#### Constructor Summary

Creates a new filtered reader.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

mark

​(int readAheadLimit)

Marks the present position in the stream.

boolean

markSupported

()

Tells whether this stream supports the mark() operation.

int

read

()

Reads a single character.

int

read

​(char[] cbuf,
int off,
int len)

Reads characters into a portion of an array.

boolean

ready

()

Tells whether this stream is ready to be read.

void

reset

()

Resets the stream.

long

skip

​(long n)

Skips characters.

- Methods declared in class java.io.

Reader

close

,

nullReader

,

read

,

read

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

Marks the present position in the stream.

Tells whether this stream supports the mark() operation.

Reads a single character.

Reads characters into a portion of an array.

Tells whether this stream is ready to be read.

Resets the stream.

Skips characters.

Methods declared in class java.io.

Reader

close

,

nullReader

,

read

,

read

,

transferTo

---

#### Methods declared in class java.io. Reader

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

- in

```java
protected
Reader
in
```

The underlying character-input stream.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FilterReader

```java
protected FilterReader​(
Reader
in)
```

Creates a new filtered reader.

**Parameters:** in

- a Reader object providing the underlying stream.
**Throws:** NullPointerException

- if

in

is

null

============ METHOD DETAIL ==========

- Method Detail

- read

```java
public int read()
throws
IOException
```

Reads a single character.

**Overrides:** read

in class

Reader
**Returns:** The character read, as an integer in the range 0 to 65535
(

0x00-0xffff

), or -1 if the end of the stream has
been reached
**Throws:** IOException

- If an I/O error occurs

- read

```java
public int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads characters into a portion of an array.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- Destination buffer
**Parameters:** off

- Offset at which to start storing characters
**Parameters:** len

- Maximum number of characters to read
**Returns:** The number of characters read, or -1 if the end of the
stream has been reached
**Throws:** IOException

- If an I/O error occurs
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips characters.

**Overrides:** skip

in class

Reader
**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IOException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- If an I/O error occurs

- markSupported

```java
public boolean markSupported()
```

Tells whether this stream supports the mark() operation.

**Overrides:** markSupported

in class

Reader
**Returns:** true if and only if this stream supports the mark operation.

- mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Marks the present position in the stream.

**Overrides:** mark

in class

Reader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.
**Throws:** IOException

- If an I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Resets the stream.

**Overrides:** reset

in class

Reader
**Throws:** IOException

- If an I/O error occurs

Field Detail

- in

```java
protected
Reader
in
```

The underlying character-input stream.

---

#### Field Detail

in

```java
protected
Reader
in
```

The underlying character-input stream.

---

#### in

protected

Reader

in

The underlying character-input stream.

Constructor Detail

- FilterReader

```java
protected FilterReader​(
Reader
in)
```

Creates a new filtered reader.

**Parameters:** in

- a Reader object providing the underlying stream.
**Throws:** NullPointerException

- if

in

is

null

---

#### Constructor Detail

FilterReader

```java
protected FilterReader​(
Reader
in)
```

Creates a new filtered reader.

**Parameters:** in

- a Reader object providing the underlying stream.
**Throws:** NullPointerException

- if

in

is

null

---

#### FilterReader

protected FilterReader​(

Reader

in)

Creates a new filtered reader.

Method Detail

- read

```java
public int read()
throws
IOException
```

Reads a single character.

**Overrides:** read

in class

Reader
**Returns:** The character read, as an integer in the range 0 to 65535
(

0x00-0xffff

), or -1 if the end of the stream has
been reached
**Throws:** IOException

- If an I/O error occurs

- read

```java
public int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads characters into a portion of an array.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- Destination buffer
**Parameters:** off

- Offset at which to start storing characters
**Parameters:** len

- Maximum number of characters to read
**Returns:** The number of characters read, or -1 if the end of the
stream has been reached
**Throws:** IOException

- If an I/O error occurs
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips characters.

**Overrides:** skip

in class

Reader
**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IOException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- If an I/O error occurs

- markSupported

```java
public boolean markSupported()
```

Tells whether this stream supports the mark() operation.

**Overrides:** markSupported

in class

Reader
**Returns:** true if and only if this stream supports the mark operation.

- mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Marks the present position in the stream.

**Overrides:** mark

in class

Reader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.
**Throws:** IOException

- If an I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Resets the stream.

**Overrides:** reset

in class

Reader
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

read

```java
public int read()
throws
IOException
```

Reads a single character.

**Overrides:** read

in class

Reader
**Returns:** The character read, as an integer in the range 0 to 65535
(

0x00-0xffff

), or -1 if the end of the stream has
been reached
**Throws:** IOException

- If an I/O error occurs

---

#### read

public int read()
throws

IOException

Reads a single character.

read

```java
public int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads characters into a portion of an array.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- Destination buffer
**Parameters:** off

- Offset at which to start storing characters
**Parameters:** len

- Maximum number of characters to read
**Returns:** The number of characters read, or -1 if the end of the
stream has been reached
**Throws:** IOException

- If an I/O error occurs
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

---

#### read

public int read​(char[] cbuf,
int off,
int len)
throws

IOException

Reads characters into a portion of an array.

skip

```java
public long skip​(long n)
throws
IOException
```

Skips characters.

**Overrides:** skip

in class

Reader
**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IOException

- If an I/O error occurs

---

#### skip

public long skip​(long n)
throws

IOException

Skips characters.

ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- If an I/O error occurs

---

#### ready

public boolean ready()
throws

IOException

Tells whether this stream is ready to be read.

markSupported

```java
public boolean markSupported()
```

Tells whether this stream supports the mark() operation.

**Overrides:** markSupported

in class

Reader
**Returns:** true if and only if this stream supports the mark operation.

---

#### markSupported

public boolean markSupported()

Tells whether this stream supports the mark() operation.

mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Marks the present position in the stream.

**Overrides:** mark

in class

Reader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.
**Throws:** IOException

- If an I/O error occurs

---

#### mark

public void mark​(int readAheadLimit)
throws

IOException

Marks the present position in the stream.

reset

```java
public void reset()
throws
IOException
```

Resets the stream.

**Overrides:** reset

in class

Reader
**Throws:** IOException

- If an I/O error occurs

---

#### reset

public void reset()
throws

IOException

Resets the stream.

---

