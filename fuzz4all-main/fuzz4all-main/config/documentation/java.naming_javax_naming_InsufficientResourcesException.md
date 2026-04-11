# Class InsufficientResourcesException

**Source:** `java.naming\javax\naming\InsufficientResourcesException.html`

### Class Description

```java
public class
InsufficientResourcesException

extends
NamingException
```

This exception is thrown when resources are not available to complete
the requested operation. This might due to a lack of resources on
the server or on the client. There are no restrictions to resource types,
as different services might make use of different resources. Such
restrictions might be due to physical limits and/or administrative quotas.
Examples of limited resources are internal buffers, memory, network bandwidth.

InsufficientResourcesException is different from LimitExceededException in that
the latter is due to user/system specified limits. See LimitExceededException
for details.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InsufficientResourcesException​(
String
explanation)

Constructs a new instance of InsufficientResourcesException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public InsufficientResourcesException()

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InsufficientResourcesException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.InsufficientResourcesException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.InsufficientResourcesException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.InsufficientResourcesException

javax.naming.NamingException

- javax.naming.InsufficientResourcesException

javax.naming.InsufficientResourcesException

**All Implemented Interfaces:** Serializable

```java
public class
InsufficientResourcesException

extends
NamingException
```

This exception is thrown when resources are not available to complete
the requested operation. This might due to a lack of resources on
the server or on the client. There are no restrictions to resource types,
as different services might make use of different resources. Such
restrictions might be due to physical limits and/or administrative quotas.
Examples of limited resources are internal buffers, memory, network bandwidth.

InsufficientResourcesException is different from LimitExceededException in that
the latter is due to user/system specified limits. See LimitExceededException
for details.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

InsufficientResourcesException

extends

NamingException

This exception is thrown when resources are not available to complete
the requested operation. This might due to a lack of resources on
the server or on the client. There are no restrictions to resource types,
as different services might make use of different resources. Such
restrictions might be due to physical limits and/or administrative quotas.
Examples of limited resources are internal buffers, memory, network bandwidth.

InsufficientResourcesException is different from LimitExceededException in that
the latter is due to user/system specified limits. See LimitExceededException
for details.

Synchronization and serialization issues that apply to NamingException
apply directly here.

InsufficientResourcesException is different from LimitExceededException in that
the latter is due to user/system specified limits. See LimitExceededException
for details.

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

InsufficientResourcesException

()

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

InsufficientResourcesException

​(

String

explanation)

Constructs a new instance of InsufficientResourcesException using an
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

InsufficientResourcesException

()

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

InsufficientResourcesException

​(

String

explanation)

Constructs a new instance of InsufficientResourcesException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

Constructs a new instance of InsufficientResourcesException using an
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

- InsufficientResourcesException

```java
public InsufficientResourcesException​(
String
explanation)
```

Constructs a new instance of InsufficientResourcesException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- InsufficientResourcesException

```java
public InsufficientResourcesException()
```

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

Constructor Detail

- InsufficientResourcesException

```java
public InsufficientResourcesException​(
String
explanation)
```

Constructs a new instance of InsufficientResourcesException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- InsufficientResourcesException

```java
public InsufficientResourcesException()
```

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

---

#### Constructor Detail

InsufficientResourcesException

```java
public InsufficientResourcesException​(
String
explanation)
```

Constructs a new instance of InsufficientResourcesException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### InsufficientResourcesException

public InsufficientResourcesException​(

String

explanation)

Constructs a new instance of InsufficientResourcesException using an
explanation. All other fields default to null.

InsufficientResourcesException

```java
public InsufficientResourcesException()
```

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

---

#### InsufficientResourcesException

public InsufficientResourcesException()

Constructs a new instance of InsufficientResourcesException with
all name resolution fields and explanation initialized to null.

---

