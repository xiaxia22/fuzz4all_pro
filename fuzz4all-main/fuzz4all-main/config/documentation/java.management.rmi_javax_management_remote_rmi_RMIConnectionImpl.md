# Class RMIConnectionImpl

**Source:** `java.management.rmi\javax\management\remote\rmi\RMIConnectionImpl.html`

### Class Description

```java
public class
RMIConnectionImpl

extends
Object

implements
RMIConnection
,
Unreferenced
```

Implementation of the

RMIConnection

interface. User
code will not usually reference this class.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Remote

,

Unreferenced

,

RMIConnection

---

### Field Details

*No entries found.*

### Constructor Details

#### public RMIConnectionImpl​(
RMIServerImpl
rmiServer,

String
connectionId,

ClassLoader
defaultClassLoader,

Subject
subject,

Map
<
String
,​?> env)

Constructs a new

RMIConnection

. This connection can be
used with the JRMP transport. This object does
not export itself: it is the responsibility of the caller to
export it appropriately (see

RMIJRMPServerImpl.makeClient(String,Subject)

).

**Parameters:**
- rmiServer

- The RMIServerImpl object for which this
connection is created. The behavior is unspecified if this
parameter is null.
- connectionId

- The ID for this connection. The behavior
is unspecified if this parameter is null.
- defaultClassLoader

- The default ClassLoader to be used
when deserializing marshalled objects. Can be null, to signify
the bootstrap class loader.
- subject

- the authenticated subject to be used for
authorization. Can be null, to signify that no subject has
been authenticated.
- env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, equivalent to an
empty map.

---

### Method Details

#### public
String
toString()

Returns a string representation of this object. In general,
the

toString

method returns a string that
"textually represents" this object. The result should be a
concise but informative representation that is easy for a
person to read.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this object.

---

### Additional Sections

#### Class RMIConnectionImpl

java.lang.Object

- javax.management.remote.rmi.RMIConnectionImpl

javax.management.remote.rmi.RMIConnectionImpl

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Remote

,

Unreferenced

,

RMIConnection

```java
public class
RMIConnectionImpl

extends
Object

implements
RMIConnection
,
Unreferenced
```

Implementation of the

RMIConnection

interface. User
code will not usually reference this class.

**Since:** 1.5

public class

RMIConnectionImpl

extends

Object

implements

RMIConnection

,

Unreferenced

Implementation of the

RMIConnection

interface. User
code will not usually reference this class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMIConnectionImpl

​(

RMIServerImpl

rmiServer,

String

connectionId,

ClassLoader

defaultClassLoader,

Subject

subject,

Map

<

String

,​?> env)

Constructs a new

RMIConnection

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns a string representation of this object.

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

wait

,

wait

,

wait

- Methods declared in interface javax.management.remote.rmi.

RMIConnection

addNotificationListener

,

addNotificationListeners

,

close

,

createMBean

,

createMBean

,

createMBean

,

createMBean

,

fetchNotifications

,

getAttribute

,

getAttributes

,

getConnectionId

,

getDefaultDomain

,

getDomains

,

getMBeanCount

,

getMBeanInfo

,

getObjectInstance

,

invoke

,

isInstanceOf

,

isRegistered

,

queryMBeans

,

queryNames

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListeners

,

setAttribute

,

setAttributes

,

unregisterMBean

- Methods declared in interface java.rmi.server.

Unreferenced

unreferenced

Constructor Summary

Constructors

Constructor

Description

RMIConnectionImpl

​(

RMIServerImpl

rmiServer,

String

connectionId,

ClassLoader

defaultClassLoader,

Subject

subject,

Map

<

String

,​?> env)

Constructs a new

RMIConnection

.

---

#### Constructor Summary

Constructs a new

RMIConnection

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns a string representation of this object.

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

wait

,

wait

,

wait

- Methods declared in interface javax.management.remote.rmi.

RMIConnection

addNotificationListener

,

addNotificationListeners

,

close

,

createMBean

,

createMBean

,

createMBean

,

createMBean

,

fetchNotifications

,

getAttribute

,

getAttributes

,

getConnectionId

,

getDefaultDomain

,

getDomains

,

getMBeanCount

,

getMBeanInfo

,

getObjectInstance

,

invoke

,

isInstanceOf

,

isRegistered

,

queryMBeans

,

queryNames

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListeners

,

setAttribute

,

setAttributes

,

unregisterMBean

- Methods declared in interface java.rmi.server.

Unreferenced

unreferenced

---

#### Method Summary

Returns a string representation of this object.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface javax.management.remote.rmi.

RMIConnection

addNotificationListener

,

addNotificationListeners

,

close

,

createMBean

,

createMBean

,

createMBean

,

createMBean

,

fetchNotifications

,

getAttribute

,

getAttributes

,

getConnectionId

,

getDefaultDomain

,

getDomains

,

getMBeanCount

,

getMBeanInfo

,

getObjectInstance

,

invoke

,

isInstanceOf

,

isRegistered

,

queryMBeans

,

queryNames

,

removeNotificationListener

,

removeNotificationListener

,

removeNotificationListeners

,

setAttribute

,

setAttributes

,

unregisterMBean

---

#### Methods declared in interface javax.management.remote.rmi. RMIConnection

Methods declared in interface java.rmi.server.

Unreferenced

unreferenced

---

#### Methods declared in interface java.rmi.server. Unreferenced

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RMIConnectionImpl

```java
public RMIConnectionImpl​(
RMIServerImpl
rmiServer,

String
connectionId,

ClassLoader
defaultClassLoader,

Subject
subject,

Map
<
String
,​?> env)
```

Constructs a new

RMIConnection

. This connection can be
used with the JRMP transport. This object does
not export itself: it is the responsibility of the caller to
export it appropriately (see

RMIJRMPServerImpl.makeClient(String,Subject)

).

**Parameters:** rmiServer

- The RMIServerImpl object for which this
connection is created. The behavior is unspecified if this
parameter is null.
**Parameters:** connectionId

- The ID for this connection. The behavior
is unspecified if this parameter is null.
**Parameters:** defaultClassLoader

- The default ClassLoader to be used
when deserializing marshalled objects. Can be null, to signify
the bootstrap class loader.
**Parameters:** subject

- the authenticated subject to be used for
authorization. Can be null, to signify that no subject has
been authenticated.
**Parameters:** env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, equivalent to an
empty map.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns a string representation of this object. In general,
the

toString

method returns a string that
"textually represents" this object. The result should be a
concise but informative representation that is easy for a
person to read.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object.

Constructor Detail

- RMIConnectionImpl

```java
public RMIConnectionImpl​(
RMIServerImpl
rmiServer,

String
connectionId,

ClassLoader
defaultClassLoader,

Subject
subject,

Map
<
String
,​?> env)
```

Constructs a new

RMIConnection

. This connection can be
used with the JRMP transport. This object does
not export itself: it is the responsibility of the caller to
export it appropriately (see

RMIJRMPServerImpl.makeClient(String,Subject)

).

**Parameters:** rmiServer

- The RMIServerImpl object for which this
connection is created. The behavior is unspecified if this
parameter is null.
**Parameters:** connectionId

- The ID for this connection. The behavior
is unspecified if this parameter is null.
**Parameters:** defaultClassLoader

- The default ClassLoader to be used
when deserializing marshalled objects. Can be null, to signify
the bootstrap class loader.
**Parameters:** subject

- the authenticated subject to be used for
authorization. Can be null, to signify that no subject has
been authenticated.
**Parameters:** env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, equivalent to an
empty map.

---

#### Constructor Detail

RMIConnectionImpl

```java
public RMIConnectionImpl​(
RMIServerImpl
rmiServer,

String
connectionId,

ClassLoader
defaultClassLoader,

Subject
subject,

Map
<
String
,​?> env)
```

Constructs a new

RMIConnection

. This connection can be
used with the JRMP transport. This object does
not export itself: it is the responsibility of the caller to
export it appropriately (see

RMIJRMPServerImpl.makeClient(String,Subject)

).

**Parameters:** rmiServer

- The RMIServerImpl object for which this
connection is created. The behavior is unspecified if this
parameter is null.
**Parameters:** connectionId

- The ID for this connection. The behavior
is unspecified if this parameter is null.
**Parameters:** defaultClassLoader

- The default ClassLoader to be used
when deserializing marshalled objects. Can be null, to signify
the bootstrap class loader.
**Parameters:** subject

- the authenticated subject to be used for
authorization. Can be null, to signify that no subject has
been authenticated.
**Parameters:** env

- the environment containing attributes for the new

RMIServerImpl

. Can be null, equivalent to an
empty map.

---

#### RMIConnectionImpl

public RMIConnectionImpl​(

RMIServerImpl

rmiServer,

String

connectionId,

ClassLoader

defaultClassLoader,

Subject

subject,

Map

<

String

,​?> env)

Constructs a new

RMIConnection

. This connection can be
used with the JRMP transport. This object does
not export itself: it is the responsibility of the caller to
export it appropriately (see

RMIJRMPServerImpl.makeClient(String,Subject)

).

Method Detail

- toString

```java
public
String
toString()
```

Returns a string representation of this object. In general,
the

toString

method returns a string that
"textually represents" this object. The result should be a
concise but informative representation that is easy for a
person to read.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object.

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns a string representation of this object. In general,
the

toString

method returns a string that
"textually represents" this object. The result should be a
concise but informative representation that is easy for a
person to read.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object.

---

#### toString

public

String

toString()

Returns a string representation of this object. In general,
the

toString

method returns a string that
"textually represents" this object. The result should be a
concise but informative representation that is easy for a
person to read.

---

