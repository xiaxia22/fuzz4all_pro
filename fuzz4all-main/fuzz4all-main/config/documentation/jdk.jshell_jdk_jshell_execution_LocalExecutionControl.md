# Class LocalExecutionControl

**Source:** `jdk.jshell\jdk\jshell\execution\LocalExecutionControl.html`

### Class Description

```java
public class
LocalExecutionControl

extends
DirectExecutionControl
```

An implementation of

ExecutionControl

which executes
in the same JVM as the JShell-core.

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

---

### Field Details

*No entries found.*

### Constructor Details

#### public LocalExecutionControl​(
LoaderDelegate
loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:**
- loaderDelegate

- the delegate to handle loading classes

---

#### public LocalExecutionControl()

Create an instance using the default class loading.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class LocalExecutionControl

java.lang.Object

- jdk.jshell.execution.DirectExecutionControl
- - jdk.jshell.execution.LocalExecutionControl

jdk.jshell.execution.DirectExecutionControl

- jdk.jshell.execution.LocalExecutionControl

jdk.jshell.execution.LocalExecutionControl

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

```java
public class
LocalExecutionControl

extends
DirectExecutionControl
```

An implementation of

ExecutionControl

which executes
in the same JVM as the JShell-core.

**Since:** 9

public class

LocalExecutionControl

extends

DirectExecutionControl

An implementation of

ExecutionControl

which executes
in the same JVM as the JShell-core.

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

LocalExecutionControl

()

Create an instance using the default class loading.

LocalExecutionControl

​(

LoaderDelegate

loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

========== METHOD SUMMARY ===========

- Method Summary

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

redefine

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

LocalExecutionControl

()

Create an instance using the default class loading.

LocalExecutionControl

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

redefine

,

varValue

---

#### Method Summary

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

redefine

,

varValue

---

#### Methods declared in interface jdk.jshell.spi. ExecutionControl

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LocalExecutionControl

```java
public LocalExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

- LocalExecutionControl

```java
public LocalExecutionControl()
```

Create an instance using the default class loading.

Constructor Detail

- LocalExecutionControl

```java
public LocalExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

- LocalExecutionControl

```java
public LocalExecutionControl()
```

Create an instance using the default class loading.

---

#### Constructor Detail

LocalExecutionControl

```java
public LocalExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

---

#### LocalExecutionControl

public LocalExecutionControl​(

LoaderDelegate

loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

LocalExecutionControl

```java
public LocalExecutionControl()
```

Create an instance using the default class loading.

---

#### LocalExecutionControl

public LocalExecutionControl()

Create an instance using the default class loading.

---

