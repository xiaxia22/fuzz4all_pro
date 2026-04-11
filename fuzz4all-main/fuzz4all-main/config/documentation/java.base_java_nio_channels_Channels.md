# Class Channels

**Source:** `java.base\java\nio\channels\Channels.html`

### Class Description

```java
public final class
Channels

extends
Object
```

Utility methods for channels and streams.

This class defines static methods that support the interoperation of the
stream classes of the

java.io

package with the channel classes
of this package.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
InputStream
newInputStream​(
ReadableByteChannel
ch)

Constructs a stream that reads bytes from the given channel.

The

read

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered, and
it will not support the

mark

or

reset

methods. The stream will be safe for access by
multiple concurrent threads. Closing the stream will in turn cause the
channel to be closed.

**Parameters:**
- ch

- The channel from which bytes will be read

**Returns:**
- A new input stream

---

#### public static
OutputStream
newOutputStream​(
WritableByteChannel
ch)

Constructs a stream that writes bytes to the given channel.

The

write

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:**
- ch

- The channel to which bytes will be written

**Returns:**
- A new output stream

---

#### public static
InputStream
newInputStream​(
AsynchronousByteChannel
ch)

Constructs a stream that reads bytes from the given channel.

The stream will not be buffered, and it will not support the

mark

or

reset

methods. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:**
- ch

- The channel from which bytes will be read

**Returns:**
- A new input stream

**Since:**
- 1.7

---

#### public static
OutputStream
newOutputStream​(
AsynchronousByteChannel
ch)

Constructs a stream that writes bytes to the given channel.

The stream will not be buffered. The stream will be safe for access
by multiple concurrent threads. Closing the stream will in turn cause
the channel to be closed.

**Parameters:**
- ch

- The channel to which bytes will be written

**Returns:**
- A new output stream

**Since:**
- 1.7

---

#### public static
ReadableByteChannel
newChannel​(
InputStream
in)

Constructs a channel that reads bytes from the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:**
- in

- The stream from which bytes are to be read

**Returns:**
- A new readable byte channel

---

#### public static
WritableByteChannel
newChannel​(
OutputStream
out)

Constructs a channel that writes bytes to the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:**
- out

- The stream to which bytes are to be written

**Returns:**
- A new writable byte channel

---

#### public static
Reader
newReader​(
ReadableByteChannel
ch,

CharsetDecoder
dec,
int minBufferCap)

Constructs a reader that decodes bytes from the given channel using the
given decoder.

The resulting stream will contain an internal input buffer of at
least

minBufferCap

bytes. The stream's

read

methods
will, as needed, fill the buffer by reading bytes from the underlying
channel; if the channel is in non-blocking mode when bytes are to be
read then an

IllegalBlockingModeException

will be thrown. The
resulting stream will not otherwise be buffered, and it will not support
the

mark

or

reset

methods.
Closing the stream will in turn cause the channel to be closed.

**Parameters:**
- ch

- The channel from which bytes will be read
- dec

- The charset decoder to be used
- minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used

**Returns:**
- A new reader

---

#### public static
Reader
newReader​(
ReadableByteChannel
ch,

String
csName)

Constructs a reader that decodes bytes from the given channel according
to the named charset.

An invocation of this method of the form

```java
Channels.newReader(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName))
```

**Parameters:**
- ch

- The channel from which bytes will be read
- csName

- The name of the charset to be used

**Returns:**
- A new reader

**Throws:**
- UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

---

#### public static
Reader
newReader​(
ReadableByteChannel
ch,

Charset
charset)

Constructs a reader that decodes bytes from the given channel according
to the given charset.

An invocation of this method of the form

```java
Channels.newReader(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName).newDecoder(), -1)
```

The reader's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetDecoder

should be used.

**Parameters:**
- ch

- The channel from which bytes will be read
- charset

- The charset to be used

**Returns:**
- A new reader

---

#### public static
Writer
newWriter​(
WritableByteChannel
ch,

CharsetEncoder
enc,
int minBufferCap)

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

The resulting stream will contain an internal output buffer of at
least

minBufferCap

bytes. The stream's

write

methods
will, as needed, flush the buffer by writing bytes to the underlying
channel; if the channel is in non-blocking mode when bytes are to be
written then an

IllegalBlockingModeException

will be thrown.
The resulting stream will not otherwise be buffered. Closing the stream
will in turn cause the channel to be closed.

**Parameters:**
- ch

- The channel to which bytes will be written
- enc

- The charset encoder to be used
- minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used

**Returns:**
- A new writer

---

#### public static
Writer
newWriter​(
WritableByteChannel
ch,

String
csName)

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName))
```

**Parameters:**
- ch

- The channel to which bytes will be written
- csName

- The name of the charset to be used

**Returns:**
- A new writer

**Throws:**
- UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

---

#### public static
Writer
newWriter​(
WritableByteChannel
ch,

Charset
charset)

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName).newEncoder(), -1)
```

The writer's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetEncoder

should be used.

**Parameters:**
- ch

- The channel to which bytes will be written
- charset

- The charset to be used

**Returns:**
- A new writer

---

### Additional Sections

#### Class Channels

java.lang.Object

- java.nio.channels.Channels

java.nio.channels.Channels

```java
public final class
Channels

extends
Object
```

Utility methods for channels and streams.

This class defines static methods that support the interoperation of the
stream classes of the

java.io

package with the channel classes
of this package.

**Since:** 1.4

public final class

Channels

extends

Object

Utility methods for channels and streams.

This class defines static methods that support the interoperation of the
stream classes of the

java.io

package with the channel classes
of this package.

This class defines static methods that support the interoperation of the
stream classes of the

java.io

package with the channel classes
of this package.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ReadableByteChannel

newChannel

​(

InputStream

in)

Constructs a channel that reads bytes from the given stream.

static

WritableByteChannel

newChannel

​(

OutputStream

out)

Constructs a channel that writes bytes to the given stream.

static

InputStream

newInputStream

​(

AsynchronousByteChannel

ch)

Constructs a stream that reads bytes from the given channel.

static

InputStream

newInputStream

​(

ReadableByteChannel

ch)

Constructs a stream that reads bytes from the given channel.

static

OutputStream

newOutputStream

​(

AsynchronousByteChannel

ch)

Constructs a stream that writes bytes to the given channel.

static

OutputStream

newOutputStream

​(

WritableByteChannel

ch)

Constructs a stream that writes bytes to the given channel.

static

Reader

newReader

​(

ReadableByteChannel

ch,

String

csName)

Constructs a reader that decodes bytes from the given channel according
to the named charset.

static

Reader

newReader

​(

ReadableByteChannel

ch,

Charset

charset)

Constructs a reader that decodes bytes from the given channel according
to the given charset.

static

Reader

newReader

​(

ReadableByteChannel

ch,

CharsetDecoder

dec,
int minBufferCap)

Constructs a reader that decodes bytes from the given channel using the
given decoder.

static

Writer

newWriter

​(

WritableByteChannel

ch,

String

csName)

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

static

Writer

newWriter

​(

WritableByteChannel

ch,

Charset

charset)

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

static

Writer

newWriter

​(

WritableByteChannel

ch,

CharsetEncoder

enc,
int minBufferCap)

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ReadableByteChannel

newChannel

​(

InputStream

in)

Constructs a channel that reads bytes from the given stream.

static

WritableByteChannel

newChannel

​(

OutputStream

out)

Constructs a channel that writes bytes to the given stream.

static

InputStream

newInputStream

​(

AsynchronousByteChannel

ch)

Constructs a stream that reads bytes from the given channel.

static

InputStream

newInputStream

​(

ReadableByteChannel

ch)

Constructs a stream that reads bytes from the given channel.

static

OutputStream

newOutputStream

​(

AsynchronousByteChannel

ch)

Constructs a stream that writes bytes to the given channel.

static

OutputStream

newOutputStream

​(

WritableByteChannel

ch)

Constructs a stream that writes bytes to the given channel.

static

Reader

newReader

​(

ReadableByteChannel

ch,

String

csName)

Constructs a reader that decodes bytes from the given channel according
to the named charset.

static

Reader

newReader

​(

ReadableByteChannel

ch,

Charset

charset)

Constructs a reader that decodes bytes from the given channel according
to the given charset.

static

Reader

newReader

​(

ReadableByteChannel

ch,

CharsetDecoder

dec,
int minBufferCap)

Constructs a reader that decodes bytes from the given channel using the
given decoder.

static

Writer

newWriter

​(

WritableByteChannel

ch,

String

csName)

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

static

Writer

newWriter

​(

WritableByteChannel

ch,

Charset

charset)

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

static

Writer

newWriter

​(

WritableByteChannel

ch,

CharsetEncoder

enc,
int minBufferCap)

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

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

Constructs a channel that reads bytes from the given stream.

Constructs a channel that writes bytes to the given stream.

Constructs a stream that reads bytes from the given channel.

Constructs a stream that writes bytes to the given channel.

Constructs a reader that decodes bytes from the given channel according
to the named charset.

Constructs a reader that decodes bytes from the given channel according
to the given charset.

Constructs a reader that decodes bytes from the given channel using the
given decoder.

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

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

============ METHOD DETAIL ==========

- Method Detail

- newInputStream

```java
public static
InputStream
newInputStream​(
ReadableByteChannel
ch)
```

Constructs a stream that reads bytes from the given channel.

The

read

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered, and
it will not support the

mark

or

reset

methods. The stream will be safe for access by
multiple concurrent threads. Closing the stream will in turn cause the
channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Returns:** A new input stream

- newOutputStream

```java
public static
OutputStream
newOutputStream​(
WritableByteChannel
ch)
```

Constructs a stream that writes bytes to the given channel.

The

write

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Returns:** A new output stream

- newInputStream

```java
public static
InputStream
newInputStream​(
AsynchronousByteChannel
ch)
```

Constructs a stream that reads bytes from the given channel.

The stream will not be buffered, and it will not support the

mark

or

reset

methods. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Returns:** A new input stream
**Since:** 1.7

- newOutputStream

```java
public static
OutputStream
newOutputStream​(
AsynchronousByteChannel
ch)
```

Constructs a stream that writes bytes to the given channel.

The stream will not be buffered. The stream will be safe for access
by multiple concurrent threads. Closing the stream will in turn cause
the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Returns:** A new output stream
**Since:** 1.7

- newChannel

```java
public static
ReadableByteChannel
newChannel​(
InputStream
in)
```

Constructs a channel that reads bytes from the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:** in

- The stream from which bytes are to be read
**Returns:** A new readable byte channel

- newChannel

```java
public static
WritableByteChannel
newChannel​(
OutputStream
out)
```

Constructs a channel that writes bytes to the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:** out

- The stream to which bytes are to be written
**Returns:** A new writable byte channel

- newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

CharsetDecoder
dec,
int minBufferCap)
```

Constructs a reader that decodes bytes from the given channel using the
given decoder.

The resulting stream will contain an internal input buffer of at
least

minBufferCap

bytes. The stream's

read

methods
will, as needed, fill the buffer by reading bytes from the underlying
channel; if the channel is in non-blocking mode when bytes are to be
read then an

IllegalBlockingModeException

will be thrown. The
resulting stream will not otherwise be buffered, and it will not support
the

mark

or

reset

methods.
Closing the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** dec

- The charset decoder to be used
**Parameters:** minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used
**Returns:** A new reader

- newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

String
csName)
```

Constructs a reader that decodes bytes from the given channel according
to the named charset.

An invocation of this method of the form

```java
Channels.newReader(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName))
```

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** csName

- The name of the charset to be used
**Returns:** A new reader
**Throws:** UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

- newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

Charset
charset)
```

Constructs a reader that decodes bytes from the given channel according
to the given charset.

An invocation of this method of the form

```java
Channels.newReader(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName).newDecoder(), -1)
```

The reader's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetDecoder

should be used.

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** charset

- The charset to be used
**Returns:** A new reader

- newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

CharsetEncoder
enc,
int minBufferCap)
```

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

The resulting stream will contain an internal output buffer of at
least

minBufferCap

bytes. The stream's

write

methods
will, as needed, flush the buffer by writing bytes to the underlying
channel; if the channel is in non-blocking mode when bytes are to be
written then an

IllegalBlockingModeException

will be thrown.
The resulting stream will not otherwise be buffered. Closing the stream
will in turn cause the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** enc

- The charset encoder to be used
**Parameters:** minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used
**Returns:** A new writer

- newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

String
csName)
```

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName))
```

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** csName

- The name of the charset to be used
**Returns:** A new writer
**Throws:** UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

- newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

Charset
charset)
```

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName).newEncoder(), -1)
```

The writer's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetEncoder

should be used.

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** charset

- The charset to be used
**Returns:** A new writer

Method Detail

- newInputStream

```java
public static
InputStream
newInputStream​(
ReadableByteChannel
ch)
```

Constructs a stream that reads bytes from the given channel.

The

read

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered, and
it will not support the

mark

or

reset

methods. The stream will be safe for access by
multiple concurrent threads. Closing the stream will in turn cause the
channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Returns:** A new input stream

- newOutputStream

```java
public static
OutputStream
newOutputStream​(
WritableByteChannel
ch)
```

Constructs a stream that writes bytes to the given channel.

The

write

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Returns:** A new output stream

- newInputStream

```java
public static
InputStream
newInputStream​(
AsynchronousByteChannel
ch)
```

Constructs a stream that reads bytes from the given channel.

The stream will not be buffered, and it will not support the

mark

or

reset

methods. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Returns:** A new input stream
**Since:** 1.7

- newOutputStream

```java
public static
OutputStream
newOutputStream​(
AsynchronousByteChannel
ch)
```

Constructs a stream that writes bytes to the given channel.

The stream will not be buffered. The stream will be safe for access
by multiple concurrent threads. Closing the stream will in turn cause
the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Returns:** A new output stream
**Since:** 1.7

- newChannel

```java
public static
ReadableByteChannel
newChannel​(
InputStream
in)
```

Constructs a channel that reads bytes from the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:** in

- The stream from which bytes are to be read
**Returns:** A new readable byte channel

- newChannel

```java
public static
WritableByteChannel
newChannel​(
OutputStream
out)
```

Constructs a channel that writes bytes to the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:** out

- The stream to which bytes are to be written
**Returns:** A new writable byte channel

- newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

CharsetDecoder
dec,
int minBufferCap)
```

Constructs a reader that decodes bytes from the given channel using the
given decoder.

The resulting stream will contain an internal input buffer of at
least

minBufferCap

bytes. The stream's

read

methods
will, as needed, fill the buffer by reading bytes from the underlying
channel; if the channel is in non-blocking mode when bytes are to be
read then an

IllegalBlockingModeException

will be thrown. The
resulting stream will not otherwise be buffered, and it will not support
the

mark

or

reset

methods.
Closing the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** dec

- The charset decoder to be used
**Parameters:** minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used
**Returns:** A new reader

- newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

String
csName)
```

Constructs a reader that decodes bytes from the given channel according
to the named charset.

An invocation of this method of the form

```java
Channels.newReader(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName))
```

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** csName

- The name of the charset to be used
**Returns:** A new reader
**Throws:** UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

- newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

Charset
charset)
```

Constructs a reader that decodes bytes from the given channel according
to the given charset.

An invocation of this method of the form

```java
Channels.newReader(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName).newDecoder(), -1)
```

The reader's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetDecoder

should be used.

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** charset

- The charset to be used
**Returns:** A new reader

- newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

CharsetEncoder
enc,
int minBufferCap)
```

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

The resulting stream will contain an internal output buffer of at
least

minBufferCap

bytes. The stream's

write

methods
will, as needed, flush the buffer by writing bytes to the underlying
channel; if the channel is in non-blocking mode when bytes are to be
written then an

IllegalBlockingModeException

will be thrown.
The resulting stream will not otherwise be buffered. Closing the stream
will in turn cause the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** enc

- The charset encoder to be used
**Parameters:** minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used
**Returns:** A new writer

- newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

String
csName)
```

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName))
```

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** csName

- The name of the charset to be used
**Returns:** A new writer
**Throws:** UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

- newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

Charset
charset)
```

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName).newEncoder(), -1)
```

The writer's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetEncoder

should be used.

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** charset

- The charset to be used
**Returns:** A new writer

---

#### Method Detail

newInputStream

```java
public static
InputStream
newInputStream​(
ReadableByteChannel
ch)
```

Constructs a stream that reads bytes from the given channel.

The

read

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered, and
it will not support the

mark

or

reset

methods. The stream will be safe for access by
multiple concurrent threads. Closing the stream will in turn cause the
channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Returns:** A new input stream

---

#### newInputStream

public static

InputStream

newInputStream​(

ReadableByteChannel

ch)

Constructs a stream that reads bytes from the given channel.

The

read

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered, and
it will not support the

mark

or

reset

methods. The stream will be safe for access by
multiple concurrent threads. Closing the stream will in turn cause the
channel to be closed.

The

read

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered, and
it will not support the

mark

or

reset

methods. The stream will be safe for access by
multiple concurrent threads. Closing the stream will in turn cause the
channel to be closed.

newOutputStream

```java
public static
OutputStream
newOutputStream​(
WritableByteChannel
ch)
```

Constructs a stream that writes bytes to the given channel.

The

write

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Returns:** A new output stream

---

#### newOutputStream

public static

OutputStream

newOutputStream​(

WritableByteChannel

ch)

Constructs a stream that writes bytes to the given channel.

The

write

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

The

write

methods of the resulting stream will throw an

IllegalBlockingModeException

if invoked while the underlying
channel is in non-blocking mode. The stream will not be buffered. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

newInputStream

```java
public static
InputStream
newInputStream​(
AsynchronousByteChannel
ch)
```

Constructs a stream that reads bytes from the given channel.

The stream will not be buffered, and it will not support the

mark

or

reset

methods. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Returns:** A new input stream
**Since:** 1.7

---

#### newInputStream

public static

InputStream

newInputStream​(

AsynchronousByteChannel

ch)

Constructs a stream that reads bytes from the given channel.

The stream will not be buffered, and it will not support the

mark

or

reset

methods. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

The stream will not be buffered, and it will not support the

mark

or

reset

methods. The
stream will be safe for access by multiple concurrent threads. Closing
the stream will in turn cause the channel to be closed.

newOutputStream

```java
public static
OutputStream
newOutputStream​(
AsynchronousByteChannel
ch)
```

Constructs a stream that writes bytes to the given channel.

The stream will not be buffered. The stream will be safe for access
by multiple concurrent threads. Closing the stream will in turn cause
the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Returns:** A new output stream
**Since:** 1.7

---

#### newOutputStream

public static

OutputStream

newOutputStream​(

AsynchronousByteChannel

ch)

Constructs a stream that writes bytes to the given channel.

The stream will not be buffered. The stream will be safe for access
by multiple concurrent threads. Closing the stream will in turn cause
the channel to be closed.

The stream will not be buffered. The stream will be safe for access
by multiple concurrent threads. Closing the stream will in turn cause
the channel to be closed.

newChannel

```java
public static
ReadableByteChannel
newChannel​(
InputStream
in)
```

Constructs a channel that reads bytes from the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:** in

- The stream from which bytes are to be read
**Returns:** A new readable byte channel

---

#### newChannel

public static

ReadableByteChannel

newChannel​(

InputStream

in)

Constructs a channel that reads bytes from the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

newChannel

```java
public static
WritableByteChannel
newChannel​(
OutputStream
out)
```

Constructs a channel that writes bytes to the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

**Parameters:** out

- The stream to which bytes are to be written
**Returns:** A new writable byte channel

---

#### newChannel

public static

WritableByteChannel

newChannel​(

OutputStream

out)

Constructs a channel that writes bytes to the given stream.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

The resulting channel will not be buffered; it will simply redirect
its I/O operations to the given stream. Closing the channel will in
turn cause the stream to be closed.

newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

CharsetDecoder
dec,
int minBufferCap)
```

Constructs a reader that decodes bytes from the given channel using the
given decoder.

The resulting stream will contain an internal input buffer of at
least

minBufferCap

bytes. The stream's

read

methods
will, as needed, fill the buffer by reading bytes from the underlying
channel; if the channel is in non-blocking mode when bytes are to be
read then an

IllegalBlockingModeException

will be thrown. The
resulting stream will not otherwise be buffered, and it will not support
the

mark

or

reset

methods.
Closing the stream will in turn cause the channel to be closed.

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** dec

- The charset decoder to be used
**Parameters:** minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used
**Returns:** A new reader

---

#### newReader

public static

Reader

newReader​(

ReadableByteChannel

ch,

CharsetDecoder

dec,
int minBufferCap)

Constructs a reader that decodes bytes from the given channel using the
given decoder.

The resulting stream will contain an internal input buffer of at
least

minBufferCap

bytes. The stream's

read

methods
will, as needed, fill the buffer by reading bytes from the underlying
channel; if the channel is in non-blocking mode when bytes are to be
read then an

IllegalBlockingModeException

will be thrown. The
resulting stream will not otherwise be buffered, and it will not support
the

mark

or

reset

methods.
Closing the stream will in turn cause the channel to be closed.

The resulting stream will contain an internal input buffer of at
least

minBufferCap

bytes. The stream's

read

methods
will, as needed, fill the buffer by reading bytes from the underlying
channel; if the channel is in non-blocking mode when bytes are to be
read then an

IllegalBlockingModeException

will be thrown. The
resulting stream will not otherwise be buffered, and it will not support
the

mark

or

reset

methods.
Closing the stream will in turn cause the channel to be closed.

newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

String
csName)
```

Constructs a reader that decodes bytes from the given channel according
to the named charset.

An invocation of this method of the form

```java
Channels.newReader(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName))
```

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** csName

- The name of the charset to be used
**Returns:** A new reader
**Throws:** UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

---

#### newReader

public static

Reader

newReader​(

ReadableByteChannel

ch,

String

csName)

Constructs a reader that decodes bytes from the given channel according
to the named charset.

An invocation of this method of the form

```java
Channels.newReader(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName))
```

An invocation of this method of the form

```java
Channels.newReader(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName))
```

Channels.newReader(ch, csname)

Channels.newReader(ch, Charset.forName(csName))

newReader

```java
public static
Reader
newReader​(
ReadableByteChannel
ch,

Charset
charset)
```

Constructs a reader that decodes bytes from the given channel according
to the given charset.

An invocation of this method of the form

```java
Channels.newReader(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName).newDecoder(), -1)
```

The reader's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetDecoder

should be used.

**Parameters:** ch

- The channel from which bytes will be read
**Parameters:** charset

- The charset to be used
**Returns:** A new reader

---

#### newReader

public static

Reader

newReader​(

ReadableByteChannel

ch,

Charset

charset)

Constructs a reader that decodes bytes from the given channel according
to the given charset.

An invocation of this method of the form

```java
Channels.newReader(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName).newDecoder(), -1)
```

The reader's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetDecoder

should be used.

An invocation of this method of the form

```java
Channels.newReader(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newReader(ch, Charset.forName(csName).newDecoder(), -1)
```

The reader's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetDecoder

should be used.

Channels.newReader(ch, charset)

Channels.newReader(ch, Charset.forName(csName).newDecoder(), -1)

The reader's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetDecoder

should be used.

newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

CharsetEncoder
enc,
int minBufferCap)
```

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

The resulting stream will contain an internal output buffer of at
least

minBufferCap

bytes. The stream's

write

methods
will, as needed, flush the buffer by writing bytes to the underlying
channel; if the channel is in non-blocking mode when bytes are to be
written then an

IllegalBlockingModeException

will be thrown.
The resulting stream will not otherwise be buffered. Closing the stream
will in turn cause the channel to be closed.

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** enc

- The charset encoder to be used
**Parameters:** minBufferCap

- The minimum capacity of the internal byte buffer,
or

-1

if an implementation-dependent
default capacity is to be used
**Returns:** A new writer

---

#### newWriter

public static

Writer

newWriter​(

WritableByteChannel

ch,

CharsetEncoder

enc,
int minBufferCap)

Constructs a writer that encodes characters using the given encoder and
writes the resulting bytes to the given channel.

The resulting stream will contain an internal output buffer of at
least

minBufferCap

bytes. The stream's

write

methods
will, as needed, flush the buffer by writing bytes to the underlying
channel; if the channel is in non-blocking mode when bytes are to be
written then an

IllegalBlockingModeException

will be thrown.
The resulting stream will not otherwise be buffered. Closing the stream
will in turn cause the channel to be closed.

The resulting stream will contain an internal output buffer of at
least

minBufferCap

bytes. The stream's

write

methods
will, as needed, flush the buffer by writing bytes to the underlying
channel; if the channel is in non-blocking mode when bytes are to be
written then an

IllegalBlockingModeException

will be thrown.
The resulting stream will not otherwise be buffered. Closing the stream
will in turn cause the channel to be closed.

newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

String
csName)
```

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName))
```

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** csName

- The name of the charset to be used
**Returns:** A new writer
**Throws:** UnsupportedCharsetException

- If no support for the named charset is available
in this instance of the Java virtual machine

---

#### newWriter

public static

Writer

newWriter​(

WritableByteChannel

ch,

String

csName)

Constructs a writer that encodes characters according to the named
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName))
```

An invocation of this method of the form

```java
Channels.newWriter(ch, csname)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName))
```

Channels.newWriter(ch, csname)

Channels.newWriter(ch, Charset.forName(csName))

newWriter

```java
public static
Writer
newWriter​(
WritableByteChannel
ch,

Charset
charset)
```

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName).newEncoder(), -1)
```

The writer's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetEncoder

should be used.

**Parameters:** ch

- The channel to which bytes will be written
**Parameters:** charset

- The charset to be used
**Returns:** A new writer

---

#### newWriter

public static

Writer

newWriter​(

WritableByteChannel

ch,

Charset

charset)

Constructs a writer that encodes characters according to the given
charset and writes the resulting bytes to the given channel.

An invocation of this method of the form

```java
Channels.newWriter(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName).newEncoder(), -1)
```

The writer's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetEncoder

should be used.

An invocation of this method of the form

```java
Channels.newWriter(ch, charset)
```

behaves in exactly the same way as the expression

```java
Channels.newWriter(ch, Charset.forName(csName).newEncoder(), -1)
```

The writer's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetEncoder

should be used.

Channels.newWriter(ch, charset)

Channels.newWriter(ch, Charset.forName(csName).newEncoder(), -1)

The writer's default action for malformed-input and unmappable-character
errors is to

report

them. When more control over the error handling is required, the constructor
that takes a

CharsetEncoder

should be used.

---

