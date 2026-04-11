# Class DefaultListModel<E>

**Source:** `java.desktop\javax\swing\DefaultListModel.html`

### Class Description

```java
public class
DefaultListModel<E>

extends
AbstractListModel
<E>
```

This class loosely implements the

java.util.Vector

API, in that it implements the 1.1.x version of

java.util.Vector

, has no collection class support,
and notifies the

ListDataListener

s when changes occur.
Presently it delegates to a

Vector

,
in a future release it will be a real Collection implementation.

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

**Type Parameters:** E

- the type of the elements of this model

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultListModel()

*No description found.*

---

### Method Details

#### public int getSize()

Returns the number of components in this list.

This method is identical to

size

, which implements the

List

interface defined in the 1.2 Collections framework.
This method exists in conjunction with

setSize

so that

size

is identifiable as a JavaBean property.

**Returns:**
- the number of components in this list

**See Also:**
- size()

---

#### public
E
getElementAt​(int index)

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:**
- index

- an index into this list

**Returns:**
- the component at the specified index

**Throws:**
- ArrayIndexOutOfBoundsException

- if the

index

is negative or greater than the current size of this
list

**See Also:**
- get(int)

---

#### public void copyInto​(
Object
[] anArray)

Copies the components of this list into the specified array.
The array must be big enough to hold all the objects in this list,
else an

IndexOutOfBoundsException

is thrown.

**Parameters:**
- anArray

- the array into which the components get copied

**See Also:**
- Vector.copyInto(Object[])

---

#### public void trimToSize()

Trims the capacity of this list to be the list's current size.

**See Also:**
- Vector.trimToSize()

---

#### public void ensureCapacity​(int minCapacity)

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

**Parameters:**
- minCapacity

- the desired minimum capacity

**See Also:**
- Vector.ensureCapacity(int)

---

#### public void setSize​(int newSize)

Sets the size of this list.

**Parameters:**
- newSize

- the new size of this list

**See Also:**
- Vector.setSize(int)

---

#### public int capacity()

Returns the current capacity of this list.

**Returns:**
- the current capacity

**See Also:**
- Vector.capacity()

---

#### public int size()

Returns the number of components in this list.

**Returns:**
- the number of components in this list

**See Also:**
- Vector.size()

---

#### public boolean isEmpty()

Tests whether this list has any components.

**Returns:**
- true

if and only if this list has
no components, that is, its size is zero;

false

otherwise

**See Also:**
- Vector.isEmpty()

---

#### public
Enumeration
<
E
> elements()

Returns an enumeration of the components of this list.

**Returns:**
- an enumeration of the components of this list

**See Also:**
- Vector.elements()

---

#### public boolean contains​(
Object
elem)

Tests whether the specified object is a component in this list.

**Parameters:**
- elem

- an object

**Returns:**
- true

if the specified object
is the same as a component in this list

**See Also:**
- Vector.contains(Object)

---

#### public int indexOf​(
Object
elem)

Searches for the first occurrence of

elem

.

**Parameters:**
- elem

- an object

**Returns:**
- the index of the first occurrence of the argument in this
list; returns

-1

if the object is not found

**See Also:**
- Vector.indexOf(Object)

---

#### public int indexOf​(
Object
elem,
int index)

Searches for the first occurrence of

elem

, beginning
the search at

index

.

**Parameters:**
- elem

- the desired component
- index

- the index from which to begin searching

**Returns:**
- the index where the first occurrence of

elem

is found after

index

; returns

-1

if the

elem

is not found in the list

**See Also:**
- Vector.indexOf(Object,int)

---

#### public int lastIndexOf​(
Object
elem)

Returns the index of the last occurrence of

elem

.

**Parameters:**
- elem

- the desired component

**Returns:**
- the index of the last occurrence of

elem

in the list; returns

elem

if the object is not found

**See Also:**
- Vector.lastIndexOf(Object)

---

#### public int lastIndexOf​(
Object
elem,
int index)

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

**Parameters:**
- elem

- the desired component
- index

- the index to start searching from

**Returns:**
- the index of the last occurrence of the

elem

in this list at position less than

index

;
returns

-1

if the object is not found

**See Also:**
- Vector.lastIndexOf(Object,int)

---

#### public
E
elementAt​(int index)

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:**
- index

- an index into this list

**Returns:**
- the component at the specified index

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index
is negative or not less than the size of the list

**See Also:**
- get(int)

,

Vector.elementAt(int)

---

#### public
E
firstElement()

Returns the first component of this list.

**Returns:**
- the first component of this list

**Throws:**
- NoSuchElementException

- if this
vector has no components

**See Also:**
- Vector.firstElement()

---

#### public
E
lastElement()

Returns the last component of the list.

**Returns:**
- the last component of the list

**Throws:**
- NoSuchElementException

- if this vector
has no components

**See Also:**
- Vector.lastElement()

---

#### public void setElementAt​(
E
element,
int index)

Sets the component at the specified

index

of this
list to be the specified element. The previous component at that
position is discarded.

Note:

Although this method is not deprecated, the preferred
method to use is

set(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:**
- element

- what the component is to be set to
- index

- the specified index

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index is invalid

**See Also:**
- set(int,Object)

,

Vector.setElementAt(Object,int)

---

#### public void removeElementAt​(int index)

Deletes the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

remove(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:**
- index

- the index of the object to remove

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index is invalid

**See Also:**
- remove(int)

,

Vector.removeElementAt(int)

---

#### public void insertElementAt​(
E
element,
int index)

Inserts the specified element as a component in this list at the
specified

index

.

Note:

Although this method is not deprecated, the preferred
method to use is

add(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:**
- element

- the component to insert
- index

- where to insert the new component

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index was invalid

**See Also:**
- add(int,Object)

,

Vector.insertElementAt(Object,int)

---

#### public void addElement​(
E
element)

Adds the specified component to the end of this list.

**Parameters:**
- element

- the component to be added

**See Also:**
- Vector.addElement(Object)

---

#### public boolean removeElement​(
Object
obj)

Removes the first (lowest-indexed) occurrence of the argument
from this list.

**Parameters:**
- obj

- the component to be removed

**Returns:**
- true

if the argument was a component of this
list;

false

otherwise

**See Also:**
- Vector.removeElement(Object)

---

#### public void removeAllElements()

Removes all components from this list and sets its size to zero.

Note:

Although this method is not deprecated, the preferred
method to use is

clear

, which implements the

List

interface defined in the 1.2 Collections framework.

**See Also:**
- clear()

,

Vector.removeAllElements()

---

#### public
String
toString()

Returns a string that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this object

---

#### public
Object
[] toArray()

Returns an array containing all of the elements in this list in the
correct order.

**Returns:**
- an array containing the elements of the list

**See Also:**
- Vector.toArray()

---

#### public
E
get​(int index)

Returns the element at the specified position in this list.

**Parameters:**
- index

- index of element to return

**Returns:**
- the element at the specified position in this list

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

---

#### public
E
set​(int index,

E
element)

Replaces the element at the specified position in this list with the
specified element.

**Parameters:**
- index

- index of element to replace
- element

- element to be stored at the specified position

**Returns:**
- the element previously at the specified position

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

---

#### public void add​(int index,

E
element)

Inserts the specified element at the specified position in this list.

**Parameters:**
- index

- index at which the specified element is to be inserted
- element

- element to be inserted

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt; size()

)

---

#### public
E
remove​(int index)

Removes the element at the specified position in this list.
Returns the element that was removed from the list

**Parameters:**
- index

- the index of the element to removed

**Returns:**
- the element previously at the specified position

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

---

#### public void clear()

Removes all of the elements from this list. The list will
be empty after this call returns (unless it throws an exception).

---

#### public void removeRange​(int fromIndex,
int toIndex)

Deletes the components at the specified range of indexes.
The removal is inclusive, so specifying a range of (1,5)
removes the component at index 1 and the component at index 5,
as well as all components in between.

**Parameters:**
- fromIndex

- the index of the lower end of the range
- toIndex

- the index of the upper end of the range

**Throws:**
- ArrayIndexOutOfBoundsException

- if the index was invalid
- IllegalArgumentException

- if

fromIndex &gt; toIndex

**See Also:**
- remove(int)

---

#### public void addAll​(
Collection
<? extends
E
> c)

Adds all of the elements present in the collection to the list.

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

#### Class DefaultListModel<E>

java.lang.Object

- javax.swing.AbstractListModel

<E>
- - javax.swing.DefaultListModel<E>

javax.swing.AbstractListModel

<E>

- javax.swing.DefaultListModel<E>

javax.swing.DefaultListModel<E>

**Type Parameters:** E

- the type of the elements of this model

**All Implemented Interfaces:** Serializable

,

ListModel

<E>

```java
public class
DefaultListModel<E>

extends
AbstractListModel
<E>
```

This class loosely implements the

java.util.Vector

API, in that it implements the 1.1.x version of

java.util.Vector

, has no collection class support,
and notifies the

ListDataListener

s when changes occur.
Presently it delegates to a

Vector

,
in a future release it will be a real Collection implementation.

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

DefaultListModel<E>

extends

AbstractListModel

<E>

This class loosely implements the

java.util.Vector

API, in that it implements the 1.1.x version of

java.util.Vector

, has no collection class support,
and notifies the

ListDataListener

s when changes occur.
Presently it delegates to a

Vector

,
in a future release it will be a real Collection implementation.

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

DefaultListModel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(int index,

E

element)

Inserts the specified element at the specified position in this list.

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

Adds all of the elements present in the collection to the list.

void

addElement

​(

E

element)

Adds the specified component to the end of this list.

int

capacity

()

Returns the current capacity of this list.

void

clear

()

Removes all of the elements from this list.

boolean

contains

​(

Object

elem)

Tests whether the specified object is a component in this list.

void

copyInto

​(

Object

[] anArray)

Copies the components of this list into the specified array.

E

elementAt

​(int index)

Returns the component at the specified index.

Enumeration

<

E

>

elements

()

Returns an enumeration of the components of this list.

void

ensureCapacity

​(int minCapacity)

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

E

firstElement

()

Returns the first component of this list.

E

get

​(int index)

Returns the element at the specified position in this list.

E

getElementAt

​(int index)

Returns the component at the specified index.

int

getSize

()

Returns the number of components in this list.

int

indexOf

​(

Object

elem)

Searches for the first occurrence of

elem

.

int

indexOf

​(

Object

elem,
int index)

Searches for the first occurrence of

elem

, beginning
the search at

index

.

void

insertElementAt

​(

E

element,
int index)

Inserts the specified element as a component in this list at the
specified

index

.

boolean

isEmpty

()

Tests whether this list has any components.

E

lastElement

()

Returns the last component of the list.

int

lastIndexOf

​(

Object

elem)

Returns the index of the last occurrence of

elem

.

int

lastIndexOf

​(

Object

elem,
int index)

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

E

remove

​(int index)

Removes the element at the specified position in this list.

void

removeAllElements

()

Removes all components from this list and sets its size to zero.

boolean

removeElement

​(

Object

obj)

Removes the first (lowest-indexed) occurrence of the argument
from this list.

void

removeElementAt

​(int index)

Deletes the component at the specified index.

void

removeRange

​(int fromIndex,
int toIndex)

Deletes the components at the specified range of indexes.

E

set

​(int index,

E

element)

Replaces the element at the specified position in this list with the
specified element.

void

setElementAt

​(

E

element,
int index)

Sets the component at the specified

index

of this
list to be the specified element.

void

setSize

​(int newSize)

Sets the size of this list.

int

size

()

Returns the number of components in this list.

Object

[]

toArray

()

Returns an array containing all of the elements in this list in the
correct order.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

trimToSize

()

Trims the capacity of this list to be the list's current size.

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

wait

,

wait

,

wait

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

DefaultListModel

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(int index,

E

element)

Inserts the specified element at the specified position in this list.

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

Adds all of the elements present in the collection to the list.

void

addElement

​(

E

element)

Adds the specified component to the end of this list.

int

capacity

()

Returns the current capacity of this list.

void

clear

()

Removes all of the elements from this list.

boolean

contains

​(

Object

elem)

Tests whether the specified object is a component in this list.

void

copyInto

​(

Object

[] anArray)

Copies the components of this list into the specified array.

E

elementAt

​(int index)

Returns the component at the specified index.

Enumeration

<

E

>

elements

()

Returns an enumeration of the components of this list.

void

ensureCapacity

​(int minCapacity)

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

E

firstElement

()

Returns the first component of this list.

E

get

​(int index)

Returns the element at the specified position in this list.

E

getElementAt

​(int index)

Returns the component at the specified index.

int

getSize

()

Returns the number of components in this list.

int

indexOf

​(

Object

elem)

Searches for the first occurrence of

elem

.

int

indexOf

​(

Object

elem,
int index)

Searches for the first occurrence of

elem

, beginning
the search at

index

.

void

insertElementAt

​(

E

element,
int index)

Inserts the specified element as a component in this list at the
specified

index

.

boolean

isEmpty

()

Tests whether this list has any components.

E

lastElement

()

Returns the last component of the list.

int

lastIndexOf

​(

Object

elem)

Returns the index of the last occurrence of

elem

.

int

lastIndexOf

​(

Object

elem,
int index)

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

E

remove

​(int index)

Removes the element at the specified position in this list.

void

removeAllElements

()

Removes all components from this list and sets its size to zero.

boolean

removeElement

​(

Object

obj)

Removes the first (lowest-indexed) occurrence of the argument
from this list.

void

removeElementAt

​(int index)

Deletes the component at the specified index.

void

removeRange

​(int fromIndex,
int toIndex)

Deletes the components at the specified range of indexes.

E

set

​(int index,

E

element)

Replaces the element at the specified position in this list with the
specified element.

void

setElementAt

​(

E

element,
int index)

Sets the component at the specified

index

of this
list to be the specified element.

void

setSize

​(int newSize)

Sets the size of this list.

int

size

()

Returns the number of components in this list.

Object

[]

toArray

()

Returns an array containing all of the elements in this list in the
correct order.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

trimToSize

()

Trims the capacity of this list to be the list's current size.

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

wait

,

wait

,

wait

---

#### Method Summary

Inserts the specified element at the specified position in this list.

Adds all of the elements present in the collection, starting
from the specified index.

Adds all of the elements present in the collection to the list.

Adds the specified component to the end of this list.

Returns the current capacity of this list.

Removes all of the elements from this list.

Tests whether the specified object is a component in this list.

Copies the components of this list into the specified array.

Returns the component at the specified index.

Returns an enumeration of the components of this list.

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

Returns the first component of this list.

Returns the element at the specified position in this list.

Returns the number of components in this list.

Searches for the first occurrence of

elem

.

Searches for the first occurrence of

elem

, beginning
the search at

index

.

Inserts the specified element as a component in this list at the
specified

index

.

Tests whether this list has any components.

Returns the last component of the list.

Returns the index of the last occurrence of

elem

.

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

Removes the element at the specified position in this list.

Removes all components from this list and sets its size to zero.

Removes the first (lowest-indexed) occurrence of the argument
from this list.

Deletes the component at the specified index.

Deletes the components at the specified range of indexes.

Replaces the element at the specified position in this list with the
specified element.

Sets the component at the specified

index

of this
list to be the specified element.

Sets the size of this list.

Returns an array containing all of the elements in this list in the
correct order.

Returns a string that displays and identifies this
object's properties.

Trims the capacity of this list to be the list's current size.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultListModel

```java
public DefaultListModel()
```

============ METHOD DETAIL ==========

- Method Detail

- getSize

```java
public int getSize()
```

Returns the number of components in this list.

This method is identical to

size

, which implements the

List

interface defined in the 1.2 Collections framework.
This method exists in conjunction with

setSize

so that

size

is identifiable as a JavaBean property.

**Returns:** the number of components in this list
**See Also:** size()

- getElementAt

```java
public
E
getElementAt​(int index)
```

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- an index into this list
**Returns:** the component at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the

index

is negative or greater than the current size of this
list
**See Also:** get(int)

- copyInto

```java
public void copyInto​(
Object
[] anArray)
```

Copies the components of this list into the specified array.
The array must be big enough to hold all the objects in this list,
else an

IndexOutOfBoundsException

is thrown.

**Parameters:** anArray

- the array into which the components get copied
**See Also:** Vector.copyInto(Object[])

- trimToSize

```java
public void trimToSize()
```

Trims the capacity of this list to be the list's current size.

**See Also:** Vector.trimToSize()

- ensureCapacity

```java
public void ensureCapacity​(int minCapacity)
```

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

**Parameters:** minCapacity

- the desired minimum capacity
**See Also:** Vector.ensureCapacity(int)

- setSize

```java
public void setSize​(int newSize)
```

Sets the size of this list.

**Parameters:** newSize

- the new size of this list
**See Also:** Vector.setSize(int)

- capacity

```java
public int capacity()
```

Returns the current capacity of this list.

**Returns:** the current capacity
**See Also:** Vector.capacity()

- size

```java
public int size()
```

Returns the number of components in this list.

**Returns:** the number of components in this list
**See Also:** Vector.size()

- isEmpty

```java
public boolean isEmpty()
```

Tests whether this list has any components.

**Returns:** true

if and only if this list has
no components, that is, its size is zero;

false

otherwise
**See Also:** Vector.isEmpty()

- elements

```java
public
Enumeration
<
E
> elements()
```

Returns an enumeration of the components of this list.

**Returns:** an enumeration of the components of this list
**See Also:** Vector.elements()

- contains

```java
public boolean contains​(
Object
elem)
```

Tests whether the specified object is a component in this list.

**Parameters:** elem

- an object
**Returns:** true

if the specified object
is the same as a component in this list
**See Also:** Vector.contains(Object)

- indexOf

```java
public int indexOf​(
Object
elem)
```

Searches for the first occurrence of

elem

.

**Parameters:** elem

- an object
**Returns:** the index of the first occurrence of the argument in this
list; returns

-1

if the object is not found
**See Also:** Vector.indexOf(Object)

- indexOf

```java
public int indexOf​(
Object
elem,
int index)
```

Searches for the first occurrence of

elem

, beginning
the search at

index

.

**Parameters:** elem

- the desired component
**Parameters:** index

- the index from which to begin searching
**Returns:** the index where the first occurrence of

elem

is found after

index

; returns

-1

if the

elem

is not found in the list
**See Also:** Vector.indexOf(Object,int)

- lastIndexOf

```java
public int lastIndexOf​(
Object
elem)
```

Returns the index of the last occurrence of

elem

.

**Parameters:** elem

- the desired component
**Returns:** the index of the last occurrence of

elem

in the list; returns

elem

if the object is not found
**See Also:** Vector.lastIndexOf(Object)

- lastIndexOf

```java
public int lastIndexOf​(
Object
elem,
int index)
```

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

**Parameters:** elem

- the desired component
**Parameters:** index

- the index to start searching from
**Returns:** the index of the last occurrence of the

elem

in this list at position less than

index

;
returns

-1

if the object is not found
**See Also:** Vector.lastIndexOf(Object,int)

- elementAt

```java
public
E
elementAt​(int index)
```

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- an index into this list
**Returns:** the component at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the index
is negative or not less than the size of the list
**See Also:** get(int)

,

Vector.elementAt(int)

- firstElement

```java
public
E
firstElement()
```

Returns the first component of this list.

**Returns:** the first component of this list
**Throws:** NoSuchElementException

- if this
vector has no components
**See Also:** Vector.firstElement()

- lastElement

```java
public
E
lastElement()
```

Returns the last component of the list.

**Returns:** the last component of the list
**Throws:** NoSuchElementException

- if this vector
has no components
**See Also:** Vector.lastElement()

- setElementAt

```java
public void setElementAt​(
E
element,
int index)
```

Sets the component at the specified

index

of this
list to be the specified element. The previous component at that
position is discarded.

Note:

Although this method is not deprecated, the preferred
method to use is

set(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** element

- what the component is to be set to
**Parameters:** index

- the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the index is invalid
**See Also:** set(int,Object)

,

Vector.setElementAt(Object,int)

- removeElementAt

```java
public void removeElementAt​(int index)
```

Deletes the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

remove(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- the index of the object to remove
**Throws:** ArrayIndexOutOfBoundsException

- if the index is invalid
**See Also:** remove(int)

,

Vector.removeElementAt(int)

- insertElementAt

```java
public void insertElementAt​(
E
element,
int index)
```

Inserts the specified element as a component in this list at the
specified

index

.

Note:

Although this method is not deprecated, the preferred
method to use is

add(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** element

- the component to insert
**Parameters:** index

- where to insert the new component
**Throws:** ArrayIndexOutOfBoundsException

- if the index was invalid
**See Also:** add(int,Object)

,

Vector.insertElementAt(Object,int)

- addElement

```java
public void addElement​(
E
element)
```

Adds the specified component to the end of this list.

**Parameters:** element

- the component to be added
**See Also:** Vector.addElement(Object)

- removeElement

```java
public boolean removeElement​(
Object
obj)
```

Removes the first (lowest-indexed) occurrence of the argument
from this list.

**Parameters:** obj

- the component to be removed
**Returns:** true

if the argument was a component of this
list;

false

otherwise
**See Also:** Vector.removeElement(Object)

- removeAllElements

```java
public void removeAllElements()
```

Removes all components from this list and sets its size to zero.

Note:

Although this method is not deprecated, the preferred
method to use is

clear

, which implements the

List

interface defined in the 1.2 Collections framework.

**See Also:** clear()

,

Vector.removeAllElements()

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

- toArray

```java
public
Object
[] toArray()
```

Returns an array containing all of the elements in this list in the
correct order.

**Returns:** an array containing the elements of the list
**See Also:** Vector.toArray()

- get

```java
public
E
get​(int index)
```

Returns the element at the specified position in this list.

**Parameters:** index

- index of element to return
**Returns:** the element at the specified position in this list
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

- set

```java
public
E
set​(int index,

E
element)
```

Replaces the element at the specified position in this list with the
specified element.

**Parameters:** index

- index of element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

- add

```java
public void add​(int index,

E
element)
```

Inserts the specified element at the specified position in this list.

**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt; size()

)

- remove

```java
public
E
remove​(int index)
```

Removes the element at the specified position in this list.
Returns the element that was removed from the list

**Parameters:** index

- the index of the element to removed
**Returns:** the element previously at the specified position
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

- clear

```java
public void clear()
```

Removes all of the elements from this list. The list will
be empty after this call returns (unless it throws an exception).

- removeRange

```java
public void removeRange​(int fromIndex,
int toIndex)
```

Deletes the components at the specified range of indexes.
The removal is inclusive, so specifying a range of (1,5)
removes the component at index 1 and the component at index 5,
as well as all components in between.

**Parameters:** fromIndex

- the index of the lower end of the range
**Parameters:** toIndex

- the index of the upper end of the range
**Throws:** ArrayIndexOutOfBoundsException

- if the index was invalid
**Throws:** IllegalArgumentException

- if

fromIndex &gt; toIndex
**See Also:** remove(int)

- addAll

```java
public void addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection to the list.

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

- DefaultListModel

```java
public DefaultListModel()
```

---

#### Constructor Detail

DefaultListModel

```java
public DefaultListModel()
```

---

#### DefaultListModel

public DefaultListModel()

Method Detail

- getSize

```java
public int getSize()
```

Returns the number of components in this list.

This method is identical to

size

, which implements the

List

interface defined in the 1.2 Collections framework.
This method exists in conjunction with

setSize

so that

size

is identifiable as a JavaBean property.

**Returns:** the number of components in this list
**See Also:** size()

- getElementAt

```java
public
E
getElementAt​(int index)
```

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- an index into this list
**Returns:** the component at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the

index

is negative or greater than the current size of this
list
**See Also:** get(int)

- copyInto

```java
public void copyInto​(
Object
[] anArray)
```

Copies the components of this list into the specified array.
The array must be big enough to hold all the objects in this list,
else an

IndexOutOfBoundsException

is thrown.

**Parameters:** anArray

- the array into which the components get copied
**See Also:** Vector.copyInto(Object[])

- trimToSize

```java
public void trimToSize()
```

Trims the capacity of this list to be the list's current size.

**See Also:** Vector.trimToSize()

- ensureCapacity

```java
public void ensureCapacity​(int minCapacity)
```

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

**Parameters:** minCapacity

- the desired minimum capacity
**See Also:** Vector.ensureCapacity(int)

- setSize

```java
public void setSize​(int newSize)
```

Sets the size of this list.

**Parameters:** newSize

- the new size of this list
**See Also:** Vector.setSize(int)

- capacity

```java
public int capacity()
```

Returns the current capacity of this list.

**Returns:** the current capacity
**See Also:** Vector.capacity()

- size

```java
public int size()
```

Returns the number of components in this list.

**Returns:** the number of components in this list
**See Also:** Vector.size()

- isEmpty

```java
public boolean isEmpty()
```

Tests whether this list has any components.

**Returns:** true

if and only if this list has
no components, that is, its size is zero;

false

otherwise
**See Also:** Vector.isEmpty()

- elements

```java
public
Enumeration
<
E
> elements()
```

Returns an enumeration of the components of this list.

**Returns:** an enumeration of the components of this list
**See Also:** Vector.elements()

- contains

```java
public boolean contains​(
Object
elem)
```

Tests whether the specified object is a component in this list.

**Parameters:** elem

- an object
**Returns:** true

if the specified object
is the same as a component in this list
**See Also:** Vector.contains(Object)

- indexOf

```java
public int indexOf​(
Object
elem)
```

Searches for the first occurrence of

elem

.

**Parameters:** elem

- an object
**Returns:** the index of the first occurrence of the argument in this
list; returns

-1

if the object is not found
**See Also:** Vector.indexOf(Object)

- indexOf

```java
public int indexOf​(
Object
elem,
int index)
```

Searches for the first occurrence of

elem

, beginning
the search at

index

.

**Parameters:** elem

- the desired component
**Parameters:** index

- the index from which to begin searching
**Returns:** the index where the first occurrence of

elem

is found after

index

; returns

-1

if the

elem

is not found in the list
**See Also:** Vector.indexOf(Object,int)

- lastIndexOf

```java
public int lastIndexOf​(
Object
elem)
```

Returns the index of the last occurrence of

elem

.

**Parameters:** elem

- the desired component
**Returns:** the index of the last occurrence of

elem

in the list; returns

elem

if the object is not found
**See Also:** Vector.lastIndexOf(Object)

- lastIndexOf

```java
public int lastIndexOf​(
Object
elem,
int index)
```

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

**Parameters:** elem

- the desired component
**Parameters:** index

- the index to start searching from
**Returns:** the index of the last occurrence of the

elem

in this list at position less than

index

;
returns

-1

if the object is not found
**See Also:** Vector.lastIndexOf(Object,int)

- elementAt

```java
public
E
elementAt​(int index)
```

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- an index into this list
**Returns:** the component at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the index
is negative or not less than the size of the list
**See Also:** get(int)

,

Vector.elementAt(int)

- firstElement

```java
public
E
firstElement()
```

Returns the first component of this list.

**Returns:** the first component of this list
**Throws:** NoSuchElementException

- if this
vector has no components
**See Also:** Vector.firstElement()

- lastElement

```java
public
E
lastElement()
```

Returns the last component of the list.

**Returns:** the last component of the list
**Throws:** NoSuchElementException

- if this vector
has no components
**See Also:** Vector.lastElement()

- setElementAt

```java
public void setElementAt​(
E
element,
int index)
```

Sets the component at the specified

index

of this
list to be the specified element. The previous component at that
position is discarded.

Note:

Although this method is not deprecated, the preferred
method to use is

set(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** element

- what the component is to be set to
**Parameters:** index

- the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the index is invalid
**See Also:** set(int,Object)

,

Vector.setElementAt(Object,int)

- removeElementAt

```java
public void removeElementAt​(int index)
```

Deletes the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

remove(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- the index of the object to remove
**Throws:** ArrayIndexOutOfBoundsException

- if the index is invalid
**See Also:** remove(int)

,

Vector.removeElementAt(int)

- insertElementAt

```java
public void insertElementAt​(
E
element,
int index)
```

Inserts the specified element as a component in this list at the
specified

index

.

Note:

Although this method is not deprecated, the preferred
method to use is

add(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** element

- the component to insert
**Parameters:** index

- where to insert the new component
**Throws:** ArrayIndexOutOfBoundsException

- if the index was invalid
**See Also:** add(int,Object)

,

Vector.insertElementAt(Object,int)

- addElement

```java
public void addElement​(
E
element)
```

Adds the specified component to the end of this list.

**Parameters:** element

- the component to be added
**See Also:** Vector.addElement(Object)

- removeElement

```java
public boolean removeElement​(
Object
obj)
```

Removes the first (lowest-indexed) occurrence of the argument
from this list.

**Parameters:** obj

- the component to be removed
**Returns:** true

if the argument was a component of this
list;

false

otherwise
**See Also:** Vector.removeElement(Object)

- removeAllElements

```java
public void removeAllElements()
```

Removes all components from this list and sets its size to zero.

Note:

Although this method is not deprecated, the preferred
method to use is

clear

, which implements the

List

interface defined in the 1.2 Collections framework.

**See Also:** clear()

,

Vector.removeAllElements()

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

- toArray

```java
public
Object
[] toArray()
```

Returns an array containing all of the elements in this list in the
correct order.

**Returns:** an array containing the elements of the list
**See Also:** Vector.toArray()

- get

```java
public
E
get​(int index)
```

Returns the element at the specified position in this list.

**Parameters:** index

- index of element to return
**Returns:** the element at the specified position in this list
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

- set

```java
public
E
set​(int index,

E
element)
```

Replaces the element at the specified position in this list with the
specified element.

**Parameters:** index

- index of element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

- add

```java
public void add​(int index,

E
element)
```

Inserts the specified element at the specified position in this list.

**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt; size()

)

- remove

```java
public
E
remove​(int index)
```

Removes the element at the specified position in this list.
Returns the element that was removed from the list

**Parameters:** index

- the index of the element to removed
**Returns:** the element previously at the specified position
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

- clear

```java
public void clear()
```

Removes all of the elements from this list. The list will
be empty after this call returns (unless it throws an exception).

- removeRange

```java
public void removeRange​(int fromIndex,
int toIndex)
```

Deletes the components at the specified range of indexes.
The removal is inclusive, so specifying a range of (1,5)
removes the component at index 1 and the component at index 5,
as well as all components in between.

**Parameters:** fromIndex

- the index of the lower end of the range
**Parameters:** toIndex

- the index of the upper end of the range
**Throws:** ArrayIndexOutOfBoundsException

- if the index was invalid
**Throws:** IllegalArgumentException

- if

fromIndex &gt; toIndex
**See Also:** remove(int)

- addAll

```java
public void addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection to the list.

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

getSize

```java
public int getSize()
```

Returns the number of components in this list.

This method is identical to

size

, which implements the

List

interface defined in the 1.2 Collections framework.
This method exists in conjunction with

setSize

so that

size

is identifiable as a JavaBean property.

**Returns:** the number of components in this list
**See Also:** size()

---

#### getSize

public int getSize()

Returns the number of components in this list.

This method is identical to

size

, which implements the

List

interface defined in the 1.2 Collections framework.
This method exists in conjunction with

setSize

so that

size

is identifiable as a JavaBean property.

This method is identical to

size

, which implements the

List

interface defined in the 1.2 Collections framework.
This method exists in conjunction with

setSize

so that

size

is identifiable as a JavaBean property.

getElementAt

```java
public
E
getElementAt​(int index)
```

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- an index into this list
**Returns:** the component at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the

index

is negative or greater than the current size of this
list
**See Also:** get(int)

---

#### getElementAt

public

E

getElementAt​(int index)

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

copyInto

```java
public void copyInto​(
Object
[] anArray)
```

Copies the components of this list into the specified array.
The array must be big enough to hold all the objects in this list,
else an

IndexOutOfBoundsException

is thrown.

**Parameters:** anArray

- the array into which the components get copied
**See Also:** Vector.copyInto(Object[])

---

#### copyInto

public void copyInto​(

Object

[] anArray)

Copies the components of this list into the specified array.
The array must be big enough to hold all the objects in this list,
else an

IndexOutOfBoundsException

is thrown.

trimToSize

```java
public void trimToSize()
```

Trims the capacity of this list to be the list's current size.

**See Also:** Vector.trimToSize()

---

#### trimToSize

public void trimToSize()

Trims the capacity of this list to be the list's current size.

ensureCapacity

```java
public void ensureCapacity​(int minCapacity)
```

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

**Parameters:** minCapacity

- the desired minimum capacity
**See Also:** Vector.ensureCapacity(int)

---

#### ensureCapacity

public void ensureCapacity​(int minCapacity)

Increases the capacity of this list, if necessary, to ensure
that it can hold at least the number of components specified by
the minimum capacity argument.

setSize

```java
public void setSize​(int newSize)
```

Sets the size of this list.

**Parameters:** newSize

- the new size of this list
**See Also:** Vector.setSize(int)

---

#### setSize

public void setSize​(int newSize)

Sets the size of this list.

capacity

```java
public int capacity()
```

Returns the current capacity of this list.

**Returns:** the current capacity
**See Also:** Vector.capacity()

---

#### capacity

public int capacity()

Returns the current capacity of this list.

size

```java
public int size()
```

Returns the number of components in this list.

**Returns:** the number of components in this list
**See Also:** Vector.size()

---

#### size

public int size()

Returns the number of components in this list.

isEmpty

```java
public boolean isEmpty()
```

Tests whether this list has any components.

**Returns:** true

if and only if this list has
no components, that is, its size is zero;

false

otherwise
**See Also:** Vector.isEmpty()

---

#### isEmpty

public boolean isEmpty()

Tests whether this list has any components.

elements

```java
public
Enumeration
<
E
> elements()
```

Returns an enumeration of the components of this list.

**Returns:** an enumeration of the components of this list
**See Also:** Vector.elements()

---

#### elements

public

Enumeration

<

E

> elements()

Returns an enumeration of the components of this list.

contains

```java
public boolean contains​(
Object
elem)
```

Tests whether the specified object is a component in this list.

**Parameters:** elem

- an object
**Returns:** true

if the specified object
is the same as a component in this list
**See Also:** Vector.contains(Object)

---

#### contains

public boolean contains​(

Object

elem)

Tests whether the specified object is a component in this list.

indexOf

```java
public int indexOf​(
Object
elem)
```

Searches for the first occurrence of

elem

.

**Parameters:** elem

- an object
**Returns:** the index of the first occurrence of the argument in this
list; returns

-1

if the object is not found
**See Also:** Vector.indexOf(Object)

---

#### indexOf

public int indexOf​(

Object

elem)

Searches for the first occurrence of

elem

.

indexOf

```java
public int indexOf​(
Object
elem,
int index)
```

Searches for the first occurrence of

elem

, beginning
the search at

index

.

**Parameters:** elem

- the desired component
**Parameters:** index

- the index from which to begin searching
**Returns:** the index where the first occurrence of

elem

is found after

index

; returns

-1

if the

elem

is not found in the list
**See Also:** Vector.indexOf(Object,int)

---

#### indexOf

public int indexOf​(

Object

elem,
int index)

Searches for the first occurrence of

elem

, beginning
the search at

index

.

lastIndexOf

```java
public int lastIndexOf​(
Object
elem)
```

Returns the index of the last occurrence of

elem

.

**Parameters:** elem

- the desired component
**Returns:** the index of the last occurrence of

elem

in the list; returns

elem

if the object is not found
**See Also:** Vector.lastIndexOf(Object)

---

#### lastIndexOf

public int lastIndexOf​(

Object

elem)

Returns the index of the last occurrence of

elem

.

lastIndexOf

```java
public int lastIndexOf​(
Object
elem,
int index)
```

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

**Parameters:** elem

- the desired component
**Parameters:** index

- the index to start searching from
**Returns:** the index of the last occurrence of the

elem

in this list at position less than

index

;
returns

-1

if the object is not found
**See Also:** Vector.lastIndexOf(Object,int)

---

#### lastIndexOf

public int lastIndexOf​(

Object

elem,
int index)

Searches backwards for

elem

, starting from the
specified index, and returns an index to it.

elementAt

```java
public
E
elementAt​(int index)
```

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- an index into this list
**Returns:** the component at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the index
is negative or not less than the size of the list
**See Also:** get(int)

,

Vector.elementAt(int)

---

#### elementAt

public

E

elementAt​(int index)

Returns the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

get(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

firstElement

```java
public
E
firstElement()
```

Returns the first component of this list.

**Returns:** the first component of this list
**Throws:** NoSuchElementException

- if this
vector has no components
**See Also:** Vector.firstElement()

---

#### firstElement

public

E

firstElement()

Returns the first component of this list.

lastElement

```java
public
E
lastElement()
```

Returns the last component of the list.

**Returns:** the last component of the list
**Throws:** NoSuchElementException

- if this vector
has no components
**See Also:** Vector.lastElement()

---

#### lastElement

public

E

lastElement()

Returns the last component of the list.

setElementAt

```java
public void setElementAt​(
E
element,
int index)
```

Sets the component at the specified

index

of this
list to be the specified element. The previous component at that
position is discarded.

Note:

Although this method is not deprecated, the preferred
method to use is

set(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** element

- what the component is to be set to
**Parameters:** index

- the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the index is invalid
**See Also:** set(int,Object)

,

Vector.setElementAt(Object,int)

---

#### setElementAt

public void setElementAt​(

E

element,
int index)

Sets the component at the specified

index

of this
list to be the specified element. The previous component at that
position is discarded.

Note:

Although this method is not deprecated, the preferred
method to use is

set(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

removeElementAt

```java
public void removeElementAt​(int index)
```

Deletes the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

remove(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** index

- the index of the object to remove
**Throws:** ArrayIndexOutOfBoundsException

- if the index is invalid
**See Also:** remove(int)

,

Vector.removeElementAt(int)

---

#### removeElementAt

public void removeElementAt​(int index)

Deletes the component at the specified index.

Note:

Although this method is not deprecated, the preferred
method to use is

remove(int)

, which implements the

List

interface defined in the 1.2 Collections framework.

insertElementAt

```java
public void insertElementAt​(
E
element,
int index)
```

Inserts the specified element as a component in this list at the
specified

index

.

Note:

Although this method is not deprecated, the preferred
method to use is

add(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

**Parameters:** element

- the component to insert
**Parameters:** index

- where to insert the new component
**Throws:** ArrayIndexOutOfBoundsException

- if the index was invalid
**See Also:** add(int,Object)

,

Vector.insertElementAt(Object,int)

---

#### insertElementAt

public void insertElementAt​(

E

element,
int index)

Inserts the specified element as a component in this list at the
specified

index

.

Note:

Although this method is not deprecated, the preferred
method to use is

add(int,Object)

, which implements the

List

interface defined in the 1.2 Collections framework.

addElement

```java
public void addElement​(
E
element)
```

Adds the specified component to the end of this list.

**Parameters:** element

- the component to be added
**See Also:** Vector.addElement(Object)

---

#### addElement

public void addElement​(

E

element)

Adds the specified component to the end of this list.

removeElement

```java
public boolean removeElement​(
Object
obj)
```

Removes the first (lowest-indexed) occurrence of the argument
from this list.

**Parameters:** obj

- the component to be removed
**Returns:** true

if the argument was a component of this
list;

false

otherwise
**See Also:** Vector.removeElement(Object)

---

#### removeElement

public boolean removeElement​(

Object

obj)

Removes the first (lowest-indexed) occurrence of the argument
from this list.

removeAllElements

```java
public void removeAllElements()
```

Removes all components from this list and sets its size to zero.

Note:

Although this method is not deprecated, the preferred
method to use is

clear

, which implements the

List

interface defined in the 1.2 Collections framework.

**See Also:** clear()

,

Vector.removeAllElements()

---

#### removeAllElements

public void removeAllElements()

Removes all components from this list and sets its size to zero.

Note:

Although this method is not deprecated, the preferred
method to use is

clear

, which implements the

List

interface defined in the 1.2 Collections framework.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

toArray

```java
public
Object
[] toArray()
```

Returns an array containing all of the elements in this list in the
correct order.

**Returns:** an array containing the elements of the list
**See Also:** Vector.toArray()

---

#### toArray

public

Object

[] toArray()

Returns an array containing all of the elements in this list in the
correct order.

get

```java
public
E
get​(int index)
```

Returns the element at the specified position in this list.

**Parameters:** index

- index of element to return
**Returns:** the element at the specified position in this list
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

---

#### get

public

E

get​(int index)

Returns the element at the specified position in this list.

set

```java
public
E
set​(int index,

E
element)
```

Replaces the element at the specified position in this list with the
specified element.

**Parameters:** index

- index of element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

---

#### set

public

E

set​(int index,

E

element)

Replaces the element at the specified position in this list with the
specified element.

add

```java
public void add​(int index,

E
element)
```

Inserts the specified element at the specified position in this list.

**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt; size()

)

---

#### add

public void add​(int index,

E

element)

Inserts the specified element at the specified position in this list.

remove

```java
public
E
remove​(int index)
```

Removes the element at the specified position in this list.
Returns the element that was removed from the list

**Parameters:** index

- the index of the element to removed
**Returns:** the element previously at the specified position
**Throws:** ArrayIndexOutOfBoundsException

- if the index is out of range
(

index &lt; 0 || index &gt;= size()

)

---

#### remove

public

E

remove​(int index)

Removes the element at the specified position in this list.
Returns the element that was removed from the list

clear

```java
public void clear()
```

Removes all of the elements from this list. The list will
be empty after this call returns (unless it throws an exception).

---

#### clear

public void clear()

Removes all of the elements from this list. The list will
be empty after this call returns (unless it throws an exception).

removeRange

```java
public void removeRange​(int fromIndex,
int toIndex)
```

Deletes the components at the specified range of indexes.
The removal is inclusive, so specifying a range of (1,5)
removes the component at index 1 and the component at index 5,
as well as all components in between.

**Parameters:** fromIndex

- the index of the lower end of the range
**Parameters:** toIndex

- the index of the upper end of the range
**Throws:** ArrayIndexOutOfBoundsException

- if the index was invalid
**Throws:** IllegalArgumentException

- if

fromIndex &gt; toIndex
**See Also:** remove(int)

---

#### removeRange

public void removeRange​(int fromIndex,
int toIndex)

Deletes the components at the specified range of indexes.
The removal is inclusive, so specifying a range of (1,5)
removes the component at index 1 and the component at index 5,
as well as all components in between.

addAll

```java
public void addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements present in the collection to the list.

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

Adds all of the elements present in the collection to the list.

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

