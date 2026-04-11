# Class TimeLimitExceededException

**Source:** `java.naming\javax\naming\TimeLimitExceededException.html`

### Class Description

```java
public class
TimeLimitExceededException

extends
LimitExceededException
```

This exception is thrown when a method
does not terminate within the specified time limit.
This can happen, for example, if the user specifies that
the method should take no longer than 10 seconds, and the
method fails to complete with 10 seconds.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TimeLimitExceededException()

Constructs a new instance of TimeLimitExceededException.
All fields default to null.

---

#### public TimeLimitExceededException​(
String
explanation)

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

**Parameters:**
- explanation

- possibly null detail about this exception.

**See Also:**
- Throwable.getMessage()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class TimeLimitExceededException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LimitExceededException
- - javax.naming.TimeLimitExceededException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LimitExceededException
- - javax.naming.TimeLimitExceededException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.LimitExceededException
- - javax.naming.TimeLimitExceededException

javax.naming.NamingException

- javax.naming.LimitExceededException
- - javax.naming.TimeLimitExceededException

javax.naming.LimitExceededException

- javax.naming.TimeLimitExceededException

javax.naming.TimeLimitExceededException

**All Implemented Interfaces:** Serializable

```java
public class
TimeLimitExceededException

extends
LimitExceededException
```

This exception is thrown when a method
does not terminate within the specified time limit.
This can happen, for example, if the user specifies that
the method should take no longer than 10 seconds, and the
method fails to complete with 10 seconds.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

TimeLimitExceededException

extends

LimitExceededException

This exception is thrown when a method
does not terminate within the specified time limit.
This can happen, for example, if the user specifies that
the method should take no longer than 10 seconds, and the
method fails to complete with 10 seconds.

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

TimeLimitExceededException

()

Constructs a new instance of TimeLimitExceededException.

TimeLimitExceededException

​(

String

explanation)

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

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

TimeLimitExceededException

()

Constructs a new instance of TimeLimitExceededException.

TimeLimitExceededException

​(

String

explanation)

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

---

#### Constructor Summary

Constructs a new instance of TimeLimitExceededException.

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

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

- TimeLimitExceededException

```java
public TimeLimitExceededException()
```

Constructs a new instance of TimeLimitExceededException.
All fields default to null.

- TimeLimitExceededException

```java
public TimeLimitExceededException​(
String
explanation)
```

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

**Parameters:** explanation

- possibly null detail about this exception.
**See Also:** Throwable.getMessage()

Constructor Detail

- TimeLimitExceededException

```java
public TimeLimitExceededException()
```

Constructs a new instance of TimeLimitExceededException.
All fields default to null.

- TimeLimitExceededException

```java
public TimeLimitExceededException​(
String
explanation)
```

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

**Parameters:** explanation

- possibly null detail about this exception.
**See Also:** Throwable.getMessage()

---

#### Constructor Detail

TimeLimitExceededException

```java
public TimeLimitExceededException()
```

Constructs a new instance of TimeLimitExceededException.
All fields default to null.

---

#### TimeLimitExceededException

public TimeLimitExceededException()

Constructs a new instance of TimeLimitExceededException.
All fields default to null.

TimeLimitExceededException

```java
public TimeLimitExceededException​(
String
explanation)
```

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

**Parameters:** explanation

- possibly null detail about this exception.
**See Also:** Throwable.getMessage()

---

#### TimeLimitExceededException

public TimeLimitExceededException​(

String

explanation)

Constructs a new instance of TimeLimitExceededException
using the argument supplied.

---

