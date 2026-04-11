# Interface DocumentationTool

**Source:** `java.compiler\javax\tools\DocumentationTool.html`

### Class Description

```java
public interface
DocumentationTool

extends
Tool
,
OptionChecker
```

Interface to invoke Java™ programming language documentation tools from
programs.

**All Superinterfaces:** OptionChecker

,

Tool

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DocumentationTool.DocumentationTask
getTask​(
Writer
out,

JavaFileManager
fileManager,

DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Class
<?> docletClass,

Iterable
<
String
> options,

Iterable
<? extends
JavaFileObject
> compilationUnits)

Creates a future for a documentation task with the given
components and arguments. The task might not have
completed as described in the DocumentationTask interface.

If a file manager is provided, it must be able to handle all
locations defined in

DocumentationTool.Location

,
as well as

StandardLocation.SOURCE_PATH

,

StandardLocation.CLASS_PATH

, and

StandardLocation.PLATFORM_CLASS_PATH

.

**Parameters:**
- out

- a Writer for additional output from the tool;
use

System.err

if

null
- fileManager

- a file manager; if

null

use the
tool's standard filemanager
- diagnosticListener

- a diagnostic listener; if

null

use the tool's default method for reporting diagnostics
- docletClass

- a class providing the necessary methods required
of a doclet; a value of

null

means to use the standard doclet.
- options

- documentation tool options and doclet options,

null

means no options
- compilationUnits

- the compilation units to compile,

null

means no compilation units

**Returns:**
- an object representing the compilation

**Throws:**
- RuntimeException

- if an unrecoverable error
occurred in a user supplied component. The

cause

will be the error in
user code.
- IllegalArgumentException

- if any of the given
compilation units are of other kind than

source

---

#### StandardJavaFileManager
getStandardFileManager​(
DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Locale
locale,

Charset
charset)

Returns a new instance of the standard file manager implementation
for this tool. The file manager will use the given diagnostic
listener for producing any non-fatal diagnostics. Fatal errors
will be signaled with the appropriate exceptions.

The standard file manager will be automatically reopened if
it is accessed after calls to

flush

or

close

.
The standard file manager must be usable with other tools.

**Parameters:**
- diagnosticListener

- a diagnostic listener for non-fatal
diagnostics; if

null

use the compiler's default method
for reporting diagnostics
- locale

- the locale to apply when formatting diagnostics;

null

means the

default locale

.
- charset

- the character set used for decoding bytes; if

null

use the platform default

**Returns:**
- the standard file manager

---

### Additional Sections

#### Interface DocumentationTool

**All Superinterfaces:** OptionChecker

,

Tool

```java
public interface
DocumentationTool

extends
Tool
,
OptionChecker
```

Interface to invoke Java™ programming language documentation tools from
programs.

**Since:** 1.8

public interface

DocumentationTool

extends

Tool

,

OptionChecker

Interface to invoke Java™ programming language documentation tools from
programs.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

DocumentationTool.DocumentationTask

Interface representing a future for a documentation task.

static class

DocumentationTool.Location

Locations specific to

DocumentationTool

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

StandardJavaFileManager

getStandardFileManager

​(

DiagnosticListener

<? super

JavaFileObject

> diagnosticListener,

Locale

locale,

Charset

charset)

Returns a new instance of the standard file manager implementation
for this tool.

DocumentationTool.DocumentationTask

getTask

​(

Writer

out,

JavaFileManager

fileManager,

DiagnosticListener

<? super

JavaFileObject

> diagnosticListener,

Class

<?> docletClass,

Iterable

<

String

> options,

Iterable

<? extends

JavaFileObject

> compilationUnits)

Creates a future for a documentation task with the given
components and arguments.

- Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

- Methods declared in interface javax.tools.

Tool

getSourceVersions

,

name

,

run

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

DocumentationTool.DocumentationTask

Interface representing a future for a documentation task.

static class

DocumentationTool.Location

Locations specific to

DocumentationTool

.

---

#### Nested Class Summary

Interface representing a future for a documentation task.

Locations specific to

DocumentationTool

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

StandardJavaFileManager

getStandardFileManager

​(

DiagnosticListener

<? super

JavaFileObject

> diagnosticListener,

Locale

locale,

Charset

charset)

Returns a new instance of the standard file manager implementation
for this tool.

DocumentationTool.DocumentationTask

getTask

​(

Writer

out,

JavaFileManager

fileManager,

DiagnosticListener

<? super

JavaFileObject

> diagnosticListener,

Class

<?> docletClass,

Iterable

<

String

> options,

Iterable

<? extends

JavaFileObject

> compilationUnits)

Creates a future for a documentation task with the given
components and arguments.

- Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

- Methods declared in interface javax.tools.

Tool

getSourceVersions

,

name

,

run

---

#### Method Summary

Returns a new instance of the standard file manager implementation
for this tool.

Creates a future for a documentation task with the given
components and arguments.

Methods declared in interface javax.tools.

OptionChecker

isSupportedOption

---

#### Methods declared in interface javax.tools. OptionChecker

Methods declared in interface javax.tools.

Tool

getSourceVersions

,

name

,

run

---

#### Methods declared in interface javax.tools. Tool

============ METHOD DETAIL ==========

- Method Detail

- getTask

```java
DocumentationTool.DocumentationTask
getTask​(
Writer
out,

JavaFileManager
fileManager,

DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Class
<?> docletClass,

Iterable
<
String
> options,

Iterable
<? extends
JavaFileObject
> compilationUnits)
```

Creates a future for a documentation task with the given
components and arguments. The task might not have
completed as described in the DocumentationTask interface.

If a file manager is provided, it must be able to handle all
locations defined in

DocumentationTool.Location

,
as well as

StandardLocation.SOURCE_PATH

,

StandardLocation.CLASS_PATH

, and

StandardLocation.PLATFORM_CLASS_PATH

.

**Parameters:** out

- a Writer for additional output from the tool;
use

System.err

if

null
**Parameters:** fileManager

- a file manager; if

null

use the
tool's standard filemanager
**Parameters:** diagnosticListener

- a diagnostic listener; if

null

use the tool's default method for reporting diagnostics
**Parameters:** docletClass

- a class providing the necessary methods required
of a doclet; a value of

null

means to use the standard doclet.
**Parameters:** options

- documentation tool options and doclet options,

null

means no options
**Parameters:** compilationUnits

- the compilation units to compile,

null

means no compilation units
**Returns:** an object representing the compilation
**Throws:** RuntimeException

- if an unrecoverable error
occurred in a user supplied component. The

cause

will be the error in
user code.
**Throws:** IllegalArgumentException

- if any of the given
compilation units are of other kind than

source

- getStandardFileManager

```java
StandardJavaFileManager
getStandardFileManager​(
DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Locale
locale,

Charset
charset)
```

Returns a new instance of the standard file manager implementation
for this tool. The file manager will use the given diagnostic
listener for producing any non-fatal diagnostics. Fatal errors
will be signaled with the appropriate exceptions.

The standard file manager will be automatically reopened if
it is accessed after calls to

flush

or

close

.
The standard file manager must be usable with other tools.

**Parameters:** diagnosticListener

- a diagnostic listener for non-fatal
diagnostics; if

null

use the compiler's default method
for reporting diagnostics
**Parameters:** locale

- the locale to apply when formatting diagnostics;

null

means the

default locale

.
**Parameters:** charset

- the character set used for decoding bytes; if

null

use the platform default
**Returns:** the standard file manager

Method Detail

- getTask

```java
DocumentationTool.DocumentationTask
getTask​(
Writer
out,

JavaFileManager
fileManager,

DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Class
<?> docletClass,

Iterable
<
String
> options,

Iterable
<? extends
JavaFileObject
> compilationUnits)
```

Creates a future for a documentation task with the given
components and arguments. The task might not have
completed as described in the DocumentationTask interface.

If a file manager is provided, it must be able to handle all
locations defined in

DocumentationTool.Location

,
as well as

StandardLocation.SOURCE_PATH

,

StandardLocation.CLASS_PATH

, and

StandardLocation.PLATFORM_CLASS_PATH

.

**Parameters:** out

- a Writer for additional output from the tool;
use

System.err

if

null
**Parameters:** fileManager

- a file manager; if

null

use the
tool's standard filemanager
**Parameters:** diagnosticListener

- a diagnostic listener; if

null

use the tool's default method for reporting diagnostics
**Parameters:** docletClass

- a class providing the necessary methods required
of a doclet; a value of

null

means to use the standard doclet.
**Parameters:** options

- documentation tool options and doclet options,

null

means no options
**Parameters:** compilationUnits

- the compilation units to compile,

null

means no compilation units
**Returns:** an object representing the compilation
**Throws:** RuntimeException

- if an unrecoverable error
occurred in a user supplied component. The

cause

will be the error in
user code.
**Throws:** IllegalArgumentException

- if any of the given
compilation units are of other kind than

source

- getStandardFileManager

```java
StandardJavaFileManager
getStandardFileManager​(
DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Locale
locale,

Charset
charset)
```

Returns a new instance of the standard file manager implementation
for this tool. The file manager will use the given diagnostic
listener for producing any non-fatal diagnostics. Fatal errors
will be signaled with the appropriate exceptions.

The standard file manager will be automatically reopened if
it is accessed after calls to

flush

or

close

.
The standard file manager must be usable with other tools.

**Parameters:** diagnosticListener

- a diagnostic listener for non-fatal
diagnostics; if

null

use the compiler's default method
for reporting diagnostics
**Parameters:** locale

- the locale to apply when formatting diagnostics;

null

means the

default locale

.
**Parameters:** charset

- the character set used for decoding bytes; if

null

use the platform default
**Returns:** the standard file manager

---

#### Method Detail

getTask

```java
DocumentationTool.DocumentationTask
getTask​(
Writer
out,

JavaFileManager
fileManager,

DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Class
<?> docletClass,

Iterable
<
String
> options,

Iterable
<? extends
JavaFileObject
> compilationUnits)
```

Creates a future for a documentation task with the given
components and arguments. The task might not have
completed as described in the DocumentationTask interface.

If a file manager is provided, it must be able to handle all
locations defined in

DocumentationTool.Location

,
as well as

StandardLocation.SOURCE_PATH

,

StandardLocation.CLASS_PATH

, and

StandardLocation.PLATFORM_CLASS_PATH

.

**Parameters:** out

- a Writer for additional output from the tool;
use

System.err

if

null
**Parameters:** fileManager

- a file manager; if

null

use the
tool's standard filemanager
**Parameters:** diagnosticListener

- a diagnostic listener; if

null

use the tool's default method for reporting diagnostics
**Parameters:** docletClass

- a class providing the necessary methods required
of a doclet; a value of

null

means to use the standard doclet.
**Parameters:** options

- documentation tool options and doclet options,

null

means no options
**Parameters:** compilationUnits

- the compilation units to compile,

null

means no compilation units
**Returns:** an object representing the compilation
**Throws:** RuntimeException

- if an unrecoverable error
occurred in a user supplied component. The

cause

will be the error in
user code.
**Throws:** IllegalArgumentException

- if any of the given
compilation units are of other kind than

source

---

#### getTask

DocumentationTool.DocumentationTask

getTask​(

Writer

out,

JavaFileManager

fileManager,

DiagnosticListener

<? super

JavaFileObject

> diagnosticListener,

Class

<?> docletClass,

Iterable

<

String

> options,

Iterable

<? extends

JavaFileObject

> compilationUnits)

Creates a future for a documentation task with the given
components and arguments. The task might not have
completed as described in the DocumentationTask interface.

If a file manager is provided, it must be able to handle all
locations defined in

DocumentationTool.Location

,
as well as

StandardLocation.SOURCE_PATH

,

StandardLocation.CLASS_PATH

, and

StandardLocation.PLATFORM_CLASS_PATH

.

If a file manager is provided, it must be able to handle all
locations defined in

DocumentationTool.Location

,
as well as

StandardLocation.SOURCE_PATH

,

StandardLocation.CLASS_PATH

, and

StandardLocation.PLATFORM_CLASS_PATH

.

getStandardFileManager

```java
StandardJavaFileManager
getStandardFileManager​(
DiagnosticListener
<? super
JavaFileObject
> diagnosticListener,

Locale
locale,

Charset
charset)
```

Returns a new instance of the standard file manager implementation
for this tool. The file manager will use the given diagnostic
listener for producing any non-fatal diagnostics. Fatal errors
will be signaled with the appropriate exceptions.

The standard file manager will be automatically reopened if
it is accessed after calls to

flush

or

close

.
The standard file manager must be usable with other tools.

**Parameters:** diagnosticListener

- a diagnostic listener for non-fatal
diagnostics; if

null

use the compiler's default method
for reporting diagnostics
**Parameters:** locale

- the locale to apply when formatting diagnostics;

null

means the

default locale

.
**Parameters:** charset

- the character set used for decoding bytes; if

null

use the platform default
**Returns:** the standard file manager

---

#### getStandardFileManager

StandardJavaFileManager

getStandardFileManager​(

DiagnosticListener

<? super

JavaFileObject

> diagnosticListener,

Locale

locale,

Charset

charset)

Returns a new instance of the standard file manager implementation
for this tool. The file manager will use the given diagnostic
listener for producing any non-fatal diagnostics. Fatal errors
will be signaled with the appropriate exceptions.

The standard file manager will be automatically reopened if
it is accessed after calls to

flush

or

close

.
The standard file manager must be usable with other tools.

The standard file manager will be automatically reopened if
it is accessed after calls to

flush

or

close

.
The standard file manager must be usable with other tools.

---

