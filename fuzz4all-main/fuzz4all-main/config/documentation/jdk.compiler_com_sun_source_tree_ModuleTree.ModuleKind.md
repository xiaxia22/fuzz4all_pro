# Enum ModuleTree.ModuleKind

**Source:** `jdk.compiler\com\sun\source\tree\ModuleTree.ModuleKind.html`

### Class Description

```java
public static enum
ModuleTree.ModuleKind

extends
Enum
<
ModuleTree.ModuleKind
>
```

The kind of the module.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleTree.ModuleKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ModuleTree.ModuleKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleTree.ModuleKind c : ModuleTree.ModuleKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ModuleTree.ModuleKind
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

#### Enum ModuleTree.ModuleKind

java.lang.Object

- java.lang.Enum

<

ModuleTree.ModuleKind

>
- - com.sun.source.tree.ModuleTree.ModuleKind

java.lang.Enum

<

ModuleTree.ModuleKind

>

- com.sun.source.tree.ModuleTree.ModuleKind

com.sun.source.tree.ModuleTree.ModuleKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleTree.ModuleKind

>

**Enclosing interface:** ModuleTree

```java
public static enum
ModuleTree.ModuleKind

extends
Enum
<
ModuleTree.ModuleKind
>
```

The kind of the module.

public static enum

ModuleTree.ModuleKind

extends

Enum

<

ModuleTree.ModuleKind

>

The kind of the module.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

OPEN

Open module.

STRONG

Strong module.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleTree.ModuleKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleTree.ModuleKind

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

OPEN

Open module.

STRONG

Strong module.

---

#### Enum Constant Summary

Open module.

Strong module.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleTree.ModuleKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleTree.ModuleKind

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
ModuleTree.ModuleKind
OPEN
```

Open module.

- STRONG

```java
public static final
ModuleTree.ModuleKind
STRONG
```

Strong module.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ModuleTree.ModuleKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleTree.ModuleKind c : ModuleTree.ModuleKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleTree.ModuleKind
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
ModuleTree.ModuleKind
OPEN
```

Open module.

- STRONG

```java
public static final
ModuleTree.ModuleKind
STRONG
```

Strong module.

---

#### Enum Constant Detail

OPEN

```java
public static final
ModuleTree.ModuleKind
OPEN
```

Open module.

---

#### OPEN

public static final

ModuleTree.ModuleKind

OPEN

Open module.

STRONG

```java
public static final
ModuleTree.ModuleKind
STRONG
```

Strong module.

---

#### STRONG

public static final

ModuleTree.ModuleKind

STRONG

Strong module.

Method Detail

- values

```java
public static
ModuleTree.ModuleKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleTree.ModuleKind c : ModuleTree.ModuleKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleTree.ModuleKind
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
ModuleTree.ModuleKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleTree.ModuleKind c : ModuleTree.ModuleKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ModuleTree.ModuleKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleTree.ModuleKind c : ModuleTree.ModuleKind.values())
System.out.println(c);
```

for (ModuleTree.ModuleKind c : ModuleTree.ModuleKind.values())
System.out.println(c);

valueOf

```java
public static
ModuleTree.ModuleKind
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

ModuleTree.ModuleKind

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

