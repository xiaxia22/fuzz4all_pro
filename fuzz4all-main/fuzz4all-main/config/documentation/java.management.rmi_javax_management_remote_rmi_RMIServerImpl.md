# Class RMIServerImpl

**Source:** `java.management.rmi\javax\management\remote\rmi\RMIServerImpl.html`

### Class Description

```java
public abstract class
RMIServerImpl

extends
Object

implements
Closeable
,
RMIServer
```

An RMI object representing a connector server. Remote clients
can make connections using the

newClient(Object)

method. This
method returns an RMI object representing the connection.

User code does not usually reference this class directly.
RMI connection servers are usually created with the class

RMIConnectorServer

. Remote clients usually create connections
either with

JMXConnectorFactory

or by instantiating

RMIConnector

.

This is an abstract class. Concrete subclasses define the
details of the client connection objects.

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

#### public RMIServerImpl​(
Map
<
String
,​?> env)

Constructs a new

RMIServerImpl

.

**Parameters:**
- env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, which is equivalent
to an empty Map.

---

### Method Details

#### protected abstract void export()
throws
IOException

Exports this RMI object.

**Throws:**
- IOException

- if this RMI object cannot be exported.

---

#### public abstract
Remote
toStub()
throws
IOException

Returns a remotable stub for this server object.

**Returns:**
- a remotable stub.

**Throws:**
- IOException

- if the stub cannot be obtained - e.g the
RMIServerImpl has not been exported yet.

---

#### public void setDefaultClassLoader​(
ClassLoader
cl)

Sets the default

ClassLoader

for this connector
server. New client connections will use this classloader.
Existing client connections are unaffected.

**Parameters:**
- cl

- the new

ClassLoader

to be used by this
connector server.

**See Also:**
- getDefaultClassLoader()

---

#### public
ClassLoader
getDefaultClassLoader()

Gets the default

ClassLoader

used by this connector
server.

**Returns:**
- the default

ClassLoader

used by this
connector server.

**See Also:**
- setDefaultClassLoader(java.lang.ClassLoader)

---

#### public void setMBeanServer​(
MBeanServer
mbs)

Sets the

MBeanServer

to which this connector
server is attached. New client connections will interact
with this

MBeanServer

. Existing client connections are
unaffected.

**Parameters:**
- mbs

- the new

MBeanServer

. Can be null, but
new client connections will be refused as long as it is.

**See Also:**
- getMBeanServer()

---

#### public
MBeanServer
getMBeanServer()

The

MBeanServer

to which this connector server
is attached. This is the last value passed to

setMBeanServer(javax.management.MBeanServer)

on this object, or null if that method has
never been called.

**Returns:**
- the

MBeanServer

to which this connector
is attached.

**See Also:**
- setMBeanServer(javax.management.MBeanServer)

---

#### public
RMIConnection
newClient​(
Object
credentials)
throws
IOException

Creates a new client connection. This method calls

makeClient

and adds the returned client connection
object to an internal list. When this

RMIServerImpl

is shut down via its

close()

method, the

close()

method of each object remaining in the list is called.

The fact that a client connection object is in this internal
list does not prevent it from being garbage collected.

**Specified by:**
- newClient

in interface

RMIServer

**Parameters:**
- credentials

- this object specifies the user-defined
credentials to be passed in to the server in order to
authenticate the caller before creating the

RMIConnection

. Can be null.

**Returns:**
- the newly-created

RMIConnection

. This is
usually the object created by

makeClient

, though
an implementation may choose to wrap that object in another
object implementing

RMIConnection

.

**Throws:**
- IOException

- if the new client object cannot be
created or exported.
- SecurityException

- if the given credentials do not allow
the server to authenticate the user successfully.
- IllegalStateException

- if

getMBeanServer()

is null.

---

#### protected abstract
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException

Creates a new client connection. This method is called by
the public method

newClient(Object)

.

**Parameters:**
- connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different ID. The behavior is unspecified if this parameter is
null.
- subject

- the authenticated subject. Can be null.

**Returns:**
- the newly-created

RMIConnection

.

**Throws:**
- IOException

- if the new client object cannot be
created or exported.

---

#### protected abstract void closeClient​(
RMIConnection
client)
throws
IOException

Closes a client connection made by

makeClient

.

**Parameters:**
- client

- a connection previously returned by

makeClient

on which the

closeClient

method has not previously been called. The behavior is
unspecified if these conditions are violated, including the
case where

client

is null.

**Throws:**
- IOException

- if the client connection cannot be
closed.

---

#### protected abstract
String
getProtocol()

Returns the protocol string for this object. The string is

rmi

for RMI/JRMP.

**Returns:**
- the protocol string for this object.

---

#### protected void clientClosed​(
RMIConnection
client)
throws
IOException

Method called when a client connection created by

makeClient

is closed. A subclass that defines

makeClient

must arrange for this method to be
called when the resultant object's

close

method is called. This enables it to be removed from
the

RMIServerImpl

's list of connections. It is
not an error for

client

not to be in that
list.

After removing

client

from the list of
connections, this method calls

closeClient(client)

.

**Parameters:**
- client

- the client connection that has been closed.

**Throws:**
- IOException

- if

closeClient(javax.management.remote.rmi.RMIConnection)

throws this
exception.
- NullPointerException

- if

client

is null.

---

#### public void close()
throws
IOException

Closes this connection server. This method first calls the

closeServer()

method so that no new client connections
will be accepted. Then, for each remaining

RMIConnection

object returned by

makeClient

, its

close

method is
called.

The behavior when this method is called more than once is
unspecified.

If

closeServer()

throws an

IOException

, the individual connections are
nevertheless closed, and then the

IOException

is
thrown from this method.

If

closeServer()

returns normally but one or more
of the individual connections throws an

IOException

, then, after closing all the
connections, one of those

IOException

s is thrown
from this method. If more than one connection throws an

IOException

, it is unspecified which one is thrown
from this method.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Throws:**
- IOException

- if

closeServer()

or one of the

RMIConnection.close()

calls threw

IOException

.

---

#### protected abstract void closeServer()
throws
IOException

Called by

close()

to close the connector server.
After returning from this method, the connector server must
not accept any new connections.

**Throws:**
- IOException

- if the attempt to close the connector
server failed.

---

### Additional Sections

#### Class RMIServerImpl

java.lang.Object

- javax.management.remote.rmi.RMIServerImpl

javax.management.remote.rmi.RMIServerImpl

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Remote

,

RMIServer

**Direct Known Subclasses:** RMIIIOPServerImpl

,

RMIJRMPServerImpl

```java
public abstract class
RMIServerImpl

extends
Object

implements
Closeable
,
RMIServer
```

An RMI object representing a connector server. Remote clients
can make connections using the

newClient(Object)

method. This
method returns an RMI object representing the connection.

User code does not usually reference this class directly.
RMI connection servers are usually created with the class

RMIConnectorServer

. Remote clients usually create connections
either with

JMXConnectorFactory

or by instantiating

RMIConnector

.

This is an abstract class. Concrete subclasses define the
details of the client connection objects.

**Since:** 1.5

public abstract class

RMIServerImpl

extends

Object

implements

Closeable

,

RMIServer

An RMI object representing a connector server. Remote clients
can make connections using the

newClient(Object)

method. This
method returns an RMI object representing the connection.

User code does not usually reference this class directly.
RMI connection servers are usually created with the class

RMIConnectorServer

. Remote clients usually create connections
either with

JMXConnectorFactory

or by instantiating

RMIConnector

.

This is an abstract class. Concrete subclasses define the
details of the client connection objects.

An RMI object representing a connector server. Remote clients
can make connections using the

newClient(Object)

method. This
method returns an RMI object representing the connection.

User code does not usually reference this class directly.
RMI connection servers are usually created with the class

RMIConnectorServer

. Remote clients usually create connections
either with

JMXConnectorFactory

or by instantiating

RMIConnector

.

This is an abstract class. Concrete subclasses define the
details of the client connection objects.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMIServerImpl

​(

Map

<

String

,​?> env)

Constructs a new

RMIServerImpl

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

clientClosed

​(

RMIConnection

client)

Method called when a client connection created by

makeClient

is closed.

void

close

()

Closes this connection server.

protected abstract void

closeClient

​(

RMIConnection

client)

Closes a client connection made by

makeClient

.

protected abstract void

closeServer

()

Called by

close()

to close the connector server.

protected abstract void

export

()

Exports this RMI object.

ClassLoader

getDefaultClassLoader

()

Gets the default

ClassLoader

used by this connector
server.

MBeanServer

getMBeanServer

()

The

MBeanServer

to which this connector server
is attached.

protected abstract

String

getProtocol

()

Returns the protocol string for this object.

protected abstract

RMIConnection

makeClient

​(

String

connectionId,

Subject

subject)

Creates a new client connection.

RMIConnection

newClient

​(

Object

credentials)

Creates a new client connection.

void

setDefaultClassLoader

​(

ClassLoader

cl)

Sets the default

ClassLoader

for this connector
server.

void

setMBeanServer

​(

MBeanServer

mbs)

Sets the

MBeanServer

to which this connector
server is attached.

abstract

Remote

toStub

()

Returns a remotable stub for this server object.

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

RMIServerImpl

​(

Map

<

String

,​?> env)

Constructs a new

RMIServerImpl

.

---

#### Constructor Summary

Constructs a new

RMIServerImpl

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

clientClosed

​(

RMIConnection

client)

Method called when a client connection created by

makeClient

is closed.

void

close

()

Closes this connection server.

protected abstract void

closeClient

​(

RMIConnection

client)

Closes a client connection made by

makeClient

.

protected abstract void

closeServer

()

Called by

close()

to close the connector server.

protected abstract void

export

()

Exports this RMI object.

ClassLoader

getDefaultClassLoader

()

Gets the default

ClassLoader

used by this connector
server.

MBeanServer

getMBeanServer

()

The

MBeanServer

to which this connector server
is attached.

protected abstract

String

getProtocol

()

Returns the protocol string for this object.

protected abstract

RMIConnection

makeClient

​(

String

connectionId,

Subject

subject)

Creates a new client connection.

RMIConnection

newClient

​(

Object

credentials)

Creates a new client connection.

void

setDefaultClassLoader

​(

ClassLoader

cl)

Sets the default

ClassLoader

for this connector
server.

void

setMBeanServer

​(

MBeanServer

mbs)

Sets the

MBeanServer

to which this connector
server is attached.

abstract

Remote

toStub

()

Returns a remotable stub for this server object.

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

Method called when a client connection created by

makeClient

is closed.

Closes this connection server.

Closes a client connection made by

makeClient

.

Called by

close()

to close the connector server.

Exports this RMI object.

Gets the default

ClassLoader

used by this connector
server.

The

MBeanServer

to which this connector server
is attached.

Returns the protocol string for this object.

Creates a new client connection.

Sets the default

ClassLoader

for this connector
server.

Sets the

MBeanServer

to which this connector
server is attached.

Returns a remotable stub for this server object.

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

- RMIServerImpl

```java
public RMIServerImpl​(
Map
<
String
,​?> env)
```

Constructs a new

RMIServerImpl

.

**Parameters:** env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, which is equivalent
to an empty Map.

============ METHOD DETAIL ==========

- Method Detail

- export

```java
protected abstract void export()
throws
IOException
```

Exports this RMI object.

**Throws:** IOException

- if this RMI object cannot be exported.

- toStub

```java
public abstract
Remote
toStub()
throws
IOException
```

Returns a remotable stub for this server object.

**Returns:** a remotable stub.
**Throws:** IOException

- if the stub cannot be obtained - e.g the
RMIServerImpl has not been exported yet.

- setDefaultClassLoader

```java
public void setDefaultClassLoader​(
ClassLoader
cl)
```

Sets the default

ClassLoader

for this connector
server. New client connections will use this classloader.
Existing client connections are unaffected.

**Parameters:** cl

- the new

ClassLoader

to be used by this
connector server.
**See Also:** getDefaultClassLoader()

- getDefaultClassLoader

```java
public
ClassLoader
getDefaultClassLoader()
```

Gets the default

ClassLoader

used by this connector
server.

**Returns:** the default

ClassLoader

used by this
connector server.
**See Also:** setDefaultClassLoader(java.lang.ClassLoader)

- setMBeanServer

```java
public void setMBeanServer​(
MBeanServer
mbs)
```

Sets the

MBeanServer

to which this connector
server is attached. New client connections will interact
with this

MBeanServer

. Existing client connections are
unaffected.

**Parameters:** mbs

- the new

MBeanServer

. Can be null, but
new client connections will be refused as long as it is.
**See Also:** getMBeanServer()

- getMBeanServer

```java
public
MBeanServer
getMBeanServer()
```

The

MBeanServer

to which this connector server
is attached. This is the last value passed to

setMBeanServer(javax.management.MBeanServer)

on this object, or null if that method has
never been called.

**Returns:** the

MBeanServer

to which this connector
is attached.
**See Also:** setMBeanServer(javax.management.MBeanServer)

- newClient

```java
public
RMIConnection
newClient​(
Object
credentials)
throws
IOException
```

Creates a new client connection. This method calls

makeClient

and adds the returned client connection
object to an internal list. When this

RMIServerImpl

is shut down via its

close()

method, the

close()

method of each object remaining in the list is called.

The fact that a client connection object is in this internal
list does not prevent it from being garbage collected.

**Specified by:** newClient

in interface

RMIServer
**Parameters:** credentials

- this object specifies the user-defined
credentials to be passed in to the server in order to
authenticate the caller before creating the

RMIConnection

. Can be null.
**Returns:** the newly-created

RMIConnection

. This is
usually the object created by

makeClient

, though
an implementation may choose to wrap that object in another
object implementing

RMIConnection

.
**Throws:** IOException

- if the new client object cannot be
created or exported.
**Throws:** SecurityException

- if the given credentials do not allow
the server to authenticate the user successfully.
**Throws:** IllegalStateException

- if

getMBeanServer()

is null.

- makeClient

```java
protected abstract
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException
```

Creates a new client connection. This method is called by
the public method

newClient(Object)

.

**Parameters:** connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different ID. The behavior is unspecified if this parameter is
null.
**Parameters:** subject

- the authenticated subject. Can be null.
**Returns:** the newly-created

RMIConnection

.
**Throws:** IOException

- if the new client object cannot be
created or exported.

- closeClient

```java
protected abstract void closeClient​(
RMIConnection
client)
throws
IOException
```

Closes a client connection made by

makeClient

.

**Parameters:** client

- a connection previously returned by

makeClient

on which the

closeClient

method has not previously been called. The behavior is
unspecified if these conditions are violated, including the
case where

client

is null.
**Throws:** IOException

- if the client connection cannot be
closed.

- getProtocol

```java
protected abstract
String
getProtocol()
```

Returns the protocol string for this object. The string is

rmi

for RMI/JRMP.

**Returns:** the protocol string for this object.

- clientClosed

```java
protected void clientClosed​(
RMIConnection
client)
throws
IOException
```

Method called when a client connection created by

makeClient

is closed. A subclass that defines

makeClient

must arrange for this method to be
called when the resultant object's

close

method is called. This enables it to be removed from
the

RMIServerImpl

's list of connections. It is
not an error for

client

not to be in that
list.

After removing

client

from the list of
connections, this method calls

closeClient(client)

.

**Parameters:** client

- the client connection that has been closed.
**Throws:** IOException

- if

closeClient(javax.management.remote.rmi.RMIConnection)

throws this
exception.
**Throws:** NullPointerException

- if

client

is null.

- close

```java
public void close()
throws
IOException
```

Closes this connection server. This method first calls the

closeServer()

method so that no new client connections
will be accepted. Then, for each remaining

RMIConnection

object returned by

makeClient

, its

close

method is
called.

The behavior when this method is called more than once is
unspecified.

If

closeServer()

throws an

IOException

, the individual connections are
nevertheless closed, and then the

IOException

is
thrown from this method.

If

closeServer()

returns normally but one or more
of the individual connections throws an

IOException

, then, after closing all the
connections, one of those

IOException

s is thrown
from this method. If more than one connection throws an

IOException

, it is unspecified which one is thrown
from this method.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if

closeServer()

or one of the

RMIConnection.close()

calls threw

IOException

.

- closeServer

```java
protected abstract void closeServer()
throws
IOException
```

Called by

close()

to close the connector server.
After returning from this method, the connector server must
not accept any new connections.

**Throws:** IOException

- if the attempt to close the connector
server failed.

Constructor Detail

- RMIServerImpl

```java
public RMIServerImpl​(
Map
<
String
,​?> env)
```

Constructs a new

RMIServerImpl

.

**Parameters:** env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, which is equivalent
to an empty Map.

---

#### Constructor Detail

RMIServerImpl

```java
public RMIServerImpl​(
Map
<
String
,​?> env)
```

Constructs a new

RMIServerImpl

.

**Parameters:** env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, which is equivalent
to an empty Map.

---

#### RMIServerImpl

public RMIServerImpl​(

Map

<

String

,​?> env)

Constructs a new

RMIServerImpl

.

Method Detail

- export

```java
protected abstract void export()
throws
IOException
```

Exports this RMI object.

**Throws:** IOException

- if this RMI object cannot be exported.

- toStub

```java
public abstract
Remote
toStub()
throws
IOException
```

Returns a remotable stub for this server object.

**Returns:** a remotable stub.
**Throws:** IOException

- if the stub cannot be obtained - e.g the
RMIServerImpl has not been exported yet.

- setDefaultClassLoader

```java
public void setDefaultClassLoader​(
ClassLoader
cl)
```

Sets the default

ClassLoader

for this connector
server. New client connections will use this classloader.
Existing client connections are unaffected.

**Parameters:** cl

- the new

ClassLoader

to be used by this
connector server.
**See Also:** getDefaultClassLoader()

- getDefaultClassLoader

```java
public
ClassLoader
getDefaultClassLoader()
```

Gets the default

ClassLoader

used by this connector
server.

**Returns:** the default

ClassLoader

used by this
connector server.
**See Also:** setDefaultClassLoader(java.lang.ClassLoader)

- setMBeanServer

```java
public void setMBeanServer​(
MBeanServer
mbs)
```

Sets the

MBeanServer

to which this connector
server is attached. New client connections will interact
with this

MBeanServer

. Existing client connections are
unaffected.

**Parameters:** mbs

- the new

MBeanServer

. Can be null, but
new client connections will be refused as long as it is.
**See Also:** getMBeanServer()

- getMBeanServer

```java
public
MBeanServer
getMBeanServer()
```

The

MBeanServer

to which this connector server
is attached. This is the last value passed to

setMBeanServer(javax.management.MBeanServer)

on this object, or null if that method has
never been called.

**Returns:** the

MBeanServer

to which this connector
is attached.
**See Also:** setMBeanServer(javax.management.MBeanServer)

- newClient

```java
public
RMIConnection
newClient​(
Object
credentials)
throws
IOException
```

Creates a new client connection. This method calls

makeClient

and adds the returned client connection
object to an internal list. When this

RMIServerImpl

is shut down via its

close()

method, the

close()

method of each object remaining in the list is called.

The fact that a client connection object is in this internal
list does not prevent it from being garbage collected.

**Specified by:** newClient

in interface

RMIServer
**Parameters:** credentials

- this object specifies the user-defined
credentials to be passed in to the server in order to
authenticate the caller before creating the

RMIConnection

. Can be null.
**Returns:** the newly-created

RMIConnection

. This is
usually the object created by

makeClient

, though
an implementation may choose to wrap that object in another
object implementing

RMIConnection

.
**Throws:** IOException

- if the new client object cannot be
created or exported.
**Throws:** SecurityException

- if the given credentials do not allow
the server to authenticate the user successfully.
**Throws:** IllegalStateException

- if

getMBeanServer()

is null.

- makeClient

```java
protected abstract
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException
```

Creates a new client connection. This method is called by
the public method

newClient(Object)

.

**Parameters:** connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different ID. The behavior is unspecified if this parameter is
null.
**Parameters:** subject

- the authenticated subject. Can be null.
**Returns:** the newly-created

RMIConnection

.
**Throws:** IOException

- if the new client object cannot be
created or exported.

- closeClient

```java
protected abstract void closeClient​(
RMIConnection
client)
throws
IOException
```

Closes a client connection made by

makeClient

.

**Parameters:** client

- a connection previously returned by

makeClient

on which the

closeClient

method has not previously been called. The behavior is
unspecified if these conditions are violated, including the
case where

client

is null.
**Throws:** IOException

- if the client connection cannot be
closed.

- getProtocol

```java
protected abstract
String
getProtocol()
```

Returns the protocol string for this object. The string is

rmi

for RMI/JRMP.

**Returns:** the protocol string for this object.

- clientClosed

```java
protected void clientClosed​(
RMIConnection
client)
throws
IOException
```

Method called when a client connection created by

makeClient

is closed. A subclass that defines

makeClient

must arrange for this method to be
called when the resultant object's

close

method is called. This enables it to be removed from
the

RMIServerImpl

's list of connections. It is
not an error for

client

not to be in that
list.

After removing

client

from the list of
connections, this method calls

closeClient(client)

.

**Parameters:** client

- the client connection that has been closed.
**Throws:** IOException

- if

closeClient(javax.management.remote.rmi.RMIConnection)

throws this
exception.
**Throws:** NullPointerException

- if

client

is null.

- close

```java
public void close()
throws
IOException
```

Closes this connection server. This method first calls the

closeServer()

method so that no new client connections
will be accepted. Then, for each remaining

RMIConnection

object returned by

makeClient

, its

close

method is
called.

The behavior when this method is called more than once is
unspecified.

If

closeServer()

throws an

IOException

, the individual connections are
nevertheless closed, and then the

IOException

is
thrown from this method.

If

closeServer()

returns normally but one or more
of the individual connections throws an

IOException

, then, after closing all the
connections, one of those

IOException

s is thrown
from this method. If more than one connection throws an

IOException

, it is unspecified which one is thrown
from this method.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if

closeServer()

or one of the

RMIConnection.close()

calls threw

IOException

.

- closeServer

```java
protected abstract void closeServer()
throws
IOException
```

Called by

close()

to close the connector server.
After returning from this method, the connector server must
not accept any new connections.

**Throws:** IOException

- if the attempt to close the connector
server failed.

---

#### Method Detail

export

```java
protected abstract void export()
throws
IOException
```

Exports this RMI object.

**Throws:** IOException

- if this RMI object cannot be exported.

---

#### export

protected abstract void export()
throws

IOException

Exports this RMI object.

toStub

```java
public abstract
Remote
toStub()
throws
IOException
```

Returns a remotable stub for this server object.

**Returns:** a remotable stub.
**Throws:** IOException

- if the stub cannot be obtained - e.g the
RMIServerImpl has not been exported yet.

---

#### toStub

public abstract

Remote

toStub()
throws

IOException

Returns a remotable stub for this server object.

setDefaultClassLoader

```java
public void setDefaultClassLoader​(
ClassLoader
cl)
```

Sets the default

ClassLoader

for this connector
server. New client connections will use this classloader.
Existing client connections are unaffected.

**Parameters:** cl

- the new

ClassLoader

to be used by this
connector server.
**See Also:** getDefaultClassLoader()

---

#### setDefaultClassLoader

public void setDefaultClassLoader​(

ClassLoader

cl)

Sets the default

ClassLoader

for this connector
server. New client connections will use this classloader.
Existing client connections are unaffected.

getDefaultClassLoader

```java
public
ClassLoader
getDefaultClassLoader()
```

Gets the default

ClassLoader

used by this connector
server.

**Returns:** the default

ClassLoader

used by this
connector server.
**See Also:** setDefaultClassLoader(java.lang.ClassLoader)

---

#### getDefaultClassLoader

public

ClassLoader

getDefaultClassLoader()

Gets the default

ClassLoader

used by this connector
server.

setMBeanServer

```java
public void setMBeanServer​(
MBeanServer
mbs)
```

Sets the

MBeanServer

to which this connector
server is attached. New client connections will interact
with this

MBeanServer

. Existing client connections are
unaffected.

**Parameters:** mbs

- the new

MBeanServer

. Can be null, but
new client connections will be refused as long as it is.
**See Also:** getMBeanServer()

---

#### setMBeanServer

public void setMBeanServer​(

MBeanServer

mbs)

Sets the

MBeanServer

to which this connector
server is attached. New client connections will interact
with this

MBeanServer

. Existing client connections are
unaffected.

getMBeanServer

```java
public
MBeanServer
getMBeanServer()
```

The

MBeanServer

to which this connector server
is attached. This is the last value passed to

setMBeanServer(javax.management.MBeanServer)

on this object, or null if that method has
never been called.

**Returns:** the

MBeanServer

to which this connector
is attached.
**See Also:** setMBeanServer(javax.management.MBeanServer)

---

#### getMBeanServer

public

MBeanServer

getMBeanServer()

The

MBeanServer

to which this connector server
is attached. This is the last value passed to

setMBeanServer(javax.management.MBeanServer)

on this object, or null if that method has
never been called.

newClient

```java
public
RMIConnection
newClient​(
Object
credentials)
throws
IOException
```

Creates a new client connection. This method calls

makeClient

and adds the returned client connection
object to an internal list. When this

RMIServerImpl

is shut down via its

close()

method, the

close()

method of each object remaining in the list is called.

The fact that a client connection object is in this internal
list does not prevent it from being garbage collected.

**Specified by:** newClient

in interface

RMIServer
**Parameters:** credentials

- this object specifies the user-defined
credentials to be passed in to the server in order to
authenticate the caller before creating the

RMIConnection

. Can be null.
**Returns:** the newly-created

RMIConnection

. This is
usually the object created by

makeClient

, though
an implementation may choose to wrap that object in another
object implementing

RMIConnection

.
**Throws:** IOException

- if the new client object cannot be
created or exported.
**Throws:** SecurityException

- if the given credentials do not allow
the server to authenticate the user successfully.
**Throws:** IllegalStateException

- if

getMBeanServer()

is null.

---

#### newClient

public

RMIConnection

newClient​(

Object

credentials)
throws

IOException

Creates a new client connection. This method calls

makeClient

and adds the returned client connection
object to an internal list. When this

RMIServerImpl

is shut down via its

close()

method, the

close()

method of each object remaining in the list is called.

The fact that a client connection object is in this internal
list does not prevent it from being garbage collected.

Creates a new client connection. This method calls

makeClient

and adds the returned client connection
object to an internal list. When this

RMIServerImpl

is shut down via its

close()

method, the

close()

method of each object remaining in the list is called.

The fact that a client connection object is in this internal
list does not prevent it from being garbage collected.

makeClient

```java
protected abstract
RMIConnection
makeClient​(
String
connectionId,

Subject
subject)
throws
IOException
```

Creates a new client connection. This method is called by
the public method

newClient(Object)

.

**Parameters:** connectionId

- the ID of the new connection. Every
connection opened by this connector server will have a
different ID. The behavior is unspecified if this parameter is
null.
**Parameters:** subject

- the authenticated subject. Can be null.
**Returns:** the newly-created

RMIConnection

.
**Throws:** IOException

- if the new client object cannot be
created or exported.

---

#### makeClient

protected abstract

RMIConnection

makeClient​(

String

connectionId,

Subject

subject)
throws

IOException

Creates a new client connection. This method is called by
the public method

newClient(Object)

.

closeClient

```java
protected abstract void closeClient​(
RMIConnection
client)
throws
IOException
```

Closes a client connection made by

makeClient

.

**Parameters:** client

- a connection previously returned by

makeClient

on which the

closeClient

method has not previously been called. The behavior is
unspecified if these conditions are violated, including the
case where

client

is null.
**Throws:** IOException

- if the client connection cannot be
closed.

---

#### closeClient

protected abstract void closeClient​(

RMIConnection

client)
throws

IOException

Closes a client connection made by

makeClient

.

getProtocol

```java
protected abstract
String
getProtocol()
```

Returns the protocol string for this object. The string is

rmi

for RMI/JRMP.

**Returns:** the protocol string for this object.

---

#### getProtocol

protected abstract

String

getProtocol()

Returns the protocol string for this object. The string is

rmi

for RMI/JRMP.

clientClosed

```java
protected void clientClosed​(
RMIConnection
client)
throws
IOException
```

Method called when a client connection created by

makeClient

is closed. A subclass that defines

makeClient

must arrange for this method to be
called when the resultant object's

close

method is called. This enables it to be removed from
the

RMIServerImpl

's list of connections. It is
not an error for

client

not to be in that
list.

After removing

client

from the list of
connections, this method calls

closeClient(client)

.

**Parameters:** client

- the client connection that has been closed.
**Throws:** IOException

- if

closeClient(javax.management.remote.rmi.RMIConnection)

throws this
exception.
**Throws:** NullPointerException

- if

client

is null.

---

#### clientClosed

protected void clientClosed​(

RMIConnection

client)
throws

IOException

Method called when a client connection created by

makeClient

is closed. A subclass that defines

makeClient

must arrange for this method to be
called when the resultant object's

close

method is called. This enables it to be removed from
the

RMIServerImpl

's list of connections. It is
not an error for

client

not to be in that
list.

After removing

client

from the list of
connections, this method calls

closeClient(client)

.

Method called when a client connection created by

makeClient

is closed. A subclass that defines

makeClient

must arrange for this method to be
called when the resultant object's

close

method is called. This enables it to be removed from
the

RMIServerImpl

's list of connections. It is
not an error for

client

not to be in that
list.

After removing

client

from the list of
connections, this method calls

closeClient(client)

.

close

```java
public void close()
throws
IOException
```

Closes this connection server. This method first calls the

closeServer()

method so that no new client connections
will be accepted. Then, for each remaining

RMIConnection

object returned by

makeClient

, its

close

method is
called.

The behavior when this method is called more than once is
unspecified.

If

closeServer()

throws an

IOException

, the individual connections are
nevertheless closed, and then the

IOException

is
thrown from this method.

If

closeServer()

returns normally but one or more
of the individual connections throws an

IOException

, then, after closing all the
connections, one of those

IOException

s is thrown
from this method. If more than one connection throws an

IOException

, it is unspecified which one is thrown
from this method.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if

closeServer()

or one of the

RMIConnection.close()

calls threw

IOException

.

---

#### close

public void close()
throws

IOException

Closes this connection server. This method first calls the

closeServer()

method so that no new client connections
will be accepted. Then, for each remaining

RMIConnection

object returned by

makeClient

, its

close

method is
called.

The behavior when this method is called more than once is
unspecified.

If

closeServer()

throws an

IOException

, the individual connections are
nevertheless closed, and then the

IOException

is
thrown from this method.

If

closeServer()

returns normally but one or more
of the individual connections throws an

IOException

, then, after closing all the
connections, one of those

IOException

s is thrown
from this method. If more than one connection throws an

IOException

, it is unspecified which one is thrown
from this method.

Closes this connection server. This method first calls the

closeServer()

method so that no new client connections
will be accepted. Then, for each remaining

RMIConnection

object returned by

makeClient

, its

close

method is
called.

The behavior when this method is called more than once is
unspecified.

If

closeServer()

throws an

IOException

, the individual connections are
nevertheless closed, and then the

IOException

is
thrown from this method.

If

closeServer()

returns normally but one or more
of the individual connections throws an

IOException

, then, after closing all the
connections, one of those

IOException

s is thrown
from this method. If more than one connection throws an

IOException

, it is unspecified which one is thrown
from this method.

closeServer

```java
protected abstract void closeServer()
throws
IOException
```

Called by

close()

to close the connector server.
After returning from this method, the connector server must
not accept any new connections.

**Throws:** IOException

- if the attempt to close the connector
server failed.

---

#### closeServer

protected abstract void closeServer()
throws

IOException

Called by

close()

to close the connector server.
After returning from this method, the connector server must
not accept any new connections.

---

