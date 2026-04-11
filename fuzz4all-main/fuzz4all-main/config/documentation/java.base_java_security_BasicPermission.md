# Class BasicPermission

**Source:** `java.base\java\security\BasicPermission.html`

### Class Description

```java
public abstract class
BasicPermission

extends
Permission

implements
Serializable
```

The BasicPermission class extends the Permission class, and
can be used as the base class for permissions that want to
follow the same naming convention as BasicPermission.

The name for a BasicPermission is the name of the given permission
(for example, "exit",
"setFactory", "print.queueJob", etc). The naming
convention follows the hierarchical property naming convention.
An asterisk may appear by itself, or if immediately preceded by a "."
may appear at the end of the name, to signify a wildcard match.
For example, "*" and "java.*" signify a wildcard match, while "*java", "a*b",
and "java*" do not.

The action string (inherited from Permission) is unused.
Thus, BasicPermission is commonly used as the base class for
"named" permissions
(ones that contain a name but no actions list; you either have the
named permission or you don't.)
Subclasses may implement actions on top of BasicPermission,
if desired.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicPermission​(
String
name)

Creates a new BasicPermission with the specified name.
Name is the symbolic name of the permission, such as
"setFactory",
"print.queueJob", or "topLevelWindow", etc.

**Parameters:**
- name

- the name of the BasicPermission.

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

#### public BasicPermission​(
String
name,

String
actions)

Creates a new BasicPermission object with the specified name.
The name is the symbolic name of the BasicPermission, and the
actions String is currently unused.

**Parameters:**
- name

- the name of the BasicPermission.
- actions

- ignored.

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

#### public boolean implies​(
Permission
p)

Checks if the specified permission is "implied" by
this object.

More specifically, this method returns true if:

- p

's class is the same as this object's class, and

p

's name equals or (in the case of wildcards)
is implied by this object's
name. For example, "a.b.*" implies "a.b.c".

**Specified by:**
- implies

in class

Permission

**Parameters:**
- p

- the permission to check against.

**Returns:**
- true if the passed permission is equal to or
implied by this permission, false otherwise.

---

#### public boolean equals​(
Object
obj)

Checks two BasicPermission objects for equality.
Checks that

obj

's class is the same as this object's class
and has the same name as this object.

**Specified by:**
- equals

in class

Permission

**Parameters:**
- obj

- the object we are testing for equality with this object.

**Returns:**
- true if

obj

's class is the same as this object's class
and has the same name as this BasicPermission object, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this object.
The hash code used is the hash code of the name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Specified by:**
- hashCode

in class

Permission

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
getActions()

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

**Specified by:**
- getActions

in class

Permission

**Returns:**
- the empty string "".

---

#### public
PermissionCollection
newPermissionCollection()

Returns a new PermissionCollection object for storing BasicPermission
objects.

BasicPermission objects must be stored in a manner that allows them
to be inserted in any order, but that also enables the
PermissionCollection

implies

method
to be implemented in an efficient (and consistent) manner.

**Overrides:**
- newPermissionCollection

in class

Permission

**Returns:**
- a new PermissionCollection object suitable for
storing BasicPermissions.

---

### Additional Sections

#### Class BasicPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission

java.security.Permission

- java.security.BasicPermission

java.security.BasicPermission

**All Implemented Interfaces:** Serializable

,

Guard

**Direct Known Subclasses:** AttachPermission

,

AudioPermission

,

AuthPermission

,

AWTPermission

,

DelegationPermission

,

FlightRecorderPermission

,

InquireSecContextPermission

,

JDIPermission

,

LinkPermission

,

LoggingPermission

,

ManagementPermission

,

MBeanServerPermission

,

MBeanTrustPermission

,

NetPermission

,

NetworkPermission

,

PropertyPermission

,

ReflectPermission

,

RuntimePermission

,

SecurityPermission

,

SerializablePermission

,

SQLPermission

,

SSLPermission

,

SubjectDelegationPermission

```java
public abstract class
BasicPermission

extends
Permission

implements
Serializable
```

The BasicPermission class extends the Permission class, and
can be used as the base class for permissions that want to
follow the same naming convention as BasicPermission.

The name for a BasicPermission is the name of the given permission
(for example, "exit",
"setFactory", "print.queueJob", etc). The naming
convention follows the hierarchical property naming convention.
An asterisk may appear by itself, or if immediately preceded by a "."
may appear at the end of the name, to signify a wildcard match.
For example, "*" and "java.*" signify a wildcard match, while "*java", "a*b",
and "java*" do not.

The action string (inherited from Permission) is unused.
Thus, BasicPermission is commonly used as the base class for
"named" permissions
(ones that contain a name but no actions list; you either have the
named permission or you don't.)
Subclasses may implement actions on top of BasicPermission,
if desired.

**Since:** 1.2
**See Also:** Permission

,

Permissions

,

PermissionCollection

,

SecurityManager

,

Serialized Form

public abstract class

BasicPermission

extends

Permission

implements

Serializable

The BasicPermission class extends the Permission class, and
can be used as the base class for permissions that want to
follow the same naming convention as BasicPermission.

The name for a BasicPermission is the name of the given permission
(for example, "exit",
"setFactory", "print.queueJob", etc). The naming
convention follows the hierarchical property naming convention.
An asterisk may appear by itself, or if immediately preceded by a "."
may appear at the end of the name, to signify a wildcard match.
For example, "*" and "java.*" signify a wildcard match, while "*java", "a*b",
and "java*" do not.

The action string (inherited from Permission) is unused.
Thus, BasicPermission is commonly used as the base class for
"named" permissions
(ones that contain a name but no actions list; you either have the
named permission or you don't.)
Subclasses may implement actions on top of BasicPermission,
if desired.

The name for a BasicPermission is the name of the given permission
(for example, "exit",
"setFactory", "print.queueJob", etc). The naming
convention follows the hierarchical property naming convention.
An asterisk may appear by itself, or if immediately preceded by a "."
may appear at the end of the name, to signify a wildcard match.
For example, "*" and "java.*" signify a wildcard match, while "*java", "a*b",
and "java*" do not.

The action string (inherited from Permission) is unused.
Thus, BasicPermission is commonly used as the base class for
"named" permissions
(ones that contain a name but no actions list; you either have the
named permission or you don't.)
Subclasses may implement actions on top of BasicPermission,
if desired.

The action string (inherited from Permission) is unused.
Thus, BasicPermission is commonly used as the base class for
"named" permissions
(ones that contain a name but no actions list; you either have the
named permission or you don't.)
Subclasses may implement actions on top of BasicPermission,
if desired.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicPermission

​(

String

name)

Creates a new BasicPermission with the specified name.

BasicPermission

​(

String

name,

String

actions)

Creates a new BasicPermission object with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two BasicPermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if the specified permission is "implied" by
this object.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing BasicPermission
objects.

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

BasicPermission

​(

String

name)

Creates a new BasicPermission with the specified name.

BasicPermission

​(

String

name,

String

actions)

Creates a new BasicPermission object with the specified name.

---

#### Constructor Summary

Creates a new BasicPermission with the specified name.

Creates a new BasicPermission object with the specified name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two BasicPermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if the specified permission is "implied" by
this object.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing BasicPermission
objects.

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

Checks two BasicPermission objects for equality.

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

Returns the hash code value for this object.

Checks if the specified permission is "implied" by
this object.

Returns a new PermissionCollection object for storing BasicPermission
objects.

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

- BasicPermission

```java
public BasicPermission​(
String
name)
```

Creates a new BasicPermission with the specified name.
Name is the symbolic name of the permission, such as
"setFactory",
"print.queueJob", or "topLevelWindow", etc.

**Parameters:** name

- the name of the BasicPermission.
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

- BasicPermission

```java
public BasicPermission​(
String
name,

String
actions)
```

Creates a new BasicPermission object with the specified name.
The name is the symbolic name of the BasicPermission, and the
actions String is currently unused.

**Parameters:** name

- the name of the BasicPermission.
**Parameters:** actions

- ignored.
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

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if the specified permission is "implied" by
this object.

More specifically, this method returns true if:

- p

's class is the same as this object's class, and

p

's name equals or (in the case of wildcards)
is implied by this object's
name. For example, "a.b.*" implies "a.b.c".

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the passed permission is equal to or
implied by this permission, false otherwise.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two BasicPermission objects for equality.
Checks that

obj

's class is the same as this object's class
and has the same name as this object.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if

obj

's class is the same as this object's class
and has the same name as this BasicPermission object, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.
The hash code used is the hash code of the name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

**Specified by:** getActions

in class

Permission
**Returns:** the empty string "".

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing BasicPermission
objects.

BasicPermission objects must be stored in a manner that allows them
to be inserted in any order, but that also enables the
PermissionCollection

implies

method
to be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for
storing BasicPermissions.

Constructor Detail

- BasicPermission

```java
public BasicPermission​(
String
name)
```

Creates a new BasicPermission with the specified name.
Name is the symbolic name of the permission, such as
"setFactory",
"print.queueJob", or "topLevelWindow", etc.

**Parameters:** name

- the name of the BasicPermission.
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

- BasicPermission

```java
public BasicPermission​(
String
name,

String
actions)
```

Creates a new BasicPermission object with the specified name.
The name is the symbolic name of the BasicPermission, and the
actions String is currently unused.

**Parameters:** name

- the name of the BasicPermission.
**Parameters:** actions

- ignored.
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

BasicPermission

```java
public BasicPermission​(
String
name)
```

Creates a new BasicPermission with the specified name.
Name is the symbolic name of the permission, such as
"setFactory",
"print.queueJob", or "topLevelWindow", etc.

**Parameters:** name

- the name of the BasicPermission.
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

#### BasicPermission

public BasicPermission​(

String

name)

Creates a new BasicPermission with the specified name.
Name is the symbolic name of the permission, such as
"setFactory",
"print.queueJob", or "topLevelWindow", etc.

BasicPermission

```java
public BasicPermission​(
String
name,

String
actions)
```

Creates a new BasicPermission object with the specified name.
The name is the symbolic name of the BasicPermission, and the
actions String is currently unused.

**Parameters:** name

- the name of the BasicPermission.
**Parameters:** actions

- ignored.
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

#### BasicPermission

public BasicPermission​(

String

name,

String

actions)

Creates a new BasicPermission object with the specified name.
The name is the symbolic name of the BasicPermission, and the
actions String is currently unused.

Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if the specified permission is "implied" by
this object.

More specifically, this method returns true if:

- p

's class is the same as this object's class, and

p

's name equals or (in the case of wildcards)
is implied by this object's
name. For example, "a.b.*" implies "a.b.c".

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the passed permission is equal to or
implied by this permission, false otherwise.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two BasicPermission objects for equality.
Checks that

obj

's class is the same as this object's class
and has the same name as this object.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if

obj

's class is the same as this object's class
and has the same name as this BasicPermission object, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.
The hash code used is the hash code of the name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

**Specified by:** getActions

in class

Permission
**Returns:** the empty string "".

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing BasicPermission
objects.

BasicPermission objects must be stored in a manner that allows them
to be inserted in any order, but that also enables the
PermissionCollection

implies

method
to be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for
storing BasicPermissions.

---

#### Method Detail

implies

```java
public boolean implies​(
Permission
p)
```

Checks if the specified permission is "implied" by
this object.

More specifically, this method returns true if:

- p

's class is the same as this object's class, and

p

's name equals or (in the case of wildcards)
is implied by this object's
name. For example, "a.b.*" implies "a.b.c".

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the passed permission is equal to or
implied by this permission, false otherwise.

---

#### implies

public boolean implies​(

Permission

p)

Checks if the specified permission is "implied" by
this object.

More specifically, this method returns true if:

- p

's class is the same as this object's class, and

p

's name equals or (in the case of wildcards)
is implied by this object's
name. For example, "a.b.*" implies "a.b.c".

More specifically, this method returns true if:

- p

's class is the same as this object's class, and

p

's name equals or (in the case of wildcards)
is implied by this object's
name. For example, "a.b.*" implies "a.b.c".

p

's class is the same as this object's class, and

p

's name equals or (in the case of wildcards)
is implied by this object's
name. For example, "a.b.*" implies "a.b.c".

equals

```java
public boolean equals​(
Object
obj)
```

Checks two BasicPermission objects for equality.
Checks that

obj

's class is the same as this object's class
and has the same name as this object.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if

obj

's class is the same as this object's class
and has the same name as this BasicPermission object, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two BasicPermission objects for equality.
Checks that

obj

's class is the same as this object's class
and has the same name as this object.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.
The hash code used is the hash code of the name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.
The hash code used is the hash code of the name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

**Specified by:** getActions

in class

Permission
**Returns:** the empty string "".

---

#### getActions

public

String

getActions()

Returns the canonical string representation of the actions,
which currently is the empty string "", since there are no actions for
a BasicPermission.

newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing BasicPermission
objects.

BasicPermission objects must be stored in a manner that allows them
to be inserted in any order, but that also enables the
PermissionCollection

implies

method
to be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for
storing BasicPermissions.

---

#### newPermissionCollection

public

PermissionCollection

newPermissionCollection()

Returns a new PermissionCollection object for storing BasicPermission
objects.

BasicPermission objects must be stored in a manner that allows them
to be inserted in any order, but that also enables the
PermissionCollection

implies

method
to be implemented in an efficient (and consistent) manner.

BasicPermission objects must be stored in a manner that allows them
to be inserted in any order, but that also enables the
PermissionCollection

implies

method
to be implemented in an efficient (and consistent) manner.

---

