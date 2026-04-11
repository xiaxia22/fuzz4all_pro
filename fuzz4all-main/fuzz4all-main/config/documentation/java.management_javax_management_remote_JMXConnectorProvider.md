# Interface JMXConnectorProvider

**Source:** `java.management\javax\management\remote\JMXConnectorProvider.html`

### Class Description

```java
public interface
JMXConnectorProvider
```

A provider for creating JMX API connector clients using a given
protocol. Instances of this interface are created by

JMXConnectorFactory

as part of its

newJMXConnector

method.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException

Creates a new connector client that is ready to connect
to the connector server at the given address. Each successful
call to this method produces a different

JMXConnector

object.

**Parameters:**
- serviceURL

- the address of the connector server to connect to.
- environment

- a read-only Map containing named attributes
to determine how the connection is made. Keys in this map must
be Strings. The appropriate type of each associated value
depends on the attribute.

**Returns:**
- a

JMXConnector

representing the new
connector client. Each successful call to this method produces
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
connection cannot be made because of a communication problem.

---

### Additional Sections

#### Interface JMXConnectorProvider

```java
public interface
JMXConnectorProvider
```

A provider for creating JMX API connector clients using a given
protocol. Instances of this interface are created by

JMXConnectorFactory

as part of its

newJMXConnector

method.

**Since:** 1.5

public interface

JMXConnectorProvider

A provider for creating JMX API connector clients using a given
protocol. Instances of this interface are created by

JMXConnectorFactory

as part of its

newJMXConnector

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JMXConnector

newJMXConnector

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)

Creates a new connector client that is ready to connect
to the connector server at the given address.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JMXConnector

newJMXConnector

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)

Creates a new connector client that is ready to connect
to the connector server at the given address.

---

#### Method Summary

Creates a new connector client that is ready to connect
to the connector server at the given address.

============ METHOD DETAIL ==========

- Method Detail

- newJMXConnector

```java
JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a new connector client that is ready to connect
to the connector server at the given address. Each successful
call to this method produces a different

JMXConnector

object.

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a read-only Map containing named attributes
to determine how the connection is made. Keys in this map must
be Strings. The appropriate type of each associated value
depends on the attribute.
**Returns:** a

JMXConnector

representing the new
connector client. Each successful call to this method produces
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
connection cannot be made because of a communication problem.

Method Detail

- newJMXConnector

```java
JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a new connector client that is ready to connect
to the connector server at the given address. Each successful
call to this method produces a different

JMXConnector

object.

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a read-only Map containing named attributes
to determine how the connection is made. Keys in this map must
be Strings. The appropriate type of each associated value
depends on the attribute.
**Returns:** a

JMXConnector

representing the new
connector client. Each successful call to this method produces
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
connection cannot be made because of a communication problem.

---

#### Method Detail

newJMXConnector

```java
JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a new connector client that is ready to connect
to the connector server at the given address. Each successful
call to this method produces a different

JMXConnector

object.

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a read-only Map containing named attributes
to determine how the connection is made. Keys in this map must
be Strings. The appropriate type of each associated value
depends on the attribute.
**Returns:** a

JMXConnector

representing the new
connector client. Each successful call to this method produces
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
connection cannot be made because of a communication problem.

---

#### newJMXConnector

JMXConnector

newJMXConnector​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)
throws

IOException

Creates a new connector client that is ready to connect
to the connector server at the given address. Each successful
call to this method produces a different

JMXConnector

object.

---

