# Class ThreadPoolExecutor.CallerRunsPolicy

**Source:** `java.base\java\util\concurrent\ThreadPoolExecutor.CallerRunsPolicy.html`

### Class Description

```java
public static class
ThreadPoolExecutor.CallerRunsPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that runs the rejected task
directly in the calling thread of the

execute

method,
unless the executor has been shut down, in which case the task
is discarded.

**All Implemented Interfaces:** RejectedExecutionHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public CallerRunsPolicy()

Creates a

CallerRunsPolicy

.

---

### Method Details

#### public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

**Specified by:**
- rejectedExecution

in interface

RejectedExecutionHandler

**Parameters:**
- r

- the runnable task requested to be executed
- e

- the executor attempting to execute this task

---

### Additional Sections

#### Class ThreadPoolExecutor.CallerRunsPolicy

java.lang.Object

- java.util.concurrent.ThreadPoolExecutor.CallerRunsPolicy

java.util.concurrent.ThreadPoolExecutor.CallerRunsPolicy

**All Implemented Interfaces:** RejectedExecutionHandler

**Enclosing class:** ThreadPoolExecutor

```java
public static class
ThreadPoolExecutor.CallerRunsPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that runs the rejected task
directly in the calling thread of the

execute

method,
unless the executor has been shut down, in which case the task
is discarded.

public static class

ThreadPoolExecutor.CallerRunsPolicy

extends

Object

implements

RejectedExecutionHandler

A handler for rejected tasks that runs the rejected task
directly in the calling thread of the

execute

method,
unless the executor has been shut down, in which case the task
is discarded.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CallerRunsPolicy

()

Creates a

CallerRunsPolicy

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

rejectedExecution

​(

Runnable

r,

ThreadPoolExecutor

e)

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

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

Constructor Summary

Constructors

Constructor

Description

CallerRunsPolicy

()

Creates a

CallerRunsPolicy

.

---

#### Constructor Summary

Creates a

CallerRunsPolicy

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

rejectedExecution

​(

Runnable

r,

ThreadPoolExecutor

e)

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

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

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CallerRunsPolicy

```java
public CallerRunsPolicy()
```

Creates a

CallerRunsPolicy

.

============ METHOD DETAIL ==========

- Method Detail

- rejectedExecution

```java
public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)
```

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task

Constructor Detail

- CallerRunsPolicy

```java
public CallerRunsPolicy()
```

Creates a

CallerRunsPolicy

.

---

#### Constructor Detail

CallerRunsPolicy

```java
public CallerRunsPolicy()
```

Creates a

CallerRunsPolicy

.

---

#### CallerRunsPolicy

public CallerRunsPolicy()

Creates a

CallerRunsPolicy

.

Method Detail

- rejectedExecution

```java
public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)
```

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task

---

#### Method Detail

rejectedExecution

```java
public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)
```

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task

---

#### rejectedExecution

public void rejectedExecution​(

Runnable

r,

ThreadPoolExecutor

e)

Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.

---

