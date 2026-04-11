# Interface AccessibleSelection

**Source:** `java.desktop\javax\accessibility\AccessibleSelection.html`

### Class Description

```java
public interface
AccessibleSelection
```

This

AccessibleSelection

interface provides the standard mechanism
for an assistive technology to determine what the current selected children
are, as well as modify the selection set. Any object that has children that
can be selected should support the

AccessibleSelection

interface.
Applications can determine if an object supports the

AccessibleSelection

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleSelection()

method. If the return value
is not

null

, the object supports this interface.

**All Known Implementing Classes:** CheckboxMenuItem.AccessibleAWTCheckboxMenuItem

,

JComboBox.AccessibleJComboBox

,

JList.AccessibleJList

,

JMenu.AccessibleJMenu

,

JMenuBar.AccessibleJMenuBar

,

JTabbedPane.AccessibleJTabbedPane

,

JTable.AccessibleJTable

,

JTree.AccessibleJTree

,

JTree.AccessibleJTree.AccessibleJTreeNode

,

List.AccessibleAWTList

,

Menu.AccessibleAWTMenu

,

MenuBar.AccessibleAWTMenuBar

,

MenuComponent.AccessibleAWTMenuComponent

,

MenuItem.AccessibleAWTMenuItem

,

PopupMenu.AccessibleAWTPopupMenu

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getAccessibleSelectionCount()

Returns the number of

Accessible

children currently selected. If
no children are selected, the return value will be 0.

**Returns:**
- the number of items currently selected

---

#### Accessible
getAccessibleSelection​(int i)

Returns an

Accessible

representing the specified selected child
of the object. If there isn't a selection, or there are fewer children
selected than the integer passed in, the return value will be

null

.

Note that the index represents the i-th selected child, which is
different from the i-th child.

**Parameters:**
- i

- the zero-based index of selected children

**Returns:**
- the i-th selected child

**See Also:**
- getAccessibleSelectionCount()

---

#### boolean isAccessibleChildSelected​(int i)

Determines if the current child of this object is selected.

**Parameters:**
- i

- the zero-based index of the child in this

Accessible

object

**Returns:**
- true

if the current child of this object is selected;
else

false

**See Also:**
- AccessibleContext.getAccessibleChild(int)

---

#### void addAccessibleSelection​(int i)

Adds the specified

Accessible

child of the object to the object's
selection. If the object supports multiple selections, the specified
child is added to any existing selection, otherwise it replaces any
existing selection in the object. If the specified child is already
selected, this method has no effect.

**Parameters:**
- i

- the zero-based index of the child

**See Also:**
- AccessibleContext.getAccessibleChild(int)

---

#### void removeAccessibleSelection​(int i)

Removes the specified child of the object from the object's selection. If
the specified item isn't currently selected, this method has no effect.

**Parameters:**
- i

- the zero-based index of the child

**See Also:**
- AccessibleContext.getAccessibleChild(int)

---

#### void clearAccessibleSelection()

Clears the selection in the object, so that no children in the object are
selected.

---

#### void selectAllAccessibleSelection()

Causes every child of the object to be selected if the object supports
multiple selections.

---

### Additional Sections

#### Interface AccessibleSelection

**All Known Implementing Classes:** CheckboxMenuItem.AccessibleAWTCheckboxMenuItem

,

JComboBox.AccessibleJComboBox

,

JList.AccessibleJList

,

JMenu.AccessibleJMenu

,

JMenuBar.AccessibleJMenuBar

,

JTabbedPane.AccessibleJTabbedPane

,

JTable.AccessibleJTable

,

JTree.AccessibleJTree

,

JTree.AccessibleJTree.AccessibleJTreeNode

,

List.AccessibleAWTList

,

Menu.AccessibleAWTMenu

,

MenuBar.AccessibleAWTMenuBar

,

MenuComponent.AccessibleAWTMenuComponent

,

MenuItem.AccessibleAWTMenuItem

,

PopupMenu.AccessibleAWTPopupMenu

```java
public interface
AccessibleSelection
```

This

AccessibleSelection

interface provides the standard mechanism
for an assistive technology to determine what the current selected children
are, as well as modify the selection set. Any object that has children that
can be selected should support the

AccessibleSelection

interface.
Applications can determine if an object supports the

AccessibleSelection

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleSelection()

method. If the return value
is not

null

, the object supports this interface.

**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleSelection()

public interface

AccessibleSelection

This

AccessibleSelection

interface provides the standard mechanism
for an assistive technology to determine what the current selected children
are, as well as modify the selection set. Any object that has children that
can be selected should support the

AccessibleSelection

interface.
Applications can determine if an object supports the

AccessibleSelection

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleSelection()

method. If the return value
is not

null

, the object supports this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addAccessibleSelection

​(int i)

Adds the specified

Accessible

child of the object to the object's
selection.

void

clearAccessibleSelection

()

Clears the selection in the object, so that no children in the object are
selected.

Accessible

getAccessibleSelection

​(int i)

Returns an

Accessible

representing the specified selected child
of the object.

int

getAccessibleSelectionCount

()

Returns the number of

Accessible

children currently selected.

boolean

isAccessibleChildSelected

​(int i)

Determines if the current child of this object is selected.

void

removeAccessibleSelection

​(int i)

Removes the specified child of the object from the object's selection.

void

selectAllAccessibleSelection

()

Causes every child of the object to be selected if the object supports
multiple selections.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addAccessibleSelection

​(int i)

Adds the specified

Accessible

child of the object to the object's
selection.

void

clearAccessibleSelection

()

Clears the selection in the object, so that no children in the object are
selected.

Accessible

getAccessibleSelection

​(int i)

Returns an

Accessible

representing the specified selected child
of the object.

int

getAccessibleSelectionCount

()

Returns the number of

Accessible

children currently selected.

boolean

isAccessibleChildSelected

​(int i)

Determines if the current child of this object is selected.

void

removeAccessibleSelection

​(int i)

Removes the specified child of the object from the object's selection.

void

selectAllAccessibleSelection

()

Causes every child of the object to be selected if the object supports
multiple selections.

---

#### Method Summary

Adds the specified

Accessible

child of the object to the object's
selection.

Clears the selection in the object, so that no children in the object are
selected.

Returns an

Accessible

representing the specified selected child
of the object.

Returns the number of

Accessible

children currently selected.

Determines if the current child of this object is selected.

Removes the specified child of the object from the object's selection.

Causes every child of the object to be selected if the object supports
multiple selections.

============ METHOD DETAIL ==========

- Method Detail

- getAccessibleSelectionCount

```java
int getAccessibleSelectionCount()
```

Returns the number of

Accessible

children currently selected. If
no children are selected, the return value will be 0.

**Returns:** the number of items currently selected

- getAccessibleSelection

```java
Accessible
getAccessibleSelection​(int i)
```

Returns an

Accessible

representing the specified selected child
of the object. If there isn't a selection, or there are fewer children
selected than the integer passed in, the return value will be

null

.

Note that the index represents the i-th selected child, which is
different from the i-th child.

**Parameters:** i

- the zero-based index of selected children
**Returns:** the i-th selected child
**See Also:** getAccessibleSelectionCount()

- isAccessibleChildSelected

```java
boolean isAccessibleChildSelected​(int i)
```

Determines if the current child of this object is selected.

**Parameters:** i

- the zero-based index of the child in this

Accessible

object
**Returns:** true

if the current child of this object is selected;
else

false
**See Also:** AccessibleContext.getAccessibleChild(int)

- addAccessibleSelection

```java
void addAccessibleSelection​(int i)
```

Adds the specified

Accessible

child of the object to the object's
selection. If the object supports multiple selections, the specified
child is added to any existing selection, otherwise it replaces any
existing selection in the object. If the specified child is already
selected, this method has no effect.

**Parameters:** i

- the zero-based index of the child
**See Also:** AccessibleContext.getAccessibleChild(int)

- removeAccessibleSelection

```java
void removeAccessibleSelection​(int i)
```

Removes the specified child of the object from the object's selection. If
the specified item isn't currently selected, this method has no effect.

**Parameters:** i

- the zero-based index of the child
**See Also:** AccessibleContext.getAccessibleChild(int)

- clearAccessibleSelection

```java
void clearAccessibleSelection()
```

Clears the selection in the object, so that no children in the object are
selected.

- selectAllAccessibleSelection

```java
void selectAllAccessibleSelection()
```

Causes every child of the object to be selected if the object supports
multiple selections.

Method Detail

- getAccessibleSelectionCount

```java
int getAccessibleSelectionCount()
```

Returns the number of

Accessible

children currently selected. If
no children are selected, the return value will be 0.

**Returns:** the number of items currently selected

- getAccessibleSelection

```java
Accessible
getAccessibleSelection​(int i)
```

Returns an

Accessible

representing the specified selected child
of the object. If there isn't a selection, or there are fewer children
selected than the integer passed in, the return value will be

null

.

Note that the index represents the i-th selected child, which is
different from the i-th child.

**Parameters:** i

- the zero-based index of selected children
**Returns:** the i-th selected child
**See Also:** getAccessibleSelectionCount()

- isAccessibleChildSelected

```java
boolean isAccessibleChildSelected​(int i)
```

Determines if the current child of this object is selected.

**Parameters:** i

- the zero-based index of the child in this

Accessible

object
**Returns:** true

if the current child of this object is selected;
else

false
**See Also:** AccessibleContext.getAccessibleChild(int)

- addAccessibleSelection

```java
void addAccessibleSelection​(int i)
```

Adds the specified

Accessible

child of the object to the object's
selection. If the object supports multiple selections, the specified
child is added to any existing selection, otherwise it replaces any
existing selection in the object. If the specified child is already
selected, this method has no effect.

**Parameters:** i

- the zero-based index of the child
**See Also:** AccessibleContext.getAccessibleChild(int)

- removeAccessibleSelection

```java
void removeAccessibleSelection​(int i)
```

Removes the specified child of the object from the object's selection. If
the specified item isn't currently selected, this method has no effect.

**Parameters:** i

- the zero-based index of the child
**See Also:** AccessibleContext.getAccessibleChild(int)

- clearAccessibleSelection

```java
void clearAccessibleSelection()
```

Clears the selection in the object, so that no children in the object are
selected.

- selectAllAccessibleSelection

```java
void selectAllAccessibleSelection()
```

Causes every child of the object to be selected if the object supports
multiple selections.

---

#### Method Detail

getAccessibleSelectionCount

```java
int getAccessibleSelectionCount()
```

Returns the number of

Accessible

children currently selected. If
no children are selected, the return value will be 0.

**Returns:** the number of items currently selected

---

#### getAccessibleSelectionCount

int getAccessibleSelectionCount()

Returns the number of

Accessible

children currently selected. If
no children are selected, the return value will be 0.

getAccessibleSelection

```java
Accessible
getAccessibleSelection​(int i)
```

Returns an

Accessible

representing the specified selected child
of the object. If there isn't a selection, or there are fewer children
selected than the integer passed in, the return value will be

null

.

Note that the index represents the i-th selected child, which is
different from the i-th child.

**Parameters:** i

- the zero-based index of selected children
**Returns:** the i-th selected child
**See Also:** getAccessibleSelectionCount()

---

#### getAccessibleSelection

Accessible

getAccessibleSelection​(int i)

Returns an

Accessible

representing the specified selected child
of the object. If there isn't a selection, or there are fewer children
selected than the integer passed in, the return value will be

null

.

Note that the index represents the i-th selected child, which is
different from the i-th child.

Note that the index represents the i-th selected child, which is
different from the i-th child.

isAccessibleChildSelected

```java
boolean isAccessibleChildSelected​(int i)
```

Determines if the current child of this object is selected.

**Parameters:** i

- the zero-based index of the child in this

Accessible

object
**Returns:** true

if the current child of this object is selected;
else

false
**See Also:** AccessibleContext.getAccessibleChild(int)

---

#### isAccessibleChildSelected

boolean isAccessibleChildSelected​(int i)

Determines if the current child of this object is selected.

addAccessibleSelection

```java
void addAccessibleSelection​(int i)
```

Adds the specified

Accessible

child of the object to the object's
selection. If the object supports multiple selections, the specified
child is added to any existing selection, otherwise it replaces any
existing selection in the object. If the specified child is already
selected, this method has no effect.

**Parameters:** i

- the zero-based index of the child
**See Also:** AccessibleContext.getAccessibleChild(int)

---

#### addAccessibleSelection

void addAccessibleSelection​(int i)

Adds the specified

Accessible

child of the object to the object's
selection. If the object supports multiple selections, the specified
child is added to any existing selection, otherwise it replaces any
existing selection in the object. If the specified child is already
selected, this method has no effect.

removeAccessibleSelection

```java
void removeAccessibleSelection​(int i)
```

Removes the specified child of the object from the object's selection. If
the specified item isn't currently selected, this method has no effect.

**Parameters:** i

- the zero-based index of the child
**See Also:** AccessibleContext.getAccessibleChild(int)

---

#### removeAccessibleSelection

void removeAccessibleSelection​(int i)

Removes the specified child of the object from the object's selection. If
the specified item isn't currently selected, this method has no effect.

clearAccessibleSelection

```java
void clearAccessibleSelection()
```

Clears the selection in the object, so that no children in the object are
selected.

---

#### clearAccessibleSelection

void clearAccessibleSelection()

Clears the selection in the object, so that no children in the object are
selected.

selectAllAccessibleSelection

```java
void selectAllAccessibleSelection()
```

Causes every child of the object to be selected if the object supports
multiple selections.

---

#### selectAllAccessibleSelection

void selectAllAccessibleSelection()

Causes every child of the object to be selected if the object supports
multiple selections.

---

