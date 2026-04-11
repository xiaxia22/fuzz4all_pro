# Class LineNumberReader

**Source:** `java.base\java\io\LineNumberReader.html`

### Class Description

```java
public class
LineNumberReader

extends
BufferedReader
```

A buffered character-input stream that keeps track of line numbers. This
class defines methods

setLineNumber(int)

and

getLineNumber()

for setting and getting the current line number
respectively.

By default, line numbering begins at 0. This number increments at every

line terminator

as the data is read, and can be changed
with a call to

setLineNumber(int)

. Note however, that

setLineNumber(int)

does not actually change the current position in
the stream; it only changes the value that will be returned by

getLineNumber()

.

A line is considered to be

terminated

by any one of a
line feed ('\n'), a carriage return ('\r'), or a carriage return followed
immediately by a linefeed.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

*No entries found.*

### Constructor Details

#### public LineNumberReader​(
Reader
in)

Create a new line-numbering reader, using the default input-buffer
size.

**Parameters:**
- in

- A Reader object to provide the underlying stream

---

#### public LineNumberReader​(
Reader
in,
int sz)

Create a new line-numbering reader, reading characters into a buffer of
the given size.

**Parameters:**
- in

- A Reader object to provide the underlying stream
- sz

- An int specifying the size of the buffer

---

### Method Details

#### public void setLineNumber​(int lineNumber)

Set the current line number.

**Parameters:**
- lineNumber

- An int specifying the line number

**See Also:**
- getLineNumber()

---

#### public int getLineNumber()

Get the current line number.

**Returns:**
- The current line number

**See Also:**
- setLineNumber(int)

---

#### public int read()
throws
IOException

Read a single character.

Line terminators

are
compressed into single newline ('\n') characters. Whenever a line
terminator is read the current line number is incremented.

**Overrides:**
- read

in class

BufferedReader

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

Read characters into a portion of an array. Whenever a

line terminator

is read the current line number is
incremented.

**Overrides:**
- read

in class

BufferedReader

**Parameters:**
- cbuf

- Destination buffer
- off

- Offset at which to start storing characters
- len

- Maximum number of characters to read

**Returns:**
- The number of bytes read, or -1 if the end of the stream has
already been reached

**Throws:**
- IOException

- If an I/O error occurs
- IndexOutOfBoundsException

- If an I/O error occurs

---

#### public
String
readLine()
throws
IOException

Read a line of text. Whenever a

line terminator

is
read the current line number is incremented.

**Overrides:**
- readLine

in class

BufferedReader

**Returns:**
- A String containing the contents of the line, not including
any

line termination characters

, or

null

if the end of the stream has been reached

**Throws:**
- IOException

- If an I/O error occurs

**See Also:**
- Files.readAllLines(java.nio.file.Path, java.nio.charset.Charset)

---

#### public long skip​(long n)
throws
IOException

Skip characters.

**Overrides:**
- skip

in class

BufferedReader

**Parameters:**
- n

- The number of characters to skip

**Returns:**
- The number of characters actually skipped

**Throws:**
- IOException

- If an I/O error occurs
- IllegalArgumentException

- If

n

is negative

---

#### public void mark​(int readAheadLimit)
throws
IOException

Mark the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point, and will also reset
the line number appropriately.

**Overrides:**
- mark

in class

BufferedReader

**Parameters:**
- readAheadLimit

- Limit on the number of characters that may be read while still
preserving the mark. After reading this many characters,
attempting to reset the stream may fail.

**Throws:**
- IOException

- If an I/O error occurs

---

#### public void reset()
throws
IOException

Reset the stream to the most recent mark.

**Overrides:**
- reset

in class

BufferedReader

**Throws:**
- IOException

- If the stream has not been marked, or if the mark has been
invalidated

---

### Additional Sections

#### Class LineNumberReader

java.lang.Object

- java.io.Reader
- - java.io.BufferedReader
- - java.io.LineNumberReader

java.io.Reader

- java.io.BufferedReader
- - java.io.LineNumberReader

java.io.BufferedReader

- java.io.LineNumberReader

java.io.LineNumberReader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

```java
public class
LineNumberReader

extends
BufferedReader
```

A buffered character-input stream that keeps track of line numbers. This
class defines methods

setLineNumber(int)

and

getLineNumber()

for setting and getting the current line number
respectively.

By default, line numbering begins at 0. This number increments at every

line terminator

as the data is read, and can be changed
with a call to

setLineNumber(int)

. Note however, that

setLineNumber(int)

does not actually change the current position in
the stream; it only changes the value that will be returned by

getLineNumber()

.

A line is considered to be

terminated

by any one of a
line feed ('\n'), a carriage return ('\r'), or a carriage return followed
immediately by a linefeed.

**Since:** 1.1

public class

LineNumberReader

extends

BufferedReader

A buffered character-input stream that keeps track of line numbers. This
class defines methods

setLineNumber(int)

and

getLineNumber()

for setting and getting the current line number
respectively.

By default, line numbering begins at 0. This number increments at every

line terminator

as the data is read, and can be changed
with a call to

setLineNumber(int)

. Note however, that

setLineNumber(int)

does not actually change the current position in
the stream; it only changes the value that will be returned by

getLineNumber()

.

A line is considered to be

terminated

by any one of a
line feed ('\n'), a carriage return ('\r'), or a carriage return followed
immediately by a linefeed.

By default, line numbering begins at 0. This number increments at every

line terminator

as the data is read, and can be changed
with a call to

setLineNumber(int)

. Note however, that

setLineNumber(int)

does not actually change the current position in
the stream; it only changes the value that will be returned by

getLineNumber()

.

A line is considered to be

terminated

by any one of a
line feed ('\n'), a carriage return ('\r'), or a carriage return followed
immediately by a linefeed.

A line is considered to be

terminated

by any one of a
line feed ('\n'), a carriage return ('\r'), or a carriage return followed
immediately by a linefeed.

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

LineNumberReader

​(

Reader

in)

Create a new line-numbering reader, using the default input-buffer
size.

LineNumberReader

​(

Reader

in,
int sz)

Create a new line-numbering reader, reading characters into a buffer of
the given size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getLineNumber

()

Get the current line number.

void

mark

​(int readAheadLimit)

Mark the present position in the stream.

int

read

()

Read a single character.

int

read

​(char[] cbuf,
int off,
int len)

Read characters into a portion of an array.

String

readLine

()

Read a line of text.

void

reset

()

Reset the stream to the most recent mark.

void

setLineNumber

​(int lineNumber)

Set the current line number.

long

skip

​(long n)

Skip characters.

- Methods declared in class java.io.

BufferedReader

lines

,

markSupported

,

ready

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

LineNumberReader

​(

Reader

in)

Create a new line-numbering reader, using the default input-buffer
size.

LineNumberReader

​(

Reader

in,
int sz)

Create a new line-numbering reader, reading characters into a buffer of
the given size.

---

#### Constructor Summary

Create a new line-numbering reader, using the default input-buffer
size.

Create a new line-numbering reader, reading characters into a buffer of
the given size.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getLineNumber

()

Get the current line number.

void

mark

​(int readAheadLimit)

Mark the present position in the stream.

int

read

()

Read a single character.

int

read

​(char[] cbuf,
int off,
int len)

Read characters into a portion of an array.

String

readLine

()

Read a line of text.

void

reset

()

Reset the stream to the most recent mark.

void

setLineNumber

​(int lineNumber)

Set the current line number.

long

skip

​(long n)

Skip characters.

- Methods declared in class java.io.

BufferedReader

lines

,

markSupported

,

ready

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

Get the current line number.

Mark the present position in the stream.

Read a single character.

Read characters into a portion of an array.

Read a line of text.

Reset the stream to the most recent mark.

Set the current line number.

Skip characters.

Methods declared in class java.io.

BufferedReader

lines

,

markSupported

,

ready

---

#### Methods declared in class java.io. BufferedReader

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LineNumberReader

```java
public LineNumberReader​(
Reader
in)
```

Create a new line-numbering reader, using the default input-buffer
size.

**Parameters:** in

- A Reader object to provide the underlying stream

- LineNumberReader

```java
public LineNumberReader​(
Reader
in,
int sz)
```

Create a new line-numbering reader, reading characters into a buffer of
the given size.

**Parameters:** in

- A Reader object to provide the underlying stream
**Parameters:** sz

- An int specifying the size of the buffer

============ METHOD DETAIL ==========

- Method Detail

- setLineNumber

```java
public void setLineNumber​(int lineNumber)
```

Set the current line number.

**Parameters:** lineNumber

- An int specifying the line number
**See Also:** getLineNumber()

- getLineNumber

```java
public int getLineNumber()
```

Get the current line number.

**Returns:** The current line number
**See Also:** setLineNumber(int)

- read

```java
public int read()
throws
IOException
```

Read a single character.

Line terminators

are
compressed into single newline ('\n') characters. Whenever a line
terminator is read the current line number is incremented.

**Overrides:** read

in class

BufferedReader
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

Read characters into a portion of an array. Whenever a

line terminator

is read the current line number is
incremented.

**Overrides:** read

in class

BufferedReader
**Parameters:** cbuf

- Destination buffer
**Parameters:** off

- Offset at which to start storing characters
**Parameters:** len

- Maximum number of characters to read
**Returns:** The number of bytes read, or -1 if the end of the stream has
already been reached
**Throws:** IOException

- If an I/O error occurs
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- readLine

```java
public
String
readLine()
throws
IOException
```

Read a line of text. Whenever a

line terminator

is
read the current line number is incremented.

**Overrides:** readLine

in class

BufferedReader
**Returns:** A String containing the contents of the line, not including
any

line termination characters

, or

null

if the end of the stream has been reached
**Throws:** IOException

- If an I/O error occurs
**See Also:** Files.readAllLines(java.nio.file.Path, java.nio.charset.Charset)

- skip

```java
public long skip​(long n)
throws
IOException
```

Skip characters.

**Overrides:** skip

in class

BufferedReader
**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IOException

- If an I/O error occurs
**Throws:** IllegalArgumentException

- If

n

is negative

- mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Mark the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point, and will also reset
the line number appropriately.

**Overrides:** mark

in class

BufferedReader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be read while still
preserving the mark. After reading this many characters,
attempting to reset the stream may fail.
**Throws:** IOException

- If an I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Reset the stream to the most recent mark.

**Overrides:** reset

in class

BufferedReader
**Throws:** IOException

- If the stream has not been marked, or if the mark has been
invalidated

Constructor Detail

- LineNumberReader

```java
public LineNumberReader​(
Reader
in)
```

Create a new line-numbering reader, using the default input-buffer
size.

**Parameters:** in

- A Reader object to provide the underlying stream

- LineNumberReader

```java
public LineNumberReader​(
Reader
in,
int sz)
```

Create a new line-numbering reader, reading characters into a buffer of
the given size.

**Parameters:** in

- A Reader object to provide the underlying stream
**Parameters:** sz

- An int specifying the size of the buffer

---

#### Constructor Detail

LineNumberReader

```java
public LineNumberReader​(
Reader
in)
```

Create a new line-numbering reader, using the default input-buffer
size.

**Parameters:** in

- A Reader object to provide the underlying stream

---

#### LineNumberReader

public LineNumberReader​(

Reader

in)

Create a new line-numbering reader, using the default input-buffer
size.

LineNumberReader

```java
public LineNumberReader​(
Reader
in,
int sz)
```

Create a new line-numbering reader, reading characters into a buffer of
the given size.

**Parameters:** in

- A Reader object to provide the underlying stream
**Parameters:** sz

- An int specifying the size of the buffer

---

#### LineNumberReader

public LineNumberReader​(

Reader

in,
int sz)

Create a new line-numbering reader, reading characters into a buffer of
the given size.

Method Detail

- setLineNumber

```java
public void setLineNumber​(int lineNumber)
```

Set the current line number.

**Parameters:** lineNumber

- An int specifying the line number
**See Also:** getLineNumber()

- getLineNumber

```java
public int getLineNumber()
```

Get the current line number.

**Returns:** The current line number
**See Also:** setLineNumber(int)

- read

```java
public int read()
throws
IOException
```

Read a single character.

Line terminators

are
compressed into single newline ('\n') characters. Whenever a line
terminator is read the current line number is incremented.

**Overrides:** read

in class

BufferedReader
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

Read characters into a portion of an array. Whenever a

line terminator

is read the current line number is
incremented.

**Overrides:** read

in class

BufferedReader
**Parameters:** cbuf

- Destination buffer
**Parameters:** off

- Offset at which to start storing characters
**Parameters:** len

- Maximum number of characters to read
**Returns:** The number of bytes read, or -1 if the end of the stream has
already been reached
**Throws:** IOException

- If an I/O error occurs
**Throws:** IndexOutOfBoundsException

- If an I/O error occurs

- readLine

```java
public
String
readLine()
throws
IOException
```

Read a line of text. Whenever a

line terminator

is
read the current line number is incremented.

**Overrides:** readLine

in class

BufferedReader
**Returns:** A String containing the contents of the line, not including
any

line termination characters

, or

null

if the end of the stream has been reached
**Throws:** IOException

- If an I/O error occurs
**See Also:** Files.readAllLines(java.nio.file.Path, java.nio.charset.Charset)

- skip

```java
public long skip​(long n)
throws
IOException
```

Skip characters.

**Overrides:** skip

in class

BufferedReader
**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IOException

- If an I/O error occurs
**Throws:** IllegalArgumentException

- If

n

is negative

- mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Mark the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point, and will also reset
the line number appropriately.

**Overrides:** mark

in class

BufferedReader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be read while still
preserving the mark. After reading this many characters,
attempting to reset the stream may fail.
**Throws:** IOException

- If an I/O error occurs

- reset

```java
public void reset()
throws
IOException
```

Reset the stream to the most recent mark.

**Overrides:** reset

in class

BufferedReader
**Throws:** IOException

- If the stream has not been marked, or if the mark has been
invalidated

---

#### Method Detail

setLineNumber

```java
public void setLineNumber​(int lineNumber)
```

Set the current line number.

**Parameters:** lineNumber

- An int specifying the line number
**See Also:** getLineNumber()

---

#### setLineNumber

public void setLineNumber​(int lineNumber)

Set the current line number.

getLineNumber

```java
public int getLineNumber()
```

Get the current line number.

**Returns:** The current line number
**See Also:** setLineNumber(int)

---

#### getLineNumber

public int getLineNumber()

Get the current line number.

read

```java
public int read()
throws
IOException
```

Read a single character.

Line terminators

are
compressed into single newline ('\n') characters. Whenever a line
terminator is read the current line number is incremented.

**Overrides:** read

in class

BufferedReader
**Returns:** The character read, or -1 if the end of the stream has been
reached
**Throws:** IOException

- If an I/O error occurs

---

#### read

public int read()
throws

IOException

Read a single character.

Line terminators

are
compressed into single newline ('\n') characters. Whenever a line
terminator is read the current line number is incremented.

read

```java
public int read​(char[] cbuf,
int off,
int len)
throws
IOException
```

Read characters into a portion of an array. Whenever a

line terminator

is read the current line number is
incremented.

**Overrides:** read

in class

BufferedReader
**Parameters:** cbuf

- Destination buffer
**Parameters:** off

- Offset at which to start storing characters
**Parameters:** len

- Maximum number of characters to read
**Returns:** The number of bytes read, or -1 if the end of the stream has
already been reached
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

Read characters into a portion of an array. Whenever a

line terminator

is read the current line number is
incremented.

readLine

```java
public
String
readLine()
throws
IOException
```

Read a line of text. Whenever a

line terminator

is
read the current line number is incremented.

**Overrides:** readLine

in class

BufferedReader
**Returns:** A String containing the contents of the line, not including
any

line termination characters

, or

null

if the end of the stream has been reached
**Throws:** IOException

- If an I/O error occurs
**See Also:** Files.readAllLines(java.nio.file.Path, java.nio.charset.Charset)

---

#### readLine

public

String

readLine()
throws

IOException

Read a line of text. Whenever a

line terminator

is
read the current line number is incremented.

skip

```java
public long skip​(long n)
throws
IOException
```

Skip characters.

**Overrides:** skip

in class

BufferedReader
**Parameters:** n

- The number of characters to skip
**Returns:** The number of characters actually skipped
**Throws:** IOException

- If an I/O error occurs
**Throws:** IllegalArgumentException

- If

n

is negative

---

#### skip

public long skip​(long n)
throws

IOException

Skip characters.

mark

```java
public void mark​(int readAheadLimit)
throws
IOException
```

Mark the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point, and will also reset
the line number appropriately.

**Overrides:** mark

in class

BufferedReader
**Parameters:** readAheadLimit

- Limit on the number of characters that may be read while still
preserving the mark. After reading this many characters,
attempting to reset the stream may fail.
**Throws:** IOException

- If an I/O error occurs

---

#### mark

public void mark​(int readAheadLimit)
throws

IOException

Mark the present position in the stream. Subsequent calls to reset()
will attempt to reposition the stream to this point, and will also reset
the line number appropriately.

reset

```java
public void reset()
throws
IOException
```

Reset the stream to the most recent mark.

**Overrides:** reset

in class

BufferedReader
**Throws:** IOException

- If the stream has not been marked, or if the mark has been
invalidated

---

#### reset

public void reset()
throws

IOException

Reset the stream to the most recent mark.

---

