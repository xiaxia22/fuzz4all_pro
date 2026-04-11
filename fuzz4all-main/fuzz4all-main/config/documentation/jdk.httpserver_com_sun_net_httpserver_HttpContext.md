# Class HttpContext

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpContext.html`

### Class Description

```java
public abstract class
HttpContext

extends
Object
```

HttpContext represents a mapping between the root URI path of an application
to a

HttpHandler

which is invoked to handle requests destined
for that path on the associated HttpServer or HttpsServer.

HttpContext instances are created by the create methods in HttpServer
and HttpsServer

A chain of

Filter

objects can be added to a HttpContext. All exchanges processed by the
context can be pre- and post-processed by each Filter in the chain.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpContext()

*No description found.*

---

### Method Details

#### public abstract
HttpHandler
getHandler()

returns the handler for this context

**Returns:**
- the HttpHandler for this context

---

#### public abstract void setHandler​(
HttpHandler
h)

Sets the handler for this context, if not already set.

**Parameters:**
- h

- the handler to set for this context

**Throws:**
- IllegalArgumentException

- if this context's handler is already set.
- NullPointerException

- if handler is

null

---

#### public abstract
String
getPath()

returns the path this context was created with

**Returns:**
- this context's path

---

#### public abstract
HttpServer
getServer()

returns the server this context was created with

**Returns:**
- this context's server

---

#### public abstract
Map
<
String
,​
Object
> getAttributes()

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

Every attribute stored in this Map will be visible to
every HttpExchange processed by this context

---

#### public abstract
List
<
Filter
> getFilters()

returns this context's list of Filters. This is the
actual list used by the server when dispatching requests
so modifications to this list immediately affect the
the handling of exchanges.

---

#### public abstract
Authenticator
setAuthenticator​(
Authenticator
auth)

Sets the Authenticator for this HttpContext. Once an authenticator
is establised on a context, all client requests must be
authenticated, and the given object will be invoked to validate each
request. Each call to this method replaces any previous value set.

**Parameters:**
- auth

- the authenticator to set. If

null

then any
previously set authenticator is removed,
and client authentication will no longer be required.

**Returns:**
- the previous Authenticator, if any set, or

null

otherwise.

---

#### public abstract
Authenticator
getAuthenticator()

Returns the currently set Authenticator for this context
if one exists.

**Returns:**
- this HttpContext's Authenticator, or

null

if none is set.

---

### Additional Sections

#### Class HttpContext

java.lang.Object

- com.sun.net.httpserver.HttpContext

com.sun.net.httpserver.HttpContext

```java
public abstract class
HttpContext

extends
Object
```

HttpContext represents a mapping between the root URI path of an application
to a

HttpHandler

which is invoked to handle requests destined
for that path on the associated HttpServer or HttpsServer.

HttpContext instances are created by the create methods in HttpServer
and HttpsServer

A chain of

Filter

objects can be added to a HttpContext. All exchanges processed by the
context can be pre- and post-processed by each Filter in the chain.

**Since:** 1.6

public abstract class

HttpContext

extends

Object

HttpContext represents a mapping between the root URI path of an application
to a

HttpHandler

which is invoked to handle requests destined
for that path on the associated HttpServer or HttpsServer.

HttpContext instances are created by the create methods in HttpServer
and HttpsServer

A chain of

Filter

objects can be added to a HttpContext. All exchanges processed by the
context can be pre- and post-processed by each Filter in the chain.

HttpContext instances are created by the create methods in HttpServer
and HttpsServer

A chain of

Filter

objects can be added to a HttpContext. All exchanges processed by the
context can be pre- and post-processed by each Filter in the chain.

A chain of

Filter

objects can be added to a HttpContext. All exchanges processed by the
context can be pre- and post-processed by each Filter in the chain.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpContext

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

Map

<

String

,​

Object

>

getAttributes

()

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

abstract

Authenticator

getAuthenticator

()

Returns the currently set Authenticator for this context
if one exists.

abstract

List

<

Filter

>

getFilters

()

returns this context's list of Filters.

abstract

HttpHandler

getHandler

()

returns the handler for this context

abstract

String

getPath

()

returns the path this context was created with

abstract

HttpServer

getServer

()

returns the server this context was created with

abstract

Authenticator

setAuthenticator

​(

Authenticator

auth)

Sets the Authenticator for this HttpContext.

abstract void

setHandler

​(

HttpHandler

h)

Sets the handler for this context, if not already set.

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

HttpContext

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

Map

<

String

,​

Object

>

getAttributes

()

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

abstract

Authenticator

getAuthenticator

()

Returns the currently set Authenticator for this context
if one exists.

abstract

List

<

Filter

>

getFilters

()

returns this context's list of Filters.

abstract

HttpHandler

getHandler

()

returns the handler for this context

abstract

String

getPath

()

returns the path this context was created with

abstract

HttpServer

getServer

()

returns the server this context was created with

abstract

Authenticator

setAuthenticator

​(

Authenticator

auth)

Sets the Authenticator for this HttpContext.

abstract void

setHandler

​(

HttpHandler

h)

Sets the handler for this context, if not already set.

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

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

Returns the currently set Authenticator for this context
if one exists.

returns this context's list of Filters.

returns the handler for this context

returns the path this context was created with

returns the server this context was created with

Sets the Authenticator for this HttpContext.

Sets the handler for this context, if not already set.

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

- HttpContext

```java
protected HttpContext()
```

============ METHOD DETAIL ==========

- Method Detail

- getHandler

```java
public abstract
HttpHandler
getHandler()
```

returns the handler for this context

**Returns:** the HttpHandler for this context

- setHandler

```java
public abstract void setHandler​(
HttpHandler
h)
```

Sets the handler for this context, if not already set.

**Parameters:** h

- the handler to set for this context
**Throws:** IllegalArgumentException

- if this context's handler is already set.
**Throws:** NullPointerException

- if handler is

null

- getPath

```java
public abstract
String
getPath()
```

returns the path this context was created with

**Returns:** this context's path

- getServer

```java
public abstract
HttpServer
getServer()
```

returns the server this context was created with

**Returns:** this context's server

- getAttributes

```java
public abstract
Map
<
String
,​
Object
> getAttributes()
```

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

Every attribute stored in this Map will be visible to
every HttpExchange processed by this context

- getFilters

```java
public abstract
List
<
Filter
> getFilters()
```

returns this context's list of Filters. This is the
actual list used by the server when dispatching requests
so modifications to this list immediately affect the
the handling of exchanges.

- setAuthenticator

```java
public abstract
Authenticator
setAuthenticator​(
Authenticator
auth)
```

Sets the Authenticator for this HttpContext. Once an authenticator
is establised on a context, all client requests must be
authenticated, and the given object will be invoked to validate each
request. Each call to this method replaces any previous value set.

**Parameters:** auth

- the authenticator to set. If

null

then any
previously set authenticator is removed,
and client authentication will no longer be required.
**Returns:** the previous Authenticator, if any set, or

null

otherwise.

- getAuthenticator

```java
public abstract
Authenticator
getAuthenticator()
```

Returns the currently set Authenticator for this context
if one exists.

**Returns:** this HttpContext's Authenticator, or

null

if none is set.

Constructor Detail

- HttpContext

```java
protected HttpContext()
```

---

#### Constructor Detail

HttpContext

```java
protected HttpContext()
```

---

#### HttpContext

protected HttpContext()

Method Detail

- getHandler

```java
public abstract
HttpHandler
getHandler()
```

returns the handler for this context

**Returns:** the HttpHandler for this context

- setHandler

```java
public abstract void setHandler​(
HttpHandler
h)
```

Sets the handler for this context, if not already set.

**Parameters:** h

- the handler to set for this context
**Throws:** IllegalArgumentException

- if this context's handler is already set.
**Throws:** NullPointerException

- if handler is

null

- getPath

```java
public abstract
String
getPath()
```

returns the path this context was created with

**Returns:** this context's path

- getServer

```java
public abstract
HttpServer
getServer()
```

returns the server this context was created with

**Returns:** this context's server

- getAttributes

```java
public abstract
Map
<
String
,​
Object
> getAttributes()
```

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

Every attribute stored in this Map will be visible to
every HttpExchange processed by this context

- getFilters

```java
public abstract
List
<
Filter
> getFilters()
```

returns this context's list of Filters. This is the
actual list used by the server when dispatching requests
so modifications to this list immediately affect the
the handling of exchanges.

- setAuthenticator

```java
public abstract
Authenticator
setAuthenticator​(
Authenticator
auth)
```

Sets the Authenticator for this HttpContext. Once an authenticator
is establised on a context, all client requests must be
authenticated, and the given object will be invoked to validate each
request. Each call to this method replaces any previous value set.

**Parameters:** auth

- the authenticator to set. If

null

then any
previously set authenticator is removed,
and client authentication will no longer be required.
**Returns:** the previous Authenticator, if any set, or

null

otherwise.

- getAuthenticator

```java
public abstract
Authenticator
getAuthenticator()
```

Returns the currently set Authenticator for this context
if one exists.

**Returns:** this HttpContext's Authenticator, or

null

if none is set.

---

#### Method Detail

getHandler

```java
public abstract
HttpHandler
getHandler()
```

returns the handler for this context

**Returns:** the HttpHandler for this context

---

#### getHandler

public abstract

HttpHandler

getHandler()

returns the handler for this context

setHandler

```java
public abstract void setHandler​(
HttpHandler
h)
```

Sets the handler for this context, if not already set.

**Parameters:** h

- the handler to set for this context
**Throws:** IllegalArgumentException

- if this context's handler is already set.
**Throws:** NullPointerException

- if handler is

null

---

#### setHandler

public abstract void setHandler​(

HttpHandler

h)

Sets the handler for this context, if not already set.

getPath

```java
public abstract
String
getPath()
```

returns the path this context was created with

**Returns:** this context's path

---

#### getPath

public abstract

String

getPath()

returns the path this context was created with

getServer

```java
public abstract
HttpServer
getServer()
```

returns the server this context was created with

**Returns:** this context's server

---

#### getServer

public abstract

HttpServer

getServer()

returns the server this context was created with

getAttributes

```java
public abstract
Map
<
String
,​
Object
> getAttributes()
```

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

Every attribute stored in this Map will be visible to
every HttpExchange processed by this context

---

#### getAttributes

public abstract

Map

<

String

,​

Object

> getAttributes()

returns a mutable Map, which can be used to pass
configuration and other data to Filter modules
and to the context's exchange handler.

Every attribute stored in this Map will be visible to
every HttpExchange processed by this context

Every attribute stored in this Map will be visible to
every HttpExchange processed by this context

getFilters

```java
public abstract
List
<
Filter
> getFilters()
```

returns this context's list of Filters. This is the
actual list used by the server when dispatching requests
so modifications to this list immediately affect the
the handling of exchanges.

---

#### getFilters

public abstract

List

<

Filter

> getFilters()

returns this context's list of Filters. This is the
actual list used by the server when dispatching requests
so modifications to this list immediately affect the
the handling of exchanges.

setAuthenticator

```java
public abstract
Authenticator
setAuthenticator​(
Authenticator
auth)
```

Sets the Authenticator for this HttpContext. Once an authenticator
is establised on a context, all client requests must be
authenticated, and the given object will be invoked to validate each
request. Each call to this method replaces any previous value set.

**Parameters:** auth

- the authenticator to set. If

null

then any
previously set authenticator is removed,
and client authentication will no longer be required.
**Returns:** the previous Authenticator, if any set, or

null

otherwise.

---

#### setAuthenticator

public abstract

Authenticator

setAuthenticator​(

Authenticator

auth)

Sets the Authenticator for this HttpContext. Once an authenticator
is establised on a context, all client requests must be
authenticated, and the given object will be invoked to validate each
request. Each call to this method replaces any previous value set.

getAuthenticator

```java
public abstract
Authenticator
getAuthenticator()
```

Returns the currently set Authenticator for this context
if one exists.

**Returns:** this HttpContext's Authenticator, or

null

if none is set.

---

#### getAuthenticator

public abstract

Authenticator

getAuthenticator()

Returns the currently set Authenticator for this context
if one exists.

---

