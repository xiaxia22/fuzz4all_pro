# Enum Snippet.Kind

**Source:** `jdk.jshell\jdk\jshell\Snippet.Kind.html`

### Class Description

```java
public static enum
Snippet.Kind

extends
Enum
<
Snippet.Kind
>
```

Describes the general kind of snippet.
The

Kind

is an immutable property of a Snippet.
It is accessed with

Snippet.kind()

.
The

Kind

can be used to determine which
subclass of Snippet it is. For example,

eval("int three() { return 3; }")

will
return a snippet creation event. The

Kind

of that Snippet
will be

METHOD

, from which you know that the subclass
of

Snippet

is

MethodSnippet

and it can be
cast as such.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Snippet.Kind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Snippet.Kind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Kind c : Snippet.Kind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Snippet.Kind
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

#### public boolean isPersistent()

Indicates whether this

Kind

of Snippet is persistent. Only
declarations are persistent because they influence future Snippets.

Note that though the

Kind

of
a Snippet may be persistent, that does not mean that the Snippet will
persist; For example it may be invalid or have been dropped. See:

Snippet.Status.isDefined()

.

**Returns:**
- true

if this

Kind

of

Snippet

is
visible to subsequent evaluations; otherwise

false

---

### Additional Sections

#### Enum Snippet.Kind

java.lang.Object

- java.lang.Enum

<

Snippet.Kind

>
- - jdk.jshell.Snippet.Kind

java.lang.Enum

<

Snippet.Kind

>

- jdk.jshell.Snippet.Kind

jdk.jshell.Snippet.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

Snippet.Kind

>

**Enclosing class:** Snippet

```java
public static enum
Snippet.Kind

extends
Enum
<
Snippet.Kind
>
```

Describes the general kind of snippet.
The

Kind

is an immutable property of a Snippet.
It is accessed with

Snippet.kind()

.
The

Kind

can be used to determine which
subclass of Snippet it is. For example,

eval("int three() { return 3; }")

will
return a snippet creation event. The

Kind

of that Snippet
will be

METHOD

, from which you know that the subclass
of

Snippet

is

MethodSnippet

and it can be
cast as such.

public static enum

Snippet.Kind

extends

Enum

<

Snippet.Kind

>

Describes the general kind of snippet.
The

Kind

is an immutable property of a Snippet.
It is accessed with

Snippet.kind()

.
The

Kind

can be used to determine which
subclass of Snippet it is. For example,

eval("int three() { return 3; }")

will
return a snippet creation event. The

Kind

of that Snippet
will be

METHOD

, from which you know that the subclass
of

Snippet

is

MethodSnippet

and it can be
cast as such.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ERRONEOUS

A syntactically incorrect input for which the specific
kind could not be determined.

EXPRESSION

An expression, with or without side-effects.

IMPORT

An import declaration:

import

...

METHOD

A method declaration.

STATEMENT

A statement.

TYPE_DECL

A type declaration.

VAR

One variable declaration.

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

isPersistent

()

Indicates whether this

Kind

of Snippet is persistent.

static

Snippet.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Snippet.Kind

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

ERRONEOUS

A syntactically incorrect input for which the specific
kind could not be determined.

EXPRESSION

An expression, with or without side-effects.

IMPORT

An import declaration:

import

...

METHOD

A method declaration.

STATEMENT

A statement.

TYPE_DECL

A type declaration.

VAR

One variable declaration.

---

#### Enum Constant Summary

A syntactically incorrect input for which the specific
kind could not be determined.

An expression, with or without side-effects.

An import declaration:

import

...

A method declaration.

A statement.

A type declaration.

One variable declaration.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isPersistent

()

Indicates whether this

Kind

of Snippet is persistent.

static

Snippet.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Snippet.Kind

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

Kind

of Snippet is persistent.

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

- IMPORT

```java
public static final
Snippet.Kind
IMPORT
```

An import declaration:

import

...
The snippet is an instance of

ImportSnippet

.

An import can be a single type import
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

),
a static single import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
an on-demand type import
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

),
or a static on-demand type import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

) --
use

Snippet.subKind()

to distinguish.

**See The Java™ Language Specification :** 8.3: importDeclaration.

An import declaration is

persistent

.

- TYPE_DECL

```java
public static final
Snippet.Kind
TYPE_DECL
```

A type declaration.
Which includes: NormalClassDeclaration, EnumDeclaration,
NormalInterfaceDeclaration, and AnnotationTypeDeclaration.
The snippet is an instance of

TypeDeclSnippet

.

A type declaration may be an interface

Snippet.SubKind.INTERFACE_SUBKIND

,
classes

Snippet.SubKind.CLASS_SUBKIND

, enums, and
annotation interfaces -- see

Snippet.SubKind

to
differentiate.

**See The Java™ Language Specification :** 7.6: TypeDeclaration.

A type declaration is

persistent

.

- METHOD

```java
public static final
Snippet.Kind
METHOD
```

A method declaration.
The snippet is an instance of

MethodSnippet

.

**See The Java™ Language Specification :** 8.4: MethodDeclaration.

A method declaration is

persistent

.

- VAR

```java
public static final
Snippet.Kind
VAR
```

One variable declaration.
Corresponding to one

VariableDeclarator

.
The snippet is an instance of

VarSnippet

.

The variable may be with or without initializer, or be a temporary
variable representing an expression -- see

Snippet.SubKind

to differentiate.

**See The Java™ Language Specification :** 8.3: FieldDeclaration.

A variable declaration is

persistent

.

- EXPRESSION

```java
public static final
Snippet.Kind
EXPRESSION
```

An expression, with or without side-effects.
The snippet is an instance of

ExpressionSnippet

.

The expression is currently either a simple named reference to a
variable (

Snippet.SubKind.VAR_VALUE_SUBKIND

) or an
assignment (both of which have natural referencing
names) -- see

Snippet.SubKind

to differentiate.
All other expression forms (operators, method calls, ...) generate a
scratch variable and so are instead of the VAR Kind.

**See The Java™ Language Specification :** 15: Expression.

- STATEMENT

```java
public static final
Snippet.Kind
STATEMENT
```

A statement.
The snippet is an instance of

StatementSnippet

.

**See The Java™ Language Specification :** 14.5: Statement.

- ERRONEOUS

```java
public static final
Snippet.Kind
ERRONEOUS
```

A syntactically incorrect input for which the specific
kind could not be determined.
The snippet is an instance of

ErroneousSnippet

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Snippet.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Kind c : Snippet.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Snippet.Kind
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

- isPersistent

```java
public boolean isPersistent()
```

Indicates whether this

Kind

of Snippet is persistent. Only
declarations are persistent because they influence future Snippets.

Note that though the

Kind

of
a Snippet may be persistent, that does not mean that the Snippet will
persist; For example it may be invalid or have been dropped. See:

Snippet.Status.isDefined()

.

**Returns:** true

if this

Kind

of

Snippet

is
visible to subsequent evaluations; otherwise

false

Enum Constant Detail

- IMPORT

```java
public static final
Snippet.Kind
IMPORT
```

An import declaration:

import

...
The snippet is an instance of

ImportSnippet

.

An import can be a single type import
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

),
a static single import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
an on-demand type import
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

),
or a static on-demand type import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

) --
use

Snippet.subKind()

to distinguish.

**See The Java™ Language Specification :** 8.3: importDeclaration.

An import declaration is

persistent

.

- TYPE_DECL

```java
public static final
Snippet.Kind
TYPE_DECL
```

A type declaration.
Which includes: NormalClassDeclaration, EnumDeclaration,
NormalInterfaceDeclaration, and AnnotationTypeDeclaration.
The snippet is an instance of

TypeDeclSnippet

.

A type declaration may be an interface

Snippet.SubKind.INTERFACE_SUBKIND

,
classes

Snippet.SubKind.CLASS_SUBKIND

, enums, and
annotation interfaces -- see

Snippet.SubKind

to
differentiate.

**See The Java™ Language Specification :** 7.6: TypeDeclaration.

A type declaration is

persistent

.

- METHOD

```java
public static final
Snippet.Kind
METHOD
```

A method declaration.
The snippet is an instance of

MethodSnippet

.

**See The Java™ Language Specification :** 8.4: MethodDeclaration.

A method declaration is

persistent

.

- VAR

```java
public static final
Snippet.Kind
VAR
```

One variable declaration.
Corresponding to one

VariableDeclarator

.
The snippet is an instance of

VarSnippet

.

The variable may be with or without initializer, or be a temporary
variable representing an expression -- see

Snippet.SubKind

to differentiate.

**See The Java™ Language Specification :** 8.3: FieldDeclaration.

A variable declaration is

persistent

.

- EXPRESSION

```java
public static final
Snippet.Kind
EXPRESSION
```

An expression, with or without side-effects.
The snippet is an instance of

ExpressionSnippet

.

The expression is currently either a simple named reference to a
variable (

Snippet.SubKind.VAR_VALUE_SUBKIND

) or an
assignment (both of which have natural referencing
names) -- see

Snippet.SubKind

to differentiate.
All other expression forms (operators, method calls, ...) generate a
scratch variable and so are instead of the VAR Kind.

**See The Java™ Language Specification :** 15: Expression.

- STATEMENT

```java
public static final
Snippet.Kind
STATEMENT
```

A statement.
The snippet is an instance of

StatementSnippet

.

**See The Java™ Language Specification :** 14.5: Statement.

- ERRONEOUS

```java
public static final
Snippet.Kind
ERRONEOUS
```

A syntactically incorrect input for which the specific
kind could not be determined.
The snippet is an instance of

ErroneousSnippet

.

---

#### Enum Constant Detail

IMPORT

```java
public static final
Snippet.Kind
IMPORT
```

An import declaration:

import

...
The snippet is an instance of

ImportSnippet

.

An import can be a single type import
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

),
a static single import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
an on-demand type import
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

),
or a static on-demand type import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

) --
use

Snippet.subKind()

to distinguish.

**See The Java™ Language Specification :** 8.3: importDeclaration.

An import declaration is

persistent

.

---

#### IMPORT

public static final

Snippet.Kind

IMPORT

An import declaration:

import

...
The snippet is an instance of

ImportSnippet

.

An import can be a single type import
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

),
a static single import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
an on-demand type import
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

),
or a static on-demand type import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

) --
use

Snippet.subKind()

to distinguish.

An import can be a single type import
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

),
a static single import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
an on-demand type import
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

),
or a static on-demand type import
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

) --
use

Snippet.subKind()

to distinguish.

An import declaration is

persistent

.

TYPE_DECL

```java
public static final
Snippet.Kind
TYPE_DECL
```

A type declaration.
Which includes: NormalClassDeclaration, EnumDeclaration,
NormalInterfaceDeclaration, and AnnotationTypeDeclaration.
The snippet is an instance of

TypeDeclSnippet

.

A type declaration may be an interface

Snippet.SubKind.INTERFACE_SUBKIND

,
classes

Snippet.SubKind.CLASS_SUBKIND

, enums, and
annotation interfaces -- see

Snippet.SubKind

to
differentiate.

**See The Java™ Language Specification :** 7.6: TypeDeclaration.

A type declaration is

persistent

.

---

#### TYPE_DECL

public static final

Snippet.Kind

TYPE_DECL

A type declaration.
Which includes: NormalClassDeclaration, EnumDeclaration,
NormalInterfaceDeclaration, and AnnotationTypeDeclaration.
The snippet is an instance of

TypeDeclSnippet

.

A type declaration may be an interface

Snippet.SubKind.INTERFACE_SUBKIND

,
classes

Snippet.SubKind.CLASS_SUBKIND

, enums, and
annotation interfaces -- see

Snippet.SubKind

to
differentiate.

A type declaration may be an interface

Snippet.SubKind.INTERFACE_SUBKIND

,
classes

Snippet.SubKind.CLASS_SUBKIND

, enums, and
annotation interfaces -- see

Snippet.SubKind

to
differentiate.

A type declaration is

persistent

.

METHOD

```java
public static final
Snippet.Kind
METHOD
```

A method declaration.
The snippet is an instance of

MethodSnippet

.

**See The Java™ Language Specification :** 8.4: MethodDeclaration.

A method declaration is

persistent

.

---

#### METHOD

public static final

Snippet.Kind

METHOD

A method declaration.
The snippet is an instance of

MethodSnippet

.

A method declaration is

persistent

.

VAR

```java
public static final
Snippet.Kind
VAR
```

One variable declaration.
Corresponding to one

VariableDeclarator

.
The snippet is an instance of

VarSnippet

.

The variable may be with or without initializer, or be a temporary
variable representing an expression -- see

Snippet.SubKind

to differentiate.

**See The Java™ Language Specification :** 8.3: FieldDeclaration.

A variable declaration is

persistent

.

---

#### VAR

public static final

Snippet.Kind

VAR

One variable declaration.
Corresponding to one

VariableDeclarator

.
The snippet is an instance of

VarSnippet

.

The variable may be with or without initializer, or be a temporary
variable representing an expression -- see

Snippet.SubKind

to differentiate.

The variable may be with or without initializer, or be a temporary
variable representing an expression -- see

Snippet.SubKind

to differentiate.

A variable declaration is

persistent

.

EXPRESSION

```java
public static final
Snippet.Kind
EXPRESSION
```

An expression, with or without side-effects.
The snippet is an instance of

ExpressionSnippet

.

The expression is currently either a simple named reference to a
variable (

Snippet.SubKind.VAR_VALUE_SUBKIND

) or an
assignment (both of which have natural referencing
names) -- see

Snippet.SubKind

to differentiate.
All other expression forms (operators, method calls, ...) generate a
scratch variable and so are instead of the VAR Kind.

**See The Java™ Language Specification :** 15: Expression.

---

#### EXPRESSION

public static final

Snippet.Kind

EXPRESSION

An expression, with or without side-effects.
The snippet is an instance of

ExpressionSnippet

.

The expression is currently either a simple named reference to a
variable (

Snippet.SubKind.VAR_VALUE_SUBKIND

) or an
assignment (both of which have natural referencing
names) -- see

Snippet.SubKind

to differentiate.
All other expression forms (operators, method calls, ...) generate a
scratch variable and so are instead of the VAR Kind.

The expression is currently either a simple named reference to a
variable (

Snippet.SubKind.VAR_VALUE_SUBKIND

) or an
assignment (both of which have natural referencing
names) -- see

Snippet.SubKind

to differentiate.
All other expression forms (operators, method calls, ...) generate a
scratch variable and so are instead of the VAR Kind.

STATEMENT

```java
public static final
Snippet.Kind
STATEMENT
```

A statement.
The snippet is an instance of

StatementSnippet

.

**See The Java™ Language Specification :** 14.5: Statement.

---

#### STATEMENT

public static final

Snippet.Kind

STATEMENT

A statement.
The snippet is an instance of

StatementSnippet

.

ERRONEOUS

```java
public static final
Snippet.Kind
ERRONEOUS
```

A syntactically incorrect input for which the specific
kind could not be determined.
The snippet is an instance of

ErroneousSnippet

.

---

#### ERRONEOUS

public static final

Snippet.Kind

ERRONEOUS

A syntactically incorrect input for which the specific
kind could not be determined.
The snippet is an instance of

ErroneousSnippet

.

Method Detail

- values

```java
public static
Snippet.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Kind c : Snippet.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Snippet.Kind
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

- isPersistent

```java
public boolean isPersistent()
```

Indicates whether this

Kind

of Snippet is persistent. Only
declarations are persistent because they influence future Snippets.

Note that though the

Kind

of
a Snippet may be persistent, that does not mean that the Snippet will
persist; For example it may be invalid or have been dropped. See:

Snippet.Status.isDefined()

.

**Returns:** true

if this

Kind

of

Snippet

is
visible to subsequent evaluations; otherwise

false

---

#### Method Detail

values

```java
public static
Snippet.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Kind c : Snippet.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Snippet.Kind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Kind c : Snippet.Kind.values())
System.out.println(c);
```

for (Snippet.Kind c : Snippet.Kind.values())
System.out.println(c);

valueOf

```java
public static
Snippet.Kind
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

Snippet.Kind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isPersistent

```java
public boolean isPersistent()
```

Indicates whether this

Kind

of Snippet is persistent. Only
declarations are persistent because they influence future Snippets.

Note that though the

Kind

of
a Snippet may be persistent, that does not mean that the Snippet will
persist; For example it may be invalid or have been dropped. See:

Snippet.Status.isDefined()

.

**Returns:** true

if this

Kind

of

Snippet

is
visible to subsequent evaluations; otherwise

false

---

#### isPersistent

public boolean isPersistent()

Indicates whether this

Kind

of Snippet is persistent. Only
declarations are persistent because they influence future Snippets.

Note that though the

Kind

of
a Snippet may be persistent, that does not mean that the Snippet will
persist; For example it may be invalid or have been dropped. See:

Snippet.Status.isDefined()

.

Note that though the

Kind

of
a Snippet may be persistent, that does not mean that the Snippet will
persist; For example it may be invalid or have been dropped. See:

Snippet.Status.isDefined()

.

---

