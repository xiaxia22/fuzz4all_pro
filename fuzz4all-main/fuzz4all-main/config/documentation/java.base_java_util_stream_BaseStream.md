# Interface BaseStream<T,​S extends BaseStream<T,​S>>

**Source:** `java.base\java\util\stream\BaseStream.html`

### Class Description

```java
public interface
BaseStream<T,​S extends BaseStream<T,​S>>

extends
AutoCloseable
```

Base interface for streams, which are sequences of elements supporting
sequential and parallel aggregate operations. The following example
illustrates an aggregate operation using the stream types

Stream

and

IntStream

, computing the sum of the weights of the red widgets:

```java
int sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToInt(w -> w.getWeight())
.sum();
```

See the class documentation for

Stream

and the package documentation
for

java.util.stream

for additional
specification of streams, stream operations, stream pipelines, and
parallelism, which governs the behavior of all stream types.

**Type Parameters:** T

- the type of the stream elements
**Type Parameters:** S

- the type of the stream implementing

BaseStream

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

Returns an iterator for the elements of this stream.

This is a

terminal
operation

.

**Returns:**
- the element iterator for this stream

---

#### Spliterator
<
T
> spliterator()

Returns a spliterator for the elements of this stream.

This is a

terminal
operation

.

The returned spliterator should report the set of characteristics derived
from the stream pipeline (namely the characteristics derived from the
stream source spliterator and the intermediate operations).
Implementations may report a sub-set of those characteristics. For
example, it may be too expensive to compute the entire set for some or
all possible stream pipelines.

**Returns:**
- the element spliterator for this stream

---

#### boolean isParallel()

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel. Calling this method after invoking an
terminal stream operation method may yield unpredictable results.

**Returns:**
- true

if this stream would execute in parallel if executed

---

#### S
sequential()

Returns an equivalent stream that is sequential. May return
itself, either because the stream was already sequential, or because
the underlying stream state was modified to be sequential.

This is an

intermediate
operation

.

**Returns:**
- a sequential stream

---

#### S
parallel()

Returns an equivalent stream that is parallel. May return
itself, either because the stream was already parallel, or because
the underlying stream state was modified to be parallel.

This is an

intermediate
operation

.

**Returns:**
- a parallel stream

---

#### S
unordered()

Returns an equivalent stream that is

unordered

. May return
itself, either because the stream was already unordered, or because
the underlying stream state was modified to be unordered.

This is an

intermediate
operation

.

**Returns:**
- an unordered stream

---

#### S
onClose​(
Runnable
closeHandler)

Returns an equivalent stream with an additional close handler. Close
handlers are run when the

close()

method
is called on the stream, and are executed in the order they were
added. All close handlers are run, even if earlier close handlers throw
exceptions. If any close handler throws an exception, the first
exception thrown will be relayed to the caller of

close()

, with
any remaining exceptions added to that exception as suppressed exceptions
(unless one of the remaining exceptions is the same exception as the
first exception, since an exception cannot suppress itself.) May
return itself.

This is an

intermediate
operation

.

**Parameters:**
- closeHandler

- A task to execute when the stream is closed

**Returns:**
- a stream with a handler that is run if the stream is closed

---

#### void close()

Closes this stream, causing all close handlers for this stream pipeline
to be called.

**Specified by:**
- close

in interface

AutoCloseable

**See Also:**
- AutoCloseable.close()

---

### Additional Sections

#### Interface BaseStream<T,​S extends BaseStream<T,​S>>

**Type Parameters:** T

- the type of the stream elements
**Type Parameters:** S

- the type of the stream implementing

BaseStream

**All Superinterfaces:** AutoCloseable

**All Known Subinterfaces:** DoubleStream

,

IntStream

,

LongStream

,

Stream

<T>

```java
public interface
BaseStream<T,​S extends BaseStream<T,​S>>

extends
AutoCloseable
```

Base interface for streams, which are sequences of elements supporting
sequential and parallel aggregate operations. The following example
illustrates an aggregate operation using the stream types

Stream

and

IntStream

, computing the sum of the weights of the red widgets:

```java
int sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToInt(w -> w.getWeight())
.sum();
```

See the class documentation for

Stream

and the package documentation
for

java.util.stream

for additional
specification of streams, stream operations, stream pipelines, and
parallelism, which governs the behavior of all stream types.

**Since:** 1.8
**See Also:** Stream

,

IntStream

,

LongStream

,

DoubleStream

,

java.util.stream

public interface

BaseStream<T,​S extends BaseStream<T,​S>>

extends

AutoCloseable

Base interface for streams, which are sequences of elements supporting
sequential and parallel aggregate operations. The following example
illustrates an aggregate operation using the stream types

Stream

and

IntStream

, computing the sum of the weights of the red widgets:

```java
int sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToInt(w -> w.getWeight())
.sum();
```

See the class documentation for

Stream

and the package documentation
for

java.util.stream

for additional
specification of streams, stream operations, stream pipelines, and
parallelism, which governs the behavior of all stream types.

int sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToInt(w -> w.getWeight())
.sum();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes this stream, causing all close handlers for this stream pipeline
to be called.

boolean

isParallel

()

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel.

Iterator

<

T

>

iterator

()

Returns an iterator for the elements of this stream.

S

onClose

​(

Runnable

closeHandler)

Returns an equivalent stream with an additional close handler.

S

parallel

()

Returns an equivalent stream that is parallel.

S

sequential

()

Returns an equivalent stream that is sequential.

Spliterator

<

T

>

spliterator

()

Returns a spliterator for the elements of this stream.

S

unordered

()

Returns an equivalent stream that is

unordered

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes this stream, causing all close handlers for this stream pipeline
to be called.

boolean

isParallel

()

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel.

Iterator

<

T

>

iterator

()

Returns an iterator for the elements of this stream.

S

onClose

​(

Runnable

closeHandler)

Returns an equivalent stream with an additional close handler.

S

parallel

()

Returns an equivalent stream that is parallel.

S

sequential

()

Returns an equivalent stream that is sequential.

Spliterator

<

T

>

spliterator

()

Returns a spliterator for the elements of this stream.

S

unordered

()

Returns an equivalent stream that is

unordered

.

---

#### Method Summary

Closes this stream, causing all close handlers for this stream pipeline
to be called.

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel.

Returns an iterator for the elements of this stream.

Returns an equivalent stream with an additional close handler.

Returns an equivalent stream that is parallel.

Returns an equivalent stream that is sequential.

Returns a spliterator for the elements of this stream.

Returns an equivalent stream that is

unordered

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

Returns an iterator for the elements of this stream.

This is a

terminal
operation

.

**Returns:** the element iterator for this stream

- spliterator

```java
Spliterator
<
T
> spliterator()
```

Returns a spliterator for the elements of this stream.

This is a

terminal
operation

.

The returned spliterator should report the set of characteristics derived
from the stream pipeline (namely the characteristics derived from the
stream source spliterator and the intermediate operations).
Implementations may report a sub-set of those characteristics. For
example, it may be too expensive to compute the entire set for some or
all possible stream pipelines.

**Returns:** the element spliterator for this stream

- isParallel

```java
boolean isParallel()
```

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel. Calling this method after invoking an
terminal stream operation method may yield unpredictable results.

**Returns:** true

if this stream would execute in parallel if executed

- sequential

```java
S
sequential()
```

Returns an equivalent stream that is sequential. May return
itself, either because the stream was already sequential, or because
the underlying stream state was modified to be sequential.

This is an

intermediate
operation

.

**Returns:** a sequential stream

- parallel

```java
S
parallel()
```

Returns an equivalent stream that is parallel. May return
itself, either because the stream was already parallel, or because
the underlying stream state was modified to be parallel.

This is an

intermediate
operation

.

**Returns:** a parallel stream

- unordered

```java
S
unordered()
```

Returns an equivalent stream that is

unordered

. May return
itself, either because the stream was already unordered, or because
the underlying stream state was modified to be unordered.

This is an

intermediate
operation

.

**Returns:** an unordered stream

- onClose

```java
S
onClose​(
Runnable
closeHandler)
```

Returns an equivalent stream with an additional close handler. Close
handlers are run when the

close()

method
is called on the stream, and are executed in the order they were
added. All close handlers are run, even if earlier close handlers throw
exceptions. If any close handler throws an exception, the first
exception thrown will be relayed to the caller of

close()

, with
any remaining exceptions added to that exception as suppressed exceptions
(unless one of the remaining exceptions is the same exception as the
first exception, since an exception cannot suppress itself.) May
return itself.

This is an

intermediate
operation

.

**Parameters:** closeHandler

- A task to execute when the stream is closed
**Returns:** a stream with a handler that is run if the stream is closed

- close

```java
void close()
```

Closes this stream, causing all close handlers for this stream pipeline
to be called.

**Specified by:** close

in interface

AutoCloseable
**See Also:** AutoCloseable.close()

Method Detail

- iterator

```java
Iterator
<
T
> iterator()
```

Returns an iterator for the elements of this stream.

This is a

terminal
operation

.

**Returns:** the element iterator for this stream

- spliterator

```java
Spliterator
<
T
> spliterator()
```

Returns a spliterator for the elements of this stream.

This is a

terminal
operation

.

The returned spliterator should report the set of characteristics derived
from the stream pipeline (namely the characteristics derived from the
stream source spliterator and the intermediate operations).
Implementations may report a sub-set of those characteristics. For
example, it may be too expensive to compute the entire set for some or
all possible stream pipelines.

**Returns:** the element spliterator for this stream

- isParallel

```java
boolean isParallel()
```

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel. Calling this method after invoking an
terminal stream operation method may yield unpredictable results.

**Returns:** true

if this stream would execute in parallel if executed

- sequential

```java
S
sequential()
```

Returns an equivalent stream that is sequential. May return
itself, either because the stream was already sequential, or because
the underlying stream state was modified to be sequential.

This is an

intermediate
operation

.

**Returns:** a sequential stream

- parallel

```java
S
parallel()
```

Returns an equivalent stream that is parallel. May return
itself, either because the stream was already parallel, or because
the underlying stream state was modified to be parallel.

This is an

intermediate
operation

.

**Returns:** a parallel stream

- unordered

```java
S
unordered()
```

Returns an equivalent stream that is

unordered

. May return
itself, either because the stream was already unordered, or because
the underlying stream state was modified to be unordered.

This is an

intermediate
operation

.

**Returns:** an unordered stream

- onClose

```java
S
onClose​(
Runnable
closeHandler)
```

Returns an equivalent stream with an additional close handler. Close
handlers are run when the

close()

method
is called on the stream, and are executed in the order they were
added. All close handlers are run, even if earlier close handlers throw
exceptions. If any close handler throws an exception, the first
exception thrown will be relayed to the caller of

close()

, with
any remaining exceptions added to that exception as suppressed exceptions
(unless one of the remaining exceptions is the same exception as the
first exception, since an exception cannot suppress itself.) May
return itself.

This is an

intermediate
operation

.

**Parameters:** closeHandler

- A task to execute when the stream is closed
**Returns:** a stream with a handler that is run if the stream is closed

- close

```java
void close()
```

Closes this stream, causing all close handlers for this stream pipeline
to be called.

**Specified by:** close

in interface

AutoCloseable
**See Also:** AutoCloseable.close()

---

#### Method Detail

iterator

```java
Iterator
<
T
> iterator()
```

Returns an iterator for the elements of this stream.

This is a

terminal
operation

.

**Returns:** the element iterator for this stream

---

#### iterator

Iterator

<

T

> iterator()

Returns an iterator for the elements of this stream.

This is a

terminal
operation

.

This is a

terminal
operation

.

spliterator

```java
Spliterator
<
T
> spliterator()
```

Returns a spliterator for the elements of this stream.

This is a

terminal
operation

.

The returned spliterator should report the set of characteristics derived
from the stream pipeline (namely the characteristics derived from the
stream source spliterator and the intermediate operations).
Implementations may report a sub-set of those characteristics. For
example, it may be too expensive to compute the entire set for some or
all possible stream pipelines.

**Returns:** the element spliterator for this stream

---

#### spliterator

Spliterator

<

T

> spliterator()

Returns a spliterator for the elements of this stream.

This is a

terminal
operation

.

The returned spliterator should report the set of characteristics derived
from the stream pipeline (namely the characteristics derived from the
stream source spliterator and the intermediate operations).
Implementations may report a sub-set of those characteristics. For
example, it may be too expensive to compute the entire set for some or
all possible stream pipelines.

This is a

terminal
operation

.

The returned spliterator should report the set of characteristics derived
from the stream pipeline (namely the characteristics derived from the
stream source spliterator and the intermediate operations).
Implementations may report a sub-set of those characteristics. For
example, it may be too expensive to compute the entire set for some or
all possible stream pipelines.

The returned spliterator should report the set of characteristics derived
from the stream pipeline (namely the characteristics derived from the
stream source spliterator and the intermediate operations).
Implementations may report a sub-set of those characteristics. For
example, it may be too expensive to compute the entire set for some or
all possible stream pipelines.

isParallel

```java
boolean isParallel()
```

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel. Calling this method after invoking an
terminal stream operation method may yield unpredictable results.

**Returns:** true

if this stream would execute in parallel if executed

---

#### isParallel

boolean isParallel()

Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel. Calling this method after invoking an
terminal stream operation method may yield unpredictable results.

sequential

```java
S
sequential()
```

Returns an equivalent stream that is sequential. May return
itself, either because the stream was already sequential, or because
the underlying stream state was modified to be sequential.

This is an

intermediate
operation

.

**Returns:** a sequential stream

---

#### sequential

S

sequential()

Returns an equivalent stream that is sequential. May return
itself, either because the stream was already sequential, or because
the underlying stream state was modified to be sequential.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

parallel

```java
S
parallel()
```

Returns an equivalent stream that is parallel. May return
itself, either because the stream was already parallel, or because
the underlying stream state was modified to be parallel.

This is an

intermediate
operation

.

**Returns:** a parallel stream

---

#### parallel

S

parallel()

Returns an equivalent stream that is parallel. May return
itself, either because the stream was already parallel, or because
the underlying stream state was modified to be parallel.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

unordered

```java
S
unordered()
```

Returns an equivalent stream that is

unordered

. May return
itself, either because the stream was already unordered, or because
the underlying stream state was modified to be unordered.

This is an

intermediate
operation

.

**Returns:** an unordered stream

---

#### unordered

S

unordered()

Returns an equivalent stream that is

unordered

. May return
itself, either because the stream was already unordered, or because
the underlying stream state was modified to be unordered.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

onClose

```java
S
onClose​(
Runnable
closeHandler)
```

Returns an equivalent stream with an additional close handler. Close
handlers are run when the

close()

method
is called on the stream, and are executed in the order they were
added. All close handlers are run, even if earlier close handlers throw
exceptions. If any close handler throws an exception, the first
exception thrown will be relayed to the caller of

close()

, with
any remaining exceptions added to that exception as suppressed exceptions
(unless one of the remaining exceptions is the same exception as the
first exception, since an exception cannot suppress itself.) May
return itself.

This is an

intermediate
operation

.

**Parameters:** closeHandler

- A task to execute when the stream is closed
**Returns:** a stream with a handler that is run if the stream is closed

---

#### onClose

S

onClose​(

Runnable

closeHandler)

Returns an equivalent stream with an additional close handler. Close
handlers are run when the

close()

method
is called on the stream, and are executed in the order they were
added. All close handlers are run, even if earlier close handlers throw
exceptions. If any close handler throws an exception, the first
exception thrown will be relayed to the caller of

close()

, with
any remaining exceptions added to that exception as suppressed exceptions
(unless one of the remaining exceptions is the same exception as the
first exception, since an exception cannot suppress itself.) May
return itself.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

close

```java
void close()
```

Closes this stream, causing all close handlers for this stream pipeline
to be called.

**Specified by:** close

in interface

AutoCloseable
**See Also:** AutoCloseable.close()

---

#### close

void close()

Closes this stream, causing all close handlers for this stream pipeline
to be called.

---

