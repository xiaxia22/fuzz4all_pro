# Class JavacTask

**Source:** `jdk.compiler\com\sun\source\util\JavacTask.html`

### Class Description

```java
public abstract class
JavacTask

extends
Object

implements
JavaCompiler.CompilationTask
```

Provides access to functionality specific to the JDK Java Compiler, javac.

**All Implemented Interfaces:** Callable

<

Boolean

>

,

JavaCompiler.CompilationTask

---

### Field Details

*No entries found.*

### Constructor Details

#### public JavacTask()

*No description found.*

---

### Method Details

#### public static
JavacTask
instance​(
ProcessingEnvironment
processingEnvironment)

Returns the

JavacTask

for a

ProcessingEnvironment

.
If the compiler is being invoked using a

CompilationTask

,
then that task will be returned.

**Parameters:**
- processingEnvironment

- the processing environment

**Returns:**
- the

JavacTask

for a

ProcessingEnvironment

**Since:**
- 1.8

---

#### public abstract
Iterable
<? extends
CompilationUnitTree
> parse()
throws
IOException

Parses the specified files returning a list of abstract syntax trees.

**Returns:**
- a list of abstract syntax trees

**Throws:**
- IOException

- if an unhandled I/O error occurred in the compiler.
- IllegalStateException

- if the operation cannot be performed at this time.

---

#### public abstract
Iterable
<? extends
Element
> analyze()
throws
IOException

Completes all analysis.

**Returns:**
- a list of elements that were analyzed

**Throws:**
- IOException

- if an unhandled I/O error occurred in the compiler.
- IllegalStateException

- if the operation cannot be performed at this time.

---

#### public abstract
Iterable
<? extends
JavaFileObject
> generate()
throws
IOException

Generates code.

**Returns:**
- a list of files that were generated

**Throws:**
- IOException

- if an unhandled I/O error occurred in the compiler.
- IllegalStateException

- if the operation cannot be performed at this time.

---

#### public abstract void setTaskListener​(
TaskListener
taskListener)

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

If another listener is receiving notifications as a result of a prior
call of this method, then that listener will no longer receive notifications.

Informally, this method is equivalent to calling

removeTaskListener

for
any listener that has been previously set, followed by

addTaskListener

for the new listener.

**Parameters:**
- taskListener

- the task listener

**Throws:**
- IllegalStateException

- if the specified listener has already been added.

---

#### public abstract void addTaskListener​(
TaskListener
taskListener)

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

This method may be called at any time before or during the compilation.

**Parameters:**
- taskListener

- the task listener

**Throws:**
- IllegalStateException

- if the specified listener has already been added.

**Since:**
- 1.8

---

#### public abstract void removeTaskListener​(
TaskListener
taskListener)

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

This method may be called at any time before or during the compilation.

**Parameters:**
- taskListener

- the task listener

**Since:**
- 1.8

---

#### public abstract
TypeMirror
getTypeMirror​(
Iterable
<? extends
Tree
> path)

Returns a type mirror of the tree node determined by the specified path.
This method has been superceded by methods on

Trees

.

**Parameters:**
- path

- the path

**Returns:**
- the type mirror

**See Also:**
- Trees.getTypeMirror(com.sun.source.util.TreePath)

---

#### public abstract
Elements
getElements()

Returns a utility object for dealing with program elements.

**Returns:**
- a utility object for dealing with program elements

---

#### public abstract
Types
getTypes()

Returns a utility object for dealing with type mirrors.

**Returns:**
- the utility object for dealing with type mirrors

---

### Additional Sections

#### Class JavacTask

java.lang.Object

- com.sun.source.util.JavacTask

com.sun.source.util.JavacTask

**All Implemented Interfaces:** Callable

<

Boolean

>

,

JavaCompiler.CompilationTask

```java
public abstract class
JavacTask

extends
Object

implements
JavaCompiler.CompilationTask
```

Provides access to functionality specific to the JDK Java Compiler, javac.

**Since:** 1.6

public abstract class

JavacTask

extends

Object

implements

JavaCompiler.CompilationTask

Provides access to functionality specific to the JDK Java Compiler, javac.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JavacTask

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

addTaskListener

​(

TaskListener

taskListener)

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

abstract

Iterable

<? extends

Element

>

analyze

()

Completes all analysis.

abstract

Iterable

<? extends

JavaFileObject

>

generate

()

Generates code.

abstract

Elements

getElements

()

Returns a utility object for dealing with program elements.

abstract

TypeMirror

getTypeMirror

​(

Iterable

<? extends

Tree

> path)

Returns a type mirror of the tree node determined by the specified path.

abstract

Types

getTypes

()

Returns a utility object for dealing with type mirrors.

static

JavacTask

instance

​(

ProcessingEnvironment

processingEnvironment)

Returns the

JavacTask

for a

ProcessingEnvironment

.

abstract

Iterable

<? extends

CompilationUnitTree

>

parse

()

Parses the specified files returning a list of abstract syntax trees.

abstract void

removeTaskListener

​(

TaskListener

taskListener)

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

abstract void

setTaskListener

​(

TaskListener

taskListener)

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

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

- Methods declared in interface javax.tools.

JavaCompiler.CompilationTask

addModules

,

call

,

setLocale

,

setProcessors

Constructor Summary

Constructors

Constructor

Description

JavacTask

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

addTaskListener

​(

TaskListener

taskListener)

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

abstract

Iterable

<? extends

Element

>

analyze

()

Completes all analysis.

abstract

Iterable

<? extends

JavaFileObject

>

generate

()

Generates code.

abstract

Elements

getElements

()

Returns a utility object for dealing with program elements.

abstract

TypeMirror

getTypeMirror

​(

Iterable

<? extends

Tree

> path)

Returns a type mirror of the tree node determined by the specified path.

abstract

Types

getTypes

()

Returns a utility object for dealing with type mirrors.

static

JavacTask

instance

​(

ProcessingEnvironment

processingEnvironment)

Returns the

JavacTask

for a

ProcessingEnvironment

.

abstract

Iterable

<? extends

CompilationUnitTree

>

parse

()

Parses the specified files returning a list of abstract syntax trees.

abstract void

removeTaskListener

​(

TaskListener

taskListener)

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

abstract void

setTaskListener

​(

TaskListener

taskListener)

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

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

- Methods declared in interface javax.tools.

JavaCompiler.CompilationTask

addModules

,

call

,

setLocale

,

setProcessors

---

#### Method Summary

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

Completes all analysis.

Generates code.

Returns a utility object for dealing with program elements.

Returns a type mirror of the tree node determined by the specified path.

Returns a utility object for dealing with type mirrors.

Returns the

JavacTask

for a

ProcessingEnvironment

.

Parses the specified files returning a list of abstract syntax trees.

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

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

Methods declared in interface javax.tools.

JavaCompiler.CompilationTask

addModules

,

call

,

setLocale

,

setProcessors

---

#### Methods declared in interface javax.tools. JavaCompiler.CompilationTask

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JavacTask

```java
public JavacTask()
```

============ METHOD DETAIL ==========

- Method Detail

- instance

```java
public static
JavacTask
instance​(
ProcessingEnvironment
processingEnvironment)
```

Returns the

JavacTask

for a

ProcessingEnvironment

.
If the compiler is being invoked using a

CompilationTask

,
then that task will be returned.

**Parameters:** processingEnvironment

- the processing environment
**Returns:** the

JavacTask

for a

ProcessingEnvironment
**Since:** 1.8

- parse

```java
public abstract
Iterable
<? extends
CompilationUnitTree
> parse()
throws
IOException
```

Parses the specified files returning a list of abstract syntax trees.

**Returns:** a list of abstract syntax trees
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

- analyze

```java
public abstract
Iterable
<? extends
Element
> analyze()
throws
IOException
```

Completes all analysis.

**Returns:** a list of elements that were analyzed
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

- generate

```java
public abstract
Iterable
<? extends
JavaFileObject
> generate()
throws
IOException
```

Generates code.

**Returns:** a list of files that were generated
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

- setTaskListener

```java
public abstract void setTaskListener​(
TaskListener
taskListener)
```

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

If another listener is receiving notifications as a result of a prior
call of this method, then that listener will no longer receive notifications.

Informally, this method is equivalent to calling

removeTaskListener

for
any listener that has been previously set, followed by

addTaskListener

for the new listener.

**Parameters:** taskListener

- the task listener
**Throws:** IllegalStateException

- if the specified listener has already been added.

- addTaskListener

```java
public abstract void addTaskListener​(
TaskListener
taskListener)
```

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

This method may be called at any time before or during the compilation.

**Parameters:** taskListener

- the task listener
**Throws:** IllegalStateException

- if the specified listener has already been added.
**Since:** 1.8

- removeTaskListener

```java
public abstract void removeTaskListener​(
TaskListener
taskListener)
```

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

This method may be called at any time before or during the compilation.

**Parameters:** taskListener

- the task listener
**Since:** 1.8

- getTypeMirror

```java
public abstract
TypeMirror
getTypeMirror​(
Iterable
<? extends
Tree
> path)
```

Returns a type mirror of the tree node determined by the specified path.
This method has been superceded by methods on

Trees

.

**Parameters:** path

- the path
**Returns:** the type mirror
**See Also:** Trees.getTypeMirror(com.sun.source.util.TreePath)

- getElements

```java
public abstract
Elements
getElements()
```

Returns a utility object for dealing with program elements.

**Returns:** a utility object for dealing with program elements

- getTypes

```java
public abstract
Types
getTypes()
```

Returns a utility object for dealing with type mirrors.

**Returns:** the utility object for dealing with type mirrors

Constructor Detail

- JavacTask

```java
public JavacTask()
```

---

#### Constructor Detail

JavacTask

```java
public JavacTask()
```

---

#### JavacTask

public JavacTask()

Method Detail

- instance

```java
public static
JavacTask
instance​(
ProcessingEnvironment
processingEnvironment)
```

Returns the

JavacTask

for a

ProcessingEnvironment

.
If the compiler is being invoked using a

CompilationTask

,
then that task will be returned.

**Parameters:** processingEnvironment

- the processing environment
**Returns:** the

JavacTask

for a

ProcessingEnvironment
**Since:** 1.8

- parse

```java
public abstract
Iterable
<? extends
CompilationUnitTree
> parse()
throws
IOException
```

Parses the specified files returning a list of abstract syntax trees.

**Returns:** a list of abstract syntax trees
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

- analyze

```java
public abstract
Iterable
<? extends
Element
> analyze()
throws
IOException
```

Completes all analysis.

**Returns:** a list of elements that were analyzed
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

- generate

```java
public abstract
Iterable
<? extends
JavaFileObject
> generate()
throws
IOException
```

Generates code.

**Returns:** a list of files that were generated
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

- setTaskListener

```java
public abstract void setTaskListener​(
TaskListener
taskListener)
```

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

If another listener is receiving notifications as a result of a prior
call of this method, then that listener will no longer receive notifications.

Informally, this method is equivalent to calling

removeTaskListener

for
any listener that has been previously set, followed by

addTaskListener

for the new listener.

**Parameters:** taskListener

- the task listener
**Throws:** IllegalStateException

- if the specified listener has already been added.

- addTaskListener

```java
public abstract void addTaskListener​(
TaskListener
taskListener)
```

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

This method may be called at any time before or during the compilation.

**Parameters:** taskListener

- the task listener
**Throws:** IllegalStateException

- if the specified listener has already been added.
**Since:** 1.8

- removeTaskListener

```java
public abstract void removeTaskListener​(
TaskListener
taskListener)
```

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

This method may be called at any time before or during the compilation.

**Parameters:** taskListener

- the task listener
**Since:** 1.8

- getTypeMirror

```java
public abstract
TypeMirror
getTypeMirror​(
Iterable
<? extends
Tree
> path)
```

Returns a type mirror of the tree node determined by the specified path.
This method has been superceded by methods on

Trees

.

**Parameters:** path

- the path
**Returns:** the type mirror
**See Also:** Trees.getTypeMirror(com.sun.source.util.TreePath)

- getElements

```java
public abstract
Elements
getElements()
```

Returns a utility object for dealing with program elements.

**Returns:** a utility object for dealing with program elements

- getTypes

```java
public abstract
Types
getTypes()
```

Returns a utility object for dealing with type mirrors.

**Returns:** the utility object for dealing with type mirrors

---

#### Method Detail

instance

```java
public static
JavacTask
instance​(
ProcessingEnvironment
processingEnvironment)
```

Returns the

JavacTask

for a

ProcessingEnvironment

.
If the compiler is being invoked using a

CompilationTask

,
then that task will be returned.

**Parameters:** processingEnvironment

- the processing environment
**Returns:** the

JavacTask

for a

ProcessingEnvironment
**Since:** 1.8

---

#### instance

public static

JavacTask

instance​(

ProcessingEnvironment

processingEnvironment)

Returns the

JavacTask

for a

ProcessingEnvironment

.
If the compiler is being invoked using a

CompilationTask

,
then that task will be returned.

parse

```java
public abstract
Iterable
<? extends
CompilationUnitTree
> parse()
throws
IOException
```

Parses the specified files returning a list of abstract syntax trees.

**Returns:** a list of abstract syntax trees
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

---

#### parse

public abstract

Iterable

<? extends

CompilationUnitTree

> parse()
throws

IOException

Parses the specified files returning a list of abstract syntax trees.

analyze

```java
public abstract
Iterable
<? extends
Element
> analyze()
throws
IOException
```

Completes all analysis.

**Returns:** a list of elements that were analyzed
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

---

#### analyze

public abstract

Iterable

<? extends

Element

> analyze()
throws

IOException

Completes all analysis.

generate

```java
public abstract
Iterable
<? extends
JavaFileObject
> generate()
throws
IOException
```

Generates code.

**Returns:** a list of files that were generated
**Throws:** IOException

- if an unhandled I/O error occurred in the compiler.
**Throws:** IllegalStateException

- if the operation cannot be performed at this time.

---

#### generate

public abstract

Iterable

<? extends

JavaFileObject

> generate()
throws

IOException

Generates code.

setTaskListener

```java
public abstract void setTaskListener​(
TaskListener
taskListener)
```

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

If another listener is receiving notifications as a result of a prior
call of this method, then that listener will no longer receive notifications.

Informally, this method is equivalent to calling

removeTaskListener

for
any listener that has been previously set, followed by

addTaskListener

for the new listener.

**Parameters:** taskListener

- the task listener
**Throws:** IllegalStateException

- if the specified listener has already been added.

---

#### setTaskListener

public abstract void setTaskListener​(

TaskListener

taskListener)

Sets a specified listener to receive notification of events
describing the progress of this compilation task.

If another listener is receiving notifications as a result of a prior
call of this method, then that listener will no longer receive notifications.

Informally, this method is equivalent to calling

removeTaskListener

for
any listener that has been previously set, followed by

addTaskListener

for the new listener.

addTaskListener

```java
public abstract void addTaskListener​(
TaskListener
taskListener)
```

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

This method may be called at any time before or during the compilation.

**Parameters:** taskListener

- the task listener
**Throws:** IllegalStateException

- if the specified listener has already been added.
**Since:** 1.8

---

#### addTaskListener

public abstract void addTaskListener​(

TaskListener

taskListener)

Adds a specified listener so that it receives notification of events
describing the progress of this compilation task.

This method may be called at any time before or during the compilation.

removeTaskListener

```java
public abstract void removeTaskListener​(
TaskListener
taskListener)
```

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

This method may be called at any time before or during the compilation.

**Parameters:** taskListener

- the task listener
**Since:** 1.8

---

#### removeTaskListener

public abstract void removeTaskListener​(

TaskListener

taskListener)

Removes the specified listener so that it no longer receives
notification of events describing the progress of this
compilation task.

This method may be called at any time before or during the compilation.

getTypeMirror

```java
public abstract
TypeMirror
getTypeMirror​(
Iterable
<? extends
Tree
> path)
```

Returns a type mirror of the tree node determined by the specified path.
This method has been superceded by methods on

Trees

.

**Parameters:** path

- the path
**Returns:** the type mirror
**See Also:** Trees.getTypeMirror(com.sun.source.util.TreePath)

---

#### getTypeMirror

public abstract

TypeMirror

getTypeMirror​(

Iterable

<? extends

Tree

> path)

Returns a type mirror of the tree node determined by the specified path.
This method has been superceded by methods on

Trees

.

getElements

```java
public abstract
Elements
getElements()
```

Returns a utility object for dealing with program elements.

**Returns:** a utility object for dealing with program elements

---

#### getElements

public abstract

Elements

getElements()

Returns a utility object for dealing with program elements.

getTypes

```java
public abstract
Types
getTypes()
```

Returns a utility object for dealing with type mirrors.

**Returns:** the utility object for dealing with type mirrors

---

#### getTypes

public abstract

Types

getTypes()

Returns a utility object for dealing with type mirrors.

---

