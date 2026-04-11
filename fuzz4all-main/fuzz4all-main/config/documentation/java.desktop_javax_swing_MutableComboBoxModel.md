# Interface MutableComboBoxModel<E>

**Source:** `java.desktop\javax\swing\MutableComboBoxModel.html`

### Class Description

```java
public interface
MutableComboBoxModel<E>

extends
ComboBoxModel
<E>
```

A mutable version of

ComboBoxModel

.

**Type Parameters:** E

- the type of the elements of this model

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addElement​(
E
item)

Adds an item at the end of the model. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:**
- item

- the item to be added

---

#### void removeElement​(
Object
obj)

Removes an item from the model. The implementation of this method should
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:**
- obj

- the

Object

to be removed

---

#### void insertElementAt​(
E
item,
int index)

Adds an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:**
- item

- the item to be added
- index

- location to add the object

---

#### void removeElementAt​(int index)

Removes an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:**
- index

- location of the item to be removed

---

### Additional Sections

#### Interface MutableComboBoxModel<E>

**Type Parameters:** E

- the type of the elements of this model

**All Superinterfaces:** ComboBoxModel

<E>

,

ListModel

<E>

**All Known Implementing Classes:** DefaultComboBoxModel

```java
public interface
MutableComboBoxModel<E>

extends
ComboBoxModel
<E>
```

A mutable version of

ComboBoxModel

.

**Since:** 1.2

public interface

MutableComboBoxModel<E>

extends

ComboBoxModel

<E>

A mutable version of

ComboBoxModel

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

addElement

​(

E

item)

Adds an item at the end of the model.

void

insertElementAt

​(

E

item,
int index)

Adds an item at a specific index.

void

removeElement

​(

Object

obj)

Removes an item from the model.

void

removeElementAt

​(int index)

Removes an item at a specific index.

- Methods declared in interface javax.swing.

ComboBoxModel

getSelectedItem

,

setSelectedItem

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

void

addElement

​(

E

item)

Adds an item at the end of the model.

void

insertElementAt

​(

E

item,
int index)

Adds an item at a specific index.

void

removeElement

​(

Object

obj)

Removes an item from the model.

void

removeElementAt

​(int index)

Removes an item at a specific index.

- Methods declared in interface javax.swing.

ComboBoxModel

getSelectedItem

,

setSelectedItem

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

Adds an item at the end of the model.

Adds an item at a specific index.

Removes an item from the model.

Removes an item at a specific index.

Methods declared in interface javax.swing.

ComboBoxModel

getSelectedItem

,

setSelectedItem

---

#### Methods declared in interface javax.swing. ComboBoxModel

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

- addElement

```java
void addElement​(
E
item)
```

Adds an item at the end of the model. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:** item

- the item to be added

- removeElement

```java
void removeElement​(
Object
obj)
```

Removes an item from the model. The implementation of this method should
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:** obj

- the

Object

to be removed

- insertElementAt

```java
void insertElementAt​(
E
item,
int index)
```

Adds an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:** item

- the item to be added
**Parameters:** index

- location to add the object

- removeElementAt

```java
void removeElementAt​(int index)
```

Removes an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:** index

- location of the item to be removed

Method Detail

- addElement

```java
void addElement​(
E
item)
```

Adds an item at the end of the model. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:** item

- the item to be added

- removeElement

```java
void removeElement​(
Object
obj)
```

Removes an item from the model. The implementation of this method should
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:** obj

- the

Object

to be removed

- insertElementAt

```java
void insertElementAt​(
E
item,
int index)
```

Adds an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:** item

- the item to be added
**Parameters:** index

- location to add the object

- removeElementAt

```java
void removeElementAt​(int index)
```

Removes an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:** index

- location of the item to be removed

---

#### Method Detail

addElement

```java
void addElement​(
E
item)
```

Adds an item at the end of the model. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:** item

- the item to be added

---

#### addElement

void addElement​(

E

item)

Adds an item at the end of the model. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

removeElement

```java
void removeElement​(
Object
obj)
```

Removes an item from the model. The implementation of this method should
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:** obj

- the

Object

to be removed

---

#### removeElement

void removeElement​(

Object

obj)

Removes an item from the model. The implementation of this method should
should notify all registered

ListDataListener

s that the
item has been removed.

insertElementAt

```java
void insertElementAt​(
E
item,
int index)
```

Adds an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

**Parameters:** item

- the item to be added
**Parameters:** index

- location to add the object

---

#### insertElementAt

void insertElementAt​(

E

item,
int index)

Adds an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been added.

removeElementAt

```java
void removeElementAt​(int index)
```

Removes an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been removed.

**Parameters:** index

- location of the item to be removed

---

#### removeElementAt

void removeElementAt​(int index)

Removes an item at a specific index. The implementation of this method
should notify all registered

ListDataListener

s that the
item has been removed.

---

