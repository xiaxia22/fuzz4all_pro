# Interface HttpClient.Builder

**Source:** `java.net.http\java\net\http\HttpClient.Builder.html`

### Class Description

```java
public static interface
HttpClient.Builder
```

A builder of

HTTP Clients

.

Builders are created by invoking

newBuilder

. Each of the setter methods modifies the state of the builder
and returns the same instance. Builders are not thread-safe and should not be
used concurrently from multiple threads without external synchronization.

**Enclosing class:** HttpClient

---

### Field Details

#### static final
ProxySelector
NO_PROXY

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

This is a convenience object that can be passed to

proxy(ProxySelector)

in order to build an instance of

HttpClient

that uses no proxy.

---

### Constructor Details

*No entries found.*

### Method Details

#### HttpClient.Builder
cookieHandler​(
CookieHandler
cookieHandler)

Sets a cookie handler.

**Parameters:**
- cookieHandler

- the cookie handler

**Returns:**
- this builder

---

#### HttpClient.Builder
connectTimeout​(
Duration
duration)

Sets the connect timeout duration for this client.

In the case where a new connection needs to be established, if
the connection cannot be established within the given

duration

, then

HttpClient::send

throws an

HttpConnectTimeoutException

, or

HttpClient::sendAsync

completes exceptionally with an

HttpConnectTimeoutException

. If a new connection does not
need to be established, for example if a connection can be reused
from a previous request, then this timeout duration has no effect.

**Parameters:**
- duration

- the duration to allow the underlying connection to be
established

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if the duration is non-positive

---

#### HttpClient.Builder
sslContext​(
SSLContext
sslContext)

Sets an

SSLContext

.

If this method is not invoked prior to

building

, then newly built clients will use the

default context

, which is normally adequate
for client applications that do not need to specify protocols, or
require client authentication.

**Parameters:**
- sslContext

- the SSLContext

**Returns:**
- this builder

---

#### HttpClient.Builder
sslParameters​(
SSLParameters
sslParameters)

Sets an

SSLParameters

.

If this method is not invoked prior to

building

, then newly built clients will use a default,
implementation specific, set of parameters.

Some parameters which are used internally by the HTTP Client
implementation (such as the application protocol list) should not be
set by callers, as they may be ignored. The contents of the given
object are copied.

**Parameters:**
- sslParameters

- the SSLParameters

**Returns:**
- this builder

---

#### HttpClient.Builder
executor​(
Executor
executor)

Sets the executor to be used for asynchronous and dependent tasks.

If this method is not invoked prior to

building

, a default executor is created for each newly built

HttpClient

.

**Parameters:**
- executor

- the Executor

**Returns:**
- this builder

**Implementation Note:**
- The default executor uses a thread pool, with a custom
thread factory. If a security manager has been installed, the thread
factory creates threads that run with an access control context that
has no permissions.

---

#### HttpClient.Builder
followRedirects​(
HttpClient.Redirect
policy)

Specifies whether requests will automatically follow redirects issued
by the server.

If this method is not invoked prior to

building

, then newly built clients will use a default redirection
policy of

NEVER

.

**Parameters:**
- policy

- the redirection policy

**Returns:**
- this builder

---

#### HttpClient.Builder
version​(
HttpClient.Version
version)

Requests a specific HTTP protocol version where possible.

If this method is not invoked prior to

building

, then newly built clients will prefer

HTTP/2

.

If set to

HTTP/2

, then each request
will attempt to upgrade to HTTP/2. If the upgrade succeeds, then the
response to this request will use HTTP/2 and all subsequent requests
and responses to the same

origin server

will use HTTP/2. If the upgrade fails, then the response will be
handled using HTTP/1.1

**Parameters:**
- version

- the requested HTTP protocol version

**Returns:**
- this builder

**Implementation Note:**
- Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the implementation
does not support this mode, then HTTP/1.1 may be used

---

#### HttpClient.Builder
priority​(int priority)

Sets the default priority for any HTTP/2 requests sent from this
client. The value provided must be between

1

and

256

(inclusive).

**Parameters:**
- priority

- the priority weighting

**Returns:**
- this builder

**Throws:**
- IllegalArgumentException

- if the given priority is out of range

---

#### HttpClient.Builder
proxy​(
ProxySelector
proxySelector)

Sets a

ProxySelector

.

**Parameters:**
- proxySelector

- the ProxySelector

**Returns:**
- this builder

**API Note:**
- ProxySelector::of

provides a

ProxySelector

which uses a single proxy for all
requests. The system-wide proxy selector can be retrieved by

ProxySelector.getDefault()

.

**Implementation Note:**
- If this method is not invoked prior to

building

,
then newly built clients will use the

default proxy selector

, which is usually
adequate for client applications. The default proxy selector supports
a set of system properties

related to

proxy settings

. This default behavior can be disabled by
supplying an explicit proxy selector, such as

NO_PROXY

or
one returned by

ProxySelector::of

, before

building

.

---

#### HttpClient.Builder
authenticator​(
Authenticator
authenticator)

Sets an authenticator to use for HTTP authentication.

**Parameters:**
- authenticator

- the Authenticator

**Returns:**
- this builder

---

#### HttpClient
build()

Returns a new

HttpClient

built from the current state of this
builder.

**Returns:**
- a new

HttpClient

---

### Additional Sections

#### Interface HttpClient.Builder

**Enclosing class:** HttpClient

```java
public static interface
HttpClient.Builder
```

A builder of

HTTP Clients

.

Builders are created by invoking

newBuilder

. Each of the setter methods modifies the state of the builder
and returns the same instance. Builders are not thread-safe and should not be
used concurrently from multiple threads without external synchronization.

**Since:** 11

public static interface

HttpClient.Builder

A builder of

HTTP Clients

.

Builders are created by invoking

newBuilder

. Each of the setter methods modifies the state of the builder
and returns the same instance. Builders are not thread-safe and should not be
used concurrently from multiple threads without external synchronization.

Builders are created by invoking

newBuilder

. Each of the setter methods modifies the state of the builder
and returns the same instance. Builders are not thread-safe and should not be
used concurrently from multiple threads without external synchronization.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ProxySelector

NO_PROXY

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpClient.Builder

authenticator

​(

Authenticator

authenticator)

Sets an authenticator to use for HTTP authentication.

HttpClient

build

()

Returns a new

HttpClient

built from the current state of this
builder.

HttpClient.Builder

connectTimeout

​(

Duration

duration)

Sets the connect timeout duration for this client.

HttpClient.Builder

cookieHandler

​(

CookieHandler

cookieHandler)

Sets a cookie handler.

HttpClient.Builder

executor

​(

Executor

executor)

Sets the executor to be used for asynchronous and dependent tasks.

HttpClient.Builder

followRedirects

​(

HttpClient.Redirect

policy)

Specifies whether requests will automatically follow redirects issued
by the server.

HttpClient.Builder

priority

​(int priority)

Sets the default priority for any HTTP/2 requests sent from this
client.

HttpClient.Builder

proxy

​(

ProxySelector

proxySelector)

Sets a

ProxySelector

.

HttpClient.Builder

sslContext

​(

SSLContext

sslContext)

Sets an

SSLContext

.

HttpClient.Builder

sslParameters

​(

SSLParameters

sslParameters)

Sets an

SSLParameters

.

HttpClient.Builder

version

​(

HttpClient.Version

version)

Requests a specific HTTP protocol version where possible.

Field Summary

Fields

Modifier and Type

Field

Description

static

ProxySelector

NO_PROXY

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

---

#### Field Summary

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpClient.Builder

authenticator

​(

Authenticator

authenticator)

Sets an authenticator to use for HTTP authentication.

HttpClient

build

()

Returns a new

HttpClient

built from the current state of this
builder.

HttpClient.Builder

connectTimeout

​(

Duration

duration)

Sets the connect timeout duration for this client.

HttpClient.Builder

cookieHandler

​(

CookieHandler

cookieHandler)

Sets a cookie handler.

HttpClient.Builder

executor

​(

Executor

executor)

Sets the executor to be used for asynchronous and dependent tasks.

HttpClient.Builder

followRedirects

​(

HttpClient.Redirect

policy)

Specifies whether requests will automatically follow redirects issued
by the server.

HttpClient.Builder

priority

​(int priority)

Sets the default priority for any HTTP/2 requests sent from this
client.

HttpClient.Builder

proxy

​(

ProxySelector

proxySelector)

Sets a

ProxySelector

.

HttpClient.Builder

sslContext

​(

SSLContext

sslContext)

Sets an

SSLContext

.

HttpClient.Builder

sslParameters

​(

SSLParameters

sslParameters)

Sets an

SSLParameters

.

HttpClient.Builder

version

​(

HttpClient.Version

version)

Requests a specific HTTP protocol version where possible.

---

#### Method Summary

Sets an authenticator to use for HTTP authentication.

Returns a new

HttpClient

built from the current state of this
builder.

Sets the connect timeout duration for this client.

Sets a cookie handler.

Sets the executor to be used for asynchronous and dependent tasks.

Specifies whether requests will automatically follow redirects issued
by the server.

Sets the default priority for any HTTP/2 requests sent from this
client.

Sets a

ProxySelector

.

Sets an

SSLContext

.

Sets an

SSLParameters

.

Requests a specific HTTP protocol version where possible.

============ FIELD DETAIL ===========

- Field Detail

- NO_PROXY

```java
static final
ProxySelector
NO_PROXY
```

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

This is a convenience object that can be passed to

proxy(ProxySelector)

in order to build an instance of

HttpClient

that uses no proxy.

============ METHOD DETAIL ==========

- Method Detail

- cookieHandler

```java
HttpClient.Builder
cookieHandler​(
CookieHandler
cookieHandler)
```

Sets a cookie handler.

**Parameters:** cookieHandler

- the cookie handler
**Returns:** this builder

- connectTimeout

```java
HttpClient.Builder
connectTimeout​(
Duration
duration)
```

Sets the connect timeout duration for this client.

In the case where a new connection needs to be established, if
the connection cannot be established within the given

duration

, then

HttpClient::send

throws an

HttpConnectTimeoutException

, or

HttpClient::sendAsync

completes exceptionally with an

HttpConnectTimeoutException

. If a new connection does not
need to be established, for example if a connection can be reused
from a previous request, then this timeout duration has no effect.

**Parameters:** duration

- the duration to allow the underlying connection to be
established
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the duration is non-positive

- sslContext

```java
HttpClient.Builder
sslContext​(
SSLContext
sslContext)
```

Sets an

SSLContext

.

If this method is not invoked prior to

building

, then newly built clients will use the

default context

, which is normally adequate
for client applications that do not need to specify protocols, or
require client authentication.

**Parameters:** sslContext

- the SSLContext
**Returns:** this builder

- sslParameters

```java
HttpClient.Builder
sslParameters​(
SSLParameters
sslParameters)
```

Sets an

SSLParameters

.

If this method is not invoked prior to

building

, then newly built clients will use a default,
implementation specific, set of parameters.

Some parameters which are used internally by the HTTP Client
implementation (such as the application protocol list) should not be
set by callers, as they may be ignored. The contents of the given
object are copied.

**Parameters:** sslParameters

- the SSLParameters
**Returns:** this builder

- executor

```java
HttpClient.Builder
executor​(
Executor
executor)
```

Sets the executor to be used for asynchronous and dependent tasks.

If this method is not invoked prior to

building

, a default executor is created for each newly built

HttpClient

.

**Implementation Note:** The default executor uses a thread pool, with a custom
thread factory. If a security manager has been installed, the thread
factory creates threads that run with an access control context that
has no permissions.
**Parameters:** executor

- the Executor
**Returns:** this builder

- followRedirects

```java
HttpClient.Builder
followRedirects​(
HttpClient.Redirect
policy)
```

Specifies whether requests will automatically follow redirects issued
by the server.

If this method is not invoked prior to

building

, then newly built clients will use a default redirection
policy of

NEVER

.

**Parameters:** policy

- the redirection policy
**Returns:** this builder

- version

```java
HttpClient.Builder
version​(
HttpClient.Version
version)
```

Requests a specific HTTP protocol version where possible.

If this method is not invoked prior to

building

, then newly built clients will prefer

HTTP/2

.

If set to

HTTP/2

, then each request
will attempt to upgrade to HTTP/2. If the upgrade succeeds, then the
response to this request will use HTTP/2 and all subsequent requests
and responses to the same

origin server

will use HTTP/2. If the upgrade fails, then the response will be
handled using HTTP/1.1

**Implementation Note:** Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the implementation
does not support this mode, then HTTP/1.1 may be used
**Parameters:** version

- the requested HTTP protocol version
**Returns:** this builder

- priority

```java
HttpClient.Builder
priority​(int priority)
```

Sets the default priority for any HTTP/2 requests sent from this
client. The value provided must be between

1

and

256

(inclusive).

**Parameters:** priority

- the priority weighting
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the given priority is out of range

- proxy

```java
HttpClient.Builder
proxy​(
ProxySelector
proxySelector)
```

Sets a

ProxySelector

.

**API Note:** ProxySelector::of

provides a

ProxySelector

which uses a single proxy for all
requests. The system-wide proxy selector can be retrieved by

ProxySelector.getDefault()

.
**Implementation Note:** If this method is not invoked prior to

building

,
then newly built clients will use the

default proxy selector

, which is usually
adequate for client applications. The default proxy selector supports
a set of system properties

related to

proxy settings

. This default behavior can be disabled by
supplying an explicit proxy selector, such as

NO_PROXY

or
one returned by

ProxySelector::of

, before

building

.
**Parameters:** proxySelector

- the ProxySelector
**Returns:** this builder

- authenticator

```java
HttpClient.Builder
authenticator​(
Authenticator
authenticator)
```

Sets an authenticator to use for HTTP authentication.

**Parameters:** authenticator

- the Authenticator
**Returns:** this builder

- build

```java
HttpClient
build()
```

Returns a new

HttpClient

built from the current state of this
builder.

**Returns:** a new

HttpClient

Field Detail

- NO_PROXY

```java
static final
ProxySelector
NO_PROXY
```

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

This is a convenience object that can be passed to

proxy(ProxySelector)

in order to build an instance of

HttpClient

that uses no proxy.

---

#### Field Detail

NO_PROXY

```java
static final
ProxySelector
NO_PROXY
```

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

This is a convenience object that can be passed to

proxy(ProxySelector)

in order to build an instance of

HttpClient

that uses no proxy.

---

#### NO_PROXY

static final

ProxySelector

NO_PROXY

A proxy selector that always return

Proxy.NO_PROXY

implying
a direct connection.

This is a convenience object that can be passed to

proxy(ProxySelector)

in order to build an instance of

HttpClient

that uses no proxy.

This is a convenience object that can be passed to

proxy(ProxySelector)

in order to build an instance of

HttpClient

that uses no proxy.

Method Detail

- cookieHandler

```java
HttpClient.Builder
cookieHandler​(
CookieHandler
cookieHandler)
```

Sets a cookie handler.

**Parameters:** cookieHandler

- the cookie handler
**Returns:** this builder

- connectTimeout

```java
HttpClient.Builder
connectTimeout​(
Duration
duration)
```

Sets the connect timeout duration for this client.

In the case where a new connection needs to be established, if
the connection cannot be established within the given

duration

, then

HttpClient::send

throws an

HttpConnectTimeoutException

, or

HttpClient::sendAsync

completes exceptionally with an

HttpConnectTimeoutException

. If a new connection does not
need to be established, for example if a connection can be reused
from a previous request, then this timeout duration has no effect.

**Parameters:** duration

- the duration to allow the underlying connection to be
established
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the duration is non-positive

- sslContext

```java
HttpClient.Builder
sslContext​(
SSLContext
sslContext)
```

Sets an

SSLContext

.

If this method is not invoked prior to

building

, then newly built clients will use the

default context

, which is normally adequate
for client applications that do not need to specify protocols, or
require client authentication.

**Parameters:** sslContext

- the SSLContext
**Returns:** this builder

- sslParameters

```java
HttpClient.Builder
sslParameters​(
SSLParameters
sslParameters)
```

Sets an

SSLParameters

.

If this method is not invoked prior to

building

, then newly built clients will use a default,
implementation specific, set of parameters.

Some parameters which are used internally by the HTTP Client
implementation (such as the application protocol list) should not be
set by callers, as they may be ignored. The contents of the given
object are copied.

**Parameters:** sslParameters

- the SSLParameters
**Returns:** this builder

- executor

```java
HttpClient.Builder
executor​(
Executor
executor)
```

Sets the executor to be used for asynchronous and dependent tasks.

If this method is not invoked prior to

building

, a default executor is created for each newly built

HttpClient

.

**Implementation Note:** The default executor uses a thread pool, with a custom
thread factory. If a security manager has been installed, the thread
factory creates threads that run with an access control context that
has no permissions.
**Parameters:** executor

- the Executor
**Returns:** this builder

- followRedirects

```java
HttpClient.Builder
followRedirects​(
HttpClient.Redirect
policy)
```

Specifies whether requests will automatically follow redirects issued
by the server.

If this method is not invoked prior to

building

, then newly built clients will use a default redirection
policy of

NEVER

.

**Parameters:** policy

- the redirection policy
**Returns:** this builder

- version

```java
HttpClient.Builder
version​(
HttpClient.Version
version)
```

Requests a specific HTTP protocol version where possible.

If this method is not invoked prior to

building

, then newly built clients will prefer

HTTP/2

.

If set to

HTTP/2

, then each request
will attempt to upgrade to HTTP/2. If the upgrade succeeds, then the
response to this request will use HTTP/2 and all subsequent requests
and responses to the same

origin server

will use HTTP/2. If the upgrade fails, then the response will be
handled using HTTP/1.1

**Implementation Note:** Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the implementation
does not support this mode, then HTTP/1.1 may be used
**Parameters:** version

- the requested HTTP protocol version
**Returns:** this builder

- priority

```java
HttpClient.Builder
priority​(int priority)
```

Sets the default priority for any HTTP/2 requests sent from this
client. The value provided must be between

1

and

256

(inclusive).

**Parameters:** priority

- the priority weighting
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the given priority is out of range

- proxy

```java
HttpClient.Builder
proxy​(
ProxySelector
proxySelector)
```

Sets a

ProxySelector

.

**API Note:** ProxySelector::of

provides a

ProxySelector

which uses a single proxy for all
requests. The system-wide proxy selector can be retrieved by

ProxySelector.getDefault()

.
**Implementation Note:** If this method is not invoked prior to

building

,
then newly built clients will use the

default proxy selector

, which is usually
adequate for client applications. The default proxy selector supports
a set of system properties

related to

proxy settings

. This default behavior can be disabled by
supplying an explicit proxy selector, such as

NO_PROXY

or
one returned by

ProxySelector::of

, before

building

.
**Parameters:** proxySelector

- the ProxySelector
**Returns:** this builder

- authenticator

```java
HttpClient.Builder
authenticator​(
Authenticator
authenticator)
```

Sets an authenticator to use for HTTP authentication.

**Parameters:** authenticator

- the Authenticator
**Returns:** this builder

- build

```java
HttpClient
build()
```

Returns a new

HttpClient

built from the current state of this
builder.

**Returns:** a new

HttpClient

---

#### Method Detail

cookieHandler

```java
HttpClient.Builder
cookieHandler​(
CookieHandler
cookieHandler)
```

Sets a cookie handler.

**Parameters:** cookieHandler

- the cookie handler
**Returns:** this builder

---

#### cookieHandler

HttpClient.Builder

cookieHandler​(

CookieHandler

cookieHandler)

Sets a cookie handler.

connectTimeout

```java
HttpClient.Builder
connectTimeout​(
Duration
duration)
```

Sets the connect timeout duration for this client.

In the case where a new connection needs to be established, if
the connection cannot be established within the given

duration

, then

HttpClient::send

throws an

HttpConnectTimeoutException

, or

HttpClient::sendAsync

completes exceptionally with an

HttpConnectTimeoutException

. If a new connection does not
need to be established, for example if a connection can be reused
from a previous request, then this timeout duration has no effect.

**Parameters:** duration

- the duration to allow the underlying connection to be
established
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the duration is non-positive

---

#### connectTimeout

HttpClient.Builder

connectTimeout​(

Duration

duration)

Sets the connect timeout duration for this client.

In the case where a new connection needs to be established, if
the connection cannot be established within the given

duration

, then

HttpClient::send

throws an

HttpConnectTimeoutException

, or

HttpClient::sendAsync

completes exceptionally with an

HttpConnectTimeoutException

. If a new connection does not
need to be established, for example if a connection can be reused
from a previous request, then this timeout duration has no effect.

In the case where a new connection needs to be established, if
the connection cannot be established within the given

duration

, then

HttpClient::send

throws an

HttpConnectTimeoutException

, or

HttpClient::sendAsync

completes exceptionally with an

HttpConnectTimeoutException

. If a new connection does not
need to be established, for example if a connection can be reused
from a previous request, then this timeout duration has no effect.

sslContext

```java
HttpClient.Builder
sslContext​(
SSLContext
sslContext)
```

Sets an

SSLContext

.

If this method is not invoked prior to

building

, then newly built clients will use the

default context

, which is normally adequate
for client applications that do not need to specify protocols, or
require client authentication.

**Parameters:** sslContext

- the SSLContext
**Returns:** this builder

---

#### sslContext

HttpClient.Builder

sslContext​(

SSLContext

sslContext)

Sets an

SSLContext

.

If this method is not invoked prior to

building

, then newly built clients will use the

default context

, which is normally adequate
for client applications that do not need to specify protocols, or
require client authentication.

If this method is not invoked prior to

building

, then newly built clients will use the

default context

, which is normally adequate
for client applications that do not need to specify protocols, or
require client authentication.

sslParameters

```java
HttpClient.Builder
sslParameters​(
SSLParameters
sslParameters)
```

Sets an

SSLParameters

.

If this method is not invoked prior to

building

, then newly built clients will use a default,
implementation specific, set of parameters.

Some parameters which are used internally by the HTTP Client
implementation (such as the application protocol list) should not be
set by callers, as they may be ignored. The contents of the given
object are copied.

**Parameters:** sslParameters

- the SSLParameters
**Returns:** this builder

---

#### sslParameters

HttpClient.Builder

sslParameters​(

SSLParameters

sslParameters)

Sets an

SSLParameters

.

If this method is not invoked prior to

building

, then newly built clients will use a default,
implementation specific, set of parameters.

Some parameters which are used internally by the HTTP Client
implementation (such as the application protocol list) should not be
set by callers, as they may be ignored. The contents of the given
object are copied.

If this method is not invoked prior to

building

, then newly built clients will use a default,
implementation specific, set of parameters.

Some parameters which are used internally by the HTTP Client
implementation (such as the application protocol list) should not be
set by callers, as they may be ignored. The contents of the given
object are copied.

Some parameters which are used internally by the HTTP Client
implementation (such as the application protocol list) should not be
set by callers, as they may be ignored. The contents of the given
object are copied.

executor

```java
HttpClient.Builder
executor​(
Executor
executor)
```

Sets the executor to be used for asynchronous and dependent tasks.

If this method is not invoked prior to

building

, a default executor is created for each newly built

HttpClient

.

**Implementation Note:** The default executor uses a thread pool, with a custom
thread factory. If a security manager has been installed, the thread
factory creates threads that run with an access control context that
has no permissions.
**Parameters:** executor

- the Executor
**Returns:** this builder

---

#### executor

HttpClient.Builder

executor​(

Executor

executor)

Sets the executor to be used for asynchronous and dependent tasks.

If this method is not invoked prior to

building

, a default executor is created for each newly built

HttpClient

.

If this method is not invoked prior to

building

, a default executor is created for each newly built

HttpClient

.

followRedirects

```java
HttpClient.Builder
followRedirects​(
HttpClient.Redirect
policy)
```

Specifies whether requests will automatically follow redirects issued
by the server.

If this method is not invoked prior to

building

, then newly built clients will use a default redirection
policy of

NEVER

.

**Parameters:** policy

- the redirection policy
**Returns:** this builder

---

#### followRedirects

HttpClient.Builder

followRedirects​(

HttpClient.Redirect

policy)

Specifies whether requests will automatically follow redirects issued
by the server.

If this method is not invoked prior to

building

, then newly built clients will use a default redirection
policy of

NEVER

.

If this method is not invoked prior to

building

, then newly built clients will use a default redirection
policy of

NEVER

.

version

```java
HttpClient.Builder
version​(
HttpClient.Version
version)
```

Requests a specific HTTP protocol version where possible.

If this method is not invoked prior to

building

, then newly built clients will prefer

HTTP/2

.

If set to

HTTP/2

, then each request
will attempt to upgrade to HTTP/2. If the upgrade succeeds, then the
response to this request will use HTTP/2 and all subsequent requests
and responses to the same

origin server

will use HTTP/2. If the upgrade fails, then the response will be
handled using HTTP/1.1

**Implementation Note:** Constraints may also affect the selection of protocol version.
For example, if HTTP/2 is requested through a proxy, and if the implementation
does not support this mode, then HTTP/1.1 may be used
**Parameters:** version

- the requested HTTP protocol version
**Returns:** this builder

---

#### version

HttpClient.Builder

version​(

HttpClient.Version

version)

Requests a specific HTTP protocol version where possible.

If this method is not invoked prior to

building

, then newly built clients will prefer

HTTP/2

.

If set to

HTTP/2

, then each request
will attempt to upgrade to HTTP/2. If the upgrade succeeds, then the
response to this request will use HTTP/2 and all subsequent requests
and responses to the same

origin server

will use HTTP/2. If the upgrade fails, then the response will be
handled using HTTP/1.1

If this method is not invoked prior to

building

, then newly built clients will prefer

HTTP/2

.

If set to

HTTP/2

, then each request
will attempt to upgrade to HTTP/2. If the upgrade succeeds, then the
response to this request will use HTTP/2 and all subsequent requests
and responses to the same

origin server

will use HTTP/2. If the upgrade fails, then the response will be
handled using HTTP/1.1

If set to

HTTP/2

, then each request
will attempt to upgrade to HTTP/2. If the upgrade succeeds, then the
response to this request will use HTTP/2 and all subsequent requests
and responses to the same

origin server

will use HTTP/2. If the upgrade fails, then the response will be
handled using HTTP/1.1

priority

```java
HttpClient.Builder
priority​(int priority)
```

Sets the default priority for any HTTP/2 requests sent from this
client. The value provided must be between

1

and

256

(inclusive).

**Parameters:** priority

- the priority weighting
**Returns:** this builder
**Throws:** IllegalArgumentException

- if the given priority is out of range

---

#### priority

HttpClient.Builder

priority​(int priority)

Sets the default priority for any HTTP/2 requests sent from this
client. The value provided must be between

1

and

256

(inclusive).

proxy

```java
HttpClient.Builder
proxy​(
ProxySelector
proxySelector)
```

Sets a

ProxySelector

.

**API Note:** ProxySelector::of

provides a

ProxySelector

which uses a single proxy for all
requests. The system-wide proxy selector can be retrieved by

ProxySelector.getDefault()

.
**Implementation Note:** If this method is not invoked prior to

building

,
then newly built clients will use the

default proxy selector

, which is usually
adequate for client applications. The default proxy selector supports
a set of system properties

related to

proxy settings

. This default behavior can be disabled by
supplying an explicit proxy selector, such as

NO_PROXY

or
one returned by

ProxySelector::of

, before

building

.
**Parameters:** proxySelector

- the ProxySelector
**Returns:** this builder

---

#### proxy

HttpClient.Builder

proxy​(

ProxySelector

proxySelector)

Sets a

ProxySelector

.

authenticator

```java
HttpClient.Builder
authenticator​(
Authenticator
authenticator)
```

Sets an authenticator to use for HTTP authentication.

**Parameters:** authenticator

- the Authenticator
**Returns:** this builder

---

#### authenticator

HttpClient.Builder

authenticator​(

Authenticator

authenticator)

Sets an authenticator to use for HTTP authentication.

build

```java
HttpClient
build()
```

Returns a new

HttpClient

built from the current state of this
builder.

**Returns:** a new

HttpClient

---

#### build

HttpClient

build()

Returns a new

HttpClient

built from the current state of this
builder.

---

