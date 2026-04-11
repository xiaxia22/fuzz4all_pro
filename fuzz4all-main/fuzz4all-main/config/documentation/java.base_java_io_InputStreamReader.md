# Class InputStreamReader

**Source:** `java.base\java\io\InputStreamReader.html`

### Class Description

```java
public class
InputStreamReader

extends
Reader
```

An InputStreamReader is a bridge from byte streams to character streams: It
reads bytes and decodes them into characters using a specified

charset

. The charset that it uses
may be specified by name or may be given explicitly, or the platform's
default charset may be accepted.

Each invocation of one of an InputStreamReader's read() methods may
cause one or more bytes to be read from the underlying byte-input stream.
To enable the efficient conversion of bytes to characters, more bytes may
be read ahead from the underlying stream than are necessary to satisfy the
current read operation.

For top efficiency, consider wrapping an InputStreamReader within a
BufferedReader. For example:

```java
BufferedReader in
= new BufferedReader(new InputStreamReader(System.in));
```

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InputStreamReader​(
InputStream
in)

Creates an InputStreamReader that uses the default charset.

**Parameters:**
- in

- An InputStream

---

#### public InputStreamReader​(
InputStream
in,

String
charsetName)
throws
UnsupportedEncodingException

Creates an InputStreamReader that uses the named charset.

**Parameters:**
- in

- An InputStream
- charsetName

- The name of a supported

charset

**Throws:**
- UnsupportedEncodingException

- If the named charset is not supported

---

#### public InputStreamReader​(
InputStream
in,

Charset
cs)

Creates an InputStreamReader that uses the given charset.

**Parameters:**
- in

- An InputStream
- cs

- A charset

**Since:**
- 1.4

---

#### public InputStreamReader​(
InputStream
in,

CharsetDecoder
dec)

Creates an InputStreamReader that uses the given charset decoder.

**Parameters:**
- in

- An InputStream
- dec

- A charset decoder

**Since:**
- 1.4

---

### Method Details

#### public
String
getEncoding()

Returns the name of the character encoding being used by this stream.

If the encoding has an historical name then that name is returned;
otherwise the encoding's canonical name is returned.

If this instance was created with the

InputStreamReader(InputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method will return

null

if the
stream has been closed.

**Returns:**
- The historical name of this encoding, or

null

if the stream has been closed

**See Also:**
- Charset

---

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
int offset,
int length)
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
- offset

- Offset at which to start storing characters
- length

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

#### public boolean ready()
throws
IOException

Tells whether this stream is ready to be read. An InputStreamReader is
ready if its input buffer is not empty, or if bytes are available to be
read from the underlying byte stream.

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

### Additional Sections

#### Class InputStreamReader

java.lang.Object

- java.io.Reader
- - java.io.InputStreamReader

java.io.Reader

- java.io.InputStreamReader

java.io.InputStreamReader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

**Direct Known Subclasses:** FileReader

```java
public class
InputStreamReader

extends
Reader
```

An InputStreamReader is a bridge from byte streams to character streams: It
reads bytes and decodes them into characters using a specified

charset

. The charset that it uses
may be specified by name or may be given explicitly, or the platform's
default charset may be accepted.

Each invocation of one of an InputStreamReader's read() methods may
cause one or more bytes to be read from the underlying byte-input stream.
To enable the efficient conversion of bytes to characters, more bytes may
be read ahead from the underlying stream than are necessary to satisfy the
current read operation.

For top efficiency, consider wrapping an InputStreamReader within a
BufferedReader. For example:

```java
BufferedReader in
= new BufferedReader(new InputStreamReader(System.in));
```

**Since:** 1.1
**See Also:** BufferedReader

,

InputStream

,

Charset

public class

InputStreamReader

extends

Reader

An InputStreamReader is a bridge from byte streams to character streams: It
reads bytes and decodes them into characters using a specified

charset

. The charset that it uses
may be specified by name or may be given explicitly, or the platform's
default charset may be accepted.

Each invocation of one of an InputStreamReader's read() methods may
cause one or more bytes to be read from the underlying byte-input stream.
To enable the efficient conversion of bytes to characters, more bytes may
be read ahead from the underlying stream than are necessary to satisfy the
current read operation.

For top efficiency, consider wrapping an InputStreamReader within a
BufferedReader. For example:

```java
BufferedReader in
= new BufferedReader(new InputStreamReader(System.in));
```

Each invocation of one of an InputStreamReader's read() methods may
cause one or more bytes to be read from the underlying byte-input stream.
To enable the efficient conversion of bytes to characters, more bytes may
be read ahead from the underlying stream than are necessary to satisfy the
current read operation.

For top efficiency, consider wrapping an InputStreamReader within a
BufferedReader. For example:

```java
BufferedReader in
= new BufferedReader(new InputStreamReader(System.in));
```

For top efficiency, consider wrapping an InputStreamReader within a
BufferedReader. For example:

```java
BufferedReader in
= new BufferedReader(new InputStreamReader(System.in));
```

BufferedReader in
= new BufferedReader(new InputStreamReader(System.in));

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

InputStreamReader

​(

InputStream

in)

Creates an InputStreamReader that uses the default charset.

InputStreamReader

​(

InputStream

in,

String

charsetName)

Creates an InputStreamReader that uses the named charset.

InputStreamReader

​(

InputStream

in,

Charset

cs)

Creates an InputStreamReader that uses the given charset.

InputStreamReader

​(

InputStream

in,

CharsetDecoder

dec)

Creates an InputStreamReader that uses the given charset decoder.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getEncoding

()

Returns the name of the character encoding being used by this stream.

int

read

()

Reads a single character.

int

read

​(char[] cbuf,
int offset,
int length)

Reads characters into a portion of an array.

boolean

ready

()

Tells whether this stream is ready to be read.

- Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

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

InputStreamReader

​(

InputStream

in)

Creates an InputStreamReader that uses the default charset.

InputStreamReader

​(

InputStream

in,

String

charsetName)

Creates an InputStreamReader that uses the named charset.

InputStreamReader

​(

InputStream

in,

Charset

cs)

Creates an InputStreamReader that uses the given charset.

InputStreamReader

​(

InputStream

in,

CharsetDecoder

dec)

Creates an InputStreamReader that uses the given charset decoder.

---

#### Constructor Summary

Creates an InputStreamReader that uses the default charset.

Creates an InputStreamReader that uses the named charset.

Creates an InputStreamReader that uses the given charset.

Creates an InputStreamReader that uses the given charset decoder.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getEncoding

()

Returns the name of the character encoding being used by this stream.

int

read

()

Reads a single character.

int

read

​(char[] cbuf,
int offset,
int length)

Reads characters into a portion of an array.

boolean

ready

()

Tells whether this stream is ready to be read.

- Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

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

Returns the name of the character encoding being used by this stream.

Reads a single character.

Reads characters into a portion of an array.

Tells whether this stream is ready to be read.

Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

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

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in)
```

Creates an InputStreamReader that uses the default charset.

**Parameters:** in

- An InputStream

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

String
charsetName)
throws
UnsupportedEncodingException
```

Creates an InputStreamReader that uses the named charset.

**Parameters:** in

- An InputStream
**Parameters:** charsetName

- The name of a supported

charset
**Throws:** UnsupportedEncodingException

- If the named charset is not supported

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

Charset
cs)
```

Creates an InputStreamReader that uses the given charset.

**Parameters:** in

- An InputStream
**Parameters:** cs

- A charset
**Since:** 1.4

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

CharsetDecoder
dec)
```

Creates an InputStreamReader that uses the given charset decoder.

**Parameters:** in

- An InputStream
**Parameters:** dec

- A charset decoder
**Since:** 1.4

============ METHOD DETAIL ==========

- Method Detail

- getEncoding

```java
public
String
getEncoding()
```

Returns the name of the character encoding being used by this stream.

If the encoding has an historical name then that name is returned;
otherwise the encoding's canonical name is returned.

If this instance was created with the

InputStreamReader(InputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method will return

null

if the
stream has been closed.

**Returns:** The historical name of this encoding, or

null

if the stream has been closed
**See Also:** Charset

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
int offset,
int length)
throws
IOException
```

Reads characters into a portion of an array.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- Destination buffer
**Parameters:** offset

- Offset at which to start storing characters
**Parameters:** length

- Maximum number of characters to read
**Returns:** The number of characters read, or -1 if the end of the
stream has been reached
**Throws:** IOException

- If an I/O error occurs
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read. An InputStreamReader is
ready if its input buffer is not empty, or if bytes are available to be
read from the underlying byte stream.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- If an I/O error occurs

Constructor Detail

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in)
```

Creates an InputStreamReader that uses the default charset.

**Parameters:** in

- An InputStream

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

String
charsetName)
throws
UnsupportedEncodingException
```

Creates an InputStreamReader that uses the named charset.

**Parameters:** in

- An InputStream
**Parameters:** charsetName

- The name of a supported

charset
**Throws:** UnsupportedEncodingException

- If the named charset is not supported

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

Charset
cs)
```

Creates an InputStreamReader that uses the given charset.

**Parameters:** in

- An InputStream
**Parameters:** cs

- A charset
**Since:** 1.4

- InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

CharsetDecoder
dec)
```

Creates an InputStreamReader that uses the given charset decoder.

**Parameters:** in

- An InputStream
**Parameters:** dec

- A charset decoder
**Since:** 1.4

---

#### Constructor Detail

InputStreamReader

```java
public InputStreamReader​(
InputStream
in)
```

Creates an InputStreamReader that uses the default charset.

**Parameters:** in

- An InputStream

---

#### InputStreamReader

public InputStreamReader​(

InputStream

in)

Creates an InputStreamReader that uses the default charset.

InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

String
charsetName)
throws
UnsupportedEncodingException
```

Creates an InputStreamReader that uses the named charset.

**Parameters:** in

- An InputStream
**Parameters:** charsetName

- The name of a supported

charset
**Throws:** UnsupportedEncodingException

- If the named charset is not supported

---

#### InputStreamReader

public InputStreamReader​(

InputStream

in,

String

charsetName)
throws

UnsupportedEncodingException

Creates an InputStreamReader that uses the named charset.

InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

Charset
cs)
```

Creates an InputStreamReader that uses the given charset.

**Parameters:** in

- An InputStream
**Parameters:** cs

- A charset
**Since:** 1.4

---

#### InputStreamReader

public InputStreamReader​(

InputStream

in,

Charset

cs)

Creates an InputStreamReader that uses the given charset.

InputStreamReader

```java
public InputStreamReader​(
InputStream
in,

CharsetDecoder
dec)
```

Creates an InputStreamReader that uses the given charset decoder.

**Parameters:** in

- An InputStream
**Parameters:** dec

- A charset decoder
**Since:** 1.4

---

#### InputStreamReader

public InputStreamReader​(

InputStream

in,

CharsetDecoder

dec)

Creates an InputStreamReader that uses the given charset decoder.

Method Detail

- getEncoding

```java
public
String
getEncoding()
```

Returns the name of the character encoding being used by this stream.

If the encoding has an historical name then that name is returned;
otherwise the encoding's canonical name is returned.

If this instance was created with the

InputStreamReader(InputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method will return

null

if the
stream has been closed.

**Returns:** The historical name of this encoding, or

null

if the stream has been closed
**See Also:** Charset

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
int offset,
int length)
throws
IOException
```

Reads characters into a portion of an array.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- Destination buffer
**Parameters:** offset

- Offset at which to start storing characters
**Parameters:** length

- Maximum number of characters to read
**Returns:** The number of characters read, or -1 if the end of the
stream has been reached
**Throws:** IOException

- If an I/O error occurs
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read. An InputStreamReader is
ready if its input buffer is not empty, or if bytes are available to be
read from the underlying byte stream.

**Overrides:** ready

in class

Reader
**Returns:** True if the next read() is guaranteed not to block for input,
false otherwise. Note that returning false does not guarantee that the
next read will block.
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

getEncoding

```java
public
String
getEncoding()
```

Returns the name of the character encoding being used by this stream.

If the encoding has an historical name then that name is returned;
otherwise the encoding's canonical name is returned.

If this instance was created with the

InputStreamReader(InputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method will return

null

if the
stream has been closed.

**Returns:** The historical name of this encoding, or

null

if the stream has been closed
**See Also:** Charset

---

#### getEncoding

public

String

getEncoding()

Returns the name of the character encoding being used by this stream.

If the encoding has an historical name then that name is returned;
otherwise the encoding's canonical name is returned.

If this instance was created with the

InputStreamReader(InputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method will return

null

if the
stream has been closed.

If the encoding has an historical name then that name is returned;
otherwise the encoding's canonical name is returned.

If this instance was created with the

InputStreamReader(InputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method will return

null

if the
stream has been closed.

If this instance was created with the

InputStreamReader(InputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method will return

null

if the
stream has been closed.

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
int offset,
int length)
throws
IOException
```

Reads characters into a portion of an array.

**Specified by:** read

in class

Reader
**Parameters:** cbuf

- Destination buffer
**Parameters:** offset

- Offset at which to start storing characters
**Parameters:** length

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
int offset,
int length)
throws

IOException

Reads characters into a portion of an array.

ready

```java
public boolean ready()
throws
IOException
```

Tells whether this stream is ready to be read. An InputStreamReader is
ready if its input buffer is not empty, or if bytes are available to be
read from the underlying byte stream.

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

Tells whether this stream is ready to be read. An InputStreamReader is
ready if its input buffer is not empty, or if bytes are available to be
read from the underlying byte stream.

---

