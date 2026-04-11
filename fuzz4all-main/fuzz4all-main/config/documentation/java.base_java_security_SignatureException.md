# Class SignatureException

**Source:** `java.base\java\security\SignatureException.html`

### Class Description

```java
public class
SignatureException

extends
GeneralSecurityException
```

This is the generic Signature exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SignatureException()

Constructs a SignatureException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public SignatureException​(
String
msg)

Constructs a SignatureException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- msg

- the detail message.

---

#### public SignatureException​(
String
message,

Throwable
cause)

Creates a

SignatureException

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

#### public SignatureException​(
Throwable
cause)

Creates a

SignatureException

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

#### Class SignatureException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.SignatureException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.SignatureException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.SignatureException

java.security.GeneralSecurityException

- java.security.SignatureException

java.security.SignatureException

**All Implemented Interfaces:** Serializable

```java
public class
SignatureException

extends
GeneralSecurityException
```

This is the generic Signature exception.

**Since:** 1.1
**See Also:** Serialized Form

public class

SignatureException

extends

GeneralSecurityException

This is the generic Signature exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SignatureException

()

Constructs a SignatureException with no detail message.

SignatureException

​(

String

msg)

Constructs a SignatureException with the specified detail
message.

SignatureException

​(

String

message,

Throwable

cause)

Creates a

SignatureException

with the specified
detail message and cause.

SignatureException

​(

Throwable

cause)

Creates a

SignatureException

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

SignatureException

()

Constructs a SignatureException with no detail message.

SignatureException

​(

String

msg)

Constructs a SignatureException with the specified detail
message.

SignatureException

​(

String

message,

Throwable

cause)

Creates a

SignatureException

with the specified
detail message and cause.

SignatureException

​(

Throwable

cause)

Creates a

SignatureException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a SignatureException with no detail message.

Constructs a SignatureException with the specified detail
message.

Creates a

SignatureException

with the specified
detail message and cause.

Creates a

SignatureException

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

- SignatureException

```java
public SignatureException()
```

Constructs a SignatureException with no detail message. A
detail message is a String that describes this particular
exception.

- SignatureException

```java
public SignatureException​(
String
msg)
```

Constructs a SignatureException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- SignatureException

```java
public SignatureException​(
String
message,

Throwable
cause)
```

Creates a

SignatureException

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

- SignatureException

```java
public SignatureException​(
Throwable
cause)
```

Creates a

SignatureException

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

- SignatureException

```java
public SignatureException()
```

Constructs a SignatureException with no detail message. A
detail message is a String that describes this particular
exception.

- SignatureException

```java
public SignatureException​(
String
msg)
```

Constructs a SignatureException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- SignatureException

```java
public SignatureException​(
String
message,

Throwable
cause)
```

Creates a

SignatureException

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

- SignatureException

```java
public SignatureException​(
Throwable
cause)
```

Creates a

SignatureException

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

SignatureException

```java
public SignatureException()
```

Constructs a SignatureException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### SignatureException

public SignatureException()

Constructs a SignatureException with no detail message. A
detail message is a String that describes this particular
exception.

SignatureException

```java
public SignatureException​(
String
msg)
```

Constructs a SignatureException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

---

#### SignatureException

public SignatureException​(

String

msg)

Constructs a SignatureException with the specified detail
message. A detail message is a String that describes this
particular exception.

SignatureException

```java
public SignatureException​(
String
message,

Throwable
cause)
```

Creates a

SignatureException

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

#### SignatureException

public SignatureException​(

String

message,

Throwable

cause)

Creates a

SignatureException

with the specified
detail message and cause.

SignatureException

```java
public SignatureException​(
Throwable
cause)
```

Creates a

SignatureException

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

#### SignatureException

public SignatureException​(

Throwable

cause)

Creates a

SignatureException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

