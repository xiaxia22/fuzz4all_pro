# Interface AccessibleExtendedTable

**Source:** `java.desktop\javax\accessibility\AccessibleExtendedTable.html`

### Class Description

```java
public interface
AccessibleExtendedTable

extends
AccessibleTable
```

Class

AccessibleExtendedTable

provides extended information about a
user-interface component that presents data in a two-dimensional table
format. Applications can determine if an object supports the

AccessibleExtendedTable

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleTable()

method. If the return value is
not

null

and the type of the return value is

AccessibleExtendedTable

, the object supports this interface.

**All Superinterfaces:** AccessibleTable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getAccessibleRow​(int index)

Returns the row number of an index in the table.

**Parameters:**
- index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.

**Returns:**
- the zero-based row of the table if one exists; otherwise -1

---

#### int getAccessibleColumn​(int index)

Returns the column number of an index in the table.

**Parameters:**
- index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.

**Returns:**
- the zero-based column of the table if one exists; otherwise -1

---

#### int getAccessibleIndex​(int r,
int c)

Returns the index at a row and column in the table.

**Parameters:**
- r

- zero-based row of the table
- c

- zero-based column of the table

**Returns:**
- the zero-based index in the table if one exists; otherwise -1.
The index is the table cell offset from row == 0 and column == 0.

---

### Additional Sections

#### Interface AccessibleExtendedTable

**All Superinterfaces:** AccessibleTable

**All Known Implementing Classes:** JTable.AccessibleJTable

```java
public interface
AccessibleExtendedTable

extends
AccessibleTable
```

Class

AccessibleExtendedTable

provides extended information about a
user-interface component that presents data in a two-dimensional table
format. Applications can determine if an object supports the

AccessibleExtendedTable

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleTable()

method. If the return value is
not

null

and the type of the return value is

AccessibleExtendedTable

, the object supports this interface.

**Since:** 1.4

public interface

AccessibleExtendedTable

extends

AccessibleTable

Class

AccessibleExtendedTable

provides extended information about a
user-interface component that presents data in a two-dimensional table
format. Applications can determine if an object supports the

AccessibleExtendedTable

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleTable()

method. If the return value is
not

null

and the type of the return value is

AccessibleExtendedTable

, the object supports this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getAccessibleColumn

​(int index)

Returns the column number of an index in the table.

int

getAccessibleIndex

​(int r,
int c)

Returns the index at a row and column in the table.

int

getAccessibleRow

​(int index)

Returns the row number of an index in the table.

- Methods declared in interface javax.accessibility.

AccessibleTable

getAccessibleAt

,

getAccessibleCaption

,

getAccessibleColumnCount

,

getAccessibleColumnDescription

,

getAccessibleColumnExtentAt

,

getAccessibleColumnHeader

,

getAccessibleRowCount

,

getAccessibleRowDescription

,

getAccessibleRowExtentAt

,

getAccessibleRowHeader

,

getAccessibleSummary

,

getSelectedAccessibleColumns

,

getSelectedAccessibleRows

,

isAccessibleColumnSelected

,

isAccessibleRowSelected

,

isAccessibleSelected

,

setAccessibleCaption

,

setAccessibleColumnDescription

,

setAccessibleColumnHeader

,

setAccessibleRowDescription

,

setAccessibleRowHeader

,

setAccessibleSummary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getAccessibleColumn

​(int index)

Returns the column number of an index in the table.

int

getAccessibleIndex

​(int r,
int c)

Returns the index at a row and column in the table.

int

getAccessibleRow

​(int index)

Returns the row number of an index in the table.

- Methods declared in interface javax.accessibility.

AccessibleTable

getAccessibleAt

,

getAccessibleCaption

,

getAccessibleColumnCount

,

getAccessibleColumnDescription

,

getAccessibleColumnExtentAt

,

getAccessibleColumnHeader

,

getAccessibleRowCount

,

getAccessibleRowDescription

,

getAccessibleRowExtentAt

,

getAccessibleRowHeader

,

getAccessibleSummary

,

getSelectedAccessibleColumns

,

getSelectedAccessibleRows

,

isAccessibleColumnSelected

,

isAccessibleRowSelected

,

isAccessibleSelected

,

setAccessibleCaption

,

setAccessibleColumnDescription

,

setAccessibleColumnHeader

,

setAccessibleRowDescription

,

setAccessibleRowHeader

,

setAccessibleSummary

---

#### Method Summary

Returns the column number of an index in the table.

Returns the index at a row and column in the table.

Returns the row number of an index in the table.

Methods declared in interface javax.accessibility.

AccessibleTable

getAccessibleAt

,

getAccessibleCaption

,

getAccessibleColumnCount

,

getAccessibleColumnDescription

,

getAccessibleColumnExtentAt

,

getAccessibleColumnHeader

,

getAccessibleRowCount

,

getAccessibleRowDescription

,

getAccessibleRowExtentAt

,

getAccessibleRowHeader

,

getAccessibleSummary

,

getSelectedAccessibleColumns

,

getSelectedAccessibleRows

,

isAccessibleColumnSelected

,

isAccessibleRowSelected

,

isAccessibleSelected

,

setAccessibleCaption

,

setAccessibleColumnDescription

,

setAccessibleColumnHeader

,

setAccessibleRowDescription

,

setAccessibleRowHeader

,

setAccessibleSummary

---

#### Methods declared in interface javax.accessibility. AccessibleTable

============ METHOD DETAIL ==========

- Method Detail

- getAccessibleRow

```java
int getAccessibleRow​(int index)
```

Returns the row number of an index in the table.

**Parameters:** index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.
**Returns:** the zero-based row of the table if one exists; otherwise -1

- getAccessibleColumn

```java
int getAccessibleColumn​(int index)
```

Returns the column number of an index in the table.

**Parameters:** index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.
**Returns:** the zero-based column of the table if one exists; otherwise -1

- getAccessibleIndex

```java
int getAccessibleIndex​(int r,
int c)
```

Returns the index at a row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the zero-based index in the table if one exists; otherwise -1.
The index is the table cell offset from row == 0 and column == 0.

Method Detail

- getAccessibleRow

```java
int getAccessibleRow​(int index)
```

Returns the row number of an index in the table.

**Parameters:** index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.
**Returns:** the zero-based row of the table if one exists; otherwise -1

- getAccessibleColumn

```java
int getAccessibleColumn​(int index)
```

Returns the column number of an index in the table.

**Parameters:** index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.
**Returns:** the zero-based column of the table if one exists; otherwise -1

- getAccessibleIndex

```java
int getAccessibleIndex​(int r,
int c)
```

Returns the index at a row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the zero-based index in the table if one exists; otherwise -1.
The index is the table cell offset from row == 0 and column == 0.

---

#### Method Detail

getAccessibleRow

```java
int getAccessibleRow​(int index)
```

Returns the row number of an index in the table.

**Parameters:** index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.
**Returns:** the zero-based row of the table if one exists; otherwise -1

---

#### getAccessibleRow

int getAccessibleRow​(int index)

Returns the row number of an index in the table.

getAccessibleColumn

```java
int getAccessibleColumn​(int index)
```

Returns the column number of an index in the table.

**Parameters:** index

- the zero-based index in the table. The index is the table
cell offset from row == 0 and column == 0.
**Returns:** the zero-based column of the table if one exists; otherwise -1

---

#### getAccessibleColumn

int getAccessibleColumn​(int index)

Returns the column number of an index in the table.

getAccessibleIndex

```java
int getAccessibleIndex​(int r,
int c)
```

Returns the index at a row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the zero-based index in the table if one exists; otherwise -1.
The index is the table cell offset from row == 0 and column == 0.

---

#### getAccessibleIndex

int getAccessibleIndex​(int r,
int c)

Returns the index at a row and column in the table.

---

