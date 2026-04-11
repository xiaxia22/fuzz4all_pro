# Interface Flow.Subscription

**Source:** `java.base\java\util\concurrent\Flow.Subscription.html`

### Class Description

```java
public static interface
Flow.Subscription
```

Message control linking a

Flow.Publisher

and

Flow.Subscriber

. Subscribers receive items only when requested,
and may cancel at any time. The methods in this interface are
intended to be invoked only by their Subscribers; usages in
other contexts have undefined effects.

**Enclosing class:** Flow

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void request​(long n)

Adds the given number

n

of items to the current
unfulfilled demand for this subscription. If

n

is
less than or equal to zero, the Subscriber will receive an

onError

signal with an

IllegalArgumentException

argument. Otherwise, the
Subscriber will receive up to

n

additional

onNext

invocations (or fewer if terminated).

**Parameters:**
- n

- the increment of demand; a value of

Long.MAX_VALUE

may be considered as effectively unbounded

---

#### void cancel()

Causes the Subscriber to (eventually) stop receiving
messages. Implementation is best-effort -- additional
messages may be received after invoking this method.
A cancelled subscription need not ever receive an

onComplete

or

onError

signal.

---

### Additional Sections

#### Interface Flow.Subscription

**Enclosing class:** Flow

```java
public static interface
Flow.Subscription
```

Message control linking a

Flow.Publisher

and

Flow.Subscriber

. Subscribers receive items only when requested,
and may cancel at any time. The methods in this interface are
intended to be invoked only by their Subscribers; usages in
other contexts have undefined effects.

public static interface

Flow.Subscription

Message control linking a

Flow.Publisher

and

Flow.Subscriber

. Subscribers receive items only when requested,
and may cancel at any time. The methods in this interface are
intended to be invoked only by their Subscribers; usages in
other contexts have undefined effects.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cancel

()

Causes the Subscriber to (eventually) stop receiving
messages.

void

request

​(long n)

Adds the given number

n

of items to the current
unfulfilled demand for this subscription.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cancel

()

Causes the Subscriber to (eventually) stop receiving
messages.

void

request

​(long n)

Adds the given number

n

of items to the current
unfulfilled demand for this subscription.

---

#### Method Summary

Causes the Subscriber to (eventually) stop receiving
messages.

Adds the given number

n

of items to the current
unfulfilled demand for this subscription.

============ METHOD DETAIL ==========

- Method Detail

- request

```java
void request​(long n)
```

Adds the given number

n

of items to the current
unfulfilled demand for this subscription. If

n

is
less than or equal to zero, the Subscriber will receive an

onError

signal with an

IllegalArgumentException

argument. Otherwise, the
Subscriber will receive up to

n

additional

onNext

invocations (or fewer if terminated).

**Parameters:** n

- the increment of demand; a value of

Long.MAX_VALUE

may be considered as effectively unbounded

- cancel

```java
void cancel()
```

Causes the Subscriber to (eventually) stop receiving
messages. Implementation is best-effort -- additional
messages may be received after invoking this method.
A cancelled subscription need not ever receive an

onComplete

or

onError

signal.

Method Detail

- request

```java
void request​(long n)
```

Adds the given number

n

of items to the current
unfulfilled demand for this subscription. If

n

is
less than or equal to zero, the Subscriber will receive an

onError

signal with an

IllegalArgumentException

argument. Otherwise, the
Subscriber will receive up to

n

additional

onNext

invocations (or fewer if terminated).

**Parameters:** n

- the increment of demand; a value of

Long.MAX_VALUE

may be considered as effectively unbounded

- cancel

```java
void cancel()
```

Causes the Subscriber to (eventually) stop receiving
messages. Implementation is best-effort -- additional
messages may be received after invoking this method.
A cancelled subscription need not ever receive an

onComplete

or

onError

signal.

---

#### Method Detail

request

```java
void request​(long n)
```

Adds the given number

n

of items to the current
unfulfilled demand for this subscription. If

n

is
less than or equal to zero, the Subscriber will receive an

onError

signal with an

IllegalArgumentException

argument. Otherwise, the
Subscriber will receive up to

n

additional

onNext

invocations (or fewer if terminated).

**Parameters:** n

- the increment of demand; a value of

Long.MAX_VALUE

may be considered as effectively unbounded

---

#### request

void request​(long n)

Adds the given number

n

of items to the current
unfulfilled demand for this subscription. If

n

is
less than or equal to zero, the Subscriber will receive an

onError

signal with an

IllegalArgumentException

argument. Otherwise, the
Subscriber will receive up to

n

additional

onNext

invocations (or fewer if terminated).

cancel

```java
void cancel()
```

Causes the Subscriber to (eventually) stop receiving
messages. Implementation is best-effort -- additional
messages may be received after invoking this method.
A cancelled subscription need not ever receive an

onComplete

or

onError

signal.

---

#### cancel

void cancel()

Causes the Subscriber to (eventually) stop receiving
messages. Implementation is best-effort -- additional
messages may be received after invoking this method.
A cancelled subscription need not ever receive an

onComplete

or

onError

signal.

---

