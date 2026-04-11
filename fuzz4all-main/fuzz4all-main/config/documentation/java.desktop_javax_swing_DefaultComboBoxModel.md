# Class DefaultComboBoxModel<E>

**Source:** `java.desktop\javax\swing\DefaultComboBoxModel.html`

### Class Description

```java
public class
DefaultComboBoxModel<E>

extends
AbstractListModel
<E>
implements
MutableComboBoxModel
<E>,
Serializable
```

The default model for combo boxes.

**Type Parameters:** E

- the type of the elements of this model

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultComboBoxModel()

Constructs an empty DefaultComboBoxModel object.

---

#### public DefaultComboBoxModel​(
E
[] items)

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

**Parameters:**
- items

- an array of Object objects

---

#### public DefaultComboBoxModel​(
Vector
<
E
> v)

Constructs a DefaultComboBoxModel object initialized with
a vector.

**Parameters:**
- v

- a Vector object ...

---

### Method Details

#### public void setSelectedItem​(
Object
anObject)

Set the value of the selected item. The selected item may be null.

**Specified by:**
- setSelectedItem

in interface

ComboBoxModel

<

E

>

**Parameters:**
- anObject

- The combo box value or null for no selection.

---

#### public int getIndexOf​(
Object
anObject)

Returns the index-position of the specified object in the list.

**Parameters:**
- anObject

- the object to return the index of

**Returns:**
- an int representing the index position, where 0 is
the first position

---

#### public void removeAllElements()

Empties the list.

---

#### public void addAll​(
Collection
<? extends
E
> c)

Adds all of the elements present in the collection.

**Parameters:**
- c

- the collection which contains the elements to add

**Throws:**
- NullPointerException

- if

c

is null

---

#### public void addAll​(int index,

Collection
<? extends
E
> c)

Adds all of the elements present in the collection, starting
from the specified index.

**Parameters:**
- index

- index at which to insert the first element from the
specified collection
- c

- the collection which contains the elements to add

**Throws:**
- ArrayIndexOutOfBoundsException

- if

index

does not
fall within the range of number of elements currently held
- NullPointerException

- if

c

is null

---

### Additional Sections

#### Class DefaultComboBoxModel<E>

java.lang.Object

- javax.swing.AbstractListModel

<E>
- - javax.swing.DefaultComboBoxModel<E>

javax.swing.AbstractListModel

<E>

- javax.swing.DefaultComboBoxModel<E>

javax.swing.DefaultComboBoxModel<E>

**Type Parameters:** E

- the type of the elements of this model

**All Implemented Interfaces:** Serializable

,

ComboBoxModel

<E>

,

ListModel

<E>

,

MutableComboBoxModel

<E>

```java
public class
DefaultComboBoxModel<E>

extends
AbstractListModel
<E>
implements
MutableComboBoxModel
<E>,
Serializable
```

The default model for combo boxes.

**Since:** 1.2
**See Also:** Serialized Form

public class

DefaultComboBoxModel<E>

extends

AbstractListModel

<E>
implements

MutableComboBoxModel

<E>,

Serializable

The default model for combo boxes.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.

AbstractListModel

listenerList

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultComboBoxModel

()

Constructs an empty DefaultComboBoxModel object.

DefaultComboBoxModel

​(

E

[] items)

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

DefaultComboBoxModel

​(

Vector

<

E

> v)

Constructs a DefaultComboBoxModel object initialized with
a vector.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAll

​(int index,

Collection

<? extends

E

> c)

Adds all of the elements present in the collection, starting
from the specified index.

void

addAll

​(

Collection

<? extends

E

> c)

Adds all of the elements present in the collection.

int

getIndexOf

​(

Object

anObject)

Returns the index-position of the specified object in the list.

void

removeAllElements

()

Empties the list.

void

setSelectedItem

​(

Object

anObject)

Set the value of the selected item.

- Methods declared in class javax.swing.

AbstractListModel

addListDataListener

,

fireContentsChanged

,

fireIntervalAdded

,

fireIntervalRemoved

,

getListDataListeners

,

getListeners

,

removeListDataListener

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

ComboBoxModel

getSelectedItem

- Methods declared in interface javax.swing.

ListModel

addListDataListener

,

getElementAt

,

getSize

,

removeListDataListener

- Methods declared in interface javax.swing.

MutableComboBoxModel

addElement

,

insertElementAt

,

removeElement

,

removeElementAt

Field Summary

- Fields declared in class javax.swing.

AbstractListModel

listenerList

---

#### Field Summary

Fields declared in class javax.swing.

AbstractListModel

listenerList

---

#### Fields declared in class javax.swing. AbstractListModel

Constructor Summary

Constructors

Constructor

Description

DefaultComboBoxModel

()

Constructs an empty DefaultComboBoxModel object.

DefaultComboBoxModel

​(

E

[] items)

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

DefaultComboBoxModel

​(

Vector

<

E

> v)

Constructs a DefaultComboBoxModel object initialized with
a vector.

---

#### Constructor Summary

Constructs an empty DefaultComboBoxModel object.

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

Constructs a DefaultComboBoxModel object initialized with
a vector.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAll

​(int index,

Collection

<? extends

E

> c)

Adds all of the elements present in the collection, starting
from the specified index.

void

addAll

​(

Collection

<? extends

E

> c)

Adds all of the elements present in the collection.

int

getIndexOf

​(

Object

anObject)

Returns the index-position of the specified object in the list.

void

removeAllElements

()

Empties the list.

void

setSelectedItem

​(

Object

anObject)

Set the value of the selected item.

- Methods declared in class javax.swing.

AbstractListModel

addListDataListener

,

fireContentsChanged

,

fireIntervalAdded

,

fireIntervalRemoved

,

getListDataListeners

,

getListeners

,

removeListDataListener

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

ComboBoxModel

getSelectedItem

- Methods declared in interface javax.swing.

ListModel

addListDataListener

,

getElementAt

,

getSize

,

removeListDataListener

- Methods declared in interface javax.swing.

MutableComboBoxModel

addElement

,

insertElementAt

,

removeElement

,

removeElementAt

---

#### Method Summary

Adds all of the elements present in the collection, starting
from the specified index.

Adds all of the elements present in the collection.

Returns the index-position of the specified object in the list.

Empties the list.

Set the value of the selected item.

Methods declared in class javax.swing.

AbstractListModel

addListDataListener

,

fireContentsChanged

,

fireIntervalAdded

,

fireIntervalRemoved

,

getListDataListeners

,

getListeners

,

removeListDataListener

---

#### Methods declared in class javax.swing. AbstractListModel

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

ComboBoxModel

getSelectedItem

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

Methods declared in interface javax.swing.

MutableComboBoxModel

addElement

,

insertElementAt

,

removeElement

,

removeElementAt

---

#### Methods declared in interface javax.swing. MutableComboBoxModel

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultComboBoxModel

```java
public DefaultComboBoxModel()
```

Constructs an empty DefaultComboBoxModel object.

- DefaultComboBoxModel

```java
public DefaultComboBoxModel​(
E
[] items)
```

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

**Parameters:** items

- an array of Object objects

- DefaultComboBoxModel

```java
public DefaultComboBoxModel​(
Vector
<
E
> v)
```

Constructs a DefaultComboBoxModel object initialized with
a vector.

**Parameters:** v

- a Vector object ...

============ METHOD DETAIL ==========

- Method Detail

- setSelectedItem

```java
public void setSelectedItem​(
Object
anObject)
```

Set the value of the selected item. The selected item may be null.

**Specified by:** setSelectedItem

in interface

ComboBoxModel

<

E

>
**Parameters:** anObject

- The combo box value or null for no selection.

- getIndexOf

```java
public int getIndexOf​(
Object
anObject)
```

Returns the index-position of the specified object in the list.

**Parameters:** anObject

- the object to return the index of
**Returns:** an int representing the index position, where 0 is
the first position

- removeAllElements

```java
public void removeAllElements()
```

Empties the list.

- addAll

```java
public void addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection.

**Parameters:** c

- the collection which contains the elements to add
**Throws:** NullPointerException

- if

c

is null

- addAll

```java
public void addAll​(int index,

Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection, starting
from the specified index.

**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- the collection which contains the elements to add
**Throws:** ArrayIndexOutOfBoundsException

- if

index

does not
fall within the range of number of elements currently held
**Throws:** NullPointerException

- if

c

is null

Constructor Detail

- DefaultComboBoxModel

```java
public DefaultComboBoxModel()
```

Constructs an empty DefaultComboBoxModel object.

- DefaultComboBoxModel

```java
public DefaultComboBoxModel​(
E
[] items)
```

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

**Parameters:** items

- an array of Object objects

- DefaultComboBoxModel

```java
public DefaultComboBoxModel​(
Vector
<
E
> v)
```

Constructs a DefaultComboBoxModel object initialized with
a vector.

**Parameters:** v

- a Vector object ...

---

#### Constructor Detail

DefaultComboBoxModel

```java
public DefaultComboBoxModel()
```

Constructs an empty DefaultComboBoxModel object.

---

#### DefaultComboBoxModel

public DefaultComboBoxModel()

Constructs an empty DefaultComboBoxModel object.

DefaultComboBoxModel

```java
public DefaultComboBoxModel​(
E
[] items)
```

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

**Parameters:** items

- an array of Object objects

---

#### DefaultComboBoxModel

public DefaultComboBoxModel​(

E

[] items)

Constructs a DefaultComboBoxModel object initialized with
an array of objects.

DefaultComboBoxModel

```java
public DefaultComboBoxModel​(
Vector
<
E
> v)
```

Constructs a DefaultComboBoxModel object initialized with
a vector.

**Parameters:** v

- a Vector object ...

---

#### DefaultComboBoxModel

public DefaultComboBoxModel​(

Vector

<

E

> v)

Constructs a DefaultComboBoxModel object initialized with
a vector.

Method Detail

- setSelectedItem

```java
public void setSelectedItem​(
Object
anObject)
```

Set the value of the selected item. The selected item may be null.

**Specified by:** setSelectedItem

in interface

ComboBoxModel

<

E

>
**Parameters:** anObject

- The combo box value or null for no selection.

- getIndexOf

```java
public int getIndexOf​(
Object
anObject)
```

Returns the index-position of the specified object in the list.

**Parameters:** anObject

- the object to return the index of
**Returns:** an int representing the index position, where 0 is
the first position

- removeAllElements

```java
public void removeAllElements()
```

Empties the list.

- addAll

```java
public void addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection.

**Parameters:** c

- the collection which contains the elements to add
**Throws:** NullPointerException

- if

c

is null

- addAll

```java
public void addAll​(int index,

Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection, starting
from the specified index.

**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- the collection which contains the elements to add
**Throws:** ArrayIndexOutOfBoundsException

- if

index

does not
fall within the range of number of elements currently held
**Throws:** NullPointerException

- if

c

is null

---

#### Method Detail

setSelectedItem

```java
public void setSelectedItem​(
Object
anObject)
```

Set the value of the selected item. The selected item may be null.

**Specified by:** setSelectedItem

in interface

ComboBoxModel

<

E

>
**Parameters:** anObject

- The combo box value or null for no selection.

---

#### setSelectedItem

public void setSelectedItem​(

Object

anObject)

Set the value of the selected item. The selected item may be null.

getIndexOf

```java
public int getIndexOf​(
Object
anObject)
```

Returns the index-position of the specified object in the list.

**Parameters:** anObject

- the object to return the index of
**Returns:** an int representing the index position, where 0 is
the first position

---

#### getIndexOf

public int getIndexOf​(

Object

anObject)

Returns the index-position of the specified object in the list.

removeAllElements

```java
public void removeAllElements()
```

Empties the list.

---

#### removeAllElements

public void removeAllElements()

Empties the list.

addAll

```java
public void addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection.

**Parameters:** c

- the collection which contains the elements to add
**Throws:** NullPointerException

- if

c

is null

---

#### addAll

public void addAll​(

Collection

<? extends

E

> c)

Adds all of the elements present in the collection.

addAll

```java
public void addAll​(int index,

Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection, starting
from the specified index.

**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- the collection which contains the elements to add
**Throws:** ArrayIndexOutOfBoundsException

- if

index

does not
fall within the range of number of elements currently held
**Throws:** NullPointerException

- if

c

is null

---

#### addAll

public void addAll​(int index,

Collection

<? extends

E

> c)

Adds all of the elements present in the collection, starting
from the specified index.

---

