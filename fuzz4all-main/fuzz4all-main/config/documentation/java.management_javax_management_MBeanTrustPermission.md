# Class MBeanTrustPermission

**Source:** `java.management\javax\management\MBeanTrustPermission.html`

### Class Description

```java
public class
MBeanTrustPermission

extends
BasicPermission
```

This permission represents "trust" in a signer or codebase.

MBeanTrustPermission contains a target name but no actions list.
A single target name, "register", is defined for this permission.
The target "*" is also allowed, permitting "register" and any future
targets that may be defined.
Only the null value or the empty string are allowed for the action
to allow the policy object to create the permissions specified in
the policy file.

If a signer, or codesource is granted this permission, then it is
considered a trusted source for MBeans. Only MBeans from trusted
sources may be registered in the MBeanServer.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanTrustPermission​(
String
name)

Create a new MBeanTrustPermission with the given name.

This constructor is equivalent to

MBeanTrustPermission(name,null)

.

**Parameters:**
- name

- the name of the permission. It must be
"register" or "*" for this permission.

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

is neither
"register" nor "*".

---

#### public MBeanTrustPermission​(
String
name,

String
actions)

Create a new MBeanTrustPermission with the given name.

**Parameters:**
- name

- the name of the permission. It must be
"register" or "*" for this permission.
- actions

- the actions for the permission. It must be
null or

""

.

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

is neither
"register" nor "*"; or if

actions

is a non-null
non-empty string.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class MBeanTrustPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - javax.management.MBeanTrustPermission

java.security.Permission

- java.security.BasicPermission
- - javax.management.MBeanTrustPermission

java.security.BasicPermission

- javax.management.MBeanTrustPermission

javax.management.MBeanTrustPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public class
MBeanTrustPermission

extends
BasicPermission
```

This permission represents "trust" in a signer or codebase.

MBeanTrustPermission contains a target name but no actions list.
A single target name, "register", is defined for this permission.
The target "*" is also allowed, permitting "register" and any future
targets that may be defined.
Only the null value or the empty string are allowed for the action
to allow the policy object to create the permissions specified in
the policy file.

If a signer, or codesource is granted this permission, then it is
considered a trusted source for MBeans. Only MBeans from trusted
sources may be registered in the MBeanServer.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanTrustPermission

extends

BasicPermission

This permission represents "trust" in a signer or codebase.

MBeanTrustPermission contains a target name but no actions list.
A single target name, "register", is defined for this permission.
The target "*" is also allowed, permitting "register" and any future
targets that may be defined.
Only the null value or the empty string are allowed for the action
to allow the policy object to create the permissions specified in
the policy file.

If a signer, or codesource is granted this permission, then it is
considered a trusted source for MBeans. Only MBeans from trusted
sources may be registered in the MBeanServer.

MBeanTrustPermission contains a target name but no actions list.
A single target name, "register", is defined for this permission.
The target "*" is also allowed, permitting "register" and any future
targets that may be defined.
Only the null value or the empty string are allowed for the action
to allow the policy object to create the permissions specified in
the policy file.

If a signer, or codesource is granted this permission, then it is
considered a trusted source for MBeans. Only MBeans from trusted
sources may be registered in the MBeanServer.

If a signer, or codesource is granted this permission, then it is
considered a trusted source for MBeans. Only MBeans from trusted
sources may be registered in the MBeanServer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanTrustPermission

​(

String

name)

Create a new MBeanTrustPermission with the given name.

MBeanTrustPermission

​(

String

name,

String

actions)

Create a new MBeanTrustPermission with the given name.

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

MBeanTrustPermission

​(

String

name)

Create a new MBeanTrustPermission with the given name.

MBeanTrustPermission

​(

String

name,

String

actions)

Create a new MBeanTrustPermission with the given name.

---

#### Constructor Summary

Create a new MBeanTrustPermission with the given name.

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

- MBeanTrustPermission

```java
public MBeanTrustPermission​(
String
name)
```

Create a new MBeanTrustPermission with the given name.

This constructor is equivalent to

MBeanTrustPermission(name,null)

.

**Parameters:** name

- the name of the permission. It must be
"register" or "*" for this permission.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is neither
"register" nor "*".

- MBeanTrustPermission

```java
public MBeanTrustPermission​(
String
name,

String
actions)
```

Create a new MBeanTrustPermission with the given name.

**Parameters:** name

- the name of the permission. It must be
"register" or "*" for this permission.
**Parameters:** actions

- the actions for the permission. It must be
null or

""

.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is neither
"register" nor "*"; or if

actions

is a non-null
non-empty string.

Constructor Detail

- MBeanTrustPermission

```java
public MBeanTrustPermission​(
String
name)
```

Create a new MBeanTrustPermission with the given name.

This constructor is equivalent to

MBeanTrustPermission(name,null)

.

**Parameters:** name

- the name of the permission. It must be
"register" or "*" for this permission.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is neither
"register" nor "*".

- MBeanTrustPermission

```java
public MBeanTrustPermission​(
String
name,

String
actions)
```

Create a new MBeanTrustPermission with the given name.

**Parameters:** name

- the name of the permission. It must be
"register" or "*" for this permission.
**Parameters:** actions

- the actions for the permission. It must be
null or

""

.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is neither
"register" nor "*"; or if

actions

is a non-null
non-empty string.

---

#### Constructor Detail

MBeanTrustPermission

```java
public MBeanTrustPermission​(
String
name)
```

Create a new MBeanTrustPermission with the given name.

This constructor is equivalent to

MBeanTrustPermission(name,null)

.

**Parameters:** name

- the name of the permission. It must be
"register" or "*" for this permission.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is neither
"register" nor "*".

---

#### MBeanTrustPermission

public MBeanTrustPermission​(

String

name)

Create a new MBeanTrustPermission with the given name.

This constructor is equivalent to

MBeanTrustPermission(name,null)

.

Create a new MBeanTrustPermission with the given name.

This constructor is equivalent to

MBeanTrustPermission(name,null)

.

MBeanTrustPermission

```java
public MBeanTrustPermission​(
String
name,

String
actions)
```

Create a new MBeanTrustPermission with the given name.

**Parameters:** name

- the name of the permission. It must be
"register" or "*" for this permission.
**Parameters:** actions

- the actions for the permission. It must be
null or

""

.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is neither
"register" nor "*"; or if

actions

is a non-null
non-empty string.

---

#### MBeanTrustPermission

public MBeanTrustPermission​(

String

name,

String

actions)

Create a new MBeanTrustPermission with the given name.

---

