# Enum Tree.Kind

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\Tree.Kind.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
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

#### public boolean isLiteral()

Returns if this is a literal tree kind or not.

**Returns:**
- true if this is a literal tree kind, false otherwise

---

#### public boolean isExpression()

Returns if this is an expression tree kind or not.

**Returns:**
- true if this is an expression tree kind, false otherwise

---

#### public boolean isStatement()

Returns if this is a statement tree kind or not.

**Returns:**
- true if this is a statement tree kind, false otherwise

---

### Additional Sections

#### Enum Tree.Kind

java.lang.Object

- java.lang.Enum

<

Tree.Kind

>
- - jdk.nashorn.api.tree.Tree.Kind

java.lang.Enum

<

Tree.Kind

>

- jdk.nashorn.api.tree.Tree.Kind

jdk.nashorn.api.tree.Tree.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

Tree.Kind

>

**Enclosing interface:** Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public static enum
Tree.Kind

extends
Enum
<
Tree.Kind
>
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Enumerates all kinds of trees.

@Deprecated

(

since

="11",

forRemoval

=true)
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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

AND_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

ARRAY_ACCESS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayAccessTree

.

ARRAY_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayLiteralTree

.

ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

AssignmentTree

.

BITWISE_COMPLEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

BLOCK

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BlockTree

.

BOOLEAN_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

BREAK

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BreakTree

.

CASE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CaseTree

.

CATCH

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CatchTree

.

CLASS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassDeclarationTree

.

CLASS_EXPRESSION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassExpressionTree

.

COMMA

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
comma

,

.

COMPILATION_UNIT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompilationUnitTree

.

CONDITIONAL_AND

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
conditional-and

&&

.

CONDITIONAL_EXPRESSION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ConditionalExpressionTree

.

CONDITIONAL_OR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
conditional-or

||

.

CONTINUE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ContinueTree

.

DEBUGGER

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DebuggerTree

.

DELETE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
delete operator

delete

.

DIVIDE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
division

/

.

DIVIDE_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

DO_WHILE_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DoWhileLoopTree

.

EMPTY_STATEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

EmptyStatementTree

.

EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
equal-to

==

.

ERROR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ErroneousTree

.

EXPORT_ENTRY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExportEntryTree

.

EXPRESSION_STATEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExpressionStatementTree

.

FOR_IN_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForInLoopTree

.

FOR_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForLoopTree

.

FUNCTION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionDeclarationTree

.

FUNCTION_EXPRESSION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionExpressionTree

.

FUNCTION_INVOCATION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionCallTree

.

GREATER_THAN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
greater-than

>

.

GREATER_THAN_EQUAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

IDENTIFIER

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IdentifierTree

.

IF

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IfTree

.

IMPORT_ENTRY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ImportEntryTree

.

IN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
in operator

in

.

INSTANCE_OF

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

InstanceOfTree

.

LABELED_STATEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LabeledStatementTree

.

LEFT_SHIFT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
left shift

<<

.

LEFT_SHIFT_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

LESS_THAN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
less-than

<

.

LESS_THAN_EQUAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

LOGICAL_COMPLEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
complement operator

!

.

MEMBER_SELECT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

MemberSelectTree

.

MINUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
subtraction

-

.

MINUS_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

MODULE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ModuleTree

.

MULTIPLY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
multiplication

*

.

MULTIPLY_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

NEW

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

NewTree

.

NOT_EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

NULL_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
the use of

null

.

NUMBER_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a number literal expression of type

double

.

OBJECT_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ObjectLiteralTree

.

OR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

OR_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

OTHER

Deprecated, for removal: This API element is subject to removal in a future version.

An implementation-reserved node.

PARENTHESIZED

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ParenthesizedTree

.

PLUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

PLUS_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

POSTFIX_DECREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

POSTFIX_INCREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

PREFIX_DECREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

PREFIX_INCREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

PROPERTY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

PropertyTree

.

REGEXP_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

RegExpLiteralTree

.

REMAINDER

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
remainder

%

.

REMAINDER_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

RETURN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ReturnTree

.

RIGHT_SHIFT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
right shift

>>

.

RIGHT_SHIFT_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

SPREAD

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SpreadTree

representing
spread "operator" for arrays and function call arguments.

STRICT_EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
equal-to

===

.

STRICT_NOT_EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!==

.

STRING_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

SWITCH

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SwitchTree

.

TEMPLATE_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TemplateLiteralTree

.

THROW

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ThrowTree

.

TRY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TryTree

.

TYPEOF

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
typeof operator

typeof

.

UNARY_MINUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing unary minus
operator

-

.

UNARY_PLUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing unary plus
operator

+

.

UNSIGNED_RIGHT_SHIFT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

VARIABLE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

VariableTree

.

VOID

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
void operator

void

.

WHILE_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WhileLoopTree

.

WITH

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WithTree

.

XOR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

XOR_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

YIELD

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

YieldTree

representing (generator)
yield expression

yield expr

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Class

<? extends

Tree

>

asInterface

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the associated interface type that uses this kind.

boolean

isExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is an expression tree kind or not.

boolean

isLiteral

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a literal tree kind or not.

boolean

isStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a statement tree kind or not.

static

Tree.Kind

valueOf

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the enum constant of this type with the specified name.

static

Tree.Kind

[]

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
bitwise and logical "and"

&

.

AND_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "and" assignment

&=

.

ARRAY_ACCESS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayAccessTree

.

ARRAY_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayLiteralTree

.

ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

AssignmentTree

.

BITWISE_COMPLEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing bitwise
complement operator

~

.

BLOCK

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BlockTree

.

BOOLEAN_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

BREAK

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BreakTree

.

CASE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CaseTree

.

CATCH

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CatchTree

.

CLASS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassDeclarationTree

.

CLASS_EXPRESSION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassExpressionTree

.

COMMA

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
comma

,

.

COMPILATION_UNIT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompilationUnitTree

.

CONDITIONAL_AND

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
conditional-and

&&

.

CONDITIONAL_EXPRESSION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ConditionalExpressionTree

.

CONDITIONAL_OR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
conditional-or

||

.

CONTINUE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ContinueTree

.

DEBUGGER

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DebuggerTree

.

DELETE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
delete operator

delete

.

DIVIDE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
division

/

.

DIVIDE_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
division assignment

/=

.

DO_WHILE_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DoWhileLoopTree

.

EMPTY_STATEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

EmptyStatementTree

.

EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
equal-to

==

.

ERROR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ErroneousTree

.

EXPORT_ENTRY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExportEntryTree

.

EXPRESSION_STATEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExpressionStatementTree

.

FOR_IN_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForInLoopTree

.

FOR_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForLoopTree

.

FUNCTION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionDeclarationTree

.

FUNCTION_EXPRESSION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionExpressionTree

.

FUNCTION_INVOCATION

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionCallTree

.

GREATER_THAN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
greater-than

>

.

GREATER_THAN_EQUAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

IDENTIFIER

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IdentifierTree

.

IF

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IfTree

.

IMPORT_ENTRY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ImportEntryTree

.

IN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
in operator

in

.

INSTANCE_OF

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

InstanceOfTree

.

LABELED_STATEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LabeledStatementTree

.

LEFT_SHIFT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
left shift

<<

.

LEFT_SHIFT_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
left shift assignment

<<=

.

LESS_THAN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
less-than

<

.

LESS_THAN_EQUAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
less-than-equal

<=

.

LOGICAL_COMPLEMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
complement operator

!

.

MEMBER_SELECT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

MemberSelectTree

.

MINUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
subtraction

-

.

MINUS_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
subtraction assignment

-=

.

MODULE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ModuleTree

.

MULTIPLY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
multiplication

*

.

MULTIPLY_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
multiplication assignment

*=

.

NEW

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

NewTree

.

NOT_EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

NULL_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
the use of

null

.

NUMBER_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a number literal expression of type

double

.

OBJECT_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ObjectLiteralTree

.

OR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
bitwise and logical "or"

|

.

OR_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

OTHER

Deprecated, for removal: This API element is subject to removal in a future version.

An implementation-reserved node.

PARENTHESIZED

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ParenthesizedTree

.

PLUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
addition or string concatenation

+

.

PLUS_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
addition or string concatenation assignment

+=

.

POSTFIX_DECREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing postfix
decrement operator

--

.

POSTFIX_INCREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing postfix
increment operator

++

.

PREFIX_DECREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing prefix
decrement operator

--

.

PREFIX_INCREMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing prefix
increment operator

++

.

PROPERTY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

PropertyTree

.

REGEXP_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

RegExpLiteralTree

.

REMAINDER

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
remainder

%

.

REMAINDER_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
remainder assignment

%=

.

RETURN

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ReturnTree

.

RIGHT_SHIFT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
right shift

>>

.

RIGHT_SHIFT_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
right shift assignment

>>=

.

SPREAD

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SpreadTree

representing
spread "operator" for arrays and function call arguments.

STRICT_EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
equal-to

===

.

STRICT_NOT_EQUAL_TO

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!==

.

STRING_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

SWITCH

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SwitchTree

.

TEMPLATE_LITERAL

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TemplateLiteralTree

.

THROW

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ThrowTree

.

TRY

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TryTree

.

TYPEOF

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
typeof operator

typeof

.

UNARY_MINUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing unary minus
operator

-

.

UNARY_PLUS

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing unary plus
operator

+

.

UNSIGNED_RIGHT_SHIFT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
unsigned right shift

>>>

.

UNSIGNED_RIGHT_SHIFT_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
unsigned right shift assignment

>>>=

.

VARIABLE

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

VariableTree

.

VOID

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
void operator

void

.

WHILE_LOOP

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WhileLoopTree

.

WITH

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WithTree

.

XOR

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
bitwise and logical "xor"

^

.

XOR_ASSIGNMENT

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "xor" assignment

^=

.

YIELD

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

YieldTree

representing (generator)
yield expression

yield expr

.

---

#### Enum Constant Summary

Deprecated, for removal: This API element is subject to removal in a future version.

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

ArrayAccessTree

.

Used for instances of

ArrayLiteralTree

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

ClassDeclarationTree

.

Used for instances of

ClassExpressionTree

.

Used for instances of

BinaryTree

representing
comma

,

.

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

DebuggerTree

.

Used for instances of

UnaryTree

representing logical
delete operator

delete

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

EmptyStatementTree

.

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

ExportEntryTree

.

Used for instances of

ExpressionStatementTree

.

Used for instances of

ForInLoopTree

.

Used for instances of

ForLoopTree

.

Used for instances of

FunctionDeclarationTree

.

Used for instances of

FunctionExpressionTree

.

Used for instances of

FunctionCallTree

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

ImportEntryTree

.

Used for instances of

BinaryTree

representing
in operator

in

.

Used for instances of

InstanceOfTree

.

Used for instances of

LabeledStatementTree

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

MemberSelectTree

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

ModuleTree

.

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

NewTree

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

LiteralTree

representing
a number literal expression of type

double

.

Used for instances of

ObjectLiteralTree

.

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

PropertyTree

.

Used for instances of

RegExpLiteralTree

.

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

SpreadTree

representing
spread "operator" for arrays and function call arguments.

Used for instances of

BinaryTree

representing
equal-to

===

.

Used for instances of

BinaryTree

representing
not-equal-to

!==

.

Used for instances of

LiteralTree

representing
a string literal expression of type

String

.

Used for instances of

SwitchTree

.

Used for instances of

TemplateLiteralTree

.

Used for instances of

ThrowTree

.

Used for instances of

TryTree

.

Used for instances of

UnaryTree

representing logical
typeof operator

typeof

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

VariableTree

.

Used for instances of

UnaryTree

representing logical
void operator

void

.

Used for instances of

WhileLoopTree

.

Used for instances of

WithTree

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

Used for instances of

YieldTree

representing (generator)
yield expression

yield expr

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Class

<? extends

Tree

>

asInterface

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the associated interface type that uses this kind.

boolean

isExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is an expression tree kind or not.

boolean

isLiteral

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a literal tree kind or not.

boolean

isStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a statement tree kind or not.

static

Tree.Kind

valueOf

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the enum constant of this type with the specified name.

static

Tree.Kind

[]

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the associated interface type that uses this kind.

Returns if this is an expression tree kind or not.

Returns if this is a literal tree kind or not.

Returns if this is a statement tree kind or not.

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

- ARRAY_ACCESS

```java
public static final
Tree.Kind
ARRAY_ACCESS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayAccessTree

.

- ARRAY_LITERAL

```java
public static final
Tree.Kind
ARRAY_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayLiteralTree

.

- ASSIGNMENT

```java
public static final
Tree.Kind
ASSIGNMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

AssignmentTree

.

- BLOCK

```java
public static final
Tree.Kind
BLOCK
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BlockTree

.

- BREAK

```java
public static final
Tree.Kind
BREAK
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BreakTree

.

- CLASS

```java
public static final
Tree.Kind
CLASS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassDeclarationTree

.

- CLASS_EXPRESSION

```java
public static final
Tree.Kind
CLASS_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassExpressionTree

.

- CASE

```java
public static final
Tree.Kind
CASE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CaseTree

.

- CATCH

```java
public static final
Tree.Kind
CATCH
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CatchTree

.

- COMPILATION_UNIT

```java
public static final
Tree.Kind
COMPILATION_UNIT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompilationUnitTree

.

- CONDITIONAL_EXPRESSION

```java
public static final
Tree.Kind
CONDITIONAL_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ConditionalExpressionTree

.

- CONTINUE

```java
public static final
Tree.Kind
CONTINUE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ContinueTree

.

- DO_WHILE_LOOP

```java
public static final
Tree.Kind
DO_WHILE_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DoWhileLoopTree

.

- DEBUGGER

```java
public static final
Tree.Kind
DEBUGGER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DebuggerTree

.

- FOR_IN_LOOP

```java
public static final
Tree.Kind
FOR_IN_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForInLoopTree

.

- FUNCTION_EXPRESSION

```java
public static final
Tree.Kind
FUNCTION_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionExpressionTree

.

- ERROR

```java
public static final
Tree.Kind
ERROR
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ErroneousTree

.

- EXPRESSION_STATEMENT

```java
public static final
Tree.Kind
EXPRESSION_STATEMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExpressionStatementTree

.

- MEMBER_SELECT

```java
public static final
Tree.Kind
MEMBER_SELECT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

MemberSelectTree

.

- FOR_LOOP

```java
public static final
Tree.Kind
FOR_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForLoopTree

.

- IDENTIFIER

```java
public static final
Tree.Kind
IDENTIFIER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IdentifierTree

.

- IF

```java
public static final
Tree.Kind
IF
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IfTree

.

- INSTANCE_OF

```java
public static final
Tree.Kind
INSTANCE_OF
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

InstanceOfTree

.

- LABELED_STATEMENT

```java
public static final
Tree.Kind
LABELED_STATEMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LabeledStatementTree

.

- MODULE

```java
public static final
Tree.Kind
MODULE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ModuleTree

.

- EXPORT_ENTRY

```java
public static final
Tree.Kind
EXPORT_ENTRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExportEntryTree

.

- IMPORT_ENTRY

```java
public static final
Tree.Kind
IMPORT_ENTRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ImportEntryTree

.

- FUNCTION

```java
public static final
Tree.Kind
FUNCTION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionDeclarationTree

.

- FUNCTION_INVOCATION

```java
public static final
Tree.Kind
FUNCTION_INVOCATION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionCallTree

.

- NEW

```java
public static final
Tree.Kind
NEW
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

NewTree

.

- OBJECT_LITERAL

```java
public static final
Tree.Kind
OBJECT_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ObjectLiteralTree

.

- PARENTHESIZED

```java
public static final
Tree.Kind
PARENTHESIZED
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ParenthesizedTree

.

- PROPERTY

```java
public static final
Tree.Kind
PROPERTY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

PropertyTree

.

- REGEXP_LITERAL

```java
public static final
Tree.Kind
REGEXP_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

RegExpLiteralTree

.

- TEMPLATE_LITERAL

```java
public static final
Tree.Kind
TEMPLATE_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TemplateLiteralTree

.

- RETURN

```java
public static final
Tree.Kind
RETURN
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ReturnTree

.

- EMPTY_STATEMENT

```java
public static final
Tree.Kind
EMPTY_STATEMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

EmptyStatementTree

.

- SWITCH

```java
public static final
Tree.Kind
SWITCH
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SwitchTree

.

- THROW

```java
public static final
Tree.Kind
THROW
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ThrowTree

.

- TRY

```java
public static final
Tree.Kind
TRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TryTree

.

- VARIABLE

```java
public static final
Tree.Kind
VARIABLE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

VariableTree

.

- WHILE_LOOP

```java
public static final
Tree.Kind
WHILE_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WhileLoopTree

.

- WITH

```java
public static final
Tree.Kind
WITH
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WithTree

.

- POSTFIX_INCREMENT

```java
public static final
Tree.Kind
POSTFIX_INCREMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
complement operator

!

.

- DELETE

```java
public static final
Tree.Kind
DELETE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
delete operator

delete

.

- TYPEOF

```java
public static final
Tree.Kind
TYPEOF
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
typeof operator

typeof

.

- VOID

```java
public static final
Tree.Kind
VOID
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
void operator

void

.

- COMMA

```java
public static final
Tree.Kind
COMMA
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
comma

,

.

- MULTIPLY

```java
public static final
Tree.Kind
MULTIPLY
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

- IN

```java
public static final
Tree.Kind
IN
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
in operator

in

.

- EQUAL_TO

```java
public static final
Tree.Kind
EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

- STRICT_EQUAL_TO

```java
public static final
Tree.Kind
STRICT_EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
equal-to

===

.

- STRICT_NOT_EQUAL_TO

```java
public static final
Tree.Kind
STRICT_NOT_EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!==

.

- AND

```java
public static final
Tree.Kind
AND
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

- SPREAD

```java
public static final
Tree.Kind
SPREAD
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SpreadTree

representing
spread "operator" for arrays and function call arguments.

- YIELD

```java
public static final
Tree.Kind
YIELD
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

YieldTree

representing (generator)
yield expression

yield expr

.

- NUMBER_LITERAL

```java
public static final
Tree.Kind
NUMBER_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a number literal expression of type

double

.

- BOOLEAN_LITERAL

```java
public static final
Tree.Kind
BOOLEAN_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

- STRING_LITERAL

```java
public static final
Tree.Kind
STRING_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
the use of

null

.

- OTHER

```java
public static final
Tree.Kind
OTHER
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the associated interface type that uses this kind.

**Returns:** the associated interface

- isLiteral

```java
public boolean isLiteral()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a literal tree kind or not.

**Returns:** true if this is a literal tree kind, false otherwise

- isExpression

```java
public boolean isExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is an expression tree kind or not.

**Returns:** true if this is an expression tree kind, false otherwise

- isStatement

```java
public boolean isStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a statement tree kind or not.

**Returns:** true if this is a statement tree kind, false otherwise

Enum Constant Detail

- ARRAY_ACCESS

```java
public static final
Tree.Kind
ARRAY_ACCESS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayAccessTree

.

- ARRAY_LITERAL

```java
public static final
Tree.Kind
ARRAY_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayLiteralTree

.

- ASSIGNMENT

```java
public static final
Tree.Kind
ASSIGNMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

AssignmentTree

.

- BLOCK

```java
public static final
Tree.Kind
BLOCK
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BlockTree

.

- BREAK

```java
public static final
Tree.Kind
BREAK
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BreakTree

.

- CLASS

```java
public static final
Tree.Kind
CLASS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassDeclarationTree

.

- CLASS_EXPRESSION

```java
public static final
Tree.Kind
CLASS_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassExpressionTree

.

- CASE

```java
public static final
Tree.Kind
CASE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CaseTree

.

- CATCH

```java
public static final
Tree.Kind
CATCH
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CatchTree

.

- COMPILATION_UNIT

```java
public static final
Tree.Kind
COMPILATION_UNIT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompilationUnitTree

.

- CONDITIONAL_EXPRESSION

```java
public static final
Tree.Kind
CONDITIONAL_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ConditionalExpressionTree

.

- CONTINUE

```java
public static final
Tree.Kind
CONTINUE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ContinueTree

.

- DO_WHILE_LOOP

```java
public static final
Tree.Kind
DO_WHILE_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DoWhileLoopTree

.

- DEBUGGER

```java
public static final
Tree.Kind
DEBUGGER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DebuggerTree

.

- FOR_IN_LOOP

```java
public static final
Tree.Kind
FOR_IN_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForInLoopTree

.

- FUNCTION_EXPRESSION

```java
public static final
Tree.Kind
FUNCTION_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionExpressionTree

.

- ERROR

```java
public static final
Tree.Kind
ERROR
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ErroneousTree

.

- EXPRESSION_STATEMENT

```java
public static final
Tree.Kind
EXPRESSION_STATEMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExpressionStatementTree

.

- MEMBER_SELECT

```java
public static final
Tree.Kind
MEMBER_SELECT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

MemberSelectTree

.

- FOR_LOOP

```java
public static final
Tree.Kind
FOR_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForLoopTree

.

- IDENTIFIER

```java
public static final
Tree.Kind
IDENTIFIER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IdentifierTree

.

- IF

```java
public static final
Tree.Kind
IF
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

IfTree

.

- INSTANCE_OF

```java
public static final
Tree.Kind
INSTANCE_OF
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

InstanceOfTree

.

- LABELED_STATEMENT

```java
public static final
Tree.Kind
LABELED_STATEMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LabeledStatementTree

.

- MODULE

```java
public static final
Tree.Kind
MODULE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ModuleTree

.

- EXPORT_ENTRY

```java
public static final
Tree.Kind
EXPORT_ENTRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExportEntryTree

.

- IMPORT_ENTRY

```java
public static final
Tree.Kind
IMPORT_ENTRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ImportEntryTree

.

- FUNCTION

```java
public static final
Tree.Kind
FUNCTION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionDeclarationTree

.

- FUNCTION_INVOCATION

```java
public static final
Tree.Kind
FUNCTION_INVOCATION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionCallTree

.

- NEW

```java
public static final
Tree.Kind
NEW
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

NewTree

.

- OBJECT_LITERAL

```java
public static final
Tree.Kind
OBJECT_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ObjectLiteralTree

.

- PARENTHESIZED

```java
public static final
Tree.Kind
PARENTHESIZED
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ParenthesizedTree

.

- PROPERTY

```java
public static final
Tree.Kind
PROPERTY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

PropertyTree

.

- REGEXP_LITERAL

```java
public static final
Tree.Kind
REGEXP_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

RegExpLiteralTree

.

- TEMPLATE_LITERAL

```java
public static final
Tree.Kind
TEMPLATE_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TemplateLiteralTree

.

- RETURN

```java
public static final
Tree.Kind
RETURN
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ReturnTree

.

- EMPTY_STATEMENT

```java
public static final
Tree.Kind
EMPTY_STATEMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

EmptyStatementTree

.

- SWITCH

```java
public static final
Tree.Kind
SWITCH
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SwitchTree

.

- THROW

```java
public static final
Tree.Kind
THROW
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ThrowTree

.

- TRY

```java
public static final
Tree.Kind
TRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TryTree

.

- VARIABLE

```java
public static final
Tree.Kind
VARIABLE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

VariableTree

.

- WHILE_LOOP

```java
public static final
Tree.Kind
WHILE_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WhileLoopTree

.

- WITH

```java
public static final
Tree.Kind
WITH
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WithTree

.

- POSTFIX_INCREMENT

```java
public static final
Tree.Kind
POSTFIX_INCREMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
complement operator

!

.

- DELETE

```java
public static final
Tree.Kind
DELETE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
delete operator

delete

.

- TYPEOF

```java
public static final
Tree.Kind
TYPEOF
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
typeof operator

typeof

.

- VOID

```java
public static final
Tree.Kind
VOID
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
void operator

void

.

- COMMA

```java
public static final
Tree.Kind
COMMA
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
comma

,

.

- MULTIPLY

```java
public static final
Tree.Kind
MULTIPLY
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
greater-than-equal

>=

.

- IN

```java
public static final
Tree.Kind
IN
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
in operator

in

.

- EQUAL_TO

```java
public static final
Tree.Kind
EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!=

.

- STRICT_EQUAL_TO

```java
public static final
Tree.Kind
STRICT_EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
equal-to

===

.

- STRICT_NOT_EQUAL_TO

```java
public static final
Tree.Kind
STRICT_NOT_EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!==

.

- AND

```java
public static final
Tree.Kind
AND
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

CompoundAssignmentTree

representing
bitwise and logical "or" assignment

|=

.

- SPREAD

```java
public static final
Tree.Kind
SPREAD
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SpreadTree

representing
spread "operator" for arrays and function call arguments.

- YIELD

```java
public static final
Tree.Kind
YIELD
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

YieldTree

representing (generator)
yield expression

yield expr

.

- NUMBER_LITERAL

```java
public static final
Tree.Kind
NUMBER_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a number literal expression of type

double

.

- BOOLEAN_LITERAL

```java
public static final
Tree.Kind
BOOLEAN_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a boolean literal expression of type

boolean

.

- STRING_LITERAL

```java
public static final
Tree.Kind
STRING_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
the use of

null

.

- OTHER

```java
public static final
Tree.Kind
OTHER
```

Deprecated, for removal: This API element is subject to removal in a future version.

An implementation-reserved node. This is the not the node
you are looking for.

---

#### Enum Constant Detail

ARRAY_ACCESS

```java
public static final
Tree.Kind
ARRAY_ACCESS
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

ARRAY_LITERAL

```java
public static final
Tree.Kind
ARRAY_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ArrayLiteralTree

.

---

#### ARRAY_LITERAL

public static final

Tree.Kind

ARRAY_LITERAL

Used for instances of

ArrayLiteralTree

.

ASSIGNMENT

```java
public static final
Tree.Kind
ASSIGNMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

CLASS

```java
public static final
Tree.Kind
CLASS
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassDeclarationTree

.

---

#### CLASS

public static final

Tree.Kind

CLASS

Used for instances of

ClassDeclarationTree

.

CLASS_EXPRESSION

```java
public static final
Tree.Kind
CLASS_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ClassExpressionTree

.

---

#### CLASS_EXPRESSION

public static final

Tree.Kind

CLASS_EXPRESSION

Used for instances of

ClassExpressionTree

.

CASE

```java
public static final
Tree.Kind
CASE
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

COMPILATION_UNIT

```java
public static final
Tree.Kind
COMPILATION_UNIT
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

DEBUGGER

```java
public static final
Tree.Kind
DEBUGGER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

DebuggerTree

.

---

#### DEBUGGER

public static final

Tree.Kind

DEBUGGER

Used for instances of

DebuggerTree

.

FOR_IN_LOOP

```java
public static final
Tree.Kind
FOR_IN_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ForInLoopTree

.

---

#### FOR_IN_LOOP

public static final

Tree.Kind

FOR_IN_LOOP

Used for instances of

ForInLoopTree

.

FUNCTION_EXPRESSION

```java
public static final
Tree.Kind
FUNCTION_EXPRESSION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionExpressionTree

.

---

#### FUNCTION_EXPRESSION

public static final

Tree.Kind

FUNCTION_EXPRESSION

Used for instances of

FunctionExpressionTree

.

ERROR

```java
public static final
Tree.Kind
ERROR
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ErroneousTree

.

---

#### ERROR

public static final

Tree.Kind

ERROR

Used for instances of

ErroneousTree

.

EXPRESSION_STATEMENT

```java
public static final
Tree.Kind
EXPRESSION_STATEMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

FOR_LOOP

```java
public static final
Tree.Kind
FOR_LOOP
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

INSTANCE_OF

```java
public static final
Tree.Kind
INSTANCE_OF
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

MODULE

```java
public static final
Tree.Kind
MODULE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ModuleTree

.

---

#### MODULE

public static final

Tree.Kind

MODULE

Used for instances of

ModuleTree

.

EXPORT_ENTRY

```java
public static final
Tree.Kind
EXPORT_ENTRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ExportEntryTree

.

---

#### EXPORT_ENTRY

public static final

Tree.Kind

EXPORT_ENTRY

Used for instances of

ExportEntryTree

.

IMPORT_ENTRY

```java
public static final
Tree.Kind
IMPORT_ENTRY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ImportEntryTree

.

---

#### IMPORT_ENTRY

public static final

Tree.Kind

IMPORT_ENTRY

Used for instances of

ImportEntryTree

.

FUNCTION

```java
public static final
Tree.Kind
FUNCTION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionDeclarationTree

.

---

#### FUNCTION

public static final

Tree.Kind

FUNCTION

Used for instances of

FunctionDeclarationTree

.

FUNCTION_INVOCATION

```java
public static final
Tree.Kind
FUNCTION_INVOCATION
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

FunctionCallTree

.

---

#### FUNCTION_INVOCATION

public static final

Tree.Kind

FUNCTION_INVOCATION

Used for instances of

FunctionCallTree

.

NEW

```java
public static final
Tree.Kind
NEW
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

NewTree

.

---

#### NEW

public static final

Tree.Kind

NEW

Used for instances of

NewTree

.

OBJECT_LITERAL

```java
public static final
Tree.Kind
OBJECT_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

ObjectLiteralTree

.

---

#### OBJECT_LITERAL

public static final

Tree.Kind

OBJECT_LITERAL

Used for instances of

ObjectLiteralTree

.

PARENTHESIZED

```java
public static final
Tree.Kind
PARENTHESIZED
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

PROPERTY

```java
public static final
Tree.Kind
PROPERTY
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

PropertyTree

.

---

#### PROPERTY

public static final

Tree.Kind

PROPERTY

Used for instances of

PropertyTree

.

REGEXP_LITERAL

```java
public static final
Tree.Kind
REGEXP_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

RegExpLiteralTree

.

---

#### REGEXP_LITERAL

public static final

Tree.Kind

REGEXP_LITERAL

Used for instances of

RegExpLiteralTree

.

TEMPLATE_LITERAL

```java
public static final
Tree.Kind
TEMPLATE_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

TemplateLiteralTree

.

---

#### TEMPLATE_LITERAL

public static final

Tree.Kind

TEMPLATE_LITERAL

Used for instances of

TemplateLiteralTree

.

RETURN

```java
public static final
Tree.Kind
RETURN
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

THROW

```java
public static final
Tree.Kind
THROW
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

VARIABLE

```java
public static final
Tree.Kind
VARIABLE
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

WITH

```java
public static final
Tree.Kind
WITH
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

WithTree

.

---

#### WITH

public static final

Tree.Kind

WITH

Used for instances of

WithTree

.

POSTFIX_INCREMENT

```java
public static final
Tree.Kind
POSTFIX_INCREMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

DELETE

```java
public static final
Tree.Kind
DELETE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
delete operator

delete

.

---

#### DELETE

public static final

Tree.Kind

DELETE

Used for instances of

UnaryTree

representing logical
delete operator

delete

.

TYPEOF

```java
public static final
Tree.Kind
TYPEOF
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
typeof operator

typeof

.

---

#### TYPEOF

public static final

Tree.Kind

TYPEOF

Used for instances of

UnaryTree

representing logical
typeof operator

typeof

.

VOID

```java
public static final
Tree.Kind
VOID
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

UnaryTree

representing logical
void operator

void

.

---

#### VOID

public static final

Tree.Kind

VOID

Used for instances of

UnaryTree

representing logical
void operator

void

.

COMMA

```java
public static final
Tree.Kind
COMMA
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
comma

,

.

---

#### COMMA

public static final

Tree.Kind

COMMA

Used for instances of

BinaryTree

representing
comma

,

.

MULTIPLY

```java
public static final
Tree.Kind
MULTIPLY
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

IN

```java
public static final
Tree.Kind
IN
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
in operator

in

.

---

#### IN

public static final

Tree.Kind

IN

Used for instances of

BinaryTree

representing
in operator

in

.

EQUAL_TO

```java
public static final
Tree.Kind
EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

STRICT_EQUAL_TO

```java
public static final
Tree.Kind
STRICT_EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
equal-to

===

.

---

#### STRICT_EQUAL_TO

public static final

Tree.Kind

STRICT_EQUAL_TO

Used for instances of

BinaryTree

representing
equal-to

===

.

STRICT_NOT_EQUAL_TO

```java
public static final
Tree.Kind
STRICT_NOT_EQUAL_TO
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

BinaryTree

representing
not-equal-to

!==

.

---

#### STRICT_NOT_EQUAL_TO

public static final

Tree.Kind

STRICT_NOT_EQUAL_TO

Used for instances of

BinaryTree

representing
not-equal-to

!==

.

AND

```java
public static final
Tree.Kind
AND
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

SPREAD

```java
public static final
Tree.Kind
SPREAD
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

SpreadTree

representing
spread "operator" for arrays and function call arguments.

---

#### SPREAD

public static final

Tree.Kind

SPREAD

Used for instances of

SpreadTree

representing
spread "operator" for arrays and function call arguments.

YIELD

```java
public static final
Tree.Kind
YIELD
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

YieldTree

representing (generator)
yield expression

yield expr

.

---

#### YIELD

public static final

Tree.Kind

YIELD

Used for instances of

YieldTree

representing (generator)
yield expression

yield expr

.

NUMBER_LITERAL

```java
public static final
Tree.Kind
NUMBER_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

Used for instances of

LiteralTree

representing
a number literal expression of type

double

.

---

#### NUMBER_LITERAL

public static final

Tree.Kind

NUMBER_LITERAL

Used for instances of

LiteralTree

representing
a number literal expression of type

double

.

BOOLEAN_LITERAL

```java
public static final
Tree.Kind
BOOLEAN_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

STRING_LITERAL

```java
public static final
Tree.Kind
STRING_LITERAL
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

OTHER

```java
public static final
Tree.Kind
OTHER
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the associated interface type that uses this kind.

**Returns:** the associated interface

- isLiteral

```java
public boolean isLiteral()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a literal tree kind or not.

**Returns:** true if this is a literal tree kind, false otherwise

- isExpression

```java
public boolean isExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is an expression tree kind or not.

**Returns:** true if this is an expression tree kind, false otherwise

- isStatement

```java
public boolean isStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a statement tree kind or not.

**Returns:** true if this is a statement tree kind, false otherwise

---

#### Method Detail

values

```java
public static
Tree.Kind
[] values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

isLiteral

```java
public boolean isLiteral()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a literal tree kind or not.

**Returns:** true if this is a literal tree kind, false otherwise

---

#### isLiteral

public boolean isLiteral()

Returns if this is a literal tree kind or not.

isExpression

```java
public boolean isExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is an expression tree kind or not.

**Returns:** true if this is an expression tree kind, false otherwise

---

#### isExpression

public boolean isExpression()

Returns if this is an expression tree kind or not.

isStatement

```java
public boolean isStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a statement tree kind or not.

**Returns:** true if this is a statement tree kind, false otherwise

---

#### isStatement

public boolean isStatement()

Returns if this is a statement tree kind or not.

---

