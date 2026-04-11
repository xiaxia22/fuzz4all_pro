# Interface Deque<E>

**Source:** `java.base\java\util\Deque.html`

### Class Description

```java
public interface
Deque<E>

extends
Queue
<E>
```

A linear collection that supports element insertion and removal at
both ends. The name

deque

is short for "double ended queue"
and is usually pronounced "deck". Most

Deque

implementations place no fixed limits on the number of elements
they may contain, but this interface supports capacity-restricted
deques as well as those with no fixed size limit.

This interface defines methods to access the elements at both
ends of the deque. Methods are provided to insert, remove, and
examine the element. Each of these methods exists in two forms:
one throws an exception if the operation fails, the other returns a
special value (either

null

or

false

, depending on
the operation). The latter form of the insert operation is
designed specifically for use with capacity-restricted

Deque

implementations; in most implementations, insert
operations cannot fail.

The twelve methods described above are summarized in the
following table:

Summary of Deque methods

First Element (Head)

Last Element (Tail)

Throws exception

Special value

Throws exception

Special value

Insert

addFirst(e)

offerFirst(e)

addLast(e)

offerLast(e)

Remove

removeFirst()

pollFirst()

removeLast()

pollLast()

Examine

getFirst()

peekFirst()

getLast()

peekLast()

This interface extends the

Queue

interface. When a deque is
used as a queue, FIFO (First-In-First-Out) behavior results. Elements are
added at the end of the deque and removed from the beginning. The methods
inherited from the

Queue

interface are precisely equivalent to

Deque

methods as indicated in the following table:

Comparison of Queue and Deque methods

Queue

Method

Equivalent

Deque

Method

add(e)

addLast(e)

offer(e)

offerLast(e)

remove()

removeFirst()

poll()

pollFirst()

element()

getFirst()

peek()

peekFirst()

Deques can also be used as LIFO (Last-In-First-Out) stacks. This
interface should be used in preference to the legacy

Stack

class.
When a deque is used as a stack, elements are pushed and popped from the
beginning of the deque. Stack methods are equivalent to

Deque

methods as indicated in the table below:

Comparison of Stack and Deque methods

Stack Method

Equivalent

Deque

Method

push(e)

addFirst(e)

pop()

removeFirst()

peek()

getFirst()

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

**Type Parameters:** E

- the type of elements held in this deque

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addFirst​(
E
e)

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerFirst(E)

.

**Parameters:**
- e

- the element to add

**Throws:**
- IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
- ClassCastException

- if the class of the specified element
prevents it from being added to this deque
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### void addLast​(
E
e)

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerLast(E)

.

This method is equivalent to

add(E)

.

**Parameters:**
- e

- the element to add

**Throws:**
- IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
- ClassCastException

- if the class of the specified element
prevents it from being added to this deque
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### boolean offerFirst​(
E
e)

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addFirst(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:**
- e

- the element to add

**Returns:**
- true

if the element was added to this deque, else

false

**Throws:**
- ClassCastException

- if the class of the specified element
prevents it from being added to this deque
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### boolean offerLast​(
E
e)

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addLast(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:**
- e

- the element to add

**Returns:**
- true

if the element was added to this deque, else

false

**Throws:**
- ClassCastException

- if the class of the specified element
prevents it from being added to this deque
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### E
removeFirst()

Retrieves and removes the first element of this deque. This method
differs from

pollFirst

only in that it throws an
exception if this deque is empty.

**Returns:**
- the head of this deque

**Throws:**
- NoSuchElementException

- if this deque is empty

---

#### E
removeLast()

Retrieves and removes the last element of this deque. This method
differs from

pollLast

only in that it throws an
exception if this deque is empty.

**Returns:**
- the tail of this deque

**Throws:**
- NoSuchElementException

- if this deque is empty

---

#### E
pollFirst()

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

**Returns:**
- the head of this deque, or

null

if this deque is empty

---

#### E
pollLast()

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

**Returns:**
- the tail of this deque, or

null

if this deque is empty

---

#### E
getFirst()

Retrieves, but does not remove, the first element of this deque.

This method differs from

peekFirst

only in that it
throws an exception if this deque is empty.

**Returns:**
- the head of this deque

**Throws:**
- NoSuchElementException

- if this deque is empty

---

#### E
getLast()

Retrieves, but does not remove, the last element of this deque.
This method differs from

peekLast

only in that it
throws an exception if this deque is empty.

**Returns:**
- the tail of this deque

**Throws:**
- NoSuchElementException

- if this deque is empty

---

#### E
peekFirst()

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

**Returns:**
- the head of this deque, or

null

if this deque is empty

---

#### E
peekLast()

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

**Returns:**
- the tail of this deque, or

null

if this deque is empty

---

#### boolean removeFirstOccurrence​(
Object
o)

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:**
- o

- element to be removed from this deque, if present

**Returns:**
- true

if an element was removed as a result of this call

**Throws:**
- ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### boolean removeLastOccurrence​(
Object
o)

Removes the last occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the last element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:**
- o

- element to be removed from this deque, if present

**Returns:**
- true

if an element was removed as a result of this call

**Throws:**
- ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### boolean add​(
E
e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.
When using a capacity-restricted deque, it is generally preferable to
use

offer

.

This method is equivalent to

addLast(E)

.

**Specified by:**
- add

in interface

Collection

<

E

>
- add

in interface

Queue

<

E

>

**Parameters:**
- e

- the element to add

**Returns:**
- true

(as specified by

Collection.add(E)

)

**Throws:**
- IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
- ClassCastException

- if the class of the specified element
prevents it from being added to this deque
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### boolean offer​(
E
e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available. When using a capacity-restricted deque, this method is
generally preferable to the

add(E)

method, which can fail to
insert an element only by throwing an exception.

This method is equivalent to

offerLast(E)

.

**Specified by:**
- offer

in interface

Queue

<

E

>

**Parameters:**
- e

- the element to add

**Returns:**
- true

if the element was added to this deque, else

false

**Throws:**
- ClassCastException

- if the class of the specified element
prevents it from being added to this deque
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### E
remove()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).
This method differs from

poll()

only in that it
throws an exception if this deque is empty.

This method is equivalent to

removeFirst()

.

**Specified by:**
- remove

in interface

Queue

<

E

>

**Returns:**
- the head of the queue represented by this deque

**Throws:**
- NoSuchElementException

- if this deque is empty

---

#### E
poll()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

This method is equivalent to

pollFirst()

.

**Specified by:**
- poll

in interface

Queue

<

E

>

**Returns:**
- the first element of this deque, or

null

if
this deque is empty

---

#### E
element()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).
This method differs from

peek

only in that it throws an
exception if this deque is empty.

This method is equivalent to

getFirst()

.

**Specified by:**
- element

in interface

Queue

<

E

>

**Returns:**
- the head of the queue represented by this deque

**Throws:**
- NoSuchElementException

- if this deque is empty

---

#### E
peek()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

This method is equivalent to

peekFirst()

.

**Specified by:**
- peek

in interface

Queue

<

E

>

**Returns:**
- the head of the queue represented by this deque, or

null

if this deque is empty

---

#### boolean addAll​(
Collection
<? extends
E
> c)

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

When using a capacity-restricted deque, it is generally preferable
to call

offer

separately on each element.

An exception encountered while trying to add an element may result
in only some of the elements having been successfully added when
the associated exception is thrown.

**Specified by:**
- addAll

in interface

Collection

<

E

>

**Parameters:**
- c

- the elements to be inserted into this deque

**Returns:**
- true

if this deque changed as a result of the call

**Throws:**
- IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions
- ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this deque
- NullPointerException

- if the specified collection contains a
null element and this deque does not permit null elements,
or if the specified collection is null
- IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this deque

**See Also:**
- Collection.add(Object)

---

#### void push​(
E
e)

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

This method is equivalent to

addFirst(E)

.

**Parameters:**
- e

- the element to push

**Throws:**
- IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
- ClassCastException

- if the class of the specified element
prevents it from being added to this deque
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### E
pop()

Pops an element from the stack represented by this deque. In other
words, removes and returns the first element of this deque.

This method is equivalent to

removeFirst()

.

**Returns:**
- the element at the front of this deque (which is the top
of the stack represented by this deque)

**Throws:**
- NoSuchElementException

- if this deque is empty

---

#### boolean remove​(
Object
o)

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

This method is equivalent to

removeFirstOccurrence(Object)

.

**Specified by:**
- remove

in interface

Collection

<

E

>

**Parameters:**
- o

- element to be removed from this deque, if present

**Returns:**
- true

if an element was removed as a result of this call

**Throws:**
- ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### boolean contains​(
Object
o)

Returns

true

if this deque contains the specified element.
More formally, returns

true

if and only if this deque contains
at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:**
- contains

in interface

Collection

<

E

>

**Parameters:**
- o

- element whose presence in this deque is to be tested

**Returns:**
- true

if this deque contains the specified element

**Throws:**
- ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
- NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### int size()

Returns the number of elements in this deque.

**Specified by:**
- size

in interface

Collection

<

E

>

**Returns:**
- the number of elements in this deque

---

#### Iterator
<
E
> iterator()

Returns an iterator over the elements in this deque in proper sequence.
The elements will be returned in order from first (head) to last (tail).

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

**Returns:**
- an iterator over the elements in this deque in proper sequence

---

#### Iterator
<
E
> descendingIterator()

Returns an iterator over the elements in this deque in reverse
sequential order. The elements will be returned in order from
last (tail) to first (head).

**Returns:**
- an iterator over the elements in this deque in reverse
sequence

---

### Additional Sections

#### Interface Deque<E>

**Type Parameters:** E

- the type of elements held in this deque

**All Superinterfaces:** Collection

<E>

,

Iterable

<E>

,

Queue

<E>

**All Known Subinterfaces:** BlockingDeque

<E>

**All Known Implementing Classes:** ArrayDeque

,

ConcurrentLinkedDeque

,

LinkedBlockingDeque

,

LinkedList

```java
public interface
Deque<E>

extends
Queue
<E>
```

A linear collection that supports element insertion and removal at
both ends. The name

deque

is short for "double ended queue"
and is usually pronounced "deck". Most

Deque

implementations place no fixed limits on the number of elements
they may contain, but this interface supports capacity-restricted
deques as well as those with no fixed size limit.

This interface defines methods to access the elements at both
ends of the deque. Methods are provided to insert, remove, and
examine the element. Each of these methods exists in two forms:
one throws an exception if the operation fails, the other returns a
special value (either

null

or

false

, depending on
the operation). The latter form of the insert operation is
designed specifically for use with capacity-restricted

Deque

implementations; in most implementations, insert
operations cannot fail.

The twelve methods described above are summarized in the
following table:

Summary of Deque methods

First Element (Head)

Last Element (Tail)

Throws exception

Special value

Throws exception

Special value

Insert

addFirst(e)

offerFirst(e)

addLast(e)

offerLast(e)

Remove

removeFirst()

pollFirst()

removeLast()

pollLast()

Examine

getFirst()

peekFirst()

getLast()

peekLast()

This interface extends the

Queue

interface. When a deque is
used as a queue, FIFO (First-In-First-Out) behavior results. Elements are
added at the end of the deque and removed from the beginning. The methods
inherited from the

Queue

interface are precisely equivalent to

Deque

methods as indicated in the following table:

Comparison of Queue and Deque methods

Queue

Method

Equivalent

Deque

Method

add(e)

addLast(e)

offer(e)

offerLast(e)

remove()

removeFirst()

poll()

pollFirst()

element()

getFirst()

peek()

peekFirst()

Deques can also be used as LIFO (Last-In-First-Out) stacks. This
interface should be used in preference to the legacy

Stack

class.
When a deque is used as a stack, elements are pushed and popped from the
beginning of the deque. Stack methods are equivalent to

Deque

methods as indicated in the table below:

Comparison of Stack and Deque methods

Stack Method

Equivalent

Deque

Method

push(e)

addFirst(e)

pop()

removeFirst()

peek()

getFirst()

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

**Since:** 1.6

public interface

Deque<E>

extends

Queue

<E>

A linear collection that supports element insertion and removal at
both ends. The name

deque

is short for "double ended queue"
and is usually pronounced "deck". Most

Deque

implementations place no fixed limits on the number of elements
they may contain, but this interface supports capacity-restricted
deques as well as those with no fixed size limit.

This interface defines methods to access the elements at both
ends of the deque. Methods are provided to insert, remove, and
examine the element. Each of these methods exists in two forms:
one throws an exception if the operation fails, the other returns a
special value (either

null

or

false

, depending on
the operation). The latter form of the insert operation is
designed specifically for use with capacity-restricted

Deque

implementations; in most implementations, insert
operations cannot fail.

The twelve methods described above are summarized in the
following table:

Summary of Deque methods

First Element (Head)

Last Element (Tail)

Throws exception

Special value

Throws exception

Special value

Insert

addFirst(e)

offerFirst(e)

addLast(e)

offerLast(e)

Remove

removeFirst()

pollFirst()

removeLast()

pollLast()

Examine

getFirst()

peekFirst()

getLast()

peekLast()

This interface extends the

Queue

interface. When a deque is
used as a queue, FIFO (First-In-First-Out) behavior results. Elements are
added at the end of the deque and removed from the beginning. The methods
inherited from the

Queue

interface are precisely equivalent to

Deque

methods as indicated in the following table:

Comparison of Queue and Deque methods

Queue

Method

Equivalent

Deque

Method

add(e)

addLast(e)

offer(e)

offerLast(e)

remove()

removeFirst()

poll()

pollFirst()

element()

getFirst()

peek()

peekFirst()

Deques can also be used as LIFO (Last-In-First-Out) stacks. This
interface should be used in preference to the legacy

Stack

class.
When a deque is used as a stack, elements are pushed and popped from the
beginning of the deque. Stack methods are equivalent to

Deque

methods as indicated in the table below:

Comparison of Stack and Deque methods

Stack Method

Equivalent

Deque

Method

push(e)

addFirst(e)

pop()

removeFirst()

peek()

getFirst()

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

This interface defines methods to access the elements at both
ends of the deque. Methods are provided to insert, remove, and
examine the element. Each of these methods exists in two forms:
one throws an exception if the operation fails, the other returns a
special value (either

null

or

false

, depending on
the operation). The latter form of the insert operation is
designed specifically for use with capacity-restricted

Deque

implementations; in most implementations, insert
operations cannot fail.

The twelve methods described above are summarized in the
following table:

Summary of Deque methods

First Element (Head)

Last Element (Tail)

Throws exception

Special value

Throws exception

Special value

Insert

addFirst(e)

offerFirst(e)

addLast(e)

offerLast(e)

Remove

removeFirst()

pollFirst()

removeLast()

pollLast()

Examine

getFirst()

peekFirst()

getLast()

peekLast()

This interface extends the

Queue

interface. When a deque is
used as a queue, FIFO (First-In-First-Out) behavior results. Elements are
added at the end of the deque and removed from the beginning. The methods
inherited from the

Queue

interface are precisely equivalent to

Deque

methods as indicated in the following table:

Comparison of Queue and Deque methods

Queue

Method

Equivalent

Deque

Method

add(e)

addLast(e)

offer(e)

offerLast(e)

remove()

removeFirst()

poll()

pollFirst()

element()

getFirst()

peek()

peekFirst()

Deques can also be used as LIFO (Last-In-First-Out) stacks. This
interface should be used in preference to the legacy

Stack

class.
When a deque is used as a stack, elements are pushed and popped from the
beginning of the deque. Stack methods are equivalent to

Deque

methods as indicated in the table below:

Comparison of Stack and Deque methods

Stack Method

Equivalent

Deque

Method

push(e)

addFirst(e)

pop()

removeFirst()

peek()

getFirst()

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

The twelve methods described above are summarized in the
following table:

Summary of Deque methods

First Element (Head)

Last Element (Tail)

Throws exception

Special value

Throws exception

Special value

Insert

addFirst(e)

offerFirst(e)

addLast(e)

offerLast(e)

Remove

removeFirst()

pollFirst()

removeLast()

pollLast()

Examine

getFirst()

peekFirst()

getLast()

peekLast()

This interface extends the

Queue

interface. When a deque is
used as a queue, FIFO (First-In-First-Out) behavior results. Elements are
added at the end of the deque and removed from the beginning. The methods
inherited from the

Queue

interface are precisely equivalent to

Deque

methods as indicated in the following table:

Comparison of Queue and Deque methods

Queue

Method

Equivalent

Deque

Method

add(e)

addLast(e)

offer(e)

offerLast(e)

remove()

removeFirst()

poll()

pollFirst()

element()

getFirst()

peek()

peekFirst()

Deques can also be used as LIFO (Last-In-First-Out) stacks. This
interface should be used in preference to the legacy

Stack

class.
When a deque is used as a stack, elements are pushed and popped from the
beginning of the deque. Stack methods are equivalent to

Deque

methods as indicated in the table below:

Comparison of Stack and Deque methods

Stack Method

Equivalent

Deque

Method

push(e)

addFirst(e)

pop()

removeFirst()

peek()

getFirst()

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

This interface extends the

Queue

interface. When a deque is
used as a queue, FIFO (First-In-First-Out) behavior results. Elements are
added at the end of the deque and removed from the beginning. The methods
inherited from the

Queue

interface are precisely equivalent to

Deque

methods as indicated in the following table:

Comparison of Queue and Deque methods

Queue

Method

Equivalent

Deque

Method

add(e)

addLast(e)

offer(e)

offerLast(e)

remove()

removeFirst()

poll()

pollFirst()

element()

getFirst()

peek()

peekFirst()

Deques can also be used as LIFO (Last-In-First-Out) stacks. This
interface should be used in preference to the legacy

Stack

class.
When a deque is used as a stack, elements are pushed and popped from the
beginning of the deque. Stack methods are equivalent to

Deque

methods as indicated in the table below:

Comparison of Stack and Deque methods

Stack Method

Equivalent

Deque

Method

push(e)

addFirst(e)

pop()

removeFirst()

peek()

getFirst()

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

Deques can also be used as LIFO (Last-In-First-Out) stacks. This
interface should be used in preference to the legacy

Stack

class.
When a deque is used as a stack, elements are pushed and popped from the
beginning of the deque. Stack methods are equivalent to

Deque

methods as indicated in the table below:

Comparison of Stack and Deque methods

Stack Method

Equivalent

Deque

Method

push(e)

addFirst(e)

pop()

removeFirst()

peek()

getFirst()

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

Note that the

peek

method works equally well when
a deque is used as a queue or a stack; in either case, elements are
drawn from the beginning of the deque.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

This interface provides two methods to remove interior
elements,

removeFirstOccurrence

and

removeLastOccurrence

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

Unlike the

List

interface, this interface does not
provide support for indexed access to elements.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

While

Deque

implementations are not strictly required
to prohibit the insertion of null elements, they are strongly
encouraged to do so. Users of any

Deque

implementations
that do allow null elements are strongly encouraged

not

to
take advantage of the ability to insert nulls. This is so because

null

is used as a special return value by various methods
to indicate that the deque is empty.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

Deque

implementations generally do not define
element-based versions of the

equals

and

hashCode

methods, but instead inherit the identity-based versions from class

Object

.

This interface is a member of the

Java Collections Framework

.

This interface is a member of the

Java Collections Framework

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

add

​(

E

e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

boolean

addAll

​(

Collection

<? extends

E

> c)

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

void

addFirst

​(

E

e)

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available.

void

addLast

​(

E

e)

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available.

boolean

contains

​(

Object

o)

Returns

true

if this deque contains the specified element.

Iterator

<

E

>

descendingIterator

()

Returns an iterator over the elements in this deque in reverse
sequential order.

E

element

()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).

E

getFirst

()

Retrieves, but does not remove, the first element of this deque.

E

getLast

()

Retrieves, but does not remove, the last element of this deque.

Iterator

<

E

>

iterator

()

Returns an iterator over the elements in this deque in proper sequence.

boolean

offer

​(

E

e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available.

boolean

offerFirst

​(

E

e)

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions.

boolean

offerLast

​(

E

e)

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions.

E

peek

()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

E

peekFirst

()

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

E

peekLast

()

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

E

poll

()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

E

pollFirst

()

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

E

pollLast

()

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

E

pop

()

Pops an element from the stack represented by this deque.

void

push

​(

E

e)

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

E

remove

()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).

boolean

remove

​(

Object

o)

Removes the first occurrence of the specified element from this deque.

E

removeFirst

()

Retrieves and removes the first element of this deque.

boolean

removeFirstOccurrence

​(

Object

o)

Removes the first occurrence of the specified element from this deque.

E

removeLast

()

Retrieves and removes the last element of this deque.

boolean

removeLastOccurrence

​(

Object

o)

Removes the last occurrence of the specified element from this deque.

int

size

()

Returns the number of elements in this deque.

- Methods declared in interface java.util.

Collection

clear

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

parallelStream

,

removeAll

,

removeIf

,

retainAll

,

spliterator

,

stream

,

toArray

,

toArray

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

add

​(

E

e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

boolean

addAll

​(

Collection

<? extends

E

> c)

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

void

addFirst

​(

E

e)

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available.

void

addLast

​(

E

e)

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available.

boolean

contains

​(

Object

o)

Returns

true

if this deque contains the specified element.

Iterator

<

E

>

descendingIterator

()

Returns an iterator over the elements in this deque in reverse
sequential order.

E

element

()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).

E

getFirst

()

Retrieves, but does not remove, the first element of this deque.

E

getLast

()

Retrieves, but does not remove, the last element of this deque.

Iterator

<

E

>

iterator

()

Returns an iterator over the elements in this deque in proper sequence.

boolean

offer

​(

E

e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available.

boolean

offerFirst

​(

E

e)

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions.

boolean

offerLast

​(

E

e)

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions.

E

peek

()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

E

peekFirst

()

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

E

peekLast

()

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

E

poll

()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

E

pollFirst

()

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

E

pollLast

()

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

E

pop

()

Pops an element from the stack represented by this deque.

void

push

​(

E

e)

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

E

remove

()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).

boolean

remove

​(

Object

o)

Removes the first occurrence of the specified element from this deque.

E

removeFirst

()

Retrieves and removes the first element of this deque.

boolean

removeFirstOccurrence

​(

Object

o)

Removes the first occurrence of the specified element from this deque.

E

removeLast

()

Retrieves and removes the last element of this deque.

boolean

removeLastOccurrence

​(

Object

o)

Removes the last occurrence of the specified element from this deque.

int

size

()

Returns the number of elements in this deque.

- Methods declared in interface java.util.

Collection

clear

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

parallelStream

,

removeAll

,

removeIf

,

retainAll

,

spliterator

,

stream

,

toArray

,

toArray

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

---

#### Method Summary

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available.

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available.

Returns

true

if this deque contains the specified element.

Returns an iterator over the elements in this deque in reverse
sequential order.

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).

Retrieves, but does not remove, the first element of this deque.

Retrieves, but does not remove, the last element of this deque.

Returns an iterator over the elements in this deque in proper sequence.

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available.

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions.

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions.

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

Pops an element from the stack represented by this deque.

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).

Removes the first occurrence of the specified element from this deque.

Retrieves and removes the first element of this deque.

Retrieves and removes the last element of this deque.

Removes the last occurrence of the specified element from this deque.

Returns the number of elements in this deque.

Methods declared in interface java.util.

Collection

clear

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

parallelStream

,

removeAll

,

removeIf

,

retainAll

,

spliterator

,

stream

,

toArray

,

toArray

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.lang.

Iterable

forEach

---

#### Methods declared in interface java.lang. Iterable

============ METHOD DETAIL ==========

- Method Detail

- addFirst

```java
void addFirst​(
E
e)
```

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerFirst(E)

.

**Parameters:** e

- the element to add
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- addLast

```java
void addLast​(
E
e)
```

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerLast(E)

.

This method is equivalent to

add(E)

.

**Parameters:** e

- the element to add
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- offerFirst

```java
boolean offerFirst​(
E
e)
```

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addFirst(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- offerLast

```java
boolean offerLast​(
E
e)
```

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addLast(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- removeFirst

```java
E
removeFirst()
```

Retrieves and removes the first element of this deque. This method
differs from

pollFirst

only in that it throws an
exception if this deque is empty.

**Returns:** the head of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- removeLast

```java
E
removeLast()
```

Retrieves and removes the last element of this deque. This method
differs from

pollLast

only in that it throws an
exception if this deque is empty.

**Returns:** the tail of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- pollFirst

```java
E
pollFirst()
```

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

**Returns:** the head of this deque, or

null

if this deque is empty

- pollLast

```java
E
pollLast()
```

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

**Returns:** the tail of this deque, or

null

if this deque is empty

- getFirst

```java
E
getFirst()
```

Retrieves, but does not remove, the first element of this deque.

This method differs from

peekFirst

only in that it
throws an exception if this deque is empty.

**Returns:** the head of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- getLast

```java
E
getLast()
```

Retrieves, but does not remove, the last element of this deque.
This method differs from

peekLast

only in that it
throws an exception if this deque is empty.

**Returns:** the tail of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- peekFirst

```java
E
peekFirst()
```

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

**Returns:** the head of this deque, or

null

if this deque is empty

- peekLast

```java
E
peekLast()
```

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

**Returns:** the tail of this deque, or

null

if this deque is empty

- removeFirstOccurrence

```java
boolean removeFirstOccurrence​(
Object
o)
```

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- removeLastOccurrence

```java
boolean removeLastOccurrence​(
Object
o)
```

Removes the last occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the last element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- add

```java
boolean add​(
E
e)
```

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.
When using a capacity-restricted deque, it is generally preferable to
use

offer

.

This method is equivalent to

addLast(E)

.

**Specified by:** add

in interface

Collection

<

E

>
**Specified by:** add

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- offer

```java
boolean offer​(
E
e)
```

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available. When using a capacity-restricted deque, this method is
generally preferable to the

add(E)

method, which can fail to
insert an element only by throwing an exception.

This method is equivalent to

offerLast(E)

.

**Specified by:** offer

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- remove

```java
E
remove()
```

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).
This method differs from

poll()

only in that it
throws an exception if this deque is empty.

This method is equivalent to

removeFirst()

.

**Specified by:** remove

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque
**Throws:** NoSuchElementException

- if this deque is empty

- poll

```java
E
poll()
```

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

This method is equivalent to

pollFirst()

.

**Specified by:** poll

in interface

Queue

<

E

>
**Returns:** the first element of this deque, or

null

if
this deque is empty

- element

```java
E
element()
```

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).
This method differs from

peek

only in that it throws an
exception if this deque is empty.

This method is equivalent to

getFirst()

.

**Specified by:** element

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque
**Throws:** NoSuchElementException

- if this deque is empty

- peek

```java
E
peek()
```

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

This method is equivalent to

peekFirst()

.

**Specified by:** peek

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque, or

null

if this deque is empty

- addAll

```java
boolean addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

When using a capacity-restricted deque, it is generally preferable
to call

offer

separately on each element.

An exception encountered while trying to add an element may result
in only some of the elements having been successfully added when
the associated exception is thrown.

**Specified by:** addAll

in interface

Collection

<

E

>
**Parameters:** c

- the elements to be inserted into this deque
**Returns:** true

if this deque changed as a result of the call
**Throws:** IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified collection contains a
null element and this deque does not permit null elements,
or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this deque
**See Also:** Collection.add(Object)

- push

```java
void push​(
E
e)
```

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

This method is equivalent to

addFirst(E)

.

**Parameters:** e

- the element to push
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- pop

```java
E
pop()
```

Pops an element from the stack represented by this deque. In other
words, removes and returns the first element of this deque.

This method is equivalent to

removeFirst()

.

**Returns:** the element at the front of this deque (which is the top
of the stack represented by this deque)
**Throws:** NoSuchElementException

- if this deque is empty

- remove

```java
boolean remove​(
Object
o)
```

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

This method is equivalent to

removeFirstOccurrence(Object)

.

**Specified by:** remove

in interface

Collection

<

E

>
**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- contains

```java
boolean contains​(
Object
o)
```

Returns

true

if this deque contains the specified element.
More formally, returns

true

if and only if this deque contains
at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:** contains

in interface

Collection

<

E

>
**Parameters:** o

- element whose presence in this deque is to be tested
**Returns:** true

if this deque contains the specified element
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- size

```java
int size()
```

Returns the number of elements in this deque.

**Specified by:** size

in interface

Collection

<

E

>
**Returns:** the number of elements in this deque

- iterator

```java
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this deque in proper sequence.
The elements will be returned in order from first (head) to last (tail).

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
**Returns:** an iterator over the elements in this deque in proper sequence

- descendingIterator

```java
Iterator
<
E
> descendingIterator()
```

Returns an iterator over the elements in this deque in reverse
sequential order. The elements will be returned in order from
last (tail) to first (head).

**Returns:** an iterator over the elements in this deque in reverse
sequence

Method Detail

- addFirst

```java
void addFirst​(
E
e)
```

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerFirst(E)

.

**Parameters:** e

- the element to add
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- addLast

```java
void addLast​(
E
e)
```

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerLast(E)

.

This method is equivalent to

add(E)

.

**Parameters:** e

- the element to add
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- offerFirst

```java
boolean offerFirst​(
E
e)
```

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addFirst(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- offerLast

```java
boolean offerLast​(
E
e)
```

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addLast(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- removeFirst

```java
E
removeFirst()
```

Retrieves and removes the first element of this deque. This method
differs from

pollFirst

only in that it throws an
exception if this deque is empty.

**Returns:** the head of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- removeLast

```java
E
removeLast()
```

Retrieves and removes the last element of this deque. This method
differs from

pollLast

only in that it throws an
exception if this deque is empty.

**Returns:** the tail of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- pollFirst

```java
E
pollFirst()
```

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

**Returns:** the head of this deque, or

null

if this deque is empty

- pollLast

```java
E
pollLast()
```

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

**Returns:** the tail of this deque, or

null

if this deque is empty

- getFirst

```java
E
getFirst()
```

Retrieves, but does not remove, the first element of this deque.

This method differs from

peekFirst

only in that it
throws an exception if this deque is empty.

**Returns:** the head of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- getLast

```java
E
getLast()
```

Retrieves, but does not remove, the last element of this deque.
This method differs from

peekLast

only in that it
throws an exception if this deque is empty.

**Returns:** the tail of this deque
**Throws:** NoSuchElementException

- if this deque is empty

- peekFirst

```java
E
peekFirst()
```

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

**Returns:** the head of this deque, or

null

if this deque is empty

- peekLast

```java
E
peekLast()
```

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

**Returns:** the tail of this deque, or

null

if this deque is empty

- removeFirstOccurrence

```java
boolean removeFirstOccurrence​(
Object
o)
```

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- removeLastOccurrence

```java
boolean removeLastOccurrence​(
Object
o)
```

Removes the last occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the last element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- add

```java
boolean add​(
E
e)
```

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.
When using a capacity-restricted deque, it is generally preferable to
use

offer

.

This method is equivalent to

addLast(E)

.

**Specified by:** add

in interface

Collection

<

E

>
**Specified by:** add

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- offer

```java
boolean offer​(
E
e)
```

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available. When using a capacity-restricted deque, this method is
generally preferable to the

add(E)

method, which can fail to
insert an element only by throwing an exception.

This method is equivalent to

offerLast(E)

.

**Specified by:** offer

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- remove

```java
E
remove()
```

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).
This method differs from

poll()

only in that it
throws an exception if this deque is empty.

This method is equivalent to

removeFirst()

.

**Specified by:** remove

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque
**Throws:** NoSuchElementException

- if this deque is empty

- poll

```java
E
poll()
```

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

This method is equivalent to

pollFirst()

.

**Specified by:** poll

in interface

Queue

<

E

>
**Returns:** the first element of this deque, or

null

if
this deque is empty

- element

```java
E
element()
```

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).
This method differs from

peek

only in that it throws an
exception if this deque is empty.

This method is equivalent to

getFirst()

.

**Specified by:** element

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque
**Throws:** NoSuchElementException

- if this deque is empty

- peek

```java
E
peek()
```

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

This method is equivalent to

peekFirst()

.

**Specified by:** peek

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque, or

null

if this deque is empty

- addAll

```java
boolean addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

When using a capacity-restricted deque, it is generally preferable
to call

offer

separately on each element.

An exception encountered while trying to add an element may result
in only some of the elements having been successfully added when
the associated exception is thrown.

**Specified by:** addAll

in interface

Collection

<

E

>
**Parameters:** c

- the elements to be inserted into this deque
**Returns:** true

if this deque changed as a result of the call
**Throws:** IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified collection contains a
null element and this deque does not permit null elements,
or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this deque
**See Also:** Collection.add(Object)

- push

```java
void push​(
E
e)
```

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

This method is equivalent to

addFirst(E)

.

**Parameters:** e

- the element to push
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

- pop

```java
E
pop()
```

Pops an element from the stack represented by this deque. In other
words, removes and returns the first element of this deque.

This method is equivalent to

removeFirst()

.

**Returns:** the element at the front of this deque (which is the top
of the stack represented by this deque)
**Throws:** NoSuchElementException

- if this deque is empty

- remove

```java
boolean remove​(
Object
o)
```

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

This method is equivalent to

removeFirstOccurrence(Object)

.

**Specified by:** remove

in interface

Collection

<

E

>
**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- contains

```java
boolean contains​(
Object
o)
```

Returns

true

if this deque contains the specified element.
More formally, returns

true

if and only if this deque contains
at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:** contains

in interface

Collection

<

E

>
**Parameters:** o

- element whose presence in this deque is to be tested
**Returns:** true

if this deque contains the specified element
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

- size

```java
int size()
```

Returns the number of elements in this deque.

**Specified by:** size

in interface

Collection

<

E

>
**Returns:** the number of elements in this deque

- iterator

```java
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this deque in proper sequence.
The elements will be returned in order from first (head) to last (tail).

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
**Returns:** an iterator over the elements in this deque in proper sequence

- descendingIterator

```java
Iterator
<
E
> descendingIterator()
```

Returns an iterator over the elements in this deque in reverse
sequential order. The elements will be returned in order from
last (tail) to first (head).

**Returns:** an iterator over the elements in this deque in reverse
sequence

---

#### Method Detail

addFirst

```java
void addFirst​(
E
e)
```

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerFirst(E)

.

**Parameters:** e

- the element to add
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### addFirst

void addFirst​(

E

e)

Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerFirst(E)

.

addLast

```java
void addLast​(
E
e)
```

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerLast(E)

.

This method is equivalent to

add(E)

.

**Parameters:** e

- the element to add
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### addLast

void addLast​(

E

e)

Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an

IllegalStateException

if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use method

offerLast(E)

.

This method is equivalent to

add(E)

.

This method is equivalent to

add(E)

.

offerFirst

```java
boolean offerFirst​(
E
e)
```

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addFirst(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### offerFirst

boolean offerFirst​(

E

e)

Inserts the specified element at the front of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addFirst(E)

method,
which can fail to insert an element only by throwing an exception.

offerLast

```java
boolean offerLast​(
E
e)
```

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addLast(E)

method,
which can fail to insert an element only by throwing an exception.

**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### offerLast

boolean offerLast​(

E

e)

Inserts the specified element at the end of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the

addLast(E)

method,
which can fail to insert an element only by throwing an exception.

removeFirst

```java
E
removeFirst()
```

Retrieves and removes the first element of this deque. This method
differs from

pollFirst

only in that it throws an
exception if this deque is empty.

**Returns:** the head of this deque
**Throws:** NoSuchElementException

- if this deque is empty

---

#### removeFirst

E

removeFirst()

Retrieves and removes the first element of this deque. This method
differs from

pollFirst

only in that it throws an
exception if this deque is empty.

removeLast

```java
E
removeLast()
```

Retrieves and removes the last element of this deque. This method
differs from

pollLast

only in that it throws an
exception if this deque is empty.

**Returns:** the tail of this deque
**Throws:** NoSuchElementException

- if this deque is empty

---

#### removeLast

E

removeLast()

Retrieves and removes the last element of this deque. This method
differs from

pollLast

only in that it throws an
exception if this deque is empty.

pollFirst

```java
E
pollFirst()
```

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

**Returns:** the head of this deque, or

null

if this deque is empty

---

#### pollFirst

E

pollFirst()

Retrieves and removes the first element of this deque,
or returns

null

if this deque is empty.

pollLast

```java
E
pollLast()
```

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

**Returns:** the tail of this deque, or

null

if this deque is empty

---

#### pollLast

E

pollLast()

Retrieves and removes the last element of this deque,
or returns

null

if this deque is empty.

getFirst

```java
E
getFirst()
```

Retrieves, but does not remove, the first element of this deque.

This method differs from

peekFirst

only in that it
throws an exception if this deque is empty.

**Returns:** the head of this deque
**Throws:** NoSuchElementException

- if this deque is empty

---

#### getFirst

E

getFirst()

Retrieves, but does not remove, the first element of this deque.

This method differs from

peekFirst

only in that it
throws an exception if this deque is empty.

getLast

```java
E
getLast()
```

Retrieves, but does not remove, the last element of this deque.
This method differs from

peekLast

only in that it
throws an exception if this deque is empty.

**Returns:** the tail of this deque
**Throws:** NoSuchElementException

- if this deque is empty

---

#### getLast

E

getLast()

Retrieves, but does not remove, the last element of this deque.
This method differs from

peekLast

only in that it
throws an exception if this deque is empty.

peekFirst

```java
E
peekFirst()
```

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

**Returns:** the head of this deque, or

null

if this deque is empty

---

#### peekFirst

E

peekFirst()

Retrieves, but does not remove, the first element of this deque,
or returns

null

if this deque is empty.

peekLast

```java
E
peekLast()
```

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

**Returns:** the tail of this deque, or

null

if this deque is empty

---

#### peekLast

E

peekLast()

Retrieves, but does not remove, the last element of this deque,
or returns

null

if this deque is empty.

removeFirstOccurrence

```java
boolean removeFirstOccurrence​(
Object
o)
```

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### removeFirstOccurrence

boolean removeFirstOccurrence​(

Object

o)

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

removeLastOccurrence

```java
boolean removeLastOccurrence​(
Object
o)
```

Removes the last occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the last element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### removeLastOccurrence

boolean removeLastOccurrence​(

Object

o)

Removes the last occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the last element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

add

```java
boolean add​(
E
e)
```

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.
When using a capacity-restricted deque, it is generally preferable to
use

offer

.

This method is equivalent to

addLast(E)

.

**Specified by:** add

in interface

Collection

<

E

>
**Specified by:** add

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

(as specified by

Collection.add(E)

)
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### add

boolean add​(

E

e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.
When using a capacity-restricted deque, it is generally preferable to
use

offer

.

This method is equivalent to

addLast(E)

.

This method is equivalent to

addLast(E)

.

offer

```java
boolean offer​(
E
e)
```

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available. When using a capacity-restricted deque, this method is
generally preferable to the

add(E)

method, which can fail to
insert an element only by throwing an exception.

This method is equivalent to

offerLast(E)

.

**Specified by:** offer

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this deque, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### offer

boolean offer​(

E

e)

Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and

false

if no space is currently
available. When using a capacity-restricted deque, this method is
generally preferable to the

add(E)

method, which can fail to
insert an element only by throwing an exception.

This method is equivalent to

offerLast(E)

.

This method is equivalent to

offerLast(E)

.

remove

```java
E
remove()
```

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).
This method differs from

poll()

only in that it
throws an exception if this deque is empty.

This method is equivalent to

removeFirst()

.

**Specified by:** remove

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque
**Throws:** NoSuchElementException

- if this deque is empty

---

#### remove

E

remove()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque).
This method differs from

poll()

only in that it
throws an exception if this deque is empty.

This method is equivalent to

removeFirst()

.

This method is equivalent to

removeFirst()

.

poll

```java
E
poll()
```

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

This method is equivalent to

pollFirst()

.

**Specified by:** poll

in interface

Queue

<

E

>
**Returns:** the first element of this deque, or

null

if
this deque is empty

---

#### poll

E

poll()

Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), or returns

null

if this deque is empty.

This method is equivalent to

pollFirst()

.

This method is equivalent to

pollFirst()

.

element

```java
E
element()
```

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).
This method differs from

peek

only in that it throws an
exception if this deque is empty.

This method is equivalent to

getFirst()

.

**Specified by:** element

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque
**Throws:** NoSuchElementException

- if this deque is empty

---

#### element

E

element()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).
This method differs from

peek

only in that it throws an
exception if this deque is empty.

This method is equivalent to

getFirst()

.

This method is equivalent to

getFirst()

.

peek

```java
E
peek()
```

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

This method is equivalent to

peekFirst()

.

**Specified by:** peek

in interface

Queue

<

E

>
**Returns:** the head of the queue represented by this deque, or

null

if this deque is empty

---

#### peek

E

peek()

Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque), or
returns

null

if this deque is empty.

This method is equivalent to

peekFirst()

.

This method is equivalent to

peekFirst()

.

addAll

```java
boolean addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

When using a capacity-restricted deque, it is generally preferable
to call

offer

separately on each element.

An exception encountered while trying to add an element may result
in only some of the elements having been successfully added when
the associated exception is thrown.

**Specified by:** addAll

in interface

Collection

<

E

>
**Parameters:** c

- the elements to be inserted into this deque
**Returns:** true

if this deque changed as a result of the call
**Throws:** IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified collection contains a
null element and this deque does not permit null elements,
or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this deque
**See Also:** Collection.add(Object)

---

#### addAll

boolean addAll​(

Collection

<? extends

E

> c)

Adds all of the elements in the specified collection at the end
of this deque, as if by calling

addLast(E)

on each one,
in the order that they are returned by the collection's iterator.

When using a capacity-restricted deque, it is generally preferable
to call

offer

separately on each element.

An exception encountered while trying to add an element may result
in only some of the elements having been successfully added when
the associated exception is thrown.

When using a capacity-restricted deque, it is generally preferable
to call

offer

separately on each element.

An exception encountered while trying to add an element may result
in only some of the elements having been successfully added when
the associated exception is thrown.

An exception encountered while trying to add an element may result
in only some of the elements having been successfully added when
the associated exception is thrown.

push

```java
void push​(
E
e)
```

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

This method is equivalent to

addFirst(E)

.

**Parameters:** e

- the element to push
**Throws:** IllegalStateException

- if the element cannot be added at this
time due to capacity restrictions
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this deque
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this deque

---

#### push

void push​(

E

e)

Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an

IllegalStateException

if no space is currently available.

This method is equivalent to

addFirst(E)

.

This method is equivalent to

addFirst(E)

.

pop

```java
E
pop()
```

Pops an element from the stack represented by this deque. In other
words, removes and returns the first element of this deque.

This method is equivalent to

removeFirst()

.

**Returns:** the element at the front of this deque (which is the top
of the stack represented by this deque)
**Throws:** NoSuchElementException

- if this deque is empty

---

#### pop

E

pop()

Pops an element from the stack represented by this deque. In other
words, removes and returns the first element of this deque.

This method is equivalent to

removeFirst()

.

This method is equivalent to

removeFirst()

.

remove

```java
boolean remove​(
Object
o)
```

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

This method is equivalent to

removeFirstOccurrence(Object)

.

**Specified by:** remove

in interface

Collection

<

E

>
**Parameters:** o

- element to be removed from this deque, if present
**Returns:** true

if an element was removed as a result of this call
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### remove

boolean remove​(

Object

o)

Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element

e

such that

Objects.equals(o, e)

(if such an element exists).
Returns

true

if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).

This method is equivalent to

removeFirstOccurrence(Object)

.

This method is equivalent to

removeFirstOccurrence(Object)

.

contains

```java
boolean contains​(
Object
o)
```

Returns

true

if this deque contains the specified element.
More formally, returns

true

if and only if this deque contains
at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:** contains

in interface

Collection

<

E

>
**Parameters:** o

- element whose presence in this deque is to be tested
**Returns:** true

if this deque contains the specified element
**Throws:** ClassCastException

- if the class of the specified element
is incompatible with this deque
(

optional

)
**Throws:** NullPointerException

- if the specified element is null and this
deque does not permit null elements
(

optional

)

---

#### contains

boolean contains​(

Object

o)

Returns

true

if this deque contains the specified element.
More formally, returns

true

if and only if this deque contains
at least one element

e

such that

Objects.equals(o, e)

.

size

```java
int size()
```

Returns the number of elements in this deque.

**Specified by:** size

in interface

Collection

<

E

>
**Returns:** the number of elements in this deque

---

#### size

int size()

Returns the number of elements in this deque.

iterator

```java
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this deque in proper sequence.
The elements will be returned in order from first (head) to last (tail).

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
**Returns:** an iterator over the elements in this deque in proper sequence

---

#### iterator

Iterator

<

E

> iterator()

Returns an iterator over the elements in this deque in proper sequence.
The elements will be returned in order from first (head) to last (tail).

descendingIterator

```java
Iterator
<
E
> descendingIterator()
```

Returns an iterator over the elements in this deque in reverse
sequential order. The elements will be returned in order from
last (tail) to first (head).

**Returns:** an iterator over the elements in this deque in reverse
sequence

---

#### descendingIterator

Iterator

<

E

> descendingIterator()

Returns an iterator over the elements in this deque in reverse
sequential order. The elements will be returned in order from
last (tail) to first (head).

---

