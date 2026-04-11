# Class InquireSecContextPermission

**Source:** `jdk.security.jgss\com\sun\security\jgss\InquireSecContextPermission.html`

### Class Description

```java
public final class
InquireSecContextPermission

extends
BasicPermission
```

This class is used to protect various attributes of an established
GSS security context that can be accessed using the

ExtendedGSSContext.inquireSecContext(com.sun.security.jgss.InquireType)

method.

The target name is the

InquireType

allowed.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public InquireSecContextPermission​(
String
name)

Constructs a new

InquireSecContextPermission

object with
the specified name. The name is the symbolic name of the

InquireType

allowed.

**Parameters:**
- name

- the

InquireType

allowed by this
permission. "*" means all

InquireType

s are allowed.

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

is empty.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InquireSecContextPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - com.sun.security.jgss.InquireSecContextPermission

java.security.Permission

- java.security.BasicPermission
- - com.sun.security.jgss.InquireSecContextPermission

java.security.BasicPermission

- com.sun.security.jgss.InquireSecContextPermission

com.sun.security.jgss.InquireSecContextPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
InquireSecContextPermission

extends
BasicPermission
```

This class is used to protect various attributes of an established
GSS security context that can be accessed using the

ExtendedGSSContext.inquireSecContext(com.sun.security.jgss.InquireType)

method.

The target name is the

InquireType

allowed.

**See Also:** Serialized Form

public final class

InquireSecContextPermission

extends

BasicPermission

This class is used to protect various attributes of an established
GSS security context that can be accessed using the

ExtendedGSSContext.inquireSecContext(com.sun.security.jgss.InquireType)

method.

The target name is the

InquireType

allowed.

The target name is the

InquireType

allowed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InquireSecContextPermission

​(

String

name)

Constructs a new

InquireSecContextPermission

object with
the specified name.

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

InquireSecContextPermission

​(

String

name)

Constructs a new

InquireSecContextPermission

object with
the specified name.

---

#### Constructor Summary

Constructs a new

InquireSecContextPermission

object with
the specified name.

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

- InquireSecContextPermission

```java
public InquireSecContextPermission​(
String
name)
```

Constructs a new

InquireSecContextPermission

object with
the specified name. The name is the symbolic name of the

InquireType

allowed.

**Parameters:** name

- the

InquireType

allowed by this
permission. "*" means all

InquireType

s are allowed.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

Constructor Detail

- InquireSecContextPermission

```java
public InquireSecContextPermission​(
String
name)
```

Constructs a new

InquireSecContextPermission

object with
the specified name. The name is the symbolic name of the

InquireType

allowed.

**Parameters:** name

- the

InquireType

allowed by this
permission. "*" means all

InquireType

s are allowed.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### Constructor Detail

InquireSecContextPermission

```java
public InquireSecContextPermission​(
String
name)
```

Constructs a new

InquireSecContextPermission

object with
the specified name. The name is the symbolic name of the

InquireType

allowed.

**Parameters:** name

- the

InquireType

allowed by this
permission. "*" means all

InquireType

s are allowed.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### InquireSecContextPermission

public InquireSecContextPermission​(

String

name)

Constructs a new

InquireSecContextPermission

object with
the specified name. The name is the symbolic name of the

InquireType

allowed.

---

