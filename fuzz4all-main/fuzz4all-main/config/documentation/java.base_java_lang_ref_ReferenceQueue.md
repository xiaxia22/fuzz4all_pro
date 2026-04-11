# Class ReferenceQueue<T>

**Source:** `java.base\java\lang\ref\ReferenceQueue.html`

### Class Description

```java
public class
ReferenceQueue<T>

extends
Object
```

Reference queues, to which registered reference objects are appended by the
garbage collector after the appropriate reachability changes are detected.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

#### public ReferenceQueue()

Constructs a new reference-object queue.

---

### Method Details

#### public
Reference
<? extends
T
> poll()

Polls this queue to see if a reference object is available. If one is
available without further delay then it is removed from the queue and
returned. Otherwise this method immediately returns

null

.

**Returns:**
- A reference object, if one was immediately available,
otherwise

null

---

#### public
Reference
<? extends
T
> remove​(long timeout)
throws
IllegalArgumentException
,

InterruptedException

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

This method does not offer real-time guarantees: It schedules the
timeout as if by invoking the

Object.wait(long)

method.

**Parameters:**
- timeout

- If positive, block for up to

timeout

milliseconds while waiting for a reference to be
added to this queue. If zero, block indefinitely.

**Returns:**
- A reference object, if one was available within the specified
timeout period, otherwise

null

**Throws:**
- IllegalArgumentException

- If the value of the timeout argument is negative
- InterruptedException

- If the timeout wait is interrupted

---

#### public
Reference
<? extends
T
> remove()
throws
InterruptedException

Removes the next reference object in this queue, blocking until one
becomes available.

**Returns:**
- A reference object, blocking until one becomes available

**Throws:**
- InterruptedException

- If the wait is interrupted

---

### Additional Sections

#### Class ReferenceQueue<T>

java.lang.Object

- java.lang.ref.ReferenceQueue<T>

java.lang.ref.ReferenceQueue<T>

```java
public class
ReferenceQueue<T>

extends
Object
```

Reference queues, to which registered reference objects are appended by the
garbage collector after the appropriate reachability changes are detected.

**Since:** 1.2

public class

ReferenceQueue<T>

extends

Object

Reference queues, to which registered reference objects are appended by the
garbage collector after the appropriate reachability changes are detected.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ReferenceQueue

()

Constructs a new reference-object queue.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Reference

<? extends

T

>

poll

()

Polls this queue to see if a reference object is available.

Reference

<? extends

T

>

remove

()

Removes the next reference object in this queue, blocking until one
becomes available.

Reference

<? extends

T

>

remove

​(long timeout)

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

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

ReferenceQueue

()

Constructs a new reference-object queue.

---

#### Constructor Summary

Constructs a new reference-object queue.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Reference

<? extends

T

>

poll

()

Polls this queue to see if a reference object is available.

Reference

<? extends

T

>

remove

()

Removes the next reference object in this queue, blocking until one
becomes available.

Reference

<? extends

T

>

remove

​(long timeout)

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Polls this queue to see if a reference object is available.

Removes the next reference object in this queue, blocking until one
becomes available.

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

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

- ReferenceQueue

```java
public ReferenceQueue()
```

Constructs a new reference-object queue.

============ METHOD DETAIL ==========

- Method Detail

- poll

```java
public
Reference
<? extends
T
> poll()
```

Polls this queue to see if a reference object is available. If one is
available without further delay then it is removed from the queue and
returned. Otherwise this method immediately returns

null

.

**Returns:** A reference object, if one was immediately available,
otherwise

null

- remove

```java
public
Reference
<? extends
T
> remove​(long timeout)
throws
IllegalArgumentException
,

InterruptedException
```

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

This method does not offer real-time guarantees: It schedules the
timeout as if by invoking the

Object.wait(long)

method.

**Parameters:** timeout

- If positive, block for up to

timeout

milliseconds while waiting for a reference to be
added to this queue. If zero, block indefinitely.
**Returns:** A reference object, if one was available within the specified
timeout period, otherwise

null
**Throws:** IllegalArgumentException

- If the value of the timeout argument is negative
**Throws:** InterruptedException

- If the timeout wait is interrupted

- remove

```java
public
Reference
<? extends
T
> remove()
throws
InterruptedException
```

Removes the next reference object in this queue, blocking until one
becomes available.

**Returns:** A reference object, blocking until one becomes available
**Throws:** InterruptedException

- If the wait is interrupted

Constructor Detail

- ReferenceQueue

```java
public ReferenceQueue()
```

Constructs a new reference-object queue.

---

#### Constructor Detail

ReferenceQueue

```java
public ReferenceQueue()
```

Constructs a new reference-object queue.

---

#### ReferenceQueue

public ReferenceQueue()

Constructs a new reference-object queue.

Method Detail

- poll

```java
public
Reference
<? extends
T
> poll()
```

Polls this queue to see if a reference object is available. If one is
available without further delay then it is removed from the queue and
returned. Otherwise this method immediately returns

null

.

**Returns:** A reference object, if one was immediately available,
otherwise

null

- remove

```java
public
Reference
<? extends
T
> remove​(long timeout)
throws
IllegalArgumentException
,

InterruptedException
```

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

This method does not offer real-time guarantees: It schedules the
timeout as if by invoking the

Object.wait(long)

method.

**Parameters:** timeout

- If positive, block for up to

timeout

milliseconds while waiting for a reference to be
added to this queue. If zero, block indefinitely.
**Returns:** A reference object, if one was available within the specified
timeout period, otherwise

null
**Throws:** IllegalArgumentException

- If the value of the timeout argument is negative
**Throws:** InterruptedException

- If the timeout wait is interrupted

- remove

```java
public
Reference
<? extends
T
> remove()
throws
InterruptedException
```

Removes the next reference object in this queue, blocking until one
becomes available.

**Returns:** A reference object, blocking until one becomes available
**Throws:** InterruptedException

- If the wait is interrupted

---

#### Method Detail

poll

```java
public
Reference
<? extends
T
> poll()
```

Polls this queue to see if a reference object is available. If one is
available without further delay then it is removed from the queue and
returned. Otherwise this method immediately returns

null

.

**Returns:** A reference object, if one was immediately available,
otherwise

null

---

#### poll

public

Reference

<? extends

T

> poll()

Polls this queue to see if a reference object is available. If one is
available without further delay then it is removed from the queue and
returned. Otherwise this method immediately returns

null

.

remove

```java
public
Reference
<? extends
T
> remove​(long timeout)
throws
IllegalArgumentException
,

InterruptedException
```

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

This method does not offer real-time guarantees: It schedules the
timeout as if by invoking the

Object.wait(long)

method.

**Parameters:** timeout

- If positive, block for up to

timeout

milliseconds while waiting for a reference to be
added to this queue. If zero, block indefinitely.
**Returns:** A reference object, if one was available within the specified
timeout period, otherwise

null
**Throws:** IllegalArgumentException

- If the value of the timeout argument is negative
**Throws:** InterruptedException

- If the timeout wait is interrupted

---

#### remove

public

Reference

<? extends

T

> remove​(long timeout)
throws

IllegalArgumentException

,

InterruptedException

Removes the next reference object in this queue, blocking until either
one becomes available or the given timeout period expires.

This method does not offer real-time guarantees: It schedules the
timeout as if by invoking the

Object.wait(long)

method.

This method does not offer real-time guarantees: It schedules the
timeout as if by invoking the

Object.wait(long)

method.

remove

```java
public
Reference
<? extends
T
> remove()
throws
InterruptedException
```

Removes the next reference object in this queue, blocking until one
becomes available.

**Returns:** A reference object, blocking until one becomes available
**Throws:** InterruptedException

- If the wait is interrupted

---

#### remove

public

Reference

<? extends

T

> remove()
throws

InterruptedException

Removes the next reference object in this queue, blocking until one
becomes available.

---

