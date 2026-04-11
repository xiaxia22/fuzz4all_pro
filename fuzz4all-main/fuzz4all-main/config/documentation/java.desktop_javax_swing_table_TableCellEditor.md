# Interface TableCellEditor

**Source:** `java.desktop\javax\swing\table\TableCellEditor.html`

### Class Description

```java
public interface
TableCellEditor

extends
CellEditor
```

This interface defines the method any object that would like to be
an editor of values for components such as

JListBox

,

JComboBox

,

JTree

, or

JTable

needs to implement.

**All Superinterfaces:** CellEditor

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Component
getTableCellEditorComponent​(
JTable
table,

Object
value,
boolean isSelected,
int row,
int column)

Sets an initial

value

for the editor. This will cause
the editor to

stopEditing

and lose any partially
edited value if the editor is editing when this method is called.

Returns the component that should be added to the client's

Component

hierarchy. Once installed in the client's
hierarchy this component will then be able to draw and receive
user input.

**Parameters:**
- table

- the

JTable

that is asking the
editor to edit; can be

null
- value

- the value of the cell to be edited; it is
up to the specific editor to interpret
and draw the value. For example, if value is
the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a valid value
- isSelected

- true if the cell is to be rendered with
highlighting
- row

- the row of the cell being edited
- column

- the column of the cell being edited

**Returns:**
- the component for editing

---

### Additional Sections

#### Interface TableCellEditor

**All Superinterfaces:** CellEditor

**All Known Implementing Classes:** DefaultCellEditor

```java
public interface
TableCellEditor

extends
CellEditor
```

This interface defines the method any object that would like to be
an editor of values for components such as

JListBox

,

JComboBox

,

JTree

, or

JTable

needs to implement.

public interface

TableCellEditor

extends

CellEditor

This interface defines the method any object that would like to be
an editor of values for components such as

JListBox

,

JComboBox

,

JTree

, or

JTable

needs to implement.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getTableCellEditorComponent

​(

JTable

table,

Object

value,
boolean isSelected,
int row,
int column)

Sets an initial

value

for the editor.

- Methods declared in interface javax.swing.

CellEditor

addCellEditorListener

,

cancelCellEditing

,

getCellEditorValue

,

isCellEditable

,

removeCellEditorListener

,

shouldSelectCell

,

stopCellEditing

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getTableCellEditorComponent

​(

JTable

table,

Object

value,
boolean isSelected,
int row,
int column)

Sets an initial

value

for the editor.

- Methods declared in interface javax.swing.

CellEditor

addCellEditorListener

,

cancelCellEditing

,

getCellEditorValue

,

isCellEditable

,

removeCellEditorListener

,

shouldSelectCell

,

stopCellEditing

---

#### Method Summary

Sets an initial

value

for the editor.

Methods declared in interface javax.swing.

CellEditor

addCellEditorListener

,

cancelCellEditing

,

getCellEditorValue

,

isCellEditable

,

removeCellEditorListener

,

shouldSelectCell

,

stopCellEditing

---

#### Methods declared in interface javax.swing. CellEditor

============ METHOD DETAIL ==========

- Method Detail

- getTableCellEditorComponent

```java
Component
getTableCellEditorComponent​(
JTable
table,

Object
value,
boolean isSelected,
int row,
int column)
```

Sets an initial

value

for the editor. This will cause
the editor to

stopEditing

and lose any partially
edited value if the editor is editing when this method is called.

Returns the component that should be added to the client's

Component

hierarchy. Once installed in the client's
hierarchy this component will then be able to draw and receive
user input.

**Parameters:** table

- the

JTable

that is asking the
editor to edit; can be

null
**Parameters:** value

- the value of the cell to be edited; it is
up to the specific editor to interpret
and draw the value. For example, if value is
the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a valid value
**Parameters:** isSelected

- true if the cell is to be rendered with
highlighting
**Parameters:** row

- the row of the cell being edited
**Parameters:** column

- the column of the cell being edited
**Returns:** the component for editing

Method Detail

- getTableCellEditorComponent

```java
Component
getTableCellEditorComponent​(
JTable
table,

Object
value,
boolean isSelected,
int row,
int column)
```

Sets an initial

value

for the editor. This will cause
the editor to

stopEditing

and lose any partially
edited value if the editor is editing when this method is called.

Returns the component that should be added to the client's

Component

hierarchy. Once installed in the client's
hierarchy this component will then be able to draw and receive
user input.

**Parameters:** table

- the

JTable

that is asking the
editor to edit; can be

null
**Parameters:** value

- the value of the cell to be edited; it is
up to the specific editor to interpret
and draw the value. For example, if value is
the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a valid value
**Parameters:** isSelected

- true if the cell is to be rendered with
highlighting
**Parameters:** row

- the row of the cell being edited
**Parameters:** column

- the column of the cell being edited
**Returns:** the component for editing

---

#### Method Detail

getTableCellEditorComponent

```java
Component
getTableCellEditorComponent​(
JTable
table,

Object
value,
boolean isSelected,
int row,
int column)
```

Sets an initial

value

for the editor. This will cause
the editor to

stopEditing

and lose any partially
edited value if the editor is editing when this method is called.

Returns the component that should be added to the client's

Component

hierarchy. Once installed in the client's
hierarchy this component will then be able to draw and receive
user input.

**Parameters:** table

- the

JTable

that is asking the
editor to edit; can be

null
**Parameters:** value

- the value of the cell to be edited; it is
up to the specific editor to interpret
and draw the value. For example, if value is
the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a valid value
**Parameters:** isSelected

- true if the cell is to be rendered with
highlighting
**Parameters:** row

- the row of the cell being edited
**Parameters:** column

- the column of the cell being edited
**Returns:** the component for editing

---

#### getTableCellEditorComponent

Component

getTableCellEditorComponent​(

JTable

table,

Object

value,
boolean isSelected,
int row,
int column)

Sets an initial

value

for the editor. This will cause
the editor to

stopEditing

and lose any partially
edited value if the editor is editing when this method is called.

Returns the component that should be added to the client's

Component

hierarchy. Once installed in the client's
hierarchy this component will then be able to draw and receive
user input.

Returns the component that should be added to the client's

Component

hierarchy. Once installed in the client's
hierarchy this component will then be able to draw and receive
user input.

---

