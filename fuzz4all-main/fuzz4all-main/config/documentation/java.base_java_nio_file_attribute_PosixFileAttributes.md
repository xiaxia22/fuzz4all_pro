# Interface PosixFileAttributes

**Source:** `java.base\java\nio\file\attribute\PosixFileAttributes.html`

### Class Description

```java
public interface
PosixFileAttributes

extends
BasicFileAttributes
```

File attributes associated with files on file systems used by operating systems
that implement the Portable Operating System Interface (POSIX) family of
standards.

The POSIX attributes of a file are retrieved using a

PosixFileAttributeView

by invoking its

readAttributes

method.

**All Superinterfaces:** BasicFileAttributes

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### UserPrincipal
owner()

Returns the owner of the file.

**Returns:**
- the file owner

**See Also:**
- FileOwnerAttributeView.setOwner(java.nio.file.attribute.UserPrincipal)

---

#### GroupPrincipal
group()

Returns the group owner of the file.

**Returns:**
- the file group owner

**See Also:**
- PosixFileAttributeView.setGroup(java.nio.file.attribute.GroupPrincipal)

---

#### Set
<
PosixFilePermission
> permissions()

Returns the permissions of the file. The file permissions are returned
as a set of

PosixFilePermission

elements. The returned set is a
copy of the file permissions and is modifiable. This allows the result
to be modified and passed to the

setPermissions

method to update the file's permissions.

**Returns:**
- the file permissions

**See Also:**
- PosixFileAttributeView.setPermissions(java.util.Set<java.nio.file.attribute.PosixFilePermission>)

---

### Additional Sections

#### Interface PosixFileAttributes

**All Superinterfaces:** BasicFileAttributes

```java
public interface
PosixFileAttributes

extends
BasicFileAttributes
```

File attributes associated with files on file systems used by operating systems
that implement the Portable Operating System Interface (POSIX) family of
standards.

The POSIX attributes of a file are retrieved using a

PosixFileAttributeView

by invoking its

readAttributes

method.

**Since:** 1.7

public interface

PosixFileAttributes

extends

BasicFileAttributes

File attributes associated with files on file systems used by operating systems
that implement the Portable Operating System Interface (POSIX) family of
standards.

The POSIX attributes of a file are retrieved using a

PosixFileAttributeView

by invoking its

readAttributes

method.

The POSIX attributes of a file are retrieved using a

PosixFileAttributeView

by invoking its

readAttributes

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GroupPrincipal

group

()

Returns the group owner of the file.

UserPrincipal

owner

()

Returns the owner of the file.

Set

<

PosixFilePermission

>

permissions

()

Returns the permissions of the file.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributes

creationTime

,

fileKey

,

isDirectory

,

isOther

,

isRegularFile

,

isSymbolicLink

,

lastAccessTime

,

lastModifiedTime

,

size

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GroupPrincipal

group

()

Returns the group owner of the file.

UserPrincipal

owner

()

Returns the owner of the file.

Set

<

PosixFilePermission

>

permissions

()

Returns the permissions of the file.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributes

creationTime

,

fileKey

,

isDirectory

,

isOther

,

isRegularFile

,

isSymbolicLink

,

lastAccessTime

,

lastModifiedTime

,

size

---

#### Method Summary

Returns the group owner of the file.

Returns the owner of the file.

Returns the permissions of the file.

Methods declared in interface java.nio.file.attribute.

BasicFileAttributes

creationTime

,

fileKey

,

isDirectory

,

isOther

,

isRegularFile

,

isSymbolicLink

,

lastAccessTime

,

lastModifiedTime

,

size

---

#### Methods declared in interface java.nio.file.attribute. BasicFileAttributes

============ METHOD DETAIL ==========

- Method Detail

- owner

```java
UserPrincipal
owner()
```

Returns the owner of the file.

**Returns:** the file owner
**See Also:** FileOwnerAttributeView.setOwner(java.nio.file.attribute.UserPrincipal)

- group

```java
GroupPrincipal
group()
```

Returns the group owner of the file.

**Returns:** the file group owner
**See Also:** PosixFileAttributeView.setGroup(java.nio.file.attribute.GroupPrincipal)

- permissions

```java
Set
<
PosixFilePermission
> permissions()
```

Returns the permissions of the file. The file permissions are returned
as a set of

PosixFilePermission

elements. The returned set is a
copy of the file permissions and is modifiable. This allows the result
to be modified and passed to the

setPermissions

method to update the file's permissions.

**Returns:** the file permissions
**See Also:** PosixFileAttributeView.setPermissions(java.util.Set<java.nio.file.attribute.PosixFilePermission>)

Method Detail

- owner

```java
UserPrincipal
owner()
```

Returns the owner of the file.

**Returns:** the file owner
**See Also:** FileOwnerAttributeView.setOwner(java.nio.file.attribute.UserPrincipal)

- group

```java
GroupPrincipal
group()
```

Returns the group owner of the file.

**Returns:** the file group owner
**See Also:** PosixFileAttributeView.setGroup(java.nio.file.attribute.GroupPrincipal)

- permissions

```java
Set
<
PosixFilePermission
> permissions()
```

Returns the permissions of the file. The file permissions are returned
as a set of

PosixFilePermission

elements. The returned set is a
copy of the file permissions and is modifiable. This allows the result
to be modified and passed to the

setPermissions

method to update the file's permissions.

**Returns:** the file permissions
**See Also:** PosixFileAttributeView.setPermissions(java.util.Set<java.nio.file.attribute.PosixFilePermission>)

---

#### Method Detail

owner

```java
UserPrincipal
owner()
```

Returns the owner of the file.

**Returns:** the file owner
**See Also:** FileOwnerAttributeView.setOwner(java.nio.file.attribute.UserPrincipal)

---

#### owner

UserPrincipal

owner()

Returns the owner of the file.

group

```java
GroupPrincipal
group()
```

Returns the group owner of the file.

**Returns:** the file group owner
**See Also:** PosixFileAttributeView.setGroup(java.nio.file.attribute.GroupPrincipal)

---

#### group

GroupPrincipal

group()

Returns the group owner of the file.

permissions

```java
Set
<
PosixFilePermission
> permissions()
```

Returns the permissions of the file. The file permissions are returned
as a set of

PosixFilePermission

elements. The returned set is a
copy of the file permissions and is modifiable. This allows the result
to be modified and passed to the

setPermissions

method to update the file's permissions.

**Returns:** the file permissions
**See Also:** PosixFileAttributeView.setPermissions(java.util.Set<java.nio.file.attribute.PosixFilePermission>)

---

#### permissions

Set

<

PosixFilePermission

> permissions()

Returns the permissions of the file. The file permissions are returned
as a set of

PosixFilePermission

elements. The returned set is a
copy of the file permissions and is modifiable. This allows the result
to be modified and passed to the

setPermissions

method to update the file's permissions.

---

