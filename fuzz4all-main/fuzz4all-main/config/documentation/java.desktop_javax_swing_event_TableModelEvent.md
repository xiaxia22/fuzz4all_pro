# Class TableModelEvent

**Source:** `java.desktop\javax\swing\event\TableModelEvent.html`

### Class Description

```java
public class
TableModelEvent

extends
EventObject
```

TableModelEvent is used to notify listeners that a table model
has changed. The model event describes changes to a TableModel
and all references to rows and columns are in the co-ordinate
system of the model.
Depending on the parameters used in the constructors, the TableModelevent
can be used to specify the following types of changes:

```java
TableModelEvent(source); // The data, ie. all rows changed
TableModelEvent(source, HEADER_ROW); // Structure change, reallocate TableColumns
TableModelEvent(source, 1); // Row 1 changed
TableModelEvent(source, 3, 6); // Rows 3 to 6 inclusive changed
TableModelEvent(source, 2, 2, 6); // Cell at (2, 6) changed
TableModelEvent(source, 3, 6, ALL_COLUMNS, INSERT); // Rows (3, 6) were inserted
TableModelEvent(source, 3, 6, ALL_COLUMNS, DELETE); // Rows (3, 6) were deleted
```

It is possible to use other combinations of the parameters, not all of them
are meaningful. By subclassing, you can add other information, for example:
whether the event WILL happen or DID happen. This makes the specification
of rows in DELETE events more useful but has not been included in
the swing package as the JTable only needs post-event notification.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int INSERT

Identifies the addition of new rows or columns.

**See Also:**
- Constant Field Values

---

#### public static final int UPDATE

Identifies a change to existing data.

**See Also:**
- Constant Field Values

---

#### public static final int DELETE

Identifies the removal of rows or columns.

**See Also:**
- Constant Field Values

---

#### public static final int HEADER_ROW

Identifies the header row.

**See Also:**
- Constant Field Values

---

#### public static final int ALL_COLUMNS

Specifies all columns in a row or rows.

**See Also:**
- Constant Field Values

---

#### protected int type

The type of the event.

---

#### protected int firstRow

The first row that has changed.

---

#### protected int lastRow

The last row that has changed.

---

#### protected int column

The column for the event.

---

### Constructor Details

#### public TableModelEvent​(
TableModel
source)

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.
The

JTable

will repaint the entire visible region on
receiving this event, querying the model for the cell values that are visible.
The structure of the table ie, the column names, types and order
have not changed.

**Parameters:**
- source

- the

TableModel

affected by this event

---

#### public TableModelEvent​(
TableModel
source,
int row)

This row of data has been updated.
To denote the arrival of a completely new table with a different structure
use

HEADER_ROW

as the value for the

row

.
When the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any TableColumns that it had and reallocates
default ones in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**Parameters:**
- source

- the

TableModel

affected by this event
- row

- the row which has been updated

---

#### public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow)

The data in rows [

firstRow

,

lastRow

] have been updated.

**Parameters:**
- source

- the

TableModel

affected by this event
- firstRow

- the first row affected by this event
- lastRow

- the last row affected by this event

---

#### public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column)

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

**Parameters:**
- source

- the

TableModel

affected by this event
- firstRow

- the first row affected by this event
- lastRow

- the last row affected by this event
- column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.

---

#### public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column,
int type)

The cells from (firstRow, column) to (lastRow, column) have been changed.
The

column

refers to the column index of the cell in the model's
co-ordinate system. When

column

is ALL_COLUMNS, all cells in the
specified range of rows are considered changed.

The

type

should be one of: INSERT, UPDATE and DELETE.

**Parameters:**
- source

- the

TableModel

affected by this event
- firstRow

- the first row affected by this event
- lastRow

- the last row affected by this event
- column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.
- type

- the type of change signified by this even,

INSERT

,

DELETE

or

UPDATE

---

### Method Details

#### public int getFirstRow()

Returns the first row that changed. HEADER_ROW means the meta data,
ie. names, types and order of the columns.

**Returns:**
- an integer signifying the first row changed

---

#### public int getLastRow()

Returns the last row that changed.

**Returns:**
- an integer signifying the last row changed

---

#### public int getColumn()

Returns the column for the event. If the return
value is ALL_COLUMNS; it means every column in the specified
rows changed.

**Returns:**
- an integer signifying which column is affected by this event

---

#### public int getType()

Returns the type of event - one of: INSERT, UPDATE and DELETE.

**Returns:**
- the type of change to a table model, an

INSERT

or

DELETE

of row(s) or column(s) or

UPDATE

to data

---

### Additional Sections

#### Class TableModelEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.TableModelEvent

java.util.EventObject

- javax.swing.event.TableModelEvent

javax.swing.event.TableModelEvent

**All Implemented Interfaces:** Serializable

```java
public class
TableModelEvent

extends
EventObject
```

TableModelEvent is used to notify listeners that a table model
has changed. The model event describes changes to a TableModel
and all references to rows and columns are in the co-ordinate
system of the model.
Depending on the parameters used in the constructors, the TableModelevent
can be used to specify the following types of changes:

```java
TableModelEvent(source); // The data, ie. all rows changed
TableModelEvent(source, HEADER_ROW); // Structure change, reallocate TableColumns
TableModelEvent(source, 1); // Row 1 changed
TableModelEvent(source, 3, 6); // Rows 3 to 6 inclusive changed
TableModelEvent(source, 2, 2, 6); // Cell at (2, 6) changed
TableModelEvent(source, 3, 6, ALL_COLUMNS, INSERT); // Rows (3, 6) were inserted
TableModelEvent(source, 3, 6, ALL_COLUMNS, DELETE); // Rows (3, 6) were deleted
```

It is possible to use other combinations of the parameters, not all of them
are meaningful. By subclassing, you can add other information, for example:
whether the event WILL happen or DID happen. This makes the specification
of rows in DELETE events more useful but has not been included in
the swing package as the JTable only needs post-event notification.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** TableModel

,

Serialized Form

public class

TableModelEvent

extends

EventObject

TableModelEvent is used to notify listeners that a table model
has changed. The model event describes changes to a TableModel
and all references to rows and columns are in the co-ordinate
system of the model.
Depending on the parameters used in the constructors, the TableModelevent
can be used to specify the following types of changes:

```java
TableModelEvent(source); // The data, ie. all rows changed
TableModelEvent(source, HEADER_ROW); // Structure change, reallocate TableColumns
TableModelEvent(source, 1); // Row 1 changed
TableModelEvent(source, 3, 6); // Rows 3 to 6 inclusive changed
TableModelEvent(source, 2, 2, 6); // Cell at (2, 6) changed
TableModelEvent(source, 3, 6, ALL_COLUMNS, INSERT); // Rows (3, 6) were inserted
TableModelEvent(source, 3, 6, ALL_COLUMNS, DELETE); // Rows (3, 6) were deleted
```

It is possible to use other combinations of the parameters, not all of them
are meaningful. By subclassing, you can add other information, for example:
whether the event WILL happen or DID happen. This makes the specification
of rows in DELETE events more useful but has not been included in
the swing package as the JTable only needs post-event notification.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

TableModelEvent(source); // The data, ie. all rows changed
TableModelEvent(source, HEADER_ROW); // Structure change, reallocate TableColumns
TableModelEvent(source, 1); // Row 1 changed
TableModelEvent(source, 3, 6); // Rows 3 to 6 inclusive changed
TableModelEvent(source, 2, 2, 6); // Cell at (2, 6) changed
TableModelEvent(source, 3, 6, ALL_COLUMNS, INSERT); // Rows (3, 6) were inserted
TableModelEvent(source, 3, 6, ALL_COLUMNS, DELETE); // Rows (3, 6) were deleted

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALL_COLUMNS

Specifies all columns in a row or rows.

protected int

column

The column for the event.

static int

DELETE

Identifies the removal of rows or columns.

protected int

firstRow

The first row that has changed.

static int

HEADER_ROW

Identifies the header row.

static int

INSERT

Identifies the addition of new rows or columns.

protected int

lastRow

The last row that has changed.

protected int

type

The type of the event.

static int

UPDATE

Identifies a change to existing data.

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TableModelEvent

​(

TableModel

source)

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.

TableModelEvent

​(

TableModel

source,
int row)

This row of data has been updated.

TableModelEvent

​(

TableModel

source,
int firstRow,
int lastRow)

The data in rows [

firstRow

,

lastRow

] have been updated.

TableModelEvent

​(

TableModel

source,
int firstRow,
int lastRow,
int column)

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

TableModelEvent

​(

TableModel

source,
int firstRow,
int lastRow,
int column,
int type)

The cells from (firstRow, column) to (lastRow, column) have been changed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumn

()

Returns the column for the event.

int

getFirstRow

()

Returns the first row that changed.

int

getLastRow

()

Returns the last row that changed.

int

getType

()

Returns the type of event - one of: INSERT, UPDATE and DELETE.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

static int

ALL_COLUMNS

Specifies all columns in a row or rows.

protected int

column

The column for the event.

static int

DELETE

Identifies the removal of rows or columns.

protected int

firstRow

The first row that has changed.

static int

HEADER_ROW

Identifies the header row.

static int

INSERT

Identifies the addition of new rows or columns.

protected int

lastRow

The last row that has changed.

protected int

type

The type of the event.

static int

UPDATE

Identifies a change to existing data.

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Specifies all columns in a row or rows.

The column for the event.

Identifies the removal of rows or columns.

The first row that has changed.

Identifies the header row.

Identifies the addition of new rows or columns.

The last row that has changed.

The type of the event.

Identifies a change to existing data.

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

TableModelEvent

​(

TableModel

source)

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.

TableModelEvent

​(

TableModel

source,
int row)

This row of data has been updated.

TableModelEvent

​(

TableModel

source,
int firstRow,
int lastRow)

The data in rows [

firstRow

,

lastRow

] have been updated.

TableModelEvent

​(

TableModel

source,
int firstRow,
int lastRow,
int column)

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

TableModelEvent

​(

TableModel

source,
int firstRow,
int lastRow,
int column,
int type)

The cells from (firstRow, column) to (lastRow, column) have been changed.

---

#### Constructor Summary

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.

This row of data has been updated.

The data in rows [

firstRow

,

lastRow

] have been updated.

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

The cells from (firstRow, column) to (lastRow, column) have been changed.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumn

()

Returns the column for the event.

int

getFirstRow

()

Returns the first row that changed.

int

getLastRow

()

Returns the last row that changed.

int

getType

()

Returns the type of event - one of: INSERT, UPDATE and DELETE.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the column for the event.

Returns the first row that changed.

Returns the last row that changed.

Returns the type of event - one of: INSERT, UPDATE and DELETE.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- INSERT

```java
public static final int INSERT
```

Identifies the addition of new rows or columns.

**See Also:** Constant Field Values

- UPDATE

```java
public static final int UPDATE
```

Identifies a change to existing data.

**See Also:** Constant Field Values

- DELETE

```java
public static final int DELETE
```

Identifies the removal of rows or columns.

**See Also:** Constant Field Values

- HEADER_ROW

```java
public static final int HEADER_ROW
```

Identifies the header row.

**See Also:** Constant Field Values

- ALL_COLUMNS

```java
public static final int ALL_COLUMNS
```

Specifies all columns in a row or rows.

**See Also:** Constant Field Values

- type

```java
protected int type
```

The type of the event.

- firstRow

```java
protected int firstRow
```

The first row that has changed.

- lastRow

```java
protected int lastRow
```

The last row that has changed.

- column

```java
protected int column
```

The column for the event.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source)
```

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.
The

JTable

will repaint the entire visible region on
receiving this event, querying the model for the cell values that are visible.
The structure of the table ie, the column names, types and order
have not changed.

**Parameters:** source

- the

TableModel

affected by this event

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int row)
```

This row of data has been updated.
To denote the arrival of a completely new table with a different structure
use

HEADER_ROW

as the value for the

row

.
When the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any TableColumns that it had and reallocates
default ones in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** row

- the row which has been updated

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow)
```

The data in rows [

firstRow

,

lastRow

] have been updated.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column)
```

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event
**Parameters:** column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column,
int type)
```

The cells from (firstRow, column) to (lastRow, column) have been changed.
The

column

refers to the column index of the cell in the model's
co-ordinate system. When

column

is ALL_COLUMNS, all cells in the
specified range of rows are considered changed.

The

type

should be one of: INSERT, UPDATE and DELETE.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event
**Parameters:** column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.
**Parameters:** type

- the type of change signified by this even,

INSERT

,

DELETE

or

UPDATE

============ METHOD DETAIL ==========

- Method Detail

- getFirstRow

```java
public int getFirstRow()
```

Returns the first row that changed. HEADER_ROW means the meta data,
ie. names, types and order of the columns.

**Returns:** an integer signifying the first row changed

- getLastRow

```java
public int getLastRow()
```

Returns the last row that changed.

**Returns:** an integer signifying the last row changed

- getColumn

```java
public int getColumn()
```

Returns the column for the event. If the return
value is ALL_COLUMNS; it means every column in the specified
rows changed.

**Returns:** an integer signifying which column is affected by this event

- getType

```java
public int getType()
```

Returns the type of event - one of: INSERT, UPDATE and DELETE.

**Returns:** the type of change to a table model, an

INSERT

or

DELETE

of row(s) or column(s) or

UPDATE

to data

Field Detail

- INSERT

```java
public static final int INSERT
```

Identifies the addition of new rows or columns.

**See Also:** Constant Field Values

- UPDATE

```java
public static final int UPDATE
```

Identifies a change to existing data.

**See Also:** Constant Field Values

- DELETE

```java
public static final int DELETE
```

Identifies the removal of rows or columns.

**See Also:** Constant Field Values

- HEADER_ROW

```java
public static final int HEADER_ROW
```

Identifies the header row.

**See Also:** Constant Field Values

- ALL_COLUMNS

```java
public static final int ALL_COLUMNS
```

Specifies all columns in a row or rows.

**See Also:** Constant Field Values

- type

```java
protected int type
```

The type of the event.

- firstRow

```java
protected int firstRow
```

The first row that has changed.

- lastRow

```java
protected int lastRow
```

The last row that has changed.

- column

```java
protected int column
```

The column for the event.

---

#### Field Detail

INSERT

```java
public static final int INSERT
```

Identifies the addition of new rows or columns.

**See Also:** Constant Field Values

---

#### INSERT

public static final int INSERT

Identifies the addition of new rows or columns.

UPDATE

```java
public static final int UPDATE
```

Identifies a change to existing data.

**See Also:** Constant Field Values

---

#### UPDATE

public static final int UPDATE

Identifies a change to existing data.

DELETE

```java
public static final int DELETE
```

Identifies the removal of rows or columns.

**See Also:** Constant Field Values

---

#### DELETE

public static final int DELETE

Identifies the removal of rows or columns.

HEADER_ROW

```java
public static final int HEADER_ROW
```

Identifies the header row.

**See Also:** Constant Field Values

---

#### HEADER_ROW

public static final int HEADER_ROW

Identifies the header row.

ALL_COLUMNS

```java
public static final int ALL_COLUMNS
```

Specifies all columns in a row or rows.

**See Also:** Constant Field Values

---

#### ALL_COLUMNS

public static final int ALL_COLUMNS

Specifies all columns in a row or rows.

type

```java
protected int type
```

The type of the event.

---

#### type

protected int type

The type of the event.

firstRow

```java
protected int firstRow
```

The first row that has changed.

---

#### firstRow

protected int firstRow

The first row that has changed.

lastRow

```java
protected int lastRow
```

The last row that has changed.

---

#### lastRow

protected int lastRow

The last row that has changed.

column

```java
protected int column
```

The column for the event.

---

#### column

protected int column

The column for the event.

Constructor Detail

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source)
```

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.
The

JTable

will repaint the entire visible region on
receiving this event, querying the model for the cell values that are visible.
The structure of the table ie, the column names, types and order
have not changed.

**Parameters:** source

- the

TableModel

affected by this event

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int row)
```

This row of data has been updated.
To denote the arrival of a completely new table with a different structure
use

HEADER_ROW

as the value for the

row

.
When the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any TableColumns that it had and reallocates
default ones in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** row

- the row which has been updated

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow)
```

The data in rows [

firstRow

,

lastRow

] have been updated.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column)
```

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event
**Parameters:** column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.

- TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column,
int type)
```

The cells from (firstRow, column) to (lastRow, column) have been changed.
The

column

refers to the column index of the cell in the model's
co-ordinate system. When

column

is ALL_COLUMNS, all cells in the
specified range of rows are considered changed.

The

type

should be one of: INSERT, UPDATE and DELETE.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event
**Parameters:** column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.
**Parameters:** type

- the type of change signified by this even,

INSERT

,

DELETE

or

UPDATE

---

#### Constructor Detail

TableModelEvent

```java
public TableModelEvent​(
TableModel
source)
```

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.
The

JTable

will repaint the entire visible region on
receiving this event, querying the model for the cell values that are visible.
The structure of the table ie, the column names, types and order
have not changed.

**Parameters:** source

- the

TableModel

affected by this event

---

#### TableModelEvent

public TableModelEvent​(

TableModel

source)

All row data in the table has changed, listeners should discard any state
that was based on the rows and requery the

TableModel

to get the new row count and all the appropriate values.
The

JTable

will repaint the entire visible region on
receiving this event, querying the model for the cell values that are visible.
The structure of the table ie, the column names, types and order
have not changed.

TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int row)
```

This row of data has been updated.
To denote the arrival of a completely new table with a different structure
use

HEADER_ROW

as the value for the

row

.
When the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any TableColumns that it had and reallocates
default ones in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** row

- the row which has been updated

---

#### TableModelEvent

public TableModelEvent​(

TableModel

source,
int row)

This row of data has been updated.
To denote the arrival of a completely new table with a different structure
use

HEADER_ROW

as the value for the

row

.
When the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any TableColumns that it had and reallocates
default ones in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow)
```

The data in rows [

firstRow

,

lastRow

] have been updated.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event

---

#### TableModelEvent

public TableModelEvent​(

TableModel

source,
int firstRow,
int lastRow)

The data in rows [

firstRow

,

lastRow

] have been updated.

TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column)
```

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event
**Parameters:** column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.

---

#### TableModelEvent

public TableModelEvent​(

TableModel

source,
int firstRow,
int lastRow,
int column)

The cells in column

column

in the range
[

firstRow

,

lastRow

] have been updated.

TableModelEvent

```java
public TableModelEvent​(
TableModel
source,
int firstRow,
int lastRow,
int column,
int type)
```

The cells from (firstRow, column) to (lastRow, column) have been changed.
The

column

refers to the column index of the cell in the model's
co-ordinate system. When

column

is ALL_COLUMNS, all cells in the
specified range of rows are considered changed.

The

type

should be one of: INSERT, UPDATE and DELETE.

**Parameters:** source

- the

TableModel

affected by this event
**Parameters:** firstRow

- the first row affected by this event
**Parameters:** lastRow

- the last row affected by this event
**Parameters:** column

- the column index of cells changed;

ALL_COLUMNS

signifies all cells in the specified range of rows are changed.
**Parameters:** type

- the type of change signified by this even,

INSERT

,

DELETE

or

UPDATE

---

#### TableModelEvent

public TableModelEvent​(

TableModel

source,
int firstRow,
int lastRow,
int column,
int type)

The cells from (firstRow, column) to (lastRow, column) have been changed.
The

column

refers to the column index of the cell in the model's
co-ordinate system. When

column

is ALL_COLUMNS, all cells in the
specified range of rows are considered changed.

The

type

should be one of: INSERT, UPDATE and DELETE.

The

type

should be one of: INSERT, UPDATE and DELETE.

Method Detail

- getFirstRow

```java
public int getFirstRow()
```

Returns the first row that changed. HEADER_ROW means the meta data,
ie. names, types and order of the columns.

**Returns:** an integer signifying the first row changed

- getLastRow

```java
public int getLastRow()
```

Returns the last row that changed.

**Returns:** an integer signifying the last row changed

- getColumn

```java
public int getColumn()
```

Returns the column for the event. If the return
value is ALL_COLUMNS; it means every column in the specified
rows changed.

**Returns:** an integer signifying which column is affected by this event

- getType

```java
public int getType()
```

Returns the type of event - one of: INSERT, UPDATE and DELETE.

**Returns:** the type of change to a table model, an

INSERT

or

DELETE

of row(s) or column(s) or

UPDATE

to data

---

#### Method Detail

getFirstRow

```java
public int getFirstRow()
```

Returns the first row that changed. HEADER_ROW means the meta data,
ie. names, types and order of the columns.

**Returns:** an integer signifying the first row changed

---

#### getFirstRow

public int getFirstRow()

Returns the first row that changed. HEADER_ROW means the meta data,
ie. names, types and order of the columns.

getLastRow

```java
public int getLastRow()
```

Returns the last row that changed.

**Returns:** an integer signifying the last row changed

---

#### getLastRow

public int getLastRow()

Returns the last row that changed.

getColumn

```java
public int getColumn()
```

Returns the column for the event. If the return
value is ALL_COLUMNS; it means every column in the specified
rows changed.

**Returns:** an integer signifying which column is affected by this event

---

#### getColumn

public int getColumn()

Returns the column for the event. If the return
value is ALL_COLUMNS; it means every column in the specified
rows changed.

getType

```java
public int getType()
```

Returns the type of event - one of: INSERT, UPDATE and DELETE.

**Returns:** the type of change to a table model, an

INSERT

or

DELETE

of row(s) or column(s) or

UPDATE

to data

---

#### getType

public int getType()

Returns the type of event - one of: INSERT, UPDATE and DELETE.

---

