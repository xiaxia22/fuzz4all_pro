# Interface Mirror

**Source:** `jdk.jdi\com\sun\jdi\Mirror.html`

### Class Description

```java
public interface
Mirror
```

A proxy used by a debugger to examine or manipulate some entity
in another virtual machine. Mirror is the root of the
interface hierarchy for this package. Mirrors can be proxies for objects
in the target VM (

ObjectReference

), primitive values
(for example,

IntegerValue

), types (for example,

ReferenceType

), dynamic application state (for example,

StackFrame

), and even debugger-specific constructs (for example,

BreakpointRequest

).
The

VirtualMachine

itself is also considered a mirror,
representing the composite state of the target VM.

There is no guarantee that a particular entity in the target VM will map
to a single instance of Mirror. Implementors are free to decide
whether a single mirror will be used for some or all mirrors. Clients
of this interface should always use

equals

to compare
two mirrors for equality.

Any method on a

Mirror

that takes a

Mirror

as an
parameter directly or indirectly (e.g., as a element in a

List

) will
throw

VMMismatchException

if the mirrors are from different
virtual machines.

**All Known Subinterfaces:** AccessWatchpointEvent

,

AccessWatchpointRequest

,

ArrayReference

,

ArrayType

,

BooleanType

,

BooleanValue

,

BreakpointEvent

,

BreakpointRequest

,

ByteType

,

ByteValue

,

CharType

,

CharValue

,

ClassLoaderReference

,

ClassObjectReference

,

ClassPrepareEvent

,

ClassPrepareRequest

,

ClassType

,

ClassUnloadEvent

,

ClassUnloadRequest

,

DoubleType

,

DoubleValue

,

Event

,

EventQueue

,

EventRequest

,

EventRequestManager

,

EventSet

,

ExceptionEvent

,

ExceptionRequest

,

Field

,

FloatType

,

FloatValue

,

IntegerType

,

IntegerValue

,

InterfaceType

,

LocalVariable

,

LocatableEvent

,

Location

,

LongType

,

LongValue

,

Method

,

MethodEntryEvent

,

MethodEntryRequest

,

MethodExitEvent

,

MethodExitRequest

,

ModificationWatchpointEvent

,

ModificationWatchpointRequest

,

ModuleReference

,

MonitorContendedEnteredEvent

,

MonitorContendedEnteredRequest

,

MonitorContendedEnterEvent

,

MonitorContendedEnterRequest

,

MonitorInfo

,

MonitorWaitedEvent

,

MonitorWaitedRequest

,

MonitorWaitEvent

,

MonitorWaitRequest

,

ObjectReference

,

PathSearchingVirtualMachine

,

PrimitiveType

,

PrimitiveValue

,

ReferenceType

,

ShortType

,

ShortValue

,

StackFrame

,

StepEvent

,

StepRequest

,

StringReference

,

ThreadDeathEvent

,

ThreadDeathRequest

,

ThreadGroupReference

,

ThreadReference

,

ThreadStartEvent

,

ThreadStartRequest

,

Type

,

TypeComponent

,

Value

,

VirtualMachine

,

VMDeathEvent

,

VMDeathRequest

,

VMDisconnectEvent

,

VMStartEvent

,

VoidType

,

VoidValue

,

WatchpointEvent

,

WatchpointRequest

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### VirtualMachine
virtualMachine()

Gets the VirtualMachine to which this
Mirror belongs. A Mirror must be associated
with a VirtualMachine to have any meaning.

**Returns:**
- the

VirtualMachine

for which this mirror is a proxy.

---

#### String
toString()

Returns a String describing this mirror

**Overrides:**
- toString

in class

Object

**Returns:**
- a string describing this mirror.

---

### Additional Sections

#### Interface Mirror

**All Known Subinterfaces:** AccessWatchpointEvent

,

AccessWatchpointRequest

,

ArrayReference

,

ArrayType

,

BooleanType

,

BooleanValue

,

BreakpointEvent

,

BreakpointRequest

,

ByteType

,

ByteValue

,

CharType

,

CharValue

,

ClassLoaderReference

,

ClassObjectReference

,

ClassPrepareEvent

,

ClassPrepareRequest

,

ClassType

,

ClassUnloadEvent

,

ClassUnloadRequest

,

DoubleType

,

DoubleValue

,

Event

,

EventQueue

,

EventRequest

,

EventRequestManager

,

EventSet

,

ExceptionEvent

,

ExceptionRequest

,

Field

,

FloatType

,

FloatValue

,

IntegerType

,

IntegerValue

,

InterfaceType

,

LocalVariable

,

LocatableEvent

,

Location

,

LongType

,

LongValue

,

Method

,

MethodEntryEvent

,

MethodEntryRequest

,

MethodExitEvent

,

MethodExitRequest

,

ModificationWatchpointEvent

,

ModificationWatchpointRequest

,

ModuleReference

,

MonitorContendedEnteredEvent

,

MonitorContendedEnteredRequest

,

MonitorContendedEnterEvent

,

MonitorContendedEnterRequest

,

MonitorInfo

,

MonitorWaitedEvent

,

MonitorWaitedRequest

,

MonitorWaitEvent

,

MonitorWaitRequest

,

ObjectReference

,

PathSearchingVirtualMachine

,

PrimitiveType

,

PrimitiveValue

,

ReferenceType

,

ShortType

,

ShortValue

,

StackFrame

,

StepEvent

,

StepRequest

,

StringReference

,

ThreadDeathEvent

,

ThreadDeathRequest

,

ThreadGroupReference

,

ThreadReference

,

ThreadStartEvent

,

ThreadStartRequest

,

Type

,

TypeComponent

,

Value

,

VirtualMachine

,

VMDeathEvent

,

VMDeathRequest

,

VMDisconnectEvent

,

VMStartEvent

,

VoidType

,

VoidValue

,

WatchpointEvent

,

WatchpointRequest

```java
public interface
Mirror
```

A proxy used by a debugger to examine or manipulate some entity
in another virtual machine. Mirror is the root of the
interface hierarchy for this package. Mirrors can be proxies for objects
in the target VM (

ObjectReference

), primitive values
(for example,

IntegerValue

), types (for example,

ReferenceType

), dynamic application state (for example,

StackFrame

), and even debugger-specific constructs (for example,

BreakpointRequest

).
The

VirtualMachine

itself is also considered a mirror,
representing the composite state of the target VM.

There is no guarantee that a particular entity in the target VM will map
to a single instance of Mirror. Implementors are free to decide
whether a single mirror will be used for some or all mirrors. Clients
of this interface should always use

equals

to compare
two mirrors for equality.

Any method on a

Mirror

that takes a

Mirror

as an
parameter directly or indirectly (e.g., as a element in a

List

) will
throw

VMMismatchException

if the mirrors are from different
virtual machines.

**Since:** 1.3
**See Also:** VirtualMachine

public interface

Mirror

A proxy used by a debugger to examine or manipulate some entity
in another virtual machine. Mirror is the root of the
interface hierarchy for this package. Mirrors can be proxies for objects
in the target VM (

ObjectReference

), primitive values
(for example,

IntegerValue

), types (for example,

ReferenceType

), dynamic application state (for example,

StackFrame

), and even debugger-specific constructs (for example,

BreakpointRequest

).
The

VirtualMachine

itself is also considered a mirror,
representing the composite state of the target VM.

There is no guarantee that a particular entity in the target VM will map
to a single instance of Mirror. Implementors are free to decide
whether a single mirror will be used for some or all mirrors. Clients
of this interface should always use

equals

to compare
two mirrors for equality.

Any method on a

Mirror

that takes a

Mirror

as an
parameter directly or indirectly (e.g., as a element in a

List

) will
throw

VMMismatchException

if the mirrors are from different
virtual machines.

There is no guarantee that a particular entity in the target VM will map
to a single instance of Mirror. Implementors are free to decide
whether a single mirror will be used for some or all mirrors. Clients
of this interface should always use

equals

to compare
two mirrors for equality.

Any method on a

Mirror

that takes a

Mirror

as an
parameter directly or indirectly (e.g., as a element in a

List

) will
throw

VMMismatchException

if the mirrors are from different
virtual machines.

Any method on a

Mirror

that takes a

Mirror

as an
parameter directly or indirectly (e.g., as a element in a

List

) will
throw

VMMismatchException

if the mirrors are from different
virtual machines.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

toString

()

Returns a String describing this mirror

VirtualMachine

virtualMachine

()

Gets the VirtualMachine to which this
Mirror belongs.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

toString

()

Returns a String describing this mirror

VirtualMachine

virtualMachine

()

Gets the VirtualMachine to which this
Mirror belongs.

---

#### Method Summary

Returns a String describing this mirror

Gets the VirtualMachine to which this
Mirror belongs.

============ METHOD DETAIL ==========

- Method Detail

- virtualMachine

```java
VirtualMachine
virtualMachine()
```

Gets the VirtualMachine to which this
Mirror belongs. A Mirror must be associated
with a VirtualMachine to have any meaning.

**Returns:** the

VirtualMachine

for which this mirror is a proxy.

- toString

```java
String
toString()
```

Returns a String describing this mirror

**Overrides:** toString

in class

Object
**Returns:** a string describing this mirror.

Method Detail

- virtualMachine

```java
VirtualMachine
virtualMachine()
```

Gets the VirtualMachine to which this
Mirror belongs. A Mirror must be associated
with a VirtualMachine to have any meaning.

**Returns:** the

VirtualMachine

for which this mirror is a proxy.

- toString

```java
String
toString()
```

Returns a String describing this mirror

**Overrides:** toString

in class

Object
**Returns:** a string describing this mirror.

---

#### Method Detail

virtualMachine

```java
VirtualMachine
virtualMachine()
```

Gets the VirtualMachine to which this
Mirror belongs. A Mirror must be associated
with a VirtualMachine to have any meaning.

**Returns:** the

VirtualMachine

for which this mirror is a proxy.

---

#### virtualMachine

VirtualMachine

virtualMachine()

Gets the VirtualMachine to which this
Mirror belongs. A Mirror must be associated
with a VirtualMachine to have any meaning.

toString

```java
String
toString()
```

Returns a String describing this mirror

**Overrides:** toString

in class

Object
**Returns:** a string describing this mirror.

---

#### toString

String

toString()

Returns a String describing this mirror

---

