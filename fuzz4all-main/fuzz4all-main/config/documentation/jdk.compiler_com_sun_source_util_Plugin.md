# Interface Plugin

**Source:** `jdk.compiler\com\sun\source\util\Plugin.html`

### Class Description

```java
public interface
Plugin
```

The interface for a javac plug-in.

The javac plug-in mechanism allows a user to specify one or more plug-ins
on the javac command line, to be started soon after the compilation
has begun. Plug-ins are identified by a user-friendly name. Each plug-in that
is started will be passed an array of strings, which may be used to
provide the plug-in with values for any desired options or other arguments.

Plug-ins are located via a

ServiceLoader

,
using the same class path as annotation processors (i.e.

ANNOTATION_PROCESSOR_PATH

or

-processorpath

).

It is expected that a typical plug-in will simply register a

TaskListener

to be informed of events during the execution
of the compilation, and that the rest of the work will be done
by the task listener.

**Since:** 1.8

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the user-friendly name of this plug-in.

**Returns:**
- the user-friendly name of the plug-in

---

#### void init​(
JavacTask
task,

String
... args)

Initializes the plug-in for a given compilation task.

**Parameters:**
- task

- The compilation task that has just been started
- args

- Arguments, if any, for the plug-in

---

### Additional Sections

#### Interface Plugin

```java
public interface
Plugin
```

The interface for a javac plug-in.

The javac plug-in mechanism allows a user to specify one or more plug-ins
on the javac command line, to be started soon after the compilation
has begun. Plug-ins are identified by a user-friendly name. Each plug-in that
is started will be passed an array of strings, which may be used to
provide the plug-in with values for any desired options or other arguments.

Plug-ins are located via a

ServiceLoader

,
using the same class path as annotation processors (i.e.

ANNOTATION_PROCESSOR_PATH

or

-processorpath

).

It is expected that a typical plug-in will simply register a

TaskListener

to be informed of events during the execution
of the compilation, and that the rest of the work will be done
by the task listener.

**Since:** 1.8

public interface

Plugin

The interface for a javac plug-in.

The javac plug-in mechanism allows a user to specify one or more plug-ins
on the javac command line, to be started soon after the compilation
has begun. Plug-ins are identified by a user-friendly name. Each plug-in that
is started will be passed an array of strings, which may be used to
provide the plug-in with values for any desired options or other arguments.

Plug-ins are located via a

ServiceLoader

,
using the same class path as annotation processors (i.e.

ANNOTATION_PROCESSOR_PATH

or

-processorpath

).

It is expected that a typical plug-in will simply register a

TaskListener

to be informed of events during the execution
of the compilation, and that the rest of the work will be done
by the task listener.

The javac plug-in mechanism allows a user to specify one or more plug-ins
on the javac command line, to be started soon after the compilation
has begun. Plug-ins are identified by a user-friendly name. Each plug-in that
is started will be passed an array of strings, which may be used to
provide the plug-in with values for any desired options or other arguments.

Plug-ins are located via a

ServiceLoader

,
using the same class path as annotation processors (i.e.

ANNOTATION_PROCESSOR_PATH

or

-processorpath

).

It is expected that a typical plug-in will simply register a

TaskListener

to be informed of events during the execution
of the compilation, and that the rest of the work will be done
by the task listener.

Plug-ins are located via a

ServiceLoader

,
using the same class path as annotation processors (i.e.

ANNOTATION_PROCESSOR_PATH

or

-processorpath

).

It is expected that a typical plug-in will simply register a

TaskListener

to be informed of events during the execution
of the compilation, and that the rest of the work will be done
by the task listener.

It is expected that a typical plug-in will simply register a

TaskListener

to be informed of events during the execution
of the compilation, and that the rest of the work will be done
by the task listener.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the user-friendly name of this plug-in.

void

init

​(

JavacTask

task,

String

... args)

Initializes the plug-in for a given compilation task.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the user-friendly name of this plug-in.

void

init

​(

JavacTask

task,

String

... args)

Initializes the plug-in for a given compilation task.

---

#### Method Summary

Returns the user-friendly name of this plug-in.

Initializes the plug-in for a given compilation task.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the user-friendly name of this plug-in.

**Returns:** the user-friendly name of the plug-in

- init

```java
void init​(
JavacTask
task,

String
... args)
```

Initializes the plug-in for a given compilation task.

**Parameters:** task

- The compilation task that has just been started
**Parameters:** args

- Arguments, if any, for the plug-in

Method Detail

- getName

```java
String
getName()
```

Returns the user-friendly name of this plug-in.

**Returns:** the user-friendly name of the plug-in

- init

```java
void init​(
JavacTask
task,

String
... args)
```

Initializes the plug-in for a given compilation task.

**Parameters:** task

- The compilation task that has just been started
**Parameters:** args

- Arguments, if any, for the plug-in

---

#### Method Detail

getName

```java
String
getName()
```

Returns the user-friendly name of this plug-in.

**Returns:** the user-friendly name of the plug-in

---

#### getName

String

getName()

Returns the user-friendly name of this plug-in.

init

```java
void init​(
JavacTask
task,

String
... args)
```

Initializes the plug-in for a given compilation task.

**Parameters:** task

- The compilation task that has just been started
**Parameters:** args

- Arguments, if any, for the plug-in

---

#### init

void init​(

JavacTask

task,

String

... args)

Initializes the plug-in for a given compilation task.

---

