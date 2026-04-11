# Class ThreadPoolExecutor.DiscardPolicy

**Source:** `java.base\java\util\concurrent\ThreadPoolExecutor.DiscardPolicy.html`

### Class Description

```java
public static class
ThreadPoolExecutor.DiscardPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that silently discards the
rejected task.

**All Implemented Interfaces:** RejectedExecutionHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public DiscardPolicy()

Creates a

DiscardPolicy

.

---

### Method Details

#### public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)

Does nothing, which has the effect of discarding task r.

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

#### Class ThreadPoolExecutor.DiscardPolicy

java.lang.Object

- java.util.concurrent.ThreadPoolExecutor.DiscardPolicy

java.util.concurrent.ThreadPoolExecutor.DiscardPolicy

**All Implemented Interfaces:** RejectedExecutionHandler

**Enclosing class:** ThreadPoolExecutor

```java
public static class
ThreadPoolExecutor.DiscardPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that silently discards the
rejected task.

public static class

ThreadPoolExecutor.DiscardPolicy

extends

Object

implements

RejectedExecutionHandler

A handler for rejected tasks that silently discards the
rejected task.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DiscardPolicy

()

Creates a

DiscardPolicy

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

Does nothing, which has the effect of discarding task r.

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

DiscardPolicy

()

Creates a

DiscardPolicy

.

---

#### Constructor Summary

Creates a

DiscardPolicy

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

Does nothing, which has the effect of discarding task r.

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

Does nothing, which has the effect of discarding task r.

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

- DiscardPolicy

```java
public DiscardPolicy()
```

Creates a

DiscardPolicy

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

Does nothing, which has the effect of discarding task r.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task

Constructor Detail

- DiscardPolicy

```java
public DiscardPolicy()
```

Creates a

DiscardPolicy

.

---

#### Constructor Detail

DiscardPolicy

```java
public DiscardPolicy()
```

Creates a

DiscardPolicy

.

---

#### DiscardPolicy

public DiscardPolicy()

Creates a

DiscardPolicy

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

Does nothing, which has the effect of discarding task r.

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

Does nothing, which has the effect of discarding task r.

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

Does nothing, which has the effect of discarding task r.

---

