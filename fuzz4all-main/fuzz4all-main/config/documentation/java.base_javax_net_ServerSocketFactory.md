# Class ServerSocketFactory

**Source:** `java.base\javax\net\ServerSocketFactory.html`

### Class Description

```java
public abstract class
ServerSocketFactory

extends
Object
```

This class creates server sockets. It may be subclassed by other
factories, which create particular types of server sockets. This
provides a general framework for the addition of public socket-level
functionality. It is the server side analogue of a socket factory,
and similarly provides a way to capture a variety of policies related
to the sockets being constructed.

Like socket factories, server Socket factory instances have
methods used to create sockets. There is also an environment
specific default server socket factory; frameworks will often use
their own customized factory.

**Direct Known Subclasses:** SSLServerSocketFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ServerSocketFactory()

Creates a server socket factory.

---

### Method Details

#### public static
ServerSocketFactory
getDefault()

Returns a copy of the environment's default socket factory.

**Returns:**
- the

ServerSocketFactory

---

#### public
ServerSocket
createServerSocket()
throws
IOException

Returns an unbound server socket. The socket is configured with
the socket options (such as accept timeout) given to this factory.

**Returns:**
- the unbound socket

**Throws:**
- IOException

- if the socket cannot be created

**See Also:**
- ServerSocket.bind(java.net.SocketAddress)

,

ServerSocket.bind(java.net.SocketAddress, int)

,

ServerSocket()

---

#### public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException

Returns a server socket bound to the specified port.
The socket is configured with the socket options
(such as accept timeout) given to this factory.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:**
- port

- the port to listen to

**Returns:**
- the

ServerSocket

**Throws:**
- IOException

- for networking errors
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.

**See Also:**
- SecurityManager.checkListen(int)

,

ServerSocket(int)

---

#### public abstract
ServerSocket
createServerSocket​(int port,
int backlog)
throws
IOException

Returns a server socket bound to the specified port, and uses the
specified connection backlog. The socket is configured with
the socket options (such as accept timeout) given to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:**
- port

- the port to listen to
- backlog

- how many connections are queued

**Returns:**
- the

ServerSocket

**Throws:**
- IOException

- for networking errors
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.

**See Also:**
- SecurityManager.checkListen(int)

,

ServerSocket(int, int)

---

#### public abstract
ServerSocket
createServerSocket​(int port,
int backlog,

InetAddress
ifAddress)
throws
IOException

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

The

ifAddress

argument can be used on a multi-homed
host for a

ServerSocket

that will only accept connect
requests to one of its addresses. If

ifAddress

is null,
it will accept connections on all local addresses. The socket is
configured with the socket options (such as accept timeout) given
to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:**
- port

- the port to listen to
- backlog

- how many connections are queued
- ifAddress

- the network interface address to use

**Returns:**
- the

ServerSocket

**Throws:**
- IOException

- for networking errors
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.

**See Also:**
- SecurityManager.checkListen(int)

,

ServerSocket(int, int, java.net.InetAddress)

---

### Additional Sections

#### Class ServerSocketFactory

java.lang.Object

- javax.net.ServerSocketFactory

javax.net.ServerSocketFactory

**Direct Known Subclasses:** SSLServerSocketFactory

```java
public abstract class
ServerSocketFactory

extends
Object
```

This class creates server sockets. It may be subclassed by other
factories, which create particular types of server sockets. This
provides a general framework for the addition of public socket-level
functionality. It is the server side analogue of a socket factory,
and similarly provides a way to capture a variety of policies related
to the sockets being constructed.

Like socket factories, server Socket factory instances have
methods used to create sockets. There is also an environment
specific default server socket factory; frameworks will often use
their own customized factory.

**Since:** 1.4
**See Also:** SocketFactory

public abstract class

ServerSocketFactory

extends

Object

This class creates server sockets. It may be subclassed by other
factories, which create particular types of server sockets. This
provides a general framework for the addition of public socket-level
functionality. It is the server side analogue of a socket factory,
and similarly provides a way to capture a variety of policies related
to the sockets being constructed.

Like socket factories, server Socket factory instances have
methods used to create sockets. There is also an environment
specific default server socket factory; frameworks will often use
their own customized factory.

Like socket factories, server Socket factory instances have
methods used to create sockets. There is also an environment
specific default server socket factory; frameworks will often use
their own customized factory.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ServerSocketFactory

()

Creates a server socket factory.

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

ServerSocket

createServerSocket

()

Returns an unbound server socket.

abstract

ServerSocket

createServerSocket

​(int port)

Returns a server socket bound to the specified port.

abstract

ServerSocket

createServerSocket

​(int port,
int backlog)

Returns a server socket bound to the specified port, and uses the
specified connection backlog.

abstract

ServerSocket

createServerSocket

​(int port,
int backlog,

InetAddress

ifAddress)

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

static

ServerSocketFactory

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

ServerSocketFactory

()

Creates a server socket factory.

---

#### Constructor Summary

Creates a server socket factory.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

ServerSocket

createServerSocket

()

Returns an unbound server socket.

abstract

ServerSocket

createServerSocket

​(int port)

Returns a server socket bound to the specified port.

abstract

ServerSocket

createServerSocket

​(int port,
int backlog)

Returns a server socket bound to the specified port, and uses the
specified connection backlog.

abstract

ServerSocket

createServerSocket

​(int port,
int backlog,

InetAddress

ifAddress)

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

static

ServerSocketFactory

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

Returns an unbound server socket.

Returns a server socket bound to the specified port.

Returns a server socket bound to the specified port, and uses the
specified connection backlog.

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

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

- ServerSocketFactory

```java
protected ServerSocketFactory()
```

Creates a server socket factory.

============ METHOD DETAIL ==========

- Method Detail

- getDefault

```java
public static
ServerSocketFactory
getDefault()
```

Returns a copy of the environment's default socket factory.

**Returns:** the

ServerSocketFactory

- createServerSocket

```java
public
ServerSocket
createServerSocket()
throws
IOException
```

Returns an unbound server socket. The socket is configured with
the socket options (such as accept timeout) given to this factory.

**Returns:** the unbound socket
**Throws:** IOException

- if the socket cannot be created
**See Also:** ServerSocket.bind(java.net.SocketAddress)

,

ServerSocket.bind(java.net.SocketAddress, int)

,

ServerSocket()

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Returns a server socket bound to the specified port.
The socket is configured with the socket options
(such as accept timeout) given to this factory.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int)

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port,
int backlog)
throws
IOException
```

Returns a server socket bound to the specified port, and uses the
specified connection backlog. The socket is configured with
the socket options (such as accept timeout) given to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Parameters:** backlog

- how many connections are queued
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int, int)

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port,
int backlog,

InetAddress
ifAddress)
throws
IOException
```

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

The

ifAddress

argument can be used on a multi-homed
host for a

ServerSocket

that will only accept connect
requests to one of its addresses. If

ifAddress

is null,
it will accept connections on all local addresses. The socket is
configured with the socket options (such as accept timeout) given
to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Parameters:** backlog

- how many connections are queued
**Parameters:** ifAddress

- the network interface address to use
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int, int, java.net.InetAddress)

Constructor Detail

- ServerSocketFactory

```java
protected ServerSocketFactory()
```

Creates a server socket factory.

---

#### Constructor Detail

ServerSocketFactory

```java
protected ServerSocketFactory()
```

Creates a server socket factory.

---

#### ServerSocketFactory

protected ServerSocketFactory()

Creates a server socket factory.

Method Detail

- getDefault

```java
public static
ServerSocketFactory
getDefault()
```

Returns a copy of the environment's default socket factory.

**Returns:** the

ServerSocketFactory

- createServerSocket

```java
public
ServerSocket
createServerSocket()
throws
IOException
```

Returns an unbound server socket. The socket is configured with
the socket options (such as accept timeout) given to this factory.

**Returns:** the unbound socket
**Throws:** IOException

- if the socket cannot be created
**See Also:** ServerSocket.bind(java.net.SocketAddress)

,

ServerSocket.bind(java.net.SocketAddress, int)

,

ServerSocket()

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Returns a server socket bound to the specified port.
The socket is configured with the socket options
(such as accept timeout) given to this factory.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int)

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port,
int backlog)
throws
IOException
```

Returns a server socket bound to the specified port, and uses the
specified connection backlog. The socket is configured with
the socket options (such as accept timeout) given to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Parameters:** backlog

- how many connections are queued
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int, int)

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port,
int backlog,

InetAddress
ifAddress)
throws
IOException
```

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

The

ifAddress

argument can be used on a multi-homed
host for a

ServerSocket

that will only accept connect
requests to one of its addresses. If

ifAddress

is null,
it will accept connections on all local addresses. The socket is
configured with the socket options (such as accept timeout) given
to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Parameters:** backlog

- how many connections are queued
**Parameters:** ifAddress

- the network interface address to use
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int, int, java.net.InetAddress)

---

#### Method Detail

getDefault

```java
public static
ServerSocketFactory
getDefault()
```

Returns a copy of the environment's default socket factory.

**Returns:** the

ServerSocketFactory

---

#### getDefault

public static

ServerSocketFactory

getDefault()

Returns a copy of the environment's default socket factory.

createServerSocket

```java
public
ServerSocket
createServerSocket()
throws
IOException
```

Returns an unbound server socket. The socket is configured with
the socket options (such as accept timeout) given to this factory.

**Returns:** the unbound socket
**Throws:** IOException

- if the socket cannot be created
**See Also:** ServerSocket.bind(java.net.SocketAddress)

,

ServerSocket.bind(java.net.SocketAddress, int)

,

ServerSocket()

---

#### createServerSocket

public

ServerSocket

createServerSocket()
throws

IOException

Returns an unbound server socket. The socket is configured with
the socket options (such as accept timeout) given to this factory.

createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Returns a server socket bound to the specified port.
The socket is configured with the socket options
(such as accept timeout) given to this factory.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int)

---

#### createServerSocket

public abstract

ServerSocket

createServerSocket​(int port)
throws

IOException

Returns a server socket bound to the specified port.
The socket is configured with the socket options
(such as accept timeout) given to this factory.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port,
int backlog)
throws
IOException
```

Returns a server socket bound to the specified port, and uses the
specified connection backlog. The socket is configured with
the socket options (such as accept timeout) given to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Parameters:** backlog

- how many connections are queued
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int, int)

---

#### createServerSocket

public abstract

ServerSocket

createServerSocket​(int port,
int backlog)
throws

IOException

Returns a server socket bound to the specified port, and uses the
specified connection backlog. The socket is configured with
the socket options (such as accept timeout) given to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port,
int backlog,

InetAddress
ifAddress)
throws
IOException
```

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

The

ifAddress

argument can be used on a multi-homed
host for a

ServerSocket

that will only accept connect
requests to one of its addresses. If

ifAddress

is null,
it will accept connections on all local addresses. The socket is
configured with the socket options (such as accept timeout) given
to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port to listen to
**Parameters:** backlog

- how many connections are queued
**Parameters:** ifAddress

- the network interface address to use
**Returns:** the

ServerSocket
**Throws:** IOException

- for networking errors
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

,

ServerSocket(int, int, java.net.InetAddress)

---

#### createServerSocket

public abstract

ServerSocket

createServerSocket​(int port,
int backlog,

InetAddress

ifAddress)
throws

IOException

Returns a server socket bound to the specified port,
with a specified listen backlog and local IP.

The

ifAddress

argument can be used on a multi-homed
host for a

ServerSocket

that will only accept connect
requests to one of its addresses. If

ifAddress

is null,
it will accept connections on all local addresses. The socket is
configured with the socket options (such as accept timeout) given
to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

The

ifAddress

argument can be used on a multi-homed
host for a

ServerSocket

that will only accept connect
requests to one of its addresses. If

ifAddress

is null,
it will accept connections on all local addresses. The socket is
configured with the socket options (such as accept timeout) given
to this factory.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

The

backlog

argument must be a positive
value greater than 0. If the value passed if equal or less
than 0, then the default value will be assumed.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

---

