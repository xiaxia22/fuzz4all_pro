# Class NamingSecurityException

**Source:** `java.naming\javax\naming\NamingSecurityException.html`

### Class Description

```java
public abstract class
NamingSecurityException

extends
NamingException
```

This is the superclass of security-related exceptions
thrown by operations in the Context and DirContext interfaces.
The nature of the failure is described by the name of the subclass.

If the program wants to handle this exception in particular, it
should catch NamingSecurityException explicitly before attempting to
catch NamingException. A program might want to do this, for example,
if it wants to treat security-related exceptions specially from
other sorts of naming exception.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NamingSecurityException​(
String
explanation)

Constructs a new instance of NamingSecurityException using the
explanation supplied. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public NamingSecurityException()

Constructs a new instance of NamingSecurityException.
All fields are initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NamingSecurityException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NamingSecurityException

javax.naming.NamingException

- javax.naming.NamingSecurityException

javax.naming.NamingSecurityException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AuthenticationException

,

AuthenticationNotSupportedException

,

NoPermissionException

```java
public abstract class
NamingSecurityException

extends
NamingException
```

This is the superclass of security-related exceptions
thrown by operations in the Context and DirContext interfaces.
The nature of the failure is described by the name of the subclass.

If the program wants to handle this exception in particular, it
should catch NamingSecurityException explicitly before attempting to
catch NamingException. A program might want to do this, for example,
if it wants to treat security-related exceptions specially from
other sorts of naming exception.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public abstract class

NamingSecurityException

extends

NamingException

This is the superclass of security-related exceptions
thrown by operations in the Context and DirContext interfaces.
The nature of the failure is described by the name of the subclass.

If the program wants to handle this exception in particular, it
should catch NamingSecurityException explicitly before attempting to
catch NamingException. A program might want to do this, for example,
if it wants to treat security-related exceptions specially from
other sorts of naming exception.

Synchronization and serialization issues that apply to NamingException
apply directly here.

If the program wants to handle this exception in particular, it
should catch NamingSecurityException explicitly before attempting to
catch NamingException. A program might want to do this, for example,
if it wants to treat security-related exceptions specially from
other sorts of naming exception.

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

NamingSecurityException

()

Constructs a new instance of NamingSecurityException.

NamingSecurityException

​(

String

explanation)

Constructs a new instance of NamingSecurityException using the
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

NamingSecurityException

()

Constructs a new instance of NamingSecurityException.

NamingSecurityException

​(

String

explanation)

Constructs a new instance of NamingSecurityException using the
explanation supplied.

---

#### Constructor Summary

Constructs a new instance of NamingSecurityException.

Constructs a new instance of NamingSecurityException using the
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

- NamingSecurityException

```java
public NamingSecurityException​(
String
explanation)
```

Constructs a new instance of NamingSecurityException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- NamingSecurityException

```java
public NamingSecurityException()
```

Constructs a new instance of NamingSecurityException.
All fields are initialized to null.

Constructor Detail

- NamingSecurityException

```java
public NamingSecurityException​(
String
explanation)
```

Constructs a new instance of NamingSecurityException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- NamingSecurityException

```java
public NamingSecurityException()
```

Constructs a new instance of NamingSecurityException.
All fields are initialized to null.

---

#### Constructor Detail

NamingSecurityException

```java
public NamingSecurityException​(
String
explanation)
```

Constructs a new instance of NamingSecurityException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### NamingSecurityException

public NamingSecurityException​(

String

explanation)

Constructs a new instance of NamingSecurityException using the
explanation supplied. All other fields default to null.

NamingSecurityException

```java
public NamingSecurityException()
```

Constructs a new instance of NamingSecurityException.
All fields are initialized to null.

---

#### NamingSecurityException

public NamingSecurityException()

Constructs a new instance of NamingSecurityException.
All fields are initialized to null.

---

