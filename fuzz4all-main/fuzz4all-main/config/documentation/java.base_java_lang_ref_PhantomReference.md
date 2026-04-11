# Class PhantomReference<T>

**Source:** `java.base\java\lang\ref\PhantomReference.html`

### Class Description

```java
public class
PhantomReference<T>

extends
Reference
<T>
```

Phantom reference objects, which are enqueued after the collector
determines that their referents may otherwise be reclaimed. Phantom
references are most often used to schedule post-mortem cleanup actions.

Suppose the garbage collector determines at a certain point in time
that an object is

phantom reachable

. At that time it will atomically clear
all phantom references to that object and all phantom references to
any other phantom-reachable objects from which that object is reachable.
At the same time or at some later time it will enqueue those newly-cleared
phantom references that are registered with reference queues.

In order to ensure that a reclaimable object remains so, the referent of
a phantom reference may not be retrieved: The

get

method of a
phantom reference always returns

null

.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

#### public PhantomReference​(
T
referent,

ReferenceQueue
<? super
T
> q)

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

It is possible to create a phantom reference with a

null

queue, but such a reference is completely useless: Its

get

method will always return

null

and, since it does not have a queue,
it will never be enqueued.

**Parameters:**
- referent

- the object the new phantom reference will refer to
- q

- the queue with which the reference is to be registered,
or

null

if registration is not required

---

### Method Details

#### public
T
get()

Returns this reference object's referent. Because the referent of a
phantom reference is always inaccessible, this method always returns

null

.

**Overrides:**
- get

in class

Reference

<

T

>

**Returns:**
- null

---

### Additional Sections

#### Class PhantomReference<T>

java.lang.Object

- java.lang.ref.Reference

<T>
- - java.lang.ref.PhantomReference<T>

java.lang.ref.Reference

<T>

- java.lang.ref.PhantomReference<T>

java.lang.ref.PhantomReference<T>

```java
public class
PhantomReference<T>

extends
Reference
<T>
```

Phantom reference objects, which are enqueued after the collector
determines that their referents may otherwise be reclaimed. Phantom
references are most often used to schedule post-mortem cleanup actions.

Suppose the garbage collector determines at a certain point in time
that an object is

phantom reachable

. At that time it will atomically clear
all phantom references to that object and all phantom references to
any other phantom-reachable objects from which that object is reachable.
At the same time or at some later time it will enqueue those newly-cleared
phantom references that are registered with reference queues.

In order to ensure that a reclaimable object remains so, the referent of
a phantom reference may not be retrieved: The

get

method of a
phantom reference always returns

null

.

**Since:** 1.2

public class

PhantomReference<T>

extends

Reference

<T>

Phantom reference objects, which are enqueued after the collector
determines that their referents may otherwise be reclaimed. Phantom
references are most often used to schedule post-mortem cleanup actions.

Suppose the garbage collector determines at a certain point in time
that an object is

phantom reachable

. At that time it will atomically clear
all phantom references to that object and all phantom references to
any other phantom-reachable objects from which that object is reachable.
At the same time or at some later time it will enqueue those newly-cleared
phantom references that are registered with reference queues.

In order to ensure that a reclaimable object remains so, the referent of
a phantom reference may not be retrieved: The

get

method of a
phantom reference always returns

null

.

Suppose the garbage collector determines at a certain point in time
that an object is

phantom reachable

. At that time it will atomically clear
all phantom references to that object and all phantom references to
any other phantom-reachable objects from which that object is reachable.
At the same time or at some later time it will enqueue those newly-cleared
phantom references that are registered with reference queues.

In order to ensure that a reclaimable object remains so, the referent of
a phantom reference may not be retrieved: The

get

method of a
phantom reference always returns

null

.

In order to ensure that a reclaimable object remains so, the referent of
a phantom reference may not be retrieved: The

get

method of a
phantom reference always returns

null

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PhantomReference

​(

T

referent,

ReferenceQueue

<? super

T

> q)

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

T

get

()

Returns this reference object's referent.

- Methods declared in class java.lang.ref.

Reference

clear

,

clone

,

enqueue

,

isEnqueued

,

reachabilityFence

- Methods declared in class java.lang.

Object

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

Constructor Summary

Constructors

Constructor

Description

PhantomReference

​(

T

referent,

ReferenceQueue

<? super

T

> q)

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

---

#### Constructor Summary

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

T

get

()

Returns this reference object's referent.

- Methods declared in class java.lang.ref.

Reference

clear

,

clone

,

enqueue

,

isEnqueued

,

reachabilityFence

- Methods declared in class java.lang.

Object

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

#### Method Summary

Returns this reference object's referent.

Methods declared in class java.lang.ref.

Reference

clear

,

clone

,

enqueue

,

isEnqueued

,

reachabilityFence

---

#### Methods declared in class java.lang.ref. Reference

Methods declared in class java.lang.

Object

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PhantomReference

```java
public PhantomReference​(
T
referent,

ReferenceQueue
<? super
T
> q)
```

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

It is possible to create a phantom reference with a

null

queue, but such a reference is completely useless: Its

get

method will always return

null

and, since it does not have a queue,
it will never be enqueued.

**Parameters:** referent

- the object the new phantom reference will refer to
**Parameters:** q

- the queue with which the reference is to be registered,
or

null

if registration is not required

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public
T
get()
```

Returns this reference object's referent. Because the referent of a
phantom reference is always inaccessible, this method always returns

null

.

**Overrides:** get

in class

Reference

<

T

>
**Returns:** null

Constructor Detail

- PhantomReference

```java
public PhantomReference​(
T
referent,

ReferenceQueue
<? super
T
> q)
```

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

It is possible to create a phantom reference with a

null

queue, but such a reference is completely useless: Its

get

method will always return

null

and, since it does not have a queue,
it will never be enqueued.

**Parameters:** referent

- the object the new phantom reference will refer to
**Parameters:** q

- the queue with which the reference is to be registered,
or

null

if registration is not required

---

#### Constructor Detail

PhantomReference

```java
public PhantomReference​(
T
referent,

ReferenceQueue
<? super
T
> q)
```

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

It is possible to create a phantom reference with a

null

queue, but such a reference is completely useless: Its

get

method will always return

null

and, since it does not have a queue,
it will never be enqueued.

**Parameters:** referent

- the object the new phantom reference will refer to
**Parameters:** q

- the queue with which the reference is to be registered,
or

null

if registration is not required

---

#### PhantomReference

public PhantomReference​(

T

referent,

ReferenceQueue

<? super

T

> q)

Creates a new phantom reference that refers to the given object and
is registered with the given queue.

It is possible to create a phantom reference with a

null

queue, but such a reference is completely useless: Its

get

method will always return

null

and, since it does not have a queue,
it will never be enqueued.

It is possible to create a phantom reference with a

null

queue, but such a reference is completely useless: Its

get

method will always return

null

and, since it does not have a queue,
it will never be enqueued.

Method Detail

- get

```java
public
T
get()
```

Returns this reference object's referent. Because the referent of a
phantom reference is always inaccessible, this method always returns

null

.

**Overrides:** get

in class

Reference

<

T

>
**Returns:** null

---

#### Method Detail

get

```java
public
T
get()
```

Returns this reference object's referent. Because the referent of a
phantom reference is always inaccessible, this method always returns

null

.

**Overrides:** get

in class

Reference

<

T

>
**Returns:** null

---

#### get

public

T

get()

Returns this reference object's referent. Because the referent of a
phantom reference is always inaccessible, this method always returns

null

.

---

