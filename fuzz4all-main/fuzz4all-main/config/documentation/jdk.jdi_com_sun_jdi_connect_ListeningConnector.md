# Interface ListeningConnector

**Source:** `jdk.jdi\com\sun\jdi\connect\ListeningConnector.html`

### Class Description

```java
public interface
ListeningConnector

extends
Connector
```

A connector which listens for a connection initiated by a target VM.

**All Superinterfaces:** Connector

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean supportsMultipleConnections()

Indicates whether this listening connector supports multiple
connections for a single argument map. If so, a call to

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

may allow
multiple target VM to become connected.

**Returns:**
- true

if multiple connections are supported;

false

otherwise.

---

#### String
startListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException

Listens for one or more connections initiated by target VMs.
The connector uses the given argument map
in determining the address at which to listen or else it generates
an appropriate listen address. In either case, an address string
is returned from this method which can be used in starting target VMs
to identify this connector. The format of the address string
is connector, transport, and, possibly, platform dependent.

The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

This method does not return a

VirtualMachine

, and, normally,
returns before any target VM initiates
a connection. The connected target is obtained through

accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

(using the same argument map as is passed to this
method).

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

**Returns:**
- the address at which the connector is listening
for a connection.

**Throws:**
- IOException

- when unable to start listening.
Specific exceptions are dependent on the Connector implementation
in use.
- IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### void stopListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException

Cancels listening for connections. The given argument map should match
the argument map given for a previous

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

invocation.

**Throws:**
- IOException

- when unable to stop listening.
Specific exceptions are dependent on the Connector implementation
in use.
- IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### VirtualMachine
accept​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException

Waits for a target VM to attach to this connector.

**Throws:**
- TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when accepting, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs whilst waiting for
the target VM to connect.
- IOException

- when unable to accept.
Specific exceptions are dependent on the Connector implementation
in use.
- IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

### Additional Sections

#### Interface ListeningConnector

**All Superinterfaces:** Connector

```java
public interface
ListeningConnector

extends
Connector
```

A connector which listens for a connection initiated by a target VM.

**Since:** 1.3

public interface

ListeningConnector

extends

Connector

A connector which listens for a connection initiated by a target VM.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.jdi.connect.

Connector

Connector.Argument

,

Connector.BooleanArgument

,

Connector.IntegerArgument

,

Connector.SelectedArgument

,

Connector.StringArgument

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

VirtualMachine

accept

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Waits for a target VM to attach to this connector.

String

startListening

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Listens for one or more connections initiated by target VMs.

void

stopListening

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Cancels listening for connections.

boolean

supportsMultipleConnections

()

Indicates whether this listening connector supports multiple
connections for a single argument map.

- Methods declared in interface com.sun.jdi.connect.

Connector

defaultArguments

,

description

,

name

,

transport

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.jdi.connect.

Connector

Connector.Argument

,

Connector.BooleanArgument

,

Connector.IntegerArgument

,

Connector.SelectedArgument

,

Connector.StringArgument

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.jdi.connect.

Connector

Connector.Argument

,

Connector.BooleanArgument

,

Connector.IntegerArgument

,

Connector.SelectedArgument

,

Connector.StringArgument

---

#### Nested classes/interfaces declared in interface com.sun.jdi.connect. Connector

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

VirtualMachine

accept

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Waits for a target VM to attach to this connector.

String

startListening

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Listens for one or more connections initiated by target VMs.

void

stopListening

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Cancels listening for connections.

boolean

supportsMultipleConnections

()

Indicates whether this listening connector supports multiple
connections for a single argument map.

- Methods declared in interface com.sun.jdi.connect.

Connector

defaultArguments

,

description

,

name

,

transport

---

#### Method Summary

Waits for a target VM to attach to this connector.

Listens for one or more connections initiated by target VMs.

Cancels listening for connections.

Indicates whether this listening connector supports multiple
connections for a single argument map.

Methods declared in interface com.sun.jdi.connect.

Connector

defaultArguments

,

description

,

name

,

transport

---

#### Methods declared in interface com.sun.jdi.connect. Connector

============ METHOD DETAIL ==========

- Method Detail

- supportsMultipleConnections

```java
boolean supportsMultipleConnections()
```

Indicates whether this listening connector supports multiple
connections for a single argument map. If so, a call to

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

may allow
multiple target VM to become connected.

**Returns:** true

if multiple connections are supported;

false

otherwise.

- startListening

```java
String
startListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Listens for one or more connections initiated by target VMs.
The connector uses the given argument map
in determining the address at which to listen or else it generates
an appropriate listen address. In either case, an address string
is returned from this method which can be used in starting target VMs
to identify this connector. The format of the address string
is connector, transport, and, possibly, platform dependent.

The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

This method does not return a

VirtualMachine

, and, normally,
returns before any target VM initiates
a connection. The connected target is obtained through

accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

(using the same argument map as is passed to this
method).

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

**Returns:** the address at which the connector is listening
for a connection.
**Throws:** IOException

- when unable to start listening.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

- stopListening

```java
void stopListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Cancels listening for connections. The given argument map should match
the argument map given for a previous

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

invocation.

**Throws:** IOException

- when unable to stop listening.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

- accept

```java
VirtualMachine
accept​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Waits for a target VM to attach to this connector.

**Throws:** TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when accepting, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs whilst waiting for
the target VM to connect.
**Throws:** IOException

- when unable to accept.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

Method Detail

- supportsMultipleConnections

```java
boolean supportsMultipleConnections()
```

Indicates whether this listening connector supports multiple
connections for a single argument map. If so, a call to

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

may allow
multiple target VM to become connected.

**Returns:** true

if multiple connections are supported;

false

otherwise.

- startListening

```java
String
startListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Listens for one or more connections initiated by target VMs.
The connector uses the given argument map
in determining the address at which to listen or else it generates
an appropriate listen address. In either case, an address string
is returned from this method which can be used in starting target VMs
to identify this connector. The format of the address string
is connector, transport, and, possibly, platform dependent.

The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

This method does not return a

VirtualMachine

, and, normally,
returns before any target VM initiates
a connection. The connected target is obtained through

accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

(using the same argument map as is passed to this
method).

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

**Returns:** the address at which the connector is listening
for a connection.
**Throws:** IOException

- when unable to start listening.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

- stopListening

```java
void stopListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Cancels listening for connections. The given argument map should match
the argument map given for a previous

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

invocation.

**Throws:** IOException

- when unable to stop listening.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

- accept

```java
VirtualMachine
accept​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Waits for a target VM to attach to this connector.

**Throws:** TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when accepting, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs whilst waiting for
the target VM to connect.
**Throws:** IOException

- when unable to accept.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### Method Detail

supportsMultipleConnections

```java
boolean supportsMultipleConnections()
```

Indicates whether this listening connector supports multiple
connections for a single argument map. If so, a call to

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

may allow
multiple target VM to become connected.

**Returns:** true

if multiple connections are supported;

false

otherwise.

---

#### supportsMultipleConnections

boolean supportsMultipleConnections()

Indicates whether this listening connector supports multiple
connections for a single argument map. If so, a call to

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

may allow
multiple target VM to become connected.

startListening

```java
String
startListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Listens for one or more connections initiated by target VMs.
The connector uses the given argument map
in determining the address at which to listen or else it generates
an appropriate listen address. In either case, an address string
is returned from this method which can be used in starting target VMs
to identify this connector. The format of the address string
is connector, transport, and, possibly, platform dependent.

The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

This method does not return a

VirtualMachine

, and, normally,
returns before any target VM initiates
a connection. The connected target is obtained through

accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

(using the same argument map as is passed to this
method).

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

**Returns:** the address at which the connector is listening
for a connection.
**Throws:** IOException

- when unable to start listening.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### startListening

String

startListening​(

Map

<

String

,​? extends

Connector.Argument

> arguments)
throws

IOException

,

IllegalConnectorArgumentsException

Listens for one or more connections initiated by target VMs.
The connector uses the given argument map
in determining the address at which to listen or else it generates
an appropriate listen address. In either case, an address string
is returned from this method which can be used in starting target VMs
to identify this connector. The format of the address string
is connector, transport, and, possibly, platform dependent.

The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

This method does not return a

VirtualMachine

, and, normally,
returns before any target VM initiates
a connection. The connected target is obtained through

accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

(using the same argument map as is passed to this
method).

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

This method does not return a

VirtualMachine

, and, normally,
returns before any target VM initiates
a connection. The connected target is obtained through

accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

(using the same argument map as is passed to this
method).

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

This method does not return a

VirtualMachine

, and, normally,
returns before any target VM initiates
a connection. The connected target is obtained through

accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

(using the same argument map as is passed to this
method).

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

If

arguments

contains addressing information and
only one connection will be accepted, the

accept

method
can be called immediately without calling this method.

stopListening

```java
void stopListening​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Cancels listening for connections. The given argument map should match
the argument map given for a previous

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

invocation.

**Throws:** IOException

- when unable to stop listening.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### stopListening

void stopListening​(

Map

<

String

,​? extends

Connector.Argument

> arguments)
throws

IOException

,

IllegalConnectorArgumentsException

Cancels listening for connections. The given argument map should match
the argument map given for a previous

startListening(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

invocation.

accept

```java
VirtualMachine
accept​(
Map
<
String
,​? extends
Connector.Argument
> arguments)
throws
IOException
,

IllegalConnectorArgumentsException
```

Waits for a target VM to attach to this connector.

**Throws:** TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when accepting, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs whilst waiting for
the target VM to connect.
**Throws:** IOException

- when unable to accept.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### accept

VirtualMachine

accept​(

Map

<

String

,​? extends

Connector.Argument

> arguments)
throws

IOException

,

IllegalConnectorArgumentsException

Waits for a target VM to attach to this connector.

---

