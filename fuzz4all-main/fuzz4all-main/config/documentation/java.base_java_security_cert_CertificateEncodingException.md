# Class CertificateEncodingException

**Source:** `java.base\java\security\cert\CertificateEncodingException.html`

### Class Description

```java
public class
CertificateEncodingException

extends
CertificateException
```

Certificate Encoding Exception. This is thrown whenever an error
occurs while attempting to encode a certificate.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertificateEncodingException()

Constructs a CertificateEncodingException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public CertificateEncodingException​(
String
message)

Constructs a CertificateEncodingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- message

- the detail message.

---

#### public CertificateEncodingException​(
String
message,

Throwable
cause)

Creates a

CertificateEncodingException

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

#### public CertificateEncodingException​(
Throwable
cause)

Creates a

CertificateEncodingException

with the specified cause and a detail message of

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

#### Class CertificateEncodingException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateEncodingException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateEncodingException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateEncodingException

java.security.GeneralSecurityException

- java.security.cert.CertificateException
- - java.security.cert.CertificateEncodingException

java.security.cert.CertificateException

- java.security.cert.CertificateEncodingException

java.security.cert.CertificateEncodingException

**All Implemented Interfaces:** Serializable

```java
public class
CertificateEncodingException

extends
CertificateException
```

Certificate Encoding Exception. This is thrown whenever an error
occurs while attempting to encode a certificate.

**Since:** 1.2
**See Also:** Serialized Form

public class

CertificateEncodingException

extends

CertificateException

Certificate Encoding Exception. This is thrown whenever an error
occurs while attempting to encode a certificate.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertificateEncodingException

()

Constructs a CertificateEncodingException with no detail message.

CertificateEncodingException

​(

String

message)

Constructs a CertificateEncodingException with the specified detail
message.

CertificateEncodingException

​(

String

message,

Throwable

cause)

Creates a

CertificateEncodingException

with the specified
detail message and cause.

CertificateEncodingException

​(

Throwable

cause)

Creates a

CertificateEncodingException

with the specified cause and a detail message of

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

CertificateEncodingException

()

Constructs a CertificateEncodingException with no detail message.

CertificateEncodingException

​(

String

message)

Constructs a CertificateEncodingException with the specified detail
message.

CertificateEncodingException

​(

String

message,

Throwable

cause)

Creates a

CertificateEncodingException

with the specified
detail message and cause.

CertificateEncodingException

​(

Throwable

cause)

Creates a

CertificateEncodingException

with the specified cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a CertificateEncodingException with no detail message.

Constructs a CertificateEncodingException with the specified detail
message.

Creates a

CertificateEncodingException

with the specified
detail message and cause.

Creates a

CertificateEncodingException

with the specified cause and a detail message of

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

- CertificateEncodingException

```java
public CertificateEncodingException()
```

Constructs a CertificateEncodingException with no detail message. A
detail message is a String that describes this particular
exception.

- CertificateEncodingException

```java
public CertificateEncodingException​(
String
message)
```

Constructs a CertificateEncodingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

- CertificateEncodingException

```java
public CertificateEncodingException​(
String
message,

Throwable
cause)
```

Creates a

CertificateEncodingException

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

- CertificateEncodingException

```java
public CertificateEncodingException​(
Throwable
cause)
```

Creates a

CertificateEncodingException

with the specified cause and a detail message of

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

- CertificateEncodingException

```java
public CertificateEncodingException()
```

Constructs a CertificateEncodingException with no detail message. A
detail message is a String that describes this particular
exception.

- CertificateEncodingException

```java
public CertificateEncodingException​(
String
message)
```

Constructs a CertificateEncodingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

- CertificateEncodingException

```java
public CertificateEncodingException​(
String
message,

Throwable
cause)
```

Creates a

CertificateEncodingException

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

- CertificateEncodingException

```java
public CertificateEncodingException​(
Throwable
cause)
```

Creates a

CertificateEncodingException

with the specified cause and a detail message of

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

CertificateEncodingException

```java
public CertificateEncodingException()
```

Constructs a CertificateEncodingException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### CertificateEncodingException

public CertificateEncodingException()

Constructs a CertificateEncodingException with no detail message. A
detail message is a String that describes this particular
exception.

CertificateEncodingException

```java
public CertificateEncodingException​(
String
message)
```

Constructs a CertificateEncodingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

---

#### CertificateEncodingException

public CertificateEncodingException​(

String

message)

Constructs a CertificateEncodingException with the specified detail
message. A detail message is a String that describes this
particular exception.

CertificateEncodingException

```java
public CertificateEncodingException​(
String
message,

Throwable
cause)
```

Creates a

CertificateEncodingException

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

#### CertificateEncodingException

public CertificateEncodingException​(

String

message,

Throwable

cause)

Creates a

CertificateEncodingException

with the specified
detail message and cause.

CertificateEncodingException

```java
public CertificateEncodingException​(
Throwable
cause)
```

Creates a

CertificateEncodingException

with the specified cause and a detail message of

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

#### CertificateEncodingException

public CertificateEncodingException​(

Throwable

cause)

Creates a

CertificateEncodingException

with the specified cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

