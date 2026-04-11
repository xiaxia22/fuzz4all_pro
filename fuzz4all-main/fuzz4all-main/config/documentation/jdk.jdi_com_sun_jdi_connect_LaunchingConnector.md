# Interface LaunchingConnector

**Source:** `jdk.jdi\com\sun\jdi\connect\LaunchingConnector.html`

### Class Description

```java
public interface
LaunchingConnector

extends
Connector
```

A connector which can launch a target VM before connecting to it.

**All Superinterfaces:** Connector

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### VirtualMachine
launch​(
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
,

VMStartException

Launches an application and connects to its VM. Properties
of the launch (possibly including options,
main class, and arguments) are specified in

arguments

.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

A target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Important note:

If a target VM is launched through this
funcctions, its output and error streams must be read as it
executes. These streams are available through the

Process

object returned by

VirtualMachine.process()

. If the streams are not periodically
read, the target VM will stop executing when the buffers for these
streams are filled.

**Parameters:**
- arguments

- the argument map to be used in launching the VM.

**Returns:**
- the

VirtualMachine

mirror of the target VM.

**Throws:**
- IOException

- when unable to launch.
Specific exceptions are dependent on the Connector implementation
in use.
- IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.
- VMStartException

- when the VM was successfully launched, but
terminated with an error before a connection could be established.

---

### Additional Sections

#### Interface LaunchingConnector

**All Superinterfaces:** Connector

```java
public interface
LaunchingConnector

extends
Connector
```

A connector which can launch a target VM before connecting to it.

**Since:** 1.3

public interface

LaunchingConnector

extends

Connector

A connector which can launch a target VM before connecting to it.

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

launch

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Launches an application and connects to its VM.

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

launch

​(

Map

<

String

,​? extends

Connector.Argument

> arguments)

Launches an application and connects to its VM.

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

Launches an application and connects to its VM.

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

- launch

```java
VirtualMachine
launch​(
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
,

VMStartException
```

Launches an application and connects to its VM. Properties
of the launch (possibly including options,
main class, and arguments) are specified in

arguments

.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

A target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Important note:

If a target VM is launched through this
funcctions, its output and error streams must be read as it
executes. These streams are available through the

Process

object returned by

VirtualMachine.process()

. If the streams are not periodically
read, the target VM will stop executing when the buffers for these
streams are filled.

**Parameters:** arguments

- the argument map to be used in launching the VM.
**Returns:** the

VirtualMachine

mirror of the target VM.
**Throws:** IOException

- when unable to launch.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.
**Throws:** VMStartException

- when the VM was successfully launched, but
terminated with an error before a connection could be established.

Method Detail

- launch

```java
VirtualMachine
launch​(
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
,

VMStartException
```

Launches an application and connects to its VM. Properties
of the launch (possibly including options,
main class, and arguments) are specified in

arguments

.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

A target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Important note:

If a target VM is launched through this
funcctions, its output and error streams must be read as it
executes. These streams are available through the

Process

object returned by

VirtualMachine.process()

. If the streams are not periodically
read, the target VM will stop executing when the buffers for these
streams are filled.

**Parameters:** arguments

- the argument map to be used in launching the VM.
**Returns:** the

VirtualMachine

mirror of the target VM.
**Throws:** IOException

- when unable to launch.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.
**Throws:** VMStartException

- when the VM was successfully launched, but
terminated with an error before a connection could be established.

---

#### Method Detail

launch

```java
VirtualMachine
launch​(
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
,

VMStartException
```

Launches an application and connects to its VM. Properties
of the launch (possibly including options,
main class, and arguments) are specified in

arguments

.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

A target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Important note:

If a target VM is launched through this
funcctions, its output and error streams must be read as it
executes. These streams are available through the

Process

object returned by

VirtualMachine.process()

. If the streams are not periodically
read, the target VM will stop executing when the buffers for these
streams are filled.

**Parameters:** arguments

- the argument map to be used in launching the VM.
**Returns:** the

VirtualMachine

mirror of the target VM.
**Throws:** IOException

- when unable to launch.
Specific exceptions are dependent on the Connector implementation
in use.
**Throws:** IllegalConnectorArgumentsException

- when one of the
connector arguments is invalid.
**Throws:** VMStartException

- when the VM was successfully launched, but
terminated with an error before a connection could be established.

---

#### launch

VirtualMachine

launch​(

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

,

VMStartException

Launches an application and connects to its VM. Properties
of the launch (possibly including options,
main class, and arguments) are specified in

arguments

.
The argument map associates argument name strings to instances
of

Connector.Argument

. The default argument map for a
connector can be obtained through

Connector.defaultArguments()

.
Argument map values can be changed, but map entries should not be
added or deleted.

A target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Important note:

If a target VM is launched through this
funcctions, its output and error streams must be read as it
executes. These streams are available through the

Process

object returned by

VirtualMachine.process()

. If the streams are not periodically
read, the target VM will stop executing when the buffers for these
streams are filled.

A target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Important note:

If a target VM is launched through this
funcctions, its output and error streams must be read as it
executes. These streams are available through the

Process

object returned by

VirtualMachine.process()

. If the streams are not periodically
read, the target VM will stop executing when the buffers for these
streams are filled.

Important note:

If a target VM is launched through this
funcctions, its output and error streams must be read as it
executes. These streams are available through the

Process

object returned by

VirtualMachine.process()

. If the streams are not periodically
read, the target VM will stop executing when the buffers for these
streams are filled.

---

