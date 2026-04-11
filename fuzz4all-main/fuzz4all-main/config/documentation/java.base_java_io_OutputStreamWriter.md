# Class OutputStreamWriter

**Source:** `java.base\java\io\OutputStreamWriter.html`

### Class Description

```java
public class
OutputStreamWriter

extends
Writer
```

An OutputStreamWriter is a bridge from character streams to byte streams:
Characters written to it are encoded into bytes using a specified

charset

. The charset that it uses
may be specified by name or may be given explicitly, or the platform's
default charset may be accepted.

Each invocation of a write() method causes the encoding converter to be
invoked on the given character(s). The resulting bytes are accumulated in a
buffer before being written to the underlying output stream. Note that the
characters passed to the write() methods are not buffered.

For top efficiency, consider wrapping an OutputStreamWriter within a
BufferedWriter so as to avoid frequent converter invocations. For example:

```java
Writer out
= new BufferedWriter(new OutputStreamWriter(System.out));
```

A

surrogate pair

is a character represented by a sequence of two

char

values: A

high

surrogate in the range '\uD800' to
'\uDBFF' followed by a

low

surrogate in the range '\uDC00' to
'\uDFFF'.

A

malformed surrogate element

is a high surrogate that is not
followed by a low surrogate or a low surrogate that is not preceded by a
high surrogate.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public OutputStreamWriter​(
OutputStream
out,

String
charsetName)
throws
UnsupportedEncodingException

Creates an OutputStreamWriter that uses the named charset.

**Parameters:**
- out

- An OutputStream
- charsetName

- The name of a supported

charset

**Throws:**
- UnsupportedEncodingException

- If the named encoding is not supported

---

#### public OutputStreamWriter​(
OutputStream
out)

Creates an OutputStreamWriter that uses the default character encoding.

**Parameters:**
- out

- An OutputStream

---

#### public OutputStreamWriter​(
OutputStream
out,

Charset
cs)

Creates an OutputStreamWriter that uses the given charset.

**Parameters:**
- out

- An OutputStream
- cs

- A charset

**Since:**
- 1.4

---

#### public OutputStreamWriter​(
OutputStream
out,

CharsetEncoder
enc)

Creates an OutputStreamWriter that uses the given charset encoder.

**Parameters:**
- out

- An OutputStream
- enc

- A charset encoder

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

OutputStreamWriter(OutputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method may return

null

if the stream has
been closed.

**Returns:**
- The historical name of this encoding, or possibly

null

if the stream has been closed

**See Also:**
- Charset

---

#### public void write​(int c)
throws
IOException

Writes a single character.

**Overrides:**
- write

in class

Writer

**Parameters:**
- c

- int specifying a character to be written

**Throws:**
- IOException

- If an I/O error occurs

---

#### public void write​(char[] cbuf,
int off,
int len)
throws
IOException

Writes a portion of an array of characters.

**Specified by:**
- write

in class

Writer

**Parameters:**
- cbuf

- Buffer of characters
- off

- Offset from which to start writing characters
- len

- Number of characters to write

**Throws:**
- IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
- IOException

- If an I/O error occurs

---

#### public void write​(
String
str,
int off,
int len)
throws
IOException

Writes a portion of a string.

**Overrides:**
- write

in class

Writer

**Parameters:**
- str

- A String
- off

- Offset from which to start writing characters
- len

- Number of characters to write

**Throws:**
- IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given string
- IOException

- If an I/O error occurs

---

#### public void flush()
throws
IOException

Flushes the stream.

**Specified by:**
- flush

in interface

Flushable
- flush

in class

Writer

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class OutputStreamWriter

java.lang.Object

- java.io.Writer
- - java.io.OutputStreamWriter

java.io.Writer

- java.io.OutputStreamWriter

java.io.OutputStreamWriter

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

**Direct Known Subclasses:** FileWriter

```java
public class
OutputStreamWriter

extends
Writer
```

An OutputStreamWriter is a bridge from character streams to byte streams:
Characters written to it are encoded into bytes using a specified

charset

. The charset that it uses
may be specified by name or may be given explicitly, or the platform's
default charset may be accepted.

Each invocation of a write() method causes the encoding converter to be
invoked on the given character(s). The resulting bytes are accumulated in a
buffer before being written to the underlying output stream. Note that the
characters passed to the write() methods are not buffered.

For top efficiency, consider wrapping an OutputStreamWriter within a
BufferedWriter so as to avoid frequent converter invocations. For example:

```java
Writer out
= new BufferedWriter(new OutputStreamWriter(System.out));
```

A

surrogate pair

is a character represented by a sequence of two

char

values: A

high

surrogate in the range '\uD800' to
'\uDBFF' followed by a

low

surrogate in the range '\uDC00' to
'\uDFFF'.

A

malformed surrogate element

is a high surrogate that is not
followed by a low surrogate or a low surrogate that is not preceded by a
high surrogate.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

**Since:** 1.1
**See Also:** BufferedWriter

,

OutputStream

,

Charset

public class

OutputStreamWriter

extends

Writer

An OutputStreamWriter is a bridge from character streams to byte streams:
Characters written to it are encoded into bytes using a specified

charset

. The charset that it uses
may be specified by name or may be given explicitly, or the platform's
default charset may be accepted.

Each invocation of a write() method causes the encoding converter to be
invoked on the given character(s). The resulting bytes are accumulated in a
buffer before being written to the underlying output stream. Note that the
characters passed to the write() methods are not buffered.

For top efficiency, consider wrapping an OutputStreamWriter within a
BufferedWriter so as to avoid frequent converter invocations. For example:

```java
Writer out
= new BufferedWriter(new OutputStreamWriter(System.out));
```

A

surrogate pair

is a character represented by a sequence of two

char

values: A

high

surrogate in the range '\uD800' to
'\uDBFF' followed by a

low

surrogate in the range '\uDC00' to
'\uDFFF'.

A

malformed surrogate element

is a high surrogate that is not
followed by a low surrogate or a low surrogate that is not preceded by a
high surrogate.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

Each invocation of a write() method causes the encoding converter to be
invoked on the given character(s). The resulting bytes are accumulated in a
buffer before being written to the underlying output stream. Note that the
characters passed to the write() methods are not buffered.

For top efficiency, consider wrapping an OutputStreamWriter within a
BufferedWriter so as to avoid frequent converter invocations. For example:

```java
Writer out
= new BufferedWriter(new OutputStreamWriter(System.out));
```

A

surrogate pair

is a character represented by a sequence of two

char

values: A

high

surrogate in the range '\uD800' to
'\uDBFF' followed by a

low

surrogate in the range '\uDC00' to
'\uDFFF'.

A

malformed surrogate element

is a high surrogate that is not
followed by a low surrogate or a low surrogate that is not preceded by a
high surrogate.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

For top efficiency, consider wrapping an OutputStreamWriter within a
BufferedWriter so as to avoid frequent converter invocations. For example:

```java
Writer out
= new BufferedWriter(new OutputStreamWriter(System.out));
```

A

surrogate pair

is a character represented by a sequence of two

char

values: A

high

surrogate in the range '\uD800' to
'\uDBFF' followed by a

low

surrogate in the range '\uDC00' to
'\uDFFF'.

A

malformed surrogate element

is a high surrogate that is not
followed by a low surrogate or a low surrogate that is not preceded by a
high surrogate.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

Writer out
= new BufferedWriter(new OutputStreamWriter(System.out));

A

surrogate pair

is a character represented by a sequence of two

char

values: A

high

surrogate in the range '\uD800' to
'\uDBFF' followed by a

low

surrogate in the range '\uDC00' to
'\uDFFF'.

A

malformed surrogate element

is a high surrogate that is not
followed by a low surrogate or a low surrogate that is not preceded by a
high surrogate.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

A

malformed surrogate element

is a high surrogate that is not
followed by a low surrogate or a low surrogate that is not preceded by a
high surrogate.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

This class always replaces malformed surrogate elements and unmappable
character sequences with the charset's default

substitution sequence

.
The

CharsetEncoder

class should be used when more
control over the encoding process is required.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

Writer

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OutputStreamWriter

​(

OutputStream

out)

Creates an OutputStreamWriter that uses the default character encoding.

OutputStreamWriter

​(

OutputStream

out,

String

charsetName)

Creates an OutputStreamWriter that uses the named charset.

OutputStreamWriter

​(

OutputStream

out,

Charset

cs)

Creates an OutputStreamWriter that uses the given charset.

OutputStreamWriter

​(

OutputStream

out,

CharsetEncoder

enc)

Creates an OutputStreamWriter that uses the given charset encoder.

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

Flushes the stream.

String

getEncoding

()

Returns the name of the character encoding being used by this stream.

void

write

​(char[] cbuf,
int off,
int len)

Writes a portion of an array of characters.

void

write

​(int c)

Writes a single character.

void

write

​(

String

str,
int off,
int len)

Writes a portion of a string.

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

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

Writer

lock

---

#### Field Summary

Fields declared in class java.io.

Writer

lock

---

#### Fields declared in class java.io. Writer

Constructor Summary

Constructors

Constructor

Description

OutputStreamWriter

​(

OutputStream

out)

Creates an OutputStreamWriter that uses the default character encoding.

OutputStreamWriter

​(

OutputStream

out,

String

charsetName)

Creates an OutputStreamWriter that uses the named charset.

OutputStreamWriter

​(

OutputStream

out,

Charset

cs)

Creates an OutputStreamWriter that uses the given charset.

OutputStreamWriter

​(

OutputStream

out,

CharsetEncoder

enc)

Creates an OutputStreamWriter that uses the given charset encoder.

---

#### Constructor Summary

Creates an OutputStreamWriter that uses the default character encoding.

Creates an OutputStreamWriter that uses the named charset.

Creates an OutputStreamWriter that uses the given charset.

Creates an OutputStreamWriter that uses the given charset encoder.

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

Flushes the stream.

String

getEncoding

()

Returns the name of the character encoding being used by this stream.

void

write

​(char[] cbuf,
int off,
int len)

Writes a portion of an array of characters.

void

write

​(int c)

Writes a single character.

void

write

​(

String

str,
int off,
int len)

Writes a portion of a string.

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

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

Flushes the stream.

Returns the name of the character encoding being used by this stream.

Writes a portion of an array of characters.

Writes a single character.

Writes a portion of a string.

Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

---

#### Methods declared in class java.io. Writer

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

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

String
charsetName)
throws
UnsupportedEncodingException
```

Creates an OutputStreamWriter that uses the named charset.

**Parameters:** out

- An OutputStream
**Parameters:** charsetName

- The name of a supported

charset
**Throws:** UnsupportedEncodingException

- If the named encoding is not supported

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out)
```

Creates an OutputStreamWriter that uses the default character encoding.

**Parameters:** out

- An OutputStream

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

Charset
cs)
```

Creates an OutputStreamWriter that uses the given charset.

**Parameters:** out

- An OutputStream
**Parameters:** cs

- A charset
**Since:** 1.4

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

CharsetEncoder
enc)
```

Creates an OutputStreamWriter that uses the given charset encoder.

**Parameters:** out

- An OutputStream
**Parameters:** enc

- A charset encoder
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

OutputStreamWriter(OutputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method may return

null

if the stream has
been closed.

**Returns:** The historical name of this encoding, or possibly

null

if the stream has been closed
**See Also:** Charset

- write

```java
public void write​(int c)
throws
IOException
```

Writes a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Buffer of characters
**Parameters:** off

- Offset from which to start writing characters
**Parameters:** len

- Number of characters to write
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(
String
str,
int off,
int len)
throws
IOException
```

Writes a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- A String
**Parameters:** off

- Offset from which to start writing characters
**Parameters:** len

- Number of characters to write
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given string
**Throws:** IOException

- If an I/O error occurs

- flush

```java
public void flush()
throws
IOException
```

Flushes the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- If an I/O error occurs

Constructor Detail

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

String
charsetName)
throws
UnsupportedEncodingException
```

Creates an OutputStreamWriter that uses the named charset.

**Parameters:** out

- An OutputStream
**Parameters:** charsetName

- The name of a supported

charset
**Throws:** UnsupportedEncodingException

- If the named encoding is not supported

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out)
```

Creates an OutputStreamWriter that uses the default character encoding.

**Parameters:** out

- An OutputStream

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

Charset
cs)
```

Creates an OutputStreamWriter that uses the given charset.

**Parameters:** out

- An OutputStream
**Parameters:** cs

- A charset
**Since:** 1.4

- OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

CharsetEncoder
enc)
```

Creates an OutputStreamWriter that uses the given charset encoder.

**Parameters:** out

- An OutputStream
**Parameters:** enc

- A charset encoder
**Since:** 1.4

---

#### Constructor Detail

OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

String
charsetName)
throws
UnsupportedEncodingException
```

Creates an OutputStreamWriter that uses the named charset.

**Parameters:** out

- An OutputStream
**Parameters:** charsetName

- The name of a supported

charset
**Throws:** UnsupportedEncodingException

- If the named encoding is not supported

---

#### OutputStreamWriter

public OutputStreamWriter​(

OutputStream

out,

String

charsetName)
throws

UnsupportedEncodingException

Creates an OutputStreamWriter that uses the named charset.

OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out)
```

Creates an OutputStreamWriter that uses the default character encoding.

**Parameters:** out

- An OutputStream

---

#### OutputStreamWriter

public OutputStreamWriter​(

OutputStream

out)

Creates an OutputStreamWriter that uses the default character encoding.

OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

Charset
cs)
```

Creates an OutputStreamWriter that uses the given charset.

**Parameters:** out

- An OutputStream
**Parameters:** cs

- A charset
**Since:** 1.4

---

#### OutputStreamWriter

public OutputStreamWriter​(

OutputStream

out,

Charset

cs)

Creates an OutputStreamWriter that uses the given charset.

OutputStreamWriter

```java
public OutputStreamWriter​(
OutputStream
out,

CharsetEncoder
enc)
```

Creates an OutputStreamWriter that uses the given charset encoder.

**Parameters:** out

- An OutputStream
**Parameters:** enc

- A charset encoder
**Since:** 1.4

---

#### OutputStreamWriter

public OutputStreamWriter​(

OutputStream

out,

CharsetEncoder

enc)

Creates an OutputStreamWriter that uses the given charset encoder.

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

OutputStreamWriter(OutputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method may return

null

if the stream has
been closed.

**Returns:** The historical name of this encoding, or possibly

null

if the stream has been closed
**See Also:** Charset

- write

```java
public void write​(int c)
throws
IOException
```

Writes a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Buffer of characters
**Parameters:** off

- Offset from which to start writing characters
**Parameters:** len

- Number of characters to write
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(
String
str,
int off,
int len)
throws
IOException
```

Writes a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- A String
**Parameters:** off

- Offset from which to start writing characters
**Parameters:** len

- Number of characters to write
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given string
**Throws:** IOException

- If an I/O error occurs

- flush

```java
public void flush()
throws
IOException
```

Flushes the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
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

OutputStreamWriter(OutputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method may return

null

if the stream has
been closed.

**Returns:** The historical name of this encoding, or possibly

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

OutputStreamWriter(OutputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method may return

null

if the stream has
been closed.

If the encoding has an historical name then that name is returned;
otherwise the encoding's canonical name is returned.

If this instance was created with the

OutputStreamWriter(OutputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method may return

null

if the stream has
been closed.

If this instance was created with the

OutputStreamWriter(OutputStream, String)

constructor then the returned
name, being unique for the encoding, may differ from the name passed to
the constructor. This method may return

null

if the stream has
been closed.

write

```java
public void write​(int c)
throws
IOException
```

Writes a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written
**Throws:** IOException

- If an I/O error occurs

---

#### write

public void write​(int c)
throws

IOException

Writes a single character.

write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Buffer of characters
**Parameters:** off

- Offset from which to start writing characters
**Parameters:** len

- Number of characters to write
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given array
**Throws:** IOException

- If an I/O error occurs

---

#### write

public void write​(char[] cbuf,
int off,
int len)
throws

IOException

Writes a portion of an array of characters.

write

```java
public void write​(
String
str,
int off,
int len)
throws
IOException
```

Writes a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- A String
**Parameters:** off

- Offset from which to start writing characters
**Parameters:** len

- Number of characters to write
**Throws:** IndexOutOfBoundsException

- If

off

is negative, or

len

is negative,
or

off + len

is negative or greater than the length
of the given string
**Throws:** IOException

- If an I/O error occurs

---

#### write

public void write​(

String

str,
int off,
int len)
throws

IOException

Writes a portion of a string.

flush

```java
public void flush()
throws
IOException
```

Flushes the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- If an I/O error occurs

---

#### flush

public void flush()
throws

IOException

Flushes the stream.

---

