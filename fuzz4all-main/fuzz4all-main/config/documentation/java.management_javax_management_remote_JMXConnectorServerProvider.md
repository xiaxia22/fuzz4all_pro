# Interface JMXConnectorServerProvider

**Source:** `java.management\javax\management\remote\JMXConnectorServerProvider.html`

### Class Description

```java
public interface
JMXConnectorServerProvider
```

A provider for creating JMX API connector servers using a given
protocol. Instances of this interface are created by

JMXConnectorServerFactory

as part of its

newJMXConnectorServer

method.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### JMXConnectorServer
newJMXConnectorServer​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException

Creates a new connector server at the given address. Each
successful call to this method produces a different

JMXConnectorServer

object.

**Parameters:**
- serviceURL

- the address of the new connector server. The
actual address of the new connector server, as returned by its

getAddress

method, will
not necessarily be exactly the same. For example, it might
include a port number if the original address did not.
- environment

- a read-only Map containing named attributes
to control the new connector server's behavior. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute.
- mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.

**Returns:**
- a

JMXConnectorServer

representing the new
connector server. Each successful call to this method produces
a different object.

**Throws:**
- NullPointerException

- if

serviceURL

or

environment

is null.
- IOException

- It is recommended for a provider
implementation to throw

MalformedURLException

if the
protocol in the

serviceURL

is not recognized by this
provider,

JMXProviderException

if this is a provider
for the protocol in

serviceURL

but it cannot be used
for some reason or any other

IOException

if the
connector server cannot be created.

---

### Additional Sections

#### Interface JMXConnectorServerProvider

```java
public interface
JMXConnectorServerProvider
```

A provider for creating JMX API connector servers using a given
protocol. Instances of this interface are created by

JMXConnectorServerFactory

as part of its

newJMXConnectorServer

method.

**Since:** 1.5

public interface

JMXConnectorServerProvider

A provider for creating JMX API connector servers using a given
protocol. Instances of this interface are created by

JMXConnectorServerFactory

as part of its

newJMXConnectorServer

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JMXConnectorServer

newJMXConnectorServer

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment,

MBeanServer

mbeanServer)

Creates a new connector server at the given address.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JMXConnectorServer

newJMXConnectorServer

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment,

MBeanServer

mbeanServer)

Creates a new connector server at the given address.

---

#### Method Summary

Creates a new connector server at the given address.

============ METHOD DETAIL ==========

- Method Detail

- newJMXConnectorServer

```java
JMXConnectorServer
newJMXConnectorServer​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException
```

Creates a new connector server at the given address. Each
successful call to this method produces a different

JMXConnectorServer

object.

**Parameters:** serviceURL

- the address of the new connector server. The
actual address of the new connector server, as returned by its

getAddress

method, will
not necessarily be exactly the same. For example, it might
include a port number if the original address did not.
**Parameters:** environment

- a read-only Map containing named attributes
to control the new connector server's behavior. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute.
**Parameters:** mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.
**Returns:** a

JMXConnectorServer

representing the new
connector server. Each successful call to this method produces
a different object.
**Throws:** NullPointerException

- if

serviceURL

or

environment

is null.
**Throws:** IOException

- It is recommended for a provider
implementation to throw

MalformedURLException

if the
protocol in the

serviceURL

is not recognized by this
provider,

JMXProviderException

if this is a provider
for the protocol in

serviceURL

but it cannot be used
for some reason or any other

IOException

if the
connector server cannot be created.

Method Detail

- newJMXConnectorServer

```java
JMXConnectorServer
newJMXConnectorServer​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException
```

Creates a new connector server at the given address. Each
successful call to this method produces a different

JMXConnectorServer

object.

**Parameters:** serviceURL

- the address of the new connector server. The
actual address of the new connector server, as returned by its

getAddress

method, will
not necessarily be exactly the same. For example, it might
include a port number if the original address did not.
**Parameters:** environment

- a read-only Map containing named attributes
to control the new connector server's behavior. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute.
**Parameters:** mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.
**Returns:** a

JMXConnectorServer

representing the new
connector server. Each successful call to this method produces
a different object.
**Throws:** NullPointerException

- if

serviceURL

or

environment

is null.
**Throws:** IOException

- It is recommended for a provider
implementation to throw

MalformedURLException

if the
protocol in the

serviceURL

is not recognized by this
provider,

JMXProviderException

if this is a provider
for the protocol in

serviceURL

but it cannot be used
for some reason or any other

IOException

if the
connector server cannot be created.

---

#### Method Detail

newJMXConnectorServer

```java
JMXConnectorServer
newJMXConnectorServer​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment,

MBeanServer
mbeanServer)
throws
IOException
```

Creates a new connector server at the given address. Each
successful call to this method produces a different

JMXConnectorServer

object.

**Parameters:** serviceURL

- the address of the new connector server. The
actual address of the new connector server, as returned by its

getAddress

method, will
not necessarily be exactly the same. For example, it might
include a port number if the original address did not.
**Parameters:** environment

- a read-only Map containing named attributes
to control the new connector server's behavior. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute.
**Parameters:** mbeanServer

- the MBean server that this connector server
is attached to. Null if this connector server will be attached
to an MBean server by being registered in it.
**Returns:** a

JMXConnectorServer

representing the new
connector server. Each successful call to this method produces
a different object.
**Throws:** NullPointerException

- if

serviceURL

or

environment

is null.
**Throws:** IOException

- It is recommended for a provider
implementation to throw

MalformedURLException

if the
protocol in the

serviceURL

is not recognized by this
provider,

JMXProviderException

if this is a provider
for the protocol in

serviceURL

but it cannot be used
for some reason or any other

IOException

if the
connector server cannot be created.

---

#### newJMXConnectorServer

JMXConnectorServer

newJMXConnectorServer​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment,

MBeanServer

mbeanServer)
throws

IOException

Creates a new connector server at the given address. Each
successful call to this method produces a different

JMXConnectorServer

object.

---

