# Class AuthenticationNotSupportedException

**Source:** `java.naming\javax\naming\AuthenticationNotSupportedException.html`

### Class Description

```java
public class
AuthenticationNotSupportedException

extends
NamingSecurityException
```

This exception is thrown when
the particular flavor of authentication requested is not supported.
For example, if the program
is attempting to use strong authentication but the directory/naming
supports only simple authentication, this exception would be thrown.
Identification of a particular flavor of authentication is
provider- and server-specific. It may be specified using
specific authentication schemes such
those identified using SASL, or a generic authentication specifier
(such as "simple" and "strong").

If the program wants to handle this exception in particular, it
should catch AuthenticationNotSupportedException explicitly before
attempting to catch NamingException. After catching

AuthenticationNotSupportedException

, the program could
reattempt the authentication using a different authentication flavor
by updating the resolved context's environment properties accordingly.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AuthenticationNotSupportedException​(
String
explanation)

Constructs a new instance of AuthenticationNotSupportedException using
an explanation. All other fields default to null.

**Parameters:**
- explanation

- A possibly null string containing additional
detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public AuthenticationNotSupportedException()

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AuthenticationNotSupportedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.AuthenticationNotSupportedException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.AuthenticationNotSupportedException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NamingSecurityException
- - javax.naming.AuthenticationNotSupportedException

javax.naming.NamingException

- javax.naming.NamingSecurityException
- - javax.naming.AuthenticationNotSupportedException

javax.naming.NamingSecurityException

- javax.naming.AuthenticationNotSupportedException

javax.naming.AuthenticationNotSupportedException

**All Implemented Interfaces:** Serializable

```java
public class
AuthenticationNotSupportedException

extends
NamingSecurityException
```

This exception is thrown when
the particular flavor of authentication requested is not supported.
For example, if the program
is attempting to use strong authentication but the directory/naming
supports only simple authentication, this exception would be thrown.
Identification of a particular flavor of authentication is
provider- and server-specific. It may be specified using
specific authentication schemes such
those identified using SASL, or a generic authentication specifier
(such as "simple" and "strong").

If the program wants to handle this exception in particular, it
should catch AuthenticationNotSupportedException explicitly before
attempting to catch NamingException. After catching

AuthenticationNotSupportedException

, the program could
reattempt the authentication using a different authentication flavor
by updating the resolved context's environment properties accordingly.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

AuthenticationNotSupportedException

extends

NamingSecurityException

This exception is thrown when
the particular flavor of authentication requested is not supported.
For example, if the program
is attempting to use strong authentication but the directory/naming
supports only simple authentication, this exception would be thrown.
Identification of a particular flavor of authentication is
provider- and server-specific. It may be specified using
specific authentication schemes such
those identified using SASL, or a generic authentication specifier
(such as "simple" and "strong").

If the program wants to handle this exception in particular, it
should catch AuthenticationNotSupportedException explicitly before
attempting to catch NamingException. After catching

AuthenticationNotSupportedException

, the program could
reattempt the authentication using a different authentication flavor
by updating the resolved context's environment properties accordingly.

Synchronization and serialization issues that apply to NamingException
apply directly here.

If the program wants to handle this exception in particular, it
should catch AuthenticationNotSupportedException explicitly before
attempting to catch NamingException. After catching

AuthenticationNotSupportedException

, the program could
reattempt the authentication using a different authentication flavor
by updating the resolved context's environment properties accordingly.

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

AuthenticationNotSupportedException

()

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

AuthenticationNotSupportedException

​(

String

explanation)

Constructs a new instance of AuthenticationNotSupportedException using
an explanation.

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

AuthenticationNotSupportedException

()

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

AuthenticationNotSupportedException

​(

String

explanation)

Constructs a new instance of AuthenticationNotSupportedException using
an explanation.

---

#### Constructor Summary

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

Constructs a new instance of AuthenticationNotSupportedException using
an explanation.

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

- AuthenticationNotSupportedException

```java
public AuthenticationNotSupportedException​(
String
explanation)
```

Constructs a new instance of AuthenticationNotSupportedException using
an explanation. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

- AuthenticationNotSupportedException

```java
public AuthenticationNotSupportedException()
```

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

Constructor Detail

- AuthenticationNotSupportedException

```java
public AuthenticationNotSupportedException​(
String
explanation)
```

Constructs a new instance of AuthenticationNotSupportedException using
an explanation. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

- AuthenticationNotSupportedException

```java
public AuthenticationNotSupportedException()
```

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

---

#### Constructor Detail

AuthenticationNotSupportedException

```java
public AuthenticationNotSupportedException​(
String
explanation)
```

Constructs a new instance of AuthenticationNotSupportedException using
an explanation. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

---

#### AuthenticationNotSupportedException

public AuthenticationNotSupportedException​(

String

explanation)

Constructs a new instance of AuthenticationNotSupportedException using
an explanation. All other fields default to null.

AuthenticationNotSupportedException

```java
public AuthenticationNotSupportedException()
```

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

---

#### AuthenticationNotSupportedException

public AuthenticationNotSupportedException()

Constructs a new instance of AuthenticationNotSupportedException
with all name resolution fields and explanation initialized to null.

---

