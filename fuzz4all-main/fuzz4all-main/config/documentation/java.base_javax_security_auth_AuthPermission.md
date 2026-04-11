# Class AuthPermission

**Source:** `java.base\javax\security\auth\AuthPermission.html`

### Class Description

```java
public final class
AuthPermission

extends
BasicPermission
```

This class is for authentication permissions. An

AuthPermission

contains a name (also referred to as a "target name") but no actions
list; you either have the named permission or you don't.

The target name is the name of a security configuration parameter
(see below). Currently the

AuthPermission

object is used to
guard access to the

Subject

,

LoginContext

, and

Configuration

objects.

The standard target names for an Authentication Permission are:

```java
doAs - allow the caller to invoke the

Subject.doAs
methods.

doAsPrivileged - allow the caller to invoke the

Subject.doAsPrivileged
methods.

getSubject - allow for the retrieval of the
Subject(s) associated with the
current Thread.

getSubjectFromDomainCombiner - allow for the retrieval of the
Subject associated with the
a
SubjectDomainCombiner
.

setReadOnly - allow the caller to set a Subject
to be read-only.

modifyPrincipals - allow the caller to modify the
Set

of Principals associated with a

Subject

modifyPublicCredentials - allow the caller to modify the

Set
of public credentials
associated with a
Subject

modifyPrivateCredentials - allow the caller to modify the

Set
of private credentials
associated with a
Subject

refreshCredential - allow code to invoke the
refresh

method on a credential which implements
the
Refreshable
interface.

destroyCredential - allow code to invoke the
destroy

method on a credential
object

which implements the
Destroyable

interface.

createLoginContext.{name} - allow code to instantiate a

LoginContext
with the
specified
name
.
name

is used as the index into the installed login

Configuration

(that returned by

Configuration.getConfiguration()
).

name
can be wildcarded (set to '*')
to allow for any name.

getLoginConfiguration - allow for the retrieval of the system-wide
login Configuration.

createLoginConfiguration.{type} - allow code to obtain a Configuration
object via

Configuration.getInstance
.

setLoginConfiguration - allow for the setting of the system-wide
login Configuration.

refreshLoginConfiguration - allow for the refreshing of the system-wide
login Configuration.
```

Please note that granting this permission with the "modifyPrincipals",
"modifyPublicCredentials" or "modifyPrivateCredentials" target allows
a JAAS login module to populate principal or credential objects into
the Subject. Although reading information inside the private credentials
set requires a

PrivateCredentialPermission

of the credential type to
be granted, reading information inside the principals set and the public
credentials set requires no additional permission. These objects can contain
potentially sensitive information. For example, login modules that read
local user information or perform a Kerberos login are able to add
potentially sensitive information such as user ids, groups and domain names
to the principals set.

The following target name has been deprecated in favor of

createLoginContext.{name}

.

```java
createLoginContext - allow code to instantiate a

LoginContext
.
```

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public AuthPermission​(
String
name)

Creates a new AuthPermission with the specified name.
The name is the symbolic name of the AuthPermission.

**Parameters:**
- name

- the name of the AuthPermission

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

#### public AuthPermission​(
String
name,

String
actions)

Creates a new AuthPermission object with the specified name.
The name is the symbolic name of the AuthPermission, and the
actions String is currently unused and should be null.

**Parameters:**
- name

- the name of the AuthPermission
- actions

- should be null.

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

#### Class AuthPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - javax.security.auth.AuthPermission

java.security.Permission

- java.security.BasicPermission
- - javax.security.auth.AuthPermission

java.security.BasicPermission

- javax.security.auth.AuthPermission

javax.security.auth.AuthPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
AuthPermission

extends
BasicPermission
```

This class is for authentication permissions. An

AuthPermission

contains a name (also referred to as a "target name") but no actions
list; you either have the named permission or you don't.

The target name is the name of a security configuration parameter
(see below). Currently the

AuthPermission

object is used to
guard access to the

Subject

,

LoginContext

, and

Configuration

objects.

The standard target names for an Authentication Permission are:

```java
doAs - allow the caller to invoke the

Subject.doAs
methods.

doAsPrivileged - allow the caller to invoke the

Subject.doAsPrivileged
methods.

getSubject - allow for the retrieval of the
Subject(s) associated with the
current Thread.

getSubjectFromDomainCombiner - allow for the retrieval of the
Subject associated with the
a
SubjectDomainCombiner
.

setReadOnly - allow the caller to set a Subject
to be read-only.

modifyPrincipals - allow the caller to modify the
Set

of Principals associated with a

Subject

modifyPublicCredentials - allow the caller to modify the

Set
of public credentials
associated with a
Subject

modifyPrivateCredentials - allow the caller to modify the

Set
of private credentials
associated with a
Subject

refreshCredential - allow code to invoke the
refresh

method on a credential which implements
the
Refreshable
interface.

destroyCredential - allow code to invoke the
destroy

method on a credential
object

which implements the
Destroyable

interface.

createLoginContext.{name} - allow code to instantiate a

LoginContext
with the
specified
name
.
name

is used as the index into the installed login

Configuration

(that returned by

Configuration.getConfiguration()
).

name
can be wildcarded (set to '*')
to allow for any name.

getLoginConfiguration - allow for the retrieval of the system-wide
login Configuration.

createLoginConfiguration.{type} - allow code to obtain a Configuration
object via

Configuration.getInstance
.

setLoginConfiguration - allow for the setting of the system-wide
login Configuration.

refreshLoginConfiguration - allow for the refreshing of the system-wide
login Configuration.
```

Please note that granting this permission with the "modifyPrincipals",
"modifyPublicCredentials" or "modifyPrivateCredentials" target allows
a JAAS login module to populate principal or credential objects into
the Subject. Although reading information inside the private credentials
set requires a

PrivateCredentialPermission

of the credential type to
be granted, reading information inside the principals set and the public
credentials set requires no additional permission. These objects can contain
potentially sensitive information. For example, login modules that read
local user information or perform a Kerberos login are able to add
potentially sensitive information such as user ids, groups and domain names
to the principals set.

The following target name has been deprecated in favor of

createLoginContext.{name}

.

```java
createLoginContext - allow code to instantiate a

LoginContext
.
```

**Implementation Note:** Implementations may define additional target names, but should use naming
conventions such as reverse domain name notation to avoid name clashes.
**Since:** 1.4
**See Also:** Serialized Form

public final class

AuthPermission

extends

BasicPermission

This class is for authentication permissions. An

AuthPermission

contains a name (also referred to as a "target name") but no actions
list; you either have the named permission or you don't.

The target name is the name of a security configuration parameter
(see below). Currently the

AuthPermission

object is used to
guard access to the

Subject

,

LoginContext

, and

Configuration

objects.

The standard target names for an Authentication Permission are:

```java
doAs - allow the caller to invoke the

Subject.doAs
methods.

doAsPrivileged - allow the caller to invoke the

Subject.doAsPrivileged
methods.

getSubject - allow for the retrieval of the
Subject(s) associated with the
current Thread.

getSubjectFromDomainCombiner - allow for the retrieval of the
Subject associated with the
a
SubjectDomainCombiner
.

setReadOnly - allow the caller to set a Subject
to be read-only.

modifyPrincipals - allow the caller to modify the
Set

of Principals associated with a

Subject

modifyPublicCredentials - allow the caller to modify the

Set
of public credentials
associated with a
Subject

modifyPrivateCredentials - allow the caller to modify the

Set
of private credentials
associated with a
Subject

refreshCredential - allow code to invoke the
refresh

method on a credential which implements
the
Refreshable
interface.

destroyCredential - allow code to invoke the
destroy

method on a credential
object

which implements the
Destroyable

interface.

createLoginContext.{name} - allow code to instantiate a

LoginContext
with the
specified
name
.
name

is used as the index into the installed login

Configuration

(that returned by

Configuration.getConfiguration()
).

name
can be wildcarded (set to '*')
to allow for any name.

getLoginConfiguration - allow for the retrieval of the system-wide
login Configuration.

createLoginConfiguration.{type} - allow code to obtain a Configuration
object via

Configuration.getInstance
.

setLoginConfiguration - allow for the setting of the system-wide
login Configuration.

refreshLoginConfiguration - allow for the refreshing of the system-wide
login Configuration.
```

Please note that granting this permission with the "modifyPrincipals",
"modifyPublicCredentials" or "modifyPrivateCredentials" target allows
a JAAS login module to populate principal or credential objects into
the Subject. Although reading information inside the private credentials
set requires a

PrivateCredentialPermission

of the credential type to
be granted, reading information inside the principals set and the public
credentials set requires no additional permission. These objects can contain
potentially sensitive information. For example, login modules that read
local user information or perform a Kerberos login are able to add
potentially sensitive information such as user ids, groups and domain names
to the principals set.

The following target name has been deprecated in favor of

createLoginContext.{name}

.

```java
createLoginContext - allow code to instantiate a

LoginContext
.
```

The target name is the name of a security configuration parameter
(see below). Currently the

AuthPermission

object is used to
guard access to the

Subject

,

LoginContext

, and

Configuration

objects.

The standard target names for an Authentication Permission are:

```java
doAs - allow the caller to invoke the

Subject.doAs
methods.

doAsPrivileged - allow the caller to invoke the

Subject.doAsPrivileged
methods.

getSubject - allow for the retrieval of the
Subject(s) associated with the
current Thread.

getSubjectFromDomainCombiner - allow for the retrieval of the
Subject associated with the
a
SubjectDomainCombiner
.

setReadOnly - allow the caller to set a Subject
to be read-only.

modifyPrincipals - allow the caller to modify the
Set

of Principals associated with a

Subject

modifyPublicCredentials - allow the caller to modify the

Set
of public credentials
associated with a
Subject

modifyPrivateCredentials - allow the caller to modify the

Set
of private credentials
associated with a
Subject

refreshCredential - allow code to invoke the
refresh

method on a credential which implements
the
Refreshable
interface.

destroyCredential - allow code to invoke the
destroy

method on a credential
object

which implements the
Destroyable

interface.

createLoginContext.{name} - allow code to instantiate a

LoginContext
with the
specified
name
.
name

is used as the index into the installed login

Configuration

(that returned by

Configuration.getConfiguration()
).

name
can be wildcarded (set to '*')
to allow for any name.

getLoginConfiguration - allow for the retrieval of the system-wide
login Configuration.

createLoginConfiguration.{type} - allow code to obtain a Configuration
object via

Configuration.getInstance
.

setLoginConfiguration - allow for the setting of the system-wide
login Configuration.

refreshLoginConfiguration - allow for the refreshing of the system-wide
login Configuration.
```

Please note that granting this permission with the "modifyPrincipals",
"modifyPublicCredentials" or "modifyPrivateCredentials" target allows
a JAAS login module to populate principal or credential objects into
the Subject. Although reading information inside the private credentials
set requires a

PrivateCredentialPermission

of the credential type to
be granted, reading information inside the principals set and the public
credentials set requires no additional permission. These objects can contain
potentially sensitive information. For example, login modules that read
local user information or perform a Kerberos login are able to add
potentially sensitive information such as user ids, groups and domain names
to the principals set.

The following target name has been deprecated in favor of

createLoginContext.{name}

.

```java
createLoginContext - allow code to instantiate a

LoginContext
.
```

The standard target names for an Authentication Permission are:

```java
doAs - allow the caller to invoke the

Subject.doAs
methods.

doAsPrivileged - allow the caller to invoke the

Subject.doAsPrivileged
methods.

getSubject - allow for the retrieval of the
Subject(s) associated with the
current Thread.

getSubjectFromDomainCombiner - allow for the retrieval of the
Subject associated with the
a
SubjectDomainCombiner
.

setReadOnly - allow the caller to set a Subject
to be read-only.

modifyPrincipals - allow the caller to modify the
Set

of Principals associated with a

Subject

modifyPublicCredentials - allow the caller to modify the

Set
of public credentials
associated with a
Subject

modifyPrivateCredentials - allow the caller to modify the

Set
of private credentials
associated with a
Subject

refreshCredential - allow code to invoke the
refresh

method on a credential which implements
the
Refreshable
interface.

destroyCredential - allow code to invoke the
destroy

method on a credential
object

which implements the
Destroyable

interface.

createLoginContext.{name} - allow code to instantiate a

LoginContext
with the
specified
name
.
name

is used as the index into the installed login

Configuration

(that returned by

Configuration.getConfiguration()
).

name
can be wildcarded (set to '*')
to allow for any name.

getLoginConfiguration - allow for the retrieval of the system-wide
login Configuration.

createLoginConfiguration.{type} - allow code to obtain a Configuration
object via

Configuration.getInstance
.

setLoginConfiguration - allow for the setting of the system-wide
login Configuration.

refreshLoginConfiguration - allow for the refreshing of the system-wide
login Configuration.
```

Please note that granting this permission with the "modifyPrincipals",
"modifyPublicCredentials" or "modifyPrivateCredentials" target allows
a JAAS login module to populate principal or credential objects into
the Subject. Although reading information inside the private credentials
set requires a

PrivateCredentialPermission

of the credential type to
be granted, reading information inside the principals set and the public
credentials set requires no additional permission. These objects can contain
potentially sensitive information. For example, login modules that read
local user information or perform a Kerberos login are able to add
potentially sensitive information such as user ids, groups and domain names
to the principals set.

The following target name has been deprecated in favor of

createLoginContext.{name}

.

```java
createLoginContext - allow code to instantiate a

LoginContext
.
```

doAs - allow the caller to invoke the

Subject.doAs

methods.

doAsPrivileged - allow the caller to invoke the

Subject.doAsPrivileged

methods.

getSubject - allow for the retrieval of the
Subject(s) associated with the
current Thread.

getSubjectFromDomainCombiner - allow for the retrieval of the
Subject associated with the
a

SubjectDomainCombiner

.

setReadOnly - allow the caller to set a Subject
to be read-only.

modifyPrincipals - allow the caller to modify the

Set

of Principals associated with a

Subject

modifyPublicCredentials - allow the caller to modify the

Set

of public credentials
associated with a

Subject

modifyPrivateCredentials - allow the caller to modify the

Set

of private credentials
associated with a

Subject

refreshCredential - allow code to invoke the

refresh

method on a credential which implements
the

Refreshable

interface.

destroyCredential - allow code to invoke the

destroy

method on a credential

object

which implements the

Destroyable

interface.

createLoginContext.{name} - allow code to instantiate a

LoginContext

with the
specified

name

.

name

is used as the index into the installed login

Configuration

(that returned by

Configuration.getConfiguration()

).

name

can be wildcarded (set to '*')
to allow for any name.

getLoginConfiguration - allow for the retrieval of the system-wide
login Configuration.

createLoginConfiguration.{type} - allow code to obtain a Configuration
object via

Configuration.getInstance

.

setLoginConfiguration - allow for the setting of the system-wide
login Configuration.

refreshLoginConfiguration - allow for the refreshing of the system-wide
login Configuration.

Please note that granting this permission with the "modifyPrincipals",
"modifyPublicCredentials" or "modifyPrivateCredentials" target allows
a JAAS login module to populate principal or credential objects into
the Subject. Although reading information inside the private credentials
set requires a

PrivateCredentialPermission

of the credential type to
be granted, reading information inside the principals set and the public
credentials set requires no additional permission. These objects can contain
potentially sensitive information. For example, login modules that read
local user information or perform a Kerberos login are able to add
potentially sensitive information such as user ids, groups and domain names
to the principals set.

The following target name has been deprecated in favor of

createLoginContext.{name}

.

```java
createLoginContext - allow code to instantiate a

LoginContext
.
```

The following target name has been deprecated in favor of

createLoginContext.{name}

.

```java
createLoginContext - allow code to instantiate a

LoginContext
.
```

createLoginContext - allow code to instantiate a

LoginContext

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AuthPermission

​(

String

name)

Creates a new AuthPermission with the specified name.

AuthPermission

​(

String

name,

String

actions)

Creates a new AuthPermission object with the specified name.

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

AuthPermission

​(

String

name)

Creates a new AuthPermission with the specified name.

AuthPermission

​(

String

name,

String

actions)

Creates a new AuthPermission object with the specified name.

---

#### Constructor Summary

Creates a new AuthPermission with the specified name.

Creates a new AuthPermission object with the specified name.

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

- AuthPermission

```java
public AuthPermission​(
String
name)
```

Creates a new AuthPermission with the specified name.
The name is the symbolic name of the AuthPermission.

**Parameters:** name

- the name of the AuthPermission
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

- AuthPermission

```java
public AuthPermission​(
String
name,

String
actions)
```

Creates a new AuthPermission object with the specified name.
The name is the symbolic name of the AuthPermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the AuthPermission
**Parameters:** actions

- should be null.
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

- AuthPermission

```java
public AuthPermission​(
String
name)
```

Creates a new AuthPermission with the specified name.
The name is the symbolic name of the AuthPermission.

**Parameters:** name

- the name of the AuthPermission
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

- AuthPermission

```java
public AuthPermission​(
String
name,

String
actions)
```

Creates a new AuthPermission object with the specified name.
The name is the symbolic name of the AuthPermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the AuthPermission
**Parameters:** actions

- should be null.
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

AuthPermission

```java
public AuthPermission​(
String
name)
```

Creates a new AuthPermission with the specified name.
The name is the symbolic name of the AuthPermission.

**Parameters:** name

- the name of the AuthPermission
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

#### AuthPermission

public AuthPermission​(

String

name)

Creates a new AuthPermission with the specified name.
The name is the symbolic name of the AuthPermission.

AuthPermission

```java
public AuthPermission​(
String
name,

String
actions)
```

Creates a new AuthPermission object with the specified name.
The name is the symbolic name of the AuthPermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the AuthPermission
**Parameters:** actions

- should be null.
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

#### AuthPermission

public AuthPermission​(

String

name,

String

actions)

Creates a new AuthPermission object with the specified name.
The name is the symbolic name of the AuthPermission, and the
actions String is currently unused and should be null.

---

