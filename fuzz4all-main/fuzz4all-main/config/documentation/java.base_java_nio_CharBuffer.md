# Class CharBuffer

**Source:** `java.base\java\nio\CharBuffer.html`

### Class Description

```java
public abstract class
CharBuffer

extends
Buffer

implements
Comparable
<
CharBuffer
>,
Appendable
,
CharSequence
,
Readable
```

A char buffer.

This class defines four categories of operations upon
char buffers:

- Absolute and relative

get

and

put

methods that read and write
single chars;
- Relative

bulk get

methods that transfer contiguous sequences of chars from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of chars from a
char array, a string, or some other char
buffer into this buffer; and
- A method for

compacting

a char buffer.

Char buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
char array or string into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a char buffer is either

direct

or

non-direct

. A
char buffer created via the

wrap

methods of this class will
be non-direct. A char buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a char buffer is direct may be determined by invoking the

isDirect

method.

This class implements the

CharSequence

interface so that
character buffers may be used wherever character sequences are accepted, for
example in the regular-expression package

java.util.regex

.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
cb.put("text/");
cb.put(subtype);
cb.put("; charset=");
cb.put(enc);
```

can, for example, be replaced by the single statement

```java
cb.put("text/").put(subtype).put("; charset=").put(enc);
```

**All Implemented Interfaces:** Appendable

,

CharSequence

,

Comparable

<

CharBuffer

>

,

Readable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
CharBuffer
allocate​(int capacity)

Allocates a new char buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

the

native order

of the underlying
hardware.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:**
- capacity

- The new buffer's capacity, in chars

**Returns:**
- The new char buffer

**Throws:**
- IllegalArgumentException

- If the

capacity

is a negative integer

---

#### public static
CharBuffer
wrap​(char[] array,
int offset,
int length)

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity will be

array.length

, its position will be

offset

, its limit
will be

offset + length

, its mark will be undefined, and its
byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and
its

array offset

will be zero.

**Parameters:**
- array

- The array that will back the new buffer
- offset

- The offset of the subarray to be used; must be non-negative and
no larger than

array.length

. The new buffer's position
will be set to this value.
- length

- The length of the subarray to be used;
must be non-negative and no larger than

array.length - offset

.
The new buffer's limit will be set to

offset + length

.

**Returns:**
- The new char buffer

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### public static
CharBuffer
wrap​(char[] array)

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:**
- array

- The array that will back this buffer

**Returns:**
- The new char buffer

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

#### public static
CharBuffer
wrap​(
CharSequence
csq,
int start,
int end)

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The buffer's capacity will be

csq.length()

, its position will be

start

, its limit
will be

end

, and its mark will be undefined.

**Parameters:**
- csq

- The character sequence from which the new character buffer is to
be created
- start

- The index of the first character to be used;
must be non-negative and no larger than

csq.length()

.
The new buffer's position will be set to this value.
- end

- The index of the character following the last character to be
used; must be no smaller than

start

and no larger
than

csq.length()

.
The new buffer's limit will be set to this value.

**Returns:**
- The new character buffer

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold

---

#### public static
CharBuffer
wrap​(
CharSequence
csq)

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The new buffer's capacity and limit will be

csq.length()

, its position will be zero, and its mark will be
undefined.

**Parameters:**
- csq

- The character sequence from which the new character buffer is to
be created

**Returns:**
- The new character buffer

---

#### public abstract
CharBuffer
slice()

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of chars remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:**
- slice

in class

Buffer

**Returns:**
- The new char buffer

---

#### public abstract
CharBuffer
duplicate()

Creates a new char buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:**
- duplicate

in class

Buffer

**Returns:**
- The new char buffer

---

#### public abstract
CharBuffer
asReadOnlyBuffer()

Creates a new, read-only char buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:**
- The new, read-only char buffer

---

#### public abstract char get()

Relative

get

method. Reads the char at this buffer's
current position, and then increments the position.

**Returns:**
- The char at the buffer's current position

**Throws:**
- BufferUnderflowException

- If the buffer's current position is not smaller than its limit

---

#### public abstract
CharBuffer
put​(char c)

Relative

put

method

(optional operation)

.

Writes the given char into this buffer at the current
position, and then increments the position.

**Parameters:**
- c

- The char to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If this buffer's current position is not smaller than its limit
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract char get​(int index)

Absolute

get

method. Reads the char at the given
index.

**Parameters:**
- index

- The index from which the char will be read

**Returns:**
- The char at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

---

#### public abstract
CharBuffer
put​(int index,
char c)

Absolute

put

method

(optional operation)

.

Writes the given char into this buffer at the given
index.

**Parameters:**
- index

- The index at which the char will be written
- c

- The char value to be written

**Returns:**
- This buffer

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public
CharBuffer
get​(char[] dst,
int offset,
int length)

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. If there are fewer chars remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

chars from this
buffer into the given array, starting at the current position of this
buffer and at the given offset in the array. The position of this
buffer is then incremented by

length

.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

**Parameters:**
- dst

- The array into which chars are to be written
- offset

- The offset within the array of the first char to be
written; must be non-negative and no larger than

dst.length
- length

- The maximum number of chars to be written to the given
array; must be non-negative and no larger than

dst.length - offset

**Returns:**
- This buffer

**Throws:**
- BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### public
CharBuffer
get​(char[] dst)

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

**Parameters:**
- dst

- The destination array

**Returns:**
- This buffer

**Throws:**
- BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer

---

#### public
CharBuffer
put​(
CharBuffer
src)

Relative bulk

put

method

(optional operation)

.

This method transfers the chars remaining in the given source
buffer into this buffer. If there are more chars remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

chars from the given
buffer into this buffer, starting at each buffer's current position.
The positions of both buffers are then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

**Parameters:**
- src

- The source buffer from which chars are to be read;
must not be this buffer

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
for the remaining chars in the source buffer
- IllegalArgumentException

- If the source buffer is this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public
CharBuffer
put​(char[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

This method transfers chars into this buffer from the given
source array. If there are more chars to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

chars from the
given array into this buffer, starting at the given offset in the array
and at the current position of this buffer. The position of this buffer
is then incremented by

length

.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:**
- src

- The array from which chars are to be read
- offset

- The offset within the array of the first char to be read;
must be non-negative and no larger than

array.length
- length

- The number of chars to be read from the given array;
must be non-negative and no larger than

array.length - offset

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public final
CharBuffer
put​(char[] src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
char array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

**Parameters:**
- src

- The source array

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public
CharBuffer
put​(
String
src,
int start,
int end)

Relative bulk

put

method

(optional operation)

.

This method transfers chars from the given string into this
buffer. If there are more chars to be copied from the string than
remain in this buffer, that is, if

end - start

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

end

-

start

chars
from the given string into this buffer, starting at the given

start

index and at the current position of this buffer. The
position of this buffer is then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:**
- src

- The string from which chars are to be read
- start

- The offset within the string of the first char to be read;
must be non-negative and no larger than

string.length()
- end

- The offset within the string of the last char to be read,
plus one; must be non-negative and no larger than

string.length()

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
- IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public final
CharBuffer
put​(
String
src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source string
into this buffer. An invocation of this method of the form

dst.put(s)

behaves in exactly the same way as the invocation

```java
dst.put(s, 0, s.length())
```

**Parameters:**
- src

- The source string

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public final boolean hasArray()

Tells whether or not this buffer is backed by an accessible char
array.

If this method returns

true

then the

array

and

arrayOffset

methods may safely be invoked.

**Specified by:**
- hasArray

in class

Buffer

**Returns:**
- true

if, and only if, this buffer
is backed by an array and is not read-only

---

#### public final char[] array()

Returns the char array that backs this
buffer

(optional operation)

.

Modifications to this buffer's content will cause the returned
array's content to be modified, and vice versa.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:**
- array

in class

Buffer

**Returns:**
- The array that backs this buffer

**Throws:**
- ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
- UnsupportedOperationException

- If this buffer is not backed by an accessible array

---

#### public final int arrayOffset()

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

If this buffer is backed by an array then buffer position

p

corresponds to array index

p

+

arrayOffset()

.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:**
- arrayOffset

in class

Buffer

**Returns:**
- The offset within this buffer's array
of the first element of the buffer

**Throws:**
- ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
- UnsupportedOperationException

- If this buffer is not backed by an accessible array

---

#### public abstract
CharBuffer
compact()

Compacts this buffer

(optional operation)

.

The chars between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
char at index

p

=

position()

is copied
to index zero, the char at index

p

+ 1 is copied
to index one, and so forth until the char at index

limit()

- 1 is copied to index

n

=

limit()

-

1

-

p

.
The buffer's position is then set to

n+1

and its limit is set to
its capacity. The mark, if defined, is discarded.

The buffer's position is set to the number of chars copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

**Returns:**
- This buffer

**Throws:**
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract boolean isDirect()

Tells whether or not this char buffer is direct.

**Specified by:**
- isDirect

in class

Buffer

**Returns:**
- true

if, and only if, this buffer is direct

---

#### public int hashCode()

Returns the current hash code of this buffer.

The hash code of a char buffer depends only upon its remaining
elements; that is, upon the elements from

position()

up to, and
including, the element at

limit()

-

1

.

Because buffer hash codes are content-dependent, it is inadvisable
to use buffers as keys in hash maps or similar data structures unless it
is known that their contents will not change.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The current hash code of this buffer

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
ob)

Tells whether or not this buffer is equal to another object.

Two char buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A char buffer is not equal to any other type of object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- ob

- The object to which this buffer is to be compared

**Returns:**
- true

if, and only if, this buffer is equal to the
given object

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int compareTo​(
CharBuffer
that)

Compares this buffer to another.

Two char buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

char

elements are compared as if by invoking

Character.compare(char,char)

.

A char buffer is not comparable to any other type of object.

**Specified by:**
- compareTo

in interface

Comparable

<

CharBuffer

>

**Parameters:**
- that

- the object to be compared.

**Returns:**
- A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

---

#### public int mismatch​(
CharBuffer
that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer. The index is relative to the

position

of each buffer and will be in the range of
0 (inclusive) up to the smaller of the

remaining

elements in each buffer (exclusive).

If the two buffers share a common prefix then the returned index is
the length of the common prefix and it follows that there is a mismatch
between the two buffers at that index within the respective buffers.
If one buffer is a proper prefix of the other then the returned index is
the smaller of the remaining elements in each buffer, and it follows that
the index is only valid for the buffer with the larger number of
remaining elements.
Otherwise, there is no mismatch.

**Parameters:**
- that

- The byte buffer to be tested for a mismatch with this buffer

**Returns:**
- The relative index of the first mismatch between this and the
given buffer, otherwise -1 if no mismatch.

**Since:**
- 11

---

#### public
String
toString()

Returns a string containing the characters in this buffer.

The first character of the resulting string will be the character at
this buffer's position, while the last character will be the character
at index

limit()

- 1. Invoking this method does not
change the buffer's position.

**Specified by:**
- toString

in interface

CharSequence

**Overrides:**
- toString

in class

Object

**Returns:**
- The specified string

---

#### public final int length()

Returns the length of this character buffer.

When viewed as a character sequence, the length of a character
buffer is simply the number of characters between the position
(inclusive) and the limit (exclusive); that is, it is equivalent to

remaining()

.

**Specified by:**
- length

in interface

CharSequence

**Returns:**
- The length of this character buffer

---

#### public final char charAt​(int index)

Reads the character at the given index relative to the current
position.

**Specified by:**
- charAt

in interface

CharSequence

**Parameters:**
- index

- The index of the character to be read, relative to the position;
must be non-negative and smaller than

remaining()

**Returns:**
- The character at index

position() + index

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on

index

do not hold

---

#### public abstract
CharBuffer
subSequence​(int start,
int end)

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

The new buffer will share this buffer's content; that is, if the
content of this buffer is mutable then modifications to one buffer will
cause the other to be modified. The new buffer's capacity will be that
of this buffer, its position will be

position()

+

start

, and its limit will be

position()

+

end

. The new buffer will be
direct if, and only if, this buffer is direct, and it will be read-only
if, and only if, this buffer is read-only.

**Specified by:**
- subSequence

in interface

CharSequence

**Parameters:**
- start

- The index, relative to the current position, of the first
character in the subsequence; must be non-negative and no larger
than

remaining()
- end

- The index, relative to the current position, of the character
following the last character in the subsequence; must be no
smaller than

start

and no larger than

remaining()

**Returns:**
- The new character buffer

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on

start

and

end

do not hold

---

#### public
CharBuffer
append​(
CharSequence
csq)

Appends the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq)

behaves in exactly the same way as the invocation

```java
dst.put(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a character buffer will return a subsequence whose
content depends upon the buffer's position and limit.

**Specified by:**
- append

in interface

Appendable

**Parameters:**
- csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this character buffer.

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

**Since:**
- 1.5

---

#### public
CharBuffer
append​(
CharSequence
csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq, start,
end)

when

csq

is not

null

, behaves in exactly the
same way as the invocation

```java
dst.put(csq.subSequence(start, end).toString())
```

**Specified by:**
- append

in interface

Appendable

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
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
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
- ReadOnlyBufferException

- If this buffer is read-only

**Since:**
- 1.5

---

#### public
CharBuffer
append​(char c)

Appends the specified char to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(c)

behaves in exactly the same way as the invocation

```java
dst.put(c)
```

**Specified by:**
- append

in interface

Appendable

**Parameters:**
- c

- The 16-bit char to append

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

**Since:**
- 1.5

---

#### public abstract
ByteOrder
order()

Retrieves this buffer's byte order.

The byte order of a char buffer created by allocation or by
wrapping an existing

char

array is the

native order

of the underlying
hardware. The byte order of a char buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

**Returns:**
- This buffer's byte order

---

### Additional Sections

#### Class CharBuffer

java.lang.Object

- java.nio.Buffer
- - java.nio.CharBuffer

java.nio.Buffer

- java.nio.CharBuffer

java.nio.CharBuffer

**All Implemented Interfaces:** Appendable

,

CharSequence

,

Comparable

<

CharBuffer

>

,

Readable

```java
public abstract class
CharBuffer

extends
Buffer

implements
Comparable
<
CharBuffer
>,
Appendable
,
CharSequence
,
Readable
```

A char buffer.

This class defines four categories of operations upon
char buffers:

- Absolute and relative

get

and

put

methods that read and write
single chars;
- Relative

bulk get

methods that transfer contiguous sequences of chars from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of chars from a
char array, a string, or some other char
buffer into this buffer; and
- A method for

compacting

a char buffer.

Char buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
char array or string into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a char buffer is either

direct

or

non-direct

. A
char buffer created via the

wrap

methods of this class will
be non-direct. A char buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a char buffer is direct may be determined by invoking the

isDirect

method.

This class implements the

CharSequence

interface so that
character buffers may be used wherever character sequences are accepted, for
example in the regular-expression package

java.util.regex

.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
cb.put("text/");
cb.put(subtype);
cb.put("; charset=");
cb.put(enc);
```

can, for example, be replaced by the single statement

```java
cb.put("text/").put(subtype).put("; charset=").put(enc);
```

**Since:** 1.4

public abstract class

CharBuffer

extends

Buffer

implements

Comparable

<

CharBuffer

>,

Appendable

,

CharSequence

,

Readable

A char buffer.

This class defines four categories of operations upon
char buffers:

- Absolute and relative

get

and

put

methods that read and write
single chars;
- Relative

bulk get

methods that transfer contiguous sequences of chars from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of chars from a
char array, a string, or some other char
buffer into this buffer; and
- A method for

compacting

a char buffer.

Char buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
char array or string into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a char buffer is either

direct

or

non-direct

. A
char buffer created via the

wrap

methods of this class will
be non-direct. A char buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a char buffer is direct may be determined by invoking the

isDirect

method.

This class implements the

CharSequence

interface so that
character buffers may be used wherever character sequences are accepted, for
example in the regular-expression package

java.util.regex

.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
cb.put("text/");
cb.put(subtype);
cb.put("; charset=");
cb.put(enc);
```

can, for example, be replaced by the single statement

```java
cb.put("text/").put(subtype).put("; charset=").put(enc);
```

This class defines four categories of operations upon
char buffers:

- Absolute and relative

get

and

put

methods that read and write
single chars;
- Relative

bulk get

methods that transfer contiguous sequences of chars from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of chars from a
char array, a string, or some other char
buffer into this buffer; and
- A method for

compacting

a char buffer.

Char buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
char array or string into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a char buffer is either

direct

or

non-direct

. A
char buffer created via the

wrap

methods of this class will
be non-direct. A char buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a char buffer is direct may be determined by invoking the

isDirect

method.

This class implements the

CharSequence

interface so that
character buffers may be used wherever character sequences are accepted, for
example in the regular-expression package

java.util.regex

.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
cb.put("text/");
cb.put(subtype);
cb.put("; charset=");
cb.put(enc);
```

can, for example, be replaced by the single statement

```java
cb.put("text/").put(subtype).put("; charset=").put(enc);
```

Absolute and relative

get

and

put

methods that read and write
single chars;

Relative

bulk get

methods that transfer contiguous sequences of chars from this buffer
into an array; and

Relative

bulk put

methods that transfer contiguous sequences of chars from a
char array, a string, or some other char
buffer into this buffer; and

A method for

compacting

a char buffer.

Absolute and relative

get

and

put

methods that read and write
single chars;

Relative

bulk get

methods that transfer contiguous sequences of chars from this buffer
into an array; and

Relative

bulk put

methods that transfer contiguous sequences of chars from a
char array, a string, or some other char
buffer into this buffer; and

A method for

compacting

a char buffer.

Char buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
char array or string into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a char buffer is either

direct

or

non-direct

. A
char buffer created via the

wrap

methods of this class will
be non-direct. A char buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a char buffer is direct may be determined by invoking the

isDirect

method.

This class implements the

CharSequence

interface so that
character buffers may be used wherever character sequences are accepted, for
example in the regular-expression package

java.util.regex

.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
cb.put("text/");
cb.put(subtype);
cb.put("; charset=");
cb.put(enc);
```

can, for example, be replaced by the single statement

```java
cb.put("text/").put(subtype).put("; charset=").put(enc);
```

Like a byte buffer, a char buffer is either

direct

or

non-direct

. A
char buffer created via the

wrap

methods of this class will
be non-direct. A char buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a char buffer is direct may be determined by invoking the

isDirect

method.

This class implements the

CharSequence

interface so that
character buffers may be used wherever character sequences are accepted, for
example in the regular-expression package

java.util.regex

.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
cb.put("text/");
cb.put(subtype);
cb.put("; charset=");
cb.put(enc);
```

can, for example, be replaced by the single statement

```java
cb.put("text/").put(subtype).put("; charset=").put(enc);
```

cb.put("text/");
cb.put(subtype);
cb.put("; charset=");
cb.put(enc);

cb.put("text/").put(subtype).put("; charset=").put(enc);

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

static

CharBuffer

allocate

​(int capacity)

Allocates a new char buffer.

CharBuffer

append

​(char c)

Appends the specified char to this
buffer

(optional operation)

.

CharBuffer

append

​(

CharSequence

csq)

Appends the specified character sequence to this
buffer

(optional operation)

.

CharBuffer

append

​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

char[]

array

()

Returns the char array that backs this
buffer

(optional operation)

.

int

arrayOffset

()

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

abstract

CharBuffer

asReadOnlyBuffer

()

Creates a new, read-only char buffer that shares this buffer's
content.

char

charAt

​(int index)

Reads the character at the given index relative to the current
position.

abstract

CharBuffer

compact

()

Compacts this buffer

(optional operation)

.

int

compareTo

​(

CharBuffer

that)

Compares this buffer to another.

abstract

CharBuffer

duplicate

()

Creates a new char buffer that shares this buffer's content.

boolean

equals

​(

Object

ob)

Tells whether or not this buffer is equal to another object.

abstract char

get

()

Relative

get

method.

CharBuffer

get

​(char[] dst)

Relative bulk

get

method.

CharBuffer

get

​(char[] dst,
int offset,
int length)

Relative bulk

get

method.

abstract char

get

​(int index)

Absolute

get

method.

boolean

hasArray

()

Tells whether or not this buffer is backed by an accessible char
array.

int

hashCode

()

Returns the current hash code of this buffer.

abstract boolean

isDirect

()

Tells whether or not this char buffer is direct.

int

length

()

Returns the length of this character buffer.

int

mismatch

​(

CharBuffer

that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

abstract

ByteOrder

order

()

Retrieves this buffer's byte order.

abstract

CharBuffer

put

​(char c)

Relative

put

method

(optional operation)

.

CharBuffer

put

​(char[] src)

Relative bulk

put

method

(optional operation)

.

CharBuffer

put

​(char[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

abstract

CharBuffer

put

​(int index,
char c)

Absolute

put

method

(optional operation)

.

CharBuffer

put

​(

String

src)

Relative bulk

put

method

(optional operation)

.

CharBuffer

put

​(

String

src,
int start,
int end)

Relative bulk

put

method

(optional operation)

.

CharBuffer

put

​(

CharBuffer

src)

Relative bulk

put

method

(optional operation)

.

int

read

​(

CharBuffer

target)

Attempts to read characters into the specified character buffer.

abstract

CharBuffer

slice

()

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

abstract

CharBuffer

subSequence

​(int start,
int end)

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

String

toString

()

Returns a string containing the characters in this buffer.

static

CharBuffer

wrap

​(char[] array)

Wraps a char array into a buffer.

static

CharBuffer

wrap

​(char[] array,
int offset,
int length)

Wraps a char array into a buffer.

static

CharBuffer

wrap

​(

CharSequence

csq)

Wraps a character sequence into a buffer.

static

CharBuffer

wrap

​(

CharSequence

csq,
int start,
int end)

Wraps a character sequence into a buffer.

- Methods declared in class java.nio.

Buffer

capacity

,

clear

,

flip

,

hasRemaining

,

isReadOnly

,

limit

,

limit

,

mark

,

position

,

position

,

remaining

,

reset

,

rewind

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface java.lang.

CharSequence

chars

,

codePoints

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

CharBuffer

allocate

​(int capacity)

Allocates a new char buffer.

CharBuffer

append

​(char c)

Appends the specified char to this
buffer

(optional operation)

.

CharBuffer

append

​(

CharSequence

csq)

Appends the specified character sequence to this
buffer

(optional operation)

.

CharBuffer

append

​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

char[]

array

()

Returns the char array that backs this
buffer

(optional operation)

.

int

arrayOffset

()

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

abstract

CharBuffer

asReadOnlyBuffer

()

Creates a new, read-only char buffer that shares this buffer's
content.

char

charAt

​(int index)

Reads the character at the given index relative to the current
position.

abstract

CharBuffer

compact

()

Compacts this buffer

(optional operation)

.

int

compareTo

​(

CharBuffer

that)

Compares this buffer to another.

abstract

CharBuffer

duplicate

()

Creates a new char buffer that shares this buffer's content.

boolean

equals

​(

Object

ob)

Tells whether or not this buffer is equal to another object.

abstract char

get

()

Relative

get

method.

CharBuffer

get

​(char[] dst)

Relative bulk

get

method.

CharBuffer

get

​(char[] dst,
int offset,
int length)

Relative bulk

get

method.

abstract char

get

​(int index)

Absolute

get

method.

boolean

hasArray

()

Tells whether or not this buffer is backed by an accessible char
array.

int

hashCode

()

Returns the current hash code of this buffer.

abstract boolean

isDirect

()

Tells whether or not this char buffer is direct.

int

length

()

Returns the length of this character buffer.

int

mismatch

​(

CharBuffer

that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

abstract

ByteOrder

order

()

Retrieves this buffer's byte order.

abstract

CharBuffer

put

​(char c)

Relative

put

method

(optional operation)

.

CharBuffer

put

​(char[] src)

Relative bulk

put

method

(optional operation)

.

CharBuffer

put

​(char[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

abstract

CharBuffer

put

​(int index,
char c)

Absolute

put

method

(optional operation)

.

CharBuffer

put

​(

String

src)

Relative bulk

put

method

(optional operation)

.

CharBuffer

put

​(

String

src,
int start,
int end)

Relative bulk

put

method

(optional operation)

.

CharBuffer

put

​(

CharBuffer

src)

Relative bulk

put

method

(optional operation)

.

int

read

​(

CharBuffer

target)

Attempts to read characters into the specified character buffer.

abstract

CharBuffer

slice

()

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

abstract

CharBuffer

subSequence

​(int start,
int end)

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

String

toString

()

Returns a string containing the characters in this buffer.

static

CharBuffer

wrap

​(char[] array)

Wraps a char array into a buffer.

static

CharBuffer

wrap

​(char[] array,
int offset,
int length)

Wraps a char array into a buffer.

static

CharBuffer

wrap

​(

CharSequence

csq)

Wraps a character sequence into a buffer.

static

CharBuffer

wrap

​(

CharSequence

csq,
int start,
int end)

Wraps a character sequence into a buffer.

- Methods declared in class java.nio.

Buffer

capacity

,

clear

,

flip

,

hasRemaining

,

isReadOnly

,

limit

,

limit

,

mark

,

position

,

position

,

remaining

,

reset

,

rewind

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface java.lang.

CharSequence

chars

,

codePoints

---

#### Method Summary

Allocates a new char buffer.

Appends the specified char to this
buffer

(optional operation)

.

Appends the specified character sequence to this
buffer

(optional operation)

.

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

Returns the char array that backs this
buffer

(optional operation)

.

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

Creates a new, read-only char buffer that shares this buffer's
content.

Reads the character at the given index relative to the current
position.

Compacts this buffer

(optional operation)

.

Compares this buffer to another.

Creates a new char buffer that shares this buffer's content.

Tells whether or not this buffer is equal to another object.

Relative

get

method.

Relative bulk

get

method.

Absolute

get

method.

Tells whether or not this buffer is backed by an accessible char
array.

Returns the current hash code of this buffer.

Tells whether or not this char buffer is direct.

Returns the length of this character buffer.

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

Retrieves this buffer's byte order.

Relative

put

method

(optional operation)

.

Relative bulk

put

method

(optional operation)

.

Absolute

put

method

(optional operation)

.

Attempts to read characters into the specified character buffer.

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

Returns a string containing the characters in this buffer.

Wraps a char array into a buffer.

Wraps a character sequence into a buffer.

Methods declared in class java.nio.

Buffer

capacity

,

clear

,

flip

,

hasRemaining

,

isReadOnly

,

limit

,

limit

,

mark

,

position

,

position

,

remaining

,

reset

,

rewind

---

#### Methods declared in class java.nio. Buffer

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Methods declared in interface java.lang.

CharSequence

chars

,

codePoints

---

#### Methods declared in interface java.lang. CharSequence

============ METHOD DETAIL ==========

- Method Detail

- allocate

```java
public static
CharBuffer
allocate​(int capacity)
```

Allocates a new char buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

the

native order

of the underlying
hardware.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:** capacity

- The new buffer's capacity, in chars
**Returns:** The new char buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- wrap

```java
public static
CharBuffer
wrap​(char[] array,
int offset,
int length)
```

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity will be

array.length

, its position will be

offset

, its limit
will be

offset + length

, its mark will be undefined, and its
byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and
its

array offset

will be zero.

**Parameters:** array

- The array that will back the new buffer
**Parameters:** offset

- The offset of the subarray to be used; must be non-negative and
no larger than

array.length

. The new buffer's position
will be set to this value.
**Parameters:** length

- The length of the subarray to be used;
must be non-negative and no larger than

array.length - offset

.
The new buffer's limit will be set to

offset + length

.
**Returns:** The new char buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- wrap

```java
public static
CharBuffer
wrap​(char[] array)
```

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:** array

- The array that will back this buffer
**Returns:** The new char buffer

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

- wrap

```java
public static
CharBuffer
wrap​(
CharSequence
csq,
int start,
int end)
```

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The buffer's capacity will be

csq.length()

, its position will be

start

, its limit
will be

end

, and its mark will be undefined.

**Parameters:** csq

- The character sequence from which the new character buffer is to
be created
**Parameters:** start

- The index of the first character to be used;
must be non-negative and no larger than

csq.length()

.
The new buffer's position will be set to this value.
**Parameters:** end

- The index of the character following the last character to be
used; must be no smaller than

start

and no larger
than

csq.length()

.
The new buffer's limit will be set to this value.
**Returns:** The new character buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold

- wrap

```java
public static
CharBuffer
wrap​(
CharSequence
csq)
```

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The new buffer's capacity and limit will be

csq.length()

, its position will be zero, and its mark will be
undefined.

**Parameters:** csq

- The character sequence from which the new character buffer is to
be created
**Returns:** The new character buffer

- slice

```java
public abstract
CharBuffer
slice()
```

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of chars remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new char buffer

- duplicate

```java
public abstract
CharBuffer
duplicate()
```

Creates a new char buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** duplicate

in class

Buffer
**Returns:** The new char buffer

- asReadOnlyBuffer

```java
public abstract
CharBuffer
asReadOnlyBuffer()
```

Creates a new, read-only char buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:** The new, read-only char buffer

- get

```java
public abstract char get()
```

Relative

get

method. Reads the char at this buffer's
current position, and then increments the position.

**Returns:** The char at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

- put

```java
public abstract
CharBuffer
put​(char c)
```

Relative

put

method

(optional operation)

.

Writes the given char into this buffer at the current
position, and then increments the position.

**Parameters:** c

- The char to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public abstract char get​(int index)
```

Absolute

get

method. Reads the char at the given
index.

**Parameters:** index

- The index from which the char will be read
**Returns:** The char at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

- put

```java
public abstract
CharBuffer
put​(int index,
char c)
```

Absolute

put

method

(optional operation)

.

Writes the given char into this buffer at the given
index.

**Parameters:** index

- The index at which the char will be written
**Parameters:** c

- The char value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public
CharBuffer
get​(char[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. If there are fewer chars remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

chars from this
buffer into the given array, starting at the current position of this
buffer and at the given offset in the array. The position of this
buffer is then incremented by

length

.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which chars are to be written
**Parameters:** offset

- The offset within the array of the first char to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of chars to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- get

```java
public
CharBuffer
get​(char[] dst)
```

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

**Parameters:** dst

- The destination array
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer

- put

```java
public
CharBuffer
put​(
CharBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the chars remaining in the given source
buffer into this buffer. If there are more chars remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

chars from the given
buffer into this buffer, starting at each buffer's current position.
The positions of both buffers are then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

**Parameters:** src

- The source buffer from which chars are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining chars in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
CharBuffer
put​(char[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers chars into this buffer from the given
source array. If there are more chars to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

chars from the
given array into this buffer, starting at the given offset in the array
and at the current position of this buffer. The position of this buffer
is then incremented by

length

.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:** src

- The array from which chars are to be read
**Parameters:** offset

- The offset within the array of the first char to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of chars to be read from the given array;
must be non-negative and no larger than

array.length - offset
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public final
CharBuffer
put​(char[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
char array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

**Parameters:** src

- The source array
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
CharBuffer
put​(
String
src,
int start,
int end)
```

Relative bulk

put

method

(optional operation)

.

This method transfers chars from the given string into this
buffer. If there are more chars to be copied from the string than
remain in this buffer, that is, if

end - start

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

end

-

start

chars
from the given string into this buffer, starting at the given

start

index and at the current position of this buffer. The
position of this buffer is then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:** src

- The string from which chars are to be read
**Parameters:** start

- The offset within the string of the first char to be read;
must be non-negative and no larger than

string.length()
**Parameters:** end

- The offset within the string of the last char to be read,
plus one; must be non-negative and no larger than

string.length()
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public final
CharBuffer
put​(
String
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source string
into this buffer. An invocation of this method of the form

dst.put(s)

behaves in exactly the same way as the invocation

```java
dst.put(s, 0, s.length())
```

**Parameters:** src

- The source string
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- hasArray

```java
public final boolean hasArray()
```

Tells whether or not this buffer is backed by an accessible char
array.

If this method returns

true

then the

array

and

arrayOffset

methods may safely be invoked.

**Specified by:** hasArray

in class

Buffer
**Returns:** true

if, and only if, this buffer
is backed by an array and is not read-only

- array

```java
public final char[] array()
```

Returns the char array that backs this
buffer

(optional operation)

.

Modifications to this buffer's content will cause the returned
array's content to be modified, and vice versa.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:** array

in class

Buffer
**Returns:** The array that backs this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
**Throws:** UnsupportedOperationException

- If this buffer is not backed by an accessible array

- arrayOffset

```java
public final int arrayOffset()
```

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

If this buffer is backed by an array then buffer position

p

corresponds to array index

p

+

arrayOffset()

.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:** arrayOffset

in class

Buffer
**Returns:** The offset within this buffer's array
of the first element of the buffer
**Throws:** ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
**Throws:** UnsupportedOperationException

- If this buffer is not backed by an accessible array

- compact

```java
public abstract
CharBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The chars between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
char at index

p

=

position()

is copied
to index zero, the char at index

p

+ 1 is copied
to index one, and so forth until the char at index

limit()

- 1 is copied to index

n

=

limit()

-

1

-

p

.
The buffer's position is then set to

n+1

and its limit is set to
its capacity. The mark, if defined, is discarded.

The buffer's position is set to the number of chars copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

**Returns:** This buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- isDirect

```java
public abstract boolean isDirect()
```

Tells whether or not this char buffer is direct.

**Specified by:** isDirect

in class

Buffer
**Returns:** true

if, and only if, this buffer is direct

- hashCode

```java
public int hashCode()
```

Returns the current hash code of this buffer.

The hash code of a char buffer depends only upon its remaining
elements; that is, upon the elements from

position()

up to, and
including, the element at

limit()

-

1

.

Because buffer hash codes are content-dependent, it is inadvisable
to use buffers as keys in hash maps or similar data structures unless it
is known that their contents will not change.

**Overrides:** hashCode

in class

Object
**Returns:** The current hash code of this buffer
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tells whether or not this buffer is equal to another object.

Two char buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A char buffer is not equal to any other type of object.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this buffer is to be compared
**Returns:** true

if, and only if, this buffer is equal to the
given object
**See Also:** Object.hashCode()

,

HashMap

- compareTo

```java
public int compareTo​(
CharBuffer
that)
```

Compares this buffer to another.

Two char buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

char

elements are compared as if by invoking

Character.compare(char,char)

.

A char buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

CharBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

- mismatch

```java
public int mismatch​(
CharBuffer
that)
```

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer. The index is relative to the

position

of each buffer and will be in the range of
0 (inclusive) up to the smaller of the

remaining

elements in each buffer (exclusive).

If the two buffers share a common prefix then the returned index is
the length of the common prefix and it follows that there is a mismatch
between the two buffers at that index within the respective buffers.
If one buffer is a proper prefix of the other then the returned index is
the smaller of the remaining elements in each buffer, and it follows that
the index is only valid for the buffer with the larger number of
remaining elements.
Otherwise, there is no mismatch.

**Parameters:** that

- The byte buffer to be tested for a mismatch with this buffer
**Returns:** The relative index of the first mismatch between this and the
given buffer, otherwise -1 if no mismatch.
**Since:** 11

- toString

```java
public
String
toString()
```

Returns a string containing the characters in this buffer.

The first character of the resulting string will be the character at
this buffer's position, while the last character will be the character
at index

limit()

- 1. Invoking this method does not
change the buffer's position.

**Specified by:** toString

in interface

CharSequence
**Overrides:** toString

in class

Object
**Returns:** The specified string

- length

```java
public final int length()
```

Returns the length of this character buffer.

When viewed as a character sequence, the length of a character
buffer is simply the number of characters between the position
(inclusive) and the limit (exclusive); that is, it is equivalent to

remaining()

.

**Specified by:** length

in interface

CharSequence
**Returns:** The length of this character buffer

- charAt

```java
public final char charAt​(int index)
```

Reads the character at the given index relative to the current
position.

**Specified by:** charAt

in interface

CharSequence
**Parameters:** index

- The index of the character to be read, relative to the position;
must be non-negative and smaller than

remaining()
**Returns:** The character at index

position() + index
**Throws:** IndexOutOfBoundsException

- If the preconditions on

index

do not hold

- subSequence

```java
public abstract
CharBuffer
subSequence​(int start,
int end)
```

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

The new buffer will share this buffer's content; that is, if the
content of this buffer is mutable then modifications to one buffer will
cause the other to be modified. The new buffer's capacity will be that
of this buffer, its position will be

position()

+

start

, and its limit will be

position()

+

end

. The new buffer will be
direct if, and only if, this buffer is direct, and it will be read-only
if, and only if, this buffer is read-only.

**Specified by:** subSequence

in interface

CharSequence
**Parameters:** start

- The index, relative to the current position, of the first
character in the subsequence; must be non-negative and no larger
than

remaining()
**Parameters:** end

- The index, relative to the current position, of the character
following the last character in the subsequence; must be no
smaller than

start

and no larger than

remaining()
**Returns:** The new character buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on

start

and

end

do not hold

- append

```java
public
CharBuffer
append​(
CharSequence
csq)
```

Appends the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq)

behaves in exactly the same way as the invocation

```java
dst.put(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a character buffer will return a subsequence whose
content depends upon the buffer's position and limit.

**Specified by:** append

in interface

Appendable
**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this character buffer.
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

- append

```java
public
CharBuffer
append​(
CharSequence
csq,
int start,
int end)
```

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq, start,
end)

when

csq

is not

null

, behaves in exactly the
same way as the invocation

```java
dst.put(csq.subSequence(start, end).toString())
```

**Specified by:** append

in interface

Appendable
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
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
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
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

- append

```java
public
CharBuffer
append​(char c)
```

Appends the specified char to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(c)

behaves in exactly the same way as the invocation

```java
dst.put(c)
```

**Specified by:** append

in interface

Appendable
**Parameters:** c

- The 16-bit char to append
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

- order

```java
public abstract
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order of a char buffer created by allocation or by
wrapping an existing

char

array is the

native order

of the underlying
hardware. The byte order of a char buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

**Returns:** This buffer's byte order

Method Detail

- allocate

```java
public static
CharBuffer
allocate​(int capacity)
```

Allocates a new char buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

the

native order

of the underlying
hardware.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:** capacity

- The new buffer's capacity, in chars
**Returns:** The new char buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- wrap

```java
public static
CharBuffer
wrap​(char[] array,
int offset,
int length)
```

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity will be

array.length

, its position will be

offset

, its limit
will be

offset + length

, its mark will be undefined, and its
byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and
its

array offset

will be zero.

**Parameters:** array

- The array that will back the new buffer
**Parameters:** offset

- The offset of the subarray to be used; must be non-negative and
no larger than

array.length

. The new buffer's position
will be set to this value.
**Parameters:** length

- The length of the subarray to be used;
must be non-negative and no larger than

array.length - offset

.
The new buffer's limit will be set to

offset + length

.
**Returns:** The new char buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- wrap

```java
public static
CharBuffer
wrap​(char[] array)
```

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:** array

- The array that will back this buffer
**Returns:** The new char buffer

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

- wrap

```java
public static
CharBuffer
wrap​(
CharSequence
csq,
int start,
int end)
```

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The buffer's capacity will be

csq.length()

, its position will be

start

, its limit
will be

end

, and its mark will be undefined.

**Parameters:** csq

- The character sequence from which the new character buffer is to
be created
**Parameters:** start

- The index of the first character to be used;
must be non-negative and no larger than

csq.length()

.
The new buffer's position will be set to this value.
**Parameters:** end

- The index of the character following the last character to be
used; must be no smaller than

start

and no larger
than

csq.length()

.
The new buffer's limit will be set to this value.
**Returns:** The new character buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold

- wrap

```java
public static
CharBuffer
wrap​(
CharSequence
csq)
```

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The new buffer's capacity and limit will be

csq.length()

, its position will be zero, and its mark will be
undefined.

**Parameters:** csq

- The character sequence from which the new character buffer is to
be created
**Returns:** The new character buffer

- slice

```java
public abstract
CharBuffer
slice()
```

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of chars remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new char buffer

- duplicate

```java
public abstract
CharBuffer
duplicate()
```

Creates a new char buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** duplicate

in class

Buffer
**Returns:** The new char buffer

- asReadOnlyBuffer

```java
public abstract
CharBuffer
asReadOnlyBuffer()
```

Creates a new, read-only char buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:** The new, read-only char buffer

- get

```java
public abstract char get()
```

Relative

get

method. Reads the char at this buffer's
current position, and then increments the position.

**Returns:** The char at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

- put

```java
public abstract
CharBuffer
put​(char c)
```

Relative

put

method

(optional operation)

.

Writes the given char into this buffer at the current
position, and then increments the position.

**Parameters:** c

- The char to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public abstract char get​(int index)
```

Absolute

get

method. Reads the char at the given
index.

**Parameters:** index

- The index from which the char will be read
**Returns:** The char at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

- put

```java
public abstract
CharBuffer
put​(int index,
char c)
```

Absolute

put

method

(optional operation)

.

Writes the given char into this buffer at the given
index.

**Parameters:** index

- The index at which the char will be written
**Parameters:** c

- The char value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public
CharBuffer
get​(char[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. If there are fewer chars remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

chars from this
buffer into the given array, starting at the current position of this
buffer and at the given offset in the array. The position of this
buffer is then incremented by

length

.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which chars are to be written
**Parameters:** offset

- The offset within the array of the first char to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of chars to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- get

```java
public
CharBuffer
get​(char[] dst)
```

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

**Parameters:** dst

- The destination array
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer

- put

```java
public
CharBuffer
put​(
CharBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the chars remaining in the given source
buffer into this buffer. If there are more chars remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

chars from the given
buffer into this buffer, starting at each buffer's current position.
The positions of both buffers are then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

**Parameters:** src

- The source buffer from which chars are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining chars in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
CharBuffer
put​(char[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers chars into this buffer from the given
source array. If there are more chars to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

chars from the
given array into this buffer, starting at the given offset in the array
and at the current position of this buffer. The position of this buffer
is then incremented by

length

.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:** src

- The array from which chars are to be read
**Parameters:** offset

- The offset within the array of the first char to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of chars to be read from the given array;
must be non-negative and no larger than

array.length - offset
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public final
CharBuffer
put​(char[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
char array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

**Parameters:** src

- The source array
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
CharBuffer
put​(
String
src,
int start,
int end)
```

Relative bulk

put

method

(optional operation)

.

This method transfers chars from the given string into this
buffer. If there are more chars to be copied from the string than
remain in this buffer, that is, if

end - start

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

end

-

start

chars
from the given string into this buffer, starting at the given

start

index and at the current position of this buffer. The
position of this buffer is then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:** src

- The string from which chars are to be read
**Parameters:** start

- The offset within the string of the first char to be read;
must be non-negative and no larger than

string.length()
**Parameters:** end

- The offset within the string of the last char to be read,
plus one; must be non-negative and no larger than

string.length()
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public final
CharBuffer
put​(
String
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source string
into this buffer. An invocation of this method of the form

dst.put(s)

behaves in exactly the same way as the invocation

```java
dst.put(s, 0, s.length())
```

**Parameters:** src

- The source string
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- hasArray

```java
public final boolean hasArray()
```

Tells whether or not this buffer is backed by an accessible char
array.

If this method returns

true

then the

array

and

arrayOffset

methods may safely be invoked.

**Specified by:** hasArray

in class

Buffer
**Returns:** true

if, and only if, this buffer
is backed by an array and is not read-only

- array

```java
public final char[] array()
```

Returns the char array that backs this
buffer

(optional operation)

.

Modifications to this buffer's content will cause the returned
array's content to be modified, and vice versa.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:** array

in class

Buffer
**Returns:** The array that backs this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
**Throws:** UnsupportedOperationException

- If this buffer is not backed by an accessible array

- arrayOffset

```java
public final int arrayOffset()
```

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

If this buffer is backed by an array then buffer position

p

corresponds to array index

p

+

arrayOffset()

.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:** arrayOffset

in class

Buffer
**Returns:** The offset within this buffer's array
of the first element of the buffer
**Throws:** ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
**Throws:** UnsupportedOperationException

- If this buffer is not backed by an accessible array

- compact

```java
public abstract
CharBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The chars between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
char at index

p

=

position()

is copied
to index zero, the char at index

p

+ 1 is copied
to index one, and so forth until the char at index

limit()

- 1 is copied to index

n

=

limit()

-

1

-

p

.
The buffer's position is then set to

n+1

and its limit is set to
its capacity. The mark, if defined, is discarded.

The buffer's position is set to the number of chars copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

**Returns:** This buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- isDirect

```java
public abstract boolean isDirect()
```

Tells whether or not this char buffer is direct.

**Specified by:** isDirect

in class

Buffer
**Returns:** true

if, and only if, this buffer is direct

- hashCode

```java
public int hashCode()
```

Returns the current hash code of this buffer.

The hash code of a char buffer depends only upon its remaining
elements; that is, upon the elements from

position()

up to, and
including, the element at

limit()

-

1

.

Because buffer hash codes are content-dependent, it is inadvisable
to use buffers as keys in hash maps or similar data structures unless it
is known that their contents will not change.

**Overrides:** hashCode

in class

Object
**Returns:** The current hash code of this buffer
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tells whether or not this buffer is equal to another object.

Two char buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A char buffer is not equal to any other type of object.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this buffer is to be compared
**Returns:** true

if, and only if, this buffer is equal to the
given object
**See Also:** Object.hashCode()

,

HashMap

- compareTo

```java
public int compareTo​(
CharBuffer
that)
```

Compares this buffer to another.

Two char buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

char

elements are compared as if by invoking

Character.compare(char,char)

.

A char buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

CharBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

- mismatch

```java
public int mismatch​(
CharBuffer
that)
```

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer. The index is relative to the

position

of each buffer and will be in the range of
0 (inclusive) up to the smaller of the

remaining

elements in each buffer (exclusive).

If the two buffers share a common prefix then the returned index is
the length of the common prefix and it follows that there is a mismatch
between the two buffers at that index within the respective buffers.
If one buffer is a proper prefix of the other then the returned index is
the smaller of the remaining elements in each buffer, and it follows that
the index is only valid for the buffer with the larger number of
remaining elements.
Otherwise, there is no mismatch.

**Parameters:** that

- The byte buffer to be tested for a mismatch with this buffer
**Returns:** The relative index of the first mismatch between this and the
given buffer, otherwise -1 if no mismatch.
**Since:** 11

- toString

```java
public
String
toString()
```

Returns a string containing the characters in this buffer.

The first character of the resulting string will be the character at
this buffer's position, while the last character will be the character
at index

limit()

- 1. Invoking this method does not
change the buffer's position.

**Specified by:** toString

in interface

CharSequence
**Overrides:** toString

in class

Object
**Returns:** The specified string

- length

```java
public final int length()
```

Returns the length of this character buffer.

When viewed as a character sequence, the length of a character
buffer is simply the number of characters between the position
(inclusive) and the limit (exclusive); that is, it is equivalent to

remaining()

.

**Specified by:** length

in interface

CharSequence
**Returns:** The length of this character buffer

- charAt

```java
public final char charAt​(int index)
```

Reads the character at the given index relative to the current
position.

**Specified by:** charAt

in interface

CharSequence
**Parameters:** index

- The index of the character to be read, relative to the position;
must be non-negative and smaller than

remaining()
**Returns:** The character at index

position() + index
**Throws:** IndexOutOfBoundsException

- If the preconditions on

index

do not hold

- subSequence

```java
public abstract
CharBuffer
subSequence​(int start,
int end)
```

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

The new buffer will share this buffer's content; that is, if the
content of this buffer is mutable then modifications to one buffer will
cause the other to be modified. The new buffer's capacity will be that
of this buffer, its position will be

position()

+

start

, and its limit will be

position()

+

end

. The new buffer will be
direct if, and only if, this buffer is direct, and it will be read-only
if, and only if, this buffer is read-only.

**Specified by:** subSequence

in interface

CharSequence
**Parameters:** start

- The index, relative to the current position, of the first
character in the subsequence; must be non-negative and no larger
than

remaining()
**Parameters:** end

- The index, relative to the current position, of the character
following the last character in the subsequence; must be no
smaller than

start

and no larger than

remaining()
**Returns:** The new character buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on

start

and

end

do not hold

- append

```java
public
CharBuffer
append​(
CharSequence
csq)
```

Appends the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq)

behaves in exactly the same way as the invocation

```java
dst.put(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a character buffer will return a subsequence whose
content depends upon the buffer's position and limit.

**Specified by:** append

in interface

Appendable
**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this character buffer.
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

- append

```java
public
CharBuffer
append​(
CharSequence
csq,
int start,
int end)
```

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq, start,
end)

when

csq

is not

null

, behaves in exactly the
same way as the invocation

```java
dst.put(csq.subSequence(start, end).toString())
```

**Specified by:** append

in interface

Appendable
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
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
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
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

- append

```java
public
CharBuffer
append​(char c)
```

Appends the specified char to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(c)

behaves in exactly the same way as the invocation

```java
dst.put(c)
```

**Specified by:** append

in interface

Appendable
**Parameters:** c

- The 16-bit char to append
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

- order

```java
public abstract
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order of a char buffer created by allocation or by
wrapping an existing

char

array is the

native order

of the underlying
hardware. The byte order of a char buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

**Returns:** This buffer's byte order

---

#### Method Detail

allocate

```java
public static
CharBuffer
allocate​(int capacity)
```

Allocates a new char buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

the

native order

of the underlying
hardware.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:** capacity

- The new buffer's capacity, in chars
**Returns:** The new char buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

---

#### allocate

public static

CharBuffer

allocate​(int capacity)

Allocates a new char buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

the

native order

of the underlying
hardware.

It will have a

backing array

, and its

array offset

will be zero.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

the

native order

of the underlying
hardware.

It will have a

backing array

, and its

array offset

will be zero.

wrap

```java
public static
CharBuffer
wrap​(char[] array,
int offset,
int length)
```

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity will be

array.length

, its position will be

offset

, its limit
will be

offset + length

, its mark will be undefined, and its
byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and
its

array offset

will be zero.

**Parameters:** array

- The array that will back the new buffer
**Parameters:** offset

- The offset of the subarray to be used; must be non-negative and
no larger than

array.length

. The new buffer's position
will be set to this value.
**Parameters:** length

- The length of the subarray to be used;
must be non-negative and no larger than

array.length - offset

.
The new buffer's limit will be set to

offset + length

.
**Returns:** The new char buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### wrap

public static

CharBuffer

wrap​(char[] array,
int offset,
int length)

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity will be

array.length

, its position will be

offset

, its limit
will be

offset + length

, its mark will be undefined, and its
byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and
its

array offset

will be zero.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity will be

array.length

, its position will be

offset

, its limit
will be

offset + length

, its mark will be undefined, and its
byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and
its

array offset

will be zero.

wrap

```java
public static
CharBuffer
wrap​(char[] array)
```

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:** array

- The array that will back this buffer
**Returns:** The new char buffer

---

#### wrap

public static

CharBuffer

wrap​(char[] array)

Wraps a char array into a buffer.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and its

array offset

will be zero.

The new buffer will be backed by the given char array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

the

native order

of the underlying
hardware.

Its

backing array

will be the given array, and its

array offset

will be zero.

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

wrap

```java
public static
CharBuffer
wrap​(
CharSequence
csq,
int start,
int end)
```

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The buffer's capacity will be

csq.length()

, its position will be

start

, its limit
will be

end

, and its mark will be undefined.

**Parameters:** csq

- The character sequence from which the new character buffer is to
be created
**Parameters:** start

- The index of the first character to be used;
must be non-negative and no larger than

csq.length()

.
The new buffer's position will be set to this value.
**Parameters:** end

- The index of the character following the last character to be
used; must be no smaller than

start

and no larger
than

csq.length()

.
The new buffer's limit will be set to this value.
**Returns:** The new character buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold

---

#### wrap

public static

CharBuffer

wrap​(

CharSequence

csq,
int start,
int end)

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The buffer's capacity will be

csq.length()

, its position will be

start

, its limit
will be

end

, and its mark will be undefined.

The content of the new, read-only buffer will be the content of the
given character sequence. The buffer's capacity will be

csq.length()

, its position will be

start

, its limit
will be

end

, and its mark will be undefined.

wrap

```java
public static
CharBuffer
wrap​(
CharSequence
csq)
```

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The new buffer's capacity and limit will be

csq.length()

, its position will be zero, and its mark will be
undefined.

**Parameters:** csq

- The character sequence from which the new character buffer is to
be created
**Returns:** The new character buffer

---

#### wrap

public static

CharBuffer

wrap​(

CharSequence

csq)

Wraps a character sequence into a buffer.

The content of the new, read-only buffer will be the content of the
given character sequence. The new buffer's capacity and limit will be

csq.length()

, its position will be zero, and its mark will be
undefined.

The content of the new, read-only buffer will be the content of the
given character sequence. The new buffer's capacity and limit will be

csq.length()

, its position will be zero, and its mark will be
undefined.

slice

```java
public abstract
CharBuffer
slice()
```

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of chars remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new char buffer

---

#### slice

public abstract

CharBuffer

slice()

Creates a new char buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of chars remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of chars remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of chars remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

duplicate

```java
public abstract
CharBuffer
duplicate()
```

Creates a new char buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** duplicate

in class

Buffer
**Returns:** The new char buffer

---

#### duplicate

public abstract

CharBuffer

duplicate()

Creates a new char buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

asReadOnlyBuffer

```java
public abstract
CharBuffer
asReadOnlyBuffer()
```

Creates a new, read-only char buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:** The new, read-only char buffer

---

#### asReadOnlyBuffer

public abstract

CharBuffer

asReadOnlyBuffer()

Creates a new, read-only char buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

The new buffer's capacity, limit, position,

mark values, and byte order will be identical to those of this buffer.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

get

```java
public abstract char get()
```

Relative

get

method. Reads the char at this buffer's
current position, and then increments the position.

**Returns:** The char at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

---

#### get

public abstract char get()

Relative

get

method. Reads the char at this buffer's
current position, and then increments the position.

put

```java
public abstract
CharBuffer
put​(char c)
```

Relative

put

method

(optional operation)

.

Writes the given char into this buffer at the current
position, and then increments the position.

**Parameters:** c

- The char to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public abstract

CharBuffer

put​(char c)

Relative

put

method

(optional operation)

.

Writes the given char into this buffer at the current
position, and then increments the position.

Writes the given char into this buffer at the current
position, and then increments the position.

get

```java
public abstract char get​(int index)
```

Absolute

get

method. Reads the char at the given
index.

**Parameters:** index

- The index from which the char will be read
**Returns:** The char at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

---

#### get

public abstract char get​(int index)

Absolute

get

method. Reads the char at the given
index.

put

```java
public abstract
CharBuffer
put​(int index,
char c)
```

Absolute

put

method

(optional operation)

.

Writes the given char into this buffer at the given
index.

**Parameters:** index

- The index at which the char will be written
**Parameters:** c

- The char value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public abstract

CharBuffer

put​(int index,
char c)

Absolute

put

method

(optional operation)

.

Writes the given char into this buffer at the given
index.

Writes the given char into this buffer at the given
index.

get

```java
public
CharBuffer
get​(char[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. If there are fewer chars remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

chars from this
buffer into the given array, starting at the current position of this
buffer and at the given offset in the array. The position of this
buffer is then incremented by

length

.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which chars are to be written
**Parameters:** offset

- The offset within the array of the first char to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of chars to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### get

public

CharBuffer

get​(char[] dst,
int offset,
int length)

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. If there are fewer chars remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

chars from this
buffer into the given array, starting at the current position of this
buffer and at the given offset in the array. The position of this
buffer is then incremented by

length

.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

This method transfers chars from this buffer into the given
destination array. If there are fewer chars remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

chars from this
buffer into the given array, starting at the current position of this
buffer and at the given offset in the array. The position of this
buffer is then incremented by

length

.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

Otherwise, this method copies

length

chars from this
buffer into the given array, starting at the current position of this
buffer and at the given offset in the array. The position of this
buffer is then incremented by

length

.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient chars in
this buffer and it is potentially much more efficient.

for (int i = off; i < off + len; i++)
dst[i] = src.get();

get

```java
public
CharBuffer
get​(char[] dst)
```

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

**Parameters:** dst

- The destination array
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

chars
remaining in this buffer

---

#### get

public

CharBuffer

get​(char[] dst)

Relative bulk

get

method.

This method transfers chars from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

This method transfers chars from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

src.get(a, 0, a.length)

put

```java
public
CharBuffer
put​(
CharBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the chars remaining in the given source
buffer into this buffer. If there are more chars remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

chars from the given
buffer into this buffer, starting at each buffer's current position.
The positions of both buffers are then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

**Parameters:** src

- The source buffer from which chars are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining chars in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public

CharBuffer

put​(

CharBuffer

src)

Relative bulk

put

method

(optional operation)

.

This method transfers the chars remaining in the given source
buffer into this buffer. If there are more chars remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

chars from the given
buffer into this buffer, starting at each buffer's current position.
The positions of both buffers are then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

This method transfers the chars remaining in the given source
buffer into this buffer. If there are more chars remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

chars from the given
buffer into this buffer, starting at each buffer's current position.
The positions of both buffers are then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

Otherwise, this method copies

n

=

src.remaining()

chars from the given
buffer into this buffer, starting at each buffer's current position.
The positions of both buffers are then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

In other words, an invocation of this method of the form

dst.put(src)

has exactly the same effect as the loop

```java
while (src.hasRemaining())
dst.put(src.get());
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient. If this buffer and
the source buffer share the same backing array or memory, then the
result will be as if the source elements were first copied to an
intermediate location before being written into this buffer.

while (src.hasRemaining())
dst.put(src.get());

put

```java
public
CharBuffer
put​(char[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers chars into this buffer from the given
source array. If there are more chars to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

chars from the
given array into this buffer, starting at the given offset in the array
and at the current position of this buffer. The position of this buffer
is then incremented by

length

.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:** src

- The array from which chars are to be read
**Parameters:** offset

- The offset within the array of the first char to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of chars to be read from the given array;
must be non-negative and no larger than

array.length - offset
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public

CharBuffer

put​(char[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

This method transfers chars into this buffer from the given
source array. If there are more chars to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

chars from the
given array into this buffer, starting at the given offset in the array
and at the current position of this buffer. The position of this buffer
is then incremented by

length

.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

This method transfers chars into this buffer from the given
source array. If there are more chars to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
chars are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

chars from the
given array into this buffer, starting at the given offset in the array
and at the current position of this buffer. The position of this buffer
is then incremented by

length

.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

Otherwise, this method copies

length

chars from the
given array into this buffer, starting at the given offset in the array
and at the current position of this buffer. The position of this buffer
is then incremented by

length

.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

In other words, an invocation of this method of the form

dst.put(src, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst.put(a[i]);
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

for (int i = off; i < off + len; i++)
dst.put(a[i]);

put

```java
public final
CharBuffer
put​(char[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
char array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

**Parameters:** src

- The source array
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public final

CharBuffer

put​(char[] src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
char array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

This method transfers the entire content of the given source
char array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

dst.put(a, 0, a.length)

put

```java
public
CharBuffer
put​(
String
src,
int start,
int end)
```

Relative bulk

put

method

(optional operation)

.

This method transfers chars from the given string into this
buffer. If there are more chars to be copied from the string than
remain in this buffer, that is, if

end - start

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

end

-

start

chars
from the given string into this buffer, starting at the given

start

index and at the current position of this buffer. The
position of this buffer is then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

**Parameters:** src

- The string from which chars are to be read
**Parameters:** start

- The offset within the string of the first char to be read;
must be non-negative and no larger than

string.length()
**Parameters:** end

- The offset within the string of the last char to be read,
plus one; must be non-negative and no larger than

string.length()
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

start

and

end

parameters do not hold
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public

CharBuffer

put​(

String

src,
int start,
int end)

Relative bulk

put

method

(optional operation)

.

This method transfers chars from the given string into this
buffer. If there are more chars to be copied from the string than
remain in this buffer, that is, if

end - start

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

end

-

start

chars
from the given string into this buffer, starting at the given

start

index and at the current position of this buffer. The
position of this buffer is then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

This method transfers chars from the given string into this
buffer. If there are more chars to be copied from the string than
remain in this buffer, that is, if

end - start

>

remaining()

,
then no chars are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

end

-

start

chars
from the given string into this buffer, starting at the given

start

index and at the current position of this buffer. The
position of this buffer is then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

Otherwise, this method copies

n

=

end

-

start

chars
from the given string into this buffer, starting at the given

start

index and at the current position of this buffer. The
position of this buffer is then incremented by

n

.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

In other words, an invocation of this method of the form

dst.put(src, start, end)

has exactly the same effect
as the loop

```java
for (int i = start; i < end; i++)
dst.put(src.charAt(i));
```

except that it first checks that there is sufficient space in this
buffer and it is potentially much more efficient.

for (int i = start; i < end; i++)
dst.put(src.charAt(i));

put

```java
public final
CharBuffer
put​(
String
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source string
into this buffer. An invocation of this method of the form

dst.put(s)

behaves in exactly the same way as the invocation

```java
dst.put(s, 0, s.length())
```

**Parameters:** src

- The source string
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public final

CharBuffer

put​(

String

src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source string
into this buffer. An invocation of this method of the form

dst.put(s)

behaves in exactly the same way as the invocation

```java
dst.put(s, 0, s.length())
```

This method transfers the entire content of the given source string
into this buffer. An invocation of this method of the form

dst.put(s)

behaves in exactly the same way as the invocation

```java
dst.put(s, 0, s.length())
```

dst.put(s, 0, s.length())

hasArray

```java
public final boolean hasArray()
```

Tells whether or not this buffer is backed by an accessible char
array.

If this method returns

true

then the

array

and

arrayOffset

methods may safely be invoked.

**Specified by:** hasArray

in class

Buffer
**Returns:** true

if, and only if, this buffer
is backed by an array and is not read-only

---

#### hasArray

public final boolean hasArray()

Tells whether or not this buffer is backed by an accessible char
array.

If this method returns

true

then the

array

and

arrayOffset

methods may safely be invoked.

If this method returns

true

then the

array

and

arrayOffset

methods may safely be invoked.

array

```java
public final char[] array()
```

Returns the char array that backs this
buffer

(optional operation)

.

Modifications to this buffer's content will cause the returned
array's content to be modified, and vice versa.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:** array

in class

Buffer
**Returns:** The array that backs this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
**Throws:** UnsupportedOperationException

- If this buffer is not backed by an accessible array

---

#### array

public final char[] array()

Returns the char array that backs this
buffer

(optional operation)

.

Modifications to this buffer's content will cause the returned
array's content to be modified, and vice versa.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

Modifications to this buffer's content will cause the returned
array's content to be modified, and vice versa.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

arrayOffset

```java
public final int arrayOffset()
```

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

If this buffer is backed by an array then buffer position

p

corresponds to array index

p

+

arrayOffset()

.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

**Specified by:** arrayOffset

in class

Buffer
**Returns:** The offset within this buffer's array
of the first element of the buffer
**Throws:** ReadOnlyBufferException

- If this buffer is backed by an array but is read-only
**Throws:** UnsupportedOperationException

- If this buffer is not backed by an accessible array

---

#### arrayOffset

public final int arrayOffset()

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

If this buffer is backed by an array then buffer position

p

corresponds to array index

p

+

arrayOffset()

.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

If this buffer is backed by an array then buffer position

p

corresponds to array index

p

+

arrayOffset()

.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

Invoke the

hasArray

method before invoking this
method in order to ensure that this buffer has an accessible backing
array.

compact

```java
public abstract
CharBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The chars between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
char at index

p

=

position()

is copied
to index zero, the char at index

p

+ 1 is copied
to index one, and so forth until the char at index

limit()

- 1 is copied to index

n

=

limit()

-

1

-

p

.
The buffer's position is then set to

n+1

and its limit is set to
its capacity. The mark, if defined, is discarded.

The buffer's position is set to the number of chars copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

**Returns:** This buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### compact

public abstract

CharBuffer

compact()

Compacts this buffer

(optional operation)

.

The chars between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
char at index

p

=

position()

is copied
to index zero, the char at index

p

+ 1 is copied
to index one, and so forth until the char at index

limit()

- 1 is copied to index

n

=

limit()

-

1

-

p

.
The buffer's position is then set to

n+1

and its limit is set to
its capacity. The mark, if defined, is discarded.

The buffer's position is set to the number of chars copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

The chars between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
char at index

p

=

position()

is copied
to index zero, the char at index

p

+ 1 is copied
to index one, and so forth until the char at index

limit()

- 1 is copied to index

n

=

limit()

-

1

-

p

.
The buffer's position is then set to

n+1

and its limit is set to
its capacity. The mark, if defined, is discarded.

The buffer's position is set to the number of chars copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

The buffer's position is set to the number of chars copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

isDirect

```java
public abstract boolean isDirect()
```

Tells whether or not this char buffer is direct.

**Specified by:** isDirect

in class

Buffer
**Returns:** true

if, and only if, this buffer is direct

---

#### isDirect

public abstract boolean isDirect()

Tells whether or not this char buffer is direct.

hashCode

```java
public int hashCode()
```

Returns the current hash code of this buffer.

The hash code of a char buffer depends only upon its remaining
elements; that is, upon the elements from

position()

up to, and
including, the element at

limit()

-

1

.

Because buffer hash codes are content-dependent, it is inadvisable
to use buffers as keys in hash maps or similar data structures unless it
is known that their contents will not change.

**Overrides:** hashCode

in class

Object
**Returns:** The current hash code of this buffer
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the current hash code of this buffer.

The hash code of a char buffer depends only upon its remaining
elements; that is, upon the elements from

position()

up to, and
including, the element at

limit()

-

1

.

Because buffer hash codes are content-dependent, it is inadvisable
to use buffers as keys in hash maps or similar data structures unless it
is known that their contents will not change.

The hash code of a char buffer depends only upon its remaining
elements; that is, upon the elements from

position()

up to, and
including, the element at

limit()

-

1

.

Because buffer hash codes are content-dependent, it is inadvisable
to use buffers as keys in hash maps or similar data structures unless it
is known that their contents will not change.

Because buffer hash codes are content-dependent, it is inadvisable
to use buffers as keys in hash maps or similar data structures unless it
is known that their contents will not change.

equals

```java
public boolean equals​(
Object
ob)
```

Tells whether or not this buffer is equal to another object.

Two char buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A char buffer is not equal to any other type of object.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this buffer is to be compared
**Returns:** true

if, and only if, this buffer is equal to the
given object
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Tells whether or not this buffer is equal to another object.

Two char buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A char buffer is not equal to any other type of object.

Two char buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A char buffer is not equal to any other type of object.

They have the same element type,

They have the same number of remaining elements, and

The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

They have the same element type,

They have the same number of remaining elements, and

The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A char buffer is not equal to any other type of object.

compareTo

```java
public int compareTo​(
CharBuffer
that)
```

Compares this buffer to another.

Two char buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

char

elements are compared as if by invoking

Character.compare(char,char)

.

A char buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

CharBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

---

#### compareTo

public int compareTo​(

CharBuffer

that)

Compares this buffer to another.

Two char buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

char

elements are compared as if by invoking

Character.compare(char,char)

.

A char buffer is not comparable to any other type of object.

Two char buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

char

elements are compared as if by invoking

Character.compare(char,char)

.

A char buffer is not comparable to any other type of object.

A char buffer is not comparable to any other type of object.

mismatch

```java
public int mismatch​(
CharBuffer
that)
```

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer. The index is relative to the

position

of each buffer and will be in the range of
0 (inclusive) up to the smaller of the

remaining

elements in each buffer (exclusive).

If the two buffers share a common prefix then the returned index is
the length of the common prefix and it follows that there is a mismatch
between the two buffers at that index within the respective buffers.
If one buffer is a proper prefix of the other then the returned index is
the smaller of the remaining elements in each buffer, and it follows that
the index is only valid for the buffer with the larger number of
remaining elements.
Otherwise, there is no mismatch.

**Parameters:** that

- The byte buffer to be tested for a mismatch with this buffer
**Returns:** The relative index of the first mismatch between this and the
given buffer, otherwise -1 if no mismatch.
**Since:** 11

---

#### mismatch

public int mismatch​(

CharBuffer

that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer. The index is relative to the

position

of each buffer and will be in the range of
0 (inclusive) up to the smaller of the

remaining

elements in each buffer (exclusive).

If the two buffers share a common prefix then the returned index is
the length of the common prefix and it follows that there is a mismatch
between the two buffers at that index within the respective buffers.
If one buffer is a proper prefix of the other then the returned index is
the smaller of the remaining elements in each buffer, and it follows that
the index is only valid for the buffer with the larger number of
remaining elements.
Otherwise, there is no mismatch.

If the two buffers share a common prefix then the returned index is
the length of the common prefix and it follows that there is a mismatch
between the two buffers at that index within the respective buffers.
If one buffer is a proper prefix of the other then the returned index is
the smaller of the remaining elements in each buffer, and it follows that
the index is only valid for the buffer with the larger number of
remaining elements.
Otherwise, there is no mismatch.

toString

```java
public
String
toString()
```

Returns a string containing the characters in this buffer.

The first character of the resulting string will be the character at
this buffer's position, while the last character will be the character
at index

limit()

- 1. Invoking this method does not
change the buffer's position.

**Specified by:** toString

in interface

CharSequence
**Overrides:** toString

in class

Object
**Returns:** The specified string

---

#### toString

public

String

toString()

Returns a string containing the characters in this buffer.

The first character of the resulting string will be the character at
this buffer's position, while the last character will be the character
at index

limit()

- 1. Invoking this method does not
change the buffer's position.

The first character of the resulting string will be the character at
this buffer's position, while the last character will be the character
at index

limit()

- 1. Invoking this method does not
change the buffer's position.

length

```java
public final int length()
```

Returns the length of this character buffer.

When viewed as a character sequence, the length of a character
buffer is simply the number of characters between the position
(inclusive) and the limit (exclusive); that is, it is equivalent to

remaining()

.

**Specified by:** length

in interface

CharSequence
**Returns:** The length of this character buffer

---

#### length

public final int length()

Returns the length of this character buffer.

When viewed as a character sequence, the length of a character
buffer is simply the number of characters between the position
(inclusive) and the limit (exclusive); that is, it is equivalent to

remaining()

.

When viewed as a character sequence, the length of a character
buffer is simply the number of characters between the position
(inclusive) and the limit (exclusive); that is, it is equivalent to

remaining()

.

charAt

```java
public final char charAt​(int index)
```

Reads the character at the given index relative to the current
position.

**Specified by:** charAt

in interface

CharSequence
**Parameters:** index

- The index of the character to be read, relative to the position;
must be non-negative and smaller than

remaining()
**Returns:** The character at index

position() + index
**Throws:** IndexOutOfBoundsException

- If the preconditions on

index

do not hold

---

#### charAt

public final char charAt​(int index)

Reads the character at the given index relative to the current
position.

subSequence

```java
public abstract
CharBuffer
subSequence​(int start,
int end)
```

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

The new buffer will share this buffer's content; that is, if the
content of this buffer is mutable then modifications to one buffer will
cause the other to be modified. The new buffer's capacity will be that
of this buffer, its position will be

position()

+

start

, and its limit will be

position()

+

end

. The new buffer will be
direct if, and only if, this buffer is direct, and it will be read-only
if, and only if, this buffer is read-only.

**Specified by:** subSequence

in interface

CharSequence
**Parameters:** start

- The index, relative to the current position, of the first
character in the subsequence; must be non-negative and no larger
than

remaining()
**Parameters:** end

- The index, relative to the current position, of the character
following the last character in the subsequence; must be no
smaller than

start

and no larger than

remaining()
**Returns:** The new character buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on

start

and

end

do not hold

---

#### subSequence

public abstract

CharBuffer

subSequence​(int start,
int end)

Creates a new character buffer that represents the specified subsequence
of this buffer, relative to the current position.

The new buffer will share this buffer's content; that is, if the
content of this buffer is mutable then modifications to one buffer will
cause the other to be modified. The new buffer's capacity will be that
of this buffer, its position will be

position()

+

start

, and its limit will be

position()

+

end

. The new buffer will be
direct if, and only if, this buffer is direct, and it will be read-only
if, and only if, this buffer is read-only.

The new buffer will share this buffer's content; that is, if the
content of this buffer is mutable then modifications to one buffer will
cause the other to be modified. The new buffer's capacity will be that
of this buffer, its position will be

position()

+

start

, and its limit will be

position()

+

end

. The new buffer will be
direct if, and only if, this buffer is direct, and it will be read-only
if, and only if, this buffer is read-only.

append

```java
public
CharBuffer
append​(
CharSequence
csq)
```

Appends the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq)

behaves in exactly the same way as the invocation

```java
dst.put(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a character buffer will return a subsequence whose
content depends upon the buffer's position and limit.

**Specified by:** append

in interface

Appendable
**Parameters:** csq

- The character sequence to append. If

csq

is

null

, then the four characters

"null"

are
appended to this character buffer.
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

---

#### append

public

CharBuffer

append​(

CharSequence

csq)

Appends the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq)

behaves in exactly the same way as the invocation

```java
dst.put(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a character buffer will return a subsequence whose
content depends upon the buffer's position and limit.

An invocation of this method of the form

dst.append(csq)

behaves in exactly the same way as the invocation

```java
dst.put(csq.toString())
```

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a character buffer will return a subsequence whose
content depends upon the buffer's position and limit.

dst.put(csq.toString())

Depending on the specification of

toString

for the
character sequence

csq

, the entire sequence may not be
appended. For instance, invoking the

toString

method of a character buffer will return a subsequence whose
content depends upon the buffer's position and limit.

append

```java
public
CharBuffer
append​(
CharSequence
csq,
int start,
int end)
```

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq, start,
end)

when

csq

is not

null

, behaves in exactly the
same way as the invocation

```java
dst.put(csq.subSequence(start, end).toString())
```

**Specified by:** append

in interface

Appendable
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
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
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
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

---

#### append

public

CharBuffer

append​(

CharSequence

csq,
int start,
int end)

Appends a subsequence of the specified character sequence to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(csq, start,
end)

when

csq

is not

null

, behaves in exactly the
same way as the invocation

```java
dst.put(csq.subSequence(start, end).toString())
```

An invocation of this method of the form

dst.append(csq, start,
end)

when

csq

is not

null

, behaves in exactly the
same way as the invocation

```java
dst.put(csq.subSequence(start, end).toString())
```

dst.put(csq.subSequence(start, end).toString())

append

```java
public
CharBuffer
append​(char c)
```

Appends the specified char to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(c)

behaves in exactly the same way as the invocation

```java
dst.put(c)
```

**Specified by:** append

in interface

Appendable
**Parameters:** c

- The 16-bit char to append
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only
**Since:** 1.5

---

#### append

public

CharBuffer

append​(char c)

Appends the specified char to this
buffer

(optional operation)

.

An invocation of this method of the form

dst.append(c)

behaves in exactly the same way as the invocation

```java
dst.put(c)
```

An invocation of this method of the form

dst.append(c)

behaves in exactly the same way as the invocation

```java
dst.put(c)
```

dst.put(c)

order

```java
public abstract
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order of a char buffer created by allocation or by
wrapping an existing

char

array is the

native order

of the underlying
hardware. The byte order of a char buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

**Returns:** This buffer's byte order

---

#### order

public abstract

ByteOrder

order()

Retrieves this buffer's byte order.

The byte order of a char buffer created by allocation or by
wrapping an existing

char

array is the

native order

of the underlying
hardware. The byte order of a char buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

The byte order of a char buffer created by allocation or by
wrapping an existing

char

array is the

native order

of the underlying
hardware. The byte order of a char buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

---

