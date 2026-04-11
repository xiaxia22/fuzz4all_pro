# Class DoubleBuffer

**Source:** `java.base\java\nio\DoubleBuffer.html`

### Class Description

```java
public abstract class
DoubleBuffer

extends
Buffer

implements
Comparable
<
DoubleBuffer
>
```

A double buffer.

This class defines four categories of operations upon
double buffers:

- Absolute and relative

get

and

put

methods that read and write
single doubles;
- Relative

bulk get

methods that transfer contiguous sequences of doubles from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of doubles from a
double array or some other double
buffer into this buffer; and
- A method for

compacting

a double buffer.

Double buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
double array into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a double buffer is either

direct

or

non-direct

. A
double buffer created via the

wrap

methods of this class will
be non-direct. A double buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a double buffer is direct may be determined by invoking the

isDirect

method.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

**All Implemented Interfaces:** Comparable

<

DoubleBuffer

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
DoubleBuffer
allocate​(int capacity)

Allocates a new double buffer.

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

- The new buffer's capacity, in doubles

**Returns:**
- The new double buffer

**Throws:**
- IllegalArgumentException

- If the

capacity

is a negative integer

---

#### public static
DoubleBuffer
wrap​(double[] array,
int offset,
int length)

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
- The new double buffer

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### public static
DoubleBuffer
wrap​(double[] array)

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
- The new double buffer

---

#### public abstract
DoubleBuffer
slice()

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of doubles remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:**
- slice

in class

Buffer

**Returns:**
- The new double buffer

---

#### public abstract
DoubleBuffer
duplicate()

Creates a new double buffer that shares this buffer's content.

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
- The new double buffer

---

#### public abstract
DoubleBuffer
asReadOnlyBuffer()

Creates a new, read-only double buffer that shares this buffer's
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
- The new, read-only double buffer

---

#### public abstract double get()

Relative

get

method. Reads the double at this buffer's
current position, and then increments the position.

**Returns:**
- The double at the buffer's current position

**Throws:**
- BufferUnderflowException

- If the buffer's current position is not smaller than its limit

---

#### public abstract
DoubleBuffer
put​(double d)

Relative

put

method

(optional operation)

.

Writes the given double into this buffer at the current
position, and then increments the position.

**Parameters:**
- d

- The double to be written

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If this buffer's current position is not smaller than its limit
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public abstract double get​(int index)

Absolute

get

method. Reads the double at the given
index.

**Parameters:**
- index

- The index from which the double will be read

**Returns:**
- The double at the given index

**Throws:**
- IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

---

#### public abstract
DoubleBuffer
put​(int index,
double d)

Absolute

put

method

(optional operation)

.

Writes the given double into this buffer at the given
index.

**Parameters:**
- index

- The index at which the double will be written
- d

- The double value to be written

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
DoubleBuffer
get​(double[] dst,
int offset,
int length)

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
destination array. If there are fewer doubles remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

doubles from this
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

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

**Parameters:**
- dst

- The array into which doubles are to be written
- offset

- The offset within the array of the first double to be
written; must be non-negative and no larger than

dst.length
- length

- The maximum number of doubles to be written to the given
array; must be non-negative and no larger than

dst.length - offset

**Returns:**
- This buffer

**Throws:**
- BufferUnderflowException

- If there are fewer than

length

doubles
remaining in this buffer
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### public
DoubleBuffer
get​(double[] dst)

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
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

doubles
remaining in this buffer

---

#### public
DoubleBuffer
put​(
DoubleBuffer
src)

Relative bulk

put

method

(optional operation)

.

This method transfers the doubles remaining in the given source
buffer into this buffer. If there are more doubles remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no doubles are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

doubles from the given
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

- The source buffer from which doubles are to be read;
must not be this buffer

**Returns:**
- This buffer

**Throws:**
- BufferOverflowException

- If there is insufficient space in this buffer
for the remaining doubles in the source buffer
- IllegalArgumentException

- If the source buffer is this buffer
- ReadOnlyBufferException

- If this buffer is read-only

---

#### public
DoubleBuffer
put​(double[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

This method transfers doubles into this buffer from the given
source array. If there are more doubles to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

doubles from the
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

- The array from which doubles are to be read
- offset

- The offset within the array of the first double to be read;
must be non-negative and no larger than

array.length
- length

- The number of doubles to be read from the given array;
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
DoubleBuffer
put​(double[] src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
double array into this buffer. An invocation of this method of the
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

Tells whether or not this buffer is backed by an accessible double
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

#### public final double[] array()

Returns the double array that backs this
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
DoubleBuffer
compact()

Compacts this buffer

(optional operation)

.

The doubles between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
double at index

p

=

position()

is copied
to index zero, the double at index

p

+ 1 is copied
to index one, and so forth until the double at index

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

The buffer's position is set to the number of doubles copied,
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

Tells whether or not this double buffer is direct.

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

The hash code of a double buffer depends only upon its remaining
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

Two double buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

A double buffer is not equal to any other type of object.

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
DoubleBuffer
that)

Compares this buffer to another.

Two double buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

double

elements are compared as if by invoking

Double.compare(double,double)

, except that

-0.0

and

0.0

are considered to be equal.

Double.NaN

is considered by this method to be equal
to itself and greater than all other

double

values
(including

Double.POSITIVE_INFINITY

).

A double buffer is not comparable to any other type of object.

**Specified by:**
- compareTo

in interface

Comparable

<

DoubleBuffer

>

**Parameters:**
- that

- the object to be compared.

**Returns:**
- A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

---

#### public int mismatch​(
DoubleBuffer
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

#### public abstract
ByteOrder
order()

Retrieves this buffer's byte order.

The byte order of a double buffer created by allocation or by
wrapping an existing

double

array is the

native order

of the underlying
hardware. The byte order of a double buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

**Returns:**
- This buffer's byte order

---

### Additional Sections

#### Class DoubleBuffer

java.lang.Object

- java.nio.Buffer
- - java.nio.DoubleBuffer

java.nio.Buffer

- java.nio.DoubleBuffer

java.nio.DoubleBuffer

**All Implemented Interfaces:** Comparable

<

DoubleBuffer

>

```java
public abstract class
DoubleBuffer

extends
Buffer

implements
Comparable
<
DoubleBuffer
>
```

A double buffer.

This class defines four categories of operations upon
double buffers:

- Absolute and relative

get

and

put

methods that read and write
single doubles;
- Relative

bulk get

methods that transfer contiguous sequences of doubles from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of doubles from a
double array or some other double
buffer into this buffer; and
- A method for

compacting

a double buffer.

Double buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
double array into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a double buffer is either

direct

or

non-direct

. A
double buffer created via the

wrap

methods of this class will
be non-direct. A double buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a double buffer is direct may be determined by invoking the

isDirect

method.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

**Since:** 1.4

public abstract class

DoubleBuffer

extends

Buffer

implements

Comparable

<

DoubleBuffer

>

A double buffer.

This class defines four categories of operations upon
double buffers:

- Absolute and relative

get

and

put

methods that read and write
single doubles;
- Relative

bulk get

methods that transfer contiguous sequences of doubles from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of doubles from a
double array or some other double
buffer into this buffer; and
- A method for

compacting

a double buffer.

Double buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
double array into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a double buffer is either

direct

or

non-direct

. A
double buffer created via the

wrap

methods of this class will
be non-direct. A double buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a double buffer is direct may be determined by invoking the

isDirect

method.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

This class defines four categories of operations upon
double buffers:

- Absolute and relative

get

and

put

methods that read and write
single doubles;
- Relative

bulk get

methods that transfer contiguous sequences of doubles from this buffer
into an array; and
- Relative

bulk put

methods that transfer contiguous sequences of doubles from a
double array or some other double
buffer into this buffer; and
- A method for

compacting

a double buffer.

Double buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
double array into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a double buffer is either

direct

or

non-direct

. A
double buffer created via the

wrap

methods of this class will
be non-direct. A double buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a double buffer is direct may be determined by invoking the

isDirect

method.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

Absolute and relative

get

and

put

methods that read and write
single doubles;

Relative

bulk get

methods that transfer contiguous sequences of doubles from this buffer
into an array; and

Relative

bulk put

methods that transfer contiguous sequences of doubles from a
double array or some other double
buffer into this buffer; and

A method for

compacting

a double buffer.

Absolute and relative

get

and

put

methods that read and write
single doubles;

Relative

bulk get

methods that transfer contiguous sequences of doubles from this buffer
into an array; and

Relative

bulk put

methods that transfer contiguous sequences of doubles from a
double array or some other double
buffer into this buffer; and

A method for

compacting

a double buffer.

Double buffers can be created either by

allocation

, which allocates space for the buffer's

content, by

wrapping

an existing
double array into a buffer, or by creating a

view

of an existing byte buffer.

Like a byte buffer, a double buffer is either

direct

or

non-direct

. A
double buffer created via the

wrap

methods of this class will
be non-direct. A double buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a double buffer is direct may be determined by invoking the

isDirect

method.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

Like a byte buffer, a double buffer is either

direct

or

non-direct

. A
double buffer created via the

wrap

methods of this class will
be non-direct. A double buffer created as a view of a byte buffer will
be direct if, and only if, the byte buffer itself is direct. Whether or not
a double buffer is direct may be determined by invoking the

isDirect

method.

Methods in this class that do not otherwise have a value to return are
specified to return the buffer upon which they are invoked. This allows
method invocations to be chained.

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

DoubleBuffer

allocate

​(int capacity)

Allocates a new double buffer.

double[]

array

()

Returns the double array that backs this
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

DoubleBuffer

asReadOnlyBuffer

()

Creates a new, read-only double buffer that shares this buffer's
content.

abstract

DoubleBuffer

compact

()

Compacts this buffer

(optional operation)

.

int

compareTo

​(

DoubleBuffer

that)

Compares this buffer to another.

abstract

DoubleBuffer

duplicate

()

Creates a new double buffer that shares this buffer's content.

boolean

equals

​(

Object

ob)

Tells whether or not this buffer is equal to another object.

abstract double

get

()

Relative

get

method.

DoubleBuffer

get

​(double[] dst)

Relative bulk

get

method.

DoubleBuffer

get

​(double[] dst,
int offset,
int length)

Relative bulk

get

method.

abstract double

get

​(int index)

Absolute

get

method.

boolean

hasArray

()

Tells whether or not this buffer is backed by an accessible double
array.

int

hashCode

()

Returns the current hash code of this buffer.

abstract boolean

isDirect

()

Tells whether or not this double buffer is direct.

int

mismatch

​(

DoubleBuffer

that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

abstract

ByteOrder

order

()

Retrieves this buffer's byte order.

abstract

DoubleBuffer

put

​(double d)

Relative

put

method

(optional operation)

.

DoubleBuffer

put

​(double[] src)

Relative bulk

put

method

(optional operation)

.

DoubleBuffer

put

​(double[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

abstract

DoubleBuffer

put

​(int index,
double d)

Absolute

put

method

(optional operation)

.

DoubleBuffer

put

​(

DoubleBuffer

src)

Relative bulk

put

method

(optional operation)

.

abstract

DoubleBuffer

slice

()

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

String

toString

()

Returns a string summarizing the state of this buffer.

static

DoubleBuffer

wrap

​(double[] array)

Wraps a double array into a buffer.

static

DoubleBuffer

wrap

​(double[] array,
int offset,
int length)

Wraps a double array into a buffer.

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

static

DoubleBuffer

allocate

​(int capacity)

Allocates a new double buffer.

double[]

array

()

Returns the double array that backs this
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

DoubleBuffer

asReadOnlyBuffer

()

Creates a new, read-only double buffer that shares this buffer's
content.

abstract

DoubleBuffer

compact

()

Compacts this buffer

(optional operation)

.

int

compareTo

​(

DoubleBuffer

that)

Compares this buffer to another.

abstract

DoubleBuffer

duplicate

()

Creates a new double buffer that shares this buffer's content.

boolean

equals

​(

Object

ob)

Tells whether or not this buffer is equal to another object.

abstract double

get

()

Relative

get

method.

DoubleBuffer

get

​(double[] dst)

Relative bulk

get

method.

DoubleBuffer

get

​(double[] dst,
int offset,
int length)

Relative bulk

get

method.

abstract double

get

​(int index)

Absolute

get

method.

boolean

hasArray

()

Tells whether or not this buffer is backed by an accessible double
array.

int

hashCode

()

Returns the current hash code of this buffer.

abstract boolean

isDirect

()

Tells whether or not this double buffer is direct.

int

mismatch

​(

DoubleBuffer

that)

Finds and returns the relative index of the first mismatch between this
buffer and a given buffer.

abstract

ByteOrder

order

()

Retrieves this buffer's byte order.

abstract

DoubleBuffer

put

​(double d)

Relative

put

method

(optional operation)

.

DoubleBuffer

put

​(double[] src)

Relative bulk

put

method

(optional operation)

.

DoubleBuffer

put

​(double[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

abstract

DoubleBuffer

put

​(int index,
double d)

Absolute

put

method

(optional operation)

.

DoubleBuffer

put

​(

DoubleBuffer

src)

Relative bulk

put

method

(optional operation)

.

abstract

DoubleBuffer

slice

()

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

String

toString

()

Returns a string summarizing the state of this buffer.

static

DoubleBuffer

wrap

​(double[] array)

Wraps a double array into a buffer.

static

DoubleBuffer

wrap

​(double[] array,
int offset,
int length)

Wraps a double array into a buffer.

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

Allocates a new double buffer.

Returns the double array that backs this
buffer

(optional operation)

.

Returns the offset within this buffer's backing array of the first
element of the buffer

(optional operation)

.

Creates a new, read-only double buffer that shares this buffer's
content.

Compacts this buffer

(optional operation)

.

Compares this buffer to another.

Creates a new double buffer that shares this buffer's content.

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

Tells whether or not this buffer is backed by an accessible double
array.

Returns the current hash code of this buffer.

Tells whether or not this double buffer is direct.

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

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

Returns a string summarizing the state of this buffer.

Wraps a double array into a buffer.

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

- allocate

```java
public static
DoubleBuffer
allocate​(int capacity)
```

Allocates a new double buffer.

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

- The new buffer's capacity, in doubles
**Returns:** The new double buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- wrap

```java
public static
DoubleBuffer
wrap​(double[] array,
int offset,
int length)
```

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
**Returns:** The new double buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- wrap

```java
public static
DoubleBuffer
wrap​(double[] array)
```

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
**Returns:** The new double buffer

- slice

```java
public abstract
DoubleBuffer
slice()
```

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of doubles remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new double buffer

- duplicate

```java
public abstract
DoubleBuffer
duplicate()
```

Creates a new double buffer that shares this buffer's content.

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
**Returns:** The new double buffer

- asReadOnlyBuffer

```java
public abstract
DoubleBuffer
asReadOnlyBuffer()
```

Creates a new, read-only double buffer that shares this buffer's
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

**Returns:** The new, read-only double buffer

- get

```java
public abstract double get()
```

Relative

get

method. Reads the double at this buffer's
current position, and then increments the position.

**Returns:** The double at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

- put

```java
public abstract
DoubleBuffer
put​(double d)
```

Relative

put

method

(optional operation)

.

Writes the given double into this buffer at the current
position, and then increments the position.

**Parameters:** d

- The double to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public abstract double get​(int index)
```

Absolute

get

method. Reads the double at the given
index.

**Parameters:** index

- The index from which the double will be read
**Returns:** The double at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

- put

```java
public abstract
DoubleBuffer
put​(int index,
double d)
```

Absolute

put

method

(optional operation)

.

Writes the given double into this buffer at the given
index.

**Parameters:** index

- The index at which the double will be written
**Parameters:** d

- The double value to be written
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
DoubleBuffer
get​(double[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
destination array. If there are fewer doubles remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

doubles from this
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

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which doubles are to be written
**Parameters:** offset

- The offset within the array of the first double to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of doubles to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

doubles
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
DoubleBuffer
get​(double[] dst)
```

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
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

doubles
remaining in this buffer

- put

```java
public
DoubleBuffer
put​(
DoubleBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the doubles remaining in the given source
buffer into this buffer. If there are more doubles remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no doubles are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

doubles from the given
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

- The source buffer from which doubles are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining doubles in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
DoubleBuffer
put​(double[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers doubles into this buffer from the given
source array. If there are more doubles to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

doubles from the
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

- The array from which doubles are to be read
**Parameters:** offset

- The offset within the array of the first double to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of doubles to be read from the given array;
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
DoubleBuffer
put​(double[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
double array into this buffer. An invocation of this method of the
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

Tells whether or not this buffer is backed by an accessible double
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
public final double[] array()
```

Returns the double array that backs this
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
DoubleBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The doubles between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
double at index

p

=

position()

is copied
to index zero, the double at index

p

+ 1 is copied
to index one, and so forth until the double at index

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

The buffer's position is set to the number of doubles copied,
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

Tells whether or not this double buffer is direct.

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

The hash code of a double buffer depends only upon its remaining
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

Two double buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

A double buffer is not equal to any other type of object.

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
DoubleBuffer
that)
```

Compares this buffer to another.

Two double buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

double

elements are compared as if by invoking

Double.compare(double,double)

, except that

-0.0

and

0.0

are considered to be equal.

Double.NaN

is considered by this method to be equal
to itself and greater than all other

double

values
(including

Double.POSITIVE_INFINITY

).

A double buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

DoubleBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

- mismatch

```java
public int mismatch​(
DoubleBuffer
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
public abstract
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order of a double buffer created by allocation or by
wrapping an existing

double

array is the

native order

of the underlying
hardware. The byte order of a double buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

**Returns:** This buffer's byte order

Method Detail

- allocate

```java
public static
DoubleBuffer
allocate​(int capacity)
```

Allocates a new double buffer.

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

- The new buffer's capacity, in doubles
**Returns:** The new double buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

- wrap

```java
public static
DoubleBuffer
wrap​(double[] array,
int offset,
int length)
```

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
**Returns:** The new double buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

- wrap

```java
public static
DoubleBuffer
wrap​(double[] array)
```

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
**Returns:** The new double buffer

- slice

```java
public abstract
DoubleBuffer
slice()
```

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of doubles remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new double buffer

- duplicate

```java
public abstract
DoubleBuffer
duplicate()
```

Creates a new double buffer that shares this buffer's content.

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
**Returns:** The new double buffer

- asReadOnlyBuffer

```java
public abstract
DoubleBuffer
asReadOnlyBuffer()
```

Creates a new, read-only double buffer that shares this buffer's
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

**Returns:** The new, read-only double buffer

- get

```java
public abstract double get()
```

Relative

get

method. Reads the double at this buffer's
current position, and then increments the position.

**Returns:** The double at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

- put

```java
public abstract
DoubleBuffer
put​(double d)
```

Relative

put

method

(optional operation)

.

Writes the given double into this buffer at the current
position, and then increments the position.

**Parameters:** d

- The double to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- get

```java
public abstract double get​(int index)
```

Absolute

get

method. Reads the double at the given
index.

**Parameters:** index

- The index from which the double will be read
**Returns:** The double at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

- put

```java
public abstract
DoubleBuffer
put​(int index,
double d)
```

Absolute

put

method

(optional operation)

.

Writes the given double into this buffer at the given
index.

**Parameters:** index

- The index at which the double will be written
**Parameters:** d

- The double value to be written
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
DoubleBuffer
get​(double[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
destination array. If there are fewer doubles remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

doubles from this
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

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which doubles are to be written
**Parameters:** offset

- The offset within the array of the first double to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of doubles to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

doubles
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
DoubleBuffer
get​(double[] dst)
```

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
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

doubles
remaining in this buffer

- put

```java
public
DoubleBuffer
put​(
DoubleBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the doubles remaining in the given source
buffer into this buffer. If there are more doubles remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no doubles are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

doubles from the given
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

- The source buffer from which doubles are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining doubles in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

- put

```java
public
DoubleBuffer
put​(double[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers doubles into this buffer from the given
source array. If there are more doubles to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

doubles from the
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

- The array from which doubles are to be read
**Parameters:** offset

- The offset within the array of the first double to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of doubles to be read from the given array;
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
DoubleBuffer
put​(double[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
double array into this buffer. An invocation of this method of the
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

Tells whether or not this buffer is backed by an accessible double
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
public final double[] array()
```

Returns the double array that backs this
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
DoubleBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The doubles between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
double at index

p

=

position()

is copied
to index zero, the double at index

p

+ 1 is copied
to index one, and so forth until the double at index

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

The buffer's position is set to the number of doubles copied,
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

Tells whether or not this double buffer is direct.

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

The hash code of a double buffer depends only upon its remaining
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

Two double buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

A double buffer is not equal to any other type of object.

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
DoubleBuffer
that)
```

Compares this buffer to another.

Two double buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

double

elements are compared as if by invoking

Double.compare(double,double)

, except that

-0.0

and

0.0

are considered to be equal.

Double.NaN

is considered by this method to be equal
to itself and greater than all other

double

values
(including

Double.POSITIVE_INFINITY

).

A double buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

DoubleBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

- mismatch

```java
public int mismatch​(
DoubleBuffer
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
public abstract
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order of a double buffer created by allocation or by
wrapping an existing

double

array is the

native order

of the underlying
hardware. The byte order of a double buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

**Returns:** This buffer's byte order

---

#### Method Detail

allocate

```java
public static
DoubleBuffer
allocate​(int capacity)
```

Allocates a new double buffer.

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

- The new buffer's capacity, in doubles
**Returns:** The new double buffer
**Throws:** IllegalArgumentException

- If the

capacity

is a negative integer

---

#### allocate

public static

DoubleBuffer

allocate​(int capacity)

Allocates a new double buffer.

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
DoubleBuffer
wrap​(double[] array,
int offset,
int length)
```

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
**Returns:** The new double buffer
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold

---

#### wrap

public static

DoubleBuffer

wrap​(double[] array,
int offset,
int length)

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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

The new buffer will be backed by the given double array;
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
DoubleBuffer
wrap​(double[] array)
```

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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
**Returns:** The new double buffer

---

#### wrap

public static

DoubleBuffer

wrap​(double[] array)

Wraps a double array into a buffer.

The new buffer will be backed by the given double array;
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

The new buffer will be backed by the given double array;
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

slice

```java
public abstract
DoubleBuffer
slice()
```

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of doubles remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

**Specified by:** slice

in class

Buffer
**Returns:** The new double buffer

---

#### slice

public abstract

DoubleBuffer

slice()

Creates a new double buffer whose content is a shared subsequence of
this buffer's content.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of doubles remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The content of the new buffer will start at this buffer's current
position. Changes to this buffer's content will be visible in the new
buffer, and vice versa; the two buffers' position, limit, and mark
values will be independent.

The new buffer's position will be zero, its capacity and its limit
will be the number of doubles remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

The new buffer's position will be zero, its capacity and its limit
will be the number of doubles remaining in this buffer, its mark will be
undefined, and its byte order will be

identical to that of this buffer.

The new buffer will be direct if, and only if, this buffer is direct, and
it will be read-only if, and only if, this buffer is read-only.

duplicate

```java
public abstract
DoubleBuffer
duplicate()
```

Creates a new double buffer that shares this buffer's content.

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
**Returns:** The new double buffer

---

#### duplicate

public abstract

DoubleBuffer

duplicate()

Creates a new double buffer that shares this buffer's content.

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
DoubleBuffer
asReadOnlyBuffer()
```

Creates a new, read-only double buffer that shares this buffer's
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

**Returns:** The new, read-only double buffer

---

#### asReadOnlyBuffer

public abstract

DoubleBuffer

asReadOnlyBuffer()

Creates a new, read-only double buffer that shares this buffer's
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
public abstract double get()
```

Relative

get

method. Reads the double at this buffer's
current position, and then increments the position.

**Returns:** The double at the buffer's current position
**Throws:** BufferUnderflowException

- If the buffer's current position is not smaller than its limit

---

#### get

public abstract double get()

Relative

get

method. Reads the double at this buffer's
current position, and then increments the position.

put

```java
public abstract
DoubleBuffer
put​(double d)
```

Relative

put

method

(optional operation)

.

Writes the given double into this buffer at the current
position, and then increments the position.

**Parameters:** d

- The double to be written
**Returns:** This buffer
**Throws:** BufferOverflowException

- If this buffer's current position is not smaller than its limit
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public abstract

DoubleBuffer

put​(double d)

Relative

put

method

(optional operation)

.

Writes the given double into this buffer at the current
position, and then increments the position.

Writes the given double into this buffer at the current
position, and then increments the position.

get

```java
public abstract double get​(int index)
```

Absolute

get

method. Reads the double at the given
index.

**Parameters:** index

- The index from which the double will be read
**Returns:** The double at the given index
**Throws:** IndexOutOfBoundsException

- If

index

is negative
or not smaller than the buffer's limit

---

#### get

public abstract double get​(int index)

Absolute

get

method. Reads the double at the given
index.

put

```java
public abstract
DoubleBuffer
put​(int index,
double d)
```

Absolute

put

method

(optional operation)

.

Writes the given double into this buffer at the given
index.

**Parameters:** index

- The index at which the double will be written
**Parameters:** d

- The double value to be written
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

DoubleBuffer

put​(int index,
double d)

Absolute

put

method

(optional operation)

.

Writes the given double into this buffer at the given
index.

Writes the given double into this buffer at the given
index.

get

```java
public
DoubleBuffer
get​(double[] dst,
int offset,
int length)
```

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
destination array. If there are fewer doubles remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

doubles from this
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

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

**Parameters:** dst

- The array into which doubles are to be written
**Parameters:** offset

- The offset within the array of the first double to be
written; must be non-negative and no larger than

dst.length
**Parameters:** length

- The maximum number of doubles to be written to the given
array; must be non-negative and no larger than

dst.length - offset
**Returns:** This buffer
**Throws:** BufferUnderflowException

- If there are fewer than

length

doubles
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

DoubleBuffer

get​(double[] dst,
int offset,
int length)

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
destination array. If there are fewer doubles remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

doubles from this
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

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

This method transfers doubles from this buffer into the given
destination array. If there are fewer doubles remaining in the
buffer than are required to satisfy the request, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferUnderflowException

is
thrown.

Otherwise, this method copies

length

doubles from this
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

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

Otherwise, this method copies

length

doubles from this
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

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

In other words, an invocation of this method of the form

src.get(dst, off, len)

has exactly the same effect as
the loop

```java
for (int i = off; i < off + len; i++)
dst[i] = src.get();
```

except that it first checks that there are sufficient doubles in
this buffer and it is potentially much more efficient.

for (int i = off; i < off + len; i++)
dst[i] = src.get();

get

```java
public
DoubleBuffer
get​(double[] dst)
```

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
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

doubles
remaining in this buffer

---

#### get

public

DoubleBuffer

get​(double[] dst)

Relative bulk

get

method.

This method transfers doubles from this buffer into the given
destination array. An invocation of this method of the form

src.get(a)

behaves in exactly the same way as the invocation

```java
src.get(a, 0, a.length)
```

This method transfers doubles from this buffer into the given
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
DoubleBuffer
put​(
DoubleBuffer
src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the doubles remaining in the given source
buffer into this buffer. If there are more doubles remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no doubles are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

doubles from the given
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

- The source buffer from which doubles are to be read;
must not be this buffer
**Returns:** This buffer
**Throws:** BufferOverflowException

- If there is insufficient space in this buffer
for the remaining doubles in the source buffer
**Throws:** IllegalArgumentException

- If the source buffer is this buffer
**Throws:** ReadOnlyBufferException

- If this buffer is read-only

---

#### put

public

DoubleBuffer

put​(

DoubleBuffer

src)

Relative bulk

put

method

(optional operation)

.

This method transfers the doubles remaining in the given source
buffer into this buffer. If there are more doubles remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no doubles are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

doubles from the given
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

This method transfers the doubles remaining in the given source
buffer into this buffer. If there are more doubles remaining in the
source buffer than in this buffer, that is, if

src.remaining()

>

remaining()

,
then no doubles are transferred and a

BufferOverflowException

is thrown.

Otherwise, this method copies

n

=

src.remaining()

doubles from the given
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

doubles from the given
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
DoubleBuffer
put​(double[] src,
int offset,
int length)
```

Relative bulk

put

method

(optional operation)

.

This method transfers doubles into this buffer from the given
source array. If there are more doubles to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

doubles from the
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

- The array from which doubles are to be read
**Parameters:** offset

- The offset within the array of the first double to be read;
must be non-negative and no larger than

array.length
**Parameters:** length

- The number of doubles to be read from the given array;
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

DoubleBuffer

put​(double[] src,
int offset,
int length)

Relative bulk

put

method

(optional operation)

.

This method transfers doubles into this buffer from the given
source array. If there are more doubles to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

doubles from the
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

This method transfers doubles into this buffer from the given
source array. If there are more doubles to be copied from the array
than remain in this buffer, that is, if

length

>

remaining()

, then no
doubles are transferred and a

BufferOverflowException

is
thrown.

Otherwise, this method copies

length

doubles from the
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

doubles from the
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
DoubleBuffer
put​(double[] src)
```

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
double array into this buffer. An invocation of this method of the
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

DoubleBuffer

put​(double[] src)

Relative bulk

put

method

(optional operation)

.

This method transfers the entire content of the given source
double array into this buffer. An invocation of this method of the
form

dst.put(a)

behaves in exactly the same way as the
invocation

```java
dst.put(a, 0, a.length)
```

This method transfers the entire content of the given source
double array into this buffer. An invocation of this method of the
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

Tells whether or not this buffer is backed by an accessible double
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

Tells whether or not this buffer is backed by an accessible double
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
public final double[] array()
```

Returns the double array that backs this
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

public final double[] array()

Returns the double array that backs this
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
DoubleBuffer
compact()
```

Compacts this buffer

(optional operation)

.

The doubles between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
double at index

p

=

position()

is copied
to index zero, the double at index

p

+ 1 is copied
to index one, and so forth until the double at index

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

The buffer's position is set to the number of doubles copied,
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

DoubleBuffer

compact()

Compacts this buffer

(optional operation)

.

The doubles between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
double at index

p

=

position()

is copied
to index zero, the double at index

p

+ 1 is copied
to index one, and so forth until the double at index

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

The buffer's position is set to the number of doubles copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

The doubles between the buffer's current position and its limit,
if any, are copied to the beginning of the buffer. That is, the
double at index

p

=

position()

is copied
to index zero, the double at index

p

+ 1 is copied
to index one, and so forth until the double at index

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

The buffer's position is set to the number of doubles copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

The buffer's position is set to the number of doubles copied,
rather than to zero, so that an invocation of this method can be
followed immediately by an invocation of another relative

put

method.

isDirect

```java
public abstract boolean isDirect()
```

Tells whether or not this double buffer is direct.

**Specified by:** isDirect

in class

Buffer
**Returns:** true

if, and only if, this buffer is direct

---

#### isDirect

public abstract boolean isDirect()

Tells whether or not this double buffer is direct.

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

The hash code of a double buffer depends only upon its remaining
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

The hash code of a double buffer depends only upon its remaining
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

The hash code of a double buffer depends only upon its remaining
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

Two double buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

A double buffer is not equal to any other type of object.

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

Two double buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

A double buffer is not equal to any other type of object.

Two double buffers are equal if, and only if,

- They have the same element type,
- They have the same number of remaining elements, and
- The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

A double buffer is not equal to any other type of object.

They have the same element type,

They have the same number of remaining elements, and

The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

They have the same element type,

They have the same number of remaining elements, and

The two sequences of remaining elements, considered
independently of their starting positions, are pointwise equal.

This method considers two double elements

a

and

b

to be equal if

(a == b) || (Double.isNaN(a) && Double.isNaN(b))

.
The values

-0.0

and

+0.0

are considered to be
equal, unlike

Double.equals(Object)

.

A double buffer is not equal to any other type of object.

compareTo

```java
public int compareTo​(
DoubleBuffer
that)
```

Compares this buffer to another.

Two double buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

double

elements are compared as if by invoking

Double.compare(double,double)

, except that

-0.0

and

0.0

are considered to be equal.

Double.NaN

is considered by this method to be equal
to itself and greater than all other

double

values
(including

Double.POSITIVE_INFINITY

).

A double buffer is not comparable to any other type of object.

**Specified by:** compareTo

in interface

Comparable

<

DoubleBuffer

>
**Parameters:** that

- the object to be compared.
**Returns:** A negative integer, zero, or a positive integer as this buffer
is less than, equal to, or greater than the given buffer

---

#### compareTo

public int compareTo​(

DoubleBuffer

that)

Compares this buffer to another.

Two double buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

double

elements are compared as if by invoking

Double.compare(double,double)

, except that

-0.0

and

0.0

are considered to be equal.

Double.NaN

is considered by this method to be equal
to itself and greater than all other

double

values
(including

Double.POSITIVE_INFINITY

).

A double buffer is not comparable to any other type of object.

Two double buffers are compared by comparing their sequences of
remaining elements lexicographically, without regard to the starting
position of each sequence within its corresponding buffer.

Pairs of

double

elements are compared as if by invoking

Double.compare(double,double)

, except that

-0.0

and

0.0

are considered to be equal.

Double.NaN

is considered by this method to be equal
to itself and greater than all other

double

values
(including

Double.POSITIVE_INFINITY

).

A double buffer is not comparable to any other type of object.

A double buffer is not comparable to any other type of object.

mismatch

```java
public int mismatch​(
DoubleBuffer
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

DoubleBuffer

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
public abstract
ByteOrder
order()
```

Retrieves this buffer's byte order.

The byte order of a double buffer created by allocation or by
wrapping an existing

double

array is the

native order

of the underlying
hardware. The byte order of a double buffer created as a

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

The byte order of a double buffer created by allocation or by
wrapping an existing

double

array is the

native order

of the underlying
hardware. The byte order of a double buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

The byte order of a double buffer created by allocation or by
wrapping an existing

double

array is the

native order

of the underlying
hardware. The byte order of a double buffer created as a

view

of a byte buffer is that of the
byte buffer at the moment that the view is created.

---

