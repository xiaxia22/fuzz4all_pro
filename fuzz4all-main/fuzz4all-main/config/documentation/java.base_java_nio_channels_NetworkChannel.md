# Interface NetworkChannel

**Source:** `java.base\java\nio\channels\NetworkChannel.html`

### Class Description

```java
public interface
NetworkChannel

extends
Channel
```

A channel to a network socket.

A channel that implements this interface is a channel to a network
socket. The

bind

method is used to bind the
socket to a local

address

, the

getLocalAddress

method returns the address that the socket is bound to, and
the

setOption

and

getOption

methods are used to set and query socket
options. An implementation of this interface should specify the socket options
that it supports.

The

bind

and

setOption

methods that do
not otherwise have a value to return are specified to return the network
channel upon which they are invoked. This allows method invocations to be
chained. Implementations of this interface should specialize the return type
so that method invocations on the implementation class can be chained.

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### NetworkChannel
bind​(
SocketAddress
local)
throws
IOException

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

**Parameters:**
- local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address

**Returns:**
- This channel

**Throws:**
- AlreadyBoundException

- If the socket is already bound
- UnsupportedAddressTypeException

- If the type of the given address is not supported
- ClosedChannelException

- If the channel is closed
- IOException

- If some other I/O error occurs
- SecurityException

- If a security manager is installed and it denies an unspecified
permission. An implementation of this interface should specify
any required permissions.

**See Also:**
- getLocalAddress()

---

#### SocketAddress
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

**Returns:**
- The socket address that the socket is bound to, or

null

if the channel's socket is not bound

**Throws:**
- ClosedChannelException

- If the channel is closed
- IOException

- If an I/O error occurs

---

#### <T>
NetworkChannel
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

**Type Parameters:**
- T

- The type of the socket option value

---

#### <T> T getOption​(
SocketOption
<T> name)
throws
IOException

Returns the value of a socket option.

**Parameters:**
- name

- The socket option

**Returns:**
- The value of the socket option. A value of

null

may be
a valid value for some socket options.

**Throws:**
- UnsupportedOperationException

- If the socket option is not supported by this channel
- ClosedChannelException

- If this channel is closed
- IOException

- If an I/O error occurs

**See Also:**
- StandardSocketOptions

**Type Parameters:**
- T

- The type of the socket option value

---

#### Set
<
SocketOption
<?>> supportedOptions()

Returns a set of the socket options supported by this channel.

This method will continue to return the set of options even after the
channel has been closed.

**Returns:**
- A set of the socket options supported by this channel

---

### Additional Sections

#### Interface NetworkChannel

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

**All Known Subinterfaces:** MulticastChannel

**All Known Implementing Classes:** AsynchronousServerSocketChannel

,

AsynchronousSocketChannel

,

DatagramChannel

,

ServerSocketChannel

,

SocketChannel

```java
public interface
NetworkChannel

extends
Channel
```

A channel to a network socket.

A channel that implements this interface is a channel to a network
socket. The

bind

method is used to bind the
socket to a local

address

, the

getLocalAddress

method returns the address that the socket is bound to, and
the

setOption

and

getOption

methods are used to set and query socket
options. An implementation of this interface should specify the socket options
that it supports.

The

bind

and

setOption

methods that do
not otherwise have a value to return are specified to return the network
channel upon which they are invoked. This allows method invocations to be
chained. Implementations of this interface should specialize the return type
so that method invocations on the implementation class can be chained.

**Since:** 1.7

public interface

NetworkChannel

extends

Channel

A channel to a network socket.

A channel that implements this interface is a channel to a network
socket. The

bind

method is used to bind the
socket to a local

address

, the

getLocalAddress

method returns the address that the socket is bound to, and
the

setOption

and

getOption

methods are used to set and query socket
options. An implementation of this interface should specify the socket options
that it supports.

The

bind

and

setOption

methods that do
not otherwise have a value to return are specified to return the network
channel upon which they are invoked. This allows method invocations to be
chained. Implementations of this interface should specialize the return type
so that method invocations on the implementation class can be chained.

A channel that implements this interface is a channel to a network
socket. The

bind

method is used to bind the
socket to a local

address

, the

getLocalAddress

method returns the address that the socket is bound to, and
the

setOption

and

getOption

methods are used to set and query socket
options. An implementation of this interface should specify the socket options
that it supports.

The

bind

and

setOption

methods that do
not otherwise have a value to return are specified to return the network
channel upon which they are invoked. This allows method invocations to be
chained. Implementations of this interface should specialize the return type
so that method invocations on the implementation class can be chained.

The

bind

and

setOption

methods that do
not otherwise have a value to return are specified to return the network
channel upon which they are invoked. This allows method invocations to be
chained. Implementations of this interface should specialize the return type
so that method invocations on the implementation class can be chained.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

NetworkChannel

bind

​(

SocketAddress

local)

Binds the channel's socket to a local address.

SocketAddress

getLocalAddress

()

Returns the socket address that this channel's socket is bound to.

<T> T

getOption

​(

SocketOption

<T> name)

Returns the value of a socket option.

<T>

NetworkChannel

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of the socket options supported by this channel.

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

NetworkChannel

bind

​(

SocketAddress

local)

Binds the channel's socket to a local address.

SocketAddress

getLocalAddress

()

Returns the socket address that this channel's socket is bound to.

<T> T

getOption

​(

SocketOption

<T> name)

Returns the value of a socket option.

<T>

NetworkChannel

setOption

​(

SocketOption

<T> name,
T value)

Sets the value of a socket option.

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of the socket options supported by this channel.

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

---

#### Method Summary

Binds the channel's socket to a local address.

Returns the socket address that this channel's socket is bound to.

Returns the value of a socket option.

Sets the value of a socket option.

Returns a set of the socket options supported by this channel.

Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

---

#### Methods declared in interface java.nio.channels. Channel

============ METHOD DETAIL ==========

- Method Detail

- bind

```java
NetworkChannel
bind​(
SocketAddress
local)
throws
IOException
```

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

**Parameters:** local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address
**Returns:** This channel
**Throws:** AlreadyBoundException

- If the socket is already bound
**Throws:** UnsupportedAddressTypeException

- If the type of the given address is not supported
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Throws:** SecurityException

- If a security manager is installed and it denies an unspecified
permission. An implementation of this interface should specify
any required permissions.
**See Also:** getLocalAddress()

- getLocalAddress

```java
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

**Returns:** The socket address that the socket is bound to, or

null

if the channel's socket is not bound
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs

- setOption

```java
<T>
NetworkChannel
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
**See Also:** StandardSocketOptions

- getOption

```java
<T> T getOption​(
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
**Returns:** The value of the socket option. A value of

null

may be
a valid value for some socket options.
**Throws:** UnsupportedOperationException

- If the socket option is not supported by this channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs
**See Also:** StandardSocketOptions

- supportedOptions

```java
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of the socket options supported by this channel.

This method will continue to return the set of options even after the
channel has been closed.

**Returns:** A set of the socket options supported by this channel

Method Detail

- bind

```java
NetworkChannel
bind​(
SocketAddress
local)
throws
IOException
```

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

**Parameters:** local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address
**Returns:** This channel
**Throws:** AlreadyBoundException

- If the socket is already bound
**Throws:** UnsupportedAddressTypeException

- If the type of the given address is not supported
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Throws:** SecurityException

- If a security manager is installed and it denies an unspecified
permission. An implementation of this interface should specify
any required permissions.
**See Also:** getLocalAddress()

- getLocalAddress

```java
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

**Returns:** The socket address that the socket is bound to, or

null

if the channel's socket is not bound
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs

- setOption

```java
<T>
NetworkChannel
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
**See Also:** StandardSocketOptions

- getOption

```java
<T> T getOption​(
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
**Returns:** The value of the socket option. A value of

null

may be
a valid value for some socket options.
**Throws:** UnsupportedOperationException

- If the socket option is not supported by this channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs
**See Also:** StandardSocketOptions

- supportedOptions

```java
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of the socket options supported by this channel.

This method will continue to return the set of options even after the
channel has been closed.

**Returns:** A set of the socket options supported by this channel

---

#### Method Detail

bind

```java
NetworkChannel
bind​(
SocketAddress
local)
throws
IOException
```

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

**Parameters:** local

- The address to bind the socket, or

null

to bind the socket
to an automatically assigned socket address
**Returns:** This channel
**Throws:** AlreadyBoundException

- If the socket is already bound
**Throws:** UnsupportedAddressTypeException

- If the type of the given address is not supported
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If some other I/O error occurs
**Throws:** SecurityException

- If a security manager is installed and it denies an unspecified
permission. An implementation of this interface should specify
any required permissions.
**See Also:** getLocalAddress()

---

#### bind

NetworkChannel

bind​(

SocketAddress

local)
throws

IOException

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

getLocalAddress

```java
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

**Returns:** The socket address that the socket is bound to, or

null

if the channel's socket is not bound
**Throws:** ClosedChannelException

- If the channel is closed
**Throws:** IOException

- If an I/O error occurs

---

#### getLocalAddress

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

Where the channel is

bound

to an Internet Protocol
socket address then the return value from this method is of type

InetSocketAddress

.

setOption

```java
<T>
NetworkChannel
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
**See Also:** StandardSocketOptions

---

#### setOption

<T>

NetworkChannel

setOption​(

SocketOption

<T> name,
T value)
throws

IOException

Sets the value of a socket option.

getOption

```java
<T> T getOption​(
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
**Returns:** The value of the socket option. A value of

null

may be
a valid value for some socket options.
**Throws:** UnsupportedOperationException

- If the socket option is not supported by this channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs
**See Also:** StandardSocketOptions

---

#### getOption

<T> T getOption​(

SocketOption

<T> name)
throws

IOException

Returns the value of a socket option.

supportedOptions

```java
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of the socket options supported by this channel.

This method will continue to return the set of options even after the
channel has been closed.

**Returns:** A set of the socket options supported by this channel

---

#### supportedOptions

Set

<

SocketOption

<?>> supportedOptions()

Returns a set of the socket options supported by this channel.

This method will continue to return the set of options even after the
channel has been closed.

This method will continue to return the set of options even after the
channel has been closed.

---

