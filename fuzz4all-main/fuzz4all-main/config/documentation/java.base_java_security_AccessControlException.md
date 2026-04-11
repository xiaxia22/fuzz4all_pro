# Class AccessControlException

**Source:** `java.base\java\security\AccessControlException.html`

### Class Description

```java
public class
AccessControlException

extends
SecurityException
```

This exception is thrown by the AccessController to indicate
that a requested access (to a critical system resource such as the
file system or the network) is denied.

The reason to deny access can vary. For example, the requested
permission might be of an incorrect type, contain an invalid
value, or request access that is not allowed according to the
security policy. Such information should be given whenever
possible at the time the exception is thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AccessControlException​(
String
s)

Constructs an

AccessControlException

with the
specified, detailed message.

**Parameters:**
- s

- the detail message.

---

#### public AccessControlException​(
String
s,

Permission
p)

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

**Parameters:**
- s

- the detail message.
- p

- the permission that caused the exception.

---

### Method Details

#### public
Permission
getPermission()

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

**Returns:**
- the Permission object.

---

### Additional Sections

#### Class AccessControlException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.SecurityException
- - java.security.AccessControlException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.SecurityException
- - java.security.AccessControlException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.SecurityException
- - java.security.AccessControlException

java.lang.RuntimeException

- java.lang.SecurityException
- - java.security.AccessControlException

java.lang.SecurityException

- java.security.AccessControlException

java.security.AccessControlException

**All Implemented Interfaces:** Serializable

```java
public class
AccessControlException

extends
SecurityException
```

This exception is thrown by the AccessController to indicate
that a requested access (to a critical system resource such as the
file system or the network) is denied.

The reason to deny access can vary. For example, the requested
permission might be of an incorrect type, contain an invalid
value, or request access that is not allowed according to the
security policy. Such information should be given whenever
possible at the time the exception is thrown.

**Since:** 1.2
**See Also:** Serialized Form

public class

AccessControlException

extends

SecurityException

This exception is thrown by the AccessController to indicate
that a requested access (to a critical system resource such as the
file system or the network) is denied.

The reason to deny access can vary. For example, the requested
permission might be of an incorrect type, contain an invalid
value, or request access that is not allowed according to the
security policy. Such information should be given whenever
possible at the time the exception is thrown.

The reason to deny access can vary. For example, the requested
permission might be of an incorrect type, contain an invalid
value, or request access that is not allowed according to the
security policy. Such information should be given whenever
possible at the time the exception is thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessControlException

​(

String

s)

Constructs an

AccessControlException

with the
specified, detailed message.

AccessControlException

​(

String

s,

Permission

p)

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Permission

getPermission

()

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

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

AccessControlException

​(

String

s)

Constructs an

AccessControlException

with the
specified, detailed message.

AccessControlException

​(

String

s,

Permission

p)

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

---

#### Constructor Summary

Constructs an

AccessControlException

with the
specified, detailed message.

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Permission

getPermission

()

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

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

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

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

- AccessControlException

```java
public AccessControlException​(
String
s)
```

Constructs an

AccessControlException

with the
specified, detailed message.

**Parameters:** s

- the detail message.

- AccessControlException

```java
public AccessControlException​(
String
s,

Permission
p)
```

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

**Parameters:** s

- the detail message.
**Parameters:** p

- the permission that caused the exception.

============ METHOD DETAIL ==========

- Method Detail

- getPermission

```java
public
Permission
getPermission()
```

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

**Returns:** the Permission object.

Constructor Detail

- AccessControlException

```java
public AccessControlException​(
String
s)
```

Constructs an

AccessControlException

with the
specified, detailed message.

**Parameters:** s

- the detail message.

- AccessControlException

```java
public AccessControlException​(
String
s,

Permission
p)
```

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

**Parameters:** s

- the detail message.
**Parameters:** p

- the permission that caused the exception.

---

#### Constructor Detail

AccessControlException

```java
public AccessControlException​(
String
s)
```

Constructs an

AccessControlException

with the
specified, detailed message.

**Parameters:** s

- the detail message.

---

#### AccessControlException

public AccessControlException​(

String

s)

Constructs an

AccessControlException

with the
specified, detailed message.

AccessControlException

```java
public AccessControlException​(
String
s,

Permission
p)
```

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

**Parameters:** s

- the detail message.
**Parameters:** p

- the permission that caused the exception.

---

#### AccessControlException

public AccessControlException​(

String

s,

Permission

p)

Constructs an

AccessControlException

with the
specified, detailed message, and the requested permission that caused
the exception.

Method Detail

- getPermission

```java
public
Permission
getPermission()
```

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

**Returns:** the Permission object.

---

#### Method Detail

getPermission

```java
public
Permission
getPermission()
```

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

**Returns:** the Permission object.

---

#### getPermission

public

Permission

getPermission()

Gets the Permission object associated with this exception, or
null if there was no corresponding Permission object.

---

