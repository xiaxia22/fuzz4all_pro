# Class AbstractOwnableSynchronizer

**Source:** `java.base\java\util\concurrent\locks\AbstractOwnableSynchronizer.html`

### Class Description

```java
public abstract class
AbstractOwnableSynchronizer

extends
Object

implements
Serializable
```

A synchronizer that may be exclusively owned by a thread. This
class provides a basis for creating locks and related synchronizers
that may entail a notion of ownership. The

AbstractOwnableSynchronizer

class itself does not manage or
use this information. However, subclasses and tools may use
appropriately maintained values to help control and monitor access
and provide diagnostics.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractOwnableSynchronizer()

Empty constructor for use by subclasses.

---

### Method Details

#### protected final void setExclusiveOwnerThread​(
Thread
thread)

Sets the thread that currently owns exclusive access.
A

null

argument indicates that no thread owns access.
This method does not otherwise impose any synchronization or

volatile

field accesses.

**Parameters:**
- thread

- the owner thread

---

#### protected final
Thread
getExclusiveOwnerThread()

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set. This method does not otherwise
impose any synchronization or

volatile

field accesses.

**Returns:**
- the owner thread

---

### Additional Sections

#### Class AbstractOwnableSynchronizer

java.lang.Object

- java.util.concurrent.locks.AbstractOwnableSynchronizer

java.util.concurrent.locks.AbstractOwnableSynchronizer

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AbstractQueuedLongSynchronizer

,

AbstractQueuedSynchronizer

```java
public abstract class
AbstractOwnableSynchronizer

extends
Object

implements
Serializable
```

A synchronizer that may be exclusively owned by a thread. This
class provides a basis for creating locks and related synchronizers
that may entail a notion of ownership. The

AbstractOwnableSynchronizer

class itself does not manage or
use this information. However, subclasses and tools may use
appropriately maintained values to help control and monitor access
and provide diagnostics.

**Since:** 1.6
**See Also:** Serialized Form

public abstract class

AbstractOwnableSynchronizer

extends

Object

implements

Serializable

A synchronizer that may be exclusively owned by a thread. This
class provides a basis for creating locks and related synchronizers
that may entail a notion of ownership. The

AbstractOwnableSynchronizer

class itself does not manage or
use this information. However, subclasses and tools may use
appropriately maintained values to help control and monitor access
and provide diagnostics.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractOwnableSynchronizer

()

Empty constructor for use by subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Thread

getExclusiveOwnerThread

()

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set.

protected void

setExclusiveOwnerThread

​(

Thread

thread)

Sets the thread that currently owns exclusive access.

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

AbstractOwnableSynchronizer

()

Empty constructor for use by subclasses.

---

#### Constructor Summary

Empty constructor for use by subclasses.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Thread

getExclusiveOwnerThread

()

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set.

protected void

setExclusiveOwnerThread

​(

Thread

thread)

Sets the thread that currently owns exclusive access.

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

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set.

Sets the thread that currently owns exclusive access.

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

- AbstractOwnableSynchronizer

```java
protected AbstractOwnableSynchronizer()
```

Empty constructor for use by subclasses.

============ METHOD DETAIL ==========

- Method Detail

- setExclusiveOwnerThread

```java
protected final void setExclusiveOwnerThread​(
Thread
thread)
```

Sets the thread that currently owns exclusive access.
A

null

argument indicates that no thread owns access.
This method does not otherwise impose any synchronization or

volatile

field accesses.

**Parameters:** thread

- the owner thread

- getExclusiveOwnerThread

```java
protected final
Thread
getExclusiveOwnerThread()
```

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set. This method does not otherwise
impose any synchronization or

volatile

field accesses.

**Returns:** the owner thread

Constructor Detail

- AbstractOwnableSynchronizer

```java
protected AbstractOwnableSynchronizer()
```

Empty constructor for use by subclasses.

---

#### Constructor Detail

AbstractOwnableSynchronizer

```java
protected AbstractOwnableSynchronizer()
```

Empty constructor for use by subclasses.

---

#### AbstractOwnableSynchronizer

protected AbstractOwnableSynchronizer()

Empty constructor for use by subclasses.

Method Detail

- setExclusiveOwnerThread

```java
protected final void setExclusiveOwnerThread​(
Thread
thread)
```

Sets the thread that currently owns exclusive access.
A

null

argument indicates that no thread owns access.
This method does not otherwise impose any synchronization or

volatile

field accesses.

**Parameters:** thread

- the owner thread

- getExclusiveOwnerThread

```java
protected final
Thread
getExclusiveOwnerThread()
```

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set. This method does not otherwise
impose any synchronization or

volatile

field accesses.

**Returns:** the owner thread

---

#### Method Detail

setExclusiveOwnerThread

```java
protected final void setExclusiveOwnerThread​(
Thread
thread)
```

Sets the thread that currently owns exclusive access.
A

null

argument indicates that no thread owns access.
This method does not otherwise impose any synchronization or

volatile

field accesses.

**Parameters:** thread

- the owner thread

---

#### setExclusiveOwnerThread

protected final void setExclusiveOwnerThread​(

Thread

thread)

Sets the thread that currently owns exclusive access.
A

null

argument indicates that no thread owns access.
This method does not otherwise impose any synchronization or

volatile

field accesses.

getExclusiveOwnerThread

```java
protected final
Thread
getExclusiveOwnerThread()
```

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set. This method does not otherwise
impose any synchronization or

volatile

field accesses.

**Returns:** the owner thread

---

#### getExclusiveOwnerThread

protected final

Thread

getExclusiveOwnerThread()

Returns the thread last set by

setExclusiveOwnerThread

,
or

null

if never set. This method does not otherwise
impose any synchronization or

volatile

field accesses.

---

