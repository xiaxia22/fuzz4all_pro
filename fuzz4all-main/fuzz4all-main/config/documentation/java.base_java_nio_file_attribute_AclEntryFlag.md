# Enum AclEntryFlag

**Source:** `java.base\java\nio\file\attribute\AclEntryFlag.html`

### Class Description

```java
public enum
AclEntryFlag

extends
Enum
<
AclEntryFlag
>
```

Defines the flags for used by the flags component of an ACL

entry

.

In this release, this class does not define flags related to

AclEntryType.AUDIT

and

AclEntryType.ALARM

entry types.

**All Implemented Interfaces:** Serializable

,

Comparable

<

AclEntryFlag

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
AclEntryFlag
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryFlag c : AclEntryFlag.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
AclEntryFlag
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

#### Enum AclEntryFlag

java.lang.Object

- java.lang.Enum

<

AclEntryFlag

>
- - java.nio.file.attribute.AclEntryFlag

java.lang.Enum

<

AclEntryFlag

>

- java.nio.file.attribute.AclEntryFlag

java.nio.file.attribute.AclEntryFlag

**All Implemented Interfaces:** Serializable

,

Comparable

<

AclEntryFlag

>

```java
public enum
AclEntryFlag

extends
Enum
<
AclEntryFlag
>
```

Defines the flags for used by the flags component of an ACL

entry

.

In this release, this class does not define flags related to

AclEntryType.AUDIT

and

AclEntryType.ALARM

entry types.

**Since:** 1.7

public enum

AclEntryFlag

extends

Enum

<

AclEntryFlag

>

Defines the flags for used by the flags component of an ACL

entry

.

In this release, this class does not define flags related to

AclEntryType.AUDIT

and

AclEntryType.ALARM

entry types.

In this release, this class does not define flags related to

AclEntryType.AUDIT

and

AclEntryType.ALARM

entry types.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DIRECTORY_INHERIT

Can be placed on a directory and indicates that the ACL entry should be
added to each new directory created.

FILE_INHERIT

Can be placed on a directory and indicates that the ACL entry should be
added to each new non-directory file created.

INHERIT_ONLY

Can be placed on a directory but does not apply to the directory,
only to newly created files/directories as specified by the

FILE_INHERIT

and

DIRECTORY_INHERIT

flags.

NO_PROPAGATE_INHERIT

Can be placed on a directory to indicate that the ACL entry should not
be placed on the newly created directory which is inheritable by
subdirectories of the created directory.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AclEntryFlag

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AclEntryFlag

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

DIRECTORY_INHERIT

Can be placed on a directory and indicates that the ACL entry should be
added to each new directory created.

FILE_INHERIT

Can be placed on a directory and indicates that the ACL entry should be
added to each new non-directory file created.

INHERIT_ONLY

Can be placed on a directory but does not apply to the directory,
only to newly created files/directories as specified by the

FILE_INHERIT

and

DIRECTORY_INHERIT

flags.

NO_PROPAGATE_INHERIT

Can be placed on a directory to indicate that the ACL entry should not
be placed on the newly created directory which is inheritable by
subdirectories of the created directory.

---

#### Enum Constant Summary

Can be placed on a directory and indicates that the ACL entry should be
added to each new directory created.

Can be placed on a directory and indicates that the ACL entry should be
added to each new non-directory file created.

Can be placed on a directory but does not apply to the directory,
only to newly created files/directories as specified by the

FILE_INHERIT

and

DIRECTORY_INHERIT

flags.

Can be placed on a directory to indicate that the ACL entry should not
be placed on the newly created directory which is inheritable by
subdirectories of the created directory.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AclEntryFlag

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AclEntryFlag

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

- FILE_INHERIT

```java
public static final
AclEntryFlag
FILE_INHERIT
```

Can be placed on a directory and indicates that the ACL entry should be
added to each new non-directory file created.

- DIRECTORY_INHERIT

```java
public static final
AclEntryFlag
DIRECTORY_INHERIT
```

Can be placed on a directory and indicates that the ACL entry should be
added to each new directory created.

- NO_PROPAGATE_INHERIT

```java
public static final
AclEntryFlag
NO_PROPAGATE_INHERIT
```

Can be placed on a directory to indicate that the ACL entry should not
be placed on the newly created directory which is inheritable by
subdirectories of the created directory.

- INHERIT_ONLY

```java
public static final
AclEntryFlag
INHERIT_ONLY
```

Can be placed on a directory but does not apply to the directory,
only to newly created files/directories as specified by the

FILE_INHERIT

and

DIRECTORY_INHERIT

flags.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
AclEntryFlag
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryFlag c : AclEntryFlag.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AclEntryFlag
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

- FILE_INHERIT

```java
public static final
AclEntryFlag
FILE_INHERIT
```

Can be placed on a directory and indicates that the ACL entry should be
added to each new non-directory file created.

- DIRECTORY_INHERIT

```java
public static final
AclEntryFlag
DIRECTORY_INHERIT
```

Can be placed on a directory and indicates that the ACL entry should be
added to each new directory created.

- NO_PROPAGATE_INHERIT

```java
public static final
AclEntryFlag
NO_PROPAGATE_INHERIT
```

Can be placed on a directory to indicate that the ACL entry should not
be placed on the newly created directory which is inheritable by
subdirectories of the created directory.

- INHERIT_ONLY

```java
public static final
AclEntryFlag
INHERIT_ONLY
```

Can be placed on a directory but does not apply to the directory,
only to newly created files/directories as specified by the

FILE_INHERIT

and

DIRECTORY_INHERIT

flags.

---

#### Enum Constant Detail

FILE_INHERIT

```java
public static final
AclEntryFlag
FILE_INHERIT
```

Can be placed on a directory and indicates that the ACL entry should be
added to each new non-directory file created.

---

#### FILE_INHERIT

public static final

AclEntryFlag

FILE_INHERIT

Can be placed on a directory and indicates that the ACL entry should be
added to each new non-directory file created.

DIRECTORY_INHERIT

```java
public static final
AclEntryFlag
DIRECTORY_INHERIT
```

Can be placed on a directory and indicates that the ACL entry should be
added to each new directory created.

---

#### DIRECTORY_INHERIT

public static final

AclEntryFlag

DIRECTORY_INHERIT

Can be placed on a directory and indicates that the ACL entry should be
added to each new directory created.

NO_PROPAGATE_INHERIT

```java
public static final
AclEntryFlag
NO_PROPAGATE_INHERIT
```

Can be placed on a directory to indicate that the ACL entry should not
be placed on the newly created directory which is inheritable by
subdirectories of the created directory.

---

#### NO_PROPAGATE_INHERIT

public static final

AclEntryFlag

NO_PROPAGATE_INHERIT

Can be placed on a directory to indicate that the ACL entry should not
be placed on the newly created directory which is inheritable by
subdirectories of the created directory.

INHERIT_ONLY

```java
public static final
AclEntryFlag
INHERIT_ONLY
```

Can be placed on a directory but does not apply to the directory,
only to newly created files/directories as specified by the

FILE_INHERIT

and

DIRECTORY_INHERIT

flags.

---

#### INHERIT_ONLY

public static final

AclEntryFlag

INHERIT_ONLY

Can be placed on a directory but does not apply to the directory,
only to newly created files/directories as specified by the

FILE_INHERIT

and

DIRECTORY_INHERIT

flags.

Method Detail

- values

```java
public static
AclEntryFlag
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryFlag c : AclEntryFlag.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AclEntryFlag
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
AclEntryFlag
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryFlag c : AclEntryFlag.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

AclEntryFlag

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryFlag c : AclEntryFlag.values())
System.out.println(c);
```

for (AclEntryFlag c : AclEntryFlag.values())
System.out.println(c);

valueOf

```java
public static
AclEntryFlag
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

AclEntryFlag

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

