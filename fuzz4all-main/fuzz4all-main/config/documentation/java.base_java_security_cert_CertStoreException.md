# Class CertStoreException

**Source:** `java.base\java\security\cert\CertStoreException.html`

### Class Description

```java
public class
CertStoreException

extends
GeneralSecurityException
```

An exception indicating one of a variety of problems retrieving
certificates and CRLs from a

CertStore

.

A

CertStoreException

provides support for wrapping
exceptions. The

getCause

method returns the throwable,
if any, that caused this exception to be thrown.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertStoreException()

Creates a

CertStoreException

with

null

as
its detail message.

---

#### public CertStoreException​(
String
msg)

Creates a

CertStoreException

with the given detail
message. A detail message is a

String

that describes this
particular exception.

**Parameters:**
- msg

- the detail message

---

#### public CertStoreException​(
Throwable
cause)

Creates a

CertStoreException

that wraps the specified
throwable. This allows any exception to be converted into a

CertStoreException

, while retaining information about the
cause, which may be useful for debugging. The detail message is
set to (

cause==null ? null : cause.toString()

) (which
typically contains the class and detail message of cause).

**Parameters:**
- cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

---

#### public CertStoreException​(
String
msg,

Throwable
cause)

Creates a

CertStoreException

with the specified detail
message and cause.

**Parameters:**
- msg

- the detail message
- cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

---

### Method Details

*No entries found.*

### Additional Sections

#### Class CertStoreException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertStoreException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertStoreException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.cert.CertStoreException

java.security.GeneralSecurityException

- java.security.cert.CertStoreException

java.security.cert.CertStoreException

**All Implemented Interfaces:** Serializable

```java
public class
CertStoreException

extends
GeneralSecurityException
```

An exception indicating one of a variety of problems retrieving
certificates and CRLs from a

CertStore

.

A

CertStoreException

provides support for wrapping
exceptions. The

getCause

method returns the throwable,
if any, that caused this exception to be thrown.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** CertStore

,

Serialized Form

public class

CertStoreException

extends

GeneralSecurityException

An exception indicating one of a variety of problems retrieving
certificates and CRLs from a

CertStore

.

A

CertStoreException

provides support for wrapping
exceptions. The

getCause

method returns the throwable,
if any, that caused this exception to be thrown.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

A

CertStoreException

provides support for wrapping
exceptions. The

getCause

method returns the throwable,
if any, that caused this exception to be thrown.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertStoreException

()

Creates a

CertStoreException

with

null

as
its detail message.

CertStoreException

​(

String

msg)

Creates a

CertStoreException

with the given detail
message.

CertStoreException

​(

String

msg,

Throwable

cause)

Creates a

CertStoreException

with the specified detail
message and cause.

CertStoreException

​(

Throwable

cause)

Creates a

CertStoreException

that wraps the specified
throwable.

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

CertStoreException

()

Creates a

CertStoreException

with

null

as
its detail message.

CertStoreException

​(

String

msg)

Creates a

CertStoreException

with the given detail
message.

CertStoreException

​(

String

msg,

Throwable

cause)

Creates a

CertStoreException

with the specified detail
message and cause.

CertStoreException

​(

Throwable

cause)

Creates a

CertStoreException

that wraps the specified
throwable.

---

#### Constructor Summary

Creates a

CertStoreException

with

null

as
its detail message.

Creates a

CertStoreException

with the given detail
message.

Creates a

CertStoreException

with the specified detail
message and cause.

Creates a

CertStoreException

that wraps the specified
throwable.

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

- CertStoreException

```java
public CertStoreException()
```

Creates a

CertStoreException

with

null

as
its detail message.

- CertStoreException

```java
public CertStoreException​(
String
msg)
```

Creates a

CertStoreException

with the given detail
message. A detail message is a

String

that describes this
particular exception.

**Parameters:** msg

- the detail message

- CertStoreException

```java
public CertStoreException​(
Throwable
cause)
```

Creates a

CertStoreException

that wraps the specified
throwable. This allows any exception to be converted into a

CertStoreException

, while retaining information about the
cause, which may be useful for debugging. The detail message is
set to (

cause==null ? null : cause.toString()

) (which
typically contains the class and detail message of cause).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

- CertStoreException

```java
public CertStoreException​(
String
msg,

Throwable
cause)
```

Creates a

CertStoreException

with the specified detail
message and cause.

**Parameters:** msg

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

Constructor Detail

- CertStoreException

```java
public CertStoreException()
```

Creates a

CertStoreException

with

null

as
its detail message.

- CertStoreException

```java
public CertStoreException​(
String
msg)
```

Creates a

CertStoreException

with the given detail
message. A detail message is a

String

that describes this
particular exception.

**Parameters:** msg

- the detail message

- CertStoreException

```java
public CertStoreException​(
Throwable
cause)
```

Creates a

CertStoreException

that wraps the specified
throwable. This allows any exception to be converted into a

CertStoreException

, while retaining information about the
cause, which may be useful for debugging. The detail message is
set to (

cause==null ? null : cause.toString()

) (which
typically contains the class and detail message of cause).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

- CertStoreException

```java
public CertStoreException​(
String
msg,

Throwable
cause)
```

Creates a

CertStoreException

with the specified detail
message and cause.

**Parameters:** msg

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

---

#### Constructor Detail

CertStoreException

```java
public CertStoreException()
```

Creates a

CertStoreException

with

null

as
its detail message.

---

#### CertStoreException

public CertStoreException()

Creates a

CertStoreException

with

null

as
its detail message.

CertStoreException

```java
public CertStoreException​(
String
msg)
```

Creates a

CertStoreException

with the given detail
message. A detail message is a

String

that describes this
particular exception.

**Parameters:** msg

- the detail message

---

#### CertStoreException

public CertStoreException​(

String

msg)

Creates a

CertStoreException

with the given detail
message. A detail message is a

String

that describes this
particular exception.

CertStoreException

```java
public CertStoreException​(
Throwable
cause)
```

Creates a

CertStoreException

that wraps the specified
throwable. This allows any exception to be converted into a

CertStoreException

, while retaining information about the
cause, which may be useful for debugging. The detail message is
set to (

cause==null ? null : cause.toString()

) (which
typically contains the class and detail message of cause).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

---

#### CertStoreException

public CertStoreException​(

Throwable

cause)

Creates a

CertStoreException

that wraps the specified
throwable. This allows any exception to be converted into a

CertStoreException

, while retaining information about the
cause, which may be useful for debugging. The detail message is
set to (

cause==null ? null : cause.toString()

) (which
typically contains the class and detail message of cause).

CertStoreException

```java
public CertStoreException​(
String
msg,

Throwable
cause)
```

Creates a

CertStoreException

with the specified detail
message and cause.

**Parameters:** msg

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

---

#### CertStoreException

public CertStoreException​(

String

msg,

Throwable

cause)

Creates a

CertStoreException

with the specified detail
message and cause.

---

