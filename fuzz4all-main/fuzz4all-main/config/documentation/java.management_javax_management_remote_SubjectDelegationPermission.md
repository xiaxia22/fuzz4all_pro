# Class SubjectDelegationPermission

**Source:** `java.management\javax\management\remote\SubjectDelegationPermission.html`

### Class Description

```java
public final class
SubjectDelegationPermission

extends
BasicPermission
```

Permission required by an authentication identity to perform
operations on behalf of an authorization identity.

A SubjectDelegationPermission contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The target name is the name of the authorization principal
classname followed by a period and the authorization principal
name, that is

"

PrincipalClassName

.

PrincipalName

"

.

An asterisk may appear by itself, or if immediately preceded
by a "." may appear at the end of the target name, to signify a
wildcard match.

For example, "*", "javax.management.remote.JMXPrincipal.*" and
"javax.management.remote.JMXPrincipal.delegate" are valid target
names. The first one denotes any principal name from any principal
class, the second one denotes any principal name of the concrete
principal class

javax.management.remote.JMXPrincipal

and the third one denotes a concrete principal name

delegate

of the concrete principal class

javax.management.remote.JMXPrincipal

.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public SubjectDelegationPermission​(
String
name)

Creates a new SubjectDelegationPermission with the specified name.
The name is the symbolic name of the SubjectDelegationPermission.

**Parameters:**
- name

- the name of the SubjectDelegationPermission

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

#### public SubjectDelegationPermission​(
String
name,

String
actions)

Creates a new SubjectDelegationPermission object with the
specified name. The name is the symbolic name of the
SubjectDelegationPermission, and the actions String is
currently unused and must be null.

**Parameters:**
- name

- the name of the SubjectDelegationPermission
- actions

- must be null.

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

is empty
or

actions

is not null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SubjectDelegationPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - javax.management.remote.SubjectDelegationPermission

java.security.Permission

- java.security.BasicPermission
- - javax.management.remote.SubjectDelegationPermission

java.security.BasicPermission

- javax.management.remote.SubjectDelegationPermission

javax.management.remote.SubjectDelegationPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
SubjectDelegationPermission

extends
BasicPermission
```

Permission required by an authentication identity to perform
operations on behalf of an authorization identity.

A SubjectDelegationPermission contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The target name is the name of the authorization principal
classname followed by a period and the authorization principal
name, that is

"

PrincipalClassName

.

PrincipalName

"

.

An asterisk may appear by itself, or if immediately preceded
by a "." may appear at the end of the target name, to signify a
wildcard match.

For example, "*", "javax.management.remote.JMXPrincipal.*" and
"javax.management.remote.JMXPrincipal.delegate" are valid target
names. The first one denotes any principal name from any principal
class, the second one denotes any principal name of the concrete
principal class

javax.management.remote.JMXPrincipal

and the third one denotes a concrete principal name

delegate

of the concrete principal class

javax.management.remote.JMXPrincipal

.

**Since:** 1.5
**See Also:** Serialized Form

public final class

SubjectDelegationPermission

extends

BasicPermission

Permission required by an authentication identity to perform
operations on behalf of an authorization identity.

A SubjectDelegationPermission contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The target name is the name of the authorization principal
classname followed by a period and the authorization principal
name, that is

"

PrincipalClassName

.

PrincipalName

"

.

An asterisk may appear by itself, or if immediately preceded
by a "." may appear at the end of the target name, to signify a
wildcard match.

For example, "*", "javax.management.remote.JMXPrincipal.*" and
"javax.management.remote.JMXPrincipal.delegate" are valid target
names. The first one denotes any principal name from any principal
class, the second one denotes any principal name of the concrete
principal class

javax.management.remote.JMXPrincipal

and the third one denotes a concrete principal name

delegate

of the concrete principal class

javax.management.remote.JMXPrincipal

.

Permission required by an authentication identity to perform
operations on behalf of an authorization identity.

A SubjectDelegationPermission contains a name (also referred
to as a "target name") but no actions list; you either have the
named permission or you don't.

The target name is the name of the authorization principal
classname followed by a period and the authorization principal
name, that is

"

PrincipalClassName

.

PrincipalName

"

.

An asterisk may appear by itself, or if immediately preceded
by a "." may appear at the end of the target name, to signify a
wildcard match.

For example, "*", "javax.management.remote.JMXPrincipal.*" and
"javax.management.remote.JMXPrincipal.delegate" are valid target
names. The first one denotes any principal name from any principal
class, the second one denotes any principal name of the concrete
principal class

javax.management.remote.JMXPrincipal

and the third one denotes a concrete principal name

delegate

of the concrete principal class

javax.management.remote.JMXPrincipal

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SubjectDelegationPermission

​(

String

name)

Creates a new SubjectDelegationPermission with the specified name.

SubjectDelegationPermission

​(

String

name,

String

actions)

Creates a new SubjectDelegationPermission object with the
specified name.

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

SubjectDelegationPermission

​(

String

name)

Creates a new SubjectDelegationPermission with the specified name.

SubjectDelegationPermission

​(

String

name,

String

actions)

Creates a new SubjectDelegationPermission object with the
specified name.

---

#### Constructor Summary

Creates a new SubjectDelegationPermission with the specified name.

Creates a new SubjectDelegationPermission object with the
specified name.

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

- SubjectDelegationPermission

```java
public SubjectDelegationPermission​(
String
name)
```

Creates a new SubjectDelegationPermission with the specified name.
The name is the symbolic name of the SubjectDelegationPermission.

**Parameters:** name

- the name of the SubjectDelegationPermission
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

- SubjectDelegationPermission

```java
public SubjectDelegationPermission​(
String
name,

String
actions)
```

Creates a new SubjectDelegationPermission object with the
specified name. The name is the symbolic name of the
SubjectDelegationPermission, and the actions String is
currently unused and must be null.

**Parameters:** name

- the name of the SubjectDelegationPermission
**Parameters:** actions

- must be null.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty
or

actions

is not null.

Constructor Detail

- SubjectDelegationPermission

```java
public SubjectDelegationPermission​(
String
name)
```

Creates a new SubjectDelegationPermission with the specified name.
The name is the symbolic name of the SubjectDelegationPermission.

**Parameters:** name

- the name of the SubjectDelegationPermission
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

- SubjectDelegationPermission

```java
public SubjectDelegationPermission​(
String
name,

String
actions)
```

Creates a new SubjectDelegationPermission object with the
specified name. The name is the symbolic name of the
SubjectDelegationPermission, and the actions String is
currently unused and must be null.

**Parameters:** name

- the name of the SubjectDelegationPermission
**Parameters:** actions

- must be null.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty
or

actions

is not null.

---

#### Constructor Detail

SubjectDelegationPermission

```java
public SubjectDelegationPermission​(
String
name)
```

Creates a new SubjectDelegationPermission with the specified name.
The name is the symbolic name of the SubjectDelegationPermission.

**Parameters:** name

- the name of the SubjectDelegationPermission
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

#### SubjectDelegationPermission

public SubjectDelegationPermission​(

String

name)

Creates a new SubjectDelegationPermission with the specified name.
The name is the symbolic name of the SubjectDelegationPermission.

SubjectDelegationPermission

```java
public SubjectDelegationPermission​(
String
name,

String
actions)
```

Creates a new SubjectDelegationPermission object with the
specified name. The name is the symbolic name of the
SubjectDelegationPermission, and the actions String is
currently unused and must be null.

**Parameters:** name

- the name of the SubjectDelegationPermission
**Parameters:** actions

- must be null.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty
or

actions

is not null.

---

#### SubjectDelegationPermission

public SubjectDelegationPermission​(

String

name,

String

actions)

Creates a new SubjectDelegationPermission object with the
specified name. The name is the symbolic name of the
SubjectDelegationPermission, and the actions String is
currently unused and must be null.

---

