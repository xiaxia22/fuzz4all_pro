# Class WebSocketHandshakeException

**Source:** `java.net.http\java\net\http\WebSocketHandshakeException.html`

### Class Description

```java
public final class
WebSocketHandshakeException

extends
IOException
```

Thrown when the opening handshake has failed.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public WebSocketHandshakeException​(
HttpResponse
<?> response)

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

**Parameters:**
- response

- the

HttpResponse

that resulted in the handshake failure

---

### Method Details

#### public
HttpResponse
<?> getResponse()

Returns the server's counterpart of the opening handshake.

The value may be unavailable (

null

) if this exception has
been serialized and then deserialized.

**Returns:**
- server response

**API Note:**
- The primary purpose of this method is to allow programmatic
examination of the reasons behind the failure of the opening handshake.
Some of these reasons might allow recovery.

---

### Additional Sections

#### Class WebSocketHandshakeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.net.http.WebSocketHandshakeException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.net.http.WebSocketHandshakeException

java.lang.Exception

- java.io.IOException
- - java.net.http.WebSocketHandshakeException

java.io.IOException

- java.net.http.WebSocketHandshakeException

java.net.http.WebSocketHandshakeException

**All Implemented Interfaces:** Serializable

```java
public final class
WebSocketHandshakeException

extends
IOException
```

Thrown when the opening handshake has failed.

**Since:** 11
**See Also:** Serialized Form

public final class

WebSocketHandshakeException

extends

IOException

Thrown when the opening handshake has failed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

WebSocketHandshakeException

​(

HttpResponse

<?> response)

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

HttpResponse

<?>

getResponse

()

Returns the server's counterpart of the opening handshake.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

WebSocketHandshakeException

​(

HttpResponse

<?> response)

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

---

#### Constructor Summary

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

HttpResponse

<?>

getResponse

()

Returns the server's counterpart of the opening handshake.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the server's counterpart of the opening handshake.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- WebSocketHandshakeException

```java
public WebSocketHandshakeException​(
HttpResponse
<?> response)
```

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

**Parameters:** response

- the

HttpResponse

that resulted in the handshake failure

============ METHOD DETAIL ==========

- Method Detail

- getResponse

```java
public
HttpResponse
<?> getResponse()
```

Returns the server's counterpart of the opening handshake.

The value may be unavailable (

null

) if this exception has
been serialized and then deserialized.

**API Note:** The primary purpose of this method is to allow programmatic
examination of the reasons behind the failure of the opening handshake.
Some of these reasons might allow recovery.
**Returns:** server response

Constructor Detail

- WebSocketHandshakeException

```java
public WebSocketHandshakeException​(
HttpResponse
<?> response)
```

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

**Parameters:** response

- the

HttpResponse

that resulted in the handshake failure

---

#### Constructor Detail

WebSocketHandshakeException

```java
public WebSocketHandshakeException​(
HttpResponse
<?> response)
```

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

**Parameters:** response

- the

HttpResponse

that resulted in the handshake failure

---

#### WebSocketHandshakeException

public WebSocketHandshakeException​(

HttpResponse

<?> response)

Constructs a

WebSocketHandshakeException

with the given

HttpResponse

.

Method Detail

- getResponse

```java
public
HttpResponse
<?> getResponse()
```

Returns the server's counterpart of the opening handshake.

The value may be unavailable (

null

) if this exception has
been serialized and then deserialized.

**API Note:** The primary purpose of this method is to allow programmatic
examination of the reasons behind the failure of the opening handshake.
Some of these reasons might allow recovery.
**Returns:** server response

---

#### Method Detail

getResponse

```java
public
HttpResponse
<?> getResponse()
```

Returns the server's counterpart of the opening handshake.

The value may be unavailable (

null

) if this exception has
been serialized and then deserialized.

**API Note:** The primary purpose of this method is to allow programmatic
examination of the reasons behind the failure of the opening handshake.
Some of these reasons might allow recovery.
**Returns:** server response

---

#### getResponse

public

HttpResponse

<?> getResponse()

Returns the server's counterpart of the opening handshake.

The value may be unavailable (

null

) if this exception has
been serialized and then deserialized.

The value may be unavailable (

null

) if this exception has
been serialized and then deserialized.

---

