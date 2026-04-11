# Interface TransferQueue<E>

**Source:** `java.base\java\util\concurrent\TransferQueue.html`

### Class Description

```java
public interface
TransferQueue<E>

extends
BlockingQueue
<E>
```

A

BlockingQueue

in which producers may wait for consumers
to receive elements. A

TransferQueue

may be useful for
example in message passing applications in which producers
sometimes (using method

transfer(E)

) await receipt of
elements by consumers invoking

take

or

poll

, while
at other times enqueue elements (via method

put

) without
waiting for receipt.

Non-blocking

and

time-out

versions of

tryTransfer

are also available.
A

TransferQueue

may also be queried, via

hasWaitingConsumer()

, whether there are any threads waiting for
items, which is a converse analogy to a

peek

operation.

Like other blocking queues, a

TransferQueue

may be
capacity bounded. If so, an attempted transfer operation may
initially block waiting for available space, and/or subsequently
block waiting for reception by a consumer. Note that in a queue
with zero capacity, such as

SynchronousQueue

,

put

and

transfer

are effectively synonymous.

This interface is a member of the

Java Collections Framework

.

**Type Parameters:** E

- the type of elements held in this queue

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean tryTransfer​(
E
e)

Transfers the element to a waiting consumer immediately, if possible.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
otherwise returning

false

without enqueuing the element.

**Parameters:**
- e

- the element to transfer

**Returns:**
- true

if the element was transferred, else

false

**Throws:**
- ClassCastException

- if the class of the specified element
prevents it from being added to this queue
- NullPointerException

- if the specified element is null
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

---

#### void transfer​(
E
e)
throws
InterruptedException

Transfers the element to a consumer, waiting if necessary to do so.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer.

**Parameters:**
- e

- the element to transfer

**Throws:**
- InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
- ClassCastException

- if the class of the specified element
prevents it from being added to this queue
- NullPointerException

- if the specified element is null
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

---

#### boolean tryTransfer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer,
returning

false

if the specified wait time elapses
before the element can be transferred.

**Parameters:**
- e

- the element to transfer
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

if
the specified waiting time elapses before completion,
in which case the element is not left enqueued

**Throws:**
- InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
- ClassCastException

- if the class of the specified element
prevents it from being added to this queue
- NullPointerException

- if the specified element is null
- IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

---

#### boolean hasWaitingConsumer()

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.
The return value represents a momentary state of affairs.

**Returns:**
- true

if there is at least one waiting consumer

---

#### int getWaitingConsumerCount()

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

. The return value is an
approximation of a momentary state of affairs, that may be
inaccurate if consumers have completed or given up waiting.
The value may be useful for monitoring and heuristics, but
not for synchronization control. Implementations of this
method are likely to be noticeably slower than those for

hasWaitingConsumer()

.

**Returns:**
- the number of consumers waiting to receive elements

---

### Additional Sections

#### Interface TransferQueue<E>

**Type Parameters:** E

- the type of elements held in this queue

**All Superinterfaces:** BlockingQueue

<E>

,

Collection

<E>

,

Iterable

<E>

,

Queue

<E>

**All Known Implementing Classes:** LinkedTransferQueue

```java
public interface
TransferQueue<E>

extends
BlockingQueue
<E>
```

A

BlockingQueue

in which producers may wait for consumers
to receive elements. A

TransferQueue

may be useful for
example in message passing applications in which producers
sometimes (using method

transfer(E)

) await receipt of
elements by consumers invoking

take

or

poll

, while
at other times enqueue elements (via method

put

) without
waiting for receipt.

Non-blocking

and

time-out

versions of

tryTransfer

are also available.
A

TransferQueue

may also be queried, via

hasWaitingConsumer()

, whether there are any threads waiting for
items, which is a converse analogy to a

peek

operation.

Like other blocking queues, a

TransferQueue

may be
capacity bounded. If so, an attempted transfer operation may
initially block waiting for available space, and/or subsequently
block waiting for reception by a consumer. Note that in a queue
with zero capacity, such as

SynchronousQueue

,

put

and

transfer

are effectively synonymous.

This interface is a member of the

Java Collections Framework

.

**Since:** 1.7

public interface

TransferQueue<E>

extends

BlockingQueue

<E>

A

BlockingQueue

in which producers may wait for consumers
to receive elements. A

TransferQueue

may be useful for
example in message passing applications in which producers
sometimes (using method

transfer(E)

) await receipt of
elements by consumers invoking

take

or

poll

, while
at other times enqueue elements (via method

put

) without
waiting for receipt.

Non-blocking

and

time-out

versions of

tryTransfer

are also available.
A

TransferQueue

may also be queried, via

hasWaitingConsumer()

, whether there are any threads waiting for
items, which is a converse analogy to a

peek

operation.

Like other blocking queues, a

TransferQueue

may be
capacity bounded. If so, an attempted transfer operation may
initially block waiting for available space, and/or subsequently
block waiting for reception by a consumer. Note that in a queue
with zero capacity, such as

SynchronousQueue

,

put

and

transfer

are effectively synonymous.

This interface is a member of the

Java Collections Framework

.

Like other blocking queues, a

TransferQueue

may be
capacity bounded. If so, an attempted transfer operation may
initially block waiting for available space, and/or subsequently
block waiting for reception by a consumer. Note that in a queue
with zero capacity, such as

SynchronousQueue

,

put

and

transfer

are effectively synonymous.

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

int

getWaitingConsumerCount

()

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

.

boolean

hasWaitingConsumer

()

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.

void

transfer

​(

E

e)

Transfers the element to a consumer, waiting if necessary to do so.

boolean

tryTransfer

​(

E

e)

Transfers the element to a waiting consumer immediately, if possible.

boolean

tryTransfer

​(

E

e,
long timeout,

TimeUnit

unit)

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

- Methods declared in interface java.util.concurrent.

BlockingQueue

add

,

contains

,

drainTo

,

drainTo

,

offer

,

offer

,

poll

,

put

,

remainingCapacity

,

remove

,

take

- Methods declared in interface java.util.

Collection

addAll

,

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

iterator

,

parallelStream

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

element

,

peek

,

poll

,

remove

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getWaitingConsumerCount

()

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

.

boolean

hasWaitingConsumer

()

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.

void

transfer

​(

E

e)

Transfers the element to a consumer, waiting if necessary to do so.

boolean

tryTransfer

​(

E

e)

Transfers the element to a waiting consumer immediately, if possible.

boolean

tryTransfer

​(

E

e,
long timeout,

TimeUnit

unit)

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

- Methods declared in interface java.util.concurrent.

BlockingQueue

add

,

contains

,

drainTo

,

drainTo

,

offer

,

offer

,

poll

,

put

,

remainingCapacity

,

remove

,

take

- Methods declared in interface java.util.

Collection

addAll

,

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

iterator

,

parallelStream

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

element

,

peek

,

poll

,

remove

---

#### Method Summary

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

.

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.

Transfers the element to a consumer, waiting if necessary to do so.

Transfers the element to a waiting consumer immediately, if possible.

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

Methods declared in interface java.util.concurrent.

BlockingQueue

add

,

contains

,

drainTo

,

drainTo

,

offer

,

offer

,

poll

,

put

,

remainingCapacity

,

remove

,

take

---

#### Methods declared in interface java.util.concurrent. BlockingQueue

Methods declared in interface java.util.

Collection

addAll

,

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

iterator

,

parallelStream

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

element

,

peek

,

poll

,

remove

---

#### Methods declared in interface java.util. Queue

============ METHOD DETAIL ==========

- Method Detail

- tryTransfer

```java
boolean tryTransfer​(
E
e)
```

Transfers the element to a waiting consumer immediately, if possible.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
otherwise returning

false

without enqueuing the element.

**Parameters:** e

- the element to transfer
**Returns:** true

if the element was transferred, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

- transfer

```java
void transfer​(
E
e)
throws
InterruptedException
```

Transfers the element to a consumer, waiting if necessary to do so.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer.

**Parameters:** e

- the element to transfer
**Throws:** InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

- tryTransfer

```java
boolean tryTransfer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer,
returning

false

if the specified wait time elapses
before the element can be transferred.

**Parameters:** e

- the element to transfer
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

if
the specified waiting time elapses before completion,
in which case the element is not left enqueued
**Throws:** InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

- hasWaitingConsumer

```java
boolean hasWaitingConsumer()
```

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.
The return value represents a momentary state of affairs.

**Returns:** true

if there is at least one waiting consumer

- getWaitingConsumerCount

```java
int getWaitingConsumerCount()
```

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

. The return value is an
approximation of a momentary state of affairs, that may be
inaccurate if consumers have completed or given up waiting.
The value may be useful for monitoring and heuristics, but
not for synchronization control. Implementations of this
method are likely to be noticeably slower than those for

hasWaitingConsumer()

.

**Returns:** the number of consumers waiting to receive elements

Method Detail

- tryTransfer

```java
boolean tryTransfer​(
E
e)
```

Transfers the element to a waiting consumer immediately, if possible.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
otherwise returning

false

without enqueuing the element.

**Parameters:** e

- the element to transfer
**Returns:** true

if the element was transferred, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

- transfer

```java
void transfer​(
E
e)
throws
InterruptedException
```

Transfers the element to a consumer, waiting if necessary to do so.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer.

**Parameters:** e

- the element to transfer
**Throws:** InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

- tryTransfer

```java
boolean tryTransfer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer,
returning

false

if the specified wait time elapses
before the element can be transferred.

**Parameters:** e

- the element to transfer
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

if
the specified waiting time elapses before completion,
in which case the element is not left enqueued
**Throws:** InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

- hasWaitingConsumer

```java
boolean hasWaitingConsumer()
```

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.
The return value represents a momentary state of affairs.

**Returns:** true

if there is at least one waiting consumer

- getWaitingConsumerCount

```java
int getWaitingConsumerCount()
```

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

. The return value is an
approximation of a momentary state of affairs, that may be
inaccurate if consumers have completed or given up waiting.
The value may be useful for monitoring and heuristics, but
not for synchronization control. Implementations of this
method are likely to be noticeably slower than those for

hasWaitingConsumer()

.

**Returns:** the number of consumers waiting to receive elements

---

#### Method Detail

tryTransfer

```java
boolean tryTransfer​(
E
e)
```

Transfers the element to a waiting consumer immediately, if possible.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
otherwise returning

false

without enqueuing the element.

**Parameters:** e

- the element to transfer
**Returns:** true

if the element was transferred, else

false
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

---

#### tryTransfer

boolean tryTransfer​(

E

e)

Transfers the element to a waiting consumer immediately, if possible.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
otherwise returning

false

without enqueuing the element.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
otherwise returning

false

without enqueuing the element.

transfer

```java
void transfer​(
E
e)
throws
InterruptedException
```

Transfers the element to a consumer, waiting if necessary to do so.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer.

**Parameters:** e

- the element to transfer
**Throws:** InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

---

#### transfer

void transfer​(

E

e)
throws

InterruptedException

Transfers the element to a consumer, waiting if necessary to do so.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer.

tryTransfer

```java
boolean tryTransfer​(
E
e,
long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer,
returning

false

if the specified wait time elapses
before the element can be transferred.

**Parameters:** e

- the element to transfer
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

if
the specified waiting time elapses before completion,
in which case the element is not left enqueued
**Throws:** InterruptedException

- if interrupted while waiting,
in which case the element is not left enqueued
**Throws:** ClassCastException

- if the class of the specified element
prevents it from being added to this queue
**Throws:** NullPointerException

- if the specified element is null
**Throws:** IllegalArgumentException

- if some property of the specified
element prevents it from being added to this queue

---

#### tryTransfer

boolean tryTransfer​(

E

e,
long timeout,

TimeUnit

unit)
throws

InterruptedException

Transfers the element to a consumer if it is possible to do so
before the timeout elapses.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer,
returning

false

if the specified wait time elapses
before the element can be transferred.

More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in

BlockingQueue.take()

or timed

poll

),
else waits until the element is received by a consumer,
returning

false

if the specified wait time elapses
before the element can be transferred.

hasWaitingConsumer

```java
boolean hasWaitingConsumer()
```

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.
The return value represents a momentary state of affairs.

**Returns:** true

if there is at least one waiting consumer

---

#### hasWaitingConsumer

boolean hasWaitingConsumer()

Returns

true

if there is at least one consumer waiting
to receive an element via

BlockingQueue.take()

or
timed

poll

.
The return value represents a momentary state of affairs.

getWaitingConsumerCount

```java
int getWaitingConsumerCount()
```

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

. The return value is an
approximation of a momentary state of affairs, that may be
inaccurate if consumers have completed or given up waiting.
The value may be useful for monitoring and heuristics, but
not for synchronization control. Implementations of this
method are likely to be noticeably slower than those for

hasWaitingConsumer()

.

**Returns:** the number of consumers waiting to receive elements

---

#### getWaitingConsumerCount

int getWaitingConsumerCount()

Returns an estimate of the number of consumers waiting to
receive elements via

BlockingQueue.take()

or timed

poll

. The return value is an
approximation of a momentary state of affairs, that may be
inaccurate if consumers have completed or given up waiting.
The value may be useful for monitoring and heuristics, but
not for synchronization control. Implementations of this
method are likely to be noticeably slower than those for

hasWaitingConsumer()

.

---

