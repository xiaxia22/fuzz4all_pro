# Interface VirtualMachine

**Source:** `jdk.jdi\com\sun\jdi\VirtualMachine.html`

### Class Description

```java
public interface
VirtualMachine

extends
Mirror
```

A virtual machine targeted for debugging.
More precisely, a

mirror

representing the
composite state of the target VM.
All other mirrors are associated with an instance of this
interface. Access to all other mirrors is achieved
directly or indirectly through an instance of this
interface.
Access to global VM properties and control of VM execution
are supported directly by this interface.

Instances of this interface are created by instances of

Connector

. For example,
an

AttachingConnector

attaches to a target VM and returns its virtual machine mirror.
A Connector will typically create a VirtualMachine by invoking
the VirtualMachineManager's

VirtualMachineManager.createVirtualMachine(Connection)

createVirtualMachine(Connection) method.

Note that a target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

**All Superinterfaces:** Mirror

---

### Field Details

#### static final int TRACE_NONE

All tracing is disabled.

**See Also:**
- Constant Field Values

---

#### static final int TRACE_SENDS

Tracing enabled for JDWP packets sent to target VM.

**See Also:**
- Constant Field Values

---

#### static final int TRACE_RECEIVES

Tracing enabled for JDWP packets received from target VM.

**See Also:**
- Constant Field Values

---

#### static final int TRACE_EVENTS

Tracing enabled for internal event handling.

**See Also:**
- Constant Field Values

---

#### static final int TRACE_REFTYPES

Tracing enabled for internal managment of reference types.

**See Also:**
- Constant Field Values

---

#### static final int TRACE_OBJREFS

Tracing enabled for internal management of object references.

**See Also:**
- Constant Field Values

---

#### static final int TRACE_ALL

All tracing is enabled.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### default
List
<
ModuleReference
> allModules()

Returns all modules. For each module in the target
VM a

ModuleReference

will be placed in the returned list.

Not all target virtual machines support this operation.
Use

canGetModuleInfo()

to determine if the operation is supported.

**Returns:**
- a list of

ModuleReference

objects, each mirroring
a module in the target VM.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

.

---

#### List
<
ReferenceType
> classesByName​(
String
className)

Returns the loaded reference types that
match a given name. The name must be fully qualified
(for example, java.lang.String). The returned list
will contain a

ReferenceType

for each class
or interface found with the given name. The search
is confined to loaded classes only; no attempt is made
to load a class of the given name.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Parameters:**
- className

- the class/interface name to search for

**Returns:**
- a list of

ReferenceType

objects, each
mirroring a type in the target VM with the given name.

---

#### List
<
ReferenceType
> allClasses()

Returns all loaded types. For each loaded type in the target
VM a

ReferenceType

will be placed in the returned list.
The list will include ReferenceTypes which mirror classes,
interfaces, and array types.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:**
- a list of

ReferenceType

objects, each mirroring
a loaded type in the target VM.

---

#### void redefineClasses​(
Map
<? extends
ReferenceType
,​byte[]> classToBytes)

All classes given are redefined according to the
definitions supplied. A method in a redefined class
is called 'equivalent' (to the old version of the
method) if

- their bytecodes are the same except for indicies into
the constant pool, and

the referenced constants are equal.

Otherwise, the new method is called 'non-equivalent'.
If a redefined method has active stack frames, those active
frames continue to run the bytecodes of the previous version of the
method. If the new version of such a method is non-equivalent,
then a method from one of these active frames is called 'obsolete' and

Method.isObsolete()

will return true when called on one of these methods.
If resetting such a frame is desired, use

ThreadReference.popFrames(StackFrame)

to pop the old obsolete method execution from the stack.
New invocations of redefined methods will always invoke the new versions.

This function does not cause any initialization except
that which would occur under the customary JVM semantics.
In other words, redefining a class does not cause
its initializers to be run. The values of preexisting
static variables will remain as they were prior to the
call. However, completely uninitialized (new) static
variables will be assigned their default value.

If a redefined class has instances then all those
instances will have the fields defined by the redefined
class at the completion of the call. Preexisting fields
will retain their previous values. Any new fields will
have their default values; no instance initializers or
constructors are run.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

**Parameters:**
- classToBytes

- A map from

ReferenceType

to array of byte.
The bytes represent the new class definition and
are in Java Virtual Machine class file format.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- If

canRedefineClasses()

is false any call of this method will throw this exception.

If

canAddMethod()

is false
attempting to add a method will throw this exception.

If

canUnrestrictedlyRedefineClasses()

is false, attempting any of the following will throw
this exception

- changing the schema (the fields)

changing the hierarchy (superclasses, interfaces)

deleting a method

changing class modifiers

changing method modifiers

changing the

NestHost

or

NestMembers

class attributes
- NoClassDefFoundError

- if the bytes
don't correspond to the reference type (the names
don't match).
- VerifyError

- if a "verifier" detects
that a class, though well formed, contains an internal
inconsistency or security problem.
- ClassFormatError

- if the bytes
do not represent a valid class.
- ClassCircularityError

- if a
circularity has been detected while initializing a class.
- UnsupportedClassVersionError

- if the
major and minor version numbers in bytes
are not supported by the VM.
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

**See Also:**
- Method.isObsolete()

,

ThreadReference.popFrames(com.sun.jdi.StackFrame)

,

canRedefineClasses()

,

canAddMethod()

,

canUnrestrictedlyRedefineClasses()

**Since:**
- 1.4

---

#### List
<
ThreadReference
> allThreads()

Returns a list of the currently running threads. For each
running thread in the target VM, a

ThreadReference

that mirrors it is placed in the list.
The returned list contains threads created through
java.lang.Thread, all native threads attached to
the target VM through JNI, and system threads created
by the target VM. Thread objects that have
not yet been started
(see

Thread.start()

)
and thread objects that have
completed their execution are not included in the returned list.

**Returns:**
- a list of

ThreadReference

objects, one for each
running thread in the mirrored VM.

---

#### void suspend()

Suspends the execution of the application running in this
virtual machine. All threads currently running will be suspended.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

ThreadReference.resume()

)
the same number of times it has been suspended.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### void resume()

Continues the execution of the application running in this
virtual machine. All threads are resumed as documented in

ThreadReference.resume()

.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

**See Also:**
- suspend()

---

#### List
<
ThreadGroupReference
> topLevelThreadGroups()

Returns each thread group which does not have a parent. For each
top level thread group a

ThreadGroupReference

is placed in the
returned list.

This command may be used as the first step in building a tree
(or trees) of the existing thread groups.

**Returns:**
- a list of

ThreadGroupReference

objects, one for each
top level thread group.

---

#### EventQueue
eventQueue()

Returns the event queue for this virtual machine.
A virtual machine has only one

EventQueue

object, this
method will return the same instance each time it
is invoked.

**Returns:**
- the

EventQueue

for this virtual machine.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### EventRequestManager
eventRequestManager()

Returns the event request manager for this virtual machine.
The

EventRequestManager

controls user settable events
such as breakpoints.
A virtual machine has only one

EventRequestManager

object,
this method will return the same instance each time it
is invoked.

**Returns:**
- the

EventRequestManager

for this virtual machine.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### BooleanValue
mirrorOf​(boolean value)

Creates a

BooleanValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- a boolean for which to create the value

**Returns:**
- the

BooleanValue

for the given boolean.

---

#### ByteValue
mirrorOf​(byte value)

Creates a

ByteValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- a byte for which to create the value

**Returns:**
- the

ByteValue

for the given byte.

---

#### CharValue
mirrorOf​(char value)

Creates a

CharValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- a char for which to create the value

**Returns:**
- the

CharValue

for the given char.

---

#### ShortValue
mirrorOf​(short value)

Creates a

ShortValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- a short for which to create the value

**Returns:**
- the

ShortValue

for the given short.

---

#### IntegerValue
mirrorOf​(int value)

Creates an

IntegerValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- an int for which to create the value

**Returns:**
- the

IntegerValue

for the given int.

---

#### LongValue
mirrorOf​(long value)

Creates a

LongValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- a long for which to create the value

**Returns:**
- the

LongValue

for the given long.

---

#### FloatValue
mirrorOf​(float value)

Creates a

FloatValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- a float for which to create the value

**Returns:**
- the

FloatValue

for the given float.

---

#### DoubleValue
mirrorOf​(double value)

Creates a

DoubleValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:**
- value

- a double for which to create the value

**Returns:**
- the

DoubleValue

for the given double.

---

#### StringReference
mirrorOf​(
String
value)

Creates a string in this virtual machine.
The created string can be used for setting and comparing against
a string value retrieved from a variable or field in this
virtual machine.

**Parameters:**
- value

- the string to be created

**Returns:**
- a

StringReference

that mirrors the newly created
string in the target VM.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

---

#### VoidValue
mirrorOfVoid()

Creates a

VoidValue

. This value
can be passed to

ThreadReference.forceEarlyReturn(com.sun.jdi.Value)

when a void method is to be exited.

**Returns:**
- the

VoidValue

.

---

#### Process
process()

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

**Returns:**
- the

Process

object for this virtual
machine, or null if it was not launched by a

LaunchingConnector

.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

---

#### void dispose()

Invalidates this virtual machine mirror.
The communication channel to the target VM is closed, and
the target VM prepares to accept another subsequent connection
from this debugger or another debugger, including the
following tasks:

- All event requests are cancelled.

All threads suspended by

suspend()

or by

ThreadReference.suspend()

are resumed as many
times as necessary for them to run.

Garbage collection is re-enabled in all cases where it was
disabled through

ObjectReference.disableCollection()

.

Any current method invocations executing in the target VM
are continued after the disconnection. Upon completion of any such
method invocation, the invoking thread continues from the
location where it was originally stopped.

Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

---

#### void exit​(int exitCode)

Causes the mirrored VM to terminate with the given error code.
All resources associated with this VirtualMachine are freed.
If the mirrored VM is remote, the communication channel
to it will be closed. Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

Threads running in the mirrored VM are abruptly terminated.
A thread death exception is not thrown and
finally blocks are not run.

**Parameters:**
- exitCode

- the exit code for the target VM. On some platforms,
the exit code might be truncated, for example, to the lower order 8 bits.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### boolean canWatchFieldModification()

Determines if the target VM supports watchpoints
for field modification.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canWatchFieldAccess()

Determines if the target VM supports watchpoints
for field access.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canGetBytecodes()

Determines if the target VM supports the retrieval
of a method's bytecodes.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canGetSyntheticAttribute()

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canGetOwnedMonitorInfo()

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canGetCurrentContendedMonitor()

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canGetMonitorInfo()

Determines if the target VM supports the retrieval
of the monitor information for an object.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canUseInstanceFilters()

Determines if the target VM supports filtering
events by specific instance object. For example,
see

BreakpointRequest.addInstanceFilter(com.sun.jdi.ObjectReference)

.

**Returns:**
- true

if the feature is supported,

false

otherwise.

---

#### boolean canRedefineClasses()

Determines if the target VM supports any level
of class redefinition.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

**Since:**
- 1.4

---

#### boolean canAddMethod()

Determines if the target VM supports the addition
of methods when performing class redefinition.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

**Since:**
- 1.4

---

#### boolean canUnrestrictedlyRedefineClasses()

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

**Since:**
- 1.4

---

#### boolean canPopFrames()

Determines if the target VM supports popping
frames of a threads stack.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- ThreadReference.popFrames(com.sun.jdi.StackFrame)

**Since:**
- 1.4

---

#### boolean canGetSourceDebugExtension()

Determines if the target VM supports getting
the source debug extension.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- ReferenceType.sourceDebugExtension()

**Since:**
- 1.4

---

#### boolean canRequestVMDeathEvent()

Determines if the target VM supports the creation of

VMDeathRequest

s.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- EventRequestManager.createVMDeathRequest()

**Since:**
- 1.4

---

#### boolean canGetMethodReturnValues()

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- EventRequestManager.createMethodExitRequest()

**Since:**
- 1.6

---

#### boolean canGetInstanceInfo()

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- instanceCounts(java.util.List<? extends com.sun.jdi.ReferenceType>)

,

ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

**Since:**
- 1.6

---

#### boolean canUseSourceNameFilters()

Determines if the target VM supports the filtering of
class prepare events by source name.

see

ClassPrepareRequest.addSourceNameFilter(java.lang.String)

.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**Since:**
- 1.6

---

#### boolean canForceEarlyReturn()

Determines if the target VM supports the forcing of a method to
return early.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- ThreadReference.forceEarlyReturn(Value)

**Since:**
- 1.6

---

#### boolean canBeModified()

Determines if the target VM is a read-only VM. If a method which
would modify the state of the VM is called on a read-only VM,
then

VMCannotBeModifiedException

is thrown.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**Since:**
- 1.5

---

#### boolean canRequestMonitorEvents()

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

MonitorContendedEnteredRequest

s.

MonitorWaitRequest

s.

MonitorWaitedRequest

s.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- EventRequestManager.createMonitorContendedEnterRequest()

,

EventRequestManager.createMonitorContendedEnteredRequest()

,

EventRequestManager.createMonitorWaitRequest()

,

EventRequestManager.createMonitorWaitedRequest()

**Since:**
- 1.6

---

#### boolean canGetMonitorFrameInfo()

Determines if the target VM supports getting which
frame has acquired a monitor.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- ThreadReference.ownedMonitorsAndFrames()

**Since:**
- 1.6

---

#### boolean canGetClassFileVersion()

Determines if the target VM supports reading class file
major and minor versions.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- ReferenceType.majorVersion()

,

ReferenceType.minorVersion()

**Since:**
- 1.6

---

#### boolean canGetConstantPool()

Determines if the target VM supports getting constant pool
information of a class.

**Returns:**
- true

if the feature is supported,

false

otherwise.

**See Also:**
- ReferenceType.constantPoolCount()

,

ReferenceType.constantPool()

**Since:**
- 1.6

---

#### default boolean canGetModuleInfo()

Determines if the target VM supports getting information about modules.

**Returns:**
- true

if the feature is supported,

false

otherwise

**See Also:**
- allModules()

,

ReferenceType.module()

,

ModuleReference

**Since:**
- 9

**Implementation Requirements:**
- The default implementation returns

false

.

---

#### void setDefaultStratum​(
String
stratum)

Set this VM's default stratum (see

Location

for a
discussion of strata). Overrides the per-class default set
in the class file.

Affects location queries (such as,

Location.sourceName()

)
and the line boundaries used in
single stepping.

**Parameters:**
- stratum

- the stratum to set as VM default,
or null to use per-class defaults.

**Throws:**
- UnsupportedOperationException

- if the
target virtual machine does not support this operation.

**Since:**
- 1.4

---

#### String
getDefaultStratum()

Return this VM's default stratum.

**Returns:**
- null

(meaning that the per-class
default -

ReferenceType.defaultStratum()

-
should be used) unless the default stratum has been
set with

setDefaultStratum(String)

.

**See Also:**
- setDefaultStratum(String)

,

ReferenceType.defaultStratum()

**Since:**
- 1.4

---

#### long[] instanceCounts​(
List
<? extends
ReferenceType
> refTypes)

Returns the number of instances of each ReferenceType in the 'refTypes'
list.
Only instances that are reachable for the purposes of garbage collection
are counted.

Not all target virtual machines support this operation.
Use

canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:**
- refTypes

- the list of

ReferenceType

objects for which counts
are to be obtained.

**Returns:**
- an array of

long

containing one element for each
element in the 'refTypes' list. Element i of the array contains
the number of instances in the target VM of the ReferenceType at
position i in the 'refTypes' list.
If the 'refTypes' list is empty, a zero-length array is returned.
If a ReferenceType in refTypes has been garbage collected, zero
is returned for its instance count.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
- NullPointerException

- if the 'refTypes' list is null.

**See Also:**
- ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

**Since:**
- 1.6

---

#### String
description()

Returns text information on the target VM and the
debugger support that mirrors it. No specific format
for this information is guaranteed.
Typically, this string contains version information for the
target VM and debugger interfaces.
More precise information
on VM and JDI versions is available through

version()

,

VirtualMachineManager.majorInterfaceVersion()

,
and

VirtualMachineManager.minorInterfaceVersion()

**Returns:**
- the description.

---

#### String
version()

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.
For obtaining the JDI interface version, use

VirtualMachineManager.majorInterfaceVersion()

and

VirtualMachineManager.minorInterfaceVersion()

**Returns:**
- the target VM version.

---

#### String
name()

Returns the name of the target VM as reported by the
property

java.vm.name

.

**Returns:**
- the target VM name.

---

#### void setDebugTraceMode​(int traceFlags)

Traces the activities performed by the com.sun.jdi implementation.
All trace information is output to System.err. The given trace
flags are used to limit the output to only the information
desired. The given flags are in effect and the corresponding
trace will continue until the next call to
this method.

Output is implementation dependent and trace mode may be ignored.

**Parameters:**
- traceFlags

- identifies which kinds of tracing to enable.

---

### Additional Sections

#### Interface VirtualMachine

**All Superinterfaces:** Mirror

**All Known Subinterfaces:** PathSearchingVirtualMachine

```java
public interface
VirtualMachine

extends
Mirror
```

A virtual machine targeted for debugging.
More precisely, a

mirror

representing the
composite state of the target VM.
All other mirrors are associated with an instance of this
interface. Access to all other mirrors is achieved
directly or indirectly through an instance of this
interface.
Access to global VM properties and control of VM execution
are supported directly by this interface.

Instances of this interface are created by instances of

Connector

. For example,
an

AttachingConnector

attaches to a target VM and returns its virtual machine mirror.
A Connector will typically create a VirtualMachine by invoking
the VirtualMachineManager's

VirtualMachineManager.createVirtualMachine(Connection)

createVirtualMachine(Connection) method.

Note that a target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

**Since:** 1.3

public interface

VirtualMachine

extends

Mirror

A virtual machine targeted for debugging.
More precisely, a

mirror

representing the
composite state of the target VM.
All other mirrors are associated with an instance of this
interface. Access to all other mirrors is achieved
directly or indirectly through an instance of this
interface.
Access to global VM properties and control of VM execution
are supported directly by this interface.

Instances of this interface are created by instances of

Connector

. For example,
an

AttachingConnector

attaches to a target VM and returns its virtual machine mirror.
A Connector will typically create a VirtualMachine by invoking
the VirtualMachineManager's

VirtualMachineManager.createVirtualMachine(Connection)

createVirtualMachine(Connection) method.

Note that a target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Instances of this interface are created by instances of

Connector

. For example,
an

AttachingConnector

attaches to a target VM and returns its virtual machine mirror.
A Connector will typically create a VirtualMachine by invoking
the VirtualMachineManager's

VirtualMachineManager.createVirtualMachine(Connection)

createVirtualMachine(Connection) method.

Note that a target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Note that a target VM launched by a launching connector is not
guaranteed to be stable until after the

VMStartEvent

has been
received.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

VirtualMachine

which
takes

VirtualMachine

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

TRACE_ALL

All tracing is enabled.

static int

TRACE_EVENTS

Tracing enabled for internal event handling.

static int

TRACE_NONE

All tracing is disabled.

static int

TRACE_OBJREFS

Tracing enabled for internal management of object references.

static int

TRACE_RECEIVES

Tracing enabled for JDWP packets received from target VM.

static int

TRACE_REFTYPES

Tracing enabled for internal managment of reference types.

static int

TRACE_SENDS

Tracing enabled for JDWP packets sent to target VM.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

List

<

ReferenceType

>

allClasses

()

Returns all loaded types.

default

List

<

ModuleReference

>

allModules

()

Returns all modules.

List

<

ThreadReference

>

allThreads

()

Returns a list of the currently running threads.

boolean

canAddMethod

()

Determines if the target VM supports the addition
of methods when performing class redefinition.

boolean

canBeModified

()

Determines if the target VM is a read-only VM.

boolean

canForceEarlyReturn

()

Determines if the target VM supports the forcing of a method to
return early.

boolean

canGetBytecodes

()

Determines if the target VM supports the retrieval
of a method's bytecodes.

boolean

canGetClassFileVersion

()

Determines if the target VM supports reading class file
major and minor versions.

boolean

canGetConstantPool

()

Determines if the target VM supports getting constant pool
information of a class.

boolean

canGetCurrentContendedMonitor

()

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

boolean

canGetInstanceInfo

()

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

boolean

canGetMethodReturnValues

()

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

default boolean

canGetModuleInfo

()

Determines if the target VM supports getting information about modules.

boolean

canGetMonitorFrameInfo

()

Determines if the target VM supports getting which
frame has acquired a monitor.

boolean

canGetMonitorInfo

()

Determines if the target VM supports the retrieval
of the monitor information for an object.

boolean

canGetOwnedMonitorInfo

()

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

boolean

canGetSourceDebugExtension

()

Determines if the target VM supports getting
the source debug extension.

boolean

canGetSyntheticAttribute

()

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

boolean

canPopFrames

()

Determines if the target VM supports popping
frames of a threads stack.

boolean

canRedefineClasses

()

Determines if the target VM supports any level
of class redefinition.

boolean

canRequestMonitorEvents

()

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

boolean

canRequestVMDeathEvent

()

Determines if the target VM supports the creation of

VMDeathRequest

s.

boolean

canUnrestrictedlyRedefineClasses

()

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

boolean

canUseInstanceFilters

()

Determines if the target VM supports filtering
events by specific instance object.

boolean

canUseSourceNameFilters

()

Determines if the target VM supports the filtering of
class prepare events by source name.

boolean

canWatchFieldAccess

()

Determines if the target VM supports watchpoints
for field access.

boolean

canWatchFieldModification

()

Determines if the target VM supports watchpoints
for field modification.

List

<

ReferenceType

>

classesByName

​(

String

className)

Returns the loaded reference types that
match a given name.

String

description

()

Returns text information on the target VM and the
debugger support that mirrors it.

void

dispose

()

Invalidates this virtual machine mirror.

EventQueue

eventQueue

()

Returns the event queue for this virtual machine.

EventRequestManager

eventRequestManager

()

Returns the event request manager for this virtual machine.

void

exit

​(int exitCode)

Causes the mirrored VM to terminate with the given error code.

String

getDefaultStratum

()

Return this VM's default stratum.

long[]

instanceCounts

​(

List

<? extends

ReferenceType

> refTypes)

Returns the number of instances of each ReferenceType in the 'refTypes'
list.

BooleanValue

mirrorOf

​(boolean value)

Creates a

BooleanValue

for the given value.

ByteValue

mirrorOf

​(byte value)

Creates a

ByteValue

for the given value.

CharValue

mirrorOf

​(char value)

Creates a

CharValue

for the given value.

DoubleValue

mirrorOf

​(double value)

Creates a

DoubleValue

for the given value.

FloatValue

mirrorOf

​(float value)

Creates a

FloatValue

for the given value.

IntegerValue

mirrorOf

​(int value)

Creates an

IntegerValue

for the given value.

LongValue

mirrorOf

​(long value)

Creates a

LongValue

for the given value.

ShortValue

mirrorOf

​(short value)

Creates a

ShortValue

for the given value.

StringReference

mirrorOf

​(

String

value)

Creates a string in this virtual machine.

VoidValue

mirrorOfVoid

()

Creates a

VoidValue

.

String

name

()

Returns the name of the target VM as reported by the
property

java.vm.name

.

Process

process

()

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

void

redefineClasses

​(

Map

<? extends

ReferenceType

,​byte[]> classToBytes)

All classes given are redefined according to the
definitions supplied.

void

resume

()

Continues the execution of the application running in this
virtual machine.

void

setDebugTraceMode

​(int traceFlags)

Traces the activities performed by the com.sun.jdi implementation.

void

setDefaultStratum

​(

String

stratum)

Set this VM's default stratum (see

Location

for a
discussion of strata).

void

suspend

()

Suspends the execution of the application running in this
virtual machine.

List

<

ThreadGroupReference

>

topLevelThreadGroups

()

Returns each thread group which does not have a parent.

String

version

()

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Field Summary

Fields

Modifier and Type

Field

Description

static int

TRACE_ALL

All tracing is enabled.

static int

TRACE_EVENTS

Tracing enabled for internal event handling.

static int

TRACE_NONE

All tracing is disabled.

static int

TRACE_OBJREFS

Tracing enabled for internal management of object references.

static int

TRACE_RECEIVES

Tracing enabled for JDWP packets received from target VM.

static int

TRACE_REFTYPES

Tracing enabled for internal managment of reference types.

static int

TRACE_SENDS

Tracing enabled for JDWP packets sent to target VM.

---

#### Field Summary

All tracing is enabled.

Tracing enabled for internal event handling.

All tracing is disabled.

Tracing enabled for internal management of object references.

Tracing enabled for JDWP packets received from target VM.

Tracing enabled for internal managment of reference types.

Tracing enabled for JDWP packets sent to target VM.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

List

<

ReferenceType

>

allClasses

()

Returns all loaded types.

default

List

<

ModuleReference

>

allModules

()

Returns all modules.

List

<

ThreadReference

>

allThreads

()

Returns a list of the currently running threads.

boolean

canAddMethod

()

Determines if the target VM supports the addition
of methods when performing class redefinition.

boolean

canBeModified

()

Determines if the target VM is a read-only VM.

boolean

canForceEarlyReturn

()

Determines if the target VM supports the forcing of a method to
return early.

boolean

canGetBytecodes

()

Determines if the target VM supports the retrieval
of a method's bytecodes.

boolean

canGetClassFileVersion

()

Determines if the target VM supports reading class file
major and minor versions.

boolean

canGetConstantPool

()

Determines if the target VM supports getting constant pool
information of a class.

boolean

canGetCurrentContendedMonitor

()

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

boolean

canGetInstanceInfo

()

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

boolean

canGetMethodReturnValues

()

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

default boolean

canGetModuleInfo

()

Determines if the target VM supports getting information about modules.

boolean

canGetMonitorFrameInfo

()

Determines if the target VM supports getting which
frame has acquired a monitor.

boolean

canGetMonitorInfo

()

Determines if the target VM supports the retrieval
of the monitor information for an object.

boolean

canGetOwnedMonitorInfo

()

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

boolean

canGetSourceDebugExtension

()

Determines if the target VM supports getting
the source debug extension.

boolean

canGetSyntheticAttribute

()

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

boolean

canPopFrames

()

Determines if the target VM supports popping
frames of a threads stack.

boolean

canRedefineClasses

()

Determines if the target VM supports any level
of class redefinition.

boolean

canRequestMonitorEvents

()

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

boolean

canRequestVMDeathEvent

()

Determines if the target VM supports the creation of

VMDeathRequest

s.

boolean

canUnrestrictedlyRedefineClasses

()

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

boolean

canUseInstanceFilters

()

Determines if the target VM supports filtering
events by specific instance object.

boolean

canUseSourceNameFilters

()

Determines if the target VM supports the filtering of
class prepare events by source name.

boolean

canWatchFieldAccess

()

Determines if the target VM supports watchpoints
for field access.

boolean

canWatchFieldModification

()

Determines if the target VM supports watchpoints
for field modification.

List

<

ReferenceType

>

classesByName

​(

String

className)

Returns the loaded reference types that
match a given name.

String

description

()

Returns text information on the target VM and the
debugger support that mirrors it.

void

dispose

()

Invalidates this virtual machine mirror.

EventQueue

eventQueue

()

Returns the event queue for this virtual machine.

EventRequestManager

eventRequestManager

()

Returns the event request manager for this virtual machine.

void

exit

​(int exitCode)

Causes the mirrored VM to terminate with the given error code.

String

getDefaultStratum

()

Return this VM's default stratum.

long[]

instanceCounts

​(

List

<? extends

ReferenceType

> refTypes)

Returns the number of instances of each ReferenceType in the 'refTypes'
list.

BooleanValue

mirrorOf

​(boolean value)

Creates a

BooleanValue

for the given value.

ByteValue

mirrorOf

​(byte value)

Creates a

ByteValue

for the given value.

CharValue

mirrorOf

​(char value)

Creates a

CharValue

for the given value.

DoubleValue

mirrorOf

​(double value)

Creates a

DoubleValue

for the given value.

FloatValue

mirrorOf

​(float value)

Creates a

FloatValue

for the given value.

IntegerValue

mirrorOf

​(int value)

Creates an

IntegerValue

for the given value.

LongValue

mirrorOf

​(long value)

Creates a

LongValue

for the given value.

ShortValue

mirrorOf

​(short value)

Creates a

ShortValue

for the given value.

StringReference

mirrorOf

​(

String

value)

Creates a string in this virtual machine.

VoidValue

mirrorOfVoid

()

Creates a

VoidValue

.

String

name

()

Returns the name of the target VM as reported by the
property

java.vm.name

.

Process

process

()

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

void

redefineClasses

​(

Map

<? extends

ReferenceType

,​byte[]> classToBytes)

All classes given are redefined according to the
definitions supplied.

void

resume

()

Continues the execution of the application running in this
virtual machine.

void

setDebugTraceMode

​(int traceFlags)

Traces the activities performed by the com.sun.jdi implementation.

void

setDefaultStratum

​(

String

stratum)

Set this VM's default stratum (see

Location

for a
discussion of strata).

void

suspend

()

Suspends the execution of the application running in this
virtual machine.

List

<

ThreadGroupReference

>

topLevelThreadGroups

()

Returns each thread group which does not have a parent.

String

version

()

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Returns all loaded types.

Returns all modules.

Returns a list of the currently running threads.

Determines if the target VM supports the addition
of methods when performing class redefinition.

Determines if the target VM is a read-only VM.

Determines if the target VM supports the forcing of a method to
return early.

Determines if the target VM supports the retrieval
of a method's bytecodes.

Determines if the target VM supports reading class file
major and minor versions.

Determines if the target VM supports getting constant pool
information of a class.

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

Determines if the target VM supports getting information about modules.

Determines if the target VM supports getting which
frame has acquired a monitor.

Determines if the target VM supports the retrieval
of the monitor information for an object.

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

Determines if the target VM supports getting
the source debug extension.

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

Determines if the target VM supports popping
frames of a threads stack.

Determines if the target VM supports any level
of class redefinition.

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

Determines if the target VM supports the creation of

VMDeathRequest

s.

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

Determines if the target VM supports filtering
events by specific instance object.

Determines if the target VM supports the filtering of
class prepare events by source name.

Determines if the target VM supports watchpoints
for field access.

Determines if the target VM supports watchpoints
for field modification.

Returns the loaded reference types that
match a given name.

Returns text information on the target VM and the
debugger support that mirrors it.

Invalidates this virtual machine mirror.

Returns the event queue for this virtual machine.

Returns the event request manager for this virtual machine.

Causes the mirrored VM to terminate with the given error code.

Return this VM's default stratum.

Returns the number of instances of each ReferenceType in the 'refTypes'
list.

Creates a

BooleanValue

for the given value.

Creates a

ByteValue

for the given value.

Creates a

CharValue

for the given value.

Creates a

DoubleValue

for the given value.

Creates a

FloatValue

for the given value.

Creates an

IntegerValue

for the given value.

Creates a

LongValue

for the given value.

Creates a

ShortValue

for the given value.

Creates a string in this virtual machine.

Creates a

VoidValue

.

Returns the name of the target VM as reported by the
property

java.vm.name

.

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

All classes given are redefined according to the
definitions supplied.

Continues the execution of the application running in this
virtual machine.

Traces the activities performed by the com.sun.jdi implementation.

Set this VM's default stratum (see

Location

for a
discussion of strata).

Suspends the execution of the application running in this
virtual machine.

Returns each thread group which does not have a parent.

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ FIELD DETAIL ===========

- Field Detail

- TRACE_NONE

```java
static final int TRACE_NONE
```

All tracing is disabled.

**See Also:** Constant Field Values

- TRACE_SENDS

```java
static final int TRACE_SENDS
```

Tracing enabled for JDWP packets sent to target VM.

**See Also:** Constant Field Values

- TRACE_RECEIVES

```java
static final int TRACE_RECEIVES
```

Tracing enabled for JDWP packets received from target VM.

**See Also:** Constant Field Values

- TRACE_EVENTS

```java
static final int TRACE_EVENTS
```

Tracing enabled for internal event handling.

**See Also:** Constant Field Values

- TRACE_REFTYPES

```java
static final int TRACE_REFTYPES
```

Tracing enabled for internal managment of reference types.

**See Also:** Constant Field Values

- TRACE_OBJREFS

```java
static final int TRACE_OBJREFS
```

Tracing enabled for internal management of object references.

**See Also:** Constant Field Values

- TRACE_ALL

```java
static final int TRACE_ALL
```

All tracing is enabled.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- allModules

```java
default
List
<
ModuleReference
> allModules()
```

Returns all modules. For each module in the target
VM a

ModuleReference

will be placed in the returned list.

Not all target virtual machines support this operation.
Use

canGetModuleInfo()

to determine if the operation is supported.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** a list of

ModuleReference

objects, each mirroring
a module in the target VM.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Since:** 9

- classesByName

```java
List
<
ReferenceType
> classesByName​(
String
className)
```

Returns the loaded reference types that
match a given name. The name must be fully qualified
(for example, java.lang.String). The returned list
will contain a

ReferenceType

for each class
or interface found with the given name. The search
is confined to loaded classes only; no attempt is made
to load a class of the given name.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Parameters:** className

- the class/interface name to search for
**Returns:** a list of

ReferenceType

objects, each
mirroring a type in the target VM with the given name.

- allClasses

```java
List
<
ReferenceType
> allClasses()
```

Returns all loaded types. For each loaded type in the target
VM a

ReferenceType

will be placed in the returned list.
The list will include ReferenceTypes which mirror classes,
interfaces, and array types.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:** a list of

ReferenceType

objects, each mirroring
a loaded type in the target VM.

- redefineClasses

```java
void redefineClasses​(
Map
<? extends
ReferenceType
,​byte[]> classToBytes)
```

All classes given are redefined according to the
definitions supplied. A method in a redefined class
is called 'equivalent' (to the old version of the
method) if

- their bytecodes are the same except for indicies into
the constant pool, and

the referenced constants are equal.

Otherwise, the new method is called 'non-equivalent'.
If a redefined method has active stack frames, those active
frames continue to run the bytecodes of the previous version of the
method. If the new version of such a method is non-equivalent,
then a method from one of these active frames is called 'obsolete' and

Method.isObsolete()

will return true when called on one of these methods.
If resetting such a frame is desired, use

ThreadReference.popFrames(StackFrame)

to pop the old obsolete method execution from the stack.
New invocations of redefined methods will always invoke the new versions.

This function does not cause any initialization except
that which would occur under the customary JVM semantics.
In other words, redefining a class does not cause
its initializers to be run. The values of preexisting
static variables will remain as they were prior to the
call. However, completely uninitialized (new) static
variables will be assigned their default value.

If a redefined class has instances then all those
instances will have the fields defined by the redefined
class at the completion of the call. Preexisting fields
will retain their previous values. Any new fields will
have their default values; no instance initializers or
constructors are run.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

**Parameters:** classToBytes

- A map from

ReferenceType

to array of byte.
The bytes represent the new class definition and
are in Java Virtual Machine class file format.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- If

canRedefineClasses()

is false any call of this method will throw this exception.

If

canAddMethod()

is false
attempting to add a method will throw this exception.

If

canUnrestrictedlyRedefineClasses()

is false, attempting any of the following will throw
this exception

- changing the schema (the fields)

changing the hierarchy (superclasses, interfaces)

deleting a method

changing class modifiers

changing method modifiers

changing the

NestHost

or

NestMembers

class attributes
**Throws:** NoClassDefFoundError

- if the bytes
don't correspond to the reference type (the names
don't match).
**Throws:** VerifyError

- if a "verifier" detects
that a class, though well formed, contains an internal
inconsistency or security problem.
**Throws:** ClassFormatError

- if the bytes
do not represent a valid class.
**Throws:** ClassCircularityError

- if a
circularity has been detected while initializing a class.
**Throws:** UnsupportedClassVersionError

- if the
major and minor version numbers in bytes
are not supported by the VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.
**Since:** 1.4
**See Also:** Method.isObsolete()

,

ThreadReference.popFrames(com.sun.jdi.StackFrame)

,

canRedefineClasses()

,

canAddMethod()

,

canUnrestrictedlyRedefineClasses()

- allThreads

```java
List
<
ThreadReference
> allThreads()
```

Returns a list of the currently running threads. For each
running thread in the target VM, a

ThreadReference

that mirrors it is placed in the list.
The returned list contains threads created through
java.lang.Thread, all native threads attached to
the target VM through JNI, and system threads created
by the target VM. Thread objects that have
not yet been started
(see

Thread.start()

)
and thread objects that have
completed their execution are not included in the returned list.

**Returns:** a list of

ThreadReference

objects, one for each
running thread in the mirrored VM.

- suspend

```java
void suspend()
```

Suspends the execution of the application running in this
virtual machine. All threads currently running will be suspended.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

ThreadReference.resume()

)
the same number of times it has been suspended.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- resume

```java
void resume()
```

Continues the execution of the application running in this
virtual machine. All threads are resumed as documented in

ThreadReference.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.
**See Also:** suspend()

- topLevelThreadGroups

```java
List
<
ThreadGroupReference
> topLevelThreadGroups()
```

Returns each thread group which does not have a parent. For each
top level thread group a

ThreadGroupReference

is placed in the
returned list.

This command may be used as the first step in building a tree
(or trees) of the existing thread groups.

**Returns:** a list of

ThreadGroupReference

objects, one for each
top level thread group.

- eventQueue

```java
EventQueue
eventQueue()
```

Returns the event queue for this virtual machine.
A virtual machine has only one

EventQueue

object, this
method will return the same instance each time it
is invoked.

**Returns:** the

EventQueue

for this virtual machine.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- eventRequestManager

```java
EventRequestManager
eventRequestManager()
```

Returns the event request manager for this virtual machine.
The

EventRequestManager

controls user settable events
such as breakpoints.
A virtual machine has only one

EventRequestManager

object,
this method will return the same instance each time it
is invoked.

**Returns:** the

EventRequestManager

for this virtual machine.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- mirrorOf

```java
BooleanValue
mirrorOf​(boolean value)
```

Creates a

BooleanValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a boolean for which to create the value
**Returns:** the

BooleanValue

for the given boolean.

- mirrorOf

```java
ByteValue
mirrorOf​(byte value)
```

Creates a

ByteValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a byte for which to create the value
**Returns:** the

ByteValue

for the given byte.

- mirrorOf

```java
CharValue
mirrorOf​(char value)
```

Creates a

CharValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a char for which to create the value
**Returns:** the

CharValue

for the given char.

- mirrorOf

```java
ShortValue
mirrorOf​(short value)
```

Creates a

ShortValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a short for which to create the value
**Returns:** the

ShortValue

for the given short.

- mirrorOf

```java
IntegerValue
mirrorOf​(int value)
```

Creates an

IntegerValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- an int for which to create the value
**Returns:** the

IntegerValue

for the given int.

- mirrorOf

```java
LongValue
mirrorOf​(long value)
```

Creates a

LongValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a long for which to create the value
**Returns:** the

LongValue

for the given long.

- mirrorOf

```java
FloatValue
mirrorOf​(float value)
```

Creates a

FloatValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a float for which to create the value
**Returns:** the

FloatValue

for the given float.

- mirrorOf

```java
DoubleValue
mirrorOf​(double value)
```

Creates a

DoubleValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a double for which to create the value
**Returns:** the

DoubleValue

for the given double.

- mirrorOf

```java
StringReference
mirrorOf​(
String
value)
```

Creates a string in this virtual machine.
The created string can be used for setting and comparing against
a string value retrieved from a variable or field in this
virtual machine.

**Parameters:** value

- the string to be created
**Returns:** a

StringReference

that mirrors the newly created
string in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

- mirrorOfVoid

```java
VoidValue
mirrorOfVoid()
```

Creates a

VoidValue

. This value
can be passed to

ThreadReference.forceEarlyReturn(com.sun.jdi.Value)

when a void method is to be exited.

**Returns:** the

VoidValue

.

- process

```java
Process
process()
```

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

**Returns:** the

Process

object for this virtual
machine, or null if it was not launched by a

LaunchingConnector

.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

- dispose

```java
void dispose()
```

Invalidates this virtual machine mirror.
The communication channel to the target VM is closed, and
the target VM prepares to accept another subsequent connection
from this debugger or another debugger, including the
following tasks:

- All event requests are cancelled.

All threads suspended by

suspend()

or by

ThreadReference.suspend()

are resumed as many
times as necessary for them to run.

Garbage collection is re-enabled in all cases where it was
disabled through

ObjectReference.disableCollection()

.

Any current method invocations executing in the target VM
are continued after the disconnection. Upon completion of any such
method invocation, the invoking thread continues from the
location where it was originally stopped.

Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

- exit

```java
void exit​(int exitCode)
```

Causes the mirrored VM to terminate with the given error code.
All resources associated with this VirtualMachine are freed.
If the mirrored VM is remote, the communication channel
to it will be closed. Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

Threads running in the mirrored VM are abruptly terminated.
A thread death exception is not thrown and
finally blocks are not run.

**Parameters:** exitCode

- the exit code for the target VM. On some platforms,
the exit code might be truncated, for example, to the lower order 8 bits.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- canWatchFieldModification

```java
boolean canWatchFieldModification()
```

Determines if the target VM supports watchpoints
for field modification.

**Returns:** true

if the feature is supported,

false

otherwise.

- canWatchFieldAccess

```java
boolean canWatchFieldAccess()
```

Determines if the target VM supports watchpoints
for field access.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetBytecodes

```java
boolean canGetBytecodes()
```

Determines if the target VM supports the retrieval
of a method's bytecodes.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetSyntheticAttribute

```java
boolean canGetSyntheticAttribute()
```

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetOwnedMonitorInfo

```java
boolean canGetOwnedMonitorInfo()
```

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetCurrentContendedMonitor

```java
boolean canGetCurrentContendedMonitor()
```

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetMonitorInfo

```java
boolean canGetMonitorInfo()
```

Determines if the target VM supports the retrieval
of the monitor information for an object.

**Returns:** true

if the feature is supported,

false

otherwise.

- canUseInstanceFilters

```java
boolean canUseInstanceFilters()
```

Determines if the target VM supports filtering
events by specific instance object. For example,
see

BreakpointRequest.addInstanceFilter(com.sun.jdi.ObjectReference)

.

**Returns:** true

if the feature is supported,

false

otherwise.

- canRedefineClasses

```java
boolean canRedefineClasses()
```

Determines if the target VM supports any level
of class redefinition.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

- canAddMethod

```java
boolean canAddMethod()
```

Determines if the target VM supports the addition
of methods when performing class redefinition.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

- canUnrestrictedlyRedefineClasses

```java
boolean canUnrestrictedlyRedefineClasses()
```

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

- canPopFrames

```java
boolean canPopFrames()
```

Determines if the target VM supports popping
frames of a threads stack.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** ThreadReference.popFrames(com.sun.jdi.StackFrame)

- canGetSourceDebugExtension

```java
boolean canGetSourceDebugExtension()
```

Determines if the target VM supports getting
the source debug extension.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** ReferenceType.sourceDebugExtension()

- canRequestVMDeathEvent

```java
boolean canRequestVMDeathEvent()
```

Determines if the target VM supports the creation of

VMDeathRequest

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** EventRequestManager.createVMDeathRequest()

- canGetMethodReturnValues

```java
boolean canGetMethodReturnValues()
```

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** EventRequestManager.createMethodExitRequest()

- canGetInstanceInfo

```java
boolean canGetInstanceInfo()
```

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** instanceCounts(java.util.List<? extends com.sun.jdi.ReferenceType>)

,

ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

- canUseSourceNameFilters

```java
boolean canUseSourceNameFilters()
```

Determines if the target VM supports the filtering of
class prepare events by source name.

see

ClassPrepareRequest.addSourceNameFilter(java.lang.String)

.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6

- canForceEarlyReturn

```java
boolean canForceEarlyReturn()
```

Determines if the target VM supports the forcing of a method to
return early.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ThreadReference.forceEarlyReturn(Value)

- canBeModified

```java
boolean canBeModified()
```

Determines if the target VM is a read-only VM. If a method which
would modify the state of the VM is called on a read-only VM,
then

VMCannotBeModifiedException

is thrown.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.5

- canRequestMonitorEvents

```java
boolean canRequestMonitorEvents()
```

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

MonitorContendedEnteredRequest

s.

MonitorWaitRequest

s.

MonitorWaitedRequest

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** EventRequestManager.createMonitorContendedEnterRequest()

,

EventRequestManager.createMonitorContendedEnteredRequest()

,

EventRequestManager.createMonitorWaitRequest()

,

EventRequestManager.createMonitorWaitedRequest()

- canGetMonitorFrameInfo

```java
boolean canGetMonitorFrameInfo()
```

Determines if the target VM supports getting which
frame has acquired a monitor.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ThreadReference.ownedMonitorsAndFrames()

- canGetClassFileVersion

```java
boolean canGetClassFileVersion()
```

Determines if the target VM supports reading class file
major and minor versions.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ReferenceType.majorVersion()

,

ReferenceType.minorVersion()

- canGetConstantPool

```java
boolean canGetConstantPool()
```

Determines if the target VM supports getting constant pool
information of a class.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ReferenceType.constantPoolCount()

,

ReferenceType.constantPool()

- canGetModuleInfo

```java
default boolean canGetModuleInfo()
```

Determines if the target VM supports getting information about modules.

**Implementation Requirements:** The default implementation returns

false

.
**Returns:** true

if the feature is supported,

false

otherwise
**Since:** 9
**See Also:** allModules()

,

ReferenceType.module()

,

ModuleReference

- setDefaultStratum

```java
void setDefaultStratum​(
String
stratum)
```

Set this VM's default stratum (see

Location

for a
discussion of strata). Overrides the per-class default set
in the class file.

Affects location queries (such as,

Location.sourceName()

)
and the line boundaries used in
single stepping.

**Parameters:** stratum

- the stratum to set as VM default,
or null to use per-class defaults.
**Throws:** UnsupportedOperationException

- if the
target virtual machine does not support this operation.
**Since:** 1.4

- getDefaultStratum

```java
String
getDefaultStratum()
```

Return this VM's default stratum.

**Returns:** null

(meaning that the per-class
default -

ReferenceType.defaultStratum()

-
should be used) unless the default stratum has been
set with

setDefaultStratum(String)

.
**Since:** 1.4
**See Also:** setDefaultStratum(String)

,

ReferenceType.defaultStratum()

- instanceCounts

```java
long[] instanceCounts​(
List
<? extends
ReferenceType
> refTypes)
```

Returns the number of instances of each ReferenceType in the 'refTypes'
list.
Only instances that are reachable for the purposes of garbage collection
are counted.

Not all target virtual machines support this operation.
Use

canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:** refTypes

- the list of

ReferenceType

objects for which counts
are to be obtained.
**Returns:** an array of

long

containing one element for each
element in the 'refTypes' list. Element i of the array contains
the number of instances in the target VM of the ReferenceType at
position i in the 'refTypes' list.
If the 'refTypes' list is empty, a zero-length array is returned.
If a ReferenceType in refTypes has been garbage collected, zero
is returned for its instance count.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
**Throws:** NullPointerException

- if the 'refTypes' list is null.
**Since:** 1.6
**See Also:** ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

- description

```java
String
description()
```

Returns text information on the target VM and the
debugger support that mirrors it. No specific format
for this information is guaranteed.
Typically, this string contains version information for the
target VM and debugger interfaces.
More precise information
on VM and JDI versions is available through

version()

,

VirtualMachineManager.majorInterfaceVersion()

,
and

VirtualMachineManager.minorInterfaceVersion()

**Returns:** the description.

- version

```java
String
version()
```

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.
For obtaining the JDI interface version, use

VirtualMachineManager.majorInterfaceVersion()

and

VirtualMachineManager.minorInterfaceVersion()

**Returns:** the target VM version.

- name

```java
String
name()
```

Returns the name of the target VM as reported by the
property

java.vm.name

.

**Returns:** the target VM name.

- setDebugTraceMode

```java
void setDebugTraceMode​(int traceFlags)
```

Traces the activities performed by the com.sun.jdi implementation.
All trace information is output to System.err. The given trace
flags are used to limit the output to only the information
desired. The given flags are in effect and the corresponding
trace will continue until the next call to
this method.

Output is implementation dependent and trace mode may be ignored.

**Parameters:** traceFlags

- identifies which kinds of tracing to enable.

Field Detail

- TRACE_NONE

```java
static final int TRACE_NONE
```

All tracing is disabled.

**See Also:** Constant Field Values

- TRACE_SENDS

```java
static final int TRACE_SENDS
```

Tracing enabled for JDWP packets sent to target VM.

**See Also:** Constant Field Values

- TRACE_RECEIVES

```java
static final int TRACE_RECEIVES
```

Tracing enabled for JDWP packets received from target VM.

**See Also:** Constant Field Values

- TRACE_EVENTS

```java
static final int TRACE_EVENTS
```

Tracing enabled for internal event handling.

**See Also:** Constant Field Values

- TRACE_REFTYPES

```java
static final int TRACE_REFTYPES
```

Tracing enabled for internal managment of reference types.

**See Also:** Constant Field Values

- TRACE_OBJREFS

```java
static final int TRACE_OBJREFS
```

Tracing enabled for internal management of object references.

**See Also:** Constant Field Values

- TRACE_ALL

```java
static final int TRACE_ALL
```

All tracing is enabled.

**See Also:** Constant Field Values

---

#### Field Detail

TRACE_NONE

```java
static final int TRACE_NONE
```

All tracing is disabled.

**See Also:** Constant Field Values

---

#### TRACE_NONE

static final int TRACE_NONE

All tracing is disabled.

TRACE_SENDS

```java
static final int TRACE_SENDS
```

Tracing enabled for JDWP packets sent to target VM.

**See Also:** Constant Field Values

---

#### TRACE_SENDS

static final int TRACE_SENDS

Tracing enabled for JDWP packets sent to target VM.

TRACE_RECEIVES

```java
static final int TRACE_RECEIVES
```

Tracing enabled for JDWP packets received from target VM.

**See Also:** Constant Field Values

---

#### TRACE_RECEIVES

static final int TRACE_RECEIVES

Tracing enabled for JDWP packets received from target VM.

TRACE_EVENTS

```java
static final int TRACE_EVENTS
```

Tracing enabled for internal event handling.

**See Also:** Constant Field Values

---

#### TRACE_EVENTS

static final int TRACE_EVENTS

Tracing enabled for internal event handling.

TRACE_REFTYPES

```java
static final int TRACE_REFTYPES
```

Tracing enabled for internal managment of reference types.

**See Also:** Constant Field Values

---

#### TRACE_REFTYPES

static final int TRACE_REFTYPES

Tracing enabled for internal managment of reference types.

TRACE_OBJREFS

```java
static final int TRACE_OBJREFS
```

Tracing enabled for internal management of object references.

**See Also:** Constant Field Values

---

#### TRACE_OBJREFS

static final int TRACE_OBJREFS

Tracing enabled for internal management of object references.

TRACE_ALL

```java
static final int TRACE_ALL
```

All tracing is enabled.

**See Also:** Constant Field Values

---

#### TRACE_ALL

static final int TRACE_ALL

All tracing is enabled.

Method Detail

- allModules

```java
default
List
<
ModuleReference
> allModules()
```

Returns all modules. For each module in the target
VM a

ModuleReference

will be placed in the returned list.

Not all target virtual machines support this operation.
Use

canGetModuleInfo()

to determine if the operation is supported.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** a list of

ModuleReference

objects, each mirroring
a module in the target VM.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Since:** 9

- classesByName

```java
List
<
ReferenceType
> classesByName​(
String
className)
```

Returns the loaded reference types that
match a given name. The name must be fully qualified
(for example, java.lang.String). The returned list
will contain a

ReferenceType

for each class
or interface found with the given name. The search
is confined to loaded classes only; no attempt is made
to load a class of the given name.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Parameters:** className

- the class/interface name to search for
**Returns:** a list of

ReferenceType

objects, each
mirroring a type in the target VM with the given name.

- allClasses

```java
List
<
ReferenceType
> allClasses()
```

Returns all loaded types. For each loaded type in the target
VM a

ReferenceType

will be placed in the returned list.
The list will include ReferenceTypes which mirror classes,
interfaces, and array types.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:** a list of

ReferenceType

objects, each mirroring
a loaded type in the target VM.

- redefineClasses

```java
void redefineClasses​(
Map
<? extends
ReferenceType
,​byte[]> classToBytes)
```

All classes given are redefined according to the
definitions supplied. A method in a redefined class
is called 'equivalent' (to the old version of the
method) if

- their bytecodes are the same except for indicies into
the constant pool, and

the referenced constants are equal.

Otherwise, the new method is called 'non-equivalent'.
If a redefined method has active stack frames, those active
frames continue to run the bytecodes of the previous version of the
method. If the new version of such a method is non-equivalent,
then a method from one of these active frames is called 'obsolete' and

Method.isObsolete()

will return true when called on one of these methods.
If resetting such a frame is desired, use

ThreadReference.popFrames(StackFrame)

to pop the old obsolete method execution from the stack.
New invocations of redefined methods will always invoke the new versions.

This function does not cause any initialization except
that which would occur under the customary JVM semantics.
In other words, redefining a class does not cause
its initializers to be run. The values of preexisting
static variables will remain as they were prior to the
call. However, completely uninitialized (new) static
variables will be assigned their default value.

If a redefined class has instances then all those
instances will have the fields defined by the redefined
class at the completion of the call. Preexisting fields
will retain their previous values. Any new fields will
have their default values; no instance initializers or
constructors are run.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

**Parameters:** classToBytes

- A map from

ReferenceType

to array of byte.
The bytes represent the new class definition and
are in Java Virtual Machine class file format.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- If

canRedefineClasses()

is false any call of this method will throw this exception.

If

canAddMethod()

is false
attempting to add a method will throw this exception.

If

canUnrestrictedlyRedefineClasses()

is false, attempting any of the following will throw
this exception

- changing the schema (the fields)

changing the hierarchy (superclasses, interfaces)

deleting a method

changing class modifiers

changing method modifiers

changing the

NestHost

or

NestMembers

class attributes
**Throws:** NoClassDefFoundError

- if the bytes
don't correspond to the reference type (the names
don't match).
**Throws:** VerifyError

- if a "verifier" detects
that a class, though well formed, contains an internal
inconsistency or security problem.
**Throws:** ClassFormatError

- if the bytes
do not represent a valid class.
**Throws:** ClassCircularityError

- if a
circularity has been detected while initializing a class.
**Throws:** UnsupportedClassVersionError

- if the
major and minor version numbers in bytes
are not supported by the VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.
**Since:** 1.4
**See Also:** Method.isObsolete()

,

ThreadReference.popFrames(com.sun.jdi.StackFrame)

,

canRedefineClasses()

,

canAddMethod()

,

canUnrestrictedlyRedefineClasses()

- allThreads

```java
List
<
ThreadReference
> allThreads()
```

Returns a list of the currently running threads. For each
running thread in the target VM, a

ThreadReference

that mirrors it is placed in the list.
The returned list contains threads created through
java.lang.Thread, all native threads attached to
the target VM through JNI, and system threads created
by the target VM. Thread objects that have
not yet been started
(see

Thread.start()

)
and thread objects that have
completed their execution are not included in the returned list.

**Returns:** a list of

ThreadReference

objects, one for each
running thread in the mirrored VM.

- suspend

```java
void suspend()
```

Suspends the execution of the application running in this
virtual machine. All threads currently running will be suspended.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

ThreadReference.resume()

)
the same number of times it has been suspended.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- resume

```java
void resume()
```

Continues the execution of the application running in this
virtual machine. All threads are resumed as documented in

ThreadReference.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.
**See Also:** suspend()

- topLevelThreadGroups

```java
List
<
ThreadGroupReference
> topLevelThreadGroups()
```

Returns each thread group which does not have a parent. For each
top level thread group a

ThreadGroupReference

is placed in the
returned list.

This command may be used as the first step in building a tree
(or trees) of the existing thread groups.

**Returns:** a list of

ThreadGroupReference

objects, one for each
top level thread group.

- eventQueue

```java
EventQueue
eventQueue()
```

Returns the event queue for this virtual machine.
A virtual machine has only one

EventQueue

object, this
method will return the same instance each time it
is invoked.

**Returns:** the

EventQueue

for this virtual machine.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- eventRequestManager

```java
EventRequestManager
eventRequestManager()
```

Returns the event request manager for this virtual machine.
The

EventRequestManager

controls user settable events
such as breakpoints.
A virtual machine has only one

EventRequestManager

object,
this method will return the same instance each time it
is invoked.

**Returns:** the

EventRequestManager

for this virtual machine.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- mirrorOf

```java
BooleanValue
mirrorOf​(boolean value)
```

Creates a

BooleanValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a boolean for which to create the value
**Returns:** the

BooleanValue

for the given boolean.

- mirrorOf

```java
ByteValue
mirrorOf​(byte value)
```

Creates a

ByteValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a byte for which to create the value
**Returns:** the

ByteValue

for the given byte.

- mirrorOf

```java
CharValue
mirrorOf​(char value)
```

Creates a

CharValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a char for which to create the value
**Returns:** the

CharValue

for the given char.

- mirrorOf

```java
ShortValue
mirrorOf​(short value)
```

Creates a

ShortValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a short for which to create the value
**Returns:** the

ShortValue

for the given short.

- mirrorOf

```java
IntegerValue
mirrorOf​(int value)
```

Creates an

IntegerValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- an int for which to create the value
**Returns:** the

IntegerValue

for the given int.

- mirrorOf

```java
LongValue
mirrorOf​(long value)
```

Creates a

LongValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a long for which to create the value
**Returns:** the

LongValue

for the given long.

- mirrorOf

```java
FloatValue
mirrorOf​(float value)
```

Creates a

FloatValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a float for which to create the value
**Returns:** the

FloatValue

for the given float.

- mirrorOf

```java
DoubleValue
mirrorOf​(double value)
```

Creates a

DoubleValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a double for which to create the value
**Returns:** the

DoubleValue

for the given double.

- mirrorOf

```java
StringReference
mirrorOf​(
String
value)
```

Creates a string in this virtual machine.
The created string can be used for setting and comparing against
a string value retrieved from a variable or field in this
virtual machine.

**Parameters:** value

- the string to be created
**Returns:** a

StringReference

that mirrors the newly created
string in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

- mirrorOfVoid

```java
VoidValue
mirrorOfVoid()
```

Creates a

VoidValue

. This value
can be passed to

ThreadReference.forceEarlyReturn(com.sun.jdi.Value)

when a void method is to be exited.

**Returns:** the

VoidValue

.

- process

```java
Process
process()
```

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

**Returns:** the

Process

object for this virtual
machine, or null if it was not launched by a

LaunchingConnector

.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

- dispose

```java
void dispose()
```

Invalidates this virtual machine mirror.
The communication channel to the target VM is closed, and
the target VM prepares to accept another subsequent connection
from this debugger or another debugger, including the
following tasks:

- All event requests are cancelled.

All threads suspended by

suspend()

or by

ThreadReference.suspend()

are resumed as many
times as necessary for them to run.

Garbage collection is re-enabled in all cases where it was
disabled through

ObjectReference.disableCollection()

.

Any current method invocations executing in the target VM
are continued after the disconnection. Upon completion of any such
method invocation, the invoking thread continues from the
location where it was originally stopped.

Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

- exit

```java
void exit​(int exitCode)
```

Causes the mirrored VM to terminate with the given error code.
All resources associated with this VirtualMachine are freed.
If the mirrored VM is remote, the communication channel
to it will be closed. Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

Threads running in the mirrored VM are abruptly terminated.
A thread death exception is not thrown and
finally blocks are not run.

**Parameters:** exitCode

- the exit code for the target VM. On some platforms,
the exit code might be truncated, for example, to the lower order 8 bits.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

- canWatchFieldModification

```java
boolean canWatchFieldModification()
```

Determines if the target VM supports watchpoints
for field modification.

**Returns:** true

if the feature is supported,

false

otherwise.

- canWatchFieldAccess

```java
boolean canWatchFieldAccess()
```

Determines if the target VM supports watchpoints
for field access.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetBytecodes

```java
boolean canGetBytecodes()
```

Determines if the target VM supports the retrieval
of a method's bytecodes.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetSyntheticAttribute

```java
boolean canGetSyntheticAttribute()
```

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetOwnedMonitorInfo

```java
boolean canGetOwnedMonitorInfo()
```

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetCurrentContendedMonitor

```java
boolean canGetCurrentContendedMonitor()
```

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

**Returns:** true

if the feature is supported,

false

otherwise.

- canGetMonitorInfo

```java
boolean canGetMonitorInfo()
```

Determines if the target VM supports the retrieval
of the monitor information for an object.

**Returns:** true

if the feature is supported,

false

otherwise.

- canUseInstanceFilters

```java
boolean canUseInstanceFilters()
```

Determines if the target VM supports filtering
events by specific instance object. For example,
see

BreakpointRequest.addInstanceFilter(com.sun.jdi.ObjectReference)

.

**Returns:** true

if the feature is supported,

false

otherwise.

- canRedefineClasses

```java
boolean canRedefineClasses()
```

Determines if the target VM supports any level
of class redefinition.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

- canAddMethod

```java
boolean canAddMethod()
```

Determines if the target VM supports the addition
of methods when performing class redefinition.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

- canUnrestrictedlyRedefineClasses

```java
boolean canUnrestrictedlyRedefineClasses()
```

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

- canPopFrames

```java
boolean canPopFrames()
```

Determines if the target VM supports popping
frames of a threads stack.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** ThreadReference.popFrames(com.sun.jdi.StackFrame)

- canGetSourceDebugExtension

```java
boolean canGetSourceDebugExtension()
```

Determines if the target VM supports getting
the source debug extension.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** ReferenceType.sourceDebugExtension()

- canRequestVMDeathEvent

```java
boolean canRequestVMDeathEvent()
```

Determines if the target VM supports the creation of

VMDeathRequest

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** EventRequestManager.createVMDeathRequest()

- canGetMethodReturnValues

```java
boolean canGetMethodReturnValues()
```

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** EventRequestManager.createMethodExitRequest()

- canGetInstanceInfo

```java
boolean canGetInstanceInfo()
```

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** instanceCounts(java.util.List<? extends com.sun.jdi.ReferenceType>)

,

ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

- canUseSourceNameFilters

```java
boolean canUseSourceNameFilters()
```

Determines if the target VM supports the filtering of
class prepare events by source name.

see

ClassPrepareRequest.addSourceNameFilter(java.lang.String)

.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6

- canForceEarlyReturn

```java
boolean canForceEarlyReturn()
```

Determines if the target VM supports the forcing of a method to
return early.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ThreadReference.forceEarlyReturn(Value)

- canBeModified

```java
boolean canBeModified()
```

Determines if the target VM is a read-only VM. If a method which
would modify the state of the VM is called on a read-only VM,
then

VMCannotBeModifiedException

is thrown.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.5

- canRequestMonitorEvents

```java
boolean canRequestMonitorEvents()
```

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

MonitorContendedEnteredRequest

s.

MonitorWaitRequest

s.

MonitorWaitedRequest

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** EventRequestManager.createMonitorContendedEnterRequest()

,

EventRequestManager.createMonitorContendedEnteredRequest()

,

EventRequestManager.createMonitorWaitRequest()

,

EventRequestManager.createMonitorWaitedRequest()

- canGetMonitorFrameInfo

```java
boolean canGetMonitorFrameInfo()
```

Determines if the target VM supports getting which
frame has acquired a monitor.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ThreadReference.ownedMonitorsAndFrames()

- canGetClassFileVersion

```java
boolean canGetClassFileVersion()
```

Determines if the target VM supports reading class file
major and minor versions.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ReferenceType.majorVersion()

,

ReferenceType.minorVersion()

- canGetConstantPool

```java
boolean canGetConstantPool()
```

Determines if the target VM supports getting constant pool
information of a class.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ReferenceType.constantPoolCount()

,

ReferenceType.constantPool()

- canGetModuleInfo

```java
default boolean canGetModuleInfo()
```

Determines if the target VM supports getting information about modules.

**Implementation Requirements:** The default implementation returns

false

.
**Returns:** true

if the feature is supported,

false

otherwise
**Since:** 9
**See Also:** allModules()

,

ReferenceType.module()

,

ModuleReference

- setDefaultStratum

```java
void setDefaultStratum​(
String
stratum)
```

Set this VM's default stratum (see

Location

for a
discussion of strata). Overrides the per-class default set
in the class file.

Affects location queries (such as,

Location.sourceName()

)
and the line boundaries used in
single stepping.

**Parameters:** stratum

- the stratum to set as VM default,
or null to use per-class defaults.
**Throws:** UnsupportedOperationException

- if the
target virtual machine does not support this operation.
**Since:** 1.4

- getDefaultStratum

```java
String
getDefaultStratum()
```

Return this VM's default stratum.

**Returns:** null

(meaning that the per-class
default -

ReferenceType.defaultStratum()

-
should be used) unless the default stratum has been
set with

setDefaultStratum(String)

.
**Since:** 1.4
**See Also:** setDefaultStratum(String)

,

ReferenceType.defaultStratum()

- instanceCounts

```java
long[] instanceCounts​(
List
<? extends
ReferenceType
> refTypes)
```

Returns the number of instances of each ReferenceType in the 'refTypes'
list.
Only instances that are reachable for the purposes of garbage collection
are counted.

Not all target virtual machines support this operation.
Use

canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:** refTypes

- the list of

ReferenceType

objects for which counts
are to be obtained.
**Returns:** an array of

long

containing one element for each
element in the 'refTypes' list. Element i of the array contains
the number of instances in the target VM of the ReferenceType at
position i in the 'refTypes' list.
If the 'refTypes' list is empty, a zero-length array is returned.
If a ReferenceType in refTypes has been garbage collected, zero
is returned for its instance count.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
**Throws:** NullPointerException

- if the 'refTypes' list is null.
**Since:** 1.6
**See Also:** ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

- description

```java
String
description()
```

Returns text information on the target VM and the
debugger support that mirrors it. No specific format
for this information is guaranteed.
Typically, this string contains version information for the
target VM and debugger interfaces.
More precise information
on VM and JDI versions is available through

version()

,

VirtualMachineManager.majorInterfaceVersion()

,
and

VirtualMachineManager.minorInterfaceVersion()

**Returns:** the description.

- version

```java
String
version()
```

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.
For obtaining the JDI interface version, use

VirtualMachineManager.majorInterfaceVersion()

and

VirtualMachineManager.minorInterfaceVersion()

**Returns:** the target VM version.

- name

```java
String
name()
```

Returns the name of the target VM as reported by the
property

java.vm.name

.

**Returns:** the target VM name.

- setDebugTraceMode

```java
void setDebugTraceMode​(int traceFlags)
```

Traces the activities performed by the com.sun.jdi implementation.
All trace information is output to System.err. The given trace
flags are used to limit the output to only the information
desired. The given flags are in effect and the corresponding
trace will continue until the next call to
this method.

Output is implementation dependent and trace mode may be ignored.

**Parameters:** traceFlags

- identifies which kinds of tracing to enable.

---

#### Method Detail

allModules

```java
default
List
<
ModuleReference
> allModules()
```

Returns all modules. For each module in the target
VM a

ModuleReference

will be placed in the returned list.

Not all target virtual machines support this operation.
Use

canGetModuleInfo()

to determine if the operation is supported.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** a list of

ModuleReference

objects, each mirroring
a module in the target VM.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Since:** 9

---

#### allModules

default

List

<

ModuleReference

> allModules()

Returns all modules. For each module in the target
VM a

ModuleReference

will be placed in the returned list.

Not all target virtual machines support this operation.
Use

canGetModuleInfo()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

canGetModuleInfo()

to determine if the operation is supported.

classesByName

```java
List
<
ReferenceType
> classesByName​(
String
className)
```

Returns the loaded reference types that
match a given name. The name must be fully qualified
(for example, java.lang.String). The returned list
will contain a

ReferenceType

for each class
or interface found with the given name. The search
is confined to loaded classes only; no attempt is made
to load a class of the given name.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Parameters:** className

- the class/interface name to search for
**Returns:** a list of

ReferenceType

objects, each
mirroring a type in the target VM with the given name.

---

#### classesByName

List

<

ReferenceType

> classesByName​(

String

className)

Returns the loaded reference types that
match a given name. The name must be fully qualified
(for example, java.lang.String). The returned list
will contain a

ReferenceType

for each class
or interface found with the given name. The search
is confined to loaded classes only; no attempt is made
to load a class of the given name.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

allClasses

```java
List
<
ReferenceType
> allClasses()
```

Returns all loaded types. For each loaded type in the target
VM a

ReferenceType

will be placed in the returned list.
The list will include ReferenceTypes which mirror classes,
interfaces, and array types.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:** a list of

ReferenceType

objects, each mirroring
a loaded type in the target VM.

---

#### allClasses

List

<

ReferenceType

> allClasses()

Returns all loaded types. For each loaded type in the target
VM a

ReferenceType

will be placed in the returned list.
The list will include ReferenceTypes which mirror classes,
interfaces, and array types.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

redefineClasses

```java
void redefineClasses​(
Map
<? extends
ReferenceType
,​byte[]> classToBytes)
```

All classes given are redefined according to the
definitions supplied. A method in a redefined class
is called 'equivalent' (to the old version of the
method) if

- their bytecodes are the same except for indicies into
the constant pool, and

the referenced constants are equal.

Otherwise, the new method is called 'non-equivalent'.
If a redefined method has active stack frames, those active
frames continue to run the bytecodes of the previous version of the
method. If the new version of such a method is non-equivalent,
then a method from one of these active frames is called 'obsolete' and

Method.isObsolete()

will return true when called on one of these methods.
If resetting such a frame is desired, use

ThreadReference.popFrames(StackFrame)

to pop the old obsolete method execution from the stack.
New invocations of redefined methods will always invoke the new versions.

This function does not cause any initialization except
that which would occur under the customary JVM semantics.
In other words, redefining a class does not cause
its initializers to be run. The values of preexisting
static variables will remain as they were prior to the
call. However, completely uninitialized (new) static
variables will be assigned their default value.

If a redefined class has instances then all those
instances will have the fields defined by the redefined
class at the completion of the call. Preexisting fields
will retain their previous values. Any new fields will
have their default values; no instance initializers or
constructors are run.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

**Parameters:** classToBytes

- A map from

ReferenceType

to array of byte.
The bytes represent the new class definition and
are in Java Virtual Machine class file format.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- If

canRedefineClasses()

is false any call of this method will throw this exception.

If

canAddMethod()

is false
attempting to add a method will throw this exception.

If

canUnrestrictedlyRedefineClasses()

is false, attempting any of the following will throw
this exception

- changing the schema (the fields)

changing the hierarchy (superclasses, interfaces)

deleting a method

changing class modifiers

changing method modifiers

changing the

NestHost

or

NestMembers

class attributes
**Throws:** NoClassDefFoundError

- if the bytes
don't correspond to the reference type (the names
don't match).
**Throws:** VerifyError

- if a "verifier" detects
that a class, though well formed, contains an internal
inconsistency or security problem.
**Throws:** ClassFormatError

- if the bytes
do not represent a valid class.
**Throws:** ClassCircularityError

- if a
circularity has been detected while initializing a class.
**Throws:** UnsupportedClassVersionError

- if the
major and minor version numbers in bytes
are not supported by the VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.
**Since:** 1.4
**See Also:** Method.isObsolete()

,

ThreadReference.popFrames(com.sun.jdi.StackFrame)

,

canRedefineClasses()

,

canAddMethod()

,

canUnrestrictedlyRedefineClasses()

---

#### redefineClasses

void redefineClasses​(

Map

<? extends

ReferenceType

,​byte[]> classToBytes)

All classes given are redefined according to the
definitions supplied. A method in a redefined class
is called 'equivalent' (to the old version of the
method) if

- their bytecodes are the same except for indicies into
the constant pool, and

the referenced constants are equal.

Otherwise, the new method is called 'non-equivalent'.
If a redefined method has active stack frames, those active
frames continue to run the bytecodes of the previous version of the
method. If the new version of such a method is non-equivalent,
then a method from one of these active frames is called 'obsolete' and

Method.isObsolete()

will return true when called on one of these methods.
If resetting such a frame is desired, use

ThreadReference.popFrames(StackFrame)

to pop the old obsolete method execution from the stack.
New invocations of redefined methods will always invoke the new versions.

This function does not cause any initialization except
that which would occur under the customary JVM semantics.
In other words, redefining a class does not cause
its initializers to be run. The values of preexisting
static variables will remain as they were prior to the
call. However, completely uninitialized (new) static
variables will be assigned their default value.

If a redefined class has instances then all those
instances will have the fields defined by the redefined
class at the completion of the call. Preexisting fields
will retain their previous values. Any new fields will
have their default values; no instance initializers or
constructors are run.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

their bytecodes are the same except for indicies into
the constant pool, and

the referenced constants are equal.

This function does not cause any initialization except
that which would occur under the customary JVM semantics.
In other words, redefining a class does not cause
its initializers to be run. The values of preexisting
static variables will remain as they were prior to the
call. However, completely uninitialized (new) static
variables will be assigned their default value.

If a redefined class has instances then all those
instances will have the fields defined by the redefined
class at the completion of the call. Preexisting fields
will retain their previous values. Any new fields will
have their default values; no instance initializers or
constructors are run.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

If a redefined class has instances then all those
instances will have the fields defined by the redefined
class at the completion of the call. Preexisting fields
will retain their previous values. Any new fields will
have their default values; no instance initializers or
constructors are run.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

Threads need not be suspended.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

No events are generated by this function.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

All breakpoints in the redefined classes are deleted.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

Not all target virtual machines support this operation.
Use

canRedefineClasses()

to determine if the operation is supported.
Use

canAddMethod()

to determine if the redefinition can add methods.
Use

canUnrestrictedlyRedefineClasses()

to determine if the redefinition can change the schema,
delete methods, change the class hierarchy, etc.

If

canRedefineClasses()

is false any call of this method will throw this exception.

If

canAddMethod()

is false
attempting to add a method will throw this exception.

If

canUnrestrictedlyRedefineClasses()

is false, attempting any of the following will throw
this exception

- changing the schema (the fields)

changing the hierarchy (superclasses, interfaces)

deleting a method

changing class modifiers

changing method modifiers

changing the

NestHost

or

NestMembers

class attributes

changing the schema (the fields)

changing the hierarchy (superclasses, interfaces)

deleting a method

changing class modifiers

changing method modifiers

changing the

NestHost

or

NestMembers

class attributes

allThreads

```java
List
<
ThreadReference
> allThreads()
```

Returns a list of the currently running threads. For each
running thread in the target VM, a

ThreadReference

that mirrors it is placed in the list.
The returned list contains threads created through
java.lang.Thread, all native threads attached to
the target VM through JNI, and system threads created
by the target VM. Thread objects that have
not yet been started
(see

Thread.start()

)
and thread objects that have
completed their execution are not included in the returned list.

**Returns:** a list of

ThreadReference

objects, one for each
running thread in the mirrored VM.

---

#### allThreads

List

<

ThreadReference

> allThreads()

Returns a list of the currently running threads. For each
running thread in the target VM, a

ThreadReference

that mirrors it is placed in the list.
The returned list contains threads created through
java.lang.Thread, all native threads attached to
the target VM through JNI, and system threads created
by the target VM. Thread objects that have
not yet been started
(see

Thread.start()

)
and thread objects that have
completed their execution are not included in the returned list.

suspend

```java
void suspend()
```

Suspends the execution of the application running in this
virtual machine. All threads currently running will be suspended.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

ThreadReference.resume()

)
the same number of times it has been suspended.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### suspend

void suspend()

Suspends the execution of the application running in this
virtual machine. All threads currently running will be suspended.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

ThreadReference.resume()

)
the same number of times it has been suspended.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

ThreadReference.resume()

)
the same number of times it has been suspended.

resume

```java
void resume()
```

Continues the execution of the application running in this
virtual machine. All threads are resumed as documented in

ThreadReference.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.
**See Also:** suspend()

---

#### resume

void resume()

Continues the execution of the application running in this
virtual machine. All threads are resumed as documented in

ThreadReference.resume()

.

topLevelThreadGroups

```java
List
<
ThreadGroupReference
> topLevelThreadGroups()
```

Returns each thread group which does not have a parent. For each
top level thread group a

ThreadGroupReference

is placed in the
returned list.

This command may be used as the first step in building a tree
(or trees) of the existing thread groups.

**Returns:** a list of

ThreadGroupReference

objects, one for each
top level thread group.

---

#### topLevelThreadGroups

List

<

ThreadGroupReference

> topLevelThreadGroups()

Returns each thread group which does not have a parent. For each
top level thread group a

ThreadGroupReference

is placed in the
returned list.

This command may be used as the first step in building a tree
(or trees) of the existing thread groups.

This command may be used as the first step in building a tree
(or trees) of the existing thread groups.

eventQueue

```java
EventQueue
eventQueue()
```

Returns the event queue for this virtual machine.
A virtual machine has only one

EventQueue

object, this
method will return the same instance each time it
is invoked.

**Returns:** the

EventQueue

for this virtual machine.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### eventQueue

EventQueue

eventQueue()

Returns the event queue for this virtual machine.
A virtual machine has only one

EventQueue

object, this
method will return the same instance each time it
is invoked.

eventRequestManager

```java
EventRequestManager
eventRequestManager()
```

Returns the event request manager for this virtual machine.
The

EventRequestManager

controls user settable events
such as breakpoints.
A virtual machine has only one

EventRequestManager

object,
this method will return the same instance each time it
is invoked.

**Returns:** the

EventRequestManager

for this virtual machine.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### eventRequestManager

EventRequestManager

eventRequestManager()

Returns the event request manager for this virtual machine.
The

EventRequestManager

controls user settable events
such as breakpoints.
A virtual machine has only one

EventRequestManager

object,
this method will return the same instance each time it
is invoked.

mirrorOf

```java
BooleanValue
mirrorOf​(boolean value)
```

Creates a

BooleanValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a boolean for which to create the value
**Returns:** the

BooleanValue

for the given boolean.

---

#### mirrorOf

BooleanValue

mirrorOf​(boolean value)

Creates a

BooleanValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
ByteValue
mirrorOf​(byte value)
```

Creates a

ByteValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a byte for which to create the value
**Returns:** the

ByteValue

for the given byte.

---

#### mirrorOf

ByteValue

mirrorOf​(byte value)

Creates a

ByteValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
CharValue
mirrorOf​(char value)
```

Creates a

CharValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a char for which to create the value
**Returns:** the

CharValue

for the given char.

---

#### mirrorOf

CharValue

mirrorOf​(char value)

Creates a

CharValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
ShortValue
mirrorOf​(short value)
```

Creates a

ShortValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a short for which to create the value
**Returns:** the

ShortValue

for the given short.

---

#### mirrorOf

ShortValue

mirrorOf​(short value)

Creates a

ShortValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
IntegerValue
mirrorOf​(int value)
```

Creates an

IntegerValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- an int for which to create the value
**Returns:** the

IntegerValue

for the given int.

---

#### mirrorOf

IntegerValue

mirrorOf​(int value)

Creates an

IntegerValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
LongValue
mirrorOf​(long value)
```

Creates a

LongValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a long for which to create the value
**Returns:** the

LongValue

for the given long.

---

#### mirrorOf

LongValue

mirrorOf​(long value)

Creates a

LongValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
FloatValue
mirrorOf​(float value)
```

Creates a

FloatValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a float for which to create the value
**Returns:** the

FloatValue

for the given float.

---

#### mirrorOf

FloatValue

mirrorOf​(float value)

Creates a

FloatValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
DoubleValue
mirrorOf​(double value)
```

Creates a

DoubleValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

**Parameters:** value

- a double for which to create the value
**Returns:** the

DoubleValue

for the given double.

---

#### mirrorOf

DoubleValue

mirrorOf​(double value)

Creates a

DoubleValue

for the given value. This value
can be used for setting and comparing against a value retrieved
from a variable or field in this virtual machine.

mirrorOf

```java
StringReference
mirrorOf​(
String
value)
```

Creates a string in this virtual machine.
The created string can be used for setting and comparing against
a string value retrieved from a variable or field in this
virtual machine.

**Parameters:** value

- the string to be created
**Returns:** a

StringReference

that mirrors the newly created
string in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

---

#### mirrorOf

StringReference

mirrorOf​(

String

value)

Creates a string in this virtual machine.
The created string can be used for setting and comparing against
a string value retrieved from a variable or field in this
virtual machine.

mirrorOfVoid

```java
VoidValue
mirrorOfVoid()
```

Creates a

VoidValue

. This value
can be passed to

ThreadReference.forceEarlyReturn(com.sun.jdi.Value)

when a void method is to be exited.

**Returns:** the

VoidValue

.

---

#### mirrorOfVoid

VoidValue

mirrorOfVoid()

Creates a

VoidValue

. This value
can be passed to

ThreadReference.forceEarlyReturn(com.sun.jdi.Value)

when a void method is to be exited.

process

```java
Process
process()
```

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

**Returns:** the

Process

object for this virtual
machine, or null if it was not launched by a

LaunchingConnector

.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only
-see

canBeModified()

.

---

#### process

Process

process()

Returns the

Process

object for this
virtual machine if launched by a

LaunchingConnector

dispose

```java
void dispose()
```

Invalidates this virtual machine mirror.
The communication channel to the target VM is closed, and
the target VM prepares to accept another subsequent connection
from this debugger or another debugger, including the
following tasks:

- All event requests are cancelled.

All threads suspended by

suspend()

or by

ThreadReference.suspend()

are resumed as many
times as necessary for them to run.

Garbage collection is re-enabled in all cases where it was
disabled through

ObjectReference.disableCollection()

.

Any current method invocations executing in the target VM
are continued after the disconnection. Upon completion of any such
method invocation, the invoking thread continues from the
location where it was originally stopped.

Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

---

#### dispose

void dispose()

Invalidates this virtual machine mirror.
The communication channel to the target VM is closed, and
the target VM prepares to accept another subsequent connection
from this debugger or another debugger, including the
following tasks:

- All event requests are cancelled.

All threads suspended by

suspend()

or by

ThreadReference.suspend()

are resumed as many
times as necessary for them to run.

Garbage collection is re-enabled in all cases where it was
disabled through

ObjectReference.disableCollection()

.

Any current method invocations executing in the target VM
are continued after the disconnection. Upon completion of any such
method invocation, the invoking thread continues from the
location where it was originally stopped.

Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

All event requests are cancelled.

All threads suspended by

suspend()

or by

ThreadReference.suspend()

are resumed as many
times as necessary for them to run.

Garbage collection is re-enabled in all cases where it was
disabled through

ObjectReference.disableCollection()

.

Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

exit

```java
void exit​(int exitCode)
```

Causes the mirrored VM to terminate with the given error code.
All resources associated with this VirtualMachine are freed.
If the mirrored VM is remote, the communication channel
to it will be closed. Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

Threads running in the mirrored VM are abruptly terminated.
A thread death exception is not thrown and
finally blocks are not run.

**Parameters:** exitCode

- the exit code for the target VM. On some platforms,
the exit code might be truncated, for example, to the lower order 8 bits.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

canBeModified()

.

---

#### exit

void exit​(int exitCode)

Causes the mirrored VM to terminate with the given error code.
All resources associated with this VirtualMachine are freed.
If the mirrored VM is remote, the communication channel
to it will be closed. Resources originating in
this VirtualMachine (ObjectReferences, ReferenceTypes, etc.)
will become invalid.

Threads running in the mirrored VM are abruptly terminated.
A thread death exception is not thrown and
finally blocks are not run.

Threads running in the mirrored VM are abruptly terminated.
A thread death exception is not thrown and
finally blocks are not run.

canWatchFieldModification

```java
boolean canWatchFieldModification()
```

Determines if the target VM supports watchpoints
for field modification.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canWatchFieldModification

boolean canWatchFieldModification()

Determines if the target VM supports watchpoints
for field modification.

canWatchFieldAccess

```java
boolean canWatchFieldAccess()
```

Determines if the target VM supports watchpoints
for field access.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canWatchFieldAccess

boolean canWatchFieldAccess()

Determines if the target VM supports watchpoints
for field access.

canGetBytecodes

```java
boolean canGetBytecodes()
```

Determines if the target VM supports the retrieval
of a method's bytecodes.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canGetBytecodes

boolean canGetBytecodes()

Determines if the target VM supports the retrieval
of a method's bytecodes.

canGetSyntheticAttribute

```java
boolean canGetSyntheticAttribute()
```

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canGetSyntheticAttribute

boolean canGetSyntheticAttribute()

Determines if the target VM supports the query
of the synthetic attribute of a method or field.

canGetOwnedMonitorInfo

```java
boolean canGetOwnedMonitorInfo()
```

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canGetOwnedMonitorInfo

boolean canGetOwnedMonitorInfo()

Determines if the target VM supports the retrieval
of the monitors owned by a thread.

canGetCurrentContendedMonitor

```java
boolean canGetCurrentContendedMonitor()
```

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canGetCurrentContendedMonitor

boolean canGetCurrentContendedMonitor()

Determines if the target VM supports the retrieval
of the monitor for which a thread is currently waiting.

canGetMonitorInfo

```java
boolean canGetMonitorInfo()
```

Determines if the target VM supports the retrieval
of the monitor information for an object.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canGetMonitorInfo

boolean canGetMonitorInfo()

Determines if the target VM supports the retrieval
of the monitor information for an object.

canUseInstanceFilters

```java
boolean canUseInstanceFilters()
```

Determines if the target VM supports filtering
events by specific instance object. For example,
see

BreakpointRequest.addInstanceFilter(com.sun.jdi.ObjectReference)

.

**Returns:** true

if the feature is supported,

false

otherwise.

---

#### canUseInstanceFilters

boolean canUseInstanceFilters()

Determines if the target VM supports filtering
events by specific instance object. For example,
see

BreakpointRequest.addInstanceFilter(com.sun.jdi.ObjectReference)

.

canRedefineClasses

```java
boolean canRedefineClasses()
```

Determines if the target VM supports any level
of class redefinition.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

---

#### canRedefineClasses

boolean canRedefineClasses()

Determines if the target VM supports any level
of class redefinition.

canAddMethod

```java
boolean canAddMethod()
```

Determines if the target VM supports the addition
of methods when performing class redefinition.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

---

#### canAddMethod

boolean canAddMethod()

Determines if the target VM supports the addition
of methods when performing class redefinition.

canUnrestrictedlyRedefineClasses

```java
boolean canUnrestrictedlyRedefineClasses()
```

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

---

#### canUnrestrictedlyRedefineClasses

boolean canUnrestrictedlyRedefineClasses()

Determines if the target VM supports
changes when performing class redefinition that are
otherwise restricted by

redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

.

canPopFrames

```java
boolean canPopFrames()
```

Determines if the target VM supports popping
frames of a threads stack.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** ThreadReference.popFrames(com.sun.jdi.StackFrame)

---

#### canPopFrames

boolean canPopFrames()

Determines if the target VM supports popping
frames of a threads stack.

canGetSourceDebugExtension

```java
boolean canGetSourceDebugExtension()
```

Determines if the target VM supports getting
the source debug extension.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** ReferenceType.sourceDebugExtension()

---

#### canGetSourceDebugExtension

boolean canGetSourceDebugExtension()

Determines if the target VM supports getting
the source debug extension.

canRequestVMDeathEvent

```java
boolean canRequestVMDeathEvent()
```

Determines if the target VM supports the creation of

VMDeathRequest

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.4
**See Also:** EventRequestManager.createVMDeathRequest()

---

#### canRequestVMDeathEvent

boolean canRequestVMDeathEvent()

Determines if the target VM supports the creation of

VMDeathRequest

s.

canGetMethodReturnValues

```java
boolean canGetMethodReturnValues()
```

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** EventRequestManager.createMethodExitRequest()

---

#### canGetMethodReturnValues

boolean canGetMethodReturnValues()

Determines if the target VM supports the inclusion of return values
in

MethodExitEvent

s.

canGetInstanceInfo

```java
boolean canGetInstanceInfo()
```

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** instanceCounts(java.util.List<? extends com.sun.jdi.ReferenceType>)

,

ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

---

#### canGetInstanceInfo

boolean canGetInstanceInfo()

Determines if the target VM supports the accessing of class instances,
instance counts, and referring objects.

canUseSourceNameFilters

```java
boolean canUseSourceNameFilters()
```

Determines if the target VM supports the filtering of
class prepare events by source name.

see

ClassPrepareRequest.addSourceNameFilter(java.lang.String)

.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6

---

#### canUseSourceNameFilters

boolean canUseSourceNameFilters()

Determines if the target VM supports the filtering of
class prepare events by source name.

see

ClassPrepareRequest.addSourceNameFilter(java.lang.String)

.

canForceEarlyReturn

```java
boolean canForceEarlyReturn()
```

Determines if the target VM supports the forcing of a method to
return early.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ThreadReference.forceEarlyReturn(Value)

---

#### canForceEarlyReturn

boolean canForceEarlyReturn()

Determines if the target VM supports the forcing of a method to
return early.

canBeModified

```java
boolean canBeModified()
```

Determines if the target VM is a read-only VM. If a method which
would modify the state of the VM is called on a read-only VM,
then

VMCannotBeModifiedException

is thrown.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.5

---

#### canBeModified

boolean canBeModified()

Determines if the target VM is a read-only VM. If a method which
would modify the state of the VM is called on a read-only VM,
then

VMCannotBeModifiedException

is thrown.

canRequestMonitorEvents

```java
boolean canRequestMonitorEvents()
```

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

MonitorContendedEnteredRequest

s.

MonitorWaitRequest

s.

MonitorWaitedRequest

s.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** EventRequestManager.createMonitorContendedEnterRequest()

,

EventRequestManager.createMonitorContendedEnteredRequest()

,

EventRequestManager.createMonitorWaitRequest()

,

EventRequestManager.createMonitorWaitedRequest()

---

#### canRequestMonitorEvents

boolean canRequestMonitorEvents()

Determines if the target VM supports the creation of

MonitorContendedEnterRequest

s.

MonitorContendedEnteredRequest

s.

MonitorWaitRequest

s.

MonitorWaitedRequest

s.

canGetMonitorFrameInfo

```java
boolean canGetMonitorFrameInfo()
```

Determines if the target VM supports getting which
frame has acquired a monitor.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ThreadReference.ownedMonitorsAndFrames()

---

#### canGetMonitorFrameInfo

boolean canGetMonitorFrameInfo()

Determines if the target VM supports getting which
frame has acquired a monitor.

canGetClassFileVersion

```java
boolean canGetClassFileVersion()
```

Determines if the target VM supports reading class file
major and minor versions.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ReferenceType.majorVersion()

,

ReferenceType.minorVersion()

---

#### canGetClassFileVersion

boolean canGetClassFileVersion()

Determines if the target VM supports reading class file
major and minor versions.

canGetConstantPool

```java
boolean canGetConstantPool()
```

Determines if the target VM supports getting constant pool
information of a class.

**Returns:** true

if the feature is supported,

false

otherwise.
**Since:** 1.6
**See Also:** ReferenceType.constantPoolCount()

,

ReferenceType.constantPool()

---

#### canGetConstantPool

boolean canGetConstantPool()

Determines if the target VM supports getting constant pool
information of a class.

canGetModuleInfo

```java
default boolean canGetModuleInfo()
```

Determines if the target VM supports getting information about modules.

**Implementation Requirements:** The default implementation returns

false

.
**Returns:** true

if the feature is supported,

false

otherwise
**Since:** 9
**See Also:** allModules()

,

ReferenceType.module()

,

ModuleReference

---

#### canGetModuleInfo

default boolean canGetModuleInfo()

Determines if the target VM supports getting information about modules.

setDefaultStratum

```java
void setDefaultStratum​(
String
stratum)
```

Set this VM's default stratum (see

Location

for a
discussion of strata). Overrides the per-class default set
in the class file.

Affects location queries (such as,

Location.sourceName()

)
and the line boundaries used in
single stepping.

**Parameters:** stratum

- the stratum to set as VM default,
or null to use per-class defaults.
**Throws:** UnsupportedOperationException

- if the
target virtual machine does not support this operation.
**Since:** 1.4

---

#### setDefaultStratum

void setDefaultStratum​(

String

stratum)

Set this VM's default stratum (see

Location

for a
discussion of strata). Overrides the per-class default set
in the class file.

Affects location queries (such as,

Location.sourceName()

)
and the line boundaries used in
single stepping.

Affects location queries (such as,

Location.sourceName()

)
and the line boundaries used in
single stepping.

getDefaultStratum

```java
String
getDefaultStratum()
```

Return this VM's default stratum.

**Returns:** null

(meaning that the per-class
default -

ReferenceType.defaultStratum()

-
should be used) unless the default stratum has been
set with

setDefaultStratum(String)

.
**Since:** 1.4
**See Also:** setDefaultStratum(String)

,

ReferenceType.defaultStratum()

---

#### getDefaultStratum

String

getDefaultStratum()

Return this VM's default stratum.

instanceCounts

```java
long[] instanceCounts​(
List
<? extends
ReferenceType
> refTypes)
```

Returns the number of instances of each ReferenceType in the 'refTypes'
list.
Only instances that are reachable for the purposes of garbage collection
are counted.

Not all target virtual machines support this operation.
Use

canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:** refTypes

- the list of

ReferenceType

objects for which counts
are to be obtained.
**Returns:** an array of

long

containing one element for each
element in the 'refTypes' list. Element i of the array contains
the number of instances in the target VM of the ReferenceType at
position i in the 'refTypes' list.
If the 'refTypes' list is empty, a zero-length array is returned.
If a ReferenceType in refTypes has been garbage collected, zero
is returned for its instance count.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
**Throws:** NullPointerException

- if the 'refTypes' list is null.
**Since:** 1.6
**See Also:** ReferenceType.instances(long)

,

ObjectReference.referringObjects(long)

---

#### instanceCounts

long[] instanceCounts​(

List

<? extends

ReferenceType

> refTypes)

Returns the number of instances of each ReferenceType in the 'refTypes'
list.
Only instances that are reachable for the purposes of garbage collection
are counted.

Not all target virtual machines support this operation.
Use

canGetInstanceInfo()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

canGetInstanceInfo()

to determine if the operation is supported.

description

```java
String
description()
```

Returns text information on the target VM and the
debugger support that mirrors it. No specific format
for this information is guaranteed.
Typically, this string contains version information for the
target VM and debugger interfaces.
More precise information
on VM and JDI versions is available through

version()

,

VirtualMachineManager.majorInterfaceVersion()

,
and

VirtualMachineManager.minorInterfaceVersion()

**Returns:** the description.

---

#### description

String

description()

Returns text information on the target VM and the
debugger support that mirrors it. No specific format
for this information is guaranteed.
Typically, this string contains version information for the
target VM and debugger interfaces.
More precise information
on VM and JDI versions is available through

version()

,

VirtualMachineManager.majorInterfaceVersion()

,
and

VirtualMachineManager.minorInterfaceVersion()

version

```java
String
version()
```

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.
For obtaining the JDI interface version, use

VirtualMachineManager.majorInterfaceVersion()

and

VirtualMachineManager.minorInterfaceVersion()

**Returns:** the target VM version.

---

#### version

String

version()

Returns the version of the Java Runtime Environment in the target
VM as reported by the property

java.version

.
For obtaining the JDI interface version, use

VirtualMachineManager.majorInterfaceVersion()

and

VirtualMachineManager.minorInterfaceVersion()

name

```java
String
name()
```

Returns the name of the target VM as reported by the
property

java.vm.name

.

**Returns:** the target VM name.

---

#### name

String

name()

Returns the name of the target VM as reported by the
property

java.vm.name

.

setDebugTraceMode

```java
void setDebugTraceMode​(int traceFlags)
```

Traces the activities performed by the com.sun.jdi implementation.
All trace information is output to System.err. The given trace
flags are used to limit the output to only the information
desired. The given flags are in effect and the corresponding
trace will continue until the next call to
this method.

Output is implementation dependent and trace mode may be ignored.

**Parameters:** traceFlags

- identifies which kinds of tracing to enable.

---

#### setDebugTraceMode

void setDebugTraceMode​(int traceFlags)

Traces the activities performed by the com.sun.jdi implementation.
All trace information is output to System.err. The given trace
flags are used to limit the output to only the information
desired. The given flags are in effect and the corresponding
trace will continue until the next call to
this method.

Output is implementation dependent and trace mode may be ignored.

Output is implementation dependent and trace mode may be ignored.

---

