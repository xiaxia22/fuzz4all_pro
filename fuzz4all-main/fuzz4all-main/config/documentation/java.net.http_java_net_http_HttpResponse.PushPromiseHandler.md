# Interface HttpResponse.PushPromiseHandler<T>

**Source:** `java.net.http\java\net\http\HttpResponse.PushPromiseHandler.html`

### Class Description

```java
public static interface
HttpResponse.PushPromiseHandler<T>
```

A handler for push promises.

A

push promise

is a synthetic request sent by an HTTP/2 server
when retrieving an initiating client-sent request. The server has
determined, possibly through inspection of the initiating request, that
the client will likely need the promised resource, and hence pushes a
synthetic push request, in the form of a push promise, to the client. The
client can choose to accept or reject the push promise request.

A push promise request may be received up to the point where the
response body of the initiating client-sent request has been fully
received. The delivery of a push promise response, however, is not
coordinated with the delivery of the response to the initiating
client-sent request.

**Type Parameters:** T

- the push promise response body type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void applyPushPromise​(
HttpRequest
initiatingRequest,

HttpRequest
pushPromiseRequest,

Function
<
HttpResponse.BodyHandler
<
T
>,​
CompletableFuture
<
HttpResponse
<
T
>>> acceptor)

Notification of an incoming push promise.

This method is invoked once for each push promise received, up
to the point where the response body of the initiating client-sent
request has been fully received.

A push promise is accepted by invoking the given

acceptor

function. The

acceptor

function must be passed a non-null

BodyHandler

, that is to be used to handle the promise's
response body. The acceptor function will return a

CompletableFuture

that completes with the promise's response.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

**Parameters:**
- initiatingRequest

- the initiating client-send request
- pushPromiseRequest

- the synthetic push request
- acceptor

- the acceptor function that must be successfully
invoked to accept the push promise

---

#### static <T>
HttpResponse.PushPromiseHandler
<T> of​(
Function
<
HttpRequest
,​
HttpResponse.BodyHandler
<T>> pushPromiseHandler,

ConcurrentMap
<
HttpRequest
,​
CompletableFuture
<
HttpResponse
<T>>> pushPromisesMap)

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

Entries are added to the given map for each push promise accepted.
The entry's key is the push request, and the entry's value is a

CompletableFuture

that completes with the response
corresponding to the key's push request. A push request is rejected /
cancelled if there is already an entry in the map whose key is

equal

to it. A push request is
rejected / cancelled if it does not have the same origin as its
initiating request.

Entries are added to the given map as soon as practically
possible when a push promise is received and accepted. That way code,
using such a map like a cache, can determine if a push promise has
been issued by the server and avoid making, possibly, unnecessary
requests.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

**Parameters:**
- pushPromiseHandler

- t he body handler to use for push promises
- pushPromisesMap

- a map to accumulate push promises into

**Returns:**
- a push promise handler

**Type Parameters:**
- T

- the push promise response body type

---

### Additional Sections

#### Interface HttpResponse.PushPromiseHandler<T>

**Type Parameters:** T

- the push promise response body type

**Enclosing interface:** HttpResponse

<

T

>

```java
public static interface
HttpResponse.PushPromiseHandler<T>
```

A handler for push promises.

A

push promise

is a synthetic request sent by an HTTP/2 server
when retrieving an initiating client-sent request. The server has
determined, possibly through inspection of the initiating request, that
the client will likely need the promised resource, and hence pushes a
synthetic push request, in the form of a push promise, to the client. The
client can choose to accept or reject the push promise request.

A push promise request may be received up to the point where the
response body of the initiating client-sent request has been fully
received. The delivery of a push promise response, however, is not
coordinated with the delivery of the response to the initiating
client-sent request.

**Since:** 11

public static interface

HttpResponse.PushPromiseHandler<T>

A handler for push promises.

A

push promise

is a synthetic request sent by an HTTP/2 server
when retrieving an initiating client-sent request. The server has
determined, possibly through inspection of the initiating request, that
the client will likely need the promised resource, and hence pushes a
synthetic push request, in the form of a push promise, to the client. The
client can choose to accept or reject the push promise request.

A push promise request may be received up to the point where the
response body of the initiating client-sent request has been fully
received. The delivery of a push promise response, however, is not
coordinated with the delivery of the response to the initiating
client-sent request.

A

push promise

is a synthetic request sent by an HTTP/2 server
when retrieving an initiating client-sent request. The server has
determined, possibly through inspection of the initiating request, that
the client will likely need the promised resource, and hence pushes a
synthetic push request, in the form of a push promise, to the client. The
client can choose to accept or reject the push promise request.

A push promise request may be received up to the point where the
response body of the initiating client-sent request has been fully
received. The delivery of a push promise response, however, is not
coordinated with the delivery of the response to the initiating
client-sent request.

A push promise request may be received up to the point where the
response body of the initiating client-sent request has been fully
received. The delivery of a push promise response, however, is not
coordinated with the delivery of the response to the initiating
client-sent request.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

applyPushPromise

​(

HttpRequest

initiatingRequest,

HttpRequest

pushPromiseRequest,

Function

<

HttpResponse.BodyHandler

<

T

>,​

CompletableFuture

<

HttpResponse

<

T

>>> acceptor)

Notification of an incoming push promise.

static <T>

HttpResponse.PushPromiseHandler

<T>

of

​(

Function

<

HttpRequest

,​

HttpResponse.BodyHandler

<T>> pushPromiseHandler,

ConcurrentMap

<

HttpRequest

,​

CompletableFuture

<

HttpResponse

<T>>> pushPromisesMap)

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

applyPushPromise

​(

HttpRequest

initiatingRequest,

HttpRequest

pushPromiseRequest,

Function

<

HttpResponse.BodyHandler

<

T

>,​

CompletableFuture

<

HttpResponse

<

T

>>> acceptor)

Notification of an incoming push promise.

static <T>

HttpResponse.PushPromiseHandler

<T>

of

​(

Function

<

HttpRequest

,​

HttpResponse.BodyHandler

<T>> pushPromiseHandler,

ConcurrentMap

<

HttpRequest

,​

CompletableFuture

<

HttpResponse

<T>>> pushPromisesMap)

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

---

#### Method Summary

Notification of an incoming push promise.

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

============ METHOD DETAIL ==========

- Method Detail

- applyPushPromise

```java
void applyPushPromise​(
HttpRequest
initiatingRequest,

HttpRequest
pushPromiseRequest,

Function
<
HttpResponse.BodyHandler
<
T
>,​
CompletableFuture
<
HttpResponse
<
T
>>> acceptor)
```

Notification of an incoming push promise.

This method is invoked once for each push promise received, up
to the point where the response body of the initiating client-sent
request has been fully received.

A push promise is accepted by invoking the given

acceptor

function. The

acceptor

function must be passed a non-null

BodyHandler

, that is to be used to handle the promise's
response body. The acceptor function will return a

CompletableFuture

that completes with the promise's response.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

**Parameters:** initiatingRequest

- the initiating client-send request
**Parameters:** pushPromiseRequest

- the synthetic push request
**Parameters:** acceptor

- the acceptor function that must be successfully
invoked to accept the push promise

- of

```java
static <T>
HttpResponse.PushPromiseHandler
<T> of​(
Function
<
HttpRequest
,​
HttpResponse.BodyHandler
<T>> pushPromiseHandler,

ConcurrentMap
<
HttpRequest
,​
CompletableFuture
<
HttpResponse
<T>>> pushPromisesMap)
```

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

Entries are added to the given map for each push promise accepted.
The entry's key is the push request, and the entry's value is a

CompletableFuture

that completes with the response
corresponding to the key's push request. A push request is rejected /
cancelled if there is already an entry in the map whose key is

equal

to it. A push request is
rejected / cancelled if it does not have the same origin as its
initiating request.

Entries are added to the given map as soon as practically
possible when a push promise is received and accepted. That way code,
using such a map like a cache, can determine if a push promise has
been issued by the server and avoid making, possibly, unnecessary
requests.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

**Type Parameters:** T

- the push promise response body type
**Parameters:** pushPromiseHandler

- t he body handler to use for push promises
**Parameters:** pushPromisesMap

- a map to accumulate push promises into
**Returns:** a push promise handler

Method Detail

- applyPushPromise

```java
void applyPushPromise​(
HttpRequest
initiatingRequest,

HttpRequest
pushPromiseRequest,

Function
<
HttpResponse.BodyHandler
<
T
>,​
CompletableFuture
<
HttpResponse
<
T
>>> acceptor)
```

Notification of an incoming push promise.

This method is invoked once for each push promise received, up
to the point where the response body of the initiating client-sent
request has been fully received.

A push promise is accepted by invoking the given

acceptor

function. The

acceptor

function must be passed a non-null

BodyHandler

, that is to be used to handle the promise's
response body. The acceptor function will return a

CompletableFuture

that completes with the promise's response.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

**Parameters:** initiatingRequest

- the initiating client-send request
**Parameters:** pushPromiseRequest

- the synthetic push request
**Parameters:** acceptor

- the acceptor function that must be successfully
invoked to accept the push promise

- of

```java
static <T>
HttpResponse.PushPromiseHandler
<T> of​(
Function
<
HttpRequest
,​
HttpResponse.BodyHandler
<T>> pushPromiseHandler,

ConcurrentMap
<
HttpRequest
,​
CompletableFuture
<
HttpResponse
<T>>> pushPromisesMap)
```

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

Entries are added to the given map for each push promise accepted.
The entry's key is the push request, and the entry's value is a

CompletableFuture

that completes with the response
corresponding to the key's push request. A push request is rejected /
cancelled if there is already an entry in the map whose key is

equal

to it. A push request is
rejected / cancelled if it does not have the same origin as its
initiating request.

Entries are added to the given map as soon as practically
possible when a push promise is received and accepted. That way code,
using such a map like a cache, can determine if a push promise has
been issued by the server and avoid making, possibly, unnecessary
requests.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

**Type Parameters:** T

- the push promise response body type
**Parameters:** pushPromiseHandler

- t he body handler to use for push promises
**Parameters:** pushPromisesMap

- a map to accumulate push promises into
**Returns:** a push promise handler

---

#### Method Detail

applyPushPromise

```java
void applyPushPromise​(
HttpRequest
initiatingRequest,

HttpRequest
pushPromiseRequest,

Function
<
HttpResponse.BodyHandler
<
T
>,​
CompletableFuture
<
HttpResponse
<
T
>>> acceptor)
```

Notification of an incoming push promise.

This method is invoked once for each push promise received, up
to the point where the response body of the initiating client-sent
request has been fully received.

A push promise is accepted by invoking the given

acceptor

function. The

acceptor

function must be passed a non-null

BodyHandler

, that is to be used to handle the promise's
response body. The acceptor function will return a

CompletableFuture

that completes with the promise's response.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

**Parameters:** initiatingRequest

- the initiating client-send request
**Parameters:** pushPromiseRequest

- the synthetic push request
**Parameters:** acceptor

- the acceptor function that must be successfully
invoked to accept the push promise

---

#### applyPushPromise

void applyPushPromise​(

HttpRequest

initiatingRequest,

HttpRequest

pushPromiseRequest,

Function

<

HttpResponse.BodyHandler

<

T

>,​

CompletableFuture

<

HttpResponse

<

T

>>> acceptor)

Notification of an incoming push promise.

This method is invoked once for each push promise received, up
to the point where the response body of the initiating client-sent
request has been fully received.

A push promise is accepted by invoking the given

acceptor

function. The

acceptor

function must be passed a non-null

BodyHandler

, that is to be used to handle the promise's
response body. The acceptor function will return a

CompletableFuture

that completes with the promise's response.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

This method is invoked once for each push promise received, up
to the point where the response body of the initiating client-sent
request has been fully received.

A push promise is accepted by invoking the given

acceptor

function. The

acceptor

function must be passed a non-null

BodyHandler

, that is to be used to handle the promise's
response body. The acceptor function will return a

CompletableFuture

that completes with the promise's response.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

A push promise is accepted by invoking the given

acceptor

function. The

acceptor

function must be passed a non-null

BodyHandler

, that is to be used to handle the promise's
response body. The acceptor function will return a

CompletableFuture

that completes with the promise's response.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

If the

acceptor

function is not successfully invoked,
then the push promise is rejected. The

acceptor

function will
throw an

IllegalStateException

if invoked more than once.

of

```java
static <T>
HttpResponse.PushPromiseHandler
<T> of​(
Function
<
HttpRequest
,​
HttpResponse.BodyHandler
<T>> pushPromiseHandler,

ConcurrentMap
<
HttpRequest
,​
CompletableFuture
<
HttpResponse
<T>>> pushPromisesMap)
```

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

Entries are added to the given map for each push promise accepted.
The entry's key is the push request, and the entry's value is a

CompletableFuture

that completes with the response
corresponding to the key's push request. A push request is rejected /
cancelled if there is already an entry in the map whose key is

equal

to it. A push request is
rejected / cancelled if it does not have the same origin as its
initiating request.

Entries are added to the given map as soon as practically
possible when a push promise is received and accepted. That way code,
using such a map like a cache, can determine if a push promise has
been issued by the server and avoid making, possibly, unnecessary
requests.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

**Type Parameters:** T

- the push promise response body type
**Parameters:** pushPromiseHandler

- t he body handler to use for push promises
**Parameters:** pushPromisesMap

- a map to accumulate push promises into
**Returns:** a push promise handler

---

#### of

static <T>

HttpResponse.PushPromiseHandler

<T> of​(

Function

<

HttpRequest

,​

HttpResponse.BodyHandler

<T>> pushPromiseHandler,

ConcurrentMap

<

HttpRequest

,​

CompletableFuture

<

HttpResponse

<T>>> pushPromisesMap)

Returns a push promise handler that accumulates push promises, and
their responses, into the given map.

Entries are added to the given map for each push promise accepted.
The entry's key is the push request, and the entry's value is a

CompletableFuture

that completes with the response
corresponding to the key's push request. A push request is rejected /
cancelled if there is already an entry in the map whose key is

equal

to it. A push request is
rejected / cancelled if it does not have the same origin as its
initiating request.

Entries are added to the given map as soon as practically
possible when a push promise is received and accepted. That way code,
using such a map like a cache, can determine if a push promise has
been issued by the server and avoid making, possibly, unnecessary
requests.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

Entries are added to the given map for each push promise accepted.
The entry's key is the push request, and the entry's value is a

CompletableFuture

that completes with the response
corresponding to the key's push request. A push request is rejected /
cancelled if there is already an entry in the map whose key is

equal

to it. A push request is
rejected / cancelled if it does not have the same origin as its
initiating request.

Entries are added to the given map as soon as practically
possible when a push promise is received and accepted. That way code,
using such a map like a cache, can determine if a push promise has
been issued by the server and avoid making, possibly, unnecessary
requests.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

Entries are added to the given map as soon as practically
possible when a push promise is received and accepted. That way code,
using such a map like a cache, can determine if a push promise has
been issued by the server and avoid making, possibly, unnecessary
requests.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

The delivery of a push promise response is not coordinated with
the delivery of the response to the initiating client-sent request.
However, when the response body for the initiating client-sent
request has been fully received, the map is guaranteed to be fully
populated, that is, no more entries will be added. The individual

CompletableFutures

contained in the map may or may not
already be completed at this point.

---

