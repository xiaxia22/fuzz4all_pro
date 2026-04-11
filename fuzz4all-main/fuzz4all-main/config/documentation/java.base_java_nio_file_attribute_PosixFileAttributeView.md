# Interface PosixFileAttributeView

**Source:** `java.base\java\nio\file\attribute\PosixFileAttributeView.html`

### Class Description

```java
public interface
PosixFileAttributeView

extends
BasicFileAttributeView
,
FileOwnerAttributeView
```

A file attribute view that provides a view of the file attributes commonly
associated with files on file systems used by operating systems that implement
the Portable Operating System Interface (POSIX) family of standards.

Operating systems that implement the

POSIX

family of standards commonly use file systems that have a
file

owner

,

group-owner

, and related

access
permissions

. This file attribute view provides read and write access
to these attributes.

The

readAttributes

method is used to read the
file's attributes. The file

owner

is
represented by a

UserPrincipal

that is the identity of the file owner
for the purposes of access control. The

group-owner

, represented by a

GroupPrincipal

, is the identity of the
group owner, where a group is an identity created for administrative purposes
so as to determine the access rights for the members of the group.

The

permissions

attribute is a
set of access permissions. This file attribute view provides access to the nine
permission defined by the

PosixFilePermission

class.
These nine permission bits determine the

read

,

write

, and

execute

access for the file owner, group, and others (others
meaning identities other than the owner and members of the group). Some
operating systems and file systems may provide additional permission bits
but access to these other bits is not defined by this class in this release.

Usage Example:

Suppose we need to print out the owner and access permissions of a file:

```java
Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));
```

Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

**All Superinterfaces:** AttributeView

,

BasicFileAttributeView

,

FileAttributeView

,

FileOwnerAttributeView

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

"posix"

.

**Specified by:**
- name

in interface

AttributeView
- name

in interface

BasicFileAttributeView
- name

in interface

FileOwnerAttributeView

**Returns:**
- the name of the attribute view

---

#### PosixFileAttributes
readAttributes()
throws
IOException

Description copied from interface:

BasicFileAttributeView

**Specified by:**
- readAttributes

in interface

BasicFileAttributeView

**Returns:**
- the file attributes

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

#### void setPermissions​(
Set
<
PosixFilePermission
> perms)
throws
IOException

Updates the file permissions.

**Parameters:**
- perms

- the new set of permissions

**Throws:**
- ClassCastException

- if the sets contains elements that are not of type

PosixFilePermission
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

---

#### void setGroup​(
GroupPrincipal
group)
throws
IOException

Updates the file group-owner.

**Parameters:**
- group

- the new file group-owner

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default provider, and a security manager is
installed, it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

---

### Additional Sections

#### Interface PosixFileAttributeView

**All Superinterfaces:** AttributeView

,

BasicFileAttributeView

,

FileAttributeView

,

FileOwnerAttributeView

```java
public interface
PosixFileAttributeView

extends
BasicFileAttributeView
,
FileOwnerAttributeView
```

A file attribute view that provides a view of the file attributes commonly
associated with files on file systems used by operating systems that implement
the Portable Operating System Interface (POSIX) family of standards.

Operating systems that implement the

POSIX

family of standards commonly use file systems that have a
file

owner

,

group-owner

, and related

access
permissions

. This file attribute view provides read and write access
to these attributes.

The

readAttributes

method is used to read the
file's attributes. The file

owner

is
represented by a

UserPrincipal

that is the identity of the file owner
for the purposes of access control. The

group-owner

, represented by a

GroupPrincipal

, is the identity of the
group owner, where a group is an identity created for administrative purposes
so as to determine the access rights for the members of the group.

The

permissions

attribute is a
set of access permissions. This file attribute view provides access to the nine
permission defined by the

PosixFilePermission

class.
These nine permission bits determine the

read

,

write

, and

execute

access for the file owner, group, and others (others
meaning identities other than the owner and members of the group). Some
operating systems and file systems may provide additional permission bits
but access to these other bits is not defined by this class in this release.

Usage Example:

Suppose we need to print out the owner and access permissions of a file:

```java
Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));
```

Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

**Since:** 1.7

public interface

PosixFileAttributeView

extends

BasicFileAttributeView

,

FileOwnerAttributeView

A file attribute view that provides a view of the file attributes commonly
associated with files on file systems used by operating systems that implement
the Portable Operating System Interface (POSIX) family of standards.

Operating systems that implement the

POSIX

family of standards commonly use file systems that have a
file

owner

,

group-owner

, and related

access
permissions

. This file attribute view provides read and write access
to these attributes.

The

readAttributes

method is used to read the
file's attributes. The file

owner

is
represented by a

UserPrincipal

that is the identity of the file owner
for the purposes of access control. The

group-owner

, represented by a

GroupPrincipal

, is the identity of the
group owner, where a group is an identity created for administrative purposes
so as to determine the access rights for the members of the group.

The

permissions

attribute is a
set of access permissions. This file attribute view provides access to the nine
permission defined by the

PosixFilePermission

class.
These nine permission bits determine the

read

,

write

, and

execute

access for the file owner, group, and others (others
meaning identities other than the owner and members of the group). Some
operating systems and file systems may provide additional permission bits
but access to these other bits is not defined by this class in this release.

Usage Example:

Suppose we need to print out the owner and access permissions of a file:

```java
Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));
```

Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

Operating systems that implement the

POSIX

family of standards commonly use file systems that have a
file

owner

,

group-owner

, and related

access
permissions

. This file attribute view provides read and write access
to these attributes.

The

readAttributes

method is used to read the
file's attributes. The file

owner

is
represented by a

UserPrincipal

that is the identity of the file owner
for the purposes of access control. The

group-owner

, represented by a

GroupPrincipal

, is the identity of the
group owner, where a group is an identity created for administrative purposes
so as to determine the access rights for the members of the group.

The

permissions

attribute is a
set of access permissions. This file attribute view provides access to the nine
permission defined by the

PosixFilePermission

class.
These nine permission bits determine the

read

,

write

, and

execute

access for the file owner, group, and others (others
meaning identities other than the owner and members of the group). Some
operating systems and file systems may provide additional permission bits
but access to these other bits is not defined by this class in this release.

Usage Example:

Suppose we need to print out the owner and access permissions of a file:

```java
Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));
```

Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

The

readAttributes

method is used to read the
file's attributes. The file

owner

is
represented by a

UserPrincipal

that is the identity of the file owner
for the purposes of access control. The

group-owner

, represented by a

GroupPrincipal

, is the identity of the
group owner, where a group is an identity created for administrative purposes
so as to determine the access rights for the members of the group.

The

permissions

attribute is a
set of access permissions. This file attribute view provides access to the nine
permission defined by the

PosixFilePermission

class.
These nine permission bits determine the

read

,

write

, and

execute

access for the file owner, group, and others (others
meaning identities other than the owner and members of the group). Some
operating systems and file systems may provide additional permission bits
but access to these other bits is not defined by this class in this release.

Usage Example:

Suppose we need to print out the owner and access permissions of a file:

```java
Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));
```

Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

The

permissions

attribute is a
set of access permissions. This file attribute view provides access to the nine
permission defined by the

PosixFilePermission

class.
These nine permission bits determine the

read

,

write

, and

execute

access for the file owner, group, and others (others
meaning identities other than the owner and members of the group). Some
operating systems and file systems may provide additional permission bits
but access to these other bits is not defined by this class in this release.

Usage Example:

Suppose we need to print out the owner and access permissions of a file:

```java
Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));
```

Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

Usage Example:

Suppose we need to print out the owner and access permissions of a file:

```java
Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));
```

Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

Path file = ...
PosixFileAttributes attrs = Files.getFileAttributeView(file, PosixFileAttributeView.class)
.readAttributes();
System.out.format("%s %s%n",
attrs.owner().getName(),
PosixFilePermissions.toString(attrs.permissions()));

---

#### Dynamic Access

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

and

FileOwnerAttributeView

, and in addition,
the following attributes are supported:

Supported attributes

Name

Type

"permissions"

Set

<

PosixFilePermission

>

"group"

GroupPrincipal

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

The

getAttribute

method may be used to read
any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

The

setAttribute

method may be used to update
the file's last modified time, last access time or create time attributes as
defined by

BasicFileAttributeView

. It may also be used to update
the permissions, owner, or group-owner as if by invoking the

setPermissions

,

setOwner

, and

setGroup

methods respectively.

Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

---

#### Setting Initial Permissions

Implementations supporting this attribute view may also support setting
the initial permissions when creating a file or directory. The
initial permissions are provided to the

createFile

or

createDirectory

methods as a

FileAttribute

with

name

"posix:permissions"

and a

value

that is the set of permissions. The
following example uses the

asFileAttribute

method to construct a

FileAttribute

when creating a
file:

```java
Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));
```

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

Path path = ...
Set<PosixFilePermission> perms =
EnumSet.of(OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ);
Files.createFile(path, PosixFilePermissions.asFileAttribute(perms));

When the access permissions are set at file creation time then the actual
value of the permissions may differ that the value of the attribute object.
The reasons for this are implementation specific. On UNIX systems, for
example, a process has a

umask

that impacts the permission bits
of newly created files. Where an implementation supports the setting of
the access permissions, and the underlying file system supports access
permissions, then it is required that the value of the actual access
permissions will be equal or less than the value of the attribute
provided to the

createFile

or

createDirectory

methods. In other words, the file may
be more secure than requested.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the attribute view.

PosixFileAttributes

readAttributes

()

Reads the basic file attributes as a bulk operation.

void

setGroup

​(

GroupPrincipal

group)

Updates the file group-owner.

void

setPermissions

​(

Set

<

PosixFilePermission

> perms)

Updates the file permissions.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributeView

setTimes

- Methods declared in interface java.nio.file.attribute.

FileOwnerAttributeView

getOwner

,

setOwner

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the attribute view.

PosixFileAttributes

readAttributes

()

Reads the basic file attributes as a bulk operation.

void

setGroup

​(

GroupPrincipal

group)

Updates the file group-owner.

void

setPermissions

​(

Set

<

PosixFilePermission

> perms)

Updates the file permissions.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributeView

setTimes

- Methods declared in interface java.nio.file.attribute.

FileOwnerAttributeView

getOwner

,

setOwner

---

#### Method Summary

Returns the name of the attribute view.

Reads the basic file attributes as a bulk operation.

Updates the file group-owner.

Updates the file permissions.

Methods declared in interface java.nio.file.attribute.

BasicFileAttributeView

setTimes

---

#### Methods declared in interface java.nio.file.attribute. BasicFileAttributeView

Methods declared in interface java.nio.file.attribute.

FileOwnerAttributeView

getOwner

,

setOwner

---

#### Methods declared in interface java.nio.file.attribute. FileOwnerAttributeView

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"posix"

.

**Specified by:** name

in interface

AttributeView
**Specified by:** name

in interface

BasicFileAttributeView
**Specified by:** name

in interface

FileOwnerAttributeView
**Returns:** the name of the attribute view

- readAttributes

```java
PosixFileAttributes
readAttributes()
throws
IOException
```

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Specified by:** readAttributes

in interface

BasicFileAttributeView
**Returns:** the file attributes
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

- setPermissions

```java
void setPermissions​(
Set
<
PosixFilePermission
> perms)
throws
IOException
```

Updates the file permissions.

**Parameters:** perms

- the new set of permissions
**Throws:** ClassCastException

- if the sets contains elements that are not of type

PosixFilePermission
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

- setGroup

```java
void setGroup​(
GroupPrincipal
group)
throws
IOException
```

Updates the file group-owner.

**Parameters:** group

- the new file group-owner
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"posix"

.

**Specified by:** name

in interface

AttributeView
**Specified by:** name

in interface

BasicFileAttributeView
**Specified by:** name

in interface

FileOwnerAttributeView
**Returns:** the name of the attribute view

- readAttributes

```java
PosixFileAttributes
readAttributes()
throws
IOException
```

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Specified by:** readAttributes

in interface

BasicFileAttributeView
**Returns:** the file attributes
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

- setPermissions

```java
void setPermissions​(
Set
<
PosixFilePermission
> perms)
throws
IOException
```

Updates the file permissions.

**Parameters:** perms

- the new set of permissions
**Throws:** ClassCastException

- if the sets contains elements that are not of type

PosixFilePermission
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

- setGroup

```java
void setGroup​(
GroupPrincipal
group)
throws
IOException
```

Updates the file group-owner.

**Parameters:** group

- the new file group-owner
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

---

#### Method Detail

name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"posix"

.

**Specified by:** name

in interface

AttributeView
**Specified by:** name

in interface

BasicFileAttributeView
**Specified by:** name

in interface

FileOwnerAttributeView
**Returns:** the name of the attribute view

---

#### name

String

name()

Returns the name of the attribute view. Attribute views of this type
have the name

"posix"

.

readAttributes

```java
PosixFileAttributes
readAttributes()
throws
IOException
```

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Specified by:** readAttributes

in interface

BasicFileAttributeView
**Returns:** the file attributes
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

#### readAttributes

PosixFileAttributes

readAttributes()
throws

IOException

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

setPermissions

```java
void setPermissions​(
Set
<
PosixFilePermission
> perms)
throws
IOException
```

Updates the file permissions.

**Parameters:** perms

- the new set of permissions
**Throws:** ClassCastException

- if the sets contains elements that are not of type

PosixFilePermission
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, and it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

---

#### setPermissions

void setPermissions​(

Set

<

PosixFilePermission

> perms)
throws

IOException

Updates the file permissions.

setGroup

```java
void setGroup​(
GroupPrincipal
group)
throws
IOException
```

Updates the file group-owner.

**Parameters:** group

- the new file group-owner
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, and a security manager is
installed, it denies

RuntimePermission

("accessUserInformation")

or its

checkWrite

method denies write access to the file.

---

#### setGroup

void setGroup​(

GroupPrincipal

group)
throws

IOException

Updates the file group-owner.

---

