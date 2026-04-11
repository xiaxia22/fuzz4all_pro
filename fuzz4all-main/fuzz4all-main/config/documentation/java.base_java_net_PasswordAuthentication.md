# Class PasswordAuthentication

**Source:** `java.base\java\net\PasswordAuthentication.html`

### Class Description

```java
public final class
PasswordAuthentication

extends
Object
```

The class PasswordAuthentication is a data holder that is used by
Authenticator. It is simply a repository for a user name and a password.

**Since:** 1.2
**See Also:** Authenticator

,

Authenticator.getPasswordAuthentication()

---

### Field Details

*No entries found.*

### Constructor Details

#### public PasswordAuthentication​(
String
userName,
char[] password)

Creates a new

PasswordAuthentication

object from the given
user name and password.

Note that the given user password is cloned before it is stored in
the new

PasswordAuthentication

object.

**Parameters:**
- userName

- the user name
- password

- the user's password

---

### Method Details

#### public
String
getUserName()

Returns the user name.

**Returns:**
- the user name

---

#### public char[] getPassword()

Returns the user password.

Note that this method returns a reference to the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:**
- the password

---

### Additional Sections

#### Class PasswordAuthentication

java.lang.Object

- java.net.PasswordAuthentication

java.net.PasswordAuthentication

```java
public final class
PasswordAuthentication

extends
Object
```

The class PasswordAuthentication is a data holder that is used by
Authenticator. It is simply a repository for a user name and a password.

**Since:** 1.2
**See Also:** Authenticator

,

Authenticator.getPasswordAuthentication()

public final class

PasswordAuthentication

extends

Object

The class PasswordAuthentication is a data holder that is used by
Authenticator. It is simply a repository for a user name and a password.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PasswordAuthentication

​(

String

userName,
char[] password)

Creates a new

PasswordAuthentication

object from the given
user name and password.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char[]

getPassword

()

Returns the user password.

String

getUserName

()

Returns the user name.

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

toString

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

PasswordAuthentication

​(

String

userName,
char[] password)

Creates a new

PasswordAuthentication

object from the given
user name and password.

---

#### Constructor Summary

Creates a new

PasswordAuthentication

object from the given
user name and password.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char[]

getPassword

()

Returns the user password.

String

getUserName

()

Returns the user name.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the user password.

Returns the user name.

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

toString

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

- PasswordAuthentication

```java
public PasswordAuthentication​(
String
userName,
char[] password)
```

Creates a new

PasswordAuthentication

object from the given
user name and password.

Note that the given user password is cloned before it is stored in
the new

PasswordAuthentication

object.

**Parameters:** userName

- the user name
**Parameters:** password

- the user's password

============ METHOD DETAIL ==========

- Method Detail

- getUserName

```java
public
String
getUserName()
```

Returns the user name.

**Returns:** the user name

- getPassword

```java
public char[] getPassword()
```

Returns the user password.

Note that this method returns a reference to the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password

Constructor Detail

- PasswordAuthentication

```java
public PasswordAuthentication​(
String
userName,
char[] password)
```

Creates a new

PasswordAuthentication

object from the given
user name and password.

Note that the given user password is cloned before it is stored in
the new

PasswordAuthentication

object.

**Parameters:** userName

- the user name
**Parameters:** password

- the user's password

---

#### Constructor Detail

PasswordAuthentication

```java
public PasswordAuthentication​(
String
userName,
char[] password)
```

Creates a new

PasswordAuthentication

object from the given
user name and password.

Note that the given user password is cloned before it is stored in
the new

PasswordAuthentication

object.

**Parameters:** userName

- the user name
**Parameters:** password

- the user's password

---

#### PasswordAuthentication

public PasswordAuthentication​(

String

userName,
char[] password)

Creates a new

PasswordAuthentication

object from the given
user name and password.

Note that the given user password is cloned before it is stored in
the new

PasswordAuthentication

object.

Note that the given user password is cloned before it is stored in
the new

PasswordAuthentication

object.

Method Detail

- getUserName

```java
public
String
getUserName()
```

Returns the user name.

**Returns:** the user name

- getPassword

```java
public char[] getPassword()
```

Returns the user password.

Note that this method returns a reference to the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password

---

#### Method Detail

getUserName

```java
public
String
getUserName()
```

Returns the user name.

**Returns:** the user name

---

#### getUserName

public

String

getUserName()

Returns the user name.

getPassword

```java
public char[] getPassword()
```

Returns the user password.

Note that this method returns a reference to the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password

---

#### getPassword

public char[] getPassword()

Returns the user password.

Note that this method returns a reference to the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

Note that this method returns a reference to the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

---

