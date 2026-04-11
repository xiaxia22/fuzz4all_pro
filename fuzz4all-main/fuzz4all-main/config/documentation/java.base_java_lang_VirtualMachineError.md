# Class VirtualMachineError

**Source:** `java.base\java\lang\VirtualMachineError.html`

### Class Description

```java
public abstract class
VirtualMachineError

extends
Error
```

Thrown to indicate that the Java Virtual Machine is broken or has
run out of resources necessary for it to continue operating.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public VirtualMachineError()

Constructs a

VirtualMachineError

with no detail message.

---

#### public VirtualMachineError​(
String
message)

Constructs a

VirtualMachineError

with the specified
detail message.

**Parameters:**
- message

- the detail message.

---

#### public VirtualMachineError​(
String
message,

Throwable
cause)

Constructs a

VirtualMachineError

with the specified
detail message and cause.

Note that the detail message
associated with

cause

is

not

automatically
incorporated in this error's detail message.

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

#### public VirtualMachineError​(
Throwable
cause)

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

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

#### Class VirtualMachineError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - java.lang.VirtualMachineError

java.lang.Throwable

- java.lang.Error
- - java.lang.VirtualMachineError

java.lang.Error

- java.lang.VirtualMachineError

java.lang.VirtualMachineError

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** InternalError

,

OutOfMemoryError

,

StackOverflowError

,

UnknownError

```java
public abstract class
VirtualMachineError

extends
Error
```

Thrown to indicate that the Java Virtual Machine is broken or has
run out of resources necessary for it to continue operating.

**Since:** 1.0
**See Also:** Serialized Form

public abstract class

VirtualMachineError

extends

Error

Thrown to indicate that the Java Virtual Machine is broken or has
run out of resources necessary for it to continue operating.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VirtualMachineError

()

Constructs a

VirtualMachineError

with no detail message.

VirtualMachineError

​(

String

message)

Constructs a

VirtualMachineError

with the specified
detail message.

VirtualMachineError

​(

String

message,

Throwable

cause)

Constructs a

VirtualMachineError

with the specified
detail message and cause.

VirtualMachineError

​(

Throwable

cause)

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

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

VirtualMachineError

()

Constructs a

VirtualMachineError

with no detail message.

VirtualMachineError

​(

String

message)

Constructs a

VirtualMachineError

with the specified
detail message.

VirtualMachineError

​(

String

message,

Throwable

cause)

Constructs a

VirtualMachineError

with the specified
detail message and cause.

VirtualMachineError

​(

Throwable

cause)

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

---

#### Constructor Summary

Constructs a

VirtualMachineError

with no detail message.

Constructs a

VirtualMachineError

with the specified
detail message.

Constructs a

VirtualMachineError

with the specified
detail message and cause.

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

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

- VirtualMachineError

```java
public VirtualMachineError()
```

Constructs a

VirtualMachineError

with no detail message.

- VirtualMachineError

```java
public VirtualMachineError​(
String
message)
```

Constructs a

VirtualMachineError

with the specified
detail message.

**Parameters:** message

- the detail message.

- VirtualMachineError

```java
public VirtualMachineError​(
String
message,

Throwable
cause)
```

Constructs a

VirtualMachineError

with the specified
detail message and cause.

Note that the detail message
associated with

cause

is

not

automatically
incorporated in this error's detail message.

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

- VirtualMachineError

```java
public VirtualMachineError​(
Throwable
cause)
```

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

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

- VirtualMachineError

```java
public VirtualMachineError()
```

Constructs a

VirtualMachineError

with no detail message.

- VirtualMachineError

```java
public VirtualMachineError​(
String
message)
```

Constructs a

VirtualMachineError

with the specified
detail message.

**Parameters:** message

- the detail message.

- VirtualMachineError

```java
public VirtualMachineError​(
String
message,

Throwable
cause)
```

Constructs a

VirtualMachineError

with the specified
detail message and cause.

Note that the detail message
associated with

cause

is

not

automatically
incorporated in this error's detail message.

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

- VirtualMachineError

```java
public VirtualMachineError​(
Throwable
cause)
```

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

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

VirtualMachineError

```java
public VirtualMachineError()
```

Constructs a

VirtualMachineError

with no detail message.

---

#### VirtualMachineError

public VirtualMachineError()

Constructs a

VirtualMachineError

with no detail message.

VirtualMachineError

```java
public VirtualMachineError​(
String
message)
```

Constructs a

VirtualMachineError

with the specified
detail message.

**Parameters:** message

- the detail message.

---

#### VirtualMachineError

public VirtualMachineError​(

String

message)

Constructs a

VirtualMachineError

with the specified
detail message.

VirtualMachineError

```java
public VirtualMachineError​(
String
message,

Throwable
cause)
```

Constructs a

VirtualMachineError

with the specified
detail message and cause.

Note that the detail message
associated with

cause

is

not

automatically
incorporated in this error's detail message.

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

#### VirtualMachineError

public VirtualMachineError​(

String

message,

Throwable

cause)

Constructs a

VirtualMachineError

with the specified
detail message and cause.

Note that the detail message
associated with

cause

is

not

automatically
incorporated in this error's detail message.

Note that the detail message
associated with

cause

is

not

automatically
incorporated in this error's detail message.

VirtualMachineError

```java
public VirtualMachineError​(
Throwable
cause)
```

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

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

#### VirtualMachineError

public VirtualMachineError​(

Throwable

cause)

Constructs an a

VirtualMachineError

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and
detail message of

cause

).

---

