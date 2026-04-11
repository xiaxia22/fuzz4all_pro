# Interface LineMap

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\LineMap.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
LineMap
```

Provides methods to convert between character positions and line numbers
for a compilation unit.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getLineNumber​(long pos)

Find the line containing a position; a line termination
character is on the line it terminates.

**Parameters:**
- pos

- character offset of the position

**Returns:**
- the line number of pos (first line is 1)

---

#### long getColumnNumber​(long pos)

Find the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

**Parameters:**
- pos

- character offset of the position

**Returns:**
- the tab-expanded column number of pos (first column is 1)

---

### Additional Sections

#### Interface LineMap

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
LineMap
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Provides methods to convert between character positions and line numbers
for a compilation unit.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

LineMap

Provides methods to convert between character positions and line numbers
for a compilation unit.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

long

getColumnNumber

​(long pos)

Deprecated, for removal: This API element is subject to removal in a future version.

Find the column for a character position.

long

getLineNumber

​(long pos)

Deprecated, for removal: This API element is subject to removal in a future version.

Find the line containing a position; a line termination
character is on the line it terminates.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

long

getColumnNumber

​(long pos)

Deprecated, for removal: This API element is subject to removal in a future version.

Find the column for a character position.

long

getLineNumber

​(long pos)

Deprecated, for removal: This API element is subject to removal in a future version.

Find the line containing a position; a line termination
character is on the line it terminates.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Find the column for a character position.

Find the line containing a position; a line termination
character is on the line it terminates.

============ METHOD DETAIL ==========

- Method Detail

- getLineNumber

```java
long getLineNumber​(long pos)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the line containing a position; a line termination
character is on the line it terminates.

**Parameters:** pos

- character offset of the position
**Returns:** the line number of pos (first line is 1)

- getColumnNumber

```java
long getColumnNumber​(long pos)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

**Parameters:** pos

- character offset of the position
**Returns:** the tab-expanded column number of pos (first column is 1)

Method Detail

- getLineNumber

```java
long getLineNumber​(long pos)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the line containing a position; a line termination
character is on the line it terminates.

**Parameters:** pos

- character offset of the position
**Returns:** the line number of pos (first line is 1)

- getColumnNumber

```java
long getColumnNumber​(long pos)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

**Parameters:** pos

- character offset of the position
**Returns:** the tab-expanded column number of pos (first column is 1)

---

#### Method Detail

getLineNumber

```java
long getLineNumber​(long pos)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the line containing a position; a line termination
character is on the line it terminates.

**Parameters:** pos

- character offset of the position
**Returns:** the line number of pos (first line is 1)

---

#### getLineNumber

long getLineNumber​(long pos)

Find the line containing a position; a line termination
character is on the line it terminates.

getColumnNumber

```java
long getColumnNumber​(long pos)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

**Parameters:** pos

- character offset of the position
**Returns:** the tab-expanded column number of pos (first column is 1)

---

#### getColumnNumber

long getColumnNumber​(long pos)

Find the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

---

