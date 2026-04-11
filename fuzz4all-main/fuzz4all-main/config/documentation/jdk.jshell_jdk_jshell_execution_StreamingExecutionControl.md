# Class StreamingExecutionControl

**Source:** `jdk.jshell\jdk\jshell\execution\StreamingExecutionControl.html`

### Class Description

```java
public class
StreamingExecutionControl

extends
Object

implements
ExecutionControl
```

An implementation of the

ExecutionControl

execution engine SPI which streams requests to a remote agent where
execution takes place.

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

---

### Field Details

*No entries found.*

### Constructor Details

#### public StreamingExecutionControl​(
ObjectOutput
out,

ObjectInput
in)

Creates an instance.

**Parameters:**
- out

- the output for commands
- in

- the input for command responses

---

### Method Details

#### public void close()

Closes the execution engine. Send an exit command to the remote agent.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

ExecutionControl

---

### Additional Sections

#### Class StreamingExecutionControl

java.lang.Object

- jdk.jshell.execution.StreamingExecutionControl

jdk.jshell.execution.StreamingExecutionControl

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

**Direct Known Subclasses:** JdiExecutionControl

```java
public class
StreamingExecutionControl

extends
Object

implements
ExecutionControl
```

An implementation of the

ExecutionControl

execution engine SPI which streams requests to a remote agent where
execution takes place.

**Since:** 9

public class

StreamingExecutionControl

extends

Object

implements

ExecutionControl

An implementation of the

ExecutionControl

execution engine SPI which streams requests to a remote agent where
execution takes place.

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

Constructor

Description

StreamingExecutionControl

​(

ObjectOutput

out,

ObjectInput

in)

Creates an instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes the execution engine.

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

extensionCommand

,

invoke

,

load

,

redefine

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

Constructor

Description

StreamingExecutionControl

​(

ObjectOutput

out,

ObjectInput

in)

Creates an instance.

---

#### Constructor Summary

Creates an instance.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes the execution engine.

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

extensionCommand

,

invoke

,

load

,

redefine

,

stop

,

varValue

---

#### Method Summary

Closes the execution engine.

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

extensionCommand

,

invoke

,

load

,

redefine

,

stop

,

varValue

---

#### Methods declared in interface jdk.jshell.spi. ExecutionControl

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StreamingExecutionControl

```java
public StreamingExecutionControl​(
ObjectOutput
out,

ObjectInput
in)
```

Creates an instance.

**Parameters:** out

- the output for commands
**Parameters:** in

- the input for command responses

============ METHOD DETAIL ==========

- Method Detail

- close

```java
public void close()
```

Closes the execution engine. Send an exit command to the remote agent.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

ExecutionControl

Constructor Detail

- StreamingExecutionControl

```java
public StreamingExecutionControl​(
ObjectOutput
out,

ObjectInput
in)
```

Creates an instance.

**Parameters:** out

- the output for commands
**Parameters:** in

- the input for command responses

---

#### Constructor Detail

StreamingExecutionControl

```java
public StreamingExecutionControl​(
ObjectOutput
out,

ObjectInput
in)
```

Creates an instance.

**Parameters:** out

- the output for commands
**Parameters:** in

- the input for command responses

---

#### StreamingExecutionControl

public StreamingExecutionControl​(

ObjectOutput

out,

ObjectInput

in)

Creates an instance.

Method Detail

- close

```java
public void close()
```

Closes the execution engine. Send an exit command to the remote agent.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

ExecutionControl

---

#### Method Detail

close

```java
public void close()
```

Closes the execution engine. Send an exit command to the remote agent.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

ExecutionControl

---

#### close

public void close()

Closes the execution engine. Send an exit command to the remote agent.

---

