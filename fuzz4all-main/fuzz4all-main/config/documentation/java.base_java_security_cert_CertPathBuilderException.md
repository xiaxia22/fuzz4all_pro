# Class CertPathBuilderException

**Source:** `java.base\java\security\cert\CertPathBuilderException.html`

### Class Description

```java
public class
CertPathBuilderException

extends
GeneralSecurityException
```

An exception indicating one of a variety of problems encountered when
building a certification path with a

CertPathBuilder

.

A

CertPathBuilderException

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

#### public CertPathBuilderException()

Creates a

CertPathBuilderException

with

null

as its detail message.

---

#### public CertPathBuilderException​(
String
msg)

Creates a

CertPathBuilderException

with the given
detail message. The detail message is a

String

that
describes this particular exception in more detail.

**Parameters:**
- msg

- the detail message

---

#### public CertPathBuilderException​(
Throwable
cause)

Creates a

CertPathBuilderException

that wraps the specified
throwable. This allows any exception to be converted into a

CertPathBuilderException

, while retaining information
about the wrapped exception, which may be useful for debugging. The
detail message is set to (

cause==null ? null : cause.toString()

)
(which typically contains the class and detail message of
cause).

**Parameters:**
- cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

---

#### public CertPathBuilderException​(
String
msg,

Throwable
cause)

Creates a

CertPathBuilderException

with the specified
detail message and cause.

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

#### Class CertPathBuilderException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertPathBuilderException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertPathBuilderException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.cert.CertPathBuilderException

java.security.GeneralSecurityException

- java.security.cert.CertPathBuilderException

java.security.cert.CertPathBuilderException

**All Implemented Interfaces:** Serializable

```java
public class
CertPathBuilderException

extends
GeneralSecurityException
```

An exception indicating one of a variety of problems encountered when
building a certification path with a

CertPathBuilder

.

A

CertPathBuilderException

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
**See Also:** CertPathBuilder

,

Serialized Form

public class

CertPathBuilderException

extends

GeneralSecurityException

An exception indicating one of a variety of problems encountered when
building a certification path with a

CertPathBuilder

.

A

CertPathBuilderException

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

CertPathBuilderException

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

CertPathBuilderException

()

Creates a

CertPathBuilderException

with

null

as its detail message.

CertPathBuilderException

​(

String

msg)

Creates a

CertPathBuilderException

with the given
detail message.

CertPathBuilderException

​(

String

msg,

Throwable

cause)

Creates a

CertPathBuilderException

with the specified
detail message and cause.

CertPathBuilderException

​(

Throwable

cause)

Creates a

CertPathBuilderException

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

CertPathBuilderException

()

Creates a

CertPathBuilderException

with

null

as its detail message.

CertPathBuilderException

​(

String

msg)

Creates a

CertPathBuilderException

with the given
detail message.

CertPathBuilderException

​(

String

msg,

Throwable

cause)

Creates a

CertPathBuilderException

with the specified
detail message and cause.

CertPathBuilderException

​(

Throwable

cause)

Creates a

CertPathBuilderException

that wraps the specified
throwable.

---

#### Constructor Summary

Creates a

CertPathBuilderException

with

null

as its detail message.

Creates a

CertPathBuilderException

with the given
detail message.

Creates a

CertPathBuilderException

with the specified
detail message and cause.

Creates a

CertPathBuilderException

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

- CertPathBuilderException

```java
public CertPathBuilderException()
```

Creates a

CertPathBuilderException

with

null

as its detail message.

- CertPathBuilderException

```java
public CertPathBuilderException​(
String
msg)
```

Creates a

CertPathBuilderException

with the given
detail message. The detail message is a

String

that
describes this particular exception in more detail.

**Parameters:** msg

- the detail message

- CertPathBuilderException

```java
public CertPathBuilderException​(
Throwable
cause)
```

Creates a

CertPathBuilderException

that wraps the specified
throwable. This allows any exception to be converted into a

CertPathBuilderException

, while retaining information
about the wrapped exception, which may be useful for debugging. The
detail message is set to (

cause==null ? null : cause.toString()

)
(which typically contains the class and detail message of
cause).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

- CertPathBuilderException

```java
public CertPathBuilderException​(
String
msg,

Throwable
cause)
```

Creates a

CertPathBuilderException

with the specified
detail message and cause.

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

- CertPathBuilderException

```java
public CertPathBuilderException()
```

Creates a

CertPathBuilderException

with

null

as its detail message.

- CertPathBuilderException

```java
public CertPathBuilderException​(
String
msg)
```

Creates a

CertPathBuilderException

with the given
detail message. The detail message is a

String

that
describes this particular exception in more detail.

**Parameters:** msg

- the detail message

- CertPathBuilderException

```java
public CertPathBuilderException​(
Throwable
cause)
```

Creates a

CertPathBuilderException

that wraps the specified
throwable. This allows any exception to be converted into a

CertPathBuilderException

, while retaining information
about the wrapped exception, which may be useful for debugging. The
detail message is set to (

cause==null ? null : cause.toString()

)
(which typically contains the class and detail message of
cause).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

- CertPathBuilderException

```java
public CertPathBuilderException​(
String
msg,

Throwable
cause)
```

Creates a

CertPathBuilderException

with the specified
detail message and cause.

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

CertPathBuilderException

```java
public CertPathBuilderException()
```

Creates a

CertPathBuilderException

with

null

as its detail message.

---

#### CertPathBuilderException

public CertPathBuilderException()

Creates a

CertPathBuilderException

with

null

as its detail message.

CertPathBuilderException

```java
public CertPathBuilderException​(
String
msg)
```

Creates a

CertPathBuilderException

with the given
detail message. The detail message is a

String

that
describes this particular exception in more detail.

**Parameters:** msg

- the detail message

---

#### CertPathBuilderException

public CertPathBuilderException​(

String

msg)

Creates a

CertPathBuilderException

with the given
detail message. The detail message is a

String

that
describes this particular exception in more detail.

CertPathBuilderException

```java
public CertPathBuilderException​(
Throwable
cause)
```

Creates a

CertPathBuilderException

that wraps the specified
throwable. This allows any exception to be converted into a

CertPathBuilderException

, while retaining information
about the wrapped exception, which may be useful for debugging. The
detail message is set to (

cause==null ? null : cause.toString()

)
(which typically contains the class and detail message of
cause).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or unknown.)

---

#### CertPathBuilderException

public CertPathBuilderException​(

Throwable

cause)

Creates a

CertPathBuilderException

that wraps the specified
throwable. This allows any exception to be converted into a

CertPathBuilderException

, while retaining information
about the wrapped exception, which may be useful for debugging. The
detail message is set to (

cause==null ? null : cause.toString()

)
(which typically contains the class and detail message of
cause).

CertPathBuilderException

```java
public CertPathBuilderException​(
String
msg,

Throwable
cause)
```

Creates a

CertPathBuilderException

with the specified
detail message and cause.

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

#### CertPathBuilderException

public CertPathBuilderException​(

String

msg,

Throwable

cause)

Creates a

CertPathBuilderException

with the specified
detail message and cause.

---

