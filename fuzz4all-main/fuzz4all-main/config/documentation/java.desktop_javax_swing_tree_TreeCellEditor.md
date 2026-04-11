# Interface TreeCellEditor

**Source:** `java.desktop\javax\swing\tree\TreeCellEditor.html`

### Class Description

```java
public interface
TreeCellEditor

extends
CellEditor
```

Adds to CellEditor the extensions necessary to configure an editor
in a tree.

**All Superinterfaces:** CellEditor

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Sets an initial

value

for the editor. This will cause
the editor to stopEditing and lose any partially edited value
if the editor is editing when this method is called.

Returns the component that should be added to the client's
Component hierarchy. Once installed in the client's hierarchy
this component will then be able to draw and receive user input.

**Parameters:**
- tree

- the JTree that is asking the editor to edit;
this parameter can be null
- value

- the value of the cell to be edited
- isSelected

- true if the cell is to be rendered with
selection highlighting
- expanded

- true if the node is expanded
- leaf

- true if the node is a leaf node
- row

- the row index of the node being edited

**Returns:**
- the component for editing

---

### Additional Sections

#### Interface TreeCellEditor

**All Superinterfaces:** CellEditor

**All Known Implementing Classes:** DefaultCellEditor

,

DefaultTreeCellEditor

```java
public interface
TreeCellEditor

extends
CellEditor
```

Adds to CellEditor the extensions necessary to configure an editor
in a tree.

**See Also:** JTree

public interface

TreeCellEditor

extends

CellEditor

Adds to CellEditor the extensions necessary to configure an editor
in a tree.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getTreeCellEditorComponent

​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

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

getTreeCellEditorComponent

​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

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

- getTreeCellEditorComponent

```java
Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Sets an initial

value

for the editor. This will cause
the editor to stopEditing and lose any partially edited value
if the editor is editing when this method is called.

Returns the component that should be added to the client's
Component hierarchy. Once installed in the client's hierarchy
this component will then be able to draw and receive user input.

**Parameters:** tree

- the JTree that is asking the editor to edit;
this parameter can be null
**Parameters:** value

- the value of the cell to be edited
**Parameters:** isSelected

- true if the cell is to be rendered with
selection highlighting
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- the row index of the node being edited
**Returns:** the component for editing

Method Detail

- getTreeCellEditorComponent

```java
Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Sets an initial

value

for the editor. This will cause
the editor to stopEditing and lose any partially edited value
if the editor is editing when this method is called.

Returns the component that should be added to the client's
Component hierarchy. Once installed in the client's hierarchy
this component will then be able to draw and receive user input.

**Parameters:** tree

- the JTree that is asking the editor to edit;
this parameter can be null
**Parameters:** value

- the value of the cell to be edited
**Parameters:** isSelected

- true if the cell is to be rendered with
selection highlighting
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- the row index of the node being edited
**Returns:** the component for editing

---

#### Method Detail

getTreeCellEditorComponent

```java
Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Sets an initial

value

for the editor. This will cause
the editor to stopEditing and lose any partially edited value
if the editor is editing when this method is called.

Returns the component that should be added to the client's
Component hierarchy. Once installed in the client's hierarchy
this component will then be able to draw and receive user input.

**Parameters:** tree

- the JTree that is asking the editor to edit;
this parameter can be null
**Parameters:** value

- the value of the cell to be edited
**Parameters:** isSelected

- true if the cell is to be rendered with
selection highlighting
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- the row index of the node being edited
**Returns:** the component for editing

---

#### getTreeCellEditorComponent

Component

getTreeCellEditorComponent​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Sets an initial

value

for the editor. This will cause
the editor to stopEditing and lose any partially edited value
if the editor is editing when this method is called.

Returns the component that should be added to the client's
Component hierarchy. Once installed in the client's hierarchy
this component will then be able to draw and receive user input.

Returns the component that should be added to the client's
Component hierarchy. Once installed in the client's hierarchy
this component will then be able to draw and receive user input.

---

