# Interface DocumentationTool.DocumentationTask

**Source:** `java.compiler\javax\tools\DocumentationTool.DocumentationTask.html`

### Class Description

```java
public static interface
DocumentationTool.DocumentationTask

extends
Callable
<
Boolean
>
```

Interface representing a future for a documentation task. The
task has not yet started. To start the task, call
the

call

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setLocale

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

Performs this documentation task. The task may only
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
- true if and only all the files were processed without errors;
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

#### Interface DocumentationTool.DocumentationTask

**All Superinterfaces:** Callable

<

Boolean

>

**Enclosing interface:** DocumentationTool

```java
public static interface
DocumentationTool.DocumentationTask

extends
Callable
<
Boolean
>
```

Interface representing a future for a documentation task. The
task has not yet started. To start the task, call
the

call

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setLocale

method.

public static interface

DocumentationTool.DocumentationTask

extends

Callable

<

Boolean

>

Interface representing a future for a documentation task. The
task has not yet started. To start the task, call
the

call

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setLocale

method.

Before calling the call method, additional aspects of the
task can be configured, for example, by calling the

setLocale

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

Performs this documentation task.

void

setLocale

​(

Locale

locale)

Sets the locale to be applied when formatting diagnostics and
other localized data.

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

Performs this documentation task.

void

setLocale

​(

Locale

locale)

Sets the locale to be applied when formatting diagnostics and
other localized data.

---

#### Method Summary

Adds root modules to be taken into account during module
resolution.

Performs this documentation task.

Sets the locale to be applied when formatting diagnostics and
other localized data.

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

Performs this documentation task. The task may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

**Specified by:** call

in interface

Callable

<

Boolean

>
**Returns:** true if and only all the files were processed without errors;
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

Performs this documentation task. The task may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

**Specified by:** call

in interface

Callable

<

Boolean

>
**Returns:** true if and only all the files were processed without errors;
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

Performs this documentation task. The task may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

**Specified by:** call

in interface

Callable

<

Boolean

>
**Returns:** true if and only all the files were processed without errors;
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

Performs this documentation task. The task may only
be performed once. Subsequent calls to this method throw
IllegalStateException.

---

