# Class HttpsExchange

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpsExchange.html`

### Class Description

```java
public abstract class
HttpsExchange

extends
HttpExchange
```

This class encapsulates a HTTPS request received and a
response to be generated in one exchange and defines
the extensions to HttpExchange that are specific to the HTTPS protocol.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpsExchange()

*No description found.*

---

### Method Details

#### public abstract
SSLSession
getSSLSession()

Get the SSLSession for this exchange.

**Returns:**
- the SSLSession

---

### Additional Sections

#### Class HttpsExchange

java.lang.Object

- com.sun.net.httpserver.HttpExchange
- - com.sun.net.httpserver.HttpsExchange

com.sun.net.httpserver.HttpExchange

- com.sun.net.httpserver.HttpsExchange

com.sun.net.httpserver.HttpsExchange

```java
public abstract class
HttpsExchange

extends
HttpExchange
```

This class encapsulates a HTTPS request received and a
response to be generated in one exchange and defines
the extensions to HttpExchange that are specific to the HTTPS protocol.

**Since:** 1.6

public abstract class

HttpsExchange

extends

HttpExchange

This class encapsulates a HTTPS request received and a
response to be generated in one exchange and defines
the extensions to HttpExchange that are specific to the HTTPS protocol.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpsExchange

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

SSLSession

getSSLSession

()

Get the SSLSession for this exchange.

- Methods declared in class com.sun.net.httpserver.

HttpExchange

close

,

getAttribute

,

getHttpContext

,

getLocalAddress

,

getPrincipal

,

getProtocol

,

getRemoteAddress

,

getRequestBody

,

getRequestHeaders

,

getRequestMethod

,

getRequestURI

,

getResponseBody

,

getResponseCode

,

getResponseHeaders

,

sendResponseHeaders

,

setAttribute

,

setStreams

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

HttpsExchange

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

SSLSession

getSSLSession

()

Get the SSLSession for this exchange.

- Methods declared in class com.sun.net.httpserver.

HttpExchange

close

,

getAttribute

,

getHttpContext

,

getLocalAddress

,

getPrincipal

,

getProtocol

,

getRemoteAddress

,

getRequestBody

,

getRequestHeaders

,

getRequestMethod

,

getRequestURI

,

getResponseBody

,

getResponseCode

,

getResponseHeaders

,

sendResponseHeaders

,

setAttribute

,

setStreams

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

Get the SSLSession for this exchange.

Methods declared in class com.sun.net.httpserver.

HttpExchange

close

,

getAttribute

,

getHttpContext

,

getLocalAddress

,

getPrincipal

,

getProtocol

,

getRemoteAddress

,

getRequestBody

,

getRequestHeaders

,

getRequestMethod

,

getRequestURI

,

getResponseBody

,

getResponseCode

,

getResponseHeaders

,

sendResponseHeaders

,

setAttribute

,

setStreams

---

#### Methods declared in class com.sun.net.httpserver. HttpExchange

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

- HttpsExchange

```java
protected HttpsExchange()
```

============ METHOD DETAIL ==========

- Method Detail

- getSSLSession

```java
public abstract
SSLSession
getSSLSession()
```

Get the SSLSession for this exchange.

**Returns:** the SSLSession

Constructor Detail

- HttpsExchange

```java
protected HttpsExchange()
```

---

#### Constructor Detail

HttpsExchange

```java
protected HttpsExchange()
```

---

#### HttpsExchange

protected HttpsExchange()

Method Detail

- getSSLSession

```java
public abstract
SSLSession
getSSLSession()
```

Get the SSLSession for this exchange.

**Returns:** the SSLSession

---

#### Method Detail

getSSLSession

```java
public abstract
SSLSession
getSSLSession()
```

Get the SSLSession for this exchange.

**Returns:** the SSLSession

---

#### getSSLSession

public abstract

SSLSession

getSSLSession()

Get the SSLSession for this exchange.

---

