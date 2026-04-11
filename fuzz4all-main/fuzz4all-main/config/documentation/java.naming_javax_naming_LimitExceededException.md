# Class LimitExceededException

**Source:** `java.naming\javax\naming\LimitExceededException.html`

### Class Description

```java
public class
LimitExceededException

extends
NamingException
```

This exception is thrown when a method
terminates abnormally due to a user or system specified limit.
This is different from a InsufficientResourceException in that
LimitExceededException is due to a user/system specified limit.
For example, running out of memory to complete the request would
be an insufficient resource. The client asking for 10 answers and
getting back 11 is a size limit exception.

Examples of these limits include client and server configuration
limits such as size, time, number of hops, etc.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public LimitExceededException()

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

---

#### public LimitExceededException​(
String
explanation)

Constructs a new instance of LimitExceededException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null detail about this exception.

**See Also:**
- Throwable.getMessage()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class LimitExceededException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LimitExceededException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LimitExceededException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.LimitExceededException

javax.naming.NamingException

- javax.naming.LimitExceededException

javax.naming.LimitExceededException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** SizeLimitExceededException

,

TimeLimitExceededException

```java
public class
LimitExceededException

extends
NamingException
```

This exception is thrown when a method
terminates abnormally due to a user or system specified limit.
This is different from a InsufficientResourceException in that
LimitExceededException is due to a user/system specified limit.
For example, running out of memory to complete the request would
be an insufficient resource. The client asking for 10 answers and
getting back 11 is a size limit exception.

Examples of these limits include client and server configuration
limits such as size, time, number of hops, etc.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

LimitExceededException

extends

NamingException

This exception is thrown when a method
terminates abnormally due to a user or system specified limit.
This is different from a InsufficientResourceException in that
LimitExceededException is due to a user/system specified limit.
For example, running out of memory to complete the request would
be an insufficient resource. The client asking for 10 answers and
getting back 11 is a size limit exception.

Examples of these limits include client and server configuration
limits such as size, time, number of hops, etc.

Synchronization and serialization issues that apply to NamingException
apply directly here.

Examples of these limits include client and server configuration
limits such as size, time, number of hops, etc.

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

LimitExceededException

()

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

LimitExceededException

​(

String

explanation)

Constructs a new instance of LimitExceededException using an
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

LimitExceededException

()

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

LimitExceededException

​(

String

explanation)

Constructs a new instance of LimitExceededException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

Constructs a new instance of LimitExceededException using an
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

- LimitExceededException

```java
public LimitExceededException()
```

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

- LimitExceededException

```java
public LimitExceededException​(
String
explanation)
```

Constructs a new instance of LimitExceededException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null detail about this exception.
**See Also:** Throwable.getMessage()

Constructor Detail

- LimitExceededException

```java
public LimitExceededException()
```

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

- LimitExceededException

```java
public LimitExceededException​(
String
explanation)
```

Constructs a new instance of LimitExceededException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null detail about this exception.
**See Also:** Throwable.getMessage()

---

#### Constructor Detail

LimitExceededException

```java
public LimitExceededException()
```

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

---

#### LimitExceededException

public LimitExceededException()

Constructs a new instance of LimitExceededException with
all name resolution fields and explanation initialized to null.

LimitExceededException

```java
public LimitExceededException​(
String
explanation)
```

Constructs a new instance of LimitExceededException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null detail about this exception.
**See Also:** Throwable.getMessage()

---

#### LimitExceededException

public LimitExceededException​(

String

explanation)

Constructs a new instance of LimitExceededException using an
explanation. All other fields default to null.

---

