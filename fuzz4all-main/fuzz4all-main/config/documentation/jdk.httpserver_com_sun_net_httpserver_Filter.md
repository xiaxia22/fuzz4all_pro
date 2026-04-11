# Class Filter

**Source:** `jdk.httpserver\com\sun\net\httpserver\Filter.html`

### Class Description

```java
public abstract class
Filter

extends
Object
```

A filter used to pre- and post-process incoming requests. Pre-processing occurs
before the application's exchange handler is invoked, and post-processing
occurs after the exchange handler returns. Filters
are organised in chains, and are associated with HttpContext instances.

Each Filter in the chain, invokes the next filter within its own
doFilter() implementation. The final Filter in the chain invokes the applications
exchange handler.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Filter()

*No description found.*

---

### Method Details

#### public abstract void doFilter​(
HttpExchange
exchange,

Filter.Chain
chain)
throws
IOException

Asks this filter to pre/post-process the given exchange. The filter
can:

- examine or modify the request headers
- filter the request body or the response body, by creating suitable
filter streams and calling

HttpExchange.setStreams(InputStream,OutputStream)
- set attribute Objects in the exchange, which other filters or the
exchange handler can access.
- decide to either

- invoke the next filter in the chain, by calling

Filter.Chain.doFilter(HttpExchange)
- terminate the chain of invocation, by

not

calling

Filter.Chain.doFilter(HttpExchange)

if option 1. above taken, then when doFilter() returns all subsequent
filters in the Chain have been called, and the response headers can be
examined or modified.

if option 2. above taken, then this Filter must use the HttpExchange
to send back an appropriate response

**Parameters:**
- exchange

- the

HttpExchange

to be filtered.
- chain

- the Chain which allows the next filter to be invoked.

**Throws:**
- IOException

- may be thrown by any filter module, and if
caught, must be rethrown again.
- NullPointerException

- if either exchange or chain are

null

---

#### public abstract
String
description()

returns a short description of this Filter

**Returns:**
- a string describing the Filter

---

### Additional Sections

#### Class Filter

java.lang.Object

- com.sun.net.httpserver.Filter

com.sun.net.httpserver.Filter

```java
public abstract class
Filter

extends
Object
```

A filter used to pre- and post-process incoming requests. Pre-processing occurs
before the application's exchange handler is invoked, and post-processing
occurs after the exchange handler returns. Filters
are organised in chains, and are associated with HttpContext instances.

Each Filter in the chain, invokes the next filter within its own
doFilter() implementation. The final Filter in the chain invokes the applications
exchange handler.

**Since:** 1.6

public abstract class

Filter

extends

Object

A filter used to pre- and post-process incoming requests. Pre-processing occurs
before the application's exchange handler is invoked, and post-processing
occurs after the exchange handler returns. Filters
are organised in chains, and are associated with HttpContext instances.

Each Filter in the chain, invokes the next filter within its own
doFilter() implementation. The final Filter in the chain invokes the applications
exchange handler.

Each Filter in the chain, invokes the next filter within its own
doFilter() implementation. The final Filter in the chain invokes the applications
exchange handler.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Filter.Chain

a chain of filters associated with a HttpServer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Filter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

description

()

returns a short description of this Filter

abstract void

doFilter

​(

HttpExchange

exchange,

Filter.Chain

chain)

Asks this filter to pre/post-process the given exchange.

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

static class

Filter.Chain

a chain of filters associated with a HttpServer.

---

#### Nested Class Summary

a chain of filters associated with a HttpServer.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Filter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

description

()

returns a short description of this Filter

abstract void

doFilter

​(

HttpExchange

exchange,

Filter.Chain

chain)

Asks this filter to pre/post-process the given exchange.

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

returns a short description of this Filter

Asks this filter to pre/post-process the given exchange.

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

- Filter

```java
protected Filter()
```

============ METHOD DETAIL ==========

- Method Detail

- doFilter

```java
public abstract void doFilter​(
HttpExchange
exchange,

Filter.Chain
chain)
throws
IOException
```

Asks this filter to pre/post-process the given exchange. The filter
can:

- examine or modify the request headers
- filter the request body or the response body, by creating suitable
filter streams and calling

HttpExchange.setStreams(InputStream,OutputStream)
- set attribute Objects in the exchange, which other filters or the
exchange handler can access.
- decide to either

- invoke the next filter in the chain, by calling

Filter.Chain.doFilter(HttpExchange)
- terminate the chain of invocation, by

not

calling

Filter.Chain.doFilter(HttpExchange)

if option 1. above taken, then when doFilter() returns all subsequent
filters in the Chain have been called, and the response headers can be
examined or modified.

if option 2. above taken, then this Filter must use the HttpExchange
to send back an appropriate response

**Parameters:** exchange

- the

HttpExchange

to be filtered.
**Parameters:** chain

- the Chain which allows the next filter to be invoked.
**Throws:** IOException

- may be thrown by any filter module, and if
caught, must be rethrown again.
**Throws:** NullPointerException

- if either exchange or chain are

null

- description

```java
public abstract
String
description()
```

returns a short description of this Filter

**Returns:** a string describing the Filter

Constructor Detail

- Filter

```java
protected Filter()
```

---

#### Constructor Detail

Filter

```java
protected Filter()
```

---

#### Filter

protected Filter()

Method Detail

- doFilter

```java
public abstract void doFilter​(
HttpExchange
exchange,

Filter.Chain
chain)
throws
IOException
```

Asks this filter to pre/post-process the given exchange. The filter
can:

- examine or modify the request headers
- filter the request body or the response body, by creating suitable
filter streams and calling

HttpExchange.setStreams(InputStream,OutputStream)
- set attribute Objects in the exchange, which other filters or the
exchange handler can access.
- decide to either

- invoke the next filter in the chain, by calling

Filter.Chain.doFilter(HttpExchange)
- terminate the chain of invocation, by

not

calling

Filter.Chain.doFilter(HttpExchange)

if option 1. above taken, then when doFilter() returns all subsequent
filters in the Chain have been called, and the response headers can be
examined or modified.

if option 2. above taken, then this Filter must use the HttpExchange
to send back an appropriate response

**Parameters:** exchange

- the

HttpExchange

to be filtered.
**Parameters:** chain

- the Chain which allows the next filter to be invoked.
**Throws:** IOException

- may be thrown by any filter module, and if
caught, must be rethrown again.
**Throws:** NullPointerException

- if either exchange or chain are

null

- description

```java
public abstract
String
description()
```

returns a short description of this Filter

**Returns:** a string describing the Filter

---

#### Method Detail

doFilter

```java
public abstract void doFilter​(
HttpExchange
exchange,

Filter.Chain
chain)
throws
IOException
```

Asks this filter to pre/post-process the given exchange. The filter
can:

- examine or modify the request headers
- filter the request body or the response body, by creating suitable
filter streams and calling

HttpExchange.setStreams(InputStream,OutputStream)
- set attribute Objects in the exchange, which other filters or the
exchange handler can access.
- decide to either

- invoke the next filter in the chain, by calling

Filter.Chain.doFilter(HttpExchange)
- terminate the chain of invocation, by

not

calling

Filter.Chain.doFilter(HttpExchange)

if option 1. above taken, then when doFilter() returns all subsequent
filters in the Chain have been called, and the response headers can be
examined or modified.

if option 2. above taken, then this Filter must use the HttpExchange
to send back an appropriate response

**Parameters:** exchange

- the

HttpExchange

to be filtered.
**Parameters:** chain

- the Chain which allows the next filter to be invoked.
**Throws:** IOException

- may be thrown by any filter module, and if
caught, must be rethrown again.
**Throws:** NullPointerException

- if either exchange or chain are

null

---

#### doFilter

public abstract void doFilter​(

HttpExchange

exchange,

Filter.Chain

chain)
throws

IOException

Asks this filter to pre/post-process the given exchange. The filter
can:

- examine or modify the request headers
- filter the request body or the response body, by creating suitable
filter streams and calling

HttpExchange.setStreams(InputStream,OutputStream)
- set attribute Objects in the exchange, which other filters or the
exchange handler can access.
- decide to either

- invoke the next filter in the chain, by calling

Filter.Chain.doFilter(HttpExchange)
- terminate the chain of invocation, by

not

calling

Filter.Chain.doFilter(HttpExchange)

if option 1. above taken, then when doFilter() returns all subsequent
filters in the Chain have been called, and the response headers can be
examined or modified.

if option 2. above taken, then this Filter must use the HttpExchange
to send back an appropriate response

examine or modify the request headers

filter the request body or the response body, by creating suitable
filter streams and calling

HttpExchange.setStreams(InputStream,OutputStream)

set attribute Objects in the exchange, which other filters or the
exchange handler can access.

decide to either

- invoke the next filter in the chain, by calling

Filter.Chain.doFilter(HttpExchange)
- terminate the chain of invocation, by

not

calling

Filter.Chain.doFilter(HttpExchange)

if option 1. above taken, then when doFilter() returns all subsequent
filters in the Chain have been called, and the response headers can be
examined or modified.

if option 2. above taken, then this Filter must use the HttpExchange
to send back an appropriate response

invoke the next filter in the chain, by calling

Filter.Chain.doFilter(HttpExchange)

terminate the chain of invocation, by

not

calling

Filter.Chain.doFilter(HttpExchange)

description

```java
public abstract
String
description()
```

returns a short description of this Filter

**Returns:** a string describing the Filter

---

#### description

public abstract

String

description()

returns a short description of this Filter

---

