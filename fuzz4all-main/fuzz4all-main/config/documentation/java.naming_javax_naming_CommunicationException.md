# Class CommunicationException

**Source:** `java.naming\javax\naming\CommunicationException.html`

### Class Description

```java
public class
CommunicationException

extends
NamingException
```

This exception is thrown when the client is
unable to communicate with the directory or naming service.
The inability to communicate with the service might be a result
of many factors, such as network partitioning, hardware or interface problems,
failures on either the client or server side.
This exception is meant to be used to capture such communication problems.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CommunicationException​(
String
explanation)

Constructs a new instance of CommunicationException using the
arguments supplied.

**Parameters:**
- explanation

- Additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public CommunicationException()

Constructs a new instance of CommunicationException.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class CommunicationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.CommunicationException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.CommunicationException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.CommunicationException

javax.naming.NamingException

- javax.naming.CommunicationException

javax.naming.CommunicationException

**All Implemented Interfaces:** Serializable

```java
public class
CommunicationException

extends
NamingException
```

This exception is thrown when the client is
unable to communicate with the directory or naming service.
The inability to communicate with the service might be a result
of many factors, such as network partitioning, hardware or interface problems,
failures on either the client or server side.
This exception is meant to be used to capture such communication problems.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

CommunicationException

extends

NamingException

This exception is thrown when the client is
unable to communicate with the directory or naming service.
The inability to communicate with the service might be a result
of many factors, such as network partitioning, hardware or interface problems,
failures on either the client or server side.
This exception is meant to be used to capture such communication problems.

Synchronization and serialization issues that apply to NamingException
apply directly here.

Synchronization and serialization issues that apply to NamingException
apply directly here.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CommunicationException

()

Constructs a new instance of CommunicationException.

CommunicationException

​(

String

explanation)

Constructs a new instance of CommunicationException using the
arguments supplied.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Field Summary

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Field Summary

Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Fields declared in class javax.naming. NamingException

Constructor Summary

Constructors

Constructor

Description

CommunicationException

()

Constructs a new instance of CommunicationException.

CommunicationException

​(

String

explanation)

Constructs a new instance of CommunicationException using the
arguments supplied.

---

#### Constructor Summary

Constructs a new instance of CommunicationException.

Constructs a new instance of CommunicationException using the
arguments supplied.

Method Summary

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

---

#### Methods declared in class javax.naming. NamingException

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

- CommunicationException

```java
public CommunicationException​(
String
explanation)
```

Constructs a new instance of CommunicationException using the
arguments supplied.

**Parameters:** explanation

- Additional detail about this exception.
**See Also:** Throwable.getMessage()

- CommunicationException

```java
public CommunicationException()
```

Constructs a new instance of CommunicationException.

Constructor Detail

- CommunicationException

```java
public CommunicationException​(
String
explanation)
```

Constructs a new instance of CommunicationException using the
arguments supplied.

**Parameters:** explanation

- Additional detail about this exception.
**See Also:** Throwable.getMessage()

- CommunicationException

```java
public CommunicationException()
```

Constructs a new instance of CommunicationException.

---

#### Constructor Detail

CommunicationException

```java
public CommunicationException​(
String
explanation)
```

Constructs a new instance of CommunicationException using the
arguments supplied.

**Parameters:** explanation

- Additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### CommunicationException

public CommunicationException​(

String

explanation)

Constructs a new instance of CommunicationException using the
arguments supplied.

CommunicationException

```java
public CommunicationException()
```

Constructs a new instance of CommunicationException.

---

#### CommunicationException

public CommunicationException()

Constructs a new instance of CommunicationException.

---

