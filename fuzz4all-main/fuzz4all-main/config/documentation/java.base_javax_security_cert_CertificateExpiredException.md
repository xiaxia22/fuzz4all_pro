# Class CertificateExpiredException

**Source:** `java.base\javax\security\cert\CertificateExpiredException.html`

### Class Description

```java
@Deprecated
(
since
="9")
public class
CertificateExpiredException

extends
CertificateException
```

Certificate Expired Exception. This is thrown whenever the current

Date

or the specified

Date

is after the

notAfter

date/time specified in the validity period
of the certificate.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertificateExpiredException()

Constructs a CertificateExpiredException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### public CertificateExpiredException​(
String
message)

Constructs a CertificateExpiredException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:**
- message

- the detail message.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class CertificateExpiredException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.security.cert.CertificateException
- - javax.security.cert.CertificateExpiredException

java.lang.Throwable

- java.lang.Exception
- - javax.security.cert.CertificateException
- - javax.security.cert.CertificateExpiredException

java.lang.Exception

- javax.security.cert.CertificateException
- - javax.security.cert.CertificateExpiredException

javax.security.cert.CertificateException

- javax.security.cert.CertificateExpiredException

javax.security.cert.CertificateExpiredException

**All Implemented Interfaces:** Serializable

```java
@Deprecated
(
since
="9")
public class
CertificateExpiredException

extends
CertificateException
```

Deprecated.

Use the classes in

java.security.cert

instead.

Certificate Expired Exception. This is thrown whenever the current

Date

or the specified

Date

is after the

notAfter

date/time specified in the validity period
of the certificate.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

**Since:** 1.4
**See Also:** Serialized Form

@Deprecated

(

since

="9")
public class

CertificateExpiredException

extends

CertificateException

Certificate Expired Exception. This is thrown whenever the current

Date

or the specified

Date

is after the

notAfter

date/time specified in the validity period
of the certificate.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertificateExpiredException

()

Deprecated.

Constructs a CertificateExpiredException with no detail message.

CertificateExpiredException

​(

String

message)

Deprecated.

Constructs a CertificateExpiredException with the specified detail
message.

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

CertificateExpiredException

()

Deprecated.

Constructs a CertificateExpiredException with no detail message.

CertificateExpiredException

​(

String

message)

Deprecated.

Constructs a CertificateExpiredException with the specified detail
message.

---

#### Constructor Summary

Deprecated.

Constructs a CertificateExpiredException with no detail message.

Constructs a CertificateExpiredException with the specified detail
message.

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

- CertificateExpiredException

```java
public CertificateExpiredException()
```

Deprecated.

Constructs a CertificateExpiredException with no detail message. A
detail message is a String that describes this particular
exception.

- CertificateExpiredException

```java
public CertificateExpiredException​(
String
message)
```

Deprecated.

Constructs a CertificateExpiredException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

Constructor Detail

- CertificateExpiredException

```java
public CertificateExpiredException()
```

Deprecated.

Constructs a CertificateExpiredException with no detail message. A
detail message is a String that describes this particular
exception.

- CertificateExpiredException

```java
public CertificateExpiredException​(
String
message)
```

Deprecated.

Constructs a CertificateExpiredException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

---

#### Constructor Detail

CertificateExpiredException

```java
public CertificateExpiredException()
```

Deprecated.

Constructs a CertificateExpiredException with no detail message. A
detail message is a String that describes this particular
exception.

---

#### CertificateExpiredException

public CertificateExpiredException()

Constructs a CertificateExpiredException with no detail message. A
detail message is a String that describes this particular
exception.

CertificateExpiredException

```java
public CertificateExpiredException​(
String
message)
```

Deprecated.

Constructs a CertificateExpiredException with the specified detail
message. A detail message is a String that describes this
particular exception.

**Parameters:** message

- the detail message.

---

#### CertificateExpiredException

public CertificateExpiredException​(

String

message)

Constructs a CertificateExpiredException with the specified detail
message. A detail message is a String that describes this
particular exception.

---

