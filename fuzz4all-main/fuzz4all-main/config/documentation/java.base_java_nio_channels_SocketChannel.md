# Class SocketChannel

**Source:** `java.base\java\nio\channels\SocketChannel.html`

### Class Description

```java
public abstract class
SocketChannel

extends
AbstractSelectableChannel

implements
ByteChannel
,
ScatteringByteChannel
,
GatheringByteChannel
,
NetworkChannel
```

A selectable channel for stream-oriented connecting sockets.

A socket channel is created by invoking one of the

open

methods of this class. It is not possible to create a channel for an arbitrary,
pre-existing socket. A newly-created socket channel is open but not yet
connected. An attempt to invoke an I/O operation upon an unconnected
channel will cause a

NotYetConnectedException

to be thrown. A
socket channel can be connected by invoking its

connect

method; once connected, a socket channel remains connected until it is
closed. Whether or not a socket channel is connected may be determined by
invoking its

isConnected

method.

Socket channels support

non-blocking connection:

A socket
channel may be created and the process of establishing the link to the
remote socket may be initiated via the

connect

method for
later completion by the

finishConnect

method.
Whether or not a connection operation is in progress may be determined by
invoking the

isConnectionPending

method.

Socket channels support

asynchronous shutdown,

which is similar
to the asynchronous close operation specified in the

Channel

class.
If the input side of a socket is shut down by one thread while another
thread is blocked in a read operation on the socket's channel, then the read
operation in the blocked thread will complete without reading any bytes and
will return

-1

. If the output side of a socket is shut down by one
thread while another thread is blocked in a write operation on the socket's
channel, then the blocked thread will receive an

AsynchronousCloseException

.

Socket options are configured using the

setOption

method. Socket channels support the following options:

Socket options

Option Name

Description

SO_SNDBUF

The size of the socket send buffer

SO_RCVBUF

The size of the socket receive buffer

SO_KEEPALIVE

Keep connection alive

SO_REUSEADDR

Re-use address

SO_LINGER

Linger on close if data is present (when configured in blocking mode
only)

TCP_NODELAY

Disable the Nagle algorithm

Additional (implementation specific) options may also be supported.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

ByteChannel

,

Channel

,

GatheringByteChannel

,

InterruptibleChannel

,

NetworkChannel

,

ReadableByteChannel

,

ScatteringByteChannel

,

WritableByteChannel

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SocketChannel​(
SelectorProvider
provider)

Initializes a new instance of this class.

**Parameters:**
- provider

- The provider that created this channel

---

### Method Details

#### public static
SocketChannel
open()
throws
IOException

Opens a socket channel.

The new channel is created by invoking the

openSocketChannel

method of the system-wide default

SelectorProvider

object.

**Returns:**
- A new socket channel

**Throws:**
- IOException

- If an I/O error occurs

---

#### public static
SocketChannel
open​(
SocketAddress
remote)
throws
IOException

Opens a socket channel and connects it to a remote address.

This convenience method works as if by invoking the

open()

method, invoking the

connect

method upon
the resulting socket channel, passing it

remote

, and then
returning that channel.

**Parameters:**
- remote

- The remote address to which the new channel is to be connected

**Returns:**
- A new, and connected, socket channel

**Throws:**
- AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
- ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
- UnresolvedAddressException

- If the given remote address is not fully resolved
- UnsupportedAddressTypeException

- If the type of the given remote address is not supported
- SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
- IOException

- If some other I/O error occurs

---

#### public final int validOps()

Returns an operation set identifying this channel's supported
operations.

Socket channels support connecting, reading, and writing, so this
method returns

(

SelectionKey.OP_CONNECT

|

SelectionKey.OP_READ

|

SelectionKey.OP_WRITE

)

.

**Specified by:**
- validOps

in class

SelectableChannel

**Returns:**
- The valid-operation set

---

#### public abstract
SocketChannel
bind​(
SocketAddress
local)
throws
IOException

Description copied from interface:

NetworkChannel

**Specified by:**
- bind

in interface

NetworkChannel

**Parameters:**
- local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address

**Returns:**
- This channel

**Throws:**
- ConnectionPendingException

- If a non-blocking connect operation is already in progress on
this channel
- AlreadyBoundException

- If the socket is already bound
- UnsupportedAddressTypeException

- If the type of the given address is not supported
- ClosedChannelException

- If the channel is closed
- IOException

- If some other I/O error occurs
- SecurityException

- If a security manager has been installed and its

checkListen

method denies
the operation

**See Also:**
- NetworkChannel.getLocalAddress()

**Since:**
- 1.7

---

#### public abstract <T>
SocketChannel
setOption​(
SocketOption
<T> name,
T value)
throws
IOException

Description copied from interface:

NetworkChannel

**Specified by:**
- setOption

in interface

NetworkChannel

**Parameters:**
- name

- The socket option
- value

- The value of the socket option. A value of

null

may be
a valid value for some socket options.

**Returns:**
- This channel

**Throws:**
- UnsupportedOperationException

- If the socket option is not supported by this channel
- IllegalArgumentException

- If the value is not a valid value for this socket option
- ClosedChannelException

- If this channel is closed
- IOException

- If an I/O error occurs

**See Also:**
- StandardSocketOptions

**Since:**
- 1.7

**Type Parameters:**
- T

- The type of the socket option value

---

#### public abstract
SocketChannel
shutdownInput()
throws
IOException

Shutdown the connection for reading without closing the channel.

Once shutdown for reading then further reads on the channel will
return

-1

, the end-of-stream indication. If the input side of the
connection is already shutdown then invoking this method has no effect.

**Returns:**
- The channel

**Throws:**
- NotYetConnectedException

- If this channel is not yet connected
- ClosedChannelException

- If this channel is closed
- IOException

- If some other I/O error occurs

**Since:**
- 1.7

---

#### public abstract
SocketChannel
shutdownOutput()
throws
IOException

Shutdown the connection for writing without closing the channel.

Once shutdown for writing then further attempts to write to the
channel will throw

ClosedChannelException

. If the output side of
the connection is already shutdown then invoking this method has no
effect.

**Returns:**
- The channel

**Throws:**
- NotYetConnectedException

- If this channel is not yet connected
- ClosedChannelException

- If this channel is closed
- IOException

- If some other I/O error occurs

**Since:**
- 1.7

---

#### public abstract
Socket
socket()

Retrieves a socket associated with this channel.

The returned object will not declare any public methods that are not
declared in the

Socket

class.

**Returns:**
- A socket associated with this channel

---

#### public abstract boolean isConnected()

Tells whether or not this channel's network socket is connected.

**Returns:**
- true

if, and only if, this channel's network socket
is

open

and connected

---

#### public abstract boolean isConnectionPending()

Tells whether or not a connection operation is in progress on this
channel.

**Returns:**
- true

if, and only if, a connection operation has been
initiated on this channel but not yet completed by invoking the

finishConnect

method

---

#### public abstract boolean connect​(
SocketAddress
remote)
throws
IOException

Connects this channel's socket.

If this channel is in non-blocking mode then an invocation of this
method initiates a non-blocking connection operation. If the connection
is established immediately, as can happen with a local connection, then
this method returns

true

. Otherwise this method returns

false

and the connection operation must later be completed by
invoking the

finishConnect

method.

If this channel is in blocking mode then an invocation of this
method will block until the connection is established or an I/O error
occurs.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

**Parameters:**
- remote

- The remote address to which this channel is to be connected

**Returns:**
- true

if a connection was established,

false

if this channel is in non-blocking mode
and the connection operation is in progress

**Throws:**
- AlreadyConnectedException

- If this channel is already connected
- ConnectionPendingException

- If a non-blocking connection operation is already in progress
on this channel
- ClosedChannelException

- If this channel is closed
- AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
- ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
- UnresolvedAddressException

- If the given remote address is not fully resolved
- UnsupportedAddressTypeException

- If the type of the given remote address is not supported
- SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
- IOException

- If some other I/O error occurs

---

#### public abstract boolean finishConnect()
throws
IOException

Finishes the process of connecting a socket channel.

A non-blocking connection operation is initiated by placing a socket
channel in non-blocking mode and then invoking its

connect

method. Once the connection is established, or the attempt has
failed, the socket channel will become connectable and this method may
be invoked to complete the connection sequence. If the connection
operation failed then invoking this method will cause an appropriate

IOException

to be thrown.

If this channel is already connected then this method will not block
and will immediately return

true

. If this channel is in
non-blocking mode then this method will return

false

if the
connection process is not yet complete. If this channel is in blocking
mode then this method will block until the connection either completes
or fails, and will always either return

true

or throw a checked
exception describing the failure.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

**Returns:**
- true

if, and only if, this channel's socket is now
connected

**Throws:**
- NoConnectionPendingException

- If this channel is not connected and a connection operation
has not been initiated
- ClosedChannelException

- If this channel is closed
- AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
- ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
- IOException

- If some other I/O error occurs

---

#### public abstract
SocketAddress
getRemoteAddress()
throws
IOException

Returns the remote address to which this channel's socket is connected.

Where the channel is bound and connected to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

**Returns:**
- The remote address;

null

if the channel's socket is not
connected

**Throws:**
- ClosedChannelException

- If the channel is closed
- IOException

- If an I/O error occurs

**Since:**
- 1.7

---

#### public abstract int read​(
ByteBuffer
dst)
throws
IOException

Description copied from interface:

ReadableByteChannel

**Specified by:**
- read

in interface

ReadableByteChannel

**Parameters:**
- dst

- The buffer into which bytes are to be transferred

**Returns:**
- The number of bytes read, possibly zero, or

-1

if the
channel has reached end-of-stream

**Throws:**
- NotYetConnectedException

- If this channel is not yet connected
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

#### public abstract long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException

Description copied from interface:

ScatteringByteChannel

**Specified by:**
- read

in interface

ScatteringByteChannel

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
- NotYetConnectedException

- If this channel is not yet connected
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

#### public final long read​(
ByteBuffer
[] dsts)
throws
IOException

Description copied from interface:

ScatteringByteChannel

**Specified by:**
- read

in interface

ScatteringByteChannel

**Parameters:**
- dsts

- The buffers into which bytes are to be transferred

**Returns:**
- The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream

**Throws:**
- NotYetConnectedException

- If this channel is not yet connected
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

#### public abstract int write​(
ByteBuffer
src)
throws
IOException

Description copied from interface:

WritableByteChannel

**Specified by:**
- write

in interface

WritableByteChannel

**Parameters:**
- src

- The buffer from which bytes are to be retrieved

**Returns:**
- The number of bytes written, possibly zero

**Throws:**
- NotYetConnectedException

- If this channel is not yet connected
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

#### public abstract long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException

Description copied from interface:

GatheringByteChannel

**Specified by:**
- write

in interface

GatheringByteChannel

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
- NotYetConnectedException

- If this channel is not yet connected
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

#### public final long write​(
ByteBuffer
[] srcs)
throws
IOException

Description copied from interface:

GatheringByteChannel

**Specified by:**
- write

in interface

GatheringByteChannel

**Parameters:**
- srcs

- The buffers from which bytes are to be retrieved

**Returns:**
- The number of bytes written, possibly zero

**Throws:**
- NotYetConnectedException

- If this channel is not yet connected
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

#### public abstract
SocketAddress
getLocalAddress()
throws
IOException

Returns the socket address that this channel's socket is bound to.

Where the channel is

bound

to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
a

SocketAddress

representing the

loopback

address and the
local port of the channel's socket is returned.

**Specified by:**
- getLocalAddress

in interface

NetworkChannel

**Returns:**
- The

SocketAddress

that the socket is bound to, or the

SocketAddress

representing the loopback address if
denied by the security manager, or

null

if the
channel's socket is not bound

**Throws:**
- ClosedChannelException

- If the channel is closed
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class SocketChannel

java.lang.Object

- java.nio.channels.spi.AbstractInterruptibleChannel
- - java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.SocketChannel

java.nio.channels.spi.AbstractInterruptibleChannel

- java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.SocketChannel

java.nio.channels.SelectableChannel

- java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.SocketChannel

java.nio.channels.spi.AbstractSelectableChannel

- java.nio.channels.SocketChannel

java.nio.channels.SocketChannel

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

ByteChannel

,

Channel

,

GatheringByteChannel

,

InterruptibleChannel

,

NetworkChannel

,

ReadableByteChannel

,

ScatteringByteChannel

,

WritableByteChannel

```java
public abstract class
SocketChannel

extends
AbstractSelectableChannel

implements
ByteChannel
,
ScatteringByteChannel
,
GatheringByteChannel
,
NetworkChannel
```

A selectable channel for stream-oriented connecting sockets.

A socket channel is created by invoking one of the

open

methods of this class. It is not possible to create a channel for an arbitrary,
pre-existing socket. A newly-created socket channel is open but not yet
connected. An attempt to invoke an I/O operation upon an unconnected
channel will cause a

NotYetConnectedException

to be thrown. A
socket channel can be connected by invoking its

connect

method; once connected, a socket channel remains connected until it is
closed. Whether or not a socket channel is connected may be determined by
invoking its

isConnected

method.

Socket channels support

non-blocking connection:

A socket
channel may be created and the process of establishing the link to the
remote socket may be initiated via the

connect

method for
later completion by the

finishConnect

method.
Whether or not a connection operation is in progress may be determined by
invoking the

isConnectionPending

method.

Socket channels support

asynchronous shutdown,

which is similar
to the asynchronous close operation specified in the

Channel

class.
If the input side of a socket is shut down by one thread while another
thread is blocked in a read operation on the socket's channel, then the read
operation in the blocked thread will complete without reading any bytes and
will return

-1

. If the output side of a socket is shut down by one
thread while another thread is blocked in a write operation on the socket's
channel, then the blocked thread will receive an

AsynchronousCloseException

.

Socket options are configured using the

setOption

method. Socket channels support the following options:

Socket options

Option Name

Description

SO_SNDBUF

The size of the socket send buffer

SO_RCVBUF

The size of the socket receive buffer

SO_KEEPALIVE

Keep connection alive

SO_REUSEADDR

Re-use address

SO_LINGER

Linger on close if data is present (when configured in blocking mode
only)

TCP_NODELAY

Disable the Nagle algorithm

Additional (implementation specific) options may also be supported.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

**Since:** 1.4

public abstract class

SocketChannel

extends

AbstractSelectableChannel

implements

ByteChannel

,

ScatteringByteChannel

,

GatheringByteChannel

,

NetworkChannel

A selectable channel for stream-oriented connecting sockets.

A socket channel is created by invoking one of the

open

methods of this class. It is not possible to create a channel for an arbitrary,
pre-existing socket. A newly-created socket channel is open but not yet
connected. An attempt to invoke an I/O operation upon an unconnected
channel will cause a

NotYetConnectedException

to be thrown. A
socket channel can be connected by invoking its

connect

method; once connected, a socket channel remains connected until it is
closed. Whether or not a socket channel is connected may be determined by
invoking its

isConnected

method.

Socket channels support

non-blocking connection:

A socket
channel may be created and the process of establishing the link to the
remote socket may be initiated via the

connect

method for
later completion by the

finishConnect

method.
Whether or not a connection operation is in progress may be determined by
invoking the

isConnectionPending

method.

Socket channels support

asynchronous shutdown,

which is similar
to the asynchronous close operation specified in the

Channel

class.
If the input side of a socket is shut down by one thread while another
thread is blocked in a read operation on the socket's channel, then the read
operation in the blocked thread will complete without reading any bytes and
will return

-1

. If the output side of a socket is shut down by one
thread while another thread is blocked in a write operation on the socket's
channel, then the blocked thread will receive an

AsynchronousCloseException

.

Socket options are configured using the

setOption

method. Socket channels support the following options:

Socket options

Option Name

Description

SO_SNDBUF

The size of the socket send buffer

SO_RCVBUF

The size of the socket receive buffer

SO_KEEPALIVE

Keep connection alive

SO_REUSEADDR

Re-use address

SO_LINGER

Linger on close if data is present (when configured in blocking mode
only)

TCP_NODELAY

Disable the Nagle algorithm

Additional (implementation specific) options may also be supported.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

A socket channel is created by invoking one of the

open

methods of this class. It is not possible to create a channel for an arbitrary,
pre-existing socket. A newly-created socket channel is open but not yet
connected. An attempt to invoke an I/O operation upon an unconnected
channel will cause a

NotYetConnectedException

to be thrown. A
socket channel can be connected by invoking its

connect

method; once connected, a socket channel remains connected until it is
closed. Whether or not a socket channel is connected may be determined by
invoking its

isConnected

method.

Socket channels support

non-blocking connection:

A socket
channel may be created and the process of establishing the link to the
remote socket may be initiated via the

connect

method for
later completion by the

finishConnect

method.
Whether or not a connection operation is in progress may be determined by
invoking the

isConnectionPending

method.

Socket channels support

asynchronous shutdown,

which is similar
to the asynchronous close operation specified in the

Channel

class.
If the input side of a socket is shut down by one thread while another
thread is blocked in a read operation on the socket's channel, then the read
operation in the blocked thread will complete without reading any bytes and
will return

-1

. If the output side of a socket is shut down by one
thread while another thread is blocked in a write operation on the socket's
channel, then the blocked thread will receive an

AsynchronousCloseException

.

Socket options are configured using the

setOption

method. Socket channels support the following options:

Socket options

Option Name

Description

SO_SNDBUF

The size of the socket send buffer

SO_RCVBUF

The size of the socket receive buffer

SO_KEEPALIVE

Keep connection alive

SO_REUSEADDR

Re-use address

SO_LINGER

Linger on close if data is present (when configured in blocking mode
only)

TCP_NODELAY

Disable the Nagle algorithm

Additional (implementation specific) options may also be supported.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

Socket channels support

non-blocking connection:

A socket
channel may be created and the process of establishing the link to the
remote socket may be initiated via the

connect

method for
later completion by the

finishConnect

method.
Whether or not a connection operation is in progress may be determined by
invoking the

isConnectionPending

method.

Socket channels support

asynchronous shutdown,

which is similar
to the asynchronous close operation specified in the

Channel

class.
If the input side of a socket is shut down by one thread while another
thread is blocked in a read operation on the socket's channel, then the read
operation in the blocked thread will complete without reading any bytes and
will return

-1

. If the output side of a socket is shut down by one
thread while another thread is blocked in a write operation on the socket's
channel, then the blocked thread will receive an

AsynchronousCloseException

.

Socket options are configured using the

setOption

method. Socket channels support the following options:

Socket options

Option Name

Description

SO_SNDBUF

The size of the socket send buffer

SO_RCVBUF

The size of the socket receive buffer

SO_KEEPALIVE

Keep connection alive

SO_REUSEADDR

Re-use address

SO_LINGER

Linger on close if data is present (when configured in blocking mode
only)

TCP_NODELAY

Disable the Nagle algorithm

Additional (implementation specific) options may also be supported.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

Socket channels support

asynchronous shutdown,

which is similar
to the asynchronous close operation specified in the

Channel

class.
If the input side of a socket is shut down by one thread while another
thread is blocked in a read operation on the socket's channel, then the read
operation in the blocked thread will complete without reading any bytes and
will return

-1

. If the output side of a socket is shut down by one
thread while another thread is blocked in a write operation on the socket's
channel, then the blocked thread will receive an

AsynchronousCloseException

.

Socket options are configured using the

setOption

method. Socket channels support the following options:

Socket options

Option Name

Description

SO_SNDBUF

The size of the socket send buffer

SO_RCVBUF

The size of the socket receive buffer

SO_KEEPALIVE

Keep connection alive

SO_REUSEADDR

Re-use address

SO_LINGER

Linger on close if data is present (when configured in blocking mode
only)

TCP_NODELAY

Disable the Nagle algorithm

Additional (implementation specific) options may also be supported.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

Socket options are configured using the

setOption

method. Socket channels support the following options:

Socket options

Option Name

Description

SO_SNDBUF

The size of the socket send buffer

SO_RCVBUF

The size of the socket receive buffer

SO_KEEPALIVE

Keep connection alive

SO_REUSEADDR

Re-use address

SO_LINGER

Linger on close if data is present (when configured in blocking mode
only)

TCP_NODELAY

Disable the Nagle algorithm

Additional (implementation specific) options may also be supported.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

Socket channels are safe for use by multiple concurrent threads. They
support concurrent reading and writing, though at most one thread may be
reading and at most one thread may be writing at any given time. The

connect

and

finishConnect

methods are
mutually synchronized against each other, and an attempt to initiate a read
or write operation while an invocation of one of these methods is in
progress will block until that invocation is complete.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SocketChannel

​(

SelectorProvider

provider)

Initializes a new instance of this class.

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

abstract

SocketChannel

bind

​(

SocketAddress

local)

Binds the channel's socket to a local address.

abstract boolean

connect

​(

SocketAddress

remote)

Connects this channel's socket.

abstract boolean

finishConnect

()

Finishes the process of connecting a socket channel.

abstract

SocketAddress

getLocalAddress

()

Returns the socket address that this channel's socket is bound to.

abstract

SocketAddress

getRemoteAddress

()

Returns the remote address to which this channel's socket is connected.

abstract boolean

isConnected

()

Tells whether or not this channel's network socket is connected.

abstract boolean

isConnectionPending

()

Tells whether or not a connection operation is in progress on this
channel.

static

SocketChannel

open

()

Opens a socket channel.

static

SocketChannel

open

​(

SocketAddress

remote)

Opens a socket channel and connects it to a remote address.

abstract int

read

​(

ByteBuffer

dst)

Reads a sequence of bytes from this channel into the given buffer.

long

read

​(

ByteBuffer

[] dsts)

Reads a sequence of bytes from this channel into the given buffers.

abstract long

read

​(

ByteBuffer

[] dsts,
int offset,
int length)

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

abstract <T>

SocketChannel

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

abstract

SocketChannel

shutdownInput

()

Shutdown the connection for reading without closing the channel.

abstract

SocketChannel

shutdownOutput

()

Shutdown the connection for writing without closing the channel.

abstract

Socket

socket

()

Retrieves a socket associated with this channel.

int

validOps

()

Returns an operation set identifying this channel's supported
operations.

abstract int

write

​(

ByteBuffer

src)

Writes a sequence of bytes to this channel from the given buffer.

long

write

​(

ByteBuffer

[] srcs)

Writes a sequence of bytes to this channel from the given buffers.

abstract long

write

​(

ByteBuffer

[] srcs,
int offset,
int length)

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

- Methods declared in class java.nio.channels.spi.

AbstractSelectableChannel

configureBlocking

,

implCloseChannel

,

implCloseSelectableChannel

,

implConfigureBlocking

,

provider

,

register

- Methods declared in class java.nio.channels.

SelectableChannel

blockingLock

,

isBlocking

,

isRegistered

,

keyFor

,

register

- Methods declared in class java.nio.channels.spi.

AbstractInterruptibleChannel

begin

,

close

,

end

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

- Methods declared in interface java.nio.channels.

Channel

isOpen

- Methods declared in interface java.nio.channels.

NetworkChannel

getOption

,

supportedOptions

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SocketChannel

​(

SelectorProvider

provider)

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

SocketChannel

bind

​(

SocketAddress

local)

Binds the channel's socket to a local address.

abstract boolean

connect

​(

SocketAddress

remote)

Connects this channel's socket.

abstract boolean

finishConnect

()

Finishes the process of connecting a socket channel.

abstract

SocketAddress

getLocalAddress

()

Returns the socket address that this channel's socket is bound to.

abstract

SocketAddress

getRemoteAddress

()

Returns the remote address to which this channel's socket is connected.

abstract boolean

isConnected

()

Tells whether or not this channel's network socket is connected.

abstract boolean

isConnectionPending

()

Tells whether or not a connection operation is in progress on this
channel.

static

SocketChannel

open

()

Opens a socket channel.

static

SocketChannel

open

​(

SocketAddress

remote)

Opens a socket channel and connects it to a remote address.

abstract int

read

​(

ByteBuffer

dst)

Reads a sequence of bytes from this channel into the given buffer.

long

read

​(

ByteBuffer

[] dsts)

Reads a sequence of bytes from this channel into the given buffers.

abstract long

read

​(

ByteBuffer

[] dsts,
int offset,
int length)

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

abstract <T>

SocketChannel

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

abstract

SocketChannel

shutdownInput

()

Shutdown the connection for reading without closing the channel.

abstract

SocketChannel

shutdownOutput

()

Shutdown the connection for writing without closing the channel.

abstract

Socket

socket

()

Retrieves a socket associated with this channel.

int

validOps

()

Returns an operation set identifying this channel's supported
operations.

abstract int

write

​(

ByteBuffer

src)

Writes a sequence of bytes to this channel from the given buffer.

long

write

​(

ByteBuffer

[] srcs)

Writes a sequence of bytes to this channel from the given buffers.

abstract long

write

​(

ByteBuffer

[] srcs,
int offset,
int length)

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

- Methods declared in class java.nio.channels.spi.

AbstractSelectableChannel

configureBlocking

,

implCloseChannel

,

implCloseSelectableChannel

,

implConfigureBlocking

,

provider

,

register

- Methods declared in class java.nio.channels.

SelectableChannel

blockingLock

,

isBlocking

,

isRegistered

,

keyFor

,

register

- Methods declared in class java.nio.channels.spi.

AbstractInterruptibleChannel

begin

,

close

,

end

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

- Methods declared in interface java.nio.channels.

Channel

isOpen

- Methods declared in interface java.nio.channels.

NetworkChannel

getOption

,

supportedOptions

---

#### Method Summary

Binds the channel's socket to a local address.

Connects this channel's socket.

Finishes the process of connecting a socket channel.

Returns the socket address that this channel's socket is bound to.

Returns the remote address to which this channel's socket is connected.

Tells whether or not this channel's network socket is connected.

Tells whether or not a connection operation is in progress on this
channel.

Opens a socket channel.

Opens a socket channel and connects it to a remote address.

Reads a sequence of bytes from this channel into the given buffer.

Reads a sequence of bytes from this channel into the given buffers.

Reads a sequence of bytes from this channel into a subsequence of the
given buffers.

Sets the value of a socket option.

Shutdown the connection for reading without closing the channel.

Shutdown the connection for writing without closing the channel.

Retrieves a socket associated with this channel.

Returns an operation set identifying this channel's supported
operations.

Writes a sequence of bytes to this channel from the given buffer.

Writes a sequence of bytes to this channel from the given buffers.

Writes a sequence of bytes to this channel from a subsequence of the
given buffers.

Methods declared in class java.nio.channels.spi.

AbstractSelectableChannel

configureBlocking

,

implCloseChannel

,

implCloseSelectableChannel

,

implConfigureBlocking

,

provider

,

register

---

#### Methods declared in class java.nio.channels.spi. AbstractSelectableChannel

Methods declared in class java.nio.channels.

SelectableChannel

blockingLock

,

isBlocking

,

isRegistered

,

keyFor

,

register

---

#### Methods declared in class java.nio.channels. SelectableChannel

Methods declared in class java.nio.channels.spi.

AbstractInterruptibleChannel

begin

,

close

,

end

---

#### Methods declared in class java.nio.channels.spi. AbstractInterruptibleChannel

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

Methods declared in interface java.nio.channels.

Channel

isOpen

---

#### Methods declared in interface java.nio.channels. Channel

Methods declared in interface java.nio.channels.

NetworkChannel

getOption

,

supportedOptions

---

#### Methods declared in interface java.nio.channels. NetworkChannel

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SocketChannel

```java
protected SocketChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this channel

============ METHOD DETAIL ==========

- Method Detail

- open

```java
public static
SocketChannel
open()
throws
IOException
```

Opens a socket channel.

The new channel is created by invoking the

openSocketChannel

method of the system-wide default

SelectorProvider

object.

**Returns:** A new socket channel
**Throws:** IOException

- If an I/O error occurs

- open

```java
public static
SocketChannel
open​(
SocketAddress
remote)
throws
IOException
```

Opens a socket channel and connects it to a remote address.

This convenience method works as if by invoking the

open()

method, invoking the

connect

method upon
the resulting socket channel, passing it

remote

, and then
returning that channel.

**Parameters:** remote

- The remote address to which the new channel is to be connected
**Returns:** A new, and connected, socket channel
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** UnresolvedAddressException

- If the given remote address is not fully resolved
**Throws:** UnsupportedAddressTypeException

- If the type of the given remote address is not supported
**Throws:** SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
**Throws:** IOException

- If some other I/O error occurs

- validOps

```java
public final int validOps()
```

Returns an operation set identifying this channel's supported
operations.

Socket channels support connecting, reading, and writing, so this
method returns

(

SelectionKey.OP_CONNECT

|

SelectionKey.OP_READ

|

SelectionKey.OP_WRITE

)

.

**Specified by:** validOps

in class

SelectableChannel
**Returns:** The valid-operation set

- bind

```java
public abstract
SocketChannel
bind​(
SocketAddress
local)
throws
IOException
```

Description copied from interface:

NetworkChannel

Binds the channel's socket to a local address.

This method is used to establish an association between the socket and
a local address. Once an association is established then the socket remains
bound until the channel is closed. If the

local

parameter has the
value

null

then the socket will be bound to an address that is
assigned automatically.

**Specified by:** bind

in interface

NetworkChannel
**Parameters:** local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address
**Returns:** This channel
**Throws:** ConnectionPendingException

- If a non-blocking connect operation is already in progress on
this channel
**Throws:** AlreadyBoundException

- If the socket is already bound
**Throws:** UnsupportedAddressTypeException

- If the type of the given address is not supported
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Throws:** SecurityException

- If a security manager has been installed and its

checkListen

method denies
the operation
**Since:** 1.7
**See Also:** NetworkChannel.getLocalAddress()

- setOption

```java
public abstract <T>
SocketChannel
setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Description copied from interface:

NetworkChannel

Sets the value of a socket option.

**Specified by:** setOption

in interface

NetworkChannel
**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be
a valid value for some socket options.
**Returns:** This channel
**Throws:** UnsupportedOperationException

- If the socket option is not supported by this channel
**Throws:** IllegalArgumentException

- If the value is not a valid value for this socket option
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7
**See Also:** StandardSocketOptions

- shutdownInput

```java
public abstract
SocketChannel
shutdownInput()
throws
IOException
```

Shutdown the connection for reading without closing the channel.

Once shutdown for reading then further reads on the channel will
return

-1

, the end-of-stream indication. If the input side of the
connection is already shutdown then invoking this method has no effect.

**Returns:** The channel
**Throws:** NotYetConnectedException

- If this channel is not yet connected
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Since:** 1.7

- shutdownOutput

```java
public abstract
SocketChannel
shutdownOutput()
throws
IOException
```

Shutdown the connection for writing without closing the channel.

Once shutdown for writing then further attempts to write to the
channel will throw

ClosedChannelException

. If the output side of
the connection is already shutdown then invoking this method has no
effect.

**Returns:** The channel
**Throws:** NotYetConnectedException

- If this channel is not yet connected
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Since:** 1.7

- socket

```java
public abstract
Socket
socket()
```

Retrieves a socket associated with this channel.

The returned object will not declare any public methods that are not
declared in the

Socket

class.

**Returns:** A socket associated with this channel

- isConnected

```java
public abstract boolean isConnected()
```

Tells whether or not this channel's network socket is connected.

**Returns:** true

if, and only if, this channel's network socket
is

open

and connected

- isConnectionPending

```java
public abstract boolean isConnectionPending()
```

Tells whether or not a connection operation is in progress on this
channel.

**Returns:** true

if, and only if, a connection operation has been
initiated on this channel but not yet completed by invoking the

finishConnect

method

- connect

```java
public abstract boolean connect​(
SocketAddress
remote)
throws
IOException
```

Connects this channel's socket.

If this channel is in non-blocking mode then an invocation of this
method initiates a non-blocking connection operation. If the connection
is established immediately, as can happen with a local connection, then
this method returns

true

. Otherwise this method returns

false

and the connection operation must later be completed by
invoking the

finishConnect

method.

If this channel is in blocking mode then an invocation of this
method will block until the connection is established or an I/O error
occurs.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

**Parameters:** remote

- The remote address to which this channel is to be connected
**Returns:** true

if a connection was established,

false

if this channel is in non-blocking mode
and the connection operation is in progress
**Throws:** AlreadyConnectedException

- If this channel is already connected
**Throws:** ConnectionPendingException

- If a non-blocking connection operation is already in progress
on this channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** UnresolvedAddressException

- If the given remote address is not fully resolved
**Throws:** UnsupportedAddressTypeException

- If the type of the given remote address is not supported
**Throws:** SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
**Throws:** IOException

- If some other I/O error occurs

- finishConnect

```java
public abstract boolean finishConnect()
throws
IOException
```

Finishes the process of connecting a socket channel.

A non-blocking connection operation is initiated by placing a socket
channel in non-blocking mode and then invoking its

connect

method. Once the connection is established, or the attempt has
failed, the socket channel will become connectable and this method may
be invoked to complete the connection sequence. If the connection
operation failed then invoking this method will cause an appropriate

IOException

to be thrown.

If this channel is already connected then this method will not block
and will immediately return

true

. If this channel is in
non-blocking mode then this method will return

false

if the
connection process is not yet complete. If this channel is in blocking
mode then this method will block until the connection either completes
or fails, and will always either return

true

or throw a checked
exception describing the failure.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

**Returns:** true

if, and only if, this channel's socket is now
connected
**Throws:** NoConnectionPendingException

- If this channel is not connected and a connection operation
has not been initiated
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

- getRemoteAddress

```java
public abstract
SocketAddress
getRemoteAddress()
throws
IOException
```

Returns the remote address to which this channel's socket is connected.

Where the channel is bound and connected to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

**Returns:** The remote address;

null

if the channel's socket is not
connected
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7

- read

```java
public abstract int read​(
ByteBuffer
dst)
throws
IOException
```

Description copied from interface:

ReadableByteChannel

Reads a sequence of bytes from this channel into the given buffer.

An attempt is made to read up to

r

bytes from the channel,
where

r

is the number of bytes remaining in the buffer, that is,

dst.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
This byte sequence will be transferred into the buffer so that the first
byte in the sequence is at index

p

and the last byte is at index

p

+

n

-

1

,
where

p

is the buffer's position at the moment this method is
invoked. Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

A read operation might not fill the buffer, and in fact it might not
read any bytes at all. Whether or not it does so depends upon the
nature and state of the channel. A socket channel in non-blocking mode,
for example, cannot read any more bytes than are immediately available
from the socket's input buffer; similarly, a file channel cannot read
any more bytes than remain in the file. It is guaranteed, however, that
if a channel is in blocking mode and there is at least one byte
remaining in the buffer then this method will block until at least one
byte is read.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Specified by:** read

in interface

ReadableByteChannel
**Parameters:** dst

- The buffer into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero, or

-1

if the
channel has reached end-of-stream
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public abstract long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException
```

Description copied from interface:

ScatteringByteChannel

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

**Specified by:** read

in interface

ScatteringByteChannel
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
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public final long read​(
ByteBuffer
[] dsts)
throws
IOException
```

Description copied from interface:

ScatteringByteChannel

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

**Specified by:** read

in interface

ScatteringByteChannel
**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

- write

```java
public abstract int write​(
ByteBuffer
src)
throws
IOException
```

Description copied from interface:

WritableByteChannel

Writes a sequence of bytes to this channel from the given buffer.

An attempt is made to write up to

r

bytes to the channel,
where

r

is the number of bytes remaining in the buffer, that is,

src.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
This byte sequence will be transferred from the buffer starting at index

p

, where

p

is the buffer's position at the moment this
method is invoked; the index of the last byte written will be

p

+

n

-

1

.
Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

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

**Specified by:** write

in interface

WritableByteChannel
**Parameters:** src

- The buffer from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public abstract long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException
```

Description copied from interface:

GatheringByteChannel

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

**Specified by:** write

in interface

GatheringByteChannel
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
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public final long write​(
ByteBuffer
[] srcs)
throws
IOException
```

Description copied from interface:

GatheringByteChannel

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

**Specified by:** write

in interface

GatheringByteChannel
**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

- getLocalAddress

```java
public abstract
SocketAddress
getLocalAddress()
throws
IOException
```

Returns the socket address that this channel's socket is bound to.

Where the channel is

bound

to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
a

SocketAddress

representing the

loopback

address and the
local port of the channel's socket is returned.

**Specified by:** getLocalAddress

in interface

NetworkChannel
**Returns:** The

SocketAddress

that the socket is bound to, or the

SocketAddress

representing the loopback address if
denied by the security manager, or

null

if the
channel's socket is not bound
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs

Constructor Detail

- SocketChannel

```java
protected SocketChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this channel

---

#### Constructor Detail

SocketChannel

```java
protected SocketChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this channel

---

#### SocketChannel

protected SocketChannel​(

SelectorProvider

provider)

Initializes a new instance of this class.

Method Detail

- open

```java
public static
SocketChannel
open()
throws
IOException
```

Opens a socket channel.

The new channel is created by invoking the

openSocketChannel

method of the system-wide default

SelectorProvider

object.

**Returns:** A new socket channel
**Throws:** IOException

- If an I/O error occurs

- open

```java
public static
SocketChannel
open​(
SocketAddress
remote)
throws
IOException
```

Opens a socket channel and connects it to a remote address.

This convenience method works as if by invoking the

open()

method, invoking the

connect

method upon
the resulting socket channel, passing it

remote

, and then
returning that channel.

**Parameters:** remote

- The remote address to which the new channel is to be connected
**Returns:** A new, and connected, socket channel
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** UnresolvedAddressException

- If the given remote address is not fully resolved
**Throws:** UnsupportedAddressTypeException

- If the type of the given remote address is not supported
**Throws:** SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
**Throws:** IOException

- If some other I/O error occurs

- validOps

```java
public final int validOps()
```

Returns an operation set identifying this channel's supported
operations.

Socket channels support connecting, reading, and writing, so this
method returns

(

SelectionKey.OP_CONNECT

|

SelectionKey.OP_READ

|

SelectionKey.OP_WRITE

)

.

**Specified by:** validOps

in class

SelectableChannel
**Returns:** The valid-operation set

- bind

```java
public abstract
SocketChannel
bind​(
SocketAddress
local)
throws
IOException
```

Description copied from interface:

NetworkChannel

Binds the channel's socket to a local address.

This method is used to establish an association between the socket and
a local address. Once an association is established then the socket remains
bound until the channel is closed. If the

local

parameter has the
value

null

then the socket will be bound to an address that is
assigned automatically.

**Specified by:** bind

in interface

NetworkChannel
**Parameters:** local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address
**Returns:** This channel
**Throws:** ConnectionPendingException

- If a non-blocking connect operation is already in progress on
this channel
**Throws:** AlreadyBoundException

- If the socket is already bound
**Throws:** UnsupportedAddressTypeException

- If the type of the given address is not supported
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Throws:** SecurityException

- If a security manager has been installed and its

checkListen

method denies
the operation
**Since:** 1.7
**See Also:** NetworkChannel.getLocalAddress()

- setOption

```java
public abstract <T>
SocketChannel
setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Description copied from interface:

NetworkChannel

Sets the value of a socket option.

**Specified by:** setOption

in interface

NetworkChannel
**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be
a valid value for some socket options.
**Returns:** This channel
**Throws:** UnsupportedOperationException

- If the socket option is not supported by this channel
**Throws:** IllegalArgumentException

- If the value is not a valid value for this socket option
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7
**See Also:** StandardSocketOptions

- shutdownInput

```java
public abstract
SocketChannel
shutdownInput()
throws
IOException
```

Shutdown the connection for reading without closing the channel.

Once shutdown for reading then further reads on the channel will
return

-1

, the end-of-stream indication. If the input side of the
connection is already shutdown then invoking this method has no effect.

**Returns:** The channel
**Throws:** NotYetConnectedException

- If this channel is not yet connected
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Since:** 1.7

- shutdownOutput

```java
public abstract
SocketChannel
shutdownOutput()
throws
IOException
```

Shutdown the connection for writing without closing the channel.

Once shutdown for writing then further attempts to write to the
channel will throw

ClosedChannelException

. If the output side of
the connection is already shutdown then invoking this method has no
effect.

**Returns:** The channel
**Throws:** NotYetConnectedException

- If this channel is not yet connected
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Since:** 1.7

- socket

```java
public abstract
Socket
socket()
```

Retrieves a socket associated with this channel.

The returned object will not declare any public methods that are not
declared in the

Socket

class.

**Returns:** A socket associated with this channel

- isConnected

```java
public abstract boolean isConnected()
```

Tells whether or not this channel's network socket is connected.

**Returns:** true

if, and only if, this channel's network socket
is

open

and connected

- isConnectionPending

```java
public abstract boolean isConnectionPending()
```

Tells whether or not a connection operation is in progress on this
channel.

**Returns:** true

if, and only if, a connection operation has been
initiated on this channel but not yet completed by invoking the

finishConnect

method

- connect

```java
public abstract boolean connect​(
SocketAddress
remote)
throws
IOException
```

Connects this channel's socket.

If this channel is in non-blocking mode then an invocation of this
method initiates a non-blocking connection operation. If the connection
is established immediately, as can happen with a local connection, then
this method returns

true

. Otherwise this method returns

false

and the connection operation must later be completed by
invoking the

finishConnect

method.

If this channel is in blocking mode then an invocation of this
method will block until the connection is established or an I/O error
occurs.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

**Parameters:** remote

- The remote address to which this channel is to be connected
**Returns:** true

if a connection was established,

false

if this channel is in non-blocking mode
and the connection operation is in progress
**Throws:** AlreadyConnectedException

- If this channel is already connected
**Throws:** ConnectionPendingException

- If a non-blocking connection operation is already in progress
on this channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** UnresolvedAddressException

- If the given remote address is not fully resolved
**Throws:** UnsupportedAddressTypeException

- If the type of the given remote address is not supported
**Throws:** SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
**Throws:** IOException

- If some other I/O error occurs

- finishConnect

```java
public abstract boolean finishConnect()
throws
IOException
```

Finishes the process of connecting a socket channel.

A non-blocking connection operation is initiated by placing a socket
channel in non-blocking mode and then invoking its

connect

method. Once the connection is established, or the attempt has
failed, the socket channel will become connectable and this method may
be invoked to complete the connection sequence. If the connection
operation failed then invoking this method will cause an appropriate

IOException

to be thrown.

If this channel is already connected then this method will not block
and will immediately return

true

. If this channel is in
non-blocking mode then this method will return

false

if the
connection process is not yet complete. If this channel is in blocking
mode then this method will block until the connection either completes
or fails, and will always either return

true

or throw a checked
exception describing the failure.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

**Returns:** true

if, and only if, this channel's socket is now
connected
**Throws:** NoConnectionPendingException

- If this channel is not connected and a connection operation
has not been initiated
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

- getRemoteAddress

```java
public abstract
SocketAddress
getRemoteAddress()
throws
IOException
```

Returns the remote address to which this channel's socket is connected.

Where the channel is bound and connected to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

**Returns:** The remote address;

null

if the channel's socket is not
connected
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7

- read

```java
public abstract int read​(
ByteBuffer
dst)
throws
IOException
```

Description copied from interface:

ReadableByteChannel

Reads a sequence of bytes from this channel into the given buffer.

An attempt is made to read up to

r

bytes from the channel,
where

r

is the number of bytes remaining in the buffer, that is,

dst.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
This byte sequence will be transferred into the buffer so that the first
byte in the sequence is at index

p

and the last byte is at index

p

+

n

-

1

,
where

p

is the buffer's position at the moment this method is
invoked. Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

A read operation might not fill the buffer, and in fact it might not
read any bytes at all. Whether or not it does so depends upon the
nature and state of the channel. A socket channel in non-blocking mode,
for example, cannot read any more bytes than are immediately available
from the socket's input buffer; similarly, a file channel cannot read
any more bytes than remain in the file. It is guaranteed, however, that
if a channel is in blocking mode and there is at least one byte
remaining in the buffer then this method will block until at least one
byte is read.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Specified by:** read

in interface

ReadableByteChannel
**Parameters:** dst

- The buffer into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero, or

-1

if the
channel has reached end-of-stream
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public abstract long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException
```

Description copied from interface:

ScatteringByteChannel

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

**Specified by:** read

in interface

ScatteringByteChannel
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
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public final long read​(
ByteBuffer
[] dsts)
throws
IOException
```

Description copied from interface:

ScatteringByteChannel

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

**Specified by:** read

in interface

ScatteringByteChannel
**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

- write

```java
public abstract int write​(
ByteBuffer
src)
throws
IOException
```

Description copied from interface:

WritableByteChannel

Writes a sequence of bytes to this channel from the given buffer.

An attempt is made to write up to

r

bytes to the channel,
where

r

is the number of bytes remaining in the buffer, that is,

src.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
This byte sequence will be transferred from the buffer starting at index

p

, where

p

is the buffer's position at the moment this
method is invoked; the index of the last byte written will be

p

+

n

-

1

.
Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

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

**Specified by:** write

in interface

WritableByteChannel
**Parameters:** src

- The buffer from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public abstract long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException
```

Description copied from interface:

GatheringByteChannel

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

**Specified by:** write

in interface

GatheringByteChannel
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
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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
public final long write​(
ByteBuffer
[] srcs)
throws
IOException
```

Description copied from interface:

GatheringByteChannel

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

**Specified by:** write

in interface

GatheringByteChannel
**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

- getLocalAddress

```java
public abstract
SocketAddress
getLocalAddress()
throws
IOException
```

Returns the socket address that this channel's socket is bound to.

Where the channel is

bound

to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
a

SocketAddress

representing the

loopback

address and the
local port of the channel's socket is returned.

**Specified by:** getLocalAddress

in interface

NetworkChannel
**Returns:** The

SocketAddress

that the socket is bound to, or the

SocketAddress

representing the loopback address if
denied by the security manager, or

null

if the
channel's socket is not bound
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

open

```java
public static
SocketChannel
open()
throws
IOException
```

Opens a socket channel.

The new channel is created by invoking the

openSocketChannel

method of the system-wide default

SelectorProvider

object.

**Returns:** A new socket channel
**Throws:** IOException

- If an I/O error occurs

---

#### open

public static

SocketChannel

open()
throws

IOException

Opens a socket channel.

The new channel is created by invoking the

openSocketChannel

method of the system-wide default

SelectorProvider

object.

The new channel is created by invoking the

openSocketChannel

method of the system-wide default

SelectorProvider

object.

open

```java
public static
SocketChannel
open​(
SocketAddress
remote)
throws
IOException
```

Opens a socket channel and connects it to a remote address.

This convenience method works as if by invoking the

open()

method, invoking the

connect

method upon
the resulting socket channel, passing it

remote

, and then
returning that channel.

**Parameters:** remote

- The remote address to which the new channel is to be connected
**Returns:** A new, and connected, socket channel
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** UnresolvedAddressException

- If the given remote address is not fully resolved
**Throws:** UnsupportedAddressTypeException

- If the type of the given remote address is not supported
**Throws:** SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
**Throws:** IOException

- If some other I/O error occurs

---

#### open

public static

SocketChannel

open​(

SocketAddress

remote)
throws

IOException

Opens a socket channel and connects it to a remote address.

This convenience method works as if by invoking the

open()

method, invoking the

connect

method upon
the resulting socket channel, passing it

remote

, and then
returning that channel.

This convenience method works as if by invoking the

open()

method, invoking the

connect

method upon
the resulting socket channel, passing it

remote

, and then
returning that channel.

validOps

```java
public final int validOps()
```

Returns an operation set identifying this channel's supported
operations.

Socket channels support connecting, reading, and writing, so this
method returns

(

SelectionKey.OP_CONNECT

|

SelectionKey.OP_READ

|

SelectionKey.OP_WRITE

)

.

**Specified by:** validOps

in class

SelectableChannel
**Returns:** The valid-operation set

---

#### validOps

public final int validOps()

Returns an operation set identifying this channel's supported
operations.

Socket channels support connecting, reading, and writing, so this
method returns

(

SelectionKey.OP_CONNECT

|

SelectionKey.OP_READ

|

SelectionKey.OP_WRITE

)

.

Socket channels support connecting, reading, and writing, so this
method returns

(

SelectionKey.OP_CONNECT

|

SelectionKey.OP_READ

|

SelectionKey.OP_WRITE

)

.

bind

```java
public abstract
SocketChannel
bind​(
SocketAddress
local)
throws
IOException
```

Description copied from interface:

NetworkChannel

Binds the channel's socket to a local address.

This method is used to establish an association between the socket and
a local address. Once an association is established then the socket remains
bound until the channel is closed. If the

local

parameter has the
value

null

then the socket will be bound to an address that is
assigned automatically.

**Specified by:** bind

in interface

NetworkChannel
**Parameters:** local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address
**Returns:** This channel
**Throws:** ConnectionPendingException

- If a non-blocking connect operation is already in progress on
this channel
**Throws:** AlreadyBoundException

- If the socket is already bound
**Throws:** UnsupportedAddressTypeException

- If the type of the given address is not supported
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Throws:** SecurityException

- If a security manager has been installed and its

checkListen

method denies
the operation
**Since:** 1.7
**See Also:** NetworkChannel.getLocalAddress()

---

#### bind

public abstract

SocketChannel

bind​(

SocketAddress

local)
throws

IOException

Description copied from interface:

NetworkChannel

Binds the channel's socket to a local address.

This method is used to establish an association between the socket and
a local address. Once an association is established then the socket remains
bound until the channel is closed. If the

local

parameter has the
value

null

then the socket will be bound to an address that is
assigned automatically.

This method is used to establish an association between the socket and
a local address. Once an association is established then the socket remains
bound until the channel is closed. If the

local

parameter has the
value

null

then the socket will be bound to an address that is
assigned automatically.

setOption

```java
public abstract <T>
SocketChannel
setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Description copied from interface:

NetworkChannel

Sets the value of a socket option.

**Specified by:** setOption

in interface

NetworkChannel
**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be
a valid value for some socket options.
**Returns:** This channel
**Throws:** UnsupportedOperationException

- If the socket option is not supported by this channel
**Throws:** IllegalArgumentException

- If the value is not a valid value for this socket option
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7
**See Also:** StandardSocketOptions

---

#### setOption

public abstract <T>

SocketChannel

setOption​(

SocketOption

<T> name,
T value)
throws

IOException

Description copied from interface:

NetworkChannel

Sets the value of a socket option.

shutdownInput

```java
public abstract
SocketChannel
shutdownInput()
throws
IOException
```

Shutdown the connection for reading without closing the channel.

Once shutdown for reading then further reads on the channel will
return

-1

, the end-of-stream indication. If the input side of the
connection is already shutdown then invoking this method has no effect.

**Returns:** The channel
**Throws:** NotYetConnectedException

- If this channel is not yet connected
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Since:** 1.7

---

#### shutdownInput

public abstract

SocketChannel

shutdownInput()
throws

IOException

Shutdown the connection for reading without closing the channel.

Once shutdown for reading then further reads on the channel will
return

-1

, the end-of-stream indication. If the input side of the
connection is already shutdown then invoking this method has no effect.

Once shutdown for reading then further reads on the channel will
return

-1

, the end-of-stream indication. If the input side of the
connection is already shutdown then invoking this method has no effect.

shutdownOutput

```java
public abstract
SocketChannel
shutdownOutput()
throws
IOException
```

Shutdown the connection for writing without closing the channel.

Once shutdown for writing then further attempts to write to the
channel will throw

ClosedChannelException

. If the output side of
the connection is already shutdown then invoking this method has no
effect.

**Returns:** The channel
**Throws:** NotYetConnectedException

- If this channel is not yet connected
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Since:** 1.7

---

#### shutdownOutput

public abstract

SocketChannel

shutdownOutput()
throws

IOException

Shutdown the connection for writing without closing the channel.

Once shutdown for writing then further attempts to write to the
channel will throw

ClosedChannelException

. If the output side of
the connection is already shutdown then invoking this method has no
effect.

Once shutdown for writing then further attempts to write to the
channel will throw

ClosedChannelException

. If the output side of
the connection is already shutdown then invoking this method has no
effect.

socket

```java
public abstract
Socket
socket()
```

Retrieves a socket associated with this channel.

The returned object will not declare any public methods that are not
declared in the

Socket

class.

**Returns:** A socket associated with this channel

---

#### socket

public abstract

Socket

socket()

Retrieves a socket associated with this channel.

The returned object will not declare any public methods that are not
declared in the

Socket

class.

The returned object will not declare any public methods that are not
declared in the

Socket

class.

isConnected

```java
public abstract boolean isConnected()
```

Tells whether or not this channel's network socket is connected.

**Returns:** true

if, and only if, this channel's network socket
is

open

and connected

---

#### isConnected

public abstract boolean isConnected()

Tells whether or not this channel's network socket is connected.

isConnectionPending

```java
public abstract boolean isConnectionPending()
```

Tells whether or not a connection operation is in progress on this
channel.

**Returns:** true

if, and only if, a connection operation has been
initiated on this channel but not yet completed by invoking the

finishConnect

method

---

#### isConnectionPending

public abstract boolean isConnectionPending()

Tells whether or not a connection operation is in progress on this
channel.

connect

```java
public abstract boolean connect​(
SocketAddress
remote)
throws
IOException
```

Connects this channel's socket.

If this channel is in non-blocking mode then an invocation of this
method initiates a non-blocking connection operation. If the connection
is established immediately, as can happen with a local connection, then
this method returns

true

. Otherwise this method returns

false

and the connection operation must later be completed by
invoking the

finishConnect

method.

If this channel is in blocking mode then an invocation of this
method will block until the connection is established or an I/O error
occurs.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

**Parameters:** remote

- The remote address to which this channel is to be connected
**Returns:** true

if a connection was established,

false

if this channel is in non-blocking mode
and the connection operation is in progress
**Throws:** AlreadyConnectedException

- If this channel is already connected
**Throws:** ConnectionPendingException

- If a non-blocking connection operation is already in progress
on this channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** UnresolvedAddressException

- If the given remote address is not fully resolved
**Throws:** UnsupportedAddressTypeException

- If the type of the given remote address is not supported
**Throws:** SecurityException

- If a security manager has been installed
and it does not permit access to the given remote endpoint
**Throws:** IOException

- If some other I/O error occurs

---

#### connect

public abstract boolean connect​(

SocketAddress

remote)
throws

IOException

Connects this channel's socket.

If this channel is in non-blocking mode then an invocation of this
method initiates a non-blocking connection operation. If the connection
is established immediately, as can happen with a local connection, then
this method returns

true

. Otherwise this method returns

false

and the connection operation must later be completed by
invoking the

finishConnect

method.

If this channel is in blocking mode then an invocation of this
method will block until the connection is established or an I/O error
occurs.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

If this channel is in non-blocking mode then an invocation of this
method initiates a non-blocking connection operation. If the connection
is established immediately, as can happen with a local connection, then
this method returns

true

. Otherwise this method returns

false

and the connection operation must later be completed by
invoking the

finishConnect

method.

If this channel is in blocking mode then an invocation of this
method will block until the connection is established or an I/O error
occurs.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

If this channel is in blocking mode then an invocation of this
method will block until the connection is established or an I/O error
occurs.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

This method performs exactly the same security checks as the

Socket

class. That is, if a security manager has been
installed then this method verifies that its

checkConnect

method permits
connecting to the address and port number of the given remote endpoint.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt is initiated but fails,
that is, if an invocation of this method throws a checked exception,
then the channel will be closed.

finishConnect

```java
public abstract boolean finishConnect()
throws
IOException
```

Finishes the process of connecting a socket channel.

A non-blocking connection operation is initiated by placing a socket
channel in non-blocking mode and then invoking its

connect

method. Once the connection is established, or the attempt has
failed, the socket channel will become connectable and this method may
be invoked to complete the connection sequence. If the connection
operation failed then invoking this method will cause an appropriate

IOException

to be thrown.

If this channel is already connected then this method will not block
and will immediately return

true

. If this channel is in
non-blocking mode then this method will return

false

if the
connection process is not yet complete. If this channel is in blocking
mode then this method will block until the connection either completes
or fails, and will always either return

true

or throw a checked
exception describing the failure.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

**Returns:** true

if, and only if, this channel's socket is now
connected
**Throws:** NoConnectionPendingException

- If this channel is not connected and a connection operation
has not been initiated
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** AsynchronousCloseException

- If another thread closes this channel
while the connect operation is in progress
**Throws:** ClosedByInterruptException

- If another thread interrupts the current thread
while the connect operation is in progress, thereby
closing the channel and setting the current thread's
interrupt status
**Throws:** IOException

- If some other I/O error occurs

---

#### finishConnect

public abstract boolean finishConnect()
throws

IOException

Finishes the process of connecting a socket channel.

A non-blocking connection operation is initiated by placing a socket
channel in non-blocking mode and then invoking its

connect

method. Once the connection is established, or the attempt has
failed, the socket channel will become connectable and this method may
be invoked to complete the connection sequence. If the connection
operation failed then invoking this method will cause an appropriate

IOException

to be thrown.

If this channel is already connected then this method will not block
and will immediately return

true

. If this channel is in
non-blocking mode then this method will return

false

if the
connection process is not yet complete. If this channel is in blocking
mode then this method will block until the connection either completes
or fails, and will always either return

true

or throw a checked
exception describing the failure.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

A non-blocking connection operation is initiated by placing a socket
channel in non-blocking mode and then invoking its

connect

method. Once the connection is established, or the attempt has
failed, the socket channel will become connectable and this method may
be invoked to complete the connection sequence. If the connection
operation failed then invoking this method will cause an appropriate

IOException

to be thrown.

If this channel is already connected then this method will not block
and will immediately return

true

. If this channel is in
non-blocking mode then this method will return

false

if the
connection process is not yet complete. If this channel is in blocking
mode then this method will block until the connection either completes
or fails, and will always either return

true

or throw a checked
exception describing the failure.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

If this channel is already connected then this method will not block
and will immediately return

true

. If this channel is in
non-blocking mode then this method will return

false

if the
connection process is not yet complete. If this channel is in blocking
mode then this method will block until the connection either completes
or fails, and will always either return

true

or throw a checked
exception describing the failure.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

This method may be invoked at any time. If a read or write
operation upon this channel is invoked while an invocation of this
method is in progress then that operation will first block until this
invocation is complete. If a connection attempt fails, that is, if an
invocation of this method throws a checked exception, then the channel
will be closed.

getRemoteAddress

```java
public abstract
SocketAddress
getRemoteAddress()
throws
IOException
```

Returns the remote address to which this channel's socket is connected.

Where the channel is bound and connected to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

**Returns:** The remote address;

null

if the channel's socket is not
connected
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7

---

#### getRemoteAddress

public abstract

SocketAddress

getRemoteAddress()
throws

IOException

Returns the remote address to which this channel's socket is connected.

Where the channel is bound and connected to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

Where the channel is bound and connected to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

read

```java
public abstract int read​(
ByteBuffer
dst)
throws
IOException
```

Description copied from interface:

ReadableByteChannel

Reads a sequence of bytes from this channel into the given buffer.

An attempt is made to read up to

r

bytes from the channel,
where

r

is the number of bytes remaining in the buffer, that is,

dst.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
This byte sequence will be transferred into the buffer so that the first
byte in the sequence is at index

p

and the last byte is at index

p

+

n

-

1

,
where

p

is the buffer's position at the moment this method is
invoked. Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

A read operation might not fill the buffer, and in fact it might not
read any bytes at all. Whether or not it does so depends upon the
nature and state of the channel. A socket channel in non-blocking mode,
for example, cannot read any more bytes than are immediately available
from the socket's input buffer; similarly, a file channel cannot read
any more bytes than remain in the file. It is guaranteed, however, that
if a channel is in blocking mode and there is at least one byte
remaining in the buffer then this method will block until at least one
byte is read.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

**Specified by:** read

in interface

ReadableByteChannel
**Parameters:** dst

- The buffer into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero, or

-1

if the
channel has reached end-of-stream
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

public abstract int read​(

ByteBuffer

dst)
throws

IOException

Description copied from interface:

ReadableByteChannel

Reads a sequence of bytes from this channel into the given buffer.

An attempt is made to read up to

r

bytes from the channel,
where

r

is the number of bytes remaining in the buffer, that is,

dst.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
This byte sequence will be transferred into the buffer so that the first
byte in the sequence is at index

p

and the last byte is at index

p

+

n

-

1

,
where

p

is the buffer's position at the moment this method is
invoked. Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

A read operation might not fill the buffer, and in fact it might not
read any bytes at all. Whether or not it does so depends upon the
nature and state of the channel. A socket channel in non-blocking mode,
for example, cannot read any more bytes than are immediately available
from the socket's input buffer; similarly, a file channel cannot read
any more bytes than remain in the file. It is guaranteed, however, that
if a channel is in blocking mode and there is at least one byte
remaining in the buffer then this method will block until at least one
byte is read.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

An attempt is made to read up to

r

bytes from the channel,
where

r

is the number of bytes remaining in the buffer, that is,

dst.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
This byte sequence will be transferred into the buffer so that the first
byte in the sequence is at index

p

and the last byte is at index

p

+

n

-

1

,
where

p

is the buffer's position at the moment this method is
invoked. Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

A read operation might not fill the buffer, and in fact it might not
read any bytes at all. Whether or not it does so depends upon the
nature and state of the channel. A socket channel in non-blocking mode,
for example, cannot read any more bytes than are immediately available
from the socket's input buffer; similarly, a file channel cannot read
any more bytes than remain in the file. It is guaranteed, however, that
if a channel is in blocking mode and there is at least one byte
remaining in the buffer then this method will block until at least one
byte is read.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

Suppose that a byte sequence of length

n

is read, where

0

<=

n

<=

r

.
This byte sequence will be transferred into the buffer so that the first
byte in the sequence is at index

p

and the last byte is at index

p

+

n

-

1

,
where

p

is the buffer's position at the moment this method is
invoked. Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

A read operation might not fill the buffer, and in fact it might not
read any bytes at all. Whether or not it does so depends upon the
nature and state of the channel. A socket channel in non-blocking mode,
for example, cannot read any more bytes than are immediately available
from the socket's input buffer; similarly, a file channel cannot read
any more bytes than remain in the file. It is guaranteed, however, that
if a channel is in blocking mode and there is at least one byte
remaining in the buffer then this method will block until at least one
byte is read.

This method may be invoked at any time. If another thread has
already initiated a read operation upon this channel, however, then an
invocation of this method will block until the first operation is
complete.

A read operation might not fill the buffer, and in fact it might not
read any bytes at all. Whether or not it does so depends upon the
nature and state of the channel. A socket channel in non-blocking mode,
for example, cannot read any more bytes than are immediately available
from the socket's input buffer; similarly, a file channel cannot read
any more bytes than remain in the file. It is guaranteed, however, that
if a channel is in blocking mode and there is at least one byte
remaining in the buffer then this method will block until at least one
byte is read.

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
public abstract long read​(
ByteBuffer
[] dsts,
int offset,
int length)
throws
IOException
```

Description copied from interface:

ScatteringByteChannel

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

**Specified by:** read

in interface

ScatteringByteChannel
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
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

public abstract long read​(

ByteBuffer

[] dsts,
int offset,
int length)
throws

IOException

Description copied from interface:

ScatteringByteChannel

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
public final long read​(
ByteBuffer
[] dsts)
throws
IOException
```

Description copied from interface:

ScatteringByteChannel

Reads a sequence of bytes from this channel into the given buffers.

An invocation of this method of the form

c.read(dsts)

behaves in exactly the same manner as the invocation

```java
c.read(dsts, 0, dsts.length);
```

**Specified by:** read

in interface

ScatteringByteChannel
**Parameters:** dsts

- The buffers into which bytes are to be transferred
**Returns:** The number of bytes read, possibly zero,
or

-1

if the channel has reached end-of-stream
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

public final long read​(

ByteBuffer

[] dsts)
throws

IOException

Description copied from interface:

ScatteringByteChannel

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

write

```java
public abstract int write​(
ByteBuffer
src)
throws
IOException
```

Description copied from interface:

WritableByteChannel

Writes a sequence of bytes to this channel from the given buffer.

An attempt is made to write up to

r

bytes to the channel,
where

r

is the number of bytes remaining in the buffer, that is,

src.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
This byte sequence will be transferred from the buffer starting at index

p

, where

p

is the buffer's position at the moment this
method is invoked; the index of the last byte written will be

p

+

n

-

1

.
Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

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

**Specified by:** write

in interface

WritableByteChannel
**Parameters:** src

- The buffer from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

public abstract int write​(

ByteBuffer

src)
throws

IOException

Description copied from interface:

WritableByteChannel

Writes a sequence of bytes to this channel from the given buffer.

An attempt is made to write up to

r

bytes to the channel,
where

r

is the number of bytes remaining in the buffer, that is,

src.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
This byte sequence will be transferred from the buffer starting at index

p

, where

p

is the buffer's position at the moment this
method is invoked; the index of the last byte written will be

p

+

n

-

1

.
Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

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

bytes to the channel,
where

r

is the number of bytes remaining in the buffer, that is,

src.remaining()

, at the moment this method is invoked.

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
This byte sequence will be transferred from the buffer starting at index

p

, where

p

is the buffer's position at the moment this
method is invoked; the index of the last byte written will be

p

+

n

-

1

.
Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

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

Suppose that a byte sequence of length

n

is written, where

0

<=

n

<=

r

.
This byte sequence will be transferred from the buffer starting at index

p

, where

p

is the buffer's position at the moment this
method is invoked; the index of the last byte written will be

p

+

n

-

1

.
Upon return the buffer's position will be equal to

p

+

n

; its limit will not have changed.

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
public abstract long write​(
ByteBuffer
[] srcs,
int offset,
int length)
throws
IOException
```

Description copied from interface:

GatheringByteChannel

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

**Specified by:** write

in interface

GatheringByteChannel
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
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

public abstract long write​(

ByteBuffer

[] srcs,
int offset,
int length)
throws

IOException

Description copied from interface:

GatheringByteChannel

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
public final long write​(
ByteBuffer
[] srcs)
throws
IOException
```

Description copied from interface:

GatheringByteChannel

Writes a sequence of bytes to this channel from the given buffers.

An invocation of this method of the form

c.write(srcs)

behaves in exactly the same manner as the invocation

```java
c.write(srcs, 0, srcs.length);
```

**Specified by:** write

in interface

GatheringByteChannel
**Parameters:** srcs

- The buffers from which bytes are to be retrieved
**Returns:** The number of bytes written, possibly zero
**Throws:** NotYetConnectedException

- If this channel is not yet connected
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

public final long write​(

ByteBuffer

[] srcs)
throws

IOException

Description copied from interface:

GatheringByteChannel

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

getLocalAddress

```java
public abstract
SocketAddress
getLocalAddress()
throws
IOException
```

Returns the socket address that this channel's socket is bound to.

Where the channel is

bound

to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
a

SocketAddress

representing the

loopback

address and the
local port of the channel's socket is returned.

**Specified by:** getLocalAddress

in interface

NetworkChannel
**Returns:** The

SocketAddress

that the socket is bound to, or the

SocketAddress

representing the loopback address if
denied by the security manager, or

null

if the
channel's socket is not bound
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs

---

#### getLocalAddress

public abstract

SocketAddress

getLocalAddress()
throws

IOException

Returns the socket address that this channel's socket is bound to.

Where the channel is

bound

to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
a

SocketAddress

representing the

loopback

address and the
local port of the channel's socket is returned.

Where the channel is

bound

to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
a

SocketAddress

representing the

loopback

address and the
local port of the channel's socket is returned.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
a

SocketAddress

representing the

loopback

address and the
local port of the channel's socket is returned.

---

