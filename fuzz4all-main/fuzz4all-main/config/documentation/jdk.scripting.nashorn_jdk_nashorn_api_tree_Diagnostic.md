# Interface Diagnostic

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\Diagnostic.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
Diagnostic
```

Interface for diagnostics from tools. A diagnostic usually reports
a problem at a specific position in a source file. However, not
all diagnostics are associated with a position or a file.

A position is a zero-based character offset from the beginning of
a file. Negative values (except

NOPOS

) are not valid
positions.

Line and column numbers begin at 1. Negative values (except

NOPOS

) and 0 are not valid line or column numbers.

Line terminator is as defined in ECMAScript specification which is one
of { \u000A, \u000B, \u2028, \u2029 }.

**Since:** 9

---

### Field Details

#### static final long NOPOS

Used to signal that no position is available.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Diagnostic.Kind
getKind()

Gets the kind of this diagnostic, for example, error or
warning.

**Returns:**
- the kind of this diagnostic

---

#### long getPosition()

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:**
- character offset from beginning of source;

NOPOS

if no location is suitable

---

#### String
getFileName()

Gets the source file name.

**Returns:**
- the file name or null if not available

---

#### long getLineNumber()

Gets the line number of the character offset returned by

getPosition()

.

**Returns:**
- a line number or

NOPOS

if and only if

getPosition()

returns

NOPOS

---

#### long getColumnNumber()

Gets the column number of the character offset returned by

getPosition()

.

**Returns:**
- a column number or

NOPOS

if and only if

getPosition()

returns

NOPOS

---

#### String
getCode()

Gets a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:**
- a diagnostic code

---

#### String
getMessage()

Gets a message for this diagnostic.

**Returns:**
- a message

---

### Additional Sections

#### Interface Diagnostic

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
Diagnostic
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Interface for diagnostics from tools. A diagnostic usually reports
a problem at a specific position in a source file. However, not
all diagnostics are associated with a position or a file.

A position is a zero-based character offset from the beginning of
a file. Negative values (except

NOPOS

) are not valid
positions.

Line and column numbers begin at 1. Negative values (except

NOPOS

) and 0 are not valid line or column numbers.

Line terminator is as defined in ECMAScript specification which is one
of { \u000A, \u000B, \u2028, \u2029 }.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

Diagnostic

Interface for diagnostics from tools. A diagnostic usually reports
a problem at a specific position in a source file. However, not
all diagnostics are associated with a position or a file.

A position is a zero-based character offset from the beginning of
a file. Negative values (except

NOPOS

) are not valid
positions.

Line and column numbers begin at 1. Negative values (except

NOPOS

) and 0 are not valid line or column numbers.

Line terminator is as defined in ECMAScript specification which is one
of { \u000A, \u000B, \u2028, \u2029 }.

A position is a zero-based character offset from the beginning of
a file. Negative values (except

NOPOS

) are not valid
positions.

Line and column numbers begin at 1. Negative values (except

NOPOS

) and 0 are not valid line or column numbers.

Line terminator is as defined in ECMAScript specification which is one
of { \u000A, \u000B, \u2028, \u2029 }.

Line and column numbers begin at 1. Negative values (except

NOPOS

) and 0 are not valid line or column numbers.

Line terminator is as defined in ECMAScript specification which is one
of { \u000A, \u000B, \u2028, \u2029 }.

Line terminator is as defined in ECMAScript specification which is one
of { \u000A, \u000B, \u2028, \u2029 }.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Diagnostic.Kind

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

NOPOS

Deprecated, for removal: This API element is subject to removal in a future version.

Used to signal that no position is available.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

String

getCode

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a diagnostic code indicating the type of diagnostic.

long

getColumnNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the column number of the character offset returned by

getPosition()

.

String

getFileName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the source file name.

Diagnostic.Kind

getKind

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this diagnostic, for example, error or
warning.

long

getLineNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the line number of the character offset returned by

getPosition()

.

String

getMessage

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a message for this diagnostic.

long

getPosition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Diagnostic.Kind

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

---

#### Nested Class Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Field Summary

Fields

Modifier and Type

Field

Description

static long

NOPOS

Deprecated, for removal: This API element is subject to removal in a future version.

Used to signal that no position is available.

---

#### Field Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Used to signal that no position is available.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

String

getCode

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a diagnostic code indicating the type of diagnostic.

long

getColumnNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the column number of the character offset returned by

getPosition()

.

String

getFileName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the source file name.

Diagnostic.Kind

getKind

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this diagnostic, for example, error or
warning.

long

getLineNumber

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the line number of the character offset returned by

getPosition()

.

String

getMessage

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a message for this diagnostic.

long

getPosition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a diagnostic code indicating the type of diagnostic.

Gets the column number of the character offset returned by

getPosition()

.

Gets the source file name.

Gets the kind of this diagnostic, for example, error or
warning.

Gets the line number of the character offset returned by

getPosition()

.

Gets a message for this diagnostic.

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

============ FIELD DETAIL ===========

- Field Detail

- NOPOS

```java
static final long NOPOS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used to signal that no position is available.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
Diagnostic.Kind
getKind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this diagnostic, for example, error or
warning.

**Returns:** the kind of this diagnostic

- getPosition

```java
long getPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if no location is suitable

- getFileName

```java
String
getFileName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the source file name.

**Returns:** the file name or null if not available

- getLineNumber

```java
long getLineNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the line number of the character offset returned by

getPosition()

.

**Returns:** a line number or

NOPOS

if and only if

getPosition()

returns

NOPOS

- getColumnNumber

```java
long getColumnNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the column number of the character offset returned by

getPosition()

.

**Returns:** a column number or

NOPOS

if and only if

getPosition()

returns

NOPOS

- getCode

```java
String
getCode()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:** a diagnostic code

- getMessage

```java
String
getMessage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a message for this diagnostic.

**Returns:** a message

Field Detail

- NOPOS

```java
static final long NOPOS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used to signal that no position is available.

**See Also:** Constant Field Values

---

#### Field Detail

NOPOS

```java
static final long NOPOS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used to signal that no position is available.

**See Also:** Constant Field Values

---

#### NOPOS

static final long NOPOS

Used to signal that no position is available.

Method Detail

- getKind

```java
Diagnostic.Kind
getKind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this diagnostic, for example, error or
warning.

**Returns:** the kind of this diagnostic

- getPosition

```java
long getPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if no location is suitable

- getFileName

```java
String
getFileName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the source file name.

**Returns:** the file name or null if not available

- getLineNumber

```java
long getLineNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the line number of the character offset returned by

getPosition()

.

**Returns:** a line number or

NOPOS

if and only if

getPosition()

returns

NOPOS

- getColumnNumber

```java
long getColumnNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the column number of the character offset returned by

getPosition()

.

**Returns:** a column number or

NOPOS

if and only if

getPosition()

returns

NOPOS

- getCode

```java
String
getCode()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:** a diagnostic code

- getMessage

```java
String
getMessage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a message for this diagnostic.

**Returns:** a message

---

#### Method Detail

getKind

```java
Diagnostic.Kind
getKind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this diagnostic, for example, error or
warning.

**Returns:** the kind of this diagnostic

---

#### getKind

Diagnostic.Kind

getKind()

Gets the kind of this diagnostic, for example, error or
warning.

getPosition

```java
long getPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if no location is suitable

---

#### getPosition

long getPosition()

Gets a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

getPosition() <= getEndPosition()

getFileName

```java
String
getFileName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the source file name.

**Returns:** the file name or null if not available

---

#### getFileName

String

getFileName()

Gets the source file name.

getLineNumber

```java
long getLineNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the line number of the character offset returned by

getPosition()

.

**Returns:** a line number or

NOPOS

if and only if

getPosition()

returns

NOPOS

---

#### getLineNumber

long getLineNumber()

Gets the line number of the character offset returned by

getPosition()

.

getColumnNumber

```java
long getColumnNumber()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the column number of the character offset returned by

getPosition()

.

**Returns:** a column number or

NOPOS

if and only if

getPosition()

returns

NOPOS

---

#### getColumnNumber

long getColumnNumber()

Gets the column number of the character offset returned by

getPosition()

.

getCode

```java
String
getCode()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:** a diagnostic code

---

#### getCode

String

getCode()

Gets a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

getMessage

```java
String
getMessage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets a message for this diagnostic.

**Returns:** a message

---

#### getMessage

String

getMessage()

Gets a message for this diagnostic.

---

