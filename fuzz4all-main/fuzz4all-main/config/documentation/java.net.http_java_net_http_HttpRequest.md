# Class HttpRequest

**Source:** `java.net.http\java\net\http\HttpRequest.html`

### Class Description

```java
public abstract class
HttpRequest

extends
Object
```

An HTTP request.

An

HttpRequest

instance is built through an

HttpRequest

builder

. An

HttpRequest

builder
is obtained from one of the

newBuilder

methods. A request's

URI

, headers, and body can be set. Request
bodies are provided through a

BodyPublisher

supplied
to one of the

POST

,

PUT

or

method

methods.
Once all required parameters have been set in the builder,

build

will return the

HttpRequest

. Builders can be
copied and modified many times in order to build multiple related requests
that differ in some parameters.

The following is an example of a GET request that prints the response
body as a String:

```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println)
.join();
```

The class

BodyPublishers

provides implementations
of many common publishers. Alternatively, a custom

BodyPublisher

implementation can be used.

**Since:** 11

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpRequest()

Creates an HttpRequest.

---

### Method Details

#### public static
HttpRequest.Builder
newBuilder​(
URI
uri)

Creates an

HttpRequest

builder with the given URI.

**Parameters:**
- uri

- the request URI

**Returns:**
- a new request builder

**Throws:**
- IllegalArgumentException

- if the URI scheme is not supported.

---

#### public static
HttpRequest.Builder
newBuilder()

Creates an

HttpRequest

builder.

**Returns:**
- a new request builder

---

#### public abstract
Optional
<
HttpRequest.BodyPublisher
> bodyPublisher()

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request. If no

BodyPublisher

was set in the requests's
builder, then the

Optional

is empty.

**Returns:**
- an

Optional

containing this request's

BodyPublisher

---

#### public abstract
String
method()

Returns the request method for this request. If not set explicitly,
the default method for any request is "GET".

**Returns:**
- this request's method

---

#### public abstract
Optional
<
Duration
> timeout()

Returns an

Optional

containing this request's timeout duration.
If the timeout duration was not set in the request's builder, then the

Optional

is empty.

**Returns:**
- an

Optional

containing this request's timeout duration

---

#### public abstract boolean expectContinue()

Returns this request's

expect continue

setting.

**Returns:**
- this request's expect continue setting

---

#### public abstract
URI
uri()

Returns this request's

URI

.

**Returns:**
- this request's URI

---

#### public abstract
Optional
<
HttpClient.Version
> version()

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

. If the version was not
set in the request's builder, then the

Optional

is empty.
In that case, the version requested will be that of the sending

HttpClient

. The corresponding

HttpResponse

should be
queried to determine the version that was actually used.

**Returns:**
- HTTP protocol version

---

#### public abstract
HttpHeaders
headers()

The (user-accessible) request headers that this request was (or will be)
sent with.

**Returns:**
- this request's HttpHeaders

---

#### public final boolean equals​(
Object
obj)

Tests this HTTP request instance for equality with the given object.

If the given object is not an

HttpRequest

then this
method returns

false

. Two HTTP requests are equal if their URI,
method, and headers fields are all equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to which this object is to be compared

**Returns:**
- true

if, and only if, the given object is an

HttpRequest

that is equal to this HTTP request

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Computes a hash code for this HTTP request instance.

The hash code is based upon the HTTP request's URI, method, and
header components, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash-code value for this HTTP request

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class HttpRequest

java.lang.Object

- java.net.http.HttpRequest

java.net.http.HttpRequest

```java
public abstract class
HttpRequest

extends
Object
```

An HTTP request.

An

HttpRequest

instance is built through an

HttpRequest

builder

. An

HttpRequest

builder
is obtained from one of the

newBuilder

methods. A request's

URI

, headers, and body can be set. Request
bodies are provided through a

BodyPublisher

supplied
to one of the

POST

,

PUT

or

method

methods.
Once all required parameters have been set in the builder,

build

will return the

HttpRequest

. Builders can be
copied and modified many times in order to build multiple related requests
that differ in some parameters.

The following is an example of a GET request that prints the response
body as a String:

```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println)
.join();
```

The class

BodyPublishers

provides implementations
of many common publishers. Alternatively, a custom

BodyPublisher

implementation can be used.

**Since:** 11

public abstract class

HttpRequest

extends

Object

An HTTP request.

An

HttpRequest

instance is built through an

HttpRequest

builder

. An

HttpRequest

builder
is obtained from one of the

newBuilder

methods. A request's

URI

, headers, and body can be set. Request
bodies are provided through a

BodyPublisher

supplied
to one of the

POST

,

PUT

or

method

methods.
Once all required parameters have been set in the builder,

build

will return the

HttpRequest

. Builders can be
copied and modified many times in order to build multiple related requests
that differ in some parameters.

The following is an example of a GET request that prints the response
body as a String:

```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println)
.join();
```

The class

BodyPublishers

provides implementations
of many common publishers. Alternatively, a custom

BodyPublisher

implementation can be used.

An

HttpRequest

instance is built through an

HttpRequest

builder

. An

HttpRequest

builder
is obtained from one of the

newBuilder

methods. A request's

URI

, headers, and body can be set. Request
bodies are provided through a

BodyPublisher

supplied
to one of the

POST

,

PUT

or

method

methods.
Once all required parameters have been set in the builder,

build

will return the

HttpRequest

. Builders can be
copied and modified many times in order to build multiple related requests
that differ in some parameters.

The following is an example of a GET request that prints the response
body as a String:

```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println)
.join();
```

The class

BodyPublishers

provides implementations
of many common publishers. Alternatively, a custom

BodyPublisher

implementation can be used.

The following is an example of a GET request that prints the response
body as a String:

```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println)
.join();
```

The class

BodyPublishers

provides implementations
of many common publishers. Alternatively, a custom

BodyPublisher

implementation can be used.

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("http://foo.com/"))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println)
.join();

The class

BodyPublishers

provides implementations
of many common publishers. Alternatively, a custom

BodyPublisher

implementation can be used.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

HttpRequest.BodyPublisher

A

BodyPublisher

converts high-level Java objects into a flow of
byte buffers suitable for sending as a request body.

static class

HttpRequest.BodyPublishers

Implementations of

BodyPublisher

that implement
various useful publishers, such as publishing the request body from a
String, or from a file.

static interface

HttpRequest.Builder

A builder of

HTTP requests

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpRequest

()

Creates an HttpRequest.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Optional

<

HttpRequest.BodyPublisher

>

bodyPublisher

()

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request.

boolean

equals

​(

Object

obj)

Tests this HTTP request instance for equality with the given object.

abstract boolean

expectContinue

()

Returns this request's

expect continue

setting.

int

hashCode

()

Computes a hash code for this HTTP request instance.

abstract

HttpHeaders

headers

()

The (user-accessible) request headers that this request was (or will be)
sent with.

abstract

String

method

()

Returns the request method for this request.

static

HttpRequest.Builder

newBuilder

()

Creates an

HttpRequest

builder.

static

HttpRequest.Builder

newBuilder

​(

URI

uri)

Creates an

HttpRequest

builder with the given URI.

abstract

Optional

<

Duration

>

timeout

()

Returns an

Optional

containing this request's timeout duration.

abstract

URI

uri

()

Returns this request's

URI

.

abstract

Optional

<

HttpClient.Version

>

version

()

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

HttpRequest.BodyPublisher

A

BodyPublisher

converts high-level Java objects into a flow of
byte buffers suitable for sending as a request body.

static class

HttpRequest.BodyPublishers

Implementations of

BodyPublisher

that implement
various useful publishers, such as publishing the request body from a
String, or from a file.

static interface

HttpRequest.Builder

A builder of

HTTP requests

.

---

#### Nested Class Summary

A

BodyPublisher

converts high-level Java objects into a flow of
byte buffers suitable for sending as a request body.

Implementations of

BodyPublisher

that implement
various useful publishers, such as publishing the request body from a
String, or from a file.

A builder of

HTTP requests

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpRequest

()

Creates an HttpRequest.

---

#### Constructor Summary

Creates an HttpRequest.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Optional

<

HttpRequest.BodyPublisher

>

bodyPublisher

()

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request.

boolean

equals

​(

Object

obj)

Tests this HTTP request instance for equality with the given object.

abstract boolean

expectContinue

()

Returns this request's

expect continue

setting.

int

hashCode

()

Computes a hash code for this HTTP request instance.

abstract

HttpHeaders

headers

()

The (user-accessible) request headers that this request was (or will be)
sent with.

abstract

String

method

()

Returns the request method for this request.

static

HttpRequest.Builder

newBuilder

()

Creates an

HttpRequest

builder.

static

HttpRequest.Builder

newBuilder

​(

URI

uri)

Creates an

HttpRequest

builder with the given URI.

abstract

Optional

<

Duration

>

timeout

()

Returns an

Optional

containing this request's timeout duration.

abstract

URI

uri

()

Returns this request's

URI

.

abstract

Optional

<

HttpClient.Version

>

version

()

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request.

Tests this HTTP request instance for equality with the given object.

Returns this request's

expect continue

setting.

Computes a hash code for this HTTP request instance.

The (user-accessible) request headers that this request was (or will be)
sent with.

Returns the request method for this request.

Creates an

HttpRequest

builder.

Creates an

HttpRequest

builder with the given URI.

Returns an

Optional

containing this request's timeout duration.

Returns this request's

URI

.

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- HttpRequest

```java
protected HttpRequest()
```

Creates an HttpRequest.

============ METHOD DETAIL ==========

- Method Detail

- newBuilder

```java
public static
HttpRequest.Builder
newBuilder​(
URI
uri)
```

Creates an

HttpRequest

builder with the given URI.

**Parameters:** uri

- the request URI
**Returns:** a new request builder
**Throws:** IllegalArgumentException

- if the URI scheme is not supported.

- newBuilder

```java
public static
HttpRequest.Builder
newBuilder()
```

Creates an

HttpRequest

builder.

**Returns:** a new request builder

- bodyPublisher

```java
public abstract
Optional
<
HttpRequest.BodyPublisher
> bodyPublisher()
```

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request. If no

BodyPublisher

was set in the requests's
builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this request's

BodyPublisher

- method

```java
public abstract
String
method()
```

Returns the request method for this request. If not set explicitly,
the default method for any request is "GET".

**Returns:** this request's method

- timeout

```java
public abstract
Optional
<
Duration
> timeout()
```

Returns an

Optional

containing this request's timeout duration.
If the timeout duration was not set in the request's builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this request's timeout duration

- expectContinue

```java
public abstract boolean expectContinue()
```

Returns this request's

expect continue

setting.

**Returns:** this request's expect continue setting

- uri

```java
public abstract
URI
uri()
```

Returns this request's

URI

.

**Returns:** this request's URI

- version

```java
public abstract
Optional
<
HttpClient.Version
> version()
```

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

. If the version was not
set in the request's builder, then the

Optional

is empty.
In that case, the version requested will be that of the sending

HttpClient

. The corresponding

HttpResponse

should be
queried to determine the version that was actually used.

**Returns:** HTTP protocol version

- headers

```java
public abstract
HttpHeaders
headers()
```

The (user-accessible) request headers that this request was (or will be)
sent with.

**Returns:** this request's HttpHeaders

- equals

```java
public final boolean equals​(
Object
obj)
```

Tests this HTTP request instance for equality with the given object.

If the given object is not an

HttpRequest

then this
method returns

false

. Two HTTP requests are equal if their URI,
method, and headers fields are all equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an

HttpRequest

that is equal to this HTTP request
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Computes a hash code for this HTTP request instance.

The hash code is based upon the HTTP request's URI, method, and
header components, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** the hash-code value for this HTTP request
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- HttpRequest

```java
protected HttpRequest()
```

Creates an HttpRequest.

---

#### Constructor Detail

HttpRequest

```java
protected HttpRequest()
```

Creates an HttpRequest.

---

#### HttpRequest

protected HttpRequest()

Creates an HttpRequest.

Method Detail

- newBuilder

```java
public static
HttpRequest.Builder
newBuilder​(
URI
uri)
```

Creates an

HttpRequest

builder with the given URI.

**Parameters:** uri

- the request URI
**Returns:** a new request builder
**Throws:** IllegalArgumentException

- if the URI scheme is not supported.

- newBuilder

```java
public static
HttpRequest.Builder
newBuilder()
```

Creates an

HttpRequest

builder.

**Returns:** a new request builder

- bodyPublisher

```java
public abstract
Optional
<
HttpRequest.BodyPublisher
> bodyPublisher()
```

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request. If no

BodyPublisher

was set in the requests's
builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this request's

BodyPublisher

- method

```java
public abstract
String
method()
```

Returns the request method for this request. If not set explicitly,
the default method for any request is "GET".

**Returns:** this request's method

- timeout

```java
public abstract
Optional
<
Duration
> timeout()
```

Returns an

Optional

containing this request's timeout duration.
If the timeout duration was not set in the request's builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this request's timeout duration

- expectContinue

```java
public abstract boolean expectContinue()
```

Returns this request's

expect continue

setting.

**Returns:** this request's expect continue setting

- uri

```java
public abstract
URI
uri()
```

Returns this request's

URI

.

**Returns:** this request's URI

- version

```java
public abstract
Optional
<
HttpClient.Version
> version()
```

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

. If the version was not
set in the request's builder, then the

Optional

is empty.
In that case, the version requested will be that of the sending

HttpClient

. The corresponding

HttpResponse

should be
queried to determine the version that was actually used.

**Returns:** HTTP protocol version

- headers

```java
public abstract
HttpHeaders
headers()
```

The (user-accessible) request headers that this request was (or will be)
sent with.

**Returns:** this request's HttpHeaders

- equals

```java
public final boolean equals​(
Object
obj)
```

Tests this HTTP request instance for equality with the given object.

If the given object is not an

HttpRequest

then this
method returns

false

. Two HTTP requests are equal if their URI,
method, and headers fields are all equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an

HttpRequest

that is equal to this HTTP request
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Computes a hash code for this HTTP request instance.

The hash code is based upon the HTTP request's URI, method, and
header components, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** the hash-code value for this HTTP request
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

newBuilder

```java
public static
HttpRequest.Builder
newBuilder​(
URI
uri)
```

Creates an

HttpRequest

builder with the given URI.

**Parameters:** uri

- the request URI
**Returns:** a new request builder
**Throws:** IllegalArgumentException

- if the URI scheme is not supported.

---

#### newBuilder

public static

HttpRequest.Builder

newBuilder​(

URI

uri)

Creates an

HttpRequest

builder with the given URI.

newBuilder

```java
public static
HttpRequest.Builder
newBuilder()
```

Creates an

HttpRequest

builder.

**Returns:** a new request builder

---

#### newBuilder

public static

HttpRequest.Builder

newBuilder()

Creates an

HttpRequest

builder.

bodyPublisher

```java
public abstract
Optional
<
HttpRequest.BodyPublisher
> bodyPublisher()
```

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request. If no

BodyPublisher

was set in the requests's
builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this request's

BodyPublisher

---

#### bodyPublisher

public abstract

Optional

<

HttpRequest.BodyPublisher

> bodyPublisher()

Returns an

Optional

containing the

HttpRequest.BodyPublisher

set on
this request. If no

BodyPublisher

was set in the requests's
builder, then the

Optional

is empty.

method

```java
public abstract
String
method()
```

Returns the request method for this request. If not set explicitly,
the default method for any request is "GET".

**Returns:** this request's method

---

#### method

public abstract

String

method()

Returns the request method for this request. If not set explicitly,
the default method for any request is "GET".

timeout

```java
public abstract
Optional
<
Duration
> timeout()
```

Returns an

Optional

containing this request's timeout duration.
If the timeout duration was not set in the request's builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this request's timeout duration

---

#### timeout

public abstract

Optional

<

Duration

> timeout()

Returns an

Optional

containing this request's timeout duration.
If the timeout duration was not set in the request's builder, then the

Optional

is empty.

expectContinue

```java
public abstract boolean expectContinue()
```

Returns this request's

expect continue

setting.

**Returns:** this request's expect continue setting

---

#### expectContinue

public abstract boolean expectContinue()

Returns this request's

expect continue

setting.

uri

```java
public abstract
URI
uri()
```

Returns this request's

URI

.

**Returns:** this request's URI

---

#### uri

public abstract

URI

uri()

Returns this request's

URI

.

version

```java
public abstract
Optional
<
HttpClient.Version
> version()
```

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

. If the version was not
set in the request's builder, then the

Optional

is empty.
In that case, the version requested will be that of the sending

HttpClient

. The corresponding

HttpResponse

should be
queried to determine the version that was actually used.

**Returns:** HTTP protocol version

---

#### version

public abstract

Optional

<

HttpClient.Version

> version()

Returns an

Optional

containing the HTTP protocol version that
will be requested for this

HttpRequest

. If the version was not
set in the request's builder, then the

Optional

is empty.
In that case, the version requested will be that of the sending

HttpClient

. The corresponding

HttpResponse

should be
queried to determine the version that was actually used.

headers

```java
public abstract
HttpHeaders
headers()
```

The (user-accessible) request headers that this request was (or will be)
sent with.

**Returns:** this request's HttpHeaders

---

#### headers

public abstract

HttpHeaders

headers()

The (user-accessible) request headers that this request was (or will be)
sent with.

equals

```java
public final boolean equals​(
Object
obj)
```

Tests this HTTP request instance for equality with the given object.

If the given object is not an

HttpRequest

then this
method returns

false

. Two HTTP requests are equal if their URI,
method, and headers fields are all equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an

HttpRequest

that is equal to this HTTP request
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Tests this HTTP request instance for equality with the given object.

If the given object is not an

HttpRequest

then this
method returns

false

. Two HTTP requests are equal if their URI,
method, and headers fields are all equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not an

HttpRequest

then this
method returns

false

. Two HTTP requests are equal if their URI,
method, and headers fields are all equal.

This method satisfies the general contract of the

Object.equals

method.

This method satisfies the general contract of the

Object.equals

method.

hashCode

```java
public final int hashCode()
```

Computes a hash code for this HTTP request instance.

The hash code is based upon the HTTP request's URI, method, and
header components, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** the hash-code value for this HTTP request
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Computes a hash code for this HTTP request instance.

The hash code is based upon the HTTP request's URI, method, and
header components, and satisfies the general contract of the

Object.hashCode

method.

The hash code is based upon the HTTP request's URI, method, and
header components, and satisfies the general contract of the

Object.hashCode

method.

---

