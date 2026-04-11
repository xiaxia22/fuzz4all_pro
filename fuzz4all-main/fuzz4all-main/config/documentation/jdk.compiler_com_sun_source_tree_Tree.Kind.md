# Enum Tree.Kind

**Source:** `jdk.compiler\com\sun\source\tree\Tree.Kind.html`

### Class Description

```java
public static enum
Tree.Kind

extends
Enum
<
Tree.Kind
>
```

Enumerates all kinds of trees.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Tree.Kind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Tree.Kind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Tree.Kind c : Tree.Kind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Tree.Kind
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

#### public
Class
<? extends
Tree
> asInterface()

Returns the associated interface type that uses this kind.

**Returns:**
- the associated interface

---

### Additional Sections

#### Enum Tree.Kind

java.lang.Object

- java.lang.Enum

<

Tree.Kind

>
- - com.sun.source.tree.Tree.Kind

java.lang.Enum

<

Tree.Kind

>

- com.sun.source.tree.Tree.Kind

com.sun.source.tree.Tree.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

Tree.Kind

>

**Enclosing interface:** Tree

```java
public static enum
Tree.Kind

extends
Enum
<
Tree.Kind
>
```

Enumerates all kinds of trees.

public static enum

Tree.Kind

extends

Enum

<

Tree.Kind

>

Enumerates all kinds of trees.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

AND

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

AND_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

ANNOTATED_TYPE

Used for instances of

AnnotatedTypeTree

representing annotated types.

ANNOTATION

Used for instances of

AnnotationTree

representing declaration annotations.

ANNOTATION_TYPE

Used for instances of

ClassTree

representing annotation types.

ARRAY_ACCESS

Used for instances of

ArrayAccessTree

.

ARRAY_TYPE

Used for instances of

ArrayTypeTree

.

ASSERT

Used for instances of

AssertTree

.

ASSIGNMENT

Used for instances of

AssignmentTree

.

BITWISE_COMPLEMENT

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

BLOCK

Used for instances of

BlockTree

.

BOOLEAN_LITERAL

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

BREAK

Used for instances of

BreakTree

.

CASE

Used for instances of

CaseTree

.

CATCH

Used for instances of

CatchTree

.

CHAR_LITERAL

Used for instances of

LiteralTree

representing
a character literal expression of type

char

.

CLASS

Used for instances of

ClassTree

representing classes.

COMPILATION_UNIT

Used for instances of

CompilationUnitTree

.

CONDITIONAL_AND

Used for instances of

BinaryTree

representing
conditional-and

&&

.

CONDITIONAL_EXPRESSION

Used for instances of

ConditionalExpressionTree

.

CONDITIONAL_OR

Used for instances of

BinaryTree

representing
conditional-or

||

.

CONTINUE

Used for instances of

ContinueTree

.

DIVIDE

Used for instances of

BinaryTree

representing
division

/

.

DIVIDE_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

DO_WHILE_LOOP

Used for instances of

DoWhileLoopTree

.

DOUBLE_LITERAL

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

double

.

EMPTY_STATEMENT

Used for instances of

EmptyStatementTree

.

ENHANCED_FOR_LOOP

Used for instances of

EnhancedForLoopTree

.

ENUM

Used for instances of

ClassTree

representing enums.

EQUAL_TO

Used for instances of

BinaryTree

representing
equal-to

==

.

ERRONEOUS

Used for instances of

ErroneousTree

.

EXPORTS

Used for instances of

ExportsTree

representing
exports directives in a module declaration.

EXPRESSION_STATEMENT

Used for instances of

ExpressionStatementTree

.

EXTENDS_WILDCARD

Used for instances of

WildcardTree

representing
an extends bounded wildcard type argument.

FLOAT_LITERAL

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

float

.

FOR_LOOP

Used for instances of

ForLoopTree

.

GREATER_THAN

Used for instances of

BinaryTree

representing
greater-than

>

.

GREATER_THAN_EQUAL

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

IDENTIFIER

Used for instances of

IdentifierTree

.

IF

Used for instances of

IfTree

.

IMPORT

Used for instances of

ImportTree

.

INSTANCE_OF

Used for instances of

InstanceOfTree

.

INT_LITERAL

Used for instances of

LiteralTree

representing
an integral literal expression of type

int

.

INTERFACE

Used for instances of

ClassTree

representing interfaces.

INTERSECTION_TYPE

Used for instances of

IntersectionTypeTree

.

LABELED_STATEMENT

Used for instances of

LabeledStatementTree

.

LAMBDA_EXPRESSION

Used for instances of

LambdaExpressionTree

.

LEFT_SHIFT

Used for instances of

BinaryTree

representing
left shift

<<

.

LEFT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

LESS_THAN

Used for instances of

BinaryTree

representing
less-than

<

.

LESS_THAN_EQUAL

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

LOGICAL_COMPLEMENT

Used for instances of

UnaryTree

representing logical
complement operator

!

.

LONG_LITERAL

Used for instances of

LiteralTree

representing
an integral literal expression of type

long

.

MEMBER_REFERENCE

Used for instances of

MemberReferenceTree

.

MEMBER_SELECT

Used for instances of

MemberSelectTree

.

METHOD

Used for instances of

MethodTree

.

METHOD_INVOCATION

Used for instances of

MethodInvocationTree

.

MINUS

Used for instances of

BinaryTree

representing
subtraction

-

.

MINUS_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

MODIFIERS

Used for instances of

ModifiersTree

.

MODULE

Used for instances of

ModuleTree

representing module declarations.

MULTIPLY

Used for instances of

BinaryTree

representing
multiplication

*

.

MULTIPLY_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

NEW_ARRAY

Used for instances of

NewArrayTree

.

NEW_CLASS

Used for instances of

NewClassTree

.

NOT_EQUAL_TO

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

NULL_LITERAL

Used for instances of

LiteralTree

representing
the use of

null

.

OPENS

Used for instances of

ExportsTree

representing
opens directives in a module declaration.

OR

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

OR_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

OTHER

An implementation-reserved node.

PACKAGE

Used for instances of

PackageTree

.

PARAMETERIZED_TYPE

Used for instances of

ParameterizedTypeTree

.

PARENTHESIZED

Used for instances of

ParenthesizedTree

.

PLUS

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

PLUS_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

POSTFIX_DECREMENT

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

POSTFIX_INCREMENT

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

PREFIX_DECREMENT

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

PREFIX_INCREMENT

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

PRIMITIVE_TYPE

Used for instances of

PrimitiveTypeTree

.

PROVIDES

Used for instances of

ProvidesTree

representing
provides directives in a module declaration.

REMAINDER

Used for instances of

BinaryTree

representing
remainder

%

.

REMAINDER_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

REQUIRES

Used for instances of

RequiresTree

representing
requires directives in a module declaration.

RETURN

Used for instances of

ReturnTree

.

RIGHT_SHIFT

Used for instances of

BinaryTree

representing
right shift

>>

.

RIGHT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

STRING_LITERAL

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

SUPER_WILDCARD

Used for instances of

WildcardTree

representing
a super bounded wildcard type argument.

SWITCH

Used for instances of

SwitchTree

.

SYNCHRONIZED

Used for instances of

SynchronizedTree

.

THROW

Used for instances of

ThrowTree

.

TRY

Used for instances of

TryTree

.

TYPE_ANNOTATION

Used for instances of

AnnotationTree

representing type annotations.

TYPE_CAST

Used for instances of

TypeCastTree

.

TYPE_PARAMETER

Used for instances of

TypeParameterTree

.

UNARY_MINUS

Used for instances of

UnaryTree

representing unary minus
operator

-

.

UNARY_PLUS

Used for instances of

UnaryTree

representing unary plus
operator

+

.

UNBOUNDED_WILDCARD

Used for instances of

WildcardTree

representing
an unbounded wildcard type argument.

UNION_TYPE

Used for instances of

UnionTypeTree

.

UNSIGNED_RIGHT_SHIFT

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

USES

Used for instances of

UsesTree

representing
uses directives in a module declaration.

VARIABLE

Used for instances of

VariableTree

.

WHILE_LOOP

Used for instances of

WhileLoopTree

.

XOR

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

XOR_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Tree

>

asInterface

()

Returns the associated interface type that uses this kind.

static

Tree.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Tree.Kind

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

AND

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

AND_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

ANNOTATED_TYPE

Used for instances of

AnnotatedTypeTree

representing annotated types.

ANNOTATION

Used for instances of

AnnotationTree

representing declaration annotations.

ANNOTATION_TYPE

Used for instances of

ClassTree

representing annotation types.

ARRAY_ACCESS

Used for instances of

ArrayAccessTree

.

ARRAY_TYPE

Used for instances of

ArrayTypeTree

.

ASSERT

Used for instances of

AssertTree

.

ASSIGNMENT

Used for instances of

AssignmentTree

.

BITWISE_COMPLEMENT

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

BLOCK

Used for instances of

BlockTree

.

BOOLEAN_LITERAL

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

BREAK

Used for instances of

BreakTree

.

CASE

Used for instances of

CaseTree

.

CATCH

Used for instances of

CatchTree

.

CHAR_LITERAL

Used for instances of

LiteralTree

representing
a character literal expression of type

char

.

CLASS

Used for instances of

ClassTree

representing classes.

COMPILATION_UNIT

Used for instances of

CompilationUnitTree

.

CONDITIONAL_AND

Used for instances of

BinaryTree

representing
conditional-and

&&

.

CONDITIONAL_EXPRESSION

Used for instances of

ConditionalExpressionTree

.

CONDITIONAL_OR

Used for instances of

BinaryTree

representing
conditional-or

||

.

CONTINUE

Used for instances of

ContinueTree

.

DIVIDE

Used for instances of

BinaryTree

representing
division

/

.

DIVIDE_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

DO_WHILE_LOOP

Used for instances of

DoWhileLoopTree

.

DOUBLE_LITERAL

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

double

.

EMPTY_STATEMENT

Used for instances of

EmptyStatementTree

.

ENHANCED_FOR_LOOP

Used for instances of

EnhancedForLoopTree

.

ENUM

Used for instances of

ClassTree

representing enums.

EQUAL_TO

Used for instances of

BinaryTree

representing
equal-to

==

.

ERRONEOUS

Used for instances of

ErroneousTree

.

EXPORTS

Used for instances of

ExportsTree

representing
exports directives in a module declaration.

EXPRESSION_STATEMENT

Used for instances of

ExpressionStatementTree

.

EXTENDS_WILDCARD

Used for instances of

WildcardTree

representing
an extends bounded wildcard type argument.

FLOAT_LITERAL

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

float

.

FOR_LOOP

Used for instances of

ForLoopTree

.

GREATER_THAN

Used for instances of

BinaryTree

representing
greater-than

>

.

GREATER_THAN_EQUAL

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

IDENTIFIER

Used for instances of

IdentifierTree

.

IF

Used for instances of

IfTree

.

IMPORT

Used for instances of

ImportTree

.

INSTANCE_OF

Used for instances of

InstanceOfTree

.

INT_LITERAL

Used for instances of

LiteralTree

representing
an integral literal expression of type

int

.

INTERFACE

Used for instances of

ClassTree

representing interfaces.

INTERSECTION_TYPE

Used for instances of

IntersectionTypeTree

.

LABELED_STATEMENT

Used for instances of

LabeledStatementTree

.

LAMBDA_EXPRESSION

Used for instances of

LambdaExpressionTree

.

LEFT_SHIFT

Used for instances of

BinaryTree

representing
left shift

<<

.

LEFT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

LESS_THAN

Used for instances of

BinaryTree

representing
less-than

<

.

LESS_THAN_EQUAL

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

LOGICAL_COMPLEMENT

Used for instances of

UnaryTree

representing logical
complement operator

!

.

LONG_LITERAL

Used for instances of

LiteralTree

representing
an integral literal expression of type

long

.

MEMBER_REFERENCE

Used for instances of

MemberReferenceTree

.

MEMBER_SELECT

Used for instances of

MemberSelectTree

.

METHOD

Used for instances of

MethodTree

.

METHOD_INVOCATION

Used for instances of

MethodInvocationTree

.

MINUS

Used for instances of

BinaryTree

representing
subtraction

-

.

MINUS_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

MODIFIERS

Used for instances of

ModifiersTree

.

MODULE

Used for instances of

ModuleTree

representing module declarations.

MULTIPLY

Used for instances of

BinaryTree

representing
multiplication

*

.

MULTIPLY_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

NEW_ARRAY

Used for instances of

NewArrayTree

.

NEW_CLASS

Used for instances of

NewClassTree

.

NOT_EQUAL_TO

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

NULL_LITERAL

Used for instances of

LiteralTree

representing
the use of

null

.

OPENS

Used for instances of

ExportsTree

representing
opens directives in a module declaration.

OR

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

OR_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

OTHER

An implementation-reserved node.

PACKAGE

Used for instances of

PackageTree

.

PARAMETERIZED_TYPE

Used for instances of

ParameterizedTypeTree

.

PARENTHESIZED

Used for instances of

ParenthesizedTree

.

PLUS

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

PLUS_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

POSTFIX_DECREMENT

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

POSTFIX_INCREMENT

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

PREFIX_DECREMENT

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

PREFIX_INCREMENT

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

PRIMITIVE_TYPE

Used for instances of

PrimitiveTypeTree

.

PROVIDES

Used for instances of

ProvidesTree

representing
provides directives in a module declaration.

REMAINDER

Used for instances of

BinaryTree

representing
remainder

%

.

REMAINDER_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

REQUIRES

Used for instances of

RequiresTree

representing
requires directives in a module declaration.

RETURN

Used for instances of

ReturnTree

.

RIGHT_SHIFT

Used for instances of

BinaryTree

representing
right shift

>>

.

RIGHT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

STRING_LITERAL

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

SUPER_WILDCARD

Used for instances of

WildcardTree

representing
a super bounded wildcard type argument.

SWITCH

Used for instances of

SwitchTree

.

SYNCHRONIZED

Used for instances of

SynchronizedTree

.

THROW

Used for instances of

ThrowTree

.

TRY

Used for instances of

TryTree

.

TYPE_ANNOTATION

Used for instances of

AnnotationTree

representing type annotations.

TYPE_CAST

Used for instances of

TypeCastTree

.

TYPE_PARAMETER

Used for instances of

TypeParameterTree

.

UNARY_MINUS

Used for instances of

UnaryTree

representing unary minus
operator

-

.

UNARY_PLUS

Used for instances of

UnaryTree

representing unary plus
operator

+

.

UNBOUNDED_WILDCARD

Used for instances of

WildcardTree

representing
an unbounded wildcard type argument.

UNION_TYPE

Used for instances of

UnionTypeTree

.

UNSIGNED_RIGHT_SHIFT

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

USES

Used for instances of

UsesTree

representing
uses directives in a module declaration.

VARIABLE

Used for instances of

VariableTree

.

WHILE_LOOP

Used for instances of

WhileLoopTree

.

XOR

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

XOR_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

---

#### Enum Constant Summary

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

Used for instances of

AnnotatedTypeTree

representing annotated types.

Used for instances of

AnnotationTree

representing declaration annotations.

Used for instances of

ClassTree

representing annotation types.

Used for instances of

ArrayAccessTree

.

Used for instances of

ArrayTypeTree

.

Used for instances of

AssertTree

.

Used for instances of

AssignmentTree

.

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

Used for instances of

BlockTree

.

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

Used for instances of

BreakTree

.

Used for instances of

CaseTree

.

Used for instances of

CatchTree

.

Used for instances of

LiteralTree

representing
a character literal expression of type

char

.

Used for instances of

ClassTree

representing classes.

Used for instances of

CompilationUnitTree

.

Used for instances of

BinaryTree

representing
conditional-and

&&

.

Used for instances of

ConditionalExpressionTree

.

Used for instances of

BinaryTree

representing
conditional-or

||

.

Used for instances of

ContinueTree

.

Used for instances of

BinaryTree

representing
division

/

.

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

Used for instances of

DoWhileLoopTree

.

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

double

.

Used for instances of

EmptyStatementTree

.

Used for instances of

EnhancedForLoopTree

.

Used for instances of

ClassTree

representing enums.

Used for instances of

BinaryTree

representing
equal-to

==

.

Used for instances of

ErroneousTree

.

Used for instances of

ExportsTree

representing
exports directives in a module declaration.

Used for instances of

ExpressionStatementTree

.

Used for instances of

WildcardTree

representing
an extends bounded wildcard type argument.

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

float

.

Used for instances of

ForLoopTree

.

Used for instances of

BinaryTree

representing
greater-than

>

.

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

Used for instances of

IdentifierTree

.

Used for instances of

IfTree

.

Used for instances of

ImportTree

.

Used for instances of

InstanceOfTree

.

Used for instances of

LiteralTree

representing
an integral literal expression of type

int

.

Used for instances of

ClassTree

representing interfaces.

Used for instances of

IntersectionTypeTree

.

Used for instances of

LabeledStatementTree

.

Used for instances of

LambdaExpressionTree

.

Used for instances of

BinaryTree

representing
left shift

<<

.

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

Used for instances of

BinaryTree

representing
less-than

<

.

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

Used for instances of

UnaryTree

representing logical
complement operator

!

.

Used for instances of

LiteralTree

representing
an integral literal expression of type

long

.

Used for instances of

MemberReferenceTree

.

Used for instances of

MemberSelectTree

.

Used for instances of

MethodTree

.

Used for instances of

MethodInvocationTree

.

Used for instances of

BinaryTree

representing
subtraction

-

.

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

Used for instances of

ModifiersTree

.

Used for instances of

ModuleTree

representing module declarations.

Used for instances of

BinaryTree

representing
multiplication

*

.

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

Used for instances of

NewArrayTree

.

Used for instances of

NewClassTree

.

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

Used for instances of

LiteralTree

representing
the use of

null

.

Used for instances of

ExportsTree

representing
opens directives in a module declaration.

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

An implementation-reserved node.

Used for instances of

PackageTree

.

Used for instances of

ParameterizedTypeTree

.

Used for instances of

ParenthesizedTree

.

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

Used for instances of

PrimitiveTypeTree

.

Used for instances of

ProvidesTree

representing
provides directives in a module declaration.

Used for instances of

BinaryTree

representing
remainder

%

.

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

Used for instances of

RequiresTree

representing
requires directives in a module declaration.

Used for instances of

ReturnTree

.

Used for instances of

BinaryTree

representing
right shift

>>

.

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

Used for instances of

WildcardTree

representing
a super bounded wildcard type argument.

Used for instances of

SwitchTree

.

Used for instances of

SynchronizedTree

.

Used for instances of

ThrowTree

.

Used for instances of

TryTree

.

Used for instances of

AnnotationTree

representing type annotations.

Used for instances of

TypeCastTree

.

Used for instances of

TypeParameterTree

.

Used for instances of

UnaryTree

representing unary minus
operator

-

.

Used for instances of

UnaryTree

representing unary plus
operator

+

.

Used for instances of

WildcardTree

representing
an unbounded wildcard type argument.

Used for instances of

UnionTypeTree

.

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

Used for instances of

UsesTree

representing
uses directives in a module declaration.

Used for instances of

VariableTree

.

Used for instances of

WhileLoopTree

.

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Tree

>

asInterface

()

Returns the associated interface type that uses this kind.

static

Tree.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Tree.Kind

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

Returns the associated interface type that uses this kind.

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

- ANNOTATED_TYPE

```java
public static final
Tree.Kind
ANNOTATED_TYPE
```

Used for instances of

AnnotatedTypeTree

representing annotated types.

- ANNOTATION

```java
public static final
Tree.Kind
ANNOTATION
```

Used for instances of

AnnotationTree

representing declaration annotations.

- TYPE_ANNOTATION

```java
public static final
Tree.Kind
TYPE_ANNOTATION
```

Used for instances of

AnnotationTree

representing type annotations.

- ARRAY_ACCESS

```java
public static final
Tree.Kind
ARRAY_ACCESS
```

Used for instances of

ArrayAccessTree

.

- ARRAY_TYPE

```java
public static final
Tree.Kind
ARRAY_TYPE
```

Used for instances of

ArrayTypeTree

.

- ASSERT

```java
public static final
Tree.Kind
ASSERT
```

Used for instances of

AssertTree

.

- ASSIGNMENT

```java
public static final
Tree.Kind
ASSIGNMENT
```

Used for instances of

AssignmentTree

.

- BLOCK

```java
public static final
Tree.Kind
BLOCK
```

Used for instances of

BlockTree

.

- BREAK

```java
public static final
Tree.Kind
BREAK
```

Used for instances of

BreakTree

.

- CASE

```java
public static final
Tree.Kind
CASE
```

Used for instances of

CaseTree

.

- CATCH

```java
public static final
Tree.Kind
CATCH
```

Used for instances of

CatchTree

.

- CLASS

```java
public static final
Tree.Kind
CLASS
```

Used for instances of

ClassTree

representing classes.

- COMPILATION_UNIT

```java
public static final
Tree.Kind
COMPILATION_UNIT
```

Used for instances of

CompilationUnitTree

.

- CONDITIONAL_EXPRESSION

```java
public static final
Tree.Kind
CONDITIONAL_EXPRESSION
```

Used for instances of

ConditionalExpressionTree

.

- CONTINUE

```java
public static final
Tree.Kind
CONTINUE
```

Used for instances of

ContinueTree

.

- DO_WHILE_LOOP

```java
public static final
Tree.Kind
DO_WHILE_LOOP
```

Used for instances of

DoWhileLoopTree

.

- ENHANCED_FOR_LOOP

```java
public static final
Tree.Kind
ENHANCED_FOR_LOOP
```

Used for instances of

EnhancedForLoopTree

.

- EXPRESSION_STATEMENT

```java
public static final
Tree.Kind
EXPRESSION_STATEMENT
```

Used for instances of

ExpressionStatementTree

.

- MEMBER_SELECT

```java
public static final
Tree.Kind
MEMBER_SELECT
```

Used for instances of

MemberSelectTree

.

- MEMBER_REFERENCE

```java
public static final
Tree.Kind
MEMBER_REFERENCE
```

Used for instances of

MemberReferenceTree

.

- FOR_LOOP

```java
public static final
Tree.Kind
FOR_LOOP
```

Used for instances of

ForLoopTree

.

- IDENTIFIER

```java
public static final
Tree.Kind
IDENTIFIER
```

Used for instances of

IdentifierTree

.

- IF

```java
public static final
Tree.Kind
IF
```

Used for instances of

IfTree

.

- IMPORT

```java
public static final
Tree.Kind
IMPORT
```

Used for instances of

ImportTree

.

- INSTANCE_OF

```java
public static final
Tree.Kind
INSTANCE_OF
```

Used for instances of

InstanceOfTree

.

- LABELED_STATEMENT

```java
public static final
Tree.Kind
LABELED_STATEMENT
```

Used for instances of

LabeledStatementTree

.

- METHOD

```java
public static final
Tree.Kind
METHOD
```

Used for instances of

MethodTree

.

- METHOD_INVOCATION

```java
public static final
Tree.Kind
METHOD_INVOCATION
```

Used for instances of

MethodInvocationTree

.

- MODIFIERS

```java
public static final
Tree.Kind
MODIFIERS
```

Used for instances of

ModifiersTree

.

- NEW_ARRAY

```java
public static final
Tree.Kind
NEW_ARRAY
```

Used for instances of

NewArrayTree

.

- NEW_CLASS

```java
public static final
Tree.Kind
NEW_CLASS
```

Used for instances of

NewClassTree

.

- LAMBDA_EXPRESSION

```java
public static final
Tree.Kind
LAMBDA_EXPRESSION
```

Used for instances of

LambdaExpressionTree

.

- PACKAGE

```java
public static final
Tree.Kind
PACKAGE
```

Used for instances of

PackageTree

.

**Since:** 9

- PARENTHESIZED

```java
public static final
Tree.Kind
PARENTHESIZED
```

Used for instances of

ParenthesizedTree

.

- PRIMITIVE_TYPE

```java
public static final
Tree.Kind
PRIMITIVE_TYPE
```

Used for instances of

PrimitiveTypeTree

.

- RETURN

```java
public static final
Tree.Kind
RETURN
```

Used for instances of

ReturnTree

.

- EMPTY_STATEMENT

```java
public static final
Tree.Kind
EMPTY_STATEMENT
```

Used for instances of

EmptyStatementTree

.

- SWITCH

```java
public static final
Tree.Kind
SWITCH
```

Used for instances of

SwitchTree

.

- SYNCHRONIZED

```java
public static final
Tree.Kind
SYNCHRONIZED
```

Used for instances of

SynchronizedTree

.

- THROW

```java
public static final
Tree.Kind
THROW
```

Used for instances of

ThrowTree

.

- TRY

```java
public static final
Tree.Kind
TRY
```

Used for instances of

TryTree

.

- PARAMETERIZED_TYPE

```java
public static final
Tree.Kind
PARAMETERIZED_TYPE
```

Used for instances of

ParameterizedTypeTree

.

- UNION_TYPE

```java
public static final
Tree.Kind
UNION_TYPE
```

Used for instances of

UnionTypeTree

.

- INTERSECTION_TYPE

```java
public static final
Tree.Kind
INTERSECTION_TYPE
```

Used for instances of

IntersectionTypeTree

.

- TYPE_CAST

```java
public static final
Tree.Kind
TYPE_CAST
```

Used for instances of

TypeCastTree

.

- TYPE_PARAMETER

```java
public static final
Tree.Kind
TYPE_PARAMETER
```

Used for instances of

TypeParameterTree

.

- VARIABLE

```java
public static final
Tree.Kind
VARIABLE
```

Used for instances of

VariableTree

.

- WHILE_LOOP

```java
public static final
Tree.Kind
WHILE_LOOP
```

Used for instances of

WhileLoopTree

.

- POSTFIX_INCREMENT

```java
public static final
Tree.Kind
POSTFIX_INCREMENT
```

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

- POSTFIX_DECREMENT

```java
public static final
Tree.Kind
POSTFIX_DECREMENT
```

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

- PREFIX_INCREMENT

```java
public static final
Tree.Kind
PREFIX_INCREMENT
```

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

- PREFIX_DECREMENT

```java
public static final
Tree.Kind
PREFIX_DECREMENT
```

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

- UNARY_PLUS

```java
public static final
Tree.Kind
UNARY_PLUS
```

Used for instances of

UnaryTree

representing unary plus
operator

+

.

- UNARY_MINUS

```java
public static final
Tree.Kind
UNARY_MINUS
```

Used for instances of

UnaryTree

representing unary minus
operator

-

.

- BITWISE_COMPLEMENT

```java
public static final
Tree.Kind
BITWISE_COMPLEMENT
```

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

- LOGICAL_COMPLEMENT

```java
public static final
Tree.Kind
LOGICAL_COMPLEMENT
```

Used for instances of

UnaryTree

representing logical
complement operator

!

.

- MULTIPLY

```java
public static final
Tree.Kind
MULTIPLY
```

Used for instances of

BinaryTree

representing
multiplication

*

.

- DIVIDE

```java
public static final
Tree.Kind
DIVIDE
```

Used for instances of

BinaryTree

representing
division

/

.

- REMAINDER

```java
public static final
Tree.Kind
REMAINDER
```

Used for instances of

BinaryTree

representing
remainder

%

.

- PLUS

```java
public static final
Tree.Kind
PLUS
```

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

- MINUS

```java
public static final
Tree.Kind
MINUS
```

Used for instances of

BinaryTree

representing
subtraction

-

.

- LEFT_SHIFT

```java
public static final
Tree.Kind
LEFT_SHIFT
```

Used for instances of

BinaryTree

representing
left shift

<<

.

- RIGHT_SHIFT

```java
public static final
Tree.Kind
RIGHT_SHIFT
```

Used for instances of

BinaryTree

representing
right shift

>>

.

- UNSIGNED_RIGHT_SHIFT

```java
public static final
Tree.Kind
UNSIGNED_RIGHT_SHIFT
```

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

- LESS_THAN

```java
public static final
Tree.Kind
LESS_THAN
```

Used for instances of

BinaryTree

representing
less-than

<

.

- GREATER_THAN

```java
public static final
Tree.Kind
GREATER_THAN
```

Used for instances of

BinaryTree

representing
greater-than

>

.

- LESS_THAN_EQUAL

```java
public static final
Tree.Kind
LESS_THAN_EQUAL
```

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

- GREATER_THAN_EQUAL

```java
public static final
Tree.Kind
GREATER_THAN_EQUAL
```

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

- EQUAL_TO

```java
public static final
Tree.Kind
EQUAL_TO
```

Used for instances of

BinaryTree

representing
equal-to

==

.

- NOT_EQUAL_TO

```java
public static final
Tree.Kind
NOT_EQUAL_TO
```

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

- AND

```java
public static final
Tree.Kind
AND
```

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

- XOR

```java
public static final
Tree.Kind
XOR
```

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

- OR

```java
public static final
Tree.Kind
OR
```

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

- CONDITIONAL_AND

```java
public static final
Tree.Kind
CONDITIONAL_AND
```

Used for instances of

BinaryTree

representing
conditional-and

&&

.

- CONDITIONAL_OR

```java
public static final
Tree.Kind
CONDITIONAL_OR
```

Used for instances of

BinaryTree

representing
conditional-or

||

.

- MULTIPLY_ASSIGNMENT

```java
public static final
Tree.Kind
MULTIPLY_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

- DIVIDE_ASSIGNMENT

```java
public static final
Tree.Kind
DIVIDE_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

- REMAINDER_ASSIGNMENT

```java
public static final
Tree.Kind
REMAINDER_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

- PLUS_ASSIGNMENT

```java
public static final
Tree.Kind
PLUS_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

- MINUS_ASSIGNMENT

```java
public static final
Tree.Kind
MINUS_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

- LEFT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
LEFT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

- RIGHT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
RIGHT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

- UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
UNSIGNED_RIGHT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

- AND_ASSIGNMENT

```java
public static final
Tree.Kind
AND_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

- XOR_ASSIGNMENT

```java
public static final
Tree.Kind
XOR_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

- OR_ASSIGNMENT

```java
public static final
Tree.Kind
OR_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

- INT_LITERAL

```java
public static final
Tree.Kind
INT_LITERAL
```

Used for instances of

LiteralTree

representing
an integral literal expression of type

int

.

- LONG_LITERAL

```java
public static final
Tree.Kind
LONG_LITERAL
```

Used for instances of

LiteralTree

representing
an integral literal expression of type

long

.

- FLOAT_LITERAL

```java
public static final
Tree.Kind
FLOAT_LITERAL
```

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

float

.

- DOUBLE_LITERAL

```java
public static final
Tree.Kind
DOUBLE_LITERAL
```

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

double

.

- BOOLEAN_LITERAL

```java
public static final
Tree.Kind
BOOLEAN_LITERAL
```

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

- CHAR_LITERAL

```java
public static final
Tree.Kind
CHAR_LITERAL
```

Used for instances of

LiteralTree

representing
a character literal expression of type

char

.

- STRING_LITERAL

```java
public static final
Tree.Kind
STRING_LITERAL
```

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

- NULL_LITERAL

```java
public static final
Tree.Kind
NULL_LITERAL
```

Used for instances of

LiteralTree

representing
the use of

null

.

- UNBOUNDED_WILDCARD

```java
public static final
Tree.Kind
UNBOUNDED_WILDCARD
```

Used for instances of

WildcardTree

representing
an unbounded wildcard type argument.

- EXTENDS_WILDCARD

```java
public static final
Tree.Kind
EXTENDS_WILDCARD
```

Used for instances of

WildcardTree

representing
an extends bounded wildcard type argument.

- SUPER_WILDCARD

```java
public static final
Tree.Kind
SUPER_WILDCARD
```

Used for instances of

WildcardTree

representing
a super bounded wildcard type argument.

- ERRONEOUS

```java
public static final
Tree.Kind
ERRONEOUS
```

Used for instances of

ErroneousTree

.

- INTERFACE

```java
public static final
Tree.Kind
INTERFACE
```

Used for instances of

ClassTree

representing interfaces.

- ENUM

```java
public static final
Tree.Kind
ENUM
```

Used for instances of

ClassTree

representing enums.

- ANNOTATION_TYPE

```java
public static final
Tree.Kind
ANNOTATION_TYPE
```

Used for instances of

ClassTree

representing annotation types.

- MODULE

```java
public static final
Tree.Kind
MODULE
```

Used for instances of

ModuleTree

representing module declarations.

- EXPORTS

```java
public static final
Tree.Kind
EXPORTS
```

Used for instances of

ExportsTree

representing
exports directives in a module declaration.

- OPENS

```java
public static final
Tree.Kind
OPENS
```

Used for instances of

ExportsTree

representing
opens directives in a module declaration.

- PROVIDES

```java
public static final
Tree.Kind
PROVIDES
```

Used for instances of

ProvidesTree

representing
provides directives in a module declaration.

- REQUIRES

```java
public static final
Tree.Kind
REQUIRES
```

Used for instances of

RequiresTree

representing
requires directives in a module declaration.

- USES

```java
public static final
Tree.Kind
USES
```

Used for instances of

UsesTree

representing
uses directives in a module declaration.

- OTHER

```java
public static final
Tree.Kind
OTHER
```

An implementation-reserved node. This is the not the node
you are looking for.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Tree.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Tree.Kind c : Tree.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Tree.Kind
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

- asInterface

```java
public
Class
<? extends
Tree
> asInterface()
```

Returns the associated interface type that uses this kind.

**Returns:** the associated interface

Enum Constant Detail

- ANNOTATED_TYPE

```java
public static final
Tree.Kind
ANNOTATED_TYPE
```

Used for instances of

AnnotatedTypeTree

representing annotated types.

- ANNOTATION

```java
public static final
Tree.Kind
ANNOTATION
```

Used for instances of

AnnotationTree

representing declaration annotations.

- TYPE_ANNOTATION

```java
public static final
Tree.Kind
TYPE_ANNOTATION
```

Used for instances of

AnnotationTree

representing type annotations.

- ARRAY_ACCESS

```java
public static final
Tree.Kind
ARRAY_ACCESS
```

Used for instances of

ArrayAccessTree

.

- ARRAY_TYPE

```java
public static final
Tree.Kind
ARRAY_TYPE
```

Used for instances of

ArrayTypeTree

.

- ASSERT

```java
public static final
Tree.Kind
ASSERT
```

Used for instances of

AssertTree

.

- ASSIGNMENT

```java
public static final
Tree.Kind
ASSIGNMENT
```

Used for instances of

AssignmentTree

.

- BLOCK

```java
public static final
Tree.Kind
BLOCK
```

Used for instances of

BlockTree

.

- BREAK

```java
public static final
Tree.Kind
BREAK
```

Used for instances of

BreakTree

.

- CASE

```java
public static final
Tree.Kind
CASE
```

Used for instances of

CaseTree

.

- CATCH

```java
public static final
Tree.Kind
CATCH
```

Used for instances of

CatchTree

.

- CLASS

```java
public static final
Tree.Kind
CLASS
```

Used for instances of

ClassTree

representing classes.

- COMPILATION_UNIT

```java
public static final
Tree.Kind
COMPILATION_UNIT
```

Used for instances of

CompilationUnitTree

.

- CONDITIONAL_EXPRESSION

```java
public static final
Tree.Kind
CONDITIONAL_EXPRESSION
```

Used for instances of

ConditionalExpressionTree

.

- CONTINUE

```java
public static final
Tree.Kind
CONTINUE
```

Used for instances of

ContinueTree

.

- DO_WHILE_LOOP

```java
public static final
Tree.Kind
DO_WHILE_LOOP
```

Used for instances of

DoWhileLoopTree

.

- ENHANCED_FOR_LOOP

```java
public static final
Tree.Kind
ENHANCED_FOR_LOOP
```

Used for instances of

EnhancedForLoopTree

.

- EXPRESSION_STATEMENT

```java
public static final
Tree.Kind
EXPRESSION_STATEMENT
```

Used for instances of

ExpressionStatementTree

.

- MEMBER_SELECT

```java
public static final
Tree.Kind
MEMBER_SELECT
```

Used for instances of

MemberSelectTree

.

- MEMBER_REFERENCE

```java
public static final
Tree.Kind
MEMBER_REFERENCE
```

Used for instances of

MemberReferenceTree

.

- FOR_LOOP

```java
public static final
Tree.Kind
FOR_LOOP
```

Used for instances of

ForLoopTree

.

- IDENTIFIER

```java
public static final
Tree.Kind
IDENTIFIER
```

Used for instances of

IdentifierTree

.

- IF

```java
public static final
Tree.Kind
IF
```

Used for instances of

IfTree

.

- IMPORT

```java
public static final
Tree.Kind
IMPORT
```

Used for instances of

ImportTree

.

- INSTANCE_OF

```java
public static final
Tree.Kind
INSTANCE_OF
```

Used for instances of

InstanceOfTree

.

- LABELED_STATEMENT

```java
public static final
Tree.Kind
LABELED_STATEMENT
```

Used for instances of

LabeledStatementTree

.

- METHOD

```java
public static final
Tree.Kind
METHOD
```

Used for instances of

MethodTree

.

- METHOD_INVOCATION

```java
public static final
Tree.Kind
METHOD_INVOCATION
```

Used for instances of

MethodInvocationTree

.

- MODIFIERS

```java
public static final
Tree.Kind
MODIFIERS
```

Used for instances of

ModifiersTree

.

- NEW_ARRAY

```java
public static final
Tree.Kind
NEW_ARRAY
```

Used for instances of

NewArrayTree

.

- NEW_CLASS

```java
public static final
Tree.Kind
NEW_CLASS
```

Used for instances of

NewClassTree

.

- LAMBDA_EXPRESSION

```java
public static final
Tree.Kind
LAMBDA_EXPRESSION
```

Used for instances of

LambdaExpressionTree

.

- PACKAGE

```java
public static final
Tree.Kind
PACKAGE
```

Used for instances of

PackageTree

.

**Since:** 9

- PARENTHESIZED

```java
public static final
Tree.Kind
PARENTHESIZED
```

Used for instances of

ParenthesizedTree

.

- PRIMITIVE_TYPE

```java
public static final
Tree.Kind
PRIMITIVE_TYPE
```

Used for instances of

PrimitiveTypeTree

.

- RETURN

```java
public static final
Tree.Kind
RETURN
```

Used for instances of

ReturnTree

.

- EMPTY_STATEMENT

```java
public static final
Tree.Kind
EMPTY_STATEMENT
```

Used for instances of

EmptyStatementTree

.

- SWITCH

```java
public static final
Tree.Kind
SWITCH
```

Used for instances of

SwitchTree

.

- SYNCHRONIZED

```java
public static final
Tree.Kind
SYNCHRONIZED
```

Used for instances of

SynchronizedTree

.

- THROW

```java
public static final
Tree.Kind
THROW
```

Used for instances of

ThrowTree

.

- TRY

```java
public static final
Tree.Kind
TRY
```

Used for instances of

TryTree

.

- PARAMETERIZED_TYPE

```java
public static final
Tree.Kind
PARAMETERIZED_TYPE
```

Used for instances of

ParameterizedTypeTree

.

- UNION_TYPE

```java
public static final
Tree.Kind
UNION_TYPE
```

Used for instances of

UnionTypeTree

.

- INTERSECTION_TYPE

```java
public static final
Tree.Kind
INTERSECTION_TYPE
```

Used for instances of

IntersectionTypeTree

.

- TYPE_CAST

```java
public static final
Tree.Kind
TYPE_CAST
```

Used for instances of

TypeCastTree

.

- TYPE_PARAMETER

```java
public static final
Tree.Kind
TYPE_PARAMETER
```

Used for instances of

TypeParameterTree

.

- VARIABLE

```java
public static final
Tree.Kind
VARIABLE
```

Used for instances of

VariableTree

.

- WHILE_LOOP

```java
public static final
Tree.Kind
WHILE_LOOP
```

Used for instances of

WhileLoopTree

.

- POSTFIX_INCREMENT

```java
public static final
Tree.Kind
POSTFIX_INCREMENT
```

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

- POSTFIX_DECREMENT

```java
public static final
Tree.Kind
POSTFIX_DECREMENT
```

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

- PREFIX_INCREMENT

```java
public static final
Tree.Kind
PREFIX_INCREMENT
```

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

- PREFIX_DECREMENT

```java
public static final
Tree.Kind
PREFIX_DECREMENT
```

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

- UNARY_PLUS

```java
public static final
Tree.Kind
UNARY_PLUS
```

Used for instances of

UnaryTree

representing unary plus
operator

+

.

- UNARY_MINUS

```java
public static final
Tree.Kind
UNARY_MINUS
```

Used for instances of

UnaryTree

representing unary minus
operator

-

.

- BITWISE_COMPLEMENT

```java
public static final
Tree.Kind
BITWISE_COMPLEMENT
```

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

- LOGICAL_COMPLEMENT

```java
public static final
Tree.Kind
LOGICAL_COMPLEMENT
```

Used for instances of

UnaryTree

representing logical
complement operator

!

.

- MULTIPLY

```java
public static final
Tree.Kind
MULTIPLY
```

Used for instances of

BinaryTree

representing
multiplication

*

.

- DIVIDE

```java
public static final
Tree.Kind
DIVIDE
```

Used for instances of

BinaryTree

representing
division

/

.

- REMAINDER

```java
public static final
Tree.Kind
REMAINDER
```

Used for instances of

BinaryTree

representing
remainder

%

.

- PLUS

```java
public static final
Tree.Kind
PLUS
```

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

- MINUS

```java
public static final
Tree.Kind
MINUS
```

Used for instances of

BinaryTree

representing
subtraction

-

.

- LEFT_SHIFT

```java
public static final
Tree.Kind
LEFT_SHIFT
```

Used for instances of

BinaryTree

representing
left shift

<<

.

- RIGHT_SHIFT

```java
public static final
Tree.Kind
RIGHT_SHIFT
```

Used for instances of

BinaryTree

representing
right shift

>>

.

- UNSIGNED_RIGHT_SHIFT

```java
public static final
Tree.Kind
UNSIGNED_RIGHT_SHIFT
```

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

- LESS_THAN

```java
public static final
Tree.Kind
LESS_THAN
```

Used for instances of

BinaryTree

representing
less-than

<

.

- GREATER_THAN

```java
public static final
Tree.Kind
GREATER_THAN
```

Used for instances of

BinaryTree

representing
greater-than

>

.

- LESS_THAN_EQUAL

```java
public static final
Tree.Kind
LESS_THAN_EQUAL
```

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

- GREATER_THAN_EQUAL

```java
public static final
Tree.Kind
GREATER_THAN_EQUAL
```

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

- EQUAL_TO

```java
public static final
Tree.Kind
EQUAL_TO
```

Used for instances of

BinaryTree

representing
equal-to

==

.

- NOT_EQUAL_TO

```java
public static final
Tree.Kind
NOT_EQUAL_TO
```

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

- AND

```java
public static final
Tree.Kind
AND
```

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

- XOR

```java
public static final
Tree.Kind
XOR
```

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

- OR

```java
public static final
Tree.Kind
OR
```

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

- CONDITIONAL_AND

```java
public static final
Tree.Kind
CONDITIONAL_AND
```

Used for instances of

BinaryTree

representing
conditional-and

&&

.

- CONDITIONAL_OR

```java
public static final
Tree.Kind
CONDITIONAL_OR
```

Used for instances of

BinaryTree

representing
conditional-or

||

.

- MULTIPLY_ASSIGNMENT

```java
public static final
Tree.Kind
MULTIPLY_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

- DIVIDE_ASSIGNMENT

```java
public static final
Tree.Kind
DIVIDE_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

- REMAINDER_ASSIGNMENT

```java
public static final
Tree.Kind
REMAINDER_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

- PLUS_ASSIGNMENT

```java
public static final
Tree.Kind
PLUS_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

- MINUS_ASSIGNMENT

```java
public static final
Tree.Kind
MINUS_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

- LEFT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
LEFT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

- RIGHT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
RIGHT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

- UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
UNSIGNED_RIGHT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

- AND_ASSIGNMENT

```java
public static final
Tree.Kind
AND_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

- XOR_ASSIGNMENT

```java
public static final
Tree.Kind
XOR_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

- OR_ASSIGNMENT

```java
public static final
Tree.Kind
OR_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

- INT_LITERAL

```java
public static final
Tree.Kind
INT_LITERAL
```

Used for instances of

LiteralTree

representing
an integral literal expression of type

int

.

- LONG_LITERAL

```java
public static final
Tree.Kind
LONG_LITERAL
```

Used for instances of

LiteralTree

representing
an integral literal expression of type

long

.

- FLOAT_LITERAL

```java
public static final
Tree.Kind
FLOAT_LITERAL
```

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

float

.

- DOUBLE_LITERAL

```java
public static final
Tree.Kind
DOUBLE_LITERAL
```

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

double

.

- BOOLEAN_LITERAL

```java
public static final
Tree.Kind
BOOLEAN_LITERAL
```

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

- CHAR_LITERAL

```java
public static final
Tree.Kind
CHAR_LITERAL
```

Used for instances of

LiteralTree

representing
a character literal expression of type

char

.

- STRING_LITERAL

```java
public static final
Tree.Kind
STRING_LITERAL
```

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

- NULL_LITERAL

```java
public static final
Tree.Kind
NULL_LITERAL
```

Used for instances of

LiteralTree

representing
the use of

null

.

- UNBOUNDED_WILDCARD

```java
public static final
Tree.Kind
UNBOUNDED_WILDCARD
```

Used for instances of

WildcardTree

representing
an unbounded wildcard type argument.

- EXTENDS_WILDCARD

```java
public static final
Tree.Kind
EXTENDS_WILDCARD
```

Used for instances of

WildcardTree

representing
an extends bounded wildcard type argument.

- SUPER_WILDCARD

```java
public static final
Tree.Kind
SUPER_WILDCARD
```

Used for instances of

WildcardTree

representing
a super bounded wildcard type argument.

- ERRONEOUS

```java
public static final
Tree.Kind
ERRONEOUS
```

Used for instances of

ErroneousTree

.

- INTERFACE

```java
public static final
Tree.Kind
INTERFACE
```

Used for instances of

ClassTree

representing interfaces.

- ENUM

```java
public static final
Tree.Kind
ENUM
```

Used for instances of

ClassTree

representing enums.

- ANNOTATION_TYPE

```java
public static final
Tree.Kind
ANNOTATION_TYPE
```

Used for instances of

ClassTree

representing annotation types.

- MODULE

```java
public static final
Tree.Kind
MODULE
```

Used for instances of

ModuleTree

representing module declarations.

- EXPORTS

```java
public static final
Tree.Kind
EXPORTS
```

Used for instances of

ExportsTree

representing
exports directives in a module declaration.

- OPENS

```java
public static final
Tree.Kind
OPENS
```

Used for instances of

ExportsTree

representing
opens directives in a module declaration.

- PROVIDES

```java
public static final
Tree.Kind
PROVIDES
```

Used for instances of

ProvidesTree

representing
provides directives in a module declaration.

- REQUIRES

```java
public static final
Tree.Kind
REQUIRES
```

Used for instances of

RequiresTree

representing
requires directives in a module declaration.

- USES

```java
public static final
Tree.Kind
USES
```

Used for instances of

UsesTree

representing
uses directives in a module declaration.

- OTHER

```java
public static final
Tree.Kind
OTHER
```

An implementation-reserved node. This is the not the node
you are looking for.

---

#### Enum Constant Detail

ANNOTATED_TYPE

```java
public static final
Tree.Kind
ANNOTATED_TYPE
```

Used for instances of

AnnotatedTypeTree

representing annotated types.

---

#### ANNOTATED_TYPE

public static final

Tree.Kind

ANNOTATED_TYPE

Used for instances of

AnnotatedTypeTree

representing annotated types.

ANNOTATION

```java
public static final
Tree.Kind
ANNOTATION
```

Used for instances of

AnnotationTree

representing declaration annotations.

---

#### ANNOTATION

public static final

Tree.Kind

ANNOTATION

Used for instances of

AnnotationTree

representing declaration annotations.

TYPE_ANNOTATION

```java
public static final
Tree.Kind
TYPE_ANNOTATION
```

Used for instances of

AnnotationTree

representing type annotations.

---

#### TYPE_ANNOTATION

public static final

Tree.Kind

TYPE_ANNOTATION

Used for instances of

AnnotationTree

representing type annotations.

ARRAY_ACCESS

```java
public static final
Tree.Kind
ARRAY_ACCESS
```

Used for instances of

ArrayAccessTree

.

---

#### ARRAY_ACCESS

public static final

Tree.Kind

ARRAY_ACCESS

Used for instances of

ArrayAccessTree

.

ARRAY_TYPE

```java
public static final
Tree.Kind
ARRAY_TYPE
```

Used for instances of

ArrayTypeTree

.

---

#### ARRAY_TYPE

public static final

Tree.Kind

ARRAY_TYPE

Used for instances of

ArrayTypeTree

.

ASSERT

```java
public static final
Tree.Kind
ASSERT
```

Used for instances of

AssertTree

.

---

#### ASSERT

public static final

Tree.Kind

ASSERT

Used for instances of

AssertTree

.

ASSIGNMENT

```java
public static final
Tree.Kind
ASSIGNMENT
```

Used for instances of

AssignmentTree

.

---

#### ASSIGNMENT

public static final

Tree.Kind

ASSIGNMENT

Used for instances of

AssignmentTree

.

BLOCK

```java
public static final
Tree.Kind
BLOCK
```

Used for instances of

BlockTree

.

---

#### BLOCK

public static final

Tree.Kind

BLOCK

Used for instances of

BlockTree

.

BREAK

```java
public static final
Tree.Kind
BREAK
```

Used for instances of

BreakTree

.

---

#### BREAK

public static final

Tree.Kind

BREAK

Used for instances of

BreakTree

.

CASE

```java
public static final
Tree.Kind
CASE
```

Used for instances of

CaseTree

.

---

#### CASE

public static final

Tree.Kind

CASE

Used for instances of

CaseTree

.

CATCH

```java
public static final
Tree.Kind
CATCH
```

Used for instances of

CatchTree

.

---

#### CATCH

public static final

Tree.Kind

CATCH

Used for instances of

CatchTree

.

CLASS

```java
public static final
Tree.Kind
CLASS
```

Used for instances of

ClassTree

representing classes.

---

#### CLASS

public static final

Tree.Kind

CLASS

Used for instances of

ClassTree

representing classes.

COMPILATION_UNIT

```java
public static final
Tree.Kind
COMPILATION_UNIT
```

Used for instances of

CompilationUnitTree

.

---

#### COMPILATION_UNIT

public static final

Tree.Kind

COMPILATION_UNIT

Used for instances of

CompilationUnitTree

.

CONDITIONAL_EXPRESSION

```java
public static final
Tree.Kind
CONDITIONAL_EXPRESSION
```

Used for instances of

ConditionalExpressionTree

.

---

#### CONDITIONAL_EXPRESSION

public static final

Tree.Kind

CONDITIONAL_EXPRESSION

Used for instances of

ConditionalExpressionTree

.

CONTINUE

```java
public static final
Tree.Kind
CONTINUE
```

Used for instances of

ContinueTree

.

---

#### CONTINUE

public static final

Tree.Kind

CONTINUE

Used for instances of

ContinueTree

.

DO_WHILE_LOOP

```java
public static final
Tree.Kind
DO_WHILE_LOOP
```

Used for instances of

DoWhileLoopTree

.

---

#### DO_WHILE_LOOP

public static final

Tree.Kind

DO_WHILE_LOOP

Used for instances of

DoWhileLoopTree

.

ENHANCED_FOR_LOOP

```java
public static final
Tree.Kind
ENHANCED_FOR_LOOP
```

Used for instances of

EnhancedForLoopTree

.

---

#### ENHANCED_FOR_LOOP

public static final

Tree.Kind

ENHANCED_FOR_LOOP

Used for instances of

EnhancedForLoopTree

.

EXPRESSION_STATEMENT

```java
public static final
Tree.Kind
EXPRESSION_STATEMENT
```

Used for instances of

ExpressionStatementTree

.

---

#### EXPRESSION_STATEMENT

public static final

Tree.Kind

EXPRESSION_STATEMENT

Used for instances of

ExpressionStatementTree

.

MEMBER_SELECT

```java
public static final
Tree.Kind
MEMBER_SELECT
```

Used for instances of

MemberSelectTree

.

---

#### MEMBER_SELECT

public static final

Tree.Kind

MEMBER_SELECT

Used for instances of

MemberSelectTree

.

MEMBER_REFERENCE

```java
public static final
Tree.Kind
MEMBER_REFERENCE
```

Used for instances of

MemberReferenceTree

.

---

#### MEMBER_REFERENCE

public static final

Tree.Kind

MEMBER_REFERENCE

Used for instances of

MemberReferenceTree

.

FOR_LOOP

```java
public static final
Tree.Kind
FOR_LOOP
```

Used for instances of

ForLoopTree

.

---

#### FOR_LOOP

public static final

Tree.Kind

FOR_LOOP

Used for instances of

ForLoopTree

.

IDENTIFIER

```java
public static final
Tree.Kind
IDENTIFIER
```

Used for instances of

IdentifierTree

.

---

#### IDENTIFIER

public static final

Tree.Kind

IDENTIFIER

Used for instances of

IdentifierTree

.

IF

```java
public static final
Tree.Kind
IF
```

Used for instances of

IfTree

.

---

#### IF

public static final

Tree.Kind

IF

Used for instances of

IfTree

.

IMPORT

```java
public static final
Tree.Kind
IMPORT
```

Used for instances of

ImportTree

.

---

#### IMPORT

public static final

Tree.Kind

IMPORT

Used for instances of

ImportTree

.

INSTANCE_OF

```java
public static final
Tree.Kind
INSTANCE_OF
```

Used for instances of

InstanceOfTree

.

---

#### INSTANCE_OF

public static final

Tree.Kind

INSTANCE_OF

Used for instances of

InstanceOfTree

.

LABELED_STATEMENT

```java
public static final
Tree.Kind
LABELED_STATEMENT
```

Used for instances of

LabeledStatementTree

.

---

#### LABELED_STATEMENT

public static final

Tree.Kind

LABELED_STATEMENT

Used for instances of

LabeledStatementTree

.

METHOD

```java
public static final
Tree.Kind
METHOD
```

Used for instances of

MethodTree

.

---

#### METHOD

public static final

Tree.Kind

METHOD

Used for instances of

MethodTree

.

METHOD_INVOCATION

```java
public static final
Tree.Kind
METHOD_INVOCATION
```

Used for instances of

MethodInvocationTree

.

---

#### METHOD_INVOCATION

public static final

Tree.Kind

METHOD_INVOCATION

Used for instances of

MethodInvocationTree

.

MODIFIERS

```java
public static final
Tree.Kind
MODIFIERS
```

Used for instances of

ModifiersTree

.

---

#### MODIFIERS

public static final

Tree.Kind

MODIFIERS

Used for instances of

ModifiersTree

.

NEW_ARRAY

```java
public static final
Tree.Kind
NEW_ARRAY
```

Used for instances of

NewArrayTree

.

---

#### NEW_ARRAY

public static final

Tree.Kind

NEW_ARRAY

Used for instances of

NewArrayTree

.

NEW_CLASS

```java
public static final
Tree.Kind
NEW_CLASS
```

Used for instances of

NewClassTree

.

---

#### NEW_CLASS

public static final

Tree.Kind

NEW_CLASS

Used for instances of

NewClassTree

.

LAMBDA_EXPRESSION

```java
public static final
Tree.Kind
LAMBDA_EXPRESSION
```

Used for instances of

LambdaExpressionTree

.

---

#### LAMBDA_EXPRESSION

public static final

Tree.Kind

LAMBDA_EXPRESSION

Used for instances of

LambdaExpressionTree

.

PACKAGE

```java
public static final
Tree.Kind
PACKAGE
```

Used for instances of

PackageTree

.

**Since:** 9

---

#### PACKAGE

public static final

Tree.Kind

PACKAGE

Used for instances of

PackageTree

.

PARENTHESIZED

```java
public static final
Tree.Kind
PARENTHESIZED
```

Used for instances of

ParenthesizedTree

.

---

#### PARENTHESIZED

public static final

Tree.Kind

PARENTHESIZED

Used for instances of

ParenthesizedTree

.

PRIMITIVE_TYPE

```java
public static final
Tree.Kind
PRIMITIVE_TYPE
```

Used for instances of

PrimitiveTypeTree

.

---

#### PRIMITIVE_TYPE

public static final

Tree.Kind

PRIMITIVE_TYPE

Used for instances of

PrimitiveTypeTree

.

RETURN

```java
public static final
Tree.Kind
RETURN
```

Used for instances of

ReturnTree

.

---

#### RETURN

public static final

Tree.Kind

RETURN

Used for instances of

ReturnTree

.

EMPTY_STATEMENT

```java
public static final
Tree.Kind
EMPTY_STATEMENT
```

Used for instances of

EmptyStatementTree

.

---

#### EMPTY_STATEMENT

public static final

Tree.Kind

EMPTY_STATEMENT

Used for instances of

EmptyStatementTree

.

SWITCH

```java
public static final
Tree.Kind
SWITCH
```

Used for instances of

SwitchTree

.

---

#### SWITCH

public static final

Tree.Kind

SWITCH

Used for instances of

SwitchTree

.

SYNCHRONIZED

```java
public static final
Tree.Kind
SYNCHRONIZED
```

Used for instances of

SynchronizedTree

.

---

#### SYNCHRONIZED

public static final

Tree.Kind

SYNCHRONIZED

Used for instances of

SynchronizedTree

.

THROW

```java
public static final
Tree.Kind
THROW
```

Used for instances of

ThrowTree

.

---

#### THROW

public static final

Tree.Kind

THROW

Used for instances of

ThrowTree

.

TRY

```java
public static final
Tree.Kind
TRY
```

Used for instances of

TryTree

.

---

#### TRY

public static final

Tree.Kind

TRY

Used for instances of

TryTree

.

PARAMETERIZED_TYPE

```java
public static final
Tree.Kind
PARAMETERIZED_TYPE
```

Used for instances of

ParameterizedTypeTree

.

---

#### PARAMETERIZED_TYPE

public static final

Tree.Kind

PARAMETERIZED_TYPE

Used for instances of

ParameterizedTypeTree

.

UNION_TYPE

```java
public static final
Tree.Kind
UNION_TYPE
```

Used for instances of

UnionTypeTree

.

---

#### UNION_TYPE

public static final

Tree.Kind

UNION_TYPE

Used for instances of

UnionTypeTree

.

INTERSECTION_TYPE

```java
public static final
Tree.Kind
INTERSECTION_TYPE
```

Used for instances of

IntersectionTypeTree

.

---

#### INTERSECTION_TYPE

public static final

Tree.Kind

INTERSECTION_TYPE

Used for instances of

IntersectionTypeTree

.

TYPE_CAST

```java
public static final
Tree.Kind
TYPE_CAST
```

Used for instances of

TypeCastTree

.

---

#### TYPE_CAST

public static final

Tree.Kind

TYPE_CAST

Used for instances of

TypeCastTree

.

TYPE_PARAMETER

```java
public static final
Tree.Kind
TYPE_PARAMETER
```

Used for instances of

TypeParameterTree

.

---

#### TYPE_PARAMETER

public static final

Tree.Kind

TYPE_PARAMETER

Used for instances of

TypeParameterTree

.

VARIABLE

```java
public static final
Tree.Kind
VARIABLE
```

Used for instances of

VariableTree

.

---

#### VARIABLE

public static final

Tree.Kind

VARIABLE

Used for instances of

VariableTree

.

WHILE_LOOP

```java
public static final
Tree.Kind
WHILE_LOOP
```

Used for instances of

WhileLoopTree

.

---

#### WHILE_LOOP

public static final

Tree.Kind

WHILE_LOOP

Used for instances of

WhileLoopTree

.

POSTFIX_INCREMENT

```java
public static final
Tree.Kind
POSTFIX_INCREMENT
```

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

---

#### POSTFIX_INCREMENT

public static final

Tree.Kind

POSTFIX_INCREMENT

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

POSTFIX_DECREMENT

```java
public static final
Tree.Kind
POSTFIX_DECREMENT
```

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

---

#### POSTFIX_DECREMENT

public static final

Tree.Kind

POSTFIX_DECREMENT

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

PREFIX_INCREMENT

```java
public static final
Tree.Kind
PREFIX_INCREMENT
```

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

---

#### PREFIX_INCREMENT

public static final

Tree.Kind

PREFIX_INCREMENT

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

PREFIX_DECREMENT

```java
public static final
Tree.Kind
PREFIX_DECREMENT
```

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

---

#### PREFIX_DECREMENT

public static final

Tree.Kind

PREFIX_DECREMENT

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

UNARY_PLUS

```java
public static final
Tree.Kind
UNARY_PLUS
```

Used for instances of

UnaryTree

representing unary plus
operator

+

.

---

#### UNARY_PLUS

public static final

Tree.Kind

UNARY_PLUS

Used for instances of

UnaryTree

representing unary plus
operator

+

.

UNARY_MINUS

```java
public static final
Tree.Kind
UNARY_MINUS
```

Used for instances of

UnaryTree

representing unary minus
operator

-

.

---

#### UNARY_MINUS

public static final

Tree.Kind

UNARY_MINUS

Used for instances of

UnaryTree

representing unary minus
operator

-

.

BITWISE_COMPLEMENT

```java
public static final
Tree.Kind
BITWISE_COMPLEMENT
```

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

---

#### BITWISE_COMPLEMENT

public static final

Tree.Kind

BITWISE_COMPLEMENT

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

LOGICAL_COMPLEMENT

```java
public static final
Tree.Kind
LOGICAL_COMPLEMENT
```

Used for instances of

UnaryTree

representing logical
complement operator

!

.

---

#### LOGICAL_COMPLEMENT

public static final

Tree.Kind

LOGICAL_COMPLEMENT

Used for instances of

UnaryTree

representing logical
complement operator

!

.

MULTIPLY

```java
public static final
Tree.Kind
MULTIPLY
```

Used for instances of

BinaryTree

representing
multiplication

*

.

---

#### MULTIPLY

public static final

Tree.Kind

MULTIPLY

Used for instances of

BinaryTree

representing
multiplication

*

.

DIVIDE

```java
public static final
Tree.Kind
DIVIDE
```

Used for instances of

BinaryTree

representing
division

/

.

---

#### DIVIDE

public static final

Tree.Kind

DIVIDE

Used for instances of

BinaryTree

representing
division

/

.

REMAINDER

```java
public static final
Tree.Kind
REMAINDER
```

Used for instances of

BinaryTree

representing
remainder

%

.

---

#### REMAINDER

public static final

Tree.Kind

REMAINDER

Used for instances of

BinaryTree

representing
remainder

%

.

PLUS

```java
public static final
Tree.Kind
PLUS
```

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

---

#### PLUS

public static final

Tree.Kind

PLUS

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

MINUS

```java
public static final
Tree.Kind
MINUS
```

Used for instances of

BinaryTree

representing
subtraction

-

.

---

#### MINUS

public static final

Tree.Kind

MINUS

Used for instances of

BinaryTree

representing
subtraction

-

.

LEFT_SHIFT

```java
public static final
Tree.Kind
LEFT_SHIFT
```

Used for instances of

BinaryTree

representing
left shift

<<

.

---

#### LEFT_SHIFT

public static final

Tree.Kind

LEFT_SHIFT

Used for instances of

BinaryTree

representing
left shift

<<

.

RIGHT_SHIFT

```java
public static final
Tree.Kind
RIGHT_SHIFT
```

Used for instances of

BinaryTree

representing
right shift

>>

.

---

#### RIGHT_SHIFT

public static final

Tree.Kind

RIGHT_SHIFT

Used for instances of

BinaryTree

representing
right shift

>>

.

UNSIGNED_RIGHT_SHIFT

```java
public static final
Tree.Kind
UNSIGNED_RIGHT_SHIFT
```

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

---

#### UNSIGNED_RIGHT_SHIFT

public static final

Tree.Kind

UNSIGNED_RIGHT_SHIFT

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

LESS_THAN

```java
public static final
Tree.Kind
LESS_THAN
```

Used for instances of

BinaryTree

representing
less-than

<

.

---

#### LESS_THAN

public static final

Tree.Kind

LESS_THAN

Used for instances of

BinaryTree

representing
less-than

<

.

GREATER_THAN

```java
public static final
Tree.Kind
GREATER_THAN
```

Used for instances of

BinaryTree

representing
greater-than

>

.

---

#### GREATER_THAN

public static final

Tree.Kind

GREATER_THAN

Used for instances of

BinaryTree

representing
greater-than

>

.

LESS_THAN_EQUAL

```java
public static final
Tree.Kind
LESS_THAN_EQUAL
```

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

---

#### LESS_THAN_EQUAL

public static final

Tree.Kind

LESS_THAN_EQUAL

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

GREATER_THAN_EQUAL

```java
public static final
Tree.Kind
GREATER_THAN_EQUAL
```

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

---

#### GREATER_THAN_EQUAL

public static final

Tree.Kind

GREATER_THAN_EQUAL

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

EQUAL_TO

```java
public static final
Tree.Kind
EQUAL_TO
```

Used for instances of

BinaryTree

representing
equal-to

==

.

---

#### EQUAL_TO

public static final

Tree.Kind

EQUAL_TO

Used for instances of

BinaryTree

representing
equal-to

==

.

NOT_EQUAL_TO

```java
public static final
Tree.Kind
NOT_EQUAL_TO
```

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

---

#### NOT_EQUAL_TO

public static final

Tree.Kind

NOT_EQUAL_TO

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

AND

```java
public static final
Tree.Kind
AND
```

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

---

#### AND

public static final

Tree.Kind

AND

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

XOR

```java
public static final
Tree.Kind
XOR
```

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

---

#### XOR

public static final

Tree.Kind

XOR

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

OR

```java
public static final
Tree.Kind
OR
```

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

---

#### OR

public static final

Tree.Kind

OR

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

CONDITIONAL_AND

```java
public static final
Tree.Kind
CONDITIONAL_AND
```

Used for instances of

BinaryTree

representing
conditional-and

&&

.

---

#### CONDITIONAL_AND

public static final

Tree.Kind

CONDITIONAL_AND

Used for instances of

BinaryTree

representing
conditional-and

&&

.

CONDITIONAL_OR

```java
public static final
Tree.Kind
CONDITIONAL_OR
```

Used for instances of

BinaryTree

representing
conditional-or

||

.

---

#### CONDITIONAL_OR

public static final

Tree.Kind

CONDITIONAL_OR

Used for instances of

BinaryTree

representing
conditional-or

||

.

MULTIPLY_ASSIGNMENT

```java
public static final
Tree.Kind
MULTIPLY_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

---

#### MULTIPLY_ASSIGNMENT

public static final

Tree.Kind

MULTIPLY_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

DIVIDE_ASSIGNMENT

```java
public static final
Tree.Kind
DIVIDE_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

---

#### DIVIDE_ASSIGNMENT

public static final

Tree.Kind

DIVIDE_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

REMAINDER_ASSIGNMENT

```java
public static final
Tree.Kind
REMAINDER_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

---

#### REMAINDER_ASSIGNMENT

public static final

Tree.Kind

REMAINDER_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

PLUS_ASSIGNMENT

```java
public static final
Tree.Kind
PLUS_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

---

#### PLUS_ASSIGNMENT

public static final

Tree.Kind

PLUS_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

MINUS_ASSIGNMENT

```java
public static final
Tree.Kind
MINUS_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

---

#### MINUS_ASSIGNMENT

public static final

Tree.Kind

MINUS_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

LEFT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
LEFT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

---

#### LEFT_SHIFT_ASSIGNMENT

public static final

Tree.Kind

LEFT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

RIGHT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
RIGHT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

---

#### RIGHT_SHIFT_ASSIGNMENT

public static final

Tree.Kind

RIGHT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

```java
public static final
Tree.Kind
UNSIGNED_RIGHT_SHIFT_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

---

#### UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

public static final

Tree.Kind

UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

AND_ASSIGNMENT

```java
public static final
Tree.Kind
AND_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

---

#### AND_ASSIGNMENT

public static final

Tree.Kind

AND_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

XOR_ASSIGNMENT

```java
public static final
Tree.Kind
XOR_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

---

#### XOR_ASSIGNMENT

public static final

Tree.Kind

XOR_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

OR_ASSIGNMENT

```java
public static final
Tree.Kind
OR_ASSIGNMENT
```

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

---

#### OR_ASSIGNMENT

public static final

Tree.Kind

OR_ASSIGNMENT

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

INT_LITERAL

```java
public static final
Tree.Kind
INT_LITERAL
```

Used for instances of

LiteralTree

representing
an integral literal expression of type

int

.

---

#### INT_LITERAL

public static final

Tree.Kind

INT_LITERAL

Used for instances of

LiteralTree

representing
an integral literal expression of type

int

.

LONG_LITERAL

```java
public static final
Tree.Kind
LONG_LITERAL
```

Used for instances of

LiteralTree

representing
an integral literal expression of type

long

.

---

#### LONG_LITERAL

public static final

Tree.Kind

LONG_LITERAL

Used for instances of

LiteralTree

representing
an integral literal expression of type

long

.

FLOAT_LITERAL

```java
public static final
Tree.Kind
FLOAT_LITERAL
```

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

float

.

---

#### FLOAT_LITERAL

public static final

Tree.Kind

FLOAT_LITERAL

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

float

.

DOUBLE_LITERAL

```java
public static final
Tree.Kind
DOUBLE_LITERAL
```

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

double

.

---

#### DOUBLE_LITERAL

public static final

Tree.Kind

DOUBLE_LITERAL

Used for instances of

LiteralTree

representing
a floating-point literal expression of type

double

.

BOOLEAN_LITERAL

```java
public static final
Tree.Kind
BOOLEAN_LITERAL
```

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

---

#### BOOLEAN_LITERAL

public static final

Tree.Kind

BOOLEAN_LITERAL

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

CHAR_LITERAL

```java
public static final
Tree.Kind
CHAR_LITERAL
```

Used for instances of

LiteralTree

representing
a character literal expression of type

char

.

---

#### CHAR_LITERAL

public static final

Tree.Kind

CHAR_LITERAL

Used for instances of

LiteralTree

representing
a character literal expression of type

char

.

STRING_LITERAL

```java
public static final
Tree.Kind
STRING_LITERAL
```

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

---

#### STRING_LITERAL

public static final

Tree.Kind

STRING_LITERAL

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

NULL_LITERAL

```java
public static final
Tree.Kind
NULL_LITERAL
```

Used for instances of

LiteralTree

representing
the use of

null

.

---

#### NULL_LITERAL

public static final

Tree.Kind

NULL_LITERAL

Used for instances of

LiteralTree

representing
the use of

null

.

UNBOUNDED_WILDCARD

```java
public static final
Tree.Kind
UNBOUNDED_WILDCARD
```

Used for instances of

WildcardTree

representing
an unbounded wildcard type argument.

---

#### UNBOUNDED_WILDCARD

public static final

Tree.Kind

UNBOUNDED_WILDCARD

Used for instances of

WildcardTree

representing
an unbounded wildcard type argument.

EXTENDS_WILDCARD

```java
public static final
Tree.Kind
EXTENDS_WILDCARD
```

Used for instances of

WildcardTree

representing
an extends bounded wildcard type argument.

---

#### EXTENDS_WILDCARD

public static final

Tree.Kind

EXTENDS_WILDCARD

Used for instances of

WildcardTree

representing
an extends bounded wildcard type argument.

SUPER_WILDCARD

```java
public static final
Tree.Kind
SUPER_WILDCARD
```

Used for instances of

WildcardTree

representing
a super bounded wildcard type argument.

---

#### SUPER_WILDCARD

public static final

Tree.Kind

SUPER_WILDCARD

Used for instances of

WildcardTree

representing
a super bounded wildcard type argument.

ERRONEOUS

```java
public static final
Tree.Kind
ERRONEOUS
```

Used for instances of

ErroneousTree

.

---

#### ERRONEOUS

public static final

Tree.Kind

ERRONEOUS

Used for instances of

ErroneousTree

.

INTERFACE

```java
public static final
Tree.Kind
INTERFACE
```

Used for instances of

ClassTree

representing interfaces.

---

#### INTERFACE

public static final

Tree.Kind

INTERFACE

Used for instances of

ClassTree

representing interfaces.

ENUM

```java
public static final
Tree.Kind
ENUM
```

Used for instances of

ClassTree

representing enums.

---

#### ENUM

public static final

Tree.Kind

ENUM

Used for instances of

ClassTree

representing enums.

ANNOTATION_TYPE

```java
public static final
Tree.Kind
ANNOTATION_TYPE
```

Used for instances of

ClassTree

representing annotation types.

---

#### ANNOTATION_TYPE

public static final

Tree.Kind

ANNOTATION_TYPE

Used for instances of

ClassTree

representing annotation types.

MODULE

```java
public static final
Tree.Kind
MODULE
```

Used for instances of

ModuleTree

representing module declarations.

---

#### MODULE

public static final

Tree.Kind

MODULE

Used for instances of

ModuleTree

representing module declarations.

EXPORTS

```java
public static final
Tree.Kind
EXPORTS
```

Used for instances of

ExportsTree

representing
exports directives in a module declaration.

---

#### EXPORTS

public static final

Tree.Kind

EXPORTS

Used for instances of

ExportsTree

representing
exports directives in a module declaration.

OPENS

```java
public static final
Tree.Kind
OPENS
```

Used for instances of

ExportsTree

representing
opens directives in a module declaration.

---

#### OPENS

public static final

Tree.Kind

OPENS

Used for instances of

ExportsTree

representing
opens directives in a module declaration.

PROVIDES

```java
public static final
Tree.Kind
PROVIDES
```

Used for instances of

ProvidesTree

representing
provides directives in a module declaration.

---

#### PROVIDES

public static final

Tree.Kind

PROVIDES

Used for instances of

ProvidesTree

representing
provides directives in a module declaration.

REQUIRES

```java
public static final
Tree.Kind
REQUIRES
```

Used for instances of

RequiresTree

representing
requires directives in a module declaration.

---

#### REQUIRES

public static final

Tree.Kind

REQUIRES

Used for instances of

RequiresTree

representing
requires directives in a module declaration.

USES

```java
public static final
Tree.Kind
USES
```

Used for instances of

UsesTree

representing
uses directives in a module declaration.

---

#### USES

public static final

Tree.Kind

USES

Used for instances of

UsesTree

representing
uses directives in a module declaration.

OTHER

```java
public static final
Tree.Kind
OTHER
```

An implementation-reserved node. This is the not the node
you are looking for.

---

#### OTHER

public static final

Tree.Kind

OTHER

An implementation-reserved node. This is the not the node
you are looking for.

Method Detail

- values

```java
public static
Tree.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Tree.Kind c : Tree.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Tree.Kind
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

- asInterface

```java
public
Class
<? extends
Tree
> asInterface()
```

Returns the associated interface type that uses this kind.

**Returns:** the associated interface

---

#### Method Detail

values

```java
public static
Tree.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Tree.Kind c : Tree.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Tree.Kind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Tree.Kind c : Tree.Kind.values())
System.out.println(c);
```

for (Tree.Kind c : Tree.Kind.values())
System.out.println(c);

valueOf

```java
public static
Tree.Kind
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

Tree.Kind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

asInterface

```java
public
Class
<? extends
Tree
> asInterface()
```

Returns the associated interface type that uses this kind.

**Returns:** the associated interface

---

#### asInterface

public

Class

<? extends

Tree

> asInterface()

Returns the associated interface type that uses this kind.

---

