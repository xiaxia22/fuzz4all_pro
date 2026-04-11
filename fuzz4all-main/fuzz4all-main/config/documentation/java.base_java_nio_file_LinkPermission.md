# Class LinkPermission

**Source:** `java.base\java\nio\file\LinkPermission.html`

### Class Description

```java
public final class
LinkPermission

extends
BasicPermission
```

The

Permission

class for link creation operations.

The following table provides a summary description of what the permission
allows, and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

hard

Ability to add an existing file to a directory. This is sometimes
known as creating a link, or hard link.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker access to all files.

symbolic

Ability to create symbolic links.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker to access to all files.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public LinkPermission​(
String
name)

Constructs a

LinkPermission

with the specified name.

**Parameters:**
- name

- the name of the permission. It must be "hard" or "symbolic".

**Throws:**
- IllegalArgumentException

- if name is empty or invalid

---

#### public LinkPermission​(
String
name,

String
actions)

Constructs a

LinkPermission

with the specified name.

**Parameters:**
- name

- the name of the permission; must be "hard" or "symbolic".
- actions

- the actions for the permission; must be the empty string or

null

**Throws:**
- IllegalArgumentException

- if name is empty or invalid, or actions is a non-empty string

---

### Method Details

*No entries found.*

### Additional Sections

#### Class LinkPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.nio.file.LinkPermission

java.security.Permission

- java.security.BasicPermission
- - java.nio.file.LinkPermission

java.security.BasicPermission

- java.nio.file.LinkPermission

java.nio.file.LinkPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
LinkPermission

extends
BasicPermission
```

The

Permission

class for link creation operations.

The following table provides a summary description of what the permission
allows, and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

hard

Ability to add an existing file to a directory. This is sometimes
known as creating a link, or hard link.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker access to all files.

symbolic

Ability to create symbolic links.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker to access to all files.

**Since:** 1.7
**See Also:** Files.createLink(java.nio.file.Path, java.nio.file.Path)

,

Files.createSymbolicLink(java.nio.file.Path, java.nio.file.Path, java.nio.file.attribute.FileAttribute<?>...)

,

Serialized Form

public final class

LinkPermission

extends

BasicPermission

The

Permission

class for link creation operations.

The following table provides a summary description of what the permission
allows, and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

hard

Ability to add an existing file to a directory. This is sometimes
known as creating a link, or hard link.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker access to all files.

symbolic

Ability to create symbolic links.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker to access to all files.

The following table provides a summary description of what the permission
allows, and discusses the risks of granting code the permission.

Table shows permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

hard

Ability to add an existing file to a directory. This is sometimes
known as creating a link, or hard link.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker access to all files.

symbolic

Ability to create symbolic links.

Extreme care should be taken when granting this permission. It allows
linking to any file or directory in the file system thus allowing the
attacker to access to all files.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LinkPermission

​(

String

name)

Constructs a

LinkPermission

with the specified name.

LinkPermission

​(

String

name,

String

actions)

Constructs a

LinkPermission

with the specified name.

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

LinkPermission

​(

String

name)

Constructs a

LinkPermission

with the specified name.

LinkPermission

​(

String

name,

String

actions)

Constructs a

LinkPermission

with the specified name.

---

#### Constructor Summary

Constructs a

LinkPermission

with the specified name.

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

- LinkPermission

```java
public LinkPermission​(
String
name)
```

Constructs a

LinkPermission

with the specified name.

**Parameters:** name

- the name of the permission. It must be "hard" or "symbolic".
**Throws:** IllegalArgumentException

- if name is empty or invalid

- LinkPermission

```java
public LinkPermission​(
String
name,

String
actions)
```

Constructs a

LinkPermission

with the specified name.

**Parameters:** name

- the name of the permission; must be "hard" or "symbolic".
**Parameters:** actions

- the actions for the permission; must be the empty string or

null
**Throws:** IllegalArgumentException

- if name is empty or invalid, or actions is a non-empty string

Constructor Detail

- LinkPermission

```java
public LinkPermission​(
String
name)
```

Constructs a

LinkPermission

with the specified name.

**Parameters:** name

- the name of the permission. It must be "hard" or "symbolic".
**Throws:** IllegalArgumentException

- if name is empty or invalid

- LinkPermission

```java
public LinkPermission​(
String
name,

String
actions)
```

Constructs a

LinkPermission

with the specified name.

**Parameters:** name

- the name of the permission; must be "hard" or "symbolic".
**Parameters:** actions

- the actions for the permission; must be the empty string or

null
**Throws:** IllegalArgumentException

- if name is empty or invalid, or actions is a non-empty string

---

#### Constructor Detail

LinkPermission

```java
public LinkPermission​(
String
name)
```

Constructs a

LinkPermission

with the specified name.

**Parameters:** name

- the name of the permission. It must be "hard" or "symbolic".
**Throws:** IllegalArgumentException

- if name is empty or invalid

---

#### LinkPermission

public LinkPermission​(

String

name)

Constructs a

LinkPermission

with the specified name.

LinkPermission

```java
public LinkPermission​(
String
name,

String
actions)
```

Constructs a

LinkPermission

with the specified name.

**Parameters:** name

- the name of the permission; must be "hard" or "symbolic".
**Parameters:** actions

- the actions for the permission; must be the empty string or

null
**Throws:** IllegalArgumentException

- if name is empty or invalid, or actions is a non-empty string

---

#### LinkPermission

public LinkPermission​(

String

name,

String

actions)

Constructs a

LinkPermission

with the specified name.

---

