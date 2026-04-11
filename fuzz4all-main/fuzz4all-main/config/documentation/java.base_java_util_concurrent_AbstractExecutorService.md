# Class AbstractExecutorService

**Source:** `java.base\java\util\concurrent\AbstractExecutorService.html`

### Class Description

```java
public abstract class
AbstractExecutorService

extends
Object

implements
ExecutorService
```

Provides default implementations of

ExecutorService

execution methods. This class implements the

submit

,

invokeAny

and

invokeAll

methods using a

RunnableFuture

returned by

newTaskFor

, which defaults
to the

FutureTask

class provided in this package. For example,
the implementation of

submit(Runnable)

creates an
associated

RunnableFuture

that is executed and
returned. Subclasses may override the

newTaskFor

methods
to return

RunnableFuture

implementations other than

FutureTask

.

Extension example

. Here is a sketch of a class
that customizes

ThreadPoolExecutor

to use
a

CustomTask

class instead of the default

FutureTask

:

```java
public class CustomThreadPoolExecutor extends ThreadPoolExecutor {

static class CustomTask<V> implements RunnableFuture<V> {...}

protected <V> RunnableFuture<V> newTaskFor(Callable<V> c) {
return new CustomTask<V>(c);
}
protected <V> RunnableFuture<V> newTaskFor(Runnable r, V v) {
return new CustomTask<V>(r, v);
}
// ... add constructors, etc.
}
```

**All Implemented Interfaces:** Executor

,

ExecutorService

---

### Field Details

*No entries found.*

### Constructor Details

#### public AbstractExecutorService()

*No description found.*

---

### Method Details

#### protected <T>
RunnableFuture
<T> newTaskFor​(
Runnable
runnable,
T value)

Returns a

RunnableFuture

for the given runnable and default
value.

**Parameters:**
- runnable

- the runnable task being wrapped
- value

- the default value for the returned future

**Returns:**
- a

RunnableFuture

which, when run, will run the
underlying runnable and which, as a

Future

, will yield
the given value as its result and provide for cancellation of
the underlying task

**Since:**
- 1.6

**Type Parameters:**
- T

- the type of the given value

---

#### protected <T>
RunnableFuture
<T> newTaskFor​(
Callable
<T> callable)

Returns a

RunnableFuture

for the given callable task.

**Parameters:**
- callable

- the callable task being wrapped

**Returns:**
- a

RunnableFuture

which, when run, will call the
underlying callable and which, as a

Future

, will yield
the callable's result as its result and provide for
cancellation of the underlying task

**Since:**
- 1.6

**Type Parameters:**
- T

- the type of the callable's result

---

#### public
Future
<?> submit​(
Runnable
task)

Description copied from interface:

ExecutorService

**Specified by:**
- submit

in interface

ExecutorService

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

#### public <T>
Future
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

**Parameters:**
- task

- the task to submit
- result

- the result to return

**Returns:**
- a Future representing pending completion of the task

**Throws:**
- RejectedExecutionException

- if the task cannot be
scheduled for execution
- NullPointerException

- if the task is null

**Type Parameters:**
- T

- the type of the result

---

#### public <T>
Future
<T> submit​(
Callable
<T> task)

Description copied from interface:

ExecutorService

**Specified by:**
- submit

in interface

ExecutorService

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

**Type Parameters:**
- T

- the type of the task's result

---

### Additional Sections

#### Class AbstractExecutorService

java.lang.Object

- java.util.concurrent.AbstractExecutorService

java.util.concurrent.AbstractExecutorService

**All Implemented Interfaces:** Executor

,

ExecutorService

**Direct Known Subclasses:** ForkJoinPool

,

ThreadPoolExecutor

```java
public abstract class
AbstractExecutorService

extends
Object

implements
ExecutorService
```

Provides default implementations of

ExecutorService

execution methods. This class implements the

submit

,

invokeAny

and

invokeAll

methods using a

RunnableFuture

returned by

newTaskFor

, which defaults
to the

FutureTask

class provided in this package. For example,
the implementation of

submit(Runnable)

creates an
associated

RunnableFuture

that is executed and
returned. Subclasses may override the

newTaskFor

methods
to return

RunnableFuture

implementations other than

FutureTask

.

Extension example

. Here is a sketch of a class
that customizes

ThreadPoolExecutor

to use
a

CustomTask

class instead of the default

FutureTask

:

```java
public class CustomThreadPoolExecutor extends ThreadPoolExecutor {

static class CustomTask<V> implements RunnableFuture<V> {...}

protected <V> RunnableFuture<V> newTaskFor(Callable<V> c) {
return new CustomTask<V>(c);
}
protected <V> RunnableFuture<V> newTaskFor(Runnable r, V v) {
return new CustomTask<V>(r, v);
}
// ... add constructors, etc.
}
```

**Since:** 1.5

public abstract class

AbstractExecutorService

extends

Object

implements

ExecutorService

Provides default implementations of

ExecutorService

execution methods. This class implements the

submit

,

invokeAny

and

invokeAll

methods using a

RunnableFuture

returned by

newTaskFor

, which defaults
to the

FutureTask

class provided in this package. For example,
the implementation of

submit(Runnable)

creates an
associated

RunnableFuture

that is executed and
returned. Subclasses may override the

newTaskFor

methods
to return

RunnableFuture

implementations other than

FutureTask

.

Extension example

. Here is a sketch of a class
that customizes

ThreadPoolExecutor

to use
a

CustomTask

class instead of the default

FutureTask

:

```java
public class CustomThreadPoolExecutor extends ThreadPoolExecutor {

static class CustomTask<V> implements RunnableFuture<V> {...}

protected <V> RunnableFuture<V> newTaskFor(Callable<V> c) {
return new CustomTask<V>(c);
}
protected <V> RunnableFuture<V> newTaskFor(Runnable r, V v) {
return new CustomTask<V>(r, v);
}
// ... add constructors, etc.
}
```

Extension example

. Here is a sketch of a class
that customizes

ThreadPoolExecutor

to use
a

CustomTask

class instead of the default

FutureTask

:

```java
public class CustomThreadPoolExecutor extends ThreadPoolExecutor {

static class CustomTask<V> implements RunnableFuture<V> {...}

protected <V> RunnableFuture<V> newTaskFor(Callable<V> c) {
return new CustomTask<V>(c);
}
protected <V> RunnableFuture<V> newTaskFor(Runnable r, V v) {
return new CustomTask<V>(r, v);
}
// ... add constructors, etc.
}
```

public class CustomThreadPoolExecutor extends ThreadPoolExecutor {

static class CustomTask<V> implements RunnableFuture<V> {...}

protected <V> RunnableFuture<V> newTaskFor(Callable<V> c) {
return new CustomTask<V>(c);
}
protected <V> RunnableFuture<V> newTaskFor(Runnable r, V v) {
return new CustomTask<V>(r, v);
}
// ... add constructors, etc.
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractExecutorService

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected <T>

RunnableFuture

<T>

newTaskFor

​(

Runnable

runnable,
T value)

Returns a

RunnableFuture

for the given runnable and default
value.

protected <T>

RunnableFuture

<T>

newTaskFor

​(

Callable

<T> callable)

Returns a

RunnableFuture

for the given callable task.

Future

<?>

submit

​(

Runnable

task)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

Future

<T>

submit

​(

Runnable

task,
T result)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

Future

<T>

submit

​(

Callable

<T> task)

Submits a value-returning task for execution and returns a
Future representing the pending results of the task.

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

Executor

execute

- Methods declared in interface java.util.concurrent.

ExecutorService

awaitTermination

,

invokeAll

,

invokeAll

,

invokeAny

,

invokeAny

,

isShutdown

,

isTerminated

,

shutdown

,

shutdownNow

Constructor Summary

Constructors

Constructor

Description

AbstractExecutorService

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected <T>

RunnableFuture

<T>

newTaskFor

​(

Runnable

runnable,
T value)

Returns a

RunnableFuture

for the given runnable and default
value.

protected <T>

RunnableFuture

<T>

newTaskFor

​(

Callable

<T> callable)

Returns a

RunnableFuture

for the given callable task.

Future

<?>

submit

​(

Runnable

task)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

Future

<T>

submit

​(

Runnable

task,
T result)

Submits a Runnable task for execution and returns a Future
representing that task.

<T>

Future

<T>

submit

​(

Callable

<T> task)

Submits a value-returning task for execution and returns a
Future representing the pending results of the task.

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

Executor

execute

- Methods declared in interface java.util.concurrent.

ExecutorService

awaitTermination

,

invokeAll

,

invokeAll

,

invokeAny

,

invokeAny

,

isShutdown

,

isTerminated

,

shutdown

,

shutdownNow

---

#### Method Summary

Returns a

RunnableFuture

for the given runnable and default
value.

Returns a

RunnableFuture

for the given callable task.

Submits a Runnable task for execution and returns a Future
representing that task.

Submits a value-returning task for execution and returns a
Future representing the pending results of the task.

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

Executor

execute

---

#### Methods declared in interface java.util.concurrent. Executor

Methods declared in interface java.util.concurrent.

ExecutorService

awaitTermination

,

invokeAll

,

invokeAll

,

invokeAny

,

invokeAny

,

isShutdown

,

isTerminated

,

shutdown

,

shutdownNow

---

#### Methods declared in interface java.util.concurrent. ExecutorService

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractExecutorService

```java
public AbstractExecutorService()
```

============ METHOD DETAIL ==========

- Method Detail

- newTaskFor

```java
protected <T>
RunnableFuture
<T> newTaskFor​(
Runnable
runnable,
T value)
```

Returns a

RunnableFuture

for the given runnable and default
value.

**Type Parameters:** T

- the type of the given value
**Parameters:** runnable

- the runnable task being wrapped
**Parameters:** value

- the default value for the returned future
**Returns:** a

RunnableFuture

which, when run, will run the
underlying runnable and which, as a

Future

, will yield
the given value as its result and provide for cancellation of
the underlying task
**Since:** 1.6

- newTaskFor

```java
protected <T>
RunnableFuture
<T> newTaskFor​(
Callable
<T> callable)
```

Returns a

RunnableFuture

for the given callable task.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the callable task being wrapped
**Returns:** a

RunnableFuture

which, when run, will call the
underlying callable and which, as a

Future

, will yield
the callable's result as its result and provide for
cancellation of the underlying task
**Since:** 1.6

- submit

```java
public
Future
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
public <T>
Future
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
**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

- submit

```java
public <T>
Future
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
**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

Constructor Detail

- AbstractExecutorService

```java
public AbstractExecutorService()
```

---

#### Constructor Detail

AbstractExecutorService

```java
public AbstractExecutorService()
```

---

#### AbstractExecutorService

public AbstractExecutorService()

Method Detail

- newTaskFor

```java
protected <T>
RunnableFuture
<T> newTaskFor​(
Runnable
runnable,
T value)
```

Returns a

RunnableFuture

for the given runnable and default
value.

**Type Parameters:** T

- the type of the given value
**Parameters:** runnable

- the runnable task being wrapped
**Parameters:** value

- the default value for the returned future
**Returns:** a

RunnableFuture

which, when run, will run the
underlying runnable and which, as a

Future

, will yield
the given value as its result and provide for cancellation of
the underlying task
**Since:** 1.6

- newTaskFor

```java
protected <T>
RunnableFuture
<T> newTaskFor​(
Callable
<T> callable)
```

Returns a

RunnableFuture

for the given callable task.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the callable task being wrapped
**Returns:** a

RunnableFuture

which, when run, will call the
underlying callable and which, as a

Future

, will yield
the callable's result as its result and provide for
cancellation of the underlying task
**Since:** 1.6

- submit

```java
public
Future
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
public <T>
Future
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
**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

- submit

```java
public <T>
Future
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
**Type Parameters:** T

- the type of the task's result
**Parameters:** task

- the task to submit
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

---

#### Method Detail

newTaskFor

```java
protected <T>
RunnableFuture
<T> newTaskFor​(
Runnable
runnable,
T value)
```

Returns a

RunnableFuture

for the given runnable and default
value.

**Type Parameters:** T

- the type of the given value
**Parameters:** runnable

- the runnable task being wrapped
**Parameters:** value

- the default value for the returned future
**Returns:** a

RunnableFuture

which, when run, will run the
underlying runnable and which, as a

Future

, will yield
the given value as its result and provide for cancellation of
the underlying task
**Since:** 1.6

---

#### newTaskFor

protected <T>

RunnableFuture

<T> newTaskFor​(

Runnable

runnable,
T value)

Returns a

RunnableFuture

for the given runnable and default
value.

newTaskFor

```java
protected <T>
RunnableFuture
<T> newTaskFor​(
Callable
<T> callable)
```

Returns a

RunnableFuture

for the given callable task.

**Type Parameters:** T

- the type of the callable's result
**Parameters:** callable

- the callable task being wrapped
**Returns:** a

RunnableFuture

which, when run, will call the
underlying callable and which, as a

Future

, will yield
the callable's result as its result and provide for
cancellation of the underlying task
**Since:** 1.6

---

#### newTaskFor

protected <T>

RunnableFuture

<T> newTaskFor​(

Callable

<T> callable)

Returns a

RunnableFuture

for the given callable task.

submit

```java
public
Future
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

submit

```java
public <T>
Future
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
**Type Parameters:** T

- the type of the result
**Parameters:** task

- the task to submit
**Parameters:** result

- the result to return
**Returns:** a Future representing pending completion of the task
**Throws:** RejectedExecutionException

- if the task cannot be
scheduled for execution
**Throws:** NullPointerException

- if the task is null

---

#### submit

public <T>

Future

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
public <T>
Future
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
**Type Parameters:** T

- the type of the task's result
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

public <T>

Future

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

---

