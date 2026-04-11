# Class DirectExecutionControl

**Source:** `jdk.jshell\jdk\jshell\execution\DirectExecutionControl.html`

### Class Description

```java
public class
DirectExecutionControl

extends
Object

implements
ExecutionControl
```

An

ExecutionControl

implementation that runs in the current process.
May be used directly, or over a channel with

Util.forwardExecutionControl(ExecutionControl, java.io.ObjectInput, java.io.ObjectOutput)

.

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

---

### Field Details

*No entries found.*

### Constructor Details

#### public DirectExecutionControl​(
LoaderDelegate
loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:**
- loaderDelegate

- the delegate to handle loading classes

---

#### public DirectExecutionControl()

Create an instance using the default class loading.

---

### Method Details

#### protected void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException

Notify that classes have been redefined.

**Parameters:**
- cbcs

- the class name and bytecodes to redefine

**Throws:**
- ExecutionControl.NotImplementedException

- if not implemented
- ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Interrupts a running invoke.

Not supported.

**Specified by:**
- stop

in interface

ExecutionControl

**Throws:**
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.InternalException

- an internal problem occurred

---

#### protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException

Finds the class with the specified binary name.

**Parameters:**
- name

- the binary name of the class

**Returns:**
- the Class Object

**Throws:**
- ClassNotFoundException

- if the class could not be found

---

#### protected
String
invoke​(
Method
doitMethod)
throws
Exception

Invoke the specified "doit-method", a static method with no parameters.
The

ExecutionControl.invoke(java.lang.String, java.lang.String)

in this class will call this to invoke.

**Parameters:**
- doitMethod

- the Method to invoke

**Returns:**
- the value or null

**Throws:**
- Exception

- any exceptions thrown by

Method.invoke(Object, Object...)

or any

ExecutionControl.ExecutionControlException

to pass-through.

---

#### protected static
String
valueString​(
Object
value)

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

**Parameters:**
- value

- the value to convert

**Returns:**
- the

String

representation

---

#### protected
String
throwConvertedInvocationException​(
Throwable
cause)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:**
- cause

- the exception to convert

**Returns:**
- never returns as it always throws

**Throws:**
- ExecutionControl.RunException

- for normal exception occurrences
- ExecutionControl.InternalException

- for internal problems

---

#### protected
String
throwConvertedOtherException​(
Throwable
ex)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:**
- ex

- the exception to convert

**Returns:**
- never returns as it always throws

**Throws:**
- ExecutionControl.RunException

- for normal exception occurrences
- ExecutionControl.InternalException

- for internal problems

---

#### protected void clientCodeEnter()
throws
ExecutionControl.InternalException

Marks entry into user code.

**Throws:**
- ExecutionControl.InternalException

- in unexpected failure cases

---

#### protected void clientCodeLeave()
throws
ExecutionControl.InternalException

Marks departure from user code.

**Throws:**
- ExecutionControl.InternalException

- in unexpected failure cases

---

### Additional Sections

#### Class DirectExecutionControl

java.lang.Object

- jdk.jshell.execution.DirectExecutionControl

jdk.jshell.execution.DirectExecutionControl

**All Implemented Interfaces:** AutoCloseable

,

ExecutionControl

**Direct Known Subclasses:** LocalExecutionControl

,

RemoteExecutionControl

```java
public class
DirectExecutionControl

extends
Object

implements
ExecutionControl
```

An

ExecutionControl

implementation that runs in the current process.
May be used directly, or over a channel with

Util.forwardExecutionControl(ExecutionControl, java.io.ObjectInput, java.io.ObjectOutput)

.

**Since:** 9

public class

DirectExecutionControl

extends

Object

implements

ExecutionControl

An

ExecutionControl

implementation that runs in the current process.
May be used directly, or over a channel with

Util.forwardExecutionControl(ExecutionControl, java.io.ObjectInput, java.io.ObjectOutput)

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

DirectExecutionControl

()

Create an instance using the default class loading.

DirectExecutionControl

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

protected void

classesRedefined

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Notify that classes have been redefined.

protected void

clientCodeEnter

()

Marks entry into user code.

protected void

clientCodeLeave

()

Marks departure from user code.

protected

Class

<?>

findClass

​(

String

name)

Finds the class with the specified binary name.

protected

String

invoke

​(

Method

doitMethod)

Invoke the specified "doit-method", a static method with no parameters.

void

stop

()

Interrupts a running invoke.

protected

String

throwConvertedInvocationException

​(

Throwable

cause)

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

protected

String

throwConvertedOtherException

​(

Throwable

ex)

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

protected static

String

valueString

​(

Object

value)

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

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

DirectExecutionControl

()

Create an instance using the default class loading.

DirectExecutionControl

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

protected void

classesRedefined

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Notify that classes have been redefined.

protected void

clientCodeEnter

()

Marks entry into user code.

protected void

clientCodeLeave

()

Marks departure from user code.

protected

Class

<?>

findClass

​(

String

name)

Finds the class with the specified binary name.

protected

String

invoke

​(

Method

doitMethod)

Invoke the specified "doit-method", a static method with no parameters.

void

stop

()

Interrupts a running invoke.

protected

String

throwConvertedInvocationException

​(

Throwable

cause)

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

protected

String

throwConvertedOtherException

​(

Throwable

ex)

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

protected static

String

valueString

​(

Object

value)

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

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

Notify that classes have been redefined.

Marks entry into user code.

Marks departure from user code.

Finds the class with the specified binary name.

Invoke the specified "doit-method", a static method with no parameters.

Interrupts a running invoke.

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

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

- DirectExecutionControl

```java
public DirectExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

- DirectExecutionControl

```java
public DirectExecutionControl()
```

Create an instance using the default class loading.

============ METHOD DETAIL ==========

- Method Detail

- classesRedefined

```java
protected void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Notify that classes have been redefined.

**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- stop

```java
public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running invoke.

Not supported.

**Specified by:** stop

in interface

ExecutionControl
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- findClass

```java
protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

Finds the class with the specified binary name.

**Parameters:** name

- the binary name of the class
**Returns:** the Class Object
**Throws:** ClassNotFoundException

- if the class could not be found

- invoke

```java
protected
String
invoke​(
Method
doitMethod)
throws
Exception
```

Invoke the specified "doit-method", a static method with no parameters.
The

ExecutionControl.invoke(java.lang.String, java.lang.String)

in this class will call this to invoke.

**Parameters:** doitMethod

- the Method to invoke
**Returns:** the value or null
**Throws:** Exception

- any exceptions thrown by

Method.invoke(Object, Object...)

or any

ExecutionControl.ExecutionControlException

to pass-through.

- valueString

```java
protected static
String
valueString​(
Object
value)
```

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

**Parameters:** value

- the value to convert
**Returns:** the

String

representation

- throwConvertedInvocationException

```java
protected
String
throwConvertedInvocationException​(
Throwable
cause)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException
```

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:** cause

- the exception to convert
**Returns:** never returns as it always throws
**Throws:** ExecutionControl.RunException

- for normal exception occurrences
**Throws:** ExecutionControl.InternalException

- for internal problems

- throwConvertedOtherException

```java
protected
String
throwConvertedOtherException​(
Throwable
ex)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException
```

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:** ex

- the exception to convert
**Returns:** never returns as it always throws
**Throws:** ExecutionControl.RunException

- for normal exception occurrences
**Throws:** ExecutionControl.InternalException

- for internal problems

- clientCodeEnter

```java
protected void clientCodeEnter()
throws
ExecutionControl.InternalException
```

Marks entry into user code.

**Throws:** ExecutionControl.InternalException

- in unexpected failure cases

- clientCodeLeave

```java
protected void clientCodeLeave()
throws
ExecutionControl.InternalException
```

Marks departure from user code.

**Throws:** ExecutionControl.InternalException

- in unexpected failure cases

Constructor Detail

- DirectExecutionControl

```java
public DirectExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

- DirectExecutionControl

```java
public DirectExecutionControl()
```

Create an instance using the default class loading.

---

#### Constructor Detail

DirectExecutionControl

```java
public DirectExecutionControl​(
LoaderDelegate
loaderDelegate)
```

Creates an instance, delegating loader operations to the specified
delegate.

**Parameters:** loaderDelegate

- the delegate to handle loading classes

---

#### DirectExecutionControl

public DirectExecutionControl​(

LoaderDelegate

loaderDelegate)

Creates an instance, delegating loader operations to the specified
delegate.

DirectExecutionControl

```java
public DirectExecutionControl()
```

Create an instance using the default class loading.

---

#### DirectExecutionControl

public DirectExecutionControl()

Create an instance using the default class loading.

Method Detail

- classesRedefined

```java
protected void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Notify that classes have been redefined.

**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- stop

```java
public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running invoke.

Not supported.

**Specified by:** stop

in interface

ExecutionControl
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- findClass

```java
protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

Finds the class with the specified binary name.

**Parameters:** name

- the binary name of the class
**Returns:** the Class Object
**Throws:** ClassNotFoundException

- if the class could not be found

- invoke

```java
protected
String
invoke​(
Method
doitMethod)
throws
Exception
```

Invoke the specified "doit-method", a static method with no parameters.
The

ExecutionControl.invoke(java.lang.String, java.lang.String)

in this class will call this to invoke.

**Parameters:** doitMethod

- the Method to invoke
**Returns:** the value or null
**Throws:** Exception

- any exceptions thrown by

Method.invoke(Object, Object...)

or any

ExecutionControl.ExecutionControlException

to pass-through.

- valueString

```java
protected static
String
valueString​(
Object
value)
```

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

**Parameters:** value

- the value to convert
**Returns:** the

String

representation

- throwConvertedInvocationException

```java
protected
String
throwConvertedInvocationException​(
Throwable
cause)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException
```

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:** cause

- the exception to convert
**Returns:** never returns as it always throws
**Throws:** ExecutionControl.RunException

- for normal exception occurrences
**Throws:** ExecutionControl.InternalException

- for internal problems

- throwConvertedOtherException

```java
protected
String
throwConvertedOtherException​(
Throwable
ex)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException
```

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:** ex

- the exception to convert
**Returns:** never returns as it always throws
**Throws:** ExecutionControl.RunException

- for normal exception occurrences
**Throws:** ExecutionControl.InternalException

- for internal problems

- clientCodeEnter

```java
protected void clientCodeEnter()
throws
ExecutionControl.InternalException
```

Marks entry into user code.

**Throws:** ExecutionControl.InternalException

- in unexpected failure cases

- clientCodeLeave

```java
protected void clientCodeLeave()
throws
ExecutionControl.InternalException
```

Marks departure from user code.

**Throws:** ExecutionControl.InternalException

- in unexpected failure cases

---

#### Method Detail

classesRedefined

```java
protected void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Notify that classes have been redefined.

**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### classesRedefined

protected void classesRedefined​(

ExecutionControl.ClassBytecodes

[] cbcs)
throws

ExecutionControl.NotImplementedException

,

ExecutionControl.EngineTerminationException

Notify that classes have been redefined.

stop

```java
public void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running invoke.

Not supported.

**Specified by:** stop

in interface

ExecutionControl
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

Interrupts a running invoke.

Not supported.

Not supported.

findClass

```java
protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

Finds the class with the specified binary name.

**Parameters:** name

- the binary name of the class
**Returns:** the Class Object
**Throws:** ClassNotFoundException

- if the class could not be found

---

#### findClass

protected

Class

<?> findClass​(

String

name)
throws

ClassNotFoundException

Finds the class with the specified binary name.

invoke

```java
protected
String
invoke​(
Method
doitMethod)
throws
Exception
```

Invoke the specified "doit-method", a static method with no parameters.
The

ExecutionControl.invoke(java.lang.String, java.lang.String)

in this class will call this to invoke.

**Parameters:** doitMethod

- the Method to invoke
**Returns:** the value or null
**Throws:** Exception

- any exceptions thrown by

Method.invoke(Object, Object...)

or any

ExecutionControl.ExecutionControlException

to pass-through.

---

#### invoke

protected

String

invoke​(

Method

doitMethod)
throws

Exception

Invoke the specified "doit-method", a static method with no parameters.
The

ExecutionControl.invoke(java.lang.String, java.lang.String)

in this class will call this to invoke.

valueString

```java
protected static
String
valueString​(
Object
value)
```

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

**Parameters:** value

- the value to convert
**Returns:** the

String

representation

---

#### valueString

protected static

String

valueString​(

Object

value)

Converts the

Object

value from

ExecutionControl.invoke(String, String)

or

ExecutionControl.varValue(String, String)

to

String

.

throwConvertedInvocationException

```java
protected
String
throwConvertedInvocationException​(
Throwable
cause)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException
```

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:** cause

- the exception to convert
**Returns:** never returns as it always throws
**Throws:** ExecutionControl.RunException

- for normal exception occurrences
**Throws:** ExecutionControl.InternalException

- for internal problems

---

#### throwConvertedInvocationException

protected

String

throwConvertedInvocationException​(

Throwable

cause)
throws

ExecutionControl.RunException

,

ExecutionControl.InternalException

Converts incoming exceptions in user code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

throwConvertedOtherException

```java
protected
String
throwConvertedOtherException​(
Throwable
ex)
throws
ExecutionControl.RunException
,

ExecutionControl.InternalException
```

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

**Parameters:** ex

- the exception to convert
**Returns:** never returns as it always throws
**Throws:** ExecutionControl.RunException

- for normal exception occurrences
**Throws:** ExecutionControl.InternalException

- for internal problems

---

#### throwConvertedOtherException

protected

String

throwConvertedOtherException​(

Throwable

ex)
throws

ExecutionControl.RunException

,

ExecutionControl.InternalException

Converts incoming exceptions in agent code into instances of subtypes of

ExecutionControl.ExecutionControlException

and throws the
converted exception.

clientCodeEnter

```java
protected void clientCodeEnter()
throws
ExecutionControl.InternalException
```

Marks entry into user code.

**Throws:** ExecutionControl.InternalException

- in unexpected failure cases

---

#### clientCodeEnter

protected void clientCodeEnter()
throws

ExecutionControl.InternalException

Marks entry into user code.

clientCodeLeave

```java
protected void clientCodeLeave()
throws
ExecutionControl.InternalException
```

Marks departure from user code.

**Throws:** ExecutionControl.InternalException

- in unexpected failure cases

---

#### clientCodeLeave

protected void clientCodeLeave()
throws

ExecutionControl.InternalException

Marks departure from user code.

---

