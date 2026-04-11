# Enum LanguageVersion

**Source:** `jdk.javadoc\com\sun\javadoc\LanguageVersion.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public enum
LanguageVersion

extends
Enum
<
LanguageVersion
>
```

Java Programming Language version. The constants of this enum
identify the JDK and J2SE releases containing language changes
relevant to doclets.

All doclets support at least the 1.1 language version.
The first release subsequent to this with language changes
affecting doclets is 1.5.

**All Implemented Interfaces:** Serializable

,

Comparable

<

LanguageVersion

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
LanguageVersion
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LanguageVersion c : LanguageVersion.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
LanguageVersion
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

#### Enum LanguageVersion

java.lang.Object

- java.lang.Enum

<

LanguageVersion

>
- - com.sun.javadoc.LanguageVersion

java.lang.Enum

<

LanguageVersion

>

- com.sun.javadoc.LanguageVersion

com.sun.javadoc.LanguageVersion

**All Implemented Interfaces:** Serializable

,

Comparable

<

LanguageVersion

>

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public enum
LanguageVersion

extends
Enum
<
LanguageVersion
>
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Java Programming Language version. The constants of this enum
identify the JDK and J2SE releases containing language changes
relevant to doclets.

All doclets support at least the 1.1 language version.
The first release subsequent to this with language changes
affecting doclets is 1.5.

**Since:** 1.5

@Deprecated

(

since

="9",

forRemoval

=true)
public enum

LanguageVersion

extends

Enum

<

LanguageVersion

>

Java Programming Language version. The constants of this enum
identify the JDK and J2SE releases containing language changes
relevant to doclets.

All doclets support at least the 1.1 language version.
The first release subsequent to this with language changes
affecting doclets is 1.5.

All doclets support at least the 1.1 language version.
The first release subsequent to this with language changes
affecting doclets is 1.5.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

JAVA_1_1

Deprecated, for removal: This API element is subject to removal in a future version.

1.1 added nested classes and interfaces.

JAVA_1_5

Deprecated, for removal: This API element is subject to removal in a future version.

1.5 added generic types, annotations, enums, and varArgs.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

LanguageVersion

valueOf

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the enum constant of this type with the specified name.

static

LanguageVersion

[]

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

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

JAVA_1_1

Deprecated, for removal: This API element is subject to removal in a future version.

1.1 added nested classes and interfaces.

JAVA_1_5

Deprecated, for removal: This API element is subject to removal in a future version.

1.5 added generic types, annotations, enums, and varArgs.

---

#### Enum Constant Summary

Deprecated, for removal: This API element is subject to removal in a future version.

1.1 added nested classes and interfaces.

1.5 added generic types, annotations, enums, and varArgs.

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

LanguageVersion

valueOf

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the enum constant of this type with the specified name.

static

LanguageVersion

[]

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

- JAVA_1_1

```java
public static final
LanguageVersion
JAVA_1_1
```

Deprecated, for removal: This API element is subject to removal in a future version.

1.1 added nested classes and interfaces.

- JAVA_1_5

```java
public static final
LanguageVersion
JAVA_1_5
```

Deprecated, for removal: This API element is subject to removal in a future version.

1.5 added generic types, annotations, enums, and varArgs.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
LanguageVersion
[] values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LanguageVersion c : LanguageVersion.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LanguageVersion
valueOf​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

- JAVA_1_1

```java
public static final
LanguageVersion
JAVA_1_1
```

Deprecated, for removal: This API element is subject to removal in a future version.

1.1 added nested classes and interfaces.

- JAVA_1_5

```java
public static final
LanguageVersion
JAVA_1_5
```

Deprecated, for removal: This API element is subject to removal in a future version.

1.5 added generic types, annotations, enums, and varArgs.

---

#### Enum Constant Detail

JAVA_1_1

```java
public static final
LanguageVersion
JAVA_1_1
```

Deprecated, for removal: This API element is subject to removal in a future version.

1.1 added nested classes and interfaces.

---

#### JAVA_1_1

public static final

LanguageVersion

JAVA_1_1

1.1 added nested classes and interfaces.

JAVA_1_5

```java
public static final
LanguageVersion
JAVA_1_5
```

Deprecated, for removal: This API element is subject to removal in a future version.

1.5 added generic types, annotations, enums, and varArgs.

---

#### JAVA_1_5

public static final

LanguageVersion

JAVA_1_5

1.5 added generic types, annotations, enums, and varArgs.

Method Detail

- values

```java
public static
LanguageVersion
[] values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LanguageVersion c : LanguageVersion.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LanguageVersion
valueOf​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

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
LanguageVersion
[] values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LanguageVersion c : LanguageVersion.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

LanguageVersion

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LanguageVersion c : LanguageVersion.values())
System.out.println(c);
```

for (LanguageVersion c : LanguageVersion.values())
System.out.println(c);

valueOf

```java
public static
LanguageVersion
valueOf​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

LanguageVersion

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

