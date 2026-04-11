# Interface JMXAddressable

**Source:** `java.management\javax\management\remote\JMXAddressable.html`

### Class Description

```java
public interface
JMXAddressable
```

Implemented by objects that can have a

JMXServiceURL

address.
All

JMXConnectorServer

objects implement this interface.
Depending on the connector implementation, a

JMXConnector

object may implement this interface too.

JMXConnector

objects for the RMI Connector are instances of

RMIConnector

which
implements this interface.

An object implementing this interface might not have an address
at a given moment. This is indicated by a null return value from

getAddress()

.

**All Known Implementing Classes:** JMXConnectorServer

,

RMIConnector

,

RMIConnectorServer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### JMXServiceURL
getAddress()

The address of this object.

**Returns:**
- the address of this object, or null if it
does not have one.

---

### Additional Sections

#### Interface JMXAddressable

**All Known Implementing Classes:** JMXConnectorServer

,

RMIConnector

,

RMIConnectorServer

```java
public interface
JMXAddressable
```

Implemented by objects that can have a

JMXServiceURL

address.
All

JMXConnectorServer

objects implement this interface.
Depending on the connector implementation, a

JMXConnector

object may implement this interface too.

JMXConnector

objects for the RMI Connector are instances of

RMIConnector

which
implements this interface.

An object implementing this interface might not have an address
at a given moment. This is indicated by a null return value from

getAddress()

.

**Since:** 1.6

public interface

JMXAddressable

Implemented by objects that can have a

JMXServiceURL

address.
All

JMXConnectorServer

objects implement this interface.
Depending on the connector implementation, a

JMXConnector

object may implement this interface too.

JMXConnector

objects for the RMI Connector are instances of

RMIConnector

which
implements this interface.

An object implementing this interface might not have an address
at a given moment. This is indicated by a null return value from

getAddress()

.

Implemented by objects that can have a

JMXServiceURL

address.
All

JMXConnectorServer

objects implement this interface.
Depending on the connector implementation, a

JMXConnector

object may implement this interface too.

JMXConnector

objects for the RMI Connector are instances of

RMIConnector

which
implements this interface.

An object implementing this interface might not have an address
at a given moment. This is indicated by a null return value from

getAddress()

.

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

The address of this object.

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

The address of this object.

---

#### Method Summary

The address of this object.

============ METHOD DETAIL ==========

- Method Detail

- getAddress

```java
JMXServiceURL
getAddress()
```

The address of this object.

**Returns:** the address of this object, or null if it
does not have one.

Method Detail

- getAddress

```java
JMXServiceURL
getAddress()
```

The address of this object.

**Returns:** the address of this object, or null if it
does not have one.

---

#### Method Detail

getAddress

```java
JMXServiceURL
getAddress()
```

The address of this object.

**Returns:** the address of this object, or null if it
does not have one.

---

#### getAddress

JMXServiceURL

getAddress()

The address of this object.

---

