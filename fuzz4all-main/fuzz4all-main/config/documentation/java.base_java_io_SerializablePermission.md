# Class SerializablePermission

**Source:** `java.base\java\io\SerializablePermission.html`

### Class Description

```java
public final class
SerializablePermission

extends
BasicPermission
```

This class is for Serializable permissions. A SerializablePermission
contains a name (also referred to as a "target name") but
no actions list; you either have the named permission
or you don't.

The target name is the name of the Serializable permission (see below).

The following table lists the standard

SerializablePermission

target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

enableSubclassImplementation

Subclass implementation of ObjectOutputStream or ObjectInputStream
to override the default serialization or deserialization, respectively,
of objects

Code can use this to serialize or
deserialize classes in a purposefully malfeasant manner. For example,
during serialization, malicious code can use this to
purposefully store confidential private field data in a way easily accessible
to attackers. Or, during deserialization it could, for example, deserialize
a class with all its private fields zeroed out.

enableSubstitution

Substitution of one object for another during
serialization or deserialization

This is dangerous because malicious code
can replace the actual object with one which has incorrect or
malignant data.

serialFilter

Setting a filter for ObjectInputStreams.

Code could remove a configured filter and remove protections
already established.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public SerializablePermission​(
String
name)

Creates a new SerializablePermission with the specified name.
The name is the symbolic name of the SerializablePermission, such as
"enableSubstitution", etc.

**Parameters:**
- name

- the name of the SerializablePermission.

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

#### public SerializablePermission​(
String
name,

String
actions)

Creates a new SerializablePermission object with the specified name.
The name is the symbolic name of the SerializablePermission, and the
actions String is currently unused and should be null.

**Parameters:**
- name

- the name of the SerializablePermission.
- actions

- currently unused and must be set to null

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

#### Class SerializablePermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.io.SerializablePermission

java.security.Permission

- java.security.BasicPermission
- - java.io.SerializablePermission

java.security.BasicPermission

- java.io.SerializablePermission

java.io.SerializablePermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
SerializablePermission

extends
BasicPermission
```

This class is for Serializable permissions. A SerializablePermission
contains a name (also referred to as a "target name") but
no actions list; you either have the named permission
or you don't.

The target name is the name of the Serializable permission (see below).

The following table lists the standard

SerializablePermission

target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

enableSubclassImplementation

Subclass implementation of ObjectOutputStream or ObjectInputStream
to override the default serialization or deserialization, respectively,
of objects

Code can use this to serialize or
deserialize classes in a purposefully malfeasant manner. For example,
during serialization, malicious code can use this to
purposefully store confidential private field data in a way easily accessible
to attackers. Or, during deserialization it could, for example, deserialize
a class with all its private fields zeroed out.

enableSubstitution

Substitution of one object for another during
serialization or deserialization

This is dangerous because malicious code
can replace the actual object with one which has incorrect or
malignant data.

serialFilter

Setting a filter for ObjectInputStreams.

Code could remove a configured filter and remove protections
already established.

**Since:** 1.2
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

SerializablePermission

extends

BasicPermission

This class is for Serializable permissions. A SerializablePermission
contains a name (also referred to as a "target name") but
no actions list; you either have the named permission
or you don't.

The target name is the name of the Serializable permission (see below).

The following table lists the standard

SerializablePermission

target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

enableSubclassImplementation

Subclass implementation of ObjectOutputStream or ObjectInputStream
to override the default serialization or deserialization, respectively,
of objects

Code can use this to serialize or
deserialize classes in a purposefully malfeasant manner. For example,
during serialization, malicious code can use this to
purposefully store confidential private field data in a way easily accessible
to attackers. Or, during deserialization it could, for example, deserialize
a class with all its private fields zeroed out.

enableSubstitution

Substitution of one object for another during
serialization or deserialization

This is dangerous because malicious code
can replace the actual object with one which has incorrect or
malignant data.

serialFilter

Setting a filter for ObjectInputStreams.

Code could remove a configured filter and remove protections
already established.

The target name is the name of the Serializable permission (see below).

The following table lists the standard

SerializablePermission

target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

enableSubclassImplementation

Subclass implementation of ObjectOutputStream or ObjectInputStream
to override the default serialization or deserialization, respectively,
of objects

Code can use this to serialize or
deserialize classes in a purposefully malfeasant manner. For example,
during serialization, malicious code can use this to
purposefully store confidential private field data in a way easily accessible
to attackers. Or, during deserialization it could, for example, deserialize
a class with all its private fields zeroed out.

enableSubstitution

Substitution of one object for another during
serialization or deserialization

This is dangerous because malicious code
can replace the actual object with one which has incorrect or
malignant data.

serialFilter

Setting a filter for ObjectInputStreams.

Code could remove a configured filter and remove protections
already established.

The following table lists the standard

SerializablePermission

target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

enableSubclassImplementation

Subclass implementation of ObjectOutputStream or ObjectInputStream
to override the default serialization or deserialization, respectively,
of objects

Code can use this to serialize or
deserialize classes in a purposefully malfeasant manner. For example,
during serialization, malicious code can use this to
purposefully store confidential private field data in a way easily accessible
to attackers. Or, during deserialization it could, for example, deserialize
a class with all its private fields zeroed out.

enableSubstitution

Substitution of one object for another during
serialization or deserialization

This is dangerous because malicious code
can replace the actual object with one which has incorrect or
malignant data.

serialFilter

Setting a filter for ObjectInputStreams.

Code could remove a configured filter and remove protections
already established.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SerializablePermission

​(

String

name)

Creates a new SerializablePermission with the specified name.

SerializablePermission

​(

String

name,

String

actions)

Creates a new SerializablePermission object with the specified name.

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

SerializablePermission

​(

String

name)

Creates a new SerializablePermission with the specified name.

SerializablePermission

​(

String

name,

String

actions)

Creates a new SerializablePermission object with the specified name.

---

#### Constructor Summary

Creates a new SerializablePermission with the specified name.

Creates a new SerializablePermission object with the specified name.

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

- SerializablePermission

```java
public SerializablePermission​(
String
name)
```

Creates a new SerializablePermission with the specified name.
The name is the symbolic name of the SerializablePermission, such as
"enableSubstitution", etc.

**Parameters:** name

- the name of the SerializablePermission.
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

- SerializablePermission

```java
public SerializablePermission​(
String
name,

String
actions)
```

Creates a new SerializablePermission object with the specified name.
The name is the symbolic name of the SerializablePermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the SerializablePermission.
**Parameters:** actions

- currently unused and must be set to null
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

- SerializablePermission

```java
public SerializablePermission​(
String
name)
```

Creates a new SerializablePermission with the specified name.
The name is the symbolic name of the SerializablePermission, such as
"enableSubstitution", etc.

**Parameters:** name

- the name of the SerializablePermission.
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

- SerializablePermission

```java
public SerializablePermission​(
String
name,

String
actions)
```

Creates a new SerializablePermission object with the specified name.
The name is the symbolic name of the SerializablePermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the SerializablePermission.
**Parameters:** actions

- currently unused and must be set to null
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

SerializablePermission

```java
public SerializablePermission​(
String
name)
```

Creates a new SerializablePermission with the specified name.
The name is the symbolic name of the SerializablePermission, such as
"enableSubstitution", etc.

**Parameters:** name

- the name of the SerializablePermission.
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

#### SerializablePermission

public SerializablePermission​(

String

name)

Creates a new SerializablePermission with the specified name.
The name is the symbolic name of the SerializablePermission, such as
"enableSubstitution", etc.

SerializablePermission

```java
public SerializablePermission​(
String
name,

String
actions)
```

Creates a new SerializablePermission object with the specified name.
The name is the symbolic name of the SerializablePermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the SerializablePermission.
**Parameters:** actions

- currently unused and must be set to null
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

#### SerializablePermission

public SerializablePermission​(

String

name,

String

actions)

Creates a new SerializablePermission object with the specified name.
The name is the symbolic name of the SerializablePermission, and the
actions String is currently unused and should be null.

---

