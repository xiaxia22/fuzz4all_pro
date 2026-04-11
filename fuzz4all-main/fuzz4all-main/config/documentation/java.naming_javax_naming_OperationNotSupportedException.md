# Class OperationNotSupportedException

**Source:** `java.naming\javax\naming\OperationNotSupportedException.html`

### Class Description

```java
public class
OperationNotSupportedException

extends
NamingException
```

This exception is thrown when a context implementation does not support
the operation being invoked.
For example, if a server does not support the Context.bind() method
it would throw OperationNotSupportedException when the bind() method
is invoked on it.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public OperationNotSupportedException()

Constructs a new instance of OperationNotSupportedException.
All fields default to null.

---

#### public OperationNotSupportedException​(
String
explanation)

Constructs a new instance of OperationNotSupportedException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception

**See Also:**
- Throwable.getMessage()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class OperationNotSupportedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.OperationNotSupportedException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.OperationNotSupportedException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.OperationNotSupportedException

javax.naming.NamingException

- javax.naming.OperationNotSupportedException

javax.naming.OperationNotSupportedException

**All Implemented Interfaces:** Serializable

```java
public class
OperationNotSupportedException

extends
NamingException
```

This exception is thrown when a context implementation does not support
the operation being invoked.
For example, if a server does not support the Context.bind() method
it would throw OperationNotSupportedException when the bind() method
is invoked on it.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

OperationNotSupportedException

extends

NamingException

This exception is thrown when a context implementation does not support
the operation being invoked.
For example, if a server does not support the Context.bind() method
it would throw OperationNotSupportedException when the bind() method
is invoked on it.

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

OperationNotSupportedException

()

Constructs a new instance of OperationNotSupportedException.

OperationNotSupportedException

​(

String

explanation)

Constructs a new instance of OperationNotSupportedException using an
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

OperationNotSupportedException

()

Constructs a new instance of OperationNotSupportedException.

OperationNotSupportedException

​(

String

explanation)

Constructs a new instance of OperationNotSupportedException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of OperationNotSupportedException.

Constructs a new instance of OperationNotSupportedException using an
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

- OperationNotSupportedException

```java
public OperationNotSupportedException()
```

Constructs a new instance of OperationNotSupportedException.
All fields default to null.

- OperationNotSupportedException

```java
public OperationNotSupportedException​(
String
explanation)
```

Constructs a new instance of OperationNotSupportedException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception
**See Also:** Throwable.getMessage()

Constructor Detail

- OperationNotSupportedException

```java
public OperationNotSupportedException()
```

Constructs a new instance of OperationNotSupportedException.
All fields default to null.

- OperationNotSupportedException

```java
public OperationNotSupportedException​(
String
explanation)
```

Constructs a new instance of OperationNotSupportedException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception
**See Also:** Throwable.getMessage()

---

#### Constructor Detail

OperationNotSupportedException

```java
public OperationNotSupportedException()
```

Constructs a new instance of OperationNotSupportedException.
All fields default to null.

---

#### OperationNotSupportedException

public OperationNotSupportedException()

Constructs a new instance of OperationNotSupportedException.
All fields default to null.

OperationNotSupportedException

```java
public OperationNotSupportedException​(
String
explanation)
```

Constructs a new instance of OperationNotSupportedException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception
**See Also:** Throwable.getMessage()

---

#### OperationNotSupportedException

public OperationNotSupportedException​(

String

explanation)

Constructs a new instance of OperationNotSupportedException using an
explanation. All other fields default to null.

---

