# Class InvalidAlgorithmParameterException

**Source:** `java.base\java\security\InvalidAlgorithmParameterException.html`

### Class Description

```java
public class
InvalidAlgorithmParameterException

extends
GeneralSecurityException
```

This is the exception for invalid or inappropriate algorithm parameters.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidAlgorithmParameterException()

Constructs an InvalidAlgorithmParameterException with no detail
message.
A detail message is a String that describes this particular
exception.

---

#### public InvalidAlgorithmParameterException​(
String
msg)

Constructs an InvalidAlgorithmParameterException with the specified
detail message.
A detail message is a String that describes this
particular exception.

**Parameters:**
- msg

- the detail message.

---

#### public InvalidAlgorithmParameterException​(
String
message,

Throwable
cause)

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

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

#### public InvalidAlgorithmParameterException​(
Throwable
cause)

Creates an

InvalidAlgorithmParameterException

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

#### Class InvalidAlgorithmParameterException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.InvalidAlgorithmParameterException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.InvalidAlgorithmParameterException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.InvalidAlgorithmParameterException

java.security.GeneralSecurityException

- java.security.InvalidAlgorithmParameterException

java.security.InvalidAlgorithmParameterException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidAlgorithmParameterException

extends
GeneralSecurityException
```

This is the exception for invalid or inappropriate algorithm parameters.

**Since:** 1.2
**See Also:** AlgorithmParameters

,

AlgorithmParameterSpec

,

Serialized Form

public class

InvalidAlgorithmParameterException

extends

GeneralSecurityException

This is the exception for invalid or inappropriate algorithm parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InvalidAlgorithmParameterException

()

Constructs an InvalidAlgorithmParameterException with no detail
message.

InvalidAlgorithmParameterException

​(

String

msg)

Constructs an InvalidAlgorithmParameterException with the specified
detail message.

InvalidAlgorithmParameterException

​(

String

message,

Throwable

cause)

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

InvalidAlgorithmParameterException

​(

Throwable

cause)

Creates an

InvalidAlgorithmParameterException

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

InvalidAlgorithmParameterException

()

Constructs an InvalidAlgorithmParameterException with no detail
message.

InvalidAlgorithmParameterException

​(

String

msg)

Constructs an InvalidAlgorithmParameterException with the specified
detail message.

InvalidAlgorithmParameterException

​(

String

message,

Throwable

cause)

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

InvalidAlgorithmParameterException

​(

Throwable

cause)

Creates an

InvalidAlgorithmParameterException

with the
specified cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs an InvalidAlgorithmParameterException with no detail
message.

Constructs an InvalidAlgorithmParameterException with the specified
detail message.

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

Creates an

InvalidAlgorithmParameterException

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

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException()
```

Constructs an InvalidAlgorithmParameterException with no detail
message.
A detail message is a String that describes this particular
exception.

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
String
msg)
```

Constructs an InvalidAlgorithmParameterException with the specified
detail message.
A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
String
message,

Throwable
cause)
```

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

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

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
Throwable
cause)
```

Creates an

InvalidAlgorithmParameterException

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

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException()
```

Constructs an InvalidAlgorithmParameterException with no detail
message.
A detail message is a String that describes this particular
exception.

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
String
msg)
```

Constructs an InvalidAlgorithmParameterException with the specified
detail message.
A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
String
message,

Throwable
cause)
```

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

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

- InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
Throwable
cause)
```

Creates an

InvalidAlgorithmParameterException

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

InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException()
```

Constructs an InvalidAlgorithmParameterException with no detail
message.
A detail message is a String that describes this particular
exception.

---

#### InvalidAlgorithmParameterException

public InvalidAlgorithmParameterException()

Constructs an InvalidAlgorithmParameterException with no detail
message.
A detail message is a String that describes this particular
exception.

InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
String
msg)
```

Constructs an InvalidAlgorithmParameterException with the specified
detail message.
A detail message is a String that describes this
particular exception.

**Parameters:** msg

- the detail message.

---

#### InvalidAlgorithmParameterException

public InvalidAlgorithmParameterException​(

String

msg)

Constructs an InvalidAlgorithmParameterException with the specified
detail message.
A detail message is a String that describes this
particular exception.

InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
String
message,

Throwable
cause)
```

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

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

#### InvalidAlgorithmParameterException

public InvalidAlgorithmParameterException​(

String

message,

Throwable

cause)

Creates an

InvalidAlgorithmParameterException

with the
specified detail message and cause.

InvalidAlgorithmParameterException

```java
public InvalidAlgorithmParameterException​(
Throwable
cause)
```

Creates an

InvalidAlgorithmParameterException

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

#### InvalidAlgorithmParameterException

public InvalidAlgorithmParameterException​(

Throwable

cause)

Creates an

InvalidAlgorithmParameterException

with the
specified cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

