# Interface SocketOptions

**Source:** `java.base\java\net\SocketOptions.html`

### Class Description

```java
public interface
SocketOptions
```

Interface of methods to get/set socket options. This interface is
implemented by:

SocketImpl

and

DatagramSocketImpl

.
Subclasses of these should override the methods
of this interface in order to support their own options.

The methods and constants which specify options in this interface are
for implementation only. If you're not subclassing SocketImpl or
DatagramSocketImpl,

you won't use these directly.

There are
type-safe methods to get/set each of these options in Socket, ServerSocket,
DatagramSocket and MulticastSocket.

**All Known Implementing Classes:** DatagramSocketImpl

,

SocketImpl

---

### Field Details

#### @Native

static final int TCP_NODELAY

Disable Nagle's algorithm for this connection. Written data
to the network is not buffered pending acknowledgement of
previously written data.

Valid for TCP only: SocketImpl.

**See Also:**
- Socket.setTcpNoDelay(boolean)

,

Socket.getTcpNoDelay()

,

Constant Field Values

---

#### @Native

static final int SO_BINDADDR

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed). The default local
address of a socket is INADDR_ANY, meaning any local address on a
multi-homed host. A multi-homed host can use this option to accept
connections to only one of its addresses (in the case of a
ServerSocket or DatagramSocket), or to specify its return address
to the peer (for a Socket or DatagramSocket). The parameter of
this option is an InetAddress.

This option

must

be specified in the constructor.

Valid for: SocketImpl, DatagramSocketImpl

**See Also:**
- Socket.getLocalAddress()

,

DatagramSocket.getLocalAddress()

,

Constant Field Values

---

#### @Native

static final int SO_REUSEADDR

Sets SO_REUSEADDR for a socket. This is used only for MulticastSockets
in java, and it is set by default for MulticastSockets.

Valid for: DatagramSocketImpl

**See Also:**
- Constant Field Values

---

#### @Native

static final int SO_REUSEPORT

Sets SO_REUSEPORT for a socket. This option enables and disables
the ability to have multiple sockets listen to the same address
and port.

Valid for: SocketImpl, DatagramSocketImpl

**See Also:**
- StandardSocketOptions.SO_REUSEPORT

,

Constant Field Values

**Since:**
- 9

---

#### @Native

static final int SO_BROADCAST

Sets SO_BROADCAST for a socket. This option enables and disables
the ability of the process to send broadcast messages. It is supported
for only datagram sockets and only on networks that support
the concept of a broadcast message (e.g. Ethernet, token ring, etc.),
and it is set by default for DatagramSockets.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### @Native

static final int IP_MULTICAST_IF

Set which outgoing interface on which to send multicast packets.
Useful on hosts with multiple network interfaces, where applications
want to use other than the system default. Takes/returns an InetAddress.

Valid for Multicast: DatagramSocketImpl

**See Also:**
- MulticastSocket.setInterface(InetAddress)

,

MulticastSocket.getInterface()

,

Constant Field Values

---

#### @Native

static final int IP_MULTICAST_IF2

Same as above. This option is introduced so that the behaviour
with IP_MULTICAST_IF will be kept the same as before, while
this new option can support setting outgoing interfaces with either
IPv4 and IPv6 addresses.

NOTE: make sure there is no conflict with this

**See Also:**
- MulticastSocket.setNetworkInterface(NetworkInterface)

,

MulticastSocket.getNetworkInterface()

,

Constant Field Values

**Since:**
- 1.4

---

#### @Native

static final int IP_MULTICAST_LOOP

This option enables or disables local loopback of multicast datagrams.
This option is enabled by default for Multicast Sockets.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### @Native

static final int IP_TOS

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### @Native

static final int SO_LINGER

Specify a linger-on-close timeout. This option disables/enables
immediate return from a

close()

of a TCP Socket. Enabling
this option with a non-zero Integer

timeout

means that a

close()

will block pending the transmission and acknowledgement
of all data written to the peer, at which point the socket is closed

gracefully

. Upon reaching the linger timeout, the socket is
closed

forcefully

, with a TCP RST. Enabling the option with a
timeout of zero does a forceful close immediately. If the specified
timeout value exceeds 65,535 it will be reduced to 65,535.

Valid only for TCP: SocketImpl

**See Also:**
- Socket.setSoLinger(boolean, int)

,

Socket.getSoLinger()

,

Constant Field Values

---

#### @Native

static final int SO_TIMEOUT

Set a timeout on blocking Socket operations:

```java
ServerSocket.accept();
SocketInputStream.read();
DatagramSocket.receive();
```

The option must be set prior to entering a blocking
operation to take effect. If the timeout expires and the
operation would continue to block,

java.io.InterruptedIOException

is raised. The Socket is
not closed in this case.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:**
- Socket.setSoTimeout(int)

,

ServerSocket.setSoTimeout(int)

,

DatagramSocket.setSoTimeout(int)

,

Constant Field Values

---

#### @Native

static final int SO_SNDBUF

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be sent over the socket. When
used in get, this must return the size of the buffer actually
used by the platform when sending out data on this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:**
- Socket.setSendBufferSize(int)

,

Socket.getSendBufferSize()

,

DatagramSocket.setSendBufferSize(int)

,

DatagramSocket.getSendBufferSize()

,

Constant Field Values

---

#### @Native

static final int SO_RCVBUF

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be received over the
socket. When used in get, this must return the size of the
buffer actually used by the platform when receiving in data on
this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:**
- Socket.setReceiveBufferSize(int)

,

Socket.getReceiveBufferSize()

,

DatagramSocket.setReceiveBufferSize(int)

,

DatagramSocket.getReceiveBufferSize()

,

Constant Field Values

---

#### @Native

static final int SO_KEEPALIVE

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer. This probe is a
TCP segment to which the peer must respond.
One of three responses is expected:
1. The peer responds with the expected ACK. The application is not
notified (since everything is OK). TCP will send another probe
following another 2 hours of inactivity.
2. The peer responds with an RST, which tells the local TCP that
the peer host has crashed and rebooted. The socket is closed.
3. There is no response from the peer. The socket is closed.

The purpose of this option is to detect if the peer host crashes.

Valid only for TCP socket: SocketImpl

**See Also:**
- Socket.setKeepAlive(boolean)

,

Socket.getKeepAlive()

,

Constant Field Values

---

#### @Native

static final int SO_OOBINLINE

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.
When the option is disabled (which is the default) urgent data
is silently discarded.

**See Also:**
- Socket.setOOBInline(boolean)

,

Socket.getOOBInline()

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void setOption​(int optID,

Object
value)
throws
SocketException

Enable/disable the option specified by

optID

. If the option
is to be enabled, and it takes an option-specific "value", this is
passed in

value

. The actual type of value is option-specific,
and it is an error to pass something that isn't of the expected type:

```java
SocketImpl s;
...
s.setOption(SO_LINGER, new Integer(10));
// OK - set SO_LINGER w/ timeout of 10 sec.
s.setOption(SO_LINGER, new Double(10));
// ERROR - expects java.lang.Integer
```

If the requested option is binary, it can be set using this method by
a java.lang.Boolean:

```java
s.setOption(TCP_NODELAY, Boolean.TRUE);
// OK - enables TCP_NODELAY, a binary option
```

Any option can be disabled using this method with a Boolean.FALSE:

```java
s.setOption(TCP_NODELAY, Boolean.FALSE);
// OK - disables TCP_NODELAY
s.setOption(SO_LINGER, Boolean.FALSE);
// OK - disables SO_LINGER
```

For an option that has a notion of on and off, and requires
a non-boolean parameter, setting its value to anything other than

Boolean.FALSE

implicitly enables it.

Throws SocketException if the option is unrecognized,
the socket is closed, or some low-level error occurred

**Parameters:**
- optID

- identifies the option
- value

- the parameter of the socket option

**Throws:**
- SocketException

- if the option is unrecognized,
the socket is closed, or some low-level error occurred

**See Also:**
- getOption(int)

---

#### Object
getOption​(int optID)
throws
SocketException

Fetch the value of an option.
Binary options will return java.lang.Boolean.TRUE
if enabled, java.lang.Boolean.FALSE if disabled, e.g.:

```java
SocketImpl s;
...
Boolean noDelay = (Boolean)(s.getOption(TCP_NODELAY));
if (noDelay.booleanValue()) {
// true if TCP_NODELAY is enabled...
...
}
```

For options that take a particular type as a parameter,
getOption(int) will return the parameter's value, else
it will return java.lang.Boolean.FALSE:

```java
Object o = s.getOption(SO_LINGER);
if (o instanceof Integer) {
System.out.print("Linger time is " + ((Integer)o).intValue());
} else {
// the true type of o is java.lang.Boolean.FALSE;
}
```

**Parameters:**
- optID

- an

int

identifying the option to fetch

**Returns:**
- the value of the option

**Throws:**
- SocketException

- if the socket is closed
- SocketException

- if

optID

is unknown along the
protocol stack (including the SocketImpl)

**See Also:**
- setOption(int, java.lang.Object)

---

### Additional Sections

#### Interface SocketOptions

**All Known Implementing Classes:** DatagramSocketImpl

,

SocketImpl

```java
public interface
SocketOptions
```

Interface of methods to get/set socket options. This interface is
implemented by:

SocketImpl

and

DatagramSocketImpl

.
Subclasses of these should override the methods
of this interface in order to support their own options.

The methods and constants which specify options in this interface are
for implementation only. If you're not subclassing SocketImpl or
DatagramSocketImpl,

you won't use these directly.

There are
type-safe methods to get/set each of these options in Socket, ServerSocket,
DatagramSocket and MulticastSocket.

**Since:** 1.1

public interface

SocketOptions

Interface of methods to get/set socket options. This interface is
implemented by:

SocketImpl

and

DatagramSocketImpl

.
Subclasses of these should override the methods
of this interface in order to support their own options.

The methods and constants which specify options in this interface are
for implementation only. If you're not subclassing SocketImpl or
DatagramSocketImpl,

you won't use these directly.

There are
type-safe methods to get/set each of these options in Socket, ServerSocket,
DatagramSocket and MulticastSocket.

The methods and constants which specify options in this interface are
for implementation only. If you're not subclassing SocketImpl or
DatagramSocketImpl,

you won't use these directly.

There are
type-safe methods to get/set each of these options in Socket, ServerSocket,
DatagramSocket and MulticastSocket.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

IP_MULTICAST_IF

Set which outgoing interface on which to send multicast packets.

static int

IP_MULTICAST_IF2

Same as above.

static int

IP_MULTICAST_LOOP

This option enables or disables local loopback of multicast datagrams.

static int

IP_TOS

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

static int

SO_BINDADDR

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed).

static int

SO_BROADCAST

Sets SO_BROADCAST for a socket.

static int

SO_KEEPALIVE

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer.

static int

SO_LINGER

Specify a linger-on-close timeout.

static int

SO_OOBINLINE

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.

static int

SO_RCVBUF

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O.

static int

SO_REUSEADDR

Sets SO_REUSEADDR for a socket.

static int

SO_REUSEPORT

Sets SO_REUSEPORT for a socket.

static int

SO_SNDBUF

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O.

static int

SO_TIMEOUT

Set a timeout on blocking Socket operations:

static int

TCP_NODELAY

Disable Nagle's algorithm for this connection.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getOption

​(int optID)

Fetch the value of an option.

void

setOption

​(int optID,

Object

value)

Enable/disable the option specified by

optID

.

Field Summary

Fields

Modifier and Type

Field

Description

static int

IP_MULTICAST_IF

Set which outgoing interface on which to send multicast packets.

static int

IP_MULTICAST_IF2

Same as above.

static int

IP_MULTICAST_LOOP

This option enables or disables local loopback of multicast datagrams.

static int

IP_TOS

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

static int

SO_BINDADDR

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed).

static int

SO_BROADCAST

Sets SO_BROADCAST for a socket.

static int

SO_KEEPALIVE

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer.

static int

SO_LINGER

Specify a linger-on-close timeout.

static int

SO_OOBINLINE

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.

static int

SO_RCVBUF

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O.

static int

SO_REUSEADDR

Sets SO_REUSEADDR for a socket.

static int

SO_REUSEPORT

Sets SO_REUSEPORT for a socket.

static int

SO_SNDBUF

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O.

static int

SO_TIMEOUT

Set a timeout on blocking Socket operations:

static int

TCP_NODELAY

Disable Nagle's algorithm for this connection.

---

#### Field Summary

Set which outgoing interface on which to send multicast packets.

Same as above.

This option enables or disables local loopback of multicast datagrams.

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed).

Sets SO_BROADCAST for a socket.

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer.

Specify a linger-on-close timeout.

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O.

Sets SO_REUSEADDR for a socket.

Sets SO_REUSEPORT for a socket.

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O.

Set a timeout on blocking Socket operations:

Disable Nagle's algorithm for this connection.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getOption

​(int optID)

Fetch the value of an option.

void

setOption

​(int optID,

Object

value)

Enable/disable the option specified by

optID

.

---

#### Method Summary

Fetch the value of an option.

Enable/disable the option specified by

optID

.

============ FIELD DETAIL ===========

- Field Detail

- TCP_NODELAY

```java
@Native

static final int TCP_NODELAY
```

Disable Nagle's algorithm for this connection. Written data
to the network is not buffered pending acknowledgement of
previously written data.

Valid for TCP only: SocketImpl.

**See Also:** Socket.setTcpNoDelay(boolean)

,

Socket.getTcpNoDelay()

,

Constant Field Values

- SO_BINDADDR

```java
@Native

static final int SO_BINDADDR
```

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed). The default local
address of a socket is INADDR_ANY, meaning any local address on a
multi-homed host. A multi-homed host can use this option to accept
connections to only one of its addresses (in the case of a
ServerSocket or DatagramSocket), or to specify its return address
to the peer (for a Socket or DatagramSocket). The parameter of
this option is an InetAddress.

This option

must

be specified in the constructor.

Valid for: SocketImpl, DatagramSocketImpl

**See Also:** Socket.getLocalAddress()

,

DatagramSocket.getLocalAddress()

,

Constant Field Values

- SO_REUSEADDR

```java
@Native

static final int SO_REUSEADDR
```

Sets SO_REUSEADDR for a socket. This is used only for MulticastSockets
in java, and it is set by default for MulticastSockets.

Valid for: DatagramSocketImpl

**See Also:** Constant Field Values

- SO_REUSEPORT

```java
@Native

static final int SO_REUSEPORT
```

Sets SO_REUSEPORT for a socket. This option enables and disables
the ability to have multiple sockets listen to the same address
and port.

Valid for: SocketImpl, DatagramSocketImpl

**Since:** 9
**See Also:** StandardSocketOptions.SO_REUSEPORT

,

Constant Field Values

- SO_BROADCAST

```java
@Native

static final int SO_BROADCAST
```

Sets SO_BROADCAST for a socket. This option enables and disables
the ability of the process to send broadcast messages. It is supported
for only datagram sockets and only on networks that support
the concept of a broadcast message (e.g. Ethernet, token ring, etc.),
and it is set by default for DatagramSockets.

**Since:** 1.4
**See Also:** Constant Field Values

- IP_MULTICAST_IF

```java
@Native

static final int IP_MULTICAST_IF
```

Set which outgoing interface on which to send multicast packets.
Useful on hosts with multiple network interfaces, where applications
want to use other than the system default. Takes/returns an InetAddress.

Valid for Multicast: DatagramSocketImpl

**See Also:** MulticastSocket.setInterface(InetAddress)

,

MulticastSocket.getInterface()

,

Constant Field Values

- IP_MULTICAST_IF2

```java
@Native

static final int IP_MULTICAST_IF2
```

Same as above. This option is introduced so that the behaviour
with IP_MULTICAST_IF will be kept the same as before, while
this new option can support setting outgoing interfaces with either
IPv4 and IPv6 addresses.

NOTE: make sure there is no conflict with this

**Since:** 1.4
**See Also:** MulticastSocket.setNetworkInterface(NetworkInterface)

,

MulticastSocket.getNetworkInterface()

,

Constant Field Values

- IP_MULTICAST_LOOP

```java
@Native

static final int IP_MULTICAST_LOOP
```

This option enables or disables local loopback of multicast datagrams.
This option is enabled by default for Multicast Sockets.

**Since:** 1.4
**See Also:** Constant Field Values

- IP_TOS

```java
@Native

static final int IP_TOS
```

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

**Since:** 1.4
**See Also:** Constant Field Values

- SO_LINGER

```java
@Native

static final int SO_LINGER
```

Specify a linger-on-close timeout. This option disables/enables
immediate return from a

close()

of a TCP Socket. Enabling
this option with a non-zero Integer

timeout

means that a

close()

will block pending the transmission and acknowledgement
of all data written to the peer, at which point the socket is closed

gracefully

. Upon reaching the linger timeout, the socket is
closed

forcefully

, with a TCP RST. Enabling the option with a
timeout of zero does a forceful close immediately. If the specified
timeout value exceeds 65,535 it will be reduced to 65,535.

Valid only for TCP: SocketImpl

**See Also:** Socket.setSoLinger(boolean, int)

,

Socket.getSoLinger()

,

Constant Field Values

- SO_TIMEOUT

```java
@Native

static final int SO_TIMEOUT
```

Set a timeout on blocking Socket operations:

```java
ServerSocket.accept();
SocketInputStream.read();
DatagramSocket.receive();
```

The option must be set prior to entering a blocking
operation to take effect. If the timeout expires and the
operation would continue to block,

java.io.InterruptedIOException

is raised. The Socket is
not closed in this case.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setSoTimeout(int)

,

ServerSocket.setSoTimeout(int)

,

DatagramSocket.setSoTimeout(int)

,

Constant Field Values

- SO_SNDBUF

```java
@Native

static final int SO_SNDBUF
```

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be sent over the socket. When
used in get, this must return the size of the buffer actually
used by the platform when sending out data on this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setSendBufferSize(int)

,

Socket.getSendBufferSize()

,

DatagramSocket.setSendBufferSize(int)

,

DatagramSocket.getSendBufferSize()

,

Constant Field Values

- SO_RCVBUF

```java
@Native

static final int SO_RCVBUF
```

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be received over the
socket. When used in get, this must return the size of the
buffer actually used by the platform when receiving in data on
this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setReceiveBufferSize(int)

,

Socket.getReceiveBufferSize()

,

DatagramSocket.setReceiveBufferSize(int)

,

DatagramSocket.getReceiveBufferSize()

,

Constant Field Values

- SO_KEEPALIVE

```java
@Native

static final int SO_KEEPALIVE
```

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer. This probe is a
TCP segment to which the peer must respond.
One of three responses is expected:
1. The peer responds with the expected ACK. The application is not
notified (since everything is OK). TCP will send another probe
following another 2 hours of inactivity.
2. The peer responds with an RST, which tells the local TCP that
the peer host has crashed and rebooted. The socket is closed.
3. There is no response from the peer. The socket is closed.

The purpose of this option is to detect if the peer host crashes.

Valid only for TCP socket: SocketImpl

**See Also:** Socket.setKeepAlive(boolean)

,

Socket.getKeepAlive()

,

Constant Field Values

- SO_OOBINLINE

```java
@Native

static final int SO_OOBINLINE
```

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.
When the option is disabled (which is the default) urgent data
is silently discarded.

**See Also:** Socket.setOOBInline(boolean)

,

Socket.getOOBInline()

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- setOption

```java
void setOption​(int optID,

Object
value)
throws
SocketException
```

Enable/disable the option specified by

optID

. If the option
is to be enabled, and it takes an option-specific "value", this is
passed in

value

. The actual type of value is option-specific,
and it is an error to pass something that isn't of the expected type:

```java
SocketImpl s;
...
s.setOption(SO_LINGER, new Integer(10));
// OK - set SO_LINGER w/ timeout of 10 sec.
s.setOption(SO_LINGER, new Double(10));
// ERROR - expects java.lang.Integer
```

If the requested option is binary, it can be set using this method by
a java.lang.Boolean:

```java
s.setOption(TCP_NODELAY, Boolean.TRUE);
// OK - enables TCP_NODELAY, a binary option
```

Any option can be disabled using this method with a Boolean.FALSE:

```java
s.setOption(TCP_NODELAY, Boolean.FALSE);
// OK - disables TCP_NODELAY
s.setOption(SO_LINGER, Boolean.FALSE);
// OK - disables SO_LINGER
```

For an option that has a notion of on and off, and requires
a non-boolean parameter, setting its value to anything other than

Boolean.FALSE

implicitly enables it.

Throws SocketException if the option is unrecognized,
the socket is closed, or some low-level error occurred

**Parameters:** optID

- identifies the option
**Parameters:** value

- the parameter of the socket option
**Throws:** SocketException

- if the option is unrecognized,
the socket is closed, or some low-level error occurred
**See Also:** getOption(int)

- getOption

```java
Object
getOption​(int optID)
throws
SocketException
```

Fetch the value of an option.
Binary options will return java.lang.Boolean.TRUE
if enabled, java.lang.Boolean.FALSE if disabled, e.g.:

```java
SocketImpl s;
...
Boolean noDelay = (Boolean)(s.getOption(TCP_NODELAY));
if (noDelay.booleanValue()) {
// true if TCP_NODELAY is enabled...
...
}
```

For options that take a particular type as a parameter,
getOption(int) will return the parameter's value, else
it will return java.lang.Boolean.FALSE:

```java
Object o = s.getOption(SO_LINGER);
if (o instanceof Integer) {
System.out.print("Linger time is " + ((Integer)o).intValue());
} else {
// the true type of o is java.lang.Boolean.FALSE;
}
```

**Parameters:** optID

- an

int

identifying the option to fetch
**Returns:** the value of the option
**Throws:** SocketException

- if the socket is closed
**Throws:** SocketException

- if

optID

is unknown along the
protocol stack (including the SocketImpl)
**See Also:** setOption(int, java.lang.Object)

Field Detail

- TCP_NODELAY

```java
@Native

static final int TCP_NODELAY
```

Disable Nagle's algorithm for this connection. Written data
to the network is not buffered pending acknowledgement of
previously written data.

Valid for TCP only: SocketImpl.

**See Also:** Socket.setTcpNoDelay(boolean)

,

Socket.getTcpNoDelay()

,

Constant Field Values

- SO_BINDADDR

```java
@Native

static final int SO_BINDADDR
```

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed). The default local
address of a socket is INADDR_ANY, meaning any local address on a
multi-homed host. A multi-homed host can use this option to accept
connections to only one of its addresses (in the case of a
ServerSocket or DatagramSocket), or to specify its return address
to the peer (for a Socket or DatagramSocket). The parameter of
this option is an InetAddress.

This option

must

be specified in the constructor.

Valid for: SocketImpl, DatagramSocketImpl

**See Also:** Socket.getLocalAddress()

,

DatagramSocket.getLocalAddress()

,

Constant Field Values

- SO_REUSEADDR

```java
@Native

static final int SO_REUSEADDR
```

Sets SO_REUSEADDR for a socket. This is used only for MulticastSockets
in java, and it is set by default for MulticastSockets.

Valid for: DatagramSocketImpl

**See Also:** Constant Field Values

- SO_REUSEPORT

```java
@Native

static final int SO_REUSEPORT
```

Sets SO_REUSEPORT for a socket. This option enables and disables
the ability to have multiple sockets listen to the same address
and port.

Valid for: SocketImpl, DatagramSocketImpl

**Since:** 9
**See Also:** StandardSocketOptions.SO_REUSEPORT

,

Constant Field Values

- SO_BROADCAST

```java
@Native

static final int SO_BROADCAST
```

Sets SO_BROADCAST for a socket. This option enables and disables
the ability of the process to send broadcast messages. It is supported
for only datagram sockets and only on networks that support
the concept of a broadcast message (e.g. Ethernet, token ring, etc.),
and it is set by default for DatagramSockets.

**Since:** 1.4
**See Also:** Constant Field Values

- IP_MULTICAST_IF

```java
@Native

static final int IP_MULTICAST_IF
```

Set which outgoing interface on which to send multicast packets.
Useful on hosts with multiple network interfaces, where applications
want to use other than the system default. Takes/returns an InetAddress.

Valid for Multicast: DatagramSocketImpl

**See Also:** MulticastSocket.setInterface(InetAddress)

,

MulticastSocket.getInterface()

,

Constant Field Values

- IP_MULTICAST_IF2

```java
@Native

static final int IP_MULTICAST_IF2
```

Same as above. This option is introduced so that the behaviour
with IP_MULTICAST_IF will be kept the same as before, while
this new option can support setting outgoing interfaces with either
IPv4 and IPv6 addresses.

NOTE: make sure there is no conflict with this

**Since:** 1.4
**See Also:** MulticastSocket.setNetworkInterface(NetworkInterface)

,

MulticastSocket.getNetworkInterface()

,

Constant Field Values

- IP_MULTICAST_LOOP

```java
@Native

static final int IP_MULTICAST_LOOP
```

This option enables or disables local loopback of multicast datagrams.
This option is enabled by default for Multicast Sockets.

**Since:** 1.4
**See Also:** Constant Field Values

- IP_TOS

```java
@Native

static final int IP_TOS
```

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

**Since:** 1.4
**See Also:** Constant Field Values

- SO_LINGER

```java
@Native

static final int SO_LINGER
```

Specify a linger-on-close timeout. This option disables/enables
immediate return from a

close()

of a TCP Socket. Enabling
this option with a non-zero Integer

timeout

means that a

close()

will block pending the transmission and acknowledgement
of all data written to the peer, at which point the socket is closed

gracefully

. Upon reaching the linger timeout, the socket is
closed

forcefully

, with a TCP RST. Enabling the option with a
timeout of zero does a forceful close immediately. If the specified
timeout value exceeds 65,535 it will be reduced to 65,535.

Valid only for TCP: SocketImpl

**See Also:** Socket.setSoLinger(boolean, int)

,

Socket.getSoLinger()

,

Constant Field Values

- SO_TIMEOUT

```java
@Native

static final int SO_TIMEOUT
```

Set a timeout on blocking Socket operations:

```java
ServerSocket.accept();
SocketInputStream.read();
DatagramSocket.receive();
```

The option must be set prior to entering a blocking
operation to take effect. If the timeout expires and the
operation would continue to block,

java.io.InterruptedIOException

is raised. The Socket is
not closed in this case.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setSoTimeout(int)

,

ServerSocket.setSoTimeout(int)

,

DatagramSocket.setSoTimeout(int)

,

Constant Field Values

- SO_SNDBUF

```java
@Native

static final int SO_SNDBUF
```

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be sent over the socket. When
used in get, this must return the size of the buffer actually
used by the platform when sending out data on this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setSendBufferSize(int)

,

Socket.getSendBufferSize()

,

DatagramSocket.setSendBufferSize(int)

,

DatagramSocket.getSendBufferSize()

,

Constant Field Values

- SO_RCVBUF

```java
@Native

static final int SO_RCVBUF
```

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be received over the
socket. When used in get, this must return the size of the
buffer actually used by the platform when receiving in data on
this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setReceiveBufferSize(int)

,

Socket.getReceiveBufferSize()

,

DatagramSocket.setReceiveBufferSize(int)

,

DatagramSocket.getReceiveBufferSize()

,

Constant Field Values

- SO_KEEPALIVE

```java
@Native

static final int SO_KEEPALIVE
```

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer. This probe is a
TCP segment to which the peer must respond.
One of three responses is expected:
1. The peer responds with the expected ACK. The application is not
notified (since everything is OK). TCP will send another probe
following another 2 hours of inactivity.
2. The peer responds with an RST, which tells the local TCP that
the peer host has crashed and rebooted. The socket is closed.
3. There is no response from the peer. The socket is closed.

The purpose of this option is to detect if the peer host crashes.

Valid only for TCP socket: SocketImpl

**See Also:** Socket.setKeepAlive(boolean)

,

Socket.getKeepAlive()

,

Constant Field Values

- SO_OOBINLINE

```java
@Native

static final int SO_OOBINLINE
```

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.
When the option is disabled (which is the default) urgent data
is silently discarded.

**See Also:** Socket.setOOBInline(boolean)

,

Socket.getOOBInline()

,

Constant Field Values

---

#### Field Detail

TCP_NODELAY

```java
@Native

static final int TCP_NODELAY
```

Disable Nagle's algorithm for this connection. Written data
to the network is not buffered pending acknowledgement of
previously written data.

Valid for TCP only: SocketImpl.

**See Also:** Socket.setTcpNoDelay(boolean)

,

Socket.getTcpNoDelay()

,

Constant Field Values

---

#### TCP_NODELAY

@Native

static final int TCP_NODELAY

Disable Nagle's algorithm for this connection. Written data
to the network is not buffered pending acknowledgement of
previously written data.

Valid for TCP only: SocketImpl.

Valid for TCP only: SocketImpl.

SO_BINDADDR

```java
@Native

static final int SO_BINDADDR
```

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed). The default local
address of a socket is INADDR_ANY, meaning any local address on a
multi-homed host. A multi-homed host can use this option to accept
connections to only one of its addresses (in the case of a
ServerSocket or DatagramSocket), or to specify its return address
to the peer (for a Socket or DatagramSocket). The parameter of
this option is an InetAddress.

This option

must

be specified in the constructor.

Valid for: SocketImpl, DatagramSocketImpl

**See Also:** Socket.getLocalAddress()

,

DatagramSocket.getLocalAddress()

,

Constant Field Values

---

#### SO_BINDADDR

@Native

static final int SO_BINDADDR

Fetch the local address binding of a socket (this option cannot
be "set" only "gotten", since sockets are bound at creation time,
and so the locally bound address cannot be changed). The default local
address of a socket is INADDR_ANY, meaning any local address on a
multi-homed host. A multi-homed host can use this option to accept
connections to only one of its addresses (in the case of a
ServerSocket or DatagramSocket), or to specify its return address
to the peer (for a Socket or DatagramSocket). The parameter of
this option is an InetAddress.

This option

must

be specified in the constructor.

Valid for: SocketImpl, DatagramSocketImpl

This option

must

be specified in the constructor.

Valid for: SocketImpl, DatagramSocketImpl

Valid for: SocketImpl, DatagramSocketImpl

SO_REUSEADDR

```java
@Native

static final int SO_REUSEADDR
```

Sets SO_REUSEADDR for a socket. This is used only for MulticastSockets
in java, and it is set by default for MulticastSockets.

Valid for: DatagramSocketImpl

**See Also:** Constant Field Values

---

#### SO_REUSEADDR

@Native

static final int SO_REUSEADDR

Sets SO_REUSEADDR for a socket. This is used only for MulticastSockets
in java, and it is set by default for MulticastSockets.

Valid for: DatagramSocketImpl

Valid for: DatagramSocketImpl

SO_REUSEPORT

```java
@Native

static final int SO_REUSEPORT
```

Sets SO_REUSEPORT for a socket. This option enables and disables
the ability to have multiple sockets listen to the same address
and port.

Valid for: SocketImpl, DatagramSocketImpl

**Since:** 9
**See Also:** StandardSocketOptions.SO_REUSEPORT

,

Constant Field Values

---

#### SO_REUSEPORT

@Native

static final int SO_REUSEPORT

Sets SO_REUSEPORT for a socket. This option enables and disables
the ability to have multiple sockets listen to the same address
and port.

Valid for: SocketImpl, DatagramSocketImpl

Valid for: SocketImpl, DatagramSocketImpl

SO_BROADCAST

```java
@Native

static final int SO_BROADCAST
```

Sets SO_BROADCAST for a socket. This option enables and disables
the ability of the process to send broadcast messages. It is supported
for only datagram sockets and only on networks that support
the concept of a broadcast message (e.g. Ethernet, token ring, etc.),
and it is set by default for DatagramSockets.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### SO_BROADCAST

@Native

static final int SO_BROADCAST

Sets SO_BROADCAST for a socket. This option enables and disables
the ability of the process to send broadcast messages. It is supported
for only datagram sockets and only on networks that support
the concept of a broadcast message (e.g. Ethernet, token ring, etc.),
and it is set by default for DatagramSockets.

IP_MULTICAST_IF

```java
@Native

static final int IP_MULTICAST_IF
```

Set which outgoing interface on which to send multicast packets.
Useful on hosts with multiple network interfaces, where applications
want to use other than the system default. Takes/returns an InetAddress.

Valid for Multicast: DatagramSocketImpl

**See Also:** MulticastSocket.setInterface(InetAddress)

,

MulticastSocket.getInterface()

,

Constant Field Values

---

#### IP_MULTICAST_IF

@Native

static final int IP_MULTICAST_IF

Set which outgoing interface on which to send multicast packets.
Useful on hosts with multiple network interfaces, where applications
want to use other than the system default. Takes/returns an InetAddress.

Valid for Multicast: DatagramSocketImpl

Valid for Multicast: DatagramSocketImpl

IP_MULTICAST_IF2

```java
@Native

static final int IP_MULTICAST_IF2
```

Same as above. This option is introduced so that the behaviour
with IP_MULTICAST_IF will be kept the same as before, while
this new option can support setting outgoing interfaces with either
IPv4 and IPv6 addresses.

NOTE: make sure there is no conflict with this

**Since:** 1.4
**See Also:** MulticastSocket.setNetworkInterface(NetworkInterface)

,

MulticastSocket.getNetworkInterface()

,

Constant Field Values

---

#### IP_MULTICAST_IF2

@Native

static final int IP_MULTICAST_IF2

Same as above. This option is introduced so that the behaviour
with IP_MULTICAST_IF will be kept the same as before, while
this new option can support setting outgoing interfaces with either
IPv4 and IPv6 addresses.

NOTE: make sure there is no conflict with this

IP_MULTICAST_LOOP

```java
@Native

static final int IP_MULTICAST_LOOP
```

This option enables or disables local loopback of multicast datagrams.
This option is enabled by default for Multicast Sockets.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### IP_MULTICAST_LOOP

@Native

static final int IP_MULTICAST_LOOP

This option enables or disables local loopback of multicast datagrams.
This option is enabled by default for Multicast Sockets.

IP_TOS

```java
@Native

static final int IP_TOS
```

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### IP_TOS

@Native

static final int IP_TOS

This option sets the type-of-service or traffic class field
in the IP header for a TCP or UDP socket.

SO_LINGER

```java
@Native

static final int SO_LINGER
```

Specify a linger-on-close timeout. This option disables/enables
immediate return from a

close()

of a TCP Socket. Enabling
this option with a non-zero Integer

timeout

means that a

close()

will block pending the transmission and acknowledgement
of all data written to the peer, at which point the socket is closed

gracefully

. Upon reaching the linger timeout, the socket is
closed

forcefully

, with a TCP RST. Enabling the option with a
timeout of zero does a forceful close immediately. If the specified
timeout value exceeds 65,535 it will be reduced to 65,535.

Valid only for TCP: SocketImpl

**See Also:** Socket.setSoLinger(boolean, int)

,

Socket.getSoLinger()

,

Constant Field Values

---

#### SO_LINGER

@Native

static final int SO_LINGER

Specify a linger-on-close timeout. This option disables/enables
immediate return from a

close()

of a TCP Socket. Enabling
this option with a non-zero Integer

timeout

means that a

close()

will block pending the transmission and acknowledgement
of all data written to the peer, at which point the socket is closed

gracefully

. Upon reaching the linger timeout, the socket is
closed

forcefully

, with a TCP RST. Enabling the option with a
timeout of zero does a forceful close immediately. If the specified
timeout value exceeds 65,535 it will be reduced to 65,535.

Valid only for TCP: SocketImpl

Valid only for TCP: SocketImpl

SO_TIMEOUT

```java
@Native

static final int SO_TIMEOUT
```

Set a timeout on blocking Socket operations:

```java
ServerSocket.accept();
SocketInputStream.read();
DatagramSocket.receive();
```

The option must be set prior to entering a blocking
operation to take effect. If the timeout expires and the
operation would continue to block,

java.io.InterruptedIOException

is raised. The Socket is
not closed in this case.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setSoTimeout(int)

,

ServerSocket.setSoTimeout(int)

,

DatagramSocket.setSoTimeout(int)

,

Constant Field Values

---

#### SO_TIMEOUT

@Native

static final int SO_TIMEOUT

Set a timeout on blocking Socket operations:

```java
ServerSocket.accept();
SocketInputStream.read();
DatagramSocket.receive();
```

The option must be set prior to entering a blocking
operation to take effect. If the timeout expires and the
operation would continue to block,

java.io.InterruptedIOException

is raised. The Socket is
not closed in this case.

Valid for all sockets: SocketImpl, DatagramSocketImpl

ServerSocket.accept();
SocketInputStream.read();
DatagramSocket.receive();

The option must be set prior to entering a blocking
operation to take effect. If the timeout expires and the
operation would continue to block,

java.io.InterruptedIOException

is raised. The Socket is
not closed in this case.

Valid for all sockets: SocketImpl, DatagramSocketImpl

Valid for all sockets: SocketImpl, DatagramSocketImpl

SO_SNDBUF

```java
@Native

static final int SO_SNDBUF
```

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be sent over the socket. When
used in get, this must return the size of the buffer actually
used by the platform when sending out data on this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setSendBufferSize(int)

,

Socket.getSendBufferSize()

,

DatagramSocket.setSendBufferSize(int)

,

DatagramSocket.getSendBufferSize()

,

Constant Field Values

---

#### SO_SNDBUF

@Native

static final int SO_SNDBUF

Set a hint the size of the underlying buffers used by the
platform for outgoing network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be sent over the socket. When
used in get, this must return the size of the buffer actually
used by the platform when sending out data on this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

SO_RCVBUF

```java
@Native

static final int SO_RCVBUF
```

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be received over the
socket. When used in get, this must return the size of the
buffer actually used by the platform when receiving in data on
this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

**See Also:** Socket.setReceiveBufferSize(int)

,

Socket.getReceiveBufferSize()

,

DatagramSocket.setReceiveBufferSize(int)

,

DatagramSocket.getReceiveBufferSize()

,

Constant Field Values

---

#### SO_RCVBUF

@Native

static final int SO_RCVBUF

Set a hint the size of the underlying buffers used by the
platform for incoming network I/O. When used in set, this is a
suggestion to the kernel from the application about the size of
buffers to use for the data to be received over the
socket. When used in get, this must return the size of the
buffer actually used by the platform when receiving in data on
this socket.

Valid for all sockets: SocketImpl, DatagramSocketImpl

SO_KEEPALIVE

```java
@Native

static final int SO_KEEPALIVE
```

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer. This probe is a
TCP segment to which the peer must respond.
One of three responses is expected:
1. The peer responds with the expected ACK. The application is not
notified (since everything is OK). TCP will send another probe
following another 2 hours of inactivity.
2. The peer responds with an RST, which tells the local TCP that
the peer host has crashed and rebooted. The socket is closed.
3. There is no response from the peer. The socket is closed.

The purpose of this option is to detect if the peer host crashes.

Valid only for TCP socket: SocketImpl

**See Also:** Socket.setKeepAlive(boolean)

,

Socket.getKeepAlive()

,

Constant Field Values

---

#### SO_KEEPALIVE

@Native

static final int SO_KEEPALIVE

When the keepalive option is set for a TCP socket and no data
has been exchanged across the socket in either direction for
2 hours (NOTE: the actual value is implementation dependent),
TCP automatically sends a keepalive probe to the peer. This probe is a
TCP segment to which the peer must respond.
One of three responses is expected:
1. The peer responds with the expected ACK. The application is not
notified (since everything is OK). TCP will send another probe
following another 2 hours of inactivity.
2. The peer responds with an RST, which tells the local TCP that
the peer host has crashed and rebooted. The socket is closed.
3. There is no response from the peer. The socket is closed.

The purpose of this option is to detect if the peer host crashes.

Valid only for TCP socket: SocketImpl

SO_OOBINLINE

```java
@Native

static final int SO_OOBINLINE
```

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.
When the option is disabled (which is the default) urgent data
is silently discarded.

**See Also:** Socket.setOOBInline(boolean)

,

Socket.getOOBInline()

,

Constant Field Values

---

#### SO_OOBINLINE

@Native

static final int SO_OOBINLINE

When the OOBINLINE option is set, any TCP urgent data received on
the socket will be received through the socket input stream.
When the option is disabled (which is the default) urgent data
is silently discarded.

Method Detail

- setOption

```java
void setOption​(int optID,

Object
value)
throws
SocketException
```

Enable/disable the option specified by

optID

. If the option
is to be enabled, and it takes an option-specific "value", this is
passed in

value

. The actual type of value is option-specific,
and it is an error to pass something that isn't of the expected type:

```java
SocketImpl s;
...
s.setOption(SO_LINGER, new Integer(10));
// OK - set SO_LINGER w/ timeout of 10 sec.
s.setOption(SO_LINGER, new Double(10));
// ERROR - expects java.lang.Integer
```

If the requested option is binary, it can be set using this method by
a java.lang.Boolean:

```java
s.setOption(TCP_NODELAY, Boolean.TRUE);
// OK - enables TCP_NODELAY, a binary option
```

Any option can be disabled using this method with a Boolean.FALSE:

```java
s.setOption(TCP_NODELAY, Boolean.FALSE);
// OK - disables TCP_NODELAY
s.setOption(SO_LINGER, Boolean.FALSE);
// OK - disables SO_LINGER
```

For an option that has a notion of on and off, and requires
a non-boolean parameter, setting its value to anything other than

Boolean.FALSE

implicitly enables it.

Throws SocketException if the option is unrecognized,
the socket is closed, or some low-level error occurred

**Parameters:** optID

- identifies the option
**Parameters:** value

- the parameter of the socket option
**Throws:** SocketException

- if the option is unrecognized,
the socket is closed, or some low-level error occurred
**See Also:** getOption(int)

- getOption

```java
Object
getOption​(int optID)
throws
SocketException
```

Fetch the value of an option.
Binary options will return java.lang.Boolean.TRUE
if enabled, java.lang.Boolean.FALSE if disabled, e.g.:

```java
SocketImpl s;
...
Boolean noDelay = (Boolean)(s.getOption(TCP_NODELAY));
if (noDelay.booleanValue()) {
// true if TCP_NODELAY is enabled...
...
}
```

For options that take a particular type as a parameter,
getOption(int) will return the parameter's value, else
it will return java.lang.Boolean.FALSE:

```java
Object o = s.getOption(SO_LINGER);
if (o instanceof Integer) {
System.out.print("Linger time is " + ((Integer)o).intValue());
} else {
// the true type of o is java.lang.Boolean.FALSE;
}
```

**Parameters:** optID

- an

int

identifying the option to fetch
**Returns:** the value of the option
**Throws:** SocketException

- if the socket is closed
**Throws:** SocketException

- if

optID

is unknown along the
protocol stack (including the SocketImpl)
**See Also:** setOption(int, java.lang.Object)

---

#### Method Detail

setOption

```java
void setOption​(int optID,

Object
value)
throws
SocketException
```

Enable/disable the option specified by

optID

. If the option
is to be enabled, and it takes an option-specific "value", this is
passed in

value

. The actual type of value is option-specific,
and it is an error to pass something that isn't of the expected type:

```java
SocketImpl s;
...
s.setOption(SO_LINGER, new Integer(10));
// OK - set SO_LINGER w/ timeout of 10 sec.
s.setOption(SO_LINGER, new Double(10));
// ERROR - expects java.lang.Integer
```

If the requested option is binary, it can be set using this method by
a java.lang.Boolean:

```java
s.setOption(TCP_NODELAY, Boolean.TRUE);
// OK - enables TCP_NODELAY, a binary option
```

Any option can be disabled using this method with a Boolean.FALSE:

```java
s.setOption(TCP_NODELAY, Boolean.FALSE);
// OK - disables TCP_NODELAY
s.setOption(SO_LINGER, Boolean.FALSE);
// OK - disables SO_LINGER
```

For an option that has a notion of on and off, and requires
a non-boolean parameter, setting its value to anything other than

Boolean.FALSE

implicitly enables it.

Throws SocketException if the option is unrecognized,
the socket is closed, or some low-level error occurred

**Parameters:** optID

- identifies the option
**Parameters:** value

- the parameter of the socket option
**Throws:** SocketException

- if the option is unrecognized,
the socket is closed, or some low-level error occurred
**See Also:** getOption(int)

---

#### setOption

void setOption​(int optID,

Object

value)
throws

SocketException

Enable/disable the option specified by

optID

. If the option
is to be enabled, and it takes an option-specific "value", this is
passed in

value

. The actual type of value is option-specific,
and it is an error to pass something that isn't of the expected type:

```java
SocketImpl s;
...
s.setOption(SO_LINGER, new Integer(10));
// OK - set SO_LINGER w/ timeout of 10 sec.
s.setOption(SO_LINGER, new Double(10));
// ERROR - expects java.lang.Integer
```

If the requested option is binary, it can be set using this method by
a java.lang.Boolean:

```java
s.setOption(TCP_NODELAY, Boolean.TRUE);
// OK - enables TCP_NODELAY, a binary option
```

Any option can be disabled using this method with a Boolean.FALSE:

```java
s.setOption(TCP_NODELAY, Boolean.FALSE);
// OK - disables TCP_NODELAY
s.setOption(SO_LINGER, Boolean.FALSE);
// OK - disables SO_LINGER
```

For an option that has a notion of on and off, and requires
a non-boolean parameter, setting its value to anything other than

Boolean.FALSE

implicitly enables it.

Throws SocketException if the option is unrecognized,
the socket is closed, or some low-level error occurred

SocketImpl s;
...
s.setOption(SO_LINGER, new Integer(10));
// OK - set SO_LINGER w/ timeout of 10 sec.
s.setOption(SO_LINGER, new Double(10));
// ERROR - expects java.lang.Integer

s.setOption(TCP_NODELAY, Boolean.TRUE);
// OK - enables TCP_NODELAY, a binary option

s.setOption(TCP_NODELAY, Boolean.FALSE);
// OK - disables TCP_NODELAY
s.setOption(SO_LINGER, Boolean.FALSE);
// OK - disables SO_LINGER

getOption

```java
Object
getOption​(int optID)
throws
SocketException
```

Fetch the value of an option.
Binary options will return java.lang.Boolean.TRUE
if enabled, java.lang.Boolean.FALSE if disabled, e.g.:

```java
SocketImpl s;
...
Boolean noDelay = (Boolean)(s.getOption(TCP_NODELAY));
if (noDelay.booleanValue()) {
// true if TCP_NODELAY is enabled...
...
}
```

For options that take a particular type as a parameter,
getOption(int) will return the parameter's value, else
it will return java.lang.Boolean.FALSE:

```java
Object o = s.getOption(SO_LINGER);
if (o instanceof Integer) {
System.out.print("Linger time is " + ((Integer)o).intValue());
} else {
// the true type of o is java.lang.Boolean.FALSE;
}
```

**Parameters:** optID

- an

int

identifying the option to fetch
**Returns:** the value of the option
**Throws:** SocketException

- if the socket is closed
**Throws:** SocketException

- if

optID

is unknown along the
protocol stack (including the SocketImpl)
**See Also:** setOption(int, java.lang.Object)

---

#### getOption

Object

getOption​(int optID)
throws

SocketException

Fetch the value of an option.
Binary options will return java.lang.Boolean.TRUE
if enabled, java.lang.Boolean.FALSE if disabled, e.g.:

```java
SocketImpl s;
...
Boolean noDelay = (Boolean)(s.getOption(TCP_NODELAY));
if (noDelay.booleanValue()) {
// true if TCP_NODELAY is enabled...
...
}
```

For options that take a particular type as a parameter,
getOption(int) will return the parameter's value, else
it will return java.lang.Boolean.FALSE:

```java
Object o = s.getOption(SO_LINGER);
if (o instanceof Integer) {
System.out.print("Linger time is " + ((Integer)o).intValue());
} else {
// the true type of o is java.lang.Boolean.FALSE;
}
```

SocketImpl s;
...
Boolean noDelay = (Boolean)(s.getOption(TCP_NODELAY));
if (noDelay.booleanValue()) {
// true if TCP_NODELAY is enabled...
...
}

For options that take a particular type as a parameter,
getOption(int) will return the parameter's value, else
it will return java.lang.Boolean.FALSE:

```java
Object o = s.getOption(SO_LINGER);
if (o instanceof Integer) {
System.out.print("Linger time is " + ((Integer)o).intValue());
} else {
// the true type of o is java.lang.Boolean.FALSE;
}
```

Object o = s.getOption(SO_LINGER);
if (o instanceof Integer) {
System.out.print("Linger time is " + ((Integer)o).intValue());
} else {
// the true type of o is java.lang.Boolean.FALSE;
}

---

