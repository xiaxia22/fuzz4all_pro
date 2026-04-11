# Class DigestException

**Source:** `java.base\java\security\DigestException.html`

### Class Description

```java
public class
DigestException

extends
GeneralSecurityException
```

This is the generic Message Digest exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DigestException()

Constructs a DigestException with no detail message. (A
detail message is a String that describes this particular
exception.)

---

#### public DigestException​(
String
msg)

Constructs a DigestException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:**
- msg

- the detail message.

---

#### public DigestException​(
String
message,

Throwable
cause)

Creates a

DigestException

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

#### public DigestException​(
Throwable
cause)

Creates a

DigestException

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

#### Class DigestException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.DigestException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.DigestException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.DigestException

java.security.GeneralSecurityException

- java.security.DigestException

java.security.DigestException

**All Implemented Interfaces:** Serializable

```java
public class
DigestException

extends
GeneralSecurityException
```

This is the generic Message Digest exception.

**Since:** 1.1
**See Also:** Serialized Form

public class

DigestException

extends

GeneralSecurityException

This is the generic Message Digest exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DigestException

()

Constructs a DigestException with no detail message.

DigestException

​(

String

msg)

Constructs a DigestException with the specified detail
message.

DigestException

​(

String

message,

Throwable

cause)

Creates a

DigestException

with the specified
detail message and cause.

DigestException

​(

Throwable

cause)

Creates a

DigestException

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

DigestException

()

Constructs a DigestException with no detail message.

DigestException

​(

String

msg)

Constructs a DigestException with the specified detail
message.

DigestException

​(

String

message,

Throwable

cause)

Creates a

DigestException

with the specified
detail message and cause.

DigestException

​(

Throwable

cause)

Creates a

DigestException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a DigestException with no detail message.

Constructs a DigestException with the specified detail
message.

Creates a

DigestException

with the specified
detail message and cause.

Creates a

DigestException

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

- DigestException

```java
public DigestException()
```

Constructs a DigestException with no detail message. (A
detail message is a String that describes this particular
exception.)

- DigestException

```java
public DigestException​(
String
msg)
```

Constructs a DigestException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:** msg

- the detail message.

- DigestException

```java
public DigestException​(
String
message,

Throwable
cause)
```

Creates a

DigestException

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

- DigestException

```java
public DigestException​(
Throwable
cause)
```

Creates a

DigestException

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

- DigestException

```java
public DigestException()
```

Constructs a DigestException with no detail message. (A
detail message is a String that describes this particular
exception.)

- DigestException

```java
public DigestException​(
String
msg)
```

Constructs a DigestException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:** msg

- the detail message.

- DigestException

```java
public DigestException​(
String
message,

Throwable
cause)
```

Creates a

DigestException

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

- DigestException

```java
public DigestException​(
Throwable
cause)
```

Creates a

DigestException

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

DigestException

```java
public DigestException()
```

Constructs a DigestException with no detail message. (A
detail message is a String that describes this particular
exception.)

---

#### DigestException

public DigestException()

Constructs a DigestException with no detail message. (A
detail message is a String that describes this particular
exception.)

DigestException

```java
public DigestException​(
String
msg)
```

Constructs a DigestException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:** msg

- the detail message.

---

#### DigestException

public DigestException​(

String

msg)

Constructs a DigestException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

DigestException

```java
public DigestException​(
String
message,

Throwable
cause)
```

Creates a

DigestException

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

#### DigestException

public DigestException​(

String

message,

Throwable

cause)

Creates a

DigestException

with the specified
detail message and cause.

DigestException

```java
public DigestException​(
Throwable
cause)
```

Creates a

DigestException

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

#### DigestException

public DigestException​(

Throwable

cause)

Creates a

DigestException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

