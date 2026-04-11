# Class RoleUnresolvedList

**Source:** `java.management\javax\management\relation\RoleUnresolvedList.html`

### Class Description

```java
public class
RoleUnresolvedList

extends
ArrayList
<
Object
>
```

A RoleUnresolvedList represents a list of RoleUnresolved objects,
representing roles not retrieved from a relation due to a problem
encountered when trying to access (read or write) the roles.

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

#### public RoleUnresolvedList()

Constructs an empty RoleUnresolvedList.

---

#### public RoleUnresolvedList​(int initialCapacity)

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

**Parameters:**
- initialCapacity

- initial capacity

---

#### public RoleUnresolvedList​(
List
<
RoleUnresolved
> list)
throws
IllegalArgumentException

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleUnresolvedList

instance has
an initial capacity of 110% of the size of the

List

specified.

**Parameters:**
- list

- the

List

that defines the initial contents of
the new

RoleUnresolvedList

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
non-RoleUnresolved objects.

**See Also:**
- ArrayList(java.util.Collection)

---

### Method Details

#### public
List
<
RoleUnresolved
> asList()

Return a view of this list as a

List<RoleUnresolved>

.
Changes to the returned value are reflected by changes
to the original

RoleUnresolvedList

and vice versa.

**Returns:**
- a

List<RoleUnresolved>

whose contents
reflect the contents of this

RoleUnresolvedList

.

If this method has ever been called on a given

RoleUnresolvedList

instance, a subsequent attempt to add
an object to that instance which is not a

RoleUnresolved

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleUnresolvedList

on which this method has never
been called does allow objects other than

RoleUnresolved

s to
be added.

**Throws:**
- IllegalArgumentException

- if this

RoleUnresolvedList

contains an element that is not a

RoleUnresolved

.

**Since:**
- 1.6

---

#### public void add​(
RoleUnresolved
role)
throws
IllegalArgumentException

Adds the RoleUnresolved specified as the last element of the list.

**Parameters:**
- role

- - the unresolved role to be added.

**Throws:**
- IllegalArgumentException

- if the unresolved role is null.

---

#### public void add​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException

Inserts the unresolved role specified as an element at the position
specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:**
- index

- - The position in the list where the new
RoleUnresolved object is to be inserted.
- role

- - The RoleUnresolved object to be inserted.

**Throws:**
- IllegalArgumentException

- if the unresolved role is null.
- IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

---

#### public void set​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException

Sets the element at the position specified to be the unresolved role
specified.
The previous element at that position is discarded.

**Parameters:**
- index

- - The position specified.
- role

- - The value to which the unresolved role element
should be set.

**Throws:**
- IllegalArgumentException

- if the unresolved role is null.
- IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index >= size()

).

---

#### public boolean addAll​(
RoleUnresolvedList
roleList)
throws
IndexOutOfBoundsException

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

**Parameters:**
- roleList

- - Elements to be inserted into the list
(can be null).

**Returns:**
- true if this list changed as a result of the call.

**Throws:**
- IndexOutOfBoundsException

- if accessing with an index
outside of the list.

---

#### public boolean addAll​(int index,

RoleUnresolvedList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

**Parameters:**
- index

- - Position at which to insert the first element from the
RoleUnresolvedList specified.
- roleList

- - Elements to be inserted into the list.

**Returns:**
- true if this list changed as a result of the call.

**Throws:**
- IllegalArgumentException

- if the role is null.
- IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

---

### Additional Sections

#### Class RoleUnresolvedList

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractList

<E>
- - java.util.ArrayList

<

Object

>
- - javax.management.relation.RoleUnresolvedList

java.util.AbstractCollection

<E>

- java.util.AbstractList

<E>
- - java.util.ArrayList

<

Object

>
- - javax.management.relation.RoleUnresolvedList

java.util.AbstractList

<E>

- java.util.ArrayList

<

Object

>
- - javax.management.relation.RoleUnresolvedList

java.util.ArrayList

<

Object

>

- javax.management.relation.RoleUnresolvedList

javax.management.relation.RoleUnresolvedList

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
RoleUnresolvedList

extends
ArrayList
<
Object
>
```

A RoleUnresolvedList represents a list of RoleUnresolved objects,
representing roles not retrieved from a relation due to a problem
encountered when trying to access (read or write) the roles.

**Since:** 1.5
**See Also:** Serialized Form

public class

RoleUnresolvedList

extends

ArrayList

<

Object

>

A RoleUnresolvedList represents a list of RoleUnresolved objects,
representing roles not retrieved from a relation due to a problem
encountered when trying to access (read or write) the roles.

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

RoleUnresolvedList

()

Constructs an empty RoleUnresolvedList.

RoleUnresolvedList

​(int initialCapacity)

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

RoleUnresolvedList

​(

List

<

RoleUnresolved

> list)

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

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

RoleUnresolved

role)

Inserts the unresolved role specified as an element at the position
specified.

void

add

​(

RoleUnresolved

role)

Adds the RoleUnresolved specified as the last element of the list.

boolean

addAll

​(int index,

RoleUnresolvedList

roleList)

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

boolean

addAll

​(

RoleUnresolvedList

roleList)

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

List

<

RoleUnresolved

>

asList

()

Return a view of this list as a

List<RoleUnresolved>

.

void

set

​(int index,

RoleUnresolved

role)

Sets the element at the position specified to be the unresolved role
specified.

- Methods declared in class java.util.

ArrayList

add

,

add

,

addAll

,

addAll

,

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

set

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

RoleUnresolvedList

()

Constructs an empty RoleUnresolvedList.

RoleUnresolvedList

​(int initialCapacity)

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

RoleUnresolvedList

​(

List

<

RoleUnresolved

> list)

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

---

#### Constructor Summary

Constructs an empty RoleUnresolvedList.

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

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

RoleUnresolved

role)

Inserts the unresolved role specified as an element at the position
specified.

void

add

​(

RoleUnresolved

role)

Adds the RoleUnresolved specified as the last element of the list.

boolean

addAll

​(int index,

RoleUnresolvedList

roleList)

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

boolean

addAll

​(

RoleUnresolvedList

roleList)

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

List

<

RoleUnresolved

>

asList

()

Return a view of this list as a

List<RoleUnresolved>

.

void

set

​(int index,

RoleUnresolved

role)

Sets the element at the position specified to be the unresolved role
specified.

- Methods declared in class java.util.

ArrayList

add

,

add

,

addAll

,

addAll

,

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

set

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

Inserts the unresolved role specified as an element at the position
specified.

Adds the RoleUnresolved specified as the last element of the list.

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

Return a view of this list as a

List<RoleUnresolved>

.

Sets the element at the position specified to be the unresolved role
specified.

Methods declared in class java.util.

ArrayList

add

,

add

,

addAll

,

addAll

,

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

set

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

- RoleUnresolvedList

```java
public RoleUnresolvedList()
```

Constructs an empty RoleUnresolvedList.

- RoleUnresolvedList

```java
public RoleUnresolvedList​(int initialCapacity)
```

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

**Parameters:** initialCapacity

- initial capacity

- RoleUnresolvedList

```java
public RoleUnresolvedList​(
List
<
RoleUnresolved
> list)
throws
IllegalArgumentException
```

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleUnresolvedList

instance has
an initial capacity of 110% of the size of the

List

specified.

**Parameters:** list

- the

List

that defines the initial contents of
the new

RoleUnresolvedList

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
non-RoleUnresolved objects.
**See Also:** ArrayList(java.util.Collection)

============ METHOD DETAIL ==========

- Method Detail

- asList

```java
public
List
<
RoleUnresolved
> asList()
```

Return a view of this list as a

List<RoleUnresolved>

.
Changes to the returned value are reflected by changes
to the original

RoleUnresolvedList

and vice versa.

**Returns:** a

List<RoleUnresolved>

whose contents
reflect the contents of this

RoleUnresolvedList

.

If this method has ever been called on a given

RoleUnresolvedList

instance, a subsequent attempt to add
an object to that instance which is not a

RoleUnresolved

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleUnresolvedList

on which this method has never
been called does allow objects other than

RoleUnresolved

s to
be added.
**Throws:** IllegalArgumentException

- if this

RoleUnresolvedList

contains an element that is not a

RoleUnresolved

.
**Since:** 1.6

- add

```java
public void add​(
RoleUnresolved
role)
throws
IllegalArgumentException
```

Adds the RoleUnresolved specified as the last element of the list.

**Parameters:** role

- - the unresolved role to be added.
**Throws:** IllegalArgumentException

- if the unresolved role is null.

- add

```java
public void add​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts the unresolved role specified as an element at the position
specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:** index

- - The position in the list where the new
RoleUnresolved object is to be inserted.
**Parameters:** role

- - The RoleUnresolved object to be inserted.
**Throws:** IllegalArgumentException

- if the unresolved role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

- set

```java
public void set​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Sets the element at the position specified to be the unresolved role
specified.
The previous element at that position is discarded.

**Parameters:** index

- - The position specified.
**Parameters:** role

- - The value to which the unresolved role element
should be set.
**Throws:** IllegalArgumentException

- if the unresolved role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index >= size()

).

- addAll

```java
public boolean addAll​(
RoleUnresolvedList
roleList)
throws
IndexOutOfBoundsException
```

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

**Parameters:** roleList

- - Elements to be inserted into the list
(can be null).
**Returns:** true if this list changed as a result of the call.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

- addAll

```java
public boolean addAll​(int index,

RoleUnresolvedList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

**Parameters:** index

- - Position at which to insert the first element from the
RoleUnresolvedList specified.
**Parameters:** roleList

- - Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

Constructor Detail

- RoleUnresolvedList

```java
public RoleUnresolvedList()
```

Constructs an empty RoleUnresolvedList.

- RoleUnresolvedList

```java
public RoleUnresolvedList​(int initialCapacity)
```

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

**Parameters:** initialCapacity

- initial capacity

- RoleUnresolvedList

```java
public RoleUnresolvedList​(
List
<
RoleUnresolved
> list)
throws
IllegalArgumentException
```

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleUnresolvedList

instance has
an initial capacity of 110% of the size of the

List

specified.

**Parameters:** list

- the

List

that defines the initial contents of
the new

RoleUnresolvedList

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
non-RoleUnresolved objects.
**See Also:** ArrayList(java.util.Collection)

---

#### Constructor Detail

RoleUnresolvedList

```java
public RoleUnresolvedList()
```

Constructs an empty RoleUnresolvedList.

---

#### RoleUnresolvedList

public RoleUnresolvedList()

Constructs an empty RoleUnresolvedList.

RoleUnresolvedList

```java
public RoleUnresolvedList​(int initialCapacity)
```

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

**Parameters:** initialCapacity

- initial capacity

---

#### RoleUnresolvedList

public RoleUnresolvedList​(int initialCapacity)

Constructs an empty RoleUnresolvedList with the initial capacity
specified.

RoleUnresolvedList

```java
public RoleUnresolvedList​(
List
<
RoleUnresolved
> list)
throws
IllegalArgumentException
```

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleUnresolvedList

instance has
an initial capacity of 110% of the size of the

List

specified.

**Parameters:** list

- the

List

that defines the initial contents of
the new

RoleUnresolvedList

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
non-RoleUnresolved objects.
**See Also:** ArrayList(java.util.Collection)

---

#### RoleUnresolvedList

public RoleUnresolvedList​(

List

<

RoleUnresolved

> list)
throws

IllegalArgumentException

Constructs a

RoleUnresolvedList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleUnresolvedList

instance has
an initial capacity of 110% of the size of the

List

specified.

Method Detail

- asList

```java
public
List
<
RoleUnresolved
> asList()
```

Return a view of this list as a

List<RoleUnresolved>

.
Changes to the returned value are reflected by changes
to the original

RoleUnresolvedList

and vice versa.

**Returns:** a

List<RoleUnresolved>

whose contents
reflect the contents of this

RoleUnresolvedList

.

If this method has ever been called on a given

RoleUnresolvedList

instance, a subsequent attempt to add
an object to that instance which is not a

RoleUnresolved

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleUnresolvedList

on which this method has never
been called does allow objects other than

RoleUnresolved

s to
be added.
**Throws:** IllegalArgumentException

- if this

RoleUnresolvedList

contains an element that is not a

RoleUnresolved

.
**Since:** 1.6

- add

```java
public void add​(
RoleUnresolved
role)
throws
IllegalArgumentException
```

Adds the RoleUnresolved specified as the last element of the list.

**Parameters:** role

- - the unresolved role to be added.
**Throws:** IllegalArgumentException

- if the unresolved role is null.

- add

```java
public void add​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts the unresolved role specified as an element at the position
specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:** index

- - The position in the list where the new
RoleUnresolved object is to be inserted.
**Parameters:** role

- - The RoleUnresolved object to be inserted.
**Throws:** IllegalArgumentException

- if the unresolved role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

- set

```java
public void set​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Sets the element at the position specified to be the unresolved role
specified.
The previous element at that position is discarded.

**Parameters:** index

- - The position specified.
**Parameters:** role

- - The value to which the unresolved role element
should be set.
**Throws:** IllegalArgumentException

- if the unresolved role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index >= size()

).

- addAll

```java
public boolean addAll​(
RoleUnresolvedList
roleList)
throws
IndexOutOfBoundsException
```

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

**Parameters:** roleList

- - Elements to be inserted into the list
(can be null).
**Returns:** true if this list changed as a result of the call.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

- addAll

```java
public boolean addAll​(int index,

RoleUnresolvedList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

**Parameters:** index

- - Position at which to insert the first element from the
RoleUnresolvedList specified.
**Parameters:** roleList

- - Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

---

#### Method Detail

asList

```java
public
List
<
RoleUnresolved
> asList()
```

Return a view of this list as a

List<RoleUnresolved>

.
Changes to the returned value are reflected by changes
to the original

RoleUnresolvedList

and vice versa.

**Returns:** a

List<RoleUnresolved>

whose contents
reflect the contents of this

RoleUnresolvedList

.

If this method has ever been called on a given

RoleUnresolvedList

instance, a subsequent attempt to add
an object to that instance which is not a

RoleUnresolved

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleUnresolvedList

on which this method has never
been called does allow objects other than

RoleUnresolved

s to
be added.
**Throws:** IllegalArgumentException

- if this

RoleUnresolvedList

contains an element that is not a

RoleUnresolved

.
**Since:** 1.6

---

#### asList

public

List

<

RoleUnresolved

> asList()

Return a view of this list as a

List<RoleUnresolved>

.
Changes to the returned value are reflected by changes
to the original

RoleUnresolvedList

and vice versa.

If this method has ever been called on a given

RoleUnresolvedList

instance, a subsequent attempt to add
an object to that instance which is not a

RoleUnresolved

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleUnresolvedList

on which this method has never
been called does allow objects other than

RoleUnresolved

s to
be added.

add

```java
public void add​(
RoleUnresolved
role)
throws
IllegalArgumentException
```

Adds the RoleUnresolved specified as the last element of the list.

**Parameters:** role

- - the unresolved role to be added.
**Throws:** IllegalArgumentException

- if the unresolved role is null.

---

#### add

public void add​(

RoleUnresolved

role)
throws

IllegalArgumentException

Adds the RoleUnresolved specified as the last element of the list.

add

```java
public void add​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts the unresolved role specified as an element at the position
specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:** index

- - The position in the list where the new
RoleUnresolved object is to be inserted.
**Parameters:** role

- - The RoleUnresolved object to be inserted.
**Throws:** IllegalArgumentException

- if the unresolved role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

---

#### add

public void add​(int index,

RoleUnresolved

role)
throws

IllegalArgumentException

,

IndexOutOfBoundsException

Inserts the unresolved role specified as an element at the position
specified.
Elements with an index greater than or equal to the current position are
shifted up.

set

```java
public void set​(int index,

RoleUnresolved
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Sets the element at the position specified to be the unresolved role
specified.
The previous element at that position is discarded.

**Parameters:** index

- - The position specified.
**Parameters:** role

- - The value to which the unresolved role element
should be set.
**Throws:** IllegalArgumentException

- if the unresolved role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index >= size()

).

---

#### set

public void set​(int index,

RoleUnresolved

role)
throws

IllegalArgumentException

,

IndexOutOfBoundsException

Sets the element at the position specified to be the unresolved role
specified.
The previous element at that position is discarded.

addAll

```java
public boolean addAll​(
RoleUnresolvedList
roleList)
throws
IndexOutOfBoundsException
```

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

**Parameters:** roleList

- - Elements to be inserted into the list
(can be null).
**Returns:** true if this list changed as a result of the call.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

---

#### addAll

public boolean addAll​(

RoleUnresolvedList

roleList)
throws

IndexOutOfBoundsException

Appends all the elements in the RoleUnresolvedList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleUnresolvedList specified.

addAll

```java
public boolean addAll​(int index,

RoleUnresolvedList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

**Parameters:** index

- - Position at which to insert the first element from the
RoleUnresolvedList specified.
**Parameters:** roleList

- - Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

index < 0 || index > size()

).

---

#### addAll

public boolean addAll​(int index,

RoleUnresolvedList

roleList)
throws

IllegalArgumentException

,

IndexOutOfBoundsException

Inserts all of the elements in the RoleUnresolvedList specified into
this list, starting at the specified position, in the order in which
they are returned by the Iterator of the RoleUnresolvedList specified.

---

