# Interface TreeVisitor<R,​P>

**Source:** `jdk.compiler\com\sun\source\tree\TreeVisitor.html`

### Class Description

```java
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
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

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
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)

Visits an AnnotatedTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitAnnotation​(
AnnotationTree
node,

P
p)

Visits an AnnotatedTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)

Visits a MethodInvocationTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitAssert​(
AssertTree
node,

P
p)

Visits an AssertTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitAssignment​(
AssignmentTree
node,

P
p)

Visits an AssignmentTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)

Visits a CompoundAssignmentTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitBinary​(
BinaryTree
node,

P
p)

Visits a BinaryTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitBlock​(
BlockTree
node,

P
p)

Visits a BlockTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitBreak​(
BreakTree
node,

P
p)

Visits a BreakTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitCase​(
CaseTree
node,

P
p)

Visits a CaseTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitCatch​(
CatchTree
node,

P
p)

Visits a CatchTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitClass​(
ClassTree
node,

P
p)

Visits a ClassTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)

Visits a ConditionalExpressionTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitContinue​(
ContinueTree
node,

P
p)

Visits a ContinueTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)

Visits a DoWhileTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitErroneous​(
ErroneousTree
node,

P
p)

Visits an ErroneousTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)

Visits an ExpressionStatementTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)

Visits an EnhancedForLoopTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitForLoop​(
ForLoopTree
node,

P
p)

Visits a ForLoopTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitIdentifier​(
IdentifierTree
node,

P
p)

Visits an IdentifierTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitIf​(
IfTree
node,

P
p)

Visits an IfTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitImport​(
ImportTree
node,

P
p)

Visits an ImportTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)

Visits an ArrayAccessTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)

Visits a LabeledStatementTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitLiteral​(
LiteralTree
node,

P
p)

Visits a LiteralTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitMethod​(
MethodTree
node,

P
p)

Visits a MethodTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitModifiers​(
ModifiersTree
node,

P
p)

Visits a ModifiersTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitNewArray​(
NewArrayTree
node,

P
p)

Visits a NewArrayTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitNewClass​(
NewClassTree
node,

P
p)

Visits a NewClassTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)

Visits a LambdaExpressionTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitPackage​(
PackageTree
node,

P
p)

Visits a PackageTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitParenthesized​(
ParenthesizedTree
node,

P
p)

Visits a ParenthesizedTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitReturn​(
ReturnTree
node,

P
p)

Visits a ReturnTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitMemberSelect​(
MemberSelectTree
node,

P
p)

Visits a MemberSelectTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitMemberReference​(
MemberReferenceTree
node,

P
p)

Visits a MemberReferenceTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)

Visits an EmptyStatementTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitSwitch​(
SwitchTree
node,

P
p)

Visits a SwitchTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitSynchronized​(
SynchronizedTree
node,

P
p)

Visits a SynchronizedTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitThrow​(
ThrowTree
node,

P
p)

Visits a ThrowTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)

Visits a CompilationUnitTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitTry​(
TryTree
node,

P
p)

Visits a TryTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)

Visits a ParameterizedTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitUnionType​(
UnionTypeTree
node,

P
p)

Visits a UnionTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)

Visits an IntersectionTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitArrayType​(
ArrayTypeTree
node,

P
p)

Visits an ArrayTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitTypeCast​(
TypeCastTree
node,

P
p)

Visits a TypeCastTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)

Visits a PrimitiveTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitTypeParameter​(
TypeParameterTree
node,

P
p)

Visits a TypeParameterTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitInstanceOf​(
InstanceOfTree
node,

P
p)

Visits an InstanceOfTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitUnary​(
UnaryTree
node,

P
p)

Visits a UnaryTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitVariable​(
VariableTree
node,

P
p)

Visits a VariableTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitWhileLoop​(
WhileLoopTree
node,

P
p)

Visits a WhileLoopTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitWildcard​(
WildcardTree
node,

P
p)

Visits a WildcardTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitModule​(
ModuleTree
node,

P
p)

Visits a ModuleTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitExports​(
ExportsTree
node,

P
p)

Visits an ExportsTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitOpens​(
OpensTree
node,

P
p)

Visits an OpensTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitProvides​(
ProvidesTree
node,

P
p)

Visits a ProvidesTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitRequires​(
RequiresTree
node,

P
p)

Visits a RequiresTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitUses​(
UsesTree
node,

P
p)

Visits a UsesTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitOther​(
Tree
node,

P
p)

Visits an unknown type of Tree node.
This can occur if the language evolves and new kinds
of nodes are added to the

Tree

hierarchy.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

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

**All Known Implementing Classes:** SimpleTreeVisitor

,

TreePathScanner

,

TreeScanner

```java
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
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

**Since:** 1.6

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
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

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
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

R

visitAnnotatedType

​(

AnnotatedTypeTree

node,

P

p)

Visits an AnnotatedTypeTree node.

R

visitAnnotation

​(

AnnotationTree

node,

P

p)

Visits an AnnotatedTree node.

R

visitArrayAccess

​(

ArrayAccessTree

node,

P

p)

Visits an ArrayAccessTree node.

R

visitArrayType

​(

ArrayTypeTree

node,

P

p)

Visits an ArrayTypeTree node.

R

visitAssert

​(

AssertTree

node,

P

p)

Visits an AssertTree node.

R

visitAssignment

​(

AssignmentTree

node,

P

p)

Visits an AssignmentTree node.

R

visitBinary

​(

BinaryTree

node,

P

p)

Visits a BinaryTree node.

R

visitBlock

​(

BlockTree

node,

P

p)

Visits a BlockTree node.

R

visitBreak

​(

BreakTree

node,

P

p)

Visits a BreakTree node.

R

visitCase

​(

CaseTree

node,

P

p)

Visits a CaseTree node.

R

visitCatch

​(

CatchTree

node,

P

p)

Visits a CatchTree node.

R

visitClass

​(

ClassTree

node,

P

p)

Visits a ClassTree node.

R

visitCompilationUnit

​(

CompilationUnitTree

node,

P

p)

Visits a CompilationUnitTree node.

R

visitCompoundAssignment

​(

CompoundAssignmentTree

node,

P

p)

Visits a CompoundAssignmentTree node.

R

visitConditionalExpression

​(

ConditionalExpressionTree

node,

P

p)

Visits a ConditionalExpressionTree node.

R

visitContinue

​(

ContinueTree

node,

P

p)

Visits a ContinueTree node.

R

visitDoWhileLoop

​(

DoWhileLoopTree

node,

P

p)

Visits a DoWhileTree node.

R

visitEmptyStatement

​(

EmptyStatementTree

node,

P

p)

Visits an EmptyStatementTree node.

R

visitEnhancedForLoop

​(

EnhancedForLoopTree

node,

P

p)

Visits an EnhancedForLoopTree node.

R

visitErroneous

​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node.

R

visitExports

​(

ExportsTree

node,

P

p)

Visits an ExportsTree node.

R

visitExpressionStatement

​(

ExpressionStatementTree

node,

P

p)

Visits an ExpressionStatementTree node.

R

visitForLoop

​(

ForLoopTree

node,

P

p)

Visits a ForLoopTree node.

R

visitIdentifier

​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node.

R

visitIf

​(

IfTree

node,

P

p)

Visits an IfTree node.

R

visitImport

​(

ImportTree

node,

P

p)

Visits an ImportTree node.

R

visitInstanceOf

​(

InstanceOfTree

node,

P

p)

Visits an InstanceOfTree node.

R

visitIntersectionType

​(

IntersectionTypeTree

node,

P

p)

Visits an IntersectionTypeTree node.

R

visitLabeledStatement

​(

LabeledStatementTree

node,

P

p)

Visits a LabeledStatementTree node.

R

visitLambdaExpression

​(

LambdaExpressionTree

node,

P

p)

Visits a LambdaExpressionTree node.

R

visitLiteral

​(

LiteralTree

node,

P

p)

Visits a LiteralTree node.

R

visitMemberReference

​(

MemberReferenceTree

node,

P

p)

Visits a MemberReferenceTree node.

R

visitMemberSelect

​(

MemberSelectTree

node,

P

p)

Visits a MemberSelectTree node.

R

visitMethod

​(

MethodTree

node,

P

p)

Visits a MethodTree node.

R

visitMethodInvocation

​(

MethodInvocationTree

node,

P

p)

Visits a MethodInvocationTree node.

R

visitModifiers

​(

ModifiersTree

node,

P

p)

Visits a ModifiersTree node.

R

visitModule

​(

ModuleTree

node,

P

p)

Visits a ModuleTree node.

R

visitNewArray

​(

NewArrayTree

node,

P

p)

Visits a NewArrayTree node.

R

visitNewClass

​(

NewClassTree

node,

P

p)

Visits a NewClassTree node.

R

visitOpens

​(

OpensTree

node,

P

p)

Visits an OpensTree node.

R

visitOther

​(

Tree

node,

P

p)

Visits an unknown type of Tree node.

R

visitPackage

​(

PackageTree

node,

P

p)

Visits a PackageTree node.

R

visitParameterizedType

​(

ParameterizedTypeTree

node,

P

p)

Visits a ParameterizedTypeTree node.

R

visitParenthesized

​(

ParenthesizedTree

node,

P

p)

Visits a ParenthesizedTree node.

R

visitPrimitiveType

​(

PrimitiveTypeTree

node,

P

p)

Visits a PrimitiveTypeTree node.

R

visitProvides

​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node.

R

visitRequires

​(

RequiresTree

node,

P

p)

Visits a RequiresTree node.

R

visitReturn

​(

ReturnTree

node,

P

p)

Visits a ReturnTree node.

R

visitSwitch

​(

SwitchTree

node,

P

p)

Visits a SwitchTree node.

R

visitSynchronized

​(

SynchronizedTree

node,

P

p)

Visits a SynchronizedTree node.

R

visitThrow

​(

ThrowTree

node,

P

p)

Visits a ThrowTree node.

R

visitTry

​(

TryTree

node,

P

p)

Visits a TryTree node.

R

visitTypeCast

​(

TypeCastTree

node,

P

p)

Visits a TypeCastTree node.

R

visitTypeParameter

​(

TypeParameterTree

node,

P

p)

Visits a TypeParameterTree node.

R

visitUnary

​(

UnaryTree

node,

P

p)

Visits a UnaryTree node.

R

visitUnionType

​(

UnionTypeTree

node,

P

p)

Visits a UnionTypeTree node.

R

visitUses

​(

UsesTree

node,

P

p)

Visits a UsesTree node.

R

visitVariable

​(

VariableTree

node,

P

p)

Visits a VariableTree node.

R

visitWhileLoop

​(

WhileLoopTree

node,

P

p)

Visits a WhileLoopTree node.

R

visitWildcard

​(

WildcardTree

node,

P

p)

Visits a WildcardTypeTree node.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

R

visitAnnotatedType

​(

AnnotatedTypeTree

node,

P

p)

Visits an AnnotatedTypeTree node.

R

visitAnnotation

​(

AnnotationTree

node,

P

p)

Visits an AnnotatedTree node.

R

visitArrayAccess

​(

ArrayAccessTree

node,

P

p)

Visits an ArrayAccessTree node.

R

visitArrayType

​(

ArrayTypeTree

node,

P

p)

Visits an ArrayTypeTree node.

R

visitAssert

​(

AssertTree

node,

P

p)

Visits an AssertTree node.

R

visitAssignment

​(

AssignmentTree

node,

P

p)

Visits an AssignmentTree node.

R

visitBinary

​(

BinaryTree

node,

P

p)

Visits a BinaryTree node.

R

visitBlock

​(

BlockTree

node,

P

p)

Visits a BlockTree node.

R

visitBreak

​(

BreakTree

node,

P

p)

Visits a BreakTree node.

R

visitCase

​(

CaseTree

node,

P

p)

Visits a CaseTree node.

R

visitCatch

​(

CatchTree

node,

P

p)

Visits a CatchTree node.

R

visitClass

​(

ClassTree

node,

P

p)

Visits a ClassTree node.

R

visitCompilationUnit

​(

CompilationUnitTree

node,

P

p)

Visits a CompilationUnitTree node.

R

visitCompoundAssignment

​(

CompoundAssignmentTree

node,

P

p)

Visits a CompoundAssignmentTree node.

R

visitConditionalExpression

​(

ConditionalExpressionTree

node,

P

p)

Visits a ConditionalExpressionTree node.

R

visitContinue

​(

ContinueTree

node,

P

p)

Visits a ContinueTree node.

R

visitDoWhileLoop

​(

DoWhileLoopTree

node,

P

p)

Visits a DoWhileTree node.

R

visitEmptyStatement

​(

EmptyStatementTree

node,

P

p)

Visits an EmptyStatementTree node.

R

visitEnhancedForLoop

​(

EnhancedForLoopTree

node,

P

p)

Visits an EnhancedForLoopTree node.

R

visitErroneous

​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node.

R

visitExports

​(

ExportsTree

node,

P

p)

Visits an ExportsTree node.

R

visitExpressionStatement

​(

ExpressionStatementTree

node,

P

p)

Visits an ExpressionStatementTree node.

R

visitForLoop

​(

ForLoopTree

node,

P

p)

Visits a ForLoopTree node.

R

visitIdentifier

​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node.

R

visitIf

​(

IfTree

node,

P

p)

Visits an IfTree node.

R

visitImport

​(

ImportTree

node,

P

p)

Visits an ImportTree node.

R

visitInstanceOf

​(

InstanceOfTree

node,

P

p)

Visits an InstanceOfTree node.

R

visitIntersectionType

​(

IntersectionTypeTree

node,

P

p)

Visits an IntersectionTypeTree node.

R

visitLabeledStatement

​(

LabeledStatementTree

node,

P

p)

Visits a LabeledStatementTree node.

R

visitLambdaExpression

​(

LambdaExpressionTree

node,

P

p)

Visits a LambdaExpressionTree node.

R

visitLiteral

​(

LiteralTree

node,

P

p)

Visits a LiteralTree node.

R

visitMemberReference

​(

MemberReferenceTree

node,

P

p)

Visits a MemberReferenceTree node.

R

visitMemberSelect

​(

MemberSelectTree

node,

P

p)

Visits a MemberSelectTree node.

R

visitMethod

​(

MethodTree

node,

P

p)

Visits a MethodTree node.

R

visitMethodInvocation

​(

MethodInvocationTree

node,

P

p)

Visits a MethodInvocationTree node.

R

visitModifiers

​(

ModifiersTree

node,

P

p)

Visits a ModifiersTree node.

R

visitModule

​(

ModuleTree

node,

P

p)

Visits a ModuleTree node.

R

visitNewArray

​(

NewArrayTree

node,

P

p)

Visits a NewArrayTree node.

R

visitNewClass

​(

NewClassTree

node,

P

p)

Visits a NewClassTree node.

R

visitOpens

​(

OpensTree

node,

P

p)

Visits an OpensTree node.

R

visitOther

​(

Tree

node,

P

p)

Visits an unknown type of Tree node.

R

visitPackage

​(

PackageTree

node,

P

p)

Visits a PackageTree node.

R

visitParameterizedType

​(

ParameterizedTypeTree

node,

P

p)

Visits a ParameterizedTypeTree node.

R

visitParenthesized

​(

ParenthesizedTree

node,

P

p)

Visits a ParenthesizedTree node.

R

visitPrimitiveType

​(

PrimitiveTypeTree

node,

P

p)

Visits a PrimitiveTypeTree node.

R

visitProvides

​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node.

R

visitRequires

​(

RequiresTree

node,

P

p)

Visits a RequiresTree node.

R

visitReturn

​(

ReturnTree

node,

P

p)

Visits a ReturnTree node.

R

visitSwitch

​(

SwitchTree

node,

P

p)

Visits a SwitchTree node.

R

visitSynchronized

​(

SynchronizedTree

node,

P

p)

Visits a SynchronizedTree node.

R

visitThrow

​(

ThrowTree

node,

P

p)

Visits a ThrowTree node.

R

visitTry

​(

TryTree

node,

P

p)

Visits a TryTree node.

R

visitTypeCast

​(

TypeCastTree

node,

P

p)

Visits a TypeCastTree node.

R

visitTypeParameter

​(

TypeParameterTree

node,

P

p)

Visits a TypeParameterTree node.

R

visitUnary

​(

UnaryTree

node,

P

p)

Visits a UnaryTree node.

R

visitUnionType

​(

UnionTypeTree

node,

P

p)

Visits a UnionTypeTree node.

R

visitUses

​(

UsesTree

node,

P

p)

Visits a UsesTree node.

R

visitVariable

​(

VariableTree

node,

P

p)

Visits a VariableTree node.

R

visitWhileLoop

​(

WhileLoopTree

node,

P

p)

Visits a WhileLoopTree node.

R

visitWildcard

​(

WildcardTree

node,

P

p)

Visits a WildcardTypeTree node.

---

#### Method Summary

Visits an AnnotatedTypeTree node.

Visits an AnnotatedTree node.

Visits an ArrayAccessTree node.

Visits an ArrayTypeTree node.

Visits an AssertTree node.

Visits an AssignmentTree node.

Visits a BinaryTree node.

Visits a BlockTree node.

Visits a BreakTree node.

Visits a CaseTree node.

Visits a CatchTree node.

Visits a ClassTree node.

Visits a CompilationUnitTree node.

Visits a CompoundAssignmentTree node.

Visits a ConditionalExpressionTree node.

Visits a ContinueTree node.

Visits a DoWhileTree node.

Visits an EmptyStatementTree node.

Visits an EnhancedForLoopTree node.

Visits an ErroneousTree node.

Visits an ExportsTree node.

Visits an ExpressionStatementTree node.

Visits a ForLoopTree node.

Visits an IdentifierTree node.

Visits an IfTree node.

Visits an ImportTree node.

Visits an InstanceOfTree node.

Visits an IntersectionTypeTree node.

Visits a LabeledStatementTree node.

Visits a LambdaExpressionTree node.

Visits a LiteralTree node.

Visits a MemberReferenceTree node.

Visits a MemberSelectTree node.

Visits a MethodTree node.

Visits a MethodInvocationTree node.

Visits a ModifiersTree node.

Visits a ModuleTree node.

Visits a NewArrayTree node.

Visits a NewClassTree node.

Visits an OpensTree node.

Visits an unknown type of Tree node.

Visits a PackageTree node.

Visits a ParameterizedTypeTree node.

Visits a ParenthesizedTree node.

Visits a PrimitiveTypeTree node.

Visits a ProvidesTree node.

Visits a RequiresTree node.

Visits a ReturnTree node.

Visits a SwitchTree node.

Visits a SynchronizedTree node.

Visits a ThrowTree node.

Visits a TryTree node.

Visits a TypeCastTree node.

Visits a TypeParameterTree node.

Visits a UnaryTree node.

Visits a UnionTypeTree node.

Visits a UsesTree node.

Visits a VariableTree node.

Visits a WhileLoopTree node.

Visits a WildcardTypeTree node.

============ METHOD DETAIL ==========

- Method Detail

- visitAnnotatedType

```java
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)
```

Visits an AnnotatedTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAnnotation

```java
R
visitAnnotation​(
AnnotationTree
node,

P
p)
```

Visits an AnnotatedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMethodInvocation

```java
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)
```

Visits a MethodInvocationTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAssert

```java
R
visitAssert​(
AssertTree
node,

P
p)
```

Visits an AssertTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAssignment

```java
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Visits an AssignmentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCompoundAssignment

```java
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Visits a CompoundAssignmentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitBinary

```java
R
visitBinary​(
BinaryTree
node,

P
p)
```

Visits a BinaryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitBlock

```java
R
visitBlock​(
BlockTree
node,

P
p)
```

Visits a BlockTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitBreak

```java
R
visitBreak​(
BreakTree
node,

P
p)
```

Visits a BreakTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCase

```java
R
visitCase​(
CaseTree
node,

P
p)
```

Visits a CaseTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCatch

```java
R
visitCatch​(
CatchTree
node,

P
p)
```

Visits a CatchTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitClass

```java
R
visitClass​(
ClassTree
node,

P
p)
```

Visits a ClassTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitConditionalExpression

```java
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Visits a ConditionalExpressionTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitContinue

```java
R
visitContinue​(
ContinueTree
node,

P
p)
```

Visits a ContinueTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDoWhileLoop

```java
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Visits a DoWhileTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitExpressionStatement

```java
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Visits an ExpressionStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitEnhancedForLoop

```java
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)
```

Visits an EnhancedForLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitForLoop

```java
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Visits a ForLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIf

```java
R
visitIf​(
IfTree
node,

P
p)
```

Visits an IfTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitImport

```java
R
visitImport​(
ImportTree
node,

P
p)
```

Visits an ImportTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitArrayAccess

```java
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Visits an ArrayAccessTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLabeledStatement

```java
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Visits a LabeledStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits a LiteralTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMethod

```java
R
visitMethod​(
MethodTree
node,

P
p)
```

Visits a MethodTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitModifiers

```java
R
visitModifiers​(
ModifiersTree
node,

P
p)
```

Visits a ModifiersTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitNewArray

```java
R
visitNewArray​(
NewArrayTree
node,

P
p)
```

Visits a NewArrayTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitNewClass

```java
R
visitNewClass​(
NewClassTree
node,

P
p)
```

Visits a NewClassTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLambdaExpression

```java
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)
```

Visits a LambdaExpressionTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitPackage

```java
R
visitPackage​(
PackageTree
node,

P
p)
```

Visits a PackageTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitParenthesized

```java
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Visits a ParenthesizedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMemberSelect

```java
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Visits a MemberSelectTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMemberReference

```java
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)
```

Visits a MemberReferenceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitEmptyStatement

```java
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Visits an EmptyStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSwitch

```java
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Visits a SwitchTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSynchronized

```java
R
visitSynchronized​(
SynchronizedTree
node,

P
p)
```

Visits a SynchronizedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitThrow

```java
R
visitThrow​(
ThrowTree
node,

P
p)
```

Visits a ThrowTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCompilationUnit

```java
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Visits a CompilationUnitTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitTry

```java
R
visitTry​(
TryTree
node,

P
p)
```

Visits a TryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitParameterizedType

```java
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)
```

Visits a ParameterizedTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnionType

```java
R
visitUnionType​(
UnionTypeTree
node,

P
p)
```

Visits a UnionTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIntersectionType

```java
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)
```

Visits an IntersectionTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitArrayType

```java
R
visitArrayType​(
ArrayTypeTree
node,

P
p)
```

Visits an ArrayTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitTypeCast

```java
R
visitTypeCast​(
TypeCastTree
node,

P
p)
```

Visits a TypeCastTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitPrimitiveType

```java
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)
```

Visits a PrimitiveTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitTypeParameter

```java
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)
```

Visits a TypeParameterTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitInstanceOf

```java
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Visits an InstanceOfTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnary

```java
R
visitUnary​(
UnaryTree
node,

P
p)
```

Visits a UnaryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitVariable

```java
R
visitVariable​(
VariableTree
node,

P
p)
```

Visits a VariableTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitWhileLoop

```java
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Visits a WhileLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitWildcard

```java
R
visitWildcard​(
WildcardTree
node,

P
p)
```

Visits a WildcardTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitModule

```java
R
visitModule​(
ModuleTree
node,

P
p)
```

Visits a ModuleTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitExports

```java
R
visitExports​(
ExportsTree
node,

P
p)
```

Visits an ExportsTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitOpens

```java
R
visitOpens​(
OpensTree
node,

P
p)
```

Visits an OpensTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitProvides

```java
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitRequires

```java
R
visitRequires​(
RequiresTree
node,

P
p)
```

Visits a RequiresTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUses

```java
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitOther

```java
R
visitOther​(
Tree
node,

P
p)
```

Visits an unknown type of Tree node.
This can occur if the language evolves and new kinds
of nodes are added to the

Tree

hierarchy.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

Method Detail

- visitAnnotatedType

```java
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)
```

Visits an AnnotatedTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAnnotation

```java
R
visitAnnotation​(
AnnotationTree
node,

P
p)
```

Visits an AnnotatedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMethodInvocation

```java
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)
```

Visits a MethodInvocationTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAssert

```java
R
visitAssert​(
AssertTree
node,

P
p)
```

Visits an AssertTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAssignment

```java
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Visits an AssignmentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCompoundAssignment

```java
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Visits a CompoundAssignmentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitBinary

```java
R
visitBinary​(
BinaryTree
node,

P
p)
```

Visits a BinaryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitBlock

```java
R
visitBlock​(
BlockTree
node,

P
p)
```

Visits a BlockTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitBreak

```java
R
visitBreak​(
BreakTree
node,

P
p)
```

Visits a BreakTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCase

```java
R
visitCase​(
CaseTree
node,

P
p)
```

Visits a CaseTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCatch

```java
R
visitCatch​(
CatchTree
node,

P
p)
```

Visits a CatchTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitClass

```java
R
visitClass​(
ClassTree
node,

P
p)
```

Visits a ClassTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitConditionalExpression

```java
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Visits a ConditionalExpressionTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitContinue

```java
R
visitContinue​(
ContinueTree
node,

P
p)
```

Visits a ContinueTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDoWhileLoop

```java
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Visits a DoWhileTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitExpressionStatement

```java
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Visits an ExpressionStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitEnhancedForLoop

```java
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)
```

Visits an EnhancedForLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitForLoop

```java
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Visits a ForLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIf

```java
R
visitIf​(
IfTree
node,

P
p)
```

Visits an IfTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitImport

```java
R
visitImport​(
ImportTree
node,

P
p)
```

Visits an ImportTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitArrayAccess

```java
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Visits an ArrayAccessTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLabeledStatement

```java
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Visits a LabeledStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits a LiteralTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMethod

```java
R
visitMethod​(
MethodTree
node,

P
p)
```

Visits a MethodTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitModifiers

```java
R
visitModifiers​(
ModifiersTree
node,

P
p)
```

Visits a ModifiersTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitNewArray

```java
R
visitNewArray​(
NewArrayTree
node,

P
p)
```

Visits a NewArrayTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitNewClass

```java
R
visitNewClass​(
NewClassTree
node,

P
p)
```

Visits a NewClassTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLambdaExpression

```java
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)
```

Visits a LambdaExpressionTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitPackage

```java
R
visitPackage​(
PackageTree
node,

P
p)
```

Visits a PackageTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitParenthesized

```java
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Visits a ParenthesizedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMemberSelect

```java
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Visits a MemberSelectTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitMemberReference

```java
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)
```

Visits a MemberReferenceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitEmptyStatement

```java
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Visits an EmptyStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSwitch

```java
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Visits a SwitchTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSynchronized

```java
R
visitSynchronized​(
SynchronizedTree
node,

P
p)
```

Visits a SynchronizedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitThrow

```java
R
visitThrow​(
ThrowTree
node,

P
p)
```

Visits a ThrowTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitCompilationUnit

```java
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Visits a CompilationUnitTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitTry

```java
R
visitTry​(
TryTree
node,

P
p)
```

Visits a TryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitParameterizedType

```java
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)
```

Visits a ParameterizedTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnionType

```java
R
visitUnionType​(
UnionTypeTree
node,

P
p)
```

Visits a UnionTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIntersectionType

```java
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)
```

Visits an IntersectionTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitArrayType

```java
R
visitArrayType​(
ArrayTypeTree
node,

P
p)
```

Visits an ArrayTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitTypeCast

```java
R
visitTypeCast​(
TypeCastTree
node,

P
p)
```

Visits a TypeCastTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitPrimitiveType

```java
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)
```

Visits a PrimitiveTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitTypeParameter

```java
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)
```

Visits a TypeParameterTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitInstanceOf

```java
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Visits an InstanceOfTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnary

```java
R
visitUnary​(
UnaryTree
node,

P
p)
```

Visits a UnaryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitVariable

```java
R
visitVariable​(
VariableTree
node,

P
p)
```

Visits a VariableTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitWhileLoop

```java
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Visits a WhileLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitWildcard

```java
R
visitWildcard​(
WildcardTree
node,

P
p)
```

Visits a WildcardTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitModule

```java
R
visitModule​(
ModuleTree
node,

P
p)
```

Visits a ModuleTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitExports

```java
R
visitExports​(
ExportsTree
node,

P
p)
```

Visits an ExportsTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitOpens

```java
R
visitOpens​(
OpensTree
node,

P
p)
```

Visits an OpensTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitProvides

```java
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitRequires

```java
R
visitRequires​(
RequiresTree
node,

P
p)
```

Visits a RequiresTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUses

```java
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitOther

```java
R
visitOther​(
Tree
node,

P
p)
```

Visits an unknown type of Tree node.
This can occur if the language evolves and new kinds
of nodes are added to the

Tree

hierarchy.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### Method Detail

visitAnnotatedType

```java
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)
```

Visits an AnnotatedTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitAnnotatedType

R

visitAnnotatedType​(

AnnotatedTypeTree

node,

P

p)

Visits an AnnotatedTypeTree node.

visitAnnotation

```java
R
visitAnnotation​(
AnnotationTree
node,

P
p)
```

Visits an AnnotatedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitAnnotation

R

visitAnnotation​(

AnnotationTree

node,

P

p)

Visits an AnnotatedTree node.

visitMethodInvocation

```java
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)
```

Visits a MethodInvocationTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitMethodInvocation

R

visitMethodInvocation​(

MethodInvocationTree

node,

P

p)

Visits a MethodInvocationTree node.

visitAssert

```java
R
visitAssert​(
AssertTree
node,

P
p)
```

Visits an AssertTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitAssert

R

visitAssert​(

AssertTree

node,

P

p)

Visits an AssertTree node.

visitAssignment

```java
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Visits an AssignmentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitAssignment

R

visitAssignment​(

AssignmentTree

node,

P

p)

Visits an AssignmentTree node.

visitCompoundAssignment

```java
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Visits a CompoundAssignmentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitCompoundAssignment

R

visitCompoundAssignment​(

CompoundAssignmentTree

node,

P

p)

Visits a CompoundAssignmentTree node.

visitBinary

```java
R
visitBinary​(
BinaryTree
node,

P
p)
```

Visits a BinaryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitBinary

R

visitBinary​(

BinaryTree

node,

P

p)

Visits a BinaryTree node.

visitBlock

```java
R
visitBlock​(
BlockTree
node,

P
p)
```

Visits a BlockTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitBlock

R

visitBlock​(

BlockTree

node,

P

p)

Visits a BlockTree node.

visitBreak

```java
R
visitBreak​(
BreakTree
node,

P
p)
```

Visits a BreakTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitBreak

R

visitBreak​(

BreakTree

node,

P

p)

Visits a BreakTree node.

visitCase

```java
R
visitCase​(
CaseTree
node,

P
p)
```

Visits a CaseTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitCase

R

visitCase​(

CaseTree

node,

P

p)

Visits a CaseTree node.

visitCatch

```java
R
visitCatch​(
CatchTree
node,

P
p)
```

Visits a CatchTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitCatch

R

visitCatch​(

CatchTree

node,

P

p)

Visits a CatchTree node.

visitClass

```java
R
visitClass​(
ClassTree
node,

P
p)
```

Visits a ClassTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitClass

R

visitClass​(

ClassTree

node,

P

p)

Visits a ClassTree node.

visitConditionalExpression

```java
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Visits a ConditionalExpressionTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitConditionalExpression

R

visitConditionalExpression​(

ConditionalExpressionTree

node,

P

p)

Visits a ConditionalExpressionTree node.

visitContinue

```java
R
visitContinue​(
ContinueTree
node,

P
p)
```

Visits a ContinueTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitContinue

R

visitContinue​(

ContinueTree

node,

P

p)

Visits a ContinueTree node.

visitDoWhileLoop

```java
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Visits a DoWhileTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitDoWhileLoop

R

visitDoWhileLoop​(

DoWhileLoopTree

node,

P

p)

Visits a DoWhileTree node.

visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitErroneous

R

visitErroneous​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node.

visitExpressionStatement

```java
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Visits an ExpressionStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitExpressionStatement

R

visitExpressionStatement​(

ExpressionStatementTree

node,

P

p)

Visits an ExpressionStatementTree node.

visitEnhancedForLoop

```java
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)
```

Visits an EnhancedForLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitEnhancedForLoop

R

visitEnhancedForLoop​(

EnhancedForLoopTree

node,

P

p)

Visits an EnhancedForLoopTree node.

visitForLoop

```java
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Visits a ForLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitForLoop

R

visitForLoop​(

ForLoopTree

node,

P

p)

Visits a ForLoopTree node.

visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitIdentifier

R

visitIdentifier​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node.

visitIf

```java
R
visitIf​(
IfTree
node,

P
p)
```

Visits an IfTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitIf

R

visitIf​(

IfTree

node,

P

p)

Visits an IfTree node.

visitImport

```java
R
visitImport​(
ImportTree
node,

P
p)
```

Visits an ImportTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitImport

R

visitImport​(

ImportTree

node,

P

p)

Visits an ImportTree node.

visitArrayAccess

```java
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Visits an ArrayAccessTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitArrayAccess

R

visitArrayAccess​(

ArrayAccessTree

node,

P

p)

Visits an ArrayAccessTree node.

visitLabeledStatement

```java
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Visits a LabeledStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitLabeledStatement

R

visitLabeledStatement​(

LabeledStatementTree

node,

P

p)

Visits a LabeledStatementTree node.

visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits a LiteralTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitLiteral

R

visitLiteral​(

LiteralTree

node,

P

p)

Visits a LiteralTree node.

visitMethod

```java
R
visitMethod​(
MethodTree
node,

P
p)
```

Visits a MethodTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitMethod

R

visitMethod​(

MethodTree

node,

P

p)

Visits a MethodTree node.

visitModifiers

```java
R
visitModifiers​(
ModifiersTree
node,

P
p)
```

Visits a ModifiersTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitModifiers

R

visitModifiers​(

ModifiersTree

node,

P

p)

Visits a ModifiersTree node.

visitNewArray

```java
R
visitNewArray​(
NewArrayTree
node,

P
p)
```

Visits a NewArrayTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitNewArray

R

visitNewArray​(

NewArrayTree

node,

P

p)

Visits a NewArrayTree node.

visitNewClass

```java
R
visitNewClass​(
NewClassTree
node,

P
p)
```

Visits a NewClassTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitNewClass

R

visitNewClass​(

NewClassTree

node,

P

p)

Visits a NewClassTree node.

visitLambdaExpression

```java
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)
```

Visits a LambdaExpressionTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitLambdaExpression

R

visitLambdaExpression​(

LambdaExpressionTree

node,

P

p)

Visits a LambdaExpressionTree node.

visitPackage

```java
R
visitPackage​(
PackageTree
node,

P
p)
```

Visits a PackageTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitPackage

R

visitPackage​(

PackageTree

node,

P

p)

Visits a PackageTree node.

visitParenthesized

```java
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Visits a ParenthesizedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitParenthesized

R

visitParenthesized​(

ParenthesizedTree

node,

P

p)

Visits a ParenthesizedTree node.

visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitReturn

R

visitReturn​(

ReturnTree

node,

P

p)

Visits a ReturnTree node.

visitMemberSelect

```java
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Visits a MemberSelectTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitMemberSelect

R

visitMemberSelect​(

MemberSelectTree

node,

P

p)

Visits a MemberSelectTree node.

visitMemberReference

```java
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)
```

Visits a MemberReferenceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitMemberReference

R

visitMemberReference​(

MemberReferenceTree

node,

P

p)

Visits a MemberReferenceTree node.

visitEmptyStatement

```java
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Visits an EmptyStatementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitEmptyStatement

R

visitEmptyStatement​(

EmptyStatementTree

node,

P

p)

Visits an EmptyStatementTree node.

visitSwitch

```java
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Visits a SwitchTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitSwitch

R

visitSwitch​(

SwitchTree

node,

P

p)

Visits a SwitchTree node.

visitSynchronized

```java
R
visitSynchronized​(
SynchronizedTree
node,

P
p)
```

Visits a SynchronizedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitSynchronized

R

visitSynchronized​(

SynchronizedTree

node,

P

p)

Visits a SynchronizedTree node.

visitThrow

```java
R
visitThrow​(
ThrowTree
node,

P
p)
```

Visits a ThrowTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitThrow

R

visitThrow​(

ThrowTree

node,

P

p)

Visits a ThrowTree node.

visitCompilationUnit

```java
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Visits a CompilationUnitTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitCompilationUnit

R

visitCompilationUnit​(

CompilationUnitTree

node,

P

p)

Visits a CompilationUnitTree node.

visitTry

```java
R
visitTry​(
TryTree
node,

P
p)
```

Visits a TryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitTry

R

visitTry​(

TryTree

node,

P

p)

Visits a TryTree node.

visitParameterizedType

```java
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)
```

Visits a ParameterizedTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitParameterizedType

R

visitParameterizedType​(

ParameterizedTypeTree

node,

P

p)

Visits a ParameterizedTypeTree node.

visitUnionType

```java
R
visitUnionType​(
UnionTypeTree
node,

P
p)
```

Visits a UnionTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitUnionType

R

visitUnionType​(

UnionTypeTree

node,

P

p)

Visits a UnionTypeTree node.

visitIntersectionType

```java
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)
```

Visits an IntersectionTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitIntersectionType

R

visitIntersectionType​(

IntersectionTypeTree

node,

P

p)

Visits an IntersectionTypeTree node.

visitArrayType

```java
R
visitArrayType​(
ArrayTypeTree
node,

P
p)
```

Visits an ArrayTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitArrayType

R

visitArrayType​(

ArrayTypeTree

node,

P

p)

Visits an ArrayTypeTree node.

visitTypeCast

```java
R
visitTypeCast​(
TypeCastTree
node,

P
p)
```

Visits a TypeCastTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitTypeCast

R

visitTypeCast​(

TypeCastTree

node,

P

p)

Visits a TypeCastTree node.

visitPrimitiveType

```java
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)
```

Visits a PrimitiveTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitPrimitiveType

R

visitPrimitiveType​(

PrimitiveTypeTree

node,

P

p)

Visits a PrimitiveTypeTree node.

visitTypeParameter

```java
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)
```

Visits a TypeParameterTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitTypeParameter

R

visitTypeParameter​(

TypeParameterTree

node,

P

p)

Visits a TypeParameterTree node.

visitInstanceOf

```java
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Visits an InstanceOfTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitInstanceOf

R

visitInstanceOf​(

InstanceOfTree

node,

P

p)

Visits an InstanceOfTree node.

visitUnary

```java
R
visitUnary​(
UnaryTree
node,

P
p)
```

Visits a UnaryTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitUnary

R

visitUnary​(

UnaryTree

node,

P

p)

Visits a UnaryTree node.

visitVariable

```java
R
visitVariable​(
VariableTree
node,

P
p)
```

Visits a VariableTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitVariable

R

visitVariable​(

VariableTree

node,

P

p)

Visits a VariableTree node.

visitWhileLoop

```java
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Visits a WhileLoopTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitWhileLoop

R

visitWhileLoop​(

WhileLoopTree

node,

P

p)

Visits a WhileLoopTree node.

visitWildcard

```java
R
visitWildcard​(
WildcardTree
node,

P
p)
```

Visits a WildcardTypeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitWildcard

R

visitWildcard​(

WildcardTree

node,

P

p)

Visits a WildcardTypeTree node.

visitModule

```java
R
visitModule​(
ModuleTree
node,

P
p)
```

Visits a ModuleTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitModule

R

visitModule​(

ModuleTree

node,

P

p)

Visits a ModuleTree node.

visitExports

```java
R
visitExports​(
ExportsTree
node,

P
p)
```

Visits an ExportsTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitExports

R

visitExports​(

ExportsTree

node,

P

p)

Visits an ExportsTree node.

visitOpens

```java
R
visitOpens​(
OpensTree
node,

P
p)
```

Visits an OpensTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitOpens

R

visitOpens​(

OpensTree

node,

P

p)

Visits an OpensTree node.

visitProvides

```java
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitProvides

R

visitProvides​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node.

visitRequires

```java
R
visitRequires​(
RequiresTree
node,

P
p)
```

Visits a RequiresTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitRequires

R

visitRequires​(

RequiresTree

node,

P

p)

Visits a RequiresTree node.

visitUses

```java
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitUses

R

visitUses​(

UsesTree

node,

P

p)

Visits a UsesTree node.

visitOther

```java
R
visitOther​(
Tree
node,

P
p)
```

Visits an unknown type of Tree node.
This can occur if the language evolves and new kinds
of nodes are added to the

Tree

hierarchy.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitOther

R

visitOther​(

Tree

node,

P

p)

Visits an unknown type of Tree node.
This can occur if the language evolves and new kinds
of nodes are added to the

Tree

hierarchy.

---

