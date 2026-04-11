# Class DatagramSocket

**Source:** `java.base\java\net\DatagramSocket.html`

### Class Description

```java
public class
DatagramSocket

extends
Object

implements
Closeable
```

This class represents a socket for sending and receiving datagram packets.

A datagram socket is the sending or receiving point for a packet
delivery service. Each packet sent or received on a datagram socket
is individually addressed and routed. Multiple packets sent from
one machine to another may be routed differently, and may arrive in
any order.

Where possible, a newly constructed

DatagramSocket

has the

SO_BROADCAST

socket option enabled so as
to allow the transmission of broadcast datagrams. In order to receive
broadcast packets a DatagramSocket should be bound to the wildcard address.
In some implementations, broadcast packets may also be received when
a DatagramSocket is bound to a more specific address.

Example:

DatagramSocket s = new DatagramSocket(null);
s.bind(new InetSocketAddress(8888));

Which is equivalent to:

DatagramSocket s = new DatagramSocket(8888);

Both cases will create a DatagramSocket able to receive broadcasts on
UDP port 8888.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DatagramSocket()
throws
SocketException

Constructs a datagram socket and binds it to any available port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with 0 as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Throws:**
- SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.

**See Also:**
- SecurityManager.checkListen(int)

---

#### protected DatagramSocket​(
DatagramSocketImpl
impl)

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

**Parameters:**
- impl

- an instance of a

DatagramSocketImpl

the subclass wishes to use on the DatagramSocket.

**Since:**
- 1.4

---

#### public DatagramSocket​(
SocketAddress
bindaddr)
throws
SocketException

Creates a datagram socket, bound to the specified local
socket address.

If, if the address is

null

, creates an unbound socket.

If there is a security manager,
its

checkListen

method is first called
with the port from the socket address
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:**
- bindaddr

- local socket address to bind, or

null

for an unbound socket.

**Throws:**
- SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.

**See Also:**
- SecurityManager.checkListen(int)

**Since:**
- 1.4

---

#### public DatagramSocket​(int port)
throws
SocketException

Constructs a datagram socket and binds it to the specified port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:**
- port

- port to use.

**Throws:**
- SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.

**See Also:**
- SecurityManager.checkListen(int)

---

#### public DatagramSocket​(int port,

InetAddress
laddr)
throws
SocketException

Creates a datagram socket, bound to the specified local
address. The local port must be between 0 and 65535 inclusive.
If the IP address is 0.0.0.0, the socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:**
- port

- local port to use
- laddr

- local address to bind

**Throws:**
- SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.

**See Also:**
- SecurityManager.checkListen(int)

**Since:**
- 1.1

---

### Method Details

#### public void bind​(
SocketAddress
addr)
throws
SocketException

Binds this DatagramSocket to a specific address and port.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:**
- addr

- The address and port to bind to.

**Throws:**
- SocketException

- if any error happens during the bind, or if the
socket is already bound.
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if addr is a SocketAddress subclass
not supported by this socket.

**Since:**
- 1.4

---

#### public void connect​(
InetAddress
address,
int port)

Connects the socket to a remote address for this socket. When a
socket is connected to a remote address, packets may only be
sent to or received from that address. By default a datagram
socket is not connected.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException. Note, there is no
guarantee that the exception will be thrown.

If a security manager has been installed then it is invoked to check
access to the remote address. Specifically, if the given

address

is a

multicast address

,
the security manager's

checkMulticast

method is invoked with the given

address

.
Otherwise, the security manager's

checkConnect

and

checkAccept

methods
are invoked, with the given

address

and

port

, to
verify that datagrams are permitted to be sent and received
respectively.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

**Parameters:**
- address

- the remote address for the socket
- port

- the remote port for the socket.

**Throws:**
- IllegalArgumentException

- if the address is null, or the port is out of range.
- SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address

**See Also:**
- disconnect()

---

#### public void connect​(
SocketAddress
addr)
throws
SocketException

Connects this socket to a remote socket address (IP address + port number).

If given an

InetSocketAddress

, this method
behaves as if invoking

connect(InetAddress,int)

with the given socket addresses IP address and port number.

**Parameters:**
- addr

- The remote address.

**Throws:**
- SocketException

- if the connect fails
- IllegalArgumentException

- if

addr

is

null

, or

addr

is a SocketAddress
subclass not supported by this socket
- SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address

**Since:**
- 1.4

---

#### public void disconnect()

Disconnects the socket. If the socket is closed or not connected,
then this method has no effect.

**See Also:**
- connect(java.net.InetAddress, int)

---

#### public boolean isBound()

Returns the binding state of the socket.

If the socket was bound prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:**
- true if the socket successfully bound to an address

**Since:**
- 1.4

---

#### public boolean isConnected()

Returns the connection state of the socket.

If the socket was connected prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:**
- true if the socket successfully connected to a server

**Since:**
- 1.4

---

#### public
InetAddress
getInetAddress()

Returns the address to which this socket is connected. Returns

null

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:**
- the address to which this socket is connected.

---

#### public int getPort()

Returns the port number to which this socket is connected.
Returns

-1

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected port number
after the socket is closed.

**Returns:**
- the port number to which this socket is connected.

---

#### public
SocketAddress
getRemoteSocketAddress()

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:**
- a

SocketAddress

representing the remote
endpoint of this socket, or

null

if it is
not connected yet.

**See Also:**
- getInetAddress()

,

getPort()

,

connect(SocketAddress)

**Since:**
- 1.4

---

#### public
SocketAddress
getLocalSocketAddress()

Returns the address of the endpoint this socket is bound to.

**Returns:**
- a

SocketAddress

representing the local endpoint of this
socket, or

null

if it is closed or not bound yet.

**See Also:**
- getLocalAddress()

,

getLocalPort()

,

bind(SocketAddress)

**Since:**
- 1.4

---

#### public void send​(
DatagramPacket
p)
throws
IOException

Sends a datagram packet from this socket. The

DatagramPacket

includes information indicating the
data to be sent, its length, the IP address of the remote host,
and the port number on the remote host.

If there is a security manager, and the socket is not currently
connected to a remote address, this method first performs some
security checks. First, if

p.getAddress().isMulticastAddress()

is true, this method calls the
security manager's

checkMulticast

method
with

p.getAddress()

as its argument.
If the evaluation of that expression is false,
this method instead calls the security manager's

checkConnect

method with arguments

p.getAddress().getHostAddress()

and

p.getPort()

. Each call to a security manager method
could result in a SecurityException if the operation is not allowed.

**Parameters:**
- p

- the

DatagramPacket

to be sent.

**Throws:**
- IOException

- if an I/O error occurs.
- SecurityException

- if a security manager exists and its

checkMulticast

or

checkConnect

method doesn't allow the send.
- PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no
guarantee that the exception will be thrown.
- IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.
- IllegalArgumentException

- if the socket is connected,
and connected address and packet address differ.

**See Also:**
- DatagramPacket

,

SecurityManager.checkMulticast(InetAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

---

#### public void receive​(
DatagramPacket
p)
throws
IOException

Receives a datagram packet from this socket. When this method
returns, the

DatagramPacket

's buffer is filled with
the data received. The datagram packet also contains the sender's
IP address, and the port number on the sender's machine.

This method blocks until a datagram is received. The

length

field of the datagram packet object contains
the length of the received message. If the message is longer than
the packet's length, the message is truncated.

If there is a security manager, a packet cannot be received if the
security manager's

checkAccept

method
does not allow it.

**Parameters:**
- p

- the

DatagramPacket

into which to place
the incoming data.

**Throws:**
- IOException

- if an I/O error occurs.
- SocketTimeoutException

- if setSoTimeout was previously called
and the timeout has expired.
- PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.
- IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.

**See Also:**
- DatagramPacket

,

DatagramSocket

---

#### public
InetAddress
getLocalAddress()

Gets the local address to which the socket is bound.

If there is a security manager, its

checkConnect

method is first called
with the host address and

-1

as its arguments to see if the operation is allowed.

**Returns:**
- the local address to which the socket is bound,

null

if the socket is closed, or
an

InetAddress

representing

wildcard

address if either the socket is not bound, or
the security manager

checkConnect

method does not allow the operation

**See Also:**
- SecurityManager.checkConnect(java.lang.String, int)

**Since:**
- 1.1

---

#### public int getLocalPort()

Returns the port number on the local host to which this socket
is bound.

**Returns:**
- the port number on the local host to which this socket is bound,

-1

if the socket is closed, or

0

if it is not bound yet.

---

#### public void setSoTimeout​(int timeout)
throws
SocketException

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds. With this option set to a non-zero timeout,
a call to receive() for this DatagramSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
DatagramSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:**
- timeout

- the specified timeout in milliseconds.

**Throws:**
- SocketException

- if there is an error in the underlying protocol, such as an UDP error.

**See Also:**
- getSoTimeout()

**Since:**
- 1.1

---

#### public int getSoTimeout()
throws
SocketException

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

**Returns:**
- the setting for SO_TIMEOUT

**Throws:**
- SocketException

- if there is an error in the underlying protocol, such as an UDP error.

**See Also:**
- setSoTimeout(int)

**Since:**
- 1.1

---

#### public void setSendBufferSize​(int size)
throws
SocketException

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

. The SO_SNDBUF option is used by the
network implementation as a hint to size the underlying
network I/O buffers. The SO_SNDBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be sent on this socket.

As SO_SNDBUF is a hint, applications that want to verify
what size the buffer is should call

getSendBufferSize()

.

Increasing the buffer size may allow multiple outgoing packets
to be queued by the network implementation when the send rate
is high.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

**Parameters:**
- size

- the size to which to set the send buffer
size. This value must be greater than 0.

**Throws:**
- SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
- IllegalArgumentException

- if the value is 0 or is
negative.

**See Also:**
- getSendBufferSize()

---

#### public int getSendBufferSize()
throws
SocketException

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

**Returns:**
- the value of the SO_SNDBUF option for this

DatagramSocket

**Throws:**
- SocketException

- if there is an error in
the underlying protocol, such as an UDP error.

**See Also:**
- setSendBufferSize(int)

---

#### public void setReceiveBufferSize​(int size)
throws
SocketException

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

. The SO_RCVBUF option is used by
the network implementation as a hint to size the underlying
network I/O buffers. The SO_RCVBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be received on this socket.

Because SO_RCVBUF is a hint, applications that want to
verify what size the buffers were set to should call

getReceiveBufferSize()

.

Increasing SO_RCVBUF may allow the network implementation
to buffer multiple packets when packets arrive faster than
are being received using

receive(DatagramPacket)

.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

**Parameters:**
- size

- the size to which to set the receive buffer
size. This value must be greater than 0.

**Throws:**
- SocketException

- if there is an error in
the underlying protocol, such as an UDP error.
- IllegalArgumentException

- if the value is 0 or is
negative.

**See Also:**
- getReceiveBufferSize()

---

#### public int getReceiveBufferSize()
throws
SocketException

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

**Returns:**
- the value of the SO_RCVBUF option for this

DatagramSocket

**Throws:**
- SocketException

- if there is an error in the underlying protocol, such as an UDP error.

**See Also:**
- setReceiveBufferSize(int)

---

#### public void setReuseAddress​(boolean on)
throws
SocketException

Enable/disable the SO_REUSEADDR socket option.

For UDP sockets it may be necessary to bind more than one
socket to the same socket address. This is typically for the
purpose of receiving multicast packets
(See

MulticastSocket

). The

SO_REUSEADDR

socket option allows multiple
sockets to be bound to the same socket address if the

SO_REUSEADDR

socket option is enabled prior
to binding the socket using

bind(SocketAddress)

.

Note: This functionality is not supported by all existing platforms,
so it is implementation specific whether this option will be ignored
or not. However, if it is not supported then

getReuseAddress()

will always return

false

.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:**
- on

- whether to enable or disable the

**Throws:**
- SocketException

- if an error occurs enabling or
disabling the

SO_RESUEADDR

socket option,
or the socket is closed.

**See Also:**
- getReuseAddress()

,

bind(SocketAddress)

,

isBound()

,

isClosed()

**Since:**
- 1.4

---

#### public boolean getReuseAddress()
throws
SocketException

Tests if SO_REUSEADDR is enabled.

**Returns:**
- a

boolean

indicating whether or not SO_REUSEADDR is enabled.

**Throws:**
- SocketException

- if there is an error
in the underlying protocol, such as an UDP error.

**See Also:**
- setReuseAddress(boolean)

**Since:**
- 1.4

---

#### public void setBroadcast​(boolean on)
throws
SocketException

Enable/disable SO_BROADCAST.

Some operating systems may require that the Java virtual machine be
started with implementation specific privileges to enable this option or
send broadcast datagrams.

**Parameters:**
- on

- whether or not to have broadcast turned on.

**Throws:**
- SocketException

- if there is an error in the underlying protocol, such as an UDP
error.

**See Also:**
- getBroadcast()

**Since:**
- 1.4

---

#### public boolean getBroadcast()
throws
SocketException

Tests if SO_BROADCAST is enabled.

**Returns:**
- a

boolean

indicating whether or not SO_BROADCAST is enabled.

**Throws:**
- SocketException

- if there is an error
in the underlying protocol, such as an UDP error.

**See Also:**
- setBroadcast(boolean)

**Since:**
- 1.4

---

#### public void setTrafficClass​(int tc)
throws
SocketException

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.
As the underlying network implementation may ignore this
value applications should consider it a hint.

The tc

must

be in the range

0 <= tc <=
255

or an IllegalArgumentException will be thrown.

Notes:

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

**Parameters:**
- tc

- an

int

value for the bitset.

**Throws:**
- SocketException

- if there is an error setting the
traffic class or type-of-service

**See Also:**
- getTrafficClass()

**Since:**
- 1.4

---

#### public int getTrafficClass()
throws
SocketException

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

As the underlying network implementation may ignore the
traffic class or type-of-service set using

setTrafficClass(int)

this method may return a different value than was previously
set using the

setTrafficClass(int)

method on this
DatagramSocket.

**Returns:**
- the traffic class or type-of-service already set

**Throws:**
- SocketException

- if there is an error obtaining the
traffic class or type-of-service value.

**See Also:**
- setTrafficClass(int)

**Since:**
- 1.4

---

#### public void close()

Closes this datagram socket.

Any thread currently blocked in

receive(java.net.DatagramPacket)

upon this socket
will throw a

SocketException

.

If this socket has an associated channel then the channel is closed
as well.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

---

#### public boolean isClosed()

Returns whether the socket is closed or not.

**Returns:**
- true if the socket has been closed

**Since:**
- 1.4

---

#### public
DatagramChannel
getChannel()

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

A datagram socket will have a channel if, and only if, the channel
itself was created via the

DatagramChannel.open

method.

**Returns:**
- the datagram channel associated with this datagram socket,
or

null

if this socket was not created for a channel

**Since:**
- 1.4

---

#### public static void setDatagramSocketImplFactory​(
DatagramSocketImplFactory
fac)
throws
IOException

Sets the datagram socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new datagram socket, the socket
implementation factory's

createDatagramSocketImpl

method is
called to create the actual datagram socket implementation.

Passing

null

to the method is a no-op unless the factory
was already set.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:**
- fac

- the desired factory.

**Throws:**
- IOException

- if an I/O error occurs when setting the
datagram socket factory.
- SocketException

- if the factory is already defined.
- SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.

**See Also:**
- DatagramSocketImplFactory.createDatagramSocketImpl()

,

SecurityManager.checkSetFactory()

**Since:**
- 1.3

---

#### public <T>
DatagramSocket
setOption​(
SocketOption
<T> name,
T value)
throws
IOException

Sets the value of a socket option.

**Parameters:**
- name

- The socket option
- value

- The value of the socket option. A value of

null

may be valid for some options.

**Returns:**
- this DatagramSocket

**Throws:**
- UnsupportedOperationException

- if the datagram socket
does not support the option.
- IllegalArgumentException

- if the value is not valid for
the option.
- IOException

- if an I/O error occurs, or if the socket is closed.
- SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.
- NullPointerException

- if name is

null

**Since:**
- 9

**Type Parameters:**
- T

- The type of the socket option value

---

#### public <T> T getOption​(
SocketOption
<T> name)
throws
IOException

Returns the value of a socket option.

**Parameters:**
- name

- The socket option

**Returns:**
- The value of the socket option.

**Throws:**
- UnsupportedOperationException

- if the datagram socket
does not support the option.
- IOException

- if an I/O error occurs, or if the socket is closed.
- NullPointerException

- if name is

null
- SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.

**Since:**
- 9

**Type Parameters:**
- T

- The type of the socket option value

---

#### public
Set
<
SocketOption
<?>> supportedOptions()

Returns a set of the socket options supported by this socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:**
- A set of the socket options supported by this socket. This set
may be empty if the socket's DatagramSocketImpl cannot be created.

**Since:**
- 9

---

### Additional Sections

#### Class DatagramSocket

java.lang.Object

- java.net.DatagramSocket

java.net.DatagramSocket

**All Implemented Interfaces:** Closeable

,

AutoCloseable

**Direct Known Subclasses:** MulticastSocket

```java
public class
DatagramSocket

extends
Object

implements
Closeable
```

This class represents a socket for sending and receiving datagram packets.

A datagram socket is the sending or receiving point for a packet
delivery service. Each packet sent or received on a datagram socket
is individually addressed and routed. Multiple packets sent from
one machine to another may be routed differently, and may arrive in
any order.

Where possible, a newly constructed

DatagramSocket

has the

SO_BROADCAST

socket option enabled so as
to allow the transmission of broadcast datagrams. In order to receive
broadcast packets a DatagramSocket should be bound to the wildcard address.
In some implementations, broadcast packets may also be received when
a DatagramSocket is bound to a more specific address.

Example:

DatagramSocket s = new DatagramSocket(null);
s.bind(new InetSocketAddress(8888));

Which is equivalent to:

DatagramSocket s = new DatagramSocket(8888);

Both cases will create a DatagramSocket able to receive broadcasts on
UDP port 8888.

**Since:** 1.0
**See Also:** DatagramPacket

,

DatagramChannel

public class

DatagramSocket

extends

Object

implements

Closeable

This class represents a socket for sending and receiving datagram packets.

A datagram socket is the sending or receiving point for a packet
delivery service. Each packet sent or received on a datagram socket
is individually addressed and routed. Multiple packets sent from
one machine to another may be routed differently, and may arrive in
any order.

Where possible, a newly constructed

DatagramSocket

has the

SO_BROADCAST

socket option enabled so as
to allow the transmission of broadcast datagrams. In order to receive
broadcast packets a DatagramSocket should be bound to the wildcard address.
In some implementations, broadcast packets may also be received when
a DatagramSocket is bound to a more specific address.

Example:

DatagramSocket s = new DatagramSocket(null);
s.bind(new InetSocketAddress(8888));

Which is equivalent to:

DatagramSocket s = new DatagramSocket(8888);

Both cases will create a DatagramSocket able to receive broadcasts on
UDP port 8888.

A datagram socket is the sending or receiving point for a packet
delivery service. Each packet sent or received on a datagram socket
is individually addressed and routed. Multiple packets sent from
one machine to another may be routed differently, and may arrive in
any order.

Where possible, a newly constructed

DatagramSocket

has the

SO_BROADCAST

socket option enabled so as
to allow the transmission of broadcast datagrams. In order to receive
broadcast packets a DatagramSocket should be bound to the wildcard address.
In some implementations, broadcast packets may also be received when
a DatagramSocket is bound to a more specific address.

Example:

DatagramSocket s = new DatagramSocket(null);
s.bind(new InetSocketAddress(8888));

Which is equivalent to:

DatagramSocket s = new DatagramSocket(8888);

Both cases will create a DatagramSocket able to receive broadcasts on
UDP port 8888.

Where possible, a newly constructed

DatagramSocket

has the

SO_BROADCAST

socket option enabled so as
to allow the transmission of broadcast datagrams. In order to receive
broadcast packets a DatagramSocket should be bound to the wildcard address.
In some implementations, broadcast packets may also be received when
a DatagramSocket is bound to a more specific address.

Example:

DatagramSocket s = new DatagramSocket(null);
s.bind(new InetSocketAddress(8888));

Which is equivalent to:

DatagramSocket s = new DatagramSocket(8888);

Both cases will create a DatagramSocket able to receive broadcasts on
UDP port 8888.

Example:

DatagramSocket s = new DatagramSocket(null);
s.bind(new InetSocketAddress(8888));

Which is equivalent to:

DatagramSocket s = new DatagramSocket(8888);

Both cases will create a DatagramSocket able to receive broadcasts on
UDP port 8888.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

DatagramSocket

()

Constructs a datagram socket and binds it to any available port
on the local host machine.

DatagramSocket

​(int port)

Constructs a datagram socket and binds it to the specified port
on the local host machine.

DatagramSocket

​(int port,

InetAddress

laddr)

Creates a datagram socket, bound to the specified local
address.

protected

DatagramSocket

​(

DatagramSocketImpl

impl)

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

DatagramSocket

​(

SocketAddress

bindaddr)

Creates a datagram socket, bound to the specified local
socket address.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

bind

​(

SocketAddress

addr)

Binds this DatagramSocket to a specific address and port.

void

close

()

Closes this datagram socket.

void

connect

​(

InetAddress

address,
int port)

Connects the socket to a remote address for this socket.

void

connect

​(

SocketAddress

addr)

Connects this socket to a remote socket address (IP address + port number).

void

disconnect

()

Disconnects the socket.

boolean

getBroadcast

()

Tests if SO_BROADCAST is enabled.

DatagramChannel

getChannel

()

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

InetAddress

getInetAddress

()

Returns the address to which this socket is connected.

InetAddress

getLocalAddress

()

Gets the local address to which the socket is bound.

int

getLocalPort

()

Returns the port number on the local host to which this socket
is bound.

SocketAddress

getLocalSocketAddress

()

Returns the address of the endpoint this socket is bound to.

<T> T

getOption

​(

SocketOption

<T> name)

Returns the value of a socket option.

int

getPort

()

Returns the port number to which this socket is connected.

int

getReceiveBufferSize

()

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

SocketAddress

getRemoteSocketAddress

()

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

boolean

getReuseAddress

()

Tests if SO_REUSEADDR is enabled.

int

getSendBufferSize

()

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

int

getSoTimeout

()

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

int

getTrafficClass

()

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

boolean

isBound

()

Returns the binding state of the socket.

boolean

isClosed

()

Returns whether the socket is closed or not.

boolean

isConnected

()

Returns the connection state of the socket.

void

receive

​(

DatagramPacket

p)

Receives a datagram packet from this socket.

void

send

​(

DatagramPacket

p)

Sends a datagram packet from this socket.

void

setBroadcast

​(boolean on)

Enable/disable SO_BROADCAST.

static void

setDatagramSocketImplFactory

​(

DatagramSocketImplFactory

fac)

Sets the datagram socket implementation factory for the
application.

<T>

DatagramSocket

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

void

setReceiveBufferSize

​(int size)

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

.

void

setReuseAddress

​(boolean on)

Enable/disable the SO_REUSEADDR socket option.

void

setSendBufferSize

​(int size)

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

.

void

setSoTimeout

​(int timeout)

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds.

void

setTrafficClass

​(int tc)

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of the socket options supported by this socket.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

DatagramSocket

()

Constructs a datagram socket and binds it to any available port
on the local host machine.

DatagramSocket

​(int port)

Constructs a datagram socket and binds it to the specified port
on the local host machine.

DatagramSocket

​(int port,

InetAddress

laddr)

Creates a datagram socket, bound to the specified local
address.

protected

DatagramSocket

​(

DatagramSocketImpl

impl)

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

DatagramSocket

​(

SocketAddress

bindaddr)

Creates a datagram socket, bound to the specified local
socket address.

---

#### Constructor Summary

Constructs a datagram socket and binds it to any available port
on the local host machine.

Constructs a datagram socket and binds it to the specified port
on the local host machine.

Creates a datagram socket, bound to the specified local
address.

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

Creates a datagram socket, bound to the specified local
socket address.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

bind

​(

SocketAddress

addr)

Binds this DatagramSocket to a specific address and port.

void

close

()

Closes this datagram socket.

void

connect

​(

InetAddress

address,
int port)

Connects the socket to a remote address for this socket.

void

connect

​(

SocketAddress

addr)

Connects this socket to a remote socket address (IP address + port number).

void

disconnect

()

Disconnects the socket.

boolean

getBroadcast

()

Tests if SO_BROADCAST is enabled.

DatagramChannel

getChannel

()

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

InetAddress

getInetAddress

()

Returns the address to which this socket is connected.

InetAddress

getLocalAddress

()

Gets the local address to which the socket is bound.

int

getLocalPort

()

Returns the port number on the local host to which this socket
is bound.

SocketAddress

getLocalSocketAddress

()

Returns the address of the endpoint this socket is bound to.

<T> T

getOption

​(

SocketOption

<T> name)

Returns the value of a socket option.

int

getPort

()

Returns the port number to which this socket is connected.

int

getReceiveBufferSize

()

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

SocketAddress

getRemoteSocketAddress

()

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

boolean

getReuseAddress

()

Tests if SO_REUSEADDR is enabled.

int

getSendBufferSize

()

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

int

getSoTimeout

()

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

int

getTrafficClass

()

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

boolean

isBound

()

Returns the binding state of the socket.

boolean

isClosed

()

Returns whether the socket is closed or not.

boolean

isConnected

()

Returns the connection state of the socket.

void

receive

​(

DatagramPacket

p)

Receives a datagram packet from this socket.

void

send

​(

DatagramPacket

p)

Sends a datagram packet from this socket.

void

setBroadcast

​(boolean on)

Enable/disable SO_BROADCAST.

static void

setDatagramSocketImplFactory

​(

DatagramSocketImplFactory

fac)

Sets the datagram socket implementation factory for the
application.

<T>

DatagramSocket

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

void

setReceiveBufferSize

​(int size)

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

.

void

setReuseAddress

​(boolean on)

Enable/disable the SO_REUSEADDR socket option.

void

setSendBufferSize

​(int size)

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

.

void

setSoTimeout

​(int timeout)

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds.

void

setTrafficClass

​(int tc)

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of the socket options supported by this socket.

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

---

#### Method Summary

Binds this DatagramSocket to a specific address and port.

Closes this datagram socket.

Connects the socket to a remote address for this socket.

Connects this socket to a remote socket address (IP address + port number).

Disconnects the socket.

Tests if SO_BROADCAST is enabled.

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

Returns the address to which this socket is connected.

Gets the local address to which the socket is bound.

Returns the port number on the local host to which this socket
is bound.

Returns the address of the endpoint this socket is bound to.

Returns the value of a socket option.

Returns the port number to which this socket is connected.

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

Tests if SO_REUSEADDR is enabled.

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

Returns the binding state of the socket.

Returns whether the socket is closed or not.

Returns the connection state of the socket.

Receives a datagram packet from this socket.

Sends a datagram packet from this socket.

Enable/disable SO_BROADCAST.

Sets the datagram socket implementation factory for the
application.

Sets the value of a socket option.

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

.

Enable/disable the SO_REUSEADDR socket option.

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

.

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds.

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.

Returns a set of the socket options supported by this socket.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DatagramSocket

```java
public DatagramSocket()
throws
SocketException
```

Constructs a datagram socket and binds it to any available port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with 0 as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**See Also:** SecurityManager.checkListen(int)

- DatagramSocket

```java
protected DatagramSocket​(
DatagramSocketImpl
impl)
```

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

**Parameters:** impl

- an instance of a

DatagramSocketImpl

the subclass wishes to use on the DatagramSocket.
**Since:** 1.4

- DatagramSocket

```java
public DatagramSocket​(
SocketAddress
bindaddr)
throws
SocketException
```

Creates a datagram socket, bound to the specified local
socket address.

If, if the address is

null

, creates an unbound socket.

If there is a security manager,
its

checkListen

method is first called
with the port from the socket address
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** bindaddr

- local socket address to bind, or

null

for an unbound socket.
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Since:** 1.4
**See Also:** SecurityManager.checkListen(int)

- DatagramSocket

```java
public DatagramSocket​(int port)
throws
SocketException
```

Constructs a datagram socket and binds it to the specified port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- port to use.
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**See Also:** SecurityManager.checkListen(int)

- DatagramSocket

```java
public DatagramSocket​(int port,

InetAddress
laddr)
throws
SocketException
```

Creates a datagram socket, bound to the specified local
address. The local port must be between 0 and 65535 inclusive.
If the IP address is 0.0.0.0, the socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- local port to use
**Parameters:** laddr

- local address to bind
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Since:** 1.1
**See Also:** SecurityManager.checkListen(int)

============ METHOD DETAIL ==========

- Method Detail

- bind

```java
public void bind​(
SocketAddress
addr)
throws
SocketException
```

Binds this DatagramSocket to a specific address and port.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:** addr

- The address and port to bind to.
**Throws:** SocketException

- if any error happens during the bind, or if the
socket is already bound.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if addr is a SocketAddress subclass
not supported by this socket.
**Since:** 1.4

- connect

```java
public void connect​(
InetAddress
address,
int port)
```

Connects the socket to a remote address for this socket. When a
socket is connected to a remote address, packets may only be
sent to or received from that address. By default a datagram
socket is not connected.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException. Note, there is no
guarantee that the exception will be thrown.

If a security manager has been installed then it is invoked to check
access to the remote address. Specifically, if the given

address

is a

multicast address

,
the security manager's

checkMulticast

method is invoked with the given

address

.
Otherwise, the security manager's

checkConnect

and

checkAccept

methods
are invoked, with the given

address

and

port

, to
verify that datagrams are permitted to be sent and received
respectively.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

**Parameters:** address

- the remote address for the socket
**Parameters:** port

- the remote port for the socket.
**Throws:** IllegalArgumentException

- if the address is null, or the port is out of range.
**Throws:** SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address
**See Also:** disconnect()

- connect

```java
public void connect​(
SocketAddress
addr)
throws
SocketException
```

Connects this socket to a remote socket address (IP address + port number).

If given an

InetSocketAddress

, this method
behaves as if invoking

connect(InetAddress,int)

with the given socket addresses IP address and port number.

**Parameters:** addr

- The remote address.
**Throws:** SocketException

- if the connect fails
**Throws:** IllegalArgumentException

- if

addr

is

null

, or

addr

is a SocketAddress
subclass not supported by this socket
**Throws:** SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address
**Since:** 1.4

- disconnect

```java
public void disconnect()
```

Disconnects the socket. If the socket is closed or not connected,
then this method has no effect.

**See Also:** connect(java.net.InetAddress, int)

- isBound

```java
public boolean isBound()
```

Returns the binding state of the socket.

If the socket was bound prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:** true if the socket successfully bound to an address
**Since:** 1.4

- isConnected

```java
public boolean isConnected()
```

Returns the connection state of the socket.

If the socket was connected prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:** true if the socket successfully connected to a server
**Since:** 1.4

- getInetAddress

```java
public
InetAddress
getInetAddress()
```

Returns the address to which this socket is connected. Returns

null

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:** the address to which this socket is connected.

- getPort

```java
public int getPort()
```

Returns the port number to which this socket is connected.
Returns

-1

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected port number
after the socket is closed.

**Returns:** the port number to which this socket is connected.

- getRemoteSocketAddress

```java
public
SocketAddress
getRemoteSocketAddress()
```

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:** a

SocketAddress

representing the remote
endpoint of this socket, or

null

if it is
not connected yet.
**Since:** 1.4
**See Also:** getInetAddress()

,

getPort()

,

connect(SocketAddress)

- getLocalSocketAddress

```java
public
SocketAddress
getLocalSocketAddress()
```

Returns the address of the endpoint this socket is bound to.

**Returns:** a

SocketAddress

representing the local endpoint of this
socket, or

null

if it is closed or not bound yet.
**Since:** 1.4
**See Also:** getLocalAddress()

,

getLocalPort()

,

bind(SocketAddress)

- send

```java
public void send​(
DatagramPacket
p)
throws
IOException
```

Sends a datagram packet from this socket. The

DatagramPacket

includes information indicating the
data to be sent, its length, the IP address of the remote host,
and the port number on the remote host.

If there is a security manager, and the socket is not currently
connected to a remote address, this method first performs some
security checks. First, if

p.getAddress().isMulticastAddress()

is true, this method calls the
security manager's

checkMulticast

method
with

p.getAddress()

as its argument.
If the evaluation of that expression is false,
this method instead calls the security manager's

checkConnect

method with arguments

p.getAddress().getHostAddress()

and

p.getPort()

. Each call to a security manager method
could result in a SecurityException if the operation is not allowed.

**Parameters:** p

- the

DatagramPacket

to be sent.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkMulticast

or

checkConnect

method doesn't allow the send.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no
guarantee that the exception will be thrown.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.
**Throws:** IllegalArgumentException

- if the socket is connected,
and connected address and packet address differ.
**See Also:** DatagramPacket

,

SecurityManager.checkMulticast(InetAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

- receive

```java
public void receive​(
DatagramPacket
p)
throws
IOException
```

Receives a datagram packet from this socket. When this method
returns, the

DatagramPacket

's buffer is filled with
the data received. The datagram packet also contains the sender's
IP address, and the port number on the sender's machine.

This method blocks until a datagram is received. The

length

field of the datagram packet object contains
the length of the received message. If the message is longer than
the packet's length, the message is truncated.

If there is a security manager, a packet cannot be received if the
security manager's

checkAccept

method
does not allow it.

**Parameters:** p

- the

DatagramPacket

into which to place
the incoming data.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** SocketTimeoutException

- if setSoTimeout was previously called
and the timeout has expired.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.
**See Also:** DatagramPacket

,

DatagramSocket

- getLocalAddress

```java
public
InetAddress
getLocalAddress()
```

Gets the local address to which the socket is bound.

If there is a security manager, its

checkConnect

method is first called
with the host address and

-1

as its arguments to see if the operation is allowed.

**Returns:** the local address to which the socket is bound,

null

if the socket is closed, or
an

InetAddress

representing

wildcard

address if either the socket is not bound, or
the security manager

checkConnect

method does not allow the operation
**Since:** 1.1
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

- getLocalPort

```java
public int getLocalPort()
```

Returns the port number on the local host to which this socket
is bound.

**Returns:** the port number on the local host to which this socket is bound,

-1

if the socket is closed, or

0

if it is not bound yet.

- setSoTimeout

```java
public void setSoTimeout​(int timeout)
throws
SocketException
```

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds. With this option set to a non-zero timeout,
a call to receive() for this DatagramSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
DatagramSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:** timeout

- the specified timeout in milliseconds.
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**Since:** 1.1
**See Also:** getSoTimeout()

- getSoTimeout

```java
public int getSoTimeout()
throws
SocketException
```

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

**Returns:** the setting for SO_TIMEOUT
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**Since:** 1.1
**See Also:** setSoTimeout(int)

- setSendBufferSize

```java
public void setSendBufferSize​(int size)
throws
SocketException
```

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

. The SO_SNDBUF option is used by the
network implementation as a hint to size the underlying
network I/O buffers. The SO_SNDBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be sent on this socket.

As SO_SNDBUF is a hint, applications that want to verify
what size the buffer is should call

getSendBufferSize()

.

Increasing the buffer size may allow multiple outgoing packets
to be queued by the network implementation when the send rate
is high.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

**Parameters:** size

- the size to which to set the send buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Throws:** IllegalArgumentException

- if the value is 0 or is
negative.
**See Also:** getSendBufferSize()

- getSendBufferSize

```java
public int getSendBufferSize()
throws
SocketException
```

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

**Returns:** the value of the SO_SNDBUF option for this

DatagramSocket
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as an UDP error.
**See Also:** setSendBufferSize(int)

- setReceiveBufferSize

```java
public void setReceiveBufferSize​(int size)
throws
SocketException
```

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

. The SO_RCVBUF option is used by
the network implementation as a hint to size the underlying
network I/O buffers. The SO_RCVBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be received on this socket.

Because SO_RCVBUF is a hint, applications that want to
verify what size the buffers were set to should call

getReceiveBufferSize()

.

Increasing SO_RCVBUF may allow the network implementation
to buffer multiple packets when packets arrive faster than
are being received using

receive(DatagramPacket)

.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

**Parameters:** size

- the size to which to set the receive buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as an UDP error.
**Throws:** IllegalArgumentException

- if the value is 0 or is
negative.
**See Also:** getReceiveBufferSize()

- getReceiveBufferSize

```java
public int getReceiveBufferSize()
throws
SocketException
```

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

**Returns:** the value of the SO_RCVBUF option for this

DatagramSocket
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**See Also:** setReceiveBufferSize(int)

- setReuseAddress

```java
public void setReuseAddress​(boolean on)
throws
SocketException
```

Enable/disable the SO_REUSEADDR socket option.

For UDP sockets it may be necessary to bind more than one
socket to the same socket address. This is typically for the
purpose of receiving multicast packets
(See

MulticastSocket

). The

SO_REUSEADDR

socket option allows multiple
sockets to be bound to the same socket address if the

SO_REUSEADDR

socket option is enabled prior
to binding the socket using

bind(SocketAddress)

.

Note: This functionality is not supported by all existing platforms,
so it is implementation specific whether this option will be ignored
or not. However, if it is not supported then

getReuseAddress()

will always return

false

.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:** on

- whether to enable or disable the
**Throws:** SocketException

- if an error occurs enabling or
disabling the

SO_RESUEADDR

socket option,
or the socket is closed.
**Since:** 1.4
**See Also:** getReuseAddress()

,

bind(SocketAddress)

,

isBound()

,

isClosed()

- getReuseAddress

```java
public boolean getReuseAddress()
throws
SocketException
```

Tests if SO_REUSEADDR is enabled.

**Returns:** a

boolean

indicating whether or not SO_REUSEADDR is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Since:** 1.4
**See Also:** setReuseAddress(boolean)

- setBroadcast

```java
public void setBroadcast​(boolean on)
throws
SocketException
```

Enable/disable SO_BROADCAST.

Some operating systems may require that the Java virtual machine be
started with implementation specific privileges to enable this option or
send broadcast datagrams.

**Parameters:** on

- whether or not to have broadcast turned on.
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP
error.
**Since:** 1.4
**See Also:** getBroadcast()

- getBroadcast

```java
public boolean getBroadcast()
throws
SocketException
```

Tests if SO_BROADCAST is enabled.

**Returns:** a

boolean

indicating whether or not SO_BROADCAST is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Since:** 1.4
**See Also:** setBroadcast(boolean)

- setTrafficClass

```java
public void setTrafficClass​(int tc)
throws
SocketException
```

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.
As the underlying network implementation may ignore this
value applications should consider it a hint.

The tc

must

be in the range

0 <= tc <=
255

or an IllegalArgumentException will be thrown.

Notes:

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

**Parameters:** tc

- an

int

value for the bitset.
**Throws:** SocketException

- if there is an error setting the
traffic class or type-of-service
**Since:** 1.4
**See Also:** getTrafficClass()

- getTrafficClass

```java
public int getTrafficClass()
throws
SocketException
```

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

As the underlying network implementation may ignore the
traffic class or type-of-service set using

setTrafficClass(int)

this method may return a different value than was previously
set using the

setTrafficClass(int)

method on this
DatagramSocket.

**Returns:** the traffic class or type-of-service already set
**Throws:** SocketException

- if there is an error obtaining the
traffic class or type-of-service value.
**Since:** 1.4
**See Also:** setTrafficClass(int)

- close

```java
public void close()
```

Closes this datagram socket.

Any thread currently blocked in

receive(java.net.DatagramPacket)

upon this socket
will throw a

SocketException

.

If this socket has an associated channel then the channel is closed
as well.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable

- isClosed

```java
public boolean isClosed()
```

Returns whether the socket is closed or not.

**Returns:** true if the socket has been closed
**Since:** 1.4

- getChannel

```java
public
DatagramChannel
getChannel()
```

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

A datagram socket will have a channel if, and only if, the channel
itself was created via the

DatagramChannel.open

method.

**Returns:** the datagram channel associated with this datagram socket,
or

null

if this socket was not created for a channel
**Since:** 1.4

- setDatagramSocketImplFactory

```java
public static void setDatagramSocketImplFactory​(
DatagramSocketImplFactory
fac)
throws
IOException
```

Sets the datagram socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new datagram socket, the socket
implementation factory's

createDatagramSocketImpl

method is
called to create the actual datagram socket implementation.

Passing

null

to the method is a no-op unless the factory
was already set.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** fac

- the desired factory.
**Throws:** IOException

- if an I/O error occurs when setting the
datagram socket factory.
**Throws:** SocketException

- if the factory is already defined.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**Since:** 1.3
**See Also:** DatagramSocketImplFactory.createDatagramSocketImpl()

,

SecurityManager.checkSetFactory()

- setOption

```java
public <T>
DatagramSocket
setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be valid for some options.
**Returns:** this DatagramSocket
**Throws:** UnsupportedOperationException

- if the datagram socket
does not support the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs, or if the socket is closed.
**Throws:** SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.
**Throws:** NullPointerException

- if name is

null
**Since:** 9

- getOption

```java
public <T> T getOption​(
SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the datagram socket
does not support the option.
**Throws:** IOException

- if an I/O error occurs, or if the socket is closed.
**Throws:** NullPointerException

- if name is

null
**Throws:** SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.
**Since:** 9

- supportedOptions

```java
public
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of the socket options supported by this socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:** A set of the socket options supported by this socket. This set
may be empty if the socket's DatagramSocketImpl cannot be created.
**Since:** 9

Constructor Detail

- DatagramSocket

```java
public DatagramSocket()
throws
SocketException
```

Constructs a datagram socket and binds it to any available port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with 0 as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**See Also:** SecurityManager.checkListen(int)

- DatagramSocket

```java
protected DatagramSocket​(
DatagramSocketImpl
impl)
```

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

**Parameters:** impl

- an instance of a

DatagramSocketImpl

the subclass wishes to use on the DatagramSocket.
**Since:** 1.4

- DatagramSocket

```java
public DatagramSocket​(
SocketAddress
bindaddr)
throws
SocketException
```

Creates a datagram socket, bound to the specified local
socket address.

If, if the address is

null

, creates an unbound socket.

If there is a security manager,
its

checkListen

method is first called
with the port from the socket address
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** bindaddr

- local socket address to bind, or

null

for an unbound socket.
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Since:** 1.4
**See Also:** SecurityManager.checkListen(int)

- DatagramSocket

```java
public DatagramSocket​(int port)
throws
SocketException
```

Constructs a datagram socket and binds it to the specified port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- port to use.
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**See Also:** SecurityManager.checkListen(int)

- DatagramSocket

```java
public DatagramSocket​(int port,

InetAddress
laddr)
throws
SocketException
```

Creates a datagram socket, bound to the specified local
address. The local port must be between 0 and 65535 inclusive.
If the IP address is 0.0.0.0, the socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- local port to use
**Parameters:** laddr

- local address to bind
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Since:** 1.1
**See Also:** SecurityManager.checkListen(int)

---

#### Constructor Detail

DatagramSocket

```java
public DatagramSocket()
throws
SocketException
```

Constructs a datagram socket and binds it to any available port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with 0 as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**See Also:** SecurityManager.checkListen(int)

---

#### DatagramSocket

public DatagramSocket()
throws

SocketException

Constructs a datagram socket and binds it to any available port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with 0 as its argument to ensure the operation is allowed.
This could result in a SecurityException.

If there is a security manager,
its

checkListen

method is first called
with 0 as its argument to ensure the operation is allowed.
This could result in a SecurityException.

DatagramSocket

```java
protected DatagramSocket​(
DatagramSocketImpl
impl)
```

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

**Parameters:** impl

- an instance of a

DatagramSocketImpl

the subclass wishes to use on the DatagramSocket.
**Since:** 1.4

---

#### DatagramSocket

protected DatagramSocket​(

DatagramSocketImpl

impl)

Creates an unbound datagram socket with the specified
DatagramSocketImpl.

DatagramSocket

```java
public DatagramSocket​(
SocketAddress
bindaddr)
throws
SocketException
```

Creates a datagram socket, bound to the specified local
socket address.

If, if the address is

null

, creates an unbound socket.

If there is a security manager,
its

checkListen

method is first called
with the port from the socket address
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** bindaddr

- local socket address to bind, or

null

for an unbound socket.
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Since:** 1.4
**See Also:** SecurityManager.checkListen(int)

---

#### DatagramSocket

public DatagramSocket​(

SocketAddress

bindaddr)
throws

SocketException

Creates a datagram socket, bound to the specified local
socket address.

If, if the address is

null

, creates an unbound socket.

If there is a security manager,
its

checkListen

method is first called
with the port from the socket address
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

If, if the address is

null

, creates an unbound socket.

If there is a security manager,
its

checkListen

method is first called
with the port from the socket address
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

If there is a security manager,
its

checkListen

method is first called
with the port from the socket address
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

DatagramSocket

```java
public DatagramSocket​(int port)
throws
SocketException
```

Constructs a datagram socket and binds it to the specified port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- port to use.
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**See Also:** SecurityManager.checkListen(int)

---

#### DatagramSocket

public DatagramSocket​(int port)
throws

SocketException

Constructs a datagram socket and binds it to the specified port
on the local host machine. The socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

DatagramSocket

```java
public DatagramSocket​(int port,

InetAddress
laddr)
throws
SocketException
```

Creates a datagram socket, bound to the specified local
address. The local port must be between 0 and 65535 inclusive.
If the IP address is 0.0.0.0, the socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- local port to use
**Parameters:** laddr

- local address to bind
**Throws:** SocketException

- if the socket could not be opened,
or the socket could not bind to the specified local port.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Since:** 1.1
**See Also:** SecurityManager.checkListen(int)

---

#### DatagramSocket

public DatagramSocket​(int port,

InetAddress

laddr)
throws

SocketException

Creates a datagram socket, bound to the specified local
address. The local port must be between 0 and 65535 inclusive.
If the IP address is 0.0.0.0, the socket will be bound to the

wildcard

address,
an IP address chosen by the kernel.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

If there is a security manager,
its

checkListen

method is first called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

Method Detail

- bind

```java
public void bind​(
SocketAddress
addr)
throws
SocketException
```

Binds this DatagramSocket to a specific address and port.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:** addr

- The address and port to bind to.
**Throws:** SocketException

- if any error happens during the bind, or if the
socket is already bound.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if addr is a SocketAddress subclass
not supported by this socket.
**Since:** 1.4

- connect

```java
public void connect​(
InetAddress
address,
int port)
```

Connects the socket to a remote address for this socket. When a
socket is connected to a remote address, packets may only be
sent to or received from that address. By default a datagram
socket is not connected.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException. Note, there is no
guarantee that the exception will be thrown.

If a security manager has been installed then it is invoked to check
access to the remote address. Specifically, if the given

address

is a

multicast address

,
the security manager's

checkMulticast

method is invoked with the given

address

.
Otherwise, the security manager's

checkConnect

and

checkAccept

methods
are invoked, with the given

address

and

port

, to
verify that datagrams are permitted to be sent and received
respectively.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

**Parameters:** address

- the remote address for the socket
**Parameters:** port

- the remote port for the socket.
**Throws:** IllegalArgumentException

- if the address is null, or the port is out of range.
**Throws:** SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address
**See Also:** disconnect()

- connect

```java
public void connect​(
SocketAddress
addr)
throws
SocketException
```

Connects this socket to a remote socket address (IP address + port number).

If given an

InetSocketAddress

, this method
behaves as if invoking

connect(InetAddress,int)

with the given socket addresses IP address and port number.

**Parameters:** addr

- The remote address.
**Throws:** SocketException

- if the connect fails
**Throws:** IllegalArgumentException

- if

addr

is

null

, or

addr

is a SocketAddress
subclass not supported by this socket
**Throws:** SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address
**Since:** 1.4

- disconnect

```java
public void disconnect()
```

Disconnects the socket. If the socket is closed or not connected,
then this method has no effect.

**See Also:** connect(java.net.InetAddress, int)

- isBound

```java
public boolean isBound()
```

Returns the binding state of the socket.

If the socket was bound prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:** true if the socket successfully bound to an address
**Since:** 1.4

- isConnected

```java
public boolean isConnected()
```

Returns the connection state of the socket.

If the socket was connected prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:** true if the socket successfully connected to a server
**Since:** 1.4

- getInetAddress

```java
public
InetAddress
getInetAddress()
```

Returns the address to which this socket is connected. Returns

null

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:** the address to which this socket is connected.

- getPort

```java
public int getPort()
```

Returns the port number to which this socket is connected.
Returns

-1

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected port number
after the socket is closed.

**Returns:** the port number to which this socket is connected.

- getRemoteSocketAddress

```java
public
SocketAddress
getRemoteSocketAddress()
```

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:** a

SocketAddress

representing the remote
endpoint of this socket, or

null

if it is
not connected yet.
**Since:** 1.4
**See Also:** getInetAddress()

,

getPort()

,

connect(SocketAddress)

- getLocalSocketAddress

```java
public
SocketAddress
getLocalSocketAddress()
```

Returns the address of the endpoint this socket is bound to.

**Returns:** a

SocketAddress

representing the local endpoint of this
socket, or

null

if it is closed or not bound yet.
**Since:** 1.4
**See Also:** getLocalAddress()

,

getLocalPort()

,

bind(SocketAddress)

- send

```java
public void send​(
DatagramPacket
p)
throws
IOException
```

Sends a datagram packet from this socket. The

DatagramPacket

includes information indicating the
data to be sent, its length, the IP address of the remote host,
and the port number on the remote host.

If there is a security manager, and the socket is not currently
connected to a remote address, this method first performs some
security checks. First, if

p.getAddress().isMulticastAddress()

is true, this method calls the
security manager's

checkMulticast

method
with

p.getAddress()

as its argument.
If the evaluation of that expression is false,
this method instead calls the security manager's

checkConnect

method with arguments

p.getAddress().getHostAddress()

and

p.getPort()

. Each call to a security manager method
could result in a SecurityException if the operation is not allowed.

**Parameters:** p

- the

DatagramPacket

to be sent.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkMulticast

or

checkConnect

method doesn't allow the send.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no
guarantee that the exception will be thrown.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.
**Throws:** IllegalArgumentException

- if the socket is connected,
and connected address and packet address differ.
**See Also:** DatagramPacket

,

SecurityManager.checkMulticast(InetAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

- receive

```java
public void receive​(
DatagramPacket
p)
throws
IOException
```

Receives a datagram packet from this socket. When this method
returns, the

DatagramPacket

's buffer is filled with
the data received. The datagram packet also contains the sender's
IP address, and the port number on the sender's machine.

This method blocks until a datagram is received. The

length

field of the datagram packet object contains
the length of the received message. If the message is longer than
the packet's length, the message is truncated.

If there is a security manager, a packet cannot be received if the
security manager's

checkAccept

method
does not allow it.

**Parameters:** p

- the

DatagramPacket

into which to place
the incoming data.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** SocketTimeoutException

- if setSoTimeout was previously called
and the timeout has expired.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.
**See Also:** DatagramPacket

,

DatagramSocket

- getLocalAddress

```java
public
InetAddress
getLocalAddress()
```

Gets the local address to which the socket is bound.

If there is a security manager, its

checkConnect

method is first called
with the host address and

-1

as its arguments to see if the operation is allowed.

**Returns:** the local address to which the socket is bound,

null

if the socket is closed, or
an

InetAddress

representing

wildcard

address if either the socket is not bound, or
the security manager

checkConnect

method does not allow the operation
**Since:** 1.1
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

- getLocalPort

```java
public int getLocalPort()
```

Returns the port number on the local host to which this socket
is bound.

**Returns:** the port number on the local host to which this socket is bound,

-1

if the socket is closed, or

0

if it is not bound yet.

- setSoTimeout

```java
public void setSoTimeout​(int timeout)
throws
SocketException
```

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds. With this option set to a non-zero timeout,
a call to receive() for this DatagramSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
DatagramSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:** timeout

- the specified timeout in milliseconds.
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**Since:** 1.1
**See Also:** getSoTimeout()

- getSoTimeout

```java
public int getSoTimeout()
throws
SocketException
```

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

**Returns:** the setting for SO_TIMEOUT
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**Since:** 1.1
**See Also:** setSoTimeout(int)

- setSendBufferSize

```java
public void setSendBufferSize​(int size)
throws
SocketException
```

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

. The SO_SNDBUF option is used by the
network implementation as a hint to size the underlying
network I/O buffers. The SO_SNDBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be sent on this socket.

As SO_SNDBUF is a hint, applications that want to verify
what size the buffer is should call

getSendBufferSize()

.

Increasing the buffer size may allow multiple outgoing packets
to be queued by the network implementation when the send rate
is high.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

**Parameters:** size

- the size to which to set the send buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Throws:** IllegalArgumentException

- if the value is 0 or is
negative.
**See Also:** getSendBufferSize()

- getSendBufferSize

```java
public int getSendBufferSize()
throws
SocketException
```

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

**Returns:** the value of the SO_SNDBUF option for this

DatagramSocket
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as an UDP error.
**See Also:** setSendBufferSize(int)

- setReceiveBufferSize

```java
public void setReceiveBufferSize​(int size)
throws
SocketException
```

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

. The SO_RCVBUF option is used by
the network implementation as a hint to size the underlying
network I/O buffers. The SO_RCVBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be received on this socket.

Because SO_RCVBUF is a hint, applications that want to
verify what size the buffers were set to should call

getReceiveBufferSize()

.

Increasing SO_RCVBUF may allow the network implementation
to buffer multiple packets when packets arrive faster than
are being received using

receive(DatagramPacket)

.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

**Parameters:** size

- the size to which to set the receive buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as an UDP error.
**Throws:** IllegalArgumentException

- if the value is 0 or is
negative.
**See Also:** getReceiveBufferSize()

- getReceiveBufferSize

```java
public int getReceiveBufferSize()
throws
SocketException
```

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

**Returns:** the value of the SO_RCVBUF option for this

DatagramSocket
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**See Also:** setReceiveBufferSize(int)

- setReuseAddress

```java
public void setReuseAddress​(boolean on)
throws
SocketException
```

Enable/disable the SO_REUSEADDR socket option.

For UDP sockets it may be necessary to bind more than one
socket to the same socket address. This is typically for the
purpose of receiving multicast packets
(See

MulticastSocket

). The

SO_REUSEADDR

socket option allows multiple
sockets to be bound to the same socket address if the

SO_REUSEADDR

socket option is enabled prior
to binding the socket using

bind(SocketAddress)

.

Note: This functionality is not supported by all existing platforms,
so it is implementation specific whether this option will be ignored
or not. However, if it is not supported then

getReuseAddress()

will always return

false

.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:** on

- whether to enable or disable the
**Throws:** SocketException

- if an error occurs enabling or
disabling the

SO_RESUEADDR

socket option,
or the socket is closed.
**Since:** 1.4
**See Also:** getReuseAddress()

,

bind(SocketAddress)

,

isBound()

,

isClosed()

- getReuseAddress

```java
public boolean getReuseAddress()
throws
SocketException
```

Tests if SO_REUSEADDR is enabled.

**Returns:** a

boolean

indicating whether or not SO_REUSEADDR is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Since:** 1.4
**See Also:** setReuseAddress(boolean)

- setBroadcast

```java
public void setBroadcast​(boolean on)
throws
SocketException
```

Enable/disable SO_BROADCAST.

Some operating systems may require that the Java virtual machine be
started with implementation specific privileges to enable this option or
send broadcast datagrams.

**Parameters:** on

- whether or not to have broadcast turned on.
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP
error.
**Since:** 1.4
**See Also:** getBroadcast()

- getBroadcast

```java
public boolean getBroadcast()
throws
SocketException
```

Tests if SO_BROADCAST is enabled.

**Returns:** a

boolean

indicating whether or not SO_BROADCAST is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Since:** 1.4
**See Also:** setBroadcast(boolean)

- setTrafficClass

```java
public void setTrafficClass​(int tc)
throws
SocketException
```

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.
As the underlying network implementation may ignore this
value applications should consider it a hint.

The tc

must

be in the range

0 <= tc <=
255

or an IllegalArgumentException will be thrown.

Notes:

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

**Parameters:** tc

- an

int

value for the bitset.
**Throws:** SocketException

- if there is an error setting the
traffic class or type-of-service
**Since:** 1.4
**See Also:** getTrafficClass()

- getTrafficClass

```java
public int getTrafficClass()
throws
SocketException
```

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

As the underlying network implementation may ignore the
traffic class or type-of-service set using

setTrafficClass(int)

this method may return a different value than was previously
set using the

setTrafficClass(int)

method on this
DatagramSocket.

**Returns:** the traffic class or type-of-service already set
**Throws:** SocketException

- if there is an error obtaining the
traffic class or type-of-service value.
**Since:** 1.4
**See Also:** setTrafficClass(int)

- close

```java
public void close()
```

Closes this datagram socket.

Any thread currently blocked in

receive(java.net.DatagramPacket)

upon this socket
will throw a

SocketException

.

If this socket has an associated channel then the channel is closed
as well.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable

- isClosed

```java
public boolean isClosed()
```

Returns whether the socket is closed or not.

**Returns:** true if the socket has been closed
**Since:** 1.4

- getChannel

```java
public
DatagramChannel
getChannel()
```

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

A datagram socket will have a channel if, and only if, the channel
itself was created via the

DatagramChannel.open

method.

**Returns:** the datagram channel associated with this datagram socket,
or

null

if this socket was not created for a channel
**Since:** 1.4

- setDatagramSocketImplFactory

```java
public static void setDatagramSocketImplFactory​(
DatagramSocketImplFactory
fac)
throws
IOException
```

Sets the datagram socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new datagram socket, the socket
implementation factory's

createDatagramSocketImpl

method is
called to create the actual datagram socket implementation.

Passing

null

to the method is a no-op unless the factory
was already set.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** fac

- the desired factory.
**Throws:** IOException

- if an I/O error occurs when setting the
datagram socket factory.
**Throws:** SocketException

- if the factory is already defined.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**Since:** 1.3
**See Also:** DatagramSocketImplFactory.createDatagramSocketImpl()

,

SecurityManager.checkSetFactory()

- setOption

```java
public <T>
DatagramSocket
setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be valid for some options.
**Returns:** this DatagramSocket
**Throws:** UnsupportedOperationException

- if the datagram socket
does not support the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs, or if the socket is closed.
**Throws:** SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.
**Throws:** NullPointerException

- if name is

null
**Since:** 9

- getOption

```java
public <T> T getOption​(
SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the datagram socket
does not support the option.
**Throws:** IOException

- if an I/O error occurs, or if the socket is closed.
**Throws:** NullPointerException

- if name is

null
**Throws:** SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.
**Since:** 9

- supportedOptions

```java
public
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of the socket options supported by this socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:** A set of the socket options supported by this socket. This set
may be empty if the socket's DatagramSocketImpl cannot be created.
**Since:** 9

---

#### Method Detail

bind

```java
public void bind​(
SocketAddress
addr)
throws
SocketException
```

Binds this DatagramSocket to a specific address and port.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:** addr

- The address and port to bind to.
**Throws:** SocketException

- if any error happens during the bind, or if the
socket is already bound.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if addr is a SocketAddress subclass
not supported by this socket.
**Since:** 1.4

---

#### bind

public void bind​(

SocketAddress

addr)
throws

SocketException

Binds this DatagramSocket to a specific address and port.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

connect

```java
public void connect​(
InetAddress
address,
int port)
```

Connects the socket to a remote address for this socket. When a
socket is connected to a remote address, packets may only be
sent to or received from that address. By default a datagram
socket is not connected.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException. Note, there is no
guarantee that the exception will be thrown.

If a security manager has been installed then it is invoked to check
access to the remote address. Specifically, if the given

address

is a

multicast address

,
the security manager's

checkMulticast

method is invoked with the given

address

.
Otherwise, the security manager's

checkConnect

and

checkAccept

methods
are invoked, with the given

address

and

port

, to
verify that datagrams are permitted to be sent and received
respectively.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

**Parameters:** address

- the remote address for the socket
**Parameters:** port

- the remote port for the socket.
**Throws:** IllegalArgumentException

- if the address is null, or the port is out of range.
**Throws:** SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address
**See Also:** disconnect()

---

#### connect

public void connect​(

InetAddress

address,
int port)

Connects the socket to a remote address for this socket. When a
socket is connected to a remote address, packets may only be
sent to or received from that address. By default a datagram
socket is not connected.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException. Note, there is no
guarantee that the exception will be thrown.

If a security manager has been installed then it is invoked to check
access to the remote address. Specifically, if the given

address

is a

multicast address

,
the security manager's

checkMulticast

method is invoked with the given

address

.
Otherwise, the security manager's

checkConnect

and

checkAccept

methods
are invoked, with the given

address

and

port

, to
verify that datagrams are permitted to be sent and received
respectively.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException. Note, there is no
guarantee that the exception will be thrown.

If a security manager has been installed then it is invoked to check
access to the remote address. Specifically, if the given

address

is a

multicast address

,
the security manager's

checkMulticast

method is invoked with the given

address

.
Otherwise, the security manager's

checkConnect

and

checkAccept

methods
are invoked, with the given

address

and

port

, to
verify that datagrams are permitted to be sent and received
respectively.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

If a security manager has been installed then it is invoked to check
access to the remote address. Specifically, if the given

address

is a

multicast address

,
the security manager's

checkMulticast

method is invoked with the given

address

.
Otherwise, the security manager's

checkConnect

and

checkAccept

methods
are invoked, with the given

address

and

port

, to
verify that datagrams are permitted to be sent and received
respectively.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

When a socket is connected,

receive

and

send

will not perform any security checks

on incoming and outgoing packets, other than matching the packet's
and the socket's address and port. On a send operation, if the
packet's address is set and the packet's address and the socket's
address do not match, an

IllegalArgumentException

will be
thrown. A socket connected to a multicast address may only be used
to send packets.

connect

```java
public void connect​(
SocketAddress
addr)
throws
SocketException
```

Connects this socket to a remote socket address (IP address + port number).

If given an

InetSocketAddress

, this method
behaves as if invoking

connect(InetAddress,int)

with the given socket addresses IP address and port number.

**Parameters:** addr

- The remote address.
**Throws:** SocketException

- if the connect fails
**Throws:** IllegalArgumentException

- if

addr

is

null

, or

addr

is a SocketAddress
subclass not supported by this socket
**Throws:** SecurityException

- if a security manager has been installed and it does
not permit access to the given remote address
**Since:** 1.4

---

#### connect

public void connect​(

SocketAddress

addr)
throws

SocketException

Connects this socket to a remote socket address (IP address + port number).

If given an

InetSocketAddress

, this method
behaves as if invoking

connect(InetAddress,int)

with the given socket addresses IP address and port number.

If given an

InetSocketAddress

, this method
behaves as if invoking

connect(InetAddress,int)

with the given socket addresses IP address and port number.

disconnect

```java
public void disconnect()
```

Disconnects the socket. If the socket is closed or not connected,
then this method has no effect.

**See Also:** connect(java.net.InetAddress, int)

---

#### disconnect

public void disconnect()

Disconnects the socket. If the socket is closed or not connected,
then this method has no effect.

isBound

```java
public boolean isBound()
```

Returns the binding state of the socket.

If the socket was bound prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:** true if the socket successfully bound to an address
**Since:** 1.4

---

#### isBound

public boolean isBound()

Returns the binding state of the socket.

If the socket was bound prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

If the socket was bound prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

isConnected

```java
public boolean isConnected()
```

Returns the connection state of the socket.

If the socket was connected prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

**Returns:** true if the socket successfully connected to a server
**Since:** 1.4

---

#### isConnected

public boolean isConnected()

Returns the connection state of the socket.

If the socket was connected prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

If the socket was connected prior to being

closed

,
then this method will continue to return

true

after the socket is closed.

getInetAddress

```java
public
InetAddress
getInetAddress()
```

Returns the address to which this socket is connected. Returns

null

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:** the address to which this socket is connected.

---

#### getInetAddress

public

InetAddress

getInetAddress()

Returns the address to which this socket is connected. Returns

null

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

getPort

```java
public int getPort()
```

Returns the port number to which this socket is connected.
Returns

-1

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected port number
after the socket is closed.

**Returns:** the port number to which this socket is connected.

---

#### getPort

public int getPort()

Returns the port number to which this socket is connected.
Returns

-1

if the socket is not connected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected port number
after the socket is closed.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected port number
after the socket is closed.

getRemoteSocketAddress

```java
public
SocketAddress
getRemoteSocketAddress()
```

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

**Returns:** a

SocketAddress

representing the remote
endpoint of this socket, or

null

if it is
not connected yet.
**Since:** 1.4
**See Also:** getInetAddress()

,

getPort()

,

connect(SocketAddress)

---

#### getRemoteSocketAddress

public

SocketAddress

getRemoteSocketAddress()

Returns the address of the endpoint this socket is connected to, or

null

if it is unconnected.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

If the socket was connected prior to being

closed

,
then this method will continue to return the connected address
after the socket is closed.

getLocalSocketAddress

```java
public
SocketAddress
getLocalSocketAddress()
```

Returns the address of the endpoint this socket is bound to.

**Returns:** a

SocketAddress

representing the local endpoint of this
socket, or

null

if it is closed or not bound yet.
**Since:** 1.4
**See Also:** getLocalAddress()

,

getLocalPort()

,

bind(SocketAddress)

---

#### getLocalSocketAddress

public

SocketAddress

getLocalSocketAddress()

Returns the address of the endpoint this socket is bound to.

send

```java
public void send​(
DatagramPacket
p)
throws
IOException
```

Sends a datagram packet from this socket. The

DatagramPacket

includes information indicating the
data to be sent, its length, the IP address of the remote host,
and the port number on the remote host.

If there is a security manager, and the socket is not currently
connected to a remote address, this method first performs some
security checks. First, if

p.getAddress().isMulticastAddress()

is true, this method calls the
security manager's

checkMulticast

method
with

p.getAddress()

as its argument.
If the evaluation of that expression is false,
this method instead calls the security manager's

checkConnect

method with arguments

p.getAddress().getHostAddress()

and

p.getPort()

. Each call to a security manager method
could result in a SecurityException if the operation is not allowed.

**Parameters:** p

- the

DatagramPacket

to be sent.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkMulticast

or

checkConnect

method doesn't allow the send.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no
guarantee that the exception will be thrown.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.
**Throws:** IllegalArgumentException

- if the socket is connected,
and connected address and packet address differ.
**See Also:** DatagramPacket

,

SecurityManager.checkMulticast(InetAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

---

#### send

public void send​(

DatagramPacket

p)
throws

IOException

Sends a datagram packet from this socket. The

DatagramPacket

includes information indicating the
data to be sent, its length, the IP address of the remote host,
and the port number on the remote host.

If there is a security manager, and the socket is not currently
connected to a remote address, this method first performs some
security checks. First, if

p.getAddress().isMulticastAddress()

is true, this method calls the
security manager's

checkMulticast

method
with

p.getAddress()

as its argument.
If the evaluation of that expression is false,
this method instead calls the security manager's

checkConnect

method with arguments

p.getAddress().getHostAddress()

and

p.getPort()

. Each call to a security manager method
could result in a SecurityException if the operation is not allowed.

If there is a security manager, and the socket is not currently
connected to a remote address, this method first performs some
security checks. First, if

p.getAddress().isMulticastAddress()

is true, this method calls the
security manager's

checkMulticast

method
with

p.getAddress()

as its argument.
If the evaluation of that expression is false,
this method instead calls the security manager's

checkConnect

method with arguments

p.getAddress().getHostAddress()

and

p.getPort()

. Each call to a security manager method
could result in a SecurityException if the operation is not allowed.

receive

```java
public void receive​(
DatagramPacket
p)
throws
IOException
```

Receives a datagram packet from this socket. When this method
returns, the

DatagramPacket

's buffer is filled with
the data received. The datagram packet also contains the sender's
IP address, and the port number on the sender's machine.

This method blocks until a datagram is received. The

length

field of the datagram packet object contains
the length of the received message. If the message is longer than
the packet's length, the message is truncated.

If there is a security manager, a packet cannot be received if the
security manager's

checkAccept

method
does not allow it.

**Parameters:** p

- the

DatagramPacket

into which to place
the incoming data.
**Throws:** IOException

- if an I/O error occurs.
**Throws:** SocketTimeoutException

- if setSoTimeout was previously called
and the timeout has expired.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode.
**See Also:** DatagramPacket

,

DatagramSocket

---

#### receive

public void receive​(

DatagramPacket

p)
throws

IOException

Receives a datagram packet from this socket. When this method
returns, the

DatagramPacket

's buffer is filled with
the data received. The datagram packet also contains the sender's
IP address, and the port number on the sender's machine.

This method blocks until a datagram is received. The

length

field of the datagram packet object contains
the length of the received message. If the message is longer than
the packet's length, the message is truncated.

If there is a security manager, a packet cannot be received if the
security manager's

checkAccept

method
does not allow it.

This method blocks until a datagram is received. The

length

field of the datagram packet object contains
the length of the received message. If the message is longer than
the packet's length, the message is truncated.

If there is a security manager, a packet cannot be received if the
security manager's

checkAccept

method
does not allow it.

If there is a security manager, a packet cannot be received if the
security manager's

checkAccept

method
does not allow it.

getLocalAddress

```java
public
InetAddress
getLocalAddress()
```

Gets the local address to which the socket is bound.

If there is a security manager, its

checkConnect

method is first called
with the host address and

-1

as its arguments to see if the operation is allowed.

**Returns:** the local address to which the socket is bound,

null

if the socket is closed, or
an

InetAddress

representing

wildcard

address if either the socket is not bound, or
the security manager

checkConnect

method does not allow the operation
**Since:** 1.1
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

---

#### getLocalAddress

public

InetAddress

getLocalAddress()

Gets the local address to which the socket is bound.

If there is a security manager, its

checkConnect

method is first called
with the host address and

-1

as its arguments to see if the operation is allowed.

If there is a security manager, its

checkConnect

method is first called
with the host address and

-1

as its arguments to see if the operation is allowed.

getLocalPort

```java
public int getLocalPort()
```

Returns the port number on the local host to which this socket
is bound.

**Returns:** the port number on the local host to which this socket is bound,

-1

if the socket is closed, or

0

if it is not bound yet.

---

#### getLocalPort

public int getLocalPort()

Returns the port number on the local host to which this socket
is bound.

setSoTimeout

```java
public void setSoTimeout​(int timeout)
throws
SocketException
```

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds. With this option set to a non-zero timeout,
a call to receive() for this DatagramSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
DatagramSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:** timeout

- the specified timeout in milliseconds.
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**Since:** 1.1
**See Also:** getSoTimeout()

---

#### setSoTimeout

public void setSoTimeout​(int timeout)
throws

SocketException

Enable/disable SO_TIMEOUT with the specified timeout, in
milliseconds. With this option set to a non-zero timeout,
a call to receive() for this DatagramSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
DatagramSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

getSoTimeout

```java
public int getSoTimeout()
throws
SocketException
```

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

**Returns:** the setting for SO_TIMEOUT
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**Since:** 1.1
**See Also:** setSoTimeout(int)

---

#### getSoTimeout

public int getSoTimeout()
throws

SocketException

Retrieve setting for SO_TIMEOUT. 0 returns implies that the
option is disabled (i.e., timeout of infinity).

setSendBufferSize

```java
public void setSendBufferSize​(int size)
throws
SocketException
```

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

. The SO_SNDBUF option is used by the
network implementation as a hint to size the underlying
network I/O buffers. The SO_SNDBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be sent on this socket.

As SO_SNDBUF is a hint, applications that want to verify
what size the buffer is should call

getSendBufferSize()

.

Increasing the buffer size may allow multiple outgoing packets
to be queued by the network implementation when the send rate
is high.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

**Parameters:** size

- the size to which to set the send buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Throws:** IllegalArgumentException

- if the value is 0 or is
negative.
**See Also:** getSendBufferSize()

---

#### setSendBufferSize

public void setSendBufferSize​(int size)
throws

SocketException

Sets the SO_SNDBUF option to the specified value for this

DatagramSocket

. The SO_SNDBUF option is used by the
network implementation as a hint to size the underlying
network I/O buffers. The SO_SNDBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be sent on this socket.

As SO_SNDBUF is a hint, applications that want to verify
what size the buffer is should call

getSendBufferSize()

.

Increasing the buffer size may allow multiple outgoing packets
to be queued by the network implementation when the send rate
is high.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

As SO_SNDBUF is a hint, applications that want to verify
what size the buffer is should call

getSendBufferSize()

.

Increasing the buffer size may allow multiple outgoing packets
to be queued by the network implementation when the send rate
is high.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

Increasing the buffer size may allow multiple outgoing packets
to be queued by the network implementation when the send rate
is high.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

Note: If

send(DatagramPacket)

is used to send a

DatagramPacket

that is larger than the setting
of SO_SNDBUF then it is implementation specific if the
packet is sent or discarded.

getSendBufferSize

```java
public int getSendBufferSize()
throws
SocketException
```

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

**Returns:** the value of the SO_SNDBUF option for this

DatagramSocket
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as an UDP error.
**See Also:** setSendBufferSize(int)

---

#### getSendBufferSize

public int getSendBufferSize()
throws

SocketException

Get value of the SO_SNDBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for output on this

DatagramSocket

.

setReceiveBufferSize

```java
public void setReceiveBufferSize​(int size)
throws
SocketException
```

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

. The SO_RCVBUF option is used by
the network implementation as a hint to size the underlying
network I/O buffers. The SO_RCVBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be received on this socket.

Because SO_RCVBUF is a hint, applications that want to
verify what size the buffers were set to should call

getReceiveBufferSize()

.

Increasing SO_RCVBUF may allow the network implementation
to buffer multiple packets when packets arrive faster than
are being received using

receive(DatagramPacket)

.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

**Parameters:** size

- the size to which to set the receive buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as an UDP error.
**Throws:** IllegalArgumentException

- if the value is 0 or is
negative.
**See Also:** getReceiveBufferSize()

---

#### setReceiveBufferSize

public void setReceiveBufferSize​(int size)
throws

SocketException

Sets the SO_RCVBUF option to the specified value for this

DatagramSocket

. The SO_RCVBUF option is used by
the network implementation as a hint to size the underlying
network I/O buffers. The SO_RCVBUF setting may also be used
by the network implementation to determine the maximum size
of the packet that can be received on this socket.

Because SO_RCVBUF is a hint, applications that want to
verify what size the buffers were set to should call

getReceiveBufferSize()

.

Increasing SO_RCVBUF may allow the network implementation
to buffer multiple packets when packets arrive faster than
are being received using

receive(DatagramPacket)

.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

Because SO_RCVBUF is a hint, applications that want to
verify what size the buffers were set to should call

getReceiveBufferSize()

.

Increasing SO_RCVBUF may allow the network implementation
to buffer multiple packets when packets arrive faster than
are being received using

receive(DatagramPacket)

.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

Increasing SO_RCVBUF may allow the network implementation
to buffer multiple packets when packets arrive faster than
are being received using

receive(DatagramPacket)

.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

Note: It is implementation specific if a packet larger
than SO_RCVBUF can be received.

getReceiveBufferSize

```java
public int getReceiveBufferSize()
throws
SocketException
```

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

**Returns:** the value of the SO_RCVBUF option for this

DatagramSocket
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP error.
**See Also:** setReceiveBufferSize(int)

---

#### getReceiveBufferSize

public int getReceiveBufferSize()
throws

SocketException

Get value of the SO_RCVBUF option for this

DatagramSocket

, that is the
buffer size used by the platform for input on this

DatagramSocket

.

setReuseAddress

```java
public void setReuseAddress​(boolean on)
throws
SocketException
```

Enable/disable the SO_REUSEADDR socket option.

For UDP sockets it may be necessary to bind more than one
socket to the same socket address. This is typically for the
purpose of receiving multicast packets
(See

MulticastSocket

). The

SO_REUSEADDR

socket option allows multiple
sockets to be bound to the same socket address if the

SO_REUSEADDR

socket option is enabled prior
to binding the socket using

bind(SocketAddress)

.

Note: This functionality is not supported by all existing platforms,
so it is implementation specific whether this option will be ignored
or not. However, if it is not supported then

getReuseAddress()

will always return

false

.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:** on

- whether to enable or disable the
**Throws:** SocketException

- if an error occurs enabling or
disabling the

SO_RESUEADDR

socket option,
or the socket is closed.
**Since:** 1.4
**See Also:** getReuseAddress()

,

bind(SocketAddress)

,

isBound()

,

isClosed()

---

#### setReuseAddress

public void setReuseAddress​(boolean on)
throws

SocketException

Enable/disable the SO_REUSEADDR socket option.

For UDP sockets it may be necessary to bind more than one
socket to the same socket address. This is typically for the
purpose of receiving multicast packets
(See

MulticastSocket

). The

SO_REUSEADDR

socket option allows multiple
sockets to be bound to the same socket address if the

SO_REUSEADDR

socket option is enabled prior
to binding the socket using

bind(SocketAddress)

.

Note: This functionality is not supported by all existing platforms,
so it is implementation specific whether this option will be ignored
or not. However, if it is not supported then

getReuseAddress()

will always return

false

.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

For UDP sockets it may be necessary to bind more than one
socket to the same socket address. This is typically for the
purpose of receiving multicast packets
(See

MulticastSocket

). The

SO_REUSEADDR

socket option allows multiple
sockets to be bound to the same socket address if the

SO_REUSEADDR

socket option is enabled prior
to binding the socket using

bind(SocketAddress)

.

Note: This functionality is not supported by all existing platforms,
so it is implementation specific whether this option will be ignored
or not. However, if it is not supported then

getReuseAddress()

will always return

false

.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

Note: This functionality is not supported by all existing platforms,
so it is implementation specific whether this option will be ignored
or not. However, if it is not supported then

getReuseAddress()

will always return

false

.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

When a

DatagramSocket

is created the initial setting
of

SO_REUSEADDR

is disabled.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

The behaviour when

SO_REUSEADDR

is enabled or
disabled after a socket is bound (See

isBound()

)
is not defined.

getReuseAddress

```java
public boolean getReuseAddress()
throws
SocketException
```

Tests if SO_REUSEADDR is enabled.

**Returns:** a

boolean

indicating whether or not SO_REUSEADDR is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Since:** 1.4
**See Also:** setReuseAddress(boolean)

---

#### getReuseAddress

public boolean getReuseAddress()
throws

SocketException

Tests if SO_REUSEADDR is enabled.

setBroadcast

```java
public void setBroadcast​(boolean on)
throws
SocketException
```

Enable/disable SO_BROADCAST.

Some operating systems may require that the Java virtual machine be
started with implementation specific privileges to enable this option or
send broadcast datagrams.

**Parameters:** on

- whether or not to have broadcast turned on.
**Throws:** SocketException

- if there is an error in the underlying protocol, such as an UDP
error.
**Since:** 1.4
**See Also:** getBroadcast()

---

#### setBroadcast

public void setBroadcast​(boolean on)
throws

SocketException

Enable/disable SO_BROADCAST.

Some operating systems may require that the Java virtual machine be
started with implementation specific privileges to enable this option or
send broadcast datagrams.

Some operating systems may require that the Java virtual machine be
started with implementation specific privileges to enable this option or
send broadcast datagrams.

getBroadcast

```java
public boolean getBroadcast()
throws
SocketException
```

Tests if SO_BROADCAST is enabled.

**Returns:** a

boolean

indicating whether or not SO_BROADCAST is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as an UDP error.
**Since:** 1.4
**See Also:** setBroadcast(boolean)

---

#### getBroadcast

public boolean getBroadcast()
throws

SocketException

Tests if SO_BROADCAST is enabled.

setTrafficClass

```java
public void setTrafficClass​(int tc)
throws
SocketException
```

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.
As the underlying network implementation may ignore this
value applications should consider it a hint.

The tc

must

be in the range

0 <= tc <=
255

or an IllegalArgumentException will be thrown.

Notes:

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

**Parameters:** tc

- an

int

value for the bitset.
**Throws:** SocketException

- if there is an error setting the
traffic class or type-of-service
**Since:** 1.4
**See Also:** getTrafficClass()

---

#### setTrafficClass

public void setTrafficClass​(int tc)
throws

SocketException

Sets traffic class or type-of-service octet in the IP
datagram header for datagrams sent from this DatagramSocket.
As the underlying network implementation may ignore this
value applications should consider it a hint.

The tc

must

be in the range

0 <= tc <=
255

or an IllegalArgumentException will be thrown.

Notes:

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

The tc

must

be in the range

0 <= tc <=
255

or an IllegalArgumentException will be thrown.

Notes:

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

Notes:

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

For Internet Protocol v4 the value consists of an

integer

, the least significant 8 bits of which
represent the value of the TOS octet in IP packets sent by
the socket.
RFC 1349 defines the TOS values as follows:

- IPTOS_LOWCOST (0x02)
- IPTOS_RELIABILITY (0x04)
- IPTOS_THROUGHPUT (0x08)
- IPTOS_LOWDELAY (0x10)

The last low order bit is always ignored as this
corresponds to the MBZ (must be zero) bit.

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

IPTOS_LOWCOST (0x02)

IPTOS_RELIABILITY (0x04)

IPTOS_THROUGHPUT (0x08)

IPTOS_LOWDELAY (0x10)

Setting bits in the precedence field may result in a
SocketException indicating that the operation is not
permitted.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

for Internet Protocol v6

tc

is the value that
would be placed into the sin6_flowinfo field of the IP header.

getTrafficClass

```java
public int getTrafficClass()
throws
SocketException
```

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

As the underlying network implementation may ignore the
traffic class or type-of-service set using

setTrafficClass(int)

this method may return a different value than was previously
set using the

setTrafficClass(int)

method on this
DatagramSocket.

**Returns:** the traffic class or type-of-service already set
**Throws:** SocketException

- if there is an error obtaining the
traffic class or type-of-service value.
**Since:** 1.4
**See Also:** setTrafficClass(int)

---

#### getTrafficClass

public int getTrafficClass()
throws

SocketException

Gets traffic class or type-of-service in the IP datagram
header for packets sent from this DatagramSocket.

As the underlying network implementation may ignore the
traffic class or type-of-service set using

setTrafficClass(int)

this method may return a different value than was previously
set using the

setTrafficClass(int)

method on this
DatagramSocket.

As the underlying network implementation may ignore the
traffic class or type-of-service set using

setTrafficClass(int)

this method may return a different value than was previously
set using the

setTrafficClass(int)

method on this
DatagramSocket.

close

```java
public void close()
```

Closes this datagram socket.

Any thread currently blocked in

receive(java.net.DatagramPacket)

upon this socket
will throw a

SocketException

.

If this socket has an associated channel then the channel is closed
as well.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable

---

#### close

public void close()

Closes this datagram socket.

Any thread currently blocked in

receive(java.net.DatagramPacket)

upon this socket
will throw a

SocketException

.

If this socket has an associated channel then the channel is closed
as well.

Any thread currently blocked in

receive(java.net.DatagramPacket)

upon this socket
will throw a

SocketException

.

If this socket has an associated channel then the channel is closed
as well.

If this socket has an associated channel then the channel is closed
as well.

isClosed

```java
public boolean isClosed()
```

Returns whether the socket is closed or not.

**Returns:** true if the socket has been closed
**Since:** 1.4

---

#### isClosed

public boolean isClosed()

Returns whether the socket is closed or not.

getChannel

```java
public
DatagramChannel
getChannel()
```

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

A datagram socket will have a channel if, and only if, the channel
itself was created via the

DatagramChannel.open

method.

**Returns:** the datagram channel associated with this datagram socket,
or

null

if this socket was not created for a channel
**Since:** 1.4

---

#### getChannel

public

DatagramChannel

getChannel()

Returns the unique

DatagramChannel

object
associated with this datagram socket, if any.

A datagram socket will have a channel if, and only if, the channel
itself was created via the

DatagramChannel.open

method.

A datagram socket will have a channel if, and only if, the channel
itself was created via the

DatagramChannel.open

method.

setDatagramSocketImplFactory

```java
public static void setDatagramSocketImplFactory​(
DatagramSocketImplFactory
fac)
throws
IOException
```

Sets the datagram socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new datagram socket, the socket
implementation factory's

createDatagramSocketImpl

method is
called to create the actual datagram socket implementation.

Passing

null

to the method is a no-op unless the factory
was already set.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** fac

- the desired factory.
**Throws:** IOException

- if an I/O error occurs when setting the
datagram socket factory.
**Throws:** SocketException

- if the factory is already defined.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**Since:** 1.3
**See Also:** DatagramSocketImplFactory.createDatagramSocketImpl()

,

SecurityManager.checkSetFactory()

---

#### setDatagramSocketImplFactory

public static void setDatagramSocketImplFactory​(

DatagramSocketImplFactory

fac)
throws

IOException

Sets the datagram socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new datagram socket, the socket
implementation factory's

createDatagramSocketImpl

method is
called to create the actual datagram socket implementation.

Passing

null

to the method is a no-op unless the factory
was already set.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

When an application creates a new datagram socket, the socket
implementation factory's

createDatagramSocketImpl

method is
called to create the actual datagram socket implementation.

Passing

null

to the method is a no-op unless the factory
was already set.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

Passing

null

to the method is a no-op unless the factory
was already set.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

setOption

```java
public <T>
DatagramSocket
setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be valid for some options.
**Returns:** this DatagramSocket
**Throws:** UnsupportedOperationException

- if the datagram socket
does not support the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs, or if the socket is closed.
**Throws:** SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.
**Throws:** NullPointerException

- if name is

null
**Since:** 9

---

#### setOption

public <T>

DatagramSocket

setOption​(

SocketOption

<T> name,
T value)
throws

IOException

Sets the value of a socket option.

getOption

```java
public <T> T getOption​(
SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the datagram socket
does not support the option.
**Throws:** IOException

- if an I/O error occurs, or if the socket is closed.
**Throws:** NullPointerException

- if name is

null
**Throws:** SecurityException

- if a security manager is set and if the socket
option requires a security permission and if the caller does
not have the required permission.

StandardSocketOptions

do not require any security permission.
**Since:** 9

---

#### getOption

public <T> T getOption​(

SocketOption

<T> name)
throws

IOException

Returns the value of a socket option.

supportedOptions

```java
public
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of the socket options supported by this socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:** A set of the socket options supported by this socket. This set
may be empty if the socket's DatagramSocketImpl cannot be created.
**Since:** 9

---

#### supportedOptions

public

Set

<

SocketOption

<?>> supportedOptions()

Returns a set of the socket options supported by this socket.

This method will continue to return the set of options even after
the socket has been closed.

---

