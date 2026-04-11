# Interface ForkJoinPool.ForkJoinWorkerThreadFactory

**Source:** `java.base\java\util\concurrent\ForkJoinPool.ForkJoinWorkerThreadFactory.html`

### Class Description

```java
public static interface
ForkJoinPool.ForkJoinWorkerThreadFactory
```

Factory for creating new

ForkJoinWorkerThread

s.
A

ForkJoinWorkerThreadFactory

must be defined and used
for

ForkJoinWorkerThread

subclasses that extend base
functionality or initialize threads with different contexts.

**Enclosing class:** ForkJoinPool

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ForkJoinWorkerThread
newThread​(
ForkJoinPool
pool)

Returns a new worker thread operating in the given pool.
Returning null or throwing an exception may result in tasks
never being executed. If this method throws an exception,
it is relayed to the caller of the method (for example

execute

) causing attempted thread creation. If this
method returns null or throws an exception, it is not
retried until the next attempted creation (for example
another call to

execute

).

**Parameters:**
- pool

- the pool this thread works in

**Returns:**
- the new worker thread, or

null

if the request
to create a thread is rejected

**Throws:**
- NullPointerException

- if the pool is null

---

### Additional Sections

#### Interface ForkJoinPool.ForkJoinWorkerThreadFactory

**Enclosing class:** ForkJoinPool

```java
public static interface
ForkJoinPool.ForkJoinWorkerThreadFactory
```

Factory for creating new

ForkJoinWorkerThread

s.
A

ForkJoinWorkerThreadFactory

must be defined and used
for

ForkJoinWorkerThread

subclasses that extend base
functionality or initialize threads with different contexts.

public static interface

ForkJoinPool.ForkJoinWorkerThreadFactory

Factory for creating new

ForkJoinWorkerThread

s.
A

ForkJoinWorkerThreadFactory

must be defined and used
for

ForkJoinWorkerThread

subclasses that extend base
functionality or initialize threads with different contexts.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ForkJoinWorkerThread

newThread

​(

ForkJoinPool

pool)

Returns a new worker thread operating in the given pool.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ForkJoinWorkerThread

newThread

​(

ForkJoinPool

pool)

Returns a new worker thread operating in the given pool.

---

#### Method Summary

Returns a new worker thread operating in the given pool.

============ METHOD DETAIL ==========

- Method Detail

- newThread

```java
ForkJoinWorkerThread
newThread​(
ForkJoinPool
pool)
```

Returns a new worker thread operating in the given pool.
Returning null or throwing an exception may result in tasks
never being executed. If this method throws an exception,
it is relayed to the caller of the method (for example

execute

) causing attempted thread creation. If this
method returns null or throws an exception, it is not
retried until the next attempted creation (for example
another call to

execute

).

**Parameters:** pool

- the pool this thread works in
**Returns:** the new worker thread, or

null

if the request
to create a thread is rejected
**Throws:** NullPointerException

- if the pool is null

Method Detail

- newThread

```java
ForkJoinWorkerThread
newThread​(
ForkJoinPool
pool)
```

Returns a new worker thread operating in the given pool.
Returning null or throwing an exception may result in tasks
never being executed. If this method throws an exception,
it is relayed to the caller of the method (for example

execute

) causing attempted thread creation. If this
method returns null or throws an exception, it is not
retried until the next attempted creation (for example
another call to

execute

).

**Parameters:** pool

- the pool this thread works in
**Returns:** the new worker thread, or

null

if the request
to create a thread is rejected
**Throws:** NullPointerException

- if the pool is null

---

#### Method Detail

newThread

```java
ForkJoinWorkerThread
newThread​(
ForkJoinPool
pool)
```

Returns a new worker thread operating in the given pool.
Returning null or throwing an exception may result in tasks
never being executed. If this method throws an exception,
it is relayed to the caller of the method (for example

execute

) causing attempted thread creation. If this
method returns null or throws an exception, it is not
retried until the next attempted creation (for example
another call to

execute

).

**Parameters:** pool

- the pool this thread works in
**Returns:** the new worker thread, or

null

if the request
to create a thread is rejected
**Throws:** NullPointerException

- if the pool is null

---

#### newThread

ForkJoinWorkerThread

newThread​(

ForkJoinPool

pool)

Returns a new worker thread operating in the given pool.
Returning null or throwing an exception may result in tasks
never being executed. If this method throws an exception,
it is relayed to the caller of the method (for example

execute

) causing attempted thread creation. If this
method returns null or throws an exception, it is not
retried until the next attempted creation (for example
another call to

execute

).

---

