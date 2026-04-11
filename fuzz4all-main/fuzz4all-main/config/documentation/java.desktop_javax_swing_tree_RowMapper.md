# Interface RowMapper

**Source:** `java.desktop\javax\swing\tree\RowMapper.html`

### Class Description

```java
public interface
RowMapper
```

Defines the requirements for an object that translates paths in
the tree into display rows.

**All Known Implementing Classes:** AbstractLayoutCache

,

FixedHeightLayoutCache

,

VariableHeightLayoutCache

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int[] getRowsForPaths​(
TreePath
[] path)

Returns the rows that the TreePath instances in

path

are being displayed at. The receiver should return an array of
the same length as that passed in, and if one of the TreePaths
in

path

is not valid its entry in the array should
be set to -1.

**Parameters:**
- path

- array of TreePath to parse

**Returns:**
- the rows that the TreePath instances in

path

are
being displayed at

---

### Additional Sections

#### Interface RowMapper

**All Known Implementing Classes:** AbstractLayoutCache

,

FixedHeightLayoutCache

,

VariableHeightLayoutCache

```java
public interface
RowMapper
```

Defines the requirements for an object that translates paths in
the tree into display rows.

public interface

RowMapper

Defines the requirements for an object that translates paths in
the tree into display rows.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int[]

getRowsForPaths

​(

TreePath

[] path)

Returns the rows that the TreePath instances in

path

are being displayed at.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int[]

getRowsForPaths

​(

TreePath

[] path)

Returns the rows that the TreePath instances in

path

are being displayed at.

---

#### Method Summary

Returns the rows that the TreePath instances in

path

are being displayed at.

============ METHOD DETAIL ==========

- Method Detail

- getRowsForPaths

```java
int[] getRowsForPaths​(
TreePath
[] path)
```

Returns the rows that the TreePath instances in

path

are being displayed at. The receiver should return an array of
the same length as that passed in, and if one of the TreePaths
in

path

is not valid its entry in the array should
be set to -1.

**Parameters:** path

- array of TreePath to parse
**Returns:** the rows that the TreePath instances in

path

are
being displayed at

Method Detail

- getRowsForPaths

```java
int[] getRowsForPaths​(
TreePath
[] path)
```

Returns the rows that the TreePath instances in

path

are being displayed at. The receiver should return an array of
the same length as that passed in, and if one of the TreePaths
in

path

is not valid its entry in the array should
be set to -1.

**Parameters:** path

- array of TreePath to parse
**Returns:** the rows that the TreePath instances in

path

are
being displayed at

---

#### Method Detail

getRowsForPaths

```java
int[] getRowsForPaths​(
TreePath
[] path)
```

Returns the rows that the TreePath instances in

path

are being displayed at. The receiver should return an array of
the same length as that passed in, and if one of the TreePaths
in

path

is not valid its entry in the array should
be set to -1.

**Parameters:** path

- array of TreePath to parse
**Returns:** the rows that the TreePath instances in

path

are
being displayed at

---

#### getRowsForPaths

int[] getRowsForPaths​(

TreePath

[] path)

Returns the rows that the TreePath instances in

path

are being displayed at. The receiver should return an array of
the same length as that passed in, and if one of the TreePaths
in

path

is not valid its entry in the array should
be set to -1.

---

