# Class JShell.Builder

**Source:** `jdk.jshell\jdk\jshell\JShell.Builder.html`

### Class Description

```java
public static class
JShell.Builder

extends
Object
```

Builder for

JShell

instances.
Create custom instances of

JShell

by using the setter
methods on this class. After zero or more of these, use the

build()

method to create a

JShell

instance.
These can all be chained. For example, setting the remote output and
error streams:

```java
JShell myShell =
JShell.builder()
.out(myOutStream)
.err(myErrStream)
.build();
```

If no special set-up is needed, just use

JShell.builder().build()

or the short-cut equivalent

JShell.create()

.

**Enclosing class:** JShell

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
JShell.Builder
in​(
InputStream
in)

Sets the input for the running evaluation (it's

System.in

). Note:
applications that use

System.in

for snippet or other
user input cannot use

System.in

as the input stream for
the remote process.

The

read

method of the

InputStream

may throw the

InterruptedIOException

to signal the user canceled the input. The currently running snippet will be automatically

stopped

.

The default, if this is not set, is to provide an empty input stream
--

new ByteArrayInputStream(new byte[0])

.

**Parameters:**
- in

- the

InputStream

to be channelled to

System.in

in the remote execution process

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
out​(
PrintStream
out)

Sets the output for the running evaluation (it's

System.out

).
The controlling process and
the remote process can share

System.out

.

The default, if this is not set, is

System.out

.

**Parameters:**
- out

- the

PrintStream

to be channelled to

System.out

in the remote execution process

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
err​(
PrintStream
err)

Sets the error output for the running evaluation (it's

System.err

). The controlling process and the remote
process can share

System.err

.

The default, if this is not set, is

System.err

.

**Parameters:**
- err

- the

PrintStream

to be channelled to

System.err

in the remote execution process

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
tempVariableNameGenerator​(
Supplier
<
String
> generator)

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created VarSnippet
instances. The name of a variable is queried with

PersistentSnippet.name()

.

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

**Parameters:**
- generator

- the

Supplier

to generate the temporary
variable name string or

null

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
idGenerator​(
BiFunction
<
Snippet
,​
Integer
,​
String
> generator)

Sets the generator of identifying names for Snippets.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created Snippet instances. The
identifying name (id) is accessed with

Snippet.id()

and can be seen in the

StackTraceElement.getFileName()

for a

EvalException

and

UnresolvedReferenceException

.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

**Parameters:**
- generator

- the

BiFunction

to generate the id
string or

null

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
remoteVMOptions​(
String
... options)

Sets additional VM options for launching the VM.

**Parameters:**
- options

- The options for the remote VM

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
compilerOptions​(
String
... options)

Adds compiler options. These additional options will be used on
parsing, analysis, and code generation calls to the compiler.
Options which interfere with results are not supported and have
undefined effects on JShell's operation.

**Parameters:**
- options

- the addition options for compiler invocations

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
executionEngine​(
String
executionControlSpec)

Sets the custom engine for execution. Snippet execution will be
provided by the

ExecutionControl

instance selected by the
specified execution control spec.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:**
- executionControlSpec

- the execution control spec,
which is documented in the

jdk.jshell.spi

package documentation.

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
executionEngine​(
ExecutionControlProvider
executionControlProvider,

Map
<
String
,​
String
> executionControlParameters)

Sets the custom engine for execution. Snippet execution will be
provided by the specified

ExecutionControl

instance.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:**
- executionControlProvider

- the provider to supply the execution
engine
- executionControlParameters

- the parameters to the provider, or

null

for default parameters

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell.Builder
fileManager​(
Function
<
StandardJavaFileManager
,​
StandardJavaFileManager
> mapping)

Configure the

FileManager

to be used by compilation and
source analysis.
If not set or passed null, the compiler's standard file manager will
be used (identity mapping).
For use in special applications where the compiler's normal file
handling needs to be overridden. See the file manager APIs for more
information.
The file manager input enables forwarding file managers, if this
is not needed, the incoming file manager can be ignored (constant
function).

**Parameters:**
- mapping

- a function that given the compiler's standard file
manager, returns a file manager to use

**Returns:**
- the

Builder

instance (for use in chained
initialization)

---

#### public
JShell
build()
throws
IllegalStateException

Builds a JShell state engine. This is the entry-point to all JShell
functionality. This creates a remote process for execution. It is
thus important to close the returned instance.

**Returns:**
- the state engine

**Throws:**
- IllegalStateException

- if the

JShell

instance could not be created.

---

### Additional Sections

#### Class JShell.Builder

java.lang.Object

- jdk.jshell.JShell.Builder

jdk.jshell.JShell.Builder

**Enclosing class:** JShell

```java
public static class
JShell.Builder

extends
Object
```

Builder for

JShell

instances.
Create custom instances of

JShell

by using the setter
methods on this class. After zero or more of these, use the

build()

method to create a

JShell

instance.
These can all be chained. For example, setting the remote output and
error streams:

```java
JShell myShell =
JShell.builder()
.out(myOutStream)
.err(myErrStream)
.build();
```

If no special set-up is needed, just use

JShell.builder().build()

or the short-cut equivalent

JShell.create()

.

public static class

JShell.Builder

extends

Object

Builder for

JShell

instances.
Create custom instances of

JShell

by using the setter
methods on this class. After zero or more of these, use the

build()

method to create a

JShell

instance.
These can all be chained. For example, setting the remote output and
error streams:

```java
JShell myShell =
JShell.builder()
.out(myOutStream)
.err(myErrStream)
.build();
```

If no special set-up is needed, just use

JShell.builder().build()

or the short-cut equivalent

JShell.create()

.

JShell myShell =
JShell.builder()
.out(myOutStream)
.err(myErrStream)
.build();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JShell

build

()

Builds a JShell state engine.

JShell.Builder

compilerOptions

​(

String

... options)

Adds compiler options.

JShell.Builder

err

​(

PrintStream

err)

Sets the error output for the running evaluation (it's

System.err

).

JShell.Builder

executionEngine

​(

String

executionControlSpec)

Sets the custom engine for execution.

JShell.Builder

executionEngine

​(

ExecutionControlProvider

executionControlProvider,

Map

<

String

,​

String

> executionControlParameters)

Sets the custom engine for execution.

JShell.Builder

fileManager

​(

Function

<

StandardJavaFileManager

,​

StandardJavaFileManager

> mapping)

Configure the

FileManager

to be used by compilation and
source analysis.

JShell.Builder

idGenerator

​(

BiFunction

<

Snippet

,​

Integer

,​

String

> generator)

Sets the generator of identifying names for Snippets.

JShell.Builder

in

​(

InputStream

in)

Sets the input for the running evaluation (it's

System.in

).

JShell.Builder

out

​(

PrintStream

out)

Sets the output for the running evaluation (it's

System.out

).

JShell.Builder

remoteVMOptions

​(

String

... options)

Sets additional VM options for launching the VM.

JShell.Builder

tempVariableNameGenerator

​(

Supplier

<

String

> generator)

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JShell

build

()

Builds a JShell state engine.

JShell.Builder

compilerOptions

​(

String

... options)

Adds compiler options.

JShell.Builder

err

​(

PrintStream

err)

Sets the error output for the running evaluation (it's

System.err

).

JShell.Builder

executionEngine

​(

String

executionControlSpec)

Sets the custom engine for execution.

JShell.Builder

executionEngine

​(

ExecutionControlProvider

executionControlProvider,

Map

<

String

,​

String

> executionControlParameters)

Sets the custom engine for execution.

JShell.Builder

fileManager

​(

Function

<

StandardJavaFileManager

,​

StandardJavaFileManager

> mapping)

Configure the

FileManager

to be used by compilation and
source analysis.

JShell.Builder

idGenerator

​(

BiFunction

<

Snippet

,​

Integer

,​

String

> generator)

Sets the generator of identifying names for Snippets.

JShell.Builder

in

​(

InputStream

in)

Sets the input for the running evaluation (it's

System.in

).

JShell.Builder

out

​(

PrintStream

out)

Sets the output for the running evaluation (it's

System.out

).

JShell.Builder

remoteVMOptions

​(

String

... options)

Sets additional VM options for launching the VM.

JShell.Builder

tempVariableNameGenerator

​(

Supplier

<

String

> generator)

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

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

---

#### Method Summary

Builds a JShell state engine.

Adds compiler options.

Sets the error output for the running evaluation (it's

System.err

).

Sets the custom engine for execution.

Configure the

FileManager

to be used by compilation and
source analysis.

Sets the generator of identifying names for Snippets.

Sets the input for the running evaluation (it's

System.in

).

Sets the output for the running evaluation (it's

System.out

).

Sets additional VM options for launching the VM.

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

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

============ METHOD DETAIL ==========

- Method Detail

- in

```java
public
JShell.Builder
in​(
InputStream
in)
```

Sets the input for the running evaluation (it's

System.in

). Note:
applications that use

System.in

for snippet or other
user input cannot use

System.in

as the input stream for
the remote process.

The

read

method of the

InputStream

may throw the

InterruptedIOException

to signal the user canceled the input. The currently running snippet will be automatically

stopped

.

The default, if this is not set, is to provide an empty input stream
--

new ByteArrayInputStream(new byte[0])

.

**Parameters:** in

- the

InputStream

to be channelled to

System.in

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

- out

```java
public
JShell.Builder
out​(
PrintStream
out)
```

Sets the output for the running evaluation (it's

System.out

).
The controlling process and
the remote process can share

System.out

.

The default, if this is not set, is

System.out

.

**Parameters:** out

- the

PrintStream

to be channelled to

System.out

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

- err

```java
public
JShell.Builder
err​(
PrintStream
err)
```

Sets the error output for the running evaluation (it's

System.err

). The controlling process and the remote
process can share

System.err

.

The default, if this is not set, is

System.err

.

**Parameters:** err

- the

PrintStream

to be channelled to

System.err

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

- tempVariableNameGenerator

```java
public
JShell.Builder
tempVariableNameGenerator​(
Supplier
<
String
> generator)
```

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created VarSnippet
instances. The name of a variable is queried with

PersistentSnippet.name()

.

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

**Parameters:** generator

- the

Supplier

to generate the temporary
variable name string or

null
**Returns:** the

Builder

instance (for use in chained
initialization)

- idGenerator

```java
public
JShell.Builder
idGenerator​(
BiFunction
<
Snippet
,​
Integer
,​
String
> generator)
```

Sets the generator of identifying names for Snippets.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created Snippet instances. The
identifying name (id) is accessed with

Snippet.id()

and can be seen in the

StackTraceElement.getFileName()

for a

EvalException

and

UnresolvedReferenceException

.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

**Parameters:** generator

- the

BiFunction

to generate the id
string or

null
**Returns:** the

Builder

instance (for use in chained
initialization)

- remoteVMOptions

```java
public
JShell.Builder
remoteVMOptions​(
String
... options)
```

Sets additional VM options for launching the VM.

**Parameters:** options

- The options for the remote VM
**Returns:** the

Builder

instance (for use in chained
initialization)

- compilerOptions

```java
public
JShell.Builder
compilerOptions​(
String
... options)
```

Adds compiler options. These additional options will be used on
parsing, analysis, and code generation calls to the compiler.
Options which interfere with results are not supported and have
undefined effects on JShell's operation.

**Parameters:** options

- the addition options for compiler invocations
**Returns:** the

Builder

instance (for use in chained
initialization)

- executionEngine

```java
public
JShell.Builder
executionEngine​(
String
executionControlSpec)
```

Sets the custom engine for execution. Snippet execution will be
provided by the

ExecutionControl

instance selected by the
specified execution control spec.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:** executionControlSpec

- the execution control spec,
which is documented in the

jdk.jshell.spi

package documentation.
**Returns:** the

Builder

instance (for use in chained
initialization)

- executionEngine

```java
public
JShell.Builder
executionEngine​(
ExecutionControlProvider
executionControlProvider,

Map
<
String
,​
String
> executionControlParameters)
```

Sets the custom engine for execution. Snippet execution will be
provided by the specified

ExecutionControl

instance.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:** executionControlProvider

- the provider to supply the execution
engine
**Parameters:** executionControlParameters

- the parameters to the provider, or

null

for default parameters
**Returns:** the

Builder

instance (for use in chained
initialization)

- fileManager

```java
public
JShell.Builder
fileManager​(
Function
<
StandardJavaFileManager
,​
StandardJavaFileManager
> mapping)
```

Configure the

FileManager

to be used by compilation and
source analysis.
If not set or passed null, the compiler's standard file manager will
be used (identity mapping).
For use in special applications where the compiler's normal file
handling needs to be overridden. See the file manager APIs for more
information.
The file manager input enables forwarding file managers, if this
is not needed, the incoming file manager can be ignored (constant
function).

**Parameters:** mapping

- a function that given the compiler's standard file
manager, returns a file manager to use
**Returns:** the

Builder

instance (for use in chained
initialization)

- build

```java
public
JShell
build()
throws
IllegalStateException
```

Builds a JShell state engine. This is the entry-point to all JShell
functionality. This creates a remote process for execution. It is
thus important to close the returned instance.

**Returns:** the state engine
**Throws:** IllegalStateException

- if the

JShell

instance could not be created.

Method Detail

- in

```java
public
JShell.Builder
in​(
InputStream
in)
```

Sets the input for the running evaluation (it's

System.in

). Note:
applications that use

System.in

for snippet or other
user input cannot use

System.in

as the input stream for
the remote process.

The

read

method of the

InputStream

may throw the

InterruptedIOException

to signal the user canceled the input. The currently running snippet will be automatically

stopped

.

The default, if this is not set, is to provide an empty input stream
--

new ByteArrayInputStream(new byte[0])

.

**Parameters:** in

- the

InputStream

to be channelled to

System.in

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

- out

```java
public
JShell.Builder
out​(
PrintStream
out)
```

Sets the output for the running evaluation (it's

System.out

).
The controlling process and
the remote process can share

System.out

.

The default, if this is not set, is

System.out

.

**Parameters:** out

- the

PrintStream

to be channelled to

System.out

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

- err

```java
public
JShell.Builder
err​(
PrintStream
err)
```

Sets the error output for the running evaluation (it's

System.err

). The controlling process and the remote
process can share

System.err

.

The default, if this is not set, is

System.err

.

**Parameters:** err

- the

PrintStream

to be channelled to

System.err

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

- tempVariableNameGenerator

```java
public
JShell.Builder
tempVariableNameGenerator​(
Supplier
<
String
> generator)
```

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created VarSnippet
instances. The name of a variable is queried with

PersistentSnippet.name()

.

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

**Parameters:** generator

- the

Supplier

to generate the temporary
variable name string or

null
**Returns:** the

Builder

instance (for use in chained
initialization)

- idGenerator

```java
public
JShell.Builder
idGenerator​(
BiFunction
<
Snippet
,​
Integer
,​
String
> generator)
```

Sets the generator of identifying names for Snippets.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created Snippet instances. The
identifying name (id) is accessed with

Snippet.id()

and can be seen in the

StackTraceElement.getFileName()

for a

EvalException

and

UnresolvedReferenceException

.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

**Parameters:** generator

- the

BiFunction

to generate the id
string or

null
**Returns:** the

Builder

instance (for use in chained
initialization)

- remoteVMOptions

```java
public
JShell.Builder
remoteVMOptions​(
String
... options)
```

Sets additional VM options for launching the VM.

**Parameters:** options

- The options for the remote VM
**Returns:** the

Builder

instance (for use in chained
initialization)

- compilerOptions

```java
public
JShell.Builder
compilerOptions​(
String
... options)
```

Adds compiler options. These additional options will be used on
parsing, analysis, and code generation calls to the compiler.
Options which interfere with results are not supported and have
undefined effects on JShell's operation.

**Parameters:** options

- the addition options for compiler invocations
**Returns:** the

Builder

instance (for use in chained
initialization)

- executionEngine

```java
public
JShell.Builder
executionEngine​(
String
executionControlSpec)
```

Sets the custom engine for execution. Snippet execution will be
provided by the

ExecutionControl

instance selected by the
specified execution control spec.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:** executionControlSpec

- the execution control spec,
which is documented in the

jdk.jshell.spi

package documentation.
**Returns:** the

Builder

instance (for use in chained
initialization)

- executionEngine

```java
public
JShell.Builder
executionEngine​(
ExecutionControlProvider
executionControlProvider,

Map
<
String
,​
String
> executionControlParameters)
```

Sets the custom engine for execution. Snippet execution will be
provided by the specified

ExecutionControl

instance.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:** executionControlProvider

- the provider to supply the execution
engine
**Parameters:** executionControlParameters

- the parameters to the provider, or

null

for default parameters
**Returns:** the

Builder

instance (for use in chained
initialization)

- fileManager

```java
public
JShell.Builder
fileManager​(
Function
<
StandardJavaFileManager
,​
StandardJavaFileManager
> mapping)
```

Configure the

FileManager

to be used by compilation and
source analysis.
If not set or passed null, the compiler's standard file manager will
be used (identity mapping).
For use in special applications where the compiler's normal file
handling needs to be overridden. See the file manager APIs for more
information.
The file manager input enables forwarding file managers, if this
is not needed, the incoming file manager can be ignored (constant
function).

**Parameters:** mapping

- a function that given the compiler's standard file
manager, returns a file manager to use
**Returns:** the

Builder

instance (for use in chained
initialization)

- build

```java
public
JShell
build()
throws
IllegalStateException
```

Builds a JShell state engine. This is the entry-point to all JShell
functionality. This creates a remote process for execution. It is
thus important to close the returned instance.

**Returns:** the state engine
**Throws:** IllegalStateException

- if the

JShell

instance could not be created.

---

#### Method Detail

in

```java
public
JShell.Builder
in​(
InputStream
in)
```

Sets the input for the running evaluation (it's

System.in

). Note:
applications that use

System.in

for snippet or other
user input cannot use

System.in

as the input stream for
the remote process.

The

read

method of the

InputStream

may throw the

InterruptedIOException

to signal the user canceled the input. The currently running snippet will be automatically

stopped

.

The default, if this is not set, is to provide an empty input stream
--

new ByteArrayInputStream(new byte[0])

.

**Parameters:** in

- the

InputStream

to be channelled to

System.in

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### in

public

JShell.Builder

in​(

InputStream

in)

Sets the input for the running evaluation (it's

System.in

). Note:
applications that use

System.in

for snippet or other
user input cannot use

System.in

as the input stream for
the remote process.

The

read

method of the

InputStream

may throw the

InterruptedIOException

to signal the user canceled the input. The currently running snippet will be automatically

stopped

.

The default, if this is not set, is to provide an empty input stream
--

new ByteArrayInputStream(new byte[0])

.

The

read

method of the

InputStream

may throw the

InterruptedIOException

to signal the user canceled the input. The currently running snippet will be automatically

stopped

.

The default, if this is not set, is to provide an empty input stream
--

new ByteArrayInputStream(new byte[0])

.

The default, if this is not set, is to provide an empty input stream
--

new ByteArrayInputStream(new byte[0])

.

out

```java
public
JShell.Builder
out​(
PrintStream
out)
```

Sets the output for the running evaluation (it's

System.out

).
The controlling process and
the remote process can share

System.out

.

The default, if this is not set, is

System.out

.

**Parameters:** out

- the

PrintStream

to be channelled to

System.out

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### out

public

JShell.Builder

out​(

PrintStream

out)

Sets the output for the running evaluation (it's

System.out

).
The controlling process and
the remote process can share

System.out

.

The default, if this is not set, is

System.out

.

The default, if this is not set, is

System.out

.

err

```java
public
JShell.Builder
err​(
PrintStream
err)
```

Sets the error output for the running evaluation (it's

System.err

). The controlling process and the remote
process can share

System.err

.

The default, if this is not set, is

System.err

.

**Parameters:** err

- the

PrintStream

to be channelled to

System.err

in the remote execution process
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### err

public

JShell.Builder

err​(

PrintStream

err)

Sets the error output for the running evaluation (it's

System.err

). The controlling process and the remote
process can share

System.err

.

The default, if this is not set, is

System.err

.

The default, if this is not set, is

System.err

.

tempVariableNameGenerator

```java
public
JShell.Builder
tempVariableNameGenerator​(
Supplier
<
String
> generator)
```

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created VarSnippet
instances. The name of a variable is queried with

PersistentSnippet.name()

.

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

**Parameters:** generator

- the

Supplier

to generate the temporary
variable name string or

null
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### tempVariableNameGenerator

public

JShell.Builder

tempVariableNameGenerator​(

Supplier

<

String

> generator)

Sets a generator of temp variable names for

VarSnippet

of

Snippet.SubKind.TEMP_VAR_EXPRESSION_SUBKIND

.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created VarSnippet
instances. The name of a variable is queried with

PersistentSnippet.name()

.

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

Do not use this method unless you have explicit need for it.

The generator will be used for newly created VarSnippet
instances. The name of a variable is queried with

PersistentSnippet.name()

.

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

The generator will be used for newly created VarSnippet
instances. The name of a variable is queried with

PersistentSnippet.name()

.

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

The callback is sent during the processing of the snippet, the
JShell state is not stable. No calls whatsoever on the

JShell

instance may be made from the callback.

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

The generated name must be unique within active snippets.

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

The default behavior (if this is not set or

generator

is null) is to generate the name as a sequential number with a
prefixing dollar sign ("$").

idGenerator

```java
public
JShell.Builder
idGenerator​(
BiFunction
<
Snippet
,​
Integer
,​
String
> generator)
```

Sets the generator of identifying names for Snippets.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created Snippet instances. The
identifying name (id) is accessed with

Snippet.id()

and can be seen in the

StackTraceElement.getFileName()

for a

EvalException

and

UnresolvedReferenceException

.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

**Parameters:** generator

- the

BiFunction

to generate the id
string or

null
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### idGenerator

public

JShell.Builder

idGenerator​(

BiFunction

<

Snippet

,​

Integer

,​

String

> generator)

Sets the generator of identifying names for Snippets.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created Snippet instances. The
identifying name (id) is accessed with

Snippet.id()

and can be seen in the

StackTraceElement.getFileName()

for a

EvalException

and

UnresolvedReferenceException

.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

Do not use this method unless you have explicit need for it.

The generator will be used for newly created Snippet instances. The
identifying name (id) is accessed with

Snippet.id()

and can be seen in the

StackTraceElement.getFileName()

for a

EvalException

and

UnresolvedReferenceException

.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

The generator will be used for newly created Snippet instances. The
identifying name (id) is accessed with

Snippet.id()

and can be seen in the

StackTraceElement.getFileName()

for a

EvalException

and

UnresolvedReferenceException

.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

The inputs to the generator are the

Snippet

and an
integer. The integer will be the same for two Snippets which would
overwrite one-another, but otherwise is unique.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

The callback is sent during the processing of the snippet and the
Snippet and the state as a whole are not stable. No calls to change
system state (including Snippet state) should be made. Queries of
Snippet may be made except to

Snippet.id()

. No
calls on the

JShell

instance may be made from the
callback, except to

status(Snippet)

.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

The default behavior (if this is not set or

generator

is null) is to generate the id as the integer converted to a string.

remoteVMOptions

```java
public
JShell.Builder
remoteVMOptions​(
String
... options)
```

Sets additional VM options for launching the VM.

**Parameters:** options

- The options for the remote VM
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### remoteVMOptions

public

JShell.Builder

remoteVMOptions​(

String

... options)

Sets additional VM options for launching the VM.

compilerOptions

```java
public
JShell.Builder
compilerOptions​(
String
... options)
```

Adds compiler options. These additional options will be used on
parsing, analysis, and code generation calls to the compiler.
Options which interfere with results are not supported and have
undefined effects on JShell's operation.

**Parameters:** options

- the addition options for compiler invocations
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### compilerOptions

public

JShell.Builder

compilerOptions​(

String

... options)

Adds compiler options. These additional options will be used on
parsing, analysis, and code generation calls to the compiler.
Options which interfere with results are not supported and have
undefined effects on JShell's operation.

executionEngine

```java
public
JShell.Builder
executionEngine​(
String
executionControlSpec)
```

Sets the custom engine for execution. Snippet execution will be
provided by the

ExecutionControl

instance selected by the
specified execution control spec.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:** executionControlSpec

- the execution control spec,
which is documented in the

jdk.jshell.spi

package documentation.
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### executionEngine

public

JShell.Builder

executionEngine​(

String

executionControlSpec)

Sets the custom engine for execution. Snippet execution will be
provided by the

ExecutionControl

instance selected by the
specified execution control spec.
Use, at most, one of these overloaded

executionEngine

builder
methods.

executionEngine

```java
public
JShell.Builder
executionEngine​(
ExecutionControlProvider
executionControlProvider,

Map
<
String
,​
String
> executionControlParameters)
```

Sets the custom engine for execution. Snippet execution will be
provided by the specified

ExecutionControl

instance.
Use, at most, one of these overloaded

executionEngine

builder
methods.

**Parameters:** executionControlProvider

- the provider to supply the execution
engine
**Parameters:** executionControlParameters

- the parameters to the provider, or

null

for default parameters
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### executionEngine

public

JShell.Builder

executionEngine​(

ExecutionControlProvider

executionControlProvider,

Map

<

String

,​

String

> executionControlParameters)

Sets the custom engine for execution. Snippet execution will be
provided by the specified

ExecutionControl

instance.
Use, at most, one of these overloaded

executionEngine

builder
methods.

fileManager

```java
public
JShell.Builder
fileManager​(
Function
<
StandardJavaFileManager
,​
StandardJavaFileManager
> mapping)
```

Configure the

FileManager

to be used by compilation and
source analysis.
If not set or passed null, the compiler's standard file manager will
be used (identity mapping).
For use in special applications where the compiler's normal file
handling needs to be overridden. See the file manager APIs for more
information.
The file manager input enables forwarding file managers, if this
is not needed, the incoming file manager can be ignored (constant
function).

**Parameters:** mapping

- a function that given the compiler's standard file
manager, returns a file manager to use
**Returns:** the

Builder

instance (for use in chained
initialization)

---

#### fileManager

public

JShell.Builder

fileManager​(

Function

<

StandardJavaFileManager

,​

StandardJavaFileManager

> mapping)

Configure the

FileManager

to be used by compilation and
source analysis.
If not set or passed null, the compiler's standard file manager will
be used (identity mapping).
For use in special applications where the compiler's normal file
handling needs to be overridden. See the file manager APIs for more
information.
The file manager input enables forwarding file managers, if this
is not needed, the incoming file manager can be ignored (constant
function).

build

```java
public
JShell
build()
throws
IllegalStateException
```

Builds a JShell state engine. This is the entry-point to all JShell
functionality. This creates a remote process for execution. It is
thus important to close the returned instance.

**Returns:** the state engine
**Throws:** IllegalStateException

- if the

JShell

instance could not be created.

---

#### build

public

JShell

build()
throws

IllegalStateException

Builds a JShell state engine. This is the entry-point to all JShell
functionality. This creates a remote process for execution. It is
thus important to close the returned instance.

---

