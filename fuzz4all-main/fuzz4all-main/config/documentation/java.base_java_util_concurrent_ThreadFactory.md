# Interface ThreadFactory

**Source:** `java.base\java\util\concurrent\ThreadFactory.html`

### Class Description

```java
public interface
ThreadFactory
```

An object that creates new threads on demand. Using thread factories
removes hardwiring of calls to

new Thread

,
enabling applications to use special thread subclasses, priorities, etc.

The simplest implementation of this interface is just:

```java
class SimpleThreadFactory implements ThreadFactory {
public Thread newThread(Runnable r) {
return new Thread(r);
}
}
```

The

Executors.defaultThreadFactory()

method provides a more
useful simple implementation, that sets the created thread context
to known values before returning it.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Thread
newThread​(
Runnable
r)

Constructs a new

Thread

. Implementations may also initialize
priority, name, daemon status,

ThreadGroup

, etc.

**Parameters:**
- r

- a runnable to be executed by new thread instance

**Returns:**
- constructed thread, or

null

if the request to
create a thread is rejected

---

### Additional Sections

#### Interface ThreadFactory

```java
public interface
ThreadFactory
```

An object that creates new threads on demand. Using thread factories
removes hardwiring of calls to

new Thread

,
enabling applications to use special thread subclasses, priorities, etc.

The simplest implementation of this interface is just:

```java
class SimpleThreadFactory implements ThreadFactory {
public Thread newThread(Runnable r) {
return new Thread(r);
}
}
```

The

Executors.defaultThreadFactory()

method provides a more
useful simple implementation, that sets the created thread context
to known values before returning it.

**Since:** 1.5

public interface

ThreadFactory

An object that creates new threads on demand. Using thread factories
removes hardwiring of calls to

new Thread

,
enabling applications to use special thread subclasses, priorities, etc.

The simplest implementation of this interface is just:

```java
class SimpleThreadFactory implements ThreadFactory {
public Thread newThread(Runnable r) {
return new Thread(r);
}
}
```

The

Executors.defaultThreadFactory()

method provides a more
useful simple implementation, that sets the created thread context
to known values before returning it.

The simplest implementation of this interface is just:

```java
class SimpleThreadFactory implements ThreadFactory {
public Thread newThread(Runnable r) {
return new Thread(r);
}
}
```

The

Executors.defaultThreadFactory()

method provides a more
useful simple implementation, that sets the created thread context
to known values before returning it.

class SimpleThreadFactory implements ThreadFactory {
public Thread newThread(Runnable r) {
return new Thread(r);
}
}

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Thread

newThread

​(

Runnable

r)

Constructs a new

Thread

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Thread

newThread

​(

Runnable

r)

Constructs a new

Thread

.

---

#### Method Summary

Constructs a new

Thread

.

============ METHOD DETAIL ==========

- Method Detail

- newThread

```java
Thread
newThread​(
Runnable
r)
```

Constructs a new

Thread

. Implementations may also initialize
priority, name, daemon status,

ThreadGroup

, etc.

**Parameters:** r

- a runnable to be executed by new thread instance
**Returns:** constructed thread, or

null

if the request to
create a thread is rejected

Method Detail

- newThread

```java
Thread
newThread​(
Runnable
r)
```

Constructs a new

Thread

. Implementations may also initialize
priority, name, daemon status,

ThreadGroup

, etc.

**Parameters:** r

- a runnable to be executed by new thread instance
**Returns:** constructed thread, or

null

if the request to
create a thread is rejected

---

#### Method Detail

newThread

```java
Thread
newThread​(
Runnable
r)
```

Constructs a new

Thread

. Implementations may also initialize
priority, name, daemon status,

ThreadGroup

, etc.

**Parameters:** r

- a runnable to be executed by new thread instance
**Returns:** constructed thread, or

null

if the request to
create a thread is rejected

---

#### newThread

Thread

newThread​(

Runnable

r)

Constructs a new

Thread

. Implementations may also initialize
priority, name, daemon status,

ThreadGroup

, etc.

---

