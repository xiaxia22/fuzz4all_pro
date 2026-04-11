# Class AbstractList<E>

**Source:** `java.base\java\util\AbstractList.html`

### Class Description

```java
public abstract class
AbstractList<E>

extends
AbstractCollection
<E>
implements
List
<E>
```

This class provides a skeletal implementation of the

List

interface to minimize the effort required to implement this interface
backed by a "random access" data store (such as an array). For sequential
access data (such as a linked list),

AbstractSequentialList

should
be used in preference to this class.

To implement an unmodifiable list, the programmer needs only to extend
this class and provide implementations for the

get(int)

and

size()

methods.

To implement a modifiable list, the programmer must additionally
override the

set(int, E)

method (which otherwise
throws an

UnsupportedOperationException

). If the list is
variable-size the programmer must additionally override the

add(int, E)

and

remove(int)

methods.

The programmer should generally provide a void (no argument) and collection
constructor, as per the recommendation in the

Collection

interface
specification.

Unlike the other abstract collection implementations, the programmer does

not

have to provide an iterator implementation; the iterator and
list iterator are implemented by this class, on top of the "random access"
methods:

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

**All Implemented Interfaces:** Iterable

<E>

,

Collection

<E>

,

List

<E>

---

### Field Details

#### protected transient int modCount

The number of times this list has been

structurally modified

.
Structural modifications are those that change the size of the
list, or otherwise perturb it in such a fashion that iterations in
progress may yield incorrect results.

This field is used by the iterator and list iterator implementation
returned by the

iterator

and

listIterator

methods.
If the value of this field changes unexpectedly, the iterator (or list
iterator) will throw a

ConcurrentModificationException

in
response to the

next

,

remove

,

previous

,

set

or

add

operations. This provides

fail-fast

behavior, rather than non-deterministic behavior in
the face of concurrent modification during iteration.

Use of this field by subclasses is optional.

If a subclass
wishes to provide fail-fast iterators (and list iterators), then it
merely has to increment this field in its

add(int, E)

and

remove(int)

methods (and any other methods that it overrides
that result in structural modifications to the list). A single call to

add(int, E)

or

remove(int)

must add no more than
one to this field, or the iterators (and list iterators) will throw
bogus

ConcurrentModificationExceptions

. If an implementation
does not wish to provide fail-fast iterators, this field may be
ignored.

---

### Constructor Details

#### protected AbstractList()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public boolean add​(
E
e)

Appends the specified element to the end of this list (optional
operation).

Lists that support this operation may place limitations on what
elements may be added to this list. In particular, some
lists will refuse to add null elements, and others will impose
restrictions on the type of elements that may be added. List
classes should clearly specify in their documentation any restrictions
on what elements may be added.

**Specified by:**
- add

in interface

Collection

<

E

>
- add

in interface

List

<

E

>

**Overrides:**
- add

in class

AbstractCollection

<

E

>

**Parameters:**
- e

- element to be appended to this list

**Returns:**
- true

(as specified by

Collection.add(E)

)

**Throws:**
- UnsupportedOperationException

- if the

add

operation
is not supported by this list
- ClassCastException

- if the class of the specified element
prevents it from being added to this list
- NullPointerException

- if the specified element is null and this
list does not permit null elements
- IllegalArgumentException

- if some property of this element
prevents it from being added to this list

**Implementation Requirements:**
- This implementation calls

add(size(), e)

.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.

---

#### public abstract
E
get​(int index)

Returns the element at the specified position in this list.

**Specified by:**
- get

in interface

List

<

E

>

**Parameters:**
- index

- index of the element to return

**Returns:**
- the element at the specified position in this list

**Throws:**
- IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

---

#### public
E
set​(int index,

E
element)

Replaces the element at the specified position in this list with the
specified element (optional operation).

**Specified by:**
- set

in interface

List

<

E

>

**Parameters:**
- index

- index of the element to replace
- element

- element to be stored at the specified position

**Returns:**
- the element previously at the specified position

**Throws:**
- UnsupportedOperationException

- if the

set

operation
is not supported by this list
- ClassCastException

- if the class of the specified element
prevents it from being added to this list
- NullPointerException

- if the specified element is null and
this list does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
- IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

**Implementation Requirements:**
- This implementation always throws an

UnsupportedOperationException

.

---

#### public void add​(int index,

E
element)

Inserts the specified element at the specified position in this list
(optional operation). Shifts the element currently at that position
(if any) and any subsequent elements to the right (adds one to their
indices).

**Specified by:**
- add

in interface

List

<

E

>

**Parameters:**
- index

- index at which the specified element is to be inserted
- element

- element to be inserted

**Throws:**
- UnsupportedOperationException

- if the

add

operation
is not supported by this list
- ClassCastException

- if the class of the specified element
prevents it from being added to this list
- NullPointerException

- if the specified element is null and
this list does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
- IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

**Implementation Requirements:**
- This implementation always throws an

UnsupportedOperationException

.

---

#### public
E
remove​(int index)

Removes the element at the specified position in this list (optional
operation). Shifts any subsequent elements to the left (subtracts one
from their indices). Returns the element that was removed from the
list.

**Specified by:**
- remove

in interface

List

<

E

>

**Parameters:**
- index

- the index of the element to be removed

**Returns:**
- the element previously at the specified position

**Throws:**
- UnsupportedOperationException

- if the

remove

operation
is not supported by this list
- IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

**Implementation Requirements:**
- This implementation always throws an

UnsupportedOperationException

.

---

#### public int indexOf​(
Object
o)

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the lowest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:**
- indexOf

in interface

List

<

E

>

**Parameters:**
- o

- element to search for

**Returns:**
- the index of the first occurrence of the specified element in
this list, or -1 if this list does not contain the element

**Throws:**
- ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
- NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

**Implementation Requirements:**
- This implementation first gets a list iterator (with

listIterator()

). Then, it iterates over the list until the
specified element is found or the end of the list is reached.

---

#### public int lastIndexOf​(
Object
o)

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the highest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:**
- lastIndexOf

in interface

List

<

E

>

**Parameters:**
- o

- element to search for

**Returns:**
- the index of the last occurrence of the specified element in
this list, or -1 if this list does not contain the element

**Throws:**
- ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
- NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

**Implementation Requirements:**
- This implementation first gets a list iterator that points to the end
of the list (with

listIterator(size())

). Then, it iterates
backwards over the list until the specified element is found, or the
beginning of the list is reached.

---

#### public void clear()

Removes all of the elements from this list (optional operation).
The list will be empty after this call returns.

**Specified by:**
- clear

in interface

Collection

<

E

>
- clear

in interface

List

<

E

>

**Overrides:**
- clear

in class

AbstractCollection

<

E

>

**Throws:**
- UnsupportedOperationException

- if the

clear

operation
is not supported by this list

**Implementation Requirements:**
- This implementation calls

removeRange(0, size())

.

Note that this implementation throws an

UnsupportedOperationException

unless

remove(int
index)

or

removeRange(int fromIndex, int toIndex)

is
overridden.

---

#### public boolean addAll​(int index,

Collection
<? extends
E
> c)

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation). Shifts the
element currently at that position (if any) and any subsequent
elements to the right (increases their indices). The new elements
will appear in this list in the order that they are returned by the
specified collection's iterator. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress. (Note that this will occur if the specified
collection is this list, and it's nonempty.)

**Specified by:**
- addAll

in interface

List

<

E

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
- UnsupportedOperationException

- if the

addAll

operation
is not supported by this list
- ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this list
- NullPointerException

- if the specified collection contains one
or more null elements and this list does not permit null
elements, or if the specified collection is null
- IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this list
- IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

**Implementation Requirements:**
- This implementation gets an iterator over the specified collection
and iterates over it, inserting the elements obtained from the
iterator into this list at the appropriate position, one at a time,
using

add(int, E)

.
Many implementations will override this method for efficiency.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.

---

#### public
Iterator
<
E
> iterator()

Returns an iterator over the elements in this list in proper sequence.

**Specified by:**
- iterator

in interface

Collection

<

E

>
- iterator

in interface

Iterable

<

E

>
- iterator

in interface

List

<

E

>
- iterator

in class

AbstractCollection

<

E

>

**Returns:**
- an iterator over the elements in this list in proper sequence

**Implementation Requirements:**
- This implementation returns a straightforward implementation of the
iterator interface, relying on the backing list's

size()

,

get(int)

, and

remove(int)

methods.

Note that the iterator returned by this method will throw an

UnsupportedOperationException

in response to its

remove

method unless the list's

remove(int)

method is
overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification
for the (protected)

modCount

field.

---

#### public
ListIterator
<
E
> listIterator()

Returns a list iterator over the elements in this list (in proper
sequence).

**Specified by:**
- listIterator

in interface

List

<

E

>

**Returns:**
- a list iterator over the elements in this list (in proper
sequence)

**See Also:**
- listIterator(int)

**Implementation Requirements:**
- This implementation returns

listIterator(0)

.

---

#### public
ListIterator
<
E
> listIterator​(int index)

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.
The specified index indicates the first element that would be
returned by an initial call to

next

.
An initial call to

previous

would
return the element with the specified index minus one.

**Specified by:**
- listIterator

in interface

List

<

E

>

**Parameters:**
- index

- index of the first element to be returned from the
list iterator (by a call to

next

)

**Returns:**
- a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list

**Throws:**
- IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

**Implementation Requirements:**
- This implementation returns a straightforward implementation of the

ListIterator

interface that extends the implementation of the

Iterator

interface returned by the

iterator()

method.
The

ListIterator

implementation relies on the backing list's

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

methods.

Note that the list iterator returned by this implementation will
throw an

UnsupportedOperationException

in response to its

remove

,

set

and

add

methods unless the
list's

remove(int)

,

set(int, E)

, and

add(int, E)

methods are overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification for
the (protected)

modCount

field.

---

#### public
List
<
E
> subList​(int fromIndex,
int toIndex)

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive. (If

fromIndex

and

toIndex

are equal, the returned list is
empty.) The returned list is backed by this list, so non-structural
changes in the returned list are reflected in this list, and vice-versa.
The returned list supports all of the optional list operations supported
by this list.

This method eliminates the need for explicit range operations (of
the sort that commonly exist for arrays). Any operation that expects
a list can be used as a range operation by passing a subList view
instead of a whole list. For example, the following idiom
removes a range of elements from a list:

```java
list.subList(from, to).clear();
```

Similar idioms may be constructed for

indexOf

and

lastIndexOf

, and all of the algorithms in the

Collections

class can be applied to a subList.

The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is

structurally modified

in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)

**Specified by:**
- subList

in interface

List

<

E

>

**Parameters:**
- fromIndex

- low endpoint (inclusive) of the subList
- toIndex

- high endpoint (exclusive) of the subList

**Returns:**
- a view of the specified range within this list

**Throws:**
- IndexOutOfBoundsException

- if an endpoint index value is out of range

(fromIndex < 0 || toIndex > size)
- IllegalArgumentException

- if the endpoint indices are out of order

(fromIndex > toIndex)

**Implementation Requirements:**
- This implementation returns a list that subclasses

AbstractList

. The subclass stores, in private fields, the
size of the subList (which can change over its lifetime), and the
expected

modCount

value of the backing list. There are two
variants of the subclass, one of which implements

RandomAccess

.
If this list implements

RandomAccess

the returned list will
be an instance of the subclass that implements

RandomAccess

.

The subclass's

set(int, E)

,

get(int)

,

add(int, E)

,

remove(int)

,

addAll(int,
Collection)

and

removeRange(int, int)

methods all
delegate to the corresponding methods on the backing abstract list,
after bounds-checking the index and adjusting for the offset. The

addAll(Collection c)

method merely returns

addAll(size,
c)

.

The

listIterator(int)

method returns a "wrapper object"
over a list iterator on the backing list, which is created with the
corresponding method on the backing list. The

iterator

method
merely returns

listIterator()

, and the

size

method
merely returns the subclass's

size

field.

All methods first check to see if the actual

modCount

of
the backing list is equal to its expected value, and throw a

ConcurrentModificationException

if it is not.

---

#### public boolean equals​(
Object
o)

Compares the specified object with this list for equality. Returns

true

if and only if the specified object is also a list, both
lists have the same size, and all corresponding pairs of elements in
the two lists are

equal

. (Two elements

e1

and

e2

are

equal

if

(e1==null ? e2==null :
e1.equals(e2))

.) In other words, two lists are defined to be
equal if they contain the same elements in the same order.

**Specified by:**
- equals

in interface

Collection

<

E

>
- equals

in interface

List

<

E

>

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to be compared for equality with this list

**Returns:**
- true

if the specified object is equal to this list

**See Also:**
- Object.hashCode()

,

HashMap

**Implementation Requirements:**
- This implementation first checks if the specified object is this
list. If so, it returns

true

; if not, it checks if the
specified object is a list. If not, it returns

false

; if so,
it iterates over both lists, comparing corresponding pairs of elements.
If any comparison returns

false

, this method returns

false

. If either iterator runs out of elements before the
other it returns

false

(as the lists are of unequal length);
otherwise it returns

true

when the iterations complete.

---

#### public int hashCode()

Returns the hash code value for this list.

**Specified by:**
- hashCode

in interface

Collection

<

E

>
- hashCode

in interface

List

<

E

>

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this list

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Implementation Requirements:**
- This implementation uses exactly the code that is used to define the
list hash function in the documentation for the

List.hashCode()

method.

---

#### protected void removeRange​(int fromIndex,
int toIndex)

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.
Shifts any succeeding elements to the left (reduces their index).
This call shortens the list by

(toIndex - fromIndex)

elements.
(If

toIndex==fromIndex

, this operation has no effect.)

This method is called by the

clear

operation on this list
and its subLists. Overriding this method to take advantage of
the internals of the list implementation can

substantially

improve the performance of the

clear

operation on this list
and its subLists.

**Parameters:**
- fromIndex

- index of first element to be removed
- toIndex

- index after last element to be removed

**Implementation Requirements:**
- This implementation gets a list iterator positioned before

fromIndex

, and repeatedly calls

ListIterator.next

followed by

ListIterator.remove

until the entire range has
been removed.

Note: if

ListIterator.remove

requires linear
time, this implementation requires quadratic time.

---

### Additional Sections

#### Class AbstractList<E>

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractList<E>

java.util.AbstractCollection

<E>

- java.util.AbstractList<E>

java.util.AbstractList<E>

**All Implemented Interfaces:** Iterable

<E>

,

Collection

<E>

,

List

<E>

**Direct Known Subclasses:** AbstractSequentialList

,

ArrayList

,

Vector

```java
public abstract class
AbstractList<E>

extends
AbstractCollection
<E>
implements
List
<E>
```

This class provides a skeletal implementation of the

List

interface to minimize the effort required to implement this interface
backed by a "random access" data store (such as an array). For sequential
access data (such as a linked list),

AbstractSequentialList

should
be used in preference to this class.

To implement an unmodifiable list, the programmer needs only to extend
this class and provide implementations for the

get(int)

and

size()

methods.

To implement a modifiable list, the programmer must additionally
override the

set(int, E)

method (which otherwise
throws an

UnsupportedOperationException

). If the list is
variable-size the programmer must additionally override the

add(int, E)

and

remove(int)

methods.

The programmer should generally provide a void (no argument) and collection
constructor, as per the recommendation in the

Collection

interface
specification.

Unlike the other abstract collection implementations, the programmer does

not

have to provide an iterator implementation; the iterator and
list iterator are implemented by this class, on top of the "random access"
methods:

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

**Since:** 1.2

public abstract class

AbstractList<E>

extends

AbstractCollection

<E>
implements

List

<E>

This class provides a skeletal implementation of the

List

interface to minimize the effort required to implement this interface
backed by a "random access" data store (such as an array). For sequential
access data (such as a linked list),

AbstractSequentialList

should
be used in preference to this class.

To implement an unmodifiable list, the programmer needs only to extend
this class and provide implementations for the

get(int)

and

size()

methods.

To implement a modifiable list, the programmer must additionally
override the

set(int, E)

method (which otherwise
throws an

UnsupportedOperationException

). If the list is
variable-size the programmer must additionally override the

add(int, E)

and

remove(int)

methods.

The programmer should generally provide a void (no argument) and collection
constructor, as per the recommendation in the

Collection

interface
specification.

Unlike the other abstract collection implementations, the programmer does

not

have to provide an iterator implementation; the iterator and
list iterator are implemented by this class, on top of the "random access"
methods:

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

To implement an unmodifiable list, the programmer needs only to extend
this class and provide implementations for the

get(int)

and

size()

methods.

To implement a modifiable list, the programmer must additionally
override the

set(int, E)

method (which otherwise
throws an

UnsupportedOperationException

). If the list is
variable-size the programmer must additionally override the

add(int, E)

and

remove(int)

methods.

The programmer should generally provide a void (no argument) and collection
constructor, as per the recommendation in the

Collection

interface
specification.

Unlike the other abstract collection implementations, the programmer does

not

have to provide an iterator implementation; the iterator and
list iterator are implemented by this class, on top of the "random access"
methods:

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

To implement a modifiable list, the programmer must additionally
override the

set(int, E)

method (which otherwise
throws an

UnsupportedOperationException

). If the list is
variable-size the programmer must additionally override the

add(int, E)

and

remove(int)

methods.

The programmer should generally provide a void (no argument) and collection
constructor, as per the recommendation in the

Collection

interface
specification.

Unlike the other abstract collection implementations, the programmer does

not

have to provide an iterator implementation; the iterator and
list iterator are implemented by this class, on top of the "random access"
methods:

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

The programmer should generally provide a void (no argument) and collection
constructor, as per the recommendation in the

Collection

interface
specification.

Unlike the other abstract collection implementations, the programmer does

not

have to provide an iterator implementation; the iterator and
list iterator are implemented by this class, on top of the "random access"
methods:

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

Unlike the other abstract collection implementations, the programmer does

not

have to provide an iterator implementation; the iterator and
list iterator are implemented by this class, on top of the "random access"
methods:

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if the
collection being implemented admits a more efficient implementation.

This class is a member of the

Java Collections Framework

.

This class is a member of the

Java Collections Framework

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

modCount

The number of times this list has been

structurally modified

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractList

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(int index,

E

element)

Inserts the specified element at the specified position in this list
(optional operation).

boolean

add

​(

E

e)

Appends the specified element to the end of this list (optional
operation).

boolean

addAll

​(int index,

Collection

<? extends

E

> c)

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation).

void

clear

()

Removes all of the elements from this list (optional operation).

boolean

equals

​(

Object

o)

Compares the specified object with this list for equality.

abstract

E

get

​(int index)

Returns the element at the specified position in this list.

int

hashCode

()

Returns the hash code value for this list.

int

indexOf

​(

Object

o)

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.

Iterator

<

E

>

iterator

()

Returns an iterator over the elements in this list in proper sequence.

int

lastIndexOf

​(

Object

o)

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.

ListIterator

<

E

>

listIterator

()

Returns a list iterator over the elements in this list (in proper
sequence).

ListIterator

<

E

>

listIterator

​(int index)

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.

E

remove

​(int index)

Removes the element at the specified position in this list (optional
operation).

protected void

removeRange

​(int fromIndex,
int toIndex)

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.

E

set

​(int index,

E

element)

Replaces the element at the specified position in this list with the
specified element (optional operation).

List

<

E

>

subList

​(int fromIndex,
int toIndex)

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive.

- Methods declared in class java.util.

AbstractCollection

addAll

,

contains

,

containsAll

,

isEmpty

,

remove

,

removeAll

,

retainAll

,

toArray

,

toArray

,

toString

- Methods declared in class java.lang.

Object

clone

,

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

removeIf

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface java.util.

List

addAll

,

contains

,

containsAll

,

isEmpty

,

remove

,

removeAll

,

replaceAll

,

retainAll

,

size

,

sort

,

spliterator

,

toArray

,

toArray

Field Summary

Fields

Modifier and Type

Field

Description

protected int

modCount

The number of times this list has been

structurally modified

.

---

#### Field Summary

The number of times this list has been

structurally modified

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractList

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(int index,

E

element)

Inserts the specified element at the specified position in this list
(optional operation).

boolean

add

​(

E

e)

Appends the specified element to the end of this list (optional
operation).

boolean

addAll

​(int index,

Collection

<? extends

E

> c)

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation).

void

clear

()

Removes all of the elements from this list (optional operation).

boolean

equals

​(

Object

o)

Compares the specified object with this list for equality.

abstract

E

get

​(int index)

Returns the element at the specified position in this list.

int

hashCode

()

Returns the hash code value for this list.

int

indexOf

​(

Object

o)

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.

Iterator

<

E

>

iterator

()

Returns an iterator over the elements in this list in proper sequence.

int

lastIndexOf

​(

Object

o)

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.

ListIterator

<

E

>

listIterator

()

Returns a list iterator over the elements in this list (in proper
sequence).

ListIterator

<

E

>

listIterator

​(int index)

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.

E

remove

​(int index)

Removes the element at the specified position in this list (optional
operation).

protected void

removeRange

​(int fromIndex,
int toIndex)

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.

E

set

​(int index,

E

element)

Replaces the element at the specified position in this list with the
specified element (optional operation).

List

<

E

>

subList

​(int fromIndex,
int toIndex)

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive.

- Methods declared in class java.util.

AbstractCollection

addAll

,

contains

,

containsAll

,

isEmpty

,

remove

,

removeAll

,

retainAll

,

toArray

,

toArray

,

toString

- Methods declared in class java.lang.

Object

clone

,

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

removeIf

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface java.util.

List

addAll

,

contains

,

containsAll

,

isEmpty

,

remove

,

removeAll

,

replaceAll

,

retainAll

,

size

,

sort

,

spliterator

,

toArray

,

toArray

---

#### Method Summary

Inserts the specified element at the specified position in this list
(optional operation).

Appends the specified element to the end of this list (optional
operation).

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation).

Removes all of the elements from this list (optional operation).

Compares the specified object with this list for equality.

Returns the element at the specified position in this list.

Returns the hash code value for this list.

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.

Returns an iterator over the elements in this list in proper sequence.

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.

Returns a list iterator over the elements in this list (in proper
sequence).

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.

Removes the element at the specified position in this list (optional
operation).

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.

Replaces the element at the specified position in this list with the
specified element (optional operation).

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive.

Methods declared in class java.util.

AbstractCollection

addAll

,

contains

,

containsAll

,

isEmpty

,

remove

,

removeAll

,

retainAll

,

toArray

,

toArray

,

toString

---

#### Methods declared in class java.util. AbstractCollection

Methods declared in class java.lang.

Object

clone

,

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

removeIf

,

stream

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.lang.

Iterable

forEach

---

#### Methods declared in interface java.lang. Iterable

Methods declared in interface java.util.

List

addAll

,

contains

,

containsAll

,

isEmpty

,

remove

,

removeAll

,

replaceAll

,

retainAll

,

size

,

sort

,

spliterator

,

toArray

,

toArray

---

#### Methods declared in interface java.util. List

============ FIELD DETAIL ===========

- Field Detail

- modCount

```java
protected transient int modCount
```

The number of times this list has been

structurally modified

.
Structural modifications are those that change the size of the
list, or otherwise perturb it in such a fashion that iterations in
progress may yield incorrect results.

This field is used by the iterator and list iterator implementation
returned by the

iterator

and

listIterator

methods.
If the value of this field changes unexpectedly, the iterator (or list
iterator) will throw a

ConcurrentModificationException

in
response to the

next

,

remove

,

previous

,

set

or

add

operations. This provides

fail-fast

behavior, rather than non-deterministic behavior in
the face of concurrent modification during iteration.

Use of this field by subclasses is optional.

If a subclass
wishes to provide fail-fast iterators (and list iterators), then it
merely has to increment this field in its

add(int, E)

and

remove(int)

methods (and any other methods that it overrides
that result in structural modifications to the list). A single call to

add(int, E)

or

remove(int)

must add no more than
one to this field, or the iterators (and list iterators) will throw
bogus

ConcurrentModificationExceptions

. If an implementation
does not wish to provide fail-fast iterators, this field may be
ignored.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractList

```java
protected AbstractList()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public boolean add​(
E
e)
```

Appends the specified element to the end of this list (optional
operation).

Lists that support this operation may place limitations on what
elements may be added to this list. In particular, some
lists will refuse to add null elements, and others will impose
restrictions on the type of elements that may be added. List
classes should clearly specify in their documentation any restrictions
on what elements may be added.

**Specified by:** add

in interface

Collection

<

E

>
**Specified by:** add

in interface

List

<

E

>
**Overrides:** add

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation calls

add(size(), e)

.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.
**Parameters:** e

- element to be appended to this list
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** UnsupportedOperationException

- if the

add

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of this element
prevents it from being added to this list

- get

```java
public abstract
E
get​(int index)
```

Returns the element at the specified position in this list.

**Specified by:** get

in interface

List

<

E

>
**Parameters:** index

- index of the element to return
**Returns:** the element at the specified position in this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

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
specified element (optional operation).

**Specified by:** set

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- index of the element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** UnsupportedOperationException

- if the

set

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and
this list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

- add

```java
public void add​(int index,

E
element)
```

Inserts the specified element at the specified position in this list
(optional operation). Shifts the element currently at that position
(if any) and any subsequent elements to the right (adds one to their
indices).

**Specified by:** add

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** UnsupportedOperationException

- if the

add

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and
this list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

- remove

```java
public
E
remove​(int index)
```

Removes the element at the specified position in this list (optional
operation). Shifts any subsequent elements to the left (subtracts one
from their indices). Returns the element that was removed from the
list.

**Specified by:** remove

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- the index of the element to be removed
**Returns:** the element previously at the specified position
**Throws:** UnsupportedOperationException

- if the

remove

operation
is not supported by this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

- indexOf

```java
public int indexOf​(
Object
o)
```

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the lowest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:** indexOf

in interface

List

<

E

>
**Implementation Requirements:** This implementation first gets a list iterator (with

listIterator()

). Then, it iterates over the list until the
specified element is found or the end of the list is reached.
**Parameters:** o

- element to search for
**Returns:** the index of the first occurrence of the specified element in
this list, or -1 if this list does not contain the element
**Throws:** ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

- lastIndexOf

```java
public int lastIndexOf​(
Object
o)
```

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the highest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:** lastIndexOf

in interface

List

<

E

>
**Implementation Requirements:** This implementation first gets a list iterator that points to the end
of the list (with

listIterator(size())

). Then, it iterates
backwards over the list until the specified element is found, or the
beginning of the list is reached.
**Parameters:** o

- element to search for
**Returns:** the index of the last occurrence of the specified element in
this list, or -1 if this list does not contain the element
**Throws:** ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

- clear

```java
public void clear()
```

Removes all of the elements from this list (optional operation).
The list will be empty after this call returns.

**Specified by:** clear

in interface

Collection

<

E

>
**Specified by:** clear

in interface

List

<

E

>
**Overrides:** clear

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation calls

removeRange(0, size())

.

Note that this implementation throws an

UnsupportedOperationException

unless

remove(int
index)

or

removeRange(int fromIndex, int toIndex)

is
overridden.
**Throws:** UnsupportedOperationException

- if the

clear

operation
is not supported by this list

- addAll

```java
public boolean addAll​(int index,

Collection
<? extends
E
> c)
```

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation). Shifts the
element currently at that position (if any) and any subsequent
elements to the right (increases their indices). The new elements
will appear in this list in the order that they are returned by the
specified collection's iterator. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress. (Note that this will occur if the specified
collection is this list, and it's nonempty.)

**Specified by:** addAll

in interface

List

<

E

>
**Implementation Requirements:** This implementation gets an iterator over the specified collection
and iterates over it, inserting the elements obtained from the
iterator into this list at the appropriate position, one at a time,
using

add(int, E)

.
Many implementations will override this method for efficiency.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.
**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** UnsupportedOperationException

- if the

addAll

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this list
**Throws:** NullPointerException

- if the specified collection contains one
or more null elements and this list does not permit null
elements, or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

- iterator

```java
public
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this list in proper sequence.

**Specified by:** iterator

in interface

Collection

<

E

>
**Specified by:** iterator

in interface

Iterable

<

E

>
**Specified by:** iterator

in interface

List

<

E

>
**Specified by:** iterator

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation returns a straightforward implementation of the
iterator interface, relying on the backing list's

size()

,

get(int)

, and

remove(int)

methods.

Note that the iterator returned by this method will throw an

UnsupportedOperationException

in response to its

remove

method unless the list's

remove(int)

method is
overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification
for the (protected)

modCount

field.
**Returns:** an iterator over the elements in this list in proper sequence

- listIterator

```java
public
ListIterator
<
E
> listIterator()
```

Returns a list iterator over the elements in this list (in proper
sequence).

**Specified by:** listIterator

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns

listIterator(0)

.
**Returns:** a list iterator over the elements in this list (in proper
sequence)
**See Also:** listIterator(int)

- listIterator

```java
public
ListIterator
<
E
> listIterator​(int index)
```

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.
The specified index indicates the first element that would be
returned by an initial call to

next

.
An initial call to

previous

would
return the element with the specified index minus one.

**Specified by:** listIterator

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns a straightforward implementation of the

ListIterator

interface that extends the implementation of the

Iterator

interface returned by the

iterator()

method.
The

ListIterator

implementation relies on the backing list's

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

methods.

Note that the list iterator returned by this implementation will
throw an

UnsupportedOperationException

in response to its

remove

,

set

and

add

methods unless the
list's

remove(int)

,

set(int, E)

, and

add(int, E)

methods are overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification for
the (protected)

modCount

field.
**Parameters:** index

- index of the first element to be returned from the
list iterator (by a call to

next

)
**Returns:** a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

- subList

```java
public
List
<
E
> subList​(int fromIndex,
int toIndex)
```

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive. (If

fromIndex

and

toIndex

are equal, the returned list is
empty.) The returned list is backed by this list, so non-structural
changes in the returned list are reflected in this list, and vice-versa.
The returned list supports all of the optional list operations supported
by this list.

This method eliminates the need for explicit range operations (of
the sort that commonly exist for arrays). Any operation that expects
a list can be used as a range operation by passing a subList view
instead of a whole list. For example, the following idiom
removes a range of elements from a list:

```java
list.subList(from, to).clear();
```

Similar idioms may be constructed for

indexOf

and

lastIndexOf

, and all of the algorithms in the

Collections

class can be applied to a subList.

The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is

structurally modified

in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)

**Specified by:** subList

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns a list that subclasses

AbstractList

. The subclass stores, in private fields, the
size of the subList (which can change over its lifetime), and the
expected

modCount

value of the backing list. There are two
variants of the subclass, one of which implements

RandomAccess

.
If this list implements

RandomAccess

the returned list will
be an instance of the subclass that implements

RandomAccess

.

The subclass's

set(int, E)

,

get(int)

,

add(int, E)

,

remove(int)

,

addAll(int,
Collection)

and

removeRange(int, int)

methods all
delegate to the corresponding methods on the backing abstract list,
after bounds-checking the index and adjusting for the offset. The

addAll(Collection c)

method merely returns

addAll(size,
c)

.

The

listIterator(int)

method returns a "wrapper object"
over a list iterator on the backing list, which is created with the
corresponding method on the backing list. The

iterator

method
merely returns

listIterator()

, and the

size

method
merely returns the subclass's

size

field.

All methods first check to see if the actual

modCount

of
the backing list is equal to its expected value, and throw a

ConcurrentModificationException

if it is not.
**Parameters:** fromIndex

- low endpoint (inclusive) of the subList
**Parameters:** toIndex

- high endpoint (exclusive) of the subList
**Returns:** a view of the specified range within this list
**Throws:** IndexOutOfBoundsException

- if an endpoint index value is out of range

(fromIndex < 0 || toIndex > size)
**Throws:** IllegalArgumentException

- if the endpoint indices are out of order

(fromIndex > toIndex)

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this list for equality. Returns

true

if and only if the specified object is also a list, both
lists have the same size, and all corresponding pairs of elements in
the two lists are

equal

. (Two elements

e1

and

e2

are

equal

if

(e1==null ? e2==null :
e1.equals(e2))

.) In other words, two lists are defined to be
equal if they contain the same elements in the same order.

**Specified by:** equals

in interface

Collection

<

E

>
**Specified by:** equals

in interface

List

<

E

>
**Overrides:** equals

in class

Object
**Implementation Requirements:** This implementation first checks if the specified object is this
list. If so, it returns

true

; if not, it checks if the
specified object is a list. If not, it returns

false

; if so,
it iterates over both lists, comparing corresponding pairs of elements.
If any comparison returns

false

, this method returns

false

. If either iterator runs out of elements before the
other it returns

false

(as the lists are of unequal length);
otherwise it returns

true

when the iterations complete.
**Parameters:** o

- the object to be compared for equality with this list
**Returns:** true

if the specified object is equal to this list
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this list.

**Specified by:** hashCode

in interface

Collection

<

E

>
**Specified by:** hashCode

in interface

List

<

E

>
**Overrides:** hashCode

in class

Object
**Implementation Requirements:** This implementation uses exactly the code that is used to define the
list hash function in the documentation for the

List.hashCode()

method.
**Returns:** the hash code value for this list
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- removeRange

```java
protected void removeRange​(int fromIndex,
int toIndex)
```

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.
Shifts any succeeding elements to the left (reduces their index).
This call shortens the list by

(toIndex - fromIndex)

elements.
(If

toIndex==fromIndex

, this operation has no effect.)

This method is called by the

clear

operation on this list
and its subLists. Overriding this method to take advantage of
the internals of the list implementation can

substantially

improve the performance of the

clear

operation on this list
and its subLists.

**Implementation Requirements:** This implementation gets a list iterator positioned before

fromIndex

, and repeatedly calls

ListIterator.next

followed by

ListIterator.remove

until the entire range has
been removed.

Note: if

ListIterator.remove

requires linear
time, this implementation requires quadratic time.
**Parameters:** fromIndex

- index of first element to be removed
**Parameters:** toIndex

- index after last element to be removed

Field Detail

- modCount

```java
protected transient int modCount
```

The number of times this list has been

structurally modified

.
Structural modifications are those that change the size of the
list, or otherwise perturb it in such a fashion that iterations in
progress may yield incorrect results.

This field is used by the iterator and list iterator implementation
returned by the

iterator

and

listIterator

methods.
If the value of this field changes unexpectedly, the iterator (or list
iterator) will throw a

ConcurrentModificationException

in
response to the

next

,

remove

,

previous

,

set

or

add

operations. This provides

fail-fast

behavior, rather than non-deterministic behavior in
the face of concurrent modification during iteration.

Use of this field by subclasses is optional.

If a subclass
wishes to provide fail-fast iterators (and list iterators), then it
merely has to increment this field in its

add(int, E)

and

remove(int)

methods (and any other methods that it overrides
that result in structural modifications to the list). A single call to

add(int, E)

or

remove(int)

must add no more than
one to this field, or the iterators (and list iterators) will throw
bogus

ConcurrentModificationExceptions

. If an implementation
does not wish to provide fail-fast iterators, this field may be
ignored.

---

#### Field Detail

modCount

```java
protected transient int modCount
```

The number of times this list has been

structurally modified

.
Structural modifications are those that change the size of the
list, or otherwise perturb it in such a fashion that iterations in
progress may yield incorrect results.

This field is used by the iterator and list iterator implementation
returned by the

iterator

and

listIterator

methods.
If the value of this field changes unexpectedly, the iterator (or list
iterator) will throw a

ConcurrentModificationException

in
response to the

next

,

remove

,

previous

,

set

or

add

operations. This provides

fail-fast

behavior, rather than non-deterministic behavior in
the face of concurrent modification during iteration.

Use of this field by subclasses is optional.

If a subclass
wishes to provide fail-fast iterators (and list iterators), then it
merely has to increment this field in its

add(int, E)

and

remove(int)

methods (and any other methods that it overrides
that result in structural modifications to the list). A single call to

add(int, E)

or

remove(int)

must add no more than
one to this field, or the iterators (and list iterators) will throw
bogus

ConcurrentModificationExceptions

. If an implementation
does not wish to provide fail-fast iterators, this field may be
ignored.

---

#### modCount

protected transient int modCount

The number of times this list has been

structurally modified

.
Structural modifications are those that change the size of the
list, or otherwise perturb it in such a fashion that iterations in
progress may yield incorrect results.

This field is used by the iterator and list iterator implementation
returned by the

iterator

and

listIterator

methods.
If the value of this field changes unexpectedly, the iterator (or list
iterator) will throw a

ConcurrentModificationException

in
response to the

next

,

remove

,

previous

,

set

or

add

operations. This provides

fail-fast

behavior, rather than non-deterministic behavior in
the face of concurrent modification during iteration.

Use of this field by subclasses is optional.

If a subclass
wishes to provide fail-fast iterators (and list iterators), then it
merely has to increment this field in its

add(int, E)

and

remove(int)

methods (and any other methods that it overrides
that result in structural modifications to the list). A single call to

add(int, E)

or

remove(int)

must add no more than
one to this field, or the iterators (and list iterators) will throw
bogus

ConcurrentModificationExceptions

. If an implementation
does not wish to provide fail-fast iterators, this field may be
ignored.

This field is used by the iterator and list iterator implementation
returned by the

iterator

and

listIterator

methods.
If the value of this field changes unexpectedly, the iterator (or list
iterator) will throw a

ConcurrentModificationException

in
response to the

next

,

remove

,

previous

,

set

or

add

operations. This provides

fail-fast

behavior, rather than non-deterministic behavior in
the face of concurrent modification during iteration.

Use of this field by subclasses is optional.

If a subclass
wishes to provide fail-fast iterators (and list iterators), then it
merely has to increment this field in its

add(int, E)

and

remove(int)

methods (and any other methods that it overrides
that result in structural modifications to the list). A single call to

add(int, E)

or

remove(int)

must add no more than
one to this field, or the iterators (and list iterators) will throw
bogus

ConcurrentModificationExceptions

. If an implementation
does not wish to provide fail-fast iterators, this field may be
ignored.

Use of this field by subclasses is optional.

If a subclass
wishes to provide fail-fast iterators (and list iterators), then it
merely has to increment this field in its

add(int, E)

and

remove(int)

methods (and any other methods that it overrides
that result in structural modifications to the list). A single call to

add(int, E)

or

remove(int)

must add no more than
one to this field, or the iterators (and list iterators) will throw
bogus

ConcurrentModificationExceptions

. If an implementation
does not wish to provide fail-fast iterators, this field may be
ignored.

Constructor Detail

- AbstractList

```java
protected AbstractList()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

AbstractList

```java
protected AbstractList()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### AbstractList

protected AbstractList()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- add

```java
public boolean add​(
E
e)
```

Appends the specified element to the end of this list (optional
operation).

Lists that support this operation may place limitations on what
elements may be added to this list. In particular, some
lists will refuse to add null elements, and others will impose
restrictions on the type of elements that may be added. List
classes should clearly specify in their documentation any restrictions
on what elements may be added.

**Specified by:** add

in interface

Collection

<

E

>
**Specified by:** add

in interface

List

<

E

>
**Overrides:** add

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation calls

add(size(), e)

.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.
**Parameters:** e

- element to be appended to this list
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** UnsupportedOperationException

- if the

add

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of this element
prevents it from being added to this list

- get

```java
public abstract
E
get​(int index)
```

Returns the element at the specified position in this list.

**Specified by:** get

in interface

List

<

E

>
**Parameters:** index

- index of the element to return
**Returns:** the element at the specified position in this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

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
specified element (optional operation).

**Specified by:** set

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- index of the element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** UnsupportedOperationException

- if the

set

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and
this list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

- add

```java
public void add​(int index,

E
element)
```

Inserts the specified element at the specified position in this list
(optional operation). Shifts the element currently at that position
(if any) and any subsequent elements to the right (adds one to their
indices).

**Specified by:** add

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** UnsupportedOperationException

- if the

add

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and
this list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

- remove

```java
public
E
remove​(int index)
```

Removes the element at the specified position in this list (optional
operation). Shifts any subsequent elements to the left (subtracts one
from their indices). Returns the element that was removed from the
list.

**Specified by:** remove

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- the index of the element to be removed
**Returns:** the element previously at the specified position
**Throws:** UnsupportedOperationException

- if the

remove

operation
is not supported by this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

- indexOf

```java
public int indexOf​(
Object
o)
```

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the lowest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:** indexOf

in interface

List

<

E

>
**Implementation Requirements:** This implementation first gets a list iterator (with

listIterator()

). Then, it iterates over the list until the
specified element is found or the end of the list is reached.
**Parameters:** o

- element to search for
**Returns:** the index of the first occurrence of the specified element in
this list, or -1 if this list does not contain the element
**Throws:** ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

- lastIndexOf

```java
public int lastIndexOf​(
Object
o)
```

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the highest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:** lastIndexOf

in interface

List

<

E

>
**Implementation Requirements:** This implementation first gets a list iterator that points to the end
of the list (with

listIterator(size())

). Then, it iterates
backwards over the list until the specified element is found, or the
beginning of the list is reached.
**Parameters:** o

- element to search for
**Returns:** the index of the last occurrence of the specified element in
this list, or -1 if this list does not contain the element
**Throws:** ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

- clear

```java
public void clear()
```

Removes all of the elements from this list (optional operation).
The list will be empty after this call returns.

**Specified by:** clear

in interface

Collection

<

E

>
**Specified by:** clear

in interface

List

<

E

>
**Overrides:** clear

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation calls

removeRange(0, size())

.

Note that this implementation throws an

UnsupportedOperationException

unless

remove(int
index)

or

removeRange(int fromIndex, int toIndex)

is
overridden.
**Throws:** UnsupportedOperationException

- if the

clear

operation
is not supported by this list

- addAll

```java
public boolean addAll​(int index,

Collection
<? extends
E
> c)
```

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation). Shifts the
element currently at that position (if any) and any subsequent
elements to the right (increases their indices). The new elements
will appear in this list in the order that they are returned by the
specified collection's iterator. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress. (Note that this will occur if the specified
collection is this list, and it's nonempty.)

**Specified by:** addAll

in interface

List

<

E

>
**Implementation Requirements:** This implementation gets an iterator over the specified collection
and iterates over it, inserting the elements obtained from the
iterator into this list at the appropriate position, one at a time,
using

add(int, E)

.
Many implementations will override this method for efficiency.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.
**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** UnsupportedOperationException

- if the

addAll

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this list
**Throws:** NullPointerException

- if the specified collection contains one
or more null elements and this list does not permit null
elements, or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

- iterator

```java
public
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this list in proper sequence.

**Specified by:** iterator

in interface

Collection

<

E

>
**Specified by:** iterator

in interface

Iterable

<

E

>
**Specified by:** iterator

in interface

List

<

E

>
**Specified by:** iterator

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation returns a straightforward implementation of the
iterator interface, relying on the backing list's

size()

,

get(int)

, and

remove(int)

methods.

Note that the iterator returned by this method will throw an

UnsupportedOperationException

in response to its

remove

method unless the list's

remove(int)

method is
overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification
for the (protected)

modCount

field.
**Returns:** an iterator over the elements in this list in proper sequence

- listIterator

```java
public
ListIterator
<
E
> listIterator()
```

Returns a list iterator over the elements in this list (in proper
sequence).

**Specified by:** listIterator

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns

listIterator(0)

.
**Returns:** a list iterator over the elements in this list (in proper
sequence)
**See Also:** listIterator(int)

- listIterator

```java
public
ListIterator
<
E
> listIterator​(int index)
```

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.
The specified index indicates the first element that would be
returned by an initial call to

next

.
An initial call to

previous

would
return the element with the specified index minus one.

**Specified by:** listIterator

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns a straightforward implementation of the

ListIterator

interface that extends the implementation of the

Iterator

interface returned by the

iterator()

method.
The

ListIterator

implementation relies on the backing list's

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

methods.

Note that the list iterator returned by this implementation will
throw an

UnsupportedOperationException

in response to its

remove

,

set

and

add

methods unless the
list's

remove(int)

,

set(int, E)

, and

add(int, E)

methods are overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification for
the (protected)

modCount

field.
**Parameters:** index

- index of the first element to be returned from the
list iterator (by a call to

next

)
**Returns:** a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

- subList

```java
public
List
<
E
> subList​(int fromIndex,
int toIndex)
```

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive. (If

fromIndex

and

toIndex

are equal, the returned list is
empty.) The returned list is backed by this list, so non-structural
changes in the returned list are reflected in this list, and vice-versa.
The returned list supports all of the optional list operations supported
by this list.

This method eliminates the need for explicit range operations (of
the sort that commonly exist for arrays). Any operation that expects
a list can be used as a range operation by passing a subList view
instead of a whole list. For example, the following idiom
removes a range of elements from a list:

```java
list.subList(from, to).clear();
```

Similar idioms may be constructed for

indexOf

and

lastIndexOf

, and all of the algorithms in the

Collections

class can be applied to a subList.

The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is

structurally modified

in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)

**Specified by:** subList

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns a list that subclasses

AbstractList

. The subclass stores, in private fields, the
size of the subList (which can change over its lifetime), and the
expected

modCount

value of the backing list. There are two
variants of the subclass, one of which implements

RandomAccess

.
If this list implements

RandomAccess

the returned list will
be an instance of the subclass that implements

RandomAccess

.

The subclass's

set(int, E)

,

get(int)

,

add(int, E)

,

remove(int)

,

addAll(int,
Collection)

and

removeRange(int, int)

methods all
delegate to the corresponding methods on the backing abstract list,
after bounds-checking the index and adjusting for the offset. The

addAll(Collection c)

method merely returns

addAll(size,
c)

.

The

listIterator(int)

method returns a "wrapper object"
over a list iterator on the backing list, which is created with the
corresponding method on the backing list. The

iterator

method
merely returns

listIterator()

, and the

size

method
merely returns the subclass's

size

field.

All methods first check to see if the actual

modCount

of
the backing list is equal to its expected value, and throw a

ConcurrentModificationException

if it is not.
**Parameters:** fromIndex

- low endpoint (inclusive) of the subList
**Parameters:** toIndex

- high endpoint (exclusive) of the subList
**Returns:** a view of the specified range within this list
**Throws:** IndexOutOfBoundsException

- if an endpoint index value is out of range

(fromIndex < 0 || toIndex > size)
**Throws:** IllegalArgumentException

- if the endpoint indices are out of order

(fromIndex > toIndex)

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this list for equality. Returns

true

if and only if the specified object is also a list, both
lists have the same size, and all corresponding pairs of elements in
the two lists are

equal

. (Two elements

e1

and

e2

are

equal

if

(e1==null ? e2==null :
e1.equals(e2))

.) In other words, two lists are defined to be
equal if they contain the same elements in the same order.

**Specified by:** equals

in interface

Collection

<

E

>
**Specified by:** equals

in interface

List

<

E

>
**Overrides:** equals

in class

Object
**Implementation Requirements:** This implementation first checks if the specified object is this
list. If so, it returns

true

; if not, it checks if the
specified object is a list. If not, it returns

false

; if so,
it iterates over both lists, comparing corresponding pairs of elements.
If any comparison returns

false

, this method returns

false

. If either iterator runs out of elements before the
other it returns

false

(as the lists are of unequal length);
otherwise it returns

true

when the iterations complete.
**Parameters:** o

- the object to be compared for equality with this list
**Returns:** true

if the specified object is equal to this list
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this list.

**Specified by:** hashCode

in interface

Collection

<

E

>
**Specified by:** hashCode

in interface

List

<

E

>
**Overrides:** hashCode

in class

Object
**Implementation Requirements:** This implementation uses exactly the code that is used to define the
list hash function in the documentation for the

List.hashCode()

method.
**Returns:** the hash code value for this list
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- removeRange

```java
protected void removeRange​(int fromIndex,
int toIndex)
```

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.
Shifts any succeeding elements to the left (reduces their index).
This call shortens the list by

(toIndex - fromIndex)

elements.
(If

toIndex==fromIndex

, this operation has no effect.)

This method is called by the

clear

operation on this list
and its subLists. Overriding this method to take advantage of
the internals of the list implementation can

substantially

improve the performance of the

clear

operation on this list
and its subLists.

**Implementation Requirements:** This implementation gets a list iterator positioned before

fromIndex

, and repeatedly calls

ListIterator.next

followed by

ListIterator.remove

until the entire range has
been removed.

Note: if

ListIterator.remove

requires linear
time, this implementation requires quadratic time.
**Parameters:** fromIndex

- index of first element to be removed
**Parameters:** toIndex

- index after last element to be removed

---

#### Method Detail

add

```java
public boolean add​(
E
e)
```

Appends the specified element to the end of this list (optional
operation).

Lists that support this operation may place limitations on what
elements may be added to this list. In particular, some
lists will refuse to add null elements, and others will impose
restrictions on the type of elements that may be added. List
classes should clearly specify in their documentation any restrictions
on what elements may be added.

**Specified by:** add

in interface

Collection

<

E

>
**Specified by:** add

in interface

List

<

E

>
**Overrides:** add

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation calls

add(size(), e)

.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.
**Parameters:** e

- element to be appended to this list
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** UnsupportedOperationException

- if the

add

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of this element
prevents it from being added to this list

---

#### add

public boolean add​(

E

e)

Appends the specified element to the end of this list (optional
operation).

Lists that support this operation may place limitations on what
elements may be added to this list. In particular, some
lists will refuse to add null elements, and others will impose
restrictions on the type of elements that may be added. List
classes should clearly specify in their documentation any restrictions
on what elements may be added.

Lists that support this operation may place limitations on what
elements may be added to this list. In particular, some
lists will refuse to add null elements, and others will impose
restrictions on the type of elements that may be added. List
classes should clearly specify in their documentation any restrictions
on what elements may be added.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.

get

```java
public abstract
E
get​(int index)
```

Returns the element at the specified position in this list.

**Specified by:** get

in interface

List

<

E

>
**Parameters:** index

- index of the element to return
**Returns:** the element at the specified position in this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

---

#### get

public abstract

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
specified element (optional operation).

**Specified by:** set

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- index of the element to replace
**Parameters:** element

- element to be stored at the specified position
**Returns:** the element previously at the specified position
**Throws:** UnsupportedOperationException

- if the

set

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and
this list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

---

#### set

public

E

set​(int index,

E

element)

Replaces the element at the specified position in this list with the
specified element (optional operation).

add

```java
public void add​(int index,

E
element)
```

Inserts the specified element at the specified position in this list
(optional operation). Shifts the element currently at that position
(if any) and any subsequent elements to the right (adds one to their
indices).

**Specified by:** add

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- index at which the specified element is to be inserted
**Parameters:** element

- element to be inserted
**Throws:** UnsupportedOperationException

- if the

add

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this list
**Throws:** NullPointerException

- if the specified element is null and
this list does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

---

#### add

public void add​(int index,

E

element)

Inserts the specified element at the specified position in this list
(optional operation). Shifts the element currently at that position
(if any) and any subsequent elements to the right (adds one to their
indices).

remove

```java
public
E
remove​(int index)
```

Removes the element at the specified position in this list (optional
operation). Shifts any subsequent elements to the left (subtracts one
from their indices). Returns the element that was removed from the
list.

**Specified by:** remove

in interface

List

<

E

>
**Implementation Requirements:** This implementation always throws an

UnsupportedOperationException

.
**Parameters:** index

- the index of the element to be removed
**Returns:** the element previously at the specified position
**Throws:** UnsupportedOperationException

- if the

remove

operation
is not supported by this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index >= size()

)

---

#### remove

public

E

remove​(int index)

Removes the element at the specified position in this list (optional
operation). Shifts any subsequent elements to the left (subtracts one
from their indices). Returns the element that was removed from the
list.

indexOf

```java
public int indexOf​(
Object
o)
```

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the lowest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:** indexOf

in interface

List

<

E

>
**Implementation Requirements:** This implementation first gets a list iterator (with

listIterator()

). Then, it iterates over the list until the
specified element is found or the end of the list is reached.
**Parameters:** o

- element to search for
**Returns:** the index of the first occurrence of the specified element in
this list, or -1 if this list does not contain the element
**Throws:** ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

---

#### indexOf

public int indexOf​(

Object

o)

Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the lowest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

lastIndexOf

```java
public int lastIndexOf​(
Object
o)
```

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the highest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

**Specified by:** lastIndexOf

in interface

List

<

E

>
**Implementation Requirements:** This implementation first gets a list iterator that points to the end
of the list (with

listIterator(size())

). Then, it iterates
backwards over the list until the specified element is found, or the
beginning of the list is reached.
**Parameters:** o

- element to search for
**Returns:** the index of the last occurrence of the specified element in
this list, or -1 if this list does not contain the element
**Throws:** ClassCastException

- if the type of the specified element
is incompatible with this list
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
list does not permit null elements
(

optional

)

---

#### lastIndexOf

public int lastIndexOf​(

Object

o)

Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the highest index

i

such that

Objects.equals(o, get(i))

,
or -1 if there is no such index.

clear

```java
public void clear()
```

Removes all of the elements from this list (optional operation).
The list will be empty after this call returns.

**Specified by:** clear

in interface

Collection

<

E

>
**Specified by:** clear

in interface

List

<

E

>
**Overrides:** clear

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation calls

removeRange(0, size())

.

Note that this implementation throws an

UnsupportedOperationException

unless

remove(int
index)

or

removeRange(int fromIndex, int toIndex)

is
overridden.
**Throws:** UnsupportedOperationException

- if the

clear

operation
is not supported by this list

---

#### clear

public void clear()

Removes all of the elements from this list (optional operation).
The list will be empty after this call returns.

Note that this implementation throws an

UnsupportedOperationException

unless

remove(int
index)

or

removeRange(int fromIndex, int toIndex)

is
overridden.

addAll

```java
public boolean addAll​(int index,

Collection
<? extends
E
> c)
```

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation). Shifts the
element currently at that position (if any) and any subsequent
elements to the right (increases their indices). The new elements
will appear in this list in the order that they are returned by the
specified collection's iterator. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress. (Note that this will occur if the specified
collection is this list, and it's nonempty.)

**Specified by:** addAll

in interface

List

<

E

>
**Implementation Requirements:** This implementation gets an iterator over the specified collection
and iterates over it, inserting the elements obtained from the
iterator into this list at the appropriate position, one at a time,
using

add(int, E)

.
Many implementations will override this method for efficiency.

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.
**Parameters:** index

- index at which to insert the first element from the
specified collection
**Parameters:** c

- collection containing elements to be added to this list
**Returns:** true

if this list changed as a result of the call
**Throws:** UnsupportedOperationException

- if the

addAll

operation
is not supported by this list
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this list
**Throws:** NullPointerException

- if the specified collection contains one
or more null elements and this list does not permit null
elements, or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

---

#### addAll

public boolean addAll​(int index,

Collection

<? extends

E

> c)

Inserts all of the elements in the specified collection into this
list at the specified position (optional operation). Shifts the
element currently at that position (if any) and any subsequent
elements to the right (increases their indices). The new elements
will appear in this list in the order that they are returned by the
specified collection's iterator. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress. (Note that this will occur if the specified
collection is this list, and it's nonempty.)

Note that this implementation throws an

UnsupportedOperationException

unless

add(int, E)

is overridden.

iterator

```java
public
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this list in proper sequence.

**Specified by:** iterator

in interface

Collection

<

E

>
**Specified by:** iterator

in interface

Iterable

<

E

>
**Specified by:** iterator

in interface

List

<

E

>
**Specified by:** iterator

in class

AbstractCollection

<

E

>
**Implementation Requirements:** This implementation returns a straightforward implementation of the
iterator interface, relying on the backing list's

size()

,

get(int)

, and

remove(int)

methods.

Note that the iterator returned by this method will throw an

UnsupportedOperationException

in response to its

remove

method unless the list's

remove(int)

method is
overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification
for the (protected)

modCount

field.
**Returns:** an iterator over the elements in this list in proper sequence

---

#### iterator

public

Iterator

<

E

> iterator()

Returns an iterator over the elements in this list in proper sequence.

Note that the iterator returned by this method will throw an

UnsupportedOperationException

in response to its

remove

method unless the list's

remove(int)

method is
overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification
for the (protected)

modCount

field.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification
for the (protected)

modCount

field.

listIterator

```java
public
ListIterator
<
E
> listIterator()
```

Returns a list iterator over the elements in this list (in proper
sequence).

**Specified by:** listIterator

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns

listIterator(0)

.
**Returns:** a list iterator over the elements in this list (in proper
sequence)
**See Also:** listIterator(int)

---

#### listIterator

public

ListIterator

<

E

> listIterator()

Returns a list iterator over the elements in this list (in proper
sequence).

listIterator

```java
public
ListIterator
<
E
> listIterator​(int index)
```

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.
The specified index indicates the first element that would be
returned by an initial call to

next

.
An initial call to

previous

would
return the element with the specified index minus one.

**Specified by:** listIterator

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns a straightforward implementation of the

ListIterator

interface that extends the implementation of the

Iterator

interface returned by the

iterator()

method.
The

ListIterator

implementation relies on the backing list's

get(int)

,

set(int, E)

,

add(int, E)

and

remove(int)

methods.

Note that the list iterator returned by this implementation will
throw an

UnsupportedOperationException

in response to its

remove

,

set

and

add

methods unless the
list's

remove(int)

,

set(int, E)

, and

add(int, E)

methods are overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification for
the (protected)

modCount

field.
**Parameters:** index

- index of the first element to be returned from the
list iterator (by a call to

next

)
**Returns:** a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

index < 0 || index > size()

)

---

#### listIterator

public

ListIterator

<

E

> listIterator​(int index)

Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.
The specified index indicates the first element that would be
returned by an initial call to

next

.
An initial call to

previous

would
return the element with the specified index minus one.

Note that the list iterator returned by this implementation will
throw an

UnsupportedOperationException

in response to its

remove

,

set

and

add

methods unless the
list's

remove(int)

,

set(int, E)

, and

add(int, E)

methods are overridden.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification for
the (protected)

modCount

field.

This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification for
the (protected)

modCount

field.

subList

```java
public
List
<
E
> subList​(int fromIndex,
int toIndex)
```

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive. (If

fromIndex

and

toIndex

are equal, the returned list is
empty.) The returned list is backed by this list, so non-structural
changes in the returned list are reflected in this list, and vice-versa.
The returned list supports all of the optional list operations supported
by this list.

This method eliminates the need for explicit range operations (of
the sort that commonly exist for arrays). Any operation that expects
a list can be used as a range operation by passing a subList view
instead of a whole list. For example, the following idiom
removes a range of elements from a list:

```java
list.subList(from, to).clear();
```

Similar idioms may be constructed for

indexOf

and

lastIndexOf

, and all of the algorithms in the

Collections

class can be applied to a subList.

The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is

structurally modified

in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)

**Specified by:** subList

in interface

List

<

E

>
**Implementation Requirements:** This implementation returns a list that subclasses

AbstractList

. The subclass stores, in private fields, the
size of the subList (which can change over its lifetime), and the
expected

modCount

value of the backing list. There are two
variants of the subclass, one of which implements

RandomAccess

.
If this list implements

RandomAccess

the returned list will
be an instance of the subclass that implements

RandomAccess

.

The subclass's

set(int, E)

,

get(int)

,

add(int, E)

,

remove(int)

,

addAll(int,
Collection)

and

removeRange(int, int)

methods all
delegate to the corresponding methods on the backing abstract list,
after bounds-checking the index and adjusting for the offset. The

addAll(Collection c)

method merely returns

addAll(size,
c)

.

The

listIterator(int)

method returns a "wrapper object"
over a list iterator on the backing list, which is created with the
corresponding method on the backing list. The

iterator

method
merely returns

listIterator()

, and the

size

method
merely returns the subclass's

size

field.

All methods first check to see if the actual

modCount

of
the backing list is equal to its expected value, and throw a

ConcurrentModificationException

if it is not.
**Parameters:** fromIndex

- low endpoint (inclusive) of the subList
**Parameters:** toIndex

- high endpoint (exclusive) of the subList
**Returns:** a view of the specified range within this list
**Throws:** IndexOutOfBoundsException

- if an endpoint index value is out of range

(fromIndex < 0 || toIndex > size)
**Throws:** IllegalArgumentException

- if the endpoint indices are out of order

(fromIndex > toIndex)

---

#### subList

public

List

<

E

> subList​(int fromIndex,
int toIndex)

Returns a view of the portion of this list between the specified

fromIndex

, inclusive, and

toIndex

, exclusive. (If

fromIndex

and

toIndex

are equal, the returned list is
empty.) The returned list is backed by this list, so non-structural
changes in the returned list are reflected in this list, and vice-versa.
The returned list supports all of the optional list operations supported
by this list.

This method eliminates the need for explicit range operations (of
the sort that commonly exist for arrays). Any operation that expects
a list can be used as a range operation by passing a subList view
instead of a whole list. For example, the following idiom
removes a range of elements from a list:

```java
list.subList(from, to).clear();
```

Similar idioms may be constructed for

indexOf

and

lastIndexOf

, and all of the algorithms in the

Collections

class can be applied to a subList.

The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is

structurally modified

in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)

This method eliminates the need for explicit range operations (of
the sort that commonly exist for arrays). Any operation that expects
a list can be used as a range operation by passing a subList view
instead of a whole list. For example, the following idiom
removes a range of elements from a list:

```java
list.subList(from, to).clear();
```

Similar idioms may be constructed for

indexOf

and

lastIndexOf

, and all of the algorithms in the

Collections

class can be applied to a subList.

The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is

structurally modified

in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)

list.subList(from, to).clear();

The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is

structurally modified

in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)

The subclass's

set(int, E)

,

get(int)

,

add(int, E)

,

remove(int)

,

addAll(int,
Collection)

and

removeRange(int, int)

methods all
delegate to the corresponding methods on the backing abstract list,
after bounds-checking the index and adjusting for the offset. The

addAll(Collection c)

method merely returns

addAll(size,
c)

.

The

listIterator(int)

method returns a "wrapper object"
over a list iterator on the backing list, which is created with the
corresponding method on the backing list. The

iterator

method
merely returns

listIterator()

, and the

size

method
merely returns the subclass's

size

field.

All methods first check to see if the actual

modCount

of
the backing list is equal to its expected value, and throw a

ConcurrentModificationException

if it is not.

The

listIterator(int)

method returns a "wrapper object"
over a list iterator on the backing list, which is created with the
corresponding method on the backing list. The

iterator

method
merely returns

listIterator()

, and the

size

method
merely returns the subclass's

size

field.

All methods first check to see if the actual

modCount

of
the backing list is equal to its expected value, and throw a

ConcurrentModificationException

if it is not.

All methods first check to see if the actual

modCount

of
the backing list is equal to its expected value, and throw a

ConcurrentModificationException

if it is not.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this list for equality. Returns

true

if and only if the specified object is also a list, both
lists have the same size, and all corresponding pairs of elements in
the two lists are

equal

. (Two elements

e1

and

e2

are

equal

if

(e1==null ? e2==null :
e1.equals(e2))

.) In other words, two lists are defined to be
equal if they contain the same elements in the same order.

**Specified by:** equals

in interface

Collection

<

E

>
**Specified by:** equals

in interface

List

<

E

>
**Overrides:** equals

in class

Object
**Implementation Requirements:** This implementation first checks if the specified object is this
list. If so, it returns

true

; if not, it checks if the
specified object is a list. If not, it returns

false

; if so,
it iterates over both lists, comparing corresponding pairs of elements.
If any comparison returns

false

, this method returns

false

. If either iterator runs out of elements before the
other it returns

false

(as the lists are of unequal length);
otherwise it returns

true

when the iterations complete.
**Parameters:** o

- the object to be compared for equality with this list
**Returns:** true

if the specified object is equal to this list
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares the specified object with this list for equality. Returns

true

if and only if the specified object is also a list, both
lists have the same size, and all corresponding pairs of elements in
the two lists are

equal

. (Two elements

e1

and

e2

are

equal

if

(e1==null ? e2==null :
e1.equals(e2))

.) In other words, two lists are defined to be
equal if they contain the same elements in the same order.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this list.

**Specified by:** hashCode

in interface

Collection

<

E

>
**Specified by:** hashCode

in interface

List

<

E

>
**Overrides:** hashCode

in class

Object
**Implementation Requirements:** This implementation uses exactly the code that is used to define the
list hash function in the documentation for the

List.hashCode()

method.
**Returns:** the hash code value for this list
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this list.

removeRange

```java
protected void removeRange​(int fromIndex,
int toIndex)
```

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.
Shifts any succeeding elements to the left (reduces their index).
This call shortens the list by

(toIndex - fromIndex)

elements.
(If

toIndex==fromIndex

, this operation has no effect.)

This method is called by the

clear

operation on this list
and its subLists. Overriding this method to take advantage of
the internals of the list implementation can

substantially

improve the performance of the

clear

operation on this list
and its subLists.

**Implementation Requirements:** This implementation gets a list iterator positioned before

fromIndex

, and repeatedly calls

ListIterator.next

followed by

ListIterator.remove

until the entire range has
been removed.

Note: if

ListIterator.remove

requires linear
time, this implementation requires quadratic time.
**Parameters:** fromIndex

- index of first element to be removed
**Parameters:** toIndex

- index after last element to be removed

---

#### removeRange

protected void removeRange​(int fromIndex,
int toIndex)

Removes from this list all of the elements whose index is between

fromIndex

, inclusive, and

toIndex

, exclusive.
Shifts any succeeding elements to the left (reduces their index).
This call shortens the list by

(toIndex - fromIndex)

elements.
(If

toIndex==fromIndex

, this operation has no effect.)

This method is called by the

clear

operation on this list
and its subLists. Overriding this method to take advantage of
the internals of the list implementation can

substantially

improve the performance of the

clear

operation on this list
and its subLists.

This method is called by the

clear

operation on this list
and its subLists. Overriding this method to take advantage of
the internals of the list implementation can

substantially

improve the performance of the

clear

operation on this list
and its subLists.

---

