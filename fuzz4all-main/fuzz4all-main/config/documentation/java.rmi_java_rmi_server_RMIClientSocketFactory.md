# Interface RMIClientSocketFactory

**Source:** `java.rmi\java\rmi\server\RMIClientSocketFactory.html`

### Class Description

```java
public interface
RMIClientSocketFactory
```

An

RMIClientSocketFactory

instance is used by the RMI runtime
in order to obtain client sockets for RMI calls. A remote object can be
associated with an

RMIClientSocketFactory

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

RMIClientSocketFactory

instance associated with a remote
object will be downloaded to clients when the remote object's reference is
transmitted in an RMI call. This

RMIClientSocketFactory

will
be used to create connections to the remote object for remote method calls.

An

RMIClientSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface should be serializable and
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
client socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

**All Known Implementing Classes:** RMISocketFactory

,

SslRMIClientSocketFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Socket
createSocket​(
String
host,
int port)
throws
IOException

Create a client socket connected to the specified host and port.

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
- 1.2

---

### Additional Sections

#### Interface RMIClientSocketFactory

**All Known Implementing Classes:** RMISocketFactory

,

SslRMIClientSocketFactory

```java
public interface
RMIClientSocketFactory
```

An

RMIClientSocketFactory

instance is used by the RMI runtime
in order to obtain client sockets for RMI calls. A remote object can be
associated with an

RMIClientSocketFactory

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

RMIClientSocketFactory

instance associated with a remote
object will be downloaded to clients when the remote object's reference is
transmitted in an RMI call. This

RMIClientSocketFactory

will
be used to create connections to the remote object for remote method calls.

An

RMIClientSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface should be serializable and
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
client socket factory, and

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

RMIClientSocketFactory

An

RMIClientSocketFactory

instance is used by the RMI runtime
in order to obtain client sockets for RMI calls. A remote object can be
associated with an

RMIClientSocketFactory

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

RMIClientSocketFactory

instance associated with a remote
object will be downloaded to clients when the remote object's reference is
transmitted in an RMI call. This

RMIClientSocketFactory

will
be used to create connections to the remote object for remote method calls.

An

RMIClientSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface should be serializable and
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
client socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

An

RMIClientSocketFactory

instance associated with a remote
object will be downloaded to clients when the remote object's reference is
transmitted in an RMI call. This

RMIClientSocketFactory

will
be used to create connections to the remote object for remote method calls.

An

RMIClientSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface should be serializable and
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
client socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

An

RMIClientSocketFactory

instance can also be associated
with a remote object registry so that clients can use custom socket
communication with a remote object registry.

An implementation of this interface should be serializable and
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
client socket factory, and

false

otherwise (and it should also
implement

Object.hashCode()

consistently with its

Object.equals

implementation).

An implementation of this interface should be serializable and
should implement

Object.equals(java.lang.Object)

to return

true

when
passed an instance that represents the same (functionally equivalent)
client socket factory, and

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

Socket

createSocket

​(

String

host,
int port)

Create a client socket connected to the specified host and port.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Socket

createSocket

​(

String

host,
int port)

Create a client socket connected to the specified host and port.

---

#### Method Summary

Create a client socket connected to the specified host and port.

============ METHOD DETAIL ==========

- Method Detail

- createSocket

```java
Socket
createSocket​(
String
host,
int port)
throws
IOException
```

Create a client socket connected to the specified host and port.

**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation
**Since:** 1.2

Method Detail

- createSocket

```java
Socket
createSocket​(
String
host,
int port)
throws
IOException
```

Create a client socket connected to the specified host and port.

**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation
**Since:** 1.2

---

#### Method Detail

createSocket

```java
Socket
createSocket​(
String
host,
int port)
throws
IOException
```

Create a client socket connected to the specified host and port.

**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation
**Since:** 1.2

---

#### createSocket

Socket

createSocket​(

String

host,
int port)
throws

IOException

Create a client socket connected to the specified host and port.

---

