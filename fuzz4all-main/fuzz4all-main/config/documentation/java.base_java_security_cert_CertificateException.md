# Class CertificateException

**Source:** `java.base\java\security\cert\CertificateException.html`

### Class Description

```java
public class
CertificateException

extends
GeneralSecurityException
```

This exception indicates one of a variety of certificate problems.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertificateException()

Constructs a certificate exception with no detail message. A detail
message is a String that describes this particular exception.

---

#### public CertificateException​(
String
msg)

Constructs a certificate exception with the given detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- msg

- the detail message.

---

#### public CertificateException​(
String
message,

Throwable
cause)

Creates a

CertificateException

with the specified
detail message and cause.

**Parameters:**
- message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)

**Since:**
- 1.5

---

#### public CertificateException​(
Throwable
cause)

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:**
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)

**Since:**
- 1.5

---

### Method Details

*No entries found.*

### Additional Sections

#### Class CertificateException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.cert.CertificateException

java.security.GeneralSecurityException

- java.security.cert.CertificateException

java.security.cert.CertificateException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** CertificateEncodingException

,

CertificateExpiredException

,

CertificateNotYetValidException

,

CertificateParsingException

,

CertificateRevokedException

```java
public class
CertificateException

extends
GeneralSecurityException
```

This exception indicates one of a variety of certificate problems.

**Since:** 1.2
**See Also:** Certificate

,

Serialized Form

public class

CertificateException

extends

GeneralSecurityException

This exception indicates one of a variety of certificate problems.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertificateException

()

Constructs a certificate exception with no detail message.

CertificateException

​(

String

msg)

Constructs a certificate exception with the given detail
message.

CertificateException

​(

String

message,

Throwable

cause)

Creates a

CertificateException

with the specified
detail message and cause.

CertificateException

​(

Throwable

cause)

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

========== METHOD SUMMARY ===========

- Method Summary

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

CertificateException

()

Constructs a certificate exception with no detail message.

CertificateException

​(

String

msg)

Constructs a certificate exception with the given detail
message.

CertificateException

​(

String

message,

Throwable

cause)

Creates a

CertificateException

with the specified
detail message and cause.

CertificateException

​(

Throwable

cause)

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a certificate exception with no detail message.

Constructs a certificate exception with the given detail
message.

Creates a

CertificateException

with the specified
detail message and cause.

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

Method Summary

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

- CertificateException

```java
public CertificateException()
```

Constructs a certificate exception with no detail message. A detail
message is a String that describes this particular exception.

- CertificateException

```java
public CertificateException​(
String
msg)
```

Constructs a certificate exception with the given detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- CertificateException

```java
public CertificateException​(
String
message,

Throwable
cause)
```

Creates a

CertificateException

with the specified
detail message and cause.

**Parameters:** message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.5

- CertificateException

```java
public CertificateException​(
Throwable
cause)
```

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.5

Constructor Detail

- CertificateException

```java
public CertificateException()
```

Constructs a certificate exception with no detail message. A detail
message is a String that describes this particular exception.

- CertificateException

```java
public CertificateException​(
String
msg)
```

Constructs a certificate exception with the given detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- CertificateException

```java
public CertificateException​(
String
message,

Throwable
cause)
```

Creates a

CertificateException

with the specified
detail message and cause.

**Parameters:** message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.5

- CertificateException

```java
public CertificateException​(
Throwable
cause)
```

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.5

---

#### Constructor Detail

CertificateException

```java
public CertificateException()
```

Constructs a certificate exception with no detail message. A detail
message is a String that describes this particular exception.

---

#### CertificateException

public CertificateException()

Constructs a certificate exception with no detail message. A detail
message is a String that describes this particular exception.

CertificateException

```java
public CertificateException​(
String
msg)
```

Constructs a certificate exception with the given detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

---

#### CertificateException

public CertificateException​(

String

msg)

Constructs a certificate exception with the given detail
message. A detail message is a String that describes this
particular exception.

CertificateException

```java
public CertificateException​(
String
message,

Throwable
cause)
```

Creates a

CertificateException

with the specified
detail message and cause.

**Parameters:** message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.5

---

#### CertificateException

public CertificateException​(

String

message,

Throwable

cause)

Creates a

CertificateException

with the specified
detail message and cause.

CertificateException

```java
public CertificateException​(
Throwable
cause)
```

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.5

---

#### CertificateException

public CertificateException​(

Throwable

cause)

Creates a

CertificateException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

