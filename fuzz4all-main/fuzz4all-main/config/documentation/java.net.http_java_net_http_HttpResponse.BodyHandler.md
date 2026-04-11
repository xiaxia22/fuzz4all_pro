# Interface HttpResponse.BodyHandler<T>

**Source:** `java.net.http\java\net\http\HttpResponse.BodyHandler.html`

### Class Description

```java
@FunctionalInterface

public static interface
HttpResponse.BodyHandler<T>
```

A handler for response bodies. The class

BodyHandlers

provides implementations of many common body handlers.

The

BodyHandler

interface allows inspection of the response
code and headers, before the actual response body is received, and is
responsible for creating the response

BodySubscriber

. The

BodySubscriber

consumes the actual response
body bytes and, typically, converts them into a higher-level Java type.

A

BodyHandler

is a function that takes a

ResponseInfo

object; and which returns a

BodySubscriber

. The

BodyHandler

is invoked when the response status code and headers
are available, but before the response body bytes are received.

The following example uses one of the

predefined body handlers

that always process the response body in the
same way ( streams the response body to a file ).

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofFile(Paths.get("/tmp/f")))
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Note, that even though the pre-defined handlers do not examine the
response code, the response code and headers are always retrievable from
the

HttpResponse

, when it is returned.

In the second example, the function returns a different subscriber
depending on the status code.

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

**Type Parameters:** T

- the response body type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### HttpResponse.BodySubscriber
<
T
> apply​(
HttpResponse.ResponseInfo
responseInfo)

Returns a

BodySubscriber

considering the
given response status code and headers. This method is invoked before
the actual response body bytes are read and its implementation must
return a

BodySubscriber

to consume the response
body bytes.

The response body can be discarded using one of

discarding

or

replacing

.

**Parameters:**
- responseInfo

- the response info

**Returns:**
- a body subscriber

---

### Additional Sections

#### Interface HttpResponse.BodyHandler<T>

**Type Parameters:** T

- the response body type

**Enclosing interface:** HttpResponse

<

T

>

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public static interface
HttpResponse.BodyHandler<T>
```

A handler for response bodies. The class

BodyHandlers

provides implementations of many common body handlers.

The

BodyHandler

interface allows inspection of the response
code and headers, before the actual response body is received, and is
responsible for creating the response

BodySubscriber

. The

BodySubscriber

consumes the actual response
body bytes and, typically, converts them into a higher-level Java type.

A

BodyHandler

is a function that takes a

ResponseInfo

object; and which returns a

BodySubscriber

. The

BodyHandler

is invoked when the response status code and headers
are available, but before the response body bytes are received.

The following example uses one of the

predefined body handlers

that always process the response body in the
same way ( streams the response body to a file ).

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofFile(Paths.get("/tmp/f")))
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Note, that even though the pre-defined handlers do not examine the
response code, the response code and headers are always retrievable from
the

HttpResponse

, when it is returned.

In the second example, the function returns a different subscriber
depending on the status code.

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

**Since:** 11
**See Also:** HttpResponse.BodyHandlers

@FunctionalInterface

public static interface

HttpResponse.BodyHandler<T>

A handler for response bodies. The class

BodyHandlers

provides implementations of many common body handlers.

The

BodyHandler

interface allows inspection of the response
code and headers, before the actual response body is received, and is
responsible for creating the response

BodySubscriber

. The

BodySubscriber

consumes the actual response
body bytes and, typically, converts them into a higher-level Java type.

A

BodyHandler

is a function that takes a

ResponseInfo

object; and which returns a

BodySubscriber

. The

BodyHandler

is invoked when the response status code and headers
are available, but before the response body bytes are received.

The following example uses one of the

predefined body handlers

that always process the response body in the
same way ( streams the response body to a file ).

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofFile(Paths.get("/tmp/f")))
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Note, that even though the pre-defined handlers do not examine the
response code, the response code and headers are always retrievable from
the

HttpResponse

, when it is returned.

In the second example, the function returns a different subscriber
depending on the status code.

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

The

BodyHandler

interface allows inspection of the response
code and headers, before the actual response body is received, and is
responsible for creating the response

BodySubscriber

. The

BodySubscriber

consumes the actual response
body bytes and, typically, converts them into a higher-level Java type.

A

BodyHandler

is a function that takes a

ResponseInfo

object; and which returns a

BodySubscriber

. The

BodyHandler

is invoked when the response status code and headers
are available, but before the response body bytes are received.

The following example uses one of the

predefined body handlers

that always process the response body in the
same way ( streams the response body to a file ).

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofFile(Paths.get("/tmp/f")))
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Note, that even though the pre-defined handlers do not examine the
response code, the response code and headers are always retrievable from
the

HttpResponse

, when it is returned.

In the second example, the function returns a different subscriber
depending on the status code.

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

A

BodyHandler

is a function that takes a

ResponseInfo

object; and which returns a

BodySubscriber

. The

BodyHandler

is invoked when the response status code and headers
are available, but before the response body bytes are received.

The following example uses one of the

predefined body handlers

that always process the response body in the
same way ( streams the response body to a file ).

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofFile(Paths.get("/tmp/f")))
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Note, that even though the pre-defined handlers do not examine the
response code, the response code and headers are always retrievable from
the

HttpResponse

, when it is returned.

In the second example, the function returns a different subscriber
depending on the status code.

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

The following example uses one of the

predefined body handlers

that always process the response body in the
same way ( streams the response body to a file ).

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofFile(Paths.get("/tmp/f")))
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Note, that even though the pre-defined handlers do not examine the
response code, the response code and headers are always retrievable from
the

HttpResponse

, when it is returned.

In the second example, the function returns a different subscriber
depending on the status code.

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofFile(Paths.get("/tmp/f")))
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);

In the second example, the function returns a different subscriber
depending on the status code.

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://www.foo.com/"))
.build();
BodyHandler<Path> bodyHandler = (rspInfo) -> rspInfo.statusCode() == 200
? BodySubscribers.ofFile(Paths.get("/tmp/f"))
: BodySubscribers.replacing(Paths.get("/NULL"));
client.sendAsync(request, bodyHandler)
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpResponse.BodySubscriber

<

T

>

apply

​(

HttpResponse.ResponseInfo

responseInfo)

Returns a

BodySubscriber

considering the
given response status code and headers.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpResponse.BodySubscriber

<

T

>

apply

​(

HttpResponse.ResponseInfo

responseInfo)

Returns a

BodySubscriber

considering the
given response status code and headers.

---

#### Method Summary

Returns a

BodySubscriber

considering the
given response status code and headers.

============ METHOD DETAIL ==========

- Method Detail

- apply

```java
HttpResponse.BodySubscriber
<
T
> apply​(
HttpResponse.ResponseInfo
responseInfo)
```

Returns a

BodySubscriber

considering the
given response status code and headers. This method is invoked before
the actual response body bytes are read and its implementation must
return a

BodySubscriber

to consume the response
body bytes.

The response body can be discarded using one of

discarding

or

replacing

.

**Parameters:** responseInfo

- the response info
**Returns:** a body subscriber

Method Detail

- apply

```java
HttpResponse.BodySubscriber
<
T
> apply​(
HttpResponse.ResponseInfo
responseInfo)
```

Returns a

BodySubscriber

considering the
given response status code and headers. This method is invoked before
the actual response body bytes are read and its implementation must
return a

BodySubscriber

to consume the response
body bytes.

The response body can be discarded using one of

discarding

or

replacing

.

**Parameters:** responseInfo

- the response info
**Returns:** a body subscriber

---

#### Method Detail

apply

```java
HttpResponse.BodySubscriber
<
T
> apply​(
HttpResponse.ResponseInfo
responseInfo)
```

Returns a

BodySubscriber

considering the
given response status code and headers. This method is invoked before
the actual response body bytes are read and its implementation must
return a

BodySubscriber

to consume the response
body bytes.

The response body can be discarded using one of

discarding

or

replacing

.

**Parameters:** responseInfo

- the response info
**Returns:** a body subscriber

---

#### apply

HttpResponse.BodySubscriber

<

T

> apply​(

HttpResponse.ResponseInfo

responseInfo)

Returns a

BodySubscriber

considering the
given response status code and headers. This method is invoked before
the actual response body bytes are read and its implementation must
return a

BodySubscriber

to consume the response
body bytes.

The response body can be discarded using one of

discarding

or

replacing

.

The response body can be discarded using one of

discarding

or

replacing

.

---

