# Class JDIPermission

**Source:** `jdk.jdi\com\sun\jdi\JDIPermission.html`

### Class Description

```java
public final class
JDIPermission

extends
BasicPermission
```

The

JDIPermission

class represents access rights to
the

VirtualMachineManager

. This is the permission
which the SecurityManager will check when code that is running with
a SecurityManager requests access to the VirtualMachineManager, as
defined in the Java Debug Interface (JDI) for the Java platform.

A

JDIPermission

object contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The following table provides a summary description of what the
permission allows, and discusses the risks of granting code the
permission.

Table shows permission target name, what the
permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

virtualMachineManager

Ability to inspect and modify the JDI objects in the

VirtualMachineManager

This allows an attacker to control the

VirtualMachineManager

and cause the system to
misbehave.

Programmers do not normally create JDIPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public JDIPermission​(
String
name)

The

JDIPermission

class represents access rights to the

VirtualMachineManager

**Parameters:**
- name

- Permission name. Must be "virtualMachineManager".

**Throws:**
- IllegalArgumentException

- if the name argument is invalid.

---

#### public JDIPermission​(
String
name,

String
actions)
throws
IllegalArgumentException

Constructs a new JDIPermission object.

**Parameters:**
- name

- Permission name. Must be "virtualMachineManager".
- actions

- Must be either null or the empty string.

**Throws:**
- IllegalArgumentException

- if arguments are invalid.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class JDIPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - com.sun.jdi.JDIPermission

java.security.Permission

- java.security.BasicPermission
- - com.sun.jdi.JDIPermission

java.security.BasicPermission

- com.sun.jdi.JDIPermission

com.sun.jdi.JDIPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
JDIPermission

extends
BasicPermission
```

The

JDIPermission

class represents access rights to
the

VirtualMachineManager

. This is the permission
which the SecurityManager will check when code that is running with
a SecurityManager requests access to the VirtualMachineManager, as
defined in the Java Debug Interface (JDI) for the Java platform.

A

JDIPermission

object contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The following table provides a summary description of what the
permission allows, and discusses the risks of granting code the
permission.

Table shows permission target name, what the
permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

virtualMachineManager

Ability to inspect and modify the JDI objects in the

VirtualMachineManager

This allows an attacker to control the

VirtualMachineManager

and cause the system to
misbehave.

Programmers do not normally create JDIPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

**Since:** 1.5
**See Also:** Bootstrap

,

BasicPermission

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

JDIPermission

extends

BasicPermission

The

JDIPermission

class represents access rights to
the

VirtualMachineManager

. This is the permission
which the SecurityManager will check when code that is running with
a SecurityManager requests access to the VirtualMachineManager, as
defined in the Java Debug Interface (JDI) for the Java platform.

A

JDIPermission

object contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The following table provides a summary description of what the
permission allows, and discusses the risks of granting code the
permission.

Table shows permission target name, what the
permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

virtualMachineManager

Ability to inspect and modify the JDI objects in the

VirtualMachineManager

This allows an attacker to control the

VirtualMachineManager

and cause the system to
misbehave.

Programmers do not normally create JDIPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

A

JDIPermission

object contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The following table provides a summary description of what the
permission allows, and discusses the risks of granting code the
permission.

Table shows permission target name, what the
permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

virtualMachineManager

Ability to inspect and modify the JDI objects in the

VirtualMachineManager

This allows an attacker to control the

VirtualMachineManager

and cause the system to
misbehave.

Programmers do not normally create JDIPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

The following table provides a summary description of what the
permission allows, and discusses the risks of granting code the
permission.

Table shows permission target name, what the
permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

virtualMachineManager

Ability to inspect and modify the JDI objects in the

VirtualMachineManager

This allows an attacker to control the

VirtualMachineManager

and cause the system to
misbehave.

Programmers do not normally create JDIPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

Programmers do not normally create JDIPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JDIPermission

​(

String

name)

The

JDIPermission

class represents access rights to the

VirtualMachineManager

JDIPermission

​(

String

name,

String

actions)

Constructs a new JDIPermission object.

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

JDIPermission

​(

String

name)

The

JDIPermission

class represents access rights to the

VirtualMachineManager

JDIPermission

​(

String

name,

String

actions)

Constructs a new JDIPermission object.

---

#### Constructor Summary

The

JDIPermission

class represents access rights to the

VirtualMachineManager

Constructs a new JDIPermission object.

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

- JDIPermission

```java
public JDIPermission​(
String
name)
```

The

JDIPermission

class represents access rights to the

VirtualMachineManager

**Parameters:** name

- Permission name. Must be "virtualMachineManager".
**Throws:** IllegalArgumentException

- if the name argument is invalid.

- JDIPermission

```java
public JDIPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Constructs a new JDIPermission object.

**Parameters:** name

- Permission name. Must be "virtualMachineManager".
**Parameters:** actions

- Must be either null or the empty string.
**Throws:** IllegalArgumentException

- if arguments are invalid.

Constructor Detail

- JDIPermission

```java
public JDIPermission​(
String
name)
```

The

JDIPermission

class represents access rights to the

VirtualMachineManager

**Parameters:** name

- Permission name. Must be "virtualMachineManager".
**Throws:** IllegalArgumentException

- if the name argument is invalid.

- JDIPermission

```java
public JDIPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Constructs a new JDIPermission object.

**Parameters:** name

- Permission name. Must be "virtualMachineManager".
**Parameters:** actions

- Must be either null or the empty string.
**Throws:** IllegalArgumentException

- if arguments are invalid.

---

#### Constructor Detail

JDIPermission

```java
public JDIPermission​(
String
name)
```

The

JDIPermission

class represents access rights to the

VirtualMachineManager

**Parameters:** name

- Permission name. Must be "virtualMachineManager".
**Throws:** IllegalArgumentException

- if the name argument is invalid.

---

#### JDIPermission

public JDIPermission​(

String

name)

The

JDIPermission

class represents access rights to the

VirtualMachineManager

JDIPermission

```java
public JDIPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Constructs a new JDIPermission object.

**Parameters:** name

- Permission name. Must be "virtualMachineManager".
**Parameters:** actions

- Must be either null or the empty string.
**Throws:** IllegalArgumentException

- if arguments are invalid.

---

#### JDIPermission

public JDIPermission​(

String

name,

String

actions)
throws

IllegalArgumentException

Constructs a new JDIPermission object.

---

