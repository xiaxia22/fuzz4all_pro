# Interface Diagnostic<S>

**Source:** `java.compiler\javax\tools\Diagnostic.html`

### Class Description

```java
public interface
Diagnostic<S>
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

**Type Parameters:** S

- the type of source object used by this diagnostic

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

Returns the kind of this diagnostic, for example, error or
warning.

**Returns:**
- the kind of this diagnostic

---

#### S
getSource()

Returns the source object associated with this diagnostic.

**Returns:**
- the source object associated with this diagnostic.

null

if no source object is associated with the
diagnostic.

---

#### long getPosition()

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:**
- character offset from beginning of source;

NOPOS

if

getSource()

would return

null

or if
no location is suitable

---

#### long getStartPosition()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

**Returns:**
- offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

---

#### long getEndPosition()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

**Returns:**
- offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

---

#### long getLineNumber()

Returns the line number of the character offset returned by

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

Returns the column number of the character offset returned by

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

Returns a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:**
- a diagnostic code

---

#### String
getMessage​(
Locale
locale)

Returns a localized message for the given locale. The actual
message is implementation-dependent. If the locale is

null

use the default locale.

**Parameters:**
- locale

- a locale; might be

null

**Returns:**
- a localized message

---

### Additional Sections

#### Interface Diagnostic<S>

**Type Parameters:** S

- the type of source object used by this diagnostic

```java
public interface
Diagnostic<S>
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

**Since:** 1.6

public interface

Diagnostic<S>

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

A position is a zero-based character offset from the beginning of
a file. Negative values (except

NOPOS

) are not valid
positions.

Line and column numbers begin at 1. Negative values (except

NOPOS

) and 0 are not valid line or column numbers.

Line and column numbers begin at 1. Negative values (except

NOPOS

) and 0 are not valid line or column numbers.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Diagnostic.Kind

Kinds of diagnostics, for example, error or warning.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

NOPOS

Used to signal that no position is available.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCode

()

Returns a diagnostic code indicating the type of diagnostic.

long

getColumnNumber

()

Returns the column number of the character offset returned by

getPosition()

.

long

getEndPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

Diagnostic.Kind

getKind

()

Returns the kind of this diagnostic, for example, error or
warning.

long

getLineNumber

()

Returns the line number of the character offset returned by

getPosition()

.

String

getMessage

​(

Locale

locale)

Returns a localized message for the given locale.

long

getPosition

()

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

S

getSource

()

Returns the source object associated with this diagnostic.

long

getStartPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Diagnostic.Kind

Kinds of diagnostics, for example, error or warning.

---

#### Nested Class Summary

Kinds of diagnostics, for example, error or warning.

Field Summary

Fields

Modifier and Type

Field

Description

static long

NOPOS

Used to signal that no position is available.

---

#### Field Summary

Used to signal that no position is available.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCode

()

Returns a diagnostic code indicating the type of diagnostic.

long

getColumnNumber

()

Returns the column number of the character offset returned by

getPosition()

.

long

getEndPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

Diagnostic.Kind

getKind

()

Returns the kind of this diagnostic, for example, error or
warning.

long

getLineNumber

()

Returns the line number of the character offset returned by

getPosition()

.

String

getMessage

​(

Locale

locale)

Returns a localized message for the given locale.

long

getPosition

()

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

S

getSource

()

Returns the source object associated with this diagnostic.

long

getStartPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

---

#### Method Summary

Returns a diagnostic code indicating the type of diagnostic.

Returns the column number of the character offset returned by

getPosition()

.

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

Returns the kind of this diagnostic, for example, error or
warning.

Returns the line number of the character offset returned by

getPosition()

.

Returns a localized message for the given locale.

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

Returns the source object associated with this diagnostic.

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

============ FIELD DETAIL ===========

- Field Detail

- NOPOS

```java
static final long NOPOS
```

Used to signal that no position is available.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
Diagnostic.Kind
getKind()
```

Returns the kind of this diagnostic, for example, error or
warning.

**Returns:** the kind of this diagnostic

- getSource

```java
S
getSource()
```

Returns the source object associated with this diagnostic.

**Returns:** the source object associated with this diagnostic.

null

if no source object is associated with the
diagnostic.

- getPosition

```java
long getPosition()
```

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if

getSource()

would return

null

or if
no location is suitable

- getStartPosition

```java
long getStartPosition()
```

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

**Returns:** offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

- getEndPosition

```java
long getEndPosition()
```

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

**Returns:** offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

- getLineNumber

```java
long getLineNumber()
```

Returns the line number of the character offset returned by

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

Returns the column number of the character offset returned by

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

Returns a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:** a diagnostic code

- getMessage

```java
String
getMessage​(
Locale
locale)
```

Returns a localized message for the given locale. The actual
message is implementation-dependent. If the locale is

null

use the default locale.

**Parameters:** locale

- a locale; might be

null
**Returns:** a localized message

Field Detail

- NOPOS

```java
static final long NOPOS
```

Used to signal that no position is available.

**See Also:** Constant Field Values

---

#### Field Detail

NOPOS

```java
static final long NOPOS
```

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

Returns the kind of this diagnostic, for example, error or
warning.

**Returns:** the kind of this diagnostic

- getSource

```java
S
getSource()
```

Returns the source object associated with this diagnostic.

**Returns:** the source object associated with this diagnostic.

null

if no source object is associated with the
diagnostic.

- getPosition

```java
long getPosition()
```

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if

getSource()

would return

null

or if
no location is suitable

- getStartPosition

```java
long getStartPosition()
```

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

**Returns:** offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

- getEndPosition

```java
long getEndPosition()
```

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

**Returns:** offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

- getLineNumber

```java
long getLineNumber()
```

Returns the line number of the character offset returned by

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

Returns the column number of the character offset returned by

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

Returns a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:** a diagnostic code

- getMessage

```java
String
getMessage​(
Locale
locale)
```

Returns a localized message for the given locale. The actual
message is implementation-dependent. If the locale is

null

use the default locale.

**Parameters:** locale

- a locale; might be

null
**Returns:** a localized message

---

#### Method Detail

getKind

```java
Diagnostic.Kind
getKind()
```

Returns the kind of this diagnostic, for example, error or
warning.

**Returns:** the kind of this diagnostic

---

#### getKind

Diagnostic.Kind

getKind()

Returns the kind of this diagnostic, for example, error or
warning.

getSource

```java
S
getSource()
```

Returns the source object associated with this diagnostic.

**Returns:** the source object associated with this diagnostic.

null

if no source object is associated with the
diagnostic.

---

#### getSource

S

getSource()

Returns the source object associated with this diagnostic.

getPosition

```java
long getPosition()
```

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if

getSource()

would return

null

or if
no location is suitable

---

#### getPosition

long getPosition()

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

getPosition() <= getEndPosition()

getStartPosition

```java
long getStartPosition()
```

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

**Returns:** offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

---

#### getStartPosition

long getStartPosition()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

getEndPosition

```java
long getEndPosition()
```

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

**Returns:** offset from beginning of file;

NOPOS

if and
only if

getPosition()

returns

NOPOS

---

#### getEndPosition

long getEndPosition()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

getLineNumber

```java
long getLineNumber()
```

Returns the line number of the character offset returned by

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

Returns the line number of the character offset returned by

getPosition()

.

getColumnNumber

```java
long getColumnNumber()
```

Returns the column number of the character offset returned by

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

Returns the column number of the character offset returned by

getPosition()

.

getCode

```java
String
getCode()
```

Returns a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:** a diagnostic code

---

#### getCode

String

getCode()

Returns a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

getMessage

```java
String
getMessage​(
Locale
locale)
```

Returns a localized message for the given locale. The actual
message is implementation-dependent. If the locale is

null

use the default locale.

**Parameters:** locale

- a locale; might be

null
**Returns:** a localized message

---

#### getMessage

String

getMessage​(

Locale

locale)

Returns a localized message for the given locale. The actual
message is implementation-dependent. If the locale is

null

use the default locale.

---

