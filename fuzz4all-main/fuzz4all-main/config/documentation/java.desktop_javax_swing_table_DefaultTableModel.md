# Class DefaultTableModel

**Source:** `java.desktop\javax\swing\table\DefaultTableModel.html`

### Class Description

```java
public class
DefaultTableModel

extends
AbstractTableModel

implements
Serializable
```

This is an implementation of

TableModel

that
uses a

Vector

of

Vectors

to store the
cell value objects.

Warning:

DefaultTableModel

returns a
column class of

Object

. When

DefaultTableModel

is used with a

TableRowSorter

this will result in extensive use of

toString

, which for non-

String

data types
is expensive. If you use

DefaultTableModel

with a

TableRowSorter

you are strongly encouraged to override

getColumnClass

to return the appropriate type.

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

,

TableModel

---

### Field Details

#### protected
Vector
<
Vector
> dataVector

The

Vector

of

Vectors

of

Object

values.

---

#### protected
Vector
columnIdentifiers

The

Vector

of column identifiers.

---

### Constructor Details

#### public DefaultTableModel()

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

---

#### public DefaultTableModel​(int rowCount,
int columnCount)

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

**Parameters:**
- rowCount

- the number of rows the table holds
- columnCount

- the number of columns the table holds

**See Also:**
- setValueAt(java.lang.Object, int, int)

---

#### public DefaultTableModel​(
Vector
<?> columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

vector.

**Parameters:**
- columnNames

-

vector

containing the names
of the new columns; if this is

null

then the model has no columns
- rowCount

- the number of rows the table holds

**See Also:**
- setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

---

#### public DefaultTableModel​(
Object
[] columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

array.

**Parameters:**
- columnNames

-

array

containing the names
of the new columns; if this is

null

then the model has no columns
- rowCount

- the number of rows the table holds

**See Also:**
- setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

---

#### public DefaultTableModel​(
Vector
<? extends
Vector
> data,

Vector
<?> columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

**Parameters:**
- data

- the data of the table, a

Vector

of

Vector

s of

Object

values
- columnNames

-

vector

containing the names
of the new columns

**See Also:**
- getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

---

#### public DefaultTableModel​(
Object
[][] data,

Object
[] columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method. The first index in the

Object[][]

array is
the row index and the second is the column index.

**Parameters:**
- data

- the data of the table
- columnNames

- the names of the columns

**See Also:**
- getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

---

### Method Details

#### public
Vector
<
Vector
> getDataVector()

Returns the

Vector

of

Vectors

that contains the table's
data values. The vectors contained in the outer vector are
each a single row of values. In other words, to get to the cell
at row 1, column 5:

((Vector)getDataVector().elementAt(1)).elementAt(5);

**Returns:**
- the vector of vectors containing the tables data values

**See Also:**
- newDataAvailable(javax.swing.event.TableModelEvent)

,

newRowsAdded(javax.swing.event.TableModelEvent)

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

---

#### public void setDataVector​(
Vector
<? extends
Vector
> dataVector,

Vector
<?> columnIdentifiers)

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.
Each row is represented in

dataVector

as a

Vector

of

Object

values.

columnIdentifiers

are the names of the new
columns. The first name in

columnIdentifiers

is
mapped to column 0 in

dataVector

. Each row in

dataVector

is adjusted to match the number of
columns in

columnIdentifiers

either by truncating the

Vector

if it is too long,
or adding

null

values if it is too short.

Note that passing in a

null

value for

dataVector

results in unspecified behavior,
an possibly an exception.

**Parameters:**
- dataVector

- the new data vector
- columnIdentifiers

- the names of the columns

**See Also:**
- getDataVector()

---

#### public void setDataVector​(
Object
[][] dataVector,

Object
[] columnIdentifiers)

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.
The first index in the

Object[][]

array is the row index and the second is the column index.

columnIdentifiers

are the names of the new columns.

**Parameters:**
- dataVector

- the new data vector
- columnIdentifiers

- the names of the columns

**See Also:**
- setDataVector(Vector, Vector)

---

#### public void newDataAvailable​(
TableModelEvent
event)

Equivalent to

fireTableChanged

.

**Parameters:**
- event

- the change event

---

#### public void newRowsAdded​(
TableModelEvent
e)

Ensures that the new rows have the correct number of columns.
This is accomplished by using the

setSize

method in

Vector

which truncates vectors
which are too long, and appends

null

s if they
are too short.
This method also sends out a

tableChanged

notification message to all the listeners.

**Parameters:**
- e

- this

TableModelEvent

describes
where the rows were added.
If

null

it assumes
all the rows were newly added

**See Also:**
- getDataVector()

---

#### public void rowsRemoved​(
TableModelEvent
event)

Equivalent to

fireTableChanged

.

**Parameters:**
- event

- the change event

---

#### public void setNumRows​(int rowCount)

Obsolete as of Java 2 platform v1.3. Please use

setRowCount

instead.

**Parameters:**
- rowCount

- the new number of rows

---

#### public void setRowCount​(int rowCount)

Sets the number of rows in the model. If the new size is greater
than the current size, new rows are added to the end of the model
If the new size is less than the current size, all
rows at index

rowCount

and greater are discarded.

**Parameters:**
- rowCount

- number of rows in the model

**See Also:**
- setColumnCount(int)

**Since:**
- 1.3

---

#### public void addRow​(
Vector
<?> rowData)

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:**
- rowData

- optional data of the row being added

---

#### public void addRow​(
Object
[] rowData)

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:**
- rowData

- optional data of the row being added

---

#### public void insertRow​(int row,

Vector
<?> rowData)

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:**
- row

- the row index of the row to be inserted
- rowData

- optional data of the row being added

**Throws:**
- ArrayIndexOutOfBoundsException

- if the row was invalid

---

#### public void insertRow​(int row,

Object
[] rowData)

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:**
- row

- the row index of the row to be inserted
- rowData

- optional data of the row being added

**Throws:**
- ArrayIndexOutOfBoundsException

- if the row was invalid

---

#### public void moveRow​(int start,
int end,
int to)

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.
After the move, the row that was at index

start

will be at index

to

.
This method will send a

tableChanged

notification
message to all the listeners.

```java
Examples of moves:

1. moveRow(1,3,5);
a|B|C|D|e|f|g|h|i|j|k - before
a|e|f|g|h|B|C|D|i|j|k - after

2. moveRow(6,7,1);
a|b|c|d|e|f|G|H|i|j|k - before
a|G|H|b|c|d|e|f|i|j|k - after
```

**Parameters:**
- start

- the starting row index to be moved
- end

- the ending row index to be moved
- to

- the destination of the rows to be moved

**Throws:**
- ArrayIndexOutOfBoundsException

- if any of the elements
would be moved out of the table's range

---

#### public void removeRow​(int row)

Removes the row at

row

from the model. Notification
of the row being removed will be sent to all the listeners.

**Parameters:**
- row

- the row index of the row to be removed

**Throws:**
- ArrayIndexOutOfBoundsException

- if the row was invalid

---

#### public void setColumnIdentifiers​(
Vector
<?> columnIdentifiers)

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:**
- columnIdentifiers

- vector of column identifiers. If

null

, set the model
to zero columns

**See Also:**
- setNumRows(int)

---

#### public void setColumnIdentifiers​(
Object
[] newIdentifiers)

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:**
- newIdentifiers

- array of column identifiers.
If

null

, set
the model to zero columns

**See Also:**
- setNumRows(int)

---

#### public void setColumnCount​(int columnCount)

Sets the number of columns in the model. If the new size is greater
than the current size, new columns are added to the end of the model
with

null

cell values.
If the new size is less than the current size, all columns at index

columnCount

and greater are discarded.

**Parameters:**
- columnCount

- the new number of columns in the model

**See Also:**
- setColumnCount(int)

**Since:**
- 1.3

---

#### public void addColumn​(
Object
columnName)

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null. This method
will send a

tableChanged

notification message to all the listeners.
This method is a cover for

addColumn(Object, Vector)

which
uses

null

as the data vector.

**Parameters:**
- columnName

- the identifier of the column being added

---

#### public void addColumn​(
Object
columnName,

Vector
<?> columnData)

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null.

columnData

is the
optional vector of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:**
- columnName

- the identifier of the column being added
- columnData

- optional data of the column being added

---

#### public void addColumn​(
Object
columnName,

Object
[] columnData)

Adds a column to the model. The new column will have the
identifier

columnName

.

columnData

is the
optional array of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:**
- columnName

- identifier of the newly created column
- columnData

- new data to be added to the column

**See Also:**
- addColumn(Object, Vector)

---

#### public int getRowCount()

Returns the number of rows in this data table.

**Specified by:**
- getRowCount

in interface

TableModel

**Returns:**
- the number of rows in the model

**See Also:**
- TableModel.getColumnCount()

---

#### public int getColumnCount()

Returns the number of columns in this data table.

**Specified by:**
- getColumnCount

in interface

TableModel

**Returns:**
- the number of columns in the model

**See Also:**
- TableModel.getRowCount()

---

#### public
String
getColumnName​(int column)

Returns the column name.

**Specified by:**
- getColumnName

in interface

TableModel

**Overrides:**
- getColumnName

in class

AbstractTableModel

**Parameters:**
- column

- the column being queried

**Returns:**
- a name for this column using the string value of the
appropriate member in

columnIdentifiers

.
If

columnIdentifiers

does not have an entry
for this index, returns the default
name provided by the superclass.

---

#### public boolean isCellEditable​(int row,
int column)

Returns true regardless of parameter values.

**Specified by:**
- isCellEditable

in interface

TableModel

**Overrides:**
- isCellEditable

in class

AbstractTableModel

**Parameters:**
- row

- the row whose value is to be queried
- column

- the column whose value is to be queried

**Returns:**
- true

**See Also:**
- setValueAt(java.lang.Object, int, int)

---

#### public
Object
getValueAt​(int row,
int column)

Returns an attribute value for the cell at

row

and

column

.

**Specified by:**
- getValueAt

in interface

TableModel

**Parameters:**
- row

- the row whose value is to be queried
- column

- the column whose value is to be queried

**Returns:**
- the value Object at the specified cell

**Throws:**
- ArrayIndexOutOfBoundsException

- if an invalid row or
column was given

---

#### public void setValueAt​(
Object
aValue,
int row,
int column)

Sets the object value for the cell at

column

and

row

.

aValue

is the new value. This method
will generate a

tableChanged

notification.

**Specified by:**
- setValueAt

in interface

TableModel

**Overrides:**
- setValueAt

in class

AbstractTableModel

**Parameters:**
- aValue

- the new value; this can be null
- row

- the row whose value is to be changed
- column

- the column whose value is to be changed

**Throws:**
- ArrayIndexOutOfBoundsException

- if an invalid row or
column was given

**See Also:**
- TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

---

#### protected static
Vector
<
Object
> convertToVector​(
Object
[] anArray)

Returns a vector that contains the same objects as the array.

**Parameters:**
- anArray

- the array to be converted

**Returns:**
- the new vector; if

anArray

is

null

,
returns

null

---

#### protected static
Vector
<
Vector
<
Object
>> convertToVector​(
Object
[][] anArray)

Returns a vector of vectors that contains the same objects as the array.

**Parameters:**
- anArray

- the double array to be converted

**Returns:**
- the new vector of vectors; if

anArray

is

null

, returns

null

---

### Additional Sections

#### Class DefaultTableModel

java.lang.Object

- javax.swing.table.AbstractTableModel
- - javax.swing.table.DefaultTableModel

javax.swing.table.AbstractTableModel

- javax.swing.table.DefaultTableModel

javax.swing.table.DefaultTableModel

**All Implemented Interfaces:** Serializable

,

TableModel

```java
public class
DefaultTableModel

extends
AbstractTableModel

implements
Serializable
```

This is an implementation of

TableModel

that
uses a

Vector

of

Vectors

to store the
cell value objects.

Warning:

DefaultTableModel

returns a
column class of

Object

. When

DefaultTableModel

is used with a

TableRowSorter

this will result in extensive use of

toString

, which for non-

String

data types
is expensive. If you use

DefaultTableModel

with a

TableRowSorter

you are strongly encouraged to override

getColumnClass

to return the appropriate type.

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

getDataVector()

,

Serialized Form

public class

DefaultTableModel

extends

AbstractTableModel

implements

Serializable

This is an implementation of

TableModel

that
uses a

Vector

of

Vectors

to store the
cell value objects.

Warning:

DefaultTableModel

returns a
column class of

Object

. When

DefaultTableModel

is used with a

TableRowSorter

this will result in extensive use of

toString

, which for non-

String

data types
is expensive. If you use

DefaultTableModel

with a

TableRowSorter

you are strongly encouraged to override

getColumnClass

to return the appropriate type.

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

Warning:

DefaultTableModel

returns a
column class of

Object

. When

DefaultTableModel

is used with a

TableRowSorter

this will result in extensive use of

toString

, which for non-

String

data types
is expensive. If you use

DefaultTableModel

with a

TableRowSorter

you are strongly encouraged to override

getColumnClass

to return the appropriate type.

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

protected

Vector

columnIdentifiers

The

Vector

of column identifiers.

protected

Vector

<

Vector

>

dataVector

The

Vector

of

Vectors

of

Object

values.

- Fields declared in class javax.swing.table.

AbstractTableModel

listenerList

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultTableModel

()

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

DefaultTableModel

​(int rowCount,
int columnCount)

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

DefaultTableModel

​(

Object

[][] data,

Object

[] columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

DefaultTableModel

​(

Object

[] columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values.

DefaultTableModel

​(

Vector

<?> columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values.

DefaultTableModel

​(

Vector

<? extends

Vector

> data,

Vector

<?> columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addColumn

​(

Object

columnName)

Adds a column to the model.

void

addColumn

​(

Object

columnName,

Object

[] columnData)

Adds a column to the model.

void

addColumn

​(

Object

columnName,

Vector

<?> columnData)

Adds a column to the model.

void

addRow

​(

Object

[] rowData)

Adds a row to the end of the model.

void

addRow

​(

Vector

<?> rowData)

Adds a row to the end of the model.

protected static

Vector

<

Object

>

convertToVector

​(

Object

[] anArray)

Returns a vector that contains the same objects as the array.

protected static

Vector

<

Vector

<

Object

>>

convertToVector

​(

Object

[][] anArray)

Returns a vector of vectors that contains the same objects as the array.

int

getColumnCount

()

Returns the number of columns in this data table.

String

getColumnName

​(int column)

Returns the column name.

Vector

<

Vector

>

getDataVector

()

Returns the

Vector

of

Vectors

that contains the table's
data values.

int

getRowCount

()

Returns the number of rows in this data table.

Object

getValueAt

​(int row,
int column)

Returns an attribute value for the cell at

row

and

column

.

void

insertRow

​(int row,

Object

[] rowData)

Inserts a row at

row

in the model.

void

insertRow

​(int row,

Vector

<?> rowData)

Inserts a row at

row

in the model.

boolean

isCellEditable

​(int row,
int column)

Returns true regardless of parameter values.

void

moveRow

​(int start,
int end,
int to)

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.

void

newDataAvailable

​(

TableModelEvent

event)

Equivalent to

fireTableChanged

.

void

newRowsAdded

​(

TableModelEvent

e)

Ensures that the new rows have the correct number of columns.

void

removeRow

​(int row)

Removes the row at

row

from the model.

void

rowsRemoved

​(

TableModelEvent

event)

Equivalent to

fireTableChanged

.

void

setColumnCount

​(int columnCount)

Sets the number of columns in the model.

void

setColumnIdentifiers

​(

Object

[] newIdentifiers)

Replaces the column identifiers in the model.

void

setColumnIdentifiers

​(

Vector

<?> columnIdentifiers)

Replaces the column identifiers in the model.

void

setDataVector

​(

Object

[][] dataVector,

Object

[] columnIdentifiers)

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.

void

setDataVector

​(

Vector

<? extends

Vector

> dataVector,

Vector

<?> columnIdentifiers)

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.

void

setNumRows

​(int rowCount)

Obsolete as of Java 2 platform v1.3.

void

setRowCount

​(int rowCount)

Sets the number of rows in the model.

void

setValueAt

​(

Object

aValue,
int row,
int column)

Sets the object value for the cell at

column

and

row

.

- Methods declared in class javax.swing.table.

AbstractTableModel

addTableModelListener

,

findColumn

,

fireTableCellUpdated

,

fireTableChanged

,

fireTableDataChanged

,

fireTableRowsDeleted

,

fireTableRowsInserted

,

fireTableRowsUpdated

,

fireTableStructureChanged

,

getColumnClass

,

getListeners

,

getTableModelListeners

,

removeTableModelListener

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

protected

Vector

columnIdentifiers

The

Vector

of column identifiers.

protected

Vector

<

Vector

>

dataVector

The

Vector

of

Vectors

of

Object

values.

- Fields declared in class javax.swing.table.

AbstractTableModel

listenerList

---

#### Field Summary

The

Vector

of column identifiers.

The

Vector

of

Vectors

of

Object

values.

Fields declared in class javax.swing.table.

AbstractTableModel

listenerList

---

#### Fields declared in class javax.swing.table. AbstractTableModel

Constructor Summary

Constructors

Constructor

Description

DefaultTableModel

()

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

DefaultTableModel

​(int rowCount,
int columnCount)

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

DefaultTableModel

​(

Object

[][] data,

Object

[] columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

DefaultTableModel

​(

Object

[] columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values.

DefaultTableModel

​(

Vector

<?> columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values.

DefaultTableModel

​(

Vector

<? extends

Vector

> data,

Vector

<?> columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

---

#### Constructor Summary

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values.

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addColumn

​(

Object

columnName)

Adds a column to the model.

void

addColumn

​(

Object

columnName,

Object

[] columnData)

Adds a column to the model.

void

addColumn

​(

Object

columnName,

Vector

<?> columnData)

Adds a column to the model.

void

addRow

​(

Object

[] rowData)

Adds a row to the end of the model.

void

addRow

​(

Vector

<?> rowData)

Adds a row to the end of the model.

protected static

Vector

<

Object

>

convertToVector

​(

Object

[] anArray)

Returns a vector that contains the same objects as the array.

protected static

Vector

<

Vector

<

Object

>>

convertToVector

​(

Object

[][] anArray)

Returns a vector of vectors that contains the same objects as the array.

int

getColumnCount

()

Returns the number of columns in this data table.

String

getColumnName

​(int column)

Returns the column name.

Vector

<

Vector

>

getDataVector

()

Returns the

Vector

of

Vectors

that contains the table's
data values.

int

getRowCount

()

Returns the number of rows in this data table.

Object

getValueAt

​(int row,
int column)

Returns an attribute value for the cell at

row

and

column

.

void

insertRow

​(int row,

Object

[] rowData)

Inserts a row at

row

in the model.

void

insertRow

​(int row,

Vector

<?> rowData)

Inserts a row at

row

in the model.

boolean

isCellEditable

​(int row,
int column)

Returns true regardless of parameter values.

void

moveRow

​(int start,
int end,
int to)

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.

void

newDataAvailable

​(

TableModelEvent

event)

Equivalent to

fireTableChanged

.

void

newRowsAdded

​(

TableModelEvent

e)

Ensures that the new rows have the correct number of columns.

void

removeRow

​(int row)

Removes the row at

row

from the model.

void

rowsRemoved

​(

TableModelEvent

event)

Equivalent to

fireTableChanged

.

void

setColumnCount

​(int columnCount)

Sets the number of columns in the model.

void

setColumnIdentifiers

​(

Object

[] newIdentifiers)

Replaces the column identifiers in the model.

void

setColumnIdentifiers

​(

Vector

<?> columnIdentifiers)

Replaces the column identifiers in the model.

void

setDataVector

​(

Object

[][] dataVector,

Object

[] columnIdentifiers)

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.

void

setDataVector

​(

Vector

<? extends

Vector

> dataVector,

Vector

<?> columnIdentifiers)

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.

void

setNumRows

​(int rowCount)

Obsolete as of Java 2 platform v1.3.

void

setRowCount

​(int rowCount)

Sets the number of rows in the model.

void

setValueAt

​(

Object

aValue,
int row,
int column)

Sets the object value for the cell at

column

and

row

.

- Methods declared in class javax.swing.table.

AbstractTableModel

addTableModelListener

,

findColumn

,

fireTableCellUpdated

,

fireTableChanged

,

fireTableDataChanged

,

fireTableRowsDeleted

,

fireTableRowsInserted

,

fireTableRowsUpdated

,

fireTableStructureChanged

,

getColumnClass

,

getListeners

,

getTableModelListeners

,

removeTableModelListener

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

Adds a column to the model.

Adds a row to the end of the model.

Returns a vector that contains the same objects as the array.

Returns a vector of vectors that contains the same objects as the array.

Returns the number of columns in this data table.

Returns the column name.

Returns the

Vector

of

Vectors

that contains the table's
data values.

Returns the number of rows in this data table.

Returns an attribute value for the cell at

row

and

column

.

Inserts a row at

row

in the model.

Returns true regardless of parameter values.

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.

Equivalent to

fireTableChanged

.

Ensures that the new rows have the correct number of columns.

Removes the row at

row

from the model.

Sets the number of columns in the model.

Replaces the column identifiers in the model.

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.

Obsolete as of Java 2 platform v1.3.

Sets the number of rows in the model.

Sets the object value for the cell at

column

and

row

.

Methods declared in class javax.swing.table.

AbstractTableModel

addTableModelListener

,

findColumn

,

fireTableCellUpdated

,

fireTableChanged

,

fireTableDataChanged

,

fireTableRowsDeleted

,

fireTableRowsInserted

,

fireTableRowsUpdated

,

fireTableStructureChanged

,

getColumnClass

,

getListeners

,

getTableModelListeners

,

removeTableModelListener

---

#### Methods declared in class javax.swing.table. AbstractTableModel

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

- dataVector

```java
protected
Vector
<
Vector
> dataVector
```

The

Vector

of

Vectors

of

Object

values.

- columnIdentifiers

```java
protected
Vector
columnIdentifiers
```

The

Vector

of column identifiers.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultTableModel

```java
public DefaultTableModel()
```

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

- DefaultTableModel

```java
public DefaultTableModel​(int rowCount,
int columnCount)
```

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

**Parameters:** rowCount

- the number of rows the table holds
**Parameters:** columnCount

- the number of columns the table holds
**See Also:** setValueAt(java.lang.Object, int, int)

- DefaultTableModel

```java
public DefaultTableModel​(
Vector
<?> columnNames,
int rowCount)
```

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

vector.

**Parameters:** columnNames

-

vector

containing the names
of the new columns; if this is

null

then the model has no columns
**Parameters:** rowCount

- the number of rows the table holds
**See Also:** setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

- DefaultTableModel

```java
public DefaultTableModel​(
Object
[] columnNames,
int rowCount)
```

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

array.

**Parameters:** columnNames

-

array

containing the names
of the new columns; if this is

null

then the model has no columns
**Parameters:** rowCount

- the number of rows the table holds
**See Also:** setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

- DefaultTableModel

```java
public DefaultTableModel​(
Vector
<? extends
Vector
> data,

Vector
<?> columnNames)
```

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

**Parameters:** data

- the data of the table, a

Vector

of

Vector

s of

Object

values
**Parameters:** columnNames

-

vector

containing the names
of the new columns
**See Also:** getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

- DefaultTableModel

```java
public DefaultTableModel​(
Object
[][] data,

Object
[] columnNames)
```

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method. The first index in the

Object[][]

array is
the row index and the second is the column index.

**Parameters:** data

- the data of the table
**Parameters:** columnNames

- the names of the columns
**See Also:** getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

============ METHOD DETAIL ==========

- Method Detail

- getDataVector

```java
public
Vector
<
Vector
> getDataVector()
```

Returns the

Vector

of

Vectors

that contains the table's
data values. The vectors contained in the outer vector are
each a single row of values. In other words, to get to the cell
at row 1, column 5:

((Vector)getDataVector().elementAt(1)).elementAt(5);

**Returns:** the vector of vectors containing the tables data values
**See Also:** newDataAvailable(javax.swing.event.TableModelEvent)

,

newRowsAdded(javax.swing.event.TableModelEvent)

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

- setDataVector

```java
public void setDataVector​(
Vector
<? extends
Vector
> dataVector,

Vector
<?> columnIdentifiers)
```

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.
Each row is represented in

dataVector

as a

Vector

of

Object

values.

columnIdentifiers

are the names of the new
columns. The first name in

columnIdentifiers

is
mapped to column 0 in

dataVector

. Each row in

dataVector

is adjusted to match the number of
columns in

columnIdentifiers

either by truncating the

Vector

if it is too long,
or adding

null

values if it is too short.

Note that passing in a

null

value for

dataVector

results in unspecified behavior,
an possibly an exception.

**Parameters:** dataVector

- the new data vector
**Parameters:** columnIdentifiers

- the names of the columns
**See Also:** getDataVector()

- setDataVector

```java
public void setDataVector​(
Object
[][] dataVector,

Object
[] columnIdentifiers)
```

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.
The first index in the

Object[][]

array is the row index and the second is the column index.

columnIdentifiers

are the names of the new columns.

**Parameters:** dataVector

- the new data vector
**Parameters:** columnIdentifiers

- the names of the columns
**See Also:** setDataVector(Vector, Vector)

- newDataAvailable

```java
public void newDataAvailable​(
TableModelEvent
event)
```

Equivalent to

fireTableChanged

.

**Parameters:** event

- the change event

- newRowsAdded

```java
public void newRowsAdded​(
TableModelEvent
e)
```

Ensures that the new rows have the correct number of columns.
This is accomplished by using the

setSize

method in

Vector

which truncates vectors
which are too long, and appends

null

s if they
are too short.
This method also sends out a

tableChanged

notification message to all the listeners.

**Parameters:** e

- this

TableModelEvent

describes
where the rows were added.
If

null

it assumes
all the rows were newly added
**See Also:** getDataVector()

- rowsRemoved

```java
public void rowsRemoved​(
TableModelEvent
event)
```

Equivalent to

fireTableChanged

.

**Parameters:** event

- the change event

- setNumRows

```java
public void setNumRows​(int rowCount)
```

Obsolete as of Java 2 platform v1.3. Please use

setRowCount

instead.

**Parameters:** rowCount

- the new number of rows

- setRowCount

```java
public void setRowCount​(int rowCount)
```

Sets the number of rows in the model. If the new size is greater
than the current size, new rows are added to the end of the model
If the new size is less than the current size, all
rows at index

rowCount

and greater are discarded.

**Parameters:** rowCount

- number of rows in the model
**Since:** 1.3
**See Also:** setColumnCount(int)

- addRow

```java
public void addRow​(
Vector
<?> rowData)
```

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:** rowData

- optional data of the row being added

- addRow

```java
public void addRow​(
Object
[] rowData)
```

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:** rowData

- optional data of the row being added

- insertRow

```java
public void insertRow​(int row,

Vector
<?> rowData)
```

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:** row

- the row index of the row to be inserted
**Parameters:** rowData

- optional data of the row being added
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

- insertRow

```java
public void insertRow​(int row,

Object
[] rowData)
```

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:** row

- the row index of the row to be inserted
**Parameters:** rowData

- optional data of the row being added
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

- moveRow

```java
public void moveRow​(int start,
int end,
int to)
```

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.
After the move, the row that was at index

start

will be at index

to

.
This method will send a

tableChanged

notification
message to all the listeners.

```java
Examples of moves:

1. moveRow(1,3,5);
a|B|C|D|e|f|g|h|i|j|k - before
a|e|f|g|h|B|C|D|i|j|k - after

2. moveRow(6,7,1);
a|b|c|d|e|f|G|H|i|j|k - before
a|G|H|b|c|d|e|f|i|j|k - after
```

**Parameters:** start

- the starting row index to be moved
**Parameters:** end

- the ending row index to be moved
**Parameters:** to

- the destination of the rows to be moved
**Throws:** ArrayIndexOutOfBoundsException

- if any of the elements
would be moved out of the table's range

- removeRow

```java
public void removeRow​(int row)
```

Removes the row at

row

from the model. Notification
of the row being removed will be sent to all the listeners.

**Parameters:** row

- the row index of the row to be removed
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

- setColumnIdentifiers

```java
public void setColumnIdentifiers​(
Vector
<?> columnIdentifiers)
```

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:** columnIdentifiers

- vector of column identifiers. If

null

, set the model
to zero columns
**See Also:** setNumRows(int)

- setColumnIdentifiers

```java
public void setColumnIdentifiers​(
Object
[] newIdentifiers)
```

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:** newIdentifiers

- array of column identifiers.
If

null

, set
the model to zero columns
**See Also:** setNumRows(int)

- setColumnCount

```java
public void setColumnCount​(int columnCount)
```

Sets the number of columns in the model. If the new size is greater
than the current size, new columns are added to the end of the model
with

null

cell values.
If the new size is less than the current size, all columns at index

columnCount

and greater are discarded.

**Parameters:** columnCount

- the new number of columns in the model
**Since:** 1.3
**See Also:** setColumnCount(int)

- addColumn

```java
public void addColumn​(
Object
columnName)
```

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null. This method
will send a

tableChanged

notification message to all the listeners.
This method is a cover for

addColumn(Object, Vector)

which
uses

null

as the data vector.

**Parameters:** columnName

- the identifier of the column being added

- addColumn

```java
public void addColumn​(
Object
columnName,

Vector
<?> columnData)
```

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null.

columnData

is the
optional vector of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:** columnName

- the identifier of the column being added
**Parameters:** columnData

- optional data of the column being added

- addColumn

```java
public void addColumn​(
Object
columnName,

Object
[] columnData)
```

Adds a column to the model. The new column will have the
identifier

columnName

.

columnData

is the
optional array of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:** columnName

- identifier of the newly created column
**Parameters:** columnData

- new data to be added to the column
**See Also:** addColumn(Object, Vector)

- getRowCount

```java
public int getRowCount()
```

Returns the number of rows in this data table.

**Specified by:** getRowCount

in interface

TableModel
**Returns:** the number of rows in the model
**See Also:** TableModel.getColumnCount()

- getColumnCount

```java
public int getColumnCount()
```

Returns the number of columns in this data table.

**Specified by:** getColumnCount

in interface

TableModel
**Returns:** the number of columns in the model
**See Also:** TableModel.getRowCount()

- getColumnName

```java
public
String
getColumnName​(int column)
```

Returns the column name.

**Specified by:** getColumnName

in interface

TableModel
**Overrides:** getColumnName

in class

AbstractTableModel
**Parameters:** column

- the column being queried
**Returns:** a name for this column using the string value of the
appropriate member in

columnIdentifiers

.
If

columnIdentifiers

does not have an entry
for this index, returns the default
name provided by the superclass.

- isCellEditable

```java
public boolean isCellEditable​(int row,
int column)
```

Returns true regardless of parameter values.

**Specified by:** isCellEditable

in interface

TableModel
**Overrides:** isCellEditable

in class

AbstractTableModel
**Parameters:** row

- the row whose value is to be queried
**Parameters:** column

- the column whose value is to be queried
**Returns:** true
**See Also:** setValueAt(java.lang.Object, int, int)

- getValueAt

```java
public
Object
getValueAt​(int row,
int column)
```

Returns an attribute value for the cell at

row

and

column

.

**Specified by:** getValueAt

in interface

TableModel
**Parameters:** row

- the row whose value is to be queried
**Parameters:** column

- the column whose value is to be queried
**Returns:** the value Object at the specified cell
**Throws:** ArrayIndexOutOfBoundsException

- if an invalid row or
column was given

- setValueAt

```java
public void setValueAt​(
Object
aValue,
int row,
int column)
```

Sets the object value for the cell at

column

and

row

.

aValue

is the new value. This method
will generate a

tableChanged

notification.

**Specified by:** setValueAt

in interface

TableModel
**Overrides:** setValueAt

in class

AbstractTableModel
**Parameters:** aValue

- the new value; this can be null
**Parameters:** row

- the row whose value is to be changed
**Parameters:** column

- the column whose value is to be changed
**Throws:** ArrayIndexOutOfBoundsException

- if an invalid row or
column was given
**See Also:** TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

- convertToVector

```java
protected static
Vector
<
Object
> convertToVector​(
Object
[] anArray)
```

Returns a vector that contains the same objects as the array.

**Parameters:** anArray

- the array to be converted
**Returns:** the new vector; if

anArray

is

null

,
returns

null

- convertToVector

```java
protected static
Vector
<
Vector
<
Object
>> convertToVector​(
Object
[][] anArray)
```

Returns a vector of vectors that contains the same objects as the array.

**Parameters:** anArray

- the double array to be converted
**Returns:** the new vector of vectors; if

anArray

is

null

, returns

null

Field Detail

- dataVector

```java
protected
Vector
<
Vector
> dataVector
```

The

Vector

of

Vectors

of

Object

values.

- columnIdentifiers

```java
protected
Vector
columnIdentifiers
```

The

Vector

of column identifiers.

---

#### Field Detail

dataVector

```java
protected
Vector
<
Vector
> dataVector
```

The

Vector

of

Vectors

of

Object

values.

---

#### dataVector

protected

Vector

<

Vector

> dataVector

The

Vector

of

Vectors

of

Object

values.

columnIdentifiers

```java
protected
Vector
columnIdentifiers
```

The

Vector

of column identifiers.

---

#### columnIdentifiers

protected

Vector

columnIdentifiers

The

Vector

of column identifiers.

Constructor Detail

- DefaultTableModel

```java
public DefaultTableModel()
```

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

- DefaultTableModel

```java
public DefaultTableModel​(int rowCount,
int columnCount)
```

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

**Parameters:** rowCount

- the number of rows the table holds
**Parameters:** columnCount

- the number of columns the table holds
**See Also:** setValueAt(java.lang.Object, int, int)

- DefaultTableModel

```java
public DefaultTableModel​(
Vector
<?> columnNames,
int rowCount)
```

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

vector.

**Parameters:** columnNames

-

vector

containing the names
of the new columns; if this is

null

then the model has no columns
**Parameters:** rowCount

- the number of rows the table holds
**See Also:** setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

- DefaultTableModel

```java
public DefaultTableModel​(
Object
[] columnNames,
int rowCount)
```

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

array.

**Parameters:** columnNames

-

array

containing the names
of the new columns; if this is

null

then the model has no columns
**Parameters:** rowCount

- the number of rows the table holds
**See Also:** setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

- DefaultTableModel

```java
public DefaultTableModel​(
Vector
<? extends
Vector
> data,

Vector
<?> columnNames)
```

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

**Parameters:** data

- the data of the table, a

Vector

of

Vector

s of

Object

values
**Parameters:** columnNames

-

vector

containing the names
of the new columns
**See Also:** getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

- DefaultTableModel

```java
public DefaultTableModel​(
Object
[][] data,

Object
[] columnNames)
```

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method. The first index in the

Object[][]

array is
the row index and the second is the column index.

**Parameters:** data

- the data of the table
**Parameters:** columnNames

- the names of the columns
**See Also:** getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

---

#### Constructor Detail

DefaultTableModel

```java
public DefaultTableModel()
```

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

---

#### DefaultTableModel

public DefaultTableModel()

Constructs a default

DefaultTableModel

which is a table of zero columns and zero rows.

DefaultTableModel

```java
public DefaultTableModel​(int rowCount,
int columnCount)
```

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

**Parameters:** rowCount

- the number of rows the table holds
**Parameters:** columnCount

- the number of columns the table holds
**See Also:** setValueAt(java.lang.Object, int, int)

---

#### DefaultTableModel

public DefaultTableModel​(int rowCount,
int columnCount)

Constructs a

DefaultTableModel

with

rowCount

and

columnCount

of

null

object values.

DefaultTableModel

```java
public DefaultTableModel​(
Vector
<?> columnNames,
int rowCount)
```

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

vector.

**Parameters:** columnNames

-

vector

containing the names
of the new columns; if this is

null

then the model has no columns
**Parameters:** rowCount

- the number of rows the table holds
**See Also:** setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

---

#### DefaultTableModel

public DefaultTableModel​(

Vector

<?> columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many columns
as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

vector.

DefaultTableModel

```java
public DefaultTableModel​(
Object
[] columnNames,
int rowCount)
```

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

array.

**Parameters:** columnNames

-

array

containing the names
of the new columns; if this is

null

then the model has no columns
**Parameters:** rowCount

- the number of rows the table holds
**See Also:** setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

,

setValueAt(java.lang.Object, int, int)

---

#### DefaultTableModel

public DefaultTableModel​(

Object

[] columnNames,
int rowCount)

Constructs a

DefaultTableModel

with as many
columns as there are elements in

columnNames

and

rowCount

of

null

object values. Each column's name will be taken from
the

columnNames

array.

DefaultTableModel

```java
public DefaultTableModel​(
Vector
<? extends
Vector
> data,

Vector
<?> columnNames)
```

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

**Parameters:** data

- the data of the table, a

Vector

of

Vector

s of

Object

values
**Parameters:** columnNames

-

vector

containing the names
of the new columns
**See Also:** getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

---

#### DefaultTableModel

public DefaultTableModel​(

Vector

<? extends

Vector

> data,

Vector

<?> columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method.

DefaultTableModel

```java
public DefaultTableModel​(
Object
[][] data,

Object
[] columnNames)
```

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method. The first index in the

Object[][]

array is
the row index and the second is the column index.

**Parameters:** data

- the data of the table
**Parameters:** columnNames

- the names of the columns
**See Also:** getDataVector()

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

---

#### DefaultTableModel

public DefaultTableModel​(

Object

[][] data,

Object

[] columnNames)

Constructs a

DefaultTableModel

and initializes the table
by passing

data

and

columnNames

to the

setDataVector

method. The first index in the

Object[][]

array is
the row index and the second is the column index.

Method Detail

- getDataVector

```java
public
Vector
<
Vector
> getDataVector()
```

Returns the

Vector

of

Vectors

that contains the table's
data values. The vectors contained in the outer vector are
each a single row of values. In other words, to get to the cell
at row 1, column 5:

((Vector)getDataVector().elementAt(1)).elementAt(5);

**Returns:** the vector of vectors containing the tables data values
**See Also:** newDataAvailable(javax.swing.event.TableModelEvent)

,

newRowsAdded(javax.swing.event.TableModelEvent)

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

- setDataVector

```java
public void setDataVector​(
Vector
<? extends
Vector
> dataVector,

Vector
<?> columnIdentifiers)
```

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.
Each row is represented in

dataVector

as a

Vector

of

Object

values.

columnIdentifiers

are the names of the new
columns. The first name in

columnIdentifiers

is
mapped to column 0 in

dataVector

. Each row in

dataVector

is adjusted to match the number of
columns in

columnIdentifiers

either by truncating the

Vector

if it is too long,
or adding

null

values if it is too short.

Note that passing in a

null

value for

dataVector

results in unspecified behavior,
an possibly an exception.

**Parameters:** dataVector

- the new data vector
**Parameters:** columnIdentifiers

- the names of the columns
**See Also:** getDataVector()

- setDataVector

```java
public void setDataVector​(
Object
[][] dataVector,

Object
[] columnIdentifiers)
```

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.
The first index in the

Object[][]

array is the row index and the second is the column index.

columnIdentifiers

are the names of the new columns.

**Parameters:** dataVector

- the new data vector
**Parameters:** columnIdentifiers

- the names of the columns
**See Also:** setDataVector(Vector, Vector)

- newDataAvailable

```java
public void newDataAvailable​(
TableModelEvent
event)
```

Equivalent to

fireTableChanged

.

**Parameters:** event

- the change event

- newRowsAdded

```java
public void newRowsAdded​(
TableModelEvent
e)
```

Ensures that the new rows have the correct number of columns.
This is accomplished by using the

setSize

method in

Vector

which truncates vectors
which are too long, and appends

null

s if they
are too short.
This method also sends out a

tableChanged

notification message to all the listeners.

**Parameters:** e

- this

TableModelEvent

describes
where the rows were added.
If

null

it assumes
all the rows were newly added
**See Also:** getDataVector()

- rowsRemoved

```java
public void rowsRemoved​(
TableModelEvent
event)
```

Equivalent to

fireTableChanged

.

**Parameters:** event

- the change event

- setNumRows

```java
public void setNumRows​(int rowCount)
```

Obsolete as of Java 2 platform v1.3. Please use

setRowCount

instead.

**Parameters:** rowCount

- the new number of rows

- setRowCount

```java
public void setRowCount​(int rowCount)
```

Sets the number of rows in the model. If the new size is greater
than the current size, new rows are added to the end of the model
If the new size is less than the current size, all
rows at index

rowCount

and greater are discarded.

**Parameters:** rowCount

- number of rows in the model
**Since:** 1.3
**See Also:** setColumnCount(int)

- addRow

```java
public void addRow​(
Vector
<?> rowData)
```

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:** rowData

- optional data of the row being added

- addRow

```java
public void addRow​(
Object
[] rowData)
```

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:** rowData

- optional data of the row being added

- insertRow

```java
public void insertRow​(int row,

Vector
<?> rowData)
```

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:** row

- the row index of the row to be inserted
**Parameters:** rowData

- optional data of the row being added
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

- insertRow

```java
public void insertRow​(int row,

Object
[] rowData)
```

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:** row

- the row index of the row to be inserted
**Parameters:** rowData

- optional data of the row being added
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

- moveRow

```java
public void moveRow​(int start,
int end,
int to)
```

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.
After the move, the row that was at index

start

will be at index

to

.
This method will send a

tableChanged

notification
message to all the listeners.

```java
Examples of moves:

1. moveRow(1,3,5);
a|B|C|D|e|f|g|h|i|j|k - before
a|e|f|g|h|B|C|D|i|j|k - after

2. moveRow(6,7,1);
a|b|c|d|e|f|G|H|i|j|k - before
a|G|H|b|c|d|e|f|i|j|k - after
```

**Parameters:** start

- the starting row index to be moved
**Parameters:** end

- the ending row index to be moved
**Parameters:** to

- the destination of the rows to be moved
**Throws:** ArrayIndexOutOfBoundsException

- if any of the elements
would be moved out of the table's range

- removeRow

```java
public void removeRow​(int row)
```

Removes the row at

row

from the model. Notification
of the row being removed will be sent to all the listeners.

**Parameters:** row

- the row index of the row to be removed
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

- setColumnIdentifiers

```java
public void setColumnIdentifiers​(
Vector
<?> columnIdentifiers)
```

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:** columnIdentifiers

- vector of column identifiers. If

null

, set the model
to zero columns
**See Also:** setNumRows(int)

- setColumnIdentifiers

```java
public void setColumnIdentifiers​(
Object
[] newIdentifiers)
```

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:** newIdentifiers

- array of column identifiers.
If

null

, set
the model to zero columns
**See Also:** setNumRows(int)

- setColumnCount

```java
public void setColumnCount​(int columnCount)
```

Sets the number of columns in the model. If the new size is greater
than the current size, new columns are added to the end of the model
with

null

cell values.
If the new size is less than the current size, all columns at index

columnCount

and greater are discarded.

**Parameters:** columnCount

- the new number of columns in the model
**Since:** 1.3
**See Also:** setColumnCount(int)

- addColumn

```java
public void addColumn​(
Object
columnName)
```

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null. This method
will send a

tableChanged

notification message to all the listeners.
This method is a cover for

addColumn(Object, Vector)

which
uses

null

as the data vector.

**Parameters:** columnName

- the identifier of the column being added

- addColumn

```java
public void addColumn​(
Object
columnName,

Vector
<?> columnData)
```

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null.

columnData

is the
optional vector of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:** columnName

- the identifier of the column being added
**Parameters:** columnData

- optional data of the column being added

- addColumn

```java
public void addColumn​(
Object
columnName,

Object
[] columnData)
```

Adds a column to the model. The new column will have the
identifier

columnName

.

columnData

is the
optional array of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:** columnName

- identifier of the newly created column
**Parameters:** columnData

- new data to be added to the column
**See Also:** addColumn(Object, Vector)

- getRowCount

```java
public int getRowCount()
```

Returns the number of rows in this data table.

**Specified by:** getRowCount

in interface

TableModel
**Returns:** the number of rows in the model
**See Also:** TableModel.getColumnCount()

- getColumnCount

```java
public int getColumnCount()
```

Returns the number of columns in this data table.

**Specified by:** getColumnCount

in interface

TableModel
**Returns:** the number of columns in the model
**See Also:** TableModel.getRowCount()

- getColumnName

```java
public
String
getColumnName​(int column)
```

Returns the column name.

**Specified by:** getColumnName

in interface

TableModel
**Overrides:** getColumnName

in class

AbstractTableModel
**Parameters:** column

- the column being queried
**Returns:** a name for this column using the string value of the
appropriate member in

columnIdentifiers

.
If

columnIdentifiers

does not have an entry
for this index, returns the default
name provided by the superclass.

- isCellEditable

```java
public boolean isCellEditable​(int row,
int column)
```

Returns true regardless of parameter values.

**Specified by:** isCellEditable

in interface

TableModel
**Overrides:** isCellEditable

in class

AbstractTableModel
**Parameters:** row

- the row whose value is to be queried
**Parameters:** column

- the column whose value is to be queried
**Returns:** true
**See Also:** setValueAt(java.lang.Object, int, int)

- getValueAt

```java
public
Object
getValueAt​(int row,
int column)
```

Returns an attribute value for the cell at

row

and

column

.

**Specified by:** getValueAt

in interface

TableModel
**Parameters:** row

- the row whose value is to be queried
**Parameters:** column

- the column whose value is to be queried
**Returns:** the value Object at the specified cell
**Throws:** ArrayIndexOutOfBoundsException

- if an invalid row or
column was given

- setValueAt

```java
public void setValueAt​(
Object
aValue,
int row,
int column)
```

Sets the object value for the cell at

column

and

row

.

aValue

is the new value. This method
will generate a

tableChanged

notification.

**Specified by:** setValueAt

in interface

TableModel
**Overrides:** setValueAt

in class

AbstractTableModel
**Parameters:** aValue

- the new value; this can be null
**Parameters:** row

- the row whose value is to be changed
**Parameters:** column

- the column whose value is to be changed
**Throws:** ArrayIndexOutOfBoundsException

- if an invalid row or
column was given
**See Also:** TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

- convertToVector

```java
protected static
Vector
<
Object
> convertToVector​(
Object
[] anArray)
```

Returns a vector that contains the same objects as the array.

**Parameters:** anArray

- the array to be converted
**Returns:** the new vector; if

anArray

is

null

,
returns

null

- convertToVector

```java
protected static
Vector
<
Vector
<
Object
>> convertToVector​(
Object
[][] anArray)
```

Returns a vector of vectors that contains the same objects as the array.

**Parameters:** anArray

- the double array to be converted
**Returns:** the new vector of vectors; if

anArray

is

null

, returns

null

---

#### Method Detail

getDataVector

```java
public
Vector
<
Vector
> getDataVector()
```

Returns the

Vector

of

Vectors

that contains the table's
data values. The vectors contained in the outer vector are
each a single row of values. In other words, to get to the cell
at row 1, column 5:

((Vector)getDataVector().elementAt(1)).elementAt(5);

**Returns:** the vector of vectors containing the tables data values
**See Also:** newDataAvailable(javax.swing.event.TableModelEvent)

,

newRowsAdded(javax.swing.event.TableModelEvent)

,

setDataVector(java.util.Vector<? extends java.util.Vector>, java.util.Vector<?>)

---

#### getDataVector

public

Vector

<

Vector

> getDataVector()

Returns the

Vector

of

Vectors

that contains the table's
data values. The vectors contained in the outer vector are
each a single row of values. In other words, to get to the cell
at row 1, column 5:

((Vector)getDataVector().elementAt(1)).elementAt(5);

((Vector)getDataVector().elementAt(1)).elementAt(5);

setDataVector

```java
public void setDataVector​(
Vector
<? extends
Vector
> dataVector,

Vector
<?> columnIdentifiers)
```

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.
Each row is represented in

dataVector

as a

Vector

of

Object

values.

columnIdentifiers

are the names of the new
columns. The first name in

columnIdentifiers

is
mapped to column 0 in

dataVector

. Each row in

dataVector

is adjusted to match the number of
columns in

columnIdentifiers

either by truncating the

Vector

if it is too long,
or adding

null

values if it is too short.

Note that passing in a

null

value for

dataVector

results in unspecified behavior,
an possibly an exception.

**Parameters:** dataVector

- the new data vector
**Parameters:** columnIdentifiers

- the names of the columns
**See Also:** getDataVector()

---

#### setDataVector

public void setDataVector​(

Vector

<? extends

Vector

> dataVector,

Vector

<?> columnIdentifiers)

Replaces the current

dataVector

instance variable
with the new

Vector

of rows,

dataVector

.
Each row is represented in

dataVector

as a

Vector

of

Object

values.

columnIdentifiers

are the names of the new
columns. The first name in

columnIdentifiers

is
mapped to column 0 in

dataVector

. Each row in

dataVector

is adjusted to match the number of
columns in

columnIdentifiers

either by truncating the

Vector

if it is too long,
or adding

null

values if it is too short.

Note that passing in a

null

value for

dataVector

results in unspecified behavior,
an possibly an exception.

Note that passing in a

null

value for

dataVector

results in unspecified behavior,
an possibly an exception.

setDataVector

```java
public void setDataVector​(
Object
[][] dataVector,

Object
[] columnIdentifiers)
```

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.
The first index in the

Object[][]

array is the row index and the second is the column index.

columnIdentifiers

are the names of the new columns.

**Parameters:** dataVector

- the new data vector
**Parameters:** columnIdentifiers

- the names of the columns
**See Also:** setDataVector(Vector, Vector)

---

#### setDataVector

public void setDataVector​(

Object

[][] dataVector,

Object

[] columnIdentifiers)

Replaces the value in the

dataVector

instance
variable with the values in the array

dataVector

.
The first index in the

Object[][]

array is the row index and the second is the column index.

columnIdentifiers

are the names of the new columns.

newDataAvailable

```java
public void newDataAvailable​(
TableModelEvent
event)
```

Equivalent to

fireTableChanged

.

**Parameters:** event

- the change event

---

#### newDataAvailable

public void newDataAvailable​(

TableModelEvent

event)

Equivalent to

fireTableChanged

.

newRowsAdded

```java
public void newRowsAdded​(
TableModelEvent
e)
```

Ensures that the new rows have the correct number of columns.
This is accomplished by using the

setSize

method in

Vector

which truncates vectors
which are too long, and appends

null

s if they
are too short.
This method also sends out a

tableChanged

notification message to all the listeners.

**Parameters:** e

- this

TableModelEvent

describes
where the rows were added.
If

null

it assumes
all the rows were newly added
**See Also:** getDataVector()

---

#### newRowsAdded

public void newRowsAdded​(

TableModelEvent

e)

Ensures that the new rows have the correct number of columns.
This is accomplished by using the

setSize

method in

Vector

which truncates vectors
which are too long, and appends

null

s if they
are too short.
This method also sends out a

tableChanged

notification message to all the listeners.

rowsRemoved

```java
public void rowsRemoved​(
TableModelEvent
event)
```

Equivalent to

fireTableChanged

.

**Parameters:** event

- the change event

---

#### rowsRemoved

public void rowsRemoved​(

TableModelEvent

event)

Equivalent to

fireTableChanged

.

setNumRows

```java
public void setNumRows​(int rowCount)
```

Obsolete as of Java 2 platform v1.3. Please use

setRowCount

instead.

**Parameters:** rowCount

- the new number of rows

---

#### setNumRows

public void setNumRows​(int rowCount)

Obsolete as of Java 2 platform v1.3. Please use

setRowCount

instead.

setRowCount

```java
public void setRowCount​(int rowCount)
```

Sets the number of rows in the model. If the new size is greater
than the current size, new rows are added to the end of the model
If the new size is less than the current size, all
rows at index

rowCount

and greater are discarded.

**Parameters:** rowCount

- number of rows in the model
**Since:** 1.3
**See Also:** setColumnCount(int)

---

#### setRowCount

public void setRowCount​(int rowCount)

Sets the number of rows in the model. If the new size is greater
than the current size, new rows are added to the end of the model
If the new size is less than the current size, all
rows at index

rowCount

and greater are discarded.

addRow

```java
public void addRow​(
Vector
<?> rowData)
```

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:** rowData

- optional data of the row being added

---

#### addRow

public void addRow​(

Vector

<?> rowData)

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

addRow

```java
public void addRow​(
Object
[] rowData)
```

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

**Parameters:** rowData

- optional data of the row being added

---

#### addRow

public void addRow​(

Object

[] rowData)

Adds a row to the end of the model. The new row will contain

null

values unless

rowData

is specified.
Notification of the row being added will be generated.

insertRow

```java
public void insertRow​(int row,

Vector
<?> rowData)
```

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:** row

- the row index of the row to be inserted
**Parameters:** rowData

- optional data of the row being added
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

---

#### insertRow

public void insertRow​(int row,

Vector

<?> rowData)

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

insertRow

```java
public void insertRow​(int row,

Object
[] rowData)
```

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

**Parameters:** row

- the row index of the row to be inserted
**Parameters:** rowData

- optional data of the row being added
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

---

#### insertRow

public void insertRow​(int row,

Object

[] rowData)

Inserts a row at

row

in the model. The new row
will contain

null

values unless

rowData

is specified. Notification of the row being added will be generated.

moveRow

```java
public void moveRow​(int start,
int end,
int to)
```

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.
After the move, the row that was at index

start

will be at index

to

.
This method will send a

tableChanged

notification
message to all the listeners.

```java
Examples of moves:

1. moveRow(1,3,5);
a|B|C|D|e|f|g|h|i|j|k - before
a|e|f|g|h|B|C|D|i|j|k - after

2. moveRow(6,7,1);
a|b|c|d|e|f|G|H|i|j|k - before
a|G|H|b|c|d|e|f|i|j|k - after
```

**Parameters:** start

- the starting row index to be moved
**Parameters:** end

- the ending row index to be moved
**Parameters:** to

- the destination of the rows to be moved
**Throws:** ArrayIndexOutOfBoundsException

- if any of the elements
would be moved out of the table's range

---

#### moveRow

public void moveRow​(int start,
int end,
int to)

Moves one or more rows from the inclusive range

start

to

end

to the

to

position in the model.
After the move, the row that was at index

start

will be at index

to

.
This method will send a

tableChanged

notification
message to all the listeners.

```java
Examples of moves:

1. moveRow(1,3,5);
a|B|C|D|e|f|g|h|i|j|k - before
a|e|f|g|h|B|C|D|i|j|k - after

2. moveRow(6,7,1);
a|b|c|d|e|f|G|H|i|j|k - before
a|G|H|b|c|d|e|f|i|j|k - after
```

Examples of moves:

1. moveRow(1,3,5);
a|B|C|D|e|f|g|h|i|j|k - before
a|e|f|g|h|B|C|D|i|j|k - after

2. moveRow(6,7,1);
a|b|c|d|e|f|G|H|i|j|k - before
a|G|H|b|c|d|e|f|i|j|k - after

removeRow

```java
public void removeRow​(int row)
```

Removes the row at

row

from the model. Notification
of the row being removed will be sent to all the listeners.

**Parameters:** row

- the row index of the row to be removed
**Throws:** ArrayIndexOutOfBoundsException

- if the row was invalid

---

#### removeRow

public void removeRow​(int row)

Removes the row at

row

from the model. Notification
of the row being removed will be sent to all the listeners.

setColumnIdentifiers

```java
public void setColumnIdentifiers​(
Vector
<?> columnIdentifiers)
```

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:** columnIdentifiers

- vector of column identifiers. If

null

, set the model
to zero columns
**See Also:** setNumRows(int)

---

#### setColumnIdentifiers

public void setColumnIdentifiers​(

Vector

<?> columnIdentifiers)

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

setColumnIdentifiers

```java
public void setColumnIdentifiers​(
Object
[] newIdentifiers)
```

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

**Parameters:** newIdentifiers

- array of column identifiers.
If

null

, set
the model to zero columns
**See Also:** setNumRows(int)

---

#### setColumnIdentifiers

public void setColumnIdentifiers​(

Object

[] newIdentifiers)

Replaces the column identifiers in the model. If the number of

newIdentifier

s is greater than the current number
of columns, new columns are added to the end of each row in the model.
If the number of

newIdentifier

s is less than the current
number of columns, all the extra columns at the end of a row are
discarded.

setColumnCount

```java
public void setColumnCount​(int columnCount)
```

Sets the number of columns in the model. If the new size is greater
than the current size, new columns are added to the end of the model
with

null

cell values.
If the new size is less than the current size, all columns at index

columnCount

and greater are discarded.

**Parameters:** columnCount

- the new number of columns in the model
**Since:** 1.3
**See Also:** setColumnCount(int)

---

#### setColumnCount

public void setColumnCount​(int columnCount)

Sets the number of columns in the model. If the new size is greater
than the current size, new columns are added to the end of the model
with

null

cell values.
If the new size is less than the current size, all columns at index

columnCount

and greater are discarded.

addColumn

```java
public void addColumn​(
Object
columnName)
```

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null. This method
will send a

tableChanged

notification message to all the listeners.
This method is a cover for

addColumn(Object, Vector)

which
uses

null

as the data vector.

**Parameters:** columnName

- the identifier of the column being added

---

#### addColumn

public void addColumn​(

Object

columnName)

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null. This method
will send a

tableChanged

notification message to all the listeners.
This method is a cover for

addColumn(Object, Vector)

which
uses

null

as the data vector.

addColumn

```java
public void addColumn​(
Object
columnName,

Vector
<?> columnData)
```

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null.

columnData

is the
optional vector of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:** columnName

- the identifier of the column being added
**Parameters:** columnData

- optional data of the column being added

---

#### addColumn

public void addColumn​(

Object

columnName,

Vector

<?> columnData)

Adds a column to the model. The new column will have the
identifier

columnName

, which may be null.

columnData

is the
optional vector of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

addColumn

```java
public void addColumn​(
Object
columnName,

Object
[] columnData)
```

Adds a column to the model. The new column will have the
identifier

columnName

.

columnData

is the
optional array of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

**Parameters:** columnName

- identifier of the newly created column
**Parameters:** columnData

- new data to be added to the column
**See Also:** addColumn(Object, Vector)

---

#### addColumn

public void addColumn​(

Object

columnName,

Object

[] columnData)

Adds a column to the model. The new column will have the
identifier

columnName

.

columnData

is the
optional array of data for the column. If it is

null

the column is filled with

null

values. Otherwise,
the new data will be added to model starting with the first
element going to row 0, etc. This method will send a

tableChanged

notification message to all the listeners.

getRowCount

```java
public int getRowCount()
```

Returns the number of rows in this data table.

**Specified by:** getRowCount

in interface

TableModel
**Returns:** the number of rows in the model
**See Also:** TableModel.getColumnCount()

---

#### getRowCount

public int getRowCount()

Returns the number of rows in this data table.

getColumnCount

```java
public int getColumnCount()
```

Returns the number of columns in this data table.

**Specified by:** getColumnCount

in interface

TableModel
**Returns:** the number of columns in the model
**See Also:** TableModel.getRowCount()

---

#### getColumnCount

public int getColumnCount()

Returns the number of columns in this data table.

getColumnName

```java
public
String
getColumnName​(int column)
```

Returns the column name.

**Specified by:** getColumnName

in interface

TableModel
**Overrides:** getColumnName

in class

AbstractTableModel
**Parameters:** column

- the column being queried
**Returns:** a name for this column using the string value of the
appropriate member in

columnIdentifiers

.
If

columnIdentifiers

does not have an entry
for this index, returns the default
name provided by the superclass.

---

#### getColumnName

public

String

getColumnName​(int column)

Returns the column name.

isCellEditable

```java
public boolean isCellEditable​(int row,
int column)
```

Returns true regardless of parameter values.

**Specified by:** isCellEditable

in interface

TableModel
**Overrides:** isCellEditable

in class

AbstractTableModel
**Parameters:** row

- the row whose value is to be queried
**Parameters:** column

- the column whose value is to be queried
**Returns:** true
**See Also:** setValueAt(java.lang.Object, int, int)

---

#### isCellEditable

public boolean isCellEditable​(int row,
int column)

Returns true regardless of parameter values.

getValueAt

```java
public
Object
getValueAt​(int row,
int column)
```

Returns an attribute value for the cell at

row

and

column

.

**Specified by:** getValueAt

in interface

TableModel
**Parameters:** row

- the row whose value is to be queried
**Parameters:** column

- the column whose value is to be queried
**Returns:** the value Object at the specified cell
**Throws:** ArrayIndexOutOfBoundsException

- if an invalid row or
column was given

---

#### getValueAt

public

Object

getValueAt​(int row,
int column)

Returns an attribute value for the cell at

row

and

column

.

setValueAt

```java
public void setValueAt​(
Object
aValue,
int row,
int column)
```

Sets the object value for the cell at

column

and

row

.

aValue

is the new value. This method
will generate a

tableChanged

notification.

**Specified by:** setValueAt

in interface

TableModel
**Overrides:** setValueAt

in class

AbstractTableModel
**Parameters:** aValue

- the new value; this can be null
**Parameters:** row

- the row whose value is to be changed
**Parameters:** column

- the column whose value is to be changed
**Throws:** ArrayIndexOutOfBoundsException

- if an invalid row or
column was given
**See Also:** TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

---

#### setValueAt

public void setValueAt​(

Object

aValue,
int row,
int column)

Sets the object value for the cell at

column

and

row

.

aValue

is the new value. This method
will generate a

tableChanged

notification.

convertToVector

```java
protected static
Vector
<
Object
> convertToVector​(
Object
[] anArray)
```

Returns a vector that contains the same objects as the array.

**Parameters:** anArray

- the array to be converted
**Returns:** the new vector; if

anArray

is

null

,
returns

null

---

#### convertToVector

protected static

Vector

<

Object

> convertToVector​(

Object

[] anArray)

Returns a vector that contains the same objects as the array.

convertToVector

```java
protected static
Vector
<
Vector
<
Object
>> convertToVector​(
Object
[][] anArray)
```

Returns a vector of vectors that contains the same objects as the array.

**Parameters:** anArray

- the double array to be converted
**Returns:** the new vector of vectors; if

anArray

is

null

, returns

null

---

#### convertToVector

protected static

Vector

<

Vector

<

Object

>> convertToVector​(

Object

[][] anArray)

Returns a vector of vectors that contains the same objects as the array.

---

