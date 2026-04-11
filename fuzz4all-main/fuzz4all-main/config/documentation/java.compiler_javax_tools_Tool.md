# Interface Tool

**Source:** `java.compiler\javax\tools\Tool.html`

### Class Description

```java
public interface
Tool
```

Common interface for tools that can be invoked from a program.
A tool is traditionally a command line program such as a compiler.
The set of tools available with a platform is defined by the
vendor.

Tools can be located using

ServiceLoader.load(Class)

.

**All Known Subinterfaces:** DocumentationTool

,

JavaCompiler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default
String
name()

Returns the name of this tool, or an empty string if no name is provided.

**Returns:**
- the name of this tool

**Since:**
- 9

**API Note:**
- It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".

**Implementation Note:**
- This implementation returns an empty string.

---

#### int run​(
InputStream
in,

OutputStream
out,

OutputStream
err,

String
... arguments)

Run the tool with the given I/O channels and arguments. By
convention a tool returns 0 for success and nonzero for errors.
Any diagnostics generated will be written to either

out

or

err

in some unspecified format.

**Parameters:**
- in

- "standard" input; use System.in if null
- out

- "standard" output; use System.out if null
- err

- "standard" error; use System.err if null
- arguments

- arguments to pass to the tool

**Returns:**
- 0 for success; nonzero otherwise

**Throws:**
- NullPointerException

- if the array of arguments contains
any

null

elements.

---

#### Set
<
SourceVersion
> getSourceVersions()

Returns the source versions of the Java™ programming language
supported by this tool.

**Returns:**
- a set of supported source versions

---

### Additional Sections

#### Interface Tool

**All Known Subinterfaces:** DocumentationTool

,

JavaCompiler

```java
public interface
Tool
```

Common interface for tools that can be invoked from a program.
A tool is traditionally a command line program such as a compiler.
The set of tools available with a platform is defined by the
vendor.

Tools can be located using

ServiceLoader.load(Class)

.

**Since:** 1.6

public interface

Tool

Common interface for tools that can be invoked from a program.
A tool is traditionally a command line program such as a compiler.
The set of tools available with a platform is defined by the
vendor.

Tools can be located using

ServiceLoader.load(Class)

.

Tools can be located using

ServiceLoader.load(Class)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

Set

<

SourceVersion

>

getSourceVersions

()

Returns the source versions of the Java™ programming language
supported by this tool.

default

String

name

()

Returns the name of this tool, or an empty string if no name is provided.

int

run

​(

InputStream

in,

OutputStream

out,

OutputStream

err,

String

... arguments)

Run the tool with the given I/O channels and arguments.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

Set

<

SourceVersion

>

getSourceVersions

()

Returns the source versions of the Java™ programming language
supported by this tool.

default

String

name

()

Returns the name of this tool, or an empty string if no name is provided.

int

run

​(

InputStream

in,

OutputStream

out,

OutputStream

err,

String

... arguments)

Run the tool with the given I/O channels and arguments.

---

#### Method Summary

Returns the source versions of the Java™ programming language
supported by this tool.

Returns the name of this tool, or an empty string if no name is provided.

Run the tool with the given I/O channels and arguments.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
default
String
name()
```

Returns the name of this tool, or an empty string if no name is provided.

**API Note:** It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".
**Implementation Note:** This implementation returns an empty string.
**Returns:** the name of this tool
**Since:** 9

- run

```java
int run​(
InputStream
in,

OutputStream
out,

OutputStream
err,

String
... arguments)
```

Run the tool with the given I/O channels and arguments. By
convention a tool returns 0 for success and nonzero for errors.
Any diagnostics generated will be written to either

out

or

err

in some unspecified format.

**Parameters:** in

- "standard" input; use System.in if null
**Parameters:** out

- "standard" output; use System.out if null
**Parameters:** err

- "standard" error; use System.err if null
**Parameters:** arguments

- arguments to pass to the tool
**Returns:** 0 for success; nonzero otherwise
**Throws:** NullPointerException

- if the array of arguments contains
any

null

elements.

- getSourceVersions

```java
Set
<
SourceVersion
> getSourceVersions()
```

Returns the source versions of the Java™ programming language
supported by this tool.

**Returns:** a set of supported source versions

Method Detail

- name

```java
default
String
name()
```

Returns the name of this tool, or an empty string if no name is provided.

**API Note:** It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".
**Implementation Note:** This implementation returns an empty string.
**Returns:** the name of this tool
**Since:** 9

- run

```java
int run​(
InputStream
in,

OutputStream
out,

OutputStream
err,

String
... arguments)
```

Run the tool with the given I/O channels and arguments. By
convention a tool returns 0 for success and nonzero for errors.
Any diagnostics generated will be written to either

out

or

err

in some unspecified format.

**Parameters:** in

- "standard" input; use System.in if null
**Parameters:** out

- "standard" output; use System.out if null
**Parameters:** err

- "standard" error; use System.err if null
**Parameters:** arguments

- arguments to pass to the tool
**Returns:** 0 for success; nonzero otherwise
**Throws:** NullPointerException

- if the array of arguments contains
any

null

elements.

- getSourceVersions

```java
Set
<
SourceVersion
> getSourceVersions()
```

Returns the source versions of the Java™ programming language
supported by this tool.

**Returns:** a set of supported source versions

---

#### Method Detail

name

```java
default
String
name()
```

Returns the name of this tool, or an empty string if no name is provided.

**API Note:** It is recommended that the name be the same as would be
used on the command line: for example, "javac", "jar", "jlink".
**Implementation Note:** This implementation returns an empty string.
**Returns:** the name of this tool
**Since:** 9

---

#### name

default

String

name()

Returns the name of this tool, or an empty string if no name is provided.

run

```java
int run​(
InputStream
in,

OutputStream
out,

OutputStream
err,

String
... arguments)
```

Run the tool with the given I/O channels and arguments. By
convention a tool returns 0 for success and nonzero for errors.
Any diagnostics generated will be written to either

out

or

err

in some unspecified format.

**Parameters:** in

- "standard" input; use System.in if null
**Parameters:** out

- "standard" output; use System.out if null
**Parameters:** err

- "standard" error; use System.err if null
**Parameters:** arguments

- arguments to pass to the tool
**Returns:** 0 for success; nonzero otherwise
**Throws:** NullPointerException

- if the array of arguments contains
any

null

elements.

---

#### run

int run​(

InputStream

in,

OutputStream

out,

OutputStream

err,

String

... arguments)

Run the tool with the given I/O channels and arguments. By
convention a tool returns 0 for success and nonzero for errors.
Any diagnostics generated will be written to either

out

or

err

in some unspecified format.

getSourceVersions

```java
Set
<
SourceVersion
> getSourceVersions()
```

Returns the source versions of the Java™ programming language
supported by this tool.

**Returns:** a set of supported source versions

---

#### getSourceVersions

Set

<

SourceVersion

> getSourceVersions()

Returns the source versions of the Java™ programming language
supported by this tool.

---

