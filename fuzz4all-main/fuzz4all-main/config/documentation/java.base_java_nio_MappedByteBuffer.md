# Class MappedByteBuffer

**Source:** `java.base\java\nio\MappedByteBuffer.html`

### Class Description

```java
public abstract class
MappedByteBuffer

extends
ByteBuffer
```

A direct byte buffer whose content is a memory-mapped region of a file.

Mapped byte buffers are created via the

FileChannel.map

method. This class
extends the

ByteBuffer

class with operations that are specific to
memory-mapped file regions.

A mapped byte buffer and the file mapping that it represents remain
valid until the buffer itself is garbage-collected.

The content of a mapped byte buffer can change at any time, for example
if the content of the corresponding region of the mapped file is changed by
this program or another. Whether or not such changes occur, and when they
occur, is operating-system dependent and therefore unspecified.

All or part of a mapped byte buffer may become
inaccessible at any time, for example if the mapped file is truncated. An
attempt to access an inaccessible region of a mapped byte buffer will not
change the buffer's content and will cause an unspecified exception to be
thrown either at the time of the access or at some later time. It is
therefore strongly recommended that appropriate precautions be taken to
avoid the manipulation of a mapped file by this program, or by a
concurrently running program, except to read or write the file's content.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

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

#### public final boolean isLoaded()

Tells whether or not this buffer's content is resident in physical
memory.

A return value of

true

implies that it is highly likely
that all of the data in this buffer is resident in physical memory and
may therefore be accessed without incurring any virtual-memory page
faults or I/O operations. A return value of

false

does not
necessarily imply that the buffer's content is not resident in physical
memory.

The returned value is a hint, rather than a guarantee, because the
underlying operating system may have paged out some of the buffer's data
by the time that an invocation of this method returns.

**Returns:**
- true

if it is likely that this buffer's content
is resident in physical memory

---

#### public final
MappedByteBuffer
load()

Loads this buffer's content into physical memory.

This method makes a best effort to ensure that, when it returns,
this buffer's content is resident in physical memory. Invoking this
method may cause some number of page faults and I/O operations to
occur.

**Returns:**
- This buffer

---

#### public final
MappedByteBuffer
force()

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

If the file mapped into this buffer resides on a local storage
device then when this method returns it is guaranteed that all changes
made to the buffer since it was created, or since this method was last
invoked, will have been written to that device.

If the file does not reside on a local device then no such guarantee
is made.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

**Returns:**
- This buffer

---

### Additional Sections

#### Class MappedByteBuffer

java.lang.Object

- java.nio.Buffer
- - java.nio.ByteBuffer
- - java.nio.MappedByteBuffer

java.nio.Buffer

- java.nio.ByteBuffer
- - java.nio.MappedByteBuffer

java.nio.ByteBuffer

- java.nio.MappedByteBuffer

java.nio.MappedByteBuffer

**All Implemented Interfaces:** Comparable

<

ByteBuffer

>

```java
public abstract class
MappedByteBuffer

extends
ByteBuffer
```

A direct byte buffer whose content is a memory-mapped region of a file.

Mapped byte buffers are created via the

FileChannel.map

method. This class
extends the

ByteBuffer

class with operations that are specific to
memory-mapped file regions.

A mapped byte buffer and the file mapping that it represents remain
valid until the buffer itself is garbage-collected.

The content of a mapped byte buffer can change at any time, for example
if the content of the corresponding region of the mapped file is changed by
this program or another. Whether or not such changes occur, and when they
occur, is operating-system dependent and therefore unspecified.

All or part of a mapped byte buffer may become
inaccessible at any time, for example if the mapped file is truncated. An
attempt to access an inaccessible region of a mapped byte buffer will not
change the buffer's content and will cause an unspecified exception to be
thrown either at the time of the access or at some later time. It is
therefore strongly recommended that appropriate precautions be taken to
avoid the manipulation of a mapped file by this program, or by a
concurrently running program, except to read or write the file's content.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

**Since:** 1.4

public abstract class

MappedByteBuffer

extends

ByteBuffer

A direct byte buffer whose content is a memory-mapped region of a file.

Mapped byte buffers are created via the

FileChannel.map

method. This class
extends the

ByteBuffer

class with operations that are specific to
memory-mapped file regions.

A mapped byte buffer and the file mapping that it represents remain
valid until the buffer itself is garbage-collected.

The content of a mapped byte buffer can change at any time, for example
if the content of the corresponding region of the mapped file is changed by
this program or another. Whether or not such changes occur, and when they
occur, is operating-system dependent and therefore unspecified.

All or part of a mapped byte buffer may become
inaccessible at any time, for example if the mapped file is truncated. An
attempt to access an inaccessible region of a mapped byte buffer will not
change the buffer's content and will cause an unspecified exception to be
thrown either at the time of the access or at some later time. It is
therefore strongly recommended that appropriate precautions be taken to
avoid the manipulation of a mapped file by this program, or by a
concurrently running program, except to read or write the file's content.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

Mapped byte buffers are created via the

FileChannel.map

method. This class
extends the

ByteBuffer

class with operations that are specific to
memory-mapped file regions.

A mapped byte buffer and the file mapping that it represents remain
valid until the buffer itself is garbage-collected.

The content of a mapped byte buffer can change at any time, for example
if the content of the corresponding region of the mapped file is changed by
this program or another. Whether or not such changes occur, and when they
occur, is operating-system dependent and therefore unspecified.

All or part of a mapped byte buffer may become
inaccessible at any time, for example if the mapped file is truncated. An
attempt to access an inaccessible region of a mapped byte buffer will not
change the buffer's content and will cause an unspecified exception to be
thrown either at the time of the access or at some later time. It is
therefore strongly recommended that appropriate precautions be taken to
avoid the manipulation of a mapped file by this program, or by a
concurrently running program, except to read or write the file's content.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

A mapped byte buffer and the file mapping that it represents remain
valid until the buffer itself is garbage-collected.

The content of a mapped byte buffer can change at any time, for example
if the content of the corresponding region of the mapped file is changed by
this program or another. Whether or not such changes occur, and when they
occur, is operating-system dependent and therefore unspecified.

All or part of a mapped byte buffer may become
inaccessible at any time, for example if the mapped file is truncated. An
attempt to access an inaccessible region of a mapped byte buffer will not
change the buffer's content and will cause an unspecified exception to be
thrown either at the time of the access or at some later time. It is
therefore strongly recommended that appropriate precautions be taken to
avoid the manipulation of a mapped file by this program, or by a
concurrently running program, except to read or write the file's content.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

The content of a mapped byte buffer can change at any time, for example
if the content of the corresponding region of the mapped file is changed by
this program or another. Whether or not such changes occur, and when they
occur, is operating-system dependent and therefore unspecified.

All or part of a mapped byte buffer may become
inaccessible at any time, for example if the mapped file is truncated. An
attempt to access an inaccessible region of a mapped byte buffer will not
change the buffer's content and will cause an unspecified exception to be
thrown either at the time of the access or at some later time. It is
therefore strongly recommended that appropriate precautions be taken to
avoid the manipulation of a mapped file by this program, or by a
concurrently running program, except to read or write the file's content.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

All or part of a mapped byte buffer may become
inaccessible at any time, for example if the mapped file is truncated. An
attempt to access an inaccessible region of a mapped byte buffer will not
change the buffer's content and will cause an unspecified exception to be
thrown either at the time of the access or at some later time. It is
therefore strongly recommended that appropriate precautions be taken to
avoid the manipulation of a mapped file by this program, or by a
concurrently running program, except to read or write the file's content.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

Mapped byte buffers otherwise behave no differently than ordinary direct
byte buffers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MappedByteBuffer

force

()

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

boolean

isLoaded

()

Tells whether or not this buffer's content is resident in physical
memory.

MappedByteBuffer

load

()

Loads this buffer's content into physical memory.

- Methods declared in class java.nio.

ByteBuffer

alignedSlice

,

alignmentOffset

,

allocate

,

allocateDirect

,

array

,

arrayOffset

,

asCharBuffer

,

asDoubleBuffer

,

asFloatBuffer

,

asIntBuffer

,

asLongBuffer

,

asReadOnlyBuffer

,

asShortBuffer

,

compact

,

compareTo

,

duplicate

,

equals

,

get

,

get

,

get

,

get

,

getChar

,

getChar

,

getDouble

,

getDouble

,

getFloat

,

getFloat

,

getInt

,

getInt

,

getLong

,

getLong

,

getShort

,

getShort

,

hasArray

,

hashCode

,

isDirect

,

mismatch

,

order

,

order

,

put

,

put

,

put

,

put

,

put

,

putChar

,

putChar

,

putDouble

,

putDouble

,

putFloat

,

putFloat

,

putInt

,

putInt

,

putLong

,

putLong

,

putShort

,

putShort

,

slice

,

toString

,

wrap

,

wrap

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

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MappedByteBuffer

force

()

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

boolean

isLoaded

()

Tells whether or not this buffer's content is resident in physical
memory.

MappedByteBuffer

load

()

Loads this buffer's content into physical memory.

- Methods declared in class java.nio.

ByteBuffer

alignedSlice

,

alignmentOffset

,

allocate

,

allocateDirect

,

array

,

arrayOffset

,

asCharBuffer

,

asDoubleBuffer

,

asFloatBuffer

,

asIntBuffer

,

asLongBuffer

,

asReadOnlyBuffer

,

asShortBuffer

,

compact

,

compareTo

,

duplicate

,

equals

,

get

,

get

,

get

,

get

,

getChar

,

getChar

,

getDouble

,

getDouble

,

getFloat

,

getFloat

,

getInt

,

getInt

,

getLong

,

getLong

,

getShort

,

getShort

,

hasArray

,

hashCode

,

isDirect

,

mismatch

,

order

,

order

,

put

,

put

,

put

,

put

,

put

,

putChar

,

putChar

,

putDouble

,

putDouble

,

putFloat

,

putFloat

,

putInt

,

putInt

,

putLong

,

putLong

,

putShort

,

putShort

,

slice

,

toString

,

wrap

,

wrap

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

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

Tells whether or not this buffer's content is resident in physical
memory.

Loads this buffer's content into physical memory.

Methods declared in class java.nio.

ByteBuffer

alignedSlice

,

alignmentOffset

,

allocate

,

allocateDirect

,

array

,

arrayOffset

,

asCharBuffer

,

asDoubleBuffer

,

asFloatBuffer

,

asIntBuffer

,

asLongBuffer

,

asReadOnlyBuffer

,

asShortBuffer

,

compact

,

compareTo

,

duplicate

,

equals

,

get

,

get

,

get

,

get

,

getChar

,

getChar

,

getDouble

,

getDouble

,

getFloat

,

getFloat

,

getInt

,

getInt

,

getLong

,

getLong

,

getShort

,

getShort

,

hasArray

,

hashCode

,

isDirect

,

mismatch

,

order

,

order

,

put

,

put

,

put

,

put

,

put

,

putChar

,

putChar

,

putDouble

,

putDouble

,

putFloat

,

putFloat

,

putInt

,

putInt

,

putLong

,

putLong

,

putShort

,

putShort

,

slice

,

toString

,

wrap

,

wrap

---

#### Methods declared in class java.nio. ByteBuffer

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

- isLoaded

```java
public final boolean isLoaded()
```

Tells whether or not this buffer's content is resident in physical
memory.

A return value of

true

implies that it is highly likely
that all of the data in this buffer is resident in physical memory and
may therefore be accessed without incurring any virtual-memory page
faults or I/O operations. A return value of

false

does not
necessarily imply that the buffer's content is not resident in physical
memory.

The returned value is a hint, rather than a guarantee, because the
underlying operating system may have paged out some of the buffer's data
by the time that an invocation of this method returns.

**Returns:** true

if it is likely that this buffer's content
is resident in physical memory

- load

```java
public final
MappedByteBuffer
load()
```

Loads this buffer's content into physical memory.

This method makes a best effort to ensure that, when it returns,
this buffer's content is resident in physical memory. Invoking this
method may cause some number of page faults and I/O operations to
occur.

**Returns:** This buffer

- force

```java
public final
MappedByteBuffer
force()
```

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

If the file mapped into this buffer resides on a local storage
device then when this method returns it is guaranteed that all changes
made to the buffer since it was created, or since this method was last
invoked, will have been written to that device.

If the file does not reside on a local device then no such guarantee
is made.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

**Returns:** This buffer

Method Detail

- isLoaded

```java
public final boolean isLoaded()
```

Tells whether or not this buffer's content is resident in physical
memory.

A return value of

true

implies that it is highly likely
that all of the data in this buffer is resident in physical memory and
may therefore be accessed without incurring any virtual-memory page
faults or I/O operations. A return value of

false

does not
necessarily imply that the buffer's content is not resident in physical
memory.

The returned value is a hint, rather than a guarantee, because the
underlying operating system may have paged out some of the buffer's data
by the time that an invocation of this method returns.

**Returns:** true

if it is likely that this buffer's content
is resident in physical memory

- load

```java
public final
MappedByteBuffer
load()
```

Loads this buffer's content into physical memory.

This method makes a best effort to ensure that, when it returns,
this buffer's content is resident in physical memory. Invoking this
method may cause some number of page faults and I/O operations to
occur.

**Returns:** This buffer

- force

```java
public final
MappedByteBuffer
force()
```

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

If the file mapped into this buffer resides on a local storage
device then when this method returns it is guaranteed that all changes
made to the buffer since it was created, or since this method was last
invoked, will have been written to that device.

If the file does not reside on a local device then no such guarantee
is made.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

**Returns:** This buffer

---

#### Method Detail

isLoaded

```java
public final boolean isLoaded()
```

Tells whether or not this buffer's content is resident in physical
memory.

A return value of

true

implies that it is highly likely
that all of the data in this buffer is resident in physical memory and
may therefore be accessed without incurring any virtual-memory page
faults or I/O operations. A return value of

false

does not
necessarily imply that the buffer's content is not resident in physical
memory.

The returned value is a hint, rather than a guarantee, because the
underlying operating system may have paged out some of the buffer's data
by the time that an invocation of this method returns.

**Returns:** true

if it is likely that this buffer's content
is resident in physical memory

---

#### isLoaded

public final boolean isLoaded()

Tells whether or not this buffer's content is resident in physical
memory.

A return value of

true

implies that it is highly likely
that all of the data in this buffer is resident in physical memory and
may therefore be accessed without incurring any virtual-memory page
faults or I/O operations. A return value of

false

does not
necessarily imply that the buffer's content is not resident in physical
memory.

The returned value is a hint, rather than a guarantee, because the
underlying operating system may have paged out some of the buffer's data
by the time that an invocation of this method returns.

A return value of

true

implies that it is highly likely
that all of the data in this buffer is resident in physical memory and
may therefore be accessed without incurring any virtual-memory page
faults or I/O operations. A return value of

false

does not
necessarily imply that the buffer's content is not resident in physical
memory.

The returned value is a hint, rather than a guarantee, because the
underlying operating system may have paged out some of the buffer's data
by the time that an invocation of this method returns.

The returned value is a hint, rather than a guarantee, because the
underlying operating system may have paged out some of the buffer's data
by the time that an invocation of this method returns.

load

```java
public final
MappedByteBuffer
load()
```

Loads this buffer's content into physical memory.

This method makes a best effort to ensure that, when it returns,
this buffer's content is resident in physical memory. Invoking this
method may cause some number of page faults and I/O operations to
occur.

**Returns:** This buffer

---

#### load

public final

MappedByteBuffer

load()

Loads this buffer's content into physical memory.

This method makes a best effort to ensure that, when it returns,
this buffer's content is resident in physical memory. Invoking this
method may cause some number of page faults and I/O operations to
occur.

This method makes a best effort to ensure that, when it returns,
this buffer's content is resident in physical memory. Invoking this
method may cause some number of page faults and I/O operations to
occur.

force

```java
public final
MappedByteBuffer
force()
```

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

If the file mapped into this buffer resides on a local storage
device then when this method returns it is guaranteed that all changes
made to the buffer since it was created, or since this method was last
invoked, will have been written to that device.

If the file does not reside on a local device then no such guarantee
is made.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

**Returns:** This buffer

---

#### force

public final

MappedByteBuffer

force()

Forces any changes made to this buffer's content to be written to the
storage device containing the mapped file.

If the file mapped into this buffer resides on a local storage
device then when this method returns it is guaranteed that all changes
made to the buffer since it was created, or since this method was last
invoked, will have been written to that device.

If the file does not reside on a local device then no such guarantee
is made.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

If the file mapped into this buffer resides on a local storage
device then when this method returns it is guaranteed that all changes
made to the buffer since it was created, or since this method was last
invoked, will have been written to that device.

If the file does not reside on a local device then no such guarantee
is made.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

If the file does not reside on a local device then no such guarantee
is made.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

If this buffer was not mapped in read/write mode (

FileChannel.MapMode.READ_WRITE

) then invoking this
method has no effect.

---

