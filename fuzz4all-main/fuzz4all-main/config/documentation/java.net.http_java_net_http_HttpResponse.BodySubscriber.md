# Interface HttpResponse.BodySubscriber<T>

**Source:** `java.net.http\java\net\http\HttpResponse.BodySubscriber.html`

### Class Description

```java
public static interface
HttpResponse.BodySubscriber<T>

extends
Flow.Subscriber
<
List
<
ByteBuffer
>>
```

A

BodySubscriber

consumes response body bytes and converts them
into a higher-level Java type. The class

BodySubscriber

provides implementations of many common body subscribers.

The object acts as a

Flow.Subscriber

<

List

<

ByteBuffer

>> to the HTTP Client implementation, which publishes
lists of ByteBuffers containing the response body. The Flow of data, as
well as the order of ByteBuffers in the Flow lists, is a strictly ordered
representation of the response body. Both the Lists and the ByteBuffers,
once passed to the subscriber, are no longer used by the HTTP Client. The
subscriber converts the incoming buffers of data to some higher-level
Java type

T

.

The

getBody()

method returns a

CompletionStage

<

T

> that provides the response body
object. The

CompletionStage

must be obtainable at any time. When
it completes depends on the nature of type

T

. In many cases,
when

T

represents the entire body after being consumed then
the

CompletionStage

completes after the body has been consumed.
If

T

is a streaming type, such as

InputStream

, then it completes before the body has been read, because
the calling code uses the

InputStream

to consume the data.

**Type Parameters:** T

- the response body type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CompletionStage
<
T
> getBody()

Returns a

CompletionStage

which when completed will return
the response body object. This method can be called at any time
relative to the other

Flow.Subscriber

methods and is invoked
using the client's

executor

.

**Returns:**
- a CompletionStage for the response body

---

### Additional Sections

#### Interface HttpResponse.BodySubscriber<T>

**Type Parameters:** T

- the response body type

**All Superinterfaces:** Flow.Subscriber

<

List

<

ByteBuffer

>>

**Enclosing interface:** HttpResponse

<

T

>

```java
public static interface
HttpResponse.BodySubscriber<T>

extends
Flow.Subscriber
<
List
<
ByteBuffer
>>
```

A

BodySubscriber

consumes response body bytes and converts them
into a higher-level Java type. The class

BodySubscriber

provides implementations of many common body subscribers.

The object acts as a

Flow.Subscriber

<

List

<

ByteBuffer

>> to the HTTP Client implementation, which publishes
lists of ByteBuffers containing the response body. The Flow of data, as
well as the order of ByteBuffers in the Flow lists, is a strictly ordered
representation of the response body. Both the Lists and the ByteBuffers,
once passed to the subscriber, are no longer used by the HTTP Client. The
subscriber converts the incoming buffers of data to some higher-level
Java type

T

.

The

getBody()

method returns a

CompletionStage

<

T

> that provides the response body
object. The

CompletionStage

must be obtainable at any time. When
it completes depends on the nature of type

T

. In many cases,
when

T

represents the entire body after being consumed then
the

CompletionStage

completes after the body has been consumed.
If

T

is a streaming type, such as

InputStream

, then it completes before the body has been read, because
the calling code uses the

InputStream

to consume the data.

**API Note:** To ensure that all resources associated with the corresponding
HTTP exchange are properly released, an implementation of

BodySubscriber

should ensure to

request

more data until one of

onComplete

or

onError

are signalled, or

cancel

its

subscription

if unable or unwilling to
do so. Calling

cancel

before exhausting the response body data
may cause the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.
**Implementation Note:** The flow of data containing the response body is immutable.
Specifically, it is a flow of unmodifiable lists of read-only ByteBuffers.
**Since:** 11
**See Also:** HttpResponse.BodySubscribers

public static interface

HttpResponse.BodySubscriber<T>

extends

Flow.Subscriber

<

List

<

ByteBuffer

>>

A

BodySubscriber

consumes response body bytes and converts them
into a higher-level Java type. The class

BodySubscriber

provides implementations of many common body subscribers.

The object acts as a

Flow.Subscriber

<

List

<

ByteBuffer

>> to the HTTP Client implementation, which publishes
lists of ByteBuffers containing the response body. The Flow of data, as
well as the order of ByteBuffers in the Flow lists, is a strictly ordered
representation of the response body. Both the Lists and the ByteBuffers,
once passed to the subscriber, are no longer used by the HTTP Client. The
subscriber converts the incoming buffers of data to some higher-level
Java type

T

.

The

getBody()

method returns a

CompletionStage

<

T

> that provides the response body
object. The

CompletionStage

must be obtainable at any time. When
it completes depends on the nature of type

T

. In many cases,
when

T

represents the entire body after being consumed then
the

CompletionStage

completes after the body has been consumed.
If

T

is a streaming type, such as

InputStream

, then it completes before the body has been read, because
the calling code uses the

InputStream

to consume the data.

The object acts as a

Flow.Subscriber

<

List

<

ByteBuffer

>> to the HTTP Client implementation, which publishes
lists of ByteBuffers containing the response body. The Flow of data, as
well as the order of ByteBuffers in the Flow lists, is a strictly ordered
representation of the response body. Both the Lists and the ByteBuffers,
once passed to the subscriber, are no longer used by the HTTP Client. The
subscriber converts the incoming buffers of data to some higher-level
Java type

T

.

The

getBody()

method returns a

CompletionStage

<

T

> that provides the response body
object. The

CompletionStage

must be obtainable at any time. When
it completes depends on the nature of type

T

. In many cases,
when

T

represents the entire body after being consumed then
the

CompletionStage

completes after the body has been consumed.
If

T

is a streaming type, such as

InputStream

, then it completes before the body has been read, because
the calling code uses the

InputStream

to consume the data.

The

getBody()

method returns a

CompletionStage

<

T

> that provides the response body
object. The

CompletionStage

must be obtainable at any time. When
it completes depends on the nature of type

T

. In many cases,
when

T

represents the entire body after being consumed then
the

CompletionStage

completes after the body has been consumed.
If

T

is a streaming type, such as

InputStream

, then it completes before the body has been read, because
the calling code uses the

InputStream

to consume the data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompletionStage

<

T

>

getBody

()

Returns a

CompletionStage

which when completed will return
the response body object.

- Methods declared in interface java.util.concurrent.

Flow.Subscriber

onComplete

,

onError

,

onNext

,

onSubscribe

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompletionStage

<

T

>

getBody

()

Returns a

CompletionStage

which when completed will return
the response body object.

- Methods declared in interface java.util.concurrent.

Flow.Subscriber

onComplete

,

onError

,

onNext

,

onSubscribe

---

#### Method Summary

Returns a

CompletionStage

which when completed will return
the response body object.

Methods declared in interface java.util.concurrent.

Flow.Subscriber

onComplete

,

onError

,

onNext

,

onSubscribe

---

#### Methods declared in interface java.util.concurrent. Flow.Subscriber

============ METHOD DETAIL ==========

- Method Detail

- getBody

```java
CompletionStage
<
T
> getBody()
```

Returns a

CompletionStage

which when completed will return
the response body object. This method can be called at any time
relative to the other

Flow.Subscriber

methods and is invoked
using the client's

executor

.

**Returns:** a CompletionStage for the response body

Method Detail

- getBody

```java
CompletionStage
<
T
> getBody()
```

Returns a

CompletionStage

which when completed will return
the response body object. This method can be called at any time
relative to the other

Flow.Subscriber

methods and is invoked
using the client's

executor

.

**Returns:** a CompletionStage for the response body

---

#### Method Detail

getBody

```java
CompletionStage
<
T
> getBody()
```

Returns a

CompletionStage

which when completed will return
the response body object. This method can be called at any time
relative to the other

Flow.Subscriber

methods and is invoked
using the client's

executor

.

**Returns:** a CompletionStage for the response body

---

#### getBody

CompletionStage

<

T

> getBody()

Returns a

CompletionStage

which when completed will return
the response body object. This method can be called at any time
relative to the other

Flow.Subscriber

methods and is invoked
using the client's

executor

.

---

