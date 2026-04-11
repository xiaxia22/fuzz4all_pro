# Class KeyStoreException

**Source:** `java.base\java\security\KeyStoreException.html`

### Class Description

```java
public class
KeyStoreException

extends
GeneralSecurityException
```

This is the generic KeyStore exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyStoreException()

Constructs a KeyStoreException with no detail message. (A
detail message is a String that describes this particular
exception.)

---

#### public KeyStoreException​(
String
msg)

Constructs a KeyStoreException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:**
- msg

- the detail message.

---

#### public KeyStoreException​(
String
message,

Throwable
cause)

Creates a

KeyStoreException

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

#### public KeyStoreException​(
Throwable
cause)

Creates a

KeyStoreException

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

#### Class KeyStoreException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyStoreException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.KeyStoreException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.KeyStoreException

java.security.GeneralSecurityException

- java.security.KeyStoreException

java.security.KeyStoreException

**All Implemented Interfaces:** Serializable

```java
public class
KeyStoreException

extends
GeneralSecurityException
```

This is the generic KeyStore exception.

**Since:** 1.2
**See Also:** Serialized Form

public class

KeyStoreException

extends

GeneralSecurityException

This is the generic KeyStore exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyStoreException

()

Constructs a KeyStoreException with no detail message.

KeyStoreException

​(

String

msg)

Constructs a KeyStoreException with the specified detail
message.

KeyStoreException

​(

String

message,

Throwable

cause)

Creates a

KeyStoreException

with the specified
detail message and cause.

KeyStoreException

​(

Throwable

cause)

Creates a

KeyStoreException

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

KeyStoreException

()

Constructs a KeyStoreException with no detail message.

KeyStoreException

​(

String

msg)

Constructs a KeyStoreException with the specified detail
message.

KeyStoreException

​(

String

message,

Throwable

cause)

Creates a

KeyStoreException

with the specified
detail message and cause.

KeyStoreException

​(

Throwable

cause)

Creates a

KeyStoreException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a KeyStoreException with no detail message.

Constructs a KeyStoreException with the specified detail
message.

Creates a

KeyStoreException

with the specified
detail message and cause.

Creates a

KeyStoreException

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

- KeyStoreException

```java
public KeyStoreException()
```

Constructs a KeyStoreException with no detail message. (A
detail message is a String that describes this particular
exception.)

- KeyStoreException

```java
public KeyStoreException​(
String
msg)
```

Constructs a KeyStoreException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:** msg

- the detail message.

- KeyStoreException

```java
public KeyStoreException​(
String
message,

Throwable
cause)
```

Creates a

KeyStoreException

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

- KeyStoreException

```java
public KeyStoreException​(
Throwable
cause)
```

Creates a

KeyStoreException

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

- KeyStoreException

```java
public KeyStoreException()
```

Constructs a KeyStoreException with no detail message. (A
detail message is a String that describes this particular
exception.)

- KeyStoreException

```java
public KeyStoreException​(
String
msg)
```

Constructs a KeyStoreException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:** msg

- the detail message.

- KeyStoreException

```java
public KeyStoreException​(
String
message,

Throwable
cause)
```

Creates a

KeyStoreException

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

- KeyStoreException

```java
public KeyStoreException​(
Throwable
cause)
```

Creates a

KeyStoreException

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

KeyStoreException

```java
public KeyStoreException()
```

Constructs a KeyStoreException with no detail message. (A
detail message is a String that describes this particular
exception.)

---

#### KeyStoreException

public KeyStoreException()

Constructs a KeyStoreException with no detail message. (A
detail message is a String that describes this particular
exception.)

KeyStoreException

```java
public KeyStoreException​(
String
msg)
```

Constructs a KeyStoreException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

**Parameters:** msg

- the detail message.

---

#### KeyStoreException

public KeyStoreException​(

String

msg)

Constructs a KeyStoreException with the specified detail
message. (A detail message is a String that describes this
particular exception.)

KeyStoreException

```java
public KeyStoreException​(
String
message,

Throwable
cause)
```

Creates a

KeyStoreException

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

#### KeyStoreException

public KeyStoreException​(

String

message,

Throwable

cause)

Creates a

KeyStoreException

with the specified
detail message and cause.

KeyStoreException

```java
public KeyStoreException​(
Throwable
cause)
```

Creates a

KeyStoreException

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

#### KeyStoreException

public KeyStoreException​(

Throwable

cause)

Creates a

KeyStoreException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

