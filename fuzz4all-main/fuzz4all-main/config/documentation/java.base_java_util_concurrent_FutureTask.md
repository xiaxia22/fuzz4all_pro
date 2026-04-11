# Class FutureTask<V>

**Source:** `java.base\java\util\concurrent\FutureTask.html`

### Class Description

```java
public class
FutureTask<V>

extends
Object

implements
RunnableFuture
<V>
```

A cancellable asynchronous computation. This class provides a base
implementation of

Future

, with methods to start and cancel
a computation, query to see if the computation is complete, and
retrieve the result of the computation. The result can only be
retrieved when the computation has completed; the

get

methods will block if the computation has not yet completed. Once
the computation has completed, the computation cannot be restarted
or cancelled (unless the computation is invoked using

runAndReset()

).

A

FutureTask

can be used to wrap a

Callable

or

Runnable

object. Because

FutureTask

implements

Runnable

, a

FutureTask

can be submitted to an

Executor

for execution.

In addition to serving as a standalone class, this class provides

protected

functionality that may be useful when creating
customized task classes.

**Type Parameters:** V

- The result type returned by this FutureTask's

get

methods

---

### Field Details

*No entries found.*

### Constructor Details

#### public FutureTask​(
Callable
<
V
> callable)

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

**Parameters:**
- callable

- the callable task

**Throws:**
- NullPointerException

- if the callable is null

---

#### public FutureTask​(
Runnable
runnable,

V
result)

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

**Parameters:**
- runnable

- the runnable task
- result

- the result to return on successful completion. If
you don't need a particular result, consider using
constructions of the form:

Future<?> f = new FutureTask<Void>(runnable, null)

**Throws:**
- NullPointerException

- if the runnable is null

---

### Method Details

#### public
V
get()
throws
InterruptedException
,

ExecutionException

Description copied from interface:

Future

**Specified by:**
- get

in interface

Future

<

V

>

**Returns:**
- the computed result

**Throws:**
- CancellationException

- if the computation was cancelled
- InterruptedException

- if the current thread was interrupted
while waiting
- ExecutionException

- if the computation threw an
exception

---

#### public
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

Description copied from interface:

Future

**Specified by:**
- get

in interface

Future

<

V

>

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
- InterruptedException

- if the current thread was interrupted
while waiting
- ExecutionException

- if the computation threw an
exception
- TimeoutException

- if the wait timed out

---

#### protected void done()

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation). The
default implementation does nothing. Subclasses may override
this method to invoke completion callbacks or perform
bookkeeping. Note that you can query status inside the
implementation of this method to determine whether this task
has been cancelled.

---

#### protected void set​(
V
v)

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon successful completion of the computation.

**Parameters:**
- v

- the value

---

#### protected void setException​(
Throwable
t)

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon failure of the computation.

**Parameters:**
- t

- the cause of failure

---

#### protected boolean runAndReset()

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled. This is
designed for use with tasks that intrinsically execute more
than once.

**Returns:**
- true

if successfully run and reset

---

#### public
String
toString()

Returns a string representation of this FutureTask.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this FutureTask

**Implementation Requirements:**
- The default implementation returns a string identifying this
FutureTask, as well as its completion state. The state, in
brackets, contains one of the strings

"Completed Normally"

,

"Completed Exceptionally"

,

"Cancelled"

, or

"Not completed"

.

---

### Additional Sections

#### Class FutureTask<V>

java.lang.Object

- java.util.concurrent.FutureTask<V>

java.util.concurrent.FutureTask<V>

**Type Parameters:** V

- The result type returned by this FutureTask's

get

methods

**All Implemented Interfaces:** Runnable

,

Future

<V>

,

RunnableFuture

<V>

```java
public class
FutureTask<V>

extends
Object

implements
RunnableFuture
<V>
```

A cancellable asynchronous computation. This class provides a base
implementation of

Future

, with methods to start and cancel
a computation, query to see if the computation is complete, and
retrieve the result of the computation. The result can only be
retrieved when the computation has completed; the

get

methods will block if the computation has not yet completed. Once
the computation has completed, the computation cannot be restarted
or cancelled (unless the computation is invoked using

runAndReset()

).

A

FutureTask

can be used to wrap a

Callable

or

Runnable

object. Because

FutureTask

implements

Runnable

, a

FutureTask

can be submitted to an

Executor

for execution.

In addition to serving as a standalone class, this class provides

protected

functionality that may be useful when creating
customized task classes.

**Since:** 1.5

public class

FutureTask<V>

extends

Object

implements

RunnableFuture

<V>

A cancellable asynchronous computation. This class provides a base
implementation of

Future

, with methods to start and cancel
a computation, query to see if the computation is complete, and
retrieve the result of the computation. The result can only be
retrieved when the computation has completed; the

get

methods will block if the computation has not yet completed. Once
the computation has completed, the computation cannot be restarted
or cancelled (unless the computation is invoked using

runAndReset()

).

A

FutureTask

can be used to wrap a

Callable

or

Runnable

object. Because

FutureTask

implements

Runnable

, a

FutureTask

can be submitted to an

Executor

for execution.

In addition to serving as a standalone class, this class provides

protected

functionality that may be useful when creating
customized task classes.

A

FutureTask

can be used to wrap a

Callable

or

Runnable

object. Because

FutureTask

implements

Runnable

, a

FutureTask

can be submitted to an

Executor

for execution.

In addition to serving as a standalone class, this class provides

protected

functionality that may be useful when creating
customized task classes.

In addition to serving as a standalone class, this class provides

protected

functionality that may be useful when creating
customized task classes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FutureTask

​(

Runnable

runnable,

V

result)

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

FutureTask

​(

Callable

<

V

> callable)

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

done

()

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation).

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

protected boolean

runAndReset

()

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled.

protected void

set

​(

V

v)

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

protected void

setException

​(

Throwable

t)

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

String

toString

()

Returns a string representation of this FutureTask.

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

Future

cancel

,

isCancelled

,

isDone

- Methods declared in interface java.util.concurrent.

RunnableFuture

run

Constructor Summary

Constructors

Constructor

Description

FutureTask

​(

Runnable

runnable,

V

result)

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

FutureTask

​(

Callable

<

V

> callable)

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

---

#### Constructor Summary

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

done

()

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation).

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

protected boolean

runAndReset

()

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled.

protected void

set

​(

V

v)

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

protected void

setException

​(

Throwable

t)

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

String

toString

()

Returns a string representation of this FutureTask.

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

Future

cancel

,

isCancelled

,

isDone

- Methods declared in interface java.util.concurrent.

RunnableFuture

run

---

#### Method Summary

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation).

Waits if necessary for the computation to complete, and then
retrieves its result.

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled.

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

Returns a string representation of this FutureTask.

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

Future

cancel

,

isCancelled

,

isDone

---

#### Methods declared in interface java.util.concurrent. Future

Methods declared in interface java.util.concurrent.

RunnableFuture

run

---

#### Methods declared in interface java.util.concurrent. RunnableFuture

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FutureTask

```java
public FutureTask​(
Callable
<
V
> callable)
```

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

**Parameters:** callable

- the callable task
**Throws:** NullPointerException

- if the callable is null

- FutureTask

```java
public FutureTask​(
Runnable
runnable,

V
result)
```

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

**Parameters:** runnable

- the runnable task
**Parameters:** result

- the result to return on successful completion. If
you don't need a particular result, consider using
constructions of the form:

Future<?> f = new FutureTask<Void>(runnable, null)
**Throws:** NullPointerException

- if the runnable is null

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public
V
get()
throws
InterruptedException
,

ExecutionException
```

Description copied from interface:

Future

Waits if necessary for the computation to complete, and then
retrieves its result.

**Specified by:** get

in interface

Future

<

V

>
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception

- get

```java
public
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

Description copied from interface:

Future

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

**Specified by:** get

in interface

Future

<

V

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** TimeoutException

- if the wait timed out

- done

```java
protected void done()
```

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation). The
default implementation does nothing. Subclasses may override
this method to invoke completion callbacks or perform
bookkeeping. Note that you can query status inside the
implementation of this method to determine whether this task
has been cancelled.

- set

```java
protected void set​(
V
v)
```

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon successful completion of the computation.

**Parameters:** v

- the value

- setException

```java
protected void setException​(
Throwable
t)
```

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon failure of the computation.

**Parameters:** t

- the cause of failure

- runAndReset

```java
protected boolean runAndReset()
```

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled. This is
designed for use with tasks that intrinsically execute more
than once.

**Returns:** true

if successfully run and reset

- toString

```java
public
String
toString()
```

Returns a string representation of this FutureTask.

**Overrides:** toString

in class

Object
**Implementation Requirements:** The default implementation returns a string identifying this
FutureTask, as well as its completion state. The state, in
brackets, contains one of the strings

"Completed Normally"

,

"Completed Exceptionally"

,

"Cancelled"

, or

"Not completed"

.
**Returns:** a string representation of this FutureTask

Constructor Detail

- FutureTask

```java
public FutureTask​(
Callable
<
V
> callable)
```

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

**Parameters:** callable

- the callable task
**Throws:** NullPointerException

- if the callable is null

- FutureTask

```java
public FutureTask​(
Runnable
runnable,

V
result)
```

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

**Parameters:** runnable

- the runnable task
**Parameters:** result

- the result to return on successful completion. If
you don't need a particular result, consider using
constructions of the form:

Future<?> f = new FutureTask<Void>(runnable, null)
**Throws:** NullPointerException

- if the runnable is null

---

#### Constructor Detail

FutureTask

```java
public FutureTask​(
Callable
<
V
> callable)
```

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

**Parameters:** callable

- the callable task
**Throws:** NullPointerException

- if the callable is null

---

#### FutureTask

public FutureTask​(

Callable

<

V

> callable)

Creates a

FutureTask

that will, upon running, execute the
given

Callable

.

FutureTask

```java
public FutureTask​(
Runnable
runnable,

V
result)
```

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

**Parameters:** runnable

- the runnable task
**Parameters:** result

- the result to return on successful completion. If
you don't need a particular result, consider using
constructions of the form:

Future<?> f = new FutureTask<Void>(runnable, null)
**Throws:** NullPointerException

- if the runnable is null

---

#### FutureTask

public FutureTask​(

Runnable

runnable,

V

result)

Creates a

FutureTask

that will, upon running, execute the
given

Runnable

, and arrange that

get

will return the
given result on successful completion.

Method Detail

- get

```java
public
V
get()
throws
InterruptedException
,

ExecutionException
```

Description copied from interface:

Future

Waits if necessary for the computation to complete, and then
retrieves its result.

**Specified by:** get

in interface

Future

<

V

>
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception

- get

```java
public
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

Description copied from interface:

Future

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

**Specified by:** get

in interface

Future

<

V

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** TimeoutException

- if the wait timed out

- done

```java
protected void done()
```

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation). The
default implementation does nothing. Subclasses may override
this method to invoke completion callbacks or perform
bookkeeping. Note that you can query status inside the
implementation of this method to determine whether this task
has been cancelled.

- set

```java
protected void set​(
V
v)
```

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon successful completion of the computation.

**Parameters:** v

- the value

- setException

```java
protected void setException​(
Throwable
t)
```

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon failure of the computation.

**Parameters:** t

- the cause of failure

- runAndReset

```java
protected boolean runAndReset()
```

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled. This is
designed for use with tasks that intrinsically execute more
than once.

**Returns:** true

if successfully run and reset

- toString

```java
public
String
toString()
```

Returns a string representation of this FutureTask.

**Overrides:** toString

in class

Object
**Implementation Requirements:** The default implementation returns a string identifying this
FutureTask, as well as its completion state. The state, in
brackets, contains one of the strings

"Completed Normally"

,

"Completed Exceptionally"

,

"Cancelled"

, or

"Not completed"

.
**Returns:** a string representation of this FutureTask

---

#### Method Detail

get

```java
public
V
get()
throws
InterruptedException
,

ExecutionException
```

Description copied from interface:

Future

Waits if necessary for the computation to complete, and then
retrieves its result.

**Specified by:** get

in interface

Future

<

V

>
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception

---

#### get

public

V

get()
throws

InterruptedException

,

ExecutionException

Description copied from interface:

Future

Waits if necessary for the computation to complete, and then
retrieves its result.

get

```java
public
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

Description copied from interface:

Future

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

**Specified by:** get

in interface

Future

<

V

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** TimeoutException

- if the wait timed out

---

#### get

public

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

Description copied from interface:

Future

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

done

```java
protected void done()
```

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation). The
default implementation does nothing. Subclasses may override
this method to invoke completion callbacks or perform
bookkeeping. Note that you can query status inside the
implementation of this method to determine whether this task
has been cancelled.

---

#### done

protected void done()

Protected method invoked when this task transitions to state

isDone

(whether normally or via cancellation). The
default implementation does nothing. Subclasses may override
this method to invoke completion callbacks or perform
bookkeeping. Note that you can query status inside the
implementation of this method to determine whether this task
has been cancelled.

set

```java
protected void set​(
V
v)
```

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon successful completion of the computation.

**Parameters:** v

- the value

---

#### set

protected void set​(

V

v)

Sets the result of this future to the given value unless
this future has already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon successful completion of the computation.

This method is invoked internally by the

RunnableFuture.run()

method
upon successful completion of the computation.

setException

```java
protected void setException​(
Throwable
t)
```

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon failure of the computation.

**Parameters:** t

- the cause of failure

---

#### setException

protected void setException​(

Throwable

t)

Causes this future to report an

ExecutionException

with the given throwable as its cause, unless this future has
already been set or has been cancelled.

This method is invoked internally by the

RunnableFuture.run()

method
upon failure of the computation.

This method is invoked internally by the

RunnableFuture.run()

method
upon failure of the computation.

runAndReset

```java
protected boolean runAndReset()
```

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled. This is
designed for use with tasks that intrinsically execute more
than once.

**Returns:** true

if successfully run and reset

---

#### runAndReset

protected boolean runAndReset()

Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled. This is
designed for use with tasks that intrinsically execute more
than once.

toString

```java
public
String
toString()
```

Returns a string representation of this FutureTask.

**Overrides:** toString

in class

Object
**Implementation Requirements:** The default implementation returns a string identifying this
FutureTask, as well as its completion state. The state, in
brackets, contains one of the strings

"Completed Normally"

,

"Completed Exceptionally"

,

"Cancelled"

, or

"Not completed"

.
**Returns:** a string representation of this FutureTask

---

#### toString

public

String

toString()

Returns a string representation of this FutureTask.

---

