# Interface JMXConnectorServerMBean

**Source:** `java.management\javax\management\remote\JMXConnectorServerMBean.html`

### Class Description

```java
public interface
JMXConnectorServerMBean
```

MBean interface for connector servers. A JMX API connector server
is attached to an MBean server, and establishes connections to that
MBean server for remote clients.

A newly-created connector server is

inactive

, and does
not yet listen for connections. Only when its

start

method has been called does it start listening for connections.

**All Known Implementing Classes:** JMXConnectorServer

,

RMIConnectorServer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void start()
throws
IOException

Activates the connector server, that is, starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

**Throws:**
- IOException

- if it is not possible to start listening
or if the connector server has been stopped.
- IllegalStateException

- if the connector server has
not been attached to an MBean server.

---

#### void stop()
throws
IOException

Deactivates the connector server, that is, stops listening for
client connections. Calling this method will also close all
client connections that were made by this server. After this
method returns, whether normally or with an exception, the
connector server will not create any new client
connections.

Once a connector server has been stopped, it cannot be started
again.

Calling this method when the connector server has already
been stopped has no effect. Calling this method when the
connector server has not yet been started will disable the
connector server object permanently.

If closing a client connection produces an exception, that
exception is not thrown from this method. A

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

is emitted from this MBean
with the connection ID of the connection that could not be
closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

**Throws:**
- IOException

- if the server cannot be closed cleanly.
When this exception is thrown, the server has already attempted
to close all client connections. All client connections are
closed except possibly those that generated exceptions when the
server attempted to close them.

---

#### boolean isActive()

Determines whether the connector server is active. A connector
server starts being active when its

start

method
returns successfully and remains active until either its

stop

method is called or the connector server
fails.

**Returns:**
- true if the connector server is active.

---

#### void setMBeanServerForwarder​(
MBeanServerForwarder
mbsf)

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server. This object will be
supplied as the

MBeanServer

for any new connection
created by this connector server. Existing connections are
unaffected.

This method can be called more than once with different

MBeanServerForwarder

objects. The result is a chain
of forwarders. The last forwarder added is the first in the chain.
In more detail:

- If this connector server is already associated with an

MBeanServer

object, then that object is given to

mbsf.setMBeanServer

. If doing so produces an exception, this
method throws the same exception without any other effect.

If this connector is not already associated with an

MBeanServer

object, or if the

mbsf.setMBeanServer

call just mentioned succeeds,
then

mbsf

becomes this connector server's

MBeanServer

.

**Parameters:**
- mbsf

- the new

MBeanServerForwarder

.

**Throws:**
- IllegalArgumentException

- if the call to

mbsf.setMBeanServer

fails
with

IllegalArgumentException

. This includes the
case where

mbsf

is null.

---

#### String
[] getConnectionIds()

The list of IDs for currently-open connections to this
connector server.

**Returns:**
- a new string array containing the list of IDs. If
there are no currently-open connections, this array will be
empty.

---

#### JMXServiceURL
getAddress()

The address of this connector server.

The address returned may not be the exact original

JMXServiceURL

that was supplied when creating the connector server, since the original
address may not always be complete. For example the port number may be
dynamically allocated when starting the connector server. Instead the
address returned is the actual

JMXServiceURL

of the

JMXConnectorServer

. This is the address that clients supply
to

JMXConnectorFactory.connect(JMXServiceURL)

.

Note that the address returned may be

null

if
the

JMXConnectorServer

is not yet

active

.

**Returns:**
- the address of this connector server, or null if it
does not have one.

---

#### Map
<
String
,​?> getAttributes()

The attributes for this connector server.

**Returns:**
- a read-only map containing the attributes for this
connector server. Attributes whose values are not serializable
are omitted from this map. If there are no serializable
attributes, the returned map is empty.

---

#### JMXConnector
toJMXConnector​(
Map
<
String
,​?> env)
throws
IOException

Returns a client stub for this connector server. A client
stub is a serializable object whose

connect

method can be used to make
one new connection to this connector server.

A given connector need not support the generation of client
stubs. However, the connectors specified by the JMX Remote API do
(JMXMP Connector and RMI Connector).

**Parameters:**
- env

- client connection parameters of the same sort that
can be provided to

JMXConnector.connect(Map)

. Can be null, which is equivalent
to an empty map.

**Returns:**
- a client stub that can be used to make a new connection
to this connector server.

**Throws:**
- UnsupportedOperationException

- if this connector
server does not support the generation of client stubs.
- IllegalStateException

- if the JMXConnectorServer is
not started (see

isActive()

).
- IOException

- if a communications problem means that a
stub cannot be created.

---

### Additional Sections

#### Interface JMXConnectorServerMBean

**All Known Implementing Classes:** JMXConnectorServer

,

RMIConnectorServer

```java
public interface
JMXConnectorServerMBean
```

MBean interface for connector servers. A JMX API connector server
is attached to an MBean server, and establishes connections to that
MBean server for remote clients.

A newly-created connector server is

inactive

, and does
not yet listen for connections. Only when its

start

method has been called does it start listening for connections.

**Since:** 1.5

public interface

JMXConnectorServerMBean

MBean interface for connector servers. A JMX API connector server
is attached to an MBean server, and establishes connections to that
MBean server for remote clients.

A newly-created connector server is

inactive

, and does
not yet listen for connections. Only when its

start

method has been called does it start listening for connections.

MBean interface for connector servers. A JMX API connector server
is attached to an MBean server, and establishes connections to that
MBean server for remote clients.

A newly-created connector server is

inactive

, and does
not yet listen for connections. Only when its

start

method has been called does it start listening for connections.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JMXServiceURL

getAddress

()

The address of this connector server.

Map

<

String

,​?>

getAttributes

()

The attributes for this connector server.

String

[]

getConnectionIds

()

The list of IDs for currently-open connections to this
connector server.

boolean

isActive

()

Determines whether the connector server is active.

void

setMBeanServerForwarder

​(

MBeanServerForwarder

mbsf)

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server.

void

start

()

Activates the connector server, that is, starts listening for
client connections.

void

stop

()

Deactivates the connector server, that is, stops listening for
client connections.

JMXConnector

toJMXConnector

​(

Map

<

String

,​?> env)

Returns a client stub for this connector server.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JMXServiceURL

getAddress

()

The address of this connector server.

Map

<

String

,​?>

getAttributes

()

The attributes for this connector server.

String

[]

getConnectionIds

()

The list of IDs for currently-open connections to this
connector server.

boolean

isActive

()

Determines whether the connector server is active.

void

setMBeanServerForwarder

​(

MBeanServerForwarder

mbsf)

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server.

void

start

()

Activates the connector server, that is, starts listening for
client connections.

void

stop

()

Deactivates the connector server, that is, stops listening for
client connections.

JMXConnector

toJMXConnector

​(

Map

<

String

,​?> env)

Returns a client stub for this connector server.

---

#### Method Summary

The address of this connector server.

The attributes for this connector server.

The list of IDs for currently-open connections to this
connector server.

Determines whether the connector server is active.

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server.

Activates the connector server, that is, starts listening for
client connections.

Deactivates the connector server, that is, stops listening for
client connections.

Returns a client stub for this connector server.

============ METHOD DETAIL ==========

- Method Detail

- start

```java
void start()
throws
IOException
```

Activates the connector server, that is, starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

**Throws:** IOException

- if it is not possible to start listening
or if the connector server has been stopped.
**Throws:** IllegalStateException

- if the connector server has
not been attached to an MBean server.

- stop

```java
void stop()
throws
IOException
```

Deactivates the connector server, that is, stops listening for
client connections. Calling this method will also close all
client connections that were made by this server. After this
method returns, whether normally or with an exception, the
connector server will not create any new client
connections.

Once a connector server has been stopped, it cannot be started
again.

Calling this method when the connector server has already
been stopped has no effect. Calling this method when the
connector server has not yet been started will disable the
connector server object permanently.

If closing a client connection produces an exception, that
exception is not thrown from this method. A

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

is emitted from this MBean
with the connection ID of the connection that could not be
closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

**Throws:** IOException

- if the server cannot be closed cleanly.
When this exception is thrown, the server has already attempted
to close all client connections. All client connections are
closed except possibly those that generated exceptions when the
server attempted to close them.

- isActive

```java
boolean isActive()
```

Determines whether the connector server is active. A connector
server starts being active when its

start

method
returns successfully and remains active until either its

stop

method is called or the connector server
fails.

**Returns:** true if the connector server is active.

- setMBeanServerForwarder

```java
void setMBeanServerForwarder​(
MBeanServerForwarder
mbsf)
```

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server. This object will be
supplied as the

MBeanServer

for any new connection
created by this connector server. Existing connections are
unaffected.

This method can be called more than once with different

MBeanServerForwarder

objects. The result is a chain
of forwarders. The last forwarder added is the first in the chain.
In more detail:

- If this connector server is already associated with an

MBeanServer

object, then that object is given to

mbsf.setMBeanServer

. If doing so produces an exception, this
method throws the same exception without any other effect.

If this connector is not already associated with an

MBeanServer

object, or if the

mbsf.setMBeanServer

call just mentioned succeeds,
then

mbsf

becomes this connector server's

MBeanServer

.

**Parameters:** mbsf

- the new

MBeanServerForwarder

.
**Throws:** IllegalArgumentException

- if the call to

mbsf.setMBeanServer

fails
with

IllegalArgumentException

. This includes the
case where

mbsf

is null.

- getConnectionIds

```java
String
[] getConnectionIds()
```

The list of IDs for currently-open connections to this
connector server.

**Returns:** a new string array containing the list of IDs. If
there are no currently-open connections, this array will be
empty.

- getAddress

```java
JMXServiceURL
getAddress()
```

The address of this connector server.

The address returned may not be the exact original

JMXServiceURL

that was supplied when creating the connector server, since the original
address may not always be complete. For example the port number may be
dynamically allocated when starting the connector server. Instead the
address returned is the actual

JMXServiceURL

of the

JMXConnectorServer

. This is the address that clients supply
to

JMXConnectorFactory.connect(JMXServiceURL)

.

Note that the address returned may be

null

if
the

JMXConnectorServer

is not yet

active

.

**Returns:** the address of this connector server, or null if it
does not have one.

- getAttributes

```java
Map
<
String
,​?> getAttributes()
```

The attributes for this connector server.

**Returns:** a read-only map containing the attributes for this
connector server. Attributes whose values are not serializable
are omitted from this map. If there are no serializable
attributes, the returned map is empty.

- toJMXConnector

```java
JMXConnector
toJMXConnector​(
Map
<
String
,​?> env)
throws
IOException
```

Returns a client stub for this connector server. A client
stub is a serializable object whose

connect

method can be used to make
one new connection to this connector server.

A given connector need not support the generation of client
stubs. However, the connectors specified by the JMX Remote API do
(JMXMP Connector and RMI Connector).

**Parameters:** env

- client connection parameters of the same sort that
can be provided to

JMXConnector.connect(Map)

. Can be null, which is equivalent
to an empty map.
**Returns:** a client stub that can be used to make a new connection
to this connector server.
**Throws:** UnsupportedOperationException

- if this connector
server does not support the generation of client stubs.
**Throws:** IllegalStateException

- if the JMXConnectorServer is
not started (see

isActive()

).
**Throws:** IOException

- if a communications problem means that a
stub cannot be created.

Method Detail

- start

```java
void start()
throws
IOException
```

Activates the connector server, that is, starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

**Throws:** IOException

- if it is not possible to start listening
or if the connector server has been stopped.
**Throws:** IllegalStateException

- if the connector server has
not been attached to an MBean server.

- stop

```java
void stop()
throws
IOException
```

Deactivates the connector server, that is, stops listening for
client connections. Calling this method will also close all
client connections that were made by this server. After this
method returns, whether normally or with an exception, the
connector server will not create any new client
connections.

Once a connector server has been stopped, it cannot be started
again.

Calling this method when the connector server has already
been stopped has no effect. Calling this method when the
connector server has not yet been started will disable the
connector server object permanently.

If closing a client connection produces an exception, that
exception is not thrown from this method. A

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

is emitted from this MBean
with the connection ID of the connection that could not be
closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

**Throws:** IOException

- if the server cannot be closed cleanly.
When this exception is thrown, the server has already attempted
to close all client connections. All client connections are
closed except possibly those that generated exceptions when the
server attempted to close them.

- isActive

```java
boolean isActive()
```

Determines whether the connector server is active. A connector
server starts being active when its

start

method
returns successfully and remains active until either its

stop

method is called or the connector server
fails.

**Returns:** true if the connector server is active.

- setMBeanServerForwarder

```java
void setMBeanServerForwarder​(
MBeanServerForwarder
mbsf)
```

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server. This object will be
supplied as the

MBeanServer

for any new connection
created by this connector server. Existing connections are
unaffected.

This method can be called more than once with different

MBeanServerForwarder

objects. The result is a chain
of forwarders. The last forwarder added is the first in the chain.
In more detail:

- If this connector server is already associated with an

MBeanServer

object, then that object is given to

mbsf.setMBeanServer

. If doing so produces an exception, this
method throws the same exception without any other effect.

If this connector is not already associated with an

MBeanServer

object, or if the

mbsf.setMBeanServer

call just mentioned succeeds,
then

mbsf

becomes this connector server's

MBeanServer

.

**Parameters:** mbsf

- the new

MBeanServerForwarder

.
**Throws:** IllegalArgumentException

- if the call to

mbsf.setMBeanServer

fails
with

IllegalArgumentException

. This includes the
case where

mbsf

is null.

- getConnectionIds

```java
String
[] getConnectionIds()
```

The list of IDs for currently-open connections to this
connector server.

**Returns:** a new string array containing the list of IDs. If
there are no currently-open connections, this array will be
empty.

- getAddress

```java
JMXServiceURL
getAddress()
```

The address of this connector server.

The address returned may not be the exact original

JMXServiceURL

that was supplied when creating the connector server, since the original
address may not always be complete. For example the port number may be
dynamically allocated when starting the connector server. Instead the
address returned is the actual

JMXServiceURL

of the

JMXConnectorServer

. This is the address that clients supply
to

JMXConnectorFactory.connect(JMXServiceURL)

.

Note that the address returned may be

null

if
the

JMXConnectorServer

is not yet

active

.

**Returns:** the address of this connector server, or null if it
does not have one.

- getAttributes

```java
Map
<
String
,​?> getAttributes()
```

The attributes for this connector server.

**Returns:** a read-only map containing the attributes for this
connector server. Attributes whose values are not serializable
are omitted from this map. If there are no serializable
attributes, the returned map is empty.

- toJMXConnector

```java
JMXConnector
toJMXConnector​(
Map
<
String
,​?> env)
throws
IOException
```

Returns a client stub for this connector server. A client
stub is a serializable object whose

connect

method can be used to make
one new connection to this connector server.

A given connector need not support the generation of client
stubs. However, the connectors specified by the JMX Remote API do
(JMXMP Connector and RMI Connector).

**Parameters:** env

- client connection parameters of the same sort that
can be provided to

JMXConnector.connect(Map)

. Can be null, which is equivalent
to an empty map.
**Returns:** a client stub that can be used to make a new connection
to this connector server.
**Throws:** UnsupportedOperationException

- if this connector
server does not support the generation of client stubs.
**Throws:** IllegalStateException

- if the JMXConnectorServer is
not started (see

isActive()

).
**Throws:** IOException

- if a communications problem means that a
stub cannot be created.

---

#### Method Detail

start

```java
void start()
throws
IOException
```

Activates the connector server, that is, starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

**Throws:** IOException

- if it is not possible to start listening
or if the connector server has been stopped.
**Throws:** IllegalStateException

- if the connector server has
not been attached to an MBean server.

---

#### start

void start()
throws

IOException

Activates the connector server, that is, starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

stop

```java
void stop()
throws
IOException
```

Deactivates the connector server, that is, stops listening for
client connections. Calling this method will also close all
client connections that were made by this server. After this
method returns, whether normally or with an exception, the
connector server will not create any new client
connections.

Once a connector server has been stopped, it cannot be started
again.

Calling this method when the connector server has already
been stopped has no effect. Calling this method when the
connector server has not yet been started will disable the
connector server object permanently.

If closing a client connection produces an exception, that
exception is not thrown from this method. A

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

is emitted from this MBean
with the connection ID of the connection that could not be
closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

**Throws:** IOException

- if the server cannot be closed cleanly.
When this exception is thrown, the server has already attempted
to close all client connections. All client connections are
closed except possibly those that generated exceptions when the
server attempted to close them.

---

#### stop

void stop()
throws

IOException

Deactivates the connector server, that is, stops listening for
client connections. Calling this method will also close all
client connections that were made by this server. After this
method returns, whether normally or with an exception, the
connector server will not create any new client
connections.

Once a connector server has been stopped, it cannot be started
again.

Calling this method when the connector server has already
been stopped has no effect. Calling this method when the
connector server has not yet been started will disable the
connector server object permanently.

If closing a client connection produces an exception, that
exception is not thrown from this method. A

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

is emitted from this MBean
with the connection ID of the connection that could not be
closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

Deactivates the connector server, that is, stops listening for
client connections. Calling this method will also close all
client connections that were made by this server. After this
method returns, whether normally or with an exception, the
connector server will not create any new client
connections.

Once a connector server has been stopped, it cannot be started
again.

Calling this method when the connector server has already
been stopped has no effect. Calling this method when the
connector server has not yet been started will disable the
connector server object permanently.

If closing a client connection produces an exception, that
exception is not thrown from this method. A

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

is emitted from this MBean
with the connection ID of the connection that could not be
closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

isActive

```java
boolean isActive()
```

Determines whether the connector server is active. A connector
server starts being active when its

start

method
returns successfully and remains active until either its

stop

method is called or the connector server
fails.

**Returns:** true if the connector server is active.

---

#### isActive

boolean isActive()

Determines whether the connector server is active. A connector
server starts being active when its

start

method
returns successfully and remains active until either its

stop

method is called or the connector server
fails.

setMBeanServerForwarder

```java
void setMBeanServerForwarder​(
MBeanServerForwarder
mbsf)
```

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server. This object will be
supplied as the

MBeanServer

for any new connection
created by this connector server. Existing connections are
unaffected.

This method can be called more than once with different

MBeanServerForwarder

objects. The result is a chain
of forwarders. The last forwarder added is the first in the chain.
In more detail:

- If this connector server is already associated with an

MBeanServer

object, then that object is given to

mbsf.setMBeanServer

. If doing so produces an exception, this
method throws the same exception without any other effect.

If this connector is not already associated with an

MBeanServer

object, or if the

mbsf.setMBeanServer

call just mentioned succeeds,
then

mbsf

becomes this connector server's

MBeanServer

.

**Parameters:** mbsf

- the new

MBeanServerForwarder

.
**Throws:** IllegalArgumentException

- if the call to

mbsf.setMBeanServer

fails
with

IllegalArgumentException

. This includes the
case where

mbsf

is null.

---

#### setMBeanServerForwarder

void setMBeanServerForwarder​(

MBeanServerForwarder

mbsf)

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server. This object will be
supplied as the

MBeanServer

for any new connection
created by this connector server. Existing connections are
unaffected.

This method can be called more than once with different

MBeanServerForwarder

objects. The result is a chain
of forwarders. The last forwarder added is the first in the chain.
In more detail:

- If this connector server is already associated with an

MBeanServer

object, then that object is given to

mbsf.setMBeanServer

. If doing so produces an exception, this
method throws the same exception without any other effect.

If this connector is not already associated with an

MBeanServer

object, or if the

mbsf.setMBeanServer

call just mentioned succeeds,
then

mbsf

becomes this connector server's

MBeanServer

.

Inserts an object that intercepts requests for the MBean server
that arrive through this connector server. This object will be
supplied as the

MBeanServer

for any new connection
created by this connector server. Existing connections are
unaffected.

This method can be called more than once with different

MBeanServerForwarder

objects. The result is a chain
of forwarders. The last forwarder added is the first in the chain.
In more detail:

If this connector server is already associated with an

MBeanServer

object, then that object is given to

mbsf.setMBeanServer

. If doing so produces an exception, this
method throws the same exception without any other effect.

If this connector is not already associated with an

MBeanServer

object, or if the

mbsf.setMBeanServer

call just mentioned succeeds,
then

mbsf

becomes this connector server's

MBeanServer

.

If this connector server is already associated with an

MBeanServer

object, then that object is given to

mbsf.setMBeanServer

. If doing so produces an exception, this
method throws the same exception without any other effect.

If this connector is not already associated with an

MBeanServer

object, or if the

mbsf.setMBeanServer

call just mentioned succeeds,
then

mbsf

becomes this connector server's

MBeanServer

.

getConnectionIds

```java
String
[] getConnectionIds()
```

The list of IDs for currently-open connections to this
connector server.

**Returns:** a new string array containing the list of IDs. If
there are no currently-open connections, this array will be
empty.

---

#### getConnectionIds

String

[] getConnectionIds()

The list of IDs for currently-open connections to this
connector server.

getAddress

```java
JMXServiceURL
getAddress()
```

The address of this connector server.

The address returned may not be the exact original

JMXServiceURL

that was supplied when creating the connector server, since the original
address may not always be complete. For example the port number may be
dynamically allocated when starting the connector server. Instead the
address returned is the actual

JMXServiceURL

of the

JMXConnectorServer

. This is the address that clients supply
to

JMXConnectorFactory.connect(JMXServiceURL)

.

Note that the address returned may be

null

if
the

JMXConnectorServer

is not yet

active

.

**Returns:** the address of this connector server, or null if it
does not have one.

---

#### getAddress

JMXServiceURL

getAddress()

The address of this connector server.

The address returned may not be the exact original

JMXServiceURL

that was supplied when creating the connector server, since the original
address may not always be complete. For example the port number may be
dynamically allocated when starting the connector server. Instead the
address returned is the actual

JMXServiceURL

of the

JMXConnectorServer

. This is the address that clients supply
to

JMXConnectorFactory.connect(JMXServiceURL)

.

Note that the address returned may be

null

if
the

JMXConnectorServer

is not yet

active

.

The address of this connector server.

The address returned may not be the exact original

JMXServiceURL

that was supplied when creating the connector server, since the original
address may not always be complete. For example the port number may be
dynamically allocated when starting the connector server. Instead the
address returned is the actual

JMXServiceURL

of the

JMXConnectorServer

. This is the address that clients supply
to

JMXConnectorFactory.connect(JMXServiceURL)

.

Note that the address returned may be

null

if
the

JMXConnectorServer

is not yet

active

.

getAttributes

```java
Map
<
String
,​?> getAttributes()
```

The attributes for this connector server.

**Returns:** a read-only map containing the attributes for this
connector server. Attributes whose values are not serializable
are omitted from this map. If there are no serializable
attributes, the returned map is empty.

---

#### getAttributes

Map

<

String

,​?> getAttributes()

The attributes for this connector server.

toJMXConnector

```java
JMXConnector
toJMXConnector​(
Map
<
String
,​?> env)
throws
IOException
```

Returns a client stub for this connector server. A client
stub is a serializable object whose

connect

method can be used to make
one new connection to this connector server.

A given connector need not support the generation of client
stubs. However, the connectors specified by the JMX Remote API do
(JMXMP Connector and RMI Connector).

**Parameters:** env

- client connection parameters of the same sort that
can be provided to

JMXConnector.connect(Map)

. Can be null, which is equivalent
to an empty map.
**Returns:** a client stub that can be used to make a new connection
to this connector server.
**Throws:** UnsupportedOperationException

- if this connector
server does not support the generation of client stubs.
**Throws:** IllegalStateException

- if the JMXConnectorServer is
not started (see

isActive()

).
**Throws:** IOException

- if a communications problem means that a
stub cannot be created.

---

#### toJMXConnector

JMXConnector

toJMXConnector​(

Map

<

String

,​?> env)
throws

IOException

Returns a client stub for this connector server. A client
stub is a serializable object whose

connect

method can be used to make
one new connection to this connector server.

A given connector need not support the generation of client
stubs. However, the connectors specified by the JMX Remote API do
(JMXMP Connector and RMI Connector).

Returns a client stub for this connector server. A client
stub is a serializable object whose

connect

method can be used to make
one new connection to this connector server.

A given connector need not support the generation of client
stubs. However, the connectors specified by the JMX Remote API do
(JMXMP Connector and RMI Connector).

---

