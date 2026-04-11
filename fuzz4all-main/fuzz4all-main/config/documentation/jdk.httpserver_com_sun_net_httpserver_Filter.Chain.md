# Class Filter.Chain

**Source:** `jdk.httpserver\com\sun\net\httpserver\Filter.Chain.html`

### Class Description

```java
public static class
Filter.Chain

extends
Object
```

a chain of filters associated with a HttpServer.
Each filter in the chain is given one of these
so it can invoke the next filter in the chain

**Enclosing class:** Filter

---

### Field Details

*No entries found.*

### Constructor Details

#### public Chain​(
List
<
Filter
> filters,

HttpHandler
handler)

*No description found.*

---

### Method Details

#### public void doFilter​(
HttpExchange
exchange)
throws
IOException

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain. The Filter may decide
to terminate the chain, by not calling this method.
In this case, the filter

must

send the
response to the request, because the application's
exchange handler will not be invoked.

**Parameters:**
- exchange

- the HttpExchange

**Throws:**
- IOException

- let exceptions pass up the stack
- NullPointerException

- if exchange is

null

---

### Additional Sections

#### Class Filter.Chain

java.lang.Object

- com.sun.net.httpserver.Filter.Chain

com.sun.net.httpserver.Filter.Chain

**Enclosing class:** Filter

```java
public static class
Filter.Chain

extends
Object
```

a chain of filters associated with a HttpServer.
Each filter in the chain is given one of these
so it can invoke the next filter in the chain

public static class

Filter.Chain

extends

Object

a chain of filters associated with a HttpServer.
Each filter in the chain is given one of these
so it can invoke the next filter in the chain

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Chain

​(

List

<

Filter

> filters,

HttpHandler

handler)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

doFilter

​(

HttpExchange

exchange)

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain.

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

Constructor

Description

Chain

​(

List

<

Filter

> filters,

HttpHandler

handler)

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

doFilter

​(

HttpExchange

exchange)

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain.

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

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain.

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

- Chain

```java
public Chain​(
List
<
Filter
> filters,

HttpHandler
handler)
```

============ METHOD DETAIL ==========

- Method Detail

- doFilter

```java
public void doFilter​(
HttpExchange
exchange)
throws
IOException
```

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain. The Filter may decide
to terminate the chain, by not calling this method.
In this case, the filter

must

send the
response to the request, because the application's
exchange handler will not be invoked.

**Parameters:** exchange

- the HttpExchange
**Throws:** IOException

- let exceptions pass up the stack
**Throws:** NullPointerException

- if exchange is

null

Constructor Detail

- Chain

```java
public Chain​(
List
<
Filter
> filters,

HttpHandler
handler)
```

---

#### Constructor Detail

Chain

```java
public Chain​(
List
<
Filter
> filters,

HttpHandler
handler)
```

---

#### Chain

public Chain​(

List

<

Filter

> filters,

HttpHandler

handler)

Method Detail

- doFilter

```java
public void doFilter​(
HttpExchange
exchange)
throws
IOException
```

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain. The Filter may decide
to terminate the chain, by not calling this method.
In this case, the filter

must

send the
response to the request, because the application's
exchange handler will not be invoked.

**Parameters:** exchange

- the HttpExchange
**Throws:** IOException

- let exceptions pass up the stack
**Throws:** NullPointerException

- if exchange is

null

---

#### Method Detail

doFilter

```java
public void doFilter​(
HttpExchange
exchange)
throws
IOException
```

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain. The Filter may decide
to terminate the chain, by not calling this method.
In this case, the filter

must

send the
response to the request, because the application's
exchange handler will not be invoked.

**Parameters:** exchange

- the HttpExchange
**Throws:** IOException

- let exceptions pass up the stack
**Throws:** NullPointerException

- if exchange is

null

---

#### doFilter

public void doFilter​(

HttpExchange

exchange)
throws

IOException

calls the next filter in the chain, or else
the users exchange handler, if this is the
final filter in the chain. The Filter may decide
to terminate the chain, by not calling this method.
In this case, the filter

must

send the
response to the request, because the application's
exchange handler will not be invoked.

---

