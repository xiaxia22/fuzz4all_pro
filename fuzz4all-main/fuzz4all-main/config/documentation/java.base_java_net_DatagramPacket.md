# Class DatagramPacket

**Source:** `java.base\java\net\DatagramPacket.html`

### Class Description

```java
public final class
DatagramPacket

extends
Object
```

This class represents a datagram packet.

Datagram packets are used to implement a connectionless packet
delivery service. Each message is routed from one machine to
another based solely on information contained within that packet.
Multiple packets sent from one machine to another might be routed
differently, and might arrive in any order. Packet delivery is
not guaranteed.

**Since:** 1.0

---

### Field Details

*No entries found.*

### Constructor Details

#### public DatagramPacket​(byte[] buf,
int offset,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:**
- buf

- buffer for holding the incoming datagram.
- offset

- the offset for the buffer
- length

- the number of bytes to read.

**Since:**
- 1.2

---

#### public DatagramPacket​(byte[] buf,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:**
- buf

- buffer for holding the incoming datagram.
- length

- the number of bytes to read.

---

#### public DatagramPacket​(byte[] buf,
int offset,
int length,

InetAddress
address,
int port)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:**
- buf

- the packet data.
- offset

- the packet data offset.
- length

- the packet data length.
- address

- the destination address.
- port

- the destination port number.

**See Also:**
- InetAddress

**Since:**
- 1.2

---

#### public DatagramPacket​(byte[] buf,
int offset,
int length,

SocketAddress
address)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:**
- buf

- the packet data.
- offset

- the packet data offset.
- length

- the packet data length.
- address

- the destination socket address.

**Throws:**
- IllegalArgumentException

- if address type is not supported

**See Also:**
- InetAddress

**Since:**
- 1.4

---

#### public DatagramPacket​(byte[] buf,
int length,

InetAddress
address,
int port)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:**
- buf

- the packet data.
- length

- the packet length.
- address

- the destination address.
- port

- the destination port number.

**See Also:**
- InetAddress

---

#### public DatagramPacket​(byte[] buf,
int length,

SocketAddress
address)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:**
- buf

- the packet data.
- length

- the packet length.
- address

- the destination address.

**Throws:**
- IllegalArgumentException

- if address type is not supported

**See Also:**
- InetAddress

**Since:**
- 1.4

---

### Method Details

#### public
InetAddress
getAddress()

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

**Returns:**
- the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

**See Also:**
- InetAddress

,

setAddress(java.net.InetAddress)

---

#### public int getPort()

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

**Returns:**
- the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

**See Also:**
- setPort(int)

---

#### public byte[] getData()

Returns the data buffer. The data received or the data to be sent
starts from the

offset

in the buffer,
and runs for

length

long.

**Returns:**
- the buffer used to receive or send data

**See Also:**
- setData(byte[], int, int)

---

#### public int getOffset()

Returns the offset of the data to be sent or the offset of the
data received.

**Returns:**
- the offset of the data to be sent or the offset of the
data received.

**Since:**
- 1.2

---

#### public int getLength()

Returns the length of the data to be sent or the length of the
data received.

**Returns:**
- the length of the data to be sent or the length of the
data received.

**See Also:**
- setLength(int)

---

#### public void setData​(byte[] buf,
int offset,
int length)

Set the data buffer for this packet. This sets the
data, length and offset of the packet.

**Parameters:**
- buf

- the buffer to set for this packet
- offset

- the offset into the data
- length

- the length of the data
and/or the length of the buffer used to receive data

**Throws:**
- NullPointerException

- if the argument is null

**See Also:**
- getData()

,

getOffset()

,

getLength()

**Since:**
- 1.2

---

#### public void setAddress​(
InetAddress
iaddr)

Sets the IP address of the machine to which this datagram
is being sent.

**Parameters:**
- iaddr

- the

InetAddress

**See Also:**
- getAddress()

**Since:**
- 1.1

---

#### public void setPort​(int iport)

Sets the port number on the remote host to which this datagram
is being sent.

**Parameters:**
- iport

- the port number

**See Also:**
- getPort()

**Since:**
- 1.1

---

#### public void setSocketAddress​(
SocketAddress
address)

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

**Parameters:**
- address

- the

SocketAddress

**Throws:**
- IllegalArgumentException

- if address is null or is a
SocketAddress subclass not supported by this socket

**See Also:**
- getSocketAddress()

**Since:**
- 1.4

---

#### public
SocketAddress
getSocketAddress()

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

**Returns:**
- the

SocketAddress

**See Also:**
- setSocketAddress(java.net.SocketAddress)

**Since:**
- 1.4

---

#### public void setData​(byte[] buf)

Set the data buffer for this packet. With the offset of
this DatagramPacket set to 0, and the length set to
the length of

buf

.

**Parameters:**
- buf

- the buffer to set for this packet.

**Throws:**
- NullPointerException

- if the argument is null.

**See Also:**
- getLength()

,

getData()

**Since:**
- 1.1

---

#### public void setLength​(int length)

Set the length for this packet. The length of the packet is
the number of bytes from the packet's data buffer that will be
sent, or the number of bytes of the packet's data buffer that
will be used for receiving data. The length must be lesser or
equal to the offset plus the length of the packet's buffer.

**Parameters:**
- length

- the length to set for this packet.

**Throws:**
- IllegalArgumentException

- if the length is negative
of if the length is greater than the packet's data buffer
length.

**See Also:**
- getLength()

,

setData(byte[], int, int)

**Since:**
- 1.1

---

### Additional Sections

#### Class DatagramPacket

java.lang.Object

- java.net.DatagramPacket

java.net.DatagramPacket

```java
public final class
DatagramPacket

extends
Object
```

This class represents a datagram packet.

Datagram packets are used to implement a connectionless packet
delivery service. Each message is routed from one machine to
another based solely on information contained within that packet.
Multiple packets sent from one machine to another might be routed
differently, and might arrive in any order. Packet delivery is
not guaranteed.

**Since:** 1.0

public final class

DatagramPacket

extends

Object

This class represents a datagram packet.

Datagram packets are used to implement a connectionless packet
delivery service. Each message is routed from one machine to
another based solely on information contained within that packet.
Multiple packets sent from one machine to another might be routed
differently, and might arrive in any order. Packet delivery is
not guaranteed.

Datagram packets are used to implement a connectionless packet
delivery service. Each message is routed from one machine to
another based solely on information contained within that packet.
Multiple packets sent from one machine to another might be routed
differently, and might arrive in any order. Packet delivery is
not guaranteed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DatagramPacket

​(byte[] buf,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

.

DatagramPacket

​(byte[] buf,
int offset,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

DatagramPacket

​(byte[] buf,
int offset,
int length,

InetAddress

address,
int port)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host.

DatagramPacket

​(byte[] buf,
int offset,
int length,

SocketAddress

address)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host.

DatagramPacket

​(byte[] buf,
int length,

InetAddress

address,
int port)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host.

DatagramPacket

​(byte[] buf,
int length,

SocketAddress

address)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InetAddress

getAddress

()

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

byte[]

getData

()

Returns the data buffer.

int

getLength

()

Returns the length of the data to be sent or the length of the
data received.

int

getOffset

()

Returns the offset of the data to be sent or the offset of the
data received.

int

getPort

()

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

SocketAddress

getSocketAddress

()

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

void

setAddress

​(

InetAddress

iaddr)

Sets the IP address of the machine to which this datagram
is being sent.

void

setData

​(byte[] buf)

Set the data buffer for this packet.

void

setData

​(byte[] buf,
int offset,
int length)

Set the data buffer for this packet.

void

setLength

​(int length)

Set the length for this packet.

void

setPort

​(int iport)

Sets the port number on the remote host to which this datagram
is being sent.

void

setSocketAddress

​(

SocketAddress

address)

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

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

Constructor

Description

DatagramPacket

​(byte[] buf,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

.

DatagramPacket

​(byte[] buf,
int offset,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

DatagramPacket

​(byte[] buf,
int offset,
int length,

InetAddress

address,
int port)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host.

DatagramPacket

​(byte[] buf,
int offset,
int length,

SocketAddress

address)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host.

DatagramPacket

​(byte[] buf,
int length,

InetAddress

address,
int port)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host.

DatagramPacket

​(byte[] buf,
int length,

SocketAddress

address)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host.

---

#### Constructor Summary

Constructs a

DatagramPacket

for receiving packets of
length

length

.

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host.

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InetAddress

getAddress

()

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

byte[]

getData

()

Returns the data buffer.

int

getLength

()

Returns the length of the data to be sent or the length of the
data received.

int

getOffset

()

Returns the offset of the data to be sent or the offset of the
data received.

int

getPort

()

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

SocketAddress

getSocketAddress

()

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

void

setAddress

​(

InetAddress

iaddr)

Sets the IP address of the machine to which this datagram
is being sent.

void

setData

​(byte[] buf)

Set the data buffer for this packet.

void

setData

​(byte[] buf,
int offset,
int length)

Set the data buffer for this packet.

void

setLength

​(int length)

Set the length for this packet.

void

setPort

​(int iport)

Sets the port number on the remote host to which this datagram
is being sent.

void

setSocketAddress

​(

SocketAddress

address)

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

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

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

Returns the data buffer.

Returns the length of the data to be sent or the length of the
data received.

Returns the offset of the data to be sent or the offset of the
data received.

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

Sets the IP address of the machine to which this datagram
is being sent.

Set the data buffer for this packet.

Set the length for this packet.

Sets the port number on the remote host to which this datagram
is being sent.

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

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

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length)
```

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- buffer for holding the incoming datagram.
**Parameters:** offset

- the offset for the buffer
**Parameters:** length

- the number of bytes to read.
**Since:** 1.2

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length)
```

Constructs a

DatagramPacket

for receiving packets of
length

length

.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- buffer for holding the incoming datagram.
**Parameters:** length

- the number of bytes to read.

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length,

InetAddress
address,
int port)
```

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** offset

- the packet data offset.
**Parameters:** length

- the packet data length.
**Parameters:** address

- the destination address.
**Parameters:** port

- the destination port number.
**Since:** 1.2
**See Also:** InetAddress

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length,

SocketAddress
address)
```

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** offset

- the packet data offset.
**Parameters:** length

- the packet data length.
**Parameters:** address

- the destination socket address.
**Throws:** IllegalArgumentException

- if address type is not supported
**Since:** 1.4
**See Also:** InetAddress

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length,

InetAddress
address,
int port)
```

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** length

- the packet length.
**Parameters:** address

- the destination address.
**Parameters:** port

- the destination port number.
**See Also:** InetAddress

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length,

SocketAddress
address)
```

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** length

- the packet length.
**Parameters:** address

- the destination address.
**Throws:** IllegalArgumentException

- if address type is not supported
**Since:** 1.4
**See Also:** InetAddress

============ METHOD DETAIL ==========

- Method Detail

- getAddress

```java
public
InetAddress
getAddress()
```

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

**Returns:** the IP address of the machine to which this datagram is being
sent or from which the datagram was received.
**See Also:** InetAddress

,

setAddress(java.net.InetAddress)

- getPort

```java
public int getPort()
```

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

**Returns:** the port number on the remote host to which this datagram is
being sent or from which the datagram was received.
**See Also:** setPort(int)

- getData

```java
public byte[] getData()
```

Returns the data buffer. The data received or the data to be sent
starts from the

offset

in the buffer,
and runs for

length

long.

**Returns:** the buffer used to receive or send data
**See Also:** setData(byte[], int, int)

- getOffset

```java
public int getOffset()
```

Returns the offset of the data to be sent or the offset of the
data received.

**Returns:** the offset of the data to be sent or the offset of the
data received.
**Since:** 1.2

- getLength

```java
public int getLength()
```

Returns the length of the data to be sent or the length of the
data received.

**Returns:** the length of the data to be sent or the length of the
data received.
**See Also:** setLength(int)

- setData

```java
public void setData​(byte[] buf,
int offset,
int length)
```

Set the data buffer for this packet. This sets the
data, length and offset of the packet.

**Parameters:** buf

- the buffer to set for this packet
**Parameters:** offset

- the offset into the data
**Parameters:** length

- the length of the data
and/or the length of the buffer used to receive data
**Throws:** NullPointerException

- if the argument is null
**Since:** 1.2
**See Also:** getData()

,

getOffset()

,

getLength()

- setAddress

```java
public void setAddress​(
InetAddress
iaddr)
```

Sets the IP address of the machine to which this datagram
is being sent.

**Parameters:** iaddr

- the

InetAddress
**Since:** 1.1
**See Also:** getAddress()

- setPort

```java
public void setPort​(int iport)
```

Sets the port number on the remote host to which this datagram
is being sent.

**Parameters:** iport

- the port number
**Since:** 1.1
**See Also:** getPort()

- setSocketAddress

```java
public void setSocketAddress​(
SocketAddress
address)
```

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

**Parameters:** address

- the

SocketAddress
**Throws:** IllegalArgumentException

- if address is null or is a
SocketAddress subclass not supported by this socket
**Since:** 1.4
**See Also:** getSocketAddress()

- getSocketAddress

```java
public
SocketAddress
getSocketAddress()
```

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

**Returns:** the

SocketAddress
**Since:** 1.4
**See Also:** setSocketAddress(java.net.SocketAddress)

- setData

```java
public void setData​(byte[] buf)
```

Set the data buffer for this packet. With the offset of
this DatagramPacket set to 0, and the length set to
the length of

buf

.

**Parameters:** buf

- the buffer to set for this packet.
**Throws:** NullPointerException

- if the argument is null.
**Since:** 1.1
**See Also:** getLength()

,

getData()

- setLength

```java
public void setLength​(int length)
```

Set the length for this packet. The length of the packet is
the number of bytes from the packet's data buffer that will be
sent, or the number of bytes of the packet's data buffer that
will be used for receiving data. The length must be lesser or
equal to the offset plus the length of the packet's buffer.

**Parameters:** length

- the length to set for this packet.
**Throws:** IllegalArgumentException

- if the length is negative
of if the length is greater than the packet's data buffer
length.
**Since:** 1.1
**See Also:** getLength()

,

setData(byte[], int, int)

Constructor Detail

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length)
```

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- buffer for holding the incoming datagram.
**Parameters:** offset

- the offset for the buffer
**Parameters:** length

- the number of bytes to read.
**Since:** 1.2

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length)
```

Constructs a

DatagramPacket

for receiving packets of
length

length

.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- buffer for holding the incoming datagram.
**Parameters:** length

- the number of bytes to read.

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length,

InetAddress
address,
int port)
```

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** offset

- the packet data offset.
**Parameters:** length

- the packet data length.
**Parameters:** address

- the destination address.
**Parameters:** port

- the destination port number.
**Since:** 1.2
**See Also:** InetAddress

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length,

SocketAddress
address)
```

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** offset

- the packet data offset.
**Parameters:** length

- the packet data length.
**Parameters:** address

- the destination socket address.
**Throws:** IllegalArgumentException

- if address type is not supported
**Since:** 1.4
**See Also:** InetAddress

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length,

InetAddress
address,
int port)
```

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** length

- the packet length.
**Parameters:** address

- the destination address.
**Parameters:** port

- the destination port number.
**See Also:** InetAddress

- DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length,

SocketAddress
address)
```

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** length

- the packet length.
**Parameters:** address

- the destination address.
**Throws:** IllegalArgumentException

- if address type is not supported
**Since:** 1.4
**See Also:** InetAddress

---

#### Constructor Detail

DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length)
```

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- buffer for holding the incoming datagram.
**Parameters:** offset

- the offset for the buffer
**Parameters:** length

- the number of bytes to read.
**Since:** 1.2

---

#### DatagramPacket

public DatagramPacket​(byte[] buf,
int offset,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

, specifying an offset into the buffer.

The

length

argument must be less than or equal to

buf.length

.

The

length

argument must be less than or equal to

buf.length

.

DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length)
```

Constructs a

DatagramPacket

for receiving packets of
length

length

.

The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- buffer for holding the incoming datagram.
**Parameters:** length

- the number of bytes to read.

---

#### DatagramPacket

public DatagramPacket​(byte[] buf,
int length)

Constructs a

DatagramPacket

for receiving packets of
length

length

.

The

length

argument must be less than or equal to

buf.length

.

The

length

argument must be less than or equal to

buf.length

.

DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length,

InetAddress
address,
int port)
```

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** offset

- the packet data offset.
**Parameters:** length

- the packet data length.
**Parameters:** address

- the destination address.
**Parameters:** port

- the destination port number.
**Since:** 1.2
**See Also:** InetAddress

---

#### DatagramPacket

public DatagramPacket​(byte[] buf,
int offset,
int length,

InetAddress

address,
int port)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int offset,
int length,

SocketAddress
address)
```

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** offset

- the packet data offset.
**Parameters:** length

- the packet data length.
**Parameters:** address

- the destination socket address.
**Throws:** IllegalArgumentException

- if address type is not supported
**Since:** 1.4
**See Also:** InetAddress

---

#### DatagramPacket

public DatagramPacket​(byte[] buf,
int offset,
int length,

SocketAddress

address)

Constructs a datagram packet for sending packets of length

length

with offset

ioffset

to the
specified port number on the specified host. The

length

argument must be less than or equal to

buf.length

.

DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length,

InetAddress
address,
int port)
```

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** length

- the packet length.
**Parameters:** address

- the destination address.
**Parameters:** port

- the destination port number.
**See Also:** InetAddress

---

#### DatagramPacket

public DatagramPacket​(byte[] buf,
int length,

InetAddress

address,
int port)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

DatagramPacket

```java
public DatagramPacket​(byte[] buf,
int length,

SocketAddress
address)
```

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

**Parameters:** buf

- the packet data.
**Parameters:** length

- the packet length.
**Parameters:** address

- the destination address.
**Throws:** IllegalArgumentException

- if address type is not supported
**Since:** 1.4
**See Also:** InetAddress

---

#### DatagramPacket

public DatagramPacket​(byte[] buf,
int length,

SocketAddress

address)

Constructs a datagram packet for sending packets of length

length

to the specified port number on the specified
host. The

length

argument must be less than or equal
to

buf.length

.

Method Detail

- getAddress

```java
public
InetAddress
getAddress()
```

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

**Returns:** the IP address of the machine to which this datagram is being
sent or from which the datagram was received.
**See Also:** InetAddress

,

setAddress(java.net.InetAddress)

- getPort

```java
public int getPort()
```

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

**Returns:** the port number on the remote host to which this datagram is
being sent or from which the datagram was received.
**See Also:** setPort(int)

- getData

```java
public byte[] getData()
```

Returns the data buffer. The data received or the data to be sent
starts from the

offset

in the buffer,
and runs for

length

long.

**Returns:** the buffer used to receive or send data
**See Also:** setData(byte[], int, int)

- getOffset

```java
public int getOffset()
```

Returns the offset of the data to be sent or the offset of the
data received.

**Returns:** the offset of the data to be sent or the offset of the
data received.
**Since:** 1.2

- getLength

```java
public int getLength()
```

Returns the length of the data to be sent or the length of the
data received.

**Returns:** the length of the data to be sent or the length of the
data received.
**See Also:** setLength(int)

- setData

```java
public void setData​(byte[] buf,
int offset,
int length)
```

Set the data buffer for this packet. This sets the
data, length and offset of the packet.

**Parameters:** buf

- the buffer to set for this packet
**Parameters:** offset

- the offset into the data
**Parameters:** length

- the length of the data
and/or the length of the buffer used to receive data
**Throws:** NullPointerException

- if the argument is null
**Since:** 1.2
**See Also:** getData()

,

getOffset()

,

getLength()

- setAddress

```java
public void setAddress​(
InetAddress
iaddr)
```

Sets the IP address of the machine to which this datagram
is being sent.

**Parameters:** iaddr

- the

InetAddress
**Since:** 1.1
**See Also:** getAddress()

- setPort

```java
public void setPort​(int iport)
```

Sets the port number on the remote host to which this datagram
is being sent.

**Parameters:** iport

- the port number
**Since:** 1.1
**See Also:** getPort()

- setSocketAddress

```java
public void setSocketAddress​(
SocketAddress
address)
```

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

**Parameters:** address

- the

SocketAddress
**Throws:** IllegalArgumentException

- if address is null or is a
SocketAddress subclass not supported by this socket
**Since:** 1.4
**See Also:** getSocketAddress()

- getSocketAddress

```java
public
SocketAddress
getSocketAddress()
```

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

**Returns:** the

SocketAddress
**Since:** 1.4
**See Also:** setSocketAddress(java.net.SocketAddress)

- setData

```java
public void setData​(byte[] buf)
```

Set the data buffer for this packet. With the offset of
this DatagramPacket set to 0, and the length set to
the length of

buf

.

**Parameters:** buf

- the buffer to set for this packet.
**Throws:** NullPointerException

- if the argument is null.
**Since:** 1.1
**See Also:** getLength()

,

getData()

- setLength

```java
public void setLength​(int length)
```

Set the length for this packet. The length of the packet is
the number of bytes from the packet's data buffer that will be
sent, or the number of bytes of the packet's data buffer that
will be used for receiving data. The length must be lesser or
equal to the offset plus the length of the packet's buffer.

**Parameters:** length

- the length to set for this packet.
**Throws:** IllegalArgumentException

- if the length is negative
of if the length is greater than the packet's data buffer
length.
**Since:** 1.1
**See Also:** getLength()

,

setData(byte[], int, int)

---

#### Method Detail

getAddress

```java
public
InetAddress
getAddress()
```

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

**Returns:** the IP address of the machine to which this datagram is being
sent or from which the datagram was received.
**See Also:** InetAddress

,

setAddress(java.net.InetAddress)

---

#### getAddress

public

InetAddress

getAddress()

Returns the IP address of the machine to which this datagram is being
sent or from which the datagram was received.

getPort

```java
public int getPort()
```

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

**Returns:** the port number on the remote host to which this datagram is
being sent or from which the datagram was received.
**See Also:** setPort(int)

---

#### getPort

public int getPort()

Returns the port number on the remote host to which this datagram is
being sent or from which the datagram was received.

getData

```java
public byte[] getData()
```

Returns the data buffer. The data received or the data to be sent
starts from the

offset

in the buffer,
and runs for

length

long.

**Returns:** the buffer used to receive or send data
**See Also:** setData(byte[], int, int)

---

#### getData

public byte[] getData()

Returns the data buffer. The data received or the data to be sent
starts from the

offset

in the buffer,
and runs for

length

long.

getOffset

```java
public int getOffset()
```

Returns the offset of the data to be sent or the offset of the
data received.

**Returns:** the offset of the data to be sent or the offset of the
data received.
**Since:** 1.2

---

#### getOffset

public int getOffset()

Returns the offset of the data to be sent or the offset of the
data received.

getLength

```java
public int getLength()
```

Returns the length of the data to be sent or the length of the
data received.

**Returns:** the length of the data to be sent or the length of the
data received.
**See Also:** setLength(int)

---

#### getLength

public int getLength()

Returns the length of the data to be sent or the length of the
data received.

setData

```java
public void setData​(byte[] buf,
int offset,
int length)
```

Set the data buffer for this packet. This sets the
data, length and offset of the packet.

**Parameters:** buf

- the buffer to set for this packet
**Parameters:** offset

- the offset into the data
**Parameters:** length

- the length of the data
and/or the length of the buffer used to receive data
**Throws:** NullPointerException

- if the argument is null
**Since:** 1.2
**See Also:** getData()

,

getOffset()

,

getLength()

---

#### setData

public void setData​(byte[] buf,
int offset,
int length)

Set the data buffer for this packet. This sets the
data, length and offset of the packet.

setAddress

```java
public void setAddress​(
InetAddress
iaddr)
```

Sets the IP address of the machine to which this datagram
is being sent.

**Parameters:** iaddr

- the

InetAddress
**Since:** 1.1
**See Also:** getAddress()

---

#### setAddress

public void setAddress​(

InetAddress

iaddr)

Sets the IP address of the machine to which this datagram
is being sent.

setPort

```java
public void setPort​(int iport)
```

Sets the port number on the remote host to which this datagram
is being sent.

**Parameters:** iport

- the port number
**Since:** 1.1
**See Also:** getPort()

---

#### setPort

public void setPort​(int iport)

Sets the port number on the remote host to which this datagram
is being sent.

setSocketAddress

```java
public void setSocketAddress​(
SocketAddress
address)
```

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

**Parameters:** address

- the

SocketAddress
**Throws:** IllegalArgumentException

- if address is null or is a
SocketAddress subclass not supported by this socket
**Since:** 1.4
**See Also:** getSocketAddress()

---

#### setSocketAddress

public void setSocketAddress​(

SocketAddress

address)

Sets the SocketAddress (usually IP address + port number) of the remote
host to which this datagram is being sent.

getSocketAddress

```java
public
SocketAddress
getSocketAddress()
```

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

**Returns:** the

SocketAddress
**Since:** 1.4
**See Also:** setSocketAddress(java.net.SocketAddress)

---

#### getSocketAddress

public

SocketAddress

getSocketAddress()

Gets the SocketAddress (usually IP address + port number) of the remote
host that this packet is being sent to or is coming from.

setData

```java
public void setData​(byte[] buf)
```

Set the data buffer for this packet. With the offset of
this DatagramPacket set to 0, and the length set to
the length of

buf

.

**Parameters:** buf

- the buffer to set for this packet.
**Throws:** NullPointerException

- if the argument is null.
**Since:** 1.1
**See Also:** getLength()

,

getData()

---

#### setData

public void setData​(byte[] buf)

Set the data buffer for this packet. With the offset of
this DatagramPacket set to 0, and the length set to
the length of

buf

.

setLength

```java
public void setLength​(int length)
```

Set the length for this packet. The length of the packet is
the number of bytes from the packet's data buffer that will be
sent, or the number of bytes of the packet's data buffer that
will be used for receiving data. The length must be lesser or
equal to the offset plus the length of the packet's buffer.

**Parameters:** length

- the length to set for this packet.
**Throws:** IllegalArgumentException

- if the length is negative
of if the length is greater than the packet's data buffer
length.
**Since:** 1.1
**See Also:** getLength()

,

setData(byte[], int, int)

---

#### setLength

public void setLength​(int length)

Set the length for this packet. The length of the packet is
the number of bytes from the packet's data buffer that will be
sent, or the number of bytes of the packet's data buffer that
will be used for receiving data. The length must be lesser or
equal to the offset plus the length of the packet's buffer.

---

