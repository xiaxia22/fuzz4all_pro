# Interface HttpResponse.ResponseInfo

**Source:** `java.net.http\java\net\http\HttpResponse.ResponseInfo.html`

### Class Description

```java
public static interface
HttpResponse.ResponseInfo
```

Initial response information supplied to a

BodyHandler

when a response is initially received and before the body is processed.

**Enclosing interface:** HttpResponse

<

T

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int statusCode()

Provides the response status code.

**Returns:**
- the response status code

---

#### HttpHeaders
headers()

Provides the response headers.

**Returns:**
- the response headers

---

#### HttpClient.Version
version()

Provides the response protocol version.

**Returns:**
- the response protocol version

---

### Additional Sections

#### Interface HttpResponse.ResponseInfo

**Enclosing interface:** HttpResponse

<

T

>

```java
public static interface
HttpResponse.ResponseInfo
```

Initial response information supplied to a

BodyHandler

when a response is initially received and before the body is processed.

public static interface

HttpResponse.ResponseInfo

Initial response information supplied to a

BodyHandler

when a response is initially received and before the body is processed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpHeaders

headers

()

Provides the response headers.

int

statusCode

()

Provides the response status code.

HttpClient.Version

version

()

Provides the response protocol version.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HttpHeaders

headers

()

Provides the response headers.

int

statusCode

()

Provides the response status code.

HttpClient.Version

version

()

Provides the response protocol version.

---

#### Method Summary

Provides the response headers.

Provides the response status code.

Provides the response protocol version.

============ METHOD DETAIL ==========

- Method Detail

- statusCode

```java
int statusCode()
```

Provides the response status code.

**Returns:** the response status code

- headers

```java
HttpHeaders
headers()
```

Provides the response headers.

**Returns:** the response headers

- version

```java
HttpClient.Version
version()
```

Provides the response protocol version.

**Returns:** the response protocol version

Method Detail

- statusCode

```java
int statusCode()
```

Provides the response status code.

**Returns:** the response status code

- headers

```java
HttpHeaders
headers()
```

Provides the response headers.

**Returns:** the response headers

- version

```java
HttpClient.Version
version()
```

Provides the response protocol version.

**Returns:** the response protocol version

---

#### Method Detail

statusCode

```java
int statusCode()
```

Provides the response status code.

**Returns:** the response status code

---

#### statusCode

int statusCode()

Provides the response status code.

headers

```java
HttpHeaders
headers()
```

Provides the response headers.

**Returns:** the response headers

---

#### headers

HttpHeaders

headers()

Provides the response headers.

version

```java
HttpClient.Version
version()
```

Provides the response protocol version.

**Returns:** the response protocol version

---

#### version

HttpClient.Version

version()

Provides the response protocol version.

---

