# Interface Iterable<T>

**Source:** `java.base\java\lang\Iterable.html`

### Class Description

```java
public interface
Iterable<T>
```

Implementing this interface allows an object to be the target of the enhanced

for

statement (sometimes called the "for-each loop" statement).

**Type Parameters:** T

- the type of elements returned by the iterator

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Iterator
<
T
> iterator()

Returns an iterator over elements of type

T

.

**Returns:**
- an Iterator.

---

#### default void forEach​(
Consumer
<? super
T
> action)

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception. Actions are performed in the order of iteration, if that
order is specified. Exceptions thrown by the action are relayed to the
caller.

The behavior of this method is unspecified if the action performs
side-effects that modify the underlying source of elements, unless an
overriding class has specified a concurrent modification policy.

**Parameters:**
- action

- The action to be performed for each element

**Throws:**
- NullPointerException

- if the specified action is null

**Since:**
- 1.8

**Implementation Requirements:**
- The default implementation behaves as if:

```java
for (T t : this)
action.accept(t);
```

---

#### default
Spliterator
<
T
> spliterator()

Creates a

Spliterator

over the elements described by this

Iterable

.

**Returns:**
- a

Spliterator

over the elements described by this

Iterable

.

**Since:**
- 1.8

**Implementation Requirements:**
- The default implementation creates an

early-binding

spliterator from the iterable's

Iterator

. The spliterator
inherits the

fail-fast

properties of the iterable's iterator.

**Implementation Note:**
- The default implementation should usually be overridden. The
spliterator returned by the default implementation has poor splitting
capabilities, is unsized, and does not report any spliterator
characteristics. Implementing classes can nearly always provide a
better implementation.

---

### Additional Sections

#### Interface Iterable<T>

**Type Parameters:** T

- the type of elements returned by the iterator

**All Known Subinterfaces:** BeanContext

,

BeanContextServices

,

BlockingDeque

<E>

,

BlockingQueue

<E>

,

Collection

<E>

,

Deque

<E>

,

DirectoryStream

<T>

,

EventSet

,

List

<E>

,

NavigableSet

<E>

,

NodeSetData

<T>

,

Path

,

Queue

<E>

,

SecureDirectoryStream

<T>

,

Set

<E>

,

SortedSet

<E>

,

TransferQueue

<E>

,

XPathNodes

**All Known Implementing Classes:** AbstractCollection

,

AbstractList

,

AbstractQueue

,

AbstractSequentialList

,

AbstractSet

,

ArrayBlockingQueue

,

ArrayDeque

,

ArrayList

,

AttributeList

,

BatchUpdateException

,

BeanContextServicesSupport

,

BeanContextSupport

,

ConcurrentHashMap.KeySetView

,

ConcurrentLinkedDeque

,

ConcurrentLinkedQueue

,

ConcurrentSkipListSet

,

CopyOnWriteArrayList

,

CopyOnWriteArraySet

,

DataTruncation

,

DelayQueue

,

DocTreePath

,

EnumSet

,

HashSet

,

JobStateReasons

,

LinkedBlockingDeque

,

LinkedBlockingQueue

,

LinkedHashSet

,

LinkedList

,

LinkedTransferQueue

,

PriorityBlockingQueue

,

PriorityQueue

,

RoleList

,

RoleUnresolvedList

,

RowSetWarning

,

SerialException

,

ServiceLoader

,

SQLClientInfoException

,

SQLDataException

,

SQLException

,

SQLFeatureNotSupportedException

,

SQLIntegrityConstraintViolationException

,

SQLInvalidAuthorizationSpecException

,

SQLNonTransientConnectionException

,

SQLNonTransientException

,

SQLRecoverableException

,

SQLSyntaxErrorException

,

SQLTimeoutException

,

SQLTransactionRollbackException

,

SQLTransientConnectionException

,

SQLTransientException

,

SQLWarning

,

Stack

,

SyncFactoryException

,

SynchronousQueue

,

SyncProviderException

,

TreePath

,

TreeSet

,

Vector

```java
public interface
Iterable<T>
```

Implementing this interface allows an object to be the target of the enhanced

for

statement (sometimes called the "for-each loop" statement).

**Since:** 1.5
**See The Java™ Language Specification :** 14.14.2 The enhanced

for

statement

public interface

Iterable<T>

Implementing this interface allows an object to be the target of the enhanced

for

statement (sometimes called the "for-each loop" statement).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default void

forEach

​(

Consumer

<? super

T

> action)

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception.

Iterator

<

T

>

iterator

()

Returns an iterator over elements of type

T

.

default

Spliterator

<

T

>

spliterator

()

Creates a

Spliterator

over the elements described by this

Iterable

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default void

forEach

​(

Consumer

<? super

T

> action)

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception.

Iterator

<

T

>

iterator

()

Returns an iterator over elements of type

T

.

default

Spliterator

<

T

>

spliterator

()

Creates a

Spliterator

over the elements described by this

Iterable

.

---

#### Method Summary

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception.

Returns an iterator over elements of type

T

.

Creates a

Spliterator

over the elements described by this

Iterable

.

============ METHOD DETAIL ==========

- Method Detail

- iterator

```java
Iterator
<
T
> iterator()
```

Returns an iterator over elements of type

T

.

**Returns:** an Iterator.

- forEach

```java
default void forEach​(
Consumer
<? super
T
> action)
```

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception. Actions are performed in the order of iteration, if that
order is specified. Exceptions thrown by the action are relayed to the
caller.

The behavior of this method is unspecified if the action performs
side-effects that modify the underlying source of elements, unless an
overriding class has specified a concurrent modification policy.

**Implementation Requirements:** The default implementation behaves as if:

```java
for (T t : this)
action.accept(t);
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null
**Since:** 1.8

- spliterator

```java
default
Spliterator
<
T
> spliterator()
```

Creates a

Spliterator

over the elements described by this

Iterable

.

**Implementation Requirements:** The default implementation creates an

early-binding

spliterator from the iterable's

Iterator

. The spliterator
inherits the

fail-fast

properties of the iterable's iterator.
**Implementation Note:** The default implementation should usually be overridden. The
spliterator returned by the default implementation has poor splitting
capabilities, is unsized, and does not report any spliterator
characteristics. Implementing classes can nearly always provide a
better implementation.
**Returns:** a

Spliterator

over the elements described by this

Iterable

.
**Since:** 1.8

Method Detail

- iterator

```java
Iterator
<
T
> iterator()
```

Returns an iterator over elements of type

T

.

**Returns:** an Iterator.

- forEach

```java
default void forEach​(
Consumer
<? super
T
> action)
```

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception. Actions are performed in the order of iteration, if that
order is specified. Exceptions thrown by the action are relayed to the
caller.

The behavior of this method is unspecified if the action performs
side-effects that modify the underlying source of elements, unless an
overriding class has specified a concurrent modification policy.

**Implementation Requirements:** The default implementation behaves as if:

```java
for (T t : this)
action.accept(t);
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null
**Since:** 1.8

- spliterator

```java
default
Spliterator
<
T
> spliterator()
```

Creates a

Spliterator

over the elements described by this

Iterable

.

**Implementation Requirements:** The default implementation creates an

early-binding

spliterator from the iterable's

Iterator

. The spliterator
inherits the

fail-fast

properties of the iterable's iterator.
**Implementation Note:** The default implementation should usually be overridden. The
spliterator returned by the default implementation has poor splitting
capabilities, is unsized, and does not report any spliterator
characteristics. Implementing classes can nearly always provide a
better implementation.
**Returns:** a

Spliterator

over the elements described by this

Iterable

.
**Since:** 1.8

---

#### Method Detail

iterator

```java
Iterator
<
T
> iterator()
```

Returns an iterator over elements of type

T

.

**Returns:** an Iterator.

---

#### iterator

Iterator

<

T

> iterator()

Returns an iterator over elements of type

T

.

forEach

```java
default void forEach​(
Consumer
<? super
T
> action)
```

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception. Actions are performed in the order of iteration, if that
order is specified. Exceptions thrown by the action are relayed to the
caller.

The behavior of this method is unspecified if the action performs
side-effects that modify the underlying source of elements, unless an
overriding class has specified a concurrent modification policy.

**Implementation Requirements:** The default implementation behaves as if:

```java
for (T t : this)
action.accept(t);
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null
**Since:** 1.8

---

#### forEach

default void forEach​(

Consumer

<? super

T

> action)

Performs the given action for each element of the

Iterable

until all elements have been processed or the action throws an
exception. Actions are performed in the order of iteration, if that
order is specified. Exceptions thrown by the action are relayed to the
caller.

The behavior of this method is unspecified if the action performs
side-effects that modify the underlying source of elements, unless an
overriding class has specified a concurrent modification policy.

The behavior of this method is unspecified if the action performs
side-effects that modify the underlying source of elements, unless an
overriding class has specified a concurrent modification policy.

The default implementation behaves as if:

```java
for (T t : this)
action.accept(t);
```

for (T t : this)
action.accept(t);

spliterator

```java
default
Spliterator
<
T
> spliterator()
```

Creates a

Spliterator

over the elements described by this

Iterable

.

**Implementation Requirements:** The default implementation creates an

early-binding

spliterator from the iterable's

Iterator

. The spliterator
inherits the

fail-fast

properties of the iterable's iterator.
**Implementation Note:** The default implementation should usually be overridden. The
spliterator returned by the default implementation has poor splitting
capabilities, is unsized, and does not report any spliterator
characteristics. Implementing classes can nearly always provide a
better implementation.
**Returns:** a

Spliterator

over the elements described by this

Iterable

.
**Since:** 1.8

---

#### spliterator

default

Spliterator

<

T

> spliterator()

Creates a

Spliterator

over the elements described by this

Iterable

.

---

