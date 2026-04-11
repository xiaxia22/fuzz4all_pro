# Class InvalidSearchControlsException

**Source:** `java.naming\javax\naming\directory\InvalidSearchControlsException.html`

### Class Description

```java
public class
InvalidSearchControlsException

extends
NamingException
```

This exception is thrown when the specification of
the SearchControls for a search operation is invalid. For example, if the scope is
set to a value other than OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE,
this exception is thrown.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidSearchControlsException()

Constructs a new instance of InvalidSearchControlsException.
All fields are set to null.

---

#### public InvalidSearchControlsException​(
String
msg)

Constructs a new instance of InvalidSearchControlsException
with an explanation. All other fields set to null.

**Parameters:**
- msg

- Detail about this exception. Can be null.

**See Also:**
- Throwable.getMessage()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InvalidSearchControlsException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.InvalidSearchControlsException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.InvalidSearchControlsException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.directory.InvalidSearchControlsException

javax.naming.NamingException

- javax.naming.directory.InvalidSearchControlsException

javax.naming.directory.InvalidSearchControlsException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidSearchControlsException

extends
NamingException
```

This exception is thrown when the specification of
the SearchControls for a search operation is invalid. For example, if the scope is
set to a value other than OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE,
this exception is thrown.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

InvalidSearchControlsException

extends

NamingException

This exception is thrown when the specification of
the SearchControls for a search operation is invalid. For example, if the scope is
set to a value other than OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE,
this exception is thrown.

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

InvalidSearchControlsException

()

Constructs a new instance of InvalidSearchControlsException.

InvalidSearchControlsException

​(

String

msg)

Constructs a new instance of InvalidSearchControlsException
with an explanation.

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

InvalidSearchControlsException

()

Constructs a new instance of InvalidSearchControlsException.

InvalidSearchControlsException

​(

String

msg)

Constructs a new instance of InvalidSearchControlsException
with an explanation.

---

#### Constructor Summary

Constructs a new instance of InvalidSearchControlsException.

Constructs a new instance of InvalidSearchControlsException
with an explanation.

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

- InvalidSearchControlsException

```java
public InvalidSearchControlsException()
```

Constructs a new instance of InvalidSearchControlsException.
All fields are set to null.

- InvalidSearchControlsException

```java
public InvalidSearchControlsException​(
String
msg)
```

Constructs a new instance of InvalidSearchControlsException
with an explanation. All other fields set to null.

**Parameters:** msg

- Detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

Constructor Detail

- InvalidSearchControlsException

```java
public InvalidSearchControlsException()
```

Constructs a new instance of InvalidSearchControlsException.
All fields are set to null.

- InvalidSearchControlsException

```java
public InvalidSearchControlsException​(
String
msg)
```

Constructs a new instance of InvalidSearchControlsException
with an explanation. All other fields set to null.

**Parameters:** msg

- Detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### Constructor Detail

InvalidSearchControlsException

```java
public InvalidSearchControlsException()
```

Constructs a new instance of InvalidSearchControlsException.
All fields are set to null.

---

#### InvalidSearchControlsException

public InvalidSearchControlsException()

Constructs a new instance of InvalidSearchControlsException.
All fields are set to null.

InvalidSearchControlsException

```java
public InvalidSearchControlsException​(
String
msg)
```

Constructs a new instance of InvalidSearchControlsException
with an explanation. All other fields set to null.

**Parameters:** msg

- Detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### InvalidSearchControlsException

public InvalidSearchControlsException​(

String

msg)

Constructs a new instance of InvalidSearchControlsException
with an explanation. All other fields set to null.

---

