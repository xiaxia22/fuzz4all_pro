# Interface ExecutionControl

**Source:** `jdk.jshell\jdk\jshell\spi\ExecutionControl.html`

### Class Description

```java
public interface
ExecutionControl

extends
AutoCloseable
```

This interface specifies the functionality that must provided to implement a
pluggable JShell execution engine.

The audience for this Service Provider Interface is engineers wishing to
implement their own version of the execution engine in support of the JShell
API.

A Snippet is compiled into code wrapped in a 'wrapper class'. The execution
engine is used by the core JShell implementation to load and, for executable
Snippets, execute the Snippet.

Methods defined in this interface should only be called by the core JShell
implementation.

**All Superinterfaces:** AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException

Attempts to load new classes.

**Parameters:**
- cbcs

- the class name and bytecodes to load

**Throws:**
- ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
- ExecutionControl.NotImplementedException

- if not implemented
- ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException

Attempts to redefine previously loaded classes.

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

#### String
invoke​(
String
className,

String
methodName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Invokes an executable Snippet by calling a method on the specified
wrapper class. The method must have no arguments and return String.

**Parameters:**
- className

- the class whose method should be invoked
- methodName

- the name of method to invoke

**Returns:**
- the result of the execution or null if no result

**Throws:**
- ExecutionControl.UserException

- the invoke raised a user exception
- ExecutionControl.ResolutionException

- the invoke attempted to directly or
indirectly invoke an unresolved snippet
- ExecutionControl.StoppedException

- if the

invoke()

was canceled by

stop()
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.InternalException

- an internal problem occurred
- ExecutionControl.RunException

---

#### String
varValue​(
String
className,

String
varName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Returns the value of a variable.

**Parameters:**
- className

- the name of the wrapper class of the variable
- varName

- the name of the variable

**Returns:**
- the value of the variable

**Throws:**
- ExecutionControl.UserException

- formatting the value raised a user exception
- ExecutionControl.ResolutionException

- formatting the value attempted to directly or
indirectly invoke an unresolved snippet
- ExecutionControl.StoppedException

- if the formatting the value was canceled by

stop()
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.InternalException

- an internal problem occurred
- ExecutionControl.RunException

---

#### void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Adds the path to the execution class path.

**Parameters:**
- path

- the path to add

**Throws:**
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.InternalException

- an internal problem occurred

---

#### void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Interrupts a running invoke.

**Throws:**
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.InternalException

- an internal problem occurred

---

#### Object
extensionCommand​(
String
command,

Object
arg)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Run a non-standard command (or a standard command from a newer version).

**Parameters:**
- command

- the non-standard command
- arg

- the commands argument

**Returns:**
- the commands return value

**Throws:**
- ExecutionControl.UserException

- the command raised a user exception
- ExecutionControl.ResolutionException

- the command attempted to directly or
indirectly invoke an unresolved snippet
- ExecutionControl.StoppedException

- if the command was canceled by

stop()
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.NotImplementedException

- if not implemented
- ExecutionControl.InternalException

- an internal problem occurred
- ExecutionControl.RunException

---

#### void close()

Shuts down this execution engine. Implementation should free all
resources held by this execution engine.

No calls to methods on this interface should be made after close.

**Specified by:**
- close

in interface

AutoCloseable

---

#### static
ExecutionControl
generate​(
ExecutionEnv
env,

String
name,

Map
<
String
,​
String
> parameters)
throws
Throwable

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:**
- env

- the execution environment (provided by JShell)
- name

- the name of provider
- parameters

- the parameter map.

**Returns:**
- the execution engine

**Throws:**
- Throwable

- an exception that occurred attempting to find or create
the execution engine.
- IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.

---

#### static
ExecutionControl
generate​(
ExecutionEnv
env,

String
spec)
throws
Throwable

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:**
- env

- the execution environment (provided by JShell)
- spec

- the

ExecutionControl

spec, which is described in
the documentation of this

package documentation

.

**Returns:**
- the execution engine

**Throws:**
- Throwable

- an exception that occurred attempting to find or create
the execution engine.
- IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.
- IllegalArgumentException

- if

spec

is malformed

---

### Additional Sections

#### Interface ExecutionControl

**All Superinterfaces:** AutoCloseable

**All Known Implementing Classes:** DirectExecutionControl

,

JdiDefaultExecutionControl

,

JdiExecutionControl

,

LocalExecutionControl

,

RemoteExecutionControl

,

StreamingExecutionControl

```java
public interface
ExecutionControl

extends
AutoCloseable
```

This interface specifies the functionality that must provided to implement a
pluggable JShell execution engine.

The audience for this Service Provider Interface is engineers wishing to
implement their own version of the execution engine in support of the JShell
API.

A Snippet is compiled into code wrapped in a 'wrapper class'. The execution
engine is used by the core JShell implementation to load and, for executable
Snippets, execute the Snippet.

Methods defined in this interface should only be called by the core JShell
implementation.

**Since:** 9

public interface

ExecutionControl

extends

AutoCloseable

This interface specifies the functionality that must provided to implement a
pluggable JShell execution engine.

The audience for this Service Provider Interface is engineers wishing to
implement their own version of the execution engine in support of the JShell
API.

A Snippet is compiled into code wrapped in a 'wrapper class'. The execution
engine is used by the core JShell implementation to load and, for executable
Snippets, execute the Snippet.

Methods defined in this interface should only be called by the core JShell
implementation.

The audience for this Service Provider Interface is engineers wishing to
implement their own version of the execution engine in support of the JShell
API.

A Snippet is compiled into code wrapped in a 'wrapper class'. The execution
engine is used by the core JShell implementation to load and, for executable
Snippets, execute the Snippet.

Methods defined in this interface should only be called by the core JShell
implementation.

A Snippet is compiled into code wrapped in a 'wrapper class'. The execution
engine is used by the core JShell implementation to load and, for executable
Snippets, execute the Snippet.

Methods defined in this interface should only be called by the core JShell
implementation.

Methods defined in this interface should only be called by the core JShell
implementation.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ExecutionControl.ClassBytecodes

Bundles class name with class bytecodes.

static class

ExecutionControl.ClassInstallException

A class install (load or redefine) encountered a problem.

static class

ExecutionControl.EngineTerminationException

Unbidden execution engine termination has occurred.

static class

ExecutionControl.ExecutionControlException

The abstract base of all

ExecutionControl

exceptions.

static class

ExecutionControl.InternalException

An internal problem has occurred.

static class

ExecutionControl.NotImplementedException

The command is not implemented.

static class

ExecutionControl.ResolutionException

An exception indicating that a

DeclarationSnippet

with unresolved
references has been encountered.

static class

ExecutionControl.RunException

The abstract base of of exceptions specific to running user code.

static class

ExecutionControl.StoppedException

An exception indicating that an

invoke(java.lang.String, java.lang.String)

(or theoretically a

varValue(java.lang.String, java.lang.String)

)
has been interrupted by a

stop()

.

static class

ExecutionControl.UserException

A 'normal' user exception occurred.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addToClasspath

​(

String

path)

Adds the path to the execution class path.

void

close

()

Shuts down this execution engine.

Object

extensionCommand

​(

String

command,

Object

arg)

Run a non-standard command (or a standard command from a newer version).

static

ExecutionControl

generate

​(

ExecutionEnv

env,

String

spec)

Search for a provider, then create and return the

ExecutionControl

instance.

static

ExecutionControl

generate

​(

ExecutionEnv

env,

String

name,

Map

<

String

,​

String

> parameters)

Search for a provider, then create and return the

ExecutionControl

instance.

String

invoke

​(

String

className,

String

methodName)

Invokes an executable Snippet by calling a method on the specified
wrapper class.

void

load

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Attempts to load new classes.

void

redefine

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Attempts to redefine previously loaded classes.

void

stop

()

Interrupts a running invoke.

String

varValue

​(

String

className,

String

varName)

Returns the value of a variable.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ExecutionControl.ClassBytecodes

Bundles class name with class bytecodes.

static class

ExecutionControl.ClassInstallException

A class install (load or redefine) encountered a problem.

static class

ExecutionControl.EngineTerminationException

Unbidden execution engine termination has occurred.

static class

ExecutionControl.ExecutionControlException

The abstract base of all

ExecutionControl

exceptions.

static class

ExecutionControl.InternalException

An internal problem has occurred.

static class

ExecutionControl.NotImplementedException

The command is not implemented.

static class

ExecutionControl.ResolutionException

An exception indicating that a

DeclarationSnippet

with unresolved
references has been encountered.

static class

ExecutionControl.RunException

The abstract base of of exceptions specific to running user code.

static class

ExecutionControl.StoppedException

An exception indicating that an

invoke(java.lang.String, java.lang.String)

(or theoretically a

varValue(java.lang.String, java.lang.String)

)
has been interrupted by a

stop()

.

static class

ExecutionControl.UserException

A 'normal' user exception occurred.

---

#### Nested Class Summary

Bundles class name with class bytecodes.

A class install (load or redefine) encountered a problem.

Unbidden execution engine termination has occurred.

The abstract base of all

ExecutionControl

exceptions.

An internal problem has occurred.

The command is not implemented.

An exception indicating that a

DeclarationSnippet

with unresolved
references has been encountered.

The abstract base of of exceptions specific to running user code.

An exception indicating that an

invoke(java.lang.String, java.lang.String)

(or theoretically a

varValue(java.lang.String, java.lang.String)

)
has been interrupted by a

stop()

.

A 'normal' user exception occurred.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addToClasspath

​(

String

path)

Adds the path to the execution class path.

void

close

()

Shuts down this execution engine.

Object

extensionCommand

​(

String

command,

Object

arg)

Run a non-standard command (or a standard command from a newer version).

static

ExecutionControl

generate

​(

ExecutionEnv

env,

String

spec)

Search for a provider, then create and return the

ExecutionControl

instance.

static

ExecutionControl

generate

​(

ExecutionEnv

env,

String

name,

Map

<

String

,​

String

> parameters)

Search for a provider, then create and return the

ExecutionControl

instance.

String

invoke

​(

String

className,

String

methodName)

Invokes an executable Snippet by calling a method on the specified
wrapper class.

void

load

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Attempts to load new classes.

void

redefine

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Attempts to redefine previously loaded classes.

void

stop

()

Interrupts a running invoke.

String

varValue

​(

String

className,

String

varName)

Returns the value of a variable.

---

#### Method Summary

Adds the path to the execution class path.

Shuts down this execution engine.

Run a non-standard command (or a standard command from a newer version).

Search for a provider, then create and return the

ExecutionControl

instance.

Invokes an executable Snippet by calling a method on the specified
wrapper class.

Attempts to load new classes.

Attempts to redefine previously loaded classes.

Interrupts a running invoke.

Returns the value of a variable.

============ METHOD DETAIL ==========

- Method Detail

- load

```java
void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to load new classes.

**Parameters:** cbcs

- the class name and bytecodes to load
**Throws:** ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- redefine

```java
void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to redefine previously loaded classes.

**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- invoke

```java
String
invoke​(
String
className,

String
methodName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Invokes an executable Snippet by calling a method on the specified
wrapper class. The method must have no arguments and return String.

**Parameters:** className

- the class whose method should be invoked
**Parameters:** methodName

- the name of method to invoke
**Returns:** the result of the execution or null if no result
**Throws:** ExecutionControl.UserException

- the invoke raised a user exception
**Throws:** ExecutionControl.ResolutionException

- the invoke attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the

invoke()

was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

- varValue

```java
String
varValue​(
String
className,

String
varName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Returns the value of a variable.

**Parameters:** className

- the name of the wrapper class of the variable
**Parameters:** varName

- the name of the variable
**Returns:** the value of the variable
**Throws:** ExecutionControl.UserException

- formatting the value raised a user exception
**Throws:** ExecutionControl.ResolutionException

- formatting the value attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the formatting the value was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

- addToClasspath

```java
void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Adds the path to the execution class path.

**Parameters:** path

- the path to add
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- stop

```java
void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running invoke.

**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- extensionCommand

```java
Object
extensionCommand​(
String
command,

Object
arg)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Run a non-standard command (or a standard command from a newer version).

**Parameters:** command

- the non-standard command
**Parameters:** arg

- the commands argument
**Returns:** the commands return value
**Throws:** ExecutionControl.UserException

- the command raised a user exception
**Throws:** ExecutionControl.ResolutionException

- the command attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the command was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

- close

```java
void close()
```

Shuts down this execution engine. Implementation should free all
resources held by this execution engine.

No calls to methods on this interface should be made after close.

**Specified by:** close

in interface

AutoCloseable

- generate

```java
static
ExecutionControl
generate​(
ExecutionEnv
env,

String
name,

Map
<
String
,​
String
> parameters)
throws
Throwable
```

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment (provided by JShell)
**Parameters:** name

- the name of provider
**Parameters:** parameters

- the parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to find or create
the execution engine.
**Throws:** IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.

- generate

```java
static
ExecutionControl
generate​(
ExecutionEnv
env,

String
spec)
throws
Throwable
```

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment (provided by JShell)
**Parameters:** spec

- the

ExecutionControl

spec, which is described in
the documentation of this

package documentation

.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to find or create
the execution engine.
**Throws:** IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.
**Throws:** IllegalArgumentException

- if

spec

is malformed

Method Detail

- load

```java
void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to load new classes.

**Parameters:** cbcs

- the class name and bytecodes to load
**Throws:** ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- redefine

```java
void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to redefine previously loaded classes.

**Parameters:** cbcs

- the class name and bytecodes to redefine
**Throws:** ExecutionControl.ClassInstallException

- exception occurred redefining the classes,
some or all were not redefined
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- invoke

```java
String
invoke​(
String
className,

String
methodName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Invokes an executable Snippet by calling a method on the specified
wrapper class. The method must have no arguments and return String.

**Parameters:** className

- the class whose method should be invoked
**Parameters:** methodName

- the name of method to invoke
**Returns:** the result of the execution or null if no result
**Throws:** ExecutionControl.UserException

- the invoke raised a user exception
**Throws:** ExecutionControl.ResolutionException

- the invoke attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the

invoke()

was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

- varValue

```java
String
varValue​(
String
className,

String
varName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Returns the value of a variable.

**Parameters:** className

- the name of the wrapper class of the variable
**Parameters:** varName

- the name of the variable
**Returns:** the value of the variable
**Throws:** ExecutionControl.UserException

- formatting the value raised a user exception
**Throws:** ExecutionControl.ResolutionException

- formatting the value attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the formatting the value was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

- addToClasspath

```java
void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Adds the path to the execution class path.

**Parameters:** path

- the path to add
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- stop

```java
void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running invoke.

**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- extensionCommand

```java
Object
extensionCommand​(
String
command,

Object
arg)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Run a non-standard command (or a standard command from a newer version).

**Parameters:** command

- the non-standard command
**Parameters:** arg

- the commands argument
**Returns:** the commands return value
**Throws:** ExecutionControl.UserException

- the command raised a user exception
**Throws:** ExecutionControl.ResolutionException

- the command attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the command was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

- close

```java
void close()
```

Shuts down this execution engine. Implementation should free all
resources held by this execution engine.

No calls to methods on this interface should be made after close.

**Specified by:** close

in interface

AutoCloseable

- generate

```java
static
ExecutionControl
generate​(
ExecutionEnv
env,

String
name,

Map
<
String
,​
String
> parameters)
throws
Throwable
```

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment (provided by JShell)
**Parameters:** name

- the name of provider
**Parameters:** parameters

- the parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to find or create
the execution engine.
**Throws:** IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.

- generate

```java
static
ExecutionControl
generate​(
ExecutionEnv
env,

String
spec)
throws
Throwable
```

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment (provided by JShell)
**Parameters:** spec

- the

ExecutionControl

spec, which is described in
the documentation of this

package documentation

.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to find or create
the execution engine.
**Throws:** IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.
**Throws:** IllegalArgumentException

- if

spec

is malformed

---

#### Method Detail

load

```java
void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to load new classes.

**Parameters:** cbcs

- the class name and bytecodes to load
**Throws:** ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### load

void load​(

ExecutionControl.ClassBytecodes

[] cbcs)
throws

ExecutionControl.ClassInstallException

,

ExecutionControl.NotImplementedException

,

ExecutionControl.EngineTerminationException

Attempts to load new classes.

redefine

```java
void redefine​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to redefine previously loaded classes.

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

void redefine​(

ExecutionControl.ClassBytecodes

[] cbcs)
throws

ExecutionControl.ClassInstallException

,

ExecutionControl.NotImplementedException

,

ExecutionControl.EngineTerminationException

Attempts to redefine previously loaded classes.

invoke

```java
String
invoke​(
String
className,

String
methodName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Invokes an executable Snippet by calling a method on the specified
wrapper class. The method must have no arguments and return String.

**Parameters:** className

- the class whose method should be invoked
**Parameters:** methodName

- the name of method to invoke
**Returns:** the result of the execution or null if no result
**Throws:** ExecutionControl.UserException

- the invoke raised a user exception
**Throws:** ExecutionControl.ResolutionException

- the invoke attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the

invoke()

was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

---

#### invoke

String

invoke​(

String

className,

String

methodName)
throws

ExecutionControl.RunException

,

ExecutionControl.EngineTerminationException

,

ExecutionControl.InternalException

Invokes an executable Snippet by calling a method on the specified
wrapper class. The method must have no arguments and return String.

varValue

```java
String
varValue​(
String
className,

String
varName)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Returns the value of a variable.

**Parameters:** className

- the name of the wrapper class of the variable
**Parameters:** varName

- the name of the variable
**Returns:** the value of the variable
**Throws:** ExecutionControl.UserException

- formatting the value raised a user exception
**Throws:** ExecutionControl.ResolutionException

- formatting the value attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the formatting the value was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

---

#### varValue

String

varValue​(

String

className,

String

varName)
throws

ExecutionControl.RunException

,

ExecutionControl.EngineTerminationException

,

ExecutionControl.InternalException

Returns the value of a variable.

addToClasspath

```java
void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Adds the path to the execution class path.

**Parameters:** path

- the path to add
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

---

#### addToClasspath

void addToClasspath​(

String

path)
throws

ExecutionControl.EngineTerminationException

,

ExecutionControl.InternalException

Adds the path to the execution class path.

stop

```java
void stop()
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Interrupts a running invoke.

**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

---

#### stop

void stop()
throws

ExecutionControl.EngineTerminationException

,

ExecutionControl.InternalException

Interrupts a running invoke.

extensionCommand

```java
Object
extensionCommand​(
String
command,

Object
arg)
throws
ExecutionControl.RunException
,

ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Run a non-standard command (or a standard command from a newer version).

**Parameters:** command

- the non-standard command
**Parameters:** arg

- the commands argument
**Returns:** the commands return value
**Throws:** ExecutionControl.UserException

- the command raised a user exception
**Throws:** ExecutionControl.ResolutionException

- the command attempted to directly or
indirectly invoke an unresolved snippet
**Throws:** ExecutionControl.StoppedException

- if the command was canceled by

stop()
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.InternalException

- an internal problem occurred
**Throws:** ExecutionControl.RunException

---

#### extensionCommand

Object

extensionCommand​(

String

command,

Object

arg)
throws

ExecutionControl.RunException

,

ExecutionControl.EngineTerminationException

,

ExecutionControl.InternalException

Run a non-standard command (or a standard command from a newer version).

close

```java
void close()
```

Shuts down this execution engine. Implementation should free all
resources held by this execution engine.

No calls to methods on this interface should be made after close.

**Specified by:** close

in interface

AutoCloseable

---

#### close

void close()

Shuts down this execution engine. Implementation should free all
resources held by this execution engine.

No calls to methods on this interface should be made after close.

No calls to methods on this interface should be made after close.

generate

```java
static
ExecutionControl
generate​(
ExecutionEnv
env,

String
name,

Map
<
String
,​
String
> parameters)
throws
Throwable
```

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment (provided by JShell)
**Parameters:** name

- the name of provider
**Parameters:** parameters

- the parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to find or create
the execution engine.
**Throws:** IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.

---

#### generate

static

ExecutionControl

generate​(

ExecutionEnv

env,

String

name,

Map

<

String

,​

String

> parameters)
throws

Throwable

Search for a provider, then create and return the

ExecutionControl

instance.

generate

```java
static
ExecutionControl
generate​(
ExecutionEnv
env,

String
spec)
throws
Throwable
```

Search for a provider, then create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment (provided by JShell)
**Parameters:** spec

- the

ExecutionControl

spec, which is described in
the documentation of this

package documentation

.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to find or create
the execution engine.
**Throws:** IllegalArgumentException

- if no ExecutionControlProvider has the
specified

name

and

parameters

.
**Throws:** IllegalArgumentException

- if

spec

is malformed

---

#### generate

static

ExecutionControl

generate​(

ExecutionEnv

env,

String

spec)
throws

Throwable

Search for a provider, then create and return the

ExecutionControl

instance.

---

