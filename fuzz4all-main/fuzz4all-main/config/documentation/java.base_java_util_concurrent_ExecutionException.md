# Class ExecutionException

**Source:** `java.base\java\util\concurrent\ExecutionException.html`

### Class Description

```java
public class
ExecutionException

extends
Exception
```

Exception thrown when attempting to retrieve the result of a task
that aborted by throwing an exception. This exception can be
inspected using the

Throwable.getCause()

method.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ExecutionException()

Constructs an

ExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

---

#### protected ExecutionException​(
String
message)

Constructs an

ExecutionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:**
- message

- the detail message

---

#### public ExecutionException​(
String
message,

Throwable
cause)

Constructs an

ExecutionException

with the specified detail
message and cause.

**Parameters:**
- message

- the detail message
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### public ExecutionException​(
Throwable
cause)

Constructs an

ExecutionException

with the specified cause.
The detail message is set to

(cause == null ? null :
cause.toString())

(which typically contains the class and
detail message of

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

#### Class ExecutionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.util.concurrent.ExecutionException

java.lang.Throwable

- java.lang.Exception
- - java.util.concurrent.ExecutionException

java.lang.Exception

- java.util.concurrent.ExecutionException

java.util.concurrent.ExecutionException

**All Implemented Interfaces:** Serializable

```java
public class
ExecutionException

extends
Exception
```

Exception thrown when attempting to retrieve the result of a task
that aborted by throwing an exception. This exception can be
inspected using the

Throwable.getCause()

method.

**Since:** 1.5
**See Also:** Future

,

Serialized Form

public class

ExecutionException

extends

Exception

Exception thrown when attempting to retrieve the result of a task
that aborted by throwing an exception. This exception can be
inspected using the

Throwable.getCause()

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ExecutionException

()

Constructs an

ExecutionException

with no detail message.

protected

ExecutionException

​(

String

message)

Constructs an

ExecutionException

with the specified detail
message.

ExecutionException

​(

String

message,

Throwable

cause)

Constructs an

ExecutionException

with the specified detail
message and cause.

ExecutionException

​(

Throwable

cause)

Constructs an

ExecutionException

with the specified cause.

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

Modifier

Constructor

Description

protected

ExecutionException

()

Constructs an

ExecutionException

with no detail message.

protected

ExecutionException

​(

String

message)

Constructs an

ExecutionException

with the specified detail
message.

ExecutionException

​(

String

message,

Throwable

cause)

Constructs an

ExecutionException

with the specified detail
message and cause.

ExecutionException

​(

Throwable

cause)

Constructs an

ExecutionException

with the specified cause.

---

#### Constructor Summary

Constructs an

ExecutionException

with no detail message.

Constructs an

ExecutionException

with the specified detail
message.

Constructs an

ExecutionException

with the specified detail
message and cause.

Constructs an

ExecutionException

with the specified cause.

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

- ExecutionException

```java
protected ExecutionException()
```

Constructs an

ExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

- ExecutionException

```java
protected ExecutionException​(
String
message)
```

Constructs an

ExecutionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:** message

- the detail message

- ExecutionException

```java
public ExecutionException​(
String
message,

Throwable
cause)
```

Constructs an

ExecutionException

with the specified detail
message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

- ExecutionException

```java
public ExecutionException​(
Throwable
cause)
```

Constructs an

ExecutionException

with the specified cause.
The detail message is set to

(cause == null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

Constructor Detail

- ExecutionException

```java
protected ExecutionException()
```

Constructs an

ExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

- ExecutionException

```java
protected ExecutionException​(
String
message)
```

Constructs an

ExecutionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:** message

- the detail message

- ExecutionException

```java
public ExecutionException​(
String
message,

Throwable
cause)
```

Constructs an

ExecutionException

with the specified detail
message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

- ExecutionException

```java
public ExecutionException​(
Throwable
cause)
```

Constructs an

ExecutionException

with the specified cause.
The detail message is set to

(cause == null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### Constructor Detail

ExecutionException

```java
protected ExecutionException()
```

Constructs an

ExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

---

#### ExecutionException

protected ExecutionException()

Constructs an

ExecutionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

ExecutionException

```java
protected ExecutionException​(
String
message)
```

Constructs an

ExecutionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:** message

- the detail message

---

#### ExecutionException

protected ExecutionException​(

String

message)

Constructs an

ExecutionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

ExecutionException

```java
public ExecutionException​(
String
message,

Throwable
cause)
```

Constructs an

ExecutionException

with the specified detail
message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### ExecutionException

public ExecutionException​(

String

message,

Throwable

cause)

Constructs an

ExecutionException

with the specified detail
message and cause.

ExecutionException

```java
public ExecutionException​(
Throwable
cause)
```

Constructs an

ExecutionException

with the specified cause.
The detail message is set to

(cause == null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### ExecutionException

public ExecutionException​(

Throwable

cause)

Constructs an

ExecutionException

with the specified cause.
The detail message is set to

(cause == null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

---

