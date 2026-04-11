# Class RMIJRMPServerImpl

**Source:** `java.management.rmi\javax\management\remote\rmi\RMIJRMPServerImpl.html`

### Class Description

```java
public class
RMIJRMPServerImpl

extends
RMIServerImpl
```

An

RMIServer

object that is exported through JRMP and that
creates client connections as RMI objects exported through JRMP.
User code does not usually reference this class directly.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Remote

,

RMIServer

---

### Field Details

*No entries found.*

### Constructor Details

#### public RMIJRMPServerImpl​(int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf,

Map
<
String
,​?> env)
throws
IOException

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

**Parameters:**
- port

- the port on which this object and the

RMIConnectionImpl

objects it creates will be exported. Can be
zero, to indicate any available port.
- csf

- the client socket factory for the created RMI
objects. Can be null.
- ssf

- the server socket factory for the created RMI
objects. Can be null.
- env

- the environment map. Can be null.

**Throws:**
- IOException

- if the

RMIServer

object
cannot be created.
- IllegalArgumentException

- if

port

is
negative.

---

### Method Details

#### public
Remote
toStub()
throws
IOException

Returns a serializable stub for this

RMIServer

object.

**Specified by:**
- toStub

in class

RMIServerImpl

**Returns:**
- a serializable stub.

**Throws:**
- IOException

- if the stub cannot be obtained - e.g the
RMIJRMPServerImpl has not been exported yet.

---

#### protected
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException

Creates a new client connection as an RMI object exported
through JRMP. The port and socket factories for the new

RMIConnection

object are the ones supplied
to the

RMIJRMPServerImpl

constructor.

**Specified by:**
- makeClient

in class

RMIServerImpl

**Parameters:**
- connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different id. The behavior is unspecified if this parameter is
null.
- subject

- the authenticated subject. Can be null.

**Returns:**
- the newly-created

RMIConnection

.

**Throws:**
- IOException

- if the new

RMIConnection

object cannot be created or exported.

---

#### protected void closeServer()
throws
IOException

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object. After returning from this method, the
connector server must not accept any new connections.

**Specified by:**
- closeServer

in class

RMIServerImpl

**Throws:**
- IOException

- if the attempt to close the connector
server failed.

---

### Additional Sections

#### Class RMIJRMPServerImpl

java.lang.Object

- javax.management.remote.rmi.RMIServerImpl
- - javax.management.remote.rmi.RMIJRMPServerImpl

javax.management.remote.rmi.RMIServerImpl

- javax.management.remote.rmi.RMIJRMPServerImpl

javax.management.remote.rmi.RMIJRMPServerImpl

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Remote

,

RMIServer

```java
public class
RMIJRMPServerImpl

extends
RMIServerImpl
```

An

RMIServer

object that is exported through JRMP and that
creates client connections as RMI objects exported through JRMP.
User code does not usually reference this class directly.

**Since:** 1.5
**See Also:** RMIServerImpl

public class

RMIJRMPServerImpl

extends

RMIServerImpl

An

RMIServer

object that is exported through JRMP and that
creates client connections as RMI objects exported through JRMP.
User code does not usually reference this class directly.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMIJRMPServerImpl

​(int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf,

Map

<

String

,​?> env)

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

closeServer

()

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object.

protected

RMIConnection

makeClient

​(

String

connectionId,

Subject

subject)

Creates a new client connection as an RMI object exported
through JRMP.

Remote

toStub

()

Returns a serializable stub for this

RMIServer

object.

- Methods declared in class javax.management.remote.rmi.

RMIServerImpl

clientClosed

,

close

,

closeClient

,

export

,

getDefaultClassLoader

,

getMBeanServer

,

getProtocol

,

newClient

,

setDefaultClassLoader

,

setMBeanServer

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

- Methods declared in interface javax.management.remote.rmi.

RMIServer

getVersion

Constructor Summary

Constructors

Constructor

Description

RMIJRMPServerImpl

​(int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf,

Map

<

String

,​?> env)

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

---

#### Constructor Summary

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

closeServer

()

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object.

protected

RMIConnection

makeClient

​(

String

connectionId,

Subject

subject)

Creates a new client connection as an RMI object exported
through JRMP.

Remote

toStub

()

Returns a serializable stub for this

RMIServer

object.

- Methods declared in class javax.management.remote.rmi.

RMIServerImpl

clientClosed

,

close

,

closeClient

,

export

,

getDefaultClassLoader

,

getMBeanServer

,

getProtocol

,

newClient

,

setDefaultClassLoader

,

setMBeanServer

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

- Methods declared in interface javax.management.remote.rmi.

RMIServer

getVersion

---

#### Method Summary

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object.

Creates a new client connection as an RMI object exported
through JRMP.

Returns a serializable stub for this

RMIServer

object.

Methods declared in class javax.management.remote.rmi.

RMIServerImpl

clientClosed

,

close

,

closeClient

,

export

,

getDefaultClassLoader

,

getMBeanServer

,

getProtocol

,

newClient

,

setDefaultClassLoader

,

setMBeanServer

---

#### Methods declared in class javax.management.remote.rmi. RMIServerImpl

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

Methods declared in interface javax.management.remote.rmi.

RMIServer

getVersion

---

#### Methods declared in interface javax.management.remote.rmi. RMIServer

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RMIJRMPServerImpl

```java
public RMIJRMPServerImpl​(int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf,

Map
<
String
,​?> env)
throws
IOException
```

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

**Parameters:** port

- the port on which this object and the

RMIConnectionImpl

objects it creates will be exported. Can be
zero, to indicate any available port.
**Parameters:** csf

- the client socket factory for the created RMI
objects. Can be null.
**Parameters:** ssf

- the server socket factory for the created RMI
objects. Can be null.
**Parameters:** env

- the environment map. Can be null.
**Throws:** IOException

- if the

RMIServer

object
cannot be created.
**Throws:** IllegalArgumentException

- if

port

is
negative.

============ METHOD DETAIL ==========

- Method Detail

- toStub

```java
public
Remote
toStub()
throws
IOException
```

Returns a serializable stub for this

RMIServer

object.

**Specified by:** toStub

in class

RMIServerImpl
**Returns:** a serializable stub.
**Throws:** IOException

- if the stub cannot be obtained - e.g the
RMIJRMPServerImpl has not been exported yet.

- makeClient

```java
protected
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException
```

Creates a new client connection as an RMI object exported
through JRMP. The port and socket factories for the new

RMIConnection

object are the ones supplied
to the

RMIJRMPServerImpl

constructor.

**Specified by:** makeClient

in class

RMIServerImpl
**Parameters:** connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different id. The behavior is unspecified if this parameter is
null.
**Parameters:** subject

- the authenticated subject. Can be null.
**Returns:** the newly-created

RMIConnection

.
**Throws:** IOException

- if the new

RMIConnection

object cannot be created or exported.

- closeServer

```java
protected void closeServer()
throws
IOException
```

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object. After returning from this method, the
connector server must not accept any new connections.

**Specified by:** closeServer

in class

RMIServerImpl
**Throws:** IOException

- if the attempt to close the connector
server failed.

Constructor Detail

- RMIJRMPServerImpl

```java
public RMIJRMPServerImpl​(int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf,

Map
<
String
,​?> env)
throws
IOException
```

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

**Parameters:** port

- the port on which this object and the

RMIConnectionImpl

objects it creates will be exported. Can be
zero, to indicate any available port.
**Parameters:** csf

- the client socket factory for the created RMI
objects. Can be null.
**Parameters:** ssf

- the server socket factory for the created RMI
objects. Can be null.
**Parameters:** env

- the environment map. Can be null.
**Throws:** IOException

- if the

RMIServer

object
cannot be created.
**Throws:** IllegalArgumentException

- if

port

is
negative.

---

#### Constructor Detail

RMIJRMPServerImpl

```java
public RMIJRMPServerImpl​(int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf,

Map
<
String
,​?> env)
throws
IOException
```

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

**Parameters:** port

- the port on which this object and the

RMIConnectionImpl

objects it creates will be exported. Can be
zero, to indicate any available port.
**Parameters:** csf

- the client socket factory for the created RMI
objects. Can be null.
**Parameters:** ssf

- the server socket factory for the created RMI
objects. Can be null.
**Parameters:** env

- the environment map. Can be null.
**Throws:** IOException

- if the

RMIServer

object
cannot be created.
**Throws:** IllegalArgumentException

- if

port

is
negative.

---

#### RMIJRMPServerImpl

public RMIJRMPServerImpl​(int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf,

Map

<

String

,​?> env)
throws

IOException

Creates a new

RMIServer

object that will be exported
on the given port using the given socket factories.

Method Detail

- toStub

```java
public
Remote
toStub()
throws
IOException
```

Returns a serializable stub for this

RMIServer

object.

**Specified by:** toStub

in class

RMIServerImpl
**Returns:** a serializable stub.
**Throws:** IOException

- if the stub cannot be obtained - e.g the
RMIJRMPServerImpl has not been exported yet.

- makeClient

```java
protected
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException
```

Creates a new client connection as an RMI object exported
through JRMP. The port and socket factories for the new

RMIConnection

object are the ones supplied
to the

RMIJRMPServerImpl

constructor.

**Specified by:** makeClient

in class

RMIServerImpl
**Parameters:** connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different id. The behavior is unspecified if this parameter is
null.
**Parameters:** subject

- the authenticated subject. Can be null.
**Returns:** the newly-created

RMIConnection

.
**Throws:** IOException

- if the new

RMIConnection

object cannot be created or exported.

- closeServer

```java
protected void closeServer()
throws
IOException
```

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object. After returning from this method, the
connector server must not accept any new connections.

**Specified by:** closeServer

in class

RMIServerImpl
**Throws:** IOException

- if the attempt to close the connector
server failed.

---

#### Method Detail

toStub

```java
public
Remote
toStub()
throws
IOException
```

Returns a serializable stub for this

RMIServer

object.

**Specified by:** toStub

in class

RMIServerImpl
**Returns:** a serializable stub.
**Throws:** IOException

- if the stub cannot be obtained - e.g the
RMIJRMPServerImpl has not been exported yet.

---

#### toStub

public

Remote

toStub()
throws

IOException

Returns a serializable stub for this

RMIServer

object.

makeClient

```java
protected
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException
```

Creates a new client connection as an RMI object exported
through JRMP. The port and socket factories for the new

RMIConnection

object are the ones supplied
to the

RMIJRMPServerImpl

constructor.

**Specified by:** makeClient

in class

RMIServerImpl
**Parameters:** connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different id. The behavior is unspecified if this parameter is
null.
**Parameters:** subject

- the authenticated subject. Can be null.
**Returns:** the newly-created

RMIConnection

.
**Throws:** IOException

- if the new

RMIConnection

object cannot be created or exported.

---

#### makeClient

protected

RMIConnection

makeClient​(

String

connectionId,

Subject

subject)
throws

IOException

Creates a new client connection as an RMI object exported
through JRMP. The port and socket factories for the new

RMIConnection

object are the ones supplied
to the

RMIJRMPServerImpl

constructor.

closeServer

```java
protected void closeServer()
throws
IOException
```

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object. After returning from this method, the
connector server must not accept any new connections.

**Specified by:** closeServer

in class

RMIServerImpl
**Throws:** IOException

- if the attempt to close the connector
server failed.

---

#### closeServer

protected void closeServer()
throws

IOException

Called by

RMIServerImpl.close()

to close the connector server by
unexporting this object. After returning from this method, the
connector server must not accept any new connections.

---

