# Interface TableModel

**Source:** `java.desktop\javax\swing\table\TableModel.html`

### Class Description

```java
public interface
TableModel
```

The

TableModel

interface specifies the methods the

JTable

will use to interrogate a tabular data model.

The

JTable

can be set up to display any data
model which implements the

TableModel

interface with a couple of lines of code:

```java
TableModel myData = new MyTableModel();
JTable table = new JTable(myData);
```

For further documentation, see

Creating a Table Model

in

The Java Tutorial

.

**All Known Implementing Classes:** AbstractTableModel

,

DefaultTableModel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getRowCount()

Returns the number of rows in the model. A

JTable

uses this method to determine how many rows it
should display. This method should be quick, as it
is called frequently during rendering.

**Returns:**
- the number of rows in the model

**See Also:**
- getColumnCount()

---

#### int getColumnCount()

Returns the number of columns in the model. A

JTable

uses this method to determine how many columns it
should create and display by default.

**Returns:**
- the number of columns in the model

**See Also:**
- getRowCount()

---

#### String
getColumnName​(int columnIndex)

Returns the name of the column at

columnIndex

. This is used
to initialize the table's column header name. Note: this name does
not need to be unique; two columns in a table can have the same name.

**Parameters:**
- columnIndex

- the index of the column

**Returns:**
- the name of the column

---

#### Class
<?> getColumnClass​(int columnIndex)

Returns the most specific superclass for all the cell values
in the column. This is used by the

JTable

to set up a
default renderer and editor for the column.

**Parameters:**
- columnIndex

- the index of the column

**Returns:**
- the common ancestor class of the object values in the model.

---

#### boolean isCellEditable​(int rowIndex,
int columnIndex)

Returns true if the cell at

rowIndex

and

columnIndex

is editable. Otherwise,

setValueAt

on the cell will not
change the value of that cell.

**Parameters:**
- rowIndex

- the row whose value to be queried
- columnIndex

- the column whose value to be queried

**Returns:**
- true if the cell is editable

**See Also:**
- setValueAt(java.lang.Object, int, int)

---

#### Object
getValueAt​(int rowIndex,
int columnIndex)

Returns the value for the cell at

columnIndex

and

rowIndex

.

**Parameters:**
- rowIndex

- the row whose value is to be queried
- columnIndex

- the column whose value is to be queried

**Returns:**
- the value Object at the specified cell

---

#### void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

**Parameters:**
- aValue

- the new value
- rowIndex

- the row whose value is to be changed
- columnIndex

- the column whose value is to be changed

**See Also:**
- getValueAt(int, int)

,

isCellEditable(int, int)

---

#### void addTableModelListener​(
TableModelListener
l)

Adds a listener to the list that is notified each time a change
to the data model occurs.

**Parameters:**
- l

- the TableModelListener

---

#### void removeTableModelListener​(
TableModelListener
l)

Removes a listener from the list that is notified each time a
change to the data model occurs.

**Parameters:**
- l

- the TableModelListener

---

### Additional Sections

#### Interface TableModel

**All Known Implementing Classes:** AbstractTableModel

,

DefaultTableModel

```java
public interface
TableModel
```

The

TableModel

interface specifies the methods the

JTable

will use to interrogate a tabular data model.

The

JTable

can be set up to display any data
model which implements the

TableModel

interface with a couple of lines of code:

```java
TableModel myData = new MyTableModel();
JTable table = new JTable(myData);
```

For further documentation, see

Creating a Table Model

in

The Java Tutorial

.

**See Also:** JTable

public interface

TableModel

The

TableModel

interface specifies the methods the

JTable

will use to interrogate a tabular data model.

The

JTable

can be set up to display any data
model which implements the

TableModel

interface with a couple of lines of code:

```java
TableModel myData = new MyTableModel();
JTable table = new JTable(myData);
```

For further documentation, see

Creating a Table Model

in

The Java Tutorial

.

The

JTable

can be set up to display any data
model which implements the

TableModel

interface with a couple of lines of code:

```java
TableModel myData = new MyTableModel();
JTable table = new JTable(myData);
```

For further documentation, see

Creating a Table Model

in

The Java Tutorial

.

TableModel myData = new MyTableModel();
JTable table = new JTable(myData);

For further documentation, see

Creating a Table Model

in

The Java Tutorial

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

addTableModelListener

​(

TableModelListener

l)

Adds a listener to the list that is notified each time a change
to the data model occurs.

Class

<?>

getColumnClass

​(int columnIndex)

Returns the most specific superclass for all the cell values
in the column.

int

getColumnCount

()

Returns the number of columns in the model.

String

getColumnName

​(int columnIndex)

Returns the name of the column at

columnIndex

.

int

getRowCount

()

Returns the number of rows in the model.

Object

getValueAt

​(int rowIndex,
int columnIndex)

Returns the value for the cell at

columnIndex

and

rowIndex

.

boolean

isCellEditable

​(int rowIndex,
int columnIndex)

Returns true if the cell at

rowIndex

and

columnIndex

is editable.

void

removeTableModelListener

​(

TableModelListener

l)

Removes a listener from the list that is notified each time a
change to the data model occurs.

void

setValueAt

​(

Object

aValue,
int rowIndex,
int columnIndex)

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addTableModelListener

​(

TableModelListener

l)

Adds a listener to the list that is notified each time a change
to the data model occurs.

Class

<?>

getColumnClass

​(int columnIndex)

Returns the most specific superclass for all the cell values
in the column.

int

getColumnCount

()

Returns the number of columns in the model.

String

getColumnName

​(int columnIndex)

Returns the name of the column at

columnIndex

.

int

getRowCount

()

Returns the number of rows in the model.

Object

getValueAt

​(int rowIndex,
int columnIndex)

Returns the value for the cell at

columnIndex

and

rowIndex

.

boolean

isCellEditable

​(int rowIndex,
int columnIndex)

Returns true if the cell at

rowIndex

and

columnIndex

is editable.

void

removeTableModelListener

​(

TableModelListener

l)

Removes a listener from the list that is notified each time a
change to the data model occurs.

void

setValueAt

​(

Object

aValue,
int rowIndex,
int columnIndex)

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

---

#### Method Summary

Adds a listener to the list that is notified each time a change
to the data model occurs.

Returns the most specific superclass for all the cell values
in the column.

Returns the number of columns in the model.

Returns the name of the column at

columnIndex

.

Returns the number of rows in the model.

Returns the value for the cell at

columnIndex

and

rowIndex

.

Returns true if the cell at

rowIndex

and

columnIndex

is editable.

Removes a listener from the list that is notified each time a
change to the data model occurs.

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

============ METHOD DETAIL ==========

- Method Detail

- getRowCount

```java
int getRowCount()
```

Returns the number of rows in the model. A

JTable

uses this method to determine how many rows it
should display. This method should be quick, as it
is called frequently during rendering.

**Returns:** the number of rows in the model
**See Also:** getColumnCount()

- getColumnCount

```java
int getColumnCount()
```

Returns the number of columns in the model. A

JTable

uses this method to determine how many columns it
should create and display by default.

**Returns:** the number of columns in the model
**See Also:** getRowCount()

- getColumnName

```java
String
getColumnName​(int columnIndex)
```

Returns the name of the column at

columnIndex

. This is used
to initialize the table's column header name. Note: this name does
not need to be unique; two columns in a table can have the same name.

**Parameters:** columnIndex

- the index of the column
**Returns:** the name of the column

- getColumnClass

```java
Class
<?> getColumnClass​(int columnIndex)
```

Returns the most specific superclass for all the cell values
in the column. This is used by the

JTable

to set up a
default renderer and editor for the column.

**Parameters:** columnIndex

- the index of the column
**Returns:** the common ancestor class of the object values in the model.

- isCellEditable

```java
boolean isCellEditable​(int rowIndex,
int columnIndex)
```

Returns true if the cell at

rowIndex

and

columnIndex

is editable. Otherwise,

setValueAt

on the cell will not
change the value of that cell.

**Parameters:** rowIndex

- the row whose value to be queried
**Parameters:** columnIndex

- the column whose value to be queried
**Returns:** true if the cell is editable
**See Also:** setValueAt(java.lang.Object, int, int)

- getValueAt

```java
Object
getValueAt​(int rowIndex,
int columnIndex)
```

Returns the value for the cell at

columnIndex

and

rowIndex

.

**Parameters:** rowIndex

- the row whose value is to be queried
**Parameters:** columnIndex

- the column whose value is to be queried
**Returns:** the value Object at the specified cell

- setValueAt

```java
void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)
```

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

**Parameters:** aValue

- the new value
**Parameters:** rowIndex

- the row whose value is to be changed
**Parameters:** columnIndex

- the column whose value is to be changed
**See Also:** getValueAt(int, int)

,

isCellEditable(int, int)

- addTableModelListener

```java
void addTableModelListener​(
TableModelListener
l)
```

Adds a listener to the list that is notified each time a change
to the data model occurs.

**Parameters:** l

- the TableModelListener

- removeTableModelListener

```java
void removeTableModelListener​(
TableModelListener
l)
```

Removes a listener from the list that is notified each time a
change to the data model occurs.

**Parameters:** l

- the TableModelListener

Method Detail

- getRowCount

```java
int getRowCount()
```

Returns the number of rows in the model. A

JTable

uses this method to determine how many rows it
should display. This method should be quick, as it
is called frequently during rendering.

**Returns:** the number of rows in the model
**See Also:** getColumnCount()

- getColumnCount

```java
int getColumnCount()
```

Returns the number of columns in the model. A

JTable

uses this method to determine how many columns it
should create and display by default.

**Returns:** the number of columns in the model
**See Also:** getRowCount()

- getColumnName

```java
String
getColumnName​(int columnIndex)
```

Returns the name of the column at

columnIndex

. This is used
to initialize the table's column header name. Note: this name does
not need to be unique; two columns in a table can have the same name.

**Parameters:** columnIndex

- the index of the column
**Returns:** the name of the column

- getColumnClass

```java
Class
<?> getColumnClass​(int columnIndex)
```

Returns the most specific superclass for all the cell values
in the column. This is used by the

JTable

to set up a
default renderer and editor for the column.

**Parameters:** columnIndex

- the index of the column
**Returns:** the common ancestor class of the object values in the model.

- isCellEditable

```java
boolean isCellEditable​(int rowIndex,
int columnIndex)
```

Returns true if the cell at

rowIndex

and

columnIndex

is editable. Otherwise,

setValueAt

on the cell will not
change the value of that cell.

**Parameters:** rowIndex

- the row whose value to be queried
**Parameters:** columnIndex

- the column whose value to be queried
**Returns:** true if the cell is editable
**See Also:** setValueAt(java.lang.Object, int, int)

- getValueAt

```java
Object
getValueAt​(int rowIndex,
int columnIndex)
```

Returns the value for the cell at

columnIndex

and

rowIndex

.

**Parameters:** rowIndex

- the row whose value is to be queried
**Parameters:** columnIndex

- the column whose value is to be queried
**Returns:** the value Object at the specified cell

- setValueAt

```java
void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)
```

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

**Parameters:** aValue

- the new value
**Parameters:** rowIndex

- the row whose value is to be changed
**Parameters:** columnIndex

- the column whose value is to be changed
**See Also:** getValueAt(int, int)

,

isCellEditable(int, int)

- addTableModelListener

```java
void addTableModelListener​(
TableModelListener
l)
```

Adds a listener to the list that is notified each time a change
to the data model occurs.

**Parameters:** l

- the TableModelListener

- removeTableModelListener

```java
void removeTableModelListener​(
TableModelListener
l)
```

Removes a listener from the list that is notified each time a
change to the data model occurs.

**Parameters:** l

- the TableModelListener

---

#### Method Detail

getRowCount

```java
int getRowCount()
```

Returns the number of rows in the model. A

JTable

uses this method to determine how many rows it
should display. This method should be quick, as it
is called frequently during rendering.

**Returns:** the number of rows in the model
**See Also:** getColumnCount()

---

#### getRowCount

int getRowCount()

Returns the number of rows in the model. A

JTable

uses this method to determine how many rows it
should display. This method should be quick, as it
is called frequently during rendering.

getColumnCount

```java
int getColumnCount()
```

Returns the number of columns in the model. A

JTable

uses this method to determine how many columns it
should create and display by default.

**Returns:** the number of columns in the model
**See Also:** getRowCount()

---

#### getColumnCount

int getColumnCount()

Returns the number of columns in the model. A

JTable

uses this method to determine how many columns it
should create and display by default.

getColumnName

```java
String
getColumnName​(int columnIndex)
```

Returns the name of the column at

columnIndex

. This is used
to initialize the table's column header name. Note: this name does
not need to be unique; two columns in a table can have the same name.

**Parameters:** columnIndex

- the index of the column
**Returns:** the name of the column

---

#### getColumnName

String

getColumnName​(int columnIndex)

Returns the name of the column at

columnIndex

. This is used
to initialize the table's column header name. Note: this name does
not need to be unique; two columns in a table can have the same name.

getColumnClass

```java
Class
<?> getColumnClass​(int columnIndex)
```

Returns the most specific superclass for all the cell values
in the column. This is used by the

JTable

to set up a
default renderer and editor for the column.

**Parameters:** columnIndex

- the index of the column
**Returns:** the common ancestor class of the object values in the model.

---

#### getColumnClass

Class

<?> getColumnClass​(int columnIndex)

Returns the most specific superclass for all the cell values
in the column. This is used by the

JTable

to set up a
default renderer and editor for the column.

isCellEditable

```java
boolean isCellEditable​(int rowIndex,
int columnIndex)
```

Returns true if the cell at

rowIndex

and

columnIndex

is editable. Otherwise,

setValueAt

on the cell will not
change the value of that cell.

**Parameters:** rowIndex

- the row whose value to be queried
**Parameters:** columnIndex

- the column whose value to be queried
**Returns:** true if the cell is editable
**See Also:** setValueAt(java.lang.Object, int, int)

---

#### isCellEditable

boolean isCellEditable​(int rowIndex,
int columnIndex)

Returns true if the cell at

rowIndex

and

columnIndex

is editable. Otherwise,

setValueAt

on the cell will not
change the value of that cell.

getValueAt

```java
Object
getValueAt​(int rowIndex,
int columnIndex)
```

Returns the value for the cell at

columnIndex

and

rowIndex

.

**Parameters:** rowIndex

- the row whose value is to be queried
**Parameters:** columnIndex

- the column whose value is to be queried
**Returns:** the value Object at the specified cell

---

#### getValueAt

Object

getValueAt​(int rowIndex,
int columnIndex)

Returns the value for the cell at

columnIndex

and

rowIndex

.

setValueAt

```java
void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)
```

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

**Parameters:** aValue

- the new value
**Parameters:** rowIndex

- the row whose value is to be changed
**Parameters:** columnIndex

- the column whose value is to be changed
**See Also:** getValueAt(int, int)

,

isCellEditable(int, int)

---

#### setValueAt

void setValueAt​(

Object

aValue,
int rowIndex,
int columnIndex)

Sets the value in the cell at

columnIndex

and

rowIndex

to

aValue

.

addTableModelListener

```java
void addTableModelListener​(
TableModelListener
l)
```

Adds a listener to the list that is notified each time a change
to the data model occurs.

**Parameters:** l

- the TableModelListener

---

#### addTableModelListener

void addTableModelListener​(

TableModelListener

l)

Adds a listener to the list that is notified each time a change
to the data model occurs.

removeTableModelListener

```java
void removeTableModelListener​(
TableModelListener
l)
```

Removes a listener from the list that is notified each time a
change to the data model occurs.

**Parameters:** l

- the TableModelListener

---

#### removeTableModelListener

void removeTableModelListener​(

TableModelListener

l)

Removes a listener from the list that is notified each time a
change to the data model occurs.

---

