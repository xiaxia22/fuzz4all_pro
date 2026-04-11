# Class AccountExpiredException

**Source:** `java.base\javax\security\auth\login\AccountExpiredException.html`

### Class Description

```java
public class
AccountExpiredException

extends
AccountException
```

Signals that a user account has expired.

This exception is thrown by LoginModules when they determine
that an account has expired. For example, a

LoginModule

,
after successfully authenticating a user, may determine that the
user's account has expired. In this case the

LoginModule

throws this exception to notify the application. The application can
then take the appropriate steps to notify the user.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AccountExpiredException()

Constructs a AccountExpiredException with no detail message. A detail
message is a String that describes this particular exception.

---

#### public AccountExpiredException​(
String
msg)

Constructs a AccountExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:**
- msg

- the detail message.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AccountExpiredException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - javax.security.auth.login.LoginException
- - javax.security.auth.login.AccountException
- - javax.security.auth.login.AccountExpiredException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - javax.security.auth.login.LoginException
- - javax.security.auth.login.AccountException
- - javax.security.auth.login.AccountExpiredException

java.lang.Exception

- java.security.GeneralSecurityException
- - javax.security.auth.login.LoginException
- - javax.security.auth.login.AccountException
- - javax.security.auth.login.AccountExpiredException

java.security.GeneralSecurityException

- javax.security.auth.login.LoginException
- - javax.security.auth.login.AccountException
- - javax.security.auth.login.AccountExpiredException

javax.security.auth.login.LoginException

- javax.security.auth.login.AccountException
- - javax.security.auth.login.AccountExpiredException

javax.security.auth.login.AccountException

- javax.security.auth.login.AccountExpiredException

javax.security.auth.login.AccountExpiredException

**All Implemented Interfaces:** Serializable

```java
public class
AccountExpiredException

extends
AccountException
```

Signals that a user account has expired.

This exception is thrown by LoginModules when they determine
that an account has expired. For example, a

LoginModule

,
after successfully authenticating a user, may determine that the
user's account has expired. In this case the

LoginModule

throws this exception to notify the application. The application can
then take the appropriate steps to notify the user.

**Since:** 1.4
**See Also:** Serialized Form

public class

AccountExpiredException

extends

AccountException

Signals that a user account has expired.

This exception is thrown by LoginModules when they determine
that an account has expired. For example, a

LoginModule

,
after successfully authenticating a user, may determine that the
user's account has expired. In this case the

LoginModule

throws this exception to notify the application. The application can
then take the appropriate steps to notify the user.

This exception is thrown by LoginModules when they determine
that an account has expired. For example, a

LoginModule

,
after successfully authenticating a user, may determine that the
user's account has expired. In this case the

LoginModule

throws this exception to notify the application. The application can
then take the appropriate steps to notify the user.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccountExpiredException

()

Constructs a AccountExpiredException with no detail message.

AccountExpiredException

​(

String

msg)

Constructs a AccountExpiredException with the specified detail
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

AccountExpiredException

()

Constructs a AccountExpiredException with no detail message.

AccountExpiredException

​(

String

msg)

Constructs a AccountExpiredException with the specified detail
message.

---

#### Constructor Summary

Constructs a AccountExpiredException with no detail message.

Constructs a AccountExpiredException with the specified detail
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

- AccountExpiredException

```java
public AccountExpiredException()
```

Constructs a AccountExpiredException with no detail message. A detail
message is a String that describes this particular exception.

- AccountExpiredException

```java
public AccountExpiredException​(
String
msg)
```

Constructs a AccountExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

Constructor Detail

- AccountExpiredException

```java
public AccountExpiredException()
```

Constructs a AccountExpiredException with no detail message. A detail
message is a String that describes this particular exception.

- AccountExpiredException

```java
public AccountExpiredException​(
String
msg)
```

Constructs a AccountExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

---

#### Constructor Detail

AccountExpiredException

```java
public AccountExpiredException()
```

Constructs a AccountExpiredException with no detail message. A detail
message is a String that describes this particular exception.

---

#### AccountExpiredException

public AccountExpiredException()

Constructs a AccountExpiredException with no detail message. A detail
message is a String that describes this particular exception.

AccountExpiredException

```java
public AccountExpiredException​(
String
msg)
```

Constructs a AccountExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** msg

- the detail message.

---

#### AccountExpiredException

public AccountExpiredException​(

String

msg)

Constructs a AccountExpiredException with the specified detail
message. A detail message is a String that describes this particular
exception.

---

