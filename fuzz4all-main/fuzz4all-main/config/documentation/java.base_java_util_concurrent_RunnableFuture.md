# Interface RunnableFuture<V>

**Source:** `java.base\java\util\concurrent\RunnableFuture.html`

### Class Description

```java
public interface
RunnableFuture<V>

extends
Runnable
,
Future
<V>
```

A

Future

that is

Runnable

. Successful execution of
the

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

#### void run()

Sets this Future to the result of its computation
unless it has been cancelled.

**Specified by:**
- run

in interface

Runnable

**See Also:**
- Thread.run()

---

### Additional Sections

#### Interface RunnableFuture<V>

**Type Parameters:** V

- The result type returned by this Future's

get

method

**All Superinterfaces:** Future

<V>

,

Runnable

**All Known Subinterfaces:** RunnableScheduledFuture

<V>

**All Known Implementing Classes:** FutureTask

,

SwingWorker

```java
public interface
RunnableFuture<V>

extends
Runnable
,
Future
<V>
```

A

Future

that is

Runnable

. Successful execution of
the

run

method causes completion of the

Future

and allows access to its results.

**Since:** 1.6
**See Also:** FutureTask

,

Executor

public interface

RunnableFuture<V>

extends

Runnable

,

Future

<V>

A

Future

that is

Runnable

. Successful execution of
the

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

void

run

()

Sets this Future to the result of its computation
unless it has been cancelled.

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

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

run

()

Sets this Future to the result of its computation
unless it has been cancelled.

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

Sets this Future to the result of its computation
unless it has been cancelled.

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

============ METHOD DETAIL ==========

- Method Detail

- run

```java
void run()
```

Sets this Future to the result of its computation
unless it has been cancelled.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

Method Detail

- run

```java
void run()
```

Sets this Future to the result of its computation
unless it has been cancelled.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

---

#### Method Detail

run

```java
void run()
```

Sets this Future to the result of its computation
unless it has been cancelled.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

---

#### run

void run()

Sets this Future to the result of its computation
unless it has been cancelled.

---

