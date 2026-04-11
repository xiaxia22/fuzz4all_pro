# Class RecursiveTask<V>

**Source:** `java.base\java\util\concurrent\RecursiveTask.html`

### Class Description

```java
public abstract class
RecursiveTask<V>

extends
ForkJoinTask
<V>
```

A recursive result-bearing

ForkJoinTask

.

For a classic example, here is a task computing Fibonacci numbers:

```java
class Fibonacci extends RecursiveTask<Integer> {
final int n;
Fibonacci(int n) { this.n = n; }
protected Integer compute() {
if (n <= 1)
return n;
Fibonacci f1 = new Fibonacci(n - 1);
f1.fork();
Fibonacci f2 = new Fibonacci(n - 2);
return f2.compute() + f1.join();
}
}
```

However, besides being a dumb way to compute Fibonacci functions
(there is a simple fast linear algorithm that you'd use in
practice), this is likely to perform poorly because the smallest
subtasks are too small to be worthwhile splitting up. Instead, as
is the case for nearly all fork/join applications, you'd pick some
minimum granularity size (for example 10 here) for which you always
sequentially solve rather than subdividing.

**All Implemented Interfaces:** Serializable

,

Future

<V>

---

### Field Details

*No entries found.*

### Constructor Details

#### public RecursiveTask()

*No description found.*

---

### Method Details

#### protected abstract
V
compute()

The main computation performed by this task.

**Returns:**
- the result of the computation

---

#### protected final boolean exec()

Implements execution conventions for RecursiveTask.

**Specified by:**
- exec

in class

ForkJoinTask

<

V

>

**Returns:**
- true

if this task is known to have completed normally

---

### Additional Sections

#### Class RecursiveTask<V>

java.lang.Object

- java.util.concurrent.ForkJoinTask

<V>
- - java.util.concurrent.RecursiveTask<V>

java.util.concurrent.ForkJoinTask

<V>

- java.util.concurrent.RecursiveTask<V>

java.util.concurrent.RecursiveTask<V>

**All Implemented Interfaces:** Serializable

,

Future

<V>

```java
public abstract class
RecursiveTask<V>

extends
ForkJoinTask
<V>
```

A recursive result-bearing

ForkJoinTask

.

For a classic example, here is a task computing Fibonacci numbers:

```java
class Fibonacci extends RecursiveTask<Integer> {
final int n;
Fibonacci(int n) { this.n = n; }
protected Integer compute() {
if (n <= 1)
return n;
Fibonacci f1 = new Fibonacci(n - 1);
f1.fork();
Fibonacci f2 = new Fibonacci(n - 2);
return f2.compute() + f1.join();
}
}
```

However, besides being a dumb way to compute Fibonacci functions
(there is a simple fast linear algorithm that you'd use in
practice), this is likely to perform poorly because the smallest
subtasks are too small to be worthwhile splitting up. Instead, as
is the case for nearly all fork/join applications, you'd pick some
minimum granularity size (for example 10 here) for which you always
sequentially solve rather than subdividing.

**Since:** 1.7
**See Also:** Serialized Form

public abstract class

RecursiveTask<V>

extends

ForkJoinTask

<V>

A recursive result-bearing

ForkJoinTask

.

For a classic example, here is a task computing Fibonacci numbers:

```java
class Fibonacci extends RecursiveTask<Integer> {
final int n;
Fibonacci(int n) { this.n = n; }
protected Integer compute() {
if (n <= 1)
return n;
Fibonacci f1 = new Fibonacci(n - 1);
f1.fork();
Fibonacci f2 = new Fibonacci(n - 2);
return f2.compute() + f1.join();
}
}
```

However, besides being a dumb way to compute Fibonacci functions
(there is a simple fast linear algorithm that you'd use in
practice), this is likely to perform poorly because the smallest
subtasks are too small to be worthwhile splitting up. Instead, as
is the case for nearly all fork/join applications, you'd pick some
minimum granularity size (for example 10 here) for which you always
sequentially solve rather than subdividing.

For a classic example, here is a task computing Fibonacci numbers:

```java
class Fibonacci extends RecursiveTask<Integer> {
final int n;
Fibonacci(int n) { this.n = n; }
protected Integer compute() {
if (n <= 1)
return n;
Fibonacci f1 = new Fibonacci(n - 1);
f1.fork();
Fibonacci f2 = new Fibonacci(n - 2);
return f2.compute() + f1.join();
}
}
```

However, besides being a dumb way to compute Fibonacci functions
(there is a simple fast linear algorithm that you'd use in
practice), this is likely to perform poorly because the smallest
subtasks are too small to be worthwhile splitting up. Instead, as
is the case for nearly all fork/join applications, you'd pick some
minimum granularity size (for example 10 here) for which you always
sequentially solve rather than subdividing.

class Fibonacci extends RecursiveTask<Integer> {
final int n;
Fibonacci(int n) { this.n = n; }
protected Integer compute() {
if (n <= 1)
return n;
Fibonacci f1 = new Fibonacci(n - 1);
f1.fork();
Fibonacci f2 = new Fibonacci(n - 2);
return f2.compute() + f1.join();
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RecursiveTask

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

V

compute

()

The main computation performed by this task.

protected boolean

exec

()

Implements execution conventions for RecursiveTask.

- Methods declared in class java.util.concurrent.

ForkJoinTask

adapt

,

adapt

,

adapt

,

cancel

,

compareAndSetForkJoinTaskTag

,

complete

,

completeExceptionally

,

fork

,

get

,

get

,

getException

,

getForkJoinTaskTag

,

getPool

,

getQueuedTaskCount

,

getRawResult

,

getSurplusQueuedTaskCount

,

helpQuiesce

,

inForkJoinPool

,

invoke

,

invokeAll

,

invokeAll

,

invokeAll

,

isCompletedAbnormally

,

isCompletedNormally

,

join

,

peekNextLocalTask

,

pollNextLocalTask

,

pollSubmission

,

pollTask

,

quietlyComplete

,

quietlyInvoke

,

quietlyJoin

,

reinitialize

,

setForkJoinTaskTag

,

setRawResult

,

tryUnfork

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

Future

isCancelled

,

isDone

Constructor Summary

Constructors

Constructor

Description

RecursiveTask

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

V

compute

()

The main computation performed by this task.

protected boolean

exec

()

Implements execution conventions for RecursiveTask.

- Methods declared in class java.util.concurrent.

ForkJoinTask

adapt

,

adapt

,

adapt

,

cancel

,

compareAndSetForkJoinTaskTag

,

complete

,

completeExceptionally

,

fork

,

get

,

get

,

getException

,

getForkJoinTaskTag

,

getPool

,

getQueuedTaskCount

,

getRawResult

,

getSurplusQueuedTaskCount

,

helpQuiesce

,

inForkJoinPool

,

invoke

,

invokeAll

,

invokeAll

,

invokeAll

,

isCompletedAbnormally

,

isCompletedNormally

,

join

,

peekNextLocalTask

,

pollNextLocalTask

,

pollSubmission

,

pollTask

,

quietlyComplete

,

quietlyInvoke

,

quietlyJoin

,

reinitialize

,

setForkJoinTaskTag

,

setRawResult

,

tryUnfork

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

Future

isCancelled

,

isDone

---

#### Method Summary

The main computation performed by this task.

Implements execution conventions for RecursiveTask.

Methods declared in class java.util.concurrent.

ForkJoinTask

adapt

,

adapt

,

adapt

,

cancel

,

compareAndSetForkJoinTaskTag

,

complete

,

completeExceptionally

,

fork

,

get

,

get

,

getException

,

getForkJoinTaskTag

,

getPool

,

getQueuedTaskCount

,

getRawResult

,

getSurplusQueuedTaskCount

,

helpQuiesce

,

inForkJoinPool

,

invoke

,

invokeAll

,

invokeAll

,

invokeAll

,

isCompletedAbnormally

,

isCompletedNormally

,

join

,

peekNextLocalTask

,

pollNextLocalTask

,

pollSubmission

,

pollTask

,

quietlyComplete

,

quietlyInvoke

,

quietlyJoin

,

reinitialize

,

setForkJoinTaskTag

,

setRawResult

,

tryUnfork

---

#### Methods declared in class java.util.concurrent. ForkJoinTask

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

Future

isCancelled

,

isDone

---

#### Methods declared in interface java.util.concurrent. Future

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RecursiveTask

```java
public RecursiveTask()
```

============ METHOD DETAIL ==========

- Method Detail

- compute

```java
protected abstract
V
compute()
```

The main computation performed by this task.

**Returns:** the result of the computation

- exec

```java
protected final boolean exec()
```

Implements execution conventions for RecursiveTask.

**Specified by:** exec

in class

ForkJoinTask

<

V

>
**Returns:** true

if this task is known to have completed normally

Constructor Detail

- RecursiveTask

```java
public RecursiveTask()
```

---

#### Constructor Detail

RecursiveTask

```java
public RecursiveTask()
```

---

#### RecursiveTask

public RecursiveTask()

Method Detail

- compute

```java
protected abstract
V
compute()
```

The main computation performed by this task.

**Returns:** the result of the computation

- exec

```java
protected final boolean exec()
```

Implements execution conventions for RecursiveTask.

**Specified by:** exec

in class

ForkJoinTask

<

V

>
**Returns:** true

if this task is known to have completed normally

---

#### Method Detail

compute

```java
protected abstract
V
compute()
```

The main computation performed by this task.

**Returns:** the result of the computation

---

#### compute

protected abstract

V

compute()

The main computation performed by this task.

exec

```java
protected final boolean exec()
```

Implements execution conventions for RecursiveTask.

**Specified by:** exec

in class

ForkJoinTask

<

V

>
**Returns:** true

if this task is known to have completed normally

---

#### exec

protected final boolean exec()

Implements execution conventions for RecursiveTask.

---

