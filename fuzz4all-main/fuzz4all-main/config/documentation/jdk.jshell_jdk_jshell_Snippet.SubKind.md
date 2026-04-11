# Enum Snippet.SubKind

**Source:** `jdk.jshell\jdk\jshell\Snippet.SubKind.html`

### Class Description

```java
public static enum
Snippet.SubKind

extends
Enum
<
Snippet.SubKind
>
```

The detailed variety of a snippet. This is a sub-classification of the
Kind. The Kind of a SubKind is accessible with

kind()

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Snippet.SubKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Snippet.SubKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.SubKind c : Snippet.SubKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Snippet.SubKind
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

#### public boolean isExecutable()

Indicates whether this

SubKind

is executable.

**Returns:**
- true

if this

SubKind

can
be executed; otherwise

false

---

#### public boolean hasValue()

Indicates whether this

SubKind

is executable and
is non-

void

.

**Returns:**
- true

if this

SubKind

has
a value; otherwise

false

---

#### public
Snippet.Kind
kind()

The

Snippet.Kind

that corresponds to this

SubKind

.

**Returns:**
- the fixed

Kind

for this

SubKind

---

### Additional Sections

#### Enum Snippet.SubKind

java.lang.Object

- java.lang.Enum

<

Snippet.SubKind

>
- - jdk.jshell.Snippet.SubKind

java.lang.Enum

<

Snippet.SubKind

>

- jdk.jshell.Snippet.SubKind

jdk.jshell.Snippet.SubKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

Snippet.SubKind

>

**Enclosing class:** Snippet

```java
public static enum
Snippet.SubKind

extends
Enum
<
Snippet.SubKind
>
```

The detailed variety of a snippet. This is a sub-classification of the
Kind. The Kind of a SubKind is accessible with

kind()

.

public static enum

Snippet.SubKind

extends

Enum

<

Snippet.SubKind

>

The detailed variety of a snippet. This is a sub-classification of the
Kind. The Kind of a SubKind is accessible with

kind()

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ANNOTATION_TYPE_SUBKIND

An annotation interface declaration.

ASSIGNMENT_SUBKIND

An assignment expression.

CLASS_SUBKIND

A class declaration.

ENUM_SUBKIND

An enum declaration.

INTERFACE_SUBKIND

An interface declaration.

METHOD_SUBKIND

A method.

OTHER_EXPRESSION_SUBKIND

An expression which has not been wrapped in a temporary variable
(reserved).

SINGLE_STATIC_IMPORT_SUBKIND

Single-Static-Import Declaration.

SINGLE_TYPE_IMPORT_SUBKIND

Single-Type-Import Declaration.

STATEMENT_SUBKIND

A statement.

STATIC_IMPORT_ON_DEMAND_SUBKIND

Static-Import-on-Demand Declaration.

TEMP_VAR_EXPRESSION_SUBKIND

An expression whose value has been stored in a temporary variable.

TYPE_IMPORT_ON_DEMAND_SUBKIND

Type-Import-on-Demand Declaration.

UNKNOWN_SUBKIND

An unknown snippet.

VAR_DECLARATION_SUBKIND

A variable declaration without initializer.

VAR_DECLARATION_WITH_INITIALIZER_SUBKIND

A variable declaration with an initializer expression.

VAR_VALUE_SUBKIND

A simple variable reference expression.

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

hasValue

()

Indicates whether this

SubKind

is executable and
is non-

void

.

boolean

isExecutable

()

Indicates whether this

SubKind

is executable.

Snippet.Kind

kind

()

The

Snippet.Kind

that corresponds to this

SubKind

.

static

Snippet.SubKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Snippet.SubKind

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

ANNOTATION_TYPE_SUBKIND

An annotation interface declaration.

ASSIGNMENT_SUBKIND

An assignment expression.

CLASS_SUBKIND

A class declaration.

ENUM_SUBKIND

An enum declaration.

INTERFACE_SUBKIND

An interface declaration.

METHOD_SUBKIND

A method.

OTHER_EXPRESSION_SUBKIND

An expression which has not been wrapped in a temporary variable
(reserved).

SINGLE_STATIC_IMPORT_SUBKIND

Single-Static-Import Declaration.

SINGLE_TYPE_IMPORT_SUBKIND

Single-Type-Import Declaration.

STATEMENT_SUBKIND

A statement.

STATIC_IMPORT_ON_DEMAND_SUBKIND

Static-Import-on-Demand Declaration.

TEMP_VAR_EXPRESSION_SUBKIND

An expression whose value has been stored in a temporary variable.

TYPE_IMPORT_ON_DEMAND_SUBKIND

Type-Import-on-Demand Declaration.

UNKNOWN_SUBKIND

An unknown snippet.

VAR_DECLARATION_SUBKIND

A variable declaration without initializer.

VAR_DECLARATION_WITH_INITIALIZER_SUBKIND

A variable declaration with an initializer expression.

VAR_VALUE_SUBKIND

A simple variable reference expression.

---

#### Enum Constant Summary

An annotation interface declaration.

An assignment expression.

A class declaration.

An enum declaration.

An interface declaration.

A method.

An expression which has not been wrapped in a temporary variable
(reserved).

Single-Static-Import Declaration.

Single-Type-Import Declaration.

A statement.

Static-Import-on-Demand Declaration.

An expression whose value has been stored in a temporary variable.

Type-Import-on-Demand Declaration.

An unknown snippet.

A variable declaration without initializer.

A variable declaration with an initializer expression.

A simple variable reference expression.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

hasValue

()

Indicates whether this

SubKind

is executable and
is non-

void

.

boolean

isExecutable

()

Indicates whether this

SubKind

is executable.

Snippet.Kind

kind

()

The

Snippet.Kind

that corresponds to this

SubKind

.

static

Snippet.SubKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Snippet.SubKind

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

Indicates whether this

SubKind

is executable and
is non-

void

.

Indicates whether this

SubKind

is executable.

The

Snippet.Kind

that corresponds to this

SubKind

.

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

- SINGLE_TYPE_IMPORT_SUBKIND

```java
public static final
Snippet.SubKind
SINGLE_TYPE_IMPORT_SUBKIND
```

Single-Type-Import Declaration.
An import declaration of a single type.

**See The Java™ Language Specification :** 7.5.1 SingleTypeImportDeclaration.

- TYPE_IMPORT_ON_DEMAND_SUBKIND

```java
public static final
Snippet.SubKind
TYPE_IMPORT_ON_DEMAND_SUBKIND
```

Type-Import-on-Demand Declaration.
A non-static "star" import.

**See The Java™ Language Specification :** 7.5.2. TypeImportOnDemandDeclaration.

- SINGLE_STATIC_IMPORT_SUBKIND

```java
public static final
Snippet.SubKind
SINGLE_STATIC_IMPORT_SUBKIND
```

Single-Static-Import Declaration.
An import of a static member.

**See The Java™ Language Specification :** 7.5.3 Single-Static-Import.

- STATIC_IMPORT_ON_DEMAND_SUBKIND

```java
public static final
Snippet.SubKind
STATIC_IMPORT_ON_DEMAND_SUBKIND
```

Static-Import-on-Demand Declaration.
A static "star" import of all static members of a named type.

**See The Java™ Language Specification :** 7.5.4. Static-Import-on-Demand Static "star" import.

- CLASS_SUBKIND

```java
public static final
Snippet.SubKind
CLASS_SUBKIND
```

A class declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 8.1. NormalClassDeclaration.

- INTERFACE_SUBKIND

```java
public static final
Snippet.SubKind
INTERFACE_SUBKIND
```

An interface declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 9.1. NormalInterfaceDeclaration.

- ENUM_SUBKIND

```java
public static final
Snippet.SubKind
ENUM_SUBKIND
```

An enum declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 8.9. EnumDeclaration.

- ANNOTATION_TYPE_SUBKIND

```java
public static final
Snippet.SubKind
ANNOTATION_TYPE_SUBKIND
```

An annotation interface declaration. A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 9.6. AnnotationTypeDeclaration.

- METHOD_SUBKIND

```java
public static final
Snippet.SubKind
METHOD_SUBKIND
```

A method. The only

SubKind

for

Snippet.Kind.METHOD

.

**See The Java™ Language Specification :** 8.4. MethodDeclaration.

- VAR_DECLARATION_SUBKIND

```java
public static final
Snippet.SubKind
VAR_DECLARATION_SUBKIND
```

A variable declaration without initializer.
A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 8.3. VariableDeclarator without VariableInitializer in
FieldDeclaration.

- VAR_DECLARATION_WITH_INITIALIZER_SUBKIND

```java
public static final
Snippet.SubKind
VAR_DECLARATION_WITH_INITIALIZER_SUBKIND
```

A variable declaration with an initializer expression. A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 8.3. VariableDeclarator with VariableInitializer in
FieldDeclaration.

- TEMP_VAR_EXPRESSION_SUBKIND

```java
public static final
Snippet.SubKind
TEMP_VAR_EXPRESSION_SUBKIND
```

An expression whose value has been stored in a temporary variable. A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 15. Primary.

- VAR_VALUE_SUBKIND

```java
public static final
Snippet.SubKind
VAR_VALUE_SUBKIND
```

A simple variable reference expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

**See The Java™ Language Specification :** 15.11. Field Access as 3.8. Identifier.

- ASSIGNMENT_SUBKIND

```java
public static final
Snippet.SubKind
ASSIGNMENT_SUBKIND
```

An assignment expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

**See The Java™ Language Specification :** 15.26. Assignment.

- OTHER_EXPRESSION_SUBKIND

```java
public static final
Snippet.SubKind
OTHER_EXPRESSION_SUBKIND
```

An expression which has not been wrapped in a temporary variable
(reserved). A

SubKind

of

Snippet.Kind.EXPRESSION

.

- STATEMENT_SUBKIND

```java
public static final
Snippet.SubKind
STATEMENT_SUBKIND
```

A statement. The only

SubKind

for

Snippet.Kind.STATEMENT

.

**See The Java™ Language Specification :** 14.5. Statement.

- UNKNOWN_SUBKIND

```java
public static final
Snippet.SubKind
UNKNOWN_SUBKIND
```

An unknown snippet. The only

SubKind

for

Snippet.Kind.ERRONEOUS

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Snippet.SubKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.SubKind c : Snippet.SubKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Snippet.SubKind
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

- isExecutable

```java
public boolean isExecutable()
```

Indicates whether this

SubKind

is executable.

**Returns:** true

if this

SubKind

can
be executed; otherwise

false

- hasValue

```java
public boolean hasValue()
```

Indicates whether this

SubKind

is executable and
is non-

void

.

**Returns:** true

if this

SubKind

has
a value; otherwise

false

- kind

```java
public
Snippet.Kind
kind()
```

The

Snippet.Kind

that corresponds to this

SubKind

.

**Returns:** the fixed

Kind

for this

SubKind

Enum Constant Detail

- SINGLE_TYPE_IMPORT_SUBKIND

```java
public static final
Snippet.SubKind
SINGLE_TYPE_IMPORT_SUBKIND
```

Single-Type-Import Declaration.
An import declaration of a single type.

**See The Java™ Language Specification :** 7.5.1 SingleTypeImportDeclaration.

- TYPE_IMPORT_ON_DEMAND_SUBKIND

```java
public static final
Snippet.SubKind
TYPE_IMPORT_ON_DEMAND_SUBKIND
```

Type-Import-on-Demand Declaration.
A non-static "star" import.

**See The Java™ Language Specification :** 7.5.2. TypeImportOnDemandDeclaration.

- SINGLE_STATIC_IMPORT_SUBKIND

```java
public static final
Snippet.SubKind
SINGLE_STATIC_IMPORT_SUBKIND
```

Single-Static-Import Declaration.
An import of a static member.

**See The Java™ Language Specification :** 7.5.3 Single-Static-Import.

- STATIC_IMPORT_ON_DEMAND_SUBKIND

```java
public static final
Snippet.SubKind
STATIC_IMPORT_ON_DEMAND_SUBKIND
```

Static-Import-on-Demand Declaration.
A static "star" import of all static members of a named type.

**See The Java™ Language Specification :** 7.5.4. Static-Import-on-Demand Static "star" import.

- CLASS_SUBKIND

```java
public static final
Snippet.SubKind
CLASS_SUBKIND
```

A class declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 8.1. NormalClassDeclaration.

- INTERFACE_SUBKIND

```java
public static final
Snippet.SubKind
INTERFACE_SUBKIND
```

An interface declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 9.1. NormalInterfaceDeclaration.

- ENUM_SUBKIND

```java
public static final
Snippet.SubKind
ENUM_SUBKIND
```

An enum declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 8.9. EnumDeclaration.

- ANNOTATION_TYPE_SUBKIND

```java
public static final
Snippet.SubKind
ANNOTATION_TYPE_SUBKIND
```

An annotation interface declaration. A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 9.6. AnnotationTypeDeclaration.

- METHOD_SUBKIND

```java
public static final
Snippet.SubKind
METHOD_SUBKIND
```

A method. The only

SubKind

for

Snippet.Kind.METHOD

.

**See The Java™ Language Specification :** 8.4. MethodDeclaration.

- VAR_DECLARATION_SUBKIND

```java
public static final
Snippet.SubKind
VAR_DECLARATION_SUBKIND
```

A variable declaration without initializer.
A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 8.3. VariableDeclarator without VariableInitializer in
FieldDeclaration.

- VAR_DECLARATION_WITH_INITIALIZER_SUBKIND

```java
public static final
Snippet.SubKind
VAR_DECLARATION_WITH_INITIALIZER_SUBKIND
```

A variable declaration with an initializer expression. A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 8.3. VariableDeclarator with VariableInitializer in
FieldDeclaration.

- TEMP_VAR_EXPRESSION_SUBKIND

```java
public static final
Snippet.SubKind
TEMP_VAR_EXPRESSION_SUBKIND
```

An expression whose value has been stored in a temporary variable. A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 15. Primary.

- VAR_VALUE_SUBKIND

```java
public static final
Snippet.SubKind
VAR_VALUE_SUBKIND
```

A simple variable reference expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

**See The Java™ Language Specification :** 15.11. Field Access as 3.8. Identifier.

- ASSIGNMENT_SUBKIND

```java
public static final
Snippet.SubKind
ASSIGNMENT_SUBKIND
```

An assignment expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

**See The Java™ Language Specification :** 15.26. Assignment.

- OTHER_EXPRESSION_SUBKIND

```java
public static final
Snippet.SubKind
OTHER_EXPRESSION_SUBKIND
```

An expression which has not been wrapped in a temporary variable
(reserved). A

SubKind

of

Snippet.Kind.EXPRESSION

.

- STATEMENT_SUBKIND

```java
public static final
Snippet.SubKind
STATEMENT_SUBKIND
```

A statement. The only

SubKind

for

Snippet.Kind.STATEMENT

.

**See The Java™ Language Specification :** 14.5. Statement.

- UNKNOWN_SUBKIND

```java
public static final
Snippet.SubKind
UNKNOWN_SUBKIND
```

An unknown snippet. The only

SubKind

for

Snippet.Kind.ERRONEOUS

.

---

#### Enum Constant Detail

SINGLE_TYPE_IMPORT_SUBKIND

```java
public static final
Snippet.SubKind
SINGLE_TYPE_IMPORT_SUBKIND
```

Single-Type-Import Declaration.
An import declaration of a single type.

**See The Java™ Language Specification :** 7.5.1 SingleTypeImportDeclaration.

---

#### SINGLE_TYPE_IMPORT_SUBKIND

public static final

Snippet.SubKind

SINGLE_TYPE_IMPORT_SUBKIND

Single-Type-Import Declaration.
An import declaration of a single type.

TYPE_IMPORT_ON_DEMAND_SUBKIND

```java
public static final
Snippet.SubKind
TYPE_IMPORT_ON_DEMAND_SUBKIND
```

Type-Import-on-Demand Declaration.
A non-static "star" import.

**See The Java™ Language Specification :** 7.5.2. TypeImportOnDemandDeclaration.

---

#### TYPE_IMPORT_ON_DEMAND_SUBKIND

public static final

Snippet.SubKind

TYPE_IMPORT_ON_DEMAND_SUBKIND

Type-Import-on-Demand Declaration.
A non-static "star" import.

SINGLE_STATIC_IMPORT_SUBKIND

```java
public static final
Snippet.SubKind
SINGLE_STATIC_IMPORT_SUBKIND
```

Single-Static-Import Declaration.
An import of a static member.

**See The Java™ Language Specification :** 7.5.3 Single-Static-Import.

---

#### SINGLE_STATIC_IMPORT_SUBKIND

public static final

Snippet.SubKind

SINGLE_STATIC_IMPORT_SUBKIND

Single-Static-Import Declaration.
An import of a static member.

STATIC_IMPORT_ON_DEMAND_SUBKIND

```java
public static final
Snippet.SubKind
STATIC_IMPORT_ON_DEMAND_SUBKIND
```

Static-Import-on-Demand Declaration.
A static "star" import of all static members of a named type.

**See The Java™ Language Specification :** 7.5.4. Static-Import-on-Demand Static "star" import.

---

#### STATIC_IMPORT_ON_DEMAND_SUBKIND

public static final

Snippet.SubKind

STATIC_IMPORT_ON_DEMAND_SUBKIND

Static-Import-on-Demand Declaration.
A static "star" import of all static members of a named type.

CLASS_SUBKIND

```java
public static final
Snippet.SubKind
CLASS_SUBKIND
```

A class declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 8.1. NormalClassDeclaration.

---

#### CLASS_SUBKIND

public static final

Snippet.SubKind

CLASS_SUBKIND

A class declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

INTERFACE_SUBKIND

```java
public static final
Snippet.SubKind
INTERFACE_SUBKIND
```

An interface declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 9.1. NormalInterfaceDeclaration.

---

#### INTERFACE_SUBKIND

public static final

Snippet.SubKind

INTERFACE_SUBKIND

An interface declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

ENUM_SUBKIND

```java
public static final
Snippet.SubKind
ENUM_SUBKIND
```

An enum declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 8.9. EnumDeclaration.

---

#### ENUM_SUBKIND

public static final

Snippet.SubKind

ENUM_SUBKIND

An enum declaration.
A

SubKind

of

Snippet.Kind.TYPE_DECL

.

ANNOTATION_TYPE_SUBKIND

```java
public static final
Snippet.SubKind
ANNOTATION_TYPE_SUBKIND
```

An annotation interface declaration. A

SubKind

of

Snippet.Kind.TYPE_DECL

.

**See The Java™ Language Specification :** 9.6. AnnotationTypeDeclaration.

---

#### ANNOTATION_TYPE_SUBKIND

public static final

Snippet.SubKind

ANNOTATION_TYPE_SUBKIND

An annotation interface declaration. A

SubKind

of

Snippet.Kind.TYPE_DECL

.

METHOD_SUBKIND

```java
public static final
Snippet.SubKind
METHOD_SUBKIND
```

A method. The only

SubKind

for

Snippet.Kind.METHOD

.

**See The Java™ Language Specification :** 8.4. MethodDeclaration.

---

#### METHOD_SUBKIND

public static final

Snippet.SubKind

METHOD_SUBKIND

A method. The only

SubKind

for

Snippet.Kind.METHOD

.

VAR_DECLARATION_SUBKIND

```java
public static final
Snippet.SubKind
VAR_DECLARATION_SUBKIND
```

A variable declaration without initializer.
A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 8.3. VariableDeclarator without VariableInitializer in
FieldDeclaration.

---

#### VAR_DECLARATION_SUBKIND

public static final

Snippet.SubKind

VAR_DECLARATION_SUBKIND

A variable declaration without initializer.
A

SubKind

of

Snippet.Kind.VAR

.

VAR_DECLARATION_WITH_INITIALIZER_SUBKIND

```java
public static final
Snippet.SubKind
VAR_DECLARATION_WITH_INITIALIZER_SUBKIND
```

A variable declaration with an initializer expression. A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 8.3. VariableDeclarator with VariableInitializer in
FieldDeclaration.

---

#### VAR_DECLARATION_WITH_INITIALIZER_SUBKIND

public static final

Snippet.SubKind

VAR_DECLARATION_WITH_INITIALIZER_SUBKIND

A variable declaration with an initializer expression. A

SubKind

of

Snippet.Kind.VAR

.

TEMP_VAR_EXPRESSION_SUBKIND

```java
public static final
Snippet.SubKind
TEMP_VAR_EXPRESSION_SUBKIND
```

An expression whose value has been stored in a temporary variable. A

SubKind

of

Snippet.Kind.VAR

.

**See The Java™ Language Specification :** 15. Primary.

---

#### TEMP_VAR_EXPRESSION_SUBKIND

public static final

Snippet.SubKind

TEMP_VAR_EXPRESSION_SUBKIND

An expression whose value has been stored in a temporary variable. A

SubKind

of

Snippet.Kind.VAR

.

VAR_VALUE_SUBKIND

```java
public static final
Snippet.SubKind
VAR_VALUE_SUBKIND
```

A simple variable reference expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

**See The Java™ Language Specification :** 15.11. Field Access as 3.8. Identifier.

---

#### VAR_VALUE_SUBKIND

public static final

Snippet.SubKind

VAR_VALUE_SUBKIND

A simple variable reference expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

ASSIGNMENT_SUBKIND

```java
public static final
Snippet.SubKind
ASSIGNMENT_SUBKIND
```

An assignment expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

**See The Java™ Language Specification :** 15.26. Assignment.

---

#### ASSIGNMENT_SUBKIND

public static final

Snippet.SubKind

ASSIGNMENT_SUBKIND

An assignment expression. A

SubKind

of

Snippet.Kind.EXPRESSION

.

OTHER_EXPRESSION_SUBKIND

```java
public static final
Snippet.SubKind
OTHER_EXPRESSION_SUBKIND
```

An expression which has not been wrapped in a temporary variable
(reserved). A

SubKind

of

Snippet.Kind.EXPRESSION

.

---

#### OTHER_EXPRESSION_SUBKIND

public static final

Snippet.SubKind

OTHER_EXPRESSION_SUBKIND

An expression which has not been wrapped in a temporary variable
(reserved). A

SubKind

of

Snippet.Kind.EXPRESSION

.

STATEMENT_SUBKIND

```java
public static final
Snippet.SubKind
STATEMENT_SUBKIND
```

A statement. The only

SubKind

for

Snippet.Kind.STATEMENT

.

**See The Java™ Language Specification :** 14.5. Statement.

---

#### STATEMENT_SUBKIND

public static final

Snippet.SubKind

STATEMENT_SUBKIND

A statement. The only

SubKind

for

Snippet.Kind.STATEMENT

.

UNKNOWN_SUBKIND

```java
public static final
Snippet.SubKind
UNKNOWN_SUBKIND
```

An unknown snippet. The only

SubKind

for

Snippet.Kind.ERRONEOUS

.

---

#### UNKNOWN_SUBKIND

public static final

Snippet.SubKind

UNKNOWN_SUBKIND

An unknown snippet. The only

SubKind

for

Snippet.Kind.ERRONEOUS

.

Method Detail

- values

```java
public static
Snippet.SubKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.SubKind c : Snippet.SubKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Snippet.SubKind
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

- isExecutable

```java
public boolean isExecutable()
```

Indicates whether this

SubKind

is executable.

**Returns:** true

if this

SubKind

can
be executed; otherwise

false

- hasValue

```java
public boolean hasValue()
```

Indicates whether this

SubKind

is executable and
is non-

void

.

**Returns:** true

if this

SubKind

has
a value; otherwise

false

- kind

```java
public
Snippet.Kind
kind()
```

The

Snippet.Kind

that corresponds to this

SubKind

.

**Returns:** the fixed

Kind

for this

SubKind

---

#### Method Detail

values

```java
public static
Snippet.SubKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.SubKind c : Snippet.SubKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Snippet.SubKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.SubKind c : Snippet.SubKind.values())
System.out.println(c);
```

for (Snippet.SubKind c : Snippet.SubKind.values())
System.out.println(c);

valueOf

```java
public static
Snippet.SubKind
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

Snippet.SubKind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isExecutable

```java
public boolean isExecutable()
```

Indicates whether this

SubKind

is executable.

**Returns:** true

if this

SubKind

can
be executed; otherwise

false

---

#### isExecutable

public boolean isExecutable()

Indicates whether this

SubKind

is executable.

hasValue

```java
public boolean hasValue()
```

Indicates whether this

SubKind

is executable and
is non-

void

.

**Returns:** true

if this

SubKind

has
a value; otherwise

false

---

#### hasValue

public boolean hasValue()

Indicates whether this

SubKind

is executable and
is non-

void

.

kind

```java
public
Snippet.Kind
kind()
```

The

Snippet.Kind

that corresponds to this

SubKind

.

**Returns:** the fixed

Kind

for this

SubKind

---

#### kind

public

Snippet.Kind

kind()

The

Snippet.Kind

that corresponds to this

SubKind

.

---

