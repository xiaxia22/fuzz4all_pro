# Enum AclEntryPermission

**Source:** `java.base\java\nio\file\attribute\AclEntryPermission.html`

### Class Description

```java
public enum
AclEntryPermission

extends
Enum
<
AclEntryPermission
>
```

Defines the permissions for use with the permissions component of an ACL

entry

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

AclEntryPermission

>

---

### Field Details

#### public static final
AclEntryPermission
LIST_DIRECTORY

Permission to list the entries of a directory (equal to

READ_DATA

)

---

#### public static final
AclEntryPermission
ADD_FILE

Permission to add a new file to a directory (equal to

WRITE_DATA

)

---

#### public static final
AclEntryPermission
ADD_SUBDIRECTORY

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
AclEntryPermission
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryPermission c : AclEntryPermission.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
AclEntryPermission
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum AclEntryPermission

java.lang.Object

- java.lang.Enum

<

AclEntryPermission

>
- - java.nio.file.attribute.AclEntryPermission

java.lang.Enum

<

AclEntryPermission

>

- java.nio.file.attribute.AclEntryPermission

java.nio.file.attribute.AclEntryPermission

**All Implemented Interfaces:** Serializable

,

Comparable

<

AclEntryPermission

>

```java
public enum
AclEntryPermission

extends
Enum
<
AclEntryPermission
>
```

Defines the permissions for use with the permissions component of an ACL

entry

.

**Since:** 1.7

public enum

AclEntryPermission

extends

Enum

<

AclEntryPermission

>

Defines the permissions for use with the permissions component of an ACL

entry

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

APPEND_DATA

Permission to append data to a file.

DELETE

Permission to delete the file.

DELETE_CHILD

Permission to delete a file or directory within a directory.

EXECUTE

Permission to execute a file.

READ_ACL

Permission to read the ACL attribute.

READ_ATTRIBUTES

The ability to read (non-acl) file attributes.

READ_DATA

Permission to read the data of the file.

READ_NAMED_ATTRS

Permission to read the named attributes of a file.

SYNCHRONIZE

Permission to access file locally at the server with synchronous reads
and writes.

WRITE_ACL

Permission to write the ACL attribute.

WRITE_ATTRIBUTES

The ability to write (non-acl) file attributes.

WRITE_DATA

Permission to modify the file's data.

WRITE_NAMED_ATTRS

Permission to write the named attributes of a file.

WRITE_OWNER

Permission to change the owner.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

AclEntryPermission

ADD_FILE

Permission to add a new file to a directory (equal to

WRITE_DATA

)

static

AclEntryPermission

ADD_SUBDIRECTORY

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

static

AclEntryPermission

LIST_DIRECTORY

Permission to list the entries of a directory (equal to

READ_DATA

)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AclEntryPermission

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AclEntryPermission

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

APPEND_DATA

Permission to append data to a file.

DELETE

Permission to delete the file.

DELETE_CHILD

Permission to delete a file or directory within a directory.

EXECUTE

Permission to execute a file.

READ_ACL

Permission to read the ACL attribute.

READ_ATTRIBUTES

The ability to read (non-acl) file attributes.

READ_DATA

Permission to read the data of the file.

READ_NAMED_ATTRS

Permission to read the named attributes of a file.

SYNCHRONIZE

Permission to access file locally at the server with synchronous reads
and writes.

WRITE_ACL

Permission to write the ACL attribute.

WRITE_ATTRIBUTES

The ability to write (non-acl) file attributes.

WRITE_DATA

Permission to modify the file's data.

WRITE_NAMED_ATTRS

Permission to write the named attributes of a file.

WRITE_OWNER

Permission to change the owner.

---

#### Enum Constant Summary

Permission to append data to a file.

Permission to delete the file.

Permission to delete a file or directory within a directory.

Permission to execute a file.

Permission to read the ACL attribute.

The ability to read (non-acl) file attributes.

Permission to read the data of the file.

Permission to read the named attributes of a file.

Permission to access file locally at the server with synchronous reads
and writes.

Permission to write the ACL attribute.

The ability to write (non-acl) file attributes.

Permission to modify the file's data.

Permission to write the named attributes of a file.

Permission to change the owner.

Field Summary

Fields

Modifier and Type

Field

Description

static

AclEntryPermission

ADD_FILE

Permission to add a new file to a directory (equal to

WRITE_DATA

)

static

AclEntryPermission

ADD_SUBDIRECTORY

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

static

AclEntryPermission

LIST_DIRECTORY

Permission to list the entries of a directory (equal to

READ_DATA

)

---

#### Field Summary

Permission to add a new file to a directory (equal to

WRITE_DATA

)

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

Permission to list the entries of a directory (equal to

READ_DATA

)

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AclEntryPermission

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AclEntryPermission

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- READ_DATA

```java
public static final
AclEntryPermission
READ_DATA
```

Permission to read the data of the file.

- WRITE_DATA

```java
public static final
AclEntryPermission
WRITE_DATA
```

Permission to modify the file's data.

- APPEND_DATA

```java
public static final
AclEntryPermission
APPEND_DATA
```

Permission to append data to a file.

- READ_NAMED_ATTRS

```java
public static final
AclEntryPermission
READ_NAMED_ATTRS
```

Permission to read the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

- WRITE_NAMED_ATTRS

```java
public static final
AclEntryPermission
WRITE_NAMED_ATTRS
```

Permission to write the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

- EXECUTE

```java
public static final
AclEntryPermission
EXECUTE
```

Permission to execute a file.

- DELETE_CHILD

```java
public static final
AclEntryPermission
DELETE_CHILD
```

Permission to delete a file or directory within a directory.

- READ_ATTRIBUTES

```java
public static final
AclEntryPermission
READ_ATTRIBUTES
```

The ability to read (non-acl) file attributes.

- WRITE_ATTRIBUTES

```java
public static final
AclEntryPermission
WRITE_ATTRIBUTES
```

The ability to write (non-acl) file attributes.

- DELETE

```java
public static final
AclEntryPermission
DELETE
```

Permission to delete the file.

- READ_ACL

```java
public static final
AclEntryPermission
READ_ACL
```

Permission to read the ACL attribute.

- WRITE_ACL

```java
public static final
AclEntryPermission
WRITE_ACL
```

Permission to write the ACL attribute.

- WRITE_OWNER

```java
public static final
AclEntryPermission
WRITE_OWNER
```

Permission to change the owner.

- SYNCHRONIZE

```java
public static final
AclEntryPermission
SYNCHRONIZE
```

Permission to access file locally at the server with synchronous reads
and writes.

============ FIELD DETAIL ===========

- Field Detail

- LIST_DIRECTORY

```java
public static final
AclEntryPermission
LIST_DIRECTORY
```

Permission to list the entries of a directory (equal to

READ_DATA

)

- ADD_FILE

```java
public static final
AclEntryPermission
ADD_FILE
```

Permission to add a new file to a directory (equal to

WRITE_DATA

)

- ADD_SUBDIRECTORY

```java
public static final
AclEntryPermission
ADD_SUBDIRECTORY
```

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
AclEntryPermission
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryPermission c : AclEntryPermission.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AclEntryPermission
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- READ_DATA

```java
public static final
AclEntryPermission
READ_DATA
```

Permission to read the data of the file.

- WRITE_DATA

```java
public static final
AclEntryPermission
WRITE_DATA
```

Permission to modify the file's data.

- APPEND_DATA

```java
public static final
AclEntryPermission
APPEND_DATA
```

Permission to append data to a file.

- READ_NAMED_ATTRS

```java
public static final
AclEntryPermission
READ_NAMED_ATTRS
```

Permission to read the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

- WRITE_NAMED_ATTRS

```java
public static final
AclEntryPermission
WRITE_NAMED_ATTRS
```

Permission to write the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

- EXECUTE

```java
public static final
AclEntryPermission
EXECUTE
```

Permission to execute a file.

- DELETE_CHILD

```java
public static final
AclEntryPermission
DELETE_CHILD
```

Permission to delete a file or directory within a directory.

- READ_ATTRIBUTES

```java
public static final
AclEntryPermission
READ_ATTRIBUTES
```

The ability to read (non-acl) file attributes.

- WRITE_ATTRIBUTES

```java
public static final
AclEntryPermission
WRITE_ATTRIBUTES
```

The ability to write (non-acl) file attributes.

- DELETE

```java
public static final
AclEntryPermission
DELETE
```

Permission to delete the file.

- READ_ACL

```java
public static final
AclEntryPermission
READ_ACL
```

Permission to read the ACL attribute.

- WRITE_ACL

```java
public static final
AclEntryPermission
WRITE_ACL
```

Permission to write the ACL attribute.

- WRITE_OWNER

```java
public static final
AclEntryPermission
WRITE_OWNER
```

Permission to change the owner.

- SYNCHRONIZE

```java
public static final
AclEntryPermission
SYNCHRONIZE
```

Permission to access file locally at the server with synchronous reads
and writes.

---

#### Enum Constant Detail

READ_DATA

```java
public static final
AclEntryPermission
READ_DATA
```

Permission to read the data of the file.

---

#### READ_DATA

public static final

AclEntryPermission

READ_DATA

Permission to read the data of the file.

WRITE_DATA

```java
public static final
AclEntryPermission
WRITE_DATA
```

Permission to modify the file's data.

---

#### WRITE_DATA

public static final

AclEntryPermission

WRITE_DATA

Permission to modify the file's data.

APPEND_DATA

```java
public static final
AclEntryPermission
APPEND_DATA
```

Permission to append data to a file.

---

#### APPEND_DATA

public static final

AclEntryPermission

APPEND_DATA

Permission to append data to a file.

READ_NAMED_ATTRS

```java
public static final
AclEntryPermission
READ_NAMED_ATTRS
```

Permission to read the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

---

#### READ_NAMED_ATTRS

public static final

AclEntryPermission

READ_NAMED_ATTRS

Permission to read the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

WRITE_NAMED_ATTRS

```java
public static final
AclEntryPermission
WRITE_NAMED_ATTRS
```

Permission to write the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

---

#### WRITE_NAMED_ATTRS

public static final

AclEntryPermission

WRITE_NAMED_ATTRS

Permission to write the named attributes of a file.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

RFC 3530: Network
File System (NFS) version 4 Protocol

defines

named attributes

as opaque files associated with a file in the file system.

EXECUTE

```java
public static final
AclEntryPermission
EXECUTE
```

Permission to execute a file.

---

#### EXECUTE

public static final

AclEntryPermission

EXECUTE

Permission to execute a file.

DELETE_CHILD

```java
public static final
AclEntryPermission
DELETE_CHILD
```

Permission to delete a file or directory within a directory.

---

#### DELETE_CHILD

public static final

AclEntryPermission

DELETE_CHILD

Permission to delete a file or directory within a directory.

READ_ATTRIBUTES

```java
public static final
AclEntryPermission
READ_ATTRIBUTES
```

The ability to read (non-acl) file attributes.

---

#### READ_ATTRIBUTES

public static final

AclEntryPermission

READ_ATTRIBUTES

The ability to read (non-acl) file attributes.

WRITE_ATTRIBUTES

```java
public static final
AclEntryPermission
WRITE_ATTRIBUTES
```

The ability to write (non-acl) file attributes.

---

#### WRITE_ATTRIBUTES

public static final

AclEntryPermission

WRITE_ATTRIBUTES

The ability to write (non-acl) file attributes.

DELETE

```java
public static final
AclEntryPermission
DELETE
```

Permission to delete the file.

---

#### DELETE

public static final

AclEntryPermission

DELETE

Permission to delete the file.

READ_ACL

```java
public static final
AclEntryPermission
READ_ACL
```

Permission to read the ACL attribute.

---

#### READ_ACL

public static final

AclEntryPermission

READ_ACL

Permission to read the ACL attribute.

WRITE_ACL

```java
public static final
AclEntryPermission
WRITE_ACL
```

Permission to write the ACL attribute.

---

#### WRITE_ACL

public static final

AclEntryPermission

WRITE_ACL

Permission to write the ACL attribute.

WRITE_OWNER

```java
public static final
AclEntryPermission
WRITE_OWNER
```

Permission to change the owner.

---

#### WRITE_OWNER

public static final

AclEntryPermission

WRITE_OWNER

Permission to change the owner.

SYNCHRONIZE

```java
public static final
AclEntryPermission
SYNCHRONIZE
```

Permission to access file locally at the server with synchronous reads
and writes.

---

#### SYNCHRONIZE

public static final

AclEntryPermission

SYNCHRONIZE

Permission to access file locally at the server with synchronous reads
and writes.

Field Detail

- LIST_DIRECTORY

```java
public static final
AclEntryPermission
LIST_DIRECTORY
```

Permission to list the entries of a directory (equal to

READ_DATA

)

- ADD_FILE

```java
public static final
AclEntryPermission
ADD_FILE
```

Permission to add a new file to a directory (equal to

WRITE_DATA

)

- ADD_SUBDIRECTORY

```java
public static final
AclEntryPermission
ADD_SUBDIRECTORY
```

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

---

#### Field Detail

LIST_DIRECTORY

```java
public static final
AclEntryPermission
LIST_DIRECTORY
```

Permission to list the entries of a directory (equal to

READ_DATA

)

---

#### LIST_DIRECTORY

public static final

AclEntryPermission

LIST_DIRECTORY

Permission to list the entries of a directory (equal to

READ_DATA

)

ADD_FILE

```java
public static final
AclEntryPermission
ADD_FILE
```

Permission to add a new file to a directory (equal to

WRITE_DATA

)

---

#### ADD_FILE

public static final

AclEntryPermission

ADD_FILE

Permission to add a new file to a directory (equal to

WRITE_DATA

)

ADD_SUBDIRECTORY

```java
public static final
AclEntryPermission
ADD_SUBDIRECTORY
```

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

---

#### ADD_SUBDIRECTORY

public static final

AclEntryPermission

ADD_SUBDIRECTORY

Permission to create a subdirectory to a directory (equal to

APPEND_DATA

)

Method Detail

- values

```java
public static
AclEntryPermission
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryPermission c : AclEntryPermission.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AclEntryPermission
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
AclEntryPermission
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryPermission c : AclEntryPermission.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

AclEntryPermission

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryPermission c : AclEntryPermission.values())
System.out.println(c);
```

for (AclEntryPermission c : AclEntryPermission.values())
System.out.println(c);

valueOf

```java
public static
AclEntryPermission
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

AclEntryPermission

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

