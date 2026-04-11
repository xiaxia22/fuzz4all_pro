# Class KeyManagementException

**Source:** `java.base\java\security\KeyManagementException.html`

### Class Description

```java
public class
KeyManagementException

extends
KeyException
```

This is the general key management exception for all operations
dealing with key management. Examples of subclasses of
KeyManagementException that developers might create for
giving more detailed information could include:

- KeyIDConflictException

KeyAuthorizationFailureException

ExpiredKeyException

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyManagementException()

Constructs a KeyManagementException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public KeyManagementException​(
String
msg)

Constructs a KeyManagementException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- msg

- the detail message.

---

#### public KeyManagementException​(
String
message,

Throwable
cause)

Creates a

KeyManagementException

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

#### public KeyManagementException​(
Throwable
cause)

Creates a

KeyManagementException

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

#### Class KeyManagementException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyException
- - java.security.KeyManagementException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyException
- - java.security.KeyManagementException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.KeyException
- - java.security.KeyManagementException

java.security.GeneralSecurityException

- java.security.KeyException
- - java.security.KeyManagementException

java.security.KeyException

- java.security.KeyManagementException

java.security.KeyManagementException

**All Implemented Interfaces:** Serializable

```java
public class
KeyManagementException

extends
KeyException
```

This is the general key management exception for all operations
dealing with key management. Examples of subclasses of
KeyManagementException that developers might create for
giving more detailed information could include:

- KeyIDConflictException

KeyAuthorizationFailureException

ExpiredKeyException

**Since:** 1.1
**See Also:** Key

,

KeyException

,

Serialized Form

public class

KeyManagementException

extends

KeyException

This is the general key management exception for all operations
dealing with key management. Examples of subclasses of
KeyManagementException that developers might create for
giving more detailed information could include:

- KeyIDConflictException

KeyAuthorizationFailureException

ExpiredKeyException

KeyIDConflictException

KeyAuthorizationFailureException

ExpiredKeyException

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyManagementException

()

Constructs a KeyManagementException with no detail message.

KeyManagementException

​(

String

msg)

Constructs a KeyManagementException with the specified detail
message.

KeyManagementException

​(

String

message,

Throwable

cause)

Creates a

KeyManagementException

with the specified
detail message and cause.

KeyManagementException

​(

Throwable

cause)

Creates a

KeyManagementException

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

KeyManagementException

()

Constructs a KeyManagementException with no detail message.

KeyManagementException

​(

String

msg)

Constructs a KeyManagementException with the specified detail
message.

KeyManagementException

​(

String

message,

Throwable

cause)

Creates a

KeyManagementException

with the specified
detail message and cause.

KeyManagementException

​(

Throwable

cause)

Creates a

KeyManagementException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a KeyManagementException with no detail message.

Constructs a KeyManagementException with the specified detail
message.

Creates a

KeyManagementException

with the specified
detail message and cause.

Creates a

KeyManagementException

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

- KeyManagementException

```java
public KeyManagementException()
```

Constructs a KeyManagementException with no detail message. A
detail message is a String that describes this particular
exception.

- KeyManagementException

```java
public KeyManagementException​(
String
msg)
```

Constructs a KeyManagementException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- KeyManagementException

```java
public KeyManagementException​(
String
message,

Throwable
cause)
```

Creates a

KeyManagementException

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

- KeyManagementException

```java
public KeyManagementException​(
Throwable
cause)
```

Creates a

KeyManagementException

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

- KeyManagementException

```java
public KeyManagementException()
```

Constructs a KeyManagementException with no detail message. A
detail message is a String that describes this particular
exception.

- KeyManagementException

```java
public KeyManagementException​(
String
msg)
```

Constructs a KeyManagementException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- KeyManagementException

```java
public KeyManagementException​(
String
message,

Throwable
cause)
```

Creates a

KeyManagementException

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

- KeyManagementException

```java
public KeyManagementException​(
Throwable
cause)
```

Creates a

KeyManagementException

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

KeyManagementException

```java
public KeyManagementException()
```

Constructs a KeyManagementException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### KeyManagementException

public KeyManagementException()

Constructs a KeyManagementException with no detail message. A
detail message is a String that describes this particular
exception.

KeyManagementException

```java
public KeyManagementException​(
String
msg)
```

Constructs a KeyManagementException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

---

#### KeyManagementException

public KeyManagementException​(

String

msg)

Constructs a KeyManagementException with the specified detail
message. A detail message is a String that describes this
particular exception.

KeyManagementException

```java
public KeyManagementException​(
String
message,

Throwable
cause)
```

Creates a

KeyManagementException

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

#### KeyManagementException

public KeyManagementException​(

String

message,

Throwable

cause)

Creates a

KeyManagementException

with the specified
detail message and cause.

KeyManagementException

```java
public KeyManagementException​(
Throwable
cause)
```

Creates a

KeyManagementException

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

#### KeyManagementException

public KeyManagementException​(

Throwable

cause)

Creates a

KeyManagementException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

