# Interface TableColumnModel

**Source:** `java.desktop\javax\swing\table\TableColumnModel.html`

### Class Description

```java
public interface
TableColumnModel
```

Defines the requirements for a table column model object suitable for
use with

JTable

.

**All Known Implementing Classes:** DefaultTableColumnModel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addColumn​(
TableColumn
aColumn)

Appends

aColumn

to the end of the

tableColumns

array.
This method posts a

columnAdded

event to its listeners.

**Parameters:**
- aColumn

- the

TableColumn

to be added

**See Also:**
- removeColumn(javax.swing.table.TableColumn)

---

#### void removeColumn​(
TableColumn
column)

Deletes the

TableColumn

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's column list.
This method posts a

columnRemoved

event to its listeners.

**Parameters:**
- column

- the

TableColumn

to be removed

**See Also:**
- addColumn(javax.swing.table.TableColumn)

---

#### void moveColumn​(int columnIndex,
int newIndex)

Moves the column and its header at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column that used
to be at

newIndex

is shifted left or right
to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
posts a

columnMoved

event to its listeners.

**Parameters:**
- columnIndex

- the index of column to be moved
- newIndex

- index of the column's new location

**Throws:**
- IllegalArgumentException

- if

columnIndex

or

newIndex

are not in the valid range

---

#### void setColumnMargin​(int newMargin)

Sets the

TableColumn

's column margin to

newMargin

. This method posts
a

columnMarginChanged

event to its listeners.

**Parameters:**
- newMargin

- the width, in pixels, of the new column margins

**See Also:**
- getColumnMargin()

---

#### int getColumnCount()

Returns the number of columns in the model.

**Returns:**
- the number of columns in the model

---

#### Enumeration
<
TableColumn
> getColumns()

Returns an

Enumeration

of all the columns in the model.

**Returns:**
- an

Enumeration

of all the columns in the model

---

#### int getColumnIndex​(
Object
columnIdentifier)

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

**Parameters:**
- columnIdentifier

- the identifier object

**Returns:**
- the index of the first table column
whose identifier is equal to

identifier

**Throws:**
- IllegalArgumentException

- if

identifier

is

null

, or no

TableColumn

has this

identifier

**See Also:**
- getColumn(int)

---

#### TableColumn
getColumn​(int columnIndex)

Returns the

TableColumn

object for the column at

columnIndex

.

**Parameters:**
- columnIndex

- the index of the desired column

**Returns:**
- the

TableColumn

object for
the column at

columnIndex

---

#### int getColumnMargin()

Returns the width between the cells in each column.

**Returns:**
- the margin, in pixels, between the cells

---

#### int getColumnIndexAtX​(int xPosition)

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

In keeping with Swing's separable model architecture, a
TableColumnModel does not know how the table columns actually appear on
screen. The visual presentation of the columns is the responsibility
of the view/controller object using this model (typically JTable). The
view/controller need not display the columns sequentially from left to
right. For example, columns could be displayed from right to left to
accommodate a locale preference or some columns might be hidden at the
request of the user. Because the model does not know how the columns
are laid out on screen, the given

xPosition

should not be
considered to be a coordinate in 2D graphics space. Instead, it should
be considered to be a width from the start of the first column in the
model. If the column index for a given X coordinate in 2D space is
required,

JTable.columnAtPoint

can be used instead.

**Parameters:**
- xPosition

- width from the start of the first column in
the model.

**Returns:**
- the index of the column; or -1 if no column is found

**See Also:**
- JTable.columnAtPoint(java.awt.Point)

---

#### int getTotalColumnWidth()

Returns the total width of all the columns.

**Returns:**
- the total computed width of all columns

---

#### void setColumnSelectionAllowed​(boolean flag)

Sets whether the columns in this model may be selected.

**Parameters:**
- flag

- true if columns may be selected; otherwise false

**See Also:**
- getColumnSelectionAllowed()

---

#### boolean getColumnSelectionAllowed()

Returns true if columns may be selected.

**Returns:**
- true if columns may be selected

**See Also:**
- setColumnSelectionAllowed(boolean)

---

#### int[] getSelectedColumns()

Returns an array of indicies of all selected columns.

**Returns:**
- an array of integers containing the indicies of all
selected columns; or an empty array if nothing is selected

---

#### int getSelectedColumnCount()

Returns the number of selected columns.

**Returns:**
- the number of selected columns; or 0 if no columns are selected

---

#### void setSelectionModel​(
ListSelectionModel
newModel)

Sets the selection model.

**Parameters:**
- newModel

- a

ListSelectionModel

object

**See Also:**
- getSelectionModel()

---

#### ListSelectionModel
getSelectionModel()

Returns the current selection model.

**Returns:**
- a

ListSelectionModel

object

**See Also:**
- setSelectionModel(javax.swing.ListSelectionModel)

---

#### void addColumnModelListener​(
TableColumnModelListener
x)

Adds a listener for table column model events.

**Parameters:**
- x

- a

TableColumnModelListener

object

---

#### void removeColumnModelListener​(
TableColumnModelListener
x)

Removes a listener for table column model events.

**Parameters:**
- x

- a

TableColumnModelListener

object

---

### Additional Sections

#### Interface TableColumnModel

**All Known Implementing Classes:** DefaultTableColumnModel

```java
public interface
TableColumnModel
```

Defines the requirements for a table column model object suitable for
use with

JTable

.

**See Also:** DefaultTableColumnModel

public interface

TableColumnModel

Defines the requirements for a table column model object suitable for
use with

JTable

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addColumn

​(

TableColumn

aColumn)

Appends

aColumn

to the end of the

tableColumns

array.

void

addColumnModelListener

​(

TableColumnModelListener

x)

Adds a listener for table column model events.

TableColumn

getColumn

​(int columnIndex)

Returns the

TableColumn

object for the column at

columnIndex

.

int

getColumnCount

()

Returns the number of columns in the model.

int

getColumnIndex

​(

Object

columnIdentifier)

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

int

getColumnIndexAtX

​(int xPosition)

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

int

getColumnMargin

()

Returns the width between the cells in each column.

Enumeration

<

TableColumn

>

getColumns

()

Returns an

Enumeration

of all the columns in the model.

boolean

getColumnSelectionAllowed

()

Returns true if columns may be selected.

int

getSelectedColumnCount

()

Returns the number of selected columns.

int[]

getSelectedColumns

()

Returns an array of indicies of all selected columns.

ListSelectionModel

getSelectionModel

()

Returns the current selection model.

int

getTotalColumnWidth

()

Returns the total width of all the columns.

void

moveColumn

​(int columnIndex,
int newIndex)

Moves the column and its header at

columnIndex

to

newIndex

.

void

removeColumn

​(

TableColumn

column)

Deletes the

TableColumn

column

from the

tableColumns

array.

void

removeColumnModelListener

​(

TableColumnModelListener

x)

Removes a listener for table column model events.

void

setColumnMargin

​(int newMargin)

Sets the

TableColumn

's column margin to

newMargin

.

void

setColumnSelectionAllowed

​(boolean flag)

Sets whether the columns in this model may be selected.

void

setSelectionModel

​(

ListSelectionModel

newModel)

Sets the selection model.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addColumn

​(

TableColumn

aColumn)

Appends

aColumn

to the end of the

tableColumns

array.

void

addColumnModelListener

​(

TableColumnModelListener

x)

Adds a listener for table column model events.

TableColumn

getColumn

​(int columnIndex)

Returns the

TableColumn

object for the column at

columnIndex

.

int

getColumnCount

()

Returns the number of columns in the model.

int

getColumnIndex

​(

Object

columnIdentifier)

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

int

getColumnIndexAtX

​(int xPosition)

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

int

getColumnMargin

()

Returns the width between the cells in each column.

Enumeration

<

TableColumn

>

getColumns

()

Returns an

Enumeration

of all the columns in the model.

boolean

getColumnSelectionAllowed

()

Returns true if columns may be selected.

int

getSelectedColumnCount

()

Returns the number of selected columns.

int[]

getSelectedColumns

()

Returns an array of indicies of all selected columns.

ListSelectionModel

getSelectionModel

()

Returns the current selection model.

int

getTotalColumnWidth

()

Returns the total width of all the columns.

void

moveColumn

​(int columnIndex,
int newIndex)

Moves the column and its header at

columnIndex

to

newIndex

.

void

removeColumn

​(

TableColumn

column)

Deletes the

TableColumn

column

from the

tableColumns

array.

void

removeColumnModelListener

​(

TableColumnModelListener

x)

Removes a listener for table column model events.

void

setColumnMargin

​(int newMargin)

Sets the

TableColumn

's column margin to

newMargin

.

void

setColumnSelectionAllowed

​(boolean flag)

Sets whether the columns in this model may be selected.

void

setSelectionModel

​(

ListSelectionModel

newModel)

Sets the selection model.

---

#### Method Summary

Appends

aColumn

to the end of the

tableColumns

array.

Adds a listener for table column model events.

Returns the

TableColumn

object for the column at

columnIndex

.

Returns the number of columns in the model.

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

Returns the width between the cells in each column.

Returns an

Enumeration

of all the columns in the model.

Returns true if columns may be selected.

Returns the number of selected columns.

Returns an array of indicies of all selected columns.

Returns the current selection model.

Returns the total width of all the columns.

Moves the column and its header at

columnIndex

to

newIndex

.

Deletes the

TableColumn

column

from the

tableColumns

array.

Removes a listener for table column model events.

Sets the

TableColumn

's column margin to

newMargin

.

Sets whether the columns in this model may be selected.

Sets the selection model.

============ METHOD DETAIL ==========

- Method Detail

- addColumn

```java
void addColumn​(
TableColumn
aColumn)
```

Appends

aColumn

to the end of the

tableColumns

array.
This method posts a

columnAdded

event to its listeners.

**Parameters:** aColumn

- the

TableColumn

to be added
**See Also:** removeColumn(javax.swing.table.TableColumn)

- removeColumn

```java
void removeColumn​(
TableColumn
column)
```

Deletes the

TableColumn

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's column list.
This method posts a

columnRemoved

event to its listeners.

**Parameters:** column

- the

TableColumn

to be removed
**See Also:** addColumn(javax.swing.table.TableColumn)

- moveColumn

```java
void moveColumn​(int columnIndex,
int newIndex)
```

Moves the column and its header at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column that used
to be at

newIndex

is shifted left or right
to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
posts a

columnMoved

event to its listeners.

**Parameters:** columnIndex

- the index of column to be moved
**Parameters:** newIndex

- index of the column's new location
**Throws:** IllegalArgumentException

- if

columnIndex

or

newIndex

are not in the valid range

- setColumnMargin

```java
void setColumnMargin​(int newMargin)
```

Sets the

TableColumn

's column margin to

newMargin

. This method posts
a

columnMarginChanged

event to its listeners.

**Parameters:** newMargin

- the width, in pixels, of the new column margins
**See Also:** getColumnMargin()

- getColumnCount

```java
int getColumnCount()
```

Returns the number of columns in the model.

**Returns:** the number of columns in the model

- getColumns

```java
Enumeration
<
TableColumn
> getColumns()
```

Returns an

Enumeration

of all the columns in the model.

**Returns:** an

Enumeration

of all the columns in the model

- getColumnIndex

```java
int getColumnIndex​(
Object
columnIdentifier)
```

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

**Parameters:** columnIdentifier

- the identifier object
**Returns:** the index of the first table column
whose identifier is equal to

identifier
**Throws:** IllegalArgumentException

- if

identifier

is

null

, or no

TableColumn

has this

identifier
**See Also:** getColumn(int)

- getColumn

```java
TableColumn
getColumn​(int columnIndex)
```

Returns the

TableColumn

object for the column at

columnIndex

.

**Parameters:** columnIndex

- the index of the desired column
**Returns:** the

TableColumn

object for
the column at

columnIndex

- getColumnMargin

```java
int getColumnMargin()
```

Returns the width between the cells in each column.

**Returns:** the margin, in pixels, between the cells

- getColumnIndexAtX

```java
int getColumnIndexAtX​(int xPosition)
```

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

In keeping with Swing's separable model architecture, a
TableColumnModel does not know how the table columns actually appear on
screen. The visual presentation of the columns is the responsibility
of the view/controller object using this model (typically JTable). The
view/controller need not display the columns sequentially from left to
right. For example, columns could be displayed from right to left to
accommodate a locale preference or some columns might be hidden at the
request of the user. Because the model does not know how the columns
are laid out on screen, the given

xPosition

should not be
considered to be a coordinate in 2D graphics space. Instead, it should
be considered to be a width from the start of the first column in the
model. If the column index for a given X coordinate in 2D space is
required,

JTable.columnAtPoint

can be used instead.

**Parameters:** xPosition

- width from the start of the first column in
the model.
**Returns:** the index of the column; or -1 if no column is found
**See Also:** JTable.columnAtPoint(java.awt.Point)

- getTotalColumnWidth

```java
int getTotalColumnWidth()
```

Returns the total width of all the columns.

**Returns:** the total computed width of all columns

- setColumnSelectionAllowed

```java
void setColumnSelectionAllowed​(boolean flag)
```

Sets whether the columns in this model may be selected.

**Parameters:** flag

- true if columns may be selected; otherwise false
**See Also:** getColumnSelectionAllowed()

- getColumnSelectionAllowed

```java
boolean getColumnSelectionAllowed()
```

Returns true if columns may be selected.

**Returns:** true if columns may be selected
**See Also:** setColumnSelectionAllowed(boolean)

- getSelectedColumns

```java
int[] getSelectedColumns()
```

Returns an array of indicies of all selected columns.

**Returns:** an array of integers containing the indicies of all
selected columns; or an empty array if nothing is selected

- getSelectedColumnCount

```java
int getSelectedColumnCount()
```

Returns the number of selected columns.

**Returns:** the number of selected columns; or 0 if no columns are selected

- setSelectionModel

```java
void setSelectionModel​(
ListSelectionModel
newModel)
```

Sets the selection model.

**Parameters:** newModel

- a

ListSelectionModel

object
**See Also:** getSelectionModel()

- getSelectionModel

```java
ListSelectionModel
getSelectionModel()
```

Returns the current selection model.

**Returns:** a

ListSelectionModel

object
**See Also:** setSelectionModel(javax.swing.ListSelectionModel)

- addColumnModelListener

```java
void addColumnModelListener​(
TableColumnModelListener
x)
```

Adds a listener for table column model events.

**Parameters:** x

- a

TableColumnModelListener

object

- removeColumnModelListener

```java
void removeColumnModelListener​(
TableColumnModelListener
x)
```

Removes a listener for table column model events.

**Parameters:** x

- a

TableColumnModelListener

object

Method Detail

- addColumn

```java
void addColumn​(
TableColumn
aColumn)
```

Appends

aColumn

to the end of the

tableColumns

array.
This method posts a

columnAdded

event to its listeners.

**Parameters:** aColumn

- the

TableColumn

to be added
**See Also:** removeColumn(javax.swing.table.TableColumn)

- removeColumn

```java
void removeColumn​(
TableColumn
column)
```

Deletes the

TableColumn

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's column list.
This method posts a

columnRemoved

event to its listeners.

**Parameters:** column

- the

TableColumn

to be removed
**See Also:** addColumn(javax.swing.table.TableColumn)

- moveColumn

```java
void moveColumn​(int columnIndex,
int newIndex)
```

Moves the column and its header at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column that used
to be at

newIndex

is shifted left or right
to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
posts a

columnMoved

event to its listeners.

**Parameters:** columnIndex

- the index of column to be moved
**Parameters:** newIndex

- index of the column's new location
**Throws:** IllegalArgumentException

- if

columnIndex

or

newIndex

are not in the valid range

- setColumnMargin

```java
void setColumnMargin​(int newMargin)
```

Sets the

TableColumn

's column margin to

newMargin

. This method posts
a

columnMarginChanged

event to its listeners.

**Parameters:** newMargin

- the width, in pixels, of the new column margins
**See Also:** getColumnMargin()

- getColumnCount

```java
int getColumnCount()
```

Returns the number of columns in the model.

**Returns:** the number of columns in the model

- getColumns

```java
Enumeration
<
TableColumn
> getColumns()
```

Returns an

Enumeration

of all the columns in the model.

**Returns:** an

Enumeration

of all the columns in the model

- getColumnIndex

```java
int getColumnIndex​(
Object
columnIdentifier)
```

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

**Parameters:** columnIdentifier

- the identifier object
**Returns:** the index of the first table column
whose identifier is equal to

identifier
**Throws:** IllegalArgumentException

- if

identifier

is

null

, or no

TableColumn

has this

identifier
**See Also:** getColumn(int)

- getColumn

```java
TableColumn
getColumn​(int columnIndex)
```

Returns the

TableColumn

object for the column at

columnIndex

.

**Parameters:** columnIndex

- the index of the desired column
**Returns:** the

TableColumn

object for
the column at

columnIndex

- getColumnMargin

```java
int getColumnMargin()
```

Returns the width between the cells in each column.

**Returns:** the margin, in pixels, between the cells

- getColumnIndexAtX

```java
int getColumnIndexAtX​(int xPosition)
```

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

In keeping with Swing's separable model architecture, a
TableColumnModel does not know how the table columns actually appear on
screen. The visual presentation of the columns is the responsibility
of the view/controller object using this model (typically JTable). The
view/controller need not display the columns sequentially from left to
right. For example, columns could be displayed from right to left to
accommodate a locale preference or some columns might be hidden at the
request of the user. Because the model does not know how the columns
are laid out on screen, the given

xPosition

should not be
considered to be a coordinate in 2D graphics space. Instead, it should
be considered to be a width from the start of the first column in the
model. If the column index for a given X coordinate in 2D space is
required,

JTable.columnAtPoint

can be used instead.

**Parameters:** xPosition

- width from the start of the first column in
the model.
**Returns:** the index of the column; or -1 if no column is found
**See Also:** JTable.columnAtPoint(java.awt.Point)

- getTotalColumnWidth

```java
int getTotalColumnWidth()
```

Returns the total width of all the columns.

**Returns:** the total computed width of all columns

- setColumnSelectionAllowed

```java
void setColumnSelectionAllowed​(boolean flag)
```

Sets whether the columns in this model may be selected.

**Parameters:** flag

- true if columns may be selected; otherwise false
**See Also:** getColumnSelectionAllowed()

- getColumnSelectionAllowed

```java
boolean getColumnSelectionAllowed()
```

Returns true if columns may be selected.

**Returns:** true if columns may be selected
**See Also:** setColumnSelectionAllowed(boolean)

- getSelectedColumns

```java
int[] getSelectedColumns()
```

Returns an array of indicies of all selected columns.

**Returns:** an array of integers containing the indicies of all
selected columns; or an empty array if nothing is selected

- getSelectedColumnCount

```java
int getSelectedColumnCount()
```

Returns the number of selected columns.

**Returns:** the number of selected columns; or 0 if no columns are selected

- setSelectionModel

```java
void setSelectionModel​(
ListSelectionModel
newModel)
```

Sets the selection model.

**Parameters:** newModel

- a

ListSelectionModel

object
**See Also:** getSelectionModel()

- getSelectionModel

```java
ListSelectionModel
getSelectionModel()
```

Returns the current selection model.

**Returns:** a

ListSelectionModel

object
**See Also:** setSelectionModel(javax.swing.ListSelectionModel)

- addColumnModelListener

```java
void addColumnModelListener​(
TableColumnModelListener
x)
```

Adds a listener for table column model events.

**Parameters:** x

- a

TableColumnModelListener

object

- removeColumnModelListener

```java
void removeColumnModelListener​(
TableColumnModelListener
x)
```

Removes a listener for table column model events.

**Parameters:** x

- a

TableColumnModelListener

object

---

#### Method Detail

addColumn

```java
void addColumn​(
TableColumn
aColumn)
```

Appends

aColumn

to the end of the

tableColumns

array.
This method posts a

columnAdded

event to its listeners.

**Parameters:** aColumn

- the

TableColumn

to be added
**See Also:** removeColumn(javax.swing.table.TableColumn)

---

#### addColumn

void addColumn​(

TableColumn

aColumn)

Appends

aColumn

to the end of the

tableColumns

array.
This method posts a

columnAdded

event to its listeners.

removeColumn

```java
void removeColumn​(
TableColumn
column)
```

Deletes the

TableColumn

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's column list.
This method posts a

columnRemoved

event to its listeners.

**Parameters:** column

- the

TableColumn

to be removed
**See Also:** addColumn(javax.swing.table.TableColumn)

---

#### removeColumn

void removeColumn​(

TableColumn

column)

Deletes the

TableColumn

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's column list.
This method posts a

columnRemoved

event to its listeners.

moveColumn

```java
void moveColumn​(int columnIndex,
int newIndex)
```

Moves the column and its header at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column that used
to be at

newIndex

is shifted left or right
to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
posts a

columnMoved

event to its listeners.

**Parameters:** columnIndex

- the index of column to be moved
**Parameters:** newIndex

- index of the column's new location
**Throws:** IllegalArgumentException

- if

columnIndex

or

newIndex

are not in the valid range

---

#### moveColumn

void moveColumn​(int columnIndex,
int newIndex)

Moves the column and its header at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column that used
to be at

newIndex

is shifted left or right
to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
posts a

columnMoved

event to its listeners.

setColumnMargin

```java
void setColumnMargin​(int newMargin)
```

Sets the

TableColumn

's column margin to

newMargin

. This method posts
a

columnMarginChanged

event to its listeners.

**Parameters:** newMargin

- the width, in pixels, of the new column margins
**See Also:** getColumnMargin()

---

#### setColumnMargin

void setColumnMargin​(int newMargin)

Sets the

TableColumn

's column margin to

newMargin

. This method posts
a

columnMarginChanged

event to its listeners.

getColumnCount

```java
int getColumnCount()
```

Returns the number of columns in the model.

**Returns:** the number of columns in the model

---

#### getColumnCount

int getColumnCount()

Returns the number of columns in the model.

getColumns

```java
Enumeration
<
TableColumn
> getColumns()
```

Returns an

Enumeration

of all the columns in the model.

**Returns:** an

Enumeration

of all the columns in the model

---

#### getColumns

Enumeration

<

TableColumn

> getColumns()

Returns an

Enumeration

of all the columns in the model.

getColumnIndex

```java
int getColumnIndex​(
Object
columnIdentifier)
```

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

**Parameters:** columnIdentifier

- the identifier object
**Returns:** the index of the first table column
whose identifier is equal to

identifier
**Throws:** IllegalArgumentException

- if

identifier

is

null

, or no

TableColumn

has this

identifier
**See Also:** getColumn(int)

---

#### getColumnIndex

int getColumnIndex​(

Object

columnIdentifier)

Returns the index of the first column in the table
whose identifier is equal to

identifier

,
when compared using

equals

.

getColumn

```java
TableColumn
getColumn​(int columnIndex)
```

Returns the

TableColumn

object for the column at

columnIndex

.

**Parameters:** columnIndex

- the index of the desired column
**Returns:** the

TableColumn

object for
the column at

columnIndex

---

#### getColumn

TableColumn

getColumn​(int columnIndex)

Returns the

TableColumn

object for the column at

columnIndex

.

getColumnMargin

```java
int getColumnMargin()
```

Returns the width between the cells in each column.

**Returns:** the margin, in pixels, between the cells

---

#### getColumnMargin

int getColumnMargin()

Returns the width between the cells in each column.

getColumnIndexAtX

```java
int getColumnIndexAtX​(int xPosition)
```

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

In keeping with Swing's separable model architecture, a
TableColumnModel does not know how the table columns actually appear on
screen. The visual presentation of the columns is the responsibility
of the view/controller object using this model (typically JTable). The
view/controller need not display the columns sequentially from left to
right. For example, columns could be displayed from right to left to
accommodate a locale preference or some columns might be hidden at the
request of the user. Because the model does not know how the columns
are laid out on screen, the given

xPosition

should not be
considered to be a coordinate in 2D graphics space. Instead, it should
be considered to be a width from the start of the first column in the
model. If the column index for a given X coordinate in 2D space is
required,

JTable.columnAtPoint

can be used instead.

**Parameters:** xPosition

- width from the start of the first column in
the model.
**Returns:** the index of the column; or -1 if no column is found
**See Also:** JTable.columnAtPoint(java.awt.Point)

---

#### getColumnIndexAtX

int getColumnIndexAtX​(int xPosition)

Returns the index of the column that lies on the
horizontal point,

xPosition

;
or -1 if it lies outside the any of the column's bounds.

In keeping with Swing's separable model architecture, a
TableColumnModel does not know how the table columns actually appear on
screen. The visual presentation of the columns is the responsibility
of the view/controller object using this model (typically JTable). The
view/controller need not display the columns sequentially from left to
right. For example, columns could be displayed from right to left to
accommodate a locale preference or some columns might be hidden at the
request of the user. Because the model does not know how the columns
are laid out on screen, the given

xPosition

should not be
considered to be a coordinate in 2D graphics space. Instead, it should
be considered to be a width from the start of the first column in the
model. If the column index for a given X coordinate in 2D space is
required,

JTable.columnAtPoint

can be used instead.

getTotalColumnWidth

```java
int getTotalColumnWidth()
```

Returns the total width of all the columns.

**Returns:** the total computed width of all columns

---

#### getTotalColumnWidth

int getTotalColumnWidth()

Returns the total width of all the columns.

setColumnSelectionAllowed

```java
void setColumnSelectionAllowed​(boolean flag)
```

Sets whether the columns in this model may be selected.

**Parameters:** flag

- true if columns may be selected; otherwise false
**See Also:** getColumnSelectionAllowed()

---

#### setColumnSelectionAllowed

void setColumnSelectionAllowed​(boolean flag)

Sets whether the columns in this model may be selected.

getColumnSelectionAllowed

```java
boolean getColumnSelectionAllowed()
```

Returns true if columns may be selected.

**Returns:** true if columns may be selected
**See Also:** setColumnSelectionAllowed(boolean)

---

#### getColumnSelectionAllowed

boolean getColumnSelectionAllowed()

Returns true if columns may be selected.

getSelectedColumns

```java
int[] getSelectedColumns()
```

Returns an array of indicies of all selected columns.

**Returns:** an array of integers containing the indicies of all
selected columns; or an empty array if nothing is selected

---

#### getSelectedColumns

int[] getSelectedColumns()

Returns an array of indicies of all selected columns.

getSelectedColumnCount

```java
int getSelectedColumnCount()
```

Returns the number of selected columns.

**Returns:** the number of selected columns; or 0 if no columns are selected

---

#### getSelectedColumnCount

int getSelectedColumnCount()

Returns the number of selected columns.

setSelectionModel

```java
void setSelectionModel​(
ListSelectionModel
newModel)
```

Sets the selection model.

**Parameters:** newModel

- a

ListSelectionModel

object
**See Also:** getSelectionModel()

---

#### setSelectionModel

void setSelectionModel​(

ListSelectionModel

newModel)

Sets the selection model.

getSelectionModel

```java
ListSelectionModel
getSelectionModel()
```

Returns the current selection model.

**Returns:** a

ListSelectionModel

object
**See Also:** setSelectionModel(javax.swing.ListSelectionModel)

---

#### getSelectionModel

ListSelectionModel

getSelectionModel()

Returns the current selection model.

addColumnModelListener

```java
void addColumnModelListener​(
TableColumnModelListener
x)
```

Adds a listener for table column model events.

**Parameters:** x

- a

TableColumnModelListener

object

---

#### addColumnModelListener

void addColumnModelListener​(

TableColumnModelListener

x)

Adds a listener for table column model events.

removeColumnModelListener

```java
void removeColumnModelListener​(
TableColumnModelListener
x)
```

Removes a listener for table column model events.

**Parameters:** x

- a

TableColumnModelListener

object

---

#### removeColumnModelListener

void removeColumnModelListener​(

TableColumnModelListener

x)

Removes a listener for table column model events.

---

