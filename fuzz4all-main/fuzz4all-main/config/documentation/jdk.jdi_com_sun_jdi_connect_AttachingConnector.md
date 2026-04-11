# Interface AttachingConnector

**Source:** `jdk.jdi\com\sun\jdi\connect\AttachingConnector.html`

### Class Description

```java
public interface
AttachingConnector

extends
Connector
```

A connector which attaches to a previously running target VM.

**All Superinterfaces:** Connector

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### VirtualMachine
attach​(
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

Attaches to a running application and returns a
mirror of its VM.

The connector uses the given argument map in
attaching the application. These arguments will include addressing
information that identifies the VM.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

**Parameters:**
- arguments

- the argument map to be used in launching the VM.

**Returns:**
- the

VirtualMachine

mirror of the target VM.

**Throws:**
- TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when attaching, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs when trying to attach
to the target VM.
- IOException

- when unable to attach.
Specific exceptions are dependent on the Connector implementation
in use.
- IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

### Additional Sections

#### Interface AttachingConnector

**All Superinterfaces:** Connector

```java
public interface
AttachingConnector

extends
Connector
```

A connector which attaches to a previously running target VM.

**Since:** 1.3

public interface

AttachingConnector

extends

Connector

A connector which attaches to a previously running target VM.

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

attach

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Attaches to a running application and returns a
mirror of its VM.

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

attach

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Attaches to a running application and returns a
mirror of its VM.

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

Attaches to a running application and returns a
mirror of its VM.

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

- attach

```java
VirtualMachine
attach​(
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

Attaches to a running application and returns a
mirror of its VM.

The connector uses the given argument map in
attaching the application. These arguments will include addressing
information that identifies the VM.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

**Parameters:** arguments

- the argument map to be used in launching the VM.
**Returns:** the

VirtualMachine

mirror of the target VM.
**Throws:** TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when attaching, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs when trying to attach
to the target VM.
**Throws:** IOException

- when unable to attach.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

Method Detail

- attach

```java
VirtualMachine
attach​(
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

Attaches to a running application and returns a
mirror of its VM.

The connector uses the given argument map in
attaching the application. These arguments will include addressing
information that identifies the VM.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

**Parameters:** arguments

- the argument map to be used in launching the VM.
**Returns:** the

VirtualMachine

mirror of the target VM.
**Throws:** TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when attaching, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs when trying to attach
to the target VM.
**Throws:** IOException

- when unable to attach.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### Method Detail

attach

```java
VirtualMachine
attach​(
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

Attaches to a running application and returns a
mirror of its VM.

The connector uses the given argument map in
attaching the application. These arguments will include addressing
information that identifies the VM.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

**Parameters:** arguments

- the argument map to be used in launching the VM.
**Returns:** the

VirtualMachine

mirror of the target VM.
**Throws:** TransportTimeoutException

- when the Connector encapsulates
a transport that supports a timeout when attaching, a

Connector.Argument

representing a timeout has been set
in the argument map, and a timeout occurs when trying to attach
to the target VM.
**Throws:** IOException

- when unable to attach.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.

---

#### attach

VirtualMachine

attach​(

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

Attaches to a running application and returns a
mirror of its VM.

The connector uses the given argument map in
attaching the application. These arguments will include addressing
information that identifies the VM.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

The connector uses the given argument map in
attaching the application. These arguments will include addressing
information that identifies the VM.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

---

