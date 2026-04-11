# Class Flow

**Source:** `java.base\java\util\concurrent\Flow.html`

### Class Description

```java
public final class
Flow

extends
Object
```

Interrelated interfaces and static methods for establishing
flow-controlled components in which

Publishers

produce items consumed by one or more

Subscribers

, each managed by a

Subscription

.

These interfaces correspond to the

reactive-streams

specification. They apply in both concurrent and distributed
asynchronous settings: All (seven) methods are defined in

void

"one-way" message style. Communication relies on a simple form
of flow control (method

Flow.Subscription.request(long)

) that can be
used to avoid resource management problems that may otherwise occur
in "push" based systems.

Examples.

A

Flow.Publisher

usually defines its own

Flow.Subscription

implementation; constructing one in method

subscribe

and issuing it to the calling

Flow.Subscriber

. It publishes items to the subscriber asynchronously,
normally using an

Executor

. For example, here is a very
simple publisher that only issues (when requested) a single

TRUE

item to a single subscriber. Because the subscriber receives
only a single item, this class does not use buffering and ordering
control required in most implementations (for example

SubmissionPublisher

).

```java
class OneShotPublisher implements Publisher<Boolean> {
private final ExecutorService executor = ForkJoinPool.commonPool(); // daemon-based
private boolean subscribed; // true after first subscribe
public synchronized void subscribe(Subscriber<? super Boolean> subscriber) {
if (subscribed)
subscriber.onError(new IllegalStateException()); // only one allowed
else {
subscribed = true;
subscriber.onSubscribe(new OneShotSubscription(subscriber, executor));
}
}
static class OneShotSubscription implements Subscription {
private final Subscriber<? super Boolean> subscriber;
private final ExecutorService executor;
private Future<?> future; // to allow cancellation
private boolean completed;
OneShotSubscription(Subscriber<? super Boolean> subscriber,
ExecutorService executor) {
this.subscriber = subscriber;
this.executor = executor;
}
public synchronized void request(long n) {
if (!completed) {
completed = true;
if (n <= 0) {
IllegalArgumentException ex = new IllegalArgumentException();
executor.execute(() -> subscriber.onError(ex));
} else {
future = executor.submit(() -> {
subscriber.onNext(Boolean.TRUE);
subscriber.onComplete();
});
}
}
}
public synchronized void cancel() {
completed = true;
if (future != null) future.cancel(false);
}
}
}
```

A

Flow.Subscriber

arranges that items be requested and
processed. Items (invocations of

Flow.Subscriber.onNext(T)

) are
not issued unless requested, but multiple items may be requested.
Many Subscriber implementations can arrange this in the style of
the following example, where a buffer size of 1 single-steps, and
larger sizes usually allow for more efficient overlapped processing
with less communication; for example with a value of 64, this keeps
total outstanding requests between 32 and 64.
Because Subscriber method invocations for a given

Flow.Subscription

are strictly ordered, there is no need for these
methods to use locks or volatiles unless a Subscriber maintains
multiple Subscriptions (in which case it is better to instead
define multiple Subscribers, each with its own Subscription).

```java
class SampleSubscriber<T> implements Subscriber<T> {
final Consumer<? super T> consumer;
Subscription subscription;
final long bufferSize;
long count;
SampleSubscriber(long bufferSize, Consumer<? super T> consumer) {
this.bufferSize = bufferSize;
this.consumer = consumer;
}
public void onSubscribe(Subscription subscription) {
long initialRequestSize = bufferSize;
count = bufferSize - bufferSize / 2; // re-request when half consumed
(this.subscription = subscription).request(initialRequestSize);
}
public void onNext(T item) {
if (--count <= 0)
subscription.request(count = bufferSize - bufferSize / 2);
consumer.accept(item);
}
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
}
```

The default value of

defaultBufferSize()

may provide a
useful starting point for choosing request sizes and capacities in
Flow components based on expected rates, resources, and usages.
Or, when flow control is never needed, a subscriber may initially
request an effectively unbounded number of items, as in:

```java
class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static int defaultBufferSize()

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

**Returns:**
- the buffer size value

**Implementation Note:**
- The current value returned is 256.

---

### Additional Sections

#### Class Flow

java.lang.Object

- java.util.concurrent.Flow

java.util.concurrent.Flow

```java
public final class
Flow

extends
Object
```

Interrelated interfaces and static methods for establishing
flow-controlled components in which

Publishers

produce items consumed by one or more

Subscribers

, each managed by a

Subscription

.

These interfaces correspond to the

reactive-streams

specification. They apply in both concurrent and distributed
asynchronous settings: All (seven) methods are defined in

void

"one-way" message style. Communication relies on a simple form
of flow control (method

Flow.Subscription.request(long)

) that can be
used to avoid resource management problems that may otherwise occur
in "push" based systems.

Examples.

A

Flow.Publisher

usually defines its own

Flow.Subscription

implementation; constructing one in method

subscribe

and issuing it to the calling

Flow.Subscriber

. It publishes items to the subscriber asynchronously,
normally using an

Executor

. For example, here is a very
simple publisher that only issues (when requested) a single

TRUE

item to a single subscriber. Because the subscriber receives
only a single item, this class does not use buffering and ordering
control required in most implementations (for example

SubmissionPublisher

).

```java
class OneShotPublisher implements Publisher<Boolean> {
private final ExecutorService executor = ForkJoinPool.commonPool(); // daemon-based
private boolean subscribed; // true after first subscribe
public synchronized void subscribe(Subscriber<? super Boolean> subscriber) {
if (subscribed)
subscriber.onError(new IllegalStateException()); // only one allowed
else {
subscribed = true;
subscriber.onSubscribe(new OneShotSubscription(subscriber, executor));
}
}
static class OneShotSubscription implements Subscription {
private final Subscriber<? super Boolean> subscriber;
private final ExecutorService executor;
private Future<?> future; // to allow cancellation
private boolean completed;
OneShotSubscription(Subscriber<? super Boolean> subscriber,
ExecutorService executor) {
this.subscriber = subscriber;
this.executor = executor;
}
public synchronized void request(long n) {
if (!completed) {
completed = true;
if (n <= 0) {
IllegalArgumentException ex = new IllegalArgumentException();
executor.execute(() -> subscriber.onError(ex));
} else {
future = executor.submit(() -> {
subscriber.onNext(Boolean.TRUE);
subscriber.onComplete();
});
}
}
}
public synchronized void cancel() {
completed = true;
if (future != null) future.cancel(false);
}
}
}
```

A

Flow.Subscriber

arranges that items be requested and
processed. Items (invocations of

Flow.Subscriber.onNext(T)

) are
not issued unless requested, but multiple items may be requested.
Many Subscriber implementations can arrange this in the style of
the following example, where a buffer size of 1 single-steps, and
larger sizes usually allow for more efficient overlapped processing
with less communication; for example with a value of 64, this keeps
total outstanding requests between 32 and 64.
Because Subscriber method invocations for a given

Flow.Subscription

are strictly ordered, there is no need for these
methods to use locks or volatiles unless a Subscriber maintains
multiple Subscriptions (in which case it is better to instead
define multiple Subscribers, each with its own Subscription).

```java
class SampleSubscriber<T> implements Subscriber<T> {
final Consumer<? super T> consumer;
Subscription subscription;
final long bufferSize;
long count;
SampleSubscriber(long bufferSize, Consumer<? super T> consumer) {
this.bufferSize = bufferSize;
this.consumer = consumer;
}
public void onSubscribe(Subscription subscription) {
long initialRequestSize = bufferSize;
count = bufferSize - bufferSize / 2; // re-request when half consumed
(this.subscription = subscription).request(initialRequestSize);
}
public void onNext(T item) {
if (--count <= 0)
subscription.request(count = bufferSize - bufferSize / 2);
consumer.accept(item);
}
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
}
```

The default value of

defaultBufferSize()

may provide a
useful starting point for choosing request sizes and capacities in
Flow components based on expected rates, resources, and usages.
Or, when flow control is never needed, a subscriber may initially
request an effectively unbounded number of items, as in:

```java
class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}
```

**Since:** 9

public final class

Flow

extends

Object

Interrelated interfaces and static methods for establishing
flow-controlled components in which

Publishers

produce items consumed by one or more

Subscribers

, each managed by a

Subscription

.

These interfaces correspond to the

reactive-streams

specification. They apply in both concurrent and distributed
asynchronous settings: All (seven) methods are defined in

void

"one-way" message style. Communication relies on a simple form
of flow control (method

Flow.Subscription.request(long)

) that can be
used to avoid resource management problems that may otherwise occur
in "push" based systems.

Examples.

A

Flow.Publisher

usually defines its own

Flow.Subscription

implementation; constructing one in method

subscribe

and issuing it to the calling

Flow.Subscriber

. It publishes items to the subscriber asynchronously,
normally using an

Executor

. For example, here is a very
simple publisher that only issues (when requested) a single

TRUE

item to a single subscriber. Because the subscriber receives
only a single item, this class does not use buffering and ordering
control required in most implementations (for example

SubmissionPublisher

).

```java
class OneShotPublisher implements Publisher<Boolean> {
private final ExecutorService executor = ForkJoinPool.commonPool(); // daemon-based
private boolean subscribed; // true after first subscribe
public synchronized void subscribe(Subscriber<? super Boolean> subscriber) {
if (subscribed)
subscriber.onError(new IllegalStateException()); // only one allowed
else {
subscribed = true;
subscriber.onSubscribe(new OneShotSubscription(subscriber, executor));
}
}
static class OneShotSubscription implements Subscription {
private final Subscriber<? super Boolean> subscriber;
private final ExecutorService executor;
private Future<?> future; // to allow cancellation
private boolean completed;
OneShotSubscription(Subscriber<? super Boolean> subscriber,
ExecutorService executor) {
this.subscriber = subscriber;
this.executor = executor;
}
public synchronized void request(long n) {
if (!completed) {
completed = true;
if (n <= 0) {
IllegalArgumentException ex = new IllegalArgumentException();
executor.execute(() -> subscriber.onError(ex));
} else {
future = executor.submit(() -> {
subscriber.onNext(Boolean.TRUE);
subscriber.onComplete();
});
}
}
}
public synchronized void cancel() {
completed = true;
if (future != null) future.cancel(false);
}
}
}
```

A

Flow.Subscriber

arranges that items be requested and
processed. Items (invocations of

Flow.Subscriber.onNext(T)

) are
not issued unless requested, but multiple items may be requested.
Many Subscriber implementations can arrange this in the style of
the following example, where a buffer size of 1 single-steps, and
larger sizes usually allow for more efficient overlapped processing
with less communication; for example with a value of 64, this keeps
total outstanding requests between 32 and 64.
Because Subscriber method invocations for a given

Flow.Subscription

are strictly ordered, there is no need for these
methods to use locks or volatiles unless a Subscriber maintains
multiple Subscriptions (in which case it is better to instead
define multiple Subscribers, each with its own Subscription).

```java
class SampleSubscriber<T> implements Subscriber<T> {
final Consumer<? super T> consumer;
Subscription subscription;
final long bufferSize;
long count;
SampleSubscriber(long bufferSize, Consumer<? super T> consumer) {
this.bufferSize = bufferSize;
this.consumer = consumer;
}
public void onSubscribe(Subscription subscription) {
long initialRequestSize = bufferSize;
count = bufferSize - bufferSize / 2; // re-request when half consumed
(this.subscription = subscription).request(initialRequestSize);
}
public void onNext(T item) {
if (--count <= 0)
subscription.request(count = bufferSize - bufferSize / 2);
consumer.accept(item);
}
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
}
```

The default value of

defaultBufferSize()

may provide a
useful starting point for choosing request sizes and capacities in
Flow components based on expected rates, resources, and usages.
Or, when flow control is never needed, a subscriber may initially
request an effectively unbounded number of items, as in:

```java
class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}
```

These interfaces correspond to the

reactive-streams

specification. They apply in both concurrent and distributed
asynchronous settings: All (seven) methods are defined in

void

"one-way" message style. Communication relies on a simple form
of flow control (method

Flow.Subscription.request(long)

) that can be
used to avoid resource management problems that may otherwise occur
in "push" based systems.

Examples.

A

Flow.Publisher

usually defines its own

Flow.Subscription

implementation; constructing one in method

subscribe

and issuing it to the calling

Flow.Subscriber

. It publishes items to the subscriber asynchronously,
normally using an

Executor

. For example, here is a very
simple publisher that only issues (when requested) a single

TRUE

item to a single subscriber. Because the subscriber receives
only a single item, this class does not use buffering and ordering
control required in most implementations (for example

SubmissionPublisher

).

```java
class OneShotPublisher implements Publisher<Boolean> {
private final ExecutorService executor = ForkJoinPool.commonPool(); // daemon-based
private boolean subscribed; // true after first subscribe
public synchronized void subscribe(Subscriber<? super Boolean> subscriber) {
if (subscribed)
subscriber.onError(new IllegalStateException()); // only one allowed
else {
subscribed = true;
subscriber.onSubscribe(new OneShotSubscription(subscriber, executor));
}
}
static class OneShotSubscription implements Subscription {
private final Subscriber<? super Boolean> subscriber;
private final ExecutorService executor;
private Future<?> future; // to allow cancellation
private boolean completed;
OneShotSubscription(Subscriber<? super Boolean> subscriber,
ExecutorService executor) {
this.subscriber = subscriber;
this.executor = executor;
}
public synchronized void request(long n) {
if (!completed) {
completed = true;
if (n <= 0) {
IllegalArgumentException ex = new IllegalArgumentException();
executor.execute(() -> subscriber.onError(ex));
} else {
future = executor.submit(() -> {
subscriber.onNext(Boolean.TRUE);
subscriber.onComplete();
});
}
}
}
public synchronized void cancel() {
completed = true;
if (future != null) future.cancel(false);
}
}
}
```

A

Flow.Subscriber

arranges that items be requested and
processed. Items (invocations of

Flow.Subscriber.onNext(T)

) are
not issued unless requested, but multiple items may be requested.
Many Subscriber implementations can arrange this in the style of
the following example, where a buffer size of 1 single-steps, and
larger sizes usually allow for more efficient overlapped processing
with less communication; for example with a value of 64, this keeps
total outstanding requests between 32 and 64.
Because Subscriber method invocations for a given

Flow.Subscription

are strictly ordered, there is no need for these
methods to use locks or volatiles unless a Subscriber maintains
multiple Subscriptions (in which case it is better to instead
define multiple Subscribers, each with its own Subscription).

```java
class SampleSubscriber<T> implements Subscriber<T> {
final Consumer<? super T> consumer;
Subscription subscription;
final long bufferSize;
long count;
SampleSubscriber(long bufferSize, Consumer<? super T> consumer) {
this.bufferSize = bufferSize;
this.consumer = consumer;
}
public void onSubscribe(Subscription subscription) {
long initialRequestSize = bufferSize;
count = bufferSize - bufferSize / 2; // re-request when half consumed
(this.subscription = subscription).request(initialRequestSize);
}
public void onNext(T item) {
if (--count <= 0)
subscription.request(count = bufferSize - bufferSize / 2);
consumer.accept(item);
}
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
}
```

The default value of

defaultBufferSize()

may provide a
useful starting point for choosing request sizes and capacities in
Flow components based on expected rates, resources, and usages.
Or, when flow control is never needed, a subscriber may initially
request an effectively unbounded number of items, as in:

```java
class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}
```

Examples.

A

Flow.Publisher

usually defines its own

Flow.Subscription

implementation; constructing one in method

subscribe

and issuing it to the calling

Flow.Subscriber

. It publishes items to the subscriber asynchronously,
normally using an

Executor

. For example, here is a very
simple publisher that only issues (when requested) a single

TRUE

item to a single subscriber. Because the subscriber receives
only a single item, this class does not use buffering and ordering
control required in most implementations (for example

SubmissionPublisher

).

```java
class OneShotPublisher implements Publisher<Boolean> {
private final ExecutorService executor = ForkJoinPool.commonPool(); // daemon-based
private boolean subscribed; // true after first subscribe
public synchronized void subscribe(Subscriber<? super Boolean> subscriber) {
if (subscribed)
subscriber.onError(new IllegalStateException()); // only one allowed
else {
subscribed = true;
subscriber.onSubscribe(new OneShotSubscription(subscriber, executor));
}
}
static class OneShotSubscription implements Subscription {
private final Subscriber<? super Boolean> subscriber;
private final ExecutorService executor;
private Future<?> future; // to allow cancellation
private boolean completed;
OneShotSubscription(Subscriber<? super Boolean> subscriber,
ExecutorService executor) {
this.subscriber = subscriber;
this.executor = executor;
}
public synchronized void request(long n) {
if (!completed) {
completed = true;
if (n <= 0) {
IllegalArgumentException ex = new IllegalArgumentException();
executor.execute(() -> subscriber.onError(ex));
} else {
future = executor.submit(() -> {
subscriber.onNext(Boolean.TRUE);
subscriber.onComplete();
});
}
}
}
public synchronized void cancel() {
completed = true;
if (future != null) future.cancel(false);
}
}
}
```

A

Flow.Subscriber

arranges that items be requested and
processed. Items (invocations of

Flow.Subscriber.onNext(T)

) are
not issued unless requested, but multiple items may be requested.
Many Subscriber implementations can arrange this in the style of
the following example, where a buffer size of 1 single-steps, and
larger sizes usually allow for more efficient overlapped processing
with less communication; for example with a value of 64, this keeps
total outstanding requests between 32 and 64.
Because Subscriber method invocations for a given

Flow.Subscription

are strictly ordered, there is no need for these
methods to use locks or volatiles unless a Subscriber maintains
multiple Subscriptions (in which case it is better to instead
define multiple Subscribers, each with its own Subscription).

```java
class SampleSubscriber<T> implements Subscriber<T> {
final Consumer<? super T> consumer;
Subscription subscription;
final long bufferSize;
long count;
SampleSubscriber(long bufferSize, Consumer<? super T> consumer) {
this.bufferSize = bufferSize;
this.consumer = consumer;
}
public void onSubscribe(Subscription subscription) {
long initialRequestSize = bufferSize;
count = bufferSize - bufferSize / 2; // re-request when half consumed
(this.subscription = subscription).request(initialRequestSize);
}
public void onNext(T item) {
if (--count <= 0)
subscription.request(count = bufferSize - bufferSize / 2);
consumer.accept(item);
}
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
}
```

The default value of

defaultBufferSize()

may provide a
useful starting point for choosing request sizes and capacities in
Flow components based on expected rates, resources, and usages.
Or, when flow control is never needed, a subscriber may initially
request an effectively unbounded number of items, as in:

```java
class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}
```

class OneShotPublisher implements Publisher<Boolean> {
private final ExecutorService executor = ForkJoinPool.commonPool(); // daemon-based
private boolean subscribed; // true after first subscribe
public synchronized void subscribe(Subscriber<? super Boolean> subscriber) {
if (subscribed)
subscriber.onError(new IllegalStateException()); // only one allowed
else {
subscribed = true;
subscriber.onSubscribe(new OneShotSubscription(subscriber, executor));
}
}
static class OneShotSubscription implements Subscription {
private final Subscriber<? super Boolean> subscriber;
private final ExecutorService executor;
private Future<?> future; // to allow cancellation
private boolean completed;
OneShotSubscription(Subscriber<? super Boolean> subscriber,
ExecutorService executor) {
this.subscriber = subscriber;
this.executor = executor;
}
public synchronized void request(long n) {
if (!completed) {
completed = true;
if (n <= 0) {
IllegalArgumentException ex = new IllegalArgumentException();
executor.execute(() -> subscriber.onError(ex));
} else {
future = executor.submit(() -> {
subscriber.onNext(Boolean.TRUE);
subscriber.onComplete();
});
}
}
}
public synchronized void cancel() {
completed = true;
if (future != null) future.cancel(false);
}
}
}

A

Flow.Subscriber

arranges that items be requested and
processed. Items (invocations of

Flow.Subscriber.onNext(T)

) are
not issued unless requested, but multiple items may be requested.
Many Subscriber implementations can arrange this in the style of
the following example, where a buffer size of 1 single-steps, and
larger sizes usually allow for more efficient overlapped processing
with less communication; for example with a value of 64, this keeps
total outstanding requests between 32 and 64.
Because Subscriber method invocations for a given

Flow.Subscription

are strictly ordered, there is no need for these
methods to use locks or volatiles unless a Subscriber maintains
multiple Subscriptions (in which case it is better to instead
define multiple Subscribers, each with its own Subscription).

```java
class SampleSubscriber<T> implements Subscriber<T> {
final Consumer<? super T> consumer;
Subscription subscription;
final long bufferSize;
long count;
SampleSubscriber(long bufferSize, Consumer<? super T> consumer) {
this.bufferSize = bufferSize;
this.consumer = consumer;
}
public void onSubscribe(Subscription subscription) {
long initialRequestSize = bufferSize;
count = bufferSize - bufferSize / 2; // re-request when half consumed
(this.subscription = subscription).request(initialRequestSize);
}
public void onNext(T item) {
if (--count <= 0)
subscription.request(count = bufferSize - bufferSize / 2);
consumer.accept(item);
}
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
}
```

The default value of

defaultBufferSize()

may provide a
useful starting point for choosing request sizes and capacities in
Flow components based on expected rates, resources, and usages.
Or, when flow control is never needed, a subscriber may initially
request an effectively unbounded number of items, as in:

```java
class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}
```

class SampleSubscriber<T> implements Subscriber<T> {
final Consumer<? super T> consumer;
Subscription subscription;
final long bufferSize;
long count;
SampleSubscriber(long bufferSize, Consumer<? super T> consumer) {
this.bufferSize = bufferSize;
this.consumer = consumer;
}
public void onSubscribe(Subscription subscription) {
long initialRequestSize = bufferSize;
count = bufferSize - bufferSize / 2; // re-request when half consumed
(this.subscription = subscription).request(initialRequestSize);
}
public void onNext(T item) {
if (--count <= 0)
subscription.request(count = bufferSize - bufferSize / 2);
consumer.accept(item);
}
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
}

The default value of

defaultBufferSize()

may provide a
useful starting point for choosing request sizes and capacities in
Flow components based on expected rates, resources, and usages.
Or, when flow control is never needed, a subscriber may initially
request an effectively unbounded number of items, as in:

```java
class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}
```

class UnboundedSubscriber<T> implements Subscriber<T> {
public void onSubscribe(Subscription subscription) {
subscription.request(Long.MAX_VALUE); // effectively unbounded
}
public void onNext(T item) { use(item); }
public void onError(Throwable ex) { ex.printStackTrace(); }
public void onComplete() {}
void use(T item) { ... }
}

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

Flow.Processor

<

T

,​

R

>

A component that acts as both a Subscriber and Publisher.

static interface

Flow.Publisher

<

T

>

A producer of items (and related control messages) received by
Subscribers.

static interface

Flow.Subscriber

<

T

>

A receiver of messages.

static interface

Flow.Subscription

Message control linking a

Flow.Publisher

and

Flow.Subscriber

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

defaultBufferSize

()

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

Flow.Processor

<

T

,​

R

>

A component that acts as both a Subscriber and Publisher.

static interface

Flow.Publisher

<

T

>

A producer of items (and related control messages) received by
Subscribers.

static interface

Flow.Subscriber

<

T

>

A receiver of messages.

static interface

Flow.Subscription

Message control linking a

Flow.Publisher

and

Flow.Subscriber

.

---

#### Nested Class Summary

A component that acts as both a Subscriber and Publisher.

A producer of items (and related control messages) received by
Subscribers.

A receiver of messages.

Message control linking a

Flow.Publisher

and

Flow.Subscriber

.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

defaultBufferSize

()

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

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

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

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

============ METHOD DETAIL ==========

- Method Detail

- defaultBufferSize

```java
public static int defaultBufferSize()
```

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

**Implementation Note:** The current value returned is 256.
**Returns:** the buffer size value

Method Detail

- defaultBufferSize

```java
public static int defaultBufferSize()
```

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

**Implementation Note:** The current value returned is 256.
**Returns:** the buffer size value

---

#### Method Detail

defaultBufferSize

```java
public static int defaultBufferSize()
```

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

**Implementation Note:** The current value returned is 256.
**Returns:** the buffer size value

---

#### defaultBufferSize

public static int defaultBufferSize()

Returns a default value for Publisher or Subscriber buffering,
that may be used in the absence of other constraints.

---

