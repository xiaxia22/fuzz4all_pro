# Interface AclEntry

**Source:** `java.base\java\security\acl\AclEntry.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AclEntry

extends
Cloneable
```

This is the interface used for representing one entry in an Access
Control List (ACL).

An ACL can be thought of as a data structure with multiple ACL entry
objects. Each ACL entry object contains a set of permissions associated
with a particular principal. (A principal represents an entity such as
an individual user or a group). Additionally, each ACL entry is specified
as being either positive or negative. If positive, the permissions are
to be granted to the associated principal. If negative, the permissions
are to be denied. Each principal can have at most one positive ACL entry
and one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if the

setNegativePermissions

method is called on it.

**All Superinterfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean setPrincipal​(
Principal
user)

Specifies the principal for which permissions are granted or denied
by this ACL entry. If a principal was already set for this ACL entry,
false is returned, otherwise true is returned.

**Parameters:**
- user

- the principal to be set for this entry.

**Returns:**
- true if the principal is set, false if there was
already a principal set for this entry.

**See Also:**
- getPrincipal()

---

#### Principal
getPrincipal()

Returns the principal for which permissions are granted or denied by
this ACL entry. Returns null if there is no principal set for this
entry yet.

**Returns:**
- the principal associated with this entry.

**See Also:**
- setPrincipal(java.security.Principal)

---

#### void setNegativePermissions()

Sets this ACL entry to be a negative one. That is, the associated
principal (e.g., a user or a group) will be denied the permission set
specified in the entry.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if this

setNegativePermissions

method is called on it.

---

#### boolean isNegative()

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

**Returns:**
- true if this is a negative ACL entry, false if it's not.

---

#### boolean addPermission​(
Permission
permission)

Adds the specified permission to this ACL entry. Note: An entry can
have multiple permissions.

**Parameters:**
- permission

- the permission to be associated with
the principal in this entry.

**Returns:**
- true if the permission was added, false if the
permission was already part of this entry's permission set.

---

#### boolean removePermission​(
Permission
permission)

Removes the specified permission from this ACL entry.

**Parameters:**
- permission

- the permission to be removed from this entry.

**Returns:**
- true if the permission is removed, false if the
permission was not part of this entry's permission set.

---

#### boolean checkPermission​(
Permission
permission)

Checks if the specified permission is part of the
permission set in this entry.

**Parameters:**
- permission

- the permission to be checked for.

**Returns:**
- true if the permission is part of the
permission set in this entry, false otherwise.

---

#### Enumeration
<
Permission
> permissions()

Returns an enumeration of the permissions in this ACL entry.

**Returns:**
- an enumeration of the permissions in this ACL entry.

---

#### String
toString()

Returns a string representation of the contents of this ACL entry.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the contents.

---

#### Object
clone()

Clones this ACL entry.

**Returns:**
- a clone of this ACL entry.

---

### Additional Sections

#### Interface AclEntry

**All Superinterfaces:** Cloneable

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AclEntry

extends
Cloneable
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is deprecated and subject to removal in a future
version of Java SE. It has been replaced by

java.security.Policy

and related classes since 1.2.

This is the interface used for representing one entry in an Access
Control List (ACL).

An ACL can be thought of as a data structure with multiple ACL entry
objects. Each ACL entry object contains a set of permissions associated
with a particular principal. (A principal represents an entity such as
an individual user or a group). Additionally, each ACL entry is specified
as being either positive or negative. If positive, the permissions are
to be granted to the associated principal. If negative, the permissions
are to be denied. Each principal can have at most one positive ACL entry
and one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if the

setNegativePermissions

method is called on it.

**Since:** 1.1
**See Also:** Acl

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

AclEntry

extends

Cloneable

This is the interface used for representing one entry in an Access
Control List (ACL).

An ACL can be thought of as a data structure with multiple ACL entry
objects. Each ACL entry object contains a set of permissions associated
with a particular principal. (A principal represents an entity such as
an individual user or a group). Additionally, each ACL entry is specified
as being either positive or negative. If positive, the permissions are
to be granted to the associated principal. If negative, the permissions
are to be denied. Each principal can have at most one positive ACL entry
and one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if the

setNegativePermissions

method is called on it.

An ACL can be thought of as a data structure with multiple ACL entry
objects. Each ACL entry object contains a set of permissions associated
with a particular principal. (A principal represents an entity such as
an individual user or a group). Additionally, each ACL entry is specified
as being either positive or negative. If positive, the permissions are
to be granted to the associated principal. If negative, the permissions
are to be denied. Each principal can have at most one positive ACL entry
and one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if the

setNegativePermissions

method is called on it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

addPermission

​(

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified permission to this ACL entry.

boolean

checkPermission

​(

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Checks if the specified permission is part of the
permission set in this entry.

Object

clone

()

Deprecated, for removal: This API element is subject to removal in a future version.

Clones this ACL entry.

Principal

getPrincipal

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal for which permissions are granted or denied by
this ACL entry.

boolean

isNegative

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

Enumeration

<

Permission

>

permissions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the permissions in this ACL entry.

boolean

removePermission

​(

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified permission from this ACL entry.

void

setNegativePermissions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this ACL entry to be a negative one.

boolean

setPrincipal

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies the principal for which permissions are granted or denied
by this ACL entry.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the contents of this ACL entry.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

addPermission

​(

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified permission to this ACL entry.

boolean

checkPermission

​(

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Checks if the specified permission is part of the
permission set in this entry.

Object

clone

()

Deprecated, for removal: This API element is subject to removal in a future version.

Clones this ACL entry.

Principal

getPrincipal

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal for which permissions are granted or denied by
this ACL entry.

boolean

isNegative

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

Enumeration

<

Permission

>

permissions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the permissions in this ACL entry.

boolean

removePermission

​(

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified permission from this ACL entry.

void

setNegativePermissions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this ACL entry to be a negative one.

boolean

setPrincipal

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies the principal for which permissions are granted or denied
by this ACL entry.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the contents of this ACL entry.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified permission to this ACL entry.

Checks if the specified permission is part of the
permission set in this entry.

Clones this ACL entry.

Returns the principal for which permissions are granted or denied by
this ACL entry.

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

Returns an enumeration of the permissions in this ACL entry.

Removes the specified permission from this ACL entry.

Sets this ACL entry to be a negative one.

Specifies the principal for which permissions are granted or denied
by this ACL entry.

Returns a string representation of the contents of this ACL entry.

============ METHOD DETAIL ==========

- Method Detail

- setPrincipal

```java
boolean setPrincipal​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies the principal for which permissions are granted or denied
by this ACL entry. If a principal was already set for this ACL entry,
false is returned, otherwise true is returned.

**Parameters:** user

- the principal to be set for this entry.
**Returns:** true if the principal is set, false if there was
already a principal set for this entry.
**See Also:** getPrincipal()

- getPrincipal

```java
Principal
getPrincipal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal for which permissions are granted or denied by
this ACL entry. Returns null if there is no principal set for this
entry yet.

**Returns:** the principal associated with this entry.
**See Also:** setPrincipal(java.security.Principal)

- setNegativePermissions

```java
void setNegativePermissions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this ACL entry to be a negative one. That is, the associated
principal (e.g., a user or a group) will be denied the permission set
specified in the entry.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if this

setNegativePermissions

method is called on it.

- isNegative

```java
boolean isNegative()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

**Returns:** true if this is a negative ACL entry, false if it's not.

- addPermission

```java
boolean addPermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified permission to this ACL entry. Note: An entry can
have multiple permissions.

**Parameters:** permission

- the permission to be associated with
the principal in this entry.
**Returns:** true if the permission was added, false if the
permission was already part of this entry's permission set.

- removePermission

```java
boolean removePermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified permission from this ACL entry.

**Parameters:** permission

- the permission to be removed from this entry.
**Returns:** true if the permission is removed, false if the
permission was not part of this entry's permission set.

- checkPermission

```java
boolean checkPermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checks if the specified permission is part of the
permission set in this entry.

**Parameters:** permission

- the permission to be checked for.
**Returns:** true if the permission is part of the
permission set in this entry, false otherwise.

- permissions

```java
Enumeration
<
Permission
> permissions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the permissions in this ACL entry.

**Returns:** an enumeration of the permissions in this ACL entry.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the contents of this ACL entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the contents.

- clone

```java
Object
clone()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Clones this ACL entry.

**Returns:** a clone of this ACL entry.

Method Detail

- setPrincipal

```java
boolean setPrincipal​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies the principal for which permissions are granted or denied
by this ACL entry. If a principal was already set for this ACL entry,
false is returned, otherwise true is returned.

**Parameters:** user

- the principal to be set for this entry.
**Returns:** true if the principal is set, false if there was
already a principal set for this entry.
**See Also:** getPrincipal()

- getPrincipal

```java
Principal
getPrincipal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal for which permissions are granted or denied by
this ACL entry. Returns null if there is no principal set for this
entry yet.

**Returns:** the principal associated with this entry.
**See Also:** setPrincipal(java.security.Principal)

- setNegativePermissions

```java
void setNegativePermissions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this ACL entry to be a negative one. That is, the associated
principal (e.g., a user or a group) will be denied the permission set
specified in the entry.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if this

setNegativePermissions

method is called on it.

- isNegative

```java
boolean isNegative()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

**Returns:** true if this is a negative ACL entry, false if it's not.

- addPermission

```java
boolean addPermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified permission to this ACL entry. Note: An entry can
have multiple permissions.

**Parameters:** permission

- the permission to be associated with
the principal in this entry.
**Returns:** true if the permission was added, false if the
permission was already part of this entry's permission set.

- removePermission

```java
boolean removePermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified permission from this ACL entry.

**Parameters:** permission

- the permission to be removed from this entry.
**Returns:** true if the permission is removed, false if the
permission was not part of this entry's permission set.

- checkPermission

```java
boolean checkPermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checks if the specified permission is part of the
permission set in this entry.

**Parameters:** permission

- the permission to be checked for.
**Returns:** true if the permission is part of the
permission set in this entry, false otherwise.

- permissions

```java
Enumeration
<
Permission
> permissions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the permissions in this ACL entry.

**Returns:** an enumeration of the permissions in this ACL entry.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the contents of this ACL entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the contents.

- clone

```java
Object
clone()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Clones this ACL entry.

**Returns:** a clone of this ACL entry.

---

#### Method Detail

setPrincipal

```java
boolean setPrincipal​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies the principal for which permissions are granted or denied
by this ACL entry. If a principal was already set for this ACL entry,
false is returned, otherwise true is returned.

**Parameters:** user

- the principal to be set for this entry.
**Returns:** true if the principal is set, false if there was
already a principal set for this entry.
**See Also:** getPrincipal()

---

#### setPrincipal

boolean setPrincipal​(

Principal

user)

Specifies the principal for which permissions are granted or denied
by this ACL entry. If a principal was already set for this ACL entry,
false is returned, otherwise true is returned.

getPrincipal

```java
Principal
getPrincipal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal for which permissions are granted or denied by
this ACL entry. Returns null if there is no principal set for this
entry yet.

**Returns:** the principal associated with this entry.
**See Also:** setPrincipal(java.security.Principal)

---

#### getPrincipal

Principal

getPrincipal()

Returns the principal for which permissions are granted or denied by
this ACL entry. Returns null if there is no principal set for this
entry yet.

setNegativePermissions

```java
void setNegativePermissions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this ACL entry to be a negative one. That is, the associated
principal (e.g., a user or a group) will be denied the permission set
specified in the entry.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if this

setNegativePermissions

method is called on it.

---

#### setNegativePermissions

void setNegativePermissions()

Sets this ACL entry to be a negative one. That is, the associated
principal (e.g., a user or a group) will be denied the permission set
specified in the entry.

Note: ACL entries are by default positive. An entry becomes a
negative entry only if this

setNegativePermissions

method is called on it.

isNegative

```java
boolean isNegative()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

**Returns:** true if this is a negative ACL entry, false if it's not.

---

#### isNegative

boolean isNegative()

Returns true if this is a negative ACL entry (one denying the
associated principal the set of permissions in the entry), false
otherwise.

addPermission

```java
boolean addPermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified permission to this ACL entry. Note: An entry can
have multiple permissions.

**Parameters:** permission

- the permission to be associated with
the principal in this entry.
**Returns:** true if the permission was added, false if the
permission was already part of this entry's permission set.

---

#### addPermission

boolean addPermission​(

Permission

permission)

Adds the specified permission to this ACL entry. Note: An entry can
have multiple permissions.

removePermission

```java
boolean removePermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified permission from this ACL entry.

**Parameters:** permission

- the permission to be removed from this entry.
**Returns:** true if the permission is removed, false if the
permission was not part of this entry's permission set.

---

#### removePermission

boolean removePermission​(

Permission

permission)

Removes the specified permission from this ACL entry.

checkPermission

```java
boolean checkPermission​(
Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checks if the specified permission is part of the
permission set in this entry.

**Parameters:** permission

- the permission to be checked for.
**Returns:** true if the permission is part of the
permission set in this entry, false otherwise.

---

#### checkPermission

boolean checkPermission​(

Permission

permission)

Checks if the specified permission is part of the
permission set in this entry.

permissions

```java
Enumeration
<
Permission
> permissions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the permissions in this ACL entry.

**Returns:** an enumeration of the permissions in this ACL entry.

---

#### permissions

Enumeration

<

Permission

> permissions()

Returns an enumeration of the permissions in this ACL entry.

toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the contents of this ACL entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the contents.

---

#### toString

String

toString()

Returns a string representation of the contents of this ACL entry.

clone

```java
Object
clone()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Clones this ACL entry.

**Returns:** a clone of this ACL entry.

---

#### clone

Object

clone()

Clones this ACL entry.

---

