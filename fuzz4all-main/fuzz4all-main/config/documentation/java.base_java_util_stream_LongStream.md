# Interface LongStream

**Source:** `java.base\java\util\stream\LongStream.html`

### Class Description

```java
public interface
LongStream

extends
BaseStream
<
Long
,​
LongStream
>
```

A sequence of primitive long-valued elements supporting sequential and parallel
aggregate operations. This is the

long

primitive specialization of

Stream

.

The following example illustrates an aggregate operation using

Stream

and

LongStream

, computing the sum of the weights of the
red widgets:

```java
long sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToLong(w -> w.getWeight())
.sum();
```

See the class documentation for

Stream

and the package documentation
for

java.util.stream

for additional
specification of streams, stream operations, stream pipelines, and
parallelism.

**All Superinterfaces:** AutoCloseable

,

BaseStream

<

Long

,​

LongStream

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### LongStream
filter​(
LongPredicate
predicate)

Returns a stream consisting of the elements of this stream that match
the given predicate.

This is an

intermediate
operation

.

**Parameters:**
- predicate

- a

non-interfering

,

stateless

predicate to apply to each element to determine if it
should be included

**Returns:**
- the new stream

---

#### LongStream
map​(
LongUnaryOperator
mapper)

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:**
- mapper

- a

non-interfering

,

stateless

function to apply to each element

**Returns:**
- the new stream

---

#### <U>
Stream
<U> mapToObj​(
LongFunction
<? extends U> mapper)

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

This is an

intermediate operation

.

**Parameters:**
- mapper

- a

non-interfering

,

stateless

function to apply to each element

**Returns:**
- the new stream

**Type Parameters:**
- U

- the element type of the new stream

---

#### IntStream
mapToInt​(
LongToIntFunction
mapper)

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:**
- mapper

- a

non-interfering

,

stateless

function to apply to each element

**Returns:**
- the new stream

---

#### DoubleStream
mapToDouble​(
LongToDoubleFunction
mapper)

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:**
- mapper

- a

non-interfering

,

stateless

function to apply to each element

**Returns:**
- the new stream

---

#### LongStream
flatMap​(
LongFunction
<? extends
LongStream
> mapper)

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element. Each mapped stream is

closed

after its contents
have been placed into this stream. (If a mapped stream is

null

an empty stream is used, instead.)

This is an

intermediate
operation

.

**Parameters:**
- mapper

- a

non-interfering

,

stateless

function to apply to each element which produces a

LongStream

of new values

**Returns:**
- the new stream

**See Also:**
- Stream.flatMap(Function)

---

#### LongStream
distinct()

Returns a stream consisting of the distinct elements of this stream.

This is a

stateful
intermediate operation

.

**Returns:**
- the new stream

---

#### LongStream
sorted()

Returns a stream consisting of the elements of this stream in sorted
order.

This is a

stateful
intermediate operation

.

**Returns:**
- the new stream

---

#### LongStream
peek​(
LongConsumer
action)

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

This is an

intermediate
operation

.

For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.

**Parameters:**
- action

- a

non-interfering

action to perform on the elements as
they are consumed from the stream

**Returns:**
- the new stream

**API Note:**
- This method exists mainly to support debugging, where you want
to see the elements as they flow past a certain point in a pipeline:

```java
LongStream.of(1, 2, 3, 4)
.filter(e -> e > 2)
.peek(e -> System.out.println("Filtered value: " + e))
.map(e -> e * e)
.peek(e -> System.out.println("Mapped value: " + e))
.sum();
```

In cases where the stream implementation is able to optimize away the
production of some or all the elements (such as with short-circuiting
operations like

findFirst

, or in the example described in

count()

), the action will not be invoked for those elements.

---

#### LongStream
limit​(long maxSize)

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

This is a

short-circuiting
stateful intermediate operation

.

**Parameters:**
- maxSize

- the number of elements the stream should be limited to

**Returns:**
- the new stream

**Throws:**
- IllegalArgumentException

- if

maxSize

is negative

**API Note:**
- While

limit()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

maxSize

, since

limit(n)

is constrained to return not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

limit()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

limit()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.

---

#### LongStream
skip​(long n)

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.
If this stream contains fewer than

n

elements then an
empty stream will be returned.

This is a

stateful
intermediate operation

.

**Parameters:**
- n

- the number of leading elements to skip

**Returns:**
- the new stream

**Throws:**
- IllegalArgumentException

- if

n

is negative

**API Note:**
- While

skip()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

n

, since

skip(n)

is constrained to skip not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

skip()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

skip()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.

---

#### default
LongStream
takeWhile​(
LongPredicate
predicate)

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.
Otherwise returns, if this stream is unordered, a stream consisting of a
subset of elements taken from this stream that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to take any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

**Parameters:**
- predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.

**Returns:**
- the new stream

**Since:**
- 9

**API Note:**
- While

takeWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

takeWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

takeWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.

**Implementation Requirements:**
- The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.

---

#### default
LongStream
dropWhile​(
LongPredicate
predicate)

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate. Otherwise returns, if this stream is
unordered, a stream consisting of the remaining elements of this stream
after dropping a subset of elements that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to drop any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

**Parameters:**
- predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.

**Returns:**
- the new stream

**Since:**
- 9

**API Note:**
- While

dropWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

dropWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

dropWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.

**Implementation Requirements:**
- The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.

---

#### void forEach​(
LongConsumer
action)

Performs an action for each element of this stream.

This is a

terminal
operation

.

For parallel stream pipelines, this operation does

not

guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.

**Parameters:**
- action

- a

non-interfering

action to perform on the elements

---

#### void forEachOrdered​(
LongConsumer
action)

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

This is a

terminal
operation

.

**Parameters:**
- action

- a

non-interfering

action to perform on the elements

**See Also:**
- forEach(LongConsumer)

---

#### long[] toArray()

Returns an array containing the elements of this stream.

This is a

terminal
operation

.

**Returns:**
- an array containing the elements of this stream

---

#### long reduce​(long identity,

LongBinaryOperator
op)

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value. This is equivalent
to:

```java
long result = identity;
for (long element : this stream)
result = accumulator.applyAsLong(result, element)
return result;
```

but is not constrained to execute sequentially.

The

identity

value must be an identity for the accumulator
function. This means that for all

x

,

accumulator.apply(identity, x)

is equal to

x

.
The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**Parameters:**
- identity

- the identity value for the accumulating function
- op

- an

associative

,

non-interfering

,

stateless

function for combining two values

**Returns:**
- the result of the reduction

**See Also:**
- sum()

,

min()

,

max()

,

average()

**API Note:**
- Sum, min, max, and average are all special cases of reduction.
Summing a stream of numbers can be expressed as:

```java
long sum = integers.reduce(0, (a, b) -> a+b);
```

or more compactly:

```java
long sum = integers.reduce(0, Long::sum);
```

While this may seem a more roundabout way to perform an aggregation
compared to simply mutating a running total in a loop, reduction
operations parallelize more gracefully, without needing additional
synchronization and with greatly reduced risk of data races.

---

#### OptionalLong
reduce​(
LongBinaryOperator
op)

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any. This is equivalent to:

```java
boolean foundAny = false;
long result = null;
for (long element : this stream) {
if (!foundAny) {
foundAny = true;
result = element;
}
else
result = accumulator.applyAsLong(result, element);
}
return foundAny ? OptionalLong.of(result) : OptionalLong.empty();
```

but is not constrained to execute sequentially.

The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**Parameters:**
- op

- an

associative

,

non-interfering

,

stateless

function for combining two values

**Returns:**
- the result of the reduction

**See Also:**
- reduce(long, LongBinaryOperator)

---

#### <R> R collect​(
Supplier
<R> supplier,

ObjLongConsumer
<R> accumulator,

BiConsumer
<R,​R> combiner)

Performs a

mutable
reduction

operation on the elements of this stream. A mutable
reduction is one in which the reduced value is a mutable result container,
such as an

ArrayList

, and elements are incorporated by updating
the state of the result rather than by replacing the result. This
produces a result equivalent to:

```java
R result = supplier.get();
for (long element : this stream)
accumulator.accept(result, element);
return result;
```

Like

reduce(long, LongBinaryOperator)

,

collect

operations
can be parallelized without requiring additional synchronization.

This is a

terminal
operation

.

**Parameters:**
- supplier

- a function that creates a new mutable result container.
For a parallel execution, this function may be called
multiple times and must return a fresh value each time.
- accumulator

- an

associative

,

non-interfering

,

stateless

function that must fold an element into a result
container.
- combiner

- an

associative

,

non-interfering

,

stateless

function that accepts two partial result containers
and merges them, which must be compatible with the
accumulator function. The combiner function must fold
the elements from the second result container into the
first result container.

**Returns:**
- the result of the reduction

**See Also:**
- Stream.collect(Supplier, BiConsumer, BiConsumer)

**Type Parameters:**
- R

- the type of the mutable result container

---

#### long sum()

Returns the sum of elements in this stream. This is a special case
of a

reduction

and is equivalent to:

```java
return reduce(0, Long::sum);
```

This is a

terminal
operation

.

**Returns:**
- the sum of elements in this stream

---

#### OptionalLong
min()

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::min);
```

This is a

terminal operation

.

**Returns:**
- an

OptionalLong

containing the minimum element of this
stream, or an empty

OptionalLong

if the stream is empty

---

#### OptionalLong
max()

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::max);
```

This is a

terminal
operation

.

**Returns:**
- an

OptionalLong

containing the maximum element of this
stream, or an empty

OptionalLong

if the stream is empty

---

#### long count()

Returns the count of elements in this stream. This is a special case of
a

reduction

and is
equivalent to:

```java
return map(e -> 1L).sum();
```

This is a

terminal operation

.

**Returns:**
- the count of elements in this stream

**API Note:**
- An implementation may choose to not execute the stream pipeline (either
sequentially or in parallel) if it is capable of computing the count
directly from the stream source. In such cases no source elements will
be traversed and no intermediate operations will be evaluated.
Behavioral parameters with side-effects, which are strongly discouraged
except for harmless cases such as debugging, may be affected. For
example, consider the following stream:

```java
LongStream s = LongStream.of(1, 2, 3, 4);
long count = s.peek(System.out::println).count();
```

The number of elements covered by the stream source is known and the
intermediate operation,

peek

, does not inject into or remove
elements from the stream (as may be the case for

flatMap

or

filter

operations). Thus the count is 4 and there is no need to
execute the pipeline and, as a side-effect, print out the elements.

---

#### OptionalDouble
average()

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty. This is a
special case of a

reduction

.

This is a

terminal
operation

.

**Returns:**
- an

OptionalDouble

containing the average element of this
stream, or an empty optional if the stream is empty

---

#### LongSummaryStatistics
summaryStatistics()

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream. This is a special case of a

reduction

.

This is a

terminal
operation

.

**Returns:**
- a

LongSummaryStatistics

describing various summary data
about the elements of this stream

---

#### boolean anyMatch​(
LongPredicate
predicate)

Returns whether any elements of this stream match the provided
predicate. May not evaluate the predicate on all elements if not
necessary for determining the result. If the stream is empty then

false

is returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**Parameters:**
- predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream

**Returns:**
- true

if any elements of the stream match the provided
predicate, otherwise

false

**API Note:**
- This method evaluates the

existential quantification

of the
predicate over the elements of the stream (for some x P(x)).

---

#### boolean allMatch​(
LongPredicate
predicate)

Returns whether all elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**Parameters:**
- predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream

**Returns:**
- true

if either all elements of the stream match the
provided predicate or the stream is empty, otherwise

false

**API Note:**
- This method evaluates the

universal quantification

of the
predicate over the elements of the stream (for all x P(x)). If the
stream is empty, the quantification is said to be

vacuously
satisfied

and is always

true

(regardless of P(x)).

---

#### boolean noneMatch​(
LongPredicate
predicate)

Returns whether no elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**Parameters:**
- predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream

**Returns:**
- true

if either no elements of the stream match the
provided predicate or the stream is empty, otherwise

false

**API Note:**
- This method evaluates the

universal quantification

of the
negated predicate over the elements of the stream (for all x ~P(x)). If
the stream is empty, the quantification is said to be vacuously satisfied
and is always

true

, regardless of P(x).

---

#### OptionalLong
findFirst()

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty. If the
stream has no encounter order, then any element may be returned.

This is a

short-circuiting
terminal operation

.

**Returns:**
- an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty

---

#### OptionalLong
findAny()

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

This is a

short-circuiting
terminal operation

.

The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use

findFirst()

instead.)

**Returns:**
- an

OptionalLong

describing some element of this stream,
or an empty

OptionalLong

if the stream is empty

**See Also:**
- findFirst()

---

#### DoubleStream
asDoubleStream()

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

This is an

intermediate
operation

.

**Returns:**
- a

DoubleStream

consisting of the elements of this stream,
converted to

double

---

#### Stream
<
Long
> boxed()

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

This is an

intermediate
operation

.

**Returns:**
- a

Stream

consistent of the elements of this stream,
each boxed to

Long

---

#### static
LongStream.Builder
builder()

Returns a builder for a

LongStream

.

**Returns:**
- a stream builder

---

#### static
LongStream
empty()

Returns an empty sequential

LongStream

.

**Returns:**
- an empty sequential stream

---

#### static
LongStream
of​(long t)

Returns a sequential

LongStream

containing a single element.

**Parameters:**
- t

- the single element

**Returns:**
- a singleton sequential stream

---

#### static
LongStream
of​(long... values)

Returns a sequential ordered stream whose elements are the specified values.

**Parameters:**
- values

- the elements of the new stream

**Returns:**
- the new stream

---

#### static
LongStream
iterate​(long seed,

LongUnaryOperator
f)

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

The first element (position

0

) in the

LongStream

will
be the provided

seed

. For

n > 0

, the element at position

n

, will be the result of applying the function

f

to the
element at position

n - 1

.

The action of applying

f

for one element

happens-before

the action of applying

f

for subsequent elements. For any given
element the action may be performed in whatever thread the library
chooses.

**Parameters:**
- seed

- the initial element
- f

- a function to be applied to the previous element to produce
a new element

**Returns:**
- a new sequential

LongStream

---

#### static
LongStream
iterate​(long seed,

LongPredicate
hasNext,

LongUnaryOperator
next)

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate. The
stream terminates as soon as the

hasNext

predicate returns false.

LongStream.iterate

should produce the same sequence of elements as
produced by the corresponding for-loop:

```java
for (long index=seed; hasNext.test(index); index = next.applyAsLong(index)) {
...
}
```

The resulting sequence may be empty if the

hasNext

predicate
does not hold on the seed value. Otherwise the first element will be the
supplied

seed

value, the next element (if present) will be the
result of applying the

next

function to the

seed

value,
and so on iteratively until the

hasNext

predicate indicates that
the stream should terminate.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

**Parameters:**
- seed

- the initial element
- hasNext

- a predicate to apply to elements to determine when the
stream must terminate.
- next

- a function to be applied to the previous element to produce
a new element

**Returns:**
- a new sequential

LongStream

**Since:**
- 9

---

#### static
LongStream
generate​(
LongSupplier
s)

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

. This is suitable for
generating constant streams, streams of random elements, etc.

**Parameters:**
- s

- the

LongSupplier

for generated elements

**Returns:**
- a new infinite sequential unordered

LongStream

---

#### static
LongStream
range​(long startInclusive,
long endExclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

**Parameters:**
- startInclusive

- the (inclusive) initial value
- endExclusive

- the exclusive upper bound

**Returns:**
- a sequential

LongStream

for the range of

long

elements

**API Note:**
- An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i < endExclusive ; i++) { ... }
```

---

#### static
LongStream
rangeClosed​(long startInclusive,
long endInclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

**Parameters:**
- startInclusive

- the (inclusive) initial value
- endInclusive

- the inclusive upper bound

**Returns:**
- a sequential

LongStream

for the range of

long

elements

**API Note:**
- An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i <= endInclusive ; i++) { ... }
```

---

#### static
LongStream
concat​(
LongStream
a,

LongStream
b)

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream. The resulting stream is ordered if both
of the input streams are ordered, and parallel if either of the input
streams is parallel. When the resulting stream is closed, the close
handlers for both input streams are invoked.

This method operates on the two input streams and binds each stream
to its source. As a result subsequent modifications to an input stream
source may not be reflected in the concatenated stream result.

**Parameters:**
- a

- the first stream
- b

- the second stream

**Returns:**
- the concatenation of the two input streams

**API Note:**
- To preserve optimization opportunities this method binds each stream to
its source and accepts only two streams as parameters. For example, the
exact size of the concatenated stream source can be computed if the exact
size of each input stream source is known.
To concatenate more streams without binding, or without nested calls to
this method, try creating a stream of streams and flat-mapping with the
identity function, for example:

```java
LongStream concat = Stream.of(s1, s2, s3, s4).flatMapToLong(s -> s);
```

**Implementation Note:**
- Use caution when constructing streams from repeated concatenation.
Accessing an element of a deeply concatenated stream can result in deep
call chains, or even

StackOverflowError

.

---

### Additional Sections

#### Interface LongStream

**All Superinterfaces:** AutoCloseable

,

BaseStream

<

Long

,​

LongStream

>

```java
public interface
LongStream

extends
BaseStream
<
Long
,​
LongStream
>
```

A sequence of primitive long-valued elements supporting sequential and parallel
aggregate operations. This is the

long

primitive specialization of

Stream

.

The following example illustrates an aggregate operation using

Stream

and

LongStream

, computing the sum of the weights of the
red widgets:

```java
long sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToLong(w -> w.getWeight())
.sum();
```

See the class documentation for

Stream

and the package documentation
for

java.util.stream

for additional
specification of streams, stream operations, stream pipelines, and
parallelism.

**Since:** 1.8
**See Also:** Stream

,

java.util.stream

public interface

LongStream

extends

BaseStream

<

Long

,​

LongStream

>

A sequence of primitive long-valued elements supporting sequential and parallel
aggregate operations. This is the

long

primitive specialization of

Stream

.

The following example illustrates an aggregate operation using

Stream

and

LongStream

, computing the sum of the weights of the
red widgets:

```java
long sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToLong(w -> w.getWeight())
.sum();
```

See the class documentation for

Stream

and the package documentation
for

java.util.stream

for additional
specification of streams, stream operations, stream pipelines, and
parallelism.

The following example illustrates an aggregate operation using

Stream

and

LongStream

, computing the sum of the weights of the
red widgets:

```java
long sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToLong(w -> w.getWeight())
.sum();
```

See the class documentation for

Stream

and the package documentation
for

java.util.stream

for additional
specification of streams, stream operations, stream pipelines, and
parallelism.

long sum = widgets.stream()
.filter(w -> w.getColor() == RED)
.mapToLong(w -> w.getWeight())
.sum();

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

LongStream.Builder

A mutable builder for a

LongStream

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

boolean

allMatch

​(

LongPredicate

predicate)

Returns whether all elements of this stream match the provided predicate.

boolean

anyMatch

​(

LongPredicate

predicate)

Returns whether any elements of this stream match the provided
predicate.

DoubleStream

asDoubleStream

()

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

OptionalDouble

average

()

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty.

Stream

<

Long

>

boxed

()

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

static

LongStream.Builder

builder

()

Returns a builder for a

LongStream

.

<R> R

collect

​(

Supplier

<R> supplier,

ObjLongConsumer

<R> accumulator,

BiConsumer

<R,​R> combiner)

Performs a

mutable
reduction

operation on the elements of this stream.

static

LongStream

concat

​(

LongStream

a,

LongStream

b)

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream.

long

count

()

Returns the count of elements in this stream.

LongStream

distinct

()

Returns a stream consisting of the distinct elements of this stream.

default

LongStream

dropWhile

​(

LongPredicate

predicate)

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate.

static

LongStream

empty

()

Returns an empty sequential

LongStream

.

LongStream

filter

​(

LongPredicate

predicate)

Returns a stream consisting of the elements of this stream that match
the given predicate.

OptionalLong

findAny

()

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

OptionalLong

findFirst

()

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty.

LongStream

flatMap

​(

LongFunction

<? extends

LongStream

> mapper)

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element.

void

forEach

​(

LongConsumer

action)

Performs an action for each element of this stream.

void

forEachOrdered

​(

LongConsumer

action)

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

static

LongStream

generate

​(

LongSupplier

s)

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

.

static

LongStream

iterate

​(long seed,

LongPredicate

hasNext,

LongUnaryOperator

next)

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate.

static

LongStream

iterate

​(long seed,

LongUnaryOperator

f)

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

LongStream

limit

​(long maxSize)

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

LongStream

map

​(

LongUnaryOperator

mapper)

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

DoubleStream

mapToDouble

​(

LongToDoubleFunction

mapper)

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

IntStream

mapToInt

​(

LongToIntFunction

mapper)

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

<U>

Stream

<U>

mapToObj

​(

LongFunction

<? extends U> mapper)

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

OptionalLong

max

()

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty.

OptionalLong

min

()

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty.

boolean

noneMatch

​(

LongPredicate

predicate)

Returns whether no elements of this stream match the provided predicate.

static

LongStream

of

​(long t)

Returns a sequential

LongStream

containing a single element.

static

LongStream

of

​(long... values)

Returns a sequential ordered stream whose elements are the specified values.

LongStream

peek

​(

LongConsumer

action)

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

static

LongStream

range

​(long startInclusive,
long endExclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

static

LongStream

rangeClosed

​(long startInclusive,
long endInclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

long

reduce

​(long identity,

LongBinaryOperator

op)

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value.

OptionalLong

reduce

​(

LongBinaryOperator

op)

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any.

LongStream

skip

​(long n)

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.

LongStream

sorted

()

Returns a stream consisting of the elements of this stream in sorted
order.

long

sum

()

Returns the sum of elements in this stream.

LongSummaryStatistics

summaryStatistics

()

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream.

default

LongStream

takeWhile

​(

LongPredicate

predicate)

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.

long[]

toArray

()

Returns an array containing the elements of this stream.

- Methods declared in interface java.util.stream.

BaseStream

close

,

isParallel

,

iterator

,

onClose

,

parallel

,

sequential

,

spliterator

,

unordered

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

LongStream.Builder

A mutable builder for a

LongStream

.

---

#### Nested Class Summary

A mutable builder for a

LongStream

.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

boolean

allMatch

​(

LongPredicate

predicate)

Returns whether all elements of this stream match the provided predicate.

boolean

anyMatch

​(

LongPredicate

predicate)

Returns whether any elements of this stream match the provided
predicate.

DoubleStream

asDoubleStream

()

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

OptionalDouble

average

()

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty.

Stream

<

Long

>

boxed

()

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

static

LongStream.Builder

builder

()

Returns a builder for a

LongStream

.

<R> R

collect

​(

Supplier

<R> supplier,

ObjLongConsumer

<R> accumulator,

BiConsumer

<R,​R> combiner)

Performs a

mutable
reduction

operation on the elements of this stream.

static

LongStream

concat

​(

LongStream

a,

LongStream

b)

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream.

long

count

()

Returns the count of elements in this stream.

LongStream

distinct

()

Returns a stream consisting of the distinct elements of this stream.

default

LongStream

dropWhile

​(

LongPredicate

predicate)

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate.

static

LongStream

empty

()

Returns an empty sequential

LongStream

.

LongStream

filter

​(

LongPredicate

predicate)

Returns a stream consisting of the elements of this stream that match
the given predicate.

OptionalLong

findAny

()

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

OptionalLong

findFirst

()

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty.

LongStream

flatMap

​(

LongFunction

<? extends

LongStream

> mapper)

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element.

void

forEach

​(

LongConsumer

action)

Performs an action for each element of this stream.

void

forEachOrdered

​(

LongConsumer

action)

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

static

LongStream

generate

​(

LongSupplier

s)

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

.

static

LongStream

iterate

​(long seed,

LongPredicate

hasNext,

LongUnaryOperator

next)

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate.

static

LongStream

iterate

​(long seed,

LongUnaryOperator

f)

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

LongStream

limit

​(long maxSize)

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

LongStream

map

​(

LongUnaryOperator

mapper)

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

DoubleStream

mapToDouble

​(

LongToDoubleFunction

mapper)

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

IntStream

mapToInt

​(

LongToIntFunction

mapper)

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

<U>

Stream

<U>

mapToObj

​(

LongFunction

<? extends U> mapper)

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

OptionalLong

max

()

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty.

OptionalLong

min

()

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty.

boolean

noneMatch

​(

LongPredicate

predicate)

Returns whether no elements of this stream match the provided predicate.

static

LongStream

of

​(long t)

Returns a sequential

LongStream

containing a single element.

static

LongStream

of

​(long... values)

Returns a sequential ordered stream whose elements are the specified values.

LongStream

peek

​(

LongConsumer

action)

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

static

LongStream

range

​(long startInclusive,
long endExclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

static

LongStream

rangeClosed

​(long startInclusive,
long endInclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

long

reduce

​(long identity,

LongBinaryOperator

op)

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value.

OptionalLong

reduce

​(

LongBinaryOperator

op)

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any.

LongStream

skip

​(long n)

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.

LongStream

sorted

()

Returns a stream consisting of the elements of this stream in sorted
order.

long

sum

()

Returns the sum of elements in this stream.

LongSummaryStatistics

summaryStatistics

()

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream.

default

LongStream

takeWhile

​(

LongPredicate

predicate)

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.

long[]

toArray

()

Returns an array containing the elements of this stream.

- Methods declared in interface java.util.stream.

BaseStream

close

,

isParallel

,

iterator

,

onClose

,

parallel

,

sequential

,

spliterator

,

unordered

---

#### Method Summary

Returns whether all elements of this stream match the provided predicate.

Returns whether any elements of this stream match the provided
predicate.

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty.

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

Returns a builder for a

LongStream

.

Performs a

mutable
reduction

operation on the elements of this stream.

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream.

Returns the count of elements in this stream.

Returns a stream consisting of the distinct elements of this stream.

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate.

Returns an empty sequential

LongStream

.

Returns a stream consisting of the elements of this stream that match
the given predicate.

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty.

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element.

Performs an action for each element of this stream.

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

.

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate.

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty.

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty.

Returns whether no elements of this stream match the provided predicate.

Returns a sequential

LongStream

containing a single element.

Returns a sequential ordered stream whose elements are the specified values.

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value.

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any.

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.

Returns a stream consisting of the elements of this stream in sorted
order.

Returns the sum of elements in this stream.

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream.

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.

Returns an array containing the elements of this stream.

Methods declared in interface java.util.stream.

BaseStream

close

,

isParallel

,

iterator

,

onClose

,

parallel

,

sequential

,

spliterator

,

unordered

---

#### Methods declared in interface java.util.stream. BaseStream

============ METHOD DETAIL ==========

- Method Detail

- filter

```java
LongStream
filter​(
LongPredicate
predicate)
```

Returns a stream consisting of the elements of this stream that match
the given predicate.

This is an

intermediate
operation

.

**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to each element to determine if it
should be included
**Returns:** the new stream

- map

```java
LongStream
map​(
LongUnaryOperator
mapper)
```

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- mapToObj

```java
<U>
Stream
<U> mapToObj​(
LongFunction
<? extends U> mapper)
```

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

This is an

intermediate operation

.

**Type Parameters:** U

- the element type of the new stream
**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- mapToInt

```java
IntStream
mapToInt​(
LongToIntFunction
mapper)
```

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- mapToDouble

```java
DoubleStream
mapToDouble​(
LongToDoubleFunction
mapper)
```

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- flatMap

```java
LongStream
flatMap​(
LongFunction
<? extends
LongStream
> mapper)
```

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element. Each mapped stream is

closed

after its contents
have been placed into this stream. (If a mapped stream is

null

an empty stream is used, instead.)

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element which produces a

LongStream

of new values
**Returns:** the new stream
**See Also:** Stream.flatMap(Function)

- distinct

```java
LongStream
distinct()
```

Returns a stream consisting of the distinct elements of this stream.

This is a

stateful
intermediate operation

.

**Returns:** the new stream

- sorted

```java
LongStream
sorted()
```

Returns a stream consisting of the elements of this stream in sorted
order.

This is a

stateful
intermediate operation

.

**Returns:** the new stream

- peek

```java
LongStream
peek​(
LongConsumer
action)
```

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

This is an

intermediate
operation

.

For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.

**API Note:** This method exists mainly to support debugging, where you want
to see the elements as they flow past a certain point in a pipeline:

```java
LongStream.of(1, 2, 3, 4)
.filter(e -> e > 2)
.peek(e -> System.out.println("Filtered value: " + e))
.map(e -> e * e)
.peek(e -> System.out.println("Mapped value: " + e))
.sum();
```

In cases where the stream implementation is able to optimize away the
production of some or all the elements (such as with short-circuiting
operations like

findFirst

, or in the example described in

count()

), the action will not be invoked for those elements.
**Parameters:** action

- a

non-interfering

action to perform on the elements as
they are consumed from the stream
**Returns:** the new stream

- limit

```java
LongStream
limit​(long maxSize)
```

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

This is a

short-circuiting
stateful intermediate operation

.

**API Note:** While

limit()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

maxSize

, since

limit(n)

is constrained to return not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

limit()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

limit()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.
**Parameters:** maxSize

- the number of elements the stream should be limited to
**Returns:** the new stream
**Throws:** IllegalArgumentException

- if

maxSize

is negative

- skip

```java
LongStream
skip​(long n)
```

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.
If this stream contains fewer than

n

elements then an
empty stream will be returned.

This is a

stateful
intermediate operation

.

**API Note:** While

skip()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

n

, since

skip(n)

is constrained to skip not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

skip()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

skip()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.
**Parameters:** n

- the number of leading elements to skip
**Returns:** the new stream
**Throws:** IllegalArgumentException

- if

n

is negative

- takeWhile

```java
default
LongStream
takeWhile​(
LongPredicate
predicate)
```

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.
Otherwise returns, if this stream is unordered, a stream consisting of a
subset of elements taken from this stream that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to take any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

**API Note:** While

takeWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

takeWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

takeWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.
**Implementation Requirements:** The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.
**Returns:** the new stream
**Since:** 9

- dropWhile

```java
default
LongStream
dropWhile​(
LongPredicate
predicate)
```

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate. Otherwise returns, if this stream is
unordered, a stream consisting of the remaining elements of this stream
after dropping a subset of elements that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to drop any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

**API Note:** While

dropWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

dropWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

dropWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.
**Implementation Requirements:** The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.
**Returns:** the new stream
**Since:** 9

- forEach

```java
void forEach​(
LongConsumer
action)
```

Performs an action for each element of this stream.

This is a

terminal
operation

.

For parallel stream pipelines, this operation does

not

guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.

**Parameters:** action

- a

non-interfering

action to perform on the elements

- forEachOrdered

```java
void forEachOrdered​(
LongConsumer
action)
```

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

This is a

terminal
operation

.

**Parameters:** action

- a

non-interfering

action to perform on the elements
**See Also:** forEach(LongConsumer)

- toArray

```java
long[] toArray()
```

Returns an array containing the elements of this stream.

This is a

terminal
operation

.

**Returns:** an array containing the elements of this stream

- reduce

```java
long reduce​(long identity,

LongBinaryOperator
op)
```

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value. This is equivalent
to:

```java
long result = identity;
for (long element : this stream)
result = accumulator.applyAsLong(result, element)
return result;
```

but is not constrained to execute sequentially.

The

identity

value must be an identity for the accumulator
function. This means that for all

x

,

accumulator.apply(identity, x)

is equal to

x

.
The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**API Note:** Sum, min, max, and average are all special cases of reduction.
Summing a stream of numbers can be expressed as:

```java
long sum = integers.reduce(0, (a, b) -> a+b);
```

or more compactly:

```java
long sum = integers.reduce(0, Long::sum);
```

While this may seem a more roundabout way to perform an aggregation
compared to simply mutating a running total in a loop, reduction
operations parallelize more gracefully, without needing additional
synchronization and with greatly reduced risk of data races.
**Parameters:** identity

- the identity value for the accumulating function
**Parameters:** op

- an

associative

,

non-interfering

,

stateless

function for combining two values
**Returns:** the result of the reduction
**See Also:** sum()

,

min()

,

max()

,

average()

- reduce

```java
OptionalLong
reduce​(
LongBinaryOperator
op)
```

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any. This is equivalent to:

```java
boolean foundAny = false;
long result = null;
for (long element : this stream) {
if (!foundAny) {
foundAny = true;
result = element;
}
else
result = accumulator.applyAsLong(result, element);
}
return foundAny ? OptionalLong.of(result) : OptionalLong.empty();
```

but is not constrained to execute sequentially.

The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**Parameters:** op

- an

associative

,

non-interfering

,

stateless

function for combining two values
**Returns:** the result of the reduction
**See Also:** reduce(long, LongBinaryOperator)

- collect

```java
<R> R collect​(
Supplier
<R> supplier,

ObjLongConsumer
<R> accumulator,

BiConsumer
<R,​R> combiner)
```

Performs a

mutable
reduction

operation on the elements of this stream. A mutable
reduction is one in which the reduced value is a mutable result container,
such as an

ArrayList

, and elements are incorporated by updating
the state of the result rather than by replacing the result. This
produces a result equivalent to:

```java
R result = supplier.get();
for (long element : this stream)
accumulator.accept(result, element);
return result;
```

Like

reduce(long, LongBinaryOperator)

,

collect

operations
can be parallelized without requiring additional synchronization.

This is a

terminal
operation

.

**Type Parameters:** R

- the type of the mutable result container
**Parameters:** supplier

- a function that creates a new mutable result container.
For a parallel execution, this function may be called
multiple times and must return a fresh value each time.
**Parameters:** accumulator

- an

associative

,

non-interfering

,

stateless

function that must fold an element into a result
container.
**Parameters:** combiner

- an

associative

,

non-interfering

,

stateless

function that accepts two partial result containers
and merges them, which must be compatible with the
accumulator function. The combiner function must fold
the elements from the second result container into the
first result container.
**Returns:** the result of the reduction
**See Also:** Stream.collect(Supplier, BiConsumer, BiConsumer)

- sum

```java
long sum()
```

Returns the sum of elements in this stream. This is a special case
of a

reduction

and is equivalent to:

```java
return reduce(0, Long::sum);
```

This is a

terminal
operation

.

**Returns:** the sum of elements in this stream

- min

```java
OptionalLong
min()
```

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::min);
```

This is a

terminal operation

.

**Returns:** an

OptionalLong

containing the minimum element of this
stream, or an empty

OptionalLong

if the stream is empty

- max

```java
OptionalLong
max()
```

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::max);
```

This is a

terminal
operation

.

**Returns:** an

OptionalLong

containing the maximum element of this
stream, or an empty

OptionalLong

if the stream is empty

- count

```java
long count()
```

Returns the count of elements in this stream. This is a special case of
a

reduction

and is
equivalent to:

```java
return map(e -> 1L).sum();
```

This is a

terminal operation

.

**API Note:** An implementation may choose to not execute the stream pipeline (either
sequentially or in parallel) if it is capable of computing the count
directly from the stream source. In such cases no source elements will
be traversed and no intermediate operations will be evaluated.
Behavioral parameters with side-effects, which are strongly discouraged
except for harmless cases such as debugging, may be affected. For
example, consider the following stream:

```java
LongStream s = LongStream.of(1, 2, 3, 4);
long count = s.peek(System.out::println).count();
```

The number of elements covered by the stream source is known and the
intermediate operation,

peek

, does not inject into or remove
elements from the stream (as may be the case for

flatMap

or

filter

operations). Thus the count is 4 and there is no need to
execute the pipeline and, as a side-effect, print out the elements.
**Returns:** the count of elements in this stream

- average

```java
OptionalDouble
average()
```

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty. This is a
special case of a

reduction

.

This is a

terminal
operation

.

**Returns:** an

OptionalDouble

containing the average element of this
stream, or an empty optional if the stream is empty

- summaryStatistics

```java
LongSummaryStatistics
summaryStatistics()
```

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream. This is a special case of a

reduction

.

This is a

terminal
operation

.

**Returns:** a

LongSummaryStatistics

describing various summary data
about the elements of this stream

- anyMatch

```java
boolean anyMatch​(
LongPredicate
predicate)
```

Returns whether any elements of this stream match the provided
predicate. May not evaluate the predicate on all elements if not
necessary for determining the result. If the stream is empty then

false

is returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

existential quantification

of the
predicate over the elements of the stream (for some x P(x)).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if any elements of the stream match the provided
predicate, otherwise

false

- allMatch

```java
boolean allMatch​(
LongPredicate
predicate)
```

Returns whether all elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

universal quantification

of the
predicate over the elements of the stream (for all x P(x)). If the
stream is empty, the quantification is said to be

vacuously
satisfied

and is always

true

(regardless of P(x)).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if either all elements of the stream match the
provided predicate or the stream is empty, otherwise

false

- noneMatch

```java
boolean noneMatch​(
LongPredicate
predicate)
```

Returns whether no elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

universal quantification

of the
negated predicate over the elements of the stream (for all x ~P(x)). If
the stream is empty, the quantification is said to be vacuously satisfied
and is always

true

, regardless of P(x).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if either no elements of the stream match the
provided predicate or the stream is empty, otherwise

false

- findFirst

```java
OptionalLong
findFirst()
```

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty. If the
stream has no encounter order, then any element may be returned.

This is a

short-circuiting
terminal operation

.

**Returns:** an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty

- findAny

```java
OptionalLong
findAny()
```

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

This is a

short-circuiting
terminal operation

.

The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use

findFirst()

instead.)

**Returns:** an

OptionalLong

describing some element of this stream,
or an empty

OptionalLong

if the stream is empty
**See Also:** findFirst()

- asDoubleStream

```java
DoubleStream
asDoubleStream()
```

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

This is an

intermediate
operation

.

**Returns:** a

DoubleStream

consisting of the elements of this stream,
converted to

double

- boxed

```java
Stream
<
Long
> boxed()
```

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

This is an

intermediate
operation

.

**Returns:** a

Stream

consistent of the elements of this stream,
each boxed to

Long

- builder

```java
static
LongStream.Builder
builder()
```

Returns a builder for a

LongStream

.

**Returns:** a stream builder

- empty

```java
static
LongStream
empty()
```

Returns an empty sequential

LongStream

.

**Returns:** an empty sequential stream

- of

```java
static
LongStream
of​(long t)
```

Returns a sequential

LongStream

containing a single element.

**Parameters:** t

- the single element
**Returns:** a singleton sequential stream

- of

```java
static
LongStream
of​(long... values)
```

Returns a sequential ordered stream whose elements are the specified values.

**Parameters:** values

- the elements of the new stream
**Returns:** the new stream

- iterate

```java
static
LongStream
iterate​(long seed,

LongUnaryOperator
f)
```

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

The first element (position

0

) in the

LongStream

will
be the provided

seed

. For

n > 0

, the element at position

n

, will be the result of applying the function

f

to the
element at position

n - 1

.

The action of applying

f

for one element

happens-before

the action of applying

f

for subsequent elements. For any given
element the action may be performed in whatever thread the library
chooses.

**Parameters:** seed

- the initial element
**Parameters:** f

- a function to be applied to the previous element to produce
a new element
**Returns:** a new sequential

LongStream

- iterate

```java
static
LongStream
iterate​(long seed,

LongPredicate
hasNext,

LongUnaryOperator
next)
```

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate. The
stream terminates as soon as the

hasNext

predicate returns false.

LongStream.iterate

should produce the same sequence of elements as
produced by the corresponding for-loop:

```java
for (long index=seed; hasNext.test(index); index = next.applyAsLong(index)) {
...
}
```

The resulting sequence may be empty if the

hasNext

predicate
does not hold on the seed value. Otherwise the first element will be the
supplied

seed

value, the next element (if present) will be the
result of applying the

next

function to the

seed

value,
and so on iteratively until the

hasNext

predicate indicates that
the stream should terminate.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

**Parameters:** seed

- the initial element
**Parameters:** hasNext

- a predicate to apply to elements to determine when the
stream must terminate.
**Parameters:** next

- a function to be applied to the previous element to produce
a new element
**Returns:** a new sequential

LongStream
**Since:** 9

- generate

```java
static
LongStream
generate​(
LongSupplier
s)
```

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

. This is suitable for
generating constant streams, streams of random elements, etc.

**Parameters:** s

- the

LongSupplier

for generated elements
**Returns:** a new infinite sequential unordered

LongStream

- range

```java
static
LongStream
range​(long startInclusive,
long endExclusive)
```

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

**API Note:** An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i < endExclusive ; i++) { ... }
```
**Parameters:** startInclusive

- the (inclusive) initial value
**Parameters:** endExclusive

- the exclusive upper bound
**Returns:** a sequential

LongStream

for the range of

long

elements

- rangeClosed

```java
static
LongStream
rangeClosed​(long startInclusive,
long endInclusive)
```

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

**API Note:** An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i <= endInclusive ; i++) { ... }
```
**Parameters:** startInclusive

- the (inclusive) initial value
**Parameters:** endInclusive

- the inclusive upper bound
**Returns:** a sequential

LongStream

for the range of

long

elements

- concat

```java
static
LongStream
concat​(
LongStream
a,

LongStream
b)
```

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream. The resulting stream is ordered if both
of the input streams are ordered, and parallel if either of the input
streams is parallel. When the resulting stream is closed, the close
handlers for both input streams are invoked.

This method operates on the two input streams and binds each stream
to its source. As a result subsequent modifications to an input stream
source may not be reflected in the concatenated stream result.

**API Note:** To preserve optimization opportunities this method binds each stream to
its source and accepts only two streams as parameters. For example, the
exact size of the concatenated stream source can be computed if the exact
size of each input stream source is known.
To concatenate more streams without binding, or without nested calls to
this method, try creating a stream of streams and flat-mapping with the
identity function, for example:

```java
LongStream concat = Stream.of(s1, s2, s3, s4).flatMapToLong(s -> s);
```
**Implementation Note:** Use caution when constructing streams from repeated concatenation.
Accessing an element of a deeply concatenated stream can result in deep
call chains, or even

StackOverflowError

.
**Parameters:** a

- the first stream
**Parameters:** b

- the second stream
**Returns:** the concatenation of the two input streams

Method Detail

- filter

```java
LongStream
filter​(
LongPredicate
predicate)
```

Returns a stream consisting of the elements of this stream that match
the given predicate.

This is an

intermediate
operation

.

**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to each element to determine if it
should be included
**Returns:** the new stream

- map

```java
LongStream
map​(
LongUnaryOperator
mapper)
```

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- mapToObj

```java
<U>
Stream
<U> mapToObj​(
LongFunction
<? extends U> mapper)
```

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

This is an

intermediate operation

.

**Type Parameters:** U

- the element type of the new stream
**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- mapToInt

```java
IntStream
mapToInt​(
LongToIntFunction
mapper)
```

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- mapToDouble

```java
DoubleStream
mapToDouble​(
LongToDoubleFunction
mapper)
```

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

- flatMap

```java
LongStream
flatMap​(
LongFunction
<? extends
LongStream
> mapper)
```

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element. Each mapped stream is

closed

after its contents
have been placed into this stream. (If a mapped stream is

null

an empty stream is used, instead.)

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element which produces a

LongStream

of new values
**Returns:** the new stream
**See Also:** Stream.flatMap(Function)

- distinct

```java
LongStream
distinct()
```

Returns a stream consisting of the distinct elements of this stream.

This is a

stateful
intermediate operation

.

**Returns:** the new stream

- sorted

```java
LongStream
sorted()
```

Returns a stream consisting of the elements of this stream in sorted
order.

This is a

stateful
intermediate operation

.

**Returns:** the new stream

- peek

```java
LongStream
peek​(
LongConsumer
action)
```

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

This is an

intermediate
operation

.

For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.

**API Note:** This method exists mainly to support debugging, where you want
to see the elements as they flow past a certain point in a pipeline:

```java
LongStream.of(1, 2, 3, 4)
.filter(e -> e > 2)
.peek(e -> System.out.println("Filtered value: " + e))
.map(e -> e * e)
.peek(e -> System.out.println("Mapped value: " + e))
.sum();
```

In cases where the stream implementation is able to optimize away the
production of some or all the elements (such as with short-circuiting
operations like

findFirst

, or in the example described in

count()

), the action will not be invoked for those elements.
**Parameters:** action

- a

non-interfering

action to perform on the elements as
they are consumed from the stream
**Returns:** the new stream

- limit

```java
LongStream
limit​(long maxSize)
```

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

This is a

short-circuiting
stateful intermediate operation

.

**API Note:** While

limit()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

maxSize

, since

limit(n)

is constrained to return not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

limit()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

limit()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.
**Parameters:** maxSize

- the number of elements the stream should be limited to
**Returns:** the new stream
**Throws:** IllegalArgumentException

- if

maxSize

is negative

- skip

```java
LongStream
skip​(long n)
```

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.
If this stream contains fewer than

n

elements then an
empty stream will be returned.

This is a

stateful
intermediate operation

.

**API Note:** While

skip()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

n

, since

skip(n)

is constrained to skip not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

skip()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

skip()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.
**Parameters:** n

- the number of leading elements to skip
**Returns:** the new stream
**Throws:** IllegalArgumentException

- if

n

is negative

- takeWhile

```java
default
LongStream
takeWhile​(
LongPredicate
predicate)
```

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.
Otherwise returns, if this stream is unordered, a stream consisting of a
subset of elements taken from this stream that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to take any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

**API Note:** While

takeWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

takeWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

takeWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.
**Implementation Requirements:** The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.
**Returns:** the new stream
**Since:** 9

- dropWhile

```java
default
LongStream
dropWhile​(
LongPredicate
predicate)
```

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate. Otherwise returns, if this stream is
unordered, a stream consisting of the remaining elements of this stream
after dropping a subset of elements that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to drop any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

**API Note:** While

dropWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

dropWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

dropWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.
**Implementation Requirements:** The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.
**Returns:** the new stream
**Since:** 9

- forEach

```java
void forEach​(
LongConsumer
action)
```

Performs an action for each element of this stream.

This is a

terminal
operation

.

For parallel stream pipelines, this operation does

not

guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.

**Parameters:** action

- a

non-interfering

action to perform on the elements

- forEachOrdered

```java
void forEachOrdered​(
LongConsumer
action)
```

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

This is a

terminal
operation

.

**Parameters:** action

- a

non-interfering

action to perform on the elements
**See Also:** forEach(LongConsumer)

- toArray

```java
long[] toArray()
```

Returns an array containing the elements of this stream.

This is a

terminal
operation

.

**Returns:** an array containing the elements of this stream

- reduce

```java
long reduce​(long identity,

LongBinaryOperator
op)
```

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value. This is equivalent
to:

```java
long result = identity;
for (long element : this stream)
result = accumulator.applyAsLong(result, element)
return result;
```

but is not constrained to execute sequentially.

The

identity

value must be an identity for the accumulator
function. This means that for all

x

,

accumulator.apply(identity, x)

is equal to

x

.
The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**API Note:** Sum, min, max, and average are all special cases of reduction.
Summing a stream of numbers can be expressed as:

```java
long sum = integers.reduce(0, (a, b) -> a+b);
```

or more compactly:

```java
long sum = integers.reduce(0, Long::sum);
```

While this may seem a more roundabout way to perform an aggregation
compared to simply mutating a running total in a loop, reduction
operations parallelize more gracefully, without needing additional
synchronization and with greatly reduced risk of data races.
**Parameters:** identity

- the identity value for the accumulating function
**Parameters:** op

- an

associative

,

non-interfering

,

stateless

function for combining two values
**Returns:** the result of the reduction
**See Also:** sum()

,

min()

,

max()

,

average()

- reduce

```java
OptionalLong
reduce​(
LongBinaryOperator
op)
```

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any. This is equivalent to:

```java
boolean foundAny = false;
long result = null;
for (long element : this stream) {
if (!foundAny) {
foundAny = true;
result = element;
}
else
result = accumulator.applyAsLong(result, element);
}
return foundAny ? OptionalLong.of(result) : OptionalLong.empty();
```

but is not constrained to execute sequentially.

The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**Parameters:** op

- an

associative

,

non-interfering

,

stateless

function for combining two values
**Returns:** the result of the reduction
**See Also:** reduce(long, LongBinaryOperator)

- collect

```java
<R> R collect​(
Supplier
<R> supplier,

ObjLongConsumer
<R> accumulator,

BiConsumer
<R,​R> combiner)
```

Performs a

mutable
reduction

operation on the elements of this stream. A mutable
reduction is one in which the reduced value is a mutable result container,
such as an

ArrayList

, and elements are incorporated by updating
the state of the result rather than by replacing the result. This
produces a result equivalent to:

```java
R result = supplier.get();
for (long element : this stream)
accumulator.accept(result, element);
return result;
```

Like

reduce(long, LongBinaryOperator)

,

collect

operations
can be parallelized without requiring additional synchronization.

This is a

terminal
operation

.

**Type Parameters:** R

- the type of the mutable result container
**Parameters:** supplier

- a function that creates a new mutable result container.
For a parallel execution, this function may be called
multiple times and must return a fresh value each time.
**Parameters:** accumulator

- an

associative

,

non-interfering

,

stateless

function that must fold an element into a result
container.
**Parameters:** combiner

- an

associative

,

non-interfering

,

stateless

function that accepts two partial result containers
and merges them, which must be compatible with the
accumulator function. The combiner function must fold
the elements from the second result container into the
first result container.
**Returns:** the result of the reduction
**See Also:** Stream.collect(Supplier, BiConsumer, BiConsumer)

- sum

```java
long sum()
```

Returns the sum of elements in this stream. This is a special case
of a

reduction

and is equivalent to:

```java
return reduce(0, Long::sum);
```

This is a

terminal
operation

.

**Returns:** the sum of elements in this stream

- min

```java
OptionalLong
min()
```

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::min);
```

This is a

terminal operation

.

**Returns:** an

OptionalLong

containing the minimum element of this
stream, or an empty

OptionalLong

if the stream is empty

- max

```java
OptionalLong
max()
```

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::max);
```

This is a

terminal
operation

.

**Returns:** an

OptionalLong

containing the maximum element of this
stream, or an empty

OptionalLong

if the stream is empty

- count

```java
long count()
```

Returns the count of elements in this stream. This is a special case of
a

reduction

and is
equivalent to:

```java
return map(e -> 1L).sum();
```

This is a

terminal operation

.

**API Note:** An implementation may choose to not execute the stream pipeline (either
sequentially or in parallel) if it is capable of computing the count
directly from the stream source. In such cases no source elements will
be traversed and no intermediate operations will be evaluated.
Behavioral parameters with side-effects, which are strongly discouraged
except for harmless cases such as debugging, may be affected. For
example, consider the following stream:

```java
LongStream s = LongStream.of(1, 2, 3, 4);
long count = s.peek(System.out::println).count();
```

The number of elements covered by the stream source is known and the
intermediate operation,

peek

, does not inject into or remove
elements from the stream (as may be the case for

flatMap

or

filter

operations). Thus the count is 4 and there is no need to
execute the pipeline and, as a side-effect, print out the elements.
**Returns:** the count of elements in this stream

- average

```java
OptionalDouble
average()
```

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty. This is a
special case of a

reduction

.

This is a

terminal
operation

.

**Returns:** an

OptionalDouble

containing the average element of this
stream, or an empty optional if the stream is empty

- summaryStatistics

```java
LongSummaryStatistics
summaryStatistics()
```

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream. This is a special case of a

reduction

.

This is a

terminal
operation

.

**Returns:** a

LongSummaryStatistics

describing various summary data
about the elements of this stream

- anyMatch

```java
boolean anyMatch​(
LongPredicate
predicate)
```

Returns whether any elements of this stream match the provided
predicate. May not evaluate the predicate on all elements if not
necessary for determining the result. If the stream is empty then

false

is returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

existential quantification

of the
predicate over the elements of the stream (for some x P(x)).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if any elements of the stream match the provided
predicate, otherwise

false

- allMatch

```java
boolean allMatch​(
LongPredicate
predicate)
```

Returns whether all elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

universal quantification

of the
predicate over the elements of the stream (for all x P(x)). If the
stream is empty, the quantification is said to be

vacuously
satisfied

and is always

true

(regardless of P(x)).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if either all elements of the stream match the
provided predicate or the stream is empty, otherwise

false

- noneMatch

```java
boolean noneMatch​(
LongPredicate
predicate)
```

Returns whether no elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

universal quantification

of the
negated predicate over the elements of the stream (for all x ~P(x)). If
the stream is empty, the quantification is said to be vacuously satisfied
and is always

true

, regardless of P(x).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if either no elements of the stream match the
provided predicate or the stream is empty, otherwise

false

- findFirst

```java
OptionalLong
findFirst()
```

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty. If the
stream has no encounter order, then any element may be returned.

This is a

short-circuiting
terminal operation

.

**Returns:** an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty

- findAny

```java
OptionalLong
findAny()
```

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

This is a

short-circuiting
terminal operation

.

The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use

findFirst()

instead.)

**Returns:** an

OptionalLong

describing some element of this stream,
or an empty

OptionalLong

if the stream is empty
**See Also:** findFirst()

- asDoubleStream

```java
DoubleStream
asDoubleStream()
```

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

This is an

intermediate
operation

.

**Returns:** a

DoubleStream

consisting of the elements of this stream,
converted to

double

- boxed

```java
Stream
<
Long
> boxed()
```

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

This is an

intermediate
operation

.

**Returns:** a

Stream

consistent of the elements of this stream,
each boxed to

Long

- builder

```java
static
LongStream.Builder
builder()
```

Returns a builder for a

LongStream

.

**Returns:** a stream builder

- empty

```java
static
LongStream
empty()
```

Returns an empty sequential

LongStream

.

**Returns:** an empty sequential stream

- of

```java
static
LongStream
of​(long t)
```

Returns a sequential

LongStream

containing a single element.

**Parameters:** t

- the single element
**Returns:** a singleton sequential stream

- of

```java
static
LongStream
of​(long... values)
```

Returns a sequential ordered stream whose elements are the specified values.

**Parameters:** values

- the elements of the new stream
**Returns:** the new stream

- iterate

```java
static
LongStream
iterate​(long seed,

LongUnaryOperator
f)
```

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

The first element (position

0

) in the

LongStream

will
be the provided

seed

. For

n > 0

, the element at position

n

, will be the result of applying the function

f

to the
element at position

n - 1

.

The action of applying

f

for one element

happens-before

the action of applying

f

for subsequent elements. For any given
element the action may be performed in whatever thread the library
chooses.

**Parameters:** seed

- the initial element
**Parameters:** f

- a function to be applied to the previous element to produce
a new element
**Returns:** a new sequential

LongStream

- iterate

```java
static
LongStream
iterate​(long seed,

LongPredicate
hasNext,

LongUnaryOperator
next)
```

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate. The
stream terminates as soon as the

hasNext

predicate returns false.

LongStream.iterate

should produce the same sequence of elements as
produced by the corresponding for-loop:

```java
for (long index=seed; hasNext.test(index); index = next.applyAsLong(index)) {
...
}
```

The resulting sequence may be empty if the

hasNext

predicate
does not hold on the seed value. Otherwise the first element will be the
supplied

seed

value, the next element (if present) will be the
result of applying the

next

function to the

seed

value,
and so on iteratively until the

hasNext

predicate indicates that
the stream should terminate.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

**Parameters:** seed

- the initial element
**Parameters:** hasNext

- a predicate to apply to elements to determine when the
stream must terminate.
**Parameters:** next

- a function to be applied to the previous element to produce
a new element
**Returns:** a new sequential

LongStream
**Since:** 9

- generate

```java
static
LongStream
generate​(
LongSupplier
s)
```

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

. This is suitable for
generating constant streams, streams of random elements, etc.

**Parameters:** s

- the

LongSupplier

for generated elements
**Returns:** a new infinite sequential unordered

LongStream

- range

```java
static
LongStream
range​(long startInclusive,
long endExclusive)
```

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

**API Note:** An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i < endExclusive ; i++) { ... }
```
**Parameters:** startInclusive

- the (inclusive) initial value
**Parameters:** endExclusive

- the exclusive upper bound
**Returns:** a sequential

LongStream

for the range of

long

elements

- rangeClosed

```java
static
LongStream
rangeClosed​(long startInclusive,
long endInclusive)
```

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

**API Note:** An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i <= endInclusive ; i++) { ... }
```
**Parameters:** startInclusive

- the (inclusive) initial value
**Parameters:** endInclusive

- the inclusive upper bound
**Returns:** a sequential

LongStream

for the range of

long

elements

- concat

```java
static
LongStream
concat​(
LongStream
a,

LongStream
b)
```

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream. The resulting stream is ordered if both
of the input streams are ordered, and parallel if either of the input
streams is parallel. When the resulting stream is closed, the close
handlers for both input streams are invoked.

This method operates on the two input streams and binds each stream
to its source. As a result subsequent modifications to an input stream
source may not be reflected in the concatenated stream result.

**API Note:** To preserve optimization opportunities this method binds each stream to
its source and accepts only two streams as parameters. For example, the
exact size of the concatenated stream source can be computed if the exact
size of each input stream source is known.
To concatenate more streams without binding, or without nested calls to
this method, try creating a stream of streams and flat-mapping with the
identity function, for example:

```java
LongStream concat = Stream.of(s1, s2, s3, s4).flatMapToLong(s -> s);
```
**Implementation Note:** Use caution when constructing streams from repeated concatenation.
Accessing an element of a deeply concatenated stream can result in deep
call chains, or even

StackOverflowError

.
**Parameters:** a

- the first stream
**Parameters:** b

- the second stream
**Returns:** the concatenation of the two input streams

---

#### Method Detail

filter

```java
LongStream
filter​(
LongPredicate
predicate)
```

Returns a stream consisting of the elements of this stream that match
the given predicate.

This is an

intermediate
operation

.

**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to each element to determine if it
should be included
**Returns:** the new stream

---

#### filter

LongStream

filter​(

LongPredicate

predicate)

Returns a stream consisting of the elements of this stream that match
the given predicate.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

map

```java
LongStream
map​(
LongUnaryOperator
mapper)
```

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

---

#### map

LongStream

map​(

LongUnaryOperator

mapper)

Returns a stream consisting of the results of applying the given
function to the elements of this stream.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

mapToObj

```java
<U>
Stream
<U> mapToObj​(
LongFunction
<? extends U> mapper)
```

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

This is an

intermediate operation

.

**Type Parameters:** U

- the element type of the new stream
**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

---

#### mapToObj

<U>

Stream

<U> mapToObj​(

LongFunction

<? extends U> mapper)

Returns an object-valued

Stream

consisting of the results of
applying the given function to the elements of this stream.

This is an

intermediate operation

.

This is an

intermediate operation

.

mapToInt

```java
IntStream
mapToInt​(
LongToIntFunction
mapper)
```

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

---

#### mapToInt

IntStream

mapToInt​(

LongToIntFunction

mapper)

Returns an

IntStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

mapToDouble

```java
DoubleStream
mapToDouble​(
LongToDoubleFunction
mapper)
```

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element
**Returns:** the new stream

---

#### mapToDouble

DoubleStream

mapToDouble​(

LongToDoubleFunction

mapper)

Returns a

DoubleStream

consisting of the results of applying the
given function to the elements of this stream.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

flatMap

```java
LongStream
flatMap​(
LongFunction
<? extends
LongStream
> mapper)
```

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element. Each mapped stream is

closed

after its contents
have been placed into this stream. (If a mapped stream is

null

an empty stream is used, instead.)

This is an

intermediate
operation

.

**Parameters:** mapper

- a

non-interfering

,

stateless

function to apply to each element which produces a

LongStream

of new values
**Returns:** the new stream
**See Also:** Stream.flatMap(Function)

---

#### flatMap

LongStream

flatMap​(

LongFunction

<? extends

LongStream

> mapper)

Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element. Each mapped stream is

closed

after its contents
have been placed into this stream. (If a mapped stream is

null

an empty stream is used, instead.)

This is an

intermediate
operation

.

This is an

intermediate
operation

.

distinct

```java
LongStream
distinct()
```

Returns a stream consisting of the distinct elements of this stream.

This is a

stateful
intermediate operation

.

**Returns:** the new stream

---

#### distinct

LongStream

distinct()

Returns a stream consisting of the distinct elements of this stream.

This is a

stateful
intermediate operation

.

This is a

stateful
intermediate operation

.

sorted

```java
LongStream
sorted()
```

Returns a stream consisting of the elements of this stream in sorted
order.

This is a

stateful
intermediate operation

.

**Returns:** the new stream

---

#### sorted

LongStream

sorted()

Returns a stream consisting of the elements of this stream in sorted
order.

This is a

stateful
intermediate operation

.

This is a

stateful
intermediate operation

.

peek

```java
LongStream
peek​(
LongConsumer
action)
```

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

This is an

intermediate
operation

.

For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.

**API Note:** This method exists mainly to support debugging, where you want
to see the elements as they flow past a certain point in a pipeline:

```java
LongStream.of(1, 2, 3, 4)
.filter(e -> e > 2)
.peek(e -> System.out.println("Filtered value: " + e))
.map(e -> e * e)
.peek(e -> System.out.println("Mapped value: " + e))
.sum();
```

In cases where the stream implementation is able to optimize away the
production of some or all the elements (such as with short-circuiting
operations like

findFirst

, or in the example described in

count()

), the action will not be invoked for those elements.
**Parameters:** action

- a

non-interfering

action to perform on the elements as
they are consumed from the stream
**Returns:** the new stream

---

#### peek

LongStream

peek​(

LongConsumer

action)

Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.

This is an

intermediate
operation

.

For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.

This is an

intermediate
operation

.

For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.

For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.

LongStream.of(1, 2, 3, 4)
.filter(e -> e > 2)
.peek(e -> System.out.println("Filtered value: " + e))
.map(e -> e * e)
.peek(e -> System.out.println("Mapped value: " + e))
.sum();

In cases where the stream implementation is able to optimize away the
production of some or all the elements (such as with short-circuiting
operations like

findFirst

, or in the example described in

count()

), the action will not be invoked for those elements.

limit

```java
LongStream
limit​(long maxSize)
```

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

This is a

short-circuiting
stateful intermediate operation

.

**API Note:** While

limit()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

maxSize

, since

limit(n)

is constrained to return not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

limit()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

limit()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.
**Parameters:** maxSize

- the number of elements the stream should be limited to
**Returns:** the new stream
**Throws:** IllegalArgumentException

- if

maxSize

is negative

---

#### limit

LongStream

limit​(long maxSize)

Returns a stream consisting of the elements of this stream, truncated
to be no longer than

maxSize

in length.

This is a

short-circuiting
stateful intermediate operation

.

This is a

short-circuiting
stateful intermediate operation

.

skip

```java
LongStream
skip​(long n)
```

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.
If this stream contains fewer than

n

elements then an
empty stream will be returned.

This is a

stateful
intermediate operation

.

**API Note:** While

skip()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of

n

, since

skip(n)

is constrained to skip not just any

n

elements, but the

first n

elements in the encounter order. Using an unordered
stream source (such as

generate(LongSupplier)

) or removing the
ordering constraint with

BaseStream.unordered()

may result in significant
speedups of

skip()

in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with

skip()

in parallel pipelines, switching to sequential execution
with

BaseStream.sequential()

may improve performance.
**Parameters:** n

- the number of leading elements to skip
**Returns:** the new stream
**Throws:** IllegalArgumentException

- if

n

is negative

---

#### skip

LongStream

skip​(long n)

Returns a stream consisting of the remaining elements of this stream
after discarding the first

n

elements of the stream.
If this stream contains fewer than

n

elements then an
empty stream will be returned.

This is a

stateful
intermediate operation

.

This is a

stateful
intermediate operation

.

takeWhile

```java
default
LongStream
takeWhile​(
LongPredicate
predicate)
```

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.
Otherwise returns, if this stream is unordered, a stream consisting of a
subset of elements taken from this stream that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to take any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

**API Note:** While

takeWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

takeWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

takeWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.
**Implementation Requirements:** The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.
**Returns:** the new stream
**Since:** 9

---

#### takeWhile

default

LongStream

takeWhile​(

LongPredicate

predicate)

Returns, if this stream is ordered, a stream consisting of the longest
prefix of elements taken from this stream that match the given predicate.
Otherwise returns, if this stream is unordered, a stream consisting of a
subset of elements taken from this stream that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to take any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to take any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to take any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
takes all elements (the result is the same as the input), or if no
elements of the stream match the given predicate then no elements are
taken (the result is an empty stream).

This is a

short-circuiting
stateful intermediate operation

.

This is a

short-circuiting
stateful intermediate operation

.

dropWhile

```java
default
LongStream
dropWhile​(
LongPredicate
predicate)
```

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate. Otherwise returns, if this stream is
unordered, a stream consisting of the remaining elements of this stream
after dropping a subset of elements that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to drop any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

**API Note:** While

dropWhile()

is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel
pipelines, since the operation is constrained to return not just any
valid prefix, but the longest prefix of elements in the encounter order.
Using an unordered stream source (such as

generate(LongSupplier)

) or removing the ordering constraint with

BaseStream.unordered()

may result in significant speedups of

dropWhile()

in parallel pipelines, if the semantics of your
situation permit. If consistency with encounter order is required, and
you are experiencing poor performance or memory utilization with

dropWhile()

in parallel pipelines, switching to sequential
execution with

BaseStream.sequential()

may improve performance.
**Implementation Requirements:** The default implementation obtains the

spliterator

of this stream, wraps that spliterator so as to support the semantics
of this operation on traversal, and returns a new stream associated with
the wrapped spliterator. The returned stream preserves the execution
characteristics of this stream (namely parallel or sequential execution
as per

BaseStream.isParallel()

) but the wrapped spliterator may choose to
not support splitting. When the returned stream is closed, the close
handlers for both the returned and this stream are invoked.
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements to determine the longest
prefix of elements.
**Returns:** the new stream
**Since:** 9

---

#### dropWhile

default

LongStream

dropWhile​(

LongPredicate

predicate)

Returns, if this stream is ordered, a stream consisting of the remaining
elements of this stream after dropping the longest prefix of elements
that match the given predicate. Otherwise returns, if this stream is
unordered, a stream consisting of the remaining elements of this stream
after dropping a subset of elements that match the given predicate.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to drop any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

If this stream is ordered then the longest prefix is a contiguous
sequence of elements of this stream that match the given predicate. The
first element of the sequence is the first element of this stream, and
the element immediately following the last element of the sequence does
not match the given predicate.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to drop any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

If this stream is unordered, and some (but not all) elements of this
stream match the given predicate, then the behavior of this operation is
nondeterministic; it is free to drop any subset of matching elements
(which includes the empty set).

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

Independent of whether this stream is ordered or unordered if all
elements of this stream match the given predicate then this operation
drops all elements (the result is an empty stream), or if no elements of
the stream match the given predicate then no elements are dropped (the
result is the same as the input).

This is a

stateful
intermediate operation

.

This is a

stateful
intermediate operation

.

forEach

```java
void forEach​(
LongConsumer
action)
```

Performs an action for each element of this stream.

This is a

terminal
operation

.

For parallel stream pipelines, this operation does

not

guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.

**Parameters:** action

- a

non-interfering

action to perform on the elements

---

#### forEach

void forEach​(

LongConsumer

action)

Performs an action for each element of this stream.

This is a

terminal
operation

.

For parallel stream pipelines, this operation does

not

guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.

This is a

terminal
operation

.

For parallel stream pipelines, this operation does

not

guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.

For parallel stream pipelines, this operation does

not

guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.

forEachOrdered

```java
void forEachOrdered​(
LongConsumer
action)
```

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

This is a

terminal
operation

.

**Parameters:** action

- a

non-interfering

action to perform on the elements
**See Also:** forEach(LongConsumer)

---

#### forEachOrdered

void forEachOrdered​(

LongConsumer

action)

Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.

This is a

terminal
operation

.

This is a

terminal
operation

.

toArray

```java
long[] toArray()
```

Returns an array containing the elements of this stream.

This is a

terminal
operation

.

**Returns:** an array containing the elements of this stream

---

#### toArray

long[] toArray()

Returns an array containing the elements of this stream.

This is a

terminal
operation

.

This is a

terminal
operation

.

reduce

```java
long reduce​(long identity,

LongBinaryOperator
op)
```

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value. This is equivalent
to:

```java
long result = identity;
for (long element : this stream)
result = accumulator.applyAsLong(result, element)
return result;
```

but is not constrained to execute sequentially.

The

identity

value must be an identity for the accumulator
function. This means that for all

x

,

accumulator.apply(identity, x)

is equal to

x

.
The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**API Note:** Sum, min, max, and average are all special cases of reduction.
Summing a stream of numbers can be expressed as:

```java
long sum = integers.reduce(0, (a, b) -> a+b);
```

or more compactly:

```java
long sum = integers.reduce(0, Long::sum);
```

While this may seem a more roundabout way to perform an aggregation
compared to simply mutating a running total in a loop, reduction
operations parallelize more gracefully, without needing additional
synchronization and with greatly reduced risk of data races.
**Parameters:** identity

- the identity value for the accumulating function
**Parameters:** op

- an

associative

,

non-interfering

,

stateless

function for combining two values
**Returns:** the result of the reduction
**See Also:** sum()

,

min()

,

max()

,

average()

---

#### reduce

long reduce​(long identity,

LongBinaryOperator

op)

Performs a

reduction

on the
elements of this stream, using the provided identity value and an

associative

accumulation function, and returns the reduced value. This is equivalent
to:

```java
long result = identity;
for (long element : this stream)
result = accumulator.applyAsLong(result, element)
return result;
```

but is not constrained to execute sequentially.

The

identity

value must be an identity for the accumulator
function. This means that for all

x

,

accumulator.apply(identity, x)

is equal to

x

.
The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

long result = identity;
for (long element : this stream)
result = accumulator.applyAsLong(result, element)
return result;

The

identity

value must be an identity for the accumulator
function. This means that for all

x

,

accumulator.apply(identity, x)

is equal to

x

.
The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

This is a

terminal
operation

.

long sum = integers.reduce(0, (a, b) -> a+b);

long sum = integers.reduce(0, Long::sum);

While this may seem a more roundabout way to perform an aggregation
compared to simply mutating a running total in a loop, reduction
operations parallelize more gracefully, without needing additional
synchronization and with greatly reduced risk of data races.

reduce

```java
OptionalLong
reduce​(
LongBinaryOperator
op)
```

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any. This is equivalent to:

```java
boolean foundAny = false;
long result = null;
for (long element : this stream) {
if (!foundAny) {
foundAny = true;
result = element;
}
else
result = accumulator.applyAsLong(result, element);
}
return foundAny ? OptionalLong.of(result) : OptionalLong.empty();
```

but is not constrained to execute sequentially.

The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

**Parameters:** op

- an

associative

,

non-interfering

,

stateless

function for combining two values
**Returns:** the result of the reduction
**See Also:** reduce(long, LongBinaryOperator)

---

#### reduce

OptionalLong

reduce​(

LongBinaryOperator

op)

Performs a

reduction

on the
elements of this stream, using an

associative

accumulation
function, and returns an

OptionalLong

describing the reduced value,
if any. This is equivalent to:

```java
boolean foundAny = false;
long result = null;
for (long element : this stream) {
if (!foundAny) {
foundAny = true;
result = element;
}
else
result = accumulator.applyAsLong(result, element);
}
return foundAny ? OptionalLong.of(result) : OptionalLong.empty();
```

but is not constrained to execute sequentially.

The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

boolean foundAny = false;
long result = null;
for (long element : this stream) {
if (!foundAny) {
foundAny = true;
result = element;
}
else
result = accumulator.applyAsLong(result, element);
}
return foundAny ? OptionalLong.of(result) : OptionalLong.empty();

The

accumulator

function must be an

associative

function.

This is a

terminal
operation

.

This is a

terminal
operation

.

collect

```java
<R> R collect​(
Supplier
<R> supplier,

ObjLongConsumer
<R> accumulator,

BiConsumer
<R,​R> combiner)
```

Performs a

mutable
reduction

operation on the elements of this stream. A mutable
reduction is one in which the reduced value is a mutable result container,
such as an

ArrayList

, and elements are incorporated by updating
the state of the result rather than by replacing the result. This
produces a result equivalent to:

```java
R result = supplier.get();
for (long element : this stream)
accumulator.accept(result, element);
return result;
```

Like

reduce(long, LongBinaryOperator)

,

collect

operations
can be parallelized without requiring additional synchronization.

This is a

terminal
operation

.

**Type Parameters:** R

- the type of the mutable result container
**Parameters:** supplier

- a function that creates a new mutable result container.
For a parallel execution, this function may be called
multiple times and must return a fresh value each time.
**Parameters:** accumulator

- an

associative

,

non-interfering

,

stateless

function that must fold an element into a result
container.
**Parameters:** combiner

- an

associative

,

non-interfering

,

stateless

function that accepts two partial result containers
and merges them, which must be compatible with the
accumulator function. The combiner function must fold
the elements from the second result container into the
first result container.
**Returns:** the result of the reduction
**See Also:** Stream.collect(Supplier, BiConsumer, BiConsumer)

---

#### collect

<R> R collect​(

Supplier

<R> supplier,

ObjLongConsumer

<R> accumulator,

BiConsumer

<R,​R> combiner)

Performs a

mutable
reduction

operation on the elements of this stream. A mutable
reduction is one in which the reduced value is a mutable result container,
such as an

ArrayList

, and elements are incorporated by updating
the state of the result rather than by replacing the result. This
produces a result equivalent to:

```java
R result = supplier.get();
for (long element : this stream)
accumulator.accept(result, element);
return result;
```

Like

reduce(long, LongBinaryOperator)

,

collect

operations
can be parallelized without requiring additional synchronization.

This is a

terminal
operation

.

R result = supplier.get();
for (long element : this stream)
accumulator.accept(result, element);
return result;

Like

reduce(long, LongBinaryOperator)

,

collect

operations
can be parallelized without requiring additional synchronization.

This is a

terminal
operation

.

This is a

terminal
operation

.

sum

```java
long sum()
```

Returns the sum of elements in this stream. This is a special case
of a

reduction

and is equivalent to:

```java
return reduce(0, Long::sum);
```

This is a

terminal
operation

.

**Returns:** the sum of elements in this stream

---

#### sum

long sum()

Returns the sum of elements in this stream. This is a special case
of a

reduction

and is equivalent to:

```java
return reduce(0, Long::sum);
```

This is a

terminal
operation

.

return reduce(0, Long::sum);

This is a

terminal
operation

.

min

```java
OptionalLong
min()
```

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::min);
```

This is a

terminal operation

.

**Returns:** an

OptionalLong

containing the minimum element of this
stream, or an empty

OptionalLong

if the stream is empty

---

#### min

OptionalLong

min()

Returns an

OptionalLong

describing the minimum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::min);
```

This is a

terminal operation

.

return reduce(Long::min);

This is a

terminal operation

.

max

```java
OptionalLong
max()
```

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::max);
```

This is a

terminal
operation

.

**Returns:** an

OptionalLong

containing the maximum element of this
stream, or an empty

OptionalLong

if the stream is empty

---

#### max

OptionalLong

max()

Returns an

OptionalLong

describing the maximum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a

reduction

and is equivalent to:

```java
return reduce(Long::max);
```

This is a

terminal
operation

.

return reduce(Long::max);

This is a

terminal
operation

.

count

```java
long count()
```

Returns the count of elements in this stream. This is a special case of
a

reduction

and is
equivalent to:

```java
return map(e -> 1L).sum();
```

This is a

terminal operation

.

**API Note:** An implementation may choose to not execute the stream pipeline (either
sequentially or in parallel) if it is capable of computing the count
directly from the stream source. In such cases no source elements will
be traversed and no intermediate operations will be evaluated.
Behavioral parameters with side-effects, which are strongly discouraged
except for harmless cases such as debugging, may be affected. For
example, consider the following stream:

```java
LongStream s = LongStream.of(1, 2, 3, 4);
long count = s.peek(System.out::println).count();
```

The number of elements covered by the stream source is known and the
intermediate operation,

peek

, does not inject into or remove
elements from the stream (as may be the case for

flatMap

or

filter

operations). Thus the count is 4 and there is no need to
execute the pipeline and, as a side-effect, print out the elements.
**Returns:** the count of elements in this stream

---

#### count

long count()

Returns the count of elements in this stream. This is a special case of
a

reduction

and is
equivalent to:

```java
return map(e -> 1L).sum();
```

This is a

terminal operation

.

return map(e -> 1L).sum();

This is a

terminal operation

.

LongStream s = LongStream.of(1, 2, 3, 4);
long count = s.peek(System.out::println).count();

average

```java
OptionalDouble
average()
```

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty. This is a
special case of a

reduction

.

This is a

terminal
operation

.

**Returns:** an

OptionalDouble

containing the average element of this
stream, or an empty optional if the stream is empty

---

#### average

OptionalDouble

average()

Returns an

OptionalDouble

describing the arithmetic mean of elements of
this stream, or an empty optional if this stream is empty. This is a
special case of a

reduction

.

This is a

terminal
operation

.

This is a

terminal
operation

.

summaryStatistics

```java
LongSummaryStatistics
summaryStatistics()
```

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream. This is a special case of a

reduction

.

This is a

terminal
operation

.

**Returns:** a

LongSummaryStatistics

describing various summary data
about the elements of this stream

---

#### summaryStatistics

LongSummaryStatistics

summaryStatistics()

Returns a

LongSummaryStatistics

describing various summary data
about the elements of this stream. This is a special case of a

reduction

.

This is a

terminal
operation

.

This is a

terminal
operation

.

anyMatch

```java
boolean anyMatch​(
LongPredicate
predicate)
```

Returns whether any elements of this stream match the provided
predicate. May not evaluate the predicate on all elements if not
necessary for determining the result. If the stream is empty then

false

is returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

existential quantification

of the
predicate over the elements of the stream (for some x P(x)).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if any elements of the stream match the provided
predicate, otherwise

false

---

#### anyMatch

boolean anyMatch​(

LongPredicate

predicate)

Returns whether any elements of this stream match the provided
predicate. May not evaluate the predicate on all elements if not
necessary for determining the result. If the stream is empty then

false

is returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

This is a

short-circuiting
terminal operation

.

allMatch

```java
boolean allMatch​(
LongPredicate
predicate)
```

Returns whether all elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

universal quantification

of the
predicate over the elements of the stream (for all x P(x)). If the
stream is empty, the quantification is said to be

vacuously
satisfied

and is always

true

(regardless of P(x)).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if either all elements of the stream match the
provided predicate or the stream is empty, otherwise

false

---

#### allMatch

boolean allMatch​(

LongPredicate

predicate)

Returns whether all elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

This is a

short-circuiting
terminal operation

.

noneMatch

```java
boolean noneMatch​(
LongPredicate
predicate)
```

Returns whether no elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

**API Note:** This method evaluates the

universal quantification

of the
negated predicate over the elements of the stream (for all x ~P(x)). If
the stream is empty, the quantification is said to be vacuously satisfied
and is always

true

, regardless of P(x).
**Parameters:** predicate

- a

non-interfering

,

stateless

predicate to apply to elements of this stream
**Returns:** true

if either no elements of the stream match the
provided predicate or the stream is empty, otherwise

false

---

#### noneMatch

boolean noneMatch​(

LongPredicate

predicate)

Returns whether no elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then

true

is
returned and the predicate is not evaluated.

This is a

short-circuiting
terminal operation

.

This is a

short-circuiting
terminal operation

.

findFirst

```java
OptionalLong
findFirst()
```

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty. If the
stream has no encounter order, then any element may be returned.

This is a

short-circuiting
terminal operation

.

**Returns:** an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty

---

#### findFirst

OptionalLong

findFirst()

Returns an

OptionalLong

describing the first element of this
stream, or an empty

OptionalLong

if the stream is empty. If the
stream has no encounter order, then any element may be returned.

This is a

short-circuiting
terminal operation

.

This is a

short-circuiting
terminal operation

.

findAny

```java
OptionalLong
findAny()
```

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

This is a

short-circuiting
terminal operation

.

The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use

findFirst()

instead.)

**Returns:** an

OptionalLong

describing some element of this stream,
or an empty

OptionalLong

if the stream is empty
**See Also:** findFirst()

---

#### findAny

OptionalLong

findAny()

Returns an

OptionalLong

describing some element of the stream, or
an empty

OptionalLong

if the stream is empty.

This is a

short-circuiting
terminal operation

.

The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use

findFirst()

instead.)

This is a

short-circuiting
terminal operation

.

The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use

findFirst()

instead.)

The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use

findFirst()

instead.)

asDoubleStream

```java
DoubleStream
asDoubleStream()
```

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

This is an

intermediate
operation

.

**Returns:** a

DoubleStream

consisting of the elements of this stream,
converted to

double

---

#### asDoubleStream

DoubleStream

asDoubleStream()

Returns a

DoubleStream

consisting of the elements of this stream,
converted to

double

.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

boxed

```java
Stream
<
Long
> boxed()
```

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

This is an

intermediate
operation

.

**Returns:** a

Stream

consistent of the elements of this stream,
each boxed to

Long

---

#### boxed

Stream

<

Long

> boxed()

Returns a

Stream

consisting of the elements of this stream,
each boxed to a

Long

.

This is an

intermediate
operation

.

This is an

intermediate
operation

.

builder

```java
static
LongStream.Builder
builder()
```

Returns a builder for a

LongStream

.

**Returns:** a stream builder

---

#### builder

static

LongStream.Builder

builder()

Returns a builder for a

LongStream

.

empty

```java
static
LongStream
empty()
```

Returns an empty sequential

LongStream

.

**Returns:** an empty sequential stream

---

#### empty

static

LongStream

empty()

Returns an empty sequential

LongStream

.

of

```java
static
LongStream
of​(long t)
```

Returns a sequential

LongStream

containing a single element.

**Parameters:** t

- the single element
**Returns:** a singleton sequential stream

---

#### of

static

LongStream

of​(long t)

Returns a sequential

LongStream

containing a single element.

of

```java
static
LongStream
of​(long... values)
```

Returns a sequential ordered stream whose elements are the specified values.

**Parameters:** values

- the elements of the new stream
**Returns:** the new stream

---

#### of

static

LongStream

of​(long... values)

Returns a sequential ordered stream whose elements are the specified values.

iterate

```java
static
LongStream
iterate​(long seed,

LongUnaryOperator
f)
```

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

The first element (position

0

) in the

LongStream

will
be the provided

seed

. For

n > 0

, the element at position

n

, will be the result of applying the function

f

to the
element at position

n - 1

.

The action of applying

f

for one element

happens-before

the action of applying

f

for subsequent elements. For any given
element the action may be performed in whatever thread the library
chooses.

**Parameters:** seed

- the initial element
**Parameters:** f

- a function to be applied to the previous element to produce
a new element
**Returns:** a new sequential

LongStream

---

#### iterate

static

LongStream

iterate​(long seed,

LongUnaryOperator

f)

Returns an infinite sequential ordered

LongStream

produced by iterative
application of a function

f

to an initial element

seed

,
producing a

Stream

consisting of

seed

,

f(seed)

,

f(f(seed))

, etc.

The first element (position

0

) in the

LongStream

will
be the provided

seed

. For

n > 0

, the element at position

n

, will be the result of applying the function

f

to the
element at position

n - 1

.

The action of applying

f

for one element

happens-before

the action of applying

f

for subsequent elements. For any given
element the action may be performed in whatever thread the library
chooses.

The first element (position

0

) in the

LongStream

will
be the provided

seed

. For

n > 0

, the element at position

n

, will be the result of applying the function

f

to the
element at position

n - 1

.

The action of applying

f

for one element

happens-before

the action of applying

f

for subsequent elements. For any given
element the action may be performed in whatever thread the library
chooses.

The action of applying

f

for one element

happens-before

the action of applying

f

for subsequent elements. For any given
element the action may be performed in whatever thread the library
chooses.

iterate

```java
static
LongStream
iterate​(long seed,

LongPredicate
hasNext,

LongUnaryOperator
next)
```

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate. The
stream terminates as soon as the

hasNext

predicate returns false.

LongStream.iterate

should produce the same sequence of elements as
produced by the corresponding for-loop:

```java
for (long index=seed; hasNext.test(index); index = next.applyAsLong(index)) {
...
}
```

The resulting sequence may be empty if the

hasNext

predicate
does not hold on the seed value. Otherwise the first element will be the
supplied

seed

value, the next element (if present) will be the
result of applying the

next

function to the

seed

value,
and so on iteratively until the

hasNext

predicate indicates that
the stream should terminate.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

**Parameters:** seed

- the initial element
**Parameters:** hasNext

- a predicate to apply to elements to determine when the
stream must terminate.
**Parameters:** next

- a function to be applied to the previous element to produce
a new element
**Returns:** a new sequential

LongStream
**Since:** 9

---

#### iterate

static

LongStream

iterate​(long seed,

LongPredicate

hasNext,

LongUnaryOperator

next)

Returns a sequential ordered

LongStream

produced by iterative
application of the given

next

function to an initial element,
conditioned on satisfying the given

hasNext

predicate. The
stream terminates as soon as the

hasNext

predicate returns false.

LongStream.iterate

should produce the same sequence of elements as
produced by the corresponding for-loop:

```java
for (long index=seed; hasNext.test(index); index = next.applyAsLong(index)) {
...
}
```

The resulting sequence may be empty if the

hasNext

predicate
does not hold on the seed value. Otherwise the first element will be the
supplied

seed

value, the next element (if present) will be the
result of applying the

next

function to the

seed

value,
and so on iteratively until the

hasNext

predicate indicates that
the stream should terminate.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

LongStream.iterate

should produce the same sequence of elements as
produced by the corresponding for-loop:

```java
for (long index=seed; hasNext.test(index); index = next.applyAsLong(index)) {
...
}
```

The resulting sequence may be empty if the

hasNext

predicate
does not hold on the seed value. Otherwise the first element will be the
supplied

seed

value, the next element (if present) will be the
result of applying the

next

function to the

seed

value,
and so on iteratively until the

hasNext

predicate indicates that
the stream should terminate.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

for (long index=seed; hasNext.test(index); index = next.applyAsLong(index)) {
...
}

The resulting sequence may be empty if the

hasNext

predicate
does not hold on the seed value. Otherwise the first element will be the
supplied

seed

value, the next element (if present) will be the
result of applying the

next

function to the

seed

value,
and so on iteratively until the

hasNext

predicate indicates that
the stream should terminate.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

The action of applying the

hasNext

predicate to an element

happens-before

the action of applying the

next

function to that element. The
action of applying the

next

function for one element

happens-before

the action of applying the

hasNext

predicate for subsequent elements. For any given element an action may
be performed in whatever thread the library chooses.

generate

```java
static
LongStream
generate​(
LongSupplier
s)
```

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

. This is suitable for
generating constant streams, streams of random elements, etc.

**Parameters:** s

- the

LongSupplier

for generated elements
**Returns:** a new infinite sequential unordered

LongStream

---

#### generate

static

LongStream

generate​(

LongSupplier

s)

Returns an infinite sequential unordered stream where each element is
generated by the provided

LongSupplier

. This is suitable for
generating constant streams, streams of random elements, etc.

range

```java
static
LongStream
range​(long startInclusive,
long endExclusive)
```

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

**API Note:** An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i < endExclusive ; i++) { ... }
```
**Parameters:** startInclusive

- the (inclusive) initial value
**Parameters:** endExclusive

- the exclusive upper bound
**Returns:** a sequential

LongStream

for the range of

long

elements

---

#### range

static

LongStream

range​(long startInclusive,
long endExclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endExclusive

(exclusive) by an incremental step of

1

.

An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i < endExclusive ; i++) { ... }
```

for (long i = startInclusive; i < endExclusive ; i++) { ... }

rangeClosed

```java
static
LongStream
rangeClosed​(long startInclusive,
long endInclusive)
```

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

**API Note:** An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i <= endInclusive ; i++) { ... }
```
**Parameters:** startInclusive

- the (inclusive) initial value
**Parameters:** endInclusive

- the inclusive upper bound
**Returns:** a sequential

LongStream

for the range of

long

elements

---

#### rangeClosed

static

LongStream

rangeClosed​(long startInclusive,
long endInclusive)

Returns a sequential ordered

LongStream

from

startInclusive

(inclusive) to

endInclusive

(inclusive) by an incremental step of

1

.

An equivalent sequence of increasing values can be produced
sequentially using a

for

loop as follows:

```java
for (long i = startInclusive; i <= endInclusive ; i++) { ... }
```

for (long i = startInclusive; i <= endInclusive ; i++) { ... }

concat

```java
static
LongStream
concat​(
LongStream
a,

LongStream
b)
```

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream. The resulting stream is ordered if both
of the input streams are ordered, and parallel if either of the input
streams is parallel. When the resulting stream is closed, the close
handlers for both input streams are invoked.

This method operates on the two input streams and binds each stream
to its source. As a result subsequent modifications to an input stream
source may not be reflected in the concatenated stream result.

**API Note:** To preserve optimization opportunities this method binds each stream to
its source and accepts only two streams as parameters. For example, the
exact size of the concatenated stream source can be computed if the exact
size of each input stream source is known.
To concatenate more streams without binding, or without nested calls to
this method, try creating a stream of streams and flat-mapping with the
identity function, for example:

```java
LongStream concat = Stream.of(s1, s2, s3, s4).flatMapToLong(s -> s);
```
**Implementation Note:** Use caution when constructing streams from repeated concatenation.
Accessing an element of a deeply concatenated stream can result in deep
call chains, or even

StackOverflowError

.
**Parameters:** a

- the first stream
**Parameters:** b

- the second stream
**Returns:** the concatenation of the two input streams

---

#### concat

static

LongStream

concat​(

LongStream

a,

LongStream

b)

Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream. The resulting stream is ordered if both
of the input streams are ordered, and parallel if either of the input
streams is parallel. When the resulting stream is closed, the close
handlers for both input streams are invoked.

This method operates on the two input streams and binds each stream
to its source. As a result subsequent modifications to an input stream
source may not be reflected in the concatenated stream result.

This method operates on the two input streams and binds each stream
to its source. As a result subsequent modifications to an input stream
source may not be reflected in the concatenated stream result.

LongStream concat = Stream.of(s1, s2, s3, s4).flatMapToLong(s -> s);

---

