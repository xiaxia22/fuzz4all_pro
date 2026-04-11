# Class TimerTask

**Source:** `java.base\java\util\TimerTask.html`

### Class Description

```java
public abstract class
TimerTask

extends
Object

implements
Runnable
```

A task that can be scheduled for one-time or repeated execution by a

Timer

.

A timer task is

not

reusable. Once a task has been scheduled
for execution on a

Timer

or cancelled, subsequent attempts to
schedule it for execution will throw

IllegalStateException

.

**All Implemented Interfaces:** Runnable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TimerTask()

Creates a new timer task.

---

### Method Details

#### public abstract void run()

The action to be performed by this timer task.

**Specified by:**
- run

in interface

Runnable

**See Also:**
- Thread.run()

---

#### public boolean cancel()

Cancels this timer task. If the task has been scheduled for one-time
execution and has not yet run, or has not yet been scheduled, it will
never run. If the task has been scheduled for repeated execution, it
will never run again. (If the task is running when this call occurs,
the task will run to completion, but will never run again.)

Note that calling this method from within the

run

method of
a repeating timer task absolutely guarantees that the timer task will
not run again.

This method may be called repeatedly; the second and subsequent
calls have no effect.

**Returns:**
- true if this task is scheduled for one-time execution and has
not yet run, or this task is scheduled for repeated execution.
Returns false if the task was scheduled for one-time execution
and has already run, or if the task was never scheduled, or if
the task was already cancelled. (Loosely speaking, this method
returns

true

if it prevents one or more scheduled
executions from taking place.)

---

#### public long scheduledExecutionTime()

Returns the

scheduled

execution time of the most recent

actual

execution of this task. (If this method is invoked
while task execution is in progress, the return value is the scheduled
execution time of the ongoing task execution.)

This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:

```java
public void run() {
if (System.currentTimeMillis() - scheduledExecutionTime() >=
MAX_TARDINESS)
return; // Too late; skip this execution.
// Perform the task
}
```

This method is typically

not

used in conjunction with

fixed-delay execution

repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.

**Returns:**
- the time at which the most recent execution of this task was
scheduled to occur, in the format returned by Date.getTime().
The return value is undefined if the task has yet to commence
its first execution.

**See Also:**
- Date.getTime()

---

### Additional Sections

#### Class TimerTask

java.lang.Object

- java.util.TimerTask

java.util.TimerTask

**All Implemented Interfaces:** Runnable

```java
public abstract class
TimerTask

extends
Object

implements
Runnable
```

A task that can be scheduled for one-time or repeated execution by a

Timer

.

A timer task is

not

reusable. Once a task has been scheduled
for execution on a

Timer

or cancelled, subsequent attempts to
schedule it for execution will throw

IllegalStateException

.

**Since:** 1.3

public abstract class

TimerTask

extends

Object

implements

Runnable

A task that can be scheduled for one-time or repeated execution by a

Timer

.

A timer task is

not

reusable. Once a task has been scheduled
for execution on a

Timer

or cancelled, subsequent attempts to
schedule it for execution will throw

IllegalStateException

.

A timer task is

not

reusable. Once a task has been scheduled
for execution on a

Timer

or cancelled, subsequent attempts to
schedule it for execution will throw

IllegalStateException

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TimerTask

()

Creates a new timer task.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

cancel

()

Cancels this timer task.

abstract void

run

()

The action to be performed by this timer task.

long

scheduledExecutionTime

()

Returns the

scheduled

execution time of the most recent

actual

execution of this task.

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

Modifier

Constructor

Description

protected

TimerTask

()

Creates a new timer task.

---

#### Constructor Summary

Creates a new timer task.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

cancel

()

Cancels this timer task.

abstract void

run

()

The action to be performed by this timer task.

long

scheduledExecutionTime

()

Returns the

scheduled

execution time of the most recent

actual

execution of this task.

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

Cancels this timer task.

The action to be performed by this timer task.

Returns the

scheduled

execution time of the most recent

actual

execution of this task.

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

- TimerTask

```java
protected TimerTask()
```

Creates a new timer task.

============ METHOD DETAIL ==========

- Method Detail

- run

```java
public abstract void run()
```

The action to be performed by this timer task.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

- cancel

```java
public boolean cancel()
```

Cancels this timer task. If the task has been scheduled for one-time
execution and has not yet run, or has not yet been scheduled, it will
never run. If the task has been scheduled for repeated execution, it
will never run again. (If the task is running when this call occurs,
the task will run to completion, but will never run again.)

Note that calling this method from within the

run

method of
a repeating timer task absolutely guarantees that the timer task will
not run again.

This method may be called repeatedly; the second and subsequent
calls have no effect.

**Returns:** true if this task is scheduled for one-time execution and has
not yet run, or this task is scheduled for repeated execution.
Returns false if the task was scheduled for one-time execution
and has already run, or if the task was never scheduled, or if
the task was already cancelled. (Loosely speaking, this method
returns

true

if it prevents one or more scheduled
executions from taking place.)

- scheduledExecutionTime

```java
public long scheduledExecutionTime()
```

Returns the

scheduled

execution time of the most recent

actual

execution of this task. (If this method is invoked
while task execution is in progress, the return value is the scheduled
execution time of the ongoing task execution.)

This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:

```java
public void run() {
if (System.currentTimeMillis() - scheduledExecutionTime() >=
MAX_TARDINESS)
return; // Too late; skip this execution.
// Perform the task
}
```

This method is typically

not

used in conjunction with

fixed-delay execution

repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.

**Returns:** the time at which the most recent execution of this task was
scheduled to occur, in the format returned by Date.getTime().
The return value is undefined if the task has yet to commence
its first execution.
**See Also:** Date.getTime()

Constructor Detail

- TimerTask

```java
protected TimerTask()
```

Creates a new timer task.

---

#### Constructor Detail

TimerTask

```java
protected TimerTask()
```

Creates a new timer task.

---

#### TimerTask

protected TimerTask()

Creates a new timer task.

Method Detail

- run

```java
public abstract void run()
```

The action to be performed by this timer task.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

- cancel

```java
public boolean cancel()
```

Cancels this timer task. If the task has been scheduled for one-time
execution and has not yet run, or has not yet been scheduled, it will
never run. If the task has been scheduled for repeated execution, it
will never run again. (If the task is running when this call occurs,
the task will run to completion, but will never run again.)

Note that calling this method from within the

run

method of
a repeating timer task absolutely guarantees that the timer task will
not run again.

This method may be called repeatedly; the second and subsequent
calls have no effect.

**Returns:** true if this task is scheduled for one-time execution and has
not yet run, or this task is scheduled for repeated execution.
Returns false if the task was scheduled for one-time execution
and has already run, or if the task was never scheduled, or if
the task was already cancelled. (Loosely speaking, this method
returns

true

if it prevents one or more scheduled
executions from taking place.)

- scheduledExecutionTime

```java
public long scheduledExecutionTime()
```

Returns the

scheduled

execution time of the most recent

actual

execution of this task. (If this method is invoked
while task execution is in progress, the return value is the scheduled
execution time of the ongoing task execution.)

This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:

```java
public void run() {
if (System.currentTimeMillis() - scheduledExecutionTime() >=
MAX_TARDINESS)
return; // Too late; skip this execution.
// Perform the task
}
```

This method is typically

not

used in conjunction with

fixed-delay execution

repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.

**Returns:** the time at which the most recent execution of this task was
scheduled to occur, in the format returned by Date.getTime().
The return value is undefined if the task has yet to commence
its first execution.
**See Also:** Date.getTime()

---

#### Method Detail

run

```java
public abstract void run()
```

The action to be performed by this timer task.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

---

#### run

public abstract void run()

The action to be performed by this timer task.

cancel

```java
public boolean cancel()
```

Cancels this timer task. If the task has been scheduled for one-time
execution and has not yet run, or has not yet been scheduled, it will
never run. If the task has been scheduled for repeated execution, it
will never run again. (If the task is running when this call occurs,
the task will run to completion, but will never run again.)

Note that calling this method from within the

run

method of
a repeating timer task absolutely guarantees that the timer task will
not run again.

This method may be called repeatedly; the second and subsequent
calls have no effect.

**Returns:** true if this task is scheduled for one-time execution and has
not yet run, or this task is scheduled for repeated execution.
Returns false if the task was scheduled for one-time execution
and has already run, or if the task was never scheduled, or if
the task was already cancelled. (Loosely speaking, this method
returns

true

if it prevents one or more scheduled
executions from taking place.)

---

#### cancel

public boolean cancel()

Cancels this timer task. If the task has been scheduled for one-time
execution and has not yet run, or has not yet been scheduled, it will
never run. If the task has been scheduled for repeated execution, it
will never run again. (If the task is running when this call occurs,
the task will run to completion, but will never run again.)

Note that calling this method from within the

run

method of
a repeating timer task absolutely guarantees that the timer task will
not run again.

This method may be called repeatedly; the second and subsequent
calls have no effect.

Note that calling this method from within the

run

method of
a repeating timer task absolutely guarantees that the timer task will
not run again.

This method may be called repeatedly; the second and subsequent
calls have no effect.

This method may be called repeatedly; the second and subsequent
calls have no effect.

scheduledExecutionTime

```java
public long scheduledExecutionTime()
```

Returns the

scheduled

execution time of the most recent

actual

execution of this task. (If this method is invoked
while task execution is in progress, the return value is the scheduled
execution time of the ongoing task execution.)

This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:

```java
public void run() {
if (System.currentTimeMillis() - scheduledExecutionTime() >=
MAX_TARDINESS)
return; // Too late; skip this execution.
// Perform the task
}
```

This method is typically

not

used in conjunction with

fixed-delay execution

repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.

**Returns:** the time at which the most recent execution of this task was
scheduled to occur, in the format returned by Date.getTime().
The return value is undefined if the task has yet to commence
its first execution.
**See Also:** Date.getTime()

---

#### scheduledExecutionTime

public long scheduledExecutionTime()

Returns the

scheduled

execution time of the most recent

actual

execution of this task. (If this method is invoked
while task execution is in progress, the return value is the scheduled
execution time of the ongoing task execution.)

This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:

```java
public void run() {
if (System.currentTimeMillis() - scheduledExecutionTime() >=
MAX_TARDINESS)
return; // Too late; skip this execution.
// Perform the task
}
```

This method is typically

not

used in conjunction with

fixed-delay execution

repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.

This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:

```java
public void run() {
if (System.currentTimeMillis() - scheduledExecutionTime() >=
MAX_TARDINESS)
return; // Too late; skip this execution.
// Perform the task
}
```

This method is typically

not

used in conjunction with

fixed-delay execution

repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.

public void run() {
if (System.currentTimeMillis() - scheduledExecutionTime() >=
MAX_TARDINESS)
return; // Too late; skip this execution.
// Perform the task
}

---

