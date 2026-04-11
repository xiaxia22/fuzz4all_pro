# Class ReflectiveOperationException

**Source:** `java.base\java\lang\ReflectiveOperationException.html`

### Class Description

```java
public class
ReflectiveOperationException

extends
Exception
```

Common superclass of exceptions thrown by reflective operations in
core reflection.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ReflectiveOperationException()

Constructs a new exception with

null

as its detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

---

#### public ReflectiveOperationException​(
String
message)

Constructs a new exception with the specified detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:**
- message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

---

#### public ReflectiveOperationException​(
String
message,

Throwable
cause)

Constructs a new exception with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

---

#### public ReflectiveOperationException​(
Throwable
cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:**
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ReflectiveOperationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.ReflectiveOperationException

java.lang.Throwable

- java.lang.Exception
- - java.lang.ReflectiveOperationException

java.lang.Exception

- java.lang.ReflectiveOperationException

java.lang.ReflectiveOperationException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** ClassNotFoundException

,

IllegalAccessException

,

InstantiationException

,

InvocationTargetException

,

NoSuchFieldException

,

NoSuchMethodException

```java
public class
ReflectiveOperationException

extends
Exception
```

Common superclass of exceptions thrown by reflective operations in
core reflection.

**Since:** 1.7
**See Also:** LinkageError

,

Serialized Form

public class

ReflectiveOperationException

extends

Exception

Common superclass of exceptions thrown by reflective operations in
core reflection.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ReflectiveOperationException

()

Constructs a new exception with

null

as its detail
message.

ReflectiveOperationException

​(

String

message)

Constructs a new exception with the specified detail message.

ReflectiveOperationException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message
and cause.

ReflectiveOperationException

​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

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

ReflectiveOperationException

()

Constructs a new exception with

null

as its detail
message.

ReflectiveOperationException

​(

String

message)

Constructs a new exception with the specified detail message.

ReflectiveOperationException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message
and cause.

ReflectiveOperationException

​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a new exception with

null

as its detail
message.

Constructs a new exception with the specified detail message.

Constructs a new exception with the specified detail message
and cause.

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

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

- ReflectiveOperationException

```java
public ReflectiveOperationException()
```

Constructs a new exception with

null

as its detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

- ReflectiveOperationException

```java
public ReflectiveOperationException​(
String
message)
```

Constructs a new exception with the specified detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- ReflectiveOperationException

```java
public ReflectiveOperationException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

- ReflectiveOperationException

```java
public ReflectiveOperationException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

Constructor Detail

- ReflectiveOperationException

```java
public ReflectiveOperationException()
```

Constructs a new exception with

null

as its detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

- ReflectiveOperationException

```java
public ReflectiveOperationException​(
String
message)
```

Constructs a new exception with the specified detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- ReflectiveOperationException

```java
public ReflectiveOperationException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

- ReflectiveOperationException

```java
public ReflectiveOperationException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

---

#### Constructor Detail

ReflectiveOperationException

```java
public ReflectiveOperationException()
```

Constructs a new exception with

null

as its detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

---

#### ReflectiveOperationException

public ReflectiveOperationException()

Constructs a new exception with

null

as its detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

ReflectiveOperationException

```java
public ReflectiveOperationException​(
String
message)
```

Constructs a new exception with the specified detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

---

#### ReflectiveOperationException

public ReflectiveOperationException​(

String

message)

Constructs a new exception with the specified detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

ReflectiveOperationException

```java
public ReflectiveOperationException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

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

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

---

#### ReflectiveOperationException

public ReflectiveOperationException​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

ReflectiveOperationException

```java
public ReflectiveOperationException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

---

#### ReflectiveOperationException

public ReflectiveOperationException​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

