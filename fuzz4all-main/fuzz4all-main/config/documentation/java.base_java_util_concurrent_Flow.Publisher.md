# Interface Flow.Publisher<T>

**Source:** `java.base\java\util\concurrent\Flow.Publisher.html`

### Class Description

```java
@FunctionalInterface

public static interface
Flow.Publisher<T>
```

A producer of items (and related control messages) received by
Subscribers. Each current

Flow.Subscriber

receives the same
items (via method

onNext

) in the same order, unless
drops or errors are encountered. If a Publisher encounters an
error that does not allow items to be issued to a Subscriber,
that Subscriber receives

onError

, and then receives no
further messages. Otherwise, when it is known that no further
messages will be issued to it, a subscriber receives

onComplete

. Publishers ensure that Subscriber method
invocations for each subscription are strictly ordered in

happens-before

order.

Publishers may vary in policy about whether drops (failures
to issue an item because of resource limitations) are treated
as unrecoverable errors. Publishers may also vary about
whether Subscribers receive items that were produced or
available before they subscribed.

**Type Parameters:** T

- the published item type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)

Adds the given Subscriber if possible. If already
subscribed, or the attempt to subscribe fails due to policy
violations or errors, the Subscriber's

onError

method is invoked with an

IllegalStateException

.
Otherwise, the Subscriber's

onSubscribe

method is
invoked with a new

Flow.Subscription

. Subscribers may
enable receiving items by invoking the

request

method of this Subscription, and may unsubscribe by
invoking its

cancel

method.

**Parameters:**
- subscriber

- the subscriber

**Throws:**
- NullPointerException

- if subscriber is null

---

### Additional Sections

#### Interface Flow.Publisher<T>

**Type Parameters:** T

- the published item type

**All Known Subinterfaces:** Flow.Processor

<T,​R>

,

HttpRequest.BodyPublisher

**All Known Implementing Classes:** SubmissionPublisher

**Enclosing class:** Flow

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public static interface
Flow.Publisher<T>
```

A producer of items (and related control messages) received by
Subscribers. Each current

Flow.Subscriber

receives the same
items (via method

onNext

) in the same order, unless
drops or errors are encountered. If a Publisher encounters an
error that does not allow items to be issued to a Subscriber,
that Subscriber receives

onError

, and then receives no
further messages. Otherwise, when it is known that no further
messages will be issued to it, a subscriber receives

onComplete

. Publishers ensure that Subscriber method
invocations for each subscription are strictly ordered in

happens-before

order.

Publishers may vary in policy about whether drops (failures
to issue an item because of resource limitations) are treated
as unrecoverable errors. Publishers may also vary about
whether Subscribers receive items that were produced or
available before they subscribed.

@FunctionalInterface

public static interface

Flow.Publisher<T>

A producer of items (and related control messages) received by
Subscribers. Each current

Flow.Subscriber

receives the same
items (via method

onNext

) in the same order, unless
drops or errors are encountered. If a Publisher encounters an
error that does not allow items to be issued to a Subscriber,
that Subscriber receives

onError

, and then receives no
further messages. Otherwise, when it is known that no further
messages will be issued to it, a subscriber receives

onComplete

. Publishers ensure that Subscriber method
invocations for each subscription are strictly ordered in

happens-before

order.

Publishers may vary in policy about whether drops (failures
to issue an item because of resource limitations) are treated
as unrecoverable errors. Publishers may also vary about
whether Subscribers receive items that were produced or
available before they subscribed.

Publishers may vary in policy about whether drops (failures
to issue an item because of resource limitations) are treated
as unrecoverable errors. Publishers may also vary about
whether Subscribers receive items that were produced or
available before they subscribed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

subscribe

​(

Flow.Subscriber

<? super

T

> subscriber)

Adds the given Subscriber if possible.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

subscribe

​(

Flow.Subscriber

<? super

T

> subscriber)

Adds the given Subscriber if possible.

---

#### Method Summary

Adds the given Subscriber if possible.

============ METHOD DETAIL ==========

- Method Detail

- subscribe

```java
void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)
```

Adds the given Subscriber if possible. If already
subscribed, or the attempt to subscribe fails due to policy
violations or errors, the Subscriber's

onError

method is invoked with an

IllegalStateException

.
Otherwise, the Subscriber's

onSubscribe

method is
invoked with a new

Flow.Subscription

. Subscribers may
enable receiving items by invoking the

request

method of this Subscription, and may unsubscribe by
invoking its

cancel

method.

**Parameters:** subscriber

- the subscriber
**Throws:** NullPointerException

- if subscriber is null

Method Detail

- subscribe

```java
void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)
```

Adds the given Subscriber if possible. If already
subscribed, or the attempt to subscribe fails due to policy
violations or errors, the Subscriber's

onError

method is invoked with an

IllegalStateException

.
Otherwise, the Subscriber's

onSubscribe

method is
invoked with a new

Flow.Subscription

. Subscribers may
enable receiving items by invoking the

request

method of this Subscription, and may unsubscribe by
invoking its

cancel

method.

**Parameters:** subscriber

- the subscriber
**Throws:** NullPointerException

- if subscriber is null

---

#### Method Detail

subscribe

```java
void subscribe​(
Flow.Subscriber
<? super
T
> subscriber)
```

Adds the given Subscriber if possible. If already
subscribed, or the attempt to subscribe fails due to policy
violations or errors, the Subscriber's

onError

method is invoked with an

IllegalStateException

.
Otherwise, the Subscriber's

onSubscribe

method is
invoked with a new

Flow.Subscription

. Subscribers may
enable receiving items by invoking the

request

method of this Subscription, and may unsubscribe by
invoking its

cancel

method.

**Parameters:** subscriber

- the subscriber
**Throws:** NullPointerException

- if subscriber is null

---

#### subscribe

void subscribe​(

Flow.Subscriber

<? super

T

> subscriber)

Adds the given Subscriber if possible. If already
subscribed, or the attempt to subscribe fails due to policy
violations or errors, the Subscriber's

onError

method is invoked with an

IllegalStateException

.
Otherwise, the Subscriber's

onSubscribe

method is
invoked with a new

Flow.Subscription

. Subscribers may
enable receiving items by invoking the

request

method of this Subscription, and may unsubscribe by
invoking its

cancel

method.

---

