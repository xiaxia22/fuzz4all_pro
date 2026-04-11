# Class DatagramSocketImpl

**Source:** `java.base\java\net\DatagramSocketImpl.html`

### Class Description

```java
public abstract class
DatagramSocketImpl

extends
Object

implements
SocketOptions
```

Abstract datagram and multicast socket implementation base class.

**All Implemented Interfaces:** SocketOptions

---

### Field Details

#### protected int localPort

The local port number.

---

#### protected
FileDescriptor
fd

The file descriptor object.

---

### Constructor Details

#### public DatagramSocketImpl()

*No description found.*

---

### Method Details

#### protected abstract void create()
throws
SocketException

Creates a datagram socket.

**Throws:**
- SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

---

#### protected abstract void bind​(int lport,

InetAddress
laddr)
throws
SocketException

Binds a datagram socket to a local port and address.

**Parameters:**
- lport

- the local port
- laddr

- the local address

**Throws:**
- SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

---

#### protected abstract void send​(
DatagramPacket
p)
throws
IOException

Sends a datagram packet. The packet contains the data and the
destination address to send the packet to.

**Parameters:**
- p

- the packet to be sent.

**Throws:**
- IOException

- if an I/O exception occurs while sending the
datagram packet.
- PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that
the exception will be thrown.

---

#### protected void connect​(
InetAddress
address,
int port)
throws
SocketException

Connects a datagram socket to a remote destination. This associates the remote
address with the local socket so that datagrams may only be sent to this destination
and received from this destination. This may be overridden to call a native
system connect.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException.
Note, there is no guarantee that the exception will be thrown.

**Parameters:**
- address

- the remote InetAddress to connect to
- port

- the remote port number

**Throws:**
- SocketException

- may be thrown if the socket cannot be
connected to the remote destination

**Since:**
- 1.4

---

#### protected void disconnect()

Disconnects a datagram socket from its remote destination.

**Since:**
- 1.4

---

#### protected abstract int peek​(
InetAddress
i)
throws
IOException

Peek at the packet to see who it is from. Updates the specified

InetAddress

to the address which the packet came from.

**Parameters:**
- i

- an InetAddress object

**Returns:**
- the port number which the packet came from.

**Throws:**
- IOException

- if an I/O exception occurs
- PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

---

#### protected abstract int peekData​(
DatagramPacket
p)
throws
IOException

Peek at the packet to see who it is from. The data is copied into the specified

DatagramPacket

. The data is returned,
but not consumed, so that a subsequent peekData/receive operation
will see the same data.

**Parameters:**
- p

- the Packet Received.

**Returns:**
- the port number which the packet came from.

**Throws:**
- IOException

- if an I/O exception occurs
- PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

**Since:**
- 1.4

---

#### protected abstract void receive​(
DatagramPacket
p)
throws
IOException

Receive the datagram packet.

**Parameters:**
- p

- the Packet Received.

**Throws:**
- IOException

- if an I/O exception occurs
while receiving the datagram packet.
- PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

---

#### @Deprecated

protected abstract void setTTL​(byte ttl)
throws
IOException

Set the TTL (time-to-live) option.

**Parameters:**
- ttl

- a byte specifying the TTL value

**Throws:**
- IOException

- if an I/O exception occurs while setting
the time-to-live option.

**See Also:**
- getTTL()

---

#### @Deprecated

protected abstract byte getTTL()
throws
IOException

Retrieve the TTL (time-to-live) option.

**Returns:**
- a byte representing the TTL value

**Throws:**
- IOException

- if an I/O exception occurs
while retrieving the time-to-live option

**See Also:**
- setTTL(byte)

---

#### protected abstract void setTimeToLive​(int ttl)
throws
IOException

Set the TTL (time-to-live) option.

**Parameters:**
- ttl

- an

int

specifying the time-to-live value

**Throws:**
- IOException

- if an I/O exception occurs
while setting the time-to-live option.

**See Also:**
- getTimeToLive()

---

#### protected abstract int getTimeToLive()
throws
IOException

Retrieve the TTL (time-to-live) option.

**Returns:**
- an

int

representing the time-to-live value

**Throws:**
- IOException

- if an I/O exception occurs
while retrieving the time-to-live option

**See Also:**
- setTimeToLive(int)

---

#### protected abstract void join​(
InetAddress
inetaddr)
throws
IOException

Join the multicast group.

**Parameters:**
- inetaddr

- multicast address to join.

**Throws:**
- IOException

- if an I/O exception occurs
while joining the multicast group.

---

#### protected abstract void leave​(
InetAddress
inetaddr)
throws
IOException

Leave the multicast group.

**Parameters:**
- inetaddr

- multicast address to leave.

**Throws:**
- IOException

- if an I/O exception occurs
while leaving the multicast group.

---

#### protected abstract void joinGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException

Join the multicast group.

**Parameters:**
- mcastaddr

- address to join.
- netIf

- specifies the local interface to receive multicast
datagram packets

**Throws:**
- IOException

- if an I/O exception occurs while joining
the multicast group

**Since:**
- 1.4

---

#### protected abstract void leaveGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException

Leave the multicast group.

**Parameters:**
- mcastaddr

- address to leave.
- netIf

- specified the local interface to leave the group at

**Throws:**
- IOException

- if an I/O exception occurs while leaving
the multicast group

**Since:**
- 1.4

---

#### protected abstract void close()

Close the socket.

---

#### protected int getLocalPort()

Gets the local port.

**Returns:**
- an

int

representing the local port value

---

#### protected
FileDescriptor
getFileDescriptor()

Gets the datagram socket file descriptor.

**Returns:**
- a

FileDescriptor

object representing the datagram socket
file descriptor

---

#### protected <T> void setOption​(
SocketOption
<T> name,
T value)
throws
IOException

Called to set a socket option.

**Parameters:**
- name

- The socket option
- value

- The value of the socket option. A value of

null

may be valid for some options.

**Throws:**
- UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
- NullPointerException

- if name is

null
- IOException

- if an I/O problem occurs while attempting to set the option

**Since:**
- 9

**Type Parameters:**
- T

- The type of the socket option value

---

#### protected <T> T getOption​(
SocketOption
<T> name)
throws
IOException

Called to get a socket option.

**Parameters:**
- name

- The socket option

**Returns:**
- the socket option

**Throws:**
- UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
- NullPointerException

- if name is

null
- IOException

- if an I/O problem occurs while attempting to set the option

**Since:**
- 9

**Type Parameters:**
- T

- The type of the socket option value

---

#### protected
Set
<
SocketOption
<?>> supportedOptions()

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

**Returns:**
- a Set of SocketOptions

**Since:**
- 9

---

### Additional Sections

#### Class DatagramSocketImpl

java.lang.Object

- java.net.DatagramSocketImpl

java.net.DatagramSocketImpl

**All Implemented Interfaces:** SocketOptions

```java
public abstract class
DatagramSocketImpl

extends
Object

implements
SocketOptions
```

Abstract datagram and multicast socket implementation base class.

**Since:** 1.1

public abstract class

DatagramSocketImpl

extends

Object

implements

SocketOptions

Abstract datagram and multicast socket implementation base class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

FileDescriptor

fd

The file descriptor object.

protected int

localPort

The local port number.

- Fields declared in interface java.net.

SocketOptions

IP_MULTICAST_IF

,

IP_MULTICAST_IF2

,

IP_MULTICAST_LOOP

,

IP_TOS

,

SO_BINDADDR

,

SO_BROADCAST

,

SO_KEEPALIVE

,

SO_LINGER

,

SO_OOBINLINE

,

SO_RCVBUF

,

SO_REUSEADDR

,

SO_REUSEPORT

,

SO_SNDBUF

,

SO_TIMEOUT

,

TCP_NODELAY

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DatagramSocketImpl

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected abstract void

bind

​(int lport,

InetAddress

laddr)

Binds a datagram socket to a local port and address.

protected abstract void

close

()

Close the socket.

protected void

connect

​(

InetAddress

address,
int port)

Connects a datagram socket to a remote destination.

protected abstract void

create

()

Creates a datagram socket.

protected void

disconnect

()

Disconnects a datagram socket from its remote destination.

protected

FileDescriptor

getFileDescriptor

()

Gets the datagram socket file descriptor.

protected int

getLocalPort

()

Gets the local port.

protected <T> T

getOption

​(

SocketOption

<T> name)

Called to get a socket option.

protected abstract int

getTimeToLive

()

Retrieve the TTL (time-to-live) option.

protected abstract byte

getTTL

()

Deprecated.

use getTimeToLive instead.

protected abstract void

join

​(

InetAddress

inetaddr)

Join the multicast group.

protected abstract void

joinGroup

​(

SocketAddress

mcastaddr,

NetworkInterface

netIf)

Join the multicast group.

protected abstract void

leave

​(

InetAddress

inetaddr)

Leave the multicast group.

protected abstract void

leaveGroup

​(

SocketAddress

mcastaddr,

NetworkInterface

netIf)

Leave the multicast group.

protected abstract int

peek

​(

InetAddress

i)

Peek at the packet to see who it is from.

protected abstract int

peekData

​(

DatagramPacket

p)

Peek at the packet to see who it is from.

protected abstract void

receive

​(

DatagramPacket

p)

Receive the datagram packet.

protected abstract void

send

​(

DatagramPacket

p)

Sends a datagram packet.

protected <T> void

setOption

​(

SocketOption

<T> name,
T value)

Called to set a socket option.

protected abstract void

setTimeToLive

​(int ttl)

Set the TTL (time-to-live) option.

protected abstract void

setTTL

​(byte ttl)

Deprecated.

use setTimeToLive instead.

protected

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

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

- Methods declared in interface java.net.

SocketOptions

getOption

,

setOption

Field Summary

Fields

Modifier and Type

Field

Description

protected

FileDescriptor

fd

The file descriptor object.

protected int

localPort

The local port number.

- Fields declared in interface java.net.

SocketOptions

IP_MULTICAST_IF

,

IP_MULTICAST_IF2

,

IP_MULTICAST_LOOP

,

IP_TOS

,

SO_BINDADDR

,

SO_BROADCAST

,

SO_KEEPALIVE

,

SO_LINGER

,

SO_OOBINLINE

,

SO_RCVBUF

,

SO_REUSEADDR

,

SO_REUSEPORT

,

SO_SNDBUF

,

SO_TIMEOUT

,

TCP_NODELAY

---

#### Field Summary

The file descriptor object.

The local port number.

Fields declared in interface java.net.

SocketOptions

IP_MULTICAST_IF

,

IP_MULTICAST_IF2

,

IP_MULTICAST_LOOP

,

IP_TOS

,

SO_BINDADDR

,

SO_BROADCAST

,

SO_KEEPALIVE

,

SO_LINGER

,

SO_OOBINLINE

,

SO_RCVBUF

,

SO_REUSEADDR

,

SO_REUSEPORT

,

SO_SNDBUF

,

SO_TIMEOUT

,

TCP_NODELAY

---

#### Fields declared in interface java.net. SocketOptions

Constructor Summary

Constructors

Constructor

Description

DatagramSocketImpl

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected abstract void

bind

​(int lport,

InetAddress

laddr)

Binds a datagram socket to a local port and address.

protected abstract void

close

()

Close the socket.

protected void

connect

​(

InetAddress

address,
int port)

Connects a datagram socket to a remote destination.

protected abstract void

create

()

Creates a datagram socket.

protected void

disconnect

()

Disconnects a datagram socket from its remote destination.

protected

FileDescriptor

getFileDescriptor

()

Gets the datagram socket file descriptor.

protected int

getLocalPort

()

Gets the local port.

protected <T> T

getOption

​(

SocketOption

<T> name)

Called to get a socket option.

protected abstract int

getTimeToLive

()

Retrieve the TTL (time-to-live) option.

protected abstract byte

getTTL

()

Deprecated.

use getTimeToLive instead.

protected abstract void

join

​(

InetAddress

inetaddr)

Join the multicast group.

protected abstract void

joinGroup

​(

SocketAddress

mcastaddr,

NetworkInterface

netIf)

Join the multicast group.

protected abstract void

leave

​(

InetAddress

inetaddr)

Leave the multicast group.

protected abstract void

leaveGroup

​(

SocketAddress

mcastaddr,

NetworkInterface

netIf)

Leave the multicast group.

protected abstract int

peek

​(

InetAddress

i)

Peek at the packet to see who it is from.

protected abstract int

peekData

​(

DatagramPacket

p)

Peek at the packet to see who it is from.

protected abstract void

receive

​(

DatagramPacket

p)

Receive the datagram packet.

protected abstract void

send

​(

DatagramPacket

p)

Sends a datagram packet.

protected <T> void

setOption

​(

SocketOption

<T> name,
T value)

Called to set a socket option.

protected abstract void

setTimeToLive

​(int ttl)

Set the TTL (time-to-live) option.

protected abstract void

setTTL

​(byte ttl)

Deprecated.

use setTimeToLive instead.

protected

Set

<

SocketOption

<?>>

supportedOptions

()

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

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

- Methods declared in interface java.net.

SocketOptions

getOption

,

setOption

---

#### Method Summary

Binds a datagram socket to a local port and address.

Close the socket.

Connects a datagram socket to a remote destination.

Creates a datagram socket.

Disconnects a datagram socket from its remote destination.

Gets the datagram socket file descriptor.

Gets the local port.

Called to get a socket option.

Retrieve the TTL (time-to-live) option.

Deprecated.

use getTimeToLive instead.

Join the multicast group.

Leave the multicast group.

Peek at the packet to see who it is from.

Receive the datagram packet.

Sends a datagram packet.

Called to set a socket option.

Set the TTL (time-to-live) option.

Deprecated.

use setTimeToLive instead.

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

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

Methods declared in interface java.net.

SocketOptions

getOption

,

setOption

---

#### Methods declared in interface java.net. SocketOptions

============ FIELD DETAIL ===========

- Field Detail

- localPort

```java
protected int localPort
```

The local port number.

- fd

```java
protected
FileDescriptor
fd
```

The file descriptor object.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DatagramSocketImpl

```java
public DatagramSocketImpl()
```

============ METHOD DETAIL ==========

- Method Detail

- create

```java
protected abstract void create()
throws
SocketException
```

Creates a datagram socket.

**Throws:** SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

- bind

```java
protected abstract void bind​(int lport,

InetAddress
laddr)
throws
SocketException
```

Binds a datagram socket to a local port and address.

**Parameters:** lport

- the local port
**Parameters:** laddr

- the local address
**Throws:** SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

- send

```java
protected abstract void send​(
DatagramPacket
p)
throws
IOException
```

Sends a datagram packet. The packet contains the data and the
destination address to send the packet to.

**Parameters:** p

- the packet to be sent.
**Throws:** IOException

- if an I/O exception occurs while sending the
datagram packet.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that
the exception will be thrown.

- connect

```java
protected void connect​(
InetAddress
address,
int port)
throws
SocketException
```

Connects a datagram socket to a remote destination. This associates the remote
address with the local socket so that datagrams may only be sent to this destination
and received from this destination. This may be overridden to call a native
system connect.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException.
Note, there is no guarantee that the exception will be thrown.

**Parameters:** address

- the remote InetAddress to connect to
**Parameters:** port

- the remote port number
**Throws:** SocketException

- may be thrown if the socket cannot be
connected to the remote destination
**Since:** 1.4

- disconnect

```java
protected void disconnect()
```

Disconnects a datagram socket from its remote destination.

**Since:** 1.4

- peek

```java
protected abstract int peek​(
InetAddress
i)
throws
IOException
```

Peek at the packet to see who it is from. Updates the specified

InetAddress

to the address which the packet came from.

**Parameters:** i

- an InetAddress object
**Returns:** the port number which the packet came from.
**Throws:** IOException

- if an I/O exception occurs
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

- peekData

```java
protected abstract int peekData​(
DatagramPacket
p)
throws
IOException
```

Peek at the packet to see who it is from. The data is copied into the specified

DatagramPacket

. The data is returned,
but not consumed, so that a subsequent peekData/receive operation
will see the same data.

**Parameters:** p

- the Packet Received.
**Returns:** the port number which the packet came from.
**Throws:** IOException

- if an I/O exception occurs
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.
**Since:** 1.4

- receive

```java
protected abstract void receive​(
DatagramPacket
p)
throws
IOException
```

Receive the datagram packet.

**Parameters:** p

- the Packet Received.
**Throws:** IOException

- if an I/O exception occurs
while receiving the datagram packet.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

- setTTL

```java
@Deprecated

protected abstract void setTTL​(byte ttl)
throws
IOException
```

Deprecated.

use setTimeToLive instead.

Set the TTL (time-to-live) option.

**Parameters:** ttl

- a byte specifying the TTL value
**Throws:** IOException

- if an I/O exception occurs while setting
the time-to-live option.
**See Also:** getTTL()

- getTTL

```java
@Deprecated

protected abstract byte getTTL()
throws
IOException
```

Deprecated.

use getTimeToLive instead.

Retrieve the TTL (time-to-live) option.

**Returns:** a byte representing the TTL value
**Throws:** IOException

- if an I/O exception occurs
while retrieving the time-to-live option
**See Also:** setTTL(byte)

- setTimeToLive

```java
protected abstract void setTimeToLive​(int ttl)
throws
IOException
```

Set the TTL (time-to-live) option.

**Parameters:** ttl

- an

int

specifying the time-to-live value
**Throws:** IOException

- if an I/O exception occurs
while setting the time-to-live option.
**See Also:** getTimeToLive()

- getTimeToLive

```java
protected abstract int getTimeToLive()
throws
IOException
```

Retrieve the TTL (time-to-live) option.

**Returns:** an

int

representing the time-to-live value
**Throws:** IOException

- if an I/O exception occurs
while retrieving the time-to-live option
**See Also:** setTimeToLive(int)

- join

```java
protected abstract void join​(
InetAddress
inetaddr)
throws
IOException
```

Join the multicast group.

**Parameters:** inetaddr

- multicast address to join.
**Throws:** IOException

- if an I/O exception occurs
while joining the multicast group.

- leave

```java
protected abstract void leave​(
InetAddress
inetaddr)
throws
IOException
```

Leave the multicast group.

**Parameters:** inetaddr

- multicast address to leave.
**Throws:** IOException

- if an I/O exception occurs
while leaving the multicast group.

- joinGroup

```java
protected abstract void joinGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException
```

Join the multicast group.

**Parameters:** mcastaddr

- address to join.
**Parameters:** netIf

- specifies the local interface to receive multicast
datagram packets
**Throws:** IOException

- if an I/O exception occurs while joining
the multicast group
**Since:** 1.4

- leaveGroup

```java
protected abstract void leaveGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException
```

Leave the multicast group.

**Parameters:** mcastaddr

- address to leave.
**Parameters:** netIf

- specified the local interface to leave the group at
**Throws:** IOException

- if an I/O exception occurs while leaving
the multicast group
**Since:** 1.4

- close

```java
protected abstract void close()
```

Close the socket.

- getLocalPort

```java
protected int getLocalPort()
```

Gets the local port.

**Returns:** an

int

representing the local port value

- getFileDescriptor

```java
protected
FileDescriptor
getFileDescriptor()
```

Gets the datagram socket file descriptor.

**Returns:** a

FileDescriptor

object representing the datagram socket
file descriptor

- setOption

```java
protected <T> void setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Called to set a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be valid for some options.
**Throws:** UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
**Throws:** NullPointerException

- if name is

null
**Throws:** IOException

- if an I/O problem occurs while attempting to set the option
**Since:** 9

- getOption

```java
protected <T> T getOption​(
SocketOption
<T> name)
throws
IOException
```

Called to get a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Returns:** the socket option
**Throws:** UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
**Throws:** NullPointerException

- if name is

null
**Throws:** IOException

- if an I/O problem occurs while attempting to set the option
**Since:** 9

- supportedOptions

```java
protected
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

**Returns:** a Set of SocketOptions
**Since:** 9

Field Detail

- localPort

```java
protected int localPort
```

The local port number.

- fd

```java
protected
FileDescriptor
fd
```

The file descriptor object.

---

#### Field Detail

localPort

```java
protected int localPort
```

The local port number.

---

#### localPort

protected int localPort

The local port number.

fd

```java
protected
FileDescriptor
fd
```

The file descriptor object.

---

#### fd

protected

FileDescriptor

fd

The file descriptor object.

Constructor Detail

- DatagramSocketImpl

```java
public DatagramSocketImpl()
```

---

#### Constructor Detail

DatagramSocketImpl

```java
public DatagramSocketImpl()
```

---

#### DatagramSocketImpl

public DatagramSocketImpl()

Method Detail

- create

```java
protected abstract void create()
throws
SocketException
```

Creates a datagram socket.

**Throws:** SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

- bind

```java
protected abstract void bind​(int lport,

InetAddress
laddr)
throws
SocketException
```

Binds a datagram socket to a local port and address.

**Parameters:** lport

- the local port
**Parameters:** laddr

- the local address
**Throws:** SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

- send

```java
protected abstract void send​(
DatagramPacket
p)
throws
IOException
```

Sends a datagram packet. The packet contains the data and the
destination address to send the packet to.

**Parameters:** p

- the packet to be sent.
**Throws:** IOException

- if an I/O exception occurs while sending the
datagram packet.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that
the exception will be thrown.

- connect

```java
protected void connect​(
InetAddress
address,
int port)
throws
SocketException
```

Connects a datagram socket to a remote destination. This associates the remote
address with the local socket so that datagrams may only be sent to this destination
and received from this destination. This may be overridden to call a native
system connect.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException.
Note, there is no guarantee that the exception will be thrown.

**Parameters:** address

- the remote InetAddress to connect to
**Parameters:** port

- the remote port number
**Throws:** SocketException

- may be thrown if the socket cannot be
connected to the remote destination
**Since:** 1.4

- disconnect

```java
protected void disconnect()
```

Disconnects a datagram socket from its remote destination.

**Since:** 1.4

- peek

```java
protected abstract int peek​(
InetAddress
i)
throws
IOException
```

Peek at the packet to see who it is from. Updates the specified

InetAddress

to the address which the packet came from.

**Parameters:** i

- an InetAddress object
**Returns:** the port number which the packet came from.
**Throws:** IOException

- if an I/O exception occurs
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

- peekData

```java
protected abstract int peekData​(
DatagramPacket
p)
throws
IOException
```

Peek at the packet to see who it is from. The data is copied into the specified

DatagramPacket

. The data is returned,
but not consumed, so that a subsequent peekData/receive operation
will see the same data.

**Parameters:** p

- the Packet Received.
**Returns:** the port number which the packet came from.
**Throws:** IOException

- if an I/O exception occurs
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.
**Since:** 1.4

- receive

```java
protected abstract void receive​(
DatagramPacket
p)
throws
IOException
```

Receive the datagram packet.

**Parameters:** p

- the Packet Received.
**Throws:** IOException

- if an I/O exception occurs
while receiving the datagram packet.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

- setTTL

```java
@Deprecated

protected abstract void setTTL​(byte ttl)
throws
IOException
```

Deprecated.

use setTimeToLive instead.

Set the TTL (time-to-live) option.

**Parameters:** ttl

- a byte specifying the TTL value
**Throws:** IOException

- if an I/O exception occurs while setting
the time-to-live option.
**See Also:** getTTL()

- getTTL

```java
@Deprecated

protected abstract byte getTTL()
throws
IOException
```

Deprecated.

use getTimeToLive instead.

Retrieve the TTL (time-to-live) option.

**Returns:** a byte representing the TTL value
**Throws:** IOException

- if an I/O exception occurs
while retrieving the time-to-live option
**See Also:** setTTL(byte)

- setTimeToLive

```java
protected abstract void setTimeToLive​(int ttl)
throws
IOException
```

Set the TTL (time-to-live) option.

**Parameters:** ttl

- an

int

specifying the time-to-live value
**Throws:** IOException

- if an I/O exception occurs
while setting the time-to-live option.
**See Also:** getTimeToLive()

- getTimeToLive

```java
protected abstract int getTimeToLive()
throws
IOException
```

Retrieve the TTL (time-to-live) option.

**Returns:** an

int

representing the time-to-live value
**Throws:** IOException

- if an I/O exception occurs
while retrieving the time-to-live option
**See Also:** setTimeToLive(int)

- join

```java
protected abstract void join​(
InetAddress
inetaddr)
throws
IOException
```

Join the multicast group.

**Parameters:** inetaddr

- multicast address to join.
**Throws:** IOException

- if an I/O exception occurs
while joining the multicast group.

- leave

```java
protected abstract void leave​(
InetAddress
inetaddr)
throws
IOException
```

Leave the multicast group.

**Parameters:** inetaddr

- multicast address to leave.
**Throws:** IOException

- if an I/O exception occurs
while leaving the multicast group.

- joinGroup

```java
protected abstract void joinGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException
```

Join the multicast group.

**Parameters:** mcastaddr

- address to join.
**Parameters:** netIf

- specifies the local interface to receive multicast
datagram packets
**Throws:** IOException

- if an I/O exception occurs while joining
the multicast group
**Since:** 1.4

- leaveGroup

```java
protected abstract void leaveGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException
```

Leave the multicast group.

**Parameters:** mcastaddr

- address to leave.
**Parameters:** netIf

- specified the local interface to leave the group at
**Throws:** IOException

- if an I/O exception occurs while leaving
the multicast group
**Since:** 1.4

- close

```java
protected abstract void close()
```

Close the socket.

- getLocalPort

```java
protected int getLocalPort()
```

Gets the local port.

**Returns:** an

int

representing the local port value

- getFileDescriptor

```java
protected
FileDescriptor
getFileDescriptor()
```

Gets the datagram socket file descriptor.

**Returns:** a

FileDescriptor

object representing the datagram socket
file descriptor

- setOption

```java
protected <T> void setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Called to set a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be valid for some options.
**Throws:** UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
**Throws:** NullPointerException

- if name is

null
**Throws:** IOException

- if an I/O problem occurs while attempting to set the option
**Since:** 9

- getOption

```java
protected <T> T getOption​(
SocketOption
<T> name)
throws
IOException
```

Called to get a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Returns:** the socket option
**Throws:** UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
**Throws:** NullPointerException

- if name is

null
**Throws:** IOException

- if an I/O problem occurs while attempting to set the option
**Since:** 9

- supportedOptions

```java
protected
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

**Returns:** a Set of SocketOptions
**Since:** 9

---

#### Method Detail

create

```java
protected abstract void create()
throws
SocketException
```

Creates a datagram socket.

**Throws:** SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

---

#### create

protected abstract void create()
throws

SocketException

Creates a datagram socket.

bind

```java
protected abstract void bind​(int lport,

InetAddress
laddr)
throws
SocketException
```

Binds a datagram socket to a local port and address.

**Parameters:** lport

- the local port
**Parameters:** laddr

- the local address
**Throws:** SocketException

- if there is an error in the
underlying protocol, such as a TCP error.

---

#### bind

protected abstract void bind​(int lport,

InetAddress

laddr)
throws

SocketException

Binds a datagram socket to a local port and address.

send

```java
protected abstract void send​(
DatagramPacket
p)
throws
IOException
```

Sends a datagram packet. The packet contains the data and the
destination address to send the packet to.

**Parameters:** p

- the packet to be sent.
**Throws:** IOException

- if an I/O exception occurs while sending the
datagram packet.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that
the exception will be thrown.

---

#### send

protected abstract void send​(

DatagramPacket

p)
throws

IOException

Sends a datagram packet. The packet contains the data and the
destination address to send the packet to.

connect

```java
protected void connect​(
InetAddress
address,
int port)
throws
SocketException
```

Connects a datagram socket to a remote destination. This associates the remote
address with the local socket so that datagrams may only be sent to this destination
and received from this destination. This may be overridden to call a native
system connect.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException.
Note, there is no guarantee that the exception will be thrown.

**Parameters:** address

- the remote InetAddress to connect to
**Parameters:** port

- the remote port number
**Throws:** SocketException

- may be thrown if the socket cannot be
connected to the remote destination
**Since:** 1.4

---

#### connect

protected void connect​(

InetAddress

address,
int port)
throws

SocketException

Connects a datagram socket to a remote destination. This associates the remote
address with the local socket so that datagrams may only be sent to this destination
and received from this destination. This may be overridden to call a native
system connect.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException.
Note, there is no guarantee that the exception will be thrown.

If the remote destination to which the socket is connected does not
exist, or is otherwise unreachable, and if an ICMP destination unreachable
packet has been received for that address, then a subsequent call to
send or receive may throw a PortUnreachableException.
Note, there is no guarantee that the exception will be thrown.

disconnect

```java
protected void disconnect()
```

Disconnects a datagram socket from its remote destination.

**Since:** 1.4

---

#### disconnect

protected void disconnect()

Disconnects a datagram socket from its remote destination.

peek

```java
protected abstract int peek​(
InetAddress
i)
throws
IOException
```

Peek at the packet to see who it is from. Updates the specified

InetAddress

to the address which the packet came from.

**Parameters:** i

- an InetAddress object
**Returns:** the port number which the packet came from.
**Throws:** IOException

- if an I/O exception occurs
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

---

#### peek

protected abstract int peek​(

InetAddress

i)
throws

IOException

Peek at the packet to see who it is from. Updates the specified

InetAddress

to the address which the packet came from.

peekData

```java
protected abstract int peekData​(
DatagramPacket
p)
throws
IOException
```

Peek at the packet to see who it is from. The data is copied into the specified

DatagramPacket

. The data is returned,
but not consumed, so that a subsequent peekData/receive operation
will see the same data.

**Parameters:** p

- the Packet Received.
**Returns:** the port number which the packet came from.
**Throws:** IOException

- if an I/O exception occurs
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.
**Since:** 1.4

---

#### peekData

protected abstract int peekData​(

DatagramPacket

p)
throws

IOException

Peek at the packet to see who it is from. The data is copied into the specified

DatagramPacket

. The data is returned,
but not consumed, so that a subsequent peekData/receive operation
will see the same data.

receive

```java
protected abstract void receive​(
DatagramPacket
p)
throws
IOException
```

Receive the datagram packet.

**Parameters:** p

- the Packet Received.
**Throws:** IOException

- if an I/O exception occurs
while receiving the datagram packet.
**Throws:** PortUnreachableException

- may be thrown if the socket is connected
to a currently unreachable destination. Note, there is no guarantee that the
exception will be thrown.

---

#### receive

protected abstract void receive​(

DatagramPacket

p)
throws

IOException

Receive the datagram packet.

setTTL

```java
@Deprecated

protected abstract void setTTL​(byte ttl)
throws
IOException
```

Deprecated.

use setTimeToLive instead.

Set the TTL (time-to-live) option.

**Parameters:** ttl

- a byte specifying the TTL value
**Throws:** IOException

- if an I/O exception occurs while setting
the time-to-live option.
**See Also:** getTTL()

---

#### setTTL

@Deprecated

protected abstract void setTTL​(byte ttl)
throws

IOException

Set the TTL (time-to-live) option.

getTTL

```java
@Deprecated

protected abstract byte getTTL()
throws
IOException
```

Deprecated.

use getTimeToLive instead.

Retrieve the TTL (time-to-live) option.

**Returns:** a byte representing the TTL value
**Throws:** IOException

- if an I/O exception occurs
while retrieving the time-to-live option
**See Also:** setTTL(byte)

---

#### getTTL

@Deprecated

protected abstract byte getTTL()
throws

IOException

Retrieve the TTL (time-to-live) option.

setTimeToLive

```java
protected abstract void setTimeToLive​(int ttl)
throws
IOException
```

Set the TTL (time-to-live) option.

**Parameters:** ttl

- an

int

specifying the time-to-live value
**Throws:** IOException

- if an I/O exception occurs
while setting the time-to-live option.
**See Also:** getTimeToLive()

---

#### setTimeToLive

protected abstract void setTimeToLive​(int ttl)
throws

IOException

Set the TTL (time-to-live) option.

getTimeToLive

```java
protected abstract int getTimeToLive()
throws
IOException
```

Retrieve the TTL (time-to-live) option.

**Returns:** an

int

representing the time-to-live value
**Throws:** IOException

- if an I/O exception occurs
while retrieving the time-to-live option
**See Also:** setTimeToLive(int)

---

#### getTimeToLive

protected abstract int getTimeToLive()
throws

IOException

Retrieve the TTL (time-to-live) option.

join

```java
protected abstract void join​(
InetAddress
inetaddr)
throws
IOException
```

Join the multicast group.

**Parameters:** inetaddr

- multicast address to join.
**Throws:** IOException

- if an I/O exception occurs
while joining the multicast group.

---

#### join

protected abstract void join​(

InetAddress

inetaddr)
throws

IOException

Join the multicast group.

leave

```java
protected abstract void leave​(
InetAddress
inetaddr)
throws
IOException
```

Leave the multicast group.

**Parameters:** inetaddr

- multicast address to leave.
**Throws:** IOException

- if an I/O exception occurs
while leaving the multicast group.

---

#### leave

protected abstract void leave​(

InetAddress

inetaddr)
throws

IOException

Leave the multicast group.

joinGroup

```java
protected abstract void joinGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException
```

Join the multicast group.

**Parameters:** mcastaddr

- address to join.
**Parameters:** netIf

- specifies the local interface to receive multicast
datagram packets
**Throws:** IOException

- if an I/O exception occurs while joining
the multicast group
**Since:** 1.4

---

#### joinGroup

protected abstract void joinGroup​(

SocketAddress

mcastaddr,

NetworkInterface

netIf)
throws

IOException

Join the multicast group.

leaveGroup

```java
protected abstract void leaveGroup​(
SocketAddress
mcastaddr,

NetworkInterface
netIf)
throws
IOException
```

Leave the multicast group.

**Parameters:** mcastaddr

- address to leave.
**Parameters:** netIf

- specified the local interface to leave the group at
**Throws:** IOException

- if an I/O exception occurs while leaving
the multicast group
**Since:** 1.4

---

#### leaveGroup

protected abstract void leaveGroup​(

SocketAddress

mcastaddr,

NetworkInterface

netIf)
throws

IOException

Leave the multicast group.

close

```java
protected abstract void close()
```

Close the socket.

---

#### close

protected abstract void close()

Close the socket.

getLocalPort

```java
protected int getLocalPort()
```

Gets the local port.

**Returns:** an

int

representing the local port value

---

#### getLocalPort

protected int getLocalPort()

Gets the local port.

getFileDescriptor

```java
protected
FileDescriptor
getFileDescriptor()
```

Gets the datagram socket file descriptor.

**Returns:** a

FileDescriptor

object representing the datagram socket
file descriptor

---

#### getFileDescriptor

protected

FileDescriptor

getFileDescriptor()

Gets the datagram socket file descriptor.

setOption

```java
protected <T> void setOption​(
SocketOption
<T> name,
T value)
throws
IOException
```

Called to set a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. A value of

null

may be valid for some options.
**Throws:** UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
**Throws:** NullPointerException

- if name is

null
**Throws:** IOException

- if an I/O problem occurs while attempting to set the option
**Since:** 9

---

#### setOption

protected <T> void setOption​(

SocketOption

<T> name,
T value)
throws

IOException

Called to set a socket option.

getOption

```java
protected <T> T getOption​(
SocketOption
<T> name)
throws
IOException
```

Called to get a socket option.

**Type Parameters:** T

- The type of the socket option value
**Parameters:** name

- The socket option
**Returns:** the socket option
**Throws:** UnsupportedOperationException

- if the DatagramSocketImpl does not
support the option
**Throws:** NullPointerException

- if name is

null
**Throws:** IOException

- if an I/O problem occurs while attempting to set the option
**Since:** 9

---

#### getOption

protected <T> T getOption​(

SocketOption

<T> name)
throws

IOException

Called to get a socket option.

supportedOptions

```java
protected
Set
<
SocketOption
<?>> supportedOptions()
```

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

**Returns:** a Set of SocketOptions
**Since:** 9

---

#### supportedOptions

protected

Set

<

SocketOption

<?>> supportedOptions()

Returns a set of SocketOptions supported by this impl
and by this impl's socket (DatagramSocket or MulticastSocket)

---

