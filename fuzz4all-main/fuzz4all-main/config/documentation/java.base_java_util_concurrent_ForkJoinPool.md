# Class ForkJoinPool

**Source:** `java.base\java\util\concurrent\ForkJoinPool.html`

### Class Description

```java
public class
ForkJoinPool

extends
AbstractExecutorService
```

An

ExecutorService

for running

ForkJoinTask

s.
A

ForkJoinPool

provides the entry point for submissions
from non-

ForkJoinTask

clients, as well as management and
monitoring operations.

A

ForkJoinPool

differs from other kinds of

ExecutorService

mainly by virtue of employing

work-stealing

: all threads in the pool attempt to find and
execute tasks submitted to the pool and/or created by other active
tasks (eventually blocking waiting for work if none exist). This
enables efficient processing when most tasks spawn other subtasks
(as do most

ForkJoinTask

s), as well as when many small
tasks are submitted to the pool from external clients. Especially
when setting

asyncMode

to true in constructors,

ForkJoinPool

s may also be appropriate for use with event-style
tasks that are never joined. All worker threads are initialized
with

Thread.isDaemon()

set

true

.

A static

commonPool()

is available and appropriate for
most applications. The common pool is used by any ForkJoinTask that
is not explicitly submitted to a specified pool. Using the common
pool normally reduces resource usage (its threads are slowly
reclaimed during periods of non-use, and reinstated upon subsequent
use).

For applications that require separate or custom pools, a

ForkJoinPool

may be constructed with a given target parallelism
level; by default, equal to the number of available processors.
The pool attempts to maintain enough active (or available) threads
by dynamically adding, suspending, or resuming internal worker
threads, even if some tasks are stalled waiting to join others.
However, no such adjustments are guaranteed in the face of blocked
I/O or other unmanaged synchronization. The nested

ForkJoinPool.ManagedBlocker

interface enables extension of the kinds of
synchronization accommodated. The default policies may be
overridden using a constructor with parameters corresponding to
those documented in class

ThreadPoolExecutor

.

In addition to execution and lifecycle control methods, this
class provides status check methods (for example

getStealCount()

) that are intended to aid in developing,
tuning, and monitoring fork/join applications. Also, method

toString()

returns indications of pool state in a
convenient form for informal monitoring.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

**All Implemented Interfaces:** Executor

,

ExecutorService

---

### Field Details

#### public static final
ForkJoinPool.ForkJoinWorkerThreadFactory
defaultForkJoinWorkerThreadFactory

Creates a new ForkJoinWorkerThread. This factory is used unless
overridden in ForkJoinPool constructors.

---

### Constructor Details

#### public ForkJoinPool()

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Throws:**
- SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### public ForkJoinPool​(int parallelism)

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

**Parameters:**
- parallelism

- the parallelism level

**Throws:**
- IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
- SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode)

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Parameters:**
- parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
- factory

- the factory for creating new threads. For default value,
use

defaultForkJoinWorkerThreadFactory

.
- handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while executing
tasks. For default value, use

null

.
- asyncMode

- if true,
establishes local first-in-first-out scheduling mode for forked
tasks that are never joined. This mode may be more appropriate
than default locally stack-based mode in applications in which
worker threads only process event-style asynchronous tasks.
For default value, use

false

.

**Throws:**
- IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
- NullPointerException

- if the factory is null
- SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode,
int corePoolSize,
int maximumPoolSize,
int minimumRunnable,

Predicate
<? super
ForkJoinPool
> saturate,
long keepAliveTime,

TimeUnit
unit)

Creates a

ForkJoinPool

with the given parameters.

**Parameters:**
- parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
- factory

- the factory for creating new threads. For
default value, use

defaultForkJoinWorkerThreadFactory

.
- handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while
executing tasks. For default value, use

null

.
- asyncMode

- if true, establishes local first-in-first-out
scheduling mode for forked tasks that are never joined. This
mode may be more appropriate than default locally stack-based
mode in applications in which worker threads only process
event-style asynchronous tasks. For default value, use

false

.
- corePoolSize

- the number of threads to keep in the pool
(unless timed out after an elapsed keep-alive). Normally (and
by default) this is the same value as the parallelism level,
but may be set to a larger value to reduce dynamic overhead if
tasks regularly block. Using a smaller value (for example

0

) has the same effect as the default.
- maximumPoolSize

- the maximum number of threads allowed.
When the maximum is reached, attempts to replace blocked
threads fail. (However, because creation and termination of
different threads may overlap, and may be managed by the given
thread factory, this value may be transiently exceeded.) To
arrange the same value as is used by default for the common
pool, use

256

plus the

parallelism

level. (By
default, the common pool allows a maximum of 256 spare
threads.) Using a value (for example

Integer.MAX_VALUE

) larger than the implementation's total
thread limit has the same effect as using this limit (which is
the default).
- minimumRunnable

- the minimum allowed number of core
threads not blocked by a join or

ForkJoinPool.ManagedBlocker

. To
ensure progress, when too few unblocked threads exist and
unexecuted tasks may exist, new threads are constructed, up to
the given maximumPoolSize. For the default value, use

1

, that ensures liveness. A larger value might improve
throughput in the presence of blocked activities, but might
not, due to increased overhead. A value of zero may be
acceptable when submitted tasks cannot have dependencies
requiring additional threads.
- saturate

- if non-null, a predicate invoked upon attempts
to create more than the maximum total allowed threads. By
default, when a thread is about to block on a join or

ForkJoinPool.ManagedBlocker

, but cannot be replaced because the
maximumPoolSize would be exceeded, a

RejectedExecutionException

is thrown. But if this predicate
returns

true

, then no exception is thrown, so the pool
continues to operate with fewer than the target number of
runnable threads, which might not ensure progress.
- keepAliveTime

- the elapsed time since last use before
a thread is terminated (and then later replaced if needed).
For the default value, use

60, TimeUnit.SECONDS

.
- unit

- the time unit for the

keepAliveTime

argument

**Throws:**
- IllegalArgumentException

- if parallelism is less than or
equal to zero, or is greater than implementation limit,
or if maximumPoolSize is less than parallelism,
of if the keepAliveTime is less than or equal to zero.
- NullPointerException

- if the factory is null
- SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

**Since:**
- 9

---

### Method Details

#### public static
ForkJoinPool
commonPool()

Returns the common pool instance. This pool is statically
constructed; its run state is unaffected by attempts to

shutdown()

or

shutdownNow()

. However this pool and any
ongoing processing are automatically terminated upon program

System.exit(int)

. Any program that relies on asynchronous
task processing to complete before program termination should
invoke

commonPool().

awaitQuiescence

,
before exit.

**Returns:**
- the common pool instance

**Since:**
- 1.8

---

#### public <T> T invoke​(
ForkJoinTask
<T> task)

Performs the given task, returning its result upon completion.
If the computation encounters an unchecked Exception or Error,
it is rethrown as the outcome of this invocation. Rethrown
exceptions behave in the same way as regular exceptions, but,
when possible, contain stack traces (as displayed for example
using

ex.printStackTrace()

) of both the current thread
as well as the thread actually encountering the exception;
minimally only the latter.

**Parameters:**
- task

- the task

**Returns:**
- the task's result

**Throws:**
- NullPointerException

- if the task is null
- RejectedExecutionException

- if the task cannot be
scheduled for execution

**Type Parameters:**
- T

- the type of the task's result

---

#### public void execute​(
ForkJoinTask
<?> task)

Arranges for (asynchronous) execution of the given task.

**Parameters:**
- task

- the task

**Throws:**
- NullPointerException

- if the task is null
- RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### public void execute​(
Runnable
task)

Description copied from interface:

Executor

**Parameters:**
- task

- the runnable task

**Throws:**
- NullPointerException

- if the task is null
- RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### public <T>
ForkJoinTask
<T> submit​(
ForkJoinTask
<T> task)

Submits a ForkJoinTask for execution.

**Parameters:**
- task

- the task to submit

**Returns:**
- the task

**Throws:**
- NullPointerException

- if the task is null
- RejectedExecutionException

- if the task cannot be
scheduled for execution

**Type Parameters:**
- T

- the type of the task's result

---

#### public <T>
ForkJoinTask
<T> submit​(
Callable
<T> task)

Description copied from interface:

ExecutorService

**Specified by:**
- submit

in interface

ExecutorService

**Overrides:**
- submit

in class

AbstractExecutorService

**Parameters:**
- task

- the task to submit

**Returns:**
- a Future representing pending completion of the task

**Throws:**
- NullPointerException

- if the task is null
- RejectedExecutionException

- if the task cannot be
scheduled for execution

**Type Parameters:**
- T

- the type of the task's result

---

#### public <T>
ForkJoinTask
<T> submit​(
Runnable
task,
T result)

Description copied from interface:

ExecutorService

**Specified by:**
- submit

in interface

ExecutorService

**Overrides:**
- submit

in class

AbstractExecutorService

**Parameters:**
- task

- the task to submit
- result

- the result to return

**Returns:**
- a Future representing pending completion of the task

**Throws:**
- NullPointerException

- if the task is null
- RejectedExecutionException

- if the task cannot be
scheduled for execution

**Type Parameters:**
- T

- the type of the result

---

#### public
ForkJoinTask
<?> submit​(
Runnable
task)

Description copied from interface:

ExecutorService

**Specified by:**
- submit

in interface

ExecutorService

**Overrides:**
- submit

in class

AbstractExecutorService

**Parameters:**
- task

- the task to submit

**Returns:**
- a Future representing pending completion of the task

**Throws:**
- NullPointerException

- if the task is null
- RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### public <T>
List
<
Future
<T>> invokeAll​(
Collection
<? extends
Callable
<T>> tasks)

Description copied from interface:

ExecutorService

**Parameters:**
- tasks

- the collection of tasks

**Returns:**
- a list of Futures representing the tasks, in the same
sequential order as produced by the iterator for the
given task list, each of which has completed

**Throws:**
- NullPointerException

- if tasks or any of its elements are

null
- RejectedExecutionException

- if any task cannot be
scheduled for execution

**Type Parameters:**
- T

- the type of the values returned from the tasks

---

#### public
ForkJoinPool.ForkJoinWorkerThreadFactory
getFactory()

Returns the factory used for constructing new workers.

**Returns:**
- the factory used for constructing new workers

---

#### public
Thread.UncaughtExceptionHandler
getUncaughtExceptionHandler()

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

**Returns:**
- the handler, or

null

if none

---

#### public int getParallelism()

Returns the targeted parallelism level of this pool.

**Returns:**
- the targeted parallelism level of this pool

---

#### public static int getCommonPoolParallelism()

Returns the targeted parallelism level of the common pool.

**Returns:**
- the targeted parallelism level of the common pool

**Since:**
- 1.8

---

#### public int getPoolSize()

Returns the number of worker threads that have started but not
yet terminated. The result returned by this method may differ
from

getParallelism()

when threads are created to
maintain parallelism when others are cooperatively blocked.

**Returns:**
- the number of worker threads

---

#### public boolean getAsyncMode()

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

**Returns:**
- true

if this pool uses async mode

---

#### public int getRunningThreadCount()

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization. This method may overestimate the
number of running threads.

**Returns:**
- the number of worker threads

---

#### public int getActiveThreadCount()

Returns an estimate of the number of threads that are currently
stealing or executing tasks. This method may overestimate the
number of active threads.

**Returns:**
- the number of active threads

---

#### public boolean isQuiescent()

Returns

true

if all worker threads are currently idle.
An idle worker is one that cannot obtain a task to execute
because none are available to steal from other threads, and
there are no pending submissions to the pool. This method is
conservative; it might not return

true

immediately upon
idleness of all threads, but will eventually become true if
threads remain inactive.

**Returns:**
- true

if all threads are currently idle

---

#### public long getStealCount()

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another. The reported value
underestimates the actual total number of steals when the pool
is not quiescent. This value may be useful for monitoring and
tuning fork/join programs: in general, steal counts should be
high enough to keep threads busy, but low enough to avoid
overhead and contention across threads.

**Returns:**
- the number of steals

---

#### public long getQueuedTaskCount()

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing). This value is only
an approximation, obtained by iterating across all threads in
the pool. This method may be useful for tuning task
granularities.

**Returns:**
- the number of queued tasks

---

#### public int getQueuedSubmissionCount()

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing. This method may take
time proportional to the number of submissions.

**Returns:**
- the number of queued submissions

---

#### public boolean hasQueuedSubmissions()

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

**Returns:**
- true

if there are any queued submissions

---

#### protected
ForkJoinTask
<?> pollSubmission()

Removes and returns the next unexecuted submission if one is
available. This method may be useful in extensions to this
class that re-assign work in systems with multiple pools.

**Returns:**
- the next submission, or

null

if none

---

#### protected int drainTasksTo​(
Collection
<? super
ForkJoinTask
<?>> c)

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status. These may include
artificially generated or wrapped tasks. This method is
designed to be invoked only when the pool is known to be
quiescent. Invocations at other times may not remove all
tasks. A failure encountered while attempting to add elements
to collection

c

may result in elements being in
neither, either or both collections when the associated
exception is thrown. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress.

**Parameters:**
- c

- the collection to transfer elements into

**Returns:**
- the number of elements transferred

---

#### public
String
toString()

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string identifying this pool, as well as its state

---

#### public void shutdown()

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted. Invocation has no effect on execution state if this
is the

commonPool()

, and no additional effect if
already shut down. Tasks that are in the process of being
submitted concurrently during the course of this method may or
may not be rejected.

**Throws:**
- SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### public
List
<
Runnable
> shutdownNow()

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks. Invocation has no effect on
execution state if this is the

commonPool()

, and no
additional effect if already shut down. Otherwise, tasks that
are in the process of being submitted or executed concurrently
during the course of this method may or may not be
rejected. This method cancels both existing and unexecuted
tasks, in order to permit termination in the presence of task
dependencies. So the method always returns an empty list
(unlike the case for some other Executors).

**Returns:**
- an empty list

**Throws:**
- SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### public boolean isTerminated()

Returns

true

if all tasks have completed following shut down.

**Returns:**
- true

if all tasks have completed following shut down

---

#### public boolean isTerminating()

Returns

true

if the process of termination has
commenced but not yet completed. This method may be useful for
debugging. A return of

true

reported a sufficient
period after shutdown may indicate that submitted tasks have
ignored or suppressed interruption, or are waiting for I/O,
causing this executor not to properly terminate. (See the
advisory notes for class

ForkJoinTask

stating that
tasks should not normally entail blocking operations. But if
they do, they must abort them on interrupt.)

**Returns:**
- true

if terminating but not yet terminated

---

#### public boolean isShutdown()

Returns

true

if this pool has been shut down.

**Returns:**
- true

if this pool has been shut down

---

#### public boolean awaitTermination​(long timeout,

TimeUnit
unit)
throws
InterruptedException

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first. Because the

commonPool()

never terminates until program shutdown, when
applied to the common pool, this method is equivalent to

awaitQuiescence(long, TimeUnit)

but always returns

false

.

**Parameters:**
- timeout

- the maximum time to wait
- unit

- the time unit of the timeout argument

**Returns:**
- true

if this executor terminated and

false

if the timeout elapsed before termination

**Throws:**
- InterruptedException

- if interrupted while waiting

---

#### public boolean awaitQuiescence​(long timeout,

TimeUnit
unit)

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

. Otherwise,
waits and/or attempts to assist performing tasks until this
pool

isQuiescent()

or the indicated timeout elapses.

**Parameters:**
- timeout

- the maximum time to wait
- unit

- the time unit of the timeout argument

**Returns:**
- true

if quiescent;

false

if the
timeout elapsed.

---

#### public static void managedBlock​(
ForkJoinPool.ManagedBlocker
blocker)
throws
InterruptedException

Runs the given possibly blocking task. When

running in a ForkJoinPool

, this
method possibly arranges for a spare thread to be activated if
necessary to ensure sufficient parallelism while the current
thread is blocked in

blocker.block()

.

This method repeatedly calls

blocker.isReleasable()

and

blocker.block()

until either method returns

true

.
Every call to

blocker.block()

is preceded by a call to

blocker.isReleasable()

that returned

false

.

If not running in a ForkJoinPool, this method is
behaviorally equivalent to

```java
while (!blocker.isReleasable())
if (blocker.block())
break;
```

If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to

blocker.block()

.

**Parameters:**
- blocker

- the blocker task

**Throws:**
- InterruptedException

- if

blocker.block()

did so

---

### Additional Sections

#### Class ForkJoinPool

java.lang.Object

- java.util.concurrent.AbstractExecutorService
- - java.util.concurrent.ForkJoinPool

java.util.concurrent.AbstractExecutorService

- java.util.concurrent.ForkJoinPool

java.util.concurrent.ForkJoinPool

**All Implemented Interfaces:** Executor

,

ExecutorService

```java
public class
ForkJoinPool

extends
AbstractExecutorService
```

An

ExecutorService

for running

ForkJoinTask

s.
A

ForkJoinPool

provides the entry point for submissions
from non-

ForkJoinTask

clients, as well as management and
monitoring operations.

A

ForkJoinPool

differs from other kinds of

ExecutorService

mainly by virtue of employing

work-stealing

: all threads in the pool attempt to find and
execute tasks submitted to the pool and/or created by other active
tasks (eventually blocking waiting for work if none exist). This
enables efficient processing when most tasks spawn other subtasks
(as do most

ForkJoinTask

s), as well as when many small
tasks are submitted to the pool from external clients. Especially
when setting

asyncMode

to true in constructors,

ForkJoinPool

s may also be appropriate for use with event-style
tasks that are never joined. All worker threads are initialized
with

Thread.isDaemon()

set

true

.

A static

commonPool()

is available and appropriate for
most applications. The common pool is used by any ForkJoinTask that
is not explicitly submitted to a specified pool. Using the common
pool normally reduces resource usage (its threads are slowly
reclaimed during periods of non-use, and reinstated upon subsequent
use).

For applications that require separate or custom pools, a

ForkJoinPool

may be constructed with a given target parallelism
level; by default, equal to the number of available processors.
The pool attempts to maintain enough active (or available) threads
by dynamically adding, suspending, or resuming internal worker
threads, even if some tasks are stalled waiting to join others.
However, no such adjustments are guaranteed in the face of blocked
I/O or other unmanaged synchronization. The nested

ForkJoinPool.ManagedBlocker

interface enables extension of the kinds of
synchronization accommodated. The default policies may be
overridden using a constructor with parameters corresponding to
those documented in class

ThreadPoolExecutor

.

In addition to execution and lifecycle control methods, this
class provides status check methods (for example

getStealCount()

) that are intended to aid in developing,
tuning, and monitoring fork/join applications. Also, method

toString()

returns indications of pool state in a
convenient form for informal monitoring.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

**Since:** 1.7

public class

ForkJoinPool

extends

AbstractExecutorService

An

ExecutorService

for running

ForkJoinTask

s.
A

ForkJoinPool

provides the entry point for submissions
from non-

ForkJoinTask

clients, as well as management and
monitoring operations.

A

ForkJoinPool

differs from other kinds of

ExecutorService

mainly by virtue of employing

work-stealing

: all threads in the pool attempt to find and
execute tasks submitted to the pool and/or created by other active
tasks (eventually blocking waiting for work if none exist). This
enables efficient processing when most tasks spawn other subtasks
(as do most

ForkJoinTask

s), as well as when many small
tasks are submitted to the pool from external clients. Especially
when setting

asyncMode

to true in constructors,

ForkJoinPool

s may also be appropriate for use with event-style
tasks that are never joined. All worker threads are initialized
with

Thread.isDaemon()

set

true

.

A static

commonPool()

is available and appropriate for
most applications. The common pool is used by any ForkJoinTask that
is not explicitly submitted to a specified pool. Using the common
pool normally reduces resource usage (its threads are slowly
reclaimed during periods of non-use, and reinstated upon subsequent
use).

For applications that require separate or custom pools, a

ForkJoinPool

may be constructed with a given target parallelism
level; by default, equal to the number of available processors.
The pool attempts to maintain enough active (or available) threads
by dynamically adding, suspending, or resuming internal worker
threads, even if some tasks are stalled waiting to join others.
However, no such adjustments are guaranteed in the face of blocked
I/O or other unmanaged synchronization. The nested

ForkJoinPool.ManagedBlocker

interface enables extension of the kinds of
synchronization accommodated. The default policies may be
overridden using a constructor with parameters corresponding to
those documented in class

ThreadPoolExecutor

.

In addition to execution and lifecycle control methods, this
class provides status check methods (for example

getStealCount()

) that are intended to aid in developing,
tuning, and monitoring fork/join applications. Also, method

toString()

returns indications of pool state in a
convenient form for informal monitoring.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

A

ForkJoinPool

differs from other kinds of

ExecutorService

mainly by virtue of employing

work-stealing

: all threads in the pool attempt to find and
execute tasks submitted to the pool and/or created by other active
tasks (eventually blocking waiting for work if none exist). This
enables efficient processing when most tasks spawn other subtasks
(as do most

ForkJoinTask

s), as well as when many small
tasks are submitted to the pool from external clients. Especially
when setting

asyncMode

to true in constructors,

ForkJoinPool

s may also be appropriate for use with event-style
tasks that are never joined. All worker threads are initialized
with

Thread.isDaemon()

set

true

.

A static

commonPool()

is available and appropriate for
most applications. The common pool is used by any ForkJoinTask that
is not explicitly submitted to a specified pool. Using the common
pool normally reduces resource usage (its threads are slowly
reclaimed during periods of non-use, and reinstated upon subsequent
use).

For applications that require separate or custom pools, a

ForkJoinPool

may be constructed with a given target parallelism
level; by default, equal to the number of available processors.
The pool attempts to maintain enough active (or available) threads
by dynamically adding, suspending, or resuming internal worker
threads, even if some tasks are stalled waiting to join others.
However, no such adjustments are guaranteed in the face of blocked
I/O or other unmanaged synchronization. The nested

ForkJoinPool.ManagedBlocker

interface enables extension of the kinds of
synchronization accommodated. The default policies may be
overridden using a constructor with parameters corresponding to
those documented in class

ThreadPoolExecutor

.

In addition to execution and lifecycle control methods, this
class provides status check methods (for example

getStealCount()

) that are intended to aid in developing,
tuning, and monitoring fork/join applications. Also, method

toString()

returns indications of pool state in a
convenient form for informal monitoring.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

A static

commonPool()

is available and appropriate for
most applications. The common pool is used by any ForkJoinTask that
is not explicitly submitted to a specified pool. Using the common
pool normally reduces resource usage (its threads are slowly
reclaimed during periods of non-use, and reinstated upon subsequent
use).

For applications that require separate or custom pools, a

ForkJoinPool

may be constructed with a given target parallelism
level; by default, equal to the number of available processors.
The pool attempts to maintain enough active (or available) threads
by dynamically adding, suspending, or resuming internal worker
threads, even if some tasks are stalled waiting to join others.
However, no such adjustments are guaranteed in the face of blocked
I/O or other unmanaged synchronization. The nested

ForkJoinPool.ManagedBlocker

interface enables extension of the kinds of
synchronization accommodated. The default policies may be
overridden using a constructor with parameters corresponding to
those documented in class

ThreadPoolExecutor

.

In addition to execution and lifecycle control methods, this
class provides status check methods (for example

getStealCount()

) that are intended to aid in developing,
tuning, and monitoring fork/join applications. Also, method

toString()

returns indications of pool state in a
convenient form for informal monitoring.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

For applications that require separate or custom pools, a

ForkJoinPool

may be constructed with a given target parallelism
level; by default, equal to the number of available processors.
The pool attempts to maintain enough active (or available) threads
by dynamically adding, suspending, or resuming internal worker
threads, even if some tasks are stalled waiting to join others.
However, no such adjustments are guaranteed in the face of blocked
I/O or other unmanaged synchronization. The nested

ForkJoinPool.ManagedBlocker

interface enables extension of the kinds of
synchronization accommodated. The default policies may be
overridden using a constructor with parameters corresponding to
those documented in class

ThreadPoolExecutor

.

In addition to execution and lifecycle control methods, this
class provides status check methods (for example

getStealCount()

) that are intended to aid in developing,
tuning, and monitoring fork/join applications. Also, method

toString()

returns indications of pool state in a
convenient form for informal monitoring.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

In addition to execution and lifecycle control methods, this
class provides status check methods (for example

getStealCount()

) that are intended to aid in developing,
tuning, and monitoring fork/join applications. Also, method

toString()

returns indications of pool state in a
convenient form for informal monitoring.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

As is the case with other ExecutorServices, there are three
main task execution methods summarized in the following table.
These are designed to be used primarily by clients not already
engaged in fork/join computations in the current pool. The main
forms of these methods accept instances of

ForkJoinTask

,
but overloaded forms also allow mixed execution of plain

Runnable

- or

Callable

- based activities as well. However,
tasks that are already executing in a pool should normally instead
use the within-computation forms listed in the table unless using
async event-style tasks that are not usually joined, in which case
there is little difference among choice of methods.

Summary of task execution methods

Call from non-fork/join clients

Call from within fork/join computations

Arrange async execution

execute(ForkJoinTask)

ForkJoinTask.fork()

Await and obtain result

invoke(ForkJoinTask)

ForkJoinTask.invoke()

Arrange exec and obtain Future

submit(ForkJoinTask)

ForkJoinTask.fork()

(ForkJoinTasks

are

Futures)

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

The parameters used to construct the common pool may be controlled by
setting the following

system properties

:

- java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

If no thread factory is supplied via a system property, then the
common pool uses a factory that uses the system class loader as the

thread context class loader

.
In addition, if a

SecurityManager

is present, then
the common pool uses a factory supplying threads that have no

Permissions

enabled.

Upon any error in establishing these settings, default parameters
are used. It is possible to disable or limit the use of threads in
the common pool by setting the parallelism property to zero, and/or
using a factory that may return

null

. However doing so may
cause unjoined tasks to never be executed.

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

java.util.concurrent.ForkJoinPool.common.parallelism

- the parallelism level, a non-negative integer

java.util.concurrent.ForkJoinPool.common.threadFactory

- the class name of a

ForkJoinPool.ForkJoinWorkerThreadFactory

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.exceptionHandler

- the class name of a

Thread.UncaughtExceptionHandler

.
The

system class loader

is used to load this class.

java.util.concurrent.ForkJoinPool.common.maximumSpares

- the maximum number of allowed extra threads to maintain target
parallelism (default 256).

Implementation notes

: This implementation restricts the
maximum number of running threads to 32767. Attempts to create
pools with greater than the maximum number result in

IllegalArgumentException

.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

This implementation rejects submitted tasks (that is, by throwing

RejectedExecutionException

) only when the pool is shut down
or internal resources have been exhausted.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

ForkJoinPool.ForkJoinWorkerThreadFactory

Factory for creating new

ForkJoinWorkerThread

s.

static interface

ForkJoinPool.ManagedBlocker

Interface for extending managed parallelism for tasks running
in

ForkJoinPool

s.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ForkJoinPool.ForkJoinWorkerThreadFactory

defaultForkJoinWorkerThreadFactory

Creates a new ForkJoinWorkerThread.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ForkJoinPool

()

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

ForkJoinPool

​(int parallelism)

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

ForkJoinPool

​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory

factory,

Thread.UncaughtExceptionHandler

handler,
boolean asyncMode)

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

ForkJoinPool

​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory

factory,

Thread.UncaughtExceptionHandler

handler,
boolean asyncMode,
int corePoolSize,
int maximumPoolSize,
int minimumRunnable,

Predicate

<? super

ForkJoinPool

> saturate,
long keepAliveTime,

TimeUnit

unit)

Creates a

ForkJoinPool

with the given parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

awaitQuiescence

​(long timeout,

TimeUnit

unit)

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

.

boolean

awaitTermination

​(long timeout,

TimeUnit

unit)

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first.

static

ForkJoinPool

commonPool

()

Returns the common pool instance.

protected int

drainTasksTo

​(

Collection

<? super

ForkJoinTask

<?>> c)

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status.

void

execute

​(

Runnable

task)

Executes the given command at some time in the future.

void

execute

​(

ForkJoinTask

<?> task)

Arranges for (asynchronous) execution of the given task.

int

getActiveThreadCount

()

Returns an estimate of the number of threads that are currently
stealing or executing tasks.

boolean

getAsyncMode

()

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

static int

getCommonPoolParallelism

()

Returns the targeted parallelism level of the common pool.

ForkJoinPool.ForkJoinWorkerThreadFactory

getFactory

()

Returns the factory used for constructing new workers.

int

getParallelism

()

Returns the targeted parallelism level of this pool.

int

getPoolSize

()

Returns the number of worker threads that have started but not
yet terminated.

int

getQueuedSubmissionCount

()

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing.

long

getQueuedTaskCount

()

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing).

int

getRunningThreadCount

()

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization.

long

getStealCount

()

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another.

Thread.UncaughtExceptionHandler

getUncaughtExceptionHandler

()

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

boolean

hasQueuedSubmissions

()

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

<T> T

invoke

​(

ForkJoinTask

<T> task)

Performs the given task, returning its result upon completion.

<T>

List

<

Future

<T>>

invokeAll

​(

Collection

<? extends

Callable

<T>> tasks)

Executes the given tasks, returning a list of Futures holding
their status and results when all complete.

boolean

isQuiescent

()

Returns

true

if all worker threads are currently idle.

boolean

isShutdown

()

Returns

true

if this pool has been shut down.

boolean

isTerminated

()

Returns

true

if all tasks have completed following shut down.

boolean

isTerminating

()

Returns

true

if the process of termination has
commenced but not yet completed.

static void

managedBlock

​(

ForkJoinPool.ManagedBlocker

blocker)

Runs the given possibly blocking task.

protected

ForkJoinTask

<?>

pollSubmission

()

Removes and returns the next unexecuted submission if one is
available.

void

shutdown

()

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted.

List

<

Runnable

>

shutdownNow

()

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks.

ForkJoinTask

<?>

submit

​(

Runnable

task)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

ForkJoinTask

<T>

submit

​(

Runnable

task,
T result)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

ForkJoinTask

<T>

submit

​(

Callable

<T> task)

Submits a value-returning task for execution and returns a
Future representing the pending results of the task.

<T>

ForkJoinTask

<T>

submit

​(

ForkJoinTask

<T> task)

Submits a ForkJoinTask for execution.

String

toString

()

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

- Methods declared in class java.util.concurrent.

AbstractExecutorService

newTaskFor

,

newTaskFor

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

ExecutorService

invokeAll

,

invokeAny

,

invokeAny

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

ForkJoinPool.ForkJoinWorkerThreadFactory

Factory for creating new

ForkJoinWorkerThread

s.

static interface

ForkJoinPool.ManagedBlocker

Interface for extending managed parallelism for tasks running
in

ForkJoinPool

s.

---

#### Nested Class Summary

Factory for creating new

ForkJoinWorkerThread

s.

Interface for extending managed parallelism for tasks running
in

ForkJoinPool

s.

Field Summary

Fields

Modifier and Type

Field

Description

static

ForkJoinPool.ForkJoinWorkerThreadFactory

defaultForkJoinWorkerThreadFactory

Creates a new ForkJoinWorkerThread.

---

#### Field Summary

Creates a new ForkJoinWorkerThread.

Constructor Summary

Constructors

Constructor

Description

ForkJoinPool

()

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

ForkJoinPool

​(int parallelism)

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

ForkJoinPool

​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory

factory,

Thread.UncaughtExceptionHandler

handler,
boolean asyncMode)

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

ForkJoinPool

​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory

factory,

Thread.UncaughtExceptionHandler

handler,
boolean asyncMode,
int corePoolSize,
int maximumPoolSize,
int minimumRunnable,

Predicate

<? super

ForkJoinPool

> saturate,
long keepAliveTime,

TimeUnit

unit)

Creates a

ForkJoinPool

with the given parameters.

---

#### Constructor Summary

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

Creates a

ForkJoinPool

with the given parameters.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

awaitQuiescence

​(long timeout,

TimeUnit

unit)

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

.

boolean

awaitTermination

​(long timeout,

TimeUnit

unit)

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first.

static

ForkJoinPool

commonPool

()

Returns the common pool instance.

protected int

drainTasksTo

​(

Collection

<? super

ForkJoinTask

<?>> c)

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status.

void

execute

​(

Runnable

task)

Executes the given command at some time in the future.

void

execute

​(

ForkJoinTask

<?> task)

Arranges for (asynchronous) execution of the given task.

int

getActiveThreadCount

()

Returns an estimate of the number of threads that are currently
stealing or executing tasks.

boolean

getAsyncMode

()

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

static int

getCommonPoolParallelism

()

Returns the targeted parallelism level of the common pool.

ForkJoinPool.ForkJoinWorkerThreadFactory

getFactory

()

Returns the factory used for constructing new workers.

int

getParallelism

()

Returns the targeted parallelism level of this pool.

int

getPoolSize

()

Returns the number of worker threads that have started but not
yet terminated.

int

getQueuedSubmissionCount

()

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing.

long

getQueuedTaskCount

()

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing).

int

getRunningThreadCount

()

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization.

long

getStealCount

()

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another.

Thread.UncaughtExceptionHandler

getUncaughtExceptionHandler

()

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

boolean

hasQueuedSubmissions

()

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

<T> T

invoke

​(

ForkJoinTask

<T> task)

Performs the given task, returning its result upon completion.

<T>

List

<

Future

<T>>

invokeAll

​(

Collection

<? extends

Callable

<T>> tasks)

Executes the given tasks, returning a list of Futures holding
their status and results when all complete.

boolean

isQuiescent

()

Returns

true

if all worker threads are currently idle.

boolean

isShutdown

()

Returns

true

if this pool has been shut down.

boolean

isTerminated

()

Returns

true

if all tasks have completed following shut down.

boolean

isTerminating

()

Returns

true

if the process of termination has
commenced but not yet completed.

static void

managedBlock

​(

ForkJoinPool.ManagedBlocker

blocker)

Runs the given possibly blocking task.

protected

ForkJoinTask

<?>

pollSubmission

()

Removes and returns the next unexecuted submission if one is
available.

void

shutdown

()

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted.

List

<

Runnable

>

shutdownNow

()

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks.

ForkJoinTask

<?>

submit

​(

Runnable

task)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

ForkJoinTask

<T>

submit

​(

Runnable

task,
T result)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

ForkJoinTask

<T>

submit

​(

Callable

<T> task)

Submits a value-returning task for execution and returns a
Future representing the pending results of the task.

<T>

ForkJoinTask

<T>

submit

​(

ForkJoinTask

<T> task)

Submits a ForkJoinTask for execution.

String

toString

()

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

- Methods declared in class java.util.concurrent.

AbstractExecutorService

newTaskFor

,

newTaskFor

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

ExecutorService

invokeAll

,

invokeAny

,

invokeAny

---

#### Method Summary

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

.

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first.

Returns the common pool instance.

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status.

Executes the given command at some time in the future.

Arranges for (asynchronous) execution of the given task.

Returns an estimate of the number of threads that are currently
stealing or executing tasks.

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

Returns the targeted parallelism level of the common pool.

Returns the factory used for constructing new workers.

Returns the targeted parallelism level of this pool.

Returns the number of worker threads that have started but not
yet terminated.

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing.

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing).

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization.

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another.

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

Performs the given task, returning its result upon completion.

Executes the given tasks, returning a list of Futures holding
their status and results when all complete.

Returns

true

if all worker threads are currently idle.

Returns

true

if this pool has been shut down.

Returns

true

if all tasks have completed following shut down.

Returns

true

if the process of termination has
commenced but not yet completed.

Runs the given possibly blocking task.

Removes and returns the next unexecuted submission if one is
available.

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted.

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks.

Submits a Runnable task for execution and returns a Future
representing that task.

Submits a value-returning task for execution and returns a
Future representing the pending results of the task.

Submits a ForkJoinTask for execution.

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

Methods declared in class java.util.concurrent.

AbstractExecutorService

newTaskFor

,

newTaskFor

---

#### Methods declared in class java.util.concurrent. AbstractExecutorService

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

ExecutorService

invokeAll

,

invokeAny

,

invokeAny

---

#### Methods declared in interface java.util.concurrent. ExecutorService

============ FIELD DETAIL ===========

- Field Detail

- defaultForkJoinWorkerThreadFactory

```java
public static final
ForkJoinPool.ForkJoinWorkerThreadFactory
defaultForkJoinWorkerThreadFactory
```

Creates a new ForkJoinWorkerThread. This factory is used unless
overridden in ForkJoinPool constructors.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ForkJoinPool

```java
public ForkJoinPool()
```

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- ForkJoinPool

```java
public ForkJoinPool​(int parallelism)
```

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

**Parameters:** parallelism

- the parallelism level
**Throws:** IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- ForkJoinPool

```java
public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode)
```

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Parameters:** parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
**Parameters:** factory

- the factory for creating new threads. For default value,
use

defaultForkJoinWorkerThreadFactory

.
**Parameters:** handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while executing
tasks. For default value, use

null

.
**Parameters:** asyncMode

- if true,
establishes local first-in-first-out scheduling mode for forked
tasks that are never joined. This mode may be more appropriate
than default locally stack-based mode in applications in which
worker threads only process event-style asynchronous tasks.
For default value, use

false

.
**Throws:** IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
**Throws:** NullPointerException

- if the factory is null
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- ForkJoinPool

```java
public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode,
int corePoolSize,
int maximumPoolSize,
int minimumRunnable,

Predicate
<? super
ForkJoinPool
> saturate,
long keepAliveTime,

TimeUnit
unit)
```

Creates a

ForkJoinPool

with the given parameters.

**Parameters:** parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
**Parameters:** factory

- the factory for creating new threads. For
default value, use

defaultForkJoinWorkerThreadFactory

.
**Parameters:** handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while
executing tasks. For default value, use

null

.
**Parameters:** asyncMode

- if true, establishes local first-in-first-out
scheduling mode for forked tasks that are never joined. This
mode may be more appropriate than default locally stack-based
mode in applications in which worker threads only process
event-style asynchronous tasks. For default value, use

false

.
**Parameters:** corePoolSize

- the number of threads to keep in the pool
(unless timed out after an elapsed keep-alive). Normally (and
by default) this is the same value as the parallelism level,
but may be set to a larger value to reduce dynamic overhead if
tasks regularly block. Using a smaller value (for example

0

) has the same effect as the default.
**Parameters:** maximumPoolSize

- the maximum number of threads allowed.
When the maximum is reached, attempts to replace blocked
threads fail. (However, because creation and termination of
different threads may overlap, and may be managed by the given
thread factory, this value may be transiently exceeded.) To
arrange the same value as is used by default for the common
pool, use

256

plus the

parallelism

level. (By
default, the common pool allows a maximum of 256 spare
threads.) Using a value (for example

Integer.MAX_VALUE

) larger than the implementation's total
thread limit has the same effect as using this limit (which is
the default).
**Parameters:** minimumRunnable

- the minimum allowed number of core
threads not blocked by a join or

ForkJoinPool.ManagedBlocker

. To
ensure progress, when too few unblocked threads exist and
unexecuted tasks may exist, new threads are constructed, up to
the given maximumPoolSize. For the default value, use

1

, that ensures liveness. A larger value might improve
throughput in the presence of blocked activities, but might
not, due to increased overhead. A value of zero may be
acceptable when submitted tasks cannot have dependencies
requiring additional threads.
**Parameters:** saturate

- if non-null, a predicate invoked upon attempts
to create more than the maximum total allowed threads. By
default, when a thread is about to block on a join or

ForkJoinPool.ManagedBlocker

, but cannot be replaced because the
maximumPoolSize would be exceeded, a

RejectedExecutionException

is thrown. But if this predicate
returns

true

, then no exception is thrown, so the pool
continues to operate with fewer than the target number of
runnable threads, which might not ensure progress.
**Parameters:** keepAliveTime

- the elapsed time since last use before
a thread is terminated (and then later replaced if needed).
For the default value, use

60, TimeUnit.SECONDS

.
**Parameters:** unit

- the time unit for the

keepAliveTime

argument
**Throws:** IllegalArgumentException

- if parallelism is less than or
equal to zero, or is greater than implementation limit,
or if maximumPoolSize is less than parallelism,
of if the keepAliveTime is less than or equal to zero.
**Throws:** NullPointerException

- if the factory is null
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- commonPool

```java
public static
ForkJoinPool
commonPool()
```

Returns the common pool instance. This pool is statically
constructed; its run state is unaffected by attempts to

shutdown()

or

shutdownNow()

. However this pool and any
ongoing processing are automatically terminated upon program

System.exit(int)

. Any program that relies on asynchronous
task processing to complete before program termination should
invoke

commonPool().

awaitQuiescence

,
before exit.

**Returns:** the common pool instance
**Since:** 1.8

- invoke

```java
public <T> T invoke​(
ForkJoinTask
<T> task)
```

Performs the given task, returning its result upon completion.
If the computation encounters an unchecked Exception or Error,
it is rethrown as the outcome of this invocation. Rethrown
exceptions behave in the same way as regular exceptions, but,
when possible, contain stack traces (as displayed for example
using

ex.printStackTrace()

) of both the current thread
as well as the thread actually encountering the exception;
minimally only the latter.

**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task
**Returns:** the task's result
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- execute

```java
public void execute​(
ForkJoinTask
<?> task)
```

Arranges for (asynchronous) execution of the given task.

**Parameters:** task

- the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- execute

```java
public void execute​(
Runnable
task)
```

Description copied from interface:

Executor

Executes the given command at some time in the future. The command
may execute in a new thread, in a pooled thread, or in the calling
thread, at the discretion of the

Executor

implementation.

**Parameters:** task

- the runnable task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public <T>
ForkJoinTask
<T> submit​(
ForkJoinTask
<T> task)
```

Submits a ForkJoinTask for execution.

**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public <T>
ForkJoinTask
<T> submit​(
Callable
<T> task)
```

Description copied from interface:

ExecutorService

Submits a value-returning task for execution and returns a
Future representing the pending results of the task. The
Future's

get

method will return the task's result upon
successful completion.

If you would like to immediately block waiting
for a task, you can use constructions of the form

result = exec.submit(aCallable).get();

Note: The

Executors

class includes a set of methods
that can convert some other common closure-like objects,
for example,

PrivilegedAction

to

Callable

form so they can be submitted.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public <T>
ForkJoinTask
<T> submit​(
Runnable
task,
T result)
```

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return the given result upon successful completion.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public
ForkJoinTask
<?> submit​(
Runnable
task)
```

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return

null

upon

successful

completion.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- invokeAll

```java
public <T>
List
<
Future
<T>> invokeAll​(
Collection
<? extends
Callable
<T>> tasks)
```

Description copied from interface:

ExecutorService

Executes the given tasks, returning a list of Futures holding
their status and results when all complete.

Future.isDone()

is

true

for each
element of the returned list.
Note that a

completed

task could have
terminated either normally or by throwing an exception.
The results of this method are undefined if the given
collection is modified while this operation is in progress.

**Type Parameters:** T

- the type of the values returned from the tasks
**Parameters:** tasks

- the collection of tasks
**Returns:** a list of Futures representing the tasks, in the same
sequential order as produced by the iterator for the
given task list, each of which has completed
**Throws:** NullPointerException

- if tasks or any of its elements are

null
**Throws:** RejectedExecutionException

- if any task cannot be
scheduled for execution

- getFactory

```java
public
ForkJoinPool.ForkJoinWorkerThreadFactory
getFactory()
```

Returns the factory used for constructing new workers.

**Returns:** the factory used for constructing new workers

- getUncaughtExceptionHandler

```java
public
Thread.UncaughtExceptionHandler
getUncaughtExceptionHandler()
```

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

**Returns:** the handler, or

null

if none

- getParallelism

```java
public int getParallelism()
```

Returns the targeted parallelism level of this pool.

**Returns:** the targeted parallelism level of this pool

- getCommonPoolParallelism

```java
public static int getCommonPoolParallelism()
```

Returns the targeted parallelism level of the common pool.

**Returns:** the targeted parallelism level of the common pool
**Since:** 1.8

- getPoolSize

```java
public int getPoolSize()
```

Returns the number of worker threads that have started but not
yet terminated. The result returned by this method may differ
from

getParallelism()

when threads are created to
maintain parallelism when others are cooperatively blocked.

**Returns:** the number of worker threads

- getAsyncMode

```java
public boolean getAsyncMode()
```

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

**Returns:** true

if this pool uses async mode

- getRunningThreadCount

```java
public int getRunningThreadCount()
```

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization. This method may overestimate the
number of running threads.

**Returns:** the number of worker threads

- getActiveThreadCount

```java
public int getActiveThreadCount()
```

Returns an estimate of the number of threads that are currently
stealing or executing tasks. This method may overestimate the
number of active threads.

**Returns:** the number of active threads

- isQuiescent

```java
public boolean isQuiescent()
```

Returns

true

if all worker threads are currently idle.
An idle worker is one that cannot obtain a task to execute
because none are available to steal from other threads, and
there are no pending submissions to the pool. This method is
conservative; it might not return

true

immediately upon
idleness of all threads, but will eventually become true if
threads remain inactive.

**Returns:** true

if all threads are currently idle

- getStealCount

```java
public long getStealCount()
```

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another. The reported value
underestimates the actual total number of steals when the pool
is not quiescent. This value may be useful for monitoring and
tuning fork/join programs: in general, steal counts should be
high enough to keep threads busy, but low enough to avoid
overhead and contention across threads.

**Returns:** the number of steals

- getQueuedTaskCount

```java
public long getQueuedTaskCount()
```

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing). This value is only
an approximation, obtained by iterating across all threads in
the pool. This method may be useful for tuning task
granularities.

**Returns:** the number of queued tasks

- getQueuedSubmissionCount

```java
public int getQueuedSubmissionCount()
```

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing. This method may take
time proportional to the number of submissions.

**Returns:** the number of queued submissions

- hasQueuedSubmissions

```java
public boolean hasQueuedSubmissions()
```

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

**Returns:** true

if there are any queued submissions

- pollSubmission

```java
protected
ForkJoinTask
<?> pollSubmission()
```

Removes and returns the next unexecuted submission if one is
available. This method may be useful in extensions to this
class that re-assign work in systems with multiple pools.

**Returns:** the next submission, or

null

if none

- drainTasksTo

```java
protected int drainTasksTo​(
Collection
<? super
ForkJoinTask
<?>> c)
```

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status. These may include
artificially generated or wrapped tasks. This method is
designed to be invoked only when the pool is known to be
quiescent. Invocations at other times may not remove all
tasks. A failure encountered while attempting to add elements
to collection

c

may result in elements being in
neither, either or both collections when the associated
exception is thrown. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress.

**Parameters:** c

- the collection to transfer elements into
**Returns:** the number of elements transferred

- toString

```java
public
String
toString()
```

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this pool, as well as its state

- shutdown

```java
public void shutdown()
```

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted. Invocation has no effect on execution state if this
is the

commonPool()

, and no additional effect if
already shut down. Tasks that are in the process of being
submitted concurrently during the course of this method may or
may not be rejected.

**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- shutdownNow

```java
public
List
<
Runnable
> shutdownNow()
```

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks. Invocation has no effect on
execution state if this is the

commonPool()

, and no
additional effect if already shut down. Otherwise, tasks that
are in the process of being submitted or executed concurrently
during the course of this method may or may not be
rejected. This method cancels both existing and unexecuted
tasks, in order to permit termination in the presence of task
dependencies. So the method always returns an empty list
(unlike the case for some other Executors).

**Returns:** an empty list
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- isTerminated

```java
public boolean isTerminated()
```

Returns

true

if all tasks have completed following shut down.

**Returns:** true

if all tasks have completed following shut down

- isTerminating

```java
public boolean isTerminating()
```

Returns

true

if the process of termination has
commenced but not yet completed. This method may be useful for
debugging. A return of

true

reported a sufficient
period after shutdown may indicate that submitted tasks have
ignored or suppressed interruption, or are waiting for I/O,
causing this executor not to properly terminate. (See the
advisory notes for class

ForkJoinTask

stating that
tasks should not normally entail blocking operations. But if
they do, they must abort them on interrupt.)

**Returns:** true

if terminating but not yet terminated

- isShutdown

```java
public boolean isShutdown()
```

Returns

true

if this pool has been shut down.

**Returns:** true

if this pool has been shut down

- awaitTermination

```java
public boolean awaitTermination​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first. Because the

commonPool()

never terminates until program shutdown, when
applied to the common pool, this method is equivalent to

awaitQuiescence(long, TimeUnit)

but always returns

false

.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if this executor terminated and

false

if the timeout elapsed before termination
**Throws:** InterruptedException

- if interrupted while waiting

- awaitQuiescence

```java
public boolean awaitQuiescence​(long timeout,

TimeUnit
unit)
```

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

. Otherwise,
waits and/or attempts to assist performing tasks until this
pool

isQuiescent()

or the indicated timeout elapses.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if quiescent;

false

if the
timeout elapsed.

- managedBlock

```java
public static void managedBlock​(
ForkJoinPool.ManagedBlocker
blocker)
throws
InterruptedException
```

Runs the given possibly blocking task. When

running in a ForkJoinPool

, this
method possibly arranges for a spare thread to be activated if
necessary to ensure sufficient parallelism while the current
thread is blocked in

blocker.block()

.

This method repeatedly calls

blocker.isReleasable()

and

blocker.block()

until either method returns

true

.
Every call to

blocker.block()

is preceded by a call to

blocker.isReleasable()

that returned

false

.

If not running in a ForkJoinPool, this method is
behaviorally equivalent to

```java
while (!blocker.isReleasable())
if (blocker.block())
break;
```

If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to

blocker.block()

.

**Parameters:** blocker

- the blocker task
**Throws:** InterruptedException

- if

blocker.block()

did so

Field Detail

- defaultForkJoinWorkerThreadFactory

```java
public static final
ForkJoinPool.ForkJoinWorkerThreadFactory
defaultForkJoinWorkerThreadFactory
```

Creates a new ForkJoinWorkerThread. This factory is used unless
overridden in ForkJoinPool constructors.

---

#### Field Detail

defaultForkJoinWorkerThreadFactory

```java
public static final
ForkJoinPool.ForkJoinWorkerThreadFactory
defaultForkJoinWorkerThreadFactory
```

Creates a new ForkJoinWorkerThread. This factory is used unless
overridden in ForkJoinPool constructors.

---

#### defaultForkJoinWorkerThreadFactory

public static final

ForkJoinPool.ForkJoinWorkerThreadFactory

defaultForkJoinWorkerThreadFactory

Creates a new ForkJoinWorkerThread. This factory is used unless
overridden in ForkJoinPool constructors.

Constructor Detail

- ForkJoinPool

```java
public ForkJoinPool()
```

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- ForkJoinPool

```java
public ForkJoinPool​(int parallelism)
```

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

**Parameters:** parallelism

- the parallelism level
**Throws:** IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- ForkJoinPool

```java
public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode)
```

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Parameters:** parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
**Parameters:** factory

- the factory for creating new threads. For default value,
use

defaultForkJoinWorkerThreadFactory

.
**Parameters:** handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while executing
tasks. For default value, use

null

.
**Parameters:** asyncMode

- if true,
establishes local first-in-first-out scheduling mode for forked
tasks that are never joined. This mode may be more appropriate
than default locally stack-based mode in applications in which
worker threads only process event-style asynchronous tasks.
For default value, use

false

.
**Throws:** IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
**Throws:** NullPointerException

- if the factory is null
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- ForkJoinPool

```java
public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode,
int corePoolSize,
int maximumPoolSize,
int minimumRunnable,

Predicate
<? super
ForkJoinPool
> saturate,
long keepAliveTime,

TimeUnit
unit)
```

Creates a

ForkJoinPool

with the given parameters.

**Parameters:** parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
**Parameters:** factory

- the factory for creating new threads. For
default value, use

defaultForkJoinWorkerThreadFactory

.
**Parameters:** handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while
executing tasks. For default value, use

null

.
**Parameters:** asyncMode

- if true, establishes local first-in-first-out
scheduling mode for forked tasks that are never joined. This
mode may be more appropriate than default locally stack-based
mode in applications in which worker threads only process
event-style asynchronous tasks. For default value, use

false

.
**Parameters:** corePoolSize

- the number of threads to keep in the pool
(unless timed out after an elapsed keep-alive). Normally (and
by default) this is the same value as the parallelism level,
but may be set to a larger value to reduce dynamic overhead if
tasks regularly block. Using a smaller value (for example

0

) has the same effect as the default.
**Parameters:** maximumPoolSize

- the maximum number of threads allowed.
When the maximum is reached, attempts to replace blocked
threads fail. (However, because creation and termination of
different threads may overlap, and may be managed by the given
thread factory, this value may be transiently exceeded.) To
arrange the same value as is used by default for the common
pool, use

256

plus the

parallelism

level. (By
default, the common pool allows a maximum of 256 spare
threads.) Using a value (for example

Integer.MAX_VALUE

) larger than the implementation's total
thread limit has the same effect as using this limit (which is
the default).
**Parameters:** minimumRunnable

- the minimum allowed number of core
threads not blocked by a join or

ForkJoinPool.ManagedBlocker

. To
ensure progress, when too few unblocked threads exist and
unexecuted tasks may exist, new threads are constructed, up to
the given maximumPoolSize. For the default value, use

1

, that ensures liveness. A larger value might improve
throughput in the presence of blocked activities, but might
not, due to increased overhead. A value of zero may be
acceptable when submitted tasks cannot have dependencies
requiring additional threads.
**Parameters:** saturate

- if non-null, a predicate invoked upon attempts
to create more than the maximum total allowed threads. By
default, when a thread is about to block on a join or

ForkJoinPool.ManagedBlocker

, but cannot be replaced because the
maximumPoolSize would be exceeded, a

RejectedExecutionException

is thrown. But if this predicate
returns

true

, then no exception is thrown, so the pool
continues to operate with fewer than the target number of
runnable threads, which might not ensure progress.
**Parameters:** keepAliveTime

- the elapsed time since last use before
a thread is terminated (and then later replaced if needed).
For the default value, use

60, TimeUnit.SECONDS

.
**Parameters:** unit

- the time unit for the

keepAliveTime

argument
**Throws:** IllegalArgumentException

- if parallelism is less than or
equal to zero, or is greater than implementation limit,
or if maximumPoolSize is less than parallelism,
of if the keepAliveTime is less than or equal to zero.
**Throws:** NullPointerException

- if the factory is null
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")
**Since:** 9

---

#### Constructor Detail

ForkJoinPool

```java
public ForkJoinPool()
```

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### ForkJoinPool

public ForkJoinPool()

Creates a

ForkJoinPool

with parallelism equal to

Runtime.availableProcessors()

, using defaults for all
other parameters (see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

ForkJoinPool

```java
public ForkJoinPool​(int parallelism)
```

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

**Parameters:** parallelism

- the parallelism level
**Throws:** IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### ForkJoinPool

public ForkJoinPool​(int parallelism)

Creates a

ForkJoinPool

with the indicated parallelism
level, using defaults for all other parameters (see

ForkJoinPool(int, ForkJoinWorkerThreadFactory,
UncaughtExceptionHandler, boolean, int, int, int, Predicate,
long, TimeUnit)

).

ForkJoinPool

```java
public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode)
```

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

**Parameters:** parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
**Parameters:** factory

- the factory for creating new threads. For default value,
use

defaultForkJoinWorkerThreadFactory

.
**Parameters:** handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while executing
tasks. For default value, use

null

.
**Parameters:** asyncMode

- if true,
establishes local first-in-first-out scheduling mode for forked
tasks that are never joined. This mode may be more appropriate
than default locally stack-based mode in applications in which
worker threads only process event-style asynchronous tasks.
For default value, use

false

.
**Throws:** IllegalArgumentException

- if parallelism less than or
equal to zero, or greater than implementation limit
**Throws:** NullPointerException

- if the factory is null
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### ForkJoinPool

public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory

factory,

Thread.UncaughtExceptionHandler

handler,
boolean asyncMode)

Creates a

ForkJoinPool

with the given parameters (using
defaults for others -- see

ForkJoinPool(int,
ForkJoinWorkerThreadFactory, UncaughtExceptionHandler, boolean,
int, int, int, Predicate, long, TimeUnit)

).

ForkJoinPool

```java
public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory
factory,

Thread.UncaughtExceptionHandler
handler,
boolean asyncMode,
int corePoolSize,
int maximumPoolSize,
int minimumRunnable,

Predicate
<? super
ForkJoinPool
> saturate,
long keepAliveTime,

TimeUnit
unit)
```

Creates a

ForkJoinPool

with the given parameters.

**Parameters:** parallelism

- the parallelism level. For default value,
use

Runtime.availableProcessors()

.
**Parameters:** factory

- the factory for creating new threads. For
default value, use

defaultForkJoinWorkerThreadFactory

.
**Parameters:** handler

- the handler for internal worker threads that
terminate due to unrecoverable errors encountered while
executing tasks. For default value, use

null

.
**Parameters:** asyncMode

- if true, establishes local first-in-first-out
scheduling mode for forked tasks that are never joined. This
mode may be more appropriate than default locally stack-based
mode in applications in which worker threads only process
event-style asynchronous tasks. For default value, use

false

.
**Parameters:** corePoolSize

- the number of threads to keep in the pool
(unless timed out after an elapsed keep-alive). Normally (and
by default) this is the same value as the parallelism level,
but may be set to a larger value to reduce dynamic overhead if
tasks regularly block. Using a smaller value (for example

0

) has the same effect as the default.
**Parameters:** maximumPoolSize

- the maximum number of threads allowed.
When the maximum is reached, attempts to replace blocked
threads fail. (However, because creation and termination of
different threads may overlap, and may be managed by the given
thread factory, this value may be transiently exceeded.) To
arrange the same value as is used by default for the common
pool, use

256

plus the

parallelism

level. (By
default, the common pool allows a maximum of 256 spare
threads.) Using a value (for example

Integer.MAX_VALUE

) larger than the implementation's total
thread limit has the same effect as using this limit (which is
the default).
**Parameters:** minimumRunnable

- the minimum allowed number of core
threads not blocked by a join or

ForkJoinPool.ManagedBlocker

. To
ensure progress, when too few unblocked threads exist and
unexecuted tasks may exist, new threads are constructed, up to
the given maximumPoolSize. For the default value, use

1

, that ensures liveness. A larger value might improve
throughput in the presence of blocked activities, but might
not, due to increased overhead. A value of zero may be
acceptable when submitted tasks cannot have dependencies
requiring additional threads.
**Parameters:** saturate

- if non-null, a predicate invoked upon attempts
to create more than the maximum total allowed threads. By
default, when a thread is about to block on a join or

ForkJoinPool.ManagedBlocker

, but cannot be replaced because the
maximumPoolSize would be exceeded, a

RejectedExecutionException

is thrown. But if this predicate
returns

true

, then no exception is thrown, so the pool
continues to operate with fewer than the target number of
runnable threads, which might not ensure progress.
**Parameters:** keepAliveTime

- the elapsed time since last use before
a thread is terminated (and then later replaced if needed).
For the default value, use

60, TimeUnit.SECONDS

.
**Parameters:** unit

- the time unit for the

keepAliveTime

argument
**Throws:** IllegalArgumentException

- if parallelism is less than or
equal to zero, or is greater than implementation limit,
or if maximumPoolSize is less than parallelism,
of if the keepAliveTime is less than or equal to zero.
**Throws:** NullPointerException

- if the factory is null
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")
**Since:** 9

---

#### ForkJoinPool

public ForkJoinPool​(int parallelism,

ForkJoinPool.ForkJoinWorkerThreadFactory

factory,

Thread.UncaughtExceptionHandler

handler,
boolean asyncMode,
int corePoolSize,
int maximumPoolSize,
int minimumRunnable,

Predicate

<? super

ForkJoinPool

> saturate,
long keepAliveTime,

TimeUnit

unit)

Creates a

ForkJoinPool

with the given parameters.

Method Detail

- commonPool

```java
public static
ForkJoinPool
commonPool()
```

Returns the common pool instance. This pool is statically
constructed; its run state is unaffected by attempts to

shutdown()

or

shutdownNow()

. However this pool and any
ongoing processing are automatically terminated upon program

System.exit(int)

. Any program that relies on asynchronous
task processing to complete before program termination should
invoke

commonPool().

awaitQuiescence

,
before exit.

**Returns:** the common pool instance
**Since:** 1.8

- invoke

```java
public <T> T invoke​(
ForkJoinTask
<T> task)
```

Performs the given task, returning its result upon completion.
If the computation encounters an unchecked Exception or Error,
it is rethrown as the outcome of this invocation. Rethrown
exceptions behave in the same way as regular exceptions, but,
when possible, contain stack traces (as displayed for example
using

ex.printStackTrace()

) of both the current thread
as well as the thread actually encountering the exception;
minimally only the latter.

**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task
**Returns:** the task's result
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- execute

```java
public void execute​(
ForkJoinTask
<?> task)
```

Arranges for (asynchronous) execution of the given task.

**Parameters:** task

- the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- execute

```java
public void execute​(
Runnable
task)
```

Description copied from interface:

Executor

Executes the given command at some time in the future. The command
may execute in a new thread, in a pooled thread, or in the calling
thread, at the discretion of the

Executor

implementation.

**Parameters:** task

- the runnable task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public <T>
ForkJoinTask
<T> submit​(
ForkJoinTask
<T> task)
```

Submits a ForkJoinTask for execution.

**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public <T>
ForkJoinTask
<T> submit​(
Callable
<T> task)
```

Description copied from interface:

ExecutorService

Submits a value-returning task for execution and returns a
Future representing the pending results of the task. The
Future's

get

method will return the task's result upon
successful completion.

If you would like to immediately block waiting
for a task, you can use constructions of the form

result = exec.submit(aCallable).get();

Note: The

Executors

class includes a set of methods
that can convert some other common closure-like objects,
for example,

PrivilegedAction

to

Callable

form so they can be submitted.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public <T>
ForkJoinTask
<T> submit​(
Runnable
task,
T result)
```

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return the given result upon successful completion.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- submit

```java
public
ForkJoinTask
<?> submit​(
Runnable
task)
```

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return

null

upon

successful

completion.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

- invokeAll

```java
public <T>
List
<
Future
<T>> invokeAll​(
Collection
<? extends
Callable
<T>> tasks)
```

Description copied from interface:

ExecutorService

Executes the given tasks, returning a list of Futures holding
their status and results when all complete.

Future.isDone()

is

true

for each
element of the returned list.
Note that a

completed

task could have
terminated either normally or by throwing an exception.
The results of this method are undefined if the given
collection is modified while this operation is in progress.

**Type Parameters:** T

- the type of the values returned from the tasks
**Parameters:** tasks

- the collection of tasks
**Returns:** a list of Futures representing the tasks, in the same
sequential order as produced by the iterator for the
given task list, each of which has completed
**Throws:** NullPointerException

- if tasks or any of its elements are

null
**Throws:** RejectedExecutionException

- if any task cannot be
scheduled for execution

- getFactory

```java
public
ForkJoinPool.ForkJoinWorkerThreadFactory
getFactory()
```

Returns the factory used for constructing new workers.

**Returns:** the factory used for constructing new workers

- getUncaughtExceptionHandler

```java
public
Thread.UncaughtExceptionHandler
getUncaughtExceptionHandler()
```

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

**Returns:** the handler, or

null

if none

- getParallelism

```java
public int getParallelism()
```

Returns the targeted parallelism level of this pool.

**Returns:** the targeted parallelism level of this pool

- getCommonPoolParallelism

```java
public static int getCommonPoolParallelism()
```

Returns the targeted parallelism level of the common pool.

**Returns:** the targeted parallelism level of the common pool
**Since:** 1.8

- getPoolSize

```java
public int getPoolSize()
```

Returns the number of worker threads that have started but not
yet terminated. The result returned by this method may differ
from

getParallelism()

when threads are created to
maintain parallelism when others are cooperatively blocked.

**Returns:** the number of worker threads

- getAsyncMode

```java
public boolean getAsyncMode()
```

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

**Returns:** true

if this pool uses async mode

- getRunningThreadCount

```java
public int getRunningThreadCount()
```

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization. This method may overestimate the
number of running threads.

**Returns:** the number of worker threads

- getActiveThreadCount

```java
public int getActiveThreadCount()
```

Returns an estimate of the number of threads that are currently
stealing or executing tasks. This method may overestimate the
number of active threads.

**Returns:** the number of active threads

- isQuiescent

```java
public boolean isQuiescent()
```

Returns

true

if all worker threads are currently idle.
An idle worker is one that cannot obtain a task to execute
because none are available to steal from other threads, and
there are no pending submissions to the pool. This method is
conservative; it might not return

true

immediately upon
idleness of all threads, but will eventually become true if
threads remain inactive.

**Returns:** true

if all threads are currently idle

- getStealCount

```java
public long getStealCount()
```

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another. The reported value
underestimates the actual total number of steals when the pool
is not quiescent. This value may be useful for monitoring and
tuning fork/join programs: in general, steal counts should be
high enough to keep threads busy, but low enough to avoid
overhead and contention across threads.

**Returns:** the number of steals

- getQueuedTaskCount

```java
public long getQueuedTaskCount()
```

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing). This value is only
an approximation, obtained by iterating across all threads in
the pool. This method may be useful for tuning task
granularities.

**Returns:** the number of queued tasks

- getQueuedSubmissionCount

```java
public int getQueuedSubmissionCount()
```

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing. This method may take
time proportional to the number of submissions.

**Returns:** the number of queued submissions

- hasQueuedSubmissions

```java
public boolean hasQueuedSubmissions()
```

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

**Returns:** true

if there are any queued submissions

- pollSubmission

```java
protected
ForkJoinTask
<?> pollSubmission()
```

Removes and returns the next unexecuted submission if one is
available. This method may be useful in extensions to this
class that re-assign work in systems with multiple pools.

**Returns:** the next submission, or

null

if none

- drainTasksTo

```java
protected int drainTasksTo​(
Collection
<? super
ForkJoinTask
<?>> c)
```

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status. These may include
artificially generated or wrapped tasks. This method is
designed to be invoked only when the pool is known to be
quiescent. Invocations at other times may not remove all
tasks. A failure encountered while attempting to add elements
to collection

c

may result in elements being in
neither, either or both collections when the associated
exception is thrown. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress.

**Parameters:** c

- the collection to transfer elements into
**Returns:** the number of elements transferred

- toString

```java
public
String
toString()
```

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this pool, as well as its state

- shutdown

```java
public void shutdown()
```

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted. Invocation has no effect on execution state if this
is the

commonPool()

, and no additional effect if
already shut down. Tasks that are in the process of being
submitted concurrently during the course of this method may or
may not be rejected.

**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- shutdownNow

```java
public
List
<
Runnable
> shutdownNow()
```

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks. Invocation has no effect on
execution state if this is the

commonPool()

, and no
additional effect if already shut down. Otherwise, tasks that
are in the process of being submitted or executed concurrently
during the course of this method may or may not be
rejected. This method cancels both existing and unexecuted
tasks, in order to permit termination in the presence of task
dependencies. So the method always returns an empty list
(unlike the case for some other Executors).

**Returns:** an empty list
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

- isTerminated

```java
public boolean isTerminated()
```

Returns

true

if all tasks have completed following shut down.

**Returns:** true

if all tasks have completed following shut down

- isTerminating

```java
public boolean isTerminating()
```

Returns

true

if the process of termination has
commenced but not yet completed. This method may be useful for
debugging. A return of

true

reported a sufficient
period after shutdown may indicate that submitted tasks have
ignored or suppressed interruption, or are waiting for I/O,
causing this executor not to properly terminate. (See the
advisory notes for class

ForkJoinTask

stating that
tasks should not normally entail blocking operations. But if
they do, they must abort them on interrupt.)

**Returns:** true

if terminating but not yet terminated

- isShutdown

```java
public boolean isShutdown()
```

Returns

true

if this pool has been shut down.

**Returns:** true

if this pool has been shut down

- awaitTermination

```java
public boolean awaitTermination​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first. Because the

commonPool()

never terminates until program shutdown, when
applied to the common pool, this method is equivalent to

awaitQuiescence(long, TimeUnit)

but always returns

false

.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if this executor terminated and

false

if the timeout elapsed before termination
**Throws:** InterruptedException

- if interrupted while waiting

- awaitQuiescence

```java
public boolean awaitQuiescence​(long timeout,

TimeUnit
unit)
```

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

. Otherwise,
waits and/or attempts to assist performing tasks until this
pool

isQuiescent()

or the indicated timeout elapses.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if quiescent;

false

if the
timeout elapsed.

- managedBlock

```java
public static void managedBlock​(
ForkJoinPool.ManagedBlocker
blocker)
throws
InterruptedException
```

Runs the given possibly blocking task. When

running in a ForkJoinPool

, this
method possibly arranges for a spare thread to be activated if
necessary to ensure sufficient parallelism while the current
thread is blocked in

blocker.block()

.

This method repeatedly calls

blocker.isReleasable()

and

blocker.block()

until either method returns

true

.
Every call to

blocker.block()

is preceded by a call to

blocker.isReleasable()

that returned

false

.

If not running in a ForkJoinPool, this method is
behaviorally equivalent to

```java
while (!blocker.isReleasable())
if (blocker.block())
break;
```

If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to

blocker.block()

.

**Parameters:** blocker

- the blocker task
**Throws:** InterruptedException

- if

blocker.block()

did so

---

#### Method Detail

commonPool

```java
public static
ForkJoinPool
commonPool()
```

Returns the common pool instance. This pool is statically
constructed; its run state is unaffected by attempts to

shutdown()

or

shutdownNow()

. However this pool and any
ongoing processing are automatically terminated upon program

System.exit(int)

. Any program that relies on asynchronous
task processing to complete before program termination should
invoke

commonPool().

awaitQuiescence

,
before exit.

**Returns:** the common pool instance
**Since:** 1.8

---

#### commonPool

public static

ForkJoinPool

commonPool()

Returns the common pool instance. This pool is statically
constructed; its run state is unaffected by attempts to

shutdown()

or

shutdownNow()

. However this pool and any
ongoing processing are automatically terminated upon program

System.exit(int)

. Any program that relies on asynchronous
task processing to complete before program termination should
invoke

commonPool().

awaitQuiescence

,
before exit.

invoke

```java
public <T> T invoke​(
ForkJoinTask
<T> task)
```

Performs the given task, returning its result upon completion.
If the computation encounters an unchecked Exception or Error,
it is rethrown as the outcome of this invocation. Rethrown
exceptions behave in the same way as regular exceptions, but,
when possible, contain stack traces (as displayed for example
using

ex.printStackTrace()

) of both the current thread
as well as the thread actually encountering the exception;
minimally only the latter.

**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task
**Returns:** the task's result
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### invoke

public <T> T invoke​(

ForkJoinTask

<T> task)

Performs the given task, returning its result upon completion.
If the computation encounters an unchecked Exception or Error,
it is rethrown as the outcome of this invocation. Rethrown
exceptions behave in the same way as regular exceptions, but,
when possible, contain stack traces (as displayed for example
using

ex.printStackTrace()

) of both the current thread
as well as the thread actually encountering the exception;
minimally only the latter.

execute

```java
public void execute​(
ForkJoinTask
<?> task)
```

Arranges for (asynchronous) execution of the given task.

**Parameters:** task

- the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### execute

public void execute​(

ForkJoinTask

<?> task)

Arranges for (asynchronous) execution of the given task.

execute

```java
public void execute​(
Runnable
task)
```

Description copied from interface:

Executor

Executes the given command at some time in the future. The command
may execute in a new thread, in a pooled thread, or in the calling
thread, at the discretion of the

Executor

implementation.

**Parameters:** task

- the runnable task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### execute

public void execute​(

Runnable

task)

Description copied from interface:

Executor

Executes the given command at some time in the future. The command
may execute in a new thread, in a pooled thread, or in the calling
thread, at the discretion of the

Executor

implementation.

submit

```java
public <T>
ForkJoinTask
<T> submit​(
ForkJoinTask
<T> task)
```

Submits a ForkJoinTask for execution.

**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### submit

public <T>

ForkJoinTask

<T> submit​(

ForkJoinTask

<T> task)

Submits a ForkJoinTask for execution.

submit

```java
public <T>
ForkJoinTask
<T> submit​(
Callable
<T> task)
```

Description copied from interface:

ExecutorService

Submits a value-returning task for execution and returns a
Future representing the pending results of the task. The
Future's

get

method will return the task's result upon
successful completion.

If you would like to immediately block waiting
for a task, you can use constructions of the form

result = exec.submit(aCallable).get();

Note: The

Executors

class includes a set of methods
that can convert some other common closure-like objects,
for example,

PrivilegedAction

to

Callable

form so they can be submitted.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### submit

public <T>

ForkJoinTask

<T> submit​(

Callable

<T> task)

Description copied from interface:

ExecutorService

Submits a value-returning task for execution and returns a
Future representing the pending results of the task. The
Future's

get

method will return the task's result upon
successful completion.

If you would like to immediately block waiting
for a task, you can use constructions of the form

result = exec.submit(aCallable).get();

Note: The

Executors

class includes a set of methods
that can convert some other common closure-like objects,
for example,

PrivilegedAction

to

Callable

form so they can be submitted.

If you would like to immediately block waiting
for a task, you can use constructions of the form

result = exec.submit(aCallable).get();

Note: The

Executors

class includes a set of methods
that can convert some other common closure-like objects,
for example,

PrivilegedAction

to

Callable

form so they can be submitted.

Note: The

Executors

class includes a set of methods
that can convert some other common closure-like objects,
for example,

PrivilegedAction

to

Callable

form so they can be submitted.

submit

```java
public <T>
ForkJoinTask
<T> submit​(
Runnable
task,
T result)
```

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return the given result upon successful completion.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### submit

public <T>

ForkJoinTask

<T> submit​(

Runnable

task,
T result)

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return the given result upon successful completion.

submit

```java
public
ForkJoinTask
<?> submit​(
Runnable
task)
```

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return

null

upon

successful

completion.

**Specified by:** submit

in interface

ExecutorService
**Overrides:** submit

in class

AbstractExecutorService
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** NullPointerException

- if the task is null
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution

---

#### submit

public

ForkJoinTask

<?> submit​(

Runnable

task)

Description copied from interface:

ExecutorService

Submits a Runnable task for execution and returns a Future
representing that task. The Future's

get

method will
return

null

upon

successful

completion.

invokeAll

```java
public <T>
List
<
Future
<T>> invokeAll​(
Collection
<? extends
Callable
<T>> tasks)
```

Description copied from interface:

ExecutorService

Executes the given tasks, returning a list of Futures holding
their status and results when all complete.

Future.isDone()

is

true

for each
element of the returned list.
Note that a

completed

task could have
terminated either normally or by throwing an exception.
The results of this method are undefined if the given
collection is modified while this operation is in progress.

**Type Parameters:** T

- the type of the values returned from the tasks
**Parameters:** tasks

- the collection of tasks
**Returns:** a list of Futures representing the tasks, in the same
sequential order as produced by the iterator for the
given task list, each of which has completed
**Throws:** NullPointerException

- if tasks or any of its elements are

null
**Throws:** RejectedExecutionException

- if any task cannot be
scheduled for execution

---

#### invokeAll

public <T>

List

<

Future

<T>> invokeAll​(

Collection

<? extends

Callable

<T>> tasks)

Description copied from interface:

ExecutorService

Executes the given tasks, returning a list of Futures holding
their status and results when all complete.

Future.isDone()

is

true

for each
element of the returned list.
Note that a

completed

task could have
terminated either normally or by throwing an exception.
The results of this method are undefined if the given
collection is modified while this operation is in progress.

getFactory

```java
public
ForkJoinPool.ForkJoinWorkerThreadFactory
getFactory()
```

Returns the factory used for constructing new workers.

**Returns:** the factory used for constructing new workers

---

#### getFactory

public

ForkJoinPool.ForkJoinWorkerThreadFactory

getFactory()

Returns the factory used for constructing new workers.

getUncaughtExceptionHandler

```java
public
Thread.UncaughtExceptionHandler
getUncaughtExceptionHandler()
```

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

**Returns:** the handler, or

null

if none

---

#### getUncaughtExceptionHandler

public

Thread.UncaughtExceptionHandler

getUncaughtExceptionHandler()

Returns the handler for internal worker threads that terminate
due to unrecoverable errors encountered while executing tasks.

getParallelism

```java
public int getParallelism()
```

Returns the targeted parallelism level of this pool.

**Returns:** the targeted parallelism level of this pool

---

#### getParallelism

public int getParallelism()

Returns the targeted parallelism level of this pool.

getCommonPoolParallelism

```java
public static int getCommonPoolParallelism()
```

Returns the targeted parallelism level of the common pool.

**Returns:** the targeted parallelism level of the common pool
**Since:** 1.8

---

#### getCommonPoolParallelism

public static int getCommonPoolParallelism()

Returns the targeted parallelism level of the common pool.

getPoolSize

```java
public int getPoolSize()
```

Returns the number of worker threads that have started but not
yet terminated. The result returned by this method may differ
from

getParallelism()

when threads are created to
maintain parallelism when others are cooperatively blocked.

**Returns:** the number of worker threads

---

#### getPoolSize

public int getPoolSize()

Returns the number of worker threads that have started but not
yet terminated. The result returned by this method may differ
from

getParallelism()

when threads are created to
maintain parallelism when others are cooperatively blocked.

getAsyncMode

```java
public boolean getAsyncMode()
```

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

**Returns:** true

if this pool uses async mode

---

#### getAsyncMode

public boolean getAsyncMode()

Returns

true

if this pool uses local first-in-first-out
scheduling mode for forked tasks that are never joined.

getRunningThreadCount

```java
public int getRunningThreadCount()
```

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization. This method may overestimate the
number of running threads.

**Returns:** the number of worker threads

---

#### getRunningThreadCount

public int getRunningThreadCount()

Returns an estimate of the number of worker threads that are
not blocked waiting to join tasks or for other managed
synchronization. This method may overestimate the
number of running threads.

getActiveThreadCount

```java
public int getActiveThreadCount()
```

Returns an estimate of the number of threads that are currently
stealing or executing tasks. This method may overestimate the
number of active threads.

**Returns:** the number of active threads

---

#### getActiveThreadCount

public int getActiveThreadCount()

Returns an estimate of the number of threads that are currently
stealing or executing tasks. This method may overestimate the
number of active threads.

isQuiescent

```java
public boolean isQuiescent()
```

Returns

true

if all worker threads are currently idle.
An idle worker is one that cannot obtain a task to execute
because none are available to steal from other threads, and
there are no pending submissions to the pool. This method is
conservative; it might not return

true

immediately upon
idleness of all threads, but will eventually become true if
threads remain inactive.

**Returns:** true

if all threads are currently idle

---

#### isQuiescent

public boolean isQuiescent()

Returns

true

if all worker threads are currently idle.
An idle worker is one that cannot obtain a task to execute
because none are available to steal from other threads, and
there are no pending submissions to the pool. This method is
conservative; it might not return

true

immediately upon
idleness of all threads, but will eventually become true if
threads remain inactive.

getStealCount

```java
public long getStealCount()
```

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another. The reported value
underestimates the actual total number of steals when the pool
is not quiescent. This value may be useful for monitoring and
tuning fork/join programs: in general, steal counts should be
high enough to keep threads busy, but low enough to avoid
overhead and contention across threads.

**Returns:** the number of steals

---

#### getStealCount

public long getStealCount()

Returns an estimate of the total number of tasks stolen from
one thread's work queue by another. The reported value
underestimates the actual total number of steals when the pool
is not quiescent. This value may be useful for monitoring and
tuning fork/join programs: in general, steal counts should be
high enough to keep threads busy, but low enough to avoid
overhead and contention across threads.

getQueuedTaskCount

```java
public long getQueuedTaskCount()
```

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing). This value is only
an approximation, obtained by iterating across all threads in
the pool. This method may be useful for tuning task
granularities.

**Returns:** the number of queued tasks

---

#### getQueuedTaskCount

public long getQueuedTaskCount()

Returns an estimate of the total number of tasks currently held
in queues by worker threads (but not including tasks submitted
to the pool that have not begun executing). This value is only
an approximation, obtained by iterating across all threads in
the pool. This method may be useful for tuning task
granularities.

getQueuedSubmissionCount

```java
public int getQueuedSubmissionCount()
```

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing. This method may take
time proportional to the number of submissions.

**Returns:** the number of queued submissions

---

#### getQueuedSubmissionCount

public int getQueuedSubmissionCount()

Returns an estimate of the number of tasks submitted to this
pool that have not yet begun executing. This method may take
time proportional to the number of submissions.

hasQueuedSubmissions

```java
public boolean hasQueuedSubmissions()
```

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

**Returns:** true

if there are any queued submissions

---

#### hasQueuedSubmissions

public boolean hasQueuedSubmissions()

Returns

true

if there are any tasks submitted to this
pool that have not yet begun executing.

pollSubmission

```java
protected
ForkJoinTask
<?> pollSubmission()
```

Removes and returns the next unexecuted submission if one is
available. This method may be useful in extensions to this
class that re-assign work in systems with multiple pools.

**Returns:** the next submission, or

null

if none

---

#### pollSubmission

protected

ForkJoinTask

<?> pollSubmission()

Removes and returns the next unexecuted submission if one is
available. This method may be useful in extensions to this
class that re-assign work in systems with multiple pools.

drainTasksTo

```java
protected int drainTasksTo​(
Collection
<? super
ForkJoinTask
<?>> c)
```

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status. These may include
artificially generated or wrapped tasks. This method is
designed to be invoked only when the pool is known to be
quiescent. Invocations at other times may not remove all
tasks. A failure encountered while attempting to add elements
to collection

c

may result in elements being in
neither, either or both collections when the associated
exception is thrown. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress.

**Parameters:** c

- the collection to transfer elements into
**Returns:** the number of elements transferred

---

#### drainTasksTo

protected int drainTasksTo​(

Collection

<? super

ForkJoinTask

<?>> c)

Removes all available unexecuted submitted and forked tasks
from scheduling queues and adds them to the given collection,
without altering their execution status. These may include
artificially generated or wrapped tasks. This method is
designed to be invoked only when the pool is known to be
quiescent. Invocations at other times may not remove all
tasks. A failure encountered while attempting to add elements
to collection

c

may result in elements being in
neither, either or both collections when the associated
exception is thrown. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress.

toString

```java
public
String
toString()
```

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this pool, as well as its state

---

#### toString

public

String

toString()

Returns a string identifying this pool, as well as its state,
including indications of run state, parallelism level, and
worker and task counts.

shutdown

```java
public void shutdown()
```

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted. Invocation has no effect on execution state if this
is the

commonPool()

, and no additional effect if
already shut down. Tasks that are in the process of being
submitted concurrently during the course of this method may or
may not be rejected.

**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### shutdown

public void shutdown()

Possibly initiates an orderly shutdown in which previously
submitted tasks are executed, but no new tasks will be
accepted. Invocation has no effect on execution state if this
is the

commonPool()

, and no additional effect if
already shut down. Tasks that are in the process of being
submitted concurrently during the course of this method may or
may not be rejected.

shutdownNow

```java
public
List
<
Runnable
> shutdownNow()
```

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks. Invocation has no effect on
execution state if this is the

commonPool()

, and no
additional effect if already shut down. Otherwise, tasks that
are in the process of being submitted or executed concurrently
during the course of this method may or may not be
rejected. This method cancels both existing and unexecuted
tasks, in order to permit termination in the presence of task
dependencies. So the method always returns an empty list
(unlike the case for some other Executors).

**Returns:** an empty list
**Throws:** SecurityException

- if a security manager exists and
the caller is not permitted to modify threads
because it does not hold

RuntimePermission

("modifyThread")

---

#### shutdownNow

public

List

<

Runnable

> shutdownNow()

Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks. Invocation has no effect on
execution state if this is the

commonPool()

, and no
additional effect if already shut down. Otherwise, tasks that
are in the process of being submitted or executed concurrently
during the course of this method may or may not be
rejected. This method cancels both existing and unexecuted
tasks, in order to permit termination in the presence of task
dependencies. So the method always returns an empty list
(unlike the case for some other Executors).

isTerminated

```java
public boolean isTerminated()
```

Returns

true

if all tasks have completed following shut down.

**Returns:** true

if all tasks have completed following shut down

---

#### isTerminated

public boolean isTerminated()

Returns

true

if all tasks have completed following shut down.

isTerminating

```java
public boolean isTerminating()
```

Returns

true

if the process of termination has
commenced but not yet completed. This method may be useful for
debugging. A return of

true

reported a sufficient
period after shutdown may indicate that submitted tasks have
ignored or suppressed interruption, or are waiting for I/O,
causing this executor not to properly terminate. (See the
advisory notes for class

ForkJoinTask

stating that
tasks should not normally entail blocking operations. But if
they do, they must abort them on interrupt.)

**Returns:** true

if terminating but not yet terminated

---

#### isTerminating

public boolean isTerminating()

Returns

true

if the process of termination has
commenced but not yet completed. This method may be useful for
debugging. A return of

true

reported a sufficient
period after shutdown may indicate that submitted tasks have
ignored or suppressed interruption, or are waiting for I/O,
causing this executor not to properly terminate. (See the
advisory notes for class

ForkJoinTask

stating that
tasks should not normally entail blocking operations. But if
they do, they must abort them on interrupt.)

isShutdown

```java
public boolean isShutdown()
```

Returns

true

if this pool has been shut down.

**Returns:** true

if this pool has been shut down

---

#### isShutdown

public boolean isShutdown()

Returns

true

if this pool has been shut down.

awaitTermination

```java
public boolean awaitTermination​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first. Because the

commonPool()

never terminates until program shutdown, when
applied to the common pool, this method is equivalent to

awaitQuiescence(long, TimeUnit)

but always returns

false

.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if this executor terminated and

false

if the timeout elapsed before termination
**Throws:** InterruptedException

- if interrupted while waiting

---

#### awaitTermination

public boolean awaitTermination​(long timeout,

TimeUnit

unit)
throws

InterruptedException

Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first. Because the

commonPool()

never terminates until program shutdown, when
applied to the common pool, this method is equivalent to

awaitQuiescence(long, TimeUnit)

but always returns

false

.

awaitQuiescence

```java
public boolean awaitQuiescence​(long timeout,

TimeUnit
unit)
```

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

. Otherwise,
waits and/or attempts to assist performing tasks until this
pool

isQuiescent()

or the indicated timeout elapses.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** true

if quiescent;

false

if the
timeout elapsed.

---

#### awaitQuiescence

public boolean awaitQuiescence​(long timeout,

TimeUnit

unit)

If called by a ForkJoinTask operating in this pool, equivalent
in effect to

ForkJoinTask.helpQuiesce()

. Otherwise,
waits and/or attempts to assist performing tasks until this
pool

isQuiescent()

or the indicated timeout elapses.

managedBlock

```java
public static void managedBlock​(
ForkJoinPool.ManagedBlocker
blocker)
throws
InterruptedException
```

Runs the given possibly blocking task. When

running in a ForkJoinPool

, this
method possibly arranges for a spare thread to be activated if
necessary to ensure sufficient parallelism while the current
thread is blocked in

blocker.block()

.

This method repeatedly calls

blocker.isReleasable()

and

blocker.block()

until either method returns

true

.
Every call to

blocker.block()

is preceded by a call to

blocker.isReleasable()

that returned

false

.

If not running in a ForkJoinPool, this method is
behaviorally equivalent to

```java
while (!blocker.isReleasable())
if (blocker.block())
break;
```

If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to

blocker.block()

.

**Parameters:** blocker

- the blocker task
**Throws:** InterruptedException

- if

blocker.block()

did so

---

#### managedBlock

public static void managedBlock​(

ForkJoinPool.ManagedBlocker

blocker)
throws

InterruptedException

Runs the given possibly blocking task. When

running in a ForkJoinPool

, this
method possibly arranges for a spare thread to be activated if
necessary to ensure sufficient parallelism while the current
thread is blocked in

blocker.block()

.

This method repeatedly calls

blocker.isReleasable()

and

blocker.block()

until either method returns

true

.
Every call to

blocker.block()

is preceded by a call to

blocker.isReleasable()

that returned

false

.

If not running in a ForkJoinPool, this method is
behaviorally equivalent to

```java
while (!blocker.isReleasable())
if (blocker.block())
break;
```

If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to

blocker.block()

.

This method repeatedly calls

blocker.isReleasable()

and

blocker.block()

until either method returns

true

.
Every call to

blocker.block()

is preceded by a call to

blocker.isReleasable()

that returned

false

.

If not running in a ForkJoinPool, this method is
behaviorally equivalent to

```java
while (!blocker.isReleasable())
if (blocker.block())
break;
```

If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to

blocker.block()

.

If not running in a ForkJoinPool, this method is
behaviorally equivalent to

```java
while (!blocker.isReleasable())
if (blocker.block())
break;
```

If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to

blocker.block()

.

while (!blocker.isReleasable())
if (blocker.block())
break;

---

