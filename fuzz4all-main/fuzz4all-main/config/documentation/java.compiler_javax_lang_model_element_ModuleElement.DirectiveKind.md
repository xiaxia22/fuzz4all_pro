# Enum ModuleElement.DirectiveKind

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.DirectiveKind.html`

### Class Description

```java
public static enum
ModuleElement.DirectiveKind

extends
Enum
<
ModuleElement.DirectiveKind
>
```

The

kind

of a directive.

Note that it is possible additional directive kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleElement.DirectiveKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ModuleElement.DirectiveKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleElement.DirectiveKind c : ModuleElement.DirectiveKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ModuleElement.DirectiveKind
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

#### Enum ModuleElement.DirectiveKind

java.lang.Object

- java.lang.Enum

<

ModuleElement.DirectiveKind

>
- - javax.lang.model.element.ModuleElement.DirectiveKind

java.lang.Enum

<

ModuleElement.DirectiveKind

>

- javax.lang.model.element.ModuleElement.DirectiveKind

javax.lang.model.element.ModuleElement.DirectiveKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

ModuleElement.DirectiveKind

>

**Enclosing interface:** ModuleElement

```java
public static enum
ModuleElement.DirectiveKind

extends
Enum
<
ModuleElement.DirectiveKind
>
```

The

kind

of a directive.

Note that it is possible additional directive kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

**Since:** 9

public static enum

ModuleElement.DirectiveKind

extends

Enum

<

ModuleElement.DirectiveKind

>

The

kind

of a directive.

Note that it is possible additional directive kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

Note that it is possible additional directive kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

EXPORTS

An "exports package-name [to module-name-list]" directive.

OPENS

An "opens package-name [to module-name-list]" directive.

PROVIDES

A "provides service-name with implementation-name" directive.

REQUIRES

A "requires (static|transitive)* module-name" directive.

USES

A "uses service-name" directive.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleElement.DirectiveKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleElement.DirectiveKind

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

EXPORTS

An "exports package-name [to module-name-list]" directive.

OPENS

An "opens package-name [to module-name-list]" directive.

PROVIDES

A "provides service-name with implementation-name" directive.

REQUIRES

A "requires (static|transitive)* module-name" directive.

USES

A "uses service-name" directive.

---

#### Enum Constant Summary

An "exports package-name [to module-name-list]" directive.

An "opens package-name [to module-name-list]" directive.

A "provides service-name with implementation-name" directive.

A "requires (static|transitive)* module-name" directive.

A "uses service-name" directive.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ModuleElement.DirectiveKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ModuleElement.DirectiveKind

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

- REQUIRES

```java
public static final
ModuleElement.DirectiveKind
REQUIRES
```

A "requires (static|transitive)* module-name" directive.

- EXPORTS

```java
public static final
ModuleElement.DirectiveKind
EXPORTS
```

An "exports package-name [to module-name-list]" directive.

- OPENS

```java
public static final
ModuleElement.DirectiveKind
OPENS
```

An "opens package-name [to module-name-list]" directive.

- USES

```java
public static final
ModuleElement.DirectiveKind
USES
```

A "uses service-name" directive.

- PROVIDES

```java
public static final
ModuleElement.DirectiveKind
PROVIDES
```

A "provides service-name with implementation-name" directive.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ModuleElement.DirectiveKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleElement.DirectiveKind c : ModuleElement.DirectiveKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleElement.DirectiveKind
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

- REQUIRES

```java
public static final
ModuleElement.DirectiveKind
REQUIRES
```

A "requires (static|transitive)* module-name" directive.

- EXPORTS

```java
public static final
ModuleElement.DirectiveKind
EXPORTS
```

An "exports package-name [to module-name-list]" directive.

- OPENS

```java
public static final
ModuleElement.DirectiveKind
OPENS
```

An "opens package-name [to module-name-list]" directive.

- USES

```java
public static final
ModuleElement.DirectiveKind
USES
```

A "uses service-name" directive.

- PROVIDES

```java
public static final
ModuleElement.DirectiveKind
PROVIDES
```

A "provides service-name with implementation-name" directive.

---

#### Enum Constant Detail

REQUIRES

```java
public static final
ModuleElement.DirectiveKind
REQUIRES
```

A "requires (static|transitive)* module-name" directive.

---

#### REQUIRES

public static final

ModuleElement.DirectiveKind

REQUIRES

A "requires (static|transitive)* module-name" directive.

EXPORTS

```java
public static final
ModuleElement.DirectiveKind
EXPORTS
```

An "exports package-name [to module-name-list]" directive.

---

#### EXPORTS

public static final

ModuleElement.DirectiveKind

EXPORTS

An "exports package-name [to module-name-list]" directive.

OPENS

```java
public static final
ModuleElement.DirectiveKind
OPENS
```

An "opens package-name [to module-name-list]" directive.

---

#### OPENS

public static final

ModuleElement.DirectiveKind

OPENS

An "opens package-name [to module-name-list]" directive.

USES

```java
public static final
ModuleElement.DirectiveKind
USES
```

A "uses service-name" directive.

---

#### USES

public static final

ModuleElement.DirectiveKind

USES

A "uses service-name" directive.

PROVIDES

```java
public static final
ModuleElement.DirectiveKind
PROVIDES
```

A "provides service-name with implementation-name" directive.

---

#### PROVIDES

public static final

ModuleElement.DirectiveKind

PROVIDES

A "provides service-name with implementation-name" directive.

Method Detail

- values

```java
public static
ModuleElement.DirectiveKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleElement.DirectiveKind c : ModuleElement.DirectiveKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ModuleElement.DirectiveKind
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
ModuleElement.DirectiveKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleElement.DirectiveKind c : ModuleElement.DirectiveKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ModuleElement.DirectiveKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ModuleElement.DirectiveKind c : ModuleElement.DirectiveKind.values())
System.out.println(c);
```

for (ModuleElement.DirectiveKind c : ModuleElement.DirectiveKind.values())
System.out.println(c);

valueOf

```java
public static
ModuleElement.DirectiveKind
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

ModuleElement.DirectiveKind

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

