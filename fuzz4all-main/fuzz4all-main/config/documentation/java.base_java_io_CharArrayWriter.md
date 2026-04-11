# Class CharArrayWriter

**Source:** `java.base\java\io\CharArrayWriter.html`

### Class Description

```java
public class
CharArrayWriter

extends
Writer
```

This class implements a character buffer that can be used as an Writer.
The buffer automatically grows when data is written to the stream. The data
can be retrieved using toCharArray() and toString().

Note: Invoking close() on this class has no effect, and methods
of this class can be called after the stream has closed
without generating an IOException.

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

---

### Field Details

#### protected char[] buf

The buffer where data is stored.

---

#### protected int count

The number of chars in the buffer.

---

### Constructor Details

#### public CharArrayWriter()

Creates a new CharArrayWriter.

---

#### public CharArrayWriter​(int initialSize)

Creates a new CharArrayWriter with the specified initial size.

**Parameters:**
- initialSize

- an int specifying the initial buffer size.

**Throws:**
- IllegalArgumentException

- if initialSize is negative

---

### Method Details

#### public void write​(int c)

Writes a character to the buffer.

**Overrides:**
- write

in class

Writer

**Parameters:**
- c

- int specifying a character to be written

---

#### public void write​(char[] c,
int off,
int len)

Writes characters to the buffer.

**Specified by:**
- write

in class

Writer

**Parameters:**
- c

- the data to be written
- off

- the start offset in the data
- len

- the number of chars that are written

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

---

#### public void write​(
String
str,
int off,
int len)

Write a portion of a string to the buffer.

**Overrides:**
- write

in class

Writer

**Parameters:**
- str

- String to be written from
- off

- Offset from which to start reading characters
- len

- Number of characters to be written

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

---

#### public void writeTo​(
Writer
out)
throws
IOException

Writes the contents of the buffer to another character stream.

**Parameters:**
- out

- the output stream to write to

**Throws:**
- IOException

- If an I/O error occurs.

---

#### public
CharArrayWriter
append​(
CharSequence
csq)

Appends the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq)

behaves in exactly the same way as the invocation

```java
out.write(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a
character buffer will return a subsequence whose content depends upon
the buffer's position and limit.

**Specified by:**
- append

in interface

Appendable

**Overrides:**
- append

in class

Writer

**Parameters:**
- csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this writer.

**Returns:**
- This writer

**Since:**
- 1.5

---

#### public
CharArrayWriter
append​(
CharSequence
csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.write(csq.subSequence(start, end).toString())
```

**Specified by:**
- append

in interface

Appendable

**Overrides:**
- append

in class

Writer

**Parameters:**
- csq

- The character sequence from which a subsequence will be
appended. If

csq

is

null

, then characters
will be appended as if

csq

contained the four
characters

"null"

.
- start

- The index of the first character in the subsequence
- end

- The index of the character following the last character in the
subsequence

**Returns:**
- This writer

**Throws:**
- IndexOutOfBoundsException

- If

start

or

end

are negative,

start

is greater than

end

, or

end

is greater than

csq.length()

**Since:**
- 1.5

---

#### public
CharArrayWriter
append​(char c)

Appends the specified character to this writer.

An invocation of this method of the form

out.append(c)

behaves in exactly the same way as the invocation

```java
out.write(c)
```

**Specified by:**
- append

in interface

Appendable

**Overrides:**
- append

in class

Writer

**Parameters:**
- c

- The 16-bit character to append

**Returns:**
- This writer

**Since:**
- 1.5

---

#### public void reset()

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

---

#### public char[] toCharArray()

Returns a copy of the input data.

**Returns:**
- an array of chars copied from the input data.

---

#### public int size()

Returns the current size of the buffer.

**Returns:**
- an int representing the current size of the buffer.

---

#### public
String
toString()

Converts input data to a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string.

---

#### public void flush()

Flush the stream.

**Specified by:**
- flush

in interface

Flushable
- flush

in class

Writer

---

#### public void close()

Close the stream. This method does not release the buffer, since its
contents might still be required. Note: Invoking this method in this class
will have no effect.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable
- close

in class

Writer

---

### Additional Sections

#### Class CharArrayWriter

java.lang.Object

- java.io.Writer
- - java.io.CharArrayWriter

java.io.Writer

- java.io.CharArrayWriter

java.io.CharArrayWriter

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

```java
public class
CharArrayWriter

extends
Writer
```

This class implements a character buffer that can be used as an Writer.
The buffer automatically grows when data is written to the stream. The data
can be retrieved using toCharArray() and toString().

Note: Invoking close() on this class has no effect, and methods
of this class can be called after the stream has closed
without generating an IOException.

**Since:** 1.1

public class

CharArrayWriter

extends

Writer

This class implements a character buffer that can be used as an Writer.
The buffer automatically grows when data is written to the stream. The data
can be retrieved using toCharArray() and toString().

Note: Invoking close() on this class has no effect, and methods
of this class can be called after the stream has closed
without generating an IOException.

Note: Invoking close() on this class has no effect, and methods
of this class can be called after the stream has closed
without generating an IOException.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected char[]

buf

The buffer where data is stored.

protected int

count

The number of chars in the buffer.

- Fields declared in class java.io.

Writer

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CharArrayWriter

()

Creates a new CharArrayWriter.

CharArrayWriter

​(int initialSize)

Creates a new CharArrayWriter with the specified initial size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CharArrayWriter

append

​(char c)

Appends the specified character to this writer.

CharArrayWriter

append

​(

CharSequence

csq)

Appends the specified character sequence to this writer.

CharArrayWriter

append

​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this writer.

void

close

()

Close the stream.

void

flush

()

Flush the stream.

void

reset

()

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

int

size

()

Returns the current size of the buffer.

char[]

toCharArray

()

Returns a copy of the input data.

String

toString

()

Converts input data to a string.

void

write

​(char[] c,
int off,
int len)

Writes characters to the buffer.

void

write

​(int c)

Writes a character to the buffer.

void

write

​(

String

str,
int off,
int len)

Write a portion of a string to the buffer.

void

writeTo

​(

Writer

out)

Writes the contents of the buffer to another character stream.

- Methods declared in class java.io.

Writer

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

protected char[]

buf

The buffer where data is stored.

protected int

count

The number of chars in the buffer.

- Fields declared in class java.io.

Writer

lock

---

#### Field Summary

The buffer where data is stored.

The number of chars in the buffer.

Fields declared in class java.io.

Writer

lock

---

#### Fields declared in class java.io. Writer

Constructor Summary

Constructors

Constructor

Description

CharArrayWriter

()

Creates a new CharArrayWriter.

CharArrayWriter

​(int initialSize)

Creates a new CharArrayWriter with the specified initial size.

---

#### Constructor Summary

Creates a new CharArrayWriter.

Creates a new CharArrayWriter with the specified initial size.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CharArrayWriter

append

​(char c)

Appends the specified character to this writer.

CharArrayWriter

append

​(

CharSequence

csq)

Appends the specified character sequence to this writer.

CharArrayWriter

append

​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this writer.

void

close

()

Close the stream.

void

flush

()

Flush the stream.

void

reset

()

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

int

size

()

Returns the current size of the buffer.

char[]

toCharArray

()

Returns a copy of the input data.

String

toString

()

Converts input data to a string.

void

write

​(char[] c,
int off,
int len)

Writes characters to the buffer.

void

write

​(int c)

Writes a character to the buffer.

void

write

​(

String

str,
int off,
int len)

Write a portion of a string to the buffer.

void

writeTo

​(

Writer

out)

Writes the contents of the buffer to another character stream.

- Methods declared in class java.io.

Writer

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

wait

,

wait

,

wait

---

#### Method Summary

Appends the specified character to this writer.

Appends the specified character sequence to this writer.

Appends a subsequence of the specified character sequence to this writer.

Close the stream.

Flush the stream.

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

Returns the current size of the buffer.

Returns a copy of the input data.

Converts input data to a string.

Writes characters to the buffer.

Writes a character to the buffer.

Write a portion of a string to the buffer.

Writes the contents of the buffer to another character stream.

Methods declared in class java.io.

Writer

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- buf

```java
protected char[] buf
```

The buffer where data is stored.

- count

```java
protected int count
```

The number of chars in the buffer.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CharArrayWriter

```java
public CharArrayWriter()
```

Creates a new CharArrayWriter.

- CharArrayWriter

```java
public CharArrayWriter​(int initialSize)
```

Creates a new CharArrayWriter with the specified initial size.

**Parameters:** initialSize

- an int specifying the initial buffer size.
**Throws:** IllegalArgumentException

- if initialSize is negative

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int c)
```

Writes a character to the buffer.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written

- write

```java
public void write​(char[] c,
int off,
int len)
```

Writes characters to the buffer.

**Specified by:** write

in class

Writer
**Parameters:** c

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of chars that are written
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

- write

```java
public void write​(
String
str,
int off,
int len)
```

Write a portion of a string to the buffer.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written from
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
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

- writeTo

```java
public void writeTo​(
Writer
out)
throws
IOException
```

Writes the contents of the buffer to another character stream.

**Parameters:** out

- the output stream to write to
**Throws:** IOException

- If an I/O error occurs.

- append

```java
public
CharArrayWriter
append​(
CharSequence
csq)
```

Appends the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq)

behaves in exactly the same way as the invocation

```java
out.write(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a
character buffer will return a subsequence whose content depends upon
the buffer's position and limit.

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this writer.
**Returns:** This writer
**Since:** 1.5

- append

```java
public
CharArrayWriter
append​(
CharSequence
csq,
int start,
int end)
```

Appends a subsequence of the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.write(csq.subSequence(start, end).toString())
```

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** csq

- The character sequence from which a subsequence will be
appended. If

csq

is

null

, then characters
will be appended as if

csq

contained the four
characters

"null"

.
**Parameters:** start

- The index of the first character in the subsequence
**Parameters:** end

- The index of the character following the last character in the
subsequence
**Returns:** This writer
**Throws:** IndexOutOfBoundsException

- If

start

or

end

are negative,

start

is greater than

end

, or

end

is greater than

csq.length()
**Since:** 1.5

- append

```java
public
CharArrayWriter
append​(char c)
```

Appends the specified character to this writer.

An invocation of this method of the form

out.append(c)

behaves in exactly the same way as the invocation

```java
out.write(c)
```

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** c

- The 16-bit character to append
**Returns:** This writer
**Since:** 1.5

- reset

```java
public void reset()
```

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

- toCharArray

```java
public char[] toCharArray()
```

Returns a copy of the input data.

**Returns:** an array of chars copied from the input data.

- size

```java
public int size()
```

Returns the current size of the buffer.

**Returns:** an int representing the current size of the buffer.

- toString

```java
public
String
toString()
```

Converts input data to a string.

**Overrides:** toString

in class

Object
**Returns:** the string.

- flush

```java
public void flush()
```

Flush the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer

- close

```java
public void close()
```

Close the stream. This method does not release the buffer, since its
contents might still be required. Note: Invoking this method in this class
will have no effect.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer

Field Detail

- buf

```java
protected char[] buf
```

The buffer where data is stored.

- count

```java
protected int count
```

The number of chars in the buffer.

---

#### Field Detail

buf

```java
protected char[] buf
```

The buffer where data is stored.

---

#### buf

protected char[] buf

The buffer where data is stored.

count

```java
protected int count
```

The number of chars in the buffer.

---

#### count

protected int count

The number of chars in the buffer.

Constructor Detail

- CharArrayWriter

```java
public CharArrayWriter()
```

Creates a new CharArrayWriter.

- CharArrayWriter

```java
public CharArrayWriter​(int initialSize)
```

Creates a new CharArrayWriter with the specified initial size.

**Parameters:** initialSize

- an int specifying the initial buffer size.
**Throws:** IllegalArgumentException

- if initialSize is negative

---

#### Constructor Detail

CharArrayWriter

```java
public CharArrayWriter()
```

Creates a new CharArrayWriter.

---

#### CharArrayWriter

public CharArrayWriter()

Creates a new CharArrayWriter.

CharArrayWriter

```java
public CharArrayWriter​(int initialSize)
```

Creates a new CharArrayWriter with the specified initial size.

**Parameters:** initialSize

- an int specifying the initial buffer size.
**Throws:** IllegalArgumentException

- if initialSize is negative

---

#### CharArrayWriter

public CharArrayWriter​(int initialSize)

Creates a new CharArrayWriter with the specified initial size.

Method Detail

- write

```java
public void write​(int c)
```

Writes a character to the buffer.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written

- write

```java
public void write​(char[] c,
int off,
int len)
```

Writes characters to the buffer.

**Specified by:** write

in class

Writer
**Parameters:** c

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of chars that are written
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

- write

```java
public void write​(
String
str,
int off,
int len)
```

Write a portion of a string to the buffer.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written from
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
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

- writeTo

```java
public void writeTo​(
Writer
out)
throws
IOException
```

Writes the contents of the buffer to another character stream.

**Parameters:** out

- the output stream to write to
**Throws:** IOException

- If an I/O error occurs.

- append

```java
public
CharArrayWriter
append​(
CharSequence
csq)
```

Appends the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq)

behaves in exactly the same way as the invocation

```java
out.write(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a
character buffer will return a subsequence whose content depends upon
the buffer's position and limit.

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this writer.
**Returns:** This writer
**Since:** 1.5

- append

```java
public
CharArrayWriter
append​(
CharSequence
csq,
int start,
int end)
```

Appends a subsequence of the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.write(csq.subSequence(start, end).toString())
```

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** csq

- The character sequence from which a subsequence will be
appended. If

csq

is

null

, then characters
will be appended as if

csq

contained the four
characters

"null"

.
**Parameters:** start

- The index of the first character in the subsequence
**Parameters:** end

- The index of the character following the last character in the
subsequence
**Returns:** This writer
**Throws:** IndexOutOfBoundsException

- If

start

or

end

are negative,

start

is greater than

end

, or

end

is greater than

csq.length()
**Since:** 1.5

- append

```java
public
CharArrayWriter
append​(char c)
```

Appends the specified character to this writer.

An invocation of this method of the form

out.append(c)

behaves in exactly the same way as the invocation

```java
out.write(c)
```

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** c

- The 16-bit character to append
**Returns:** This writer
**Since:** 1.5

- reset

```java
public void reset()
```

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

- toCharArray

```java
public char[] toCharArray()
```

Returns a copy of the input data.

**Returns:** an array of chars copied from the input data.

- size

```java
public int size()
```

Returns the current size of the buffer.

**Returns:** an int representing the current size of the buffer.

- toString

```java
public
String
toString()
```

Converts input data to a string.

**Overrides:** toString

in class

Object
**Returns:** the string.

- flush

```java
public void flush()
```

Flush the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer

- close

```java
public void close()
```

Close the stream. This method does not release the buffer, since its
contents might still be required. Note: Invoking this method in this class
will have no effect.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer

---

#### Method Detail

write

```java
public void write​(int c)
```

Writes a character to the buffer.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written

---

#### write

public void write​(int c)

Writes a character to the buffer.

write

```java
public void write​(char[] c,
int off,
int len)
```

Writes characters to the buffer.

**Specified by:** write

in class

Writer
**Parameters:** c

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of chars that are written
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

---

#### write

public void write​(char[] c,
int off,
int len)

Writes characters to the buffer.

write

```java
public void write​(
String
str,
int off,
int len)
```

Write a portion of a string to the buffer.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written from
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
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

---

#### write

public void write​(

String

str,
int off,
int len)

Write a portion of a string to the buffer.

writeTo

```java
public void writeTo​(
Writer
out)
throws
IOException
```

Writes the contents of the buffer to another character stream.

**Parameters:** out

- the output stream to write to
**Throws:** IOException

- If an I/O error occurs.

---

#### writeTo

public void writeTo​(

Writer

out)
throws

IOException

Writes the contents of the buffer to another character stream.

append

```java
public
CharArrayWriter
append​(
CharSequence
csq)
```

Appends the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq)

behaves in exactly the same way as the invocation

```java
out.write(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a
character buffer will return a subsequence whose content depends upon
the buffer's position and limit.

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this writer.
**Returns:** This writer
**Since:** 1.5

---

#### append

public

CharArrayWriter

append​(

CharSequence

csq)

Appends the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq)

behaves in exactly the same way as the invocation

```java
out.write(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a
character buffer will return a subsequence whose content depends upon
the buffer's position and limit.

An invocation of this method of the form

out.append(csq)

behaves in exactly the same way as the invocation

```java
out.write(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a
character buffer will return a subsequence whose content depends upon
the buffer's position and limit.

out.write(csq.toString())

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a
character buffer will return a subsequence whose content depends upon
the buffer's position and limit.

append

```java
public
CharArrayWriter
append​(
CharSequence
csq,
int start,
int end)
```

Appends a subsequence of the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.write(csq.subSequence(start, end).toString())
```

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** csq

- The character sequence from which a subsequence will be
appended. If

csq

is

null

, then characters
will be appended as if

csq

contained the four
characters

"null"

.
**Parameters:** start

- The index of the first character in the subsequence
**Parameters:** end

- The index of the character following the last character in the
subsequence
**Returns:** This writer
**Throws:** IndexOutOfBoundsException

- If

start

or

end

are negative,

start

is greater than

end

, or

end

is greater than

csq.length()
**Since:** 1.5

---

#### append

public

CharArrayWriter

append​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this writer.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.write(csq.subSequence(start, end).toString())
```

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.write(csq.subSequence(start, end).toString())
```

out.write(csq.subSequence(start, end).toString())

append

```java
public
CharArrayWriter
append​(char c)
```

Appends the specified character to this writer.

An invocation of this method of the form

out.append(c)

behaves in exactly the same way as the invocation

```java
out.write(c)
```

**Specified by:** append

in interface

Appendable
**Overrides:** append

in class

Writer
**Parameters:** c

- The 16-bit character to append
**Returns:** This writer
**Since:** 1.5

---

#### append

public

CharArrayWriter

append​(char c)

Appends the specified character to this writer.

An invocation of this method of the form

out.append(c)

behaves in exactly the same way as the invocation

```java
out.write(c)
```

An invocation of this method of the form

out.append(c)

behaves in exactly the same way as the invocation

```java
out.write(c)
```

out.write(c)

reset

```java
public void reset()
```

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

---

#### reset

public void reset()

Resets the buffer so that you can use it again without
throwing away the already allocated buffer.

toCharArray

```java
public char[] toCharArray()
```

Returns a copy of the input data.

**Returns:** an array of chars copied from the input data.

---

#### toCharArray

public char[] toCharArray()

Returns a copy of the input data.

size

```java
public int size()
```

Returns the current size of the buffer.

**Returns:** an int representing the current size of the buffer.

---

#### size

public int size()

Returns the current size of the buffer.

toString

```java
public
String
toString()
```

Converts input data to a string.

**Overrides:** toString

in class

Object
**Returns:** the string.

---

#### toString

public

String

toString()

Converts input data to a string.

flush

```java
public void flush()
```

Flush the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer

---

#### flush

public void flush()

Flush the stream.

close

```java
public void close()
```

Close the stream. This method does not release the buffer, since its
contents might still be required. Note: Invoking this method in this class
will have no effect.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer

---

#### close

public void close()

Close the stream. This method does not release the buffer, since its
contents might still be required. Note: Invoking this method in this class
will have no effect.

---

