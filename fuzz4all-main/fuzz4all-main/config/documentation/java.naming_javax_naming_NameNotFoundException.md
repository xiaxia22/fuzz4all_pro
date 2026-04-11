# Class NameNotFoundException

**Source:** `java.naming\javax\naming\NameNotFoundException.html`

### Class Description

```java
public class
NameNotFoundException

extends
NamingException
```

This exception is thrown when a component of the name cannot be resolved
because it is not bound.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NameNotFoundException​(
String
explanation)

Constructs a new instance of NameNotFoundException using the
explanation supplied. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about
this exception.

**See Also:**
- Throwable.getMessage()

---

#### public NameNotFoundException()

Constructs a new instance of NameNotFoundException.
all name resolution fields and explanation initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NameNotFoundException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NameNotFoundException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NameNotFoundException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NameNotFoundException

javax.naming.NamingException

- javax.naming.NameNotFoundException

javax.naming.NameNotFoundException

**All Implemented Interfaces:** Serializable

```java
public class
NameNotFoundException

extends
NamingException
```

This exception is thrown when a component of the name cannot be resolved
because it is not bound.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

NameNotFoundException

extends

NamingException

This exception is thrown when a component of the name cannot be resolved
because it is not bound.

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

NameNotFoundException

()

Constructs a new instance of NameNotFoundException.

NameNotFoundException

​(

String

explanation)

Constructs a new instance of NameNotFoundException using the
explanation supplied.

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

NameNotFoundException

()

Constructs a new instance of NameNotFoundException.

NameNotFoundException

​(

String

explanation)

Constructs a new instance of NameNotFoundException using the
explanation supplied.

---

#### Constructor Summary

Constructs a new instance of NameNotFoundException.

Constructs a new instance of NameNotFoundException using the
explanation supplied.

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

- NameNotFoundException

```java
public NameNotFoundException​(
String
explanation)
```

Constructs a new instance of NameNotFoundException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about
this exception.
**See Also:** Throwable.getMessage()

- NameNotFoundException

```java
public NameNotFoundException()
```

Constructs a new instance of NameNotFoundException.
all name resolution fields and explanation initialized to null.

Constructor Detail

- NameNotFoundException

```java
public NameNotFoundException​(
String
explanation)
```

Constructs a new instance of NameNotFoundException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about
this exception.
**See Also:** Throwable.getMessage()

- NameNotFoundException

```java
public NameNotFoundException()
```

Constructs a new instance of NameNotFoundException.
all name resolution fields and explanation initialized to null.

---

#### Constructor Detail

NameNotFoundException

```java
public NameNotFoundException​(
String
explanation)
```

Constructs a new instance of NameNotFoundException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about
this exception.
**See Also:** Throwable.getMessage()

---

#### NameNotFoundException

public NameNotFoundException​(

String

explanation)

Constructs a new instance of NameNotFoundException using the
explanation supplied. All other fields default to null.

NameNotFoundException

```java
public NameNotFoundException()
```

Constructs a new instance of NameNotFoundException.
all name resolution fields and explanation initialized to null.

---

#### NameNotFoundException

public NameNotFoundException()

Constructs a new instance of NameNotFoundException.
all name resolution fields and explanation initialized to null.

---

