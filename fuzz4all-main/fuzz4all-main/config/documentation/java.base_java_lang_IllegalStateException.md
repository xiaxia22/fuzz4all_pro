# Class IllegalStateException

**Source:** `java.base\java\lang\IllegalStateException.html`

### Class Description

```java
public class
IllegalStateException

extends
RuntimeException
```

Signals that a method has been invoked at an illegal or
inappropriate time. In other words, the Java environment or
Java application is not in an appropriate state for the requested
operation.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IllegalStateException()

Constructs an IllegalStateException with no detail message.
A detail message is a String that describes this particular exception.

---

#### public IllegalStateException​(
String
s)

Constructs an IllegalStateException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:**
- s

- the String that contains a detailed message

---

#### public IllegalStateException​(
String
message,

Throwable
cause)

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

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

value
is permitted, and indicates that the cause is nonexistent or
unknown.)

**Since:**
- 1.5

---

#### public IllegalStateException​(
Throwable
cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

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

**Since:**
- 1.5

---

### Method Details

*No entries found.*

### Additional Sections

#### Class IllegalStateException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalStateException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalStateException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.IllegalStateException

java.lang.RuntimeException

- java.lang.IllegalStateException

java.lang.IllegalStateException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AcceptPendingException

,

AlreadyBoundException

,

AlreadyConnectedException

,

CancellationException

,

CancelledKeyException

,

ClosedDirectoryStreamException

,

ClosedFileSystemException

,

ClosedSelectorException

,

ClosedWatchServiceException

,

ConnectionPendingException

,

FormatterClosedException

,

IllegalBlockingModeException

,

IllegalComponentStateException

,

IllegalReceiveException

,

IllegalUnbindException

,

InvalidDnDOperationException

,

InvalidMarkException

,

NoConnectionPendingException

,

NonReadableChannelException

,

NonWritableChannelException

,

NotYetBoundException

,

NotYetConnectedException

,

OverlappingFileLockException

,

ReadPendingException

,

ShutdownChannelGroupException

,

WritePendingException

```java
public class
IllegalStateException

extends
RuntimeException
```

Signals that a method has been invoked at an illegal or
inappropriate time. In other words, the Java environment or
Java application is not in an appropriate state for the requested
operation.

**Since:** 1.1
**See Also:** Serialized Form

public class

IllegalStateException

extends

RuntimeException

Signals that a method has been invoked at an illegal or
inappropriate time. In other words, the Java environment or
Java application is not in an appropriate state for the requested
operation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IllegalStateException

()

Constructs an IllegalStateException with no detail message.

IllegalStateException

​(

String

s)

Constructs an IllegalStateException with the specified detail
message.

IllegalStateException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

IllegalStateException

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

IllegalStateException

()

Constructs an IllegalStateException with no detail message.

IllegalStateException

​(

String

s)

Constructs an IllegalStateException with the specified detail
message.

IllegalStateException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

IllegalStateException

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

Constructs an IllegalStateException with no detail message.

Constructs an IllegalStateException with the specified detail
message.

Constructs a new exception with the specified detail message and
cause.

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

- IllegalStateException

```java
public IllegalStateException()
```

Constructs an IllegalStateException with no detail message.
A detail message is a String that describes this particular exception.

- IllegalStateException

```java
public IllegalStateException​(
String
s)
```

Constructs an IllegalStateException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** s

- the String that contains a detailed message

- IllegalStateException

```java
public IllegalStateException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

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

value
is permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

- IllegalStateException

```java
public IllegalStateException​(
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
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

Constructor Detail

- IllegalStateException

```java
public IllegalStateException()
```

Constructs an IllegalStateException with no detail message.
A detail message is a String that describes this particular exception.

- IllegalStateException

```java
public IllegalStateException​(
String
s)
```

Constructs an IllegalStateException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** s

- the String that contains a detailed message

- IllegalStateException

```java
public IllegalStateException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

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

value
is permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

- IllegalStateException

```java
public IllegalStateException​(
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
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### Constructor Detail

IllegalStateException

```java
public IllegalStateException()
```

Constructs an IllegalStateException with no detail message.
A detail message is a String that describes this particular exception.

---

#### IllegalStateException

public IllegalStateException()

Constructs an IllegalStateException with no detail message.
A detail message is a String that describes this particular exception.

IllegalStateException

```java
public IllegalStateException​(
String
s)
```

Constructs an IllegalStateException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** s

- the String that contains a detailed message

---

#### IllegalStateException

public IllegalStateException​(

String

s)

Constructs an IllegalStateException with the specified detail
message. A detail message is a String that describes this particular
exception.

IllegalStateException

```java
public IllegalStateException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

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

value
is permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### IllegalStateException

public IllegalStateException​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

IllegalStateException

```java
public IllegalStateException​(
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
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### IllegalStateException

public IllegalStateException​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

---

