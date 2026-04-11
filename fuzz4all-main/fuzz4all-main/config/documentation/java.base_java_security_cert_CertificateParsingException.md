# Class CertificateParsingException

**Source:** `java.base\java\security\cert\CertificateParsingException.html`

### Class Description

```java
public class
CertificateParsingException

extends
CertificateException
```

Certificate Parsing Exception. This is thrown whenever an
invalid DER-encoded certificate is parsed or unsupported DER features
are found in the Certificate.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertificateParsingException()

Constructs a CertificateParsingException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public CertificateParsingException​(
String
message)

Constructs a CertificateParsingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- message

- the detail message.

---

#### public CertificateParsingException​(
String
message,

Throwable
cause)

Creates a

CertificateParsingException

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

#### public CertificateParsingException​(
Throwable
cause)

Creates a

CertificateParsingException

with the
specified cause and a detail message of

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

#### Class CertificateParsingException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateParsingException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateParsingException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateParsingException

java.security.GeneralSecurityException

- java.security.cert.CertificateException
- - java.security.cert.CertificateParsingException

java.security.cert.CertificateException

- java.security.cert.CertificateParsingException

java.security.cert.CertificateParsingException

**All Implemented Interfaces:** Serializable

```java
public class
CertificateParsingException

extends
CertificateException
```

Certificate Parsing Exception. This is thrown whenever an
invalid DER-encoded certificate is parsed or unsupported DER features
are found in the Certificate.

**Since:** 1.2
**See Also:** Serialized Form

public class

CertificateParsingException

extends

CertificateException

Certificate Parsing Exception. This is thrown whenever an
invalid DER-encoded certificate is parsed or unsupported DER features
are found in the Certificate.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertificateParsingException

()

Constructs a CertificateParsingException with no detail message.

CertificateParsingException

​(

String

message)

Constructs a CertificateParsingException with the specified detail
message.

CertificateParsingException

​(

String

message,

Throwable

cause)

Creates a

CertificateParsingException

with the specified
detail message and cause.

CertificateParsingException

​(

Throwable

cause)

Creates a

CertificateParsingException

with the
specified cause and a detail message of

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

CertificateParsingException

()

Constructs a CertificateParsingException with no detail message.

CertificateParsingException

​(

String

message)

Constructs a CertificateParsingException with the specified detail
message.

CertificateParsingException

​(

String

message,

Throwable

cause)

Creates a

CertificateParsingException

with the specified
detail message and cause.

CertificateParsingException

​(

Throwable

cause)

Creates a

CertificateParsingException

with the
specified cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a CertificateParsingException with no detail message.

Constructs a CertificateParsingException with the specified detail
message.

Creates a

CertificateParsingException

with the specified
detail message and cause.

Creates a

CertificateParsingException

with the
specified cause and a detail message of

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

- CertificateParsingException

```java
public CertificateParsingException()
```

Constructs a CertificateParsingException with no detail message. A
detail message is a String that describes this particular
exception.

- CertificateParsingException

```java
public CertificateParsingException​(
String
message)
```

Constructs a CertificateParsingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

- CertificateParsingException

```java
public CertificateParsingException​(
String
message,

Throwable
cause)
```

Creates a

CertificateParsingException

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

- CertificateParsingException

```java
public CertificateParsingException​(
Throwable
cause)
```

Creates a

CertificateParsingException

with the
specified cause and a detail message of

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

- CertificateParsingException

```java
public CertificateParsingException()
```

Constructs a CertificateParsingException with no detail message. A
detail message is a String that describes this particular
exception.

- CertificateParsingException

```java
public CertificateParsingException​(
String
message)
```

Constructs a CertificateParsingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

- CertificateParsingException

```java
public CertificateParsingException​(
String
message,

Throwable
cause)
```

Creates a

CertificateParsingException

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

- CertificateParsingException

```java
public CertificateParsingException​(
Throwable
cause)
```

Creates a

CertificateParsingException

with the
specified cause and a detail message of

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

CertificateParsingException

```java
public CertificateParsingException()
```

Constructs a CertificateParsingException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### CertificateParsingException

public CertificateParsingException()

Constructs a CertificateParsingException with no detail message. A
detail message is a String that describes this particular
exception.

CertificateParsingException

```java
public CertificateParsingException​(
String
message)
```

Constructs a CertificateParsingException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

---

#### CertificateParsingException

public CertificateParsingException​(

String

message)

Constructs a CertificateParsingException with the specified detail
message. A detail message is a String that describes this
particular exception.

CertificateParsingException

```java
public CertificateParsingException​(
String
message,

Throwable
cause)
```

Creates a

CertificateParsingException

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

#### CertificateParsingException

public CertificateParsingException​(

String

message,

Throwable

cause)

Creates a

CertificateParsingException

with the specified
detail message and cause.

CertificateParsingException

```java
public CertificateParsingException​(
Throwable
cause)
```

Creates a

CertificateParsingException

with the
specified cause and a detail message of

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

#### CertificateParsingException

public CertificateParsingException​(

Throwable

cause)

Creates a

CertificateParsingException

with the
specified cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

