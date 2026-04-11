# Class SubmissionPublisher<T>

**Source:** `java.base\java\util\concurrent\SubmissionPublisher.html`

### Class Description

```java
public class
SubmissionPublisher<T>

extends
Object

implements
Flow.Publisher
<T>,
AutoCloseable
```

A

Flow.Publisher

that asynchronously issues submitted
(non-null) items to current subscribers until it is closed. Each
current subscriber receives newly submitted items in the same order
unless drops or exceptions are encountered. Using a
SubmissionPublisher allows item generators to act as compliant

reactive-streams

Publishers relying on drop handling and/or blocking for flow
control.

A SubmissionPublisher uses the

Executor

supplied in its
constructor for delivery to subscribers. The best choice of
Executor depends on expected usage. If the generator(s) of
submitted items run in separate threads, and the number of
subscribers can be estimated, consider using a

Executors.newFixedThreadPool(int)

. Otherwise consider using the
default, normally the

ForkJoinPool.commonPool()

.

Buffering allows producers and consumers to transiently operate
at different rates. Each subscriber uses an independent buffer.
Buffers are created upon first use and expanded as needed up to the
given maximum. (The enforced capacity may be rounded up to the
nearest power of two and/or bounded by the largest value supported
by this implementation.) Invocations of

request

do not directly result in
buffer expansion, but risk saturation if unfilled requests exceed
the maximum capacity. The default value of

Flow.defaultBufferSize()

may provide a useful starting point for
choosing a capacity based on expected rates, resources, and usages.

A single SubmissionPublisher may be shared among multiple
sources. Actions in a source thread prior to publishing an item or
issuing a signal

happen-before

actions subsequent to the corresponding
access by each subscriber. But reported estimates of lag and demand
are designed for use in monitoring, not for synchronization
control, and may reflect stale or inaccurate views of progress.

Publication methods support different policies about what to do
when buffers are saturated. Method

submit

blocks until resources are available. This is simplest, but least
responsive. The

offer

methods may drop items (either
immediately or with bounded timeout), but provide an opportunity to
interpose a handler and then retry.

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

**Type Parameters:** T

- the published item type

---

### Field Details

*No entries found.*

### Constructor Details

#### public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity,

BiConsumer
<? super
Flow.Subscriber
<? super
T
>,​? super
Throwable
> handler)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

**Parameters:**
- executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
- maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)
- handler

- if non-null, procedure to invoke upon exception
thrown in method

onNext

**Throws:**
- NullPointerException

- if executor is null
- IllegalArgumentException

- if maxBufferCapacity not
positive

---

#### public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

**Parameters:**
- executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
- maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)

**Throws:**
- NullPointerException

- if executor is null
- IllegalArgumentException

- if maxBufferCapacity not
positive

---

#### public SubmissionPublisher()

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

---

### Method Details

#### public void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)

Adds the given Subscriber unless already subscribed. If already
subscribed, the Subscriber's

onError

method is invoked on
the existing subscription with an

IllegalStateException

.
Otherwise, upon success, the Subscriber's

onSubscribe

method is invoked
asynchronously with a new

Flow.Subscription

. If

onSubscribe

throws an exception, the
subscription is cancelled. Otherwise, if this SubmissionPublisher
was closed exceptionally, then the subscriber's

onError

method is invoked with the
corresponding exception, or if closed without exception, the
subscriber's

onComplete

method is invoked. Subscribers may enable receiving items by
invoking the

request

method of the new Subscription, and may unsubscribe by invoking
its

cancel

method.

**Specified by:**
- subscribe

in interface

Flow.Publisher

<

T

>

**Parameters:**
- subscriber

- the subscriber

**Throws:**
- NullPointerException

- if subscriber is null

---

#### public int submit​(
T
item)

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable. This method returns an estimate of
the maximum lag (number of items submitted but not yet consumed)
among all current subscribers. This value is at least one
(accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers,
then this exception is rethrown, in which case not all
subscribers will have been issued this item.

**Parameters:**
- item

- the (non-null) item to publish

**Returns:**
- the estimated maximum lag among subscribers

**Throws:**
- IllegalStateException

- if closed
- NullPointerException

- if item is null
- RejectedExecutionException

- if thrown by Executor

---

#### public int offer​(
T
item,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method. The item may be
dropped by one or more subscribers if resource limits are
exceeded, in which case the given handler (if non-null) is
invoked, and if it returns true, retried once. Other calls to
methods in this class by other threads are blocked while the
handler is invoked. Unless recovery is assured, options are
usually limited to logging the error and/or issuing an

onError

signal to the
subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:**
- item

- the (non-null) item to publish
- onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)

**Returns:**
- if negative, the (negative) number of drops; otherwise
an estimate of maximum lag

**Throws:**
- IllegalStateException

- if closed
- NullPointerException

- if item is null
- RejectedExecutionException

- if thrown by Executor

---

#### public int offer​(
T
item,
long timeout,

TimeUnit
unit,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once. (The drop handler may distinguish
timeouts from interrupts by checking whether the current thread
is interrupted.) Other calls to methods in this class by other
threads are blocked while the handler is invoked. Unless
recovery is assured, options are usually limited to logging the
error and/or issuing an

onError

signal to the subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:**
- item

- the (non-null) item to publish
- timeout

- how long to wait for resources for any subscriber
before giving up, in units of

unit
- unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
- onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)

**Returns:**
- if negative, the (negative) number of drops; otherwise
an estimate of maximum lag

**Throws:**
- IllegalStateException

- if closed
- NullPointerException

- if item is null
- RejectedExecutionException

- if thrown by Executor

---

#### public void close()

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.
Upon return, this method does

NOT

guarantee that all
subscribers have yet completed.

**Specified by:**
- close

in interface

AutoCloseable

---

#### public void closeExceptionally​(
Throwable
error)

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish. Future subscribers also receive the given
error. Upon return, this method does

NOT

guarantee
that all subscribers have yet completed.

**Parameters:**
- error

- the

onError

argument sent to subscribers

**Throws:**
- NullPointerException

- if error is null

---

#### public boolean isClosed()

Returns true if this publisher is not accepting submissions.

**Returns:**
- true if closed

---

#### public
Throwable
getClosedException()

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

**Returns:**
- the exception, or null if none

---

#### public boolean hasSubscribers()

Returns true if this publisher has any subscribers.

**Returns:**
- true if this publisher has any subscribers

---

#### public int getNumberOfSubscribers()

Returns the number of current subscribers.

**Returns:**
- the number of current subscribers

---

#### public
Executor
getExecutor()

Returns the Executor used for asynchronous delivery.

**Returns:**
- the Executor used for asynchronous delivery

---

#### public int getMaxBufferCapacity()

Returns the maximum per-subscriber buffer capacity.

**Returns:**
- the maximum per-subscriber buffer capacity

---

#### public
List
<
Flow.Subscriber
<? super
T
>> getSubscribers()

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

**Returns:**
- list of current subscribers

---

#### public boolean isSubscribed​(
Flow.Subscriber
<? super
T
> subscriber)

Returns true if the given Subscriber is currently subscribed.

**Parameters:**
- subscriber

- the subscriber

**Returns:**
- true if currently subscribed

**Throws:**
- NullPointerException

- if subscriber is null

---

#### public long estimateMinimumDemand()

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

**Returns:**
- the estimate, or zero if no subscribers

---

#### public int estimateMaximumLag()

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

**Returns:**
- the estimate

---

#### public
CompletableFuture
<
Void
> consume​(
Consumer
<? super
T
> consumer)

Processes all published items using the given Consumer function.
Returns a CompletableFuture that is completed normally when this
publisher signals

onComplete

, or completed exceptionally upon any error, or an
exception is thrown by the Consumer, or the returned
CompletableFuture is cancelled, in which case no further items
are processed.

**Parameters:**
- consumer

- the function applied to each onNext item

**Returns:**
- a CompletableFuture that is completed normally
when the publisher signals onComplete, and exceptionally
upon any error or cancellation

**Throws:**
- NullPointerException

- if consumer is null

---

### Additional Sections

#### Class SubmissionPublisher<T>

java.lang.Object

- java.util.concurrent.SubmissionPublisher<T>

java.util.concurrent.SubmissionPublisher<T>

**Type Parameters:** T

- the published item type

**All Implemented Interfaces:** AutoCloseable

,

Flow.Publisher

<T>

```java
public class
SubmissionPublisher<T>

extends
Object

implements
Flow.Publisher
<T>,
AutoCloseable
```

A

Flow.Publisher

that asynchronously issues submitted
(non-null) items to current subscribers until it is closed. Each
current subscriber receives newly submitted items in the same order
unless drops or exceptions are encountered. Using a
SubmissionPublisher allows item generators to act as compliant

reactive-streams

Publishers relying on drop handling and/or blocking for flow
control.

A SubmissionPublisher uses the

Executor

supplied in its
constructor for delivery to subscribers. The best choice of
Executor depends on expected usage. If the generator(s) of
submitted items run in separate threads, and the number of
subscribers can be estimated, consider using a

Executors.newFixedThreadPool(int)

. Otherwise consider using the
default, normally the

ForkJoinPool.commonPool()

.

Buffering allows producers and consumers to transiently operate
at different rates. Each subscriber uses an independent buffer.
Buffers are created upon first use and expanded as needed up to the
given maximum. (The enforced capacity may be rounded up to the
nearest power of two and/or bounded by the largest value supported
by this implementation.) Invocations of

request

do not directly result in
buffer expansion, but risk saturation if unfilled requests exceed
the maximum capacity. The default value of

Flow.defaultBufferSize()

may provide a useful starting point for
choosing a capacity based on expected rates, resources, and usages.

A single SubmissionPublisher may be shared among multiple
sources. Actions in a source thread prior to publishing an item or
issuing a signal

happen-before

actions subsequent to the corresponding
access by each subscriber. But reported estimates of lag and demand
are designed for use in monitoring, not for synchronization
control, and may reflect stale or inaccurate views of progress.

Publication methods support different policies about what to do
when buffers are saturated. Method

submit

blocks until resources are available. This is simplest, but least
responsive. The

offer

methods may drop items (either
immediately or with bounded timeout), but provide an opportunity to
interpose a handler and then retry.

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

**Since:** 9

public class

SubmissionPublisher<T>

extends

Object

implements

Flow.Publisher

<T>,

AutoCloseable

A

Flow.Publisher

that asynchronously issues submitted
(non-null) items to current subscribers until it is closed. Each
current subscriber receives newly submitted items in the same order
unless drops or exceptions are encountered. Using a
SubmissionPublisher allows item generators to act as compliant

reactive-streams

Publishers relying on drop handling and/or blocking for flow
control.

A SubmissionPublisher uses the

Executor

supplied in its
constructor for delivery to subscribers. The best choice of
Executor depends on expected usage. If the generator(s) of
submitted items run in separate threads, and the number of
subscribers can be estimated, consider using a

Executors.newFixedThreadPool(int)

. Otherwise consider using the
default, normally the

ForkJoinPool.commonPool()

.

Buffering allows producers and consumers to transiently operate
at different rates. Each subscriber uses an independent buffer.
Buffers are created upon first use and expanded as needed up to the
given maximum. (The enforced capacity may be rounded up to the
nearest power of two and/or bounded by the largest value supported
by this implementation.) Invocations of

request

do not directly result in
buffer expansion, but risk saturation if unfilled requests exceed
the maximum capacity. The default value of

Flow.defaultBufferSize()

may provide a useful starting point for
choosing a capacity based on expected rates, resources, and usages.

A single SubmissionPublisher may be shared among multiple
sources. Actions in a source thread prior to publishing an item or
issuing a signal

happen-before

actions subsequent to the corresponding
access by each subscriber. But reported estimates of lag and demand
are designed for use in monitoring, not for synchronization
control, and may reflect stale or inaccurate views of progress.

Publication methods support different policies about what to do
when buffers are saturated. Method

submit

blocks until resources are available. This is simplest, but least
responsive. The

offer

methods may drop items (either
immediately or with bounded timeout), but provide an opportunity to
interpose a handler and then retry.

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

A SubmissionPublisher uses the

Executor

supplied in its
constructor for delivery to subscribers. The best choice of
Executor depends on expected usage. If the generator(s) of
submitted items run in separate threads, and the number of
subscribers can be estimated, consider using a

Executors.newFixedThreadPool(int)

. Otherwise consider using the
default, normally the

ForkJoinPool.commonPool()

.

Buffering allows producers and consumers to transiently operate
at different rates. Each subscriber uses an independent buffer.
Buffers are created upon first use and expanded as needed up to the
given maximum. (The enforced capacity may be rounded up to the
nearest power of two and/or bounded by the largest value supported
by this implementation.) Invocations of

request

do not directly result in
buffer expansion, but risk saturation if unfilled requests exceed
the maximum capacity. The default value of

Flow.defaultBufferSize()

may provide a useful starting point for
choosing a capacity based on expected rates, resources, and usages.

A single SubmissionPublisher may be shared among multiple
sources. Actions in a source thread prior to publishing an item or
issuing a signal

happen-before

actions subsequent to the corresponding
access by each subscriber. But reported estimates of lag and demand
are designed for use in monitoring, not for synchronization
control, and may reflect stale or inaccurate views of progress.

Publication methods support different policies about what to do
when buffers are saturated. Method

submit

blocks until resources are available. This is simplest, but least
responsive. The

offer

methods may drop items (either
immediately or with bounded timeout), but provide an opportunity to
interpose a handler and then retry.

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

Buffering allows producers and consumers to transiently operate
at different rates. Each subscriber uses an independent buffer.
Buffers are created upon first use and expanded as needed up to the
given maximum. (The enforced capacity may be rounded up to the
nearest power of two and/or bounded by the largest value supported
by this implementation.) Invocations of

request

do not directly result in
buffer expansion, but risk saturation if unfilled requests exceed
the maximum capacity. The default value of

Flow.defaultBufferSize()

may provide a useful starting point for
choosing a capacity based on expected rates, resources, and usages.

A single SubmissionPublisher may be shared among multiple
sources. Actions in a source thread prior to publishing an item or
issuing a signal

happen-before

actions subsequent to the corresponding
access by each subscriber. But reported estimates of lag and demand
are designed for use in monitoring, not for synchronization
control, and may reflect stale or inaccurate views of progress.

Publication methods support different policies about what to do
when buffers are saturated. Method

submit

blocks until resources are available. This is simplest, but least
responsive. The

offer

methods may drop items (either
immediately or with bounded timeout), but provide an opportunity to
interpose a handler and then retry.

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

A single SubmissionPublisher may be shared among multiple
sources. Actions in a source thread prior to publishing an item or
issuing a signal

happen-before

actions subsequent to the corresponding
access by each subscriber. But reported estimates of lag and demand
are designed for use in monitoring, not for synchronization
control, and may reflect stale or inaccurate views of progress.

Publication methods support different policies about what to do
when buffers are saturated. Method

submit

blocks until resources are available. This is simplest, but least
responsive. The

offer

methods may drop items (either
immediately or with bounded timeout), but provide an opportunity to
interpose a handler and then retry.

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

Publication methods support different policies about what to do
when buffers are saturated. Method

submit

blocks until resources are available. This is simplest, but least
responsive. The

offer

methods may drop items (either
immediately or with bounded timeout), but provide an opportunity to
interpose a handler and then retry.

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

If any Subscriber method throws an exception, its subscription
is cancelled. If a handler is supplied as a constructor argument,
it is invoked before cancellation upon an exception in method

onNext

, but exceptions in methods

onSubscribe

,

onError

and

onComplete

are not recorded or
handled before cancellation. If the supplied Executor throws

RejectedExecutionException

(or any other RuntimeException
or Error) when attempting to execute a task, or a drop handler
throws an exception when processing a dropped item, then the
exception is rethrown. In these cases, not all subscribers will
have been issued the published item. It is usually good practice to

closeExceptionally

in these cases.

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

Method

consume(Consumer)

simplifies support for a
common case in which the only action of a subscriber is to request
and process all items using a supplied function.

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

This class may also serve as a convenient base for subclasses
that generate items, and use the methods in this class to publish
them. For example here is a class that periodically publishes the
items generated from a supplier. (In practice you might add methods
to independently start and stop generation, to share Executors
among publishers, and so on, or use a SubmissionPublisher as a
component rather than a superclass.)

```java
class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}
```

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

class PeriodicPublisher<T> extends SubmissionPublisher<T> {
final ScheduledFuture<?> periodicTask;
final ScheduledExecutorService scheduler;
PeriodicPublisher(Executor executor, int maxBufferCapacity,
Supplier<? extends T> supplier,
long period, TimeUnit unit) {
super(executor, maxBufferCapacity);
scheduler = new ScheduledThreadPoolExecutor(1);
periodicTask = scheduler.scheduleAtFixedRate(
() -> submit(supplier.get()), 0, period, unit);
}
public void close() {
periodicTask.cancel(false);
scheduler.shutdown();
super.close();
}
}

Here is an example of a

Flow.Processor

implementation.
It uses single-step requests to its publisher for simplicity of
illustration. A more adaptive version could monitor flow using the
lag estimate returned from

submit

, along with other utility
methods.

```java
class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}
```

class TransformProcessor<S,T> extends SubmissionPublisher<T>
implements Flow.Processor<S,T> {
final Function<? super S, ? extends T> function;
Flow.Subscription subscription;
TransformProcessor(Executor executor, int maxBufferCapacity,
Function<? super S, ? extends T> function) {
super(executor, maxBufferCapacity);
this.function = function;
}
public void onSubscribe(Flow.Subscription subscription) {
(this.subscription = subscription).request(1);
}
public void onNext(S item) {
subscription.request(1);
submit(function.apply(item));
}
public void onError(Throwable ex) { closeExceptionally(ex); }
public void onComplete() { close(); }
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SubmissionPublisher

()

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

SubmissionPublisher

​(

Executor

executor,
int maxBufferCapacity)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

SubmissionPublisher

​(

Executor

executor,
int maxBufferCapacity,

BiConsumer

<? super

Flow.Subscriber

<? super

T

>,​? super

Throwable

> handler)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.

void

closeExceptionally

​(

Throwable

error)

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish.

CompletableFuture

<

Void

>

consume

​(

Consumer

<? super

T

> consumer)

Processes all published items using the given Consumer function.

int

estimateMaximumLag

()

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

long

estimateMinimumDemand

()

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

Throwable

getClosedException

()

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

Executor

getExecutor

()

Returns the Executor used for asynchronous delivery.

int

getMaxBufferCapacity

()

Returns the maximum per-subscriber buffer capacity.

int

getNumberOfSubscribers

()

Returns the number of current subscribers.

List

<

Flow.Subscriber

<? super

T

>>

getSubscribers

()

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

boolean

hasSubscribers

()

Returns true if this publisher has any subscribers.

boolean

isClosed

()

Returns true if this publisher is not accepting submissions.

boolean

isSubscribed

​(

Flow.Subscriber

<? super

T

> subscriber)

Returns true if the given Subscriber is currently subscribed.

int

offer

​(

T

item,
long timeout,

TimeUnit

unit,

BiPredicate

<

Flow.Subscriber

<? super

T

>,​? super

T

> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once.

int

offer

​(

T

item,

BiPredicate

<

Flow.Subscriber

<? super

T

>,​? super

T

> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method.

int

submit

​(

T

item)

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable.

void

subscribe

​(

Flow.Subscriber

<? super

T

> subscriber)

Adds the given Subscriber unless already subscribed.

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

Constructor

Description

SubmissionPublisher

()

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

SubmissionPublisher

​(

Executor

executor,
int maxBufferCapacity)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

SubmissionPublisher

​(

Executor

executor,
int maxBufferCapacity,

BiConsumer

<? super

Flow.Subscriber

<? super

T

>,​? super

Throwable

> handler)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

---

#### Constructor Summary

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.

void

closeExceptionally

​(

Throwable

error)

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish.

CompletableFuture

<

Void

>

consume

​(

Consumer

<? super

T

> consumer)

Processes all published items using the given Consumer function.

int

estimateMaximumLag

()

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

long

estimateMinimumDemand

()

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

Throwable

getClosedException

()

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

Executor

getExecutor

()

Returns the Executor used for asynchronous delivery.

int

getMaxBufferCapacity

()

Returns the maximum per-subscriber buffer capacity.

int

getNumberOfSubscribers

()

Returns the number of current subscribers.

List

<

Flow.Subscriber

<? super

T

>>

getSubscribers

()

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

boolean

hasSubscribers

()

Returns true if this publisher has any subscribers.

boolean

isClosed

()

Returns true if this publisher is not accepting submissions.

boolean

isSubscribed

​(

Flow.Subscriber

<? super

T

> subscriber)

Returns true if the given Subscriber is currently subscribed.

int

offer

​(

T

item,
long timeout,

TimeUnit

unit,

BiPredicate

<

Flow.Subscriber

<? super

T

>,​? super

T

> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once.

int

offer

​(

T

item,

BiPredicate

<

Flow.Subscriber

<? super

T

>,​? super

T

> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method.

int

submit

​(

T

item)

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable.

void

subscribe

​(

Flow.Subscriber

<? super

T

> subscriber)

Adds the given Subscriber unless already subscribed.

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

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish.

Processes all published items using the given Consumer function.

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

Returns the Executor used for asynchronous delivery.

Returns the maximum per-subscriber buffer capacity.

Returns the number of current subscribers.

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

Returns true if this publisher has any subscribers.

Returns true if this publisher is not accepting submissions.

Returns true if the given Subscriber is currently subscribed.

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once.

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method.

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable.

Adds the given Subscriber unless already subscribed.

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

- SubmissionPublisher

```java
public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity,

BiConsumer
<? super
Flow.Subscriber
<? super
T
>,​? super
Throwable
> handler)
```

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

**Parameters:** executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
**Parameters:** maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)
**Parameters:** handler

- if non-null, procedure to invoke upon exception
thrown in method

onNext
**Throws:** NullPointerException

- if executor is null
**Throws:** IllegalArgumentException

- if maxBufferCapacity not
positive

- SubmissionPublisher

```java
public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity)
```

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

**Parameters:** executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
**Parameters:** maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)
**Throws:** NullPointerException

- if executor is null
**Throws:** IllegalArgumentException

- if maxBufferCapacity not
positive

- SubmissionPublisher

```java
public SubmissionPublisher()
```

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

============ METHOD DETAIL ==========

- Method Detail

- subscribe

```java
public void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)
```

Adds the given Subscriber unless already subscribed. If already
subscribed, the Subscriber's

onError

method is invoked on
the existing subscription with an

IllegalStateException

.
Otherwise, upon success, the Subscriber's

onSubscribe

method is invoked
asynchronously with a new

Flow.Subscription

. If

onSubscribe

throws an exception, the
subscription is cancelled. Otherwise, if this SubmissionPublisher
was closed exceptionally, then the subscriber's

onError

method is invoked with the
corresponding exception, or if closed without exception, the
subscriber's

onComplete

method is invoked. Subscribers may enable receiving items by
invoking the

request

method of the new Subscription, and may unsubscribe by invoking
its

cancel

method.

**Specified by:** subscribe

in interface

Flow.Publisher

<

T

>
**Parameters:** subscriber

- the subscriber
**Throws:** NullPointerException

- if subscriber is null

- submit

```java
public int submit​(
T
item)
```

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable. This method returns an estimate of
the maximum lag (number of items submitted but not yet consumed)
among all current subscribers. This value is at least one
(accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers,
then this exception is rethrown, in which case not all
subscribers will have been issued this item.

**Parameters:** item

- the (non-null) item to publish
**Returns:** the estimated maximum lag among subscribers
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

- offer

```java
public int offer​(
T
item,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)
```

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method. The item may be
dropped by one or more subscribers if resource limits are
exceeded, in which case the given handler (if non-null) is
invoked, and if it returns true, retried once. Other calls to
methods in this class by other threads are blocked while the
handler is invoked. Unless recovery is assured, options are
usually limited to logging the error and/or issuing an

onError

signal to the
subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:** item

- the (non-null) item to publish
**Parameters:** onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)
**Returns:** if negative, the (negative) number of drops; otherwise
an estimate of maximum lag
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

- offer

```java
public int offer​(
T
item,
long timeout,

TimeUnit
unit,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)
```

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once. (The drop handler may distinguish
timeouts from interrupts by checking whether the current thread
is interrupted.) Other calls to methods in this class by other
threads are blocked while the handler is invoked. Unless
recovery is assured, options are usually limited to logging the
error and/or issuing an

onError

signal to the subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:** item

- the (non-null) item to publish
**Parameters:** timeout

- how long to wait for resources for any subscriber
before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Parameters:** onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)
**Returns:** if negative, the (negative) number of drops; otherwise
an estimate of maximum lag
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

- close

```java
public void close()
```

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.
Upon return, this method does

NOT

guarantee that all
subscribers have yet completed.

**Specified by:** close

in interface

AutoCloseable

- closeExceptionally

```java
public void closeExceptionally​(
Throwable
error)
```

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish. Future subscribers also receive the given
error. Upon return, this method does

NOT

guarantee
that all subscribers have yet completed.

**Parameters:** error

- the

onError

argument sent to subscribers
**Throws:** NullPointerException

- if error is null

- isClosed

```java
public boolean isClosed()
```

Returns true if this publisher is not accepting submissions.

**Returns:** true if closed

- getClosedException

```java
public
Throwable
getClosedException()
```

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

**Returns:** the exception, or null if none

- hasSubscribers

```java
public boolean hasSubscribers()
```

Returns true if this publisher has any subscribers.

**Returns:** true if this publisher has any subscribers

- getNumberOfSubscribers

```java
public int getNumberOfSubscribers()
```

Returns the number of current subscribers.

**Returns:** the number of current subscribers

- getExecutor

```java
public
Executor
getExecutor()
```

Returns the Executor used for asynchronous delivery.

**Returns:** the Executor used for asynchronous delivery

- getMaxBufferCapacity

```java
public int getMaxBufferCapacity()
```

Returns the maximum per-subscriber buffer capacity.

**Returns:** the maximum per-subscriber buffer capacity

- getSubscribers

```java
public
List
<
Flow.Subscriber
<? super
T
>> getSubscribers()
```

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

**Returns:** list of current subscribers

- isSubscribed

```java
public boolean isSubscribed​(
Flow.Subscriber
<? super
T
> subscriber)
```

Returns true if the given Subscriber is currently subscribed.

**Parameters:** subscriber

- the subscriber
**Returns:** true if currently subscribed
**Throws:** NullPointerException

- if subscriber is null

- estimateMinimumDemand

```java
public long estimateMinimumDemand()
```

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

**Returns:** the estimate, or zero if no subscribers

- estimateMaximumLag

```java
public int estimateMaximumLag()
```

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

**Returns:** the estimate

- consume

```java
public
CompletableFuture
<
Void
> consume​(
Consumer
<? super
T
> consumer)
```

Processes all published items using the given Consumer function.
Returns a CompletableFuture that is completed normally when this
publisher signals

onComplete

, or completed exceptionally upon any error, or an
exception is thrown by the Consumer, or the returned
CompletableFuture is cancelled, in which case no further items
are processed.

**Parameters:** consumer

- the function applied to each onNext item
**Returns:** a CompletableFuture that is completed normally
when the publisher signals onComplete, and exceptionally
upon any error or cancellation
**Throws:** NullPointerException

- if consumer is null

Constructor Detail

- SubmissionPublisher

```java
public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity,

BiConsumer
<? super
Flow.Subscriber
<? super
T
>,​? super
Throwable
> handler)
```

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

**Parameters:** executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
**Parameters:** maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)
**Parameters:** handler

- if non-null, procedure to invoke upon exception
thrown in method

onNext
**Throws:** NullPointerException

- if executor is null
**Throws:** IllegalArgumentException

- if maxBufferCapacity not
positive

- SubmissionPublisher

```java
public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity)
```

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

**Parameters:** executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
**Parameters:** maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)
**Throws:** NullPointerException

- if executor is null
**Throws:** IllegalArgumentException

- if maxBufferCapacity not
positive

- SubmissionPublisher

```java
public SubmissionPublisher()
```

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

---

#### Constructor Detail

SubmissionPublisher

```java
public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity,

BiConsumer
<? super
Flow.Subscriber
<? super
T
>,​? super
Throwable
> handler)
```

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

**Parameters:** executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
**Parameters:** maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)
**Parameters:** handler

- if non-null, procedure to invoke upon exception
thrown in method

onNext
**Throws:** NullPointerException

- if executor is null
**Throws:** IllegalArgumentException

- if maxBufferCapacity not
positive

---

#### SubmissionPublisher

public SubmissionPublisher​(

Executor

executor,
int maxBufferCapacity,

BiConsumer

<? super

Flow.Subscriber

<? super

T

>,​? super

Throwable

> handler)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and, if non-null, the given handler invoked
when any Subscriber throws an exception in method

onNext

.

SubmissionPublisher

```java
public SubmissionPublisher​(
Executor
executor,
int maxBufferCapacity)
```

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

**Parameters:** executor

- the executor to use for async delivery,
supporting creation of at least one independent thread
**Parameters:** maxBufferCapacity

- the maximum capacity for each
subscriber's buffer (the enforced capacity may be rounded up to
the nearest power of two and/or bounded by the largest value
supported by this implementation; method

getMaxBufferCapacity()

returns the actual value)
**Throws:** NullPointerException

- if executor is null
**Throws:** IllegalArgumentException

- if maxBufferCapacity not
positive

---

#### SubmissionPublisher

public SubmissionPublisher​(

Executor

executor,
int maxBufferCapacity)

Creates a new SubmissionPublisher using the given Executor for
async delivery to subscribers, with the given maximum buffer size
for each subscriber, and no handler for Subscriber exceptions in
method

onNext

.

SubmissionPublisher

```java
public SubmissionPublisher()
```

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

---

#### SubmissionPublisher

public SubmissionPublisher()

Creates a new SubmissionPublisher using the

ForkJoinPool.commonPool()

for async delivery to subscribers
(unless it does not support a parallelism level of at least two,
in which case, a new Thread is created to run each task), with
maximum buffer capacity of

Flow.defaultBufferSize()

, and no
handler for Subscriber exceptions in method

onNext

.

Method Detail

- subscribe

```java
public void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)
```

Adds the given Subscriber unless already subscribed. If already
subscribed, the Subscriber's

onError

method is invoked on
the existing subscription with an

IllegalStateException

.
Otherwise, upon success, the Subscriber's

onSubscribe

method is invoked
asynchronously with a new

Flow.Subscription

. If

onSubscribe

throws an exception, the
subscription is cancelled. Otherwise, if this SubmissionPublisher
was closed exceptionally, then the subscriber's

onError

method is invoked with the
corresponding exception, or if closed without exception, the
subscriber's

onComplete

method is invoked. Subscribers may enable receiving items by
invoking the

request

method of the new Subscription, and may unsubscribe by invoking
its

cancel

method.

**Specified by:** subscribe

in interface

Flow.Publisher

<

T

>
**Parameters:** subscriber

- the subscriber
**Throws:** NullPointerException

- if subscriber is null

- submit

```java
public int submit​(
T
item)
```

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable. This method returns an estimate of
the maximum lag (number of items submitted but not yet consumed)
among all current subscribers. This value is at least one
(accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers,
then this exception is rethrown, in which case not all
subscribers will have been issued this item.

**Parameters:** item

- the (non-null) item to publish
**Returns:** the estimated maximum lag among subscribers
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

- offer

```java
public int offer​(
T
item,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)
```

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method. The item may be
dropped by one or more subscribers if resource limits are
exceeded, in which case the given handler (if non-null) is
invoked, and if it returns true, retried once. Other calls to
methods in this class by other threads are blocked while the
handler is invoked. Unless recovery is assured, options are
usually limited to logging the error and/or issuing an

onError

signal to the
subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:** item

- the (non-null) item to publish
**Parameters:** onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)
**Returns:** if negative, the (negative) number of drops; otherwise
an estimate of maximum lag
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

- offer

```java
public int offer​(
T
item,
long timeout,

TimeUnit
unit,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)
```

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once. (The drop handler may distinguish
timeouts from interrupts by checking whether the current thread
is interrupted.) Other calls to methods in this class by other
threads are blocked while the handler is invoked. Unless
recovery is assured, options are usually limited to logging the
error and/or issuing an

onError

signal to the subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:** item

- the (non-null) item to publish
**Parameters:** timeout

- how long to wait for resources for any subscriber
before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Parameters:** onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)
**Returns:** if negative, the (negative) number of drops; otherwise
an estimate of maximum lag
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

- close

```java
public void close()
```

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.
Upon return, this method does

NOT

guarantee that all
subscribers have yet completed.

**Specified by:** close

in interface

AutoCloseable

- closeExceptionally

```java
public void closeExceptionally​(
Throwable
error)
```

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish. Future subscribers also receive the given
error. Upon return, this method does

NOT

guarantee
that all subscribers have yet completed.

**Parameters:** error

- the

onError

argument sent to subscribers
**Throws:** NullPointerException

- if error is null

- isClosed

```java
public boolean isClosed()
```

Returns true if this publisher is not accepting submissions.

**Returns:** true if closed

- getClosedException

```java
public
Throwable
getClosedException()
```

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

**Returns:** the exception, or null if none

- hasSubscribers

```java
public boolean hasSubscribers()
```

Returns true if this publisher has any subscribers.

**Returns:** true if this publisher has any subscribers

- getNumberOfSubscribers

```java
public int getNumberOfSubscribers()
```

Returns the number of current subscribers.

**Returns:** the number of current subscribers

- getExecutor

```java
public
Executor
getExecutor()
```

Returns the Executor used for asynchronous delivery.

**Returns:** the Executor used for asynchronous delivery

- getMaxBufferCapacity

```java
public int getMaxBufferCapacity()
```

Returns the maximum per-subscriber buffer capacity.

**Returns:** the maximum per-subscriber buffer capacity

- getSubscribers

```java
public
List
<
Flow.Subscriber
<? super
T
>> getSubscribers()
```

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

**Returns:** list of current subscribers

- isSubscribed

```java
public boolean isSubscribed​(
Flow.Subscriber
<? super
T
> subscriber)
```

Returns true if the given Subscriber is currently subscribed.

**Parameters:** subscriber

- the subscriber
**Returns:** true if currently subscribed
**Throws:** NullPointerException

- if subscriber is null

- estimateMinimumDemand

```java
public long estimateMinimumDemand()
```

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

**Returns:** the estimate, or zero if no subscribers

- estimateMaximumLag

```java
public int estimateMaximumLag()
```

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

**Returns:** the estimate

- consume

```java
public
CompletableFuture
<
Void
> consume​(
Consumer
<? super
T
> consumer)
```

Processes all published items using the given Consumer function.
Returns a CompletableFuture that is completed normally when this
publisher signals

onComplete

, or completed exceptionally upon any error, or an
exception is thrown by the Consumer, or the returned
CompletableFuture is cancelled, in which case no further items
are processed.

**Parameters:** consumer

- the function applied to each onNext item
**Returns:** a CompletableFuture that is completed normally
when the publisher signals onComplete, and exceptionally
upon any error or cancellation
**Throws:** NullPointerException

- if consumer is null

---

#### Method Detail

subscribe

```java
public void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)
```

Adds the given Subscriber unless already subscribed. If already
subscribed, the Subscriber's

onError

method is invoked on
the existing subscription with an

IllegalStateException

.
Otherwise, upon success, the Subscriber's

onSubscribe

method is invoked
asynchronously with a new

Flow.Subscription

. If

onSubscribe

throws an exception, the
subscription is cancelled. Otherwise, if this SubmissionPublisher
was closed exceptionally, then the subscriber's

onError

method is invoked with the
corresponding exception, or if closed without exception, the
subscriber's

onComplete

method is invoked. Subscribers may enable receiving items by
invoking the

request

method of the new Subscription, and may unsubscribe by invoking
its

cancel

method.

**Specified by:** subscribe

in interface

Flow.Publisher

<

T

>
**Parameters:** subscriber

- the subscriber
**Throws:** NullPointerException

- if subscriber is null

---

#### subscribe

public void subscribe​(

Flow.Subscriber

<? super

T

> subscriber)

Adds the given Subscriber unless already subscribed. If already
subscribed, the Subscriber's

onError

method is invoked on
the existing subscription with an

IllegalStateException

.
Otherwise, upon success, the Subscriber's

onSubscribe

method is invoked
asynchronously with a new

Flow.Subscription

. If

onSubscribe

throws an exception, the
subscription is cancelled. Otherwise, if this SubmissionPublisher
was closed exceptionally, then the subscriber's

onError

method is invoked with the
corresponding exception, or if closed without exception, the
subscriber's

onComplete

method is invoked. Subscribers may enable receiving items by
invoking the

request

method of the new Subscription, and may unsubscribe by invoking
its

cancel

method.

submit

```java
public int submit​(
T
item)
```

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable. This method returns an estimate of
the maximum lag (number of items submitted but not yet consumed)
among all current subscribers. This value is at least one
(accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers,
then this exception is rethrown, in which case not all
subscribers will have been issued this item.

**Parameters:** item

- the (non-null) item to publish
**Returns:** the estimated maximum lag among subscribers
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

---

#### submit

public int submit​(

T

item)

Publishes the given item to each current subscriber by
asynchronously invoking its

onNext

method, blocking uninterruptibly while resources for any
subscriber are unavailable. This method returns an estimate of
the maximum lag (number of items submitted but not yet consumed)
among all current subscribers. This value is at least one
(accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers,
then this exception is rethrown, in which case not all
subscribers will have been issued this item.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers,
then this exception is rethrown, in which case not all
subscribers will have been issued this item.

offer

```java
public int offer​(
T
item,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)
```

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method. The item may be
dropped by one or more subscribers if resource limits are
exceeded, in which case the given handler (if non-null) is
invoked, and if it returns true, retried once. Other calls to
methods in this class by other threads are blocked while the
handler is invoked. Unless recovery is assured, options are
usually limited to logging the error and/or issuing an

onError

signal to the
subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:** item

- the (non-null) item to publish
**Parameters:** onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)
**Returns:** if negative, the (negative) number of drops; otherwise
an estimate of maximum lag
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

---

#### offer

public int offer​(

T

item,

BiPredicate

<

Flow.Subscriber

<? super

T

>,​? super

T

> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method. The item may be
dropped by one or more subscribers if resource limits are
exceeded, in which case the given handler (if non-null) is
invoked, and if it returns true, retried once. Other calls to
methods in this class by other threads are blocked while the
handler is invoked. Unless recovery is assured, options are
usually limited to logging the error and/or issuing an

onError

signal to the
subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

offer

```java
public int offer​(
T
item,
long timeout,

TimeUnit
unit,

BiPredicate
<
Flow.Subscriber
<? super
T
>,​? super
T
> onDrop)
```

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once. (The drop handler may distinguish
timeouts from interrupts by checking whether the current thread
is interrupted.) Other calls to methods in this class by other
threads are blocked while the handler is invoked. Unless
recovery is assured, options are usually limited to logging the
error and/or issuing an

onError

signal to the subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

**Parameters:** item

- the (non-null) item to publish
**Parameters:** timeout

- how long to wait for resources for any subscriber
before giving up, in units of

unit
**Parameters:** unit

- a

TimeUnit

determining how to interpret the

timeout

parameter
**Parameters:** onDrop

- if non-null, the handler invoked upon a drop to a
subscriber, with arguments of the subscriber and item; if it
returns true, an offer is re-attempted (once)
**Returns:** if negative, the (negative) number of drops; otherwise
an estimate of maximum lag
**Throws:** IllegalStateException

- if closed
**Throws:** NullPointerException

- if item is null
**Throws:** RejectedExecutionException

- if thrown by Executor

---

#### offer

public int offer​(

T

item,
long timeout,

TimeUnit

unit,

BiPredicate

<

Flow.Subscriber

<? super

T

>,​? super

T

> onDrop)

Publishes the given item, if possible, to each current subscriber
by asynchronously invoking its

onNext

method, blocking while
resources for any subscription are unavailable, up to the
specified timeout or until the caller thread is interrupted, at
which point the given handler (if non-null) is invoked, and if it
returns true, retried once. (The drop handler may distinguish
timeouts from interrupts by checking whether the current thread
is interrupted.) Other calls to methods in this class by other
threads are blocked while the handler is invoked. Unless
recovery is assured, options are usually limited to logging the
error and/or issuing an

onError

signal to the subscriber.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

This method returns a status indicator: If negative, it
represents the (negative) number of drops (failed attempts to
issue the item to a subscriber). Otherwise it is an estimate of
the maximum lag (number of items submitted but not yet
consumed) among all current subscribers. This value is at least
one (accounting for this submitted item) if there are any
subscribers, else zero.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

If the Executor for this publisher throws a
RejectedExecutionException (or any other RuntimeException or
Error) when attempting to asynchronously notify subscribers, or
the drop handler throws an exception when processing a dropped
item, then this exception is rethrown.

close

```java
public void close()
```

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.
Upon return, this method does

NOT

guarantee that all
subscribers have yet completed.

**Specified by:** close

in interface

AutoCloseable

---

#### close

public void close()

Unless already closed, issues

onComplete

signals to current
subscribers, and disallows subsequent attempts to publish.
Upon return, this method does

NOT

guarantee that all
subscribers have yet completed.

closeExceptionally

```java
public void closeExceptionally​(
Throwable
error)
```

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish. Future subscribers also receive the given
error. Upon return, this method does

NOT

guarantee
that all subscribers have yet completed.

**Parameters:** error

- the

onError

argument sent to subscribers
**Throws:** NullPointerException

- if error is null

---

#### closeExceptionally

public void closeExceptionally​(

Throwable

error)

Unless already closed, issues

onError

signals to current
subscribers with the given error, and disallows subsequent
attempts to publish. Future subscribers also receive the given
error. Upon return, this method does

NOT

guarantee
that all subscribers have yet completed.

isClosed

```java
public boolean isClosed()
```

Returns true if this publisher is not accepting submissions.

**Returns:** true if closed

---

#### isClosed

public boolean isClosed()

Returns true if this publisher is not accepting submissions.

getClosedException

```java
public
Throwable
getClosedException()
```

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

**Returns:** the exception, or null if none

---

#### getClosedException

public

Throwable

getClosedException()

Returns the exception associated with

closeExceptionally

, or null if
not closed or if closed normally.

hasSubscribers

```java
public boolean hasSubscribers()
```

Returns true if this publisher has any subscribers.

**Returns:** true if this publisher has any subscribers

---

#### hasSubscribers

public boolean hasSubscribers()

Returns true if this publisher has any subscribers.

getNumberOfSubscribers

```java
public int getNumberOfSubscribers()
```

Returns the number of current subscribers.

**Returns:** the number of current subscribers

---

#### getNumberOfSubscribers

public int getNumberOfSubscribers()

Returns the number of current subscribers.

getExecutor

```java
public
Executor
getExecutor()
```

Returns the Executor used for asynchronous delivery.

**Returns:** the Executor used for asynchronous delivery

---

#### getExecutor

public

Executor

getExecutor()

Returns the Executor used for asynchronous delivery.

getMaxBufferCapacity

```java
public int getMaxBufferCapacity()
```

Returns the maximum per-subscriber buffer capacity.

**Returns:** the maximum per-subscriber buffer capacity

---

#### getMaxBufferCapacity

public int getMaxBufferCapacity()

Returns the maximum per-subscriber buffer capacity.

getSubscribers

```java
public
List
<
Flow.Subscriber
<? super
T
>> getSubscribers()
```

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

**Returns:** list of current subscribers

---

#### getSubscribers

public

List

<

Flow.Subscriber

<? super

T

>> getSubscribers()

Returns a list of current subscribers for monitoring and
tracking purposes, not for invoking

Flow.Subscriber

methods on the subscribers.

isSubscribed

```java
public boolean isSubscribed​(
Flow.Subscriber
<? super
T
> subscriber)
```

Returns true if the given Subscriber is currently subscribed.

**Parameters:** subscriber

- the subscriber
**Returns:** true if currently subscribed
**Throws:** NullPointerException

- if subscriber is null

---

#### isSubscribed

public boolean isSubscribed​(

Flow.Subscriber

<? super

T

> subscriber)

Returns true if the given Subscriber is currently subscribed.

estimateMinimumDemand

```java
public long estimateMinimumDemand()
```

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

**Returns:** the estimate, or zero if no subscribers

---

#### estimateMinimumDemand

public long estimateMinimumDemand()

Returns an estimate of the minimum number of items requested
(via

request

) but not
yet produced, among all current subscribers.

estimateMaximumLag

```java
public int estimateMaximumLag()
```

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

**Returns:** the estimate

---

#### estimateMaximumLag

public int estimateMaximumLag()

Returns an estimate of the maximum number of items produced but
not yet consumed among all current subscribers.

consume

```java
public
CompletableFuture
<
Void
> consume​(
Consumer
<? super
T
> consumer)
```

Processes all published items using the given Consumer function.
Returns a CompletableFuture that is completed normally when this
publisher signals

onComplete

, or completed exceptionally upon any error, or an
exception is thrown by the Consumer, or the returned
CompletableFuture is cancelled, in which case no further items
are processed.

**Parameters:** consumer

- the function applied to each onNext item
**Returns:** a CompletableFuture that is completed normally
when the publisher signals onComplete, and exceptionally
upon any error or cancellation
**Throws:** NullPointerException

- if consumer is null

---

#### consume

public

CompletableFuture

<

Void

> consume​(

Consumer

<? super

T

> consumer)

Processes all published items using the given Consumer function.
Returns a CompletableFuture that is completed normally when this
publisher signals

onComplete

, or completed exceptionally upon any error, or an
exception is thrown by the Consumer, or the returned
CompletableFuture is cancelled, in which case no further items
are processed.

---

