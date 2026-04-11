# Class HttpClient

**Source:** `java.net.http\java\net\http\HttpClient.html`

### Class Description

```java
public abstract class
HttpClient

extends
Object
```

An HTTP Client.

An

HttpClient

can be used to send

requests

and retrieve their

responses

. An

HttpClient

is created through a

builder

. The
builder can be used to configure per-client state, like: the preferred
protocol version ( HTTP/1.1 or HTTP/2 ), whether to follow redirects, a
proxy, an authenticator, etc. Once built, an

HttpClient

is immutable,
and can be used to send multiple requests.

An

HttpClient

provides configuration information, and resource
sharing, for all requests sent through it.

A

BodyHandler

must be supplied for each

HttpRequest

sent. The

BodyHandler

determines how to handle the
response body, if any. Once an

HttpResponse

is received, the
headers, response code, and body (typically) are available. Whether the
response body bytes have been read or not depends on the type,

T

, of
the response body.

Requests can be sent either synchronously or asynchronously:

- send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.
- sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

**Implementation Note:** If an explicit

executor

has not been set for an

HttpClient

, and a security manager
has been installed, then the default executor will execute asynchronous and
dependent tasks in a context that is granted no permissions. Custom

request body publishers

,

response body handlers

,

response body subscribers

, and

WebSocket Listeners

, if executing operations that require
privileges, should do so within an appropriate

privileged context

.
**Since:** 11

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpClient()

Creates an HttpClient.

---

### Method Details

#### public static
HttpClient
newHttpClient()

Returns a new

HttpClient

with default settings.

Equivalent to

newBuilder().build()

.

The default settings include: the "GET" request method, a preference
of

HTTP/2

, a redirection policy of

NEVER

, the

default proxy selector

, and the

default SSL context

.

**Returns:**
- a new HttpClient

**Implementation Note:**
- The system-wide default values are retrieved at the time the

HttpClient

instance is constructed. Changing the system-wide
values after an

HttpClient

instance has been built, for
instance, by calling

ProxySelector.setDefault(ProxySelector)

or

SSLContext.setDefault(SSLContext)

, has no effect on already
built instances.

---

#### public static
HttpClient.Builder
newBuilder()

Creates a new

HttpClient

builder.

**Returns:**
- an

HttpClient.Builder

---

#### public abstract
Optional
<
CookieHandler
> cookieHandler()

Returns an

Optional

containing this client's

CookieHandler

. If no

CookieHandler

was set in this client's
builder, then the

Optional

is empty.

**Returns:**
- an

Optional

containing this client's

CookieHandler

---

#### public abstract
Optional
<
Duration
> connectTimeout()

Returns an

Optional

containing the

connect timeout duration

for this client. If the

connect timeout duration

was not set in the client's builder, then the

Optional

is empty.

**Returns:**
- an

Optional

containing this client's connect timeout
duration

---

#### public abstract
HttpClient.Redirect
followRedirects()

Returns the follow redirects policy for this client. The default value
for client's built by builders that do not specify a redirect policy is

NEVER

.

**Returns:**
- this client's follow redirects setting

---

#### public abstract
Optional
<
ProxySelector
> proxy()

Returns an

Optional

containing the

ProxySelector

supplied to this client. If no proxy selector was set in this client's
builder, then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have a non-exposed

default proxy selector

that is
used for sending HTTP requests.

**Returns:**
- an

Optional

containing the proxy selector supplied
to this client.

---

#### public abstract
SSLContext
sslContext()

Returns this client's

SSLContext

.

If no

SSLContext

was set in this client's builder, then the

default context

is returned.

**Returns:**
- this client's SSLContext

---

#### public abstract
SSLParameters
sslParameters()

Returns a copy of this client's

SSLParameters

.

If no

SSLParameters

were set in the client's builder, then an
implementation specific default set of parameters, that the client will
use, is returned.

**Returns:**
- this client's

SSLParameters

---

#### public abstract
Optional
<
Authenticator
> authenticator()

Returns an

Optional

containing the

Authenticator

set on
this client. If no

Authenticator

was set in the client's builder,
then the

Optional

is empty.

**Returns:**
- an

Optional

containing this client's

Authenticator

---

#### public abstract
HttpClient.Version
version()

Returns the preferred HTTP protocol version for this client. The default
value is

HttpClient.Version.HTTP_2

**Returns:**
- the HTTP protocol version requested

**Implementation Note:**
- Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the
implementation does not support this mode, then HTTP/1.1 may be used

---

#### public abstract
Optional
<
Executor
> executor()

Returns an

Optional

containing this client's

Executor

. If no

Executor

was set in the client's builder,
then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have an non-exposed

default executor

that is used for
executing asynchronous and dependent tasks.

**Returns:**
- an

Optional

containing this client's

Executor

---

#### public abstract <T>
HttpResponse
<T> send​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)
throws
IOException
,

InterruptedException

Sends the given request using this client, blocking if necessary to get
the response. The returned

HttpResponse

<T>

contains the
response status, headers, and body ( as handled by given response body
handler ).

**Parameters:**
- request

- the request
- responseBodyHandler

- the response body handler

**Returns:**
- the response

**Throws:**
- IOException

- if an I/O error occurs when sending or receiving
- InterruptedException

- if the operation is interrupted
- IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

**Type Parameters:**
- T

- the response body type

---

#### public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)

Sends the given request asynchronously using this client with the given
response body handler.

Equivalent to:

sendAsync(request, responseBodyHandler, null)

.

**Parameters:**
- request

- the request
- responseBodyHandler

- the response body handler

**Returns:**
- a

CompletableFuture<HttpResponse<T>>

**Throws:**
- IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

**Type Parameters:**
- T

- the response body type

---

#### public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler,

HttpResponse.PushPromiseHandler
<T> pushPromiseHandler)

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

The returned completable future, if completed successfully, completes
with an

HttpResponse

<T>

that contains the response status,
headers, and body ( as handled by given response body handler ).

Push promises

received, if any, are
handled by the given

pushPromiseHandler

. A

null

valued

pushPromiseHandler

rejects any push promises.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

**Parameters:**
- request

- the request
- responseBodyHandler

- the response body handler
- pushPromiseHandler

- push promise handler, may be null

**Returns:**
- a

CompletableFuture<HttpResponse<T>>

**Throws:**
- IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

**Type Parameters:**
- T

- the response body type

---

#### public
WebSocket.Builder
newWebSocketBuilder()

Creates a new

WebSocket

builder (optional operation).

Example

```java
HttpClient client = HttpClient.newHttpClient();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Finer control over the WebSocket Opening Handshake can be achieved
by using a custom

HttpClient

.

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

**Returns:**
- a

WebSocket.Builder

**Throws:**
- UnsupportedOperationException

- if this

HttpClient

does not provide WebSocket support

**Implementation Requirements:**
- The default implementation of this method throws

UnsupportedOperationException

. Clients obtained through

newHttpClient()

or

newBuilder()

return a

WebSocket

builder.

**Implementation Note:**
- Both builder and

WebSocket

s created with it operate in
a non-blocking fashion. That is, their methods do not block before
returning a

CompletableFuture

. Asynchronous tasks are executed in
this

HttpClient

's executor.

When a

CompletionStage

returned from

Listener.onClose

completes,
the

WebSocket

will send a Close message that has the same code
the received message has and an empty reason.

---

### Additional Sections

#### Class HttpClient

java.lang.Object

- java.net.http.HttpClient

java.net.http.HttpClient

```java
public abstract class
HttpClient

extends
Object
```

An HTTP Client.

An

HttpClient

can be used to send

requests

and retrieve their

responses

. An

HttpClient

is created through a

builder

. The
builder can be used to configure per-client state, like: the preferred
protocol version ( HTTP/1.1 or HTTP/2 ), whether to follow redirects, a
proxy, an authenticator, etc. Once built, an

HttpClient

is immutable,
and can be used to send multiple requests.

An

HttpClient

provides configuration information, and resource
sharing, for all requests sent through it.

A

BodyHandler

must be supplied for each

HttpRequest

sent. The

BodyHandler

determines how to handle the
response body, if any. Once an

HttpResponse

is received, the
headers, response code, and body (typically) are available. Whether the
response body bytes have been read or not depends on the type,

T

, of
the response body.

Requests can be sent either synchronously or asynchronously:

- send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.
- sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

**Implementation Note:** If an explicit

executor

has not been set for an

HttpClient

, and a security manager
has been installed, then the default executor will execute asynchronous and
dependent tasks in a context that is granted no permissions. Custom

request body publishers

,

response body handlers

,

response body subscribers

, and

WebSocket Listeners

, if executing operations that require
privileges, should do so within an appropriate

privileged context

.
**Since:** 11

public abstract class

HttpClient

extends

Object

An HTTP Client.

An

HttpClient

can be used to send

requests

and retrieve their

responses

. An

HttpClient

is created through a

builder

. The
builder can be used to configure per-client state, like: the preferred
protocol version ( HTTP/1.1 or HTTP/2 ), whether to follow redirects, a
proxy, an authenticator, etc. Once built, an

HttpClient

is immutable,
and can be used to send multiple requests.

An

HttpClient

provides configuration information, and resource
sharing, for all requests sent through it.

A

BodyHandler

must be supplied for each

HttpRequest

sent. The

BodyHandler

determines how to handle the
response body, if any. Once an

HttpResponse

is received, the
headers, response code, and body (typically) are available. Whether the
response body bytes have been read or not depends on the type,

T

, of
the response body.

Requests can be sent either synchronously or asynchronously:

- send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.
- sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

An

HttpClient

can be used to send

requests

and retrieve their

responses

. An

HttpClient

is created through a

builder

. The
builder can be used to configure per-client state, like: the preferred
protocol version ( HTTP/1.1 or HTTP/2 ), whether to follow redirects, a
proxy, an authenticator, etc. Once built, an

HttpClient

is immutable,
and can be used to send multiple requests.

An

HttpClient

provides configuration information, and resource
sharing, for all requests sent through it.

A

BodyHandler

must be supplied for each

HttpRequest

sent. The

BodyHandler

determines how to handle the
response body, if any. Once an

HttpResponse

is received, the
headers, response code, and body (typically) are available. Whether the
response body bytes have been read or not depends on the type,

T

, of
the response body.

Requests can be sent either synchronously or asynchronously:

- send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.
- sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

An

HttpClient

provides configuration information, and resource
sharing, for all requests sent through it.

A

BodyHandler

must be supplied for each

HttpRequest

sent. The

BodyHandler

determines how to handle the
response body, if any. Once an

HttpResponse

is received, the
headers, response code, and body (typically) are available. Whether the
response body bytes have been read or not depends on the type,

T

, of
the response body.

Requests can be sent either synchronously or asynchronously:

- send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.
- sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

A

BodyHandler

must be supplied for each

HttpRequest

sent. The

BodyHandler

determines how to handle the
response body, if any. Once an

HttpResponse

is received, the
headers, response code, and body (typically) are available. Whether the
response body bytes have been read or not depends on the type,

T

, of
the response body.

Requests can be sent either synchronously or asynchronously:

- send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.
- sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

Requests can be sent either synchronously or asynchronously:

- send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.
- sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

send(HttpRequest, BodyHandler)

blocks
until the request has been sent and the response has been received.

sendAsync(HttpRequest, BodyHandler)

sends the
request and receives the response asynchronously. The

sendAsync

method returns immediately with a

CompletableFuture

<

HttpResponse

>. The

CompletableFuture

completes when the response becomes available. The
returned

CompletableFuture

can be combined in different ways to
declare dependencies among several asynchronous tasks.

Synchronous Example

```java
HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

HttpClient client = HttpClient.newBuilder()
.version(Version.HTTP_1_1)
.followRedirects(Redirect.NORMAL)
.connectTimeout(Duration.ofSeconds(20))
.proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
.authenticator(Authenticator.getDefault())
.build();
HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());

Asynchronous Example

```java
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);
```

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.timeout(Duration.ofMinutes(2))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();
client.sendAsync(request, BodyHandlers.ofString())
.thenApply(HttpResponse::body)
.thenAccept(System.out::println);

Security checks

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

If a security manager is present then security checks are performed by
the HTTP Client's sending methods. An appropriate

URLPermission

is
required to access the destination server, and proxy server if one has
been configured. The form of the

URLPermission

required to access a
proxy has a

method

parameter of

"CONNECT"

(for all kinds of
proxying) and a

URL

string of the form

"socket://host:port"

where host and port specify the proxy's address.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

HttpClient.Builder

A builder of

HTTP Clients

.

static class

HttpClient.Redirect

Defines the automatic redirection policy.

static class

HttpClient.Version

The HTTP protocol version.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpClient

()

Creates an HttpClient.

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

Authenticator

>

authenticator

()

Returns an

Optional

containing the

Authenticator

set on
this client.

abstract

Optional

<

Duration

>

connectTimeout

()

Returns an

Optional

containing the

connect timeout duration

for this client.

abstract

Optional

<

CookieHandler

>

cookieHandler

()

Returns an

Optional

containing this client's

CookieHandler

.

abstract

Optional

<

Executor

>

executor

()

Returns an

Optional

containing this client's

Executor

.

abstract

HttpClient.Redirect

followRedirects

()

Returns the follow redirects policy for this client.

static

HttpClient.Builder

newBuilder

()

Creates a new

HttpClient

builder.

static

HttpClient

newHttpClient

()

Returns a new

HttpClient

with default settings.

WebSocket.Builder

newWebSocketBuilder

()

Creates a new

WebSocket

builder (optional operation).

abstract

Optional

<

ProxySelector

>

proxy

()

Returns an

Optional

containing the

ProxySelector

supplied to this client.

abstract <T>

HttpResponse

<T>

send

​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler)

Sends the given request using this client, blocking if necessary to get
the response.

abstract <T>

CompletableFuture

<

HttpResponse

<T>>

sendAsync

​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler)

Sends the given request asynchronously using this client with the given
response body handler.

abstract <T>

CompletableFuture

<

HttpResponse

<T>>

sendAsync

​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler,

HttpResponse.PushPromiseHandler

<T> pushPromiseHandler)

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

abstract

SSLContext

sslContext

()

Returns this client's

SSLContext

.

abstract

SSLParameters

sslParameters

()

Returns a copy of this client's

SSLParameters

.

abstract

HttpClient.Version

version

()

Returns the preferred HTTP protocol version for this client.

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

HttpClient.Builder

A builder of

HTTP Clients

.

static class

HttpClient.Redirect

Defines the automatic redirection policy.

static class

HttpClient.Version

The HTTP protocol version.

---

#### Nested Class Summary

A builder of

HTTP Clients

.

Defines the automatic redirection policy.

The HTTP protocol version.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpClient

()

Creates an HttpClient.

---

#### Constructor Summary

Creates an HttpClient.

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

Authenticator

>

authenticator

()

Returns an

Optional

containing the

Authenticator

set on
this client.

abstract

Optional

<

Duration

>

connectTimeout

()

Returns an

Optional

containing the

connect timeout duration

for this client.

abstract

Optional

<

CookieHandler

>

cookieHandler

()

Returns an

Optional

containing this client's

CookieHandler

.

abstract

Optional

<

Executor

>

executor

()

Returns an

Optional

containing this client's

Executor

.

abstract

HttpClient.Redirect

followRedirects

()

Returns the follow redirects policy for this client.

static

HttpClient.Builder

newBuilder

()

Creates a new

HttpClient

builder.

static

HttpClient

newHttpClient

()

Returns a new

HttpClient

with default settings.

WebSocket.Builder

newWebSocketBuilder

()

Creates a new

WebSocket

builder (optional operation).

abstract

Optional

<

ProxySelector

>

proxy

()

Returns an

Optional

containing the

ProxySelector

supplied to this client.

abstract <T>

HttpResponse

<T>

send

​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler)

Sends the given request using this client, blocking if necessary to get
the response.

abstract <T>

CompletableFuture

<

HttpResponse

<T>>

sendAsync

​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler)

Sends the given request asynchronously using this client with the given
response body handler.

abstract <T>

CompletableFuture

<

HttpResponse

<T>>

sendAsync

​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler,

HttpResponse.PushPromiseHandler

<T> pushPromiseHandler)

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

abstract

SSLContext

sslContext

()

Returns this client's

SSLContext

.

abstract

SSLParameters

sslParameters

()

Returns a copy of this client's

SSLParameters

.

abstract

HttpClient.Version

version

()

Returns the preferred HTTP protocol version for this client.

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

Returns an

Optional

containing the

Authenticator

set on
this client.

Returns an

Optional

containing the

connect timeout duration

for this client.

Returns an

Optional

containing this client's

CookieHandler

.

Returns an

Optional

containing this client's

Executor

.

Returns the follow redirects policy for this client.

Creates a new

HttpClient

builder.

Returns a new

HttpClient

with default settings.

Creates a new

WebSocket

builder (optional operation).

Returns an

Optional

containing the

ProxySelector

supplied to this client.

Sends the given request using this client, blocking if necessary to get
the response.

Sends the given request asynchronously using this client with the given
response body handler.

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

Returns this client's

SSLContext

.

Returns a copy of this client's

SSLParameters

.

Returns the preferred HTTP protocol version for this client.

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

- HttpClient

```java
protected HttpClient()
```

Creates an HttpClient.

============ METHOD DETAIL ==========

- Method Detail

- newHttpClient

```java
public static
HttpClient
newHttpClient()
```

Returns a new

HttpClient

with default settings.

Equivalent to

newBuilder().build()

.

The default settings include: the "GET" request method, a preference
of

HTTP/2

, a redirection policy of

NEVER

, the

default proxy selector

, and the

default SSL context

.

**Implementation Note:** The system-wide default values are retrieved at the time the

HttpClient

instance is constructed. Changing the system-wide
values after an

HttpClient

instance has been built, for
instance, by calling

ProxySelector.setDefault(ProxySelector)

or

SSLContext.setDefault(SSLContext)

, has no effect on already
built instances.
**Returns:** a new HttpClient

- newBuilder

```java
public static
HttpClient.Builder
newBuilder()
```

Creates a new

HttpClient

builder.

**Returns:** an

HttpClient.Builder

- cookieHandler

```java
public abstract
Optional
<
CookieHandler
> cookieHandler()
```

Returns an

Optional

containing this client's

CookieHandler

. If no

CookieHandler

was set in this client's
builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this client's

CookieHandler

- connectTimeout

```java
public abstract
Optional
<
Duration
> connectTimeout()
```

Returns an

Optional

containing the

connect timeout duration

for this client. If the

connect timeout duration

was not set in the client's builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this client's connect timeout
duration

- followRedirects

```java
public abstract
HttpClient.Redirect
followRedirects()
```

Returns the follow redirects policy for this client. The default value
for client's built by builders that do not specify a redirect policy is

NEVER

.

**Returns:** this client's follow redirects setting

- proxy

```java
public abstract
Optional
<
ProxySelector
> proxy()
```

Returns an

Optional

containing the

ProxySelector

supplied to this client. If no proxy selector was set in this client's
builder, then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have a non-exposed

default proxy selector

that is
used for sending HTTP requests.

**Returns:** an

Optional

containing the proxy selector supplied
to this client.

- sslContext

```java
public abstract
SSLContext
sslContext()
```

Returns this client's

SSLContext

.

If no

SSLContext

was set in this client's builder, then the

default context

is returned.

**Returns:** this client's SSLContext

- sslParameters

```java
public abstract
SSLParameters
sslParameters()
```

Returns a copy of this client's

SSLParameters

.

If no

SSLParameters

were set in the client's builder, then an
implementation specific default set of parameters, that the client will
use, is returned.

**Returns:** this client's

SSLParameters

- authenticator

```java
public abstract
Optional
<
Authenticator
> authenticator()
```

Returns an

Optional

containing the

Authenticator

set on
this client. If no

Authenticator

was set in the client's builder,
then the

Optional

is empty.

**Returns:** an

Optional

containing this client's

Authenticator

- version

```java
public abstract
HttpClient.Version
version()
```

Returns the preferred HTTP protocol version for this client. The default
value is

HttpClient.Version.HTTP_2

**Implementation Note:** Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the
implementation does not support this mode, then HTTP/1.1 may be used
**Returns:** the HTTP protocol version requested

- executor

```java
public abstract
Optional
<
Executor
> executor()
```

Returns an

Optional

containing this client's

Executor

. If no

Executor

was set in the client's builder,
then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have an non-exposed

default executor

that is used for
executing asynchronous and dependent tasks.

**Returns:** an

Optional

containing this client's

Executor

- send

```java
public abstract <T>
HttpResponse
<T> send​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)
throws
IOException
,

InterruptedException
```

Sends the given request using this client, blocking if necessary to get
the response. The returned

HttpResponse

<T>

contains the
response status, headers, and body ( as handled by given response body
handler ).

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Returns:** the response
**Throws:** IOException

- if an I/O error occurs when sending or receiving
**Throws:** InterruptedException

- if the operation is interrupted
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.
**Throws:** SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

- sendAsync

```java
public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)
```

Sends the given request asynchronously using this client with the given
response body handler.

Equivalent to:

sendAsync(request, responseBodyHandler, null)

.

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Returns:** a

CompletableFuture<HttpResponse<T>>
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

- sendAsync

```java
public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler,

HttpResponse.PushPromiseHandler
<T> pushPromiseHandler)
```

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

The returned completable future, if completed successfully, completes
with an

HttpResponse

<T>

that contains the response status,
headers, and body ( as handled by given response body handler ).

Push promises

received, if any, are
handled by the given

pushPromiseHandler

. A

null

valued

pushPromiseHandler

rejects any push promises.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Parameters:** pushPromiseHandler

- push promise handler, may be null
**Returns:** a

CompletableFuture<HttpResponse<T>>
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

- newWebSocketBuilder

```java
public
WebSocket.Builder
newWebSocketBuilder()
```

Creates a new

WebSocket

builder (optional operation).

Example

```java
HttpClient client = HttpClient.newHttpClient();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Finer control over the WebSocket Opening Handshake can be achieved
by using a custom

HttpClient

.

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

**Implementation Requirements:** The default implementation of this method throws

UnsupportedOperationException

. Clients obtained through

newHttpClient()

or

newBuilder()

return a

WebSocket

builder.
**Implementation Note:** Both builder and

WebSocket

s created with it operate in
a non-blocking fashion. That is, their methods do not block before
returning a

CompletableFuture

. Asynchronous tasks are executed in
this

HttpClient

's executor.

When a

CompletionStage

returned from

Listener.onClose

completes,
the

WebSocket

will send a Close message that has the same code
the received message has and an empty reason.
**Returns:** a

WebSocket.Builder
**Throws:** UnsupportedOperationException

- if this

HttpClient

does not provide WebSocket support

Constructor Detail

- HttpClient

```java
protected HttpClient()
```

Creates an HttpClient.

---

#### Constructor Detail

HttpClient

```java
protected HttpClient()
```

Creates an HttpClient.

---

#### HttpClient

protected HttpClient()

Creates an HttpClient.

Method Detail

- newHttpClient

```java
public static
HttpClient
newHttpClient()
```

Returns a new

HttpClient

with default settings.

Equivalent to

newBuilder().build()

.

The default settings include: the "GET" request method, a preference
of

HTTP/2

, a redirection policy of

NEVER

, the

default proxy selector

, and the

default SSL context

.

**Implementation Note:** The system-wide default values are retrieved at the time the

HttpClient

instance is constructed. Changing the system-wide
values after an

HttpClient

instance has been built, for
instance, by calling

ProxySelector.setDefault(ProxySelector)

or

SSLContext.setDefault(SSLContext)

, has no effect on already
built instances.
**Returns:** a new HttpClient

- newBuilder

```java
public static
HttpClient.Builder
newBuilder()
```

Creates a new

HttpClient

builder.

**Returns:** an

HttpClient.Builder

- cookieHandler

```java
public abstract
Optional
<
CookieHandler
> cookieHandler()
```

Returns an

Optional

containing this client's

CookieHandler

. If no

CookieHandler

was set in this client's
builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this client's

CookieHandler

- connectTimeout

```java
public abstract
Optional
<
Duration
> connectTimeout()
```

Returns an

Optional

containing the

connect timeout duration

for this client. If the

connect timeout duration

was not set in the client's builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this client's connect timeout
duration

- followRedirects

```java
public abstract
HttpClient.Redirect
followRedirects()
```

Returns the follow redirects policy for this client. The default value
for client's built by builders that do not specify a redirect policy is

NEVER

.

**Returns:** this client's follow redirects setting

- proxy

```java
public abstract
Optional
<
ProxySelector
> proxy()
```

Returns an

Optional

containing the

ProxySelector

supplied to this client. If no proxy selector was set in this client's
builder, then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have a non-exposed

default proxy selector

that is
used for sending HTTP requests.

**Returns:** an

Optional

containing the proxy selector supplied
to this client.

- sslContext

```java
public abstract
SSLContext
sslContext()
```

Returns this client's

SSLContext

.

If no

SSLContext

was set in this client's builder, then the

default context

is returned.

**Returns:** this client's SSLContext

- sslParameters

```java
public abstract
SSLParameters
sslParameters()
```

Returns a copy of this client's

SSLParameters

.

If no

SSLParameters

were set in the client's builder, then an
implementation specific default set of parameters, that the client will
use, is returned.

**Returns:** this client's

SSLParameters

- authenticator

```java
public abstract
Optional
<
Authenticator
> authenticator()
```

Returns an

Optional

containing the

Authenticator

set on
this client. If no

Authenticator

was set in the client's builder,
then the

Optional

is empty.

**Returns:** an

Optional

containing this client's

Authenticator

- version

```java
public abstract
HttpClient.Version
version()
```

Returns the preferred HTTP protocol version for this client. The default
value is

HttpClient.Version.HTTP_2

**Implementation Note:** Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the
implementation does not support this mode, then HTTP/1.1 may be used
**Returns:** the HTTP protocol version requested

- executor

```java
public abstract
Optional
<
Executor
> executor()
```

Returns an

Optional

containing this client's

Executor

. If no

Executor

was set in the client's builder,
then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have an non-exposed

default executor

that is used for
executing asynchronous and dependent tasks.

**Returns:** an

Optional

containing this client's

Executor

- send

```java
public abstract <T>
HttpResponse
<T> send​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)
throws
IOException
,

InterruptedException
```

Sends the given request using this client, blocking if necessary to get
the response. The returned

HttpResponse

<T>

contains the
response status, headers, and body ( as handled by given response body
handler ).

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Returns:** the response
**Throws:** IOException

- if an I/O error occurs when sending or receiving
**Throws:** InterruptedException

- if the operation is interrupted
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.
**Throws:** SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

- sendAsync

```java
public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)
```

Sends the given request asynchronously using this client with the given
response body handler.

Equivalent to:

sendAsync(request, responseBodyHandler, null)

.

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Returns:** a

CompletableFuture<HttpResponse<T>>
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

- sendAsync

```java
public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler,

HttpResponse.PushPromiseHandler
<T> pushPromiseHandler)
```

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

The returned completable future, if completed successfully, completes
with an

HttpResponse

<T>

that contains the response status,
headers, and body ( as handled by given response body handler ).

Push promises

received, if any, are
handled by the given

pushPromiseHandler

. A

null

valued

pushPromiseHandler

rejects any push promises.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Parameters:** pushPromiseHandler

- push promise handler, may be null
**Returns:** a

CompletableFuture<HttpResponse<T>>
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

- newWebSocketBuilder

```java
public
WebSocket.Builder
newWebSocketBuilder()
```

Creates a new

WebSocket

builder (optional operation).

Example

```java
HttpClient client = HttpClient.newHttpClient();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Finer control over the WebSocket Opening Handshake can be achieved
by using a custom

HttpClient

.

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

**Implementation Requirements:** The default implementation of this method throws

UnsupportedOperationException

. Clients obtained through

newHttpClient()

or

newBuilder()

return a

WebSocket

builder.
**Implementation Note:** Both builder and

WebSocket

s created with it operate in
a non-blocking fashion. That is, their methods do not block before
returning a

CompletableFuture

. Asynchronous tasks are executed in
this

HttpClient

's executor.

When a

CompletionStage

returned from

Listener.onClose

completes,
the

WebSocket

will send a Close message that has the same code
the received message has and an empty reason.
**Returns:** a

WebSocket.Builder
**Throws:** UnsupportedOperationException

- if this

HttpClient

does not provide WebSocket support

---

#### Method Detail

newHttpClient

```java
public static
HttpClient
newHttpClient()
```

Returns a new

HttpClient

with default settings.

Equivalent to

newBuilder().build()

.

The default settings include: the "GET" request method, a preference
of

HTTP/2

, a redirection policy of

NEVER

, the

default proxy selector

, and the

default SSL context

.

**Implementation Note:** The system-wide default values are retrieved at the time the

HttpClient

instance is constructed. Changing the system-wide
values after an

HttpClient

instance has been built, for
instance, by calling

ProxySelector.setDefault(ProxySelector)

or

SSLContext.setDefault(SSLContext)

, has no effect on already
built instances.
**Returns:** a new HttpClient

---

#### newHttpClient

public static

HttpClient

newHttpClient()

Returns a new

HttpClient

with default settings.

Equivalent to

newBuilder().build()

.

The default settings include: the "GET" request method, a preference
of

HTTP/2

, a redirection policy of

NEVER

, the

default proxy selector

, and the

default SSL context

.

Equivalent to

newBuilder().build()

.

The default settings include: the "GET" request method, a preference
of

HTTP/2

, a redirection policy of

NEVER

, the

default proxy selector

, and the

default SSL context

.

The default settings include: the "GET" request method, a preference
of

HTTP/2

, a redirection policy of

NEVER

, the

default proxy selector

, and the

default SSL context

.

newBuilder

```java
public static
HttpClient.Builder
newBuilder()
```

Creates a new

HttpClient

builder.

**Returns:** an

HttpClient.Builder

---

#### newBuilder

public static

HttpClient.Builder

newBuilder()

Creates a new

HttpClient

builder.

cookieHandler

```java
public abstract
Optional
<
CookieHandler
> cookieHandler()
```

Returns an

Optional

containing this client's

CookieHandler

. If no

CookieHandler

was set in this client's
builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this client's

CookieHandler

---

#### cookieHandler

public abstract

Optional

<

CookieHandler

> cookieHandler()

Returns an

Optional

containing this client's

CookieHandler

. If no

CookieHandler

was set in this client's
builder, then the

Optional

is empty.

connectTimeout

```java
public abstract
Optional
<
Duration
> connectTimeout()
```

Returns an

Optional

containing the

connect timeout duration

for this client. If the

connect timeout duration

was not set in the client's builder, then the

Optional

is empty.

**Returns:** an

Optional

containing this client's connect timeout
duration

---

#### connectTimeout

public abstract

Optional

<

Duration

> connectTimeout()

Returns an

Optional

containing the

connect timeout duration

for this client. If the

connect timeout duration

was not set in the client's builder, then the

Optional

is empty.

followRedirects

```java
public abstract
HttpClient.Redirect
followRedirects()
```

Returns the follow redirects policy for this client. The default value
for client's built by builders that do not specify a redirect policy is

NEVER

.

**Returns:** this client's follow redirects setting

---

#### followRedirects

public abstract

HttpClient.Redirect

followRedirects()

Returns the follow redirects policy for this client. The default value
for client's built by builders that do not specify a redirect policy is

NEVER

.

proxy

```java
public abstract
Optional
<
ProxySelector
> proxy()
```

Returns an

Optional

containing the

ProxySelector

supplied to this client. If no proxy selector was set in this client's
builder, then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have a non-exposed

default proxy selector

that is
used for sending HTTP requests.

**Returns:** an

Optional

containing the proxy selector supplied
to this client.

---

#### proxy

public abstract

Optional

<

ProxySelector

> proxy()

Returns an

Optional

containing the

ProxySelector

supplied to this client. If no proxy selector was set in this client's
builder, then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have a non-exposed

default proxy selector

that is
used for sending HTTP requests.

Even though this method may return an empty optional, the

HttpClient

may still have a non-exposed

default proxy selector

that is
used for sending HTTP requests.

sslContext

```java
public abstract
SSLContext
sslContext()
```

Returns this client's

SSLContext

.

If no

SSLContext

was set in this client's builder, then the

default context

is returned.

**Returns:** this client's SSLContext

---

#### sslContext

public abstract

SSLContext

sslContext()

Returns this client's

SSLContext

.

If no

SSLContext

was set in this client's builder, then the

default context

is returned.

If no

SSLContext

was set in this client's builder, then the

default context

is returned.

sslParameters

```java
public abstract
SSLParameters
sslParameters()
```

Returns a copy of this client's

SSLParameters

.

If no

SSLParameters

were set in the client's builder, then an
implementation specific default set of parameters, that the client will
use, is returned.

**Returns:** this client's

SSLParameters

---

#### sslParameters

public abstract

SSLParameters

sslParameters()

Returns a copy of this client's

SSLParameters

.

If no

SSLParameters

were set in the client's builder, then an
implementation specific default set of parameters, that the client will
use, is returned.

If no

SSLParameters

were set in the client's builder, then an
implementation specific default set of parameters, that the client will
use, is returned.

authenticator

```java
public abstract
Optional
<
Authenticator
> authenticator()
```

Returns an

Optional

containing the

Authenticator

set on
this client. If no

Authenticator

was set in the client's builder,
then the

Optional

is empty.

**Returns:** an

Optional

containing this client's

Authenticator

---

#### authenticator

public abstract

Optional

<

Authenticator

> authenticator()

Returns an

Optional

containing the

Authenticator

set on
this client. If no

Authenticator

was set in the client's builder,
then the

Optional

is empty.

version

```java
public abstract
HttpClient.Version
version()
```

Returns the preferred HTTP protocol version for this client. The default
value is

HttpClient.Version.HTTP_2

**Implementation Note:** Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the
implementation does not support this mode, then HTTP/1.1 may be used
**Returns:** the HTTP protocol version requested

---

#### version

public abstract

HttpClient.Version

version()

Returns the preferred HTTP protocol version for this client. The default
value is

HttpClient.Version.HTTP_2

executor

```java
public abstract
Optional
<
Executor
> executor()
```

Returns an

Optional

containing this client's

Executor

. If no

Executor

was set in the client's builder,
then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have an non-exposed

default executor

that is used for
executing asynchronous and dependent tasks.

**Returns:** an

Optional

containing this client's

Executor

---

#### executor

public abstract

Optional

<

Executor

> executor()

Returns an

Optional

containing this client's

Executor

. If no

Executor

was set in the client's builder,
then the

Optional

is empty.

Even though this method may return an empty optional, the

HttpClient

may still have an non-exposed

default executor

that is used for
executing asynchronous and dependent tasks.

Even though this method may return an empty optional, the

HttpClient

may still have an non-exposed

default executor

that is used for
executing asynchronous and dependent tasks.

send

```java
public abstract <T>
HttpResponse
<T> send​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)
throws
IOException
,

InterruptedException
```

Sends the given request using this client, blocking if necessary to get
the response. The returned

HttpResponse

<T>

contains the
response status, headers, and body ( as handled by given response body
handler ).

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Returns:** the response
**Throws:** IOException

- if an I/O error occurs when sending or receiving
**Throws:** InterruptedException

- if the operation is interrupted
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.
**Throws:** SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

---

#### send

public abstract <T>

HttpResponse

<T> send​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler)
throws

IOException

,

InterruptedException

Sends the given request using this client, blocking if necessary to get
the response. The returned

HttpResponse

<T>

contains the
response status, headers, and body ( as handled by given response body
handler ).

sendAsync

```java
public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler)
```

Sends the given request asynchronously using this client with the given
response body handler.

Equivalent to:

sendAsync(request, responseBodyHandler, null)

.

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Returns:** a

CompletableFuture<HttpResponse<T>>
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

---

#### sendAsync

public abstract <T>

CompletableFuture

<

HttpResponse

<T>> sendAsync​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler)

Sends the given request asynchronously using this client with the given
response body handler.

Equivalent to:

sendAsync(request, responseBodyHandler, null)

.

Equivalent to:

sendAsync(request, responseBodyHandler, null)

.

sendAsync

```java
public abstract <T>
CompletableFuture
<
HttpResponse
<T>> sendAsync​(
HttpRequest
request,

HttpResponse.BodyHandler
<T> responseBodyHandler,

HttpResponse.PushPromiseHandler
<T> pushPromiseHandler)
```

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

The returned completable future, if completed successfully, completes
with an

HttpResponse

<T>

that contains the response status,
headers, and body ( as handled by given response body handler ).

Push promises

received, if any, are
handled by the given

pushPromiseHandler

. A

null

valued

pushPromiseHandler

rejects any push promises.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

**Type Parameters:** T

- the response body type
**Parameters:** request

- the request
**Parameters:** responseBodyHandler

- the response body handler
**Parameters:** pushPromiseHandler

- push promise handler, may be null
**Returns:** a

CompletableFuture<HttpResponse<T>>
**Throws:** IllegalArgumentException

- if the

request

argument is not
a request that could have been validly built as specified by

HttpRequest.Builder

.

---

#### sendAsync

public abstract <T>

CompletableFuture

<

HttpResponse

<T>> sendAsync​(

HttpRequest

request,

HttpResponse.BodyHandler

<T> responseBodyHandler,

HttpResponse.PushPromiseHandler

<T> pushPromiseHandler)

Sends the given request asynchronously using this client with the given
response body handler and push promise handler.

The returned completable future, if completed successfully, completes
with an

HttpResponse

<T>

that contains the response status,
headers, and body ( as handled by given response body handler ).

Push promises

received, if any, are
handled by the given

pushPromiseHandler

. A

null

valued

pushPromiseHandler

rejects any push promises.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

The returned completable future, if completed successfully, completes
with an

HttpResponse

<T>

that contains the response status,
headers, and body ( as handled by given response body handler ).

Push promises

received, if any, are
handled by the given

pushPromiseHandler

. A

null

valued

pushPromiseHandler

rejects any push promises.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

Push promises

received, if any, are
handled by the given

pushPromiseHandler

. A

null

valued

pushPromiseHandler

rejects any push promises.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

The returned completable future completes exceptionally with:

- IOException

- if an I/O error occurs when sending or receiving
- SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

IOException

- if an I/O error occurs when sending or receiving

SecurityException

- If a security manager has been installed
and it denies

access

to the
URL in the given request, or proxy if one is configured.
See

security checks

for further
information.

newWebSocketBuilder

```java
public
WebSocket.Builder
newWebSocketBuilder()
```

Creates a new

WebSocket

builder (optional operation).

Example

```java
HttpClient client = HttpClient.newHttpClient();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Finer control over the WebSocket Opening Handshake can be achieved
by using a custom

HttpClient

.

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

**Implementation Requirements:** The default implementation of this method throws

UnsupportedOperationException

. Clients obtained through

newHttpClient()

or

newBuilder()

return a

WebSocket

builder.
**Implementation Note:** Both builder and

WebSocket

s created with it operate in
a non-blocking fashion. That is, their methods do not block before
returning a

CompletableFuture

. Asynchronous tasks are executed in
this

HttpClient

's executor.

When a

CompletionStage

returned from

Listener.onClose

completes,
the

WebSocket

will send a Close message that has the same code
the received message has and an empty reason.
**Returns:** a

WebSocket.Builder
**Throws:** UnsupportedOperationException

- if this

HttpClient

does not provide WebSocket support

---

#### newWebSocketBuilder

public

WebSocket.Builder

newWebSocketBuilder()

Creates a new

WebSocket

builder (optional operation).

Example

```java
HttpClient client = HttpClient.newHttpClient();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Finer control over the WebSocket Opening Handshake can be achieved
by using a custom

HttpClient

.

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Example

```java
HttpClient client = HttpClient.newHttpClient();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Finer control over the WebSocket Opening Handshake can be achieved
by using a custom

HttpClient

.

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

HttpClient client = HttpClient.newHttpClient();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);

Finer control over the WebSocket Opening Handshake can be achieved
by using a custom

HttpClient

.

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

Example

```java
InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);
```

InetSocketAddress addr = new InetSocketAddress("proxy.example.com", 80);
HttpClient client = HttpClient.newBuilder()
.proxy(ProxySelector.of(addr))
.build();
CompletableFuture<WebSocket> ws = client.newWebSocketBuilder()
.buildAsync(URI.create("ws://websocket.example.com"), listener);

When a

CompletionStage

returned from

Listener.onClose

completes,
the

WebSocket

will send a Close message that has the same code
the received message has and an empty reason.

---

