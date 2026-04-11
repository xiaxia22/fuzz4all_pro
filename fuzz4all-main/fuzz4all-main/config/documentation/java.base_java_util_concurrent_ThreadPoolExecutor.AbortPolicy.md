# Class ThreadPoolExecutor.AbortPolicy

**Source:** `java.base\java\util\concurrent\ThreadPoolExecutor.AbortPolicy.html`

### Class Description

```java
public static class
ThreadPoolExecutor.AbortPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that throws a

RejectedExecutionException

.

This is the default handler for

ThreadPoolExecutor

and

ScheduledThreadPoolExecutor

.

**All Implemented Interfaces:** RejectedExecutionHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public AbortPolicy()

Creates an

AbortPolicy

.

---

### Method Details

#### public void rejectedExecution​(
Runnable
r,

ThreadPoolExecutor
e)

Always throws RejectedExecutionException.

**Specified by:**
- rejectedExecution

in interface

RejectedExecutionHandler

**Parameters:**
- r

- the runnable task requested to be executed
- e

- the executor attempting to execute this task

**Throws:**
- RejectedExecutionException

- always

---

### Additional Sections

#### Class ThreadPoolExecutor.AbortPolicy

java.lang.Object

- java.util.concurrent.ThreadPoolExecutor.AbortPolicy

java.util.concurrent.ThreadPoolExecutor.AbortPolicy

**All Implemented Interfaces:** RejectedExecutionHandler

**Enclosing class:** ThreadPoolExecutor

```java
public static class
ThreadPoolExecutor.AbortPolicy

extends
Object

implements
RejectedExecutionHandler
```

A handler for rejected tasks that throws a

RejectedExecutionException

.

This is the default handler for

ThreadPoolExecutor

and

ScheduledThreadPoolExecutor

.

public static class

ThreadPoolExecutor.AbortPolicy

extends

Object

implements

RejectedExecutionHandler

A handler for rejected tasks that throws a

RejectedExecutionException

.

This is the default handler for

ThreadPoolExecutor

and

ScheduledThreadPoolExecutor

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbortPolicy

()

Creates an

AbortPolicy

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

Always throws RejectedExecutionException.

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

AbortPolicy

()

Creates an

AbortPolicy

.

---

#### Constructor Summary

Creates an

AbortPolicy

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

Always throws RejectedExecutionException.

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

Always throws RejectedExecutionException.

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

- AbortPolicy

```java
public AbortPolicy()
```

Creates an

AbortPolicy

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

Always throws RejectedExecutionException.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task
**Throws:** RejectedExecutionException

- always

Constructor Detail

- AbortPolicy

```java
public AbortPolicy()
```

Creates an

AbortPolicy

.

---

#### Constructor Detail

AbortPolicy

```java
public AbortPolicy()
```

Creates an

AbortPolicy

.

---

#### AbortPolicy

public AbortPolicy()

Creates an

AbortPolicy

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

Always throws RejectedExecutionException.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task
**Throws:** RejectedExecutionException

- always

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

Always throws RejectedExecutionException.

**Specified by:** rejectedExecution

in interface

RejectedExecutionHandler
**Parameters:** r

- the runnable task requested to be executed
**Parameters:** e

- the executor attempting to execute this task
**Throws:** RejectedExecutionException

- always

---

#### rejectedExecution

public void rejectedExecution​(

Runnable

r,

ThreadPoolExecutor

e)

Always throws RejectedExecutionException.

---

