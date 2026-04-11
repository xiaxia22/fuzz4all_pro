# Class Authenticator.Retry

**Source:** `jdk.httpserver\com\sun\net\httpserver\Authenticator.Retry.html`

### Class Description

```java
public static class
Authenticator.Retry

extends
Authenticator.Result
```

Indicates an authentication must be retried. The
response code to be sent back is as returned from
getResponseCode(). The Authenticator must also have
set any necessary response headers in the given HttpExchange
before returning this Retry object.

**Enclosing class:** Authenticator

---

### Field Details

*No entries found.*

### Constructor Details

#### public Retry​(int responseCode)

*No description found.*

---

### Method Details

#### public int getResponseCode()

returns the response code to send to the client

---

### Additional Sections

#### Class Authenticator.Retry

java.lang.Object

- com.sun.net.httpserver.Authenticator.Result
- - com.sun.net.httpserver.Authenticator.Retry

com.sun.net.httpserver.Authenticator.Result

- com.sun.net.httpserver.Authenticator.Retry

com.sun.net.httpserver.Authenticator.Retry

**Enclosing class:** Authenticator

```java
public static class
Authenticator.Retry

extends
Authenticator.Result
```

Indicates an authentication must be retried. The
response code to be sent back is as returned from
getResponseCode(). The Authenticator must also have
set any necessary response headers in the given HttpExchange
before returning this Retry object.

public static class

Authenticator.Retry

extends

Authenticator.Result

Indicates an authentication must be retried. The
response code to be sent back is as returned from
getResponseCode(). The Authenticator must also have
set any necessary response headers in the given HttpExchange
before returning this Retry object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Retry

​(int responseCode)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getResponseCode

()

returns the response code to send to the client

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

Retry

​(int responseCode)

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getResponseCode

()

returns the response code to send to the client

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

returns the response code to send to the client

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

- Retry

```java
public Retry​(int responseCode)
```

============ METHOD DETAIL ==========

- Method Detail

- getResponseCode

```java
public int getResponseCode()
```

returns the response code to send to the client

Constructor Detail

- Retry

```java
public Retry​(int responseCode)
```

---

#### Constructor Detail

Retry

```java
public Retry​(int responseCode)
```

---

#### Retry

public Retry​(int responseCode)

Method Detail

- getResponseCode

```java
public int getResponseCode()
```

returns the response code to send to the client

---

#### Method Detail

getResponseCode

```java
public int getResponseCode()
```

returns the response code to send to the client

---

#### getResponseCode

public int getResponseCode()

returns the response code to send to the client

---

