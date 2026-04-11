# Class SecurityException

**Source:** `java.base\java\lang\SecurityException.html`

### Class Description

```java
public class
SecurityException

extends
RuntimeException
```

Thrown by the security manager to indicate a security violation.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SecurityException()

Constructs a

SecurityException

with no detail message.

---

#### public SecurityException​(
String
s)

Constructs a

SecurityException

with the specified
detail message.

**Parameters:**
- s

- the detail message.

---

#### public SecurityException​(
String
message,

Throwable
cause)

Creates a

SecurityException

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

#### public SecurityException​(
Throwable
cause)

Creates a

SecurityException

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

#### Class SecurityException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.SecurityException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.SecurityException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.SecurityException

java.lang.RuntimeException

- java.lang.SecurityException

java.lang.SecurityException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AccessControlException

,

RMISecurityException

```java
public class
SecurityException

extends
RuntimeException
```

Thrown by the security manager to indicate a security violation.

**Since:** 1.0
**See Also:** SecurityManager

,

Serialized Form

public class

SecurityException

extends

RuntimeException

Thrown by the security manager to indicate a security violation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SecurityException

()

Constructs a

SecurityException

with no detail message.

SecurityException

​(

String

s)

Constructs a

SecurityException

with the specified
detail message.

SecurityException

​(

String

message,

Throwable

cause)

Creates a

SecurityException

with the specified
detail message and cause.

SecurityException

​(

Throwable

cause)

Creates a

SecurityException

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

SecurityException

()

Constructs a

SecurityException

with no detail message.

SecurityException

​(

String

s)

Constructs a

SecurityException

with the specified
detail message.

SecurityException

​(

String

message,

Throwable

cause)

Creates a

SecurityException

with the specified
detail message and cause.

SecurityException

​(

Throwable

cause)

Creates a

SecurityException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a

SecurityException

with no detail message.

Constructs a

SecurityException

with the specified
detail message.

Creates a

SecurityException

with the specified
detail message and cause.

Creates a

SecurityException

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

- SecurityException

```java
public SecurityException()
```

Constructs a

SecurityException

with no detail message.

- SecurityException

```java
public SecurityException​(
String
s)
```

Constructs a

SecurityException

with the specified
detail message.

**Parameters:** s

- the detail message.

- SecurityException

```java
public SecurityException​(
String
message,

Throwable
cause)
```

Creates a

SecurityException

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

- SecurityException

```java
public SecurityException​(
Throwable
cause)
```

Creates a

SecurityException

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

- SecurityException

```java
public SecurityException()
```

Constructs a

SecurityException

with no detail message.

- SecurityException

```java
public SecurityException​(
String
s)
```

Constructs a

SecurityException

with the specified
detail message.

**Parameters:** s

- the detail message.

- SecurityException

```java
public SecurityException​(
String
message,

Throwable
cause)
```

Creates a

SecurityException

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

- SecurityException

```java
public SecurityException​(
Throwable
cause)
```

Creates a

SecurityException

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

SecurityException

```java
public SecurityException()
```

Constructs a

SecurityException

with no detail message.

---

#### SecurityException

public SecurityException()

Constructs a

SecurityException

with no detail message.

SecurityException

```java
public SecurityException​(
String
s)
```

Constructs a

SecurityException

with the specified
detail message.

**Parameters:** s

- the detail message.

---

#### SecurityException

public SecurityException​(

String

s)

Constructs a

SecurityException

with the specified
detail message.

SecurityException

```java
public SecurityException​(
String
message,

Throwable
cause)
```

Creates a

SecurityException

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

#### SecurityException

public SecurityException​(

String

message,

Throwable

cause)

Creates a

SecurityException

with the specified
detail message and cause.

SecurityException

```java
public SecurityException​(
Throwable
cause)
```

Creates a

SecurityException

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

#### SecurityException

public SecurityException​(

Throwable

cause)

Creates a

SecurityException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

