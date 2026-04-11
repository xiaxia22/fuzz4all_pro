# Interface Owner

**Source:** `java.base\java\security\acl\Owner.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Owner
```

Interface for managing owners of Access Control Lists (ACLs) or ACL
configurations. (Note that the Acl interface in the

java.security.acl

package extends this Owner
interface.) The initial owner Principal should be specified as an
argument to the constructor of the class implementing this interface.

**All Known Subinterfaces:** Acl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean addOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException

Adds an owner. Only owners can modify ACL contents. The caller
principal must be an owner of the ACL in order to invoke this method.
That is, only an owner can add another owner. The initial owner is
configured at ACL construction time.

**Parameters:**
- caller

- the principal invoking this method. It must be an owner
of the ACL.
- owner

- the owner that should be added to the list of owners.

**Returns:**
- true if successful, false if owner is already an owner.

**Throws:**
- NotOwnerException

- if the caller principal is not an owner
of the ACL.

---

#### boolean deleteOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException
,

LastOwnerException

Deletes an owner. If this is the last owner in the ACL, an exception is
raised.

The caller principal must be an owner of the ACL in order to invoke
this method.

**Parameters:**
- caller

- the principal invoking this method. It must be an owner
of the ACL.
- owner

- the owner to be removed from the list of owners.

**Returns:**
- true if the owner is removed, false if the owner is not part
of the list of owners.

**Throws:**
- NotOwnerException

- if the caller principal is not an owner
of the ACL.
- LastOwnerException

- if there is only one owner left, so that
deleteOwner would leave the ACL owner-less.

---

#### boolean isOwner​(
Principal
owner)

Returns true if the given principal is an owner of the ACL.

**Parameters:**
- owner

- the principal to be checked to determine whether or not
it is an owner.

**Returns:**
- true if the passed principal is in the list of owners, false
if not.

---

### Additional Sections

#### Interface Owner

**All Known Subinterfaces:** Acl

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Owner
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is deprecated and subject to removal in a future
version of Java SE. It has been replaced by

java.security.Policy

and related classes since 1.2.

Interface for managing owners of Access Control Lists (ACLs) or ACL
configurations. (Note that the Acl interface in the

java.security.acl

package extends this Owner
interface.) The initial owner Principal should be specified as an
argument to the constructor of the class implementing this interface.

**Since:** 1.1
**See Also:** Acl

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Owner

Interface for managing owners of Access Control Lists (ACLs) or ACL
configurations. (Note that the Acl interface in the

java.security.acl

package extends this Owner
interface.) The initial owner Principal should be specified as an
argument to the constructor of the class implementing this interface.

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

addOwner

​(

Principal

caller,

Principal

owner)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an owner.

boolean

deleteOwner

​(

Principal

caller,

Principal

owner)

Deprecated, for removal: This API element is subject to removal in a future version.

Deletes an owner.

boolean

isOwner

​(

Principal

owner)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the given principal is an owner of the ACL.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

addOwner

​(

Principal

caller,

Principal

owner)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an owner.

boolean

deleteOwner

​(

Principal

caller,

Principal

owner)

Deprecated, for removal: This API element is subject to removal in a future version.

Deletes an owner.

boolean

isOwner

​(

Principal

owner)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the given principal is an owner of the ACL.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an owner.

Deletes an owner.

Returns true if the given principal is an owner of the ACL.

============ METHOD DETAIL ==========

- Method Detail

- addOwner

```java
boolean addOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an owner. Only owners can modify ACL contents. The caller
principal must be an owner of the ACL in order to invoke this method.
That is, only an owner can add another owner. The initial owner is
configured at ACL construction time.

**Parameters:** caller

- the principal invoking this method. It must be an owner
of the ACL.
**Parameters:** owner

- the owner that should be added to the list of owners.
**Returns:** true if successful, false if owner is already an owner.
**Throws:** NotOwnerException

- if the caller principal is not an owner
of the ACL.

- deleteOwner

```java
boolean deleteOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException
,

LastOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Deletes an owner. If this is the last owner in the ACL, an exception is
raised.

The caller principal must be an owner of the ACL in order to invoke
this method.

**Parameters:** caller

- the principal invoking this method. It must be an owner
of the ACL.
**Parameters:** owner

- the owner to be removed from the list of owners.
**Returns:** true if the owner is removed, false if the owner is not part
of the list of owners.
**Throws:** NotOwnerException

- if the caller principal is not an owner
of the ACL.
**Throws:** LastOwnerException

- if there is only one owner left, so that
deleteOwner would leave the ACL owner-less.

- isOwner

```java
boolean isOwner​(
Principal
owner)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the given principal is an owner of the ACL.

**Parameters:** owner

- the principal to be checked to determine whether or not
it is an owner.
**Returns:** true if the passed principal is in the list of owners, false
if not.

Method Detail

- addOwner

```java
boolean addOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an owner. Only owners can modify ACL contents. The caller
principal must be an owner of the ACL in order to invoke this method.
That is, only an owner can add another owner. The initial owner is
configured at ACL construction time.

**Parameters:** caller

- the principal invoking this method. It must be an owner
of the ACL.
**Parameters:** owner

- the owner that should be added to the list of owners.
**Returns:** true if successful, false if owner is already an owner.
**Throws:** NotOwnerException

- if the caller principal is not an owner
of the ACL.

- deleteOwner

```java
boolean deleteOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException
,

LastOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Deletes an owner. If this is the last owner in the ACL, an exception is
raised.

The caller principal must be an owner of the ACL in order to invoke
this method.

**Parameters:** caller

- the principal invoking this method. It must be an owner
of the ACL.
**Parameters:** owner

- the owner to be removed from the list of owners.
**Returns:** true if the owner is removed, false if the owner is not part
of the list of owners.
**Throws:** NotOwnerException

- if the caller principal is not an owner
of the ACL.
**Throws:** LastOwnerException

- if there is only one owner left, so that
deleteOwner would leave the ACL owner-less.

- isOwner

```java
boolean isOwner​(
Principal
owner)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the given principal is an owner of the ACL.

**Parameters:** owner

- the principal to be checked to determine whether or not
it is an owner.
**Returns:** true if the passed principal is in the list of owners, false
if not.

---

#### Method Detail

addOwner

```java
boolean addOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an owner. Only owners can modify ACL contents. The caller
principal must be an owner of the ACL in order to invoke this method.
That is, only an owner can add another owner. The initial owner is
configured at ACL construction time.

**Parameters:** caller

- the principal invoking this method. It must be an owner
of the ACL.
**Parameters:** owner

- the owner that should be added to the list of owners.
**Returns:** true if successful, false if owner is already an owner.
**Throws:** NotOwnerException

- if the caller principal is not an owner
of the ACL.

---

#### addOwner

boolean addOwner​(

Principal

caller,

Principal

owner)
throws

NotOwnerException

Adds an owner. Only owners can modify ACL contents. The caller
principal must be an owner of the ACL in order to invoke this method.
That is, only an owner can add another owner. The initial owner is
configured at ACL construction time.

deleteOwner

```java
boolean deleteOwner​(
Principal
caller,

Principal
owner)
throws
NotOwnerException
,

LastOwnerException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Deletes an owner. If this is the last owner in the ACL, an exception is
raised.

The caller principal must be an owner of the ACL in order to invoke
this method.

**Parameters:** caller

- the principal invoking this method. It must be an owner
of the ACL.
**Parameters:** owner

- the owner to be removed from the list of owners.
**Returns:** true if the owner is removed, false if the owner is not part
of the list of owners.
**Throws:** NotOwnerException

- if the caller principal is not an owner
of the ACL.
**Throws:** LastOwnerException

- if there is only one owner left, so that
deleteOwner would leave the ACL owner-less.

---

#### deleteOwner

boolean deleteOwner​(

Principal

caller,

Principal

owner)
throws

NotOwnerException

,

LastOwnerException

Deletes an owner. If this is the last owner in the ACL, an exception is
raised.

The caller principal must be an owner of the ACL in order to invoke
this method.

The caller principal must be an owner of the ACL in order to invoke
this method.

isOwner

```java
boolean isOwner​(
Principal
owner)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the given principal is an owner of the ACL.

**Parameters:** owner

- the principal to be checked to determine whether or not
it is an owner.
**Returns:** true if the passed principal is in the list of owners, false
if not.

---

#### isOwner

boolean isOwner​(

Principal

owner)

Returns true if the given principal is an owner of the ACL.

---

