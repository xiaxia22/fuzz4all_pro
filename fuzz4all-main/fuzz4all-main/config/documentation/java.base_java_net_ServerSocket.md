# Class ServerSocket

**Source:** `java.base\java\net\ServerSocket.html`

### Class Description

```java
public class
ServerSocket

extends
Object

implements
Closeable
```

This class implements server sockets. A server socket waits for
requests to come in over the network. It performs some operation
based on that request, and then possibly returns a result to the requester.

The actual work of the server socket is performed by an instance
of the

SocketImpl

class. An application can
change the socket factory that creates the socket
implementation to configure itself to create sockets
appropriate to the local firewall.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ServerSocket()
throws
IOException

Creates an unbound server socket.

**Throws:**
- IOException

- IO error when opening the socket.

---

#### public ServerSocket​(int port)
throws
IOException

Creates a server socket, bound to the specified port. A port number
of

0

means that the port number is automatically
allocated, typically from an ephemeral port range. This port
number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to

50

. If a connection
indication arrives when the queue is full, the connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:**
- port

- the port number, or

0

to use a port
number that is automatically allocated.

**Throws:**
- IOException

- if an I/O error occurs when opening the socket.
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.

**See Also:**
- SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

---

#### public ServerSocket​(int port,
int backlog)
throws
IOException

Creates a server socket and binds it to the specified local port
number, with the specified backlog.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to the

backlog

parameter. If
a connection indication arrives when the queue is full, the
connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:**
- port

- the port number, or

0

to use a port
number that is automatically allocated.
- backlog

- requested maximum length of the queue of incoming
connections.

**Throws:**
- IOException

- if an I/O error occurs when opening the socket.
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.

**See Also:**
- SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

---

#### public ServerSocket​(int port,
int backlog,

InetAddress
bindAddr)
throws
IOException

Create a server with the specified port, listen backlog, and
local IP address to bind to. The

bindAddr

argument
can be used on a multi-homed host for a ServerSocket that
will only accept connect requests to one of its addresses.
If

bindAddr

is null, it will default accepting
connections on any/all local addresses.
The port must be between 0 and 65535, inclusive.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

If there is a security manager, this method
calls its

checkListen

method
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:**
- port

- the port number, or

0

to use a port
number that is automatically allocated.
- backlog

- requested maximum length of the queue of incoming
connections.
- bindAddr

- the local InetAddress the server will bind to

**Throws:**
- SecurityException

- if a security manager exists and
its

checkListen

method doesn't allow the operation.
- IOException

- if an I/O error occurs when opening the socket.
- IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.

**See Also:**
- SocketOptions

,

SocketImpl

,

SecurityManager.checkListen(int)

**Since:**
- 1.1

---

### Method Details

#### public void bind​(
SocketAddress
endpoint)
throws
IOException

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:**
- endpoint

- The IP address and port number to bind to.

**Throws:**
- IOException

- if the bind operation fails, or if the socket
is already bound.
- SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket

**Since:**
- 1.4

---

#### public void bind​(
SocketAddress
endpoint,
int backlog)
throws
IOException

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:**
- endpoint

- The IP address and port number to bind to.
- backlog

- requested maximum length of the queue of
incoming connections.

**Throws:**
- IOException

- if the bind operation fails, or if the socket
is already bound.
- SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket

**Since:**
- 1.4

---

#### public
InetAddress
getInetAddress()

Returns the local address of this server socket.

If the socket was bound prior to being

closed

,
then this method will continue to return the local address
after the socket is closed.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
the

loopback

address is returned.

**Returns:**
- the address to which this socket is bound,
or the loopback address if denied by the security manager,
or

null

if the socket is unbound.

**See Also:**
- SecurityManager.checkConnect(java.lang.String, int)

---

#### public int getLocalPort()

Returns the port number on which this socket is listening.

If the socket was bound prior to being

closed

,
then this method will continue to return the port number
after the socket is closed.

**Returns:**
- the port number to which this socket is listening or
-1 if the socket is not bound yet.

---

#### public
SocketAddress
getLocalSocketAddress()

Returns the address of the endpoint this socket is bound to.

If the socket was bound prior to being

closed

,
then this method will continue to return the address of the endpoint
after the socket is closed.

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

address and the local
port to which the socket is bound is returned.

**Returns:**
- a

SocketAddress

representing the local endpoint of
this socket, or a

SocketAddress

representing the
loopback address if denied by the security manager,
or

null

if the socket is not bound yet.

**See Also:**
- getInetAddress()

,

getLocalPort()

,

bind(SocketAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

**Since:**
- 1.4

---

#### public
Socket
accept()
throws
IOException

Listens for a connection to be made to this socket and accepts
it. The method blocks until a connection is made.

A new Socket

s

is created and, if there
is a security manager,
the security manager's

checkAccept

method is called
with

s.getInetAddress().getHostAddress()

and

s.getPort()

as its arguments to ensure the operation is allowed.
This could result in a SecurityException.

**Returns:**
- the new Socket

**Throws:**
- IOException

- if an I/O error occurs when waiting for a
connection.
- SecurityException

- if a security manager exists and its

checkAccept

method doesn't allow the operation.
- SocketTimeoutException

- if a timeout was previously set with setSoTimeout and
the timeout has been reached.
- IllegalBlockingModeException

- if this socket has an associated channel, the channel is in
non-blocking mode, and there is no connection ready to be
accepted

**See Also:**
- SecurityManager.checkAccept(java.lang.String, int)

---

#### protected final void implAccept​(
Socket
s)
throws
IOException

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket. So a FooServerSocket
will typically hand this method an

empty

FooSocket. On
return from implAccept the FooSocket will be connected to a client.

**Parameters:**
- s

- the Socket

**Throws:**
- IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode
- IOException

- if an I/O error occurs when waiting
for a connection.

**Since:**
- 1.1

---

#### public void close()
throws
IOException

Closes this socket.

Any thread currently blocked in

accept()

will throw
a

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

**Throws:**
- IOException

- if an I/O error occurs when closing the socket.

---

#### public
ServerSocketChannel
getChannel()

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

A server socket will have a channel if, and only if, the channel
itself was created via the

ServerSocketChannel.open

method.

**Returns:**
- the server-socket channel associated with this socket,
or

null

if this socket was not created
for a channel

**Since:**
- 1.4

---

#### public boolean isBound()

Returns the binding state of the ServerSocket.

**Returns:**
- true if the ServerSocket successfully bound to an address

**Since:**
- 1.4

---

#### public boolean isClosed()

Returns the closed state of the ServerSocket.

**Returns:**
- true if the socket has been closed

**Since:**
- 1.4

---

#### public void setSoTimeout​(int timeout)
throws
SocketException

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds. With this option set to a non-zero
timeout, a call to accept() for this ServerSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
ServerSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:**
- timeout

- the specified timeout, in milliseconds

**Throws:**
- SocketException

- if there is an error in
the underlying protocol, such as a TCP error.

**See Also:**
- getSoTimeout()

**Since:**
- 1.1

---

#### public int getSoTimeout()
throws
IOException

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

**Returns:**
- the

SO_TIMEOUT

value

**Throws:**
- IOException

- if an I/O error occurs

**See Also:**
- setSoTimeout(int)

**Since:**
- 1.1

---

#### public void setReuseAddress​(boolean on)
throws
SocketException

Enable/disable the

SO_REUSEADDR

socket option.

When a TCP connection is closed the connection may remain
in a timeout state for a period of time after the connection
is closed (typically known as the

TIME_WAIT

state
or

2MSL

wait state).
For applications using a well known socket address or port
it may not be possible to bind a socket to the required

SocketAddress

if there is a connection in the
timeout state involving the socket address or port.

Enabling

SO_REUSEADDR

prior to
binding the socket using

bind(SocketAddress)

allows the socket
to be bound even though a previous connection is in a timeout state.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:**
- on

- whether to enable or disable the socket option

**Throws:**
- SocketException

- if an error occurs enabling or
disabling the

SO_REUSEADDR

socket option, or the socket is closed.

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

Tests if

SO_REUSEADDR

is enabled.

**Returns:**
- a

boolean

indicating whether or not

SO_REUSEADDR

is enabled.

**Throws:**
- SocketException

- if there is an error
in the underlying protocol, such as a TCP error.

**See Also:**
- setReuseAddress(boolean)

**Since:**
- 1.4

---

#### public
String
toString()

Returns the implementation address and implementation port of
this socket as a

String

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
an

InetAddress

representing the

loopback

address is returned as
the implementation address.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this socket.

---

#### public static void setSocketFactory​(
SocketImplFactory
fac)
throws
IOException

Sets the server socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new server socket, the socket
implementation factory's

createSocketImpl

method is
called to create the actual socket implementation.

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
socket factory.
- SocketException

- if the factory has already been defined.
- SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.

**See Also:**
- SocketImplFactory.createSocketImpl()

,

SecurityManager.checkSetFactory()

---

#### public void setReceiveBufferSize​(int size)
throws
SocketException

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

. The value actually set
in the accepted socket must be determined by calling

Socket.getReceiveBufferSize()

after the socket
is returned by

accept()

.

The value of

SO_RCVBUF

is used both to
set the size of the internal socket receive buffer, and to set the size
of the TCP receive window that is advertized to the remote peer.

It is possible to change the value subsequently, by calling

Socket.setReceiveBufferSize(int)

. However, if the application
wishes to allow a receive window larger than 64K bytes, as defined by RFC1323
then the proposed value must be set in the ServerSocket

before

it is bound to a local address. This implies, that the ServerSocket must be
created with the no-argument constructor, then setReceiveBufferSize() must
be called and lastly the ServerSocket is bound to an address by calling bind().

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

**Parameters:**
- size

- the size to which to set the receive buffer
size. This value must be greater than 0.

**Throws:**
- SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
- IllegalArgumentException

- if the
value is 0 or is negative.

**See Also:**
- getReceiveBufferSize()

**Since:**
- 1.4

---

#### public int getReceiveBufferSize()
throws
SocketException

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

Note, the value actually set in the accepted socket is determined by
calling

Socket.getReceiveBufferSize()

.

**Returns:**
- the value of the

SO_RCVBUF

option for this

Socket

.

**Throws:**
- SocketException

- if there is an error
in the underlying protocol, such as a TCP error.

**See Also:**
- setReceiveBufferSize(int)

**Since:**
- 1.4

---

#### public void setPerformancePreferences​(int connectionTime,
int latency,
int bandwidth)

Sets performance preferences for this ServerSocket.

Sockets use the TCP/IP protocol by default. Some implementations
may offer alternative protocols which have different performance
characteristics than TCP/IP. This method allows the application to
express its own preferences as to how these tradeoffs should be made
when the implementation chooses from the available protocols.

Performance preferences are described by three integers
whose values indicate the relative importance of short connection time,
low latency, and high bandwidth. The absolute values of the integers
are irrelevant; in order to choose a protocol the values are simply
compared, with larger values indicating stronger preferences. If the
application prefers short connection time over both low latency and high
bandwidth, for example, then it could invoke this method with the values

(1, 0, 0)

. If the application prefers high bandwidth above low
latency, and low latency above short connection time, then it could
invoke this method with the values

(0, 1, 2)

.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

**Parameters:**
- connectionTime

- An

int

expressing the relative importance of a short
connection time
- latency

- An

int

expressing the relative importance of low
latency
- bandwidth

- An

int

expressing the relative importance of high
bandwidth

**Since:**
- 1.5

---

#### public <T>
ServerSocket
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
- this ServerSocket

**Throws:**
- UnsupportedOperationException

- if the server socket does not
support the option.
- IllegalArgumentException

- if the value is not valid for
the option.
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

- if the server socket does not
support the option.
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

Returns a set of the socket options supported by this server socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:**
- A set of the socket options supported by this socket. This set
may be empty if the socket's SocketImpl cannot be created.

**Since:**
- 9

---

### Additional Sections

#### Class ServerSocket

java.lang.Object

- java.net.ServerSocket

java.net.ServerSocket

**All Implemented Interfaces:** Closeable

,

AutoCloseable

**Direct Known Subclasses:** SSLServerSocket

```java
public class
ServerSocket

extends
Object

implements
Closeable
```

This class implements server sockets. A server socket waits for
requests to come in over the network. It performs some operation
based on that request, and then possibly returns a result to the requester.

The actual work of the server socket is performed by an instance
of the

SocketImpl

class. An application can
change the socket factory that creates the socket
implementation to configure itself to create sockets
appropriate to the local firewall.

**Since:** 1.0
**See Also:** SocketImpl

,

setSocketFactory(java.net.SocketImplFactory)

,

ServerSocketChannel

public class

ServerSocket

extends

Object

implements

Closeable

This class implements server sockets. A server socket waits for
requests to come in over the network. It performs some operation
based on that request, and then possibly returns a result to the requester.

The actual work of the server socket is performed by an instance
of the

SocketImpl

class. An application can
change the socket factory that creates the socket
implementation to configure itself to create sockets
appropriate to the local firewall.

The actual work of the server socket is performed by an instance
of the

SocketImpl

class. An application can
change the socket factory that creates the socket
implementation to configure itself to create sockets
appropriate to the local firewall.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ServerSocket

()

Creates an unbound server socket.

ServerSocket

​(int port)

Creates a server socket, bound to the specified port.

ServerSocket

​(int port,
int backlog)

Creates a server socket and binds it to the specified local port
number, with the specified backlog.

ServerSocket

​(int port,
int backlog,

InetAddress

bindAddr)

Create a server with the specified port, listen backlog, and
local IP address to bind to.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Socket

accept

()

Listens for a connection to be made to this socket and accepts
it.

void

bind

​(

SocketAddress

endpoint)

Binds the

ServerSocket

to a specific address
(IP address and port number).

void

bind

​(

SocketAddress

endpoint,
int backlog)

Binds the

ServerSocket

to a specific address
(IP address and port number).

void

close

()

Closes this socket.

ServerSocketChannel

getChannel

()

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

InetAddress

getInetAddress

()

Returns the local address of this server socket.

int

getLocalPort

()

Returns the port number on which this socket is listening.

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

getReceiveBufferSize

()

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

boolean

getReuseAddress

()

Tests if

SO_REUSEADDR

is enabled.

int

getSoTimeout

()

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

protected void

implAccept

​(

Socket

s)

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket.

boolean

isBound

()

Returns the binding state of the ServerSocket.

boolean

isClosed

()

Returns the closed state of the ServerSocket.

<T>

ServerSocket

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

void

setPerformancePreferences

​(int connectionTime,
int latency,
int bandwidth)

Sets performance preferences for this ServerSocket.

void

setReceiveBufferSize

​(int size)

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

.

void

setReuseAddress

​(boolean on)

Enable/disable the

SO_REUSEADDR

socket option.

static void

setSocketFactory

​(

SocketImplFactory

fac)

Sets the server socket implementation factory for the
application.

void

setSoTimeout

​(int timeout)

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds.

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of the socket options supported by this server socket.

String

toString

()

Returns the implementation address and implementation port of
this socket as a

String

.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ServerSocket

()

Creates an unbound server socket.

ServerSocket

​(int port)

Creates a server socket, bound to the specified port.

ServerSocket

​(int port,
int backlog)

Creates a server socket and binds it to the specified local port
number, with the specified backlog.

ServerSocket

​(int port,
int backlog,

InetAddress

bindAddr)

Create a server with the specified port, listen backlog, and
local IP address to bind to.

---

#### Constructor Summary

Creates an unbound server socket.

Creates a server socket, bound to the specified port.

Creates a server socket and binds it to the specified local port
number, with the specified backlog.

Create a server with the specified port, listen backlog, and
local IP address to bind to.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Socket

accept

()

Listens for a connection to be made to this socket and accepts
it.

void

bind

​(

SocketAddress

endpoint)

Binds the

ServerSocket

to a specific address
(IP address and port number).

void

bind

​(

SocketAddress

endpoint,
int backlog)

Binds the

ServerSocket

to a specific address
(IP address and port number).

void

close

()

Closes this socket.

ServerSocketChannel

getChannel

()

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

InetAddress

getInetAddress

()

Returns the local address of this server socket.

int

getLocalPort

()

Returns the port number on which this socket is listening.

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

getReceiveBufferSize

()

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

boolean

getReuseAddress

()

Tests if

SO_REUSEADDR

is enabled.

int

getSoTimeout

()

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

protected void

implAccept

​(

Socket

s)

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket.

boolean

isBound

()

Returns the binding state of the ServerSocket.

boolean

isClosed

()

Returns the closed state of the ServerSocket.

<T>

ServerSocket

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

void

setPerformancePreferences

​(int connectionTime,
int latency,
int bandwidth)

Sets performance preferences for this ServerSocket.

void

setReceiveBufferSize

​(int size)

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

.

void

setReuseAddress

​(boolean on)

Enable/disable the

SO_REUSEADDR

socket option.

static void

setSocketFactory

​(

SocketImplFactory

fac)

Sets the server socket implementation factory for the
application.

void

setSoTimeout

​(int timeout)

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds.

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of the socket options supported by this server socket.

String

toString

()

Returns the implementation address and implementation port of
this socket as a

String

.

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

wait

,

wait

,

wait

---

#### Method Summary

Listens for a connection to be made to this socket and accepts
it.

Binds the

ServerSocket

to a specific address
(IP address and port number).

Closes this socket.

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

Returns the local address of this server socket.

Returns the port number on which this socket is listening.

Returns the address of the endpoint this socket is bound to.

Returns the value of a socket option.

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

Tests if

SO_REUSEADDR

is enabled.

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket.

Returns the binding state of the ServerSocket.

Returns the closed state of the ServerSocket.

Sets the value of a socket option.

Sets performance preferences for this ServerSocket.

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

.

Enable/disable the

SO_REUSEADDR

socket option.

Sets the server socket implementation factory for the
application.

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds.

Returns a set of the socket options supported by this server socket.

Returns the implementation address and implementation port of
this socket as a

String

.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ServerSocket

```java
public ServerSocket()
throws
IOException
```

Creates an unbound server socket.

**Throws:** IOException

- IO error when opening the socket.

- ServerSocket

```java
public ServerSocket​(int port)
throws
IOException
```

Creates a server socket, bound to the specified port. A port number
of

0

means that the port number is automatically
allocated, typically from an ephemeral port range. This port
number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to

50

. If a connection
indication arrives when the queue is full, the connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**See Also:** SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

- ServerSocket

```java
public ServerSocket​(int port,
int backlog)
throws
IOException
```

Creates a server socket and binds it to the specified local port
number, with the specified backlog.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to the

backlog

parameter. If
a connection indication arrives when the queue is full, the
connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**See Also:** SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

- ServerSocket

```java
public ServerSocket​(int port,
int backlog,

InetAddress
bindAddr)
throws
IOException
```

Create a server with the specified port, listen backlog, and
local IP address to bind to. The

bindAddr

argument
can be used on a multi-homed host for a ServerSocket that
will only accept connect requests to one of its addresses.
If

bindAddr

is null, it will default accepting
connections on any/all local addresses.
The port must be between 0 and 65535, inclusive.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

If there is a security manager, this method
calls its

checkListen

method
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Parameters:** bindAddr

- the local InetAddress the server will bind to
**Throws:** SecurityException

- if a security manager exists and
its

checkListen

method doesn't allow the operation.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**Since:** 1.1
**See Also:** SocketOptions

,

SocketImpl

,

SecurityManager.checkListen(int)

============ METHOD DETAIL ==========

- Method Detail

- bind

```java
public void bind​(
SocketAddress
endpoint)
throws
IOException
```

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:** endpoint

- The IP address and port number to bind to.
**Throws:** IOException

- if the bind operation fails, or if the socket
is already bound.
**Throws:** SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket
**Since:** 1.4

- bind

```java
public void bind​(
SocketAddress
endpoint,
int backlog)
throws
IOException
```

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** endpoint

- The IP address and port number to bind to.
**Parameters:** backlog

- requested maximum length of the queue of
incoming connections.
**Throws:** IOException

- if the bind operation fails, or if the socket
is already bound.
**Throws:** SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket
**Since:** 1.4

- getInetAddress

```java
public
InetAddress
getInetAddress()
```

Returns the local address of this server socket.

If the socket was bound prior to being

closed

,
then this method will continue to return the local address
after the socket is closed.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
the

loopback

address is returned.

**Returns:** the address to which this socket is bound,
or the loopback address if denied by the security manager,
or

null

if the socket is unbound.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

- getLocalPort

```java
public int getLocalPort()
```

Returns the port number on which this socket is listening.

If the socket was bound prior to being

closed

,
then this method will continue to return the port number
after the socket is closed.

**Returns:** the port number to which this socket is listening or
-1 if the socket is not bound yet.

- getLocalSocketAddress

```java
public
SocketAddress
getLocalSocketAddress()
```

Returns the address of the endpoint this socket is bound to.

If the socket was bound prior to being

closed

,
then this method will continue to return the address of the endpoint
after the socket is closed.

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

address and the local
port to which the socket is bound is returned.

**Returns:** a

SocketAddress

representing the local endpoint of
this socket, or a

SocketAddress

representing the
loopback address if denied by the security manager,
or

null

if the socket is not bound yet.
**Since:** 1.4
**See Also:** getInetAddress()

,

getLocalPort()

,

bind(SocketAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

- accept

```java
public
Socket
accept()
throws
IOException
```

Listens for a connection to be made to this socket and accepts
it. The method blocks until a connection is made.

A new Socket

s

is created and, if there
is a security manager,
the security manager's

checkAccept

method is called
with

s.getInetAddress().getHostAddress()

and

s.getPort()

as its arguments to ensure the operation is allowed.
This could result in a SecurityException.

**Returns:** the new Socket
**Throws:** IOException

- if an I/O error occurs when waiting for a
connection.
**Throws:** SecurityException

- if a security manager exists and its

checkAccept

method doesn't allow the operation.
**Throws:** SocketTimeoutException

- if a timeout was previously set with setSoTimeout and
the timeout has been reached.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel, the channel is in
non-blocking mode, and there is no connection ready to be
accepted
**See Also:** SecurityManager.checkAccept(java.lang.String, int)

- implAccept

```java
protected final void implAccept​(
Socket
s)
throws
IOException
```

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket. So a FooServerSocket
will typically hand this method an

empty

FooSocket. On
return from implAccept the FooSocket will be connected to a client.

**Parameters:** s

- the Socket
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode
**Throws:** IOException

- if an I/O error occurs when waiting
for a connection.
**Since:** 1.1

- close

```java
public void close()
throws
IOException
```

Closes this socket.

Any thread currently blocked in

accept()

will throw
a

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
**Throws:** IOException

- if an I/O error occurs when closing the socket.

- getChannel

```java
public
ServerSocketChannel
getChannel()
```

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

A server socket will have a channel if, and only if, the channel
itself was created via the

ServerSocketChannel.open

method.

**Returns:** the server-socket channel associated with this socket,
or

null

if this socket was not created
for a channel
**Since:** 1.4

- isBound

```java
public boolean isBound()
```

Returns the binding state of the ServerSocket.

**Returns:** true if the ServerSocket successfully bound to an address
**Since:** 1.4

- isClosed

```java
public boolean isClosed()
```

Returns the closed state of the ServerSocket.

**Returns:** true if the socket has been closed
**Since:** 1.4

- setSoTimeout

```java
public void setSoTimeout​(int timeout)
throws
SocketException
```

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds. With this option set to a non-zero
timeout, a call to accept() for this ServerSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
ServerSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:** timeout

- the specified timeout, in milliseconds
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as a TCP error.
**Since:** 1.1
**See Also:** getSoTimeout()

- getSoTimeout

```java
public int getSoTimeout()
throws
IOException
```

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

**Returns:** the

SO_TIMEOUT

value
**Throws:** IOException

- if an I/O error occurs
**Since:** 1.1
**See Also:** setSoTimeout(int)

- setReuseAddress

```java
public void setReuseAddress​(boolean on)
throws
SocketException
```

Enable/disable the

SO_REUSEADDR

socket option.

When a TCP connection is closed the connection may remain
in a timeout state for a period of time after the connection
is closed (typically known as the

TIME_WAIT

state
or

2MSL

wait state).
For applications using a well known socket address or port
it may not be possible to bind a socket to the required

SocketAddress

if there is a connection in the
timeout state involving the socket address or port.

Enabling

SO_REUSEADDR

prior to
binding the socket using

bind(SocketAddress)

allows the socket
to be bound even though a previous connection is in a timeout state.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:** on

- whether to enable or disable the socket option
**Throws:** SocketException

- if an error occurs enabling or
disabling the

SO_REUSEADDR

socket option, or the socket is closed.
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

Tests if

SO_REUSEADDR

is enabled.

**Returns:** a

boolean

indicating whether or not

SO_REUSEADDR

is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Since:** 1.4
**See Also:** setReuseAddress(boolean)

- toString

```java
public
String
toString()
```

Returns the implementation address and implementation port of
this socket as a

String

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
an

InetAddress

representing the

loopback

address is returned as
the implementation address.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this socket.

- setSocketFactory

```java
public static void setSocketFactory​(
SocketImplFactory
fac)
throws
IOException
```

Sets the server socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new server socket, the socket
implementation factory's

createSocketImpl

method is
called to create the actual socket implementation.

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
socket factory.
**Throws:** SocketException

- if the factory has already been defined.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**See Also:** SocketImplFactory.createSocketImpl()

,

SecurityManager.checkSetFactory()

- setReceiveBufferSize

```java
public void setReceiveBufferSize​(int size)
throws
SocketException
```

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

. The value actually set
in the accepted socket must be determined by calling

Socket.getReceiveBufferSize()

after the socket
is returned by

accept()

.

The value of

SO_RCVBUF

is used both to
set the size of the internal socket receive buffer, and to set the size
of the TCP receive window that is advertized to the remote peer.

It is possible to change the value subsequently, by calling

Socket.setReceiveBufferSize(int)

. However, if the application
wishes to allow a receive window larger than 64K bytes, as defined by RFC1323
then the proposed value must be set in the ServerSocket

before

it is bound to a local address. This implies, that the ServerSocket must be
created with the no-argument constructor, then setReceiveBufferSize() must
be called and lastly the ServerSocket is bound to an address by calling bind().

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

**Parameters:** size

- the size to which to set the receive buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Throws:** IllegalArgumentException

- if the
value is 0 or is negative.
**Since:** 1.4
**See Also:** getReceiveBufferSize()

- getReceiveBufferSize

```java
public int getReceiveBufferSize()
throws
SocketException
```

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

Note, the value actually set in the accepted socket is determined by
calling

Socket.getReceiveBufferSize()

.

**Returns:** the value of the

SO_RCVBUF

option for this

Socket

.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Since:** 1.4
**See Also:** setReceiveBufferSize(int)

- setPerformancePreferences

```java
public void setPerformancePreferences​(int connectionTime,
int latency,
int bandwidth)
```

Sets performance preferences for this ServerSocket.

Sockets use the TCP/IP protocol by default. Some implementations
may offer alternative protocols which have different performance
characteristics than TCP/IP. This method allows the application to
express its own preferences as to how these tradeoffs should be made
when the implementation chooses from the available protocols.

Performance preferences are described by three integers
whose values indicate the relative importance of short connection time,
low latency, and high bandwidth. The absolute values of the integers
are irrelevant; in order to choose a protocol the values are simply
compared, with larger values indicating stronger preferences. If the
application prefers short connection time over both low latency and high
bandwidth, for example, then it could invoke this method with the values

(1, 0, 0)

. If the application prefers high bandwidth above low
latency, and low latency above short connection time, then it could
invoke this method with the values

(0, 1, 2)

.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

**Parameters:** connectionTime

- An

int

expressing the relative importance of a short
connection time
**Parameters:** latency

- An

int

expressing the relative importance of low
latency
**Parameters:** bandwidth

- An

int

expressing the relative importance of high
bandwidth
**Since:** 1.5

- setOption

```java
public <T>
ServerSocket
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
**Returns:** this ServerSocket
**Throws:** UnsupportedOperationException

- if the server socket does not
support the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
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

- if the server socket does not
support the option.
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

Returns a set of the socket options supported by this server socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:** A set of the socket options supported by this socket. This set
may be empty if the socket's SocketImpl cannot be created.
**Since:** 9

Constructor Detail

- ServerSocket

```java
public ServerSocket()
throws
IOException
```

Creates an unbound server socket.

**Throws:** IOException

- IO error when opening the socket.

- ServerSocket

```java
public ServerSocket​(int port)
throws
IOException
```

Creates a server socket, bound to the specified port. A port number
of

0

means that the port number is automatically
allocated, typically from an ephemeral port range. This port
number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to

50

. If a connection
indication arrives when the queue is full, the connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**See Also:** SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

- ServerSocket

```java
public ServerSocket​(int port,
int backlog)
throws
IOException
```

Creates a server socket and binds it to the specified local port
number, with the specified backlog.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to the

backlog

parameter. If
a connection indication arrives when the queue is full, the
connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**See Also:** SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

- ServerSocket

```java
public ServerSocket​(int port,
int backlog,

InetAddress
bindAddr)
throws
IOException
```

Create a server with the specified port, listen backlog, and
local IP address to bind to. The

bindAddr

argument
can be used on a multi-homed host for a ServerSocket that
will only accept connect requests to one of its addresses.
If

bindAddr

is null, it will default accepting
connections on any/all local addresses.
The port must be between 0 and 65535, inclusive.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

If there is a security manager, this method
calls its

checkListen

method
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Parameters:** bindAddr

- the local InetAddress the server will bind to
**Throws:** SecurityException

- if a security manager exists and
its

checkListen

method doesn't allow the operation.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**Since:** 1.1
**See Also:** SocketOptions

,

SocketImpl

,

SecurityManager.checkListen(int)

---

#### Constructor Detail

ServerSocket

```java
public ServerSocket()
throws
IOException
```

Creates an unbound server socket.

**Throws:** IOException

- IO error when opening the socket.

---

#### ServerSocket

public ServerSocket()
throws

IOException

Creates an unbound server socket.

ServerSocket

```java
public ServerSocket​(int port)
throws
IOException
```

Creates a server socket, bound to the specified port. A port number
of

0

means that the port number is automatically
allocated, typically from an ephemeral port range. This port
number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to

50

. If a connection
indication arrives when the queue is full, the connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**See Also:** SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

---

#### ServerSocket

public ServerSocket​(int port)
throws

IOException

Creates a server socket, bound to the specified port. A port number
of

0

means that the port number is automatically
allocated, typically from an ephemeral port range. This port
number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to

50

. If a connection
indication arrives when the queue is full, the connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The maximum queue length for incoming connection indications (a
request to connect) is set to

50

. If a connection
indication arrives when the queue is full, the connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

ServerSocket

```java
public ServerSocket​(int port,
int backlog)
throws
IOException
```

Creates a server socket and binds it to the specified local port
number, with the specified backlog.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to the

backlog

parameter. If
a connection indication arrives when the queue is full, the
connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**See Also:** SocketImpl

,

SocketImplFactory.createSocketImpl()

,

setSocketFactory(java.net.SocketImplFactory)

,

SecurityManager.checkListen(int)

---

#### ServerSocket

public ServerSocket​(int port,
int backlog)
throws

IOException

Creates a server socket and binds it to the specified local port
number, with the specified backlog.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

The maximum queue length for incoming connection indications (a
request to connect) is set to the

backlog

parameter. If
a connection indication arrives when the queue is full, the
connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

The maximum queue length for incoming connection indications (a
request to connect) is set to the

backlog

parameter. If
a connection indication arrives when the queue is full, the
connection is refused.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If the application has specified a server socket factory, that
factory's

createSocketImpl

method is called to create
the actual socket implementation. Otherwise a "plain" socket is created.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager,
its

checkListen

method is called
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

ServerSocket

```java
public ServerSocket​(int port,
int backlog,

InetAddress
bindAddr)
throws
IOException
```

Create a server with the specified port, listen backlog, and
local IP address to bind to. The

bindAddr

argument
can be used on a multi-homed host for a ServerSocket that
will only accept connect requests to one of its addresses.
If

bindAddr

is null, it will default accepting
connections on any/all local addresses.
The port must be between 0 and 65535, inclusive.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

If there is a security manager, this method
calls its

checkListen

method
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** port

- the port number, or

0

to use a port
number that is automatically allocated.
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Parameters:** bindAddr

- the local InetAddress the server will bind to
**Throws:** SecurityException

- if a security manager exists and
its

checkListen

method doesn't allow the operation.
**Throws:** IOException

- if an I/O error occurs when opening the socket.
**Throws:** IllegalArgumentException

- if the port parameter is outside
the specified range of valid port values, which is between
0 and 65535, inclusive.
**Since:** 1.1
**See Also:** SocketOptions

,

SocketImpl

,

SecurityManager.checkListen(int)

---

#### ServerSocket

public ServerSocket​(int port,
int backlog,

InetAddress

bindAddr)
throws

IOException

Create a server with the specified port, listen backlog, and
local IP address to bind to. The

bindAddr

argument
can be used on a multi-homed host for a ServerSocket that
will only accept connect requests to one of its addresses.
If

bindAddr

is null, it will default accepting
connections on any/all local addresses.
The port must be between 0 and 65535, inclusive.
A port number of

0

means that the port number is
automatically allocated, typically from an ephemeral port range.
This port number can then be retrieved by calling

getLocalPort

.

If there is a security manager, this method
calls its

checkListen

method
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, this method
calls its

checkListen

method
with the

port

argument
as its argument to ensure the operation is allowed.
This could result in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

Method Detail

- bind

```java
public void bind​(
SocketAddress
endpoint)
throws
IOException
```

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:** endpoint

- The IP address and port number to bind to.
**Throws:** IOException

- if the bind operation fails, or if the socket
is already bound.
**Throws:** SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket
**Since:** 1.4

- bind

```java
public void bind​(
SocketAddress
endpoint,
int backlog)
throws
IOException
```

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** endpoint

- The IP address and port number to bind to.
**Parameters:** backlog

- requested maximum length of the queue of
incoming connections.
**Throws:** IOException

- if the bind operation fails, or if the socket
is already bound.
**Throws:** SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket
**Since:** 1.4

- getInetAddress

```java
public
InetAddress
getInetAddress()
```

Returns the local address of this server socket.

If the socket was bound prior to being

closed

,
then this method will continue to return the local address
after the socket is closed.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
the

loopback

address is returned.

**Returns:** the address to which this socket is bound,
or the loopback address if denied by the security manager,
or

null

if the socket is unbound.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

- getLocalPort

```java
public int getLocalPort()
```

Returns the port number on which this socket is listening.

If the socket was bound prior to being

closed

,
then this method will continue to return the port number
after the socket is closed.

**Returns:** the port number to which this socket is listening or
-1 if the socket is not bound yet.

- getLocalSocketAddress

```java
public
SocketAddress
getLocalSocketAddress()
```

Returns the address of the endpoint this socket is bound to.

If the socket was bound prior to being

closed

,
then this method will continue to return the address of the endpoint
after the socket is closed.

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

address and the local
port to which the socket is bound is returned.

**Returns:** a

SocketAddress

representing the local endpoint of
this socket, or a

SocketAddress

representing the
loopback address if denied by the security manager,
or

null

if the socket is not bound yet.
**Since:** 1.4
**See Also:** getInetAddress()

,

getLocalPort()

,

bind(SocketAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

- accept

```java
public
Socket
accept()
throws
IOException
```

Listens for a connection to be made to this socket and accepts
it. The method blocks until a connection is made.

A new Socket

s

is created and, if there
is a security manager,
the security manager's

checkAccept

method is called
with

s.getInetAddress().getHostAddress()

and

s.getPort()

as its arguments to ensure the operation is allowed.
This could result in a SecurityException.

**Returns:** the new Socket
**Throws:** IOException

- if an I/O error occurs when waiting for a
connection.
**Throws:** SecurityException

- if a security manager exists and its

checkAccept

method doesn't allow the operation.
**Throws:** SocketTimeoutException

- if a timeout was previously set with setSoTimeout and
the timeout has been reached.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel, the channel is in
non-blocking mode, and there is no connection ready to be
accepted
**See Also:** SecurityManager.checkAccept(java.lang.String, int)

- implAccept

```java
protected final void implAccept​(
Socket
s)
throws
IOException
```

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket. So a FooServerSocket
will typically hand this method an

empty

FooSocket. On
return from implAccept the FooSocket will be connected to a client.

**Parameters:** s

- the Socket
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode
**Throws:** IOException

- if an I/O error occurs when waiting
for a connection.
**Since:** 1.1

- close

```java
public void close()
throws
IOException
```

Closes this socket.

Any thread currently blocked in

accept()

will throw
a

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
**Throws:** IOException

- if an I/O error occurs when closing the socket.

- getChannel

```java
public
ServerSocketChannel
getChannel()
```

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

A server socket will have a channel if, and only if, the channel
itself was created via the

ServerSocketChannel.open

method.

**Returns:** the server-socket channel associated with this socket,
or

null

if this socket was not created
for a channel
**Since:** 1.4

- isBound

```java
public boolean isBound()
```

Returns the binding state of the ServerSocket.

**Returns:** true if the ServerSocket successfully bound to an address
**Since:** 1.4

- isClosed

```java
public boolean isClosed()
```

Returns the closed state of the ServerSocket.

**Returns:** true if the socket has been closed
**Since:** 1.4

- setSoTimeout

```java
public void setSoTimeout​(int timeout)
throws
SocketException
```

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds. With this option set to a non-zero
timeout, a call to accept() for this ServerSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
ServerSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:** timeout

- the specified timeout, in milliseconds
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as a TCP error.
**Since:** 1.1
**See Also:** getSoTimeout()

- getSoTimeout

```java
public int getSoTimeout()
throws
IOException
```

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

**Returns:** the

SO_TIMEOUT

value
**Throws:** IOException

- if an I/O error occurs
**Since:** 1.1
**See Also:** setSoTimeout(int)

- setReuseAddress

```java
public void setReuseAddress​(boolean on)
throws
SocketException
```

Enable/disable the

SO_REUSEADDR

socket option.

When a TCP connection is closed the connection may remain
in a timeout state for a period of time after the connection
is closed (typically known as the

TIME_WAIT

state
or

2MSL

wait state).
For applications using a well known socket address or port
it may not be possible to bind a socket to the required

SocketAddress

if there is a connection in the
timeout state involving the socket address or port.

Enabling

SO_REUSEADDR

prior to
binding the socket using

bind(SocketAddress)

allows the socket
to be bound even though a previous connection is in a timeout state.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:** on

- whether to enable or disable the socket option
**Throws:** SocketException

- if an error occurs enabling or
disabling the

SO_REUSEADDR

socket option, or the socket is closed.
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

Tests if

SO_REUSEADDR

is enabled.

**Returns:** a

boolean

indicating whether or not

SO_REUSEADDR

is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Since:** 1.4
**See Also:** setReuseAddress(boolean)

- toString

```java
public
String
toString()
```

Returns the implementation address and implementation port of
this socket as a

String

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
an

InetAddress

representing the

loopback

address is returned as
the implementation address.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this socket.

- setSocketFactory

```java
public static void setSocketFactory​(
SocketImplFactory
fac)
throws
IOException
```

Sets the server socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new server socket, the socket
implementation factory's

createSocketImpl

method is
called to create the actual socket implementation.

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
socket factory.
**Throws:** SocketException

- if the factory has already been defined.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**See Also:** SocketImplFactory.createSocketImpl()

,

SecurityManager.checkSetFactory()

- setReceiveBufferSize

```java
public void setReceiveBufferSize​(int size)
throws
SocketException
```

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

. The value actually set
in the accepted socket must be determined by calling

Socket.getReceiveBufferSize()

after the socket
is returned by

accept()

.

The value of

SO_RCVBUF

is used both to
set the size of the internal socket receive buffer, and to set the size
of the TCP receive window that is advertized to the remote peer.

It is possible to change the value subsequently, by calling

Socket.setReceiveBufferSize(int)

. However, if the application
wishes to allow a receive window larger than 64K bytes, as defined by RFC1323
then the proposed value must be set in the ServerSocket

before

it is bound to a local address. This implies, that the ServerSocket must be
created with the no-argument constructor, then setReceiveBufferSize() must
be called and lastly the ServerSocket is bound to an address by calling bind().

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

**Parameters:** size

- the size to which to set the receive buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Throws:** IllegalArgumentException

- if the
value is 0 or is negative.
**Since:** 1.4
**See Also:** getReceiveBufferSize()

- getReceiveBufferSize

```java
public int getReceiveBufferSize()
throws
SocketException
```

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

Note, the value actually set in the accepted socket is determined by
calling

Socket.getReceiveBufferSize()

.

**Returns:** the value of the

SO_RCVBUF

option for this

Socket

.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Since:** 1.4
**See Also:** setReceiveBufferSize(int)

- setPerformancePreferences

```java
public void setPerformancePreferences​(int connectionTime,
int latency,
int bandwidth)
```

Sets performance preferences for this ServerSocket.

Sockets use the TCP/IP protocol by default. Some implementations
may offer alternative protocols which have different performance
characteristics than TCP/IP. This method allows the application to
express its own preferences as to how these tradeoffs should be made
when the implementation chooses from the available protocols.

Performance preferences are described by three integers
whose values indicate the relative importance of short connection time,
low latency, and high bandwidth. The absolute values of the integers
are irrelevant; in order to choose a protocol the values are simply
compared, with larger values indicating stronger preferences. If the
application prefers short connection time over both low latency and high
bandwidth, for example, then it could invoke this method with the values

(1, 0, 0)

. If the application prefers high bandwidth above low
latency, and low latency above short connection time, then it could
invoke this method with the values

(0, 1, 2)

.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

**Parameters:** connectionTime

- An

int

expressing the relative importance of a short
connection time
**Parameters:** latency

- An

int

expressing the relative importance of low
latency
**Parameters:** bandwidth

- An

int

expressing the relative importance of high
bandwidth
**Since:** 1.5

- setOption

```java
public <T>
ServerSocket
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
**Returns:** this ServerSocket
**Throws:** UnsupportedOperationException

- if the server socket does not
support the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
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

- if the server socket does not
support the option.
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

Returns a set of the socket options supported by this server socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:** A set of the socket options supported by this socket. This set
may be empty if the socket's SocketImpl cannot be created.
**Since:** 9

---

#### Method Detail

bind

```java
public void bind​(
SocketAddress
endpoint)
throws
IOException
```

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

**Parameters:** endpoint

- The IP address and port number to bind to.
**Throws:** IOException

- if the bind operation fails, or if the socket
is already bound.
**Throws:** SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket
**Since:** 1.4

---

#### bind

public void bind​(

SocketAddress

endpoint)
throws

IOException

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

bind

```java
public void bind​(
SocketAddress
endpoint,
int backlog)
throws
IOException
```

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

**Parameters:** endpoint

- The IP address and port number to bind to.
**Parameters:** backlog

- requested maximum length of the queue of
incoming connections.
**Throws:** IOException

- if the bind operation fails, or if the socket
is already bound.
**Throws:** SecurityException

- if a

SecurityManager

is present and
its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if endpoint is a
SocketAddress subclass not supported by this socket
**Since:** 1.4

---

#### bind

public void bind​(

SocketAddress

endpoint,
int backlog)
throws

IOException

Binds the

ServerSocket

to a specific address
(IP address and port number).

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If the address is

null

, then the system will pick up
an ephemeral port and a valid local address to bind the socket.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

getInetAddress

```java
public
InetAddress
getInetAddress()
```

Returns the local address of this server socket.

If the socket was bound prior to being

closed

,
then this method will continue to return the local address
after the socket is closed.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
the

loopback

address is returned.

**Returns:** the address to which this socket is bound,
or the loopback address if denied by the security manager,
or

null

if the socket is unbound.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

---

#### getInetAddress

public

InetAddress

getInetAddress()

Returns the local address of this server socket.

If the socket was bound prior to being

closed

,
then this method will continue to return the local address
after the socket is closed.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
the

loopback

address is returned.

If the socket was bound prior to being

closed

,
then this method will continue to return the local address
after the socket is closed.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
the

loopback

address is returned.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
the

loopback

address is returned.

getLocalPort

```java
public int getLocalPort()
```

Returns the port number on which this socket is listening.

If the socket was bound prior to being

closed

,
then this method will continue to return the port number
after the socket is closed.

**Returns:** the port number to which this socket is listening or
-1 if the socket is not bound yet.

---

#### getLocalPort

public int getLocalPort()

Returns the port number on which this socket is listening.

If the socket was bound prior to being

closed

,
then this method will continue to return the port number
after the socket is closed.

If the socket was bound prior to being

closed

,
then this method will continue to return the port number
after the socket is closed.

getLocalSocketAddress

```java
public
SocketAddress
getLocalSocketAddress()
```

Returns the address of the endpoint this socket is bound to.

If the socket was bound prior to being

closed

,
then this method will continue to return the address of the endpoint
after the socket is closed.

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

address and the local
port to which the socket is bound is returned.

**Returns:** a

SocketAddress

representing the local endpoint of
this socket, or a

SocketAddress

representing the
loopback address if denied by the security manager,
or

null

if the socket is not bound yet.
**Since:** 1.4
**See Also:** getInetAddress()

,

getLocalPort()

,

bind(SocketAddress)

,

SecurityManager.checkConnect(java.lang.String, int)

---

#### getLocalSocketAddress

public

SocketAddress

getLocalSocketAddress()

Returns the address of the endpoint this socket is bound to.

If the socket was bound prior to being

closed

,
then this method will continue to return the address of the endpoint
after the socket is closed.

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

address and the local
port to which the socket is bound is returned.

If the socket was bound prior to being

closed

,
then this method will continue to return the address of the endpoint
after the socket is closed.

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

address and the local
port to which the socket is bound is returned.

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

address and the local
port to which the socket is bound is returned.

accept

```java
public
Socket
accept()
throws
IOException
```

Listens for a connection to be made to this socket and accepts
it. The method blocks until a connection is made.

A new Socket

s

is created and, if there
is a security manager,
the security manager's

checkAccept

method is called
with

s.getInetAddress().getHostAddress()

and

s.getPort()

as its arguments to ensure the operation is allowed.
This could result in a SecurityException.

**Returns:** the new Socket
**Throws:** IOException

- if an I/O error occurs when waiting for a
connection.
**Throws:** SecurityException

- if a security manager exists and its

checkAccept

method doesn't allow the operation.
**Throws:** SocketTimeoutException

- if a timeout was previously set with setSoTimeout and
the timeout has been reached.
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel, the channel is in
non-blocking mode, and there is no connection ready to be
accepted
**See Also:** SecurityManager.checkAccept(java.lang.String, int)

---

#### accept

public

Socket

accept()
throws

IOException

Listens for a connection to be made to this socket and accepts
it. The method blocks until a connection is made.

A new Socket

s

is created and, if there
is a security manager,
the security manager's

checkAccept

method is called
with

s.getInetAddress().getHostAddress()

and

s.getPort()

as its arguments to ensure the operation is allowed.
This could result in a SecurityException.

A new Socket

s

is created and, if there
is a security manager,
the security manager's

checkAccept

method is called
with

s.getInetAddress().getHostAddress()

and

s.getPort()

as its arguments to ensure the operation is allowed.
This could result in a SecurityException.

implAccept

```java
protected final void implAccept​(
Socket
s)
throws
IOException
```

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket. So a FooServerSocket
will typically hand this method an

empty

FooSocket. On
return from implAccept the FooSocket will be connected to a client.

**Parameters:** s

- the Socket
**Throws:** IllegalBlockingModeException

- if this socket has an associated channel,
and the channel is in non-blocking mode
**Throws:** IOException

- if an I/O error occurs when waiting
for a connection.
**Since:** 1.1

---

#### implAccept

protected final void implAccept​(

Socket

s)
throws

IOException

Subclasses of ServerSocket use this method to override accept()
to return their own subclass of socket. So a FooServerSocket
will typically hand this method an

empty

FooSocket. On
return from implAccept the FooSocket will be connected to a client.

close

```java
public void close()
throws
IOException
```

Closes this socket.

Any thread currently blocked in

accept()

will throw
a

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
**Throws:** IOException

- if an I/O error occurs when closing the socket.

---

#### close

public void close()
throws

IOException

Closes this socket.

Any thread currently blocked in

accept()

will throw
a

SocketException

.

If this socket has an associated channel then the channel is closed
as well.

If this socket has an associated channel then the channel is closed
as well.

getChannel

```java
public
ServerSocketChannel
getChannel()
```

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

A server socket will have a channel if, and only if, the channel
itself was created via the

ServerSocketChannel.open

method.

**Returns:** the server-socket channel associated with this socket,
or

null

if this socket was not created
for a channel
**Since:** 1.4

---

#### getChannel

public

ServerSocketChannel

getChannel()

Returns the unique

ServerSocketChannel

object
associated with this socket, if any.

A server socket will have a channel if, and only if, the channel
itself was created via the

ServerSocketChannel.open

method.

A server socket will have a channel if, and only if, the channel
itself was created via the

ServerSocketChannel.open

method.

isBound

```java
public boolean isBound()
```

Returns the binding state of the ServerSocket.

**Returns:** true if the ServerSocket successfully bound to an address
**Since:** 1.4

---

#### isBound

public boolean isBound()

Returns the binding state of the ServerSocket.

isClosed

```java
public boolean isClosed()
```

Returns the closed state of the ServerSocket.

**Returns:** true if the socket has been closed
**Since:** 1.4

---

#### isClosed

public boolean isClosed()

Returns the closed state of the ServerSocket.

setSoTimeout

```java
public void setSoTimeout​(int timeout)
throws
SocketException
```

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds. With this option set to a non-zero
timeout, a call to accept() for this ServerSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
ServerSocket is still valid. The option

must

be enabled
prior to entering the blocking operation to have effect. The
timeout must be

> 0

.
A timeout of zero is interpreted as an infinite timeout.

**Parameters:** timeout

- the specified timeout, in milliseconds
**Throws:** SocketException

- if there is an error in
the underlying protocol, such as a TCP error.
**Since:** 1.1
**See Also:** getSoTimeout()

---

#### setSoTimeout

public void setSoTimeout​(int timeout)
throws

SocketException

Enable/disable

SO_TIMEOUT

with the
specified timeout, in milliseconds. With this option set to a non-zero
timeout, a call to accept() for this ServerSocket
will block for only this amount of time. If the timeout expires,
a

java.net.SocketTimeoutException

is raised, though the
ServerSocket is still valid. The option

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
IOException
```

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

**Returns:** the

SO_TIMEOUT

value
**Throws:** IOException

- if an I/O error occurs
**Since:** 1.1
**See Also:** setSoTimeout(int)

---

#### getSoTimeout

public int getSoTimeout()
throws

IOException

Retrieve setting for

SO_TIMEOUT

.
0 returns implies that the option is disabled (i.e., timeout of infinity).

setReuseAddress

```java
public void setReuseAddress​(boolean on)
throws
SocketException
```

Enable/disable the

SO_REUSEADDR

socket option.

When a TCP connection is closed the connection may remain
in a timeout state for a period of time after the connection
is closed (typically known as the

TIME_WAIT

state
or

2MSL

wait state).
For applications using a well known socket address or port
it may not be possible to bind a socket to the required

SocketAddress

if there is a connection in the
timeout state involving the socket address or port.

Enabling

SO_REUSEADDR

prior to
binding the socket using

bind(SocketAddress)

allows the socket
to be bound even though a previous connection is in a timeout state.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

**Parameters:** on

- whether to enable or disable the socket option
**Throws:** SocketException

- if an error occurs enabling or
disabling the

SO_REUSEADDR

socket option, or the socket is closed.
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

Enable/disable the

SO_REUSEADDR

socket option.

When a TCP connection is closed the connection may remain
in a timeout state for a period of time after the connection
is closed (typically known as the

TIME_WAIT

state
or

2MSL

wait state).
For applications using a well known socket address or port
it may not be possible to bind a socket to the required

SocketAddress

if there is a connection in the
timeout state involving the socket address or port.

Enabling

SO_REUSEADDR

prior to
binding the socket using

bind(SocketAddress)

allows the socket
to be bound even though a previous connection is in a timeout state.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

When a TCP connection is closed the connection may remain
in a timeout state for a period of time after the connection
is closed (typically known as the

TIME_WAIT

state
or

2MSL

wait state).
For applications using a well known socket address or port
it may not be possible to bind a socket to the required

SocketAddress

if there is a connection in the
timeout state involving the socket address or port.

Enabling

SO_REUSEADDR

prior to
binding the socket using

bind(SocketAddress)

allows the socket
to be bound even though a previous connection is in a timeout state.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

Enabling

SO_REUSEADDR

prior to
binding the socket using

bind(SocketAddress)

allows the socket
to be bound even though a previous connection is in a timeout state.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

When a

ServerSocket

is created the initial setting
of

SO_REUSEADDR

is not defined.
Applications can use

getReuseAddress()

to determine the initial
setting of

SO_REUSEADDR

.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

The behaviour when

SO_REUSEADDR

is
enabled or disabled after a socket is bound (See

isBound()

)
is not defined.

getReuseAddress

```java
public boolean getReuseAddress()
throws
SocketException
```

Tests if

SO_REUSEADDR

is enabled.

**Returns:** a

boolean

indicating whether or not

SO_REUSEADDR

is enabled.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Since:** 1.4
**See Also:** setReuseAddress(boolean)

---

#### getReuseAddress

public boolean getReuseAddress()
throws

SocketException

Tests if

SO_REUSEADDR

is enabled.

toString

```java
public
String
toString()
```

Returns the implementation address and implementation port of
this socket as a

String

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
an

InetAddress

representing the

loopback

address is returned as
the implementation address.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this socket.

---

#### toString

public

String

toString()

Returns the implementation address and implementation port of
this socket as a

String

.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
an

InetAddress

representing the

loopback

address is returned as
the implementation address.

If there is a security manager set, its

checkConnect

method is
called with the local address and

-1

as its arguments to see
if the operation is allowed. If the operation is not allowed,
an

InetAddress

representing the

loopback

address is returned as
the implementation address.

setSocketFactory

```java
public static void setSocketFactory​(
SocketImplFactory
fac)
throws
IOException
```

Sets the server socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new server socket, the socket
implementation factory's

createSocketImpl

method is
called to create the actual socket implementation.

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
socket factory.
**Throws:** SocketException

- if the factory has already been defined.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**See Also:** SocketImplFactory.createSocketImpl()

,

SecurityManager.checkSetFactory()

---

#### setSocketFactory

public static void setSocketFactory​(

SocketImplFactory

fac)
throws

IOException

Sets the server socket implementation factory for the
application. The factory can be specified only once.

When an application creates a new server socket, the socket
implementation factory's

createSocketImpl

method is
called to create the actual socket implementation.

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

When an application creates a new server socket, the socket
implementation factory's

createSocketImpl

method is
called to create the actual socket implementation.

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

setReceiveBufferSize

```java
public void setReceiveBufferSize​(int size)
throws
SocketException
```

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

. The value actually set
in the accepted socket must be determined by calling

Socket.getReceiveBufferSize()

after the socket
is returned by

accept()

.

The value of

SO_RCVBUF

is used both to
set the size of the internal socket receive buffer, and to set the size
of the TCP receive window that is advertized to the remote peer.

It is possible to change the value subsequently, by calling

Socket.setReceiveBufferSize(int)

. However, if the application
wishes to allow a receive window larger than 64K bytes, as defined by RFC1323
then the proposed value must be set in the ServerSocket

before

it is bound to a local address. This implies, that the ServerSocket must be
created with the no-argument constructor, then setReceiveBufferSize() must
be called and lastly the ServerSocket is bound to an address by calling bind().

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

**Parameters:** size

- the size to which to set the receive buffer
size. This value must be greater than 0.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Throws:** IllegalArgumentException

- if the
value is 0 or is negative.
**Since:** 1.4
**See Also:** getReceiveBufferSize()

---

#### setReceiveBufferSize

public void setReceiveBufferSize​(int size)
throws

SocketException

Sets a default proposed value for the

SO_RCVBUF

option for sockets
accepted from this

ServerSocket

. The value actually set
in the accepted socket must be determined by calling

Socket.getReceiveBufferSize()

after the socket
is returned by

accept()

.

The value of

SO_RCVBUF

is used both to
set the size of the internal socket receive buffer, and to set the size
of the TCP receive window that is advertized to the remote peer.

It is possible to change the value subsequently, by calling

Socket.setReceiveBufferSize(int)

. However, if the application
wishes to allow a receive window larger than 64K bytes, as defined by RFC1323
then the proposed value must be set in the ServerSocket

before

it is bound to a local address. This implies, that the ServerSocket must be
created with the no-argument constructor, then setReceiveBufferSize() must
be called and lastly the ServerSocket is bound to an address by calling bind().

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

The value of

SO_RCVBUF

is used both to
set the size of the internal socket receive buffer, and to set the size
of the TCP receive window that is advertized to the remote peer.

It is possible to change the value subsequently, by calling

Socket.setReceiveBufferSize(int)

. However, if the application
wishes to allow a receive window larger than 64K bytes, as defined by RFC1323
then the proposed value must be set in the ServerSocket

before

it is bound to a local address. This implies, that the ServerSocket must be
created with the no-argument constructor, then setReceiveBufferSize() must
be called and lastly the ServerSocket is bound to an address by calling bind().

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

It is possible to change the value subsequently, by calling

Socket.setReceiveBufferSize(int)

. However, if the application
wishes to allow a receive window larger than 64K bytes, as defined by RFC1323
then the proposed value must be set in the ServerSocket

before

it is bound to a local address. This implies, that the ServerSocket must be
created with the no-argument constructor, then setReceiveBufferSize() must
be called and lastly the ServerSocket is bound to an address by calling bind().

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

Failure to do this will not cause an error, and the buffer size may be set to the
requested value but the TCP receive window in sockets accepted from
this ServerSocket will be no larger than 64K bytes.

getReceiveBufferSize

```java
public int getReceiveBufferSize()
throws
SocketException
```

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

Note, the value actually set in the accepted socket is determined by
calling

Socket.getReceiveBufferSize()

.

**Returns:** the value of the

SO_RCVBUF

option for this

Socket

.
**Throws:** SocketException

- if there is an error
in the underlying protocol, such as a TCP error.
**Since:** 1.4
**See Also:** setReceiveBufferSize(int)

---

#### getReceiveBufferSize

public int getReceiveBufferSize()
throws

SocketException

Gets the value of the

SO_RCVBUF

option
for this

ServerSocket

, that is the proposed buffer size that
will be used for Sockets accepted from this

ServerSocket

.

Note, the value actually set in the accepted socket is determined by
calling

Socket.getReceiveBufferSize()

.

Note, the value actually set in the accepted socket is determined by
calling

Socket.getReceiveBufferSize()

.

setPerformancePreferences

```java
public void setPerformancePreferences​(int connectionTime,
int latency,
int bandwidth)
```

Sets performance preferences for this ServerSocket.

Sockets use the TCP/IP protocol by default. Some implementations
may offer alternative protocols which have different performance
characteristics than TCP/IP. This method allows the application to
express its own preferences as to how these tradeoffs should be made
when the implementation chooses from the available protocols.

Performance preferences are described by three integers
whose values indicate the relative importance of short connection time,
low latency, and high bandwidth. The absolute values of the integers
are irrelevant; in order to choose a protocol the values are simply
compared, with larger values indicating stronger preferences. If the
application prefers short connection time over both low latency and high
bandwidth, for example, then it could invoke this method with the values

(1, 0, 0)

. If the application prefers high bandwidth above low
latency, and low latency above short connection time, then it could
invoke this method with the values

(0, 1, 2)

.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

**Parameters:** connectionTime

- An

int

expressing the relative importance of a short
connection time
**Parameters:** latency

- An

int

expressing the relative importance of low
latency
**Parameters:** bandwidth

- An

int

expressing the relative importance of high
bandwidth
**Since:** 1.5

---

#### setPerformancePreferences

public void setPerformancePreferences​(int connectionTime,
int latency,
int bandwidth)

Sets performance preferences for this ServerSocket.

Sockets use the TCP/IP protocol by default. Some implementations
may offer alternative protocols which have different performance
characteristics than TCP/IP. This method allows the application to
express its own preferences as to how these tradeoffs should be made
when the implementation chooses from the available protocols.

Performance preferences are described by three integers
whose values indicate the relative importance of short connection time,
low latency, and high bandwidth. The absolute values of the integers
are irrelevant; in order to choose a protocol the values are simply
compared, with larger values indicating stronger preferences. If the
application prefers short connection time over both low latency and high
bandwidth, for example, then it could invoke this method with the values

(1, 0, 0)

. If the application prefers high bandwidth above low
latency, and low latency above short connection time, then it could
invoke this method with the values

(0, 1, 2)

.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

Sockets use the TCP/IP protocol by default. Some implementations
may offer alternative protocols which have different performance
characteristics than TCP/IP. This method allows the application to
express its own preferences as to how these tradeoffs should be made
when the implementation chooses from the available protocols.

Performance preferences are described by three integers
whose values indicate the relative importance of short connection time,
low latency, and high bandwidth. The absolute values of the integers
are irrelevant; in order to choose a protocol the values are simply
compared, with larger values indicating stronger preferences. If the
application prefers short connection time over both low latency and high
bandwidth, for example, then it could invoke this method with the values

(1, 0, 0)

. If the application prefers high bandwidth above low
latency, and low latency above short connection time, then it could
invoke this method with the values

(0, 1, 2)

.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

Performance preferences are described by three integers
whose values indicate the relative importance of short connection time,
low latency, and high bandwidth. The absolute values of the integers
are irrelevant; in order to choose a protocol the values are simply
compared, with larger values indicating stronger preferences. If the
application prefers short connection time over both low latency and high
bandwidth, for example, then it could invoke this method with the values

(1, 0, 0)

. If the application prefers high bandwidth above low
latency, and low latency above short connection time, then it could
invoke this method with the values

(0, 1, 2)

.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

Invoking this method after this socket has been bound
will have no effect. This implies that in order to use this capability
requires the socket to be created with the no-argument constructor.

setOption

```java
public <T>
ServerSocket
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
**Returns:** this ServerSocket
**Throws:** UnsupportedOperationException

- if the server socket does not
support the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
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

#### setOption

public <T>

ServerSocket

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

- if the server socket does not
support the option.
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

Returns a set of the socket options supported by this server socket.

This method will continue to return the set of options even after
the socket has been closed.

**Returns:** A set of the socket options supported by this socket. This set
may be empty if the socket's SocketImpl cannot be created.
**Since:** 9

---

#### supportedOptions

public

Set

<

SocketOption

<?>> supportedOptions()

Returns a set of the socket options supported by this server socket.

This method will continue to return the set of options even after
the socket has been closed.

---

