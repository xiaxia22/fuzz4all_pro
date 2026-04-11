# Enum ModuleDescriptor.Opens.Modifier

**Source:** `java.base\java\lang\module\ModuleDescriptor.Opens.Modifier.html`

### Class Description

```java
public static enum
ModuleDescriptor.Opens.Modifier

extends
Enum
<
ModuleDescriptor.Opens.Modifier
>
```

A modifier on an open package.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleDescriptor.Opens.Modifier

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ModuleDescriptor.Opens.Modifier
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Opens.Modifier c : ModuleDescriptor.Opens.Modifier.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ModuleDescriptor.Opens.Modifier
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

#### Enum ModuleDescriptor.Opens.Modifier

java.lang.Object

- java.lang.Enum

<

ModuleDescriptor.Opens.Modifier

>
- - java.lang.module.ModuleDescriptor.Opens.Modifier

java.lang.Enum

<

ModuleDescriptor.Opens.Modifier

>

- java.lang.module.ModuleDescriptor.Opens.Modifier

java.lang.module.ModuleDescriptor.Opens.Modifier

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleDescriptor.Opens.Modifier

>

**Enclosing class:** ModuleDescriptor.Opens

```java
public static enum
ModuleDescriptor.Opens.Modifier

extends
Enum
<
ModuleDescriptor.Opens.Modifier
>
```

A modifier on an open package.

**Since:** 9
**See Also:** ModuleDescriptor.Opens.modifiers()

public static enum

ModuleDescriptor.Opens.Modifier

extends

Enum

<

ModuleDescriptor.Opens.Modifier

>

A modifier on an open package.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

MANDATED

The open package was implicitly declared in the source of the
module declaration.

SYNTHETIC

The open package was not explicitly or implicitly declared in
the source of the module declaration.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleDescriptor.Opens.Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleDescriptor.Opens.Modifier

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

MANDATED

The open package was implicitly declared in the source of the
module declaration.

SYNTHETIC

The open package was not explicitly or implicitly declared in
the source of the module declaration.

---

#### Enum Constant Summary

The open package was implicitly declared in the source of the
module declaration.

The open package was not explicitly or implicitly declared in
the source of the module declaration.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleDescriptor.Opens.Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleDescriptor.Opens.Modifier

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

- SYNTHETIC

```java
public static final
ModuleDescriptor.Opens.Modifier
SYNTHETIC
```

The open package was not explicitly or implicitly declared in
the source of the module declaration.

- MANDATED

```java
public static final
ModuleDescriptor.Opens.Modifier
MANDATED
```

The open package was implicitly declared in the source of the
module declaration.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ModuleDescriptor.Opens.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Opens.Modifier c : ModuleDescriptor.Opens.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleDescriptor.Opens.Modifier
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

- SYNTHETIC

```java
public static final
ModuleDescriptor.Opens.Modifier
SYNTHETIC
```

The open package was not explicitly or implicitly declared in
the source of the module declaration.

- MANDATED

```java
public static final
ModuleDescriptor.Opens.Modifier
MANDATED
```

The open package was implicitly declared in the source of the
module declaration.

---

#### Enum Constant Detail

SYNTHETIC

```java
public static final
ModuleDescriptor.Opens.Modifier
SYNTHETIC
```

The open package was not explicitly or implicitly declared in
the source of the module declaration.

---

#### SYNTHETIC

public static final

ModuleDescriptor.Opens.Modifier

SYNTHETIC

The open package was not explicitly or implicitly declared in
the source of the module declaration.

MANDATED

```java
public static final
ModuleDescriptor.Opens.Modifier
MANDATED
```

The open package was implicitly declared in the source of the
module declaration.

---

#### MANDATED

public static final

ModuleDescriptor.Opens.Modifier

MANDATED

The open package was implicitly declared in the source of the
module declaration.

Method Detail

- values

```java
public static
ModuleDescriptor.Opens.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Opens.Modifier c : ModuleDescriptor.Opens.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleDescriptor.Opens.Modifier
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
ModuleDescriptor.Opens.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Opens.Modifier c : ModuleDescriptor.Opens.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ModuleDescriptor.Opens.Modifier

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Opens.Modifier c : ModuleDescriptor.Opens.Modifier.values())
System.out.println(c);
```

for (ModuleDescriptor.Opens.Modifier c : ModuleDescriptor.Opens.Modifier.values())
System.out.println(c);

valueOf

```java
public static
ModuleDescriptor.Opens.Modifier
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

ModuleDescriptor.Opens.Modifier

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

