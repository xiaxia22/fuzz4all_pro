# Class ManagementPermission

**Source:** `java.management\java\lang\management\ManagementPermission.html`

### Class Description

```java
public final class
ManagementPermission

extends
BasicPermission
```

The permission which the SecurityManager will check when code
that is running with a SecurityManager calls methods defined
in the management interface for the Java platform.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

control

Ability to control the runtime characteristics of the Java virtual
machine, for example, enabling and disabling the verbose output for
the class loading or memory system, setting the threshold of a memory
pool, and enabling and disabling the thread contention monitoring
support. Some actions controlled by this permission can disclose
information about the running application, like the -verbose:class
flag.

This allows an attacker to control the runtime characteristics
of the Java virtual machine and cause the system to misbehave. An
attacker can also access some information related to the running
application.

monitor

Ability to retrieve runtime information about
the Java virtual machine such as thread
stack trace, a list of all loaded class names, and input arguments
to the Java virtual machine.

This allows malicious code to monitor runtime information and
uncover vulnerabilities.

Programmers do not normally create ManagementPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public ManagementPermission​(
String
name)

Constructs a ManagementPermission with the specified name.

**Parameters:**
- name

- Permission name. Must be either "monitor" or "control".

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

is empty or invalid.

---

#### public ManagementPermission​(
String
name,

String
actions)
throws
IllegalArgumentException

Constructs a new ManagementPermission object.

**Parameters:**
- name

- Permission name. Must be either "monitor" or "control".
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

is empty or
if arguments are invalid.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ManagementPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.lang.management.ManagementPermission

java.security.Permission

- java.security.BasicPermission
- - java.lang.management.ManagementPermission

java.security.BasicPermission

- java.lang.management.ManagementPermission

java.lang.management.ManagementPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
ManagementPermission

extends
BasicPermission
```

The permission which the SecurityManager will check when code
that is running with a SecurityManager calls methods defined
in the management interface for the Java platform.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

control

Ability to control the runtime characteristics of the Java virtual
machine, for example, enabling and disabling the verbose output for
the class loading or memory system, setting the threshold of a memory
pool, and enabling and disabling the thread contention monitoring
support. Some actions controlled by this permission can disclose
information about the running application, like the -verbose:class
flag.

This allows an attacker to control the runtime characteristics
of the Java virtual machine and cause the system to misbehave. An
attacker can also access some information related to the running
application.

monitor

Ability to retrieve runtime information about
the Java virtual machine such as thread
stack trace, a list of all loaded class names, and input arguments
to the Java virtual machine.

This allows malicious code to monitor runtime information and
uncover vulnerabilities.

Programmers do not normally create ManagementPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

**Since:** 1.5
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

ManagementPermission

extends

BasicPermission

The permission which the SecurityManager will check when code
that is running with a SecurityManager calls methods defined
in the management interface for the Java platform.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

control

Ability to control the runtime characteristics of the Java virtual
machine, for example, enabling and disabling the verbose output for
the class loading or memory system, setting the threshold of a memory
pool, and enabling and disabling the thread contention monitoring
support. Some actions controlled by this permission can disclose
information about the running application, like the -verbose:class
flag.

This allows an attacker to control the runtime characteristics
of the Java virtual machine and cause the system to misbehave. An
attacker can also access some information related to the running
application.

monitor

Ability to retrieve runtime information about
the Java virtual machine such as thread
stack trace, a list of all loaded class names, and input arguments
to the Java virtual machine.

This allows malicious code to monitor runtime information and
uncover vulnerabilities.

Programmers do not normally create ManagementPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

control

Ability to control the runtime characteristics of the Java virtual
machine, for example, enabling and disabling the verbose output for
the class loading or memory system, setting the threshold of a memory
pool, and enabling and disabling the thread contention monitoring
support. Some actions controlled by this permission can disclose
information about the running application, like the -verbose:class
flag.

This allows an attacker to control the runtime characteristics
of the Java virtual machine and cause the system to misbehave. An
attacker can also access some information related to the running
application.

monitor

Ability to retrieve runtime information about
the Java virtual machine such as thread
stack trace, a list of all loaded class names, and input arguments
to the Java virtual machine.

This allows malicious code to monitor runtime information and
uncover vulnerabilities.

Programmers do not normally create ManagementPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

Programmers do not normally create ManagementPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ManagementPermission

​(

String

name)

Constructs a ManagementPermission with the specified name.

ManagementPermission

​(

String

name,

String

actions)

Constructs a new ManagementPermission object.

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

ManagementPermission

​(

String

name)

Constructs a ManagementPermission with the specified name.

ManagementPermission

​(

String

name,

String

actions)

Constructs a new ManagementPermission object.

---

#### Constructor Summary

Constructs a ManagementPermission with the specified name.

Constructs a new ManagementPermission object.

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

- ManagementPermission

```java
public ManagementPermission​(
String
name)
```

Constructs a ManagementPermission with the specified name.

**Parameters:** name

- Permission name. Must be either "monitor" or "control".
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or invalid.

- ManagementPermission

```java
public ManagementPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Constructs a new ManagementPermission object.

**Parameters:** name

- Permission name. Must be either "monitor" or "control".
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

is empty or
if arguments are invalid.

Constructor Detail

- ManagementPermission

```java
public ManagementPermission​(
String
name)
```

Constructs a ManagementPermission with the specified name.

**Parameters:** name

- Permission name. Must be either "monitor" or "control".
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or invalid.

- ManagementPermission

```java
public ManagementPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Constructs a new ManagementPermission object.

**Parameters:** name

- Permission name. Must be either "monitor" or "control".
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

is empty or
if arguments are invalid.

---

#### Constructor Detail

ManagementPermission

```java
public ManagementPermission​(
String
name)
```

Constructs a ManagementPermission with the specified name.

**Parameters:** name

- Permission name. Must be either "monitor" or "control".
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or invalid.

---

#### ManagementPermission

public ManagementPermission​(

String

name)

Constructs a ManagementPermission with the specified name.

ManagementPermission

```java
public ManagementPermission​(
String
name,

String
actions)
throws
IllegalArgumentException
```

Constructs a new ManagementPermission object.

**Parameters:** name

- Permission name. Must be either "monitor" or "control".
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

is empty or
if arguments are invalid.

---

#### ManagementPermission

public ManagementPermission​(

String

name,

String

actions)
throws

IllegalArgumentException

Constructs a new ManagementPermission object.

---

