# Class SimpleTreeVisitor<R,​P>

**Source:** `jdk.compiler\com\sun\source\util\SimpleTreeVisitor.html`

### Class Description

```java
public class
SimpleTreeVisitor<R,​P>

extends
Object

implements
TreeVisitor
<R,​P>
```

A simple visitor for tree nodes.

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

#### protected final
R
DEFAULT_VALUE

The default value, returned by the

default action

.

---

### Constructor Details

#### protected SimpleTreeVisitor()

Creates a visitor, with a DEFAULT_VALUE of

null

.

---

#### protected SimpleTreeVisitor​(
R
defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:**
- defaultValue

- the default value to be returned by the default action.

---

### Method Details

#### protected
R
defaultAction​(
Tree
node,

P
p)

The default action, used by all visit methods that are not overridden.

**Parameters:**
- node

- the node being visited
- p

- the parameter value passed to the visit method

**Returns:**
- the result value to be returned from the visit method

---

#### public final
R
visit​(
Tree
node,

P
p)

Invokes the appropriate visit method specific to the type of the node.

**Parameters:**
- node

- the node on which to dispatch
- p

- a parameter to be passed to the appropriate visit method

**Returns:**
- the value returns from the appropriate visit method

---

#### public final
R
visit​(
Iterable
<? extends
Tree
> nodes,

P
p)

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:**
- nodes

- the nodes on which to dispatch
- p

- a parameter value to be passed to each appropriate visit method

**Returns:**
- the value return from the last of the visit methods, or null
if none were called.

---

#### public
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)

Visits a CompilationUnitTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitCompilationUnit

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitPackage​(
PackageTree
node,

P
p)

Visits a PackageTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitPackage

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitImport​(
ImportTree
node,

P
p)

Visits an ImportTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitImport

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitClass​(
ClassTree
node,

P
p)

Visits a ClassTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitClass

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitMethod​(
MethodTree
node,

P
p)

Visits a MethodTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitMethod

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitVariable​(
VariableTree
node,

P
p)

Visits a VariableTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitVariable

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)

Visits an EmptyStatementTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitEmptyStatement

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitBlock​(
BlockTree
node,

P
p)

Visits a BlockTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitBlock

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)

Visits a DoWhileTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitDoWhileLoop

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)

Visits a WhileLoopTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitWhileLoop

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitForLoop​(
ForLoopTree
node,

P
p)

Visits a ForLoopTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitForLoop

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)

Visits an EnhancedForLoopTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitEnhancedForLoop

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)

Visits a LabeledStatementTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitLabeledStatement

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitSwitch​(
SwitchTree
node,

P
p)

Visits a SwitchTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitSwitch

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitCase​(
CaseTree
node,

P
p)

Visits a CaseTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitCase

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitSynchronized​(
SynchronizedTree
node,

P
p)

Visits a SynchronizedTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitSynchronized

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitTry​(
TryTree
node,

P
p)

Visits a TryTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitTry

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitCatch​(
CatchTree
node,

P
p)

Visits a CatchTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitCatch

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)

Visits a ConditionalExpressionTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitConditionalExpression

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitIf​(
IfTree
node,

P
p)

Visits an IfTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitIf

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)

Visits an ExpressionStatementTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitExpressionStatement

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitBreak​(
BreakTree
node,

P
p)

Visits a BreakTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitBreak

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitContinue​(
ContinueTree
node,

P
p)

Visits a ContinueTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitContinue

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitReturn​(
ReturnTree
node,

P
p)

Visits a ReturnTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitReturn

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitThrow​(
ThrowTree
node,

P
p)

Visits a ThrowTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitThrow

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitAssert​(
AssertTree
node,

P
p)

Visits an AssertTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitAssert

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)

Visits a MethodInvocationTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitMethodInvocation

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitNewClass​(
NewClassTree
node,

P
p)

Visits a NewClassTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitNewClass

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitNewArray​(
NewArrayTree
node,

P
p)

Visits a NewArrayTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitNewArray

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)

Visits a LambdaExpressionTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitLambdaExpression

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)

Visits a ParenthesizedTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitParenthesized

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitAssignment​(
AssignmentTree
node,

P
p)

Visits an AssignmentTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitAssignment

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)

Visits a CompoundAssignmentTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitCompoundAssignment

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitUnary​(
UnaryTree
node,

P
p)

Visits a UnaryTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitUnary

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitBinary​(
BinaryTree
node,

P
p)

Visits a BinaryTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitBinary

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitTypeCast​(
TypeCastTree
node,

P
p)

Visits a TypeCastTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitTypeCast

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)

Visits an InstanceOfTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitInstanceOf

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)

Visits an ArrayAccessTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitArrayAccess

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)

Visits a MemberSelectTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitMemberSelect

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)

Visits a MemberReferenceTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitMemberReference

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitIdentifier​(
IdentifierTree
node,

P
p)

Visits an IdentifierTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitIdentifier

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitLiteral​(
LiteralTree
node,

P
p)

Visits a LiteralTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitLiteral

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)

Visits a PrimitiveTypeTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitPrimitiveType

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitArrayType​(
ArrayTypeTree
node,

P
p)

Visits an ArrayTypeTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitArrayType

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)

Visits a ParameterizedTypeTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitParameterizedType

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitUnionType​(
UnionTypeTree
node,

P
p)

Visits a UnionTypeTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitUnionType

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)

Visits an IntersectionTypeTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitIntersectionType

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)

Visits a TypeParameterTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitTypeParameter

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitWildcard​(
WildcardTree
node,

P
p)

Visits a WildcardTypeTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitWildcard

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitModifiers​(
ModifiersTree
node,

P
p)

Visits a ModifiersTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitModifiers

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitAnnotation​(
AnnotationTree
node,

P
p)

Visits an AnnotatedTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitAnnotation

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)

Visits an AnnotatedTypeTree node. This implementation calls

defaultAction

.

**Specified by:**
- visitAnnotatedType

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

#### public
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

hierarchy. This implementation calls

defaultAction

.

**Specified by:**
- visitOther

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of

defaultAction

---

### Additional Sections

#### Class SimpleTreeVisitor<R,​P>

java.lang.Object

- com.sun.source.util.SimpleTreeVisitor<R,​P>

com.sun.source.util.SimpleTreeVisitor<R,​P>

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

**All Implemented Interfaces:** TreeVisitor

<R,​P>

```java
public class
SimpleTreeVisitor<R,​P>

extends
Object

implements
TreeVisitor
<R,​P>
```

A simple visitor for tree nodes.

**Since:** 1.6

public class

SimpleTreeVisitor<R,​P>

extends

Object

implements

TreeVisitor

<R,​P>

A simple visitor for tree nodes.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

The default value, returned by the

default action

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleTreeVisitor

()

Creates a visitor, with a DEFAULT_VALUE of

null

.

protected

SimpleTreeVisitor

​(

R

defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

R

defaultAction

​(

Tree

node,

P

p)

The default action, used by all visit methods that are not overridden.

R

visit

​(

Tree

node,

P

p)

Invokes the appropriate visit method specific to the type of the node.

R

visit

​(

Iterable

<? extends

Tree

> nodes,

P

p)

Invokes the appropriate visit method on each of a sequence of nodes.

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

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface com.sun.source.tree.

TreeVisitor

visitErroneous

,

visitExports

,

visitModule

,

visitOpens

,

visitProvides

,

visitRequires

,

visitUses

Field Summary

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

The default value, returned by the

default action

.

---

#### Field Summary

The default value, returned by the

default action

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleTreeVisitor

()

Creates a visitor, with a DEFAULT_VALUE of

null

.

protected

SimpleTreeVisitor

​(

R

defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

---

#### Constructor Summary

Creates a visitor, with a DEFAULT_VALUE of

null

.

Creates a visitor, with a specified DEFAULT_VALUE.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

R

defaultAction

​(

Tree

node,

P

p)

The default action, used by all visit methods that are not overridden.

R

visit

​(

Tree

node,

P

p)

Invokes the appropriate visit method specific to the type of the node.

R

visit

​(

Iterable

<? extends

Tree

> nodes,

P

p)

Invokes the appropriate visit method on each of a sequence of nodes.

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

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface com.sun.source.tree.

TreeVisitor

visitErroneous

,

visitExports

,

visitModule

,

visitOpens

,

visitProvides

,

visitRequires

,

visitUses

---

#### Method Summary

The default action, used by all visit methods that are not overridden.

Invokes the appropriate visit method specific to the type of the node.

Invokes the appropriate visit method on each of a sequence of nodes.

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

Visits a NewArrayTree node.

Visits a NewClassTree node.

Visits an unknown type of Tree node.

Visits a PackageTree node.

Visits a ParameterizedTypeTree node.

Visits a ParenthesizedTree node.

Visits a PrimitiveTypeTree node.

Visits a ReturnTree node.

Visits a SwitchTree node.

Visits a SynchronizedTree node.

Visits a ThrowTree node.

Visits a TryTree node.

Visits a TypeCastTree node.

Visits a TypeParameterTree node.

Visits a UnaryTree node.

Visits a UnionTypeTree node.

Visits a VariableTree node.

Visits a WhileLoopTree node.

Visits a WildcardTypeTree node.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface com.sun.source.tree.

TreeVisitor

visitErroneous

,

visitExports

,

visitModule

,

visitOpens

,

visitProvides

,

visitRequires

,

visitUses

---

#### Methods declared in interface com.sun.source.tree. TreeVisitor

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The default value, returned by the

default action

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleTreeVisitor

```java
protected SimpleTreeVisitor()
```

Creates a visitor, with a DEFAULT_VALUE of

null

.

- SimpleTreeVisitor

```java
protected SimpleTreeVisitor​(
R
defaultValue)
```

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:** defaultValue

- the default value to be returned by the default action.

============ METHOD DETAIL ==========

- Method Detail

- defaultAction

```java
protected
R
defaultAction​(
Tree
node,

P
p)
```

The default action, used by all visit methods that are not overridden.

**Parameters:** node

- the node being visited
**Parameters:** p

- the parameter value passed to the visit method
**Returns:** the result value to be returned from the visit method

- visit

```java
public final
R
visit​(
Tree
node,

P
p)
```

Invokes the appropriate visit method specific to the type of the node.

**Parameters:** node

- the node on which to dispatch
**Parameters:** p

- a parameter to be passed to the appropriate visit method
**Returns:** the value returns from the appropriate visit method

- visit

```java
public final
R
visit​(
Iterable
<? extends
Tree
> nodes,

P
p)
```

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:** nodes

- the nodes on which to dispatch
**Parameters:** p

- a parameter value to be passed to each appropriate visit method
**Returns:** the value return from the last of the visit methods, or null
if none were called.

- visitCompilationUnit

```java
public
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Visits a CompilationUnitTree node. This implementation calls

defaultAction

.

**Specified by:** visitCompilationUnit

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitPackage

```java
public
R
visitPackage​(
PackageTree
node,

P
p)
```

Visits a PackageTree node. This implementation calls

defaultAction

.

**Specified by:** visitPackage

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitImport

```java
public
R
visitImport​(
ImportTree
node,

P
p)
```

Visits an ImportTree node. This implementation calls

defaultAction

.

**Specified by:** visitImport

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitClass

```java
public
R
visitClass​(
ClassTree
node,

P
p)
```

Visits a ClassTree node. This implementation calls

defaultAction

.

**Specified by:** visitClass

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMethod

```java
public
R
visitMethod​(
MethodTree
node,

P
p)
```

Visits a MethodTree node. This implementation calls

defaultAction

.

**Specified by:** visitMethod

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitVariable

```java
public
R
visitVariable​(
VariableTree
node,

P
p)
```

Visits a VariableTree node. This implementation calls

defaultAction

.

**Specified by:** visitVariable

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitEmptyStatement

```java
public
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Visits an EmptyStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitEmptyStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitBlock

```java
public
R
visitBlock​(
BlockTree
node,

P
p)
```

Visits a BlockTree node. This implementation calls

defaultAction

.

**Specified by:** visitBlock

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitDoWhileLoop

```java
public
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Visits a DoWhileTree node. This implementation calls

defaultAction

.

**Specified by:** visitDoWhileLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitWhileLoop

```java
public
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Visits a WhileLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitWhileLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitForLoop

```java
public
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Visits a ForLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitForLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitEnhancedForLoop

```java
public
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)
```

Visits an EnhancedForLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitEnhancedForLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitLabeledStatement

```java
public
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Visits a LabeledStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitLabeledStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitSwitch

```java
public
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Visits a SwitchTree node. This implementation calls

defaultAction

.

**Specified by:** visitSwitch

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitCase

```java
public
R
visitCase​(
CaseTree
node,

P
p)
```

Visits a CaseTree node. This implementation calls

defaultAction

.

**Specified by:** visitCase

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitSynchronized

```java
public
R
visitSynchronized​(
SynchronizedTree
node,

P
p)
```

Visits a SynchronizedTree node. This implementation calls

defaultAction

.

**Specified by:** visitSynchronized

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitTry

```java
public
R
visitTry​(
TryTree
node,

P
p)
```

Visits a TryTree node. This implementation calls

defaultAction

.

**Specified by:** visitTry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitCatch

```java
public
R
visitCatch​(
CatchTree
node,

P
p)
```

Visits a CatchTree node. This implementation calls

defaultAction

.

**Specified by:** visitCatch

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitConditionalExpression

```java
public
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Visits a ConditionalExpressionTree node. This implementation calls

defaultAction

.

**Specified by:** visitConditionalExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitIf

```java
public
R
visitIf​(
IfTree
node,

P
p)
```

Visits an IfTree node. This implementation calls

defaultAction

.

**Specified by:** visitIf

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitExpressionStatement

```java
public
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Visits an ExpressionStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitExpressionStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitBreak

```java
public
R
visitBreak​(
BreakTree
node,

P
p)
```

Visits a BreakTree node. This implementation calls

defaultAction

.

**Specified by:** visitBreak

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitContinue

```java
public
R
visitContinue​(
ContinueTree
node,

P
p)
```

Visits a ContinueTree node. This implementation calls

defaultAction

.

**Specified by:** visitContinue

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitReturn

```java
public
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node. This implementation calls

defaultAction

.

**Specified by:** visitReturn

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitThrow

```java
public
R
visitThrow​(
ThrowTree
node,

P
p)
```

Visits a ThrowTree node. This implementation calls

defaultAction

.

**Specified by:** visitThrow

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAssert

```java
public
R
visitAssert​(
AssertTree
node,

P
p)
```

Visits an AssertTree node. This implementation calls

defaultAction

.

**Specified by:** visitAssert

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMethodInvocation

```java
public
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)
```

Visits a MethodInvocationTree node. This implementation calls

defaultAction

.

**Specified by:** visitMethodInvocation

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitNewClass

```java
public
R
visitNewClass​(
NewClassTree
node,

P
p)
```

Visits a NewClassTree node. This implementation calls

defaultAction

.

**Specified by:** visitNewClass

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitNewArray

```java
public
R
visitNewArray​(
NewArrayTree
node,

P
p)
```

Visits a NewArrayTree node. This implementation calls

defaultAction

.

**Specified by:** visitNewArray

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitLambdaExpression

```java
public
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)
```

Visits a LambdaExpressionTree node. This implementation calls

defaultAction

.

**Specified by:** visitLambdaExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitParenthesized

```java
public
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Visits a ParenthesizedTree node. This implementation calls

defaultAction

.

**Specified by:** visitParenthesized

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAssignment

```java
public
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Visits an AssignmentTree node. This implementation calls

defaultAction

.

**Specified by:** visitAssignment

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitCompoundAssignment

```java
public
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Visits a CompoundAssignmentTree node. This implementation calls

defaultAction

.

**Specified by:** visitCompoundAssignment

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitUnary

```java
public
R
visitUnary​(
UnaryTree
node,

P
p)
```

Visits a UnaryTree node. This implementation calls

defaultAction

.

**Specified by:** visitUnary

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitBinary

```java
public
R
visitBinary​(
BinaryTree
node,

P
p)
```

Visits a BinaryTree node. This implementation calls

defaultAction

.

**Specified by:** visitBinary

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitTypeCast

```java
public
R
visitTypeCast​(
TypeCastTree
node,

P
p)
```

Visits a TypeCastTree node. This implementation calls

defaultAction

.

**Specified by:** visitTypeCast

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitInstanceOf

```java
public
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Visits an InstanceOfTree node. This implementation calls

defaultAction

.

**Specified by:** visitInstanceOf

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitArrayAccess

```java
public
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Visits an ArrayAccessTree node. This implementation calls

defaultAction

.

**Specified by:** visitArrayAccess

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMemberSelect

```java
public
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Visits a MemberSelectTree node. This implementation calls

defaultAction

.

**Specified by:** visitMemberSelect

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMemberReference

```java
public
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)
```

Visits a MemberReferenceTree node. This implementation calls

defaultAction

.

**Specified by:** visitMemberReference

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitIdentifier

```java
public
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node. This implementation calls

defaultAction

.

**Specified by:** visitIdentifier

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitLiteral

```java
public
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits a LiteralTree node. This implementation calls

defaultAction

.

**Specified by:** visitLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitPrimitiveType

```java
public
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)
```

Visits a PrimitiveTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitPrimitiveType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitArrayType

```java
public
R
visitArrayType​(
ArrayTypeTree
node,

P
p)
```

Visits an ArrayTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitArrayType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitParameterizedType

```java
public
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)
```

Visits a ParameterizedTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitParameterizedType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitUnionType

```java
public
R
visitUnionType​(
UnionTypeTree
node,

P
p)
```

Visits a UnionTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitUnionType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitIntersectionType

```java
public
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)
```

Visits an IntersectionTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitIntersectionType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)
```

Visits a TypeParameterTree node. This implementation calls

defaultAction

.

**Specified by:** visitTypeParameter

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitWildcard

```java
public
R
visitWildcard​(
WildcardTree
node,

P
p)
```

Visits a WildcardTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitWildcard

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitModifiers

```java
public
R
visitModifiers​(
ModifiersTree
node,

P
p)
```

Visits a ModifiersTree node. This implementation calls

defaultAction

.

**Specified by:** visitModifiers

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAnnotation

```java
public
R
visitAnnotation​(
AnnotationTree
node,

P
p)
```

Visits an AnnotatedTree node. This implementation calls

defaultAction

.

**Specified by:** visitAnnotation

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAnnotatedType

```java
public
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)
```

Visits an AnnotatedTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitAnnotatedType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitOther

```java
public
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

hierarchy. This implementation calls

defaultAction

.

**Specified by:** visitOther

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The default value, returned by the

default action

.

---

#### Field Detail

DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The default value, returned by the

default action

.

---

#### DEFAULT_VALUE

protected final

R

DEFAULT_VALUE

The default value, returned by the

default action

.

Constructor Detail

- SimpleTreeVisitor

```java
protected SimpleTreeVisitor()
```

Creates a visitor, with a DEFAULT_VALUE of

null

.

- SimpleTreeVisitor

```java
protected SimpleTreeVisitor​(
R
defaultValue)
```

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:** defaultValue

- the default value to be returned by the default action.

---

#### Constructor Detail

SimpleTreeVisitor

```java
protected SimpleTreeVisitor()
```

Creates a visitor, with a DEFAULT_VALUE of

null

.

---

#### SimpleTreeVisitor

protected SimpleTreeVisitor()

Creates a visitor, with a DEFAULT_VALUE of

null

.

SimpleTreeVisitor

```java
protected SimpleTreeVisitor​(
R
defaultValue)
```

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:** defaultValue

- the default value to be returned by the default action.

---

#### SimpleTreeVisitor

protected SimpleTreeVisitor​(

R

defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

Method Detail

- defaultAction

```java
protected
R
defaultAction​(
Tree
node,

P
p)
```

The default action, used by all visit methods that are not overridden.

**Parameters:** node

- the node being visited
**Parameters:** p

- the parameter value passed to the visit method
**Returns:** the result value to be returned from the visit method

- visit

```java
public final
R
visit​(
Tree
node,

P
p)
```

Invokes the appropriate visit method specific to the type of the node.

**Parameters:** node

- the node on which to dispatch
**Parameters:** p

- a parameter to be passed to the appropriate visit method
**Returns:** the value returns from the appropriate visit method

- visit

```java
public final
R
visit​(
Iterable
<? extends
Tree
> nodes,

P
p)
```

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:** nodes

- the nodes on which to dispatch
**Parameters:** p

- a parameter value to be passed to each appropriate visit method
**Returns:** the value return from the last of the visit methods, or null
if none were called.

- visitCompilationUnit

```java
public
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Visits a CompilationUnitTree node. This implementation calls

defaultAction

.

**Specified by:** visitCompilationUnit

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitPackage

```java
public
R
visitPackage​(
PackageTree
node,

P
p)
```

Visits a PackageTree node. This implementation calls

defaultAction

.

**Specified by:** visitPackage

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitImport

```java
public
R
visitImport​(
ImportTree
node,

P
p)
```

Visits an ImportTree node. This implementation calls

defaultAction

.

**Specified by:** visitImport

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitClass

```java
public
R
visitClass​(
ClassTree
node,

P
p)
```

Visits a ClassTree node. This implementation calls

defaultAction

.

**Specified by:** visitClass

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMethod

```java
public
R
visitMethod​(
MethodTree
node,

P
p)
```

Visits a MethodTree node. This implementation calls

defaultAction

.

**Specified by:** visitMethod

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitVariable

```java
public
R
visitVariable​(
VariableTree
node,

P
p)
```

Visits a VariableTree node. This implementation calls

defaultAction

.

**Specified by:** visitVariable

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitEmptyStatement

```java
public
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Visits an EmptyStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitEmptyStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitBlock

```java
public
R
visitBlock​(
BlockTree
node,

P
p)
```

Visits a BlockTree node. This implementation calls

defaultAction

.

**Specified by:** visitBlock

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitDoWhileLoop

```java
public
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Visits a DoWhileTree node. This implementation calls

defaultAction

.

**Specified by:** visitDoWhileLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitWhileLoop

```java
public
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Visits a WhileLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitWhileLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitForLoop

```java
public
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Visits a ForLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitForLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitEnhancedForLoop

```java
public
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)
```

Visits an EnhancedForLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitEnhancedForLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitLabeledStatement

```java
public
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Visits a LabeledStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitLabeledStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitSwitch

```java
public
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Visits a SwitchTree node. This implementation calls

defaultAction

.

**Specified by:** visitSwitch

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitCase

```java
public
R
visitCase​(
CaseTree
node,

P
p)
```

Visits a CaseTree node. This implementation calls

defaultAction

.

**Specified by:** visitCase

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitSynchronized

```java
public
R
visitSynchronized​(
SynchronizedTree
node,

P
p)
```

Visits a SynchronizedTree node. This implementation calls

defaultAction

.

**Specified by:** visitSynchronized

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitTry

```java
public
R
visitTry​(
TryTree
node,

P
p)
```

Visits a TryTree node. This implementation calls

defaultAction

.

**Specified by:** visitTry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitCatch

```java
public
R
visitCatch​(
CatchTree
node,

P
p)
```

Visits a CatchTree node. This implementation calls

defaultAction

.

**Specified by:** visitCatch

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitConditionalExpression

```java
public
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Visits a ConditionalExpressionTree node. This implementation calls

defaultAction

.

**Specified by:** visitConditionalExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitIf

```java
public
R
visitIf​(
IfTree
node,

P
p)
```

Visits an IfTree node. This implementation calls

defaultAction

.

**Specified by:** visitIf

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitExpressionStatement

```java
public
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Visits an ExpressionStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitExpressionStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitBreak

```java
public
R
visitBreak​(
BreakTree
node,

P
p)
```

Visits a BreakTree node. This implementation calls

defaultAction

.

**Specified by:** visitBreak

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitContinue

```java
public
R
visitContinue​(
ContinueTree
node,

P
p)
```

Visits a ContinueTree node. This implementation calls

defaultAction

.

**Specified by:** visitContinue

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitReturn

```java
public
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node. This implementation calls

defaultAction

.

**Specified by:** visitReturn

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitThrow

```java
public
R
visitThrow​(
ThrowTree
node,

P
p)
```

Visits a ThrowTree node. This implementation calls

defaultAction

.

**Specified by:** visitThrow

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAssert

```java
public
R
visitAssert​(
AssertTree
node,

P
p)
```

Visits an AssertTree node. This implementation calls

defaultAction

.

**Specified by:** visitAssert

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMethodInvocation

```java
public
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)
```

Visits a MethodInvocationTree node. This implementation calls

defaultAction

.

**Specified by:** visitMethodInvocation

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitNewClass

```java
public
R
visitNewClass​(
NewClassTree
node,

P
p)
```

Visits a NewClassTree node. This implementation calls

defaultAction

.

**Specified by:** visitNewClass

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitNewArray

```java
public
R
visitNewArray​(
NewArrayTree
node,

P
p)
```

Visits a NewArrayTree node. This implementation calls

defaultAction

.

**Specified by:** visitNewArray

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitLambdaExpression

```java
public
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)
```

Visits a LambdaExpressionTree node. This implementation calls

defaultAction

.

**Specified by:** visitLambdaExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitParenthesized

```java
public
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Visits a ParenthesizedTree node. This implementation calls

defaultAction

.

**Specified by:** visitParenthesized

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAssignment

```java
public
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Visits an AssignmentTree node. This implementation calls

defaultAction

.

**Specified by:** visitAssignment

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitCompoundAssignment

```java
public
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Visits a CompoundAssignmentTree node. This implementation calls

defaultAction

.

**Specified by:** visitCompoundAssignment

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitUnary

```java
public
R
visitUnary​(
UnaryTree
node,

P
p)
```

Visits a UnaryTree node. This implementation calls

defaultAction

.

**Specified by:** visitUnary

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitBinary

```java
public
R
visitBinary​(
BinaryTree
node,

P
p)
```

Visits a BinaryTree node. This implementation calls

defaultAction

.

**Specified by:** visitBinary

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitTypeCast

```java
public
R
visitTypeCast​(
TypeCastTree
node,

P
p)
```

Visits a TypeCastTree node. This implementation calls

defaultAction

.

**Specified by:** visitTypeCast

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitInstanceOf

```java
public
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Visits an InstanceOfTree node. This implementation calls

defaultAction

.

**Specified by:** visitInstanceOf

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitArrayAccess

```java
public
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Visits an ArrayAccessTree node. This implementation calls

defaultAction

.

**Specified by:** visitArrayAccess

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMemberSelect

```java
public
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Visits a MemberSelectTree node. This implementation calls

defaultAction

.

**Specified by:** visitMemberSelect

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitMemberReference

```java
public
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)
```

Visits a MemberReferenceTree node. This implementation calls

defaultAction

.

**Specified by:** visitMemberReference

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitIdentifier

```java
public
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node. This implementation calls

defaultAction

.

**Specified by:** visitIdentifier

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitLiteral

```java
public
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits a LiteralTree node. This implementation calls

defaultAction

.

**Specified by:** visitLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitPrimitiveType

```java
public
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)
```

Visits a PrimitiveTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitPrimitiveType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitArrayType

```java
public
R
visitArrayType​(
ArrayTypeTree
node,

P
p)
```

Visits an ArrayTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitArrayType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitParameterizedType

```java
public
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)
```

Visits a ParameterizedTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitParameterizedType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitUnionType

```java
public
R
visitUnionType​(
UnionTypeTree
node,

P
p)
```

Visits a UnionTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitUnionType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitIntersectionType

```java
public
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)
```

Visits an IntersectionTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitIntersectionType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)
```

Visits a TypeParameterTree node. This implementation calls

defaultAction

.

**Specified by:** visitTypeParameter

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitWildcard

```java
public
R
visitWildcard​(
WildcardTree
node,

P
p)
```

Visits a WildcardTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitWildcard

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitModifiers

```java
public
R
visitModifiers​(
ModifiersTree
node,

P
p)
```

Visits a ModifiersTree node. This implementation calls

defaultAction

.

**Specified by:** visitModifiers

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAnnotation

```java
public
R
visitAnnotation​(
AnnotationTree
node,

P
p)
```

Visits an AnnotatedTree node. This implementation calls

defaultAction

.

**Specified by:** visitAnnotation

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitAnnotatedType

```java
public
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)
```

Visits an AnnotatedTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitAnnotatedType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

- visitOther

```java
public
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

hierarchy. This implementation calls

defaultAction

.

**Specified by:** visitOther

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### Method Detail

defaultAction

```java
protected
R
defaultAction​(
Tree
node,

P
p)
```

The default action, used by all visit methods that are not overridden.

**Parameters:** node

- the node being visited
**Parameters:** p

- the parameter value passed to the visit method
**Returns:** the result value to be returned from the visit method

---

#### defaultAction

protected

R

defaultAction​(

Tree

node,

P

p)

The default action, used by all visit methods that are not overridden.

visit

```java
public final
R
visit​(
Tree
node,

P
p)
```

Invokes the appropriate visit method specific to the type of the node.

**Parameters:** node

- the node on which to dispatch
**Parameters:** p

- a parameter to be passed to the appropriate visit method
**Returns:** the value returns from the appropriate visit method

---

#### visit

public final

R

visit​(

Tree

node,

P

p)

Invokes the appropriate visit method specific to the type of the node.

visit

```java
public final
R
visit​(
Iterable
<? extends
Tree
> nodes,

P
p)
```

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:** nodes

- the nodes on which to dispatch
**Parameters:** p

- a parameter value to be passed to each appropriate visit method
**Returns:** the value return from the last of the visit methods, or null
if none were called.

---

#### visit

public final

R

visit​(

Iterable

<? extends

Tree

> nodes,

P

p)

Invokes the appropriate visit method on each of a sequence of nodes.

visitCompilationUnit

```java
public
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)
```

Visits a CompilationUnitTree node. This implementation calls

defaultAction

.

**Specified by:** visitCompilationUnit

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitCompilationUnit

public

R

visitCompilationUnit​(

CompilationUnitTree

node,

P

p)

Visits a CompilationUnitTree node. This implementation calls

defaultAction

.

visitPackage

```java
public
R
visitPackage​(
PackageTree
node,

P
p)
```

Visits a PackageTree node. This implementation calls

defaultAction

.

**Specified by:** visitPackage

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitPackage

public

R

visitPackage​(

PackageTree

node,

P

p)

Visits a PackageTree node. This implementation calls

defaultAction

.

visitImport

```java
public
R
visitImport​(
ImportTree
node,

P
p)
```

Visits an ImportTree node. This implementation calls

defaultAction

.

**Specified by:** visitImport

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitImport

public

R

visitImport​(

ImportTree

node,

P

p)

Visits an ImportTree node. This implementation calls

defaultAction

.

visitClass

```java
public
R
visitClass​(
ClassTree
node,

P
p)
```

Visits a ClassTree node. This implementation calls

defaultAction

.

**Specified by:** visitClass

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitClass

public

R

visitClass​(

ClassTree

node,

P

p)

Visits a ClassTree node. This implementation calls

defaultAction

.

visitMethod

```java
public
R
visitMethod​(
MethodTree
node,

P
p)
```

Visits a MethodTree node. This implementation calls

defaultAction

.

**Specified by:** visitMethod

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitMethod

public

R

visitMethod​(

MethodTree

node,

P

p)

Visits a MethodTree node. This implementation calls

defaultAction

.

visitVariable

```java
public
R
visitVariable​(
VariableTree
node,

P
p)
```

Visits a VariableTree node. This implementation calls

defaultAction

.

**Specified by:** visitVariable

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitVariable

public

R

visitVariable​(

VariableTree

node,

P

p)

Visits a VariableTree node. This implementation calls

defaultAction

.

visitEmptyStatement

```java
public
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)
```

Visits an EmptyStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitEmptyStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitEmptyStatement

public

R

visitEmptyStatement​(

EmptyStatementTree

node,

P

p)

Visits an EmptyStatementTree node. This implementation calls

defaultAction

.

visitBlock

```java
public
R
visitBlock​(
BlockTree
node,

P
p)
```

Visits a BlockTree node. This implementation calls

defaultAction

.

**Specified by:** visitBlock

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitBlock

public

R

visitBlock​(

BlockTree

node,

P

p)

Visits a BlockTree node. This implementation calls

defaultAction

.

visitDoWhileLoop

```java
public
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)
```

Visits a DoWhileTree node. This implementation calls

defaultAction

.

**Specified by:** visitDoWhileLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitDoWhileLoop

public

R

visitDoWhileLoop​(

DoWhileLoopTree

node,

P

p)

Visits a DoWhileTree node. This implementation calls

defaultAction

.

visitWhileLoop

```java
public
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)
```

Visits a WhileLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitWhileLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitWhileLoop

public

R

visitWhileLoop​(

WhileLoopTree

node,

P

p)

Visits a WhileLoopTree node. This implementation calls

defaultAction

.

visitForLoop

```java
public
R
visitForLoop​(
ForLoopTree
node,

P
p)
```

Visits a ForLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitForLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitForLoop

public

R

visitForLoop​(

ForLoopTree

node,

P

p)

Visits a ForLoopTree node. This implementation calls

defaultAction

.

visitEnhancedForLoop

```java
public
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)
```

Visits an EnhancedForLoopTree node. This implementation calls

defaultAction

.

**Specified by:** visitEnhancedForLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitEnhancedForLoop

public

R

visitEnhancedForLoop​(

EnhancedForLoopTree

node,

P

p)

Visits an EnhancedForLoopTree node. This implementation calls

defaultAction

.

visitLabeledStatement

```java
public
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)
```

Visits a LabeledStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitLabeledStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitLabeledStatement

public

R

visitLabeledStatement​(

LabeledStatementTree

node,

P

p)

Visits a LabeledStatementTree node. This implementation calls

defaultAction

.

visitSwitch

```java
public
R
visitSwitch​(
SwitchTree
node,

P
p)
```

Visits a SwitchTree node. This implementation calls

defaultAction

.

**Specified by:** visitSwitch

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitSwitch

public

R

visitSwitch​(

SwitchTree

node,

P

p)

Visits a SwitchTree node. This implementation calls

defaultAction

.

visitCase

```java
public
R
visitCase​(
CaseTree
node,

P
p)
```

Visits a CaseTree node. This implementation calls

defaultAction

.

**Specified by:** visitCase

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitCase

public

R

visitCase​(

CaseTree

node,

P

p)

Visits a CaseTree node. This implementation calls

defaultAction

.

visitSynchronized

```java
public
R
visitSynchronized​(
SynchronizedTree
node,

P
p)
```

Visits a SynchronizedTree node. This implementation calls

defaultAction

.

**Specified by:** visitSynchronized

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitSynchronized

public

R

visitSynchronized​(

SynchronizedTree

node,

P

p)

Visits a SynchronizedTree node. This implementation calls

defaultAction

.

visitTry

```java
public
R
visitTry​(
TryTree
node,

P
p)
```

Visits a TryTree node. This implementation calls

defaultAction

.

**Specified by:** visitTry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitTry

public

R

visitTry​(

TryTree

node,

P

p)

Visits a TryTree node. This implementation calls

defaultAction

.

visitCatch

```java
public
R
visitCatch​(
CatchTree
node,

P
p)
```

Visits a CatchTree node. This implementation calls

defaultAction

.

**Specified by:** visitCatch

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitCatch

public

R

visitCatch​(

CatchTree

node,

P

p)

Visits a CatchTree node. This implementation calls

defaultAction

.

visitConditionalExpression

```java
public
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)
```

Visits a ConditionalExpressionTree node. This implementation calls

defaultAction

.

**Specified by:** visitConditionalExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitConditionalExpression

public

R

visitConditionalExpression​(

ConditionalExpressionTree

node,

P

p)

Visits a ConditionalExpressionTree node. This implementation calls

defaultAction

.

visitIf

```java
public
R
visitIf​(
IfTree
node,

P
p)
```

Visits an IfTree node. This implementation calls

defaultAction

.

**Specified by:** visitIf

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitIf

public

R

visitIf​(

IfTree

node,

P

p)

Visits an IfTree node. This implementation calls

defaultAction

.

visitExpressionStatement

```java
public
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)
```

Visits an ExpressionStatementTree node. This implementation calls

defaultAction

.

**Specified by:** visitExpressionStatement

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitExpressionStatement

public

R

visitExpressionStatement​(

ExpressionStatementTree

node,

P

p)

Visits an ExpressionStatementTree node. This implementation calls

defaultAction

.

visitBreak

```java
public
R
visitBreak​(
BreakTree
node,

P
p)
```

Visits a BreakTree node. This implementation calls

defaultAction

.

**Specified by:** visitBreak

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitBreak

public

R

visitBreak​(

BreakTree

node,

P

p)

Visits a BreakTree node. This implementation calls

defaultAction

.

visitContinue

```java
public
R
visitContinue​(
ContinueTree
node,

P
p)
```

Visits a ContinueTree node. This implementation calls

defaultAction

.

**Specified by:** visitContinue

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitContinue

public

R

visitContinue​(

ContinueTree

node,

P

p)

Visits a ContinueTree node. This implementation calls

defaultAction

.

visitReturn

```java
public
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node. This implementation calls

defaultAction

.

**Specified by:** visitReturn

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitReturn

public

R

visitReturn​(

ReturnTree

node,

P

p)

Visits a ReturnTree node. This implementation calls

defaultAction

.

visitThrow

```java
public
R
visitThrow​(
ThrowTree
node,

P
p)
```

Visits a ThrowTree node. This implementation calls

defaultAction

.

**Specified by:** visitThrow

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitThrow

public

R

visitThrow​(

ThrowTree

node,

P

p)

Visits a ThrowTree node. This implementation calls

defaultAction

.

visitAssert

```java
public
R
visitAssert​(
AssertTree
node,

P
p)
```

Visits an AssertTree node. This implementation calls

defaultAction

.

**Specified by:** visitAssert

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitAssert

public

R

visitAssert​(

AssertTree

node,

P

p)

Visits an AssertTree node. This implementation calls

defaultAction

.

visitMethodInvocation

```java
public
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)
```

Visits a MethodInvocationTree node. This implementation calls

defaultAction

.

**Specified by:** visitMethodInvocation

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitMethodInvocation

public

R

visitMethodInvocation​(

MethodInvocationTree

node,

P

p)

Visits a MethodInvocationTree node. This implementation calls

defaultAction

.

visitNewClass

```java
public
R
visitNewClass​(
NewClassTree
node,

P
p)
```

Visits a NewClassTree node. This implementation calls

defaultAction

.

**Specified by:** visitNewClass

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitNewClass

public

R

visitNewClass​(

NewClassTree

node,

P

p)

Visits a NewClassTree node. This implementation calls

defaultAction

.

visitNewArray

```java
public
R
visitNewArray​(
NewArrayTree
node,

P
p)
```

Visits a NewArrayTree node. This implementation calls

defaultAction

.

**Specified by:** visitNewArray

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitNewArray

public

R

visitNewArray​(

NewArrayTree

node,

P

p)

Visits a NewArrayTree node. This implementation calls

defaultAction

.

visitLambdaExpression

```java
public
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)
```

Visits a LambdaExpressionTree node. This implementation calls

defaultAction

.

**Specified by:** visitLambdaExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitLambdaExpression

public

R

visitLambdaExpression​(

LambdaExpressionTree

node,

P

p)

Visits a LambdaExpressionTree node. This implementation calls

defaultAction

.

visitParenthesized

```java
public
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)
```

Visits a ParenthesizedTree node. This implementation calls

defaultAction

.

**Specified by:** visitParenthesized

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitParenthesized

public

R

visitParenthesized​(

ParenthesizedTree

node,

P

p)

Visits a ParenthesizedTree node. This implementation calls

defaultAction

.

visitAssignment

```java
public
R
visitAssignment​(
AssignmentTree
node,

P
p)
```

Visits an AssignmentTree node. This implementation calls

defaultAction

.

**Specified by:** visitAssignment

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitAssignment

public

R

visitAssignment​(

AssignmentTree

node,

P

p)

Visits an AssignmentTree node. This implementation calls

defaultAction

.

visitCompoundAssignment

```java
public
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)
```

Visits a CompoundAssignmentTree node. This implementation calls

defaultAction

.

**Specified by:** visitCompoundAssignment

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitCompoundAssignment

public

R

visitCompoundAssignment​(

CompoundAssignmentTree

node,

P

p)

Visits a CompoundAssignmentTree node. This implementation calls

defaultAction

.

visitUnary

```java
public
R
visitUnary​(
UnaryTree
node,

P
p)
```

Visits a UnaryTree node. This implementation calls

defaultAction

.

**Specified by:** visitUnary

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitUnary

public

R

visitUnary​(

UnaryTree

node,

P

p)

Visits a UnaryTree node. This implementation calls

defaultAction

.

visitBinary

```java
public
R
visitBinary​(
BinaryTree
node,

P
p)
```

Visits a BinaryTree node. This implementation calls

defaultAction

.

**Specified by:** visitBinary

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitBinary

public

R

visitBinary​(

BinaryTree

node,

P

p)

Visits a BinaryTree node. This implementation calls

defaultAction

.

visitTypeCast

```java
public
R
visitTypeCast​(
TypeCastTree
node,

P
p)
```

Visits a TypeCastTree node. This implementation calls

defaultAction

.

**Specified by:** visitTypeCast

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitTypeCast

public

R

visitTypeCast​(

TypeCastTree

node,

P

p)

Visits a TypeCastTree node. This implementation calls

defaultAction

.

visitInstanceOf

```java
public
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)
```

Visits an InstanceOfTree node. This implementation calls

defaultAction

.

**Specified by:** visitInstanceOf

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitInstanceOf

public

R

visitInstanceOf​(

InstanceOfTree

node,

P

p)

Visits an InstanceOfTree node. This implementation calls

defaultAction

.

visitArrayAccess

```java
public
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)
```

Visits an ArrayAccessTree node. This implementation calls

defaultAction

.

**Specified by:** visitArrayAccess

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitArrayAccess

public

R

visitArrayAccess​(

ArrayAccessTree

node,

P

p)

Visits an ArrayAccessTree node. This implementation calls

defaultAction

.

visitMemberSelect

```java
public
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)
```

Visits a MemberSelectTree node. This implementation calls

defaultAction

.

**Specified by:** visitMemberSelect

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitMemberSelect

public

R

visitMemberSelect​(

MemberSelectTree

node,

P

p)

Visits a MemberSelectTree node. This implementation calls

defaultAction

.

visitMemberReference

```java
public
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)
```

Visits a MemberReferenceTree node. This implementation calls

defaultAction

.

**Specified by:** visitMemberReference

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitMemberReference

public

R

visitMemberReference​(

MemberReferenceTree

node,

P

p)

Visits a MemberReferenceTree node. This implementation calls

defaultAction

.

visitIdentifier

```java
public
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node. This implementation calls

defaultAction

.

**Specified by:** visitIdentifier

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitIdentifier

public

R

visitIdentifier​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node. This implementation calls

defaultAction

.

visitLiteral

```java
public
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits a LiteralTree node. This implementation calls

defaultAction

.

**Specified by:** visitLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitLiteral

public

R

visitLiteral​(

LiteralTree

node,

P

p)

Visits a LiteralTree node. This implementation calls

defaultAction

.

visitPrimitiveType

```java
public
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)
```

Visits a PrimitiveTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitPrimitiveType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitPrimitiveType

public

R

visitPrimitiveType​(

PrimitiveTypeTree

node,

P

p)

Visits a PrimitiveTypeTree node. This implementation calls

defaultAction

.

visitArrayType

```java
public
R
visitArrayType​(
ArrayTypeTree
node,

P
p)
```

Visits an ArrayTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitArrayType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitArrayType

public

R

visitArrayType​(

ArrayTypeTree

node,

P

p)

Visits an ArrayTypeTree node. This implementation calls

defaultAction

.

visitParameterizedType

```java
public
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)
```

Visits a ParameterizedTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitParameterizedType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitParameterizedType

public

R

visitParameterizedType​(

ParameterizedTypeTree

node,

P

p)

Visits a ParameterizedTypeTree node. This implementation calls

defaultAction

.

visitUnionType

```java
public
R
visitUnionType​(
UnionTypeTree
node,

P
p)
```

Visits a UnionTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitUnionType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitUnionType

public

R

visitUnionType​(

UnionTypeTree

node,

P

p)

Visits a UnionTypeTree node. This implementation calls

defaultAction

.

visitIntersectionType

```java
public
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)
```

Visits an IntersectionTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitIntersectionType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitIntersectionType

public

R

visitIntersectionType​(

IntersectionTypeTree

node,

P

p)

Visits an IntersectionTypeTree node. This implementation calls

defaultAction

.

visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)
```

Visits a TypeParameterTree node. This implementation calls

defaultAction

.

**Specified by:** visitTypeParameter

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitTypeParameter

public

R

visitTypeParameter​(

TypeParameterTree

node,

P

p)

Visits a TypeParameterTree node. This implementation calls

defaultAction

.

visitWildcard

```java
public
R
visitWildcard​(
WildcardTree
node,

P
p)
```

Visits a WildcardTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitWildcard

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitWildcard

public

R

visitWildcard​(

WildcardTree

node,

P

p)

Visits a WildcardTypeTree node. This implementation calls

defaultAction

.

visitModifiers

```java
public
R
visitModifiers​(
ModifiersTree
node,

P
p)
```

Visits a ModifiersTree node. This implementation calls

defaultAction

.

**Specified by:** visitModifiers

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitModifiers

public

R

visitModifiers​(

ModifiersTree

node,

P

p)

Visits a ModifiersTree node. This implementation calls

defaultAction

.

visitAnnotation

```java
public
R
visitAnnotation​(
AnnotationTree
node,

P
p)
```

Visits an AnnotatedTree node. This implementation calls

defaultAction

.

**Specified by:** visitAnnotation

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitAnnotation

public

R

visitAnnotation​(

AnnotationTree

node,

P

p)

Visits an AnnotatedTree node. This implementation calls

defaultAction

.

visitAnnotatedType

```java
public
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)
```

Visits an AnnotatedTypeTree node. This implementation calls

defaultAction

.

**Specified by:** visitAnnotatedType

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitAnnotatedType

public

R

visitAnnotatedType​(

AnnotatedTypeTree

node,

P

p)

Visits an AnnotatedTypeTree node. This implementation calls

defaultAction

.

visitOther

```java
public
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

hierarchy. This implementation calls

defaultAction

.

**Specified by:** visitOther

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction

---

#### visitOther

public

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

hierarchy. This implementation calls

defaultAction

.

---

