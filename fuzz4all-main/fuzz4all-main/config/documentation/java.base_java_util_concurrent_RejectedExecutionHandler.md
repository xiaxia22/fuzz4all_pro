# Interface RejectedExecutionHandler

**Source:** `java.base\java\util\concurrent\RejectedExecutionHandler.html`

### Class Description

```java
public interface
RejectedExecutionHandler
```

A handler for tasks that cannot be executed by a

ThreadPoolExecutor

.

**All Known Implementing Classes:** ThreadPoolExecutor.AbortPolicy

,

ThreadPoolExecutor.CallerRunsPolicy

,

ThreadPoolExecutor.DiscardOldestPolicy

,

ThreadPoolExecutor.DiscardPolicy

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
executor)

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task. This may occur when no more threads or queue slots are
available because their bounds would be exceeded, or upon
shutdown of the Executor.

In the absence of other alternatives, the method may throw
an unchecked

RejectedExecutionException

, which will be
propagated to the caller of

execute

.

**Parameters:**
- r

- the runnable task requested to be executed
- executor

- the executor attempting to execute this task

**Throws:**
- RejectedExecutionException

- if there is no remedy

---

### Additional Sections

#### Interface RejectedExecutionHandler

**All Known Implementing Classes:** ThreadPoolExecutor.AbortPolicy

,

ThreadPoolExecutor.CallerRunsPolicy

,

ThreadPoolExecutor.DiscardOldestPolicy

,

ThreadPoolExecutor.DiscardPolicy

```java
public interface
RejectedExecutionHandler
```

A handler for tasks that cannot be executed by a

ThreadPoolExecutor

.

**Since:** 1.5

public interface

RejectedExecutionHandler

A handler for tasks that cannot be executed by a

ThreadPoolExecutor

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

rejectedExecution

​(

Runnable

r,

ThreadPoolExecutor

executor)

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

rejectedExecution

​(

Runnable

r,

ThreadPoolExecutor

executor)

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task.

---

#### Method Summary

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task.

============ METHOD DETAIL ==========

- Method Detail

- rejectedExecution

```java
void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
executor)
```

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task. This may occur when no more threads or queue slots are
available because their bounds would be exceeded, or upon
shutdown of the Executor.

In the absence of other alternatives, the method may throw
an unchecked

RejectedExecutionException

, which will be
propagated to the caller of

execute

.

**Parameters:** r

- the runnable task requested to be executed
**Parameters:** executor

- the executor attempting to execute this task
**Throws:** RejectedExecutionException

- if there is no remedy

Method Detail

- rejectedExecution

```java
void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
executor)
```

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task. This may occur when no more threads or queue slots are
available because their bounds would be exceeded, or upon
shutdown of the Executor.

In the absence of other alternatives, the method may throw
an unchecked

RejectedExecutionException

, which will be
propagated to the caller of

execute

.

**Parameters:** r

- the runnable task requested to be executed
**Parameters:** executor

- the executor attempting to execute this task
**Throws:** RejectedExecutionException

- if there is no remedy

---

#### Method Detail

rejectedExecution

```java
void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
executor)
```

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task. This may occur when no more threads or queue slots are
available because their bounds would be exceeded, or upon
shutdown of the Executor.

In the absence of other alternatives, the method may throw
an unchecked

RejectedExecutionException

, which will be
propagated to the caller of

execute

.

**Parameters:** r

- the runnable task requested to be executed
**Parameters:** executor

- the executor attempting to execute this task
**Throws:** RejectedExecutionException

- if there is no remedy

---

#### rejectedExecution

void rejectedExecution​(

Runnable

r,

ThreadPoolExecutor

executor)

Method that may be invoked by a

ThreadPoolExecutor

when

execute

cannot accept a
task. This may occur when no more threads or queue slots are
available because their bounds would be exceeded, or upon
shutdown of the Executor.

In the absence of other alternatives, the method may throw
an unchecked

RejectedExecutionException

, which will be
propagated to the caller of

execute

.

In the absence of other alternatives, the method may throw
an unchecked

RejectedExecutionException

, which will be
propagated to the caller of

execute

.

---

