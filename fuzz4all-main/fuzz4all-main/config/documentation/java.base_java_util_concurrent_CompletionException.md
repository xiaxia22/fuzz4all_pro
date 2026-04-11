# Class CompletionException

**Source:** `java.base\java\util\concurrent\CompletionException.html`

### Class Description

```java
public class
CompletionException

extends
RuntimeException
```

Exception thrown when an error or other exception is encountered
in the course of completing a result or task.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CompletionException()

Constructs a

CompletionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

---

#### protected CompletionException​(
String
message)

Constructs a

CompletionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:**
- message

- the detail message

---

#### public CompletionException​(
String
message,

Throwable
cause)

Constructs a

CompletionException

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

#### public CompletionException​(
Throwable
cause)

Constructs a

CompletionException

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

#### Class CompletionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.util.concurrent.CompletionException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.util.concurrent.CompletionException

java.lang.Exception

- java.lang.RuntimeException
- - java.util.concurrent.CompletionException

java.lang.RuntimeException

- java.util.concurrent.CompletionException

java.util.concurrent.CompletionException

**All Implemented Interfaces:** Serializable

```java
public class
CompletionException

extends
RuntimeException
```

Exception thrown when an error or other exception is encountered
in the course of completing a result or task.

**Since:** 1.8
**See Also:** Serialized Form

public class

CompletionException

extends

RuntimeException

Exception thrown when an error or other exception is encountered
in the course of completing a result or task.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CompletionException

()

Constructs a

CompletionException

with no detail message.

protected

CompletionException

​(

String

message)

Constructs a

CompletionException

with the specified detail
message.

CompletionException

​(

String

message,

Throwable

cause)

Constructs a

CompletionException

with the specified detail
message and cause.

CompletionException

​(

Throwable

cause)

Constructs a

CompletionException

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

CompletionException

()

Constructs a

CompletionException

with no detail message.

protected

CompletionException

​(

String

message)

Constructs a

CompletionException

with the specified detail
message.

CompletionException

​(

String

message,

Throwable

cause)

Constructs a

CompletionException

with the specified detail
message and cause.

CompletionException

​(

Throwable

cause)

Constructs a

CompletionException

with the specified cause.

---

#### Constructor Summary

Constructs a

CompletionException

with no detail message.

Constructs a

CompletionException

with the specified detail
message.

Constructs a

CompletionException

with the specified detail
message and cause.

Constructs a

CompletionException

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

- CompletionException

```java
protected CompletionException()
```

Constructs a

CompletionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

- CompletionException

```java
protected CompletionException​(
String
message)
```

Constructs a

CompletionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:** message

- the detail message

- CompletionException

```java
public CompletionException​(
String
message,

Throwable
cause)
```

Constructs a

CompletionException

with the specified detail
message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

- CompletionException

```java
public CompletionException​(
Throwable
cause)
```

Constructs a

CompletionException

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

- CompletionException

```java
protected CompletionException()
```

Constructs a

CompletionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

- CompletionException

```java
protected CompletionException​(
String
message)
```

Constructs a

CompletionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:** message

- the detail message

- CompletionException

```java
public CompletionException​(
String
message,

Throwable
cause)
```

Constructs a

CompletionException

with the specified detail
message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

- CompletionException

```java
public CompletionException​(
Throwable
cause)
```

Constructs a

CompletionException

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

CompletionException

```java
protected CompletionException()
```

Constructs a

CompletionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

---

#### CompletionException

protected CompletionException()

Constructs a

CompletionException

with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

CompletionException

```java
protected CompletionException​(
String
message)
```

Constructs a

CompletionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

**Parameters:** message

- the detail message

---

#### CompletionException

protected CompletionException​(

String

message)

Constructs a

CompletionException

with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to

initCause

.

CompletionException

```java
public CompletionException​(
String
message,

Throwable
cause)
```

Constructs a

CompletionException

with the specified detail
message and cause.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method)

---

#### CompletionException

public CompletionException​(

String

message,

Throwable

cause)

Constructs a

CompletionException

with the specified detail
message and cause.

CompletionException

```java
public CompletionException​(
Throwable
cause)
```

Constructs a

CompletionException

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

#### CompletionException

public CompletionException​(

Throwable

cause)

Constructs a

CompletionException

with the specified cause.
The detail message is set to

(cause == null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

---

