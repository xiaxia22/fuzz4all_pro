# Class ByteBuffer

**Source:** `java.base\java\nio\ByteBuffer.html`

### Class Description

```java
public abstract class
ByteBuffer

extends
Buffer

implements
Comparable
<
ByteBuffer
>
```

A byte buffer.

This class defines six categories of operations upon
byte buffers:

- Absolute and relative

get

and

put

methods that read and write
single bytes;
- Relative

bulk get

methods that transfer contiguous sequences of bytes from this buffer
into an array;
- Relative

bulk put

methods that transfer contiguous sequences of bytes from a
byte array or some other byte
buffer into this buffer;
- Absolute and relative

get

and

put

methods that read and
write values of other primitive types, translating them to and from
sequences of bytes in a particular byte order;
- Methods for creating

view buffers

,
which allow a byte buffer to be viewed as a buffer containing values of
some other primitive type; and
- A method for

compacting

a byte buffer.

Byte buffers can be created either by

allocation

, which allocates space for the buffer's

content, or by

wrapping

an
existing byte array into a buffer.

Direct

vs.

non-direct buffers

A byte buffer is either

direct

or

non-direct

. Given a
direct byte buffer, the Java virtual machine will make a best effort to
perform native I/O operations directly upon it. That is, it will attempt to
avoid copying the buffer's content to (or from) an intermediate buffer
before (or after) each invocation of one of the underlying operating
system's native I/O operations.

A direct byte buffer may be created by invoking the

allocateDirect

factory method of this class. The
buffers returned by this method typically have somewhat higher allocation
and deallocation costs than non-direct buffers. The contents of direct
buffers may reside outside of the normal garbage-collected heap, and so
their impact upon the memory footprint of an application might not be
obvious. It is therefore recommended that direct buffers be allocated
primarily for large, long-lived buffers that are subject to the underlying
system's native I/O operations. In general it is best to allocate direct
buffers only when they yield a measurable gain in program performance.

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

**All Implemented Interfaces:** Comparable

<

ByteBuffer

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ByteBuffer
allocateDirect​(int capacity)

Allocates a new direct byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

. Whether or not it has a

backing array

is unspecified.

**Parameters:**
- capacity

- The new buffer's capacity, in bytes

**Returns:**
- The new byte buffer

**Throws:**
- IllegalArgumentException

- If the

capacity

is a negative integer

---

#### public static
ByteBuffer
allocate​(int capacity)

Allocates a new byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:**
- capacity

- The new buffer's capacity, in bytes

**Returns:**
- The new byte buffer

**Throws:**
- IllegalArgumentException

- If the

capacity

is a negative integer

---

#### public static
ByteBuffer
wrap​(byte[] array,
int offset,
int length)

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
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

BIG_ENDIAN

.

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
- The new byte buffer

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### public static
ByteBuffer
wrap​(byte[] array)

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:**
- array

- The array that will back this buffer

**Returns:**
- The new byte buffer

---

#### public abstract
ByteBuffer
slice()

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:**
- slice

in class

Buffer

**Returns:**
- The new byte buffer

**See Also:**
- alignedSlice(int)

---

#### public abstract
ByteBuffer
duplicate()

Creates a new byte buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:**
- duplicate

in class

Buffer

**Returns:**
- The new byte buffer

---

#### public abstract
ByteBuffer
asReadOnlyBuffer()

Creates a new, read-only byte buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:**
- The new, read-only byte buffer

---

#### public abstract byte get()

Relative

get

method. Reads the byte at this buffer's
current position, and then increments the position.

**Returns:**
- The byte at the buffer's current position

**Throws:**
- BufferUnderflowException

- If the buffer's current position is not smaller than its limit

---

#### public abstract
ByteBuffer
put​(byte b)

Relative

put

method

(optional operation)

.

Writes the given byte into this buffer at the current
position, and then increments the position.

**Parameters:**
- b

- The byte to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If this buffer's current position is not smaller than its limit
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract byte get​(int index)

Absolute

get

method. Reads the byte at the given
index.

**Parameters:**
- index

- The index from which the byte will be read

**Returns:**
- The byte at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

---

#### public abstract
ByteBuffer
put​(int index,
byte b)

Absolute

put

method

(optional operation)

.

Writes the given byte into this buffer at the given
index.

**Parameters:**
- index

- The index at which the byte will be written
- b

- The byte value to be written

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
ByteBuffer
get​(byte[] dst,
int offset,
int length)

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
destination array. If there are fewer bytes remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

bytes from this
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

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

**Parameters:**
- dst

- The array into which bytes are to be written
- offset

- The offset within the array of the first byte to be
written; must be non-negative and no larger than

dst.length
- length

- The maximum number of bytes to be written to the given
array; must be non-negative and no larger than

dst.length - offset

**Returns:**
- This buffer

**Throws:**
- BufferUnderflowException

- If there are fewer than

length

bytes
remaining in this buffer
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### public
ByteBuffer
get​(byte[] dst)

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
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

bytes
remaining in this buffer

---

#### public
ByteBuffer
put​(
ByteBuffer
src)

Relative bulk

put

method

(optional operation)

.

This method transfers the bytes remaining in the given source
buffer into this buffer. If there are more bytes remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no bytes are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

bytes from the given
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

- The source buffer from which bytes are to be read;
must not be this buffer

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
for the remaining bytes in the source buffer
- IllegalArgumentException

- If the source buffer is this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public
ByteBuffer
put​(byte[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

This method transfers bytes into this buffer from the given
source array. If there are more bytes to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

bytes from the
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

- The array from which bytes are to be read
- offset

- The offset within the array of the first byte to be read;
must be non-negative and no larger than

array.length
- length

- The number of bytes to be read from the given array;
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
ByteBuffer
put​(byte[] src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
byte array into this buffer. An invocation of this method of the
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

#### public final boolean hasArray()

Tells whether or not this buffer is backed by an accessible byte
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

#### public final byte[] array()

Returns the byte array that backs this
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
ByteBuffer
compact()

Compacts this buffer

(optional operation)

.

The bytes between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
byte at index

p

=

position()

is copied
to index zero, the byte at index

p

+ 1 is copied
to index one, and so forth until the byte at index

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

The buffer's position is set to the number of bytes copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

Invoke this method after writing data from a buffer in case the
write was incomplete. The following loop, for example, copies bytes
from one channel to another via the buffer

buf

:

```java
buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}
```

**Returns:**
- This buffer

**Throws:**
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract boolean isDirect()

Tells whether or not this byte buffer is direct.

**Specified by:**
- isDirect

in class

Buffer

**Returns:**
- true

if, and only if, this buffer is direct

---

#### public
String
toString()

Returns a string summarizing the state of this buffer.

**Overrides:**
- toString

in class

Object

**Returns:**
- A summary string

---

#### public int hashCode()

Returns the current hash code of this buffer.

The hash code of a byte buffer depends only upon its remaining
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

Two byte buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A byte buffer is not equal to any other type of object.

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
ByteBuffer
that)

Compares this buffer to another.

Two byte buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

byte

elements are compared as if by invoking

Byte.compare(byte,byte)

.

A byte buffer is not comparable to any other type of object.

**Specified by:**
- compareTo

in interface

Comparable

<

ByteBuffer

>

**Parameters:**
- that

- the object to be compared.

**Returns:**
- A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

---

#### public int mismatch​(
ByteBuffer
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

#### public final
ByteOrder
order()

Retrieves this buffer's byte order.

The byte order is used when reading or writing multibyte values, and
when creating buffers that are views of this byte buffer. The order of
a newly-created byte buffer is always

BIG_ENDIAN

.

**Returns:**
- This buffer's byte order

---

#### public final
ByteBuffer
order​(
ByteOrder
bo)

Modifies this buffer's byte order.

**Parameters:**
- bo

- The new byte order,
either

BIG_ENDIAN

or

LITTLE_ENDIAN

**Returns:**
- This buffer

---

#### public final int alignmentOffset​(int index,
int unitSize)

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

A return value greater than zero indicates the address of the byte at
the index is misaligned for the unit size, and the value's quantity
indicates how much the index should be rounded up or down to locate a
byte at an aligned address. Otherwise, a value of

0

indicates
that the address of the byte at the index is aligned for the unit size.

**Parameters:**
- index

- The index to query for alignment offset, must be non-negative, no
upper bounds check is performed
- unitSize

- The unit size in bytes, must be a power of

2

**Returns:**
- The indexed byte's memory address modulus the unit size

**Throws:**
- IllegalArgumentException

- If the index is negative or the unit size is not a power of

2
- UnsupportedOperationException

- If the native platform does not guarantee stable alignment offset
values for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.

**See Also:**
- alignedSlice(int)

**Since:**
- 9

**API Note:**
- This method may be utilized to determine if unit size bytes from an
index can be accessed atomically, if supported by the native platform.

**Implementation Note:**
- This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.

---

#### public final
ByteBuffer
alignedSlice​(int unitSize)

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

The content of the new buffer will start at this buffer's current
position rounded up to the index of the nearest aligned byte for the
given unit size, and end at this buffer's limit rounded down to the index
of the nearest aligned byte for the given unit size.
If rounding results in out-of-bound values then the new buffer's capacity
and limit will be zero. If rounding is within bounds the following
expressions will be true for a new buffer

nb

and unit size

unitSize

:

```java
nb.alignmentOffset(0, unitSize) == 0
nb.alignmentOffset(nb.limit(), unitSize) == 0
```

Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Parameters:**
- unitSize

- The unit size in bytes, must be a power of

2

**Returns:**
- The new byte buffer

**Throws:**
- IllegalArgumentException

- If the unit size not a power of

2
- UnsupportedOperationException

- If the native platform does not guarantee stable aligned slices
for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.

**See Also:**
- alignmentOffset(int, int)

,

slice()

**Since:**
- 9

**API Note:**
- This method may be utilized to create a new buffer where unit size bytes
from index, that is a multiple of the unit size, may be accessed
atomically, if supported by the native platform.

**Implementation Note:**
- This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.

---

#### public abstract char getChar()

Relative

get

method for reading a char value.

Reads the next two bytes at this buffer's current position,
composing them into a char value according to the current byte order,
and then increments the position by two.

**Returns:**
- The char value at the buffer's current position

**Throws:**
- BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

---

#### public abstract
ByteBuffer
putChar​(char value)

Relative

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:**
- value

- The char value to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract char getChar​(int index)

Absolute

get

method for reading a char value.

Reads two bytes at the given index, composing them into a
char value according to the current byte order.

**Parameters:**
- index

- The index from which the bytes will be read

**Returns:**
- The char value at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

---

#### public abstract
ByteBuffer
putChar​(int index,
char value)

Absolute

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the given index.

**Parameters:**
- index

- The index at which the bytes will be written
- value

- The char value to be written

**Returns:**
- This buffer

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract
CharBuffer
asCharBuffer()

Creates a view of this byte buffer as a char buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:**
- A new char buffer

---

#### public abstract short getShort()

Relative

get

method for reading a short value.

Reads the next two bytes at this buffer's current position,
composing them into a short value according to the current byte order,
and then increments the position by two.

**Returns:**
- The short value at the buffer's current position

**Throws:**
- BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

---

#### public abstract
ByteBuffer
putShort​(short value)

Relative

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:**
- value

- The short value to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract short getShort​(int index)

Absolute

get

method for reading a short value.

Reads two bytes at the given index, composing them into a
short value according to the current byte order.

**Parameters:**
- index

- The index from which the bytes will be read

**Returns:**
- The short value at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

---

#### public abstract
ByteBuffer
putShort​(int index,
short value)

Absolute

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the given index.

**Parameters:**
- index

- The index at which the bytes will be written
- value

- The short value to be written

**Returns:**
- This buffer

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract
ShortBuffer
asShortBuffer()

Creates a view of this byte buffer as a short buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:**
- A new short buffer

---

#### public abstract int getInt()

Relative

get

method for reading an int value.

Reads the next four bytes at this buffer's current position,
composing them into an int value according to the current byte order,
and then increments the position by four.

**Returns:**
- The int value at the buffer's current position

**Throws:**
- BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

---

#### public abstract
ByteBuffer
putInt​(int value)

Relative

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:**
- value

- The int value to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract int getInt​(int index)

Absolute

get

method for reading an int value.

Reads four bytes at the given index, composing them into a
int value according to the current byte order.

**Parameters:**
- index

- The index from which the bytes will be read

**Returns:**
- The int value at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

---

#### public abstract
ByteBuffer
putInt​(int index,
int value)

Absolute

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the given index.

**Parameters:**
- index

- The index at which the bytes will be written
- value

- The int value to be written

**Returns:**
- This buffer

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract
IntBuffer
asIntBuffer()

Creates a view of this byte buffer as an int buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:**
- A new int buffer

---

#### public abstract long getLong()

Relative

get

method for reading a long value.

Reads the next eight bytes at this buffer's current position,
composing them into a long value according to the current byte order,
and then increments the position by eight.

**Returns:**
- The long value at the buffer's current position

**Throws:**
- BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

---

#### public abstract
ByteBuffer
putLong​(long value)

Relative

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:**
- value

- The long value to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract long getLong​(int index)

Absolute

get

method for reading a long value.

Reads eight bytes at the given index, composing them into a
long value according to the current byte order.

**Parameters:**
- index

- The index from which the bytes will be read

**Returns:**
- The long value at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

---

#### public abstract
ByteBuffer
putLong​(int index,
long value)

Absolute

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the given index.

**Parameters:**
- index

- The index at which the bytes will be written
- value

- The long value to be written

**Returns:**
- This buffer

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract
LongBuffer
asLongBuffer()

Creates a view of this byte buffer as a long buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:**
- A new long buffer

---

#### public abstract float getFloat()

Relative

get

method for reading a float value.

Reads the next four bytes at this buffer's current position,
composing them into a float value according to the current byte order,
and then increments the position by four.

**Returns:**
- The float value at the buffer's current position

**Throws:**
- BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

---

#### public abstract
ByteBuffer
putFloat​(float value)

Relative

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:**
- value

- The float value to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract float getFloat​(int index)

Absolute

get

method for reading a float value.

Reads four bytes at the given index, composing them into a
float value according to the current byte order.

**Parameters:**
- index

- The index from which the bytes will be read

**Returns:**
- The float value at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

---

#### public abstract
ByteBuffer
putFloat​(int index,
float value)

Absolute

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the given index.

**Parameters:**
- index

- The index at which the bytes will be written
- value

- The float value to be written

**Returns:**
- This buffer

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract
FloatBuffer
asFloatBuffer()

Creates a view of this byte buffer as a float buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:**
- A new float buffer

---

#### public abstract double getDouble()

Relative

get

method for reading a double value.

Reads the next eight bytes at this buffer's current position,
composing them into a double value according to the current byte order,
and then increments the position by eight.

**Returns:**
- The double value at the buffer's current position

**Throws:**
- BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

---

#### public abstract
ByteBuffer
putDouble​(double value)

Relative

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:**
- value

- The double value to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract double getDouble​(int index)

Absolute

get

method for reading a double value.

Reads eight bytes at the given index, composing them into a
double value according to the current byte order.

**Parameters:**
- index

- The index from which the bytes will be read

**Returns:**
- The double value at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

---

#### public abstract
ByteBuffer
putDouble​(int index,
double value)

Absolute

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the given index.

**Parameters:**
- index

- The index at which the bytes will be written
- value

- The double value to be written

**Returns:**
- This buffer

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract
DoubleBuffer
asDoubleBuffer()

Creates a view of this byte buffer as a double buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:**
- A new double buffer

---

### Additional Sections

#### Class ByteBuffer

java.lang.Object

- java.nio.Buffer
- - java.nio.ByteBuffer

java.nio.Buffer

- java.nio.ByteBuffer

java.nio.ByteBuffer

**All Implemented Interfaces:** Comparable

<

ByteBuffer

>

**Direct Known Subclasses:** MappedByteBuffer

```java
public abstract class
ByteBuffer

extends
Buffer

implements
Comparable
<
ByteBuffer
>
```

A byte buffer.

This class defines six categories of operations upon
byte buffers:

- Absolute and relative

get

and

put

methods that read and write
single bytes;
- Relative

bulk get

methods that transfer contiguous sequences of bytes from this buffer
into an array;
- Relative

bulk put

methods that transfer contiguous sequences of bytes from a
byte array or some other byte
buffer into this buffer;
- Absolute and relative

get

and

put

methods that read and
write values of other primitive types, translating them to and from
sequences of bytes in a particular byte order;
- Methods for creating

view buffers

,
which allow a byte buffer to be viewed as a buffer containing values of
some other primitive type; and
- A method for

compacting

a byte buffer.

Byte buffers can be created either by

allocation

, which allocates space for the buffer's

content, or by

wrapping

an
existing byte array into a buffer.

Direct

vs.

non-direct buffers

A byte buffer is either

direct

or

non-direct

. Given a
direct byte buffer, the Java virtual machine will make a best effort to
perform native I/O operations directly upon it. That is, it will attempt to
avoid copying the buffer's content to (or from) an intermediate buffer
before (or after) each invocation of one of the underlying operating
system's native I/O operations.

A direct byte buffer may be created by invoking the

allocateDirect

factory method of this class. The
buffers returned by this method typically have somewhat higher allocation
and deallocation costs than non-direct buffers. The contents of direct
buffers may reside outside of the normal garbage-collected heap, and so
their impact upon the memory footprint of an application might not be
obvious. It is therefore recommended that direct buffers be allocated
primarily for large, long-lived buffers that are subject to the underlying
system's native I/O operations. In general it is best to allocate direct
buffers only when they yield a measurable gain in program performance.

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

**Since:** 1.4

public abstract class

ByteBuffer

extends

Buffer

implements

Comparable

<

ByteBuffer

>

A byte buffer.

This class defines six categories of operations upon
byte buffers:

- Absolute and relative

get

and

put

methods that read and write
single bytes;
- Relative

bulk get

methods that transfer contiguous sequences of bytes from this buffer
into an array;
- Relative

bulk put

methods that transfer contiguous sequences of bytes from a
byte array or some other byte
buffer into this buffer;
- Absolute and relative

get

and

put

methods that read and
write values of other primitive types, translating them to and from
sequences of bytes in a particular byte order;
- Methods for creating

view buffers

,
which allow a byte buffer to be viewed as a buffer containing values of
some other primitive type; and
- A method for

compacting

a byte buffer.

Byte buffers can be created either by

allocation

, which allocates space for the buffer's

content, or by

wrapping

an
existing byte array into a buffer.

Direct

vs.

non-direct buffers

A byte buffer is either

direct

or

non-direct

. Given a
direct byte buffer, the Java virtual machine will make a best effort to
perform native I/O operations directly upon it. That is, it will attempt to
avoid copying the buffer's content to (or from) an intermediate buffer
before (or after) each invocation of one of the underlying operating
system's native I/O operations.

A direct byte buffer may be created by invoking the

allocateDirect

factory method of this class. The
buffers returned by this method typically have somewhat higher allocation
and deallocation costs than non-direct buffers. The contents of direct
buffers may reside outside of the normal garbage-collected heap, and so
their impact upon the memory footprint of an application might not be
obvious. It is therefore recommended that direct buffers be allocated
primarily for large, long-lived buffers that are subject to the underlying
system's native I/O operations. In general it is best to allocate direct
buffers only when they yield a measurable gain in program performance.

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

This class defines six categories of operations upon
byte buffers:

- Absolute and relative

get

and

put

methods that read and write
single bytes;
- Relative

bulk get

methods that transfer contiguous sequences of bytes from this buffer
into an array;
- Relative

bulk put

methods that transfer contiguous sequences of bytes from a
byte array or some other byte
buffer into this buffer;
- Absolute and relative

get

and

put

methods that read and
write values of other primitive types, translating them to and from
sequences of bytes in a particular byte order;
- Methods for creating

view buffers

,
which allow a byte buffer to be viewed as a buffer containing values of
some other primitive type; and
- A method for

compacting

a byte buffer.

Byte buffers can be created either by

allocation

, which allocates space for the buffer's

content, or by

wrapping

an
existing byte array into a buffer.

Direct

vs.

non-direct buffers

A byte buffer is either

direct

or

non-direct

. Given a
direct byte buffer, the Java virtual machine will make a best effort to
perform native I/O operations directly upon it. That is, it will attempt to
avoid copying the buffer's content to (or from) an intermediate buffer
before (or after) each invocation of one of the underlying operating
system's native I/O operations.

A direct byte buffer may be created by invoking the

allocateDirect

factory method of this class. The
buffers returned by this method typically have somewhat higher allocation
and deallocation costs than non-direct buffers. The contents of direct
buffers may reside outside of the normal garbage-collected heap, and so
their impact upon the memory footprint of an application might not be
obvious. It is therefore recommended that direct buffers be allocated
primarily for large, long-lived buffers that are subject to the underlying
system's native I/O operations. In general it is best to allocate direct
buffers only when they yield a measurable gain in program performance.

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

Absolute and relative

get

and

put

methods that read and write
single bytes;

Relative

bulk get

methods that transfer contiguous sequences of bytes from this buffer
into an array;

Relative

bulk put

methods that transfer contiguous sequences of bytes from a
byte array or some other byte
buffer into this buffer;

Absolute and relative

get

and

put

methods that read and
write values of other primitive types, translating them to and from
sequences of bytes in a particular byte order;

Methods for creating

view buffers

,
which allow a byte buffer to be viewed as a buffer containing values of
some other primitive type; and

A method for

compacting

a byte buffer.

Absolute and relative

get

and

put

methods that read and write
single bytes;

Relative

bulk get

methods that transfer contiguous sequences of bytes from this buffer
into an array;

Relative

bulk put

methods that transfer contiguous sequences of bytes from a
byte array or some other byte
buffer into this buffer;

Absolute and relative

get

and

put

methods that read and
write values of other primitive types, translating them to and from
sequences of bytes in a particular byte order;

Methods for creating

view buffers

,
which allow a byte buffer to be viewed as a buffer containing values of
some other primitive type; and

A method for

compacting

a byte buffer.

Byte buffers can be created either by

allocation

, which allocates space for the buffer's

content, or by

wrapping

an
existing byte array into a buffer.

Direct

vs.

non-direct buffers

A byte buffer is either

direct

or

non-direct

. Given a
direct byte buffer, the Java virtual machine will make a best effort to
perform native I/O operations directly upon it. That is, it will attempt to
avoid copying the buffer's content to (or from) an intermediate buffer
before (or after) each invocation of one of the underlying operating
system's native I/O operations.

A direct byte buffer may be created by invoking the

allocateDirect

factory method of this class. The
buffers returned by this method typically have somewhat higher allocation
and deallocation costs than non-direct buffers. The contents of direct
buffers may reside outside of the normal garbage-collected heap, and so
their impact upon the memory footprint of an application might not be
obvious. It is therefore recommended that direct buffers be allocated
primarily for large, long-lived buffers that are subject to the underlying
system's native I/O operations. In general it is best to allocate direct
buffers only when they yield a measurable gain in program performance.

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

---

#### Direct vs. non-direct buffers

A byte buffer is either

direct

or

non-direct

. Given a
direct byte buffer, the Java virtual machine will make a best effort to
perform native I/O operations directly upon it. That is, it will attempt to
avoid copying the buffer's content to (or from) an intermediate buffer
before (or after) each invocation of one of the underlying operating
system's native I/O operations.

A direct byte buffer may be created by invoking the

allocateDirect

factory method of this class. The
buffers returned by this method typically have somewhat higher allocation
and deallocation costs than non-direct buffers. The contents of direct
buffers may reside outside of the normal garbage-collected heap, and so
their impact upon the memory footprint of an application might not be
obvious. It is therefore recommended that direct buffers be allocated
primarily for large, long-lived buffers that are subject to the underlying
system's native I/O operations. In general it is best to allocate direct
buffers only when they yield a measurable gain in program performance.

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

A direct byte buffer may be created by invoking the

allocateDirect

factory method of this class. The
buffers returned by this method typically have somewhat higher allocation
and deallocation costs than non-direct buffers. The contents of direct
buffers may reside outside of the normal garbage-collected heap, and so
their impact upon the memory footprint of an application might not be
obvious. It is therefore recommended that direct buffers be allocated
primarily for large, long-lived buffers that are subject to the underlying
system's native I/O operations. In general it is best to allocate direct
buffers only when they yield a measurable gain in program performance.

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

A direct byte buffer may also be created by

mapping

a region of a file
directly into memory. An implementation of the Java platform may optionally
support the creation of direct byte buffers from native code via JNI. If an
instance of one of these kinds of buffers refers to an inaccessible region
of memory then an attempt to access that region will not change the buffer's
content and will cause an unspecified exception to be thrown either at the
time of the access or at some later time.

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

Whether a byte buffer is direct or non-direct may be determined by
invoking its

isDirect

method. This method is provided so
that explicit buffer management can be done in performance-critical code.

Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

---

#### Access to binary data

This class defines methods for reading and writing values of all other
primitive types, except

boolean

. Primitive values are translated
to (or from) sequences of bytes according to the buffer's current byte
order, which may be retrieved and modified via the

order

methods. Specific byte orders are represented by instances of the

ByteOrder

class. The initial order of a byte buffer is always

BIG_ENDIAN

.

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

For access to heterogeneous binary data, that is, sequences of values of
different types, this class defines a family of absolute and relative

get

and

put

methods for each type. For 32-bit floating-point
values, for example, this class defines:

```java
float
getFloat()

float
getFloat(int index)

void
putFloat(float f)

void
putFloat(int index, float f)
```

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

float

getFloat()

float

getFloat(int index)

void

putFloat(float f)

void

putFloat(int index, float f)

Corresponding methods are defined for the types

char,
short, int, long

, and

double

. The index
parameters of the absolute

get

and

put

methods are in terms of
bytes rather than of the type being read or written.

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

For access to homogeneous binary data, that is, sequences of values of
the same type, this class defines methods that can create

views

of a
given byte buffer. A

view buffer

is simply another buffer whose
content is backed by the byte buffer. Changes to the byte buffer's content
will be visible in the view buffer, and vice versa; the two buffers'
position, limit, and mark values are independent. The

asFloatBuffer

method, for example, creates an instance of
the

FloatBuffer

class that is backed by the byte buffer upon which
the method is invoked. Corresponding view-creation methods are defined for
the types

char, short, int, long

, and

double

.

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

View buffers have three important advantages over the families of
type-specific

get

and

put

methods described above:

- A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;
- A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and
- A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;

A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and

A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

A view buffer is indexed not in terms of bytes but rather in terms
of the type-specific size of its values;

A view buffer provides relative bulk

get

and

put

methods that can transfer contiguous sequences of values between a buffer
and an array or some other buffer of the same type; and

A view buffer is potentially much more efficient because it will
be direct if, and only if, its backing byte buffer is direct.

The byte order of a view buffer is fixed to be that of its byte buffer
at the time that the view is created.

---

#### Invocation chaining

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

The sequence of statements

```java
bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);
```

can, for example, be replaced by the single statement

```java
bb.putInt(0xCAFEBABE).putShort(3).putShort(45);
```

bb.putInt(0xCAFEBABE);
bb.putShort(3);
bb.putShort(45);

bb.putInt(0xCAFEBABE).putShort(3).putShort(45);

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

ByteBuffer

alignedSlice

​(int unitSize)

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

int

alignmentOffset

​(int index,
int unitSize)

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

static

ByteBuffer

allocate

​(int capacity)

Allocates a new byte buffer.

static

ByteBuffer

allocateDirect

​(int capacity)

Allocates a new direct byte buffer.

byte[]

array

()

Returns the byte array that backs this
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

asCharBuffer

()

Creates a view of this byte buffer as a char buffer.

abstract

DoubleBuffer

asDoubleBuffer

()

Creates a view of this byte buffer as a double buffer.

abstract

FloatBuffer

asFloatBuffer

()

Creates a view of this byte buffer as a float buffer.

abstract

IntBuffer

asIntBuffer

()

Creates a view of this byte buffer as an int buffer.

abstract

LongBuffer

asLongBuffer

()

Creates a view of this byte buffer as a long buffer.

abstract

ByteBuffer

asReadOnlyBuffer

()

Creates a new, read-only byte buffer that shares this buffer's
content.

abstract

ShortBuffer

asShortBuffer

()

Creates a view of this byte buffer as a short buffer.

abstract

ByteBuffer

compact

()

Compacts this buffer

(optional operation)

.

int

compareTo

​(

ByteBuffer

that)

Compares this buffer to another.

abstract

ByteBuffer

duplicate

()

Creates a new byte buffer that shares this buffer's content.

boolean

equals

​(

Object

ob)

Tells whether or not this buffer is equal to another object.

abstract byte

get

()

Relative

get

method.

ByteBuffer

get

​(byte[] dst)

Relative bulk

get

method.

ByteBuffer

get

​(byte[] dst,
int offset,
int length)

Relative bulk

get

method.

abstract byte

get

​(int index)

Absolute

get

method.

abstract char

getChar

()

Relative

get

method for reading a char value.

abstract char

getChar

​(int index)

Absolute

get

method for reading a char value.

abstract double

getDouble

()

Relative

get

method for reading a double value.

abstract double

getDouble

​(int index)

Absolute

get

method for reading a double value.

abstract float

getFloat

()

Relative

get

method for reading a float value.

abstract float

getFloat

​(int index)

Absolute

get

method for reading a float value.

abstract int

getInt

()

Relative

get

method for reading an int value.

abstract int

getInt

​(int index)

Absolute

get

method for reading an int value.

abstract long

getLong

()

Relative

get

method for reading a long value.

abstract long

getLong

​(int index)

Absolute

get

method for reading a long value.

abstract short

getShort

()

Relative

get

method for reading a short value.

abstract short

getShort

​(int index)

Absolute

get

method for reading a short value.

boolean

hasArray

()

Tells whether or not this buffer is backed by an accessible byte
array.

int

hashCode

()

Returns the current hash code of this buffer.

abstract boolean

isDirect

()

Tells whether or not this byte buffer is direct.

int

mismatch

​(

ByteBuffer

that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

ByteOrder

order

()

Retrieves this buffer's byte order.

ByteBuffer

order

​(

ByteOrder

bo)

Modifies this buffer's byte order.

abstract

ByteBuffer

put

​(byte b)

Relative

put

method

(optional operation)

.

ByteBuffer

put

​(byte[] src)

Relative bulk

put

method

(optional operation)

.

ByteBuffer

put

​(byte[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

abstract

ByteBuffer

put

​(int index,
byte b)

Absolute

put

method

(optional operation)

.

ByteBuffer

put

​(

ByteBuffer

src)

Relative bulk

put

method

(optional operation)

.

abstract

ByteBuffer

putChar

​(char value)

Relative

put

method for writing a char
value

(optional operation)

.

abstract

ByteBuffer

putChar

​(int index,
char value)

Absolute

put

method for writing a char
value

(optional operation)

.

abstract

ByteBuffer

putDouble

​(double value)

Relative

put

method for writing a double
value

(optional operation)

.

abstract

ByteBuffer

putDouble

​(int index,
double value)

Absolute

put

method for writing a double
value

(optional operation)

.

abstract

ByteBuffer

putFloat

​(float value)

Relative

put

method for writing a float
value

(optional operation)

.

abstract

ByteBuffer

putFloat

​(int index,
float value)

Absolute

put

method for writing a float
value

(optional operation)

.

abstract

ByteBuffer

putInt

​(int value)

Relative

put

method for writing an int
value

(optional operation)

.

abstract

ByteBuffer

putInt

​(int index,
int value)

Absolute

put

method for writing an int
value

(optional operation)

.

abstract

ByteBuffer

putLong

​(int index,
long value)

Absolute

put

method for writing a long
value

(optional operation)

.

abstract

ByteBuffer

putLong

​(long value)

Relative

put

method for writing a long
value

(optional operation)

.

abstract

ByteBuffer

putShort

​(int index,
short value)

Absolute

put

method for writing a short
value

(optional operation)

.

abstract

ByteBuffer

putShort

​(short value)

Relative

put

method for writing a short
value

(optional operation)

.

abstract

ByteBuffer

slice

()

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

String

toString

()

Returns a string summarizing the state of this buffer.

static

ByteBuffer

wrap

​(byte[] array)

Wraps a byte array into a buffer.

static

ByteBuffer

wrap

​(byte[] array,
int offset,
int length)

Wraps a byte array into a buffer.

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

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

ByteBuffer

alignedSlice

​(int unitSize)

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

int

alignmentOffset

​(int index,
int unitSize)

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

static

ByteBuffer

allocate

​(int capacity)

Allocates a new byte buffer.

static

ByteBuffer

allocateDirect

​(int capacity)

Allocates a new direct byte buffer.

byte[]

array

()

Returns the byte array that backs this
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

asCharBuffer

()

Creates a view of this byte buffer as a char buffer.

abstract

DoubleBuffer

asDoubleBuffer

()

Creates a view of this byte buffer as a double buffer.

abstract

FloatBuffer

asFloatBuffer

()

Creates a view of this byte buffer as a float buffer.

abstract

IntBuffer

asIntBuffer

()

Creates a view of this byte buffer as an int buffer.

abstract

LongBuffer

asLongBuffer

()

Creates a view of this byte buffer as a long buffer.

abstract

ByteBuffer

asReadOnlyBuffer

()

Creates a new, read-only byte buffer that shares this buffer's
content.

abstract

ShortBuffer

asShortBuffer

()

Creates a view of this byte buffer as a short buffer.

abstract

ByteBuffer

compact

()

Compacts this buffer

(optional operation)

.

int

compareTo

​(

ByteBuffer

that)

Compares this buffer to another.

abstract

ByteBuffer

duplicate

()

Creates a new byte buffer that shares this buffer's content.

boolean

equals

​(

Object

ob)

Tells whether or not this buffer is equal to another object.

abstract byte

get

()

Relative

get

method.

ByteBuffer

get

​(byte[] dst)

Relative bulk

get

method.

ByteBuffer

get

​(byte[] dst,
int offset,
int length)

Relative bulk

get

method.

abstract byte

get

​(int index)

Absolute

get

method.

abstract char

getChar

()

Relative

get

method for reading a char value.

abstract char

getChar

​(int index)

Absolute

get

method for reading a char value.

abstract double

getDouble

()

Relative

get

method for reading a double value.

abstract double

getDouble

​(int index)

Absolute

get

method for reading a double value.

abstract float

getFloat

()

Relative

get

method for reading a float value.

abstract float

getFloat

​(int index)

Absolute

get

method for reading a float value.

abstract int

getInt

()

Relative

get

method for reading an int value.

abstract int

getInt

​(int index)

Absolute

get

method for reading an int value.

abstract long

getLong

()

Relative

get

method for reading a long value.

abstract long

getLong

​(int index)

Absolute

get

method for reading a long value.

abstract short

getShort

()

Relative

get

method for reading a short value.

abstract short

getShort

​(int index)

Absolute

get

method for reading a short value.

boolean

hasArray

()

Tells whether or not this buffer is backed by an accessible byte
array.

int

hashCode

()

Returns the current hash code of this buffer.

abstract boolean

isDirect

()

Tells whether or not this byte buffer is direct.

int

mismatch

​(

ByteBuffer

that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

ByteOrder

order

()

Retrieves this buffer's byte order.

ByteBuffer

order

​(

ByteOrder

bo)

Modifies this buffer's byte order.

abstract

ByteBuffer

put

​(byte b)

Relative

put

method

(optional operation)

.

ByteBuffer

put

​(byte[] src)

Relative bulk

put

method

(optional operation)

.

ByteBuffer

put

​(byte[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

abstract

ByteBuffer

put

​(int index,
byte b)

Absolute

put

method

(optional operation)

.

ByteBuffer

put

​(

ByteBuffer

src)

Relative bulk

put

method

(optional operation)

.

abstract

ByteBuffer

putChar

​(char value)

Relative

put

method for writing a char
value

(optional operation)

.

abstract

ByteBuffer

putChar

​(int index,
char value)

Absolute

put

method for writing a char
value

(optional operation)

.

abstract

ByteBuffer

putDouble

​(double value)

Relative

put

method for writing a double
value

(optional operation)

.

abstract

ByteBuffer

putDouble

​(int index,
double value)

Absolute

put

method for writing a double
value

(optional operation)

.

abstract

ByteBuffer

putFloat

​(float value)

Relative

put

method for writing a float
value

(optional operation)

.

abstract

ByteBuffer

putFloat

​(int index,
float value)

Absolute

put

method for writing a float
value

(optional operation)

.

abstract

ByteBuffer

putInt

​(int value)

Relative

put

method for writing an int
value

(optional operation)

.

abstract

ByteBuffer

putInt

​(int index,
int value)

Absolute

put

method for writing an int
value

(optional operation)

.

abstract

ByteBuffer

putLong

​(int index,
long value)

Absolute

put

method for writing a long
value

(optional operation)

.

abstract

ByteBuffer

putLong

​(long value)

Relative

put

method for writing a long
value

(optional operation)

.

abstract

ByteBuffer

putShort

​(int index,
short value)

Absolute

put

method for writing a short
value

(optional operation)

.

abstract

ByteBuffer

putShort

​(short value)

Relative

put

method for writing a short
value

(optional operation)

.

abstract

ByteBuffer

slice

()

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

String

toString

()

Returns a string summarizing the state of this buffer.

static

ByteBuffer

wrap

​(byte[] array)

Wraps a byte array into a buffer.

static

ByteBuffer

wrap

​(byte[] array,
int offset,
int length)

Wraps a byte array into a buffer.

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

---

#### Method Summary

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

Allocates a new byte buffer.

Allocates a new direct byte buffer.

Returns the byte array that backs this
buffer

(optional operation)

.

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

Creates a view of this byte buffer as a char buffer.

Creates a view of this byte buffer as a double buffer.

Creates a view of this byte buffer as a float buffer.

Creates a view of this byte buffer as an int buffer.

Creates a view of this byte buffer as a long buffer.

Creates a new, read-only byte buffer that shares this buffer's
content.

Creates a view of this byte buffer as a short buffer.

Compacts this buffer

(optional operation)

.

Compares this buffer to another.

Creates a new byte buffer that shares this buffer's content.

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

Relative

get

method for reading a char value.

Absolute

get

method for reading a char value.

Relative

get

method for reading a double value.

Absolute

get

method for reading a double value.

Relative

get

method for reading a float value.

Absolute

get

method for reading a float value.

Relative

get

method for reading an int value.

Absolute

get

method for reading an int value.

Relative

get

method for reading a long value.

Absolute

get

method for reading a long value.

Relative

get

method for reading a short value.

Absolute

get

method for reading a short value.

Tells whether or not this buffer is backed by an accessible byte
array.

Returns the current hash code of this buffer.

Tells whether or not this byte buffer is direct.

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

Retrieves this buffer's byte order.

Modifies this buffer's byte order.

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

Relative

put

method for writing a char
value

(optional operation)

.

Absolute

put

method for writing a char
value

(optional operation)

.

Relative

put

method for writing a double
value

(optional operation)

.

Absolute

put

method for writing a double
value

(optional operation)

.

Relative

put

method for writing a float
value

(optional operation)

.

Absolute

put

method for writing a float
value

(optional operation)

.

Relative

put

method for writing an int
value

(optional operation)

.

Absolute

put

method for writing an int
value

(optional operation)

.

Absolute

put

method for writing a long
value

(optional operation)

.

Relative

put

method for writing a long
value

(optional operation)

.

Absolute

put

method for writing a short
value

(optional operation)

.

Relative

put

method for writing a short
value

(optional operation)

.

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

Returns a string summarizing the state of this buffer.

Wraps a byte array into a buffer.

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

============ METHOD DETAIL ==========

- Method Detail

- allocateDirect

```java
public static
ByteBuffer
allocateDirect​(int capacity)
```

Allocates a new direct byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

. Whether or not it has a

backing array

is unspecified.

**Parameters:** capacity

- The new buffer's capacity, in bytes
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- allocate

```java
public static
ByteBuffer
allocate​(int capacity)
```

Allocates a new byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:** capacity

- The new buffer's capacity, in bytes
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- wrap

```java
public static
ByteBuffer
wrap​(byte[] array,
int offset,
int length)
```

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
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

BIG_ENDIAN

.

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
**Returns:** The new byte buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- wrap

```java
public static
ByteBuffer
wrap​(byte[] array)
```

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:** array

- The array that will back this buffer
**Returns:** The new byte buffer

- slice

```java
public abstract
ByteBuffer
slice()
```

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new byte buffer
**See Also:** alignedSlice(int)

- duplicate

```java
public abstract
ByteBuffer
duplicate()
```

Creates a new byte buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** duplicate

in class

Buffer
**Returns:** The new byte buffer

- asReadOnlyBuffer

```java
public abstract
ByteBuffer
asReadOnlyBuffer()
```

Creates a new, read-only byte buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:** The new, read-only byte buffer

- get

```java
public abstract byte get()
```

Relative

get

method. Reads the byte at this buffer's
current position, and then increments the position.

**Returns:** The byte at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

- put

```java
public abstract
ByteBuffer
put​(byte b)
```

Relative

put

method

(optional operation)

.

Writes the given byte into this buffer at the current
position, and then increments the position.

**Parameters:** b

- The byte to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public abstract byte get​(int index)
```

Absolute

get

method. Reads the byte at the given
index.

**Parameters:** index

- The index from which the byte will be read
**Returns:** The byte at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

- put

```java
public abstract
ByteBuffer
put​(int index,
byte b)
```

Absolute

put

method

(optional operation)

.

Writes the given byte into this buffer at the given
index.

**Parameters:** index

- The index at which the byte will be written
**Parameters:** b

- The byte value to be written
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
ByteBuffer
get​(byte[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
destination array. If there are fewer bytes remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

bytes from this
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

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which bytes are to be written
**Parameters:** offset

- The offset within the array of the first byte to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of bytes to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

bytes
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
ByteBuffer
get​(byte[] dst)
```

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
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

bytes
remaining in this buffer

- put

```java
public
ByteBuffer
put​(
ByteBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the bytes remaining in the given source
buffer into this buffer. If there are more bytes remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no bytes are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

bytes from the given
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

- The source buffer from which bytes are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining bytes in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
ByteBuffer
put​(byte[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers bytes into this buffer from the given
source array. If there are more bytes to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

bytes from the
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

- The array from which bytes are to be read
**Parameters:** offset

- The offset within the array of the first byte to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of bytes to be read from the given array;
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
ByteBuffer
put​(byte[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
byte array into this buffer. An invocation of this method of the
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

- hasArray

```java
public final boolean hasArray()
```

Tells whether or not this buffer is backed by an accessible byte
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
public final byte[] array()
```

Returns the byte array that backs this
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
ByteBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The bytes between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
byte at index

p

=

position()

is copied
to index zero, the byte at index

p

+ 1 is copied
to index one, and so forth until the byte at index

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

The buffer's position is set to the number of bytes copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

Invoke this method after writing data from a buffer in case the
write was incomplete. The following loop, for example, copies bytes
from one channel to another via the buffer

buf

:

```java
buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}
```

**Returns:** This buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- isDirect

```java
public abstract boolean isDirect()
```

Tells whether or not this byte buffer is direct.

**Specified by:** isDirect

in class

Buffer
**Returns:** true

if, and only if, this buffer is direct

- toString

```java
public
String
toString()
```

Returns a string summarizing the state of this buffer.

**Overrides:** toString

in class

Object
**Returns:** A summary string

- hashCode

```java
public int hashCode()
```

Returns the current hash code of this buffer.

The hash code of a byte buffer depends only upon its remaining
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

Two byte buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A byte buffer is not equal to any other type of object.

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
ByteBuffer
that)
```

Compares this buffer to another.

Two byte buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

byte

elements are compared as if by invoking

Byte.compare(byte,byte)

.

A byte buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

ByteBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

- mismatch

```java
public int mismatch​(
ByteBuffer
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

- order

```java
public final
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order is used when reading or writing multibyte values, and
when creating buffers that are views of this byte buffer. The order of
a newly-created byte buffer is always

BIG_ENDIAN

.

**Returns:** This buffer's byte order

- order

```java
public final
ByteBuffer
order​(
ByteOrder
bo)
```

Modifies this buffer's byte order.

**Parameters:** bo

- The new byte order,
either

BIG_ENDIAN

or

LITTLE_ENDIAN
**Returns:** This buffer

- alignmentOffset

```java
public final int alignmentOffset​(int index,
int unitSize)
```

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

A return value greater than zero indicates the address of the byte at
the index is misaligned for the unit size, and the value's quantity
indicates how much the index should be rounded up or down to locate a
byte at an aligned address. Otherwise, a value of

0

indicates
that the address of the byte at the index is aligned for the unit size.

**API Note:** This method may be utilized to determine if unit size bytes from an
index can be accessed atomically, if supported by the native platform.
**Implementation Note:** This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.
**Parameters:** index

- The index to query for alignment offset, must be non-negative, no
upper bounds check is performed
**Parameters:** unitSize

- The unit size in bytes, must be a power of

2
**Returns:** The indexed byte's memory address modulus the unit size
**Throws:** IllegalArgumentException

- If the index is negative or the unit size is not a power of

2
**Throws:** UnsupportedOperationException

- If the native platform does not guarantee stable alignment offset
values for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.
**Since:** 9
**See Also:** alignedSlice(int)

- alignedSlice

```java
public final
ByteBuffer
alignedSlice​(int unitSize)
```

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

The content of the new buffer will start at this buffer's current
position rounded up to the index of the nearest aligned byte for the
given unit size, and end at this buffer's limit rounded down to the index
of the nearest aligned byte for the given unit size.
If rounding results in out-of-bound values then the new buffer's capacity
and limit will be zero. If rounding is within bounds the following
expressions will be true for a new buffer

nb

and unit size

unitSize

:

```java
nb.alignmentOffset(0, unitSize) == 0
nb.alignmentOffset(nb.limit(), unitSize) == 0
```

Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**API Note:** This method may be utilized to create a new buffer where unit size bytes
from index, that is a multiple of the unit size, may be accessed
atomically, if supported by the native platform.
**Implementation Note:** This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.
**Parameters:** unitSize

- The unit size in bytes, must be a power of

2
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the unit size not a power of

2
**Throws:** UnsupportedOperationException

- If the native platform does not guarantee stable aligned slices
for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.
**Since:** 9
**See Also:** alignmentOffset(int, int)

,

slice()

- getChar

```java
public abstract char getChar()
```

Relative

get

method for reading a char value.

Reads the next two bytes at this buffer's current position,
composing them into a char value according to the current byte order,
and then increments the position by two.

**Returns:** The char value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

- putChar

```java
public abstract
ByteBuffer
putChar​(char value)
```

Relative

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:** value

- The char value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getChar

```java
public abstract char getChar​(int index)
```

Absolute

get

method for reading a char value.

Reads two bytes at the given index, composing them into a
char value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The char value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

- putChar

```java
public abstract
ByteBuffer
putChar​(int index,
char value)
```

Absolute

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The char value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asCharBuffer

```java
public abstract
CharBuffer
asCharBuffer()
```

Creates a view of this byte buffer as a char buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new char buffer

- getShort

```java
public abstract short getShort()
```

Relative

get

method for reading a short value.

Reads the next two bytes at this buffer's current position,
composing them into a short value according to the current byte order,
and then increments the position by two.

**Returns:** The short value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

- putShort

```java
public abstract
ByteBuffer
putShort​(short value)
```

Relative

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:** value

- The short value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getShort

```java
public abstract short getShort​(int index)
```

Absolute

get

method for reading a short value.

Reads two bytes at the given index, composing them into a
short value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The short value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

- putShort

```java
public abstract
ByteBuffer
putShort​(int index,
short value)
```

Absolute

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The short value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asShortBuffer

```java
public abstract
ShortBuffer
asShortBuffer()
```

Creates a view of this byte buffer as a short buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new short buffer

- getInt

```java
public abstract int getInt()
```

Relative

get

method for reading an int value.

Reads the next four bytes at this buffer's current position,
composing them into an int value according to the current byte order,
and then increments the position by four.

**Returns:** The int value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

- putInt

```java
public abstract
ByteBuffer
putInt​(int value)
```

Relative

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:** value

- The int value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getInt

```java
public abstract int getInt​(int index)
```

Absolute

get

method for reading an int value.

Reads four bytes at the given index, composing them into a
int value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The int value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

- putInt

```java
public abstract
ByteBuffer
putInt​(int index,
int value)
```

Absolute

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The int value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asIntBuffer

```java
public abstract
IntBuffer
asIntBuffer()
```

Creates a view of this byte buffer as an int buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new int buffer

- getLong

```java
public abstract long getLong()
```

Relative

get

method for reading a long value.

Reads the next eight bytes at this buffer's current position,
composing them into a long value according to the current byte order,
and then increments the position by eight.

**Returns:** The long value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

- putLong

```java
public abstract
ByteBuffer
putLong​(long value)
```

Relative

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:** value

- The long value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getLong

```java
public abstract long getLong​(int index)
```

Absolute

get

method for reading a long value.

Reads eight bytes at the given index, composing them into a
long value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The long value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

- putLong

```java
public abstract
ByteBuffer
putLong​(int index,
long value)
```

Absolute

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The long value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asLongBuffer

```java
public abstract
LongBuffer
asLongBuffer()
```

Creates a view of this byte buffer as a long buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new long buffer

- getFloat

```java
public abstract float getFloat()
```

Relative

get

method for reading a float value.

Reads the next four bytes at this buffer's current position,
composing them into a float value according to the current byte order,
and then increments the position by four.

**Returns:** The float value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

- putFloat

```java
public abstract
ByteBuffer
putFloat​(float value)
```

Relative

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:** value

- The float value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getFloat

```java
public abstract float getFloat​(int index)
```

Absolute

get

method for reading a float value.

Reads four bytes at the given index, composing them into a
float value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The float value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

- putFloat

```java
public abstract
ByteBuffer
putFloat​(int index,
float value)
```

Absolute

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The float value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asFloatBuffer

```java
public abstract
FloatBuffer
asFloatBuffer()
```

Creates a view of this byte buffer as a float buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new float buffer

- getDouble

```java
public abstract double getDouble()
```

Relative

get

method for reading a double value.

Reads the next eight bytes at this buffer's current position,
composing them into a double value according to the current byte order,
and then increments the position by eight.

**Returns:** The double value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

- putDouble

```java
public abstract
ByteBuffer
putDouble​(double value)
```

Relative

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:** value

- The double value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getDouble

```java
public abstract double getDouble​(int index)
```

Absolute

get

method for reading a double value.

Reads eight bytes at the given index, composing them into a
double value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The double value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

- putDouble

```java
public abstract
ByteBuffer
putDouble​(int index,
double value)
```

Absolute

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The double value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asDoubleBuffer

```java
public abstract
DoubleBuffer
asDoubleBuffer()
```

Creates a view of this byte buffer as a double buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new double buffer

Method Detail

- allocateDirect

```java
public static
ByteBuffer
allocateDirect​(int capacity)
```

Allocates a new direct byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

. Whether or not it has a

backing array

is unspecified.

**Parameters:** capacity

- The new buffer's capacity, in bytes
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- allocate

```java
public static
ByteBuffer
allocate​(int capacity)
```

Allocates a new byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:** capacity

- The new buffer's capacity, in bytes
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- wrap

```java
public static
ByteBuffer
wrap​(byte[] array,
int offset,
int length)
```

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
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

BIG_ENDIAN

.

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
**Returns:** The new byte buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- wrap

```java
public static
ByteBuffer
wrap​(byte[] array)
```

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:** array

- The array that will back this buffer
**Returns:** The new byte buffer

- slice

```java
public abstract
ByteBuffer
slice()
```

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new byte buffer
**See Also:** alignedSlice(int)

- duplicate

```java
public abstract
ByteBuffer
duplicate()
```

Creates a new byte buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** duplicate

in class

Buffer
**Returns:** The new byte buffer

- asReadOnlyBuffer

```java
public abstract
ByteBuffer
asReadOnlyBuffer()
```

Creates a new, read-only byte buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:** The new, read-only byte buffer

- get

```java
public abstract byte get()
```

Relative

get

method. Reads the byte at this buffer's
current position, and then increments the position.

**Returns:** The byte at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

- put

```java
public abstract
ByteBuffer
put​(byte b)
```

Relative

put

method

(optional operation)

.

Writes the given byte into this buffer at the current
position, and then increments the position.

**Parameters:** b

- The byte to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public abstract byte get​(int index)
```

Absolute

get

method. Reads the byte at the given
index.

**Parameters:** index

- The index from which the byte will be read
**Returns:** The byte at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

- put

```java
public abstract
ByteBuffer
put​(int index,
byte b)
```

Absolute

put

method

(optional operation)

.

Writes the given byte into this buffer at the given
index.

**Parameters:** index

- The index at which the byte will be written
**Parameters:** b

- The byte value to be written
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
ByteBuffer
get​(byte[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
destination array. If there are fewer bytes remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

bytes from this
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

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which bytes are to be written
**Parameters:** offset

- The offset within the array of the first byte to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of bytes to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

bytes
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
ByteBuffer
get​(byte[] dst)
```

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
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

bytes
remaining in this buffer

- put

```java
public
ByteBuffer
put​(
ByteBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the bytes remaining in the given source
buffer into this buffer. If there are more bytes remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no bytes are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

bytes from the given
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

- The source buffer from which bytes are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining bytes in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
ByteBuffer
put​(byte[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers bytes into this buffer from the given
source array. If there are more bytes to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

bytes from the
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

- The array from which bytes are to be read
**Parameters:** offset

- The offset within the array of the first byte to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of bytes to be read from the given array;
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
ByteBuffer
put​(byte[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
byte array into this buffer. An invocation of this method of the
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

- hasArray

```java
public final boolean hasArray()
```

Tells whether or not this buffer is backed by an accessible byte
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
public final byte[] array()
```

Returns the byte array that backs this
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
ByteBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The bytes between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
byte at index

p

=

position()

is copied
to index zero, the byte at index

p

+ 1 is copied
to index one, and so forth until the byte at index

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

The buffer's position is set to the number of bytes copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

Invoke this method after writing data from a buffer in case the
write was incomplete. The following loop, for example, copies bytes
from one channel to another via the buffer

buf

:

```java
buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}
```

**Returns:** This buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- isDirect

```java
public abstract boolean isDirect()
```

Tells whether or not this byte buffer is direct.

**Specified by:** isDirect

in class

Buffer
**Returns:** true

if, and only if, this buffer is direct

- toString

```java
public
String
toString()
```

Returns a string summarizing the state of this buffer.

**Overrides:** toString

in class

Object
**Returns:** A summary string

- hashCode

```java
public int hashCode()
```

Returns the current hash code of this buffer.

The hash code of a byte buffer depends only upon its remaining
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

Two byte buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A byte buffer is not equal to any other type of object.

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
ByteBuffer
that)
```

Compares this buffer to another.

Two byte buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

byte

elements are compared as if by invoking

Byte.compare(byte,byte)

.

A byte buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

ByteBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

- mismatch

```java
public int mismatch​(
ByteBuffer
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

- order

```java
public final
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order is used when reading or writing multibyte values, and
when creating buffers that are views of this byte buffer. The order of
a newly-created byte buffer is always

BIG_ENDIAN

.

**Returns:** This buffer's byte order

- order

```java
public final
ByteBuffer
order​(
ByteOrder
bo)
```

Modifies this buffer's byte order.

**Parameters:** bo

- The new byte order,
either

BIG_ENDIAN

or

LITTLE_ENDIAN
**Returns:** This buffer

- alignmentOffset

```java
public final int alignmentOffset​(int index,
int unitSize)
```

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

A return value greater than zero indicates the address of the byte at
the index is misaligned for the unit size, and the value's quantity
indicates how much the index should be rounded up or down to locate a
byte at an aligned address. Otherwise, a value of

0

indicates
that the address of the byte at the index is aligned for the unit size.

**API Note:** This method may be utilized to determine if unit size bytes from an
index can be accessed atomically, if supported by the native platform.
**Implementation Note:** This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.
**Parameters:** index

- The index to query for alignment offset, must be non-negative, no
upper bounds check is performed
**Parameters:** unitSize

- The unit size in bytes, must be a power of

2
**Returns:** The indexed byte's memory address modulus the unit size
**Throws:** IllegalArgumentException

- If the index is negative or the unit size is not a power of

2
**Throws:** UnsupportedOperationException

- If the native platform does not guarantee stable alignment offset
values for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.
**Since:** 9
**See Also:** alignedSlice(int)

- alignedSlice

```java
public final
ByteBuffer
alignedSlice​(int unitSize)
```

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

The content of the new buffer will start at this buffer's current
position rounded up to the index of the nearest aligned byte for the
given unit size, and end at this buffer's limit rounded down to the index
of the nearest aligned byte for the given unit size.
If rounding results in out-of-bound values then the new buffer's capacity
and limit will be zero. If rounding is within bounds the following
expressions will be true for a new buffer

nb

and unit size

unitSize

:

```java
nb.alignmentOffset(0, unitSize) == 0
nb.alignmentOffset(nb.limit(), unitSize) == 0
```

Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**API Note:** This method may be utilized to create a new buffer where unit size bytes
from index, that is a multiple of the unit size, may be accessed
atomically, if supported by the native platform.
**Implementation Note:** This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.
**Parameters:** unitSize

- The unit size in bytes, must be a power of

2
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the unit size not a power of

2
**Throws:** UnsupportedOperationException

- If the native platform does not guarantee stable aligned slices
for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.
**Since:** 9
**See Also:** alignmentOffset(int, int)

,

slice()

- getChar

```java
public abstract char getChar()
```

Relative

get

method for reading a char value.

Reads the next two bytes at this buffer's current position,
composing them into a char value according to the current byte order,
and then increments the position by two.

**Returns:** The char value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

- putChar

```java
public abstract
ByteBuffer
putChar​(char value)
```

Relative

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:** value

- The char value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getChar

```java
public abstract char getChar​(int index)
```

Absolute

get

method for reading a char value.

Reads two bytes at the given index, composing them into a
char value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The char value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

- putChar

```java
public abstract
ByteBuffer
putChar​(int index,
char value)
```

Absolute

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The char value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asCharBuffer

```java
public abstract
CharBuffer
asCharBuffer()
```

Creates a view of this byte buffer as a char buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new char buffer

- getShort

```java
public abstract short getShort()
```

Relative

get

method for reading a short value.

Reads the next two bytes at this buffer's current position,
composing them into a short value according to the current byte order,
and then increments the position by two.

**Returns:** The short value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

- putShort

```java
public abstract
ByteBuffer
putShort​(short value)
```

Relative

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:** value

- The short value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getShort

```java
public abstract short getShort​(int index)
```

Absolute

get

method for reading a short value.

Reads two bytes at the given index, composing them into a
short value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The short value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

- putShort

```java
public abstract
ByteBuffer
putShort​(int index,
short value)
```

Absolute

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The short value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asShortBuffer

```java
public abstract
ShortBuffer
asShortBuffer()
```

Creates a view of this byte buffer as a short buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new short buffer

- getInt

```java
public abstract int getInt()
```

Relative

get

method for reading an int value.

Reads the next four bytes at this buffer's current position,
composing them into an int value according to the current byte order,
and then increments the position by four.

**Returns:** The int value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

- putInt

```java
public abstract
ByteBuffer
putInt​(int value)
```

Relative

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:** value

- The int value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getInt

```java
public abstract int getInt​(int index)
```

Absolute

get

method for reading an int value.

Reads four bytes at the given index, composing them into a
int value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The int value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

- putInt

```java
public abstract
ByteBuffer
putInt​(int index,
int value)
```

Absolute

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The int value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asIntBuffer

```java
public abstract
IntBuffer
asIntBuffer()
```

Creates a view of this byte buffer as an int buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new int buffer

- getLong

```java
public abstract long getLong()
```

Relative

get

method for reading a long value.

Reads the next eight bytes at this buffer's current position,
composing them into a long value according to the current byte order,
and then increments the position by eight.

**Returns:** The long value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

- putLong

```java
public abstract
ByteBuffer
putLong​(long value)
```

Relative

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:** value

- The long value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getLong

```java
public abstract long getLong​(int index)
```

Absolute

get

method for reading a long value.

Reads eight bytes at the given index, composing them into a
long value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The long value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

- putLong

```java
public abstract
ByteBuffer
putLong​(int index,
long value)
```

Absolute

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The long value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asLongBuffer

```java
public abstract
LongBuffer
asLongBuffer()
```

Creates a view of this byte buffer as a long buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new long buffer

- getFloat

```java
public abstract float getFloat()
```

Relative

get

method for reading a float value.

Reads the next four bytes at this buffer's current position,
composing them into a float value according to the current byte order,
and then increments the position by four.

**Returns:** The float value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

- putFloat

```java
public abstract
ByteBuffer
putFloat​(float value)
```

Relative

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:** value

- The float value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getFloat

```java
public abstract float getFloat​(int index)
```

Absolute

get

method for reading a float value.

Reads four bytes at the given index, composing them into a
float value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The float value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

- putFloat

```java
public abstract
ByteBuffer
putFloat​(int index,
float value)
```

Absolute

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The float value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asFloatBuffer

```java
public abstract
FloatBuffer
asFloatBuffer()
```

Creates a view of this byte buffer as a float buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new float buffer

- getDouble

```java
public abstract double getDouble()
```

Relative

get

method for reading a double value.

Reads the next eight bytes at this buffer's current position,
composing them into a double value according to the current byte order,
and then increments the position by eight.

**Returns:** The double value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

- putDouble

```java
public abstract
ByteBuffer
putDouble​(double value)
```

Relative

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:** value

- The double value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- getDouble

```java
public abstract double getDouble​(int index)
```

Absolute

get

method for reading a double value.

Reads eight bytes at the given index, composing them into a
double value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The double value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

- putDouble

```java
public abstract
ByteBuffer
putDouble​(int index,
double value)
```

Absolute

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The double value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- asDoubleBuffer

```java
public abstract
DoubleBuffer
asDoubleBuffer()
```

Creates a view of this byte buffer as a double buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new double buffer

---

#### Method Detail

allocateDirect

```java
public static
ByteBuffer
allocateDirect​(int capacity)
```

Allocates a new direct byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

. Whether or not it has a

backing array

is unspecified.

**Parameters:** capacity

- The new buffer's capacity, in bytes
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

---

#### allocateDirect

public static

ByteBuffer

allocateDirect​(int capacity)

Allocates a new direct byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

. Whether or not it has a

backing array

is unspecified.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

. Whether or not it has a

backing array

is unspecified.

allocate

```java
public static
ByteBuffer
allocate​(int capacity)
```

Allocates a new byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

.

It will have a

backing array

, and its

array offset

will be zero.

**Parameters:** capacity

- The new buffer's capacity, in bytes
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

---

#### allocate

public static

ByteBuffer

allocate​(int capacity)

Allocates a new byte buffer.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

.

It will have a

backing array

, and its

array offset

will be zero.

The new buffer's position will be zero, its limit will be its
capacity, its mark will be undefined, each of its elements will be
initialized to zero, and its byte order will be

BIG_ENDIAN

.

It will have a

backing array

, and its

array offset

will be zero.

wrap

```java
public static
ByteBuffer
wrap​(byte[] array,
int offset,
int length)
```

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
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

BIG_ENDIAN

.

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
**Returns:** The new byte buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### wrap

public static

ByteBuffer

wrap​(byte[] array,
int offset,
int length)

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
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

BIG_ENDIAN

.

Its

backing array

will be the given array, and
its

array offset

will be zero.

The new buffer will be backed by the given byte array;
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

BIG_ENDIAN

.

Its

backing array

will be the given array, and
its

array offset

will be zero.

wrap

```java
public static
ByteBuffer
wrap​(byte[] array)
```

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

Its

backing array

will be the given array, and its

array offset

will be zero.

**Parameters:** array

- The array that will back this buffer
**Returns:** The new byte buffer

---

#### wrap

public static

ByteBuffer

wrap​(byte[] array)

Wraps a byte array into a buffer.

The new buffer will be backed by the given byte array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

Its

backing array

will be the given array, and its

array offset

will be zero.

The new buffer will be backed by the given byte array;
that is, modifications to the buffer will cause the array to be modified
and vice versa. The new buffer's capacity and limit will be

array.length

, its position will be zero, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

Its

backing array

will be the given array, and its

array offset

will be zero.

slice

```java
public abstract
ByteBuffer
slice()
```

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new byte buffer
**See Also:** alignedSlice(int)

---

#### slice

public abstract

ByteBuffer

slice()

Creates a new byte buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer, its mark will be
undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

duplicate

```java
public abstract
ByteBuffer
duplicate()
```

Creates a new byte buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** duplicate

in class

Buffer
**Returns:** The new byte buffer

---

#### duplicate

public abstract

ByteBuffer

duplicate()

Creates a new byte buffer that shares this buffer's content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer, and vice
versa; the two buffers' position, limit, and mark values will be
independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

asReadOnlyBuffer

```java
public abstract
ByteBuffer
asReadOnlyBuffer()
```

Creates a new, read-only byte buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

**Returns:** The new, read-only byte buffer

---

#### asReadOnlyBuffer

public abstract

ByteBuffer

asReadOnlyBuffer()

Creates a new, read-only byte buffer that shares this buffer's
content.

The content of the new buffer will be that of this buffer. Changes
to this buffer's content will be visible in the new buffer; the new
buffer itself, however, will be read-only and will not allow the shared
content to be modified. The two buffers' position, limit, and mark
values will be independent.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

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

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

If this buffer is itself read-only then this method behaves in
exactly the same way as the

duplicate

method.

The new buffer's capacity, limit, position,

and mark values will be identical to those of this buffer, and its byte
order will be

BIG_ENDIAN

.

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
public abstract byte get()
```

Relative

get

method. Reads the byte at this buffer's
current position, and then increments the position.

**Returns:** The byte at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

---

#### get

public abstract byte get()

Relative

get

method. Reads the byte at this buffer's
current position, and then increments the position.

put

```java
public abstract
ByteBuffer
put​(byte b)
```

Relative

put

method

(optional operation)

.

Writes the given byte into this buffer at the current
position, and then increments the position.

**Parameters:** b

- The byte to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public abstract

ByteBuffer

put​(byte b)

Relative

put

method

(optional operation)

.

Writes the given byte into this buffer at the current
position, and then increments the position.

Writes the given byte into this buffer at the current
position, and then increments the position.

get

```java
public abstract byte get​(int index)
```

Absolute

get

method. Reads the byte at the given
index.

**Parameters:** index

- The index from which the byte will be read
**Returns:** The byte at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

---

#### get

public abstract byte get​(int index)

Absolute

get

method. Reads the byte at the given
index.

put

```java
public abstract
ByteBuffer
put​(int index,
byte b)
```

Absolute

put

method

(optional operation)

.

Writes the given byte into this buffer at the given
index.

**Parameters:** index

- The index at which the byte will be written
**Parameters:** b

- The byte value to be written
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

ByteBuffer

put​(int index,
byte b)

Absolute

put

method

(optional operation)

.

Writes the given byte into this buffer at the given
index.

Writes the given byte into this buffer at the given
index.

get

```java
public
ByteBuffer
get​(byte[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
destination array. If there are fewer bytes remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

bytes from this
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

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which bytes are to be written
**Parameters:** offset

- The offset within the array of the first byte to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of bytes to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

bytes
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

ByteBuffer

get​(byte[] dst,
int offset,
int length)

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
destination array. If there are fewer bytes remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

bytes from this
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

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

This method transfers bytes from this buffer into the given
destination array. If there are fewer bytes remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

bytes from this
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

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

Otherwise, this method copies

length

bytes from this
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

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient bytes in
this buffer and it is potentially much more efficient.

for (int i = off; i < off + len; i++)
dst[i] = src.get();

get

```java
public
ByteBuffer
get​(byte[] dst)
```

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
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

bytes
remaining in this buffer

---

#### get

public

ByteBuffer

get​(byte[] dst)

Relative bulk

get

method.

This method transfers bytes from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

This method transfers bytes from this buffer into the given
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
ByteBuffer
put​(
ByteBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the bytes remaining in the given source
buffer into this buffer. If there are more bytes remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no bytes are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

bytes from the given
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

- The source buffer from which bytes are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining bytes in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public

ByteBuffer

put​(

ByteBuffer

src)

Relative bulk

put

method

(optional operation)

.

This method transfers the bytes remaining in the given source
buffer into this buffer. If there are more bytes remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no bytes are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

bytes from the given
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

This method transfers the bytes remaining in the given source
buffer into this buffer. If there are more bytes remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no bytes are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

bytes from the given
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

bytes from the given
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
ByteBuffer
put​(byte[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers bytes into this buffer from the given
source array. If there are more bytes to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

bytes from the
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

- The array from which bytes are to be read
**Parameters:** offset

- The offset within the array of the first byte to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of bytes to be read from the given array;
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

ByteBuffer

put​(byte[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

This method transfers bytes into this buffer from the given
source array. If there are more bytes to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

bytes from the
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

This method transfers bytes into this buffer from the given
source array. If there are more bytes to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
bytes are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

bytes from the
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

bytes from the
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
ByteBuffer
put​(byte[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
byte array into this buffer. An invocation of this method of the
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

ByteBuffer

put​(byte[] src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
byte array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

This method transfers the entire content of the given source
byte array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

dst.put(a, 0, a.length)

hasArray

```java
public final boolean hasArray()
```

Tells whether or not this buffer is backed by an accessible byte
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

Tells whether or not this buffer is backed by an accessible byte
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
public final byte[] array()
```

Returns the byte array that backs this
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

public final byte[] array()

Returns the byte array that backs this
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
ByteBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The bytes between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
byte at index

p

=

position()

is copied
to index zero, the byte at index

p

+ 1 is copied
to index one, and so forth until the byte at index

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

The buffer's position is set to the number of bytes copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

Invoke this method after writing data from a buffer in case the
write was incomplete. The following loop, for example, copies bytes
from one channel to another via the buffer

buf

:

```java
buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}
```

**Returns:** This buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### compact

public abstract

ByteBuffer

compact()

Compacts this buffer

(optional operation)

.

The bytes between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
byte at index

p

=

position()

is copied
to index zero, the byte at index

p

+ 1 is copied
to index one, and so forth until the byte at index

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

The buffer's position is set to the number of bytes copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

Invoke this method after writing data from a buffer in case the
write was incomplete. The following loop, for example, copies bytes
from one channel to another via the buffer

buf

:

```java
buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}
```

The bytes between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
byte at index

p

=

position()

is copied
to index zero, the byte at index

p

+ 1 is copied
to index one, and so forth until the byte at index

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

The buffer's position is set to the number of bytes copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

Invoke this method after writing data from a buffer in case the
write was incomplete. The following loop, for example, copies bytes
from one channel to another via the buffer

buf

:

```java
buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}
```

The buffer's position is set to the number of bytes copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

Invoke this method after writing data from a buffer in case the
write was incomplete. The following loop, for example, copies bytes
from one channel to another via the buffer

buf

:

```java
buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}
```

buf.clear(); // Prepare buffer for use
while (in.read(buf) >= 0 || buf.position != 0) {
buf.flip();
out.write(buf);
buf.compact(); // In case of partial write
}

isDirect

```java
public abstract boolean isDirect()
```

Tells whether or not this byte buffer is direct.

**Specified by:** isDirect

in class

Buffer
**Returns:** true

if, and only if, this buffer is direct

---

#### isDirect

public abstract boolean isDirect()

Tells whether or not this byte buffer is direct.

toString

```java
public
String
toString()
```

Returns a string summarizing the state of this buffer.

**Overrides:** toString

in class

Object
**Returns:** A summary string

---

#### toString

public

String

toString()

Returns a string summarizing the state of this buffer.

hashCode

```java
public int hashCode()
```

Returns the current hash code of this buffer.

The hash code of a byte buffer depends only upon its remaining
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

The hash code of a byte buffer depends only upon its remaining
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

The hash code of a byte buffer depends only upon its remaining
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

Two byte buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A byte buffer is not equal to any other type of object.

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

Two byte buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A byte buffer is not equal to any other type of object.

Two byte buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A byte buffer is not equal to any other type of object.

They have the same element type,

They have the same number of remaining elements, and

The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

They have the same element type,

They have the same number of remaining elements, and

The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

A byte buffer is not equal to any other type of object.

compareTo

```java
public int compareTo​(
ByteBuffer
that)
```

Compares this buffer to another.

Two byte buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

byte

elements are compared as if by invoking

Byte.compare(byte,byte)

.

A byte buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

ByteBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

---

#### compareTo

public int compareTo​(

ByteBuffer

that)

Compares this buffer to another.

Two byte buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

byte

elements are compared as if by invoking

Byte.compare(byte,byte)

.

A byte buffer is not comparable to any other type of object.

Two byte buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

byte

elements are compared as if by invoking

Byte.compare(byte,byte)

.

A byte buffer is not comparable to any other type of object.

A byte buffer is not comparable to any other type of object.

mismatch

```java
public int mismatch​(
ByteBuffer
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

ByteBuffer

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

order

```java
public final
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order is used when reading or writing multibyte values, and
when creating buffers that are views of this byte buffer. The order of
a newly-created byte buffer is always

BIG_ENDIAN

.

**Returns:** This buffer's byte order

---

#### order

public final

ByteOrder

order()

Retrieves this buffer's byte order.

The byte order is used when reading or writing multibyte values, and
when creating buffers that are views of this byte buffer. The order of
a newly-created byte buffer is always

BIG_ENDIAN

.

The byte order is used when reading or writing multibyte values, and
when creating buffers that are views of this byte buffer. The order of
a newly-created byte buffer is always

BIG_ENDIAN

.

order

```java
public final
ByteBuffer
order​(
ByteOrder
bo)
```

Modifies this buffer's byte order.

**Parameters:** bo

- The new byte order,
either

BIG_ENDIAN

or

LITTLE_ENDIAN
**Returns:** This buffer

---

#### order

public final

ByteBuffer

order​(

ByteOrder

bo)

Modifies this buffer's byte order.

alignmentOffset

```java
public final int alignmentOffset​(int index,
int unitSize)
```

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

A return value greater than zero indicates the address of the byte at
the index is misaligned for the unit size, and the value's quantity
indicates how much the index should be rounded up or down to locate a
byte at an aligned address. Otherwise, a value of

0

indicates
that the address of the byte at the index is aligned for the unit size.

**API Note:** This method may be utilized to determine if unit size bytes from an
index can be accessed atomically, if supported by the native platform.
**Implementation Note:** This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.
**Parameters:** index

- The index to query for alignment offset, must be non-negative, no
upper bounds check is performed
**Parameters:** unitSize

- The unit size in bytes, must be a power of

2
**Returns:** The indexed byte's memory address modulus the unit size
**Throws:** IllegalArgumentException

- If the index is negative or the unit size is not a power of

2
**Throws:** UnsupportedOperationException

- If the native platform does not guarantee stable alignment offset
values for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.
**Since:** 9
**See Also:** alignedSlice(int)

---

#### alignmentOffset

public final int alignmentOffset​(int index,
int unitSize)

Returns the memory address, pointing to the byte at the given index,
modulus the given unit size.

A return value greater than zero indicates the address of the byte at
the index is misaligned for the unit size, and the value's quantity
indicates how much the index should be rounded up or down to locate a
byte at an aligned address. Otherwise, a value of

0

indicates
that the address of the byte at the index is aligned for the unit size.

A return value greater than zero indicates the address of the byte at
the index is misaligned for the unit size, and the value's quantity
indicates how much the index should be rounded up or down to locate a
byte at an aligned address. Otherwise, a value of

0

indicates
that the address of the byte at the index is aligned for the unit size.

alignedSlice

```java
public final
ByteBuffer
alignedSlice​(int unitSize)
```

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

The content of the new buffer will start at this buffer's current
position rounded up to the index of the nearest aligned byte for the
given unit size, and end at this buffer's limit rounded down to the index
of the nearest aligned byte for the given unit size.
If rounding results in out-of-bound values then the new buffer's capacity
and limit will be zero. If rounding is within bounds the following
expressions will be true for a new buffer

nb

and unit size

unitSize

:

```java
nb.alignmentOffset(0, unitSize) == 0
nb.alignmentOffset(nb.limit(), unitSize) == 0
```

Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**API Note:** This method may be utilized to create a new buffer where unit size bytes
from index, that is a multiple of the unit size, may be accessed
atomically, if supported by the native platform.
**Implementation Note:** This implementation throws

UnsupportedOperationException

for
non-direct buffers when the given unit size is greater then

8

.
**Parameters:** unitSize

- The unit size in bytes, must be a power of

2
**Returns:** The new byte buffer
**Throws:** IllegalArgumentException

- If the unit size not a power of

2
**Throws:** UnsupportedOperationException

- If the native platform does not guarantee stable aligned slices
for the given unit size when managing the memory regions
of buffers of the same kind as this buffer (direct or
non-direct). For example, if garbage collection would result
in the moving of a memory region covered by a non-direct buffer
from one location to another and both locations have different
alignment characteristics.
**Since:** 9
**See Also:** alignmentOffset(int, int)

,

slice()

---

#### alignedSlice

public final

ByteBuffer

alignedSlice​(int unitSize)

Creates a new byte buffer whose content is a shared and aligned
subsequence of this buffer's content.

The content of the new buffer will start at this buffer's current
position rounded up to the index of the nearest aligned byte for the
given unit size, and end at this buffer's limit rounded down to the index
of the nearest aligned byte for the given unit size.
If rounding results in out-of-bound values then the new buffer's capacity
and limit will be zero. If rounding is within bounds the following
expressions will be true for a new buffer

nb

and unit size

unitSize

:

```java
nb.alignmentOffset(0, unitSize) == 0
nb.alignmentOffset(nb.limit(), unitSize) == 0
```

Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position rounded up to the index of the nearest aligned byte for the
given unit size, and end at this buffer's limit rounded down to the index
of the nearest aligned byte for the given unit size.
If rounding results in out-of-bound values then the new buffer's capacity
and limit will be zero. If rounding is within bounds the following
expressions will be true for a new buffer

nb

and unit size

unitSize

:

```java
nb.alignmentOffset(0, unitSize) == 0
nb.alignmentOffset(nb.limit(), unitSize) == 0
```

Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

nb.alignmentOffset(0, unitSize) == 0
nb.alignmentOffset(nb.limit(), unitSize) == 0

Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer or fewer subject to
alignment, its mark will be undefined, and its byte order will be

BIG_ENDIAN

.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

getChar

```java
public abstract char getChar()
```

Relative

get

method for reading a char value.

Reads the next two bytes at this buffer's current position,
composing them into a char value according to the current byte order,
and then increments the position by two.

**Returns:** The char value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

---

#### getChar

public abstract char getChar()

Relative

get

method for reading a char value.

Reads the next two bytes at this buffer's current position,
composing them into a char value according to the current byte order,
and then increments the position by two.

Reads the next two bytes at this buffer's current position,
composing them into a char value according to the current byte order,
and then increments the position by two.

putChar

```java
public abstract
ByteBuffer
putChar​(char value)
```

Relative

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:** value

- The char value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putChar

public abstract

ByteBuffer

putChar​(char value)

Relative

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

getChar

```java
public abstract char getChar​(int index)
```

Absolute

get

method for reading a char value.

Reads two bytes at the given index, composing them into a
char value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The char value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

---

#### getChar

public abstract char getChar​(int index)

Absolute

get

method for reading a char value.

Reads two bytes at the given index, composing them into a
char value according to the current byte order.

Reads two bytes at the given index, composing them into a
char value according to the current byte order.

putChar

```java
public abstract
ByteBuffer
putChar​(int index,
char value)
```

Absolute

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The char value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putChar

public abstract

ByteBuffer

putChar​(int index,
char value)

Absolute

put

method for writing a char
value

(optional operation)

.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the given index.

Writes two bytes containing the given char value, in the
current byte order, into this buffer at the given index.

asCharBuffer

```java
public abstract
CharBuffer
asCharBuffer()
```

Creates a view of this byte buffer as a char buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new char buffer

---

#### asCharBuffer

public abstract

CharBuffer

asCharBuffer()

Creates a view of this byte buffer as a char buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

getShort

```java
public abstract short getShort()
```

Relative

get

method for reading a short value.

Reads the next two bytes at this buffer's current position,
composing them into a short value according to the current byte order,
and then increments the position by two.

**Returns:** The short value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than two bytes
remaining in this buffer

---

#### getShort

public abstract short getShort()

Relative

get

method for reading a short value.

Reads the next two bytes at this buffer's current position,
composing them into a short value according to the current byte order,
and then increments the position by two.

Reads the next two bytes at this buffer's current position,
composing them into a short value according to the current byte order,
and then increments the position by two.

putShort

```java
public abstract
ByteBuffer
putShort​(short value)
```

Relative

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

**Parameters:** value

- The short value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than two bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putShort

public abstract

ByteBuffer

putShort​(short value)

Relative

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the current position, and then
increments the position by two.

getShort

```java
public abstract short getShort​(int index)
```

Absolute

get

method for reading a short value.

Reads two bytes at the given index, composing them into a
short value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The short value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one

---

#### getShort

public abstract short getShort​(int index)

Absolute

get

method for reading a short value.

Reads two bytes at the given index, composing them into a
short value according to the current byte order.

Reads two bytes at the given index, composing them into a
short value according to the current byte order.

putShort

```java
public abstract
ByteBuffer
putShort​(int index,
short value)
```

Absolute

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The short value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus one
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putShort

public abstract

ByteBuffer

putShort​(int index,
short value)

Absolute

put

method for writing a short
value

(optional operation)

.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the given index.

Writes two bytes containing the given short value, in the
current byte order, into this buffer at the given index.

asShortBuffer

```java
public abstract
ShortBuffer
asShortBuffer()
```

Creates a view of this byte buffer as a short buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new short buffer

---

#### asShortBuffer

public abstract

ShortBuffer

asShortBuffer()

Creates a view of this byte buffer as a short buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
two, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

getInt

```java
public abstract int getInt()
```

Relative

get

method for reading an int value.

Reads the next four bytes at this buffer's current position,
composing them into an int value according to the current byte order,
and then increments the position by four.

**Returns:** The int value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

---

#### getInt

public abstract int getInt()

Relative

get

method for reading an int value.

Reads the next four bytes at this buffer's current position,
composing them into an int value according to the current byte order,
and then increments the position by four.

Reads the next four bytes at this buffer's current position,
composing them into an int value according to the current byte order,
and then increments the position by four.

putInt

```java
public abstract
ByteBuffer
putInt​(int value)
```

Relative

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:** value

- The int value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putInt

public abstract

ByteBuffer

putInt​(int value)

Relative

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

getInt

```java
public abstract int getInt​(int index)
```

Absolute

get

method for reading an int value.

Reads four bytes at the given index, composing them into a
int value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The int value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

---

#### getInt

public abstract int getInt​(int index)

Absolute

get

method for reading an int value.

Reads four bytes at the given index, composing them into a
int value according to the current byte order.

Reads four bytes at the given index, composing them into a
int value according to the current byte order.

putInt

```java
public abstract
ByteBuffer
putInt​(int index,
int value)
```

Absolute

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The int value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putInt

public abstract

ByteBuffer

putInt​(int index,
int value)

Absolute

put

method for writing an int
value

(optional operation)

.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the given index.

Writes four bytes containing the given int value, in the
current byte order, into this buffer at the given index.

asIntBuffer

```java
public abstract
IntBuffer
asIntBuffer()
```

Creates a view of this byte buffer as an int buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new int buffer

---

#### asIntBuffer

public abstract

IntBuffer

asIntBuffer()

Creates a view of this byte buffer as an int buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

getLong

```java
public abstract long getLong()
```

Relative

get

method for reading a long value.

Reads the next eight bytes at this buffer's current position,
composing them into a long value according to the current byte order,
and then increments the position by eight.

**Returns:** The long value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

---

#### getLong

public abstract long getLong()

Relative

get

method for reading a long value.

Reads the next eight bytes at this buffer's current position,
composing them into a long value according to the current byte order,
and then increments the position by eight.

Reads the next eight bytes at this buffer's current position,
composing them into a long value according to the current byte order,
and then increments the position by eight.

putLong

```java
public abstract
ByteBuffer
putLong​(long value)
```

Relative

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:** value

- The long value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putLong

public abstract

ByteBuffer

putLong​(long value)

Relative

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

getLong

```java
public abstract long getLong​(int index)
```

Absolute

get

method for reading a long value.

Reads eight bytes at the given index, composing them into a
long value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The long value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

---

#### getLong

public abstract long getLong​(int index)

Absolute

get

method for reading a long value.

Reads eight bytes at the given index, composing them into a
long value according to the current byte order.

Reads eight bytes at the given index, composing them into a
long value according to the current byte order.

putLong

```java
public abstract
ByteBuffer
putLong​(int index,
long value)
```

Absolute

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The long value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putLong

public abstract

ByteBuffer

putLong​(int index,
long value)

Absolute

put

method for writing a long
value

(optional operation)

.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the given index.

Writes eight bytes containing the given long value, in the
current byte order, into this buffer at the given index.

asLongBuffer

```java
public abstract
LongBuffer
asLongBuffer()
```

Creates a view of this byte buffer as a long buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new long buffer

---

#### asLongBuffer

public abstract

LongBuffer

asLongBuffer()

Creates a view of this byte buffer as a long buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

getFloat

```java
public abstract float getFloat()
```

Relative

get

method for reading a float value.

Reads the next four bytes at this buffer's current position,
composing them into a float value according to the current byte order,
and then increments the position by four.

**Returns:** The float value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than four bytes
remaining in this buffer

---

#### getFloat

public abstract float getFloat()

Relative

get

method for reading a float value.

Reads the next four bytes at this buffer's current position,
composing them into a float value according to the current byte order,
and then increments the position by four.

Reads the next four bytes at this buffer's current position,
composing them into a float value according to the current byte order,
and then increments the position by four.

putFloat

```java
public abstract
ByteBuffer
putFloat​(float value)
```

Relative

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

**Parameters:** value

- The float value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than four bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putFloat

public abstract

ByteBuffer

putFloat​(float value)

Relative

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the current position, and then
increments the position by four.

getFloat

```java
public abstract float getFloat​(int index)
```

Absolute

get

method for reading a float value.

Reads four bytes at the given index, composing them into a
float value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The float value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three

---

#### getFloat

public abstract float getFloat​(int index)

Absolute

get

method for reading a float value.

Reads four bytes at the given index, composing them into a
float value according to the current byte order.

Reads four bytes at the given index, composing them into a
float value according to the current byte order.

putFloat

```java
public abstract
ByteBuffer
putFloat​(int index,
float value)
```

Absolute

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The float value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus three
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putFloat

public abstract

ByteBuffer

putFloat​(int index,
float value)

Absolute

put

method for writing a float
value

(optional operation)

.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the given index.

Writes four bytes containing the given float value, in the
current byte order, into this buffer at the given index.

asFloatBuffer

```java
public abstract
FloatBuffer
asFloatBuffer()
```

Creates a view of this byte buffer as a float buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new float buffer

---

#### asFloatBuffer

public abstract

FloatBuffer

asFloatBuffer()

Creates a view of this byte buffer as a float buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
four, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

getDouble

```java
public abstract double getDouble()
```

Relative

get

method for reading a double value.

Reads the next eight bytes at this buffer's current position,
composing them into a double value according to the current byte order,
and then increments the position by eight.

**Returns:** The double value at the buffer's current position
**Throws:** BufferUnderflowException

- If there are fewer than eight bytes
remaining in this buffer

---

#### getDouble

public abstract double getDouble()

Relative

get

method for reading a double value.

Reads the next eight bytes at this buffer's current position,
composing them into a double value according to the current byte order,
and then increments the position by eight.

Reads the next eight bytes at this buffer's current position,
composing them into a double value according to the current byte order,
and then increments the position by eight.

putDouble

```java
public abstract
ByteBuffer
putDouble​(double value)
```

Relative

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

**Parameters:** value

- The double value to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there are fewer than eight bytes
remaining in this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putDouble

public abstract

ByteBuffer

putDouble​(double value)

Relative

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the current position, and then
increments the position by eight.

getDouble

```java
public abstract double getDouble​(int index)
```

Absolute

get

method for reading a double value.

Reads eight bytes at the given index, composing them into a
double value according to the current byte order.

**Parameters:** index

- The index from which the bytes will be read
**Returns:** The double value at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven

---

#### getDouble

public abstract double getDouble​(int index)

Absolute

get

method for reading a double value.

Reads eight bytes at the given index, composing them into a
double value according to the current byte order.

Reads eight bytes at the given index, composing them into a
double value according to the current byte order.

putDouble

```java
public abstract
ByteBuffer
putDouble​(int index,
double value)
```

Absolute

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the given index.

**Parameters:** index

- The index at which the bytes will be written
**Parameters:** value

- The double value to be written
**Returns:** This buffer
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit,
minus seven
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### putDouble

public abstract

ByteBuffer

putDouble​(int index,
double value)

Absolute

put

method for writing a double
value

(optional operation)

.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the given index.

Writes eight bytes containing the given double value, in the
current byte order, into this buffer at the given index.

asDoubleBuffer

```java
public abstract
DoubleBuffer
asDoubleBuffer()
```

Creates a view of this byte buffer as a double buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

**Returns:** A new double buffer

---

#### asDoubleBuffer

public abstract

DoubleBuffer

asDoubleBuffer()

Creates a view of this byte buffer as a double buffer.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of bytes remaining in this buffer divided by
eight, its mark will be undefined, and its byte order will be that
of the byte buffer at the moment the view is created. The new buffer
will be direct if, and only if, this buffer is direct, and it will be
read-only if, and only if, this buffer is read-only.

---

