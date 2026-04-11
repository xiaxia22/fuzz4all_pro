# Class AbstractQueue<E>

**Source:** `java.base\java\util\AbstractQueue.html`

### Class Description

```java
public abstract class
AbstractQueue<E>

extends
AbstractCollection
<E>
implements
Queue
<E>
```

This class provides skeletal implementations of some

Queue

operations. The implementations in this class are appropriate when
the base implementation does

not

allow

null

elements. Methods

add

,

remove

, and

element

are based on

offer

,

poll

, and

peek

, respectively, but throw
exceptions instead of indicating failure via

false

or

null

returns.

A

Queue

implementation that extends this class must
minimally define a method

Queue.offer(E)

which does not permit
insertion of

null

elements, along with methods

Queue.peek()

,

Queue.poll()

,

Collection.size()

, and

Collection.iterator()

. Typically, additional methods will be
overridden as well. If these requirements cannot be met, consider
instead subclassing

AbstractCollection

.

This class is a member of the

Java Collections Framework

.

**Type Parameters:** E

- the type of elements held in this queue

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractQueue()

Constructor for use by subclasses.

---

### Method Details

#### public boolean add​(
E
e)

Inserts the specified element into this queue if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

This implementation returns

true

if

offer

succeeds,
else throws an

IllegalStateException

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

**Overrides:**
- add

in class

AbstractCollection

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
prevents it from being added to this queue
- NullPointerException

- if the specified element is null and
this queue does not permit null elements
- IllegalArgumentException

- if some property of this element
prevents it from being added to this queue

---

#### public
E
remove()

Retrieves and removes the head of this queue. This method differs
from

poll

only in that it throws an exception if this
queue is empty.

This implementation returns the result of

poll

unless the queue is empty.

**Specified by:**
- remove

in interface

Queue

<

E

>

**Returns:**
- the head of this queue

**Throws:**
- NoSuchElementException

- if this queue is empty

---

#### public
E
element()

Retrieves, but does not remove, the head of this queue. This method
differs from

peek

only in that it throws an exception if
this queue is empty.

This implementation returns the result of

peek

unless the queue is empty.

**Specified by:**
- element

in interface

Queue

<

E

>

**Returns:**
- the head of this queue

**Throws:**
- NoSuchElementException

- if this queue is empty

---

#### public void clear()

Removes all of the elements from this queue.
The queue will be empty after this call returns.

This implementation repeatedly invokes

poll

until it
returns

null

.

**Specified by:**
- clear

in interface

Collection

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

---

#### public boolean addAll​(
Collection
<? extends
E
> c)

Adds all of the elements in the specified collection to this
queue. Attempts to addAll of a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

This implementation iterates over the specified collection,
and adds each element returned by the iterator to this
queue, in turn. A runtime exception encountered while
trying to add an element (including, in particular, a

null

element) may result in only some of the elements
having been successfully added when the associated exception is
thrown.

**Specified by:**
- addAll

in interface

Collection

<

E

>

**Overrides:**
- addAll

in class

AbstractCollection

<

E

>

**Parameters:**
- c

- collection containing elements to be added to this queue

**Returns:**
- true

if this queue changed as a result of the call

**Throws:**
- ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this queue
- NullPointerException

- if the specified collection contains a
null element and this queue does not permit null elements,
or if the specified collection is null
- IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this
queue, or if the specified collection is this queue
- IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions

**See Also:**
- add(Object)

---

### Additional Sections

#### Class AbstractQueue<E>

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractQueue<E>

java.util.AbstractCollection

<E>

- java.util.AbstractQueue<E>

java.util.AbstractQueue<E>

**Type Parameters:** E

- the type of elements held in this queue

**All Implemented Interfaces:** Iterable

<E>

,

Collection

<E>

,

Queue

<E>

**Direct Known Subclasses:** ArrayBlockingQueue

,

ConcurrentLinkedQueue

,

DelayQueue

,

LinkedBlockingDeque

,

LinkedBlockingQueue

,

LinkedTransferQueue

,

PriorityBlockingQueue

,

PriorityQueue

,

SynchronousQueue

```java
public abstract class
AbstractQueue<E>

extends
AbstractCollection
<E>
implements
Queue
<E>
```

This class provides skeletal implementations of some

Queue

operations. The implementations in this class are appropriate when
the base implementation does

not

allow

null

elements. Methods

add

,

remove

, and

element

are based on

offer

,

poll

, and

peek

, respectively, but throw
exceptions instead of indicating failure via

false

or

null

returns.

A

Queue

implementation that extends this class must
minimally define a method

Queue.offer(E)

which does not permit
insertion of

null

elements, along with methods

Queue.peek()

,

Queue.poll()

,

Collection.size()

, and

Collection.iterator()

. Typically, additional methods will be
overridden as well. If these requirements cannot be met, consider
instead subclassing

AbstractCollection

.

This class is a member of the

Java Collections Framework

.

**Since:** 1.5

public abstract class

AbstractQueue<E>

extends

AbstractCollection

<E>
implements

Queue

<E>

This class provides skeletal implementations of some

Queue

operations. The implementations in this class are appropriate when
the base implementation does

not

allow

null

elements. Methods

add

,

remove

, and

element

are based on

offer

,

poll

, and

peek

, respectively, but throw
exceptions instead of indicating failure via

false

or

null

returns.

A

Queue

implementation that extends this class must
minimally define a method

Queue.offer(E)

which does not permit
insertion of

null

elements, along with methods

Queue.peek()

,

Queue.poll()

,

Collection.size()

, and

Collection.iterator()

. Typically, additional methods will be
overridden as well. If these requirements cannot be met, consider
instead subclassing

AbstractCollection

.

This class is a member of the

Java Collections Framework

.

A

Queue

implementation that extends this class must
minimally define a method

Queue.offer(E)

which does not permit
insertion of

null

elements, along with methods

Queue.peek()

,

Queue.poll()

,

Collection.size()

, and

Collection.iterator()

. Typically, additional methods will be
overridden as well. If these requirements cannot be met, consider
instead subclassing

AbstractCollection

.

This class is a member of the

Java Collections Framework

.

This class is a member of the

Java Collections Framework

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractQueue

()

Constructor for use by subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

E

e)

Inserts the specified element into this queue if it is possible to do so
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

Adds all of the elements in the specified collection to this
queue.

void

clear

()

Removes all of the elements from this queue.

E

element

()

Retrieves, but does not remove, the head of this queue.

E

remove

()

Retrieves and removes the head of this queue.

- Methods declared in class java.util.

AbstractCollection

contains

,

containsAll

,

isEmpty

,

iterator

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

- Methods declared in interface java.util.

Collection

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

parallelStream

,

remove

,

removeAll

,

removeIf

,

retainAll

,

size

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

- Methods declared in interface java.util.

Queue

offer

,

peek

,

poll

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractQueue

()

Constructor for use by subclasses.

---

#### Constructor Summary

Constructor for use by subclasses.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

E

e)

Inserts the specified element into this queue if it is possible to do so
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

Adds all of the elements in the specified collection to this
queue.

void

clear

()

Removes all of the elements from this queue.

E

element

()

Retrieves, but does not remove, the head of this queue.

E

remove

()

Retrieves and removes the head of this queue.

- Methods declared in class java.util.

AbstractCollection

contains

,

containsAll

,

isEmpty

,

iterator

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

- Methods declared in interface java.util.

Collection

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

parallelStream

,

remove

,

removeAll

,

removeIf

,

retainAll

,

size

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

- Methods declared in interface java.util.

Queue

offer

,

peek

,

poll

---

#### Method Summary

Inserts the specified element into this queue if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

Adds all of the elements in the specified collection to this
queue.

Removes all of the elements from this queue.

Retrieves, but does not remove, the head of this queue.

Retrieves and removes the head of this queue.

Methods declared in class java.util.

AbstractCollection

contains

,

containsAll

,

isEmpty

,

iterator

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

Methods declared in interface java.util.

Collection

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

parallelStream

,

remove

,

removeAll

,

removeIf

,

retainAll

,

size

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

Methods declared in interface java.util.

Queue

offer

,

peek

,

poll

---

#### Methods declared in interface java.util. Queue

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractQueue

```java
protected AbstractQueue()
```

Constructor for use by subclasses.

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public boolean add​(
E
e)
```

Inserts the specified element into this queue if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

This implementation returns

true

if

offer

succeeds,
else throws an

IllegalStateException

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
**Overrides:** add

in class

AbstractCollection

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
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null and
this queue does not permit null elements
**Throws:** IllegalArgumentException

- if some property of this element
prevents it from being added to this queue

- remove

```java
public
E
remove()
```

Retrieves and removes the head of this queue. This method differs
from

poll

only in that it throws an exception if this
queue is empty.

This implementation returns the result of

poll

unless the queue is empty.

**Specified by:** remove

in interface

Queue

<

E

>
**Returns:** the head of this queue
**Throws:** NoSuchElementException

- if this queue is empty

- element

```java
public
E
element()
```

Retrieves, but does not remove, the head of this queue. This method
differs from

peek

only in that it throws an exception if
this queue is empty.

This implementation returns the result of

peek

unless the queue is empty.

**Specified by:** element

in interface

Queue

<

E

>
**Returns:** the head of this queue
**Throws:** NoSuchElementException

- if this queue is empty

- clear

```java
public void clear()
```

Removes all of the elements from this queue.
The queue will be empty after this call returns.

This implementation repeatedly invokes

poll

until it
returns

null

.

**Specified by:** clear

in interface

Collection

<

E

>
**Overrides:** clear

in class

AbstractCollection

<

E

>

- addAll

```java
public boolean addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements in the specified collection to this
queue. Attempts to addAll of a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

This implementation iterates over the specified collection,
and adds each element returned by the iterator to this
queue, in turn. A runtime exception encountered while
trying to add an element (including, in particular, a

null

element) may result in only some of the elements
having been successfully added when the associated exception is
thrown.

**Specified by:** addAll

in interface

Collection

<

E

>
**Overrides:** addAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- collection containing elements to be added to this queue
**Returns:** true

if this queue changed as a result of the call
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified collection contains a
null element and this queue does not permit null elements,
or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this
queue, or if the specified collection is this queue
**Throws:** IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions
**See Also:** add(Object)

Constructor Detail

- AbstractQueue

```java
protected AbstractQueue()
```

Constructor for use by subclasses.

---

#### Constructor Detail

AbstractQueue

```java
protected AbstractQueue()
```

Constructor for use by subclasses.

---

#### AbstractQueue

protected AbstractQueue()

Constructor for use by subclasses.

Method Detail

- add

```java
public boolean add​(
E
e)
```

Inserts the specified element into this queue if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

This implementation returns

true

if

offer

succeeds,
else throws an

IllegalStateException

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
**Overrides:** add

in class

AbstractCollection

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
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null and
this queue does not permit null elements
**Throws:** IllegalArgumentException

- if some property of this element
prevents it from being added to this queue

- remove

```java
public
E
remove()
```

Retrieves and removes the head of this queue. This method differs
from

poll

only in that it throws an exception if this
queue is empty.

This implementation returns the result of

poll

unless the queue is empty.

**Specified by:** remove

in interface

Queue

<

E

>
**Returns:** the head of this queue
**Throws:** NoSuchElementException

- if this queue is empty

- element

```java
public
E
element()
```

Retrieves, but does not remove, the head of this queue. This method
differs from

peek

only in that it throws an exception if
this queue is empty.

This implementation returns the result of

peek

unless the queue is empty.

**Specified by:** element

in interface

Queue

<

E

>
**Returns:** the head of this queue
**Throws:** NoSuchElementException

- if this queue is empty

- clear

```java
public void clear()
```

Removes all of the elements from this queue.
The queue will be empty after this call returns.

This implementation repeatedly invokes

poll

until it
returns

null

.

**Specified by:** clear

in interface

Collection

<

E

>
**Overrides:** clear

in class

AbstractCollection

<

E

>

- addAll

```java
public boolean addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements in the specified collection to this
queue. Attempts to addAll of a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

This implementation iterates over the specified collection,
and adds each element returned by the iterator to this
queue, in turn. A runtime exception encountered while
trying to add an element (including, in particular, a

null

element) may result in only some of the elements
having been successfully added when the associated exception is
thrown.

**Specified by:** addAll

in interface

Collection

<

E

>
**Overrides:** addAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- collection containing elements to be added to this queue
**Returns:** true

if this queue changed as a result of the call
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified collection contains a
null element and this queue does not permit null elements,
or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this
queue, or if the specified collection is this queue
**Throws:** IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions
**See Also:** add(Object)

---

#### Method Detail

add

```java
public boolean add​(
E
e)
```

Inserts the specified element into this queue if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

This implementation returns

true

if

offer

succeeds,
else throws an

IllegalStateException

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
**Overrides:** add

in class

AbstractCollection

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
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null and
this queue does not permit null elements
**Throws:** IllegalArgumentException

- if some property of this element
prevents it from being added to this queue

---

#### add

public boolean add​(

E

e)

Inserts the specified element into this queue if it is possible to do so
immediately without violating capacity restrictions, returning

true

upon success and throwing an

IllegalStateException

if no space is currently available.

This implementation returns

true

if

offer

succeeds,
else throws an

IllegalStateException

.

This implementation returns

true

if

offer

succeeds,
else throws an

IllegalStateException

.

remove

```java
public
E
remove()
```

Retrieves and removes the head of this queue. This method differs
from

poll

only in that it throws an exception if this
queue is empty.

This implementation returns the result of

poll

unless the queue is empty.

**Specified by:** remove

in interface

Queue

<

E

>
**Returns:** the head of this queue
**Throws:** NoSuchElementException

- if this queue is empty

---

#### remove

public

E

remove()

Retrieves and removes the head of this queue. This method differs
from

poll

only in that it throws an exception if this
queue is empty.

This implementation returns the result of

poll

unless the queue is empty.

This implementation returns the result of

poll

unless the queue is empty.

element

```java
public
E
element()
```

Retrieves, but does not remove, the head of this queue. This method
differs from

peek

only in that it throws an exception if
this queue is empty.

This implementation returns the result of

peek

unless the queue is empty.

**Specified by:** element

in interface

Queue

<

E

>
**Returns:** the head of this queue
**Throws:** NoSuchElementException

- if this queue is empty

---

#### element

public

E

element()

Retrieves, but does not remove, the head of this queue. This method
differs from

peek

only in that it throws an exception if
this queue is empty.

This implementation returns the result of

peek

unless the queue is empty.

This implementation returns the result of

peek

unless the queue is empty.

clear

```java
public void clear()
```

Removes all of the elements from this queue.
The queue will be empty after this call returns.

This implementation repeatedly invokes

poll

until it
returns

null

.

**Specified by:** clear

in interface

Collection

<

E

>
**Overrides:** clear

in class

AbstractCollection

<

E

>

---

#### clear

public void clear()

Removes all of the elements from this queue.
The queue will be empty after this call returns.

This implementation repeatedly invokes

poll

until it
returns

null

.

This implementation repeatedly invokes

poll

until it
returns

null

.

addAll

```java
public boolean addAll​(
Collection
<? extends
E
> c)
```

Adds all of the elements in the specified collection to this
queue. Attempts to addAll of a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

This implementation iterates over the specified collection,
and adds each element returned by the iterator to this
queue, in turn. A runtime exception encountered while
trying to add an element (including, in particular, a

null

element) may result in only some of the elements
having been successfully added when the associated exception is
thrown.

**Specified by:** addAll

in interface

Collection

<

E

>
**Overrides:** addAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- collection containing elements to be added to this queue
**Returns:** true

if this queue changed as a result of the call
**Throws:** ClassCastException

- if the class of an element of the specified
collection prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified collection contains a
null element and this queue does not permit null elements,
or if the specified collection is null
**Throws:** IllegalArgumentException

- if some property of an element of the
specified collection prevents it from being added to this
queue, or if the specified collection is this queue
**Throws:** IllegalStateException

- if not all the elements can be added at
this time due to insertion restrictions
**See Also:** add(Object)

---

#### addAll

public boolean addAll​(

Collection

<? extends

E

> c)

Adds all of the elements in the specified collection to this
queue. Attempts to addAll of a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

This implementation iterates over the specified collection,
and adds each element returned by the iterator to this
queue, in turn. A runtime exception encountered while
trying to add an element (including, in particular, a

null

element) may result in only some of the elements
having been successfully added when the associated exception is
thrown.

This implementation iterates over the specified collection,
and adds each element returned by the iterator to this
queue, in turn. A runtime exception encountered while
trying to add an element (including, in particular, a

null

element) may result in only some of the elements
having been successfully added when the associated exception is
thrown.

---

