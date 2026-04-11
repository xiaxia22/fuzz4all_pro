# Class RuntimeException

**Source:** `java.base\java\lang\RuntimeException.html`

### Class Description

```java
public class
RuntimeException

extends
Exception
```

RuntimeException

is the superclass of those
exceptions that can be thrown during the normal operation of the
Java Virtual Machine.

RuntimeException

and its subclasses are

unchecked
exceptions

. Unchecked exceptions do

not

need to be
declared in a method or constructor's

throws

clause if they
can be thrown by the execution of the method or constructor and
propagate outside the method or constructor boundary.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RuntimeException()

Constructs a new runtime exception with

null

as its
detail message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

---

#### public RuntimeException​(
String
message)

Constructs a new runtime exception with the specified detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:**
- message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

---

#### public RuntimeException​(
String
message,

Throwable
cause)

Constructs a new runtime exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this runtime exception's detail message.

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

#### public RuntimeException​(
Throwable
cause)

Constructs a new runtime exception with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

). This constructor is useful for runtime exceptions
that are little more than wrappers for other throwables.

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

#### protected RuntimeException​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

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

#### Class RuntimeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException

java.lang.Exception

- java.lang.RuntimeException

java.lang.RuntimeException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AnnotationTypeMismatchException

,

ArithmeticException

,

ArrayStoreException

,

BufferOverflowException

,

BufferUnderflowException

,

CannotRedoException

,

CannotUndoException

,

CatalogException

,

ClassCastException

,

ClassNotPreparedException

,

CMMException

,

CompletionException

,

ConcurrentModificationException

,

DateTimeException

,

DOMException

,

DuplicateRequestException

,

EmptyStackException

,

EnumConstantNotPresentException

,

EventException

,

FileSystemAlreadyExistsException

,

FileSystemNotFoundException

,

FindException

,

IllegalArgumentException

,

IllegalCallerException

,

IllegalMonitorStateException

,

IllegalPathStateException

,

IllegalStateException

,

IllformedLocaleException

,

ImagingOpException

,

InaccessibleObjectException

,

IncompleteAnnotationException

,

InconsistentDebugInfoException

,

IndexOutOfBoundsException

,

InternalException

,

InvalidCodeIndexException

,

InvalidLineNumberException

,

InvalidModuleDescriptorException

,

InvalidModuleException

,

InvalidRequestStateException

,

InvalidStackFrameException

,

JarSignerException

,

JMRuntimeException

,

JSException

,

LayerInstantiationException

,

LSException

,

MalformedParameterizedTypeException

,

MalformedParametersException

,

MirroredTypesException

,

MissingResourceException

,

NashornException

,

NativeMethodException

,

NegativeArraySizeException

,

NoSuchDynamicMethodException

,

NoSuchElementException

,

NoSuchMechanismException

,

NullPointerException

,

ObjectCollectedException

,

ProfileDataException

,

ProviderException

,

ProviderNotFoundException

,

RangeException

,

RasterFormatException

,

RejectedExecutionException

,

ResolutionException

,

SecurityException

,

SPIResolutionException

,

TypeNotPresentException

,

UncheckedIOException

,

UndeclaredThrowableException

,

UnknownEntityException

,

UnknownTreeException

,

UnmodifiableModuleException

,

UnmodifiableSetException

,

UnsupportedOperationException

,

VMDisconnectedException

,

VMMismatchException

,

VMOutOfMemoryException

,

WrongMethodTypeException

,

XPathException

```java
public class
RuntimeException

extends
Exception
```

RuntimeException

is the superclass of those
exceptions that can be thrown during the normal operation of the
Java Virtual Machine.

RuntimeException

and its subclasses are

unchecked
exceptions

. Unchecked exceptions do

not

need to be
declared in a method or constructor's

throws

clause if they
can be thrown by the execution of the method or constructor and
propagate outside the method or constructor boundary.

**Since:** 1.0
**See Also:** Serialized Form
**See The Java™ Language Specification :** 11.2 Compile-Time Checking of Exceptions

public class

RuntimeException

extends

Exception

RuntimeException

is the superclass of those
exceptions that can be thrown during the normal operation of the
Java Virtual Machine.

RuntimeException

and its subclasses are

unchecked
exceptions

. Unchecked exceptions do

not

need to be
declared in a method or constructor's

throws

clause if they
can be thrown by the execution of the method or constructor and
propagate outside the method or constructor boundary.

RuntimeException

and its subclasses are

unchecked
exceptions

. Unchecked exceptions do

not

need to be
declared in a method or constructor's

throws

clause if they
can be thrown by the execution of the method or constructor and
propagate outside the method or constructor boundary.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

RuntimeException

()

Constructs a new runtime exception with

null

as its
detail message.

RuntimeException

​(

String

message)

Constructs a new runtime exception with the specified detail message.

RuntimeException

​(

String

message,

Throwable

cause)

Constructs a new runtime exception with the specified detail message and
cause.

protected

RuntimeException

​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

RuntimeException

​(

Throwable

cause)

Constructs a new runtime exception with the specified cause and a
detail message of

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

Modifier

Constructor

Description

RuntimeException

()

Constructs a new runtime exception with

null

as its
detail message.

RuntimeException

​(

String

message)

Constructs a new runtime exception with the specified detail message.

RuntimeException

​(

String

message,

Throwable

cause)

Constructs a new runtime exception with the specified detail message and
cause.

protected

RuntimeException

​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

RuntimeException

​(

Throwable

cause)

Constructs a new runtime exception with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a new runtime exception with

null

as its
detail message.

Constructs a new runtime exception with the specified detail message.

Constructs a new runtime exception with the specified detail message and
cause.

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

Constructs a new runtime exception with the specified cause and a
detail message of

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

- RuntimeException

```java
public RuntimeException()
```

Constructs a new runtime exception with

null

as its
detail message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

- RuntimeException

```java
public RuntimeException​(
String
message)
```

Constructs a new runtime exception with the specified detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- RuntimeException

```java
public RuntimeException​(
String
message,

Throwable
cause)
```

Constructs a new runtime exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this runtime exception's detail message.

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

- RuntimeException

```java
public RuntimeException​(
Throwable
cause)
```

Constructs a new runtime exception with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

). This constructor is useful for runtime exceptions
that are little more than wrappers for other throwables.

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.4

- RuntimeException

```java
protected RuntimeException​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

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

- RuntimeException

```java
public RuntimeException()
```

Constructs a new runtime exception with

null

as its
detail message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

- RuntimeException

```java
public RuntimeException​(
String
message)
```

Constructs a new runtime exception with the specified detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- RuntimeException

```java
public RuntimeException​(
String
message,

Throwable
cause)
```

Constructs a new runtime exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this runtime exception's detail message.

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

- RuntimeException

```java
public RuntimeException​(
Throwable
cause)
```

Constructs a new runtime exception with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

). This constructor is useful for runtime exceptions
that are little more than wrappers for other throwables.

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.4

- RuntimeException

```java
protected RuntimeException​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

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

RuntimeException

```java
public RuntimeException()
```

Constructs a new runtime exception with

null

as its
detail message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

---

#### RuntimeException

public RuntimeException()

Constructs a new runtime exception with

null

as its
detail message. The cause is not initialized, and may subsequently be
initialized by a call to

Throwable.initCause(java.lang.Throwable)

.

RuntimeException

```java
public RuntimeException​(
String
message)
```

Constructs a new runtime exception with the specified detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

---

#### RuntimeException

public RuntimeException​(

String

message)

Constructs a new runtime exception with the specified detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

RuntimeException

```java
public RuntimeException​(
String
message,

Throwable
cause)
```

Constructs a new runtime exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this runtime exception's detail message.

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

#### RuntimeException

public RuntimeException​(

String

message,

Throwable

cause)

Constructs a new runtime exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this runtime exception's detail message.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this runtime exception's detail message.

RuntimeException

```java
public RuntimeException​(
Throwable
cause)
```

Constructs a new runtime exception with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

). This constructor is useful for runtime exceptions
that are little more than wrappers for other throwables.

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

#### RuntimeException

public RuntimeException​(

Throwable

cause)

Constructs a new runtime exception with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

). This constructor is useful for runtime exceptions
that are little more than wrappers for other throwables.

RuntimeException

```java
protected RuntimeException​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

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

#### RuntimeException

protected RuntimeException​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new runtime exception with the specified detail
message, cause, suppression enabled or disabled, and writable
stack trace enabled or disabled.

---

