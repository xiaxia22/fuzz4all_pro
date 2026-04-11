# Class WeakReference<T>

**Source:** `java.base\java\lang\ref\WeakReference.html`

### Class Description

```java
public class
WeakReference<T>

extends
Reference
<T>
```

Weak reference objects, which do not prevent their referents from being
made finalizable, finalized, and then reclaimed. Weak references are most
often used to implement canonicalizing mappings.

Suppose that the garbage collector determines at a certain point in time
that an object is

weakly
reachable

. At that time it will atomically clear all weak references to
that object and all weak references to any other weakly-reachable objects
from which that object is reachable through a chain of strong and soft
references. At the same time it will declare all of the formerly
weakly-reachable objects to be finalizable. At the same time or at some
later time it will enqueue those newly-cleared weak references that are
registered with reference queues.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

#### public WeakReference​(
T
referent)

Creates a new weak reference that refers to the given object. The new
reference is not registered with any queue.

**Parameters:**
- referent

- object the new weak reference will refer to

---

#### public WeakReference​(
T
referent,

ReferenceQueue
<? super
T
> q)

Creates a new weak reference that refers to the given object and is
registered with the given queue.

**Parameters:**
- referent

- object the new weak reference will refer to
- q

- the queue with which the reference is to be registered,
or

null

if registration is not required

---

### Method Details

*No entries found.*

### Additional Sections

#### Class WeakReference<T>

java.lang.Object

- java.lang.ref.Reference

<T>
- - java.lang.ref.WeakReference<T>

java.lang.ref.Reference

<T>

- java.lang.ref.WeakReference<T>

java.lang.ref.WeakReference<T>

```java
public class
WeakReference<T>

extends
Reference
<T>
```

Weak reference objects, which do not prevent their referents from being
made finalizable, finalized, and then reclaimed. Weak references are most
often used to implement canonicalizing mappings.

Suppose that the garbage collector determines at a certain point in time
that an object is

weakly
reachable

. At that time it will atomically clear all weak references to
that object and all weak references to any other weakly-reachable objects
from which that object is reachable through a chain of strong and soft
references. At the same time it will declare all of the formerly
weakly-reachable objects to be finalizable. At the same time or at some
later time it will enqueue those newly-cleared weak references that are
registered with reference queues.

**Since:** 1.2

public class

WeakReference<T>

extends

Reference

<T>

Weak reference objects, which do not prevent their referents from being
made finalizable, finalized, and then reclaimed. Weak references are most
often used to implement canonicalizing mappings.

Suppose that the garbage collector determines at a certain point in time
that an object is

weakly
reachable

. At that time it will atomically clear all weak references to
that object and all weak references to any other weakly-reachable objects
from which that object is reachable through a chain of strong and soft
references. At the same time it will declare all of the formerly
weakly-reachable objects to be finalizable. At the same time or at some
later time it will enqueue those newly-cleared weak references that are
registered with reference queues.

Suppose that the garbage collector determines at a certain point in time
that an object is

weakly
reachable

. At that time it will atomically clear all weak references to
that object and all weak references to any other weakly-reachable objects
from which that object is reachable through a chain of strong and soft
references. At the same time it will declare all of the formerly
weakly-reachable objects to be finalizable. At the same time or at some
later time it will enqueue those newly-cleared weak references that are
registered with reference queues.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

WeakReference

​(

T

referent)

Creates a new weak reference that refers to the given object.

WeakReference

​(

T

referent,

ReferenceQueue

<? super

T

> q)

Creates a new weak reference that refers to the given object and is
registered with the given queue.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.ref.

Reference

clear

,

clone

,

enqueue

,

get

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

WeakReference

​(

T

referent)

Creates a new weak reference that refers to the given object.

WeakReference

​(

T

referent,

ReferenceQueue

<? super

T

> q)

Creates a new weak reference that refers to the given object and is
registered with the given queue.

---

#### Constructor Summary

Creates a new weak reference that refers to the given object.

Creates a new weak reference that refers to the given object and is
registered with the given queue.

Method Summary

- Methods declared in class java.lang.ref.

Reference

clear

,

clone

,

enqueue

,

get

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

Methods declared in class java.lang.ref.

Reference

clear

,

clone

,

enqueue

,

get

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

- WeakReference

```java
public WeakReference​(
T
referent)
```

Creates a new weak reference that refers to the given object. The new
reference is not registered with any queue.

**Parameters:** referent

- object the new weak reference will refer to

- WeakReference

```java
public WeakReference​(
T
referent,

ReferenceQueue
<? super
T
> q)
```

Creates a new weak reference that refers to the given object and is
registered with the given queue.

**Parameters:** referent

- object the new weak reference will refer to
**Parameters:** q

- the queue with which the reference is to be registered,
or

null

if registration is not required

Constructor Detail

- WeakReference

```java
public WeakReference​(
T
referent)
```

Creates a new weak reference that refers to the given object. The new
reference is not registered with any queue.

**Parameters:** referent

- object the new weak reference will refer to

- WeakReference

```java
public WeakReference​(
T
referent,

ReferenceQueue
<? super
T
> q)
```

Creates a new weak reference that refers to the given object and is
registered with the given queue.

**Parameters:** referent

- object the new weak reference will refer to
**Parameters:** q

- the queue with which the reference is to be registered,
or

null

if registration is not required

---

#### Constructor Detail

WeakReference

```java
public WeakReference​(
T
referent)
```

Creates a new weak reference that refers to the given object. The new
reference is not registered with any queue.

**Parameters:** referent

- object the new weak reference will refer to

---

#### WeakReference

public WeakReference​(

T

referent)

Creates a new weak reference that refers to the given object. The new
reference is not registered with any queue.

WeakReference

```java
public WeakReference​(
T
referent,

ReferenceQueue
<? super
T
> q)
```

Creates a new weak reference that refers to the given object and is
registered with the given queue.

**Parameters:** referent

- object the new weak reference will refer to
**Parameters:** q

- the queue with which the reference is to be registered,
or

null

if registration is not required

---

#### WeakReference

public WeakReference​(

T

referent,

ReferenceQueue

<? super

T

> q)

Creates a new weak reference that refers to the given object and is
registered with the given queue.

---

