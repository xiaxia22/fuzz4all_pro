# Interface ComboBoxModel<E>

**Source:** `java.desktop\javax\swing\ComboBoxModel.html`

### Class Description

```java
public interface
ComboBoxModel<E>

extends
ListModel
<E>
```

A data model for a combo box. This interface extends

ListDataModel

and adds the concept of a

selected item

. The selected item is generally
the item which is visible in the combo box display area.

The selected item may not necessarily be managed by the underlying

ListModel

. This disjoint behavior allows for the temporary
storage and retrieval of a selected item in the model.

**Type Parameters:** E

- the type of the elements of this model

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setSelectedItem​(
Object
anItem)

Set the selected item. The implementation of this method should notify
all registered

ListDataListener

s that the contents
have changed.

**Parameters:**
- anItem

- the list object to select or

null

to clear the selection

---

#### Object
getSelectedItem()

Returns the selected item

**Returns:**
- The selected item or

null

if there is no selection

---

### Additional Sections

#### Interface ComboBoxModel<E>

**Type Parameters:** E

- the type of the elements of this model

**All Superinterfaces:** ListModel

<E>

**All Known Subinterfaces:** MutableComboBoxModel

<E>

**All Known Implementing Classes:** DefaultComboBoxModel

,

MetalFileChooserUI.DirectoryComboBoxModel

,

MetalFileChooserUI.FilterComboBoxModel

```java
public interface
ComboBoxModel<E>

extends
ListModel
<E>
```

A data model for a combo box. This interface extends

ListDataModel

and adds the concept of a

selected item

. The selected item is generally
the item which is visible in the combo box display area.

The selected item may not necessarily be managed by the underlying

ListModel

. This disjoint behavior allows for the temporary
storage and retrieval of a selected item in the model.

**Since:** 1.2

public interface

ComboBoxModel<E>

extends

ListModel

<E>

A data model for a combo box. This interface extends

ListDataModel

and adds the concept of a

selected item

. The selected item is generally
the item which is visible in the combo box display area.

The selected item may not necessarily be managed by the underlying

ListModel

. This disjoint behavior allows for the temporary
storage and retrieval of a selected item in the model.

The selected item may not necessarily be managed by the underlying

ListModel

. This disjoint behavior allows for the temporary
storage and retrieval of a selected item in the model.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getSelectedItem

()

Returns the selected item

void

setSelectedItem

​(

Object

anItem)

Set the selected item.

- Methods declared in interface javax.swing.

ListModel

addListDataListener

,

getElementAt

,

getSize

,

removeListDataListener

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getSelectedItem

()

Returns the selected item

void

setSelectedItem

​(

Object

anItem)

Set the selected item.

- Methods declared in interface javax.swing.

ListModel

addListDataListener

,

getElementAt

,

getSize

,

removeListDataListener

---

#### Method Summary

Returns the selected item

Set the selected item.

Methods declared in interface javax.swing.

ListModel

addListDataListener

,

getElementAt

,

getSize

,

removeListDataListener

---

#### Methods declared in interface javax.swing. ListModel

============ METHOD DETAIL ==========

- Method Detail

- setSelectedItem

```java
void setSelectedItem​(
Object
anItem)
```

Set the selected item. The implementation of this method should notify
all registered

ListDataListener

s that the contents
have changed.

**Parameters:** anItem

- the list object to select or

null

to clear the selection

- getSelectedItem

```java
Object
getSelectedItem()
```

Returns the selected item

**Returns:** The selected item or

null

if there is no selection

Method Detail

- setSelectedItem

```java
void setSelectedItem​(
Object
anItem)
```

Set the selected item. The implementation of this method should notify
all registered

ListDataListener

s that the contents
have changed.

**Parameters:** anItem

- the list object to select or

null

to clear the selection

- getSelectedItem

```java
Object
getSelectedItem()
```

Returns the selected item

**Returns:** The selected item or

null

if there is no selection

---

#### Method Detail

setSelectedItem

```java
void setSelectedItem​(
Object
anItem)
```

Set the selected item. The implementation of this method should notify
all registered

ListDataListener

s that the contents
have changed.

**Parameters:** anItem

- the list object to select or

null

to clear the selection

---

#### setSelectedItem

void setSelectedItem​(

Object

anItem)

Set the selected item. The implementation of this method should notify
all registered

ListDataListener

s that the contents
have changed.

getSelectedItem

```java
Object
getSelectedItem()
```

Returns the selected item

**Returns:** The selected item or

null

if there is no selection

---

#### getSelectedItem

Object

getSelectedItem()

Returns the selected item

---

