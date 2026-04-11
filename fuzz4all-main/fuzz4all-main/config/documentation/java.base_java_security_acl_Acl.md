# Interface Acl

**Source:** `java.base\java\security\acl\Acl.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Acl

extends
Owner
```

Interface representing an Access Control List (ACL). An Access
Control List is a data structure used to guard access to
resources.

An ACL can be thought of as a data structure with multiple ACL
entries. Each ACL entry, of interface type AclEntry, contains a
set of permissions associated with a particular principal. (A
principal represents an entity such as an individual user or a
group). Additionally, each ACL entry is specified as being either
positive or negative. If positive, the permissions are to be
granted to the associated principal. If negative, the permissions
are to be denied.

The ACL Entries in each ACL observe the following rules:

- Each principal can have at most one positive ACL entry and
one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal. Each entry specifies
the set of permissions that are to be granted (if positive) or
denied (if negative).

If there is no entry for a particular principal, then the
principal is considered to have a null (empty) permission set.

If there is a positive entry that grants a principal a
particular permission, and a negative entry that denies the
principal the same permission, the result is as though the
permission was never granted or denied.

Individual permissions always override permissions of the
group(s) to which the individual belongs. That is, individual
negative permissions (specific denial of permissions) override the
groups' positive permissions. And individual positive permissions
override the groups' negative permissions.

The

java.security.acl

package provides the
interfaces to the ACL and related data structures (ACL entries,
groups, permissions, etc.).

The

java.security.acl.Acl

interface extends the

java.security.acl.Owner

interface. The Owner
interface is used to maintain a list of owners for each ACL. Only
owners are allowed to modify an ACL. For example, only an owner can
call the ACL's

addEntry

method to add a new ACL entry
to the ACL.

**All Superinterfaces:** Owner

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setName​(
Principal
caller,

String
name)
throws
NotOwnerException

Sets the name of this ACL.

**Parameters:**
- caller

- the principal invoking this method. It must be an
owner of this ACL.
- name

- the name to be given to this ACL.

**Throws:**
- NotOwnerException

- if the caller principal
is not an owner of this ACL.

**See Also:**
- getName()

---

#### String
getName()

Returns the name of this ACL.

**Returns:**
- the name of this ACL.

**See Also:**
- setName(java.security.Principal, java.lang.String)

---

#### boolean addEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException

Adds an ACL entry to this ACL. An entry associates a principal
(e.g., an individual or a group) with a set of
permissions. Each principal can have at most one positive ACL
entry (specifying permissions to be granted to the principal)
and one negative ACL entry (specifying permissions to be
denied). If there is already an ACL entry of the same type
(negative or positive) already in the ACL, false is returned.

**Parameters:**
- caller

- the principal invoking this method. It must be an
owner of this ACL.
- entry

- the ACL entry to be added to this ACL.

**Returns:**
- true on success, false if an entry of the same type
(positive or negative) for the same principal is already
present in this ACL.

**Throws:**
- NotOwnerException

- if the caller principal
is not an owner of this ACL.

---

#### boolean removeEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException

Removes an ACL entry from this ACL.

**Parameters:**
- caller

- the principal invoking this method. It must be an
owner of this ACL.
- entry

- the ACL entry to be removed from this ACL.

**Returns:**
- true on success, false if the entry is not part of this ACL.

**Throws:**
- NotOwnerException

- if the caller principal is not
an owner of this Acl.

---

#### Enumeration
<
Permission
> getPermissions​(
Principal
user)

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group). This set of allowed permissions is calculated as
follows:

- If there is no entry in this Access Control List for the
specified principal, an empty permission set is returned.

Otherwise, the principal's group permission sets are determined.
(A principal can belong to one or more groups, where a group is a
group of principals, represented by the Group interface.)
The group positive permission set is the union of all
the positive permissions of each group that the principal belongs to.
The group negative permission set is the union of all
the negative permissions of each group that the principal belongs to.
If there is a specific permission that occurs in both
the positive permission set and the negative permission set,
it is removed from both.

The individual positive and negative permission sets are also
determined. The positive permission set contains the permissions
specified in the positive ACL entry (if any) for the principal.
Similarly, the negative permission set contains the permissions
specified in the negative ACL entry (if any) for the principal.
The individual positive (or negative) permission set is considered
to be null if there is not a positive (negative) ACL entry for the
principal in this ACL.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

**Parameters:**
- user

- the principal whose permission set is to be returned.

**Returns:**
- the permission set specifying the permissions the principal
is allowed.

---

#### Enumeration
<
AclEntry
> entries()

Returns an enumeration of the entries in this ACL. Each element in
the enumeration is of type AclEntry.

**Returns:**
- an enumeration of the entries in this ACL.

---

#### boolean checkPermission​(
Principal
principal,

Permission
permission)

Checks whether or not the specified principal has the specified
permission. If it does, true is returned, otherwise false is returned.

More specifically, this method checks whether the passed permission
is a member of the allowed permission set of the specified principal.
The allowed permission set is determined by the same algorithm as is
used by the

getPermissions

method.

**Parameters:**
- principal

- the principal, assumed to be a valid authenticated
Principal.
- permission

- the permission to be checked for.

**Returns:**
- true if the principal has the specified permission, false
otherwise.

**See Also:**
- getPermissions(java.security.Principal)

---

#### String
toString()

Returns a string representation of the
ACL contents.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the ACL contents.

---

### Additional Sections

#### Interface Acl

**All Superinterfaces:** Owner

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Acl

extends
Owner
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is deprecated and subject to removal in a future
version of Java SE. It has been replaced by

java.security.Policy

and related classes since 1.2.

Interface representing an Access Control List (ACL). An Access
Control List is a data structure used to guard access to
resources.

An ACL can be thought of as a data structure with multiple ACL
entries. Each ACL entry, of interface type AclEntry, contains a
set of permissions associated with a particular principal. (A
principal represents an entity such as an individual user or a
group). Additionally, each ACL entry is specified as being either
positive or negative. If positive, the permissions are to be
granted to the associated principal. If negative, the permissions
are to be denied.

The ACL Entries in each ACL observe the following rules:

- Each principal can have at most one positive ACL entry and
one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal. Each entry specifies
the set of permissions that are to be granted (if positive) or
denied (if negative).

If there is no entry for a particular principal, then the
principal is considered to have a null (empty) permission set.

If there is a positive entry that grants a principal a
particular permission, and a negative entry that denies the
principal the same permission, the result is as though the
permission was never granted or denied.

Individual permissions always override permissions of the
group(s) to which the individual belongs. That is, individual
negative permissions (specific denial of permissions) override the
groups' positive permissions. And individual positive permissions
override the groups' negative permissions.

The

java.security.acl

package provides the
interfaces to the ACL and related data structures (ACL entries,
groups, permissions, etc.).

The

java.security.acl.Acl

interface extends the

java.security.acl.Owner

interface. The Owner
interface is used to maintain a list of owners for each ACL. Only
owners are allowed to modify an ACL. For example, only an owner can
call the ACL's

addEntry

method to add a new ACL entry
to the ACL.

**Since:** 1.1
**See Also:** AclEntry

,

Owner

,

getPermissions(java.security.Principal)

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Acl

extends

Owner

Interface representing an Access Control List (ACL). An Access
Control List is a data structure used to guard access to
resources.

An ACL can be thought of as a data structure with multiple ACL
entries. Each ACL entry, of interface type AclEntry, contains a
set of permissions associated with a particular principal. (A
principal represents an entity such as an individual user or a
group). Additionally, each ACL entry is specified as being either
positive or negative. If positive, the permissions are to be
granted to the associated principal. If negative, the permissions
are to be denied.

The ACL Entries in each ACL observe the following rules:

- Each principal can have at most one positive ACL entry and
one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal. Each entry specifies
the set of permissions that are to be granted (if positive) or
denied (if negative).

If there is no entry for a particular principal, then the
principal is considered to have a null (empty) permission set.

If there is a positive entry that grants a principal a
particular permission, and a negative entry that denies the
principal the same permission, the result is as though the
permission was never granted or denied.

Individual permissions always override permissions of the
group(s) to which the individual belongs. That is, individual
negative permissions (specific denial of permissions) override the
groups' positive permissions. And individual positive permissions
override the groups' negative permissions.

The

java.security.acl

package provides the
interfaces to the ACL and related data structures (ACL entries,
groups, permissions, etc.).

The

java.security.acl.Acl

interface extends the

java.security.acl.Owner

interface. The Owner
interface is used to maintain a list of owners for each ACL. Only
owners are allowed to modify an ACL. For example, only an owner can
call the ACL's

addEntry

method to add a new ACL entry
to the ACL.

An ACL can be thought of as a data structure with multiple ACL
entries. Each ACL entry, of interface type AclEntry, contains a
set of permissions associated with a particular principal. (A
principal represents an entity such as an individual user or a
group). Additionally, each ACL entry is specified as being either
positive or negative. If positive, the permissions are to be
granted to the associated principal. If negative, the permissions
are to be denied.

The ACL Entries in each ACL observe the following rules:

- Each principal can have at most one positive ACL entry and
one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal. Each entry specifies
the set of permissions that are to be granted (if positive) or
denied (if negative).

If there is no entry for a particular principal, then the
principal is considered to have a null (empty) permission set.

If there is a positive entry that grants a principal a
particular permission, and a negative entry that denies the
principal the same permission, the result is as though the
permission was never granted or denied.

Individual permissions always override permissions of the
group(s) to which the individual belongs. That is, individual
negative permissions (specific denial of permissions) override the
groups' positive permissions. And individual positive permissions
override the groups' negative permissions.

The

java.security.acl

package provides the
interfaces to the ACL and related data structures (ACL entries,
groups, permissions, etc.).

The

java.security.acl.Acl

interface extends the

java.security.acl.Owner

interface. The Owner
interface is used to maintain a list of owners for each ACL. Only
owners are allowed to modify an ACL. For example, only an owner can
call the ACL's

addEntry

method to add a new ACL entry
to the ACL.

The ACL Entries in each ACL observe the following rules:

- Each principal can have at most one positive ACL entry and
one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal. Each entry specifies
the set of permissions that are to be granted (if positive) or
denied (if negative).

If there is no entry for a particular principal, then the
principal is considered to have a null (empty) permission set.

If there is a positive entry that grants a principal a
particular permission, and a negative entry that denies the
principal the same permission, the result is as though the
permission was never granted or denied.

Individual permissions always override permissions of the
group(s) to which the individual belongs. That is, individual
negative permissions (specific denial of permissions) override the
groups' positive permissions. And individual positive permissions
override the groups' negative permissions.

The

java.security.acl

package provides the
interfaces to the ACL and related data structures (ACL entries,
groups, permissions, etc.).

The

java.security.acl.Acl

interface extends the

java.security.acl.Owner

interface. The Owner
interface is used to maintain a list of owners for each ACL. Only
owners are allowed to modify an ACL. For example, only an owner can
call the ACL's

addEntry

method to add a new ACL entry
to the ACL.

Each principal can have at most one positive ACL entry and
one negative entry; that is, multiple positive or negative ACL
entries are not allowed for any principal. Each entry specifies
the set of permissions that are to be granted (if positive) or
denied (if negative).

If there is no entry for a particular principal, then the
principal is considered to have a null (empty) permission set.

If there is a positive entry that grants a principal a
particular permission, and a negative entry that denies the
principal the same permission, the result is as though the
permission was never granted or denied.

Individual permissions always override permissions of the
group(s) to which the individual belongs. That is, individual
negative permissions (specific denial of permissions) override the
groups' positive permissions. And individual positive permissions
override the groups' negative permissions.

The

java.security.acl.Acl

interface extends the

java.security.acl.Owner

interface. The Owner
interface is used to maintain a list of owners for each ACL. Only
owners are allowed to modify an ACL. For example, only an owner can
call the ACL's

addEntry

method to add a new ACL entry
to the ACL.

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

addEntry

​(

Principal

caller,

AclEntry

entry)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an ACL entry to this ACL.

boolean

checkPermission

​(

Principal

principal,

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Checks whether or not the specified principal has the specified
permission.

Enumeration

<

AclEntry

>

entries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the entries in this ACL.

String

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this ACL.

Enumeration

<

Permission

>

getPermissions

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group).

boolean

removeEntry

​(

Principal

caller,

AclEntry

entry)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an ACL entry from this ACL.

void

setName

​(

Principal

caller,

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the name of this ACL.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the
ACL contents.

- Methods declared in interface java.security.acl.

Owner

addOwner

,

deleteOwner

,

isOwner

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

addEntry

​(

Principal

caller,

AclEntry

entry)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an ACL entry to this ACL.

boolean

checkPermission

​(

Principal

principal,

Permission

permission)

Deprecated, for removal: This API element is subject to removal in a future version.

Checks whether or not the specified principal has the specified
permission.

Enumeration

<

AclEntry

>

entries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the entries in this ACL.

String

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this ACL.

Enumeration

<

Permission

>

getPermissions

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group).

boolean

removeEntry

​(

Principal

caller,

AclEntry

entry)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an ACL entry from this ACL.

void

setName

​(

Principal

caller,

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the name of this ACL.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the
ACL contents.

- Methods declared in interface java.security.acl.

Owner

addOwner

,

deleteOwner

,

isOwner

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an ACL entry to this ACL.

Checks whether or not the specified principal has the specified
permission.

Returns an enumeration of the entries in this ACL.

Returns the name of this ACL.

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group).

Removes an ACL entry from this ACL.

Sets the name of this ACL.

Returns a string representation of the
ACL contents.

Methods declared in interface java.security.acl.

Owner

addOwner

,

deleteOwner

,

isOwner

---

#### Methods declared in interface java.security.acl. Owner

============ METHOD DETAIL ==========

- Method Detail

- setName

```java
void setName​(
Principal
caller,

String
name)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the name of this ACL.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** name

- the name to be given to this ACL.
**Throws:** NotOwnerException

- if the caller principal
is not an owner of this ACL.
**See Also:** getName()

- getName

```java
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this ACL.

**Returns:** the name of this ACL.
**See Also:** setName(java.security.Principal, java.lang.String)

- addEntry

```java
boolean addEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an ACL entry to this ACL. An entry associates a principal
(e.g., an individual or a group) with a set of
permissions. Each principal can have at most one positive ACL
entry (specifying permissions to be granted to the principal)
and one negative ACL entry (specifying permissions to be
denied). If there is already an ACL entry of the same type
(negative or positive) already in the ACL, false is returned.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** entry

- the ACL entry to be added to this ACL.
**Returns:** true on success, false if an entry of the same type
(positive or negative) for the same principal is already
present in this ACL.
**Throws:** NotOwnerException

- if the caller principal
is not an owner of this ACL.

- removeEntry

```java
boolean removeEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an ACL entry from this ACL.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** entry

- the ACL entry to be removed from this ACL.
**Returns:** true on success, false if the entry is not part of this ACL.
**Throws:** NotOwnerException

- if the caller principal is not
an owner of this Acl.

- getPermissions

```java
Enumeration
<
Permission
> getPermissions​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group). This set of allowed permissions is calculated as
follows:

- If there is no entry in this Access Control List for the
specified principal, an empty permission set is returned.

Otherwise, the principal's group permission sets are determined.
(A principal can belong to one or more groups, where a group is a
group of principals, represented by the Group interface.)
The group positive permission set is the union of all
the positive permissions of each group that the principal belongs to.
The group negative permission set is the union of all
the negative permissions of each group that the principal belongs to.
If there is a specific permission that occurs in both
the positive permission set and the negative permission set,
it is removed from both.

The individual positive and negative permission sets are also
determined. The positive permission set contains the permissions
specified in the positive ACL entry (if any) for the principal.
Similarly, the negative permission set contains the permissions
specified in the negative ACL entry (if any) for the principal.
The individual positive (or negative) permission set is considered
to be null if there is not a positive (negative) ACL entry for the
principal in this ACL.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

**Parameters:** user

- the principal whose permission set is to be returned.
**Returns:** the permission set specifying the permissions the principal
is allowed.

- entries

```java
Enumeration
<
AclEntry
> entries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the entries in this ACL. Each element in
the enumeration is of type AclEntry.

**Returns:** an enumeration of the entries in this ACL.

- checkPermission

```java
boolean checkPermission​(
Principal
principal,

Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checks whether or not the specified principal has the specified
permission. If it does, true is returned, otherwise false is returned.

More specifically, this method checks whether the passed permission
is a member of the allowed permission set of the specified principal.
The allowed permission set is determined by the same algorithm as is
used by the

getPermissions

method.

**Parameters:** principal

- the principal, assumed to be a valid authenticated
Principal.
**Parameters:** permission

- the permission to be checked for.
**Returns:** true if the principal has the specified permission, false
otherwise.
**See Also:** getPermissions(java.security.Principal)

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the
ACL contents.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the ACL contents.

Method Detail

- setName

```java
void setName​(
Principal
caller,

String
name)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the name of this ACL.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** name

- the name to be given to this ACL.
**Throws:** NotOwnerException

- if the caller principal
is not an owner of this ACL.
**See Also:** getName()

- getName

```java
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this ACL.

**Returns:** the name of this ACL.
**See Also:** setName(java.security.Principal, java.lang.String)

- addEntry

```java
boolean addEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an ACL entry to this ACL. An entry associates a principal
(e.g., an individual or a group) with a set of
permissions. Each principal can have at most one positive ACL
entry (specifying permissions to be granted to the principal)
and one negative ACL entry (specifying permissions to be
denied). If there is already an ACL entry of the same type
(negative or positive) already in the ACL, false is returned.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** entry

- the ACL entry to be added to this ACL.
**Returns:** true on success, false if an entry of the same type
(positive or negative) for the same principal is already
present in this ACL.
**Throws:** NotOwnerException

- if the caller principal
is not an owner of this ACL.

- removeEntry

```java
boolean removeEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an ACL entry from this ACL.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** entry

- the ACL entry to be removed from this ACL.
**Returns:** true on success, false if the entry is not part of this ACL.
**Throws:** NotOwnerException

- if the caller principal is not
an owner of this Acl.

- getPermissions

```java
Enumeration
<
Permission
> getPermissions​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group). This set of allowed permissions is calculated as
follows:

- If there is no entry in this Access Control List for the
specified principal, an empty permission set is returned.

Otherwise, the principal's group permission sets are determined.
(A principal can belong to one or more groups, where a group is a
group of principals, represented by the Group interface.)
The group positive permission set is the union of all
the positive permissions of each group that the principal belongs to.
The group negative permission set is the union of all
the negative permissions of each group that the principal belongs to.
If there is a specific permission that occurs in both
the positive permission set and the negative permission set,
it is removed from both.

The individual positive and negative permission sets are also
determined. The positive permission set contains the permissions
specified in the positive ACL entry (if any) for the principal.
Similarly, the negative permission set contains the permissions
specified in the negative ACL entry (if any) for the principal.
The individual positive (or negative) permission set is considered
to be null if there is not a positive (negative) ACL entry for the
principal in this ACL.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

**Parameters:** user

- the principal whose permission set is to be returned.
**Returns:** the permission set specifying the permissions the principal
is allowed.

- entries

```java
Enumeration
<
AclEntry
> entries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the entries in this ACL. Each element in
the enumeration is of type AclEntry.

**Returns:** an enumeration of the entries in this ACL.

- checkPermission

```java
boolean checkPermission​(
Principal
principal,

Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checks whether or not the specified principal has the specified
permission. If it does, true is returned, otherwise false is returned.

More specifically, this method checks whether the passed permission
is a member of the allowed permission set of the specified principal.
The allowed permission set is determined by the same algorithm as is
used by the

getPermissions

method.

**Parameters:** principal

- the principal, assumed to be a valid authenticated
Principal.
**Parameters:** permission

- the permission to be checked for.
**Returns:** true if the principal has the specified permission, false
otherwise.
**See Also:** getPermissions(java.security.Principal)

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the
ACL contents.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the ACL contents.

---

#### Method Detail

setName

```java
void setName​(
Principal
caller,

String
name)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the name of this ACL.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** name

- the name to be given to this ACL.
**Throws:** NotOwnerException

- if the caller principal
is not an owner of this ACL.
**See Also:** getName()

---

#### setName

void setName​(

Principal

caller,

String

name)
throws

NotOwnerException

Sets the name of this ACL.

getName

```java
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this ACL.

**Returns:** the name of this ACL.
**See Also:** setName(java.security.Principal, java.lang.String)

---

#### getName

String

getName()

Returns the name of this ACL.

addEntry

```java
boolean addEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an ACL entry to this ACL. An entry associates a principal
(e.g., an individual or a group) with a set of
permissions. Each principal can have at most one positive ACL
entry (specifying permissions to be granted to the principal)
and one negative ACL entry (specifying permissions to be
denied). If there is already an ACL entry of the same type
(negative or positive) already in the ACL, false is returned.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** entry

- the ACL entry to be added to this ACL.
**Returns:** true on success, false if an entry of the same type
(positive or negative) for the same principal is already
present in this ACL.
**Throws:** NotOwnerException

- if the caller principal
is not an owner of this ACL.

---

#### addEntry

boolean addEntry​(

Principal

caller,

AclEntry

entry)
throws

NotOwnerException

Adds an ACL entry to this ACL. An entry associates a principal
(e.g., an individual or a group) with a set of
permissions. Each principal can have at most one positive ACL
entry (specifying permissions to be granted to the principal)
and one negative ACL entry (specifying permissions to be
denied). If there is already an ACL entry of the same type
(negative or positive) already in the ACL, false is returned.

removeEntry

```java
boolean removeEntry​(
Principal
caller,

AclEntry
entry)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an ACL entry from this ACL.

**Parameters:** caller

- the principal invoking this method. It must be an
owner of this ACL.
**Parameters:** entry

- the ACL entry to be removed from this ACL.
**Returns:** true on success, false if the entry is not part of this ACL.
**Throws:** NotOwnerException

- if the caller principal is not
an owner of this Acl.

---

#### removeEntry

boolean removeEntry​(

Principal

caller,

AclEntry

entry)
throws

NotOwnerException

Removes an ACL entry from this ACL.

getPermissions

```java
Enumeration
<
Permission
> getPermissions​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group). This set of allowed permissions is calculated as
follows:

- If there is no entry in this Access Control List for the
specified principal, an empty permission set is returned.

Otherwise, the principal's group permission sets are determined.
(A principal can belong to one or more groups, where a group is a
group of principals, represented by the Group interface.)
The group positive permission set is the union of all
the positive permissions of each group that the principal belongs to.
The group negative permission set is the union of all
the negative permissions of each group that the principal belongs to.
If there is a specific permission that occurs in both
the positive permission set and the negative permission set,
it is removed from both.

The individual positive and negative permission sets are also
determined. The positive permission set contains the permissions
specified in the positive ACL entry (if any) for the principal.
Similarly, the negative permission set contains the permissions
specified in the negative ACL entry (if any) for the principal.
The individual positive (or negative) permission set is considered
to be null if there is not a positive (negative) ACL entry for the
principal in this ACL.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

**Parameters:** user

- the principal whose permission set is to be returned.
**Returns:** the permission set specifying the permissions the principal
is allowed.

---

#### getPermissions

Enumeration

<

Permission

> getPermissions​(

Principal

user)

Returns an enumeration for the set of allowed permissions for the
specified principal (representing an entity such as an individual or
a group). This set of allowed permissions is calculated as
follows:

- If there is no entry in this Access Control List for the
specified principal, an empty permission set is returned.

Otherwise, the principal's group permission sets are determined.
(A principal can belong to one or more groups, where a group is a
group of principals, represented by the Group interface.)
The group positive permission set is the union of all
the positive permissions of each group that the principal belongs to.
The group negative permission set is the union of all
the negative permissions of each group that the principal belongs to.
If there is a specific permission that occurs in both
the positive permission set and the negative permission set,
it is removed from both.

The individual positive and negative permission sets are also
determined. The positive permission set contains the permissions
specified in the positive ACL entry (if any) for the principal.
Similarly, the negative permission set contains the permissions
specified in the negative ACL entry (if any) for the principal.
The individual positive (or negative) permission set is considered
to be null if there is not a positive (negative) ACL entry for the
principal in this ACL.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

If there is no entry in this Access Control List for the
specified principal, an empty permission set is returned.

Otherwise, the principal's group permission sets are determined.
(A principal can belong to one or more groups, where a group is a
group of principals, represented by the Group interface.)
The group positive permission set is the union of all
the positive permissions of each group that the principal belongs to.
The group negative permission set is the union of all
the negative permissions of each group that the principal belongs to.
If there is a specific permission that occurs in both
the positive permission set and the negative permission set,
it is removed from both.

The individual positive and negative permission sets are also
determined. The positive permission set contains the permissions
specified in the positive ACL entry (if any) for the principal.
Similarly, the negative permission set contains the permissions
specified in the negative ACL entry (if any) for the principal.
The individual positive (or negative) permission set is considered
to be null if there is not a positive (negative) ACL entry for the
principal in this ACL.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

The individual positive and negative permission sets are also
determined. The positive permission set contains the permissions
specified in the positive ACL entry (if any) for the principal.
Similarly, the negative permission set contains the permissions
specified in the negative ACL entry (if any) for the principal.
The individual positive (or negative) permission set is considered
to be null if there is not a positive (negative) ACL entry for the
principal in this ACL.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

The set of permissions granted to the principal is then calculated
using the simple rule that individual permissions always override
the group permissions. That is, the principal's individual negative
permission set (specific denial of permissions) overrides the group
positive permission set, and the principal's individual positive
permission set overrides the group negative permission set.

entries

```java
Enumeration
<
AclEntry
> entries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the entries in this ACL. Each element in
the enumeration is of type AclEntry.

**Returns:** an enumeration of the entries in this ACL.

---

#### entries

Enumeration

<

AclEntry

> entries()

Returns an enumeration of the entries in this ACL. Each element in
the enumeration is of type AclEntry.

checkPermission

```java
boolean checkPermission​(
Principal
principal,

Permission
permission)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checks whether or not the specified principal has the specified
permission. If it does, true is returned, otherwise false is returned.

More specifically, this method checks whether the passed permission
is a member of the allowed permission set of the specified principal.
The allowed permission set is determined by the same algorithm as is
used by the

getPermissions

method.

**Parameters:** principal

- the principal, assumed to be a valid authenticated
Principal.
**Parameters:** permission

- the permission to be checked for.
**Returns:** true if the principal has the specified permission, false
otherwise.
**See Also:** getPermissions(java.security.Principal)

---

#### checkPermission

boolean checkPermission​(

Principal

principal,

Permission

permission)

Checks whether or not the specified principal has the specified
permission. If it does, true is returned, otherwise false is returned.

More specifically, this method checks whether the passed permission
is a member of the allowed permission set of the specified principal.
The allowed permission set is determined by the same algorithm as is
used by the

getPermissions

method.

toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the
ACL contents.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the ACL contents.

---

#### toString

String

toString()

Returns a string representation of the
ACL contents.

---

