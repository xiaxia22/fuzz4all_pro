# Interface ToolProvider

**Source:** `java.base\java\util\spi\ToolProvider.html`

### Class Description

```java
public interface
ToolProvider
```

An interface for command-line tools to provide a way to
be invoked without necessarily starting a new VM.

Tool providers are normally located using the service-provider
loading facility defined by

ServiceLoader

.
Each provider must provide a name, and a method to run
an instance of the corresponding tool. When a tool is run,
it will be provided with an array of string arguments, and a
pair of streams: one for normal (or expected) output and the other
for reporting any errors that may occur.
The interpretation of the string arguments will normally be defined by
each individual tool provider, but will generally correspond to the
arguments that could be provided to the tool when invoking the tool
from the command line.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the name of this tool provider.

**Returns:**
- the name of this tool provider

**API Note:**
- It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".

---

#### int run​(
PrintWriter
out,

PrintWriter
err,

String
... args)

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**Parameters:**
- out

- a stream to which "expected" output should be written
- err

- a stream to which any error messages should be written
- args

- the command-line arguments for the tool

**Returns:**
- the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.

**Throws:**
- NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

**API Note:**
- The interpretation of the arguments will be specific to
each tool.

---

#### default int run​(
PrintStream
out,

PrintStream
err,

String
... args)

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**Parameters:**
- out

- a stream to which "expected" output should be written
- err

- a stream to which any error messages should be written
- args

- the command-line arguments for the tool

**Returns:**
- the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.

**Throws:**
- NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

**API Note:**
- The interpretation of the arguments will be specific to
each tool.

**Implementation Note:**
- This implementation wraps the

out

and

err

streams within

PrintWriter

s, and then calls

run(PrintWriter, PrintWriter, String[])

.

---

#### static
Optional
<
ToolProvider
> findFirst​(
String
name)

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

**Parameters:**
- name

- the name of the desired tool provider

**Returns:**
- an

Optional<ToolProvider>

of the first instance found

**Throws:**
- NullPointerException

- if

name

is

null

---

### Additional Sections

#### Interface ToolProvider

```java
public interface
ToolProvider
```

An interface for command-line tools to provide a way to
be invoked without necessarily starting a new VM.

Tool providers are normally located using the service-provider
loading facility defined by

ServiceLoader

.
Each provider must provide a name, and a method to run
an instance of the corresponding tool. When a tool is run,
it will be provided with an array of string arguments, and a
pair of streams: one for normal (or expected) output and the other
for reporting any errors that may occur.
The interpretation of the string arguments will normally be defined by
each individual tool provider, but will generally correspond to the
arguments that could be provided to the tool when invoking the tool
from the command line.

**Since:** 9

public interface

ToolProvider

An interface for command-line tools to provide a way to
be invoked without necessarily starting a new VM.

Tool providers are normally located using the service-provider
loading facility defined by

ServiceLoader

.
Each provider must provide a name, and a method to run
an instance of the corresponding tool. When a tool is run,
it will be provided with an array of string arguments, and a
pair of streams: one for normal (or expected) output and the other
for reporting any errors that may occur.
The interpretation of the string arguments will normally be defined by
each individual tool provider, but will generally correspond to the
arguments that could be provided to the tool when invoking the tool
from the command line.

Tool providers are normally located using the service-provider
loading facility defined by

ServiceLoader

.
Each provider must provide a name, and a method to run
an instance of the corresponding tool. When a tool is run,
it will be provided with an array of string arguments, and a
pair of streams: one for normal (or expected) output and the other
for reporting any errors that may occur.
The interpretation of the string arguments will normally be defined by
each individual tool provider, but will generally correspond to the
arguments that could be provided to the tool when invoking the tool
from the command line.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

static

Optional

<

ToolProvider

>

findFirst

​(

String

name)

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

String

name

()

Returns the name of this tool provider.

default int

run

​(

PrintStream

out,

PrintStream

err,

String

... args)

Runs an instance of the tool, returning zero for a successful run.

int

run

​(

PrintWriter

out,

PrintWriter

err,

String

... args)

Runs an instance of the tool, returning zero for a successful run.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

static

Optional

<

ToolProvider

>

findFirst

​(

String

name)

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

String

name

()

Returns the name of this tool provider.

default int

run

​(

PrintStream

out,

PrintStream

err,

String

... args)

Runs an instance of the tool, returning zero for a successful run.

int

run

​(

PrintWriter

out,

PrintWriter

err,

String

... args)

Runs an instance of the tool, returning zero for a successful run.

---

#### Method Summary

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

Returns the name of this tool provider.

Runs an instance of the tool, returning zero for a successful run.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of this tool provider.

**API Note:** It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".
**Returns:** the name of this tool provider

- run

```java
int run​(
PrintWriter
out,

PrintWriter
err,

String
... args)
```

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**API Note:** The interpretation of the arguments will be specific to
each tool.
**Parameters:** out

- a stream to which "expected" output should be written
**Parameters:** err

- a stream to which any error messages should be written
**Parameters:** args

- the command-line arguments for the tool
**Returns:** the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.
**Throws:** NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

- run

```java
default int run​(
PrintStream
out,

PrintStream
err,

String
... args)
```

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**API Note:** The interpretation of the arguments will be specific to
each tool.
**Implementation Note:** This implementation wraps the

out

and

err

streams within

PrintWriter

s, and then calls

run(PrintWriter, PrintWriter, String[])

.
**Parameters:** out

- a stream to which "expected" output should be written
**Parameters:** err

- a stream to which any error messages should be written
**Parameters:** args

- the command-line arguments for the tool
**Returns:** the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.
**Throws:** NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

- findFirst

```java
static
Optional
<
ToolProvider
> findFirst​(
String
name)
```

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

**Parameters:** name

- the name of the desired tool provider
**Returns:** an

Optional<ToolProvider>

of the first instance found
**Throws:** NullPointerException

- if

name

is

null

Method Detail

- name

```java
String
name()
```

Returns the name of this tool provider.

**API Note:** It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".
**Returns:** the name of this tool provider

- run

```java
int run​(
PrintWriter
out,

PrintWriter
err,

String
... args)
```

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**API Note:** The interpretation of the arguments will be specific to
each tool.
**Parameters:** out

- a stream to which "expected" output should be written
**Parameters:** err

- a stream to which any error messages should be written
**Parameters:** args

- the command-line arguments for the tool
**Returns:** the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.
**Throws:** NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

- run

```java
default int run​(
PrintStream
out,

PrintStream
err,

String
... args)
```

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**API Note:** The interpretation of the arguments will be specific to
each tool.
**Implementation Note:** This implementation wraps the

out

and

err

streams within

PrintWriter

s, and then calls

run(PrintWriter, PrintWriter, String[])

.
**Parameters:** out

- a stream to which "expected" output should be written
**Parameters:** err

- a stream to which any error messages should be written
**Parameters:** args

- the command-line arguments for the tool
**Returns:** the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.
**Throws:** NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

- findFirst

```java
static
Optional
<
ToolProvider
> findFirst​(
String
name)
```

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

**Parameters:** name

- the name of the desired tool provider
**Returns:** an

Optional<ToolProvider>

of the first instance found
**Throws:** NullPointerException

- if

name

is

null

---

#### Method Detail

name

```java
String
name()
```

Returns the name of this tool provider.

**API Note:** It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".
**Returns:** the name of this tool provider

---

#### name

String

name()

Returns the name of this tool provider.

run

```java
int run​(
PrintWriter
out,

PrintWriter
err,

String
... args)
```

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**API Note:** The interpretation of the arguments will be specific to
each tool.
**Parameters:** out

- a stream to which "expected" output should be written
**Parameters:** err

- a stream to which any error messages should be written
**Parameters:** args

- the command-line arguments for the tool
**Returns:** the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.
**Throws:** NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

---

#### run

int run​(

PrintWriter

out,

PrintWriter

err,

String

... args)

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

run

```java
default int run​(
PrintStream
out,

PrintStream
err,

String
... args)
```

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

**API Note:** The interpretation of the arguments will be specific to
each tool.
**Implementation Note:** This implementation wraps the

out

and

err

streams within

PrintWriter

s, and then calls

run(PrintWriter, PrintWriter, String[])

.
**Parameters:** out

- a stream to which "expected" output should be written
**Parameters:** err

- a stream to which any error messages should be written
**Parameters:** args

- the command-line arguments for the tool
**Returns:** the result of executing the tool.
A return value of 0 means the tool did not encounter any errors;
any other value indicates that at least one error occurred
during execution.
**Throws:** NullPointerException

- if any of the arguments are

null

,
or if there are any

null

values in the

args

array

---

#### run

default int run​(

PrintStream

out,

PrintStream

err,

String

... args)

Runs an instance of the tool, returning zero for a successful run.
Any non-zero return value indicates a tool-specific error during the
execution.

Two streams should be provided, for "expected" output, and for any
error messages. If it is not necessary to distinguish the output,
the same stream may be used for both.

findFirst

```java
static
Optional
<
ToolProvider
> findFirst​(
String
name)
```

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

**Parameters:** name

- the name of the desired tool provider
**Returns:** an

Optional<ToolProvider>

of the first instance found
**Throws:** NullPointerException

- if

name

is

null

---

#### findFirst

static

Optional

<

ToolProvider

> findFirst​(

String

name)

Returns the first instance of a

ToolProvider

with the given name,
as loaded by

ServiceLoader

using the system class loader.

---

