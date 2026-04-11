# Interface SourcePosition

**Source:** `jdk.javadoc\com\sun\javadoc\SourcePosition.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
SourcePosition
```

This interface describes a source position: filename, line number,
and column number.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### File
file()

The source file. Returns null if no file information is
available.

**Returns:**
- the source file as a File.

---

#### int line()

The line in the source file. The first line is numbered 1;
0 means no line number information is available.

**Returns:**
- the line number in the source file as an integer.

---

#### int column()

The column in the source file. The first column is
numbered 1; 0 means no column information is available.
Columns count characters in the input stream; a tab
advances the column number to the next 8-column tab stop.

**Returns:**
- the column on the source line as an integer.

---

#### String
toString()

Convert the source position to the form "Filename:line".

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Interface SourcePosition

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
SourcePosition
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

This interface describes a source position: filename, line number,
and column number.

**Since:** 1.4

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

SourcePosition

This interface describes a source position: filename, line number,
and column number.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

int

column

()

Deprecated, for removal: This API element is subject to removal in a future version.

The column in the source file.

File

file

()

Deprecated, for removal: This API element is subject to removal in a future version.

The source file.

int

line

()

Deprecated, for removal: This API element is subject to removal in a future version.

The line in the source file.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the source position to the form "Filename:line".

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

int

column

()

Deprecated, for removal: This API element is subject to removal in a future version.

The column in the source file.

File

file

()

Deprecated, for removal: This API element is subject to removal in a future version.

The source file.

int

line

()

Deprecated, for removal: This API element is subject to removal in a future version.

The line in the source file.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the source position to the form "Filename:line".

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

The column in the source file.

The source file.

The line in the source file.

Convert the source position to the form "Filename:line".

============ METHOD DETAIL ==========

- Method Detail

- file

```java
File
file()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The source file. Returns null if no file information is
available.

**Returns:** the source file as a File.

- line

```java
int line()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The line in the source file. The first line is numbered 1;
0 means no line number information is available.

**Returns:** the line number in the source file as an integer.

- column

```java
int column()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The column in the source file. The first column is
numbered 1; 0 means no column information is available.
Columns count characters in the input stream; a tab
advances the column number to the next 8-column tab stop.

**Returns:** the column on the source line as an integer.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the source position to the form "Filename:line".

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Method Detail

- file

```java
File
file()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The source file. Returns null if no file information is
available.

**Returns:** the source file as a File.

- line

```java
int line()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The line in the source file. The first line is numbered 1;
0 means no line number information is available.

**Returns:** the line number in the source file as an integer.

- column

```java
int column()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The column in the source file. The first column is
numbered 1; 0 means no column information is available.
Columns count characters in the input stream; a tab
advances the column number to the next 8-column tab stop.

**Returns:** the column on the source line as an integer.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the source position to the form "Filename:line".

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

file

```java
File
file()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The source file. Returns null if no file information is
available.

**Returns:** the source file as a File.

---

#### file

File

file()

The source file. Returns null if no file information is
available.

line

```java
int line()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The line in the source file. The first line is numbered 1;
0 means no line number information is available.

**Returns:** the line number in the source file as an integer.

---

#### line

int line()

The line in the source file. The first line is numbered 1;
0 means no line number information is available.

column

```java
int column()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The column in the source file. The first column is
numbered 1; 0 means no column information is available.
Columns count characters in the input stream; a tab
advances the column number to the next 8-column tab stop.

**Returns:** the column on the source line as an integer.

---

#### column

int column()

The column in the source file. The first column is
numbered 1; 0 means no column information is available.
Columns count characters in the input stream; a tab
advances the column number to the next 8-column tab stop.

toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert the source position to the form "Filename:line".

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

String

toString()

Convert the source position to the form "Filename:line".

---

