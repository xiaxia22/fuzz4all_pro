# Class RemoteExecutionControl

**Source:** `jdk.jshell\jdk\jshell\execution\RemoteExecutionControl.html`

### Class Description

```java
public class
RemoteExecutionControl

extends
DirectExecutionControl

implements
ExecutionControl
```

The remote agent runs in the execution process (separate from the main JShell
process). This agent loads code over a socket from the main JShell process,
executes the code, and other misc, Specialization of

DirectExecutionControl

which adds stop support controlled by
an external process. Designed to work with

JdiDefaultExecutionControl

.

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

---

### Field Details

*No entries found.*

### Constructor Details

#### public RemoteExecutionControl​(
LoaderDelegate
loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:**
- loaderDelegate

- the delegate to handle loading classes

---

#### public RemoteExecutionControl()

Create an instance using the default class loading.

---

### Method Details

#### public static void main​(
String
[] args)
throws
Exception

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

**Parameters:**
- args

- standard command-line arguments, expectation is the socket
number is the only argument

**Throws:**
- Exception

- any unexpected exception

---

#### public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException

Redefine processing on the remote end is only to register the redefined classes

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
- ExecutionControl.NotImplementedException

- if not implemented
- ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

### Additional Sections

#### Class RemoteExecutionControl

java.lang.Object

- jdk.jshell.execution.DirectExecutionControl
- - jdk.jshell.execution.RemoteExecutionControl

jdk.jshell.execution.DirectExecutionControl

- jdk.jshell.execution.RemoteExecutionControl

jdk.jshell.execution.RemoteExecutionControl

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

```java
public class
RemoteExecutionControl

extends
DirectExecutionControl

implements
ExecutionControl
```

The remote agent runs in the execution process (separate from the main JShell
process). This agent loads code over a socket from the main JShell process,
executes the code, and other misc, Specialization of

DirectExecutionControl

which adds stop support controlled by
an external process. Designed to work with

JdiDefaultExecutionControl

.

**Since:** 9

public class

RemoteExecutionControl

extends

DirectExecutionControl

implements

ExecutionControl

The remote agent runs in the execution process (separate from the main JShell
process). This agent loads code over a socket from the main JShell process,
executes the code, and other misc, Specialization of

DirectExecutionControl

which adds stop support controlled by
an external process. Designed to work with

JdiDefaultExecutionControl

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

Constructor

Description

RemoteExecutionControl

()

Create an instance using the default class loading.

RemoteExecutionControl

​(

LoaderDelegate

loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static void

main

​(

String

[] args)

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

void

redefine

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Redefine processing on the remote end is only to register the redefined classes

- Methods declared in class jdk.jshell.execution.

DirectExecutionControl

classesRedefined

,

clientCodeEnter

,

clientCodeLeave

,

findClass

,

invoke

,

stop

,

throwConvertedInvocationException

,

throwConvertedOtherException

,

valueString

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

Constructor

Description

RemoteExecutionControl

()

Create an instance using the default class loading.

RemoteExecutionControl

​(

LoaderDelegate

loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

---

#### Constructor Summary

Create an instance using the default class loading.

Creates an instance, delegating loader operations to the specified
delegate.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static void

main

​(

String

[] args)

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

void

redefine

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Redefine processing on the remote end is only to register the redefined classes

- Methods declared in class jdk.jshell.execution.

DirectExecutionControl

classesRedefined

,

clientCodeEnter

,

clientCodeLeave

,

findClass

,

invoke

,

stop

,

throwConvertedInvocationException

,

throwConvertedOtherException

,

valueString

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

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

Redefine processing on the remote end is only to register the redefined classes

Methods declared in class jdk.jshell.execution.

DirectExecutionControl

classesRedefined

,

clientCodeEnter

,

clientCodeLeave

,

findClass

,

invoke

,

stop

,

throwConvertedInvocationException

,

throwConvertedOtherException

,

valueString

---

#### Methods declared in class jdk.jshell.execution. DirectExecutionControl

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

- RemoteExecutionControl

```java
public RemoteExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

- RemoteExecutionControl

```java
public RemoteExecutionControl()
```

Create an instance using the default class loading.

============ METHOD DETAIL ==========

- Method Detail

- main

```java
public static void main​(
String
[] args)
throws
Exception
```

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

**Parameters:** args

- standard command-line arguments, expectation is the socket
number is the only argument
**Throws:** Exception

- any unexpected exception

- redefine

```java
public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Redefine processing on the remote end is only to register the redefined classes

**Specified by:** redefine

in interface

ExecutionControl
**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

Constructor Detail

- RemoteExecutionControl

```java
public RemoteExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

- RemoteExecutionControl

```java
public RemoteExecutionControl()
```

Create an instance using the default class loading.

---

#### Constructor Detail

RemoteExecutionControl

```java
public RemoteExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

---

#### RemoteExecutionControl

public RemoteExecutionControl​(

LoaderDelegate

loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

RemoteExecutionControl

```java
public RemoteExecutionControl()
```

Create an instance using the default class loading.

---

#### RemoteExecutionControl

public RemoteExecutionControl()

Create an instance using the default class loading.

Method Detail

- main

```java
public static void main​(
String
[] args)
throws
Exception
```

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

**Parameters:** args

- standard command-line arguments, expectation is the socket
number is the only argument
**Throws:** Exception

- any unexpected exception

- redefine

```java
public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Redefine processing on the remote end is only to register the redefined classes

**Specified by:** redefine

in interface

ExecutionControl
**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### Method Detail

main

```java
public static void main​(
String
[] args)
throws
Exception
```

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

**Parameters:** args

- standard command-line arguments, expectation is the socket
number is the only argument
**Throws:** Exception

- any unexpected exception

---

#### main

public static void main​(

String

[] args)
throws

Exception

Launch the agent, connecting to the JShell-core over the socket specified
in the command-line argument.

redefine

```java
public void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Redefine processing on the remote end is only to register the redefined classes

**Specified by:** redefine

in interface

ExecutionControl
**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
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

ExecutionControl.NotImplementedException

,

ExecutionControl.EngineTerminationException

Redefine processing on the remote end is only to register the redefined classes

---

