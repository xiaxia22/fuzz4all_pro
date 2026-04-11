# Class DefaultCellEditor

**Source:** `java.desktop\javax\swing\DefaultCellEditor.html`

### Class Description

```java
public class
DefaultCellEditor

extends
AbstractCellEditor

implements
TableCellEditor
,
TreeCellEditor
```

The default editor for table and tree cells.

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

CellEditor

,

TableCellEditor

,

TreeCellEditor

---

### Field Details

#### protected
JComponent
editorComponent

The Swing component being edited.

---

#### protected
DefaultCellEditor.EditorDelegate
delegate

The delegate class which handles all methods sent from the

CellEditor

.

---

#### protected int clickCountToStart

An integer specifying the number of clicks needed to start editing.
Even if

clickCountToStart

is defined as zero, it
will not initiate until a click occurs.

---

### Constructor Details

#### @ConstructorProperties
("component")
public DefaultCellEditor​(
JTextField
textField)

Constructs a

DefaultCellEditor

that uses a text field.

**Parameters:**
- textField

- a

JTextField

object

---

#### public DefaultCellEditor​(
JCheckBox
checkBox)

Constructs a

DefaultCellEditor

object that uses a check box.

**Parameters:**
- checkBox

- a

JCheckBox

object

---

#### public DefaultCellEditor​(
JComboBox
<?> comboBox)

Constructs a

DefaultCellEditor

object that uses a
combo box.

**Parameters:**
- comboBox

- a

JComboBox

object

---

### Method Details

#### public
Component
getComponent()

Returns a reference to the editor component.

**Returns:**
- the editor

Component

---

#### public void setClickCountToStart​(int count)

Specifies the number of clicks needed to start editing.

**Parameters:**
- count

- an int specifying the number of clicks needed to start editing

**See Also:**
- getClickCountToStart()

---

#### public int getClickCountToStart()

Returns the number of clicks needed to start editing.

**Returns:**
- the number of clicks needed to start editing

---

#### public
Object
getCellEditorValue()

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:**
- getCellEditorValue

in interface

CellEditor

**Returns:**
- the value contained in the editor

**See Also:**
- DefaultCellEditor.EditorDelegate.getCellEditorValue()

---

#### public boolean isCellEditable​(
EventObject
anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:**
- isCellEditable

in interface

CellEditor

**Overrides:**
- isCellEditable

in class

AbstractCellEditor

**Parameters:**
- anEvent

- an event object

**Returns:**
- true

**See Also:**
- DefaultCellEditor.EditorDelegate.isCellEditable(EventObject)

---

#### public boolean shouldSelectCell​(
EventObject
anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:**
- shouldSelectCell

in interface

CellEditor

**Overrides:**
- shouldSelectCell

in class

AbstractCellEditor

**Parameters:**
- anEvent

- an event object

**Returns:**
- true

**See Also:**
- DefaultCellEditor.EditorDelegate.shouldSelectCell(EventObject)

---

#### public boolean stopCellEditing()

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:**
- stopCellEditing

in interface

CellEditor

**Overrides:**
- stopCellEditing

in class

AbstractCellEditor

**Returns:**
- true

**See Also:**
- DefaultCellEditor.EditorDelegate.stopCellEditing()

---

#### public void cancelCellEditing()

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:**
- cancelCellEditing

in interface

CellEditor

**Overrides:**
- cancelCellEditing

in class

AbstractCellEditor

**See Also:**
- DefaultCellEditor.EditorDelegate.cancelCellEditing()

---

#### public
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

Implements the

TreeCellEditor

interface.

**Specified by:**
- getTreeCellEditorComponent

in interface

TreeCellEditor

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

#### public
Component
getTableCellEditorComponent​(
JTable
table,

Object
value,
boolean isSelected,
int row,
int column)

Implements the

TableCellEditor

interface.

**Specified by:**
- getTableCellEditorComponent

in interface

TableCellEditor

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

#### Class DefaultCellEditor

java.lang.Object

- javax.swing.AbstractCellEditor
- - javax.swing.DefaultCellEditor

javax.swing.AbstractCellEditor

- javax.swing.DefaultCellEditor

javax.swing.DefaultCellEditor

**All Implemented Interfaces:** Serializable

,

CellEditor

,

TableCellEditor

,

TreeCellEditor

```java
public class
DefaultCellEditor

extends
AbstractCellEditor

implements
TableCellEditor
,
TreeCellEditor
```

The default editor for table and tree cells.

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

**Since:** 1.2
**See Also:** Serialized Form

public class

DefaultCellEditor

extends

AbstractCellEditor

implements

TableCellEditor

,

TreeCellEditor

The default editor for table and tree cells.

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

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

DefaultCellEditor.EditorDelegate

The protected

EditorDelegate

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

clickCountToStart

An integer specifying the number of clicks needed to start editing.

protected

DefaultCellEditor.EditorDelegate

delegate

The delegate class which handles all methods sent from the

CellEditor

.

protected

JComponent

editorComponent

The Swing component being edited.

- Fields declared in class javax.swing.

AbstractCellEditor

changeEvent

,

listenerList

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultCellEditor

​(

JCheckBox

checkBox)

Constructs a

DefaultCellEditor

object that uses a check box.

DefaultCellEditor

​(

JComboBox

<?> comboBox)

Constructs a

DefaultCellEditor

object that uses a
combo box.

DefaultCellEditor

​(

JTextField

textField)

Constructs a

DefaultCellEditor

that uses a text field.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

cancelCellEditing

()

Forwards the message from the

CellEditor

to
the

delegate

.

Object

getCellEditorValue

()

Forwards the message from the

CellEditor

to
the

delegate

.

int

getClickCountToStart

()

Returns the number of clicks needed to start editing.

Component

getComponent

()

Returns a reference to the editor component.

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

Implements the

TableCellEditor

interface.

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

Implements the

TreeCellEditor

interface.

boolean

isCellEditable

​(

EventObject

anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

void

setClickCountToStart

​(int count)

Specifies the number of clicks needed to start editing.

boolean

shouldSelectCell

​(

EventObject

anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

boolean

stopCellEditing

()

Forwards the message from the

CellEditor

to
the

delegate

.

- Methods declared in class javax.swing.

AbstractCellEditor

addCellEditorListener

,

fireEditingCanceled

,

fireEditingStopped

,

getCellEditorListeners

,

removeCellEditorListener

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

- Methods declared in interface javax.swing.

CellEditor

addCellEditorListener

,

removeCellEditorListener

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

DefaultCellEditor.EditorDelegate

The protected

EditorDelegate

class.

---

#### Nested Class Summary

The protected

EditorDelegate

class.

Field Summary

Fields

Modifier and Type

Field

Description

protected int

clickCountToStart

An integer specifying the number of clicks needed to start editing.

protected

DefaultCellEditor.EditorDelegate

delegate

The delegate class which handles all methods sent from the

CellEditor

.

protected

JComponent

editorComponent

The Swing component being edited.

- Fields declared in class javax.swing.

AbstractCellEditor

changeEvent

,

listenerList

---

#### Field Summary

An integer specifying the number of clicks needed to start editing.

The delegate class which handles all methods sent from the

CellEditor

.

The Swing component being edited.

Fields declared in class javax.swing.

AbstractCellEditor

changeEvent

,

listenerList

---

#### Fields declared in class javax.swing. AbstractCellEditor

Constructor Summary

Constructors

Constructor

Description

DefaultCellEditor

​(

JCheckBox

checkBox)

Constructs a

DefaultCellEditor

object that uses a check box.

DefaultCellEditor

​(

JComboBox

<?> comboBox)

Constructs a

DefaultCellEditor

object that uses a
combo box.

DefaultCellEditor

​(

JTextField

textField)

Constructs a

DefaultCellEditor

that uses a text field.

---

#### Constructor Summary

Constructs a

DefaultCellEditor

object that uses a check box.

Constructs a

DefaultCellEditor

object that uses a
combo box.

Constructs a

DefaultCellEditor

that uses a text field.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

cancelCellEditing

()

Forwards the message from the

CellEditor

to
the

delegate

.

Object

getCellEditorValue

()

Forwards the message from the

CellEditor

to
the

delegate

.

int

getClickCountToStart

()

Returns the number of clicks needed to start editing.

Component

getComponent

()

Returns a reference to the editor component.

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

Implements the

TableCellEditor

interface.

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

Implements the

TreeCellEditor

interface.

boolean

isCellEditable

​(

EventObject

anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

void

setClickCountToStart

​(int count)

Specifies the number of clicks needed to start editing.

boolean

shouldSelectCell

​(

EventObject

anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

boolean

stopCellEditing

()

Forwards the message from the

CellEditor

to
the

delegate

.

- Methods declared in class javax.swing.

AbstractCellEditor

addCellEditorListener

,

fireEditingCanceled

,

fireEditingStopped

,

getCellEditorListeners

,

removeCellEditorListener

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

- Methods declared in interface javax.swing.

CellEditor

addCellEditorListener

,

removeCellEditorListener

---

#### Method Summary

Forwards the message from the

CellEditor

to
the

delegate

.

Returns the number of clicks needed to start editing.

Returns a reference to the editor component.

Implements the

TableCellEditor

interface.

Implements the

TreeCellEditor

interface.

Specifies the number of clicks needed to start editing.

Methods declared in class javax.swing.

AbstractCellEditor

addCellEditorListener

,

fireEditingCanceled

,

fireEditingStopped

,

getCellEditorListeners

,

removeCellEditorListener

---

#### Methods declared in class javax.swing. AbstractCellEditor

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

Methods declared in interface javax.swing.

CellEditor

addCellEditorListener

,

removeCellEditorListener

---

#### Methods declared in interface javax.swing. CellEditor

============ FIELD DETAIL ===========

- Field Detail

- editorComponent

```java
protected
JComponent
editorComponent
```

The Swing component being edited.

- delegate

```java
protected
DefaultCellEditor.EditorDelegate
delegate
```

The delegate class which handles all methods sent from the

CellEditor

.

- clickCountToStart

```java
protected int clickCountToStart
```

An integer specifying the number of clicks needed to start editing.
Even if

clickCountToStart

is defined as zero, it
will not initiate until a click occurs.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultCellEditor

```java
@ConstructorProperties
("component")
public DefaultCellEditor​(
JTextField
textField)
```

Constructs a

DefaultCellEditor

that uses a text field.

**Parameters:** textField

- a

JTextField

object

- DefaultCellEditor

```java
public DefaultCellEditor​(
JCheckBox
checkBox)
```

Constructs a

DefaultCellEditor

object that uses a check box.

**Parameters:** checkBox

- a

JCheckBox

object

- DefaultCellEditor

```java
public DefaultCellEditor​(
JComboBox
<?> comboBox)
```

Constructs a

DefaultCellEditor

object that uses a
combo box.

**Parameters:** comboBox

- a

JComboBox

object

============ METHOD DETAIL ==========

- Method Detail

- getComponent

```java
public
Component
getComponent()
```

Returns a reference to the editor component.

**Returns:** the editor

Component

- setClickCountToStart

```java
public void setClickCountToStart​(int count)
```

Specifies the number of clicks needed to start editing.

**Parameters:** count

- an int specifying the number of clicks needed to start editing
**See Also:** getClickCountToStart()

- getClickCountToStart

```java
public int getClickCountToStart()
```

Returns the number of clicks needed to start editing.

**Returns:** the number of clicks needed to start editing

- getCellEditorValue

```java
public
Object
getCellEditorValue()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** getCellEditorValue

in interface

CellEditor
**Returns:** the value contained in the editor
**See Also:** DefaultCellEditor.EditorDelegate.getCellEditorValue()

- isCellEditable

```java
public boolean isCellEditable​(
EventObject
anEvent)
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** isCellEditable

in interface

CellEditor
**Overrides:** isCellEditable

in class

AbstractCellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.isCellEditable(EventObject)

- shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
anEvent)
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Overrides:** shouldSelectCell

in class

AbstractCellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.shouldSelectCell(EventObject)

- stopCellEditing

```java
public boolean stopCellEditing()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** stopCellEditing

in interface

CellEditor
**Overrides:** stopCellEditing

in class

AbstractCellEditor
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.stopCellEditing()

- cancelCellEditing

```java
public void cancelCellEditing()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** cancelCellEditing

in interface

CellEditor
**Overrides:** cancelCellEditing

in class

AbstractCellEditor
**See Also:** DefaultCellEditor.EditorDelegate.cancelCellEditing()

- getTreeCellEditorComponent

```java
public
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

Implements the

TreeCellEditor

interface.

**Specified by:** getTreeCellEditorComponent

in interface

TreeCellEditor
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

- getTableCellEditorComponent

```java
public
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

Implements the

TableCellEditor

interface.

**Specified by:** getTableCellEditorComponent

in interface

TableCellEditor
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

Field Detail

- editorComponent

```java
protected
JComponent
editorComponent
```

The Swing component being edited.

- delegate

```java
protected
DefaultCellEditor.EditorDelegate
delegate
```

The delegate class which handles all methods sent from the

CellEditor

.

- clickCountToStart

```java
protected int clickCountToStart
```

An integer specifying the number of clicks needed to start editing.
Even if

clickCountToStart

is defined as zero, it
will not initiate until a click occurs.

---

#### Field Detail

editorComponent

```java
protected
JComponent
editorComponent
```

The Swing component being edited.

---

#### editorComponent

protected

JComponent

editorComponent

The Swing component being edited.

delegate

```java
protected
DefaultCellEditor.EditorDelegate
delegate
```

The delegate class which handles all methods sent from the

CellEditor

.

---

#### delegate

protected

DefaultCellEditor.EditorDelegate

delegate

The delegate class which handles all methods sent from the

CellEditor

.

clickCountToStart

```java
protected int clickCountToStart
```

An integer specifying the number of clicks needed to start editing.
Even if

clickCountToStart

is defined as zero, it
will not initiate until a click occurs.

---

#### clickCountToStart

protected int clickCountToStart

An integer specifying the number of clicks needed to start editing.
Even if

clickCountToStart

is defined as zero, it
will not initiate until a click occurs.

Constructor Detail

- DefaultCellEditor

```java
@ConstructorProperties
("component")
public DefaultCellEditor​(
JTextField
textField)
```

Constructs a

DefaultCellEditor

that uses a text field.

**Parameters:** textField

- a

JTextField

object

- DefaultCellEditor

```java
public DefaultCellEditor​(
JCheckBox
checkBox)
```

Constructs a

DefaultCellEditor

object that uses a check box.

**Parameters:** checkBox

- a

JCheckBox

object

- DefaultCellEditor

```java
public DefaultCellEditor​(
JComboBox
<?> comboBox)
```

Constructs a

DefaultCellEditor

object that uses a
combo box.

**Parameters:** comboBox

- a

JComboBox

object

---

#### Constructor Detail

DefaultCellEditor

```java
@ConstructorProperties
("component")
public DefaultCellEditor​(
JTextField
textField)
```

Constructs a

DefaultCellEditor

that uses a text field.

**Parameters:** textField

- a

JTextField

object

---

#### DefaultCellEditor

@ConstructorProperties

("component")
public DefaultCellEditor​(

JTextField

textField)

Constructs a

DefaultCellEditor

that uses a text field.

DefaultCellEditor

```java
public DefaultCellEditor​(
JCheckBox
checkBox)
```

Constructs a

DefaultCellEditor

object that uses a check box.

**Parameters:** checkBox

- a

JCheckBox

object

---

#### DefaultCellEditor

public DefaultCellEditor​(

JCheckBox

checkBox)

Constructs a

DefaultCellEditor

object that uses a check box.

DefaultCellEditor

```java
public DefaultCellEditor​(
JComboBox
<?> comboBox)
```

Constructs a

DefaultCellEditor

object that uses a
combo box.

**Parameters:** comboBox

- a

JComboBox

object

---

#### DefaultCellEditor

public DefaultCellEditor​(

JComboBox

<?> comboBox)

Constructs a

DefaultCellEditor

object that uses a
combo box.

Method Detail

- getComponent

```java
public
Component
getComponent()
```

Returns a reference to the editor component.

**Returns:** the editor

Component

- setClickCountToStart

```java
public void setClickCountToStart​(int count)
```

Specifies the number of clicks needed to start editing.

**Parameters:** count

- an int specifying the number of clicks needed to start editing
**See Also:** getClickCountToStart()

- getClickCountToStart

```java
public int getClickCountToStart()
```

Returns the number of clicks needed to start editing.

**Returns:** the number of clicks needed to start editing

- getCellEditorValue

```java
public
Object
getCellEditorValue()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** getCellEditorValue

in interface

CellEditor
**Returns:** the value contained in the editor
**See Also:** DefaultCellEditor.EditorDelegate.getCellEditorValue()

- isCellEditable

```java
public boolean isCellEditable​(
EventObject
anEvent)
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** isCellEditable

in interface

CellEditor
**Overrides:** isCellEditable

in class

AbstractCellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.isCellEditable(EventObject)

- shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
anEvent)
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Overrides:** shouldSelectCell

in class

AbstractCellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.shouldSelectCell(EventObject)

- stopCellEditing

```java
public boolean stopCellEditing()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** stopCellEditing

in interface

CellEditor
**Overrides:** stopCellEditing

in class

AbstractCellEditor
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.stopCellEditing()

- cancelCellEditing

```java
public void cancelCellEditing()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** cancelCellEditing

in interface

CellEditor
**Overrides:** cancelCellEditing

in class

AbstractCellEditor
**See Also:** DefaultCellEditor.EditorDelegate.cancelCellEditing()

- getTreeCellEditorComponent

```java
public
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

Implements the

TreeCellEditor

interface.

**Specified by:** getTreeCellEditorComponent

in interface

TreeCellEditor
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

- getTableCellEditorComponent

```java
public
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

Implements the

TableCellEditor

interface.

**Specified by:** getTableCellEditorComponent

in interface

TableCellEditor
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

getComponent

```java
public
Component
getComponent()
```

Returns a reference to the editor component.

**Returns:** the editor

Component

---

#### getComponent

public

Component

getComponent()

Returns a reference to the editor component.

setClickCountToStart

```java
public void setClickCountToStart​(int count)
```

Specifies the number of clicks needed to start editing.

**Parameters:** count

- an int specifying the number of clicks needed to start editing
**See Also:** getClickCountToStart()

---

#### setClickCountToStart

public void setClickCountToStart​(int count)

Specifies the number of clicks needed to start editing.

getClickCountToStart

```java
public int getClickCountToStart()
```

Returns the number of clicks needed to start editing.

**Returns:** the number of clicks needed to start editing

---

#### getClickCountToStart

public int getClickCountToStart()

Returns the number of clicks needed to start editing.

getCellEditorValue

```java
public
Object
getCellEditorValue()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** getCellEditorValue

in interface

CellEditor
**Returns:** the value contained in the editor
**See Also:** DefaultCellEditor.EditorDelegate.getCellEditorValue()

---

#### getCellEditorValue

public

Object

getCellEditorValue()

Forwards the message from the

CellEditor

to
the

delegate

.

isCellEditable

```java
public boolean isCellEditable​(
EventObject
anEvent)
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** isCellEditable

in interface

CellEditor
**Overrides:** isCellEditable

in class

AbstractCellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.isCellEditable(EventObject)

---

#### isCellEditable

public boolean isCellEditable​(

EventObject

anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
anEvent)
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Overrides:** shouldSelectCell

in class

AbstractCellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.shouldSelectCell(EventObject)

---

#### shouldSelectCell

public boolean shouldSelectCell​(

EventObject

anEvent)

Forwards the message from the

CellEditor

to
the

delegate

.

stopCellEditing

```java
public boolean stopCellEditing()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** stopCellEditing

in interface

CellEditor
**Overrides:** stopCellEditing

in class

AbstractCellEditor
**Returns:** true
**See Also:** DefaultCellEditor.EditorDelegate.stopCellEditing()

---

#### stopCellEditing

public boolean stopCellEditing()

Forwards the message from the

CellEditor

to
the

delegate

.

cancelCellEditing

```java
public void cancelCellEditing()
```

Forwards the message from the

CellEditor

to
the

delegate

.

**Specified by:** cancelCellEditing

in interface

CellEditor
**Overrides:** cancelCellEditing

in class

AbstractCellEditor
**See Also:** DefaultCellEditor.EditorDelegate.cancelCellEditing()

---

#### cancelCellEditing

public void cancelCellEditing()

Forwards the message from the

CellEditor

to
the

delegate

.

getTreeCellEditorComponent

```java
public
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

Implements the

TreeCellEditor

interface.

**Specified by:** getTreeCellEditorComponent

in interface

TreeCellEditor
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

public

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

Implements the

TreeCellEditor

interface.

getTableCellEditorComponent

```java
public
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

Implements the

TableCellEditor

interface.

**Specified by:** getTableCellEditorComponent

in interface

TableCellEditor
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

public

Component

getTableCellEditorComponent​(

JTable

table,

Object

value,
boolean isSelected,
int row,
int column)

Implements the

TableCellEditor

interface.

---

