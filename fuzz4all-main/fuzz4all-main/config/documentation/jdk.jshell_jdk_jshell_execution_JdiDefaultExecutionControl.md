# Class JdiDefaultExecutionControl

**Source:** `jdk.jshell\jdk\jshell\execution\JdiDefaultExecutionControl.html`

### Class Description

```java
public class
JdiDefaultExecutionControl

extends
JdiExecutionControl
```

The implementation of

ExecutionControl

that the
JShell-core uses by default.
Launches a remote process -- the "remote agent".
Interfaces to the remote agent over a socket and via JDI.
Designed to work with

RemoteExecutionControl

.

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

**Throws:**
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.InternalException

- an internal problem occurred

---

### Additional Sections

#### Class JdiDefaultExecutionControl

java.lang.Object

- jdk.jshell.execution.StreamingExecutionControl
- - jdk.jshell.execution.JdiExecutionControl
- - jdk.jshell.execution.JdiDefaultExecutionControl

jdk.jshell.execution.StreamingExecutionControl

- jdk.jshell.execution.JdiExecutionControl
- - jdk.jshell.execution.JdiDefaultExecutionControl

jdk.jshell.execution.JdiExecutionControl

- jdk.jshell.execution.JdiDefaultExecutionControl

jdk.jshell.execution.JdiDefaultExecutionControl

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

```java
public class
JdiDefaultExecutionControl

extends
JdiExecutionControl
```

The implementation of

ExecutionControl

that the
JShell-core uses by default.
Launches a remote process -- the "remote agent".
Interfaces to the remote agent over a socket and via JDI.
Designed to work with

RemoteExecutionControl

.

**Since:** 9

public class

JdiDefaultExecutionControl

extends

JdiExecutionControl

The implementation of

ExecutionControl

that the
JShell-core uses by default.
Launches a remote process -- the "remote agent".
Interfaces to the remote agent over a socket and via JDI.
Designed to work with

RemoteExecutionControl

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

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

stop

()

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

- Methods declared in class jdk.jshell.execution.

JdiExecutionControl

redefine

,

referenceType

,

vm

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

stop

()

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

- Methods declared in class jdk.jshell.execution.

JdiExecutionControl

redefine

,

referenceType

,

vm

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

varValue

---

#### Method Summary

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

Methods declared in class jdk.jshell.execution.

JdiExecutionControl

redefine

,

referenceType

,

vm

---

#### Methods declared in class jdk.jshell.execution. JdiExecutionControl

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

varValue

---

#### Methods declared in interface jdk.jshell.spi. ExecutionControl

============ METHOD DETAIL ==========

- Method Detail

- stop

```java
public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

Method Detail

- stop

```java
public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

---

#### Method Detail

stop

```java
public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

---

#### stop

public void stop()
throws

ExecutionControl.EngineTerminationException

,

ExecutionControl.InternalException

Interrupts a running remote invoke by manipulating remote variables
and sending a stop via JDI.

---

