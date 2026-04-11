# Interface FileOwnerAttributeView

**Source:** `java.base\java\nio\file\attribute\FileOwnerAttributeView.html`

### Class Description

```java
public interface
FileOwnerAttributeView

extends
FileAttributeView
```

A file attribute view that supports reading or updating the owner of a file.
This file attribute view is intended for file system implementations that
support a file attribute that represents an identity that is the owner of
the file. Often the owner of a file is the identity of the entity that
created the file.

The

getOwner

or

setOwner

methods may
be used to read or update the owner of the file.

The

getAttribute

and

setAttribute

methods may also be
used to read or update the owner. In that case, the owner attribute is
identified by the name

"owner"

, and the value of the attribute is
a

UserPrincipal

.

**All Superinterfaces:** AttributeView

,

FileAttributeView

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the name of the attribute view. Attribute views of this type
have the name

"owner"

.

**Specified by:**
- name

in interface

AttributeView

**Returns:**
- the name of the attribute view

---

#### UserPrincipal
getOwner()
throws
IOException

Read the file owner.

It is implementation specific if the file owner can be a

group

.

**Returns:**
- the file owner

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkRead

method
denies read access to the file.

---

#### void setOwner​(
UserPrincipal
owner)
throws
IOException

Updates the file owner.

It is implementation specific if the file owner can be a

group

. To ensure consistent and correct behavior
across platforms it is recommended that this method should only be used
to set the file owner to a user principal that is not a group.

**Parameters:**
- owner

- the new file owner

**Throws:**
- IOException

- if an I/O error occurs, or the

owner

parameter is a
group and this implementation does not support setting the owner
to a group
- SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method
denies write access to the file.

---

### Additional Sections

#### Interface FileOwnerAttributeView

**All Superinterfaces:** AttributeView

,

FileAttributeView

**All Known Subinterfaces:** AclFileAttributeView

,

PosixFileAttributeView

```java
public interface
FileOwnerAttributeView

extends
FileAttributeView
```

A file attribute view that supports reading or updating the owner of a file.
This file attribute view is intended for file system implementations that
support a file attribute that represents an identity that is the owner of
the file. Often the owner of a file is the identity of the entity that
created the file.

The

getOwner

or

setOwner

methods may
be used to read or update the owner of the file.

The

getAttribute

and

setAttribute

methods may also be
used to read or update the owner. In that case, the owner attribute is
identified by the name

"owner"

, and the value of the attribute is
a

UserPrincipal

.

**Since:** 1.7

public interface

FileOwnerAttributeView

extends

FileAttributeView

A file attribute view that supports reading or updating the owner of a file.
This file attribute view is intended for file system implementations that
support a file attribute that represents an identity that is the owner of
the file. Often the owner of a file is the identity of the entity that
created the file.

The

getOwner

or

setOwner

methods may
be used to read or update the owner of the file.

The

getAttribute

and

setAttribute

methods may also be
used to read or update the owner. In that case, the owner attribute is
identified by the name

"owner"

, and the value of the attribute is
a

UserPrincipal

.

The

getOwner

or

setOwner

methods may
be used to read or update the owner of the file.

The

getAttribute

and

setAttribute

methods may also be
used to read or update the owner. In that case, the owner attribute is
identified by the name

"owner"

, and the value of the attribute is
a

UserPrincipal

.

The

getAttribute

and

setAttribute

methods may also be
used to read or update the owner. In that case, the owner attribute is
identified by the name

"owner"

, and the value of the attribute is
a

UserPrincipal

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

UserPrincipal

getOwner

()

Read the file owner.

String

name

()

Returns the name of the attribute view.

void

setOwner

​(

UserPrincipal

owner)

Updates the file owner.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

UserPrincipal

getOwner

()

Read the file owner.

String

name

()

Returns the name of the attribute view.

void

setOwner

​(

UserPrincipal

owner)

Updates the file owner.

---

#### Method Summary

Read the file owner.

Returns the name of the attribute view.

Updates the file owner.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"owner"

.

**Specified by:** name

in interface

AttributeView
**Returns:** the name of the attribute view

- getOwner

```java
UserPrincipal
getOwner()
throws
IOException
```

Read the file owner.

It is implementation specific if the file owner can be a

group

.

**Returns:** the file owner
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkRead

method
denies read access to the file.

- setOwner

```java
void setOwner​(
UserPrincipal
owner)
throws
IOException
```

Updates the file owner.

It is implementation specific if the file owner can be a

group

. To ensure consistent and correct behavior
across platforms it is recommended that this method should only be used
to set the file owner to a user principal that is not a group.

**Parameters:** owner

- the new file owner
**Throws:** IOException

- if an I/O error occurs, or the

owner

parameter is a
group and this implementation does not support setting the owner
to a group
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method
denies write access to the file.

Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"owner"

.

**Specified by:** name

in interface

AttributeView
**Returns:** the name of the attribute view

- getOwner

```java
UserPrincipal
getOwner()
throws
IOException
```

Read the file owner.

It is implementation specific if the file owner can be a

group

.

**Returns:** the file owner
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkRead

method
denies read access to the file.

- setOwner

```java
void setOwner​(
UserPrincipal
owner)
throws
IOException
```

Updates the file owner.

It is implementation specific if the file owner can be a

group

. To ensure consistent and correct behavior
across platforms it is recommended that this method should only be used
to set the file owner to a user principal that is not a group.

**Parameters:** owner

- the new file owner
**Throws:** IOException

- if an I/O error occurs, or the

owner

parameter is a
group and this implementation does not support setting the owner
to a group
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method
denies write access to the file.

---

#### Method Detail

name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"owner"

.

**Specified by:** name

in interface

AttributeView
**Returns:** the name of the attribute view

---

#### name

String

name()

Returns the name of the attribute view. Attribute views of this type
have the name

"owner"

.

getOwner

```java
UserPrincipal
getOwner()
throws
IOException
```

Read the file owner.

It is implementation specific if the file owner can be a

group

.

**Returns:** the file owner
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkRead

method
denies read access to the file.

---

#### getOwner

UserPrincipal

getOwner()
throws

IOException

Read the file owner.

It is implementation specific if the file owner can be a

group

.

It is implementation specific if the file owner can be a

group

.

setOwner

```java
void setOwner​(
UserPrincipal
owner)
throws
IOException
```

Updates the file owner.

It is implementation specific if the file owner can be a

group

. To ensure consistent and correct behavior
across platforms it is recommended that this method should only be used
to set the file owner to a user principal that is not a group.

**Parameters:** owner

- the new file owner
**Throws:** IOException

- if an I/O error occurs, or the

owner

parameter is a
group and this implementation does not support setting the owner
to a group
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method
denies write access to the file.

---

#### setOwner

void setOwner​(

UserPrincipal

owner)
throws

IOException

Updates the file owner.

It is implementation specific if the file owner can be a

group

. To ensure consistent and correct behavior
across platforms it is recommended that this method should only be used
to set the file owner to a user principal that is not a group.

It is implementation specific if the file owner can be a

group

. To ensure consistent and correct behavior
across platforms it is recommended that this method should only be used
to set the file owner to a user principal that is not a group.

---

