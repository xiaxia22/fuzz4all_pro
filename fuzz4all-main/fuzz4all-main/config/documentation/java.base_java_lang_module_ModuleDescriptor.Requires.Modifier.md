# Enum ModuleDescriptor.Requires.Modifier

**Source:** `java.base\java\lang\module\ModuleDescriptor.Requires.Modifier.html`

### Class Description

```java
public static enum
ModuleDescriptor.Requires.Modifier

extends
Enum
<
ModuleDescriptor.Requires.Modifier
>
```

A modifier on a module dependence.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleDescriptor.Requires.Modifier

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ModuleDescriptor.Requires.Modifier
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Requires.Modifier c : ModuleDescriptor.Requires.Modifier.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ModuleDescriptor.Requires.Modifier
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

#### Enum ModuleDescriptor.Requires.Modifier

java.lang.Object

- java.lang.Enum

<

ModuleDescriptor.Requires.Modifier

>
- - java.lang.module.ModuleDescriptor.Requires.Modifier

java.lang.Enum

<

ModuleDescriptor.Requires.Modifier

>

- java.lang.module.ModuleDescriptor.Requires.Modifier

java.lang.module.ModuleDescriptor.Requires.Modifier

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleDescriptor.Requires.Modifier

>

**Enclosing class:** ModuleDescriptor.Requires

```java
public static enum
ModuleDescriptor.Requires.Modifier

extends
Enum
<
ModuleDescriptor.Requires.Modifier
>
```

A modifier on a module dependence.

**Since:** 9
**See Also:** ModuleDescriptor.Requires.modifiers()

public static enum

ModuleDescriptor.Requires.Modifier

extends

Enum

<

ModuleDescriptor.Requires.Modifier

>

A modifier on a module dependence.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

MANDATED

The dependence was implicitly declared in the source of the module
declaration.

STATIC

The dependence is mandatory in the static phase, during compilation,
but is optional in the dynamic phase, during execution.

SYNTHETIC

The dependence was not explicitly or implicitly declared in the
source of the module declaration.

TRANSITIVE

The dependence causes any module which depends on the

current
module

to have an implicitly declared dependence on the module
named by the

Requires

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleDescriptor.Requires.Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleDescriptor.Requires.Modifier

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

The dependence was implicitly declared in the source of the module
declaration.

STATIC

The dependence is mandatory in the static phase, during compilation,
but is optional in the dynamic phase, during execution.

SYNTHETIC

The dependence was not explicitly or implicitly declared in the
source of the module declaration.

TRANSITIVE

The dependence causes any module which depends on the

current
module

to have an implicitly declared dependence on the module
named by the

Requires

.

---

#### Enum Constant Summary

The dependence was implicitly declared in the source of the module
declaration.

The dependence is mandatory in the static phase, during compilation,
but is optional in the dynamic phase, during execution.

The dependence was not explicitly or implicitly declared in the
source of the module declaration.

The dependence causes any module which depends on the

current
module

to have an implicitly declared dependence on the module
named by the

Requires

.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleDescriptor.Requires.Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleDescriptor.Requires.Modifier

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

- TRANSITIVE

```java
public static final
ModuleDescriptor.Requires.Modifier
TRANSITIVE
```

The dependence causes any module which depends on the

current
module

to have an implicitly declared dependence on the module
named by the

Requires

.

- STATIC

```java
public static final
ModuleDescriptor.Requires.Modifier
STATIC
```

The dependence is mandatory in the static phase, during compilation,
but is optional in the dynamic phase, during execution.

- SYNTHETIC

```java
public static final
ModuleDescriptor.Requires.Modifier
SYNTHETIC
```

The dependence was not explicitly or implicitly declared in the
source of the module declaration.

- MANDATED

```java
public static final
ModuleDescriptor.Requires.Modifier
MANDATED
```

The dependence was implicitly declared in the source of the module
declaration.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ModuleDescriptor.Requires.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Requires.Modifier c : ModuleDescriptor.Requires.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleDescriptor.Requires.Modifier
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

- TRANSITIVE

```java
public static final
ModuleDescriptor.Requires.Modifier
TRANSITIVE
```

The dependence causes any module which depends on the

current
module

to have an implicitly declared dependence on the module
named by the

Requires

.

- STATIC

```java
public static final
ModuleDescriptor.Requires.Modifier
STATIC
```

The dependence is mandatory in the static phase, during compilation,
but is optional in the dynamic phase, during execution.

- SYNTHETIC

```java
public static final
ModuleDescriptor.Requires.Modifier
SYNTHETIC
```

The dependence was not explicitly or implicitly declared in the
source of the module declaration.

- MANDATED

```java
public static final
ModuleDescriptor.Requires.Modifier
MANDATED
```

The dependence was implicitly declared in the source of the module
declaration.

---

#### Enum Constant Detail

TRANSITIVE

```java
public static final
ModuleDescriptor.Requires.Modifier
TRANSITIVE
```

The dependence causes any module which depends on the

current
module

to have an implicitly declared dependence on the module
named by the

Requires

.

---

#### TRANSITIVE

public static final

ModuleDescriptor.Requires.Modifier

TRANSITIVE

The dependence causes any module which depends on the

current
module

to have an implicitly declared dependence on the module
named by the

Requires

.

STATIC

```java
public static final
ModuleDescriptor.Requires.Modifier
STATIC
```

The dependence is mandatory in the static phase, during compilation,
but is optional in the dynamic phase, during execution.

---

#### STATIC

public static final

ModuleDescriptor.Requires.Modifier

STATIC

The dependence is mandatory in the static phase, during compilation,
but is optional in the dynamic phase, during execution.

SYNTHETIC

```java
public static final
ModuleDescriptor.Requires.Modifier
SYNTHETIC
```

The dependence was not explicitly or implicitly declared in the
source of the module declaration.

---

#### SYNTHETIC

public static final

ModuleDescriptor.Requires.Modifier

SYNTHETIC

The dependence was not explicitly or implicitly declared in the
source of the module declaration.

MANDATED

```java
public static final
ModuleDescriptor.Requires.Modifier
MANDATED
```

The dependence was implicitly declared in the source of the module
declaration.

---

#### MANDATED

public static final

ModuleDescriptor.Requires.Modifier

MANDATED

The dependence was implicitly declared in the source of the module
declaration.

Method Detail

- values

```java
public static
ModuleDescriptor.Requires.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Requires.Modifier c : ModuleDescriptor.Requires.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleDescriptor.Requires.Modifier
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
ModuleDescriptor.Requires.Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Requires.Modifier c : ModuleDescriptor.Requires.Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ModuleDescriptor.Requires.Modifier

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleDescriptor.Requires.Modifier c : ModuleDescriptor.Requires.Modifier.values())
System.out.println(c);
```

for (ModuleDescriptor.Requires.Modifier c : ModuleDescriptor.Requires.Modifier.values())
System.out.println(c);

valueOf

```java
public static
ModuleDescriptor.Requires.Modifier
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

ModuleDescriptor.Requires.Modifier

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

