# Enum LinkOption

**Source:** `java.base\java\nio\file\LinkOption.html`

### Class Description

```java
public enum
LinkOption

extends
Enum
<
LinkOption
>
implements
OpenOption
,
CopyOption
```

Defines the options as to how symbolic links are handled.

**All Implemented Interfaces:** Serializable

,

Comparable

<

LinkOption

>

,

CopyOption

,

OpenOption

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
LinkOption
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LinkOption c : LinkOption.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
LinkOption
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

#### Enum LinkOption

java.lang.Object

- java.lang.Enum

<

LinkOption

>
- - java.nio.file.LinkOption

java.lang.Enum

<

LinkOption

>

- java.nio.file.LinkOption

java.nio.file.LinkOption

**All Implemented Interfaces:** Serializable

,

Comparable

<

LinkOption

>

,

CopyOption

,

OpenOption

```java
public enum
LinkOption

extends
Enum
<
LinkOption
>
implements
OpenOption
,
CopyOption
```

Defines the options as to how symbolic links are handled.

**Since:** 1.7

public enum

LinkOption

extends

Enum

<

LinkOption

>
implements

OpenOption

,

CopyOption

Defines the options as to how symbolic links are handled.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

NOFOLLOW_LINKS

Do not follow symbolic links.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

LinkOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

LinkOption

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

NOFOLLOW_LINKS

Do not follow symbolic links.

---

#### Enum Constant Summary

Do not follow symbolic links.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

LinkOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

LinkOption

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

- NOFOLLOW_LINKS

```java
public static final
LinkOption
NOFOLLOW_LINKS
```

Do not follow symbolic links.

**See Also:** Files.getFileAttributeView(Path,Class,LinkOption[])

,

Files.copy(java.nio.file.Path, java.nio.file.Path, java.nio.file.CopyOption...)

,

SecureDirectoryStream.newByteChannel(T, java.util.Set<? extends java.nio.file.OpenOption>, java.nio.file.attribute.FileAttribute<?>...)

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
LinkOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LinkOption c : LinkOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LinkOption
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

- NOFOLLOW_LINKS

```java
public static final
LinkOption
NOFOLLOW_LINKS
```

Do not follow symbolic links.

**See Also:** Files.getFileAttributeView(Path,Class,LinkOption[])

,

Files.copy(java.nio.file.Path, java.nio.file.Path, java.nio.file.CopyOption...)

,

SecureDirectoryStream.newByteChannel(T, java.util.Set<? extends java.nio.file.OpenOption>, java.nio.file.attribute.FileAttribute<?>...)

---

#### Enum Constant Detail

NOFOLLOW_LINKS

```java
public static final
LinkOption
NOFOLLOW_LINKS
```

Do not follow symbolic links.

**See Also:** Files.getFileAttributeView(Path,Class,LinkOption[])

,

Files.copy(java.nio.file.Path, java.nio.file.Path, java.nio.file.CopyOption...)

,

SecureDirectoryStream.newByteChannel(T, java.util.Set<? extends java.nio.file.OpenOption>, java.nio.file.attribute.FileAttribute<?>...)

---

#### NOFOLLOW_LINKS

public static final

LinkOption

NOFOLLOW_LINKS

Do not follow symbolic links.

Method Detail

- values

```java
public static
LinkOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LinkOption c : LinkOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LinkOption
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
LinkOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LinkOption c : LinkOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

LinkOption

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LinkOption c : LinkOption.values())
System.out.println(c);
```

for (LinkOption c : LinkOption.values())
System.out.println(c);

valueOf

```java
public static
LinkOption
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

LinkOption

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

