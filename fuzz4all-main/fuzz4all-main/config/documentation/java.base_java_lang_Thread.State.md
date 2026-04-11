# Enum Thread.State

**Source:** `java.base\java\lang\Thread.State.html`

### Class Description

```java
public static enum
Thread.State

extends
Enum
<
Thread.State
>
```

A thread state. A thread can be in one of the following states:

- NEW

A thread that has not yet started is in this state.
- RUNNABLE

A thread executing in the Java virtual machine is in this state.
- BLOCKED

A thread that is blocked waiting for a monitor lock
is in this state.
- WAITING

A thread that is waiting indefinitely for another thread to
perform a particular action is in this state.
- TIMED_WAITING

A thread that is waiting for another thread to perform an action
for up to a specified waiting time is in this state.
- TERMINATED

A thread that has exited is in this state.

A thread can be in only one state at a given point in time.
These states are virtual machine states which do not reflect
any operating system thread states.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Thread.State

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Thread.State
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Thread.State c : Thread.State.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Thread.State
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum Thread.State

java.lang.Object

- java.lang.Enum

<

Thread.State

>
- - java.lang.Thread.State

java.lang.Enum

<

Thread.State

>

- java.lang.Thread.State

java.lang.Thread.State

**All Implemented Interfaces:** Serializable

,

Comparable

<

Thread.State

>

**Enclosing class:** Thread

```java
public static enum
Thread.State

extends
Enum
<
Thread.State
>
```

A thread state. A thread can be in one of the following states:

- NEW

A thread that has not yet started is in this state.
- RUNNABLE

A thread executing in the Java virtual machine is in this state.
- BLOCKED

A thread that is blocked waiting for a monitor lock
is in this state.
- WAITING

A thread that is waiting indefinitely for another thread to
perform a particular action is in this state.
- TIMED_WAITING

A thread that is waiting for another thread to perform an action
for up to a specified waiting time is in this state.
- TERMINATED

A thread that has exited is in this state.

A thread can be in only one state at a given point in time.
These states are virtual machine states which do not reflect
any operating system thread states.

**Since:** 1.5
**See Also:** Thread.getState()

public static enum

Thread.State

extends

Enum

<

Thread.State

>

A thread state. A thread can be in one of the following states:

- NEW

A thread that has not yet started is in this state.
- RUNNABLE

A thread executing in the Java virtual machine is in this state.
- BLOCKED

A thread that is blocked waiting for a monitor lock
is in this state.
- WAITING

A thread that is waiting indefinitely for another thread to
perform a particular action is in this state.
- TIMED_WAITING

A thread that is waiting for another thread to perform an action
for up to a specified waiting time is in this state.
- TERMINATED

A thread that has exited is in this state.

A thread can be in only one state at a given point in time.
These states are virtual machine states which do not reflect
any operating system thread states.

NEW

A thread that has not yet started is in this state.

RUNNABLE

A thread executing in the Java virtual machine is in this state.

BLOCKED

A thread that is blocked waiting for a monitor lock
is in this state.

WAITING

A thread that is waiting indefinitely for another thread to
perform a particular action is in this state.

TIMED_WAITING

A thread that is waiting for another thread to perform an action
for up to a specified waiting time is in this state.

TERMINATED

A thread that has exited is in this state.

A thread can be in only one state at a given point in time.
These states are virtual machine states which do not reflect
any operating system thread states.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

BLOCKED

Thread state for a thread blocked waiting for a monitor lock.

NEW

Thread state for a thread which has not yet started.

RUNNABLE

Thread state for a runnable thread.

TERMINATED

Thread state for a terminated thread.

TIMED_WAITING

Thread state for a waiting thread with a specified waiting time.

WAITING

Thread state for a waiting thread.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Thread.State

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Thread.State

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Enum Constant Summary

Enum Constants

Enum Constant

Description

BLOCKED

Thread state for a thread blocked waiting for a monitor lock.

NEW

Thread state for a thread which has not yet started.

RUNNABLE

Thread state for a runnable thread.

TERMINATED

Thread state for a terminated thread.

TIMED_WAITING

Thread state for a waiting thread with a specified waiting time.

WAITING

Thread state for a waiting thread.

---

#### Enum Constant Summary

Thread state for a thread blocked waiting for a monitor lock.

Thread state for a thread which has not yet started.

Thread state for a runnable thread.

Thread state for a terminated thread.

Thread state for a waiting thread with a specified waiting time.

Thread state for a waiting thread.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Thread.State

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Thread.State

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- NEW

```java
public static final
Thread.State
NEW
```

Thread state for a thread which has not yet started.

- RUNNABLE

```java
public static final
Thread.State
RUNNABLE
```

Thread state for a runnable thread. A thread in the runnable
state is executing in the Java virtual machine but it may
be waiting for other resources from the operating system
such as processor.

- BLOCKED

```java
public static final
Thread.State
BLOCKED
```

Thread state for a thread blocked waiting for a monitor lock.
A thread in the blocked state is waiting for a monitor lock
to enter a synchronized block/method or
reenter a synchronized block/method after calling

Object.wait

.

- WAITING

```java
public static final
Thread.State
WAITING
```

Thread state for a waiting thread.
A thread is in the waiting state due to calling one of the
following methods:

- Object.wait

with no timeout
- Thread.join

with no timeout
- LockSupport.park

A thread in the waiting state is waiting for another thread to
perform a particular action.

For example, a thread that has called

Object.wait()

on an object is waiting for another thread to call

Object.notify()

or

Object.notifyAll()

on
that object. A thread that has called

Thread.join()

is waiting for a specified thread to terminate.

- TIMED_WAITING

```java
public static final
Thread.State
TIMED_WAITING
```

Thread state for a waiting thread with a specified waiting time.
A thread is in the timed waiting state due to calling one of
the following methods with a specified positive waiting time:

- Thread.sleep
- Object.wait

with timeout
- Thread.join

with timeout
- LockSupport.parkNanos
- LockSupport.parkUntil

- TERMINATED

```java
public static final
Thread.State
TERMINATED
```

Thread state for a terminated thread.
The thread has completed execution.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Thread.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Thread.State c : Thread.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Thread.State
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- NEW

```java
public static final
Thread.State
NEW
```

Thread state for a thread which has not yet started.

- RUNNABLE

```java
public static final
Thread.State
RUNNABLE
```

Thread state for a runnable thread. A thread in the runnable
state is executing in the Java virtual machine but it may
be waiting for other resources from the operating system
such as processor.

- BLOCKED

```java
public static final
Thread.State
BLOCKED
```

Thread state for a thread blocked waiting for a monitor lock.
A thread in the blocked state is waiting for a monitor lock
to enter a synchronized block/method or
reenter a synchronized block/method after calling

Object.wait

.

- WAITING

```java
public static final
Thread.State
WAITING
```

Thread state for a waiting thread.
A thread is in the waiting state due to calling one of the
following methods:

- Object.wait

with no timeout
- Thread.join

with no timeout
- LockSupport.park

A thread in the waiting state is waiting for another thread to
perform a particular action.

For example, a thread that has called

Object.wait()

on an object is waiting for another thread to call

Object.notify()

or

Object.notifyAll()

on
that object. A thread that has called

Thread.join()

is waiting for a specified thread to terminate.

- TIMED_WAITING

```java
public static final
Thread.State
TIMED_WAITING
```

Thread state for a waiting thread with a specified waiting time.
A thread is in the timed waiting state due to calling one of
the following methods with a specified positive waiting time:

- Thread.sleep
- Object.wait

with timeout
- Thread.join

with timeout
- LockSupport.parkNanos
- LockSupport.parkUntil

- TERMINATED

```java
public static final
Thread.State
TERMINATED
```

Thread state for a terminated thread.
The thread has completed execution.

---

#### Enum Constant Detail

NEW

```java
public static final
Thread.State
NEW
```

Thread state for a thread which has not yet started.

---

#### NEW

public static final

Thread.State

NEW

Thread state for a thread which has not yet started.

RUNNABLE

```java
public static final
Thread.State
RUNNABLE
```

Thread state for a runnable thread. A thread in the runnable
state is executing in the Java virtual machine but it may
be waiting for other resources from the operating system
such as processor.

---

#### RUNNABLE

public static final

Thread.State

RUNNABLE

Thread state for a runnable thread. A thread in the runnable
state is executing in the Java virtual machine but it may
be waiting for other resources from the operating system
such as processor.

BLOCKED

```java
public static final
Thread.State
BLOCKED
```

Thread state for a thread blocked waiting for a monitor lock.
A thread in the blocked state is waiting for a monitor lock
to enter a synchronized block/method or
reenter a synchronized block/method after calling

Object.wait

.

---

#### BLOCKED

public static final

Thread.State

BLOCKED

Thread state for a thread blocked waiting for a monitor lock.
A thread in the blocked state is waiting for a monitor lock
to enter a synchronized block/method or
reenter a synchronized block/method after calling

Object.wait

.

WAITING

```java
public static final
Thread.State
WAITING
```

Thread state for a waiting thread.
A thread is in the waiting state due to calling one of the
following methods:

- Object.wait

with no timeout
- Thread.join

with no timeout
- LockSupport.park

A thread in the waiting state is waiting for another thread to
perform a particular action.

For example, a thread that has called

Object.wait()

on an object is waiting for another thread to call

Object.notify()

or

Object.notifyAll()

on
that object. A thread that has called

Thread.join()

is waiting for a specified thread to terminate.

---

#### WAITING

public static final

Thread.State

WAITING

Thread state for a waiting thread.
A thread is in the waiting state due to calling one of the
following methods:

- Object.wait

with no timeout
- Thread.join

with no timeout
- LockSupport.park

A thread in the waiting state is waiting for another thread to
perform a particular action.

For example, a thread that has called

Object.wait()

on an object is waiting for another thread to call

Object.notify()

or

Object.notifyAll()

on
that object. A thread that has called

Thread.join()

is waiting for a specified thread to terminate.

Object.wait

with no timeout

Thread.join

with no timeout

LockSupport.park

A thread in the waiting state is waiting for another thread to
perform a particular action.

For example, a thread that has called

Object.wait()

on an object is waiting for another thread to call

Object.notify()

or

Object.notifyAll()

on
that object. A thread that has called

Thread.join()

is waiting for a specified thread to terminate.

TIMED_WAITING

```java
public static final
Thread.State
TIMED_WAITING
```

Thread state for a waiting thread with a specified waiting time.
A thread is in the timed waiting state due to calling one of
the following methods with a specified positive waiting time:

- Thread.sleep
- Object.wait

with timeout
- Thread.join

with timeout
- LockSupport.parkNanos
- LockSupport.parkUntil

---

#### TIMED_WAITING

public static final

Thread.State

TIMED_WAITING

Thread state for a waiting thread with a specified waiting time.
A thread is in the timed waiting state due to calling one of
the following methods with a specified positive waiting time:

- Thread.sleep
- Object.wait

with timeout
- Thread.join

with timeout
- LockSupport.parkNanos
- LockSupport.parkUntil

Thread.sleep

Object.wait

with timeout

Thread.join

with timeout

LockSupport.parkNanos

LockSupport.parkUntil

TERMINATED

```java
public static final
Thread.State
TERMINATED
```

Thread state for a terminated thread.
The thread has completed execution.

---

#### TERMINATED

public static final

Thread.State

TERMINATED

Thread state for a terminated thread.
The thread has completed execution.

Method Detail

- values

```java
public static
Thread.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Thread.State c : Thread.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Thread.State
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
Thread.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Thread.State c : Thread.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Thread.State

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Thread.State c : Thread.State.values())
System.out.println(c);
```

for (Thread.State c : Thread.State.values())
System.out.println(c);

valueOf

```java
public static
Thread.State
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

Thread.State

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

