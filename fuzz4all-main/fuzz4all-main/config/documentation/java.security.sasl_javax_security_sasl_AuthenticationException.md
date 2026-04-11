# Class AuthenticationException

**Source:** `java.security.sasl\javax\security\sasl\AuthenticationException.html`

### Class Description

```java
public class
AuthenticationException

extends
SaslException
```

This exception is thrown by a SASL mechanism implementation
to indicate that the SASL
exchange has failed due to reasons related to authentication, such as
an invalid identity, passphrase, or key.

Note that the lack of an AuthenticationException does not mean that
the failure was not due to an authentication error. A SASL mechanism
implementation might throw the more general SaslException instead of
AuthenticationException if it is unable to determine the nature
of the failure, or if does not want to disclose the nature of
the failure, for example, due to security reasons.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AuthenticationException()

Constructs a new instance of

AuthenticationException

.
The root exception and the detailed message are null.

---

#### public AuthenticationException​(
String
detail)

Constructs a new instance of

AuthenticationException

with a detailed message.
The root exception is null.

**Parameters:**
- detail

- A possibly null string containing details of the exception.

**See Also:**
- Throwable.getMessage()

---

#### public AuthenticationException​(
String
detail,

Throwable
ex)

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

**Parameters:**
- detail

- A possibly null string containing details of the exception.
- ex

- A possibly null root exception that caused this exception.

**See Also:**
- Throwable.getMessage()

,

Throwable.getCause()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AuthenticationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - javax.security.sasl.SaslException
- - javax.security.sasl.AuthenticationException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - javax.security.sasl.SaslException
- - javax.security.sasl.AuthenticationException

java.lang.Exception

- java.io.IOException
- - javax.security.sasl.SaslException
- - javax.security.sasl.AuthenticationException

java.io.IOException

- javax.security.sasl.SaslException
- - javax.security.sasl.AuthenticationException

javax.security.sasl.SaslException

- javax.security.sasl.AuthenticationException

javax.security.sasl.AuthenticationException

**All Implemented Interfaces:** Serializable

```java
public class
AuthenticationException

extends
SaslException
```

This exception is thrown by a SASL mechanism implementation
to indicate that the SASL
exchange has failed due to reasons related to authentication, such as
an invalid identity, passphrase, or key.

Note that the lack of an AuthenticationException does not mean that
the failure was not due to an authentication error. A SASL mechanism
implementation might throw the more general SaslException instead of
AuthenticationException if it is unable to determine the nature
of the failure, or if does not want to disclose the nature of
the failure, for example, due to security reasons.

**Since:** 1.5
**See Also:** Serialized Form

public class

AuthenticationException

extends

SaslException

This exception is thrown by a SASL mechanism implementation
to indicate that the SASL
exchange has failed due to reasons related to authentication, such as
an invalid identity, passphrase, or key.

Note that the lack of an AuthenticationException does not mean that
the failure was not due to an authentication error. A SASL mechanism
implementation might throw the more general SaslException instead of
AuthenticationException if it is unable to determine the nature
of the failure, or if does not want to disclose the nature of
the failure, for example, due to security reasons.

Note that the lack of an AuthenticationException does not mean that
the failure was not due to an authentication error. A SASL mechanism
implementation might throw the more general SaslException instead of
AuthenticationException if it is unable to determine the nature
of the failure, or if does not want to disclose the nature of
the failure, for example, due to security reasons.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AuthenticationException

()

Constructs a new instance of

AuthenticationException

.

AuthenticationException

​(

String

detail)

Constructs a new instance of

AuthenticationException

with a detailed message.

AuthenticationException

​(

String

detail,

Throwable

ex)

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.security.sasl.

SaslException

toString

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

AuthenticationException

()

Constructs a new instance of

AuthenticationException

.

AuthenticationException

​(

String

detail)

Constructs a new instance of

AuthenticationException

with a detailed message.

AuthenticationException

​(

String

detail,

Throwable

ex)

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

---

#### Constructor Summary

Constructs a new instance of

AuthenticationException

.

Constructs a new instance of

AuthenticationException

with a detailed message.

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

Method Summary

- Methods declared in class javax.security.sasl.

SaslException

toString

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

Methods declared in class javax.security.sasl.

SaslException

toString

---

#### Methods declared in class javax.security.sasl. SaslException

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

- AuthenticationException

```java
public AuthenticationException()
```

Constructs a new instance of

AuthenticationException

.
The root exception and the detailed message are null.

- AuthenticationException

```java
public AuthenticationException​(
String
detail)
```

Constructs a new instance of

AuthenticationException

with a detailed message.
The root exception is null.

**Parameters:** detail

- A possibly null string containing details of the exception.
**See Also:** Throwable.getMessage()

- AuthenticationException

```java
public AuthenticationException​(
String
detail,

Throwable
ex)
```

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

**Parameters:** detail

- A possibly null string containing details of the exception.
**Parameters:** ex

- A possibly null root exception that caused this exception.
**See Also:** Throwable.getMessage()

,

Throwable.getCause()

Constructor Detail

- AuthenticationException

```java
public AuthenticationException()
```

Constructs a new instance of

AuthenticationException

.
The root exception and the detailed message are null.

- AuthenticationException

```java
public AuthenticationException​(
String
detail)
```

Constructs a new instance of

AuthenticationException

with a detailed message.
The root exception is null.

**Parameters:** detail

- A possibly null string containing details of the exception.
**See Also:** Throwable.getMessage()

- AuthenticationException

```java
public AuthenticationException​(
String
detail,

Throwable
ex)
```

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

**Parameters:** detail

- A possibly null string containing details of the exception.
**Parameters:** ex

- A possibly null root exception that caused this exception.
**See Also:** Throwable.getMessage()

,

Throwable.getCause()

---

#### Constructor Detail

AuthenticationException

```java
public AuthenticationException()
```

Constructs a new instance of

AuthenticationException

.
The root exception and the detailed message are null.

---

#### AuthenticationException

public AuthenticationException()

Constructs a new instance of

AuthenticationException

.
The root exception and the detailed message are null.

AuthenticationException

```java
public AuthenticationException​(
String
detail)
```

Constructs a new instance of

AuthenticationException

with a detailed message.
The root exception is null.

**Parameters:** detail

- A possibly null string containing details of the exception.
**See Also:** Throwable.getMessage()

---

#### AuthenticationException

public AuthenticationException​(

String

detail)

Constructs a new instance of

AuthenticationException

with a detailed message.
The root exception is null.

AuthenticationException

```java
public AuthenticationException​(
String
detail,

Throwable
ex)
```

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

**Parameters:** detail

- A possibly null string containing details of the exception.
**Parameters:** ex

- A possibly null root exception that caused this exception.
**See Also:** Throwable.getMessage()

,

Throwable.getCause()

---

#### AuthenticationException

public AuthenticationException​(

String

detail,

Throwable

ex)

Constructs a new instance of

AuthenticationException

with a detailed message
and a root exception.

---

