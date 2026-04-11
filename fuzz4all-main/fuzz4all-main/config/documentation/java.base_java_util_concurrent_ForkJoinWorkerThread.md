# Class ForkJoinWorkerThread

**Source:** `java.base\java\util\concurrent\ForkJoinWorkerThread.html`

### Class Description

```java
public class
ForkJoinWorkerThread

extends
Thread
```

A thread managed by a

ForkJoinPool

, which executes

ForkJoinTask

s.
This class is subclassable solely for the sake of adding
functionality -- there are no overridable methods dealing with
scheduling or execution. However, you can override initialization
and termination methods surrounding the main task processing loop.
If you do create such a subclass, you will also need to supply a
custom

ForkJoinPool.ForkJoinWorkerThreadFactory

to

use it

in a

ForkJoinPool

.

**All Implemented Interfaces:** Runnable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ForkJoinWorkerThread​(
ForkJoinPool
pool)

Creates a ForkJoinWorkerThread operating in the given pool.

**Parameters:**
- pool

- the pool this thread works in

**Throws:**
- NullPointerException

- if pool is null

---

### Method Details

#### public
ForkJoinPool
getPool()

Returns the pool hosting this thread.

**Returns:**
- the pool

---

#### public int getPoolIndex()

Returns the unique index number of this thread in its pool.
The returned value ranges from zero to the maximum number of
threads (minus one) that may exist in the pool, and does not
change during the lifetime of the thread. This method may be
useful for applications that track status or collect results
per-worker-thread rather than per-task.

**Returns:**
- the index number

---

#### protected void onStart()

Initializes internal state after construction but before
processing any tasks. If you override this method, you must
invoke

super.onStart()

at the beginning of the method.
Initialization requires care: Most fields must have legal
default values, to ensure that attempted accesses from other
threads work correctly even before this thread starts
processing tasks.

---

#### protected void onTermination​(
Throwable
exception)

Performs cleanup associated with termination of this worker
thread. If you override this method, you must invoke

super.onTermination

at the end of the overridden method.

**Parameters:**
- exception

- the exception causing this thread to abort due
to an unrecoverable error, or

null

if completed normally

---

#### public void run()

This method is required to be public, but should never be
called explicitly. It performs the main run loop to execute

ForkJoinTask

s.

**Specified by:**
- run

in interface

Runnable

**Overrides:**
- run

in class

Thread

**See Also:**
- Thread.start()

,

Thread.stop()

,

Thread(ThreadGroup, Runnable, String)

---

### Additional Sections

#### Class ForkJoinWorkerThread

java.lang.Object

- java.lang.Thread
- - java.util.concurrent.ForkJoinWorkerThread

java.lang.Thread

- java.util.concurrent.ForkJoinWorkerThread

java.util.concurrent.ForkJoinWorkerThread

**All Implemented Interfaces:** Runnable

```java
public class
ForkJoinWorkerThread

extends
Thread
```

A thread managed by a

ForkJoinPool

, which executes

ForkJoinTask

s.
This class is subclassable solely for the sake of adding
functionality -- there are no overridable methods dealing with
scheduling or execution. However, you can override initialization
and termination methods surrounding the main task processing loop.
If you do create such a subclass, you will also need to supply a
custom

ForkJoinPool.ForkJoinWorkerThreadFactory

to

use it

in a

ForkJoinPool

.

**Since:** 1.7

public class

ForkJoinWorkerThread

extends

Thread

A thread managed by a

ForkJoinPool

, which executes

ForkJoinTask

s.
This class is subclassable solely for the sake of adding
functionality -- there are no overridable methods dealing with
scheduling or execution. However, you can override initialization
and termination methods surrounding the main task processing loop.
If you do create such a subclass, you will also need to supply a
custom

ForkJoinPool.ForkJoinWorkerThreadFactory

to

use it

in a

ForkJoinPool

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.lang.

Thread

Thread.State

,

Thread.UncaughtExceptionHandler

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.lang.

Thread

MAX_PRIORITY

,

MIN_PRIORITY

,

NORM_PRIORITY

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForkJoinWorkerThread

​(

ForkJoinPool

pool)

Creates a ForkJoinWorkerThread operating in the given pool.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ForkJoinPool

getPool

()

Returns the pool hosting this thread.

int

getPoolIndex

()

Returns the unique index number of this thread in its pool.

protected void

onStart

()

Initializes internal state after construction but before
processing any tasks.

protected void

onTermination

​(

Throwable

exception)

Performs cleanup associated with termination of this worker
thread.

void

run

()

This method is required to be public, but should never be
called explicitly.

- Methods declared in class java.lang.

Thread

activeCount

,

checkAccess

,

clone

,

countStackFrames

,

currentThread

,

dumpStack

,

enumerate

,

getAllStackTraces

,

getContextClassLoader

,

getDefaultUncaughtExceptionHandler

,

getId

,

getName

,

getPriority

,

getStackTrace

,

getState

,

getThreadGroup

,

getUncaughtExceptionHandler

,

holdsLock

,

interrupt

,

interrupted

,

isAlive

,

isDaemon

,

isInterrupted

,

join

,

join

,

join

,

onSpinWait

,

resume

,

setContextClassLoader

,

setDaemon

,

setDefaultUncaughtExceptionHandler

,

setName

,

setPriority

,

setUncaughtExceptionHandler

,

sleep

,

sleep

,

start

,

stop

,

suspend

,

toString

,

yield

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

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class java.lang.

Thread

Thread.State

,

Thread.UncaughtExceptionHandler

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.lang.

Thread

Thread.State

,

Thread.UncaughtExceptionHandler

---

#### Nested classes/interfaces declared in class java.lang. Thread

Field Summary

- Fields declared in class java.lang.

Thread

MAX_PRIORITY

,

MIN_PRIORITY

,

NORM_PRIORITY

---

#### Field Summary

Fields declared in class java.lang.

Thread

MAX_PRIORITY

,

MIN_PRIORITY

,

NORM_PRIORITY

---

#### Fields declared in class java.lang. Thread

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForkJoinWorkerThread

​(

ForkJoinPool

pool)

Creates a ForkJoinWorkerThread operating in the given pool.

---

#### Constructor Summary

Creates a ForkJoinWorkerThread operating in the given pool.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ForkJoinPool

getPool

()

Returns the pool hosting this thread.

int

getPoolIndex

()

Returns the unique index number of this thread in its pool.

protected void

onStart

()

Initializes internal state after construction but before
processing any tasks.

protected void

onTermination

​(

Throwable

exception)

Performs cleanup associated with termination of this worker
thread.

void

run

()

This method is required to be public, but should never be
called explicitly.

- Methods declared in class java.lang.

Thread

activeCount

,

checkAccess

,

clone

,

countStackFrames

,

currentThread

,

dumpStack

,

enumerate

,

getAllStackTraces

,

getContextClassLoader

,

getDefaultUncaughtExceptionHandler

,

getId

,

getName

,

getPriority

,

getStackTrace

,

getState

,

getThreadGroup

,

getUncaughtExceptionHandler

,

holdsLock

,

interrupt

,

interrupted

,

isAlive

,

isDaemon

,

isInterrupted

,

join

,

join

,

join

,

onSpinWait

,

resume

,

setContextClassLoader

,

setDaemon

,

setDefaultUncaughtExceptionHandler

,

setName

,

setPriority

,

setUncaughtExceptionHandler

,

sleep

,

sleep

,

start

,

stop

,

suspend

,

toString

,

yield

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the pool hosting this thread.

Returns the unique index number of this thread in its pool.

Initializes internal state after construction but before
processing any tasks.

Performs cleanup associated with termination of this worker
thread.

This method is required to be public, but should never be
called explicitly.

Methods declared in class java.lang.

Thread

activeCount

,

checkAccess

,

clone

,

countStackFrames

,

currentThread

,

dumpStack

,

enumerate

,

getAllStackTraces

,

getContextClassLoader

,

getDefaultUncaughtExceptionHandler

,

getId

,

getName

,

getPriority

,

getStackTrace

,

getState

,

getThreadGroup

,

getUncaughtExceptionHandler

,

holdsLock

,

interrupt

,

interrupted

,

isAlive

,

isDaemon

,

isInterrupted

,

join

,

join

,

join

,

onSpinWait

,

resume

,

setContextClassLoader

,

setDaemon

,

setDefaultUncaughtExceptionHandler

,

setName

,

setPriority

,

setUncaughtExceptionHandler

,

sleep

,

sleep

,

start

,

stop

,

suspend

,

toString

,

yield

---

#### Methods declared in class java.lang. Thread

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ForkJoinWorkerThread

```java
protected ForkJoinWorkerThread​(
ForkJoinPool
pool)
```

Creates a ForkJoinWorkerThread operating in the given pool.

**Parameters:** pool

- the pool this thread works in
**Throws:** NullPointerException

- if pool is null

============ METHOD DETAIL ==========

- Method Detail

- getPool

```java
public
ForkJoinPool
getPool()
```

Returns the pool hosting this thread.

**Returns:** the pool

- getPoolIndex

```java
public int getPoolIndex()
```

Returns the unique index number of this thread in its pool.
The returned value ranges from zero to the maximum number of
threads (minus one) that may exist in the pool, and does not
change during the lifetime of the thread. This method may be
useful for applications that track status or collect results
per-worker-thread rather than per-task.

**Returns:** the index number

- onStart

```java
protected void onStart()
```

Initializes internal state after construction but before
processing any tasks. If you override this method, you must
invoke

super.onStart()

at the beginning of the method.
Initialization requires care: Most fields must have legal
default values, to ensure that attempted accesses from other
threads work correctly even before this thread starts
processing tasks.

- onTermination

```java
protected void onTermination​(
Throwable
exception)
```

Performs cleanup associated with termination of this worker
thread. If you override this method, you must invoke

super.onTermination

at the end of the overridden method.

**Parameters:** exception

- the exception causing this thread to abort due
to an unrecoverable error, or

null

if completed normally

- run

```java
public void run()
```

This method is required to be public, but should never be
called explicitly. It performs the main run loop to execute

ForkJoinTask

s.

**Specified by:** run

in interface

Runnable
**Overrides:** run

in class

Thread
**See Also:** Thread.start()

,

Thread.stop()

,

Thread(ThreadGroup, Runnable, String)

Constructor Detail

- ForkJoinWorkerThread

```java
protected ForkJoinWorkerThread​(
ForkJoinPool
pool)
```

Creates a ForkJoinWorkerThread operating in the given pool.

**Parameters:** pool

- the pool this thread works in
**Throws:** NullPointerException

- if pool is null

---

#### Constructor Detail

ForkJoinWorkerThread

```java
protected ForkJoinWorkerThread​(
ForkJoinPool
pool)
```

Creates a ForkJoinWorkerThread operating in the given pool.

**Parameters:** pool

- the pool this thread works in
**Throws:** NullPointerException

- if pool is null

---

#### ForkJoinWorkerThread

protected ForkJoinWorkerThread​(

ForkJoinPool

pool)

Creates a ForkJoinWorkerThread operating in the given pool.

Method Detail

- getPool

```java
public
ForkJoinPool
getPool()
```

Returns the pool hosting this thread.

**Returns:** the pool

- getPoolIndex

```java
public int getPoolIndex()
```

Returns the unique index number of this thread in its pool.
The returned value ranges from zero to the maximum number of
threads (minus one) that may exist in the pool, and does not
change during the lifetime of the thread. This method may be
useful for applications that track status or collect results
per-worker-thread rather than per-task.

**Returns:** the index number

- onStart

```java
protected void onStart()
```

Initializes internal state after construction but before
processing any tasks. If you override this method, you must
invoke

super.onStart()

at the beginning of the method.
Initialization requires care: Most fields must have legal
default values, to ensure that attempted accesses from other
threads work correctly even before this thread starts
processing tasks.

- onTermination

```java
protected void onTermination​(
Throwable
exception)
```

Performs cleanup associated with termination of this worker
thread. If you override this method, you must invoke

super.onTermination

at the end of the overridden method.

**Parameters:** exception

- the exception causing this thread to abort due
to an unrecoverable error, or

null

if completed normally

- run

```java
public void run()
```

This method is required to be public, but should never be
called explicitly. It performs the main run loop to execute

ForkJoinTask

s.

**Specified by:** run

in interface

Runnable
**Overrides:** run

in class

Thread
**See Also:** Thread.start()

,

Thread.stop()

,

Thread(ThreadGroup, Runnable, String)

---

#### Method Detail

getPool

```java
public
ForkJoinPool
getPool()
```

Returns the pool hosting this thread.

**Returns:** the pool

---

#### getPool

public

ForkJoinPool

getPool()

Returns the pool hosting this thread.

getPoolIndex

```java
public int getPoolIndex()
```

Returns the unique index number of this thread in its pool.
The returned value ranges from zero to the maximum number of
threads (minus one) that may exist in the pool, and does not
change during the lifetime of the thread. This method may be
useful for applications that track status or collect results
per-worker-thread rather than per-task.

**Returns:** the index number

---

#### getPoolIndex

public int getPoolIndex()

Returns the unique index number of this thread in its pool.
The returned value ranges from zero to the maximum number of
threads (minus one) that may exist in the pool, and does not
change during the lifetime of the thread. This method may be
useful for applications that track status or collect results
per-worker-thread rather than per-task.

onStart

```java
protected void onStart()
```

Initializes internal state after construction but before
processing any tasks. If you override this method, you must
invoke

super.onStart()

at the beginning of the method.
Initialization requires care: Most fields must have legal
default values, to ensure that attempted accesses from other
threads work correctly even before this thread starts
processing tasks.

---

#### onStart

protected void onStart()

Initializes internal state after construction but before
processing any tasks. If you override this method, you must
invoke

super.onStart()

at the beginning of the method.
Initialization requires care: Most fields must have legal
default values, to ensure that attempted accesses from other
threads work correctly even before this thread starts
processing tasks.

onTermination

```java
protected void onTermination​(
Throwable
exception)
```

Performs cleanup associated with termination of this worker
thread. If you override this method, you must invoke

super.onTermination

at the end of the overridden method.

**Parameters:** exception

- the exception causing this thread to abort due
to an unrecoverable error, or

null

if completed normally

---

#### onTermination

protected void onTermination​(

Throwable

exception)

Performs cleanup associated with termination of this worker
thread. If you override this method, you must invoke

super.onTermination

at the end of the overridden method.

run

```java
public void run()
```

This method is required to be public, but should never be
called explicitly. It performs the main run loop to execute

ForkJoinTask

s.

**Specified by:** run

in interface

Runnable
**Overrides:** run

in class

Thread
**See Also:** Thread.start()

,

Thread.stop()

,

Thread(ThreadGroup, Runnable, String)

---

#### run

public void run()

This method is required to be public, but should never be
called explicitly. It performs the main run loop to execute

ForkJoinTask

s.

---

