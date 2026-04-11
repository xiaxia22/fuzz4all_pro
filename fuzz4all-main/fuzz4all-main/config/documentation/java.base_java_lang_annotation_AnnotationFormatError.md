# Class AnnotationFormatError

**Source:** `java.base\java\lang\annotation\AnnotationFormatError.html`

### Class Description

```java
public class
AnnotationFormatError

extends
Error
```

Thrown when the annotation parser attempts to read an annotation
from a class file and determines that the annotation is malformed.
This error can be thrown by the

API used to read annotations
reflectively

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AnnotationFormatError​(
String
message)

Constructs a new

AnnotationFormatError

with the specified
detail message.

**Parameters:**
- message

- the detail message.

---

#### public AnnotationFormatError​(
String
message,

Throwable
cause)

Constructs a new

AnnotationFormatError

with the specified
detail message and cause. Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:**
- message

- the detail message
- cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### public AnnotationFormatError​(
Throwable
cause)

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:**
- cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AnnotationFormatError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - java.lang.annotation.AnnotationFormatError

java.lang.Throwable

- java.lang.Error
- - java.lang.annotation.AnnotationFormatError

java.lang.Error

- java.lang.annotation.AnnotationFormatError

java.lang.annotation.AnnotationFormatError

**All Implemented Interfaces:** Serializable

```java
public class
AnnotationFormatError

extends
Error
```

Thrown when the annotation parser attempts to read an annotation
from a class file and determines that the annotation is malformed.
This error can be thrown by the

API used to read annotations
reflectively

.

**Since:** 1.5
**See Also:** AnnotatedElement

,

Serialized Form

public class

AnnotationFormatError

extends

Error

Thrown when the annotation parser attempts to read an annotation
from a class file and determines that the annotation is malformed.
This error can be thrown by the

API used to read annotations
reflectively

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AnnotationFormatError

​(

String

message)

Constructs a new

AnnotationFormatError

with the specified
detail message.

AnnotationFormatError

​(

String

message,

Throwable

cause)

Constructs a new

AnnotationFormatError

with the specified
detail message and cause.

AnnotationFormatError

​(

Throwable

cause)

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

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

AnnotationFormatError

​(

String

message)

Constructs a new

AnnotationFormatError

with the specified
detail message.

AnnotationFormatError

​(

String

message,

Throwable

cause)

Constructs a new

AnnotationFormatError

with the specified
detail message and cause.

AnnotationFormatError

​(

Throwable

cause)

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a new

AnnotationFormatError

with the specified
detail message.

Constructs a new

AnnotationFormatError

with the specified
detail message and cause.

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

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

- AnnotationFormatError

```java
public AnnotationFormatError​(
String
message)
```

Constructs a new

AnnotationFormatError

with the specified
detail message.

**Parameters:** message

- the detail message.

- AnnotationFormatError

```java
public AnnotationFormatError​(
String
message,

Throwable
cause)
```

Constructs a new

AnnotationFormatError

with the specified
detail message and cause. Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

- AnnotationFormatError

```java
public AnnotationFormatError​(
Throwable
cause)
```

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

Constructor Detail

- AnnotationFormatError

```java
public AnnotationFormatError​(
String
message)
```

Constructs a new

AnnotationFormatError

with the specified
detail message.

**Parameters:** message

- the detail message.

- AnnotationFormatError

```java
public AnnotationFormatError​(
String
message,

Throwable
cause)
```

Constructs a new

AnnotationFormatError

with the specified
detail message and cause. Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

- AnnotationFormatError

```java
public AnnotationFormatError​(
Throwable
cause)
```

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### Constructor Detail

AnnotationFormatError

```java
public AnnotationFormatError​(
String
message)
```

Constructs a new

AnnotationFormatError

with the specified
detail message.

**Parameters:** message

- the detail message.

---

#### AnnotationFormatError

public AnnotationFormatError​(

String

message)

Constructs a new

AnnotationFormatError

with the specified
detail message.

AnnotationFormatError

```java
public AnnotationFormatError​(
String
message,

Throwable
cause)
```

Constructs a new

AnnotationFormatError

with the specified
detail message and cause. Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### AnnotationFormatError

public AnnotationFormatError​(

String

message,

Throwable

cause)

Constructs a new

AnnotationFormatError

with the specified
detail message and cause. Note that the detail message associated
with

cause

is

not

automatically incorporated in
this error's detail message.

AnnotationFormatError

```java
public AnnotationFormatError​(
Throwable
cause)
```

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### AnnotationFormatError

public AnnotationFormatError​(

Throwable

cause)

Constructs a new

AnnotationFormatError

with the specified
cause and a detail message of

(cause == null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

