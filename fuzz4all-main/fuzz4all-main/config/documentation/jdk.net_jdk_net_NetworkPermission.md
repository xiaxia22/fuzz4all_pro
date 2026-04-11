# Class NetworkPermission

**Source:** `jdk.net\jdk\net\NetworkPermission.html`

### Class Description

```java
public final class
NetworkPermission

extends
BasicPermission
```

Represents permission to access the extended networking capabilities
defined in the jdk.net package. These permissions contain a target
name, but no actions list. Callers either possess the permission or not.

The following targets are defined:

permission target name,
what the target allows,and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setOption.SO_FLOW_SLA

set the

SO_FLOW_SLA

option
on any socket that supports it

allows caller to set a higher priority or bandwidth allocation
to sockets it creates, than they might otherwise be allowed.

getOption.SO_FLOW_SLA

retrieve the

SO_FLOW_SLA

setting from any socket that supports the option

allows caller access to SLA information that it might not
otherwise have

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public NetworkPermission​(
String
name)

Creates a NetworkPermission with the given target name.

**Parameters:**
- name

- the permission target name

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

#### public NetworkPermission​(
String
name,

String
actions)

Creates a NetworkPermission with the given target name.

**Parameters:**
- name

- the permission target name
- actions

- should be

null

. Is ignored if not.

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

#### Class NetworkPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - jdk.net.NetworkPermission

java.security.Permission

- java.security.BasicPermission
- - jdk.net.NetworkPermission

java.security.BasicPermission

- jdk.net.NetworkPermission

jdk.net.NetworkPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
NetworkPermission

extends
BasicPermission
```

Represents permission to access the extended networking capabilities
defined in the jdk.net package. These permissions contain a target
name, but no actions list. Callers either possess the permission or not.

The following targets are defined:

permission target name,
what the target allows,and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setOption.SO_FLOW_SLA

set the

SO_FLOW_SLA

option
on any socket that supports it

allows caller to set a higher priority or bandwidth allocation
to sockets it creates, than they might otherwise be allowed.

getOption.SO_FLOW_SLA

retrieve the

SO_FLOW_SLA

setting from any socket that supports the option

allows caller access to SLA information that it might not
otherwise have

**Since:** 1.8
**See Also:** ExtendedSocketOptions

,

Serialized Form

public final class

NetworkPermission

extends

BasicPermission

Represents permission to access the extended networking capabilities
defined in the jdk.net package. These permissions contain a target
name, but no actions list. Callers either possess the permission or not.

The following targets are defined:

permission target name,
what the target allows,and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setOption.SO_FLOW_SLA

set the

SO_FLOW_SLA

option
on any socket that supports it

allows caller to set a higher priority or bandwidth allocation
to sockets it creates, than they might otherwise be allowed.

getOption.SO_FLOW_SLA

retrieve the

SO_FLOW_SLA

setting from any socket that supports the option

allows caller access to SLA information that it might not
otherwise have

The following targets are defined:

permission target name,
what the target allows,and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setOption.SO_FLOW_SLA

set the

SO_FLOW_SLA

option
on any socket that supports it

allows caller to set a higher priority or bandwidth allocation
to sockets it creates, than they might otherwise be allowed.

getOption.SO_FLOW_SLA

retrieve the

SO_FLOW_SLA

setting from any socket that supports the option

allows caller access to SLA information that it might not
otherwise have

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NetworkPermission

​(

String

name)

Creates a NetworkPermission with the given target name.

NetworkPermission

​(

String

name,

String

actions)

Creates a NetworkPermission with the given target name.

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

NetworkPermission

​(

String

name)

Creates a NetworkPermission with the given target name.

NetworkPermission

​(

String

name,

String

actions)

Creates a NetworkPermission with the given target name.

---

#### Constructor Summary

Creates a NetworkPermission with the given target name.

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

- NetworkPermission

```java
public NetworkPermission​(
String
name)
```

Creates a NetworkPermission with the given target name.

**Parameters:** name

- the permission target name
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

- NetworkPermission

```java
public NetworkPermission​(
String
name,

String
actions)
```

Creates a NetworkPermission with the given target name.

**Parameters:** name

- the permission target name
**Parameters:** actions

- should be

null

. Is ignored if not.
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

- NetworkPermission

```java
public NetworkPermission​(
String
name)
```

Creates a NetworkPermission with the given target name.

**Parameters:** name

- the permission target name
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

- NetworkPermission

```java
public NetworkPermission​(
String
name,

String
actions)
```

Creates a NetworkPermission with the given target name.

**Parameters:** name

- the permission target name
**Parameters:** actions

- should be

null

. Is ignored if not.
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

NetworkPermission

```java
public NetworkPermission​(
String
name)
```

Creates a NetworkPermission with the given target name.

**Parameters:** name

- the permission target name
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

#### NetworkPermission

public NetworkPermission​(

String

name)

Creates a NetworkPermission with the given target name.

NetworkPermission

```java
public NetworkPermission​(
String
name,

String
actions)
```

Creates a NetworkPermission with the given target name.

**Parameters:** name

- the permission target name
**Parameters:** actions

- should be

null

. Is ignored if not.
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

#### NetworkPermission

public NetworkPermission​(

String

name,

String

actions)

Creates a NetworkPermission with the given target name.

---

