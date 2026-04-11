# Class AuthenticationException

**Source:** `java.naming\javax\naming\AuthenticationException.html`

### Class Description

```java
public class
AuthenticationException

extends
NamingSecurityException
```

This exception is thrown when an authentication error occurs while
accessing the naming or directory service.
An authentication error can happen, for example, when the credentials
supplied by the user program are invalid or otherwise fail to
authenticate the user to the naming/directory service.

If the program wants to handle this exception in particular, it
should catch AuthenticationException explicitly before attempting to
catch NamingException. After catching AuthenticationException, the
program could reattempt the authentication by updating
the resolved context's environment properties with the appropriate
credentials.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AuthenticationException​(
String
explanation)

Constructs a new instance of AuthenticationException using the
explanation supplied. All other fields default to null.

**Parameters:**
- explanation

- A possibly null string containing
additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public AuthenticationException()

Constructs a new instance of AuthenticationException.
All fields are set to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AuthenticationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.AuthenticationException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.AuthenticationException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.AuthenticationException

javax.naming.NamingException

- javax.naming.NamingSecurityException
- - javax.naming.AuthenticationException

javax.naming.NamingSecurityException

- javax.naming.AuthenticationException

javax.naming.AuthenticationException

**All Implemented Interfaces:** Serializable

```java
public class
AuthenticationException

extends
NamingSecurityException
```

This exception is thrown when an authentication error occurs while
accessing the naming or directory service.
An authentication error can happen, for example, when the credentials
supplied by the user program are invalid or otherwise fail to
authenticate the user to the naming/directory service.

If the program wants to handle this exception in particular, it
should catch AuthenticationException explicitly before attempting to
catch NamingException. After catching AuthenticationException, the
program could reattempt the authentication by updating
the resolved context's environment properties with the appropriate
credentials.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

AuthenticationException

extends

NamingSecurityException

This exception is thrown when an authentication error occurs while
accessing the naming or directory service.
An authentication error can happen, for example, when the credentials
supplied by the user program are invalid or otherwise fail to
authenticate the user to the naming/directory service.

If the program wants to handle this exception in particular, it
should catch AuthenticationException explicitly before attempting to
catch NamingException. After catching AuthenticationException, the
program could reattempt the authentication by updating
the resolved context's environment properties with the appropriate
credentials.

Synchronization and serialization issues that apply to NamingException
apply directly here.

If the program wants to handle this exception in particular, it
should catch AuthenticationException explicitly before attempting to
catch NamingException. After catching AuthenticationException, the
program could reattempt the authentication by updating
the resolved context's environment properties with the appropriate
credentials.

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

AuthenticationException

()

Constructs a new instance of AuthenticationException.

AuthenticationException

​(

String

explanation)

Constructs a new instance of AuthenticationException using the
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

AuthenticationException

()

Constructs a new instance of AuthenticationException.

AuthenticationException

​(

String

explanation)

Constructs a new instance of AuthenticationException using the
explanation supplied.

---

#### Constructor Summary

Constructs a new instance of AuthenticationException.

Constructs a new instance of AuthenticationException using the
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

- AuthenticationException

```java
public AuthenticationException​(
String
explanation)
```

Constructs a new instance of AuthenticationException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

- AuthenticationException

```java
public AuthenticationException()
```

Constructs a new instance of AuthenticationException.
All fields are set to null.

Constructor Detail

- AuthenticationException

```java
public AuthenticationException​(
String
explanation)
```

Constructs a new instance of AuthenticationException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

- AuthenticationException

```java
public AuthenticationException()
```

Constructs a new instance of AuthenticationException.
All fields are set to null.

---

#### Constructor Detail

AuthenticationException

```java
public AuthenticationException​(
String
explanation)
```

Constructs a new instance of AuthenticationException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### AuthenticationException

public AuthenticationException​(

String

explanation)

Constructs a new instance of AuthenticationException using the
explanation supplied. All other fields default to null.

AuthenticationException

```java
public AuthenticationException()
```

Constructs a new instance of AuthenticationException.
All fields are set to null.

---

#### AuthenticationException

public AuthenticationException()

Constructs a new instance of AuthenticationException.
All fields are set to null.

---

