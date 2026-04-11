# Class CredentialExpiredException

**Source:** `java.base\javax\security\auth\login\CredentialExpiredException.html`

### Class Description

```java
public class
CredentialExpiredException

extends
CredentialException
```

Signals that a

Credential

has expired.

This exception is thrown by LoginModules when they determine
that a

Credential

has expired.
For example, a

LoginModule

authenticating a user
in its

login

method may determine that the user's
password, although entered correctly, has expired. In this case
the

LoginModule

throws this exception to notify
the application. The application can then take the appropriate
steps to assist the user in updating the password.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CredentialExpiredException()

Constructs a CredentialExpiredException with no detail message. A detail
message is a String that describes this particular exception.

---

#### public CredentialExpiredException​(
String
msg)

Constructs a CredentialExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:**
- msg

- the detail message.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class CredentialExpiredException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - javax.security.auth.login.LoginException
- - javax.security.auth.login.CredentialException
- - javax.security.auth.login.CredentialExpiredException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - javax.security.auth.login.LoginException
- - javax.security.auth.login.CredentialException
- - javax.security.auth.login.CredentialExpiredException

java.lang.Exception

- java.security.GeneralSecurityException
- - javax.security.auth.login.LoginException
- - javax.security.auth.login.CredentialException
- - javax.security.auth.login.CredentialExpiredException

java.security.GeneralSecurityException

- javax.security.auth.login.LoginException
- - javax.security.auth.login.CredentialException
- - javax.security.auth.login.CredentialExpiredException

javax.security.auth.login.LoginException

- javax.security.auth.login.CredentialException
- - javax.security.auth.login.CredentialExpiredException

javax.security.auth.login.CredentialException

- javax.security.auth.login.CredentialExpiredException

javax.security.auth.login.CredentialExpiredException

**All Implemented Interfaces:** Serializable

```java
public class
CredentialExpiredException

extends
CredentialException
```

Signals that a

Credential

has expired.

This exception is thrown by LoginModules when they determine
that a

Credential

has expired.
For example, a

LoginModule

authenticating a user
in its

login

method may determine that the user's
password, although entered correctly, has expired. In this case
the

LoginModule

throws this exception to notify
the application. The application can then take the appropriate
steps to assist the user in updating the password.

**Since:** 1.4
**See Also:** Serialized Form

public class

CredentialExpiredException

extends

CredentialException

Signals that a

Credential

has expired.

This exception is thrown by LoginModules when they determine
that a

Credential

has expired.
For example, a

LoginModule

authenticating a user
in its

login

method may determine that the user's
password, although entered correctly, has expired. In this case
the

LoginModule

throws this exception to notify
the application. The application can then take the appropriate
steps to assist the user in updating the password.

This exception is thrown by LoginModules when they determine
that a

Credential

has expired.
For example, a

LoginModule

authenticating a user
in its

login

method may determine that the user's
password, although entered correctly, has expired. In this case
the

LoginModule

throws this exception to notify
the application. The application can then take the appropriate
steps to assist the user in updating the password.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CredentialExpiredException

()

Constructs a CredentialExpiredException with no detail message.

CredentialExpiredException

​(

String

msg)

Constructs a CredentialExpiredException with the specified detail
message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Constructor Summary

Constructors

Constructor

Description

CredentialExpiredException

()

Constructs a CredentialExpiredException with no detail message.

CredentialExpiredException

​(

String

msg)

Constructs a CredentialExpiredException with the specified detail
message.

---

#### Constructor Summary

Constructs a CredentialExpiredException with no detail message.

Constructs a CredentialExpiredException with the specified detail
message.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

- CredentialExpiredException

```java
public CredentialExpiredException()
```

Constructs a CredentialExpiredException with no detail message. A detail
message is a String that describes this particular exception.

- CredentialExpiredException

```java
public CredentialExpiredException​(
String
msg)
```

Constructs a CredentialExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

Constructor Detail

- CredentialExpiredException

```java
public CredentialExpiredException()
```

Constructs a CredentialExpiredException with no detail message. A detail
message is a String that describes this particular exception.

- CredentialExpiredException

```java
public CredentialExpiredException​(
String
msg)
```

Constructs a CredentialExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

---

#### Constructor Detail

CredentialExpiredException

```java
public CredentialExpiredException()
```

Constructs a CredentialExpiredException with no detail message. A detail
message is a String that describes this particular exception.

---

#### CredentialExpiredException

public CredentialExpiredException()

Constructs a CredentialExpiredException with no detail message. A detail
message is a String that describes this particular exception.

CredentialExpiredException

```java
public CredentialExpiredException​(
String
msg)
```

Constructs a CredentialExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

---

#### CredentialExpiredException

public CredentialExpiredException​(

String

msg)

Constructs a CredentialExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

---

