# Class RMIConnector

**Source:** `java.management.rmi\javax\management\remote\rmi\RMIConnector.html`

### Class Description

```java
public class
RMIConnector

extends
Object

implements
JMXConnector
,
Serializable
,
JMXAddressable
```

A connection to a remote RMI connector. Usually, such
connections are made using

JMXConnectorFactory

.
However, specialized applications can use this class directly, for
example with an

RMIServer

stub obtained without going
through JNDI.

**All Implemented Interfaces:** Closeable

,

Serializable

,

AutoCloseable

,

JMXAddressable

,

JMXConnector

---

### Field Details

*No entries found.*

### Constructor Details

#### public RMIConnector​(
JMXServiceURL
url,

Map
<
String
,​?> environment)

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

The address can refer directly to the connector server,
using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/stub/
encoded-stub
```

(Here, the square brackets

[]

are not part of the
address but indicate that the host and port are optional.)

The address can instead indicate where to find an RMI stub
through JNDI, using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/jndi/
jndi-name
```

An implementation may also recognize additional address
syntaxes, for example:

```java
service:jmx:iiop://
[host[:port]]
/stub/
encoded-stub
```

**Parameters:**
- url

- the address of the RMI connector server.
- environment

- additional attributes specifying how to make
the connection. For JNDI-based addresses, these attributes can
usefully include JNDI attributes recognized by

InitialContext

. This
parameter can be null, which is equivalent to an empty Map.

**Throws:**
- IllegalArgumentException

- if

url

is null.

---

#### public RMIConnector​(
RMIServer
rmiServer,

Map
<
String
,​?> environment)

Constructs an

RMIConnector

using the given RMI stub.

**Parameters:**
- rmiServer

- an RMI stub representing the RMI connector server.
- environment

- additional attributes specifying how to make
the connection. This parameter can be null, which is
equivalent to an empty Map.

**Throws:**
- IllegalArgumentException

- if

rmiServer

is null.

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

#### public
JMXServiceURL
getAddress()

The address of this connector.

**Specified by:**
- getAddress

in interface

JMXAddressable

**Returns:**
- the address of this connector, or null if it
does not have one.

**Since:**
- 1.6

---

#### public void connect()
throws
IOException

Description copied from interface:

JMXConnector

**Specified by:**
- connect

in interface

JMXConnector

**Throws:**
- IOException

- if the connection could not be made because of a
communication problem

---

#### public void connect​(
Map
<
String
,​?> environment)
throws
IOException

Description copied from interface:

JMXConnector

**Specified by:**
- connect

in interface

JMXConnector

**Parameters:**
- environment

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.

**Throws:**
- IOException

- if the connection could not be made because of a
communication problem

---

### Additional Sections

#### Class RMIConnector

java.lang.Object

- javax.management.remote.rmi.RMIConnector

javax.management.remote.rmi.RMIConnector

**All Implemented Interfaces:** Closeable

,

Serializable

,

AutoCloseable

,

JMXAddressable

,

JMXConnector

```java
public class
RMIConnector

extends
Object

implements
JMXConnector
,
Serializable
,
JMXAddressable
```

A connection to a remote RMI connector. Usually, such
connections are made using

JMXConnectorFactory

.
However, specialized applications can use this class directly, for
example with an

RMIServer

stub obtained without going
through JNDI.

**Since:** 1.5
**See Also:** Serialized Form

public class

RMIConnector

extends

Object

implements

JMXConnector

,

Serializable

,

JMXAddressable

A connection to a remote RMI connector. Usually, such
connections are made using

JMXConnectorFactory

.
However, specialized applications can use this class directly, for
example with an

RMIServer

stub obtained without going
through JNDI.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.management.remote.

JMXConnector

CREDENTIALS

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMIConnector

​(

JMXServiceURL

url,

Map

<

String

,​?> environment)

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

RMIConnector

​(

RMIServer

rmiServer,

Map

<

String

,​?> environment)

Constructs an

RMIConnector

using the given RMI stub.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

,​?> environment)

Establishes the connection to the connector server.

JMXServiceURL

getAddress

()

The address of this connector.

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

- Methods declared in interface javax.management.remote.

JMXConnector

addConnectionNotificationListener

,

close

,

getConnectionId

,

getMBeanServerConnection

,

getMBeanServerConnection

,

removeConnectionNotificationListener

,

removeConnectionNotificationListener

Field Summary

- Fields declared in interface javax.management.remote.

JMXConnector

CREDENTIALS

---

#### Field Summary

Fields declared in interface javax.management.remote.

JMXConnector

CREDENTIALS

---

#### Fields declared in interface javax.management.remote. JMXConnector

Constructor Summary

Constructors

Constructor

Description

RMIConnector

​(

JMXServiceURL

url,

Map

<

String

,​?> environment)

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

RMIConnector

​(

RMIServer

rmiServer,

Map

<

String

,​?> environment)

Constructs an

RMIConnector

using the given RMI stub.

---

#### Constructor Summary

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

Constructs an

RMIConnector

using the given RMI stub.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

,​?> environment)

Establishes the connection to the connector server.

JMXServiceURL

getAddress

()

The address of this connector.

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

- Methods declared in interface javax.management.remote.

JMXConnector

addConnectionNotificationListener

,

close

,

getConnectionId

,

getMBeanServerConnection

,

getMBeanServerConnection

,

removeConnectionNotificationListener

,

removeConnectionNotificationListener

---

#### Method Summary

Establishes the connection to the connector server.

The address of this connector.

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

Methods declared in interface javax.management.remote.

JMXConnector

addConnectionNotificationListener

,

close

,

getConnectionId

,

getMBeanServerConnection

,

getMBeanServerConnection

,

removeConnectionNotificationListener

,

removeConnectionNotificationListener

---

#### Methods declared in interface javax.management.remote. JMXConnector

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RMIConnector

```java
public RMIConnector​(
JMXServiceURL
url,

Map
<
String
,​?> environment)
```

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

The address can refer directly to the connector server,
using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/stub/
encoded-stub
```

(Here, the square brackets

[]

are not part of the
address but indicate that the host and port are optional.)

The address can instead indicate where to find an RMI stub
through JNDI, using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/jndi/
jndi-name
```

An implementation may also recognize additional address
syntaxes, for example:

```java
service:jmx:iiop://
[host[:port]]
/stub/
encoded-stub
```

**Parameters:** url

- the address of the RMI connector server.
**Parameters:** environment

- additional attributes specifying how to make
the connection. For JNDI-based addresses, these attributes can
usefully include JNDI attributes recognized by

InitialContext

. This
parameter can be null, which is equivalent to an empty Map.
**Throws:** IllegalArgumentException

- if

url

is null.

- RMIConnector

```java
public RMIConnector​(
RMIServer
rmiServer,

Map
<
String
,​?> environment)
```

Constructs an

RMIConnector

using the given RMI stub.

**Parameters:** rmiServer

- an RMI stub representing the RMI connector server.
**Parameters:** environment

- additional attributes specifying how to make
the connection. This parameter can be null, which is
equivalent to an empty Map.
**Throws:** IllegalArgumentException

- if

rmiServer

is null.

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

- getAddress

```java
public
JMXServiceURL
getAddress()
```

The address of this connector.

**Specified by:** getAddress

in interface

JMXAddressable
**Returns:** the address of this connector, or null if it
does not have one.
**Since:** 1.6

- connect

```java
public void connect()
throws
IOException
```

Description copied from interface:

JMXConnector

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

**Specified by:** connect

in interface

JMXConnector
**Throws:** IOException

- if the connection could not be made because of a
communication problem

- connect

```java
public void connect​(
Map
<
String
,​?> environment)
throws
IOException
```

Description copied from interface:

JMXConnector

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

JMXConnector.close()

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

**Specified by:** connect

in interface

JMXConnector
**Parameters:** environment

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.
**Throws:** IOException

- if the connection could not be made because of a
communication problem

Constructor Detail

- RMIConnector

```java
public RMIConnector​(
JMXServiceURL
url,

Map
<
String
,​?> environment)
```

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

The address can refer directly to the connector server,
using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/stub/
encoded-stub
```

(Here, the square brackets

[]

are not part of the
address but indicate that the host and port are optional.)

The address can instead indicate where to find an RMI stub
through JNDI, using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/jndi/
jndi-name
```

An implementation may also recognize additional address
syntaxes, for example:

```java
service:jmx:iiop://
[host[:port]]
/stub/
encoded-stub
```

**Parameters:** url

- the address of the RMI connector server.
**Parameters:** environment

- additional attributes specifying how to make
the connection. For JNDI-based addresses, these attributes can
usefully include JNDI attributes recognized by

InitialContext

. This
parameter can be null, which is equivalent to an empty Map.
**Throws:** IllegalArgumentException

- if

url

is null.

- RMIConnector

```java
public RMIConnector​(
RMIServer
rmiServer,

Map
<
String
,​?> environment)
```

Constructs an

RMIConnector

using the given RMI stub.

**Parameters:** rmiServer

- an RMI stub representing the RMI connector server.
**Parameters:** environment

- additional attributes specifying how to make
the connection. This parameter can be null, which is
equivalent to an empty Map.
**Throws:** IllegalArgumentException

- if

rmiServer

is null.

---

#### Constructor Detail

RMIConnector

```java
public RMIConnector​(
JMXServiceURL
url,

Map
<
String
,​?> environment)
```

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

The address can refer directly to the connector server,
using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/stub/
encoded-stub
```

(Here, the square brackets

[]

are not part of the
address but indicate that the host and port are optional.)

The address can instead indicate where to find an RMI stub
through JNDI, using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/jndi/
jndi-name
```

An implementation may also recognize additional address
syntaxes, for example:

```java
service:jmx:iiop://
[host[:port]]
/stub/
encoded-stub
```

**Parameters:** url

- the address of the RMI connector server.
**Parameters:** environment

- additional attributes specifying how to make
the connection. For JNDI-based addresses, these attributes can
usefully include JNDI attributes recognized by

InitialContext

. This
parameter can be null, which is equivalent to an empty Map.
**Throws:** IllegalArgumentException

- if

url

is null.

---

#### RMIConnector

public RMIConnector​(

JMXServiceURL

url,

Map

<

String

,​?> environment)

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

The address can refer directly to the connector server,
using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/stub/
encoded-stub
```

(Here, the square brackets

[]

are not part of the
address but indicate that the host and port are optional.)

The address can instead indicate where to find an RMI stub
through JNDI, using the following syntax:

```java
service:jmx:rmi://
[host[:port]]
/jndi/
jndi-name
```

An implementation may also recognize additional address
syntaxes, for example:

```java
service:jmx:iiop://
[host[:port]]
/stub/
encoded-stub
```

Constructs an

RMIConnector

that will connect
the RMI connector server with the given address.

The address can refer directly to the connector server,
using the following syntax:

service:jmx:rmi://

[host[:port]]

/stub/

encoded-stub

(Here, the square brackets

[]

are not part of the
address but indicate that the host and port are optional.)

The address can instead indicate where to find an RMI stub
through JNDI, using the following syntax:

service:jmx:rmi://

[host[:port]]

/jndi/

jndi-name

An implementation may also recognize additional address
syntaxes, for example:

service:jmx:iiop://

[host[:port]]

/stub/

encoded-stub

RMIConnector

```java
public RMIConnector​(
RMIServer
rmiServer,

Map
<
String
,​?> environment)
```

Constructs an

RMIConnector

using the given RMI stub.

**Parameters:** rmiServer

- an RMI stub representing the RMI connector server.
**Parameters:** environment

- additional attributes specifying how to make
the connection. This parameter can be null, which is
equivalent to an empty Map.
**Throws:** IllegalArgumentException

- if

rmiServer

is null.

---

#### RMIConnector

public RMIConnector​(

RMIServer

rmiServer,

Map

<

String

,​?> environment)

Constructs an

RMIConnector

using the given RMI stub.

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

- getAddress

```java
public
JMXServiceURL
getAddress()
```

The address of this connector.

**Specified by:** getAddress

in interface

JMXAddressable
**Returns:** the address of this connector, or null if it
does not have one.
**Since:** 1.6

- connect

```java
public void connect()
throws
IOException
```

Description copied from interface:

JMXConnector

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

**Specified by:** connect

in interface

JMXConnector
**Throws:** IOException

- if the connection could not be made because of a
communication problem

- connect

```java
public void connect​(
Map
<
String
,​?> environment)
throws
IOException
```

Description copied from interface:

JMXConnector

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

JMXConnector.close()

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

**Specified by:** connect

in interface

JMXConnector
**Parameters:** environment

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.
**Throws:** IOException

- if the connection could not be made because of a
communication problem

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

getAddress

```java
public
JMXServiceURL
getAddress()
```

The address of this connector.

**Specified by:** getAddress

in interface

JMXAddressable
**Returns:** the address of this connector, or null if it
does not have one.
**Since:** 1.6

---

#### getAddress

public

JMXServiceURL

getAddress()

The address of this connector.

connect

```java
public void connect()
throws
IOException
```

Description copied from interface:

JMXConnector

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

**Specified by:** connect

in interface

JMXConnector
**Throws:** IOException

- if the connection could not be made because of a
communication problem

---

#### connect

public void connect()
throws

IOException

Description copied from interface:

JMXConnector

Establishes the connection to the connector server. This
method is equivalent to

connect(null)

.

connect

```java
public void connect​(
Map
<
String
,​?> environment)
throws
IOException
```

Description copied from interface:

JMXConnector

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

JMXConnector.close()

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

**Specified by:** connect

in interface

JMXConnector
**Parameters:** environment

- the properties of the connection. Properties in
this map override properties in the map specified when the

JMXConnector

was created, if any. This parameter
can be null, which is equivalent to an empty map.
**Throws:** IOException

- if the connection could not be made because of a
communication problem

---

#### connect

public void connect​(

Map

<

String

,​?> environment)
throws

IOException

Description copied from interface:

JMXConnector

Establishes the connection to the connector server.

If

connect

has already been called successfully
on this object, calling it again has no effect. If, however,

JMXConnector.close()

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

JMXConnector.close()

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

---

