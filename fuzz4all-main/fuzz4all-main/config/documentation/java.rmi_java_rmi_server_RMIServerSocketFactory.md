# Interface RMIServerSocketFactory

**Source:** `java.rmi\java\rmi\server\RMIServerSocketFactory.html`

### Class Description

```java
public interface
RMIServerSocketFactory
```

An

RMIServerSocketFactory

instance is used by the RMI runtime
in order to obtain server sockets for RMI calls. A remote object can be
associated with an

RMIServerSocketFactory

when it is
created/exported via the constructors or

exportObject

methods
of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

An

RMIServerSocketFactory

instance associated with a remote
object is used to obtain the

ServerSocket

used to accept
incoming calls from clients.

An

RMIServerSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
server socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

**All Known Implementing Classes:** RMISocketFactory

,

SslRMIServerSocketFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ServerSocket
createServerSocket​(int port)
throws
IOException

Create a server socket on the specified port (port 0 indicates
an anonymous port).

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
- 1.2

---

### Additional Sections

#### Interface RMIServerSocketFactory

**All Known Implementing Classes:** RMISocketFactory

,

SslRMIServerSocketFactory

```java
public interface
RMIServerSocketFactory
```

An

RMIServerSocketFactory

instance is used by the RMI runtime
in order to obtain server sockets for RMI calls. A remote object can be
associated with an

RMIServerSocketFactory

when it is
created/exported via the constructors or

exportObject

methods
of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

An

RMIServerSocketFactory

instance associated with a remote
object is used to obtain the

ServerSocket

used to accept
incoming calls from clients.

An

RMIServerSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
server socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

**Since:** 1.2
**See Also:** UnicastRemoteObject

,

Activatable

,

LocateRegistry

public interface

RMIServerSocketFactory

An

RMIServerSocketFactory

instance is used by the RMI runtime
in order to obtain server sockets for RMI calls. A remote object can be
associated with an

RMIServerSocketFactory

when it is
created/exported via the constructors or

exportObject

methods
of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

An

RMIServerSocketFactory

instance associated with a remote
object is used to obtain the

ServerSocket

used to accept
incoming calls from clients.

An

RMIServerSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
server socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

An

RMIServerSocketFactory

instance associated with a remote
object is used to obtain the

ServerSocket

used to accept
incoming calls from clients.

An

RMIServerSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
server socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

An

RMIServerSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
server socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

An implementation of this interface
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
server socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ServerSocket

createServerSocket

​(int port)

Create a server socket on the specified port (port 0 indicates
an anonymous port).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ServerSocket

createServerSocket

​(int port)

Create a server socket on the specified port (port 0 indicates
an anonymous port).

---

#### Method Summary

Create a server socket on the specified port (port 0 indicates
an anonymous port).

============ METHOD DETAIL ==========

- Method Detail

- createServerSocket

```java
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Create a server socket on the specified port (port 0 indicates
an anonymous port).

**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation
**Since:** 1.2

Method Detail

- createServerSocket

```java
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Create a server socket on the specified port (port 0 indicates
an anonymous port).

**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation
**Since:** 1.2

---

#### Method Detail

createServerSocket

```java
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Create a server socket on the specified port (port 0 indicates
an anonymous port).

**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation
**Since:** 1.2

---

#### createServerSocket

ServerSocket

createServerSocket​(int port)
throws

IOException

Create a server socket on the specified port (port 0 indicates
an anonymous port).

---

