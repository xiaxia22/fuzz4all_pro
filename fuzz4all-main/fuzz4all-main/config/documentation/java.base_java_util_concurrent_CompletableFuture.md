# Class CompletableFuture<T>

**Source:** `java.base\java\util\concurrent\CompletableFuture.html`

### Class Description

```java
public class
CompletableFuture<T>

extends
Object

implements
Future
<T>,
CompletionStage
<T>
```

A

Future

that may be explicitly completed (setting its
value and status), and may be used as a

CompletionStage

,
supporting dependent functions and actions that trigger upon its
completion.

When two or more threads attempt to

complete

,

completeExceptionally

, or

cancel

a CompletableFuture, only one of them succeeds.

In addition to these and related methods for directly
manipulating status and results, CompletableFuture implements
interface

CompletionStage

with the following policies:

- Actions supplied for dependent completions of

non-async

methods may be performed by the thread that
completes the current CompletableFuture, or by any other caller of
a completion method.

All

async

methods without an explicit Executor
argument are performed using the

ForkJoinPool.commonPool()

(unless it does not support a parallelism level of at least two, in
which case, a new Thread is created to run each task). This may be
overridden for non-static methods in subclasses by defining method

defaultExecutor()

. To simplify monitoring, debugging,
and tracking, all generated asynchronous tasks are instances of the
marker interface

CompletableFuture.AsynchronousCompletionTask

. Operations
with time-delays can use adapter methods defined in this class, for
example:

supplyAsync(supplier, delayedExecutor(timeout,
timeUnit))

. To support methods with delays and timeouts, this
class maintains at most one daemon thread for triggering and
cancelling actions, not for running them.

All CompletionStage methods are implemented independently of
other public methods, so the behavior of one method is not impacted
by overrides of others in subclasses.

All CompletionStage methods return CompletableFutures. To
restrict usages to only those methods defined in interface
CompletionStage, use method

minimalCompletionStage()

. Or to
ensure only that clients do not themselves modify a future, use
method

copy()

.

CompletableFuture also implements

Future

with the following
policies:

- Since (unlike

FutureTask

) this class has no direct
control over the computation that causes it to be completed,
cancellation is treated as just another form of exceptional
completion. Method

cancel

has the same effect as

completeExceptionally(new CancellationException())

. Method

isCompletedExceptionally()

can be used to determine if a
CompletableFuture completed in any exceptional fashion.

In case of exceptional completion with a CompletionException,
methods

get()

and

get(long, TimeUnit)

throw an

ExecutionException

with the same cause as held in the
corresponding CompletionException. To simplify usage in most
contexts, this class also defines methods

join()

and

getNow(T)

that instead throw the CompletionException directly
in these cases.

Arguments used to pass a completion result (that is, for
parameters of type

T

) for methods accepting them may be
null, but passing a null value for any other parameter will result
in a

NullPointerException

being thrown.

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

**Type Parameters:** T

- The result type returned by this future's

join

and

get

methods

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompletableFuture()

Creates a new incomplete CompletableFuture.

---

### Method Details

#### public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

**Parameters:**
- supplier

- a function returning the value to be used
to complete the returned CompletableFuture

**Returns:**
- the new CompletableFuture

**Type Parameters:**
- U

- the function's return type

---

#### public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier,

Executor
executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

**Parameters:**
- supplier

- a function returning the value to be used
to complete the returned CompletableFuture
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletableFuture

**Type Parameters:**
- U

- the function's return type

---

#### public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

**Parameters:**
- runnable

- the action to run before completing the
returned CompletableFuture

**Returns:**
- the new CompletableFuture

---

#### public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable,

Executor
executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

**Parameters:**
- runnable

- the action to run before completing the
returned CompletableFuture
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletableFuture

---

#### public static <U>
CompletableFuture
<U> completedFuture​(U value)

Returns a new CompletableFuture that is already completed with
the given value.

**Parameters:**
- value

- the value

**Returns:**
- the completed CompletableFuture

**Type Parameters:**
- U

- the type of the value

---

#### public boolean isDone()

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

**Specified by:**
- isDone

in interface

Future

<

T

>

**Returns:**
- true

if completed

---

#### public
T
get()
throws
InterruptedException
,

ExecutionException

Waits if necessary for this future to complete, and then
returns its result.

**Specified by:**
- get

in interface

Future

<

T

>

**Returns:**
- the result value

**Throws:**
- CancellationException

- if this future was cancelled
- ExecutionException

- if this future completed exceptionally
- InterruptedException

- if the current thread was interrupted
while waiting

---

#### public
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

**Specified by:**
- get

in interface

Future

<

T

>

**Parameters:**
- timeout

- the maximum time to wait
- unit

- the time unit of the timeout argument

**Returns:**
- the result value

**Throws:**
- CancellationException

- if this future was cancelled
- ExecutionException

- if this future completed exceptionally
- InterruptedException

- if the current thread was interrupted
while waiting
- TimeoutException

- if the wait timed out

---

#### public
T
join()

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally. To better
conform with the use of common functional forms, if a
computation involved in the completion of this
CompletableFuture threw an exception, this method throws an
(unchecked)

CompletionException

with the underlying
exception as its cause.

**Returns:**
- the result value

**Throws:**
- CancellationException

- if the computation was cancelled
- CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

---

#### public
T
getNow​(
T
valueIfAbsent)

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

**Parameters:**
- valueIfAbsent

- the value to return if not completed

**Returns:**
- the result value, if completed, else the given valueIfAbsent

**Throws:**
- CancellationException

- if the computation was cancelled
- CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

---

#### public boolean complete​(
T
value)

If not already completed, sets the value returned by

get()

and related methods to the given value.

**Parameters:**
- value

- the result value

**Returns:**
- true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

---

#### public boolean completeExceptionally​(
Throwable
ex)

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

**Parameters:**
- ex

- the exception

**Returns:**
- true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

---

#### public
CompletableFuture
<
T
> toCompletableFuture()

Returns this CompletableFuture.

**Specified by:**
- toCompletableFuture

in interface

CompletionStage

<

T

>

**Returns:**
- this CompletableFuture

---

#### public
CompletableFuture
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.
Note: More flexible versions of this functionality are
available using methods

whenComplete

and

handle

.

**Specified by:**
- exceptionally

in interface

CompletionStage

<

T

>

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletableFuture if this CompletableFuture completed
exceptionally

**Returns:**
- the new CompletableFuture

---

#### public static
CompletableFuture
<
Void
> allOf​(
CompletableFuture
<?>... cfs)

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete. If any of the given
CompletableFutures complete exceptionally, then the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. Otherwise, the results,
if any, of the given CompletableFutures are not reflected in
the returned CompletableFuture, but may be obtained by
inspecting them individually. If no CompletableFutures are
provided, returns a CompletableFuture completed with the value

null

.

Among the applications of this method is to await completion
of a set of independent CompletableFutures before continuing a
program, as in:

CompletableFuture.allOf(c1, c2,
c3).join();

.

**Parameters:**
- cfs

- the CompletableFutures

**Returns:**
- a new CompletableFuture that is completed when all of the
given CompletableFutures complete

**Throws:**
- NullPointerException

- if the array or any of its elements are

null

---

#### public static
CompletableFuture
<
Object
> anyOf​(
CompletableFuture
<?>... cfs)

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.
Otherwise, if it completed exceptionally, the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. If no CompletableFutures
are provided, returns an incomplete CompletableFuture.

**Parameters:**
- cfs

- the CompletableFutures

**Returns:**
- a new CompletableFuture that is completed with the
result or exception of any of the given CompletableFutures when
one completes

**Throws:**
- NullPointerException

- if the array or any of its elements are

null

---

#### public boolean cancel​(boolean mayInterruptIfRunning)

If not already completed, completes this CompletableFuture with
a

CancellationException

. Dependent CompletableFutures
that have not already completed will also complete
exceptionally, with a

CompletionException

caused by
this

CancellationException

.

**Specified by:**
- cancel

in interface

Future

<

T

>

**Parameters:**
- mayInterruptIfRunning

- this value has no effect in this
implementation because interrupts are not used to control
processing.

**Returns:**
- true

if this task is now cancelled

---

#### public boolean isCancelled()

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

**Specified by:**
- isCancelled

in interface

Future

<

T

>

**Returns:**
- true

if this CompletableFuture was cancelled
before it completed normally

---

#### public boolean isCompletedExceptionally()

Returns

true

if this CompletableFuture completed
exceptionally, in any way. Possible causes include
cancellation, explicit invocation of

completeExceptionally

, and abrupt termination of a
CompletionStage action.

**Returns:**
- true

if this CompletableFuture completed
exceptionally

---

#### public void obtrudeValue​(
T
value)

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:**
- value

- the completion value

---

#### public void obtrudeException​(
Throwable
ex)

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:**
- ex

- the exception

**Throws:**
- NullPointerException

- if the exception is null

---

#### public int getNumberOfDependents()

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.
This method is designed for use in monitoring system state, not
for synchronization control.

**Returns:**
- the number of dependent CompletableFutures

---

#### public
String
toString()

Returns a string identifying this CompletableFuture, as well as
its completion state. The state, in brackets, contains the
String

"Completed Normally"

or the String

"Completed Exceptionally"

, or the String

"Not
completed"

followed by the number of CompletableFutures
dependent upon its completion, if any.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string identifying this CompletableFuture, as well as its state

---

#### public <U>
CompletableFuture
<U> newIncompleteFuture()

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method. Subclasses should
normally override this method to return an instance of the same
class as this CompletableFuture. The default implementation
returns an instance of class CompletableFuture.

**Returns:**
- a new CompletableFuture

**Since:**
- 9

**Type Parameters:**
- U

- the type of the value

---

#### public
Executor
defaultExecutor()

Returns the default Executor used for async methods that do not
specify an Executor. This class uses the

ForkJoinPool.commonPool()

if it supports more than one
parallel thread, or else an Executor using one thread per async
task. This method may be overridden in subclasses to return
an Executor that provides at least one independent thread.

**Returns:**
- the executor

**Since:**
- 9

---

#### public
CompletableFuture
<
T
> copy()

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally. If this CompletableFuture completes exceptionally,
then the returned CompletableFuture completes exceptionally
with a CompletionException with this exception as cause. The
behavior is equivalent to

thenApply(x -> x)

. This
method may be useful as a form of "defensive copying", to
prevent clients from completing, while still being able to
arrange dependent actions.

**Returns:**
- the new CompletableFuture

**Since:**
- 9

---

#### public
CompletionStage
<
T
> minimalCompletionStage()

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

. If this CompletableFuture completes
exceptionally, then the returned CompletionStage completes
exceptionally with a CompletionException with this exception as
cause.

Unless overridden by a subclass, a new non-minimal
CompletableFuture with all methods available can be obtained from
a minimal CompletionStage via

toCompletableFuture()

.
For example, completion of a minimal stage can be awaited by

```java
minimalStage.toCompletableFuture().join();
```

**Returns:**
- the new CompletionStage

**Since:**
- 9

---

#### public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier,

Executor
executor)

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

**Parameters:**
- supplier

- a function returning the value to be used
to complete this CompletableFuture
- executor

- the executor to use for asynchronous execution

**Returns:**
- this CompletableFuture

**Since:**
- 9

---

#### public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier)

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

**Parameters:**
- supplier

- a function returning the value to be used
to complete this CompletableFuture

**Returns:**
- this CompletableFuture

**Since:**
- 9

---

#### public
CompletableFuture
<
T
> orTimeout​(long timeout,

TimeUnit
unit)

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

**Parameters:**
- timeout

- how long to wait before completing exceptionally
with a TimeoutException, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

timeout

parameter

**Returns:**
- this CompletableFuture

**Since:**
- 9

---

#### public
CompletableFuture
<
T
> completeOnTimeout​(
T
value,
long timeout,

TimeUnit
unit)

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

**Parameters:**
- value

- the value to use upon timeout
- timeout

- how long to wait before completing normally
with the given value, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

timeout

parameter

**Returns:**
- this CompletableFuture

**Since:**
- 9

---

#### public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit,

Executor
executor)

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:**
- delay

- how long to delay, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

delay

parameter
- executor

- the base executor

**Returns:**
- the new delayed executor

**Since:**
- 9

---

#### public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit)

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:**
- delay

- how long to delay, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

delay

parameter

**Returns:**
- the new delayed executor

**Since:**
- 9

---

#### public static <U>
CompletionStage
<U> completedStage​(U value)

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

**Parameters:**
- value

- the value

**Returns:**
- the completed CompletionStage

**Since:**
- 9

**Type Parameters:**
- U

- the type of the value

---

#### public static <U>
CompletableFuture
<U> failedFuture​(
Throwable
ex)

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

**Parameters:**
- ex

- the exception

**Returns:**
- the exceptionally completed CompletableFuture

**Since:**
- 9

**Type Parameters:**
- U

- the type of the value

---

#### public static <U>
CompletionStage
<U> failedStage​(
Throwable
ex)

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

**Parameters:**
- ex

- the exception

**Returns:**
- the exceptionally completed CompletionStage

**Since:**
- 9

**Type Parameters:**
- U

- the type of the value

---

### Additional Sections

#### Class CompletableFuture<T>

java.lang.Object

- java.util.concurrent.CompletableFuture<T>

java.util.concurrent.CompletableFuture<T>

**Type Parameters:** T

- The result type returned by this future's

join

and

get

methods

**All Implemented Interfaces:** CompletionStage

<T>

,

Future

<T>

```java
public class
CompletableFuture<T>

extends
Object

implements
Future
<T>,
CompletionStage
<T>
```

A

Future

that may be explicitly completed (setting its
value and status), and may be used as a

CompletionStage

,
supporting dependent functions and actions that trigger upon its
completion.

When two or more threads attempt to

complete

,

completeExceptionally

, or

cancel

a CompletableFuture, only one of them succeeds.

In addition to these and related methods for directly
manipulating status and results, CompletableFuture implements
interface

CompletionStage

with the following policies:

- Actions supplied for dependent completions of

non-async

methods may be performed by the thread that
completes the current CompletableFuture, or by any other caller of
a completion method.

All

async

methods without an explicit Executor
argument are performed using the

ForkJoinPool.commonPool()

(unless it does not support a parallelism level of at least two, in
which case, a new Thread is created to run each task). This may be
overridden for non-static methods in subclasses by defining method

defaultExecutor()

. To simplify monitoring, debugging,
and tracking, all generated asynchronous tasks are instances of the
marker interface

CompletableFuture.AsynchronousCompletionTask

. Operations
with time-delays can use adapter methods defined in this class, for
example:

supplyAsync(supplier, delayedExecutor(timeout,
timeUnit))

. To support methods with delays and timeouts, this
class maintains at most one daemon thread for triggering and
cancelling actions, not for running them.

All CompletionStage methods are implemented independently of
other public methods, so the behavior of one method is not impacted
by overrides of others in subclasses.

All CompletionStage methods return CompletableFutures. To
restrict usages to only those methods defined in interface
CompletionStage, use method

minimalCompletionStage()

. Or to
ensure only that clients do not themselves modify a future, use
method

copy()

.

CompletableFuture also implements

Future

with the following
policies:

- Since (unlike

FutureTask

) this class has no direct
control over the computation that causes it to be completed,
cancellation is treated as just another form of exceptional
completion. Method

cancel

has the same effect as

completeExceptionally(new CancellationException())

. Method

isCompletedExceptionally()

can be used to determine if a
CompletableFuture completed in any exceptional fashion.

In case of exceptional completion with a CompletionException,
methods

get()

and

get(long, TimeUnit)

throw an

ExecutionException

with the same cause as held in the
corresponding CompletionException. To simplify usage in most
contexts, this class also defines methods

join()

and

getNow(T)

that instead throw the CompletionException directly
in these cases.

Arguments used to pass a completion result (that is, for
parameters of type

T

) for methods accepting them may be
null, but passing a null value for any other parameter will result
in a

NullPointerException

being thrown.

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

**Since:** 1.8

public class

CompletableFuture<T>

extends

Object

implements

Future

<T>,

CompletionStage

<T>

A

Future

that may be explicitly completed (setting its
value and status), and may be used as a

CompletionStage

,
supporting dependent functions and actions that trigger upon its
completion.

When two or more threads attempt to

complete

,

completeExceptionally

, or

cancel

a CompletableFuture, only one of them succeeds.

In addition to these and related methods for directly
manipulating status and results, CompletableFuture implements
interface

CompletionStage

with the following policies:

- Actions supplied for dependent completions of

non-async

methods may be performed by the thread that
completes the current CompletableFuture, or by any other caller of
a completion method.

All

async

methods without an explicit Executor
argument are performed using the

ForkJoinPool.commonPool()

(unless it does not support a parallelism level of at least two, in
which case, a new Thread is created to run each task). This may be
overridden for non-static methods in subclasses by defining method

defaultExecutor()

. To simplify monitoring, debugging,
and tracking, all generated asynchronous tasks are instances of the
marker interface

CompletableFuture.AsynchronousCompletionTask

. Operations
with time-delays can use adapter methods defined in this class, for
example:

supplyAsync(supplier, delayedExecutor(timeout,
timeUnit))

. To support methods with delays and timeouts, this
class maintains at most one daemon thread for triggering and
cancelling actions, not for running them.

All CompletionStage methods are implemented independently of
other public methods, so the behavior of one method is not impacted
by overrides of others in subclasses.

All CompletionStage methods return CompletableFutures. To
restrict usages to only those methods defined in interface
CompletionStage, use method

minimalCompletionStage()

. Or to
ensure only that clients do not themselves modify a future, use
method

copy()

.

CompletableFuture also implements

Future

with the following
policies:

- Since (unlike

FutureTask

) this class has no direct
control over the computation that causes it to be completed,
cancellation is treated as just another form of exceptional
completion. Method

cancel

has the same effect as

completeExceptionally(new CancellationException())

. Method

isCompletedExceptionally()

can be used to determine if a
CompletableFuture completed in any exceptional fashion.

In case of exceptional completion with a CompletionException,
methods

get()

and

get(long, TimeUnit)

throw an

ExecutionException

with the same cause as held in the
corresponding CompletionException. To simplify usage in most
contexts, this class also defines methods

join()

and

getNow(T)

that instead throw the CompletionException directly
in these cases.

Arguments used to pass a completion result (that is, for
parameters of type

T

) for methods accepting them may be
null, but passing a null value for any other parameter will result
in a

NullPointerException

being thrown.

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

When two or more threads attempt to

complete

,

completeExceptionally

, or

cancel

a CompletableFuture, only one of them succeeds.

In addition to these and related methods for directly
manipulating status and results, CompletableFuture implements
interface

CompletionStage

with the following policies:

- Actions supplied for dependent completions of

non-async

methods may be performed by the thread that
completes the current CompletableFuture, or by any other caller of
a completion method.

All

async

methods without an explicit Executor
argument are performed using the

ForkJoinPool.commonPool()

(unless it does not support a parallelism level of at least two, in
which case, a new Thread is created to run each task). This may be
overridden for non-static methods in subclasses by defining method

defaultExecutor()

. To simplify monitoring, debugging,
and tracking, all generated asynchronous tasks are instances of the
marker interface

CompletableFuture.AsynchronousCompletionTask

. Operations
with time-delays can use adapter methods defined in this class, for
example:

supplyAsync(supplier, delayedExecutor(timeout,
timeUnit))

. To support methods with delays and timeouts, this
class maintains at most one daemon thread for triggering and
cancelling actions, not for running them.

All CompletionStage methods are implemented independently of
other public methods, so the behavior of one method is not impacted
by overrides of others in subclasses.

All CompletionStage methods return CompletableFutures. To
restrict usages to only those methods defined in interface
CompletionStage, use method

minimalCompletionStage()

. Or to
ensure only that clients do not themselves modify a future, use
method

copy()

.

CompletableFuture also implements

Future

with the following
policies:

- Since (unlike

FutureTask

) this class has no direct
control over the computation that causes it to be completed,
cancellation is treated as just another form of exceptional
completion. Method

cancel

has the same effect as

completeExceptionally(new CancellationException())

. Method

isCompletedExceptionally()

can be used to determine if a
CompletableFuture completed in any exceptional fashion.

In case of exceptional completion with a CompletionException,
methods

get()

and

get(long, TimeUnit)

throw an

ExecutionException

with the same cause as held in the
corresponding CompletionException. To simplify usage in most
contexts, this class also defines methods

join()

and

getNow(T)

that instead throw the CompletionException directly
in these cases.

Arguments used to pass a completion result (that is, for
parameters of type

T

) for methods accepting them may be
null, but passing a null value for any other parameter will result
in a

NullPointerException

being thrown.

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

In addition to these and related methods for directly
manipulating status and results, CompletableFuture implements
interface

CompletionStage

with the following policies:

- Actions supplied for dependent completions of

non-async

methods may be performed by the thread that
completes the current CompletableFuture, or by any other caller of
a completion method.

All

async

methods without an explicit Executor
argument are performed using the

ForkJoinPool.commonPool()

(unless it does not support a parallelism level of at least two, in
which case, a new Thread is created to run each task). This may be
overridden for non-static methods in subclasses by defining method

defaultExecutor()

. To simplify monitoring, debugging,
and tracking, all generated asynchronous tasks are instances of the
marker interface

CompletableFuture.AsynchronousCompletionTask

. Operations
with time-delays can use adapter methods defined in this class, for
example:

supplyAsync(supplier, delayedExecutor(timeout,
timeUnit))

. To support methods with delays and timeouts, this
class maintains at most one daemon thread for triggering and
cancelling actions, not for running them.

All CompletionStage methods are implemented independently of
other public methods, so the behavior of one method is not impacted
by overrides of others in subclasses.

All CompletionStage methods return CompletableFutures. To
restrict usages to only those methods defined in interface
CompletionStage, use method

minimalCompletionStage()

. Or to
ensure only that clients do not themselves modify a future, use
method

copy()

.

CompletableFuture also implements

Future

with the following
policies:

- Since (unlike

FutureTask

) this class has no direct
control over the computation that causes it to be completed,
cancellation is treated as just another form of exceptional
completion. Method

cancel

has the same effect as

completeExceptionally(new CancellationException())

. Method

isCompletedExceptionally()

can be used to determine if a
CompletableFuture completed in any exceptional fashion.

In case of exceptional completion with a CompletionException,
methods

get()

and

get(long, TimeUnit)

throw an

ExecutionException

with the same cause as held in the
corresponding CompletionException. To simplify usage in most
contexts, this class also defines methods

join()

and

getNow(T)

that instead throw the CompletionException directly
in these cases.

Arguments used to pass a completion result (that is, for
parameters of type

T

) for methods accepting them may be
null, but passing a null value for any other parameter will result
in a

NullPointerException

being thrown.

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

Actions supplied for dependent completions of

non-async

methods may be performed by the thread that
completes the current CompletableFuture, or by any other caller of
a completion method.

All

async

methods without an explicit Executor
argument are performed using the

ForkJoinPool.commonPool()

(unless it does not support a parallelism level of at least two, in
which case, a new Thread is created to run each task). This may be
overridden for non-static methods in subclasses by defining method

defaultExecutor()

. To simplify monitoring, debugging,
and tracking, all generated asynchronous tasks are instances of the
marker interface

CompletableFuture.AsynchronousCompletionTask

. Operations
with time-delays can use adapter methods defined in this class, for
example:

supplyAsync(supplier, delayedExecutor(timeout,
timeUnit))

. To support methods with delays and timeouts, this
class maintains at most one daemon thread for triggering and
cancelling actions, not for running them.

All CompletionStage methods are implemented independently of
other public methods, so the behavior of one method is not impacted
by overrides of others in subclasses.

All CompletionStage methods return CompletableFutures. To
restrict usages to only those methods defined in interface
CompletionStage, use method

minimalCompletionStage()

. Or to
ensure only that clients do not themselves modify a future, use
method

copy()

.

CompletableFuture also implements

Future

with the following
policies:

- Since (unlike

FutureTask

) this class has no direct
control over the computation that causes it to be completed,
cancellation is treated as just another form of exceptional
completion. Method

cancel

has the same effect as

completeExceptionally(new CancellationException())

. Method

isCompletedExceptionally()

can be used to determine if a
CompletableFuture completed in any exceptional fashion.

In case of exceptional completion with a CompletionException,
methods

get()

and

get(long, TimeUnit)

throw an

ExecutionException

with the same cause as held in the
corresponding CompletionException. To simplify usage in most
contexts, this class also defines methods

join()

and

getNow(T)

that instead throw the CompletionException directly
in these cases.

Arguments used to pass a completion result (that is, for
parameters of type

T

) for methods accepting them may be
null, but passing a null value for any other parameter will result
in a

NullPointerException

being thrown.

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

Since (unlike

FutureTask

) this class has no direct
control over the computation that causes it to be completed,
cancellation is treated as just another form of exceptional
completion. Method

cancel

has the same effect as

completeExceptionally(new CancellationException())

. Method

isCompletedExceptionally()

can be used to determine if a
CompletableFuture completed in any exceptional fashion.

In case of exceptional completion with a CompletionException,
methods

get()

and

get(long, TimeUnit)

throw an

ExecutionException

with the same cause as held in the
corresponding CompletionException. To simplify usage in most
contexts, this class also defines methods

join()

and

getNow(T)

that instead throw the CompletionException directly
in these cases.

Arguments used to pass a completion result (that is, for
parameters of type

T

) for methods accepting them may be
null, but passing a null value for any other parameter will result
in a

NullPointerException

being thrown.

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

Subclasses of this class should normally override the "virtual
constructor" method

newIncompleteFuture()

, which establishes
the concrete type returned by CompletionStage methods. For example,
here is a class that substitutes a different default Executor and
disables the

obtrude

methods:

```java
class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}
```

class MyCompletableFuture<T> extends CompletableFuture<T> {
static final Executor myExecutor = ...;
public MyCompletableFuture() { }
public <U> CompletableFuture<U> newIncompleteFuture() {
return new MyCompletableFuture<U>(); }
public Executor defaultExecutor() {
return myExecutor; }
public void obtrudeValue(T value) {
throw new UnsupportedOperationException(); }
public void obtrudeException(Throwable ex) {
throw new UnsupportedOperationException(); }
}

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

CompletableFuture.AsynchronousCompletionTask

A marker interface identifying asynchronous tasks produced by

async

methods.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompletableFuture

()

Creates a new incomplete CompletableFuture.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

CompletableFuture

<

Void

>

allOf

​(

CompletableFuture

<?>... cfs)

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete.

static

CompletableFuture

<

Object

>

anyOf

​(

CompletableFuture

<?>... cfs)

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.

boolean

cancel

​(boolean mayInterruptIfRunning)

If not already completed, completes this CompletableFuture with
a

CancellationException

.

boolean

complete

​(

T

value)

If not already completed, sets the value returned by

get()

and related methods to the given value.

CompletableFuture

<

T

>

completeAsync

​(

Supplier

<? extends

T

> supplier)

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

CompletableFuture

<

T

>

completeAsync

​(

Supplier

<? extends

T

> supplier,

Executor

executor)

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

static <U>

CompletableFuture

<U>

completedFuture

​(U value)

Returns a new CompletableFuture that is already completed with
the given value.

static <U>

CompletionStage

<U>

completedStage

​(U value)

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

boolean

completeExceptionally

​(

Throwable

ex)

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

CompletableFuture

<

T

>

completeOnTimeout

​(

T

value,
long timeout,

TimeUnit

unit)

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

CompletableFuture

<

T

>

copy

()

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally.

Executor

defaultExecutor

()

Returns the default Executor used for async methods that do not
specify an Executor.

static

Executor

delayedExecutor

​(long delay,

TimeUnit

unit)

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).

static

Executor

delayedExecutor

​(long delay,

TimeUnit

unit,

Executor

executor)

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).

CompletableFuture

<

T

>

exceptionally

​(

Function

<

Throwable

,​? extends

T

> fn)

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.

static <U>

CompletableFuture

<U>

failedFuture

​(

Throwable

ex)

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

static <U>

CompletionStage

<U>

failedStage

​(

Throwable

ex)

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

T

get

()

Waits if necessary for this future to complete, and then
returns its result.

T

get

​(long timeout,

TimeUnit

unit)

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

T

getNow

​(

T

valueIfAbsent)

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

int

getNumberOfDependents

()

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.

boolean

isCancelled

()

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

boolean

isCompletedExceptionally

()

Returns

true

if this CompletableFuture completed
exceptionally, in any way.

boolean

isDone

()

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

T

join

()

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally.

CompletionStage

<

T

>

minimalCompletionStage

()

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

.

<U>

CompletableFuture

<U>

newIncompleteFuture

()

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method.

void

obtrudeException

​(

Throwable

ex)

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed.

void

obtrudeValue

​(

T

value)

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed.

CompletableFuture

<

T

>

orTimeout

​(long timeout,

TimeUnit

unit)

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

static

CompletableFuture

<

Void

>

runAsync

​(

Runnable

runnable)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

static

CompletableFuture

<

Void

>

runAsync

​(

Runnable

runnable,

Executor

executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

static <U>

CompletableFuture

<U>

supplyAsync

​(

Supplier

<U> supplier)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

static <U>

CompletableFuture

<U>

supplyAsync

​(

Supplier

<U> supplier,

Executor

executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

CompletableFuture

<

T

>

toCompletableFuture

()

Returns this CompletableFuture.

String

toString

()

Returns a string identifying this CompletableFuture, as well as
its completion state.

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

CompletionStage

acceptEither

,

acceptEitherAsync

,

acceptEitherAsync

,

applyToEither

,

applyToEitherAsync

,

applyToEitherAsync

,

handle

,

handleAsync

,

handleAsync

,

runAfterBoth

,

runAfterBothAsync

,

runAfterBothAsync

,

runAfterEither

,

runAfterEitherAsync

,

runAfterEitherAsync

,

thenAccept

,

thenAcceptAsync

,

thenAcceptAsync

,

thenAcceptBoth

,

thenAcceptBothAsync

,

thenAcceptBothAsync

,

thenApply

,

thenApplyAsync

,

thenApplyAsync

,

thenCombine

,

thenCombineAsync

,

thenCombineAsync

,

thenCompose

,

thenComposeAsync

,

thenComposeAsync

,

thenRun

,

thenRunAsync

,

thenRunAsync

,

whenComplete

,

whenCompleteAsync

,

whenCompleteAsync

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

CompletableFuture.AsynchronousCompletionTask

A marker interface identifying asynchronous tasks produced by

async

methods.

---

#### Nested Class Summary

A marker interface identifying asynchronous tasks produced by

async

methods.

Constructor Summary

Constructors

Constructor

Description

CompletableFuture

()

Creates a new incomplete CompletableFuture.

---

#### Constructor Summary

Creates a new incomplete CompletableFuture.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

CompletableFuture

<

Void

>

allOf

​(

CompletableFuture

<?>... cfs)

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete.

static

CompletableFuture

<

Object

>

anyOf

​(

CompletableFuture

<?>... cfs)

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.

boolean

cancel

​(boolean mayInterruptIfRunning)

If not already completed, completes this CompletableFuture with
a

CancellationException

.

boolean

complete

​(

T

value)

If not already completed, sets the value returned by

get()

and related methods to the given value.

CompletableFuture

<

T

>

completeAsync

​(

Supplier

<? extends

T

> supplier)

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

CompletableFuture

<

T

>

completeAsync

​(

Supplier

<? extends

T

> supplier,

Executor

executor)

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

static <U>

CompletableFuture

<U>

completedFuture

​(U value)

Returns a new CompletableFuture that is already completed with
the given value.

static <U>

CompletionStage

<U>

completedStage

​(U value)

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

boolean

completeExceptionally

​(

Throwable

ex)

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

CompletableFuture

<

T

>

completeOnTimeout

​(

T

value,
long timeout,

TimeUnit

unit)

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

CompletableFuture

<

T

>

copy

()

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally.

Executor

defaultExecutor

()

Returns the default Executor used for async methods that do not
specify an Executor.

static

Executor

delayedExecutor

​(long delay,

TimeUnit

unit)

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).

static

Executor

delayedExecutor

​(long delay,

TimeUnit

unit,

Executor

executor)

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).

CompletableFuture

<

T

>

exceptionally

​(

Function

<

Throwable

,​? extends

T

> fn)

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.

static <U>

CompletableFuture

<U>

failedFuture

​(

Throwable

ex)

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

static <U>

CompletionStage

<U>

failedStage

​(

Throwable

ex)

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

T

get

()

Waits if necessary for this future to complete, and then
returns its result.

T

get

​(long timeout,

TimeUnit

unit)

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

T

getNow

​(

T

valueIfAbsent)

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

int

getNumberOfDependents

()

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.

boolean

isCancelled

()

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

boolean

isCompletedExceptionally

()

Returns

true

if this CompletableFuture completed
exceptionally, in any way.

boolean

isDone

()

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

T

join

()

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally.

CompletionStage

<

T

>

minimalCompletionStage

()

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

.

<U>

CompletableFuture

<U>

newIncompleteFuture

()

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method.

void

obtrudeException

​(

Throwable

ex)

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed.

void

obtrudeValue

​(

T

value)

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed.

CompletableFuture

<

T

>

orTimeout

​(long timeout,

TimeUnit

unit)

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

static

CompletableFuture

<

Void

>

runAsync

​(

Runnable

runnable)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

static

CompletableFuture

<

Void

>

runAsync

​(

Runnable

runnable,

Executor

executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

static <U>

CompletableFuture

<U>

supplyAsync

​(

Supplier

<U> supplier)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

static <U>

CompletableFuture

<U>

supplyAsync

​(

Supplier

<U> supplier,

Executor

executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

CompletableFuture

<

T

>

toCompletableFuture

()

Returns this CompletableFuture.

String

toString

()

Returns a string identifying this CompletableFuture, as well as
its completion state.

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

CompletionStage

acceptEither

,

acceptEitherAsync

,

acceptEitherAsync

,

applyToEither

,

applyToEitherAsync

,

applyToEitherAsync

,

handle

,

handleAsync

,

handleAsync

,

runAfterBoth

,

runAfterBothAsync

,

runAfterBothAsync

,

runAfterEither

,

runAfterEitherAsync

,

runAfterEitherAsync

,

thenAccept

,

thenAcceptAsync

,

thenAcceptAsync

,

thenAcceptBoth

,

thenAcceptBothAsync

,

thenAcceptBothAsync

,

thenApply

,

thenApplyAsync

,

thenApplyAsync

,

thenCombine

,

thenCombineAsync

,

thenCombineAsync

,

thenCompose

,

thenComposeAsync

,

thenComposeAsync

,

thenRun

,

thenRunAsync

,

thenRunAsync

,

whenComplete

,

whenCompleteAsync

,

whenCompleteAsync

---

#### Method Summary

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete.

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.

If not already completed, completes this CompletableFuture with
a

CancellationException

.

If not already completed, sets the value returned by

get()

and related methods to the given value.

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

Returns a new CompletableFuture that is already completed with
the given value.

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally.

Returns the default Executor used for async methods that do not
specify an Executor.

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

Waits if necessary for this future to complete, and then
returns its result.

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

Returns

true

if this CompletableFuture completed
exceptionally, in any way.

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally.

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

.

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method.

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed.

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed.

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

Returns this CompletableFuture.

Returns a string identifying this CompletableFuture, as well as
its completion state.

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

CompletionStage

acceptEither

,

acceptEitherAsync

,

acceptEitherAsync

,

applyToEither

,

applyToEitherAsync

,

applyToEitherAsync

,

handle

,

handleAsync

,

handleAsync

,

runAfterBoth

,

runAfterBothAsync

,

runAfterBothAsync

,

runAfterEither

,

runAfterEitherAsync

,

runAfterEitherAsync

,

thenAccept

,

thenAcceptAsync

,

thenAcceptAsync

,

thenAcceptBoth

,

thenAcceptBothAsync

,

thenAcceptBothAsync

,

thenApply

,

thenApplyAsync

,

thenApplyAsync

,

thenCombine

,

thenCombineAsync

,

thenCombineAsync

,

thenCompose

,

thenComposeAsync

,

thenComposeAsync

,

thenRun

,

thenRunAsync

,

thenRunAsync

,

whenComplete

,

whenCompleteAsync

,

whenCompleteAsync

---

#### Methods declared in interface java.util.concurrent. CompletionStage

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompletableFuture

```java
public CompletableFuture()
```

Creates a new incomplete CompletableFuture.

============ METHOD DETAIL ==========

- Method Detail

- supplyAsync

```java
public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

**Type Parameters:** U

- the function's return type
**Parameters:** supplier

- a function returning the value to be used
to complete the returned CompletableFuture
**Returns:** the new CompletableFuture

- supplyAsync

```java
public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier,

Executor
executor)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

**Type Parameters:** U

- the function's return type
**Parameters:** supplier

- a function returning the value to be used
to complete the returned CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletableFuture

- runAsync

```java
public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

**Parameters:** runnable

- the action to run before completing the
returned CompletableFuture
**Returns:** the new CompletableFuture

- runAsync

```java
public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable,

Executor
executor)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

**Parameters:** runnable

- the action to run before completing the
returned CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletableFuture

- completedFuture

```java
public static <U>
CompletableFuture
<U> completedFuture​(U value)
```

Returns a new CompletableFuture that is already completed with
the given value.

**Type Parameters:** U

- the type of the value
**Parameters:** value

- the value
**Returns:** the completed CompletableFuture

- isDone

```java
public boolean isDone()
```

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

**Specified by:** isDone

in interface

Future

<

T

>
**Returns:** true

if completed

- get

```java
public
T
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for this future to complete, and then
returns its result.

**Specified by:** get

in interface

Future

<

T

>
**Returns:** the result value
**Throws:** CancellationException

- if this future was cancelled
**Throws:** ExecutionException

- if this future completed exceptionally
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting

- get

```java
public
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException
```

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

**Specified by:** get

in interface

Future

<

T

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the result value
**Throws:** CancellationException

- if this future was cancelled
**Throws:** ExecutionException

- if this future completed exceptionally
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** TimeoutException

- if the wait timed out

- join

```java
public
T
join()
```

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally. To better
conform with the use of common functional forms, if a
computation involved in the completion of this
CompletableFuture threw an exception, this method throws an
(unchecked)

CompletionException

with the underlying
exception as its cause.

**Returns:** the result value
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

- getNow

```java
public
T
getNow​(
T
valueIfAbsent)
```

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

**Parameters:** valueIfAbsent

- the value to return if not completed
**Returns:** the result value, if completed, else the given valueIfAbsent
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

- complete

```java
public boolean complete​(
T
value)
```

If not already completed, sets the value returned by

get()

and related methods to the given value.

**Parameters:** value

- the result value
**Returns:** true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

- completeExceptionally

```java
public boolean completeExceptionally​(
Throwable
ex)
```

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

**Parameters:** ex

- the exception
**Returns:** true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

- toCompletableFuture

```java
public
CompletableFuture
<
T
> toCompletableFuture()
```

Returns this CompletableFuture.

**Specified by:** toCompletableFuture

in interface

CompletionStage

<

T

>
**Returns:** this CompletableFuture

- exceptionally

```java
public
CompletableFuture
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)
```

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.
Note: More flexible versions of this functionality are
available using methods

whenComplete

and

handle

.

**Specified by:** exceptionally

in interface

CompletionStage

<

T

>
**Parameters:** fn

- the function to use to compute the value of the
returned CompletableFuture if this CompletableFuture completed
exceptionally
**Returns:** the new CompletableFuture

- allOf

```java
public static
CompletableFuture
<
Void
> allOf​(
CompletableFuture
<?>... cfs)
```

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete. If any of the given
CompletableFutures complete exceptionally, then the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. Otherwise, the results,
if any, of the given CompletableFutures are not reflected in
the returned CompletableFuture, but may be obtained by
inspecting them individually. If no CompletableFutures are
provided, returns a CompletableFuture completed with the value

null

.

Among the applications of this method is to await completion
of a set of independent CompletableFutures before continuing a
program, as in:

CompletableFuture.allOf(c1, c2,
c3).join();

.

**Parameters:** cfs

- the CompletableFutures
**Returns:** a new CompletableFuture that is completed when all of the
given CompletableFutures complete
**Throws:** NullPointerException

- if the array or any of its elements are

null

- anyOf

```java
public static
CompletableFuture
<
Object
> anyOf​(
CompletableFuture
<?>... cfs)
```

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.
Otherwise, if it completed exceptionally, the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. If no CompletableFutures
are provided, returns an incomplete CompletableFuture.

**Parameters:** cfs

- the CompletableFutures
**Returns:** a new CompletableFuture that is completed with the
result or exception of any of the given CompletableFutures when
one completes
**Throws:** NullPointerException

- if the array or any of its elements are

null

- cancel

```java
public boolean cancel​(boolean mayInterruptIfRunning)
```

If not already completed, completes this CompletableFuture with
a

CancellationException

. Dependent CompletableFutures
that have not already completed will also complete
exceptionally, with a

CompletionException

caused by
this

CancellationException

.

**Specified by:** cancel

in interface

Future

<

T

>
**Parameters:** mayInterruptIfRunning

- this value has no effect in this
implementation because interrupts are not used to control
processing.
**Returns:** true

if this task is now cancelled

- isCancelled

```java
public boolean isCancelled()
```

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

**Specified by:** isCancelled

in interface

Future

<

T

>
**Returns:** true

if this CompletableFuture was cancelled
before it completed normally

- isCompletedExceptionally

```java
public boolean isCompletedExceptionally()
```

Returns

true

if this CompletableFuture completed
exceptionally, in any way. Possible causes include
cancellation, explicit invocation of

completeExceptionally

, and abrupt termination of a
CompletionStage action.

**Returns:** true

if this CompletableFuture completed
exceptionally

- obtrudeValue

```java
public void obtrudeValue​(
T
value)
```

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:** value

- the completion value

- obtrudeException

```java
public void obtrudeException​(
Throwable
ex)
```

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:** ex

- the exception
**Throws:** NullPointerException

- if the exception is null

- getNumberOfDependents

```java
public int getNumberOfDependents()
```

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.
This method is designed for use in monitoring system state, not
for synchronization control.

**Returns:** the number of dependent CompletableFutures

- toString

```java
public
String
toString()
```

Returns a string identifying this CompletableFuture, as well as
its completion state. The state, in brackets, contains the
String

"Completed Normally"

or the String

"Completed Exceptionally"

, or the String

"Not
completed"

followed by the number of CompletableFutures
dependent upon its completion, if any.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this CompletableFuture, as well as its state

- newIncompleteFuture

```java
public <U>
CompletableFuture
<U> newIncompleteFuture()
```

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method. Subclasses should
normally override this method to return an instance of the same
class as this CompletableFuture. The default implementation
returns an instance of class CompletableFuture.

**Type Parameters:** U

- the type of the value
**Returns:** a new CompletableFuture
**Since:** 9

- defaultExecutor

```java
public
Executor
defaultExecutor()
```

Returns the default Executor used for async methods that do not
specify an Executor. This class uses the

ForkJoinPool.commonPool()

if it supports more than one
parallel thread, or else an Executor using one thread per async
task. This method may be overridden in subclasses to return
an Executor that provides at least one independent thread.

**Returns:** the executor
**Since:** 9

- copy

```java
public
CompletableFuture
<
T
> copy()
```

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally. If this CompletableFuture completes exceptionally,
then the returned CompletableFuture completes exceptionally
with a CompletionException with this exception as cause. The
behavior is equivalent to

thenApply(x -> x)

. This
method may be useful as a form of "defensive copying", to
prevent clients from completing, while still being able to
arrange dependent actions.

**Returns:** the new CompletableFuture
**Since:** 9

- minimalCompletionStage

```java
public
CompletionStage
<
T
> minimalCompletionStage()
```

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

. If this CompletableFuture completes
exceptionally, then the returned CompletionStage completes
exceptionally with a CompletionException with this exception as
cause.

Unless overridden by a subclass, a new non-minimal
CompletableFuture with all methods available can be obtained from
a minimal CompletionStage via

toCompletableFuture()

.
For example, completion of a minimal stage can be awaited by

```java
minimalStage.toCompletableFuture().join();
```

**Returns:** the new CompletionStage
**Since:** 9

- completeAsync

```java
public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier,

Executor
executor)
```

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

**Parameters:** supplier

- a function returning the value to be used
to complete this CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** this CompletableFuture
**Since:** 9

- completeAsync

```java
public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier)
```

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

**Parameters:** supplier

- a function returning the value to be used
to complete this CompletableFuture
**Returns:** this CompletableFuture
**Since:** 9

- orTimeout

```java
public
CompletableFuture
<
T
> orTimeout​(long timeout,

TimeUnit
unit)
```

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

**Parameters:** timeout

- how long to wait before completing exceptionally
with a TimeoutException, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** this CompletableFuture
**Since:** 9

- completeOnTimeout

```java
public
CompletableFuture
<
T
> completeOnTimeout​(
T
value,
long timeout,

TimeUnit
unit)
```

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

**Parameters:** value

- the value to use upon timeout
**Parameters:** timeout

- how long to wait before completing normally
with the given value, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** this CompletableFuture
**Since:** 9

- delayedExecutor

```java
public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit,

Executor
executor)
```

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:** delay

- how long to delay, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

delay

parameter
**Parameters:** executor

- the base executor
**Returns:** the new delayed executor
**Since:** 9

- delayedExecutor

```java
public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit)
```

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:** delay

- how long to delay, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

delay

parameter
**Returns:** the new delayed executor
**Since:** 9

- completedStage

```java
public static <U>
CompletionStage
<U> completedStage​(U value)
```

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

**Type Parameters:** U

- the type of the value
**Parameters:** value

- the value
**Returns:** the completed CompletionStage
**Since:** 9

- failedFuture

```java
public static <U>
CompletableFuture
<U> failedFuture​(
Throwable
ex)
```

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

**Type Parameters:** U

- the type of the value
**Parameters:** ex

- the exception
**Returns:** the exceptionally completed CompletableFuture
**Since:** 9

- failedStage

```java
public static <U>
CompletionStage
<U> failedStage​(
Throwable
ex)
```

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

**Type Parameters:** U

- the type of the value
**Parameters:** ex

- the exception
**Returns:** the exceptionally completed CompletionStage
**Since:** 9

Constructor Detail

- CompletableFuture

```java
public CompletableFuture()
```

Creates a new incomplete CompletableFuture.

---

#### Constructor Detail

CompletableFuture

```java
public CompletableFuture()
```

Creates a new incomplete CompletableFuture.

---

#### CompletableFuture

public CompletableFuture()

Creates a new incomplete CompletableFuture.

Method Detail

- supplyAsync

```java
public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

**Type Parameters:** U

- the function's return type
**Parameters:** supplier

- a function returning the value to be used
to complete the returned CompletableFuture
**Returns:** the new CompletableFuture

- supplyAsync

```java
public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier,

Executor
executor)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

**Type Parameters:** U

- the function's return type
**Parameters:** supplier

- a function returning the value to be used
to complete the returned CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletableFuture

- runAsync

```java
public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

**Parameters:** runnable

- the action to run before completing the
returned CompletableFuture
**Returns:** the new CompletableFuture

- runAsync

```java
public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable,

Executor
executor)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

**Parameters:** runnable

- the action to run before completing the
returned CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletableFuture

- completedFuture

```java
public static <U>
CompletableFuture
<U> completedFuture​(U value)
```

Returns a new CompletableFuture that is already completed with
the given value.

**Type Parameters:** U

- the type of the value
**Parameters:** value

- the value
**Returns:** the completed CompletableFuture

- isDone

```java
public boolean isDone()
```

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

**Specified by:** isDone

in interface

Future

<

T

>
**Returns:** true

if completed

- get

```java
public
T
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for this future to complete, and then
returns its result.

**Specified by:** get

in interface

Future

<

T

>
**Returns:** the result value
**Throws:** CancellationException

- if this future was cancelled
**Throws:** ExecutionException

- if this future completed exceptionally
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting

- get

```java
public
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException
```

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

**Specified by:** get

in interface

Future

<

T

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the result value
**Throws:** CancellationException

- if this future was cancelled
**Throws:** ExecutionException

- if this future completed exceptionally
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** TimeoutException

- if the wait timed out

- join

```java
public
T
join()
```

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally. To better
conform with the use of common functional forms, if a
computation involved in the completion of this
CompletableFuture threw an exception, this method throws an
(unchecked)

CompletionException

with the underlying
exception as its cause.

**Returns:** the result value
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

- getNow

```java
public
T
getNow​(
T
valueIfAbsent)
```

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

**Parameters:** valueIfAbsent

- the value to return if not completed
**Returns:** the result value, if completed, else the given valueIfAbsent
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

- complete

```java
public boolean complete​(
T
value)
```

If not already completed, sets the value returned by

get()

and related methods to the given value.

**Parameters:** value

- the result value
**Returns:** true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

- completeExceptionally

```java
public boolean completeExceptionally​(
Throwable
ex)
```

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

**Parameters:** ex

- the exception
**Returns:** true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

- toCompletableFuture

```java
public
CompletableFuture
<
T
> toCompletableFuture()
```

Returns this CompletableFuture.

**Specified by:** toCompletableFuture

in interface

CompletionStage

<

T

>
**Returns:** this CompletableFuture

- exceptionally

```java
public
CompletableFuture
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)
```

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.
Note: More flexible versions of this functionality are
available using methods

whenComplete

and

handle

.

**Specified by:** exceptionally

in interface

CompletionStage

<

T

>
**Parameters:** fn

- the function to use to compute the value of the
returned CompletableFuture if this CompletableFuture completed
exceptionally
**Returns:** the new CompletableFuture

- allOf

```java
public static
CompletableFuture
<
Void
> allOf​(
CompletableFuture
<?>... cfs)
```

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete. If any of the given
CompletableFutures complete exceptionally, then the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. Otherwise, the results,
if any, of the given CompletableFutures are not reflected in
the returned CompletableFuture, but may be obtained by
inspecting them individually. If no CompletableFutures are
provided, returns a CompletableFuture completed with the value

null

.

Among the applications of this method is to await completion
of a set of independent CompletableFutures before continuing a
program, as in:

CompletableFuture.allOf(c1, c2,
c3).join();

.

**Parameters:** cfs

- the CompletableFutures
**Returns:** a new CompletableFuture that is completed when all of the
given CompletableFutures complete
**Throws:** NullPointerException

- if the array or any of its elements are

null

- anyOf

```java
public static
CompletableFuture
<
Object
> anyOf​(
CompletableFuture
<?>... cfs)
```

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.
Otherwise, if it completed exceptionally, the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. If no CompletableFutures
are provided, returns an incomplete CompletableFuture.

**Parameters:** cfs

- the CompletableFutures
**Returns:** a new CompletableFuture that is completed with the
result or exception of any of the given CompletableFutures when
one completes
**Throws:** NullPointerException

- if the array or any of its elements are

null

- cancel

```java
public boolean cancel​(boolean mayInterruptIfRunning)
```

If not already completed, completes this CompletableFuture with
a

CancellationException

. Dependent CompletableFutures
that have not already completed will also complete
exceptionally, with a

CompletionException

caused by
this

CancellationException

.

**Specified by:** cancel

in interface

Future

<

T

>
**Parameters:** mayInterruptIfRunning

- this value has no effect in this
implementation because interrupts are not used to control
processing.
**Returns:** true

if this task is now cancelled

- isCancelled

```java
public boolean isCancelled()
```

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

**Specified by:** isCancelled

in interface

Future

<

T

>
**Returns:** true

if this CompletableFuture was cancelled
before it completed normally

- isCompletedExceptionally

```java
public boolean isCompletedExceptionally()
```

Returns

true

if this CompletableFuture completed
exceptionally, in any way. Possible causes include
cancellation, explicit invocation of

completeExceptionally

, and abrupt termination of a
CompletionStage action.

**Returns:** true

if this CompletableFuture completed
exceptionally

- obtrudeValue

```java
public void obtrudeValue​(
T
value)
```

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:** value

- the completion value

- obtrudeException

```java
public void obtrudeException​(
Throwable
ex)
```

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:** ex

- the exception
**Throws:** NullPointerException

- if the exception is null

- getNumberOfDependents

```java
public int getNumberOfDependents()
```

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.
This method is designed for use in monitoring system state, not
for synchronization control.

**Returns:** the number of dependent CompletableFutures

- toString

```java
public
String
toString()
```

Returns a string identifying this CompletableFuture, as well as
its completion state. The state, in brackets, contains the
String

"Completed Normally"

or the String

"Completed Exceptionally"

, or the String

"Not
completed"

followed by the number of CompletableFutures
dependent upon its completion, if any.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this CompletableFuture, as well as its state

- newIncompleteFuture

```java
public <U>
CompletableFuture
<U> newIncompleteFuture()
```

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method. Subclasses should
normally override this method to return an instance of the same
class as this CompletableFuture. The default implementation
returns an instance of class CompletableFuture.

**Type Parameters:** U

- the type of the value
**Returns:** a new CompletableFuture
**Since:** 9

- defaultExecutor

```java
public
Executor
defaultExecutor()
```

Returns the default Executor used for async methods that do not
specify an Executor. This class uses the

ForkJoinPool.commonPool()

if it supports more than one
parallel thread, or else an Executor using one thread per async
task. This method may be overridden in subclasses to return
an Executor that provides at least one independent thread.

**Returns:** the executor
**Since:** 9

- copy

```java
public
CompletableFuture
<
T
> copy()
```

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally. If this CompletableFuture completes exceptionally,
then the returned CompletableFuture completes exceptionally
with a CompletionException with this exception as cause. The
behavior is equivalent to

thenApply(x -> x)

. This
method may be useful as a form of "defensive copying", to
prevent clients from completing, while still being able to
arrange dependent actions.

**Returns:** the new CompletableFuture
**Since:** 9

- minimalCompletionStage

```java
public
CompletionStage
<
T
> minimalCompletionStage()
```

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

. If this CompletableFuture completes
exceptionally, then the returned CompletionStage completes
exceptionally with a CompletionException with this exception as
cause.

Unless overridden by a subclass, a new non-minimal
CompletableFuture with all methods available can be obtained from
a minimal CompletionStage via

toCompletableFuture()

.
For example, completion of a minimal stage can be awaited by

```java
minimalStage.toCompletableFuture().join();
```

**Returns:** the new CompletionStage
**Since:** 9

- completeAsync

```java
public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier,

Executor
executor)
```

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

**Parameters:** supplier

- a function returning the value to be used
to complete this CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** this CompletableFuture
**Since:** 9

- completeAsync

```java
public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier)
```

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

**Parameters:** supplier

- a function returning the value to be used
to complete this CompletableFuture
**Returns:** this CompletableFuture
**Since:** 9

- orTimeout

```java
public
CompletableFuture
<
T
> orTimeout​(long timeout,

TimeUnit
unit)
```

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

**Parameters:** timeout

- how long to wait before completing exceptionally
with a TimeoutException, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** this CompletableFuture
**Since:** 9

- completeOnTimeout

```java
public
CompletableFuture
<
T
> completeOnTimeout​(
T
value,
long timeout,

TimeUnit
unit)
```

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

**Parameters:** value

- the value to use upon timeout
**Parameters:** timeout

- how long to wait before completing normally
with the given value, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** this CompletableFuture
**Since:** 9

- delayedExecutor

```java
public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit,

Executor
executor)
```

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:** delay

- how long to delay, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

delay

parameter
**Parameters:** executor

- the base executor
**Returns:** the new delayed executor
**Since:** 9

- delayedExecutor

```java
public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit)
```

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:** delay

- how long to delay, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

delay

parameter
**Returns:** the new delayed executor
**Since:** 9

- completedStage

```java
public static <U>
CompletionStage
<U> completedStage​(U value)
```

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

**Type Parameters:** U

- the type of the value
**Parameters:** value

- the value
**Returns:** the completed CompletionStage
**Since:** 9

- failedFuture

```java
public static <U>
CompletableFuture
<U> failedFuture​(
Throwable
ex)
```

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

**Type Parameters:** U

- the type of the value
**Parameters:** ex

- the exception
**Returns:** the exceptionally completed CompletableFuture
**Since:** 9

- failedStage

```java
public static <U>
CompletionStage
<U> failedStage​(
Throwable
ex)
```

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

**Type Parameters:** U

- the type of the value
**Parameters:** ex

- the exception
**Returns:** the exceptionally completed CompletionStage
**Since:** 9

---

#### Method Detail

supplyAsync

```java
public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

**Type Parameters:** U

- the function's return type
**Parameters:** supplier

- a function returning the value to be used
to complete the returned CompletableFuture
**Returns:** the new CompletableFuture

---

#### supplyAsync

public static <U>

CompletableFuture

<U> supplyAsync​(

Supplier

<U> supplier)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

with
the value obtained by calling the given Supplier.

supplyAsync

```java
public static <U>
CompletableFuture
<U> supplyAsync​(
Supplier
<U> supplier,

Executor
executor)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

**Type Parameters:** U

- the function's return type
**Parameters:** supplier

- a function returning the value to be used
to complete the returned CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletableFuture

---

#### supplyAsync

public static <U>

CompletableFuture

<U> supplyAsync​(

Supplier

<U> supplier,

Executor

executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.

runAsync

```java
public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

**Parameters:** runnable

- the action to run before completing the
returned CompletableFuture
**Returns:** the new CompletableFuture

---

#### runAsync

public static

CompletableFuture

<

Void

> runAsync​(

Runnable

runnable)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the

ForkJoinPool.commonPool()

after
it runs the given action.

runAsync

```java
public static
CompletableFuture
<
Void
> runAsync​(
Runnable
runnable,

Executor
executor)
```

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

**Parameters:** runnable

- the action to run before completing the
returned CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletableFuture

---

#### runAsync

public static

CompletableFuture

<

Void

> runAsync​(

Runnable

runnable,

Executor

executor)

Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.

completedFuture

```java
public static <U>
CompletableFuture
<U> completedFuture​(U value)
```

Returns a new CompletableFuture that is already completed with
the given value.

**Type Parameters:** U

- the type of the value
**Parameters:** value

- the value
**Returns:** the completed CompletableFuture

---

#### completedFuture

public static <U>

CompletableFuture

<U> completedFuture​(U value)

Returns a new CompletableFuture that is already completed with
the given value.

isDone

```java
public boolean isDone()
```

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

**Specified by:** isDone

in interface

Future

<

T

>
**Returns:** true

if completed

---

#### isDone

public boolean isDone()

Returns

true

if completed in any fashion: normally,
exceptionally, or via cancellation.

get

```java
public
T
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for this future to complete, and then
returns its result.

**Specified by:** get

in interface

Future

<

T

>
**Returns:** the result value
**Throws:** CancellationException

- if this future was cancelled
**Throws:** ExecutionException

- if this future completed exceptionally
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting

---

#### get

public

T

get()
throws

InterruptedException

,

ExecutionException

Waits if necessary for this future to complete, and then
returns its result.

get

```java
public
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException
```

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

**Specified by:** get

in interface

Future

<

T

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the result value
**Throws:** CancellationException

- if this future was cancelled
**Throws:** ExecutionException

- if this future completed exceptionally
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** TimeoutException

- if the wait timed out

---

#### get

public

T

get​(long timeout,

TimeUnit

unit)
throws

InterruptedException

,

ExecutionException

,

TimeoutException

Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.

join

```java
public
T
join()
```

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally. To better
conform with the use of common functional forms, if a
computation involved in the completion of this
CompletableFuture threw an exception, this method throws an
(unchecked)

CompletionException

with the underlying
exception as its cause.

**Returns:** the result value
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

---

#### join

public

T

join()

Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally. To better
conform with the use of common functional forms, if a
computation involved in the completion of this
CompletableFuture threw an exception, this method throws an
(unchecked)

CompletionException

with the underlying
exception as its cause.

getNow

```java
public
T
getNow​(
T
valueIfAbsent)
```

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

**Parameters:** valueIfAbsent

- the value to return if not completed
**Returns:** the result value, if completed, else the given valueIfAbsent
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** CompletionException

- if this future completed
exceptionally or a completion computation threw an exception

---

#### getNow

public

T

getNow​(

T

valueIfAbsent)

Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.

complete

```java
public boolean complete​(
T
value)
```

If not already completed, sets the value returned by

get()

and related methods to the given value.

**Parameters:** value

- the result value
**Returns:** true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

---

#### complete

public boolean complete​(

T

value)

If not already completed, sets the value returned by

get()

and related methods to the given value.

completeExceptionally

```java
public boolean completeExceptionally​(
Throwable
ex)
```

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

**Parameters:** ex

- the exception
**Returns:** true

if this invocation caused this CompletableFuture
to transition to a completed state, else

false

---

#### completeExceptionally

public boolean completeExceptionally​(

Throwable

ex)

If not already completed, causes invocations of

get()

and related methods to throw the given exception.

toCompletableFuture

```java
public
CompletableFuture
<
T
> toCompletableFuture()
```

Returns this CompletableFuture.

**Specified by:** toCompletableFuture

in interface

CompletionStage

<

T

>
**Returns:** this CompletableFuture

---

#### toCompletableFuture

public

CompletableFuture

<

T

> toCompletableFuture()

Returns this CompletableFuture.

exceptionally

```java
public
CompletableFuture
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)
```

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.
Note: More flexible versions of this functionality are
available using methods

whenComplete

and

handle

.

**Specified by:** exceptionally

in interface

CompletionStage

<

T

>
**Parameters:** fn

- the function to use to compute the value of the
returned CompletableFuture if this CompletableFuture completed
exceptionally
**Returns:** the new CompletableFuture

---

#### exceptionally

public

CompletableFuture

<

T

> exceptionally​(

Function

<

Throwable

,​? extends

T

> fn)

Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.
Note: More flexible versions of this functionality are
available using methods

whenComplete

and

handle

.

allOf

```java
public static
CompletableFuture
<
Void
> allOf​(
CompletableFuture
<?>... cfs)
```

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete. If any of the given
CompletableFutures complete exceptionally, then the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. Otherwise, the results,
if any, of the given CompletableFutures are not reflected in
the returned CompletableFuture, but may be obtained by
inspecting them individually. If no CompletableFutures are
provided, returns a CompletableFuture completed with the value

null

.

Among the applications of this method is to await completion
of a set of independent CompletableFutures before continuing a
program, as in:

CompletableFuture.allOf(c1, c2,
c3).join();

.

**Parameters:** cfs

- the CompletableFutures
**Returns:** a new CompletableFuture that is completed when all of the
given CompletableFutures complete
**Throws:** NullPointerException

- if the array or any of its elements are

null

---

#### allOf

public static

CompletableFuture

<

Void

> allOf​(

CompletableFuture

<?>... cfs)

Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete. If any of the given
CompletableFutures complete exceptionally, then the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. Otherwise, the results,
if any, of the given CompletableFutures are not reflected in
the returned CompletableFuture, but may be obtained by
inspecting them individually. If no CompletableFutures are
provided, returns a CompletableFuture completed with the value

null

.

Among the applications of this method is to await completion
of a set of independent CompletableFutures before continuing a
program, as in:

CompletableFuture.allOf(c1, c2,
c3).join();

.

Among the applications of this method is to await completion
of a set of independent CompletableFutures before continuing a
program, as in:

CompletableFuture.allOf(c1, c2,
c3).join();

.

anyOf

```java
public static
CompletableFuture
<
Object
> anyOf​(
CompletableFuture
<?>... cfs)
```

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.
Otherwise, if it completed exceptionally, the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. If no CompletableFutures
are provided, returns an incomplete CompletableFuture.

**Parameters:** cfs

- the CompletableFutures
**Returns:** a new CompletableFuture that is completed with the
result or exception of any of the given CompletableFutures when
one completes
**Throws:** NullPointerException

- if the array or any of its elements are

null

---

#### anyOf

public static

CompletableFuture

<

Object

> anyOf​(

CompletableFuture

<?>... cfs)

Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.
Otherwise, if it completed exceptionally, the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. If no CompletableFutures
are provided, returns an incomplete CompletableFuture.

cancel

```java
public boolean cancel​(boolean mayInterruptIfRunning)
```

If not already completed, completes this CompletableFuture with
a

CancellationException

. Dependent CompletableFutures
that have not already completed will also complete
exceptionally, with a

CompletionException

caused by
this

CancellationException

.

**Specified by:** cancel

in interface

Future

<

T

>
**Parameters:** mayInterruptIfRunning

- this value has no effect in this
implementation because interrupts are not used to control
processing.
**Returns:** true

if this task is now cancelled

---

#### cancel

public boolean cancel​(boolean mayInterruptIfRunning)

If not already completed, completes this CompletableFuture with
a

CancellationException

. Dependent CompletableFutures
that have not already completed will also complete
exceptionally, with a

CompletionException

caused by
this

CancellationException

.

isCancelled

```java
public boolean isCancelled()
```

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

**Specified by:** isCancelled

in interface

Future

<

T

>
**Returns:** true

if this CompletableFuture was cancelled
before it completed normally

---

#### isCancelled

public boolean isCancelled()

Returns

true

if this CompletableFuture was cancelled
before it completed normally.

isCompletedExceptionally

```java
public boolean isCompletedExceptionally()
```

Returns

true

if this CompletableFuture completed
exceptionally, in any way. Possible causes include
cancellation, explicit invocation of

completeExceptionally

, and abrupt termination of a
CompletionStage action.

**Returns:** true

if this CompletableFuture completed
exceptionally

---

#### isCompletedExceptionally

public boolean isCompletedExceptionally()

Returns

true

if this CompletableFuture completed
exceptionally, in any way. Possible causes include
cancellation, explicit invocation of

completeExceptionally

, and abrupt termination of a
CompletionStage action.

obtrudeValue

```java
public void obtrudeValue​(
T
value)
```

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:** value

- the completion value

---

#### obtrudeValue

public void obtrudeValue​(

T

value)

Forcibly sets or resets the value subsequently returned by
method

get()

and related methods, whether or not
already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

obtrudeException

```java
public void obtrudeException​(
Throwable
ex)
```

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

**Parameters:** ex

- the exception
**Throws:** NullPointerException

- if the exception is null

---

#### obtrudeException

public void obtrudeException​(

Throwable

ex)

Forcibly causes subsequent invocations of method

get()

and related methods to throw the given exception, whether or
not already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.

getNumberOfDependents

```java
public int getNumberOfDependents()
```

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.
This method is designed for use in monitoring system state, not
for synchronization control.

**Returns:** the number of dependent CompletableFutures

---

#### getNumberOfDependents

public int getNumberOfDependents()

Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.
This method is designed for use in monitoring system state, not
for synchronization control.

toString

```java
public
String
toString()
```

Returns a string identifying this CompletableFuture, as well as
its completion state. The state, in brackets, contains the
String

"Completed Normally"

or the String

"Completed Exceptionally"

, or the String

"Not
completed"

followed by the number of CompletableFutures
dependent upon its completion, if any.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this CompletableFuture, as well as its state

---

#### toString

public

String

toString()

Returns a string identifying this CompletableFuture, as well as
its completion state. The state, in brackets, contains the
String

"Completed Normally"

or the String

"Completed Exceptionally"

, or the String

"Not
completed"

followed by the number of CompletableFutures
dependent upon its completion, if any.

newIncompleteFuture

```java
public <U>
CompletableFuture
<U> newIncompleteFuture()
```

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method. Subclasses should
normally override this method to return an instance of the same
class as this CompletableFuture. The default implementation
returns an instance of class CompletableFuture.

**Type Parameters:** U

- the type of the value
**Returns:** a new CompletableFuture
**Since:** 9

---

#### newIncompleteFuture

public <U>

CompletableFuture

<U> newIncompleteFuture()

Returns a new incomplete CompletableFuture of the type to be
returned by a CompletionStage method. Subclasses should
normally override this method to return an instance of the same
class as this CompletableFuture. The default implementation
returns an instance of class CompletableFuture.

defaultExecutor

```java
public
Executor
defaultExecutor()
```

Returns the default Executor used for async methods that do not
specify an Executor. This class uses the

ForkJoinPool.commonPool()

if it supports more than one
parallel thread, or else an Executor using one thread per async
task. This method may be overridden in subclasses to return
an Executor that provides at least one independent thread.

**Returns:** the executor
**Since:** 9

---

#### defaultExecutor

public

Executor

defaultExecutor()

Returns the default Executor used for async methods that do not
specify an Executor. This class uses the

ForkJoinPool.commonPool()

if it supports more than one
parallel thread, or else an Executor using one thread per async
task. This method may be overridden in subclasses to return
an Executor that provides at least one independent thread.

copy

```java
public
CompletableFuture
<
T
> copy()
```

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally. If this CompletableFuture completes exceptionally,
then the returned CompletableFuture completes exceptionally
with a CompletionException with this exception as cause. The
behavior is equivalent to

thenApply(x -> x)

. This
method may be useful as a form of "defensive copying", to
prevent clients from completing, while still being able to
arrange dependent actions.

**Returns:** the new CompletableFuture
**Since:** 9

---

#### copy

public

CompletableFuture

<

T

> copy()

Returns a new CompletableFuture that is completed normally with
the same value as this CompletableFuture when it completes
normally. If this CompletableFuture completes exceptionally,
then the returned CompletableFuture completes exceptionally
with a CompletionException with this exception as cause. The
behavior is equivalent to

thenApply(x -> x)

. This
method may be useful as a form of "defensive copying", to
prevent clients from completing, while still being able to
arrange dependent actions.

minimalCompletionStage

```java
public
CompletionStage
<
T
> minimalCompletionStage()
```

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

. If this CompletableFuture completes
exceptionally, then the returned CompletionStage completes
exceptionally with a CompletionException with this exception as
cause.

Unless overridden by a subclass, a new non-minimal
CompletableFuture with all methods available can be obtained from
a minimal CompletionStage via

toCompletableFuture()

.
For example, completion of a minimal stage can be awaited by

```java
minimalStage.toCompletableFuture().join();
```

**Returns:** the new CompletionStage
**Since:** 9

---

#### minimalCompletionStage

public

CompletionStage

<

T

> minimalCompletionStage()

Returns a new CompletionStage that is completed normally with
the same value as this CompletableFuture when it completes
normally, and cannot be independently completed or otherwise
used in ways not defined by the methods of interface

CompletionStage

. If this CompletableFuture completes
exceptionally, then the returned CompletionStage completes
exceptionally with a CompletionException with this exception as
cause.

Unless overridden by a subclass, a new non-minimal
CompletableFuture with all methods available can be obtained from
a minimal CompletionStage via

toCompletableFuture()

.
For example, completion of a minimal stage can be awaited by

```java
minimalStage.toCompletableFuture().join();
```

Unless overridden by a subclass, a new non-minimal
CompletableFuture with all methods available can be obtained from
a minimal CompletionStage via

toCompletableFuture()

.
For example, completion of a minimal stage can be awaited by

```java
minimalStage.toCompletableFuture().join();
```

minimalStage.toCompletableFuture().join();

completeAsync

```java
public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier,

Executor
executor)
```

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

**Parameters:** supplier

- a function returning the value to be used
to complete this CompletableFuture
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** this CompletableFuture
**Since:** 9

---

#### completeAsync

public

CompletableFuture

<

T

> completeAsync​(

Supplier

<? extends

T

> supplier,

Executor

executor)

Completes this CompletableFuture with the result of
the given Supplier function invoked from an asynchronous
task using the given executor.

completeAsync

```java
public
CompletableFuture
<
T
> completeAsync​(
Supplier
<? extends
T
> supplier)
```

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

**Parameters:** supplier

- a function returning the value to be used
to complete this CompletableFuture
**Returns:** this CompletableFuture
**Since:** 9

---

#### completeAsync

public

CompletableFuture

<

T

> completeAsync​(

Supplier

<? extends

T

> supplier)

Completes this CompletableFuture with the result of the given
Supplier function invoked from an asynchronous task using the
default executor.

orTimeout

```java
public
CompletableFuture
<
T
> orTimeout​(long timeout,

TimeUnit
unit)
```

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

**Parameters:** timeout

- how long to wait before completing exceptionally
with a TimeoutException, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** this CompletableFuture
**Since:** 9

---

#### orTimeout

public

CompletableFuture

<

T

> orTimeout​(long timeout,

TimeUnit

unit)

Exceptionally completes this CompletableFuture with
a

TimeoutException

if not otherwise completed
before the given timeout.

completeOnTimeout

```java
public
CompletableFuture
<
T
> completeOnTimeout​(
T
value,
long timeout,

TimeUnit
unit)
```

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

**Parameters:** value

- the value to use upon timeout
**Parameters:** timeout

- how long to wait before completing normally
with the given value, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** this CompletableFuture
**Since:** 9

---

#### completeOnTimeout

public

CompletableFuture

<

T

> completeOnTimeout​(

T

value,
long timeout,

TimeUnit

unit)

Completes this CompletableFuture with the given value if not
otherwise completed before the given timeout.

delayedExecutor

```java
public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit,

Executor
executor)
```

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:** delay

- how long to delay, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

delay

parameter
**Parameters:** executor

- the base executor
**Returns:** the new delayed executor
**Since:** 9

---

#### delayedExecutor

public static

Executor

delayedExecutor​(long delay,

TimeUnit

unit,

Executor

executor)

Returns a new Executor that submits a task to the given base
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

delayedExecutor

```java
public static
Executor
delayedExecutor​(long delay,

TimeUnit
unit)
```

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

**Parameters:** delay

- how long to delay, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

delay

parameter
**Returns:** the new delayed executor
**Since:** 9

---

#### delayedExecutor

public static

Executor

delayedExecutor​(long delay,

TimeUnit

unit)

Returns a new Executor that submits a task to the default
executor after the given delay (or no delay if non-positive).
Each delay commences upon invocation of the returned executor's

execute

method.

completedStage

```java
public static <U>
CompletionStage
<U> completedStage​(U value)
```

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

**Type Parameters:** U

- the type of the value
**Parameters:** value

- the value
**Returns:** the completed CompletionStage
**Since:** 9

---

#### completedStage

public static <U>

CompletionStage

<U> completedStage​(U value)

Returns a new CompletionStage that is already completed with
the given value and supports only those methods in
interface

CompletionStage

.

failedFuture

```java
public static <U>
CompletableFuture
<U> failedFuture​(
Throwable
ex)
```

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

**Type Parameters:** U

- the type of the value
**Parameters:** ex

- the exception
**Returns:** the exceptionally completed CompletableFuture
**Since:** 9

---

#### failedFuture

public static <U>

CompletableFuture

<U> failedFuture​(

Throwable

ex)

Returns a new CompletableFuture that is already completed
exceptionally with the given exception.

failedStage

```java
public static <U>
CompletionStage
<U> failedStage​(
Throwable
ex)
```

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

**Type Parameters:** U

- the type of the value
**Parameters:** ex

- the exception
**Returns:** the exceptionally completed CompletionStage
**Since:** 9

---

#### failedStage

public static <U>

CompletionStage

<U> failedStage​(

Throwable

ex)

Returns a new CompletionStage that is already completed
exceptionally with the given exception and supports only those
methods in interface

CompletionStage

.

---

