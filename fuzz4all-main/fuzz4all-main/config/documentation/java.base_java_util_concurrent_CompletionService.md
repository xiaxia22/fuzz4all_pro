# Interface CompletionService<V>

**Source:** `java.base\java\util\concurrent\CompletionService.html`

### Class Description

```java
public interface
CompletionService<V>
```

A service that decouples the production of new asynchronous tasks
from the consumption of the results of completed tasks. Producers

submit

tasks for execution. Consumers

take

completed tasks and process their results in the order they
complete. A

CompletionService

can for example be used to
manage asynchronous I/O, in which tasks that perform reads are
submitted in one part of a program or system, and then acted upon
in a different part of the program when the reads complete,
possibly in a different order than they were requested.

Typically, a

CompletionService

relies on a separate

Executor

to actually execute the tasks, in which case the

CompletionService

only manages an internal completion
queue. The

ExecutorCompletionService

class provides an
implementation of this approach.

Memory consistency effects: Actions in a thread prior to
submitting a task to a

CompletionService

happen-before

actions taken by that task, which in turn

happen-before

actions following a successful return from the corresponding

take()

.

**All Known Implementing Classes:** ExecutorCompletionService

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Future
<
V
> submit​(
Callable
<
V
> task)

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

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

#### Future
<
V
> submit​(
Runnable
task,

V
result)

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

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

#### Future
<
V
> take()
throws
InterruptedException

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

**Returns:**
- the Future representing the next completed task

**Throws:**
- InterruptedException

- if interrupted while waiting

---

#### Future
<
V
> poll()

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

**Returns:**
- the Future representing the next completed task, or

null

if none are present

---

#### Future
<
V
> poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

**Parameters:**
- timeout

- how long to wait before giving up, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

timeout

parameter

**Returns:**
- the Future representing the next completed task or

null

if the specified waiting time elapses
before one is present

**Throws:**
- InterruptedException

- if interrupted while waiting

---

### Additional Sections

#### Interface CompletionService<V>

**All Known Implementing Classes:** ExecutorCompletionService

```java
public interface
CompletionService<V>
```

A service that decouples the production of new asynchronous tasks
from the consumption of the results of completed tasks. Producers

submit

tasks for execution. Consumers

take

completed tasks and process their results in the order they
complete. A

CompletionService

can for example be used to
manage asynchronous I/O, in which tasks that perform reads are
submitted in one part of a program or system, and then acted upon
in a different part of the program when the reads complete,
possibly in a different order than they were requested.

Typically, a

CompletionService

relies on a separate

Executor

to actually execute the tasks, in which case the

CompletionService

only manages an internal completion
queue. The

ExecutorCompletionService

class provides an
implementation of this approach.

Memory consistency effects: Actions in a thread prior to
submitting a task to a

CompletionService

happen-before

actions taken by that task, which in turn

happen-before

actions following a successful return from the corresponding

take()

.

**Since:** 1.5

public interface

CompletionService<V>

A service that decouples the production of new asynchronous tasks
from the consumption of the results of completed tasks. Producers

submit

tasks for execution. Consumers

take

completed tasks and process their results in the order they
complete. A

CompletionService

can for example be used to
manage asynchronous I/O, in which tasks that perform reads are
submitted in one part of a program or system, and then acted upon
in a different part of the program when the reads complete,
possibly in a different order than they were requested.

Typically, a

CompletionService

relies on a separate

Executor

to actually execute the tasks, in which case the

CompletionService

only manages an internal completion
queue. The

ExecutorCompletionService

class provides an
implementation of this approach.

Memory consistency effects: Actions in a thread prior to
submitting a task to a

CompletionService

happen-before

actions taken by that task, which in turn

happen-before

actions following a successful return from the corresponding

take()

.

Typically, a

CompletionService

relies on a separate

Executor

to actually execute the tasks, in which case the

CompletionService

only manages an internal completion
queue. The

ExecutorCompletionService

class provides an
implementation of this approach.

Memory consistency effects: Actions in a thread prior to
submitting a task to a

CompletionService

happen-before

actions taken by that task, which in turn

happen-before

actions following a successful return from the corresponding

take()

.

Memory consistency effects: Actions in a thread prior to
submitting a task to a

CompletionService

happen-before

actions taken by that task, which in turn

happen-before

actions following a successful return from the corresponding

take()

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Future

<

V

>

poll

()

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

Future

<

V

>

poll

​(long timeout,

TimeUnit

unit)

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

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

Future

<

V

>

take

()

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Future

<

V

>

poll

()

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

Future

<

V

>

poll

​(long timeout,

TimeUnit

unit)

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

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

Future

<

V

>

take

()

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

---

#### Method Summary

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

Submits a Runnable task for execution and returns a Future
representing that task.

Submits a value-returning task for execution and returns a Future
representing the pending results of the task.

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

============ METHOD DETAIL ==========

- Method Detail

- submit

```java
Future
<
V
> submit​(
Callable
<
V
> task)
```

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

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
Future
<
V
> submit​(
Runnable
task,

V
result)
```

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

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

- take

```java
Future
<
V
> take()
throws
InterruptedException
```

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

**Returns:** the Future representing the next completed task
**Throws:** InterruptedException

- if interrupted while waiting

- poll

```java
Future
<
V
> poll()
```

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

**Returns:** the Future representing the next completed task, or

null

if none are present

- poll

```java
Future
<
V
> poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** the Future representing the next completed task or

null

if the specified waiting time elapses
before one is present
**Throws:** InterruptedException

- if interrupted while waiting

Method Detail

- submit

```java
Future
<
V
> submit​(
Callable
<
V
> task)
```

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

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
Future
<
V
> submit​(
Runnable
task,

V
result)
```

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

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

- take

```java
Future
<
V
> take()
throws
InterruptedException
```

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

**Returns:** the Future representing the next completed task
**Throws:** InterruptedException

- if interrupted while waiting

- poll

```java
Future
<
V
> poll()
```

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

**Returns:** the Future representing the next completed task, or

null

if none are present

- poll

```java
Future
<
V
> poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** the Future representing the next completed task or

null

if the specified waiting time elapses
before one is present
**Throws:** InterruptedException

- if interrupted while waiting

---

#### Method Detail

submit

```java
Future
<
V
> submit​(
Callable
<
V
> task)
```

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

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

Future

<

V

> submit​(

Callable

<

V

> task)

Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.

submit

```java
Future
<
V
> submit​(
Runnable
task,

V
result)
```

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

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

Future

<

V

> submit​(

Runnable

task,

V

result)

Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.

take

```java
Future
<
V
> take()
throws
InterruptedException
```

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

**Returns:** the Future representing the next completed task
**Throws:** InterruptedException

- if interrupted while waiting

---

#### take

Future

<

V

> take()
throws

InterruptedException

Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

poll

```java
Future
<
V
> poll()
```

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

**Returns:** the Future representing the next completed task, or

null

if none are present

---

#### poll

Future

<

V

> poll()

Retrieves and removes the Future representing the next
completed task, or

null

if none are present.

poll

```java
Future
<
V
> poll​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

**Parameters:** timeout

- how long to wait before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Returns:** the Future representing the next completed task or

null

if the specified waiting time elapses
before one is present
**Throws:** InterruptedException

- if interrupted while waiting

---

#### poll

Future

<

V

> poll​(long timeout,

TimeUnit

unit)
throws

InterruptedException

Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.

---

