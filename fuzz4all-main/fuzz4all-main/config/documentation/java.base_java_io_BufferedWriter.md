# Class BufferedWriter

**Source:** `java.base\java\io\BufferedWriter.html`

### Class Description

```java
public class
BufferedWriter

extends
Writer
```

Writes text to a character-output stream, buffering characters so as to
provide for the efficient writing of single characters, arrays, and strings.

The buffer size may be specified, or the default size may be accepted.
The default is large enough for most purposes.

A newLine() method is provided, which uses the platform's own notion of
line separator as defined by the system property

line.separator

.
Not all platforms use the newline character ('\n') to terminate lines.
Calling this method to terminate each output line is therefore preferred to
writing a newline character directly.

In general, a Writer sends its output immediately to the underlying
character or byte stream. Unless prompt output is required, it is advisable
to wrap a BufferedWriter around any Writer whose write() operations may be
costly, such as FileWriters and OutputStreamWriters. For example,

```java
PrintWriter out
= new PrintWriter(new BufferedWriter(new FileWriter("foo.out")));
```

will buffer the PrintWriter's output to the file. Without buffering, each
invocation of a print() method would cause characters to be converted into
bytes that would then be written immediately to the file, which can be very
inefficient.

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

#### public BufferedWriter​(
Writer
out)

Creates a buffered character-output stream that uses a default-sized
output buffer.

**Parameters:**
- out

- A Writer

---

#### public BufferedWriter​(
Writer
out,
int sz)

Creates a new buffered character-output stream that uses an output
buffer of the given size.

**Parameters:**
- out

- A Writer
- sz

- Output-buffer size, a positive integer

**Throws:**
- IllegalArgumentException

- If

sz <= 0

---

### Method Details

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

Ordinarily this method stores characters from the given array into
this stream's buffer, flushing the buffer to the underlying stream as
needed. If the requested length is at least as large as the buffer,
however, then this method will flush the buffer and write the characters
directly to the underlying stream. Thus redundant

BufferedWriter

s will not copy data unnecessarily.

**Specified by:**
- write

in class

Writer

**Parameters:**
- cbuf

- A character array
- off

- Offset from which to start reading characters
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
s,
int off,
int len)
throws
IOException

Writes a portion of a String.

**Overrides:**
- write

in class

Writer

**Parameters:**
- s

- String to be written
- off

- Offset from which to start reading characters
- len

- Number of characters to be written

**Throws:**
- IndexOutOfBoundsException

- If

off

is negative,
or

off + len

is greater than the length
of the given string
- IOException

- If an I/O error occurs

**Implementation Requirements:**
- While the specification of this method in the

superclass

recommends that an

IndexOutOfBoundsException

be thrown
if

len

is negative or

off + len

is negative,
the implementation in this class does not throw such an exception in
these cases but instead simply writes no characters.

---

#### public void newLine()
throws
IOException

Writes a line separator. The line separator string is defined by the
system property

line.separator

, and is not necessarily a single
newline ('\n') character.

**Throws:**
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

#### Class BufferedWriter

java.lang.Object

- java.io.Writer
- - java.io.BufferedWriter

java.io.Writer

- java.io.BufferedWriter

java.io.BufferedWriter

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

```java
public class
BufferedWriter

extends
Writer
```

Writes text to a character-output stream, buffering characters so as to
provide for the efficient writing of single characters, arrays, and strings.

The buffer size may be specified, or the default size may be accepted.
The default is large enough for most purposes.

A newLine() method is provided, which uses the platform's own notion of
line separator as defined by the system property

line.separator

.
Not all platforms use the newline character ('\n') to terminate lines.
Calling this method to terminate each output line is therefore preferred to
writing a newline character directly.

In general, a Writer sends its output immediately to the underlying
character or byte stream. Unless prompt output is required, it is advisable
to wrap a BufferedWriter around any Writer whose write() operations may be
costly, such as FileWriters and OutputStreamWriters. For example,

```java
PrintWriter out
= new PrintWriter(new BufferedWriter(new FileWriter("foo.out")));
```

will buffer the PrintWriter's output to the file. Without buffering, each
invocation of a print() method would cause characters to be converted into
bytes that would then be written immediately to the file, which can be very
inefficient.

**Since:** 1.1
**See Also:** PrintWriter

,

FileWriter

,

OutputStreamWriter

,

Files.newBufferedWriter(java.nio.file.Path, java.nio.charset.Charset, java.nio.file.OpenOption...)

public class

BufferedWriter

extends

Writer

Writes text to a character-output stream, buffering characters so as to
provide for the efficient writing of single characters, arrays, and strings.

The buffer size may be specified, or the default size may be accepted.
The default is large enough for most purposes.

A newLine() method is provided, which uses the platform's own notion of
line separator as defined by the system property

line.separator

.
Not all platforms use the newline character ('\n') to terminate lines.
Calling this method to terminate each output line is therefore preferred to
writing a newline character directly.

In general, a Writer sends its output immediately to the underlying
character or byte stream. Unless prompt output is required, it is advisable
to wrap a BufferedWriter around any Writer whose write() operations may be
costly, such as FileWriters and OutputStreamWriters. For example,

```java
PrintWriter out
= new PrintWriter(new BufferedWriter(new FileWriter("foo.out")));
```

will buffer the PrintWriter's output to the file. Without buffering, each
invocation of a print() method would cause characters to be converted into
bytes that would then be written immediately to the file, which can be very
inefficient.

The buffer size may be specified, or the default size may be accepted.
The default is large enough for most purposes.

A newLine() method is provided, which uses the platform's own notion of
line separator as defined by the system property

line.separator

.
Not all platforms use the newline character ('\n') to terminate lines.
Calling this method to terminate each output line is therefore preferred to
writing a newline character directly.

In general, a Writer sends its output immediately to the underlying
character or byte stream. Unless prompt output is required, it is advisable
to wrap a BufferedWriter around any Writer whose write() operations may be
costly, such as FileWriters and OutputStreamWriters. For example,

```java
PrintWriter out
= new PrintWriter(new BufferedWriter(new FileWriter("foo.out")));
```

will buffer the PrintWriter's output to the file. Without buffering, each
invocation of a print() method would cause characters to be converted into
bytes that would then be written immediately to the file, which can be very
inefficient.

A newLine() method is provided, which uses the platform's own notion of
line separator as defined by the system property

line.separator

.
Not all platforms use the newline character ('\n') to terminate lines.
Calling this method to terminate each output line is therefore preferred to
writing a newline character directly.

In general, a Writer sends its output immediately to the underlying
character or byte stream. Unless prompt output is required, it is advisable
to wrap a BufferedWriter around any Writer whose write() operations may be
costly, such as FileWriters and OutputStreamWriters. For example,

```java
PrintWriter out
= new PrintWriter(new BufferedWriter(new FileWriter("foo.out")));
```

will buffer the PrintWriter's output to the file. Without buffering, each
invocation of a print() method would cause characters to be converted into
bytes that would then be written immediately to the file, which can be very
inefficient.

In general, a Writer sends its output immediately to the underlying
character or byte stream. Unless prompt output is required, it is advisable
to wrap a BufferedWriter around any Writer whose write() operations may be
costly, such as FileWriters and OutputStreamWriters. For example,

```java
PrintWriter out
= new PrintWriter(new BufferedWriter(new FileWriter("foo.out")));
```

will buffer the PrintWriter's output to the file. Without buffering, each
invocation of a print() method would cause characters to be converted into
bytes that would then be written immediately to the file, which can be very
inefficient.

PrintWriter out
= new PrintWriter(new BufferedWriter(new FileWriter("foo.out")));

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

BufferedWriter

​(

Writer

out)

Creates a buffered character-output stream that uses a default-sized
output buffer.

BufferedWriter

​(

Writer

out,
int sz)

Creates a new buffered character-output stream that uses an output
buffer of the given size.

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

void

newLine

()

Writes a line separator.

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

s,
int off,
int len)

Writes a portion of a String.

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

BufferedWriter

​(

Writer

out)

Creates a buffered character-output stream that uses a default-sized
output buffer.

BufferedWriter

​(

Writer

out,
int sz)

Creates a new buffered character-output stream that uses an output
buffer of the given size.

---

#### Constructor Summary

Creates a buffered character-output stream that uses a default-sized
output buffer.

Creates a new buffered character-output stream that uses an output
buffer of the given size.

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

void

newLine

()

Writes a line separator.

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

s,
int off,
int len)

Writes a portion of a String.

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

Writes a line separator.

Writes a portion of an array of characters.

Writes a single character.

Writes a portion of a String.

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

- BufferedWriter

```java
public BufferedWriter​(
Writer
out)
```

Creates a buffered character-output stream that uses a default-sized
output buffer.

**Parameters:** out

- A Writer

- BufferedWriter

```java
public BufferedWriter​(
Writer
out,
int sz)
```

Creates a new buffered character-output stream that uses an output
buffer of the given size.

**Parameters:** out

- A Writer
**Parameters:** sz

- Output-buffer size, a positive integer
**Throws:** IllegalArgumentException

- If

sz <= 0

============ METHOD DETAIL ==========

- Method Detail

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

Ordinarily this method stores characters from the given array into
this stream's buffer, flushing the buffer to the underlying stream as
needed. If the requested length is at least as large as the buffer,
however, then this method will flush the buffer and write the characters
directly to the underlying stream. Thus redundant

BufferedWriter

s will not copy data unnecessarily.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- A character array
**Parameters:** off

- Offset from which to start reading characters
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
s,
int off,
int len)
throws
IOException
```

Writes a portion of a String.

**Overrides:** write

in class

Writer
**Implementation Requirements:** While the specification of this method in the

superclass

recommends that an

IndexOutOfBoundsException

be thrown
if

len

is negative or

off + len

is negative,
the implementation in this class does not throw such an exception in
these cases but instead simply writes no characters.
**Parameters:** s

- String to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If

off

is negative,
or

off + len

is greater than the length
of the given string
**Throws:** IOException

- If an I/O error occurs

- newLine

```java
public void newLine()
throws
IOException
```

Writes a line separator. The line separator string is defined by the
system property

line.separator

, and is not necessarily a single
newline ('\n') character.

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

- BufferedWriter

```java
public BufferedWriter​(
Writer
out)
```

Creates a buffered character-output stream that uses a default-sized
output buffer.

**Parameters:** out

- A Writer

- BufferedWriter

```java
public BufferedWriter​(
Writer
out,
int sz)
```

Creates a new buffered character-output stream that uses an output
buffer of the given size.

**Parameters:** out

- A Writer
**Parameters:** sz

- Output-buffer size, a positive integer
**Throws:** IllegalArgumentException

- If

sz <= 0

---

#### Constructor Detail

BufferedWriter

```java
public BufferedWriter​(
Writer
out)
```

Creates a buffered character-output stream that uses a default-sized
output buffer.

**Parameters:** out

- A Writer

---

#### BufferedWriter

public BufferedWriter​(

Writer

out)

Creates a buffered character-output stream that uses a default-sized
output buffer.

BufferedWriter

```java
public BufferedWriter​(
Writer
out,
int sz)
```

Creates a new buffered character-output stream that uses an output
buffer of the given size.

**Parameters:** out

- A Writer
**Parameters:** sz

- Output-buffer size, a positive integer
**Throws:** IllegalArgumentException

- If

sz <= 0

---

#### BufferedWriter

public BufferedWriter​(

Writer

out,
int sz)

Creates a new buffered character-output stream that uses an output
buffer of the given size.

Method Detail

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

Ordinarily this method stores characters from the given array into
this stream's buffer, flushing the buffer to the underlying stream as
needed. If the requested length is at least as large as the buffer,
however, then this method will flush the buffer and write the characters
directly to the underlying stream. Thus redundant

BufferedWriter

s will not copy data unnecessarily.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- A character array
**Parameters:** off

- Offset from which to start reading characters
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
s,
int off,
int len)
throws
IOException
```

Writes a portion of a String.

**Overrides:** write

in class

Writer
**Implementation Requirements:** While the specification of this method in the

superclass

recommends that an

IndexOutOfBoundsException

be thrown
if

len

is negative or

off + len

is negative,
the implementation in this class does not throw such an exception in
these cases but instead simply writes no characters.
**Parameters:** s

- String to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If

off

is negative,
or

off + len

is greater than the length
of the given string
**Throws:** IOException

- If an I/O error occurs

- newLine

```java
public void newLine()
throws
IOException
```

Writes a line separator. The line separator string is defined by the
system property

line.separator

, and is not necessarily a single
newline ('\n') character.

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

Ordinarily this method stores characters from the given array into
this stream's buffer, flushing the buffer to the underlying stream as
needed. If the requested length is at least as large as the buffer,
however, then this method will flush the buffer and write the characters
directly to the underlying stream. Thus redundant

BufferedWriter

s will not copy data unnecessarily.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- A character array
**Parameters:** off

- Offset from which to start reading characters
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

Ordinarily this method stores characters from the given array into
this stream's buffer, flushing the buffer to the underlying stream as
needed. If the requested length is at least as large as the buffer,
however, then this method will flush the buffer and write the characters
directly to the underlying stream. Thus redundant

BufferedWriter

s will not copy data unnecessarily.

Ordinarily this method stores characters from the given array into
this stream's buffer, flushing the buffer to the underlying stream as
needed. If the requested length is at least as large as the buffer,
however, then this method will flush the buffer and write the characters
directly to the underlying stream. Thus redundant

BufferedWriter

s will not copy data unnecessarily.

write

```java
public void write​(
String
s,
int off,
int len)
throws
IOException
```

Writes a portion of a String.

**Overrides:** write

in class

Writer
**Implementation Requirements:** While the specification of this method in the

superclass

recommends that an

IndexOutOfBoundsException

be thrown
if

len

is negative or

off + len

is negative,
the implementation in this class does not throw such an exception in
these cases but instead simply writes no characters.
**Parameters:** s

- String to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If

off

is negative,
or

off + len

is greater than the length
of the given string
**Throws:** IOException

- If an I/O error occurs

---

#### write

public void write​(

String

s,
int off,
int len)
throws

IOException

Writes a portion of a String.

newLine

```java
public void newLine()
throws
IOException
```

Writes a line separator. The line separator string is defined by the
system property

line.separator

, and is not necessarily a single
newline ('\n') character.

**Throws:** IOException

- If an I/O error occurs

---

#### newLine

public void newLine()
throws

IOException

Writes a line separator. The line separator string is defined by the
system property

line.separator

, and is not necessarily a single
newline ('\n') character.

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

