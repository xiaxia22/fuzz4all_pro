# Interface TreeVisitor<R,​P>

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\TreeVisitor.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
TreeVisitor<R,​P>
```

A visitor of trees, in the style of the visitor design pattern.
Classes implementing this interface are used to operate
on a tree when the kind of tree is unknown at compile time.
When a visitor is passed to an tree's

accept

method, the

visit

Xyz

method most applicable
to that tree is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the ECMAScript programming
language. When new visit methods are added for new Tree subtypes,
default method bodies will be introduced which will call visitUnknown
method as a fallback.

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's
methods. Use

Void

for visitors that do not need an
additional parameter.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### R
visitAssignment​(
AssignmentTree
node,

P
p)

Visit assignment tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)

Visit compound assignment tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitBinary​(
BinaryTree
node,

P
p)

Visit binary expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitBlock​(
BlockTree
node,

P
p)

Visit block statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitBreak​(
BreakTree
node,

P
p)

Visit break statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitCase​(
CaseTree
node,

P
p)

Visit case statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitCatch​(
CatchTree
node,

P
p)

Visit catch block statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)

Visit class statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitClassExpression​(
ClassExpressionTree
node,

P
p)

Visit class expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)

Visit conditional expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitContinue​(
ContinueTree
node,

P
p)

Visit continue statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitDebugger​(
DebuggerTree
node,

P
p)

Visit debugger statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)

Visit do-while statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitErroneous​(
ErroneousTree
node,

P
p)

Visit error expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)

Visit expression statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitForLoop​(
ForLoopTree
node,

P
p)

Visit 'for' statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitForInLoop​(
ForInLoopTree
node,

P
p)

Visit for..in statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)

Visit for..of statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitFunctionCall​(
FunctionCallTree
node,

P
p)

Visit function call expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitFunctionDeclaration​(
FunctionDeclarationTree
node,

P
p)

Visit function declaration tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitFunctionExpression​(
FunctionExpressionTree
node,

P
p)

Visit function expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitIdentifier​(
IdentifierTree
node,

P
p)

Visit identifier tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitIf​(
IfTree
node,

P
p)

Visit 'if' statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)

Visit array access expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitArrayLiteral​(
ArrayLiteralTree
node,

P
p)

Visit array literal expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)

Visit labeled statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitLiteral​(
LiteralTree
node,

P
p)

Visit literal expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitParenthesized​(
ParenthesizedTree
node,

P
p)

Visit parenthesized expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitReturn​(
ReturnTree
node,

P
p)

Visit return statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitMemberSelect​(
MemberSelectTree
node,

P
p)

Visit member select expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitNew​(
NewTree
node,

P
p)

Visit 'new' expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitObjectLiteral​(
ObjectLiteralTree
node,

P
p)

Visit object literal tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitProperty​(
PropertyTree
node,

P
p)

Visit a property of an object literal expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitRegExpLiteral​(
RegExpLiteralTree
node,

P
p)

Visit regular expression literal tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)

Visit template literal tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)

Visit an empty statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitSpread​(
SpreadTree
node,

P
p)

Visit 'spread' expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitSwitch​(
SwitchTree
node,

P
p)

Visit 'switch' statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitThrow​(
ThrowTree
node,

P
p)

Visit 'throw' expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)

Visit compilation unit tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitModule​(
ModuleTree
node,

P
p)

Visit Module tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitExportEntry​(
ExportEntryTree
node,

P
p)

Visit Module ExportEntry tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitImportEntry​(
ImportEntryTree
node,

P
p)

Visit Module ImportEntry tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitTry​(
TryTree
node,

P
p)

Visit 'try' statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitInstanceOf​(
InstanceOfTree
node,

P
p)

Visit 'instanceof' expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitUnary​(
UnaryTree
node,

P
p)

Visit unary expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitVariable​(
VariableTree
node,

P
p)

Visit variable declaration tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitWhileLoop​(
WhileLoopTree
node,

P
p)

Visit 'while' statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitWith​(
WithTree
node,

P
p)

Visit 'with' statement tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitYield​(
YieldTree
node,

P
p)

Visit 'yield' expression tree.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

#### R
visitUnknown​(
Tree
node,

P
p)

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- value from the visitor

---

### Additional Sections

#### Interface TreeVisitor<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's
methods. Use

Void

for visitors that do not need an
additional parameter.

**All Known Implementing Classes:** SimpleTreeVisitorES5_1

,

SimpleTreeVisitorES6

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
TreeVisitor<R,​P>
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A visitor of trees, in the style of the visitor design pattern.
Classes implementing this interface are used to operate
on a tree when the kind of tree is unknown at compile time.
When a visitor is passed to an tree's

accept

method, the

visit

Xyz

method most applicable
to that tree is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the ECMAScript programming
language. When new visit methods are added for new Tree subtypes,
default method bodies will be introduced which will call visitUnknown
method as a fallback.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

TreeVisitor<R,​P>

A visitor of trees, in the style of the visitor design pattern.
Classes implementing this interface are used to operate
on a tree when the kind of tree is unknown at compile time.
When a visitor is passed to an tree's

accept

method, the

visit

Xyz

method most applicable
to that tree is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the ECMAScript programming
language. When new visit methods are added for new Tree subtypes,
default method bodies will be introduced which will call visitUnknown
method as a fallback.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the ECMAScript programming
language. When new visit methods are added for new Tree subtypes,
default method bodies will be introduced which will call visitUnknown
method as a fallback.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the ECMAScript programming
language. When new visit methods are added for new Tree subtypes,
default method bodies will be introduced which will call visitUnknown
method as a fallback.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

R

visitArrayAccess

​(

ArrayAccessTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array access expression tree.

R

visitArrayLiteral

​(

ArrayLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array literal expression tree.

R

visitAssignment

​(

AssignmentTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit assignment tree.

R

visitBinary

​(

BinaryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit binary expression tree.

R

visitBlock

​(

BlockTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit block statement tree.

R

visitBreak

​(

BreakTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit break statement tree.

R

visitCase

​(

CaseTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit case statement tree.

R

visitCatch

​(

CatchTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit catch block statement tree.

R

visitClassDeclaration

​(

ClassDeclarationTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class statement tree.

R

visitClassExpression

​(

ClassExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class expression tree.

R

visitCompilationUnit

​(

CompilationUnitTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compilation unit tree.

R

visitCompoundAssignment

​(

CompoundAssignmentTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compound assignment tree.

R

visitConditionalExpression

​(

ConditionalExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit conditional expression tree.

R

visitContinue

​(

ContinueTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit continue statement tree.

R

visitDebugger

​(

DebuggerTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit debugger statement tree.

R

visitDoWhileLoop

​(

DoWhileLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit do-while statement tree.

R

visitEmptyStatement

​(

EmptyStatementTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit an empty statement tree.

R

visitErroneous

​(

ErroneousTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit error expression tree.

R

visitExportEntry

​(

ExportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ExportEntry tree.

R

visitExpressionStatement

​(

ExpressionStatementTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit expression statement tree.

R

visitForInLoop

​(

ForInLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..in statement tree.

R

visitForLoop

​(

ForLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'for' statement tree.

R

visitForOfLoop

​(

ForOfLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..of statement tree.

R

visitFunctionCall

​(

FunctionCallTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function call expression tree.

R

visitFunctionDeclaration

​(

FunctionDeclarationTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function declaration tree.

R

visitFunctionExpression

​(

FunctionExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function expression tree.

R

visitIdentifier

​(

IdentifierTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit identifier tree.

R

visitIf

​(

IfTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'if' statement tree.

R

visitImportEntry

​(

ImportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ImportEntry tree.

R

visitInstanceOf

​(

InstanceOfTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'instanceof' expression tree.

R

visitLabeledStatement

​(

LabeledStatementTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit labeled statement tree.

R

visitLiteral

​(

LiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit literal expression tree.

R

visitMemberSelect

​(

MemberSelectTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit member select expression tree.

R

visitModule

​(

ModuleTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module tree.

R

visitNew

​(

NewTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'new' expression tree.

R

visitObjectLiteral

​(

ObjectLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit object literal tree.

R

visitParenthesized

​(

ParenthesizedTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit parenthesized expression tree.

R

visitProperty

​(

PropertyTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit a property of an object literal expression tree.

R

visitRegExpLiteral

​(

RegExpLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit regular expression literal tree.

R

visitReturn

​(

ReturnTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit return statement tree.

R

visitSpread

​(

SpreadTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'spread' expression tree.

R

visitSwitch

​(

SwitchTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'switch' statement tree.

R

visitTemplateLiteral

​(

TemplateLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit template literal tree.

R

visitThrow

​(

ThrowTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'throw' expression tree.

R

visitTry

​(

TryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'try' statement tree.

R

visitUnary

​(

UnaryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unary expression tree.

R

visitUnknown

​(

Tree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree.

R

visitVariable

​(

VariableTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit variable declaration tree.

R

visitWhileLoop

​(

WhileLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'while' statement tree.

R

visitWith

​(

WithTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'with' statement tree.

R

visitYield

​(

YieldTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'yield' expression tree.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

R

visitArrayAccess

​(

ArrayAccessTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array access expression tree.

R

visitArrayLiteral

​(

ArrayLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array literal expression tree.

R

visitAssignment

​(

AssignmentTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit assignment tree.

R

visitBinary

​(

BinaryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit binary expression tree.

R

visitBlock

​(

BlockTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit block statement tree.

R

visitBreak

​(

BreakTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit break statement tree.

R

visitCase

​(

CaseTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit case statement tree.

R

visitCatch

​(

CatchTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit catch block statement tree.

R

visitClassDeclaration

​(

ClassDeclarationTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class statement tree.

R

visitClassExpression

​(

ClassExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class expression tree.

R

visitCompilationUnit

​(

CompilationUnitTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compilation unit tree.

R

visitCompoundAssignment

​(

CompoundAssignmentTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compound assignment tree.

R

visitConditionalExpression

​(

ConditionalExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit conditional expression tree.

R

visitContinue

​(

ContinueTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit continue statement tree.

R

visitDebugger

​(

DebuggerTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit debugger statement tree.

R

visitDoWhileLoop

​(

DoWhileLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit do-while statement tree.

R

visitEmptyStatement

​(

EmptyStatementTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit an empty statement tree.

R

visitErroneous

​(

ErroneousTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit error expression tree.

R

visitExportEntry

​(

ExportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ExportEntry tree.

R

visitExpressionStatement

​(

ExpressionStatementTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit expression statement tree.

R

visitForInLoop

​(

ForInLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..in statement tree.

R

visitForLoop

​(

ForLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'for' statement tree.

R

visitForOfLoop

​(

ForOfLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..of statement tree.

R

visitFunctionCall

​(

FunctionCallTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function call expression tree.

R

visitFunctionDeclaration

​(

FunctionDeclarationTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function declaration tree.

R

visitFunctionExpression

​(

FunctionExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function expression tree.

R

visitIdentifier

​(

IdentifierTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit identifier tree.

R

visitIf

​(

IfTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'if' statement tree.

R

visitImportEntry

​(

ImportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ImportEntry tree.

R

visitInstanceOf

​(

InstanceOfTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'instanceof' expression tree.

R

visitLabeledStatement

​(

LabeledStatementTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit labeled statement tree.

R

visitLiteral

​(

LiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit literal expression tree.

R

visitMemberSelect

​(

MemberSelectTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit member select expression tree.

R

visitModule

​(

ModuleTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module tree.

R

visitNew

​(

NewTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'new' expression tree.

R

visitObjectLiteral

​(

ObjectLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit object literal tree.

R

visitParenthesized

​(

ParenthesizedTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit parenthesized expression tree.

R

visitProperty

​(

PropertyTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit a property of an object literal expression tree.

R

visitRegExpLiteral

​(

RegExpLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit regular expression literal tree.

R

visitReturn

​(

ReturnTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit return statement tree.

R

visitSpread

​(

SpreadTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'spread' expression tree.

R

visitSwitch

​(

SwitchTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'switch' statement tree.

R

visitTemplateLiteral

​(

TemplateLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit template literal tree.

R

visitThrow

​(

ThrowTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'throw' expression tree.

R

visitTry

​(

TryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'try' statement tree.

R

visitUnary

​(

UnaryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unary expression tree.

R

visitUnknown

​(

Tree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree.

R

visitVariable

​(

VariableTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit variable declaration tree.

R

visitWhileLoop

​(

WhileLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'while' statement tree.

R

visitWith

​(

WithTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'with' statement tree.

R

visitYield

​(

YieldTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'yield' expression tree.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array access expression tree.

Visit array literal expression tree.

Visit assignment tree.

Visit binary expression tree.

Visit block statement tree.

Visit break statement tree.

Visit case statement tree.

Visit catch block statement tree.

Visit class statement tree.

Visit class expression tree.

Visit compilation unit tree.

Visit compound assignment tree.

Visit conditional expression tree.

Visit continue statement tree.

Visit debugger statement tree.

Visit do-while statement tree.

Visit an empty statement tree.

Visit error expression tree.

Visit Module ExportEntry tree.

Visit expression statement tree.

Visit for..in statement tree.

Visit 'for' statement tree.

Visit for..of statement tree.

Visit function call expression tree.

Visit function declaration tree.

Visit function expression tree.

Visit identifier tree.

Visit 'if' statement tree.

Visit Module ImportEntry tree.

Visit 'instanceof' expression tree.

Visit labeled statement tree.

Visit literal expression tree.

Visit member select expression tree.

Visit Module tree.

Visit 'new' expression tree.

Visit object literal tree.

Visit parenthesized expression tree.

Visit a property of an object literal expression tree.

Visit regular expression literal tree.

Visit return statement tree.

Visit 'spread' expression tree.

Visit 'switch' statement tree.

Visit template literal tree.

Visit 'throw' expression tree.

Visit 'try' statement tree.

Visit unary expression tree.

Visit unknown expression/statement tree.

Visit variable declaration tree.

Visit 'while' statement tree.

Visit 'with' statement tree.

Visit 'yield' expression tree.

============ METHOD DETAIL ==========

- Method Detail

- visitAssignment

```java
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit assignment tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCompoundAssignment

```java
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compound assignment tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitBinary

```java
R
visitBinary​(
BinaryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit binary expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitBlock

```java
R
visitBlock​(
BlockTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit block statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitBreak

```java
R
visitBreak​(
BreakTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit break statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCase

```java
R
visitCase​(
CaseTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit case statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCatch

```java
R
visitCatch​(
CatchTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit catch block statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitClassDeclaration

```java
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitClassExpression

```java
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitConditionalExpression

```java
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit conditional expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitContinue

```java
R
visitContinue​(
ContinueTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit continue statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitDebugger

```java
R
visitDebugger​(
DebuggerTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit debugger statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitDoWhileLoop

```java
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit do-while statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit error expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitExpressionStatement

```java
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit expression statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitForLoop

```java
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'for' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitForInLoop

```java
R
visitForInLoop​(
ForInLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..in statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitForOfLoop

```java
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..of statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitFunctionCall

```java
R
visitFunctionCall​(
FunctionCallTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function call expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitFunctionDeclaration

```java
R
visitFunctionDeclaration​(
FunctionDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function declaration tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitFunctionExpression

```java
R
visitFunctionExpression​(
FunctionExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit identifier tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitIf

```java
R
visitIf​(
IfTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'if' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitArrayAccess

```java
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array access expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitArrayLiteral

```java
R
visitArrayLiteral​(
ArrayLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitLabeledStatement

```java
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit labeled statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitParenthesized

```java
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit parenthesized expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit return statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitMemberSelect

```java
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit member select expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitNew

```java
R
visitNew​(
NewTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'new' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitObjectLiteral

```java
R
visitObjectLiteral​(
ObjectLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit object literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitProperty

```java
R
visitProperty​(
PropertyTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit a property of an object literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitRegExpLiteral

```java
R
visitRegExpLiteral​(
RegExpLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit regular expression literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitTemplateLiteral

```java
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit template literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitEmptyStatement

```java
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit an empty statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitSpread

```java
R
visitSpread​(
SpreadTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'spread' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitSwitch

```java
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'switch' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitThrow

```java
R
visitThrow​(
ThrowTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'throw' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCompilationUnit

```java
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compilation unit tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitModule

```java
R
visitModule​(
ModuleTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitExportEntry

```java
R
visitExportEntry​(
ExportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ExportEntry tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitImportEntry

```java
R
visitImportEntry​(
ImportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ImportEntry tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitTry

```java
R
visitTry​(
TryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'try' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitInstanceOf

```java
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'instanceof' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitUnary

```java
R
visitUnary​(
UnaryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unary expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitVariable

```java
R
visitVariable​(
VariableTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit variable declaration tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitWhileLoop

```java
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'while' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitWith

```java
R
visitWith​(
WithTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'with' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitYield

```java
R
visitYield​(
YieldTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'yield' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitUnknown

```java
R
visitUnknown​(
Tree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

Method Detail

- visitAssignment

```java
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit assignment tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCompoundAssignment

```java
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compound assignment tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitBinary

```java
R
visitBinary​(
BinaryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit binary expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitBlock

```java
R
visitBlock​(
BlockTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit block statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitBreak

```java
R
visitBreak​(
BreakTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit break statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCase

```java
R
visitCase​(
CaseTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit case statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCatch

```java
R
visitCatch​(
CatchTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit catch block statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitClassDeclaration

```java
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitClassExpression

```java
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitConditionalExpression

```java
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit conditional expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitContinue

```java
R
visitContinue​(
ContinueTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit continue statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitDebugger

```java
R
visitDebugger​(
DebuggerTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit debugger statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitDoWhileLoop

```java
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit do-while statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit error expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitExpressionStatement

```java
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit expression statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitForLoop

```java
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'for' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitForInLoop

```java
R
visitForInLoop​(
ForInLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..in statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitForOfLoop

```java
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..of statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitFunctionCall

```java
R
visitFunctionCall​(
FunctionCallTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function call expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitFunctionDeclaration

```java
R
visitFunctionDeclaration​(
FunctionDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function declaration tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitFunctionExpression

```java
R
visitFunctionExpression​(
FunctionExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit identifier tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitIf

```java
R
visitIf​(
IfTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'if' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitArrayAccess

```java
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array access expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitArrayLiteral

```java
R
visitArrayLiteral​(
ArrayLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitLabeledStatement

```java
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit labeled statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitParenthesized

```java
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit parenthesized expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit return statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitMemberSelect

```java
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit member select expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitNew

```java
R
visitNew​(
NewTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'new' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitObjectLiteral

```java
R
visitObjectLiteral​(
ObjectLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit object literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitProperty

```java
R
visitProperty​(
PropertyTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit a property of an object literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitRegExpLiteral

```java
R
visitRegExpLiteral​(
RegExpLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit regular expression literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitTemplateLiteral

```java
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit template literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitEmptyStatement

```java
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit an empty statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitSpread

```java
R
visitSpread​(
SpreadTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'spread' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitSwitch

```java
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'switch' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitThrow

```java
R
visitThrow​(
ThrowTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'throw' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitCompilationUnit

```java
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compilation unit tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitModule

```java
R
visitModule​(
ModuleTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitExportEntry

```java
R
visitExportEntry​(
ExportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ExportEntry tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitImportEntry

```java
R
visitImportEntry​(
ImportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ImportEntry tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitTry

```java
R
visitTry​(
TryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'try' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitInstanceOf

```java
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'instanceof' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitUnary

```java
R
visitUnary​(
UnaryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unary expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitVariable

```java
R
visitVariable​(
VariableTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit variable declaration tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitWhileLoop

```java
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'while' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitWith

```java
R
visitWith​(
WithTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'with' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitYield

```java
R
visitYield​(
YieldTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'yield' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

- visitUnknown

```java
R
visitUnknown​(
Tree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### Method Detail

visitAssignment

```java
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit assignment tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitAssignment

R

visitAssignment​(

AssignmentTree

node,

P

p)

Visit assignment tree.

visitCompoundAssignment

```java
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compound assignment tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitCompoundAssignment

R

visitCompoundAssignment​(

CompoundAssignmentTree

node,

P

p)

Visit compound assignment tree.

visitBinary

```java
R
visitBinary​(
BinaryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit binary expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitBinary

R

visitBinary​(

BinaryTree

node,

P

p)

Visit binary expression tree.

visitBlock

```java
R
visitBlock​(
BlockTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit block statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitBlock

R

visitBlock​(

BlockTree

node,

P

p)

Visit block statement tree.

visitBreak

```java
R
visitBreak​(
BreakTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit break statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitBreak

R

visitBreak​(

BreakTree

node,

P

p)

Visit break statement tree.

visitCase

```java
R
visitCase​(
CaseTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit case statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitCase

R

visitCase​(

CaseTree

node,

P

p)

Visit case statement tree.

visitCatch

```java
R
visitCatch​(
CatchTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit catch block statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitCatch

R

visitCatch​(

CatchTree

node,

P

p)

Visit catch block statement tree.

visitClassDeclaration

```java
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitClassDeclaration

R

visitClassDeclaration​(

ClassDeclarationTree

node,

P

p)

Visit class statement tree.

visitClassExpression

```java
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitClassExpression

R

visitClassExpression​(

ClassExpressionTree

node,

P

p)

Visit class expression tree.

visitConditionalExpression

```java
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit conditional expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitConditionalExpression

R

visitConditionalExpression​(

ConditionalExpressionTree

node,

P

p)

Visit conditional expression tree.

visitContinue

```java
R
visitContinue​(
ContinueTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit continue statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitContinue

R

visitContinue​(

ContinueTree

node,

P

p)

Visit continue statement tree.

visitDebugger

```java
R
visitDebugger​(
DebuggerTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit debugger statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitDebugger

R

visitDebugger​(

DebuggerTree

node,

P

p)

Visit debugger statement tree.

visitDoWhileLoop

```java
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit do-while statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitDoWhileLoop

R

visitDoWhileLoop​(

DoWhileLoopTree

node,

P

p)

Visit do-while statement tree.

visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit error expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitErroneous

R

visitErroneous​(

ErroneousTree

node,

P

p)

Visit error expression tree.

visitExpressionStatement

```java
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit expression statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitExpressionStatement

R

visitExpressionStatement​(

ExpressionStatementTree

node,

P

p)

Visit expression statement tree.

visitForLoop

```java
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'for' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitForLoop

R

visitForLoop​(

ForLoopTree

node,

P

p)

Visit 'for' statement tree.

visitForInLoop

```java
R
visitForInLoop​(
ForInLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..in statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitForInLoop

R

visitForInLoop​(

ForInLoopTree

node,

P

p)

Visit for..in statement tree.

visitForOfLoop

```java
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..of statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitForOfLoop

R

visitForOfLoop​(

ForOfLoopTree

node,

P

p)

Visit for..of statement tree.

visitFunctionCall

```java
R
visitFunctionCall​(
FunctionCallTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function call expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitFunctionCall

R

visitFunctionCall​(

FunctionCallTree

node,

P

p)

Visit function call expression tree.

visitFunctionDeclaration

```java
R
visitFunctionDeclaration​(
FunctionDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function declaration tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitFunctionDeclaration

R

visitFunctionDeclaration​(

FunctionDeclarationTree

node,

P

p)

Visit function declaration tree.

visitFunctionExpression

```java
R
visitFunctionExpression​(
FunctionExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit function expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitFunctionExpression

R

visitFunctionExpression​(

FunctionExpressionTree

node,

P

p)

Visit function expression tree.

visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit identifier tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitIdentifier

R

visitIdentifier​(

IdentifierTree

node,

P

p)

Visit identifier tree.

visitIf

```java
R
visitIf​(
IfTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'if' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitIf

R

visitIf​(

IfTree

node,

P

p)

Visit 'if' statement tree.

visitArrayAccess

```java
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array access expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitArrayAccess

R

visitArrayAccess​(

ArrayAccessTree

node,

P

p)

Visit array access expression tree.

visitArrayLiteral

```java
R
visitArrayLiteral​(
ArrayLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit array literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitArrayLiteral

R

visitArrayLiteral​(

ArrayLiteralTree

node,

P

p)

Visit array literal expression tree.

visitLabeledStatement

```java
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit labeled statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitLabeledStatement

R

visitLabeledStatement​(

LabeledStatementTree

node,

P

p)

Visit labeled statement tree.

visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitLiteral

R

visitLiteral​(

LiteralTree

node,

P

p)

Visit literal expression tree.

visitParenthesized

```java
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit parenthesized expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitParenthesized

R

visitParenthesized​(

ParenthesizedTree

node,

P

p)

Visit parenthesized expression tree.

visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit return statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitReturn

R

visitReturn​(

ReturnTree

node,

P

p)

Visit return statement tree.

visitMemberSelect

```java
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit member select expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitMemberSelect

R

visitMemberSelect​(

MemberSelectTree

node,

P

p)

Visit member select expression tree.

visitNew

```java
R
visitNew​(
NewTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'new' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitNew

R

visitNew​(

NewTree

node,

P

p)

Visit 'new' expression tree.

visitObjectLiteral

```java
R
visitObjectLiteral​(
ObjectLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit object literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitObjectLiteral

R

visitObjectLiteral​(

ObjectLiteralTree

node,

P

p)

Visit object literal tree.

visitProperty

```java
R
visitProperty​(
PropertyTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit a property of an object literal expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitProperty

R

visitProperty​(

PropertyTree

node,

P

p)

Visit a property of an object literal expression tree.

visitRegExpLiteral

```java
R
visitRegExpLiteral​(
RegExpLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit regular expression literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitRegExpLiteral

R

visitRegExpLiteral​(

RegExpLiteralTree

node,

P

p)

Visit regular expression literal tree.

visitTemplateLiteral

```java
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit template literal tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitTemplateLiteral

R

visitTemplateLiteral​(

TemplateLiteralTree

node,

P

p)

Visit template literal tree.

visitEmptyStatement

```java
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit an empty statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitEmptyStatement

R

visitEmptyStatement​(

EmptyStatementTree

node,

P

p)

Visit an empty statement tree.

visitSpread

```java
R
visitSpread​(
SpreadTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'spread' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitSpread

R

visitSpread​(

SpreadTree

node,

P

p)

Visit 'spread' expression tree.

visitSwitch

```java
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'switch' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitSwitch

R

visitSwitch​(

SwitchTree

node,

P

p)

Visit 'switch' statement tree.

visitThrow

```java
R
visitThrow​(
ThrowTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'throw' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitThrow

R

visitThrow​(

ThrowTree

node,

P

p)

Visit 'throw' expression tree.

visitCompilationUnit

```java
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit compilation unit tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitCompilationUnit

R

visitCompilationUnit​(

CompilationUnitTree

node,

P

p)

Visit compilation unit tree.

visitModule

```java
R
visitModule​(
ModuleTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitModule

R

visitModule​(

ModuleTree

node,

P

p)

Visit Module tree.

visitExportEntry

```java
R
visitExportEntry​(
ExportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ExportEntry tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitExportEntry

R

visitExportEntry​(

ExportEntryTree

node,

P

p)

Visit Module ExportEntry tree.

visitImportEntry

```java
R
visitImportEntry​(
ImportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ImportEntry tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitImportEntry

R

visitImportEntry​(

ImportEntryTree

node,

P

p)

Visit Module ImportEntry tree.

visitTry

```java
R
visitTry​(
TryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'try' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitTry

R

visitTry​(

TryTree

node,

P

p)

Visit 'try' statement tree.

visitInstanceOf

```java
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'instanceof' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitInstanceOf

R

visitInstanceOf​(

InstanceOfTree

node,

P

p)

Visit 'instanceof' expression tree.

visitUnary

```java
R
visitUnary​(
UnaryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unary expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitUnary

R

visitUnary​(

UnaryTree

node,

P

p)

Visit unary expression tree.

visitVariable

```java
R
visitVariable​(
VariableTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit variable declaration tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitVariable

R

visitVariable​(

VariableTree

node,

P

p)

Visit variable declaration tree.

visitWhileLoop

```java
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'while' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitWhileLoop

R

visitWhileLoop​(

WhileLoopTree

node,

P

p)

Visit 'while' statement tree.

visitWith

```java
R
visitWith​(
WithTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'with' statement tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitWith

R

visitWith​(

WithTree

node,

P

p)

Visit 'with' statement tree.

visitYield

```java
R
visitYield​(
YieldTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'yield' expression tree.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitYield

R

visitYield​(

YieldTree

node,

P

p)

Visit 'yield' expression tree.

visitUnknown

```java
R
visitUnknown​(
Tree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitUnknown

R

visitUnknown​(

Tree

node,

P

p)

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

---

