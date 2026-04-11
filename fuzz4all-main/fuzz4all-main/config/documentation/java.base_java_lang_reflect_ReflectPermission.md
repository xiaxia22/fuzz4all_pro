# Class ReflectPermission

**Source:** `java.base\java\lang\reflect\ReflectPermission.html`

### Class Description

```java
public final class
ReflectPermission

extends
BasicPermission
```

The Permission class for reflective operations.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

suppressAccessChecks

ability to suppress the standard Java language access checks
on fields and methods in a class; allow access not only public members
but also allow access to default (package) access, protected,
and private members.

This is dangerous in that information (possibly confidential) and
methods normally unavailable would be accessible to malicious code.

newProxyInPackage.{package name}

ability to create a proxy instance in the specified package of which
the non-public interface that the proxy class implements.

This gives code access to classes in packages to which it normally
does not have access and the dynamic proxy class is in the system
protection domain. Malicious code may use these classes to
help in its attempt to compromise security in the system.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public ReflectPermission​(
String
name)

Constructs a ReflectPermission with the specified name.

**Parameters:**
- name

- the name of the ReflectPermission

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

#### public ReflectPermission​(
String
name,

String
actions)

Constructs a ReflectPermission with the specified name and actions.
The actions should be null; they are ignored.

**Parameters:**
- name

- the name of the ReflectPermission
- actions

- should be null

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

#### Class ReflectPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.lang.reflect.ReflectPermission

java.security.Permission

- java.security.BasicPermission
- - java.lang.reflect.ReflectPermission

java.security.BasicPermission

- java.lang.reflect.ReflectPermission

java.lang.reflect.ReflectPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
ReflectPermission

extends
BasicPermission
```

The Permission class for reflective operations.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

suppressAccessChecks

ability to suppress the standard Java language access checks
on fields and methods in a class; allow access not only public members
but also allow access to default (package) access, protected,
and private members.

This is dangerous in that information (possibly confidential) and
methods normally unavailable would be accessible to malicious code.

newProxyInPackage.{package name}

ability to create a proxy instance in the specified package of which
the non-public interface that the proxy class implements.

This gives code access to classes in packages to which it normally
does not have access and the dynamic proxy class is in the system
protection domain. Malicious code may use these classes to
help in its attempt to compromise security in the system.

**Since:** 1.2
**See Also:** Permission

,

BasicPermission

,

AccessibleObject

,

Field.get(java.lang.Object)

,

Field.set(java.lang.Object, java.lang.Object)

,

Method.invoke(java.lang.Object, java.lang.Object...)

,

Constructor.newInstance(java.lang.Object...)

,

Proxy.newProxyInstance(java.lang.ClassLoader, java.lang.Class<?>[], java.lang.reflect.InvocationHandler)

,

Serialized Form

public final class

ReflectPermission

extends

BasicPermission

The Permission class for reflective operations.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

suppressAccessChecks

ability to suppress the standard Java language access checks
on fields and methods in a class; allow access not only public members
but also allow access to default (package) access, protected,
and private members.

This is dangerous in that information (possibly confidential) and
methods normally unavailable would be accessible to malicious code.

newProxyInPackage.{package name}

ability to create a proxy instance in the specified package of which
the non-public interface that the proxy class implements.

This gives code access to classes in packages to which it normally
does not have access and the dynamic proxy class is in the system
protection domain. Malicious code may use these classes to
help in its attempt to compromise security in the system.

The following table
provides a summary description of what the permission allows,
and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

suppressAccessChecks

ability to suppress the standard Java language access checks
on fields and methods in a class; allow access not only public members
but also allow access to default (package) access, protected,
and private members.

This is dangerous in that information (possibly confidential) and
methods normally unavailable would be accessible to malicious code.

newProxyInPackage.{package name}

ability to create a proxy instance in the specified package of which
the non-public interface that the proxy class implements.

This gives code access to classes in packages to which it normally
does not have access and the dynamic proxy class is in the system
protection domain. Malicious code may use these classes to
help in its attempt to compromise security in the system.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ReflectPermission

​(

String

name)

Constructs a ReflectPermission with the specified name.

ReflectPermission

​(

String

name,

String

actions)

Constructs a ReflectPermission with the specified name and actions.

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

ReflectPermission

​(

String

name)

Constructs a ReflectPermission with the specified name.

ReflectPermission

​(

String

name,

String

actions)

Constructs a ReflectPermission with the specified name and actions.

---

#### Constructor Summary

Constructs a ReflectPermission with the specified name.

Constructs a ReflectPermission with the specified name and actions.

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

- ReflectPermission

```java
public ReflectPermission​(
String
name)
```

Constructs a ReflectPermission with the specified name.

**Parameters:** name

- the name of the ReflectPermission
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

- ReflectPermission

```java
public ReflectPermission​(
String
name,

String
actions)
```

Constructs a ReflectPermission with the specified name and actions.
The actions should be null; they are ignored.

**Parameters:** name

- the name of the ReflectPermission
**Parameters:** actions

- should be null
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

- ReflectPermission

```java
public ReflectPermission​(
String
name)
```

Constructs a ReflectPermission with the specified name.

**Parameters:** name

- the name of the ReflectPermission
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

- ReflectPermission

```java
public ReflectPermission​(
String
name,

String
actions)
```

Constructs a ReflectPermission with the specified name and actions.
The actions should be null; they are ignored.

**Parameters:** name

- the name of the ReflectPermission
**Parameters:** actions

- should be null
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

ReflectPermission

```java
public ReflectPermission​(
String
name)
```

Constructs a ReflectPermission with the specified name.

**Parameters:** name

- the name of the ReflectPermission
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

#### ReflectPermission

public ReflectPermission​(

String

name)

Constructs a ReflectPermission with the specified name.

ReflectPermission

```java
public ReflectPermission​(
String
name,

String
actions)
```

Constructs a ReflectPermission with the specified name and actions.
The actions should be null; they are ignored.

**Parameters:** name

- the name of the ReflectPermission
**Parameters:** actions

- should be null
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

#### ReflectPermission

public ReflectPermission​(

String

name,

String

actions)

Constructs a ReflectPermission with the specified name and actions.
The actions should be null; they are ignored.

---

