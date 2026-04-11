# Class InternalError

**Source:** `java.base\java\lang\InternalError.html`

### Class Description

```java
public class
InternalError

extends
VirtualMachineError
```

Thrown to indicate some unexpected internal error has occurred in
the Java Virtual Machine.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InternalError()

Constructs an

InternalError

with no detail message.

---

#### public InternalError​(
String
message)

Constructs an

InternalError

with the specified
detail message.

**Parameters:**
- message

- the detail message.

---

#### public InternalError​(
String
message,

Throwable
cause)

Constructs an

InternalError

with the specified detail
message and cause.

Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

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

**Since:**
- 1.8

---

#### public InternalError​(
Throwable
cause)

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

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

**Since:**
- 1.8

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InternalError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - java.lang.VirtualMachineError
- - java.lang.InternalError

java.lang.Throwable

- java.lang.Error
- - java.lang.VirtualMachineError
- - java.lang.InternalError

java.lang.Error

- java.lang.VirtualMachineError
- - java.lang.InternalError

java.lang.VirtualMachineError

- java.lang.InternalError

java.lang.InternalError

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** ZipError

```java
public class
InternalError

extends
VirtualMachineError
```

Thrown to indicate some unexpected internal error has occurred in
the Java Virtual Machine.

**Since:** 1.0
**See Also:** Serialized Form

public class

InternalError

extends

VirtualMachineError

Thrown to indicate some unexpected internal error has occurred in
the Java Virtual Machine.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InternalError

()

Constructs an

InternalError

with no detail message.

InternalError

​(

String

message)

Constructs an

InternalError

with the specified
detail message.

InternalError

​(

String

message,

Throwable

cause)

Constructs an

InternalError

with the specified detail
message and cause.

InternalError

​(

Throwable

cause)

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

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

InternalError

()

Constructs an

InternalError

with no detail message.

InternalError

​(

String

message)

Constructs an

InternalError

with the specified
detail message.

InternalError

​(

String

message,

Throwable

cause)

Constructs an

InternalError

with the specified detail
message and cause.

InternalError

​(

Throwable

cause)

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

---

#### Constructor Summary

Constructs an

InternalError

with no detail message.

Constructs an

InternalError

with the specified
detail message.

Constructs an

InternalError

with the specified detail
message and cause.

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

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

- InternalError

```java
public InternalError()
```

Constructs an

InternalError

with no detail message.

- InternalError

```java
public InternalError​(
String
message)
```

Constructs an

InternalError

with the specified
detail message.

**Parameters:** message

- the detail message.

- InternalError

```java
public InternalError​(
String
message,

Throwable
cause)
```

Constructs an

InternalError

with the specified detail
message and cause.

Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

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
**Since:** 1.8

- InternalError

```java
public InternalError​(
Throwable
cause)
```

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

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
**Since:** 1.8

Constructor Detail

- InternalError

```java
public InternalError()
```

Constructs an

InternalError

with no detail message.

- InternalError

```java
public InternalError​(
String
message)
```

Constructs an

InternalError

with the specified
detail message.

**Parameters:** message

- the detail message.

- InternalError

```java
public InternalError​(
String
message,

Throwable
cause)
```

Constructs an

InternalError

with the specified detail
message and cause.

Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

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
**Since:** 1.8

- InternalError

```java
public InternalError​(
Throwable
cause)
```

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

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
**Since:** 1.8

---

#### Constructor Detail

InternalError

```java
public InternalError()
```

Constructs an

InternalError

with no detail message.

---

#### InternalError

public InternalError()

Constructs an

InternalError

with no detail message.

InternalError

```java
public InternalError​(
String
message)
```

Constructs an

InternalError

with the specified
detail message.

**Parameters:** message

- the detail message.

---

#### InternalError

public InternalError​(

String

message)

Constructs an

InternalError

with the specified
detail message.

InternalError

```java
public InternalError​(
String
message,

Throwable
cause)
```

Constructs an

InternalError

with the specified detail
message and cause.

Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

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
**Since:** 1.8

---

#### InternalError

public InternalError​(

String

message,

Throwable

cause)

Constructs an

InternalError

with the specified detail
message and cause.

Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

InternalError

```java
public InternalError​(
Throwable
cause)
```

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

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
**Since:** 1.8

---

#### InternalError

public InternalError​(

Throwable

cause)

Constructs an

InternalError

with the specified cause
and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

---

