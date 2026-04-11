# Interface JMXConnector

**Source:** `java.management\javax\management\remote\JMXConnector.html`

### Class Description

```java
public interface
JMXConnector

extends
Closeable
```

The client end of a JMX API connector. An object of this type can
be used to establish a connection to a connector server.

A newly-created object of this type is unconnected. Its

connect

method must be called before it can be used.
However, objects created by

JMXConnectorFactory.connect

are already connected.

**All Superinterfaces:** AutoCloseable

,

Closeable

---

### Field Details

#### static final
String
CREDENTIALS

Name of the attribute that specifies the credentials to send
to the connector server during connection. The value
associated with this attribute, if any, is a serializable
object of an appropriate type for the server's

JMXAuthenticator

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void connect()
throws
IOException

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

**Throws:**
- IOException

- if the connection could not be made
because of a communication problem.
- SecurityException

- if the connection could not be
made for security reasons.

---

#### void connect​(
Map
<
String
,​?> env)
throws
IOException

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

close()

was called after

connect

, the new

connect

will throw an

IOException

.

Otherwise, either

connect

has never been called
on this object, or it has been called but produced an
exception. Then calling

connect

will attempt to
establish a connection to the connector server.

**Parameters:**
- env

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.

**Throws:**
- IOException

- if the connection could not be made
because of a communication problem.
- SecurityException

- if the connection could not be
made for security reasons.

---

#### MBeanServerConnection
getMBeanServerConnection()
throws
IOException

Returns an

MBeanServerConnection

object
representing a remote MBean server. For a given

JMXConnector

, two successful calls to this method
will usually return the same

MBeanServerConnection

object, though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server. The value returned by the MBean server method is the
value returned to the client. If the MBean server method
produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

Calling this method is equivalent to calling

getMBeanServerConnection(null)

meaning that no delegation subject is specified and that all the
operations called on the

MBeanServerConnection

must
use the authenticated subject, if any.

**Returns:**
- an object that implements the

MBeanServerConnection

interface by forwarding its
methods to the remote MBean server.

**Throws:**
- IOException

- if a valid

MBeanServerConnection

cannot be created, for
instance because the connection to the remote MBean server has
not yet been established (with the

connect

method), or it has been closed, or it has broken.

---

#### MBeanServerConnection
getMBeanServerConnection​(
Subject
delegationSubject)
throws
IOException

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject. For a given

JMXConnector

and

Subject

, two successful calls to this method will
usually return the same

MBeanServerConnection

object,
though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server on behalf of the given delegation subject instead of the
authenticated subject. The value returned by the MBean server
method is the value returned to the client. If the MBean server
method produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

**Parameters:**
- delegationSubject

- the

Subject

on behalf of
which requests will be performed. Can be null, in which case
requests will be performed on behalf of the authenticated
Subject, if any.

**Returns:**
- an object that implements the

MBeanServerConnection

interface by forwarding its methods to the remote MBean server on behalf
of a given delegation subject.

**Throws:**
- IOException

- if a valid

MBeanServerConnection

cannot be created, for instance because the connection to the remote
MBean server has not yet been established (with the

connect

method), or it has been closed, or it has broken.

---

#### void close()
throws
IOException

Closes the client connection to its server. Any ongoing or new
request using the MBeanServerConnection returned by

getMBeanServerConnection()

will get an

IOException

.

If

close

has already been called successfully
on this object, calling it again has no effect. If

close

has never been called, or if it was called
but produced an exception, an attempt will be made to close the
connection. This attempt can succeed, in which case

close

will return normally, or it can generate an
exception.

Closing a connection is a potentially slow operation. For
example, if the server has crashed, the close operation might
have to wait for a network protocol timeout. Callers that do
not want to block in a close operation should do it in a
separate thread.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Throws:**
- IOException

- if the connection cannot be closed
cleanly. If this exception is thrown, it is not known whether
the server end of the connection has been cleanly closed.

---

#### void addConnectionNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)

Adds a listener to be informed of changes in connection
status. The listener will receive notifications of type

JMXConnectionNotification

. An implementation can send other
types of notifications too.

Any number of listeners can be added with this method. The
same listener can be added more than once with the same or
different values for the filter and handback. There is no
special treatment of a duplicate entry. For example, if a
listener is registered twice with no filter, then its

handleNotification

method will be called twice for
each notification.

**Parameters:**
- listener

- a listener to receive connection status
notifications.
- filter

- a filter to select which notifications are to be
delivered to the listener, or null if all notifications are to
be delivered.
- handback

- an object to be given to the listener along
with each notification. Can be null.

**Throws:**
- NullPointerException

- if

listener

is
null.

**See Also:**
- removeConnectionNotificationListener(javax.management.NotificationListener)

,

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### void removeConnectionNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added. If
there is more than one matching listener, all are removed.

**Parameters:**
- listener

- a listener to receive connection status
notifications.

**Throws:**
- NullPointerException

- if

listener

is
null.
- ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

.

**See Also:**
- removeConnectionNotificationListener(NotificationListener,
NotificationFilter, Object)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### void removeConnectionNotificationListener​(
NotificationListener
l,

NotificationFilter
f,

Object
handback)
throws
ListenerNotFoundException

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added with
the same three parameters. If there is more than one matching
listener, only one is removed.

**Parameters:**
- l

- a listener to receive connection status notifications.
- f

- a filter to select which notifications are to be
delivered to the listener. Can be null.
- handback

- an object to be given to the listener along
with each notification. Can be null.

**Throws:**
- ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

, or is not
registered with the given filter and handback.

**See Also:**
- removeConnectionNotificationListener(NotificationListener)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### String
getConnectionId()
throws
IOException

Gets this connection's ID from the connector server. For a
given connector server, every connection will have a unique id
which does not change during the lifetime of the
connection.

**Returns:**
- the unique ID of this connection. This is the same as
the ID that the connector server includes in its

JMXConnectionNotification

s. The

package description

describes the
conventions for connection IDs.

**Throws:**
- IOException

- if the connection ID cannot be obtained,
for instance because the connection is closed or broken.

---

### Additional Sections

#### Interface JMXConnector

**All Superinterfaces:** AutoCloseable

,

Closeable

**All Known Implementing Classes:** RMIConnector

```java
public interface
JMXConnector

extends
Closeable
```

The client end of a JMX API connector. An object of this type can
be used to establish a connection to a connector server.

A newly-created object of this type is unconnected. Its

connect

method must be called before it can be used.
However, objects created by

JMXConnectorFactory.connect

are already connected.

**Since:** 1.5

public interface

JMXConnector

extends

Closeable

The client end of a JMX API connector. An object of this type can
be used to establish a connection to a connector server.

A newly-created object of this type is unconnected. Its

connect

method must be called before it can be used.
However, objects created by

JMXConnectorFactory.connect

are already connected.

The client end of a JMX API connector. An object of this type can
be used to establish a connection to a connector server.

A newly-created object of this type is unconnected. Its

connect

method must be called before it can be used.
However, objects created by

JMXConnectorFactory.connect

are already connected.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

CREDENTIALS

Name of the attribute that specifies the credentials to send
to the connector server during connection.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addConnectionNotificationListener

​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to be informed of changes in connection
status.

void

close

()

Closes the client connection to its server.

void

connect

()

Establishes the connection to the connector server.

void

connect

​(

Map

<

String

,​?> env)

Establishes the connection to the connector server.

String

getConnectionId

()

Gets this connection's ID from the connector server.

MBeanServerConnection

getMBeanServerConnection

()

Returns an

MBeanServerConnection

object
representing a remote MBean server.

MBeanServerConnection

getMBeanServerConnection

​(

Subject

delegationSubject)

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject.

void

removeConnectionNotificationListener

​(

NotificationListener

listener)

Removes a listener from the list to be informed of changes
in status.

void

removeConnectionNotificationListener

​(

NotificationListener

l,

NotificationFilter

f,

Object

handback)

Removes a listener from the list to be informed of changes
in status.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

CREDENTIALS

Name of the attribute that specifies the credentials to send
to the connector server during connection.

---

#### Field Summary

Name of the attribute that specifies the credentials to send
to the connector server during connection.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addConnectionNotificationListener

​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to be informed of changes in connection
status.

void

close

()

Closes the client connection to its server.

void

connect

()

Establishes the connection to the connector server.

void

connect

​(

Map

<

String

,​?> env)

Establishes the connection to the connector server.

String

getConnectionId

()

Gets this connection's ID from the connector server.

MBeanServerConnection

getMBeanServerConnection

()

Returns an

MBeanServerConnection

object
representing a remote MBean server.

MBeanServerConnection

getMBeanServerConnection

​(

Subject

delegationSubject)

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject.

void

removeConnectionNotificationListener

​(

NotificationListener

listener)

Removes a listener from the list to be informed of changes
in status.

void

removeConnectionNotificationListener

​(

NotificationListener

l,

NotificationFilter

f,

Object

handback)

Removes a listener from the list to be informed of changes
in status.

---

#### Method Summary

Adds a listener to be informed of changes in connection
status.

Closes the client connection to its server.

Establishes the connection to the connector server.

Gets this connection's ID from the connector server.

Returns an

MBeanServerConnection

object
representing a remote MBean server.

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject.

Removes a listener from the list to be informed of changes
in status.

============ FIELD DETAIL ===========

- Field Detail

- CREDENTIALS

```java
static final
String
CREDENTIALS
```

Name of the attribute that specifies the credentials to send
to the connector server during connection. The value
associated with this attribute, if any, is a serializable
object of an appropriate type for the server's

JMXAuthenticator

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- connect

```java
void connect()
throws
IOException
```

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

**Throws:** IOException

- if the connection could not be made
because of a communication problem.
**Throws:** SecurityException

- if the connection could not be
made for security reasons.

- connect

```java
void connect​(
Map
<
String
,​?> env)
throws
IOException
```

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

close()

was called after

connect

, the new

connect

will throw an

IOException

.

Otherwise, either

connect

has never been called
on this object, or it has been called but produced an
exception. Then calling

connect

will attempt to
establish a connection to the connector server.

**Parameters:** env

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.
**Throws:** IOException

- if the connection could not be made
because of a communication problem.
**Throws:** SecurityException

- if the connection could not be
made for security reasons.

- getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection()
throws
IOException
```

Returns an

MBeanServerConnection

object
representing a remote MBean server. For a given

JMXConnector

, two successful calls to this method
will usually return the same

MBeanServerConnection

object, though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server. The value returned by the MBean server method is the
value returned to the client. If the MBean server method
produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

Calling this method is equivalent to calling

getMBeanServerConnection(null)

meaning that no delegation subject is specified and that all the
operations called on the

MBeanServerConnection

must
use the authenticated subject, if any.

**Returns:** an object that implements the

MBeanServerConnection

interface by forwarding its
methods to the remote MBean server.
**Throws:** IOException

- if a valid

MBeanServerConnection

cannot be created, for
instance because the connection to the remote MBean server has
not yet been established (with the

connect

method), or it has been closed, or it has broken.

- getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection​(
Subject
delegationSubject)
throws
IOException
```

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject. For a given

JMXConnector

and

Subject

, two successful calls to this method will
usually return the same

MBeanServerConnection

object,
though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server on behalf of the given delegation subject instead of the
authenticated subject. The value returned by the MBean server
method is the value returned to the client. If the MBean server
method produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

**Parameters:** delegationSubject

- the

Subject

on behalf of
which requests will be performed. Can be null, in which case
requests will be performed on behalf of the authenticated
Subject, if any.
**Returns:** an object that implements the

MBeanServerConnection

interface by forwarding its methods to the remote MBean server on behalf
of a given delegation subject.
**Throws:** IOException

- if a valid

MBeanServerConnection

cannot be created, for instance because the connection to the remote
MBean server has not yet been established (with the

connect

method), or it has been closed, or it has broken.

- close

```java
void close()
throws
IOException
```

Closes the client connection to its server. Any ongoing or new
request using the MBeanServerConnection returned by

getMBeanServerConnection()

will get an

IOException

.

If

close

has already been called successfully
on this object, calling it again has no effect. If

close

has never been called, or if it was called
but produced an exception, an attempt will be made to close the
connection. This attempt can succeed, in which case

close

will return normally, or it can generate an
exception.

Closing a connection is a potentially slow operation. For
example, if the server has crashed, the close operation might
have to wait for a network protocol timeout. Callers that do
not want to block in a close operation should do it in a
separate thread.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if the connection cannot be closed
cleanly. If this exception is thrown, it is not known whether
the server end of the connection has been cleanly closed.

- addConnectionNotificationListener

```java
void addConnectionNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
```

Adds a listener to be informed of changes in connection
status. The listener will receive notifications of type

JMXConnectionNotification

. An implementation can send other
types of notifications too.

Any number of listeners can be added with this method. The
same listener can be added more than once with the same or
different values for the filter and handback. There is no
special treatment of a duplicate entry. For example, if a
listener is registered twice with no filter, then its

handleNotification

method will be called twice for
each notification.

**Parameters:** listener

- a listener to receive connection status
notifications.
**Parameters:** filter

- a filter to select which notifications are to be
delivered to the listener, or null if all notifications are to
be delivered.
**Parameters:** handback

- an object to be given to the listener along
with each notification. Can be null.
**Throws:** NullPointerException

- if

listener

is
null.
**See Also:** removeConnectionNotificationListener(javax.management.NotificationListener)

,

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- removeConnectionNotificationListener

```java
void removeConnectionNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added. If
there is more than one matching listener, all are removed.

**Parameters:** listener

- a listener to receive connection status
notifications.
**Throws:** NullPointerException

- if

listener

is
null.
**Throws:** ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

.
**See Also:** removeConnectionNotificationListener(NotificationListener,
NotificationFilter, Object)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- removeConnectionNotificationListener

```java
void removeConnectionNotificationListener​(
NotificationListener
l,

NotificationFilter
f,

Object
handback)
throws
ListenerNotFoundException
```

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added with
the same three parameters. If there is more than one matching
listener, only one is removed.

**Parameters:** l

- a listener to receive connection status notifications.
**Parameters:** f

- a filter to select which notifications are to be
delivered to the listener. Can be null.
**Parameters:** handback

- an object to be given to the listener along
with each notification. Can be null.
**Throws:** ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

, or is not
registered with the given filter and handback.
**See Also:** removeConnectionNotificationListener(NotificationListener)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- getConnectionId

```java
String
getConnectionId()
throws
IOException
```

Gets this connection's ID from the connector server. For a
given connector server, every connection will have a unique id
which does not change during the lifetime of the
connection.

**Returns:** the unique ID of this connection. This is the same as
the ID that the connector server includes in its

JMXConnectionNotification

s. The

package description

describes the
conventions for connection IDs.
**Throws:** IOException

- if the connection ID cannot be obtained,
for instance because the connection is closed or broken.

Field Detail

- CREDENTIALS

```java
static final
String
CREDENTIALS
```

Name of the attribute that specifies the credentials to send
to the connector server during connection. The value
associated with this attribute, if any, is a serializable
object of an appropriate type for the server's

JMXAuthenticator

.

**See Also:** Constant Field Values

---

#### Field Detail

CREDENTIALS

```java
static final
String
CREDENTIALS
```

Name of the attribute that specifies the credentials to send
to the connector server during connection. The value
associated with this attribute, if any, is a serializable
object of an appropriate type for the server's

JMXAuthenticator

.

**See Also:** Constant Field Values

---

#### CREDENTIALS

static final

String

CREDENTIALS

Name of the attribute that specifies the credentials to send
to the connector server during connection. The value
associated with this attribute, if any, is a serializable
object of an appropriate type for the server's

JMXAuthenticator

.

Method Detail

- connect

```java
void connect()
throws
IOException
```

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

**Throws:** IOException

- if the connection could not be made
because of a communication problem.
**Throws:** SecurityException

- if the connection could not be
made for security reasons.

- connect

```java
void connect​(
Map
<
String
,​?> env)
throws
IOException
```

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

close()

was called after

connect

, the new

connect

will throw an

IOException

.

Otherwise, either

connect

has never been called
on this object, or it has been called but produced an
exception. Then calling

connect

will attempt to
establish a connection to the connector server.

**Parameters:** env

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.
**Throws:** IOException

- if the connection could not be made
because of a communication problem.
**Throws:** SecurityException

- if the connection could not be
made for security reasons.

- getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection()
throws
IOException
```

Returns an

MBeanServerConnection

object
representing a remote MBean server. For a given

JMXConnector

, two successful calls to this method
will usually return the same

MBeanServerConnection

object, though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server. The value returned by the MBean server method is the
value returned to the client. If the MBean server method
produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

Calling this method is equivalent to calling

getMBeanServerConnection(null)

meaning that no delegation subject is specified and that all the
operations called on the

MBeanServerConnection

must
use the authenticated subject, if any.

**Returns:** an object that implements the

MBeanServerConnection

interface by forwarding its
methods to the remote MBean server.
**Throws:** IOException

- if a valid

MBeanServerConnection

cannot be created, for
instance because the connection to the remote MBean server has
not yet been established (with the

connect

method), or it has been closed, or it has broken.

- getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection​(
Subject
delegationSubject)
throws
IOException
```

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject. For a given

JMXConnector

and

Subject

, two successful calls to this method will
usually return the same

MBeanServerConnection

object,
though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server on behalf of the given delegation subject instead of the
authenticated subject. The value returned by the MBean server
method is the value returned to the client. If the MBean server
method produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

**Parameters:** delegationSubject

- the

Subject

on behalf of
which requests will be performed. Can be null, in which case
requests will be performed on behalf of the authenticated
Subject, if any.
**Returns:** an object that implements the

MBeanServerConnection

interface by forwarding its methods to the remote MBean server on behalf
of a given delegation subject.
**Throws:** IOException

- if a valid

MBeanServerConnection

cannot be created, for instance because the connection to the remote
MBean server has not yet been established (with the

connect

method), or it has been closed, or it has broken.

- close

```java
void close()
throws
IOException
```

Closes the client connection to its server. Any ongoing or new
request using the MBeanServerConnection returned by

getMBeanServerConnection()

will get an

IOException

.

If

close

has already been called successfully
on this object, calling it again has no effect. If

close

has never been called, or if it was called
but produced an exception, an attempt will be made to close the
connection. This attempt can succeed, in which case

close

will return normally, or it can generate an
exception.

Closing a connection is a potentially slow operation. For
example, if the server has crashed, the close operation might
have to wait for a network protocol timeout. Callers that do
not want to block in a close operation should do it in a
separate thread.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if the connection cannot be closed
cleanly. If this exception is thrown, it is not known whether
the server end of the connection has been cleanly closed.

- addConnectionNotificationListener

```java
void addConnectionNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
```

Adds a listener to be informed of changes in connection
status. The listener will receive notifications of type

JMXConnectionNotification

. An implementation can send other
types of notifications too.

Any number of listeners can be added with this method. The
same listener can be added more than once with the same or
different values for the filter and handback. There is no
special treatment of a duplicate entry. For example, if a
listener is registered twice with no filter, then its

handleNotification

method will be called twice for
each notification.

**Parameters:** listener

- a listener to receive connection status
notifications.
**Parameters:** filter

- a filter to select which notifications are to be
delivered to the listener, or null if all notifications are to
be delivered.
**Parameters:** handback

- an object to be given to the listener along
with each notification. Can be null.
**Throws:** NullPointerException

- if

listener

is
null.
**See Also:** removeConnectionNotificationListener(javax.management.NotificationListener)

,

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- removeConnectionNotificationListener

```java
void removeConnectionNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added. If
there is more than one matching listener, all are removed.

**Parameters:** listener

- a listener to receive connection status
notifications.
**Throws:** NullPointerException

- if

listener

is
null.
**Throws:** ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

.
**See Also:** removeConnectionNotificationListener(NotificationListener,
NotificationFilter, Object)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- removeConnectionNotificationListener

```java
void removeConnectionNotificationListener​(
NotificationListener
l,

NotificationFilter
f,

Object
handback)
throws
ListenerNotFoundException
```

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added with
the same three parameters. If there is more than one matching
listener, only one is removed.

**Parameters:** l

- a listener to receive connection status notifications.
**Parameters:** f

- a filter to select which notifications are to be
delivered to the listener. Can be null.
**Parameters:** handback

- an object to be given to the listener along
with each notification. Can be null.
**Throws:** ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

, or is not
registered with the given filter and handback.
**See Also:** removeConnectionNotificationListener(NotificationListener)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- getConnectionId

```java
String
getConnectionId()
throws
IOException
```

Gets this connection's ID from the connector server. For a
given connector server, every connection will have a unique id
which does not change during the lifetime of the
connection.

**Returns:** the unique ID of this connection. This is the same as
the ID that the connector server includes in its

JMXConnectionNotification

s. The

package description

describes the
conventions for connection IDs.
**Throws:** IOException

- if the connection ID cannot be obtained,
for instance because the connection is closed or broken.

---

#### Method Detail

connect

```java
void connect()
throws
IOException
```

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

**Throws:** IOException

- if the connection could not be made
because of a communication problem.
**Throws:** SecurityException

- if the connection could not be
made for security reasons.

---

#### connect

void connect()
throws

IOException

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

connect

```java
void connect​(
Map
<
String
,​?> env)
throws
IOException
```

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

close()

was called after

connect

, the new

connect

will throw an

IOException

.

Otherwise, either

connect

has never been called
on this object, or it has been called but produced an
exception. Then calling

connect

will attempt to
establish a connection to the connector server.

**Parameters:** env

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.
**Throws:** IOException

- if the connection could not be made
because of a communication problem.
**Throws:** SecurityException

- if the connection could not be
made for security reasons.

---

#### connect

void connect​(

Map

<

String

,​?> env)
throws

IOException

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

close()

was called after

connect

, the new

connect

will throw an

IOException

.

Otherwise, either

connect

has never been called
on this object, or it has been called but produced an
exception. Then calling

connect

will attempt to
establish a connection to the connector server.

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

close()

was called after

connect

, the new

connect

will throw an

IOException

.

Otherwise, either

connect

has never been called
on this object, or it has been called but produced an
exception. Then calling

connect

will attempt to
establish a connection to the connector server.

Otherwise, either

connect

has never been called
on this object, or it has been called but produced an
exception. Then calling

connect

will attempt to
establish a connection to the connector server.

getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection()
throws
IOException
```

Returns an

MBeanServerConnection

object
representing a remote MBean server. For a given

JMXConnector

, two successful calls to this method
will usually return the same

MBeanServerConnection

object, though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server. The value returned by the MBean server method is the
value returned to the client. If the MBean server method
produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

Calling this method is equivalent to calling

getMBeanServerConnection(null)

meaning that no delegation subject is specified and that all the
operations called on the

MBeanServerConnection

must
use the authenticated subject, if any.

**Returns:** an object that implements the

MBeanServerConnection

interface by forwarding its
methods to the remote MBean server.
**Throws:** IOException

- if a valid

MBeanServerConnection

cannot be created, for
instance because the connection to the remote MBean server has
not yet been established (with the

connect

method), or it has been closed, or it has broken.

---

#### getMBeanServerConnection

MBeanServerConnection

getMBeanServerConnection()
throws

IOException

Returns an

MBeanServerConnection

object
representing a remote MBean server. For a given

JMXConnector

, two successful calls to this method
will usually return the same

MBeanServerConnection

object, though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server. The value returned by the MBean server method is the
value returned to the client. If the MBean server method
produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

Calling this method is equivalent to calling

getMBeanServerConnection(null)

meaning that no delegation subject is specified and that all the
operations called on the

MBeanServerConnection

must
use the authenticated subject, if any.

Returns an

MBeanServerConnection

object
representing a remote MBean server. For a given

JMXConnector

, two successful calls to this method
will usually return the same

MBeanServerConnection

object, though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server. The value returned by the MBean server method is the
value returned to the client. If the MBean server method
produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

Calling this method is equivalent to calling

getMBeanServerConnection(null)

meaning that no delegation subject is specified and that all the
operations called on the

MBeanServerConnection

must
use the authenticated subject, if any.

getMBeanServerConnection

```java
MBeanServerConnection
getMBeanServerConnection​(
Subject
delegationSubject)
throws
IOException
```

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject. For a given

JMXConnector

and

Subject

, two successful calls to this method will
usually return the same

MBeanServerConnection

object,
though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server on behalf of the given delegation subject instead of the
authenticated subject. The value returned by the MBean server
method is the value returned to the client. If the MBean server
method produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

**Parameters:** delegationSubject

- the

Subject

on behalf of
which requests will be performed. Can be null, in which case
requests will be performed on behalf of the authenticated
Subject, if any.
**Returns:** an object that implements the

MBeanServerConnection

interface by forwarding its methods to the remote MBean server on behalf
of a given delegation subject.
**Throws:** IOException

- if a valid

MBeanServerConnection

cannot be created, for instance because the connection to the remote
MBean server has not yet been established (with the

connect

method), or it has been closed, or it has broken.

---

#### getMBeanServerConnection

MBeanServerConnection

getMBeanServerConnection​(

Subject

delegationSubject)
throws

IOException

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject. For a given

JMXConnector

and

Subject

, two successful calls to this method will
usually return the same

MBeanServerConnection

object,
though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server on behalf of the given delegation subject instead of the
authenticated subject. The value returned by the MBean server
method is the value returned to the client. If the MBean server
method produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

Returns an

MBeanServerConnection

object representing
a remote MBean server on which operations are performed on behalf of
the supplied delegation subject. For a given

JMXConnector

and

Subject

, two successful calls to this method will
usually return the same

MBeanServerConnection

object,
though this is not required.

For each method in the returned

MBeanServerConnection

, calling the method causes
the corresponding method to be called in the remote MBean
server on behalf of the given delegation subject instead of the
authenticated subject. The value returned by the MBean server
method is the value returned to the client. If the MBean server
method produces an

Exception

, the same

Exception

is seen by the client. If the MBean
server method, or the attempt to call it, produces an

Error

, the

Error

is wrapped in a

JMXServerErrorException

, which is seen by the
client.

close

```java
void close()
throws
IOException
```

Closes the client connection to its server. Any ongoing or new
request using the MBeanServerConnection returned by

getMBeanServerConnection()

will get an

IOException

.

If

close

has already been called successfully
on this object, calling it again has no effect. If

close

has never been called, or if it was called
but produced an exception, an attempt will be made to close the
connection. This attempt can succeed, in which case

close

will return normally, or it can generate an
exception.

Closing a connection is a potentially slow operation. For
example, if the server has crashed, the close operation might
have to wait for a network protocol timeout. Callers that do
not want to block in a close operation should do it in a
separate thread.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if the connection cannot be closed
cleanly. If this exception is thrown, it is not known whether
the server end of the connection has been cleanly closed.

---

#### close

void close()
throws

IOException

Closes the client connection to its server. Any ongoing or new
request using the MBeanServerConnection returned by

getMBeanServerConnection()

will get an

IOException

.

If

close

has already been called successfully
on this object, calling it again has no effect. If

close

has never been called, or if it was called
but produced an exception, an attempt will be made to close the
connection. This attempt can succeed, in which case

close

will return normally, or it can generate an
exception.

Closing a connection is a potentially slow operation. For
example, if the server has crashed, the close operation might
have to wait for a network protocol timeout. Callers that do
not want to block in a close operation should do it in a
separate thread.

Closes the client connection to its server. Any ongoing or new
request using the MBeanServerConnection returned by

getMBeanServerConnection()

will get an

IOException

.

If

close

has already been called successfully
on this object, calling it again has no effect. If

close

has never been called, or if it was called
but produced an exception, an attempt will be made to close the
connection. This attempt can succeed, in which case

close

will return normally, or it can generate an
exception.

Closing a connection is a potentially slow operation. For
example, if the server has crashed, the close operation might
have to wait for a network protocol timeout. Callers that do
not want to block in a close operation should do it in a
separate thread.

addConnectionNotificationListener

```java
void addConnectionNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
```

Adds a listener to be informed of changes in connection
status. The listener will receive notifications of type

JMXConnectionNotification

. An implementation can send other
types of notifications too.

Any number of listeners can be added with this method. The
same listener can be added more than once with the same or
different values for the filter and handback. There is no
special treatment of a duplicate entry. For example, if a
listener is registered twice with no filter, then its

handleNotification

method will be called twice for
each notification.

**Parameters:** listener

- a listener to receive connection status
notifications.
**Parameters:** filter

- a filter to select which notifications are to be
delivered to the listener, or null if all notifications are to
be delivered.
**Parameters:** handback

- an object to be given to the listener along
with each notification. Can be null.
**Throws:** NullPointerException

- if

listener

is
null.
**See Also:** removeConnectionNotificationListener(javax.management.NotificationListener)

,

NotificationBroadcaster.addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### addConnectionNotificationListener

void addConnectionNotificationListener​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to be informed of changes in connection
status. The listener will receive notifications of type

JMXConnectionNotification

. An implementation can send other
types of notifications too.

Any number of listeners can be added with this method. The
same listener can be added more than once with the same or
different values for the filter and handback. There is no
special treatment of a duplicate entry. For example, if a
listener is registered twice with no filter, then its

handleNotification

method will be called twice for
each notification.

Adds a listener to be informed of changes in connection
status. The listener will receive notifications of type

JMXConnectionNotification

. An implementation can send other
types of notifications too.

Any number of listeners can be added with this method. The
same listener can be added more than once with the same or
different values for the filter and handback. There is no
special treatment of a duplicate entry. For example, if a
listener is registered twice with no filter, then its

handleNotification

method will be called twice for
each notification.

removeConnectionNotificationListener

```java
void removeConnectionNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added. If
there is more than one matching listener, all are removed.

**Parameters:** listener

- a listener to receive connection status
notifications.
**Throws:** NullPointerException

- if

listener

is
null.
**Throws:** ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

.
**See Also:** removeConnectionNotificationListener(NotificationListener,
NotificationFilter, Object)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### removeConnectionNotificationListener

void removeConnectionNotificationListener​(

NotificationListener

listener)
throws

ListenerNotFoundException

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added. If
there is more than one matching listener, all are removed.

removeConnectionNotificationListener

```java
void removeConnectionNotificationListener​(
NotificationListener
l,

NotificationFilter
f,

Object
handback)
throws
ListenerNotFoundException
```

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added with
the same three parameters. If there is more than one matching
listener, only one is removed.

**Parameters:** l

- a listener to receive connection status notifications.
**Parameters:** f

- a filter to select which notifications are to be
delivered to the listener. Can be null.
**Parameters:** handback

- an object to be given to the listener along
with each notification. Can be null.
**Throws:** ListenerNotFoundException

- if the listener is not
registered with this

JMXConnector

, or is not
registered with the given filter and handback.
**See Also:** removeConnectionNotificationListener(NotificationListener)

,

addConnectionNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### removeConnectionNotificationListener

void removeConnectionNotificationListener​(

NotificationListener

l,

NotificationFilter

f,

Object

handback)
throws

ListenerNotFoundException

Removes a listener from the list to be informed of changes
in status. The listener must previously have been added with
the same three parameters. If there is more than one matching
listener, only one is removed.

getConnectionId

```java
String
getConnectionId()
throws
IOException
```

Gets this connection's ID from the connector server. For a
given connector server, every connection will have a unique id
which does not change during the lifetime of the
connection.

**Returns:** the unique ID of this connection. This is the same as
the ID that the connector server includes in its

JMXConnectionNotification

s. The

package description

describes the
conventions for connection IDs.
**Throws:** IOException

- if the connection ID cannot be obtained,
for instance because the connection is closed or broken.

---

#### getConnectionId

String

getConnectionId()
throws

IOException

Gets this connection's ID from the connector server. For a
given connector server, every connection will have a unique id
which does not change during the lifetime of the
connection.

---

