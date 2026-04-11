# Interface CellEditor

**Source:** `java.desktop\javax\swing\CellEditor.html`

### Class Description

```java
public interface
CellEditor
```

This interface defines the methods any general editor should be able
to implement.

Having this interface enables complex components (the client of the
editor) such as

JTree

and

JTable

to allow any generic editor to
edit values in a table cell, or tree cell, etc. Without this generic
editor interface,

JTable

would have to know about specific editors,
such as

JTextField

,

JCheckBox

,

JComboBox

,
etc. In addition, without this interface, clients of editors such as

JTable

would not be able
to work with any editors developed in the future by the user
or a 3rd party ISV.

To use this interface, a developer creating a new editor can have the
new component implement the interface. Or the developer can
choose a wrapper based approach and provide a companion object which
implements the

CellEditor

interface (See

DefaultCellEditor

for example). The wrapper approach
is particularly useful if the user want to use a 3rd party ISV
editor with

JTable

, but the ISV didn't implement the

CellEditor

interface. The user can simply create an object
that contains an instance of the 3rd party editor object and "translate"
the

CellEditor

API into the 3rd party editor's API.

**All Known Subinterfaces:** TableCellEditor

,

TreeCellEditor

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
getCellEditorValue()

Returns the value contained in the editor.

**Returns:**
- the value contained in the editor

---

#### boolean isCellEditable​(
EventObject
anEvent)

Asks the editor if it can start editing using

anEvent

.

anEvent

is in the invoking component coordinate system.
The editor can not assume the Component returned by

getCellEditorComponent

is installed. This method
is intended for the use of client to avoid the cost of setting up
and installing the editor component if editing is not possible.
If editing can be started this method returns true.

**Parameters:**
- anEvent

- the event the editor should use to consider
whether to begin editing or not

**Returns:**
- true if editing can be started

**See Also:**
- shouldSelectCell(java.util.EventObject)

---

#### boolean shouldSelectCell​(
EventObject
anEvent)

Returns true if the editing cell should be selected, false otherwise.
Typically, the return value is true, because is most cases the editing
cell should be selected. However, it is useful to return false to
keep the selection from changing for some types of edits.
eg. A table that contains a column of check boxes, the user might
want to be able to change those checkboxes without altering the
selection. (See Netscape Communicator for just such an example)
Of course, it is up to the client of the editor to use the return
value, but it doesn't need to if it doesn't want to.

**Parameters:**
- anEvent

- the event the editor should use to start
editing

**Returns:**
- true if the editor would like the editing cell to be selected;
otherwise returns false

**See Also:**
- isCellEditable(java.util.EventObject)

---

#### boolean stopCellEditing()

Tells the editor to stop editing and accept any partially edited
value as the value of the editor. The editor returns false if
editing was not stopped; this is useful for editors that validate
and can not accept invalid entries.

**Returns:**
- true if editing was stopped; false otherwise

---

#### void cancelCellEditing()

Tells the editor to cancel editing and not accept any partially
edited value.

---

#### void addCellEditorListener​(
CellEditorListener
l)

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

**Parameters:**
- l

- the CellEditorListener

---

#### void removeCellEditorListener​(
CellEditorListener
l)

Removes a listener from the list that's notified

**Parameters:**
- l

- the CellEditorListener

---

### Additional Sections

#### Interface CellEditor

**All Known Subinterfaces:** TableCellEditor

,

TreeCellEditor

**All Known Implementing Classes:** AbstractCellEditor

,

DefaultCellEditor

,

DefaultTreeCellEditor

```java
public interface
CellEditor
```

This interface defines the methods any general editor should be able
to implement.

Having this interface enables complex components (the client of the
editor) such as

JTree

and

JTable

to allow any generic editor to
edit values in a table cell, or tree cell, etc. Without this generic
editor interface,

JTable

would have to know about specific editors,
such as

JTextField

,

JCheckBox

,

JComboBox

,
etc. In addition, without this interface, clients of editors such as

JTable

would not be able
to work with any editors developed in the future by the user
or a 3rd party ISV.

To use this interface, a developer creating a new editor can have the
new component implement the interface. Or the developer can
choose a wrapper based approach and provide a companion object which
implements the

CellEditor

interface (See

DefaultCellEditor

for example). The wrapper approach
is particularly useful if the user want to use a 3rd party ISV
editor with

JTable

, but the ISV didn't implement the

CellEditor

interface. The user can simply create an object
that contains an instance of the 3rd party editor object and "translate"
the

CellEditor

API into the 3rd party editor's API.

**Since:** 1.2
**See Also:** CellEditorListener

public interface

CellEditor

This interface defines the methods any general editor should be able
to implement.

Having this interface enables complex components (the client of the
editor) such as

JTree

and

JTable

to allow any generic editor to
edit values in a table cell, or tree cell, etc. Without this generic
editor interface,

JTable

would have to know about specific editors,
such as

JTextField

,

JCheckBox

,

JComboBox

,
etc. In addition, without this interface, clients of editors such as

JTable

would not be able
to work with any editors developed in the future by the user
or a 3rd party ISV.

To use this interface, a developer creating a new editor can have the
new component implement the interface. Or the developer can
choose a wrapper based approach and provide a companion object which
implements the

CellEditor

interface (See

DefaultCellEditor

for example). The wrapper approach
is particularly useful if the user want to use a 3rd party ISV
editor with

JTable

, but the ISV didn't implement the

CellEditor

interface. The user can simply create an object
that contains an instance of the 3rd party editor object and "translate"
the

CellEditor

API into the 3rd party editor's API.

Having this interface enables complex components (the client of the
editor) such as

JTree

and

JTable

to allow any generic editor to
edit values in a table cell, or tree cell, etc. Without this generic
editor interface,

JTable

would have to know about specific editors,
such as

JTextField

,

JCheckBox

,

JComboBox

,
etc. In addition, without this interface, clients of editors such as

JTable

would not be able
to work with any editors developed in the future by the user
or a 3rd party ISV.

To use this interface, a developer creating a new editor can have the
new component implement the interface. Or the developer can
choose a wrapper based approach and provide a companion object which
implements the

CellEditor

interface (See

DefaultCellEditor

for example). The wrapper approach
is particularly useful if the user want to use a 3rd party ISV
editor with

JTable

, but the ISV didn't implement the

CellEditor

interface. The user can simply create an object
that contains an instance of the 3rd party editor object and "translate"
the

CellEditor

API into the 3rd party editor's API.

To use this interface, a developer creating a new editor can have the
new component implement the interface. Or the developer can
choose a wrapper based approach and provide a companion object which
implements the

CellEditor

interface (See

DefaultCellEditor

for example). The wrapper approach
is particularly useful if the user want to use a 3rd party ISV
editor with

JTable

, but the ISV didn't implement the

CellEditor

interface. The user can simply create an object
that contains an instance of the 3rd party editor object and "translate"
the

CellEditor

API into the 3rd party editor's API.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addCellEditorListener

​(

CellEditorListener

l)

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

void

cancelCellEditing

()

Tells the editor to cancel editing and not accept any partially
edited value.

Object

getCellEditorValue

()

Returns the value contained in the editor.

boolean

isCellEditable

​(

EventObject

anEvent)

Asks the editor if it can start editing using

anEvent

.

void

removeCellEditorListener

​(

CellEditorListener

l)

Removes a listener from the list that's notified

boolean

shouldSelectCell

​(

EventObject

anEvent)

Returns true if the editing cell should be selected, false otherwise.

boolean

stopCellEditing

()

Tells the editor to stop editing and accept any partially edited
value as the value of the editor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addCellEditorListener

​(

CellEditorListener

l)

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

void

cancelCellEditing

()

Tells the editor to cancel editing and not accept any partially
edited value.

Object

getCellEditorValue

()

Returns the value contained in the editor.

boolean

isCellEditable

​(

EventObject

anEvent)

Asks the editor if it can start editing using

anEvent

.

void

removeCellEditorListener

​(

CellEditorListener

l)

Removes a listener from the list that's notified

boolean

shouldSelectCell

​(

EventObject

anEvent)

Returns true if the editing cell should be selected, false otherwise.

boolean

stopCellEditing

()

Tells the editor to stop editing and accept any partially edited
value as the value of the editor.

---

#### Method Summary

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

Tells the editor to cancel editing and not accept any partially
edited value.

Returns the value contained in the editor.

Asks the editor if it can start editing using

anEvent

.

Removes a listener from the list that's notified

Returns true if the editing cell should be selected, false otherwise.

Tells the editor to stop editing and accept any partially edited
value as the value of the editor.

============ METHOD DETAIL ==========

- Method Detail

- getCellEditorValue

```java
Object
getCellEditorValue()
```

Returns the value contained in the editor.

**Returns:** the value contained in the editor

- isCellEditable

```java
boolean isCellEditable​(
EventObject
anEvent)
```

Asks the editor if it can start editing using

anEvent

.

anEvent

is in the invoking component coordinate system.
The editor can not assume the Component returned by

getCellEditorComponent

is installed. This method
is intended for the use of client to avoid the cost of setting up
and installing the editor component if editing is not possible.
If editing can be started this method returns true.

**Parameters:** anEvent

- the event the editor should use to consider
whether to begin editing or not
**Returns:** true if editing can be started
**See Also:** shouldSelectCell(java.util.EventObject)

- shouldSelectCell

```java
boolean shouldSelectCell​(
EventObject
anEvent)
```

Returns true if the editing cell should be selected, false otherwise.
Typically, the return value is true, because is most cases the editing
cell should be selected. However, it is useful to return false to
keep the selection from changing for some types of edits.
eg. A table that contains a column of check boxes, the user might
want to be able to change those checkboxes without altering the
selection. (See Netscape Communicator for just such an example)
Of course, it is up to the client of the editor to use the return
value, but it doesn't need to if it doesn't want to.

**Parameters:** anEvent

- the event the editor should use to start
editing
**Returns:** true if the editor would like the editing cell to be selected;
otherwise returns false
**See Also:** isCellEditable(java.util.EventObject)

- stopCellEditing

```java
boolean stopCellEditing()
```

Tells the editor to stop editing and accept any partially edited
value as the value of the editor. The editor returns false if
editing was not stopped; this is useful for editors that validate
and can not accept invalid entries.

**Returns:** true if editing was stopped; false otherwise

- cancelCellEditing

```java
void cancelCellEditing()
```

Tells the editor to cancel editing and not accept any partially
edited value.

- addCellEditorListener

```java
void addCellEditorListener​(
CellEditorListener
l)
```

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

**Parameters:** l

- the CellEditorListener

- removeCellEditorListener

```java
void removeCellEditorListener​(
CellEditorListener
l)
```

Removes a listener from the list that's notified

**Parameters:** l

- the CellEditorListener

Method Detail

- getCellEditorValue

```java
Object
getCellEditorValue()
```

Returns the value contained in the editor.

**Returns:** the value contained in the editor

- isCellEditable

```java
boolean isCellEditable​(
EventObject
anEvent)
```

Asks the editor if it can start editing using

anEvent

.

anEvent

is in the invoking component coordinate system.
The editor can not assume the Component returned by

getCellEditorComponent

is installed. This method
is intended for the use of client to avoid the cost of setting up
and installing the editor component if editing is not possible.
If editing can be started this method returns true.

**Parameters:** anEvent

- the event the editor should use to consider
whether to begin editing or not
**Returns:** true if editing can be started
**See Also:** shouldSelectCell(java.util.EventObject)

- shouldSelectCell

```java
boolean shouldSelectCell​(
EventObject
anEvent)
```

Returns true if the editing cell should be selected, false otherwise.
Typically, the return value is true, because is most cases the editing
cell should be selected. However, it is useful to return false to
keep the selection from changing for some types of edits.
eg. A table that contains a column of check boxes, the user might
want to be able to change those checkboxes without altering the
selection. (See Netscape Communicator for just such an example)
Of course, it is up to the client of the editor to use the return
value, but it doesn't need to if it doesn't want to.

**Parameters:** anEvent

- the event the editor should use to start
editing
**Returns:** true if the editor would like the editing cell to be selected;
otherwise returns false
**See Also:** isCellEditable(java.util.EventObject)

- stopCellEditing

```java
boolean stopCellEditing()
```

Tells the editor to stop editing and accept any partially edited
value as the value of the editor. The editor returns false if
editing was not stopped; this is useful for editors that validate
and can not accept invalid entries.

**Returns:** true if editing was stopped; false otherwise

- cancelCellEditing

```java
void cancelCellEditing()
```

Tells the editor to cancel editing and not accept any partially
edited value.

- addCellEditorListener

```java
void addCellEditorListener​(
CellEditorListener
l)
```

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

**Parameters:** l

- the CellEditorListener

- removeCellEditorListener

```java
void removeCellEditorListener​(
CellEditorListener
l)
```

Removes a listener from the list that's notified

**Parameters:** l

- the CellEditorListener

---

#### Method Detail

getCellEditorValue

```java
Object
getCellEditorValue()
```

Returns the value contained in the editor.

**Returns:** the value contained in the editor

---

#### getCellEditorValue

Object

getCellEditorValue()

Returns the value contained in the editor.

isCellEditable

```java
boolean isCellEditable​(
EventObject
anEvent)
```

Asks the editor if it can start editing using

anEvent

.

anEvent

is in the invoking component coordinate system.
The editor can not assume the Component returned by

getCellEditorComponent

is installed. This method
is intended for the use of client to avoid the cost of setting up
and installing the editor component if editing is not possible.
If editing can be started this method returns true.

**Parameters:** anEvent

- the event the editor should use to consider
whether to begin editing or not
**Returns:** true if editing can be started
**See Also:** shouldSelectCell(java.util.EventObject)

---

#### isCellEditable

boolean isCellEditable​(

EventObject

anEvent)

Asks the editor if it can start editing using

anEvent

.

anEvent

is in the invoking component coordinate system.
The editor can not assume the Component returned by

getCellEditorComponent

is installed. This method
is intended for the use of client to avoid the cost of setting up
and installing the editor component if editing is not possible.
If editing can be started this method returns true.

shouldSelectCell

```java
boolean shouldSelectCell​(
EventObject
anEvent)
```

Returns true if the editing cell should be selected, false otherwise.
Typically, the return value is true, because is most cases the editing
cell should be selected. However, it is useful to return false to
keep the selection from changing for some types of edits.
eg. A table that contains a column of check boxes, the user might
want to be able to change those checkboxes without altering the
selection. (See Netscape Communicator for just such an example)
Of course, it is up to the client of the editor to use the return
value, but it doesn't need to if it doesn't want to.

**Parameters:** anEvent

- the event the editor should use to start
editing
**Returns:** true if the editor would like the editing cell to be selected;
otherwise returns false
**See Also:** isCellEditable(java.util.EventObject)

---

#### shouldSelectCell

boolean shouldSelectCell​(

EventObject

anEvent)

Returns true if the editing cell should be selected, false otherwise.
Typically, the return value is true, because is most cases the editing
cell should be selected. However, it is useful to return false to
keep the selection from changing for some types of edits.
eg. A table that contains a column of check boxes, the user might
want to be able to change those checkboxes without altering the
selection. (See Netscape Communicator for just such an example)
Of course, it is up to the client of the editor to use the return
value, but it doesn't need to if it doesn't want to.

stopCellEditing

```java
boolean stopCellEditing()
```

Tells the editor to stop editing and accept any partially edited
value as the value of the editor. The editor returns false if
editing was not stopped; this is useful for editors that validate
and can not accept invalid entries.

**Returns:** true if editing was stopped; false otherwise

---

#### stopCellEditing

boolean stopCellEditing()

Tells the editor to stop editing and accept any partially edited
value as the value of the editor. The editor returns false if
editing was not stopped; this is useful for editors that validate
and can not accept invalid entries.

cancelCellEditing

```java
void cancelCellEditing()
```

Tells the editor to cancel editing and not accept any partially
edited value.

---

#### cancelCellEditing

void cancelCellEditing()

Tells the editor to cancel editing and not accept any partially
edited value.

addCellEditorListener

```java
void addCellEditorListener​(
CellEditorListener
l)
```

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

**Parameters:** l

- the CellEditorListener

---

#### addCellEditorListener

void addCellEditorListener​(

CellEditorListener

l)

Adds a listener to the list that's notified when the editor
stops, or cancels editing.

removeCellEditorListener

```java
void removeCellEditorListener​(
CellEditorListener
l)
```

Removes a listener from the list that's notified

**Parameters:** l

- the CellEditorListener

---

#### removeCellEditorListener

void removeCellEditorListener​(

CellEditorListener

l)

Removes a listener from the list that's notified

---

