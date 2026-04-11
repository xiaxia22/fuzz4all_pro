# Interface Future<V>

**Source:** `java.base\java\util\concurrent\Future.html`

### Class Description

```java
public interface
Future<V>
```

A

Future

represents the result of an asynchronous
computation. Methods are provided to check if the computation is
complete, to wait for its completion, and to retrieve the result of
the computation. The result can only be retrieved using method

get

when the computation has completed, blocking if
necessary until it is ready. Cancellation is performed by the

cancel

method. Additional methods are provided to
determine if the task completed normally or was cancelled. Once a
computation has completed, the computation cannot be cancelled.
If you would like to use a

Future

for the sake
of cancellability but not provide a usable result, you can
declare types of the form

Future<?>

and
return

null

as a result of the underlying task.

Sample Usage

(Note that the following classes are all
made-up.)

```java
interface ArchiveSearcher { String search(String target); }
class App {
ExecutorService executor = ...
ArchiveSearcher searcher = ...
void showSearch(String target) throws InterruptedException {
Callable<String> task = () -> searcher.search(target);
Future<String> future = executor.submit(task);
displayOtherThings(); // do other things while searching
try {
displayText(future.get()); // use future
} catch (ExecutionException ex) { cleanup(); return; }
}
}
```

The

FutureTask

class is an implementation of

Future

that
implements

Runnable

, and so may be executed by an

Executor

.
For example, the above construction with

submit

could be replaced by:

```java
FutureTask<String> future = new FutureTask<>(task);
executor.execute(future);
```

Memory consistency effects: Actions taken by the asynchronous computation

happen-before

actions following the corresponding

Future.get()

in another thread.

**Type Parameters:** V

- The result type returned by this Future's

get

method

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean cancel​(boolean mayInterruptIfRunning)

Attempts to cancel execution of this task. This attempt will
fail if the task has already completed, has already been cancelled,
or could not be cancelled for some other reason. If successful,
and this task has not started when

cancel

is called,
this task should never run. If the task has already started,
then the

mayInterruptIfRunning

parameter determines
whether the thread executing this task should be interrupted in
an attempt to stop the task.

After this method returns, subsequent calls to

isDone()

will
always return

true

. Subsequent calls to

isCancelled()

will always return

true

if this method returned

true

.

**Parameters:**
- mayInterruptIfRunning

-

true

if the thread executing this
task should be interrupted; otherwise, in-progress tasks are allowed
to complete

**Returns:**
- false

if the task could not be cancelled,
typically because it has already completed normally;

true

otherwise

---

#### boolean isCancelled()

Returns

true

if this task was cancelled before it completed
normally.

**Returns:**
- true

if this task was cancelled before it completed

---

#### boolean isDone()

Returns

true

if this task completed.

Completion may be due to normal termination, an exception, or
cancellation -- in all of these cases, this method will return

true

.

**Returns:**
- true

if this task completed

---

#### V
get()
throws
InterruptedException
,

ExecutionException

Waits if necessary for the computation to complete, and then
retrieves its result.

**Returns:**
- the computed result

**Throws:**
- CancellationException

- if the computation was cancelled
- ExecutionException

- if the computation threw an
exception
- InterruptedException

- if the current thread was interrupted
while waiting

---

#### V
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

**Parameters:**
- timeout

- the maximum time to wait
- unit

- the time unit of the timeout argument

**Returns:**
- the computed result

**Throws:**
- CancellationException

- if the computation was cancelled
- ExecutionException

- if the computation threw an
exception
- InterruptedException

- if the current thread was interrupted
while waiting
- TimeoutException

- if the wait timed out

---

### Additional Sections

#### Interface Future<V>

**Type Parameters:** V

- The result type returned by this Future's

get

method

**All Known Subinterfaces:** RunnableFuture

<V>

,

RunnableScheduledFuture

<V>

,

ScheduledFuture

<V>

**All Known Implementing Classes:** CompletableFuture

,

CountedCompleter

,

ForkJoinTask

,

FutureTask

,

RecursiveAction

,

RecursiveTask

,

SwingWorker

```java
public interface
Future<V>
```

A

Future

represents the result of an asynchronous
computation. Methods are provided to check if the computation is
complete, to wait for its completion, and to retrieve the result of
the computation. The result can only be retrieved using method

get

when the computation has completed, blocking if
necessary until it is ready. Cancellation is performed by the

cancel

method. Additional methods are provided to
determine if the task completed normally or was cancelled. Once a
computation has completed, the computation cannot be cancelled.
If you would like to use a

Future

for the sake
of cancellability but not provide a usable result, you can
declare types of the form

Future<?>

and
return

null

as a result of the underlying task.

Sample Usage

(Note that the following classes are all
made-up.)

```java
interface ArchiveSearcher { String search(String target); }
class App {
ExecutorService executor = ...
ArchiveSearcher searcher = ...
void showSearch(String target) throws InterruptedException {
Callable<String> task = () -> searcher.search(target);
Future<String> future = executor.submit(task);
displayOtherThings(); // do other things while searching
try {
displayText(future.get()); // use future
} catch (ExecutionException ex) { cleanup(); return; }
}
}
```

The

FutureTask

class is an implementation of

Future

that
implements

Runnable

, and so may be executed by an

Executor

.
For example, the above construction with

submit

could be replaced by:

```java
FutureTask<String> future = new FutureTask<>(task);
executor.execute(future);
```

Memory consistency effects: Actions taken by the asynchronous computation

happen-before

actions following the corresponding

Future.get()

in another thread.

**Since:** 1.5
**See Also:** FutureTask

,

Executor

public interface

Future<V>

A

Future

represents the result of an asynchronous
computation. Methods are provided to check if the computation is
complete, to wait for its completion, and to retrieve the result of
the computation. The result can only be retrieved using method

get

when the computation has completed, blocking if
necessary until it is ready. Cancellation is performed by the

cancel

method. Additional methods are provided to
determine if the task completed normally or was cancelled. Once a
computation has completed, the computation cannot be cancelled.
If you would like to use a

Future

for the sake
of cancellability but not provide a usable result, you can
declare types of the form

Future<?>

and
return

null

as a result of the underlying task.

Sample Usage

(Note that the following classes are all
made-up.)

```java
interface ArchiveSearcher { String search(String target); }
class App {
ExecutorService executor = ...
ArchiveSearcher searcher = ...
void showSearch(String target) throws InterruptedException {
Callable<String> task = () -> searcher.search(target);
Future<String> future = executor.submit(task);
displayOtherThings(); // do other things while searching
try {
displayText(future.get()); // use future
} catch (ExecutionException ex) { cleanup(); return; }
}
}
```

The

FutureTask

class is an implementation of

Future

that
implements

Runnable

, and so may be executed by an

Executor

.
For example, the above construction with

submit

could be replaced by:

```java
FutureTask<String> future = new FutureTask<>(task);
executor.execute(future);
```

Memory consistency effects: Actions taken by the asynchronous computation

happen-before

actions following the corresponding

Future.get()

in another thread.

Sample Usage

(Note that the following classes are all
made-up.)

```java
interface ArchiveSearcher { String search(String target); }
class App {
ExecutorService executor = ...
ArchiveSearcher searcher = ...
void showSearch(String target) throws InterruptedException {
Callable<String> task = () -> searcher.search(target);
Future<String> future = executor.submit(task);
displayOtherThings(); // do other things while searching
try {
displayText(future.get()); // use future
} catch (ExecutionException ex) { cleanup(); return; }
}
}
```

The

FutureTask

class is an implementation of

Future

that
implements

Runnable

, and so may be executed by an

Executor

.
For example, the above construction with

submit

could be replaced by:

```java
FutureTask<String> future = new FutureTask<>(task);
executor.execute(future);
```

Memory consistency effects: Actions taken by the asynchronous computation

happen-before

actions following the corresponding

Future.get()

in another thread.

interface ArchiveSearcher { String search(String target); }
class App {
ExecutorService executor = ...
ArchiveSearcher searcher = ...
void showSearch(String target) throws InterruptedException {
Callable<String> task = () -> searcher.search(target);
Future<String> future = executor.submit(task);
displayOtherThings(); // do other things while searching
try {
displayText(future.get()); // use future
} catch (ExecutionException ex) { cleanup(); return; }
}
}

FutureTask<String> future = new FutureTask<>(task);
executor.execute(future);

Memory consistency effects: Actions taken by the asynchronous computation

happen-before

actions following the corresponding

Future.get()

in another thread.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

cancel

​(boolean mayInterruptIfRunning)

Attempts to cancel execution of this task.

V

get

()

Waits if necessary for the computation to complete, and then
retrieves its result.

V

get

​(long timeout,

TimeUnit

unit)

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

boolean

isCancelled

()

Returns

true

if this task was cancelled before it completed
normally.

boolean

isDone

()

Returns

true

if this task completed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

cancel

​(boolean mayInterruptIfRunning)

Attempts to cancel execution of this task.

V

get

()

Waits if necessary for the computation to complete, and then
retrieves its result.

V

get

​(long timeout,

TimeUnit

unit)

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

boolean

isCancelled

()

Returns

true

if this task was cancelled before it completed
normally.

boolean

isDone

()

Returns

true

if this task completed.

---

#### Method Summary

Attempts to cancel execution of this task.

Waits if necessary for the computation to complete, and then
retrieves its result.

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Returns

true

if this task was cancelled before it completed
normally.

Returns

true

if this task completed.

============ METHOD DETAIL ==========

- Method Detail

- cancel

```java
boolean cancel​(boolean mayInterruptIfRunning)
```

Attempts to cancel execution of this task. This attempt will
fail if the task has already completed, has already been cancelled,
or could not be cancelled for some other reason. If successful,
and this task has not started when

cancel

is called,
this task should never run. If the task has already started,
then the

mayInterruptIfRunning

parameter determines
whether the thread executing this task should be interrupted in
an attempt to stop the task.

After this method returns, subsequent calls to

isDone()

will
always return

true

. Subsequent calls to

isCancelled()

will always return

true

if this method returned

true

.

**Parameters:** mayInterruptIfRunning

-

true

if the thread executing this
task should be interrupted; otherwise, in-progress tasks are allowed
to complete
**Returns:** false

if the task could not be cancelled,
typically because it has already completed normally;

true

otherwise

- isCancelled

```java
boolean isCancelled()
```

Returns

true

if this task was cancelled before it completed
normally.

**Returns:** true

if this task was cancelled before it completed

- isDone

```java
boolean isDone()
```

Returns

true

if this task completed.

Completion may be due to normal termination, an exception, or
cancellation -- in all of these cases, this method will return

true

.

**Returns:** true

if this task completed

- get

```java
V
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for the computation to complete, and then
retrieves its result.

**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting

- get

```java
V
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

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** TimeoutException

- if the wait timed out

Method Detail

- cancel

```java
boolean cancel​(boolean mayInterruptIfRunning)
```

Attempts to cancel execution of this task. This attempt will
fail if the task has already completed, has already been cancelled,
or could not be cancelled for some other reason. If successful,
and this task has not started when

cancel

is called,
this task should never run. If the task has already started,
then the

mayInterruptIfRunning

parameter determines
whether the thread executing this task should be interrupted in
an attempt to stop the task.

After this method returns, subsequent calls to

isDone()

will
always return

true

. Subsequent calls to

isCancelled()

will always return

true

if this method returned

true

.

**Parameters:** mayInterruptIfRunning

-

true

if the thread executing this
task should be interrupted; otherwise, in-progress tasks are allowed
to complete
**Returns:** false

if the task could not be cancelled,
typically because it has already completed normally;

true

otherwise

- isCancelled

```java
boolean isCancelled()
```

Returns

true

if this task was cancelled before it completed
normally.

**Returns:** true

if this task was cancelled before it completed

- isDone

```java
boolean isDone()
```

Returns

true

if this task completed.

Completion may be due to normal termination, an exception, or
cancellation -- in all of these cases, this method will return

true

.

**Returns:** true

if this task completed

- get

```java
V
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for the computation to complete, and then
retrieves its result.

**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting

- get

```java
V
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

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** TimeoutException

- if the wait timed out

---

#### Method Detail

cancel

```java
boolean cancel​(boolean mayInterruptIfRunning)
```

Attempts to cancel execution of this task. This attempt will
fail if the task has already completed, has already been cancelled,
or could not be cancelled for some other reason. If successful,
and this task has not started when

cancel

is called,
this task should never run. If the task has already started,
then the

mayInterruptIfRunning

parameter determines
whether the thread executing this task should be interrupted in
an attempt to stop the task.

After this method returns, subsequent calls to

isDone()

will
always return

true

. Subsequent calls to

isCancelled()

will always return

true

if this method returned

true

.

**Parameters:** mayInterruptIfRunning

-

true

if the thread executing this
task should be interrupted; otherwise, in-progress tasks are allowed
to complete
**Returns:** false

if the task could not be cancelled,
typically because it has already completed normally;

true

otherwise

---

#### cancel

boolean cancel​(boolean mayInterruptIfRunning)

Attempts to cancel execution of this task. This attempt will
fail if the task has already completed, has already been cancelled,
or could not be cancelled for some other reason. If successful,
and this task has not started when

cancel

is called,
this task should never run. If the task has already started,
then the

mayInterruptIfRunning

parameter determines
whether the thread executing this task should be interrupted in
an attempt to stop the task.

After this method returns, subsequent calls to

isDone()

will
always return

true

. Subsequent calls to

isCancelled()

will always return

true

if this method returned

true

.

After this method returns, subsequent calls to

isDone()

will
always return

true

. Subsequent calls to

isCancelled()

will always return

true

if this method returned

true

.

isCancelled

```java
boolean isCancelled()
```

Returns

true

if this task was cancelled before it completed
normally.

**Returns:** true

if this task was cancelled before it completed

---

#### isCancelled

boolean isCancelled()

Returns

true

if this task was cancelled before it completed
normally.

isDone

```java
boolean isDone()
```

Returns

true

if this task completed.

Completion may be due to normal termination, an exception, or
cancellation -- in all of these cases, this method will return

true

.

**Returns:** true

if this task completed

---

#### isDone

boolean isDone()

Returns

true

if this task completed.

Completion may be due to normal termination, an exception, or
cancellation -- in all of these cases, this method will return

true

.

get

```java
V
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for the computation to complete, and then
retrieves its result.

**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting

---

#### get

V

get()
throws

InterruptedException

,

ExecutionException

Waits if necessary for the computation to complete, and then
retrieves its result.

get

```java
V
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

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** TimeoutException

- if the wait timed out

---

#### get

V

get​(long timeout,

TimeUnit

unit)
throws

InterruptedException

,

ExecutionException

,

TimeoutException

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

---

