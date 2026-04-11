# Class SynchronousQueue<E>

**Source:** `java.base\java\util\concurrent\SynchronousQueue.html`

### Class Description

```java
public class
SynchronousQueue<E>

extends
AbstractQueue
<E>
implements
BlockingQueue
<E>,
Serializable
```

A

blocking queue

in which each insert
operation must wait for a corresponding remove operation by another
thread, and vice versa. A synchronous queue does not have any
internal capacity, not even a capacity of one. You cannot

peek

at a synchronous queue because an element is only
present when you try to remove it; you cannot insert an element
(using any method) unless another thread is trying to remove it;
you cannot iterate as there is nothing to iterate. The

head

of the queue is the element that the first queued
inserting thread is trying to add to the queue; if there is no such
queued thread then no element is available for removal and

poll()

will return

null

. For purposes of other

Collection

methods (for example

contains

), a

SynchronousQueue

acts as an empty collection. This queue
does not permit

null

elements.

Synchronous queues are similar to rendezvous channels used in
CSP and Ada. They are well suited for handoff designs, in which an
object running in one thread must sync up with an object running
in another thread in order to hand it some information, event, or
task.

This class supports an optional fairness policy for ordering
waiting producer and consumer threads. By default, this ordering
is not guaranteed. However, a queue constructed with fairness set
to

true

grants threads access in FIFO order.

This class and its iterator implement all of the

optional

methods of the

Collection

and

Iterator

interfaces.

This class is a member of the

Java Collections Framework

.

**Type Parameters:** E

- the type of elements held in this queue

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynchronousQueue()

Creates a

SynchronousQueue

with nonfair access policy.

---

#### public SynchronousQueue​(boolean fair)

Creates a

SynchronousQueue

with the specified fairness policy.

**Parameters:**
- fair

- if true, waiting threads contend in FIFO order for
access; otherwise the order is unspecified.

---

### Method Details

#### public void put​(
E
e)
throws
InterruptedException

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

**Specified by:**
- put

in interface

BlockingQueue

<

E

>

**Parameters:**
- e

- the element to add

**Throws:**
- InterruptedException

- if interrupted while waiting
- NullPointerException

- if the specified element is null

---

#### public boolean offer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

**Specified by:**
- offer

in interface

BlockingQueue

<

E

>

**Parameters:**
- e

- the element to add
- timeout

- how long to wait before giving up, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

timeout

parameter

**Returns:**
- true

if successful, or

false

if the
specified waiting time elapses before a consumer appears

**Throws:**
- InterruptedException

- if interrupted while waiting
- NullPointerException

- if the specified element is null

---

#### public boolean offer​(
E
e)

Inserts the specified element into this queue, if another thread is
waiting to receive it.

**Specified by:**
- offer

in interface

BlockingQueue

<

E

>
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

if the element was added to this queue, else

false

**Throws:**
- NullPointerException

- if the specified element is null

---

#### public
E
take()
throws
InterruptedException

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

**Specified by:**
- take

in interface

BlockingQueue

<

E

>

**Returns:**
- the head of this queue

**Throws:**
- InterruptedException

- if interrupted while waiting

---

#### public
E
poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

**Specified by:**
- poll

in interface

BlockingQueue

<

E

>

**Parameters:**
- timeout

- how long to wait before giving up, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

timeout

parameter

**Returns:**
- the head of this queue, or

null

if the
specified waiting time elapses before an element is present

**Throws:**
- InterruptedException

- if interrupted while waiting

---

#### public
E
poll()

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

**Specified by:**
- poll

in interface

Queue

<

E

>

**Returns:**
- the head of this queue, or

null

if no
element is available

---

#### public boolean isEmpty()

Always returns

true

.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- isEmpty

in interface

Collection

<

E

>

**Overrides:**
- isEmpty

in class

AbstractCollection

<

E

>

**Returns:**
- true

---

#### public int size()

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- size

in interface

Collection

<

E

>

**Returns:**
- zero

---

#### public int remainingCapacity()

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- remainingCapacity

in interface

BlockingQueue

<

E

>

**Returns:**
- zero

---

#### public void clear()

Does nothing.
A

SynchronousQueue

has no internal capacity.

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

AbstractQueue

<

E

>

---

#### public boolean contains​(
Object
o)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- contains

in interface

BlockingQueue

<

E

>
- contains

in interface

Collection

<

E

>

**Overrides:**
- contains

in class

AbstractCollection

<

E

>

**Parameters:**
- o

- the element

**Returns:**
- false

---

#### public boolean remove​(
Object
o)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- remove

in interface

BlockingQueue

<

E

>
- remove

in interface

Collection

<

E

>

**Overrides:**
- remove

in class

AbstractCollection

<

E

>

**Parameters:**
- o

- the element to remove

**Returns:**
- false

---

#### public boolean containsAll​(
Collection
<?> c)

Returns

false

unless the given collection is empty.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- containsAll

in interface

Collection

<

E

>

**Overrides:**
- containsAll

in class

AbstractCollection

<

E

>

**Parameters:**
- c

- the collection

**Returns:**
- false

unless given collection is empty

**See Also:**
- AbstractCollection.contains(Object)

---

#### public boolean removeAll​(
Collection
<?> c)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- removeAll

in interface

Collection

<

E

>

**Overrides:**
- removeAll

in class

AbstractCollection

<

E

>

**Parameters:**
- c

- the collection

**Returns:**
- false

**See Also:**
- AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

---

#### public boolean retainAll​(
Collection
<?> c)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:**
- retainAll

in interface

Collection

<

E

>

**Overrides:**
- retainAll

in class

AbstractCollection

<

E

>

**Parameters:**
- c

- the collection

**Returns:**
- false

**See Also:**
- AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

---

#### public
E
peek()

Always returns

null

.
A

SynchronousQueue

does not return elements
unless actively waited on.

**Specified by:**
- peek

in interface

Queue

<

E

>

**Returns:**
- null

---

#### public
Iterator
<
E
> iterator()

Returns an empty iterator in which

hasNext

always returns

false

.

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

in class

AbstractCollection

<

E

>

**Returns:**
- an empty iterator

---

#### public
Spliterator
<
E
> spliterator()

Returns an empty spliterator in which calls to

trySplit

always return

null

.

**Specified by:**
- spliterator

in interface

Collection

<

E

>
- spliterator

in interface

Iterable

<

E

>

**Returns:**
- an empty spliterator

**Since:**
- 1.8

---

#### public
Object
[] toArray()

Returns a zero-length array.

**Specified by:**
- toArray

in interface

Collection

<

E

>

**Overrides:**
- toArray

in class

AbstractCollection

<

E

>

**Returns:**
- a zero-length array

---

#### public <T> T[] toArray​(T[] a)

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

**Specified by:**
- toArray

in interface

Collection

<

E

>

**Overrides:**
- toArray

in class

AbstractCollection

<

E

>

**Parameters:**
- a

- the array

**Returns:**
- the specified array

**Throws:**
- NullPointerException

- if the specified array is null

**Type Parameters:**
- T

- the component type of the array to contain the collection

---

#### public
String
toString()

Always returns

"[]"

.

**Overrides:**
- toString

in class

AbstractCollection

<

E

>

**Returns:**
- "[]"

---

#### public int drainTo​(
Collection
<? super
E
> c)

Description copied from interface:

BlockingQueue

**Specified by:**
- drainTo

in interface

BlockingQueue

<

E

>

**Parameters:**
- c

- the collection to transfer elements into

**Returns:**
- the number of elements transferred

**Throws:**
- UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
- ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
- NullPointerException

- if the specified collection is null
- IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

---

#### public int drainTo​(
Collection
<? super
E
> c,
int maxElements)

Description copied from interface:

BlockingQueue

**Specified by:**
- drainTo

in interface

BlockingQueue

<

E

>

**Parameters:**
- c

- the collection to transfer elements into
- maxElements

- the maximum number of elements to transfer

**Returns:**
- the number of elements transferred

**Throws:**
- UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
- ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
- NullPointerException

- if the specified collection is null
- IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

---

### Additional Sections

#### Class SynchronousQueue<E>

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractQueue

<E>
- - java.util.concurrent.SynchronousQueue<E>

java.util.AbstractCollection

<E>

- java.util.AbstractQueue

<E>
- - java.util.concurrent.SynchronousQueue<E>

java.util.AbstractQueue

<E>

- java.util.concurrent.SynchronousQueue<E>

java.util.concurrent.SynchronousQueue<E>

**Type Parameters:** E

- the type of elements held in this queue

**All Implemented Interfaces:** Serializable

,

Iterable

<E>

,

Collection

<E>

,

BlockingQueue

<E>

,

Queue

<E>

```java
public class
SynchronousQueue<E>

extends
AbstractQueue
<E>
implements
BlockingQueue
<E>,
Serializable
```

A

blocking queue

in which each insert
operation must wait for a corresponding remove operation by another
thread, and vice versa. A synchronous queue does not have any
internal capacity, not even a capacity of one. You cannot

peek

at a synchronous queue because an element is only
present when you try to remove it; you cannot insert an element
(using any method) unless another thread is trying to remove it;
you cannot iterate as there is nothing to iterate. The

head

of the queue is the element that the first queued
inserting thread is trying to add to the queue; if there is no such
queued thread then no element is available for removal and

poll()

will return

null

. For purposes of other

Collection

methods (for example

contains

), a

SynchronousQueue

acts as an empty collection. This queue
does not permit

null

elements.

Synchronous queues are similar to rendezvous channels used in
CSP and Ada. They are well suited for handoff designs, in which an
object running in one thread must sync up with an object running
in another thread in order to hand it some information, event, or
task.

This class supports an optional fairness policy for ordering
waiting producer and consumer threads. By default, this ordering
is not guaranteed. However, a queue constructed with fairness set
to

true

grants threads access in FIFO order.

This class and its iterator implement all of the

optional

methods of the

Collection

and

Iterator

interfaces.

This class is a member of the

Java Collections Framework

.

**Since:** 1.5
**See Also:** Serialized Form

public class

SynchronousQueue<E>

extends

AbstractQueue

<E>
implements

BlockingQueue

<E>,

Serializable

A

blocking queue

in which each insert
operation must wait for a corresponding remove operation by another
thread, and vice versa. A synchronous queue does not have any
internal capacity, not even a capacity of one. You cannot

peek

at a synchronous queue because an element is only
present when you try to remove it; you cannot insert an element
(using any method) unless another thread is trying to remove it;
you cannot iterate as there is nothing to iterate. The

head

of the queue is the element that the first queued
inserting thread is trying to add to the queue; if there is no such
queued thread then no element is available for removal and

poll()

will return

null

. For purposes of other

Collection

methods (for example

contains

), a

SynchronousQueue

acts as an empty collection. This queue
does not permit

null

elements.

Synchronous queues are similar to rendezvous channels used in
CSP and Ada. They are well suited for handoff designs, in which an
object running in one thread must sync up with an object running
in another thread in order to hand it some information, event, or
task.

This class supports an optional fairness policy for ordering
waiting producer and consumer threads. By default, this ordering
is not guaranteed. However, a queue constructed with fairness set
to

true

grants threads access in FIFO order.

This class and its iterator implement all of the

optional

methods of the

Collection

and

Iterator

interfaces.

This class is a member of the

Java Collections Framework

.

Synchronous queues are similar to rendezvous channels used in
CSP and Ada. They are well suited for handoff designs, in which an
object running in one thread must sync up with an object running
in another thread in order to hand it some information, event, or
task.

This class supports an optional fairness policy for ordering
waiting producer and consumer threads. By default, this ordering
is not guaranteed. However, a queue constructed with fairness set
to

true

grants threads access in FIFO order.

This class and its iterator implement all of the

optional

methods of the

Collection

and

Iterator

interfaces.

This class is a member of the

Java Collections Framework

.

This class supports an optional fairness policy for ordering
waiting producer and consumer threads. By default, this ordering
is not guaranteed. However, a queue constructed with fairness set
to

true

grants threads access in FIFO order.

This class and its iterator implement all of the

optional

methods of the

Collection

and

Iterator

interfaces.

This class is a member of the

Java Collections Framework

.

This class and its iterator implement all of the

optional

methods of the

Collection

and

Iterator

interfaces.

This class is a member of the

Java Collections Framework

.

This class is a member of the

Java Collections Framework

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynchronousQueue

()

Creates a

SynchronousQueue

with nonfair access policy.

SynchronousQueue

​(boolean fair)

Creates a

SynchronousQueue

with the specified fairness policy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Does nothing.

boolean

contains

​(

Object

o)

Always returns

false

.

boolean

containsAll

​(

Collection

<?> c)

Returns

false

unless the given collection is empty.

int

drainTo

​(

Collection

<? super

E

> c)

Removes all available elements from this queue and adds them
to the given collection.

int

drainTo

​(

Collection

<? super

E

> c,
int maxElements)

Removes at most the given number of available elements from
this queue and adds them to the given collection.

boolean

isEmpty

()

Always returns

true

.

Iterator

<

E

>

iterator

()

Returns an empty iterator in which

hasNext

always returns

false

.

boolean

offer

​(

E

e)

Inserts the specified element into this queue, if another thread is
waiting to receive it.

boolean

offer

​(

E

e,
long timeout,

TimeUnit

unit)

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

E

peek

()

Always returns

null

.

E

poll

()

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

E

poll

​(long timeout,

TimeUnit

unit)

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

void

put

​(

E

e)

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

int

remainingCapacity

()

Always returns zero.

boolean

remove

​(

Object

o)

Always returns

false

.

boolean

removeAll

​(

Collection

<?> c)

Always returns

false

.

boolean

retainAll

​(

Collection

<?> c)

Always returns

false

.

int

size

()

Always returns zero.

Spliterator

<

E

>

spliterator

()

Returns an empty spliterator in which calls to

trySplit

always return

null

.

E

take

()

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

Object

[]

toArray

()

Returns a zero-length array.

<T> T[]

toArray

​(T[] a)

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

String

toString

()

Always returns

"[]"

.

- Methods declared in class java.util.

AbstractQueue

add

,

addAll

,

element

,

remove

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

- Methods declared in interface java.util.concurrent.

BlockingQueue

add

- Methods declared in interface java.util.

Collection

addAll

,

equals

,

hashCode

,

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

Queue

element

,

remove

Constructor Summary

Constructors

Constructor

Description

SynchronousQueue

()

Creates a

SynchronousQueue

with nonfair access policy.

SynchronousQueue

​(boolean fair)

Creates a

SynchronousQueue

with the specified fairness policy.

---

#### Constructor Summary

Creates a

SynchronousQueue

with nonfair access policy.

Creates a

SynchronousQueue

with the specified fairness policy.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Does nothing.

boolean

contains

​(

Object

o)

Always returns

false

.

boolean

containsAll

​(

Collection

<?> c)

Returns

false

unless the given collection is empty.

int

drainTo

​(

Collection

<? super

E

> c)

Removes all available elements from this queue and adds them
to the given collection.

int

drainTo

​(

Collection

<? super

E

> c,
int maxElements)

Removes at most the given number of available elements from
this queue and adds them to the given collection.

boolean

isEmpty

()

Always returns

true

.

Iterator

<

E

>

iterator

()

Returns an empty iterator in which

hasNext

always returns

false

.

boolean

offer

​(

E

e)

Inserts the specified element into this queue, if another thread is
waiting to receive it.

boolean

offer

​(

E

e,
long timeout,

TimeUnit

unit)

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

E

peek

()

Always returns

null

.

E

poll

()

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

E

poll

​(long timeout,

TimeUnit

unit)

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

void

put

​(

E

e)

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

int

remainingCapacity

()

Always returns zero.

boolean

remove

​(

Object

o)

Always returns

false

.

boolean

removeAll

​(

Collection

<?> c)

Always returns

false

.

boolean

retainAll

​(

Collection

<?> c)

Always returns

false

.

int

size

()

Always returns zero.

Spliterator

<

E

>

spliterator

()

Returns an empty spliterator in which calls to

trySplit

always return

null

.

E

take

()

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

Object

[]

toArray

()

Returns a zero-length array.

<T> T[]

toArray

​(T[] a)

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

String

toString

()

Always returns

"[]"

.

- Methods declared in class java.util.

AbstractQueue

add

,

addAll

,

element

,

remove

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

- Methods declared in interface java.util.concurrent.

BlockingQueue

add

- Methods declared in interface java.util.

Collection

addAll

,

equals

,

hashCode

,

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

Queue

element

,

remove

---

#### Method Summary

Does nothing.

Always returns

false

.

Returns

false

unless the given collection is empty.

Removes all available elements from this queue and adds them
to the given collection.

Removes at most the given number of available elements from
this queue and adds them to the given collection.

Always returns

true

.

Returns an empty iterator in which

hasNext

always returns

false

.

Inserts the specified element into this queue, if another thread is
waiting to receive it.

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

Always returns

null

.

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

Always returns zero.

Returns an empty spliterator in which calls to

trySplit

always return

null

.

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

Returns a zero-length array.

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

Always returns

"[]"

.

Methods declared in class java.util.

AbstractQueue

add

,

addAll

,

element

,

remove

---

#### Methods declared in class java.util. AbstractQueue

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

Methods declared in interface java.util.concurrent.

BlockingQueue

add

---

#### Methods declared in interface java.util.concurrent. BlockingQueue

Methods declared in interface java.util.

Collection

addAll

,

equals

,

hashCode

,

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

Queue

element

,

remove

---

#### Methods declared in interface java.util. Queue

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynchronousQueue

```java
public SynchronousQueue()
```

Creates a

SynchronousQueue

with nonfair access policy.

- SynchronousQueue

```java
public SynchronousQueue​(boolean fair)
```

Creates a

SynchronousQueue

with the specified fairness policy.

**Parameters:** fair

- if true, waiting threads contend in FIFO order for
access; otherwise the order is unspecified.

============ METHOD DETAIL ==========

- Method Detail

- put

```java
public void put​(
E
e)
throws
InterruptedException
```

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

**Specified by:** put

in interface

BlockingQueue

<

E

>
**Parameters:** e

- the element to add
**Throws:** InterruptedException

- if interrupted while waiting
**Throws:** NullPointerException

- if the specified element is null

- offer

```java
public boolean offer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

**Specified by:** offer

in interface

BlockingQueue

<

E

>
**Parameters:** e

- the element to add
**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** true

if successful, or

false

if the
specified waiting time elapses before a consumer appears
**Throws:** InterruptedException

- if interrupted while waiting
**Throws:** NullPointerException

- if the specified element is null

- offer

```java
public boolean offer​(
E
e)
```

Inserts the specified element into this queue, if another thread is
waiting to receive it.

**Specified by:** offer

in interface

BlockingQueue

<

E

>
**Specified by:** offer

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this queue, else

false
**Throws:** NullPointerException

- if the specified element is null

- take

```java
public
E
take()
throws
InterruptedException
```

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

**Specified by:** take

in interface

BlockingQueue

<

E

>
**Returns:** the head of this queue
**Throws:** InterruptedException

- if interrupted while waiting

- poll

```java
public
E
poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

**Specified by:** poll

in interface

BlockingQueue

<

E

>
**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** the head of this queue, or

null

if the
specified waiting time elapses before an element is present
**Throws:** InterruptedException

- if interrupted while waiting

- poll

```java
public
E
poll()
```

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

**Specified by:** poll

in interface

Queue

<

E

>
**Returns:** the head of this queue, or

null

if no
element is available

- isEmpty

```java
public boolean isEmpty()
```

Always returns

true

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** isEmpty

in interface

Collection

<

E

>
**Overrides:** isEmpty

in class

AbstractCollection

<

E

>
**Returns:** true

- size

```java
public int size()
```

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:** size

in interface

Collection

<

E

>
**Returns:** zero

- remainingCapacity

```java
public int remainingCapacity()
```

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:** remainingCapacity

in interface

BlockingQueue

<

E

>
**Returns:** zero

- clear

```java
public void clear()
```

Does nothing.
A

SynchronousQueue

has no internal capacity.

**Specified by:** clear

in interface

Collection

<

E

>
**Overrides:** clear

in class

AbstractQueue

<

E

>

- contains

```java
public boolean contains​(
Object
o)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** contains

in interface

BlockingQueue

<

E

>
**Specified by:** contains

in interface

Collection

<

E

>
**Overrides:** contains

in class

AbstractCollection

<

E

>
**Parameters:** o

- the element
**Returns:** false

- remove

```java
public boolean remove​(
Object
o)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** remove

in interface

BlockingQueue

<

E

>
**Specified by:** remove

in interface

Collection

<

E

>
**Overrides:** remove

in class

AbstractCollection

<

E

>
**Parameters:** o

- the element to remove
**Returns:** false

- containsAll

```java
public boolean containsAll​(
Collection
<?> c)
```

Returns

false

unless the given collection is empty.
A

SynchronousQueue

has no internal capacity.

**Specified by:** containsAll

in interface

Collection

<

E

>
**Overrides:** containsAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false

unless given collection is empty
**See Also:** AbstractCollection.contains(Object)

- removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** removeAll

in interface

Collection

<

E

>
**Overrides:** removeAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

- retainAll

```java
public boolean retainAll​(
Collection
<?> c)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** retainAll

in interface

Collection

<

E

>
**Overrides:** retainAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

- peek

```java
public
E
peek()
```

Always returns

null

.
A

SynchronousQueue

does not return elements
unless actively waited on.

**Specified by:** peek

in interface

Queue

<

E

>
**Returns:** null

- iterator

```java
public
Iterator
<
E
> iterator()
```

Returns an empty iterator in which

hasNext

always returns

false

.

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

in class

AbstractCollection

<

E

>
**Returns:** an empty iterator

- spliterator

```java
public
Spliterator
<
E
> spliterator()
```

Returns an empty spliterator in which calls to

trySplit

always return

null

.

**Specified by:** spliterator

in interface

Collection

<

E

>
**Specified by:** spliterator

in interface

Iterable

<

E

>
**Returns:** an empty spliterator
**Since:** 1.8

- toArray

```java
public
Object
[] toArray()
```

Returns a zero-length array.

**Specified by:** toArray

in interface

Collection

<

E

>
**Overrides:** toArray

in class

AbstractCollection

<

E

>
**Returns:** a zero-length array

- toArray

```java
public <T> T[] toArray​(T[] a)
```

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

**Specified by:** toArray

in interface

Collection

<

E

>
**Overrides:** toArray

in class

AbstractCollection

<

E

>
**Type Parameters:** T

- the component type of the array to contain the collection
**Parameters:** a

- the array
**Returns:** the specified array
**Throws:** NullPointerException

- if the specified array is null

- toString

```java
public
String
toString()
```

Always returns

"[]"

.

**Overrides:** toString

in class

AbstractCollection

<

E

>
**Returns:** "[]"

- drainTo

```java
public int drainTo​(
Collection
<? super
E
> c)
```

Description copied from interface:

BlockingQueue

Removes all available elements from this queue and adds them
to the given collection. This operation may be more
efficient than repeatedly polling this queue. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

**Specified by:** drainTo

in interface

BlockingQueue

<

E

>
**Parameters:** c

- the collection to transfer elements into
**Returns:** the number of elements transferred
**Throws:** UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
**Throws:** ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
**Throws:** NullPointerException

- if the specified collection is null
**Throws:** IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

- drainTo

```java
public int drainTo​(
Collection
<? super
E
> c,
int maxElements)
```

Description copied from interface:

BlockingQueue

Removes at most the given number of available elements from
this queue and adds them to the given collection. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

**Specified by:** drainTo

in interface

BlockingQueue

<

E

>
**Parameters:** c

- the collection to transfer elements into
**Parameters:** maxElements

- the maximum number of elements to transfer
**Returns:** the number of elements transferred
**Throws:** UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
**Throws:** ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
**Throws:** NullPointerException

- if the specified collection is null
**Throws:** IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

Constructor Detail

- SynchronousQueue

```java
public SynchronousQueue()
```

Creates a

SynchronousQueue

with nonfair access policy.

- SynchronousQueue

```java
public SynchronousQueue​(boolean fair)
```

Creates a

SynchronousQueue

with the specified fairness policy.

**Parameters:** fair

- if true, waiting threads contend in FIFO order for
access; otherwise the order is unspecified.

---

#### Constructor Detail

SynchronousQueue

```java
public SynchronousQueue()
```

Creates a

SynchronousQueue

with nonfair access policy.

---

#### SynchronousQueue

public SynchronousQueue()

Creates a

SynchronousQueue

with nonfair access policy.

SynchronousQueue

```java
public SynchronousQueue​(boolean fair)
```

Creates a

SynchronousQueue

with the specified fairness policy.

**Parameters:** fair

- if true, waiting threads contend in FIFO order for
access; otherwise the order is unspecified.

---

#### SynchronousQueue

public SynchronousQueue​(boolean fair)

Creates a

SynchronousQueue

with the specified fairness policy.

Method Detail

- put

```java
public void put​(
E
e)
throws
InterruptedException
```

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

**Specified by:** put

in interface

BlockingQueue

<

E

>
**Parameters:** e

- the element to add
**Throws:** InterruptedException

- if interrupted while waiting
**Throws:** NullPointerException

- if the specified element is null

- offer

```java
public boolean offer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

**Specified by:** offer

in interface

BlockingQueue

<

E

>
**Parameters:** e

- the element to add
**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** true

if successful, or

false

if the
specified waiting time elapses before a consumer appears
**Throws:** InterruptedException

- if interrupted while waiting
**Throws:** NullPointerException

- if the specified element is null

- offer

```java
public boolean offer​(
E
e)
```

Inserts the specified element into this queue, if another thread is
waiting to receive it.

**Specified by:** offer

in interface

BlockingQueue

<

E

>
**Specified by:** offer

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this queue, else

false
**Throws:** NullPointerException

- if the specified element is null

- take

```java
public
E
take()
throws
InterruptedException
```

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

**Specified by:** take

in interface

BlockingQueue

<

E

>
**Returns:** the head of this queue
**Throws:** InterruptedException

- if interrupted while waiting

- poll

```java
public
E
poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

**Specified by:** poll

in interface

BlockingQueue

<

E

>
**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** the head of this queue, or

null

if the
specified waiting time elapses before an element is present
**Throws:** InterruptedException

- if interrupted while waiting

- poll

```java
public
E
poll()
```

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

**Specified by:** poll

in interface

Queue

<

E

>
**Returns:** the head of this queue, or

null

if no
element is available

- isEmpty

```java
public boolean isEmpty()
```

Always returns

true

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** isEmpty

in interface

Collection

<

E

>
**Overrides:** isEmpty

in class

AbstractCollection

<

E

>
**Returns:** true

- size

```java
public int size()
```

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:** size

in interface

Collection

<

E

>
**Returns:** zero

- remainingCapacity

```java
public int remainingCapacity()
```

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:** remainingCapacity

in interface

BlockingQueue

<

E

>
**Returns:** zero

- clear

```java
public void clear()
```

Does nothing.
A

SynchronousQueue

has no internal capacity.

**Specified by:** clear

in interface

Collection

<

E

>
**Overrides:** clear

in class

AbstractQueue

<

E

>

- contains

```java
public boolean contains​(
Object
o)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** contains

in interface

BlockingQueue

<

E

>
**Specified by:** contains

in interface

Collection

<

E

>
**Overrides:** contains

in class

AbstractCollection

<

E

>
**Parameters:** o

- the element
**Returns:** false

- remove

```java
public boolean remove​(
Object
o)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** remove

in interface

BlockingQueue

<

E

>
**Specified by:** remove

in interface

Collection

<

E

>
**Overrides:** remove

in class

AbstractCollection

<

E

>
**Parameters:** o

- the element to remove
**Returns:** false

- containsAll

```java
public boolean containsAll​(
Collection
<?> c)
```

Returns

false

unless the given collection is empty.
A

SynchronousQueue

has no internal capacity.

**Specified by:** containsAll

in interface

Collection

<

E

>
**Overrides:** containsAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false

unless given collection is empty
**See Also:** AbstractCollection.contains(Object)

- removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** removeAll

in interface

Collection

<

E

>
**Overrides:** removeAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

- retainAll

```java
public boolean retainAll​(
Collection
<?> c)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** retainAll

in interface

Collection

<

E

>
**Overrides:** retainAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

- peek

```java
public
E
peek()
```

Always returns

null

.
A

SynchronousQueue

does not return elements
unless actively waited on.

**Specified by:** peek

in interface

Queue

<

E

>
**Returns:** null

- iterator

```java
public
Iterator
<
E
> iterator()
```

Returns an empty iterator in which

hasNext

always returns

false

.

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

in class

AbstractCollection

<

E

>
**Returns:** an empty iterator

- spliterator

```java
public
Spliterator
<
E
> spliterator()
```

Returns an empty spliterator in which calls to

trySplit

always return

null

.

**Specified by:** spliterator

in interface

Collection

<

E

>
**Specified by:** spliterator

in interface

Iterable

<

E

>
**Returns:** an empty spliterator
**Since:** 1.8

- toArray

```java
public
Object
[] toArray()
```

Returns a zero-length array.

**Specified by:** toArray

in interface

Collection

<

E

>
**Overrides:** toArray

in class

AbstractCollection

<

E

>
**Returns:** a zero-length array

- toArray

```java
public <T> T[] toArray​(T[] a)
```

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

**Specified by:** toArray

in interface

Collection

<

E

>
**Overrides:** toArray

in class

AbstractCollection

<

E

>
**Type Parameters:** T

- the component type of the array to contain the collection
**Parameters:** a

- the array
**Returns:** the specified array
**Throws:** NullPointerException

- if the specified array is null

- toString

```java
public
String
toString()
```

Always returns

"[]"

.

**Overrides:** toString

in class

AbstractCollection

<

E

>
**Returns:** "[]"

- drainTo

```java
public int drainTo​(
Collection
<? super
E
> c)
```

Description copied from interface:

BlockingQueue

Removes all available elements from this queue and adds them
to the given collection. This operation may be more
efficient than repeatedly polling this queue. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

**Specified by:** drainTo

in interface

BlockingQueue

<

E

>
**Parameters:** c

- the collection to transfer elements into
**Returns:** the number of elements transferred
**Throws:** UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
**Throws:** ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
**Throws:** NullPointerException

- if the specified collection is null
**Throws:** IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

- drainTo

```java
public int drainTo​(
Collection
<? super
E
> c,
int maxElements)
```

Description copied from interface:

BlockingQueue

Removes at most the given number of available elements from
this queue and adds them to the given collection. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

**Specified by:** drainTo

in interface

BlockingQueue

<

E

>
**Parameters:** c

- the collection to transfer elements into
**Parameters:** maxElements

- the maximum number of elements to transfer
**Returns:** the number of elements transferred
**Throws:** UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
**Throws:** ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
**Throws:** NullPointerException

- if the specified collection is null
**Throws:** IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

---

#### Method Detail

put

```java
public void put​(
E
e)
throws
InterruptedException
```

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

**Specified by:** put

in interface

BlockingQueue

<

E

>
**Parameters:** e

- the element to add
**Throws:** InterruptedException

- if interrupted while waiting
**Throws:** NullPointerException

- if the specified element is null

---

#### put

public void put​(

E

e)
throws

InterruptedException

Adds the specified element to this queue, waiting if necessary for
another thread to receive it.

offer

```java
public boolean offer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

**Specified by:** offer

in interface

BlockingQueue

<

E

>
**Parameters:** e

- the element to add
**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** true

if successful, or

false

if the
specified waiting time elapses before a consumer appears
**Throws:** InterruptedException

- if interrupted while waiting
**Throws:** NullPointerException

- if the specified element is null

---

#### offer

public boolean offer​(

E

e,
long timeout,

TimeUnit

unit)
throws

InterruptedException

Inserts the specified element into this queue, waiting if necessary
up to the specified wait time for another thread to receive it.

offer

```java
public boolean offer​(
E
e)
```

Inserts the specified element into this queue, if another thread is
waiting to receive it.

**Specified by:** offer

in interface

BlockingQueue

<

E

>
**Specified by:** offer

in interface

Queue

<

E

>
**Parameters:** e

- the element to add
**Returns:** true

if the element was added to this queue, else

false
**Throws:** NullPointerException

- if the specified element is null

---

#### offer

public boolean offer​(

E

e)

Inserts the specified element into this queue, if another thread is
waiting to receive it.

take

```java
public
E
take()
throws
InterruptedException
```

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

**Specified by:** take

in interface

BlockingQueue

<

E

>
**Returns:** the head of this queue
**Throws:** InterruptedException

- if interrupted while waiting

---

#### take

public

E

take()
throws

InterruptedException

Retrieves and removes the head of this queue, waiting if necessary
for another thread to insert it.

poll

```java
public
E
poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

**Specified by:** poll

in interface

BlockingQueue

<

E

>
**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** the head of this queue, or

null

if the
specified waiting time elapses before an element is present
**Throws:** InterruptedException

- if interrupted while waiting

---

#### poll

public

E

poll​(long timeout,

TimeUnit

unit)
throws

InterruptedException

Retrieves and removes the head of this queue, waiting
if necessary up to the specified wait time, for another thread
to insert it.

poll

```java
public
E
poll()
```

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

**Specified by:** poll

in interface

Queue

<

E

>
**Returns:** the head of this queue, or

null

if no
element is available

---

#### poll

public

E

poll()

Retrieves and removes the head of this queue, if another thread
is currently making an element available.

isEmpty

```java
public boolean isEmpty()
```

Always returns

true

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** isEmpty

in interface

Collection

<

E

>
**Overrides:** isEmpty

in class

AbstractCollection

<

E

>
**Returns:** true

---

#### isEmpty

public boolean isEmpty()

Always returns

true

.
A

SynchronousQueue

has no internal capacity.

size

```java
public int size()
```

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:** size

in interface

Collection

<

E

>
**Returns:** zero

---

#### size

public int size()

Always returns zero.
A

SynchronousQueue

has no internal capacity.

remainingCapacity

```java
public int remainingCapacity()
```

Always returns zero.
A

SynchronousQueue

has no internal capacity.

**Specified by:** remainingCapacity

in interface

BlockingQueue

<

E

>
**Returns:** zero

---

#### remainingCapacity

public int remainingCapacity()

Always returns zero.
A

SynchronousQueue

has no internal capacity.

clear

```java
public void clear()
```

Does nothing.
A

SynchronousQueue

has no internal capacity.

**Specified by:** clear

in interface

Collection

<

E

>
**Overrides:** clear

in class

AbstractQueue

<

E

>

---

#### clear

public void clear()

Does nothing.
A

SynchronousQueue

has no internal capacity.

contains

```java
public boolean contains​(
Object
o)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** contains

in interface

BlockingQueue

<

E

>
**Specified by:** contains

in interface

Collection

<

E

>
**Overrides:** contains

in class

AbstractCollection

<

E

>
**Parameters:** o

- the element
**Returns:** false

---

#### contains

public boolean contains​(

Object

o)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

remove

```java
public boolean remove​(
Object
o)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** remove

in interface

BlockingQueue

<

E

>
**Specified by:** remove

in interface

Collection

<

E

>
**Overrides:** remove

in class

AbstractCollection

<

E

>
**Parameters:** o

- the element to remove
**Returns:** false

---

#### remove

public boolean remove​(

Object

o)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

containsAll

```java
public boolean containsAll​(
Collection
<?> c)
```

Returns

false

unless the given collection is empty.
A

SynchronousQueue

has no internal capacity.

**Specified by:** containsAll

in interface

Collection

<

E

>
**Overrides:** containsAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false

unless given collection is empty
**See Also:** AbstractCollection.contains(Object)

---

#### containsAll

public boolean containsAll​(

Collection

<?> c)

Returns

false

unless the given collection is empty.
A

SynchronousQueue

has no internal capacity.

removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** removeAll

in interface

Collection

<

E

>
**Overrides:** removeAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

---

#### removeAll

public boolean removeAll​(

Collection

<?> c)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

retainAll

```java
public boolean retainAll​(
Collection
<?> c)
```

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

**Specified by:** retainAll

in interface

Collection

<

E

>
**Overrides:** retainAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- the collection
**Returns:** false
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

---

#### retainAll

public boolean retainAll​(

Collection

<?> c)

Always returns

false

.
A

SynchronousQueue

has no internal capacity.

peek

```java
public
E
peek()
```

Always returns

null

.
A

SynchronousQueue

does not return elements
unless actively waited on.

**Specified by:** peek

in interface

Queue

<

E

>
**Returns:** null

---

#### peek

public

E

peek()

Always returns

null

.
A

SynchronousQueue

does not return elements
unless actively waited on.

iterator

```java
public
Iterator
<
E
> iterator()
```

Returns an empty iterator in which

hasNext

always returns

false

.

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

in class

AbstractCollection

<

E

>
**Returns:** an empty iterator

---

#### iterator

public

Iterator

<

E

> iterator()

Returns an empty iterator in which

hasNext

always returns

false

.

spliterator

```java
public
Spliterator
<
E
> spliterator()
```

Returns an empty spliterator in which calls to

trySplit

always return

null

.

**Specified by:** spliterator

in interface

Collection

<

E

>
**Specified by:** spliterator

in interface

Iterable

<

E

>
**Returns:** an empty spliterator
**Since:** 1.8

---

#### spliterator

public

Spliterator

<

E

> spliterator()

Returns an empty spliterator in which calls to

trySplit

always return

null

.

toArray

```java
public
Object
[] toArray()
```

Returns a zero-length array.

**Specified by:** toArray

in interface

Collection

<

E

>
**Overrides:** toArray

in class

AbstractCollection

<

E

>
**Returns:** a zero-length array

---

#### toArray

public

Object

[] toArray()

Returns a zero-length array.

toArray

```java
public <T> T[] toArray​(T[] a)
```

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

**Specified by:** toArray

in interface

Collection

<

E

>
**Overrides:** toArray

in class

AbstractCollection

<

E

>
**Type Parameters:** T

- the component type of the array to contain the collection
**Parameters:** a

- the array
**Returns:** the specified array
**Throws:** NullPointerException

- if the specified array is null

---

#### toArray

public <T> T[] toArray​(T[] a)

Sets the zeroth element of the specified array to

null

(if the array has non-zero length) and returns it.

toString

```java
public
String
toString()
```

Always returns

"[]"

.

**Overrides:** toString

in class

AbstractCollection

<

E

>
**Returns:** "[]"

---

#### toString

public

String

toString()

Always returns

"[]"

.

drainTo

```java
public int drainTo​(
Collection
<? super
E
> c)
```

Description copied from interface:

BlockingQueue

Removes all available elements from this queue and adds them
to the given collection. This operation may be more
efficient than repeatedly polling this queue. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

**Specified by:** drainTo

in interface

BlockingQueue

<

E

>
**Parameters:** c

- the collection to transfer elements into
**Returns:** the number of elements transferred
**Throws:** UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
**Throws:** ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
**Throws:** NullPointerException

- if the specified collection is null
**Throws:** IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

---

#### drainTo

public int drainTo​(

Collection

<? super

E

> c)

Description copied from interface:

BlockingQueue

Removes all available elements from this queue and adds them
to the given collection. This operation may be more
efficient than repeatedly polling this queue. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

drainTo

```java
public int drainTo​(
Collection
<? super
E
> c,
int maxElements)
```

Description copied from interface:

BlockingQueue

Removes at most the given number of available elements from
this queue and adds them to the given collection. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

**Specified by:** drainTo

in interface

BlockingQueue

<

E

>
**Parameters:** c

- the collection to transfer elements into
**Parameters:** maxElements

- the maximum number of elements to transfer
**Returns:** the number of elements transferred
**Throws:** UnsupportedOperationException

- if addition of elements
is not supported by the specified collection
**Throws:** ClassCastException

- if the class of an element of this queue
prevents it from being added to the specified collection
**Throws:** NullPointerException

- if the specified collection is null
**Throws:** IllegalArgumentException

- if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection

---

#### drainTo

public int drainTo​(

Collection

<? super

E

> c,
int maxElements)

Description copied from interface:

BlockingQueue

Removes at most the given number of available elements from
this queue and adds them to the given collection. A failure
encountered while attempting to add elements to
collection

c

may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in

IllegalArgumentException

. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.

---

