# Interface HttpRequest.Builder

**Source:** `java.net.http\java\net\http\HttpRequest.Builder.html`

### Class Description

```java
public static interface
HttpRequest.Builder
```

A builder of

HTTP requests

.

Instances of

HttpRequest.Builder

are created by calling

HttpRequest.newBuilder(URI)

or

HttpRequest.newBuilder()

.

The builder can be used to configure per-request state, such as: the
request URI, the request method (default is GET unless explicitly set),
specific request headers, etc. Each of the setter methods modifies the
state of the builder and returns the same instance. The methods are not
synchronized and should not be called from multiple threads without
external synchronization. The

build

method returns a new

HttpRequest

each time it is invoked. Once built an

HttpRequest

is immutable, and can be sent multiple times.

Note, that not all request headers may be set by user code. Some are
restricted for security reasons and others such as the headers relating
to authentication, redirection and cookie management may be managed by
specific APIs rather than through directly user set headers.

**Enclosing class:** HttpRequest

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### HttpRequest.Builder
uri​(
URI
uri)

Sets this

HttpRequest

's request

URI

.

**Parameters:**
- uri

- the request URI

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if the

URI

scheme is not
supported

---

#### HttpRequest.Builder
expectContinue​(boolean enable)

Requests the server to acknowledge the request before sending the
body. This is disabled by default. If enabled, the server is
requested to send an error response or a

100 Continue

response before the client sends the request body. This means the
request publisher for the request will not be invoked until this
interim response is received.

**Parameters:**
- enable

-

true

if Expect continue to be sent

**Returns:**
- this builder

---

#### HttpRequest.Builder
version​(
HttpClient.Version
version)

Sets the preferred

HttpClient.Version

for this request.

The corresponding

HttpResponse

should be checked for the
version that was actually used. If the version is not set in a
request, then the version requested will be that of the sending

HttpClient

.

**Parameters:**
- version

- the HTTP protocol version requested

**Returns:**
- this builder

---

#### HttpRequest.Builder
header​(
String
name,

String
value)

Adds the given name value pair to the set of headers for this request.
The given value is added to the list of values for that name.

**Parameters:**
- name

- the header name
- value

- the header value

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if the header name or value is not
valid, see

RFC 7230 section-3.2

, or the header name or value is restricted
by the implementation.

**Implementation Note:**
- An implementation may choose to restrict some header names
or values, as the HTTP Client may determine their value itself.
For example, "Content-Length", which will be determined by
the request Publisher. In such a case, an implementation of

HttpRequest.Builder

may choose to throw an

IllegalArgumentException

if such a header is passed
to the builder.

---

#### HttpRequest.Builder
headers​(
String
... headers)

Adds the given name value pairs to the set of headers for this
request. The supplied

String

instances must alternate as
header names and header values.
To add several values to the same name then the same name must
be supplied with each new value.

**Parameters:**
- headers

- the list of name value pairs

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if there are an odd number of
parameters, or if a header name or value is not valid, see

RFC 7230 section-3.2

, or a header name or value is

restricted

by the
implementation.

---

#### HttpRequest.Builder
timeout​(
Duration
duration)

Sets a timeout for this request. If the response is not received
within the specified timeout then an

HttpTimeoutException

is
thrown from

HttpClient::send

or

HttpClient::sendAsync

completes exceptionally with an

HttpTimeoutException

. The effect
of not setting a timeout is the same as setting an infinite Duration, ie.
block forever.

**Parameters:**
- duration

- the timeout duration

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if the duration is non-positive

---

#### HttpRequest.Builder
setHeader​(
String
name,

String
value)

Sets the given name value pair to the set of headers for this
request. This overwrites any previously set values for name.

**Parameters:**
- name

- the header name
- value

- the header value

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if the header name or value is not valid,
see

RFC 7230 section-3.2

, or the header name or value is

restricted

by the
implementation.

---

#### HttpRequest.Builder
GET()

Sets the request method of this builder to GET.
This is the default.

**Returns:**
- this builder

---

#### HttpRequest.Builder
POST​(
HttpRequest.BodyPublisher
bodyPublisher)

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

**Parameters:**
- bodyPublisher

- the body publisher

**Returns:**
- this builder

---

#### HttpRequest.Builder
PUT​(
HttpRequest.BodyPublisher
bodyPublisher)

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

**Parameters:**
- bodyPublisher

- the body publisher

**Returns:**
- this builder

---

#### HttpRequest.Builder
DELETE()

Sets the request method of this builder to DELETE.

**Returns:**
- this builder

---

#### HttpRequest.Builder
method​(
String
method,

HttpRequest.BodyPublisher
bodyPublisher)

Sets the request method and request body of this builder to the
given values.

**Parameters:**
- method

- the method to use
- bodyPublisher

- the body publisher

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if the method name is not
valid, see

RFC 7230 section-3.1.1

, or the method is restricted by the
implementation.

**API Note:**
- The

noBody

request
body publisher can be used where no request body is required or
appropriate. Whether a method is restricted, or not, is
implementation specific. For example, some implementations may choose
to restrict the

CONNECT

method.

---

#### HttpRequest
build()

Builds and returns an

HttpRequest

.

**Returns:**
- a new

HttpRequest

**Throws:**
- IllegalStateException

- if a URI has not been set

---

#### HttpRequest.Builder
copy()

Returns an exact duplicate copy of this

Builder

based on
current state. The new builder can then be modified independently of
this builder.

**Returns:**
- an exact copy of this builder

---

### Additional Sections

#### Interface HttpRequest.Builder

**Enclosing class:** HttpRequest

```java
public static interface
HttpRequest.Builder
```

A builder of

HTTP requests

.

Instances of

HttpRequest.Builder

are created by calling

HttpRequest.newBuilder(URI)

or

HttpRequest.newBuilder()

.

The builder can be used to configure per-request state, such as: the
request URI, the request method (default is GET unless explicitly set),
specific request headers, etc. Each of the setter methods modifies the
state of the builder and returns the same instance. The methods are not
synchronized and should not be called from multiple threads without
external synchronization. The

build

method returns a new

HttpRequest

each time it is invoked. Once built an

HttpRequest

is immutable, and can be sent multiple times.

Note, that not all request headers may be set by user code. Some are
restricted for security reasons and others such as the headers relating
to authentication, redirection and cookie management may be managed by
specific APIs rather than through directly user set headers.

**Since:** 11

public static interface

HttpRequest.Builder

A builder of

HTTP requests

.

Instances of

HttpRequest.Builder

are created by calling

HttpRequest.newBuilder(URI)

or

HttpRequest.newBuilder()

.

The builder can be used to configure per-request state, such as: the
request URI, the request method (default is GET unless explicitly set),
specific request headers, etc. Each of the setter methods modifies the
state of the builder and returns the same instance. The methods are not
synchronized and should not be called from multiple threads without
external synchronization. The

build

method returns a new

HttpRequest

each time it is invoked. Once built an

HttpRequest

is immutable, and can be sent multiple times.

Note, that not all request headers may be set by user code. Some are
restricted for security reasons and others such as the headers relating
to authentication, redirection and cookie management may be managed by
specific APIs rather than through directly user set headers.

Instances of

HttpRequest.Builder

are created by calling

HttpRequest.newBuilder(URI)

or

HttpRequest.newBuilder()

.

The builder can be used to configure per-request state, such as: the
request URI, the request method (default is GET unless explicitly set),
specific request headers, etc. Each of the setter methods modifies the
state of the builder and returns the same instance. The methods are not
synchronized and should not be called from multiple threads without
external synchronization. The

build

method returns a new

HttpRequest

each time it is invoked. Once built an

HttpRequest

is immutable, and can be sent multiple times.

Note, that not all request headers may be set by user code. Some are
restricted for security reasons and others such as the headers relating
to authentication, redirection and cookie management may be managed by
specific APIs rather than through directly user set headers.

The builder can be used to configure per-request state, such as: the
request URI, the request method (default is GET unless explicitly set),
specific request headers, etc. Each of the setter methods modifies the
state of the builder and returns the same instance. The methods are not
synchronized and should not be called from multiple threads without
external synchronization. The

build

method returns a new

HttpRequest

each time it is invoked. Once built an

HttpRequest

is immutable, and can be sent multiple times.

Note, that not all request headers may be set by user code. Some are
restricted for security reasons and others such as the headers relating
to authentication, redirection and cookie management may be managed by
specific APIs rather than through directly user set headers.

Note, that not all request headers may be set by user code. Some are
restricted for security reasons and others such as the headers relating
to authentication, redirection and cookie management may be managed by
specific APIs rather than through directly user set headers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpRequest

build

()

Builds and returns an

HttpRequest

.

HttpRequest.Builder

copy

()

Returns an exact duplicate copy of this

Builder

based on
current state.

HttpRequest.Builder

DELETE

()

Sets the request method of this builder to DELETE.

HttpRequest.Builder

expectContinue

​(boolean enable)

Requests the server to acknowledge the request before sending the
body.

HttpRequest.Builder

GET

()

Sets the request method of this builder to GET.

HttpRequest.Builder

header

​(

String

name,

String

value)

Adds the given name value pair to the set of headers for this request.

HttpRequest.Builder

headers

​(

String

... headers)

Adds the given name value pairs to the set of headers for this
request.

HttpRequest.Builder

method

​(

String

method,

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method and request body of this builder to the
given values.

HttpRequest.Builder

POST

​(

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

HttpRequest.Builder

PUT

​(

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

HttpRequest.Builder

setHeader

​(

String

name,

String

value)

Sets the given name value pair to the set of headers for this
request.

HttpRequest.Builder

timeout

​(

Duration

duration)

Sets a timeout for this request.

HttpRequest.Builder

uri

​(

URI

uri)

Sets this

HttpRequest

's request

URI

.

HttpRequest.Builder

version

​(

HttpClient.Version

version)

Sets the preferred

HttpClient.Version

for this request.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpRequest

build

()

Builds and returns an

HttpRequest

.

HttpRequest.Builder

copy

()

Returns an exact duplicate copy of this

Builder

based on
current state.

HttpRequest.Builder

DELETE

()

Sets the request method of this builder to DELETE.

HttpRequest.Builder

expectContinue

​(boolean enable)

Requests the server to acknowledge the request before sending the
body.

HttpRequest.Builder

GET

()

Sets the request method of this builder to GET.

HttpRequest.Builder

header

​(

String

name,

String

value)

Adds the given name value pair to the set of headers for this request.

HttpRequest.Builder

headers

​(

String

... headers)

Adds the given name value pairs to the set of headers for this
request.

HttpRequest.Builder

method

​(

String

method,

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method and request body of this builder to the
given values.

HttpRequest.Builder

POST

​(

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

HttpRequest.Builder

PUT

​(

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

HttpRequest.Builder

setHeader

​(

String

name,

String

value)

Sets the given name value pair to the set of headers for this
request.

HttpRequest.Builder

timeout

​(

Duration

duration)

Sets a timeout for this request.

HttpRequest.Builder

uri

​(

URI

uri)

Sets this

HttpRequest

's request

URI

.

HttpRequest.Builder

version

​(

HttpClient.Version

version)

Sets the preferred

HttpClient.Version

for this request.

---

#### Method Summary

Builds and returns an

HttpRequest

.

Returns an exact duplicate copy of this

Builder

based on
current state.

Sets the request method of this builder to DELETE.

Requests the server to acknowledge the request before sending the
body.

Sets the request method of this builder to GET.

Adds the given name value pair to the set of headers for this request.

Adds the given name value pairs to the set of headers for this
request.

Sets the request method and request body of this builder to the
given values.

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

Sets the given name value pair to the set of headers for this
request.

Sets a timeout for this request.

Sets this

HttpRequest

's request

URI

.

Sets the preferred

HttpClient.Version

for this request.

============ METHOD DETAIL ==========

- Method Detail

- uri

```java
HttpRequest.Builder
uri​(
URI
uri)
```

Sets this

HttpRequest

's request

URI

.

**Parameters:** uri

- the request URI
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the

URI

scheme is not
supported

- expectContinue

```java
HttpRequest.Builder
expectContinue​(boolean enable)
```

Requests the server to acknowledge the request before sending the
body. This is disabled by default. If enabled, the server is
requested to send an error response or a

100 Continue

response before the client sends the request body. This means the
request publisher for the request will not be invoked until this
interim response is received.

**Parameters:** enable

-

true

if Expect continue to be sent
**Returns:** this builder

- version

```java
HttpRequest.Builder
version​(
HttpClient.Version
version)
```

Sets the preferred

HttpClient.Version

for this request.

The corresponding

HttpResponse

should be checked for the
version that was actually used. If the version is not set in a
request, then the version requested will be that of the sending

HttpClient

.

**Parameters:** version

- the HTTP protocol version requested
**Returns:** this builder

- header

```java
HttpRequest.Builder
header​(
String
name,

String
value)
```

Adds the given name value pair to the set of headers for this request.
The given value is added to the list of values for that name.

**Implementation Note:** An implementation may choose to restrict some header names
or values, as the HTTP Client may determine their value itself.
For example, "Content-Length", which will be determined by
the request Publisher. In such a case, an implementation of

HttpRequest.Builder

may choose to throw an

IllegalArgumentException

if such a header is passed
to the builder.
**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the header name or value is not
valid, see

RFC 7230 section-3.2

, or the header name or value is restricted
by the implementation.

- headers

```java
HttpRequest.Builder
headers​(
String
... headers)
```

Adds the given name value pairs to the set of headers for this
request. The supplied

String

instances must alternate as
header names and header values.
To add several values to the same name then the same name must
be supplied with each new value.

**Parameters:** headers

- the list of name value pairs
**Returns:** this builder
**Throws:** IllegalArgumentException

- if there are an odd number of
parameters, or if a header name or value is not valid, see

RFC 7230 section-3.2

, or a header name or value is

restricted

by the
implementation.

- timeout

```java
HttpRequest.Builder
timeout​(
Duration
duration)
```

Sets a timeout for this request. If the response is not received
within the specified timeout then an

HttpTimeoutException

is
thrown from

HttpClient::send

or

HttpClient::sendAsync

completes exceptionally with an

HttpTimeoutException

. The effect
of not setting a timeout is the same as setting an infinite Duration, ie.
block forever.

**Parameters:** duration

- the timeout duration
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the duration is non-positive

- setHeader

```java
HttpRequest.Builder
setHeader​(
String
name,

String
value)
```

Sets the given name value pair to the set of headers for this
request. This overwrites any previously set values for name.

**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the header name or value is not valid,
see

RFC 7230 section-3.2

, or the header name or value is

restricted

by the
implementation.

- GET

```java
HttpRequest.Builder
GET()
```

Sets the request method of this builder to GET.
This is the default.

**Returns:** this builder

- POST

```java
HttpRequest.Builder
POST​(
HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder

- PUT

```java
HttpRequest.Builder
PUT​(
HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder

- DELETE

```java
HttpRequest.Builder
DELETE()
```

Sets the request method of this builder to DELETE.

**Returns:** this builder

- method

```java
HttpRequest.Builder
method​(
String
method,

HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method and request body of this builder to the
given values.

**API Note:** The

noBody

request
body publisher can be used where no request body is required or
appropriate. Whether a method is restricted, or not, is
implementation specific. For example, some implementations may choose
to restrict the

CONNECT

method.
**Parameters:** method

- the method to use
**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the method name is not
valid, see

RFC 7230 section-3.1.1

, or the method is restricted by the
implementation.

- build

```java
HttpRequest
build()
```

Builds and returns an

HttpRequest

.

**Returns:** a new

HttpRequest
**Throws:** IllegalStateException

- if a URI has not been set

- copy

```java
HttpRequest.Builder
copy()
```

Returns an exact duplicate copy of this

Builder

based on
current state. The new builder can then be modified independently of
this builder.

**Returns:** an exact copy of this builder

Method Detail

- uri

```java
HttpRequest.Builder
uri​(
URI
uri)
```

Sets this

HttpRequest

's request

URI

.

**Parameters:** uri

- the request URI
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the

URI

scheme is not
supported

- expectContinue

```java
HttpRequest.Builder
expectContinue​(boolean enable)
```

Requests the server to acknowledge the request before sending the
body. This is disabled by default. If enabled, the server is
requested to send an error response or a

100 Continue

response before the client sends the request body. This means the
request publisher for the request will not be invoked until this
interim response is received.

**Parameters:** enable

-

true

if Expect continue to be sent
**Returns:** this builder

- version

```java
HttpRequest.Builder
version​(
HttpClient.Version
version)
```

Sets the preferred

HttpClient.Version

for this request.

The corresponding

HttpResponse

should be checked for the
version that was actually used. If the version is not set in a
request, then the version requested will be that of the sending

HttpClient

.

**Parameters:** version

- the HTTP protocol version requested
**Returns:** this builder

- header

```java
HttpRequest.Builder
header​(
String
name,

String
value)
```

Adds the given name value pair to the set of headers for this request.
The given value is added to the list of values for that name.

**Implementation Note:** An implementation may choose to restrict some header names
or values, as the HTTP Client may determine their value itself.
For example, "Content-Length", which will be determined by
the request Publisher. In such a case, an implementation of

HttpRequest.Builder

may choose to throw an

IllegalArgumentException

if such a header is passed
to the builder.
**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the header name or value is not
valid, see

RFC 7230 section-3.2

, or the header name or value is restricted
by the implementation.

- headers

```java
HttpRequest.Builder
headers​(
String
... headers)
```

Adds the given name value pairs to the set of headers for this
request. The supplied

String

instances must alternate as
header names and header values.
To add several values to the same name then the same name must
be supplied with each new value.

**Parameters:** headers

- the list of name value pairs
**Returns:** this builder
**Throws:** IllegalArgumentException

- if there are an odd number of
parameters, or if a header name or value is not valid, see

RFC 7230 section-3.2

, or a header name or value is

restricted

by the
implementation.

- timeout

```java
HttpRequest.Builder
timeout​(
Duration
duration)
```

Sets a timeout for this request. If the response is not received
within the specified timeout then an

HttpTimeoutException

is
thrown from

HttpClient::send

or

HttpClient::sendAsync

completes exceptionally with an

HttpTimeoutException

. The effect
of not setting a timeout is the same as setting an infinite Duration, ie.
block forever.

**Parameters:** duration

- the timeout duration
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the duration is non-positive

- setHeader

```java
HttpRequest.Builder
setHeader​(
String
name,

String
value)
```

Sets the given name value pair to the set of headers for this
request. This overwrites any previously set values for name.

**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the header name or value is not valid,
see

RFC 7230 section-3.2

, or the header name or value is

restricted

by the
implementation.

- GET

```java
HttpRequest.Builder
GET()
```

Sets the request method of this builder to GET.
This is the default.

**Returns:** this builder

- POST

```java
HttpRequest.Builder
POST​(
HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder

- PUT

```java
HttpRequest.Builder
PUT​(
HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder

- DELETE

```java
HttpRequest.Builder
DELETE()
```

Sets the request method of this builder to DELETE.

**Returns:** this builder

- method

```java
HttpRequest.Builder
method​(
String
method,

HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method and request body of this builder to the
given values.

**API Note:** The

noBody

request
body publisher can be used where no request body is required or
appropriate. Whether a method is restricted, or not, is
implementation specific. For example, some implementations may choose
to restrict the

CONNECT

method.
**Parameters:** method

- the method to use
**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the method name is not
valid, see

RFC 7230 section-3.1.1

, or the method is restricted by the
implementation.

- build

```java
HttpRequest
build()
```

Builds and returns an

HttpRequest

.

**Returns:** a new

HttpRequest
**Throws:** IllegalStateException

- if a URI has not been set

- copy

```java
HttpRequest.Builder
copy()
```

Returns an exact duplicate copy of this

Builder

based on
current state. The new builder can then be modified independently of
this builder.

**Returns:** an exact copy of this builder

---

#### Method Detail

uri

```java
HttpRequest.Builder
uri​(
URI
uri)
```

Sets this

HttpRequest

's request

URI

.

**Parameters:** uri

- the request URI
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the

URI

scheme is not
supported

---

#### uri

HttpRequest.Builder

uri​(

URI

uri)

Sets this

HttpRequest

's request

URI

.

expectContinue

```java
HttpRequest.Builder
expectContinue​(boolean enable)
```

Requests the server to acknowledge the request before sending the
body. This is disabled by default. If enabled, the server is
requested to send an error response or a

100 Continue

response before the client sends the request body. This means the
request publisher for the request will not be invoked until this
interim response is received.

**Parameters:** enable

-

true

if Expect continue to be sent
**Returns:** this builder

---

#### expectContinue

HttpRequest.Builder

expectContinue​(boolean enable)

Requests the server to acknowledge the request before sending the
body. This is disabled by default. If enabled, the server is
requested to send an error response or a

100 Continue

response before the client sends the request body. This means the
request publisher for the request will not be invoked until this
interim response is received.

version

```java
HttpRequest.Builder
version​(
HttpClient.Version
version)
```

Sets the preferred

HttpClient.Version

for this request.

The corresponding

HttpResponse

should be checked for the
version that was actually used. If the version is not set in a
request, then the version requested will be that of the sending

HttpClient

.

**Parameters:** version

- the HTTP protocol version requested
**Returns:** this builder

---

#### version

HttpRequest.Builder

version​(

HttpClient.Version

version)

Sets the preferred

HttpClient.Version

for this request.

The corresponding

HttpResponse

should be checked for the
version that was actually used. If the version is not set in a
request, then the version requested will be that of the sending

HttpClient

.

The corresponding

HttpResponse

should be checked for the
version that was actually used. If the version is not set in a
request, then the version requested will be that of the sending

HttpClient

.

header

```java
HttpRequest.Builder
header​(
String
name,

String
value)
```

Adds the given name value pair to the set of headers for this request.
The given value is added to the list of values for that name.

**Implementation Note:** An implementation may choose to restrict some header names
or values, as the HTTP Client may determine their value itself.
For example, "Content-Length", which will be determined by
the request Publisher. In such a case, an implementation of

HttpRequest.Builder

may choose to throw an

IllegalArgumentException

if such a header is passed
to the builder.
**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the header name or value is not
valid, see

RFC 7230 section-3.2

, or the header name or value is restricted
by the implementation.

---

#### header

HttpRequest.Builder

header​(

String

name,

String

value)

Adds the given name value pair to the set of headers for this request.
The given value is added to the list of values for that name.

headers

```java
HttpRequest.Builder
headers​(
String
... headers)
```

Adds the given name value pairs to the set of headers for this
request. The supplied

String

instances must alternate as
header names and header values.
To add several values to the same name then the same name must
be supplied with each new value.

**Parameters:** headers

- the list of name value pairs
**Returns:** this builder
**Throws:** IllegalArgumentException

- if there are an odd number of
parameters, or if a header name or value is not valid, see

RFC 7230 section-3.2

, or a header name or value is

restricted

by the
implementation.

---

#### headers

HttpRequest.Builder

headers​(

String

... headers)

Adds the given name value pairs to the set of headers for this
request. The supplied

String

instances must alternate as
header names and header values.
To add several values to the same name then the same name must
be supplied with each new value.

timeout

```java
HttpRequest.Builder
timeout​(
Duration
duration)
```

Sets a timeout for this request. If the response is not received
within the specified timeout then an

HttpTimeoutException

is
thrown from

HttpClient::send

or

HttpClient::sendAsync

completes exceptionally with an

HttpTimeoutException

. The effect
of not setting a timeout is the same as setting an infinite Duration, ie.
block forever.

**Parameters:** duration

- the timeout duration
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the duration is non-positive

---

#### timeout

HttpRequest.Builder

timeout​(

Duration

duration)

Sets a timeout for this request. If the response is not received
within the specified timeout then an

HttpTimeoutException

is
thrown from

HttpClient::send

or

HttpClient::sendAsync

completes exceptionally with an

HttpTimeoutException

. The effect
of not setting a timeout is the same as setting an infinite Duration, ie.
block forever.

setHeader

```java
HttpRequest.Builder
setHeader​(
String
name,

String
value)
```

Sets the given name value pair to the set of headers for this
request. This overwrites any previously set values for name.

**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the header name or value is not valid,
see

RFC 7230 section-3.2

, or the header name or value is

restricted

by the
implementation.

---

#### setHeader

HttpRequest.Builder

setHeader​(

String

name,

String

value)

Sets the given name value pair to the set of headers for this
request. This overwrites any previously set values for name.

GET

```java
HttpRequest.Builder
GET()
```

Sets the request method of this builder to GET.
This is the default.

**Returns:** this builder

---

#### GET

HttpRequest.Builder

GET()

Sets the request method of this builder to GET.
This is the default.

POST

```java
HttpRequest.Builder
POST​(
HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder

---

#### POST

HttpRequest.Builder

POST​(

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method of this builder to POST and sets its
request body publisher to the given value.

PUT

```java
HttpRequest.Builder
PUT​(
HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder

---

#### PUT

HttpRequest.Builder

PUT​(

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method of this builder to PUT and sets its
request body publisher to the given value.

DELETE

```java
HttpRequest.Builder
DELETE()
```

Sets the request method of this builder to DELETE.

**Returns:** this builder

---

#### DELETE

HttpRequest.Builder

DELETE()

Sets the request method of this builder to DELETE.

method

```java
HttpRequest.Builder
method​(
String
method,

HttpRequest.BodyPublisher
bodyPublisher)
```

Sets the request method and request body of this builder to the
given values.

**API Note:** The

noBody

request
body publisher can be used where no request body is required or
appropriate. Whether a method is restricted, or not, is
implementation specific. For example, some implementations may choose
to restrict the

CONNECT

method.
**Parameters:** method

- the method to use
**Parameters:** bodyPublisher

- the body publisher
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the method name is not
valid, see

RFC 7230 section-3.1.1

, or the method is restricted by the
implementation.

---

#### method

HttpRequest.Builder

method​(

String

method,

HttpRequest.BodyPublisher

bodyPublisher)

Sets the request method and request body of this builder to the
given values.

build

```java
HttpRequest
build()
```

Builds and returns an

HttpRequest

.

**Returns:** a new

HttpRequest
**Throws:** IllegalStateException

- if a URI has not been set

---

#### build

HttpRequest

build()

Builds and returns an

HttpRequest

.

copy

```java
HttpRequest.Builder
copy()
```

Returns an exact duplicate copy of this

Builder

based on
current state. The new builder can then be modified independently of
this builder.

**Returns:** an exact copy of this builder

---

#### copy

HttpRequest.Builder

copy()

Returns an exact duplicate copy of this

Builder

based on
current state. The new builder can then be modified independently of
this builder.

---

