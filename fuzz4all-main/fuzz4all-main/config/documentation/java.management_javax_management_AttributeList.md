# Class AttributeList

**Source:** `java.management\javax\management\AttributeList.html`

### Class Description

```java
public class
AttributeList

extends
ArrayList
<
Object
>
```

Represents a list of values for attributes of an MBean. See the

getAttributes

and

setAttributes

methods of

MBeanServer

and

MBeanServerConnection

.

For compatibility reasons, it is possible, though
highly discouraged, to add objects to an

AttributeList

that are
not instances of

Attribute

. However, an

AttributeList

can be made

type-safe

, which means that an attempt to add
an object that is not an

Attribute

will produce an

IllegalArgumentException

. An

AttributeList

becomes type-safe
when the method

asList()

is called on it.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Iterable

<

Object

>

,

Collection

<

Object

>

,

List

<

Object

>

,

RandomAccess

---

### Field Details

*No entries found.*

### Constructor Details

#### public AttributeList()

Constructs an empty

AttributeList

.

---

#### public AttributeList​(int initialCapacity)

Constructs an empty

AttributeList

with
the initial capacity specified.

**Parameters:**
- initialCapacity

- the initial capacity of the

AttributeList

, as specified by

ArrayList(int)

.

---

#### public AttributeList​(
AttributeList
list)

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator. The

AttributeList

instance has an initial capacity of
110% of the size of the

AttributeList

specified.

**Parameters:**
- list

- the

AttributeList

that defines the initial
contents of the new

AttributeList

.

**See Also:**
- ArrayList(java.util.Collection)

---

#### public AttributeList​(
List
<
Attribute
> list)

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

**Parameters:**
- list

- the

List

that defines the initial contents of
the new

AttributeList

.

**Throws:**
- IllegalArgumentException

- if the

list

parameter
is

null

or if the

list

parameter contains any
non-Attribute objects.

**See Also:**
- ArrayList(java.util.Collection)

**Since:**
- 1.6

---

### Method Details

#### public
List
<
Attribute
> asList()

Return a view of this list as a

List<Attribute>

.
Changes to the returned value are reflected by changes
to the original

AttributeList

and vice versa.

**Returns:**
- a

List<Attribute>

whose contents
reflect the contents of this

AttributeList

.

If this method has ever been called on a given

AttributeList

instance, a subsequent attempt to add
an object to that instance which is not an

Attribute

will fail with an

IllegalArgumentException

. For compatibility
reasons, an

AttributeList

on which this method has never
been called does allow objects other than

Attribute

s to
be added.

**Throws:**
- IllegalArgumentException

- if this

AttributeList

contains
an element that is not an

Attribute

.

**Since:**
- 1.6

---

#### public void add​(
Attribute
object)

Adds the

Attribute

specified as the last element of the list.

**Parameters:**
- object

- The attribute to be added.

---

#### public void add​(int index,

Attribute
object)

Inserts the attribute specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up. If the index is out of range (index < 0 || index >
size()) a RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:**
- object

- The

Attribute

object to be inserted.
- index

- The position in the list where the new

Attribute

object is to be inserted.

---

#### public void set​(int index,

Attribute
object)

Sets the element at the position specified to be the attribute specified.
The previous element at that position is discarded. If the index is
out of range (index < 0 || index > size()) a RuntimeOperationsException
should be raised, wrapping the java.lang.IndexOutOfBoundsException thrown.

**Parameters:**
- object

- The value to which the attribute element should be set.
- index

- The position specified.

---

#### public boolean addAll​(
AttributeList
list)

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

**Parameters:**
- list

- Elements to be inserted into the list.

**Returns:**
- true if this list changed as a result of the call.

**See Also:**
- ArrayList.addAll(java.util.Collection)

---

#### public boolean addAll​(int index,

AttributeList
list)

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.
If the index is out of range (index < 0 || index > size()) a
RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:**
- list

- Elements to be inserted into the list.
- index

- Position at which to insert the first element from the

AttributeList

specified.

**Returns:**
- true if this list changed as a result of the call.

**See Also:**
- ArrayList.addAll(int, java.util.Collection)

---

#### public boolean add​(
Object
element)

Appends the specified element to the end of this list.

**Specified by:**
- add

in interface

Collection

<

Object

>
- add

in interface

List

<

Object

>

**Overrides:**
- add

in class

ArrayList

<

Object

>

**Parameters:**
- element

- element to be appended to this list

**Returns:**
- true

(as specified by

Collection.add(E)

)

**Throws:**
- IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

---

#### public void add​(int index,

Object
element)

Inserts the specified element at the specified position in this
list. Shifts the element currently at that position (if any) and
any subsequent elements to the right (adds one to their indices).

**Specified by:**
- add

in interface

List

<

Object

>

**Overrides:**
- add

in class

ArrayList

<

Object

>

**Parameters:**
- index

- index at which the specified element is to be inserted
- element

- element to be inserted

**Throws:**
- IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

---

#### public boolean addAll​(
Collection
<?> c)

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator. The behavior of this operation is
undefined if the specified collection is modified while the operation
is in progress. (This implies that the behavior of this call is
undefined if the specified collection is this list, and this
list is nonempty.)

**Specified by:**
- addAll

in interface

Collection

<

Object

>
- addAll

in interface

List

<

Object

>

**Overrides:**
- addAll

in class

ArrayList

<

Object

>

**Parameters:**
- c

- collection containing elements to be added to this list

**Returns:**
- true

if this list changed as a result of the call

**Throws:**
- IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.

**See Also:**
- AbstractCollection.add(Object)

---

#### public boolean addAll​(int index,

Collection
<?> c)

Inserts all of the elements in the specified collection into this
list, starting at the specified position. Shifts the element
currently at that position (if any) and any subsequent elements to
the right (increases their indices). The new elements will appear
in the list in the order that they are returned by the
specified collection's iterator.

**Specified by:**
- addAll

in interface

List

<

Object

>

**Overrides:**
- addAll

in class

ArrayList

<

Object

>

**Parameters:**
- index

- index at which to insert the first element from the
specified collection
- c

- collection containing elements to be added to this list

**Returns:**
- true

if this list changed as a result of the call

**Throws:**
- IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.

---

#### public
Object
set​(int index,

Object
element)

Replaces the element at the specified position in this list with
the specified element.

**Specified by:**
- set

in interface

List

<

Object

>

**Overrides:**
- set

in class

ArrayList

<

Object

>

**Parameters:**
- index

- index of the element to replace
- element

- element to be stored at the specified position

**Returns:**
- the element previously at the specified position

**Throws:**
- IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

---

### Additional Sections

#### Class AttributeList

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractList

<E>
- - java.util.ArrayList

<

Object

>
- - javax.management.AttributeList

java.util.AbstractCollection

<E>

- java.util.AbstractList

<E>
- - java.util.ArrayList

<

Object

>
- - javax.management.AttributeList

java.util.AbstractList

<E>

- java.util.ArrayList

<

Object

>
- - javax.management.AttributeList

java.util.ArrayList

<

Object

>

- javax.management.AttributeList

javax.management.AttributeList

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Iterable

<

Object

>

,

Collection

<

Object

>

,

List

<

Object

>

,

RandomAccess

```java
public class
AttributeList

extends
ArrayList
<
Object
>
```

Represents a list of values for attributes of an MBean. See the

getAttributes

and

setAttributes

methods of

MBeanServer

and

MBeanServerConnection

.

For compatibility reasons, it is possible, though
highly discouraged, to add objects to an

AttributeList

that are
not instances of

Attribute

. However, an

AttributeList

can be made

type-safe

, which means that an attempt to add
an object that is not an

Attribute

will produce an

IllegalArgumentException

. An

AttributeList

becomes type-safe
when the method

asList()

is called on it.

**Since:** 1.5
**See Also:** Serialized Form

public class

AttributeList

extends

ArrayList

<

Object

>

Represents a list of values for attributes of an MBean. See the

getAttributes

and

setAttributes

methods of

MBeanServer

and

MBeanServerConnection

.

For compatibility reasons, it is possible, though
highly discouraged, to add objects to an

AttributeList

that are
not instances of

Attribute

. However, an

AttributeList

can be made

type-safe

, which means that an attempt to add
an object that is not an

Attribute

will produce an

IllegalArgumentException

. An

AttributeList

becomes type-safe
when the method

asList()

is called on it.

Represents a list of values for attributes of an MBean. See the

getAttributes

and

setAttributes

methods of

MBeanServer

and

MBeanServerConnection

.

For compatibility reasons, it is possible, though
highly discouraged, to add objects to an

AttributeList

that are
not instances of

Attribute

. However, an

AttributeList

can be made

type-safe

, which means that an attempt to add
an object that is not an

Attribute

will produce an

IllegalArgumentException

. An

AttributeList

becomes type-safe
when the method

asList()

is called on it.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

AbstractList

modCount

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AttributeList

()

Constructs an empty

AttributeList

.

AttributeList

​(int initialCapacity)

Constructs an empty

AttributeList

with
the initial capacity specified.

AttributeList

​(

List

<

Attribute

> list)

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

AttributeList

​(

AttributeList

list)

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator.

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

Object

element)

Inserts the specified element at the specified position in this
list.

void

add

​(int index,

Attribute

object)

Inserts the attribute specified as an element at the position specified.

boolean

add

​(

Object

element)

Appends the specified element to the end of this list.

void

add

​(

Attribute

object)

Adds the

Attribute

specified as the last element of the list.

boolean

addAll

​(int index,

Collection

<?> c)

Inserts all of the elements in the specified collection into this
list, starting at the specified position.

boolean

addAll

​(int index,

AttributeList

list)

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.

boolean

addAll

​(

Collection

<?> c)

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator.

boolean

addAll

​(

AttributeList

list)

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

List

<

Attribute

>

asList

()

Return a view of this list as a

List<Attribute>

.

Object

set

​(int index,

Object

element)

Replaces the element at the specified position in this list with
the specified element.

void

set

​(int index,

Attribute

object)

Sets the element at the position specified to be the attribute specified.

- Methods declared in class java.util.

ArrayList

clear

,

clone

,

contains

,

ensureCapacity

,

forEach

,

get

,

indexOf

,

isEmpty

,

iterator

,

lastIndexOf

,

listIterator

,

listIterator

,

remove

,

remove

,

removeAll

,

removeIf

,

removeRange

,

retainAll

,

size

,

spliterator

,

subList

,

toArray

,

toArray

,

trimToSize

- Methods declared in class java.util.

AbstractList

equals

,

hashCode

- Methods declared in class java.util.

AbstractCollection

containsAll

,

toString

- Methods declared in class java.lang.

Object

finalize

,

getClass

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

- Methods declared in interface java.util.

Collection

parallelStream

,

stream

,

toArray

- Methods declared in interface java.util.

List

containsAll

,

equals

,

hashCode

,

replaceAll

,

sort

Field Summary

- Fields declared in class java.util.

AbstractList

modCount

---

#### Field Summary

Fields declared in class java.util.

AbstractList

modCount

---

#### Fields declared in class java.util. AbstractList

Constructor Summary

Constructors

Constructor

Description

AttributeList

()

Constructs an empty

AttributeList

.

AttributeList

​(int initialCapacity)

Constructs an empty

AttributeList

with
the initial capacity specified.

AttributeList

​(

List

<

Attribute

> list)

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

AttributeList

​(

AttributeList

list)

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator.

---

#### Constructor Summary

Constructs an empty

AttributeList

.

Constructs an empty

AttributeList

with
the initial capacity specified.

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator.

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

Object

element)

Inserts the specified element at the specified position in this
list.

void

add

​(int index,

Attribute

object)

Inserts the attribute specified as an element at the position specified.

boolean

add

​(

Object

element)

Appends the specified element to the end of this list.

void

add

​(

Attribute

object)

Adds the

Attribute

specified as the last element of the list.

boolean

addAll

​(int index,

Collection

<?> c)

Inserts all of the elements in the specified collection into this
list, starting at the specified position.

boolean

addAll

​(int index,

AttributeList

list)

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.

boolean

addAll

​(

Collection

<?> c)

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator.

boolean

addAll

​(

AttributeList

list)

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

List

<

Attribute

>

asList

()

Return a view of this list as a

List<Attribute>

.

Object

set

​(int index,

Object

element)

Replaces the element at the specified position in this list with
the specified element.

void

set

​(int index,

Attribute

object)

Sets the element at the position specified to be the attribute specified.

- Methods declared in class java.util.

ArrayList

clear

,

clone

,

contains

,

ensureCapacity

,

forEach

,

get

,

indexOf

,

isEmpty

,

iterator

,

lastIndexOf

,

listIterator

,

listIterator

,

remove

,

remove

,

removeAll

,

removeIf

,

removeRange

,

retainAll

,

size

,

spliterator

,

subList

,

toArray

,

toArray

,

trimToSize

- Methods declared in class java.util.

AbstractList

equals

,

hashCode

- Methods declared in class java.util.

AbstractCollection

containsAll

,

toString

- Methods declared in class java.lang.

Object

finalize

,

getClass

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

- Methods declared in interface java.util.

Collection

parallelStream

,

stream

,

toArray

- Methods declared in interface java.util.

List

containsAll

,

equals

,

hashCode

,

replaceAll

,

sort

---

#### Method Summary

Inserts the specified element at the specified position in this
list.

Inserts the attribute specified as an element at the position specified.

Appends the specified element to the end of this list.

Adds the

Attribute

specified as the last element of the list.

Inserts all of the elements in the specified collection into this
list, starting at the specified position.

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator.

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

Return a view of this list as a

List<Attribute>

.

Replaces the element at the specified position in this list with
the specified element.

Sets the element at the position specified to be the attribute specified.

Methods declared in class java.util.

ArrayList

clear

,

clone

,

contains

,

ensureCapacity

,

forEach

,

get

,

indexOf

,

isEmpty

,

iterator

,

lastIndexOf

,

listIterator

,

listIterator

,

remove

,

remove

,

removeAll

,

removeIf

,

removeRange

,

retainAll

,

size

,

spliterator

,

subList

,

toArray

,

toArray

,

trimToSize

---

#### Methods declared in class java.util. ArrayList

Methods declared in class java.util.

AbstractList

equals

,

hashCode

---

#### Methods declared in class java.util. AbstractList

Methods declared in class java.util.

AbstractCollection

containsAll

,

toString

---

#### Methods declared in class java.util. AbstractCollection

Methods declared in class java.lang.

Object

finalize

,

getClass

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

Methods declared in interface java.util.

Collection

parallelStream

,

stream

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.util.

List

containsAll

,

equals

,

hashCode

,

replaceAll

,

sort

---

#### Methods declared in interface java.util. List

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AttributeList

```java
public AttributeList()
```

Constructs an empty

AttributeList

.

- AttributeList

```java
public AttributeList​(int initialCapacity)
```

Constructs an empty

AttributeList

with
the initial capacity specified.

**Parameters:** initialCapacity

- the initial capacity of the

AttributeList

, as specified by

ArrayList(int)

.

- AttributeList

```java
public AttributeList​(
AttributeList
list)
```

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator. The

AttributeList

instance has an initial capacity of
110% of the size of the

AttributeList

specified.

**Parameters:** list

- the

AttributeList

that defines the initial
contents of the new

AttributeList

.
**See Also:** ArrayList(java.util.Collection)

- AttributeList

```java
public AttributeList​(
List
<
Attribute
> list)
```

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

**Parameters:** list

- the

List

that defines the initial contents of
the new

AttributeList

.
**Throws:** IllegalArgumentException

- if the

list

parameter
is

null

or if the

list

parameter contains any
non-Attribute objects.
**Since:** 1.6
**See Also:** ArrayList(java.util.Collection)

============ METHOD DETAIL ==========

- Method Detail

- asList

```java
public
List
<
Attribute
> asList()
```

Return a view of this list as a

List<Attribute>

.
Changes to the returned value are reflected by changes
to the original

AttributeList

and vice versa.

**Returns:** a

List<Attribute>

whose contents
reflect the contents of this

AttributeList

.

If this method has ever been called on a given

AttributeList

instance, a subsequent attempt to add
an object to that instance which is not an

Attribute

will fail with an

IllegalArgumentException

. For compatibility
reasons, an

AttributeList

on which this method has never
been called does allow objects other than

Attribute

s to
be added.
**Throws:** IllegalArgumentException

- if this

AttributeList

contains
an element that is not an

Attribute

.
**Since:** 1.6

- add

```java
public void add​(
Attribute
object)
```

Adds the

Attribute

specified as the last element of the list.

**Parameters:** object

- The attribute to be added.

- add

```java
public void add​(int index,

Attribute
object)
```

Inserts the attribute specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up. If the index is out of range (index < 0 || index >
size()) a RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:** object

- The

Attribute

object to be inserted.
**Parameters:** index

- The position in the list where the new

Attribute

object is to be inserted.

- set

```java
public void set​(int index,

Attribute
object)
```

Sets the element at the position specified to be the attribute specified.
The previous element at that position is discarded. If the index is
out of range (index < 0 || index > size()) a RuntimeOperationsException
should be raised, wrapping the java.lang.IndexOutOfBoundsException thrown.

**Parameters:** object

- The value to which the attribute element should be set.
**Parameters:** index

- The position specified.

- addAll

```java
public boolean addAll​(
AttributeList
list)
```

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

**Parameters:** list

- Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**See Also:** ArrayList.addAll(java.util.Collection)

- addAll

```java
public boolean addAll​(int index,

AttributeList
list)
```

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.
If the index is out of range (index < 0 || index > size()) a
RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:** list

- Elements to be inserted into the list.
**Parameters:** index

- Position at which to insert the first element from the

AttributeList

specified.
**Returns:** true if this list changed as a result of the call.
**See Also:** ArrayList.addAll(int, java.util.Collection)

- add

```java
public boolean add​(
Object
element)
```

Appends the specified element to the end of this list.

**Specified by:** add

in interface

Collection

<

Object

>
**Specified by:** add

in interface

List

<

Object

>
**Overrides:** add

in class

ArrayList

<

Object

>
**Parameters:** element

- element to be appended to this list
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

- add

```java
public void add​(int index,

Object
element)
```

Inserts the specified element at the specified position in this
list. Shifts the element currently at that position (if any) and
any subsequent elements to the right (adds one to their indices).

**Specified by:** add

in interface

List

<

Object

>
**Overrides:** add

in class

ArrayList

<

Object

>
**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

- addAll

```java
public boolean addAll​(
Collection
<?> c)
```

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator. The behavior of this operation is
undefined if the specified collection is modified while the operation
is in progress. (This implies that the behavior of this call is
undefined if the specified collection is this list, and this
list is nonempty.)

**Specified by:** addAll

in interface

Collection

<

Object

>
**Specified by:** addAll

in interface

List

<

Object

>
**Overrides:** addAll

in class

ArrayList

<

Object

>
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.
**See Also:** AbstractCollection.add(Object)

- addAll

```java
public boolean addAll​(int index,

Collection
<?> c)
```

Inserts all of the elements in the specified collection into this
list, starting at the specified position. Shifts the element
currently at that position (if any) and any subsequent elements to
the right (increases their indices). The new elements will appear
in the list in the order that they are returned by the
specified collection's iterator.

**Specified by:** addAll

in interface

List

<

Object

>
**Overrides:** addAll

in class

ArrayList

<

Object

>
**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.

- set

```java
public
Object
set​(int index,

Object
element)
```

Replaces the element at the specified position in this list with
the specified element.

**Specified by:** set

in interface

List

<

Object

>
**Overrides:** set

in class

ArrayList

<

Object

>
**Parameters:** index

- index of the element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

Constructor Detail

- AttributeList

```java
public AttributeList()
```

Constructs an empty

AttributeList

.

- AttributeList

```java
public AttributeList​(int initialCapacity)
```

Constructs an empty

AttributeList

with
the initial capacity specified.

**Parameters:** initialCapacity

- the initial capacity of the

AttributeList

, as specified by

ArrayList(int)

.

- AttributeList

```java
public AttributeList​(
AttributeList
list)
```

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator. The

AttributeList

instance has an initial capacity of
110% of the size of the

AttributeList

specified.

**Parameters:** list

- the

AttributeList

that defines the initial
contents of the new

AttributeList

.
**See Also:** ArrayList(java.util.Collection)

- AttributeList

```java
public AttributeList​(
List
<
Attribute
> list)
```

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

**Parameters:** list

- the

List

that defines the initial contents of
the new

AttributeList

.
**Throws:** IllegalArgumentException

- if the

list

parameter
is

null

or if the

list

parameter contains any
non-Attribute objects.
**Since:** 1.6
**See Also:** ArrayList(java.util.Collection)

---

#### Constructor Detail

AttributeList

```java
public AttributeList()
```

Constructs an empty

AttributeList

.

---

#### AttributeList

public AttributeList()

Constructs an empty

AttributeList

.

AttributeList

```java
public AttributeList​(int initialCapacity)
```

Constructs an empty

AttributeList

with
the initial capacity specified.

**Parameters:** initialCapacity

- the initial capacity of the

AttributeList

, as specified by

ArrayList(int)

.

---

#### AttributeList

public AttributeList​(int initialCapacity)

Constructs an empty

AttributeList

with
the initial capacity specified.

AttributeList

```java
public AttributeList​(
AttributeList
list)
```

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator. The

AttributeList

instance has an initial capacity of
110% of the size of the

AttributeList

specified.

**Parameters:** list

- the

AttributeList

that defines the initial
contents of the new

AttributeList

.
**See Also:** ArrayList(java.util.Collection)

---

#### AttributeList

public AttributeList​(

AttributeList

list)

Constructs an

AttributeList

containing the
elements of the

AttributeList

specified, in the
order in which they are returned by the

AttributeList

's iterator. The

AttributeList

instance has an initial capacity of
110% of the size of the

AttributeList

specified.

AttributeList

```java
public AttributeList​(
List
<
Attribute
> list)
```

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

**Parameters:** list

- the

List

that defines the initial contents of
the new

AttributeList

.
**Throws:** IllegalArgumentException

- if the

list

parameter
is

null

or if the

list

parameter contains any
non-Attribute objects.
**Since:** 1.6
**See Also:** ArrayList(java.util.Collection)

---

#### AttributeList

public AttributeList​(

List

<

Attribute

> list)

Constructs an

AttributeList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

Method Detail

- asList

```java
public
List
<
Attribute
> asList()
```

Return a view of this list as a

List<Attribute>

.
Changes to the returned value are reflected by changes
to the original

AttributeList

and vice versa.

**Returns:** a

List<Attribute>

whose contents
reflect the contents of this

AttributeList

.

If this method has ever been called on a given

AttributeList

instance, a subsequent attempt to add
an object to that instance which is not an

Attribute

will fail with an

IllegalArgumentException

. For compatibility
reasons, an

AttributeList

on which this method has never
been called does allow objects other than

Attribute

s to
be added.
**Throws:** IllegalArgumentException

- if this

AttributeList

contains
an element that is not an

Attribute

.
**Since:** 1.6

- add

```java
public void add​(
Attribute
object)
```

Adds the

Attribute

specified as the last element of the list.

**Parameters:** object

- The attribute to be added.

- add

```java
public void add​(int index,

Attribute
object)
```

Inserts the attribute specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up. If the index is out of range (index < 0 || index >
size()) a RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:** object

- The

Attribute

object to be inserted.
**Parameters:** index

- The position in the list where the new

Attribute

object is to be inserted.

- set

```java
public void set​(int index,

Attribute
object)
```

Sets the element at the position specified to be the attribute specified.
The previous element at that position is discarded. If the index is
out of range (index < 0 || index > size()) a RuntimeOperationsException
should be raised, wrapping the java.lang.IndexOutOfBoundsException thrown.

**Parameters:** object

- The value to which the attribute element should be set.
**Parameters:** index

- The position specified.

- addAll

```java
public boolean addAll​(
AttributeList
list)
```

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

**Parameters:** list

- Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**See Also:** ArrayList.addAll(java.util.Collection)

- addAll

```java
public boolean addAll​(int index,

AttributeList
list)
```

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.
If the index is out of range (index < 0 || index > size()) a
RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:** list

- Elements to be inserted into the list.
**Parameters:** index

- Position at which to insert the first element from the

AttributeList

specified.
**Returns:** true if this list changed as a result of the call.
**See Also:** ArrayList.addAll(int, java.util.Collection)

- add

```java
public boolean add​(
Object
element)
```

Appends the specified element to the end of this list.

**Specified by:** add

in interface

Collection

<

Object

>
**Specified by:** add

in interface

List

<

Object

>
**Overrides:** add

in class

ArrayList

<

Object

>
**Parameters:** element

- element to be appended to this list
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

- add

```java
public void add​(int index,

Object
element)
```

Inserts the specified element at the specified position in this
list. Shifts the element currently at that position (if any) and
any subsequent elements to the right (adds one to their indices).

**Specified by:** add

in interface

List

<

Object

>
**Overrides:** add

in class

ArrayList

<

Object

>
**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

- addAll

```java
public boolean addAll​(
Collection
<?> c)
```

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator. The behavior of this operation is
undefined if the specified collection is modified while the operation
is in progress. (This implies that the behavior of this call is
undefined if the specified collection is this list, and this
list is nonempty.)

**Specified by:** addAll

in interface

Collection

<

Object

>
**Specified by:** addAll

in interface

List

<

Object

>
**Overrides:** addAll

in class

ArrayList

<

Object

>
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.
**See Also:** AbstractCollection.add(Object)

- addAll

```java
public boolean addAll​(int index,

Collection
<?> c)
```

Inserts all of the elements in the specified collection into this
list, starting at the specified position. Shifts the element
currently at that position (if any) and any subsequent elements to
the right (increases their indices). The new elements will appear
in the list in the order that they are returned by the
specified collection's iterator.

**Specified by:** addAll

in interface

List

<

Object

>
**Overrides:** addAll

in class

ArrayList

<

Object

>
**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.

- set

```java
public
Object
set​(int index,

Object
element)
```

Replaces the element at the specified position in this list with
the specified element.

**Specified by:** set

in interface

List

<

Object

>
**Overrides:** set

in class

ArrayList

<

Object

>
**Parameters:** index

- index of the element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

---

#### Method Detail

asList

```java
public
List
<
Attribute
> asList()
```

Return a view of this list as a

List<Attribute>

.
Changes to the returned value are reflected by changes
to the original

AttributeList

and vice versa.

**Returns:** a

List<Attribute>

whose contents
reflect the contents of this

AttributeList

.

If this method has ever been called on a given

AttributeList

instance, a subsequent attempt to add
an object to that instance which is not an

Attribute

will fail with an

IllegalArgumentException

. For compatibility
reasons, an

AttributeList

on which this method has never
been called does allow objects other than

Attribute

s to
be added.
**Throws:** IllegalArgumentException

- if this

AttributeList

contains
an element that is not an

Attribute

.
**Since:** 1.6

---

#### asList

public

List

<

Attribute

> asList()

Return a view of this list as a

List<Attribute>

.
Changes to the returned value are reflected by changes
to the original

AttributeList

and vice versa.

If this method has ever been called on a given

AttributeList

instance, a subsequent attempt to add
an object to that instance which is not an

Attribute

will fail with an

IllegalArgumentException

. For compatibility
reasons, an

AttributeList

on which this method has never
been called does allow objects other than

Attribute

s to
be added.

add

```java
public void add​(
Attribute
object)
```

Adds the

Attribute

specified as the last element of the list.

**Parameters:** object

- The attribute to be added.

---

#### add

public void add​(

Attribute

object)

Adds the

Attribute

specified as the last element of the list.

add

```java
public void add​(int index,

Attribute
object)
```

Inserts the attribute specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up. If the index is out of range (index < 0 || index >
size()) a RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:** object

- The

Attribute

object to be inserted.
**Parameters:** index

- The position in the list where the new

Attribute

object is to be inserted.

---

#### add

public void add​(int index,

Attribute

object)

Inserts the attribute specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up. If the index is out of range (index < 0 || index >
size()) a RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

set

```java
public void set​(int index,

Attribute
object)
```

Sets the element at the position specified to be the attribute specified.
The previous element at that position is discarded. If the index is
out of range (index < 0 || index > size()) a RuntimeOperationsException
should be raised, wrapping the java.lang.IndexOutOfBoundsException thrown.

**Parameters:** object

- The value to which the attribute element should be set.
**Parameters:** index

- The position specified.

---

#### set

public void set​(int index,

Attribute

object)

Sets the element at the position specified to be the attribute specified.
The previous element at that position is discarded. If the index is
out of range (index < 0 || index > size()) a RuntimeOperationsException
should be raised, wrapping the java.lang.IndexOutOfBoundsException thrown.

addAll

```java
public boolean addAll​(
AttributeList
list)
```

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

**Parameters:** list

- Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**See Also:** ArrayList.addAll(java.util.Collection)

---

#### addAll

public boolean addAll​(

AttributeList

list)

Appends all the elements in the

AttributeList

specified to
the end of the list, in the order in which they are returned by the
Iterator of the

AttributeList

specified.

addAll

```java
public boolean addAll​(int index,

AttributeList
list)
```

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.
If the index is out of range (index < 0 || index > size()) a
RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

**Parameters:** list

- Elements to be inserted into the list.
**Parameters:** index

- Position at which to insert the first element from the

AttributeList

specified.
**Returns:** true if this list changed as a result of the call.
**See Also:** ArrayList.addAll(int, java.util.Collection)

---

#### addAll

public boolean addAll​(int index,

AttributeList

list)

Inserts all of the elements in the

AttributeList

specified
into this list, starting at the specified position, in the order in which
they are returned by the Iterator of the

AttributeList

specified.
If the index is out of range (index < 0 || index > size()) a
RuntimeOperationsException should be raised, wrapping the
java.lang.IndexOutOfBoundsException thrown.

add

```java
public boolean add​(
Object
element)
```

Appends the specified element to the end of this list.

**Specified by:** add

in interface

Collection

<

Object

>
**Specified by:** add

in interface

List

<

Object

>
**Overrides:** add

in class

ArrayList

<

Object

>
**Parameters:** element

- element to be appended to this list
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

---

#### add

public boolean add​(

Object

element)

Appends the specified element to the end of this list.

add

```java
public void add​(int index,

Object
element)
```

Inserts the specified element at the specified position in this
list. Shifts the element currently at that position (if any) and
any subsequent elements to the right (adds one to their indices).

**Specified by:** add

in interface

List

<

Object

>
**Overrides:** add

in class

ArrayList

<

Object

>
**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

---

#### add

public void add​(int index,

Object

element)

Inserts the specified element at the specified position in this
list. Shifts the element currently at that position (if any) and
any subsequent elements to the right (adds one to their indices).

addAll

```java
public boolean addAll​(
Collection
<?> c)
```

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator. The behavior of this operation is
undefined if the specified collection is modified while the operation
is in progress. (This implies that the behavior of this call is
undefined if the specified collection is this list, and this
list is nonempty.)

**Specified by:** addAll

in interface

Collection

<

Object

>
**Specified by:** addAll

in interface

List

<

Object

>
**Overrides:** addAll

in class

ArrayList

<

Object

>
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.
**See Also:** AbstractCollection.add(Object)

---

#### addAll

public boolean addAll​(

Collection

<?> c)

Appends all of the elements in the specified collection to the end of
this list, in the order that they are returned by the
specified collection's Iterator. The behavior of this operation is
undefined if the specified collection is modified while the operation
is in progress. (This implies that the behavior of this call is
undefined if the specified collection is this list, and this
list is nonempty.)

addAll

```java
public boolean addAll​(int index,

Collection
<?> c)
```

Inserts all of the elements in the specified collection into this
list, starting at the specified position. Shifts the element
currently at that position (if any) and any subsequent elements to
the right (increases their indices). The new elements will appear
in the list in the order that they are returned by the
specified collection's iterator.

**Specified by:** addAll

in interface

List

<

Object

>
**Overrides:** addAll

in class

ArrayList

<

Object

>
**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

c

contains an
element that is not an

Attribute

.

---

#### addAll

public boolean addAll​(int index,

Collection

<?> c)

Inserts all of the elements in the specified collection into this
list, starting at the specified position. Shifts the element
currently at that position (if any) and any subsequent elements to
the right (increases their indices). The new elements will appear
in the list in the order that they are returned by the
specified collection's iterator.

set

```java
public
Object
set​(int index,

Object
element)
```

Replaces the element at the specified position in this list with
the specified element.

**Specified by:** set

in interface

List

<

Object

>
**Overrides:** set

in class

ArrayList

<

Object

>
**Parameters:** index

- index of the element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** IllegalArgumentException

- if this

AttributeList

is

type-safe

and

element

is not an

Attribute

.

---

#### set

public

Object

set​(int index,

Object

element)

Replaces the element at the specified position in this list with
the specified element.

---

