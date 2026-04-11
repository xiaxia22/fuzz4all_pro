# Class StringWriter

**Source:** `java.base\java\io\StringWriter.html`

### Class Description

```java
public class
StringWriter

extends
Writer
```

A character stream that collects its output in a string buffer, which can
then be used to construct a string.

Closing a

StringWriter

has no effect. The methods in this class
can be called after the stream has been closed without generating an

IOException

.

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

#### public StringWriter()

Create a new string writer using the default initial string-buffer
size.

---

#### public StringWriter​(int initialSize)

Create a new string writer using the specified initial string-buffer
size.

**Parameters:**
- initialSize

- The number of

char

values that will fit into this buffer
before it is automatically expanded

**Throws:**
- IllegalArgumentException

- If

initialSize

is negative

---

### Method Details

#### public void write​(int c)

Write a single character.

**Overrides:**
- write

in class

Writer

**Parameters:**
- c

- int specifying a character to be written

---

#### public void write​(char[] cbuf,
int off,
int len)

Write a portion of an array of characters.

**Specified by:**
- write

in class

Writer

**Parameters:**
- cbuf

- Array of characters
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

---

#### public void write​(
String
str)

Write a string.

**Overrides:**
- write

in class

Writer

**Parameters:**
- str

- String to be written

---

#### public void write​(
String
str,
int off,
int len)

Write a portion of a string.

**Overrides:**
- write

in class

Writer

**Parameters:**
- str

- String to be written
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

---

#### public
StringWriter
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
StringWriter
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
StringWriter
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

#### public
String
toString()

Return the buffer's current value as a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### public
StringBuffer
getBuffer()

Return the string buffer itself.

**Returns:**
- StringBuffer holding the current buffer value.

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
throws
IOException

Closing a

StringWriter

has no effect. The methods in this
class can be called after the stream has been closed without generating
an

IOException

.

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

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class StringWriter

java.lang.Object

- java.io.Writer
- - java.io.StringWriter

java.io.Writer

- java.io.StringWriter

java.io.StringWriter

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

```java
public class
StringWriter

extends
Writer
```

A character stream that collects its output in a string buffer, which can
then be used to construct a string.

Closing a

StringWriter

has no effect. The methods in this class
can be called after the stream has been closed without generating an

IOException

.

**Since:** 1.1

public class

StringWriter

extends

Writer

A character stream that collects its output in a string buffer, which can
then be used to construct a string.

Closing a

StringWriter

has no effect. The methods in this class
can be called after the stream has been closed without generating an

IOException

.

Closing a

StringWriter

has no effect. The methods in this class
can be called after the stream has been closed without generating an

IOException

.

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

StringWriter

()

Create a new string writer using the default initial string-buffer
size.

StringWriter

​(int initialSize)

Create a new string writer using the specified initial string-buffer
size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

StringWriter

append

​(char c)

Appends the specified character to this writer.

StringWriter

append

​(

CharSequence

csq)

Appends the specified character sequence to this writer.

StringWriter

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

Closing a

StringWriter

has no effect.

void

flush

()

Flush the stream.

StringBuffer

getBuffer

()

Return the string buffer itself.

String

toString

()

Return the buffer's current value as a string.

void

write

​(char[] cbuf,
int off,
int len)

Write a portion of an array of characters.

void

write

​(int c)

Write a single character.

void

write

​(

String

str)

Write a string.

void

write

​(

String

str,
int off,
int len)

Write a portion of a string.

- Methods declared in class java.io.

Writer

nullWriter

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

StringWriter

()

Create a new string writer using the default initial string-buffer
size.

StringWriter

​(int initialSize)

Create a new string writer using the specified initial string-buffer
size.

---

#### Constructor Summary

Create a new string writer using the default initial string-buffer
size.

Create a new string writer using the specified initial string-buffer
size.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

StringWriter

append

​(char c)

Appends the specified character to this writer.

StringWriter

append

​(

CharSequence

csq)

Appends the specified character sequence to this writer.

StringWriter

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

Closing a

StringWriter

has no effect.

void

flush

()

Flush the stream.

StringBuffer

getBuffer

()

Return the string buffer itself.

String

toString

()

Return the buffer's current value as a string.

void

write

​(char[] cbuf,
int off,
int len)

Write a portion of an array of characters.

void

write

​(int c)

Write a single character.

void

write

​(

String

str)

Write a string.

void

write

​(

String

str,
int off,
int len)

Write a portion of a string.

- Methods declared in class java.io.

Writer

nullWriter

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

Closing a

StringWriter

has no effect.

Flush the stream.

Return the string buffer itself.

Return the buffer's current value as a string.

Write a portion of an array of characters.

Write a single character.

Write a string.

Write a portion of a string.

Methods declared in class java.io.

Writer

nullWriter

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StringWriter

```java
public StringWriter()
```

Create a new string writer using the default initial string-buffer
size.

- StringWriter

```java
public StringWriter​(int initialSize)
```

Create a new string writer using the specified initial string-buffer
size.

**Parameters:** initialSize

- The number of

char

values that will fit into this buffer
before it is automatically expanded
**Throws:** IllegalArgumentException

- If

initialSize

is negative

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int c)
```

Write a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written

- write

```java
public void write​(char[] cbuf,
int off,
int len)
```

Write a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Array of characters
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

- write

```java
public void write​(
String
str)
```

Write a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written

- write

```java
public void write​(
String
str,
int off,
int len)
```

Write a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written
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

- append

```java
public
StringWriter
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
StringWriter
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
StringWriter
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

- toString

```java
public
String
toString()
```

Return the buffer's current value as a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getBuffer

```java
public
StringBuffer
getBuffer()
```

Return the string buffer itself.

**Returns:** StringBuffer holding the current buffer value.

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
throws
IOException
```

Closing a

StringWriter

has no effect. The methods in this
class can be called after the stream has been closed without generating
an

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer
**Throws:** IOException

- If an I/O error occurs

Constructor Detail

- StringWriter

```java
public StringWriter()
```

Create a new string writer using the default initial string-buffer
size.

- StringWriter

```java
public StringWriter​(int initialSize)
```

Create a new string writer using the specified initial string-buffer
size.

**Parameters:** initialSize

- The number of

char

values that will fit into this buffer
before it is automatically expanded
**Throws:** IllegalArgumentException

- If

initialSize

is negative

---

#### Constructor Detail

StringWriter

```java
public StringWriter()
```

Create a new string writer using the default initial string-buffer
size.

---

#### StringWriter

public StringWriter()

Create a new string writer using the default initial string-buffer
size.

StringWriter

```java
public StringWriter​(int initialSize)
```

Create a new string writer using the specified initial string-buffer
size.

**Parameters:** initialSize

- The number of

char

values that will fit into this buffer
before it is automatically expanded
**Throws:** IllegalArgumentException

- If

initialSize

is negative

---

#### StringWriter

public StringWriter​(int initialSize)

Create a new string writer using the specified initial string-buffer
size.

Method Detail

- write

```java
public void write​(int c)
```

Write a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written

- write

```java
public void write​(char[] cbuf,
int off,
int len)
```

Write a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Array of characters
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

- write

```java
public void write​(
String
str)
```

Write a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written

- write

```java
public void write​(
String
str,
int off,
int len)
```

Write a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written
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

- append

```java
public
StringWriter
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
StringWriter
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
StringWriter
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

- toString

```java
public
String
toString()
```

Return the buffer's current value as a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getBuffer

```java
public
StringBuffer
getBuffer()
```

Return the string buffer itself.

**Returns:** StringBuffer holding the current buffer value.

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
throws
IOException
```

Closing a

StringWriter

has no effect. The methods in this
class can be called after the stream has been closed without generating
an

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

write

```java
public void write​(int c)
```

Write a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written

---

#### write

public void write​(int c)

Write a single character.

write

```java
public void write​(char[] cbuf,
int off,
int len)
```

Write a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Array of characters
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

---

#### write

public void write​(char[] cbuf,
int off,
int len)

Write a portion of an array of characters.

write

```java
public void write​(
String
str)
```

Write a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written

---

#### write

public void write​(

String

str)

Write a string.

write

```java
public void write​(
String
str,
int off,
int len)
```

Write a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written
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

---

#### write

public void write​(

String

str,
int off,
int len)

Write a portion of a string.

append

```java
public
StringWriter
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

StringWriter

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
StringWriter
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

StringWriter

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
StringWriter
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

StringWriter

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

toString

```java
public
String
toString()
```

Return the buffer's current value as a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Return the buffer's current value as a string.

getBuffer

```java
public
StringBuffer
getBuffer()
```

Return the string buffer itself.

**Returns:** StringBuffer holding the current buffer value.

---

#### getBuffer

public

StringBuffer

getBuffer()

Return the string buffer itself.

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
throws
IOException
```

Closing a

StringWriter

has no effect. The methods in this
class can be called after the stream has been closed without generating
an

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Writer
**Throws:** IOException

- If an I/O error occurs

---

#### close

public void close()
throws

IOException

Closing a

StringWriter

has no effect. The methods in this
class can be called after the stream has been closed without generating
an

IOException

.

---

