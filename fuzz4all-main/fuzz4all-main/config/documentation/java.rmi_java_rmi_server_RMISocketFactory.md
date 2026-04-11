# Class RMISocketFactory

**Source:** `java.rmi\java\rmi\server\RMISocketFactory.html`

### Class Description

```java
public abstract class
RMISocketFactory

extends
Object

implements
RMIClientSocketFactory
,
RMIServerSocketFactory
```

An

RMISocketFactory

instance is used by the RMI runtime
in order to obtain client and server sockets for RMI calls. An
application may use the

setSocketFactory

method to
request that the RMI runtime use its socket factory instance
instead of the default implementation.

The default socket factory implementation creates a direct
socket connection to the remote host.

The default socket factory implementation creates server sockets that
are bound to the wildcard address, which accepts requests from all network
interfaces.

**All Implemented Interfaces:** RMIClientSocketFactory

,

RMIServerSocketFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public RMISocketFactory()

Constructs an

RMISocketFactory

.

**Since:**
- 1.1

---

### Method Details

#### public abstract
Socket
createSocket​(
String
host,
int port)
throws
IOException

Creates a client socket connected to the specified host and port.

**Specified by:**
- createSocket

in interface

RMIClientSocketFactory

**Parameters:**
- host

- the host name
- port

- the port number

**Returns:**
- a socket connected to the specified host and port.

**Throws:**
- IOException

- if an I/O error occurs during socket creation

**Since:**
- 1.1

---

#### public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException

Create a server socket on the specified port (port 0 indicates
an anonymous port).

**Specified by:**
- createServerSocket

in interface

RMIServerSocketFactory

**Parameters:**
- port

- the port number

**Returns:**
- the server socket on the specified port

**Throws:**
- IOException

- if an I/O error occurs during server socket
creation

**Since:**
- 1.1

---

#### public static void setSocketFactory​(
RMISocketFactory
fac)
throws
IOException

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory). The RMI socket factory can only be set once. Note: The
RMISocketFactory may only be set if the current security manager allows
setting a socket factory; if disallowed, a SecurityException will be
thrown.

**Parameters:**
- fac

- the socket factory

**Throws:**
- IOException

- if the RMI socket factory is already set
- SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.

**See Also:**
- getSocketFactory()

,

SecurityManager.checkSetFactory()

**Since:**
- 1.1

---

#### public static
RMISocketFactory
getSocketFactory()

Returns the socket factory set by the

setSocketFactory

method. Returns

null

if no socket factory has been
set.

**Returns:**
- the socket factory

**See Also:**
- setSocketFactory(RMISocketFactory)

**Since:**
- 1.1

---

#### public static
RMISocketFactory
getDefaultSocketFactory()

Returns a reference to the default socket factory used
by this RMI implementation. This will be the factory used
by the RMI runtime when

getSocketFactory

returns

null

.

**Returns:**
- the default RMI socket factory

**Since:**
- 1.1

---

#### public static void setFailureHandler​(
RMIFailureHandler
fh)

Sets the failure handler to be called by the RMI runtime if server
socket creation fails. By default, if no failure handler is installed
and server socket creation fails, the RMI runtime does attempt to
recreate the server socket.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a

SecurityException

.

**Parameters:**
- fh

- the failure handler

**Throws:**
- SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the
operation.

**See Also:**
- getFailureHandler()

,

RMIFailureHandler.failure(Exception)

**Since:**
- 1.1

---

#### public static
RMIFailureHandler
getFailureHandler()

Returns the handler for socket creation failure set by the

setFailureHandler

method.

**Returns:**
- the failure handler

**See Also:**
- setFailureHandler(RMIFailureHandler)

**Since:**
- 1.1

---

### Additional Sections

#### Class RMISocketFactory

java.lang.Object

- java.rmi.server.RMISocketFactory

java.rmi.server.RMISocketFactory

**All Implemented Interfaces:** RMIClientSocketFactory

,

RMIServerSocketFactory

```java
public abstract class
RMISocketFactory

extends
Object

implements
RMIClientSocketFactory
,
RMIServerSocketFactory
```

An

RMISocketFactory

instance is used by the RMI runtime
in order to obtain client and server sockets for RMI calls. An
application may use the

setSocketFactory

method to
request that the RMI runtime use its socket factory instance
instead of the default implementation.

The default socket factory implementation creates a direct
socket connection to the remote host.

The default socket factory implementation creates server sockets that
are bound to the wildcard address, which accepts requests from all network
interfaces.

**Implementation Note:** You can use the

RMISocketFactory

class to create a server socket that
is bound to a specific address, restricting the origin of requests. For example,
the following code implements a socket factory that binds server sockets to an IPv4
loopback address. This restricts RMI to processing requests only from the local host.

```java
class LoopbackSocketFactory extends RMISocketFactory {
public ServerSocket createServerSocket(int port) throws IOException {
return new ServerSocket(port, 5, InetAddress.getByName("127.0.0.1"));
}

public Socket createSocket(String host, int port) throws IOException {
// just call the default client socket factory
return RMISocketFactory.getDefaultSocketFactory()
.createSocket(host, port);
}
}

// ...

RMISocketFactory.setSocketFactory(new LoopbackSocketFactory());
```

Set the

java.rmi.server.hostname

system property
to

127.0.0.1

to ensure that the generated stubs connect to the right
network interface.
**Since:** 1.1

public abstract class

RMISocketFactory

extends

Object

implements

RMIClientSocketFactory

,

RMIServerSocketFactory

An

RMISocketFactory

instance is used by the RMI runtime
in order to obtain client and server sockets for RMI calls. An
application may use the

setSocketFactory

method to
request that the RMI runtime use its socket factory instance
instead of the default implementation.

The default socket factory implementation creates a direct
socket connection to the remote host.

The default socket factory implementation creates server sockets that
are bound to the wildcard address, which accepts requests from all network
interfaces.

The default socket factory implementation creates a direct
socket connection to the remote host.

The default socket factory implementation creates server sockets that
are bound to the wildcard address, which accepts requests from all network
interfaces.

The default socket factory implementation creates server sockets that
are bound to the wildcard address, which accepts requests from all network
interfaces.

You can use the

RMISocketFactory

class to create a server socket that
is bound to a specific address, restricting the origin of requests. For example,
the following code implements a socket factory that binds server sockets to an IPv4
loopback address. This restricts RMI to processing requests only from the local host.

```java
class LoopbackSocketFactory extends RMISocketFactory {
public ServerSocket createServerSocket(int port) throws IOException {
return new ServerSocket(port, 5, InetAddress.getByName("127.0.0.1"));
}

public Socket createSocket(String host, int port) throws IOException {
// just call the default client socket factory
return RMISocketFactory.getDefaultSocketFactory()
.createSocket(host, port);
}
}

// ...

RMISocketFactory.setSocketFactory(new LoopbackSocketFactory());
```

Set the

java.rmi.server.hostname

system property
to

127.0.0.1

to ensure that the generated stubs connect to the right
network interface.

class LoopbackSocketFactory extends RMISocketFactory {
public ServerSocket createServerSocket(int port) throws IOException {
return new ServerSocket(port, 5, InetAddress.getByName("127.0.0.1"));
}

public Socket createSocket(String host, int port) throws IOException {
// just call the default client socket factory
return RMISocketFactory.getDefaultSocketFactory()
.createSocket(host, port);
}
}

// ...

RMISocketFactory.setSocketFactory(new LoopbackSocketFactory());

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMISocketFactory

()

Constructs an

RMISocketFactory

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

abstract

ServerSocket

createServerSocket

​(int port)

Create a server socket on the specified port (port 0 indicates
an anonymous port).

abstract

Socket

createSocket

​(

String

host,
int port)

Creates a client socket connected to the specified host and port.

static

RMISocketFactory

getDefaultSocketFactory

()

Returns a reference to the default socket factory used
by this RMI implementation.

static

RMIFailureHandler

getFailureHandler

()

Returns the handler for socket creation failure set by the

setFailureHandler

method.

static

RMISocketFactory

getSocketFactory

()

Returns the socket factory set by the

setSocketFactory

method.

static void

setFailureHandler

​(

RMIFailureHandler

fh)

Sets the failure handler to be called by the RMI runtime if server
socket creation fails.

static void

setSocketFactory

​(

RMISocketFactory

fac)

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory).

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

RMISocketFactory

()

Constructs an

RMISocketFactory

.

---

#### Constructor Summary

Constructs an

RMISocketFactory

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

abstract

ServerSocket

createServerSocket

​(int port)

Create a server socket on the specified port (port 0 indicates
an anonymous port).

abstract

Socket

createSocket

​(

String

host,
int port)

Creates a client socket connected to the specified host and port.

static

RMISocketFactory

getDefaultSocketFactory

()

Returns a reference to the default socket factory used
by this RMI implementation.

static

RMIFailureHandler

getFailureHandler

()

Returns the handler for socket creation failure set by the

setFailureHandler

method.

static

RMISocketFactory

getSocketFactory

()

Returns the socket factory set by the

setSocketFactory

method.

static void

setFailureHandler

​(

RMIFailureHandler

fh)

Sets the failure handler to be called by the RMI runtime if server
socket creation fails.

static void

setSocketFactory

​(

RMISocketFactory

fac)

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory).

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

Create a server socket on the specified port (port 0 indicates
an anonymous port).

Creates a client socket connected to the specified host and port.

Returns a reference to the default socket factory used
by this RMI implementation.

Returns the handler for socket creation failure set by the

setFailureHandler

method.

Returns the socket factory set by the

setSocketFactory

method.

Sets the failure handler to be called by the RMI runtime if server
socket creation fails.

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory).

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

- RMISocketFactory

```java
public RMISocketFactory()
```

Constructs an

RMISocketFactory

.

**Since:** 1.1

============ METHOD DETAIL ==========

- Method Detail

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
```

Creates a client socket connected to the specified host and port.

**Specified by:** createSocket

in interface

RMIClientSocketFactory
**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation
**Since:** 1.1

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Create a server socket on the specified port (port 0 indicates
an anonymous port).

**Specified by:** createServerSocket

in interface

RMIServerSocketFactory
**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation
**Since:** 1.1

- setSocketFactory

```java
public static void setSocketFactory​(
RMISocketFactory
fac)
throws
IOException
```

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory). The RMI socket factory can only be set once. Note: The
RMISocketFactory may only be set if the current security manager allows
setting a socket factory; if disallowed, a SecurityException will be
thrown.

**Parameters:** fac

- the socket factory
**Throws:** IOException

- if the RMI socket factory is already set
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**Since:** 1.1
**See Also:** getSocketFactory()

,

SecurityManager.checkSetFactory()

- getSocketFactory

```java
public static
RMISocketFactory
getSocketFactory()
```

Returns the socket factory set by the

setSocketFactory

method. Returns

null

if no socket factory has been
set.

**Returns:** the socket factory
**Since:** 1.1
**See Also:** setSocketFactory(RMISocketFactory)

- getDefaultSocketFactory

```java
public static
RMISocketFactory
getDefaultSocketFactory()
```

Returns a reference to the default socket factory used
by this RMI implementation. This will be the factory used
by the RMI runtime when

getSocketFactory

returns

null

.

**Returns:** the default RMI socket factory
**Since:** 1.1

- setFailureHandler

```java
public static void setFailureHandler​(
RMIFailureHandler
fh)
```

Sets the failure handler to be called by the RMI runtime if server
socket creation fails. By default, if no failure handler is installed
and server socket creation fails, the RMI runtime does attempt to
recreate the server socket.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a

SecurityException

.

**Parameters:** fh

- the failure handler
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the
operation.
**Since:** 1.1
**See Also:** getFailureHandler()

,

RMIFailureHandler.failure(Exception)

- getFailureHandler

```java
public static
RMIFailureHandler
getFailureHandler()
```

Returns the handler for socket creation failure set by the

setFailureHandler

method.

**Returns:** the failure handler
**Since:** 1.1
**See Also:** setFailureHandler(RMIFailureHandler)

Constructor Detail

- RMISocketFactory

```java
public RMISocketFactory()
```

Constructs an

RMISocketFactory

.

**Since:** 1.1

---

#### Constructor Detail

RMISocketFactory

```java
public RMISocketFactory()
```

Constructs an

RMISocketFactory

.

**Since:** 1.1

---

#### RMISocketFactory

public RMISocketFactory()

Constructs an

RMISocketFactory

.

Method Detail

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
```

Creates a client socket connected to the specified host and port.

**Specified by:** createSocket

in interface

RMIClientSocketFactory
**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation
**Since:** 1.1

- createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Create a server socket on the specified port (port 0 indicates
an anonymous port).

**Specified by:** createServerSocket

in interface

RMIServerSocketFactory
**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation
**Since:** 1.1

- setSocketFactory

```java
public static void setSocketFactory​(
RMISocketFactory
fac)
throws
IOException
```

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory). The RMI socket factory can only be set once. Note: The
RMISocketFactory may only be set if the current security manager allows
setting a socket factory; if disallowed, a SecurityException will be
thrown.

**Parameters:** fac

- the socket factory
**Throws:** IOException

- if the RMI socket factory is already set
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**Since:** 1.1
**See Also:** getSocketFactory()

,

SecurityManager.checkSetFactory()

- getSocketFactory

```java
public static
RMISocketFactory
getSocketFactory()
```

Returns the socket factory set by the

setSocketFactory

method. Returns

null

if no socket factory has been
set.

**Returns:** the socket factory
**Since:** 1.1
**See Also:** setSocketFactory(RMISocketFactory)

- getDefaultSocketFactory

```java
public static
RMISocketFactory
getDefaultSocketFactory()
```

Returns a reference to the default socket factory used
by this RMI implementation. This will be the factory used
by the RMI runtime when

getSocketFactory

returns

null

.

**Returns:** the default RMI socket factory
**Since:** 1.1

- setFailureHandler

```java
public static void setFailureHandler​(
RMIFailureHandler
fh)
```

Sets the failure handler to be called by the RMI runtime if server
socket creation fails. By default, if no failure handler is installed
and server socket creation fails, the RMI runtime does attempt to
recreate the server socket.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a

SecurityException

.

**Parameters:** fh

- the failure handler
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the
operation.
**Since:** 1.1
**See Also:** getFailureHandler()

,

RMIFailureHandler.failure(Exception)

- getFailureHandler

```java
public static
RMIFailureHandler
getFailureHandler()
```

Returns the handler for socket creation failure set by the

setFailureHandler

method.

**Returns:** the failure handler
**Since:** 1.1
**See Also:** setFailureHandler(RMIFailureHandler)

---

#### Method Detail

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
```

Creates a client socket connected to the specified host and port.

**Specified by:** createSocket

in interface

RMIClientSocketFactory
**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation
**Since:** 1.1

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

Creates a client socket connected to the specified host and port.

createServerSocket

```java
public abstract
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Create a server socket on the specified port (port 0 indicates
an anonymous port).

**Specified by:** createServerSocket

in interface

RMIServerSocketFactory
**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation
**Since:** 1.1

---

#### createServerSocket

public abstract

ServerSocket

createServerSocket​(int port)
throws

IOException

Create a server socket on the specified port (port 0 indicates
an anonymous port).

setSocketFactory

```java
public static void setSocketFactory​(
RMISocketFactory
fac)
throws
IOException
```

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory). The RMI socket factory can only be set once. Note: The
RMISocketFactory may only be set if the current security manager allows
setting a socket factory; if disallowed, a SecurityException will be
thrown.

**Parameters:** fac

- the socket factory
**Throws:** IOException

- if the RMI socket factory is already set
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the operation.
**Since:** 1.1
**See Also:** getSocketFactory()

,

SecurityManager.checkSetFactory()

---

#### setSocketFactory

public static void setSocketFactory​(

RMISocketFactory

fac)
throws

IOException

Set the global socket factory from which RMI gets sockets (if the
remote object is not associated with a specific client and/or server
socket factory). The RMI socket factory can only be set once. Note: The
RMISocketFactory may only be set if the current security manager allows
setting a socket factory; if disallowed, a SecurityException will be
thrown.

getSocketFactory

```java
public static
RMISocketFactory
getSocketFactory()
```

Returns the socket factory set by the

setSocketFactory

method. Returns

null

if no socket factory has been
set.

**Returns:** the socket factory
**Since:** 1.1
**See Also:** setSocketFactory(RMISocketFactory)

---

#### getSocketFactory

public static

RMISocketFactory

getSocketFactory()

Returns the socket factory set by the

setSocketFactory

method. Returns

null

if no socket factory has been
set.

getDefaultSocketFactory

```java
public static
RMISocketFactory
getDefaultSocketFactory()
```

Returns a reference to the default socket factory used
by this RMI implementation. This will be the factory used
by the RMI runtime when

getSocketFactory

returns

null

.

**Returns:** the default RMI socket factory
**Since:** 1.1

---

#### getDefaultSocketFactory

public static

RMISocketFactory

getDefaultSocketFactory()

Returns a reference to the default socket factory used
by this RMI implementation. This will be the factory used
by the RMI runtime when

getSocketFactory

returns

null

.

setFailureHandler

```java
public static void setFailureHandler​(
RMIFailureHandler
fh)
```

Sets the failure handler to be called by the RMI runtime if server
socket creation fails. By default, if no failure handler is installed
and server socket creation fails, the RMI runtime does attempt to
recreate the server socket.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a

SecurityException

.

**Parameters:** fh

- the failure handler
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow the
operation.
**Since:** 1.1
**See Also:** getFailureHandler()

,

RMIFailureHandler.failure(Exception)

---

#### setFailureHandler

public static void setFailureHandler​(

RMIFailureHandler

fh)

Sets the failure handler to be called by the RMI runtime if server
socket creation fails. By default, if no failure handler is installed
and server socket creation fails, the RMI runtime does attempt to
recreate the server socket.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a

SecurityException

.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a

SecurityException

.

getFailureHandler

```java
public static
RMIFailureHandler
getFailureHandler()
```

Returns the handler for socket creation failure set by the

setFailureHandler

method.

**Returns:** the failure handler
**Since:** 1.1
**See Also:** setFailureHandler(RMIFailureHandler)

---

#### getFailureHandler

public static

RMIFailureHandler

getFailureHandler()

Returns the handler for socket creation failure set by the

setFailureHandler

method.

---

