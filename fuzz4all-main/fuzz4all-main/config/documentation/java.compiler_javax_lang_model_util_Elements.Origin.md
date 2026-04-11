# Enum Elements.Origin

**Source:** `java.compiler\javax\lang\model\util\Elements.Origin.html`

### Class Description

```java
public static enum
Elements.Origin

extends
Enum
<
Elements.Origin
>
```

The

origin

of an element or other language model
item. The origin of an element or item models how a construct
in a program is declared in the source code, explicitly,
implicitly, etc.

Note that it is possible additional kinds of origin values
will be added in future versions of the platform.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Elements.Origin

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Elements.Origin
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Elements.Origin c : Elements.Origin.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Elements.Origin
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

#### public boolean isDeclared()

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

**Returns:**
- true

for

EXPLICIT

and

MANDATED

,

false

otherwise.

---

### Additional Sections

#### Enum Elements.Origin

java.lang.Object

- java.lang.Enum

<

Elements.Origin

>
- - javax.lang.model.util.Elements.Origin

java.lang.Enum

<

Elements.Origin

>

- javax.lang.model.util.Elements.Origin

javax.lang.model.util.Elements.Origin

**All Implemented Interfaces:** Serializable

,

Comparable

<

Elements.Origin

>

**Enclosing interface:** Elements

```java
public static enum
Elements.Origin

extends
Enum
<
Elements.Origin
>
```

The

origin

of an element or other language model
item. The origin of an element or item models how a construct
in a program is declared in the source code, explicitly,
implicitly, etc.

Note that it is possible additional kinds of origin values
will be added in future versions of the platform.

**Since:** 9
**See The Java™ Language Specification :** 13.1 The Form of a Binary

public static enum

Elements.Origin

extends

Enum

<

Elements.Origin

>

The

origin

of an element or other language model
item. The origin of an element or item models how a construct
in a program is declared in the source code, explicitly,
implicitly, etc.

Note that it is possible additional kinds of origin values
will be added in future versions of the platform.

Note that it is possible additional kinds of origin values
will be added in future versions of the platform.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

EXPLICIT

Describes a construct explicitly declared in source code.

MANDATED

A mandated construct is one that is not explicitly declared
in the source code, but whose presence is mandated by the
specification.

SYNTHETIC

A synthetic construct is one that is neither implicitly nor
explicitly declared in the source code.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isDeclared

()

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

static

Elements.Origin

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Elements.Origin

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

EXPLICIT

Describes a construct explicitly declared in source code.

MANDATED

A mandated construct is one that is not explicitly declared
in the source code, but whose presence is mandated by the
specification.

SYNTHETIC

A synthetic construct is one that is neither implicitly nor
explicitly declared in the source code.

---

#### Enum Constant Summary

Describes a construct explicitly declared in source code.

A mandated construct is one that is not explicitly declared
in the source code, but whose presence is mandated by the
specification.

A synthetic construct is one that is neither implicitly nor
explicitly declared in the source code.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isDeclared

()

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

static

Elements.Origin

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Elements.Origin

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

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

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

- EXPLICIT

```java
public static final
Elements.Origin
EXPLICIT
```

Describes a construct explicitly declared in source code.

- MANDATED

```java
public static final
Elements.Origin
MANDATED
```

A mandated construct is one that is not explicitly declared
in the source code, but whose presence is mandated by the
specification. Such a construct is said to be implicitly
declared.

One example of a mandated element is a

default
constructor

in a class that contains no explicit
constructor declarations.

Another example of a mandated construct is an implicitly
declared

container annotation

used to hold
multiple annotations of a repeatable annotation type.

**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9.3 Enum Members, 9.6.3 Repeatable Annotation Types, 9.7.5 Multiple Annotations of the Same Type

- SYNTHETIC

```java
public static final
Elements.Origin
SYNTHETIC
```

A synthetic construct is one that is neither implicitly nor
explicitly declared in the source code. Such a construct is
typically a translation artifact created by a compiler.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Elements.Origin
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Elements.Origin c : Elements.Origin.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Elements.Origin
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

- isDeclared

```java
public boolean isDeclared()
```

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

**Returns:** true

for

EXPLICIT

and

MANDATED

,

false

otherwise.

Enum Constant Detail

- EXPLICIT

```java
public static final
Elements.Origin
EXPLICIT
```

Describes a construct explicitly declared in source code.

- MANDATED

```java
public static final
Elements.Origin
MANDATED
```

A mandated construct is one that is not explicitly declared
in the source code, but whose presence is mandated by the
specification. Such a construct is said to be implicitly
declared.

One example of a mandated element is a

default
constructor

in a class that contains no explicit
constructor declarations.

Another example of a mandated construct is an implicitly
declared

container annotation

used to hold
multiple annotations of a repeatable annotation type.

**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9.3 Enum Members, 9.6.3 Repeatable Annotation Types, 9.7.5 Multiple Annotations of the Same Type

- SYNTHETIC

```java
public static final
Elements.Origin
SYNTHETIC
```

A synthetic construct is one that is neither implicitly nor
explicitly declared in the source code. Such a construct is
typically a translation artifact created by a compiler.

---

#### Enum Constant Detail

EXPLICIT

```java
public static final
Elements.Origin
EXPLICIT
```

Describes a construct explicitly declared in source code.

---

#### EXPLICIT

public static final

Elements.Origin

EXPLICIT

Describes a construct explicitly declared in source code.

MANDATED

```java
public static final
Elements.Origin
MANDATED
```

A mandated construct is one that is not explicitly declared
in the source code, but whose presence is mandated by the
specification. Such a construct is said to be implicitly
declared.

One example of a mandated element is a

default
constructor

in a class that contains no explicit
constructor declarations.

Another example of a mandated construct is an implicitly
declared

container annotation

used to hold
multiple annotations of a repeatable annotation type.

**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9.3 Enum Members, 9.6.3 Repeatable Annotation Types, 9.7.5 Multiple Annotations of the Same Type

---

#### MANDATED

public static final

Elements.Origin

MANDATED

A mandated construct is one that is not explicitly declared
in the source code, but whose presence is mandated by the
specification. Such a construct is said to be implicitly
declared.

One example of a mandated element is a

default
constructor

in a class that contains no explicit
constructor declarations.

Another example of a mandated construct is an implicitly
declared

container annotation

used to hold
multiple annotations of a repeatable annotation type.

SYNTHETIC

```java
public static final
Elements.Origin
SYNTHETIC
```

A synthetic construct is one that is neither implicitly nor
explicitly declared in the source code. Such a construct is
typically a translation artifact created by a compiler.

---

#### SYNTHETIC

public static final

Elements.Origin

SYNTHETIC

A synthetic construct is one that is neither implicitly nor
explicitly declared in the source code. Such a construct is
typically a translation artifact created by a compiler.

Method Detail

- values

```java
public static
Elements.Origin
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Elements.Origin c : Elements.Origin.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Elements.Origin
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

- isDeclared

```java
public boolean isDeclared()
```

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

**Returns:** true

for

EXPLICIT

and

MANDATED

,

false

otherwise.

---

#### Method Detail

values

```java
public static
Elements.Origin
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Elements.Origin c : Elements.Origin.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Elements.Origin

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Elements.Origin c : Elements.Origin.values())
System.out.println(c);
```

for (Elements.Origin c : Elements.Origin.values())
System.out.println(c);

valueOf

```java
public static
Elements.Origin
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

Elements.Origin

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isDeclared

```java
public boolean isDeclared()
```

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

**Returns:** true

for

EXPLICIT

and

MANDATED

,

false

otherwise.

---

#### isDeclared

public boolean isDeclared()

Returns

true

for values corresponding to constructs
that are implicitly or explicitly declared,

false

otherwise.

---

