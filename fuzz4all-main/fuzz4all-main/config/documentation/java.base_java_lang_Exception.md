# Class Exception

**Source:** `java.base\java\lang\Exception.html`

### Class Description

```java
public class
Exception

extends
Throwable
```

The class

Exception

and its subclasses are a form of

Throwable

that indicates conditions that a reasonable
application might want to catch.

The class

Exception

and any subclasses that are not also
subclasses of

RuntimeException

are

checked
exceptions

. Checked exceptions need to be declared in a
method or constructor's

throws

clause if they can be thrown
by the execution of the method or constructor and propagate outside
the method or constructor boundary.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Exception()

Constructs a new exception with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

---

#### public Exception​(
String
message)

Constructs a new exception with the specified detail message. The
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

#### public Exception​(
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

automatically incorporated in
this exception's detail message.

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

#### public Exception​(
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
- 1.4

---

#### protected Exception​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new exception with the specified detail message,
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

#### Class Exception

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception

java.lang.Throwable

- java.lang.Exception

java.lang.Exception

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AbsentInformationException

,

AclNotFoundException

,

ActivationException

,

AgentInitializationException

,

AgentLoadException

,

AlreadyBoundException

,

AttachNotSupportedException

,

AWTException

,

BackingStoreException

,

BadAttributeValueExpException

,

BadBinaryOpValueExpException

,

BadLocationException

,

BadStringOperationException

,

BrokenBarrierException

,

CardException

,

CertificateException

,

ClassNotLoadedException

,

CloneNotSupportedException

,

DataFormatException

,

DatatypeConfigurationException

,

DestroyFailedException

,

ExecutionControl.ExecutionControlException

,

ExecutionException

,

ExpandVetoException

,

FontFormatException

,

GeneralSecurityException

,

GSSException

,

IllegalClassFormatException

,

IllegalConnectorArgumentsException

,

IncompatibleThreadStateException

,

InterruptedException

,

IntrospectionException

,

InvalidApplicationException

,

InvalidMidiDataException

,

InvalidPreferencesFormatException

,

InvalidTargetObjectTypeException

,

InvalidTypeException

,

InvocationException

,

IOException

,

JMException

,

JShellException

,

KeySelectorException

,

LambdaConversionException

,

LastOwnerException

,

LineUnavailableException

,

MarshalException

,

MidiUnavailableException

,

MimeTypeParseException

,

NamingException

,

NoninvertibleTransformException

,

NotBoundException

,

NotOwnerException

,

ParseException

,

ParserConfigurationException

,

PrinterException

,

PrintException

,

PrivilegedActionException

,

PropertyVetoException

,

ReflectiveOperationException

,

RefreshFailedException

,

RuntimeException

,

SAXException

,

ScriptException

,

ServerNotActiveException

,

SQLException

,

StringConcatException

,

TimeoutException

,

TooManyListenersException

,

TransformerException

,

TransformException

,

UnmodifiableClassException

,

UnsupportedAudioFileException

,

UnsupportedCallbackException

,

UnsupportedFlavorException

,

UnsupportedLookAndFeelException

,

URIReferenceException

,

URISyntaxException

,

VMStartException

,

XAException

,

XMLParseException

,

XMLSignatureException

,

XMLStreamException

,

XPathException

```java
public class
Exception

extends
Throwable
```

The class

Exception

and its subclasses are a form of

Throwable

that indicates conditions that a reasonable
application might want to catch.

The class

Exception

and any subclasses that are not also
subclasses of

RuntimeException

are

checked
exceptions

. Checked exceptions need to be declared in a
method or constructor's

throws

clause if they can be thrown
by the execution of the method or constructor and propagate outside
the method or constructor boundary.

**Since:** 1.0
**See Also:** Error

,

Serialized Form
**See The Java™ Language Specification :** 11.2 Compile-Time Checking of Exceptions

public class

Exception

extends

Throwable

The class

Exception

and its subclasses are a form of

Throwable

that indicates conditions that a reasonable
application might want to catch.

The class

Exception

and any subclasses that are not also
subclasses of

RuntimeException

are

checked
exceptions

. Checked exceptions need to be declared in a
method or constructor's

throws

clause if they can be thrown
by the execution of the method or constructor and propagate outside
the method or constructor boundary.

The class

Exception

and any subclasses that are not also
subclasses of

RuntimeException

are

checked
exceptions

. Checked exceptions need to be declared in a
method or constructor's

throws

clause if they can be thrown
by the execution of the method or constructor and propagate outside
the method or constructor boundary.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

Exception

()

Constructs a new exception with

null

as its detail message.

Exception

​(

String

message)

Constructs a new exception with the specified detail message.

Exception

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

protected

Exception

​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new exception with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

Exception

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

Modifier

Constructor

Description

Exception

()

Constructs a new exception with

null

as its detail message.

Exception

​(

String

message)

Constructs a new exception with the specified detail message.

Exception

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

protected

Exception

​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new exception with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

Exception

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

Constructs a new exception with

null

as its detail message.

Constructs a new exception with the specified detail message.

Constructs a new exception with the specified detail message and
cause.

Constructs a new exception with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

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

- Exception

```java
public Exception()
```

Constructs a new exception with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

- Exception

```java
public Exception​(
String
message)
```

Constructs a new exception with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- Exception

```java
public Exception​(
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

automatically incorporated in
this exception's detail message.

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

- Exception

```java
public Exception​(
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
**Since:** 1.4

- Exception

```java
protected Exception​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new exception with the specified detail message,
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

- Exception

```java
public Exception()
```

Constructs a new exception with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

- Exception

```java
public Exception​(
String
message)
```

Constructs a new exception with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

**Parameters:** message

- the detail message. The detail message is saved for
later retrieval by the

Throwable.getMessage()

method.

- Exception

```java
public Exception​(
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

automatically incorporated in
this exception's detail message.

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

- Exception

```java
public Exception​(
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
**Since:** 1.4

- Exception

```java
protected Exception​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new exception with the specified detail message,
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

Exception

```java
public Exception()
```

Constructs a new exception with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

---

#### Exception

public Exception()

Constructs a new exception with

null

as its detail message.
The cause is not initialized, and may subsequently be initialized by a
call to

Throwable.initCause(java.lang.Throwable)

.

Exception

```java
public Exception​(
String
message)
```

Constructs a new exception with the specified detail message. The
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

#### Exception

public Exception​(

String

message)

Constructs a new exception with the specified detail message. The
cause is not initialized, and may subsequently be initialized by
a call to

Throwable.initCause(java.lang.Throwable)

.

Exception

```java
public Exception​(
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

automatically incorporated in
this exception's detail message.

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

#### Exception

public Exception​(

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

automatically incorporated in
this exception's detail message.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

Exception

```java
public Exception​(
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
**Since:** 1.4

---

#### Exception

public Exception​(

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

Exception

```java
protected Exception​(
String
message,

Throwable
cause,
boolean enableSuppression,
boolean writableStackTrace)
```

Constructs a new exception with the specified detail message,
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

#### Exception

protected Exception​(

String

message,

Throwable

cause,
boolean enableSuppression,
boolean writableStackTrace)

Constructs a new exception with the specified detail message,
cause, suppression enabled or disabled, and writable stack
trace enabled or disabled.

---

