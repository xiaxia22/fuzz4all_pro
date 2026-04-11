# Class UserPrincipalNotFoundException

**Source:** `java.base\java\nio\file\attribute\UserPrincipalNotFoundException.html`

### Class Description

```java
public class
UserPrincipalNotFoundException

extends
IOException
```

Checked exception thrown when a lookup of

UserPrincipal

fails because
the principal does not exist.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UserPrincipalNotFoundException​(
String
name)

Constructs an instance of this class.

**Parameters:**
- name

- the principal name; may be

null

---

### Method Details

#### public
String
getName()

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

**Returns:**
- the user principal name or

null

---

### Additional Sections

#### Class UserPrincipalNotFoundException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.file.attribute.UserPrincipalNotFoundException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.file.attribute.UserPrincipalNotFoundException

java.lang.Exception

- java.io.IOException
- - java.nio.file.attribute.UserPrincipalNotFoundException

java.io.IOException

- java.nio.file.attribute.UserPrincipalNotFoundException

java.nio.file.attribute.UserPrincipalNotFoundException

**All Implemented Interfaces:** Serializable

```java
public class
UserPrincipalNotFoundException

extends
IOException
```

Checked exception thrown when a lookup of

UserPrincipal

fails because
the principal does not exist.

**Since:** 1.7
**See Also:** Serialized Form

public class

UserPrincipalNotFoundException

extends

IOException

Checked exception thrown when a lookup of

UserPrincipal

fails because
the principal does not exist.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UserPrincipalNotFoundException

​(

String

name)

Constructs an instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

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

UserPrincipalNotFoundException

​(

String

name)

Constructs an instance of this class.

---

#### Constructor Summary

Constructs an instance of this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

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

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

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

- UserPrincipalNotFoundException

```java
public UserPrincipalNotFoundException​(
String
name)
```

Constructs an instance of this class.

**Parameters:** name

- the principal name; may be

null

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

**Returns:** the user principal name or

null

Constructor Detail

- UserPrincipalNotFoundException

```java
public UserPrincipalNotFoundException​(
String
name)
```

Constructs an instance of this class.

**Parameters:** name

- the principal name; may be

null

---

#### Constructor Detail

UserPrincipalNotFoundException

```java
public UserPrincipalNotFoundException​(
String
name)
```

Constructs an instance of this class.

**Parameters:** name

- the principal name; may be

null

---

#### UserPrincipalNotFoundException

public UserPrincipalNotFoundException​(

String

name)

Constructs an instance of this class.

Method Detail

- getName

```java
public
String
getName()
```

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

**Returns:** the user principal name or

null

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

**Returns:** the user principal name or

null

---

#### getName

public

String

getName()

Returns the user principal name if this exception was created with the
user principal name that was not found, otherwise

null

.

---

