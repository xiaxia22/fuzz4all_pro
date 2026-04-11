# Class ExecutorCompletionService<V>

**Source:** `java.base\java\util\concurrent\ExecutorCompletionService.html`

### Class Description

```java
public class
ExecutorCompletionService<V>

extends
Object

implements
CompletionService
<V>
```

A

CompletionService

that uses a supplied

Executor

to execute tasks. This class arranges that submitted tasks are,
upon completion, placed on a queue accessible using

take

.
The class is lightweight enough to be suitable for transient use
when processing groups of tasks.

Usage Examples.

Suppose you have a set of solvers for a certain problem, each
returning a value of some type

Result

, and would like to
run them concurrently, processing the results of each of them that
return a non-null value, in some method

use(Result r)

. You
could write this as:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException, ExecutionException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
solvers.forEach(cs::submit);
for (int i = solvers.size(); i > 0; i--) {
Result r = cs.take().get();
if (r != null)
use(r);
}
}
```

Suppose instead that you would like to use the first non-null result
of the set of tasks, ignoring any that encounter exceptions,
and cancelling all other tasks when the first one is ready:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
int n = solvers.size();
List<Future<Result>> futures = new ArrayList<>(n);
Result result = null;
try {
solvers.forEach(solver -> futures.add(cs.submit(solver)));
for (int i = n; i > 0; i--) {
try {
Result r = cs.take().get();
if (r != null) {
result = r;
break;
}
} catch (ExecutionException ignore) {}
}
} finally {
futures.forEach(future -> future.cancel(true));
}

if (result != null)
use(result);
}
```

**All Implemented Interfaces:** CompletionService

<V>

---

### Field Details

*No entries found.*

### Constructor Details

#### public ExecutorCompletionService​(
Executor
executor)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

**Parameters:**
- executor

- the executor to use

**Throws:**
- NullPointerException

- if executor is

null

---

#### public ExecutorCompletionService​(
Executor
executor,

BlockingQueue
<
Future
<
V
>> completionQueue)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

**Parameters:**
- executor

- the executor to use
- completionQueue

- the queue to use as the completion queue
normally one dedicated for use by this service. This
queue is treated as unbounded -- failed attempted

Queue.add

operations for completed tasks cause
them not to be retrievable.

**Throws:**
- NullPointerException

- if executor or completionQueue are

null

---

### Method Details

#### public
Future
<
V
> submit​(
Callable
<
V
> task)

Description copied from interface:

CompletionService

**Specified by:**
- submit

in interface

CompletionService

<

V

>

**Parameters:**
- task

- the task to submit

**Returns:**
- a Future representing pending completion of the task

**Throws:**
- RejectedExecutionException

- if the task cannot be
scheduled for execution
- NullPointerException

- if the task is null

---

#### public
Future
<
V
> submit​(
Runnable
task,

V
result)

Description copied from interface:

CompletionService

**Specified by:**
- submit

in interface

CompletionService

<

V

>

**Parameters:**
- task

- the task to submit
- result

- the result to return upon successful completion

**Returns:**
- a Future representing pending completion of the task,
and whose

get()

method will return the given
result value upon completion

**Throws:**
- RejectedExecutionException

- if the task cannot be
scheduled for execution
- NullPointerException

- if the task is null

---

### Additional Sections

#### Class ExecutorCompletionService<V>

java.lang.Object

- java.util.concurrent.ExecutorCompletionService<V>

java.util.concurrent.ExecutorCompletionService<V>

**All Implemented Interfaces:** CompletionService

<V>

```java
public class
ExecutorCompletionService<V>

extends
Object

implements
CompletionService
<V>
```

A

CompletionService

that uses a supplied

Executor

to execute tasks. This class arranges that submitted tasks are,
upon completion, placed on a queue accessible using

take

.
The class is lightweight enough to be suitable for transient use
when processing groups of tasks.

Usage Examples.

Suppose you have a set of solvers for a certain problem, each
returning a value of some type

Result

, and would like to
run them concurrently, processing the results of each of them that
return a non-null value, in some method

use(Result r)

. You
could write this as:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException, ExecutionException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
solvers.forEach(cs::submit);
for (int i = solvers.size(); i > 0; i--) {
Result r = cs.take().get();
if (r != null)
use(r);
}
}
```

Suppose instead that you would like to use the first non-null result
of the set of tasks, ignoring any that encounter exceptions,
and cancelling all other tasks when the first one is ready:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
int n = solvers.size();
List<Future<Result>> futures = new ArrayList<>(n);
Result result = null;
try {
solvers.forEach(solver -> futures.add(cs.submit(solver)));
for (int i = n; i > 0; i--) {
try {
Result r = cs.take().get();
if (r != null) {
result = r;
break;
}
} catch (ExecutionException ignore) {}
}
} finally {
futures.forEach(future -> future.cancel(true));
}

if (result != null)
use(result);
}
```

**Since:** 1.5

public class

ExecutorCompletionService<V>

extends

Object

implements

CompletionService

<V>

A

CompletionService

that uses a supplied

Executor

to execute tasks. This class arranges that submitted tasks are,
upon completion, placed on a queue accessible using

take

.
The class is lightweight enough to be suitable for transient use
when processing groups of tasks.

Usage Examples.

Suppose you have a set of solvers for a certain problem, each
returning a value of some type

Result

, and would like to
run them concurrently, processing the results of each of them that
return a non-null value, in some method

use(Result r)

. You
could write this as:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException, ExecutionException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
solvers.forEach(cs::submit);
for (int i = solvers.size(); i > 0; i--) {
Result r = cs.take().get();
if (r != null)
use(r);
}
}
```

Suppose instead that you would like to use the first non-null result
of the set of tasks, ignoring any that encounter exceptions,
and cancelling all other tasks when the first one is ready:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
int n = solvers.size();
List<Future<Result>> futures = new ArrayList<>(n);
Result result = null;
try {
solvers.forEach(solver -> futures.add(cs.submit(solver)));
for (int i = n; i > 0; i--) {
try {
Result r = cs.take().get();
if (r != null) {
result = r;
break;
}
} catch (ExecutionException ignore) {}
}
} finally {
futures.forEach(future -> future.cancel(true));
}

if (result != null)
use(result);
}
```

Usage Examples.

Suppose you have a set of solvers for a certain problem, each
returning a value of some type

Result

, and would like to
run them concurrently, processing the results of each of them that
return a non-null value, in some method

use(Result r)

. You
could write this as:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException, ExecutionException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
solvers.forEach(cs::submit);
for (int i = solvers.size(); i > 0; i--) {
Result r = cs.take().get();
if (r != null)
use(r);
}
}
```

Suppose instead that you would like to use the first non-null result
of the set of tasks, ignoring any that encounter exceptions,
and cancelling all other tasks when the first one is ready:

```java
void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
int n = solvers.size();
List<Future<Result>> futures = new ArrayList<>(n);
Result result = null;
try {
solvers.forEach(solver -> futures.add(cs.submit(solver)));
for (int i = n; i > 0; i--) {
try {
Result r = cs.take().get();
if (r != null) {
result = r;
break;
}
} catch (ExecutionException ignore) {}
}
} finally {
futures.forEach(future -> future.cancel(true));
}

if (result != null)
use(result);
}
```

void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException, ExecutionException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
solvers.forEach(cs::submit);
for (int i = solvers.size(); i > 0; i--) {
Result r = cs.take().get();
if (r != null)
use(r);
}
}

void solve(Executor e,
Collection<Callable<Result>> solvers)
throws InterruptedException {
CompletionService<Result> cs
= new ExecutorCompletionService<>(e);
int n = solvers.size();
List<Future<Result>> futures = new ArrayList<>(n);
Result result = null;
try {
solvers.forEach(solver -> futures.add(cs.submit(solver)));
for (int i = n; i > 0; i--) {
try {
Result r = cs.take().get();
if (r != null) {
result = r;
break;
}
} catch (ExecutionException ignore) {}
}
} finally {
futures.forEach(future -> future.cancel(true));
}

if (result != null)
use(result);
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ExecutorCompletionService

​(

Executor

executor)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

ExecutorCompletionService

​(

Executor

executor,

BlockingQueue

<

Future

<

V

>> completionQueue)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Future

<

V

>

submit

​(

Runnable

task,

V

result)

Submits a Runnable task for execution and returns a Future
representing that task.

Future

<

V

>

submit

​(

Callable

<

V

> task)

Submits a value-returning task for execution and returns a Future
representing the pending results of the task.

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

- Methods declared in interface java.util.concurrent.

CompletionService

poll

,

poll

,

take

Constructor Summary

Constructors

Constructor

Description

ExecutorCompletionService

​(

Executor

executor)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

ExecutorCompletionService

​(

Executor

executor,

BlockingQueue

<

Future

<

V

>> completionQueue)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

---

#### Constructor Summary

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Future

<

V

>

submit

​(

Runnable

task,

V

result)

Submits a Runnable task for execution and returns a Future
representing that task.

Future

<

V

>

submit

​(

Callable

<

V

> task)

Submits a value-returning task for execution and returns a Future
representing the pending results of the task.

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

- Methods declared in interface java.util.concurrent.

CompletionService

poll

,

poll

,

take

---

#### Method Summary

Submits a Runnable task for execution and returns a Future
representing that task.

Submits a value-returning task for execution and returns a Future
representing the pending results of the task.

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

Methods declared in interface java.util.concurrent.

CompletionService

poll

,

poll

,

take

---

#### Methods declared in interface java.util.concurrent. CompletionService

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ExecutorCompletionService

```java
public ExecutorCompletionService​(
Executor
executor)
```

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

**Parameters:** executor

- the executor to use
**Throws:** NullPointerException

- if executor is

null

- ExecutorCompletionService

```java
public ExecutorCompletionService​(
Executor
executor,

BlockingQueue
<
Future
<
V
>> completionQueue)
```

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

**Parameters:** executor

- the executor to use
**Parameters:** completionQueue

- the queue to use as the completion queue
normally one dedicated for use by this service. This
queue is treated as unbounded -- failed attempted

Queue.add

operations for completed tasks cause
them not to be retrievable.
**Throws:** NullPointerException

- if executor or completionQueue are

null

============ METHOD DETAIL ==========

- Method Detail

- submit

```java
public
Future
<
V
> submit​(
Callable
<
V
> task)
```

Description copied from interface:

CompletionService

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

**Specified by:** submit

in interface

CompletionService

<

V

>
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

- submit

```java
public
Future
<
V
> submit​(
Runnable
task,

V
result)
```

Description copied from interface:

CompletionService

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

**Specified by:** submit

in interface

CompletionService

<

V

>
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return upon successful completion
**Returns:** a Future representing pending completion of the task,
and whose

get()

method will return the given
result value upon completion
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

Constructor Detail

- ExecutorCompletionService

```java
public ExecutorCompletionService​(
Executor
executor)
```

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

**Parameters:** executor

- the executor to use
**Throws:** NullPointerException

- if executor is

null

- ExecutorCompletionService

```java
public ExecutorCompletionService​(
Executor
executor,

BlockingQueue
<
Future
<
V
>> completionQueue)
```

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

**Parameters:** executor

- the executor to use
**Parameters:** completionQueue

- the queue to use as the completion queue
normally one dedicated for use by this service. This
queue is treated as unbounded -- failed attempted

Queue.add

operations for completed tasks cause
them not to be retrievable.
**Throws:** NullPointerException

- if executor or completionQueue are

null

---

#### Constructor Detail

ExecutorCompletionService

```java
public ExecutorCompletionService​(
Executor
executor)
```

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

**Parameters:** executor

- the executor to use
**Throws:** NullPointerException

- if executor is

null

---

#### ExecutorCompletionService

public ExecutorCompletionService​(

Executor

executor)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and a

LinkedBlockingQueue

as a completion queue.

ExecutorCompletionService

```java
public ExecutorCompletionService​(
Executor
executor,

BlockingQueue
<
Future
<
V
>> completionQueue)
```

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

**Parameters:** executor

- the executor to use
**Parameters:** completionQueue

- the queue to use as the completion queue
normally one dedicated for use by this service. This
queue is treated as unbounded -- failed attempted

Queue.add

operations for completed tasks cause
them not to be retrievable.
**Throws:** NullPointerException

- if executor or completionQueue are

null

---

#### ExecutorCompletionService

public ExecutorCompletionService​(

Executor

executor,

BlockingQueue

<

Future

<

V

>> completionQueue)

Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

Method Detail

- submit

```java
public
Future
<
V
> submit​(
Callable
<
V
> task)
```

Description copied from interface:

CompletionService

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

**Specified by:** submit

in interface

CompletionService

<

V

>
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

- submit

```java
public
Future
<
V
> submit​(
Runnable
task,

V
result)
```

Description copied from interface:

CompletionService

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

**Specified by:** submit

in interface

CompletionService

<

V

>
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return upon successful completion
**Returns:** a Future representing pending completion of the task,
and whose

get()

method will return the given
result value upon completion
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

---

#### Method Detail

submit

```java
public
Future
<
V
> submit​(
Callable
<
V
> task)
```

Description copied from interface:

CompletionService

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

**Specified by:** submit

in interface

CompletionService

<

V

>
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

---

#### submit

public

Future

<

V

> submit​(

Callable

<

V

> task)

Description copied from interface:

CompletionService

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

submit

```java
public
Future
<
V
> submit​(
Runnable
task,

V
result)
```

Description copied from interface:

CompletionService

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

**Specified by:** submit

in interface

CompletionService

<

V

>
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return upon successful completion
**Returns:** a Future representing pending completion of the task,
and whose

get()

method will return the given
result value upon completion
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

---

#### submit

public

Future

<

V

> submit​(

Runnable

task,

V

result)

Description copied from interface:

CompletionService

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

---

