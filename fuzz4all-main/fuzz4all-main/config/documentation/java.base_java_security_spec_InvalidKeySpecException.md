# Class InvalidKeySpecException

**Source:** `java.base\java\security\spec\InvalidKeySpecException.html`

### Class Description

```java
public class
InvalidKeySpecException

extends
GeneralSecurityException
```

This is the exception for invalid key specifications.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidKeySpecException()

Constructs an InvalidKeySpecException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public InvalidKeySpecException​(
String
msg)

Constructs an InvalidKeySpecException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- msg

- the detail message.

---

#### public InvalidKeySpecException​(
String
message,

Throwable
cause)

Creates an

InvalidKeySpecException

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

#### public InvalidKeySpecException​(
Throwable
cause)

Creates an

InvalidKeySpecException

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

#### Class InvalidKeySpecException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.spec.InvalidKeySpecException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.spec.InvalidKeySpecException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.spec.InvalidKeySpecException

java.security.GeneralSecurityException

- java.security.spec.InvalidKeySpecException

java.security.spec.InvalidKeySpecException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidKeySpecException

extends
GeneralSecurityException
```

This is the exception for invalid key specifications.

**Since:** 1.2
**See Also:** KeySpec

,

Serialized Form

public class

InvalidKeySpecException

extends

GeneralSecurityException

This is the exception for invalid key specifications.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InvalidKeySpecException

()

Constructs an InvalidKeySpecException with no detail message.

InvalidKeySpecException

​(

String

msg)

Constructs an InvalidKeySpecException with the specified detail
message.

InvalidKeySpecException

​(

String

message,

Throwable

cause)

Creates an

InvalidKeySpecException

with the specified
detail message and cause.

InvalidKeySpecException

​(

Throwable

cause)

Creates an

InvalidKeySpecException

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

InvalidKeySpecException

()

Constructs an InvalidKeySpecException with no detail message.

InvalidKeySpecException

​(

String

msg)

Constructs an InvalidKeySpecException with the specified detail
message.

InvalidKeySpecException

​(

String

message,

Throwable

cause)

Creates an

InvalidKeySpecException

with the specified
detail message and cause.

InvalidKeySpecException

​(

Throwable

cause)

Creates an

InvalidKeySpecException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs an InvalidKeySpecException with no detail message.

Constructs an InvalidKeySpecException with the specified detail
message.

Creates an

InvalidKeySpecException

with the specified
detail message and cause.

Creates an

InvalidKeySpecException

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

- InvalidKeySpecException

```java
public InvalidKeySpecException()
```

Constructs an InvalidKeySpecException with no detail message. A
detail message is a String that describes this particular
exception.

- InvalidKeySpecException

```java
public InvalidKeySpecException​(
String
msg)
```

Constructs an InvalidKeySpecException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- InvalidKeySpecException

```java
public InvalidKeySpecException​(
String
message,

Throwable
cause)
```

Creates an

InvalidKeySpecException

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

- InvalidKeySpecException

```java
public InvalidKeySpecException​(
Throwable
cause)
```

Creates an

InvalidKeySpecException

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

- InvalidKeySpecException

```java
public InvalidKeySpecException()
```

Constructs an InvalidKeySpecException with no detail message. A
detail message is a String that describes this particular
exception.

- InvalidKeySpecException

```java
public InvalidKeySpecException​(
String
msg)
```

Constructs an InvalidKeySpecException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- InvalidKeySpecException

```java
public InvalidKeySpecException​(
String
message,

Throwable
cause)
```

Creates an

InvalidKeySpecException

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

- InvalidKeySpecException

```java
public InvalidKeySpecException​(
Throwable
cause)
```

Creates an

InvalidKeySpecException

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

InvalidKeySpecException

```java
public InvalidKeySpecException()
```

Constructs an InvalidKeySpecException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### InvalidKeySpecException

public InvalidKeySpecException()

Constructs an InvalidKeySpecException with no detail message. A
detail message is a String that describes this particular
exception.

InvalidKeySpecException

```java
public InvalidKeySpecException​(
String
msg)
```

Constructs an InvalidKeySpecException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

---

#### InvalidKeySpecException

public InvalidKeySpecException​(

String

msg)

Constructs an InvalidKeySpecException with the specified detail
message. A detail message is a String that describes this
particular exception.

InvalidKeySpecException

```java
public InvalidKeySpecException​(
String
message,

Throwable
cause)
```

Creates an

InvalidKeySpecException

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

#### InvalidKeySpecException

public InvalidKeySpecException​(

String

message,

Throwable

cause)

Creates an

InvalidKeySpecException

with the specified
detail message and cause.

InvalidKeySpecException

```java
public InvalidKeySpecException​(
Throwable
cause)
```

Creates an

InvalidKeySpecException

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

#### InvalidKeySpecException

public InvalidKeySpecException​(

Throwable

cause)

Creates an

InvalidKeySpecException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

