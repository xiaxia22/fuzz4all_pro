# Class ThreadPoolExecutor.DiscardOldestPolicy

**Source:** `java.base\java\util\concurrent\ThreadPoolExecutor.DiscardOldestPolicy.html`

### Class Description

```java
public static class
ThreadPoolExecutor.DiscardOldestPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that discards the oldest unhandled
request and then retries

execute

, unless the executor
is shut down, in which case the task is discarded.

**All Implemented Interfaces:** RejectedExecutionHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public DiscardOldestPolicy()

Creates a

DiscardOldestPolicy

for the given executor.

---

### Method Details

#### public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

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

#### Class ThreadPoolExecutor.DiscardOldestPolicy

java.lang.Object

- java.util.concurrent.ThreadPoolExecutor.DiscardOldestPolicy

java.util.concurrent.ThreadPoolExecutor.DiscardOldestPolicy

**All Implemented Interfaces:** RejectedExecutionHandler

**Enclosing class:** ThreadPoolExecutor

```java
public static class
ThreadPoolExecutor.DiscardOldestPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that discards the oldest unhandled
request and then retries

execute

, unless the executor
is shut down, in which case the task is discarded.

public static class

ThreadPoolExecutor.DiscardOldestPolicy

extends

Object

implements

RejectedExecutionHandler

A handler for rejected tasks that discards the oldest unhandled
request and then retries

execute

, unless the executor
is shut down, in which case the task is discarded.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DiscardOldestPolicy

()

Creates a

DiscardOldestPolicy

for the given executor.

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

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

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

DiscardOldestPolicy

()

Creates a

DiscardOldestPolicy

for the given executor.

---

#### Constructor Summary

Creates a

DiscardOldestPolicy

for the given executor.

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

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

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

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

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

- DiscardOldestPolicy

```java
public DiscardOldestPolicy()
```

Creates a

DiscardOldestPolicy

for the given executor.

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

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task

Constructor Detail

- DiscardOldestPolicy

```java
public DiscardOldestPolicy()
```

Creates a

DiscardOldestPolicy

for the given executor.

---

#### Constructor Detail

DiscardOldestPolicy

```java
public DiscardOldestPolicy()
```

Creates a

DiscardOldestPolicy

for the given executor.

---

#### DiscardOldestPolicy

public DiscardOldestPolicy()

Creates a

DiscardOldestPolicy

for the given executor.

Method Detail

- rejectedExecution

```java
public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)
```

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

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

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

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

Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.

---

