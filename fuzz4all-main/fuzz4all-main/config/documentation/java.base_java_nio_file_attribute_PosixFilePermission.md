# Enum PosixFilePermission

**Source:** `java.base\java\nio\file\attribute\PosixFilePermission.html`

### Class Description

```java
public enum
PosixFilePermission

extends
Enum
<
PosixFilePermission
>
```

Defines the bits for use with the

permissions

attribute.

The

PosixFilePermissions

class defines methods for manipulating
set of permissions.

**All Implemented Interfaces:** Serializable

,

Comparable

<

PosixFilePermission

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
PosixFilePermission
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PosixFilePermission c : PosixFilePermission.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
PosixFilePermission
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

#### Enum PosixFilePermission

java.lang.Object

- java.lang.Enum

<

PosixFilePermission

>
- - java.nio.file.attribute.PosixFilePermission

java.lang.Enum

<

PosixFilePermission

>

- java.nio.file.attribute.PosixFilePermission

java.nio.file.attribute.PosixFilePermission

**All Implemented Interfaces:** Serializable

,

Comparable

<

PosixFilePermission

>

```java
public enum
PosixFilePermission

extends
Enum
<
PosixFilePermission
>
```

Defines the bits for use with the

permissions

attribute.

The

PosixFilePermissions

class defines methods for manipulating
set of permissions.

**Since:** 1.7

public enum

PosixFilePermission

extends

Enum

<

PosixFilePermission

>

Defines the bits for use with the

permissions

attribute.

The

PosixFilePermissions

class defines methods for manipulating
set of permissions.

The

PosixFilePermissions

class defines methods for manipulating
set of permissions.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

GROUP_EXECUTE

Execute/search permission, group.

GROUP_READ

Read permission, group.

GROUP_WRITE

Write permission, group.

OTHERS_EXECUTE

Execute/search permission, others.

OTHERS_READ

Read permission, others.

OTHERS_WRITE

Write permission, others.

OWNER_EXECUTE

Execute/search permission, owner.

OWNER_READ

Read permission, owner.

OWNER_WRITE

Write permission, owner.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PosixFilePermission

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PosixFilePermission

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

GROUP_EXECUTE

Execute/search permission, group.

GROUP_READ

Read permission, group.

GROUP_WRITE

Write permission, group.

OTHERS_EXECUTE

Execute/search permission, others.

OTHERS_READ

Read permission, others.

OTHERS_WRITE

Write permission, others.

OWNER_EXECUTE

Execute/search permission, owner.

OWNER_READ

Read permission, owner.

OWNER_WRITE

Write permission, owner.

---

#### Enum Constant Summary

Execute/search permission, group.

Read permission, group.

Write permission, group.

Execute/search permission, others.

Read permission, others.

Write permission, others.

Execute/search permission, owner.

Read permission, owner.

Write permission, owner.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PosixFilePermission

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PosixFilePermission

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

- OWNER_READ

```java
public static final
PosixFilePermission
OWNER_READ
```

Read permission, owner.

- OWNER_WRITE

```java
public static final
PosixFilePermission
OWNER_WRITE
```

Write permission, owner.

- OWNER_EXECUTE

```java
public static final
PosixFilePermission
OWNER_EXECUTE
```

Execute/search permission, owner.

- GROUP_READ

```java
public static final
PosixFilePermission
GROUP_READ
```

Read permission, group.

- GROUP_WRITE

```java
public static final
PosixFilePermission
GROUP_WRITE
```

Write permission, group.

- GROUP_EXECUTE

```java
public static final
PosixFilePermission
GROUP_EXECUTE
```

Execute/search permission, group.

- OTHERS_READ

```java
public static final
PosixFilePermission
OTHERS_READ
```

Read permission, others.

- OTHERS_WRITE

```java
public static final
PosixFilePermission
OTHERS_WRITE
```

Write permission, others.

- OTHERS_EXECUTE

```java
public static final
PosixFilePermission
OTHERS_EXECUTE
```

Execute/search permission, others.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
PosixFilePermission
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PosixFilePermission c : PosixFilePermission.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PosixFilePermission
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

- OWNER_READ

```java
public static final
PosixFilePermission
OWNER_READ
```

Read permission, owner.

- OWNER_WRITE

```java
public static final
PosixFilePermission
OWNER_WRITE
```

Write permission, owner.

- OWNER_EXECUTE

```java
public static final
PosixFilePermission
OWNER_EXECUTE
```

Execute/search permission, owner.

- GROUP_READ

```java
public static final
PosixFilePermission
GROUP_READ
```

Read permission, group.

- GROUP_WRITE

```java
public static final
PosixFilePermission
GROUP_WRITE
```

Write permission, group.

- GROUP_EXECUTE

```java
public static final
PosixFilePermission
GROUP_EXECUTE
```

Execute/search permission, group.

- OTHERS_READ

```java
public static final
PosixFilePermission
OTHERS_READ
```

Read permission, others.

- OTHERS_WRITE

```java
public static final
PosixFilePermission
OTHERS_WRITE
```

Write permission, others.

- OTHERS_EXECUTE

```java
public static final
PosixFilePermission
OTHERS_EXECUTE
```

Execute/search permission, others.

---

#### Enum Constant Detail

OWNER_READ

```java
public static final
PosixFilePermission
OWNER_READ
```

Read permission, owner.

---

#### OWNER_READ

public static final

PosixFilePermission

OWNER_READ

Read permission, owner.

OWNER_WRITE

```java
public static final
PosixFilePermission
OWNER_WRITE
```

Write permission, owner.

---

#### OWNER_WRITE

public static final

PosixFilePermission

OWNER_WRITE

Write permission, owner.

OWNER_EXECUTE

```java
public static final
PosixFilePermission
OWNER_EXECUTE
```

Execute/search permission, owner.

---

#### OWNER_EXECUTE

public static final

PosixFilePermission

OWNER_EXECUTE

Execute/search permission, owner.

GROUP_READ

```java
public static final
PosixFilePermission
GROUP_READ
```

Read permission, group.

---

#### GROUP_READ

public static final

PosixFilePermission

GROUP_READ

Read permission, group.

GROUP_WRITE

```java
public static final
PosixFilePermission
GROUP_WRITE
```

Write permission, group.

---

#### GROUP_WRITE

public static final

PosixFilePermission

GROUP_WRITE

Write permission, group.

GROUP_EXECUTE

```java
public static final
PosixFilePermission
GROUP_EXECUTE
```

Execute/search permission, group.

---

#### GROUP_EXECUTE

public static final

PosixFilePermission

GROUP_EXECUTE

Execute/search permission, group.

OTHERS_READ

```java
public static final
PosixFilePermission
OTHERS_READ
```

Read permission, others.

---

#### OTHERS_READ

public static final

PosixFilePermission

OTHERS_READ

Read permission, others.

OTHERS_WRITE

```java
public static final
PosixFilePermission
OTHERS_WRITE
```

Write permission, others.

---

#### OTHERS_WRITE

public static final

PosixFilePermission

OTHERS_WRITE

Write permission, others.

OTHERS_EXECUTE

```java
public static final
PosixFilePermission
OTHERS_EXECUTE
```

Execute/search permission, others.

---

#### OTHERS_EXECUTE

public static final

PosixFilePermission

OTHERS_EXECUTE

Execute/search permission, others.

Method Detail

- values

```java
public static
PosixFilePermission
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PosixFilePermission c : PosixFilePermission.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PosixFilePermission
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
PosixFilePermission
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PosixFilePermission c : PosixFilePermission.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

PosixFilePermission

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PosixFilePermission c : PosixFilePermission.values())
System.out.println(c);
```

for (PosixFilePermission c : PosixFilePermission.values())
System.out.println(c);

valueOf

```java
public static
PosixFilePermission
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

PosixFilePermission

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

