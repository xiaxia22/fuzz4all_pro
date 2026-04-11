# Class SSLException

**Source:** `java.base\javax\net\ssl\SSLException.html`

### Class Description

```java
public class
SSLException

extends
IOException
```

Indicates some kind of error detected by an SSL subsystem.
This class is the general class of exceptions produced
by failed SSL-related operations.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SSLException​(
String
reason)

Constructs an exception reporting an error found by
an SSL subsystem.

**Parameters:**
- reason

- describes the problem.

---

#### public SSLException​(
String
message,

Throwable
cause)

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

**Since:**
- 1.5

---

#### public SSLException​(
Throwable
cause)

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

**Since:**
- 1.5

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SSLException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - javax.net.ssl.SSLException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - javax.net.ssl.SSLException

java.lang.Exception

- java.io.IOException
- - javax.net.ssl.SSLException

java.io.IOException

- javax.net.ssl.SSLException

javax.net.ssl.SSLException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** SSLHandshakeException

,

SSLKeyException

,

SSLPeerUnverifiedException

,

SSLProtocolException

```java
public class
SSLException

extends
IOException
```

Indicates some kind of error detected by an SSL subsystem.
This class is the general class of exceptions produced
by failed SSL-related operations.

**Since:** 1.4
**See Also:** Serialized Form

public class

SSLException

extends

IOException

Indicates some kind of error detected by an SSL subsystem.
This class is the general class of exceptions produced
by failed SSL-related operations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SSLException

​(

String

reason)

Constructs an exception reporting an error found by
an SSL subsystem.

SSLException

​(

String

message,

Throwable

cause)

Creates a

SSLException

with the specified
detail message and cause.

SSLException

​(

Throwable

cause)

Creates a

SSLException

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

SSLException

​(

String

reason)

Constructs an exception reporting an error found by
an SSL subsystem.

SSLException

​(

String

message,

Throwable

cause)

Creates a

SSLException

with the specified
detail message and cause.

SSLException

​(

Throwable

cause)

Creates a

SSLException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs an exception reporting an error found by
an SSL subsystem.

Creates a

SSLException

with the specified
detail message and cause.

Creates a

SSLException

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

- SSLException

```java
public SSLException​(
String
reason)
```

Constructs an exception reporting an error found by
an SSL subsystem.

**Parameters:** reason

- describes the problem.

- SSLException

```java
public SSLException​(
String
message,

Throwable
cause)
```

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

- SSLException

```java
public SSLException​(
Throwable
cause)
```

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

Constructor Detail

- SSLException

```java
public SSLException​(
String
reason)
```

Constructs an exception reporting an error found by
an SSL subsystem.

**Parameters:** reason

- describes the problem.

- SSLException

```java
public SSLException​(
String
message,

Throwable
cause)
```

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

- SSLException

```java
public SSLException​(
Throwable
cause)
```

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### Constructor Detail

SSLException

```java
public SSLException​(
String
reason)
```

Constructs an exception reporting an error found by
an SSL subsystem.

**Parameters:** reason

- describes the problem.

---

#### SSLException

public SSLException​(

String

reason)

Constructs an exception reporting an error found by
an SSL subsystem.

SSLException

```java
public SSLException​(
String
message,

Throwable
cause)
```

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### SSLException

public SSLException​(

String

message,

Throwable

cause)

Creates a

SSLException

with the specified
detail message and cause.

SSLException

```java
public SSLException​(
Throwable
cause)
```

Creates a

SSLException

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### SSLException

public SSLException​(

Throwable

cause)

Creates a

SSLException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

