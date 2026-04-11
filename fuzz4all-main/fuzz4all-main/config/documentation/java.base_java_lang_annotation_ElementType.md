# Enum ElementType

**Source:** `java.base\java\lang\annotation\ElementType.html`

### Class Description

```java
public enum
ElementType

extends
Enum
<
ElementType
>
```

The constants of this enumerated type provide a simple classification of the
syntactic locations where annotations may appear in a Java program. These
constants are used in

Target

meta-annotations to specify where it is legal to write annotations of a
given type.

The syntactic locations where annotations may appear are split into

declaration contexts

, where annotations apply to declarations, and

type contexts

, where annotations apply to types used in
declarations and expressions.

The constants

ANNOTATION_TYPE

,

CONSTRUCTOR

,

FIELD

,

LOCAL_VARIABLE

,

METHOD

,

PACKAGE

,

MODULE

,

PARAMETER

,

TYPE

, and

TYPE_PARAMETER

correspond to the declaration contexts in JLS 9.6.4.1.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.FIELD)

may only be written as a modifier for a
field declaration.

The constant

TYPE_USE

corresponds to the type contexts in JLS
4.11, as well as to two declaration contexts: type declarations (including
annotation type declarations) and type parameter declarations.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ElementType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ElementType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementType c : ElementType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ElementType
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

#### Enum ElementType

java.lang.Object

- java.lang.Enum

<

ElementType

>
- - java.lang.annotation.ElementType

java.lang.Enum

<

ElementType

>

- java.lang.annotation.ElementType

java.lang.annotation.ElementType

**All Implemented Interfaces:** Serializable

,

Comparable

<

ElementType

>

```java
public enum
ElementType

extends
Enum
<
ElementType
>
```

The constants of this enumerated type provide a simple classification of the
syntactic locations where annotations may appear in a Java program. These
constants are used in

Target

meta-annotations to specify where it is legal to write annotations of a
given type.

The syntactic locations where annotations may appear are split into

declaration contexts

, where annotations apply to declarations, and

type contexts

, where annotations apply to types used in
declarations and expressions.

The constants

ANNOTATION_TYPE

,

CONSTRUCTOR

,

FIELD

,

LOCAL_VARIABLE

,

METHOD

,

PACKAGE

,

MODULE

,

PARAMETER

,

TYPE

, and

TYPE_PARAMETER

correspond to the declaration contexts in JLS 9.6.4.1.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.FIELD)

may only be written as a modifier for a
field declaration.

The constant

TYPE_USE

corresponds to the type contexts in JLS
4.11, as well as to two declaration contexts: type declarations (including
annotation type declarations) and type parameter declarations.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

**Since:** 1.5
**See The Java™ Language Specification :** 9.6.4.1 @Target, 4.1 The Kinds of Types and Values

public enum

ElementType

extends

Enum

<

ElementType

>

The constants of this enumerated type provide a simple classification of the
syntactic locations where annotations may appear in a Java program. These
constants are used in

Target

meta-annotations to specify where it is legal to write annotations of a
given type.

The syntactic locations where annotations may appear are split into

declaration contexts

, where annotations apply to declarations, and

type contexts

, where annotations apply to types used in
declarations and expressions.

The constants

ANNOTATION_TYPE

,

CONSTRUCTOR

,

FIELD

,

LOCAL_VARIABLE

,

METHOD

,

PACKAGE

,

MODULE

,

PARAMETER

,

TYPE

, and

TYPE_PARAMETER

correspond to the declaration contexts in JLS 9.6.4.1.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.FIELD)

may only be written as a modifier for a
field declaration.

The constant

TYPE_USE

corresponds to the type contexts in JLS
4.11, as well as to two declaration contexts: type declarations (including
annotation type declarations) and type parameter declarations.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

The syntactic locations where annotations may appear are split into

declaration contexts

, where annotations apply to declarations, and

type contexts

, where annotations apply to types used in
declarations and expressions.

The constants

ANNOTATION_TYPE

,

CONSTRUCTOR

,

FIELD

,

LOCAL_VARIABLE

,

METHOD

,

PACKAGE

,

MODULE

,

PARAMETER

,

TYPE

, and

TYPE_PARAMETER

correspond to the declaration contexts in JLS 9.6.4.1.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.FIELD)

may only be written as a modifier for a
field declaration.

The constant

TYPE_USE

corresponds to the type contexts in JLS
4.11, as well as to two declaration contexts: type declarations (including
annotation type declarations) and type parameter declarations.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

The constants

ANNOTATION_TYPE

,

CONSTRUCTOR

,

FIELD

,

LOCAL_VARIABLE

,

METHOD

,

PACKAGE

,

MODULE

,

PARAMETER

,

TYPE

, and

TYPE_PARAMETER

correspond to the declaration contexts in JLS 9.6.4.1.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.FIELD)

may only be written as a modifier for a
field declaration.

The constant

TYPE_USE

corresponds to the type contexts in JLS
4.11, as well as to two declaration contexts: type declarations (including
annotation type declarations) and type parameter declarations.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.FIELD)

may only be written as a modifier for a
field declaration.

The constant

TYPE_USE

corresponds to the type contexts in JLS
4.11, as well as to two declaration contexts: type declarations (including
annotation type declarations) and type parameter declarations.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

The constant

TYPE_USE

corresponds to the type contexts in JLS
4.11, as well as to two declaration contexts: type declarations (including
annotation type declarations) and type parameter declarations.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

For example, an annotation whose type is meta-annotated with

@Target(ElementType.TYPE_USE)

may be written on the type of a field
(or within the type of the field, if it is a nested, parameterized, or array
type), and may also appear as a modifier for, say, a class declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

The

TYPE_USE

constant includes type declarations and type
parameter declarations as a convenience for designers of type checkers which
give semantics to annotation types. For example, if the annotation type

NonNull

is meta-annotated with

@Target(ElementType.TYPE_USE)

, then

@NonNull

class C {...}

could be treated by a type checker as indicating that
all variables of class

C

are non-null, while still allowing
variables of other classes to be non-null or not non-null based on whether

@NonNull

appears at the variable's declaration.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ANNOTATION_TYPE

Annotation type declaration

CONSTRUCTOR

Constructor declaration

FIELD

Field declaration (includes enum constants)

LOCAL_VARIABLE

Local variable declaration

METHOD

Method declaration

MODULE

Module declaration.

PACKAGE

Package declaration

PARAMETER

Formal parameter declaration

TYPE

Class, interface (including annotation type), or enum declaration

TYPE_PARAMETER

Type parameter declaration

TYPE_USE

Use of a type

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ElementType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ElementType

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

ANNOTATION_TYPE

Annotation type declaration

CONSTRUCTOR

Constructor declaration

FIELD

Field declaration (includes enum constants)

LOCAL_VARIABLE

Local variable declaration

METHOD

Method declaration

MODULE

Module declaration.

PACKAGE

Package declaration

PARAMETER

Formal parameter declaration

TYPE

Class, interface (including annotation type), or enum declaration

TYPE_PARAMETER

Type parameter declaration

TYPE_USE

Use of a type

---

#### Enum Constant Summary

Annotation type declaration

Constructor declaration

Field declaration (includes enum constants)

Local variable declaration

Method declaration

Module declaration.

Package declaration

Formal parameter declaration

Class, interface (including annotation type), or enum declaration

Type parameter declaration

Use of a type

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ElementType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ElementType

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

- TYPE

```java
public static final
ElementType
TYPE
```

Class, interface (including annotation type), or enum declaration

- FIELD

```java
public static final
ElementType
FIELD
```

Field declaration (includes enum constants)

- METHOD

```java
public static final
ElementType
METHOD
```

Method declaration

- PARAMETER

```java
public static final
ElementType
PARAMETER
```

Formal parameter declaration

- CONSTRUCTOR

```java
public static final
ElementType
CONSTRUCTOR
```

Constructor declaration

- LOCAL_VARIABLE

```java
public static final
ElementType
LOCAL_VARIABLE
```

Local variable declaration

- ANNOTATION_TYPE

```java
public static final
ElementType
ANNOTATION_TYPE
```

Annotation type declaration

- PACKAGE

```java
public static final
ElementType
PACKAGE
```

Package declaration

- TYPE_PARAMETER

```java
public static final
ElementType
TYPE_PARAMETER
```

Type parameter declaration

**Since:** 1.8

- TYPE_USE

```java
public static final
ElementType
TYPE_USE
```

Use of a type

**Since:** 1.8

- MODULE

```java
public static final
ElementType
MODULE
```

Module declaration.

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ElementType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementType c : ElementType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ElementType
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

- TYPE

```java
public static final
ElementType
TYPE
```

Class, interface (including annotation type), or enum declaration

- FIELD

```java
public static final
ElementType
FIELD
```

Field declaration (includes enum constants)

- METHOD

```java
public static final
ElementType
METHOD
```

Method declaration

- PARAMETER

```java
public static final
ElementType
PARAMETER
```

Formal parameter declaration

- CONSTRUCTOR

```java
public static final
ElementType
CONSTRUCTOR
```

Constructor declaration

- LOCAL_VARIABLE

```java
public static final
ElementType
LOCAL_VARIABLE
```

Local variable declaration

- ANNOTATION_TYPE

```java
public static final
ElementType
ANNOTATION_TYPE
```

Annotation type declaration

- PACKAGE

```java
public static final
ElementType
PACKAGE
```

Package declaration

- TYPE_PARAMETER

```java
public static final
ElementType
TYPE_PARAMETER
```

Type parameter declaration

**Since:** 1.8

- TYPE_USE

```java
public static final
ElementType
TYPE_USE
```

Use of a type

**Since:** 1.8

- MODULE

```java
public static final
ElementType
MODULE
```

Module declaration.

**Since:** 9

---

#### Enum Constant Detail

TYPE

```java
public static final
ElementType
TYPE
```

Class, interface (including annotation type), or enum declaration

---

#### TYPE

public static final

ElementType

TYPE

Class, interface (including annotation type), or enum declaration

FIELD

```java
public static final
ElementType
FIELD
```

Field declaration (includes enum constants)

---

#### FIELD

public static final

ElementType

FIELD

Field declaration (includes enum constants)

METHOD

```java
public static final
ElementType
METHOD
```

Method declaration

---

#### METHOD

public static final

ElementType

METHOD

Method declaration

PARAMETER

```java
public static final
ElementType
PARAMETER
```

Formal parameter declaration

---

#### PARAMETER

public static final

ElementType

PARAMETER

Formal parameter declaration

CONSTRUCTOR

```java
public static final
ElementType
CONSTRUCTOR
```

Constructor declaration

---

#### CONSTRUCTOR

public static final

ElementType

CONSTRUCTOR

Constructor declaration

LOCAL_VARIABLE

```java
public static final
ElementType
LOCAL_VARIABLE
```

Local variable declaration

---

#### LOCAL_VARIABLE

public static final

ElementType

LOCAL_VARIABLE

Local variable declaration

ANNOTATION_TYPE

```java
public static final
ElementType
ANNOTATION_TYPE
```

Annotation type declaration

---

#### ANNOTATION_TYPE

public static final

ElementType

ANNOTATION_TYPE

Annotation type declaration

PACKAGE

```java
public static final
ElementType
PACKAGE
```

Package declaration

---

#### PACKAGE

public static final

ElementType

PACKAGE

Package declaration

TYPE_PARAMETER

```java
public static final
ElementType
TYPE_PARAMETER
```

Type parameter declaration

**Since:** 1.8

---

#### TYPE_PARAMETER

public static final

ElementType

TYPE_PARAMETER

Type parameter declaration

TYPE_USE

```java
public static final
ElementType
TYPE_USE
```

Use of a type

**Since:** 1.8

---

#### TYPE_USE

public static final

ElementType

TYPE_USE

Use of a type

MODULE

```java
public static final
ElementType
MODULE
```

Module declaration.

**Since:** 9

---

#### MODULE

public static final

ElementType

MODULE

Module declaration.

Method Detail

- values

```java
public static
ElementType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementType c : ElementType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ElementType
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
ElementType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementType c : ElementType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ElementType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementType c : ElementType.values())
System.out.println(c);
```

for (ElementType c : ElementType.values())
System.out.println(c);

valueOf

```java
public static
ElementType
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

ElementType

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

