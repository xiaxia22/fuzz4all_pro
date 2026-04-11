# Class JdiExecutionControl

**Source:** `jdk.jshell\jdk\jshell\execution\JdiExecutionControl.html`

### Class Description

```java
public abstract class
JdiExecutionControl

extends
StreamingExecutionControl

implements
ExecutionControl
```

Abstract JDI implementation of

ExecutionControl

.

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

---

### Field Details

*No entries found.*

### Constructor Details

#### protected JdiExecutionControl​(
ObjectOutput
out,

ObjectInput
in)

Create an instance.

**Parameters:**
- out

- the output from the remote agent
- in

- the input to the remote agent

---

### Method Details

#### protected abstract
VirtualMachine
vm()
throws
ExecutionControl.EngineTerminationException

Returns the JDI

VirtualMachine

instance.

**Returns:**
- the virtual machine

**Throws:**
- ExecutionControl.EngineTerminationException

- if the VM is dead/disconnected

---

#### public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.EngineTerminationException

Redefine the specified classes. Where 'redefine' is, as in JDI and JVMTI,
an in-place replacement of the classes (preserving class identity) --
that is, existing references to the class do not need to be recompiled.
This implementation uses JDI

VirtualMachine.redefineClasses(java.util.Map)

.
It will be unsuccessful if
the signature of the class has changed (see the JDI spec). The
JShell-core is designed to adapt to unsuccessful redefine.

**Specified by:**
- redefine

in interface

ExecutionControl

**Parameters:**
- cbcs

- the class name and bytecodes to redefine

**Throws:**
- ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
- ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### protected
ReferenceType
referenceType​(
VirtualMachine
vm,

String
name)

Returns the JDI

ReferenceType

corresponding to the specified
class name.

**Parameters:**
- vm

- the current JDI

VirtualMachine

as returned by

vm()
- name

- the class name to look-up

**Returns:**
- the corresponding

ReferenceType

---

### Additional Sections

#### Class JdiExecutionControl

java.lang.Object

- jdk.jshell.execution.StreamingExecutionControl
- - jdk.jshell.execution.JdiExecutionControl

jdk.jshell.execution.StreamingExecutionControl

- jdk.jshell.execution.JdiExecutionControl

jdk.jshell.execution.JdiExecutionControl

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

**Direct Known Subclasses:** JdiDefaultExecutionControl

```java
public abstract class
JdiExecutionControl

extends
StreamingExecutionControl

implements
ExecutionControl
```

Abstract JDI implementation of

ExecutionControl

.

**Since:** 9

public abstract class

JdiExecutionControl

extends

StreamingExecutionControl

implements

ExecutionControl

Abstract JDI implementation of

ExecutionControl

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface jdk.jshell.spi.

ExecutionControl

ExecutionControl.ClassBytecodes

,

ExecutionControl.ClassInstallException

,

ExecutionControl.EngineTerminationException

,

ExecutionControl.ExecutionControlException

,

ExecutionControl.InternalException

,

ExecutionControl.NotImplementedException

,

ExecutionControl.ResolutionException

,

ExecutionControl.RunException

,

ExecutionControl.StoppedException

,

ExecutionControl.UserException

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JdiExecutionControl

​(

ObjectOutput

out,

ObjectInput

in)

Create an instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

redefine

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Redefine the specified classes.

protected

ReferenceType

referenceType

​(

VirtualMachine

vm,

String

name)

Returns the JDI

ReferenceType

corresponding to the specified
class name.

protected abstract

VirtualMachine

vm

()

Returns the JDI

VirtualMachine

instance.

- Methods declared in class jdk.jshell.execution.

StreamingExecutionControl

close

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface jdk.jshell.spi.

ExecutionControl

addToClasspath

,

close

,

extensionCommand

,

invoke

,

load

,

stop

,

varValue

Nested Class Summary

- Nested classes/interfaces declared in interface jdk.jshell.spi.

ExecutionControl

ExecutionControl.ClassBytecodes

,

ExecutionControl.ClassInstallException

,

ExecutionControl.EngineTerminationException

,

ExecutionControl.ExecutionControlException

,

ExecutionControl.InternalException

,

ExecutionControl.NotImplementedException

,

ExecutionControl.ResolutionException

,

ExecutionControl.RunException

,

ExecutionControl.StoppedException

,

ExecutionControl.UserException

---

#### Nested Class Summary

Nested classes/interfaces declared in interface jdk.jshell.spi.

ExecutionControl

ExecutionControl.ClassBytecodes

,

ExecutionControl.ClassInstallException

,

ExecutionControl.EngineTerminationException

,

ExecutionControl.ExecutionControlException

,

ExecutionControl.InternalException

,

ExecutionControl.NotImplementedException

,

ExecutionControl.ResolutionException

,

ExecutionControl.RunException

,

ExecutionControl.StoppedException

,

ExecutionControl.UserException

---

#### Nested classes/interfaces declared in interface jdk.jshell.spi. ExecutionControl

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JdiExecutionControl

​(

ObjectOutput

out,

ObjectInput

in)

Create an instance.

---

#### Constructor Summary

Create an instance.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

redefine

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Redefine the specified classes.

protected

ReferenceType

referenceType

​(

VirtualMachine

vm,

String

name)

Returns the JDI

ReferenceType

corresponding to the specified
class name.

protected abstract

VirtualMachine

vm

()

Returns the JDI

VirtualMachine

instance.

- Methods declared in class jdk.jshell.execution.

StreamingExecutionControl

close

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface jdk.jshell.spi.

ExecutionControl

addToClasspath

,

close

,

extensionCommand

,

invoke

,

load

,

stop

,

varValue

---

#### Method Summary

Redefine the specified classes.

Returns the JDI

ReferenceType

corresponding to the specified
class name.

Returns the JDI

VirtualMachine

instance.

Methods declared in class jdk.jshell.execution.

StreamingExecutionControl

close

---

#### Methods declared in class jdk.jshell.execution. StreamingExecutionControl

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface jdk.jshell.spi.

ExecutionControl

addToClasspath

,

close

,

extensionCommand

,

invoke

,

load

,

stop

,

varValue

---

#### Methods declared in interface jdk.jshell.spi. ExecutionControl

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JdiExecutionControl

```java
protected JdiExecutionControl​(
ObjectOutput
out,

ObjectInput
in)
```

Create an instance.

**Parameters:** out

- the output from the remote agent
**Parameters:** in

- the input to the remote agent

============ METHOD DETAIL ==========

- Method Detail

- vm

```java
protected abstract
VirtualMachine
vm()
throws
ExecutionControl.EngineTerminationException
```

Returns the JDI

VirtualMachine

instance.

**Returns:** the virtual machine
**Throws:** ExecutionControl.EngineTerminationException

- if the VM is dead/disconnected

- redefine

```java
public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.EngineTerminationException
```

Redefine the specified classes. Where 'redefine' is, as in JDI and JVMTI,
an in-place replacement of the classes (preserving class identity) --
that is, existing references to the class do not need to be recompiled.
This implementation uses JDI

VirtualMachine.redefineClasses(java.util.Map)

.
It will be unsuccessful if
the signature of the class has changed (see the JDI spec). The
JShell-core is designed to adapt to unsuccessful redefine.

**Specified by:** redefine

in interface

ExecutionControl
**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- referenceType

```java
protected
ReferenceType
referenceType​(
VirtualMachine
vm,

String
name)
```

Returns the JDI

ReferenceType

corresponding to the specified
class name.

**Parameters:** vm

- the current JDI

VirtualMachine

as returned by

vm()
**Parameters:** name

- the class name to look-up
**Returns:** the corresponding

ReferenceType

Constructor Detail

- JdiExecutionControl

```java
protected JdiExecutionControl​(
ObjectOutput
out,

ObjectInput
in)
```

Create an instance.

**Parameters:** out

- the output from the remote agent
**Parameters:** in

- the input to the remote agent

---

#### Constructor Detail

JdiExecutionControl

```java
protected JdiExecutionControl​(
ObjectOutput
out,

ObjectInput
in)
```

Create an instance.

**Parameters:** out

- the output from the remote agent
**Parameters:** in

- the input to the remote agent

---

#### JdiExecutionControl

protected JdiExecutionControl​(

ObjectOutput

out,

ObjectInput

in)

Create an instance.

Method Detail

- vm

```java
protected abstract
VirtualMachine
vm()
throws
ExecutionControl.EngineTerminationException
```

Returns the JDI

VirtualMachine

instance.

**Returns:** the virtual machine
**Throws:** ExecutionControl.EngineTerminationException

- if the VM is dead/disconnected

- redefine

```java
public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.EngineTerminationException
```

Redefine the specified classes. Where 'redefine' is, as in JDI and JVMTI,
an in-place replacement of the classes (preserving class identity) --
that is, existing references to the class do not need to be recompiled.
This implementation uses JDI

VirtualMachine.redefineClasses(java.util.Map)

.
It will be unsuccessful if
the signature of the class has changed (see the JDI spec). The
JShell-core is designed to adapt to unsuccessful redefine.

**Specified by:** redefine

in interface

ExecutionControl
**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- referenceType

```java
protected
ReferenceType
referenceType​(
VirtualMachine
vm,

String
name)
```

Returns the JDI

ReferenceType

corresponding to the specified
class name.

**Parameters:** vm

- the current JDI

VirtualMachine

as returned by

vm()
**Parameters:** name

- the class name to look-up
**Returns:** the corresponding

ReferenceType

---

#### Method Detail

vm

```java
protected abstract
VirtualMachine
vm()
throws
ExecutionControl.EngineTerminationException
```

Returns the JDI

VirtualMachine

instance.

**Returns:** the virtual machine
**Throws:** ExecutionControl.EngineTerminationException

- if the VM is dead/disconnected

---

#### vm

protected abstract

VirtualMachine

vm()
throws

ExecutionControl.EngineTerminationException

Returns the JDI

VirtualMachine

instance.

redefine

```java
public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.EngineTerminationException
```

Redefine the specified classes. Where 'redefine' is, as in JDI and JVMTI,
an in-place replacement of the classes (preserving class identity) --
that is, existing references to the class do not need to be recompiled.
This implementation uses JDI

VirtualMachine.redefineClasses(java.util.Map)

.
It will be unsuccessful if
the signature of the class has changed (see the JDI spec). The
JShell-core is designed to adapt to unsuccessful redefine.

**Specified by:** redefine

in interface

ExecutionControl
**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### redefine

public void redefine​(

ExecutionControl.ClassBytecodes

[] cbcs)
throws

ExecutionControl.ClassInstallException

,

ExecutionControl.EngineTerminationException

Redefine the specified classes. Where 'redefine' is, as in JDI and JVMTI,
an in-place replacement of the classes (preserving class identity) --
that is, existing references to the class do not need to be recompiled.
This implementation uses JDI

VirtualMachine.redefineClasses(java.util.Map)

.
It will be unsuccessful if
the signature of the class has changed (see the JDI spec). The
JShell-core is designed to adapt to unsuccessful redefine.

referenceType

```java
protected
ReferenceType
referenceType​(
VirtualMachine
vm,

String
name)
```

Returns the JDI

ReferenceType

corresponding to the specified
class name.

**Parameters:** vm

- the current JDI

VirtualMachine

as returned by

vm()
**Parameters:** name

- the class name to look-up
**Returns:** the corresponding

ReferenceType

---

#### referenceType

protected

ReferenceType

referenceType​(

VirtualMachine

vm,

String

name)

Returns the JDI

ReferenceType

corresponding to the specified
class name.

---

