# Enum FileVisitOption

**Source:** `java.base\java\nio\file\FileVisitOption.html`

### Class Description

```java
public enum
FileVisitOption

extends
Enum
<
FileVisitOption
>
```

Defines the file tree traversal options.

**All Implemented Interfaces:** Serializable

,

Comparable

<

FileVisitOption

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
FileVisitOption
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitOption c : FileVisitOption.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
FileVisitOption
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

#### Enum FileVisitOption

java.lang.Object

- java.lang.Enum

<

FileVisitOption

>
- - java.nio.file.FileVisitOption

java.lang.Enum

<

FileVisitOption

>

- java.nio.file.FileVisitOption

java.nio.file.FileVisitOption

**All Implemented Interfaces:** Serializable

,

Comparable

<

FileVisitOption

>

```java
public enum
FileVisitOption

extends
Enum
<
FileVisitOption
>
```

Defines the file tree traversal options.

**Since:** 1.7
**See Also:** Files.walkFileTree(java.nio.file.Path, java.util.Set<java.nio.file.FileVisitOption>, int, java.nio.file.FileVisitor<? super java.nio.file.Path>)

public enum

FileVisitOption

extends

Enum

<

FileVisitOption

>

Defines the file tree traversal options.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

FOLLOW_LINKS

Follow symbolic links.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FileVisitOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

FileVisitOption

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

FOLLOW_LINKS

Follow symbolic links.

---

#### Enum Constant Summary

Follow symbolic links.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FileVisitOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

FileVisitOption

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

- FOLLOW_LINKS

```java
public static final
FileVisitOption
FOLLOW_LINKS
```

Follow symbolic links.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
FileVisitOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitOption c : FileVisitOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
FileVisitOption
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

- FOLLOW_LINKS

```java
public static final
FileVisitOption
FOLLOW_LINKS
```

Follow symbolic links.

---

#### Enum Constant Detail

FOLLOW_LINKS

```java
public static final
FileVisitOption
FOLLOW_LINKS
```

Follow symbolic links.

---

#### FOLLOW_LINKS

public static final

FileVisitOption

FOLLOW_LINKS

Follow symbolic links.

Method Detail

- values

```java
public static
FileVisitOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitOption c : FileVisitOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
FileVisitOption
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
FileVisitOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitOption c : FileVisitOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

FileVisitOption

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitOption c : FileVisitOption.values())
System.out.println(c);
```

for (FileVisitOption c : FileVisitOption.values())
System.out.println(c);

valueOf

```java
public static
FileVisitOption
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

FileVisitOption

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

