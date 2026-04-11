# Class ProtectionDomain

**Source:** `java.base\java\security\ProtectionDomain.html`

### Class Description

```java
public class
ProtectionDomain

extends
Object
```

The ProtectionDomain class encapsulates the characteristics of a domain,
which encloses a set of classes whose instances are granted a set
of permissions when being executed on behalf of a given set of Principals.

A static set of permissions can be bound to a ProtectionDomain when it is
constructed; such permissions are granted to the domain regardless of the
Policy in force. However, to support dynamic security policies, a
ProtectionDomain can also be constructed such that it is dynamically
mapped to a set of permissions by the current Policy whenever a permission
is checked.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

#### public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions)

Creates a new ProtectionDomain with the given CodeSource and
Permissions. If the permissions object is not null, then

setReadOnly()

will be called on the passed in
Permissions object.

The permissions granted to this domain are static, i.e.
invoking the

staticPermissionsOnly()

method returns true.
They contain only the ones passed to this constructor and
the current Policy will not be consulted.

**Parameters:**
- codesource

- the codesource associated with this domain
- permissions

- the permissions granted to this domain

---

#### public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions,

ClassLoader
classloader,

Principal
[] principals)

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals. If the
permissions object is not null, then

setReadOnly()

will be called on the passed in Permissions object.

The permissions granted to this domain are dynamic, i.e.
invoking the

staticPermissionsOnly()

method returns false.
They include both the static permissions passed to this constructor,
and any permissions granted to this domain by the current Policy at the
time a permission is checked.

This constructor is typically used by

ClassLoaders

and

DomainCombiners

which delegate to

Policy

to actively associate the permissions granted to
this domain. This constructor affords the
Policy provider the opportunity to augment the supplied
PermissionCollection to reflect policy changes.

**Parameters:**
- codesource

- the CodeSource associated with this domain
- permissions

- the permissions granted to this domain
- classloader

- the ClassLoader associated with this domain
- principals

- the array of Principals associated with this
domain. The contents of the array are copied to protect against
subsequent modification.

**See Also:**
- Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

**Since:**
- 1.4

---

### Method Details

#### public final
CodeSource
getCodeSource()

Returns the CodeSource of this domain.

**Returns:**
- the CodeSource of this domain which may be null.

**Since:**
- 1.2

---

#### public final
ClassLoader
getClassLoader()

Returns the ClassLoader of this domain.

**Returns:**
- the ClassLoader of this domain which may be null.

**Since:**
- 1.4

---

#### public final
Principal
[] getPrincipals()

Returns an array of principals for this domain.

**Returns:**
- a non-null array of principals for this domain.
Returns a new array each time this method is called.

**Since:**
- 1.4

---

#### public final
PermissionCollection
getPermissions()

Returns the static permissions granted to this domain.

**Returns:**
- the static set of permissions for this domain which may be null.

**See Also:**
- Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

---

#### public final boolean staticPermissionsOnly()

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

**Returns:**
- true if this domain contains only static permissions.

**Since:**
- 9

---

#### public boolean implies​(
Permission
perm)

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

The set of permissions evaluated is a function of whether the
ProtectionDomain was constructed with a static set of permissions
or it was bound to a dynamically mapped set of permissions.

If the

staticPermissionsOnly()

method returns
true, then the permission will only be checked against the
PermissionCollection supplied at construction.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

**Parameters:**
- perm

- the Permission object to check.

**Returns:**
- true if

perm

is implied by this ProtectionDomain.

---

#### public
String
toString()

Convert a ProtectionDomain to a String.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class ProtectionDomain

java.lang.Object

- java.security.ProtectionDomain

java.security.ProtectionDomain

```java
public class
ProtectionDomain

extends
Object
```

The ProtectionDomain class encapsulates the characteristics of a domain,
which encloses a set of classes whose instances are granted a set
of permissions when being executed on behalf of a given set of Principals.

A static set of permissions can be bound to a ProtectionDomain when it is
constructed; such permissions are granted to the domain regardless of the
Policy in force. However, to support dynamic security policies, a
ProtectionDomain can also be constructed such that it is dynamically
mapped to a set of permissions by the current Policy whenever a permission
is checked.

**Since:** 1.2

public class

ProtectionDomain

extends

Object

The ProtectionDomain class encapsulates the characteristics of a domain,
which encloses a set of classes whose instances are granted a set
of permissions when being executed on behalf of a given set of Principals.

A static set of permissions can be bound to a ProtectionDomain when it is
constructed; such permissions are granted to the domain regardless of the
Policy in force. However, to support dynamic security policies, a
ProtectionDomain can also be constructed such that it is dynamically
mapped to a set of permissions by the current Policy whenever a permission
is checked.

A static set of permissions can be bound to a ProtectionDomain when it is
constructed; such permissions are granted to the domain regardless of the
Policy in force. However, to support dynamic security policies, a
ProtectionDomain can also be constructed such that it is dynamically
mapped to a set of permissions by the current Policy whenever a permission
is checked.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ProtectionDomain

​(

CodeSource

codesource,

PermissionCollection

permissions)

Creates a new ProtectionDomain with the given CodeSource and
Permissions.

ProtectionDomain

​(

CodeSource

codesource,

PermissionCollection

permissions,

ClassLoader

classloader,

Principal

[] principals)

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ClassLoader

getClassLoader

()

Returns the ClassLoader of this domain.

CodeSource

getCodeSource

()

Returns the CodeSource of this domain.

PermissionCollection

getPermissions

()

Returns the static permissions granted to this domain.

Principal

[]

getPrincipals

()

Returns an array of principals for this domain.

boolean

implies

​(

Permission

perm)

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

boolean

staticPermissionsOnly

()

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

String

toString

()

Convert a ProtectionDomain to a String.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ProtectionDomain

​(

CodeSource

codesource,

PermissionCollection

permissions)

Creates a new ProtectionDomain with the given CodeSource and
Permissions.

ProtectionDomain

​(

CodeSource

codesource,

PermissionCollection

permissions,

ClassLoader

classloader,

Principal

[] principals)

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals.

---

#### Constructor Summary

Creates a new ProtectionDomain with the given CodeSource and
Permissions.

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ClassLoader

getClassLoader

()

Returns the ClassLoader of this domain.

CodeSource

getCodeSource

()

Returns the CodeSource of this domain.

PermissionCollection

getPermissions

()

Returns the static permissions granted to this domain.

Principal

[]

getPrincipals

()

Returns an array of principals for this domain.

boolean

implies

​(

Permission

perm)

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

boolean

staticPermissionsOnly

()

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

String

toString

()

Convert a ProtectionDomain to a String.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the ClassLoader of this domain.

Returns the CodeSource of this domain.

Returns the static permissions granted to this domain.

Returns an array of principals for this domain.

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

Convert a ProtectionDomain to a String.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ProtectionDomain

```java
public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions)
```

Creates a new ProtectionDomain with the given CodeSource and
Permissions. If the permissions object is not null, then

setReadOnly()

will be called on the passed in
Permissions object.

The permissions granted to this domain are static, i.e.
invoking the

staticPermissionsOnly()

method returns true.
They contain only the ones passed to this constructor and
the current Policy will not be consulted.

**Parameters:** codesource

- the codesource associated with this domain
**Parameters:** permissions

- the permissions granted to this domain

- ProtectionDomain

```java
public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions,

ClassLoader
classloader,

Principal
[] principals)
```

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals. If the
permissions object is not null, then

setReadOnly()

will be called on the passed in Permissions object.

The permissions granted to this domain are dynamic, i.e.
invoking the

staticPermissionsOnly()

method returns false.
They include both the static permissions passed to this constructor,
and any permissions granted to this domain by the current Policy at the
time a permission is checked.

This constructor is typically used by

ClassLoaders

and

DomainCombiners

which delegate to

Policy

to actively associate the permissions granted to
this domain. This constructor affords the
Policy provider the opportunity to augment the supplied
PermissionCollection to reflect policy changes.

**Parameters:** codesource

- the CodeSource associated with this domain
**Parameters:** permissions

- the permissions granted to this domain
**Parameters:** classloader

- the ClassLoader associated with this domain
**Parameters:** principals

- the array of Principals associated with this
domain. The contents of the array are copied to protect against
subsequent modification.
**Since:** 1.4
**See Also:** Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

============ METHOD DETAIL ==========

- Method Detail

- getCodeSource

```java
public final
CodeSource
getCodeSource()
```

Returns the CodeSource of this domain.

**Returns:** the CodeSource of this domain which may be null.
**Since:** 1.2

- getClassLoader

```java
public final
ClassLoader
getClassLoader()
```

Returns the ClassLoader of this domain.

**Returns:** the ClassLoader of this domain which may be null.
**Since:** 1.4

- getPrincipals

```java
public final
Principal
[] getPrincipals()
```

Returns an array of principals for this domain.

**Returns:** a non-null array of principals for this domain.
Returns a new array each time this method is called.
**Since:** 1.4

- getPermissions

```java
public final
PermissionCollection
getPermissions()
```

Returns the static permissions granted to this domain.

**Returns:** the static set of permissions for this domain which may be null.
**See Also:** Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

- staticPermissionsOnly

```java
public final boolean staticPermissionsOnly()
```

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

**Returns:** true if this domain contains only static permissions.
**Since:** 9

- implies

```java
public boolean implies​(
Permission
perm)
```

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

The set of permissions evaluated is a function of whether the
ProtectionDomain was constructed with a static set of permissions
or it was bound to a dynamically mapped set of permissions.

If the

staticPermissionsOnly()

method returns
true, then the permission will only be checked against the
PermissionCollection supplied at construction.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

**Parameters:** perm

- the Permission object to check.
**Returns:** true if

perm

is implied by this ProtectionDomain.

- toString

```java
public
String
toString()
```

Convert a ProtectionDomain to a String.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- ProtectionDomain

```java
public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions)
```

Creates a new ProtectionDomain with the given CodeSource and
Permissions. If the permissions object is not null, then

setReadOnly()

will be called on the passed in
Permissions object.

The permissions granted to this domain are static, i.e.
invoking the

staticPermissionsOnly()

method returns true.
They contain only the ones passed to this constructor and
the current Policy will not be consulted.

**Parameters:** codesource

- the codesource associated with this domain
**Parameters:** permissions

- the permissions granted to this domain

- ProtectionDomain

```java
public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions,

ClassLoader
classloader,

Principal
[] principals)
```

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals. If the
permissions object is not null, then

setReadOnly()

will be called on the passed in Permissions object.

The permissions granted to this domain are dynamic, i.e.
invoking the

staticPermissionsOnly()

method returns false.
They include both the static permissions passed to this constructor,
and any permissions granted to this domain by the current Policy at the
time a permission is checked.

This constructor is typically used by

ClassLoaders

and

DomainCombiners

which delegate to

Policy

to actively associate the permissions granted to
this domain. This constructor affords the
Policy provider the opportunity to augment the supplied
PermissionCollection to reflect policy changes.

**Parameters:** codesource

- the CodeSource associated with this domain
**Parameters:** permissions

- the permissions granted to this domain
**Parameters:** classloader

- the ClassLoader associated with this domain
**Parameters:** principals

- the array of Principals associated with this
domain. The contents of the array are copied to protect against
subsequent modification.
**Since:** 1.4
**See Also:** Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

---

#### Constructor Detail

ProtectionDomain

```java
public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions)
```

Creates a new ProtectionDomain with the given CodeSource and
Permissions. If the permissions object is not null, then

setReadOnly()

will be called on the passed in
Permissions object.

The permissions granted to this domain are static, i.e.
invoking the

staticPermissionsOnly()

method returns true.
They contain only the ones passed to this constructor and
the current Policy will not be consulted.

**Parameters:** codesource

- the codesource associated with this domain
**Parameters:** permissions

- the permissions granted to this domain

---

#### ProtectionDomain

public ProtectionDomain​(

CodeSource

codesource,

PermissionCollection

permissions)

Creates a new ProtectionDomain with the given CodeSource and
Permissions. If the permissions object is not null, then

setReadOnly()

will be called on the passed in
Permissions object.

The permissions granted to this domain are static, i.e.
invoking the

staticPermissionsOnly()

method returns true.
They contain only the ones passed to this constructor and
the current Policy will not be consulted.

The permissions granted to this domain are static, i.e.
invoking the

staticPermissionsOnly()

method returns true.
They contain only the ones passed to this constructor and
the current Policy will not be consulted.

ProtectionDomain

```java
public ProtectionDomain​(
CodeSource
codesource,

PermissionCollection
permissions,

ClassLoader
classloader,

Principal
[] principals)
```

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals. If the
permissions object is not null, then

setReadOnly()

will be called on the passed in Permissions object.

The permissions granted to this domain are dynamic, i.e.
invoking the

staticPermissionsOnly()

method returns false.
They include both the static permissions passed to this constructor,
and any permissions granted to this domain by the current Policy at the
time a permission is checked.

This constructor is typically used by

ClassLoaders

and

DomainCombiners

which delegate to

Policy

to actively associate the permissions granted to
this domain. This constructor affords the
Policy provider the opportunity to augment the supplied
PermissionCollection to reflect policy changes.

**Parameters:** codesource

- the CodeSource associated with this domain
**Parameters:** permissions

- the permissions granted to this domain
**Parameters:** classloader

- the ClassLoader associated with this domain
**Parameters:** principals

- the array of Principals associated with this
domain. The contents of the array are copied to protect against
subsequent modification.
**Since:** 1.4
**See Also:** Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

---

#### ProtectionDomain

public ProtectionDomain​(

CodeSource

codesource,

PermissionCollection

permissions,

ClassLoader

classloader,

Principal

[] principals)

Creates a new ProtectionDomain qualified by the given CodeSource,
Permissions, ClassLoader and array of Principals. If the
permissions object is not null, then

setReadOnly()

will be called on the passed in Permissions object.

The permissions granted to this domain are dynamic, i.e.
invoking the

staticPermissionsOnly()

method returns false.
They include both the static permissions passed to this constructor,
and any permissions granted to this domain by the current Policy at the
time a permission is checked.

This constructor is typically used by

ClassLoaders

and

DomainCombiners

which delegate to

Policy

to actively associate the permissions granted to
this domain. This constructor affords the
Policy provider the opportunity to augment the supplied
PermissionCollection to reflect policy changes.

The permissions granted to this domain are dynamic, i.e.
invoking the

staticPermissionsOnly()

method returns false.
They include both the static permissions passed to this constructor,
and any permissions granted to this domain by the current Policy at the
time a permission is checked.

This constructor is typically used by

ClassLoaders

and

DomainCombiners

which delegate to

Policy

to actively associate the permissions granted to
this domain. This constructor affords the
Policy provider the opportunity to augment the supplied
PermissionCollection to reflect policy changes.

This constructor is typically used by

ClassLoaders

and

DomainCombiners

which delegate to

Policy

to actively associate the permissions granted to
this domain. This constructor affords the
Policy provider the opportunity to augment the supplied
PermissionCollection to reflect policy changes.

Method Detail

- getCodeSource

```java
public final
CodeSource
getCodeSource()
```

Returns the CodeSource of this domain.

**Returns:** the CodeSource of this domain which may be null.
**Since:** 1.2

- getClassLoader

```java
public final
ClassLoader
getClassLoader()
```

Returns the ClassLoader of this domain.

**Returns:** the ClassLoader of this domain which may be null.
**Since:** 1.4

- getPrincipals

```java
public final
Principal
[] getPrincipals()
```

Returns an array of principals for this domain.

**Returns:** a non-null array of principals for this domain.
Returns a new array each time this method is called.
**Since:** 1.4

- getPermissions

```java
public final
PermissionCollection
getPermissions()
```

Returns the static permissions granted to this domain.

**Returns:** the static set of permissions for this domain which may be null.
**See Also:** Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

- staticPermissionsOnly

```java
public final boolean staticPermissionsOnly()
```

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

**Returns:** true if this domain contains only static permissions.
**Since:** 9

- implies

```java
public boolean implies​(
Permission
perm)
```

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

The set of permissions evaluated is a function of whether the
ProtectionDomain was constructed with a static set of permissions
or it was bound to a dynamically mapped set of permissions.

If the

staticPermissionsOnly()

method returns
true, then the permission will only be checked against the
PermissionCollection supplied at construction.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

**Parameters:** perm

- the Permission object to check.
**Returns:** true if

perm

is implied by this ProtectionDomain.

- toString

```java
public
String
toString()
```

Convert a ProtectionDomain to a String.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getCodeSource

```java
public final
CodeSource
getCodeSource()
```

Returns the CodeSource of this domain.

**Returns:** the CodeSource of this domain which may be null.
**Since:** 1.2

---

#### getCodeSource

public final

CodeSource

getCodeSource()

Returns the CodeSource of this domain.

getClassLoader

```java
public final
ClassLoader
getClassLoader()
```

Returns the ClassLoader of this domain.

**Returns:** the ClassLoader of this domain which may be null.
**Since:** 1.4

---

#### getClassLoader

public final

ClassLoader

getClassLoader()

Returns the ClassLoader of this domain.

getPrincipals

```java
public final
Principal
[] getPrincipals()
```

Returns an array of principals for this domain.

**Returns:** a non-null array of principals for this domain.
Returns a new array each time this method is called.
**Since:** 1.4

---

#### getPrincipals

public final

Principal

[] getPrincipals()

Returns an array of principals for this domain.

getPermissions

```java
public final
PermissionCollection
getPermissions()
```

Returns the static permissions granted to this domain.

**Returns:** the static set of permissions for this domain which may be null.
**See Also:** Policy.refresh()

,

Policy.getPermissions(ProtectionDomain)

---

#### getPermissions

public final

PermissionCollection

getPermissions()

Returns the static permissions granted to this domain.

staticPermissionsOnly

```java
public final boolean staticPermissionsOnly()
```

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

**Returns:** true if this domain contains only static permissions.
**Since:** 9

---

#### staticPermissionsOnly

public final boolean staticPermissionsOnly()

Returns true if this domain contains only static permissions
and does not check the current

Policy

at the time of
permission checking.

implies

```java
public boolean implies​(
Permission
perm)
```

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

The set of permissions evaluated is a function of whether the
ProtectionDomain was constructed with a static set of permissions
or it was bound to a dynamically mapped set of permissions.

If the

staticPermissionsOnly()

method returns
true, then the permission will only be checked against the
PermissionCollection supplied at construction.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

**Parameters:** perm

- the Permission object to check.
**Returns:** true if

perm

is implied by this ProtectionDomain.

---

#### implies

public boolean implies​(

Permission

perm)

Check and see if this ProtectionDomain implies the permissions
expressed in the Permission object.

The set of permissions evaluated is a function of whether the
ProtectionDomain was constructed with a static set of permissions
or it was bound to a dynamically mapped set of permissions.

If the

staticPermissionsOnly()

method returns
true, then the permission will only be checked against the
PermissionCollection supplied at construction.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

The set of permissions evaluated is a function of whether the
ProtectionDomain was constructed with a static set of permissions
or it was bound to a dynamically mapped set of permissions.

If the

staticPermissionsOnly()

method returns
true, then the permission will only be checked against the
PermissionCollection supplied at construction.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

If the

staticPermissionsOnly()

method returns
true, then the permission will only be checked against the
PermissionCollection supplied at construction.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

Otherwise, the permission will be checked against the combination
of the PermissionCollection supplied at construction and
the current Policy binding.

toString

```java
public
String
toString()
```

Convert a ProtectionDomain to a String.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Convert a ProtectionDomain to a String.

---

