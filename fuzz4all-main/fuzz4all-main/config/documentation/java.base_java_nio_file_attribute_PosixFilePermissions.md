# Class PosixFilePermissions

**Source:** `java.base\java\nio\file\attribute\PosixFilePermissions.html`

### Class Description

```java
public final class
PosixFilePermissions

extends
Object
```

This class consists exclusively of static methods that operate on sets of

PosixFilePermission

objects.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
String
toString​(
Set
<
PosixFilePermission
> perms)

Returns the

String

representation of a set of permissions. It
is guaranteed that the returned

String

can be parsed by the

fromString(java.lang.String)

method.

If the set contains

null

or elements that are not of type

PosixFilePermission

then these elements are ignored.

**Parameters:**
- perms

- the set of permissions

**Returns:**
- the string representation of the permission set

---

#### public static
Set
<
PosixFilePermission
> fromString​(
String
perms)

Returns the set of permissions corresponding to a given

String

representation.

The

perms

parameter is a

String

representing the
permissions. It has 9 characters that are interpreted as three sets of
three. The first set refers to the owner's permissions; the next to the
group permissions and the last to others. Within each set, the first
character is

'r'

to indicate permission to read, the second
character is

'w'

to indicate permission to write, and the third
character is

'x'

for execute permission. Where a permission is
not set then the corresponding character is set to

'-'

.

Usage Example:

Suppose we require the set of permissions that indicate the owner has read,
write, and execute permissions, the group has read and execute permissions
and others have none.

```java
Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
```

**Parameters:**
- perms

- string representing a set of permissions

**Returns:**
- the resulting set of permissions

**Throws:**
- IllegalArgumentException

- if the string cannot be converted to a set of permissions

**See Also:**
- toString(Set)

---

#### public static
FileAttribute
<
Set
<
PosixFilePermission
>> asFileAttribute​(
Set
<
PosixFilePermission
> perms)

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

**Parameters:**
- perms

- the set of permissions

**Returns:**
- an attribute encapsulating the given file permissions with

name

"posix:permissions"

**Throws:**
- ClassCastException

- if the set contains elements that are not of type

PosixFilePermission

---

### Additional Sections

#### Class PosixFilePermissions

java.lang.Object

- java.nio.file.attribute.PosixFilePermissions

java.nio.file.attribute.PosixFilePermissions

```java
public final class
PosixFilePermissions

extends
Object
```

This class consists exclusively of static methods that operate on sets of

PosixFilePermission

objects.

**Since:** 1.7

public final class

PosixFilePermissions

extends

Object

This class consists exclusively of static methods that operate on sets of

PosixFilePermission

objects.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FileAttribute

<

Set

<

PosixFilePermission

>>

asFileAttribute

​(

Set

<

PosixFilePermission

> perms)

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

static

Set

<

PosixFilePermission

>

fromString

​(

String

perms)

Returns the set of permissions corresponding to a given

String

representation.

static

String

toString

​(

Set

<

PosixFilePermission

> perms)

Returns the

String

representation of a set of permissions.

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

toString

,

wait

,

wait

,

wait

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FileAttribute

<

Set

<

PosixFilePermission

>>

asFileAttribute

​(

Set

<

PosixFilePermission

> perms)

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

static

Set

<

PosixFilePermission

>

fromString

​(

String

perms)

Returns the set of permissions corresponding to a given

String

representation.

static

String

toString

​(

Set

<

PosixFilePermission

> perms)

Returns the

String

representation of a set of permissions.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

Returns the set of permissions corresponding to a given

String

representation.

Returns the

String

representation of a set of permissions.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public static
String
toString​(
Set
<
PosixFilePermission
> perms)
```

Returns the

String

representation of a set of permissions. It
is guaranteed that the returned

String

can be parsed by the

fromString(java.lang.String)

method.

If the set contains

null

or elements that are not of type

PosixFilePermission

then these elements are ignored.

**Parameters:** perms

- the set of permissions
**Returns:** the string representation of the permission set

- fromString

```java
public static
Set
<
PosixFilePermission
> fromString​(
String
perms)
```

Returns the set of permissions corresponding to a given

String

representation.

The

perms

parameter is a

String

representing the
permissions. It has 9 characters that are interpreted as three sets of
three. The first set refers to the owner's permissions; the next to the
group permissions and the last to others. Within each set, the first
character is

'r'

to indicate permission to read, the second
character is

'w'

to indicate permission to write, and the third
character is

'x'

for execute permission. Where a permission is
not set then the corresponding character is set to

'-'

.

Usage Example:

Suppose we require the set of permissions that indicate the owner has read,
write, and execute permissions, the group has read and execute permissions
and others have none.

```java
Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
```

**Parameters:** perms

- string representing a set of permissions
**Returns:** the resulting set of permissions
**Throws:** IllegalArgumentException

- if the string cannot be converted to a set of permissions
**See Also:** toString(Set)

- asFileAttribute

```java
public static
FileAttribute
<
Set
<
PosixFilePermission
>> asFileAttribute​(
Set
<
PosixFilePermission
> perms)
```

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

**Parameters:** perms

- the set of permissions
**Returns:** an attribute encapsulating the given file permissions with

name

"posix:permissions"
**Throws:** ClassCastException

- if the set contains elements that are not of type

PosixFilePermission

Method Detail

- toString

```java
public static
String
toString​(
Set
<
PosixFilePermission
> perms)
```

Returns the

String

representation of a set of permissions. It
is guaranteed that the returned

String

can be parsed by the

fromString(java.lang.String)

method.

If the set contains

null

or elements that are not of type

PosixFilePermission

then these elements are ignored.

**Parameters:** perms

- the set of permissions
**Returns:** the string representation of the permission set

- fromString

```java
public static
Set
<
PosixFilePermission
> fromString​(
String
perms)
```

Returns the set of permissions corresponding to a given

String

representation.

The

perms

parameter is a

String

representing the
permissions. It has 9 characters that are interpreted as three sets of
three. The first set refers to the owner's permissions; the next to the
group permissions and the last to others. Within each set, the first
character is

'r'

to indicate permission to read, the second
character is

'w'

to indicate permission to write, and the third
character is

'x'

for execute permission. Where a permission is
not set then the corresponding character is set to

'-'

.

Usage Example:

Suppose we require the set of permissions that indicate the owner has read,
write, and execute permissions, the group has read and execute permissions
and others have none.

```java
Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
```

**Parameters:** perms

- string representing a set of permissions
**Returns:** the resulting set of permissions
**Throws:** IllegalArgumentException

- if the string cannot be converted to a set of permissions
**See Also:** toString(Set)

- asFileAttribute

```java
public static
FileAttribute
<
Set
<
PosixFilePermission
>> asFileAttribute​(
Set
<
PosixFilePermission
> perms)
```

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

**Parameters:** perms

- the set of permissions
**Returns:** an attribute encapsulating the given file permissions with

name

"posix:permissions"
**Throws:** ClassCastException

- if the set contains elements that are not of type

PosixFilePermission

---

#### Method Detail

toString

```java
public static
String
toString​(
Set
<
PosixFilePermission
> perms)
```

Returns the

String

representation of a set of permissions. It
is guaranteed that the returned

String

can be parsed by the

fromString(java.lang.String)

method.

If the set contains

null

or elements that are not of type

PosixFilePermission

then these elements are ignored.

**Parameters:** perms

- the set of permissions
**Returns:** the string representation of the permission set

---

#### toString

public static

String

toString​(

Set

<

PosixFilePermission

> perms)

Returns the

String

representation of a set of permissions. It
is guaranteed that the returned

String

can be parsed by the

fromString(java.lang.String)

method.

If the set contains

null

or elements that are not of type

PosixFilePermission

then these elements are ignored.

If the set contains

null

or elements that are not of type

PosixFilePermission

then these elements are ignored.

fromString

```java
public static
Set
<
PosixFilePermission
> fromString​(
String
perms)
```

Returns the set of permissions corresponding to a given

String

representation.

The

perms

parameter is a

String

representing the
permissions. It has 9 characters that are interpreted as three sets of
three. The first set refers to the owner's permissions; the next to the
group permissions and the last to others. Within each set, the first
character is

'r'

to indicate permission to read, the second
character is

'w'

to indicate permission to write, and the third
character is

'x'

for execute permission. Where a permission is
not set then the corresponding character is set to

'-'

.

Usage Example:

Suppose we require the set of permissions that indicate the owner has read,
write, and execute permissions, the group has read and execute permissions
and others have none.

```java
Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
```

**Parameters:** perms

- string representing a set of permissions
**Returns:** the resulting set of permissions
**Throws:** IllegalArgumentException

- if the string cannot be converted to a set of permissions
**See Also:** toString(Set)

---

#### fromString

public static

Set

<

PosixFilePermission

> fromString​(

String

perms)

Returns the set of permissions corresponding to a given

String

representation.

The

perms

parameter is a

String

representing the
permissions. It has 9 characters that are interpreted as three sets of
three. The first set refers to the owner's permissions; the next to the
group permissions and the last to others. Within each set, the first
character is

'r'

to indicate permission to read, the second
character is

'w'

to indicate permission to write, and the third
character is

'x'

for execute permission. Where a permission is
not set then the corresponding character is set to

'-'

.

Usage Example:

Suppose we require the set of permissions that indicate the owner has read,
write, and execute permissions, the group has read and execute permissions
and others have none.

```java
Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
```

The

perms

parameter is a

String

representing the
permissions. It has 9 characters that are interpreted as three sets of
three. The first set refers to the owner's permissions; the next to the
group permissions and the last to others. Within each set, the first
character is

'r'

to indicate permission to read, the second
character is

'w'

to indicate permission to write, and the third
character is

'x'

for execute permission. Where a permission is
not set then the corresponding character is set to

'-'

.

Usage Example:

Suppose we require the set of permissions that indicate the owner has read,
write, and execute permissions, the group has read and execute permissions
and others have none.

```java
Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
```

Usage Example:

Suppose we require the set of permissions that indicate the owner has read,
write, and execute permissions, the group has read and execute permissions
and others have none.

```java
Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
```

Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");

asFileAttribute

```java
public static
FileAttribute
<
Set
<
PosixFilePermission
>> asFileAttribute​(
Set
<
PosixFilePermission
> perms)
```

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

**Parameters:** perms

- the set of permissions
**Returns:** an attribute encapsulating the given file permissions with

name

"posix:permissions"
**Throws:** ClassCastException

- if the set contains elements that are not of type

PosixFilePermission

---

#### asFileAttribute

public static

FileAttribute

<

Set

<

PosixFilePermission

>> asFileAttribute​(

Set

<

PosixFilePermission

> perms)

Creates a

FileAttribute

, encapsulating a copy of the given file
permissions, suitable for passing to the

createFile

or

createDirectory

methods.

---

