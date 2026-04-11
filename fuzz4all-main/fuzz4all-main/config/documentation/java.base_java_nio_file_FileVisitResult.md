# Enum FileVisitResult

**Source:** `java.base\java\nio\file\FileVisitResult.html`

### Class Description

```java
public enum
FileVisitResult

extends
Enum
<
FileVisitResult
>
```

The result type of a

FileVisitor

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

FileVisitResult

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
FileVisitResult
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitResult c : FileVisitResult.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
FileVisitResult
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

#### Enum FileVisitResult

java.lang.Object

- java.lang.Enum

<

FileVisitResult

>
- - java.nio.file.FileVisitResult

java.lang.Enum

<

FileVisitResult

>

- java.nio.file.FileVisitResult

java.nio.file.FileVisitResult

**All Implemented Interfaces:** Serializable

,

Comparable

<

FileVisitResult

>

```java
public enum
FileVisitResult

extends
Enum
<
FileVisitResult
>
```

The result type of a

FileVisitor

.

**Since:** 1.7
**See Also:** Files.walkFileTree(java.nio.file.Path, java.util.Set<java.nio.file.FileVisitOption>, int, java.nio.file.FileVisitor<? super java.nio.file.Path>)

public enum

FileVisitResult

extends

Enum

<

FileVisitResult

>

The result type of a

FileVisitor

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CONTINUE

Continue.

SKIP_SIBLINGS

Continue without visiting the

siblings

of this file or directory.

SKIP_SUBTREE

Continue without visiting the entries in this directory.

TERMINATE

Terminate.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FileVisitResult

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

FileVisitResult

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

CONTINUE

Continue.

SKIP_SIBLINGS

Continue without visiting the

siblings

of this file or directory.

SKIP_SUBTREE

Continue without visiting the entries in this directory.

TERMINATE

Terminate.

---

#### Enum Constant Summary

Continue.

Continue without visiting the

siblings

of this file or directory.

Continue without visiting the entries in this directory.

Terminate.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FileVisitResult

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

FileVisitResult

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

- CONTINUE

```java
public static final
FileVisitResult
CONTINUE
```

Continue. When returned from a

preVisitDirectory

method then the entries in the directory should also
be visited.

- TERMINATE

```java
public static final
FileVisitResult
TERMINATE
```

Terminate.

- SKIP_SUBTREE

```java
public static final
FileVisitResult
SKIP_SUBTREE
```

Continue without visiting the entries in this directory. This result
is only meaningful when returned from the

preVisitDirectory

method; otherwise
this result type is the same as returning

CONTINUE

.

- SKIP_SIBLINGS

```java
public static final
FileVisitResult
SKIP_SIBLINGS
```

Continue without visiting the

siblings

of this file or directory.
If returned from the

preVisitDirectory

method then the entries in the directory are also
skipped and the

postVisitDirectory

method is not invoked.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
FileVisitResult
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitResult c : FileVisitResult.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
FileVisitResult
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

- CONTINUE

```java
public static final
FileVisitResult
CONTINUE
```

Continue. When returned from a

preVisitDirectory

method then the entries in the directory should also
be visited.

- TERMINATE

```java
public static final
FileVisitResult
TERMINATE
```

Terminate.

- SKIP_SUBTREE

```java
public static final
FileVisitResult
SKIP_SUBTREE
```

Continue without visiting the entries in this directory. This result
is only meaningful when returned from the

preVisitDirectory

method; otherwise
this result type is the same as returning

CONTINUE

.

- SKIP_SIBLINGS

```java
public static final
FileVisitResult
SKIP_SIBLINGS
```

Continue without visiting the

siblings

of this file or directory.
If returned from the

preVisitDirectory

method then the entries in the directory are also
skipped and the

postVisitDirectory

method is not invoked.

---

#### Enum Constant Detail

CONTINUE

```java
public static final
FileVisitResult
CONTINUE
```

Continue. When returned from a

preVisitDirectory

method then the entries in the directory should also
be visited.

---

#### CONTINUE

public static final

FileVisitResult

CONTINUE

Continue. When returned from a

preVisitDirectory

method then the entries in the directory should also
be visited.

TERMINATE

```java
public static final
FileVisitResult
TERMINATE
```

Terminate.

---

#### TERMINATE

public static final

FileVisitResult

TERMINATE

Terminate.

SKIP_SUBTREE

```java
public static final
FileVisitResult
SKIP_SUBTREE
```

Continue without visiting the entries in this directory. This result
is only meaningful when returned from the

preVisitDirectory

method; otherwise
this result type is the same as returning

CONTINUE

.

---

#### SKIP_SUBTREE

public static final

FileVisitResult

SKIP_SUBTREE

Continue without visiting the entries in this directory. This result
is only meaningful when returned from the

preVisitDirectory

method; otherwise
this result type is the same as returning

CONTINUE

.

SKIP_SIBLINGS

```java
public static final
FileVisitResult
SKIP_SIBLINGS
```

Continue without visiting the

siblings

of this file or directory.
If returned from the

preVisitDirectory

method then the entries in the directory are also
skipped and the

postVisitDirectory

method is not invoked.

---

#### SKIP_SIBLINGS

public static final

FileVisitResult

SKIP_SIBLINGS

Continue without visiting the

siblings

of this file or directory.
If returned from the

preVisitDirectory

method then the entries in the directory are also
skipped and the

postVisitDirectory

method is not invoked.

Method Detail

- values

```java
public static
FileVisitResult
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitResult c : FileVisitResult.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
FileVisitResult
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
FileVisitResult
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitResult c : FileVisitResult.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

FileVisitResult

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FileVisitResult c : FileVisitResult.values())
System.out.println(c);
```

for (FileVisitResult c : FileVisitResult.values())
System.out.println(c);

valueOf

```java
public static
FileVisitResult
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

FileVisitResult

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

