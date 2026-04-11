# Class NoSuchAlgorithmException

**Source:** `java.base\java\security\NoSuchAlgorithmException.html`

### Class Description

```java
public class
NoSuchAlgorithmException

extends
GeneralSecurityException
```

This exception is thrown when a particular cryptographic algorithm is
requested but is not available in the environment.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NoSuchAlgorithmException()

Constructs a NoSuchAlgorithmException with no detail
message. A detail message is a String that describes this
particular exception.

---

#### public NoSuchAlgorithmException​(
String
msg)

Constructs a NoSuchAlgorithmException with the specified
detail message. A detail message is a String that describes
this particular exception, which may, for example, specify which
algorithm is not available.

**Parameters:**
- msg

- the detail message.

---

#### public NoSuchAlgorithmException​(
String
message,

Throwable
cause)

Creates a

NoSuchAlgorithmException

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

#### public NoSuchAlgorithmException​(
Throwable
cause)

Creates a

NoSuchAlgorithmException

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

#### Class NoSuchAlgorithmException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.NoSuchAlgorithmException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.NoSuchAlgorithmException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.NoSuchAlgorithmException

java.security.GeneralSecurityException

- java.security.NoSuchAlgorithmException

java.security.NoSuchAlgorithmException

**All Implemented Interfaces:** Serializable

```java
public class
NoSuchAlgorithmException

extends
GeneralSecurityException
```

This exception is thrown when a particular cryptographic algorithm is
requested but is not available in the environment.

**Since:** 1.1
**See Also:** Serialized Form

public class

NoSuchAlgorithmException

extends

GeneralSecurityException

This exception is thrown when a particular cryptographic algorithm is
requested but is not available in the environment.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NoSuchAlgorithmException

()

Constructs a NoSuchAlgorithmException with no detail
message.

NoSuchAlgorithmException

​(

String

msg)

Constructs a NoSuchAlgorithmException with the specified
detail message.

NoSuchAlgorithmException

​(

String

message,

Throwable

cause)

Creates a

NoSuchAlgorithmException

with the specified
detail message and cause.

NoSuchAlgorithmException

​(

Throwable

cause)

Creates a

NoSuchAlgorithmException

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

NoSuchAlgorithmException

()

Constructs a NoSuchAlgorithmException with no detail
message.

NoSuchAlgorithmException

​(

String

msg)

Constructs a NoSuchAlgorithmException with the specified
detail message.

NoSuchAlgorithmException

​(

String

message,

Throwable

cause)

Creates a

NoSuchAlgorithmException

with the specified
detail message and cause.

NoSuchAlgorithmException

​(

Throwable

cause)

Creates a

NoSuchAlgorithmException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a NoSuchAlgorithmException with no detail
message.

Constructs a NoSuchAlgorithmException with the specified
detail message.

Creates a

NoSuchAlgorithmException

with the specified
detail message and cause.

Creates a

NoSuchAlgorithmException

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

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException()
```

Constructs a NoSuchAlgorithmException with no detail
message. A detail message is a String that describes this
particular exception.

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
String
msg)
```

Constructs a NoSuchAlgorithmException with the specified
detail message. A detail message is a String that describes
this particular exception, which may, for example, specify which
algorithm is not available.

**Parameters:** msg

- the detail message.

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
String
message,

Throwable
cause)
```

Creates a

NoSuchAlgorithmException

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

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
Throwable
cause)
```

Creates a

NoSuchAlgorithmException

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

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException()
```

Constructs a NoSuchAlgorithmException with no detail
message. A detail message is a String that describes this
particular exception.

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
String
msg)
```

Constructs a NoSuchAlgorithmException with the specified
detail message. A detail message is a String that describes
this particular exception, which may, for example, specify which
algorithm is not available.

**Parameters:** msg

- the detail message.

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
String
message,

Throwable
cause)
```

Creates a

NoSuchAlgorithmException

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

- NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
Throwable
cause)
```

Creates a

NoSuchAlgorithmException

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

NoSuchAlgorithmException

```java
public NoSuchAlgorithmException()
```

Constructs a NoSuchAlgorithmException with no detail
message. A detail message is a String that describes this
particular exception.

---

#### NoSuchAlgorithmException

public NoSuchAlgorithmException()

Constructs a NoSuchAlgorithmException with no detail
message. A detail message is a String that describes this
particular exception.

NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
String
msg)
```

Constructs a NoSuchAlgorithmException with the specified
detail message. A detail message is a String that describes
this particular exception, which may, for example, specify which
algorithm is not available.

**Parameters:** msg

- the detail message.

---

#### NoSuchAlgorithmException

public NoSuchAlgorithmException​(

String

msg)

Constructs a NoSuchAlgorithmException with the specified
detail message. A detail message is a String that describes
this particular exception, which may, for example, specify which
algorithm is not available.

NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
String
message,

Throwable
cause)
```

Creates a

NoSuchAlgorithmException

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

#### NoSuchAlgorithmException

public NoSuchAlgorithmException​(

String

message,

Throwable

cause)

Creates a

NoSuchAlgorithmException

with the specified
detail message and cause.

NoSuchAlgorithmException

```java
public NoSuchAlgorithmException​(
Throwable
cause)
```

Creates a

NoSuchAlgorithmException

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

#### NoSuchAlgorithmException

public NoSuchAlgorithmException​(

Throwable

cause)

Creates a

NoSuchAlgorithmException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

