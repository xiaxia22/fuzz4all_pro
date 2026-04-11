# Class IOException

**Source:** `java.base\java\io\IOException.html`

### Class Description

```java
public class
IOException

extends
Exception
```

Signals that an I/O exception of some sort has occurred. This
class is the general class of exceptions produced by failed or
interrupted I/O operations.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IOException()

Constructs an

IOException

with

null

as its error detail message.

---

#### public IOException​(
String
message)

Constructs an

IOException

with the specified detail message.

**Parameters:**
- message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)

---

#### public IOException​(
String
message,

Throwable
cause)

Constructs an

IOException

with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated into this exception's detail
message.

**Parameters:**
- message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)
- cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)

**Since:**
- 1.6

---

#### public IOException​(
Throwable
cause)

Constructs an

IOException

with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).
This constructor is useful for IO exceptions that are little more
than wrappers for other throwables.

**Parameters:**
- cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)

**Since:**
- 1.6

---

### Method Details

*No entries found.*

### Additional Sections

#### Class IOException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException

java.lang.Exception

- java.io.IOException

java.io.IOException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AttachOperationFailedException

,

ChangedCharSetException

,

CharacterCodingException

,

CharConversionException

,

ClosedChannelException

,

ClosedConnectionException

,

EOFException

,

FileLockInterruptionException

,

FileNotFoundException

,

FilerException

,

FileSystemException

,

HttpRetryException

,

HttpTimeoutException

,

IIOException

,

InterruptedByTimeoutException

,

InterruptedIOException

,

InvalidPropertiesFormatException

,

JMXProviderException

,

JMXServerErrorException

,

MalformedURLException

,

ObjectStreamException

,

ProtocolException

,

RemoteException

,

SaslException

,

SocketException

,

SSLException

,

SyncFailedException

,

TransportTimeoutException

,

UnknownHostException

,

UnknownServiceException

,

UnsupportedEncodingException

,

UserPrincipalNotFoundException

,

UTFDataFormatException

,

WebSocketHandshakeException

,

ZipException

```java
public class
IOException

extends
Exception
```

Signals that an I/O exception of some sort has occurred. This
class is the general class of exceptions produced by failed or
interrupted I/O operations.

**Since:** 1.0
**See Also:** InputStream

,

OutputStream

,

Serialized Form

public class

IOException

extends

Exception

Signals that an I/O exception of some sort has occurred. This
class is the general class of exceptions produced by failed or
interrupted I/O operations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IOException

()

Constructs an

IOException

with

null

as its error detail message.

IOException

​(

String

message)

Constructs an

IOException

with the specified detail message.

IOException

​(

String

message,

Throwable

cause)

Constructs an

IOException

with the specified detail message
and cause.

IOException

​(

Throwable

cause)

Constructs an

IOException

with the specified cause and a
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

Constructor

Description

IOException

()

Constructs an

IOException

with

null

as its error detail message.

IOException

​(

String

message)

Constructs an

IOException

with the specified detail message.

IOException

​(

String

message,

Throwable

cause)

Constructs an

IOException

with the specified detail message
and cause.

IOException

​(

Throwable

cause)

Constructs an

IOException

with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs an

IOException

with

null

as its error detail message.

Constructs an

IOException

with the specified detail message.

Constructs an

IOException

with the specified detail message
and cause.

Constructs an

IOException

with the specified cause and a
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

- IOException

```java
public IOException()
```

Constructs an

IOException

with

null

as its error detail message.

- IOException

```java
public IOException​(
String
message)
```

Constructs an

IOException

with the specified detail message.

**Parameters:** message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)

- IOException

```java
public IOException​(
String
message,

Throwable
cause)
```

Constructs an

IOException

with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated into this exception's detail
message.

**Parameters:** message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)
**Parameters:** cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.6

- IOException

```java
public IOException​(
Throwable
cause)
```

Constructs an

IOException

with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).
This constructor is useful for IO exceptions that are little more
than wrappers for other throwables.

**Parameters:** cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.6

Constructor Detail

- IOException

```java
public IOException()
```

Constructs an

IOException

with

null

as its error detail message.

- IOException

```java
public IOException​(
String
message)
```

Constructs an

IOException

with the specified detail message.

**Parameters:** message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)

- IOException

```java
public IOException​(
String
message,

Throwable
cause)
```

Constructs an

IOException

with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated into this exception's detail
message.

**Parameters:** message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)
**Parameters:** cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.6

- IOException

```java
public IOException​(
Throwable
cause)
```

Constructs an

IOException

with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).
This constructor is useful for IO exceptions that are little more
than wrappers for other throwables.

**Parameters:** cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.6

---

#### Constructor Detail

IOException

```java
public IOException()
```

Constructs an

IOException

with

null

as its error detail message.

---

#### IOException

public IOException()

Constructs an

IOException

with

null

as its error detail message.

IOException

```java
public IOException​(
String
message)
```

Constructs an

IOException

with the specified detail message.

**Parameters:** message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)

---

#### IOException

public IOException​(

String

message)

Constructs an

IOException

with the specified detail message.

IOException

```java
public IOException​(
String
message,

Throwable
cause)
```

Constructs an

IOException

with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated into this exception's detail
message.

**Parameters:** message

- The detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method)
**Parameters:** cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.6

---

#### IOException

public IOException​(

String

message,

Throwable

cause)

Constructs an

IOException

with the specified detail message
and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated into this exception's detail
message.

Note that the detail message associated with

cause

is

not

automatically incorporated into this exception's detail
message.

IOException

```java
public IOException​(
Throwable
cause)
```

Constructs an

IOException

with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).
This constructor is useful for IO exceptions that are little more
than wrappers for other throwables.

**Parameters:** cause

- The cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A null value is permitted,
and indicates that the cause is nonexistent or unknown.)
**Since:** 1.6

---

#### IOException

public IOException​(

Throwable

cause)

Constructs an

IOException

with the specified cause and a
detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).
This constructor is useful for IO exceptions that are little more
than wrappers for other throwables.

---

