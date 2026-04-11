# Class DefaultTableColumnModel

**Source:** `java.desktop\javax\swing\table\DefaultTableColumnModel.html`

### Class Description

```java
public class
DefaultTableColumnModel

extends
Object

implements
TableColumnModel
,
PropertyChangeListener
,
ListSelectionListener
,
Serializable
```

The standard column-handler for a

JTable

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

**All Implemented Interfaces:** PropertyChangeListener

,

Serializable

,

EventListener

,

ListSelectionListener

,

TableColumnModel

---

### Field Details

#### protected
Vector
<
TableColumn
> tableColumns

Array of TableColumn objects in this model

---

#### protected
ListSelectionModel
selectionModel

Model for keeping track of column selections

---

#### protected int columnMargin

Width margin between each column

---

#### protected
EventListenerList
listenerList

List of TableColumnModelListener

---

#### protected transient
ChangeEvent
changeEvent

Change event (only one needed)

---

#### protected boolean columnSelectionAllowed

Column selection allowed in this column model

---

#### protected int totalColumnWidth

A local cache of the combined width of all columns

---

### Constructor Details

#### public DefaultTableColumnModel()

Creates a default table column model.

---

### Method Details

#### public void addColumn​(
TableColumn
aColumn)

Appends

aColumn

to the end of the

tableColumns

array.
This method also posts the

columnAdded

event to its listeners.

**Specified by:**
- addColumn

in interface

TableColumnModel

**Parameters:**
- aColumn

- the

TableColumn

to be added

**Throws:**
- IllegalArgumentException

- if

aColumn

is

null

**See Also:**
- removeColumn(javax.swing.table.TableColumn)

---

#### public void removeColumn​(
TableColumn
column)

Deletes the

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's columns list.

tile

is called
to resize both the header and table views.
This method also posts a

columnRemoved

event to its listeners.

**Specified by:**
- removeColumn

in interface

TableColumnModel

**Parameters:**
- column

- the

TableColumn

to be removed

**See Also:**
- addColumn(javax.swing.table.TableColumn)

---

#### public void moveColumn​(int columnIndex,
int newIndex)

Moves the column and heading at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column
that used to be at

newIndex

is shifted
left or right to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
also posts a

columnMoved

event to its listeners.

**Specified by:**
- moveColumn

in interface

TableColumnModel

**Parameters:**
- columnIndex

- the index of column to be moved
- newIndex

- new index to move the column

**Throws:**
- IllegalArgumentException

- if

column

or

newIndex

are not in the valid range

---

#### public void setColumnMargin​(int newMargin)

Sets the column margin to

newMargin

. This method
also posts a

columnMarginChanged

event to its
listeners.

**Specified by:**
- setColumnMargin

in interface

TableColumnModel

**Parameters:**
- newMargin

- the new margin width, in pixels

**See Also:**
- getColumnMargin()

,

getTotalColumnWidth()

---

#### public int getColumnCount()

Returns the number of columns in the

tableColumns

array.

**Specified by:**
- getColumnCount

in interface

TableColumnModel

**Returns:**
- the number of columns in the

tableColumns

array

**See Also:**
- getColumns()

---

#### public
Enumeration
<
TableColumn
> getColumns()

Returns an

Enumeration

of all the columns in the model.

**Specified by:**
- getColumns

in interface

TableColumnModel

**Returns:**
- an

Enumeration

of the columns in the model

---

#### public int getColumnIndex​(
Object
identifier)

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

**Specified by:**
- getColumnIndex

in interface

TableColumnModel

**Parameters:**
- identifier

- the identifier object

**Returns:**
- the index of the first column in the

tableColumns

array whose identifier
is equal to

identifier

**Throws:**
- IllegalArgumentException

- if

identifier

is

null

, or if no

TableColumn

has this

identifier

**See Also:**
- getColumn(int)

---

#### public
TableColumn
getColumn​(int columnIndex)

Returns the

TableColumn

object for the column
at

columnIndex

.

**Specified by:**
- getColumn

in interface

TableColumnModel

**Parameters:**
- columnIndex

- the index of the column desired

**Returns:**
- the

TableColumn

object for the column
at

columnIndex

---

#### public int getColumnMargin()

Returns the width margin for

TableColumn

.
The default

columnMargin

is 1.

**Specified by:**
- getColumnMargin

in interface

TableColumnModel

**Returns:**
- the maximum width for the

TableColumn

**See Also:**
- setColumnMargin(int)

---

#### public int getColumnIndexAtX​(int x)

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

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

**Specified by:**
- getColumnIndexAtX

in interface

TableColumnModel

**Parameters:**
- x

- the horizontal location of interest

**Returns:**
- the index of the column or -1 if no column is found

**See Also:**
- JTable.columnAtPoint(java.awt.Point)

---

#### public int getTotalColumnWidth()

Returns the total combined width of all columns.

**Specified by:**
- getTotalColumnWidth

in interface

TableColumnModel

**Returns:**
- the

totalColumnWidth

property

---

#### public void setSelectionModel​(
ListSelectionModel
newModel)

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model. If

newModel

is

null

,
an exception is thrown.

**Specified by:**
- setSelectionModel

in interface

TableColumnModel

**Parameters:**
- newModel

- the new selection model

**Throws:**
- IllegalArgumentException

- if

newModel

is

null

**See Also:**
- getSelectionModel()

---

#### public
ListSelectionModel
getSelectionModel()

Returns the

ListSelectionModel

that is used to
maintain column selection state.

**Specified by:**
- getSelectionModel

in interface

TableColumnModel

**Returns:**
- the object that provides column selection state. Or

null

if row selection is not allowed.

**See Also:**
- setSelectionModel(javax.swing.ListSelectionModel)

---

#### public void setColumnSelectionAllowed​(boolean flag)

Sets whether column selection is allowed. The default is false.

**Specified by:**
- setColumnSelectionAllowed

in interface

TableColumnModel

**Parameters:**
- flag

- true if column selection will be allowed, false otherwise

**See Also:**
- TableColumnModel.getColumnSelectionAllowed()

---

#### public boolean getColumnSelectionAllowed()

Returns true if column selection is allowed, otherwise false.
The default is false.

**Specified by:**
- getColumnSelectionAllowed

in interface

TableColumnModel

**Returns:**
- the

columnSelectionAllowed

property

**See Also:**
- TableColumnModel.setColumnSelectionAllowed(boolean)

---

#### public int[] getSelectedColumns()

Returns an array of selected columns. If

selectionModel

is

null

, returns an empty array.

**Specified by:**
- getSelectedColumns

in interface

TableColumnModel

**Returns:**
- an array of selected columns or an empty array if nothing
is selected or the

selectionModel

is

null

---

#### public int getSelectedColumnCount()

Returns the number of columns selected.

**Specified by:**
- getSelectedColumnCount

in interface

TableColumnModel

**Returns:**
- the number of columns selected

---

#### public void addColumnModelListener​(
TableColumnModelListener
x)

Adds a listener for table column model events.

**Specified by:**
- addColumnModelListener

in interface

TableColumnModel

**Parameters:**
- x

- a

TableColumnModelListener

object

---

#### public void removeColumnModelListener​(
TableColumnModelListener
x)

Removes a listener for table column model events.

**Specified by:**
- removeColumnModelListener

in interface

TableColumnModel

**Parameters:**
- x

- a

TableColumnModelListener

object

---

#### public
TableColumnModelListener
[] getColumnModelListeners()

Returns an array of all the column model listeners
registered on this model.

**Returns:**
- all of this default table column model's

ColumnModelListener

s
or an empty
array if no column model listeners are currently registered

**See Also:**
- addColumnModelListener(javax.swing.event.TableColumnModelListener)

,

removeColumnModelListener(javax.swing.event.TableColumnModelListener)

**Since:**
- 1.4

---

#### protected void fireColumnAdded​(
TableColumnModelEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event received

**See Also:**
- EventListenerList

---

#### protected void fireColumnRemoved​(
TableColumnModelEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event received

**See Also:**
- EventListenerList

---

#### protected void fireColumnMoved​(
TableColumnModelEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event received

**See Also:**
- EventListenerList

---

#### protected void fireColumnSelectionChanged​(
ListSelectionEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event received

**See Also:**
- EventListenerList

---

#### protected void fireColumnMarginChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**See Also:**
- EventListenerList

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
upon this model.

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

DefaultTableColumnModel

m

for its column model listeners with the following code:

```java
ColumnModelListener[] cmls = (ColumnModelListener[])(m.getListeners(ColumnModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this model,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- getColumnModelListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the listener type

---

#### public void propertyChange​(
PropertyChangeEvent
evt)

Property Change Listener change method. Used to track changes
to the column width or preferred column width.

**Specified by:**
- propertyChange

in interface

PropertyChangeListener

**Parameters:**
- evt

-

PropertyChangeEvent

---

#### public void valueChanged​(
ListSelectionEvent
e)

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

**Specified by:**
- valueChanged

in interface

ListSelectionListener

**Parameters:**
- e

- the change event

---

#### protected
ListSelectionModel
createSelectionModel()

Creates a new default list selection model.

**Returns:**
- a newly created default list selection model.

---

#### protected void recalcWidthCache()

Recalculates the total combined width of all columns. Updates the

totalColumnWidth

property.

---

### Additional Sections

#### Class DefaultTableColumnModel

java.lang.Object

- javax.swing.table.DefaultTableColumnModel

javax.swing.table.DefaultTableColumnModel

**All Implemented Interfaces:** PropertyChangeListener

,

Serializable

,

EventListener

,

ListSelectionListener

,

TableColumnModel

```java
public class
DefaultTableColumnModel

extends
Object

implements
TableColumnModel
,
PropertyChangeListener
,
ListSelectionListener
,
Serializable
```

The standard column-handler for a

JTable

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

**See Also:** JTable

,

Serialized Form

public class

DefaultTableColumnModel

extends

Object

implements

TableColumnModel

,

PropertyChangeListener

,

ListSelectionListener

,

Serializable

The standard column-handler for a

JTable

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

ChangeEvent

changeEvent

Change event (only one needed)

protected int

columnMargin

Width margin between each column

protected boolean

columnSelectionAllowed

Column selection allowed in this column model

protected

EventListenerList

listenerList

List of TableColumnModelListener

protected

ListSelectionModel

selectionModel

Model for keeping track of column selections

protected

Vector

<

TableColumn

>

tableColumns

Array of TableColumn objects in this model

protected int

totalColumnWidth

A local cache of the combined width of all columns

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultTableColumnModel

()

Creates a default table column model.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

protected

ListSelectionModel

createSelectionModel

()

Creates a new default list selection model.

protected void

fireColumnAdded

​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnMarginChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnMoved

​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnRemoved

​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnSelectionChanged

​(

ListSelectionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

TableColumn

getColumn

​(int columnIndex)

Returns the

TableColumn

object for the column
at

columnIndex

.

int

getColumnCount

()

Returns the number of columns in the

tableColumns

array.

int

getColumnIndex

​(

Object

identifier)

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

int

getColumnIndexAtX

​(int x)

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

int

getColumnMargin

()

Returns the width margin for

TableColumn

.

TableColumnModelListener

[]

getColumnModelListeners

()

Returns an array of all the column model listeners
registered on this model.

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

Returns true if column selection is allowed, otherwise false.

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
upon this model.

int

getSelectedColumnCount

()

Returns the number of columns selected.

int[]

getSelectedColumns

()

Returns an array of selected columns.

ListSelectionModel

getSelectionModel

()

Returns the

ListSelectionModel

that is used to
maintain column selection state.

int

getTotalColumnWidth

()

Returns the total combined width of all columns.

void

moveColumn

​(int columnIndex,
int newIndex)

Moves the column and heading at

columnIndex

to

newIndex

.

void

propertyChange

​(

PropertyChangeEvent

evt)

Property Change Listener change method.

protected void

recalcWidthCache

()

Recalculates the total combined width of all columns.

void

removeColumn

​(

TableColumn

column)

Deletes the

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

Sets the column margin to

newMargin

.

void

setColumnSelectionAllowed

​(boolean flag)

Sets whether column selection is allowed.

void

setSelectionModel

​(

ListSelectionModel

newModel)

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model.

void

valueChanged

​(

ListSelectionEvent

e)

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

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

ChangeEvent

changeEvent

Change event (only one needed)

protected int

columnMargin

Width margin between each column

protected boolean

columnSelectionAllowed

Column selection allowed in this column model

protected

EventListenerList

listenerList

List of TableColumnModelListener

protected

ListSelectionModel

selectionModel

Model for keeping track of column selections

protected

Vector

<

TableColumn

>

tableColumns

Array of TableColumn objects in this model

protected int

totalColumnWidth

A local cache of the combined width of all columns

---

#### Field Summary

Change event (only one needed)

Width margin between each column

Column selection allowed in this column model

List of TableColumnModelListener

Model for keeping track of column selections

Array of TableColumn objects in this model

A local cache of the combined width of all columns

Constructor Summary

Constructors

Constructor

Description

DefaultTableColumnModel

()

Creates a default table column model.

---

#### Constructor Summary

Creates a default table column model.

Method Summary

All Methods

Instance Methods

Concrete Methods

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

protected

ListSelectionModel

createSelectionModel

()

Creates a new default list selection model.

protected void

fireColumnAdded

​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnMarginChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnMoved

​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnRemoved

​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireColumnSelectionChanged

​(

ListSelectionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

TableColumn

getColumn

​(int columnIndex)

Returns the

TableColumn

object for the column
at

columnIndex

.

int

getColumnCount

()

Returns the number of columns in the

tableColumns

array.

int

getColumnIndex

​(

Object

identifier)

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

int

getColumnIndexAtX

​(int x)

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

int

getColumnMargin

()

Returns the width margin for

TableColumn

.

TableColumnModelListener

[]

getColumnModelListeners

()

Returns an array of all the column model listeners
registered on this model.

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

Returns true if column selection is allowed, otherwise false.

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
upon this model.

int

getSelectedColumnCount

()

Returns the number of columns selected.

int[]

getSelectedColumns

()

Returns an array of selected columns.

ListSelectionModel

getSelectionModel

()

Returns the

ListSelectionModel

that is used to
maintain column selection state.

int

getTotalColumnWidth

()

Returns the total combined width of all columns.

void

moveColumn

​(int columnIndex,
int newIndex)

Moves the column and heading at

columnIndex

to

newIndex

.

void

propertyChange

​(

PropertyChangeEvent

evt)

Property Change Listener change method.

protected void

recalcWidthCache

()

Recalculates the total combined width of all columns.

void

removeColumn

​(

TableColumn

column)

Deletes the

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

Sets the column margin to

newMargin

.

void

setColumnSelectionAllowed

​(boolean flag)

Sets whether column selection is allowed.

void

setSelectionModel

​(

ListSelectionModel

newModel)

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model.

void

valueChanged

​(

ListSelectionEvent

e)

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

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

Appends

aColumn

to the end of the

tableColumns

array.

Adds a listener for table column model events.

Creates a new default list selection model.

Notifies all listeners that have registered interest for
notification on this event type.

Returns the

TableColumn

object for the column
at

columnIndex

.

Returns the number of columns in the

tableColumns

array.

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

Returns the width margin for

TableColumn

.

Returns an array of all the column model listeners
registered on this model.

Returns an

Enumeration

of all the columns in the model.

Returns true if column selection is allowed, otherwise false.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this model.

Returns the number of columns selected.

Returns an array of selected columns.

Returns the

ListSelectionModel

that is used to
maintain column selection state.

Returns the total combined width of all columns.

Moves the column and heading at

columnIndex

to

newIndex

.

Property Change Listener change method.

Recalculates the total combined width of all columns.

Deletes the

column

from the

tableColumns

array.

Removes a listener for table column model events.

Sets the column margin to

newMargin

.

Sets whether column selection is allowed.

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model.

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

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

- tableColumns

```java
protected
Vector
<
TableColumn
> tableColumns
```

Array of TableColumn objects in this model

- selectionModel

```java
protected
ListSelectionModel
selectionModel
```

Model for keeping track of column selections

- columnMargin

```java
protected int columnMargin
```

Width margin between each column

- listenerList

```java
protected
EventListenerList
listenerList
```

List of TableColumnModelListener

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Change event (only one needed)

- columnSelectionAllowed

```java
protected boolean columnSelectionAllowed
```

Column selection allowed in this column model

- totalColumnWidth

```java
protected int totalColumnWidth
```

A local cache of the combined width of all columns

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultTableColumnModel

```java
public DefaultTableColumnModel()
```

Creates a default table column model.

============ METHOD DETAIL ==========

- Method Detail

- addColumn

```java
public void addColumn​(
TableColumn
aColumn)
```

Appends

aColumn

to the end of the

tableColumns

array.
This method also posts the

columnAdded

event to its listeners.

**Specified by:** addColumn

in interface

TableColumnModel
**Parameters:** aColumn

- the

TableColumn

to be added
**Throws:** IllegalArgumentException

- if

aColumn

is

null
**See Also:** removeColumn(javax.swing.table.TableColumn)

- removeColumn

```java
public void removeColumn​(
TableColumn
column)
```

Deletes the

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's columns list.

tile

is called
to resize both the header and table views.
This method also posts a

columnRemoved

event to its listeners.

**Specified by:** removeColumn

in interface

TableColumnModel
**Parameters:** column

- the

TableColumn

to be removed
**See Also:** addColumn(javax.swing.table.TableColumn)

- moveColumn

```java
public void moveColumn​(int columnIndex,
int newIndex)
```

Moves the column and heading at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column
that used to be at

newIndex

is shifted
left or right to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
also posts a

columnMoved

event to its listeners.

**Specified by:** moveColumn

in interface

TableColumnModel
**Parameters:** columnIndex

- the index of column to be moved
**Parameters:** newIndex

- new index to move the column
**Throws:** IllegalArgumentException

- if

column

or

newIndex

are not in the valid range

- setColumnMargin

```java
public void setColumnMargin​(int newMargin)
```

Sets the column margin to

newMargin

. This method
also posts a

columnMarginChanged

event to its
listeners.

**Specified by:** setColumnMargin

in interface

TableColumnModel
**Parameters:** newMargin

- the new margin width, in pixels
**See Also:** getColumnMargin()

,

getTotalColumnWidth()

- getColumnCount

```java
public int getColumnCount()
```

Returns the number of columns in the

tableColumns

array.

**Specified by:** getColumnCount

in interface

TableColumnModel
**Returns:** the number of columns in the

tableColumns

array
**See Also:** getColumns()

- getColumns

```java
public
Enumeration
<
TableColumn
> getColumns()
```

Returns an

Enumeration

of all the columns in the model.

**Specified by:** getColumns

in interface

TableColumnModel
**Returns:** an

Enumeration

of the columns in the model

- getColumnIndex

```java
public int getColumnIndex​(
Object
identifier)
```

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

**Specified by:** getColumnIndex

in interface

TableColumnModel
**Parameters:** identifier

- the identifier object
**Returns:** the index of the first column in the

tableColumns

array whose identifier
is equal to

identifier
**Throws:** IllegalArgumentException

- if

identifier

is

null

, or if no

TableColumn

has this

identifier
**See Also:** getColumn(int)

- getColumn

```java
public
TableColumn
getColumn​(int columnIndex)
```

Returns the

TableColumn

object for the column
at

columnIndex

.

**Specified by:** getColumn

in interface

TableColumnModel
**Parameters:** columnIndex

- the index of the column desired
**Returns:** the

TableColumn

object for the column
at

columnIndex

- getColumnMargin

```java
public int getColumnMargin()
```

Returns the width margin for

TableColumn

.
The default

columnMargin

is 1.

**Specified by:** getColumnMargin

in interface

TableColumnModel
**Returns:** the maximum width for the

TableColumn
**See Also:** setColumnMargin(int)

- getColumnIndexAtX

```java
public int getColumnIndexAtX​(int x)
```

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

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

**Specified by:** getColumnIndexAtX

in interface

TableColumnModel
**Parameters:** x

- the horizontal location of interest
**Returns:** the index of the column or -1 if no column is found
**See Also:** JTable.columnAtPoint(java.awt.Point)

- getTotalColumnWidth

```java
public int getTotalColumnWidth()
```

Returns the total combined width of all columns.

**Specified by:** getTotalColumnWidth

in interface

TableColumnModel
**Returns:** the

totalColumnWidth

property

- setSelectionModel

```java
public void setSelectionModel​(
ListSelectionModel
newModel)
```

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model. If

newModel

is

null

,
an exception is thrown.

**Specified by:** setSelectionModel

in interface

TableColumnModel
**Parameters:** newModel

- the new selection model
**Throws:** IllegalArgumentException

- if

newModel

is

null
**See Also:** getSelectionModel()

- getSelectionModel

```java
public
ListSelectionModel
getSelectionModel()
```

Returns the

ListSelectionModel

that is used to
maintain column selection state.

**Specified by:** getSelectionModel

in interface

TableColumnModel
**Returns:** the object that provides column selection state. Or

null

if row selection is not allowed.
**See Also:** setSelectionModel(javax.swing.ListSelectionModel)

- setColumnSelectionAllowed

```java
public void setColumnSelectionAllowed​(boolean flag)
```

Sets whether column selection is allowed. The default is false.

**Specified by:** setColumnSelectionAllowed

in interface

TableColumnModel
**Parameters:** flag

- true if column selection will be allowed, false otherwise
**See Also:** TableColumnModel.getColumnSelectionAllowed()

- getColumnSelectionAllowed

```java
public boolean getColumnSelectionAllowed()
```

Returns true if column selection is allowed, otherwise false.
The default is false.

**Specified by:** getColumnSelectionAllowed

in interface

TableColumnModel
**Returns:** the

columnSelectionAllowed

property
**See Also:** TableColumnModel.setColumnSelectionAllowed(boolean)

- getSelectedColumns

```java
public int[] getSelectedColumns()
```

Returns an array of selected columns. If

selectionModel

is

null

, returns an empty array.

**Specified by:** getSelectedColumns

in interface

TableColumnModel
**Returns:** an array of selected columns or an empty array if nothing
is selected or the

selectionModel

is

null

- getSelectedColumnCount

```java
public int getSelectedColumnCount()
```

Returns the number of columns selected.

**Specified by:** getSelectedColumnCount

in interface

TableColumnModel
**Returns:** the number of columns selected

- addColumnModelListener

```java
public void addColumnModelListener​(
TableColumnModelListener
x)
```

Adds a listener for table column model events.

**Specified by:** addColumnModelListener

in interface

TableColumnModel
**Parameters:** x

- a

TableColumnModelListener

object

- removeColumnModelListener

```java
public void removeColumnModelListener​(
TableColumnModelListener
x)
```

Removes a listener for table column model events.

**Specified by:** removeColumnModelListener

in interface

TableColumnModel
**Parameters:** x

- a

TableColumnModelListener

object

- getColumnModelListeners

```java
public
TableColumnModelListener
[] getColumnModelListeners()
```

Returns an array of all the column model listeners
registered on this model.

**Returns:** all of this default table column model's

ColumnModelListener

s
or an empty
array if no column model listeners are currently registered
**Since:** 1.4
**See Also:** addColumnModelListener(javax.swing.event.TableColumnModelListener)

,

removeColumnModelListener(javax.swing.event.TableColumnModelListener)

- fireColumnAdded

```java
protected void fireColumnAdded​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnRemoved

```java
protected void fireColumnRemoved​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnMoved

```java
protected void fireColumnMoved​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnSelectionChanged

```java
protected void fireColumnSelectionChanged​(
ListSelectionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnMarginChanged

```java
protected void fireColumnMarginChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**See Also:** EventListenerList

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
upon this model.

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

DefaultTableColumnModel

m

for its column model listeners with the following code:

```java
ColumnModelListener[] cmls = (ColumnModelListener[])(m.getListeners(ColumnModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getColumnModelListeners()

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
evt)
```

Property Change Listener change method. Used to track changes
to the column width or preferred column width.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** evt

-

PropertyChangeEvent

- valueChanged

```java
public void valueChanged​(
ListSelectionEvent
e)
```

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

**Specified by:** valueChanged

in interface

ListSelectionListener
**Parameters:** e

- the change event

- createSelectionModel

```java
protected
ListSelectionModel
createSelectionModel()
```

Creates a new default list selection model.

**Returns:** a newly created default list selection model.

- recalcWidthCache

```java
protected void recalcWidthCache()
```

Recalculates the total combined width of all columns. Updates the

totalColumnWidth

property.

Field Detail

- tableColumns

```java
protected
Vector
<
TableColumn
> tableColumns
```

Array of TableColumn objects in this model

- selectionModel

```java
protected
ListSelectionModel
selectionModel
```

Model for keeping track of column selections

- columnMargin

```java
protected int columnMargin
```

Width margin between each column

- listenerList

```java
protected
EventListenerList
listenerList
```

List of TableColumnModelListener

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Change event (only one needed)

- columnSelectionAllowed

```java
protected boolean columnSelectionAllowed
```

Column selection allowed in this column model

- totalColumnWidth

```java
protected int totalColumnWidth
```

A local cache of the combined width of all columns

---

#### Field Detail

tableColumns

```java
protected
Vector
<
TableColumn
> tableColumns
```

Array of TableColumn objects in this model

---

#### tableColumns

protected

Vector

<

TableColumn

> tableColumns

Array of TableColumn objects in this model

selectionModel

```java
protected
ListSelectionModel
selectionModel
```

Model for keeping track of column selections

---

#### selectionModel

protected

ListSelectionModel

selectionModel

Model for keeping track of column selections

columnMargin

```java
protected int columnMargin
```

Width margin between each column

---

#### columnMargin

protected int columnMargin

Width margin between each column

listenerList

```java
protected
EventListenerList
listenerList
```

List of TableColumnModelListener

---

#### listenerList

protected

EventListenerList

listenerList

List of TableColumnModelListener

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Change event (only one needed)

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Change event (only one needed)

columnSelectionAllowed

```java
protected boolean columnSelectionAllowed
```

Column selection allowed in this column model

---

#### columnSelectionAllowed

protected boolean columnSelectionAllowed

Column selection allowed in this column model

totalColumnWidth

```java
protected int totalColumnWidth
```

A local cache of the combined width of all columns

---

#### totalColumnWidth

protected int totalColumnWidth

A local cache of the combined width of all columns

Constructor Detail

- DefaultTableColumnModel

```java
public DefaultTableColumnModel()
```

Creates a default table column model.

---

#### Constructor Detail

DefaultTableColumnModel

```java
public DefaultTableColumnModel()
```

Creates a default table column model.

---

#### DefaultTableColumnModel

public DefaultTableColumnModel()

Creates a default table column model.

Method Detail

- addColumn

```java
public void addColumn​(
TableColumn
aColumn)
```

Appends

aColumn

to the end of the

tableColumns

array.
This method also posts the

columnAdded

event to its listeners.

**Specified by:** addColumn

in interface

TableColumnModel
**Parameters:** aColumn

- the

TableColumn

to be added
**Throws:** IllegalArgumentException

- if

aColumn

is

null
**See Also:** removeColumn(javax.swing.table.TableColumn)

- removeColumn

```java
public void removeColumn​(
TableColumn
column)
```

Deletes the

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's columns list.

tile

is called
to resize both the header and table views.
This method also posts a

columnRemoved

event to its listeners.

**Specified by:** removeColumn

in interface

TableColumnModel
**Parameters:** column

- the

TableColumn

to be removed
**See Also:** addColumn(javax.swing.table.TableColumn)

- moveColumn

```java
public void moveColumn​(int columnIndex,
int newIndex)
```

Moves the column and heading at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column
that used to be at

newIndex

is shifted
left or right to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
also posts a

columnMoved

event to its listeners.

**Specified by:** moveColumn

in interface

TableColumnModel
**Parameters:** columnIndex

- the index of column to be moved
**Parameters:** newIndex

- new index to move the column
**Throws:** IllegalArgumentException

- if

column

or

newIndex

are not in the valid range

- setColumnMargin

```java
public void setColumnMargin​(int newMargin)
```

Sets the column margin to

newMargin

. This method
also posts a

columnMarginChanged

event to its
listeners.

**Specified by:** setColumnMargin

in interface

TableColumnModel
**Parameters:** newMargin

- the new margin width, in pixels
**See Also:** getColumnMargin()

,

getTotalColumnWidth()

- getColumnCount

```java
public int getColumnCount()
```

Returns the number of columns in the

tableColumns

array.

**Specified by:** getColumnCount

in interface

TableColumnModel
**Returns:** the number of columns in the

tableColumns

array
**See Also:** getColumns()

- getColumns

```java
public
Enumeration
<
TableColumn
> getColumns()
```

Returns an

Enumeration

of all the columns in the model.

**Specified by:** getColumns

in interface

TableColumnModel
**Returns:** an

Enumeration

of the columns in the model

- getColumnIndex

```java
public int getColumnIndex​(
Object
identifier)
```

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

**Specified by:** getColumnIndex

in interface

TableColumnModel
**Parameters:** identifier

- the identifier object
**Returns:** the index of the first column in the

tableColumns

array whose identifier
is equal to

identifier
**Throws:** IllegalArgumentException

- if

identifier

is

null

, or if no

TableColumn

has this

identifier
**See Also:** getColumn(int)

- getColumn

```java
public
TableColumn
getColumn​(int columnIndex)
```

Returns the

TableColumn

object for the column
at

columnIndex

.

**Specified by:** getColumn

in interface

TableColumnModel
**Parameters:** columnIndex

- the index of the column desired
**Returns:** the

TableColumn

object for the column
at

columnIndex

- getColumnMargin

```java
public int getColumnMargin()
```

Returns the width margin for

TableColumn

.
The default

columnMargin

is 1.

**Specified by:** getColumnMargin

in interface

TableColumnModel
**Returns:** the maximum width for the

TableColumn
**See Also:** setColumnMargin(int)

- getColumnIndexAtX

```java
public int getColumnIndexAtX​(int x)
```

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

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

**Specified by:** getColumnIndexAtX

in interface

TableColumnModel
**Parameters:** x

- the horizontal location of interest
**Returns:** the index of the column or -1 if no column is found
**See Also:** JTable.columnAtPoint(java.awt.Point)

- getTotalColumnWidth

```java
public int getTotalColumnWidth()
```

Returns the total combined width of all columns.

**Specified by:** getTotalColumnWidth

in interface

TableColumnModel
**Returns:** the

totalColumnWidth

property

- setSelectionModel

```java
public void setSelectionModel​(
ListSelectionModel
newModel)
```

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model. If

newModel

is

null

,
an exception is thrown.

**Specified by:** setSelectionModel

in interface

TableColumnModel
**Parameters:** newModel

- the new selection model
**Throws:** IllegalArgumentException

- if

newModel

is

null
**See Also:** getSelectionModel()

- getSelectionModel

```java
public
ListSelectionModel
getSelectionModel()
```

Returns the

ListSelectionModel

that is used to
maintain column selection state.

**Specified by:** getSelectionModel

in interface

TableColumnModel
**Returns:** the object that provides column selection state. Or

null

if row selection is not allowed.
**See Also:** setSelectionModel(javax.swing.ListSelectionModel)

- setColumnSelectionAllowed

```java
public void setColumnSelectionAllowed​(boolean flag)
```

Sets whether column selection is allowed. The default is false.

**Specified by:** setColumnSelectionAllowed

in interface

TableColumnModel
**Parameters:** flag

- true if column selection will be allowed, false otherwise
**See Also:** TableColumnModel.getColumnSelectionAllowed()

- getColumnSelectionAllowed

```java
public boolean getColumnSelectionAllowed()
```

Returns true if column selection is allowed, otherwise false.
The default is false.

**Specified by:** getColumnSelectionAllowed

in interface

TableColumnModel
**Returns:** the

columnSelectionAllowed

property
**See Also:** TableColumnModel.setColumnSelectionAllowed(boolean)

- getSelectedColumns

```java
public int[] getSelectedColumns()
```

Returns an array of selected columns. If

selectionModel

is

null

, returns an empty array.

**Specified by:** getSelectedColumns

in interface

TableColumnModel
**Returns:** an array of selected columns or an empty array if nothing
is selected or the

selectionModel

is

null

- getSelectedColumnCount

```java
public int getSelectedColumnCount()
```

Returns the number of columns selected.

**Specified by:** getSelectedColumnCount

in interface

TableColumnModel
**Returns:** the number of columns selected

- addColumnModelListener

```java
public void addColumnModelListener​(
TableColumnModelListener
x)
```

Adds a listener for table column model events.

**Specified by:** addColumnModelListener

in interface

TableColumnModel
**Parameters:** x

- a

TableColumnModelListener

object

- removeColumnModelListener

```java
public void removeColumnModelListener​(
TableColumnModelListener
x)
```

Removes a listener for table column model events.

**Specified by:** removeColumnModelListener

in interface

TableColumnModel
**Parameters:** x

- a

TableColumnModelListener

object

- getColumnModelListeners

```java
public
TableColumnModelListener
[] getColumnModelListeners()
```

Returns an array of all the column model listeners
registered on this model.

**Returns:** all of this default table column model's

ColumnModelListener

s
or an empty
array if no column model listeners are currently registered
**Since:** 1.4
**See Also:** addColumnModelListener(javax.swing.event.TableColumnModelListener)

,

removeColumnModelListener(javax.swing.event.TableColumnModelListener)

- fireColumnAdded

```java
protected void fireColumnAdded​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnRemoved

```java
protected void fireColumnRemoved​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnMoved

```java
protected void fireColumnMoved​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnSelectionChanged

```java
protected void fireColumnSelectionChanged​(
ListSelectionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

- fireColumnMarginChanged

```java
protected void fireColumnMarginChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**See Also:** EventListenerList

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
upon this model.

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

DefaultTableColumnModel

m

for its column model listeners with the following code:

```java
ColumnModelListener[] cmls = (ColumnModelListener[])(m.getListeners(ColumnModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getColumnModelListeners()

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
evt)
```

Property Change Listener change method. Used to track changes
to the column width or preferred column width.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** evt

-

PropertyChangeEvent

- valueChanged

```java
public void valueChanged​(
ListSelectionEvent
e)
```

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

**Specified by:** valueChanged

in interface

ListSelectionListener
**Parameters:** e

- the change event

- createSelectionModel

```java
protected
ListSelectionModel
createSelectionModel()
```

Creates a new default list selection model.

**Returns:** a newly created default list selection model.

- recalcWidthCache

```java
protected void recalcWidthCache()
```

Recalculates the total combined width of all columns. Updates the

totalColumnWidth

property.

---

#### Method Detail

addColumn

```java
public void addColumn​(
TableColumn
aColumn)
```

Appends

aColumn

to the end of the

tableColumns

array.
This method also posts the

columnAdded

event to its listeners.

**Specified by:** addColumn

in interface

TableColumnModel
**Parameters:** aColumn

- the

TableColumn

to be added
**Throws:** IllegalArgumentException

- if

aColumn

is

null
**See Also:** removeColumn(javax.swing.table.TableColumn)

---

#### addColumn

public void addColumn​(

TableColumn

aColumn)

Appends

aColumn

to the end of the

tableColumns

array.
This method also posts the

columnAdded

event to its listeners.

removeColumn

```java
public void removeColumn​(
TableColumn
column)
```

Deletes the

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's columns list.

tile

is called
to resize both the header and table views.
This method also posts a

columnRemoved

event to its listeners.

**Specified by:** removeColumn

in interface

TableColumnModel
**Parameters:** column

- the

TableColumn

to be removed
**See Also:** addColumn(javax.swing.table.TableColumn)

---

#### removeColumn

public void removeColumn​(

TableColumn

column)

Deletes the

column

from the

tableColumns

array. This method will do nothing if

column

is not in the table's columns list.

tile

is called
to resize both the header and table views.
This method also posts a

columnRemoved

event to its listeners.

moveColumn

```java
public void moveColumn​(int columnIndex,
int newIndex)
```

Moves the column and heading at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column
that used to be at

newIndex

is shifted
left or right to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
also posts a

columnMoved

event to its listeners.

**Specified by:** moveColumn

in interface

TableColumnModel
**Parameters:** columnIndex

- the index of column to be moved
**Parameters:** newIndex

- new index to move the column
**Throws:** IllegalArgumentException

- if

column

or

newIndex

are not in the valid range

---

#### moveColumn

public void moveColumn​(int columnIndex,
int newIndex)

Moves the column and heading at

columnIndex

to

newIndex

. The old column at

columnIndex

will now be found at

newIndex

. The column
that used to be at

newIndex

is shifted
left or right to make room. This will not move any columns if

columnIndex

equals

newIndex

. This method
also posts a

columnMoved

event to its listeners.

setColumnMargin

```java
public void setColumnMargin​(int newMargin)
```

Sets the column margin to

newMargin

. This method
also posts a

columnMarginChanged

event to its
listeners.

**Specified by:** setColumnMargin

in interface

TableColumnModel
**Parameters:** newMargin

- the new margin width, in pixels
**See Also:** getColumnMargin()

,

getTotalColumnWidth()

---

#### setColumnMargin

public void setColumnMargin​(int newMargin)

Sets the column margin to

newMargin

. This method
also posts a

columnMarginChanged

event to its
listeners.

getColumnCount

```java
public int getColumnCount()
```

Returns the number of columns in the

tableColumns

array.

**Specified by:** getColumnCount

in interface

TableColumnModel
**Returns:** the number of columns in the

tableColumns

array
**See Also:** getColumns()

---

#### getColumnCount

public int getColumnCount()

Returns the number of columns in the

tableColumns

array.

getColumns

```java
public
Enumeration
<
TableColumn
> getColumns()
```

Returns an

Enumeration

of all the columns in the model.

**Specified by:** getColumns

in interface

TableColumnModel
**Returns:** an

Enumeration

of the columns in the model

---

#### getColumns

public

Enumeration

<

TableColumn

> getColumns()

Returns an

Enumeration

of all the columns in the model.

getColumnIndex

```java
public int getColumnIndex​(
Object
identifier)
```

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

**Specified by:** getColumnIndex

in interface

TableColumnModel
**Parameters:** identifier

- the identifier object
**Returns:** the index of the first column in the

tableColumns

array whose identifier
is equal to

identifier
**Throws:** IllegalArgumentException

- if

identifier

is

null

, or if no

TableColumn

has this

identifier
**See Also:** getColumn(int)

---

#### getColumnIndex

public int getColumnIndex​(

Object

identifier)

Returns the index of the first column in the

tableColumns

array whose identifier is equal to

identifier

,
when compared using

equals

.

getColumn

```java
public
TableColumn
getColumn​(int columnIndex)
```

Returns the

TableColumn

object for the column
at

columnIndex

.

**Specified by:** getColumn

in interface

TableColumnModel
**Parameters:** columnIndex

- the index of the column desired
**Returns:** the

TableColumn

object for the column
at

columnIndex

---

#### getColumn

public

TableColumn

getColumn​(int columnIndex)

Returns the

TableColumn

object for the column
at

columnIndex

.

getColumnMargin

```java
public int getColumnMargin()
```

Returns the width margin for

TableColumn

.
The default

columnMargin

is 1.

**Specified by:** getColumnMargin

in interface

TableColumnModel
**Returns:** the maximum width for the

TableColumn
**See Also:** setColumnMargin(int)

---

#### getColumnMargin

public int getColumnMargin()

Returns the width margin for

TableColumn

.
The default

columnMargin

is 1.

getColumnIndexAtX

```java
public int getColumnIndexAtX​(int x)
```

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

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

**Specified by:** getColumnIndexAtX

in interface

TableColumnModel
**Parameters:** x

- the horizontal location of interest
**Returns:** the index of the column or -1 if no column is found
**See Also:** JTable.columnAtPoint(java.awt.Point)

---

#### getColumnIndexAtX

public int getColumnIndexAtX​(int x)

Returns the index of the column that lies at position

x

,
or -1 if no column covers this point.

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
public int getTotalColumnWidth()
```

Returns the total combined width of all columns.

**Specified by:** getTotalColumnWidth

in interface

TableColumnModel
**Returns:** the

totalColumnWidth

property

---

#### getTotalColumnWidth

public int getTotalColumnWidth()

Returns the total combined width of all columns.

setSelectionModel

```java
public void setSelectionModel​(
ListSelectionModel
newModel)
```

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model. If

newModel

is

null

,
an exception is thrown.

**Specified by:** setSelectionModel

in interface

TableColumnModel
**Parameters:** newModel

- the new selection model
**Throws:** IllegalArgumentException

- if

newModel

is

null
**See Also:** getSelectionModel()

---

#### setSelectionModel

public void setSelectionModel​(

ListSelectionModel

newModel)

Sets the selection model for this

TableColumnModel

to

newModel

and registers for listener notifications from the new selection
model. If

newModel

is

null

,
an exception is thrown.

getSelectionModel

```java
public
ListSelectionModel
getSelectionModel()
```

Returns the

ListSelectionModel

that is used to
maintain column selection state.

**Specified by:** getSelectionModel

in interface

TableColumnModel
**Returns:** the object that provides column selection state. Or

null

if row selection is not allowed.
**See Also:** setSelectionModel(javax.swing.ListSelectionModel)

---

#### getSelectionModel

public

ListSelectionModel

getSelectionModel()

Returns the

ListSelectionModel

that is used to
maintain column selection state.

setColumnSelectionAllowed

```java
public void setColumnSelectionAllowed​(boolean flag)
```

Sets whether column selection is allowed. The default is false.

**Specified by:** setColumnSelectionAllowed

in interface

TableColumnModel
**Parameters:** flag

- true if column selection will be allowed, false otherwise
**See Also:** TableColumnModel.getColumnSelectionAllowed()

---

#### setColumnSelectionAllowed

public void setColumnSelectionAllowed​(boolean flag)

Sets whether column selection is allowed. The default is false.

getColumnSelectionAllowed

```java
public boolean getColumnSelectionAllowed()
```

Returns true if column selection is allowed, otherwise false.
The default is false.

**Specified by:** getColumnSelectionAllowed

in interface

TableColumnModel
**Returns:** the

columnSelectionAllowed

property
**See Also:** TableColumnModel.setColumnSelectionAllowed(boolean)

---

#### getColumnSelectionAllowed

public boolean getColumnSelectionAllowed()

Returns true if column selection is allowed, otherwise false.
The default is false.

getSelectedColumns

```java
public int[] getSelectedColumns()
```

Returns an array of selected columns. If

selectionModel

is

null

, returns an empty array.

**Specified by:** getSelectedColumns

in interface

TableColumnModel
**Returns:** an array of selected columns or an empty array if nothing
is selected or the

selectionModel

is

null

---

#### getSelectedColumns

public int[] getSelectedColumns()

Returns an array of selected columns. If

selectionModel

is

null

, returns an empty array.

getSelectedColumnCount

```java
public int getSelectedColumnCount()
```

Returns the number of columns selected.

**Specified by:** getSelectedColumnCount

in interface

TableColumnModel
**Returns:** the number of columns selected

---

#### getSelectedColumnCount

public int getSelectedColumnCount()

Returns the number of columns selected.

addColumnModelListener

```java
public void addColumnModelListener​(
TableColumnModelListener
x)
```

Adds a listener for table column model events.

**Specified by:** addColumnModelListener

in interface

TableColumnModel
**Parameters:** x

- a

TableColumnModelListener

object

---

#### addColumnModelListener

public void addColumnModelListener​(

TableColumnModelListener

x)

Adds a listener for table column model events.

removeColumnModelListener

```java
public void removeColumnModelListener​(
TableColumnModelListener
x)
```

Removes a listener for table column model events.

**Specified by:** removeColumnModelListener

in interface

TableColumnModel
**Parameters:** x

- a

TableColumnModelListener

object

---

#### removeColumnModelListener

public void removeColumnModelListener​(

TableColumnModelListener

x)

Removes a listener for table column model events.

getColumnModelListeners

```java
public
TableColumnModelListener
[] getColumnModelListeners()
```

Returns an array of all the column model listeners
registered on this model.

**Returns:** all of this default table column model's

ColumnModelListener

s
or an empty
array if no column model listeners are currently registered
**Since:** 1.4
**See Also:** addColumnModelListener(javax.swing.event.TableColumnModelListener)

,

removeColumnModelListener(javax.swing.event.TableColumnModelListener)

---

#### getColumnModelListeners

public

TableColumnModelListener

[] getColumnModelListeners()

Returns an array of all the column model listeners
registered on this model.

fireColumnAdded

```java
protected void fireColumnAdded​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

---

#### fireColumnAdded

protected void fireColumnAdded​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

fireColumnRemoved

```java
protected void fireColumnRemoved​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

---

#### fireColumnRemoved

protected void fireColumnRemoved​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

fireColumnMoved

```java
protected void fireColumnMoved​(
TableColumnModelEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

---

#### fireColumnMoved

protected void fireColumnMoved​(

TableColumnModelEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

fireColumnSelectionChanged

```java
protected void fireColumnSelectionChanged​(
ListSelectionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event received
**See Also:** EventListenerList

---

#### fireColumnSelectionChanged

protected void fireColumnSelectionChanged​(

ListSelectionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

fireColumnMarginChanged

```java
protected void fireColumnMarginChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**See Also:** EventListenerList

---

#### fireColumnMarginChanged

protected void fireColumnMarginChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

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
upon this model.

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

DefaultTableColumnModel

m

for its column model listeners with the following code:

```java
ColumnModelListener[] cmls = (ColumnModelListener[])(m.getListeners(ColumnModelListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getColumnModelListeners()

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
upon this model.

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

DefaultTableColumnModel

m

for its column model listeners with the following code:

```java
ColumnModelListener[] cmls = (ColumnModelListener[])(m.getListeners(ColumnModelListener.class));
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

DefaultTableColumnModel

m

for its column model listeners with the following code:

```java
ColumnModelListener[] cmls = (ColumnModelListener[])(m.getListeners(ColumnModelListener.class));
```

If no such listeners exist, this method returns an empty array.

ColumnModelListener[] cmls = (ColumnModelListener[])(m.getListeners(ColumnModelListener.class));

propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
evt)
```

Property Change Listener change method. Used to track changes
to the column width or preferred column width.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** evt

-

PropertyChangeEvent

---

#### propertyChange

public void propertyChange​(

PropertyChangeEvent

evt)

Property Change Listener change method. Used to track changes
to the column width or preferred column width.

valueChanged

```java
public void valueChanged​(
ListSelectionEvent
e)
```

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

**Specified by:** valueChanged

in interface

ListSelectionListener
**Parameters:** e

- the change event

---

#### valueChanged

public void valueChanged​(

ListSelectionEvent

e)

A

ListSelectionListener

that forwards

ListSelectionEvents

when there is a column
selection change.

createSelectionModel

```java
protected
ListSelectionModel
createSelectionModel()
```

Creates a new default list selection model.

**Returns:** a newly created default list selection model.

---

#### createSelectionModel

protected

ListSelectionModel

createSelectionModel()

Creates a new default list selection model.

recalcWidthCache

```java
protected void recalcWidthCache()
```

Recalculates the total combined width of all columns. Updates the

totalColumnWidth

property.

---

#### recalcWidthCache

protected void recalcWidthCache()

Recalculates the total combined width of all columns. Updates the

totalColumnWidth

property.

---

