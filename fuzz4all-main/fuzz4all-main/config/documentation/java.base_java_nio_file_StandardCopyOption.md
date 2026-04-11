# Enum StandardCopyOption

**Source:** `java.base\java\nio\file\StandardCopyOption.html`

### Class Description

```java
public enum
StandardCopyOption

extends
Enum
<
StandardCopyOption
>
implements
CopyOption
```

Defines the standard copy options.

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardCopyOption

>

,

CopyOption

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StandardCopyOption
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardCopyOption c : StandardCopyOption.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
StandardCopyOption
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

#### Enum StandardCopyOption

java.lang.Object

- java.lang.Enum

<

StandardCopyOption

>
- - java.nio.file.StandardCopyOption

java.lang.Enum

<

StandardCopyOption

>

- java.nio.file.StandardCopyOption

java.nio.file.StandardCopyOption

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardCopyOption

>

,

CopyOption

```java
public enum
StandardCopyOption

extends
Enum
<
StandardCopyOption
>
implements
CopyOption
```

Defines the standard copy options.

**Since:** 1.7

public enum

StandardCopyOption

extends

Enum

<

StandardCopyOption

>
implements

CopyOption

Defines the standard copy options.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ATOMIC_MOVE

Move the file as an atomic file system operation.

COPY_ATTRIBUTES

Copy attributes to the new file.

REPLACE_EXISTING

Replace an existing file if it exists.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardCopyOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardCopyOption

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

ATOMIC_MOVE

Move the file as an atomic file system operation.

COPY_ATTRIBUTES

Copy attributes to the new file.

REPLACE_EXISTING

Replace an existing file if it exists.

---

#### Enum Constant Summary

Move the file as an atomic file system operation.

Copy attributes to the new file.

Replace an existing file if it exists.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardCopyOption

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardCopyOption

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

- REPLACE_EXISTING

```java
public static final
StandardCopyOption
REPLACE_EXISTING
```

Replace an existing file if it exists.

- COPY_ATTRIBUTES

```java
public static final
StandardCopyOption
COPY_ATTRIBUTES
```

Copy attributes to the new file.

- ATOMIC_MOVE

```java
public static final
StandardCopyOption
ATOMIC_MOVE
```

Move the file as an atomic file system operation.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
StandardCopyOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardCopyOption c : StandardCopyOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardCopyOption
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

- REPLACE_EXISTING

```java
public static final
StandardCopyOption
REPLACE_EXISTING
```

Replace an existing file if it exists.

- COPY_ATTRIBUTES

```java
public static final
StandardCopyOption
COPY_ATTRIBUTES
```

Copy attributes to the new file.

- ATOMIC_MOVE

```java
public static final
StandardCopyOption
ATOMIC_MOVE
```

Move the file as an atomic file system operation.

---

#### Enum Constant Detail

REPLACE_EXISTING

```java
public static final
StandardCopyOption
REPLACE_EXISTING
```

Replace an existing file if it exists.

---

#### REPLACE_EXISTING

public static final

StandardCopyOption

REPLACE_EXISTING

Replace an existing file if it exists.

COPY_ATTRIBUTES

```java
public static final
StandardCopyOption
COPY_ATTRIBUTES
```

Copy attributes to the new file.

---

#### COPY_ATTRIBUTES

public static final

StandardCopyOption

COPY_ATTRIBUTES

Copy attributes to the new file.

ATOMIC_MOVE

```java
public static final
StandardCopyOption
ATOMIC_MOVE
```

Move the file as an atomic file system operation.

---

#### ATOMIC_MOVE

public static final

StandardCopyOption

ATOMIC_MOVE

Move the file as an atomic file system operation.

Method Detail

- values

```java
public static
StandardCopyOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardCopyOption c : StandardCopyOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardCopyOption
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
StandardCopyOption
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardCopyOption c : StandardCopyOption.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

StandardCopyOption

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardCopyOption c : StandardCopyOption.values())
System.out.println(c);
```

for (StandardCopyOption c : StandardCopyOption.values())
System.out.println(c);

valueOf

```java
public static
StandardCopyOption
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

StandardCopyOption

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

