# Class SizeLimitExceededException

**Source:** `java.naming\javax\naming\SizeLimitExceededException.html`

### Class Description

```java
public class
SizeLimitExceededException

extends
LimitExceededException
```

This exception is thrown when a method
produces a result that exceeds a size-related limit.
This can happen, for example, if the result contains
more objects than the user requested, or when the size
of the result exceeds some implementation-specific limit.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SizeLimitExceededException()

Constructs a new instance of SizeLimitExceededException.
All fields default to null.

---

#### public SizeLimitExceededException​(
String
explanation)

Constructs a new instance of SizeLimitExceededException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null detail about this exception.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SizeLimitExceededException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LimitExceededException
- - javax.naming.SizeLimitExceededException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LimitExceededException
- - javax.naming.SizeLimitExceededException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.LimitExceededException
- - javax.naming.SizeLimitExceededException

javax.naming.NamingException

- javax.naming.LimitExceededException
- - javax.naming.SizeLimitExceededException

javax.naming.LimitExceededException

- javax.naming.SizeLimitExceededException

javax.naming.SizeLimitExceededException

**All Implemented Interfaces:** Serializable

```java
public class
SizeLimitExceededException

extends
LimitExceededException
```

This exception is thrown when a method
produces a result that exceeds a size-related limit.
This can happen, for example, if the result contains
more objects than the user requested, or when the size
of the result exceeds some implementation-specific limit.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

SizeLimitExceededException

extends

LimitExceededException

This exception is thrown when a method
produces a result that exceeds a size-related limit.
This can happen, for example, if the result contains
more objects than the user requested, or when the size
of the result exceeds some implementation-specific limit.

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

SizeLimitExceededException

()

Constructs a new instance of SizeLimitExceededException.

SizeLimitExceededException

​(

String

explanation)

Constructs a new instance of SizeLimitExceededException using an
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

SizeLimitExceededException

()

Constructs a new instance of SizeLimitExceededException.

SizeLimitExceededException

​(

String

explanation)

Constructs a new instance of SizeLimitExceededException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of SizeLimitExceededException.

Constructs a new instance of SizeLimitExceededException using an
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

- SizeLimitExceededException

```java
public SizeLimitExceededException()
```

Constructs a new instance of SizeLimitExceededException.
All fields default to null.

- SizeLimitExceededException

```java
public SizeLimitExceededException​(
String
explanation)
```

Constructs a new instance of SizeLimitExceededException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null detail about this exception.

Constructor Detail

- SizeLimitExceededException

```java
public SizeLimitExceededException()
```

Constructs a new instance of SizeLimitExceededException.
All fields default to null.

- SizeLimitExceededException

```java
public SizeLimitExceededException​(
String
explanation)
```

Constructs a new instance of SizeLimitExceededException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null detail about this exception.

---

#### Constructor Detail

SizeLimitExceededException

```java
public SizeLimitExceededException()
```

Constructs a new instance of SizeLimitExceededException.
All fields default to null.

---

#### SizeLimitExceededException

public SizeLimitExceededException()

Constructs a new instance of SizeLimitExceededException.
All fields default to null.

SizeLimitExceededException

```java
public SizeLimitExceededException​(
String
explanation)
```

Constructs a new instance of SizeLimitExceededException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null detail about this exception.

---

#### SizeLimitExceededException

public SizeLimitExceededException​(

String

explanation)

Constructs a new instance of SizeLimitExceededException using an
explanation. All other fields default to null.

---

