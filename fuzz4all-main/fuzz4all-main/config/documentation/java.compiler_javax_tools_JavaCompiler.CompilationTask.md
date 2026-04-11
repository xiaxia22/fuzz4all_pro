# Interface JavaCompiler.CompilationTask

**Source:** `java.compiler\javax\tools\JavaCompiler.CompilationTask.html`

### Class Description

```java
public static interface
JavaCompiler.CompilationTask

extends
Callable
<
Boolean
>
```

Interface representing a future for a compilation task. The
compilation task has not yet started. To start the task, call
the

call

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setProcessors

method.

**All Superinterfaces:** Callable

<

Boolean

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addModules​(
Iterable
<
String
> moduleNames)

Adds root modules to be taken into account during module
resolution.
Invalid module names may cause either

IllegalArgumentException

to be thrown,
or diagnostics to be reported when the task is started.

**Parameters:**
- moduleNames

- the names of the root modules

**Throws:**
- IllegalArgumentException

- may be thrown for some
invalid module names
- IllegalStateException

- if the task has started

**Since:**
- 9

---

#### void setProcessors​(
Iterable
<? extends
Processor
> processors)

Sets processors (for annotation processing). This will
bypass the normal discovery mechanism.

**Parameters:**
- processors

- processors (for annotation processing)

**Throws:**
- IllegalStateException

- if the task has started

---

#### void setLocale​(
Locale
locale)

Sets the locale to be applied when formatting diagnostics and
other localized data.

**Parameters:**
- locale

- the locale to apply;

null

means apply no
locale

**Throws:**
- IllegalStateException

- if the task has started

---

#### Boolean
call()

Performs this compilation task. The compilation may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

**Specified by:**
- call

in interface

Callable

<

Boolean

>

**Returns:**
- true if and only all the files compiled without errors;
false otherwise

**Throws:**
- RuntimeException

- if an unrecoverable error occurred
in a user-supplied component. The

cause

will be the error
in user code.
- IllegalStateException

- if called more than once

---

### Additional Sections

#### Interface JavaCompiler.CompilationTask

**All Superinterfaces:** Callable

<

Boolean

>

**All Known Implementing Classes:** JavacTask

**Enclosing interface:** JavaCompiler

```java
public static interface
JavaCompiler.CompilationTask

extends
Callable
<
Boolean
>
```

Interface representing a future for a compilation task. The
compilation task has not yet started. To start the task, call
the

call

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setProcessors

method.

public static interface

JavaCompiler.CompilationTask

extends

Callable

<

Boolean

>

Interface representing a future for a compilation task. The
compilation task has not yet started. To start the task, call
the

call

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setProcessors

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setProcessors

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addModules

​(

Iterable

<

String

> moduleNames)

Adds root modules to be taken into account during module
resolution.

Boolean

call

()

Performs this compilation task.

void

setLocale

​(

Locale

locale)

Sets the locale to be applied when formatting diagnostics and
other localized data.

void

setProcessors

​(

Iterable

<? extends

Processor

> processors)

Sets processors (for annotation processing).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addModules

​(

Iterable

<

String

> moduleNames)

Adds root modules to be taken into account during module
resolution.

Boolean

call

()

Performs this compilation task.

void

setLocale

​(

Locale

locale)

Sets the locale to be applied when formatting diagnostics and
other localized data.

void

setProcessors

​(

Iterable

<? extends

Processor

> processors)

Sets processors (for annotation processing).

---

#### Method Summary

Adds root modules to be taken into account during module
resolution.

Performs this compilation task.

Sets the locale to be applied when formatting diagnostics and
other localized data.

Sets processors (for annotation processing).

============ METHOD DETAIL ==========

- Method Detail

- addModules

```java
void addModules​(
Iterable
<
String
> moduleNames)
```

Adds root modules to be taken into account during module
resolution.
Invalid module names may cause either

IllegalArgumentException

to be thrown,
or diagnostics to be reported when the task is started.

**Parameters:** moduleNames

- the names of the root modules
**Throws:** IllegalArgumentException

- may be thrown for some
invalid module names
**Throws:** IllegalStateException

- if the task has started
**Since:** 9

- setProcessors

```java
void setProcessors​(
Iterable
<? extends
Processor
> processors)
```

Sets processors (for annotation processing). This will
bypass the normal discovery mechanism.

**Parameters:** processors

- processors (for annotation processing)
**Throws:** IllegalStateException

- if the task has started

- setLocale

```java
void setLocale​(
Locale
locale)
```

Sets the locale to be applied when formatting diagnostics and
other localized data.

**Parameters:** locale

- the locale to apply;

null

means apply no
locale
**Throws:** IllegalStateException

- if the task has started

- call

```java
Boolean
call()
```

Performs this compilation task. The compilation may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

**Specified by:** call

in interface

Callable

<

Boolean

>
**Returns:** true if and only all the files compiled without errors;
false otherwise
**Throws:** RuntimeException

- if an unrecoverable error occurred
in a user-supplied component. The

cause

will be the error
in user code.
**Throws:** IllegalStateException

- if called more than once

Method Detail

- addModules

```java
void addModules​(
Iterable
<
String
> moduleNames)
```

Adds root modules to be taken into account during module
resolution.
Invalid module names may cause either

IllegalArgumentException

to be thrown,
or diagnostics to be reported when the task is started.

**Parameters:** moduleNames

- the names of the root modules
**Throws:** IllegalArgumentException

- may be thrown for some
invalid module names
**Throws:** IllegalStateException

- if the task has started
**Since:** 9

- setProcessors

```java
void setProcessors​(
Iterable
<? extends
Processor
> processors)
```

Sets processors (for annotation processing). This will
bypass the normal discovery mechanism.

**Parameters:** processors

- processors (for annotation processing)
**Throws:** IllegalStateException

- if the task has started

- setLocale

```java
void setLocale​(
Locale
locale)
```

Sets the locale to be applied when formatting diagnostics and
other localized data.

**Parameters:** locale

- the locale to apply;

null

means apply no
locale
**Throws:** IllegalStateException

- if the task has started

- call

```java
Boolean
call()
```

Performs this compilation task. The compilation may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

**Specified by:** call

in interface

Callable

<

Boolean

>
**Returns:** true if and only all the files compiled without errors;
false otherwise
**Throws:** RuntimeException

- if an unrecoverable error occurred
in a user-supplied component. The

cause

will be the error
in user code.
**Throws:** IllegalStateException

- if called more than once

---

#### Method Detail

addModules

```java
void addModules​(
Iterable
<
String
> moduleNames)
```

Adds root modules to be taken into account during module
resolution.
Invalid module names may cause either

IllegalArgumentException

to be thrown,
or diagnostics to be reported when the task is started.

**Parameters:** moduleNames

- the names of the root modules
**Throws:** IllegalArgumentException

- may be thrown for some
invalid module names
**Throws:** IllegalStateException

- if the task has started
**Since:** 9

---

#### addModules

void addModules​(

Iterable

<

String

> moduleNames)

Adds root modules to be taken into account during module
resolution.
Invalid module names may cause either

IllegalArgumentException

to be thrown,
or diagnostics to be reported when the task is started.

setProcessors

```java
void setProcessors​(
Iterable
<? extends
Processor
> processors)
```

Sets processors (for annotation processing). This will
bypass the normal discovery mechanism.

**Parameters:** processors

- processors (for annotation processing)
**Throws:** IllegalStateException

- if the task has started

---

#### setProcessors

void setProcessors​(

Iterable

<? extends

Processor

> processors)

Sets processors (for annotation processing). This will
bypass the normal discovery mechanism.

setLocale

```java
void setLocale​(
Locale
locale)
```

Sets the locale to be applied when formatting diagnostics and
other localized data.

**Parameters:** locale

- the locale to apply;

null

means apply no
locale
**Throws:** IllegalStateException

- if the task has started

---

#### setLocale

void setLocale​(

Locale

locale)

Sets the locale to be applied when formatting diagnostics and
other localized data.

call

```java
Boolean
call()
```

Performs this compilation task. The compilation may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

**Specified by:** call

in interface

Callable

<

Boolean

>
**Returns:** true if and only all the files compiled without errors;
false otherwise
**Throws:** RuntimeException

- if an unrecoverable error occurred
in a user-supplied component. The

cause

will be the error
in user code.
**Throws:** IllegalStateException

- if called more than once

---

#### call

Boolean

call()

Performs this compilation task. The compilation may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

---

