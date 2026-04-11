# Class TaskEvent

**Source:** `jdk.compiler\com\sun\source\util\TaskEvent.html`

### Class Description

```java
public final class
TaskEvent

extends
Object
```

Provides details about work that has been done by the JDK Java Compiler, javac.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public TaskEvent​(
TaskEvent.Kind
kind)

Creates a task event for a given kind.
The source file, compilation unit and type element
are all set to

null

.

**Parameters:**
- kind

- the kind of the event

---

#### public TaskEvent​(
TaskEvent.Kind
kind,

JavaFileObject
sourceFile)

Creates a task event for a given kind and source file.
The compilation unit and type element are both set to

null

.

**Parameters:**
- kind

- the kind of the event
- sourceFile

- the source file

---

#### public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit)

Creates a task event for a given kind and compilation unit.
The source file is set from the compilation unit,
and the type element is set to

null

.

**Parameters:**
- kind

- the kind of the event
- unit

- the compilation unit

---

#### public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit,

TypeElement
clazz)

Creates a task event for a given kind, compilation unit
and type element.
The source file is set from the compilation unit.

**Parameters:**
- kind

- the kind of the event
- unit

- the compilation unit
- clazz

- the type element

---

### Method Details

#### public
TaskEvent.Kind
getKind()

Returns the kind for this event.

**Returns:**
- the kind

---

#### public
JavaFileObject
getSourceFile()

Returns the source file for this event.
May be

null

.

**Returns:**
- the source file

---

#### public
CompilationUnitTree
getCompilationUnit()

Returns the compilation unit for this event.
May be

null

.

**Returns:**
- the compilation unit

---

#### public
TypeElement
getTypeElement()

Returns the type element for this event.
May be

null

.

**Returns:**
- the type element

---

### Additional Sections

#### Class TaskEvent

java.lang.Object

- com.sun.source.util.TaskEvent

com.sun.source.util.TaskEvent

```java
public final class
TaskEvent

extends
Object
```

Provides details about work that has been done by the JDK Java Compiler, javac.

**Since:** 1.6

public final class

TaskEvent

extends

Object

Provides details about work that has been done by the JDK Java Compiler, javac.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

TaskEvent.Kind

Kind of task event.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TaskEvent

​(

TaskEvent.Kind

kind)

Creates a task event for a given kind.

TaskEvent

​(

TaskEvent.Kind

kind,

CompilationUnitTree

unit)

Creates a task event for a given kind and compilation unit.

TaskEvent

​(

TaskEvent.Kind

kind,

CompilationUnitTree

unit,

TypeElement

clazz)

Creates a task event for a given kind, compilation unit
and type element.

TaskEvent

​(

TaskEvent.Kind

kind,

JavaFileObject

sourceFile)

Creates a task event for a given kind and source file.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CompilationUnitTree

getCompilationUnit

()

Returns the compilation unit for this event.

TaskEvent.Kind

getKind

()

Returns the kind for this event.

JavaFileObject

getSourceFile

()

Returns the source file for this event.

TypeElement

getTypeElement

()

Returns the type element for this event.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

TaskEvent.Kind

Kind of task event.

---

#### Nested Class Summary

Kind of task event.

Constructor Summary

Constructors

Constructor

Description

TaskEvent

​(

TaskEvent.Kind

kind)

Creates a task event for a given kind.

TaskEvent

​(

TaskEvent.Kind

kind,

CompilationUnitTree

unit)

Creates a task event for a given kind and compilation unit.

TaskEvent

​(

TaskEvent.Kind

kind,

CompilationUnitTree

unit,

TypeElement

clazz)

Creates a task event for a given kind, compilation unit
and type element.

TaskEvent

​(

TaskEvent.Kind

kind,

JavaFileObject

sourceFile)

Creates a task event for a given kind and source file.

---

#### Constructor Summary

Creates a task event for a given kind.

Creates a task event for a given kind and compilation unit.

Creates a task event for a given kind, compilation unit
and type element.

Creates a task event for a given kind and source file.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CompilationUnitTree

getCompilationUnit

()

Returns the compilation unit for this event.

TaskEvent.Kind

getKind

()

Returns the kind for this event.

JavaFileObject

getSourceFile

()

Returns the source file for this event.

TypeElement

getTypeElement

()

Returns the type element for this event.

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

Returns the compilation unit for this event.

Returns the kind for this event.

Returns the source file for this event.

Returns the type element for this event.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind)
```

Creates a task event for a given kind.
The source file, compilation unit and type element
are all set to

null

.

**Parameters:** kind

- the kind of the event

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

JavaFileObject
sourceFile)
```

Creates a task event for a given kind and source file.
The compilation unit and type element are both set to

null

.

**Parameters:** kind

- the kind of the event
**Parameters:** sourceFile

- the source file

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit)
```

Creates a task event for a given kind and compilation unit.
The source file is set from the compilation unit,
and the type element is set to

null

.

**Parameters:** kind

- the kind of the event
**Parameters:** unit

- the compilation unit

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit,

TypeElement
clazz)
```

Creates a task event for a given kind, compilation unit
and type element.
The source file is set from the compilation unit.

**Parameters:** kind

- the kind of the event
**Parameters:** unit

- the compilation unit
**Parameters:** clazz

- the type element

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
public
TaskEvent.Kind
getKind()
```

Returns the kind for this event.

**Returns:** the kind

- getSourceFile

```java
public
JavaFileObject
getSourceFile()
```

Returns the source file for this event.
May be

null

.

**Returns:** the source file

- getCompilationUnit

```java
public
CompilationUnitTree
getCompilationUnit()
```

Returns the compilation unit for this event.
May be

null

.

**Returns:** the compilation unit

- getTypeElement

```java
public
TypeElement
getTypeElement()
```

Returns the type element for this event.
May be

null

.

**Returns:** the type element

Constructor Detail

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind)
```

Creates a task event for a given kind.
The source file, compilation unit and type element
are all set to

null

.

**Parameters:** kind

- the kind of the event

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

JavaFileObject
sourceFile)
```

Creates a task event for a given kind and source file.
The compilation unit and type element are both set to

null

.

**Parameters:** kind

- the kind of the event
**Parameters:** sourceFile

- the source file

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit)
```

Creates a task event for a given kind and compilation unit.
The source file is set from the compilation unit,
and the type element is set to

null

.

**Parameters:** kind

- the kind of the event
**Parameters:** unit

- the compilation unit

- TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit,

TypeElement
clazz)
```

Creates a task event for a given kind, compilation unit
and type element.
The source file is set from the compilation unit.

**Parameters:** kind

- the kind of the event
**Parameters:** unit

- the compilation unit
**Parameters:** clazz

- the type element

---

#### Constructor Detail

TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind)
```

Creates a task event for a given kind.
The source file, compilation unit and type element
are all set to

null

.

**Parameters:** kind

- the kind of the event

---

#### TaskEvent

public TaskEvent​(

TaskEvent.Kind

kind)

Creates a task event for a given kind.
The source file, compilation unit and type element
are all set to

null

.

TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

JavaFileObject
sourceFile)
```

Creates a task event for a given kind and source file.
The compilation unit and type element are both set to

null

.

**Parameters:** kind

- the kind of the event
**Parameters:** sourceFile

- the source file

---

#### TaskEvent

public TaskEvent​(

TaskEvent.Kind

kind,

JavaFileObject

sourceFile)

Creates a task event for a given kind and source file.
The compilation unit and type element are both set to

null

.

TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit)
```

Creates a task event for a given kind and compilation unit.
The source file is set from the compilation unit,
and the type element is set to

null

.

**Parameters:** kind

- the kind of the event
**Parameters:** unit

- the compilation unit

---

#### TaskEvent

public TaskEvent​(

TaskEvent.Kind

kind,

CompilationUnitTree

unit)

Creates a task event for a given kind and compilation unit.
The source file is set from the compilation unit,
and the type element is set to

null

.

TaskEvent

```java
public TaskEvent​(
TaskEvent.Kind
kind,

CompilationUnitTree
unit,

TypeElement
clazz)
```

Creates a task event for a given kind, compilation unit
and type element.
The source file is set from the compilation unit.

**Parameters:** kind

- the kind of the event
**Parameters:** unit

- the compilation unit
**Parameters:** clazz

- the type element

---

#### TaskEvent

public TaskEvent​(

TaskEvent.Kind

kind,

CompilationUnitTree

unit,

TypeElement

clazz)

Creates a task event for a given kind, compilation unit
and type element.
The source file is set from the compilation unit.

Method Detail

- getKind

```java
public
TaskEvent.Kind
getKind()
```

Returns the kind for this event.

**Returns:** the kind

- getSourceFile

```java
public
JavaFileObject
getSourceFile()
```

Returns the source file for this event.
May be

null

.

**Returns:** the source file

- getCompilationUnit

```java
public
CompilationUnitTree
getCompilationUnit()
```

Returns the compilation unit for this event.
May be

null

.

**Returns:** the compilation unit

- getTypeElement

```java
public
TypeElement
getTypeElement()
```

Returns the type element for this event.
May be

null

.

**Returns:** the type element

---

#### Method Detail

getKind

```java
public
TaskEvent.Kind
getKind()
```

Returns the kind for this event.

**Returns:** the kind

---

#### getKind

public

TaskEvent.Kind

getKind()

Returns the kind for this event.

getSourceFile

```java
public
JavaFileObject
getSourceFile()
```

Returns the source file for this event.
May be

null

.

**Returns:** the source file

---

#### getSourceFile

public

JavaFileObject

getSourceFile()

Returns the source file for this event.
May be

null

.

getCompilationUnit

```java
public
CompilationUnitTree
getCompilationUnit()
```

Returns the compilation unit for this event.
May be

null

.

**Returns:** the compilation unit

---

#### getCompilationUnit

public

CompilationUnitTree

getCompilationUnit()

Returns the compilation unit for this event.
May be

null

.

getTypeElement

```java
public
TypeElement
getTypeElement()
```

Returns the type element for this event.
May be

null

.

**Returns:** the type element

---

#### getTypeElement

public

TypeElement

getTypeElement()

Returns the type element for this event.
May be

null

.

---

