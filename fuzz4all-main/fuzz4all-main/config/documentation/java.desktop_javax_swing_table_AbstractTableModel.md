# Class AbstractTableModel

**Source:** `java.desktop\javax\swing\table\AbstractTableModel.html`

### Class Description

```java
public abstract class
AbstractTableModel

extends
Object

implements
TableModel
,
Serializable
```

This abstract class provides default implementations for most of
the methods in the

TableModel

interface. It takes care of
the management of listeners and provides some conveniences for generating

TableModelEvents

and dispatching them to the listeners.
To create a concrete

TableModel

as a subclass of

AbstractTableModel

you need only provide implementations
for the following three methods:

```java
public int getRowCount();
public int getColumnCount();
public Object getValueAt(int row, int column);
```

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
EventListenerList
listenerList

List of listeners

---

### Constructor Details

#### public AbstractTableModel()

*No description found.*

---

### Method Details

#### public
String
getColumnName​(int column)

Returns a default name for the column using spreadsheet conventions:
A, B, C, ... Z, AA, AB, etc. If

column

cannot be found,
returns an empty string.

**Specified by:**
- getColumnName

in interface

TableModel

**Parameters:**
- column

- the column being queried

**Returns:**
- a string containing the default name of

column

---

#### public int findColumn​(
String
columnName)

Returns a column given its name.
Implementation is naive so this should be overridden if
this method is to be called often. This method is not
in the

TableModel

interface and is not used by the

JTable

.

**Parameters:**
- columnName

- string containing name of column to be located

**Returns:**
- the column with

columnName

, or -1 if not found

---

#### public
Class
<?> getColumnClass​(int columnIndex)

Returns

Object.class

regardless of

columnIndex

.

**Specified by:**
- getColumnClass

in interface

TableModel

**Parameters:**
- columnIndex

- the column being queried

**Returns:**
- the Object.class

---

#### public boolean isCellEditable​(int rowIndex,
int columnIndex)

Returns false. This is the default implementation for all cells.

**Specified by:**
- isCellEditable

in interface

TableModel

**Parameters:**
- rowIndex

- the row being queried
- columnIndex

- the column being queried

**Returns:**
- false

**See Also:**
- TableModel.setValueAt(java.lang.Object, int, int)

---

#### public void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

**Specified by:**
- setValueAt

in interface

TableModel

**Parameters:**
- aValue

- value to assign to cell
- rowIndex

- row of cell
- columnIndex

- column of cell

**See Also:**
- TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

---

#### public void addTableModelListener​(
TableModelListener
l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:**
- addTableModelListener

in interface

TableModel

**Parameters:**
- l

- the TableModelListener

---

#### public void removeTableModelListener​(
TableModelListener
l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:**
- removeTableModelListener

in interface

TableModel

**Parameters:**
- l

- the TableModelListener

---

#### public
TableModelListener
[] getTableModelListeners()

Returns an array of all the table model listeners
registered on this model.

**Returns:**
- all of this model's

TableModelListener

s
or an empty
array if no table model listeners are currently registered

**See Also:**
- addTableModelListener(javax.swing.event.TableModelListener)

,

removeTableModelListener(javax.swing.event.TableModelListener)

**Since:**
- 1.4

---

#### public void fireTableDataChanged()

Notifies all listeners that all cell values in the table's
rows may have changed. The number of rows may also have changed
and the

JTable

should redraw the
table from scratch. The structure of the table (as in the order of the
columns) is assumed to be the same.

**See Also:**
- TableModelEvent

,

EventListenerList

,

JTable.tableChanged(TableModelEvent)

---

#### public void fireTableStructureChanged()

Notifies all listeners that the table's structure has changed.
The number of columns in the table, and the names and types of
the new columns may be different from the previous state.
If the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any table columns that it had and reallocates
default columns in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**See Also:**
- TableModelEvent

,

EventListenerList

---

#### public void fireTableRowsInserted​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

**Parameters:**
- firstRow

- the first row
- lastRow

- the last row

**See Also:**
- TableModelEvent

,

EventListenerList

---

#### public void fireTableRowsUpdated​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

**Parameters:**
- firstRow

- the first row
- lastRow

- the last row

**See Also:**
- TableModelEvent

,

EventListenerList

---

#### public void fireTableRowsDeleted​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

**Parameters:**
- firstRow

- the first row
- lastRow

- the last row

**See Also:**
- TableModelEvent

,

EventListenerList

---

#### public void fireTableCellUpdated​(int row,
int column)

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

**Parameters:**
- row

- row of cell which has been updated
- column

- column of cell which has been updated

**See Also:**
- TableModelEvent

,

EventListenerList

---

#### public void fireTableChanged​(
TableModelEvent
e)

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

**Parameters:**
- e

- the event to be forwarded

**See Also:**
- addTableModelListener(javax.swing.event.TableModelListener)

,

TableModelEvent

,

EventListenerList

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a
model

m

for its table model listeners with the following code:

```java
TableModelListener[] tmls = (TableModelListener[])(m.getListeners(TableModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- getTableModelListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the listener type

---

### Additional Sections

#### Class AbstractTableModel

java.lang.Object

- javax.swing.table.AbstractTableModel

javax.swing.table.AbstractTableModel

**All Implemented Interfaces:** Serializable

,

TableModel

**Direct Known Subclasses:** DefaultTableModel

```java
public abstract class
AbstractTableModel

extends
Object

implements
TableModel
,
Serializable
```

This abstract class provides default implementations for most of
the methods in the

TableModel

interface. It takes care of
the management of listeners and provides some conveniences for generating

TableModelEvents

and dispatching them to the listeners.
To create a concrete

TableModel

as a subclass of

AbstractTableModel

you need only provide implementations
for the following three methods:

```java
public int getRowCount();
public int getColumnCount();
public Object getValueAt(int row, int column);
```

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

**See Also:** Serialized Form

public abstract class

AbstractTableModel

extends

Object

implements

TableModel

,

Serializable

This abstract class provides default implementations for most of
the methods in the

TableModel

interface. It takes care of
the management of listeners and provides some conveniences for generating

TableModelEvents

and dispatching them to the listeners.
To create a concrete

TableModel

as a subclass of

AbstractTableModel

you need only provide implementations
for the following three methods:

```java
public int getRowCount();
public int getColumnCount();
public Object getValueAt(int row, int column);
```

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

public int getRowCount();
public int getColumnCount();
public Object getValueAt(int row, int column);

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

EventListenerList

listenerList

List of listeners

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractTableModel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addTableModelListener

​(

TableModelListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

int

findColumn

​(

String

columnName)

Returns a column given its name.

void

fireTableCellUpdated

​(int row,
int column)

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

void

fireTableChanged

​(

TableModelEvent

e)

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

void

fireTableDataChanged

()

Notifies all listeners that all cell values in the table's
rows may have changed.

void

fireTableRowsDeleted

​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

void

fireTableRowsInserted

​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

void

fireTableRowsUpdated

​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

void

fireTableStructureChanged

()

Notifies all listeners that the table's structure has changed.

Class

<?>

getColumnClass

​(int columnIndex)

Returns

Object.class

regardless of

columnIndex

.

String

getColumnName

​(int column)

Returns a default name for the column using spreadsheet conventions:
A, B, C, ...

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

TableModelListener

[]

getTableModelListeners

()

Returns an array of all the table model listeners
registered on this model.

boolean

isCellEditable

​(int rowIndex,
int columnIndex)

Returns false.

void

removeTableModelListener

​(

TableModelListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

void

setValueAt

​(

Object

aValue,
int rowIndex,
int columnIndex)

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

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

- Methods declared in interface javax.swing.table.

TableModel

getColumnCount

,

getRowCount

,

getValueAt

Field Summary

Fields

Modifier and Type

Field

Description

protected

EventListenerList

listenerList

List of listeners

---

#### Field Summary

List of listeners

Constructor Summary

Constructors

Constructor

Description

AbstractTableModel

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addTableModelListener

​(

TableModelListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

int

findColumn

​(

String

columnName)

Returns a column given its name.

void

fireTableCellUpdated

​(int row,
int column)

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

void

fireTableChanged

​(

TableModelEvent

e)

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

void

fireTableDataChanged

()

Notifies all listeners that all cell values in the table's
rows may have changed.

void

fireTableRowsDeleted

​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

void

fireTableRowsInserted

​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

void

fireTableRowsUpdated

​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

void

fireTableStructureChanged

()

Notifies all listeners that the table's structure has changed.

Class

<?>

getColumnClass

​(int columnIndex)

Returns

Object.class

regardless of

columnIndex

.

String

getColumnName

​(int column)

Returns a default name for the column using spreadsheet conventions:
A, B, C, ...

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

TableModelListener

[]

getTableModelListeners

()

Returns an array of all the table model listeners
registered on this model.

boolean

isCellEditable

​(int rowIndex,
int columnIndex)

Returns false.

void

removeTableModelListener

​(

TableModelListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

void

setValueAt

​(

Object

aValue,
int rowIndex,
int columnIndex)

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

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

- Methods declared in interface javax.swing.table.

TableModel

getColumnCount

,

getRowCount

,

getValueAt

---

#### Method Summary

Adds a listener to the list that's notified each time a change
to the data model occurs.

Returns a column given its name.

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

Notifies all listeners that all cell values in the table's
rows may have changed.

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

Notifies all listeners that the table's structure has changed.

Returns

Object.class

regardless of

columnIndex

.

Returns a default name for the column using spreadsheet conventions:
A, B, C, ...

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

Returns an array of all the table model listeners
registered on this model.

Returns false.

Removes a listener from the list that's notified each time a
change to the data model occurs.

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

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

Methods declared in interface javax.swing.table.

TableModel

getColumnCount

,

getRowCount

,

getValueAt

---

#### Methods declared in interface javax.swing.table. TableModel

============ FIELD DETAIL ===========

- Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

List of listeners

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractTableModel

```java
public AbstractTableModel()
```

============ METHOD DETAIL ==========

- Method Detail

- getColumnName

```java
public
String
getColumnName​(int column)
```

Returns a default name for the column using spreadsheet conventions:
A, B, C, ... Z, AA, AB, etc. If

column

cannot be found,
returns an empty string.

**Specified by:** getColumnName

in interface

TableModel
**Parameters:** column

- the column being queried
**Returns:** a string containing the default name of

column

- findColumn

```java
public int findColumn​(
String
columnName)
```

Returns a column given its name.
Implementation is naive so this should be overridden if
this method is to be called often. This method is not
in the

TableModel

interface and is not used by the

JTable

.

**Parameters:** columnName

- string containing name of column to be located
**Returns:** the column with

columnName

, or -1 if not found

- getColumnClass

```java
public
Class
<?> getColumnClass​(int columnIndex)
```

Returns

Object.class

regardless of

columnIndex

.

**Specified by:** getColumnClass

in interface

TableModel
**Parameters:** columnIndex

- the column being queried
**Returns:** the Object.class

- isCellEditable

```java
public boolean isCellEditable​(int rowIndex,
int columnIndex)
```

Returns false. This is the default implementation for all cells.

**Specified by:** isCellEditable

in interface

TableModel
**Parameters:** rowIndex

- the row being queried
**Parameters:** columnIndex

- the column being queried
**Returns:** false
**See Also:** TableModel.setValueAt(java.lang.Object, int, int)

- setValueAt

```java
public void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)
```

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

**Specified by:** setValueAt

in interface

TableModel
**Parameters:** aValue

- value to assign to cell
**Parameters:** rowIndex

- row of cell
**Parameters:** columnIndex

- column of cell
**See Also:** TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

- addTableModelListener

```java
public void addTableModelListener​(
TableModelListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:** addTableModelListener

in interface

TableModel
**Parameters:** l

- the TableModelListener

- removeTableModelListener

```java
public void removeTableModelListener​(
TableModelListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:** removeTableModelListener

in interface

TableModel
**Parameters:** l

- the TableModelListener

- getTableModelListeners

```java
public
TableModelListener
[] getTableModelListeners()
```

Returns an array of all the table model listeners
registered on this model.

**Returns:** all of this model's

TableModelListener

s
or an empty
array if no table model listeners are currently registered
**Since:** 1.4
**See Also:** addTableModelListener(javax.swing.event.TableModelListener)

,

removeTableModelListener(javax.swing.event.TableModelListener)

- fireTableDataChanged

```java
public void fireTableDataChanged()
```

Notifies all listeners that all cell values in the table's
rows may have changed. The number of rows may also have changed
and the

JTable

should redraw the
table from scratch. The structure of the table (as in the order of the
columns) is assumed to be the same.

**See Also:** TableModelEvent

,

EventListenerList

,

JTable.tableChanged(TableModelEvent)

- fireTableStructureChanged

```java
public void fireTableStructureChanged()
```

Notifies all listeners that the table's structure has changed.
The number of columns in the table, and the names and types of
the new columns may be different from the previous state.
If the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any table columns that it had and reallocates
default columns in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**See Also:** TableModelEvent

,

EventListenerList

- fireTableRowsInserted

```java
public void fireTableRowsInserted​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

- fireTableRowsUpdated

```java
public void fireTableRowsUpdated​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

- fireTableRowsDeleted

```java
public void fireTableRowsDeleted​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

- fireTableCellUpdated

```java
public void fireTableCellUpdated​(int row,
int column)
```

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

**Parameters:** row

- row of cell which has been updated
**Parameters:** column

- column of cell which has been updated
**See Also:** TableModelEvent

,

EventListenerList

- fireTableChanged

```java
public void fireTableChanged​(
TableModelEvent
e)
```

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

**Parameters:** e

- the event to be forwarded
**See Also:** addTableModelListener(javax.swing.event.TableModelListener)

,

TableModelEvent

,

EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a
model

m

for its table model listeners with the following code:

```java
TableModelListener[] tmls = (TableModelListener[])(m.getListeners(TableModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getTableModelListeners()

Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

List of listeners

---

#### Field Detail

listenerList

```java
protected
EventListenerList
listenerList
```

List of listeners

---

#### listenerList

protected

EventListenerList

listenerList

List of listeners

Constructor Detail

- AbstractTableModel

```java
public AbstractTableModel()
```

---

#### Constructor Detail

AbstractTableModel

```java
public AbstractTableModel()
```

---

#### AbstractTableModel

public AbstractTableModel()

Method Detail

- getColumnName

```java
public
String
getColumnName​(int column)
```

Returns a default name for the column using spreadsheet conventions:
A, B, C, ... Z, AA, AB, etc. If

column

cannot be found,
returns an empty string.

**Specified by:** getColumnName

in interface

TableModel
**Parameters:** column

- the column being queried
**Returns:** a string containing the default name of

column

- findColumn

```java
public int findColumn​(
String
columnName)
```

Returns a column given its name.
Implementation is naive so this should be overridden if
this method is to be called often. This method is not
in the

TableModel

interface and is not used by the

JTable

.

**Parameters:** columnName

- string containing name of column to be located
**Returns:** the column with

columnName

, or -1 if not found

- getColumnClass

```java
public
Class
<?> getColumnClass​(int columnIndex)
```

Returns

Object.class

regardless of

columnIndex

.

**Specified by:** getColumnClass

in interface

TableModel
**Parameters:** columnIndex

- the column being queried
**Returns:** the Object.class

- isCellEditable

```java
public boolean isCellEditable​(int rowIndex,
int columnIndex)
```

Returns false. This is the default implementation for all cells.

**Specified by:** isCellEditable

in interface

TableModel
**Parameters:** rowIndex

- the row being queried
**Parameters:** columnIndex

- the column being queried
**Returns:** false
**See Also:** TableModel.setValueAt(java.lang.Object, int, int)

- setValueAt

```java
public void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)
```

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

**Specified by:** setValueAt

in interface

TableModel
**Parameters:** aValue

- value to assign to cell
**Parameters:** rowIndex

- row of cell
**Parameters:** columnIndex

- column of cell
**See Also:** TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

- addTableModelListener

```java
public void addTableModelListener​(
TableModelListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:** addTableModelListener

in interface

TableModel
**Parameters:** l

- the TableModelListener

- removeTableModelListener

```java
public void removeTableModelListener​(
TableModelListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:** removeTableModelListener

in interface

TableModel
**Parameters:** l

- the TableModelListener

- getTableModelListeners

```java
public
TableModelListener
[] getTableModelListeners()
```

Returns an array of all the table model listeners
registered on this model.

**Returns:** all of this model's

TableModelListener

s
or an empty
array if no table model listeners are currently registered
**Since:** 1.4
**See Also:** addTableModelListener(javax.swing.event.TableModelListener)

,

removeTableModelListener(javax.swing.event.TableModelListener)

- fireTableDataChanged

```java
public void fireTableDataChanged()
```

Notifies all listeners that all cell values in the table's
rows may have changed. The number of rows may also have changed
and the

JTable

should redraw the
table from scratch. The structure of the table (as in the order of the
columns) is assumed to be the same.

**See Also:** TableModelEvent

,

EventListenerList

,

JTable.tableChanged(TableModelEvent)

- fireTableStructureChanged

```java
public void fireTableStructureChanged()
```

Notifies all listeners that the table's structure has changed.
The number of columns in the table, and the names and types of
the new columns may be different from the previous state.
If the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any table columns that it had and reallocates
default columns in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**See Also:** TableModelEvent

,

EventListenerList

- fireTableRowsInserted

```java
public void fireTableRowsInserted​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

- fireTableRowsUpdated

```java
public void fireTableRowsUpdated​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

- fireTableRowsDeleted

```java
public void fireTableRowsDeleted​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

- fireTableCellUpdated

```java
public void fireTableCellUpdated​(int row,
int column)
```

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

**Parameters:** row

- row of cell which has been updated
**Parameters:** column

- column of cell which has been updated
**See Also:** TableModelEvent

,

EventListenerList

- fireTableChanged

```java
public void fireTableChanged​(
TableModelEvent
e)
```

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

**Parameters:** e

- the event to be forwarded
**See Also:** addTableModelListener(javax.swing.event.TableModelListener)

,

TableModelEvent

,

EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a
model

m

for its table model listeners with the following code:

```java
TableModelListener[] tmls = (TableModelListener[])(m.getListeners(TableModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getTableModelListeners()

---

#### Method Detail

getColumnName

```java
public
String
getColumnName​(int column)
```

Returns a default name for the column using spreadsheet conventions:
A, B, C, ... Z, AA, AB, etc. If

column

cannot be found,
returns an empty string.

**Specified by:** getColumnName

in interface

TableModel
**Parameters:** column

- the column being queried
**Returns:** a string containing the default name of

column

---

#### getColumnName

public

String

getColumnName​(int column)

Returns a default name for the column using spreadsheet conventions:
A, B, C, ... Z, AA, AB, etc. If

column

cannot be found,
returns an empty string.

findColumn

```java
public int findColumn​(
String
columnName)
```

Returns a column given its name.
Implementation is naive so this should be overridden if
this method is to be called often. This method is not
in the

TableModel

interface and is not used by the

JTable

.

**Parameters:** columnName

- string containing name of column to be located
**Returns:** the column with

columnName

, or -1 if not found

---

#### findColumn

public int findColumn​(

String

columnName)

Returns a column given its name.
Implementation is naive so this should be overridden if
this method is to be called often. This method is not
in the

TableModel

interface and is not used by the

JTable

.

getColumnClass

```java
public
Class
<?> getColumnClass​(int columnIndex)
```

Returns

Object.class

regardless of

columnIndex

.

**Specified by:** getColumnClass

in interface

TableModel
**Parameters:** columnIndex

- the column being queried
**Returns:** the Object.class

---

#### getColumnClass

public

Class

<?> getColumnClass​(int columnIndex)

Returns

Object.class

regardless of

columnIndex

.

isCellEditable

```java
public boolean isCellEditable​(int rowIndex,
int columnIndex)
```

Returns false. This is the default implementation for all cells.

**Specified by:** isCellEditable

in interface

TableModel
**Parameters:** rowIndex

- the row being queried
**Parameters:** columnIndex

- the column being queried
**Returns:** false
**See Also:** TableModel.setValueAt(java.lang.Object, int, int)

---

#### isCellEditable

public boolean isCellEditable​(int rowIndex,
int columnIndex)

Returns false. This is the default implementation for all cells.

setValueAt

```java
public void setValueAt​(
Object
aValue,
int rowIndex,
int columnIndex)
```

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

**Specified by:** setValueAt

in interface

TableModel
**Parameters:** aValue

- value to assign to cell
**Parameters:** rowIndex

- row of cell
**Parameters:** columnIndex

- column of cell
**See Also:** TableModel.getValueAt(int, int)

,

TableModel.isCellEditable(int, int)

---

#### setValueAt

public void setValueAt​(

Object

aValue,
int rowIndex,
int columnIndex)

This empty implementation is provided so users don't have to implement
this method if their data model is not editable.

addTableModelListener

```java
public void addTableModelListener​(
TableModelListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:** addTableModelListener

in interface

TableModel
**Parameters:** l

- the TableModelListener

---

#### addTableModelListener

public void addTableModelListener​(

TableModelListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

removeTableModelListener

```java
public void removeTableModelListener​(
TableModelListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:** removeTableModelListener

in interface

TableModel
**Parameters:** l

- the TableModelListener

---

#### removeTableModelListener

public void removeTableModelListener​(

TableModelListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

getTableModelListeners

```java
public
TableModelListener
[] getTableModelListeners()
```

Returns an array of all the table model listeners
registered on this model.

**Returns:** all of this model's

TableModelListener

s
or an empty
array if no table model listeners are currently registered
**Since:** 1.4
**See Also:** addTableModelListener(javax.swing.event.TableModelListener)

,

removeTableModelListener(javax.swing.event.TableModelListener)

---

#### getTableModelListeners

public

TableModelListener

[] getTableModelListeners()

Returns an array of all the table model listeners
registered on this model.

fireTableDataChanged

```java
public void fireTableDataChanged()
```

Notifies all listeners that all cell values in the table's
rows may have changed. The number of rows may also have changed
and the

JTable

should redraw the
table from scratch. The structure of the table (as in the order of the
columns) is assumed to be the same.

**See Also:** TableModelEvent

,

EventListenerList

,

JTable.tableChanged(TableModelEvent)

---

#### fireTableDataChanged

public void fireTableDataChanged()

Notifies all listeners that all cell values in the table's
rows may have changed. The number of rows may also have changed
and the

JTable

should redraw the
table from scratch. The structure of the table (as in the order of the
columns) is assumed to be the same.

fireTableStructureChanged

```java
public void fireTableStructureChanged()
```

Notifies all listeners that the table's structure has changed.
The number of columns in the table, and the names and types of
the new columns may be different from the previous state.
If the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any table columns that it had and reallocates
default columns in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

**See Also:** TableModelEvent

,

EventListenerList

---

#### fireTableStructureChanged

public void fireTableStructureChanged()

Notifies all listeners that the table's structure has changed.
The number of columns in the table, and the names and types of
the new columns may be different from the previous state.
If the

JTable

receives this event and its

autoCreateColumnsFromModel

flag is set it discards any table columns that it had and reallocates
default columns in the order they appear in the model. This is the
same as calling

setModel(TableModel)

on the

JTable

.

fireTableRowsInserted

```java
public void fireTableRowsInserted​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

---

#### fireTableRowsInserted

public void fireTableRowsInserted​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been inserted.

fireTableRowsUpdated

```java
public void fireTableRowsUpdated​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

---

#### fireTableRowsUpdated

public void fireTableRowsUpdated​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been updated.

fireTableRowsDeleted

```java
public void fireTableRowsDeleted​(int firstRow,
int lastRow)
```

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

**Parameters:** firstRow

- the first row
**Parameters:** lastRow

- the last row
**See Also:** TableModelEvent

,

EventListenerList

---

#### fireTableRowsDeleted

public void fireTableRowsDeleted​(int firstRow,
int lastRow)

Notifies all listeners that rows in the range

[firstRow, lastRow]

, inclusive, have been deleted.

fireTableCellUpdated

```java
public void fireTableCellUpdated​(int row,
int column)
```

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

**Parameters:** row

- row of cell which has been updated
**Parameters:** column

- column of cell which has been updated
**See Also:** TableModelEvent

,

EventListenerList

---

#### fireTableCellUpdated

public void fireTableCellUpdated​(int row,
int column)

Notifies all listeners that the value of the cell at

[row, column]

has been updated.

fireTableChanged

```java
public void fireTableChanged​(
TableModelEvent
e)
```

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

**Parameters:** e

- the event to be forwarded
**See Also:** addTableModelListener(javax.swing.event.TableModelListener)

,

TableModelEvent

,

EventListenerList

---

#### fireTableChanged

public void fireTableChanged​(

TableModelEvent

e)

Forwards the given notification event to all

TableModelListeners

that registered
themselves as listeners for this table model.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a
model

m

for its table model listeners with the following code:

```java
TableModelListener[] tmls = (TableModelListener[])(m.getListeners(TableModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getTableModelListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

AbstractTableModel

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a
model

m

for its table model listeners with the following code:

```java
TableModelListener[] tmls = (TableModelListener[])(m.getListeners(TableModelListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a
model

m

for its table model listeners with the following code:

```java
TableModelListener[] tmls = (TableModelListener[])(m.getListeners(TableModelListener.class));
```

If no such listeners exist, this method returns an empty array.

TableModelListener[] tmls = (TableModelListener[])(m.getListeners(TableModelListener.class));

---

