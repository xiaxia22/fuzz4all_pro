# Interface TableCellRenderer

**Source:** `java.desktop\javax\swing\table\TableCellRenderer.html`

### Class Description

```java
public interface
TableCellRenderer
```

This interface defines the method required by any object that
would like to be a renderer for cells in a

JTable

.

**All Known Implementing Classes:** DefaultTableCellRenderer

,

DefaultTableCellRenderer.UIResource

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the component used for drawing the cell. This method is
used to configure the renderer appropriately before drawing.

The

TableCellRenderer

is also responsible for rendering the
the cell representing the table's current DnD drop location if
it has one. If this renderer cares about rendering
the DnD drop location, it should query the table directly to
see if the given row and column represent the drop location:

```java
JTable.DropLocation dropLocation = table.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsertRow()
&& !dropLocation.isInsertColumn()
&& dropLocation.getRow() == row
&& dropLocation.getColumn() == column) {

// this cell represents the current drop location
// so render it specially, perhaps with a different color
}
```

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Parameters:**
- table

- the

JTable

that is asking the
renderer to draw; can be

null
- value

- the value of the cell to be rendered. It is
up to the specific renderer to interpret
and draw the value. For example, if

value

is the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a
valid value
- isSelected

- true if the cell is to be rendered with the
selection highlighted; otherwise false
- hasFocus

- if true, render cell appropriately. For
example, put a special border on the cell, if
the cell can be edited, render in the color used
to indicate editing
- row

- the row index of the cell being drawn. When
drawing the header, the value of

row

is -1
- column

- the column index of the cell being drawn

**Returns:**
- the component used for drawing the cell.

**See Also:**
- JComponent.isPaintingForPrint()

---

### Additional Sections

#### Interface TableCellRenderer

**All Known Implementing Classes:** DefaultTableCellRenderer

,

DefaultTableCellRenderer.UIResource

```java
public interface
TableCellRenderer
```

This interface defines the method required by any object that
would like to be a renderer for cells in a

JTable

.

public interface

TableCellRenderer

This interface defines the method required by any object that
would like to be a renderer for cells in a

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

Component

getTableCellRendererComponent

​(

JTable

table,

Object

value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the component used for drawing the cell.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getTableCellRendererComponent

​(

JTable

table,

Object

value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the component used for drawing the cell.

---

#### Method Summary

Returns the component used for drawing the cell.

============ METHOD DETAIL ==========

- Method Detail

- getTableCellRendererComponent

```java
Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)
```

Returns the component used for drawing the cell. This method is
used to configure the renderer appropriately before drawing.

The

TableCellRenderer

is also responsible for rendering the
the cell representing the table's current DnD drop location if
it has one. If this renderer cares about rendering
the DnD drop location, it should query the table directly to
see if the given row and column represent the drop location:

```java
JTable.DropLocation dropLocation = table.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsertRow()
&& !dropLocation.isInsertColumn()
&& dropLocation.getRow() == row
&& dropLocation.getColumn() == column) {

// this cell represents the current drop location
// so render it specially, perhaps with a different color
}
```

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Parameters:** table

- the

JTable

that is asking the
renderer to draw; can be

null
**Parameters:** value

- the value of the cell to be rendered. It is
up to the specific renderer to interpret
and draw the value. For example, if

value

is the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a
valid value
**Parameters:** isSelected

- true if the cell is to be rendered with the
selection highlighted; otherwise false
**Parameters:** hasFocus

- if true, render cell appropriately. For
example, put a special border on the cell, if
the cell can be edited, render in the color used
to indicate editing
**Parameters:** row

- the row index of the cell being drawn. When
drawing the header, the value of

row

is -1
**Parameters:** column

- the column index of the cell being drawn
**Returns:** the component used for drawing the cell.
**See Also:** JComponent.isPaintingForPrint()

Method Detail

- getTableCellRendererComponent

```java
Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)
```

Returns the component used for drawing the cell. This method is
used to configure the renderer appropriately before drawing.

The

TableCellRenderer

is also responsible for rendering the
the cell representing the table's current DnD drop location if
it has one. If this renderer cares about rendering
the DnD drop location, it should query the table directly to
see if the given row and column represent the drop location:

```java
JTable.DropLocation dropLocation = table.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsertRow()
&& !dropLocation.isInsertColumn()
&& dropLocation.getRow() == row
&& dropLocation.getColumn() == column) {

// this cell represents the current drop location
// so render it specially, perhaps with a different color
}
```

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Parameters:** table

- the

JTable

that is asking the
renderer to draw; can be

null
**Parameters:** value

- the value of the cell to be rendered. It is
up to the specific renderer to interpret
and draw the value. For example, if

value

is the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a
valid value
**Parameters:** isSelected

- true if the cell is to be rendered with the
selection highlighted; otherwise false
**Parameters:** hasFocus

- if true, render cell appropriately. For
example, put a special border on the cell, if
the cell can be edited, render in the color used
to indicate editing
**Parameters:** row

- the row index of the cell being drawn. When
drawing the header, the value of

row

is -1
**Parameters:** column

- the column index of the cell being drawn
**Returns:** the component used for drawing the cell.
**See Also:** JComponent.isPaintingForPrint()

---

#### Method Detail

getTableCellRendererComponent

```java
Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)
```

Returns the component used for drawing the cell. This method is
used to configure the renderer appropriately before drawing.

The

TableCellRenderer

is also responsible for rendering the
the cell representing the table's current DnD drop location if
it has one. If this renderer cares about rendering
the DnD drop location, it should query the table directly to
see if the given row and column represent the drop location:

```java
JTable.DropLocation dropLocation = table.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsertRow()
&& !dropLocation.isInsertColumn()
&& dropLocation.getRow() == row
&& dropLocation.getColumn() == column) {

// this cell represents the current drop location
// so render it specially, perhaps with a different color
}
```

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Parameters:** table

- the

JTable

that is asking the
renderer to draw; can be

null
**Parameters:** value

- the value of the cell to be rendered. It is
up to the specific renderer to interpret
and draw the value. For example, if

value

is the string "true", it could be rendered as a
string or it could be rendered as a check
box that is checked.

null

is a
valid value
**Parameters:** isSelected

- true if the cell is to be rendered with the
selection highlighted; otherwise false
**Parameters:** hasFocus

- if true, render cell appropriately. For
example, put a special border on the cell, if
the cell can be edited, render in the color used
to indicate editing
**Parameters:** row

- the row index of the cell being drawn. When
drawing the header, the value of

row

is -1
**Parameters:** column

- the column index of the cell being drawn
**Returns:** the component used for drawing the cell.
**See Also:** JComponent.isPaintingForPrint()

---

#### getTableCellRendererComponent

Component

getTableCellRendererComponent​(

JTable

table,

Object

value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the component used for drawing the cell. This method is
used to configure the renderer appropriately before drawing.

The

TableCellRenderer

is also responsible for rendering the
the cell representing the table's current DnD drop location if
it has one. If this renderer cares about rendering
the DnD drop location, it should query the table directly to
see if the given row and column represent the drop location:

```java
JTable.DropLocation dropLocation = table.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsertRow()
&& !dropLocation.isInsertColumn()
&& dropLocation.getRow() == row
&& dropLocation.getColumn() == column) {

// this cell represents the current drop location
// so render it specially, perhaps with a different color
}
```

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

The

TableCellRenderer

is also responsible for rendering the
the cell representing the table's current DnD drop location if
it has one. If this renderer cares about rendering
the DnD drop location, it should query the table directly to
see if the given row and column represent the drop location:

```java
JTable.DropLocation dropLocation = table.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsertRow()
&& !dropLocation.isInsertColumn()
&& dropLocation.getRow() == row
&& dropLocation.getColumn() == column) {

// this cell represents the current drop location
// so render it specially, perhaps with a different color
}
```

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

JTable.DropLocation dropLocation = table.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsertRow()
&& !dropLocation.isInsertColumn()
&& dropLocation.getRow() == row
&& dropLocation.getColumn() == column) {

// this cell represents the current drop location
// so render it specially, perhaps with a different color
}

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

---

