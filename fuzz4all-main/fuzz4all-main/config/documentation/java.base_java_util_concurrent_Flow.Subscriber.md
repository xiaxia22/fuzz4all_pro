# Interface Flow.Subscriber<T>

**Source:** `java.base\java\util\concurrent\Flow.Subscriber.html`

### Class Description

```java
public static interface
Flow.Subscriber<T>
```

A receiver of messages. The methods in this interface are
invoked in strict sequential order for each

Flow.Subscription

.

**Type Parameters:** T

- the subscribed item type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void onSubscribe​(
Flow.Subscription
subscription)

Method invoked prior to invoking any other Subscriber
methods for the given Subscription. If this method throws
an exception, resulting behavior is not guaranteed, but may
cause the Subscription not to be established or to be cancelled.

Typically, implementations of this method invoke

subscription.request

to enable receiving items.

**Parameters:**
- subscription

- a new subscription

---

#### void onNext​(
T
item)

Method invoked with a Subscription's next item. If this
method throws an exception, resulting behavior is not
guaranteed, but may cause the Subscription to be cancelled.

**Parameters:**
- item

- the item

---

#### void onError​(
Throwable
throwable)

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription. If this method
itself throws an exception, resulting behavior is
undefined.

**Parameters:**
- throwable

- the exception

---

#### void onComplete()

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.
If this method throws an exception, resulting behavior is
undefined.

---

### Additional Sections

#### Interface Flow.Subscriber<T>

**Type Parameters:** T

- the subscribed item type

**All Known Subinterfaces:** Flow.Processor

<T,​R>

,

HttpResponse.BodySubscriber

<T>

**Enclosing class:** Flow

```java
public static interface
Flow.Subscriber<T>
```

A receiver of messages. The methods in this interface are
invoked in strict sequential order for each

Flow.Subscription

.

public static interface

Flow.Subscriber<T>

A receiver of messages. The methods in this interface are
invoked in strict sequential order for each

Flow.Subscription

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

onComplete

()

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.

void

onError

​(

Throwable

throwable)

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription.

void

onNext

​(

T

item)

Method invoked with a Subscription's next item.

void

onSubscribe

​(

Flow.Subscription

subscription)

Method invoked prior to invoking any other Subscriber
methods for the given Subscription.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

onComplete

()

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.

void

onError

​(

Throwable

throwable)

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription.

void

onNext

​(

T

item)

Method invoked with a Subscription's next item.

void

onSubscribe

​(

Flow.Subscription

subscription)

Method invoked prior to invoking any other Subscriber
methods for the given Subscription.

---

#### Method Summary

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription.

Method invoked with a Subscription's next item.

Method invoked prior to invoking any other Subscriber
methods for the given Subscription.

============ METHOD DETAIL ==========

- Method Detail

- onSubscribe

```java
void onSubscribe​(
Flow.Subscription
subscription)
```

Method invoked prior to invoking any other Subscriber
methods for the given Subscription. If this method throws
an exception, resulting behavior is not guaranteed, but may
cause the Subscription not to be established or to be cancelled.

Typically, implementations of this method invoke

subscription.request

to enable receiving items.

**Parameters:** subscription

- a new subscription

- onNext

```java
void onNext​(
T
item)
```

Method invoked with a Subscription's next item. If this
method throws an exception, resulting behavior is not
guaranteed, but may cause the Subscription to be cancelled.

**Parameters:** item

- the item

- onError

```java
void onError​(
Throwable
throwable)
```

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription. If this method
itself throws an exception, resulting behavior is
undefined.

**Parameters:** throwable

- the exception

- onComplete

```java
void onComplete()
```

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.
If this method throws an exception, resulting behavior is
undefined.

Method Detail

- onSubscribe

```java
void onSubscribe​(
Flow.Subscription
subscription)
```

Method invoked prior to invoking any other Subscriber
methods for the given Subscription. If this method throws
an exception, resulting behavior is not guaranteed, but may
cause the Subscription not to be established or to be cancelled.

Typically, implementations of this method invoke

subscription.request

to enable receiving items.

**Parameters:** subscription

- a new subscription

- onNext

```java
void onNext​(
T
item)
```

Method invoked with a Subscription's next item. If this
method throws an exception, resulting behavior is not
guaranteed, but may cause the Subscription to be cancelled.

**Parameters:** item

- the item

- onError

```java
void onError​(
Throwable
throwable)
```

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription. If this method
itself throws an exception, resulting behavior is
undefined.

**Parameters:** throwable

- the exception

- onComplete

```java
void onComplete()
```

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.
If this method throws an exception, resulting behavior is
undefined.

---

#### Method Detail

onSubscribe

```java
void onSubscribe​(
Flow.Subscription
subscription)
```

Method invoked prior to invoking any other Subscriber
methods for the given Subscription. If this method throws
an exception, resulting behavior is not guaranteed, but may
cause the Subscription not to be established or to be cancelled.

Typically, implementations of this method invoke

subscription.request

to enable receiving items.

**Parameters:** subscription

- a new subscription

---

#### onSubscribe

void onSubscribe​(

Flow.Subscription

subscription)

Method invoked prior to invoking any other Subscriber
methods for the given Subscription. If this method throws
an exception, resulting behavior is not guaranteed, but may
cause the Subscription not to be established or to be cancelled.

Typically, implementations of this method invoke

subscription.request

to enable receiving items.

Typically, implementations of this method invoke

subscription.request

to enable receiving items.

onNext

```java
void onNext​(
T
item)
```

Method invoked with a Subscription's next item. If this
method throws an exception, resulting behavior is not
guaranteed, but may cause the Subscription to be cancelled.

**Parameters:** item

- the item

---

#### onNext

void onNext​(

T

item)

Method invoked with a Subscription's next item. If this
method throws an exception, resulting behavior is not
guaranteed, but may cause the Subscription to be cancelled.

onError

```java
void onError​(
Throwable
throwable)
```

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription. If this method
itself throws an exception, resulting behavior is
undefined.

**Parameters:** throwable

- the exception

---

#### onError

void onError​(

Throwable

throwable)

Method invoked upon an unrecoverable error encountered by a
Publisher or Subscription, after which no other Subscriber
methods are invoked by the Subscription. If this method
itself throws an exception, resulting behavior is
undefined.

onComplete

```java
void onComplete()
```

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.
If this method throws an exception, resulting behavior is
undefined.

---

#### onComplete

void onComplete()

Method invoked when it is known that no additional
Subscriber method invocations will occur for a Subscription
that is not already terminated by error, after which no
other Subscriber methods are invoked by the Subscription.
If this method throws an exception, resulting behavior is
undefined.

---

