# Interface GatheringByteChannel

**Source:** `java.base\java\nio\channels\GatheringByteChannel.html`

### Class Description

```java
public interface
GatheringByteChannel

extends
WritableByteChannel
```

A channel that can write bytes from a sequence of buffers.

A

gathering

write operation writes, in a single invocation, a
sequence of bytes from one or more of a given sequence of buffers.
Gathering writes are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

scattering

read operations are defined in the

ScatteringByteChannel

interface.

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

,

WritableByteChannel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

An attempt is made to write up to

r

bytes to this channel,
where

r

is the total number of bytes remaining in the specified
subsequence of the given buffer array, that is,

```java
srcs[offset].remaining()
+ srcs[offset+1].remaining()
+ ... + srcs[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
Up to the first

srcs[offset].remaining()

bytes of this sequence
are written from buffer

srcs[offset]

, up to the next

srcs[offset+1].remaining()

bytes are written from buffer

srcs[offset+1]

, and so forth, until the entire byte sequence is
written. As many bytes as possible are written from each buffer, hence
the final position of each updated buffer, except the last updated
buffer, is guaranteed to be equal to that buffer's limit.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:**
- srcs

- The buffers from which bytes are to be retrieved
- offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; must be non-negative and no
larger than

srcs.length
- length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

srcs.length

-

offset

**Returns:**
- The number of bytes written, possibly zero

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
- NonWritableChannelException

- If this channel was not opened for writing
- ClosedChannelException

- If this channel is closed
- AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
- ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
- IOException

- If some other I/O error occurs

---

#### long write​(
ByteBuffer
[] srcs)
throws
IOException

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

**Parameters:**
- srcs

- The buffers from which bytes are to be retrieved

**Returns:**
- The number of bytes written, possibly zero

**Throws:**
- NonWritableChannelException

- If this channel was not opened for writing
- ClosedChannelException

- If this channel is closed
- AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
- ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
- IOException

- If some other I/O error occurs

---

### Additional Sections

#### Interface GatheringByteChannel

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

,

WritableByteChannel

**All Known Implementing Classes:** DatagramChannel

,

FileChannel

,

Pipe.SinkChannel

,

SocketChannel

```java
public interface
GatheringByteChannel

extends
WritableByteChannel
```

A channel that can write bytes from a sequence of buffers.

A

gathering

write operation writes, in a single invocation, a
sequence of bytes from one or more of a given sequence of buffers.
Gathering writes are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

scattering

read operations are defined in the

ScatteringByteChannel

interface.

**Since:** 1.4

public interface

GatheringByteChannel

extends

WritableByteChannel

A channel that can write bytes from a sequence of buffers.

A

gathering

write operation writes, in a single invocation, a
sequence of bytes from one or more of a given sequence of buffers.
Gathering writes are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

scattering

read operations are defined in the

ScatteringByteChannel

interface.

A

gathering

write operation writes, in a single invocation, a
sequence of bytes from one or more of a given sequence of buffers.
Gathering writes are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

scattering

read operations are defined in the

ScatteringByteChannel

interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

write

​(

ByteBuffer

[] srcs)

Writes a sequence of bytes to this channel from the given buffers.

long

write

​(

ByteBuffer

[] srcs,
int offset,
int length)

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

- Methods declared in interface java.nio.channels.

WritableByteChannel

write

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

write

​(

ByteBuffer

[] srcs)

Writes a sequence of bytes to this channel from the given buffers.

long

write

​(

ByteBuffer

[] srcs,
int offset,
int length)

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

- Methods declared in interface java.nio.channels.

WritableByteChannel

write

---

#### Method Summary

Writes a sequence of bytes to this channel from the given buffers.

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

---

#### Methods declared in interface java.nio.channels. Channel

Methods declared in interface java.nio.channels.

WritableByteChannel

write

---

#### Methods declared in interface java.nio.channels. WritableByteChannel

============ METHOD DETAIL ==========

- Method Detail

- write

```java
long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException
```

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

An attempt is made to write up to

r

bytes to this channel,
where

r

is the total number of bytes remaining in the specified
subsequence of the given buffer array, that is,

```java
srcs[offset].remaining()
+ srcs[offset+1].remaining()
+ ... + srcs[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
Up to the first

srcs[offset].remaining()

bytes of this sequence
are written from buffer

srcs[offset]

, up to the next

srcs[offset+1].remaining()

bytes are written from buffer

srcs[offset+1]

, and so forth, until the entire byte sequence is
written. As many bytes as possible are written from each buffer, hence
the final position of each updated buffer, except the last updated
buffer, is guaranteed to be equal to that buffer's limit.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; must be non-negative and no
larger than

srcs.length
**Parameters:** length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

srcs.length

-

offset
**Returns:** The number of bytes written, possibly zero
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** NonWritableChannelException

- If this channel was not opened for writing
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

- write

```java
long write​(
ByteBuffer
[] srcs)
throws
IOException
```

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NonWritableChannelException

- If this channel was not opened for writing
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

Method Detail

- write

```java
long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException
```

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

An attempt is made to write up to

r

bytes to this channel,
where

r

is the total number of bytes remaining in the specified
subsequence of the given buffer array, that is,

```java
srcs[offset].remaining()
+ srcs[offset+1].remaining()
+ ... + srcs[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
Up to the first

srcs[offset].remaining()

bytes of this sequence
are written from buffer

srcs[offset]

, up to the next

srcs[offset+1].remaining()

bytes are written from buffer

srcs[offset+1]

, and so forth, until the entire byte sequence is
written. As many bytes as possible are written from each buffer, hence
the final position of each updated buffer, except the last updated
buffer, is guaranteed to be equal to that buffer's limit.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; must be non-negative and no
larger than

srcs.length
**Parameters:** length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

srcs.length

-

offset
**Returns:** The number of bytes written, possibly zero
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** NonWritableChannelException

- If this channel was not opened for writing
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

- write

```java
long write​(
ByteBuffer
[] srcs)
throws
IOException
```

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NonWritableChannelException

- If this channel was not opened for writing
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

---

#### Method Detail

write

```java
long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException
```

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

An attempt is made to write up to

r

bytes to this channel,
where

r

is the total number of bytes remaining in the specified
subsequence of the given buffer array, that is,

```java
srcs[offset].remaining()
+ srcs[offset+1].remaining()
+ ... + srcs[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
Up to the first

srcs[offset].remaining()

bytes of this sequence
are written from buffer

srcs[offset]

, up to the next

srcs[offset+1].remaining()

bytes are written from buffer

srcs[offset+1]

, and so forth, until the entire byte sequence is
written. As many bytes as possible are written from each buffer, hence
the final position of each updated buffer, except the last updated
buffer, is guaranteed to be equal to that buffer's limit.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; must be non-negative and no
larger than

srcs.length
**Parameters:** length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

srcs.length

-

offset
**Returns:** The number of bytes written, possibly zero
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** NonWritableChannelException

- If this channel was not opened for writing
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

---

#### write

long write​(

ByteBuffer

[] srcs,
int offset,
int length)
throws

IOException

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

An attempt is made to write up to

r

bytes to this channel,
where

r

is the total number of bytes remaining in the specified
subsequence of the given buffer array, that is,

```java
srcs[offset].remaining()
+ srcs[offset+1].remaining()
+ ... + srcs[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
Up to the first

srcs[offset].remaining()

bytes of this sequence
are written from buffer

srcs[offset]

, up to the next

srcs[offset+1].remaining()

bytes are written from buffer

srcs[offset+1]

, and so forth, until the entire byte sequence is
written. As many bytes as possible are written from each buffer, hence
the final position of each updated buffer, except the last updated
buffer, is guaranteed to be equal to that buffer's limit.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

An attempt is made to write up to

r

bytes to this channel,
where

r

is the total number of bytes remaining in the specified
subsequence of the given buffer array, that is,

```java
srcs[offset].remaining()
+ srcs[offset+1].remaining()
+ ... + srcs[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
Up to the first

srcs[offset].remaining()

bytes of this sequence
are written from buffer

srcs[offset]

, up to the next

srcs[offset+1].remaining()

bytes are written from buffer

srcs[offset+1]

, and so forth, until the entire byte sequence is
written. As many bytes as possible are written from each buffer, hence
the final position of each updated buffer, except the last updated
buffer, is guaranteed to be equal to that buffer's limit.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

srcs[offset].remaining()
+ srcs[offset+1].remaining()
+ ... + srcs[offset+length-1].remaining()

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
Up to the first

srcs[offset].remaining()

bytes of this sequence
are written from buffer

srcs[offset]

, up to the next

srcs[offset+1].remaining()

bytes are written from buffer

srcs[offset+1]

, and so forth, until the entire byte sequence is
written. As many bytes as possible are written from each buffer, hence
the final position of each updated buffer, except the last updated
buffer, is guaranteed to be equal to that buffer's limit.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

Unless otherwise specified, a write operation will return only after
writing all of the

r

requested bytes. Some types of channels,
depending upon their state, may write only some of the bytes or possibly
none at all. A socket channel in non-blocking mode, for example, cannot
write any more bytes than are free in the socket's output buffer.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

This method may be invoked at any time. If another thread has
already initiated a write operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

write

```java
long write​(
ByteBuffer
[] srcs)
throws
IOException
```

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NonWritableChannelException

- If this channel was not opened for writing
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the write operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the write operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

---

#### write

long write​(

ByteBuffer

[] srcs)
throws

IOException

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

c.write(srcs, 0, srcs.length);

---

