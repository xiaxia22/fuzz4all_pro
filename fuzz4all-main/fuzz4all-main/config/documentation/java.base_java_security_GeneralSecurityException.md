# Class GeneralSecurityException

**Source:** `java.base\java\security\GeneralSecurityException.html`

### Class Description

```java
public class
GeneralSecurityException

extends
Exception
```

The

GeneralSecurityException

class is a generic
security exception class that provides type safety for all the
security-related exception classes that extend from it.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public GeneralSecurityException()

Constructs a GeneralSecurityException with no detail message.

---

#### public GeneralSecurityException​(
String
msg)

Constructs a GeneralSecurityException with the specified detail
message.
A detail message is a String that describes this particular
exception.

**Parameters:**
- msg

- the detail message.

---

#### public GeneralSecurityException​(
String
message,

Throwable
cause)

Creates a

GeneralSecurityException

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

#### public GeneralSecurityException​(
Throwable
cause)

Creates a

GeneralSecurityException

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

#### Class GeneralSecurityException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException

java.lang.Exception

- java.security.GeneralSecurityException

java.security.GeneralSecurityException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** BadPaddingException

,

CertificateException

,

CertPathBuilderException

,

CertPathValidatorException

,

CertStoreException

,

CRLException

,

DigestException

,

ExemptionMechanismException

,

IllegalBlockSizeException

,

InvalidAlgorithmParameterException

,

InvalidKeySpecException

,

InvalidParameterSpecException

,

KeyException

,

KeyStoreException

,

LoginException

,

NoSuchAlgorithmException

,

NoSuchPaddingException

,

NoSuchProviderException

,

ShortBufferException

,

SignatureException

,

UnrecoverableEntryException

```java
public class
GeneralSecurityException

extends
Exception
```

The

GeneralSecurityException

class is a generic
security exception class that provides type safety for all the
security-related exception classes that extend from it.

**Since:** 1.2
**See Also:** Serialized Form

public class

GeneralSecurityException

extends

Exception

The

GeneralSecurityException

class is a generic
security exception class that provides type safety for all the
security-related exception classes that extend from it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GeneralSecurityException

()

Constructs a GeneralSecurityException with no detail message.

GeneralSecurityException

​(

String

msg)

Constructs a GeneralSecurityException with the specified detail
message.

GeneralSecurityException

​(

String

message,

Throwable

cause)

Creates a

GeneralSecurityException

with the specified
detail message and cause.

GeneralSecurityException

​(

Throwable

cause)

Creates a

GeneralSecurityException

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

GeneralSecurityException

()

Constructs a GeneralSecurityException with no detail message.

GeneralSecurityException

​(

String

msg)

Constructs a GeneralSecurityException with the specified detail
message.

GeneralSecurityException

​(

String

message,

Throwable

cause)

Creates a

GeneralSecurityException

with the specified
detail message and cause.

GeneralSecurityException

​(

Throwable

cause)

Creates a

GeneralSecurityException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a GeneralSecurityException with no detail message.

Constructs a GeneralSecurityException with the specified detail
message.

Creates a

GeneralSecurityException

with the specified
detail message and cause.

Creates a

GeneralSecurityException

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

- GeneralSecurityException

```java
public GeneralSecurityException()
```

Constructs a GeneralSecurityException with no detail message.

- GeneralSecurityException

```java
public GeneralSecurityException​(
String
msg)
```

Constructs a GeneralSecurityException with the specified detail
message.
A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

- GeneralSecurityException

```java
public GeneralSecurityException​(
String
message,

Throwable
cause)
```

Creates a

GeneralSecurityException

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

- GeneralSecurityException

```java
public GeneralSecurityException​(
Throwable
cause)
```

Creates a

GeneralSecurityException

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

- GeneralSecurityException

```java
public GeneralSecurityException()
```

Constructs a GeneralSecurityException with no detail message.

- GeneralSecurityException

```java
public GeneralSecurityException​(
String
msg)
```

Constructs a GeneralSecurityException with the specified detail
message.
A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

- GeneralSecurityException

```java
public GeneralSecurityException​(
String
message,

Throwable
cause)
```

Creates a

GeneralSecurityException

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

- GeneralSecurityException

```java
public GeneralSecurityException​(
Throwable
cause)
```

Creates a

GeneralSecurityException

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

GeneralSecurityException

```java
public GeneralSecurityException()
```

Constructs a GeneralSecurityException with no detail message.

---

#### GeneralSecurityException

public GeneralSecurityException()

Constructs a GeneralSecurityException with no detail message.

GeneralSecurityException

```java
public GeneralSecurityException​(
String
msg)
```

Constructs a GeneralSecurityException with the specified detail
message.
A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

---

#### GeneralSecurityException

public GeneralSecurityException​(

String

msg)

Constructs a GeneralSecurityException with the specified detail
message.
A detail message is a String that describes this particular
exception.

GeneralSecurityException

```java
public GeneralSecurityException​(
String
message,

Throwable
cause)
```

Creates a

GeneralSecurityException

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

#### GeneralSecurityException

public GeneralSecurityException​(

String

message,

Throwable

cause)

Creates a

GeneralSecurityException

with the specified
detail message and cause.

GeneralSecurityException

```java
public GeneralSecurityException​(
Throwable
cause)
```

Creates a

GeneralSecurityException

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

#### GeneralSecurityException

public GeneralSecurityException​(

Throwable

cause)

Creates a

GeneralSecurityException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

