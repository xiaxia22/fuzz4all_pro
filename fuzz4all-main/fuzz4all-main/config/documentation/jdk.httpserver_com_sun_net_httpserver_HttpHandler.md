# Interface HttpHandler

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpHandler.html`

### Class Description

```java
public interface
HttpHandler
```

A handler which is invoked to process HTTP exchanges. Each
HTTP exchange is handled by one of these handlers.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void handle​(
HttpExchange
exchange)
throws
IOException

Handle the given request and generate an appropriate response.
See

HttpExchange

for a description of the steps
involved in handling an exchange.

**Parameters:**
- exchange

- the exchange containing the request from the
client and used to send the response

**Throws:**
- NullPointerException

- if exchange is

null
- IOException

---

### Additional Sections

#### Interface HttpHandler

```java
public interface
HttpHandler
```

A handler which is invoked to process HTTP exchanges. Each
HTTP exchange is handled by one of these handlers.

**Since:** 1.6

public interface

HttpHandler

A handler which is invoked to process HTTP exchanges. Each
HTTP exchange is handled by one of these handlers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handle

​(

HttpExchange

exchange)

Handle the given request and generate an appropriate response.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handle

​(

HttpExchange

exchange)

Handle the given request and generate an appropriate response.

---

#### Method Summary

Handle the given request and generate an appropriate response.

============ METHOD DETAIL ==========

- Method Detail

- handle

```java
void handle​(
HttpExchange
exchange)
throws
IOException
```

Handle the given request and generate an appropriate response.
See

HttpExchange

for a description of the steps
involved in handling an exchange.

**Parameters:** exchange

- the exchange containing the request from the
client and used to send the response
**Throws:** NullPointerException

- if exchange is

null
**Throws:** IOException

Method Detail

- handle

```java
void handle​(
HttpExchange
exchange)
throws
IOException
```

Handle the given request and generate an appropriate response.
See

HttpExchange

for a description of the steps
involved in handling an exchange.

**Parameters:** exchange

- the exchange containing the request from the
client and used to send the response
**Throws:** NullPointerException

- if exchange is

null
**Throws:** IOException

---

#### Method Detail

handle

```java
void handle​(
HttpExchange
exchange)
throws
IOException
```

Handle the given request and generate an appropriate response.
See

HttpExchange

for a description of the steps
involved in handling an exchange.

**Parameters:** exchange

- the exchange containing the request from the
client and used to send the response
**Throws:** NullPointerException

- if exchange is

null
**Throws:** IOException

---

#### handle

void handle​(

HttpExchange

exchange)
throws

IOException

Handle the given request and generate an appropriate response.
See

HttpExchange

for a description of the steps
involved in handling an exchange.

---

