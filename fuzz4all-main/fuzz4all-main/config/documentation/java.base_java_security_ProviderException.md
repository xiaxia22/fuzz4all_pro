# Class ProviderException

**Source:** `java.base\java\security\ProviderException.html`

### Class Description

```java
public class
ProviderException

extends
RuntimeException
```

A runtime exception for Provider exceptions (such as
misconfiguration errors or unrecoverable internal errors),
which may be subclassed by Providers to
throw specialized, provider-specific runtime errors.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ProviderException()

Constructs a ProviderException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public ProviderException​(
String
s)

Constructs a ProviderException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- s

- the detail message.

---

#### public ProviderException​(
String
message,

Throwable
cause)

Creates a

ProviderException

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

#### public ProviderException​(
Throwable
cause)

Creates a

ProviderException

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

#### Class ProviderException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.security.ProviderException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.security.ProviderException

java.lang.Exception

- java.lang.RuntimeException
- - java.security.ProviderException

java.lang.RuntimeException

- java.security.ProviderException

java.security.ProviderException

**All Implemented Interfaces:** Serializable

```java
public class
ProviderException

extends
RuntimeException
```

A runtime exception for Provider exceptions (such as
misconfiguration errors or unrecoverable internal errors),
which may be subclassed by Providers to
throw specialized, provider-specific runtime errors.

**Since:** 1.1
**See Also:** Serialized Form

public class

ProviderException

extends

RuntimeException

A runtime exception for Provider exceptions (such as
misconfiguration errors or unrecoverable internal errors),
which may be subclassed by Providers to
throw specialized, provider-specific runtime errors.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ProviderException

()

Constructs a ProviderException with no detail message.

ProviderException

​(

String

s)

Constructs a ProviderException with the specified detail
message.

ProviderException

​(

String

message,

Throwable

cause)

Creates a

ProviderException

with the specified
detail message and cause.

ProviderException

​(

Throwable

cause)

Creates a

ProviderException

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

ProviderException

()

Constructs a ProviderException with no detail message.

ProviderException

​(

String

s)

Constructs a ProviderException with the specified detail
message.

ProviderException

​(

String

message,

Throwable

cause)

Creates a

ProviderException

with the specified
detail message and cause.

ProviderException

​(

Throwable

cause)

Creates a

ProviderException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a ProviderException with no detail message.

Constructs a ProviderException with the specified detail
message.

Creates a

ProviderException

with the specified
detail message and cause.

Creates a

ProviderException

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

- ProviderException

```java
public ProviderException()
```

Constructs a ProviderException with no detail message. A
detail message is a String that describes this particular
exception.

- ProviderException

```java
public ProviderException​(
String
s)
```

Constructs a ProviderException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** s

- the detail message.

- ProviderException

```java
public ProviderException​(
String
message,

Throwable
cause)
```

Creates a

ProviderException

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

- ProviderException

```java
public ProviderException​(
Throwable
cause)
```

Creates a

ProviderException

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

- ProviderException

```java
public ProviderException()
```

Constructs a ProviderException with no detail message. A
detail message is a String that describes this particular
exception.

- ProviderException

```java
public ProviderException​(
String
s)
```

Constructs a ProviderException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** s

- the detail message.

- ProviderException

```java
public ProviderException​(
String
message,

Throwable
cause)
```

Creates a

ProviderException

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

- ProviderException

```java
public ProviderException​(
Throwable
cause)
```

Creates a

ProviderException

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

ProviderException

```java
public ProviderException()
```

Constructs a ProviderException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### ProviderException

public ProviderException()

Constructs a ProviderException with no detail message. A
detail message is a String that describes this particular
exception.

ProviderException

```java
public ProviderException​(
String
s)
```

Constructs a ProviderException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** s

- the detail message.

---

#### ProviderException

public ProviderException​(

String

s)

Constructs a ProviderException with the specified detail
message. A detail message is a String that describes this
particular exception.

ProviderException

```java
public ProviderException​(
String
message,

Throwable
cause)
```

Creates a

ProviderException

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

#### ProviderException

public ProviderException​(

String

message,

Throwable

cause)

Creates a

ProviderException

with the specified
detail message and cause.

ProviderException

```java
public ProviderException​(
Throwable
cause)
```

Creates a

ProviderException

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

#### ProviderException

public ProviderException​(

Throwable

cause)

Creates a

ProviderException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

