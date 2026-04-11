# Class KeyException

**Source:** `java.base\java\security\KeyException.html`

### Class Description

```java
public class
KeyException

extends
GeneralSecurityException
```

This is the basic key exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyException()

Constructs a KeyException with no detail message. A detail
message is a String that describes this particular exception.

---

#### public KeyException​(
String
msg)

Constructs a KeyException with the specified detail message.
A detail message is a String that describes this particular
exception.

**Parameters:**
- msg

- the detail message.

---

#### public KeyException​(
String
message,

Throwable
cause)

Creates a

KeyException

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

#### public KeyException​(
Throwable
cause)

Creates a

KeyException

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

#### Class KeyException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.KeyException

java.security.GeneralSecurityException

- java.security.KeyException

java.security.KeyException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** InvalidKeyException

,

KeyManagementException

```java
public class
KeyException

extends
GeneralSecurityException
```

This is the basic key exception.

**Since:** 1.1
**See Also:** Key

,

InvalidKeyException

,

KeyManagementException

,

Serialized Form

public class

KeyException

extends

GeneralSecurityException

This is the basic key exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyException

()

Constructs a KeyException with no detail message.

KeyException

​(

String

msg)

Constructs a KeyException with the specified detail message.

KeyException

​(

String

message,

Throwable

cause)

Creates a

KeyException

with the specified
detail message and cause.

KeyException

​(

Throwable

cause)

Creates a

KeyException

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

KeyException

()

Constructs a KeyException with no detail message.

KeyException

​(

String

msg)

Constructs a KeyException with the specified detail message.

KeyException

​(

String

message,

Throwable

cause)

Creates a

KeyException

with the specified
detail message and cause.

KeyException

​(

Throwable

cause)

Creates a

KeyException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a KeyException with no detail message.

Constructs a KeyException with the specified detail message.

Creates a

KeyException

with the specified
detail message and cause.

Creates a

KeyException

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

- KeyException

```java
public KeyException()
```

Constructs a KeyException with no detail message. A detail
message is a String that describes this particular exception.

- KeyException

```java
public KeyException​(
String
msg)
```

Constructs a KeyException with the specified detail message.
A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

- KeyException

```java
public KeyException​(
String
message,

Throwable
cause)
```

Creates a

KeyException

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

- KeyException

```java
public KeyException​(
Throwable
cause)
```

Creates a

KeyException

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

- KeyException

```java
public KeyException()
```

Constructs a KeyException with no detail message. A detail
message is a String that describes this particular exception.

- KeyException

```java
public KeyException​(
String
msg)
```

Constructs a KeyException with the specified detail message.
A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

- KeyException

```java
public KeyException​(
String
message,

Throwable
cause)
```

Creates a

KeyException

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

- KeyException

```java
public KeyException​(
Throwable
cause)
```

Creates a

KeyException

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

KeyException

```java
public KeyException()
```

Constructs a KeyException with no detail message. A detail
message is a String that describes this particular exception.

---

#### KeyException

public KeyException()

Constructs a KeyException with no detail message. A detail
message is a String that describes this particular exception.

KeyException

```java
public KeyException​(
String
msg)
```

Constructs a KeyException with the specified detail message.
A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

---

#### KeyException

public KeyException​(

String

msg)

Constructs a KeyException with the specified detail message.
A detail message is a String that describes this particular
exception.

KeyException

```java
public KeyException​(
String
message,

Throwable
cause)
```

Creates a

KeyException

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

#### KeyException

public KeyException​(

String

message,

Throwable

cause)

Creates a

KeyException

with the specified
detail message and cause.

KeyException

```java
public KeyException​(
Throwable
cause)
```

Creates a

KeyException

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

#### KeyException

public KeyException​(

Throwable

cause)

Creates a

KeyException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

