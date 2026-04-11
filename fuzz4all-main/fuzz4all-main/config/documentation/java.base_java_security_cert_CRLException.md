# Class CRLException

**Source:** `java.base\java\security\cert\CRLException.html`

### Class Description

```java
public class
CRLException

extends
GeneralSecurityException
```

CRL (Certificate Revocation List) Exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CRLException()

Constructs a CRLException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public CRLException​(
String
message)

Constructs a CRLException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- message

- the detail message.

---

#### public CRLException​(
String
message,

Throwable
cause)

Creates a

CRLException

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

#### public CRLException​(
Throwable
cause)

Creates a

CRLException

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

#### Class CRLException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CRLException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CRLException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.cert.CRLException

java.security.GeneralSecurityException

- java.security.cert.CRLException

java.security.cert.CRLException

**All Implemented Interfaces:** Serializable

```java
public class
CRLException

extends
GeneralSecurityException
```

CRL (Certificate Revocation List) Exception.

**Since:** 1.2
**See Also:** Serialized Form

public class

CRLException

extends

GeneralSecurityException

CRL (Certificate Revocation List) Exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CRLException

()

Constructs a CRLException with no detail message.

CRLException

​(

String

message)

Constructs a CRLException with the specified detail
message.

CRLException

​(

String

message,

Throwable

cause)

Creates a

CRLException

with the specified
detail message and cause.

CRLException

​(

Throwable

cause)

Creates a

CRLException

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

CRLException

()

Constructs a CRLException with no detail message.

CRLException

​(

String

message)

Constructs a CRLException with the specified detail
message.

CRLException

​(

String

message,

Throwable

cause)

Creates a

CRLException

with the specified
detail message and cause.

CRLException

​(

Throwable

cause)

Creates a

CRLException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a CRLException with no detail message.

Constructs a CRLException with the specified detail
message.

Creates a

CRLException

with the specified
detail message and cause.

Creates a

CRLException

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

- CRLException

```java
public CRLException()
```

Constructs a CRLException with no detail message. A
detail message is a String that describes this particular
exception.

- CRLException

```java
public CRLException​(
String
message)
```

Constructs a CRLException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

- CRLException

```java
public CRLException​(
String
message,

Throwable
cause)
```

Creates a

CRLException

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

- CRLException

```java
public CRLException​(
Throwable
cause)
```

Creates a

CRLException

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

- CRLException

```java
public CRLException()
```

Constructs a CRLException with no detail message. A
detail message is a String that describes this particular
exception.

- CRLException

```java
public CRLException​(
String
message)
```

Constructs a CRLException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

- CRLException

```java
public CRLException​(
String
message,

Throwable
cause)
```

Creates a

CRLException

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

- CRLException

```java
public CRLException​(
Throwable
cause)
```

Creates a

CRLException

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

CRLException

```java
public CRLException()
```

Constructs a CRLException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### CRLException

public CRLException()

Constructs a CRLException with no detail message. A
detail message is a String that describes this particular
exception.

CRLException

```java
public CRLException​(
String
message)
```

Constructs a CRLException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

---

#### CRLException

public CRLException​(

String

message)

Constructs a CRLException with the specified detail
message. A detail message is a String that describes this
particular exception.

CRLException

```java
public CRLException​(
String
message,

Throwable
cause)
```

Creates a

CRLException

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

#### CRLException

public CRLException​(

String

message,

Throwable

cause)

Creates a

CRLException

with the specified
detail message and cause.

CRLException

```java
public CRLException​(
Throwable
cause)
```

Creates a

CRLException

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

#### CRLException

public CRLException​(

Throwable

cause)

Creates a

CRLException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

