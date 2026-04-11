# Class Reader

**Source:** `java.base\java\io\Reader.html`

### Class Description

```java
public abstract class
Reader

extends
Object

implements
Readable
,
Closeable
```

Abstract class for reading character streams. The only methods that a
subclass must implement are read(char[], int, int) and close(). Most
subclasses, however, will override some of the methods defined here in order
to provide higher efficiency, additional functionality, or both.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

#### protected
Object
lock

The object used to synchronize operations on this stream. For
efficiency, a character-stream object may use an object other than
itself to protect critical sections. A subclass should therefore use
the object in this field rather than

this

or a synchronized
method.

---

### Constructor Details

#### protected Reader()

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

---

#### protected Reader​(
Object
lock)

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

**Parameters:**
- lock

- The Object to synchronize on.

---

### Method Details

#### public static
Reader
nullReader()

Returns a new

Reader

that reads no characters. The returned
stream is initially open. The stream is closed by calling the

close()

method. Subsequent calls to

close()

have no
effect.

While the stream is open, the

read()

,

read(char[])

,

read(char[], int, int)

,

read(Charbuffer)

,

ready()

,

skip(long)

, and

transferTo()

methods all
behave as if end of stream has been reached. After the stream has been
closed, these methods all throw

IOException

.

The

markSupported()

method returns

false

. The

mark()

and

reset()

methods throw an

IOException

.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

**Returns:**
- a

Reader

which reads no characters

**Since:**
- 11

---

#### public int read​(
CharBuffer
target)
throws
IOException

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Specified by:**
- read

in interface

Readable

**Parameters:**
- target

- the buffer to read characters into

**Returns:**
- The number of characters added to the buffer, or
-1 if this source of characters is at its end

**Throws:**
- IOException

- if an I/O error occurs
- NullPointerException

- if target is null
- ReadOnlyBufferException

- if target is a read only buffer

**Since:**
- 1.5

---

#### public int read()
throws
IOException

Reads a single character. This method will block until a character is
available, an I/O error occurs, or the end of the stream is reached.

Subclasses that intend to support efficient single-character input
should override this method.

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

#### public int read​(char[] cbuf)
throws
IOException

Reads characters into an array. This method will block until some input
is available, an I/O error occurs, or the end of the stream is reached.

**Parameters:**
- cbuf

- Destination buffer

**Returns:**
- The number of characters read, or -1
if the end of the stream
has been reached

**Throws:**
- IOException

- If an I/O error occurs

---

#### public abstract int read​(char[] cbuf,
int off,
int len)
throws
IOException

Reads characters into a portion of an array. This method will block
until some input is available, an I/O error occurs, or the end of the
stream is reached.

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

- If

off

is negative, or

len

is negative,
or

len

is greater than

cbuf.length - off

---

#### public long skip​(long n)
throws
IOException

Skips characters. This method will block until some characters are
available, an I/O error occurs, or the end of the stream is reached.

**Parameters:**
- n

- The number of characters to skip

**Returns:**
- The number of characters actually skipped

**Throws:**
- IllegalArgumentException

- If

n

is negative.
- IOException

- If an I/O error occurs

---

#### public boolean ready()
throws
IOException

Tells whether this stream is ready to be read.

**Returns:**
- True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.

**Throws:**
- IOException

- If an I/O error occurs

---

#### public boolean markSupported()

Tells whether this stream supports the mark() operation. The default
implementation always returns false. Subclasses should override this
method.

**Returns:**
- true if and only if this stream supports the mark operation.

---

#### public void mark​(int readAheadLimit)
throws
IOException

Marks the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point. Not all
character-input streams support the mark() operation.

**Parameters:**
- readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.

**Throws:**
- IOException

- If the stream does not support mark(),
or if some other I/O error occurs

---

#### public void reset()
throws
IOException

Resets the stream. If the stream has been marked, then attempt to
reposition it at the mark. If the stream has not been marked, then
attempt to reset it in some way appropriate to the particular stream,
for example by repositioning it to its starting point. Not all
character-input streams support the reset() operation, and some support
reset() without supporting mark().

**Throws:**
- IOException

- If the stream has not been marked,
or if the mark has been invalidated,
or if the stream does not support reset(),
or if some other I/O error occurs

---

#### public abstract void close()
throws
IOException

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(), ready(),
mark(), reset(), or skip() invocations will throw an IOException.
Closing a previously closed stream has no effect.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Throws:**
- IOException

- If an I/O error occurs

---

#### public long transferTo​(
Writer
out)
throws
IOException

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read. On return, this reader
will be at end of the stream. This method does not close either reader
or writer.

This method may block indefinitely reading from the reader, or
writing to the writer. The behavior for the case where the reader
and/or writer is

asynchronously closed

, or the thread
interrupted during the transfer, is highly reader and writer
specific, and therefore not specified.

If an I/O error occurs reading from the reader or writing to the
writer, then it may do so after some characters have been read or
written. Consequently the reader may not be at end of the stream and
one, or both, streams may be in an inconsistent state. It is strongly
recommended that both streams be promptly closed if an I/O error occurs.

**Parameters:**
- out

- the writer, non-null

**Returns:**
- the number of characters transferred

**Throws:**
- IOException

- if an I/O error occurs when reading or writing
- NullPointerException

- if

out

is

null

**Since:**
- 10

---

### Additional Sections

#### Class Reader

java.lang.Object

- java.io.Reader

java.io.Reader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

**Direct Known Subclasses:** BufferedReader

,

CharArrayReader

,

FilterReader

,

InputStreamReader

,

PipedReader

,

StringReader

,

URLReader

```java
public abstract class
Reader

extends
Object

implements
Readable
,
Closeable
```

Abstract class for reading character streams. The only methods that a
subclass must implement are read(char[], int, int) and close(). Most
subclasses, however, will override some of the methods defined here in order
to provide higher efficiency, additional functionality, or both.

**Since:** 1.1
**See Also:** BufferedReader

,

LineNumberReader

,

CharArrayReader

,

InputStreamReader

,

FileReader

,

FilterReader

,

PushbackReader

,

PipedReader

,

StringReader

,

Writer

public abstract class

Reader

extends

Object

implements

Readable

,

Closeable

Abstract class for reading character streams. The only methods that a
subclass must implement are read(char[], int, int) and close(). Most
subclasses, however, will override some of the methods defined here in order
to provide higher efficiency, additional functionality, or both.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

lock

The object used to synchronize operations on this stream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Reader

()

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

protected

Reader

​(

Object

lock)

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

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

Tells whether this stream supports the mark() operation.

static

Reader

nullReader

()

Returns a new

Reader

that reads no characters.

int

read

()

Reads a single character.

int

read

​(char[] cbuf)

Reads characters into an array.

abstract int

read

​(char[] cbuf,
int off,
int len)

Reads characters into a portion of an array.

int

read

​(

CharBuffer

target)

Attempts to read characters into the specified character buffer.

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

long

transferTo

​(

Writer

out)

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read.

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

Object

lock

The object used to synchronize operations on this stream.

---

#### Field Summary

The object used to synchronize operations on this stream.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Reader

()

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

protected

Reader

​(

Object

lock)

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

---

#### Constructor Summary

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

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

Tells whether this stream supports the mark() operation.

static

Reader

nullReader

()

Returns a new

Reader

that reads no characters.

int

read

()

Reads a single character.

int

read

​(char[] cbuf)

Reads characters into an array.

abstract int

read

​(char[] cbuf,
int off,
int len)

Reads characters into a portion of an array.

int

read

​(

CharBuffer

target)

Attempts to read characters into the specified character buffer.

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

long

transferTo

​(

Writer

out)

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read.

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

Tells whether this stream supports the mark() operation.

Returns a new

Reader

that reads no characters.

Reads a single character.

Reads characters into an array.

Reads characters into a portion of an array.

Attempts to read characters into the specified character buffer.

Tells whether this stream is ready to be read.

Resets the stream.

Skips characters.

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read.

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

- lock

```java
protected
Object
lock
```

The object used to synchronize operations on this stream. For
efficiency, a character-stream object may use an object other than
itself to protect critical sections. A subclass should therefore use
the object in this field rather than

this

or a synchronized
method.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Reader

```java
protected Reader()
```

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

- Reader

```java
protected Reader​(
Object
lock)
```

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

**Parameters:** lock

- The Object to synchronize on.

============ METHOD DETAIL ==========

- Method Detail

- nullReader

```java
public static
Reader
nullReader()
```

Returns a new

Reader

that reads no characters. The returned
stream is initially open. The stream is closed by calling the

close()

method. Subsequent calls to

close()

have no
effect.

While the stream is open, the

read()

,

read(char[])

,

read(char[], int, int)

,

read(Charbuffer)

,

ready()

,

skip(long)

, and

transferTo()

methods all
behave as if end of stream has been reached. After the stream has been
closed, these methods all throw

IOException

.

The

markSupported()

method returns

false

. The

mark()

and

reset()

methods throw an

IOException

.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

**Returns:** a

Reader

which reads no characters
**Since:** 11

- read

```java
public int read​(
CharBuffer
target)
throws
IOException
```

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Specified by:** read

in interface

Readable
**Parameters:** target

- the buffer to read characters into
**Returns:** The number of characters added to the buffer, or
-1 if this source of characters is at its end
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if target is null
**Throws:** ReadOnlyBufferException

- if target is a read only buffer
**Since:** 1.5

- read

```java
public int read()
throws
IOException
```

Reads a single character. This method will block until a character is
available, an I/O error occurs, or the end of the stream is reached.

Subclasses that intend to support efficient single-character input
should override this method.

**Returns:** The character read, as an integer in the range 0 to 65535
(

0x00-0xffff

), or -1 if the end of the stream has
been reached
**Throws:** IOException

- If an I/O error occurs

- read

```java
public int read​(char[] cbuf)
throws
IOException
```

Reads characters into an array. This method will block until some input
is available, an I/O error occurs, or the end of the stream is reached.

**Parameters:** cbuf

- Destination buffer
**Returns:** The number of characters read, or -1
if the end of the stream
has been reached
**Throws:** IOException

- If an I/O error occurs

- read

```java
public abstract int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads characters into a portion of an array. This method will block
until some input is available, an I/O error occurs, or the end of the
stream is reached.

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

- If

off

is negative, or

len

is negative,
or

len

is greater than

cbuf.length - off

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips characters. This method will block until some characters are
available, an I/O error occurs, or the end of the stream is reached.

**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IllegalArgumentException

- If

n

is negative.
**Throws:** IOException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read.

**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- If an I/O error occurs

- markSupported

```java
public boolean markSupported()
```

Tells whether this stream supports the mark() operation. The default
implementation always returns false. Subclasses should override this
method.

**Returns:** true if and only if this stream supports the mark operation.

- mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Marks the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point. Not all
character-input streams support the mark() operation.

**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.
**Throws:** IOException

- If the stream does not support mark(),
or if some other I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Resets the stream. If the stream has been marked, then attempt to
reposition it at the mark. If the stream has not been marked, then
attempt to reset it in some way appropriate to the particular stream,
for example by repositioning it to its starting point. Not all
character-input streams support the reset() operation, and some support
reset() without supporting mark().

**Throws:** IOException

- If the stream has not been marked,
or if the mark has been invalidated,
or if the stream does not support reset(),
or if some other I/O error occurs

- close

```java
public abstract void close()
throws
IOException
```

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(), ready(),
mark(), reset(), or skip() invocations will throw an IOException.
Closing a previously closed stream has no effect.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- If an I/O error occurs

- transferTo

```java
public long transferTo​(
Writer
out)
throws
IOException
```

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read. On return, this reader
will be at end of the stream. This method does not close either reader
or writer.

This method may block indefinitely reading from the reader, or
writing to the writer. The behavior for the case where the reader
and/or writer is

asynchronously closed

, or the thread
interrupted during the transfer, is highly reader and writer
specific, and therefore not specified.

If an I/O error occurs reading from the reader or writing to the
writer, then it may do so after some characters have been read or
written. Consequently the reader may not be at end of the stream and
one, or both, streams may be in an inconsistent state. It is strongly
recommended that both streams be promptly closed if an I/O error occurs.

**Parameters:** out

- the writer, non-null
**Returns:** the number of characters transferred
**Throws:** IOException

- if an I/O error occurs when reading or writing
**Throws:** NullPointerException

- if

out

is

null
**Since:** 10

Field Detail

- lock

```java
protected
Object
lock
```

The object used to synchronize operations on this stream. For
efficiency, a character-stream object may use an object other than
itself to protect critical sections. A subclass should therefore use
the object in this field rather than

this

or a synchronized
method.

---

#### Field Detail

lock

```java
protected
Object
lock
```

The object used to synchronize operations on this stream. For
efficiency, a character-stream object may use an object other than
itself to protect critical sections. A subclass should therefore use
the object in this field rather than

this

or a synchronized
method.

---

#### lock

protected

Object

lock

The object used to synchronize operations on this stream. For
efficiency, a character-stream object may use an object other than
itself to protect critical sections. A subclass should therefore use
the object in this field rather than

this

or a synchronized
method.

Constructor Detail

- Reader

```java
protected Reader()
```

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

- Reader

```java
protected Reader​(
Object
lock)
```

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

**Parameters:** lock

- The Object to synchronize on.

---

#### Constructor Detail

Reader

```java
protected Reader()
```

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

---

#### Reader

protected Reader()

Creates a new character-stream reader whose critical sections will
synchronize on the reader itself.

Reader

```java
protected Reader​(
Object
lock)
```

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

**Parameters:** lock

- The Object to synchronize on.

---

#### Reader

protected Reader​(

Object

lock)

Creates a new character-stream reader whose critical sections will
synchronize on the given object.

Method Detail

- nullReader

```java
public static
Reader
nullReader()
```

Returns a new

Reader

that reads no characters. The returned
stream is initially open. The stream is closed by calling the

close()

method. Subsequent calls to

close()

have no
effect.

While the stream is open, the

read()

,

read(char[])

,

read(char[], int, int)

,

read(Charbuffer)

,

ready()

,

skip(long)

, and

transferTo()

methods all
behave as if end of stream has been reached. After the stream has been
closed, these methods all throw

IOException

.

The

markSupported()

method returns

false

. The

mark()

and

reset()

methods throw an

IOException

.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

**Returns:** a

Reader

which reads no characters
**Since:** 11

- read

```java
public int read​(
CharBuffer
target)
throws
IOException
```

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Specified by:** read

in interface

Readable
**Parameters:** target

- the buffer to read characters into
**Returns:** The number of characters added to the buffer, or
-1 if this source of characters is at its end
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if target is null
**Throws:** ReadOnlyBufferException

- if target is a read only buffer
**Since:** 1.5

- read

```java
public int read()
throws
IOException
```

Reads a single character. This method will block until a character is
available, an I/O error occurs, or the end of the stream is reached.

Subclasses that intend to support efficient single-character input
should override this method.

**Returns:** The character read, as an integer in the range 0 to 65535
(

0x00-0xffff

), or -1 if the end of the stream has
been reached
**Throws:** IOException

- If an I/O error occurs

- read

```java
public int read​(char[] cbuf)
throws
IOException
```

Reads characters into an array. This method will block until some input
is available, an I/O error occurs, or the end of the stream is reached.

**Parameters:** cbuf

- Destination buffer
**Returns:** The number of characters read, or -1
if the end of the stream
has been reached
**Throws:** IOException

- If an I/O error occurs

- read

```java
public abstract int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads characters into a portion of an array. This method will block
until some input is available, an I/O error occurs, or the end of the
stream is reached.

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

- If

off

is negative, or

len

is negative,
or

len

is greater than

cbuf.length - off

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips characters. This method will block until some characters are
available, an I/O error occurs, or the end of the stream is reached.

**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IllegalArgumentException

- If

n

is negative.
**Throws:** IOException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read.

**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- If an I/O error occurs

- markSupported

```java
public boolean markSupported()
```

Tells whether this stream supports the mark() operation. The default
implementation always returns false. Subclasses should override this
method.

**Returns:** true if and only if this stream supports the mark operation.

- mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Marks the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point. Not all
character-input streams support the mark() operation.

**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.
**Throws:** IOException

- If the stream does not support mark(),
or if some other I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Resets the stream. If the stream has been marked, then attempt to
reposition it at the mark. If the stream has not been marked, then
attempt to reset it in some way appropriate to the particular stream,
for example by repositioning it to its starting point. Not all
character-input streams support the reset() operation, and some support
reset() without supporting mark().

**Throws:** IOException

- If the stream has not been marked,
or if the mark has been invalidated,
or if the stream does not support reset(),
or if some other I/O error occurs

- close

```java
public abstract void close()
throws
IOException
```

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(), ready(),
mark(), reset(), or skip() invocations will throw an IOException.
Closing a previously closed stream has no effect.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- If an I/O error occurs

- transferTo

```java
public long transferTo​(
Writer
out)
throws
IOException
```

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read. On return, this reader
will be at end of the stream. This method does not close either reader
or writer.

This method may block indefinitely reading from the reader, or
writing to the writer. The behavior for the case where the reader
and/or writer is

asynchronously closed

, or the thread
interrupted during the transfer, is highly reader and writer
specific, and therefore not specified.

If an I/O error occurs reading from the reader or writing to the
writer, then it may do so after some characters have been read or
written. Consequently the reader may not be at end of the stream and
one, or both, streams may be in an inconsistent state. It is strongly
recommended that both streams be promptly closed if an I/O error occurs.

**Parameters:** out

- the writer, non-null
**Returns:** the number of characters transferred
**Throws:** IOException

- if an I/O error occurs when reading or writing
**Throws:** NullPointerException

- if

out

is

null
**Since:** 10

---

#### Method Detail

nullReader

```java
public static
Reader
nullReader()
```

Returns a new

Reader

that reads no characters. The returned
stream is initially open. The stream is closed by calling the

close()

method. Subsequent calls to

close()

have no
effect.

While the stream is open, the

read()

,

read(char[])

,

read(char[], int, int)

,

read(Charbuffer)

,

ready()

,

skip(long)

, and

transferTo()

methods all
behave as if end of stream has been reached. After the stream has been
closed, these methods all throw

IOException

.

The

markSupported()

method returns

false

. The

mark()

and

reset()

methods throw an

IOException

.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

**Returns:** a

Reader

which reads no characters
**Since:** 11

---

#### nullReader

public static

Reader

nullReader()

Returns a new

Reader

that reads no characters. The returned
stream is initially open. The stream is closed by calling the

close()

method. Subsequent calls to

close()

have no
effect.

While the stream is open, the

read()

,

read(char[])

,

read(char[], int, int)

,

read(Charbuffer)

,

ready()

,

skip(long)

, and

transferTo()

methods all
behave as if end of stream has been reached. After the stream has been
closed, these methods all throw

IOException

.

The

markSupported()

method returns

false

. The

mark()

and

reset()

methods throw an

IOException

.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

While the stream is open, the

read()

,

read(char[])

,

read(char[], int, int)

,

read(Charbuffer)

,

ready()

,

skip(long)

, and

transferTo()

methods all
behave as if end of stream has been reached. After the stream has been
closed, these methods all throw

IOException

.

The

markSupported()

method returns

false

. The

mark()

and

reset()

methods throw an

IOException

.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

The

markSupported()

method returns

false

. The

mark()

and

reset()

methods throw an

IOException

.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

The

object

used to synchronize operations on the
returned

Reader

is not specified.

read

```java
public int read​(
CharBuffer
target)
throws
IOException
```

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Specified by:** read

in interface

Readable
**Parameters:** target

- the buffer to read characters into
**Returns:** The number of characters added to the buffer, or
-1 if this source of characters is at its end
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if target is null
**Throws:** ReadOnlyBufferException

- if target is a read only buffer
**Since:** 1.5

---

#### read

public int read​(

CharBuffer

target)
throws

IOException

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

read

```java
public int read()
throws
IOException
```

Reads a single character. This method will block until a character is
available, an I/O error occurs, or the end of the stream is reached.

Subclasses that intend to support efficient single-character input
should override this method.

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

Reads a single character. This method will block until a character is
available, an I/O error occurs, or the end of the stream is reached.

Subclasses that intend to support efficient single-character input
should override this method.

Subclasses that intend to support efficient single-character input
should override this method.

read

```java
public int read​(char[] cbuf)
throws
IOException
```

Reads characters into an array. This method will block until some input
is available, an I/O error occurs, or the end of the stream is reached.

**Parameters:** cbuf

- Destination buffer
**Returns:** The number of characters read, or -1
if the end of the stream
has been reached
**Throws:** IOException

- If an I/O error occurs

---

#### read

public int read​(char[] cbuf)
throws

IOException

Reads characters into an array. This method will block until some input
is available, an I/O error occurs, or the end of the stream is reached.

read

```java
public abstract int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Reads characters into a portion of an array. This method will block
until some input is available, an I/O error occurs, or the end of the
stream is reached.

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

- If

off

is negative, or

len

is negative,
or

len

is greater than

cbuf.length - off

---

#### read

public abstract int read​(char[] cbuf,
int off,
int len)
throws

IOException

Reads characters into a portion of an array. This method will block
until some input is available, an I/O error occurs, or the end of the
stream is reached.

skip

```java
public long skip​(long n)
throws
IOException
```

Skips characters. This method will block until some characters are
available, an I/O error occurs, or the end of the stream is reached.

**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IllegalArgumentException

- If

n

is negative.
**Throws:** IOException

- If an I/O error occurs

---

#### skip

public long skip​(long n)
throws

IOException

Skips characters. This method will block until some characters are
available, an I/O error occurs, or the end of the stream is reached.

ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read.

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

Tells whether this stream supports the mark() operation. The default
implementation always returns false. Subclasses should override this
method.

**Returns:** true if and only if this stream supports the mark operation.

---

#### markSupported

public boolean markSupported()

Tells whether this stream supports the mark() operation. The default
implementation always returns false. Subclasses should override this
method.

mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Marks the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point. Not all
character-input streams support the mark() operation.

**Parameters:** readAheadLimit

- Limit on the number of characters that may be
read while still preserving the mark. After
reading this many characters, attempting to
reset the stream may fail.
**Throws:** IOException

- If the stream does not support mark(),
or if some other I/O error occurs

---

#### mark

public void mark​(int readAheadLimit)
throws

IOException

Marks the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point. Not all
character-input streams support the mark() operation.

reset

```java
public void reset()
throws
IOException
```

Resets the stream. If the stream has been marked, then attempt to
reposition it at the mark. If the stream has not been marked, then
attempt to reset it in some way appropriate to the particular stream,
for example by repositioning it to its starting point. Not all
character-input streams support the reset() operation, and some support
reset() without supporting mark().

**Throws:** IOException

- If the stream has not been marked,
or if the mark has been invalidated,
or if the stream does not support reset(),
or if some other I/O error occurs

---

#### reset

public void reset()
throws

IOException

Resets the stream. If the stream has been marked, then attempt to
reposition it at the mark. If the stream has not been marked, then
attempt to reset it in some way appropriate to the particular stream,
for example by repositioning it to its starting point. Not all
character-input streams support the reset() operation, and some support
reset() without supporting mark().

close

```java
public abstract void close()
throws
IOException
```

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(), ready(),
mark(), reset(), or skip() invocations will throw an IOException.
Closing a previously closed stream has no effect.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- If an I/O error occurs

---

#### close

public abstract void close()
throws

IOException

Closes the stream and releases any system resources associated with
it. Once the stream has been closed, further read(), ready(),
mark(), reset(), or skip() invocations will throw an IOException.
Closing a previously closed stream has no effect.

transferTo

```java
public long transferTo​(
Writer
out)
throws
IOException
```

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read. On return, this reader
will be at end of the stream. This method does not close either reader
or writer.

This method may block indefinitely reading from the reader, or
writing to the writer. The behavior for the case where the reader
and/or writer is

asynchronously closed

, or the thread
interrupted during the transfer, is highly reader and writer
specific, and therefore not specified.

If an I/O error occurs reading from the reader or writing to the
writer, then it may do so after some characters have been read or
written. Consequently the reader may not be at end of the stream and
one, or both, streams may be in an inconsistent state. It is strongly
recommended that both streams be promptly closed if an I/O error occurs.

**Parameters:** out

- the writer, non-null
**Returns:** the number of characters transferred
**Throws:** IOException

- if an I/O error occurs when reading or writing
**Throws:** NullPointerException

- if

out

is

null
**Since:** 10

---

#### transferTo

public long transferTo​(

Writer

out)
throws

IOException

Reads all characters from this reader and writes the characters to the
given writer in the order that they are read. On return, this reader
will be at end of the stream. This method does not close either reader
or writer.

This method may block indefinitely reading from the reader, or
writing to the writer. The behavior for the case where the reader
and/or writer is

asynchronously closed

, or the thread
interrupted during the transfer, is highly reader and writer
specific, and therefore not specified.

If an I/O error occurs reading from the reader or writing to the
writer, then it may do so after some characters have been read or
written. Consequently the reader may not be at end of the stream and
one, or both, streams may be in an inconsistent state. It is strongly
recommended that both streams be promptly closed if an I/O error occurs.

This method may block indefinitely reading from the reader, or
writing to the writer. The behavior for the case where the reader
and/or writer is

asynchronously closed

, or the thread
interrupted during the transfer, is highly reader and writer
specific, and therefore not specified.

If an I/O error occurs reading from the reader or writing to the
writer, then it may do so after some characters have been read or
written. Consequently the reader may not be at end of the stream and
one, or both, streams may be in an inconsistent state. It is strongly
recommended that both streams be promptly closed if an I/O error occurs.

If an I/O error occurs reading from the reader or writing to the
writer, then it may do so after some characters have been read or
written. Consequently the reader may not be at end of the stream and
one, or both, streams may be in an inconsistent state. It is strongly
recommended that both streams be promptly closed if an I/O error occurs.

---

