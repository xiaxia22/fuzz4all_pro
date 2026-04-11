# Interface ScheduledFuture<V>

**Source:** `java.base\java\util\concurrent\ScheduledFuture.html`

### Class Description

```java
public interface
ScheduledFuture<V>

extends
Delayed
,
Future
<V>
```

A delayed result-bearing action that can be cancelled.
Usually a scheduled future is the result of scheduling
a task with a

ScheduledExecutorService

.

**Type Parameters:** V

- The result type returned by this Future

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface ScheduledFuture<V>

**Type Parameters:** V

- The result type returned by this Future

**All Superinterfaces:** Comparable

<

Delayed

>

,

Delayed

,

Future

<V>

**All Known Subinterfaces:** RunnableScheduledFuture

<V>

```java
public interface
ScheduledFuture<V>

extends
Delayed
,
Future
<V>
```

A delayed result-bearing action that can be cancelled.
Usually a scheduled future is the result of scheduling
a task with a

ScheduledExecutorService

.

**Since:** 1.5

public interface

ScheduledFuture<V>

extends

Delayed

,

Future

<V>

A delayed result-bearing action that can be cancelled.
Usually a scheduled future is the result of scheduling
a task with a

ScheduledExecutorService

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface java.util.concurrent.

Delayed

getDelay

- Methods declared in interface java.util.concurrent.

Future

cancel

,

get

,

get

,

isCancelled

,

isDone

Method Summary

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface java.util.concurrent.

Delayed

getDelay

- Methods declared in interface java.util.concurrent.

Future

cancel

,

get

,

get

,

isCancelled

,

isDone

---

#### Method Summary

Methods declared in interface java.lang.

Comparable

compareTo

---

#### Methods declared in interface java.lang. Comparable

Methods declared in interface java.util.concurrent.

Delayed

getDelay

---

#### Methods declared in interface java.util.concurrent. Delayed

Methods declared in interface java.util.concurrent.

Future

cancel

,

get

,

get

,

isCancelled

,

isDone

---

