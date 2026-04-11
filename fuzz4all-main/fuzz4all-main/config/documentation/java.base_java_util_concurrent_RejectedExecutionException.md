# Class RejectedExecutionException

**Source:** `java.base\java\util\concurrent\RejectedExecutionException.html`

### Class Description

```java
public class
RejectedExecutionException

extends
RuntimeException
```

Exception thrown by an

Executor

when a task cannot be
accepted for execution.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RejectedExecutionException()

Constructs a

RejectedExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

---

#### public RejectedExecutionException​(
String
message)

Constructs a

RejectedExecutionException

with the
specified detail message. The cause is not initialized, and may
subsequently be initialized by a call to

initCause

.

**Parameters:**
- message

- the detail message

---

#### public RejectedExecutionException​(
String
message,

Throwable
cause)

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

**Parameters:**
- message

- the detail message
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### public RejectedExecutionException​(
Throwable
cause)

Constructs a

RejectedExecutionException

with the
specified cause. The detail message is set to

(cause ==
null ? null : cause.toString())

(which typically contains
the class and detail message of

cause

).

**Parameters:**
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

### Method Details

*No entries found.*

### Additional Sections

#### Class RejectedExecutionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.util.concurrent.RejectedExecutionException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.util.concurrent.RejectedExecutionException

java.lang.Exception

- java.lang.RuntimeException
- - java.util.concurrent.RejectedExecutionException

java.lang.RuntimeException

- java.util.concurrent.RejectedExecutionException

java.util.concurrent.RejectedExecutionException

**All Implemented Interfaces:** Serializable

```java
public class
RejectedExecutionException

extends
RuntimeException
```

Exception thrown by an

Executor

when a task cannot be
accepted for execution.

**Since:** 1.5
**See Also:** Serialized Form

public class

RejectedExecutionException

extends

RuntimeException

Exception thrown by an

Executor

when a task cannot be
accepted for execution.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RejectedExecutionException

()

Constructs a

RejectedExecutionException

with no detail message.

RejectedExecutionException

​(

String

message)

Constructs a

RejectedExecutionException

with the
specified detail message.

RejectedExecutionException

​(

String

message,

Throwable

cause)

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

RejectedExecutionException

​(

Throwable

cause)

Constructs a

RejectedExecutionException

with the
specified cause.

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

RejectedExecutionException

()

Constructs a

RejectedExecutionException

with no detail message.

RejectedExecutionException

​(

String

message)

Constructs a

RejectedExecutionException

with the
specified detail message.

RejectedExecutionException

​(

String

message,

Throwable

cause)

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

RejectedExecutionException

​(

Throwable

cause)

Constructs a

RejectedExecutionException

with the
specified cause.

---

#### Constructor Summary

Constructs a

RejectedExecutionException

with no detail message.

Constructs a

RejectedExecutionException

with the
specified detail message.

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

Constructs a

RejectedExecutionException

with the
specified cause.

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

- RejectedExecutionException

```java
public RejectedExecutionException()
```

Constructs a

RejectedExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

- RejectedExecutionException

```java
public RejectedExecutionException​(
String
message)
```

Constructs a

RejectedExecutionException

with the
specified detail message. The cause is not initialized, and may
subsequently be initialized by a call to

initCause

.

**Parameters:** message

- the detail message

- RejectedExecutionException

```java
public RejectedExecutionException​(
String
message,

Throwable
cause)
```

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

- RejectedExecutionException

```java
public RejectedExecutionException​(
Throwable
cause)
```

Constructs a

RejectedExecutionException

with the
specified cause. The detail message is set to

(cause ==
null ? null : cause.toString())

(which typically contains
the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

Constructor Detail

- RejectedExecutionException

```java
public RejectedExecutionException()
```

Constructs a

RejectedExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

- RejectedExecutionException

```java
public RejectedExecutionException​(
String
message)
```

Constructs a

RejectedExecutionException

with the
specified detail message. The cause is not initialized, and may
subsequently be initialized by a call to

initCause

.

**Parameters:** message

- the detail message

- RejectedExecutionException

```java
public RejectedExecutionException​(
String
message,

Throwable
cause)
```

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

- RejectedExecutionException

```java
public RejectedExecutionException​(
Throwable
cause)
```

Constructs a

RejectedExecutionException

with the
specified cause. The detail message is set to

(cause ==
null ? null : cause.toString())

(which typically contains
the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### Constructor Detail

RejectedExecutionException

```java
public RejectedExecutionException()
```

Constructs a

RejectedExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

---

#### RejectedExecutionException

public RejectedExecutionException()

Constructs a

RejectedExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

RejectedExecutionException

```java
public RejectedExecutionException​(
String
message)
```

Constructs a

RejectedExecutionException

with the
specified detail message. The cause is not initialized, and may
subsequently be initialized by a call to

initCause

.

**Parameters:** message

- the detail message

---

#### RejectedExecutionException

public RejectedExecutionException​(

String

message)

Constructs a

RejectedExecutionException

with the
specified detail message. The cause is not initialized, and may
subsequently be initialized by a call to

initCause

.

RejectedExecutionException

```java
public RejectedExecutionException​(
String
message,

Throwable
cause)
```

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### RejectedExecutionException

public RejectedExecutionException​(

String

message,

Throwable

cause)

Constructs a

RejectedExecutionException

with the
specified detail message and cause.

RejectedExecutionException

```java
public RejectedExecutionException​(
Throwable
cause)
```

Constructs a

RejectedExecutionException

with the
specified cause. The detail message is set to

(cause ==
null ? null : cause.toString())

(which typically contains
the class and detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### RejectedExecutionException

public RejectedExecutionException​(

Throwable

cause)

Constructs a

RejectedExecutionException

with the
specified cause. The detail message is set to

(cause ==
null ? null : cause.toString())

(which typically contains
the class and detail message of

cause

).

---

