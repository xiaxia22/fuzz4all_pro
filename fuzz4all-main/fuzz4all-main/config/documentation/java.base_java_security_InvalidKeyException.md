# Class InvalidKeyException

**Source:** `java.base\java\security\InvalidKeyException.html`

### Class Description

```java
public class
InvalidKeyException

extends
KeyException
```

This is the exception for invalid Keys (invalid encoding, wrong
length, uninitialized, etc).

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidKeyException()

Constructs an InvalidKeyException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public InvalidKeyException​(
String
msg)

Constructs an InvalidKeyException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- msg

- the detail message.

---

#### public InvalidKeyException​(
String
message,

Throwable
cause)

Creates an

InvalidKeyException

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

#### public InvalidKeyException​(
Throwable
cause)

Creates an

InvalidKeyException

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

#### Class InvalidKeyException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyException
- - java.security.InvalidKeyException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyException
- - java.security.InvalidKeyException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.KeyException
- - java.security.InvalidKeyException

java.security.GeneralSecurityException

- java.security.KeyException
- - java.security.InvalidKeyException

java.security.KeyException

- java.security.InvalidKeyException

java.security.InvalidKeyException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidKeyException

extends
KeyException
```

This is the exception for invalid Keys (invalid encoding, wrong
length, uninitialized, etc).

**Since:** 1.1
**See Also:** Serialized Form

public class

InvalidKeyException

extends

KeyException

This is the exception for invalid Keys (invalid encoding, wrong
length, uninitialized, etc).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InvalidKeyException

()

Constructs an InvalidKeyException with no detail message.

InvalidKeyException

​(

String

msg)

Constructs an InvalidKeyException with the specified detail
message.

InvalidKeyException

​(

String

message,

Throwable

cause)

Creates an

InvalidKeyException

with the specified
detail message and cause.

InvalidKeyException

​(

Throwable

cause)

Creates an

InvalidKeyException

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

InvalidKeyException

()

Constructs an InvalidKeyException with no detail message.

InvalidKeyException

​(

String

msg)

Constructs an InvalidKeyException with the specified detail
message.

InvalidKeyException

​(

String

message,

Throwable

cause)

Creates an

InvalidKeyException

with the specified
detail message and cause.

InvalidKeyException

​(

Throwable

cause)

Creates an

InvalidKeyException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs an InvalidKeyException with no detail message.

Constructs an InvalidKeyException with the specified detail
message.

Creates an

InvalidKeyException

with the specified
detail message and cause.

Creates an

InvalidKeyException

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

- InvalidKeyException

```java
public InvalidKeyException()
```

Constructs an InvalidKeyException with no detail message. A
detail message is a String that describes this particular
exception.

- InvalidKeyException

```java
public InvalidKeyException​(
String
msg)
```

Constructs an InvalidKeyException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- InvalidKeyException

```java
public InvalidKeyException​(
String
message,

Throwable
cause)
```

Creates an

InvalidKeyException

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

- InvalidKeyException

```java
public InvalidKeyException​(
Throwable
cause)
```

Creates an

InvalidKeyException

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

- InvalidKeyException

```java
public InvalidKeyException()
```

Constructs an InvalidKeyException with no detail message. A
detail message is a String that describes this particular
exception.

- InvalidKeyException

```java
public InvalidKeyException​(
String
msg)
```

Constructs an InvalidKeyException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- InvalidKeyException

```java
public InvalidKeyException​(
String
message,

Throwable
cause)
```

Creates an

InvalidKeyException

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

- InvalidKeyException

```java
public InvalidKeyException​(
Throwable
cause)
```

Creates an

InvalidKeyException

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

InvalidKeyException

```java
public InvalidKeyException()
```

Constructs an InvalidKeyException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### InvalidKeyException

public InvalidKeyException()

Constructs an InvalidKeyException with no detail message. A
detail message is a String that describes this particular
exception.

InvalidKeyException

```java
public InvalidKeyException​(
String
msg)
```

Constructs an InvalidKeyException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

---

#### InvalidKeyException

public InvalidKeyException​(

String

msg)

Constructs an InvalidKeyException with the specified detail
message. A detail message is a String that describes this
particular exception.

InvalidKeyException

```java
public InvalidKeyException​(
String
message,

Throwable
cause)
```

Creates an

InvalidKeyException

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

#### InvalidKeyException

public InvalidKeyException​(

String

message,

Throwable

cause)

Creates an

InvalidKeyException

with the specified
detail message and cause.

InvalidKeyException

```java
public InvalidKeyException​(
Throwable
cause)
```

Creates an

InvalidKeyException

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

#### InvalidKeyException

public InvalidKeyException​(

Throwable

cause)

Creates an

InvalidKeyException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

