# Enum ModuleDescriptor.Modifier

**Source:** `java.base\java\lang\module\ModuleDescriptor.Modifier.html`

### Class Description

```java
public static enum
ModuleDescriptor.Modifier

extends
Enum
<
ModuleDescriptor.Modifier
>
```

A modifier on a module.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleDescriptor.Modifier

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ModuleDescriptor.Modifier
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Modifier c : ModuleDescriptor.Modifier.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ModuleDescriptor.Modifier
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

#### Enum ModuleDescriptor.Modifier

java.lang.Object

- java.lang.Enum

<

ModuleDescriptor.Modifier

>
- - java.lang.module.ModuleDescriptor.Modifier

java.lang.Enum

<

ModuleDescriptor.Modifier

>

- java.lang.module.ModuleDescriptor.Modifier

java.lang.module.ModuleDescriptor.Modifier

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleDescriptor.Modifier

>

**Enclosing class:** ModuleDescriptor

```java
public static enum
ModuleDescriptor.Modifier

extends
Enum
<
ModuleDescriptor.Modifier
>
```

A modifier on a module.

**Since:** 9
**See Also:** ModuleDescriptor.modifiers()

public static enum

ModuleDescriptor.Modifier

extends

Enum

<

ModuleDescriptor.Modifier

>

A modifier on a module.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

AUTOMATIC

An automatic module.

MANDATED

The module was implicitly declared.

OPEN

An open module.

SYNTHETIC

The module was not explicitly or implicitly declared.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleDescriptor.Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleDescriptor.Modifier

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

AUTOMATIC

An automatic module.

MANDATED

The module was implicitly declared.

OPEN

An open module.

SYNTHETIC

The module was not explicitly or implicitly declared.

---

#### Enum Constant Summary

An automatic module.

The module was implicitly declared.

An open module.

The module was not explicitly or implicitly declared.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleDescriptor.Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleDescriptor.Modifier

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

- OPEN

```java
public static final
ModuleDescriptor.Modifier
OPEN
```

An open module. An open module does not declare any open packages
but the resulting module is treated as if all packages are open.

- AUTOMATIC

```java
public static final
ModuleDescriptor.Modifier
AUTOMATIC
```

An automatic module. An automatic module is treated as if it exports
and opens all packages.

**API Note:** This modifier does not correspond to a module flag in the
binary form of a module declaration (

module-info.class

).

- SYNTHETIC

```java
public static final
ModuleDescriptor.Modifier
SYNTHETIC
```

The module was not explicitly or implicitly declared.

- MANDATED

```java
public static final
ModuleDescriptor.Modifier
MANDATED
```

The module was implicitly declared.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ModuleDescriptor.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Modifier c : ModuleDescriptor.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleDescriptor.Modifier
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

- OPEN

```java
public static final
ModuleDescriptor.Modifier
OPEN
```

An open module. An open module does not declare any open packages
but the resulting module is treated as if all packages are open.

- AUTOMATIC

```java
public static final
ModuleDescriptor.Modifier
AUTOMATIC
```

An automatic module. An automatic module is treated as if it exports
and opens all packages.

**API Note:** This modifier does not correspond to a module flag in the
binary form of a module declaration (

module-info.class

).

- SYNTHETIC

```java
public static final
ModuleDescriptor.Modifier
SYNTHETIC
```

The module was not explicitly or implicitly declared.

- MANDATED

```java
public static final
ModuleDescriptor.Modifier
MANDATED
```

The module was implicitly declared.

---

#### Enum Constant Detail

OPEN

```java
public static final
ModuleDescriptor.Modifier
OPEN
```

An open module. An open module does not declare any open packages
but the resulting module is treated as if all packages are open.

---

#### OPEN

public static final

ModuleDescriptor.Modifier

OPEN

An open module. An open module does not declare any open packages
but the resulting module is treated as if all packages are open.

AUTOMATIC

```java
public static final
ModuleDescriptor.Modifier
AUTOMATIC
```

An automatic module. An automatic module is treated as if it exports
and opens all packages.

**API Note:** This modifier does not correspond to a module flag in the
binary form of a module declaration (

module-info.class

).

---

#### AUTOMATIC

public static final

ModuleDescriptor.Modifier

AUTOMATIC

An automatic module. An automatic module is treated as if it exports
and opens all packages.

SYNTHETIC

```java
public static final
ModuleDescriptor.Modifier
SYNTHETIC
```

The module was not explicitly or implicitly declared.

---

#### SYNTHETIC

public static final

ModuleDescriptor.Modifier

SYNTHETIC

The module was not explicitly or implicitly declared.

MANDATED

```java
public static final
ModuleDescriptor.Modifier
MANDATED
```

The module was implicitly declared.

---

#### MANDATED

public static final

ModuleDescriptor.Modifier

MANDATED

The module was implicitly declared.

Method Detail

- values

```java
public static
ModuleDescriptor.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Modifier c : ModuleDescriptor.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleDescriptor.Modifier
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
ModuleDescriptor.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Modifier c : ModuleDescriptor.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ModuleDescriptor.Modifier

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Modifier c : ModuleDescriptor.Modifier.values())
System.out.println(c);
```

for (ModuleDescriptor.Modifier c : ModuleDescriptor.Modifier.values())
System.out.println(c);

valueOf

```java
public static
ModuleDescriptor.Modifier
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

ModuleDescriptor.Modifier

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

