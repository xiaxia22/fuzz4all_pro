# Interface RunnableScheduledFuture<V>

**Source:** `java.base\java\util\concurrent\RunnableScheduledFuture.html`

### Class Description

```java
public interface
RunnableScheduledFuture<V>

extends
RunnableFuture
<V>,
ScheduledFuture
<V>
```

A

ScheduledFuture

that is

Runnable

. Successful
execution of the

run

method causes completion of the

Future

and allows access to its results.

**Type Parameters:** V

- The result type returned by this Future's

get

method

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isPeriodic()

Returns

true

if this task is periodic. A periodic task may
re-run according to some schedule. A non-periodic task can be
run only once.

**Returns:**
- true

if this task is periodic

---

### Additional Sections

#### Interface RunnableScheduledFuture<V>

**Type Parameters:** V

- The result type returned by this Future's

get

method

**All Superinterfaces:** Comparable

<

Delayed

>

,

Delayed

,

Future

<V>

,

Runnable

,

RunnableFuture

<V>

,

ScheduledFuture

<V>

```java
public interface
RunnableScheduledFuture<V>

extends
RunnableFuture
<V>,
ScheduledFuture
<V>
```

A

ScheduledFuture

that is

Runnable

. Successful
execution of the

run

method causes completion of the

Future

and allows access to its results.

**Since:** 1.6
**See Also:** FutureTask

,

Executor

public interface

RunnableScheduledFuture<V>

extends

RunnableFuture

<V>,

ScheduledFuture

<V>

A

ScheduledFuture

that is

Runnable

. Successful
execution of the

run

method causes completion of the

Future

and allows access to its results.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isPeriodic

()

Returns

true

if this task is periodic.

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

- Methods declared in interface java.util.concurrent.

RunnableFuture

run

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isPeriodic

()

Returns

true

if this task is periodic.

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

- Methods declared in interface java.util.concurrent.

RunnableFuture

run

---

#### Method Summary

Returns

true

if this task is periodic.

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

#### Methods declared in interface java.util.concurrent. Future

Methods declared in interface java.util.concurrent.

RunnableFuture

run

---

#### Methods declared in interface java.util.concurrent. RunnableFuture

============ METHOD DETAIL ==========

- Method Detail

- isPeriodic

```java
boolean isPeriodic()
```

Returns

true

if this task is periodic. A periodic task may
re-run according to some schedule. A non-periodic task can be
run only once.

**Returns:** true

if this task is periodic

Method Detail

- isPeriodic

```java
boolean isPeriodic()
```

Returns

true

if this task is periodic. A periodic task may
re-run according to some schedule. A non-periodic task can be
run only once.

**Returns:** true

if this task is periodic

---

#### Method Detail

isPeriodic

```java
boolean isPeriodic()
```

Returns

true

if this task is periodic. A periodic task may
re-run according to some schedule. A non-periodic task can be
run only once.

**Returns:** true

if this task is periodic

---

#### isPeriodic

boolean isPeriodic()

Returns

true

if this task is periodic. A periodic task may
re-run according to some schedule. A non-periodic task can be
run only once.

---

