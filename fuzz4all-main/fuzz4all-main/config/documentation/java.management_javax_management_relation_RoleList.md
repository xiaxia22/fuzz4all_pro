# Class RoleList

**Source:** `java.management\javax\management\relation\RoleList.html`

### Class Description

```java
public class
RoleList

extends
ArrayList
<
Object
>
```

A RoleList represents a list of roles (Role objects). It is used as
parameter when creating a relation, and when trying to set several roles in
a relation (via 'setRoles()' method). It is returned as part of a
RoleResult, to provide roles successfully retrieved.

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

#### public RoleList()

Constructs an empty RoleList.

---

#### public RoleList​(int initialCapacity)

Constructs an empty RoleList with the initial capacity
specified.

**Parameters:**
- initialCapacity

- initial capacity

---

#### public RoleList​(
List
<
Role
> list)
throws
IllegalArgumentException

Constructs a

RoleList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleList

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

RoleList

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
non-Role objects.

**See Also:**
- ArrayList(java.util.Collection)

---

### Method Details

#### public
List
<
Role
> asList()

Return a view of this list as a

List<Role>

.
Changes to the returned value are reflected by changes
to the original

RoleList

and vice versa.

**Returns:**
- a

List<Role>

whose contents
reflect the contents of this

RoleList

.

If this method has ever been called on a given

RoleList

instance, a subsequent attempt to add
an object to that instance which is not a

Role

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleList

on which this method has never
been called does allow objects other than

Role

s to
be added.

**Throws:**
- IllegalArgumentException

- if this

RoleList

contains
an element that is not a

Role

.

**Since:**
- 1.6

---

#### public void add​(
Role
role)
throws
IllegalArgumentException

Adds the Role specified as the last element of the list.

**Parameters:**
- role

- the role to be added.

**Throws:**
- IllegalArgumentException

- if the role is null.

---

#### public void add​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException

Inserts the role specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:**
- index

- The position in the list where the new Role
object is to be inserted.
- role

- The Role object to be inserted.

**Throws:**
- IllegalArgumentException

- if the role is null.
- IndexOutOfBoundsException

- if accessing with an index
outside of the list.

---

#### public void set​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException

Sets the element at the position specified to be the role
specified.
The previous element at that position is discarded.

**Parameters:**
- index

- The position specified.
- role

- The value to which the role element should be set.

**Throws:**
- IllegalArgumentException

- if the role is null.
- IndexOutOfBoundsException

- if accessing with an index
outside of the list.

---

#### public boolean addAll​(
RoleList
roleList)
throws
IndexOutOfBoundsException

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

**Parameters:**
- roleList

- Elements to be inserted into the list (can be null)

**Returns:**
- true if this list changed as a result of the call.

**Throws:**
- IndexOutOfBoundsException

- if accessing with an index
outside of the list.

**See Also:**
- ArrayList.addAll(Collection)

---

#### public boolean addAll​(int index,

RoleList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

**Parameters:**
- index

- Position at which to insert the first element from the
RoleList specified.
- roleList

- Elements to be inserted into the list.

**Returns:**
- true if this list changed as a result of the call.

**Throws:**
- IllegalArgumentException

- if the role is null.
- IndexOutOfBoundsException

- if accessing with an index
outside of the list.

**See Also:**
- ArrayList.addAll(int, Collection)

---

### Additional Sections

#### Class RoleList

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractList

<E>
- - java.util.ArrayList

<

Object

>
- - javax.management.relation.RoleList

java.util.AbstractCollection

<E>

- java.util.AbstractList

<E>
- - java.util.ArrayList

<

Object

>
- - javax.management.relation.RoleList

java.util.AbstractList

<E>

- java.util.ArrayList

<

Object

>
- - javax.management.relation.RoleList

java.util.ArrayList

<

Object

>

- javax.management.relation.RoleList

javax.management.relation.RoleList

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
RoleList

extends
ArrayList
<
Object
>
```

A RoleList represents a list of roles (Role objects). It is used as
parameter when creating a relation, and when trying to set several roles in
a relation (via 'setRoles()' method). It is returned as part of a
RoleResult, to provide roles successfully retrieved.

**Since:** 1.5
**See Also:** Serialized Form

public class

RoleList

extends

ArrayList

<

Object

>

A RoleList represents a list of roles (Role objects). It is used as
parameter when creating a relation, and when trying to set several roles in
a relation (via 'setRoles()' method). It is returned as part of a
RoleResult, to provide roles successfully retrieved.

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

RoleList

()

Constructs an empty RoleList.

RoleList

​(int initialCapacity)

Constructs an empty RoleList with the initial capacity
specified.

RoleList

​(

List

<

Role

> list)

Constructs a

RoleList

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

Role

role)

Inserts the role specified as an element at the position specified.

void

add

​(

Role

role)

Adds the Role specified as the last element of the list.

boolean

addAll

​(int index,

RoleList

roleList)

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

boolean

addAll

​(

RoleList

roleList)

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

List

<

Role

>

asList

()

Return a view of this list as a

List<Role>

.

void

set

​(int index,

Role

role)

Sets the element at the position specified to be the role
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

RoleList

()

Constructs an empty RoleList.

RoleList

​(int initialCapacity)

Constructs an empty RoleList with the initial capacity
specified.

RoleList

​(

List

<

Role

> list)

Constructs a

RoleList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator.

---

#### Constructor Summary

Constructs an empty RoleList.

Constructs an empty RoleList with the initial capacity
specified.

Constructs a

RoleList

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

Role

role)

Inserts the role specified as an element at the position specified.

void

add

​(

Role

role)

Adds the Role specified as the last element of the list.

boolean

addAll

​(int index,

RoleList

roleList)

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

boolean

addAll

​(

RoleList

roleList)

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

List

<

Role

>

asList

()

Return a view of this list as a

List<Role>

.

void

set

​(int index,

Role

role)

Sets the element at the position specified to be the role
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

Inserts the role specified as an element at the position specified.

Adds the Role specified as the last element of the list.

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

Return a view of this list as a

List<Role>

.

Sets the element at the position specified to be the role
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

- RoleList

```java
public RoleList()
```

Constructs an empty RoleList.

- RoleList

```java
public RoleList​(int initialCapacity)
```

Constructs an empty RoleList with the initial capacity
specified.

**Parameters:** initialCapacity

- initial capacity

- RoleList

```java
public RoleList​(
List
<
Role
> list)
throws
IllegalArgumentException
```

Constructs a

RoleList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleList

instance has
an initial capacity of 110% of the size of the

List

specified.

**Parameters:** list

- the

List

that defines the initial contents of
the new

RoleList

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
non-Role objects.
**See Also:** ArrayList(java.util.Collection)

============ METHOD DETAIL ==========

- Method Detail

- asList

```java
public
List
<
Role
> asList()
```

Return a view of this list as a

List<Role>

.
Changes to the returned value are reflected by changes
to the original

RoleList

and vice versa.

**Returns:** a

List<Role>

whose contents
reflect the contents of this

RoleList

.

If this method has ever been called on a given

RoleList

instance, a subsequent attempt to add
an object to that instance which is not a

Role

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleList

on which this method has never
been called does allow objects other than

Role

s to
be added.
**Throws:** IllegalArgumentException

- if this

RoleList

contains
an element that is not a

Role

.
**Since:** 1.6

- add

```java
public void add​(
Role
role)
throws
IllegalArgumentException
```

Adds the Role specified as the last element of the list.

**Parameters:** role

- the role to be added.
**Throws:** IllegalArgumentException

- if the role is null.

- add

```java
public void add​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts the role specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:** index

- The position in the list where the new Role
object is to be inserted.
**Parameters:** role

- The Role object to be inserted.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

- set

```java
public void set​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Sets the element at the position specified to be the role
specified.
The previous element at that position is discarded.

**Parameters:** index

- The position specified.
**Parameters:** role

- The value to which the role element should be set.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

- addAll

```java
public boolean addAll​(
RoleList
roleList)
throws
IndexOutOfBoundsException
```

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

**Parameters:** roleList

- Elements to be inserted into the list (can be null)
**Returns:** true if this list changed as a result of the call.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.
**See Also:** ArrayList.addAll(Collection)

- addAll

```java
public boolean addAll​(int index,

RoleList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

**Parameters:** index

- Position at which to insert the first element from the
RoleList specified.
**Parameters:** roleList

- Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.
**See Also:** ArrayList.addAll(int, Collection)

Constructor Detail

- RoleList

```java
public RoleList()
```

Constructs an empty RoleList.

- RoleList

```java
public RoleList​(int initialCapacity)
```

Constructs an empty RoleList with the initial capacity
specified.

**Parameters:** initialCapacity

- initial capacity

- RoleList

```java
public RoleList​(
List
<
Role
> list)
throws
IllegalArgumentException
```

Constructs a

RoleList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleList

instance has
an initial capacity of 110% of the size of the

List

specified.

**Parameters:** list

- the

List

that defines the initial contents of
the new

RoleList

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
non-Role objects.
**See Also:** ArrayList(java.util.Collection)

---

#### Constructor Detail

RoleList

```java
public RoleList()
```

Constructs an empty RoleList.

---

#### RoleList

public RoleList()

Constructs an empty RoleList.

RoleList

```java
public RoleList​(int initialCapacity)
```

Constructs an empty RoleList with the initial capacity
specified.

**Parameters:** initialCapacity

- initial capacity

---

#### RoleList

public RoleList​(int initialCapacity)

Constructs an empty RoleList with the initial capacity
specified.

RoleList

```java
public RoleList​(
List
<
Role
> list)
throws
IllegalArgumentException
```

Constructs a

RoleList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleList

instance has
an initial capacity of 110% of the size of the

List

specified.

**Parameters:** list

- the

List

that defines the initial contents of
the new

RoleList

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
non-Role objects.
**See Also:** ArrayList(java.util.Collection)

---

#### RoleList

public RoleList​(

List

<

Role

> list)
throws

IllegalArgumentException

Constructs a

RoleList

containing the elements of the

List

specified, in the order in which they are returned by
the

List

's iterator. The

RoleList

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
Role
> asList()
```

Return a view of this list as a

List<Role>

.
Changes to the returned value are reflected by changes
to the original

RoleList

and vice versa.

**Returns:** a

List<Role>

whose contents
reflect the contents of this

RoleList

.

If this method has ever been called on a given

RoleList

instance, a subsequent attempt to add
an object to that instance which is not a

Role

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleList

on which this method has never
been called does allow objects other than

Role

s to
be added.
**Throws:** IllegalArgumentException

- if this

RoleList

contains
an element that is not a

Role

.
**Since:** 1.6

- add

```java
public void add​(
Role
role)
throws
IllegalArgumentException
```

Adds the Role specified as the last element of the list.

**Parameters:** role

- the role to be added.
**Throws:** IllegalArgumentException

- if the role is null.

- add

```java
public void add​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts the role specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:** index

- The position in the list where the new Role
object is to be inserted.
**Parameters:** role

- The Role object to be inserted.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

- set

```java
public void set​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Sets the element at the position specified to be the role
specified.
The previous element at that position is discarded.

**Parameters:** index

- The position specified.
**Parameters:** role

- The value to which the role element should be set.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

- addAll

```java
public boolean addAll​(
RoleList
roleList)
throws
IndexOutOfBoundsException
```

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

**Parameters:** roleList

- Elements to be inserted into the list (can be null)
**Returns:** true if this list changed as a result of the call.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.
**See Also:** ArrayList.addAll(Collection)

- addAll

```java
public boolean addAll​(int index,

RoleList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

**Parameters:** index

- Position at which to insert the first element from the
RoleList specified.
**Parameters:** roleList

- Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.
**See Also:** ArrayList.addAll(int, Collection)

---

#### Method Detail

asList

```java
public
List
<
Role
> asList()
```

Return a view of this list as a

List<Role>

.
Changes to the returned value are reflected by changes
to the original

RoleList

and vice versa.

**Returns:** a

List<Role>

whose contents
reflect the contents of this

RoleList

.

If this method has ever been called on a given

RoleList

instance, a subsequent attempt to add
an object to that instance which is not a

Role

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleList

on which this method has never
been called does allow objects other than

Role

s to
be added.
**Throws:** IllegalArgumentException

- if this

RoleList

contains
an element that is not a

Role

.
**Since:** 1.6

---

#### asList

public

List

<

Role

> asList()

Return a view of this list as a

List<Role>

.
Changes to the returned value are reflected by changes
to the original

RoleList

and vice versa.

If this method has ever been called on a given

RoleList

instance, a subsequent attempt to add
an object to that instance which is not a

Role

will fail with an

IllegalArgumentException

. For compatibility
reasons, a

RoleList

on which this method has never
been called does allow objects other than

Role

s to
be added.

add

```java
public void add​(
Role
role)
throws
IllegalArgumentException
```

Adds the Role specified as the last element of the list.

**Parameters:** role

- the role to be added.
**Throws:** IllegalArgumentException

- if the role is null.

---

#### add

public void add​(

Role

role)
throws

IllegalArgumentException

Adds the Role specified as the last element of the list.

add

```java
public void add​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts the role specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up.

**Parameters:** index

- The position in the list where the new Role
object is to be inserted.
**Parameters:** role

- The Role object to be inserted.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

---

#### add

public void add​(int index,

Role

role)
throws

IllegalArgumentException

,

IndexOutOfBoundsException

Inserts the role specified as an element at the position specified.
Elements with an index greater than or equal to the current position are
shifted up.

set

```java
public void set​(int index,

Role
role)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Sets the element at the position specified to be the role
specified.
The previous element at that position is discarded.

**Parameters:** index

- The position specified.
**Parameters:** role

- The value to which the role element should be set.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.

---

#### set

public void set​(int index,

Role

role)
throws

IllegalArgumentException

,

IndexOutOfBoundsException

Sets the element at the position specified to be the role
specified.
The previous element at that position is discarded.

addAll

```java
public boolean addAll​(
RoleList
roleList)
throws
IndexOutOfBoundsException
```

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

**Parameters:** roleList

- Elements to be inserted into the list (can be null)
**Returns:** true if this list changed as a result of the call.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.
**See Also:** ArrayList.addAll(Collection)

---

#### addAll

public boolean addAll​(

RoleList

roleList)
throws

IndexOutOfBoundsException

Appends all the elements in the RoleList specified to the end
of the list, in the order in which they are returned by the Iterator of
the RoleList specified.

addAll

```java
public boolean addAll​(int index,

RoleList
roleList)
throws
IllegalArgumentException
,

IndexOutOfBoundsException
```

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

**Parameters:** index

- Position at which to insert the first element from the
RoleList specified.
**Parameters:** roleList

- Elements to be inserted into the list.
**Returns:** true if this list changed as a result of the call.
**Throws:** IllegalArgumentException

- if the role is null.
**Throws:** IndexOutOfBoundsException

- if accessing with an index
outside of the list.
**See Also:** ArrayList.addAll(int, Collection)

---

#### addAll

public boolean addAll​(int index,

RoleList

roleList)
throws

IllegalArgumentException

,

IndexOutOfBoundsException

Inserts all of the elements in the RoleList specified into this
list, starting at the specified position, in the order in which they are
returned by the Iterator of the RoleList specified.

---

