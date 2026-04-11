# Class NoPermissionException

**Source:** `java.naming\javax\naming\NoPermissionException.html`

### Class Description

```java
public class
NoPermissionException

extends
NamingSecurityException
```

This exception is thrown when attempting to perform an operation
for which the client has no permission. The access control/permission
model is dictated by the directory/naming server.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NoPermissionException​(
String
explanation)

Constructs a new instance of NoPermissionException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

---

#### public NoPermissionException()

Constructs a new instance of NoPermissionException.
All fields are initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NoPermissionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.NoPermissionException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.NoPermissionException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.NoPermissionException

javax.naming.NamingException

- javax.naming.NamingSecurityException
- - javax.naming.NoPermissionException

javax.naming.NamingSecurityException

- javax.naming.NoPermissionException

javax.naming.NoPermissionException

**All Implemented Interfaces:** Serializable

```java
public class
NoPermissionException

extends
NamingSecurityException
```

This exception is thrown when attempting to perform an operation
for which the client has no permission. The access control/permission
model is dictated by the directory/naming server.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

NoPermissionException

extends

NamingSecurityException

This exception is thrown when attempting to perform an operation
for which the client has no permission. The access control/permission
model is dictated by the directory/naming server.

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

NoPermissionException

()

Constructs a new instance of NoPermissionException.

NoPermissionException

​(

String

explanation)

Constructs a new instance of NoPermissionException using an
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

NoPermissionException

()

Constructs a new instance of NoPermissionException.

NoPermissionException

​(

String

explanation)

Constructs a new instance of NoPermissionException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of NoPermissionException.

Constructs a new instance of NoPermissionException using an
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

- NoPermissionException

```java
public NoPermissionException​(
String
explanation)
```

Constructs a new instance of NoPermissionException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.

- NoPermissionException

```java
public NoPermissionException()
```

Constructs a new instance of NoPermissionException.
All fields are initialized to null.

Constructor Detail

- NoPermissionException

```java
public NoPermissionException​(
String
explanation)
```

Constructs a new instance of NoPermissionException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.

- NoPermissionException

```java
public NoPermissionException()
```

Constructs a new instance of NoPermissionException.
All fields are initialized to null.

---

#### Constructor Detail

NoPermissionException

```java
public NoPermissionException​(
String
explanation)
```

Constructs a new instance of NoPermissionException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.

---

#### NoPermissionException

public NoPermissionException​(

String

explanation)

Constructs a new instance of NoPermissionException using an
explanation. All other fields default to null.

NoPermissionException

```java
public NoPermissionException()
```

Constructs a new instance of NoPermissionException.
All fields are initialized to null.

---

#### NoPermissionException

public NoPermissionException()

Constructs a new instance of NoPermissionException.
All fields are initialized to null.

---

