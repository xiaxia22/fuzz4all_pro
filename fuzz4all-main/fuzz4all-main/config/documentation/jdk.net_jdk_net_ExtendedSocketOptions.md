# Class ExtendedSocketOptions

**Source:** `jdk.net\jdk\net\ExtendedSocketOptions.html`

### Class Description

```java
public final class
ExtendedSocketOptions

extends
Object
```

Defines extended socket options, beyond those defined in

StandardSocketOptions

. These options may be platform
specific.

**Since:** 1.8

---

### Field Details

#### public static final
SocketOption
<
SocketFlow
> SO_FLOW_SLA

Service level properties. When a security manager is installed,
setting or getting this option requires a

NetworkPermission

("setOption.SO_FLOW_SLA")

or

"getOption.SO_FLOW_SLA"

respectively.

---

#### public static final
SocketOption
<
Boolean
> TCP_QUICKACK

Disable Delayed Acknowledgements.

This socket option can be used to reduce or disable delayed
acknowledgments (ACKs). When

TCP_QUICKACK

is enabled, ACKs are
sent immediately, rather than delayed if needed in accordance to normal
TCP operation. This option is not permanent, it only enables a switch to
or from

TCP_QUICKACK

mode. Subsequent operations of the TCP
protocol will once again disable/enable

TCP_QUICKACK

mode
depending on internal protocol processing and factors such as delayed ACK
timeouts occurring and data transfer, therefore this option needs to be
set with

setOption

after each operation of TCP on a given socket.

The value of this socket option is a

Boolean

that represents
whether the option is enabled or disabled. The socket option is specific
to stream-oriented sockets using the TCP/IP protocol. The exact semantics
of this socket option are socket type and system dependent.

**Since:**
- 10

---

#### public static final
SocketOption
<
Integer
> TCP_KEEPIDLE

Keep-Alive idle time.

The value of this socket option is an

Integer

that is the number
of seconds of idle time before keep-alive initiates a probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. The default value for this idle period is
system dependent, but is typically 2 hours. The

TCP_KEEPIDLE

option can be used to affect this value for a given socket.

**Since:**
- 11

---

#### public static final
SocketOption
<
Integer
> TCP_KEEPINTERVAL

Keep-Alive retransmission interval time.

The value of this socket option is an

Integer

that is the number
of seconds to wait before retransmitting a keep-alive probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe after some amount of time.
The default value for this retransmission interval is system dependent,
but is typically 75 seconds. The

TCP_KEEPINTERVAL

option can be
used to affect this value for a given socket.

**Since:**
- 11

---

#### public static final
SocketOption
<
Integer
> TCP_KEEPCOUNT

Keep-Alive retransmission maximum limit.

The value of this socket option is an

Integer

that is the maximum
number of keep-alive probes to be sent. The socket option is specific to
stream-oriented sockets using the TCP/IP protocol. The exact semantics of
this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe a certain number of times
before a connection is considered to be broken. The default value for
this keep-alive probe retransmit limit is system dependent, but is
typically 8. The

TCP_KEEPCOUNT

option can be used to affect this
value for a given socket.

**Since:**
- 11

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class ExtendedSocketOptions

java.lang.Object

- jdk.net.ExtendedSocketOptions

jdk.net.ExtendedSocketOptions

```java
public final class
ExtendedSocketOptions

extends
Object
```

Defines extended socket options, beyond those defined in

StandardSocketOptions

. These options may be platform
specific.

**Since:** 1.8

public final class

ExtendedSocketOptions

extends

Object

Defines extended socket options, beyond those defined in

StandardSocketOptions

. These options may be platform
specific.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

SocketOption

<

SocketFlow

>

SO_FLOW_SLA

Service level properties.

static

SocketOption

<

Integer

>

TCP_KEEPCOUNT

Keep-Alive retransmission maximum limit.

static

SocketOption

<

Integer

>

TCP_KEEPIDLE

Keep-Alive idle time.

static

SocketOption

<

Integer

>

TCP_KEEPINTERVAL

Keep-Alive retransmission interval time.

static

SocketOption

<

Boolean

>

TCP_QUICKACK

Disable Delayed Acknowledgements.

========== METHOD SUMMARY ===========

- Method Summary

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

Field Summary

Fields

Modifier and Type

Field

Description

static

SocketOption

<

SocketFlow

>

SO_FLOW_SLA

Service level properties.

static

SocketOption

<

Integer

>

TCP_KEEPCOUNT

Keep-Alive retransmission maximum limit.

static

SocketOption

<

Integer

>

TCP_KEEPIDLE

Keep-Alive idle time.

static

SocketOption

<

Integer

>

TCP_KEEPINTERVAL

Keep-Alive retransmission interval time.

static

SocketOption

<

Boolean

>

TCP_QUICKACK

Disable Delayed Acknowledgements.

---

#### Field Summary

Service level properties.

Keep-Alive retransmission maximum limit.

Keep-Alive idle time.

Keep-Alive retransmission interval time.

Disable Delayed Acknowledgements.

Method Summary

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

============ FIELD DETAIL ===========

- Field Detail

- SO_FLOW_SLA

```java
public static final
SocketOption
<
SocketFlow
> SO_FLOW_SLA
```

Service level properties. When a security manager is installed,
setting or getting this option requires a

NetworkPermission

("setOption.SO_FLOW_SLA")

or

"getOption.SO_FLOW_SLA"

respectively.

- TCP_QUICKACK

```java
public static final
SocketOption
<
Boolean
> TCP_QUICKACK
```

Disable Delayed Acknowledgements.

This socket option can be used to reduce or disable delayed
acknowledgments (ACKs). When

TCP_QUICKACK

is enabled, ACKs are
sent immediately, rather than delayed if needed in accordance to normal
TCP operation. This option is not permanent, it only enables a switch to
or from

TCP_QUICKACK

mode. Subsequent operations of the TCP
protocol will once again disable/enable

TCP_QUICKACK

mode
depending on internal protocol processing and factors such as delayed ACK
timeouts occurring and data transfer, therefore this option needs to be
set with

setOption

after each operation of TCP on a given socket.

The value of this socket option is a

Boolean

that represents
whether the option is enabled or disabled. The socket option is specific
to stream-oriented sockets using the TCP/IP protocol. The exact semantics
of this socket option are socket type and system dependent.

**Since:** 10

- TCP_KEEPIDLE

```java
public static final
SocketOption
<
Integer
> TCP_KEEPIDLE
```

Keep-Alive idle time.

The value of this socket option is an

Integer

that is the number
of seconds of idle time before keep-alive initiates a probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. The default value for this idle period is
system dependent, but is typically 2 hours. The

TCP_KEEPIDLE

option can be used to affect this value for a given socket.

**Since:** 11

- TCP_KEEPINTERVAL

```java
public static final
SocketOption
<
Integer
> TCP_KEEPINTERVAL
```

Keep-Alive retransmission interval time.

The value of this socket option is an

Integer

that is the number
of seconds to wait before retransmitting a keep-alive probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe after some amount of time.
The default value for this retransmission interval is system dependent,
but is typically 75 seconds. The

TCP_KEEPINTERVAL

option can be
used to affect this value for a given socket.

**Since:** 11

- TCP_KEEPCOUNT

```java
public static final
SocketOption
<
Integer
> TCP_KEEPCOUNT
```

Keep-Alive retransmission maximum limit.

The value of this socket option is an

Integer

that is the maximum
number of keep-alive probes to be sent. The socket option is specific to
stream-oriented sockets using the TCP/IP protocol. The exact semantics of
this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe a certain number of times
before a connection is considered to be broken. The default value for
this keep-alive probe retransmit limit is system dependent, but is
typically 8. The

TCP_KEEPCOUNT

option can be used to affect this
value for a given socket.

**Since:** 11

Field Detail

- SO_FLOW_SLA

```java
public static final
SocketOption
<
SocketFlow
> SO_FLOW_SLA
```

Service level properties. When a security manager is installed,
setting or getting this option requires a

NetworkPermission

("setOption.SO_FLOW_SLA")

or

"getOption.SO_FLOW_SLA"

respectively.

- TCP_QUICKACK

```java
public static final
SocketOption
<
Boolean
> TCP_QUICKACK
```

Disable Delayed Acknowledgements.

This socket option can be used to reduce or disable delayed
acknowledgments (ACKs). When

TCP_QUICKACK

is enabled, ACKs are
sent immediately, rather than delayed if needed in accordance to normal
TCP operation. This option is not permanent, it only enables a switch to
or from

TCP_QUICKACK

mode. Subsequent operations of the TCP
protocol will once again disable/enable

TCP_QUICKACK

mode
depending on internal protocol processing and factors such as delayed ACK
timeouts occurring and data transfer, therefore this option needs to be
set with

setOption

after each operation of TCP on a given socket.

The value of this socket option is a

Boolean

that represents
whether the option is enabled or disabled. The socket option is specific
to stream-oriented sockets using the TCP/IP protocol. The exact semantics
of this socket option are socket type and system dependent.

**Since:** 10

- TCP_KEEPIDLE

```java
public static final
SocketOption
<
Integer
> TCP_KEEPIDLE
```

Keep-Alive idle time.

The value of this socket option is an

Integer

that is the number
of seconds of idle time before keep-alive initiates a probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. The default value for this idle period is
system dependent, but is typically 2 hours. The

TCP_KEEPIDLE

option can be used to affect this value for a given socket.

**Since:** 11

- TCP_KEEPINTERVAL

```java
public static final
SocketOption
<
Integer
> TCP_KEEPINTERVAL
```

Keep-Alive retransmission interval time.

The value of this socket option is an

Integer

that is the number
of seconds to wait before retransmitting a keep-alive probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe after some amount of time.
The default value for this retransmission interval is system dependent,
but is typically 75 seconds. The

TCP_KEEPINTERVAL

option can be
used to affect this value for a given socket.

**Since:** 11

- TCP_KEEPCOUNT

```java
public static final
SocketOption
<
Integer
> TCP_KEEPCOUNT
```

Keep-Alive retransmission maximum limit.

The value of this socket option is an

Integer

that is the maximum
number of keep-alive probes to be sent. The socket option is specific to
stream-oriented sockets using the TCP/IP protocol. The exact semantics of
this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe a certain number of times
before a connection is considered to be broken. The default value for
this keep-alive probe retransmit limit is system dependent, but is
typically 8. The

TCP_KEEPCOUNT

option can be used to affect this
value for a given socket.

**Since:** 11

---

#### Field Detail

SO_FLOW_SLA

```java
public static final
SocketOption
<
SocketFlow
> SO_FLOW_SLA
```

Service level properties. When a security manager is installed,
setting or getting this option requires a

NetworkPermission

("setOption.SO_FLOW_SLA")

or

"getOption.SO_FLOW_SLA"

respectively.

---

#### SO_FLOW_SLA

public static final

SocketOption

<

SocketFlow

> SO_FLOW_SLA

Service level properties. When a security manager is installed,
setting or getting this option requires a

NetworkPermission

("setOption.SO_FLOW_SLA")

or

"getOption.SO_FLOW_SLA"

respectively.

TCP_QUICKACK

```java
public static final
SocketOption
<
Boolean
> TCP_QUICKACK
```

Disable Delayed Acknowledgements.

This socket option can be used to reduce or disable delayed
acknowledgments (ACKs). When

TCP_QUICKACK

is enabled, ACKs are
sent immediately, rather than delayed if needed in accordance to normal
TCP operation. This option is not permanent, it only enables a switch to
or from

TCP_QUICKACK

mode. Subsequent operations of the TCP
protocol will once again disable/enable

TCP_QUICKACK

mode
depending on internal protocol processing and factors such as delayed ACK
timeouts occurring and data transfer, therefore this option needs to be
set with

setOption

after each operation of TCP on a given socket.

The value of this socket option is a

Boolean

that represents
whether the option is enabled or disabled. The socket option is specific
to stream-oriented sockets using the TCP/IP protocol. The exact semantics
of this socket option are socket type and system dependent.

**Since:** 10

---

#### TCP_QUICKACK

public static final

SocketOption

<

Boolean

> TCP_QUICKACK

Disable Delayed Acknowledgements.

This socket option can be used to reduce or disable delayed
acknowledgments (ACKs). When

TCP_QUICKACK

is enabled, ACKs are
sent immediately, rather than delayed if needed in accordance to normal
TCP operation. This option is not permanent, it only enables a switch to
or from

TCP_QUICKACK

mode. Subsequent operations of the TCP
protocol will once again disable/enable

TCP_QUICKACK

mode
depending on internal protocol processing and factors such as delayed ACK
timeouts occurring and data transfer, therefore this option needs to be
set with

setOption

after each operation of TCP on a given socket.

The value of this socket option is a

Boolean

that represents
whether the option is enabled or disabled. The socket option is specific
to stream-oriented sockets using the TCP/IP protocol. The exact semantics
of this socket option are socket type and system dependent.

This socket option can be used to reduce or disable delayed
acknowledgments (ACKs). When

TCP_QUICKACK

is enabled, ACKs are
sent immediately, rather than delayed if needed in accordance to normal
TCP operation. This option is not permanent, it only enables a switch to
or from

TCP_QUICKACK

mode. Subsequent operations of the TCP
protocol will once again disable/enable

TCP_QUICKACK

mode
depending on internal protocol processing and factors such as delayed ACK
timeouts occurring and data transfer, therefore this option needs to be
set with

setOption

after each operation of TCP on a given socket.

The value of this socket option is a

Boolean

that represents
whether the option is enabled or disabled. The socket option is specific
to stream-oriented sockets using the TCP/IP protocol. The exact semantics
of this socket option are socket type and system dependent.

The value of this socket option is a

Boolean

that represents
whether the option is enabled or disabled. The socket option is specific
to stream-oriented sockets using the TCP/IP protocol. The exact semantics
of this socket option are socket type and system dependent.

TCP_KEEPIDLE

```java
public static final
SocketOption
<
Integer
> TCP_KEEPIDLE
```

Keep-Alive idle time.

The value of this socket option is an

Integer

that is the number
of seconds of idle time before keep-alive initiates a probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. The default value for this idle period is
system dependent, but is typically 2 hours. The

TCP_KEEPIDLE

option can be used to affect this value for a given socket.

**Since:** 11

---

#### TCP_KEEPIDLE

public static final

SocketOption

<

Integer

> TCP_KEEPIDLE

Keep-Alive idle time.

The value of this socket option is an

Integer

that is the number
of seconds of idle time before keep-alive initiates a probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. The default value for this idle period is
system dependent, but is typically 2 hours. The

TCP_KEEPIDLE

option can be used to affect this value for a given socket.

The value of this socket option is an

Integer

that is the number
of seconds of idle time before keep-alive initiates a probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. The default value for this idle period is
system dependent, but is typically 2 hours. The

TCP_KEEPIDLE

option can be used to affect this value for a given socket.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. The default value for this idle period is
system dependent, but is typically 2 hours. The

TCP_KEEPIDLE

option can be used to affect this value for a given socket.

TCP_KEEPINTERVAL

```java
public static final
SocketOption
<
Integer
> TCP_KEEPINTERVAL
```

Keep-Alive retransmission interval time.

The value of this socket option is an

Integer

that is the number
of seconds to wait before retransmitting a keep-alive probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe after some amount of time.
The default value for this retransmission interval is system dependent,
but is typically 75 seconds. The

TCP_KEEPINTERVAL

option can be
used to affect this value for a given socket.

**Since:** 11

---

#### TCP_KEEPINTERVAL

public static final

SocketOption

<

Integer

> TCP_KEEPINTERVAL

Keep-Alive retransmission interval time.

The value of this socket option is an

Integer

that is the number
of seconds to wait before retransmitting a keep-alive probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe after some amount of time.
The default value for this retransmission interval is system dependent,
but is typically 75 seconds. The

TCP_KEEPINTERVAL

option can be
used to affect this value for a given socket.

The value of this socket option is an

Integer

that is the number
of seconds to wait before retransmitting a keep-alive probe. The socket
option is specific to stream-oriented sockets using the TCP/IP protocol.
The exact semantics of this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe after some amount of time.
The default value for this retransmission interval is system dependent,
but is typically 75 seconds. The

TCP_KEEPINTERVAL

option can be
used to affect this value for a given socket.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe after some amount of time.
The default value for this retransmission interval is system dependent,
but is typically 75 seconds. The

TCP_KEEPINTERVAL

option can be
used to affect this value for a given socket.

TCP_KEEPCOUNT

```java
public static final
SocketOption
<
Integer
> TCP_KEEPCOUNT
```

Keep-Alive retransmission maximum limit.

The value of this socket option is an

Integer

that is the maximum
number of keep-alive probes to be sent. The socket option is specific to
stream-oriented sockets using the TCP/IP protocol. The exact semantics of
this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe a certain number of times
before a connection is considered to be broken. The default value for
this keep-alive probe retransmit limit is system dependent, but is
typically 8. The

TCP_KEEPCOUNT

option can be used to affect this
value for a given socket.

**Since:** 11

---

#### TCP_KEEPCOUNT

public static final

SocketOption

<

Integer

> TCP_KEEPCOUNT

Keep-Alive retransmission maximum limit.

The value of this socket option is an

Integer

that is the maximum
number of keep-alive probes to be sent. The socket option is specific to
stream-oriented sockets using the TCP/IP protocol. The exact semantics of
this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe a certain number of times
before a connection is considered to be broken. The default value for
this keep-alive probe retransmit limit is system dependent, but is
typically 8. The

TCP_KEEPCOUNT

option can be used to affect this
value for a given socket.

The value of this socket option is an

Integer

that is the maximum
number of keep-alive probes to be sent. The socket option is specific to
stream-oriented sockets using the TCP/IP protocol. The exact semantics of
this socket option are system dependent.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe a certain number of times
before a connection is considered to be broken. The default value for
this keep-alive probe retransmit limit is system dependent, but is
typically 8. The

TCP_KEEPCOUNT

option can be used to affect this
value for a given socket.

When the

SO_KEEPALIVE

option is enabled, TCP probes a connection that has been
idle for some amount of time. If the remote system does not respond to a
keep-alive probe, TCP retransmits the probe a certain number of times
before a connection is considered to be broken. The default value for
this keep-alive probe retransmit limit is system dependent, but is
typically 8. The

TCP_KEEPCOUNT

option can be used to affect this
value for a given socket.

---

