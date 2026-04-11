# Class UserPrincipalLookupService

**Source:** `java.base\java\nio\file\attribute\UserPrincipalLookupService.html`

### Class Description

```java
public abstract class
UserPrincipalLookupService

extends
Object
```

An object to lookup user and group principals by name. A

UserPrincipal

represents an identity that may be used to determine access rights to objects
in a file system. A

GroupPrincipal

represents a

group identity

.
A

UserPrincipalLookupService

defines methods to lookup identities by
name or group name (which are typically user or account names). Whether names
and group names are case sensitive or not depends on the implementation.
The exact definition of a group is implementation specific but typically a
group represents an identity created for administrative purposes so as to
determine the access rights for the members of the group. In particular it is
implementation specific if the

namespace

for names and groups is the
same or is distinct. To ensure consistent and correct behavior across
platforms it is recommended that this API be used as if the namespaces are
distinct. In other words, the

lookupPrincipalByName

should be used to lookup users, and

lookupPrincipalByGroupName

should be used to
lookup groups.

**Since:** 1.7
**See Also:** FileSystem.getUserPrincipalLookupService()

---

### Field Details

*No entries found.*

### Constructor Details

#### protected UserPrincipalLookupService()

Initializes a new instance of this class.

---

### Method Details

#### public abstract
UserPrincipal
lookupPrincipalByName​(
String
name)
throws
IOException

Lookup a user principal by name.

**Parameters:**
- name

- the string representation of the user principal to lookup

**Returns:**
- a user principal

**Throws:**
- UserPrincipalNotFoundException

- the principal does not exist
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

---

#### public abstract
GroupPrincipal
lookupPrincipalByGroupName​(
String
group)
throws
IOException

Lookup a group principal by group name.

Where an implementation does not support any notion of group then
this method always throws

UserPrincipalNotFoundException

. Where
the namespace for user accounts and groups is the same, then this method
is identical to invoking

lookupPrincipalByName

.

**Parameters:**
- group

- the string representation of the group to lookup

**Returns:**
- a group principal

**Throws:**
- UserPrincipalNotFoundException

- the principal does not exist or is not a group
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

---

### Additional Sections

#### Class UserPrincipalLookupService

java.lang.Object

- java.nio.file.attribute.UserPrincipalLookupService

java.nio.file.attribute.UserPrincipalLookupService

```java
public abstract class
UserPrincipalLookupService

extends
Object
```

An object to lookup user and group principals by name. A

UserPrincipal

represents an identity that may be used to determine access rights to objects
in a file system. A

GroupPrincipal

represents a

group identity

.
A

UserPrincipalLookupService

defines methods to lookup identities by
name or group name (which are typically user or account names). Whether names
and group names are case sensitive or not depends on the implementation.
The exact definition of a group is implementation specific but typically a
group represents an identity created for administrative purposes so as to
determine the access rights for the members of the group. In particular it is
implementation specific if the

namespace

for names and groups is the
same or is distinct. To ensure consistent and correct behavior across
platforms it is recommended that this API be used as if the namespaces are
distinct. In other words, the

lookupPrincipalByName

should be used to lookup users, and

lookupPrincipalByGroupName

should be used to
lookup groups.

**Since:** 1.7
**See Also:** FileSystem.getUserPrincipalLookupService()

public abstract class

UserPrincipalLookupService

extends

Object

An object to lookup user and group principals by name. A

UserPrincipal

represents an identity that may be used to determine access rights to objects
in a file system. A

GroupPrincipal

represents a

group identity

.
A

UserPrincipalLookupService

defines methods to lookup identities by
name or group name (which are typically user or account names). Whether names
and group names are case sensitive or not depends on the implementation.
The exact definition of a group is implementation specific but typically a
group represents an identity created for administrative purposes so as to
determine the access rights for the members of the group. In particular it is
implementation specific if the

namespace

for names and groups is the
same or is distinct. To ensure consistent and correct behavior across
platforms it is recommended that this API be used as if the namespaces are
distinct. In other words, the

lookupPrincipalByName

should be used to lookup users, and

lookupPrincipalByGroupName

should be used to
lookup groups.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

UserPrincipalLookupService

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

GroupPrincipal

lookupPrincipalByGroupName

​(

String

group)

Lookup a group principal by group name.

abstract

UserPrincipal

lookupPrincipalByName

​(

String

name)

Lookup a user principal by name.

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

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

UserPrincipalLookupService

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

GroupPrincipal

lookupPrincipalByGroupName

​(

String

group)

Lookup a group principal by group name.

abstract

UserPrincipal

lookupPrincipalByName

​(

String

name)

Lookup a user principal by name.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Lookup a group principal by group name.

Lookup a user principal by name.

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

toString

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

- UserPrincipalLookupService

```java
protected UserPrincipalLookupService()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- lookupPrincipalByName

```java
public abstract
UserPrincipal
lookupPrincipalByName​(
String
name)
throws
IOException
```

Lookup a user principal by name.

**Parameters:** name

- the string representation of the user principal to lookup
**Returns:** a user principal
**Throws:** UserPrincipalNotFoundException

- the principal does not exist
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

- lookupPrincipalByGroupName

```java
public abstract
GroupPrincipal
lookupPrincipalByGroupName​(
String
group)
throws
IOException
```

Lookup a group principal by group name.

Where an implementation does not support any notion of group then
this method always throws

UserPrincipalNotFoundException

. Where
the namespace for user accounts and groups is the same, then this method
is identical to invoking

lookupPrincipalByName

.

**Parameters:** group

- the string representation of the group to lookup
**Returns:** a group principal
**Throws:** UserPrincipalNotFoundException

- the principal does not exist or is not a group
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

Constructor Detail

- UserPrincipalLookupService

```java
protected UserPrincipalLookupService()
```

Initializes a new instance of this class.

---

#### Constructor Detail

UserPrincipalLookupService

```java
protected UserPrincipalLookupService()
```

Initializes a new instance of this class.

---

#### UserPrincipalLookupService

protected UserPrincipalLookupService()

Initializes a new instance of this class.

Method Detail

- lookupPrincipalByName

```java
public abstract
UserPrincipal
lookupPrincipalByName​(
String
name)
throws
IOException
```

Lookup a user principal by name.

**Parameters:** name

- the string representation of the user principal to lookup
**Returns:** a user principal
**Throws:** UserPrincipalNotFoundException

- the principal does not exist
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

- lookupPrincipalByGroupName

```java
public abstract
GroupPrincipal
lookupPrincipalByGroupName​(
String
group)
throws
IOException
```

Lookup a group principal by group name.

Where an implementation does not support any notion of group then
this method always throws

UserPrincipalNotFoundException

. Where
the namespace for user accounts and groups is the same, then this method
is identical to invoking

lookupPrincipalByName

.

**Parameters:** group

- the string representation of the group to lookup
**Returns:** a group principal
**Throws:** UserPrincipalNotFoundException

- the principal does not exist or is not a group
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

---

#### Method Detail

lookupPrincipalByName

```java
public abstract
UserPrincipal
lookupPrincipalByName​(
String
name)
throws
IOException
```

Lookup a user principal by name.

**Parameters:** name

- the string representation of the user principal to lookup
**Returns:** a user principal
**Throws:** UserPrincipalNotFoundException

- the principal does not exist
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

---

#### lookupPrincipalByName

public abstract

UserPrincipal

lookupPrincipalByName​(

String

name)
throws

IOException

Lookup a user principal by name.

lookupPrincipalByGroupName

```java
public abstract
GroupPrincipal
lookupPrincipalByGroupName​(
String
group)
throws
IOException
```

Lookup a group principal by group name.

Where an implementation does not support any notion of group then
this method always throws

UserPrincipalNotFoundException

. Where
the namespace for user accounts and groups is the same, then this method
is identical to invoking

lookupPrincipalByName

.

**Parameters:** group

- the string representation of the group to lookup
**Returns:** a group principal
**Throws:** UserPrincipalNotFoundException

- the principal does not exist or is not a group
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it checks

RuntimePermission

("lookupUserInformation")

---

#### lookupPrincipalByGroupName

public abstract

GroupPrincipal

lookupPrincipalByGroupName​(

String

group)
throws

IOException

Lookup a group principal by group name.

Where an implementation does not support any notion of group then
this method always throws

UserPrincipalNotFoundException

. Where
the namespace for user accounts and groups is the same, then this method
is identical to invoking

lookupPrincipalByName

.

Where an implementation does not support any notion of group then
this method always throws

UserPrincipalNotFoundException

. Where
the namespace for user accounts and groups is the same, then this method
is identical to invoking

lookupPrincipalByName

.

---

