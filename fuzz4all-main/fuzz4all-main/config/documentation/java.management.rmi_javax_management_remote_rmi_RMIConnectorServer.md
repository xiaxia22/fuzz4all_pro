# Class RMIConnectorServer

**Source:** `java.management.rmi\javax\management\remote\rmi\RMIConnectorServer.html`

### Class Description

```java
public class
RMIConnectorServer

extends
JMXConnectorServer
```

A JMX API connector server that creates RMI-based connections
from remote clients. Usually, such connector servers are made
using

JMXConnectorServerFactory

. However, specialized applications can
use this class directly, for example with an

RMIServerImpl

object.

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
JNDI_REBIND_ATTRIBUTE

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address. The value
associated with this attribute, if any, should be a string that
is equal, ignoring case, to

"true"

or

"false"

. The default value is false.

**See Also:**
- Constant Field Values

---

#### public static final
String
RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIClientSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:**
- Constant Field Values

---

#### public static final
String
RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIServerSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="10",

forRemoval
=true)
public static final
String
CREDENTIAL_TYPES

Name of the attribute that specifies a list of class names acceptable
as parameters to the

RMIServer.newClient()

remote method call.

This list of classes should correspond to the transitive closure of the
credentials class (or classes) used by the installed

JMXAuthenticator

associated with the

RMIServer

implementation.

If the attribute is not set, or is null, then any class is
deemed acceptable.

**See Also:**
- Constant Field Values

---

#### public static final
String
CREDENTIALS_FILTER_PATTERN

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

The filter pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

This list of classes allowed by filter should correspond to the
transitive closure of the credentials class (or classes) used by the
installed

JMXAuthenticator

associated with the

RMIServer

implementation.
If the attribute is not set then any class is deemed acceptable.

**See Also:**
- ObjectInputFilter

,

Constant Field Values

---

#### public static final
String
SERIAL_FILTER_PATTERN

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

The filter will be called for any class found in the serialized
stream sent to server by client, including all JMX defined classes
(such as

ObjectName

), all method parameters,
and, if present in the stream, all classes transitively referred by
the serial form of any deserialized object.
The pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

.
It may define an allow-list of permitted classes, a reject-list of
rejected classes, a maximum depth for the deserialized objects,
etc.

To be functional, the filter should allow at least all the
concrete types in the transitive closure of all objects that
might get serialized when serializing all JMX classes referred
as parameters in the

RMIConnection

interface,
plus all classes that a

client

might need to transmit wrapped in

marshalled objects

in order to interoperate with the MBeans registered
in the

MBeanServer

. That would potentially include all the
concrete

JMX OpenTypes

and the
classes they use in their serial form.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment)
throws
IOException

Makes an

RMIConnectorServer

.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,null)

**Parameters:**
- url

- the URL defining how to create the connector server.
Cannot be null.
- environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.

**Throws:**
- IllegalArgumentException

- if

url

is null.
- MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid when
this constructor is used.
- IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

---

#### public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException

Makes an

RMIConnectorServer

for the given MBean
server.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,mbeanServer)

**Parameters:**
- url

- the URL defining how to create the connector server.
Cannot be null.
- environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
- mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.

**Throws:**
- IllegalArgumentException

- if

url

is null.
- MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid
when this constructor is used.
- IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

---

#### public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

RMIServerImpl
rmiServerImpl,

MBeanServer
mbeanServer)
throws
IOException

Makes an

RMIConnectorServer

for the given MBean
server.

**Parameters:**
- url

- the URL defining how to create the connector server.
Cannot be null.
- environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
- rmiServerImpl

- An implementation of the RMIServer interface,
consistent with the protocol type specified in

url

.
If this parameter is non null, the protocol type specified by

url

is not constrained, and is assumed to be valid.
Otherwise, only "rmi" will be recognized.
- mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.

**Throws:**
- IllegalArgumentException

- if

url

is null.
- MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is recognized
when

rmiServerImpl

is null.
- IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

**See Also:**
- start()

---

### Method Details

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

**Specified by:**
- toJMXConnector

in interface

JMXConnectorServerMBean

**Overrides:**
- toJMXConnector

in class

JMXConnectorServer

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

#### public void start()
throws
IOException

Activates the connector server, that is starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

The behavior of this method when called for the first time
depends on the parameters that were supplied at construction,
as described below.

First, an object of a subclass of

RMIServerImpl

is
required, to export the connector server through RMI:

- If an

RMIServerImpl

was supplied to the
constructor, it is used.

Otherwise, if the

JMXServiceURL

was null, or its protocol part was

rmi

, an object
of type

RMIJRMPServerImpl

is created.

Otherwise, the implementation can create an
implementation-specific

RMIServerImpl

or it can throw

MalformedURLException

.

If the given address includes a JNDI directory URL as
specified in the package documentation for

javax.management.remote.rmi

, then this

RMIConnectorServer

will bootstrap by binding the

RMIServerImpl

to the given address.

If the URL path part of the

JMXServiceURL

was
empty or a single slash (

/

), then the RMI object
will not be bound to a directory. Instead, a reference to it
will be encoded in the URL path of the RMIConnectorServer
address (returned by

JMXConnectorServerMBean.getAddress()

). The encodings for

rmi

are described in the package documentation for

javax.management.remote.rmi

.

The behavior when the URL path is neither empty nor a JNDI
directory URL, or when the protocol is not

rmi

,
is implementation defined, and may include throwing

MalformedURLException

when the connector server is created
or when it is started.

**Throws:**
- IllegalStateException

- if the connector server has
not been attached to an MBean server.
- IOException

- if the connector server cannot be
started.

---

#### public void stop()
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

is emitted from this MBean with the
connection ID of the connection that could not be closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

This method calls the method

close

on the connector server's

RMIServerImpl

object.

If the

RMIServerImpl

was bound to a JNDI
directory by the

start

method, it is unbound
from the directory by this method.

**Throws:**
- IOException

- if the server cannot be closed cleanly,
or if the

RMIServerImpl

cannot be unbound from the
directory. When this exception is thrown, the server has
already attempted to close all client connections, if
appropriate; to call

RMIServerImpl.close()

; and to
unbind the

RMIServerImpl

from its directory, if
appropriate. All client connections are closed except possibly
those that generated exceptions when the server attempted to
close them.

---

### Additional Sections

#### Class RMIConnectorServer

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.remote.JMXConnectorServer
- - javax.management.remote.rmi.RMIConnectorServer

javax.management.NotificationBroadcasterSupport

- javax.management.remote.JMXConnectorServer
- - javax.management.remote.rmi.RMIConnectorServer

javax.management.remote.JMXConnectorServer

- javax.management.remote.rmi.RMIConnectorServer

javax.management.remote.rmi.RMIConnectorServer

**All Implemented Interfaces:** MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

,

JMXAddressable

,

JMXConnectorServerMBean

```java
public class
RMIConnectorServer

extends
JMXConnectorServer
```

A JMX API connector server that creates RMI-based connections
from remote clients. Usually, such connector servers are made
using

JMXConnectorServerFactory

. However, specialized applications can
use this class directly, for example with an

RMIServerImpl

object.

**Since:** 1.5

public class

RMIConnectorServer

extends

JMXConnectorServer

A JMX API connector server that creates RMI-based connections
from remote clients. Usually, such connector servers are made
using

JMXConnectorServerFactory

. However, specialized applications can
use this class directly, for example with an

RMIServerImpl

object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

CREDENTIAL_TYPES

Deprecated, for removal: This API element is subject to removal in a future version.

Use

CREDENTIALS_FILTER_PATTERN

with a

filter pattern

string instead.

static

String

CREDENTIALS_FILTER_PATTERN

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

static

String

JNDI_REBIND_ATTRIBUTE

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address.

static

String

RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector.

static

String

RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector.

static

String

SERIAL_FILTER_PATTERN

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

- Fields declared in class javax.management.remote.

JMXConnectorServer

AUTHENTICATOR

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMIConnectorServer

​(

JMXServiceURL

url,

Map

<

String

,​?> environment)

Makes an

RMIConnectorServer

.

RMIConnectorServer

​(

JMXServiceURL

url,

Map

<

String

,​?> environment,

MBeanServer

mbeanServer)

Makes an

RMIConnectorServer

for the given MBean
server.

RMIConnectorServer

​(

JMXServiceURL

url,

Map

<

String

,​?> environment,

RMIServerImpl

rmiServerImpl,

MBeanServer

mbeanServer)

Makes an

RMIConnectorServer

for the given MBean
server.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

start

()

Activates the connector server, that is starts listening for
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

- Methods declared in class javax.management.remote.

JMXConnectorServer

connectionClosed

,

connectionFailed

,

connectionOpened

,

getMBeanServer

,

getNotificationInfo

,

preDeregister

,

preRegister

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

CREDENTIAL_TYPES

Deprecated, for removal: This API element is subject to removal in a future version.

Use

CREDENTIALS_FILTER_PATTERN

with a

filter pattern

string instead.

static

String

CREDENTIALS_FILTER_PATTERN

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

static

String

JNDI_REBIND_ATTRIBUTE

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address.

static

String

RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector.

static

String

RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector.

static

String

SERIAL_FILTER_PATTERN

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

- Fields declared in class javax.management.remote.

JMXConnectorServer

AUTHENTICATOR

---

#### Field Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Use

CREDENTIALS_FILTER_PATTERN

with a

filter pattern

string instead.

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address.

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector.

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector.

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

Fields declared in class javax.management.remote.

JMXConnectorServer

AUTHENTICATOR

---

#### Fields declared in class javax.management.remote. JMXConnectorServer

Constructor Summary

Constructors

Constructor

Description

RMIConnectorServer

​(

JMXServiceURL

url,

Map

<

String

,​?> environment)

Makes an

RMIConnectorServer

.

RMIConnectorServer

​(

JMXServiceURL

url,

Map

<

String

,​?> environment,

MBeanServer

mbeanServer)

Makes an

RMIConnectorServer

for the given MBean
server.

RMIConnectorServer

​(

JMXServiceURL

url,

Map

<

String

,​?> environment,

RMIServerImpl

rmiServerImpl,

MBeanServer

mbeanServer)

Makes an

RMIConnectorServer

for the given MBean
server.

---

#### Constructor Summary

Makes an

RMIConnectorServer

.

Makes an

RMIConnectorServer

for the given MBean
server.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

start

()

Activates the connector server, that is starts listening for
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

- Methods declared in class javax.management.remote.

JMXConnectorServer

connectionClosed

,

connectionFailed

,

connectionOpened

,

getMBeanServer

,

getNotificationInfo

,

preDeregister

,

preRegister

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

Activates the connector server, that is starts listening for
client connections.

Deactivates the connector server, that is, stops listening for
client connections.

Returns a client stub for this connector server.

Methods declared in class javax.management.remote.

JMXConnectorServer

connectionClosed

,

connectionFailed

,

connectionOpened

,

getMBeanServer

,

getNotificationInfo

,

preDeregister

,

preRegister

---

#### Methods declared in class javax.management.remote. JMXConnectorServer

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

- JNDI_REBIND_ATTRIBUTE

```java
public static final
String
JNDI_REBIND_ATTRIBUTE
```

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address. The value
associated with this attribute, if any, should be a string that
is equal, ignoring case, to

"true"

or

"false"

. The default value is false.

**See Also:** Constant Field Values

- RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

```java
public static final
String
RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE
```

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIClientSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:** Constant Field Values

- RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

```java
public static final
String
RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE
```

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIServerSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:** Constant Field Values

- CREDENTIAL_TYPES

```java
@Deprecated
(
since
="10",

forRemoval
=true)
public static final
String
CREDENTIAL_TYPES
```

Deprecated, for removal: This API element is subject to removal in a future version.

Use

CREDENTIALS_FILTER_PATTERN

with a

filter pattern

string instead.

Name of the attribute that specifies a list of class names acceptable
as parameters to the

RMIServer.newClient()

remote method call.

This list of classes should correspond to the transitive closure of the
credentials class (or classes) used by the installed

JMXAuthenticator

associated with the

RMIServer

implementation.

If the attribute is not set, or is null, then any class is
deemed acceptable.

**See Also:** Constant Field Values

- CREDENTIALS_FILTER_PATTERN

```java
public static final
String
CREDENTIALS_FILTER_PATTERN
```

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

The filter pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

This list of classes allowed by filter should correspond to the
transitive closure of the credentials class (or classes) used by the
installed

JMXAuthenticator

associated with the

RMIServer

implementation.
If the attribute is not set then any class is deemed acceptable.

**See Also:** ObjectInputFilter

,

Constant Field Values

- SERIAL_FILTER_PATTERN

```java
public static final
String
SERIAL_FILTER_PATTERN
```

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

The filter will be called for any class found in the serialized
stream sent to server by client, including all JMX defined classes
(such as

ObjectName

), all method parameters,
and, if present in the stream, all classes transitively referred by
the serial form of any deserialized object.
The pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

.
It may define an allow-list of permitted classes, a reject-list of
rejected classes, a maximum depth for the deserialized objects,
etc.

To be functional, the filter should allow at least all the
concrete types in the transitive closure of all objects that
might get serialized when serializing all JMX classes referred
as parameters in the

RMIConnection

interface,
plus all classes that a

client

might need to transmit wrapped in

marshalled objects

in order to interoperate with the MBeans registered
in the

MBeanServer

. That would potentially include all the
concrete

JMX OpenTypes

and the
classes they use in their serial form.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment)
throws
IOException
```

Makes an

RMIConnectorServer

.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,null)

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid when
this constructor is used.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

- RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException
```

Makes an

RMIConnectorServer

for the given MBean
server.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,mbeanServer)

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Parameters:** mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid
when this constructor is used.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

- RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

RMIServerImpl
rmiServerImpl,

MBeanServer
mbeanServer)
throws
IOException
```

Makes an

RMIConnectorServer

for the given MBean
server.

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Parameters:** rmiServerImpl

- An implementation of the RMIServer interface,
consistent with the protocol type specified in

url

.
If this parameter is non null, the protocol type specified by

url

is not constrained, and is assumed to be valid.
Otherwise, only "rmi" will be recognized.
**Parameters:** mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is recognized
when

rmiServerImpl

is null.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.
**See Also:** start()

============ METHOD DETAIL ==========

- Method Detail

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

**Specified by:** toJMXConnector

in interface

JMXConnectorServerMBean
**Overrides:** toJMXConnector

in class

JMXConnectorServer
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

- start

```java
public void start()
throws
IOException
```

Activates the connector server, that is starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

The behavior of this method when called for the first time
depends on the parameters that were supplied at construction,
as described below.

First, an object of a subclass of

RMIServerImpl

is
required, to export the connector server through RMI:

- If an

RMIServerImpl

was supplied to the
constructor, it is used.

Otherwise, if the

JMXServiceURL

was null, or its protocol part was

rmi

, an object
of type

RMIJRMPServerImpl

is created.

Otherwise, the implementation can create an
implementation-specific

RMIServerImpl

or it can throw

MalformedURLException

.

If the given address includes a JNDI directory URL as
specified in the package documentation for

javax.management.remote.rmi

, then this

RMIConnectorServer

will bootstrap by binding the

RMIServerImpl

to the given address.

If the URL path part of the

JMXServiceURL

was
empty or a single slash (

/

), then the RMI object
will not be bound to a directory. Instead, a reference to it
will be encoded in the URL path of the RMIConnectorServer
address (returned by

JMXConnectorServerMBean.getAddress()

). The encodings for

rmi

are described in the package documentation for

javax.management.remote.rmi

.

The behavior when the URL path is neither empty nor a JNDI
directory URL, or when the protocol is not

rmi

,
is implementation defined, and may include throwing

MalformedURLException

when the connector server is created
or when it is started.

**Throws:** IllegalStateException

- if the connector server has
not been attached to an MBean server.
**Throws:** IOException

- if the connector server cannot be
started.

- stop

```java
public void stop()
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

is emitted from this MBean with the
connection ID of the connection that could not be closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

This method calls the method

close

on the connector server's

RMIServerImpl

object.

If the

RMIServerImpl

was bound to a JNDI
directory by the

start

method, it is unbound
from the directory by this method.

**Throws:** IOException

- if the server cannot be closed cleanly,
or if the

RMIServerImpl

cannot be unbound from the
directory. When this exception is thrown, the server has
already attempted to close all client connections, if
appropriate; to call

RMIServerImpl.close()

; and to
unbind the

RMIServerImpl

from its directory, if
appropriate. All client connections are closed except possibly
those that generated exceptions when the server attempted to
close them.

Field Detail

- JNDI_REBIND_ATTRIBUTE

```java
public static final
String
JNDI_REBIND_ATTRIBUTE
```

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address. The value
associated with this attribute, if any, should be a string that
is equal, ignoring case, to

"true"

or

"false"

. The default value is false.

**See Also:** Constant Field Values

- RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

```java
public static final
String
RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE
```

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIClientSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:** Constant Field Values

- RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

```java
public static final
String
RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE
```

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIServerSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:** Constant Field Values

- CREDENTIAL_TYPES

```java
@Deprecated
(
since
="10",

forRemoval
=true)
public static final
String
CREDENTIAL_TYPES
```

Deprecated, for removal: This API element is subject to removal in a future version.

Use

CREDENTIALS_FILTER_PATTERN

with a

filter pattern

string instead.

Name of the attribute that specifies a list of class names acceptable
as parameters to the

RMIServer.newClient()

remote method call.

This list of classes should correspond to the transitive closure of the
credentials class (or classes) used by the installed

JMXAuthenticator

associated with the

RMIServer

implementation.

If the attribute is not set, or is null, then any class is
deemed acceptable.

**See Also:** Constant Field Values

- CREDENTIALS_FILTER_PATTERN

```java
public static final
String
CREDENTIALS_FILTER_PATTERN
```

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

The filter pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

This list of classes allowed by filter should correspond to the
transitive closure of the credentials class (or classes) used by the
installed

JMXAuthenticator

associated with the

RMIServer

implementation.
If the attribute is not set then any class is deemed acceptable.

**See Also:** ObjectInputFilter

,

Constant Field Values

- SERIAL_FILTER_PATTERN

```java
public static final
String
SERIAL_FILTER_PATTERN
```

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

The filter will be called for any class found in the serialized
stream sent to server by client, including all JMX defined classes
(such as

ObjectName

), all method parameters,
and, if present in the stream, all classes transitively referred by
the serial form of any deserialized object.
The pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

.
It may define an allow-list of permitted classes, a reject-list of
rejected classes, a maximum depth for the deserialized objects,
etc.

To be functional, the filter should allow at least all the
concrete types in the transitive closure of all objects that
might get serialized when serializing all JMX classes referred
as parameters in the

RMIConnection

interface,
plus all classes that a

client

might need to transmit wrapped in

marshalled objects

in order to interoperate with the MBeans registered
in the

MBeanServer

. That would potentially include all the
concrete

JMX OpenTypes

and the
classes they use in their serial form.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

**See Also:** Constant Field Values

---

#### Field Detail

JNDI_REBIND_ATTRIBUTE

```java
public static final
String
JNDI_REBIND_ATTRIBUTE
```

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address. The value
associated with this attribute, if any, should be a string that
is equal, ignoring case, to

"true"

or

"false"

. The default value is false.

**See Also:** Constant Field Values

---

#### JNDI_REBIND_ATTRIBUTE

public static final

String

JNDI_REBIND_ATTRIBUTE

Name of the attribute that specifies whether the

RMIServer

stub that represents an RMI connector server should
override an existing stub at the same address. The value
associated with this attribute, if any, should be a string that
is equal, ignoring case, to

"true"

or

"false"

. The default value is false.

RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

```java
public static final
String
RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE
```

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIClientSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:** Constant Field Values

---

#### RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

public static final

String

RMI_CLIENT_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIClientSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIClientSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

```java
public static final
String
RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE
```

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIServerSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

**See Also:** Constant Field Values

---

#### RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

public static final

String

RMI_SERVER_SOCKET_FACTORY_ATTRIBUTE

Name of the attribute that specifies the

RMIServerSocketFactory

for the RMI objects created in
conjunction with this connector. The value associated with this
attribute must be of type

RMIServerSocketFactory

and can
only be specified in the

Map

argument supplied when
creating a connector server.

CREDENTIAL_TYPES

```java
@Deprecated
(
since
="10",

forRemoval
=true)
public static final
String
CREDENTIAL_TYPES
```

Deprecated, for removal: This API element is subject to removal in a future version.

Use

CREDENTIALS_FILTER_PATTERN

with a

filter pattern

string instead.

Name of the attribute that specifies a list of class names acceptable
as parameters to the

RMIServer.newClient()

remote method call.

This list of classes should correspond to the transitive closure of the
credentials class (or classes) used by the installed

JMXAuthenticator

associated with the

RMIServer

implementation.

If the attribute is not set, or is null, then any class is
deemed acceptable.

**See Also:** Constant Field Values

---

#### CREDENTIAL_TYPES

@Deprecated

(

since

="10",

forRemoval

=true)
public static final

String

CREDENTIAL_TYPES

Name of the attribute that specifies a list of class names acceptable
as parameters to the

RMIServer.newClient()

remote method call.

This list of classes should correspond to the transitive closure of the
credentials class (or classes) used by the installed

JMXAuthenticator

associated with the

RMIServer

implementation.

If the attribute is not set, or is null, then any class is
deemed acceptable.

This list of classes should correspond to the transitive closure of the
credentials class (or classes) used by the installed

JMXAuthenticator

associated with the

RMIServer

implementation.

If the attribute is not set, or is null, then any class is
deemed acceptable.

If the attribute is not set, or is null, then any class is
deemed acceptable.

CREDENTIALS_FILTER_PATTERN

```java
public static final
String
CREDENTIALS_FILTER_PATTERN
```

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

The filter pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

This list of classes allowed by filter should correspond to the
transitive closure of the credentials class (or classes) used by the
installed

JMXAuthenticator

associated with the

RMIServer

implementation.
If the attribute is not set then any class is deemed acceptable.

**See Also:** ObjectInputFilter

,

Constant Field Values

---

#### CREDENTIALS_FILTER_PATTERN

public static final

String

CREDENTIALS_FILTER_PATTERN

Name of the attribute that specifies an

ObjectInputFilter

pattern string to filter classes acceptable
for

RMIServer.newClient()

remote method call.

The filter pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

This list of classes allowed by filter should correspond to the
transitive closure of the credentials class (or classes) used by the
installed

JMXAuthenticator

associated with the

RMIServer

implementation.
If the attribute is not set then any class is deemed acceptable.

The filter pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

This list of classes allowed by filter should correspond to the
transitive closure of the credentials class (or classes) used by the
installed

JMXAuthenticator

associated with the

RMIServer

implementation.
If the attribute is not set then any class is deemed acceptable.

This list of classes allowed by filter should correspond to the
transitive closure of the credentials class (or classes) used by the
installed

JMXAuthenticator

associated with the

RMIServer

implementation.
If the attribute is not set then any class is deemed acceptable.

SERIAL_FILTER_PATTERN

```java
public static final
String
SERIAL_FILTER_PATTERN
```

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

The filter will be called for any class found in the serialized
stream sent to server by client, including all JMX defined classes
(such as

ObjectName

), all method parameters,
and, if present in the stream, all classes transitively referred by
the serial form of any deserialized object.
The pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

.
It may define an allow-list of permitted classes, a reject-list of
rejected classes, a maximum depth for the deserialized objects,
etc.

To be functional, the filter should allow at least all the
concrete types in the transitive closure of all objects that
might get serialized when serializing all JMX classes referred
as parameters in the

RMIConnection

interface,
plus all classes that a

client

might need to transmit wrapped in

marshalled objects

in order to interoperate with the MBeans registered
in the

MBeanServer

. That would potentially include all the
concrete

JMX OpenTypes

and the
classes they use in their serial form.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

**See Also:** Constant Field Values

---

#### SERIAL_FILTER_PATTERN

public static final

String

SERIAL_FILTER_PATTERN

This attribute defines a pattern from which to create a

ObjectInputFilter

that will be used when deserializing
objects sent to the

JMXConnectorServer

by any client.

The filter will be called for any class found in the serialized
stream sent to server by client, including all JMX defined classes
(such as

ObjectName

), all method parameters,
and, if present in the stream, all classes transitively referred by
the serial form of any deserialized object.
The pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

.
It may define an allow-list of permitted classes, a reject-list of
rejected classes, a maximum depth for the deserialized objects,
etc.

To be functional, the filter should allow at least all the
concrete types in the transitive closure of all objects that
might get serialized when serializing all JMX classes referred
as parameters in the

RMIConnection

interface,
plus all classes that a

client

might need to transmit wrapped in

marshalled objects

in order to interoperate with the MBeans registered
in the

MBeanServer

. That would potentially include all the
concrete

JMX OpenTypes

and the
classes they use in their serial form.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

The filter will be called for any class found in the serialized
stream sent to server by client, including all JMX defined classes
(such as

ObjectName

), all method parameters,
and, if present in the stream, all classes transitively referred by
the serial form of any deserialized object.
The pattern must be in same format as used in

ObjectInputFilter.Config.createFilter(java.lang.String)

.
It may define an allow-list of permitted classes, a reject-list of
rejected classes, a maximum depth for the deserialized objects,
etc.

To be functional, the filter should allow at least all the
concrete types in the transitive closure of all objects that
might get serialized when serializing all JMX classes referred
as parameters in the

RMIConnection

interface,
plus all classes that a

client

might need to transmit wrapped in

marshalled objects

in order to interoperate with the MBeans registered
in the

MBeanServer

. That would potentially include all the
concrete

JMX OpenTypes

and the
classes they use in their serial form.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

To be functional, the filter should allow at least all the
concrete types in the transitive closure of all objects that
might get serialized when serializing all JMX classes referred
as parameters in the

RMIConnection

interface,
plus all classes that a

client

might need to transmit wrapped in

marshalled objects

in order to interoperate with the MBeans registered
in the

MBeanServer

. That would potentially include all the
concrete

JMX OpenTypes

and the
classes they use in their serial form.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

Care must be taken when defining such a filter, as defining
an allow-list that is too narrow or a reject-list that is too wide may
prevent legitimate clients from interoperating with the

JMXConnectorServer

.

Constructor Detail

- RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment)
throws
IOException
```

Makes an

RMIConnectorServer

.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,null)

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid when
this constructor is used.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

- RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException
```

Makes an

RMIConnectorServer

for the given MBean
server.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,mbeanServer)

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Parameters:** mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid
when this constructor is used.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

- RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

RMIServerImpl
rmiServerImpl,

MBeanServer
mbeanServer)
throws
IOException
```

Makes an

RMIConnectorServer

for the given MBean
server.

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Parameters:** rmiServerImpl

- An implementation of the RMIServer interface,
consistent with the protocol type specified in

url

.
If this parameter is non null, the protocol type specified by

url

is not constrained, and is assumed to be valid.
Otherwise, only "rmi" will be recognized.
**Parameters:** mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is recognized
when

rmiServerImpl

is null.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.
**See Also:** start()

---

#### Constructor Detail

RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment)
throws
IOException
```

Makes an

RMIConnectorServer

.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,null)

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid when
this constructor is used.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

---

#### RMIConnectorServer

public RMIConnectorServer​(

JMXServiceURL

url,

Map

<

String

,​?> environment)
throws

IOException

Makes an

RMIConnectorServer

.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,null)

RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException
```

Makes an

RMIConnectorServer

for the given MBean
server.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,mbeanServer)

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Parameters:** mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is valid
when this constructor is used.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.

---

#### RMIConnectorServer

public RMIConnectorServer​(

JMXServiceURL

url,

Map

<

String

,​?> environment,

MBeanServer

mbeanServer)
throws

IOException

Makes an

RMIConnectorServer

for the given MBean
server.
This is equivalent to calling

RMIConnectorServer(directoryURL,environment,null,mbeanServer)

RMIConnectorServer

```java
public RMIConnectorServer​(
JMXServiceURL
url,

Map
<
String
,​?> environment,

RMIServerImpl
rmiServerImpl,

MBeanServer
mbeanServer)
throws
IOException
```

Makes an

RMIConnectorServer

for the given MBean
server.

**Parameters:** url

- the URL defining how to create the connector server.
Cannot be null.
**Parameters:** environment

- attributes governing the creation and
storing of the RMI object. Can be null, which is equivalent to
an empty Map.
**Parameters:** rmiServerImpl

- An implementation of the RMIServer interface,
consistent with the protocol type specified in

url

.
If this parameter is non null, the protocol type specified by

url

is not constrained, and is assumed to be valid.
Otherwise, only "rmi" will be recognized.
**Parameters:** mbeanServer

- the MBean server to which the new connector
server is attached, or null if it will be attached by being
registered as an MBean in the MBean server.
**Throws:** IllegalArgumentException

- if

url

is null.
**Throws:** MalformedURLException

- if

url

does not
conform to the syntax for an RMI connector, or if its protocol
is not recognized by this implementation. Only "rmi" is recognized
when

rmiServerImpl

is null.
**Throws:** IOException

- if the connector server cannot be created
for some reason or if it is inevitable that its

start

method will fail.
**See Also:** start()

---

#### RMIConnectorServer

public RMIConnectorServer​(

JMXServiceURL

url,

Map

<

String

,​?> environment,

RMIServerImpl

rmiServerImpl,

MBeanServer

mbeanServer)
throws

IOException

Makes an

RMIConnectorServer

for the given MBean
server.

Method Detail

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

**Specified by:** toJMXConnector

in interface

JMXConnectorServerMBean
**Overrides:** toJMXConnector

in class

JMXConnectorServer
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

- start

```java
public void start()
throws
IOException
```

Activates the connector server, that is starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

The behavior of this method when called for the first time
depends on the parameters that were supplied at construction,
as described below.

First, an object of a subclass of

RMIServerImpl

is
required, to export the connector server through RMI:

- If an

RMIServerImpl

was supplied to the
constructor, it is used.

Otherwise, if the

JMXServiceURL

was null, or its protocol part was

rmi

, an object
of type

RMIJRMPServerImpl

is created.

Otherwise, the implementation can create an
implementation-specific

RMIServerImpl

or it can throw

MalformedURLException

.

If the given address includes a JNDI directory URL as
specified in the package documentation for

javax.management.remote.rmi

, then this

RMIConnectorServer

will bootstrap by binding the

RMIServerImpl

to the given address.

If the URL path part of the

JMXServiceURL

was
empty or a single slash (

/

), then the RMI object
will not be bound to a directory. Instead, a reference to it
will be encoded in the URL path of the RMIConnectorServer
address (returned by

JMXConnectorServerMBean.getAddress()

). The encodings for

rmi

are described in the package documentation for

javax.management.remote.rmi

.

The behavior when the URL path is neither empty nor a JNDI
directory URL, or when the protocol is not

rmi

,
is implementation defined, and may include throwing

MalformedURLException

when the connector server is created
or when it is started.

**Throws:** IllegalStateException

- if the connector server has
not been attached to an MBean server.
**Throws:** IOException

- if the connector server cannot be
started.

- stop

```java
public void stop()
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

is emitted from this MBean with the
connection ID of the connection that could not be closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

This method calls the method

close

on the connector server's

RMIServerImpl

object.

If the

RMIServerImpl

was bound to a JNDI
directory by the

start

method, it is unbound
from the directory by this method.

**Throws:** IOException

- if the server cannot be closed cleanly,
or if the

RMIServerImpl

cannot be unbound from the
directory. When this exception is thrown, the server has
already attempted to close all client connections, if
appropriate; to call

RMIServerImpl.close()

; and to
unbind the

RMIServerImpl

from its directory, if
appropriate. All client connections are closed except possibly
those that generated exceptions when the server attempted to
close them.

---

#### Method Detail

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

**Specified by:** toJMXConnector

in interface

JMXConnectorServerMBean
**Overrides:** toJMXConnector

in class

JMXConnectorServer
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

start

```java
public void start()
throws
IOException
```

Activates the connector server, that is starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

The behavior of this method when called for the first time
depends on the parameters that were supplied at construction,
as described below.

First, an object of a subclass of

RMIServerImpl

is
required, to export the connector server through RMI:

- If an

RMIServerImpl

was supplied to the
constructor, it is used.

Otherwise, if the

JMXServiceURL

was null, or its protocol part was

rmi

, an object
of type

RMIJRMPServerImpl

is created.

Otherwise, the implementation can create an
implementation-specific

RMIServerImpl

or it can throw

MalformedURLException

.

If the given address includes a JNDI directory URL as
specified in the package documentation for

javax.management.remote.rmi

, then this

RMIConnectorServer

will bootstrap by binding the

RMIServerImpl

to the given address.

If the URL path part of the

JMXServiceURL

was
empty or a single slash (

/

), then the RMI object
will not be bound to a directory. Instead, a reference to it
will be encoded in the URL path of the RMIConnectorServer
address (returned by

JMXConnectorServerMBean.getAddress()

). The encodings for

rmi

are described in the package documentation for

javax.management.remote.rmi

.

The behavior when the URL path is neither empty nor a JNDI
directory URL, or when the protocol is not

rmi

,
is implementation defined, and may include throwing

MalformedURLException

when the connector server is created
or when it is started.

**Throws:** IllegalStateException

- if the connector server has
not been attached to an MBean server.
**Throws:** IOException

- if the connector server cannot be
started.

---

#### start

public void start()
throws

IOException

Activates the connector server, that is starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

The behavior of this method when called for the first time
depends on the parameters that were supplied at construction,
as described below.

First, an object of a subclass of

RMIServerImpl

is
required, to export the connector server through RMI:

- If an

RMIServerImpl

was supplied to the
constructor, it is used.

Otherwise, if the

JMXServiceURL

was null, or its protocol part was

rmi

, an object
of type

RMIJRMPServerImpl

is created.

Otherwise, the implementation can create an
implementation-specific

RMIServerImpl

or it can throw

MalformedURLException

.

If the given address includes a JNDI directory URL as
specified in the package documentation for

javax.management.remote.rmi

, then this

RMIConnectorServer

will bootstrap by binding the

RMIServerImpl

to the given address.

If the URL path part of the

JMXServiceURL

was
empty or a single slash (

/

), then the RMI object
will not be bound to a directory. Instead, a reference to it
will be encoded in the URL path of the RMIConnectorServer
address (returned by

JMXConnectorServerMBean.getAddress()

). The encodings for

rmi

are described in the package documentation for

javax.management.remote.rmi

.

The behavior when the URL path is neither empty nor a JNDI
directory URL, or when the protocol is not

rmi

,
is implementation defined, and may include throwing

MalformedURLException

when the connector server is created
or when it is started.

Activates the connector server, that is starts listening for
client connections. Calling this method when the connector
server is already active has no effect. Calling this method
when the connector server has been stopped will generate an

IOException

.

The behavior of this method when called for the first time
depends on the parameters that were supplied at construction,
as described below.

First, an object of a subclass of

RMIServerImpl

is
required, to export the connector server through RMI:

If an

RMIServerImpl

was supplied to the
constructor, it is used.

Otherwise, if the

JMXServiceURL

was null, or its protocol part was

rmi

, an object
of type

RMIJRMPServerImpl

is created.

Otherwise, the implementation can create an
implementation-specific

RMIServerImpl

or it can throw

MalformedURLException

.

If the given address includes a JNDI directory URL as
specified in the package documentation for

javax.management.remote.rmi

, then this

RMIConnectorServer

will bootstrap by binding the

RMIServerImpl

to the given address.

If the URL path part of the

JMXServiceURL

was
empty or a single slash (

/

), then the RMI object
will not be bound to a directory. Instead, a reference to it
will be encoded in the URL path of the RMIConnectorServer
address (returned by

JMXConnectorServerMBean.getAddress()

). The encodings for

rmi

are described in the package documentation for

javax.management.remote.rmi

.

The behavior when the URL path is neither empty nor a JNDI
directory URL, or when the protocol is not

rmi

,
is implementation defined, and may include throwing

MalformedURLException

when the connector server is created
or when it is started.

stop

```java
public void stop()
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

is emitted from this MBean with the
connection ID of the connection that could not be closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

This method calls the method

close

on the connector server's

RMIServerImpl

object.

If the

RMIServerImpl

was bound to a JNDI
directory by the

start

method, it is unbound
from the directory by this method.

**Throws:** IOException

- if the server cannot be closed cleanly,
or if the

RMIServerImpl

cannot be unbound from the
directory. When this exception is thrown, the server has
already attempted to close all client connections, if
appropriate; to call

RMIServerImpl.close()

; and to
unbind the

RMIServerImpl

from its directory, if
appropriate. All client connections are closed except possibly
those that generated exceptions when the server attempted to
close them.

---

#### stop

public void stop()
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

is emitted from this MBean with the
connection ID of the connection that could not be closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

This method calls the method

close

on the connector server's

RMIServerImpl

object.

If the

RMIServerImpl

was bound to a JNDI
directory by the

start

method, it is unbound
from the directory by this method.

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

is emitted from this MBean with the
connection ID of the connection that could not be closed.

Closing a connector server is a potentially slow operation.
For example, if a client machine with an open connection has
crashed, the close operation might have to wait for a network
protocol timeout. Callers that do not want to block in a close
operation should do it in a separate thread.

This method calls the method

close

on the connector server's

RMIServerImpl

object.

If the

RMIServerImpl

was bound to a JNDI
directory by the

start

method, it is unbound
from the directory by this method.

---

