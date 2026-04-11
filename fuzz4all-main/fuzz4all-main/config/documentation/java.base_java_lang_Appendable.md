# Interface Appendable

**Source:** `java.base\java\lang\Appendable.html`

### Class Description

```java
public interface
Appendable
```

An object to which

char

sequences and values can be appended. The

Appendable

interface must be implemented by any class whose
instances are intended to receive formatted output from a

Formatter

.

The characters to be appended should be valid Unicode characters as
described in

Unicode Character
Representation

. Note that supplementary characters may be composed of
multiple 16-bit

char

values.

Appendables are not necessarily safe for multithreaded access. Thread
safety is the responsibility of classes that extend and implement this
interface.

Since this interface may be implemented by existing classes
with different styles of error handling there is no guarantee that
errors will be propagated to the invoker.

**All Known Implementing Classes:** BufferedWriter

,

CharArrayWriter

,

CharBuffer

,

FileWriter

,

FilterWriter

,

LogStream

,

OutputStreamWriter

,

PipedWriter

,

PrintStream

,

PrintWriter

,

StringBuffer

,

StringBuilder

,

StringWriter

,

Writer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Appendable
append​(
CharSequence
csq)
throws
IOException

Appends the specified character sequence to this

Appendable

.

Depending on which class implements the character sequence

csq

, the entire sequence may not be appended. For
instance, if

csq

is a

CharBuffer

then
the subsequence to append is defined by the buffer's position and limit.

**Parameters:**
- csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this Appendable.

**Returns:**
- A reference to this

Appendable

**Throws:**
- IOException

- If an I/O error occurs

---

#### Appendable
append​(
CharSequence
csq,
int start,
int end)
throws
IOException

Appends a subsequence of the specified character sequence to this

Appendable

.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.append(csq.subSequence(start, end))
```

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
- A reference to this

Appendable

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
- IOException

- If an I/O error occurs

---

#### Appendable
append​(char c)
throws
IOException

Appends the specified character to this

Appendable

.

**Parameters:**
- c

- The character to append

**Returns:**
- A reference to this

Appendable

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Interface Appendable

**All Known Implementing Classes:** BufferedWriter

,

CharArrayWriter

,

CharBuffer

,

FileWriter

,

FilterWriter

,

LogStream

,

OutputStreamWriter

,

PipedWriter

,

PrintStream

,

PrintWriter

,

StringBuffer

,

StringBuilder

,

StringWriter

,

Writer

```java
public interface
Appendable
```

An object to which

char

sequences and values can be appended. The

Appendable

interface must be implemented by any class whose
instances are intended to receive formatted output from a

Formatter

.

The characters to be appended should be valid Unicode characters as
described in

Unicode Character
Representation

. Note that supplementary characters may be composed of
multiple 16-bit

char

values.

Appendables are not necessarily safe for multithreaded access. Thread
safety is the responsibility of classes that extend and implement this
interface.

Since this interface may be implemented by existing classes
with different styles of error handling there is no guarantee that
errors will be propagated to the invoker.

**Since:** 1.5

public interface

Appendable

An object to which

char

sequences and values can be appended. The

Appendable

interface must be implemented by any class whose
instances are intended to receive formatted output from a

Formatter

.

The characters to be appended should be valid Unicode characters as
described in

Unicode Character
Representation

. Note that supplementary characters may be composed of
multiple 16-bit

char

values.

Appendables are not necessarily safe for multithreaded access. Thread
safety is the responsibility of classes that extend and implement this
interface.

Since this interface may be implemented by existing classes
with different styles of error handling there is no guarantee that
errors will be propagated to the invoker.

The characters to be appended should be valid Unicode characters as
described in

Unicode Character
Representation

. Note that supplementary characters may be composed of
multiple 16-bit

char

values.

Appendables are not necessarily safe for multithreaded access. Thread
safety is the responsibility of classes that extend and implement this
interface.

Since this interface may be implemented by existing classes
with different styles of error handling there is no guarantee that
errors will be propagated to the invoker.

Appendables are not necessarily safe for multithreaded access. Thread
safety is the responsibility of classes that extend and implement this
interface.

Since this interface may be implemented by existing classes
with different styles of error handling there is no guarantee that
errors will be propagated to the invoker.

Since this interface may be implemented by existing classes
with different styles of error handling there is no guarantee that
errors will be propagated to the invoker.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Appendable

append

​(char c)

Appends the specified character to this

Appendable

.

Appendable

append

​(

CharSequence

csq)

Appends the specified character sequence to this

Appendable

.

Appendable

append

​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this

Appendable

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Appendable

append

​(char c)

Appends the specified character to this

Appendable

.

Appendable

append

​(

CharSequence

csq)

Appends the specified character sequence to this

Appendable

.

Appendable

append

​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this

Appendable

.

---

#### Method Summary

Appends the specified character to this

Appendable

.

Appends the specified character sequence to this

Appendable

.

Appends a subsequence of the specified character sequence to this

Appendable

.

============ METHOD DETAIL ==========

- Method Detail

- append

```java
Appendable
append​(
CharSequence
csq)
throws
IOException
```

Appends the specified character sequence to this

Appendable

.

Depending on which class implements the character sequence

csq

, the entire sequence may not be appended. For
instance, if

csq

is a

CharBuffer

then
the subsequence to append is defined by the buffer's position and limit.

**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this Appendable.
**Returns:** A reference to this

Appendable
**Throws:** IOException

- If an I/O error occurs

- append

```java
Appendable
append​(
CharSequence
csq,
int start,
int end)
throws
IOException
```

Appends a subsequence of the specified character sequence to this

Appendable

.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.append(csq.subSequence(start, end))
```

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
**Returns:** A reference to this

Appendable
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
**Throws:** IOException

- If an I/O error occurs

- append

```java
Appendable
append​(char c)
throws
IOException
```

Appends the specified character to this

Appendable

.

**Parameters:** c

- The character to append
**Returns:** A reference to this

Appendable
**Throws:** IOException

- If an I/O error occurs

Method Detail

- append

```java
Appendable
append​(
CharSequence
csq)
throws
IOException
```

Appends the specified character sequence to this

Appendable

.

Depending on which class implements the character sequence

csq

, the entire sequence may not be appended. For
instance, if

csq

is a

CharBuffer

then
the subsequence to append is defined by the buffer's position and limit.

**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this Appendable.
**Returns:** A reference to this

Appendable
**Throws:** IOException

- If an I/O error occurs

- append

```java
Appendable
append​(
CharSequence
csq,
int start,
int end)
throws
IOException
```

Appends a subsequence of the specified character sequence to this

Appendable

.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.append(csq.subSequence(start, end))
```

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
**Returns:** A reference to this

Appendable
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
**Throws:** IOException

- If an I/O error occurs

- append

```java
Appendable
append​(char c)
throws
IOException
```

Appends the specified character to this

Appendable

.

**Parameters:** c

- The character to append
**Returns:** A reference to this

Appendable
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

append

```java
Appendable
append​(
CharSequence
csq)
throws
IOException
```

Appends the specified character sequence to this

Appendable

.

Depending on which class implements the character sequence

csq

, the entire sequence may not be appended. For
instance, if

csq

is a

CharBuffer

then
the subsequence to append is defined by the buffer's position and limit.

**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this Appendable.
**Returns:** A reference to this

Appendable
**Throws:** IOException

- If an I/O error occurs

---

#### append

Appendable

append​(

CharSequence

csq)
throws

IOException

Appends the specified character sequence to this

Appendable

.

Depending on which class implements the character sequence

csq

, the entire sequence may not be appended. For
instance, if

csq

is a

CharBuffer

then
the subsequence to append is defined by the buffer's position and limit.

Depending on which class implements the character sequence

csq

, the entire sequence may not be appended. For
instance, if

csq

is a

CharBuffer

then
the subsequence to append is defined by the buffer's position and limit.

append

```java
Appendable
append​(
CharSequence
csq,
int start,
int end)
throws
IOException
```

Appends a subsequence of the specified character sequence to this

Appendable

.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.append(csq.subSequence(start, end))
```

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
**Returns:** A reference to this

Appendable
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
**Throws:** IOException

- If an I/O error occurs

---

#### append

Appendable

append​(

CharSequence

csq,
int start,
int end)
throws

IOException

Appends a subsequence of the specified character sequence to this

Appendable

.

An invocation of this method of the form

out.append(csq, start, end)

when

csq

is not

null

, behaves in
exactly the same way as the invocation

```java
out.append(csq.subSequence(start, end))
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
out.append(csq.subSequence(start, end))
```

out.append(csq.subSequence(start, end))

append

```java
Appendable
append​(char c)
throws
IOException
```

Appends the specified character to this

Appendable

.

**Parameters:** c

- The character to append
**Returns:** A reference to this

Appendable
**Throws:** IOException

- If an I/O error occurs

---

#### append

Appendable

append​(char c)
throws

IOException

Appends the specified character to this

Appendable

.

---

