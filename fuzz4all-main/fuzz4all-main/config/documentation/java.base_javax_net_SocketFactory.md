# Class SocketFactory

**Source:** `java.base\javax\net\SocketFactory.html`

### Class Description

```java
public abstract class
SocketFactory

extends
Object
```

This class creates sockets. It may be subclassed by other factories,
which create particular subclasses of sockets and thus provide a general
framework for the addition of public socket-level functionality.

Socket factories are a simple way to capture a variety of policies
related to the sockets being constructed, producing such sockets in
a way which does not require special configuration of the code which
asks for the sockets:

- Due to polymorphism of both factories and sockets, different
kinds of sockets can be used by the same application code just
by passing it different kinds of factories.

Factories can themselves be customized with parameters used
in socket construction. So for example, factories could be
customized to return sockets with different networking timeouts
or security parameters already configured.

The sockets returned to the application can be subclasses
of java.net.Socket, so that they can directly expose new APIs
for features such as compression, security, record marking,
statistics collection, or firewall tunneling.

Factory classes are specified by environment-specific configuration
mechanisms. For example, the

getDefault

method could return
a factory that was appropriate for a particular user or applet, and a
framework could use a factory customized to its own purposes.

**Direct Known Subclasses:** SSLSocketFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SocketFactory()

Creates a

SocketFactory

.

---

### Method Details

#### public static
SocketFactory
getDefault()

Returns a copy of the environment's default socket factory.

**Returns:**
- the default

SocketFactory

---

#### public
Socket
createSocket()
throws
IOException

Creates an unconnected socket.

**Returns:**
- the unconnected socket

**Throws:**
- IOException

- if the socket cannot be created

**See Also:**
- Socket.connect(java.net.SocketAddress)

,

Socket.connect(java.net.SocketAddress, int)

,

Socket()

---

#### public abstract
Socket
createSocket​(
String
host,
int port)
throws
IOException
,

UnknownHostException

Creates a socket and connects it to the specified remote host
at the specified remote port. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:**
- host

- the server host name with which to connect, or

null

for the loopback address.
- port

- the server port

**Returns:**
- the

Socket

**Throws:**
- IOException

- if an I/O error occurs when creating the socket
- SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
- UnknownHostException

- if the host is not known
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.

**See Also:**
- SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int)

---

#### public abstract
Socket
createSocket​(
String
host,
int port,

InetAddress
localHost,
int localPort)
throws
IOException
,

UnknownHostException

Creates a socket and connects it to the specified remote host
on the specified remote port.
The socket will also be bound to the local address and port supplied.
This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:**
- host

- the server host name with which to connect, or

null

for the loopback address.
- port

- the server port
- localHost

- the local address the socket is bound to
- localPort

- the local port the socket is bound to

**Returns:**
- the

Socket

**Throws:**
- IOException

- if an I/O error occurs when creating the socket
- SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
- UnknownHostException

- if the host is not known
- IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.

**See Also:**
- SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int, java.net.InetAddress, int)

---

#### public abstract
Socket
createSocket​(
InetAddress
host,
int port)
throws
IOException

Creates a socket and connects it to the specified port number
at the specified address. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:**
- host

- the server host
- port

- the server port

**Returns:**
- the

Socket

**Throws:**
- IOException

- if an I/O error occurs when creating the socket
- SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
- NullPointerException

- if

host

is null.

**See Also:**
- SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int)

---

#### public abstract
Socket
createSocket​(
InetAddress
address,
int port,

InetAddress
localAddress,
int localPort)
throws
IOException

Creates a socket and connect it to the specified remote address
on the specified remote port. The socket will also be bound
to the local address and port suplied. The socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:**
- address

- the server network address
- port

- the server port
- localAddress

- the client network address
- localPort

- the client port

**Returns:**
- the

Socket

**Throws:**
- IOException

- if an I/O error occurs when creating the socket
- SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.
- NullPointerException

- if

address

is null.

**See Also:**
- SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int,
java.net.InetAddress, int)

---

### Additional Sections

#### Class SocketFactory

java.lang.Object

- javax.net.SocketFactory

javax.net.SocketFactory

**Direct Known Subclasses:** SSLSocketFactory

```java
public abstract class
SocketFactory

extends
Object
```

This class creates sockets. It may be subclassed by other factories,
which create particular subclasses of sockets and thus provide a general
framework for the addition of public socket-level functionality.

Socket factories are a simple way to capture a variety of policies
related to the sockets being constructed, producing such sockets in
a way which does not require special configuration of the code which
asks for the sockets:

- Due to polymorphism of both factories and sockets, different
kinds of sockets can be used by the same application code just
by passing it different kinds of factories.

Factories can themselves be customized with parameters used
in socket construction. So for example, factories could be
customized to return sockets with different networking timeouts
or security parameters already configured.

The sockets returned to the application can be subclasses
of java.net.Socket, so that they can directly expose new APIs
for features such as compression, security, record marking,
statistics collection, or firewall tunneling.

Factory classes are specified by environment-specific configuration
mechanisms. For example, the

getDefault

method could return
a factory that was appropriate for a particular user or applet, and a
framework could use a factory customized to its own purposes.

**Since:** 1.4
**See Also:** ServerSocketFactory

public abstract class

SocketFactory

extends

Object

This class creates sockets. It may be subclassed by other factories,
which create particular subclasses of sockets and thus provide a general
framework for the addition of public socket-level functionality.

Socket factories are a simple way to capture a variety of policies
related to the sockets being constructed, producing such sockets in
a way which does not require special configuration of the code which
asks for the sockets:

- Due to polymorphism of both factories and sockets, different
kinds of sockets can be used by the same application code just
by passing it different kinds of factories.

Factories can themselves be customized with parameters used
in socket construction. So for example, factories could be
customized to return sockets with different networking timeouts
or security parameters already configured.

The sockets returned to the application can be subclasses
of java.net.Socket, so that they can directly expose new APIs
for features such as compression, security, record marking,
statistics collection, or firewall tunneling.

Factory classes are specified by environment-specific configuration
mechanisms. For example, the

getDefault

method could return
a factory that was appropriate for a particular user or applet, and a
framework could use a factory customized to its own purposes.

Socket factories are a simple way to capture a variety of policies
related to the sockets being constructed, producing such sockets in
a way which does not require special configuration of the code which
asks for the sockets:

- Due to polymorphism of both factories and sockets, different
kinds of sockets can be used by the same application code just
by passing it different kinds of factories.

Factories can themselves be customized with parameters used
in socket construction. So for example, factories could be
customized to return sockets with different networking timeouts
or security parameters already configured.

The sockets returned to the application can be subclasses
of java.net.Socket, so that they can directly expose new APIs
for features such as compression, security, record marking,
statistics collection, or firewall tunneling.

Factory classes are specified by environment-specific configuration
mechanisms. For example, the

getDefault

method could return
a factory that was appropriate for a particular user or applet, and a
framework could use a factory customized to its own purposes.

Due to polymorphism of both factories and sockets, different
kinds of sockets can be used by the same application code just
by passing it different kinds of factories.

Factories can themselves be customized with parameters used
in socket construction. So for example, factories could be
customized to return sockets with different networking timeouts
or security parameters already configured.

The sockets returned to the application can be subclasses
of java.net.Socket, so that they can directly expose new APIs
for features such as compression, security, record marking,
statistics collection, or firewall tunneling.

Factory classes are specified by environment-specific configuration
mechanisms. For example, the

getDefault

method could return
a factory that was appropriate for a particular user or applet, and a
framework could use a factory customized to its own purposes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SocketFactory

()

Creates a

SocketFactory

.

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

Socket

createSocket

()

Creates an unconnected socket.

abstract

Socket

createSocket

​(

String

host,
int port)

Creates a socket and connects it to the specified remote host
at the specified remote port.

abstract

Socket

createSocket

​(

String

host,
int port,

InetAddress

localHost,
int localPort)

Creates a socket and connects it to the specified remote host
on the specified remote port.

abstract

Socket

createSocket

​(

InetAddress

host,
int port)

Creates a socket and connects it to the specified port number
at the specified address.

abstract

Socket

createSocket

​(

InetAddress

address,
int port,

InetAddress

localAddress,
int localPort)

Creates a socket and connect it to the specified remote address
on the specified remote port.

static

SocketFactory

getDefault

()

Returns a copy of the environment's default socket factory.

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

protected

SocketFactory

()

Creates a

SocketFactory

.

---

#### Constructor Summary

Creates a

SocketFactory

.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Socket

createSocket

()

Creates an unconnected socket.

abstract

Socket

createSocket

​(

String

host,
int port)

Creates a socket and connects it to the specified remote host
at the specified remote port.

abstract

Socket

createSocket

​(

String

host,
int port,

InetAddress

localHost,
int localPort)

Creates a socket and connects it to the specified remote host
on the specified remote port.

abstract

Socket

createSocket

​(

InetAddress

host,
int port)

Creates a socket and connects it to the specified port number
at the specified address.

abstract

Socket

createSocket

​(

InetAddress

address,
int port,

InetAddress

localAddress,
int localPort)

Creates a socket and connect it to the specified remote address
on the specified remote port.

static

SocketFactory

getDefault

()

Returns a copy of the environment's default socket factory.

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

Creates an unconnected socket.

Creates a socket and connects it to the specified remote host
at the specified remote port.

Creates a socket and connects it to the specified remote host
on the specified remote port.

Creates a socket and connects it to the specified port number
at the specified address.

Creates a socket and connect it to the specified remote address
on the specified remote port.

Returns a copy of the environment's default socket factory.

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

- SocketFactory

```java
protected SocketFactory()
```

Creates a

SocketFactory

.

============ METHOD DETAIL ==========

- Method Detail

- getDefault

```java
public static
SocketFactory
getDefault()
```

Returns a copy of the environment's default socket factory.

**Returns:** the default

SocketFactory

- createSocket

```java
public
Socket
createSocket()
throws
IOException
```

Creates an unconnected socket.

**Returns:** the unconnected socket
**Throws:** IOException

- if the socket cannot be created
**See Also:** Socket.connect(java.net.SocketAddress)

,

Socket.connect(java.net.SocketAddress, int)

,

Socket()

- createSocket

```java
public abstract
Socket
createSocket​(
String
host,
int port)
throws
IOException
,

UnknownHostException
```

Creates a socket and connects it to the specified remote host
at the specified remote port. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host name with which to connect, or

null

for the loopback address.
**Parameters:** port

- the server port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** UnknownHostException

- if the host is not known
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int)

- createSocket

```java
public abstract
Socket
createSocket​(
String
host,
int port,

InetAddress
localHost,
int localPort)
throws
IOException
,

UnknownHostException
```

Creates a socket and connects it to the specified remote host
on the specified remote port.
The socket will also be bound to the local address and port supplied.
This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host name with which to connect, or

null

for the loopback address.
**Parameters:** port

- the server port
**Parameters:** localHost

- the local address the socket is bound to
**Parameters:** localPort

- the local port the socket is bound to
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** UnknownHostException

- if the host is not known
**Throws:** IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int, java.net.InetAddress, int)

- createSocket

```java
public abstract
Socket
createSocket​(
InetAddress
host,
int port)
throws
IOException
```

Creates a socket and connects it to the specified port number
at the specified address. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host
**Parameters:** port

- the server port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**Throws:** NullPointerException

- if

host

is null.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int)

- createSocket

```java
public abstract
Socket
createSocket​(
InetAddress
address,
int port,

InetAddress
localAddress,
int localPort)
throws
IOException
```

Creates a socket and connect it to the specified remote address
on the specified remote port. The socket will also be bound
to the local address and port suplied. The socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** address

- the server network address
**Parameters:** port

- the server port
**Parameters:** localAddress

- the client network address
**Parameters:** localPort

- the client port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.
**Throws:** NullPointerException

- if

address

is null.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int,
java.net.InetAddress, int)

Constructor Detail

- SocketFactory

```java
protected SocketFactory()
```

Creates a

SocketFactory

.

---

#### Constructor Detail

SocketFactory

```java
protected SocketFactory()
```

Creates a

SocketFactory

.

---

#### SocketFactory

protected SocketFactory()

Creates a

SocketFactory

.

Method Detail

- getDefault

```java
public static
SocketFactory
getDefault()
```

Returns a copy of the environment's default socket factory.

**Returns:** the default

SocketFactory

- createSocket

```java
public
Socket
createSocket()
throws
IOException
```

Creates an unconnected socket.

**Returns:** the unconnected socket
**Throws:** IOException

- if the socket cannot be created
**See Also:** Socket.connect(java.net.SocketAddress)

,

Socket.connect(java.net.SocketAddress, int)

,

Socket()

- createSocket

```java
public abstract
Socket
createSocket​(
String
host,
int port)
throws
IOException
,

UnknownHostException
```

Creates a socket and connects it to the specified remote host
at the specified remote port. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host name with which to connect, or

null

for the loopback address.
**Parameters:** port

- the server port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** UnknownHostException

- if the host is not known
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int)

- createSocket

```java
public abstract
Socket
createSocket​(
String
host,
int port,

InetAddress
localHost,
int localPort)
throws
IOException
,

UnknownHostException
```

Creates a socket and connects it to the specified remote host
on the specified remote port.
The socket will also be bound to the local address and port supplied.
This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host name with which to connect, or

null

for the loopback address.
**Parameters:** port

- the server port
**Parameters:** localHost

- the local address the socket is bound to
**Parameters:** localPort

- the local port the socket is bound to
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** UnknownHostException

- if the host is not known
**Throws:** IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int, java.net.InetAddress, int)

- createSocket

```java
public abstract
Socket
createSocket​(
InetAddress
host,
int port)
throws
IOException
```

Creates a socket and connects it to the specified port number
at the specified address. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host
**Parameters:** port

- the server port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**Throws:** NullPointerException

- if

host

is null.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int)

- createSocket

```java
public abstract
Socket
createSocket​(
InetAddress
address,
int port,

InetAddress
localAddress,
int localPort)
throws
IOException
```

Creates a socket and connect it to the specified remote address
on the specified remote port. The socket will also be bound
to the local address and port suplied. The socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** address

- the server network address
**Parameters:** port

- the server port
**Parameters:** localAddress

- the client network address
**Parameters:** localPort

- the client port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.
**Throws:** NullPointerException

- if

address

is null.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int,
java.net.InetAddress, int)

---

#### Method Detail

getDefault

```java
public static
SocketFactory
getDefault()
```

Returns a copy of the environment's default socket factory.

**Returns:** the default

SocketFactory

---

#### getDefault

public static

SocketFactory

getDefault()

Returns a copy of the environment's default socket factory.

createSocket

```java
public
Socket
createSocket()
throws
IOException
```

Creates an unconnected socket.

**Returns:** the unconnected socket
**Throws:** IOException

- if the socket cannot be created
**See Also:** Socket.connect(java.net.SocketAddress)

,

Socket.connect(java.net.SocketAddress, int)

,

Socket()

---

#### createSocket

public

Socket

createSocket()
throws

IOException

Creates an unconnected socket.

createSocket

```java
public abstract
Socket
createSocket​(
String
host,
int port)
throws
IOException
,

UnknownHostException
```

Creates a socket and connects it to the specified remote host
at the specified remote port. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host name with which to connect, or

null

for the loopback address.
**Parameters:** port

- the server port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** UnknownHostException

- if the host is not known
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int)

---

#### createSocket

public abstract

Socket

createSocket​(

String

host,
int port)
throws

IOException

,

UnknownHostException

Creates a socket and connects it to the specified remote host
at the specified remote port. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

createSocket

```java
public abstract
Socket
createSocket​(
String
host,
int port,

InetAddress
localHost,
int localPort)
throws
IOException
,

UnknownHostException
```

Creates a socket and connects it to the specified remote host
on the specified remote port.
The socket will also be bound to the local address and port supplied.
This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host name with which to connect, or

null

for the loopback address.
**Parameters:** port

- the server port
**Parameters:** localHost

- the local address the socket is bound to
**Parameters:** localPort

- the local port the socket is bound to
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** UnknownHostException

- if the host is not known
**Throws:** IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(String, int, java.net.InetAddress, int)

---

#### createSocket

public abstract

Socket

createSocket​(

String

host,
int port,

InetAddress

localHost,
int localPort)
throws

IOException

,

UnknownHostException

Creates a socket and connects it to the specified remote host
on the specified remote port.
The socket will also be bound to the local address and port supplied.
This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

createSocket

```java
public abstract
Socket
createSocket​(
InetAddress
host,
int port)
throws
IOException
```

Creates a socket and connects it to the specified port number
at the specified address. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** host

- the server host
**Parameters:** port

- the server port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**Throws:** NullPointerException

- if

host

is null.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int)

---

#### createSocket

public abstract

Socket

createSocket​(

InetAddress

host,
int port)
throws

IOException

Creates a socket and connects it to the specified port number
at the specified address. This socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

createSocket

```java
public abstract
Socket
createSocket​(
InetAddress
address,
int port,

InetAddress
localAddress,
int localPort)
throws
IOException
```

Creates a socket and connect it to the specified remote address
on the specified remote port. The socket will also be bound
to the local address and port suplied. The socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

**Parameters:** address

- the server network address
**Parameters:** port

- the server port
**Parameters:** localAddress

- the client network address
**Parameters:** localPort

- the client port
**Returns:** the

Socket
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkConnect

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter or localPort
parameter is outside the specified range of valid port values,
which is between 0 and 65535, inclusive.
**Throws:** NullPointerException

- if

address

is null.
**See Also:** SecurityManager.checkConnect(java.lang.String, int)

,

Socket(java.net.InetAddress, int,
java.net.InetAddress, int)

---

#### createSocket

public abstract

Socket

createSocket​(

InetAddress

address,
int port,

InetAddress

localAddress,
int localPort)
throws

IOException

Creates a socket and connect it to the specified remote address
on the specified remote port. The socket will also be bound
to the local address and port suplied. The socket is configured using
the socket options established for this factory.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

If there is a security manager, its

checkConnect

method is called with the host address and

port

as its arguments. This could result in a SecurityException.

---

