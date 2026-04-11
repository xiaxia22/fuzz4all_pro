# Class ReentrantLock

**Source:** `java.base\java\util\concurrent\locks\ReentrantLock.html`

### Class Description

```java
public class
ReentrantLock

extends
Object

implements
Lock
,
Serializable
```

A reentrant mutual exclusion

Lock

with the same basic
behavior and semantics as the implicit monitor lock accessed using

synchronized

methods and statements, but with extended
capabilities.

A

ReentrantLock

is

owned

by the thread last
successfully locking, but not yet unlocking it. A thread invoking

lock

will return, successfully acquiring the lock, when
the lock is not owned by another thread. The method will return
immediately if the current thread already owns the lock. This can
be checked using methods

isHeldByCurrentThread()

, and

getHoldCount()

.

The constructor for this class accepts an optional

fairness

parameter. When set

true

, under
contention, locks favor granting access to the longest-waiting
thread. Otherwise this lock does not guarantee any particular
access order. Programs using fair locks accessed by many threads
may display lower overall throughput (i.e., are slower; often much
slower) than those using the default setting, but have smaller
variances in times to obtain locks and guarantee lack of
starvation. Note however, that fairness of locks does not guarantee
fairness of thread scheduling. Thus, one of many threads using a
fair lock may obtain it multiple times in succession while other
active threads are not progressing and not currently holding the
lock.
Also note that the untimed

tryLock()

method does not
honor the fairness setting. It will succeed if the lock
is available even if other threads are waiting.

It is recommended practice to

always

immediately
follow a call to

lock

with a

try

block, most
typically in a before/after construction such as:

```java
class X {
private final ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
lock.lock(); // block until condition holds
try {
// ... method body
} finally {
lock.unlock()
}
}
}
```

In addition to implementing the

Lock

interface, this
class defines a number of

public

and

protected

methods for inspecting the state of the lock. Some of these
methods are only useful for instrumentation and monitoring.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

**All Implemented Interfaces:** Serializable

,

Lock

---

### Field Details

*No entries found.*

### Constructor Details

#### public ReentrantLock()

Creates an instance of

ReentrantLock

.
This is equivalent to using

ReentrantLock(false)

.

---

#### public ReentrantLock​(boolean fair)

Creates an instance of

ReentrantLock

with the
given fairness policy.

**Parameters:**
- fair

-

true

if this lock should use a fair ordering policy

---

### Method Details

#### public void lock()

Acquires the lock.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

**Specified by:**
- lock

in interface

Lock

---

#### public void lockInterruptibly()
throws
InterruptedException

Acquires the lock unless the current thread is

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds this lock then the hold count
is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

**Specified by:**
- lockInterruptibly

in interface

Lock

**Throws:**
- InterruptedException

- if the current thread is interrupted

---

#### public boolean tryLock()

Acquires the lock only if it is not held by another thread at the time
of invocation.

Acquires the lock if it is not held by another thread and
returns immediately with the value

true

, setting the
lock hold count to one. Even when this lock has been set to use a
fair ordering policy, a call to

tryLock()

will

immediately acquire the lock if it is available, whether or not
other threads are currently waiting for the lock.
This "barging" behavior can be useful in certain
circumstances, even though it breaks fairness. If you want to honor
the fairness setting for this lock, then use

tryLock(0, TimeUnit.SECONDS)

which is almost equivalent (it also detects interruption).

If the current thread already holds this lock then the hold
count is incremented by one and the method returns

true

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

**Specified by:**
- tryLock

in interface

Lock

**Returns:**
- true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

otherwise

---

#### public boolean tryLock​(long timeout,

TimeUnit
unit)
throws
InterruptedException

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately with the value

true

, setting the lock hold count
to one. If this lock has been set to use a fair ordering policy then
an available lock

will not

be acquired if any other threads
are waiting for the lock. This is in contrast to the

tryLock()

method. If you want a timed

tryLock

that does permit barging on
a fair lock then combine the timed and un-timed forms together:

```java
if (lock.tryLock() ||
lock.tryLock(timeout, unit)) {
...
}
```

If the current thread
already holds this lock then the hold count is incremented by one and
the method returns

true

.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

**Specified by:**
- tryLock

in interface

Lock

**Parameters:**
- timeout

- the time to wait for the lock
- unit

- the time unit of the timeout argument

**Returns:**
- true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

if the waiting time elapsed before
the lock could be acquired

**Throws:**
- InterruptedException

- if the current thread is interrupted
- NullPointerException

- if the time unit is null

---

#### public void unlock()

Attempts to release this lock.

If the current thread is the holder of this lock then the hold
count is decremented. If the hold count is now zero then the lock
is released. If the current thread is not the holder of this
lock then

IllegalMonitorStateException

is thrown.

**Specified by:**
- unlock

in interface

Lock

**Throws:**
- IllegalMonitorStateException

- if the current thread does not
hold this lock

---

#### public
Condition
newCondition()

Returns a

Condition

instance for use with this

Lock

instance.

The returned

Condition

instance supports the same
usages as do the

Object

monitor methods (

wait

,

notify

, and

notifyAll

) when used with the built-in
monitor lock.

- If this lock is not held when any of the

Condition

waiting

or

signalling

methods are called, then an

IllegalMonitorStateException

is thrown.

When the condition

waiting

methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.

If a thread is

interrupted

while waiting then the wait will terminate, an

InterruptedException

will be thrown, and the thread's
interrupted status will be cleared.

Waiting threads are signalled in FIFO order.

The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for

fair

locks favors those threads that have been
waiting the longest.

**Specified by:**
- newCondition

in interface

Lock

**Returns:**
- the Condition object

---

#### public int getHoldCount()

Queries the number of holds on this lock by the current thread.

A thread has a hold on a lock for each lock action that is not
matched by an unlock action.

The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:**
- the number of holds on this lock by the current thread,
or zero if this lock is not held by the current thread

---

#### public boolean isHeldByCurrentThread()

Queries if this lock is held by the current thread.

Analogous to the

Thread.holdsLock(Object)

method for
built-in monitor locks, this method is typically used for
debugging and testing. For example, a method that should only be
called while a lock is held can assert that this is the case:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert lock.isHeldByCurrentThread();
// ... method body
}
}
```

It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:**
- true

if current thread holds this lock and

false

otherwise

---

#### public boolean isLocked()

Queries if this lock is held by any thread. This method is
designed for use in monitoring of the system state,
not for synchronization control.

**Returns:**
- true

if any thread holds this lock and

false

otherwise

---

#### public final boolean isFair()

Returns

true

if this lock has fairness set true.

**Returns:**
- true

if this lock has fairness set true

---

#### protected
Thread
getOwner()

Returns the thread that currently owns this lock, or

null

if not owned. When this method is called by a
thread that is not the owner, the return value reflects a
best-effort approximation of current lock status. For example,
the owner may be momentarily

null

even if there are
threads trying to acquire the lock but have not yet done so.
This method is designed to facilitate construction of
subclasses that provide more extensive lock monitoring
facilities.

**Returns:**
- the owner, or

null

if not owned

---

#### public final boolean hasQueuedThreads()

Queries whether any threads are waiting to acquire this lock. Note that
because cancellations may occur at any time, a

true

return does not guarantee that any other thread will ever
acquire this lock. This method is designed primarily for use in
monitoring of the system state.

**Returns:**
- true

if there may be other threads waiting to
acquire the lock

---

#### public final boolean hasQueuedThread​(
Thread
thread)

Queries whether the given thread is waiting to acquire this
lock. Note that because cancellations may occur at any time, a

true

return does not guarantee that this thread
will ever acquire this lock. This method is designed primarily for use
in monitoring of the system state.

**Parameters:**
- thread

- the thread

**Returns:**
- true

if the given thread is queued waiting for this lock

**Throws:**
- NullPointerException

- if the thread is null

---

#### public final int getQueueLength()

Returns an estimate of the number of threads waiting to acquire
this lock. The value is only an estimate because the number of
threads may change dynamically while this method traverses
internal data structures. This method is designed for use in
monitoring system state, not for synchronization control.

**Returns:**
- the estimated number of threads waiting for this lock

---

#### protected
Collection
<
Thread
> getQueuedThreads()

Returns a collection containing threads that may be waiting to
acquire this lock. Because the actual set of threads may change
dynamically while constructing this result, the returned
collection is only a best-effort estimate. The elements of the
returned collection are in no particular order. This method is
designed to facilitate construction of subclasses that provide
more extensive monitoring facilities.

**Returns:**
- the collection of threads

---

#### public boolean hasWaiters​(
Condition
condition)

Queries whether any threads are waiting on the given condition
associated with this lock. Note that because timeouts and
interrupts may occur at any time, a

true

return does
not guarantee that a future

signal

will awaken any
threads. This method is designed primarily for use in
monitoring of the system state.

**Parameters:**
- condition

- the condition

**Returns:**
- true

if there are any waiting threads

**Throws:**
- IllegalMonitorStateException

- if this lock is not held
- IllegalArgumentException

- if the given condition is
not associated with this lock
- NullPointerException

- if the condition is null

---

#### public int getWaitQueueLength​(
Condition
condition)

Returns an estimate of the number of threads waiting on the
given condition associated with this lock. Note that because
timeouts and interrupts may occur at any time, the estimate
serves only as an upper bound on the actual number of waiters.
This method is designed for use in monitoring of the system
state, not for synchronization control.

**Parameters:**
- condition

- the condition

**Returns:**
- the estimated number of waiting threads

**Throws:**
- IllegalMonitorStateException

- if this lock is not held
- IllegalArgumentException

- if the given condition is
not associated with this lock
- NullPointerException

- if the condition is null

---

#### protected
Collection
<
Thread
> getWaitingThreads​(
Condition
condition)

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.
Because the actual set of threads may change dynamically while
constructing this result, the returned collection is only a
best-effort estimate. The elements of the returned collection
are in no particular order. This method is designed to
facilitate construction of subclasses that provide more
extensive condition monitoring facilities.

**Parameters:**
- condition

- the condition

**Returns:**
- the collection of threads

**Throws:**
- IllegalMonitorStateException

- if this lock is not held
- IllegalArgumentException

- if the given condition is
not associated with this lock
- NullPointerException

- if the condition is null

---

#### public
String
toString()

Returns a string identifying this lock, as well as its lock state.
The state, in brackets, includes either the String

"Unlocked"

or the String

"Locked by"

followed by the

name

of the owning thread.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string identifying this lock, as well as its lock state

---

### Additional Sections

#### Class ReentrantLock

java.lang.Object

- java.util.concurrent.locks.ReentrantLock

java.util.concurrent.locks.ReentrantLock

**All Implemented Interfaces:** Serializable

,

Lock

```java
public class
ReentrantLock

extends
Object

implements
Lock
,
Serializable
```

A reentrant mutual exclusion

Lock

with the same basic
behavior and semantics as the implicit monitor lock accessed using

synchronized

methods and statements, but with extended
capabilities.

A

ReentrantLock

is

owned

by the thread last
successfully locking, but not yet unlocking it. A thread invoking

lock

will return, successfully acquiring the lock, when
the lock is not owned by another thread. The method will return
immediately if the current thread already owns the lock. This can
be checked using methods

isHeldByCurrentThread()

, and

getHoldCount()

.

The constructor for this class accepts an optional

fairness

parameter. When set

true

, under
contention, locks favor granting access to the longest-waiting
thread. Otherwise this lock does not guarantee any particular
access order. Programs using fair locks accessed by many threads
may display lower overall throughput (i.e., are slower; often much
slower) than those using the default setting, but have smaller
variances in times to obtain locks and guarantee lack of
starvation. Note however, that fairness of locks does not guarantee
fairness of thread scheduling. Thus, one of many threads using a
fair lock may obtain it multiple times in succession while other
active threads are not progressing and not currently holding the
lock.
Also note that the untimed

tryLock()

method does not
honor the fairness setting. It will succeed if the lock
is available even if other threads are waiting.

It is recommended practice to

always

immediately
follow a call to

lock

with a

try

block, most
typically in a before/after construction such as:

```java
class X {
private final ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
lock.lock(); // block until condition holds
try {
// ... method body
} finally {
lock.unlock()
}
}
}
```

In addition to implementing the

Lock

interface, this
class defines a number of

public

and

protected

methods for inspecting the state of the lock. Some of these
methods are only useful for instrumentation and monitoring.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

**Since:** 1.5
**See Also:** Serialized Form

public class

ReentrantLock

extends

Object

implements

Lock

,

Serializable

A reentrant mutual exclusion

Lock

with the same basic
behavior and semantics as the implicit monitor lock accessed using

synchronized

methods and statements, but with extended
capabilities.

A

ReentrantLock

is

owned

by the thread last
successfully locking, but not yet unlocking it. A thread invoking

lock

will return, successfully acquiring the lock, when
the lock is not owned by another thread. The method will return
immediately if the current thread already owns the lock. This can
be checked using methods

isHeldByCurrentThread()

, and

getHoldCount()

.

The constructor for this class accepts an optional

fairness

parameter. When set

true

, under
contention, locks favor granting access to the longest-waiting
thread. Otherwise this lock does not guarantee any particular
access order. Programs using fair locks accessed by many threads
may display lower overall throughput (i.e., are slower; often much
slower) than those using the default setting, but have smaller
variances in times to obtain locks and guarantee lack of
starvation. Note however, that fairness of locks does not guarantee
fairness of thread scheduling. Thus, one of many threads using a
fair lock may obtain it multiple times in succession while other
active threads are not progressing and not currently holding the
lock.
Also note that the untimed

tryLock()

method does not
honor the fairness setting. It will succeed if the lock
is available even if other threads are waiting.

It is recommended practice to

always

immediately
follow a call to

lock

with a

try

block, most
typically in a before/after construction such as:

```java
class X {
private final ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
lock.lock(); // block until condition holds
try {
// ... method body
} finally {
lock.unlock()
}
}
}
```

In addition to implementing the

Lock

interface, this
class defines a number of

public

and

protected

methods for inspecting the state of the lock. Some of these
methods are only useful for instrumentation and monitoring.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

A

ReentrantLock

is

owned

by the thread last
successfully locking, but not yet unlocking it. A thread invoking

lock

will return, successfully acquiring the lock, when
the lock is not owned by another thread. The method will return
immediately if the current thread already owns the lock. This can
be checked using methods

isHeldByCurrentThread()

, and

getHoldCount()

.

The constructor for this class accepts an optional

fairness

parameter. When set

true

, under
contention, locks favor granting access to the longest-waiting
thread. Otherwise this lock does not guarantee any particular
access order. Programs using fair locks accessed by many threads
may display lower overall throughput (i.e., are slower; often much
slower) than those using the default setting, but have smaller
variances in times to obtain locks and guarantee lack of
starvation. Note however, that fairness of locks does not guarantee
fairness of thread scheduling. Thus, one of many threads using a
fair lock may obtain it multiple times in succession while other
active threads are not progressing and not currently holding the
lock.
Also note that the untimed

tryLock()

method does not
honor the fairness setting. It will succeed if the lock
is available even if other threads are waiting.

It is recommended practice to

always

immediately
follow a call to

lock

with a

try

block, most
typically in a before/after construction such as:

```java
class X {
private final ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
lock.lock(); // block until condition holds
try {
// ... method body
} finally {
lock.unlock()
}
}
}
```

In addition to implementing the

Lock

interface, this
class defines a number of

public

and

protected

methods for inspecting the state of the lock. Some of these
methods are only useful for instrumentation and monitoring.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

The constructor for this class accepts an optional

fairness

parameter. When set

true

, under
contention, locks favor granting access to the longest-waiting
thread. Otherwise this lock does not guarantee any particular
access order. Programs using fair locks accessed by many threads
may display lower overall throughput (i.e., are slower; often much
slower) than those using the default setting, but have smaller
variances in times to obtain locks and guarantee lack of
starvation. Note however, that fairness of locks does not guarantee
fairness of thread scheduling. Thus, one of many threads using a
fair lock may obtain it multiple times in succession while other
active threads are not progressing and not currently holding the
lock.
Also note that the untimed

tryLock()

method does not
honor the fairness setting. It will succeed if the lock
is available even if other threads are waiting.

It is recommended practice to

always

immediately
follow a call to

lock

with a

try

block, most
typically in a before/after construction such as:

```java
class X {
private final ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
lock.lock(); // block until condition holds
try {
// ... method body
} finally {
lock.unlock()
}
}
}
```

In addition to implementing the

Lock

interface, this
class defines a number of

public

and

protected

methods for inspecting the state of the lock. Some of these
methods are only useful for instrumentation and monitoring.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

It is recommended practice to

always

immediately
follow a call to

lock

with a

try

block, most
typically in a before/after construction such as:

```java
class X {
private final ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
lock.lock(); // block until condition holds
try {
// ... method body
} finally {
lock.unlock()
}
}
}
```

In addition to implementing the

Lock

interface, this
class defines a number of

public

and

protected

methods for inspecting the state of the lock. Some of these
methods are only useful for instrumentation and monitoring.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

class X {
private final ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
lock.lock(); // block until condition holds
try {
// ... method body
} finally {
lock.unlock()
}
}
}

In addition to implementing the

Lock

interface, this
class defines a number of

public

and

protected

methods for inspecting the state of the lock. Some of these
methods are only useful for instrumentation and monitoring.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

Serialization of this class behaves in the same way as built-in
locks: a deserialized lock is in the unlocked state, regardless of
its state when serialized.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

This lock supports a maximum of 2147483647 recursive locks by
the same thread. Attempts to exceed this limit result in

Error

throws from locking methods.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ReentrantLock

()

Creates an instance of

ReentrantLock

.

ReentrantLock

​(boolean fair)

Creates an instance of

ReentrantLock

with the
given fairness policy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getHoldCount

()

Queries the number of holds on this lock by the current thread.

protected

Thread

getOwner

()

Returns the thread that currently owns this lock, or

null

if not owned.

protected

Collection

<

Thread

>

getQueuedThreads

()

Returns a collection containing threads that may be waiting to
acquire this lock.

int

getQueueLength

()

Returns an estimate of the number of threads waiting to acquire
this lock.

protected

Collection

<

Thread

>

getWaitingThreads

​(

Condition

condition)

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.

int

getWaitQueueLength

​(

Condition

condition)

Returns an estimate of the number of threads waiting on the
given condition associated with this lock.

boolean

hasQueuedThread

​(

Thread

thread)

Queries whether the given thread is waiting to acquire this
lock.

boolean

hasQueuedThreads

()

Queries whether any threads are waiting to acquire this lock.

boolean

hasWaiters

​(

Condition

condition)

Queries whether any threads are waiting on the given condition
associated with this lock.

boolean

isFair

()

Returns

true

if this lock has fairness set true.

boolean

isHeldByCurrentThread

()

Queries if this lock is held by the current thread.

boolean

isLocked

()

Queries if this lock is held by any thread.

void

lock

()

Acquires the lock.

void

lockInterruptibly

()

Acquires the lock unless the current thread is

interrupted

.

Condition

newCondition

()

Returns a

Condition

instance for use with this

Lock

instance.

String

toString

()

Returns a string identifying this lock, as well as its lock state.

boolean

tryLock

()

Acquires the lock only if it is not held by another thread at the time
of invocation.

boolean

tryLock

​(long timeout,

TimeUnit

unit)

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

void

unlock

()

Attempts to release this lock.

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

Constructor Summary

Constructors

Constructor

Description

ReentrantLock

()

Creates an instance of

ReentrantLock

.

ReentrantLock

​(boolean fair)

Creates an instance of

ReentrantLock

with the
given fairness policy.

---

#### Constructor Summary

Creates an instance of

ReentrantLock

.

Creates an instance of

ReentrantLock

with the
given fairness policy.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getHoldCount

()

Queries the number of holds on this lock by the current thread.

protected

Thread

getOwner

()

Returns the thread that currently owns this lock, or

null

if not owned.

protected

Collection

<

Thread

>

getQueuedThreads

()

Returns a collection containing threads that may be waiting to
acquire this lock.

int

getQueueLength

()

Returns an estimate of the number of threads waiting to acquire
this lock.

protected

Collection

<

Thread

>

getWaitingThreads

​(

Condition

condition)

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.

int

getWaitQueueLength

​(

Condition

condition)

Returns an estimate of the number of threads waiting on the
given condition associated with this lock.

boolean

hasQueuedThread

​(

Thread

thread)

Queries whether the given thread is waiting to acquire this
lock.

boolean

hasQueuedThreads

()

Queries whether any threads are waiting to acquire this lock.

boolean

hasWaiters

​(

Condition

condition)

Queries whether any threads are waiting on the given condition
associated with this lock.

boolean

isFair

()

Returns

true

if this lock has fairness set true.

boolean

isHeldByCurrentThread

()

Queries if this lock is held by the current thread.

boolean

isLocked

()

Queries if this lock is held by any thread.

void

lock

()

Acquires the lock.

void

lockInterruptibly

()

Acquires the lock unless the current thread is

interrupted

.

Condition

newCondition

()

Returns a

Condition

instance for use with this

Lock

instance.

String

toString

()

Returns a string identifying this lock, as well as its lock state.

boolean

tryLock

()

Acquires the lock only if it is not held by another thread at the time
of invocation.

boolean

tryLock

​(long timeout,

TimeUnit

unit)

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

void

unlock

()

Attempts to release this lock.

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

---

#### Method Summary

Queries the number of holds on this lock by the current thread.

Returns the thread that currently owns this lock, or

null

if not owned.

Returns a collection containing threads that may be waiting to
acquire this lock.

Returns an estimate of the number of threads waiting to acquire
this lock.

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.

Returns an estimate of the number of threads waiting on the
given condition associated with this lock.

Queries whether the given thread is waiting to acquire this
lock.

Queries whether any threads are waiting to acquire this lock.

Queries whether any threads are waiting on the given condition
associated with this lock.

Returns

true

if this lock has fairness set true.

Queries if this lock is held by the current thread.

Queries if this lock is held by any thread.

Acquires the lock.

Acquires the lock unless the current thread is

interrupted

.

Returns a

Condition

instance for use with this

Lock

instance.

Returns a string identifying this lock, as well as its lock state.

Acquires the lock only if it is not held by another thread at the time
of invocation.

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

Attempts to release this lock.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ReentrantLock

```java
public ReentrantLock()
```

Creates an instance of

ReentrantLock

.
This is equivalent to using

ReentrantLock(false)

.

- ReentrantLock

```java
public ReentrantLock​(boolean fair)
```

Creates an instance of

ReentrantLock

with the
given fairness policy.

**Parameters:** fair

-

true

if this lock should use a fair ordering policy

============ METHOD DETAIL ==========

- Method Detail

- lock

```java
public void lock()
```

Acquires the lock.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

**Specified by:** lock

in interface

Lock

- lockInterruptibly

```java
public void lockInterruptibly()
throws
InterruptedException
```

Acquires the lock unless the current thread is

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds this lock then the hold count
is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

**Specified by:** lockInterruptibly

in interface

Lock
**Throws:** InterruptedException

- if the current thread is interrupted

- tryLock

```java
public boolean tryLock()
```

Acquires the lock only if it is not held by another thread at the time
of invocation.

Acquires the lock if it is not held by another thread and
returns immediately with the value

true

, setting the
lock hold count to one. Even when this lock has been set to use a
fair ordering policy, a call to

tryLock()

will

immediately acquire the lock if it is available, whether or not
other threads are currently waiting for the lock.
This "barging" behavior can be useful in certain
circumstances, even though it breaks fairness. If you want to honor
the fairness setting for this lock, then use

tryLock(0, TimeUnit.SECONDS)

which is almost equivalent (it also detects interruption).

If the current thread already holds this lock then the hold
count is incremented by one and the method returns

true

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

**Specified by:** tryLock

in interface

Lock
**Returns:** true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

otherwise

- tryLock

```java
public boolean tryLock​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately with the value

true

, setting the lock hold count
to one. If this lock has been set to use a fair ordering policy then
an available lock

will not

be acquired if any other threads
are waiting for the lock. This is in contrast to the

tryLock()

method. If you want a timed

tryLock

that does permit barging on
a fair lock then combine the timed and un-timed forms together:

```java
if (lock.tryLock() ||
lock.tryLock(timeout, unit)) {
...
}
```

If the current thread
already holds this lock then the hold count is incremented by one and
the method returns

true

.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

**Specified by:** tryLock

in interface

Lock
**Parameters:** timeout

- the time to wait for the lock
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

if the waiting time elapsed before
the lock could be acquired
**Throws:** InterruptedException

- if the current thread is interrupted
**Throws:** NullPointerException

- if the time unit is null

- unlock

```java
public void unlock()
```

Attempts to release this lock.

If the current thread is the holder of this lock then the hold
count is decremented. If the hold count is now zero then the lock
is released. If the current thread is not the holder of this
lock then

IllegalMonitorStateException

is thrown.

**Specified by:** unlock

in interface

Lock
**Throws:** IllegalMonitorStateException

- if the current thread does not
hold this lock

- newCondition

```java
public
Condition
newCondition()
```

Returns a

Condition

instance for use with this

Lock

instance.

The returned

Condition

instance supports the same
usages as do the

Object

monitor methods (

wait

,

notify

, and

notifyAll

) when used with the built-in
monitor lock.

- If this lock is not held when any of the

Condition

waiting

or

signalling

methods are called, then an

IllegalMonitorStateException

is thrown.

When the condition

waiting

methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.

If a thread is

interrupted

while waiting then the wait will terminate, an

InterruptedException

will be thrown, and the thread's
interrupted status will be cleared.

Waiting threads are signalled in FIFO order.

The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for

fair

locks favors those threads that have been
waiting the longest.

**Specified by:** newCondition

in interface

Lock
**Returns:** the Condition object

- getHoldCount

```java
public int getHoldCount()
```

Queries the number of holds on this lock by the current thread.

A thread has a hold on a lock for each lock action that is not
matched by an unlock action.

The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:** the number of holds on this lock by the current thread,
or zero if this lock is not held by the current thread

- isHeldByCurrentThread

```java
public boolean isHeldByCurrentThread()
```

Queries if this lock is held by the current thread.

Analogous to the

Thread.holdsLock(Object)

method for
built-in monitor locks, this method is typically used for
debugging and testing. For example, a method that should only be
called while a lock is held can assert that this is the case:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert lock.isHeldByCurrentThread();
// ... method body
}
}
```

It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:** true

if current thread holds this lock and

false

otherwise

- isLocked

```java
public boolean isLocked()
```

Queries if this lock is held by any thread. This method is
designed for use in monitoring of the system state,
not for synchronization control.

**Returns:** true

if any thread holds this lock and

false

otherwise

- isFair

```java
public final boolean isFair()
```

Returns

true

if this lock has fairness set true.

**Returns:** true

if this lock has fairness set true

- getOwner

```java
protected
Thread
getOwner()
```

Returns the thread that currently owns this lock, or

null

if not owned. When this method is called by a
thread that is not the owner, the return value reflects a
best-effort approximation of current lock status. For example,
the owner may be momentarily

null

even if there are
threads trying to acquire the lock but have not yet done so.
This method is designed to facilitate construction of
subclasses that provide more extensive lock monitoring
facilities.

**Returns:** the owner, or

null

if not owned

- hasQueuedThreads

```java
public final boolean hasQueuedThreads()
```

Queries whether any threads are waiting to acquire this lock. Note that
because cancellations may occur at any time, a

true

return does not guarantee that any other thread will ever
acquire this lock. This method is designed primarily for use in
monitoring of the system state.

**Returns:** true

if there may be other threads waiting to
acquire the lock

- hasQueuedThread

```java
public final boolean hasQueuedThread​(
Thread
thread)
```

Queries whether the given thread is waiting to acquire this
lock. Note that because cancellations may occur at any time, a

true

return does not guarantee that this thread
will ever acquire this lock. This method is designed primarily for use
in monitoring of the system state.

**Parameters:** thread

- the thread
**Returns:** true

if the given thread is queued waiting for this lock
**Throws:** NullPointerException

- if the thread is null

- getQueueLength

```java
public final int getQueueLength()
```

Returns an estimate of the number of threads waiting to acquire
this lock. The value is only an estimate because the number of
threads may change dynamically while this method traverses
internal data structures. This method is designed for use in
monitoring system state, not for synchronization control.

**Returns:** the estimated number of threads waiting for this lock

- getQueuedThreads

```java
protected
Collection
<
Thread
> getQueuedThreads()
```

Returns a collection containing threads that may be waiting to
acquire this lock. Because the actual set of threads may change
dynamically while constructing this result, the returned
collection is only a best-effort estimate. The elements of the
returned collection are in no particular order. This method is
designed to facilitate construction of subclasses that provide
more extensive monitoring facilities.

**Returns:** the collection of threads

- hasWaiters

```java
public boolean hasWaiters​(
Condition
condition)
```

Queries whether any threads are waiting on the given condition
associated with this lock. Note that because timeouts and
interrupts may occur at any time, a

true

return does
not guarantee that a future

signal

will awaken any
threads. This method is designed primarily for use in
monitoring of the system state.

**Parameters:** condition

- the condition
**Returns:** true

if there are any waiting threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

- getWaitQueueLength

```java
public int getWaitQueueLength​(
Condition
condition)
```

Returns an estimate of the number of threads waiting on the
given condition associated with this lock. Note that because
timeouts and interrupts may occur at any time, the estimate
serves only as an upper bound on the actual number of waiters.
This method is designed for use in monitoring of the system
state, not for synchronization control.

**Parameters:** condition

- the condition
**Returns:** the estimated number of waiting threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

- getWaitingThreads

```java
protected
Collection
<
Thread
> getWaitingThreads​(
Condition
condition)
```

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.
Because the actual set of threads may change dynamically while
constructing this result, the returned collection is only a
best-effort estimate. The elements of the returned collection
are in no particular order. This method is designed to
facilitate construction of subclasses that provide more
extensive condition monitoring facilities.

**Parameters:** condition

- the condition
**Returns:** the collection of threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

- toString

```java
public
String
toString()
```

Returns a string identifying this lock, as well as its lock state.
The state, in brackets, includes either the String

"Unlocked"

or the String

"Locked by"

followed by the

name

of the owning thread.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this lock, as well as its lock state

Constructor Detail

- ReentrantLock

```java
public ReentrantLock()
```

Creates an instance of

ReentrantLock

.
This is equivalent to using

ReentrantLock(false)

.

- ReentrantLock

```java
public ReentrantLock​(boolean fair)
```

Creates an instance of

ReentrantLock

with the
given fairness policy.

**Parameters:** fair

-

true

if this lock should use a fair ordering policy

---

#### Constructor Detail

ReentrantLock

```java
public ReentrantLock()
```

Creates an instance of

ReentrantLock

.
This is equivalent to using

ReentrantLock(false)

.

---

#### ReentrantLock

public ReentrantLock()

Creates an instance of

ReentrantLock

.
This is equivalent to using

ReentrantLock(false)

.

ReentrantLock

```java
public ReentrantLock​(boolean fair)
```

Creates an instance of

ReentrantLock

with the
given fairness policy.

**Parameters:** fair

-

true

if this lock should use a fair ordering policy

---

#### ReentrantLock

public ReentrantLock​(boolean fair)

Creates an instance of

ReentrantLock

with the
given fairness policy.

Method Detail

- lock

```java
public void lock()
```

Acquires the lock.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

**Specified by:** lock

in interface

Lock

- lockInterruptibly

```java
public void lockInterruptibly()
throws
InterruptedException
```

Acquires the lock unless the current thread is

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds this lock then the hold count
is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

**Specified by:** lockInterruptibly

in interface

Lock
**Throws:** InterruptedException

- if the current thread is interrupted

- tryLock

```java
public boolean tryLock()
```

Acquires the lock only if it is not held by another thread at the time
of invocation.

Acquires the lock if it is not held by another thread and
returns immediately with the value

true

, setting the
lock hold count to one. Even when this lock has been set to use a
fair ordering policy, a call to

tryLock()

will

immediately acquire the lock if it is available, whether or not
other threads are currently waiting for the lock.
This "barging" behavior can be useful in certain
circumstances, even though it breaks fairness. If you want to honor
the fairness setting for this lock, then use

tryLock(0, TimeUnit.SECONDS)

which is almost equivalent (it also detects interruption).

If the current thread already holds this lock then the hold
count is incremented by one and the method returns

true

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

**Specified by:** tryLock

in interface

Lock
**Returns:** true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

otherwise

- tryLock

```java
public boolean tryLock​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately with the value

true

, setting the lock hold count
to one. If this lock has been set to use a fair ordering policy then
an available lock

will not

be acquired if any other threads
are waiting for the lock. This is in contrast to the

tryLock()

method. If you want a timed

tryLock

that does permit barging on
a fair lock then combine the timed and un-timed forms together:

```java
if (lock.tryLock() ||
lock.tryLock(timeout, unit)) {
...
}
```

If the current thread
already holds this lock then the hold count is incremented by one and
the method returns

true

.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

**Specified by:** tryLock

in interface

Lock
**Parameters:** timeout

- the time to wait for the lock
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

if the waiting time elapsed before
the lock could be acquired
**Throws:** InterruptedException

- if the current thread is interrupted
**Throws:** NullPointerException

- if the time unit is null

- unlock

```java
public void unlock()
```

Attempts to release this lock.

If the current thread is the holder of this lock then the hold
count is decremented. If the hold count is now zero then the lock
is released. If the current thread is not the holder of this
lock then

IllegalMonitorStateException

is thrown.

**Specified by:** unlock

in interface

Lock
**Throws:** IllegalMonitorStateException

- if the current thread does not
hold this lock

- newCondition

```java
public
Condition
newCondition()
```

Returns a

Condition

instance for use with this

Lock

instance.

The returned

Condition

instance supports the same
usages as do the

Object

monitor methods (

wait

,

notify

, and

notifyAll

) when used with the built-in
monitor lock.

- If this lock is not held when any of the

Condition

waiting

or

signalling

methods are called, then an

IllegalMonitorStateException

is thrown.

When the condition

waiting

methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.

If a thread is

interrupted

while waiting then the wait will terminate, an

InterruptedException

will be thrown, and the thread's
interrupted status will be cleared.

Waiting threads are signalled in FIFO order.

The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for

fair

locks favors those threads that have been
waiting the longest.

**Specified by:** newCondition

in interface

Lock
**Returns:** the Condition object

- getHoldCount

```java
public int getHoldCount()
```

Queries the number of holds on this lock by the current thread.

A thread has a hold on a lock for each lock action that is not
matched by an unlock action.

The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:** the number of holds on this lock by the current thread,
or zero if this lock is not held by the current thread

- isHeldByCurrentThread

```java
public boolean isHeldByCurrentThread()
```

Queries if this lock is held by the current thread.

Analogous to the

Thread.holdsLock(Object)

method for
built-in monitor locks, this method is typically used for
debugging and testing. For example, a method that should only be
called while a lock is held can assert that this is the case:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert lock.isHeldByCurrentThread();
// ... method body
}
}
```

It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:** true

if current thread holds this lock and

false

otherwise

- isLocked

```java
public boolean isLocked()
```

Queries if this lock is held by any thread. This method is
designed for use in monitoring of the system state,
not for synchronization control.

**Returns:** true

if any thread holds this lock and

false

otherwise

- isFair

```java
public final boolean isFair()
```

Returns

true

if this lock has fairness set true.

**Returns:** true

if this lock has fairness set true

- getOwner

```java
protected
Thread
getOwner()
```

Returns the thread that currently owns this lock, or

null

if not owned. When this method is called by a
thread that is not the owner, the return value reflects a
best-effort approximation of current lock status. For example,
the owner may be momentarily

null

even if there are
threads trying to acquire the lock but have not yet done so.
This method is designed to facilitate construction of
subclasses that provide more extensive lock monitoring
facilities.

**Returns:** the owner, or

null

if not owned

- hasQueuedThreads

```java
public final boolean hasQueuedThreads()
```

Queries whether any threads are waiting to acquire this lock. Note that
because cancellations may occur at any time, a

true

return does not guarantee that any other thread will ever
acquire this lock. This method is designed primarily for use in
monitoring of the system state.

**Returns:** true

if there may be other threads waiting to
acquire the lock

- hasQueuedThread

```java
public final boolean hasQueuedThread​(
Thread
thread)
```

Queries whether the given thread is waiting to acquire this
lock. Note that because cancellations may occur at any time, a

true

return does not guarantee that this thread
will ever acquire this lock. This method is designed primarily for use
in monitoring of the system state.

**Parameters:** thread

- the thread
**Returns:** true

if the given thread is queued waiting for this lock
**Throws:** NullPointerException

- if the thread is null

- getQueueLength

```java
public final int getQueueLength()
```

Returns an estimate of the number of threads waiting to acquire
this lock. The value is only an estimate because the number of
threads may change dynamically while this method traverses
internal data structures. This method is designed for use in
monitoring system state, not for synchronization control.

**Returns:** the estimated number of threads waiting for this lock

- getQueuedThreads

```java
protected
Collection
<
Thread
> getQueuedThreads()
```

Returns a collection containing threads that may be waiting to
acquire this lock. Because the actual set of threads may change
dynamically while constructing this result, the returned
collection is only a best-effort estimate. The elements of the
returned collection are in no particular order. This method is
designed to facilitate construction of subclasses that provide
more extensive monitoring facilities.

**Returns:** the collection of threads

- hasWaiters

```java
public boolean hasWaiters​(
Condition
condition)
```

Queries whether any threads are waiting on the given condition
associated with this lock. Note that because timeouts and
interrupts may occur at any time, a

true

return does
not guarantee that a future

signal

will awaken any
threads. This method is designed primarily for use in
monitoring of the system state.

**Parameters:** condition

- the condition
**Returns:** true

if there are any waiting threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

- getWaitQueueLength

```java
public int getWaitQueueLength​(
Condition
condition)
```

Returns an estimate of the number of threads waiting on the
given condition associated with this lock. Note that because
timeouts and interrupts may occur at any time, the estimate
serves only as an upper bound on the actual number of waiters.
This method is designed for use in monitoring of the system
state, not for synchronization control.

**Parameters:** condition

- the condition
**Returns:** the estimated number of waiting threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

- getWaitingThreads

```java
protected
Collection
<
Thread
> getWaitingThreads​(
Condition
condition)
```

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.
Because the actual set of threads may change dynamically while
constructing this result, the returned collection is only a
best-effort estimate. The elements of the returned collection
are in no particular order. This method is designed to
facilitate construction of subclasses that provide more
extensive condition monitoring facilities.

**Parameters:** condition

- the condition
**Returns:** the collection of threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

- toString

```java
public
String
toString()
```

Returns a string identifying this lock, as well as its lock state.
The state, in brackets, includes either the String

"Unlocked"

or the String

"Locked by"

followed by the

name

of the owning thread.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this lock, as well as its lock state

---

#### Method Detail

lock

```java
public void lock()
```

Acquires the lock.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

**Specified by:** lock

in interface

Lock

---

#### lock

public void lock()

Acquires the lock.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.

lockInterruptibly

```java
public void lockInterruptibly()
throws
InterruptedException
```

Acquires the lock unless the current thread is

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds this lock then the hold count
is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

**Specified by:** lockInterruptibly

in interface

Lock
**Throws:** InterruptedException

- if the current thread is interrupted

---

#### lockInterruptibly

public void lockInterruptibly()
throws

InterruptedException

Acquires the lock unless the current thread is

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds this lock then the hold count
is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.

If the current thread already holds this lock then the hold count
is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

If the current thread already holds this lock then the hold count
is incremented by one and the method returns immediately.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

The lock is acquired by the current thread; or

Some other thread

interrupts

the
current thread.

If the lock is acquired by the current thread then the lock hold
count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

has its interrupted status set on entry to this method; or

is

interrupted

while acquiring
the lock,

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock.

tryLock

```java
public boolean tryLock()
```

Acquires the lock only if it is not held by another thread at the time
of invocation.

Acquires the lock if it is not held by another thread and
returns immediately with the value

true

, setting the
lock hold count to one. Even when this lock has been set to use a
fair ordering policy, a call to

tryLock()

will

immediately acquire the lock if it is available, whether or not
other threads are currently waiting for the lock.
This "barging" behavior can be useful in certain
circumstances, even though it breaks fairness. If you want to honor
the fairness setting for this lock, then use

tryLock(0, TimeUnit.SECONDS)

which is almost equivalent (it also detects interruption).

If the current thread already holds this lock then the hold
count is incremented by one and the method returns

true

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

**Specified by:** tryLock

in interface

Lock
**Returns:** true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

otherwise

---

#### tryLock

public boolean tryLock()

Acquires the lock only if it is not held by another thread at the time
of invocation.

Acquires the lock if it is not held by another thread and
returns immediately with the value

true

, setting the
lock hold count to one. Even when this lock has been set to use a
fair ordering policy, a call to

tryLock()

will

immediately acquire the lock if it is available, whether or not
other threads are currently waiting for the lock.
This "barging" behavior can be useful in certain
circumstances, even though it breaks fairness. If you want to honor
the fairness setting for this lock, then use

tryLock(0, TimeUnit.SECONDS)

which is almost equivalent (it also detects interruption).

If the current thread already holds this lock then the hold
count is incremented by one and the method returns

true

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

Acquires the lock if it is not held by another thread and
returns immediately with the value

true

, setting the
lock hold count to one. Even when this lock has been set to use a
fair ordering policy, a call to

tryLock()

will

immediately acquire the lock if it is available, whether or not
other threads are currently waiting for the lock.
This "barging" behavior can be useful in certain
circumstances, even though it breaks fairness. If you want to honor
the fairness setting for this lock, then use

tryLock(0, TimeUnit.SECONDS)

which is almost equivalent (it also detects interruption).

If the current thread already holds this lock then the hold
count is incremented by one and the method returns

true

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

If the current thread already holds this lock then the hold
count is incremented by one and the method returns

true

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

If the lock is held by another thread then this method will return
immediately with the value

false

.

tryLock

```java
public boolean tryLock​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately with the value

true

, setting the lock hold count
to one. If this lock has been set to use a fair ordering policy then
an available lock

will not

be acquired if any other threads
are waiting for the lock. This is in contrast to the

tryLock()

method. If you want a timed

tryLock

that does permit barging on
a fair lock then combine the timed and un-timed forms together:

```java
if (lock.tryLock() ||
lock.tryLock(timeout, unit)) {
...
}
```

If the current thread
already holds this lock then the hold count is incremented by one and
the method returns

true

.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

**Specified by:** tryLock

in interface

Lock
**Parameters:** timeout

- the time to wait for the lock
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if the lock was free and was acquired by the
current thread, or the lock was already held by the current
thread; and

false

if the waiting time elapsed before
the lock could be acquired
**Throws:** InterruptedException

- if the current thread is interrupted
**Throws:** NullPointerException

- if the time unit is null

---

#### tryLock

public boolean tryLock​(long timeout,

TimeUnit

unit)
throws

InterruptedException

Acquires the lock if it is not held by another thread within the given
waiting time and the current thread has not been

interrupted

.

Acquires the lock if it is not held by another thread and returns
immediately with the value

true

, setting the lock hold count
to one. If this lock has been set to use a fair ordering policy then
an available lock

will not

be acquired if any other threads
are waiting for the lock. This is in contrast to the

tryLock()

method. If you want a timed

tryLock

that does permit barging on
a fair lock then combine the timed and un-timed forms together:

```java
if (lock.tryLock() ||
lock.tryLock(timeout, unit)) {
...
}
```

If the current thread
already holds this lock then the hold count is incremented by one and
the method returns

true

.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

Acquires the lock if it is not held by another thread and returns
immediately with the value

true

, setting the lock hold count
to one. If this lock has been set to use a fair ordering policy then
an available lock

will not

be acquired if any other threads
are waiting for the lock. This is in contrast to the

tryLock()

method. If you want a timed

tryLock

that does permit barging on
a fair lock then combine the timed and un-timed forms together:

```java
if (lock.tryLock() ||
lock.tryLock(timeout, unit)) {
...
}
```

If the current thread
already holds this lock then the hold count is incremented by one and
the method returns

true

.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

if (lock.tryLock() ||
lock.tryLock(timeout, unit)) {
...
}

If the current thread
already holds this lock then the hold count is incremented by one and
the method returns

true

.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:

- The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

The lock is acquired by the current thread; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses

If the lock is acquired then the value

true

is returned and
the lock hold count is set to one.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

has its interrupted status set on entry to this method; or

is

interrupted

while
acquiring the lock,

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

In this implementation, as this method is an explicit
interruption point, preference is given to responding to the
interrupt over normal or reentrant acquisition of the lock, and
over reporting the elapse of the waiting time.

unlock

```java
public void unlock()
```

Attempts to release this lock.

If the current thread is the holder of this lock then the hold
count is decremented. If the hold count is now zero then the lock
is released. If the current thread is not the holder of this
lock then

IllegalMonitorStateException

is thrown.

**Specified by:** unlock

in interface

Lock
**Throws:** IllegalMonitorStateException

- if the current thread does not
hold this lock

---

#### unlock

public void unlock()

Attempts to release this lock.

If the current thread is the holder of this lock then the hold
count is decremented. If the hold count is now zero then the lock
is released. If the current thread is not the holder of this
lock then

IllegalMonitorStateException

is thrown.

If the current thread is the holder of this lock then the hold
count is decremented. If the hold count is now zero then the lock
is released. If the current thread is not the holder of this
lock then

IllegalMonitorStateException

is thrown.

newCondition

```java
public
Condition
newCondition()
```

Returns a

Condition

instance for use with this

Lock

instance.

The returned

Condition

instance supports the same
usages as do the

Object

monitor methods (

wait

,

notify

, and

notifyAll

) when used with the built-in
monitor lock.

- If this lock is not held when any of the

Condition

waiting

or

signalling

methods are called, then an

IllegalMonitorStateException

is thrown.

When the condition

waiting

methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.

If a thread is

interrupted

while waiting then the wait will terminate, an

InterruptedException

will be thrown, and the thread's
interrupted status will be cleared.

Waiting threads are signalled in FIFO order.

The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for

fair

locks favors those threads that have been
waiting the longest.

**Specified by:** newCondition

in interface

Lock
**Returns:** the Condition object

---

#### newCondition

public

Condition

newCondition()

Returns a

Condition

instance for use with this

Lock

instance.

The returned

Condition

instance supports the same
usages as do the

Object

monitor methods (

wait

,

notify

, and

notifyAll

) when used with the built-in
monitor lock.

- If this lock is not held when any of the

Condition

waiting

or

signalling

methods are called, then an

IllegalMonitorStateException

is thrown.

When the condition

waiting

methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.

If a thread is

interrupted

while waiting then the wait will terminate, an

InterruptedException

will be thrown, and the thread's
interrupted status will be cleared.

Waiting threads are signalled in FIFO order.

The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for

fair

locks favors those threads that have been
waiting the longest.

The returned

Condition

instance supports the same
usages as do the

Object

monitor methods (

wait

,

notify

, and

notifyAll

) when used with the built-in
monitor lock.

- If this lock is not held when any of the

Condition

waiting

or

signalling

methods are called, then an

IllegalMonitorStateException

is thrown.

When the condition

waiting

methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.

If a thread is

interrupted

while waiting then the wait will terminate, an

InterruptedException

will be thrown, and the thread's
interrupted status will be cleared.

Waiting threads are signalled in FIFO order.

The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for

fair

locks favors those threads that have been
waiting the longest.

If this lock is not held when any of the

Condition

waiting

or

signalling

methods are called, then an

IllegalMonitorStateException

is thrown.

When the condition

waiting

methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.

If a thread is

interrupted

while waiting then the wait will terminate, an

InterruptedException

will be thrown, and the thread's
interrupted status will be cleared.

Waiting threads are signalled in FIFO order.

The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for

fair

locks favors those threads that have been
waiting the longest.

getHoldCount

```java
public int getHoldCount()
```

Queries the number of holds on this lock by the current thread.

A thread has a hold on a lock for each lock action that is not
matched by an unlock action.

The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:** the number of holds on this lock by the current thread,
or zero if this lock is not held by the current thread

---

#### getHoldCount

public int getHoldCount()

Queries the number of holds on this lock by the current thread.

A thread has a hold on a lock for each lock action that is not
matched by an unlock action.

The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

A thread has a hold on a lock for each lock action that is not
matched by an unlock action.

The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

class X {
ReentrantLock lock = new ReentrantLock();
// ...
public void m() {
assert lock.getHoldCount() == 0;
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}

isHeldByCurrentThread

```java
public boolean isHeldByCurrentThread()
```

Queries if this lock is held by the current thread.

Analogous to the

Thread.holdsLock(Object)

method for
built-in monitor locks, this method is typically used for
debugging and testing. For example, a method that should only be
called while a lock is held can assert that this is the case:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert lock.isHeldByCurrentThread();
// ... method body
}
}
```

It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

**Returns:** true

if current thread holds this lock and

false

otherwise

---

#### isHeldByCurrentThread

public boolean isHeldByCurrentThread()

Queries if this lock is held by the current thread.

Analogous to the

Thread.holdsLock(Object)

method for
built-in monitor locks, this method is typically used for
debugging and testing. For example, a method that should only be
called while a lock is held can assert that this is the case:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert lock.isHeldByCurrentThread();
// ... method body
}
}
```

It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

Analogous to the

Thread.holdsLock(Object)

method for
built-in monitor locks, this method is typically used for
debugging and testing. For example, a method that should only be
called while a lock is held can assert that this is the case:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert lock.isHeldByCurrentThread();
// ... method body
}
}
```

It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert lock.isHeldByCurrentThread();
// ... method body
}
}

It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:

```java
class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}
```

class X {
ReentrantLock lock = new ReentrantLock();
// ...

public void m() {
assert !lock.isHeldByCurrentThread();
lock.lock();
try {
// ... method body
} finally {
lock.unlock();
}
}
}

isLocked

```java
public boolean isLocked()
```

Queries if this lock is held by any thread. This method is
designed for use in monitoring of the system state,
not for synchronization control.

**Returns:** true

if any thread holds this lock and

false

otherwise

---

#### isLocked

public boolean isLocked()

Queries if this lock is held by any thread. This method is
designed for use in monitoring of the system state,
not for synchronization control.

isFair

```java
public final boolean isFair()
```

Returns

true

if this lock has fairness set true.

**Returns:** true

if this lock has fairness set true

---

#### isFair

public final boolean isFair()

Returns

true

if this lock has fairness set true.

getOwner

```java
protected
Thread
getOwner()
```

Returns the thread that currently owns this lock, or

null

if not owned. When this method is called by a
thread that is not the owner, the return value reflects a
best-effort approximation of current lock status. For example,
the owner may be momentarily

null

even if there are
threads trying to acquire the lock but have not yet done so.
This method is designed to facilitate construction of
subclasses that provide more extensive lock monitoring
facilities.

**Returns:** the owner, or

null

if not owned

---

#### getOwner

protected

Thread

getOwner()

Returns the thread that currently owns this lock, or

null

if not owned. When this method is called by a
thread that is not the owner, the return value reflects a
best-effort approximation of current lock status. For example,
the owner may be momentarily

null

even if there are
threads trying to acquire the lock but have not yet done so.
This method is designed to facilitate construction of
subclasses that provide more extensive lock monitoring
facilities.

hasQueuedThreads

```java
public final boolean hasQueuedThreads()
```

Queries whether any threads are waiting to acquire this lock. Note that
because cancellations may occur at any time, a

true

return does not guarantee that any other thread will ever
acquire this lock. This method is designed primarily for use in
monitoring of the system state.

**Returns:** true

if there may be other threads waiting to
acquire the lock

---

#### hasQueuedThreads

public final boolean hasQueuedThreads()

Queries whether any threads are waiting to acquire this lock. Note that
because cancellations may occur at any time, a

true

return does not guarantee that any other thread will ever
acquire this lock. This method is designed primarily for use in
monitoring of the system state.

hasQueuedThread

```java
public final boolean hasQueuedThread​(
Thread
thread)
```

Queries whether the given thread is waiting to acquire this
lock. Note that because cancellations may occur at any time, a

true

return does not guarantee that this thread
will ever acquire this lock. This method is designed primarily for use
in monitoring of the system state.

**Parameters:** thread

- the thread
**Returns:** true

if the given thread is queued waiting for this lock
**Throws:** NullPointerException

- if the thread is null

---

#### hasQueuedThread

public final boolean hasQueuedThread​(

Thread

thread)

Queries whether the given thread is waiting to acquire this
lock. Note that because cancellations may occur at any time, a

true

return does not guarantee that this thread
will ever acquire this lock. This method is designed primarily for use
in monitoring of the system state.

getQueueLength

```java
public final int getQueueLength()
```

Returns an estimate of the number of threads waiting to acquire
this lock. The value is only an estimate because the number of
threads may change dynamically while this method traverses
internal data structures. This method is designed for use in
monitoring system state, not for synchronization control.

**Returns:** the estimated number of threads waiting for this lock

---

#### getQueueLength

public final int getQueueLength()

Returns an estimate of the number of threads waiting to acquire
this lock. The value is only an estimate because the number of
threads may change dynamically while this method traverses
internal data structures. This method is designed for use in
monitoring system state, not for synchronization control.

getQueuedThreads

```java
protected
Collection
<
Thread
> getQueuedThreads()
```

Returns a collection containing threads that may be waiting to
acquire this lock. Because the actual set of threads may change
dynamically while constructing this result, the returned
collection is only a best-effort estimate. The elements of the
returned collection are in no particular order. This method is
designed to facilitate construction of subclasses that provide
more extensive monitoring facilities.

**Returns:** the collection of threads

---

#### getQueuedThreads

protected

Collection

<

Thread

> getQueuedThreads()

Returns a collection containing threads that may be waiting to
acquire this lock. Because the actual set of threads may change
dynamically while constructing this result, the returned
collection is only a best-effort estimate. The elements of the
returned collection are in no particular order. This method is
designed to facilitate construction of subclasses that provide
more extensive monitoring facilities.

hasWaiters

```java
public boolean hasWaiters​(
Condition
condition)
```

Queries whether any threads are waiting on the given condition
associated with this lock. Note that because timeouts and
interrupts may occur at any time, a

true

return does
not guarantee that a future

signal

will awaken any
threads. This method is designed primarily for use in
monitoring of the system state.

**Parameters:** condition

- the condition
**Returns:** true

if there are any waiting threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

---

#### hasWaiters

public boolean hasWaiters​(

Condition

condition)

Queries whether any threads are waiting on the given condition
associated with this lock. Note that because timeouts and
interrupts may occur at any time, a

true

return does
not guarantee that a future

signal

will awaken any
threads. This method is designed primarily for use in
monitoring of the system state.

getWaitQueueLength

```java
public int getWaitQueueLength​(
Condition
condition)
```

Returns an estimate of the number of threads waiting on the
given condition associated with this lock. Note that because
timeouts and interrupts may occur at any time, the estimate
serves only as an upper bound on the actual number of waiters.
This method is designed for use in monitoring of the system
state, not for synchronization control.

**Parameters:** condition

- the condition
**Returns:** the estimated number of waiting threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

---

#### getWaitQueueLength

public int getWaitQueueLength​(

Condition

condition)

Returns an estimate of the number of threads waiting on the
given condition associated with this lock. Note that because
timeouts and interrupts may occur at any time, the estimate
serves only as an upper bound on the actual number of waiters.
This method is designed for use in monitoring of the system
state, not for synchronization control.

getWaitingThreads

```java
protected
Collection
<
Thread
> getWaitingThreads​(
Condition
condition)
```

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.
Because the actual set of threads may change dynamically while
constructing this result, the returned collection is only a
best-effort estimate. The elements of the returned collection
are in no particular order. This method is designed to
facilitate construction of subclasses that provide more
extensive condition monitoring facilities.

**Parameters:** condition

- the condition
**Returns:** the collection of threads
**Throws:** IllegalMonitorStateException

- if this lock is not held
**Throws:** IllegalArgumentException

- if the given condition is
not associated with this lock
**Throws:** NullPointerException

- if the condition is null

---

#### getWaitingThreads

protected

Collection

<

Thread

> getWaitingThreads​(

Condition

condition)

Returns a collection containing those threads that may be
waiting on the given condition associated with this lock.
Because the actual set of threads may change dynamically while
constructing this result, the returned collection is only a
best-effort estimate. The elements of the returned collection
are in no particular order. This method is designed to
facilitate construction of subclasses that provide more
extensive condition monitoring facilities.

toString

```java
public
String
toString()
```

Returns a string identifying this lock, as well as its lock state.
The state, in brackets, includes either the String

"Unlocked"

or the String

"Locked by"

followed by the

name

of the owning thread.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this lock, as well as its lock state

---

#### toString

public

String

toString()

Returns a string identifying this lock, as well as its lock state.
The state, in brackets, includes either the String

"Unlocked"

or the String

"Locked by"

followed by the

name

of the owning thread.

---

