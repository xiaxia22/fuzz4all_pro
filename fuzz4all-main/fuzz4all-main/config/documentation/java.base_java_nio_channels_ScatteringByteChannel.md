# Interface ScatteringByteChannel

**Source:** `java.base\java\nio\channels\ScatteringByteChannel.html`

### Class Description

```java
public interface
ScatteringByteChannel

extends
ReadableByteChannel
```

A channel that can read bytes into a sequence of buffers.

A

scattering

read operation reads, in a single invocation, a
sequence of bytes into one or more of a given sequence of buffers.
Scattering reads are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

gathering

write operations are defined in the

GatheringByteChannel

interface.

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

,

ReadableByteChannel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

An invocation of this method attempts to read up to

r

bytes
from this channel, where

r

is the total number of bytes remaining
the specified subsequence of the given buffer array, that is,

```java
dsts[offset].remaining()
+ dsts[offset+1].remaining()
+ ... + dsts[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
Up to the first

dsts[offset].remaining()

bytes of this sequence
are transferred into buffer

dsts[offset]

, up to the next

dsts[offset+1].remaining()

bytes are transferred into buffer

dsts[offset+1]

, and so forth, until the entire byte sequence
is transferred into the given buffers. As many bytes as possible are
transferred into each buffer, hence the final position of each updated
buffer, except the last updated buffer, is guaranteed to be equal to
that buffer's limit.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:**
- dsts

- The buffers into which bytes are to be transferred
- offset

- The offset within the buffer array of the first buffer into
which bytes are to be transferred; must be non-negative and no
larger than

dsts.length
- length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

dsts.length

-

offset

**Returns:**
- The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream

**Throws:**
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
- NonReadableChannelException

- If this channel was not opened for reading
- ClosedChannelException

- If this channel is closed
- AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
- ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
- IOException

- If some other I/O error occurs

---

#### long read​(
ByteBuffer
[] dsts)
throws
IOException

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

**Parameters:**
- dsts

- The buffers into which bytes are to be transferred

**Returns:**
- The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream

**Throws:**
- NonReadableChannelException

- If this channel was not opened for reading
- ClosedChannelException

- If this channel is closed
- AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
- ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
- IOException

- If some other I/O error occurs

---

### Additional Sections

#### Interface ScatteringByteChannel

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

,

ReadableByteChannel

**All Known Implementing Classes:** DatagramChannel

,

FileChannel

,

Pipe.SourceChannel

,

SocketChannel

```java
public interface
ScatteringByteChannel

extends
ReadableByteChannel
```

A channel that can read bytes into a sequence of buffers.

A

scattering

read operation reads, in a single invocation, a
sequence of bytes into one or more of a given sequence of buffers.
Scattering reads are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

gathering

write operations are defined in the

GatheringByteChannel

interface.

**Since:** 1.4

public interface

ScatteringByteChannel

extends

ReadableByteChannel

A channel that can read bytes into a sequence of buffers.

A

scattering

read operation reads, in a single invocation, a
sequence of bytes into one or more of a given sequence of buffers.
Scattering reads are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

gathering

write operations are defined in the

GatheringByteChannel

interface.

A

scattering

read operation reads, in a single invocation, a
sequence of bytes into one or more of a given sequence of buffers.
Scattering reads are often useful when implementing network protocols or
file formats that, for example, group data into segments consisting of one
or more fixed-length headers followed by a variable-length body. Similar

gathering

write operations are defined in the

GatheringByteChannel

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

read

​(

ByteBuffer

[] dsts)

Reads a sequence of bytes from this channel into the given buffers.

long

read

​(

ByteBuffer

[] dsts,
int offset,
int length)

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

- Methods declared in interface java.nio.channels.

ReadableByteChannel

read

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

read

​(

ByteBuffer

[] dsts)

Reads a sequence of bytes from this channel into the given buffers.

long

read

​(

ByteBuffer

[] dsts,
int offset,
int length)

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

- Methods declared in interface java.nio.channels.

ReadableByteChannel

read

---

#### Method Summary

Reads a sequence of bytes from this channel into the given buffers.

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

---

#### Methods declared in interface java.nio.channels. Channel

Methods declared in interface java.nio.channels.

ReadableByteChannel

read

---

#### Methods declared in interface java.nio.channels. ReadableByteChannel

============ METHOD DETAIL ==========

- Method Detail

- read

```java
long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException
```

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

An invocation of this method attempts to read up to

r

bytes
from this channel, where

r

is the total number of bytes remaining
the specified subsequence of the given buffer array, that is,

```java
dsts[offset].remaining()
+ dsts[offset+1].remaining()
+ ... + dsts[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
Up to the first

dsts[offset].remaining()

bytes of this sequence
are transferred into buffer

dsts[offset]

, up to the next

dsts[offset+1].remaining()

bytes are transferred into buffer

dsts[offset+1]

, and so forth, until the entire byte sequence
is transferred into the given buffers. As many bytes as possible are
transferred into each buffer, hence the final position of each updated
buffer, except the last updated buffer, is guaranteed to be equal to
that buffer's limit.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Parameters:** offset

- The offset within the buffer array of the first buffer into
which bytes are to be transferred; must be non-negative and no
larger than

dsts.length
**Parameters:** length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

dsts.length

-

offset
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** NonReadableChannelException

- If this channel was not opened for reading
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

- read

```java
long read​(
ByteBuffer
[] dsts)
throws
IOException
```

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** NonReadableChannelException

- If this channel was not opened for reading
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

Method Detail

- read

```java
long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException
```

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

An invocation of this method attempts to read up to

r

bytes
from this channel, where

r

is the total number of bytes remaining
the specified subsequence of the given buffer array, that is,

```java
dsts[offset].remaining()
+ dsts[offset+1].remaining()
+ ... + dsts[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
Up to the first

dsts[offset].remaining()

bytes of this sequence
are transferred into buffer

dsts[offset]

, up to the next

dsts[offset+1].remaining()

bytes are transferred into buffer

dsts[offset+1]

, and so forth, until the entire byte sequence
is transferred into the given buffers. As many bytes as possible are
transferred into each buffer, hence the final position of each updated
buffer, except the last updated buffer, is guaranteed to be equal to
that buffer's limit.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Parameters:** offset

- The offset within the buffer array of the first buffer into
which bytes are to be transferred; must be non-negative and no
larger than

dsts.length
**Parameters:** length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

dsts.length

-

offset
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** NonReadableChannelException

- If this channel was not opened for reading
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

- read

```java
long read​(
ByteBuffer
[] dsts)
throws
IOException
```

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** NonReadableChannelException

- If this channel was not opened for reading
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

---

#### Method Detail

read

```java
long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException
```

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

An invocation of this method attempts to read up to

r

bytes
from this channel, where

r

is the total number of bytes remaining
the specified subsequence of the given buffer array, that is,

```java
dsts[offset].remaining()
+ dsts[offset+1].remaining()
+ ... + dsts[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
Up to the first

dsts[offset].remaining()

bytes of this sequence
are transferred into buffer

dsts[offset]

, up to the next

dsts[offset+1].remaining()

bytes are transferred into buffer

dsts[offset+1]

, and so forth, until the entire byte sequence
is transferred into the given buffers. As many bytes as possible are
transferred into each buffer, hence the final position of each updated
buffer, except the last updated buffer, is guaranteed to be equal to
that buffer's limit.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Parameters:** offset

- The offset within the buffer array of the first buffer into
which bytes are to be transferred; must be non-negative and no
larger than

dsts.length
**Parameters:** length

- The maximum number of buffers to be accessed; must be
non-negative and no larger than

dsts.length

-

offset
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold
**Throws:** NonReadableChannelException

- If this channel was not opened for reading
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

---

#### read

long read​(

ByteBuffer

[] dsts,
int offset,
int length)
throws

IOException

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

An invocation of this method attempts to read up to

r

bytes
from this channel, where

r

is the total number of bytes remaining
the specified subsequence of the given buffer array, that is,

```java
dsts[offset].remaining()
+ dsts[offset+1].remaining()
+ ... + dsts[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
Up to the first

dsts[offset].remaining()

bytes of this sequence
are transferred into buffer

dsts[offset]

, up to the next

dsts[offset+1].remaining()

bytes are transferred into buffer

dsts[offset+1]

, and so forth, until the entire byte sequence
is transferred into the given buffers. As many bytes as possible are
transferred into each buffer, hence the final position of each updated
buffer, except the last updated buffer, is guaranteed to be equal to
that buffer's limit.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

An invocation of this method attempts to read up to

r

bytes
from this channel, where

r

is the total number of bytes remaining
the specified subsequence of the given buffer array, that is,

```java
dsts[offset].remaining()
+ dsts[offset+1].remaining()
+ ... + dsts[offset+length-1].remaining()
```

at the moment that this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
Up to the first

dsts[offset].remaining()

bytes of this sequence
are transferred into buffer

dsts[offset]

, up to the next

dsts[offset+1].remaining()

bytes are transferred into buffer

dsts[offset+1]

, and so forth, until the entire byte sequence
is transferred into the given buffers. As many bytes as possible are
transferred into each buffer, hence the final position of each updated
buffer, except the last updated buffer, is guaranteed to be equal to
that buffer's limit.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

dsts[offset].remaining()
+ dsts[offset+1].remaining()
+ ... + dsts[offset+length-1].remaining()

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
Up to the first

dsts[offset].remaining()

bytes of this sequence
are transferred into buffer

dsts[offset]

, up to the next

dsts[offset+1].remaining()

bytes are transferred into buffer

dsts[offset+1]

, and so forth, until the entire byte sequence
is transferred into the given buffers. As many bytes as possible are
transferred into each buffer, hence the final position of each updated
buffer, except the last updated buffer, is guaranteed to be equal to
that buffer's limit.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

read

```java
long read​(
ByteBuffer
[] dsts)
throws
IOException
```

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** NonReadableChannelException

- If this channel was not opened for reading
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the read operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the read operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

---

#### read

long read​(

ByteBuffer

[] dsts)
throws

IOException

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

c.read(dsts, 0, dsts.length);

---

