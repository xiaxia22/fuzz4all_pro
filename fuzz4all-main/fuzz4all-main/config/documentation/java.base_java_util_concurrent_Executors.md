# Class Executors

**Source:** `java.base\java\util\concurrent\Executors.html`

### Class Description

```java
public class
Executors

extends
Object
```

Factory and utility methods for

Executor

,

ExecutorService

,

ScheduledExecutorService

,

ThreadFactory

, and

Callable

classes defined in this
package. This class supports the following kinds of methods:

- Methods that create and return an

ExecutorService

set up with commonly useful configuration settings.

Methods that create and return a

ScheduledExecutorService

set up with commonly useful configuration settings.

Methods that create and return a "wrapped" ExecutorService, that
disables reconfiguration by making implementation-specific methods
inaccessible.

Methods that create and return a

ThreadFactory

that sets newly created threads to a known state.

Methods that create and return a

Callable

out of other closure-like forms, so they can be used
in execution methods requiring

Callable

.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ExecutorService
newFixedThreadPool​(int nThreads)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue. At any point, at most

nThreads

threads will be active processing tasks.
If additional tasks are submitted when all threads are active,
they will wait in the queue until a thread is available.
If any thread terminates due to a failure during execution
prior to shutdown, a new one will take its place if needed to
execute subsequent tasks. The threads in the pool will exist
until it is explicitly

shutdown

.

**Parameters:**
- nThreads

- the number of threads in the pool

**Returns:**
- the newly created thread pool

**Throws:**
- IllegalArgumentException

- if

nThreads <= 0

---

#### public static
ExecutorService
newWorkStealingPool​(int parallelism)

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention. The parallelism level corresponds to the
maximum number of threads actively engaged in, or available to
engage in, task processing. The actual number of threads may
grow and shrink dynamically. A work-stealing pool makes no
guarantees about the order in which submitted tasks are
executed.

**Parameters:**
- parallelism

- the targeted parallelism level

**Returns:**
- the newly created thread pool

**Throws:**
- IllegalArgumentException

- if

parallelism <= 0

**Since:**
- 1.8

---

#### public static
ExecutorService
newWorkStealingPool()

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

**Returns:**
- the newly created thread pool

**See Also:**
- newWorkStealingPool(int)

**Since:**
- 1.8

---

#### public static
ExecutorService
newFixedThreadPool​(int nThreads,

ThreadFactory
threadFactory)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed. At any point,
at most

nThreads

threads will be active processing
tasks. If additional tasks are submitted when all threads are
active, they will wait in the queue until a thread is
available. If any thread terminates due to a failure during
execution prior to shutdown, a new one will take its place if
needed to execute subsequent tasks. The threads in the pool will
exist until it is explicitly

shutdown

.

**Parameters:**
- nThreads

- the number of threads in the pool
- threadFactory

- the factory to use when creating new threads

**Returns:**
- the newly created thread pool

**Throws:**
- NullPointerException

- if threadFactory is null
- IllegalArgumentException

- if

nThreads <= 0

---

#### public static
ExecutorService
newSingleThreadExecutor()

Creates an Executor that uses a single worker thread operating
off an unbounded queue. (Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newFixedThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:**
- the newly created single-threaded Executor

---

#### public static
ExecutorService
newSingleThreadExecutor​(
ThreadFactory
threadFactory)

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed. Unlike the otherwise
equivalent

newFixedThreadPool(1, threadFactory)

the
returned executor is guaranteed not to be reconfigurable to use
additional threads.

**Parameters:**
- threadFactory

- the factory to use when creating new threads

**Returns:**
- the newly created single-threaded Executor

**Throws:**
- NullPointerException

- if threadFactory is null

---

#### public static
ExecutorService
newCachedThreadPool()

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available. These pools will typically improve the performance
of programs that execute many short-lived asynchronous tasks.
Calls to

execute

will reuse previously constructed
threads if available. If no existing thread is available, a new
thread will be created and added to the pool. Threads that have
not been used for sixty seconds are terminated and removed from
the cache. Thus, a pool that remains idle for long enough will
not consume any resources. Note that pools with similar
properties but different details (for example, timeout parameters)
may be created using

ThreadPoolExecutor

constructors.

**Returns:**
- the newly created thread pool

---

#### public static
ExecutorService
newCachedThreadPool​(
ThreadFactory
threadFactory)

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

**Parameters:**
- threadFactory

- the factory to use when creating new threads

**Returns:**
- the newly created thread pool

**Throws:**
- NullPointerException

- if threadFactory is null

---

#### public static
ScheduledExecutorService
newSingleThreadScheduledExecutor()

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.
(Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newScheduledThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:**
- the newly created scheduled executor

---

#### public static
ScheduledExecutorService
newSingleThreadScheduledExecutor​(
ThreadFactory
threadFactory)

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically. (Note
however that if this single thread terminates due to a failure
during execution prior to shutdown, a new one will take its
place if needed to execute subsequent tasks.) Tasks are
guaranteed to execute sequentially, and no more than one task
will be active at any given time. Unlike the otherwise
equivalent

newScheduledThreadPool(1, threadFactory)

the returned executor is guaranteed not to be reconfigurable to
use additional threads.

**Parameters:**
- threadFactory

- the factory to use when creating new threads

**Returns:**
- the newly created scheduled executor

**Throws:**
- NullPointerException

- if threadFactory is null

---

#### public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:**
- corePoolSize

- the number of threads to keep in the pool,
even if they are idle

**Returns:**
- the newly created scheduled thread pool

**Throws:**
- IllegalArgumentException

- if

corePoolSize < 0

---

#### public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize,

ThreadFactory
threadFactory)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:**
- corePoolSize

- the number of threads to keep in the pool,
even if they are idle
- threadFactory

- the factory to use when the executor
creates a new thread

**Returns:**
- the newly created scheduled thread pool

**Throws:**
- IllegalArgumentException

- if

corePoolSize < 0
- NullPointerException

- if threadFactory is null

---

#### public static
ExecutorService
unconfigurableExecutorService​(
ExecutorService
executor)

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:**
- executor

- the underlying implementation

**Returns:**
- an

ExecutorService

instance

**Throws:**
- NullPointerException

- if executor null

---

#### public static
ScheduledExecutorService
unconfigurableScheduledExecutorService​(
ScheduledExecutorService
executor)

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:**
- executor

- the underlying implementation

**Returns:**
- a

ScheduledExecutorService

instance

**Throws:**
- NullPointerException

- if executor null

---

#### public static
ThreadFactory
defaultThreadFactory()

Returns a default thread factory used to create new threads.
This factory creates all new threads used by an Executor in the
same

ThreadGroup

. If there is a

SecurityManager

, it uses the group of

System.getSecurityManager()

, else the group of the thread
invoking this

defaultThreadFactory

method. Each new
thread is created as a non-daemon thread with priority set to
the smaller of

Thread.NORM_PRIORITY

and the maximum
priority permitted in the thread group. New threads have names
accessible via

Thread.getName()

of

pool-N-thread-M

, where

N

is the sequence
number of this factory, and

M

is the sequence number
of the thread created by this factory.

**Returns:**
- a thread factory

---

#### public static
ThreadFactory
privilegedThreadFactory()

Returns a thread factory used to create new threads that
have the same permissions as the current thread.
This factory creates threads with the same settings as

defaultThreadFactory()

, additionally setting the
AccessControlContext and contextClassLoader of new threads to
be the same as the thread invoking this

privilegedThreadFactory

method. A new

privilegedThreadFactory

can be created within an

AccessController.doPrivileged

action setting the current thread's access control context to
create threads with the selected permission settings holding
within that action.

Note that while tasks running within such threads will have
the same access control and class loader settings as the
current thread, they need not have the same

ThreadLocal

or

InheritableThreadLocal

values. If necessary,
particular values of thread locals can be set or reset before
any task runs in

ThreadPoolExecutor

subclasses using

ThreadPoolExecutor.beforeExecute(Thread, Runnable)

.
Also, if it is necessary to initialize worker threads to have
the same InheritableThreadLocal settings as some other
designated thread, you can create a custom ThreadFactory in
which that thread waits for and services requests to create
others that will inherit its values.

**Returns:**
- a thread factory

**Throws:**
- AccessControlException

- if the current access control
context does not have permission to both get and set context
class loader

---

#### public static <T>
Callable
<T> callable​(
Runnable
task,
T result)

Returns a

Callable

object that, when
called, runs the given task and returns the given result. This
can be useful when applying methods requiring a

Callable

to an otherwise resultless action.

**Parameters:**
- task

- the task to run
- result

- the result to return

**Returns:**
- a callable object

**Throws:**
- NullPointerException

- if task null

**Type Parameters:**
- T

- the type of the result

---

#### public static
Callable
<
Object
> callable​(
Runnable
task)

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

**Parameters:**
- task

- the task to run

**Returns:**
- a callable object

**Throws:**
- NullPointerException

- if task null

---

#### public static
Callable
<
Object
> callable​(
PrivilegedAction
<?> action)

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

**Parameters:**
- action

- the privileged action to run

**Returns:**
- a callable object

**Throws:**
- NullPointerException

- if action null

---

#### public static
Callable
<
Object
> callable​(
PrivilegedExceptionAction
<?> action)

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

**Parameters:**
- action

- the privileged exception action to run

**Returns:**
- a callable object

**Throws:**
- NullPointerException

- if action null

---

#### public static <T>
Callable
<T> privilegedCallable​(
Callable
<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context. This method should normally be invoked within
an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Parameters:**
- callable

- the underlying task

**Returns:**
- a callable object

**Throws:**
- NullPointerException

- if callable null

**Type Parameters:**
- T

- the type of the callable's result

---

#### public static <T>
Callable
<T> privilegedCallableUsingCurrentClassLoader​(
Callable
<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader. This method should normally be invoked
within an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Parameters:**
- callable

- the underlying task

**Returns:**
- a callable object

**Throws:**
- NullPointerException

- if callable null
- AccessControlException

- if the current access control
context does not have permission to both set and get context
class loader

**Type Parameters:**
- T

- the type of the callable's result

---

### Additional Sections

#### Class Executors

java.lang.Object

- java.util.concurrent.Executors

java.util.concurrent.Executors

```java
public class
Executors

extends
Object
```

Factory and utility methods for

Executor

,

ExecutorService

,

ScheduledExecutorService

,

ThreadFactory

, and

Callable

classes defined in this
package. This class supports the following kinds of methods:

- Methods that create and return an

ExecutorService

set up with commonly useful configuration settings.

Methods that create and return a

ScheduledExecutorService

set up with commonly useful configuration settings.

Methods that create and return a "wrapped" ExecutorService, that
disables reconfiguration by making implementation-specific methods
inaccessible.

Methods that create and return a

ThreadFactory

that sets newly created threads to a known state.

Methods that create and return a

Callable

out of other closure-like forms, so they can be used
in execution methods requiring

Callable

.

**Since:** 1.5

public class

Executors

extends

Object

Factory and utility methods for

Executor

,

ExecutorService

,

ScheduledExecutorService

,

ThreadFactory

, and

Callable

classes defined in this
package. This class supports the following kinds of methods:

- Methods that create and return an

ExecutorService

set up with commonly useful configuration settings.

Methods that create and return a

ScheduledExecutorService

set up with commonly useful configuration settings.

Methods that create and return a "wrapped" ExecutorService, that
disables reconfiguration by making implementation-specific methods
inaccessible.

Methods that create and return a

ThreadFactory

that sets newly created threads to a known state.

Methods that create and return a

Callable

out of other closure-like forms, so they can be used
in execution methods requiring

Callable

.

Methods that create and return an

ExecutorService

set up with commonly useful configuration settings.

Methods that create and return a

ScheduledExecutorService

set up with commonly useful configuration settings.

Methods that create and return a "wrapped" ExecutorService, that
disables reconfiguration by making implementation-specific methods
inaccessible.

Methods that create and return a

ThreadFactory

that sets newly created threads to a known state.

Methods that create and return a

Callable

out of other closure-like forms, so they can be used
in execution methods requiring

Callable

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Callable

<

Object

>

callable

​(

Runnable

task)

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

static <T>

Callable

<T>

callable

​(

Runnable

task,
T result)

Returns a

Callable

object that, when
called, runs the given task and returns the given result.

static

Callable

<

Object

>

callable

​(

PrivilegedAction

<?> action)

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

static

Callable

<

Object

>

callable

​(

PrivilegedExceptionAction

<?> action)

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

static

ThreadFactory

defaultThreadFactory

()

Returns a default thread factory used to create new threads.

static

ExecutorService

newCachedThreadPool

()

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available.

static

ExecutorService

newCachedThreadPool

​(

ThreadFactory

threadFactory)

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

static

ExecutorService

newFixedThreadPool

​(int nThreads)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue.

static

ExecutorService

newFixedThreadPool

​(int nThreads,

ThreadFactory

threadFactory)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed.

static

ScheduledExecutorService

newScheduledThreadPool

​(int corePoolSize)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

static

ScheduledExecutorService

newScheduledThreadPool

​(int corePoolSize,

ThreadFactory

threadFactory)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

static

ExecutorService

newSingleThreadExecutor

()

Creates an Executor that uses a single worker thread operating
off an unbounded queue.

static

ExecutorService

newSingleThreadExecutor

​(

ThreadFactory

threadFactory)

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed.

static

ScheduledExecutorService

newSingleThreadScheduledExecutor

()

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.

static

ScheduledExecutorService

newSingleThreadScheduledExecutor

​(

ThreadFactory

threadFactory)

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.

static

ExecutorService

newWorkStealingPool

()

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

static

ExecutorService

newWorkStealingPool

​(int parallelism)

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention.

static <T>

Callable

<T>

privilegedCallable

​(

Callable

<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context.

static <T>

Callable

<T>

privilegedCallableUsingCurrentClassLoader

​(

Callable

<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader.

static

ThreadFactory

privilegedThreadFactory

()

Returns a thread factory used to create new threads that
have the same permissions as the current thread.

static

ExecutorService

unconfigurableExecutorService

​(

ExecutorService

executor)

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts.

static

ScheduledExecutorService

unconfigurableScheduledExecutorService

​(

ScheduledExecutorService

executor)

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Callable

<

Object

>

callable

​(

Runnable

task)

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

static <T>

Callable

<T>

callable

​(

Runnable

task,
T result)

Returns a

Callable

object that, when
called, runs the given task and returns the given result.

static

Callable

<

Object

>

callable

​(

PrivilegedAction

<?> action)

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

static

Callable

<

Object

>

callable

​(

PrivilegedExceptionAction

<?> action)

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

static

ThreadFactory

defaultThreadFactory

()

Returns a default thread factory used to create new threads.

static

ExecutorService

newCachedThreadPool

()

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available.

static

ExecutorService

newCachedThreadPool

​(

ThreadFactory

threadFactory)

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

static

ExecutorService

newFixedThreadPool

​(int nThreads)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue.

static

ExecutorService

newFixedThreadPool

​(int nThreads,

ThreadFactory

threadFactory)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed.

static

ScheduledExecutorService

newScheduledThreadPool

​(int corePoolSize)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

static

ScheduledExecutorService

newScheduledThreadPool

​(int corePoolSize,

ThreadFactory

threadFactory)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

static

ExecutorService

newSingleThreadExecutor

()

Creates an Executor that uses a single worker thread operating
off an unbounded queue.

static

ExecutorService

newSingleThreadExecutor

​(

ThreadFactory

threadFactory)

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed.

static

ScheduledExecutorService

newSingleThreadScheduledExecutor

()

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.

static

ScheduledExecutorService

newSingleThreadScheduledExecutor

​(

ThreadFactory

threadFactory)

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.

static

ExecutorService

newWorkStealingPool

()

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

static

ExecutorService

newWorkStealingPool

​(int parallelism)

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention.

static <T>

Callable

<T>

privilegedCallable

​(

Callable

<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context.

static <T>

Callable

<T>

privilegedCallableUsingCurrentClassLoader

​(

Callable

<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader.

static

ThreadFactory

privilegedThreadFactory

()

Returns a thread factory used to create new threads that
have the same permissions as the current thread.

static

ExecutorService

unconfigurableExecutorService

​(

ExecutorService

executor)

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts.

static

ScheduledExecutorService

unconfigurableScheduledExecutorService

​(

ScheduledExecutorService

executor)

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts.

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

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

Returns a

Callable

object that, when
called, runs the given task and returns the given result.

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

Returns a default thread factory used to create new threads.

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available.

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue.

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed.

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

Creates an Executor that uses a single worker thread operating
off an unbounded queue.

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed.

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention.

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context.

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader.

Returns a thread factory used to create new threads that
have the same permissions as the current thread.

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts.

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts.

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

============ METHOD DETAIL ==========

- Method Detail

- newFixedThreadPool

```java
public static
ExecutorService
newFixedThreadPool​(int nThreads)
```

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue. At any point, at most

nThreads

threads will be active processing tasks.
If additional tasks are submitted when all threads are active,
they will wait in the queue until a thread is available.
If any thread terminates due to a failure during execution
prior to shutdown, a new one will take its place if needed to
execute subsequent tasks. The threads in the pool will exist
until it is explicitly

shutdown

.

**Parameters:** nThreads

- the number of threads in the pool
**Returns:** the newly created thread pool
**Throws:** IllegalArgumentException

- if

nThreads <= 0

- newWorkStealingPool

```java
public static
ExecutorService
newWorkStealingPool​(int parallelism)
```

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention. The parallelism level corresponds to the
maximum number of threads actively engaged in, or available to
engage in, task processing. The actual number of threads may
grow and shrink dynamically. A work-stealing pool makes no
guarantees about the order in which submitted tasks are
executed.

**Parameters:** parallelism

- the targeted parallelism level
**Returns:** the newly created thread pool
**Throws:** IllegalArgumentException

- if

parallelism <= 0
**Since:** 1.8

- newWorkStealingPool

```java
public static
ExecutorService
newWorkStealingPool()
```

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

**Returns:** the newly created thread pool
**Since:** 1.8
**See Also:** newWorkStealingPool(int)

- newFixedThreadPool

```java
public static
ExecutorService
newFixedThreadPool​(int nThreads,

ThreadFactory
threadFactory)
```

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed. At any point,
at most

nThreads

threads will be active processing
tasks. If additional tasks are submitted when all threads are
active, they will wait in the queue until a thread is
available. If any thread terminates due to a failure during
execution prior to shutdown, a new one will take its place if
needed to execute subsequent tasks. The threads in the pool will
exist until it is explicitly

shutdown

.

**Parameters:** nThreads

- the number of threads in the pool
**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created thread pool
**Throws:** NullPointerException

- if threadFactory is null
**Throws:** IllegalArgumentException

- if

nThreads <= 0

- newSingleThreadExecutor

```java
public static
ExecutorService
newSingleThreadExecutor()
```

Creates an Executor that uses a single worker thread operating
off an unbounded queue. (Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newFixedThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:** the newly created single-threaded Executor

- newSingleThreadExecutor

```java
public static
ExecutorService
newSingleThreadExecutor​(
ThreadFactory
threadFactory)
```

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed. Unlike the otherwise
equivalent

newFixedThreadPool(1, threadFactory)

the
returned executor is guaranteed not to be reconfigurable to use
additional threads.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created single-threaded Executor
**Throws:** NullPointerException

- if threadFactory is null

- newCachedThreadPool

```java
public static
ExecutorService
newCachedThreadPool()
```

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available. These pools will typically improve the performance
of programs that execute many short-lived asynchronous tasks.
Calls to

execute

will reuse previously constructed
threads if available. If no existing thread is available, a new
thread will be created and added to the pool. Threads that have
not been used for sixty seconds are terminated and removed from
the cache. Thus, a pool that remains idle for long enough will
not consume any resources. Note that pools with similar
properties but different details (for example, timeout parameters)
may be created using

ThreadPoolExecutor

constructors.

**Returns:** the newly created thread pool

- newCachedThreadPool

```java
public static
ExecutorService
newCachedThreadPool​(
ThreadFactory
threadFactory)
```

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created thread pool
**Throws:** NullPointerException

- if threadFactory is null

- newSingleThreadScheduledExecutor

```java
public static
ScheduledExecutorService
newSingleThreadScheduledExecutor()
```

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.
(Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newScheduledThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:** the newly created scheduled executor

- newSingleThreadScheduledExecutor

```java
public static
ScheduledExecutorService
newSingleThreadScheduledExecutor​(
ThreadFactory
threadFactory)
```

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically. (Note
however that if this single thread terminates due to a failure
during execution prior to shutdown, a new one will take its
place if needed to execute subsequent tasks.) Tasks are
guaranteed to execute sequentially, and no more than one task
will be active at any given time. Unlike the otherwise
equivalent

newScheduledThreadPool(1, threadFactory)

the returned executor is guaranteed not to be reconfigurable to
use additional threads.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created scheduled executor
**Throws:** NullPointerException

- if threadFactory is null

- newScheduledThreadPool

```java
public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize)
```

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:** corePoolSize

- the number of threads to keep in the pool,
even if they are idle
**Returns:** the newly created scheduled thread pool
**Throws:** IllegalArgumentException

- if

corePoolSize < 0

- newScheduledThreadPool

```java
public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize,

ThreadFactory
threadFactory)
```

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:** corePoolSize

- the number of threads to keep in the pool,
even if they are idle
**Parameters:** threadFactory

- the factory to use when the executor
creates a new thread
**Returns:** the newly created scheduled thread pool
**Throws:** IllegalArgumentException

- if

corePoolSize < 0
**Throws:** NullPointerException

- if threadFactory is null

- unconfigurableExecutorService

```java
public static
ExecutorService
unconfigurableExecutorService​(
ExecutorService
executor)
```

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:** executor

- the underlying implementation
**Returns:** an

ExecutorService

instance
**Throws:** NullPointerException

- if executor null

- unconfigurableScheduledExecutorService

```java
public static
ScheduledExecutorService
unconfigurableScheduledExecutorService​(
ScheduledExecutorService
executor)
```

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:** executor

- the underlying implementation
**Returns:** a

ScheduledExecutorService

instance
**Throws:** NullPointerException

- if executor null

- defaultThreadFactory

```java
public static
ThreadFactory
defaultThreadFactory()
```

Returns a default thread factory used to create new threads.
This factory creates all new threads used by an Executor in the
same

ThreadGroup

. If there is a

SecurityManager

, it uses the group of

System.getSecurityManager()

, else the group of the thread
invoking this

defaultThreadFactory

method. Each new
thread is created as a non-daemon thread with priority set to
the smaller of

Thread.NORM_PRIORITY

and the maximum
priority permitted in the thread group. New threads have names
accessible via

Thread.getName()

of

pool-N-thread-M

, where

N

is the sequence
number of this factory, and

M

is the sequence number
of the thread created by this factory.

**Returns:** a thread factory

- privilegedThreadFactory

```java
public static
ThreadFactory
privilegedThreadFactory()
```

Returns a thread factory used to create new threads that
have the same permissions as the current thread.
This factory creates threads with the same settings as

defaultThreadFactory()

, additionally setting the
AccessControlContext and contextClassLoader of new threads to
be the same as the thread invoking this

privilegedThreadFactory

method. A new

privilegedThreadFactory

can be created within an

AccessController.doPrivileged

action setting the current thread's access control context to
create threads with the selected permission settings holding
within that action.

Note that while tasks running within such threads will have
the same access control and class loader settings as the
current thread, they need not have the same

ThreadLocal

or

InheritableThreadLocal

values. If necessary,
particular values of thread locals can be set or reset before
any task runs in

ThreadPoolExecutor

subclasses using

ThreadPoolExecutor.beforeExecute(Thread, Runnable)

.
Also, if it is necessary to initialize worker threads to have
the same InheritableThreadLocal settings as some other
designated thread, you can create a custom ThreadFactory in
which that thread waits for and services requests to create
others that will inherit its values.

**Returns:** a thread factory
**Throws:** AccessControlException

- if the current access control
context does not have permission to both get and set context
class loader

- callable

```java
public static <T>
Callable
<T> callable​(
Runnable
task,
T result)
```

Returns a

Callable

object that, when
called, runs the given task and returns the given result. This
can be useful when applying methods requiring a

Callable

to an otherwise resultless action.

**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to run
**Parameters:** result

- the result to return
**Returns:** a callable object
**Throws:** NullPointerException

- if task null

- callable

```java
public static
Callable
<
Object
> callable​(
Runnable
task)
```

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

**Parameters:** task

- the task to run
**Returns:** a callable object
**Throws:** NullPointerException

- if task null

- callable

```java
public static
Callable
<
Object
> callable​(
PrivilegedAction
<?> action)
```

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

**Parameters:** action

- the privileged action to run
**Returns:** a callable object
**Throws:** NullPointerException

- if action null

- callable

```java
public static
Callable
<
Object
> callable​(
PrivilegedExceptionAction
<?> action)
```

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

**Parameters:** action

- the privileged exception action to run
**Returns:** a callable object
**Throws:** NullPointerException

- if action null

- privilegedCallable

```java
public static <T>
Callable
<T> privilegedCallable​(
Callable
<T> callable)
```

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context. This method should normally be invoked within
an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the underlying task
**Returns:** a callable object
**Throws:** NullPointerException

- if callable null

- privilegedCallableUsingCurrentClassLoader

```java
public static <T>
Callable
<T> privilegedCallableUsingCurrentClassLoader​(
Callable
<T> callable)
```

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader. This method should normally be invoked
within an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the underlying task
**Returns:** a callable object
**Throws:** NullPointerException

- if callable null
**Throws:** AccessControlException

- if the current access control
context does not have permission to both set and get context
class loader

Method Detail

- newFixedThreadPool

```java
public static
ExecutorService
newFixedThreadPool​(int nThreads)
```

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue. At any point, at most

nThreads

threads will be active processing tasks.
If additional tasks are submitted when all threads are active,
they will wait in the queue until a thread is available.
If any thread terminates due to a failure during execution
prior to shutdown, a new one will take its place if needed to
execute subsequent tasks. The threads in the pool will exist
until it is explicitly

shutdown

.

**Parameters:** nThreads

- the number of threads in the pool
**Returns:** the newly created thread pool
**Throws:** IllegalArgumentException

- if

nThreads <= 0

- newWorkStealingPool

```java
public static
ExecutorService
newWorkStealingPool​(int parallelism)
```

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention. The parallelism level corresponds to the
maximum number of threads actively engaged in, or available to
engage in, task processing. The actual number of threads may
grow and shrink dynamically. A work-stealing pool makes no
guarantees about the order in which submitted tasks are
executed.

**Parameters:** parallelism

- the targeted parallelism level
**Returns:** the newly created thread pool
**Throws:** IllegalArgumentException

- if

parallelism <= 0
**Since:** 1.8

- newWorkStealingPool

```java
public static
ExecutorService
newWorkStealingPool()
```

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

**Returns:** the newly created thread pool
**Since:** 1.8
**See Also:** newWorkStealingPool(int)

- newFixedThreadPool

```java
public static
ExecutorService
newFixedThreadPool​(int nThreads,

ThreadFactory
threadFactory)
```

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed. At any point,
at most

nThreads

threads will be active processing
tasks. If additional tasks are submitted when all threads are
active, they will wait in the queue until a thread is
available. If any thread terminates due to a failure during
execution prior to shutdown, a new one will take its place if
needed to execute subsequent tasks. The threads in the pool will
exist until it is explicitly

shutdown

.

**Parameters:** nThreads

- the number of threads in the pool
**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created thread pool
**Throws:** NullPointerException

- if threadFactory is null
**Throws:** IllegalArgumentException

- if

nThreads <= 0

- newSingleThreadExecutor

```java
public static
ExecutorService
newSingleThreadExecutor()
```

Creates an Executor that uses a single worker thread operating
off an unbounded queue. (Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newFixedThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:** the newly created single-threaded Executor

- newSingleThreadExecutor

```java
public static
ExecutorService
newSingleThreadExecutor​(
ThreadFactory
threadFactory)
```

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed. Unlike the otherwise
equivalent

newFixedThreadPool(1, threadFactory)

the
returned executor is guaranteed not to be reconfigurable to use
additional threads.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created single-threaded Executor
**Throws:** NullPointerException

- if threadFactory is null

- newCachedThreadPool

```java
public static
ExecutorService
newCachedThreadPool()
```

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available. These pools will typically improve the performance
of programs that execute many short-lived asynchronous tasks.
Calls to

execute

will reuse previously constructed
threads if available. If no existing thread is available, a new
thread will be created and added to the pool. Threads that have
not been used for sixty seconds are terminated and removed from
the cache. Thus, a pool that remains idle for long enough will
not consume any resources. Note that pools with similar
properties but different details (for example, timeout parameters)
may be created using

ThreadPoolExecutor

constructors.

**Returns:** the newly created thread pool

- newCachedThreadPool

```java
public static
ExecutorService
newCachedThreadPool​(
ThreadFactory
threadFactory)
```

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created thread pool
**Throws:** NullPointerException

- if threadFactory is null

- newSingleThreadScheduledExecutor

```java
public static
ScheduledExecutorService
newSingleThreadScheduledExecutor()
```

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.
(Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newScheduledThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:** the newly created scheduled executor

- newSingleThreadScheduledExecutor

```java
public static
ScheduledExecutorService
newSingleThreadScheduledExecutor​(
ThreadFactory
threadFactory)
```

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically. (Note
however that if this single thread terminates due to a failure
during execution prior to shutdown, a new one will take its
place if needed to execute subsequent tasks.) Tasks are
guaranteed to execute sequentially, and no more than one task
will be active at any given time. Unlike the otherwise
equivalent

newScheduledThreadPool(1, threadFactory)

the returned executor is guaranteed not to be reconfigurable to
use additional threads.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created scheduled executor
**Throws:** NullPointerException

- if threadFactory is null

- newScheduledThreadPool

```java
public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize)
```

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:** corePoolSize

- the number of threads to keep in the pool,
even if they are idle
**Returns:** the newly created scheduled thread pool
**Throws:** IllegalArgumentException

- if

corePoolSize < 0

- newScheduledThreadPool

```java
public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize,

ThreadFactory
threadFactory)
```

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:** corePoolSize

- the number of threads to keep in the pool,
even if they are idle
**Parameters:** threadFactory

- the factory to use when the executor
creates a new thread
**Returns:** the newly created scheduled thread pool
**Throws:** IllegalArgumentException

- if

corePoolSize < 0
**Throws:** NullPointerException

- if threadFactory is null

- unconfigurableExecutorService

```java
public static
ExecutorService
unconfigurableExecutorService​(
ExecutorService
executor)
```

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:** executor

- the underlying implementation
**Returns:** an

ExecutorService

instance
**Throws:** NullPointerException

- if executor null

- unconfigurableScheduledExecutorService

```java
public static
ScheduledExecutorService
unconfigurableScheduledExecutorService​(
ScheduledExecutorService
executor)
```

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:** executor

- the underlying implementation
**Returns:** a

ScheduledExecutorService

instance
**Throws:** NullPointerException

- if executor null

- defaultThreadFactory

```java
public static
ThreadFactory
defaultThreadFactory()
```

Returns a default thread factory used to create new threads.
This factory creates all new threads used by an Executor in the
same

ThreadGroup

. If there is a

SecurityManager

, it uses the group of

System.getSecurityManager()

, else the group of the thread
invoking this

defaultThreadFactory

method. Each new
thread is created as a non-daemon thread with priority set to
the smaller of

Thread.NORM_PRIORITY

and the maximum
priority permitted in the thread group. New threads have names
accessible via

Thread.getName()

of

pool-N-thread-M

, where

N

is the sequence
number of this factory, and

M

is the sequence number
of the thread created by this factory.

**Returns:** a thread factory

- privilegedThreadFactory

```java
public static
ThreadFactory
privilegedThreadFactory()
```

Returns a thread factory used to create new threads that
have the same permissions as the current thread.
This factory creates threads with the same settings as

defaultThreadFactory()

, additionally setting the
AccessControlContext and contextClassLoader of new threads to
be the same as the thread invoking this

privilegedThreadFactory

method. A new

privilegedThreadFactory

can be created within an

AccessController.doPrivileged

action setting the current thread's access control context to
create threads with the selected permission settings holding
within that action.

Note that while tasks running within such threads will have
the same access control and class loader settings as the
current thread, they need not have the same

ThreadLocal

or

InheritableThreadLocal

values. If necessary,
particular values of thread locals can be set or reset before
any task runs in

ThreadPoolExecutor

subclasses using

ThreadPoolExecutor.beforeExecute(Thread, Runnable)

.
Also, if it is necessary to initialize worker threads to have
the same InheritableThreadLocal settings as some other
designated thread, you can create a custom ThreadFactory in
which that thread waits for and services requests to create
others that will inherit its values.

**Returns:** a thread factory
**Throws:** AccessControlException

- if the current access control
context does not have permission to both get and set context
class loader

- callable

```java
public static <T>
Callable
<T> callable​(
Runnable
task,
T result)
```

Returns a

Callable

object that, when
called, runs the given task and returns the given result. This
can be useful when applying methods requiring a

Callable

to an otherwise resultless action.

**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to run
**Parameters:** result

- the result to return
**Returns:** a callable object
**Throws:** NullPointerException

- if task null

- callable

```java
public static
Callable
<
Object
> callable​(
Runnable
task)
```

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

**Parameters:** task

- the task to run
**Returns:** a callable object
**Throws:** NullPointerException

- if task null

- callable

```java
public static
Callable
<
Object
> callable​(
PrivilegedAction
<?> action)
```

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

**Parameters:** action

- the privileged action to run
**Returns:** a callable object
**Throws:** NullPointerException

- if action null

- callable

```java
public static
Callable
<
Object
> callable​(
PrivilegedExceptionAction
<?> action)
```

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

**Parameters:** action

- the privileged exception action to run
**Returns:** a callable object
**Throws:** NullPointerException

- if action null

- privilegedCallable

```java
public static <T>
Callable
<T> privilegedCallable​(
Callable
<T> callable)
```

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context. This method should normally be invoked within
an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the underlying task
**Returns:** a callable object
**Throws:** NullPointerException

- if callable null

- privilegedCallableUsingCurrentClassLoader

```java
public static <T>
Callable
<T> privilegedCallableUsingCurrentClassLoader​(
Callable
<T> callable)
```

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader. This method should normally be invoked
within an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the underlying task
**Returns:** a callable object
**Throws:** NullPointerException

- if callable null
**Throws:** AccessControlException

- if the current access control
context does not have permission to both set and get context
class loader

---

#### Method Detail

newFixedThreadPool

```java
public static
ExecutorService
newFixedThreadPool​(int nThreads)
```

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue. At any point, at most

nThreads

threads will be active processing tasks.
If additional tasks are submitted when all threads are active,
they will wait in the queue until a thread is available.
If any thread terminates due to a failure during execution
prior to shutdown, a new one will take its place if needed to
execute subsequent tasks. The threads in the pool will exist
until it is explicitly

shutdown

.

**Parameters:** nThreads

- the number of threads in the pool
**Returns:** the newly created thread pool
**Throws:** IllegalArgumentException

- if

nThreads <= 0

---

#### newFixedThreadPool

public static

ExecutorService

newFixedThreadPool​(int nThreads)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue. At any point, at most

nThreads

threads will be active processing tasks.
If additional tasks are submitted when all threads are active,
they will wait in the queue until a thread is available.
If any thread terminates due to a failure during execution
prior to shutdown, a new one will take its place if needed to
execute subsequent tasks. The threads in the pool will exist
until it is explicitly

shutdown

.

newWorkStealingPool

```java
public static
ExecutorService
newWorkStealingPool​(int parallelism)
```

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention. The parallelism level corresponds to the
maximum number of threads actively engaged in, or available to
engage in, task processing. The actual number of threads may
grow and shrink dynamically. A work-stealing pool makes no
guarantees about the order in which submitted tasks are
executed.

**Parameters:** parallelism

- the targeted parallelism level
**Returns:** the newly created thread pool
**Throws:** IllegalArgumentException

- if

parallelism <= 0
**Since:** 1.8

---

#### newWorkStealingPool

public static

ExecutorService

newWorkStealingPool​(int parallelism)

Creates a thread pool that maintains enough threads to support
the given parallelism level, and may use multiple queues to
reduce contention. The parallelism level corresponds to the
maximum number of threads actively engaged in, or available to
engage in, task processing. The actual number of threads may
grow and shrink dynamically. A work-stealing pool makes no
guarantees about the order in which submitted tasks are
executed.

newWorkStealingPool

```java
public static
ExecutorService
newWorkStealingPool()
```

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

**Returns:** the newly created thread pool
**Since:** 1.8
**See Also:** newWorkStealingPool(int)

---

#### newWorkStealingPool

public static

ExecutorService

newWorkStealingPool()

Creates a work-stealing thread pool using the number of

available processors

as its target parallelism level.

newFixedThreadPool

```java
public static
ExecutorService
newFixedThreadPool​(int nThreads,

ThreadFactory
threadFactory)
```

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed. At any point,
at most

nThreads

threads will be active processing
tasks. If additional tasks are submitted when all threads are
active, they will wait in the queue until a thread is
available. If any thread terminates due to a failure during
execution prior to shutdown, a new one will take its place if
needed to execute subsequent tasks. The threads in the pool will
exist until it is explicitly

shutdown

.

**Parameters:** nThreads

- the number of threads in the pool
**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created thread pool
**Throws:** NullPointerException

- if threadFactory is null
**Throws:** IllegalArgumentException

- if

nThreads <= 0

---

#### newFixedThreadPool

public static

ExecutorService

newFixedThreadPool​(int nThreads,

ThreadFactory

threadFactory)

Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed. At any point,
at most

nThreads

threads will be active processing
tasks. If additional tasks are submitted when all threads are
active, they will wait in the queue until a thread is
available. If any thread terminates due to a failure during
execution prior to shutdown, a new one will take its place if
needed to execute subsequent tasks. The threads in the pool will
exist until it is explicitly

shutdown

.

newSingleThreadExecutor

```java
public static
ExecutorService
newSingleThreadExecutor()
```

Creates an Executor that uses a single worker thread operating
off an unbounded queue. (Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newFixedThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:** the newly created single-threaded Executor

---

#### newSingleThreadExecutor

public static

ExecutorService

newSingleThreadExecutor()

Creates an Executor that uses a single worker thread operating
off an unbounded queue. (Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newFixedThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

newSingleThreadExecutor

```java
public static
ExecutorService
newSingleThreadExecutor​(
ThreadFactory
threadFactory)
```

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed. Unlike the otherwise
equivalent

newFixedThreadPool(1, threadFactory)

the
returned executor is guaranteed not to be reconfigurable to use
additional threads.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created single-threaded Executor
**Throws:** NullPointerException

- if threadFactory is null

---

#### newSingleThreadExecutor

public static

ExecutorService

newSingleThreadExecutor​(

ThreadFactory

threadFactory)

Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed. Unlike the otherwise
equivalent

newFixedThreadPool(1, threadFactory)

the
returned executor is guaranteed not to be reconfigurable to use
additional threads.

newCachedThreadPool

```java
public static
ExecutorService
newCachedThreadPool()
```

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available. These pools will typically improve the performance
of programs that execute many short-lived asynchronous tasks.
Calls to

execute

will reuse previously constructed
threads if available. If no existing thread is available, a new
thread will be created and added to the pool. Threads that have
not been used for sixty seconds are terminated and removed from
the cache. Thus, a pool that remains idle for long enough will
not consume any resources. Note that pools with similar
properties but different details (for example, timeout parameters)
may be created using

ThreadPoolExecutor

constructors.

**Returns:** the newly created thread pool

---

#### newCachedThreadPool

public static

ExecutorService

newCachedThreadPool()

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available. These pools will typically improve the performance
of programs that execute many short-lived asynchronous tasks.
Calls to

execute

will reuse previously constructed
threads if available. If no existing thread is available, a new
thread will be created and added to the pool. Threads that have
not been used for sixty seconds are terminated and removed from
the cache. Thus, a pool that remains idle for long enough will
not consume any resources. Note that pools with similar
properties but different details (for example, timeout parameters)
may be created using

ThreadPoolExecutor

constructors.

newCachedThreadPool

```java
public static
ExecutorService
newCachedThreadPool​(
ThreadFactory
threadFactory)
```

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created thread pool
**Throws:** NullPointerException

- if threadFactory is null

---

#### newCachedThreadPool

public static

ExecutorService

newCachedThreadPool​(

ThreadFactory

threadFactory)

Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.

newSingleThreadScheduledExecutor

```java
public static
ScheduledExecutorService
newSingleThreadScheduledExecutor()
```

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.
(Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newScheduledThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

**Returns:** the newly created scheduled executor

---

#### newSingleThreadScheduledExecutor

public static

ScheduledExecutorService

newSingleThreadScheduledExecutor()

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically.
(Note however that if this single
thread terminates due to a failure during execution prior to
shutdown, a new one will take its place if needed to execute
subsequent tasks.) Tasks are guaranteed to execute
sequentially, and no more than one task will be active at any
given time. Unlike the otherwise equivalent

newScheduledThreadPool(1)

the returned executor is
guaranteed not to be reconfigurable to use additional threads.

newSingleThreadScheduledExecutor

```java
public static
ScheduledExecutorService
newSingleThreadScheduledExecutor​(
ThreadFactory
threadFactory)
```

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically. (Note
however that if this single thread terminates due to a failure
during execution prior to shutdown, a new one will take its
place if needed to execute subsequent tasks.) Tasks are
guaranteed to execute sequentially, and no more than one task
will be active at any given time. Unlike the otherwise
equivalent

newScheduledThreadPool(1, threadFactory)

the returned executor is guaranteed not to be reconfigurable to
use additional threads.

**Parameters:** threadFactory

- the factory to use when creating new threads
**Returns:** the newly created scheduled executor
**Throws:** NullPointerException

- if threadFactory is null

---

#### newSingleThreadScheduledExecutor

public static

ScheduledExecutorService

newSingleThreadScheduledExecutor​(

ThreadFactory

threadFactory)

Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically. (Note
however that if this single thread terminates due to a failure
during execution prior to shutdown, a new one will take its
place if needed to execute subsequent tasks.) Tasks are
guaranteed to execute sequentially, and no more than one task
will be active at any given time. Unlike the otherwise
equivalent

newScheduledThreadPool(1, threadFactory)

the returned executor is guaranteed not to be reconfigurable to
use additional threads.

newScheduledThreadPool

```java
public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize)
```

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:** corePoolSize

- the number of threads to keep in the pool,
even if they are idle
**Returns:** the newly created scheduled thread pool
**Throws:** IllegalArgumentException

- if

corePoolSize < 0

---

#### newScheduledThreadPool

public static

ScheduledExecutorService

newScheduledThreadPool​(int corePoolSize)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

newScheduledThreadPool

```java
public static
ScheduledExecutorService
newScheduledThreadPool​(int corePoolSize,

ThreadFactory
threadFactory)
```

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

**Parameters:** corePoolSize

- the number of threads to keep in the pool,
even if they are idle
**Parameters:** threadFactory

- the factory to use when the executor
creates a new thread
**Returns:** the newly created scheduled thread pool
**Throws:** IllegalArgumentException

- if

corePoolSize < 0
**Throws:** NullPointerException

- if threadFactory is null

---

#### newScheduledThreadPool

public static

ScheduledExecutorService

newScheduledThreadPool​(int corePoolSize,

ThreadFactory

threadFactory)

Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.

unconfigurableExecutorService

```java
public static
ExecutorService
unconfigurableExecutorService​(
ExecutorService
executor)
```

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:** executor

- the underlying implementation
**Returns:** an

ExecutorService

instance
**Throws:** NullPointerException

- if executor null

---

#### unconfigurableExecutorService

public static

ExecutorService

unconfigurableExecutorService​(

ExecutorService

executor)

Returns an object that delegates all defined

ExecutorService

methods to the given executor, but not any
other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

unconfigurableScheduledExecutorService

```java
public static
ScheduledExecutorService
unconfigurableScheduledExecutorService​(
ScheduledExecutorService
executor)
```

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

**Parameters:** executor

- the underlying implementation
**Returns:** a

ScheduledExecutorService

instance
**Throws:** NullPointerException

- if executor null

---

#### unconfigurableScheduledExecutorService

public static

ScheduledExecutorService

unconfigurableScheduledExecutorService​(

ScheduledExecutorService

executor)

Returns an object that delegates all defined

ScheduledExecutorService

methods to the given executor, but
not any other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.

defaultThreadFactory

```java
public static
ThreadFactory
defaultThreadFactory()
```

Returns a default thread factory used to create new threads.
This factory creates all new threads used by an Executor in the
same

ThreadGroup

. If there is a

SecurityManager

, it uses the group of

System.getSecurityManager()

, else the group of the thread
invoking this

defaultThreadFactory

method. Each new
thread is created as a non-daemon thread with priority set to
the smaller of

Thread.NORM_PRIORITY

and the maximum
priority permitted in the thread group. New threads have names
accessible via

Thread.getName()

of

pool-N-thread-M

, where

N

is the sequence
number of this factory, and

M

is the sequence number
of the thread created by this factory.

**Returns:** a thread factory

---

#### defaultThreadFactory

public static

ThreadFactory

defaultThreadFactory()

Returns a default thread factory used to create new threads.
This factory creates all new threads used by an Executor in the
same

ThreadGroup

. If there is a

SecurityManager

, it uses the group of

System.getSecurityManager()

, else the group of the thread
invoking this

defaultThreadFactory

method. Each new
thread is created as a non-daemon thread with priority set to
the smaller of

Thread.NORM_PRIORITY

and the maximum
priority permitted in the thread group. New threads have names
accessible via

Thread.getName()

of

pool-N-thread-M

, where

N

is the sequence
number of this factory, and

M

is the sequence number
of the thread created by this factory.

privilegedThreadFactory

```java
public static
ThreadFactory
privilegedThreadFactory()
```

Returns a thread factory used to create new threads that
have the same permissions as the current thread.
This factory creates threads with the same settings as

defaultThreadFactory()

, additionally setting the
AccessControlContext and contextClassLoader of new threads to
be the same as the thread invoking this

privilegedThreadFactory

method. A new

privilegedThreadFactory

can be created within an

AccessController.doPrivileged

action setting the current thread's access control context to
create threads with the selected permission settings holding
within that action.

Note that while tasks running within such threads will have
the same access control and class loader settings as the
current thread, they need not have the same

ThreadLocal

or

InheritableThreadLocal

values. If necessary,
particular values of thread locals can be set or reset before
any task runs in

ThreadPoolExecutor

subclasses using

ThreadPoolExecutor.beforeExecute(Thread, Runnable)

.
Also, if it is necessary to initialize worker threads to have
the same InheritableThreadLocal settings as some other
designated thread, you can create a custom ThreadFactory in
which that thread waits for and services requests to create
others that will inherit its values.

**Returns:** a thread factory
**Throws:** AccessControlException

- if the current access control
context does not have permission to both get and set context
class loader

---

#### privilegedThreadFactory

public static

ThreadFactory

privilegedThreadFactory()

Returns a thread factory used to create new threads that
have the same permissions as the current thread.
This factory creates threads with the same settings as

defaultThreadFactory()

, additionally setting the
AccessControlContext and contextClassLoader of new threads to
be the same as the thread invoking this

privilegedThreadFactory

method. A new

privilegedThreadFactory

can be created within an

AccessController.doPrivileged

action setting the current thread's access control context to
create threads with the selected permission settings holding
within that action.

Note that while tasks running within such threads will have
the same access control and class loader settings as the
current thread, they need not have the same

ThreadLocal

or

InheritableThreadLocal

values. If necessary,
particular values of thread locals can be set or reset before
any task runs in

ThreadPoolExecutor

subclasses using

ThreadPoolExecutor.beforeExecute(Thread, Runnable)

.
Also, if it is necessary to initialize worker threads to have
the same InheritableThreadLocal settings as some other
designated thread, you can create a custom ThreadFactory in
which that thread waits for and services requests to create
others that will inherit its values.

Note that while tasks running within such threads will have
the same access control and class loader settings as the
current thread, they need not have the same

ThreadLocal

or

InheritableThreadLocal

values. If necessary,
particular values of thread locals can be set or reset before
any task runs in

ThreadPoolExecutor

subclasses using

ThreadPoolExecutor.beforeExecute(Thread, Runnable)

.
Also, if it is necessary to initialize worker threads to have
the same InheritableThreadLocal settings as some other
designated thread, you can create a custom ThreadFactory in
which that thread waits for and services requests to create
others that will inherit its values.

callable

```java
public static <T>
Callable
<T> callable​(
Runnable
task,
T result)
```

Returns a

Callable

object that, when
called, runs the given task and returns the given result. This
can be useful when applying methods requiring a

Callable

to an otherwise resultless action.

**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to run
**Parameters:** result

- the result to return
**Returns:** a callable object
**Throws:** NullPointerException

- if task null

---

#### callable

public static <T>

Callable

<T> callable​(

Runnable

task,
T result)

Returns a

Callable

object that, when
called, runs the given task and returns the given result. This
can be useful when applying methods requiring a

Callable

to an otherwise resultless action.

callable

```java
public static
Callable
<
Object
> callable​(
Runnable
task)
```

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

**Parameters:** task

- the task to run
**Returns:** a callable object
**Throws:** NullPointerException

- if task null

---

#### callable

public static

Callable

<

Object

> callable​(

Runnable

task)

Returns a

Callable

object that, when
called, runs the given task and returns

null

.

callable

```java
public static
Callable
<
Object
> callable​(
PrivilegedAction
<?> action)
```

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

**Parameters:** action

- the privileged action to run
**Returns:** a callable object
**Throws:** NullPointerException

- if action null

---

#### callable

public static

Callable

<

Object

> callable​(

PrivilegedAction

<?> action)

Returns a

Callable

object that, when
called, runs the given privileged action and returns its result.

callable

```java
public static
Callable
<
Object
> callable​(
PrivilegedExceptionAction
<?> action)
```

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

**Parameters:** action

- the privileged exception action to run
**Returns:** a callable object
**Throws:** NullPointerException

- if action null

---

#### callable

public static

Callable

<

Object

> callable​(

PrivilegedExceptionAction

<?> action)

Returns a

Callable

object that, when
called, runs the given privileged exception action and returns
its result.

privilegedCallable

```java
public static <T>
Callable
<T> privilegedCallable​(
Callable
<T> callable)
```

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context. This method should normally be invoked within
an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the underlying task
**Returns:** a callable object
**Throws:** NullPointerException

- if callable null

---

#### privilegedCallable

public static <T>

Callable

<T> privilegedCallable​(

Callable

<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context. This method should normally be invoked within
an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

privilegedCallableUsingCurrentClassLoader

```java
public static <T>
Callable
<T> privilegedCallableUsingCurrentClassLoader​(
Callable
<T> callable)
```

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader. This method should normally be invoked
within an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the underlying task
**Returns:** a callable object
**Throws:** NullPointerException

- if callable null
**Throws:** AccessControlException

- if the current access control
context does not have permission to both set and get context
class loader

---

#### privilegedCallableUsingCurrentClassLoader

public static <T>

Callable

<T> privilegedCallableUsingCurrentClassLoader​(

Callable

<T> callable)

Returns a

Callable

object that will, when called,
execute the given

callable

under the current access
control context, with the current context class loader as the
context class loader. This method should normally be invoked
within an

AccessController.doPrivileged

action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated

AccessControlException

.

---

