# Class Error

**Source:** `java.base\java\lang\Error.html`

### Class Description

```java
public class
Error

extends
Throwable
```

An

Error

is a subclass of

Throwable

that indicates serious problems that a reasonable application
should not try to catch. Most such errors are abnormal conditions.
The

ThreadDeath

error, though a "normal" condition,
is also a subclass of

Error

because most applications
should not try to catch it.

A method is not required to declare in its

throws

clause any subclasses of

Error

that might be thrown
during the execution of the method but not caught, since these
errors are abnormal conditions that should never occur.

That is,

Error

and its subclasses are regarded as unchecked
exceptions for the purposes of compile-time checking of exceptions.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Error()

Constructs a new error with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

---

#### public Error​(
String
message)

Constructs a new error with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:**
- message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

---

#### public Error​(
String
message,

Throwable
cause)

Constructs a new error with the specified detail message and
cause.

Note that the detail message associated with

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
- 1.4

---

#### public Error​(
Throwable
cause)

Constructs a new error with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for errors that are little more than
wrappers for other throwables.

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
- 1.4

---

#### protected Error​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

**Parameters:**
- message

- the detail message.
- cause

- the cause. (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
- enableSuppression

- whether or not suppression is enabled
or disabled
- writableStackTrace

- whether or not the stack trace should
be writable

**Since:**
- 1.7

---

### Method Details

*No entries found.*

### Additional Sections

#### Class Error

java.lang.Object

- java.lang.Throwable
- - java.lang.Error

java.lang.Throwable

- java.lang.Error

java.lang.Error

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AnnotationFormatError

,

AssertionError

,

AWTError

,

CoderMalfunctionError

,

FactoryConfigurationError

,

FactoryConfigurationError

,

IOError

,

LinkageError

,

SchemaFactoryConfigurationError

,

ServiceConfigurationError

,

ThreadDeath

,

TransformerFactoryConfigurationError

,

VirtualMachineError

```java
public class
Error

extends
Throwable
```

An

Error

is a subclass of

Throwable

that indicates serious problems that a reasonable application
should not try to catch. Most such errors are abnormal conditions.
The

ThreadDeath

error, though a "normal" condition,
is also a subclass of

Error

because most applications
should not try to catch it.

A method is not required to declare in its

throws

clause any subclasses of

Error

that might be thrown
during the execution of the method but not caught, since these
errors are abnormal conditions that should never occur.

That is,

Error

and its subclasses are regarded as unchecked
exceptions for the purposes of compile-time checking of exceptions.

**Since:** 1.0
**See Also:** ThreadDeath

,

Serialized Form
**See The Java™ Language Specification :** 11.2 Compile-Time Checking of Exceptions

public class

Error

extends

Throwable

An

Error

is a subclass of

Throwable

that indicates serious problems that a reasonable application
should not try to catch. Most such errors are abnormal conditions.
The

ThreadDeath

error, though a "normal" condition,
is also a subclass of

Error

because most applications
should not try to catch it.

A method is not required to declare in its

throws

clause any subclasses of

Error

that might be thrown
during the execution of the method but not caught, since these
errors are abnormal conditions that should never occur.

That is,

Error

and its subclasses are regarded as unchecked
exceptions for the purposes of compile-time checking of exceptions.

A method is not required to declare in its

throws

clause any subclasses of

Error

that might be thrown
during the execution of the method but not caught, since these
errors are abnormal conditions that should never occur.

That is,

Error

and its subclasses are regarded as unchecked
exceptions for the purposes of compile-time checking of exceptions.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

Error

()

Constructs a new error with

null

as its detail message.

Error

​(

String

message)

Constructs a new error with the specified detail message.

Error

​(

String

message,

Throwable

cause)

Constructs a new error with the specified detail message and
cause.

protected

Error

​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

Error

​(

Throwable

cause)

Constructs a new error with the specified cause and a detail
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

Modifier

Constructor

Description

Error

()

Constructs a new error with

null

as its detail message.

Error

​(

String

message)

Constructs a new error with the specified detail message.

Error

​(

String

message,

Throwable

cause)

Constructs a new error with the specified detail message and
cause.

protected

Error

​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

Error

​(

Throwable

cause)

Constructs a new error with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a new error with

null

as its detail message.

Constructs a new error with the specified detail message.

Constructs a new error with the specified detail message and
cause.

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

Constructs a new error with the specified cause and a detail
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

- Error

```java
public Error()
```

Constructs a new error with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

- Error

```java
public Error​(
String
message)
```

Constructs a new error with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- Error

```java
public Error​(
String
message,

Throwable
cause)
```

Constructs a new error with the specified detail message and
cause.

Note that the detail message associated with

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
**Since:** 1.4

- Error

```java
public Error​(
Throwable
cause)
```

Constructs a new error with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for errors that are little more than
wrappers for other throwables.

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.4

- Error

```java
protected Error​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

**Parameters:** message

- the detail message.
**Parameters:** cause

- the cause. (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Parameters:** enableSuppression

- whether or not suppression is enabled
or disabled
**Parameters:** writableStackTrace

- whether or not the stack trace should
be writable
**Since:** 1.7

Constructor Detail

- Error

```java
public Error()
```

Constructs a new error with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

- Error

```java
public Error​(
String
message)
```

Constructs a new error with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- Error

```java
public Error​(
String
message,

Throwable
cause)
```

Constructs a new error with the specified detail message and
cause.

Note that the detail message associated with

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
**Since:** 1.4

- Error

```java
public Error​(
Throwable
cause)
```

Constructs a new error with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for errors that are little more than
wrappers for other throwables.

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.4

- Error

```java
protected Error​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

**Parameters:** message

- the detail message.
**Parameters:** cause

- the cause. (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Parameters:** enableSuppression

- whether or not suppression is enabled
or disabled
**Parameters:** writableStackTrace

- whether or not the stack trace should
be writable
**Since:** 1.7

---

#### Constructor Detail

Error

```java
public Error()
```

Constructs a new error with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

---

#### Error

public Error()

Constructs a new error with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

Error

```java
public Error​(
String
message)
```

Constructs a new error with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

---

#### Error

public Error​(

String

message)

Constructs a new error with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

Error

```java
public Error​(
String
message,

Throwable
cause)
```

Constructs a new error with the specified detail message and
cause.

Note that the detail message associated with

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
**Since:** 1.4

---

#### Error

public Error​(

String

message,

Throwable

cause)

Constructs a new error with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

Error

```java
public Error​(
Throwable
cause)
```

Constructs a new error with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for errors that are little more than
wrappers for other throwables.

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.4

---

#### Error

public Error​(

Throwable

cause)

Constructs a new error with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for errors that are little more than
wrappers for other throwables.

Error

```java
protected Error​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

**Parameters:** message

- the detail message.
**Parameters:** cause

- the cause. (A

null

value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Parameters:** enableSuppression

- whether or not suppression is enabled
or disabled
**Parameters:** writableStackTrace

- whether or not the stack trace should
be writable
**Since:** 1.7

---

#### Error

protected Error​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new error with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

---

