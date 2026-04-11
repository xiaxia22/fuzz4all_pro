# Interface Thread.UncaughtExceptionHandler

**Source:** `java.base\java\lang\Thread.UncaughtExceptionHandler.html`

### Class Description

```java
@FunctionalInterface

public static interface
Thread.UncaughtExceptionHandler
```

Interface for handlers invoked when a

Thread

abruptly
terminates due to an uncaught exception.

When a thread is about to terminate due to an uncaught exception
the Java Virtual Machine will query the thread for its

UncaughtExceptionHandler

using

Thread.getUncaughtExceptionHandler()

and will invoke the handler's

uncaughtException

method, passing the thread and the
exception as arguments.
If a thread has not had its

UncaughtExceptionHandler

explicitly set, then its

ThreadGroup

object acts as its

UncaughtExceptionHandler

. If the

ThreadGroup

object
has no
special requirements for dealing with the exception, it can forward
the invocation to the

default uncaught exception handler

.

**All Known Implementing Classes:** ThreadGroup

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void uncaughtException​(
Thread
t,

Throwable
e)

Method invoked when the given thread terminates due to the
given uncaught exception.

Any exception thrown by this method will be ignored by the
Java Virtual Machine.

**Parameters:**
- t

- the thread
- e

- the exception

---

### Additional Sections

#### Interface Thread.UncaughtExceptionHandler

**All Known Implementing Classes:** ThreadGroup

**Enclosing class:** Thread

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public static interface
Thread.UncaughtExceptionHandler
```

Interface for handlers invoked when a

Thread

abruptly
terminates due to an uncaught exception.

When a thread is about to terminate due to an uncaught exception
the Java Virtual Machine will query the thread for its

UncaughtExceptionHandler

using

Thread.getUncaughtExceptionHandler()

and will invoke the handler's

uncaughtException

method, passing the thread and the
exception as arguments.
If a thread has not had its

UncaughtExceptionHandler

explicitly set, then its

ThreadGroup

object acts as its

UncaughtExceptionHandler

. If the

ThreadGroup

object
has no
special requirements for dealing with the exception, it can forward
the invocation to the

default uncaught exception handler

.

**Since:** 1.5
**See Also:** Thread.setDefaultUncaughtExceptionHandler(java.lang.Thread.UncaughtExceptionHandler)

,

Thread.setUncaughtExceptionHandler(java.lang.Thread.UncaughtExceptionHandler)

,

ThreadGroup.uncaughtException(java.lang.Thread, java.lang.Throwable)

@FunctionalInterface

public static interface

Thread.UncaughtExceptionHandler

Interface for handlers invoked when a

Thread

abruptly
terminates due to an uncaught exception.

When a thread is about to terminate due to an uncaught exception
the Java Virtual Machine will query the thread for its

UncaughtExceptionHandler

using

Thread.getUncaughtExceptionHandler()

and will invoke the handler's

uncaughtException

method, passing the thread and the
exception as arguments.
If a thread has not had its

UncaughtExceptionHandler

explicitly set, then its

ThreadGroup

object acts as its

UncaughtExceptionHandler

. If the

ThreadGroup

object
has no
special requirements for dealing with the exception, it can forward
the invocation to the

default uncaught exception handler

.

When a thread is about to terminate due to an uncaught exception
the Java Virtual Machine will query the thread for its

UncaughtExceptionHandler

using

Thread.getUncaughtExceptionHandler()

and will invoke the handler's

uncaughtException

method, passing the thread and the
exception as arguments.
If a thread has not had its

UncaughtExceptionHandler

explicitly set, then its

ThreadGroup

object acts as its

UncaughtExceptionHandler

. If the

ThreadGroup

object
has no
special requirements for dealing with the exception, it can forward
the invocation to the

default uncaught exception handler

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

uncaughtException

​(

Thread

t,

Throwable

e)

Method invoked when the given thread terminates due to the
given uncaught exception.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

uncaughtException

​(

Thread

t,

Throwable

e)

Method invoked when the given thread terminates due to the
given uncaught exception.

---

#### Method Summary

Method invoked when the given thread terminates due to the
given uncaught exception.

============ METHOD DETAIL ==========

- Method Detail

- uncaughtException

```java
void uncaughtException​(
Thread
t,

Throwable
e)
```

Method invoked when the given thread terminates due to the
given uncaught exception.

Any exception thrown by this method will be ignored by the
Java Virtual Machine.

**Parameters:** t

- the thread
**Parameters:** e

- the exception

Method Detail

- uncaughtException

```java
void uncaughtException​(
Thread
t,

Throwable
e)
```

Method invoked when the given thread terminates due to the
given uncaught exception.

Any exception thrown by this method will be ignored by the
Java Virtual Machine.

**Parameters:** t

- the thread
**Parameters:** e

- the exception

---

#### Method Detail

uncaughtException

```java
void uncaughtException​(
Thread
t,

Throwable
e)
```

Method invoked when the given thread terminates due to the
given uncaught exception.

Any exception thrown by this method will be ignored by the
Java Virtual Machine.

**Parameters:** t

- the thread
**Parameters:** e

- the exception

---

#### uncaughtException

void uncaughtException​(

Thread

t,

Throwable

e)

Method invoked when the given thread terminates due to the
given uncaught exception.

Any exception thrown by this method will be ignored by the
Java Virtual Machine.

Any exception thrown by this method will be ignored by the
Java Virtual Machine.

---

