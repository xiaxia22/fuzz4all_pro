# Class Diag

**Source:** `jdk.jshell\jdk\jshell\Diag.html`

### Class Description

```java
public abstract class
Diag

extends
Object
```

Diagnostic information for a Snippet.

**Since:** 9
**See Also:** JShell.diagnostics(jdk.jshell.Snippet)

---

### Field Details

#### public static final long NOPOS

Used to signal that no position is available.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public abstract boolean isError()

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

**Returns:**
- true

if this diagnostic is an error; otherwise

false

---

#### public abstract long getPosition()

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:**
- character offset from beginning of source;

NOPOS

if the position is not available.

---

#### public abstract long getStartPosition()

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

#### public abstract long getEndPosition()

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

#### public abstract
String
getCode()

Returns a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

**Returns:**
- a diagnostic code

---

#### public abstract
String
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

#### Class Diag

java.lang.Object

- jdk.jshell.Diag

jdk.jshell.Diag

```java
public abstract class
Diag

extends
Object
```

Diagnostic information for a Snippet.

**Since:** 9
**See Also:** JShell.diagnostics(jdk.jshell.Snippet)

public abstract class

Diag

extends

Object

Diagnostic information for a Snippet.

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

abstract

String

getCode

()

Returns a diagnostic code indicating the type of diagnostic.

abstract long

getEndPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

abstract

String

getMessage

​(

Locale

locale)

Returns a localized message for the given locale.

abstract long

getPosition

()

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

abstract long

getStartPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

abstract boolean

isError

()

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

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

abstract

String

getCode

()

Returns a diagnostic code indicating the type of diagnostic.

abstract long

getEndPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

abstract

String

getMessage

​(

Locale

locale)

Returns a localized message for the given locale.

abstract long

getPosition

()

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

abstract long

getStartPosition

()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

abstract boolean

isError

()

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

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

Returns a diagnostic code indicating the type of diagnostic.

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

Returns a localized message for the given locale.

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem.

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

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

============ FIELD DETAIL ===========

- Field Detail

- NOPOS

```java
public static final long NOPOS
```

Used to signal that no position is available.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- isError

```java
public abstract boolean isError()
```

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

**Returns:** true

if this diagnostic is an error; otherwise

false

- getPosition

```java
public abstract long getPosition()
```

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if the position is not available.

- getStartPosition

```java
public abstract long getStartPosition()
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
public abstract long getEndPosition()
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

- getCode

```java
public abstract
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
public abstract
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
public static final long NOPOS
```

Used to signal that no position is available.

**See Also:** Constant Field Values

---

#### Field Detail

NOPOS

```java
public static final long NOPOS
```

Used to signal that no position is available.

**See Also:** Constant Field Values

---

#### NOPOS

public static final long NOPOS

Used to signal that no position is available.

Method Detail

- isError

```java
public abstract boolean isError()
```

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

**Returns:** true

if this diagnostic is an error; otherwise

false

- getPosition

```java
public abstract long getPosition()
```

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if the position is not available.

- getStartPosition

```java
public abstract long getStartPosition()
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
public abstract long getEndPosition()
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

- getCode

```java
public abstract
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
public abstract
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

isError

```java
public abstract boolean isError()
```

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

**Returns:** true

if this diagnostic is an error; otherwise

false

---

#### isError

public abstract boolean isError()

Indicates whether this diagnostic is an error (as opposed to a warning or
note).

getPosition

```java
public abstract long getPosition()
```

Returns a character offset from the beginning of the source object
associated with this diagnostic that indicates the location of
the problem. In addition, the following must be true:

getStartPostion() <= getPosition()

getPosition() <= getEndPosition()

**Returns:** character offset from beginning of source;

NOPOS

if the position is not available.

---

#### getPosition

public abstract long getPosition()

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
public abstract long getStartPosition()
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

public abstract long getStartPosition()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the start of the
problem.

getEndPosition

```java
public abstract long getEndPosition()
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

public abstract long getEndPosition()

Returns the character offset from the beginning of the file
associated with this diagnostic that indicates the end of the
problem.

getCode

```java
public abstract
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

public abstract

String

getCode()

Returns a diagnostic code indicating the type of diagnostic. The
code is implementation-dependent and might be

null

.

getMessage

```java
public abstract
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

public abstract

String

getMessage​(

Locale

locale)

Returns a localized message for the given locale. The actual
message is implementation-dependent. If the locale is

null

use the default locale.

---

