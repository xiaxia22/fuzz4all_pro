# Class LoggingPermission

**Source:** `java.logging\java\util\logging\LoggingPermission.html`

### Class Description

```java
public final class
LoggingPermission

extends
BasicPermission
```

The permission which the SecurityManager will check when code
that is running with a SecurityManager calls one of the logging
control methods (such as Logger.setLevel).

Currently there is only one named LoggingPermission. This is "control"
and it grants the ability to control the logging configuration, for
example by adding or removing Handlers, by adding or removing Filters,
or by changing logging levels.

Programmers do not normally create LoggingPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public LoggingPermission​(
String
name,

String
actions)
throws
IllegalArgumentException

Creates a new LoggingPermission object.

**Parameters:**
- name

- Permission name. Must be "control".
- actions

- Must be either null or the empty string.

**Throws:**
- NullPointerException

- if

name

is

null

.
- IllegalArgumentException

- if

name

is empty or if
arguments are invalid.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class LoggingPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.util.logging.LoggingPermission

java.security.Permission

- java.security.BasicPermission
- - java.util.logging.LoggingPermission

java.security.BasicPermission

- java.util.logging.LoggingPermission

java.util.logging.LoggingPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
LoggingPermission

extends
BasicPermission
```

The permission which the SecurityManager will check when code
that is running with a SecurityManager calls one of the logging
control methods (such as Logger.setLevel).

Currently there is only one named LoggingPermission. This is "control"
and it grants the ability to control the logging configuration, for
example by adding or removing Handlers, by adding or removing Filters,
or by changing logging levels.

Programmers do not normally create LoggingPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

**Since:** 1.4
**See Also:** BasicPermission

,

Permission

,

Permissions

,

PermissionCollection

,

SecurityManager

,

Serialized Form

public final class

LoggingPermission

extends

BasicPermission

The permission which the SecurityManager will check when code
that is running with a SecurityManager calls one of the logging
control methods (such as Logger.setLevel).

Currently there is only one named LoggingPermission. This is "control"
and it grants the ability to control the logging configuration, for
example by adding or removing Handlers, by adding or removing Filters,
or by changing logging levels.

Programmers do not normally create LoggingPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

Currently there is only one named LoggingPermission. This is "control"
and it grants the ability to control the logging configuration, for
example by adding or removing Handlers, by adding or removing Filters,
or by changing logging levels.

Programmers do not normally create LoggingPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

Programmers do not normally create LoggingPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LoggingPermission

​(

String

name,

String

actions)

Creates a new LoggingPermission object.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

LoggingPermission

​(

String

name,

String

actions)

Creates a new LoggingPermission object.

---

#### Constructor Summary

Creates a new LoggingPermission object.

Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

---

#### Methods declared in class java.security. BasicPermission

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- LoggingPermission

```java
public LoggingPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Creates a new LoggingPermission object.

**Parameters:** name

- Permission name. Must be "control".
**Parameters:** actions

- Must be either null or the empty string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or if
arguments are invalid.

Constructor Detail

- LoggingPermission

```java
public LoggingPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Creates a new LoggingPermission object.

**Parameters:** name

- Permission name. Must be "control".
**Parameters:** actions

- Must be either null or the empty string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or if
arguments are invalid.

---

#### Constructor Detail

LoggingPermission

```java
public LoggingPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Creates a new LoggingPermission object.

**Parameters:** name

- Permission name. Must be "control".
**Parameters:** actions

- Must be either null or the empty string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or if
arguments are invalid.

---

#### LoggingPermission

public LoggingPermission​(

String

name,

String

actions)
throws

IllegalArgumentException

Creates a new LoggingPermission object.

---

