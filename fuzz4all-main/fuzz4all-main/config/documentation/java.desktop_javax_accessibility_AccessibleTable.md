# Interface AccessibleTable

**Source:** `java.desktop\javax\accessibility\AccessibleTable.html`

### Class Description

```java
public interface
AccessibleTable
```

Class

AccessibleTable

describes a user-interface component that
presents data in a two-dimensional table format.

**All Known Subinterfaces:** AccessibleExtendedTable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Accessible
getAccessibleCaption()

Returns the caption for the table.

**Returns:**
- the caption for the table

---

#### void setAccessibleCaption​(
Accessible
a)

Sets the caption for the table.

**Parameters:**
- a

- the caption for the table

---

#### Accessible
getAccessibleSummary()

Returns the summary description of the table.

**Returns:**
- the summary description of the table

---

#### void setAccessibleSummary​(
Accessible
a)

Sets the summary description of the table.

**Parameters:**
- a

- the summary description of the table

---

#### int getAccessibleRowCount()

Returns the number of rows in the table.

**Returns:**
- the number of rows in the table

---

#### int getAccessibleColumnCount()

Returns the number of columns in the table.

**Returns:**
- the number of columns in the table

---

#### Accessible
getAccessibleAt​(int r,
int c)

Returns the

Accessible

at a specified row and column in the
table.

**Parameters:**
- r

- zero-based row of the table
- c

- zero-based column of the table

**Returns:**
- the

Accessible

at the specified row and column

---

#### int getAccessibleRowExtentAt​(int r,
int c)

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:**
- r

- zero-based row of the table
- c

- zero-based column of the table

**Returns:**
- the number of rows occupied by the

Accessible

at a given
specified (row, column)

---

#### int getAccessibleColumnExtentAt​(int r,
int c)

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:**
- r

- zero-based row of the table
- c

- zero-based column of the table

**Returns:**
- the number of columns occupied by the

Accessible

at a
given specified row and column

---

#### AccessibleTable
getAccessibleRowHeader()

Returns the row headers as an

AccessibleTable

.

**Returns:**
- an

AccessibleTable

representing the row headers

---

#### void setAccessibleRowHeader​(
AccessibleTable
table)

Sets the row headers.

**Parameters:**
- table

- an

AccessibleTable

representing the row headers

---

#### AccessibleTable
getAccessibleColumnHeader()

Returns the column headers as an

AccessibleTable

.

**Returns:**
- an

AccessibleTable

representing the column headers

---

#### void setAccessibleColumnHeader​(
AccessibleTable
table)

Sets the column headers.

**Parameters:**
- table

- an

AccessibleTable

representing the column headers

---

#### Accessible
getAccessibleRowDescription​(int r)

Returns the description of the specified row in the table.

**Parameters:**
- r

- zero-based row of the table

**Returns:**
- the description of the row

---

#### void setAccessibleRowDescription​(int r,

Accessible
a)

Sets the description text of the specified row of the table.

**Parameters:**
- r

- zero-based row of the table
- a

- the description of the row

---

#### Accessible
getAccessibleColumnDescription​(int c)

Returns the description text of the specified column in the table.

**Parameters:**
- c

- zero-based column of the table

**Returns:**
- the text description of the column

---

#### void setAccessibleColumnDescription​(int c,

Accessible
a)

Sets the description text of the specified column in the table.

**Parameters:**
- c

- zero-based column of the table
- a

- the text description of the column

---

#### boolean isAccessibleSelected​(int r,
int c)

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

**Parameters:**
- r

- zero-based row of the table
- c

- zero-based column of the table

**Returns:**
- the boolean value

true

if the accessible at the row and
column is selected. Otherwise, the boolean value

false

---

#### boolean isAccessibleRowSelected​(int r)

Returns a boolean value indicating whether the specified row is selected.

**Parameters:**
- r

- zero-based row of the table

**Returns:**
- the boolean value

true

if the specified row is selected.
Otherwise,

false

.

---

#### boolean isAccessibleColumnSelected​(int c)

Returns a boolean value indicating whether the specified column is
selected.

**Parameters:**
- c

- zero-based column of the table

**Returns:**
- the boolean value

true

if the specified column is
selected. Otherwise,

false

.

---

#### int[] getSelectedAccessibleRows()

Returns the selected rows in a table.

**Returns:**
- an array of selected rows where each element is a zero-based row
of the table

---

#### int[] getSelectedAccessibleColumns()

Returns the selected columns in a table.

**Returns:**
- an array of selected columns where each element is a zero-based
column of the table

---

### Additional Sections

#### Interface AccessibleTable

**All Known Subinterfaces:** AccessibleExtendedTable

**All Known Implementing Classes:** JTable.AccessibleJTable

```java
public interface
AccessibleTable
```

Class

AccessibleTable

describes a user-interface component that
presents data in a two-dimensional table format.

**Since:** 1.3

public interface

AccessibleTable

Class

AccessibleTable

describes a user-interface component that
presents data in a two-dimensional table format.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Accessible

getAccessibleAt

​(int r,
int c)

Returns the

Accessible

at a specified row and column in the
table.

Accessible

getAccessibleCaption

()

Returns the caption for the table.

int

getAccessibleColumnCount

()

Returns the number of columns in the table.

Accessible

getAccessibleColumnDescription

​(int c)

Returns the description text of the specified column in the table.

int

getAccessibleColumnExtentAt

​(int r,
int c)

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

AccessibleTable

getAccessibleColumnHeader

()

Returns the column headers as an

AccessibleTable

.

int

getAccessibleRowCount

()

Returns the number of rows in the table.

Accessible

getAccessibleRowDescription

​(int r)

Returns the description of the specified row in the table.

int

getAccessibleRowExtentAt

​(int r,
int c)

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

AccessibleTable

getAccessibleRowHeader

()

Returns the row headers as an

AccessibleTable

.

Accessible

getAccessibleSummary

()

Returns the summary description of the table.

int[]

getSelectedAccessibleColumns

()

Returns the selected columns in a table.

int[]

getSelectedAccessibleRows

()

Returns the selected rows in a table.

boolean

isAccessibleColumnSelected

​(int c)

Returns a boolean value indicating whether the specified column is
selected.

boolean

isAccessibleRowSelected

​(int r)

Returns a boolean value indicating whether the specified row is selected.

boolean

isAccessibleSelected

​(int r,
int c)

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

void

setAccessibleCaption

​(

Accessible

a)

Sets the caption for the table.

void

setAccessibleColumnDescription

​(int c,

Accessible

a)

Sets the description text of the specified column in the table.

void

setAccessibleColumnHeader

​(

AccessibleTable

table)

Sets the column headers.

void

setAccessibleRowDescription

​(int r,

Accessible

a)

Sets the description text of the specified row of the table.

void

setAccessibleRowHeader

​(

AccessibleTable

table)

Sets the row headers.

void

setAccessibleSummary

​(

Accessible

a)

Sets the summary description of the table.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Accessible

getAccessibleAt

​(int r,
int c)

Returns the

Accessible

at a specified row and column in the
table.

Accessible

getAccessibleCaption

()

Returns the caption for the table.

int

getAccessibleColumnCount

()

Returns the number of columns in the table.

Accessible

getAccessibleColumnDescription

​(int c)

Returns the description text of the specified column in the table.

int

getAccessibleColumnExtentAt

​(int r,
int c)

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

AccessibleTable

getAccessibleColumnHeader

()

Returns the column headers as an

AccessibleTable

.

int

getAccessibleRowCount

()

Returns the number of rows in the table.

Accessible

getAccessibleRowDescription

​(int r)

Returns the description of the specified row in the table.

int

getAccessibleRowExtentAt

​(int r,
int c)

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

AccessibleTable

getAccessibleRowHeader

()

Returns the row headers as an

AccessibleTable

.

Accessible

getAccessibleSummary

()

Returns the summary description of the table.

int[]

getSelectedAccessibleColumns

()

Returns the selected columns in a table.

int[]

getSelectedAccessibleRows

()

Returns the selected rows in a table.

boolean

isAccessibleColumnSelected

​(int c)

Returns a boolean value indicating whether the specified column is
selected.

boolean

isAccessibleRowSelected

​(int r)

Returns a boolean value indicating whether the specified row is selected.

boolean

isAccessibleSelected

​(int r,
int c)

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

void

setAccessibleCaption

​(

Accessible

a)

Sets the caption for the table.

void

setAccessibleColumnDescription

​(int c,

Accessible

a)

Sets the description text of the specified column in the table.

void

setAccessibleColumnHeader

​(

AccessibleTable

table)

Sets the column headers.

void

setAccessibleRowDescription

​(int r,

Accessible

a)

Sets the description text of the specified row of the table.

void

setAccessibleRowHeader

​(

AccessibleTable

table)

Sets the row headers.

void

setAccessibleSummary

​(

Accessible

a)

Sets the summary description of the table.

---

#### Method Summary

Returns the

Accessible

at a specified row and column in the
table.

Returns the caption for the table.

Returns the number of columns in the table.

Returns the description text of the specified column in the table.

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

Returns the column headers as an

AccessibleTable

.

Returns the number of rows in the table.

Returns the description of the specified row in the table.

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

Returns the row headers as an

AccessibleTable

.

Returns the summary description of the table.

Returns the selected columns in a table.

Returns the selected rows in a table.

Returns a boolean value indicating whether the specified column is
selected.

Returns a boolean value indicating whether the specified row is selected.

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

Sets the caption for the table.

Sets the description text of the specified column in the table.

Sets the column headers.

Sets the description text of the specified row of the table.

Sets the row headers.

Sets the summary description of the table.

============ METHOD DETAIL ==========

- Method Detail

- getAccessibleCaption

```java
Accessible
getAccessibleCaption()
```

Returns the caption for the table.

**Returns:** the caption for the table

- setAccessibleCaption

```java
void setAccessibleCaption​(
Accessible
a)
```

Sets the caption for the table.

**Parameters:** a

- the caption for the table

- getAccessibleSummary

```java
Accessible
getAccessibleSummary()
```

Returns the summary description of the table.

**Returns:** the summary description of the table

- setAccessibleSummary

```java
void setAccessibleSummary​(
Accessible
a)
```

Sets the summary description of the table.

**Parameters:** a

- the summary description of the table

- getAccessibleRowCount

```java
int getAccessibleRowCount()
```

Returns the number of rows in the table.

**Returns:** the number of rows in the table

- getAccessibleColumnCount

```java
int getAccessibleColumnCount()
```

Returns the number of columns in the table.

**Returns:** the number of columns in the table

- getAccessibleAt

```java
Accessible
getAccessibleAt​(int r,
int c)
```

Returns the

Accessible

at a specified row and column in the
table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the

Accessible

at the specified row and column

- getAccessibleRowExtentAt

```java
int getAccessibleRowExtentAt​(int r,
int c)
```

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the number of rows occupied by the

Accessible

at a given
specified (row, column)

- getAccessibleColumnExtentAt

```java
int getAccessibleColumnExtentAt​(int r,
int c)
```

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the number of columns occupied by the

Accessible

at a
given specified row and column

- getAccessibleRowHeader

```java
AccessibleTable
getAccessibleRowHeader()
```

Returns the row headers as an

AccessibleTable

.

**Returns:** an

AccessibleTable

representing the row headers

- setAccessibleRowHeader

```java
void setAccessibleRowHeader​(
AccessibleTable
table)
```

Sets the row headers.

**Parameters:** table

- an

AccessibleTable

representing the row headers

- getAccessibleColumnHeader

```java
AccessibleTable
getAccessibleColumnHeader()
```

Returns the column headers as an

AccessibleTable

.

**Returns:** an

AccessibleTable

representing the column headers

- setAccessibleColumnHeader

```java
void setAccessibleColumnHeader​(
AccessibleTable
table)
```

Sets the column headers.

**Parameters:** table

- an

AccessibleTable

representing the column headers

- getAccessibleRowDescription

```java
Accessible
getAccessibleRowDescription​(int r)
```

Returns the description of the specified row in the table.

**Parameters:** r

- zero-based row of the table
**Returns:** the description of the row

- setAccessibleRowDescription

```java
void setAccessibleRowDescription​(int r,

Accessible
a)
```

Sets the description text of the specified row of the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** a

- the description of the row

- getAccessibleColumnDescription

```java
Accessible
getAccessibleColumnDescription​(int c)
```

Returns the description text of the specified column in the table.

**Parameters:** c

- zero-based column of the table
**Returns:** the text description of the column

- setAccessibleColumnDescription

```java
void setAccessibleColumnDescription​(int c,

Accessible
a)
```

Sets the description text of the specified column in the table.

**Parameters:** c

- zero-based column of the table
**Parameters:** a

- the text description of the column

- isAccessibleSelected

```java
boolean isAccessibleSelected​(int r,
int c)
```

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the boolean value

true

if the accessible at the row and
column is selected. Otherwise, the boolean value

false

- isAccessibleRowSelected

```java
boolean isAccessibleRowSelected​(int r)
```

Returns a boolean value indicating whether the specified row is selected.

**Parameters:** r

- zero-based row of the table
**Returns:** the boolean value

true

if the specified row is selected.
Otherwise,

false

.

- isAccessibleColumnSelected

```java
boolean isAccessibleColumnSelected​(int c)
```

Returns a boolean value indicating whether the specified column is
selected.

**Parameters:** c

- zero-based column of the table
**Returns:** the boolean value

true

if the specified column is
selected. Otherwise,

false

.

- getSelectedAccessibleRows

```java
int[] getSelectedAccessibleRows()
```

Returns the selected rows in a table.

**Returns:** an array of selected rows where each element is a zero-based row
of the table

- getSelectedAccessibleColumns

```java
int[] getSelectedAccessibleColumns()
```

Returns the selected columns in a table.

**Returns:** an array of selected columns where each element is a zero-based
column of the table

Method Detail

- getAccessibleCaption

```java
Accessible
getAccessibleCaption()
```

Returns the caption for the table.

**Returns:** the caption for the table

- setAccessibleCaption

```java
void setAccessibleCaption​(
Accessible
a)
```

Sets the caption for the table.

**Parameters:** a

- the caption for the table

- getAccessibleSummary

```java
Accessible
getAccessibleSummary()
```

Returns the summary description of the table.

**Returns:** the summary description of the table

- setAccessibleSummary

```java
void setAccessibleSummary​(
Accessible
a)
```

Sets the summary description of the table.

**Parameters:** a

- the summary description of the table

- getAccessibleRowCount

```java
int getAccessibleRowCount()
```

Returns the number of rows in the table.

**Returns:** the number of rows in the table

- getAccessibleColumnCount

```java
int getAccessibleColumnCount()
```

Returns the number of columns in the table.

**Returns:** the number of columns in the table

- getAccessibleAt

```java
Accessible
getAccessibleAt​(int r,
int c)
```

Returns the

Accessible

at a specified row and column in the
table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the

Accessible

at the specified row and column

- getAccessibleRowExtentAt

```java
int getAccessibleRowExtentAt​(int r,
int c)
```

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the number of rows occupied by the

Accessible

at a given
specified (row, column)

- getAccessibleColumnExtentAt

```java
int getAccessibleColumnExtentAt​(int r,
int c)
```

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the number of columns occupied by the

Accessible

at a
given specified row and column

- getAccessibleRowHeader

```java
AccessibleTable
getAccessibleRowHeader()
```

Returns the row headers as an

AccessibleTable

.

**Returns:** an

AccessibleTable

representing the row headers

- setAccessibleRowHeader

```java
void setAccessibleRowHeader​(
AccessibleTable
table)
```

Sets the row headers.

**Parameters:** table

- an

AccessibleTable

representing the row headers

- getAccessibleColumnHeader

```java
AccessibleTable
getAccessibleColumnHeader()
```

Returns the column headers as an

AccessibleTable

.

**Returns:** an

AccessibleTable

representing the column headers

- setAccessibleColumnHeader

```java
void setAccessibleColumnHeader​(
AccessibleTable
table)
```

Sets the column headers.

**Parameters:** table

- an

AccessibleTable

representing the column headers

- getAccessibleRowDescription

```java
Accessible
getAccessibleRowDescription​(int r)
```

Returns the description of the specified row in the table.

**Parameters:** r

- zero-based row of the table
**Returns:** the description of the row

- setAccessibleRowDescription

```java
void setAccessibleRowDescription​(int r,

Accessible
a)
```

Sets the description text of the specified row of the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** a

- the description of the row

- getAccessibleColumnDescription

```java
Accessible
getAccessibleColumnDescription​(int c)
```

Returns the description text of the specified column in the table.

**Parameters:** c

- zero-based column of the table
**Returns:** the text description of the column

- setAccessibleColumnDescription

```java
void setAccessibleColumnDescription​(int c,

Accessible
a)
```

Sets the description text of the specified column in the table.

**Parameters:** c

- zero-based column of the table
**Parameters:** a

- the text description of the column

- isAccessibleSelected

```java
boolean isAccessibleSelected​(int r,
int c)
```

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the boolean value

true

if the accessible at the row and
column is selected. Otherwise, the boolean value

false

- isAccessibleRowSelected

```java
boolean isAccessibleRowSelected​(int r)
```

Returns a boolean value indicating whether the specified row is selected.

**Parameters:** r

- zero-based row of the table
**Returns:** the boolean value

true

if the specified row is selected.
Otherwise,

false

.

- isAccessibleColumnSelected

```java
boolean isAccessibleColumnSelected​(int c)
```

Returns a boolean value indicating whether the specified column is
selected.

**Parameters:** c

- zero-based column of the table
**Returns:** the boolean value

true

if the specified column is
selected. Otherwise,

false

.

- getSelectedAccessibleRows

```java
int[] getSelectedAccessibleRows()
```

Returns the selected rows in a table.

**Returns:** an array of selected rows where each element is a zero-based row
of the table

- getSelectedAccessibleColumns

```java
int[] getSelectedAccessibleColumns()
```

Returns the selected columns in a table.

**Returns:** an array of selected columns where each element is a zero-based
column of the table

---

#### Method Detail

getAccessibleCaption

```java
Accessible
getAccessibleCaption()
```

Returns the caption for the table.

**Returns:** the caption for the table

---

#### getAccessibleCaption

Accessible

getAccessibleCaption()

Returns the caption for the table.

setAccessibleCaption

```java
void setAccessibleCaption​(
Accessible
a)
```

Sets the caption for the table.

**Parameters:** a

- the caption for the table

---

#### setAccessibleCaption

void setAccessibleCaption​(

Accessible

a)

Sets the caption for the table.

getAccessibleSummary

```java
Accessible
getAccessibleSummary()
```

Returns the summary description of the table.

**Returns:** the summary description of the table

---

#### getAccessibleSummary

Accessible

getAccessibleSummary()

Returns the summary description of the table.

setAccessibleSummary

```java
void setAccessibleSummary​(
Accessible
a)
```

Sets the summary description of the table.

**Parameters:** a

- the summary description of the table

---

#### setAccessibleSummary

void setAccessibleSummary​(

Accessible

a)

Sets the summary description of the table.

getAccessibleRowCount

```java
int getAccessibleRowCount()
```

Returns the number of rows in the table.

**Returns:** the number of rows in the table

---

#### getAccessibleRowCount

int getAccessibleRowCount()

Returns the number of rows in the table.

getAccessibleColumnCount

```java
int getAccessibleColumnCount()
```

Returns the number of columns in the table.

**Returns:** the number of columns in the table

---

#### getAccessibleColumnCount

int getAccessibleColumnCount()

Returns the number of columns in the table.

getAccessibleAt

```java
Accessible
getAccessibleAt​(int r,
int c)
```

Returns the

Accessible

at a specified row and column in the
table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the

Accessible

at the specified row and column

---

#### getAccessibleAt

Accessible

getAccessibleAt​(int r,
int c)

Returns the

Accessible

at a specified row and column in the
table.

getAccessibleRowExtentAt

```java
int getAccessibleRowExtentAt​(int r,
int c)
```

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the number of rows occupied by the

Accessible

at a given
specified (row, column)

---

#### getAccessibleRowExtentAt

int getAccessibleRowExtentAt​(int r,
int c)

Returns the number of rows occupied by the

Accessible

at a
specified row and column in the table.

getAccessibleColumnExtentAt

```java
int getAccessibleColumnExtentAt​(int r,
int c)
```

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the number of columns occupied by the

Accessible

at a
given specified row and column

---

#### getAccessibleColumnExtentAt

int getAccessibleColumnExtentAt​(int r,
int c)

Returns the number of columns occupied by the

Accessible

at a
specified row and column in the table.

getAccessibleRowHeader

```java
AccessibleTable
getAccessibleRowHeader()
```

Returns the row headers as an

AccessibleTable

.

**Returns:** an

AccessibleTable

representing the row headers

---

#### getAccessibleRowHeader

AccessibleTable

getAccessibleRowHeader()

Returns the row headers as an

AccessibleTable

.

setAccessibleRowHeader

```java
void setAccessibleRowHeader​(
AccessibleTable
table)
```

Sets the row headers.

**Parameters:** table

- an

AccessibleTable

representing the row headers

---

#### setAccessibleRowHeader

void setAccessibleRowHeader​(

AccessibleTable

table)

Sets the row headers.

getAccessibleColumnHeader

```java
AccessibleTable
getAccessibleColumnHeader()
```

Returns the column headers as an

AccessibleTable

.

**Returns:** an

AccessibleTable

representing the column headers

---

#### getAccessibleColumnHeader

AccessibleTable

getAccessibleColumnHeader()

Returns the column headers as an

AccessibleTable

.

setAccessibleColumnHeader

```java
void setAccessibleColumnHeader​(
AccessibleTable
table)
```

Sets the column headers.

**Parameters:** table

- an

AccessibleTable

representing the column headers

---

#### setAccessibleColumnHeader

void setAccessibleColumnHeader​(

AccessibleTable

table)

Sets the column headers.

getAccessibleRowDescription

```java
Accessible
getAccessibleRowDescription​(int r)
```

Returns the description of the specified row in the table.

**Parameters:** r

- zero-based row of the table
**Returns:** the description of the row

---

#### getAccessibleRowDescription

Accessible

getAccessibleRowDescription​(int r)

Returns the description of the specified row in the table.

setAccessibleRowDescription

```java
void setAccessibleRowDescription​(int r,

Accessible
a)
```

Sets the description text of the specified row of the table.

**Parameters:** r

- zero-based row of the table
**Parameters:** a

- the description of the row

---

#### setAccessibleRowDescription

void setAccessibleRowDescription​(int r,

Accessible

a)

Sets the description text of the specified row of the table.

getAccessibleColumnDescription

```java
Accessible
getAccessibleColumnDescription​(int c)
```

Returns the description text of the specified column in the table.

**Parameters:** c

- zero-based column of the table
**Returns:** the text description of the column

---

#### getAccessibleColumnDescription

Accessible

getAccessibleColumnDescription​(int c)

Returns the description text of the specified column in the table.

setAccessibleColumnDescription

```java
void setAccessibleColumnDescription​(int c,

Accessible
a)
```

Sets the description text of the specified column in the table.

**Parameters:** c

- zero-based column of the table
**Parameters:** a

- the text description of the column

---

#### setAccessibleColumnDescription

void setAccessibleColumnDescription​(int c,

Accessible

a)

Sets the description text of the specified column in the table.

isAccessibleSelected

```java
boolean isAccessibleSelected​(int r,
int c)
```

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

**Parameters:** r

- zero-based row of the table
**Parameters:** c

- zero-based column of the table
**Returns:** the boolean value

true

if the accessible at the row and
column is selected. Otherwise, the boolean value

false

---

#### isAccessibleSelected

boolean isAccessibleSelected​(int r,
int c)

Returns a boolean value indicating whether the accessible at a specified
row and column is selected.

isAccessibleRowSelected

```java
boolean isAccessibleRowSelected​(int r)
```

Returns a boolean value indicating whether the specified row is selected.

**Parameters:** r

- zero-based row of the table
**Returns:** the boolean value

true

if the specified row is selected.
Otherwise,

false

.

---

#### isAccessibleRowSelected

boolean isAccessibleRowSelected​(int r)

Returns a boolean value indicating whether the specified row is selected.

isAccessibleColumnSelected

```java
boolean isAccessibleColumnSelected​(int c)
```

Returns a boolean value indicating whether the specified column is
selected.

**Parameters:** c

- zero-based column of the table
**Returns:** the boolean value

true

if the specified column is
selected. Otherwise,

false

.

---

#### isAccessibleColumnSelected

boolean isAccessibleColumnSelected​(int c)

Returns a boolean value indicating whether the specified column is
selected.

getSelectedAccessibleRows

```java
int[] getSelectedAccessibleRows()
```

Returns the selected rows in a table.

**Returns:** an array of selected rows where each element is a zero-based row
of the table

---

#### getSelectedAccessibleRows

int[] getSelectedAccessibleRows()

Returns the selected rows in a table.

getSelectedAccessibleColumns

```java
int[] getSelectedAccessibleColumns()
```

Returns the selected columns in a table.

**Returns:** an array of selected columns where each element is a zero-based
column of the table

---

#### getSelectedAccessibleColumns

int[] getSelectedAccessibleColumns()

Returns the selected columns in a table.

---

