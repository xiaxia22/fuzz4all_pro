# Class StringReader

**Source:** `java.base\java\io\StringReader.html`

### Class Description

```java
public class
StringReader

extends
Reader
```

A character stream whose source is a string.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringReader​(
String
s)

Creates a new string reader.

**Parameters:**
- s

- String providing the character stream.

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
- The character read, or -1 if the end of the stream has been
reached

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

- Offset at which to start writing characters
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

#### public long skip​(long ns)
throws
IOException

Skips the specified number of characters in the stream. Returns
the number of characters that were skipped.

The

ns

parameter may be negative, even though the

skip

method of the

Reader

superclass throws
an exception in this case. Negative values of

ns

cause the
stream to skip backwards. Negative return values indicate a skip
backwards. It is not possible to skip backwards past the beginning of
the string.

If the entire string has been read or skipped, then this method has
no effect and always returns 0.

**Overrides:**
- skip

in class

Reader

**Parameters:**
- ns

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
- True if the next read() is guaranteed not to block for input

**Throws:**
- IOException

- If the stream is closed

---

#### public boolean markSupported()

Tells whether this stream supports the mark() operation, which it does.

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

Marks the present position in the stream. Subsequent calls to reset()
will reposition the stream to this point.

**Overrides:**
- mark

in class

Reader

**Parameters:**
- readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. Because
the stream's input comes from a string, there
is no actual limit, so this argument must not
be negative, but is otherwise ignored.

**Throws:**
- IllegalArgumentException

- If

readAheadLimit < 0
- IOException

- If an I/O error occurs

---

#### public void reset()
throws
IOException

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

**Overrides:**
- reset

in class

Reader

**Throws:**
- IOException

- If an I/O error occurs

---

#### public void close()

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(),
ready(), mark(), or reset() invocations will throw an IOException.
Closing a previously closed stream has no effect. This method will block
while there is another thread blocking on the reader.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable
- close

in class

Reader

---

### Additional Sections

#### Class StringReader

java.lang.Object

- java.io.Reader
- - java.io.StringReader

java.io.Reader

- java.io.StringReader

java.io.StringReader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

```java
public class
StringReader

extends
Reader
```

A character stream whose source is a string.

**Since:** 1.1

public class

StringReader

extends

Reader

A character stream whose source is a string.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

Reader

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringReader

​(

String

s)

Creates a new string reader.

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

Closes the stream and releases any system resources associated with
it.

void

mark

​(int readAheadLimit)

Marks the present position in the stream.

boolean

markSupported

()

Tells whether this stream supports the mark() operation, which it does.

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

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

long

skip

​(long ns)

Skips the specified number of characters in the stream.

- Methods declared in class java.io.

Reader

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

- Fields declared in class java.io.

Reader

lock

---

#### Field Summary

Fields declared in class java.io.

Reader

lock

---

#### Fields declared in class java.io. Reader

Constructor Summary

Constructors

Constructor

Description

StringReader

​(

String

s)

Creates a new string reader.

---

#### Constructor Summary

Creates a new string reader.

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

Closes the stream and releases any system resources associated with
it.

void

mark

​(int readAheadLimit)

Marks the present position in the stream.

boolean

markSupported

()

Tells whether this stream supports the mark() operation, which it does.

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

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

long

skip

​(long ns)

Skips the specified number of characters in the stream.

- Methods declared in class java.io.

Reader

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

Closes the stream and releases any system resources associated with
it.

Marks the present position in the stream.

Tells whether this stream supports the mark() operation, which it does.

Reads a single character.

Reads characters into a portion of an array.

Tells whether this stream is ready to be read.

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

Skips the specified number of characters in the stream.

Methods declared in class java.io.

Reader

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StringReader

```java
public StringReader​(
String
s)
```

Creates a new string reader.

**Parameters:** s

- String providing the character stream.

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
**Returns:** The character read, or -1 if the end of the stream has been
reached
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

- Offset at which to start writing characters
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
public long skip​(long ns)
throws
IOException
```

Skips the specified number of characters in the stream. Returns
the number of characters that were skipped.

The

ns

parameter may be negative, even though the

skip

method of the

Reader

superclass throws
an exception in this case. Negative values of

ns

cause the
stream to skip backwards. Negative return values indicate a skip
backwards. It is not possible to skip backwards past the beginning of
the string.

If the entire string has been read or skipped, then this method has
no effect and always returns 0.

**Overrides:** skip

in class

Reader
**Parameters:** ns

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
**Returns:** True if the next read() is guaranteed not to block for input
**Throws:** IOException

- If the stream is closed

- markSupported

```java
public boolean markSupported()
```

Tells whether this stream supports the mark() operation, which it does.

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

Marks the present position in the stream. Subsequent calls to reset()
will reposition the stream to this point.

**Overrides:** mark

in class

Reader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. Because
the stream's input comes from a string, there
is no actual limit, so this argument must not
be negative, but is otherwise ignored.
**Throws:** IllegalArgumentException

- If

readAheadLimit < 0
**Throws:** IOException

- If an I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

**Overrides:** reset

in class

Reader
**Throws:** IOException

- If an I/O error occurs

- close

```java
public void close()
```

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(),
ready(), mark(), or reset() invocations will throw an IOException.
Closing a previously closed stream has no effect. This method will block
while there is another thread blocking on the reader.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Reader

Constructor Detail

- StringReader

```java
public StringReader​(
String
s)
```

Creates a new string reader.

**Parameters:** s

- String providing the character stream.

---

#### Constructor Detail

StringReader

```java
public StringReader​(
String
s)
```

Creates a new string reader.

**Parameters:** s

- String providing the character stream.

---

#### StringReader

public StringReader​(

String

s)

Creates a new string reader.

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
**Returns:** The character read, or -1 if the end of the stream has been
reached
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

- Offset at which to start writing characters
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
public long skip​(long ns)
throws
IOException
```

Skips the specified number of characters in the stream. Returns
the number of characters that were skipped.

The

ns

parameter may be negative, even though the

skip

method of the

Reader

superclass throws
an exception in this case. Negative values of

ns

cause the
stream to skip backwards. Negative return values indicate a skip
backwards. It is not possible to skip backwards past the beginning of
the string.

If the entire string has been read or skipped, then this method has
no effect and always returns 0.

**Overrides:** skip

in class

Reader
**Parameters:** ns

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
**Returns:** True if the next read() is guaranteed not to block for input
**Throws:** IOException

- If the stream is closed

- markSupported

```java
public boolean markSupported()
```

Tells whether this stream supports the mark() operation, which it does.

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

Marks the present position in the stream. Subsequent calls to reset()
will reposition the stream to this point.

**Overrides:** mark

in class

Reader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. Because
the stream's input comes from a string, there
is no actual limit, so this argument must not
be negative, but is otherwise ignored.
**Throws:** IllegalArgumentException

- If

readAheadLimit < 0
**Throws:** IOException

- If an I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

**Overrides:** reset

in class

Reader
**Throws:** IOException

- If an I/O error occurs

- close

```java
public void close()
```

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(),
ready(), mark(), or reset() invocations will throw an IOException.
Closing a previously closed stream has no effect. This method will block
while there is another thread blocking on the reader.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Reader

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
**Returns:** The character read, or -1 if the end of the stream has been
reached
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

- Offset at which to start writing characters
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
public long skip​(long ns)
throws
IOException
```

Skips the specified number of characters in the stream. Returns
the number of characters that were skipped.

The

ns

parameter may be negative, even though the

skip

method of the

Reader

superclass throws
an exception in this case. Negative values of

ns

cause the
stream to skip backwards. Negative return values indicate a skip
backwards. It is not possible to skip backwards past the beginning of
the string.

If the entire string has been read or skipped, then this method has
no effect and always returns 0.

**Overrides:** skip

in class

Reader
**Parameters:** ns

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IOException

- If an I/O error occurs

---

#### skip

public long skip​(long ns)
throws

IOException

Skips the specified number of characters in the stream. Returns
the number of characters that were skipped.

The

ns

parameter may be negative, even though the

skip

method of the

Reader

superclass throws
an exception in this case. Negative values of

ns

cause the
stream to skip backwards. Negative return values indicate a skip
backwards. It is not possible to skip backwards past the beginning of
the string.

If the entire string has been read or skipped, then this method has
no effect and always returns 0.

The

ns

parameter may be negative, even though the

skip

method of the

Reader

superclass throws
an exception in this case. Negative values of

ns

cause the
stream to skip backwards. Negative return values indicate a skip
backwards. It is not possible to skip backwards past the beginning of
the string.

If the entire string has been read or skipped, then this method has
no effect and always returns 0.

If the entire string has been read or skipped, then this method has
no effect and always returns 0.

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
**Returns:** True if the next read() is guaranteed not to block for input
**Throws:** IOException

- If the stream is closed

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

Tells whether this stream supports the mark() operation, which it does.

**Overrides:** markSupported

in class

Reader
**Returns:** true if and only if this stream supports the mark operation.

---

#### markSupported

public boolean markSupported()

Tells whether this stream supports the mark() operation, which it does.

mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Marks the present position in the stream. Subsequent calls to reset()
will reposition the stream to this point.

**Overrides:** mark

in class

Reader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. Because
the stream's input comes from a string, there
is no actual limit, so this argument must not
be negative, but is otherwise ignored.
**Throws:** IllegalArgumentException

- If

readAheadLimit < 0
**Throws:** IOException

- If an I/O error occurs

---

#### mark

public void mark​(int readAheadLimit)
throws

IOException

Marks the present position in the stream. Subsequent calls to reset()
will reposition the stream to this point.

reset

```java
public void reset()
throws
IOException
```

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

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

Resets the stream to the most recent mark, or to the beginning of the
string if it has never been marked.

close

```java
public void close()
```

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(),
ready(), mark(), or reset() invocations will throw an IOException.
Closing a previously closed stream has no effect. This method will block
while there is another thread blocking on the reader.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Reader

---

#### close

public void close()

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(),
ready(), mark(), or reset() invocations will throw an IOException.
Closing a previously closed stream has no effect. This method will block
while there is another thread blocking on the reader.

---

