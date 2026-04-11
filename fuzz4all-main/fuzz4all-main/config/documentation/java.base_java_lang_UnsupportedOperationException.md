# Class UnsupportedOperationException

**Source:** `java.base\java\lang\UnsupportedOperationException.html`

### Class Description

```java
public class
UnsupportedOperationException

extends
RuntimeException
```

Thrown to indicate that the requested operation is not supported.

This class is a member of the

Java Collections Framework

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnsupportedOperationException()

Constructs an UnsupportedOperationException with no detail message.

---

#### public UnsupportedOperationException​(
String
message)

Constructs an UnsupportedOperationException with the specified
detail message.

**Parameters:**
- message

- the detail message

---

#### public UnsupportedOperationException​(
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

#### public UnsupportedOperationException​(
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

#### Class UnsupportedOperationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.UnsupportedOperationException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.UnsupportedOperationException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.UnsupportedOperationException

java.lang.RuntimeException

- java.lang.UnsupportedOperationException

java.lang.UnsupportedOperationException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** HeadlessException

,

ReadOnlyBufferException

,

ReadOnlyFileSystemException

,

VMCannotBeModifiedException

```java
public class
UnsupportedOperationException

extends
RuntimeException
```

Thrown to indicate that the requested operation is not supported.

This class is a member of the

Java Collections Framework

.

**Since:** 1.2
**See Also:** Serialized Form

public class

UnsupportedOperationException

extends

RuntimeException

Thrown to indicate that the requested operation is not supported.

This class is a member of the

Java Collections Framework

.

This class is a member of the

Java Collections Framework

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnsupportedOperationException

()

Constructs an UnsupportedOperationException with no detail message.

UnsupportedOperationException

​(

String

message)

Constructs an UnsupportedOperationException with the specified
detail message.

UnsupportedOperationException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

UnsupportedOperationException

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

UnsupportedOperationException

()

Constructs an UnsupportedOperationException with no detail message.

UnsupportedOperationException

​(

String

message)

Constructs an UnsupportedOperationException with the specified
detail message.

UnsupportedOperationException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

UnsupportedOperationException

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

Constructs an UnsupportedOperationException with no detail message.

Constructs an UnsupportedOperationException with the specified
detail message.

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

- UnsupportedOperationException

```java
public UnsupportedOperationException()
```

Constructs an UnsupportedOperationException with no detail message.

- UnsupportedOperationException

```java
public UnsupportedOperationException​(
String
message)
```

Constructs an UnsupportedOperationException with the specified
detail message.

**Parameters:** message

- the detail message

- UnsupportedOperationException

```java
public UnsupportedOperationException​(
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

- UnsupportedOperationException

```java
public UnsupportedOperationException​(
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

- UnsupportedOperationException

```java
public UnsupportedOperationException()
```

Constructs an UnsupportedOperationException with no detail message.

- UnsupportedOperationException

```java
public UnsupportedOperationException​(
String
message)
```

Constructs an UnsupportedOperationException with the specified
detail message.

**Parameters:** message

- the detail message

- UnsupportedOperationException

```java
public UnsupportedOperationException​(
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

- UnsupportedOperationException

```java
public UnsupportedOperationException​(
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

UnsupportedOperationException

```java
public UnsupportedOperationException()
```

Constructs an UnsupportedOperationException with no detail message.

---

#### UnsupportedOperationException

public UnsupportedOperationException()

Constructs an UnsupportedOperationException with no detail message.

UnsupportedOperationException

```java
public UnsupportedOperationException​(
String
message)
```

Constructs an UnsupportedOperationException with the specified
detail message.

**Parameters:** message

- the detail message

---

#### UnsupportedOperationException

public UnsupportedOperationException​(

String

message)

Constructs an UnsupportedOperationException with the specified
detail message.

UnsupportedOperationException

```java
public UnsupportedOperationException​(
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

#### UnsupportedOperationException

public UnsupportedOperationException​(

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

UnsupportedOperationException

```java
public UnsupportedOperationException​(
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

#### UnsupportedOperationException

public UnsupportedOperationException​(

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

