# Class HttpServer

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpServer.html`

### Class Description

```java
public abstract class
HttpServer

extends
Object
```

This class implements a simple HTTP server. A HttpServer is bound to an IP address
and port number and listens for incoming TCP connections from clients on this address.
The sub-class

HttpsServer

implements a server which handles HTTPS requests.

One or more

HttpHandler

objects must be associated with a server
in order to process requests. Each such HttpHandler is registered
with a root URI path which represents the
location of the application or service on this server. The mapping of a handler
to a HttpServer is encapsulated by a

HttpContext

object. HttpContexts
are created by calling

createContext(String,HttpHandler)

.
Any request for which no handler can be found is rejected with a 404 response.
Management of threads can be done external to this object by providing a

Executor

object. If none is provided a default
implementation is used.

Mapping request URIs to HttpContext paths

When a HTTP request is received,
the appropriate HttpContext (and handler) is located by finding the context
whose path is the longest matching prefix of the request URI's path.
Paths are matched literally, which means that the strings are compared
case sensitively, and with no conversion to or from any encoded forms.
For example. Given a HttpServer with the following HttpContexts configured.

description

Context

Context path

ctx1

"/"

ctx2

"/apps/"

ctx3

"/apps/foo/"

the following table shows some request URIs and which, if any context they would
match with.

description

Request URI

Matches context

"http://foo.com/apps/foo/bar"

ctx3

"http://foo.com/apps/Foo/bar"

no match, wrong case

"http://foo.com/apps/app1"

ctx2

"http://foo.com/foo"

ctx1

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

**Direct Known Subclasses:** HttpsServer

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpServer()

*No description found.*

---

### Method Details

#### public static
HttpServer
create()
throws
IOException

creates a HttpServer instance which is initially not bound to any local address/port.
The HttpServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

bind(InetSocketAddress,int)

before it can be used.

**Throws:**
- IOException

---

#### public static
HttpServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpServer is acquired from the currently installed

HttpServerProvider

**Parameters:**
- addr

- the address to listen on, if

null

then bind() must be called
to set the address
- backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.

**Throws:**
- BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
- IOException

---

#### public abstract void bind​(
InetSocketAddress
addr,
int backlog)
throws
IOException

Binds a currently unbound HttpServer to the given address and port number.
A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.

**Parameters:**
- addr

- the address to listen on
- backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.

**Throws:**
- BindException

- if the server cannot bind to the requested address or if the server
is already bound.
- NullPointerException

- if addr is

null
- IOException

---

#### public abstract void start()

Starts this server in a new background thread. The background thread
inherits the priority, thread group and context class loader
of the caller.

---

#### public abstract void setExecutor​(
Executor
executor)

sets this server's

Executor

object. An
Executor must be established before

start()

is called.
All HTTP requests are handled in tasks given to the executor.
If this method is not called (before start()) or if it is
called with a

null

Executor, then
a default implementation is used, which uses the thread
which was created by the

start()

method.

**Parameters:**
- executor

- the Executor to set, or

null

for default
implementation

**Throws:**
- IllegalStateException

- if the server is already started

---

#### public abstract
Executor
getExecutor()

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

**Returns:**
- the Executor established for this server or

null

if not set.

---

#### public abstract void stop​(int delay)

stops this server by closing the listening socket and disallowing
any new exchanges from being processed. The method will then block
until all current exchange handlers have completed or else when
approximately

delay

seconds have elapsed (whichever happens
sooner). Then, all open TCP connections are closed, the background
thread created by start() exits, and the method returns.
Once stopped, a HttpServer cannot be re-used.

**Parameters:**
- delay

- the maximum time in seconds to wait until exchanges have finished.

**Throws:**
- IllegalArgumentException

- if delay is less than zero.

---

#### public abstract
HttpContext
createContext​(
String
path,

HttpHandler
handler)

Creates a HttpContext. A HttpContext represents a mapping from a
URI path to a exchange handler on this HttpServer. Once created, all requests
received by the server for the path will be handled by calling
the given handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:**
- path

- the root URI path to associate the context with
- handler

- the handler to invoke for incoming requests.

**Throws:**
- IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
- NullPointerException

- if either path, or handler are

null

---

#### public abstract
HttpContext
createContext​(
String
path)

Creates a HttpContext without initially specifying a handler. The handler must later be specified using

HttpContext.setHandler(HttpHandler)

. A HttpContext represents a mapping from a
URI path to an exchange handler on this HttpServer. Once created, and when
the handler has been set, all requests
received by the server for the path will be handled by calling
the handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:**
- path

- the root URI path to associate the context with

**Throws:**
- IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
- NullPointerException

- if path is

null

---

#### public abstract void removeContext​(
String
path)
throws
IllegalArgumentException

Removes the context identified by the given path from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:**
- path

- the path of the handler to remove

**Throws:**
- IllegalArgumentException

- if no handler corresponding to this
path exists.
- NullPointerException

- if path is

null

---

#### public abstract void removeContext​(
HttpContext
context)

Removes the given context from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:**
- context

- the context to remove

**Throws:**
- NullPointerException

- if context is

null

---

#### public abstract
InetSocketAddress
getAddress()

returns the address this server is listening on

**Returns:**
- the address/port number the server is listening on

---

### Additional Sections

#### Class HttpServer

java.lang.Object

- com.sun.net.httpserver.HttpServer

com.sun.net.httpserver.HttpServer

**Direct Known Subclasses:** HttpsServer

```java
public abstract class
HttpServer

extends
Object
```

This class implements a simple HTTP server. A HttpServer is bound to an IP address
and port number and listens for incoming TCP connections from clients on this address.
The sub-class

HttpsServer

implements a server which handles HTTPS requests.

One or more

HttpHandler

objects must be associated with a server
in order to process requests. Each such HttpHandler is registered
with a root URI path which represents the
location of the application or service on this server. The mapping of a handler
to a HttpServer is encapsulated by a

HttpContext

object. HttpContexts
are created by calling

createContext(String,HttpHandler)

.
Any request for which no handler can be found is rejected with a 404 response.
Management of threads can be done external to this object by providing a

Executor

object. If none is provided a default
implementation is used.

Mapping request URIs to HttpContext paths

When a HTTP request is received,
the appropriate HttpContext (and handler) is located by finding the context
whose path is the longest matching prefix of the request URI's path.
Paths are matched literally, which means that the strings are compared
case sensitively, and with no conversion to or from any encoded forms.
For example. Given a HttpServer with the following HttpContexts configured.

description

Context

Context path

ctx1

"/"

ctx2

"/apps/"

ctx3

"/apps/foo/"

the following table shows some request URIs and which, if any context they would
match with.

description

Request URI

Matches context

"http://foo.com/apps/foo/bar"

ctx3

"http://foo.com/apps/Foo/bar"

no match, wrong case

"http://foo.com/apps/app1"

ctx2

"http://foo.com/foo"

ctx1

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

**Since:** 1.6

public abstract class

HttpServer

extends

Object

This class implements a simple HTTP server. A HttpServer is bound to an IP address
and port number and listens for incoming TCP connections from clients on this address.
The sub-class

HttpsServer

implements a server which handles HTTPS requests.

One or more

HttpHandler

objects must be associated with a server
in order to process requests. Each such HttpHandler is registered
with a root URI path which represents the
location of the application or service on this server. The mapping of a handler
to a HttpServer is encapsulated by a

HttpContext

object. HttpContexts
are created by calling

createContext(String,HttpHandler)

.
Any request for which no handler can be found is rejected with a 404 response.
Management of threads can be done external to this object by providing a

Executor

object. If none is provided a default
implementation is used.

Mapping request URIs to HttpContext paths

When a HTTP request is received,
the appropriate HttpContext (and handler) is located by finding the context
whose path is the longest matching prefix of the request URI's path.
Paths are matched literally, which means that the strings are compared
case sensitively, and with no conversion to or from any encoded forms.
For example. Given a HttpServer with the following HttpContexts configured.

description

Context

Context path

ctx1

"/"

ctx2

"/apps/"

ctx3

"/apps/foo/"

the following table shows some request URIs and which, if any context they would
match with.

description

Request URI

Matches context

"http://foo.com/apps/foo/bar"

ctx3

"http://foo.com/apps/Foo/bar"

no match, wrong case

"http://foo.com/apps/app1"

ctx2

"http://foo.com/foo"

ctx1

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

One or more

HttpHandler

objects must be associated with a server
in order to process requests. Each such HttpHandler is registered
with a root URI path which represents the
location of the application or service on this server. The mapping of a handler
to a HttpServer is encapsulated by a

HttpContext

object. HttpContexts
are created by calling

createContext(String,HttpHandler)

.
Any request for which no handler can be found is rejected with a 404 response.
Management of threads can be done external to this object by providing a

Executor

object. If none is provided a default
implementation is used.

Mapping request URIs to HttpContext paths

When a HTTP request is received,
the appropriate HttpContext (and handler) is located by finding the context
whose path is the longest matching prefix of the request URI's path.
Paths are matched literally, which means that the strings are compared
case sensitively, and with no conversion to or from any encoded forms.
For example. Given a HttpServer with the following HttpContexts configured.

description

Context

Context path

ctx1

"/"

ctx2

"/apps/"

ctx3

"/apps/foo/"

the following table shows some request URIs and which, if any context they would
match with.

description

Request URI

Matches context

"http://foo.com/apps/foo/bar"

ctx3

"http://foo.com/apps/Foo/bar"

no match, wrong case

"http://foo.com/apps/app1"

ctx2

"http://foo.com/foo"

ctx1

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

Mapping request URIs to HttpContext paths

When a HTTP request is received,
the appropriate HttpContext (and handler) is located by finding the context
whose path is the longest matching prefix of the request URI's path.
Paths are matched literally, which means that the strings are compared
case sensitively, and with no conversion to or from any encoded forms.
For example. Given a HttpServer with the following HttpContexts configured.

description

Context

Context path

ctx1

"/"

ctx2

"/apps/"

ctx3

"/apps/foo/"

the following table shows some request URIs and which, if any context they would
match with.

description

Request URI

Matches context

"http://foo.com/apps/foo/bar"

ctx3

"http://foo.com/apps/Foo/bar"

no match, wrong case

"http://foo.com/apps/app1"

ctx2

"http://foo.com/foo"

ctx1

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

When a HTTP request is received,
the appropriate HttpContext (and handler) is located by finding the context
whose path is the longest matching prefix of the request URI's path.
Paths are matched literally, which means that the strings are compared
case sensitively, and with no conversion to or from any encoded forms.
For example. Given a HttpServer with the following HttpContexts configured.

description

Context

Context path

ctx1

"/"

ctx2

"/apps/"

ctx3

"/apps/foo/"

the following table shows some request URIs and which, if any context they would
match with.

description

Request URI

Matches context

"http://foo.com/apps/foo/bar"

ctx3

"http://foo.com/apps/Foo/bar"

no match, wrong case

"http://foo.com/apps/app1"

ctx2

"http://foo.com/foo"

ctx1

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

the following table shows some request URIs and which, if any context they would
match with.

description

Request URI

Matches context

"http://foo.com/apps/foo/bar"

ctx3

"http://foo.com/apps/Foo/bar"

no match, wrong case

"http://foo.com/apps/app1"

ctx2

"http://foo.com/foo"

ctx1

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

Note about socket backlogs

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

When binding to an address and port number, the application can also specify an integer

backlog

parameter. This represents the maximum number of incoming TCP connections
which the system will queue internally. Connections are queued while they are waiting to
be accepted by the HttpServer. When the limit is reached, further connections may be
rejected (or possibly ignored) by the underlying TCP implementation. Setting the right
backlog value is a compromise between efficient resource usage in the TCP layer (not setting
it too high) and allowing adequate throughput of incoming requests (not setting it too low).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpServer

()

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

abstract void

bind

​(

InetSocketAddress

addr,
int backlog)

Binds a currently unbound HttpServer to the given address and port number.

static

HttpServer

create

()

creates a HttpServer instance which is initially not bound to any local address/port.

static

HttpServer

create

​(

InetSocketAddress

addr,
int backlog)

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified.

abstract

HttpContext

createContext

​(

String

path)

Creates a HttpContext without initially specifying a handler.

abstract

HttpContext

createContext

​(

String

path,

HttpHandler

handler)

Creates a HttpContext.

abstract

InetSocketAddress

getAddress

()

returns the address this server is listening on

abstract

Executor

getExecutor

()

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

abstract void

removeContext

​(

HttpContext

context)

Removes the given context from the server.

abstract void

removeContext

​(

String

path)

Removes the context identified by the given path from the server.

abstract void

setExecutor

​(

Executor

executor)

sets this server's

Executor

object.

abstract void

start

()

Starts this server in a new background thread.

abstract void

stop

​(int delay)

stops this server by closing the listening socket and disallowing
any new exchanges from being processed.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpServer

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

bind

​(

InetSocketAddress

addr,
int backlog)

Binds a currently unbound HttpServer to the given address and port number.

static

HttpServer

create

()

creates a HttpServer instance which is initially not bound to any local address/port.

static

HttpServer

create

​(

InetSocketAddress

addr,
int backlog)

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified.

abstract

HttpContext

createContext

​(

String

path)

Creates a HttpContext without initially specifying a handler.

abstract

HttpContext

createContext

​(

String

path,

HttpHandler

handler)

Creates a HttpContext.

abstract

InetSocketAddress

getAddress

()

returns the address this server is listening on

abstract

Executor

getExecutor

()

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

abstract void

removeContext

​(

HttpContext

context)

Removes the given context from the server.

abstract void

removeContext

​(

String

path)

Removes the context identified by the given path from the server.

abstract void

setExecutor

​(

Executor

executor)

sets this server's

Executor

object.

abstract void

start

()

Starts this server in a new background thread.

abstract void

stop

​(int delay)

stops this server by closing the listening socket and disallowing
any new exchanges from being processed.

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

Binds a currently unbound HttpServer to the given address and port number.

creates a HttpServer instance which is initially not bound to any local address/port.

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified.

Creates a HttpContext without initially specifying a handler.

Creates a HttpContext.

returns the address this server is listening on

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

Removes the given context from the server.

Removes the context identified by the given path from the server.

sets this server's

Executor

object.

Starts this server in a new background thread.

stops this server by closing the listening socket and disallowing
any new exchanges from being processed.

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

- HttpServer

```java
protected HttpServer()
```

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public static
HttpServer
create()
throws
IOException
```

creates a HttpServer instance which is initially not bound to any local address/port.
The HttpServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

bind(InetSocketAddress,int)

before it can be used.

**Throws:** IOException

- create

```java
public static
HttpServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpServer is acquired from the currently installed

HttpServerProvider

**Parameters:** addr

- the address to listen on, if

null

then bind() must be called
to set the address
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
**Throws:** IOException

- bind

```java
public abstract void bind​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Binds a currently unbound HttpServer to the given address and port number.
A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.

**Parameters:** addr

- the address to listen on
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address or if the server
is already bound.
**Throws:** NullPointerException

- if addr is

null
**Throws:** IOException

- start

```java
public abstract void start()
```

Starts this server in a new background thread. The background thread
inherits the priority, thread group and context class loader
of the caller.

- setExecutor

```java
public abstract void setExecutor​(
Executor
executor)
```

sets this server's

Executor

object. An
Executor must be established before

start()

is called.
All HTTP requests are handled in tasks given to the executor.
If this method is not called (before start()) or if it is
called with a

null

Executor, then
a default implementation is used, which uses the thread
which was created by the

start()

method.

**Parameters:** executor

- the Executor to set, or

null

for default
implementation
**Throws:** IllegalStateException

- if the server is already started

- getExecutor

```java
public abstract
Executor
getExecutor()
```

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

**Returns:** the Executor established for this server or

null

if not set.

- stop

```java
public abstract void stop​(int delay)
```

stops this server by closing the listening socket and disallowing
any new exchanges from being processed. The method will then block
until all current exchange handlers have completed or else when
approximately

delay

seconds have elapsed (whichever happens
sooner). Then, all open TCP connections are closed, the background
thread created by start() exits, and the method returns.
Once stopped, a HttpServer cannot be re-used.

**Parameters:** delay

- the maximum time in seconds to wait until exchanges have finished.
**Throws:** IllegalArgumentException

- if delay is less than zero.

- createContext

```java
public abstract
HttpContext
createContext​(
String
path,

HttpHandler
handler)
```

Creates a HttpContext. A HttpContext represents a mapping from a
URI path to a exchange handler on this HttpServer. Once created, all requests
received by the server for the path will be handled by calling
the given handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:** path

- the root URI path to associate the context with
**Parameters:** handler

- the handler to invoke for incoming requests.
**Throws:** IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
**Throws:** NullPointerException

- if either path, or handler are

null

- createContext

```java
public abstract
HttpContext
createContext​(
String
path)
```

Creates a HttpContext without initially specifying a handler. The handler must later be specified using

HttpContext.setHandler(HttpHandler)

. A HttpContext represents a mapping from a
URI path to an exchange handler on this HttpServer. Once created, and when
the handler has been set, all requests
received by the server for the path will be handled by calling
the handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:** path

- the root URI path to associate the context with
**Throws:** IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
**Throws:** NullPointerException

- if path is

null

- removeContext

```java
public abstract void removeContext​(
String
path)
throws
IllegalArgumentException
```

Removes the context identified by the given path from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:** path

- the path of the handler to remove
**Throws:** IllegalArgumentException

- if no handler corresponding to this
path exists.
**Throws:** NullPointerException

- if path is

null

- removeContext

```java
public abstract void removeContext​(
HttpContext
context)
```

Removes the given context from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:** context

- the context to remove
**Throws:** NullPointerException

- if context is

null

- getAddress

```java
public abstract
InetSocketAddress
getAddress()
```

returns the address this server is listening on

**Returns:** the address/port number the server is listening on

Constructor Detail

- HttpServer

```java
protected HttpServer()
```

---

#### Constructor Detail

HttpServer

```java
protected HttpServer()
```

---

#### HttpServer

protected HttpServer()

Method Detail

- create

```java
public static
HttpServer
create()
throws
IOException
```

creates a HttpServer instance which is initially not bound to any local address/port.
The HttpServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

bind(InetSocketAddress,int)

before it can be used.

**Throws:** IOException

- create

```java
public static
HttpServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpServer is acquired from the currently installed

HttpServerProvider

**Parameters:** addr

- the address to listen on, if

null

then bind() must be called
to set the address
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
**Throws:** IOException

- bind

```java
public abstract void bind​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Binds a currently unbound HttpServer to the given address and port number.
A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.

**Parameters:** addr

- the address to listen on
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address or if the server
is already bound.
**Throws:** NullPointerException

- if addr is

null
**Throws:** IOException

- start

```java
public abstract void start()
```

Starts this server in a new background thread. The background thread
inherits the priority, thread group and context class loader
of the caller.

- setExecutor

```java
public abstract void setExecutor​(
Executor
executor)
```

sets this server's

Executor

object. An
Executor must be established before

start()

is called.
All HTTP requests are handled in tasks given to the executor.
If this method is not called (before start()) or if it is
called with a

null

Executor, then
a default implementation is used, which uses the thread
which was created by the

start()

method.

**Parameters:** executor

- the Executor to set, or

null

for default
implementation
**Throws:** IllegalStateException

- if the server is already started

- getExecutor

```java
public abstract
Executor
getExecutor()
```

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

**Returns:** the Executor established for this server or

null

if not set.

- stop

```java
public abstract void stop​(int delay)
```

stops this server by closing the listening socket and disallowing
any new exchanges from being processed. The method will then block
until all current exchange handlers have completed or else when
approximately

delay

seconds have elapsed (whichever happens
sooner). Then, all open TCP connections are closed, the background
thread created by start() exits, and the method returns.
Once stopped, a HttpServer cannot be re-used.

**Parameters:** delay

- the maximum time in seconds to wait until exchanges have finished.
**Throws:** IllegalArgumentException

- if delay is less than zero.

- createContext

```java
public abstract
HttpContext
createContext​(
String
path,

HttpHandler
handler)
```

Creates a HttpContext. A HttpContext represents a mapping from a
URI path to a exchange handler on this HttpServer. Once created, all requests
received by the server for the path will be handled by calling
the given handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:** path

- the root URI path to associate the context with
**Parameters:** handler

- the handler to invoke for incoming requests.
**Throws:** IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
**Throws:** NullPointerException

- if either path, or handler are

null

- createContext

```java
public abstract
HttpContext
createContext​(
String
path)
```

Creates a HttpContext without initially specifying a handler. The handler must later be specified using

HttpContext.setHandler(HttpHandler)

. A HttpContext represents a mapping from a
URI path to an exchange handler on this HttpServer. Once created, and when
the handler has been set, all requests
received by the server for the path will be handled by calling
the handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:** path

- the root URI path to associate the context with
**Throws:** IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
**Throws:** NullPointerException

- if path is

null

- removeContext

```java
public abstract void removeContext​(
String
path)
throws
IllegalArgumentException
```

Removes the context identified by the given path from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:** path

- the path of the handler to remove
**Throws:** IllegalArgumentException

- if no handler corresponding to this
path exists.
**Throws:** NullPointerException

- if path is

null

- removeContext

```java
public abstract void removeContext​(
HttpContext
context)
```

Removes the given context from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:** context

- the context to remove
**Throws:** NullPointerException

- if context is

null

- getAddress

```java
public abstract
InetSocketAddress
getAddress()
```

returns the address this server is listening on

**Returns:** the address/port number the server is listening on

---

#### Method Detail

create

```java
public static
HttpServer
create()
throws
IOException
```

creates a HttpServer instance which is initially not bound to any local address/port.
The HttpServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

bind(InetSocketAddress,int)

before it can be used.

**Throws:** IOException

---

#### create

public static

HttpServer

create()
throws

IOException

creates a HttpServer instance which is initially not bound to any local address/port.
The HttpServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

bind(InetSocketAddress,int)

before it can be used.

create

```java
public static
HttpServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpServer is acquired from the currently installed

HttpServerProvider

**Parameters:** addr

- the address to listen on, if

null

then bind() must be called
to set the address
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
**Throws:** IOException

---

#### create

public static

HttpServer

create​(

InetSocketAddress

addr,
int backlog)
throws

IOException

Create a

HttpServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpServer is acquired from the currently installed

HttpServerProvider

bind

```java
public abstract void bind​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Binds a currently unbound HttpServer to the given address and port number.
A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.

**Parameters:** addr

- the address to listen on
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address or if the server
is already bound.
**Throws:** NullPointerException

- if addr is

null
**Throws:** IOException

---

#### bind

public abstract void bind​(

InetSocketAddress

addr,
int backlog)
throws

IOException

Binds a currently unbound HttpServer to the given address and port number.
A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.

start

```java
public abstract void start()
```

Starts this server in a new background thread. The background thread
inherits the priority, thread group and context class loader
of the caller.

---

#### start

public abstract void start()

Starts this server in a new background thread. The background thread
inherits the priority, thread group and context class loader
of the caller.

setExecutor

```java
public abstract void setExecutor​(
Executor
executor)
```

sets this server's

Executor

object. An
Executor must be established before

start()

is called.
All HTTP requests are handled in tasks given to the executor.
If this method is not called (before start()) or if it is
called with a

null

Executor, then
a default implementation is used, which uses the thread
which was created by the

start()

method.

**Parameters:** executor

- the Executor to set, or

null

for default
implementation
**Throws:** IllegalStateException

- if the server is already started

---

#### setExecutor

public abstract void setExecutor​(

Executor

executor)

sets this server's

Executor

object. An
Executor must be established before

start()

is called.
All HTTP requests are handled in tasks given to the executor.
If this method is not called (before start()) or if it is
called with a

null

Executor, then
a default implementation is used, which uses the thread
which was created by the

start()

method.

getExecutor

```java
public abstract
Executor
getExecutor()
```

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

**Returns:** the Executor established for this server or

null

if not set.

---

#### getExecutor

public abstract

Executor

getExecutor()

returns this server's Executor object if one was specified with

setExecutor(Executor)

, or

null

if none was
specified.

stop

```java
public abstract void stop​(int delay)
```

stops this server by closing the listening socket and disallowing
any new exchanges from being processed. The method will then block
until all current exchange handlers have completed or else when
approximately

delay

seconds have elapsed (whichever happens
sooner). Then, all open TCP connections are closed, the background
thread created by start() exits, and the method returns.
Once stopped, a HttpServer cannot be re-used.

**Parameters:** delay

- the maximum time in seconds to wait until exchanges have finished.
**Throws:** IllegalArgumentException

- if delay is less than zero.

---

#### stop

public abstract void stop​(int delay)

stops this server by closing the listening socket and disallowing
any new exchanges from being processed. The method will then block
until all current exchange handlers have completed or else when
approximately

delay

seconds have elapsed (whichever happens
sooner). Then, all open TCP connections are closed, the background
thread created by start() exits, and the method returns.
Once stopped, a HttpServer cannot be re-used.

createContext

```java
public abstract
HttpContext
createContext​(
String
path,

HttpHandler
handler)
```

Creates a HttpContext. A HttpContext represents a mapping from a
URI path to a exchange handler on this HttpServer. Once created, all requests
received by the server for the path will be handled by calling
the given handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:** path

- the root URI path to associate the context with
**Parameters:** handler

- the handler to invoke for incoming requests.
**Throws:** IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
**Throws:** NullPointerException

- if either path, or handler are

null

---

#### createContext

public abstract

HttpContext

createContext​(

String

path,

HttpHandler

handler)

Creates a HttpContext. A HttpContext represents a mapping from a
URI path to a exchange handler on this HttpServer. Once created, all requests
received by the server for the path will be handled by calling
the given handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

createContext

```java
public abstract
HttpContext
createContext​(
String
path)
```

Creates a HttpContext without initially specifying a handler. The handler must later be specified using

HttpContext.setHandler(HttpHandler)

. A HttpContext represents a mapping from a
URI path to an exchange handler on this HttpServer. Once created, and when
the handler has been set, all requests
received by the server for the path will be handled by calling
the handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

**Parameters:** path

- the root URI path to associate the context with
**Throws:** IllegalArgumentException

- if path is invalid, or if a context
already exists for this path
**Throws:** NullPointerException

- if path is

null

---

#### createContext

public abstract

HttpContext

createContext​(

String

path)

Creates a HttpContext without initially specifying a handler. The handler must later be specified using

HttpContext.setHandler(HttpHandler)

. A HttpContext represents a mapping from a
URI path to an exchange handler on this HttpServer. Once created, and when
the handler has been set, all requests
received by the server for the path will be handled by calling
the handler object. The context is identified by the path, and
can later be removed from the server using this with the

removeContext(String)

method.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

The path specifies the root URI path for this context. The first character of path must be
'/'.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

The class overview describes how incoming request URIs are

mapped

to HttpContext instances.

removeContext

```java
public abstract void removeContext​(
String
path)
throws
IllegalArgumentException
```

Removes the context identified by the given path from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:** path

- the path of the handler to remove
**Throws:** IllegalArgumentException

- if no handler corresponding to this
path exists.
**Throws:** NullPointerException

- if path is

null

---

#### removeContext

public abstract void removeContext​(

String

path)
throws

IllegalArgumentException

Removes the context identified by the given path from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

removeContext

```java
public abstract void removeContext​(
HttpContext
context)
```

Removes the given context from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

**Parameters:** context

- the context to remove
**Throws:** NullPointerException

- if context is

null

---

#### removeContext

public abstract void removeContext​(

HttpContext

context)

Removes the given context from the server.
Removing a context does not affect exchanges currently being processed
but prevents new ones from being accepted.

getAddress

```java
public abstract
InetSocketAddress
getAddress()
```

returns the address this server is listening on

**Returns:** the address/port number the server is listening on

---

#### getAddress

public abstract

InetSocketAddress

getAddress()

returns the address this server is listening on

---

