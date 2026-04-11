# Interface LineMap

**Source:** `jdk.compiler\com\sun\source\tree\LineMap.html`

### Class Description

```java
public interface
LineMap
```

Provides methods to convert between character positions and line numbers
for a compilation unit.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getStartPosition​(long line)

Finds the start position of a line.

**Parameters:**
- line

- line number (beginning at 1)

**Returns:**
- position of first character in line

**Throws:**
- IndexOutOfBoundsException

- if

lineNumber < 1

if

lineNumber > no. of lines

---

#### long getPosition​(long line,
long column)

Finds the position corresponding to a (line,column).

**Parameters:**
- line

- line number (beginning at 1)
- column

- tab-expanded column number (beginning 1)

**Returns:**
- position of character

**Throws:**
- IndexOutOfBoundsException

- if

line < 1

if

line > no. of lines

---

#### long getLineNumber​(long pos)

Finds the line containing a position; a line termination
character is on the line it terminates.

**Parameters:**
- pos

- character offset of the position

**Returns:**
- the line number of pos (first line is 1)

---

#### long getColumnNumber​(long pos)

Finds the column for a character position.
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
public interface
LineMap
```

Provides methods to convert between character positions and line numbers
for a compilation unit.

**Since:** 1.6

public interface

LineMap

Provides methods to convert between character positions and line numbers
for a compilation unit.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getColumnNumber

​(long pos)

Finds the column for a character position.

long

getLineNumber

​(long pos)

Finds the line containing a position; a line termination
character is on the line it terminates.

long

getPosition

​(long line,
long column)

Finds the position corresponding to a (line,column).

long

getStartPosition

​(long line)

Finds the start position of a line.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getColumnNumber

​(long pos)

Finds the column for a character position.

long

getLineNumber

​(long pos)

Finds the line containing a position; a line termination
character is on the line it terminates.

long

getPosition

​(long line,
long column)

Finds the position corresponding to a (line,column).

long

getStartPosition

​(long line)

Finds the start position of a line.

---

#### Method Summary

Finds the column for a character position.

Finds the line containing a position; a line termination
character is on the line it terminates.

Finds the position corresponding to a (line,column).

Finds the start position of a line.

============ METHOD DETAIL ==========

- Method Detail

- getStartPosition

```java
long getStartPosition​(long line)
```

Finds the start position of a line.

**Parameters:** line

- line number (beginning at 1)
**Returns:** position of first character in line
**Throws:** IndexOutOfBoundsException

- if

lineNumber < 1

if

lineNumber > no. of lines

- getPosition

```java
long getPosition​(long line,
long column)
```

Finds the position corresponding to a (line,column).

**Parameters:** line

- line number (beginning at 1)
**Parameters:** column

- tab-expanded column number (beginning 1)
**Returns:** position of character
**Throws:** IndexOutOfBoundsException

- if

line < 1

if

line > no. of lines

- getLineNumber

```java
long getLineNumber​(long pos)
```

Finds the line containing a position; a line termination
character is on the line it terminates.

**Parameters:** pos

- character offset of the position
**Returns:** the line number of pos (first line is 1)

- getColumnNumber

```java
long getColumnNumber​(long pos)
```

Finds the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

**Parameters:** pos

- character offset of the position
**Returns:** the tab-expanded column number of pos (first column is 1)

Method Detail

- getStartPosition

```java
long getStartPosition​(long line)
```

Finds the start position of a line.

**Parameters:** line

- line number (beginning at 1)
**Returns:** position of first character in line
**Throws:** IndexOutOfBoundsException

- if

lineNumber < 1

if

lineNumber > no. of lines

- getPosition

```java
long getPosition​(long line,
long column)
```

Finds the position corresponding to a (line,column).

**Parameters:** line

- line number (beginning at 1)
**Parameters:** column

- tab-expanded column number (beginning 1)
**Returns:** position of character
**Throws:** IndexOutOfBoundsException

- if

line < 1

if

line > no. of lines

- getLineNumber

```java
long getLineNumber​(long pos)
```

Finds the line containing a position; a line termination
character is on the line it terminates.

**Parameters:** pos

- character offset of the position
**Returns:** the line number of pos (first line is 1)

- getColumnNumber

```java
long getColumnNumber​(long pos)
```

Finds the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

**Parameters:** pos

- character offset of the position
**Returns:** the tab-expanded column number of pos (first column is 1)

---

#### Method Detail

getStartPosition

```java
long getStartPosition​(long line)
```

Finds the start position of a line.

**Parameters:** line

- line number (beginning at 1)
**Returns:** position of first character in line
**Throws:** IndexOutOfBoundsException

- if

lineNumber < 1

if

lineNumber > no. of lines

---

#### getStartPosition

long getStartPosition​(long line)

Finds the start position of a line.

getPosition

```java
long getPosition​(long line,
long column)
```

Finds the position corresponding to a (line,column).

**Parameters:** line

- line number (beginning at 1)
**Parameters:** column

- tab-expanded column number (beginning 1)
**Returns:** position of character
**Throws:** IndexOutOfBoundsException

- if

line < 1

if

line > no. of lines

---

#### getPosition

long getPosition​(long line,
long column)

Finds the position corresponding to a (line,column).

getLineNumber

```java
long getLineNumber​(long pos)
```

Finds the line containing a position; a line termination
character is on the line it terminates.

**Parameters:** pos

- character offset of the position
**Returns:** the line number of pos (first line is 1)

---

#### getLineNumber

long getLineNumber​(long pos)

Finds the line containing a position; a line termination
character is on the line it terminates.

getColumnNumber

```java
long getColumnNumber​(long pos)
```

Finds the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

**Parameters:** pos

- character offset of the position
**Returns:** the tab-expanded column number of pos (first column is 1)

---

#### getColumnNumber

long getColumnNumber​(long pos)

Finds the column for a character position.
Tab characters preceding the position on the same line
will be expanded when calculating the column number.

---

