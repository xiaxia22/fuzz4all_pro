# Class ServiceUnavailableException

**Source:** `java.naming\javax\naming\ServiceUnavailableException.html`

### Class Description

```java
public class
ServiceUnavailableException

extends
NamingException
```

This exception is thrown when attempting to communicate with a
directory or naming service and that service is not available.
It might be unavailable for different reasons. For example,
the server might be too busy to service the request, or the server
might not be registered to service any requests, etc.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ServiceUnavailableException​(
String
explanation)

Constructs a new instance of ServiceUnavailableException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public ServiceUnavailableException()

Constructs a new instance of ServiceUnavailableException.
All fields default to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ServiceUnavailableException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ServiceUnavailableException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ServiceUnavailableException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.ServiceUnavailableException

javax.naming.NamingException

- javax.naming.ServiceUnavailableException

javax.naming.ServiceUnavailableException

**All Implemented Interfaces:** Serializable

```java
public class
ServiceUnavailableException

extends
NamingException
```

This exception is thrown when attempting to communicate with a
directory or naming service and that service is not available.
It might be unavailable for different reasons. For example,
the server might be too busy to service the request, or the server
might not be registered to service any requests, etc.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

ServiceUnavailableException

extends

NamingException

This exception is thrown when attempting to communicate with a
directory or naming service and that service is not available.
It might be unavailable for different reasons. For example,
the server might be too busy to service the request, or the server
might not be registered to service any requests, etc.

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

ServiceUnavailableException

()

Constructs a new instance of ServiceUnavailableException.

ServiceUnavailableException

​(

String

explanation)

Constructs a new instance of ServiceUnavailableException using an
explanation.

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

ServiceUnavailableException

()

Constructs a new instance of ServiceUnavailableException.

ServiceUnavailableException

​(

String

explanation)

Constructs a new instance of ServiceUnavailableException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of ServiceUnavailableException.

Constructs a new instance of ServiceUnavailableException using an
explanation.

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

- ServiceUnavailableException

```java
public ServiceUnavailableException​(
String
explanation)
```

Constructs a new instance of ServiceUnavailableException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- ServiceUnavailableException

```java
public ServiceUnavailableException()
```

Constructs a new instance of ServiceUnavailableException.
All fields default to null.

Constructor Detail

- ServiceUnavailableException

```java
public ServiceUnavailableException​(
String
explanation)
```

Constructs a new instance of ServiceUnavailableException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- ServiceUnavailableException

```java
public ServiceUnavailableException()
```

Constructs a new instance of ServiceUnavailableException.
All fields default to null.

---

#### Constructor Detail

ServiceUnavailableException

```java
public ServiceUnavailableException​(
String
explanation)
```

Constructs a new instance of ServiceUnavailableException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### ServiceUnavailableException

public ServiceUnavailableException​(

String

explanation)

Constructs a new instance of ServiceUnavailableException using an
explanation. All other fields default to null.

ServiceUnavailableException

```java
public ServiceUnavailableException()
```

Constructs a new instance of ServiceUnavailableException.
All fields default to null.

---

#### ServiceUnavailableException

public ServiceUnavailableException()

Constructs a new instance of ServiceUnavailableException.
All fields default to null.

---

