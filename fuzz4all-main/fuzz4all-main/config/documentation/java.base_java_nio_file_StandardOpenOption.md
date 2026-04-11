# Enum StandardOpenOption

**Source:** `java.base\java\nio\file\StandardOpenOption.html`

### Class Description

```java
public enum
StandardOpenOption

extends
Enum
<
StandardOpenOption
>
implements
OpenOption
```

Defines the standard open options.

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardOpenOption

>

,

OpenOption

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StandardOpenOption
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOpenOption c : StandardOpenOption.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
StandardOpenOption
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

#### Enum StandardOpenOption

java.lang.Object

- java.lang.Enum

<

StandardOpenOption

>
- - java.nio.file.StandardOpenOption

java.lang.Enum

<

StandardOpenOption

>

- java.nio.file.StandardOpenOption

java.nio.file.StandardOpenOption

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardOpenOption

>

,

OpenOption

```java
public enum
StandardOpenOption

extends
Enum
<
StandardOpenOption
>
implements
OpenOption
```

Defines the standard open options.

**Since:** 1.7

public enum

StandardOpenOption

extends

Enum

<

StandardOpenOption

>
implements

OpenOption

Defines the standard open options.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

APPEND

If the file is opened for

WRITE

access then bytes will be written
to the end of the file rather than the beginning.

CREATE

Create a new file if it does not exist.

CREATE_NEW

Create a new file, failing if the file already exists.

DELETE_ON_CLOSE

Delete on close.

DSYNC

Requires that every update to the file's content be written
synchronously to the underlying storage device.

READ

Open for read access.

SPARSE

Sparse file.

SYNC

Requires that every update to the file's content or metadata be written
synchronously to the underlying storage device.

TRUNCATE_EXISTING

If the file already exists and it is opened for

WRITE

access, then its length is truncated to 0.

WRITE

Open for write access.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardOpenOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardOpenOption

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

APPEND

If the file is opened for

WRITE

access then bytes will be written
to the end of the file rather than the beginning.

CREATE

Create a new file if it does not exist.

CREATE_NEW

Create a new file, failing if the file already exists.

DELETE_ON_CLOSE

Delete on close.

DSYNC

Requires that every update to the file's content be written
synchronously to the underlying storage device.

READ

Open for read access.

SPARSE

Sparse file.

SYNC

Requires that every update to the file's content or metadata be written
synchronously to the underlying storage device.

TRUNCATE_EXISTING

If the file already exists and it is opened for

WRITE

access, then its length is truncated to 0.

WRITE

Open for write access.

---

#### Enum Constant Summary

If the file is opened for

WRITE

access then bytes will be written
to the end of the file rather than the beginning.

Create a new file if it does not exist.

Create a new file, failing if the file already exists.

Delete on close.

Requires that every update to the file's content be written
synchronously to the underlying storage device.

Open for read access.

Sparse file.

Requires that every update to the file's content or metadata be written
synchronously to the underlying storage device.

If the file already exists and it is opened for

WRITE

access, then its length is truncated to 0.

Open for write access.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardOpenOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardOpenOption

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

- READ

```java
public static final
StandardOpenOption
READ
```

Open for read access.

- WRITE

```java
public static final
StandardOpenOption
WRITE
```

Open for write access.

- APPEND

```java
public static final
StandardOpenOption
APPEND
```

If the file is opened for

WRITE

access then bytes will be written
to the end of the file rather than the beginning.

If the file is opened for write access by other programs, then it
is file system specific if writing to the end of the file is atomic.

- TRUNCATE_EXISTING

```java
public static final
StandardOpenOption
TRUNCATE_EXISTING
```

If the file already exists and it is opened for

WRITE

access, then its length is truncated to 0. This option is ignored
if the file is opened only for

READ

access.

- CREATE

```java
public static final
StandardOpenOption
CREATE
```

Create a new file if it does not exist.
This option is ignored if the

CREATE_NEW

option is also set.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

- CREATE_NEW

```java
public static final
StandardOpenOption
CREATE_NEW
```

Create a new file, failing if the file already exists.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

- DELETE_ON_CLOSE

```java
public static final
StandardOpenOption
DELETE_ON_CLOSE
```

Delete on close. When this option is present then the implementation
makes a

best effort

attempt to delete the file when closed
by the appropriate

close

method. If the

close

method is
not invoked then a

best effort

attempt is made to delete the
file when the Java virtual machine terminates (either normally, as
defined by the Java Language Specification, or where possible, abnormally).
This option is primarily intended for use with

work files

that
are used solely by a single instance of the Java virtual machine. This
option is not recommended for use when opening files that are open
concurrently by other entities. Many of the details as to when and how
the file is deleted are implementation specific and therefore not
specified. In particular, an implementation may be unable to guarantee
that it deletes the expected file when replaced by an attacker while the
file is open. Consequently, security sensitive applications should take
care when using this option.

For security reasons, this option may imply the

LinkOption.NOFOLLOW_LINKS

option. In other words, if the option is present
when opening an existing file that is a symbolic link then it may fail
(by throwing

IOException

).

- SPARSE

```java
public static final
StandardOpenOption
SPARSE
```

Sparse file. When used with the

CREATE_NEW

option then this
option provides a

hint

that the new file will be sparse. The
option is ignored when the file system does not support the creation of
sparse files.

- SYNC

```java
public static final
StandardOpenOption
SYNC
```

Requires that every update to the file's content or metadata be written
synchronously to the underlying storage device.

**See Also:** Synchronized I/O file integrity

- DSYNC

```java
public static final
StandardOpenOption
DSYNC
```

Requires that every update to the file's content be written
synchronously to the underlying storage device.

**See Also:** Synchronized I/O file integrity

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
StandardOpenOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOpenOption c : StandardOpenOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardOpenOption
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

- READ

```java
public static final
StandardOpenOption
READ
```

Open for read access.

- WRITE

```java
public static final
StandardOpenOption
WRITE
```

Open for write access.

- APPEND

```java
public static final
StandardOpenOption
APPEND
```

If the file is opened for

WRITE

access then bytes will be written
to the end of the file rather than the beginning.

If the file is opened for write access by other programs, then it
is file system specific if writing to the end of the file is atomic.

- TRUNCATE_EXISTING

```java
public static final
StandardOpenOption
TRUNCATE_EXISTING
```

If the file already exists and it is opened for

WRITE

access, then its length is truncated to 0. This option is ignored
if the file is opened only for

READ

access.

- CREATE

```java
public static final
StandardOpenOption
CREATE
```

Create a new file if it does not exist.
This option is ignored if the

CREATE_NEW

option is also set.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

- CREATE_NEW

```java
public static final
StandardOpenOption
CREATE_NEW
```

Create a new file, failing if the file already exists.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

- DELETE_ON_CLOSE

```java
public static final
StandardOpenOption
DELETE_ON_CLOSE
```

Delete on close. When this option is present then the implementation
makes a

best effort

attempt to delete the file when closed
by the appropriate

close

method. If the

close

method is
not invoked then a

best effort

attempt is made to delete the
file when the Java virtual machine terminates (either normally, as
defined by the Java Language Specification, or where possible, abnormally).
This option is primarily intended for use with

work files

that
are used solely by a single instance of the Java virtual machine. This
option is not recommended for use when opening files that are open
concurrently by other entities. Many of the details as to when and how
the file is deleted are implementation specific and therefore not
specified. In particular, an implementation may be unable to guarantee
that it deletes the expected file when replaced by an attacker while the
file is open. Consequently, security sensitive applications should take
care when using this option.

For security reasons, this option may imply the

LinkOption.NOFOLLOW_LINKS

option. In other words, if the option is present
when opening an existing file that is a symbolic link then it may fail
(by throwing

IOException

).

- SPARSE

```java
public static final
StandardOpenOption
SPARSE
```

Sparse file. When used with the

CREATE_NEW

option then this
option provides a

hint

that the new file will be sparse. The
option is ignored when the file system does not support the creation of
sparse files.

- SYNC

```java
public static final
StandardOpenOption
SYNC
```

Requires that every update to the file's content or metadata be written
synchronously to the underlying storage device.

**See Also:** Synchronized I/O file integrity

- DSYNC

```java
public static final
StandardOpenOption
DSYNC
```

Requires that every update to the file's content be written
synchronously to the underlying storage device.

**See Also:** Synchronized I/O file integrity

---

#### Enum Constant Detail

READ

```java
public static final
StandardOpenOption
READ
```

Open for read access.

---

#### READ

public static final

StandardOpenOption

READ

Open for read access.

WRITE

```java
public static final
StandardOpenOption
WRITE
```

Open for write access.

---

#### WRITE

public static final

StandardOpenOption

WRITE

Open for write access.

APPEND

```java
public static final
StandardOpenOption
APPEND
```

If the file is opened for

WRITE

access then bytes will be written
to the end of the file rather than the beginning.

If the file is opened for write access by other programs, then it
is file system specific if writing to the end of the file is atomic.

---

#### APPEND

public static final

StandardOpenOption

APPEND

If the file is opened for

WRITE

access then bytes will be written
to the end of the file rather than the beginning.

If the file is opened for write access by other programs, then it
is file system specific if writing to the end of the file is atomic.

If the file is opened for write access by other programs, then it
is file system specific if writing to the end of the file is atomic.

TRUNCATE_EXISTING

```java
public static final
StandardOpenOption
TRUNCATE_EXISTING
```

If the file already exists and it is opened for

WRITE

access, then its length is truncated to 0. This option is ignored
if the file is opened only for

READ

access.

---

#### TRUNCATE_EXISTING

public static final

StandardOpenOption

TRUNCATE_EXISTING

If the file already exists and it is opened for

WRITE

access, then its length is truncated to 0. This option is ignored
if the file is opened only for

READ

access.

CREATE

```java
public static final
StandardOpenOption
CREATE
```

Create a new file if it does not exist.
This option is ignored if the

CREATE_NEW

option is also set.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

---

#### CREATE

public static final

StandardOpenOption

CREATE

Create a new file if it does not exist.
This option is ignored if the

CREATE_NEW

option is also set.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

CREATE_NEW

```java
public static final
StandardOpenOption
CREATE_NEW
```

Create a new file, failing if the file already exists.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

---

#### CREATE_NEW

public static final

StandardOpenOption

CREATE_NEW

Create a new file, failing if the file already exists.
The check for the existence of the file and the creation of the file
if it does not exist is atomic with respect to other file system
operations.

DELETE_ON_CLOSE

```java
public static final
StandardOpenOption
DELETE_ON_CLOSE
```

Delete on close. When this option is present then the implementation
makes a

best effort

attempt to delete the file when closed
by the appropriate

close

method. If the

close

method is
not invoked then a

best effort

attempt is made to delete the
file when the Java virtual machine terminates (either normally, as
defined by the Java Language Specification, or where possible, abnormally).
This option is primarily intended for use with

work files

that
are used solely by a single instance of the Java virtual machine. This
option is not recommended for use when opening files that are open
concurrently by other entities. Many of the details as to when and how
the file is deleted are implementation specific and therefore not
specified. In particular, an implementation may be unable to guarantee
that it deletes the expected file when replaced by an attacker while the
file is open. Consequently, security sensitive applications should take
care when using this option.

For security reasons, this option may imply the

LinkOption.NOFOLLOW_LINKS

option. In other words, if the option is present
when opening an existing file that is a symbolic link then it may fail
(by throwing

IOException

).

---

#### DELETE_ON_CLOSE

public static final

StandardOpenOption

DELETE_ON_CLOSE

Delete on close. When this option is present then the implementation
makes a

best effort

attempt to delete the file when closed
by the appropriate

close

method. If the

close

method is
not invoked then a

best effort

attempt is made to delete the
file when the Java virtual machine terminates (either normally, as
defined by the Java Language Specification, or where possible, abnormally).
This option is primarily intended for use with

work files

that
are used solely by a single instance of the Java virtual machine. This
option is not recommended for use when opening files that are open
concurrently by other entities. Many of the details as to when and how
the file is deleted are implementation specific and therefore not
specified. In particular, an implementation may be unable to guarantee
that it deletes the expected file when replaced by an attacker while the
file is open. Consequently, security sensitive applications should take
care when using this option.

For security reasons, this option may imply the

LinkOption.NOFOLLOW_LINKS

option. In other words, if the option is present
when opening an existing file that is a symbolic link then it may fail
(by throwing

IOException

).

For security reasons, this option may imply the

LinkOption.NOFOLLOW_LINKS

option. In other words, if the option is present
when opening an existing file that is a symbolic link then it may fail
(by throwing

IOException

).

SPARSE

```java
public static final
StandardOpenOption
SPARSE
```

Sparse file. When used with the

CREATE_NEW

option then this
option provides a

hint

that the new file will be sparse. The
option is ignored when the file system does not support the creation of
sparse files.

---

#### SPARSE

public static final

StandardOpenOption

SPARSE

Sparse file. When used with the

CREATE_NEW

option then this
option provides a

hint

that the new file will be sparse. The
option is ignored when the file system does not support the creation of
sparse files.

SYNC

```java
public static final
StandardOpenOption
SYNC
```

Requires that every update to the file's content or metadata be written
synchronously to the underlying storage device.

**See Also:** Synchronized I/O file integrity

---

#### SYNC

public static final

StandardOpenOption

SYNC

Requires that every update to the file's content or metadata be written
synchronously to the underlying storage device.

DSYNC

```java
public static final
StandardOpenOption
DSYNC
```

Requires that every update to the file's content be written
synchronously to the underlying storage device.

**See Also:** Synchronized I/O file integrity

---

#### DSYNC

public static final

StandardOpenOption

DSYNC

Requires that every update to the file's content be written
synchronously to the underlying storage device.

Method Detail

- values

```java
public static
StandardOpenOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOpenOption c : StandardOpenOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardOpenOption
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
StandardOpenOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOpenOption c : StandardOpenOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

StandardOpenOption

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOpenOption c : StandardOpenOption.values())
System.out.println(c);
```

for (StandardOpenOption c : StandardOpenOption.values())
System.out.println(c);

valueOf

```java
public static
StandardOpenOption
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

StandardOpenOption

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

