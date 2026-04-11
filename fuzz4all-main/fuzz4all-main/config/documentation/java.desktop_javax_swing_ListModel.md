# Interface ListModel<E>

**Source:** `java.desktop\javax\swing\ListModel.html`

### Class Description

```java
public interface
ListModel<E>
```

This interface defines the methods components like JList use
to get the value of each cell in a list and the length of the list.
Logically the model is a vector, indices vary from 0 to
ListDataModel.getSize() - 1. Any change to the contents or
length of the data model must be reported to all of the
ListDataListeners.

**Type Parameters:** E

- the type of the elements of this model

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getSize()

Returns the length of the list.

**Returns:**
- the length of the list

---

#### E
getElementAt​(int index)

Returns the value at the specified index.

**Parameters:**
- index

- the requested index

**Returns:**
- the value at

index

---

#### void addListDataListener​(
ListDataListener
l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Parameters:**
- l

- the

ListDataListener

to be added

---

#### void removeListDataListener​(
ListDataListener
l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Parameters:**
- l

- the

ListDataListener

to be removed

---

### Additional Sections

#### Interface ListModel<E>

**Type Parameters:** E

- the type of the elements of this model

**All Known Subinterfaces:** ComboBoxModel

<E>

,

MutableComboBoxModel

<E>

**All Known Implementing Classes:** AbstractListModel

,

BasicDirectoryModel

,

DefaultComboBoxModel

,

DefaultListModel

,

MetalFileChooserUI.DirectoryComboBoxModel

,

MetalFileChooserUI.FilterComboBoxModel

```java
public interface
ListModel<E>
```

This interface defines the methods components like JList use
to get the value of each cell in a list and the length of the list.
Logically the model is a vector, indices vary from 0 to
ListDataModel.getSize() - 1. Any change to the contents or
length of the data model must be reported to all of the
ListDataListeners.

**Since:** 1.2
**See Also:** JList

public interface

ListModel<E>

This interface defines the methods components like JList use
to get the value of each cell in a list and the length of the list.
Logically the model is a vector, indices vary from 0 to
ListDataModel.getSize() - 1. Any change to the contents or
length of the data model must be reported to all of the
ListDataListeners.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addListDataListener

​(

ListDataListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

E

getElementAt

​(int index)

Returns the value at the specified index.

int

getSize

()

Returns the length of the list.

void

removeListDataListener

​(

ListDataListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addListDataListener

​(

ListDataListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

E

getElementAt

​(int index)

Returns the value at the specified index.

int

getSize

()

Returns the length of the list.

void

removeListDataListener

​(

ListDataListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

---

#### Method Summary

Adds a listener to the list that's notified each time a change
to the data model occurs.

Returns the value at the specified index.

Returns the length of the list.

Removes a listener from the list that's notified each time a
change to the data model occurs.

============ METHOD DETAIL ==========

- Method Detail

- getSize

```java
int getSize()
```

Returns the length of the list.

**Returns:** the length of the list

- getElementAt

```java
E
getElementAt​(int index)
```

Returns the value at the specified index.

**Parameters:** index

- the requested index
**Returns:** the value at

index

- addListDataListener

```java
void addListDataListener​(
ListDataListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Parameters:** l

- the

ListDataListener

to be added

- removeListDataListener

```java
void removeListDataListener​(
ListDataListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Parameters:** l

- the

ListDataListener

to be removed

Method Detail

- getSize

```java
int getSize()
```

Returns the length of the list.

**Returns:** the length of the list

- getElementAt

```java
E
getElementAt​(int index)
```

Returns the value at the specified index.

**Parameters:** index

- the requested index
**Returns:** the value at

index

- addListDataListener

```java
void addListDataListener​(
ListDataListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Parameters:** l

- the

ListDataListener

to be added

- removeListDataListener

```java
void removeListDataListener​(
ListDataListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Parameters:** l

- the

ListDataListener

to be removed

---

#### Method Detail

getSize

```java
int getSize()
```

Returns the length of the list.

**Returns:** the length of the list

---

#### getSize

int getSize()

Returns the length of the list.

getElementAt

```java
E
getElementAt​(int index)
```

Returns the value at the specified index.

**Parameters:** index

- the requested index
**Returns:** the value at

index

---

#### getElementAt

E

getElementAt​(int index)

Returns the value at the specified index.

addListDataListener

```java
void addListDataListener​(
ListDataListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Parameters:** l

- the

ListDataListener

to be added

---

#### addListDataListener

void addListDataListener​(

ListDataListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

removeListDataListener

```java
void removeListDataListener​(
ListDataListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Parameters:** l

- the

ListDataListener

to be removed

---

#### removeListDataListener

void removeListDataListener​(

ListDataListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

---

