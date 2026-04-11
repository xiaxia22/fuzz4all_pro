# Interface WebSocket.Builder

**Source:** `java.net.http\java\net\http\WebSocket.Builder.html`

### Class Description

```java
public static interface
WebSocket.Builder
```

A builder of

WebSocket Clients

.

Builders are created by invoking

HttpClient.newWebSocketBuilder

.
The intermediate (setter-like) methods change the state of the builder
and return the same builder they have been invoked on. If an intermediate
method is not invoked, an appropriate default value (or behavior) will be
assumed. A

Builder

is not safe for use by multiple threads
without external synchronization.

**Enclosing interface:** WebSocket

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### WebSocket.Builder
header​(
String
name,

String
value)

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

Headers defined in the

WebSocket
Protocol

are illegal. If this method is not invoked, no
additional HTTP headers will be sent.

**Parameters:**
- name

- the header name
- value

- the header value

**Returns:**
- this builder

---

#### WebSocket.Builder
connectTimeout​(
Duration
timeout)

Sets a timeout for establishing a WebSocket connection.

If the connection is not established within the specified
duration then building of the

WebSocket

will fail with

HttpTimeoutException

. If this method is not invoked then the
infinite timeout is assumed.

**Parameters:**
- timeout

- the timeout, non-

negative

,
non-

ZERO

**Returns:**
- this builder

---

#### WebSocket.Builder
subprotocols​(
String
mostPreferred,

String
... lesserPreferred)

Sets a request for the given subprotocols.

After the

WebSocket

has been built, the actual
subprotocol can be queried through

WebSocket.getSubprotocol()

.

Subprotocols are specified in the order of preference. The most
preferred subprotocol is specified first. If there are any additional
subprotocols they are enumerated from the most preferred to the least
preferred.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

**Parameters:**
- mostPreferred

- the most preferred subprotocol
- lesserPreferred

- the lesser preferred subprotocols

**Returns:**
- this builder

---

#### CompletableFuture
<
WebSocket
> buildAsync​(
URI
uri,

WebSocket.Listener
listener)

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

Returns a

CompletableFuture

which will either complete
normally with the resulting

WebSocket

or complete
exceptionally with one of the following errors:

- IOException

-
if an I/O error occurs

WebSocketHandshakeException

-
if the opening handshake fails

HttpTimeoutException

-
if the opening handshake does not complete within
the timeout

InterruptedException

-
if the operation is interrupted

SecurityException

-
if a security manager has been installed and it denies

access

to

uri

.

Security checks

contains more information relating to the security context
in which the the listener is invoked.

IllegalArgumentException

-
if any of the arguments of this builder's methods are
illegal

**Parameters:**
- uri

- the WebSocket URI
- listener

- the listener

**Returns:**
- a

CompletableFuture

with the

WebSocket

---

### Additional Sections

#### Interface WebSocket.Builder

**Enclosing interface:** WebSocket

```java
public static interface
WebSocket.Builder
```

A builder of

WebSocket Clients

.

Builders are created by invoking

HttpClient.newWebSocketBuilder

.
The intermediate (setter-like) methods change the state of the builder
and return the same builder they have been invoked on. If an intermediate
method is not invoked, an appropriate default value (or behavior) will be
assumed. A

Builder

is not safe for use by multiple threads
without external synchronization.

**Since:** 11

public static interface

WebSocket.Builder

A builder of

WebSocket Clients

.

Builders are created by invoking

HttpClient.newWebSocketBuilder

.
The intermediate (setter-like) methods change the state of the builder
and return the same builder they have been invoked on. If an intermediate
method is not invoked, an appropriate default value (or behavior) will be
assumed. A

Builder

is not safe for use by multiple threads
without external synchronization.

Builders are created by invoking

HttpClient.newWebSocketBuilder

.
The intermediate (setter-like) methods change the state of the builder
and return the same builder they have been invoked on. If an intermediate
method is not invoked, an appropriate default value (or behavior) will be
assumed. A

Builder

is not safe for use by multiple threads
without external synchronization.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompletableFuture

<

WebSocket

>

buildAsync

​(

URI

uri,

WebSocket.Listener

listener)

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

WebSocket.Builder

connectTimeout

​(

Duration

timeout)

Sets a timeout for establishing a WebSocket connection.

WebSocket.Builder

header

​(

String

name,

String

value)

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

WebSocket.Builder

subprotocols

​(

String

mostPreferred,

String

... lesserPreferred)

Sets a request for the given subprotocols.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompletableFuture

<

WebSocket

>

buildAsync

​(

URI

uri,

WebSocket.Listener

listener)

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

WebSocket.Builder

connectTimeout

​(

Duration

timeout)

Sets a timeout for establishing a WebSocket connection.

WebSocket.Builder

header

​(

String

name,

String

value)

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

WebSocket.Builder

subprotocols

​(

String

mostPreferred,

String

... lesserPreferred)

Sets a request for the given subprotocols.

---

#### Method Summary

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

Sets a timeout for establishing a WebSocket connection.

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

Sets a request for the given subprotocols.

============ METHOD DETAIL ==========

- Method Detail

- header

```java
WebSocket.Builder
header​(
String
name,

String
value)
```

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

Headers defined in the

WebSocket
Protocol

are illegal. If this method is not invoked, no
additional HTTP headers will be sent.

**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder

- connectTimeout

```java
WebSocket.Builder
connectTimeout​(
Duration
timeout)
```

Sets a timeout for establishing a WebSocket connection.

If the connection is not established within the specified
duration then building of the

WebSocket

will fail with

HttpTimeoutException

. If this method is not invoked then the
infinite timeout is assumed.

**Parameters:** timeout

- the timeout, non-

negative

,
non-

ZERO
**Returns:** this builder

- subprotocols

```java
WebSocket.Builder
subprotocols​(
String
mostPreferred,

String
... lesserPreferred)
```

Sets a request for the given subprotocols.

After the

WebSocket

has been built, the actual
subprotocol can be queried through

WebSocket.getSubprotocol()

.

Subprotocols are specified in the order of preference. The most
preferred subprotocol is specified first. If there are any additional
subprotocols they are enumerated from the most preferred to the least
preferred.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

**Parameters:** mostPreferred

- the most preferred subprotocol
**Parameters:** lesserPreferred

- the lesser preferred subprotocols
**Returns:** this builder

- buildAsync

```java
CompletableFuture
<
WebSocket
> buildAsync​(
URI
uri,

WebSocket.Listener
listener)
```

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

Returns a

CompletableFuture

which will either complete
normally with the resulting

WebSocket

or complete
exceptionally with one of the following errors:

- IOException

-
if an I/O error occurs

WebSocketHandshakeException

-
if the opening handshake fails

HttpTimeoutException

-
if the opening handshake does not complete within
the timeout

InterruptedException

-
if the operation is interrupted

SecurityException

-
if a security manager has been installed and it denies

access

to

uri

.

Security checks

contains more information relating to the security context
in which the the listener is invoked.

IllegalArgumentException

-
if any of the arguments of this builder's methods are
illegal

**Parameters:** uri

- the WebSocket URI
**Parameters:** listener

- the listener
**Returns:** a

CompletableFuture

with the

WebSocket

Method Detail

- header

```java
WebSocket.Builder
header​(
String
name,

String
value)
```

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

Headers defined in the

WebSocket
Protocol

are illegal. If this method is not invoked, no
additional HTTP headers will be sent.

**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder

- connectTimeout

```java
WebSocket.Builder
connectTimeout​(
Duration
timeout)
```

Sets a timeout for establishing a WebSocket connection.

If the connection is not established within the specified
duration then building of the

WebSocket

will fail with

HttpTimeoutException

. If this method is not invoked then the
infinite timeout is assumed.

**Parameters:** timeout

- the timeout, non-

negative

,
non-

ZERO
**Returns:** this builder

- subprotocols

```java
WebSocket.Builder
subprotocols​(
String
mostPreferred,

String
... lesserPreferred)
```

Sets a request for the given subprotocols.

After the

WebSocket

has been built, the actual
subprotocol can be queried through

WebSocket.getSubprotocol()

.

Subprotocols are specified in the order of preference. The most
preferred subprotocol is specified first. If there are any additional
subprotocols they are enumerated from the most preferred to the least
preferred.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

**Parameters:** mostPreferred

- the most preferred subprotocol
**Parameters:** lesserPreferred

- the lesser preferred subprotocols
**Returns:** this builder

- buildAsync

```java
CompletableFuture
<
WebSocket
> buildAsync​(
URI
uri,

WebSocket.Listener
listener)
```

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

Returns a

CompletableFuture

which will either complete
normally with the resulting

WebSocket

or complete
exceptionally with one of the following errors:

- IOException

-
if an I/O error occurs

WebSocketHandshakeException

-
if the opening handshake fails

HttpTimeoutException

-
if the opening handshake does not complete within
the timeout

InterruptedException

-
if the operation is interrupted

SecurityException

-
if a security manager has been installed and it denies

access

to

uri

.

Security checks

contains more information relating to the security context
in which the the listener is invoked.

IllegalArgumentException

-
if any of the arguments of this builder's methods are
illegal

**Parameters:** uri

- the WebSocket URI
**Parameters:** listener

- the listener
**Returns:** a

CompletableFuture

with the

WebSocket

---

#### Method Detail

header

```java
WebSocket.Builder
header​(
String
name,

String
value)
```

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

Headers defined in the

WebSocket
Protocol

are illegal. If this method is not invoked, no
additional HTTP headers will be sent.

**Parameters:** name

- the header name
**Parameters:** value

- the header value
**Returns:** this builder

---

#### header

WebSocket.Builder

header​(

String

name,

String

value)

Adds the given name-value pair to the list of additional HTTP headers
sent during the opening handshake.

Headers defined in the

WebSocket
Protocol

are illegal. If this method is not invoked, no
additional HTTP headers will be sent.

Headers defined in the

WebSocket
Protocol

are illegal. If this method is not invoked, no
additional HTTP headers will be sent.

connectTimeout

```java
WebSocket.Builder
connectTimeout​(
Duration
timeout)
```

Sets a timeout for establishing a WebSocket connection.

If the connection is not established within the specified
duration then building of the

WebSocket

will fail with

HttpTimeoutException

. If this method is not invoked then the
infinite timeout is assumed.

**Parameters:** timeout

- the timeout, non-

negative

,
non-

ZERO
**Returns:** this builder

---

#### connectTimeout

WebSocket.Builder

connectTimeout​(

Duration

timeout)

Sets a timeout for establishing a WebSocket connection.

If the connection is not established within the specified
duration then building of the

WebSocket

will fail with

HttpTimeoutException

. If this method is not invoked then the
infinite timeout is assumed.

If the connection is not established within the specified
duration then building of the

WebSocket

will fail with

HttpTimeoutException

. If this method is not invoked then the
infinite timeout is assumed.

subprotocols

```java
WebSocket.Builder
subprotocols​(
String
mostPreferred,

String
... lesserPreferred)
```

Sets a request for the given subprotocols.

After the

WebSocket

has been built, the actual
subprotocol can be queried through

WebSocket.getSubprotocol()

.

Subprotocols are specified in the order of preference. The most
preferred subprotocol is specified first. If there are any additional
subprotocols they are enumerated from the most preferred to the least
preferred.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

**Parameters:** mostPreferred

- the most preferred subprotocol
**Parameters:** lesserPreferred

- the lesser preferred subprotocols
**Returns:** this builder

---

#### subprotocols

WebSocket.Builder

subprotocols​(

String

mostPreferred,

String

... lesserPreferred)

Sets a request for the given subprotocols.

After the

WebSocket

has been built, the actual
subprotocol can be queried through

WebSocket.getSubprotocol()

.

Subprotocols are specified in the order of preference. The most
preferred subprotocol is specified first. If there are any additional
subprotocols they are enumerated from the most preferred to the least
preferred.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

After the

WebSocket

has been built, the actual
subprotocol can be queried through

WebSocket.getSubprotocol()

.

Subprotocols are specified in the order of preference. The most
preferred subprotocol is specified first. If there are any additional
subprotocols they are enumerated from the most preferred to the least
preferred.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

Subprotocols are specified in the order of preference. The most
preferred subprotocol is specified first. If there are any additional
subprotocols they are enumerated from the most preferred to the least
preferred.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

Subprotocols not conforming to the syntax of subprotocol
identifiers are illegal. If this method is not invoked then no
subprotocols will be requested.

buildAsync

```java
CompletableFuture
<
WebSocket
> buildAsync​(
URI
uri,

WebSocket.Listener
listener)
```

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

Returns a

CompletableFuture

which will either complete
normally with the resulting

WebSocket

or complete
exceptionally with one of the following errors:

- IOException

-
if an I/O error occurs

WebSocketHandshakeException

-
if the opening handshake fails

HttpTimeoutException

-
if the opening handshake does not complete within
the timeout

InterruptedException

-
if the operation is interrupted

SecurityException

-
if a security manager has been installed and it denies

access

to

uri

.

Security checks

contains more information relating to the security context
in which the the listener is invoked.

IllegalArgumentException

-
if any of the arguments of this builder's methods are
illegal

**Parameters:** uri

- the WebSocket URI
**Parameters:** listener

- the listener
**Returns:** a

CompletableFuture

with the

WebSocket

---

#### buildAsync

CompletableFuture

<

WebSocket

> buildAsync​(

URI

uri,

WebSocket.Listener

listener)

Builds a

WebSocket

connected to the given

URI

and
associated with the given

Listener

.

Returns a

CompletableFuture

which will either complete
normally with the resulting

WebSocket

or complete
exceptionally with one of the following errors:

- IOException

-
if an I/O error occurs

WebSocketHandshakeException

-
if the opening handshake fails

HttpTimeoutException

-
if the opening handshake does not complete within
the timeout

InterruptedException

-
if the operation is interrupted

SecurityException

-
if a security manager has been installed and it denies

access

to

uri

.

Security checks

contains more information relating to the security context
in which the the listener is invoked.

IllegalArgumentException

-
if any of the arguments of this builder's methods are
illegal

Returns a

CompletableFuture

which will either complete
normally with the resulting

WebSocket

or complete
exceptionally with one of the following errors:

- IOException

-
if an I/O error occurs

WebSocketHandshakeException

-
if the opening handshake fails

HttpTimeoutException

-
if the opening handshake does not complete within
the timeout

InterruptedException

-
if the operation is interrupted

SecurityException

-
if a security manager has been installed and it denies

access

to

uri

.

Security checks

contains more information relating to the security context
in which the the listener is invoked.

IllegalArgumentException

-
if any of the arguments of this builder's methods are
illegal

IOException

-
if an I/O error occurs

WebSocketHandshakeException

-
if the opening handshake fails

HttpTimeoutException

-
if the opening handshake does not complete within
the timeout

InterruptedException

-
if the operation is interrupted

SecurityException

-
if a security manager has been installed and it denies

access

to

uri

.

Security checks

contains more information relating to the security context
in which the the listener is invoked.

IllegalArgumentException

-
if any of the arguments of this builder's methods are
illegal

---

