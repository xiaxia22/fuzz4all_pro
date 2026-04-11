# Class JMXConnectorServer

**Source:** `java.management\javax\management\remote\JMXConnectorServer.html`

### Class Description

```java
public abstract class
JMXConnectorServer

extends
NotificationBroadcasterSupport

implements
JMXConnectorServerMBean
,
MBeanRegistration
,
JMXAddressable
```

Superclass of every connector server. A connector server is
attached to an MBean server. It listens for client connection
requests and creates a connection for each one.

A connector server is associated with an MBean server either by
registering it in that MBean server, or by passing the MBean server
to its constructor.

A connector server is inactive when created. It only starts
listening for client connections when the

start

method is called. A connector server stops listening for client
connections when the

stop

method is called or when
the connector server is unregistered from its MBean server.

Stopping a connector server does not unregister it from its
MBean server. A connector server once stopped cannot be
restarted.

Each time a client connection is made or broken, a notification
of class

JMXConnectionNotification

is emitted.

**All Implemented Interfaces:** MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

,

JMXAddressable

,

JMXConnectorServerMBean

---

### Field Details

#### public static final
String
AUTHENTICATOR

Name of the attribute that specifies the authenticator for a
connector server. The value associated with this attribute, if
any, must be an object that implements the interface

JMXAuthenticator

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public JMXConnectorServer()

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to. This constructor
is typically called by one of the

createMBean

methods when creating, within an MBean server, a connector
server that makes it available remotely.

---

#### public JMXConnectorServer​(
MBeanServer
mbeanServer)

Constructs a connector server that is attached to the given
MBean server. A connector server that is created in this way
can be registered in a different MBean server, or not registered
in any MBean server.

**Parameters:**
- mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.

---

### Method Details

#### public
MBeanServer
getMBeanServer()

Returns the MBean server that this connector server is
attached to.

**Returns:**
- the MBean server that this connector server is attached
to, or null if it is not yet attached to an MBean server.

---

#### public
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

The default implementation of this method uses

JMXConnectorServerMBean.getAddress()

and

JMXConnectorFactory

to generate the
stub, with code equivalent to the following:

```java
JMXServiceURL addr =
getAddress()
;
return
JMXConnectorFactory.newJMXConnector(addr, env)
;
```

A connector server for which this is inappropriate must
override this method so that it either implements the
appropriate logic or throws

UnsupportedOperationException

.

**Specified by:**
- toJMXConnector

in interface

JMXConnectorServerMBean

**Parameters:**
- env

- client connection parameters of the same sort that
could be provided to

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

JMXConnectorServerMBean.isActive()

).
- IOException

- if a communications problem means that a
stub cannot be created.

---

#### public
MBeanNotificationInfo
[] getNotificationInfo()

Returns an array indicating the notifications that this MBean
sends. The implementation in

JMXConnectorServer

returns an array with one element, indicating that it can emit
notifications of class

JMXConnectionNotification

with
the types defined in that class. A subclass that can emit other
notifications should return an array that contains this element
plus descriptions of the other notifications.

**Specified by:**
- getNotificationInfo

in interface

NotificationBroadcaster

**Returns:**
- the array of possible notifications.

---

#### protected void connectionOpened​(
String
connectionId,

String
message,

Object
userData)

Called by a subclass when a new client connection is opened.
Adds

connectionId

to the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.OPENED

.

**Parameters:**
- connectionId

- the ID of the new connection. This must be
different from the ID of any connection previously opened by
this connector server.
- message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
- userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.

**Throws:**
- NullPointerException

- if

connectionId

is
null.

---

#### protected void connectionClosed​(
String
connectionId,

String
message,

Object
userData)

Called by a subclass when a client connection is closed
normally. Removes

connectionId

from the list returned
by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.CLOSED

.

**Parameters:**
- connectionId

- the ID of the closed connection.
- message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
- userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.

**Throws:**
- NullPointerException

- if

connectionId

is null.

---

#### protected void connectionFailed​(
String
connectionId,

String
message,

Object
userData)

Called by a subclass when a client connection fails.
Removes

connectionId

from the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

.

**Parameters:**
- connectionId

- the ID of the failed connection.
- message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
- userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.

**Throws:**
- NullPointerException

- if

connectionId

is
null.

---

#### public
ObjectName
preRegister​(
MBeanServer
mbs,

ObjectName
name)

Called by an MBean server when this connector server is
registered in that MBean server. This connector server becomes
attached to the MBean server and its

getMBeanServer()

method will return

mbs

.

If this connector server is already attached to an MBean
server, this method has no effect. The MBean server it is
attached to is not necessarily the one it is being registered
in.

**Specified by:**
- preRegister

in interface

MBeanRegistration

**Parameters:**
- mbs

- the MBean server in which this connection server is
being registered.
- name

- The object name of the MBean.

**Returns:**
- The name under which the MBean is to be registered.

**Throws:**
- NullPointerException

- if

mbs

or

name

is null.

---

#### public void preDeregister()
throws
Exception

Called by an MBean server when this connector server is
unregistered from that MBean server. If this connector server
was attached to that MBean server by being registered in it,
and if the connector server is still active,
then unregistering it will call the

stop

method.
If the

stop

method throws an exception, the
unregistration attempt will fail. It is recommended to call
the

stop

method explicitly before unregistering
the MBean.

**Specified by:**
- preDeregister

in interface

MBeanRegistration

**Throws:**
- IOException

- if thrown by the

stop

method.
- Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

---

### Additional Sections

#### Class JMXConnectorServer

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.remote.JMXConnectorServer

javax.management.NotificationBroadcasterSupport

- javax.management.remote.JMXConnectorServer

javax.management.remote.JMXConnectorServer

**All Implemented Interfaces:** MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

,

JMXAddressable

,

JMXConnectorServerMBean

**Direct Known Subclasses:** RMIConnectorServer

```java
public abstract class
JMXConnectorServer

extends
NotificationBroadcasterSupport

implements
JMXConnectorServerMBean
,
MBeanRegistration
,
JMXAddressable
```

Superclass of every connector server. A connector server is
attached to an MBean server. It listens for client connection
requests and creates a connection for each one.

A connector server is associated with an MBean server either by
registering it in that MBean server, or by passing the MBean server
to its constructor.

A connector server is inactive when created. It only starts
listening for client connections when the

start

method is called. A connector server stops listening for client
connections when the

stop

method is called or when
the connector server is unregistered from its MBean server.

Stopping a connector server does not unregister it from its
MBean server. A connector server once stopped cannot be
restarted.

Each time a client connection is made or broken, a notification
of class

JMXConnectionNotification

is emitted.

**Since:** 1.5

public abstract class

JMXConnectorServer

extends

NotificationBroadcasterSupport

implements

JMXConnectorServerMBean

,

MBeanRegistration

,

JMXAddressable

Superclass of every connector server. A connector server is
attached to an MBean server. It listens for client connection
requests and creates a connection for each one.

A connector server is associated with an MBean server either by
registering it in that MBean server, or by passing the MBean server
to its constructor.

A connector server is inactive when created. It only starts
listening for client connections when the

start

method is called. A connector server stops listening for client
connections when the

stop

method is called or when
the connector server is unregistered from its MBean server.

Stopping a connector server does not unregister it from its
MBean server. A connector server once stopped cannot be
restarted.

Each time a client connection is made or broken, a notification
of class

JMXConnectionNotification

is emitted.

Superclass of every connector server. A connector server is
attached to an MBean server. It listens for client connection
requests and creates a connection for each one.

A connector server is associated with an MBean server either by
registering it in that MBean server, or by passing the MBean server
to its constructor.

A connector server is inactive when created. It only starts
listening for client connections when the

start

method is called. A connector server stops listening for client
connections when the

stop

method is called or when
the connector server is unregistered from its MBean server.

Stopping a connector server does not unregister it from its
MBean server. A connector server once stopped cannot be
restarted.

Each time a client connection is made or broken, a notification
of class

JMXConnectionNotification

is emitted.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

AUTHENTICATOR

Name of the attribute that specifies the authenticator for a
connector server.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JMXConnectorServer

()

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to.

JMXConnectorServer

​(

MBeanServer

mbeanServer)

Constructs a connector server that is attached to the given
MBean server.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

connectionClosed

​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a client connection is closed
normally.

protected void

connectionFailed

​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a client connection fails.

protected void

connectionOpened

​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a new client connection is opened.

MBeanServer

getMBeanServer

()

Returns the MBean server that this connector server is
attached to.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns an array indicating the notifications that this MBean
sends.

void

preDeregister

()

Called by an MBean server when this connector server is
unregistered from that MBean server.

ObjectName

preRegister

​(

MBeanServer

mbs,

ObjectName

name)

Called by an MBean server when this connector server is
registered in that MBean server.

JMXConnector

toJMXConnector

​(

Map

<

String

,​?> env)

Returns a client stub for this connector server.

- Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

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

- Methods declared in interface javax.management.remote.

JMXAddressable

getAddress

- Methods declared in interface javax.management.remote.

JMXConnectorServerMBean

getAddress

,

getAttributes

,

getConnectionIds

,

isActive

,

setMBeanServerForwarder

,

start

,

stop

- Methods declared in interface javax.management.

MBeanRegistration

postDeregister

,

postRegister

- Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

Field Summary

Fields

Modifier and Type

Field

Description

static

String

AUTHENTICATOR

Name of the attribute that specifies the authenticator for a
connector server.

---

#### Field Summary

Name of the attribute that specifies the authenticator for a
connector server.

Constructor Summary

Constructors

Constructor

Description

JMXConnectorServer

()

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to.

JMXConnectorServer

​(

MBeanServer

mbeanServer)

Constructs a connector server that is attached to the given
MBean server.

---

#### Constructor Summary

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to.

Constructs a connector server that is attached to the given
MBean server.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

connectionClosed

​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a client connection is closed
normally.

protected void

connectionFailed

​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a client connection fails.

protected void

connectionOpened

​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a new client connection is opened.

MBeanServer

getMBeanServer

()

Returns the MBean server that this connector server is
attached to.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns an array indicating the notifications that this MBean
sends.

void

preDeregister

()

Called by an MBean server when this connector server is
unregistered from that MBean server.

ObjectName

preRegister

​(

MBeanServer

mbs,

ObjectName

name)

Called by an MBean server when this connector server is
registered in that MBean server.

JMXConnector

toJMXConnector

​(

Map

<

String

,​?> env)

Returns a client stub for this connector server.

- Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

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

- Methods declared in interface javax.management.remote.

JMXAddressable

getAddress

- Methods declared in interface javax.management.remote.

JMXConnectorServerMBean

getAddress

,

getAttributes

,

getConnectionIds

,

isActive

,

setMBeanServerForwarder

,

start

,

stop

- Methods declared in interface javax.management.

MBeanRegistration

postDeregister

,

postRegister

- Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Method Summary

Called by a subclass when a client connection is closed
normally.

Called by a subclass when a client connection fails.

Called by a subclass when a new client connection is opened.

Returns the MBean server that this connector server is
attached to.

Returns an array indicating the notifications that this MBean
sends.

Called by an MBean server when this connector server is
unregistered from that MBean server.

Called by an MBean server when this connector server is
registered in that MBean server.

Returns a client stub for this connector server.

Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

---

#### Methods declared in class javax.management. NotificationBroadcasterSupport

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

Methods declared in interface javax.management.remote.

JMXAddressable

getAddress

---

#### Methods declared in interface javax.management.remote. JMXAddressable

Methods declared in interface javax.management.remote.

JMXConnectorServerMBean

getAddress

,

getAttributes

,

getConnectionIds

,

isActive

,

setMBeanServerForwarder

,

start

,

stop

---

#### Methods declared in interface javax.management.remote. JMXConnectorServerMBean

Methods declared in interface javax.management.

MBeanRegistration

postDeregister

,

postRegister

---

#### Methods declared in interface javax.management. MBeanRegistration

Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationBroadcaster

Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationEmitter

============ FIELD DETAIL ===========

- Field Detail

- AUTHENTICATOR

```java
public static final
String
AUTHENTICATOR
```

Name of the attribute that specifies the authenticator for a
connector server. The value associated with this attribute, if
any, must be an object that implements the interface

JMXAuthenticator

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JMXConnectorServer

```java
public JMXConnectorServer()
```

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to. This constructor
is typically called by one of the

createMBean

methods when creating, within an MBean server, a connector
server that makes it available remotely.

- JMXConnectorServer

```java
public JMXConnectorServer​(
MBeanServer
mbeanServer)
```

Constructs a connector server that is attached to the given
MBean server. A connector server that is created in this way
can be registered in a different MBean server, or not registered
in any MBean server.

**Parameters:** mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.

============ METHOD DETAIL ==========

- Method Detail

- getMBeanServer

```java
public
MBeanServer
getMBeanServer()
```

Returns the MBean server that this connector server is
attached to.

**Returns:** the MBean server that this connector server is attached
to, or null if it is not yet attached to an MBean server.

- toJMXConnector

```java
public
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

The default implementation of this method uses

JMXConnectorServerMBean.getAddress()

and

JMXConnectorFactory

to generate the
stub, with code equivalent to the following:

```java
JMXServiceURL addr =
getAddress()
;
return
JMXConnectorFactory.newJMXConnector(addr, env)
;
```

A connector server for which this is inappropriate must
override this method so that it either implements the
appropriate logic or throws

UnsupportedOperationException

.

**Specified by:** toJMXConnector

in interface

JMXConnectorServerMBean
**Parameters:** env

- client connection parameters of the same sort that
could be provided to

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

JMXConnectorServerMBean.isActive()

).
**Throws:** IOException

- if a communications problem means that a
stub cannot be created.

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns an array indicating the notifications that this MBean
sends. The implementation in

JMXConnectorServer

returns an array with one element, indicating that it can emit
notifications of class

JMXConnectionNotification

with
the types defined in that class. A subclass that can emit other
notifications should return an array that contains this element
plus descriptions of the other notifications.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

- connectionOpened

```java
protected void connectionOpened​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a new client connection is opened.
Adds

connectionId

to the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.OPENED

.

**Parameters:** connectionId

- the ID of the new connection. This must be
different from the ID of any connection previously opened by
this connector server.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is
null.

- connectionClosed

```java
protected void connectionClosed​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a client connection is closed
normally. Removes

connectionId

from the list returned
by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.CLOSED

.

**Parameters:** connectionId

- the ID of the closed connection.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is null.

- connectionFailed

```java
protected void connectionFailed​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a client connection fails.
Removes

connectionId

from the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

.

**Parameters:** connectionId

- the ID of the failed connection.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is
null.

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
mbs,

ObjectName
name)
```

Called by an MBean server when this connector server is
registered in that MBean server. This connector server becomes
attached to the MBean server and its

getMBeanServer()

method will return

mbs

.

If this connector server is already attached to an MBean
server, this method has no effect. The MBean server it is
attached to is not necessarily the one it is being registered
in.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** mbs

- the MBean server in which this connection server is
being registered.
**Parameters:** name

- The object name of the MBean.
**Returns:** The name under which the MBean is to be registered.
**Throws:** NullPointerException

- if

mbs

or

name

is null.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Called by an MBean server when this connector server is
unregistered from that MBean server. If this connector server
was attached to that MBean server by being registered in it,
and if the connector server is still active,
then unregistering it will call the

stop

method.
If the

stop

method throws an exception, the
unregistration attempt will fail. It is recommended to call
the

stop

method explicitly before unregistering
the MBean.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** IOException

- if thrown by the

stop

method.
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

Field Detail

- AUTHENTICATOR

```java
public static final
String
AUTHENTICATOR
```

Name of the attribute that specifies the authenticator for a
connector server. The value associated with this attribute, if
any, must be an object that implements the interface

JMXAuthenticator

.

**See Also:** Constant Field Values

---

#### Field Detail

AUTHENTICATOR

```java
public static final
String
AUTHENTICATOR
```

Name of the attribute that specifies the authenticator for a
connector server. The value associated with this attribute, if
any, must be an object that implements the interface

JMXAuthenticator

.

**See Also:** Constant Field Values

---

#### AUTHENTICATOR

public static final

String

AUTHENTICATOR

Name of the attribute that specifies the authenticator for a
connector server. The value associated with this attribute, if
any, must be an object that implements the interface

JMXAuthenticator

.

Constructor Detail

- JMXConnectorServer

```java
public JMXConnectorServer()
```

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to. This constructor
is typically called by one of the

createMBean

methods when creating, within an MBean server, a connector
server that makes it available remotely.

- JMXConnectorServer

```java
public JMXConnectorServer​(
MBeanServer
mbeanServer)
```

Constructs a connector server that is attached to the given
MBean server. A connector server that is created in this way
can be registered in a different MBean server, or not registered
in any MBean server.

**Parameters:** mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.

---

#### Constructor Detail

JMXConnectorServer

```java
public JMXConnectorServer()
```

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to. This constructor
is typically called by one of the

createMBean

methods when creating, within an MBean server, a connector
server that makes it available remotely.

---

#### JMXConnectorServer

public JMXConnectorServer()

Constructs a connector server that will be registered as an
MBean in the MBean server it is attached to. This constructor
is typically called by one of the

createMBean

methods when creating, within an MBean server, a connector
server that makes it available remotely.

JMXConnectorServer

```java
public JMXConnectorServer​(
MBeanServer
mbeanServer)
```

Constructs a connector server that is attached to the given
MBean server. A connector server that is created in this way
can be registered in a different MBean server, or not registered
in any MBean server.

**Parameters:** mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.

---

#### JMXConnectorServer

public JMXConnectorServer​(

MBeanServer

mbeanServer)

Constructs a connector server that is attached to the given
MBean server. A connector server that is created in this way
can be registered in a different MBean server, or not registered
in any MBean server.

Method Detail

- getMBeanServer

```java
public
MBeanServer
getMBeanServer()
```

Returns the MBean server that this connector server is
attached to.

**Returns:** the MBean server that this connector server is attached
to, or null if it is not yet attached to an MBean server.

- toJMXConnector

```java
public
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

The default implementation of this method uses

JMXConnectorServerMBean.getAddress()

and

JMXConnectorFactory

to generate the
stub, with code equivalent to the following:

```java
JMXServiceURL addr =
getAddress()
;
return
JMXConnectorFactory.newJMXConnector(addr, env)
;
```

A connector server for which this is inappropriate must
override this method so that it either implements the
appropriate logic or throws

UnsupportedOperationException

.

**Specified by:** toJMXConnector

in interface

JMXConnectorServerMBean
**Parameters:** env

- client connection parameters of the same sort that
could be provided to

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

JMXConnectorServerMBean.isActive()

).
**Throws:** IOException

- if a communications problem means that a
stub cannot be created.

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns an array indicating the notifications that this MBean
sends. The implementation in

JMXConnectorServer

returns an array with one element, indicating that it can emit
notifications of class

JMXConnectionNotification

with
the types defined in that class. A subclass that can emit other
notifications should return an array that contains this element
plus descriptions of the other notifications.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

- connectionOpened

```java
protected void connectionOpened​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a new client connection is opened.
Adds

connectionId

to the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.OPENED

.

**Parameters:** connectionId

- the ID of the new connection. This must be
different from the ID of any connection previously opened by
this connector server.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is
null.

- connectionClosed

```java
protected void connectionClosed​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a client connection is closed
normally. Removes

connectionId

from the list returned
by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.CLOSED

.

**Parameters:** connectionId

- the ID of the closed connection.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is null.

- connectionFailed

```java
protected void connectionFailed​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a client connection fails.
Removes

connectionId

from the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

.

**Parameters:** connectionId

- the ID of the failed connection.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is
null.

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
mbs,

ObjectName
name)
```

Called by an MBean server when this connector server is
registered in that MBean server. This connector server becomes
attached to the MBean server and its

getMBeanServer()

method will return

mbs

.

If this connector server is already attached to an MBean
server, this method has no effect. The MBean server it is
attached to is not necessarily the one it is being registered
in.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** mbs

- the MBean server in which this connection server is
being registered.
**Parameters:** name

- The object name of the MBean.
**Returns:** The name under which the MBean is to be registered.
**Throws:** NullPointerException

- if

mbs

or

name

is null.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Called by an MBean server when this connector server is
unregistered from that MBean server. If this connector server
was attached to that MBean server by being registered in it,
and if the connector server is still active,
then unregistering it will call the

stop

method.
If the

stop

method throws an exception, the
unregistration attempt will fail. It is recommended to call
the

stop

method explicitly before unregistering
the MBean.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** IOException

- if thrown by the

stop

method.
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

---

#### Method Detail

getMBeanServer

```java
public
MBeanServer
getMBeanServer()
```

Returns the MBean server that this connector server is
attached to.

**Returns:** the MBean server that this connector server is attached
to, or null if it is not yet attached to an MBean server.

---

#### getMBeanServer

public

MBeanServer

getMBeanServer()

Returns the MBean server that this connector server is
attached to.

toJMXConnector

```java
public
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

The default implementation of this method uses

JMXConnectorServerMBean.getAddress()

and

JMXConnectorFactory

to generate the
stub, with code equivalent to the following:

```java
JMXServiceURL addr =
getAddress()
;
return
JMXConnectorFactory.newJMXConnector(addr, env)
;
```

A connector server for which this is inappropriate must
override this method so that it either implements the
appropriate logic or throws

UnsupportedOperationException

.

**Specified by:** toJMXConnector

in interface

JMXConnectorServerMBean
**Parameters:** env

- client connection parameters of the same sort that
could be provided to

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

JMXConnectorServerMBean.isActive()

).
**Throws:** IOException

- if a communications problem means that a
stub cannot be created.

---

#### toJMXConnector

public

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

The default implementation of this method uses

JMXConnectorServerMBean.getAddress()

and

JMXConnectorFactory

to generate the
stub, with code equivalent to the following:

```java
JMXServiceURL addr =
getAddress()
;
return
JMXConnectorFactory.newJMXConnector(addr, env)
;
```

A connector server for which this is inappropriate must
override this method so that it either implements the
appropriate logic or throws

UnsupportedOperationException

.

Returns a client stub for this connector server. A client
stub is a serializable object whose

connect

method can be used to make
one new connection to this connector server.

A given connector need not support the generation of client
stubs. However, the connectors specified by the JMX Remote API do
(JMXMP Connector and RMI Connector).

The default implementation of this method uses

JMXConnectorServerMBean.getAddress()

and

JMXConnectorFactory

to generate the
stub, with code equivalent to the following:

JMXServiceURL addr =

getAddress()

;
return

JMXConnectorFactory.newJMXConnector(addr, env)

;

A connector server for which this is inappropriate must
override this method so that it either implements the
appropriate logic or throws

UnsupportedOperationException

.

getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns an array indicating the notifications that this MBean
sends. The implementation in

JMXConnectorServer

returns an array with one element, indicating that it can emit
notifications of class

JMXConnectionNotification

with
the types defined in that class. A subclass that can emit other
notifications should return an array that contains this element
plus descriptions of the other notifications.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

---

#### getNotificationInfo

public

MBeanNotificationInfo

[] getNotificationInfo()

Returns an array indicating the notifications that this MBean
sends. The implementation in

JMXConnectorServer

returns an array with one element, indicating that it can emit
notifications of class

JMXConnectionNotification

with
the types defined in that class. A subclass that can emit other
notifications should return an array that contains this element
plus descriptions of the other notifications.

connectionOpened

```java
protected void connectionOpened​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a new client connection is opened.
Adds

connectionId

to the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.OPENED

.

**Parameters:** connectionId

- the ID of the new connection. This must be
different from the ID of any connection previously opened by
this connector server.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is
null.

---

#### connectionOpened

protected void connectionOpened​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a new client connection is opened.
Adds

connectionId

to the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.OPENED

.

connectionClosed

```java
protected void connectionClosed​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a client connection is closed
normally. Removes

connectionId

from the list returned
by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.CLOSED

.

**Parameters:** connectionId

- the ID of the closed connection.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is null.

---

#### connectionClosed

protected void connectionClosed​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a client connection is closed
normally. Removes

connectionId

from the list returned
by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.CLOSED

.

connectionFailed

```java
protected void connectionFailed​(
String
connectionId,

String
message,

Object
userData)
```

Called by a subclass when a client connection fails.
Removes

connectionId

from the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

.

**Parameters:** connectionId

- the ID of the failed connection.
**Parameters:** message

- the message for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getMessage()

.
**Parameters:** userData

- the

userData

for the emitted

JMXConnectionNotification

. Can be null. See

Notification.getUserData()

.
**Throws:** NullPointerException

- if

connectionId

is
null.

---

#### connectionFailed

protected void connectionFailed​(

String

connectionId,

String

message,

Object

userData)

Called by a subclass when a client connection fails.
Removes

connectionId

from the list returned by

JMXConnectorServerMBean.getConnectionIds()

, then emits a

JMXConnectionNotification

with type

JMXConnectionNotification.FAILED

.

preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
mbs,

ObjectName
name)
```

Called by an MBean server when this connector server is
registered in that MBean server. This connector server becomes
attached to the MBean server and its

getMBeanServer()

method will return

mbs

.

If this connector server is already attached to an MBean
server, this method has no effect. The MBean server it is
attached to is not necessarily the one it is being registered
in.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** mbs

- the MBean server in which this connection server is
being registered.
**Parameters:** name

- The object name of the MBean.
**Returns:** The name under which the MBean is to be registered.
**Throws:** NullPointerException

- if

mbs

or

name

is null.

---

#### preRegister

public

ObjectName

preRegister​(

MBeanServer

mbs,

ObjectName

name)

Called by an MBean server when this connector server is
registered in that MBean server. This connector server becomes
attached to the MBean server and its

getMBeanServer()

method will return

mbs

.

If this connector server is already attached to an MBean
server, this method has no effect. The MBean server it is
attached to is not necessarily the one it is being registered
in.

Called by an MBean server when this connector server is
registered in that MBean server. This connector server becomes
attached to the MBean server and its

getMBeanServer()

method will return

mbs

.

If this connector server is already attached to an MBean
server, this method has no effect. The MBean server it is
attached to is not necessarily the one it is being registered
in.

preDeregister

```java
public void preDeregister()
throws
Exception
```

Called by an MBean server when this connector server is
unregistered from that MBean server. If this connector server
was attached to that MBean server by being registered in it,
and if the connector server is still active,
then unregistering it will call the

stop

method.
If the

stop

method throws an exception, the
unregistration attempt will fail. It is recommended to call
the

stop

method explicitly before unregistering
the MBean.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** IOException

- if thrown by the

stop

method.
**Throws:** Exception

- This exception will be caught by
the MBean server and re-thrown as an

MBeanRegistrationException

.

---

#### preDeregister

public void preDeregister()
throws

Exception

Called by an MBean server when this connector server is
unregistered from that MBean server. If this connector server
was attached to that MBean server by being registered in it,
and if the connector server is still active,
then unregistering it will call the

stop

method.
If the

stop

method throws an exception, the
unregistration attempt will fail. It is recommended to call
the

stop

method explicitly before unregistering
the MBean.

---

